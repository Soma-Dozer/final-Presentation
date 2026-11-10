# 주장 → 근거 → URL 통합본 (research R1~R9 + 덱 슬라이드 출처)

> 정리 2026-11-08 · ppt-start · 원본: `research/R1~R9-*.md` (research-1·2 세션 산출물 + R7 시장 규모·경쟁사 · R8 보고서 시장 동향 대조 · R9 GitHub 채용 활용) + 이 세션에서 만든 Problem 이미지 출처
> R7~R9 통합 2026-11-08. 상세 표·원문 문구는 각 R 파일에 있다.
> **URL 있는 것만** 실었다. URL 없는 내부 근거(R2-ef-offdev·R3-ef-timeline)는 맨 끝 «URL 없음»에 한 줄씩.
> 상태: **✅** 원문 직접 확인 · **📰** 언론·2차 경유(원문 미확인) · **🏷** 벤더 자체 발표
> 수치 옆 «⚠»는 표현 한계 — 덱에 쓸 때 그 단서를 같이 붙일 것.

---

## 1. AI가 코드를 짜는 시대 (Problem 1–2장)

| # | 주장 | 근거 (수치·원문) | URL | 상태 |
|---|---|---|---|---|
| 1-1 | 개발자 대부분이 AI 도구를 쓴다 | Stack Overflow 2025: 84%가 사용 중이거나 사용 예정 (전년 76%). 전체 응답자, 해당 문항 n=33,662 | https://survey.stackoverflow.co/2025/ai | ✅ |
| 1-2 | 쓰는 사람은 많지만 정확도는 덜 믿는다 | 같은 설문: AI 결과 정확도 신뢰 33% vs 불신 46% | https://survey.stackoverflow.co/2025/ai | ✅ |
| 1-3 | Google 신규 코드의 75%가 AI 생성 (엔지니어 검토·승인) | Pichai, Cloud Next 2026-04. 25%(2024-10) → 50%(2025 가을) → 75% | https://www.semafor.com/article/04/24/2026/google-ceo-says-75-of-companys-new-code-is-ai-generated · https://the-decoder.com/google-says-75-percent-of-its-new-code-is-now-written-by-ai/ · https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/ | 📰 (CEO 발언 보도) |
| 1-4 | AI가 혼자 하는 작업 길이가 약 7개월마다 2배 | METR 50% time horizon: GPT-4 약 4분(2023) → Claude 3.7 약 60분(2025-02) → Opus 4.6 약 12시간(2026-02). ⚠ 성공률 50%, 사람 전문가 소요시간 기준, 16시간 초과는 METR 스스로 신뢰 불가 | https://metr.org/assets/benchmark_results_1_1.yaml · https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ · https://metr.org/time-horizons/ | ✅ |
| 1-5 | 실제 GitHub 이슈 해결률이 급상승 | Devin 13.86%(2024-03, 원본 SWE-bench 일부) → Claude 3.5 Sonnet 49.0%(2024-10, Verified) → Sonnet 4.5 77.2%(2025-09). ⚠ 벤치마크가 중간에 바뀜, «2025년 말 약 80%»까지만 | https://cognition.com/blog/introducing-devin · https://www.anthropic.com/news/3-5-models-and-computer-use · https://www.anthropic.com/news/claude-sonnet-4-5 | ✅ |
| 1-6 | SWE-bench 점수 1년 만에 +67.3%p | Stanford AI Index 2025 (2023→2024) | https://hai.stanford.edu/ai-index/2025-ai-index-report | ✅ |
| 1-7 | GitHub 신규 개발자 1년 3,600만 명, 80%가 첫 주에 Copilot 사용 | Octoverse 2025: 1.8억+ 개발자, 신규 3,600만(+23%), 매초 1명 이상 가입 | https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ | ✅ |
| 1-8 | 2026 최신 모델은 하루~며칠치 일을 한다 | Opus 5.5 발표(2026-09-22) 고객 일화: 18시간+ 단독 작업, 68만 줄 이전을 하루 안에. Terminal-Bench 4.0 66.4% (GPT-6 Astra 57.9%). ⚠ 벤더 선정 일화, 측정값 아님 · METR 시간값 없음 | https://anthropic.com/news/claude-opus-5-5 · https://metr.org/blog/2026-09-22-claude-opus-5-5/ | ✅🏷 |
| 1-9 | YC W25 4분의 1은 코드 95%가 AI 생성 | Jared Friedman 발언. ⚠ 기술 창업자 대상, «비전공자» 근거 아님 | https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/ | 📰 |
| 1-10 | 바이브 코딩이 보편화 | Collins 올해의 단어 2025 = vibe coding | https://kvia.com/news/business-technology/cnn-business-consumer/2025/11/06/vibe-coding-named-collins-dictionarys-word-of-the-year/ | 📰 |
| 1-11 | AI 코딩 도구 시장이 커졌다 | Copilot 누적 2,000만+ / Cursor ARR $1B / Lovable ARR 약 $200M · 6천만 프로젝트 / Replit ARR 약 $253M(추정) | https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/ · https://siliconangle.com/2025/11/13/nvidia-google-back-2-3b-round-ai-code-editor-startup-cursor/ · https://www.vktr.com/ai-platforms/lovable-raises-400-million-at-133-billion-valuation/ · https://sacra.com/research/replit-at-253m-arr-growing-2352-yoy/ | 📰 |
| 1-12 | 국내 비개발자도 AI로 앱을 만든다 | 4시간에 서비스, 7일에 앱 사례. 앱스토어 2026 1Q 신규 앱 23.58만(+84%) | https://www.khan.co.kr/article/202606021614001 | 📰 |

**반대 근거 (Q&A 대비)**

| # | 내용 | URL | 상태 |
|---|---|---|---|
| 1-R1 | METR RCT: 숙련 개발자 16명, AI 쓰면 19% 더 느림 (본인은 20% 빨라졌다고 인식). 페이지에 «out of date» | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | ✅ |
| 1-R2 | Veracode: LLM 생성 코드 45%에서 보안 취약점 (벤치마크 과제 80개) | https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ | ✅ |
| 1-R3 | METR 후속(2026-02): 재측정은 «very weak evidence» — 수치 인용 금지 | https://metr.org/blog/2026-02-24-uplift-update/ | ✅ |

---

## 2. 개발자 채용 시장 (Problem 3장)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 2-1 | 개발자 공고가 가장 먼저 줄었다 | 원티드 공고 72,793건(2025-01~2026-04): 유의하게 감소한 직군 6개 중 5개가 개발자. 캐치: 3월 IT·통신 대기업·중견 신입 공고 −73% YoY | https://v.daum.net/v/PPvRLmmjh7 | ✅ (중앙일보 본문, 원자료 미확인) |
| 2-2 | 대형 IT사 신규 채용 급감 | 2022→2024: 네이버 599→258 · 카카오 870→314 · NC 646→311 · 넷마블 224→46 (ESG 보고서, 전 직군) | https://v.daum.net/v/PPvRLmmjh7 | ✅ |
| 2-3 | IT 공고·취업자 감소 | 고용24 IT 24개 분야 공고 2022 8,209 → 2025 2,360. 2026-02 IT 취업자 −4.2만 YoY. ⚠ 고용24는 중소기업 위주, 노동부도 «대표성 없음» | https://www.khan.co.kr/article/202604230600021/amp | ✅ |
| 2-4 | 미국도 소프트웨어 개발 공고 감소 | Indeed 지수 81.6 (2026-10-30, 2020-02=100) → 약 −18% | https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE | ✅ |
| 2-5 | 미국 SW 엔지니어 공고 −49% | Indeed Hiring Lab: 2020 초 대비 −49%, 기술 공고 전체 −36% (2025-07) | https://hiringlab.indeed.com/2025/07/30/the-us-tech-hiring-freeze-continues/ · https://hiringlab.indeed.com/2026/06/18/us-labor-market-snapshot-may-2026/ | ✅ |
| 2-6 | 개발 공고 중 신입 대상은 0.8%, 지원자는 29.5%가 신입 | 사람인·점핏 2025 상반기 (개발 직군) | https://www.etoday.co.kr/news/view/2500510 · https://www.news2day.co.kr/article/20250827500153 | 📰 (리포트 랜딩엔 없음) |
| 2-7 | 개발 공고 9.2만 건 · 지원 260만 건 (2025 상반기) | 공고 92,341 · 지원 2,601,390. ⚠ «약 10만» 아님, 지원은 «건» (1인 다중 지원) | https://jumpit.saramin.co.kr/report/2025/recruit | ✅ |
| 2-8 | 공고의 82%가 «경력만» | 대한상의 2025 상반기 공고 144,181건: 경력만 82%, 신입만 2.6%. 구직자 53.9% «경력 중심이 진입장벽». ⚠ «기업의 82%» 아님, 전 직군 | https://newstomato.com/ReadNews.aspx?no=1266174 | ✅ |
| 2-9 | 대기업 신입의 28.1%가 중고신입 | 한경협 2025 하반기 (121개사) | https://www.segye.com/newsView/20250921508532 | ✅ |
| 2-10 | 신규채용 계획 기업 감소 | 경총: 2022 72.0% → 2025 60.8% (100인 이상 500개사) | https://biz.newdaily.co.kr/site/data/html/2025/03/20/2025032000190.amp.html | ✅ |
| 2-11 | 청년 취업자 감소의 94%가 AI 고노출 업종 | 한은 2026-08: 청년 취업자 −28.5만. 진단은 «기존 추세를 AI가 가속» (단독 원인 아님) | https://etoday.co.kr/news/view/2615429 | ✅ (기사, 한은 PDF 미열람) |
| 2-12 | AI 고노출 직군 22~25세 고용 19% 낮음 | Stanford «Canaries in the Coal Mine» 개정판: 경력자는 격차 없음, 신규 채용 감소 경로. ⚠ «개발자 −20%»는 개정판 본문에 없음 | https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf | ✅ |
| 2-13 | Big Tech 신규 채용 중 신입 비중 7%, 2019 대비 절반 이하 | SignalFire State of Talent 2025. ⚠ 건수 아닌 비중 | https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025 | ✅ |
| 2-14 | 기업은 «직무 경험»을 가장 본다 | 경총 2025: 신규채용 최우선 평가 요소 «직무 관련 업무 경험» 81.6%. ⚠ 전 직군 | https://biz.newdaily.co.kr/site/data/html/2025/03/20/2025032000190.amp.html | ✅ |
| 2-15 | 채용 담당자: «이력서 프로젝트를 물으면 답을 못 한다» | OKKY 설문 IT 전문가 71명: 신입 최소 요건 개인 프로젝트 39.44% | https://byline.network/2025/02/27-431/ | ✅ (표본 작음) |
| 2-16 | 동점 후보면 인턴 경험이 결정 | NACE Job Outlook 2026 (183개사) | https://naceweb.org/talent-acquisition/candidate-selection/internship-experience-often-the-deciding-factor-between-equal-candidates | ✅ |
| 2-17 | 2028년 지원자 4명 중 1명이 가짜 | Gartner 예측 (HR Dive 보도). ⚠ 신원 사기, 코드 이해도와 결이 다름 | https://www.hrdive.com/news/fake-job-candidates-ai/757126/ | 📰 |
| 2-18 | 글로벌 채용 SW 시장 2025년 34.1억 달러 → 2034년 74.8억 달러 (CAGR 8.95%) | Fortune Business Insights (2026-10 갱신). ⚠ 37.4억은 2026 *예측 시작값* — «2026년 37.4억» 쓰지 말 것. 유료 조사업체 자체 추정 | https://www.fortunebusinessinsights.com/recruitment-software-market-100081 | ✅ (R8) |
| 2-19 | HR 업무 AI 도입 43% (전년 26%) | SHRM 2025 Talent Trends, 미국 HR 전문가. 채용 분야 AI 사용 51%. ⚠ 본문 회원 전용, 표본 미확인 | https://www.shrm.org/topics-tools/research/2025-talent-trends/ai-in-hr | 📰 (R8) |
| 2-20 | 개발자 68%가 AI 활용 능력이 채용 요건이 될 것으로 *예상* | JetBrains State of Developer Ecosystem 2025, n=24,534. ⚠ «예상»으로만 | https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/ | 📰 (R8, 403) |
| 2-21 | SW 기업 채용 애로 1순위 «필요 역량 인력 부족» 30.0% | 소프트웨어정책연구소 SW산업 실태조사(컴퓨터월드 2025-07-31 재인용). ⚠ 원 보고서 미확인, «2024 조사»로만 | https://www.comworld.co.kr/news/articleView.html?idxno=51644 | 📰 (R8) |
| 2-22 | Z세대 취준생 98% 취업 준비에 AI 활용 | 진학사 캐치 조사(한국경제 2026-07-07). ⚠ 조사 기간 미공개 | https://www.hankyung.com/article/2026070709791 | ✅ (R8) |
| 2-23 | 사람인 AI 서비스 이용자 96% 증가 (2026 상반기, 전년 하반기 대비) | 뉴스1 2026-07-21. ⚠ «AI 취업 준비 서비스» 아님 — 사람인 **AI 서비스 이용자 전체** | https://www.news1.kr/industry/general-industry/6226185 | ✅ (R8) |
| 2-24 | 잘못된 채용 1건 비용 $14,900, 기업 74%가 잘못 채용 경험 | CareerBuilder·Harris Poll 2017 (미국 HR 2,257명). ⚠ 2017년 미국. «미 노동부 연봉의 30%» 대체용 | https://www.hrdive.com/news/careerbuilder-74-of-employers-admit-hiring-the-wrong-candidate/512577/ | ✅ (R8) |

**반대 근거**

| # | 내용 | URL | 상태 |
|---|---|---|---|
| 2-R1 | 2026 신입 채용 계획 반등: 인크루트 73.4%(+7.9%p), 대기업 87.3% | https://magazine.hankyung.com/job-joy/article/202602105354d | ✅ |
| 2-R2 | 경총 2026 신규채용 계획 66.6%로 반등 | https://biz.sbs.co.kr/amp/article/20000296336 | 📰 |
| 2-R3 | 미국 SW 공고 저점 대비 +15%, 단 증가분 71%가 시니어 | https://www.cio.com/article/4195780/it-hiring-sees-a-boost-as-software-development-jobs-slowly-bounce-back.html | ✅ |
| 2-R4 | Yale Budget Lab: ChatGPT 이후 노동시장 전반 교란 아직 없음 | https://www.theregister.com/2025/10/01/ai_isnt_taking_people_jobs/ | 📰 |
| 2-R5 | 스킬 기반 채용 선언이 실제로는 700건 중 1건 미만 | https://www.hrdive.com/news/employers-failing-at-skills-based-hiring/707897/ | 📰 |

---

## 3. 기술면접이 «왜·어떻게»를 묻는 쪽으로 (Problem 4–5장)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 3-1 | Big Tech 면접관 58%가 AI 때문에 질문을 바꿨다 | interviewing.io 면접관 n=63(Big Tech 45). 원문 «adjusted the kind of questions». «왜 그렇게 짰나»는 별도 인용. ⚠ 58% = 질문 «종류» 조정, «방식» 아님 · 알고리즘 폐기 0명 | https://newsletter.pragmaticengineer.com/p/the-pulse-146 · https://interviewing.io/blog/how-is-ai-changing-interview-processes-not-much-and-a-whole-lot | ✅ |
| 3-2 | 엔지니어링 리더 71%: AI 때문에 기술 역량 평가가 어려워졌다 | Karat 2026 (미·인·중 400명). 같은 자료: 62%는 여전히 면접 AI 금지 | https://karat.com/engineering-interview-trends-2026/ | ✅ |
| 3-3 | 채용 담당자 60%: AI 때문에 실력 평가가 어려워졌다 | WGU 2026-09, 미국 채용 실무자 n=3,128. ⚠ 전 직군 | https://www.wgu.edu/newsroom/press-release/2026/09/ai-has-made-real-skills-harder-to-evaluate.html | ✅ |
| 3-4 | 정형 문제는 AI로 뚫린다 | interviewing.io 실험 32건: LeetCode 원문 통과 73% vs 커스텀 질문 25%, 면접관 부정행위 감지 0건 | https://interviewing.io/blog/how-hard-is-it-to-cheat-with-chatgpt-in-technical-interviews | ✅ |
| 3-5 | 평가 부정행위 시도가 2배 이상 | CodeSignal: 16%(2024) → 35%(2025) | https://codesignal.com/newsroom/press-releases/codesignal-detection-systems-identify-and-stop-record-high-cheating-attempts-as-assessment-fraud-more-than-doubled-in-2025/ | ✅🏷 |
| 3-6 | 채용 담당자 46%가 AI로 면접 답하는 지원자를 목격 | Resume Genius 2026-07. ⚠ 표본 수치가 페이지 안에서 엇갈림 | https://resumegenius.com/blog/job-hunting/ai-impact-on-hiring-2026 | ✅ |
| 3-7 | 국내 실제 면접 질문: «왜 이 코드를 썼는지 코드적으로 설명해 주세요» | 잡플래닛 2026년 5~6월 면접 리뷰 큐레이션 (이스트소프트·토스). ⚠ 사례, 비중 아님 · AD 표기 | https://www.jobplanet.co.kr/contents/news-8309 | ✅ (사용자 붙여넣기로 확인) |
| 3-8 | 시스템 설계·트레이드오프 판단이 중요해짐 | LeadDev: Cursor 온사이트는 자사 코드베이스 과제, Meta는 코드베이스 기반 AI 허용 라운드 | https://leaddev.com/hiring/think-the-technical-interview-is-dead-think-again | ✅ |
| 3-9 | 국내 HR: 성과보다 «문제 해결 과정·사고 흐름» 질문 | 한국경제 2026-07-30. Z세대 98% AI 활용 | https://v.daum.net/v/20260730185808268 | 📰 |
| 3-10 | 국내 기업: 최종 판정은 면접으로 직접 확인 | 디지털타임스 2025-11-23. 구직자 91% AI 경험 | https://v.daum.net/v/20251123025247720 | 📰 |
| 3-11 | 심층 면접이 개발자 채용의 새 표준 | 코리아비즈니스리뷰 2025-12-12 (기자 해석) | https://www.koreabizreview.com/articles/kbr-legacy-7362 | 📰 |
| 3-12 | AI 허용 시 «오류 포착·트레이드오프 설명»을 중시 | CoderPad 2026 State of Tech Hiring (650+) | https://coderpad.io/blog/hiring-developers/new-research-the-2026-state-of-tech-hiring-what-ai-means-for-developers-and-hiring-teams/ | ✅🏷 |

**기업 사례 (면접 방식 변경)**

| # | 기업 · 변경 | URL | 상태 |
|---|---|---|---|
| 3-C1 | Canva: CS 기초 스크리닝 → AI 허용 코딩 면접 (2025-06) | https://canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews | ✅ |
| 3-C2 | CJ올리브영: 경력 개발 라이브 코딩 폐지 → AI 과제로 과정 평가 (2026-07) | https://view.asiae.co.kr/article/2026072108302549045 | ✅ |
| 3-C3 | 넥슨: 인턴 코딩테스트 폐지, AI 면접·AI 활용 평가 (2026-09) | https://byline.network/2026/09/2-451/ | ✅ |
| 3-C4 | 컬리: 개발자 코테에 ChatGPT 허용 (2025-06) | https://v.daum.net/v/20250610060102680 | 📰 |
| 3-C5 | 크래프톤 «코파 프로브»: AI 대화·프롬프트·검증 기록 평가 | https://www.dailian.co.kr/news/view/1684386 | ✅ |
| 3-C6 | Google: 대면 면접 최소 1회 «fundamentals 확인» (Pichai). ⚠ «부정행위 때문» 아님 | https://lexfridman.com/sundar-pichai-transcript/ | ✅ |
| 3-C7 | Google: 2026 하반기 code comprehension 라운드에 Gemini 허용 (BI 보도) | https://finance.yahoo.com/sectors/technology/articles/asking-kid-math-test-without-151500986.html | 📰 |
| 3-C8 | Meta: 일부 코딩 면접 AI 허용 (2025-07) | https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/ | 📰 |
| 3-C9 | Shopify: 도구 허용, 핵심은 생성 코드 리뷰 능력 | https://newsletter.pragmaticengineer.com/p/how-ai-is-changing-software-engineering | ✅ |
| 3-C10 | Cursor: 스크리닝 단계는 AI 금지 | https://newsletter.pragmaticengineer.com/p/the-pulse-138 | ✅ (티저) |
| 3-C11 | Anthropic: 라이브 면접 AI 기본 금지 | https://www.anthropic.com/candidate-ai-guidance | ✅ |

---

## 4. «같은 LLM이라도 차이는 하네스» (Solution 8장)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 4-1 | 같은 모델도 인터페이스만 바꾸면 성능 1.6배 | SWE-agent (NeurIPS 2024): GPT-4 Turbo, SWE-bench Lite 11.0% → 18.0%. 요소 하나 빼면 10.3~15.0 | https://arxiv.org/html/2405.15793v3 | ✅ |
| 4-2 | 같은 모델도 스캐폴드에 따라 성능이 크게 달라짐 | Anthropic: «can vary significantly based on this scaffolding, even when using the same underlying AI model» | https://www.anthropic.com/engineering/swe-bench-sonnet | ✅ |
| 4-3 | 스캐폴드만 바꿔도 최대 11~15% 차이 | Epoch AI: GPT-5 최대 11%, Kimi K2 Thinking 최대 15% | https://epochai.substack.com/p/why-benchmarking-is-hard | ✅ (요약 경유) |
| 4-4 | 테스트 도구를 주면 성능이 크게 오른다 | Anthropic long-running agents (정량 없음) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | ✅ |
| 4-5 | 단순 절차가 복잡한 에이전트를 이긴다 (간접) | Agentless: SWE-bench Lite 32.00%, $0.70/문항 | https://arxiv.org/abs/2407.01489 | ✅ (초록) |
| 4-R | ⚠ 반대: 모델 세대 효과가 더 큼 (같은 스캐폴드 22% → 49%). «하네스가 모델보다 중요» 금지 | https://www.anthropic.com/engineering/swe-bench-sonnet | ✅ |

---

## 5. 경쟁사 (Solution 10장 · Effect 차별점)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 5-1 | Greenroom은 GitHub 레포를 읽는다 (본인 커밋 구분·공고 맞춤은 확인 안 됨) | «Ari reads your repos before the session starts», Pro $10 | https://usegreenroom.app | ✅ |
| 5-2 | 사람인 AI 모의면접은 이력서 기반 + 사람인 공고 URL 맞춤 | «사람인 채용 공고 URL만 입력하면…» | https://m.saramin.co.kr/member/ai-interview | ✅ |
| 5-3 | Final Round AI는 이력서·JD 기반, GitHub 입력 없음 | 입력: target role, company, JD, resume | https://www.finalroundai.com/ai-mock-interview | ✅ (요약 경유) |
| 5-4 | 꼬꼬면은 이력서 + 500+ 문항 은행, GitHub 언급 없음 | — | https://kokomen.kr | ✅ (요약 경유) |
| 5-5 | 캐치 AI 면접 튜터: 공고·이력서 반영 | — | https://www.catch.co.kr/JobN/AIInterviewTutor/main | ✅ |
| 5-6 | 국내 GitHub 기반 면접 질문 도구는 사이드 프로젝트 수준 | techGiterview (오픈소스, 개발 중) | https://github.com/hong-seongmin/techGiterview · https://news.hada.io/topic?id=22760 | 📰 |
| 5-7 | 캐치 AI면접튜터는 **공고·이력서 + 최신 3개년 실제 면접후기(기출)**를 이미 결합 | 1회권 12,000원(30일)·3회권 30,000원. 개발자 전용 아님. → «공고 맞춤 + 기출»은 단독 차별점 아님, 차별점은 «본인 커밋» | https://www.catch.co.kr/JobN/AIInterviewTutor/main | ✅ (R7) |
| 5-8 | 인프런 모의면접: 기출 + 이력서·포트폴리오 PDF(선택), 개발 3직무, 1회 12,000원 | GitHub 입력 없음(공개 페이지 기준) | https://www.inflearn.com/ai-interviews | ✅ (R7) |
| 5-9 | 코드잇 «어센트»: 이력서·자소서 업로드 → 예상 질문 (개발자 특화 아님) | 경쟁사 표 추가 권장. 공식 페이지 미열람 | 한국경제 2026-06-17 (URL은 R7 작업자 c.md) | 📰 (R7) |
| 5-10 | 원티드 AI 면접코칭: 공고 링크만 입력 (2023), 2026 운영 여부 불명 | GPT API, 이력서·GitHub 없음 | https://news.hada.io (GeekNews 2023-03, R7 작업자 c.md) | ✅ 2023 기준 (R7) |
| 5-11 | 그리팅(두들린) 2025 매출 27억 6,188만 원 (+25.5%), 순손실 약 53.8억 | NICE D&B 재무(인크루트 경유). ⚠ «고객사 3,000곳»은 **2023-02** 값 — 연도 붙일 것 | https://www.incruit.com/company/1685961857/ · https://blog.greetinghr.com/doodlin-greeting-story/ | ✅ 매출 / ⚠ 손실 (R7) |
| 5-12 | 티오(TIO): 일반 취준생용 AI 어시스턴트. 공고 링크(사람인·잡코리아·원티드·인크루트·캐치) + 경험 자료(PDF·Notion) → 문항별 자소서 초안·첨삭·기업 분석(DART·뉴스). 면접 준비는 «확장» 언급만, 방식 미공개. GitHub·코드 입력 없음. 무료 하루 AI 5회, 유료 가격 미공개(블로그 9,900/24,900원 ⚠). «취준생 12만 명» 자사 주장 | 개발자 특화 아님 → «공고 맞춤 자소서»는 이미 있음, 차별점은 «본인 코드» | https://tiokorea.com/ | ✅ (11-09, 공식 페이지) |
| ⚠ | **«경쟁자 없음»·«GitHub 읽는 곳 없음» 금지.** 방어 가능한 문장: «공개 페이지 기준, 본인 커밋만 + 질문별 근거 코드 + 한국 공고 단위를 함께 하는 서비스는 확인되지 않음 (2026-11-06)» | — | — |

---

## 6. 시장 규모 · 가격 (Effect · 부록 A11)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 6-1 | 1인당 평가 단가 ₩2만은 공개가 범위 안 | 프로그래머스 ₩16,500/인 · CodeSignal 약 ₩19,000~22,000 · Codility 약 ₩33,600~44,800 (₩1,400/USD) | https://business.programmers.co.kr/business/introduce_coding_test · https://codesignal.com/pricing/ · https://www.codility.com/pricing/ | ✅ |
| 6-2 | 사람 면접 대행은 1건 ₩28만~63만 | Karat 제3자 추정 $200~450 | https://www.vendr.com/marketplace/karat | 📰 |
| 6-3 | 서류 → 면접 전환 10%는 보수적 가정 | 해외 Jobvite 8.4% · 국내 경총 신입 16.0%(2015). ⚠ 국내 개발 직군 실측 없음 → ⚙ 가정 유지 | https://www.jobvite.com/?p=8529 · https://www.kyeonggi.com/article/201505170650470 | 📰 |
| 6-4 | 공고 중 개발·IT 비중 19.9% | 비즈니스피플 2025.1~5. ⚠ 공고 측 비중, 취준생 비중 아님 | https://www.asiae.co.kr/en/article/2025062508402377108 | 📰 |
| 6-5 | 청년 취업시험 준비자 58.5만 명 (개발 비중은 ⚙ 가정) | 통계청 청년층 부가조사 2025.5 | https://dgmbc.com/NewsArticle/632760 · https://biz.newdaily.co.kr/site/data/html/2025/07/24/2025072400277.amp.html | 📰 |
| 6-6 | 국비 개발·디지털 교육 연 5.8만 명 | K-디지털 트레이닝 정원 57,689 (2024). 취업률 50.3%(2023) | https://v.daum.net/v/20240405100138376 · https://magazine.hankyung.com/business/article/202511081461b | 📰 |
| 6-7 | 면접 준비 인원 약 17만~35만 명 (⚙ 환산) | 사람인·점핏 2025 상반기 지원 2,601,390건(2-7) ÷ 신입 1인 평균 지원 15.5곳/7.5곳(잡코리아 2021, 신입 1,126명). ⚠ 2021 일반 신입 수치·플랫폼 간 중복 미제거. 상반기 값 = 연간 하한, ×2 금지 | https://www.inews24.com/view/1399047 | ✅ 원수치 / ⚙ 환산 (R7) |
| 6-8 | B2C 지불 앵커: AI 모의면접 1회 12,000원 | 인프런·캐치 동일 가격 (5-7·5-8) | https://www.inflearn.com/ai-interviews · https://www.catch.co.kr/JobN/AIInterviewTutor/main | ✅ (R7) |
| 6-9 | 취준생 월평균 취업 준비 비용 약 28만 원, 면접비가 가장 큰 부담 10% | 캐치 구직자 1,001명. ⚠ 10%는 «가장 큰 부담으로 꼽은 비율», 지출 비중 아님 | https://mobile.newsis.com/view/NISX20251018_0003367696 | ✅ (R7) |
| 6-10 | 취업 사교육비 연평균 455만 원 (2022 227만 원의 약 2배) | 잡코리아 조사, 교육의봄 재인용. 표본 미공개 | https://www.newsis.com/view/NISX20260609_0003661665 | 📰 (R7) |
| 6-11 | 바텀업 시장 규모 연 0.2억~2.7억 원 | 17만~35만 명(6-7) × 전환 1~5%(⚙) × 객단가 1.2만~1.6만 원(12,000원 ✅ / Plus 7,900×2개월 ⚙). ⚠ 보고서의 1.2/6.2/12.3억보다 한 자릿수 작음(건→명 환산, 객단가 1~2회분) | 위 6-7·6-8 | ⚙ (R7) |
| 6-12 | 글로벌 모의면접·면접 준비 도구 시장 $0.4B~2.5B (정의별 상이) | 벤더 리포트 5종, 2023~24 기준 8배 넘게 벌어짐, CAGR 5~16%. ⚠ 숫자 하나만 인용 금지, 범위로만 | R7 4절 표 | ⚠ (R7) |

---

## 7. 퍼널 해석 (인앱 브라우저 이탈)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 7-1 | 인앱 웹뷰는 브라우저 로그인 상태를 공유하지 않는다 → OAuth 이탈 추정 | RFC 8252 §8.12 «embedded user-agents do not share the authentication state…». ⚠ «추정»으로만, 우리 격차 10배는 외부 근거 범위 밖 | https://www.rfc-editor.org/rfc/rfc8252 | ✅ |
| 7-2 | Google은 2021년 웹뷰 OAuth를 차단 | `disallowed_useragent` | https://developers.googleblog.com/en/upcoming-security-changes-to-googles-oauth-20-authorization-endpoint-in-embedded-webviews/ | ✅ |
| 7-3 | 인앱 → 외부 브라우저로 내보내면 전환 상승 | Escape Hatch: +30%~+241% (벤더, 이커머스) | https://getescapehatch.com/case-studies | 🏷 |
| 7-4 | 웹뷰 OAuth 실패 사례 | Buffer 엔지니어링 (Android Instagram OAuth 멈춤) | https://buffer.com/resources/digging-into-failed-redirects-within-android-webviews/ | ✅ |
| 7-5 | 재직 구직자는 평일 저녁 7~10시 검색 피크 | Indeed 2016 미국. ⚠ «취준생은 밤에 준비» 일반화 금지, 야간 가입은 자체 데이터로만 | https://indeed.com/lead/timing-matters-in-the-job-search | ✅ |

---

## 8. 채용에서 GitHub의 위치 (R9)

| # | 주장 | 근거 | URL | 상태 |
|---|---|---|---|---|
| 8-1 | 채용 담당자 56.8%가 이력서에서 개인 GitHub를 눈여겨본다 (2위) | 프로그래머스 «2023 개발자 채용 트렌드», 채용 담당자 241명(HR 143·개발자 98), 복수응답. 같은 조사 «역량 검증» **52.7%**(보고서 53.4%는 오기) | https://programmers.co.kr/pages/2023-recruiting-survey | ✅ |
| 8-2 | 토스 프론트엔드: 이력서 없이 GitHub 리포지토리 링크만으로 지원받는 전형 (2025-04-08~05-31) | "저희 프론트엔드 리더들은 오직 코드를 기준으로 평가할게요." 평가: 모듈화·디렉토리·TypeScript·커밋/PR 단위·README. ⚠ 합격자 배출 미확인, 원문은 «이력서 없이»(자소서 아님), 한 기업 한시 전형 | https://toss.tech/article/frontend-apply-without-resume | ✅★ |
| 8-3 | 토스 2020 NEXT 공채: 서류 평가 폐지, 이력서·포트폴리오는 코딩테스트 합격자만 | GitHub 언급 없음 | https://toss.im/tossfeed/article/next-developer-recruitment-2020 | ✅ |
| 8-4 | 엔지니어링 리더 34%가 면접 외 준비도 신호로 «GitHub 같은 공개 코드 포트폴리오» | CodePath 2025, 리더 222명 | https://www.codepath.org/news/what-do-tech-companies-want-from-new-hires | ✅★ |

**반대 근거**

| # | 내용 | URL | 상태 |
|---|---|---|---|
| 8-R1 | 원티드 2023: 면접관이 꼽은 채용 평가 중요 요소에서 깃헙 20.3% (9개 중 7위, 지원자 예상 34.2%). 1위 커뮤니케이션 77.6%·프로젝트 경험 75.0% | https://static.wanted.co.kr/images/data_report/Wanted_report_developer.pdf | ✅★ |
| 8-R2 | 공고·지원서에서 GitHub를 요구·우대하는 비율 통계는 **없음** (원티드·점핏·잡코리아·사람인) | — | 못 찾음 |

→ 방어 가능한 범위: «GitHub는 많은 채용 담당자가 *참고*하는 자료이고, 토스처럼 코드만으로 지원받는 전형도 있었다.» **«기본 절차·필수» 금지.**

---

## URL 없음 — 내부 근거 (참고, 이 표엔 안 넣음)

- **R2-ef-offdev** (Dozer 비개발 활동): 멘토링 녹취·사업자등록·직업정보제공 신고·통신판매업·특허 3건·광고 집행. 근거는 로컬 원본(녹취·증명서·캡처)이라 URL이 없음. 경로는 R2-ef-offdev.md 표 참조.
- **R3-ef-timeline** (20주 타임라인): 커밋·PR·서류 날짜. git 해시가 근거.
- 야간 가입 30%, 인앱 전환 0.10~0.15%: 자체 데이터.

## 인용 금지 (URL은 있었지만 1차 미확인·출처 불명)

- 무신사 «면접 전원 Codex 제공», 그렙 «66.5% AI 역량 기준 없음», 그리팅 «82% AI 평가 불신», 무하유 «43.8%» — 스니펫만
- «Instagram 1.2% · Facebook 1.5% · 네이티브 3.4%» 전환율 — 출처 불명
- SWE-bench Verified 2026 96~97%, «SWE-bench Pro 89.9%», «Opus 5.5 48시간» — 1차 출처 없음
- «개발자 22~25세 −20%» — Stanford 개정판 본문에 없음
- TribePad «근무시간 중 61%» — 우리 주장과 반대 방향
- «미 노동부: 잘못된 채용 = 연봉의 최소 30%» — DOL 1차 출처 없음 (R8). 대체는 2-24
- «국내 채용 SaaS 시장 수백억 원대» — 근거 없음 (R7)
- «SW 개발자 약 24.8만 명(SW산업 실태조사 2024)» — 검색 요약뿐, 원문 URL 없음 (R7)
- «GitHub 제출이 기본 절차/필수» · «토스가 깃헙 링크로만 뽑았다» — 근거 범위 밖 (R9)
- «프로그래머스 2020 37.9% → 2023 56.8% 증가» — 문항이 다름 (R9)
