# E. DevFit과 Claude Code 비교 파일럿 (실측)

> 실행: 2026-11-05 00:43~01:30 KST (UTC 2026-11-04 15:43~) · 프로토콜은 `C-quality.md` §3-2를 따랐고, 바꾼 점은 아래 §1-5에 적었다.
> 원출력과 스크립트는 `last-dance/collect/exp-compare/`에 있다(§7). 결정론 채점에는 LLM을 쓰지 않았다(0회).
> ⚠️ **파일럿이다.** 레포 4개, 군마다 1회 실행, 군별 n=18~32다. 승률로 쓰지 말고 비율과 n을 같이 적는다.

---

## 요약

**결정론 지표 (근거 필드를 클론한 레포와 `git`으로 대조, n은 문항 수)**

| 군 | n | SHA 실존 | 파일 실존 | 인용 코드 실존 | 근거 3종 모두 실존 | 본인 커밋 | 코드 앵커 있음 | 레포 고유 앵커 없음(이식성 proxy) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A. DevFit (prod `500f4af`) | 28 | 28 (100%) | 28 (100%) | 28 (100%)* | 28 (100%) | 28 (100%) | 21 (75%) | 12 (43%) |
| B1. Claude Code + clone | 32 | 32 (100%) | 32 (100%) | 30 (94%)** | 30 (94%) | 32 (100%) | 32 (100%) | 2 (6%) |
| B2. Claude, 도구 없음 (링크만) | 18 | **0 (0%)** | 0 (0%) | 0 (0%) | **0 (0%)** | 0 (0%) | 18 (100%)*** | 7 (39%) |

\* DevFit은 인용 칸이 따로 없다. 그래서 서버가 모델에 보낸 패치에서 한 줄을 골라 인용으로 썼다(§2). 이 값은 **정의상 거의 100%가 된다.** 비교에 쓰면 안 된다.
\** 실패 2건은 Claude Code가 API 키를 `<KEY>`, `<원래 키 값>`으로 **일부러 가린** 인용이다. 지어낸 인용은 0건이다.
\*** B2의 앵커는 `requests`, `timeout`처럼 흔한 단어가 레포에 우연히 있어서 맞은 경우다. 실제로 B2 코드는 지어낸 것이다(§4-1). 이 행은 이 지표의 한계를 보여 준다.

**결론 3줄**
1. 레포를 clone하고 git을 읽게 하면 **Claude Code도 근거를 거의 정확하게 붙인다**(30/32). 작성자 로그인을 알려 주면 남의 커밋도 걸러 낸다(itsdangerous `mitsuhiko` 8/8). 이 두 지표로는 DevFit이 이겼다고 말할 수 없다.
2. 레포를 읽지 못하는 범용 AI(B2)는 **근거 18개를 모두 지어냈다.** «레포를 확인해 보니»라고 쓰고는 없는 커밋·파일·코드를 만들어 냈다. 그 레포가 «비어 있다», «남의 README뿐이다»라는 거짓 판정도 2건 나왔다. «링크만 주면 된다»는 반론은 실측으로 반박된다.
3. 질문이 코드 식별자를 직접 짚는 비율(구체성 proxy)은 **Claude Code가 DevFit보다 높았다**(레포 고유 앵커 있음 30/32 대 16/28). 그래서 DevFit의 차별점은 «더 정확한 질문»이 아니다. 「분석 절차를 사용자 대신 서버가 강제한다」와 「공고 단위 제품 흐름」으로 말해야 한다. 질문 품질의 승패는 사람 채점이 끝나기 전까지 미정이다.

**장표용 한 줄 (결과와 관계없이 참인 문장)**

> «같은 공개 레포 4개·같은 공고·같은 지시로 돌린 파일럿(78문항)에서 링크만 받은 범용 AI는 근거 18개를 모두 지어냈습니다(0/18 실존). 레포를 직접 읽은 Claude Code는 30/32, DevFit은 28/28이 실존했습니다. 차이는 모델이 아니라 **레포를 실제로 읽고 대조하는 절차**에서 납니다. DevFit은 그 절차를 사용자가 프롬프트를 짜지 않아도 서버가 매번 강제합니다.»

- 쓰면 안 되는 문장: «DevFit 질문이 Claude Code보다 정확하다/구체적이다». 근거 실존은 비슷했고, 구체성 proxy는 Claude Code가 높았다.

---

## 1. 설정

### 1-1. 입력 (고정)

| case_id | 레포 (공개, 2026-11-05 `gh api`로 확인) | 로그인 | 공고 | 레포 HEAD | 커밋 수 (전체 / 로그인 본인) |
|---|---|---|---|---|---|
| fe-signify | `aidengoldkr/Signify` (TS FE) | aidengoldkr | FE | `f3b3f54` | 9 / 9 |
| py-ddareungi | `aidengoldkr/Ddareungi-Navigation-Kakao-ChatBot` (Python BE) | aidengoldkr | BE | `9a7ee58` | 4 / 4 (2개는 author 이름이 «Kunwoo Kim», 같은 이메일) |
| fe-aiden-web | `aidengoldkr/Aiden-WEB` (TS FE) | aidengoldkr | FE | `29c9835` | 20 / 20 |
| oss-itsdangerous | `pallets/itsdangerous` (다수 작성자 OSS, 본인 커밋 필터 시험용) | **mitsuhiko** | BE | `672971d` | 677 / 91 (davidism 341 등 다른 기여자가 다수) |

- itsdangerous를 고른 이유: 작고(약 0.9MB), 기여자가 여럿이며, 지정 로그인의 커밋이 전체의 약 14%뿐이다. caddy는 클론 비용이 커서 뺐다.
- 공고는 포지션마다 1개로 고정했다. 두 군과 네 레포에 같은 문구를 넣었다(`exp-compare/work/jd.json`). `Devfit/evaluation/corpus/main-a.json`의 JD를 조합해 다시 썼다.
  - **FE**: «[모집부문] 프론트엔드 엔지니어(신입) [주요업무] React/Next.js 기반 웹 서비스 화면 개발, 사용자 입력 처리와 상태 관리 설계, 외부 API 연동, 접근성과 성능 최적화 [자격요건] TypeScript 이해, React 컴포넌트 설계 경험, HTTP/브라우저 동작 이해 [우대사항] SSR/정적 배포 경험, 브라우저 API(Canvas·Pointer Events 등) 활용 경험, 테스트 작성 경험»
  - **BE**: «[모집부문] 백엔드 개발자(신입) [주요업무] Python 기반 서버·라이브러리 개발, 외부 API 연동, 인증 토큰·서명 등 보안 관련 로직 구현, 서버리스/클라우드 배포 운영 [자격요건] Python 이해, REST API와 HTTP 이해 [우대사항] 오픈소스 기여 경험, 테스트 코드 작성 습관, AWS Lambda 등 서버리스 배포 경험»

### 1-2. A군: DevFit

- 코드: `Devfit_BE` **`origin/prod` = `500f4af`**(2026-11-03, PR #163 병합)를 `git archive`로 깨끗하게 꺼냈다. 원본 저장소는 건드리지 않았다(checkout·stash·build·worktree 0회).
  ```bash
  git -C Devfit/Devfit_BE archive origin/prod | tar -x -C last-dance/collect/exp-compare/work/devfit-be-prod
  ```
- 실행기: `Devfit/evaluation/scripts/run-harness.sh`를 `work/run-harness.sh`로 복사했다. 바꾼 것은 `BE=` 경로 한 줄뿐이다.
  ```bash
  cd last-dance/collect/exp-compare/work
  ./run-harness.sh $PWD/spec.json $PWD/../raw/devfit asm
  ```
  AWS 자격증명은 `aws configure export-credentials --profile asm`으로 프로세스 환경에만 넘겼고, GitHub 토큰은 `gh auth token`을 썼다. 파일이나 로그에는 쓰지 않았다.
- 하네스는 `QuestionQualityHarness`다. 운영 `CandidateAnalysisPipeline`과 같은 `GithubService.indexRepository` → `EpisodeCatalogService.buildAndStore` → `QuestionBankService.generateAndStore` → `CodeReadingQuestionService`를 부른다. 계정·크레딧·토큰 암호화만 우회한다.
- **모드**: B2C 기본 경로다. 이 경로는 `AnalysisMode`를 받지 않는다(`AnalysisMode`는 `extractSnippets`에만 있고, prod에서는 호출처가 없다. `C-quality.md` §5). 근거 선별은 결정론이고, 질문 생성 LLM은 `zai.glm-5`다(Bedrock 호출 34회, temperature 0.2). `questions-version: 13`, `evidence-patch-lines: 72`.
- 빌드·실행: Gradle `evalHarness`, BUILD SUCCESSFUL in 8m 9s(컴파일 포함). JDK 21.0.11.
- 레포별 결과: Signify 8문항(72s) · Ddareungi **4문항**(33s) · Aiden-WEB 11문항(137s) · itsdangerous 25문항(226s). 결정론 코드 읽기 질문은 4레포 모두 0개였다. 4레포 모두 `partial=true`이고 경고는 «품질 기준 미달 꼬리질문/예상 질문 1~3개 제외»다.
- **선택 규칙(체리피킹 없음)**: 하네스가 덤프한 순서(`difficulty ASC, id ASC`)대로 LLM 본 질문을 앞에서부터 최대 8개 골랐다. 꼬리질문은 넣지 않았다. Ddareungi는 4개뿐이라 n=4다. 8개를 넘는 20문항(Aiden-WEB 3, itsdangerous 17)도 따로 채점했는데 결과가 같았다(§3-2).
- 비용: Bedrock 비용은 측정하지 못했다. 하네스에 users 행이 없어 `llm_usage_event` 기록이 FK 위반으로 실패했다(질문 생성과는 무관한 경고다). 호출 수(34회)만 확인했다.

### 1-3. B1군: Claude Code + clone

- Claude Code **2.1.318**, 모델 **`claude-opus-5-5`**(결과 JSON의 `modelUsage`로 확인), 2026-11-05 실행.
- clone 위치는 `/private/tmp/claude-501/-Users-aiden-dev-teams-ASM/44e5b55b-bef1-4a3a-8ba1-583a405dcd7e/scratchpad/exp-clones/<repo>`다. ASM의 `CLAUDE.md`가 끼어들지 않게 ASM 밖에 두었다.
- 명령(`work/run-claude.sh`):
  ```bash
  cd exp-clones/<repo>
  claude -p "$PROMPT" --output-format json --no-session-persistence --strict-mcp-config \
    --setting-sources project,local \
    --tools Read Grep Glob Bash \
    --allowedTools Read Grep Glob 'Bash(git log:*)' 'Bash(git show:*)' 'Bash(git blame:*)' \
                   'Bash(git ls-files:*)' 'Bash(git rev-parse:*)' 'Bash(ls:*)'
  ```
  읽기 전용 도구만 허용했다. 허용 목록 밖의 Bash 명령(`cat`, 파이프·`cd` 조합 등)은 자동으로 거부됐다. 레포별 거부는 Signify 2, Ddareungi 2, Aiden-WEB 2, itsdangerous 1건이다. 4레포 모두 거부 이후에도 8문항을 끝까지 냈다.
- 프롬프트는 군과 레포에 관계없이 같다(`work/prompts/*.txt`, B1과 B2는 바이트 단위로 같다):
  ```
  레포: https://github.com/<owner>/<repo>

  이 레포와 아래 채용공고로, 이 레포 작성자 `<login>`에게 물을 기술면접 질문 8개를 만들어라. 각 질문마다 근거(커밋 SHA, 파일 경로, 코드 줄)를 붙여라. JSON 배열로: [{question, commit_sha, file_path, code_quote}]

  [채용공고]
  <포지션별 JD>
  ```
- 레포별 비용·시간(CLI가 낸 정가 기준): Signify $0.46 / 314s · Ddareungi $0.26 / 292s · Aiden-WEB $0.58 / 335s · itsdangerous $0.24 / 167s. 합계 약 **$1.54**. 4레포 모두 8문항을 냈다.

### 1-4. B2군: 도구 없는 Claude («링크만 주기» 모의)

- 같은 CLI와 모델로 `--tools ""`(도구 0개)를 주고, 빈 디렉터리에서 같은 프롬프트를 넣었다. **ChatGPT가 아니라 «도구 없는 Claude»다.** 웹 검색도 없다.
- 1차 실행 4건 중 2건이 쓸 수 없는 상태로 끝났다.
  - Signify: 출력 토큰 상한(128k)을 채운 뒤 «safeguards flagged» API 오류로 끝났다($2.63, 906s).
  - itsdangerous: 지어낸 `<invoke name="Bash">` 블록을 출력하다 128k 상한에서 잘렸다($3.34, 835s).
  - 두 건은 같은 명령으로 **딱 한 번** 다시 돌렸고, 그 결과를 썼다. 1차 출력은 `raw/claude/*.try1.json`에 남겼다.
- 최종: Signify 2문항 · Ddareungi 8문항 · **Aiden-WEB 0문항**(질문을 만들지 않았다. §4-1) · itsdangerous 8문항. 합계 **n=18**.

### 1-5. 프로토콜과 달라진 점

| C-quality §3-2 | 이번 실행 | 이유 |
|---|---|---|
| A군은 prod 앱에서 준비 카드를 생성 | prod 코드 archive에 하네스를 돌림 | 운영 DB·앱을 쓰지 않는다는 규칙. 질문 생성 경로는 같다 |
| B군은 ChatGPT(링크만) | 도구 없는 Claude (`--tools ""`) | 같은 모델·같은 CLI로 «레포 접근 여부» 한 변수만 바꾸기 위해 |
| 공고 1개 | 포지션별 1개(FE·BE) | 4레포가 FE 2개·BE 2개라서 |
| 레포 맞히기 3지선다 | **4지선다**(우연 25%) | 다수 작성자 OSS 1개를 더해 레포가 4개가 됐다 |

---

## 2. 채점 정의 (`exp-compare/work/score.py`)

| 지표 | 판정 |
|---|---|
| SHA 실존 | `git rev-parse --verify <sha>^{commit}` 성공. 짧은 SHA는 허용하고, 모호하면 실패로 본다 |
| 파일 실존 | `<sha>:<path>` 또는 `<sha>^:<path>`가 존재(삭제 커밋 허용). 경로 뒤 줄 범위 표기(`:12-30`, `#L12-L30`)는 떼고 본다. B1이 이 표기를 붙인 것은 오류로 치지 않았다 |
| (보조) 커밋이 그 파일을 수정 | 첫 부모 기준 `git show -m --first-parent --name-only`. 머지 커밋도 처리한다 |
| 인용 코드 실존 | 인용의 비어 있지 않은 모든 줄(diff `+/-` 표시와 `...` 줄은 뺀다)이 공백 정규화 후 `<sha>` 또는 `<sha>^` 시점 파일에 부분 문자열로 있다 |
| 본인 커밋 | GitHub API `repos/{r}/commits/{sha}`의 `author.login`이 로그인과 같다. Co-authored-by 트레일러에 로그인이 있어도 인정했다(DevFit의 0.70 규칙과 같다). 이번 표본에서는 두 방식의 결과가 같았다 |
| 코드 앵커 | `QuestionGrounding`(prod)과 같은 정규식으로 질문에서 앵커를 뽑았다. 영문 식별자 4자 이상(불용어·프로젝트명 제외)과 비자명한 숫자다. 그중 1개 이상이 **그 레포의 전체 이력**(`git log -p --all` + 경로 + HEAD 본문)에 있으면 앵커가 있다고 본다. 질문 본문의 커밋 SHA 조각은 앵커로 세지 않았다 |
| 레포 고유 앵커 / 이식성 proxy | 레포에 있는 앵커 중 **이 실험의 다른 레포 3개 어디에도 없는 것**을 레포 고유 앵커로 본다. 이것이 0개인 질문을 «이식 가능(proxy)»으로 센다 |

- **DevFit의 근거 필드 매핑**: `commit_sha` = `commit_hash`, `file_path` = `primary_source_file`, `code_quote` = `primary_source_diff`의 추가 줄 중 질문 앵커를 가장 많이 포함한 한 줄이다. 맞는 줄이 없으면 첫 추가 줄을 쓴다(`work/normalize.py`). DevFit은 «서버가 실제 패치를 붙인다»는 구조이므로 SHA·파일 실존은 의미가 있지만, **인용 실존은 구조상 거의 참이 된다.**

---

## 3. 결과

### 3-1. 군 × 레포

| 군 | 레포 | n | SHA | 파일 | 수정 파일 | 인용 | 근거 3종 | 본인 | 앵커 | 이식성 proxy | 근거 커밋 수 / 파일 수 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A | Signify | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 6 | 4 | 2 / 2 |
| A | Ddareungi | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 1 | 1 / 1 |
| A | Aiden-WEB | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 5 | 5 | 3 / 3 |
| A | itsdangerous | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 6 | 2 | 5 / 2 |
| B1 | Signify | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 0 | 5 / 8 |
| B1 | Ddareungi | 8 | 8 | 8 | 8 | 6 | 6 | 8 | 8 | 1 | 2 / 2 |
| B1 | Aiden-WEB | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 1 | 4 / 8 |
| B1 | itsdangerous | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 0 | 7 / 3 |
| B2 | Signify | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | (가짜 1) |
| B2 | Ddareungi | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 5 | (가짜 1) |
| B2 | Aiden-WEB | 0 | — | — | — | — | — | — | — | — | 질문 거부 |
| B2 | itsdangerous | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | (가짜 8) |

- 원값: `exp-compare/raw/metrics.json`, 문항별: `exp-compare/raw/scored.jsonl`.

### 3-2. 보조 측정

| 측정 | A | B1 | B2 |
|---|---|---|---|
| 인용 줄이 **레포 이력 어디든** 있는가(SHA 무시) | 28/28 | 30/32 | **7/18**(itsdangerous 7/8, 개인 레포 0/10) |
| 레포에 있는 앵커가 **인용 파일**에도 있는가 | 19/21 | 32/32 | — |
| DevFit 8개 밖 20문항(Aiden-WEB 3 + itsdangerous 17) | SHA·파일·본인 20/20, 앵커 15/20, 이식성 proxy 9/20 | — | — |
| 생성 시간(레포당) | 33~226s | 167~335s | 20~50s(재시도분) |

- B2가 itsdangerous에서 인용 7/8을 맞힌 것은 **유명 OSS 코드를 학습해서 외우고 있기 때문**으로 보인다. SHA는 8개 모두 가짜다. 개인 레포에서는 인용 10개가 모두 이력에 없다.

---

## 4. 눈에 띈 사례 (공개 레포 내용만 인용)

### 4-1. B2(링크만): 레포를 «읽었다»고 쓰고 지어냄

- **Aiden-WEB: 레포 내용을 지어내 판정했다.** 출력은 «`git clone` 후 전체 브랜치 조회» 결과라며 «파일은 README.md 하나뿐, 내용은 "Mobile Hacking Lab — Android Pentest Notes", 커밋 9개 모두 `Sandeep Gill`이 작성, `aidengoldkr` 커밋 0개»라고 단정하고 질문을 만들지 않았다. 실제로는 파일 95개, 커밋 20개이고 모두 aidengoldkr가 썼다. 도구가 0개였으므로 clone은 일어나지 않았다(`num_turns: 1`).
- **Signify(재시도): «커밋 1개(`cedd1e1a…`), 파일 3개(README·LICENSE·.gitignore), 소스 없음»이라고 판정했다.** 그러고는 `.gitignore` 근거 질문 2개만 냈다. 실제 레포는 커밋 9개에 MediaPipe 수어 인식 앱 소스가 있다. 레포 이름을 보고 «서명 패드»일 것이라고 추측하기도 했다.
- **Ddareungi: 코드 전체를 지어냈다.** «main.py 약 105줄, Flask `/navigate`, 카카오 로컬 API로 좌표 변환»이라고 썼지만, 실제 구조는 `app.py`(`/message`, 콜백) + `BackEnd/main.py`(Lambda·Selenium·T map)다. 커밋 `8b6cdaf…`·`09a5d56…`는 없는 커밋이다. 출력 안에 `<invoke name="Bash">` 블록 5개를 «실행 결과»처럼 적었다. 지어낸 «API 키» 문자열도 인용했다(실제 이력에는 없다. 이 문서에는 옮기지 않는다).
- **itsdangerous: SHA 8개가 모두 가짜이고, 일부는 눈에 띄는 패턴이다**(`3fe7c2d0e8f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8`, `5d9fa1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8`). 그런데도 출력 첫 줄은 «아래 SHA, 파일 경로, 인용 코드는 모두 실제 커밋 내용과 대조한 것입니다»였다.
- 함의: «링크만 주면 된다»에서는 근거가 0/18 실존했다. 레포를 실제로 읽는 단계가 없으면 근거 요구는 오히려 **그럴듯한 가짜 근거**를 만든다.

### 4-2. B1(Claude Code + clone): 강점과 약점

- 강점 ① **본인 커밋 필터를 스스로 했다.** itsdangerous에서 «Armin Ronacher(`mitsuhiko`)가 직접 작성한 커밋 91개 중 8개를 골랐다»고 썼고, 실제로 8/8이 mitsuhiko 커밋이다.
- 강점 ② **구체적이다.** 예: «EPOCH를 time.mktime(...)으로 계산하던 코드를 UTC 기준 상수 1293840000으로 바꾸셨습니다…»(`59f3bf7`, `itsdangerous.py`). «canonicalizeHands는 MediaPipe가 붙여 주는 handedness 라벨로 벡터의 슬롯을 정합니다. 그런데 ae5d01a에서 후면 카메라가 추가된 뒤로는…»(Signify). 여러 커밋에 걸친 상호작용(카메라 전환 × 손 좌우 정규화)을 짚은 질문은 DevFit 표본에는 없었다.
- 강점 ③ **비밀값을 가렸다.** Ddareungi에서 공개 이력에 남은 키를 인용하지 않고 `<KEY>`로 바꿨다. 인용 실존 2건 실패는 모두 이 경우다.
- 약점 ① **응답 언어가 흔들렸다.** 한국어 프롬프트였는데 Ddareungi 8문항은 모두 영어로 나왔다. 1회 실행이라 원인은 확인하지 못했다.
- 약점 ② **시간과 비용.** 레포당 3~5.5분, $0.24~0.58이다. Aiden-WEB은 21턴을 썼다. 사용자가 CLI와 권한, 프롬프트를 직접 준비해야 한다.
- 참고: Signify·Aiden-WEB에는 레포 안에 `CLAUDE.md`가 있다(91줄, 72줄). B1은 이 파일을 프로젝트 지침으로 읽었을 것이다. 실제 지원자 레포에서도 흔한 상황이라 그대로 두었다.

### 4-3. A(DevFit): 약점

- **근거 커밋이 몰린다.** Signify 8문항이 커밋 2개에서 나왔고, 그중 하나(`357ffc3`)는 44파일·4,857줄짜리 초기 커밋이다. Ddareungi 4문항은 모두 커밋 1개(`9a83730`)에서 나왔다. 키를 지운 커밋 `2a7cea1`은 질문이 되지 않았다. B1은 이 커밋으로 «히스토리에 남은 비밀값» 질문을 만들었다.
- **표시 파일이 질문 대상과 어긋난다.** «핸드 트래킹 지연 시간을 P50 값으로 보여주시는데…»의 근거 파일은 `src/hooks/useKeyboardOverride.ts`로 표시된다. 그러나 `latencyP50`은 같은 커밋의 `src/routes/MainView.tsx:48`에 있다. 문항의 `primary_source_file`이 Episode 대표 파일을 가리키기 때문으로 보인다(인용 파일 앵커 일치 19/21).
- **식별자를 덜 쓴다.** «특정 키를 누르면 지연 시간을 두고 여러 단계의 텍스트가 순차적으로 나타나도록 구현하셨는데…»처럼 코드를 한국어로 풀어 말하는 질문이 많다. 레포 고유 앵커가 0개인 질문이 12/28로, B1의 2/32보다 많다. 말로 답하는 면접에는 오히려 맞는 문체일 수 있지만 **이것은 사람 채점으로만 판정할 수 있다.**
- 작은 레포는 문항이 적다. Ddareungi는 커밋 2개(본인 기준)라 4문항만 나왔다. Claude Code는 같은 레포에서 8문항을 만들었다.

---

## 5. 정직한 단서

1. **n이 작다.** 레포 4개, 군별 18~32문항, 군마다 1회 실행이다. 레포 3개는 작성자가 1명이라 본인 커밋 지표가 거의 자동으로 참이다. 이 지표를 실제로 시험한 레포는 itsdangerous 하나다.
2. **같은 지시를 줬다.** B1에 작성자 로그인과 «근거를 붙여라»를 명시했다. 일반 사용자가 이렇게 묻지 않으면 결과가 달라질 수 있지만, 이번 실험은 그 경우를 재지 않았다. 반대로 공정성을 위해 B군이 할 일을 미리 알려 준 셈이라, **B1의 수치는 «잘 지시받은 Claude Code»의 상한에 가깝다.**
3. **DevFit의 인용 실존 100%는 정의상 값이다.** 서버가 붙인 패치에서 인용을 뽑았기 때문이다. DevFit의 실질 근거 지표는 SHA·파일·본인 실존과 «앵커가 인용 파일에 있음»(19/21)이다.
4. **실행마다 결과가 다르다.** DevFit 근거 선별은 결정론이지만 질문 문구는 LLM(temperature 0.2)이 만든다. Claude Code도 실행마다 다르다. B2는 1차 실행 4건 중 2건이 실패해 재시도했다(실패 출력은 보존).
5. **B2는 ChatGPT가 아니다.** 도구 없는 Claude Opus 5.5다. 다른 모델은 «레포를 읽을 수 없다»고 거절할 수도 있다. 이번 결과는 «이 모델은 거절 대신 지어냈다»까지만 말한다.
6. **앵커 지표는 필요조건일 뿐이다.** B2 Ddareungi는 코드를 지어냈는데도 앵커 8/8이 나왔다. `requests`, `timeout` 같은 흔한 단어가 레포에도 있기 때문이다. 이식성 proxy도 «식별자를 언급하는가»만 잰다. 질문이 실제로 다른 레포에 이식 가능한지는 사람 채점(§6)이 정답이다.
7. **비용은 나란히 비교할 수 없다.** Claude Code는 정가 $1.54(B1)를 냈다. DevFit은 Bedrock 34회 호출의 비용을 하네스에서 기록하지 못했다.
8. **하네스는 prod 앱 자체가 아니다.** 질문 생성 경로는 같지만 세트 구성·어필 포인트·UI는 거치지 않았다.

---

## 6. 사람이 할 일 (블라인드 채점)

- 파일: **`last-dance/collect/exp-compare/blind-sheet.csv`**(78문항, 무작위 순서, seed 20261105). 정답 키 **`answer-key.csv`**는 평가자에게 주지 말 것.
- 형식만 통일하고 내용은 고치지 않았다(`work/make_blind.py`). 바꾼 것: 공백, 레포 이름 → «[프로젝트]», 맨 앞 «[프로젝트] 프로젝트에서» 머리말 제거, 백틱 제거, 본문 SHA → «[커밋]». ⚠️ B1 Ddareungi 8문항은 영어라 군이 드러난다. 번역하면 내용을 바꾸게 되므로 그대로 두었다. 집계할 때 이 8문항을 뺀 값도 같이 볼 것.
- 평가자는 3명(팀원 2명 + 가능하면 멘토 1명)이다. 각자 파일을 복사해 `rater` 칸에 이름을 쓰고 문항마다 세 칸을 채운다.
  1. 이식성: 다른 프로젝트에도 그대로 물을 수 있는가 (예/아니오)
  2. 실제 면접에서 쓰겠나 (쓰겠다/모르겠다/안 쓰겠다)
  3. 어느 레포에서 나왔나 (Signify / Ddareungi / Aiden-WEB / itsdangerous). 참고용으로 레포 한 줄 설명만 준다: Signify = 웹캠 수어 인식 React 앱, Ddareungi = 따릉이 길찾기 카카오 챗봇(Flask + Lambda), Aiden-WEB = 개인 포트폴리오 Next.js 사이트, itsdangerous = Python 서명·토큰 라이브러리
- 집계:
  ```bash
  cd last-dance/collect/exp-compare
  python3 -I work/aggregate_blind.py answer-key.csv rater1.csv rater2.csv rater3.csv
  ```
  군별 «이식성=예» 비율, «쓰겠다/모르겠다/안 쓰겠다» 비율, 레포 맞히기 정답률(우연 25%), 평가자 쌍별 정확 일치율이 나온다. 무작위 값으로 넣어 동작만 확인했다.
- 덱 반영 규칙: 사람 채점에서 B1이 이기는 항목이 있으면 **그대로 적는다.** 그 경우에도 §요약의 한 줄(B2 0/18 · 절차 차이)은 참으로 남는다.

---

## 7. 파일

| 경로 | 내용 |
|---|---|
| `last-dance/collect/exp-compare/work/spec.json`, `jd.json` | DevFit 하네스 입력 · 포지션별 공고 |
| `…/work/run-harness.sh` | 원본 실행기 복사본(BE 경로만 archive로 변경) |
| `…/work/run-claude.sh`, `…/work/prompts/` | B1·B2 실행 명령 · 실제 프롬프트 원문 8개 |
| `…/work/normalize.py`, `score.py`, `make_blind.py`, `aggregate_blind.py` | 정규화 · 결정론 채점 · 블라인드지 · 사람 채점 집계 (stdlib만) |
| `…/work/devfit-be-prod/` | `origin/prod` `500f4af` archive |
| `…/work/clones/` | 채점용 fresh clone 4개 |
| `…/raw/devfit/{questions,episodes,runs}.jsonl` | DevFit 원출력 |
| `…/raw/claude/*.json` | Claude Code 원출력(B2 1차 실패분은 `*.try1.json`) · `claude-meta.json` |
| `…/raw/scored.jsonl`, `metrics.json`, `*_devfit_beyond8.*` | 문항별 채점 · 집계 |
| `…/raw-devfit-harness.log` | 하네스 전체 로그 |
| `…/blind-sheet.csv`, `answer-key.csv` | 사람 채점지 · 정답 키 |

⛔ `raw/`의 DevFit 패치와 B1 출력에는 Ddareungi 공개 이력에 남은 실제 API 키·엔드포인트가 들어 있을 수 있다. B2 출력에는 지어낸 키 문자열이 있다. **`raw/`를 그대로 공개하거나 장표에 붙이지 말 것.**
