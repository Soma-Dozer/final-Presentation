# R1 — «경험 위주 기술면접» 주장 + 경쟁사 비교표 근거

> 조사일 2026-11-06 · research-2 세션 (Opus 총괄 + Sonnet Worker 4개) · 핵심 근거 5건은 Opus가 원문 재확인
> 표기: ✅원문 확인 · 📰언론 경유 · ❌못 찾음 / 직접·간접 근거

## 덱에 쓸 수 있는 한 줄 + 출처

1. **«Big Tech 면접관 58%가 AI 때문에 질문 방식을 바꿨다 — "왜 그렇게 짰나", "이 줄을 지우면?"»** — interviewing.io 면접관 설문 n=63, The Pragmatic Engineer «The Pulse #146»(2025-09-18) ✅ 간접
2. **«Canva는 CS 기초 코딩 스크리닝을 AI 허용 면접으로 대체, CJ올리브영은 라이브 코딩을 없애고 '과정 평가' AI 과제로 교체»** — Canva Engineering Blog(2025-06-11) ✅ 직접 / 아시아경제(2026-07-21) 📰 직접
2-1. (국내 정성) **«"왜 이 코드를 썼는지 코드적으로 설명해 주세요" · "다른 방법은 왜 선택하지 않았나" — 2026년 5~6월 실제 개발자 면접 질문»** — 잡플래닛 면접 리뷰 큐레이션(2026-07-01), 이스트소프트·비바리퍼블리카 ✅ 간접(사례, 비중 수치 아님)
3. **경쟁사 표 수정 필요:** Greenroom은 GitHub 레포를 읽고 질문한다(«코드 확인 없음» 틀림). 사람인은 사람인 공고 URL 맞춤을 지원한다(«'일부'» → «자사 공고 한정»). 안전한 차별점은 **«팀 레포에서 본인 커밋 단위 분석 + 한국 공고 맞춤 (확인된 범위에서)»**.

---

## 🔴 덱 문구 주의 (먼저 읽기)

- **«알고리즘 → 경험 위주로 바뀌었다» 단정 금지.** 같은 Pulse #146 설문에서 Big Tech·New Big Tech 53명 중 **"알고리즘 질문에서 벗어났다"고 답한 사람 0명**. 질문이 *대체*가 아니라 *설명·꼬리질문형으로 변형*되는 중이다.
  - 안전한 표현: «AI로 결과물만으론 변별이 안 돼, 면접이 '왜·어떻게'를 캐묻는 쪽으로 바뀌고 있다»
- **«경험 질문 비중 X% 증가» 같은 직접 수치는 국내·해외 모두 못 찾음.** 수치를 만들어 넣지 말 것.
- **Google 대면 면접 복귀를 «AI 부정행위 때문»이라 쓰지 말 것.** Pichai 원문에 cheating이라는 말이 없다("make sure the fundamentals are there"). 부정행위 프레임은 언론 해석.
- **«GitHub을 읽는 경쟁자가 없다» 금지** — Greenroom 존재.

---

## 조사 1 — C1 «AI 발전으로 기술면접이 경험 위주로 묻는다»

### ① 질문이 바뀌었다는 근거

| ID | 자료 | 핵심 수치/내용 | 상태 | 직접성 | 한계 |
|---|---|---|---|---|---|
| E1 | The Pragmatic Engineer, «The Pulse #146» (2025-09-18) — https://newsletter.pragmaticengineer.com/p/the-pulse-146 | interviewing.io 면접관 n=63(Big Tech 45·New Big Tech 7·스타트업 11). **81% AI 부정행위 의심, 31% 실제 적발, Big Tech 면접관 58% "질문 종류를 조정했다"**. 전술: "Focusing on the 'why'", 세분화 질문 *"What does this line of code do, what would happen if we remove this line…"*, Apple "more real-world questions and fewer algorithmic ones" | ✅ (Opus 재확인) | 간접(질문 '변형'의 직접 증거, '경험 위주' 전환은 아님) | 소표본·자기보고·설문 시점 미기재. 알고리즘 폐기 0명 |
| E2 | interviewing.io, «How hard is it to cheat with ChatGPT in technical interviews?» — https://interviewing.io/blog/how-hard-is-it-to-cheat-with-chatgpt-in-technical-interviews | 모의면접 32건. 통과율 대조군 53% / LeetCode 원문 73% / 변형 67% / **커스텀 질문 25%**. 면접관은 부정행위를 1건도 감지 못함 → 실무 기반 고유 문제로 이동 권고 | ✅ (Worker) | 간접 — "정형 문제는 AI로 뚫린다"의 실험 근거 | n 작음, 자사 실험, 날짜 미표기 |
| E3 | LeadDev, «Think the technical interview is dead? Think again» (2026-05-06) — https://leaddev.com/hiring/think-the-technical-interview-is-dead-think-again | Formation 인용 "System design and judgment of technical trade-offs are increasingly important". Cursor: 최종 온사이트에서 자사 코드베이스로 1~2일 작업 후 발표. Meta: 코드베이스 기반 AI 허용 라운드 | ✅ (Worker) | 직접(사례·증언), 수치 없음 | 정성 |
| E4 | CoderPad, «2026 State of Tech Hiring» 블로그 (2026-03-11) — https://coderpad.io/blog/hiring-developers/new-research-the-2026-state-of-tech-hiring-what-ai-means-for-developers-and-hiring-teams/ | 응답 650+. AI 허용 시 채용 리더가 "오류 포착, 트레이드오프 설명"을 중시 | ✅ 블로그만 (PDF 미열람) | 약한 간접 | 벤더 자료, 형식 변화 % 없음 |
| E5 | 한국경제 (2026-07-30) — https://v.daum.net/v/20260730185808268 | AI로 자소서가 비슷해져 서류 변별 어려움. HR 전문가 "면접에서 성과보다 **문제 해결 과정·사고 흐름**을 묻는 질문이 중요해졌다". 캐치 Z세대 1,025명 중 98% AI 활용(자소서 초안 84%) | ✅ (Worker) 📰 | 간접 | 개발자 한정 아님 |
| E6 | 디지털타임스 (2025-11-23) — https://v.daum.net/v/20251123025247720 | 기업이 AI 탐지는 참고만, **"최종 판정은 면접으로 직접 확인"**. 캐치 구직자 2,000명 중 91% AI 경험, 무하유 AI 판별 검사 3.6배 증가, 자소서 69~70% AI 도움(카피킬러·프리즘 2025 1Q) | ✅ (Worker) 📰 | 간접 | 개발자 한정 아님 |
| E7 | 코리아비즈니스리뷰 (2025-12-12) — https://www.koreabizreview.com/articles/kbr-legacy-7362 | "심층 면접이 개발자 채용의 새로운 표준" — 설계 선택 이유, "AI가 제안한 코드 오류를 어떻게 검증했나" | ✅ (Worker) | 간접(기자 해석) | 설문 아님 |
| E8 | 📰 Karat — 엔지니어링 리더 400명 중 71% "AI가 기술 평가를 더 어렵게 만든다" | | 📰 (PDF 추출 실패) | 간접 | 원문 미확인 — 쓰려면 재확인 |
| E9 | 📰 Greenhouse (2025-11) — 미국 채용관리자 39%가 검증용 대면 면접 확대 | | 📰 | 간접(대면 회귀) | 질문 유형 변화 아님 |

#### E19 — 잡플래닛 «토스·무신사 개발자 면접 질문, 실제로 이랬다» (2026-07-01) — https://www.jobplanet.co.kr/contents/news-8309
- **상태:** 원문 확인(사용자 브라우저 → 붙여넣기). 자동 접근은 차단돼 있었음.
- **자료 성격:** 잡플래닛 면접 리뷰 중 **2026년 5~6월** 개발자 면접 질문을 에디터가 골라 정리한 큐레이션. 8개 카테고리, 36개 사례. 페이지 상단에 «AD» 표기가 있음(광고성 콘텐츠일 수 있음 — 인용 시 확인).
- **도입부 원문:** "AI가 코드를 대신 짜주는 시대. 면접장의 질문 트렌드도 빠르게 바뀌고 있어요." → 매체의 서술이지 측정값이 아님.
- **C1에 바로 쓸 수 있는 실제 질문(지원자 리뷰 기반):**
  - **이스트소프트(백엔드):** "어떤 프로젝트를 했고 맡은 역할, 담당 기능은? 트러블슈팅 경험은? **왜 이 코드를 썼는지 코드적으로 설명해 주세요.**" — 의도 해설: "이력서에 쓴 프로젝트를 **실제로 본인이 했는지**, 남의 코드를 옮겨 쓴 게 아닌지 확인. **코드 한 줄까지** 파고들어서 진짜 이해도를 검증" ← DevFit 문제 정의와 거의 같은 문장
  - **비바리퍼블리카(토스, 시스템엔지니어):** "기술적으로 흥미로운 부분, **다른 방법은 왜 선택하지 않았는지**" ← 트레이드오프 질문의 직접 사례
  - **안랩(백엔드):** "여태 개발한 것 중 후회되는 게 뭔지"
  - **어드민랩(웹개발):** "JPA 사용 중 겪은 문제와 해결 경험 / 쿼리 성능 개선 경험 / 배포 중 장애 발생 시 대응"
  - **플랜잇헬스케어:** "AI를 이용해 라이브 코딩 시킴", **하나루프:** "AI 안 쓰고 코딩할 수 있나요?", **퀸텟시스템즈:** "AI보다 더 나은 나의 강점이 무엇인지"
- **카테고리 구성(사례 수):** 지원동기 4 · 경력·프로젝트 심화 3 · 기술·CS 6 · 설계·아키텍처 5 · 트러블슈팅·운영 4 · AI 활용 5 · 협업 5 · 커리어 4.
- **직접성:** 간접. 실제로 경험·근거를 묻는 질문이 나왔다는 **국내 정성 사례**로는 직접 근거지만, "비중이 늘었다"는 근거는 아님.
- **한계:** 에디터가 고른 사례라 대표성이 없음. 카테고리별 개수를 «비중»으로 쓰면 안 됨. 시계열 비교 없음. 기술·CS 질문(6건)도 여전히 가장 많음. 인용문은 지원자 후기이고 «질문 의도»는 매체 해설.
- **덱 활용 권장:** 문제 정의 슬라이드에 실제 질문 인용 1~2개. 예: «"왜 이 코드를 썼는지 코드적으로 설명해 주세요" — 2026년 5~6월 실제 개발자 면접 질문(잡플래닛 면접 리뷰)».

### ② AI 때문에 코딩테스트·면접 방식을 바꾼 기업 사례

| ID | 기업 | 무엇을 바꿨나 | 출처 | 상태 | 직접성 |
|---|---|---|---|---|---|
| E10 | **Canva** (2025-06-11) | 백엔드·프론트 "traditional Computer Science Fundamentals screening"을 **AI-Assisted Coding 면접으로 대체**. Copilot·Cursor·Claude 사용 기대. 평가: "Can they make sound technical decisions…", "identify and fix issues in AI-generated code" | https://canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews | ✅ (Opus 재확인) | **직접** · 한계: 파일럿, 현재 상태 미확인, '트레이드오프 설명'은 원문 기준 아님 |
| E11 | **CJ올리브영** (2026-07-21) | 경력 개발 직군 **라이브 코딩 전형 폐지 → AI 과제 도입**. 크래프톤 '코파 프로브'로 "문제 정의 방식, AI 활용 및 프롬프트 작성 과정, 반복 개선 과정, 결과 검증 방식 등 전 과정" 평가 | https://view.asiae.co.kr/article/2026072108302549045 | ✅ 📰 (Opus 재확인) | **직접** (국내 최신·최강) |
| E12 | **넥슨** (2026-09-02) | 인턴십 '넥토리얼' 코딩테스트 폐지, AI 면접·AI 활용 역량평가 도입 (채용팀장 인용) | https://byline.network/2026/09/2-451/ | ✅ (Worker) 📰 | 직접 |
| E13 | **컬리** (2025-06-10) | 개발자 공채 코딩테스트에서 ChatGPT 사용 허용(창립 후 처음) | https://v.daum.net/v/20250610060102680 (중앙일보 단독) | ✅ (Worker) 📰 | 직접 · 일부 블로그의 "2025년 1월"은 오기 |
| E14 | **Google** (2025-06-05) | Pichai: "we'll introduce at least one round of in-person interviews… to make sure the fundamentals are there" + "if you can use these tools to generate better code, I think that's an asset" | https://lexfridman.com/sundar-pichai-transcript/ | ✅ (Worker) | 직접(경영진 1차 발언) · "부정행위 때문" 아님 |
| E15 | 📰 Google AI 허용 파일럿 (2026-05) | 2026 하반기부터 주니어·중급 SWE의 code comprehension 라운드에서 Gemini 허용, AI fluency 평가 (BI 내부 문서 보도) | https://finance.yahoo.com/sectors/technology/articles/asking-kid-math-test-without-151500986.html | 📰 | 직접(내용) / 출처는 언론 |
| E16 | 📰 Meta (2025-07-29) | 일부 코딩 면접에서 AI 어시스턴트 허용 ("more representative of the developer environment…") | https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/ | 📰 | 직접(내용) |
| E17 | Anthropic (2025-07 갱신) | 라이브 면접 "no AI assistance unless we indicate otherwise" — 허용이 아니라 기본 금지 | https://www.anthropic.com/candidate-ai-guidance | ✅ (Worker) | 간접(정책 명문화) |
| E18 | 📰 Amazon (2025 초) | 면접 중 GenAI 사용 시 "disqualification" — 형식 변경 아닌 금지 | itpro.com 재보도 | 📰 | 간접 |

### 못 찾음 (조사 1)
- ❌ 사람인·잡코리아·원티드·점핏·랠릿·인프런·커리어리·프로그래머스의 **기술면접 질문 유형 변화 설문/수치**
- ❌ 토스·카카오·네이버·우아한형제들·당근·라인·쿠팡·삼성의 **AI로 인한 면접/코테 변경 공지**
- ❌ HackerRank Developer Skills Report 원문 수치(게이트) — 비공식 미러 수치 사용 금지
- ❌ "X% 기업이 면접 형식을 변경" 직접 수치 / 경험 질문 비중 시계열
- ✅ 잡플래닛 기사 → 사용자가 원문을 붙여넣어 확인함. 아래 E19 참조. **질문 유형 분포 수치는 없다.**
- ⚠️ 무신사 "면접 전원에 Codex 제공", 그렙 'AI 역량평가'·"66.5% AI 역량 측정 기준 없음" — 스니펫만, 인용 금지

---

## 조사 2 — 경쟁사 비교표 검증

덱 문구: «AI 모의면접(사람인 · Final Round AI 등)은 ① 질문 근거가 이력서·자기소개, ② 근거 코드 확인 없음, ③ 팀 프로젝트 본인 커밋 구분 없음, ④ 한국 채용 공고 맞춤 '일부'»

### 🔴 틀린 칸
1. **Greenroom ①② 틀림** — usegreenroom.app 원문: *"Ari reads your repos before the session starts"*, *"Ari's questions are pulled from your own repos"*, Pro($10/월) 기능 "GitHub repo analysis" (✅ Opus 재확인). 커밋·본인 기여 구분·JD 입력은 페이지에 언급 없음. 인도 시장 중심(₹ 프로모션), 한국 공고 맞춤 없음.
   - 덱에서 Greenroom을 «코드 확인 없음» 칸에 넣지 말 것. 넣는다면 «레포 단위 분석, 본인 커밋 구분·공고 맞춤 확인 안 됨»으로.
   - ⚠️ 의도한 Greenroom이 이 서비스(usegreenroom.app)인지 확인 필요 — 한국 서비스 Greenroom은 못 찾음.
2. **사람인 ④ 수정** — 원문: *"사람인 채용 공고 URL만 입력하면, 기업과 지원 직무에 맞춘 맞춤형 면접 연습이 가능해요."* (✅ Opus 재확인). 공고 맞춤은 있고, 사람인 공고 한정으로 보임(타 사이트 거부 문구는 없음). → «'일부'»보다 **«자사 공고만»**이 정확.

### 칸별 판정

| 서비스 | ① 이력서·자소서 근거 | ② 코드 확인 없음 | ③ 본인 커밋 구분 없음 | ④ 한국 공고 맞춤 '일부' |
|---|---|---|---|---|
| 사람인 AI 모의면접 (m.saramin.co.kr/member/ai-interview) | ✅ 맞음 — "이력서 내용을 분석해 실제 면접처럼 맞춤형 질문" | ✅ 맞음 (GitHub·코드 언급 없음) | ✅ 맞음 | ⚠️ 수정 — 사람인 공고 URL 맞춤 지원 → «자사 공고만» |
| Final Round AI (finalroundai.com/ai-mock-interview) | △ 부분 — 이력서 + JD + 업로드 자료 | ✅ 맞음 | ✅ 맞음 | ✅ 맞음 계열 — JD 텍스트 입력, 한국 공고 URL 언급 없음 |
| Greenroom (usegreenroom.app) | ❌ 틀림 — 근거 = GitHub 레포 | ❌ 틀림 | 확인 불가 (언급 없음) | 확인 불가 (JD 언급 없음) |
| 꼬꼬면 (kokomen.kr, 소마 팀) | △ 부분 — 이력서·포트폴리오 분석 기능 있으나 모의면접 질문은 "면접관 출신 개발자가 직접 작성한 500+ 질문" | ✅ 맞음 | ✅ 맞음 | ✅ 맞음 (공고 언급 없음) |

(사람인·Greenroom은 Opus 재확인, Final Round AI·꼬꼬면은 Worker 확인 — WebFetch 요약 경유라 인용문은 재진술일 수 있음)

### 표에 없던 관련 서비스
- **캐치 AI 면접 튜터** (catch.co.kr/JobN/AIInterviewTutor/main) — "채용공고·이력서까지 반영한 나만의 질문". 공고 맞춤 국내 서비스 → 표 ④ 칸 비교 대상 후보.

### GitHub 레포로 면접 질문을 만드는 다른 서비스 (전부 본인 커밋 구분 언급 없음)
| 서비스 | 내용 | 상태 |
|---|---|---|
| Greenroom (usegreenroom.app) | 음성 AI 면접관이 레포 읽고 프로젝트 질문, 상용 | ✅ |
| techGiterview (github.com/hong-seongmin/techGiterview) | 레포 파일 기반 질문 + 모의면접, 개발 중 (GeekNews 소개 news.hada.io/topic?id=22760) | 📰 |
| PathFinder (github.com/vamsikunal/PathFinder) | 레포·커밋 히스토리로 prep.md 생성 | 검색 요약만 |
| GitHub Interview Question Generator (Greasyfork 스크립트), interview-gen(CLI, 면접관용), GitDog(면접관용 챗봇) | 소규모 도구 | 검색 요약 |
| CleverChatter, GitReady, Archon, Synvex, devfolio AI Mock Interview | 해커톤급 | 검색 요약만 |
| Interviewer.ai, Jobright, Huru, Yoodli, Sensei AI, LockedIn AI, Interview Warmup, Exponent | GitHub 기능 근거 못 찾음 (개별 페이지 미열람 → «없다» 단정 불가) | ❌ |

→ **방어 가능한 차별점:** «팀 레포에서 **본인 커밋·diff만** 골라 + **한국 채용 공고 단위**로 질문» — 경쟁 서비스 공개 페이지에서 이 둘은 확인되지 않음. 덱에는 «공개 페이지 기준» 단서를 붙일 것.

---

## Research Trace
- Worker A(국내 리포트·언론·기술블로그), B(해외 설문·플랫폼 데이터), C(기업 사례), D(경쟁사) 병렬 실행 → Opus가 헤드라인 근거 5건(Pulse #146, Canva, CJ올리브영, Greenroom, 사람인) 원문 재확인.
- 주요 검색어: "AI 코딩 시대 개발자 면접 바뀐다", "인사담당자 설문 AI 자소서 판별 면접", "코딩테스트 폐지 라이브코딩", "interviewing.io AI cheating", "CoderPad State of Tech Hiring 2026", "Karat AI interviews", "GitHub repository interview questions generator".
- 접근 실패: 잡플래닛(자동 접근 차단, 우회 안 함), Gartner(403), Karat PDF, HackerRank(게이트), Amazon BI 원문.
- 한계: 전체 웹을 조사했다고 주장하지 않음. 반대 근거는 따로 찾지 않았고, 조사 중 나온 것(알고리즘 폐기 0명)만 기록.
