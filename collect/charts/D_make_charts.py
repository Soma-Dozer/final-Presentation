import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np, datetime as dt
fp="/System/Library/Fonts/AppleSDGothicNeo.ttc"
fm.fontManager.addfont(fp)
name=fm.FontProperties(fname=fp).get_name()
plt.rcParams.update({"font.family":name,"axes.unicode_minus":False,"figure.facecolor":"white",
  "axes.facecolor":"white","text.color":"black","axes.labelcolor":"black","xtick.color":"black","ytick.color":"black",
  "axes.edgecolor":"black","font.size":20})
OUT="/Users/aiden/dev/teams/ASM/last-dance/collect/charts/"
ACC="#6c5ce7"; GREY="#9a9a9a"; RED="#d63031"
def fig(): 
    f=plt.figure(figsize=(16,9),dpi=120); return f
def foot(f,t): f.text(0.02,0.015,t,fontsize=14,color="#444",va="bottom")
def title(f,t,s=None):
    f.text(0.04,0.93,t,fontsize=34,weight="bold")
    if s: f.text(0.04,0.885,s,fontsize=18,color="#333")

# 1 funnel
f=fig(); title(f,"퍼널: 방문 2.2만 → 가입 83 → 답변 13","가장 큰 이탈은 «방문 → 가입» (99.6% 이탈) · 두 번째는 «분석 → 답변» (77% 이탈)")
ax=f.add_axes([0.30,0.10,0.55,0.74])
steps=[("광고 노출","782,238","Meta+Google 광고 관리자"),("광고 클릭","23,336","Meta 링크 클릭+Google 클릭"),
 ("랜딩 방문자","22,360","Clarity 고유 방문자(전 유입)"),("가입 회원","83","관리자 DB"),("공고 등록","64","관리자 DB"),
 ("레포 분석","57","관리자 DB"),("답변","13","관리자 DB")]
vals=[782238,23336,22360,83,64,57,13]
y=np.arange(len(vals))[::-1]
cols=[GREY,GREY,GREY,ACC,ACC,ACC,ACC]
ax.barh(y,vals,color=cols,height=0.62); ax.set_xscale("log"); ax.set_xlim(5,3e6)
ax.set_yticks(y); ax.set_yticklabels([s[0] for s in steps],fontsize=22)
for yi,v,s in zip(y,vals,steps): ax.text(v*1.15,yi,f"{s[1]}",va="center",fontsize=22,weight="bold")
conv=["","3.0%","(도구 다름)","0.37%","77.1%","89.1%","22.8%"]
for yi,c in zip(y,conv):
    if c: ax.text(2.2e6,yi+0.5,c,ha="right",va="center",fontsize=17,color=RED if c in("0.37%","22.8%") else "#333")
ax.spines[["top","right"]].set_visible(False)
ax.tick_params(axis="x",labelsize=14)
foot(f,"회색 = 광고·분석 도구(서로 기준 다름, 직접 나눗셈 비교 불가) · 보라 = 관리자 DB 정본(11-04 12:27, 회원 83명에 팀원·멘토 4명 포함) · 기간 8/1~11/4 · 별도: 비로그인 공고 등록 62명")
f.savefig(OUT+"D1_funnel.png"); plt.close(f)

# 2 growth
f=fig(); title(f,"누적 회원 8/7 7명 → 11/4 83명","위: 누적 회원(선)·주간 신규 가입(막대) · 아래: Google 광고 주간 지출 · Meta 주간 지출은 데이터 없음(캠페인 합계만 있음)")
import matplotlib.dates as md
ax=f.add_axes([0.07,0.40,0.86,0.44])
cum={"08-07":7,"08-16":9,"08-23":11,"08-30":15,"09-06":23,"09-13":28,"09-20":35,"09-27":40,"10-04":58,"10-11":63,"10-18":70,"10-25":71,"11-01":82,"11-04":83}
d=[dt.date(2026,int(k[:2]),int(k[3:])) for k in cum]; v=list(cum.values())
wk=[dt.date(2026,8,24)+dt.timedelta(7*i) for i in range(10)]
adds=[4,8,5,7,5,18,5,7,1,11]
ax.bar([w+dt.timedelta(3) for w in wk],adds,width=5.5,color="#d9d4fb",label="주간 신규 가입(월~일)")
for w,a in zip(wk,adds): ax.text(w+dt.timedelta(3),a+1,f"+{a}",ha="center",fontsize=16,weight="bold")
ax.plot(d,v,color=ACC,lw=4,marker="o",ms=8,label="누적 회원 (관리자 DB 차트 판독, ±1)")
ax.text(d[-1],v[-1]+4,"83",ha="center",fontsize=20,weight="bold",color=ACC)
ax.set_ylim(0,95); ax.set_ylabel("명"); ax.legend(loc="upper left",fontsize=15,frameon=False)
ax.spines[["top","right"]].set_visible(False); ax.xaxis.set_major_formatter(md.DateFormatter("%m/%d")); ax.tick_params(labelsize=15)
xl=(dt.date(2026,8,4),dt.date(2026,11,7)); ax.set_xlim(*xl)
ax2=f.add_axes([0.07,0.12,0.86,0.20],sharex=ax)
g=[43756,10963,16,487,84031,185330,415553,224413,27541,113605]
ax2.bar([w+dt.timedelta(3) for w in wk],[x/10000 for x in g],width=5.5,color="#555")
for w,x in zip(wk,g): ax2.text(w+dt.timedelta(3),x/10000+1.5,f"{x/10000:.1f}",ha="center",fontsize=13)
ax2.set_ylim(0,52); ax2.set_ylabel("Google 지출\n(만원)",fontsize=14); ax2.spines[["top","right"]].set_visible(False); ax2.tick_params(labelsize=13)
ax2.xaxis.set_major_formatter(md.DateFormatter("%m/%d"))
foot(f,"출처: 관리자 B2C 대시보드 성장 차트(365일, 11-04 12:32) 좌표 판독 ±1 · Google Ads 주간(ads_weekly.csv, 8/24~) · 주간 가입 vs Google 지출 r≈0.20, vs 클릭 r≈0.68(n=10, 9/28 주 1점이 좌우)\nMeta는 11/4 조회 시 «계정 지출 한도 도달»로 게재 중단(중단 날짜 미상) · Clarity 11월 1~4일 세션 163")
f.savefig(OUT+"D2_growth_weekly.png"); plt.close(f)

# 3 in-app gap
f=fig(); title(f,"Instagram 인앱이 늘자 체류·전환이 같이 꺼졌다","Clarity 월별 · 인앱 비중이 낮은 달(8월·11월)과 높은 달(9·10월) 비교")
months=["8월\n인앱 12%","9월\n인앱 91%","10월\n인앱 86%","11월 1~4일\n광고 중단"]
inapp=[11.8,91.1,86.1,None]; active=[138,12,15,120]; per1k=[15.0,3.6,2.2,12.3]
ax=f.add_axes([0.06,0.17,0.40,0.63]); ax.bar(months,active,color=[ACC,GREY,GREY,ACC])
for i,a in enumerate(active): ax.text(i,a+3,f"{a}초",ha="center",fontsize=20,weight="bold")
ax.set_title("세션 평균 활성 시간",fontsize=22); ax.set_ylim(0,165); ax.spines[["top","right"]].set_visible(False); ax.tick_params(labelsize=15)
ax=f.add_axes([0.55,0.17,0.40,0.63]); ax.bar(months,per1k,color=[ACC,GREY,GREY,ACC])
for i,a in enumerate(per1k): ax.text(i,a+0.3,f"{a:.1f}",ha="center",fontsize=20,weight="bold")
ax.set_title("세션 1,000개당 신규 가입",fontsize=22); ax.set_ylim(0,18); ax.spines[["top","right"]].set_visible(False); ax.tick_params(labelsize=15)
foot(f,"활성 시간: Clarity 월별(8월 2.3분, 11월 2.0분 환산) · 가입: 관리자 성장 차트 판독(±1)을 Clarity 세션으로 나눔 — 도구가 달라 방향만 본다. 8월은 팀·멘토 가입 포함, 11월은 표본 163세션.\nGA 기기별 1인당 주요 이벤트: 데스크톱 1.01 vs 모바일 0.12 (8.4배)")
f.savefig(OUT+"D3_inapp_gap.png"); plt.close(f)

# 4 channel cost
f=fig(); title(f,"채널별 비용: 랜딩은 싸고, 가입은 비싸다","광고 합계 ₩347.5만 (Meta ₩233.8만 · Google ₩113.7만) · 가입 1명당 비용은 귀속이 불확실해 범위로 표기")
ax=f.add_axes([0.25,0.16,0.68,0.66])
rows=[("Meta · 랜딩 1회",151,151),("Google · 클릭 1회",563,563),("Google · 전환 1건\n(공고 생성 · GA 집계)",43730,43730),
      ("전체 광고 · 가입 1명",41870,129000),("Meta · 가입 1명(추정)",80800,118800)]
y=np.arange(len(rows))[::-1]
for yi,(n,lo,hi) in zip(y,rows):
    if lo==hi: ax.barh(yi,lo,color=ACC,height=0.5); ax.text(lo*1.15,yi,f"₩{lo:,}",va="center",fontsize=19,weight="bold")
    else:
        ax.barh(yi,hi-lo,left=lo,color="#d9d4fb",height=0.5,edgecolor=ACC,lw=2); ax.text(hi*1.15,yi,f"₩{lo/10000:.1f}만~₩{hi/10000:.1f}만",va="center",fontsize=19,weight="bold")
ax.set_xscale("log"); ax.set_xlim(80,1.2e6); ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontsize=18)
ax.spines[["top","right"]].set_visible(False); ax.tick_params(axis="x",labelsize=14)
foot(f,"전체·가입: 하한 = ₩347.5만 ÷ 83명(전원 광고 유입 가정), 상한 = 광고 귀속 32%(GA 첫 유입 기준 주요 이벤트 중 유료 비중) 가정\nMeta 추정 = 9~10월 비인스타 세션이 8·11월 전환율(1.2~1.5%)로 가입했다고 보고 남은 가입을 Meta에 귀속(20~29명)\n자연 검색: Search Console 클릭 37(대부분 «devfit» 브랜드 검색) · 출처 meta_ads_campaigns_alltime.csv · ads_channels_alltime.csv")
f.savefig(OUT+"D4_channel_cost.png"); plt.close(f)

# 5 VOC clusters
f=fig(); title(f,"직접 들은 목소리 29건: 반론이 가치만큼 많았다","사용자 1 · 현직 개발자 멘토 1 · IT 기업 대표 1 · 소마 전략 멘토 1 — 발언 단위 집계")
ax=f.add_axes([0.28,0.16,0.64,0.64])
cl=[("가치 (질문 품질·관점)",9),("반론 (범용 AI·코드 수준·신뢰)",9),("요청 (기출·음성·시각화·플로우)",6),("고통 (기억·정보·면접 흐름)",5)]
y=np.arange(len(cl))[::-1]; ax.barh(y,[c[1] for c in cl],color=[ACC,RED,GREY,"#333"],height=0.55)
for yi,c in zip(y,cl): ax.text(c[1]+0.15,yi,str(c[1]),va="center",fontsize=24,weight="bold")
ax.set_yticks(y); ax.set_yticklabels([c[0] for c in cl],fontsize=20); ax.set_xlim(0,11); ax.spines[["top","right"]].set_visible(False)
foot(f,"출처: user_interview/devfit_user_interview_jeonggyumin.md · docs/feedback/260907 분석·녹취 · last-dance/05-현장검증.md · planning/07-소마-인증-전략.md\n공개 회고(velog·OKKY) 16건은 별도(우리 사용자 아님) · 표본이 4명이라 빈도는 경향이 아니라 목록이다. 네이버 멘토 2시간 미팅은 기록이 없어 제외")
f.savefig(OUT+"D5_voc_clusters.png"); plt.close(f)
print("ok")
