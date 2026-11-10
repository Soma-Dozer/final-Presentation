# DevFit 출시 이후 지표 (GA4 · Google Ads)

조회일 2026-11-04 · 조회 방법: dozer 계정 Chrome 세션에서 GA4·Google Ads 콘솔을 읽어 옴 (설정은 바꾸지 않음)

- GA4 속성 `devfit` (`a406212787p551980846`, 측정 ID `G-TLTFN3QT2N`)
- Google Ads `Devfit` (PMax `Campaign #1`, 일예산 ₩15,000, 8/24부터 지출)

## 폴더

| 경로 | 내용 |
|---|---|
| `charts/` | PPT용 PNG 13장 (1920×1080, Pretendard, B2C 보라) |
| `data/` | 차트 원본 CSV 20개 |
| `scripts/make_charts.py` | `data/` → `charts/` 재생성 스크립트 |

## 차트 목록

| 파일 | 한 줄 메시지 |
|---|---|
| `00_kpi_summary.png` | 사용자 235 · 세션 680 · Ads ₩113.7만 · 전환 26 · GA가 본 광고 클릭 5.7% · D7 리텐션 ~1% |
| `01_ads_weekly_cost_conversions.png` | 10/5 주 최고점(₩41.6만·전환 12), 전환 집계는 9/21 주부터 |
| `02_ads_channel_cost_vs_conversions.png` | 검색이 비용 69%·전환 21/26, YouTube·파트너·디스커버 ₩27.2만에 전환 1 |
| `03_ads_clicks_vs_ga_sessions.png` | Ads 클릭 2,018 vs GA Cross-network 세션 116 |
| `04_ads_search_terms.png` | 전환된 검색어는 «기술면접·AI 모의면접» 계열뿐 |
| `05_funnel_sep_vs_oct.png` | 단계별 도달률 9월 vs 10월 |
| `06_prep_to_analysis.png` | 준비 카드 → 분석 시작 88% → 52% (p=0.017) |
| `07_device_gap.png` | 1인당 주요 이벤트 데스크톱 1.01 vs 모바일 0.12 |
| `08_retention_curve.png` | D1 ~6%, D7 ~1% |
| `09_daily_new_users.png` | 일별 신규 사용자 9/1~11/3 (하루 평균 3.3명) |
| `10_channel_quality.png` | 첫 유입 채널별 신규 사용자·전환율 |
| `11_landing_pages.png` | 방문 페이지별 세션·전환율 |
| `12_ga_config_audit_table.png` | GA4 설정 점검 표 (10항목) |

## 해석할 때 지켜야 할 것

1. **GA4 실수집은 9/1부터다.** 8월은 동의 게이트 때문에 19명만 잡혔다. 그래서 "8월 출시" 이후 전체 수치가 아니라 9월 이후 수치로 읽어야 한다.
2. **GA4 숫자는 실제의 하한이다.** Consent Mode 기본값이 `denied`라 동의하지 않은 사용자는 보고서에 나오지 않는다. Ads 클릭 대비 GA 세션이 5.7%다.
3. **팀 트래픽이 섞여 있다.** 내부 트래픽 규칙이 0개이고 필터는 «테스트» 상태다. Direct 채널과 `clarity.microsoft.com` 유입이 특히 오염됐다.
4. **Referral 전환율(79%)은 무시한다.** GitHub OAuth 복귀가 `github.com / referral` 세션으로 잡힌다.
5. **표본이 작다.** 사용자 235명 규모다. p값은 방향을 참고하는 용도로만 쓴다.
6. **차트에서 환산한 근사치가 두 개 있다.** `ga_daily_new_users.csv`(±1명)와 `ga_retention_curve.csv`는 GA 차트 SVG 좌표를 축 눈금으로 환산한 값이다. 일별 합계는 사용자 획득 표와 대조했다(9/1~15 44명 일치).

## 다시 만들기

```bash
python3 -m venv .venv && .venv/bin/pip install matplotlib
.venv/bin/python scripts/make_charts.py
```

Pretendard OTF가 `~/Library/Fonts`에 있어야 한글이 깨지지 않는다.

## 운영 DB 기준 수치 (관리자 콘솔, 11-04)

**정본은 `data/admin_db_snapshot_20261104_1227.csv`(12:27 KST 365일 화면, 캡처 `screenshots/admin_b2c_*_20261104-12*.png`)다.** `admin_db_snapshot_20261104.csv`(09:41)는 이력이다. 덱에는 GA가 아니라 이 수치를 쓴다.

- 회원 83명(팀원·멘토 4명 포함, 내부 제외 약 79명) vs GA 신규 가입 이벤트 40명 → GA는 가입의 약 절반만 잡는다.
- 결제 0건·0원. B2B 지표는 콘솔에 아직 연결되지 않았다.

## Microsoft Clarity (11-04)

`data/clarity_dashboard_20261104.csv`, 화면 캡처 `screenshots/clarity_dashboard_30d.jpg`. Clarity는 동의와 무관하게 수집해 GA보다 실제 트래픽에 가깝다. 날짜는 «사용자 지정»으로 8/1부터 고를 수 있다. 월별 수치는 `data/clarity_monthly.csv`, 차트는 `13_clarity_monthly_sessions.png`·`14_measurement_gap.png`.

- 8/1~11/4 세션 23,763 · 고유 방문자 22,360 (GA4 사용자 235의 약 95배). 월별 8월 533 → 9월 10,991 → 10월 12,077 → 11월 1~4일 163.
- 최근 30일만 보면 세션 9,260 · 고유 사용자 8,727.
- 유입의 83%가 instagram.com(7,673세션), 브라우저의 86%가 Instagram 인앱이다. 대부분 Meta 광고로 보인다.
- 활성 시간 16초 · 스크롤 29% · 세션당 1.29페이지 → 인앱 랜딩에서 대부분 바로 이탈한다.
- LCP 7.1초(나쁨), JS 오류의 67%가 React #418(하이드레이션 불일치).
- 프로젝트 이름·도메인은 옛 호스트 `interview.devfit.app`으로 남아 있지만 실제 수집은 `devfit.app`이다.

## Meta 광고 (11-04, 8/1~11/3)

`data/meta_ads_campaigns_alltime.csv`, 캡처 `screenshots/meta_ads_*`, 차트 `15_paid_ads_total.png`.

- 지출 ₩2,338,208 · 노출 666,197 · 링크 클릭 21,318(CPC ₩110) · 랜딩 페이지 조회 15,514(₩151/조회). 캠페인 4개에서 지출.
- 현재 «계정 지출 한도 도달»로 게재 중단 → Clarity 11월 세션 급감(163)과 맞는다.
- Meta 랜딩 조회 15,514 ≈ Clarity instagram.com 세션 20,025 (Meta는 픽셀 로드 기준이라 더 적다). GA4 Paid Social은 이 중 수십 명만 잡았다.
- Google+Meta 합계 ₩3,475,180. 가입 회원 83명으로 나누면 ₩41,870/가입(광고 외 유입 포함, 상한 추정).

## Google Search Console (11-04, 8/4~11/2)

`data/gsc_performance_3m.csv`, 캡처 `screenshots/gsc_performance_3m.jpg`.

- 클릭 37 · 노출 88 · CTR 42% · 평균 순위 5.6. 검색어는 사실상 «devfit» 브랜드 검색뿐(클릭 25/노출 57).
- 자연 검색 유입은 거의 없다 → 유입은 광고(Meta·Google) 의존.
- **GA4 ↔ Search Console 연결 0건**(GA4 관리 › Search Console 링크). 연결은 설정 변경이라 하지 않았다.
