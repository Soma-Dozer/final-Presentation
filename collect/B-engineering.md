# B · 엔지니어링 프로세스·전달 지표 (수행과정 20 · 결과물 50)

> 집계 2026-11-05. 원천: `Soma-Dozer/Devfit_FE`·`Devfit_BE` 원격 ref(`git fetch` 후 `origin/*`만), `gh api actions/runs` 전량(FE 1,341 · BE 1,053 실행, Slack 알림·promotion-source 포함), `gh pr list --state all`(FE 210 · BE 163, 병합 358).
> 11-05 00:00 KST 이후 원격 커밋은 0건이라 `03-실행력-집계.md`의 기준값(커밋 1,467 · 병합 PR 358 · prod 배포 138 · prod 승격 PR 154)과 그대로 맞는다.
> 경계: **중간평가 전 = ~08-20, 후 = 08-21 00:00 KST(= 08-20T15:00Z)부터.** 시각은 모두 KST.
> 원시 데이터: `collect/data/` · 재현 스크립트: `collect/scripts/` (`python3 <script> <scratch>`, 입력은 아래 수집 명령으로 만든 `runs_*.tsv`·`pr_*.json`)

공통 수집 명령:
```bash
# Actions 실행 전량 (→ data/gh_runs_full_{FE,BE}.tsv)
gh api -X GET repos/Soma-Dozer/Devfit_$R/actions/runs --paginate -f per_page=100 \
  --jq '.workflow_runs[] | [.id,.name,.event,.head_branch,.status,.conclusion,.created_at,.updated_at,.run_started_at,.head_sha,.run_attempt] | @tsv'
# PR 전량 (→ data/prs_all.csv)
gh pr list -R Soma-Dozer/Devfit_$R --state all --limit 2000 \
  --json number,title,author,createdAt,mergedAt,closedAt,state,baseRefName,headRefName,reviews,comments,additions,deletions,changedFiles,mergeCommit
```

---

## 1. DORA형 전달 지표

### 1-1. 배포 빈도 (운영)

| | 중간평가 전 (08-03 첫 배포 → 08-20, 17.5일) | 중간평가 후 (08-21 → 11-04, 75일) |
|---|---|---|
| 운영 배포 성공 | 24회 | **114회** |
| 주당 평균 | 9.6회/주 | **10.6회/주** |
| 운영 배포가 있었던 날 | 11일 | **35일 / 76일** |
| 주별 중앙값 (W35–W44 완주 주) | — | 8.5회 (범위 4–21) |
| 최대 주 | W34 13회 | **W42(10-12~18) 21회** |

- 첫 운영 배포 주(W32)부터 **14주 연속, 운영 배포가 없는 주가 0주**다.
- **산출:** `scripts/dora.py` — `CI/CD` 워크플로, `head_branch=prod`, `event∈{push, workflow_dispatch}`, `conclusion=success`. 주는 ISO 주(KST). → `data/dora_prod_deploys_weekly.csv`
- **덱 활용:** 수행과정 20 — «14주 연속 매주 운영 배포, 주 평균 10회». 주별 막대(FE/BE 누적) + 08-20 세로선.
- **주의:** 주 평균은 전후가 비슷하다(9.6 → 10.6). «배포 속도가 올라갔다»가 아니라 **«출시 첫 주부터 끝까지 리듬을 유지했다»**로 쓴다. FE 1회에 B2C·B2B·admin 3개 서피스가 같이 나가지만 1회로 셌다.

### 1-2. 변경 리드타임 (커밋 작성 → 운영 브랜치 반영)

| | 전 (운영 반영 28회 · 커밋 178) | 후 (운영 반영 125회 · 커밋 487) | 전체 (665) |
|---|---|---|---|
| 중앙값 | 17.0시간 | 17.8시간 | 17.6시간 |
| p90 | 102.5시간 (4.3일) | 146.4시간 (6.1일) | 141.6시간 |
| 24시간 안에 운영 반영 | 56% | 57% | |
| 7일 안에 운영 반영 | 99% | 90% | |
| 운영 반영 1회당 커밋 중앙값 | 3 | 2 | |

- BE만 보면 전 18.7h → 후 23.5h, FE는 17.0h → 7.7h.
- **산출:** `scripts/dora.py` — `git log --first-parent origin/prod`에서 08-03(첫 운영 배포) 이후의 각 반영점 P에 대해 `git log --no-merges <직전 P>..P`로 새로 들어온 커밋을 뽑고, `P의 committer 시각 − 커밋 author 시각`. → `data/dora_lead_time_commits.csv`
- **덱 활용:** 수행과정 — «커밋의 절반 이상이 하루 안에 운영에 나간다(중앙값 18시간)». 리드타임 분포 히스토그램 1장.
- **주의:** ① 반영 시각은 prod 브랜치 병합 시각이다. 실제 배포 완료는 그 뒤 FE 중앙 6.7분, BE 11.9분(아래 1-5)이 더 걸린다. ② 중간평가 후 p90이 늘었다(4.3 → 6.1일). `release/*` 브랜치로 묶어 staging을 거치는 방식이 자리 잡은 영향으로 보이는데, 원인은 확인하지 않았다. **«리드타임 단축»은 주장하지 않는다.** ③ `git log --first-parent origin/prod` 앞부분(06-29~08-02)은 main 이력이라 리드타임이 0으로 잡히므로 08-03 이전은 뺐다.

### 1-3. 변경 실패율 (대리지표)

운영 브랜치 push 실패 20건을, 실패한 잡 기준으로 나눴다.

| 분류 | 전 | 후 | 의미 |
|---|---|---|---|
| **배포 잡 실패** (`deploy-production*`) | 4 | **2** | 실제 배포 시도가 실패한 것 |
| 승격 게이트 차단 (`verify-production-promotion`) | 3 | 8 | staging→prod 병합 PR 없이 prod가 움직이면 배포 전에 막음 |
| 분석 문서 유출 게이트 (`block-analysis-on-production`) | 0 | 1 | 개발용 분석 문서가 운영 경로에 섞이면 막음 |
| 테스트 실패 | 0 | 1 | |
| 워크플로 파일 오류 (10-28, 실행 0초) | 0 | 1 | |

- **배포 실패율 = 배포 잡 실패 ÷ (운영 배포 성공 + 배포 잡 실패):** 전 **4/28 = 14.3%** → 후 **2/116 = 1.7%**.
- 되돌리기(revert) 커밋: `origin/prod`에 3건(FE 08-10 글래스모피즘 원복, BE 09-15 음성 프롬프트, FE 07-23 `rollback`). 원격 전체 3건.
- `hotfix` 이름의 PR은 0건이다. 브랜치명·제목에 `fix`가 들어간 staging/prod PR은 25건(전부 중간평가 후)이지만 일반 버그 수정도 섞여 있어 실패율 계산에는 쓰지 않았다.
- **산출:** `scripts/gates.py` — 실패 실행마다 `gh api repos/Soma-Dozer/Devfit_$R/actions/runs/$ID/jobs --jq '[.jobs[]|select(.conclusion=="failure")|.name]'`. revert: `git log origin/prod -i --grep='^revert'`. → `data/ci_failed_runs_by_job.csv`, `data/dora_prod_failures_mttr.csv`
- **덱 활용:** 수행과정 — «운영 배포 실패율 14% → 2%». 같은 장표에 «게이트가 배포 전에 막은 운영 push 13건»을 함께 둔다(1-6).
- **주의:** DORA의 정식 CFR은 «배포 후 장애·롤백 비율»이다. 우리는 운영 장애 기록(Sentry 인시던트)을 대조하지 않았고, 보고 있는 것은 **«배포 시도가 실패한 비율»**이다. 장표에도 «배포 실패율»이라고 쓴다. 표본도 작다(전 28회).

### 1-4. 복구 시간 (대리지표: 배포 잡 실패 → 같은 저장소 다음 운영 배포 성공)

| 사건 | 실패 단계 | 복구 |
|---|---|---|
| FE 08-03 12:00 (첫 배포일) | deploy-production | 49분 |
| BE 08-03 12:00 (첫 배포일) | deploy-production | 57분 |
| BE 08-11 00:25 → 00:55 재실패 | Secrets Manager 게시 → ECS 배포 | 120분 |
| FE 10-14 13:13 | `npm run admin:build` (관리자 콘솔) | **39분** |
| BE 10-28 08:18 | deploy-production (단계 미기록) | 27시간 (다음 날 11:27) |

- 전: 3건, 중앙값 57분. 후: 2건, 39분과 27시간.
- **덱 활용:** 넣는다면 «배포가 실패해도 1시간 안에 다시 배포했다(5건 중 4건)»까지만. 5건뿐이라 중앙값은 장표에 올리지 않는다.
- **주의:** 배포 실패가 곧 서비스 중단은 아니다. ECS 롤링 배포라 이전 버전이 계속 돌았을 수 있는데, 이건 확인하지 않았다. 10-28의 27시간은 «다음 운영 배포까지 걸린 시간»이지 장애 시간이 아니다. 그 사이 12:15 push는 승격 게이트에서 한 번 더 막혔다.

### 1-5. 배포 소요 (운영, 첫 시도 성공 실행, 실행 전체 시간)

| | 전 중앙/p90 | 후 중앙/p90 |
|---|---|---|
| FE | 3.4 / 5.5분 | 6.7 / 8.4분 (관리자 콘솔 잡 추가, 08-28) |
| BE | 14.8 / 15.1분 | 11.9 / 15.2분 |

- 산출: `scripts/dora.py`, `updated_at − run_started_at`, `run_attempt=1`.
- 주의: `08-타임라인.md`의 «429–488초 → 145–260초»는 `deploy-production` **잡 단위** 값이다. 이 표는 실행 전체(테스트 포함) 시간이라 둘을 섞지 않는다.

---

## 2. 테스트 증가

시점마다 **그 시각 직전 `main` push 실행의 `head_sha`**(= 그때 main이 가리키던 커밋)를 잡아 `git ls-tree`·`git grep <sha>`로 셌다. 체크아웃하지 않았다.

| 시점 (KST 00:00) | BE 테스트 파일 | BE `@Test` 메서드 | FE 단위 테스트 파일 | FE `it/test` | FE E2E 파일/테스트 | BE 테스트 LOC | FE 테스트 LOC |
|---|---|---|---|---|---|---|---|
| 07-15 | 16 | 44 | 3 | 13 | 0/0 | 1,304 | 127 |
| 08-01 | 59 | 303 | 19 | 112 | 2/9 | 8,101 | 1,999 |
| **08-21 (중간평가)** | **93** | **488** | **48** | **269** | **4/13** | 14,192 | 4,929 |
| 09-15 | 142 | 835 | 69 | 418 | 7/23 | 23,090 | 8,523 |
| 10-01 | 234 | 1,409 | 80 | 563 | 8/32 | 40,147 | 11,980 |
| 10-15 | 254 | 1,514 | 89 | 635 | 15/56 | 42,622 | 14,978 |
| 11-01 | 328 | 1,932 | 124 | 782 | 25/83 | 52,324 | 18,642 |
| **11-05 (현재)** | **339** | **2,000** | **127** | **807** | **25/83** | **54,195** | **19,077** |

- **중간평가 → 현재:** BE 테스트 메서드 488 → 2,000 (**4.1배**), FE 269 → 807 (3.0배), E2E 13 → 83. **합계 자동 테스트 2,890개**(BE 2,000 + FE 807 + E2E 83).
- 테스트 코드 / 제품 코드 줄 수 비율: BE 0.64, FE 0.26.
- **산출:** `scripts/growth.py`. BE: `git grep -c -E '^[[:space:]]*@(Test|ParameterizedTest|RepeatedTest)([[:space:](]|$)' <sha> -- src/test`. FE: `*.test|spec.ts(x)`(e2e 제외)에서 `git grep -c -E '^[[:space:]]*(it|test)(\.(each|only|skip|todo|concurrent))*[(\`]'`, E2E는 `e2e/`에서 `test(`. → `data/growth_tests_loc_flyway.csv`
- **덱 활용:** 결과물 50(품질)·수행과정 — «자동 테스트 2,890개, 중간평가 이후 BE 4배». 선 그래프 1장(BE/FE/E2E 3선 + 08-20 세로선).
- **주의:** 정적 카운트다. 실제로 몇 개가 통과하는지는 이번에 돌리지 않았다(지침상 테스트 실행 금지). 다만 main push마다 CI `test` 잡이 전부 돌고, 실패하면 개발 배포가 막힌다(1-6). `it.each`는 1개로 센다. BE `evaluation/` 하네스 같은 opt-in live 테스트도 메서드 수에 들어 있다. 루트 `CLAUDE.md`의 «E2E 5개»는 낡은 값이다(현재 25파일).

---

## 3. 코드베이스 증가 · Flyway

| 시점 | BE 제품 코드 LOC | FE 제품 코드 LOC | 합계 | Flyway 최고 버전 |
|---|---|---|---|---|
| 07-01 | 2,490 | 3,096 | 5,586 | — |
| 08-01 | 28,146 | 19,792 | 47,938 | V25 |
| **08-21** | 39,070 | 37,854 | **76,924** | **V42** |
| 09-15 | 50,582 | 47,170 | 97,752 | V51 |
| 10-01 | 67,121 | 51,094 | 118,215 | V61 |
| 11-01 | 83,068 | 71,067 | 154,135 | V83 |
| **11-05** | **85,105** | **72,085** | **157,190** | **V87** |

- 테스트까지 합치면 현재 **230,462줄**(제품 157,190 + 테스트 73,272).
- **Flyway:** 중간평가 V42 → 현재 **V87 (+45개)**. `origin/main`은 V1~V87에 빈 번호가 없다. `origin/prod`는 V85·V86 없이 V87까지 들어가 있다. V85·V86은 아직 운영에 안 나간 «멘토링 개선» PR(BE#157)에 묶여 있고, `spring.flyway.out-of-order: true`라 나중에 승격해도 적용된다.
- 월별 코드 증감(비병합 커밋, 코드 확장자만, 추가/삭제): BE 9월 +73,117/−5,573이 최대. 월별 표는 `data/monthly_commits_churn.csv`.
- **산출:** `scripts/growth.py` — `git grep -c -I '' <sha> -- '*.ts' '*.tsx' '*.java' '*.sql' '*.py' '*.css' '*.mjs' …`(package-lock 제외, 빈 줄 포함 물리 줄 수). Flyway는 `src/main/resources/db/migration/V*__` + `src/main/java/db/migration/V*__`(V42·V87은 Java).
  월별 증감: `scripts/pattern.py` — `git log --remotes=origin --numstat`.
- **덱 활용:** 결과물 50 — «중간평가 이후 코드 7.7만 → 15.7만 줄, DB 스키마 변경 45회»는 보조 수치로만. 핵심 장표에는 테스트(2)를 쓰는 편이 낫다.
- **주의:** LOC는 «많이 만들었다»의 근거일 뿐 품질 근거가 아니다. 심사위원이 «AI로 찍어낸 줄 수 아니냐»고 물을 수 있다. 쓰려면 테스트 비율(BE 0.64)과 함께 쓴다. CS 지식백과 본문(`content/*.html` 173개)·SVG는 LOC에서 뺐다.

---

## 4. 작업 패턴 (KST, 비병합 커밋 961개 · author 시각)

| | 전체 | 중간평가 전 (424) | 후 (537) |
|---|---|---|---|
| 22시~06시 커밋 비율 | 26.0% | 26.2% | 25.9% |
| 00시~06시 | 14.9% | 17.7% | 12.7% |
| 주말(토·일) | 14.4% | 14.4% | 14.3% |
| 커밋이 있었던 날 | 94일 / 129일 (73%) | 40 / 53일 | 54 / 76일 |
| 최장 연속 커밋 일수 | 12일 | | |

- 시간대(0→23시): `55 36 15 28 9 0 0 19 29 23 40 47 55 42 86 79 49 49 35 61 56 41 51 56`. 14~15시가 최고, 05~06시는 0.
- 요일: 월 161 · 화 172 · 수 158 · **목 230** · 금 102 · 토 89 · 일 49.
- **산출:** `scripts/pattern.py` — `git log --remotes=origin --format='%H%x09%aI%x09%an%x09%P' --numstat`, 부모가 2개 이상인 병합 커밋 506개는 제외. → `data/commit_heatmap_weekday_hour_kst.csv`(요일×시간 7×24), `data/commits_remote_all.csv`
- **덱 활용:** 수행과정 «실행력» 장표의 보조 히트맵. 메시지는 **«129일 중 94일 커밋, 최장 12일 연속»** 정도로 사실만. 야근 비율은 장표 본문에 쓰지 않는다.
- **주의:** ① author 시각은 커밋을 만든 시각이지 일한 시간이 아니다. 에이전트가 만든 커밋, rebase한 커밋도 섞여 있다. ② 팀원 3명이 모두 학생·연수생이라 «주말 14%»가 낮다고 해석하면 안 된다(평일 수업 외 시간이 섞인다). ③ 야간 비율을 «열정»으로 포장하면 역효과가 날 수 있으니 수치만 쓴다.

---

## 5. PR 리뷰

| 지표 | 값 |
|---|---|
| 병합 PR | 358 (FE 201 · BE 157) — prod 154 · staging 133 · main 67 · 기타 4 |
| **GitHub 리뷰(approve/comment review)가 달린 PR** | **0건 (0%)** |
| 코멘트가 1개라도 달린 PR | 2건 (0.6%) |
| 작성자 본인이 병합 | 344 / 358 (96%) |
| PR 본문 50자 이상 | 312 / 358 (87%) |
| 본문에 테스트·검증 언급 (`test|테스트|검증|vitest|gradlew`) | 257 / 358 (72%) |
| 생성→병합 시간 중앙값 | **0.11시간 (≈7분)**, p90 1.3시간 |
| └ main 대상 | 중앙 0.13h, p90 12.4h |
| └ staging 대상 | 중앙 0.10h, p90 0.3h |
| └ prod 대상 | 중앙 0.12h, p90 1.2h |

- **산출:** `scripts/prs.py`(`reviews`·`comments` 필드). 표본을 REST로 다시 확인: `gh api repos/Soma-Dozer/Devfit_$R/pulls/$N/reviews`(FE/BE #5·50·120·150 모두 0). 병합자: `gh pr list --state merged --json author,mergedBy,body`. → `data/prs_all.csv`
- **덱 활용:** **장표에 쓰지 않는다.** 질의응답 대비용이다. «리뷰 문화»를 물으면 이렇게 답한다: «사람이 승인하는 방식 대신, 병합 전 CI 테스트와 승격 게이트를 통과해야만 운영에 나가는 구조로 막았다. PR 본문의 72%에 검증 내역을 적었다.»
- **주의:** 🔴 **«코드 리뷰를 했다»는 주장 금지.** GitHub 리뷰는 0건이다. 브랜치 보호(필수 리뷰·필수 체크)도 비공개 무료 플랜이라 API가 403을 준다(`Upgrade to GitHub Pro`). 그래서 운영 보호는 병합 차단이 아니라 **배포 잡의 `needs` 조건**으로 걸려 있다. 실제로 staging이 아닌 브랜치에서 prod로 병합된 PR이 4건 있다(FE#27 08-17, FE#123·BE#80·BE#82 10-01). 이런 PR은 `Production promotion source` 검사가 빨간불을 띄웠지만 병합 자체는 막지 못했다.

---

## 6. CI 품질 게이트

`origin/main`의 `ci.yml` 잡과 처음 생긴 날짜(`git log --remotes=origin --reverse -S '  <job>:' -- .github/workflows/ci.yml`):

| 게이트 | 저장소 | 도입 | 운영(prod)에 있음 | 막은 횟수 (실패 실행) |
|---|---|---|---|---|
| `test` (BE: gradle test+package / FE: npm test·lint·build·admin 검증) | FE·BE | 07-11 | Y | **112회** (기능 PR 37 · staging PR 18 · main push 56 · prod 1) |
| FE→BE API 계약 대조 (FE `test` 잡이 BE 소스를 받아 대조) | FE | 08-13 `ea2b489` | Y | `test` 실패에 포함 |
| `verify-production-promotion` (병합된 staging→prod PR 필수) | FE·BE | 08-01 | Y | **11회** (전 3 · 후 8) |
| `Production promotion source` (prod PR의 head가 staging인지, `pull_request_target`) | FE·BE | — | Y | 18회 (FE 10 · BE 8) |
| `block-analysis-on-production` (개발용 분석 문서가 운영 경로에 섞이는지) | FE | 08-13 | Y | 3회 (+ 다른 실패와 겹친 경우 다수) |
| `speech-local-test` (음성 스케줄링) | BE | 09-17 | Y | `test`와 함께 실패 |
| `npm audit --audit-level=high` | FE | 11-01 `84fb8ca` | 확인 안 함 | 0 |
| `vulnerability-scan` (bootJar 내장 CycloneDX SBOM → grype HIGH/CRITICAL) | BE | **11-02 `f7d2f42`** | **N (main만)** | 0 (11-02 이후 main 실행 통과) |

- CI 실행 실패율(Slack·promotion-source 제외): 전 34/307 = 11.1% → 후 113/708 = 16.0%. 후가 높은 이유는 테스트가 4배로 늘면서 **게이트가 더 자주 걸렸기 때문**으로 읽을 수 있다. 다만 원인을 따로 확인하지는 않았다.
- **배포 전에 막힌 운영 push 13건**(승격 게이트 11 + 유출 게이트 1 + 테스트 1)이 있었고, 이 중 실제로 운영에 나간 것은 0건이다.
- **산출:** `scripts/gates.py` (실패 실행 140건마다 jobs API 조회) → `data/ci_failed_runs_by_job.csv`
- **덱 활용:** 수행과정 20 — 파이프라인 도식 1장: `기능 브랜치 → main(test·계약 대조, 개발 배포) → staging PR(test) → prod PR(승격 출처 검사) → prod push(승격 검증 + 유출 차단 + test) → 운영 배포`. 각 화살표 밑에 막은 횟수(112 · 18 · 11 · 3)를 단다.
- **주의:** SBOM 취약점 게이트는 **운영 경로에 아직 없다**(`origin/prod`의 `ci.yml`에 `vulnerability-scan` 없음). 장표에 넣으면 «main에 도입»이라고 쓴다. `08-타임라인.md`의 서술과도 맞다.

---

## 7. 중간평가 이후 출시 기능

08-21 이후 병합되고 **병합 커밋이 `origin/prod`의 조상인 것**(`git merge-base --is-ancestor <mergeCommit> origin/prod`)만 셌다. staging 대상 PR 119건 + main 대상 PR 50건이 운영에 반영됐다. 운영에 안 나간 것은 2건(«멘토링 개선» FE#204·BE#157, 11-02 main 병합)이다. FE·BE 짝 PR은 1개 기능으로 묶었다. → `data/prs_post_mideval_delivery.csv`

| 묶음 | 운영 반영 기능 (대표 PR) | 수 |
|---|---|---|
| 공고 수집 확장 | 인크루트 지원(BE#33) · 대기업 공식 채용 사이트(BE#37) · 기업 로고 번들(BE#58) · 공고 캐시+크롤러+토스 커리어 V59·V60(BE#60) · 대표 공고 카드(토스·SK하이닉스 FE#147, kt is FE#163) | 5 |
| 질문 품질 엔진 | 난이도 축 분리(BE#46) · 모의면접 출력 한도(BE#44) · 실제 면접 출제 근거 연결(BE#75/FE#110) · 기출 근거 853건(BE#85) · 회사별 기출 탭(BE#122/FE#173) · 유의미 커밋 판별 Decisions(BE#112) · 근거 diff 판별+병렬 수집(BE#130) · 출력 상한 1만 토큰(BE#110) · pgvector 기출 연결(BE#158→prod) | 9 |
| 음성 모의면접 | Supertonic 전환(BE#53, **prod 09-16 `98ebb0f`**) · 음성 UI(FE#74) · 답변 기반 꼬리질문·종합 피드백(BE#83/FE#125) · 꼬리질문 명확성(BE#86) | 4 |
| 진입 장벽 낮추기 | 비로그인 준비 기록(BE#79/FE#122) · 공고 없는 CS 면접(BE#81/FE#124) · 무공고 레포 분석 연결(BE#84/FE#128) · 분석 대기 게임(FE#116 외) | 4 |
| 면접 리뷰·KPI | 실제 면접 리뷰+KPI(BE#77/FE#113) · 일정 없는 리뷰(BE#115/FE#168) · 기존 공고 선택(BE#119/FE#170) · 콜백 메일 재방문 집계(BE#103/FE#158) | 4 |
| 결제 | 토스 결제 심사용 TEST 결제(BE#105/FE#160) · 결제 심사 권한(BE#113) · **단건 결제 LIVE 분리 + Free 월 10회**(BE#153/FE#200) · 결제·탈퇴 결함 7건 수정(BE#134) | 4 |
| B2B | 면접 브리프·공개 설정(BE#49/FE#70) · 조직 관리·블라인드 평가(BE#145/FE#188) | 2 |
| 관리자·운영 지표 | 관리자 콘솔·운영 API(BE#27/FE#49) · 사용량·단가 계측(BE#29·#39) · 회원 사용 순위(BE#67) · 기출 DB 조회(BE#73) · 행동·유입 분석(BE#101/FE#154) · 게스트 지표 분리(BE#88) · 메일 발송+이미지(BE#138·#160) · SBOM 화면(BE#151/FE#197) | 8 |
| 안정성·관측·인프라 | Sentry 운영 수집(BE#92/FE#138) · Sentry 지연 로딩(FE#152) · 비동기 배포+Slack(BE#63) · 분석 실패 사유 코드(BE#123/FE#174) · Spring Boot 4.1 / Next 16.4.3 / Node 24 업그레이드(BE#151/FE#197) · private scope 단일 조회(FE#104·#105) | 6 |
| 유입(SEO·공유) | CS 기술면접 질문 색인(FE#80) · 도해 이미지 검색(FE#83) · 운영 canonical apex 전환(FE#76) · 랜딩 메타·JSON-LD·404(FE#73) · OG 이미지 교체(FE#207·#209) | 5 |
| **합계** | | **51** |

- **산출:** 위 CSV의 `title`을 손으로 묶었다. PR 없이 main에 직접 push된 커밋은 이 표에 없다.
- **덱 활용:** 결과물 50 — «중간평가 이후 76일, 운영에 나간 기능 51개(10개 묶음)». 묶음별 막대 + 대표 기능 3개(단건 결제 LIVE · 기출 853건+pgvector · 음성 모의면접)만 크게.
- **주의:** 묶는 방식에 따라 수가 달라진다(±10). 장표에는 «50여 개»나 «10개 영역»으로 쓰는 편이 안전하다. 관리자·운영 지표(8)는 사용자 기능이 아니므로, 사용자 기능만 말할 때는 43개다. 반대로 `fix:` PR(25건)은 일부만 기능으로 넣었다.

---

## 기존 문서와 어긋나거나 새로 확인된 것

1. **BE#53 음성 모의면접(Supertonic)은 운영에 나갔다.** 09-16 21:17 prod 병합 `98ebb0f`, 같은 날 `Backend CI/CD` prod push 성공. `08-타임라인.md`의 «넣지 않은 것» 2번째 항목은 이제 해소할 수 있다.
2. **SBOM 게이트(`f7d2f42`)가 운영에 없다는 것도 확인했다.** `origin/prod` `ci.yml`에 `vulnerability-scan` 잡이 없고, 이 커밋을 묶은 BE#157은 prod의 조상이 아니다.
3. **운영 DB 스키마는 V87까지 갔지만 V85·V86은 빠져 있다.** out-of-order 설정이 있어 당장 위험하지는 않다. 다만 «V87까지 운영 반영»을 «마이그레이션 87개 운영 반영»으로 바꿔 쓰면 틀린다(운영에는 85개).
4. 루트 `CLAUDE.md`의 «E2E Playwright 5개», «BE 101파일»은 낡았다. 현재 E2E 25파일·BE 테스트 339파일이다.
