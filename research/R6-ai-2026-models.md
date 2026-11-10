# R6 — 덱 2장 «2026 칸» 최신 모델 근거 (Claude Opus 5.5 · GPT-6 Astra)

> 조사일 2026-11-07 · 요청: ppt-start · Opus가 직접 조사(WebSearch/WebFetch)
> 표기: **✅** = 1차 출처 원문을 열어 확인 · **📰** = 언론·제3자 블로그만 · **🏷 벤더** = 모델을 만든 회사가 직접 잰 값
> 덱 파일·claims.md는 수정하지 않았다.

## 한눈에

| 질문 | 답 |
|---|---|
| METR time horizon (사람 N시간 작업) | **둘 다 없음.** METR은 Opus 5.5를 출시 전에 평가했지만 시간 값은 공개하지 않았다. METR time-horizons 페이지는 2026-09-08 이후 «더 이상 갱신하지 않는다»고 적었고, 목록에 Opus 5.5·Astra가 없다 |
| «Astra»의 정체 | **OpenAI GPT-6 Astra** (2026-09-03 출시, API `gpt-6-astra`). Google Project Astra가 아니다. Anthropic의 Opus 5.5 발표 비교표에도 «GPT-6 Astra»로 나온다 |
| 비전공자용 한 줄로 쓸 수 있는 수치 | METR 값은 없다. 대신 **Anthropic 발표문의 고객 사례**가 있다. «엔지니어 팀이 몇 주 걸릴 68만 줄 코드 이전을 하루 안에», «18시간 넘게 혼자 작업». 모두 🏷 벤더 발표의 일화이고 측정값이 아니다 |

---

## 1. Claude Opus 5.5 (Anthropic)

- 공식 발표: https://anthropic.com/news/claude-opus-5-5 · 발표일 **2026-09-22** ✅
- 모델 ID `claude-opus-5-5`. 가격은 언론 보도 기준 $4/$20 (📰)

### 벤치마크 (발표문 표, 🏷 벤더 측정) ✅

| 벤치마크 | Opus 5.5 | Fable 5.1 | Opus 5 | GPT-6 Astra | GPT-5.6 Sol |
|---|---|---|---|---|---|
| Terminal-Bench 4.0 | **66.4%** | 55.8% | 52.3% | 57.9% | 37.3% |
| FrontierCode v1.1 (Main) | **54.4%** | 50.3% | 48.0% | 53.3% | 47.5% |
| CursorBench 4.0 | 57.8% | 51.8% | 46.6% | — | 41.7% |
| AutomationBench | 40.0% | 31.4% | 26.9% | **41.4%** | 28.8% |
| OSWorld 2.1 (partial) | 81.8% | 80.7% | 74.0% | — | — |
| Terminal-Bench-Science 0.1 | 58.7% | 52.6% | 29.0% | **64.6%** | 22.4% |

- 각주(원문): «all Claude Opus 5.5 results use adaptive thinking at max effort». Terminal-Bench 4.0만 «Opus 5.5 at xhigh effort and GPT-6 Astra at high effort, as reported by OpenAI»다.
- **SWE-bench Verified/Pro는 발표문에 없다.** 제3자 블로그에 도는 «SWE-bench Pro 89.9%» 같은 수치는 1차 출처에서 확인되지 않으니 쓰지 말 것.
- 독립 측정 (📰): Artificial Analysis Terminal-Bench 4.0 59.6%, Vals AI 61.6~65.2%. 설정에 따라 벤더 값보다 낮다.

### 사람 시간 환산에 쓸 수 있는 문장 (🏷 벤더 발표문의 고객 일화) ✅

- «One tester completed a **680,000-line code migration in less than a day**—work that would have taken an engineering team weeks.» (회사명 없음)
- Clio, Sean Heintz: «It stayed on task for **over 18 hours** defining how our services talk to each other» (밤새 레포 6개를 무인으로)
- Stripe, Cristian Rivera: «On a **multi-day rebase of 40 stacked pull requests**, one Claude Opus 5.5 session directed a dozen more sessions»
- Chicago Trading Company: «Overnight, Claude Opus 5.5 autonomously handled a bug … I hadn't had time to diagnose.»

→ 이 문장들은 **측정값이 아니다.** 벤더가 고른 고객 사례이고, 2023~2025 칸의 METR 값과 같은 잣대가 아니다.

### METR

- METR 블로그 «Summary of METR's predeployment evaluation of Claude Opus 5.5» (2026-09-22) https://metr.org/blog/2026-09-22-claude-opus-5-5/ ✅
  - **time horizon 수치 없음.** AI R&D 가속 평가가 중심이다. 원문: «an incremental improvement above Fable 5.1 on our quantitative evaluations», «preliminary evaluation»
- X에 도는 «Opus 5.5 48시간»(Tenobrus)은 ECI 점수를 외삽한 값이다. 작성자 스스로 방법론 근거가 없다고 밝혔으니 **사용 금지.**

## 2. GPT-6 Astra (OpenAI)

- 정체: OpenAI GPT-6 Astra. 출시 **2026-09-03**. API `gpt-6-astra`, 컨텍스트 1,050,000 토큰, 지식 컷오프 2026-04-30
  - 개발자 문서 https://developers.openai.com/api/docs/models/gpt-6-astra.md ✅ (문서에는 출시일과 벤치마크가 없음)
  - 출시일은 Axios 2026-09-03 등 언론 다수 (📰)
- OpenAI 공식 발표 페이지 `openai.com/index/gpt-6-astra/`는 **403으로 열지 못했다.** 아래 OpenAI 수치는 2차 출처를 거쳤다.

| 벤치마크 | Astra | 출처 | 상태 |
|---|---|---|---|
| Terminal-Bench 4.0 | **57.9%** | Anthropic 발표 표, «as reported by OpenAI» | ✅ (Anthropic 페이지, 원 측정은 🏷 OpenAI) — Vellum은 57.7로 적어 0.2p 어긋남 |
| AutomationBench | 41.4% | Anthropic 발표 표 | ✅ (위와 같음) |
| FrontierCode v1.1 Main | 53.3% | Anthropic 발표 표 | ✅ (위와 같음) |
| DeepSWE v1.1 | 74.1% (GPT-5.6 Sol 72.7%) | Vellum, OpenAI 표 인용 https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained | 📰 🏷 |
| OSWorld 2.0 | 72.6% | 같은 곳 | 📰 🏷 |
| AA Coding Agent Index | 67.0 (Fable 5.1 67.2, Fable 5 68.1) | Artificial Analysis, Vellum 경유 | 📰 (독립 측정) |

- METR time horizon: **없음** (METR 페이지 목록에 없음).
- «사람 N시간» 류의 공식 문장: **확인 못 함** (발표 페이지 403).

## 3. METR 공식 페이지 현황

https://metr.org/time-horizons/ ✅
- 마지막 갱신 2026-09-08. 원문: «is no longer actively updated»
- 최신 추가 모델은 Claude Mythos Preview (early, 2026-05-08)이고, Opus 4.6은 2026-02-20에 추가됐다
- 원문: **«Measurements above 16 hrs are unreliable with our current task suite.»** 덱에서 «사람 N시간»을 더 늘리면 측정 한계를 넘는다
- 현재 덱의 «Opus 4.6 12시간»은 Wikipedia METR 항목의 «11 hours 59 minutes (TH 1.1)»와 일치한다 (📰. METR 페이지 텍스트에는 모델별 값이 없고 YAML 데이터에 있음)

---

## 덱 2026 칸 — 권장안

**권장: A안.** B안은 사용자가 Astra까지 넣으라고 했을 때만 쓴다.

- **A안 (추천): METR 잣대는 유지하고 최신 모델은 벤치마크와 일화로 보강**
  - 제목: «2026: 개발자 하루~며칠치 일»
  - 본문: «사람 12시간 작업 (Claude Opus 4.6, METR 측정)» + «Opus 5.5: 혼자 18시간 넘게 작업, 팀이 몇 주 걸릴 68만 줄 이전을 하루 안에 (Anthropic 고객 사례, 2026-09)»
  - 장점: 2023~2025 칸과 같은 METR 잣대가 이어지고, «지금 모델» 요구도 반영한다
- **B안: 사용자 지시대로 Opus 5.5·Astra 기준으로 완전 교체**
  - 제목: «2026: 개발자 며칠치 일»
  - 본문: «Claude Opus 5.5 · GPT-6 Astra — 터미널 실무 과제 Terminal-Bench 4.0에서 66.4% · 57.9%» + 고객 일화
  - 각주: «벤더 측정 · METR 시간 측정값 없음»
  - 단점: 앞 칸과 잣대(METR 시간)가 끊긴다. Terminal-Bench %는 비전공자에게 와닿지 않는다

각주 필수 (어느 안이든):
- «18시간·68만 줄은 Anthropic 발표문의 고객 사례(벤더 선정)이며 측정값이 아님»
- «METR은 Opus 5.5·GPT-6 Astra의 시간 값을 공개하지 않음 (2026-11 기준)»

쓰지 말 것:
- SWE-bench Pro 89.9% 등 블로그 수치 (1차 출처에 없음)
- «Opus 5.5 48시간» (비공식 외삽)
- «Astra가 Opus 5.5보다 낫다/못하다» 단정. 벤치마크마다 1위가 갈린다: Terminal-Bench는 Opus, AutomationBench·T-B Science는 Astra

## 접근 실패
- openai.com/index/gpt-6-astra/ 403 (OpenAI 1차 수치 미확인)
- METR time-horizons 모델별 값 (YAML 데이터 미열람)
