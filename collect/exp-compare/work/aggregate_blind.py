#!/usr/bin/env python3
"""사람 채점 집계. 평가자마다 blind-sheet.csv를 복사해 채운 파일을 인자로 준다.

  python3 -I aggregate_blind.py ../answer-key.csv rater1.csv rater2.csv rater3.csv

각 파일의 rater 칸이 비어 있으면 파일 이름을 평가자 이름으로 쓴다.
출력: 군별(A=DevFit, B1=Claude Code+clone, B2=Claude 도구 없음) ×
  이식성 '예' 비율 / '쓰겠다' 비율 / '안 쓰겠다' 비율 / 레포 맞히기 정답률(우연 25%), n,
  그리고 평가자 쌍별 정확 일치율.
빈 칸은 분모에서 뺀다(응답한 칸만 센다).
"""
import csv
import itertools
import sys
from collections import defaultdict
from pathlib import Path


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def col(row, prefix):
    for k, v in row.items():
        if k and k.startswith(prefix):
            return (v or "").strip()
    return ""


def main():
    key = {r["id"]: r for r in load(sys.argv[1])}
    raters = {}
    for p in sys.argv[2:]:
        rows = load(p)
        name = next((r["rater"] for r in rows if r.get("rater")), Path(p).stem)
        raters[name] = {r["id"]: r for r in rows}
    stats = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for name, rows in raters.items():
        for qid, r in rows.items():
            if qid not in key:
                continue
            arm = key[qid]["arm"]
            for a in (arm, "ALL"):
                s = stats[a]
                port = col(r, "이식성")
                if port:
                    s["이식성=예"][1] += 1
                    s["이식성=예"][0] += port.startswith("예")
                use = col(r, "실제 면접")
                if use:
                    for lab in ("쓰겠다", "모르겠다", "안 쓰겠다"):
                        s[lab][1] += 1
                        s[lab][0] += (use.replace(" ", "") == lab.replace(" ", ""))
                guess = col(r, "어느 레포")
                if guess:
                    s["레포 맞히기"][1] += 1
                    s["레포 맞히기"][0] += guess.lower() == key[qid]["repo_answer"].lower()
    for arm in ("A", "B1", "B2", "ALL"):
        if arm not in stats:
            continue
        parts = [f"{m} {k}/{n} ({k / n:.0%})" for m, (k, n) in stats[arm].items() if n]
        print(arm, " | ".join(parts))
    names = list(raters)
    for x, y in itertools.combinations(names, 2):
        for prefix in ("이식성", "실제 면접", "어느 레포"):
            same = tot = 0
            for qid in key:
                a, b = col(raters[x].get(qid, {}), prefix), col(raters[y].get(qid, {}), prefix)
                if a and b:
                    tot += 1
                    same += a == b
            if tot:
                print(f"일치 {x}-{y} {prefix}: {same}/{tot} ({same / tot:.0%})")


if __name__ == "__main__":
    main()
