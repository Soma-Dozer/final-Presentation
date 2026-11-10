#!/usr/bin/env python3
"""세 군의 원출력을 같은 모양(items.jsonl)으로 맞춘다. 질문 본문은 건드리지 않는다.

A(DevFit) 선택 규칙 — 체리피킹 없음:
  하네스가 덤프한 순서(= StudyQuestion difficulty ASC, id ASC — 제품 저장소 조회 순서) 그대로,
  LLM이 만든 본 질문(generation_source가 결정론 code-reading/부재 질문이 아닌 것)만 앞에서 8개.
  꼬리질문(follow_ups)은 쓰지 않는다. 결정론 질문은 별도 표(보조)로만 센다.
A의 근거 필드 매핑:
  commit_sha = commit_hash, file_path = primary_source_file,
  code_quote = primary_source_diff(서버가 모델에 보낸 패치)에서 '+' 추가 줄 중
               질문 앵커를 가장 많이 포함한 줄 1개(동점이면 먼저 나온 줄). 앵커가 하나도 안 맞으면
               첫 번째 비어있지 않은 추가 줄. 즉 «서버가 보여 준 근거가 실제 파일에 있는가»를 잰다.
B1/B2: 모델이 낸 JSON 배열의 앞 8개를 그대로.
"""
import json
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
RAW = WORK.parent / "raw"
sys.path.insert(0, str(WORK))
from score import anchors, project_tokens  # noqa: E402

CASES = {c["id"]: c for c in json.loads((WORK / "spec.json").read_text())["cases"]}


def repo_of(case):
    return CASES[case]["repoUrl"].replace("https://github.com/", "")


def is_llm_main(q):
    src = (q.get("generation_source") or "").lower()
    return not any(k in src for k in ("code-reading", "code_reading", "codereading", "absence", "deterministic", "rule"))


def pick_quote(diff, question, repo):
    adds = []
    for ln in (diff or "").splitlines():
        if ln.startswith("+") and not ln.startswith("+++"):
            s = ln[1:].strip()
            if s:
                adds.append(s)
    if not adds:
        return ""
    anc = anchors(question, project_tokens(repo))
    best, best_n = adds[0], 0
    for s in adds:
        n = sum(1 for a in anc if a in s.lower())
        if n > best_n:
            best, best_n = s, n
    return best


def devfit_items():
    out, extra = [], []
    path = RAW / "devfit" / "questions.jsonl"
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    by_case = {}
    for r in rows:
        by_case.setdefault(r["case_id"], []).append(r)
    for case, qs in by_case.items():
        repo = repo_of(case)
        main = [q for q in qs if is_llm_main(q)]
        for rank, q in enumerate(main):
            item = {
                "arm": "A", "case_id": case, "repo": repo, "login": CASES[case]["login"],
                "rank": rank + 1, "question": q["question"], "commit_sha": q.get("commit_hash"),
                "file_path": q.get("primary_source_file"),
                "code_quote": pick_quote(q.get("primary_source_diff"), q["question"], repo),
                "type": q.get("type"), "difficulty": q.get("difficulty"),
                "generation_source": q.get("generation_source"),
            }
            (out if rank < 8 else extra).append(item)
    return out, extra


def parse_claude(path):
    doc = json.loads(path.read_text())
    text = doc.get("result", "")
    m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.S)
    blob = m.group(1) if m else text[text.find("["): text.rfind("]") + 1]
    try:
        arr = json.loads(blob)
    except Exception:
        arr = []
    return doc, arr


def claude_items(arm):
    out, meta = [], {}
    for case in CASES:
        p = RAW / "claude" / f"{arm}-{case}.json"
        if not p.exists() or p.stat().st_size == 0:
            meta[case] = {"error": "no output"}
            continue
        doc, arr = parse_claude(p)
        meta[case] = {"parsed": len(arr), "models": list((doc.get("modelUsage") or {}).keys()),
                      "num_turns": doc.get("num_turns"), "cost_usd": doc.get("total_cost_usd"),
                      "duration_ms": doc.get("duration_ms"), "is_error": doc.get("is_error")}
        repo = repo_of(case)
        for rank, q in enumerate(arr[:8]):
            out.append({"arm": arm, "case_id": case, "repo": repo, "login": CASES[case]["login"],
                        "rank": rank + 1, "question": q.get("question", ""),
                        "commit_sha": str(q.get("commit_sha") or ""),
                        "file_path": str(q.get("file_path") or ""),
                        "code_quote": str(q.get("code_quote") or "")})
    return out, meta


def main():
    a, a_extra = devfit_items()
    b1, m1 = claude_items("B1")
    b2, m2 = claude_items("B2")
    items = a + b1 + b2
    for i, it in enumerate(items):
        it["item_id"] = f"{it['arm']}-{it['case_id']}-{it['rank']}"
    with open(WORK / "items.jsonl", "w") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    with open(WORK / "items_devfit_beyond8.jsonl", "w") as f:
        for it in a_extra:
            it["item_id"] = f"A-{it['case_id']}-{it['rank']}"
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    (RAW / "claude-meta.json").write_text(json.dumps({"B1": m1, "B2": m2}, ensure_ascii=False, indent=2))
    print(len(a), len(a_extra), len(b1), len(b2))
    print(json.dumps({"B1": m1, "B2": m2}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
