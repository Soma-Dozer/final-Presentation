#!/usr/bin/env python3
"""블라인드 채점지 생성. 내용은 고치지 않고 형식만 통일한다.

형식 통일 규칙 (세 군에 똑같이 적용):
  1. 줄바꿈·연속 공백 → 공백 1칸, 앞뒤 공백 제거
  2. 레포 이름(owner/repo, repo 이름, 하이픈·공백 변형) → «[프로젝트]» (레포 맞히기 문항이 이름으로 풀리지 않게)
  3. 맨 앞의 «[프로젝트] 프로젝트에서(는)» 머리말 제거 (DevFit 고유 문체 단서)
  4. 마크다운 백틱 제거
  5. 본문의 커밋 SHA(hex 7~40자) → «[커밋]» (B1만 SHA를 본문에 적는 문체 단서)
출력: ../blind-sheet.csv (평가자용), ../answer-key.csv (집계용, 평가자에게 주지 말 것)
"""
import csv
import json
import random
import re
from pathlib import Path

WORK = Path(__file__).resolve().parent
OUT = WORK.parent
SEED = 20261105

REPO_CHOICE = {
    "aidengoldkr/Signify": "Signify",
    "aidengoldkr/Ddareungi-Navigation-Kakao-ChatBot": "Ddareungi",
    "aidengoldkr/Aiden-WEB": "Aiden-WEB",
    "pallets/itsdangerous": "itsdangerous",
}


def name_patterns(repo):
    name = repo.split("/")[-1]
    pats = {repo, name, name.replace("-", " "), name.replace("-", "")}
    if "Ddareungi" in name:
        pats |= {"Ddareungi-Navigation", "Ddareungi Navigation", "Ddareungi", "따릉이 네비게이션 챗봇"}
    return sorted(pats, key=len, reverse=True)


def normalize(q, repo):
    t = re.sub(r"\s+", " ", q or "").strip().replace("`", "")
    for p in name_patterns(repo):
        t = re.sub(re.escape(p), "[프로젝트]", t, flags=re.I)
    # 본문에 박힌 커밋 SHA(7~40자 hex, 숫자 포함)는 B1 고유 문체라 «[커밋]»으로 바꾼다.
    t = re.sub(r"(?<![0-9A-Za-z])(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}(?![0-9A-Za-z])", "[커밋]", t)
    t = re.sub(r"^\[프로젝트\]\s*(프로젝트)?\s*(에서는|에서|은|는)\s*,?\s*", "", t)
    return t


def main():
    items = [json.loads(l) for l in (WORK / "items.jsonl").read_text().splitlines() if l.strip()]
    rng = random.Random(SEED)
    rng.shuffle(items)
    choices = " / ".join(REPO_CHOICE.values())
    with open(OUT / "blind-sheet.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "question", "rater", f"이식성(예/아니오)",
                    "실제 면접에서 쓰겠나(쓰겠다/모르겠다/안 쓰겠다)", f"어느 레포({choices})"])
        for i, it in enumerate(items, 1):
            w.writerow([f"Q{i:03d}", normalize(it["question"], it["repo"]), "", "", "", ""])
    with open(OUT / "answer-key.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "item_id", "arm", "case_id", "repo_answer"])
        for i, it in enumerate(items, 1):
            w.writerow([f"Q{i:03d}", it["item_id"], it["arm"], it["case_id"], REPO_CHOICE[it["repo"]]])
    print(len(items), "items")


if __name__ == "__main__":
    main()
