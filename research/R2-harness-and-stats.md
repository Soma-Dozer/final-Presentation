# R2 — 6장 «하네스» 외부 근거 · 3장 통계 3개 원문 대조

> 조사일 2026-11-06 · 요청: ppt-start · Sonnet Worker 3개 + Opus 직접 재확인(SWE-agent 표)
> 검증 표기: **Y** = 원문 본문 열람 · **A** = 초록·요약·미러만 · **N** = 2차 출처만
> 덱 파일·claims.md는 수정하지 않았다. 최종보고서는 열지 않았다.

## 한눈에

| 장 | 항목 | 판정 |
|---|---|---|
| 6장 | «같은 LLM이라도, 차이는 하네스» | **외부 1차 근거 확보.** 정량은 SWE-agent 논문(같은 GPT-4 Turbo, 18.0% vs 11.0%), 정성은 Anthropic 엔지니어링 블로그, 최대 격차는 Epoch AI(GPT-5 최대 11%). 반대 근거(모델 세대 효과가 더 큼)도 함께 적어야 함 |
| 3장 ① | 84% Stack Overflow | **그대로 사용 가능.** 각주로 모집단 보강 |
| 3장 ② | 60% WGU | **그대로 사용 가능.** «미국 채용 담당자(전 직군)»를 명시 |
| 3장 ③ | 58% Pulse #146 | **수정 필요.** 원문은 «질문의 *종류*를 조정». «왜 그렇게 짰나»는 원문에 있지만 58%와 연결된 수치가 아님 |

---

## A. 6장 «같은 LLM이라도, 차이는 하네스입니다»

### A1. SWE-agent (Yang et al., NeurIPS 2024) — 같은 모델, 정량 비교 ✅ 가장 강함
- 출처: arXiv:2405.15793v3 · https://arxiv.org/html/2405.15793v3 · 2024-05 (NeurIPS 2024)
- **Table 1 (GPT-4 Turbo, SWE-bench Lite, % Resolved)** — Opus가 원문 HTML을 직접 열어 재확인:
  - SWE-agent: **18.00** ($1.67)
  - Shell-only agent: **11.00** ($1.46)
  - Shell-only agent, w/o Demonstration: **7.33** ($0.79)
  - RAG: 2.67
- **Table 3 ablation (같은 GPT-4 Turbo, 기준 18.0)** — 인터페이스 요소 하나만 바꿔도 점수가 떨어진다:
  - 편집 시 linting 제거: 15.0
  - 편집 기능 제거: 10.3
  - 검색 방식 iterative: 12.0
  - 파일 뷰어 전체 파일: 12.7
  - 컨텍스트 전체 기록: 15.0
- 인용: *"SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files"*
- 장표용 문장: **«같은 GPT-4 Turbo로도 에이전트 인터페이스만 바꾸면 SWE-bench Lite 해결률이 11.0% → 18.0%(1.6배)»**
- 한계: 2024년 모델이고 Lite 분할(300문항)이다. 표는 원문 레이아웃이 깨져 있어 라벨 일부를 재구성했다(수치는 일치).
- 검증: **Y**

### A2. Anthropic Engineering — "Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet" — 정성 1차 출처
- URL: https://www.anthropic.com/engineering/swe-bench-sonnet (2025-01로 알려져 있으나 페이지에서 날짜는 미확인)
- 인용: *"The performance of an agent on SWE-bench can vary significantly based on this scaffolding, even when using the same underlying AI model."*
- 인용: 개발자·스타트업들이 *"optimizing scaffoldings to greatly improve the performance around the same model"*에 성공했다.
- 설계: Bash와 str_replace 편집 도구만 두는 최소 스캐폴드. 도구 설명을 반복 개선했다(절대경로 강제 등).
- 검증: **Y**

### A3. Epoch AI — "Why benchmarking is hard" (Gradient Updates) — 최대 격차
- URL: https://epochai.substack.com/p/why-benchmarking-is-hard · Florian Brand, JS Denain · 2025-12-23
- 인용: *"simply switching the scaffold makes up to an 11% difference for GPT-5"* / *"up to a 15% difference for Kimi K2 Thinking"* / *"The choice of scaffold has the single biggest impact on the overall performance."*
- 비교한 스캐폴드: Claude Code, OpenHands, mini-SWE-agent (SWE-bench Verified)
- 한계: 스캐폴드별 점수는 확인하지 못했고 «최대» 격차만 있다. 원문 표기가 «%»라 %p인지는 확정하지 못했다. 본문은 fetch 요약으로 확인했다.
- 검증: **Y(요약 경유)**. 2차 보도는 The Decoder 2026-01-10.

### A4. Anthropic — "Effective harnesses for long-running agents" (2025-11-26) — 보조
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 인용: *"Providing Claude with these kinds of testing tools dramatically improved performance."*
- 정량 비교 없음. 검증: **Y**

### A5. 간접 근거 (본문 인용은 비권장)
- Agentless (arXiv:2407.01489): 에이전트 없이 단순 절차만으로 SWE-bench Lite 32.00%, 문항당 $0.70. «복잡한 에이전트보다 절차 설계가 중요하다»는 간접 근거다. 검증 A.
- Kapoor et al. "AI Agents That Matter" (arXiv:2407.01502): *"the community has reached mistaken conclusions about the sources of accuracy gains"*. 검증 A.
- 인용 금지(원문 미확인): Sonnet 4.5 SWE-agent 43.2% vs Cline 59.8%(블로그), SusVibes 수치, OpenAI SWE-bench Verified의 GPT-4o 스캐폴드별 수치(원문 403).

### A6. 반대·보완 근거 (덱에서 숨기지 말 것)
- **모델 세대 효과도 크다.** A2 같은 글에서 같은 스캐폴드인데 Claude 3 Opus 22% → 3.5 Sonnet(old) 33% → 3.5 Sonnet(new) 49%였다. 같은 기간 스캐폴드 격차(최대 11~15%)보다 모델 교체 폭이 더 크다.
- Epoch: 스캐폴드 외에 API 제공자 차이도 큰 변수라고 했다(2차 보도 기준).
- Anthropic의 철학은 *"keep the scaffolding minimal"*이다. «하네스가 두꺼울수록 좋다»가 아니라 «도구·인터페이스 설계가 결과를 바꾼다»로 읽어야 한다.
- 권장 문구: «모델이 같아도 하네스 설계에 따라 성능이 크게 달라진다» (O) / «모델보다 하네스가 더 중요하다» (X, 반대 근거와 충돌)

---

## B. 3장 통계 3개 원문 대조

> 아래 인용은 WebFetch가 원문 그대로라고 돌려준 문구다. 발표 전에 원문 페이지를 한 번 눈으로 확인할 것을 권한다.

### B1. 84% — Stack Overflow Developer Survey 2025
- URL: https://survey.stackoverflow.co/2025/ai
- 원문: *"84% of respondents are using or planning to use AI tools in their development process, an increase over last year (76%)."*
- 표본: «All Respondents» 탭, 해당 문항 응답 33,662건. 84%는 매일 47.1 + 매주 17.7 + 월 1회 이하 13.7 + 곧 사용 예정 5.3을 합친 값이다.
- 장표와의 차이: 거의 없다. 모집단이 전문 개발자만이 아니라 학생·취미 개발자를 포함한 전체 응답자라는 점만 다르다.
- **판정: 그대로 사용.** 각주에 «전체 응답자, 해당 문항 n=33,662»를 단다.

### B2. 60% — WGU Workforce Decoded 2026
- URL: https://www.wgu.edu/newsroom/press-release/2026/09/ai-has-made-real-skills-harder-to-evaluate.html (발행 2026-09-30)
- 원문: *"The national survey of 3,128 U.S. hiring professionals found… 60% say AI is making it harder to evaluate candidates' real skills."*
- 조사: Centiment 수행(WGU 의뢰), 2026-06-24 ~ 07-07, 미국 채용 실무자 n=3,128
- 장표와의 차이: 개발자 채용에 한정된 수치가 아니라 **전 직군**이다. 문항 원문과 응답 척도는 보도자료에 없다(보고서 PDF는 열지 못함).
- **판정: 그대로 사용.** 단 «미국 채용 담당자(전 직군) n=3,128»을 명시한다.

### B3. 58% — The Pulse #146 / interviewing.io
- 원문 A, Pragmatic Engineer (2025-09-18): https://newsletter.pragmaticengineer.com/p/the-pulse-146
  - *"58% of Big Tech interviewers said they have adjusted the kind of questions they ask in an effort to combat potential AI…"* (문장 뒷부분은 fetch가 잘라서 확인하지 못함)
  - 표본: *"63 detailed responses"*(Big Tech 45 · New Big Tech 7 · 스타트업 11)
- 원문 B, interviewing.io 블로그 (날짜 미표기, 본문에 2025-10-08 EDIT): https://interviewing.io/blog/how-is-ai-changing-interview-processes-not-much-and-a-whole-lot
  - *"58% of FAANG interviewers said that they have adjusted the kinds of algorithmic questions they ask."*
  - 표본: *"We got 67 responses"*, 그중 FAANG 52
  - **n 불일치(63 vs 67)**: 블로그가 응답을 추가한 갱신본일 가능성이 있다(추정). 58%의 분모가 Big Tech 45명인지 52명인지는 원문에 명시돼 있지 않다.
- **«왜 그렇게 짰나» 풀이 검증**
  - 원문에 있다: Pulse *"Ask why a candidate made choices, and have them explain in detail."* · *"More follow-up questions"*. 블로그에는 Meta 면접관 *"more focused on the WHY than the HOW"*, Microsoft *"what does this line of code do"*, *"it is not about what question is asked but about how to ask follow-up questions."*
  - 그러나 **58%와는 연결되지 않는다.** 58%는 «(알고리즘) 질문의 *종류*를 조정했다»는 비율이다. «왜»는 일부 면접관이 개별 인용에서 말한 변화 중 하나일 뿐이다. 다른 변화로 LeetCode 변형, 커스텀 문제, 부정행위 탐지 도구, 대면 복귀 논의가 있다. 블로그는 FAANG의 가장 큰 프로세스 변화를 **탐지 소프트웨어**라고 서술한다.
  - 장표의 «질문 *방식*»도 원문 «kinds of questions(종류)»와 어긋난다.
- **판정: 수정 필요.** 대체 문구:
  1. «Big Tech 면접관 58%가 AI 대응으로 **질문을 바꿨다** — 일부는 "무엇을 썼나"보다 **"왜 그렇게 짰나"**를 묻는다»
  2. «AI 대응으로 면접 질문의 종류를 조정한 Big Tech 면접관 58%» + 주석 «일부 면접관: "왜 그렇게 선택했는지 자세히 설명시킨다"»
  - 출처 표기 권장: «interviewing.io 면접관 설문(n=63, Big Tech 45), via The Pragmatic Engineer 2025-09-18». n은 하나로 정해 쓰고 불일치는 각주에 남긴다. 자발 응답이고 표본이 작다는 점도 각주에 넣는다.

---

## 접근 실패
- OpenAI "Introducing SWE-bench Verified" 원문 403 (미러만 확인)
- swebench.com 리더보드 데이터 로딩 실패, `/bash-only.html` 404
- Epoch의 SWE-bench Verified 상세 리뷰(스캐폴드별 점수표) 못 찾음
- WGU 보고서 PDF 미열람
