# DevFit 기술 하이라이트

> SW Maestro 17기 · Team Dozer · 2026-11-04 기준
> 근거: Devfit_BE · Devfit_FE 소스, `gh run view` 배포 기록, `docs/question-quality-evaluation`, `docs/ops/llm-cost-model.md`, `feedback/00_공방표_Attack-Defense.md`
> 아티팩트: https://claude.ai/artifact/U4BRHsaBYNuZwL1MDCYeL7

채용공고와 지원자의 GitHub 코드로 기술면접 질문을 만드는 DevFit의 엔지니어링 포인트를 모았다. "기술적"의 기준에는 피드백을 받고 고친 개선도 포함한다.

| 구분 | 건수 |
|---|---|
| 피드백 → 개선 루프 | 15 |
| 영역별 기술 항목 | 28 |
| 발표 시 표현 주의 | 11 |

---

## 0. 발표 메인으로 쓸 5개

1. **근거 게이트가 코드로 질문을 거른다.** 입력 게이트(diff 로직 라인 수)와 출력 게이트(질문 속 식별자가 실제 코드에 있는지)를 프롬프트가 아니라 서버 코드로 강제한다. 근거가 없으면 모델을 부르지 않는다.
2. **질문 품질을 재는 평가 하네스.** 운영 파이프라인을 그대로 호출하고 8축 루브릭, 결정적 지표 13개, 회귀 게이트로 채점한다. 근거 Episode 맞히기 81.9% (4지선다, 우연 25%).
3. **본인이 짠 코드에서만 출제.** 커밋 작성자를 인증 이메일·GitHub 로그인과 대조해 기여 신뢰도를 매기고, 본인 커밋이 아니면 버린다. "AI로 짰나"가 아니라 "알고 짰나"를 묻는다.
4. **피드백 하나에 원인 → 수정 → 측정.** "쉬움 질문이 사실 확인뿐" 지적에 원인(난이도=유형 1:1 사상)을 찾고 분리해 저난도 반사실 질문을 12% → 78%로 올렸다.
5. **배포를 Step Functions로 넘긴 CI/CD.** Actions는 이미지 digest만 넘기고 종료한다. staging→prod 승격 게이트, OIDC, SHA 고정 액션, SBOM 취약점 차단까지 갖췄다. 운영 배포 잡 약 7.5분 → 3분.

---

## 1. 피드백 → 개선 루프 (15건)

출처: 중간 = 08-20 중간평가 심사위원, 0807 / 0907 / 0922 / 1102 = 각 멘토링. 
| # | 피드백 (출처) | 찾은 원인 | 수정 | 결과 |
|---|---|---|---|---|
| 1 | 쉬움 난이도가 코드 사실 확인에 그친다 (0907#1 한유일 멘토) | 난이도와 질문 유형이 1:1로 묶여 있었다 (예외 0/114) | 난이도를 근거 두께로 정하도록 분리 (BE `32e25e9` `8aa7bfa`), 09-09 prod | **저난도 반사실 질문 12% → 78%** |
| 2 | AI 질문 품질을 자동 검증할 방법 필요 (중간#5) | 품질을 감으로 판단, 버전 간 비교 기준 없음 | 평가 하네스: 운영 파이프라인 직접 호출, 8축 루브릭, blind/grounded 이중 채점, 결정적 지표 13개, 실패 시 exit 1 회귀 게이트 | **근거 Episode 맞히기 81.9%** (n=177, 우연 25%) ⚠️ QI 버전 간 차이는 재실행 잡음 7.5점 이내라 "개선 입증 못 함"으로 보고 |
| 3 | 정확성·유용성·변별도를 객관 검증하라 (중간#4) | LLM 심판 하나의 점수를 절대값으로 믿었다 | 심판 노이즈 직접 측정: 자기 일관성 n=80, Kimi·DeepSeek 교차 n=180, 같은 코드 재실행, 현직자 블라인드 리뷰 | **재실행 ±1 이내 96% 이상, 잡음 7.5점 수치화** ⚠️ 사람 기준선 1명·21문항, 변별도 실측 0건 |
| 4 | (긍정) 커밋·diff 연결로 설명 가능성 확보 (중간#3) | 근거 연결이 프롬프트 지시에만 의존 | 서버가 evidenceQuote 대조 (12자 이상, 주석 제거, 보낸 코드의 줄 시작과 일치). 근거 없으면 모델 미호출 + 사유 코드 (BE `b7175be`) | **인용 46/46 일치** ⚠️ 불일치는 폐기되므로 필터 결과, 품질 지표 아님 |
| 5 | 근거 게이트 임계값 재보정 (내부 회귀) | 366문항 코퍼스에서 근거 20줄 미만일 때 CODE_FLOW 품질 40.2 | THIN(<20줄)이면 WHY_DECISION·TRADE_OFF만 허용. 200/300줄 재보정은 질문이 48 → 17개로 줄어 되돌림 | 보정 이력이 `EvidenceGate.java` javadoc에 남음 |
| 6 | 의도별 카테고리로 질문 생성 (중간#6) | 유형이 섞여 나오고, 팀 레포에서 남의 코드로도 출제 | 의도 7유형 + 본인 기여 필터 (작성자 일치 1.0, Co-authored-by 0.70, 그 외 제외), 사용자 정정 가능 (`ContributionOwnershipService`) | 본인 커밋이 아닌 코드는 출제 제외 |
| 7 | RAG는 정확매칭 + 임베딩, 레퍼런스 보존 (1102#4) | 기출 연결이 어휘 매칭(임계 0.72)에만 의존 | pgvector: V87 마이그레이션, Bedrock 임베딩, 비동기 임베딩 캐시, 워커 임대 테이블로 다중 서버 중복 방지. 어휘 매칭 병행 | **11-02 prod 반영 (`c680990`)**, 출처 URL 304개 보존 |
| 8 | 배포 완료를 기다리지 말고 던져두라 (0922#2) | Actions 러너가 ECS 안정화까지 대기 | Step Functions 위임: 이미지 digest + Secrets 버전만 넘기고 종료. 멱등 실행 이름(재시도에 다른 입력이면 거부). 동기 폴백은 DynamoDB 락 | **운영 배포 잡 429–488초 → 145–260초** ⚠️ 단축이 prod async 전환(10-15)보다 먼저 나타남, 원인 귀속 미검증 |
| 9 | 배포 결과를 모른다 / 캐시는 쓰나 (0922#1·#3) | 알림 없음, Docker 레이어 순서 비효율 | Slack 배포 알림 (BE `0770825`, 세션 당일), GHA 캐시 + 모델 레이어 순서 조정 (`bf771eb`) | Slack에서 배포 결과 확인 ⚠️ BE 테스트 잡이 3–4분 → 7–11분으로 늘어 남은 병목 |
| 10 | 분석 실패 이유를 사용자가 아나 (0922#12) | 실패 시 재시도 버튼만 노출 | 근거 없음 사유 코드 + FE 사유별 안내 (FE `741df1e`) | 재시도 대신 원인 안내 |
| 11 | "GitHub 연동하면 털리는 거 아냐?" (0807#10) | 처음부터 넓은 권한 요청 | 최소 scope(`read:user,user:email`), private은 추가 동의, 토큰 AES-256-GCM, clone 토큰은 env 주입으로 `ps`·.git/config 비노출 (FE `baebd8d`) | 레포 범위를 사용자가 선택 |
| 12 | SBOM으로 무엇을 막는지 사례 필요 (1102#7) | SBOM만 만들고 미사용 | bootJar 내 CycloneDX SBOM을 grype로 스캔, HIGH·CRITICAL이면 배포 차단, 예외 90일 상한. React2Shell 영향 판정 문서 | **의존성 203개 중 차단 0건, React2Shell 비해당** ⚠️ 발표용 사례 장표 없음 |
| 13 | 음성 입력 필요 / AI 코치 타임아웃 (0907#6·#10) | 출력 토큰 상한 1280으로 응답 잘림 | STT·TTS + 답변 기반 꼬리질문, 출력 토큰 1280 → 8192 (BE `c5a3ac7`), `max_tokens` 잘림을 예외로 감지 | **v13 음성 꼬리질문 1/4 → 4/4** ⚠️ 코드 샘플 1개·합성 답변 2개 기준 |
| 14 | 원가 기반 바텀업 가격 / 결제엔 사업자 필요 (0807#4·#8) | 원가를 모른 채 가격 책정 | LLM 호출별 원가 ledger (별도 트랜잭션, 호출 시점 가격 고정). 사업자 등록 후 Toss: Idempotency-Key, 주문 상태 머신, 웹훅 대신 서버 간 조회로 대사 | **1런 330원 (94% glm-5), B2B 1인 1,404원 실측. 단건 결제 LIVE 11-02** ⚠️ 원가는 8월 측정 |
| 15 | questionCount·repoSummary 버그가 prod까지 감 (운영 사고) | FE·BE API 계약 확인 단계 없음 | FE CI가 BE 소스를 체크아웃해 라우트·필드를 대조하는 교차 레포 계약 테스트 (`lib/candidate-api-contract.test.ts`) | 계약이 어긋나면 FE CI 실패 |

---

## 2. 영역별 기술 항목 (28건)

검증 수준: **[코드]** 소스에서 확인 · **[문서]** 문서·측정 자료 기준

### A. 레포 분석 파이프라인

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| 잠근 partial clone [코드] | `clone --bare --filter=blob:none --single-branch --no-tags`. hooks 끔, fsck 켬, submodule 끔, https만. private 토큰은 github.com 한정 extraHeader를 env로 주입 | 레포 상한 1024MiB, clone 120s, 캐시 30일 | `github/GitRepositoryEvidenceCollector.java:500-560` |
| 룰 + LLM 커밋 점수 [코드] | 룰 점수를 midrank 백분위로 변환, 동점은 SHA로 결정적 분리. LLM 판정과 blend, 커버리지 50% 미만·실패 잦으면 룰만으로 자동 폴백 | keyword 0.40 / specificity 0.60, 동시 6, 레포당 25s, 쿨다운 15분 | `github/CommitDecisionBlend.java` |
| 노이즈 커밋·파일 제거 [코드] | merge·chore·docs·lint·bump·dependabot 제외, lockfile·minified 무시, 테스트 경로 감점, `--unified=30` 맥락 | 로그 1000커밋, diff 후보 12, 스니펫 6 | `GitRepositoryEvidenceCollector.java ~838` |
| 코드 축 Episode 구성 [코드] | technicalDepth, evidenceDensity, jobRelevance로 선정. 커밋 메시지는 동점일 때만 | 레포당 4–10 Episode | `study/EpisodeBuilder.java` |
| 재분석 재사용 4단계 [코드] | 입력 지문으로 ALL(Bedrock 호출 0) / KEEP_LLM / EVIDENCE_ONLY / NONE 선택 | — | `study/CatalogGenerationVersion.java:40-55` |
| LLM 없는 출력 게이트 [코드] | 질문에서 영문 식별자·숫자 anchor 추출. 코드에 없고 문장에만 있으면 폐기 또는 1회 재질의(KEEP/DISCARD/REASK). 일반 CS 질문 이탈도 감지. 정규식은 평가 하네스와 동일 | 최소 3문항, A/B 63개 중 5개 폐기 | `study/QuestionGrounding.java` |

### B. LLM 레이어 (Bedrock)

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| 작업별 모델 라우팅 [코드] | 추론 `zai.glm-5`, 코드 `qwen3-coder-next`, 추출 `glm-4.7-flash`, 비전 `nova-2-lite`, 사업자등록증 OCR `qwen3-vl-235b` | — | `bedrock/BedrockService.java` |
| 게이트가 스키마 enum을 줄임 [코드] | Converse API `json_schema` 구조화 출력. 게이트를 통과한 유형만 enum에 남겨 잘못된 유형과 출력 토큰을 동시 감소 | — | `BedrockService.java:2434-2460` |
| 호출 분할로 생성 시간 절반 [문서] | Episode 1개 = 1호출, 호출당 유형 최대 4, 6 병렬. 잘림은 `LlmOutputTruncatedException`. 출력 예산 min(10,000, 240s × 60tok/s × 0.75) | 평균 93.70s → 49.07s, 잘림 1 → 0, 출력 토큰 −13.8% | `docs/REPOSITORY_ANALYSIS_PERFORMANCE.md:72` |
| LLM 원가 ledger [코드] | 호출마다 `REQUIRES_NEW`로 기록. 프롬프트 글자 수와 실제 토큰 수를 같이 저장해 chars/token 재보정 가능, 가격은 호출 시점 고정 | 보존 400일, 한글 1.3자/토큰 | `bedrock/LlmUsageRecorder.java` |

### C. 데이터

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| 실기업 기출 데이터셋 [문서] | 3축 분류, 13개 반복 그룹. 후보 소스 191개 조사(84개 비권장), 잡코리아·사람인 크롤링 판례 검토. prod 업로드 SHA 검증 | 853건, 41개사, 출처 URL 304, 799 갱신 / 54 유지 | `research/interview-evidence-polished/` |
| 기업 채용사이트 24곳 크롤러 [코드] | 모든 요청이 `SafeFetcher` 경유, 리다이렉트마다 허용 호스트 재확인(SSRF 방지). 이미지형 공고만 비전 OCR | 24 사이트, OCR 동시 8, 사이트 간격 400ms, 연속 실패 10회 중단 | `prep/corporate/CorporateSiteRegistry.java` |
| 공고 캐시·일일 예산 [문서] | read-through 캐시, 본문 해시 키 인사이트. KST 일일 LLM·OCR 상한, heartbeat로 멈춘 실행 복구 | LLM 1000/일, OCR 300/일, 시드 1,397행·2,657 인사이트 ≈ $2 | `docs/posting-cache/DESIGN.md` |

### D. 비동기 · 결제 · 크레딧

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| DB 기반 작업 큐 [코드] | CAS 상태 갱신으로 claim, 지수 백오프(30s × 2ⁿ, 최대 3회), 45분 락 타임아웃, stale 스캔. 추가 질문은 `FOR UPDATE SKIP LOCKED` | 스케줄러 4 / Hikari 10 | `prep/CandidateAnalysisQueue.java:49-86` |
| 리셋 잡 없는 크레딧 [코드] | KST 날짜 버킷이라 자정 리셋 불필요. 예약 → 확정 2단계, 60분 넘은 예약은 reconciler가 회수하고 누락 환불 보정 | 10 크레딧/일, 회수 60분 | `credit/CandidateCreditReconciler.java` |
| Toss 결제 상태 머신 [코드] | lease 기반 주문 상태(VERIFYING, PAID, REFUND_PENDING, PARTIALLY_REFUNDED) + PAST_DUE 갱신. 웹훅 필드 불신, 서버 간 조회로 대사. 결제 데이터 AES-GCM | — | `billing/PaymentService.java`, `PaymentCipher.java` |

### E. 음성 모의면접

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| AudioWorklet 리샘플링 [코드] | 16kHz mono PCM16 다운샘플, 콜백 간 위상 유지로 클릭 노이즈 방지. 서버 롤링 재전사 단위에 맞춘 320ms 프레임, 정지 시 잔여 flush | 5120 샘플 = 320ms, flush-ack 300ms | `Devfit_FE/public/pcm-worklet.js` |
| 스트리밍 STT·TTS 폴백 [코드] | AWS Transcribe 스트리밍(WebSocket), 50–200ms 청크 재분할. Polly에 한국어 남성 음성이 없어 OpenAI TTS·edge-tts 사이드카로 보완, 실패 시 Polly | — | `study/SttWebSocketHandler.java`, `speech/AudioChunker.java` |

### F. 인프라 · CI/CD

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| staging → prod 승격 게이트 [코드] | `pull_request_target`는 PR 메타데이터만 읽고 코드 미체크아웃. 병합된 staging→prod PR에서 온 push가 아니면 prod 배포 거부 | — | `.github/workflows/production-promotion-source.yml` |
| CI 비밀값 위생 [코드] | OIDC 역할, 모든 액션 SHA 고정, dotenv 검증, 덮어쓰기 금지 예약 키, `umask 077` 임시 파일 종료 시 삭제. 내부 `/analysis` 문서 prod 차단 | — | `Devfit_BE/.github/workflows/ci.yml` |
| 서버 없는 Next.js 운영 [코드] | static export → S3 + CloudFront. 동적 ID는 CloudFront Function이 `__id__` 프리렌더 페이지로 rewrite, 빌드 결과와 대조 테스트. B2C·B2B·admin 별도 빌드·버킷·배포 | static immutable 1년, HTML must-revalidate, FE 배포 130–195s | `Devfit_FE/infra/cloudfront-rewrite.js` |
| 엣지 보안 헤더 [코드] | CloudFront 응답 헤더 정책: HSTS 1년, X-Frame-Options DENY, COOP, 마이크는 자기 도메인만. RSC 서버·`"use server"` 없어 React2Shell 비해당 | — | `infra/cloudfront-response-headers.json` |
| 병렬 ECS 롤아웃 [코드] | backend·analysis-worker 동시 배포, 롤아웃 상태 폴링 + `services-stable` | — | `ci.yml ~710` (`de8b57e`) |

### G. 보안 · 관측 · 운영

| 항목 | 메커니즘 | 수치 | 근거 |
|---|---|---|---|
| 잠금 DoS를 피한 로그인 제한 [코드] | 계정 잠금 대신 고정 윈도. 토큰 SHA-256 지문 저장, refresh 회전, 상수 시간 비교. 암호화 키 없으면 prod 기동 거부 | IP 20 / 계정 10 per 10분, bcrypt 12 | `auth/GithubTokenCipher.java` |
| 유료 경로 남용 방지·실삭제 [코드] | 피드백·꼬리질문 LLM 호출 사용자당 시간당 60회. 탈퇴 시 FK 순서 물리 삭제 | — | `study/LlmQuotaGuard.java`, `user/UserDeletionService.java` |
| 관리자 콘솔·동의 기반 분석 [코드] | 별도 Next 앱, Cognito OAuth PKCE(S256 + state). 회원·사용량·실패·공고 캐시·Sentry·감사 로그 등 약 20개 화면. GA4·Ads는 Consent Mode v2 기본 거부. Sentry FE·BE·워커 | — | `Devfit_FE/admin/lib/auth.ts`, `lib/analytics.ts` |
| CS 지식백과 SEO/GEO [문서] | CS 아티클 172편, JSON-LD 6종(TechArticle, FAQPage, BreadcrumbList, Speakable, Organization, WebApplication), AI 인용용 llms.txt, 배포 후 IndexNow | Lighthouse Perf 99, SEO 100, LCP 1.8s, CLS 0 | `Devfit_FE/content/cs`, `infra/search-indexing.md` |
| 테스트 규모 [코드] | BE Testcontainers PostgreSQL 통합 테스트, 평가 하네스는 JUnit eval 태그로 분리. FE Vitest·Playwright, 교차 레포 API 계약 테스트 | BE 테스트 파일 326, @Test ≈ 1,916, Vitest 117, Playwright 30 | `Devfit_BE/src/test`, `Devfit_FE/e2e` |

---

## 3. 발표 시 주의 (11건)

코드·실행 기록으로 확인한 사실과 자료상 주장이 다른 지점. → 는 대신 쓸 표현.

| 주장 | 문제 | 대신 쓸 표현 |
|---|---|---|
| "인용 일치율 46/46" | 서버가 불일치 인용을 폐기하므로 정의상 100% | → "실제 코드와 다른 인용은 서버가 폐기한다" |
| QI 점수 상승·하락 | 재실행 잡음 7.5점 > 측정된 개선폭(1.5–3.8). v12에서는 두 심판 방향도 반대 | → "Episode 맞히기 81.9%"처럼 우연 대비 지표 사용 |
| "검증된 기출 853건" | 매니페스트 `human_review_completed: false`, 검토 필요 158건, LLM 큐레이션 | → "공개 출처 304개에서 수집, 출처 보존" |
| "배포 8분 → 3분" | 운영 배포 잡만 해당. 단축이 async 전환보다 먼저 나타남. 전체 파이프라인은 테스트 잡 증가로 오히려 길어짐 | → "운영 배포 단계 약 7.5분 → 3분, 배포 대기는 Step Functions로 이관" |
| 원가 330원/런 | 8월 측정값. v13에서 음성을 GLM-5로 옮겨 지금은 더 높을 수 있음 | → "8월 실측 기준" 명시 |
| 특허 | 2026-11-01에 3건을 출원했다: 10-2026-0214808 질문 선별, 10-2026-0214809 질문 생성, 10-2026-0214811 음성 대화 답변 평가. 출원인은 김건우(개인), 발명자는 김건우·박천웅·노재원이고 심사청구는 하지 않았다. `docs/patent`의 나머지 초안 8건은 미출원이다. 근거: `last-dance/metrics/screenshots/patent_*.png` | → "특허 3건 출원". «등록»·«회사 특허»라고 쓰지 않는다 |
| Playwright · Terraform · 알람 | Playwright CI 미실행, `.tf` 파일 워크스페이스에 없음, CloudWatch 알람 못 찾음 | — |
| 자체 음성 모델 | `speech/` Raon-Speech-9B는 스파이크, 운영 경로 아님. 운영은 Transcribe·Polly | — |
| SEO 성과 | 9-17 기준 `site:devfit.app` 0건, Search Console 미등록 | → Lighthouse 점수만 언급 |
| 보안 부채 | Spring Security·Bean Validation 없음, X-Forwarded-For 위조로 rate limit 우회 가능, Spring Boot 3.4.1 OSS 지원 종료 | → 질문 나오면 부채 목록으로 인정 |
| 로컬 BE 체크아웃 | 로컬 `feat/local-leftovers-20261028`에는 pgvector 코드 없음 | → 시연·코드 설명은 `origin/prod` 기준 |
