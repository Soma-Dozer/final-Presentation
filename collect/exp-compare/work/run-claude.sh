#!/usr/bin/env bash
# usage: run-claude.sh <arm:B1|B2> <case_id> <owner/repo> <login> <position>
set -uo pipefail
ARM=$1; CASE=$2; REPO=$3; LOGIN=$4; POS=$5
W=/Users/aiden/dev/teams/ASM/last-dance/collect/exp-compare/work
OUT=$W/../raw/claude
C=/private/tmp/claude-501/-Users-aiden-dev-teams-ASM/44e5b55b-bef1-4a3a-8ba1-583a405dcd7e/scratchpad/exp-clones
JD=$(python3 -c "import json,sys;print(json.load(open('$W/jd.json'))['$POS'])")
PROMPT="레포: https://github.com/$REPO

이 레포와 아래 채용공고로, 이 레포 작성자 \`$LOGIN\`에게 물을 기술면접 질문 8개를 만들어라. 각 질문마다 근거(커밋 SHA, 파일 경로, 코드 줄)를 붙여라. JSON 배열로: [{question, commit_sha, file_path, code_quote}]

[채용공고]
$JD"
printf '%s' "$PROMPT" > $W/prompts/$ARM-$CASE.txt
if [ "$ARM" = B1 ]; then
  cd "$C/${REPO#*/}"
  claude -p "$PROMPT" --output-format json --no-session-persistence --strict-mcp-config \
    --setting-sources project,local \
    --tools Read Grep Glob Bash \
    --allowedTools Read Grep Glob 'Bash(git log:*)' 'Bash(git show:*)' 'Bash(git blame:*)' 'Bash(git ls-files:*)' 'Bash(git rev-parse:*)' 'Bash(ls:*)' \
    > $OUT/$ARM-$CASE.json 2> $OUT/$ARM-$CASE.err
else
  mkdir -p $C/empty && cd $C/empty
  claude -p "$PROMPT" --output-format json --no-session-persistence --strict-mcp-config \
    --setting-sources project,local --tools "" \
    > $OUT/$ARM-$CASE.json 2> $OUT/$ARM-$CASE.err
fi
echo "$ARM $CASE exit=$?"
