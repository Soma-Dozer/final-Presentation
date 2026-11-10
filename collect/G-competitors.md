# G. 경쟁 지형 — p4 «반론: Claude Code에 GitHub 링크 주면 되지 않나» + 부록 A2

> 조사: 2026-11-05 (KST). 웹 검색·공개 페이지 열람만 했다. 가입·로그인·폼 제출은 하지 않았다.
> **모든 외부 칸의 접근일은 2026-11-05다.** 페이지에 적혀 있지 않은 것은 «확인 불가»로 적었다. «페이지에 없다»는 «기능이 없다»를 증명하지 않는다.
> DevFit 칸은 웹이 아니라 **운영 브랜치 코드**로 확인했다: BE `origin/prod` = `500f4af`(2026-11-03), FE `origin/prod` = `2c46ce6`.
> 재사용한 이전 노트: `Devfit/research/b2b-market/business/04-competitor-landscape.md`(2026-07-15, B2B 고용주 측). Emble·depthhire는 오늘 다시 확인했다.

---

## 0. 결론 먼저

1. **«지원자 본인 GitHub를 읽고 질문하는 B2C 모의면접»은 우리만 하는 일이 아니다.** Greenroom(usegreenroom.app, 2026년 개시, $10/월 Pro에 «GitHub repo analysis» 포함, 음성)이 가장 가깝다. 「유일하다」, 「최초다」, 「세계 유일」이라는 말은 쓰면 안 된다.
2. 오늘 공개 페이지로 확인된 범위에서 DevFit만 동시에 갖춘 것은 네 가지다. 여기서도 «유일»이 아니라 **«공개 자료에서 확인되지 않았다»**로 말한다.
   - (a) **본인이 author인 커밋·PR만** 골라 근거로 쓴다.
   - (b) 질문마다 **그 커밋의 실제 diff와 GitHub 원문 링크**를 붙인다.
   - (c) **한국 채용 공고 URL**(채용 플랫폼 5곳 + 기업 채용 사이트 24곳)을 그대로 받아 공고 단위로 준비한다.
   - (d) 한국어로 제공한다.
3. 범용 LLM이 «레포를 못 읽는다»는 말은 **틀렸다.**
   - ChatGPT GitHub 커넥터는 코드를 읽고 스니펫을 인용한다.
   - Claude.ai GitHub 연동도 파일을 읽는다. 다만 **커밋 이력은 가져오지 않는다**고 공식 문서에 적혀 있다.
   - 우리 파일럿에서 근거를 지어낸 쪽은 «링크만 붙여 넣고 도구가 없는» 경우였다.
   - 그래서 p4의 논지는 «AI가 못 한다»가 아니다. **«올바른 절차(clone → 본인 커밋 필터 → diff 대조 → 공고 대조)를 사용자가 매번 직접 짜야 한다. DevFit은 그 절차를 서버가 강제한다»**로 간다.
4. ⚠️ **이름 충돌 메모가 바뀌었다.** `devfit.co`는 2026-11-05 현재 **도메인 파킹 페이지**다(`/lander` → `LANDER_SYSTEM="PW"`, `ap:"parking"`). 운영 중인 «개발자 면접 준비» 서비스가 아니다. CLAUDE.md 함정 10의 «devfit.co가 같은 카테고리를 점유»는 오늘 실측과 다르다. 같은 이름으로 GitHub 데이터를 써서 기업에 개발자 리포트를 만들어 주던 «DevFit»(BetaList, 2018-03 등재)은 확인된다. 그것이 devfit.co와 같은 회사인지는 확인 불가다.

---

## 1. 비교표 (A2 전체판)

범례
- **O**: 공개 페이지에 명시돼 있다.
- **X**: 공개 페이지에 «없다»고 적혀 있거나, 구조상 그 기능이 아니다.
- **–**: 페이지에 언급이 없다. 부재를 증명하지는 않는다.
- **확인 불가**: 정보를 찾지 못했다.

| 서비스 | 입력 | 본인 코드·커밋을 읽나 | 질문에 근거(파일/커밋/코드) 표시 | 특정 공고 맞춤 | 음성 모의 | 가격 | 한국어 | B2B |
|---|---|---|---|---|---|---|---|---|
| **DevFit** | 공고 URL/이미지 + GitHub 레포 [D1][D2] | **O — 본인 author 커밋·PR만**(`search/commits?q=author:<user>`, `type:pr author:`) [D3]. 파일럿 본인 커밋 28/28 [E] | **O — 질문마다 «근거 코드 보기» diff + «GitHub에서 원문 보기» 링크** [D4] | **O — 채용 플랫폼 5곳 + 기업 채용 사이트 24곳 URL 파싱**, 공고 1개 = 준비 1회 [D1][D2] | O [D5] | Free(음성 면접 월 10회) / Plus 월 7,900원 / 추가생성권 1,900원 [D6] | O | O — 공개 지원 링크 + 면접관 콘솔 [D7] |
| Greenroom | GitHub 레포(+목표 직무, 면접 일정), LinkedIn(Pro) [G1] | O — «Ari reads your repos before the session» [G1]. 커밋 단위인지·본인 필터는 – | – (예시 질문에 레포명만 있고 파일·커밋 표기는 없다) [G1] | – (JD 입력 언급 없음) [G1][G2] | O (voice-first) [G1] | Free 월 1회 / Pro $10 / Premium $20. 레포 분석은 Pro부터 [G2] | – [G1] | 「For teams — Soon」 대기 명단 [G1] |
| Final Round AI | 이력서 + JD + 직무·회사 [F1][F2] | – (GitHub 언급 없음. 코딩은 화면 캡처 풀이) [F1][F2] | – | O (Goal에 JD) [F2] | O («answer out loud») [F2] | Free / Pro $25+/월 [F1] | «143 Languages & accents», 한국어 명시는 없음 [F2] | – |
| 사람인 AI 모의면접 | 이력서 + **사람인 공고 URL** [S1] | X (이력서 기반) [S1] | – | O (사람인 공고 한정) [S1] | O (마이크 필수, 카메라 선택) [S1] | 유료 이용권, 30일 유효, 금액은 페이지에 없음 [S1][S2] | O | – [S1] |
| 꼬꼬면 (kokomen.kr) | 이력서·포트폴리오 [K1] | – (GitHub 언급 없음) [K1] | –. 질문은 «현직 출신이 작성한 500+ 문항 은행» [K1] | – [K1] | O [K1] | 토큰 구매. 금액 확인 불가 [K1] | O (개발자 특화) | – [K1] |
| 잘봐요 | 기업 인재상 지정 + 이력서(유료) [J1] | X | – | 기업 인재상 단위(공고 직접 입력은 –) [J1] | 영상 [J1] | 4,900원~, 3회 15,900원 [J1]. 3자 블로그 출처 | O | – |
| 뷰인터(viewinter) | 확인 불가 (공식 페이지 본문이 비어 있다) [V1] | 확인 불가 | 확인 불가 | 확인 불가 | 확인 불가 (영상면접 계열로 표기) [V1] | 앱 무료 + 인앱 결제 [V2] | O | 확인 불가 |
| Huru | JD 붙여넣기 / LinkedIn·Indeed 공고 확장 프로그램, 242개 직무 은행 [H1] | – | – | O [H1] | O (오디오/영상) [H1] | 구직자 무료, Enterprise 별도 [H1] | X (영·서·포·독·불만) [H1] | O (대학·기관) [H1] |
| Yoodli | 확인 불가 (JD·이력서 업로드 언급 없음) [Y1] | – | – | – | 확인 불가 | Free 5회 / $8 / $20 (연간) [Y1] | – | O (Business/Enterprise) [Y1] |
| Big Interview | 질문 은행 + 이력서 도구 [B1] | – | – | – | 영상 [B1] | $39/월, $99/3개월, $299 평생 [B1] | – | O (대학 커리어센터) [B1] |
| interviewing.io | – (익명 사람 모의면접 + AI 면접관) [I1] | – | – | – | 오디오+채팅 [I1] | 페이지에 없음 [I1] | – | 「For employers」 링크만 [I1] |
| Exponent → **Aced** / Pramp | 질문 은행·강의·코칭. Pramp는 동료 매칭 [X1][X2] | – | – | – | 동료끼리 1:1 [X2] | Pramp 무료 [X2]. 유료 금액 확인 불가 | – | – |
| Google Interview Warmup | — | — | — | — | — | — | — | **2026-04 종료**로 3자 보도. 공식 페이지에는 이름이 없고 Gemini Live를 안내한다 [W1][W2] |
| ChatGPT + GitHub 커넥터 | 사용자가 연결한 레포 [C1] | O — «read, analyze, and cite the relevant snippets» [C1]. 본인 커밋 필터는 사용자가 지시해야 한다 | 사용자가 지시하면 | 사용자가 공고를 붙여 넣으면 | (별도 음성 모드) | 플랜별로 다름 [C1] | O | – |
| Claude.ai + GitHub 연동 | 선택한 브랜치의 파일 [C2] | 파일만 읽는다. **«commit history, PRs… are not retrieved»** [C2] | 사용자가 지시하면 | 사용자가 붙여 넣으면 | – | 모든 플랜(베타) [C2] | O | – |
| (참고) Emble / depthhire | **고용주의** 레포·문서·JD [P1][P2] | X (회사 코드베이스 기반) | – | O (JD) | – | 확인 불가 | – | O (고용주용) |
| (참고) 오픈소스 repo-interviewer | 본인 레포 [R1] | 목표로 적혀 있다(«cite real files and lines»). **Phase 0, star 1** [R1] | 계획 단계 | – | – | 무료 | – | – |

**DevFit 칸 중 «공개 자료상 다른 곳에서 확인되지 않은» 것**
- 본인 author 커밋·PR 필터. Greenroom은 «레포를 읽는다»까지만 적혀 있다.
- 질문별 diff + GitHub 원문 링크.
- 한국 채용 플랫폼·기업 채용 사이트 29곳의 URL 파싱. 사람인은 자사 공고 URL만 받는다.
- 위 셋을 한국어로 한 흐름에 묶은 것.

---

## 2. p4 권장 구성

**보여 줄 행은 3개다.**

| | 내 코드를 읽나 | 근거가 실제로 있나 (파일럿) | 공고 맞춤 |
|---|---|---|---|
| 링크만 준 범용 AI (도구 없음) | 못 읽는다 | **0/18 실존** — 근거 18개를 모두 지어냈다 | 붙여 넣으면 |
| AI 모의면접 (사람인·Final Round 등) | 이력서만 본다 | 해당 없음 (코드 근거가 없다) | O |
| **DevFit** | 본인 커밋만 골라 읽는다 | **28/28 실존**, 질문마다 diff 링크 | 한국 공고 URL 29곳 |

- 행 1이 반론에 직접 답한다. 행 2는 «시장에 이미 AI 면접이 많지 않나»에 답한다. 행 3이 우리 자리다.
- Greenroom은 표에 넣지 않는다. **Q&A 예비 답변으로 준비해 둔다**(아래). 넣으면 심사위원이 «그럼 Greenroom과 뭐가 다르냐»로 25분을 쓴다.
- ⛔ **Claude Code + clone(30/32)은 덱에 넣지 않는다.** QA 대비용으로만 쓴다(E-compare 규칙).

**장표 한 줄 (방어 가능한 형태)**
> «링크만 받은 AI는 근거 18개를 모두 지어냈습니다. 레포를 실제로 열어 내 커밋만 골라 대조하는 절차가 필요하고, DevFit은 그 절차를 매번 서버가 대신합니다. 그 위에 한국 공고 29곳을 그대로 붙입니다.»

**쓰면 안 되는 표현**
- «세계 유일», «최초», «경쟁사 없음»: Greenroom이 있다.
- «AI는 레포를 못 읽는다»: ChatGPT 커넥터와 Claude 연동으로 읽을 수 있다.
- «DevFit 질문이 Claude보다 정확하다»: E-compare 결론 3과 충돌한다.
- «devfit.co와 혼동 주의 / 동명 경쟁사»: 오늘 기준 파킹 도메인이다.

---

## 3. Q&A 예비 답변 (외부 심사위원용)

| 예상 질문 | 답 (사실만) |
|---|---|
| «ChatGPT에 GitHub 연결하면 되잖아요?» | 됩니다. 다만 본인 커밋만 거르기, 공고와 대조하기, 질문마다 diff 붙이기를 사용자가 매번 지시해야 합니다. 저희는 그 절차를 제품에 고정했습니다. Claude.ai 연동은 공식 문서상 커밋 이력을 가져오지 않습니다 [C2]. |
| «Claude Code로 clone하면요?» | 저희 파일럿에서도 근거를 잘 붙였습니다(30/32). 그래서 저희는 정확도가 아니라 절차 강제와 공고 흐름으로 차별화한다고 말씀드립니다. (QA에서만 언급) |
| «GitHub 읽는 모의면접, 이미 있지 않나요? (Greenroom)» | 있습니다. 공개 페이지 기준 Greenroom은 레포를 읽고 음성 면접을 합니다. 본인 커밋 필터, 질문별 근거 표기, 특정 공고 입력, 한국어는 페이지에서 확인되지 않았습니다 [G1][G2]. 저희 입력 단위는 «한국 공고 1개»입니다. |
| «사람인도 공고 맞춤 AI 면접 하는데요?» | 사람인은 이력서와 사람인 공고를 씁니다 [S1]. 코드를 근거로 묻지 않고, 사람인 밖의 공고는 받지 않습니다. 저희는 기업 채용 사이트 24곳을 포함해 29곳을 받습니다. |
| «가격 경쟁력은?» | Plus 월 7,900원입니다. Final Round $25+, Greenroom Pro $10입니다. 결제는 아직 0건이라 가격 검증은 주장하지 않습니다. |

---

## 4. 출처 (모두 접근일 2026-11-05)

- [D1] `Devfit_BE` origin/prod `500f4af` — `prep/JobPostingFetchService` `BOARDS`(채용 플랫폼 5곳) · CLAUDE.md §prep
- [D2] `Devfit_BE` origin/prod `500f4af` — `src/main/java/com/devfit/prep/corporate/CorporateSiteRegistry.java` (`Site()` 24개 실측)
- [D3] `Devfit_BE` origin/prod `500f4af` — `src/main/java/com/devfit/github/GithubService.java:912`(`type:pr author:`), `:927-928`(`search/commits … author:`)
- [D4] `Devfit_FE` origin/prod `2c46ce6` — `components/candidate/study/StudySetWorkspace.tsx:416-430` («근거 코드 보기», `DiffHunk`, «GitHub에서 원문 보기»)
- [D5] `Devfit_FE` — `components/candidate/study/VoiceInterviewStage.tsx`, `VoiceDialogueStage.tsx`
- [D6] `Devfit_FE` origin/prod `2c46ce6` — `app/billing-terms/page.tsx:17-18`
- [D7] CLAUDE.md §B2B (`/apply/{token}`, `/recruit/*`)
- [E] `last-dance/collect/E-compare.md` 요약표 (B2 0/18, A 28/28)
- [G1] https://usegreenroom.app/ · [G2] https://usegreenroom.app/pricing
- [F1] https://www.finalroundai.com/pricing · [F2] https://www.finalroundai.com/ai-mock-interview
- [S1] https://m.saramin.co.kr/member/ai-interview · [S2] https://www.aceround.app/ko/blog/saramin-ai-mock-interview-korea/ (3자, 30일 유효·연습 5문항/실전 11문항)
- [K1] https://kokomen.kr/
- [J1] https://www.aceround.app/ko/blog/jalbwayo-ai-mock-interview-korea/ (3자 블로그, 공식 페이지 미확인)
- [V1] https://www.viewinter.ai/ → https://front.viewinter.ai/index.html (본문 비어 있음) · [V2] https://apps.apple.com/mt/app/viewinter/id1434802044 (검색 요약)
- [H1] https://www.huru.ai/
- [Y1] https://yoodli.ai/pricing
- [B1] https://www.biginterview.com/
- [I1] https://interviewing.io/ (`/pricing`은 404)
- [X1] https://www.aced.io/ («Aced (formerly Exponent)», tryexponent.com/pricing → aced.io/pricing 301 → 404) · [X2] https://www.pramp.com/ · https://prnewswire.com/news-releases/technical-interview-practice-pramp-joins-forces-with-exponent-301428106.html (2021 인수)
- [W1] https://www.aceround.app/blog/google-interview-warmup-review/ · https://www.finalroundai.com/community/t/google-interview-warmup-is-gone-gemini-live-isnt-a-swap/425 (3자, 이해관계 있음) · [W2] https://grow.google/certificates/interview-warmup/ (Interview Warmup 언급 없음, Gemini Live 안내)
- [C1] https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-research-and-codex
- [C2] https://support.claude.com/en/articles/10167454-use-the-github-integration
- [P1] https://emble.in/ · [P2] https://www.depthhire.com/
- [R1] https://github.com/Aryankanani1/repo-interviewer
- devfit.co: `curl -sL https://devfit.co` → `/lander` 파킹 스크립트 · https://betalist.com/startups/devfit (2018-03 Featured, 고용주용 GitHub 리포트)
- 그 밖에 GitHub 기반 한국 프로젝트: Giterview(Medium 글은 403으로 열리지 않았다. 검색 요약상 약 1,000일 전 학생 프로젝트로 레포·이력서 기반, 현재 운영 여부는 확인 불가) — https://github.com/Seungkiii/Giterview

**확인하지 못한 것**
- 뷰인터 개인 요금과 기능
- 사람인·꼬꼬면·Aced 금액
- Greenroom이 커밋을 읽는지, 한국어를 지원하는지
- 잡코리아 자체 AI 모의면접 (공식 페이지를 찾지 못했다)
- Copilot은 IDE 안 도구라 조사하지 않았다.
