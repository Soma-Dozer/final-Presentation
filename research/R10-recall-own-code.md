# R10 — «취준생은 전에 짠 자기 코드를 다시 보기 힘들고, 면접에서 그 코드를 기억하지 못한다»

> 조사일 2026-11-10 · 요청: ppt-start (최종발표 Problem 장 5쪽)
> 1절은 Opus가 논문 PDF 원문을 직접 받아 확인했다. 2~4절은 Sonnet 작업자가 조사했고, 핵심 인용은 Opus가 다시 열어 확인했다.
> 표기: **✅** = 1차 출처 원문 확인 · **✅★** = Opus가 원문 문장을 직접 재확인 · **📰** = 2차 인용만 · **⚠** = 한계·주의
> 덱·claims.md·최종보고서는 열지 않았다.

## ⭐ 장표 추천 (맨 위)

**숫자 1~2개**
1. **«30일이면 자기 코드의 절반을 잊는다»** — 오픈소스 개발자 60명이 «파일의 절반을 잊는 데 걸리는 기간»을 중앙값 30일로 답했다. 본인 추정치다. (Krüger et al., ICSE 2018) ✅★
2. **«개발 시간의 58%는 코드를 읽고 이해하는 데 쓴다. 경력 3년 미만은 66%»** — 현업 개발자 78명, 3,148 작업시간을 실측했다. (Xia et al., IEEE TSE 2017/2018) ✅★

**문장 2~3개**
- A. «개발자는 자기가 쓴 코드도 한 달이면 절반을 잊는다고 답한다. (Krüger et al., 2018, n=60)»
- B. «현업 개발자도 시간의 58%를 코드를 이해하는 데 쓴다. 경력이 짧을수록 그 비율은 66%로 올라간다. (Xia et al., 2018, n=78)»
- C. «채용 담당자들은 "이력서에 적어둔 프로젝트를 물어보면 답변을 못하는 분들을 많이 봤다"고 말한다. (OKKY×바이라인네트워크, 2025-02, IT 전문가 71명)» — R4에서 이미 확인 ✅★

**AI 연결 보조:** «AI로 코딩한 그룹은 방금 쓴 라이브러리에 대한 이해도 퀴즈에서 50%를 받았다. 손으로 짠 그룹은 67%였다. (Anthropic, 2026-01, 52명)» ✅

**쓰지 말 것:** «취준생 N%가 면접에서 자기 코드를 기억 못 한다» 같은 설문 수치. 그런 조사는 **찾지 못했다.**

## 한눈에

| # | 질문 | 판정 | 핵심 근거 |
|---|---|---|---|
| 1 | 개발자가 자기 코드를 잊는다는 정량 근거 | **강함 (연구)** | Krüger 2018: 파일 절반 망각 중앙값 30일·평균 40일, n=60 ✅★ · Xia 2018: 이해 활동 58%, n=78 ✅★ |
| 2 | 취준생이 면접에서 자기 프로젝트 설명에 막힌다는 설문·후기 | **약함** — 정량 설문은 못 찾음, 후기만 있음 | velog 후기 «내가 진행한 프로젝트들에 관해서 묻는데도 '아 ... 그거 뭐였더라'» ✅★ (면접 준비 단계의 일) |
| 3 | 면접관 관찰 «본인 프로젝트를 설명 못 한다» | **중간** | OKKY 채용 담당자 발언 ✅★ (n=71, 표본 작음) · 개발자 면접관 대상 정량 설문은 못 찾음 |
| 4 | 포트폴리오 레포의 커밋 수·레포 수 규모 | **못 찾음** | 부트캠프·우테코·소마 평균 커밋 수 통계 없음 |

⚠ 이 주장을 **직접** 다룬 자료는 없다. «취준생이 자기 코드를 다시 읽기 힘들다»를 직접 잰 연구나 설문은 찾지 못했다. 장표는 «개발자 일반의 망각 연구(1번)» + «면접관 관찰(3번)» 두 갈래로 간접 구성해야 한다.

---

## 1. 자기 코드 망각·코드 이해 비용 (연구)

### 1-1. Krüger, Wiemann, Fenske, Saake, Leich — «Do You Remember This Source Code?» (ICSE 2018) ✅★
- 원문 PDF(저자 preprint): https://jacobkrueger.github.io/assets/papers/Krueger2018Remember.pdf · DOI 10.1145/3180155.3180215 · 접근 2026-11-10
- 표본: «an empirical study that we conducted with **60 open-source developers**», «from 10 GitHub projects». 설문 응답을 각자의 커밋 기록과 대조했다.
- 핵심 문장 (5.2절): «our participants state that they **forget half of their files after 30 days in the median and 40 days on average**.»
  - ⚠ 측정값이 아니다. 개발자 본인이 «절반을 잊는 데 며칠 걸리나»에 답한 **자기 추정치**다.
- 결론 (초록): «The results show that **forgetting is an important factor** when considering familiarity and program comprehension of developers.»
- ⚠ 반대 방향 결과 (같은 논문, 2019 요약본 https://jacobkrueger.github.io/assets/papers/Krueger2019UnderstandingForget.pdf):
  - «repetitions as well as the ratio of own code are significantly positively correlated to familiarity». 같은 파일을 여러 번 고쳤거나 내가 쓴 코드의 비율이 높으면 더 오래 기억한다.
  - Ebbinghaus 망각곡선은 «only applicable if a developer edited a file only once»일 때만 들어맞았다. 커밋을 한 번만 한 27명이 여기에 해당한다.
  - → 장표에서는 «한 번 짜고 다시 안 본 코드일수록 빨리 잊는다»로 쓰는 편이 원문에 더 가깝다. 취준생의 팀 프로젝트(짧게 만들고 끝나는 코드)에 맞는 조건이다.

### 1-2. Xia, Bao, Lo, Xing, Hassan, Li — «Measuring Program Comprehension: A Large-Scale Field Study with Professionals» (IEEE TSE vol.44 no.10, 2018. 온라인 2017) ✅★
- 원문 PDF: https://xin-xia.github.io/publication/TSE17.pdf · DOI 10.1109/TSE.2017.2734091 · 접근 2026-11-10
- 표본: «seven real projects, on **78 professional developers**, and amounting to **3,148 working hours**». IDE 밖(브라우저·문서 편집기)의 활동까지 자동으로 기록했다.
- 핵심 문장: «on average developers spend **58 percent** of their time on program comprehension activities»
- 경력별 수치 (RQ4): «developers of low, medium, and high experience spend **66.37, 55.97, and 44.43 percent** of their time on program comprehension». 저경력은 경력 3년 미만, 고경력은 5년 초과다.
- ⚠ «자기 코드」가 아니라 **코드 일반**을 이해하는 시간이다. «다시 읽는 데 드는 비용이 크다»를 보여 주는 근거이고, «자기 코드를 잊는다»를 직접 보여 주지는 않는다.

### 1-3. Minelli et al. 2015 (ICPC) — 이해 활동 70% 📰
- Xia 논문 서론의 인용: «Minelli et al. study the IDE interactions of 18 developers over 700 working hours, and find that on average developers spend **70 percent** of their time performing program comprehension activities»
- ⚠ 같은 문단에서 Xia가 한계를 지적한다. 18명 중 현업은 7명이고, 데이터의 85% 이상이 박사과정생 3명에게서 나왔다. **58%(Xia)를 쓰고 70%는 쓰지 말 것.**

### 1-4. (AI 연결 보조) Anthropic — «How AI assistance impacts the formation of coding skills» (2026-01-29) ✅
- https://www.anthropic.com/research/AI-assistance-coding-skills · 논문 https://arxiv.org/abs/2601.20245 · 접근 2026-11-10
- 표본: «52 (mostly junior) software engineers». 모르는 Python 라이브러리(Trio)로 과제를 하게 한 무작위 실험이다.
- 원문: «participants in the AI group scored **17% lower** than those who coded by hand». 퀴즈 평균은 AI 그룹 50%, 직접 코딩 그룹 67%다.
- 원문: «The largest gap in scores between the two groups was on **debugging questions**.»
- ⚠ 원문의 한계: «Our sample was relatively small, and our assessment measured comprehension **shortly after** the coding task.» 장기 망각을 잰 연구가 아니다. 🏷 AI 회사의 자체 연구다.
- ⚠ 「17% lower」는 67→50, 즉 **17%p** 차이다. 장표에서는 «50% vs 67%»로 쓰는 편이 오해가 적다.

## 2. 취준생·신입 — 면접에서 자기 프로젝트 설명에 막힘

**정량 설문: 못 찾음.** «프로젝트 질문에 답하지 못함 N%» 같은 개발자 설문은 국내·해외 모두 없었다.
- ⚠ keduitcenter.co.kr의 «60% 이상 신입 개발자들이 실무 경험 부족을 실패 원인»은 원자료를 확인할 수 없다. 인용 금지.

후기 (개인 경험 ⚠, 원문 확인):
1. **velog @jpy1030, 2025-05-08** «2025 팀네이버 신입 공채 1차 면접 탈락 회고» ✅★ — https://velog.io/@jpy1030/2025-팀네이버-신입-공채-1차-면접-탈락-회고
   - «가장 어려운 건 나/내 포트폴리오/내 기술 블로그 등에 관한 면접 질문이었다.»
   - «심지어 내가 진행한 프로젝트들에 관해서 묻는데도 '아 ... 그거 뭐였더라' 이 생각만 계속 들었다.»
   - ⚠ 실제 면접이 아니라 **면접 준비(모의 면접 스터디) 단계**에서 한 말이다. 실제 2차 면접에서는 연습한 질문이 나왔다고 썼다.
2. velog @yuhyerin, 2024-09-19 (면접관 관점, **경력직** 대상) ✅ — https://velog.io/@yuhyerin/기술-면접에서-탈락하는-개발자-유형-경력직-기술-면접을-대하는-태도
   - 프레임워크 선택 이유를 물으면 «그냥요... 유명해서요...»라고 답하는 «대충형» 사례.

간접 설문 (전 직군 ⚠):
- 사람인, 기업 927곳, 2020-07 ✅ (뉴스1 경유, https://www.fnnews.com/news/202007090938403194)
  - 83.8%가 «지원자의 거짓말을 판단한 경험이 있다»고 답했다.
  - 거짓말이라고 판단하는 경우 1위는 «답변의 근거가 불충분할 때» 46.3%(복수응답)다.
  - ⚠ 개발자에 한정하지 않았고, «근거 불충분»이 «기억 못 함»과 같지 않다. 장표에 넣지 않는 편이 좋다.

## 3. 면접관 관찰

- **OKKY × 바이라인네트워크, 2025-02-28** ✅★ (R4 V2에서 확인) — https://byline.network/2025/02/27-431/ · IT 전문가 71명
  - 채용 담당자 발언: «스스로 이력서에 적어둔 프로젝트에 대해 물어보면 답변을 못하는 분들을 많이 봤다»
  - ⚠ 표본이 작다(71명). 수치가 아니라 응답자 1명의 발언이다.
- 원티드랩 brunch, 2017-11-24 ✅ — https://brunch.co.kr/@wantedlab/43
  - «"A에서 C로 안 가고 왜 B로 갔느냐"라는 그다음 질문에 대답할 수 없다»
  - ⚠ 거짓 경력을 걸러내는 맥락이지 기억 문제가 아니다.
- velog @okorion, 2026-06-10 «AI 시대의 개발자 면접을 어떻게 설계해야 할까» ✅ (블로그 의견) — https://velog.io/@okorion/AI-시대의-개발자-면접을-어떻게-설계해야-할까-h3exijf9
  - «AI가 설계를 제안하고, 코드를 만들고 … 면접관은 무엇을 평가해야 할까.» 꼬리질문이 필요하다는 주장이다.
  - ⚠ 검색 요약에 뜬 «완벽한 코드를 내고도 설명이 무너지는 지원자가 생각보다 많다»는 본문에 **없다**. 인용 금지.
- 토스·우아한형제들·카카오·당근 기술블로그의 «프로젝트를 설명하지 못한다» 관찰: **못 찾음.**
- 개발자 면접관 대상 정량 설문: **못 찾음.**

## 4. 포트폴리오 레포 규모 (커밋·레포 수)

**못 찾음.** 부트캠프·우테코·소마 팀 프로젝트의 평균 커밋 수나 취준생 1인당 레포 수 통계는 없었다.
- 대안: Devfit이 분석한 실제 레포의 커밋 수 분포를 직접 집계해 «Devfit 자체 데이터»로 표기하는 방법이 있다. 다만 이번 조사에서 그 값을 뽑지 않았으므로 **지금 덱에 숫자를 넣으면 안 된다.**

## 반대 근거·한계

- 망각에는 예외가 있다. 반복해서 고친 파일, 내가 쓴 비율이 높은 파일은 오래 기억한다(Krüger 2018/2019). 장기 프로젝트의 주 기여자에게는 주장이 약해진다.
- 신입 면접에서는 «모르면 모른다고 하는 것»도 괜찮게 받아들여진다. jpy1030은 «모른다고 바로 답했더니 다른 질문으로 넘어가주셔서 그건 잘했다»고 썼다.
- 인사담당자 설문에서 면접 비호감 1위는 프로젝트 설명이 아니다. 사람인 2018(575명) 1위는 «지원 회사의 기본 정보도 모르는 지원자» 24.2%였다 ✅ (https://www.saramin.co.kr/zf_user/help/live/view?idx=78745&listType=news)
- Xia 58%는 코드 일반의 이해 시간이고, Anthropic 17%p는 작업 직후 측정이다. 둘 다 «자기 코드를 몇 달 뒤 잊는다»의 직접 증거가 아니다.

## 접근 실패
- inthiswork.com/archives/238654: 본문 잘림
- Reddit 원문: 검색 요약의 «completely blank» 류 글을 원문에서 확인하지 못함 → 인용 금지
- 사람인 «377명/48.9%»: 출처 재확인 불가 → 폐기
- 인크루트 334명 «업무지식 24.6%»: 검색 요약만 있음 📰
