# H. 시장·문제 근거 수치 수집 (p3 문제 / p23 시장)

> 작성 2026-11-05 · 범위: 공개 웹 자료만(로그인·양식 없음) · 목적: 소마 17기 최종평가 덱 p3·p23 교체용
> 등급: 🟢 1차/공식 · 🟡 신뢰할 만한 2차(기업 자체조사·언론 경유) · 🔴 약함(덱 사용 금지)
> 원칙: 각 수치는 **원문 확인 여부**를 같이 적었다. "원문 확인"은 발행처 페이지를 직접 열어 본 것, "언론 경유"는 기사만 본 것.

---

## 0. 결론 먼저

**p3 단일 최선 수치 (추천)**
> **채용 담당자 60%: "AI 때문에 지원자의 실제 역량을 평가하기 더 어려워졌다"**
> — WGU *Workforce Decoded* 2026, 미국 채용 실무자 N=3,128 (Centiment 실사, 2026-06-24~07-07), 발표 2026-09-30. 🟡 (원문 확인)

이유: DevFit의 판별 기준 "알고 짰는가"와 문장이 1:1로 맞고, 표본·실사기관·기간이 공개돼 있으며 2026년 최신이다. 단점은 미국 표본 — 슬라이드에 "미국" 명시.

보조로 한 줄 더 쓸 수 있다면 공급 쪽 사실을 짝지운다:
> **개발자 84%가 AI 도구를 쓰거나 쓸 계획 — 그러나 46%는 정확도를 불신** (Stack Overflow Developer Survey 2025, 응답 ~33.6k) 🟡 (원문 확인)

**p23 추천 (≤6줄)**
1. 국내 개발자 채용공고 **약 10만 건 / 지원 약 260만 건 (2025 상반기, 사람인·점핏)** 🟡
2. 신입 비중: **공고 0.8% vs 지원 29.5%** — 신입은 공급 과잉, 검증 수단이 병목 🟡
3. 일반기업체 취업 준비 청년 **약 20만 명** (60만 × 34.0%, 국가데이터처 2026-05 청년층 부가조사) 🟢
4. 취업 사교육 이용 **42.9%**, 이용자 1인 **연 455만 원** (잡코리아 2025, N=485) 🟡
5. Bottom-up(국내, 기준안): **B2B TAM ~1,040억 · SAM ~104억 · SOM(3년) ~5억 / B2C 유료 SAM ~10억** — 전부 위 수치 × 내부 가격 앵커
6. 글로벌 "기술역량 스크리닝 SW" 시장보고서는 **$0.34B~$3.15B로 10배 엇갈림** → 덱에 단일 숫자로 쓰지 않음 🔴

⚠️ 기존 p23의 **5년 SOM ARR ≈ 27억은 공개 수치 기반 국내 bottom-up으로는 재현되지 않는다** (아래 §3에서 3년 SOM 0.8억~5.2억). 27억은 글로벌 SAM 가정에서 나온 내부 추정이므로, 덱에 남기려면 "글로벌 확장 가정"이라는 라벨이 필요하다.

---

## 1. 문제(p3) 후보 수치

| # | 수치 | 출처 · 발행처 · 연도 | 원문 인용(≤15단어) | 표본/방법 | 등급 |
|---|---|---|---|---|---|
| P1 | 채용 담당자 **60%** "AI로 실제 역량 평가가 어려워짐" | WGU Workforce Decoded 2026 · [press release](https://www.wgu.edu/newsroom/press-release/2026/09/ai-has-made-real-skills-harder-to-evaluate.html) | "60% say AI is making it harder to evaluate candidates' real skills." | 미국 채용 관여자 3,128명, Centiment, 2026-06-24~07-07 | 🟡 원문 확인 |
| P1-b | 같은 조사: 평가가 어려워졌다는 기업의 **54%**가 AI로 신입 채용 감소 (그 외 기업 20%) | 동일 | (상관관계, 인과 아님이라고 WGU가 명시) | 동일 | 🟡 |
| P2 | 개발자 **84%** AI 도구 사용/계획, **46%** 정확도 불신(신뢰 33%), **66%** "거의 맞지만 아닌" 결과가 최대 불만 | Stack Overflow Developer Survey 2025 · [AI 섹션](https://survey.stackoverflow.co/2025/ai) | "84% of respondents are using or planning to use AI tools" | 사용 문항 33,662 응답 / 신뢰 33,244 | 🟡 원문 확인 |
| P2-b | 2026판: AI를 "쉽게 검증할 수 있을 때만" 신뢰 **48%** | Stack Overflow 2026 · [AI 섹션](https://survey.stackoverflow.co/2026/ai) | 문항 구조가 2025와 달라 시계열 비교 금지 | — | 🟡 원문 확인(문항 해석 주의) |
| P3 | 개발자 **76%** "AI가 평가(코딩테스트)를 속이기 쉽게 만든다", **29%** 코드가 AI 생성(평균) | HackerRank 2025 Developer Skills Report · [report](https://www.hackerrank.com/reports/developer-skills-report-2025) | "76% say AI makes gaming assessments easier" (페이지 요약 기준) | 13,732명, 102개국, 2024Q4~2025초 | 🟡 원문 확인 · **벤더 자체조사**(이해상충) |
| P3-b | 같은 리포트: **78%** 평가가 실무와 불일치, **66%** 실무형 평가 선호 | 동일 | — | 동일 | 🟡 |
| P4 | 채용 관리자 **65%** 지원자의 기만적 AI 사용 적발, 미국 **39%** 대면면접 확대 | Greenhouse 2025 AI in Hiring Report · [newsroom 2025-11-19](https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair) | "Two in every three (65%) hiring managers have caught applicants using AI deceptively." | 4,136명(미·영·아일랜드·독), 그중 채용측 1,236 | 🟡 원문 확인 · ATS 벤더 |
| P5 | 2028년까지 지원자 프로필 **4명 중 1명** 가짜 (예측) / 지원자 **6%** 면접 사기 경험 | Gartner 2025-07-31 press release (원문 403, [HR Dive 경유](https://www.hrdive.com/news/fake-job-candidates-ai/757126/)) | Gartner 인용: "harder for employers to evaluate candidates' true abilities" | 지원자 ~3,000명(2Q25) | 🟡 언론 경유 — "예측"을 사실처럼 쓰지 말 것 |
| P6 | 개발자 공고 중 **신입 0.8%** vs 지원 중 **신입 29.5%** | 사람인·점핏 2025 상반기 개발자 채용 리포트 · [이투데이 2025-08-27](https://www.etoday.co.kr/news/view/2500510) | 공고 10만여 건·지원 260여만 건 분석 | 플랫폼 내부 데이터 | 🟡 언론 경유 · 원 리포트 미확인. "경력무관" 구간 처리 불명 → 수치 그대로 쓰되 출처 각주 필수 |
| P7 | JetBrains: 개발자 **85%** AI 도구 정기 사용 | JetBrains State of Developer Ecosystem 2025 (ITWorld 경유) | — | 24,534명, 194개국 | 🟡 언론 경유 |

### p3에 쓰지 말 것
- 🔴 **"잘못된 채용 비용 = 연봉 30%"** — 원출처 없음(금지 유지). 이번 조사에서도 1차 출처는 찾지 못했다.
- 🔴 Karat "엔지니어링 리더 71% AI로 기술평가 어려워짐" — 데모 도메인 페이지에서만 확인, Karat 원문 미발견.
- 🔴 Fabric "59% 채용관리자 AI 위장 의심" — 원조사 미확인.
- 🔴 무하유 "AI 자소서 10건 중 6건" — 커뮤니티 글 경유, 원 리포트 미확인.
- 국내 개발자 AI 도구 사용률 공식 통계(SPRi·NIPA·과기정통부)는 **찾지 못했다.** 국내 수치가 필요하면 "글로벌 조사 기준"으로 표기.

---

## 2. 시장(p23) 후보 수치

### 2-1. 국내 수요 측 (B2C)

| # | 수치 | 출처 | 등급 |
|---|---|---|---|
| M1 | 취업시험 준비 청년 **60만 명**, 그중 일반기업체 준비 **34.0%** (→ 약 20.4만 명, 곱셈은 본 문서 계산) | 국가데이터처(구 통계청) 2026-05 경제활동인구조사 청년층 부가조사, 발표 2026-07-23 · [korea.kr](https://www.korea.kr/news/policyNewsView.do?newsId=156771847), [뉴시스](https://mobile.newsis.com/view/NISX20260723_0003720080) | 🟢 (비율은 korea.kr 원문, 60만은 뉴시스) |
| M1-b | 2025-05: 일반기업체 준비 **36.0% / 21.1만 명** (2006년 이후 최고) | 같은 조사 2025판 (언론 경유) | 🟢 |
| M1-c | 미취업 졸업자 **124.3만 명**, 1년 이상 미취업 **48.6%** | 2026 청년층 부가조사 | 🟢 |
| M2 | 대졸 취준생 **42.9%** 취업 사교육 이용, 이용자 월 **38만 원 / 연 455만 원** (2021년 218만 원) | 잡코리아 콘텐츠LAB, N=485 · [아시아경제 2025-09-12](https://www.asiae.co.kr/en/article/2025091208015043842) | 🟡 비대표 표본 |
| M2-b | 사교육 항목 중 "IT·컴퓨터 활용" **32.7%**, "자소서·면접 컨설팅" **17.8%** (복수응답) | 동일 | 🟡 |
| M2-c | 캐치 조사: 구직자 월평균 취업 준비 비용 약 **28만 원** (N=1,001) | [뉴시스 2025-10-18](https://mobile.newsis.com/view/NISX20251018_0003367696) | 🟡 범위 정의 상이 |
| — | **국내 "개발자 취준생 수" 공식 통계는 없다.** SW 관련 학과 입학정원 "약 2만 명"(업계 설명, 2022 아시아경제)은 🔴. 교육통계(KESS) 계열별 졸업자로 직접 뽑아야 함 — 이번 범위에서 못 함 | | 🔴 |

### 2-2. 국내 구매 측 (B2B)

| # | 수치 | 출처 | 등급 |
|---|---|---|---|
| M3 | 2025 상반기 개발자 공고 **약 10만 건**, 지원 **약 260만 건**; 공고 1위 서버/백엔드 16.2% | 사람인·점핏 리포트 · [이투데이](https://www.etoday.co.kr/news/view/2500510) | 🟡 플랫폼 2곳 한정, 중복게시 포함 가능 |
| M4 | 공고 연차 분포: 5~10년 **39.7%**, 신입 **0.8%** / 지원: 신입 **29.5%** | 동일 | 🟡 |
| M5 | 대기업 정규직 신입 공고 2025-01~11 전년 대비 **-43%**, IT·통신에서 두드러짐 | 캐치 분석(언론 재인용) | 🔴 원문 미확인 |
| M6 | 국내 SW 인력 **64.3만 명** (2025, +0.2%) | SPRi "2025 SW산업 실태조사"라고 잡플래닛 기사가 인용 | 🔴 SPRi 원문 미확인 — 확인 전 사용 금지 |
| M7 | SW 매출 1,000억 이상 기업 **167개사**, SW 산업 매출 140.6조 원(2024 회계) | KOSA 2025 SW 천억클럽 · [바이라인 2025-11-25](https://byline.network/2025/11/25-499/) | 🟡 (대기업 세그먼트 크기 참고용) |

### 2-3. 글로벌

| # | 수치 | 출처 | 등급 |
|---|---|---|---|
| G1 | 미국 SW 개발자·QA 고용 2024~34 **+15%**, 연평균 openings **129,200** | U.S. BLS OOH · [link](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) | 🟢 (기존 01 문서에서 확인) |
| G2 | HackerRank 플랫폼: 개발자 2,600만, 연 **300만+ 평가** | HackerRank 2025 리포트 | 🟡 자사 수치 |
| G3 | "Technical Skills Screening Software" 2024 **$339M** (Spherical Insights) vs 2025 **$3.15B** (Wise Guy Reports) | 유료 리포트 티저 | 🔴 정의·방법론 비공개, 10배 차이 |
| G4 | "Technical Assessment Platform" 2025 **$3.5B~$5.8B** (WiseGuy / DataHorizzon / MarketIntelo) | 유료 리포트 티저 | 🔴 |
| G5 | Gartner Market Guide for Technical Skills Assessment Platforms (2024) — **시장규모 수치 없음**. "Gartner $2.8B"는 벤더 블로그 귀속뿐 | [Gartner abstract](https://www.gartner.com/en/documents/5368363) | 🔴 ($2.8B는 내부 03 문서 TAM과 같은 숫자 — 출처 불명이므로 덱에서 제거 권고) |

→ **글로벌 TAM은 단일 숫자로 쓰지 말 것.** 쓰려면 "시장조사기관 추정치 $0.3B~$3B+, 방법론 비공개로 편차 10배"처럼 범위+경고로만.

---

## 3. Bottom-up TAM / SAM / SOM (국내, 공개 수치 × 명시 가정)

### 가정 표 (🟢🟡 = 외부 수치, ⚙ = 내부 가정)

| 기호 | 값 | 근거 |
|---|---|---|
| A | 개발자 공고 지원 **520만 건/년** | M3 260만 × 2 (⚙ 하반기 동일 가정, 2개 플랫폼만 — 원티드·잡코리아 제외로 과소, 중복지원으로 과대) |
| B | 면접 대상 비율 **5% (보수) / 10% (기준)** | ⚙ 서류 통과율 가정 |
| C | 지원자 1인당 가격 **₩10,000 (보수) / ₩20,000 (기준)** | ⚙ `planning/03-B2B-트랙.md` §5-1 티어의 1인 단가 ₩10,000~30,000 하단. 원가 실측 ₩1,000~2,000 (07 문서) |
| D | 일반기업체 취준 청년 **20.4만 명** | M1 🟢 |
| E | 그중 개발 직군 비중 **10% (보수) / 20% (기준)** | ⚙ (공고 중 개발·IT 비중 19.9%라는 민간 분석이 상한 참고, 🔴) |
| F | 취업 사교육 지불 비율 **42.9%** | M2 🟡 |
| G | 사교육 이용자 연 지출 **₩455만** | M2 🟡 |
| H | DevFit B2C 연 결제 가정 **₩30,000 (보수) / ₩60,000 (기준)** | ⚙ 공고 시즌 1~2회 × 월 결제 가정. 가격 미정(02 문서: 가격표 미노출) |

### B2B (국내)

| | 식 | 보수 | 기준 |
|---|---|---|---|
| **TAM** — 모든 개발자 지원을 1인 단가로 분석 | A × C | 520만 × ₩1만 = **520억** | 520만 × ₩2만 = **1,040억** |
| **SAM** — 면접 대상자만 | A × B × C | 26만 × ₩1만 = **26억** | 52만 × ₩2만 = **104억** |
| **SOM (3년)** — SAM 점유 | SAM × 3% / 5% | **0.8억** | **5.2억** |

참고: 내부 03 문서 SOM 3년 = 유료 200곳 × 연 ARPU ₩156만 ≈ **3.1억** → 위 범위(0.8~5.2억) 안에 들어온다. 두 경로가 맞물리므로 **3년 SOM "약 3억 원대"는 방어 가능**. 반면 5년 ARR 27억은 국내만으로는 SAM(104억)의 26%를 요구 — 근거 부족.

### B2C (국내)

| | 식 | 보수 | 기준 |
|---|---|---|---|
| 대상 인구 | D × E | 2.04만 명 | 4.08만 명 |
| **TAM** — 개발 취준생의 취업 사교육 총지출 | D × E × F × G | 8,752명 × ₩455만 = **398억** | 17,503명 × ₩455만 = **796억** |
| **SAM** — 지불 의향층 × DevFit 가격 | D × E × F × H | 8,752 × ₩3만 = **2.6억** | 17,503 × ₩6만 = **10.5억** |
| 참고: 면접·컨설팅 항목 이용자 | D × E × F × 17.8% | 1,558명 | 3,116명 |

해석: **B2C 국내 매출 시장은 작다(SAM 수억~10억).** B2C는 매출이 아니라 사용자 규모(대상 2~4만 명 중 도달률)로 말하는 편이 정직하고, 07 전략 문서의 "B2C = 사용자 수 성과" 프레임과도 맞는다. 덱에서는 "대상 개발 취준생 약 2~4만 명 / 그중 사교육 지불 42.9%"를 쓰고 원화 TAM은 B2B 쪽에 싣기를 권한다.

### 민감도 메모
- E(개발 비중)가 가장 약한 가정이다. KESS 컴퓨터·통신 계열 졸업자 수를 뽑으면 🟢로 대체 가능.
- 취업시험 준비자(60만)는 "시험 준비 중인 비경제활동 청년"만 센다 — 재직 중 이직 준비, 부트캠프 수강생은 빠져 **과소 추정** 방향.
- A는 지원 "건수"이지 사람 수가 아니다. 중복지원이 많아 B2C 인구 추정에는 쓰지 않았다.

---

## 4. 덱 문구 제안 (복붙용)

**p3**
> 채용 담당자의 **60%**가 "AI 때문에 지원자의 실제 역량을 평가하기 더 어려워졌다"고 답했다.
> *출처: WGU Workforce Decoded 2026 (미국 채용 실무자 3,128명)*

(보조) 개발자 84%가 AI 코딩 도구를 쓰지만, 46%는 그 결과를 믿지 않는다. *— Stack Overflow Developer Survey 2025*

**p23**
> 국내 개발자 채용: 반기 공고 10만 건 · 지원 260만 건 (사람인·점핏, 2025 상반기)
> 신입은 지원의 29.5%를 차지하지만 공고의 0.8%뿐
> B2B SAM ≈ 104억 원 = 면접 대상 52만 명/년 × 1인 2만 원 (보수 26억)
> 3년 SOM ≈ 3억 원대 (상향식 0.8~5.2억 · 내부 고객수 기반 3.1억 일치)
> B2C: 일반기업체 취준 청년 20.4만 명(국가데이터처) 중 개발 직군 2~4만 명, 42.9%가 취업 사교육 지출(연 455만 원)

---

## 5. 출처 목록

- WGU, "AI has made real skills harder to evaluate" (2026-09-30) — https://www.wgu.edu/newsroom/press-release/2026/09/ai-has-made-real-skills-harder-to-evaluate.html
- Stack Overflow Developer Survey 2025, AI — https://survey.stackoverflow.co/2025/ai
- Stack Overflow Developer Survey 2026, AI — https://survey.stackoverflow.co/2026/ai
- HackerRank 2025 Developer Skills Report — https://www.hackerrank.com/reports/developer-skills-report-2025
- Greenhouse 2025 AI in Hiring Report (2025-11-19) — https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair
- Gartner (2025-07-31) via HR Dive — https://www.hrdive.com/news/fake-job-candidates-ai/757126/
- 이투데이, 사람인-점핏 2025 상반기 개발자 채용 리포트 (2025-08-27) — https://www.etoday.co.kr/news/view/2500510
- 정책브리핑, 2026 청년층 부가조사 (2026-07-23) — https://www.korea.kr/news/policyNewsView.do?newsId=156771847
- 뉴시스, 2026 청년층 부가조사 — https://mobile.newsis.com/view/NISX20260723_0003720080
- 아시아경제, 잡코리아 취업 사교육 조사 (2025-09-12) — https://www.asiae.co.kr/en/article/2025091208015043842
- 뉴시스, 캐치 취업준비 비용 조사 (2025-10-18) — https://mobile.newsis.com/view/NISX20251018_0003367696
- 바이라인네트워크, KOSA SW 천억클럽 (2025-11-25) — https://byline.network/2025/11/25-499/
- U.S. BLS OOH, Software Developers — https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Gartner Market Guide abstract — https://www.gartner.com/en/documents/5368363
- (🔴 참고만) Spherical Insights, Wise Guy Reports, MarketIntelo, DataHorizzon 시장 리포트 티저
