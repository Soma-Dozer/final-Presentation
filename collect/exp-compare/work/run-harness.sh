#!/usr/bin/env bash
# 질문 품질 평가 코퍼스 생성기 실행기.
#
#   evaluation/scripts/run-harness.sh <corpus.json> <out-dir> [aws-profile]
#
# 프로덕션 질문 생성 파이프라인(GithubService → EpisodeCatalogService → QuestionBankService)을
# 그대로 호출한다. 실제 GitHub API와 실제 Bedrock을 쓰므로 비용이 든다.
#
# 자격증명은 파일에 쓰지 않는다 — 실행 시점에 aws CLI에서 읽어 프로세스 환경으로만 넘긴다.
set -euo pipefail

SPEC="${1:?corpus json path required}"
OUT="${2:?output dir required}"
PROFILE="${3:-asm}"

BE="/Users/aiden/dev/teams/ASM/last-dance/collect/exp-compare/work/devfit-be-prod"

# ~/.aws/config의 login_session 프로필은 Java SDK가 만료된 로그인 세션으로 해석해 실패한다.
# CLI가 해석한 정적 자격증명을 환경변수로 넘겨 DefaultCredentialsProvider가 집게 한다.
eval "$(aws configure export-credentials --profile "$PROFILE" --format env)"

mkdir -p "$OUT"
cd "$BE"
DEVFIT_EVAL=1 \
DEVFIT_EVAL_SPEC="$SPEC" \
DEVFIT_EVAL_OUT="$OUT" \
DEVFIT_EVAL_AWS_PROFILE="" \
AWS_REGION="${AWS_REGION:-us-east-1}" \
GITHUB_EVAL_TOKEN="${GITHUB_EVAL_TOKEN:-$(gh auth token)}" \
./gradlew evalHarness --tests '*QuestionQualityHarness*' "${@:4}"
