"""DevFit GA4·Google Ads 지표 차트 생성 (PPT 16:9용 PNG).

실행: <venv>/bin/python scripts/make_charts.py   (metrics/ 에서)
입력: data/*.csv  출력: charts/*.png (1920x1080)
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

ROOT = Path(__file__).resolve().parent.parent
DATA, OUT = ROOT / "data", ROOT / "charts"
OUT.mkdir(exist_ok=True)

# --- 폰트: Pretendard 단일 패밀리 ---
for f in Path.home().joinpath("Library/Fonts").glob("Pretendard-*.otf"):
    fm.fontManager.addfont(str(f))
plt.rcParams.update({
    "font.family": "Pretendard",
    "axes.unicode_minus": False,
    "font.size": 13,
})

# --- 토큰 (devfit-brand B2C) ---
BRAND = "#6C5CE7"
DEEP = "#5847D6"
LIGHT = "#A99FF2"   # 2계열 비교용 (validator PASS, 대비 WARN → 값 직접 표기)
CONTEXT = "#C9CBD1"  # 강조하지 않는 맥락 막대 (값 직접 표기)
INK = "#171719"
MUTED = "#686D76"
GRID = "#E6E7EA"
BG = "#FFFFFF"

W, H, DPI = 9.6, 5.4, 200  # 1920x1080


def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        rows = [r for r in f if not r.startswith("#")]
    return list(csv.DictReader(rows))


def fig(nrows=1, ncols=1, **kw):
    f, ax = plt.subplots(nrows, ncols, figsize=(W, H), dpi=DPI, facecolor=BG, **kw)
    return f, ax


def style(ax, grid="y"):
    ax.set_facecolor(BG)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=11)
    if grid:
        ax.grid(axis=grid, color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)


def header(f, title, sub, source="출처: GA4 속성 devfit(p551980846) · Google Ads Devfit · 2026-11-04 조회"):
    f.text(0.045, 0.93, title, fontsize=21, fontweight="bold", color=INK, ha="left")
    f.text(0.045, 0.875, sub, fontsize=12.5, color=MUTED, ha="left")
    f.text(0.045, 0.03, source, fontsize=9.5, color=MUTED, ha="left")


def save(f, name):
    f.savefig(OUT / name, dpi=DPI, facecolor=BG)
    plt.close(f)
    print("saved", name)


def won(v):
    return f"₩{v/10000:.1f}만" if v >= 10000 else f"₩{v:,.0f}"


# 00 KPI 요약 -----------------------------------------------------------
def kpi():
    f = plt.figure(figsize=(W, H), dpi=DPI, facecolor=BG)
    header(f, "출시 이후 핵심 지표", "GA4 2026-09-01~11-03 (8월은 동의 게이트로 19명만 수집) · Google Ads 2026-08-24~11-03")
    tiles = [
        ("235명", "GA4 사용자", "9/1 이후 실수집"),
        ("680회", "GA4 세션", "주요 이벤트 108건"),
        ("₩113.7만", "Google Ads 비용", "클릭 2,018회"),
        ("26건", "Ads 전환", "CPA ₩43,730"),
        ("5.7%", "Ads 클릭 중 GA가 본 비율", "GA Cross-network 세션 116"),
        ("~1%", "D7 리텐션", "D1 약 6%"),
    ]
    for i, (v, label, note) in enumerate(tiles):
        c, r = i % 3, i // 3
        x, y = 0.045 + c * 0.31, 0.50 - r * 0.36
        ax = f.add_axes([x, y, 0.29, 0.31])
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_color(GRID)
        ax.set_facecolor("#F7F7F8")
        ax.text(0.07, 0.62, v, fontsize=30, fontweight="bold", color=BRAND if i in (4, 5) else INK, transform=ax.transAxes)
        ax.text(0.07, 0.36, label, fontsize=13, color=INK, transform=ax.transAxes)
        ax.text(0.07, 0.16, note, fontsize=11, color=MUTED, transform=ax.transAxes)
    save(f, "00_kpi_summary.png")


# 01 Ads 주별 비용·전환 (small multiples, 단일 축 원칙) ------------------
def ads_weekly():
    rows = read("ads_weekly.csv")
    labels = [r["week_start"][5:].replace("-", "/") for r in rows]
    cost = [int(r["cost_krw"]) for r in rows]
    conv = [int(r["conversions"]) for r in rows]
    f, (a1, a2) = fig(2, 1, sharex=True, gridspec_kw={"height_ratios": [1.3, 1], "hspace": 0.35})
    f.subplots_adjust(left=0.07, right=0.97, top=0.78, bottom=0.12)
    header(f, "Google Ads 주별 비용과 전환", "10/5 주가 최고점(₩41.6만·전환 12) · 전환 집계는 9/21 주부터 · 11/2 주는 3일치")
    x = range(len(rows))
    b = a1.bar(x, cost, color=BRAND, width=0.62)
    for i, v in enumerate(cost):
        if v > 5000:
            a1.text(i, v + 8000, won(v), ha="center", fontsize=10, color=INK)
    a1.set_title("비용", loc="left", fontsize=12, color=MUTED)
    a1.set_yticks([]); style(a1, None)
    a2.bar(x, conv, color=DEEP, width=0.62)
    for i, v in enumerate(conv):
        a2.text(i, v + 0.3, f"{v}", ha="center", fontsize=10.5, color=INK)
    a2.set_title("전환(기본 전환 = prep_created)", loc="left", fontsize=12, color=MUTED)
    a2.set_yticks([]); style(a2, None)
    a2.set_xticks(list(x)); a2.set_xticklabels(labels)
    a2.axvspan(-0.5, 3.5, color="#F7F7F8", zorder=0)
    a2.text(1.5, max(conv) * 0.6, "전환 추적 전", ha="center", fontsize=10.5, color=MUTED)
    save(f, "01_ads_weekly_cost_conversions.png")


# 02 Ads 채널별 비용 vs 전환 -----------------------------------------------
def ads_channels():
    rows = [r for r in read("ads_channels_alltime.csv") if r["channel"] not in ("TOTAL", "Gmail")]
    rows.sort(key=lambda r: int(r["cost_krw"]))
    names = [r["channel"] for r in rows]
    cost = [int(r["cost_krw"]) for r in rows]
    conv = [int(r["conversions"]) for r in rows]
    total = sum(cost)
    colors = [BRAND if n == "Google 검색" else CONTEXT for n in names]
    f, (a1, a2) = fig(1, 2, sharey=True, gridspec_kw={"wspace": 0.08})
    f.subplots_adjust(left=0.16, right=0.96, top=0.76, bottom=0.12)
    header(f, "PMax 채널별 비용과 전환 (8/24~11/3)", "검색이 비용 69%로 전환 26건 중 21건 · YouTube·파트너·디스커버 ₩27.2만에 전환 1건")
    a1.barh(names, cost, color=colors, height=0.6)
    for i, v in enumerate(cost):
        a1.text(v + total * 0.01, i, f"{won(v)} ({v/total:.0%})", va="center", fontsize=10.5, color=INK)
    a1.set_xlim(0, max(cost) * 1.45); a1.set_xticks([]); a1.set_title("비용", loc="left", color=MUTED, fontsize=12)
    style(a1, None)
    a2.barh(names, conv, color=colors, height=0.6)
    for i, v in enumerate(conv):
        cpa = f" · CPA {won(cost[i]/v)}" if v else ""
        a2.text(v + 0.3, i, f"{v}건{cpa}", va="center", fontsize=10.5, color=INK)
    a2.set_xlim(0, max(conv) * 1.9); a2.set_xticks([]); a2.set_title("전환", loc="left", color=MUTED, fontsize=12)
    style(a2, None)
    a1.tick_params(axis="y", labelsize=12, colors=INK)
    save(f, "02_ads_channel_cost_vs_conversions.png")


# 03 Ads 클릭 vs GA가 본 세션 -------------------------------------------
def visibility():
    names = ["Google Ads 클릭(전체)", "그중 검색 클릭", "GA4 Cross-network 세션"]
    vals = [2018, 321, 116]
    f, ax = fig()
    f.subplots_adjust(left=0.25, right=0.92, top=0.74, bottom=0.14)
    header(f, "광고 클릭 중 GA4에 잡힌 건 5.7%", "동의 거부 사용자 미집계 + YouTube 저품질 클릭 추정 · GA4 수치는 실제 유입의 하한으로 읽어야 해요")
    ax.barh(names[::-1], vals[::-1], color=[BRAND, CONTEXT, CONTEXT], height=0.55)
    for i, v in enumerate(vals[::-1]):
        ax.text(v + 25, i, f"{v:,}", va="center", fontsize=13, color=INK)
    ax.set_xlim(0, 2400); ax.set_xticks([])
    style(ax, None); ax.tick_params(axis="y", labelsize=13, colors=INK)
    save(f, "03_ads_clicks_vs_ga_sessions.png")


# 04 검색어 ----------------------------------------------------------------
def search_terms():
    rows = read("ads_search_terms_top.csv")
    rows.sort(key=lambda r: int(r["clicks"]))
    rows = rows[-16:]
    names = [r["search_term"] for r in rows]
    clicks = [int(r["clicks"]) for r in rows]
    conv = [int(r["conversions"]) for r in rows]
    f, ax = fig()
    f.subplots_adjust(left=0.2, right=0.93, top=0.78, bottom=0.11)
    header(f, "전환된 검색어는 «기술면접·AI 모의면접» 계열뿐", "보라 = 전환 발생 · 회색 = 전환 0 · 클릭 상위 16개(전체 2,980개 중), 8/24~11/3")
    ax.barh(names, clicks, color=[BRAND if c else CONTEXT for c in conv], height=0.62)
    for i, (v, c, r) in enumerate(zip(clicks, conv, rows)):
        ax.text(v + 0.3, i, f"{v}클릭 · {won(int(r['cost_krw']))}" + ("  · 전환 1" if c else ""), va="center", fontsize=9.5, color=INK)
    ax.set_xlim(0, max(clicks) * 1.55); ax.set_xticks([])
    style(ax, None); ax.tick_params(axis="y", labelsize=10.5, colors=INK)
    save(f, "04_ads_search_terms.png")


# 05 월별 퍼널 -------------------------------------------------------------
def funnel():
    rows = read("ga_funnel_by_month.csv")
    tot_s, tot_o = 102, 132
    steps = [r for r in rows if r["step"] in ("cta_click", "login_start", "prep_created", "analysis_started", "study_set_completed")]
    lab = {"cta_click": "CTA 클릭", "login_start": "로그인 시작", "prep_created": "준비 카드 생성", "analysis_started": "레포 분석 시작", "study_set_completed": "학습 세트 완료"}
    names = [lab[r["step"]] for r in steps][::-1]
    s = [int(r["sep_users"]) / tot_s * 100 for r in steps][::-1]
    o = [int(r["oct1_nov3_users"]) / tot_o * 100 for r in steps][::-1]
    sn = [int(r["sep_users"]) for r in steps][::-1]
    on = [int(r["oct1_nov3_users"]) for r in steps][::-1]
    f, ax = fig()
    f.subplots_adjust(left=0.17, right=0.93, top=0.74, bottom=0.12)
    header(f, "단계별 도달 사용자 비율 — 9월 vs 10월", "분모 = 기간 사용자(9월 102명 · 10/1~11/3 132명) · 이벤트를 1회 이상 보낸 사용자")
    y = range(len(names)); h = 0.36
    ax.barh([i + h / 2 for i in y], s, height=h - 0.04, color=LIGHT, label="9월")
    ax.barh([i - h / 2 for i in y], o, height=h - 0.04, color=DEEP, label="10/1~11/3")
    for i in y:
        ax.text(s[i] + 0.6, i + h / 2, f"{s[i]:.0f}% ({sn[i]}명)", va="center", fontsize=10, color=INK)
        ax.text(o[i] + 0.6, i - h / 2, f"{o[i]:.0f}% ({on[i]}명)", va="center", fontsize=10, color=INK)
    ax.set_yticks(list(y)); ax.set_yticklabels(names)
    ax.set_xlim(0, 45); ax.set_xticks([])
    style(ax, None); ax.tick_params(axis="y", labelsize=12, colors=INK)
    ax.legend(loc="lower right", frameon=False, fontsize=11)
    save(f, "05_funnel_sep_vs_oct.png")


# 06 준비 카드 → 분석 시작 전환율 ------------------------------------------
def prep_to_analysis():
    f, ax = fig()
    f.subplots_adjust(left=0.1, right=0.9, top=0.74, bottom=0.16)
    header(f, "준비 카드를 만든 사람 중 분석까지 간 비율이 반토막", "prep_created 사용자 중 analysis_started 사용자 · Fisher 정확검정 p = 0.017 (표본 작음, 방향성 참고)")
    names = ["9월", "10/1~11/3"]
    vals = [14 / 16 * 100, 21 / 40 * 100]
    ax.bar(names, vals, color=[LIGHT, DEEP], width=0.45)
    for i, (v, n) in enumerate(zip(vals, ["14 / 16명", "21 / 40명"])):
        ax.text(i, v + 2, f"{v:.0f}%", ha="center", fontsize=24, fontweight="bold", color=INK)
        ax.text(i, v + 15, n, ha="center", fontsize=11, color=MUTED)
    ax.set_ylim(0, 120); ax.set_yticks([])
    style(ax, None); ax.tick_params(axis="x", labelsize=13, colors=INK)
    save(f, "06_prep_to_analysis.png")


# 07 기기 격차 ----------------------------------------------------------------
def device():
    rows = read("ga_device.csv")
    names = [{"mobile": "모바일", "desktop": "데스크톱", "tablet": "태블릿"}[r["device"]] for r in rows]
    users = [int(r["active_users"]) for r in rows]
    kpu = [float(r["key_events_per_user"]) for r in rows]
    eng = [int(r["avg_engagement_sec_per_user"]) for r in rows]
    f, (a1, a2) = fig(1, 2, gridspec_kw={"wspace": 0.25})
    f.subplots_adjust(left=0.06, right=0.96, top=0.74, bottom=0.14)
    header(f, "들어오는 건 모바일, 쓰는 건 데스크톱", "사용자 1인당 주요 이벤트 — 데스크톱 1.01 vs 모바일 0.12 (약 8배) · 8/1~11/3")
    c = [LIGHT, DEEP, CONTEXT]
    a1.bar(names, users, color=c, width=0.55)
    for i, v in enumerate(users):
        a1.text(i, v + 3, f"{v}명", ha="center", fontsize=13, color=INK)
    a1.set_ylim(0, max(users) * 1.2)
    a1.set_title("활성 사용자", loc="left", color=MUTED, fontsize=12); a1.set_yticks([]); style(a1, None)
    a2.bar(names, kpu, color=c, width=0.55)
    for i, (v, e) in enumerate(zip(kpu, eng)):
        a2.text(i, v + 0.03, f"{v:.2f}", ha="center", fontsize=13, color=INK)
        a2.text(i, -0.12, f"평균 참여 {e//60}분 {e%60}초", ha="center", fontsize=9.5, color=MUTED)
    a2.set_ylim(-0.18, 1.2)
    a2.set_title("1인당 주요 이벤트", loc="left", color=MUTED, fontsize=12); a2.set_yticks([]); style(a2, None)
    for a in (a1, a2):
        a.tick_params(axis="x", labelsize=12, colors=INK)
    save(f, "07_device_gap.png")


# 08 리텐션 곡선 ------------------------------------------------------------
def retention():
    rows = read("ga_retention_curve.csv")
    d = [int(r["day"]) for r in rows]
    v = [float(r["retention_pct"]) for r in rows]
    f, ax = fig()
    f.subplots_adjust(left=0.07, right=0.95, top=0.74, bottom=0.14)
    header(f, "리텐션: D1 약 6%, D7 약 1%", "GA4 유지 개요 «사용자 유지율»(11/3까지 42일) 차트에서 환산한 근사치 · D0 = 100% 생략")
    ax.plot(d[1:], v[1:], color=BRAND, linewidth=2)
    ax.scatter([1, 7], [v[1], v[7]], s=50, color=BRAND, zorder=3, edgecolor=BG, linewidth=2)
    ax.annotate(f"D1 {v[1]:.1f}%", (1, v[1]), xytext=(8, 4), textcoords="offset points", fontsize=12, color=INK)
    ax.annotate(f"D7 {v[7]:.1f}%", (7, v[7]), xytext=(-10, -22), textcoords="offset points", fontsize=12, color=INK)
    ax.set_xlim(0.5, 41.5); ax.set_ylim(0, 8)
    ax.set_xticks([1, 7, 14, 21, 28, 35, 41]); ax.set_xticklabels([f"D{x}" for x in [1, 7, 14, 21, 28, 35, 41]])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _: f"{y:.0f}%"))
    style(ax, "y")
    save(f, "08_retention_curve.png")


# 09 일별 신규 사용자 -----------------------------------------------------
def daily():
    rows = read("ga_daily_new_users.csv")
    d = [r["date"] for r in rows]
    v = [int(r["new_users"]) for r in rows]
    f, ax = fig()
    f.subplots_adjust(left=0.06, right=0.97, top=0.74, bottom=0.14)
    header(f, "일별 신규 사용자 (9/1~11/3)", f"합계 약 {sum(v)}명 · 하루 평균 {sum(v)/len(v):.1f}명 · 차트 SVG 환산 근사치(±1명)")
    ax.bar(range(len(v)), v, color=BRAND, width=0.7)
    top = []
    for i in sorted(range(len(v)), key=lambda i: -v[i]):
        if all(abs(i - j) > 2 for j in top):
            top.append(i)
        if len(top) == 4:
            break
    for i in top:
        ax.text(i, v[i] + 0.3, f"{d[i][5:].replace('-', '/')}\n{v[i]}명", ha="center", fontsize=9.5, color=INK)
    ticks = [i for i, x in enumerate(d) if x.endswith(("-01", "-15"))]
    ax.set_xticks(ticks); ax.set_xticklabels([d[i][5:].replace("-", "/") for i in ticks])
    ax.set_ylim(0, max(v) * 1.35)
    ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    style(ax, "y")
    save(f, "09_daily_new_users.png")


# 10 채널 품질 ---------------------------------------------------------------
def channel_quality():
    rows = [r for r in read("ga_new_user_channels_alltime.csv") if r["first_user_channel"] in ("Direct", "Paid Social", "Cross-network", "Referral", "Organic Search", "Organic Social")]
    lab = {"Direct": "Direct", "Paid Social": "Meta 광고", "Cross-network": "Google PMax", "Referral": "Referral*", "Organic Search": "자연 검색", "Organic Social": "자연 소셜"}
    names = [lab[r["first_user_channel"]] for r in rows][::-1]
    nu = [int(r["new_users"]) for r in rows][::-1]
    rate = [float(r["user_key_event_rate_pct"]) for r in rows][::-1]
    eng = [int(r["avg_engagement_sec_per_active_user"]) for r in rows][::-1]
    f, (a1, a2) = fig(1, 2, sharey=True, gridspec_kw={"wspace": 0.1})
    f.subplots_adjust(left=0.14, right=0.95, top=0.74, bottom=0.14)
    header(f, "첫 유입 채널별 신규 사용자와 전환율", "Meta 광고는 신규 63명 중 주요 이벤트 9.7%·평균 참여 56초 · *Referral은 GitHub OAuth 복귀 세션으로 부풀려짐")
    col = [BRAND if n == "Google PMax" else (LIGHT if n == "Meta 광고" else CONTEXT) for n in names]
    a1.barh(names, nu, color=col, height=0.6)
    for i, v in enumerate(nu):
        a1.text(v + 1, i, f"{v}명", va="center", fontsize=11, color=INK)
    a1.set_xlim(0, 105); a1.set_xticks([]); a1.set_title("신규 사용자", loc="left", color=MUTED, fontsize=12); style(a1, None)
    a2.barh(names, rate, color=col, height=0.6)
    for i, (v, e) in enumerate(zip(rate, eng)):
        a2.text(v + 1, i, f"{v:.0f}% · 참여 {e//60}분 {e%60}초", va="center", fontsize=10.5, color=INK)
    a2.set_xlim(0, 125); a2.set_xticks([]); a2.set_title("주요 이벤트 사용자 비율", loc="left", color=MUTED, fontsize=12); style(a2, None)
    a1.tick_params(axis="y", labelsize=12, colors=INK)
    save(f, "10_channel_quality.png")


# 11 랜딩 페이지 --------------------------------------------------------------
def landing():
    rows = [r for r in read("ga_landing_pages.csv") if r["landing_page"] in ("/", "/candidate/analyze", "/candidate/dashboard", "/login", "/cs")]
    names = [r["landing_page"] for r in rows][::-1]
    sess = [int(r["sessions"]) for r in rows][::-1]
    rate = [float(r["session_key_event_rate_pct"]) for r in rows][::-1]
    f, (a1, a2) = fig(1, 2, sharey=True, gridspec_kw={"wspace": 0.1})
    f.subplots_adjust(left=0.2, right=0.95, top=0.74, bottom=0.14)
    header(f, "방문 페이지별 세션과 전환율", "랜딩 «/» 세션 56% · /candidate/analyze 직접 진입은 전환율 40% · CS 지식백과 /cs 진입은 3세션")
    col = [BRAND if n == "/candidate/analyze" else CONTEXT for n in names]
    a1.barh(names, sess, color=col, height=0.6)
    for i, v in enumerate(sess):
        a1.text(v + 4, i, f"{v}", va="center", fontsize=11, color=INK)
    a1.set_xlim(0, 460); a1.set_xticks([]); a1.set_title("세션", loc="left", color=MUTED, fontsize=12); style(a1, None)
    a2.barh(names, rate, color=col, height=0.6)
    for i, v in enumerate(rate):
        a2.text(v + 0.8, i, f"{v:.1f}%", va="center", fontsize=11, color=INK)
    a2.set_xlim(0, 50); a2.set_xticks([]); a2.set_title("세션 주요 이벤트 비율", loc="left", color=MUTED, fontsize=12); style(a2, None)
    a1.tick_params(axis="y", labelsize=12, colors=INK)
    save(f, "11_landing_pages.png")


# 12 GA4 설정 점검 표 ------------------------------------------------------
def config_table():
    rows = read("ga_config_audit.csv")
    f = plt.figure(figsize=(W, H), dpi=DPI, facecolor=BG)
    header(f, "GA4 설정 점검 결과", "2026-11-04 관리자 화면 실측 · 설정은 변경하지 않음")
    ax = f.add_axes([0.045, 0.08, 0.91, 0.76]); ax.axis("off")
    cols = ["항목", "현재", "문제", "조치"]
    import textwrap
    wr = lambda t, n: "\n".join(textwrap.wrap(t, n, break_long_words=True))
    cell = [[wr(r["item"], 18), wr(r["current"], 24), wr(r["issue"], 38), wr(r["fix"], 30)] for r in rows]
    t = ax.table(cellText=cell, colLabels=cols, loc="upper left", cellLoc="left", colLoc="left",
                 colWidths=[0.17, 0.2, 0.35, 0.28])
    t.auto_set_font_size(False); t.set_fontsize(8)
    nl = [1] + [max(len(x.split("\n")) for x in row) for row in cell]
    unit = 0.98 / sum(n + 0.7 for n in nl)
    for (r, c), cl in t.get_celld().items():
        cl.set_height(unit * (nl[r] + 0.7))
    for (r, c), cl in t.get_celld().items():
        cl.set_edgecolor(GRID); cl.set_linewidth(0.6)
        cl.get_text().set_wrap(True)
        if r == 0:
            cl.set_facecolor("#EFEDFD"); cl.get_text().set_fontweight("bold"); cl.get_text().set_color(INK)
        else:
            cl.get_text().set_color(INK if c != 2 else "#333333")
    save(f, "12_ga_config_audit_table.png")


# 13 Clarity 월별 세션 ----------------------------------------------------
CLARITY_SRC = "출처: Microsoft Clarity 프로젝트 y0zy3l5yz5 · 봇 세션 제외 · 2026-11-04 조회"


def clarity_monthly():
    rows = [r for r in read("clarity_monthly.csv") if r["month"].startswith("2026-")]
    labels = ["8월", "9월", "10월", "11월 1~4일"]
    vals = [int(r["sessions"]) for r in rows]
    insta = [int(r["instagram_sessions"]) if r["instagram_sessions"] else 0 for r in rows]
    f, ax = fig()
    f.subplots_adjust(left=0.07, right=0.95, top=0.74, bottom=0.12)
    header(f, "방문 2.4만 세션, 대부분 Instagram 광고에서 왔어요",
           "Clarity 세션(동의와 무관하게 수집) · 9~10월 세션의 87%가 instagram.com 유입 · 11월 들어 광고가 멈추며 급감",
           CLARITY_SRC)
    x = range(len(vals))
    ax.bar(x, vals, color=CONTEXT, width=0.56, label="전체 세션")
    ax.bar(x, insta, color=BRAND, width=0.56, label="그중 instagram.com 유입")
    for i, (v, n) in enumerate(zip(vals, insta)):
        ax.text(i, v + 250, f"{v:,}", ha="center", fontsize=14, fontweight="bold", color=INK)
        if n > 1000:
            ax.text(i, n / 2, f"{n:,}", ha="center", va="center", fontsize=11.5, color="white")
    ax.set_xticks(list(x)); ax.set_xticklabels(labels, fontsize=13, color=INK)
    ax.set_ylim(0, 14000); ax.set_yticks([0, 5000, 10000])
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    style(ax)
    ax.legend(loc="upper right", frameon=False, fontsize=11.5, labelcolor=INK)
    save(f, "13_clarity_monthly_sessions.png")


# 14 측정 도구별 같은 기간 숫자 ------------------------------------------
def measurement_gap():
    f = plt.figure(figsize=(W, H), dpi=DPI, facecolor=BG)
    header(f, "같은 사람들을 도구마다 다르게 셌어요",
           "출시 이후 누적 · GA4는 동의한 사용자만 집계해 실제의 하한 · 가입·결제는 운영 DB(관리자 콘솔) 기준",
           "출처: Microsoft Clarity · GA4 devfit · Devfit 관리자 콘솔 · 관리자 콘솔 365일 2026-11-04 12:27 KST · 회원 83명 중 팀원·멘토 4명 포함")
    tiles = [
        ("22,360명", "Clarity 고유 방문자", "8/1~11/4 · 세션 23,763", INK),
        ("235명", "GA4 사용자", "Clarity의 약 1% · 동의 사용자만", MUTED),
        ("83명", "가입 회원 (DB)", "내부 제외 약 79명 · 방문자의 약 0.4%", BRAND),
        ("64명", "공고 등록 회원 (DB)", "등록 공고 153건", INK),
        ("13명", "답변까지 간 회원 (DB)", "학습 세트 155건 · 완료 6건", INK),
        ("0건", "결제 (DB)", "Toss LIVE 11-02~", INK),
    ]
    for i, (v, label, note, col) in enumerate(tiles):
        c, r = i % 3, i // 3
        x, y = 0.045 + c * 0.31, 0.50 - r * 0.36
        ax = f.add_axes([x, y, 0.29, 0.31])
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(GRID)
        ax.set_facecolor("#F7F7F8")
        ax.text(0.07, 0.62, v, fontsize=30, fontweight="bold", color=col, transform=ax.transAxes)
        ax.text(0.07, 0.36, label, fontsize=13, color=INK, transform=ax.transAxes)
        ax.text(0.07, 0.16, note, fontsize=11, color=MUTED, transform=ax.transAxes)
    save(f, "14_measurement_gap.png")


# 15 유료 광고 전체 (Meta + Google) ---------------------------------------
def paid_total():
    f, ax = fig()
    f.subplots_adjust(left=0.24, right=0.93, top=0.72, bottom=0.14)
    header(f, "광고비 ₩347.5만, 2/3가 Meta(Instagram)였어요",
           "Meta ₩233.8만 · 링크 클릭 21,318 · 랜딩 조회 15,514  |  Google ₩113.7만 · 클릭 2,018  |  가입 회원 83명 (8/1~11/3)",
           "출처: Meta 광고 관리자 act=1393342212942122 · Google Ads Devfit · 관리자 콘솔 2026-11-04 · Meta는 계정 지출 한도 도달로 게재 중단")
    names = ["Meta · 기본 캠페인 설정", "Meta · test1", "Meta · 10/25 캠페인", "Meta · 10/13 new 캠페인", "Google Ads · PMax"]
    vals = [687298, 918330, 415080, 317500, 1136972]
    notes = ["링크 클릭 9,369 · CPC ₩73", "링크 클릭 7,377 · CPC ₩124", "링크 클릭 3,672 · CPC ₩113",
             "링크 클릭 900 · CPC ₩353", "클릭 2,018 · 전환 26"]
    cols = [BRAND, BRAND, BRAND, BRAND, CONTEXT]
    y = list(range(len(vals)))[::-1]
    ax.barh(y, vals, color=cols, height=0.55)
    for yi, v, n in zip(y, vals, notes):
        ax.text(v + 15000, yi, f"{won(v)}   {n}", va="center", fontsize=12, color=INK)
    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=12.5, color=INK)
    ax.set_xlim(0, 1900000); ax.set_xticks([])
    style(ax, None)
    save(f, "15_paid_ads_total.png")


if __name__ == "__main__":
    for fn in (kpi, ads_weekly, ads_channels, visibility, search_terms, funnel, prep_to_analysis,
               device, retention, daily, channel_quality, landing, config_table, clarity_monthly, measurement_gap, paid_total):
        fn()
