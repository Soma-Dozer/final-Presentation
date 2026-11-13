# R11: «기술면접이 지원자 자신의 코드를 설명하게 하는 쪽으로 바뀌고 있다» 근거

> 조사일 2026-11-13 · 요청: 덱 4쪽 근거 교체 (넥슨 코테 폐지·CJ올리브영 AI 과제·컬리 ChatGPT 허용은 «AI 허용» 근거라 주장과 어긋남)
> 표기 (R1~R9와 같음):
> - **✅** 이번에 원문을 직접 열어 문구를 확인했다
> - **📰** 검색 요약이나 2차 인용으로만 확인했다 (원문 접근 실패)
> - **⚠** 대표성·출처 성격에 주의가 필요하다
> 덱(final-deck/)·claims.md·최종보고서는 열지 않았다.

---

## 장표에 바로 쓸 수 있는 근거 TOP 4

| # | 기업/출처 | 날짜 | 한 줄 요약 | URL | 확인 |
|---|---|---|---|---|---|
| 1 | **넥슨 기술면접관** (오윤호 넥슨코리아 실장, NDC 26 강연) · 천지일보 보도 | 2026-06-17 | 10년 넘게 기술면접을 맡은 면접관이 핵심 질문을 공개했다. "이 코드는 어떤 기능을 하고, 왜 이렇게 구현했나요." 그리고 "복사해왔거나 AI가 짜준 코드는 이 세 질문에 답을 못하는 경우가 너무 많다", "이 질문만으로 면접의 50%는 정리가 된다"고 말했다. 신입 포트폴리오를 두고 한 이야기다 | https://www.newscj.com/news/articleView.html?idxno=3409912 | ✅ |
| 2 | **잡플래닛 면접 리뷰 큐레이션** (이스트소프트 백엔드 실제 질문) | 2026-07-01 | "왜 이 코드를 썼는지 코드적으로 설명해 주세요." 매체 해설: 이력서 프로젝트를 «실제로 본인이 했는지» 확인하려고 «코드 한 줄까지» 판다 | https://www.jobplanet.co.kr/contents/news-8309 | ✅ (R1 E19, 사용자 붙여넣기로 확인. 기존 근거) |
| 3 | **The Pragmatic Engineer «The Pulse #146»** (interviewing.io 면접관 설문) | 2025-09-18 | "58% of Big Tech interviewers said they have adjusted the kind of questions they ask". 바뀐 전술은 "Ask why a candidate made choices, and have them explain in detail", "What does this line of code do, what would happen if we remove this line…" | https://newsletter.pragmaticengineer.com/p/the-pulse-146 | ✅ (이번에 재확인) |
| 4 | **Codility** (글로벌 코딩 평가 플랫폼) «Follow-Up Questions for Take-Home Assessments» | 2025-09-18 (도움말 생성일) | 과제를 제출하면 AI가 **지원자가 제출한 코드**를 분석해 맞춤 후속 질문을 만든다. 목적은 지원자가 "truly grasp their solution"하는지 보고 "validate their authorship"하는 것이다 | https://support.codility.com/hc/en-us/articles/39175728044689-Follow-Up-Questions-for-Take-Home-Assessments | ✅ (본문 페이지는 403. 같은 글을 Zendesk API `…/api/v2/help_center/en-us/articles/39175728044689.json`으로 열어 확인) |

**덱 문구 후보 (근거 범위 안):**
- «넥슨 면접관: "이 코드는 어떤 기능을 하고, 왜 이렇게 구현했나요"가 면접의 절반» (넥슨 NDC 26, 2026)
- «Big Tech 면접관 58%가 AI 때문에 질문을 바꿨다: "왜 그렇게 짰나", "이 줄을 지우면?"» (interviewing.io·Pragmatic Engineer, 2025, n=63)
- «평가 플랫폼도 제출 코드에 대한 후속 질문으로 본인 작성 여부를 확인한다» (Codility, 2025)

**쓰면 안 되는 표현:** «기업 X%가 코드 설명 면접을 도입했다»(그런 수치는 국내외 모두 못 찾음) · «코딩테스트가 사라지고 있다»(반대 근거 많음, 아래 3절) · «넥슨이 면접 방식을 바꿨다»(1번은 면접관 개인의 강연 발언이고 전형 변경 공지가 아님)

---

## 1. 국내 근거 상세

### 1-1. 넥슨 NDC 26: 오윤호 실장 «넥슨의 기술 면접 기준» ✅

| 항목 | 내용 |
|---|---|
| 1차 출처 | 천지일보 «"AI가 짜준 코드, 내 실력 아니다"… 21년 개발자의 경고», 손고은 기자, 2026-06-17 12:32 https://www.newscj.com/news/articleView.html?idxno=3409912 ✅ |
| 보조 출처 | 게임뷰 «[NDC26] 오윤호 넥슨 실장이 공유하는 넥슨의 기술 면접 기준은?» https://www.gamevu.co.kr/news/articleView.html?idxno=58753 📰 (접속 실패, 검색 요약만: 포트폴리오에 대한 «세부적인 경험» 질문이 기본이고, 모르는 부분이 나올 때까지 질문을 이어간다) |
| 발언자 | 오윤호 넥슨코리아 실장. 기사 기준 10년 넘게 넥슨 기술면접 담당 |
| 원문 인용 | "이 코드는 어떤 기능을 하고, 왜 이렇게 구현했나요." / "복사해왔거나 AI가 짜준 코드는 이 세 질문에 답을 못하는 경우가 너무 많다" / "이 질문만으로 면접의 50%는 정리가 된다" |
| 대상 | 신입 지원자 포트폴리오. 원문: "요즘 신입 지원자 포트폴리오를 보면 화려하고 다양한 엔진, 라이브러리, 프레임워크를 썼다고 한다" |
| 직접성 | **직접.** «지원자 자신의 코드를 설명하게 하는 면접 + AI 코드 문제의식»이 한 문단에 다 있다 |
| 한계 | 면접관 한 명의 강연 발언이다. 전형 변경 공지나 통계가 아니다. 넥슨이 이 기준을 «새로 도입»했다는 서술도 없다. 기사는 포트폴리오 코드인지 별도 과제 코드인지 명시하지 않는다. «바뀌고 있다»의 시계열 근거로 쓰기보다 «AI 시대 면접관이 실제로 묻는 것»의 근거로 쓰는 게 안전하다 |
| 참고 | 같은 넥슨이 2026-08 넥토리얼에서 코딩테스트를 폐지했다(블로터 2026-08-26 https://www.bloter.net/news/articleView.html?idxno=671869 ✅, 홍자현 채용팀장 "채용 방식에도 변화가 필요하다고 판단했다"). 이 기사에는 직군·팀 면접에서 결과물을 설명하게 한다는 내용이 **없다** ✅ |

### 1-2. 잡플래닛 2026년 5~6월 실제 면접 질문 (기존 R1 E19 재사용)

R1 E19 그대로. 이스트소프트 "왜 이 코드를 썼는지 코드적으로 설명해 주세요", 비바리퍼블리카 "다른 방법은 왜 선택하지 않았는지". 큐레이션이라 비중 수치로 쓰면 안 된다. 상단 «AD» 표기 확인 필요.

### 1-3. 토스 프론트엔드 «이력서 없이 GitHub 리포지토리 링크로 지원» ✅ (R9 1-1 재확인)

- 2025-04-08, 박서진 Head of Frontend. "저희 프론트엔드 리더들은 오직 코드를 기준으로 평가할게요." https://toss.tech/article/frontend-apply-without-resume ✅
- **이번에 다시 확인한 한계:** 리포 제출 뒤 면접에서 그 코드를 다루는지는 본문에 **없다**. 댓글의 «과제전형은 동일할까요?» 질문에도 답이 없다.
- 토스 NEXT 2023·2024 공식 페이지도 «과제 전형 → 직무 인터뷰» 순서만 있고, 인터뷰에서 과제 코드를 다룬다는 문장은 **없다** ✅ (https://toss.im/career/next-developer-2024, https://toss.im/career/next-developer-2023)
- 덱 활용: «지원자 본인 코드를 평가 대상으로 삼는 전형이 생겼다»까지만. «코드를 설명하게 한다»의 근거는 아니다.

### 1-4. 현대오토에버 1차 면접: 코딩테스트 풀이·과제 PT 재설명 📰⚠

- 잡플래닛 정리글(news-8558)의 검색 요약: "1차 면접은 코딩테스트 풀이나 과제 PT를 다시 설명하게 하고, 지원서에 쓴 프로젝트에서 '왜 이 기술을 골랐는지'를 끝까지 묻는 방식이 반복됐어요." https://www.jobplanet.co.kr/contents/news-8558 (403, 원문 미확인)
- 합격 후기(링커리어 https://community.linkareer.com/pass-review/1264556 등)도 «코딩 테스트 결과를 1차 면접에 진행»했다고 전한다 📰
- 공식 공고(캐치 게재 2026 3분기 공고)와 원티드 인사담당자 인터뷰에는 이 내용이 **없다** ✅ (https://m.catch.co.kr/NCS/RecruitInfoDetails/557455, https://www.wanted.co.kr/events/2025recruitingcarnival_hyundai_report)
- 판정: 후기 기반이라 장표 본문에는 쓰지 말고, 쓴다면 Q&A 노트용.

### 1-5. 기타 국내 (약한 근거)

| 자료 | 내용 | 확인 | 판정 |
|---|---|---|---|
| CIO Korea 칼럼, Nick Hodges, 2025-07-24 https://www.cio.com/article/4027594/ | "지원자는 일정 기간 동안 과제를 수행한 뒤, 결과물을 시연하고 코드에 대해 설명한다." 필자가 선호하는 방식이라는 의견이다 | ✅ | 해외 필자의 번역 칼럼. 사례가 아니라 주장 |
| 웍스피어 HR 블로그, 2026-07-07 https://blog.worxphere.ai/ai-developer-interview-questions | «본인이 작성한 코드 중 가장 자랑스러운 부분과 그 이유», «AI가 짜준 코드를 그대로 쓴 적이 있나요? 그 코드를 어떻게 검증했나요?» 같은 질문을 권한다 | ✅ | HR 솔루션사의 권고. 실제 도입 사례 아님. 인용 수치(Gartner 등)는 원문 대응이 어긋나 인용 금지 |
| 코리아비즈니스리뷰, 2025-12-12 (R1 E7) | "AI가 제안한 코드의 오류를 어떻게 검증했는가?" | ✅ | «본인 코드 설명»이 아니라 AI 활용 검증 질문 |
| 동아일보, 2026-09-12 (네이트 https://m.news.nate.com/view/20260912n05091) | CoderPad 조사 인용, 과정·판단 설명이 중요해졌다 | ✅ | 본인 코드를 설명하게 한다는 문장은 없음 |

---

## 2. 해외 근거 상세

### 2-1. The Pragmatic Engineer «The Pulse #146» ✅ (R1 E1 재확인)

- 2025-09-18. interviewing.io 면접관 설문, "They received 63 detailed responses"(Big Tech 45, New Big Tech 7, 스타트업 11).
- "58% of Big Tech interviewers said they have adjusted the kind of questions they ask" + "in an effort to combat potential AI "cheat tool" usage."
- 전술: "Ask why a candidate made choices, and have them explain in detail." / "Pushing candidates to explain their thinking, which an LLM struggles to do." / "What does this line of code do, what would happen if we remove this line, what is a different way to do the same thing?"
- 한계: 58%의 정확한 분모는 기사에 없다(Big Tech 응답 기준). 여기서 «코드»는 면접 중 지원자가 쓴 코드다. «과거 프로젝트 코드»는 아니지만 «자기 코드를 설명하게 한다»에는 맞는다.

### 2-2. The Pragmatic Engineer «How GenAI changes tech hiring» ✅

- 2024-12-03, Gergely Orosz·Elin Nilsson. https://newsletter.pragmaticengineer.com/p/how-genai-changes-tech-hiring
- 시리즈 A 스타트업 Head of Data(익명): "Live discussion about the deliverable has become more valuable, and the code itself less valuable"
- 과제(take-home) 결과물보다 그 결과물에 대한 대화가 중요해졌다는 현장 증언. 익명 1인이고, 관련 섹션 본문은 유료라 못 봤다.

### 2-3. Codility 제출 코드 후속 질문 기능 ✅

- 생성 2025-09-18, 수정 2025-09-23. 원문: AI가 "analyzes their code and generates a small set of targeted, time-boxed questions" / 목적 "help you understand how well candidates truly grasp their solution, validate their authorship."
- 검색 요약(📰): 지원자당 3문항, 문항당 2분, 리뷰어는 코드 옆에서 문답 기록을 본다.
- 의미: 평가 벤더가 «본인 코드에 대한 설명으로 작성자 확인»을 제품 기능으로 만들었다. 수요가 있다는 간접 증거.
- 한계: 벤더 자료. 도입 기업 수·사용률 없음.

### 2-4. 대학 교육 쪽 유사 흐름: «Code Interviews» (SIGCSE 2025) ✅

- Kannam·Yang·Dharm·Lin, SIGCSE 2025 Experience Report, arXiv 2410.01010 (2024-10-01). https://arxiv.org/abs/2410.01010
- 과제를 낸 학생과 1:1로 그 코드를 이야기하는 «code interview»를 주간 TA 세션 대신 운영. 동기: "Generative artificial intelligence poses new challenges around assessment"
- 채용이 아닌 교육 사례다. 덱 본문보다 Q&A용 («AI 이후 자기 코드 설명이 진위 확인 수단으로 쓰인다»의 보조).

### 2-5. Greenhouse «AI in Hiring» 2025 ✅ (간접)

- 2025-11-19. "To verify authenticity, 39% of hiring managers in the U.S. are conducting more in-person interviews." 응답 4,136명(미국 채용 담당자·관리자 665명 포함). https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair
- 직군 일반이고, «코드 설명»이 아니라 «대면 면접 확대»다. 진위 확인 수요의 배경 수치로만.

### 2-6. 확인했으나 이 주장에는 맞지 않는 것

- **DoorDash** (2026-03, https://careersatdoordash.com/blog/doordash-is-rebuilding-its-engineering-interviews-around-ai/ 📰): 코딩 라운드를 60분 AI 보조 작업 세션으로 교체. 지원자 자신의 기존 코드가 아니라 주어진 프로젝트다. 넥슨·CJ올리브영과 같은 «AI 활용 평가» 범주.
- **HackerRank 차크라** (AI포스트 2026-10-06 https://www.aipostkorea.com/news/articleView.html?idxno=12877 ✅): 면접 중 선택 이유를 묻는 «인라인 후속 질문», AI 기여분과 본인 수정분을 나눠 보여준다. 역시 면접 중 작성 코드 기준이고 AI 유창성 평가가 핵심.
- **Karat NextGen**: 다중 파일 프로젝트 + AI 도우미 + 면접관이 추론을 캐묻는 형식(검색 요약 📰). 자기 코드 아님.

---

## 3. 반대 근거 (덱에서 과장하지 않도록)

| 내용 | 출처 | 확인 |
|---|---|---|
| 조직의 **62%**가 여전히 기술면접에서 AI를 금지한다. 엔지니어링 리더 400명 | Karat «Engineering Interview Trends 2026» (2026-01-07) https://karat.com/engineering-interview-trends-2026/ | ✅ (R5 S1) |
| Big Tech·New Big Tech 면접관 중 «알고리즘 질문을 버렸다»는 응답 **0명**. 질문이 대체가 아니라 «설명·꼬리질문형으로 변형» | Pulse #146 | ✅ (R1) |
| 무신사 AI 네이티브 공채도 **1차는 코딩테스트**(약 1,700명) → 2차 AI 도구 활용 → 3차 면접 | 무신사 보도자료 2026-03-30 (검색 요약) | 📰 (뉴스룸 URL이 리다이렉트돼 원문 미확인) |
| 현대오토에버 2026 신입 공채는 코딩테스트 전형을 유지 | 캐치 공고 2026 3분기 «코딩테스트 전형» | ✅ |
| 그렙: 개발 직군은 코딩테스트를 유지하고 AI 평가를 추가 | R5 K1 | ✅📰 |
| 넥슨·CJ올리브영·컬리 사례는 «AI 활용 평가» 도입이지 «본인 코드 설명» 도입이 아니다. 넥슨 넥토리얼 기사에도 결과물 설명 면접 언급 없음 | 블로터 2026-08-26 | ✅ |
| 2026년엔 오히려 «라이브 코딩이 과제보다 낫다»는 주장도 있다 (과제는 AI로 대신 풀 수 있어서) | techinterview.org «Why live coding rounds are beating take-homes in 2026» | 📰 (미열람, 상업 사이트) |
| 네이버·카카오·당근은 코테에서 AI를 금지한다는 정리 | 잡코리아 2026-05-09 · aceround.app | 📰⚠ 블로그 수준, 1차 자료 없음 (R5와 같은 판단) |

→ 반대 근거가 말하는 것: **코딩테스트도, AI 금지도 그대로 남아 있다.** 그래서 «코테가 사라지고 코드 설명 면접으로 대체된다»는 근거 밖이다. 근거가 받치는 범위는 «AI로 결과물만 봐선 변별이 안 돼, 면접에서 지원자가 쓴 코드를 "왜 이렇게 짰나"로 확인하는 비중이 커지고 있다»까지다. 이 결론은 AI 허용 쪽과 금지 쪽 모두와 충돌하지 않는다.

---

## 4. 못 찾은 것

- ❌ 국내 기업의 **공식** 발표·채용 블로그 중 «과제 리뷰 면접 / 코드 리뷰 면접 / 포트폴리오 코드 기반 면접을 도입·확대했다»는 2024~2026 자료. (토스·카카오·현대오토에버는 후기에서만 «과제·풀이를 면접에서 설명» 언급, 공식 문서엔 없음)
- ❌ «코드 설명형 면접 비중 X%» 같은 국내·해외 정량 수치. 가장 가까운 것은 Pulse #146의 58%(질문 «종류»를 바꿨다)다.
- ❌ HackerRank·CoderPad의 «제출 코드 설명» 공식 기능 문서 (CoderPad는 서드파티 비교글에서만 언급)
- 접근 실패: 게임뷰(연결 거부), 잡플래닛 news-8558(403), 무신사 뉴스룸(리다이렉트), 한빛+(본문 로딩 안 됨), velog 카카오 후기(504)

---

## 5. 덱 4쪽 교체 추천

현재 «채용 방식 변화» 3건(넥슨 인턴 코테 폐지·CJ올리브영 AI 과제·컬리 ChatGPT 허용)은 «AI 활용 평가» 근거라 주장과 맞지 않는다. 다음으로 바꾸기를 권한다.

| 현재 | 교체안 | 이유 |
|---|---|---|
| 넥슨 인턴 코딩테스트 폐지 | **넥슨 면접관 (NDC 26, 2026-06)**: "이 코드는 어떤 기능을 하고, 왜 이렇게 구현했나요." 이 질문으로 면접의 50%가 정리된다 | 같은 회사라 장표 흐름을 유지한다. 주장과 1:1로 맞는다 |
| CJ올리브영 AI 과제 | **Big Tech 면접관 58% 질문 변경** (Pulse #146, 2025-09, n=63): "왜 그렇게 짰나", "이 줄을 지우면?" | 유일한 정량 근거다. 이미 R1에서 확인했다 |
| 컬리 ChatGPT 허용 | **Codility (2025-09)**: 제출한 코드에 후속 질문을 붙여 본인 작성 여부 확인 | 업계 도구가 «자기 코드 설명»을 기능으로 만들었다. 대안: 토스 2025 «GitHub 리포 링크로 지원»(코드 자체를 평가하지만 «설명» 근거는 아님) |

각주 예: `넥슨 NDC 26 강연(천지일보 보도), 2026.` · `The Pragmatic Engineer, 「The Pulse #146」, 2025.` · `Codility, 「Follow-Up Questions for Take-Home Assessments」, 2025.`

넥슨·CJ올리브영·컬리 3건은 Q&A 노트에서 «AI 활용 평가도 같이 늘고 있다»는 보조 답변으로 돌리면 된다.

---

## Research Trace

- 주요 검색어: «과제 리뷰 면접», «코드 리뷰 면접 도입», «AI로 짠 코드 설명 못해 면접», «NDC26 오윤호», «현대오토에버 1차 면접 코딩테스트 리뷰», «무신사 Codex 면접», «Codility follow-up questions», «Karat 2026», «Greenhouse 39% in-person», «code interviews SIGCSE».
- 원문을 직접 연 것: 천지일보(넥슨), 블로터(넥슨), Pulse #146, Pragmatic Engineer 2024-12, Codility(Zendesk API), arXiv 2410.01010, Greenhouse, CIO 칼럼, 웍스피어, 코리아비즈니스리뷰, 토스 기술블로그·NEXT 2023/2024, 원티드 현대오토에버, 캐치 공고, AI포스트, 잡코리아, 동아(네이트).
- 전체 웹을 조사했다고 주장하지 않는다. 기업 공식 채용 블로그는 검색엔진이 잘 잡지 못해 토스·카카오·현대오토에버 외에는 직접 열지 못했다.
