# R3 — 인앱 이탈 · 야간 가입 · 경쟁사 표 · 시장 규모 근거

> 조사일 2026-11-06 · 요청: ppt-start · research-2 (Opus 총괄 + Sonnet Worker 4개)
> 표기: **직접** = 원문을 열어 확인 · **간접** = 언론·벤더 경유 또는 검색 요약 · **없음** = 못 찾음
> 덱 파일·claims.md는 수정하지 않았고, 최종보고서는 읽지 않았다. R1-ef-market.md와 R1-experience-interview.md에서 확정한 내용은 다시 조사하지 않았다.

## 한눈에 — 덱 문구 판정

| # | 덱 문구 | 판정 | 덱에 붙일 출처 |
|---|---|---|---|
| 1 | «인앱 웹뷰에는 GitHub 로그인 세션이 없어 OAuth에서 이탈하는 것으로 추정» | **«추정»을 유지하면 써도 됨.** 웹뷰가 브라우저와 로그인 상태를 공유하지 않는다는 점은 표준 문서가 **직접** 뒷받침한다. GitHub에 특정된 근거와 독립적인 전환율 수치는 **없음** | RFC 8252 §8.12 · Google 개발자 블로그(2021 웹뷰 차단) |
| 2 | «가입 30%가 밤 9시~새벽 1시 — 취준생은 밤에 준비합니다» | **외부 근거 없음.** «자체 가입 데이터 기준»으로만 쓸 것. «취준생은 밤에 준비한다»는 일반화는 빼거나 «우리 사용자는»으로 바꿀 것 | 내부 데이터 |
| 3 | 경쟁사 표 (Greenroom 3칸, 3개 서비스의 GitHub 입력, 사람인 자사 공고) | **표는 유지할 수 있다.** 단 Greenroom은 «레포를 읽는다»를 인정하고, «본인 커밋 구분·질문별 근거·공고 맞춤»은 «공개 페이지에서 확인 안 됨»으로 표기할 것 | 각 서비스 공개 페이지(2026-11-06 확인) |
| 4 | «개발 취준생 약 2~4만 명(내부 추정)» | **직접 앵커 없음.** 상위 모수(청년 취업시험 준비자 58.5만)와 국비 교육 정원(KDT 연 5.8만)만 간접 앵커로 확보. «20.4만»의 출처는 못 찾음 | 통계청 청년층 부가조사 2025.5(언론 경유) |

---

## 1. Instagram 인앱 브라우저 이탈

**우리 데이터:** 인앱 유입 가입 전환 0.10~0.15% vs 그 외 1.2~1.5% (약 10배 차이)

| ID | 자료 | 핵심 인용·수치 | 상태 | 직접성 | 한계 |
|---|---|---|---|---|---|
| F1 | **IETF RFC 8252 «OAuth 2.0 for Native Apps» §8.12** — https://www.rfc-editor.org/rfc/rfc8252 | "embedded user-agents **do not share the authentication state with other apps or the browser**, requiring the user to log in for every authorization request, which is often considered an inferior user experience." / "native apps MUST NOT use embedded user-agents to perform authorization requests and allows that authorization endpoints MAY take steps to detect and block authorization requests in embedded user-agents." / §4 "Being able to use the existing authentication session in the browser enables single sign-on" | 직접 (Worker 열람) | **직접 — 메커니즘** | 표준 권고 문서다. 이탈률 수치는 없다 |
| F2 | **Google Developers Blog — «Upcoming security changes to Google's OAuth 2.0 authorization endpoint in embedded webviews»** — https://developers.googleblog.com/en/upcoming-security-changes-to-googles-oauth-20-authorization-endpoint-in-embedded-webviews/ | "All embedded webviews will be blocked starting on September 30, 2021." 오류 코드 `disallowed_useragent` | 직접 (Worker 열람) | 직접 — 대형 IdP가 웹뷰 OAuth를 차단한 선례 | Google 사례다. GitHub이 같은 정책을 쓴다는 근거는 없다 |
| F3 | Buffer 엔지니어링 블로그 — https://buffer.com/resources/digging-into-failed-redirects-within-android-webviews/ | Android WebView에서 Instagram OAuth가 "hang on the authentication screen without redirecting" | 직접 (Worker 열람) | 간접 — 웹뷰 OAuth 실패 사례 | 원인은 앱의 DOM storage 설정이라 일반화하기 어렵다 |
| F4 | Felix Krause, «iOS Privacy: Instagram and Facebook can track anything…» (2022) — krausefx.com | Instagram은 외부 링크를 인앱 브라우저로 열고 사용자가 끌 수 없다. SFSafariViewController는 "loads pages outside of SocialApp's process space" | 직접 (Worker 열람) | 간접 — 인앱 브라우저 강제 | **쿠키·세션 격리 근거로 인용하면 안 된다.** 그 내용은 글에 없다 |
| F5 | Escape Hatch 사례 — https://getescapehatch.com/case-studies | 인스타 트래픽 50/50 테스트에서 Safari로 내보낸 쪽의 체크아웃 전환 **+30%~+241%** (예: 18만 명 +40%, z=8.7) | 벤더 경유 | 간접 — 인앱 전환 저하 수치 | 인앱 탈출 도구를 파는 벤더의 자체 보고다. 이커머스 결제 기준이고 로그인이 아니다 |
| F6 | «Instagram 1.2% · Facebook 1.5% · 네이티브 3.4%» 류 수치 | — | 스니펫만, 출처 불명 | — | **인용 금지** |
| — | WKWebView가 Safari와 쿠키를 공유하지 않는다는 Apple 공식 문서 | — | **못 찾음**(Apple 원문 미열람, 2차 서술만 있음) | — | 1차 인용 불가 |
| — | GitHub 공식 문서·커뮤니티의 Instagram 인앱 로그인 실패 / GitHub의 웹뷰 차단 정책 | — | **못 찾음** | — | — |

**덱 권고**
- 각주: «웹뷰는 브라우저의 로그인 상태를 공유하지 않음 (IETF RFC 8252 §8.12) · Google은 2021년 웹뷰 OAuth를 차단 (`disallowed_useragent`)».
- **«입증»이 아니라 «정합적 가설»로 쓸 것.** 외부 벤더 격차는 약 1.4~3.4배인데 우리 격차는 약 10배라, 외부 근거로 설명되는 폭을 넘는다.
- 가장 강한 보강은 자체 A/B다. 인앱 유입을 외부 브라우저로 유도하는 버전과 비교하면 된다.

## 2. 야간 가입 «밤 9시~새벽 1시 30%»

| ID | 자료 | 내용 | 상태 | 직접성 |
|---|---|---|---|---|
| N1 | Indeed «Timing Matters in the Job Search» (2016, 미국) — https://indeed.com/lead/timing-matters-in-the-job-search | 재직 중 구직자는 월~수 **저녁 7~10시** 검색이 가장 많고, 일요일 저녁 6~9시에 급증한다. 전체 피크는 화요일 11~12시다. 실업·저학력 구직자는 10~16시에 몰린다 | 직접 (Worker 열람) | 간접 — 미국, 2016년, 취준생 특정 아님, 새벽 구간 없음 |
| — | 잡코리아·사람인·인크루트·원티드·링커리어·캐치의 이용 시간대 통계 | — | **못 찾음** | — |
| — | 모바일인덱스·와이즈앱 시간대 데이터 / 심야 지원 비율 / «밤에 자소서» 설문 | — | **못 찾음** | — |
| — | (참고·시간대 아님) 사람인 «구직자 48.2%가 마감 2~3일 전 접수», 잡코리아 «자소서 하루 평균 약 242분(2016)» | — | 언론 경유, 스니펫 | 관련 약함 |
| ⚠️ | TribePad(영국) «지원의 61%가 근무시간 중, 저녁 27%» | — | 스니펫 | **반대 방향이므로 인용하지 말 것** |

→ **판정: 한국 외부 근거 없음.** «자체 가입 데이터 기준(n=…)»으로 표기한다. 해외 참고로 Indeed 2016을 쓸 수는 있다. 다만 «미국 재직 구직자의 평일 저녁 검색 피크»까지만 쓰고, 취준생이나 새벽으로 넓히면 안 된다.
→ 후속 후보(미열람): KIHASA 2024 생활시간조사 원자료 분석 https://www.kihasa.re.kr/api/kihasa/file/download?seq=34280

## 3. 경쟁사 표 (2026-11-06 공개 페이지 기준)

### Greenroom (usegreenroom.app) — 홈·/compare·/prep·/about·/blog 목록 열람
| 질문 | 답 | 근거 |
|---|---|---|
| GitHub을 읽나 | **예** | "Ari reads your repos before the session starts." / FAQ "The conversation is built from your GitHub repos, your target role, and your interview timeline." / /about "We read your repos to personalise your session." (Opus·Worker 모두 확인) |
| 본인 커밋을 구분하나 | **확인 안 됨** | commits·contributions 문구 0건 |
| 질문마다 근거를 보여주나 | **확인 안 됨** | 홈 목업에 "// Your repo: redis-job-queue" + "Why did you choose at-least-once delivery"가 있을 뿐, 파일·코드를 인용한다는 기능 설명은 없다 |
| 특정 공고에 맞추나 | **확인 안 됨** | 맞춤 기준은 "target role"과 타임라인이다. /prep은 Amazon·Google·Meta 정적 가이드다 |
| 가격·시장 | Free / Pro $10 / Premium $20 ("GitHub repo analysis"는 Pro), 인도 중심(₹ 프로모션) | |

### GitHub·코드 입력 여부
| 서비스 | GitHub·코드 입력 | 근거 |
|---|---|---|
| Final Round AI (finalroundai.com/ai-mock-interview) | **없음(언급 없음)** | 입력은 "Your Goal, including the target role, company, job description, resume and uploaded materials." 도움말 센터는 못 찾음 |
| 사람인 AI 모의면접 (m.saramin.co.kr/member/ai-interview) | **없음(언급 없음)** | "Ai 면접관이 이력서 내용을 분석해…" (Opus 확인) |
| 꼬꼬면 (kokomen.kr) | **없음(언급 없음)** | 사이트에 GitHub·채용공고 문구가 없다. GeekNews(2026-04-15) 소개에는 «지원 공고 기준으로 점수화 + 개선점 제안», «기술 스택별 실전 질문»이 있다. 공고 칸은 «일부»일 수 있으니 재확인 권장 |

### «사람인은 자사 공고만»
- 원문은 "**사람인 채용 공고 URL만** 입력하면, 기업과 지원 직무에 맞춘 맞춤형 면접 연습이 가능해요." (Opus 확인, 11-06)
- 다른 사이트 URL이나 붙여넣은 JD를 받는다는 문구는 없다. 거부한다는 명시도 없다.
- → **«사람인 공고 URL 기준»**이 가장 안전하다. «자사 공고만»도 문구상 맞다.
- 부수 발견: 원티드 AI 면접코칭도 «원티드 공고 URL»을 안내한다고 한다. 제3자 블로그 경유라 간접이다.

### 국내에서 GitHub을 읽어 면접 질문을 만드는 서비스
| 서비스 | 내용 | 성격 | 본인 커밋 구분 | 상태 |
|---|---|---|---|---|
| techGiterview — github.com/hong-seongmin/techGiterview (GeekNews news.hada.io/topic?id=22760) | 레포 링크를 넣으면 파일 기반 질문을 만들고 모의면접으로 이어진다. Gemini·GitHub 키가 필요하고 개발 중이다 | 오픈소스 사이드 프로젝트 | 언급 없음 | 간접 |
| Giterview (Medium @nakyung.ahn.03) | "본인의 깃허브 계정을 연동시켜 … 레포지토리를 가져오고" | 사이드 프로젝트 추정, 약 3년 전 글이라 운영 여부 불명 | 언급 없음 | 스니펫만 |
| GitHub Interview Question Generator (Greasyfork 540120) | 현재 디렉터리 파일 최대 5개, public 레포만 | 유저스크립트 | 커밋 아님 | 간접 |
| 원티드·프로그래머스·잡코리아·인프런·코드잇·점핏·디스콰이엇 | 커밋 단위 분석 서비스는 못 찾음 | — | — | 검색만 함, 전수 조사 아님 |

→ **«경쟁자 없음» 류 주장은 쓰면 안 된다.** 해외에는 Greenroom(상용)이 있고, 국내에는 techGiterview 같은 사이드 프로젝트가 있다.
→ **방어 가능한 문장:** «공개 페이지 기준으로, 팀 레포에서 **본인 커밋만** 골라 + 질문마다 **근거 코드**를 보여주고 + **한국 채용 공고 단위**로 맞추는 서비스는 확인되지 않았다(2026-11-06)».

## 4. 시장 규모

### 4-a. 사람인·점핏 2025 상반기 리포트 — R1-ef-market.md에서 확정 (다시 조사하지 않음)
- 공고 **92,341건** · 지원 **2,601,390건** (점핏 리포트 랜딩 https://jumpit.saramin.co.kr/report/2025/recruit, **직접**)
- → «약 10만 건»은 틀렸다. **«약 9.2만 건»**이 맞다. 출처는 «언론 보도 경유»에서 **«점핏 리포트(직접)»**로 올릴 수 있다.
- 신입 공고 0.8% · 신입 지원 29.5%는 리포트 랜딩에 없고 이투데이·뉴스투데이 경유다(**간접**).

### 4-b. «개발 취준생 약 2~4만 명» 외부 앵커
| ID | 자료 | 수치 | 상태 | 직접성 | 한계 |
|---|---|---|---|---|---|
| M1 | 통계청 경제활동인구조사 청년층 부가조사 (2025.5) — 대구MBC 2025-07-26 https://dgmbc.com/NewsArticle/632760 | 15~29세 비경제활동인구 중 **취업시험 준비자 58.5만 명(14.5%)**, 전년보다 2만 명 증가. 준비 분야는 일반기업체 36.0% · 공무원 18.2% · 기능자격 17.8% | 언론 경유 (페이지 열람) | 간접 — 상위 모수 | 개발 직군 분리값은 없다. KOSIS 원자료가 필요하다 |
| M2 | 같은 조사 — 뉴데일리 2025-07-24 https://biz.newdaily.co.kr/site/data/html/2025/07/24/2025072400277.amp.html | 청년 인구 797.4만 · 최근 졸업자 268.1만 · 미취업자 주된 활동 «직업교육·취업시험 준비» 40.5% | 언론 경유 | 간접 | 같은 한계 |
| M3 | K-디지털 트레이닝 2024 상반기 1차 선정 — 헤럴드경제 2024-04-05 https://v.daum.net/v/20240405100138376 | 연 훈련 규모 **57,689명** (기존 38,877 + 신규 18,812) | 언론 경유 | 간접 — 개발 교육 공급 규모 | 정원이지 수료자가 아니다. 비개발 디지털 과정도 포함된다 |
| M4 | KDT 성과 — 한경비즈니스 https://magazine.hankyung.com/business/article/202511081461b | 2023년 취업률 50.3%, 예산 2021년 2,224억 → 2025년 4,781억 | 언론 경유 | 간접 | — |
| — | 교육통계(KESS)·대학알리미의 연간 SW/컴퓨터 전공 졸업자 수 | — | **못 찾음** (웹 검색으로는 집계값이 안 나온다. kess.kedi.re.kr 또는 academyinfo.go.kr 직접 조회가 필요하다) | — | — |
| — | KDT 연간 수료자 · 개발자 취준생 직접 추정 | — | **못 찾음** | — | — |
| ⚠️ | SSAFY 기수당 약 950명 / 누적 수료 1.2만 명 이상 · SPRi 2023 «SW융합인력 33만» | — | 스니펫만 | — | **재확인 전 인용 금지** |

- **«20.4만»의 출처는 못 찾음.** 가장 가까운 값은 58.5만 × 일반기업체 36.0% ≈ 21.1만이다(계산값이며 20.4만과 일치하지 않는다). 20.4만이 무엇인지 덱 담당자가 확인해야 한다.
- 2~4만은 58.5만의 약 3.4~6.8%다. 개발 직군 비중은 여전히 ⚙ 가정이다.
- **덱 권고:** «청년 취업시험 준비자 58.5만 명(통계청, 2025.5) 중 개발 직군 비중을 가정(⚙)해 2~4만 명 추정». KDT 연 5.8만 명 정원은 «개발·디지털 교육 공급 규모» 참고 각주로 쓸 수 있다.

---

## Research Trace
- Worker 4개(인앱 · 야간 · 경쟁사 · 시장)를 병렬로 돌렸다. Opus는 SW 전공 졸업자 수를 추가로 1회 검색했다(집계값 못 찾음).
- 경쟁사 Greenroom·사람인 문구는 오늘(R1) Opus가 원문을 다시 확인했다. Final Round AI·꼬꼬면은 Worker가 확인했다(WebFetch 요약 경유라 인용은 재진술일 수 있음).
- 접근 실패: Apple WKWebView 공식 문서, Facebook 개발자 커뮤니티 스레드, Medium(403), 삼성뉴스룸(타임아웃), KOSIS 원자료, KIHASA PDF.
- 반대 근거는 따로 찾지 않았다. 조사 중 나온 것(TribePad, 외부 격차 1.4~3.4배 vs 우리 10배)만 기록했다.
