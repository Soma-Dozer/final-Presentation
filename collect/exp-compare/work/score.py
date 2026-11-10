#!/usr/bin/env python3
"""DevFit vs Claude Code 파일럿 — 결정론 채점 (LLM 0회).

입력: work/items.jsonl (normalize.py가 세 군의 출력을 같은 모양으로 맞춘 것)
  {item_id, arm, case_id, repo, login, question, commit_sha, file_path, code_quote}
출력: ../raw/scored.jsonl, ../raw/metrics.json, 표준출력 표

판정 규칙 (E-compare.md §채점 정의와 같다):
  sha_ok     : git rev-parse --verify <sha>^{commit} 성공 (짧은 SHA 허용, 모호하면 실패)
  file_ok    : sha_ok 이고 <sha>:<path> 또는 <sha>^:<path>가 blob (삭제 커밋 허용)
  touched    : sha_ok 이고 그 커밋이 그 파일을 실제로 바꿨다 (git show --name-only)
  quote_ok   : file_ok 이고 인용의 모든 비어있지 않은 줄(diff 마커 +/- 제거, '...' 줄 제외)이
               공백 정규화 후 그 시점 파일(<sha>) 또는 직전 시점(<sha>^) 본문에 부분문자열로 있다
  (경로 뒤 줄 범위 표기 `:12-30`·`#L12-L30`은 떼고 본다)
  evidence_ok: sha_ok & file_ok & quote_ok 셋 다
  own_strict : 커밋 author login == login (GitHub API)
  own_coauth : own_strict 또는 커밋 메시지 Co-authored-by 줄에 login 포함 (DevFit의 0.70 규칙과 같은 취급)
  anchored   : 질문 앵커(QuestionGrounding 정규식) 중 ≥1개가 그 레포 전체 이력(git log -p --all + 경로)에 있다
  specific   : anchored 중 그 앵커가 이 실험의 다른 레포 3개 어디에도 없다
  portable   : specific 앵커가 0개 (이식성 proxy — 다른 레포에 그대로 물어도 말이 되는 질문일 가능성)
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

WORK = Path(__file__).resolve().parent
CLONES = WORK / "clones"
RAW = WORK.parent / "raw"

IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
NUMBER = re.compile(r"(?<![0-9A-Za-z_.])\d+(?:\.\d+)?(?![0-9A-Za-z_])")
STOP = {"the", "and", "for", "with", "this", "that", "http", "https", "com", "www",
        "api", "true", "false", "null", "none", "int", "str", "var", "let", "const",
        "return", "import", "from", "class", "def", "func", "public", "private"}
TRIVIAL = {"1", "2", "3", "0", "10", "100"}


def project_tokens(full):
    full = full.lower()
    name = full.split("/")[-1]
    out = {full, name}
    out |= {p for p in re.split(r"[\s_-]+", name) if len(p) >= 3}
    out.discard("")
    return out


def anchors(text, excluded):
    out = []
    for m in IDENT.finditer(text or ""):
        raw = m.group()
        if len(raw) < 4:
            continue
        t = raw.lower()
        if t in STOP or t in excluded:
            continue
        if any(len(p) >= 4 and p in t for p in excluded):
            continue
        out.append(t)
    for m in NUMBER.finditer(text or ""):
        if m.group() not in TRIVIAL:
            out.append(m.group())
    return list(dict.fromkeys(out))


def git(repo_dir, *args):
    r = subprocess.run(["git", "-C", str(repo_dir), *args], capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


_corpus_cache = {}


def repo_corpus(name):
    if name not in _corpus_cache:
        _, log = git(CLONES / name, "log", "-p", "--all", "--format=%H%n%B")
        _, paths = git(CLONES / name, "log", "--all", "--name-only", "--format=")
        _, head = git(CLONES / name, "grep", "-I", "-h", "", "HEAD")
        _corpus_cache[name] = (log + "\n" + paths + "\n" + head).lower()
    return _corpus_cache[name]


_login_cache = {}


def commit_login(repo, sha):
    key = (repo, sha)
    if key not in _login_cache:
        r = subprocess.run(["gh", "api", f"repos/{repo}/commits/{sha}", "--jq", ".author.login // \"\""],
                           capture_output=True)
        _login_cache[key] = r.stdout.decode().strip() if r.returncode == 0 else ""
    return _login_cache[key]


def quote_lines(q):
    lines = []
    for ln in (q or "").splitlines():
        s = ln.strip()
        if s.startswith(("+", "-")) and not s.startswith(("++", "--")):
            s = s[1:]
        s = ws(s)
        if not s or set(s) <= {".", "…"} or s in ("...", "…"):
            continue
        lines.append(s)
    return lines


def clean_path(p):
    """경로 뒤에 붙은 줄 범위 표기(`:106-108`, `:22-28, 39-41`, `#L161-L199`)만 떼어낸다."""
    p = (p or "").strip()
    p = re.sub(r"#L\d+(-L?\d+)?$", "", p)
    p = re.sub(r":\d+(-\d+)?(,\s*\d+(-\d+)?)*$", "", p)
    if p.startswith("./"):
        p = p[2:]
    return p


def score_item(it, all_repos):
    name = it["repo"].split("/")[-1]
    d = CLONES / name
    res = dict(it)
    sha = (it.get("commit_sha") or "").strip()
    path = clean_path(it.get("file_path"))
    full = ""
    res["sha_ok"] = False
    if re.fullmatch(r"[0-9a-fA-F]{7,40}", sha):
        rc, out = git(d, "rev-parse", "--verify", "--quiet", sha + "^{commit}")
        if rc == 0:
            full = out.strip()
            res["sha_ok"] = True
    res["full_sha"] = full
    res["file_ok"] = res["touched"] = res["quote_ok"] = False
    blob_texts = []
    if full and path:
        for ref in (full, full + "^"):
            rc, txt = git(d, "show", f"{ref}:{path}")
            if rc == 0:
                blob_texts.append(ws(txt))
        res["file_ok"] = bool(blob_texts)
        # 머지 커밋은 combined diff가 비므로 첫 부모 기준으로 본다.
        _, names = git(d, "show", "-m", "--first-parent", "--name-only", "--format=", full)
        res["touched"] = path in names.split()
    ql = quote_lines(it.get("code_quote"))
    res["quote_line_count"] = len(ql)
    if blob_texts and ql:
        # 각 줄이 커밋 시점 또는 직전 시점 파일 중 하나에 있으면 된다(diff의 '-' 줄은 직전 시점에만 있다).
        res["quote_ok"] = all(any(l in b for b in blob_texts) for l in ql)
        res["quote_masked"] = any(re.search(r"<[^<>]*(KEY|키|REDACTED|redacted)[^<>]*>", l) for l in ql)
    res["evidence_ok"] = res["sha_ok"] and res["file_ok"] and res["quote_ok"]
    # 본인 작성
    res["author_login"] = commit_login(it["repo"], full) if full else ""
    res["own_strict"] = bool(full) and res["author_login"].lower() == it["login"].lower()
    coauth = False
    if full:
        _, msg = git(d, "log", "-1", "--format=%B", full)
        coauth = any(l.lower().startswith("co-authored-by:") and it["login"].lower() in l.lower()
                     for l in msg.splitlines())
    res["own_coauth"] = res["own_strict"] or coauth
    # 앵커
    # 질문 본문에 적힌 커밋 SHA 조각(예: ec1bf5b, 2a7cea1→a7cea1)은 코드 앵커로 세지 않는다.
    anc = [a for a in anchors(it["question"], project_tokens(it["repo"]))
           if not (re.fullmatch(r"[0-9a-f]{6,40}", a) and re.search(r"\d", a))]
    corpus = repo_corpus(name)
    in_repo = [a for a in anc if a in corpus]
    others = [r for r in all_repos if r != it["repo"]]
    specific = [a for a in in_repo if not any(a in repo_corpus(o.split("/")[-1]) for o in others)]
    res["anchors"] = anc
    res["anchors_in_repo"] = in_repo
    res["anchors_specific"] = specific
    res["anchored"] = bool(in_repo)
    res["portable"] = not specific
    return res


METRICS = ["sha_ok", "file_ok", "touched", "quote_ok", "evidence_ok",
           "own_strict", "own_coauth", "anchored", "portable"]


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else WORK / "items.jsonl"
    tag = sys.argv[2] if len(sys.argv) > 2 else ""
    items = [json.loads(l) for l in src.read_text().splitlines() if l.strip()]
    # 레포 고유 앵커 판정의 비교군은 항상 실험 레포 4개 전부다.
    repos = sorted(c["repoUrl"].replace("https://github.com/", "")
                   for c in json.loads((WORK / "spec.json").read_text())["cases"])
    scored = [score_item(i, repos) for i in items]
    with open(RAW / f"scored{tag}.jsonl", "w") as f:
        for s in scored:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    groups = defaultdict(list)
    for s in scored:
        groups[(s["arm"], s["case_id"])].append(s)
        groups[(s["arm"], "ALL")].append(s)
    table = {}
    for (arm, case), rows in sorted(groups.items()):
        n = len(rows)
        table[f"{arm}|{case}"] = {"n": n, **{m: sum(r[m] for r in rows) for m in METRICS}}
    (RAW / f"metrics{tag}.json").write_text(json.dumps(table, ensure_ascii=False, indent=2))
    hdr = ["arm", "case", "n"] + METRICS
    print("\t".join(hdr))
    for k, v in table.items():
        arm, case = k.split("|")
        print("\t".join([arm, case, str(v["n"])] + [f"{v[m]}/{v['n']}" for m in METRICS]))


if __name__ == "__main__":
    sys.exit(main())
