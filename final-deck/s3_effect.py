# -*- coding: utf-8 -*-
# 3부 — Effect + 부록 A4·A5·A9·A11
# 담당: ppt-effect · 공용 헬퍼/CSS는 core.py (ppt-start 관리) — 고칠 일이 있으면 ppt-start에 요청
# 장표 추가: S.append(shell(...)) 다음 줄에 S.note('''발표자 노트''') · 부록은 APX.append(shell('Appendix · A<n>', ...))
# 구성 (2026-11-06 사용자 지시 — 참고 덱 ASM/최종발표_ppt.pdf 36–44장 순서):
#   ① 6개월 타임라인 → ② 개발 외적으로 한 일 → ③ 지표(유저·실운영) → ④ 비즈니스 모델 → ⑤ 비전
# 원칙: 장당 메시지 1개 · 큰 숫자 1~2개 · 본문 3줄 이하 · 뺀 숫자는 노트/부록
from core import *

S = Slides()    # 본편 — 이 파일 순서 그대로 들어간다
APX = Slides()  # 부록 — A번호 순으로 자동 정렬
CSS = r"""
/* BM · 시장 (11-11 보강) */
.ef-bm2{flex:1;min-height:0;display:grid;grid-template-columns:1fr 560px;grid-template-rows:auto auto 1fr;gap:20px 48px;margin-top:6px}
.ef-tiers{grid-column:1;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.ef-tier{background:#f3f2f8;border-radius:22px;padding:28px 28px 26px;display:flex;flex-direction:column;gap:6px}
.ef-tier.on{background:var(--ink);color:#fff}
.ef-tier em{font-style:normal;font-size:22px;font-weight:900;color:var(--purple-deep)}
.ef-tier.on em{color:#c9c2f7}
.ef-tier b{font-size:52px;font-weight:900;letter-spacing:-.05em;line-height:1.1}
.ef-tier b i{font-style:normal;font-size:22px;font-weight:800;margin-left:6px;opacity:.7}
.ef-tier span{font-size:22px;font-weight:800;margin-top:4px}
.ef-tier small{font-size:17px;font-weight:700;opacity:.72;line-height:1.45}
.ef-ue{grid-column:1;display:flex;flex-direction:column}
.ef-ue-h{font-size:24px;font-weight:900;color:var(--muted);letter-spacing:-.03em;margin-bottom:10px}
.ef-ue-h span{font-size:18px;font-weight:700}
.ef-ue-row{display:grid;grid-template-columns:300px 200px 1fr;align-items:baseline;gap:16px;padding:12px 0;border-bottom:1px solid #e6e4ee}
.ef-ue-row span{font-size:23px;font-weight:800;color:var(--ink)}
.ef-ue-row b{font-size:34px;font-weight:900;letter-spacing:-.04em;text-align:right}
.ef-ue-row small{font-size:17px;font-weight:700;color:var(--muted)}
.ef-ue-sum{margin-top:18px;font-size:28px;font-weight:900;letter-spacing:-.04em;color:var(--ink)}
.ef-ue-sum b{color:var(--purple)}
.ef-ue-sum small{font-size:18px;font-weight:700;color:var(--muted);letter-spacing:-.02em}
.ef-pay{grid-column:1;display:flex;align-items:center;gap:18px;background:#f3f2f8;border-radius:16px;padding:16px 26px;font-size:21px;font-weight:800}
.ef-pay b{color:var(--purple-deep);font-weight:900}
.ef-pay span{opacity:.72}
.ef-bm2-shot{grid-column:2;grid-row:1 / span 3;align-self:center;border-radius:18px;overflow:hidden;box-shadow:0 18px 44px rgba(28,20,48,.16);border:1px solid var(--line)}
.ef-bm2-shot img{display:block;width:100%;height:auto}
.ef-one{flex:1;min-height:0;display:grid;grid-template-columns:780px 1fr;gap:64px;align-items:center;padding:0 10px}
.ef-circ{position:relative;width:740px;height:640px}
.ef-circ .c{position:absolute;left:50%;transform:translateX(-50%);bottom:0;border-radius:50%;display:flex;flex-direction:column;align-items:center;text-align:center}
.ef-circ .c em{font-style:normal;font-size:24px;font-weight:900;letter-spacing:.02em}
.ef-circ .c b{font-size:46px;font-weight:900;letter-spacing:-.05em;line-height:1.1}
.ef-circ .c span{font-size:17px;font-weight:700;opacity:.75}
.ef-circ .c code{font-family:inherit;margin-top:6px;font-size:16px;font-weight:800;line-height:1.35;letter-spacing:-.03em;color:var(--purple-deep)}
.ef-circ .som code{color:#ece9fb;font-size:14px}
.ef-circ .tam{width:640px;height:640px;background:#ece9fb;padding-top:34px;color:var(--ink)}
.ef-circ .tam em{color:var(--purple-deep)}
.ef-circ .sam{width:430px;height:430px;background:#c9c2f7;padding-top:30px;color:var(--ink)}
.ef-circ .sam em{color:var(--purple-deep)}
.ef-circ .som{width:220px;height:220px;background:var(--purple);color:#fff;justify-content:center}
.ef-circ .som b{font-size:40px}
.ef-one-r{display:flex;flex-direction:column}
.ef-one-k{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px;margin-bottom:34px}
.ef-one-k>div{background:#f3f2f8;border-radius:20px;padding:20px 24px}
.ef-one-k>div.op{background:none;padding:0;font-size:24px;font-weight:900;color:var(--purple-deep)}
.ef-one-k>div.hi{background:var(--ink);color:#fff}
.ef-one-k small{display:block;font-size:17px;font-weight:800;opacity:.75}
.ef-one-k b{display:block;font-size:46px;font-weight:900;letter-spacing:-.05em;line-height:1.15}
.ef-one-k .hi b{color:#c9c2f7}
.ef-one-k i{display:block;font-style:normal;font-size:15px;font-weight:700;opacity:.7}
.ef-tss{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:22px;padding:0 10px}
.ef-tss-t{width:100%;border-collapse:separate;border-spacing:14px 12px;table-layout:fixed}
.ef-tss-t th{font-size:34px;font-weight:900;text-align:left;padding:0 26px 4px;color:var(--purple-deep);letter-spacing:-.04em}
.ef-tss-t th.b2b{color:#005ce6}
.ef-tss-t th:first-child{width:190px}
.ef-tss-t th.sub{font-size:24px;color:var(--muted)}
.ef-tss-t th.sub.b2b{color:#005ce6}
.ef-tss-t td.ef-pt b{font-size:52px}
.ef-tss-t td.ef-pp b{font-size:34px}
.ef-tss-t td.ef-pp span{font-size:16px}
.ef-tss-t td.ef-pt{background:var(--purple-pale)}
.ef-tss-t tr.som td.ef-pt{background:var(--ink)}
.ef-tss-t th small{display:block;font-size:18px;font-weight:700;color:var(--muted);letter-spacing:-.02em}
.ef-tss-t td{background:#f3f2f8;border-radius:18px;padding:20px 26px;vertical-align:middle;text-align:left}
.ef-tss-t td.b2b{background:#eef4ff}
.ef-tss-t td.k{background:none;font-size:36px;font-weight:900;letter-spacing:-.03em;padding-left:6px}
.ef-tss-t td.k small{display:block;font-size:18px;font-weight:700;color:var(--muted)}
.ef-tss-t td b{display:block;font-size:44px;font-weight:900;letter-spacing:-.05em;line-height:1.15}
.ef-tss-t td span{display:block;font-size:19px;font-weight:700;color:var(--muted);margin-top:4px;letter-spacing:-.03em}
.ef-tss-t td span em{font-style:normal;font-size:14px;font-weight:800;margin-left:8px;padding:2px 6px;border-radius:6px;background:#dfe3ec;color:#4b5161;vertical-align:2px}
.ef-tss-t tr.som td{background:var(--ink);color:#fff}
.ef-tss-t tr.som td.b2b{background:#0b2a5c}
.ef-tss-t tr.som td.k{background:none;color:var(--ink)}
.ef-tss-t tr.som td b{color:#c9c2f7}
.ef-tss-t tr.som td.b2b b{color:#a9c8ff}
.ef-tss-t tr.som td span{color:#d6d3e0}
.ef-tss-note{font-size:17px;font-weight:700;color:var(--muted);padding-left:14px}
.ef-hy{flex:none;margin-top:auto!important;display:grid;grid-template-columns:1.75fr 1fr;grid-template-rows:auto;align-content:center;gap:28px;margin-top:4px}
.ef-hy-c{display:flex;flex-direction:column;gap:16px;border:2px solid #e6e4ee;border-radius:26px;padding:22px 24px}
.ef-hy-c.b2b{border-color:#cfe0ff}
.ef-hy-h{font-size:20px;font-weight:800;color:var(--muted);display:flex;align-items:baseline;gap:12px}
.ef-hy-h b{font-size:30px;font-weight:900;color:var(--purple-deep);letter-spacing:-.03em}
.ef-hy-c.b2b .ef-hy-h b{color:#005ce6}
.ef-hy .ef-tiers{grid-column:auto}
.ef-hy .ef-tier{padding:22px 22px 20px}
.ef-hy .ef-tier b{font-size:46px}
.ef-tier.ent{background:#eef4ff}
.ef-tier.ent em{color:#005ce6}
.ef-tier.ent b{font-size:40px}
.ef-hy-q{background:var(--purple-pale);border-radius:18px;padding:22px 26px}
.ef-hy-qh{font-size:17px;font-weight:800;color:var(--purple-deep)}
.ef-hy-q p{margin:8px 0 6px;font-size:30px;font-weight:900;letter-spacing:-.04em;color:var(--ink)}
.ef-hy-q small{font-size:18px;font-weight:700;color:var(--muted)}
.ef-hy-ue{margin-top:auto;display:flex;flex-direction:column;gap:6px}
.ef-hy-ue div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid #e6e4ee;padding:8px 2px}
.ef-hy-ue span{font-size:20px;font-weight:800}
.ef-hy-ue b{font-size:32px;font-weight:900;letter-spacing:-.04em}
.ef-hy-ue small{font-size:16px;font-weight:700;color:var(--muted);margin-top:4px}
.ef-hy ~ .ef-pay{margin-top:20px;margin-bottom:auto}
.ef-season{margin-top:14px;display:flex;flex-direction:column;gap:10px}
.ef-season-r{display:grid;grid-template-columns:80px 1fr 330px;align-items:center;gap:16px}
.ef-season-r>span{font-size:22px;font-weight:900;color:var(--purple-deep)}
.ef-season-r.b>span{color:#005ce6}
.ef-season-r em{font-style:normal;font-size:20px;font-weight:800;color:var(--ink)}
.ef-season-r em b{color:#005ce6;font-weight:900}
.ef-season .m{display:grid;grid-template-columns:repeat(12,1fr);gap:4px}
.ef-season .m i{font-style:normal;text-align:center;font-size:15px;font-weight:800;padding:6px 0;border-radius:6px;background:#f0eff5;color:#9a97a8}
.ef-season .m i.on{background:var(--purple);color:#fff}
.ef-season .bar{background:#005ce6;color:#fff;border-radius:6px;padding:6px 16px;font-size:16px;font-weight:800;text-align:center}
.ef-ent-r{height:470px}
.ef-msz{flex:1;min-height:0;display:grid;grid-template-columns:.9fr 1.1fr;gap:72px;align-items:center;padding:0 20px}
.ef-msz-l{display:flex;flex-direction:column;gap:14px}
.ef-msz-step{background:#f3f2f8;border-radius:22px;padding:24px 30px}
.ef-msz-step small{display:block;font-size:20px;font-weight:800;color:var(--muted)}
.ef-msz-step b{display:block;font-size:56px;font-weight:900;letter-spacing:-.05em;line-height:1.15}
.ef-msz-step i{display:block;font-style:normal;font-size:16px;font-weight:700;color:var(--muted)}
.ef-msz-step.big{background:var(--ink);color:#fff}
.ef-msz-step.big b{font-size:84px;color:#c9c2f7}
.ef-msz-step.big small,.ef-msz-step.big i{color:#d6d3e0}
.ef-msz-op{font-size:26px;font-weight:900;color:var(--purple-deep);padding-left:30px}
.ef-msz-op i{display:block;font-style:normal;font-size:16px;font-weight:700;color:var(--muted)}
.ef-sc{display:grid;grid-template-columns:90px 1fr 210px;grid-template-rows:auto auto;column-gap:18px;align-items:center;margin-top:22px}
.ef-sc span{font-size:30px;font-weight:900}
.ef-sc i{display:block;height:36px;border-radius:6px;background:#c9c2f7}
.ef-sc i.top{background:var(--purple)}
.ef-sc b{font-size:32px;font-weight:900;letter-spacing:-.04em;text-align:right}
.ef-sc small{grid-column:2 / span 2;font-size:17px;font-weight:700;color:var(--muted);margin-top:6px}
.ef-msz-note{margin-top:30px;padding-top:18px;border-top:1px solid #e6e4ee;font-size:20px;font-weight:800;color:var(--ink);line-height:1.5}

/* 파워유저 (11-11) */
.ef-pu{display:grid;grid-template-columns:1.25fr .75fr;gap:64px;width:100%;align-items:start;padding:0 20px}
.ef-pu-t{width:100%;border-collapse:collapse;font-size:22px}
.ef-pu-t th{font-size:17px;font-weight:800;color:var(--muted);text-align:right;padding:0 10px 12px;border-bottom:2px solid var(--ink);white-space:nowrap}
.ef-pu-t td{padding:11px 10px;text-align:right;font-weight:700;color:var(--ink);border-bottom:1px solid #e6e4ee;white-space:nowrap;font-variant-numeric:tabular-nums}
.ef-pu-t th:first-child,.ef-pu-t td:first-child{text-align:left}
.ef-pu-t td:first-child{font-weight:900}
.ef-pu-t td.d{color:var(--purple-deep)}
.ef-pu-t td.d b{font-size:26px;font-weight:900}
.ef-pu-r .ef-bar{grid-template-columns:170px 1fr 56px;gap:14px;margin-bottom:12px}
.ef-pu-r .ef-bar span,.ef-pu-r .ef-bar b{font-size:22px}
.ef-pu-r .ef-bar i{height:26px}
.ef-d3{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;align-items:start;margin:auto 0}.ef-d3 figure{margin:0;text-align:center}.ef-d3 img{height:560px;max-width:100%;object-fit:contain;display:block;margin:0 auto;border:1px solid var(--line);box-shadow:0 18px 40px rgba(20,16,40,.14);background:#fff}.ef-d3 figcaption{margin-top:16px;font-size:16px;font-weight:700;color:var(--muted)}.ef-d3 figcaption b{display:block;font-size:22px;font-weight:900;color:var(--ink);margin-bottom:2px}
.ef-dj{display:grid;grid-template-columns:auto 1fr;gap:44px;align-items:center;margin:auto 0}.ef-dj .ef-law-doc{transform:none}.ef-dj .ef-law-doc img{height:600px;width:auto}.ef-dj .r{display:flex;flex-direction:column;gap:22px}.ef-dj .why{font-size:24px;font-weight:700;line-height:1.55;color:var(--ink);background:var(--purple-pale);border-radius:18px;padding:22px 28px;word-break:keep-all}.ef-dj .why small{display:block;font-size:16px;font-weight:900;color:var(--purple);margin-bottom:6px}.ef-dj .why b{color:var(--purple)}.ef-dj .ef-law-act p{font-size:17px}.ef-dj .src{display:block;margin-top:10px;font-size:14px;color:var(--muted);font-family:inherit}
.ef-dp{display:grid;grid-template-columns:1fr 1fr;gap:40px;flex:1;min-height:0}.ef-dp .l,.ef-dp .r{position:relative;min-height:620px}.ef-dp .hd{font-size:18px;font-weight:900;color:var(--purple)}.ef-dp .nt,.ef-dp .sp{position:absolute}.ef-dp .nt img{width:600px;display:block;border:1px solid var(--line);box-shadow:0 14px 34px rgba(20,16,40,.16);background:#fff}.ef-dp .sp img{height:560px;display:block;border:1px solid var(--line);box-shadow:0 14px 34px rgba(20,16,40,.16);background:#fff}.ef-dp .l .nt,.ef-dp .l .hd{margin-left:var(--ofl)}.ef-dp .r .sp,.ef-dp .r .hd{margin-left:var(--ofr)}.ef-dp .l{--ofl:calc((100% - 668px)/2)}.ef-dp .r{--ofr:calc((100% - 640px)/2)}.ef-dp .tag{position:absolute;left:12px;top:-14px;background:var(--ink);color:#fff;font-size:14px;font-weight:800;padding:5px 11px;border-radius:4px;white-space:nowrap}

/* 부록 A16 직업정보제공사업 법률 (11-11) */
.ef-lawa{flex:1;min-height:0;display:grid;grid-template-columns:470px 1fr;gap:56px;align-items:center;margin-top:10px;padding:0 20px}
.ef-lawa .ef-law-doc img{max-height:640px;width:auto;max-width:100%}
.ef-lawa .ef-law-act{padding:36px 44px}
.ef-lawa .ef-law-act h4{font-size:30px;margin-bottom:22px}
.ef-lawa .ef-law-act p{font-size:23px;line-height:1.7;margin-bottom:18px}
.ef-lawa .ef-law-act .src{display:block;margin-top:22px;font-family:Pretendard,sans-serif;font-size:17px;font-weight:700;color:var(--muted)}

.ev-a .sd img{height:600px}
/* Effect — 장당 핵심 1개 (참고: ASM/최종발표_ppt.pdf 40–44) */
.ef-stage{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;width:100%}
.ef-col{flex:1;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;width:100%}
.ef-two{display:grid;grid-template-columns:1fr 1fr;gap:110px;width:100%;padding:0 60px;align-items:end}
.ef-num b{display:block;font-size:210px;font-weight:900;line-height:1;letter-spacing:-.06em;color:var(--purple)}
.ef-num b.k{color:var(--ink)}
.ef-num b small{font-size:.42em;letter-spacing:-.04em;margin-left:6px}
.ef-num span{display:block;margin-top:24px;font-size:34px;font-weight:800;line-height:1.4;letter-spacing:-.04em;color:var(--ink);word-break:keep-all}
.ef-num i{display:block;margin-top:10px;font-style:normal;font-size:22px;font-weight:700;color:var(--muted)}
.ef-line{text-align:center;font-size:34px;font-weight:900;letter-spacing:-.045em;color:var(--ink)}
.ef-line span{color:var(--purple)}
.ef-shot{background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:18px 22px;overflow:hidden}
.ef-shot img{display:block;width:100%;height:auto}
.ef-bm{display:grid;grid-template-columns:1.05fr .95fr;gap:70px;width:100%;align-items:center}
.ef-bm .ef-shot{padding:0}
.ef-rows{display:flex;flex-direction:column;gap:30px}
.ef-row{display:grid;grid-template-columns:230px 1fr;align-items:baseline;gap:20px}
.ef-row span{font-size:30px;font-weight:800;color:var(--muted);letter-spacing:-.03em}
.ef-row b{font-size:64px;font-weight:900;letter-spacing:-.05em;color:var(--ink)}
.ef-row b.p{color:var(--purple)}
.ef-row b small{font-size:28px;font-weight:800;color:var(--muted);margin-left:8px;letter-spacing:-.02em}
.ef-vision{width:100%;max-width:1220px}
.ef-vision img{display:block;width:100%;height:auto;border-radius:22px}
.ef-chips{display:flex;gap:36px;justify-content:center;flex-wrap:wrap;font-size:24px;font-weight:800;color:var(--ink);letter-spacing:-.03em}
.ef-chips span.dev:before{background:#fff;box-shadow:inset 0 0 0 3px #9a94a3}
.ef-chips span:before{content:'';display:inline-block;width:12px;height:12px;border-radius:50%;background:#1f9d55;margin-right:10px;vertical-align:middle}
.ef-road{display:grid;grid-template-columns:.8fr 1.2fr;gap:80px;width:100%;align-items:center}
.ef-road .step-strip{margin-top:0}
.ef-tl{flex:1;min-height:0;display:grid;grid-template-columns:200px repeat(5,1fr);grid-template-rows:auto repeat(4,1fr);gap:10px;position:relative}
.ef-tl .wk{text-align:center;font-size:22px;font-weight:900;color:var(--ink);letter-spacing:-.03em;padding:8px 0 10px;border-bottom:3px solid var(--line)}
.ef-tl .wk small{display:block;font-size:16px;font-weight:700;color:var(--muted);margin-top:2px}
.ef-tl .ln{display:flex;align-items:center;font-size:22px;font-weight:900;color:var(--muted);letter-spacing:-.03em;border-right:3px solid var(--line);padding-right:14px}
.ef-tl .ln.biz{color:var(--purple)}
.ef-tl .cell{display:flex;flex-direction:column;justify-content:center;gap:8px;min-height:0;border-bottom:1px dashed #e1dde7;padding:6px 0}
.ef-tl .pill{background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px 12px;font-size:18px;font-weight:800;line-height:1.3;letter-spacing:-.035em;color:var(--ink);box-shadow:0 4px 12px rgba(25,20,40,.05)}
.ef-tl .pill small{display:block;font-size:14px;font-weight:700;color:var(--muted)}
.ef-tl .pill.biz{background:var(--purple-pale);border-color:transparent;color:var(--purple-deep)}
.ef-tl .pill.star{background:var(--purple);border-color:transparent;color:#fff}
.ef-tl .pill.star small{color:#ddd8ff}
.ef-tlhead{display:flex;align-items:baseline;justify-content:space-between;margin:-6px 0 14px}
.ef-tlhead .ph{display:flex;gap:10px}
.ef-tlhead .ph span{padding:4px 2px 6px;color:#a19ba7;font-size:18px;font-weight:900;border-bottom:3px solid transparent}
.ef-tlhead .ph span.on{color:var(--purple-deep);border-bottom-color:var(--purple)}
.ef-tlhead .big{font-size:24px;font-weight:800;color:var(--muted)}
.ef-tlhead .big b{font-size:46px;font-weight:900;color:var(--purple);letter-spacing:-.05em;margin:0 6px}
.ef-law{display:grid;grid-template-columns:1fr 1fr;gap:40px;flex:1;min-height:0;margin-top:8px}
.ef-law-l,.ef-law-r{border-radius:28px;padding:36px 40px;display:flex;flex-direction:column;min-height:0}
.ef-law-l{background:#f3f2f8}
.ef-law-r{background:#f3f2f8}
.ef-law-h{display:flex;align-items:center;gap:16px}
.ef-law-h b{font-size:34px;font-weight:900;letter-spacing:-.045em}
.ef-law-stage{flex:1;margin-top:30px;display:grid;grid-template-columns:330px 1fr;gap:28px;align-items:center}
.ef-law-doc{position:relative;transform:rotate(-1.5deg)}
.ef-law-doc img{display:block;width:100%;height:auto;border:1px solid var(--line);box-shadow:0 18px 40px rgba(20,16,40,.16)}
.ef-law-doc .tag{position:absolute;left:12px;top:-15px;background:var(--ink);color:#fff;font-size:15px;font-weight:800;padding:6px 12px;border-radius:4px;white-space:nowrap}
.ef-law-act{background:#fff;border-radius:16px;border-top:6px solid var(--ink);box-shadow:0 22px 50px rgba(20,16,40,.18);padding:24px 26px;font-family:'Noto Serif KR',serif}
.ef-law-act h4{margin:0 0 12px;font-size:21px;font-weight:900;font-family:inherit}
.ef-law-act p{margin:0 0 10px;font-size:16px;line-height:1.62;color:var(--ink);font-weight:500}
.ef-law-act p:last-child{margin:0}
.ef-law-act p b{font-weight:900}
.ef-law-who{display:flex;align-items:center;gap:18px;margin-top:auto}
.ef-law-who>span{width:64px;height:64px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-size:32px}
.ef-law-who b{display:block;font-size:28px;font-weight:900;letter-spacing:-.04em}
.ef-law-who small{display:block;font-size:19px;font-weight:700;color:var(--muted);margin-top:2px}
.ef-law-ops{margin:28px 0 0;display:flex;flex-direction:column;gap:18px}
.ef-law-key{background:#fff;border-left:8px solid var(--purple);border-radius:18px;box-shadow:0 14px 34px rgba(20,16,40,.10);padding:22px 30px;font-size:32px;font-weight:900;line-height:1.32;letter-spacing:-.045em}
.ef-law-key small{display:block;font-size:18px;font-weight:800;color:var(--purple-deep);margin-bottom:10px;letter-spacing:0}
.ef-law-pi{margin:24px 0 auto;padding-top:20px;border-top:1px solid #dcdae6}
.ef-law-pi small{display:block;font-size:18px;font-weight:800;color:var(--muted);margin-bottom:12px}
.ef-law-pi ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.ef-law-pi li{font-size:22px;font-weight:800;letter-spacing:-.03em;color:var(--ink);display:flex;gap:14px;align-items:baseline}
.ef-law-pi li i{font-style:normal;flex:0 0 52px;font-size:18px;font-weight:900;color:var(--purple-deep)}
.ef-law-etc{margin:28px 0 auto;padding-top:22px;border-top:1px solid #dcdae6;font-size:24px;font-weight:700;line-height:1.5;color:var(--ink);letter-spacing:-.03em}
.ef-law-etc small{display:block;font-size:18px;font-weight:800;color:var(--muted);margin-bottom:12px}
.ef-law-etc ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:12px}
.ef-mtab{display:flex;flex-direction:column;gap:14px;flex:1;min-height:0;margin-top:6px}
.ef-mh,.ef-mr{display:grid;grid-template-columns:400px 1fr 1fr;gap:36px;align-items:center}
.ef-mh{padding:0 36px;font-size:18px;font-weight:800;color:var(--muted);letter-spacing:.02em}
.ef-mr{background:#fff;border:1px solid var(--line);border-radius:22px;box-shadow:var(--shadow);padding:20px 36px;flex:1;min-height:0}
.ef-mr-who{display:flex;flex-direction:column;justify-content:center;gap:4px}
.ef-mr-who b,.ef-mr-who small{align-self:flex-start!important;margin:0!important;text-align:left}
.ef-mr-lg{grid-row:1 / span 2;height:92px;display:flex;align-items:center;justify-content:center}
.ef-mr-lg img{max-height:92px;max-width:150px;width:auto;height:auto;object-fit:contain}
.ef-mr-who b{font-size:28px;font-weight:900;letter-spacing:-.04em;align-self:end}
.ef-mr-who small{font-size:17px;font-weight:700;color:var(--muted);align-self:start;margin-top:2px}
.ef-mr-adv{font-size:19px;font-weight:700;line-height:1.5;color:var(--ink);letter-spacing:-.02em}
.ef-mr-work{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.ef-mr-work li{position:relative;padding-left:22px;font-size:18px;font-weight:700;line-height:1.45;letter-spacing:-.02em}
.ef-mr-work li::before{content:'→';position:absolute;left:0;color:var(--purple);font-weight:900}
.ef-mr-work b{color:var(--purple)}
.ef-mr.todo{background:transparent;border-style:dashed;box-shadow:none}
.ef-mr.todo .ef-mr-who b{color:var(--ink)}
.ef-mr.todo .ef-mr-adv,.ef-mr.todo .ef-mr-work li{color:var(--muted)}
.ef-mentors{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.ef-m{background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:34px 34px 30px;text-align:center}
.ef-m .ef-lg{height:64px;display:flex;align-items:center;justify-content:center;margin-bottom:22px}
.ef-m .ef-lg img{height:46px;width:auto;max-width:240px;object-fit:contain}
.ef-m b{display:block;font-size:32px;font-weight:900;letter-spacing:-.045em}
.ef-m span{display:block;margin-top:8px;font-size:22px;font-weight:800;color:var(--ink)}
.ef-m small{display:block;margin-top:10px;font-size:18px;font-weight:700;color:var(--muted)}
.ef-ceo{display:grid;grid-template-columns:330px 1fr;gap:30px;align-items:center;margin-top:30px;flex:1;min-height:0}
.ef-ceo-k{font-size:30px;font-weight:800;letter-spacing:-.04em;line-height:1.35}
.ef-ceo-k b{color:var(--purple);font-weight:900}
.ef-ceo-k small{display:block;margin-top:12px;font-size:19px;font-weight:700;color:var(--muted)}
.ef-ceo .ef-shot{padding:14px}
.ef-field{display:grid;grid-template-columns:1.35fr 1fr;gap:44px;flex:1;min-height:0;align-items:start}
.ef-fcol{display:flex;flex-direction:column;gap:18px;min-height:0}
.ef-fcol .ef-shot{padding:14px}
.ef-cap{font-size:28px;font-weight:900;letter-spacing:-.04em;color:var(--ink);text-align:center}
.ef-cap small{display:block;margin-top:6px;font-size:20px;font-weight:700;color:var(--muted)}
.ef-quote{margin-top:10px;background:var(--purple-pale);border-radius:22px;padding:28px 34px;font-size:32px;font-weight:900;letter-spacing:-.045em;color:var(--purple-deep);text-align:center}
.ef-quote small{display:block;margin-top:10px;font-size:20px;font-weight:700;color:var(--muted)}
.ef-num .ef-tag{font-style:normal;margin-left:12px;color:var(--purple-deep);font-size:22px;font-weight:900;letter-spacing:-.02em}
.ef-num .ef-tag:before{content:'('}
.ef-num .ef-tag:after{content:')'}
/* 차별점 — 개발자 기술면접 전용 지형 + 비교표, 2장 (사용자 지시 2026-11-07) */
.df-land{display:grid;grid-template-columns:1.35fr 1fr;gap:28px;flex:1;min-height:0;margin-top:8px}
.df-g{background:#fff;border:1px solid var(--line);border-radius:26px;padding:40px 44px;box-shadow:var(--shadow);display:flex;flex-direction:column;justify-content:center;gap:30px}
.df-g.dev{background:var(--purple-pale);border-color:transparent}
.df-gh{display:flex;flex-direction:column;gap:6px}
.df-gh b{font-size:30px;font-weight:900;letter-spacing:-.04em;color:var(--muted)}
.df-g.dev .df-gh b{color:var(--purple-deep)}
.df-gh em{font-style:normal;font-size:140px;font-weight:900;letter-spacing:-.06em;color:#c9c4d0;line-height:1}
.df-gh em i{font-style:normal;font-size:52px;margin-left:6px;letter-spacing:-.03em}
.df-gh small{font-size:22px;font-weight:800;color:var(--muted)}
.df-sq{display:flex;gap:10px}
.df-sq span{width:44px;height:44px;border-radius:12px;background:#d9d5df}
.df-sq span.off{background:transparent;border:2px dashed #c9c4d0}
.df-g.dev .df-sq span{background:#b9b0f5}
.df-g.dev .df-sq span.kr{background:var(--purple)}
.df-g.dev .df-gh em{color:var(--purple)}
.df-base{font-size:26px;line-height:1.45;font-weight:800;letter-spacing:-.03em;color:var(--ink)}
.df-base span{color:var(--muted);font-weight:700;margin-right:10px}
.df-chips{font-size:26px;font-weight:800;line-height:1.55;color:#6b6575;letter-spacing:-.03em;border-top:1px solid var(--line);padding-top:22px}
.df-chips span:not(:last-child):after{content:' ·';color:#bdb7c4;display:inline-block;white-space:pre;text-decoration:none}
.df-g.dev .df-chips{color:var(--purple-deep)}
.df-chips span.off{text-decoration:line-through;color:#a9a3b0}
.df-chips span{white-space:nowrap}
.df-g.dev .df-chips{font-size:24px}
.df-g.dev .df-sq span{width:36px;height:36px;border-radius:10px}
.df-me{margin-top:24px;background:var(--purple);color:#fff;border-radius:22px;padding:24px 36px;font-size:28px;font-weight:900;letter-spacing:-.04em;display:flex;align-items:center;gap:22px}
.df-me small{font-size:20px;font-weight:800;color:#ddd8ff;padding-left:22px;border-left:2px solid rgba(255,255,255,.35)}
.df-wrap{display:flex;flex-direction:column;flex:1;min-height:0;justify-content:center}
.df-t{width:100%;border-collapse:separate;border-spacing:0 14px;table-layout:fixed}
.df-t th{font-size:22px;font-weight:900;color:var(--muted);padding:0 16px 2px;text-align:center;letter-spacing:-.02em}
.df-t th:first-child{text-align:left;width:280px}
.df-t td{background:#fff;padding:26px 16px;font-size:25px;font-weight:800;letter-spacing:-.03em;text-align:center;border-top:1px solid var(--line);border-bottom:1px solid var(--line);line-height:1.3;color:var(--ink)}
.df-t td:first-child{text-align:left;border-left:1px solid var(--line);border-radius:18px 0 0 18px;font-size:27px;font-weight:900}
.df-t td:first-child small{display:block;font-size:16px;font-weight:700;color:var(--muted)}
.df-t td:last-child{border-right:1px solid var(--line);border-radius:0 18px 18px 0}
.df-t td.n{color:#b8b2bf;font-weight:700}
.df-t tr.me td{background:var(--purple);color:#fff;border-color:transparent}
.df-t tr.me td small{color:#ddd8ff}
.dc-wrap{display:flex;flex-direction:column;flex:1;min-height:0;justify-content:center;gap:12px}
.dc-box{background:#f3f2f8;border-radius:30px;padding:20px}
.dc-t{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed;background:#fff;border-radius:20px;overflow:hidden}
.dc-t th{background:#eeecfb;font-size:20px;font-weight:800;color:#6b6575;padding:16px 10px;text-align:center;letter-spacing:-.02em}
.dc-t th:first-child{text-align:left;padding-left:30px;width:470px}
.dc-t th.me{color:var(--purple-deep);font-weight:900}
.dc-t td{font-size:28px;font-weight:900;text-align:center;padding:13px 10px;line-height:1.15;border-top:1px solid #ecebf1;letter-spacing:-.03em}
.dc-t td:first-child{text-align:left;padding-left:30px;line-height:1.4;font-size:24px;font-weight:900;color:var(--ink)}
.dc-t td.y{color:#1f9d55}
.dc-t td.p{color:#c27c0e}
.dc-t td.x{color:#b8b2bf;font-weight:700}
.dc-t td.me{background:#f7f5ff}
.dc-t td.x.me{color:#8f8899}
.df-leg{font-size:17px;font-weight:700;color:var(--muted);text-align:right;margin-top:6px}
/* 11-10 추가 — 마케팅 · 유저 · B2B */
.ef-mk{display:grid;grid-template-columns:1.25fr .75fr;gap:48px;width:100%;flex:1;min-height:0;align-items:center}
.ef-mk-list{display:flex;flex-direction:column;gap:14px}
.ef-mk-row{display:grid;grid-template-columns:120px 300px 1fr;align-items:center;gap:22px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 26px;box-shadow:0 6px 18px rgba(25,20,40,.04)}
.ef-mk-row .k{font-size:26px;font-weight:900;color:var(--purple);letter-spacing:-.04em}
.ef-mk-row b{font-size:32px;font-weight:900;color:var(--ink);letter-spacing:-.045em;line-height:1.2}
.ef-mk-row span{font-size:20px;font-weight:700;color:var(--muted);line-height:1.45;letter-spacing:-.03em;word-break:keep-all}
.ef-mk-ph{position:relative;height:640px}
.ef-mk-ph figure{position:absolute;margin:0;background:#fff;padding:10px;border-radius:10px;box-shadow:0 18px 40px rgba(20,16,40,.16)}
.ef-mk-ph figure img{display:block;width:100%;height:auto;border-radius:4px}
.ef-mk-ph figcaption{font-size:16px;font-weight:800;color:var(--muted);margin-top:8px;letter-spacing:-.02em}
.ef-mk-ph .a{left:0;top:10px;width:96%;transform:rotate(-1.2deg);z-index:1}
.ef-mk-ph .b{right:0;bottom:0;width:46%;transform:rotate(2deg);z-index:2}
.ef-us{display:grid;grid-template-columns:1.1fr .9fr;gap:80px;width:100%;align-items:center;padding:0 30px}
.ef-us-h{font-size:26px;font-weight:900;color:var(--muted);letter-spacing:-.03em;margin-bottom:22px}
.ef-bar{display:grid;grid-template-columns:230px 1fr 70px;align-items:center;gap:18px;margin-bottom:16px}
.ef-bar span{font-size:28px;font-weight:900;color:var(--ink);letter-spacing:-.04em}
.ef-bar i{display:block;height:34px;border-radius:6px;background:#c9c2f7}
.ef-bar i.top{background:var(--purple)}
.ef-bar b{font-size:28px;font-weight:900;color:var(--ink);text-align:right}
.ef-us-meta{margin-top:26px;font-size:20px;font-weight:700;color:var(--muted);line-height:1.6;letter-spacing:-.03em}
.ef-us-meta b{color:var(--ink);font-weight:900}
.ef-us-r{display:flex;flex-direction:column;gap:46px}
.ef-us-r .ef-num b{font-size:150px}
.ef-vs{width:100%;border-collapse:collapse;font-size:19px}
.ef-vs th{text-align:left;font-size:22px;font-weight:900;padding:0 12px 10px;color:var(--purple-deep)}
.ef-vs th.b{color:#005ce6}
.ef-vs td{padding:10px 12px;border-top:1px solid #e6e4ee;font-weight:700;color:var(--ink);text-align:left;word-break:keep-all}
.ef-vs td:first-child{color:var(--muted);font-weight:800;width:120px}
.ef-vs td.b{background:#eef4ff;font-weight:800}
.ef-leak{background:var(--ink);color:#fff;border-radius:20px;padding:20px 26px;text-align:left}
.ef-leak h4{margin:0 0 10px;font-size:24px;font-weight:900;color:#a9c8ff}
.ef-leak ol{margin:0;padding-left:22px;font-size:18px;font-weight:700;line-height:1.6}
.ef-leak b{color:#fff;font-weight:900}
.ef-entm{flex:1;min-height:0;display:grid;gap:18px 22px;align-content:center;justify-content:center}
.ef-entm.c2{grid-template-columns:repeat(2,500px)}
.ef-entm.c3{grid-template-columns:repeat(3,500px)}
.ef-entm.c1{grid-template-columns:repeat(2,820px)}
.ef-entm figure{margin:0;text-align:center}
.ef-entm img{display:block;width:100%;height:auto;border-radius:10px;border:1px solid var(--line);box-shadow:0 10px 28px rgba(28,20,48,.10)}
.ef-entm figcaption{margin-top:6px;font-size:14px;font-weight:700;color:var(--muted)}
.ef-ent{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;width:100%;flex:1;min-height:0;align-items:center}
.ef-ent-l{display:flex;flex-direction:column;gap:22px}
.ef-ent-box{border-radius:20px;padding:24px 28px;background:#f3f2f8;text-align:left}
.ef-ent-box *{text-align:left!important;word-spacing:normal;letter-spacing:-.03em}
.ef-ent-box ol li{display:block}
.ef-ent-box.cd{background:var(--purple-pale)}
.ef-ent-box h4{margin:0 0 12px;font-size:26px;font-weight:900;letter-spacing:-.04em;color:var(--ink)}
.ef-ent-box.cd h4{color:var(--purple-deep)}
.ef-ent-box ol,.ef-ent-box p{margin:0;padding-left:0;list-style:none;font-size:20px;font-weight:700;line-height:1.65;color:var(--ink);letter-spacing:-.03em;word-break:keep-all}
.ef-ent-box ol li:before{content:counter(li);counter-increment:li;display:inline-block;width:28px;height:28px;line-height:28px;text-align:center;border-radius:6px;background:var(--purple);color:#fff;font-size:15px;font-weight:900;margin-right:10px;vertical-align:2px}
.ef-ent-box ol{counter-reset:li}
.ef-ent-plus{text-align:center;font-size:40px;font-weight:900;color:var(--purple);line-height:1;margin:-8px 0}
.ef-ent-guide{display:flex;align-items:center;gap:16px;color:var(--muted);font-size:18px;font-weight:700;text-decoration:none;align-self:flex-start}
.ef-ent-guide img{width:96px;height:96px;display:block}
.ef-ent-guide span{white-space:nowrap}
.ef-ent-r{position:relative;height:600px}
.ef-ent-r .ef-shot{position:absolute;padding:0;border-radius:18px}
.ef-ent-r .s1{left:0;top:0;width:86%;z-index:1}
.ef-ent-r .s2{right:0;bottom:0;width:62%;z-index:2;box-shadow:0 24px 60px rgba(20,16,40,.22)}
.ef-state{margin-top:14px;text-align:center;font-size:24px;font-weight:800;color:var(--muted);letter-spacing:-.03em}
.ef-state b{color:var(--ink);font-weight:900}


/* Marketing: verified source snapshots, 2026-11-11 */
@font-face{font-family:Pretendard;src:url('assets/mkt-Pretendard-Regular.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:Pretendard;src:url('assets/mkt-Pretendard-Bold.woff2') format('woff2');font-weight:700;font-display:swap}
@font-face{font-family:Pretendard;src:url('assets/mkt-Pretendard-Black.woff2') format('woff2');font-weight:900;font-display:swap}
.ef-mkt{flex:1;min-height:0;display:flex;flex-direction:column;gap:22px}
.ef-mkt *{letter-spacing:-.025em;word-break:keep-all}
.ef-mkt-period{font-size:20px;font-weight:700;color:var(--muted);margin:0}
.ef-mkt-foot{font-size:20px;line-height:1.5;color:var(--muted);margin-top:auto;font-weight:700}
.ef-mkt-layout{display:grid;grid-template-columns:1.9fr 1fr;gap:34px;flex:1;min-height:0;align-items:stretch}
.ef-mkt-channels{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-content:stretch}
.ef-mkt-channel{background:white;padding:28px 30px;border:1px solid var(--line);border-radius:16px}
.ef-mkt-channel .tag{color:var(--purple);font-size:25px;font-weight:900;margin-bottom:18px}
.ef-mkt-channel h3{font-size:35px;line-height:1.2;margin:0 0 18px;font-weight:900}
.ef-mkt-channel p{font-size:24px;line-height:1.5;color:var(--muted);margin:0;font-weight:700}
.ef-mkt-channel small{display:block;font-size:19px;line-height:1.5;color:var(--muted);margin-top:18px}
.ef-mkt-photo{display:flex;flex-direction:column;gap:16px;min-height:0}
.ef-mkt-photo img{width:100%;object-fit:cover;border-radius:12px}
.ef-mkt-photo .fair{height:330px}
.ef-mkt-photo .goods{height:220px;object-position:center 58%}
.ef-mkt-photo span{font-size:20px;font-weight:700;color:var(--muted)}
.ef-mkt-ads{display:grid;grid-template-columns:1fr 1fr;gap:30px;flex:1}
.ef-mkt-ad{border-radius:20px;background:white;border:1px solid var(--line);padding:30px 38px;display:flex;flex-direction:column;gap:18px}
.ef-mkt-ad h3{font-size:36px;margin:0;font-weight:900}
.ef-mkt-ad .spend{display:flex;justify-content:space-between;font-size:25px;color:var(--muted);font-weight:700}
.ef-mkt-ad .spend b{color:var(--ink)}
.ef-mkt-ad .click{font-size:102px;font-weight:900;line-height:1.05;color:var(--purple);letter-spacing:-.055em}
.ef-mkt-ad .click small{font-size:27px;letter-spacing:-.03em;margin-left:14px;color:var(--muted)}
.ef-mkt-ad .metrics{display:grid;grid-template-columns:1.15fr 1fr .75fr;gap:18px;padding:16px 0 20px;border-bottom:1px solid var(--line)}
.ef-mkt-ad .metrics b{font-size:35px;display:block;line-height:1.2}
.ef-mkt-ad .metrics span{font-size:20px;font-weight:700;color:var(--muted);display:block;margin-bottom:10px}
.ef-mkt-ad .engage{display:flex;justify-content:space-between;align-items:center;gap:16px}
.ef-mkt-ad .engage span{font-size:21px;font-weight:700;line-height:1.5;color:var(--muted)}
.ef-mkt-ad .engage b{font-size:42px;white-space:nowrap;color:var(--purple-deep)}
.ef-mkt-ad .engage small{font-size:18px;color:var(--muted);display:block;text-align:right;margin-top:5px}
.ef-mkt-ad.google .click{color:var(--ink)}
.ef-mkt-plots{display:flex;flex-direction:column;gap:18px}
.ef-mkt-plot{padding:20px 22px 4px;background:white;border:1px solid var(--line);border-radius:16px;min-height:0}
.ef-mkt-plot h3{font-size:25px;margin:0 0 0 16px;font-weight:900;display:flex;justify-content:space-between;align-items:baseline}
.ef-mkt-plot h3 span{font-size:18px;color:var(--muted);font-weight:700}
.ef-mkt-plot img{width:100%;height:235px;object-fit:contain}
.ef-mkt-stats{display:flex;flex-direction:column;gap:22px}
.ef-mkt-stat{background:var(--purple-pale);border-radius:18px;padding:30px 32px;flex:1;display:flex;flex-direction:column;justify-content:center}
.ef-mkt-stat.dark{background:#eeecf2}
.ef-mkt-stat .number{font-size:96px;line-height:1.05;font-weight:900;color:var(--purple-deep);letter-spacing:-.06em}
.ef-mkt-stat.dark .number{color:var(--ink)}
.ef-mkt-stat .number small{font-size:29px;letter-spacing:-.02em;margin-left:7px}
.ef-mkt-stat h3{font-size:28px;margin:16px 0 8px;font-weight:900}
.ef-mkt-stat p{font-size:20px;line-height:1.5;margin:0;color:var(--muted);font-weight:700}
.ef-mkt-guestplot{display:flex;flex-direction:column;justify-content:center;padding:24px 26px;background:white;border:1px solid var(--line);border-radius:20px}
.ef-mkt-guestplot h3{font-size:30px;margin:0 0 28px 12px;font-weight:900}
.ef-mkt-guestplot img{width:100%;height:440px;object-fit:contain}
.ef-mkt-usage{display:grid;grid-template-columns:1.7fr 1fr;gap:45px;flex:1;align-items:stretch}
.ef-mkt-usage .chart{background:white;border:1px solid var(--line);border-radius:20px;padding:34px 38px}
.ef-mkt-usage .chart h3{font-size:30px;margin:0 0 30px;font-weight:900}
.ef-mkt-bar{display:grid;grid-template-columns:170px 1fr 140px;gap:18px;align-items:center;margin:26px 0}
.ef-mkt-bar>span{font-size:28px;font-weight:900}
.ef-mkt-bar .track{height:34px;background:#efedf6;border-radius:5px;overflow:hidden}
.ef-mkt-bar .fill{height:100%;background:var(--purple)}
.ef-mkt-bar strong{font-size:30px;text-align:right;font-weight:900}
.ef-mkt-bar strong small{font-size:20px;color:var(--muted);margin-left:6px}
.ef-mkt-focus{display:flex;flex-direction:column;justify-content:center;gap:26px}
.ef-mkt-focus .big{font-size:100px;font-weight:900;line-height:1;color:var(--purple);letter-spacing:-.06em}
.ef-mkt-focus .big small{font-size:34px;margin-left:10px}
.ef-mkt-focus h3{font-size:34px;font-weight:900;line-height:1.35;margin:0}
.ef-mkt-focus p{font-size:24px;line-height:1.6;margin:0;font-weight:700;color:var(--muted)}
.ef-mkt-next{padding:22px 24px;background:var(--purple-pale);border-left:5px solid var(--purple);font-size:23px;font-weight:700;line-height:1.55}
.ef-mkt-next b{display:block;color:var(--purple-deep);margin-bottom:6px}

"""

























# MARKETING_REVISION_CSS_BEGIN
CSS += '\n/* marketing revision: evidence and product metrics */\n.ef-mr-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;flex:1;min-height:0}\n.ef-mr-grid.wide{grid-template-columns:1.7fr 1fr}\n.ef-mr-card{background:white;border:1px solid var(--line);border-radius:18px;padding:30px 34px;min-height:0}\n.ef-mr-card h3{font-size:32px;margin:0 0 18px;line-height:1.3;font-weight:900}\n.ef-mr-card p{font-size:25px;line-height:1.55;margin:14px 0;color:var(--muted);font-weight:700}\n.ef-mr-card .label{color:var(--purple);font-size:23px;font-weight:900;margin-bottom:18px}\n.ef-mr-number{font-size:102px;line-height:1.1;font-weight:900;color:var(--purple-deep);letter-spacing:-.055em}\n.ef-mr-number small{font-size:30px;margin-left:10px;letter-spacing:-.02em}\n.ef-mr-card .sub{font-size:20px;color:var(--muted);line-height:1.55;margin-top:15px}\n.ef-mr-card .rule{border-top:1px solid var(--line);padding-top:22px;margin-top:23px}\n.ef-mr-pair{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:26px 0}\n.ef-mr-pair b{font-size:39px;display:block;margin-top:8px;color:var(--ink)}\n.ef-mr-pair span{font-size:22px;color:var(--muted);font-weight:700}\n.ef-mr-highlight{padding:20px 24px;background:var(--purple-pale);border-left:5px solid var(--purple);font-size:25px;font-weight:800;line-height:1.5;margin-top:20px}\n.ef-mr-chart{width:100%;height:540px;object-fit:contain;display:block}\n.ef-mr-chart.accounts{height:580px}\n.ef-mr-aside{display:flex;flex-direction:column;gap:22px}\n.ef-mr-aside .ef-mr-card{flex:1;display:flex;flex-direction:column;justify-content:center}\n.ef-mr-bars{display:flex;flex-direction:column;gap:25px;margin-top:28px}\n.ef-mr-bar{display:grid;grid-template-columns:160px 1fr 150px;align-items:center;gap:16px;font-size:25px;font-weight:800}\n.ef-mr-track{height:34px;background:#efedf6;border-radius:4px;overflow:hidden}\n.ef-mr-fill{height:100%;background:var(--purple)}\n.ef-mr-bar b{text-align:right;font-size:27px}\n.ef-mr-strip{display:flex;height:62px;border-radius:6px;overflow:hidden;margin:22px 0 30px;color:white;font-size:26px;font-weight:900}\n.ef-mr-strip div{display:flex;align-items:center;justify-content:center}\n.ef-mr-three{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;flex:1}\n.ef-mr-three .ef-mr-number{font-size:88px}\n.ef-mr-three .ef-mr-card{display:flex;flex-direction:column}\n.ef-mr-three .ef-mr-card .rule{margin-top:auto}\n.ef-mr-table{width:100%;border-collapse:collapse;font-size:24px}\n.ef-mr-table td,.ef-mr-table th{text-align:left;padding:17px 8px;border-bottom:1px solid var(--line)}\n.ef-mr-table th{font-size:21px;color:var(--muted)}\n.ef-mr-table td:last-child{text-align:right;font-weight:900;color:var(--purple-deep)}\n/* Presentation copy: secondary explanations are retained in speaker notes. */\n.ef-marketing-slide .folio{display:none}\n.ef-marketing-slide .ef-mkt-photo{gap:20px;justify-content:flex-start}\n.ef-marketing-slide .ef-mkt-photo .goods{height:390px;object-fit:contain;object-position:center;background:#eeecf2}\n.ef-marketing-slide .ef-mkt-photo .fair{height:330px;object-fit:contain;background:#eeecf2}\n.ef-marketing-slide .ef-mr-card p,.ef-marketing-slide .ef-mkt-channel p{color:var(--ink)}\n.ef-cash-head{font-size:80px;font-weight:900;color:var(--purple-deep);letter-spacing:-.045em;margin:22px 0 34px}\n.ef-cash-head span{color:#aba3bd;font-size:60px;margin:0 12px}\n.ef-cash-compare{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:20px 0 35px}\n.ef-cash-compare h3{font-size:27px}\n.ef-cash-track{height:40px;background:#eeecf3;border-radius:4px;margin-bottom:20px}\n.ef-cash-track>div{height:100%;background:var(--purple);border-radius:4px}\n.ef-cash-compare b{font-size:42px;font-weight:900}\n.ef-cash-compare p{font-size:22px;line-height:1.5}\n.ef-cash-table{width:100%;border-collapse:collapse;margin-top:30px;font-size:26px}\n.ef-cash-table td,.ef-cash-table th{padding:21px 12px;text-align:right;border-bottom:1px solid var(--line)}\n.ef-cash-table td:first-child,.ef-cash-table th:first-child{text-align:left}\n.ef-cash-table th{font-size:24px}\n.ef-cash-table td:last-child{font-weight:900;color:var(--purple-deep)}\n.ef-cash-table .accent{background:var(--purple-pale);font-weight:900}\n.ef-perf-chart{width:100%;height:420px;object-fit:contain;display:block;margin:8px 0}\n.ef-perf-table{width:100%;border-collapse:collapse;font-size:24px;margin:26px 0}\n.ef-perf-table td,.ef-perf-table th{padding:20px 9px;border-bottom:1px solid var(--line);text-align:right}\n.ef-perf-table td:first-child,.ef-perf-table th:first-child{text-align:left}\n.ef-perf-table td:last-child{font-weight:900;color:var(--purple-deep)}\n.ef-perf-table th{font-size:23px}\n.ef-perf-note{font-size:23px;line-height:1.6;color:var(--ink);font-weight:700;margin-top:20px}\n.ef-performance-kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:25px}\n.ef-performance-kpis .ef-mr-card{padding:25px 30px}\n.ef-performance-kpis .metric{font-size:56px;font-weight:900;color:var(--purple-deep);line-height:1.25;letter-spacing:-.04em}\n.ef-performance-kpis .metric small{font-size:29px}\n.ef-performance-kpis .flow{font-size:27px;font-weight:800;margin-top:18px;color:var(--ink)}\n.ef-performance-kpis .change{font-size:25px;color:var(--purple-deep);font-weight:900;margin-top:14px}\n.ef-performance-summary{display:grid;grid-template-columns:1.6fr 1fr;gap:26px;flex:1}\n.ef-performance-summary .ef-mr-card{padding:25px 30px}\n\n.ef-ad-period{font-size:23px;font-weight:700;color:var(--ink);margin:0;line-height:1.4}\n.ef-ad-chart{width:100%;height:335px;object-fit:contain;display:block}\n.ef-ad-observations{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}\n.ef-ad-observation{border:1px solid var(--line);background:white;border-radius:14px;padding:23px 27px}\n.ef-ad-observation .label{font-size:23px;font-weight:900;color:var(--purple);margin-bottom:13px}\n.ef-ad-observation h3{font-size:29px;line-height:1.35;margin:0 0 12px;font-weight:900}\n.ef-ad-observation p{font-size:23px;line-height:1.5;margin:0;font-weight:700}\n.ef-ad-observation b{color:var(--purple-deep)}\n.ef-ad-ai{display:grid;grid-template-columns:0.9fr 1.6fr;gap:28px;flex:1;min-height:0}\n.ef-ad-ai .ef-mr-number{font-size:83px}\n.ef-ad-table{font-size:25px;width:100%;border-collapse:collapse;margin-top:15px}\n.ef-ad-table th,.ef-ad-table td{padding:16px 10px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}\n.ef-ad-table th{font-size:21px;font-weight:800}\n.ef-ad-table th:first-child,.ef-ad-table td:first-child{text-align:left}\n.ef-ad-table tr.selected{background:var(--purple-pale);color:var(--purple-deep);font-weight:900}\n.ef-ad-ai .ef-mr-highlight{font-size:25px;margin-top:28px}\n.ef-ad-region{display:grid;grid-template-columns:1fr 1.35fr;gap:28px;flex:1;min-height:0}\n.ef-ad-region .ef-mr-bar{grid-template-columns:150px 1fr 150px;margin:18px 0;font-size:25px}\n.ef-ad-region .ef-mr-bars{gap:25px;margin:35px 0}\n.ef-ad-region .ef-mr-track{height:40px}\n.ef-ad-region .ef-mr-number{font-size:94px;margin:25px 0 16px}\n.ef-feature-top{display:grid;grid-template-columns:1fr 1fr;gap:25px}\n.ef-feature-bottom{display:grid;grid-template-columns:repeat(3,1fr);gap:25px;flex:1}\n.ef-feature-card{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px}\n.ef-feature-card h3{font-size:29px;margin:0 0 14px;font-weight:900;line-height:1.4}\n.ef-feature-card p{font-size:23px;font-weight:700;margin:12px 0 0;line-height:1.5}\n.ef-feature-number{font-size:85px;line-height:1.1;font-weight:900;color:var(--purple-deep);letter-spacing:-.05em}\n.ef-feature-number small{font-size:28px;margin-left:10px}\n.ef-feature-top .ef-feature-card{display:grid;grid-template-columns:1.2fr 1fr;align-items:center;gap:20px;min-height:240px}\n.ef-feature-top .ef-feature-number{text-align:right;font-size:96px}\n.ef-feature-bottom .ef-feature-card{display:flex;flex-direction:column;justify-content:center;background:linear-gradient(180deg,#fff 25%,#f6f4ff 100%)}\n.ef-feature-bottom .ef-feature-number{margin:18px 0;font-size:96px}\n.ef-plan-grid{display:grid;grid-template-columns:1.12fr 1fr;gap:28px;flex:1;min-height:0}\n.ef-plan-creative{background:#30264e;border-radius:18px;padding:35px 38px;color:white;display:flex;flex-direction:column}\n.ef-plan-creative .label{font-size:24px;font-weight:800;color:#d8cdff;margin-bottom:23px}\n.ef-plan-creative h3{font-size:44px;line-height:1.3;margin:0 0 25px;font-weight:900}\n.ef-plan-scenes{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:10px 0 30px}\n.ef-plan-scene{border:1px solid #70638e;border-radius:10px;background:#40345e;padding:24px 23px;min-height:145px}\n.ef-plan-scene b{font-size:26px;display:block;margin-bottom:14px}\n.ef-plan-scene span{font-size:24px;line-height:1.5;display:block}\n.ef-plan-cta{font-size:28px;font-weight:900;color:#33264f;background:#e7ddff;border-radius:8px;padding:22px 25px;margin-top:auto;text-align:center}\n.ef-plan-measure{display:grid;grid-template-rows:1fr 1fr;gap:24px;min-height:0}\n.ef-plan-measure .ef-mr-card{flex:1;padding:29px 32px}\n.ef-plan-measure h3{font-size:31px}\n.ef-plan-measure .ef-mr-highlight{font-size:25px;margin-top:15px}\n.ef-mock-current{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px;display:flex;flex-direction:column}\n.ef-mock-current .label,.ef-mock-value .label,.ef-mock-next .label{font-size:23px;font-weight:900;color:var(--purple);margin-bottom:20px}\n.ef-mock-kpis{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin:12px 0 8px;flex:1}\n.ef-mock-kpi{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:24px;padding-right:28px;border-right:1px solid var(--line)}\n.ef-mock-kpi:last-child{border:0;padding-right:0}\n.ef-mock-kpi h3{font-size:29px;line-height:1.4;margin:0;font-weight:900}\n.ef-mock-kpi p{font-size:25px;line-height:1.4;margin:0;font-weight:700}\n.ef-mock-kpi .number{font-size:118px;line-height:1;font-weight:900;white-space:nowrap;color:var(--purple-deep);letter-spacing:-.05em}\n.ef-mock-kpi .number small{font-size:26px;letter-spacing:-.02em;margin-left:10px}\n.ef-mock-direction{display:grid;grid-template-columns:1fr 1.2fr;gap:28px;flex:1;min-height:0}\n.ef-mock-value{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px;color:var(--ink)}\n.ef-mock-value .label{color:var(--purple);margin-bottom:16px}\n.ef-mock-core-body{display:grid;grid-template-columns:1fr 1.2fr;gap:45px;align-items:center}\n.ef-mock-value h3{font-size:36px;line-height:1.3;font-weight:900;margin:0}\n.ef-mock-value p{font-size:24px;line-height:1.5;font-weight:700;margin:0}\n.ef-mock-value .emphasis{font-size:23px;line-height:1.5;font-weight:800;color:var(--purple-deep);margin-top:12px}\n.ef-mock-next{background:white;border:1px solid var(--line);border-radius:16px;padding:30px 34px;display:flex;flex-direction:column}\n.ef-mock-next h3{font-size:40px;line-height:1.35;font-weight:900;margin:8px 0 22px}\n.ef-mock-next p{font-size:25px;line-height:1.6;font-weight:700;margin:0 0 24px}\n.ef-mock-goal{font-size:28px;font-weight:900;line-height:1.4;background:var(--purple-pale);color:var(--purple-deep);border-left:5px solid var(--purple);padding:22px 24px;margin-top:auto}\n'
# MARKETING_REVISION_CSS_END

# ================= 4. Effect =================
S.append(divider('04 · Effect', 'Effect', '6개월 수행 내용, 운영 지표, 비즈니스 모델, 비전'))
S.note('''[구분] Effect — 6개월 동안 무엇을 했고, 무엇이 남았는지.''')


# ---------- 마케팅: 2026-11-11 검증 집계, Effect 시작부 ----------
S.append(shell('Effect', '검색 · 광고 · SNS · 현장을 통한 <span class="purple">사용자 유입</span>', '''
<div class="ef-mkt">
 <div class="ef-mkt-layout">
  <div class="ef-mkt-channels">
   <div class="ef-mkt-channel"><div class="tag">검색 콘텐츠</div><h3>CS 문서 172편<br>면접 질문 875문항</h3><p>직군 가이드 12종과 함께<br>학습 콘텐츠에서 서비스로 연결</p></div>
   <div class="ef-mkt-channel"><div class="tag">유료 광고</div><h3>Meta · Google Ads</h3><p>채널별 캠페인 집행<br>클릭 비용과 참여 지표 비교</p></div>
   <div class="ef-mkt-channel"><div class="tag">SNS</div><h3>Threads · Instagram</h3><p>서비스 소개 콘텐츠 게시<br>UTM으로 유입 경로 구분</p></div>
   <div class="ef-mkt-channel"><div class="tag">현장 홍보</div><h3>숭실대 취업 박람회</h3><p>서비스 소개 팜플렛과<br>QR 클리커 굿즈 배포</p></div>
  </div>
  <div class="ef-mkt-photo"><img class="fair" src="assets/ef-fair.jpg" alt="숭실대 취업 박람회 DevFit 소개 현장"><img class="goods" src="assets/ef-goods.jpg" alt="DevFit 팜플렛과 QR 클리커 굿즈"></div>
 </div>
</div>''', cls='ef-marketing-slide', source='Dozer, 「DevFit 최종보고서 마케팅」, 2026. Microsoft Clarity, 「CS 지식백과 진입 집계」, 2026. Meta·Google Ads, 「캠페인 내보내기」, 2026.'))
S.note('''[약 25초] 마케팅은 검색 콘텐츠, 유료 광고, SNS, 현장 홍보로 나눠 실행했습니다. CS 문서와 면접 질문에서 서비스를 접할 수 있게 했고, Meta와 Google 광고를 집행했습니다. SNS는 게시물별 유입 경로를 구분했고, 숭실대 취업 박람회에서는 팜플렛과 QR 굿즈로 직접 소개했습니다.

근거: final-report의 기존 마케팅 장표와 사진 원본. 콘텐츠 규모 172편·875문항·가이드 12종은 원본 보고서 기준. CS 진입 169세션은 cs_acquisition_summary.json, 2026-08-12~11-09 04:39 KST. 직접·내부·광고 등 모든 진입 포함이며 검색 성과로 주장하지 않음. 검색결과 referrer 확인 세션은 3건(네이버 Search Advisor 1건 제외). 박람회 날짜·배포량·가입 효과는 미확인.
광고비 3,501,256원=Meta 2,338,208+Google 1,163,048. 11/05 검증 CSV 기준이며 실제 카드 결제액·VAT 포함 청구액과 다름. 11/04 부록 A5의 광고비와 집계 시점이 다름.
기존 콜백 메일은 구축 근거만 있고 실제 발송·복귀 성과가 확인되지 않아 수행 실적 목록에 포함하지 않음.''')


S.append(shell('Effect', 'Meta 중심 집행, <span class="purple">유입 비용과 참여를 함께 고려</span>', '\n<div class="ef-mkt"><p class="ef-mkt-period">11/05 누적 집행 · Meta 233.8만 원 / Google 116.3만 원</p>\n<div class="ef-mr-strip"><div style="width:66.78%;background:#6c5ce7">Meta 66.8%</div><div style="width:33.22%;background:#3d354f">Google 33.2%</div></div>\n<div class="ef-mr-grid">\n <div class="ef-mr-card"><div class="label">Meta에 더 많은 비중을 둔 근거</div><h3>낮은 클릭 비용으로<br>서비스 유입 규모 확보</h3><div class="ef-mr-pair"><div><span>링크 클릭당 비용</span><b>110원</b></div><div><span>링크 클릭</span><b>21,318회</b></div></div><p>소재를 바꾸며 반응을 탐색하고<br>적은 단가로 넓은 접점 확보</p></div>\n <div class="ef-mr-card"><div class="label">Google에도 예산을 유지한 근거</div><h3>검색 의도가 있는 유입과<br>서비스 이용 가능성 확인</h3><div class="ef-mr-pair"><div><span>광고 클릭당 비용</span><b>571원</b></div><div><span>광고 클릭</span><b>2,038회</b></div></div><p>Google 광고로 처음 유입된<br>활성 사용자당 평균 참여 시간 <b>4분 38초</b></p></div>\n</div></div>', cls='ef-marketing-slide', source='Meta·Google Ads, 「11/05 캠페인 CSV」, 2026. Google Analytics 4, 「8/24~11/05 사용자 획득」, 2026.'))
S.note('[약 30초] 누적 집행액은 Meta가 약 3분의 2, Google이 약 3분의 1입니다. Meta는 클릭당 약 110원으로 폭넓게 서비스를 알리고 소재 반응을 탐색하는 데 활용했습니다. Google은 클릭 단가가 높지만 관측된 사용자 참여 시간이 길어, 검색 의도가 있는 유입을 함께 확인하는 채널로 설명할 수 있습니다. 실제 지표를 바탕으로 집행 비중의 타당성을 설명하는 것이며, 처음부터 2 대 1이 최적임을 실험으로 입증했다는 뜻은 아닙니다.\n근거: 03_Meta캠페인.csv 합계2,338,208원/21,318링크클릭;04_Google주별.csv 합계1,163,048원/2,038클릭. 합3,501,256원; Meta66.782%,Google33.218%. CPC109.68/570.68원. 예산계획서나 날짜별 배분 결정 로그는 미확인; 이 슬라이드는 사후 성과 해석에 따른 설명 근거. 광고 클릭 정의는 플랫폼별로 다름. GA4 05_GA4획득.csv 첫 사용자 소스/매체 ig/paid61명57초, google/cpc57명278초. 활성 사용자당 평균 참여 시간이며 세션 체류시간 아님. 측정 동의 범위의 표본이며 인과 실험 아님. Google PMax 전체를 검색광고라고 부르지 않음. Google 최신11/11 지출1,377,062원과 혼합하지 않고11/05 스냅샷 사용.')

S.append(shell('Effect', '초반 노출 집중을 보고, <span class="purple">새 광고를 순차 투입</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">가설 1 · 1주 단위 신규 소재 투입으로 초기 노출 확보 시도</p>\n<div class="ef-mr-card" style="padding:12px 25px"><img class="ef-ad-chart" src="assets/mkt-ad-additions.svg" alt="전체 광고 일별 노출과 10월13일 새 고객 광고 추가, 10월23일 재집행, 10월25일 광고 추가"></div>\n<div class="ef-ad-observations">\n<div class="ef-ad-observation"><div class="label">초기 광고에서 관찰</div><h3>광고 1 · 집행 초반 노출 집중</h3><p>2일 차 <b>3,172회</b><br>3일 차 273회</p></div>\n<div class="ef-ad-observation"><div class="label">새 고객 광고 · 10/13 시작</div><h3>첫날 대비 2일 차 노출 확대</h3><p>7,155회 → <b>13,635회</b><br>10/23 재집행 후 2일 차 34,239회</p></div>\n<div class="ef-ad-observation"><div class="label">10/25 광고 · 10/25 시작</div><h3>2일 차에 해당 광고 최대 노출</h3><p>15,854회 → <b>26,918회</b><br>첫날 대비 <b>69.8% 증가</b></p></div>\n</div></div>', cls='ef-marketing-slide', source='Meta Ads, 「광고 이름·광고 세트별 일별 실적 CSV」, 2026-11-11. Dozer 운영자, 「소재 추가 운영 의도」, 2026-11-11.'))
S.note('[약 35초] 먼저 집행한 광고에서 초반에 노출이 집중되는 사례를 보고, 일주일 단위로 새 소재를 넣어 초기 반응을 확보해 보자는 가설을 세웠습니다. 예를 들어 광고1은2일차3,172회였지만3일차에는273회로 줄었습니다. 이후 새 고객 광고와10월25일 광고를 추가했습니다. 새 고객 광고는첫날7,155회에서2일차13,635회로,10월25일 광고는15,854회에서2일차26,918회로 늘었습니다. 신규 광고의 집행 초반에 노출이 확대되는 현상을 다시 관찰했습니다.\n운영 의도: 사용자2026-11-11 설명의 일주일 단위 광고 추가 시도. 실제 최초 노출일은 새 고객 광고10/13,재집행10/23,10/25광고10/25. 두 광고 최초 집행일 간격은12일,재집행과10/25간격은2일이므로 정확히7일마다 집행했다고 발표하지 않음. 날짜는 업로드/편집 시각이 아닌 최초 실제 노출일. 재집행은10/15~22해당광고 노출없음 뒤10/23관측 재개를 뜻함.\ndata/troubleshooting/meta-ad-daily.csv는광고세트와광고이름·일별실적의실제Meta내보내기. 일별전체노출합666197. 그래프는광고전체합,하단은개별광고수치이므로10/25총노출26517과개별첫날15854를혼동하지않음. 새고객10/13:7155,10/14:13635,10/23:28223,10/24:34239,10/25:10663.10/25광고의10/26:26918은해당광고최대일노출. (26918/15854-1)*100=69.7868%.\n앞선모든광고에서1~2일최대였다는뜻은아님. test세트는3일차최대, test사본과오디세이는후반최대인반례도있음. 초반집중관찰사례를제시한것이며주간교체의보편적효과를입증한것이아님. 광고1중단및소재변경,예산,집행시간,타깃,학습상태를통제하지않았으므로노출감소를소재피로도만으로단정하거나플랫폼노출부스트라고설명하지않음.')

S.append(shell('Effect', 'AI 기능을 활용한 10/25 광고, <span class="purple">첫 7일 노출 최다</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">가설 2 · Meta AI 기능 활용 시 노출 확대 가능성 · 전체 6개 광고 세트의 첫 7일 비교</p>\n<div class="ef-ad-ai"><div class="ef-mr-card"><div class="label">10/25 캠페인에 적용</div><h3>AI 이미지 생성<br>+ 음악 추가</h3><p>Meta가 제공하는 기능을<br>활용해 광고 소재 제작</p><div class="rule"><div class="ef-mr-number">124,257<small>회</small></div><h3 style="margin-top:18px">첫 7일 노출 수 1위</h3></div><div class="ef-mr-highlight">1,000회 노출당 비용도 최저<br><b>3,340원</b></div></div>\n<div class="ef-mr-card"><div class="label">최초 노출일부터 7일간 · 모든 실집행 광고 세트</div><table class="ef-ad-table"><thead><tr><th>광고 세트</th><th>노출 수</th><th>집행액</th><th>1천 회당 비용</th></tr></thead><tbody><tr><td>기본 광고 세트</td><td>40,047</td><td>13.5만</td><td>3,360원</td></tr><tr><td>test</td><td>51,552</td><td>19.1만</td><td>3,705원</td></tr><tr><td>test 사본</td><td>58,213</td><td>25.0만</td><td>4,290원</td></tr><tr><td>10/13 · 새 고객</td><td>20,790</td><td>8.3만</td><td>3,972원</td></tr><tr><td>테스트</td><td>17,341</td><td>6.8만</td><td>3,934원</td></tr><tr class="selected"><td>10/25 · AI 활용</td><td>124,257</td><td>41.5만</td><td>3,340원</td></tr></tbody></table><div class="ef-mr-highlight">다른 5개 세트의 합산 기준 대비<br>1,000회 노출당 비용 <b>13.5% 낮음</b></div></div></div></div>', cls='ef-marketing-slide', source='Meta Ads, 「광고 세트별 첫 7일 실적」, 2026-11-11. Dozer 운영자, 「10/25 AI 이미지·음악 기능 활용」, 2026-11-11.'))
S.note('[약 35초] 두 번째는Meta자체AI기능을활용하면노출확대에도움이될수있다는가설입니다.10월25일캠페인에는AI이미지생성과음악추가를활용했습니다. 모든광고세트의최초노출일부터7일을비교한결과10월25일세트가124,257회로가장많이노출됐습니다. 집행액이서로다르므로1,000회노출당비용도함께봤습니다.10월25일세트는3,340원으로가장낮았고,나머지5개세트의합산기준보다13.5%낮았습니다. AI기능을활용한광고에서초기노출성과가좋았던사례입니다.\n음악추가·AI이미지생성을10/25캠페인에사용했다는사실은사용자2026-11-11운영설명에근거.기존확인자료meta-ad-settings.json은test1소재의현재설정이므로10/25의기능증빙으로전용하지않음. 음악추가가반드시AI로작곡한음악이라는뜻도아님.\n모집단:meta-ad-daily.csv의실제노출있는6개광고세트모두. 비교기준은각세트최초실노출일부터6일후까지7개달력일. 무집행일포함,서로다른광고가동일세트에있으면합산. 기간8/31~9/6,9/26~10/2,9/29~10/5,10/13~19두세트,10/25~31. scripts/analyze_ad_level.py와ad-set-first7-comparison.csv참조. 10/25노출124257,지출415079,CPM3340.48786;나머지합산CPM3863.38411,13.5347%낮음.단순CPM평균이아닌지출합/노출합.기본세트CPM3360.20426과의차이는약0.6%로근소함.10/25의총집행기간노출124258과1회차이는11/1잔여노출1회.\n첫7일의관측순위이며전체기간이나클릭률·클릭당비용까지1위라는뜻은아님. 전체기간CPM은기본세트2990.41원으로10/25보다낮음. 다른세트도AI기능을사용했을수있으며ON/OFF대조군없음. 예산·기간·타깃·소재·집행중단을통제하지않아AI사용자체의효과또는Meta의노출우대가증명됐다고말하지않음.기간선택은초기집행성과비교를위해모든세트에동일7일규칙적용;비용보정지표가인과통제를대체하지않음.')

S.append(shell('Effect', '서울에서 시작해, <span class="purple">전국 16개 시도로 도달 확대</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">초기 서울 타기팅 → 대한민국 전체로 확대 · Meta 지역별 도달 수 기준</p>\n<div class="ef-ad-region"><div class="ef-mr-card"><div class="label">1단계 · 서울 우선 공략</div><h3>초기 기본 광고 세트<br>8/31~9/23</h3><div class="ef-mr-number">138,998<small>명</small></div><h3>서울 도달 수</h3><p>서울을 중심으로<br>서비스 인지도 확보</p><div class="ef-mr-highlight">인접 경기 지역에도<br>14,366명 도달</div></div>\n<div class="ef-mr-card"><div class="label">2단계 · 전국으로 접점 확대</div><h3>새 고객 광고 · 10/13~25</h3><div class="ef-mr-bars"><div class="ef-mr-bar"><span>서울</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:50.05%;background:#b7a7df"></div></div><b>15,014</b></div><div class="ef-mr-bar"><span>경기·인천</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:71.67%;background:#9580d2"></div></div><b>21,500</b></div><div class="ef-mr-bar"><span>비수도권</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:92.61%;background:#6c5ce7"></div></div><b>27,783</b></div></div><div class="ef-mr-highlight">비수도권에서도 <b>27,783</b> 도달<br>전국 <b>16개 시도</b>에서 광고 도달 확인</div><p style="font-size:22px;margin-top:24px">경기·인천 및 비수도권: 시도별 도달 수 합계</p></div></div></div>', cls='ef-marketing-slide', source='Meta Ads, 「광고 세트×지역 도달 실적 CSV」, 2026-11-11. Dozer 운영자, 「서울→전국 타기팅 변경」, 2026-11-11.'))
S.note("[약30초] 처음에는서울을우선공략해서비스를알렸습니다. 초기기본광고세트에서서울도달수는138,998명이었습니다. 이후온라인서비스의이용가능지역에맞춰대한민국전체로타기팅을넓혔습니다. 새고객광고에서는서울15,014,경기·인천21,500,비수도권27,783의지역별도달을확인했습니다. 서울에서시작해전국16개시도로접점을넓힌운영과정입니다.\n실측:data/troubleshooting/meta-adset-region-reach.csv,Meta보고서광고세트×지역의도달지표.초기기본광고세트정식이름'추천 설정이 적용된 새로운 트래픽 광고 세트',8/31~9/23실제집행.서울138998,경기14366,인천0. 광고별도달을합산하지않고광고세트수준으로중복제거된지역별추정치를조회. 초기서울설정은사용자설명이나실제경기에도도달하므로서울밖0이라고말하지않음.\n전국확대사례는10/13광고세트/새고객광고,10/13~25실제노출일5일. 서울15014,경기18404,인천3096,나머지13개시도27783,Unknown4. 국가전체도달추정치63603과지역합계64301은일치하지않음:Meta의추정·중복등으로지역수치의단순합을중복제거된고유인원으로표현하면안됨. 화면에경기인천·비수도권은시도합계임을명시. 비수도권합계는서울경기인천및Unknown제외. 전국17개시도중세종별도행없음,도달확인16개. 10/25광고는4지역에서만도달이확인되므로전국확대성과로대체하지않음.\n비교는운영단계의대표광고세트로노출지역이다양해졌음을보임. 서로다른집행기간·비용으로도달규모증가율이나지역확대로인한가입상승을계산하지않음. 모든지역에균등분배됐다는뜻이아니며점차넓힌도달범위에관한설명.")

S.append(shell('Effect', '캐시워크 제외 전후, <span class="purple">광고 클릭 효율 비교</span>', '\n<div class="ef-mkt"><p class="ef-mkt-period">9/30 캐시워크 제외 · 전 9/23~29 / 후 10/01~07 · Google 캠페인 전체 실적</p>\n<div class="ef-performance-kpis">\n<div class="ef-mr-card"><div class="label">클릭당 비용</div><div class="metric">43.4<small>% 감소</small></div><div class="flow">486원 → 275원</div></div>\n<div class="ef-mr-card"><div class="label">클릭률</div><div class="metric">1.43<small>배</small></div><div class="flow">1.39% → 1.98%</div></div>\n<div class="ef-mr-card"><div class="label">광고비 1만 원당 클릭</div><div class="metric">76.7<small>% 증가</small></div><div class="flow">20.6회 → 36.4회</div></div>\n</div><div class="ef-performance-summary">\n<div class="ef-mr-card"><div class="label">전후 7일 집행 실적</div><table class="ef-perf-table" style="margin:5px 0"><tr><th>지표</th><th>제외 전</th><th>제외 후</th></tr><tr><td>광고비</td><td>146,233원</td><td>210,293원</td></tr><tr><td>전체 노출</td><td>21,677회</td><td>38,658회</td></tr><tr><td>클릭 수</td><td>301회</td><td>765회</td></tr></table></div>\n<div class="ef-mr-card"><div class="label">성과 해석</div><h3>지출 증가율보다<br>높은 클릭 증가율</h3><p>광고비 <b>43.8% 증가</b><br>클릭 수 <b>154.2% 증가</b></p><div class="ef-mr-highlight">클릭당 비용과 클릭률에서<br>유입 효율 개선 확인</div></div></div></div>', cls='ef-marketing-slide', source='Google Ads, 「변경 이력·캠페인 실적」, 2026-11-11 조회. Google Ads Help, 「About All conversions」.'))
S.note('[약 30초] 캐시워크를 제외한 뒤 해당앱노출이0이됐다는것은차단여부확인에불과해성과지표에서뺐습니다. 전후7일의캠페인전체실적을비교하면클릭당비용은486원에서275원으로43.4%낮아졌고,클릭률은1.39%에서1.98%로높아졌습니다.광고비1만원당확보한클릭도20.6회에서36.4회로늘었습니다.지출은43.8%늘었지만클릭은154.2%늘어클릭유입효율개선을확인했습니다.예산·입찰·소재도함께바뀌어변화전체를캐시워크제외만의효과라고단정하지는않습니다.\n변경시각2026-09-30 16:03:10 KST,계정제외mobileapp::2-com.cashwalk.cashwalk추가.비교기간9/23~29대10/1~7,양쪽7일·변경일제외.정본data/troubleshooting/cashwalk-before-after.json,실조회google-campaigns-before.json/after.json.전노출21677/클릭301/지출146233원,후38658/765/210293원.CPC485.8239→274.8928원,43.4172%감소.CTR1.3885685→1.9788918%,1.42513배,+0.5903233%p.클릭/지출*10000=20.5836→36.3778,76.7316%증가.1만원당클릭은실제동일예산으로실험한결과가아니라관측지출을정규화한값이며CPC의역수라독립된3번째효과근거는아님.광고비43.8068%증가,클릭154.1528%증가.\n동일시점입찰조정·제외키워드·전환목표등변경,9/28예산증액·신규애셋등동반변화.랜덤대조군없음.클릭효율개선을가입전환·면접이용·매출개선으로확대하지않음.전환수열은9/30저장소접근선택이주요→부수로바뀌고면접준비생성전환이신규추가돼전후구성이다름.각기간기본전환수4건과4건을동일행동의전환비교로쓰지않음.모든전환수에는페이지조회등다른행동이섞이므로그합계로성과주장하지않음. Google공식 https://support.google.com/google-ads/answer/3419678?hl=en , https://support.google.com/google-ads/answer/2375435?hl=en .\n캐시워크12516→0및보고서내65.2→0%는제외작동확인용보조근거로만보존;PMax게재위치보고서는검색노출제외라캠페인전체분모와다름.슬라이드성과비교는같은캠페인전체분모만사용.앱별지출이나가입손실액추정금지.')

S.append(shell('Effect', '로그인 회원 수의 <span class="purple">누적 추이</span>', '<div class="ef-mkt"><p class="ef-mkt-period">8/03~11/11 05:42 KST · 상단 누적 / 하단 일별 신규</p><div class="ef-mr-grid wide"><div class="ef-mr-card"><img class="ef-mr-chart accounts" src="assets/mkt-login-trend.svg" alt="로그인 회원 누적 및 일별 추이"></div><div class="ef-mr-aside"><div class="ef-mr-card"><div class="ef-mr-number">86<small>개</small></div><h3 style="margin-top:24px">로그인 회원</h3><p>GitHub 로그인 등으로 가입한<br>정식 회원 계정</p></div></div></div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「회원·게스트 계정 생성일 집계」, 2026-11-11.'))
S.note('[약 15초] 로그인 회원는 현재86개입니다. 위는누적계정수,아래는그날새로생성된계정수입니다.\n운영DB 읽기전용 트랜잭션,2026-11-11 05:42 KST. data/features/counts.sql 및counts.json. CANDIDATE계정 중 payment-test.invalid/review.invalid이메일제외. 내부운영자소유일반계정은추가제외하지않아기존관리자회원집계와일치. 사용자개별식별자는저장하지않음. 계정의created_at(UTC)+9시간KST가입일집계. 현재남아있는회원/게스트상태에따른계정생성추이이며일별로그인횟수나DAU가아님. 게스트→회원전환은현재회원으로분류되어과거곡선이재집계시바뀔수있음. 오늘은조회시점부분값이며이전날들과선연결. 전체연속날짜8/03~11/11. 합계는계정합이지동일인중복제거된사람수가아님.')

S.append(shell('Effect', '비로그인 체험 계정 수의 <span class="purple">누적 추이</span>', '<div class="ef-mkt"><p class="ef-mkt-period">8/03~11/11 05:42 KST · 상단 누적 / 하단 일별 신규</p><div class="ef-mr-grid wide"><div class="ef-mr-card"><img class="ef-mr-chart accounts" src="assets/mkt-guest-trend.svg" alt="비로그인 체험 계정 누적 및 일별 추이"></div><div class="ef-mr-aside"><div class="ef-mr-card"><div class="ef-mr-number">485<small>개</small></div><h3 style="margin-top:24px">비로그인 체험 계정</h3><p>로그인 전 서비스 체험을 위해<br>생성된 게스트 계정</p></div></div></div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「회원·게스트 계정 생성일 집계」, 2026-11-11.'))
S.note('[약 15초] 비로그인 체험 계정는 현재485개입니다. 위는누적계정수,아래는그날새로생성된계정수입니다.\n운영DB 읽기전용 트랜잭션,2026-11-11 05:42 KST. data/features/counts.sql 및counts.json. CANDIDATE계정 중 payment-test.invalid/review.invalid이메일제외. 내부운영자소유일반계정은추가제외하지않아기존관리자회원집계와일치. 사용자개별식별자는저장하지않음. 계정의created_at(UTC)+9시간KST가입일집계. 현재남아있는회원/게스트상태에따른계정생성추이이며일별로그인횟수나DAU가아님. 게스트→회원전환은현재회원으로분류되어과거곡선이재집계시바뀔수있음. 오늘은조회시점부분값이며이전날들과선연결. 전체연속날짜8/03~11/11. 합계는계정합이지동일인중복제거된사람수가아님.')

S.append(shell('Effect', '로그인·비로그인 계정을 합친 <span class="purple">전체 추이</span>', '<div class="ef-mkt"><p class="ef-mkt-period">8/03~11/11 05:42 KST · 상단 누적 / 하단 일별 신규</p><div class="ef-mr-grid wide"><div class="ef-mr-card"><img class="ef-mr-chart accounts" src="assets/mkt-combined-trend.svg" alt="계정 합계 누적 및 일별 추이"></div><div class="ef-mr-aside"><div class="ef-mr-card"><div class="ef-mr-number">571<small>개</small></div><h3 style="margin-top:24px">계정 합계</h3><p>로그인 회원 86개<br>+ 비로그인 체험 계정 485개</p></div></div></div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「회원·게스트 계정 생성일 집계」, 2026-11-11.'))
S.note('[약 15초] 계정 합계는 현재571개입니다. 위는누적계정수,아래는그날새로생성된계정수입니다.\n운영DB 읽기전용 트랜잭션,2026-11-11 05:42 KST. data/features/counts.sql 및counts.json. CANDIDATE계정 중 payment-test.invalid/review.invalid이메일제외. 내부운영자소유일반계정은추가제외하지않아기존관리자회원집계와일치. 사용자개별식별자는저장하지않음. 계정의created_at(UTC)+9시간KST가입일집계. 현재남아있는회원/게스트상태에따른계정생성추이이며일별로그인횟수나DAU가아님. 게스트→회원전환은현재회원으로분류되어과거곡선이재집계시바뀔수있음. 오늘은조회시점부분값이며이전날들과선연결. 전체연속날짜8/03~11/11. 합계는계정합이지동일인중복제거된사람수가아님.')

S.append(shell('Effect', '공고 분석부터 면접·피드백까지, <span class="purple">기능 이용 실적</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">로그인·비로그인 합산 · 테스트 계정 제외 · 11/11 05:42 KST</p>\n<div class="ef-feature-top">\n<div class="ef-feature-card"><div><h3>공고 분석 결과</h3><p>분석 결과를 보유한 준비 카드<br>서로 다른 공고 본문 141개</p></div><div class="ef-feature-number">234<small>건</small></div></div>\n<div class="ef-feature-card"><div><h3>레포지토리 코드 분석</h3><p>실제 코드 근거 생성 기준<br>고유 저장소 220개</p></div><div class="ef-feature-number">359<small>건</small></div></div>\n</div><div class="ef-feature-bottom">\n<div class="ef-feature-card"><h3>텍스트 면접 세트</h3><div class="ef-feature-number">66<small>세트</small></div><p>문항을 실제 열어본 세트<br>질문 학습 포함</p></div>\n<div class="ef-feature-card"><h3>음성 모의면접</h3><div class="ef-feature-number">20<small>세트</small></div><p>문항을 실제 열어본 세트<br>음성 인식 10세트 · 25회</p></div>\n<div class="ef-feature-card"><h3>문항 피드백 생성</h3><div class="ef-feature-number">91<small>개</small></div><p>문항별 답변 피드백<br>37개 세트에 제공</p></div>\n</div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「공고·레포 분석, 문항 열람, 음성 인식, 문항 피드백 집계」, 2026-11-11.'))
S.note('[약35초] 실제이용기록을기준으로대표기능의성과를한장에모았습니다. 공고분석결과를보유한준비카드는234건,코드근거가생성된레포분석은359건입니다. 고유저장소로는220개입니다. 문항을실제로열어본텍스트면접세트는질문학습을포함해66세트,음성모의면접은20세트였습니다. 문항별피드백은37개세트에서총91개생성됐습니다. 이수치는기능별이용기록이며고유사용자수와는다릅니다.\n통합전39·40페이지의동일DB집계. CANDIDATE계정중payment-test.invalid/review.invalid제외.일반내부계정추가제외없음. SQL읽기전용. 공고본문과insight결과존재234카드,md5본문141,전체준비252;캐시재사용포함,고유정규화공고141을뜻하지않음.레포분석snippet>0이고cs_only=false,READY49+PARTIAL310=359.실패58·CS전용65제외.저장소정규화이름lower기준220.359건모두완전성공이라고쓰지않음.\nset_id별viewed_at보유를1세트로집계.텍스트66=JD_MATCH33+PRIORITY31+MOCK_INTERVIEW2로질문학습포함. 운영화면의텍스트입력은JD_MATCH이고기본모의면접은PRIORITY로생성됨. MOCK_INTERVIEW라는DB유형명만으로텍스트모의면접을정의하면누락이생기므로모드분류는voice_enabled기준. 텍스트MOCK_INTERVIEW2세트는질문은행선택경로의일부이며텍스트모의면접전체가아님.음성MOCK_INTERVIEW20,STT보유10세트25건,음성답변저장9세트. 문항열람은재실행횟수/모든질문완료수와다름. 모의면접완료상태0.피드백attempt_feedback91행/37세트,그중MOCK_INTERVIEW8행/7세트. 피드백생성이지확인/열람횟수아님.각지표를사람수퍼널로연결하거나합산하지않음.')

S.append(shell('Effect', '핵심 기능인 모의면접, <span class="purple">이용 확대에 맞춘 광고</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">11/11 05:42 KST · 로그인·비로그인 합산 · 계정 기준 중복 제거</p>\n<div class="ef-mock-value"><div class="label">01 DevFit의 핵심 기능</div><div class="ef-mock-core-body"><h3>내 코드로 연습하는<br>텍스트·음성 모의면접</h3><div><p>코드 기반 질문에 직접 답하고<br>피드백으로 설명력을 점검하는 경험</p><div class="emphasis">핵심 기능의 가치를 알리고 실제 답변까지 이어지는 이용 확대</div></div></div></div>\n<div class="ef-mock-direction"><div class="ef-mock-current"><div class="label">02 이용 현황 · 모의면접 문항을 열어본 계정</div><div class="ef-mock-kpis">\n<div class="ef-mock-kpi"><h3>텍스트 모의면접</h3><div class="number">29<small>개 계정</small></div><p>66세트 문항 열람</p></div>\n<div class="ef-mock-kpi"><h3>음성 모의면접</h3><div class="number">5<small>개 계정</small></div><p>20세트 문항 열람</p></div>\n</div></div>\n<div class="ef-mock-next"><div class="label">03 앞으로의 광고 포커스</div><h3>앞으로는 모의면접 기능을<br>중점적으로 홍보합니다</h3><p>내 코드로 답변을 연습하고 피드백을 받는<br>텍스트·음성 모의면접의 가치를 알립니다.</p><div class="ef-mock-goal">목표 · 모의면접 기능 이용자 확대</div></div></div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「답변 모드별 문항 열람·답변 보유 계정 집계」, 2026-11-11. DevFit FE·BE, 「운영 브랜치 모드 분류 코드」, 2026-11-11.'))
S.note("[약25초] DevFit의 핵심 기능은 내 코드에서 나온 질문에 직접 답하고 피드백을 받는 텍스트·음성 모의면접입니다. 실제 이용 현황을 보면 문항을 열어본 계정은 텍스트 29개, 음성 5개입니다. 앞으로는 이 모의면접 기능을 중점적으로 홍보하겠습니다. 내 코드로 답변을 연습하고 피드백을 받는 가치를 알려, 핵심 기능을 이용하는 사용자를 늘리는 것이 목표입니다.\n정정: 이전40쪽의텍스트1개/답변2개는set_type='MOCK_INTERVIEW'로잘못한정한부분집계였다. 운영코드상텍스트입력선택은JD_MATCH,자동기본모의면접은PRIORITY로생성되므로두유형을제외하면실제텍스트이용을누락한다. 현재화면·관리자와같이voice_enabled=false를텍스트,true를음성으로분류하되이용지표는세트생성후실제문항최초열람을확인한계정으로집계. 생성수와문항열람수를혼동하지않음.\n코드근거: Devfit_FE prod 9b436df993d0a2d6e51db5b097abc0f52757d666의SetDashboard.tsx, ANSWER_MODE_OPTIONS의JD_MATCH=텍스트입력,MOCK_INTERVIEW=음성인식,카드표시voiceEnabled기준. Devfit_BE prod 88d6f3b8f0f2c0a78dbb64ac85adc9f6c7cec363의StudySetService.java는bootstrapDefaultSet에서PRIORITY로기본모의면접생성;AdminBehaviorService.java도voice_enabled로TEXT/VOICE분류. 저장사본data/features/*-prod.*. 관리자생성기준수치와차이가나는이유는관리자가created_at을집계하고이슬라이드는viewed_at까지확인하기때문. 제외계정기준도관리자기본과다를수있음.\n데이터근거:data/features/interview-mode-audit.sql, interview-mode-audit.json. 운영DB읽기전용집계,개인식별자·원문답변추출없음. 조회시각2026-11-10T22:07:33.706168+00:00. 이전39쪽과맞추기위해계정·세트생성및문항최초열람을2026-11-10 20:42:51.23812UTC(11/11 05:42:51KST)이하로제한. CANDIDATE중payment-test.invalid/review.invalid제외,내부일반계정포함. 현재보존데이터/현재guest상태기준. 답변은당시이전생성된question_attempt의현재비공백answer를집계하므로과거수정·삭제를완전히복원하는시점복구쿼리는아님.\n텍스트:201세트생성/87계정,66세트열람/29계정(회원21·게스트8),답변기록32세트/19계정. 열람세트유형JD_MATCH33·PRIORITY31·MOCK_INTERVIEW2. 유형별이용계정은20·17·1이며중복이있어단순합이아닌user_id중복제거로29. 음성:20세트열람/5계정(회원3·게스트2),답변기록10세트/2계정,STT10세트/2계정. 두모드이용중복5계정→합계29,답변계정중복2→합계19. 39쪽66세트와40쪽29계정은같은텍스트모드·문항열람범위. 기록보유계정이지고유자연인수는아님. 문항열람은전체면접완료나답변완료가아님. StudySetService.restoreArchivedAnswers로이전답변복원도가능하므로답변19는'신규답변제출자'대신'답변기록보유계정'으로표기.\n화면에서는 중복 제거 계정·답변 기록 합계와 하단 집계 설명을 삭제하고, 계정 수와 열람 세트 수를 확대 배치. 집계 정의와 원자료는 위 근거 노트에 보존. 3번은 모의면접 기능의 가치 홍보와 이용자 확대라는 향후 방향만 제시하며, 영상 제작·랜딩·CTA·광고비 등 구체적인 광고 방식 설명은 삭제. 향후 계획이며 집행 완료가 아님. 임의 목표 수치 없음. 이용이 적은 원인이 광고라고 입증한 것은 아님. 실제 광고 설정 변경·게시 없음.")

# ---------- 마케팅 끝 ----------


# ---------- ③ 지표 — 유저 · 실운영 ----------
S.append(shell('Effect', '사용량 상위 8명: 가입 후 <span class="purple">최대 69일째 재방문</span>', '''
<div class="ef-stage"><div class="ef-pu">
  <div class="ef-pu-l">
    <div class="ef-us-h">상위 8명 · 외부 회원<br><small style="font-size:18px">관리자 콘솔 · 2026-11-11 조회 · 이름·메일 비공개</small></div>
    <table class="ef-pu-t"><thead><tr><th>회원</th><th>가입</th><th>최근 방문</th><th>분석한 날</th><th>걸친 주</th><th>저장소 분석</th><th>LLM 호출</th></tr></thead><tbody><tr><td>회원 A</td><td>09-03</td><td>11-11</td><td class="d"><b>8</b>일</td><td>3주</td><td>3회</td><td>49</td></tr><tr><td>회원 B</td><td>09-27</td><td>11-02</td><td class="d"><b>3</b>일</td><td>3주</td><td>1회</td><td>37</td></tr><tr><td>회원 C</td><td>10-09</td><td>11-06</td><td class="d"><b>2</b>일</td><td>2주</td><td>4회</td><td>147</td></tr><tr><td>회원 D</td><td>10-14</td><td>11-11</td><td class="d"><b>2</b>일</td><td>2주</td><td>4회</td><td>95</td></tr><tr><td>회원 E</td><td>09-27</td><td>10-22</td><td class="d"><b>1</b>일</td><td>1주</td><td>32회</td><td>247</td></tr><tr><td>회원 F</td><td>10-23</td><td>11-08</td><td class="d"><b>3</b>일</td><td>3주</td><td>6회</td><td>77</td></tr><tr><td>회원 G</td><td>10-26</td><td>11-11</td><td class="d"><b>2</b>일</td><td>1주</td><td>7회</td><td>371</td></tr><tr><td>회원 H</td><td>10-28</td><td>11-11</td><td class="d"><b>1</b>일</td><td>1주</td><td>2회</td><td>238</td></tr></tbody></table>
    <div class="ef-us-meta">8명 중 <b>6명</b>이 서로 다른 날 다시 와서 분석 · <b>5명</b>은 2주 이상에 걸쳐 사용 · 7명이 11월에도 방문</div>
  </div>
  <div class="ef-pu-r">
    <div class="ef-us-h">외부 회원이 준비한 공고 <b style="color:var(--ink)">83건</b><br><small style="font-size:18px">11-04 집계 · 외부 회원 79명 · 고유 회원 수</small></div>
    <div class="ef-bar"><span>토스 계열</span><i class="top" style="width:100%"></i><b>9명</b></div>
    <div class="ef-bar"><span>현대자동차</span><i style="width:44%"></i><b>4명</b></div>
    <div class="ef-bar"><span>롯데이노베이트</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-bar"><span>당근</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-bar"><span>SK하이닉스</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-us-meta">공고 2건 이상 준비한 회원 <b>16명</b> (공고 등록 회원의 27%)<br>포지션 <b>백엔드 34 · 프론트엔드 19</b> (공고의 64%)</div>
  </div>
</div></div>''', source='파워유저: 관리자 콘솔 회원 목록 상위 8명 (2026-11-11 캡처, 제외 표시 없는 외부 회원, 이름·메일 비공개) · 공고: 관리자 콘솔 회원별 상세 합산 (2026-11-04 집계, 내부 계정 4명 제외 외부 회원 79명 기준 · 게스트 공고 제외)'))
S.note('''[≈18초] 사용량 상위 8명을 보면, 가입하고 길게는 69일이 지나서도 다시 찾아왔고 8명 중 7명은 11월에도 방문했습니다. 6명은 서로 다른 날 다시 와서 저장소를 분석했고, 5명은 2주 이상에 걸쳐 썼습니다. 외부 회원들이 실제로 준비한 공고는 83건입니다. 토스 계열을 준비한 회원이 9명으로 가장 많고, 현대자동차, 롯데이노베이트, 당근, SK하이닉스가 뒤를 잇습니다. 백엔드와 프론트엔드가 공고의 64%입니다. 공고를 두 건 이상 준비한 회원이 16명, 가입하고 일주일이 지나서도 다시 와서 쓰는 회원이 14명입니다.

상위 8명 표 빈도 칸(11-11 관리자 콘솔 GET /api/admin/b2c/members/{id}?days=90, 읽기 전용): 분석한 날 = llm.daily에서 호출 1회 이상인 날짜 수(가입 후 전 기간, 창 08-14~) · 걸친 주 = 그 날짜들이 걸친 월요일 시작 주 수 · 저장소 분석 = activity.analyses.total. 회원별 분석한 날/주: A 8/3 · B 3/3 · C 2/2 · D 2/2 · E 1/1 · F 3/3 · G 2/1 · H 1/1 (합계 22일, 중앙값 2일). 최근 방문 = 콘솔 lastVisitedAt(로그인·페이지 방문 기준, 분석을 안 한 방문 포함). ⚠ Q&A: «매일 쓰나?» → 아니오, LLM을 쓴 날 기준 1~8일. 마지막 분석일은 A 09-17 · B 11-02 · C 10-30 · D 10-23 · E 09-27 · F 11-02 · G 10-28 · H 10-28 — 최근 방문과 다름. 학습 세트 답변 기록이 있는 회원은 D·E 2명. ⛔ «매일»·«주 N회»·«충성 고객»·«팬» 금지. 콘솔 «loyal» 정렬 원본은 앞에 8월 가입 계정 6개가 더 있음(캡처에 없음, 내부 계정 여부 미확인) — 표는 캡처와 같은 8명(가입 시각으로 대조).
파워유저 표 원본(11-11 사용자 제공 관리자 콘솔 캡처): 순위는 콘솔 목록 순서 그대로(정렬 기준은 콘솔 기본값) · 8명 모두 상태 «사용 중»·제외 체크 없음(외부 회원). 회원 A~H = 순위 1~8. 가입 후 이용 = 최근 방문일 − 가입일(일). 누적 토큰 A 19만 · B 17.5만 · C 49.8만 · D 79.8만 · E 193.4만 · F 55.7만 · G 148.4만 · H 65.8만, 합계 629.4만. 11월 미방문 1명 = E(최근 10-22). ⛔ 이름·메일·GitHub ID를 장표·발화에 쓰지 않음(캡처 원본에 실명·메일 있음 — 원본 이미지 장표에 넣지 말 것). 공고 83건(11-04)과 파워유저 표(11-11)는 집계 시점이 다름.
출처: collect/A-admin-usage.md §1-1·§4 (GET /b2c/members/{id} × 83명 합산, 2026-11-04, 내부 계정 user id 1·5·7·11 제외 → 외부 79명). 공고 83건 전부 집계(10건 초과 회원 없음). 게스트 공고 66건은 어드민 목록에 없어 제외.
기준 차이: 보고서 KPI(83명·90.4%·81.9%)는 11-09 게스트 제외 회원 83명 기준, 이 장 공고 막대는 11-04 외부 79명 기준, 마케팅 장 누적 회원 86명은 11-11 기준 — 숫자를 서로 섞지 않음(활성화 장은 11-11 마케팅 개편에서 본편에서 빠짐). 공고 83건과 회원 83명은 우연히 같은 숫자.
회사: 고유 회원 수, 토스 계열 = 토스·토스증권·토스플레이스 등 합산. 1명짜리 회사명은 쓰지 않음(특정인 추정 방지), 회사 미입력 11명. 로고 쓰지 않음.
출처 구분: 채용 플랫폼 33(원티드 16 · 잡코리아 12 · 사람인 5) · 기업 채용 사이트 18(토스 7 · 현대차 4 · 롯데 2 · KT·풍산·그리팅·K뱅크·삼성 각 1) · URL 없음(텍스트 붙여넣기·이미지) 32.
16명 = 공고 2건 이상 등록 회원(공고 등록 회원 60명의 27%). 14명 = 가입 후 7일 이상 지나서도 활동 기록이 있는 회원(lastActivityAt 기준 재방문 근사치, 79명의 18%).
⛔ «팬 N명»·«열성 팬» 라벨 금지. ⛔ «토스 지원자가 많이 쓴다» 이상의 일반화 금지(칸 대부분 1~2명). 세트 완료·답변 수 같은 하위 수치는 넣지 않음.''')




# ---------- ① 6개월 타임라인 ---------- (근거: research/R3-ef-timeline.md)

LANES = [('biz', '사업 · 검증'), ('ai', 'AI · 엔진'), ('be', '백엔드 · 인프라'), ('fe', '프론트엔드')]
PHASES = ['1–10주 · 피봇 · MVP · 출시', '11–20주 · 질문 품질 개선 · 수익화']
def timeline(phase, cols, events, big):
    """cols: [(라벨, 시작일)] 5개(2주 단위) · events: {(lane, 열 인덱스 0~4): [(라벨, 날짜, kind)]} · kind: ''/'star'"""
    ph = ''.join(f'<span class="{"on" if i == phase else ""}">{n}</span>' for i, n in enumerate(PHASES))
    g = ['<div class="ef-tl"><div></div>'] + [f'<div class="wk">{w}<small>{d}~</small></div>' for w, d in cols]
    for key, name in LANES:
        g.append(f'<div class="ln {"biz" if key == "biz" else ""}">{name}</div>')
        for i in range(5):
            items = events.get((key, i), [])
            pills = ''.join(f'<div class="pill {k or ("biz" if key == "biz" else "")}">{t}<small>{d}</small></div>' for t, d, k in items)
            g.append(f'<div class="cell">{pills}</div>')
    g.append('</div>')
    return f'<div class="ef-tlhead"><div class="ph">{ph}</div><div class="big">{big}</div></div>' + ''.join(g)

S.append(shell('Effect', '1–10주차: 피봇 후 MVP 구축과 <span class="purple">첫 운영 배포·중간평가</span>', timeline(0,
    [('1–2주차', '06-29'), ('3–4주차', '07-13'), ('5–6주차', '07-27'), ('7–8주차', '08-10'), ('9–10주차', '08-24')], {
    ('biz', 0): [('피봇 승인 → 개발 착수', '06-24 신청 · 06-29 첫 커밋', '')],
    ('biz', 1): [('공고 단위 준비로 제품 재정의', '07-16', '')],
    ('biz', 2): [('약관 · 처리방침 · SEO 기반', '07-27', ''), ('자유 멘토링 3시간', '08-07', '')],
    ('biz', 3): [('★ 중간평가 · 피드백 19건', '08-20', 'star')],
    ('biz', 4): [('Google 광고 집행 시작', '08-24', ''), ('사업자등록 (도저랩스)', '09-02', '')],
    ('ai', 0): [('분석 엔진 · 프롬프트 압축', '06-29', ''), ('내가 짠 커밋만 조준', '07-05', '')],
    ('ai', 1): [('합불·저자 판정 제거', '07-18', '')],
    ('ai', 2): [('질문 유용성 라벨', '07-27', '')],
    ('ai', 3): [('비공개 레포 분석 (증분 동의)', '08-18', '')],
    ('ai', 4): [('질문 품질 평가 하네스', '09-06', '')],
    ('be', 0): [('GitHub 로그인', '06-30', ''), ('JWT 쿠키 인증', '07-11', '')],
    ('be', 1): [('B2B 채용 워크플로', '07-19', ''), ('CI/CD · S3 + CloudFront', '07-23', '')],
    ('be', 2): [('운영 승격 게이트', '08-01', ''), ('★ 첫 운영 배포 (B2C 출시)', '08-03', 'star')],
    ('be', 3): [('로그인 시도 제한 · P0 4건', '08-13', '')],
    ('be', 4): [('관리자 API · 사용량 계측', '08-28', ''), ('인크루트 공고 지원', '09-01', '')],
    ('fe', 0): [('프론트 초기화', '06-29', ''), ('분석 결과 대시보드', '07-07', '')],
    ('fe', 1): [('B2C 랜딩 · 로그인', '07-13', ''), ('공고 중심 랜딩 개편', '07-19', '')],
    ('fe', 3): [('FE↔BE API 계약 CI', '08-13', ''), ('레포 범위 선택 ← 08-07 지적', '08-23', '')],
    ('fe', 4): [('관리자 콘솔 13화면', '08-28', ''), ('푸터 사업자 정보 고지', '09-03', '')],
}, '출시 전 커밋<b>307</b>개 · 출시 후 5주 운영 배포<b>43</b>회'), source='날짜: 커밋·PR·서류로 확인한 것만 (research/R3-ef-timeline.md) · 커밋 = BE+FE 원격 전체, 08-02까지 · 운영 배포 = 운영 브랜치 성공 배포 (BE+FE, 08-03 ~ 09-06)'))
S.note('''[≈18초] 6월 24일 베베톡에서 DevFit으로 피봇을 신청했고, 29일 첫 커밋을 했습니다. 5주 동안 내가 짠 커밋만 골라 읽는 분석 엔진, GitHub 로그인, B2B 채용 흐름, CI/CD와 운영 승격 게이트까지 세웠고, 8월 3일 첫 운영 배포로 B2C를 열었습니다. 8월 20일 중간평가에서 피드백 19건을 받았고, 자유 멘토링에서 나온 «모르는 서비스에 GitHub를 연결하면 털리지 않냐»는 지적은 레포 범위 선택 화면으로 답했습니다. 9월 2일 사업자등록을 했습니다.

출처: research/R3-ef-timeline.md §2·§3. 피봇 신청서 admin/soma/첨부1(06-24, 직접) · 승인 의견서 06-25(고세환 멘토). 커밋 307 = git rev-list --count --remotes=origin --until=2026-08-03 (FE+BE). 운영 배포 43회 = collect/data/dora_prod_deploys_weekly.csv W32–W36. Google Ads 08-24(ads_weekly.csv 첫 비용).
«합불·저자 판정 제거»(07-18, BE b75c6f6·FE ac41bfe) = GDPR Art 22 대응. 본연수 시작일·팀 결성일은 문서에 없어 쓰지 않음.
⛔ Meta 광고 시작일(08-10)은 원천 미확인 → 넣지 않음. GA4 코드(08-12)는 운영 반영일 미확인 → 넣지 않음.''')

S.append(shell('Effect', '11–20주차: 질문 품질 개선과 <span class="purple">결제 · 특허 · 신고</span> 완료', timeline(1,
    [('11–12주차', '09-07'), ('13–14주차', '09-21'), ('15–16주차', '10-05'), ('17–18주차', '10-19'), ('19–20주차', '11-02')], {
    ('biz', 0): [('한유일 멘토 · 현직자 인터뷰', '09-07', ''), ('검색 유입 정비 (SEO)', '09-16~17', '')],
    ('biz', 1): [('CI/CD 멘토링', '09-22', '')],
    ('biz', 2): [('토스 결제 심사 연동', '10-15', '')],
    ('biz', 3): [('직업정보제공사업 신고', '10-19', ''), ('★ 특허 3건 출원', '11-01', 'star')],
    ('biz', 4): [('통신판매업 신고 · 상표 출원공고 결정', '11-02 · 11-06', ''), ('최종 보고서 · 발표', '11-09 · 11-11', '')],
    ('ai', 0): [('★ 난이도·유형 분리 ← 09-07', '09-09', 'star'), ('음성 모의면접 운영', '09-16', '')],
    ('ai', 1): [('답변 기반 음성 꼬리질문', '10-01', '')],
    ('ai', 2): [('실기업 기출 운영', '10-08', ''), ('커밋 판별 근거 · 기출 조회', '10-18', '')],
    ('ai', 3): [('분석 실패 사유 코드', '10-19', ''), ('근거 diff 판별 · 병렬 수집', '10-24', '')],
    ('ai', 4): [('★ 기출 의미 검색 (pgvector)', '11-02', 'star'), ('공개 기출 1,880건', '11-08', '')],
    ('be', 0): [('모의면접 출력 한도', '09-07', ''), ('공고 캐시 · 크롤러', '09-19', '')],
    ('be', 1): [('비동기 배포 + Slack', '09-22', '')],
    ('be', 2): [('Sentry 운영 오류 수집', '10-08', ''), ('관리자 유입·이용 통계', '10-14', '')],
    ('be', 3): [('결제·탈퇴 결함 7건 수정', '10-22', ''), ('B2B 블라인드 평가', '10-29', '')],
    ('be', 4): [('★ 단건 결제 운영 반영', '11-02', 'star')],
    ('fe', 0): [('음성 모의면접 화면', '09-16', ''), ('CS 면접 질문 색인', '09-17', '')],
    ('fe', 1): [('면접 출제 사례 표시', '09-30', '')],
    ('fe', 2): [('결제 심사 페이지', '10-15', '')],
    ('fe', 3): [('분석 실패 사유 안내 ← 09-22', '10-19', ''), ('블라인드 평가 화면', '10-29', '')],
}, '누적 운영 배포<b>138</b>회'), source='누적 운영 배포 = 출시 후 전체 (03-실행력-집계.md) · research/R3-ef-timeline.md'))
S.note('''[≈18초] 9월 7일 한유일 멘토님이 쉬운 질문이 사실 확인뿐이라고 지적하셨고, 난이도·유형 분리를 운영에 반영했습니다. 9월 22일 멘토링에서 나온 배포 알림 요청도 반영했고, 음성 모의면접과 실기업 기출이 들어갔고, 지금 기출은 1,880건입니다. 마지막 구간에는 돈을 받을 준비를 했습니다. 토스 결제 심사를 거쳐 11월 2일 단건 결제를 운영에 반영했고, 직업정보제공사업·통신판매업 신고와 특허 3건 출원을 마쳤습니다. 출시 후 운영 배포는 모두 138회입니다.

출처: research/R3-ef-timeline.md §4·§5. 11–15주 커밋 556개(BE+FE 원격, 09-07~10-11, 네 구간 중 최대 — 장표에서는 뺌). 난이도 분리 BE 32e25e9·8aa7bfa → prod #47 6cf2a7e. 음성 BE#53 → prod #54 98ebb0f. 기출 BE#85 → prod #89(10-08), 10-11 정제 업로드(41개사) = 1차 853건. 11-08 운영 DB 실측(gichul) 기출 1,880 / 벡터 1,880 · 누락 0 = 1차 853 + 2차 1,027 (ppt-start 전달, 사용자 지시). 10-08 칸에 1,880을 쓰지 않음 — 그 시점엔 853. 단건 결제 BE#153 → prod #154 fe0bce6(11-02). 기출 pgvector BE#159 c680990(11-02). 특허 출원번호통지서 3건(11-01). 상표 출원공고결정서 40-2026-0177374(11-06 발송, claims C10).
장표에서 뺀 항목(2장 압축, 2026-11-07): 광고 수신 동의·약관 개정(09-09) · IT 기업 대표 서면 회신(10-26) · 김종욱 멘토 서비스 검증(10-25) · 전략 멘토링(11-02) — 멘토 건은 부록 A15(현업 검토)에서 다룸.
단건 결제 LIVE는 사용자 확인 완료(claims.md C3). 매출은 0.
⛔ 숭실대 취업박람회(09-09~10)는 실시일 미확인 → 넣지 않음. «1,880건 검증됨»·«검증된 기출» 금지(사람 검수 REVIEWED 0).
SBOM 차단 게이트 f7d2f42는 11-05 0fe63e1 승격으로 origin/prod 반영(merge-base 확인) → «HIGH·CRITICAL 1건 이상이면 배포 잡 중단 · 백엔드만»까지 허용, ⛔ «취약점 0건 = 안전»·«FE 포함» 금지.
⛔ «운영» 라벨 금지(main만): 11-02 멘토링 개선 4종 · 처리방침 OpenAI 고지 · Free 월 5회 축소.
토스페이먼츠 계약 완료는 BM 장에 표기(11-11 사용자 지시). 날짜(10-28)는 간접이라 장표에 쓰지 않음.''')

# ---------- ② 개발 외적으로 한 일 ---------- (근거: research/R2-ef-offdev.md · feedback/05_세션별분석)
def mrow(logo, alt, who, role, advice, works, todo=False):
    w = ''.join(f'<li>{x}</li>' for x in works)
    return f'''<div class="ef-mr{' todo' if todo else ''}">
  <div class="ef-mr-who"><b>{who}</b><small>{role}</small></div>
  <div class="ef-mr-adv">{advice}</div>
  <ul class="ef-mr-work">{w}</ul>
</div>'''
APX.append(shell('Appendix · A15', '현업 면접관·게임사 대표의 <span class="purple">서비스 검토와 반영</span>', f"""
<div class="ef-mtab">
  <div class="ef-mh"><span>누구</span><span>조언</span><span>반영</span></div>
  {mrow('ef-logo-naver.png', 'NAVER', '김종욱 멘토', '네이버 검색 백엔드·AI', '10-25 Webex 약 2시간 서비스 검증. 지원자 분석 범위, 면접관 콘솔 완성도, 지원자 화면 동선까지 DevFit 전반을 실사용 관점에서 점검', ['조직 저장소 프로젝트도 지원자 분석 대상으로 연결', '면접관 콘솔 아이콘·공용 UI 정비, 모바일 하단 탭 추가', '면접관 랜딩에 콘솔 3단계 예시 데모 (채용 생성 → 접수·분석 → 면접 브리프)', '지원자 화면에서 모의면접을 준비의 첫 행동으로 배치'])}
  {mrow('ef-logo-kakao.svg', 'kakao', '한유일 멘토', '카카오 백엔드 · 면접관 경험', '중간·어려움 난이도는 "충분히 괜찮다"는 평가. 다만 쉬움 난이도는 코드 사실 확인 수준이라 실제 면접에서는 나오지 않는 질문. 면접관은 구조를 묻고 꼬리질문으로 파고든다는 조언', ['난이도·유형 분리로 저난도 추론형 질문 <b>1/8 → 7/9</b>', 'AI 코치 응답 잘림 수정 (출력 상한 1,280 → 8,192 토큰)', '모의면접 음성 답변·음성 꼬리질문 도입', '재로그인 시 비공개 레포 권한이 사라지던 문제 해소'])}
  {mrow('ef-logo-samsung.svg', 'SAMSUNG', '김한빛 멘토', '삼성전자 출신 · 팀 담당 멘토', '매주 정기 멘토링으로 질문 생성 로직·품질 평가 하네스·프롬프트 개선안을 주 단위로 검토. CI/CD 구성과 운영 비용 구조 점검', ['8축 루브릭 기반 질문 품질 평가 하네스 구축', '프롬프트 버전 A/B 비교 후 개선판 채택', '근거 diff 판별로 근거 밖 단정 질문 차단', '평가 결과를 다음 주 프롬프트 수정에 반영'])}
  {mrow('ef-logo-basakan.png', '바삭한소프트', '김준엽 대표', '바삭한소프트 공동대표 · 게임 개발', 'CS와 프로젝트 경험의 비중은 기업 인재상에 따라 상이. 포트폴리오 면접에서는 "왜 그 기술을 선택했는지, 그 선택이 최선이었는지"를 많이 물음. 자사는 이미 지원자 GitHub를 AI로 검토 중이라는 경쟁 관점의 지적', ['결정 이유·트레이드오프 질문 유형과 현업 평가 방식의 일치 확인', '"Claude Code에 링크를 넘기면 된다"는 반론을 비교 실험으로 검증', '본인 커밋만 선별 · 코드에 없는 식별자 질문 서버 폐기로 차별화'])}
</div>""", source='한유일 멘토 09-07 녹취(68분) · 김한빛 멘토 정기 멘토링 · 김종욱 멘토 10-25 Webex · 바삭한소프트 대표 10-26 이메일 회신'))
APX.note('''[부록 · 11-10 사용자 지시로 본편에서 이동] 현업 면접관과 게임사 대표에게 서비스를 검토받고 반영했습니다. 카카오 한유일 멘토님이 쉬운 질문은 실제 면접에서 안 나온다고 지적하셔서 저난도 추론형 질문을 8개 중 1개에서 9개 중 7개로 늘렸습니다. 담당이신 삼성 출신 김한빛 멘토님과는 매주 만나 질문 품질 평가 하네스를 다듬었고, 기술면접이 까다로운 게임 개발 분야는 바삭한소프트 김준엽 대표님께 직접 여쭤 "왜 그 선택이었는지"를 묻는다는 답을 받았습니다.

근거: 한유일 멘토 09-07 녹취(feedback/01_녹취/2026-09-07_한유일멘토.txt, 68분) · 대응 feedback/05_세션별분석/2026-09-07_한유일멘토_대응현황.md (난이도·유형 분리 09-09 운영 반영, 저난도 반사실 질문 1/8→7/9 — ⛔ «12%→78%» 표기 금지(ppt-dev 관리), 음성 입력 BE 15e9e5d 등).
김한빛 멘토 = 팀 담당 멘토, 매주 정기 멘토링(사용자 확인 2026-11-06) · 09-22 CI/CD·비용 멘토링도 김한빛 멘토(사용자 확인). 반영 3건은 질문 품질 루프 기록: 8축 루브릭 평가(09-02) → 결함 31건 수정(09-08) → 프롬프트 v11·v12 A/B(10-15) → v13(10-16) · 근거 diff 판별 BE 48d58e7/f5bad96(10-24) — 출처 feedback/05_세션별분석/2026-08-20_중간평가_대응현황.md #2, 2026-09-22_CICD멘토링_대응현황.md #11. 개별 항목을 김한빛 멘토 한 분의 지적으로 단정하지 말 것(«정기 멘토링에서 함께 검토»).
김종욱 멘토 10-25 Webex «Dozer 팀 - 서비스 검증» 12:55~15:04 — 발언 기록 없음. 반영 4건은 사용자 지시(11-08)로 «미팅 직후 커밋»을 피드백 반영으로 넣은 것: 조직 저장소 연결 BE edeaee8(10-27, 박천웅) · 면접관 콘솔 정비 FE 6ec85b8(10-26) · 면접관 랜딩 데모 FE 4958c81(10-26) · 모의면접 우선 배치 FE c8a41b2(10-28) — 4건 모두 origin/prod 조상 확인(merge-base). 커밋 메시지에 멘토 언급 없음 → 미팅→반영 인과는 팀 주장(사용자 진술, claims.md C9 등록 11-08).
조언 칸(11-08 사용자 지시 «그냥 좀 써놔»): 발언 기록이 없어 반영 4건에서 거꾸로 적은 검토 주제(분석 범위·콘솔 완성도·화면 동선)임 — 멘토 발언 인용 아님, 따옴표 쓰지 않음.
⛔ 멘토 발언을 지어내 인용하지 말 것. Q&A «무슨 지적이었나» → «서비스 전반을 검증받고, 그 직후 면접관 콘솔과 지원자 분석 범위를 손봤다»까지만. 조언 칸에 멘토 발언 문장을 넣지 않음.
바삭한소프트: 김준엽 공동대표(이메일 서명 «바삭한소프트 김준엽», 공동대표 김준엽·차상근 — 아시아타임즈 2025-05-29·minimap 인터뷰). 10-23 한양대 청소년 비즈쿨 특강 → 10-26 이메일 회신. 회신 전제: 최근 1년은 기술면접을 직접 주도하지 않음 → 질문 품질 근거로 쓰지 않고 "현업 평가 방식"과 "경쟁 반론"으로만. 반론 비교 실험: 링크만 준 범용 AI 근거 0/18 · 레포를 읽힌 Claude Code 30/32 · DevFit 28/28 (collect/E-compare.md). 로고: 나무위키 문서의 회사 로고(원 출처 basakansoft.com, 현재 접속 불가).
로고: 회사 로고는 소속 표시로만 — 회사가 DevFit을 쓰거나 후원한다는 뜻이 아님. «각 회사에서 면접관 경험» · «전체 검토»는 claims.md C4. «기술면접이 까다로운 게임 개발» = C5 («가장» 금지).
추가 반영 항목 근거(collect/I-feedback-patterns.md §1-2): 한유일 09-07 → AI 코치 출력 상한 1280→8192 BE c5a3ac7(당일) · 음성 STT·TTS·음성 꼬리질문 BE 98ebb0f 등(09-16 운영) · private scope 보존 FE 61fbe10·BE 7399ff1(09-09·09-16). 김준엽 «CS·프로젝트 비중은 인재상 따라 상이»·«자사는 GitHub를 AI로 검토» = 10-26 회신 요지(05-현장검증.md §3). 김한빛 «주간 개선 루프»는 매주 멘토링 + 하네스 개선 이력(사용자 진술 11-06) 기반 서술.''')

def docimg(src, alt, ratio, cap=''):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="docimg" style="aspect-ratio:{ratio}"><img src="assets/{src}" alt="{alt}">{c}</div>'

import os as _os
BIZ_SRC = 'cert-biz.png' if _os.path.exists(_os.path.join(_os.path.dirname(OUT), 'assets', 'cert-biz.png')) else ''
def stackdoc(src, alt, cap, left, top, rot, z):
    return f'<div class="sd" style="left:{left}px;top:{top}px;transform:rotate({rot}deg);z-index:{z}"><img src="assets/{src}" alt="{alt}"><span class="tag">{cap}</span></div>'
pat = [('patent-a.png', '10-2026-0214808', '선별'), ('patent-b.png', '10-2026-0214809', '생성'), ('patent-c.png', '10-2026-0214811', '음성')]
S.append(shell('Effect', '<span class="purple">사업자등록 · 통신판매업 신고 · 직업정보제공사업 신고 · 상표 출원</span>', f'''
<div class="ef-d3">
  <figure><img src="assets/{BIZ_SRC}" alt="사업자등록증"><figcaption><b>사업자등록증</b>도저랩스 · 개업 2026-09-02</figcaption></figure>
  <figure><img src="assets/cert-mail.png" alt="통신판매업 신고증"><figcaption><b>통신판매업 신고증</b>제2026-서울서초-3702호 · 11-02</figcaption></figure>
  <figure><img src="assets/cert-job.png" alt="직업정보제공사업 신고확인증"><figcaption><b>직업정보제공사업 신고</b>서울청 제2026-31호 · 10-19</figcaption></figure>
  <figure><img src="assets/ef-trademark.png" alt="DevFit 상표 출원공고결정서 (제42류, 출원번호 40-2026-0177374)"><figcaption><b>상표 출원공고 결정</b>DevFit · 제42류 · 40-2026-0177374</figcaption></figure>
</div>''', source='증빙 원본 스캔·캡처 그대로 (자르거나 가리지 않음) · 상표는 출원공고 결정 단계 · 직업안정법 근거 조문은 부록 A16'))
S.note('''[≈10초] 결제를 받으려면 서류가 필요했습니다. 사업자등록과 통신판매업 신고를 마쳤고, 채용공고를 모아 보여 주는 서비스라 직업안정법에 따라 직업정보제공사업 신고도 10월 19일에 마쳤습니다. DevFit이라는 이름은 상표로 출원해 출원공고 결정까지 받았습니다.

[증빙] 사업자등록증(640-21-02214, 개업 2026-09-02, 서초세무서) · 통신판매업 신고증(제2026-서울서초-3702호, 11-02) · 상표 출원공고결정서(DevFit, 제42류, 출원번호 40-2026-0177374, 지식재산처 2026-11-06 발송, 상표법 제57조, 출원인 박천웅, 원본 ASM/devfit_출원공고결정서.pdf 1쪽) 원본 그대로(자르지 않고 가리지 않음).
상표: 출원공고 결정 = 심사 통과 후 공고 단계(이의신청 기간 남음), 등록 아님 → «출원공고 결정»까지만. ⛔ «상표 등록» 금지. ⛔ «매출» · «공동대표» 금지.
44·45 합침(11-11 사용자 지시 «44,45 합쳐»). 법 조문은 부록 A16.

[직업정보제공사업 신고 · 법률 멘토링 메모 — Q&A용]
직업정보제공사업 신고확인증: 서울청 제2026-31호(10-19). 근거 법조 직업안정법 제2조의2 제8호·제23조(법률 제20121호, 2024. 1. 23. 일부개정, 2024. 7. 24. 시행), law.go.kr에서 2026-11-06 그대로 복사. 신고확인증 본문에도 «직업안정법 제23조»가 적혀 있음. 공고 수(플랫폼 5 + 기업 사이트 24)는 prep/JobPostingFetchService BOARDS 5 + CorporateSiteRegistry 24.
법률 멘토링: «법무법인 백상 김재철 변호사», 소마 공식 «[자유 멘토링] Dozer(도저)팀 법률멘토링» 2026-11-05(자문 계약 아님). «기출문제 크롤링·가공 = 저작권 침해 해당 없음»은 구두 검토 의견 → «법률 멘토 검토 의견»으로만. «출원 전 공개 기술 → 특허 공지예외주장 신청» 조언도 같은 멘토링의 구두 조언(특허법 제30조).
개인정보 보호 조치: §30 처리방침 · §22 선택 동의 · §29 토큰 AES/GCM · §21 탈퇴 시 물리 삭제. ⛔ «개인정보 보호법 완전 준수»·«위반 없음»·«법률 검토 통과» 금지. 처리방침에 OpenAI 국외 이전 등 미반영(collect/K-compliance.md §1).
순서 주의: 신고(10-19)가 멘토링(11-05)보다 먼저 → «멘토링 결과로 신고했다»고 말하지 않음. ⛔ 외부 법무법인 자문으로 말하지 않음 (claims.md C6). 같은 내용 부록 A16.''')

spec = [('patent-spec-a.png', '선별'), ('patent-spec-b.png', '생성'), ('patent-spec-c.png', '음성')]
S.append(shell('Effect', '핵심 기술 3건 <span class="purple">특허 출원</span>: 질문 선별 · 질문 생성 · 음성 답변 평가', f'''
<div class="ef-dp">
  <div class="l"><div class="hd">출원번호통지서 (2026-11-01)</div>
    {''.join(f"""<div class="nt" style="left:{i*34}px;top:{38+i*168}px;z-index:{i+1}"><img src="assets/{f}" alt="{n} 출원번호통지서"><span class="tag">{k} · {n}</span></div>""" for i, (f, n, k) in enumerate(pat))}
  </div>
  <div class="r"><div class="hd">특허 명세서</div>
    {''.join(f"""<div class="sp" style="left:{i*120}px;top:{38+i*22}px;z-index:{i+1};transform:rotate({(i-1)*1.6}deg)"><img src="assets/{f}" alt="{k} 특허 명세서 첫 장"><span class="tag">{k}</span></div>""" for i, (f, k) in enumerate(spec))}
  </div>
</div>''', source='출원번호통지서 원본 캡처 · 명세서는 출원 제출본 docx 첫 장 렌더링 (특허/A_면접질문선별, B_면접질문생성, C_음성모의면접) · 출원 단계'))
S.note('''[≈10초] 핵심 기술은 특허 3건으로 출원했습니다. 커밋에서 면접 질문을 고르는 방법, 근거를 대조해 질문을 만드는 방법, 음성 대화로 답변을 평가하는 방법입니다. 왼쪽이 출원번호통지서, 오른쪽이 명세서입니다.

[증빙] 출원번호통지서 3건(2026-11-01): 10-2026-0214808(코드 저장소 기반 면접 질문 선별 방법 및 시스템) · 10-2026-0214809(코드 저장소 기반 면접 질문 생성 방법 및 시스템) · 10-2026-0214811(음성 대화 기반 면접 답변 평가 방법 및 시스템). 출원인 김건우, 발명자 김건우 박천웅 노재원, 심사청구(무) 공개신청(무).
명세서 이미지는 devfit/특허/ 아래 제출본 docx를 LibreOffice로 렌더링한 첫 장.
⛔ 특허 «등록»·«회사 특허» 금지 (출원 단계, 출원인 김건우 개인). 청구항 요지는 부록 A9.''')

APX.append(shell('Appendix · A16', '채용공고를 보여 주는 서비스의 <span class="purple">직업정보제공사업 신고</span> 근거', """
<div class="ef-lawa">
  <div class="ef-law-doc"><img src="assets/cert-job.png" alt="직업정보제공사업 신고확인증"><span class="tag">신고확인증 · 서울청 제2026-31호</span></div>
  <div class="ef-law-act">
    <h4>직업안정법</h4>
    <p><b>제2조의2(정의)</b> 8. "직업정보제공사업"이란 신문, 잡지, 그 밖의 간행물 또는 유선ㆍ무선방송이나 컴퓨터통신 등으로 구인ㆍ구직 정보 등 직업정보를 제공하는 사업을 말한다.</p>
    <p><b>제23조(직업정보제공사업의 신고)</b> ① 직업정보제공사업을 하려는 자(제18조에 따라 무료직업소개사업을 하는 자와 제19조에 따라 유료직업소개사업을 하는 자는 제외한다)는 고용노동부장관에게 신고하여야 한다. 신고 사항을 변경하는 경우에도 또한 같다.</p>
    <p>② 제1항에 따른 신고 사항, 신고 절차, 그 밖에 신고에 필요한 사항은 대통령령으로 정한다.</p>
    <span class="src">법률 제20121호, 2024. 1. 23., 일부개정 · 국가법령정보센터 원문</span>
  </div>
</div>""", source='신고확인증 원본 그대로 (자르거나 가리지 않음) · 직업안정법 [법률 제20121호, 2024. 1. 23., 일부개정] 국가법령정보센터 원문'))
APX.note('''[부록 · 11-11 사용자 지시] DevFit은 채용 플랫폼 5곳과 기업 채용 사이트의 채용공고를 가져와 보여 주므로 직업안정법 제2조의2 제8호의 직업정보제공사업에 해당하고, 제23조에 따라 신고했습니다(신고확인증 서울청 제2026-31호, 10-19). 본편에서는 36쪽 서류 장의 ③.
⛔ «법률 검토 통과»·«외부 법무법인 자문» 금지(claims.md C6). 법률 멘토링·저작권 검토 의견 관련 Q&A 메모는 36쪽 서류 장 노트 끝.''')


# ---------- 시장 규모 (11-11 사용자 지시: TAM·SAM·SOM 표, B2C·B2B 하이브리드) ----------
S.append(shell('Effect', '<span class="purple">시장 규모</span> 분석', '''
<div class="ef-one">
  <div class="ef-circ">
    <div class="c tam"><em>TAM</em><b>약 1,132억 원</b><span>개발자 채용 전체 · 구직자 준비 + 기업 검증</span><code>구직자 38.8만 명 × 23,700원<br>+ 입사지원 520만 건 × 2만 원</code></div>
    <div class="c sam"><em>SAM</em><b>약 143억 원</b><span>돈을 쓰는 구간</span><code>취업 준비 지출 42.9% × 92억<br>+ 면접 단계 10% × 1,040억</code></div>
    <div class="c som"><em>SOM</em><b>약 4억 원</b><span>3년 내 목표</span><code>B2C 전환 1%<br>+ B2B SAM 3%</code></div>
  </div>
  <div class="ef-one-r">
    <div class="ef-one-k">
      <div><small>연간 개발 직군 입사지원</small><b>약 520만 건</b><i>사람인 · 점핏 2025 상반기 260만 건 × 2</i></div>
      <div class="op">÷ 13.4회</div>
      <div class="hi"><small>면접을 준비하는 개발자 구직자</small><b>약 38.8만 명</b><i>1인 평균 입사지원 13.4회 (한경협 2025)</i></div>
    </div>
    <div class="ef-ue-h">B2C 유료 전환 시나리오 <span>(가정 · 1인 3개월 구독 23,700원)</span></div>
    <div class="ef-sc"><span>1.0%</span><i style="width:20%"></i><b>약 9,200만 원</b><small>약 3,881명 · 초기 목표</small></div>
    <div class="ef-sc"><span>2.0%</span><i style="width:40%"></i><b>약 1.84억 원</b><small>약 7,761명 · 대학 · 부트캠프 제휴 포함</small></div>
    <div class="ef-sc"><span>5.0%</span><i class="top" style="width:100%"></i><b>약 4.6억 원</b><small>약 19,403명 · 기업용 제품 연계 시</small></div>
  </div>
</div>''', source='점핏 "2025 상반기 개발자 채용 리포트" · 한국경제인협회 2025 구직자 조사(평균 입사지원 13.4회) · 잡코리아 콘텐츠LAB 2025(대졸 취준생 42.9% 취업 사교육 이용, N=485) · B2B 단가·면접 비율·점유율은 내부 가정'))
S.note('''[≈22초] 시장 규모는 B2C와 B2B를 합쳐 하나로 봤습니다. 한 해 개발 직군 지원 520만 건을 구직자는 준비하고 기업은 검증하니, 전체 시장은 약 1,132억 원입니다. 실제로 돈을 쓰는 구간으로 좁히면 약 143억 원, 3년 안에 약 4억 원이 목표입니다. 구직자만 보면, 520만 건을 1인 평균 지원 13.4회로 나눠 연 38만 8천 명이고, 1%만 3개월 구독해도 약 9,200만 원, 대학·부트캠프 제휴까지 2%면 약 1억 8천만 원입니다.

분해(Q&A): TAM = B2C 92억 + B2B 1,040억 · SAM = B2C 39.5억(42.9% 지출층) + B2B 104억(면접 단계 10%) · SOM = B2C 0.92억(1%) + B2B 3.1억(SAM 3%). 11-11 사용자 지시 «하나의 TAM·SAM·SOM으로, 기존 지표(38.8만 명 · 전환 시나리오)도 살리고». 원 크기는 금액 비례 아님.

계산: 2,601,390 × 2 ≈ 520만 건(하반기 동일 가정) ÷ 13.4회 ≈ 38.8만 명(최종보고서와 같은 계산).
B2C: TAM 388,100 × 23,700원(3개월 무료 체험 후 7,900 × 3) ≈ 92.0억 · SAM × 42.9% ≈ 166,500명 ≈ 39.5억 · SOM 1% = 3,881명 × 23,700 ≈ 0.92억(최종보고서 시나리오와 같은 값, 2%·5%는 부록 A11).
B2B: TAM 520만 × ₩2만 = 1,040억 · SAM × 10%(서류 통과율 가정) = 52만 건 = 104억 · SOM 3% ≈ 3.1억(3년). collect/H-market.md §3 «3년 SOM 약 3억 원대 방어 가능»(상향식 0.8~5.2억 · 내부 고객 수 기반 3.1억 일치).
합산: TAM 92 + 1,040 = 1,132억 · SAM 39.5 + 104 = 143.5억 → «약 143억» · SOM 0.92 + 3.1 = 4.0억. 11-11 사용자 지시 «둘이 합쳐서 개발자 채용시장 전체, DevFit Platform 기준».
보수안(₩1만·5%): B2B TAM 520억 · SAM 26억 · SOM 0.8억 → 플랫폼 TAM 612억 · SAM 65억 · SOM 1.7억 — Q&A용.
출처 등급: 520만 건(점핏 리포트 직접, ×2는 가정) · 13.4회(한경협 2025) · 42.9%(잡코리아 콘텐츠LAB N=485, 비대표 표본 🟡) · ₩2만·10%·3%는 내부 가정(⚙, research/R1-ef-market.md #3 «써도 되나 가정 표기 유지»). 기간 주의: B2C SOM은 연 단위 1% 시나리오, B2B SOM은 3년 목표 → 합계는 «3년 내 목표»로만 말함.
⛔ «매출 전망»으로 말하지 않음 — 시장 규모. ⛔ 5년 SOM 27억 · TAM $2.8B 금지(재현 불가). ⛔ «52만 명» 아님 → «52만 건».''')

# ---------- 차별점 — 면접 대비 서비스 지형 + 개발자 서비스 비교 ---------- (근거: collect/G-competitors.md)
def df_row(name, sub, cells, me=False):
    tds = ''.join(f'<td class="n">{c}</td>' if c in ('–', '확인 안 됨') else f'<td>{c}</td>' for c in cells)
    return f'<tr class="{"me" if me else ""}"><td>{name}<small>{sub}</small></td>{tds}</tr>'

GEN = ['사람인 AI 모의면접', '잘봐요', '뷰인터', '티오(TIO)', 'Final Round AI', 'Huru', 'Yoodli', 'Big Interview']
DEV = ['점핏', '프로그래머스', '프로그래머스 비즈니스', '코드트리', '구름 Devth', '인프런 모의면접', '꼬꼬면', '테크톡', 'Tech Check', 'F-Lab']

S.append(shell('Effect', '채용·구직 서비스는 1,484곳이지만 <span class="purple">개발자 취업 준비 전용</span>은 국내 10곳', f'''
<div class="df-land">
  <div class="df-g"><div class="df-gh"><b>채용 · 구직 정보 서비스</b><em>1,484<i>곳</i></em><small>고용노동부 신고 직업정보제공사업체 · 2025.10.31 기준</small></div>
    <div class="df-base"><span>면접 대비 · 취업 준비 AI 조사 9곳</span>질문 근거는 이력서 · 자소서 · 채용 공고(JD)</div>
    <div class="df-chips">{' '.join(f'<span>{x}</span>' for x in GEN)} <span class="off">Google Interview Warmup</span></div></div>
  <div class="df-g dev"><div class="df-gh"><b>개발자 취업 준비 전용</b><em>10<i>곳</i></em><small>국내 운영 중 · 채용 1 · 코딩테스트 4 · 기술면접 4 · 멘토링 1</small></div>
    <div class="df-sq">{'<span class="kr"></span>'*10}</div>
    <div class="df-base"><span>내 GitHub 코드로 질문</span>공개 페이지 기준 0곳</div>
    <div class="df-chips">{' '.join(f'<span>{x}</span>' for x in DEV)}</div></div>
</div>
<div class="df-me">DevFit: 내가 짠 커밋으로 하는 개발자 취업 준비<small>공고 수집 · 근거 코드 질문 · 음성 모의면접 · 지원 일정 관리</small></div>''', source='각 서비스 공개 페이지 기준 (2026-11-05 · 11-07 확인) · 국내외 36건(국내 18 · 해외 18) 조사, 2026-11 기준'))
S.note('''[≈12초] 고용노동부에 신고된 채용·구직 정보 서비스만 1,484곳입니다. 면접 대비 서비스도 많지만 대부분 이력서와 자소서, 채용 공고를 보고 일반 직무 질문을 만듭니다. 개발자만을 위한 취업 준비 서비스는 저희가 찾은 국내 운영 중 서비스로 10곳이고, 채용 1곳, 코딩테스트 4곳, 기술면접 4곳, 멘토링 1곳입니다. 그중 지원자 본인의 GitHub 코드로 질문을 만드는 곳은 공개 페이지에서 확인되지 않았습니다.

오른쪽 10곳 근거: collect/G4-dev-jobprep.md (research-2, 접근 2026-11-07, 공개 검색 기준 — 노트·Q&A에서는 «최소 10곳»). 채용 점핏 · 코딩테스트 프로그래머스 연습·프로그래머스 비즈니스(기업용)·코드트리·구름 Devth(기업용) · 기술면접 인프런 모의면접·꼬꼬면·테크톡(iOS 개인 앱)·Tech Check(iOS 개인 앱) · 멘토링 F-Lab. 기업 서비스만 세면 8곳. 제외: 랠릿(IT 전반)·프로그래머스 커리어(접속 불가)·백준(재오픈 연기)·solved.ac(403)·원티드·사람인·그룹바이·코멘토(범용)·부트캠프·강의·오픈소스·개인 레포. «0곳» = 국내 운영 중 10곳 공개 페이지 기준. F-Lab «Github 상시 코드 리뷰»는 사람 멘토 리뷰라 질문 생성 아님. 해외 Greenroom은 레포 단위 분석을 공개(다음 장 비교표) → ⛔ «세계 유일»·«GitHub 기반은 DevFit뿐». 1,484곳(신고 사업장)과 10곳(조사한 제품)은 세는 단위가 다름 → «1,484곳 중 10곳» 금지.

근거: 1,484곳 = 공공데이터포털 «고용노동부_직업정보제공사업자 현황_20251031»(https://www.data.go.kr/data/15068779/fileData.do, 접근 2026-11-07, CSV 1,484행 직접 집계 — collect/G3-jobprep-count.md). 직업안정법 §23 신고 사업장 수 = 채용·구직 정보 사이트·앱·매체 운영자 전체(사람인·잡코리아·인크루트·링커리어·리멤버·코멘토·인프랩 포함, 건설 인력·지역 구인지도 포함). DevFit(제2026-31호)은 기준일 이후 신고라 미포함. ⛔ «취업 준비 서비스 1,484개»·«면접 대비 1,484곳» 금지 — 채용·구직 정보 서비스로만. 오른쪽 10곳과는 세는 단위가 다름.
면접 대비 목록: last-dance/collect/G-competitors.md §1 (공개 페이지, 접근일 2026-11-05).
- 일반 면접: 사람인(이력서+사람인 공고 한정) · 잘봐요(3자 블로그 출처) · 뷰인터(공식 본문 비어 있음) · Final Round AI · Huru · Yoodli · Big Interview. Google Interview Warmup은 2026-04 종료(3자 보도) → 취소선.
- (이전 판) 개발자 기술면접 전용 5곳: 인프런 모의면접·꼬꼬면(국내) · Greenroom · interviewing.io · Pramp·Aced(해외) — 다음 장 비교표의 열.
- 숫자 8(면접 대비)은 «조사 범위(G-competitors §1) 안의 개수»이지 시장 전체 집계가 아님 — Q&A에서 그렇게 답할 것. 범용 AI(ChatGPT·Claude)·고용주용(Emble·depthhire)·오픈소스는 세지 않음. 인프런 모의면접은 collect/G2-inflearn.md(2026-11-07, research-2) 반영.
- 티오(TIO, 일반 취업 준비 AI): 공고 링크 분석 O, 업로드한 경험 자료·자기소개서 중심 → 코드 기반 질문 X (최종보고서 경쟁 표, 서비스 소개 페이지). 개발자 전용 아님이라 왼쪽 그룹.
- 전체 조사 범위는 최종보고서와 같은 «국내외 36건(국내 18·해외 18), 2026-11 기준». 이 장의 9곳·10곳은 그중 화면에 올린 것.
- 회사 로고는 쓰지 않음(BUILD.md 로고 예외는 멘토 소속 4개사뿐, 경쟁사 상표 사용 리스크).
- «국내 상용 2곳» = 조사 범위 내 표현. techGiterview·Giterview(오픈소스·학생 프로젝트)는 상용 아님 — 질문 받으면 존재를 인정.
⛔ «유일»·«최초»·«경쟁자 없음» 금지.''')

COLS = ['DevFit', '티오(TIO)', '인프런 모의면접', '꼬꼬면', 'Greenroom', 'interviewing.io', 'Pramp · Aced']
DC_ROWS = [
    ('GitHub 레포 연동 분석', ['제공', '–', '–', '–', '제공', '–', '–']),
    ('팀 레포에서 내가 짠 커밋만 선별', ['제공', '–', '–', '–', '확인 안 됨', '–', '–']),
    ('비공개 레포 분석', ['제공', '–', '–', '–', '확인 안 됨', '–', '–']),
    ('질문마다 근거 코드 · 원문 링크', ['제공', '–', '–', '–', '확인 안 됨', '–', '–']),
    ('공고 링크로 본문 분석', ['제공', '제공', '–', '–', '–', '–', '–']),
    ('공고 캡처 이미지에서도 본문 추출', ['제공', '–', '–', '–', '–', '–', '–']),
    ('공고 자격요건 ↔ 내 코드 어필 포인트', ['제공', '–', '–', '–', '–', '–', '–']),
    ('기출 · 문항 은행 기반 질문', ['제공', '–', '제공', '제공', '확인 안 됨', '–', '제공']),
    ('음성 모의면접 · 꼬리질문', ['제공', '–', '제공', '제공', '제공', '제공', '일부']),
    ('지원 일정 · 마감 관리', ['제공', '–', '–', '–', '–', '–', '–']),
    ('기업 면접관용 검증 콘솔', ['제공', '–', '–', '–', '–', '–', '–']),
]
DC_CLS = {'제공': 'y', '일부': 'p', '없음': 'x', '–': 'x', '확인 안 됨': 'p'}
DC_MARK = {'제공': '✓', '일부': '△', '없음': '✕', '–': '✕', '확인 안 됨': '△'}
def dc_table():
    head = '<tr><th>기능</th>' + ''.join(f'<th class="{"me" if i == 0 else ""}">{c}</th>' for i, c in enumerate(COLS)) + '</tr>'
    body = ''.join('<tr><td>' + f + '</td>' + ''.join(f'<td class="{DC_CLS[v]}{" me" if i == 0 else ""}">{DC_MARK[v]}</td>' for i, v in enumerate(vals)) + '</tr>' for f, vals in DC_ROWS)
    return f'<table class="dc-t"><thead>{head}</thead><tbody>{body}</tbody></table>'

S.append(shell('Effect', '개발자 대상 서비스 비교: <span class="purple">내 커밋 · 근거 코드 · 공고 가져오기</span>', f'''
<div class="dc-wrap">
  <div class="dc-box">{dc_table()}</div>
  <div class="ef-line" style="margin-top:18px">국내외 36건 조사 결과, 본인 커밋 선별 · 공고 교차 · 근거 코드 대조를 함께 하는 서비스 <span>확인되지 않음 (2026-11 기준)</span></div>
</div>''', source='각 서비스 공개 페이지 기준 (2026-11-05 · 인프런 11-07 확인 · 티오 최종보고서 경쟁 표) · DevFit 칸은 운영 코드 기준'))
S.note('''[≈15초] 개발자 서비스들도 질문은 기출 문항 은행이나 레포 단위에서 나옵니다. 인프런 모의면접은 기출 패턴과 이력서로 묻습니다. DevFit은 팀 프로젝트에서도 내가 짠 커밋만 골라, 질문마다 그 diff와 원문 링크를 붙입니다. 공고는 링크만 넣으면 본문을 바로 가져오고, 캡처 이미지여도 읽어 냅니다. 채용 플랫폼 5곳과 기업 채용 사이트 24곳, 29곳을 지원합니다.

조사 범위: 국내외 36건(국내 18·해외 18), 2026-11 기준 — 최종보고서와 같음. 하단 문장은 보고서 «…서비스는 확인되지 않았다(2026년 11월 기준)»와 같은 수위. ⛔ «유일»·«최초»·«경쟁자 없음» 금지.
- 티오(TIO): 일반 취업 준비 AI. 공고 링크 분석 O(✓), 질문 근거는 업로드한 경험 자료·자기소개서 → 코드 기반 질문 X. 그 밖의 행은 공개 페이지에서 확인 안 함(✕ = 부재 증명 아님). 출처: 최종보고서 각주 20 «티오(TIO) - 취업 준비 AI 어시스턴트» 서비스 소개 페이지.
- 공고 행 이름을 «공고 링크로 본문 분석»으로 바꿈(티오도 링크 분석). DevFit의 29곳(플랫폼 5 + 기업 24) 지원은 노트로만.
근거: last-dance/collect/G-competitors.md §1 (공개 페이지, 접근일 2026-11-05) · collect/G2-inflearn.md (2026-11-07). DevFit 칸은 운영 코드(BE origin/prod 500f4af · FE 2c46ce6) 기준.
- 인프런 모의면접(inflearn.com/ai-interviews): AI 면접관, 개발자 전용(백엔드·FDE·프론트엔드), 기출 문항 은행 + 이력서·포트폴리오 PDF(선택), 음성·꼬리질문·아바타, 한국어. GitHub·커밋·공고 URL 입력은 공개 페이지에 없음. 첫 1회 무료, 이후 1회 12,000원. 출시 시점은 관계자 LinkedIn 글뿐(«2026년 하반기»로만). 인프랩이 랠릿을 운영하지만 연동 언급 없음.
- DevFit «기출» = 공개 기출 1,880건(11-08 운영 DB, 1차 853 + 2차 1,027).
- Greenroom(usegreenroom.app): Pro $10에 «GitHub repo analysis»(레포 단위 → «일부»), 음성. 본인 커밋 구분·질문별 근거·특정 공고·한국어는 공개 페이지에 없음. Q&A 최우선 대비.
- 꼬꼬면(kokomen.kr): 개발자 특화, 이력서·포트폴리오 + 현직 출신 500+ 문항 은행, 음성, 한국어. GitHub 언급 없음.
- interviewing.io: 익명 사람 모의면접 + AI 면접관, 오디오+채팅. Pramp(2021 Exponent 인수 → Aced): 동료 1:1 매칭(«일부»)·질문 은행.
표 읽는 법(화면 범례는 사용자 지시로 뺌, 11-07 · ✓/✕ 표기도 사용자 지시): ✓ = 공개 페이지·운영 코드로 확인 · ✕ = 공개 페이지에서 확인되지 않음(기능 부재를 증명하지 않음) · △ = 부분 확인(사용자 지시 11-07): Greenroom 커밋 선별·비공개 레포·근거 코드·문항 은행은 레포를 읽는다는 것까지만 공개, Pramp는 동료 1:1(AI 꼬리질문 아님). 한국어 행은 사용자 지시로 뺌(인프런·꼬꼬면 O, Greenroom 확인 불가).
행 근거(11-07 추가): GitHub 연동 = Greenroom «Ari reads your repos»(G1) · 본인 커밋 선별 = GithubService author: 필터(D3), Greenroom은 레포 단위까지만 공개 · 비공개 레포 = includePrivate 증분 동의(users.github_scopes, V38) · 공고 자동 수집 = prep/JobPostingFetchService BOARDS 5 + CorporateSiteRegistry 24(D1·D2) · 캡처 이미지 = /candidate/interview-preps/extract-image(vision OCR) — 경쟁 5곳 공개 페이지에 공고 URL·이미지 입력 언급 없음(사람인은 자사 공고 URL만 받지만 이 표에 없음) · 어필 포인트 = prep/AppealService · 지원 일정·마감 = journey/ 여정 트래커(운영 중) · 면접관 콘솔 = /recruit/*(Greenroom «For teams — Soon», interviewing.io «For employers» 링크만 → –).\n⛔ «AI는 레포를 못 읽는다» 금지(ChatGPT 커넥터·Claude 연동은 읽음). ⛔ 타사 비방 금지 — 공개 페이지 사실만, «–»는 부재가 아님.''')

# ---------- ④ 비즈니스 모델 (11-11 사용자 지시: B2C·B2B 하이브리드, B2C 근거 = 사용자 인터뷰) ----------
S.append(shell('Effect', 'B2C 구독과 B2B 이용료의 <span class="purple">하이브리드 수익 모델</span>', '''
<div class="ef-hy">
  <div class="ef-hy-c">
    <div class="ef-hy-h"><b>B2C</b>개발자 구직자 · 운영 중</div>
    <div class="ef-tiers">
      <div class="ef-tier"><em>무료</em><b>0원</b><span>기본 분석 하루 10회</span><small>공고 분석 · 근거 코드 질문 · 텍스트 모의면접</small></div>
      <div class="ef-tier on"><em>Plus 구독</em><b>7,900원<i>/ 월</i></b><span>3개월 무료 체험</span><small>음성 모의면접 · 자기소개서 작성 · 우선 처리</small></div>
      <div class="ef-tier"><em>추가 생성권</em><b>1,900원<i>/ 1회</i></b><span>공고 1건 질문 추가 생성</span><small>6개월 유효 · 공고 단위 구매</small></div>
    </div>
    <div class="ef-hy-q"><div class="ef-hy-qh">B2C 지불 의향 · 사용자 인터뷰 (개발자 구직자, 프론트엔드 인턴 지원 경험)</div>
      <p>"면접 1회 기준 만원 정도, 준비기간 동안이면 2만원까지는 결제할 의향이 있습니다"</p>
      <small>Plus 월 7,900원 · 추가 생성권 1,900원은 이 범위 안</small></div>
  </div>
  <div class="ef-hy-c b2b">
    <div class="ef-hy-h"><b>B2B</b>기업 채용팀 · 개발 완료</div>
    <div class="ef-tier ent"><em>DevFit Enterprise</em><b>지원자 단위<i>이용료</i></b><span>지원자 1명 분석마다 과금</span><small>가격은 기업 파일럿 결과로 확정</small></div>
    <div class="ef-hy-ue">
      <div><span>분석 1회 변동비</span><b>약 330원</b></div>
      <div><span>코드 변경 없는 재분석</span><b>0원</b></div>
      <small>B2C · B2B가 같은 분석 엔진이라 원가 구조 공유</small>
    </div>
  </div>
</div>
<div class="ef-pay"><b>토스페이먼츠 계약 완료</b><span>추가 생성권 단건 결제 11-02 운영 반영</span></div>''', source='요금 구성: devfit.app/pricing 운영 화면 · 최종보고서 「요금제와 결제」 · 변동비: 최종보고서 「단위 경제성」(CloudWatch 실측) · 사용자 인터뷰: 개발자 구직자 1대1 인터뷰(중간평가 발표 수록)'))
S.note('''[≈20초] 수익 모델은 B2C와 B2B를 함께 가져가는 하이브리드입니다. 개인은 기본 분석을 하루 10회 무료로 쓰고, 음성 모의면접과 자기소개서는 월 7,900원 Plus 구독, 같은 공고 질문을 더 받으면 1,900원 추가 생성권입니다. 인터뷰한 구직자는 면접 1회에 만 원, 준비 기간 전체로는 2만 원까지 낼 의향이 있다고 했고, 지금 가격은 그 범위 안입니다. 기업은 지원자 1명을 분석할 때마다 이용료를 냅니다. 둘 다 같은 엔진이라 분석 1회 원가는 약 330원이고, 결제는 토스페이먼츠와 계약을 마쳤습니다.

B2C 근거 원문: 중간평가 IR 덱(vendor/irdeck_new.html 1485~1501행) «지원자 A · 20세, 프론트엔드 인턴 지원 경험 · 1대1 인터뷰» — Q «얼마까지 결제할 의향이 있으신가요?» → A «면접 1회 기준 만원 정도, 준비기간 동안이면 2만원까지는 결제할 의향이 있습니다». 같은 덱 B2C 칸 «인터뷰 기준 지불 의향은 면접 1회 1만원, 준비기간 이용권 2만원». 원 녹취 파일은 저장소에서 찾지 못함 → 출처는 중간평가 덱 수록본. 화자는 역할로만.
⚠️ 한계(Q&A): 인터뷰 1명의 진술 의향(실제 결제 아님). 보조 근거: 다른 구직자 인터뷰(feedback/04_사용자인터뷰)에서 «학원에 가서 도움을 받았다» · AI에 월 약 90만 원 지출 — 이미 취업 준비에 돈을 쓰는 층. 같은 인터뷰의 «이미 쓰는 AI로 준비하면 된다» 반론(O1)은 범용 AI 비교 실험(근거 실존 0/18 vs 28/28)으로 답.
B2B 과금: collect/J-b2b-pilot.md «지원자 1명당 종량, 가격은 원가 ₩1,000~2,000에서 바텀업, 파일럿 결과로 확정». 시장 장의 1인 2만 원은 시장 크기 계산용 가정이지 확정 가격이 아님.
변동비: 최종보고서 단위 경제성 — 약 330원(저장소 3개, CloudWatch 실측) · 20개 상한 약 1,404원 · 재분석 0원 · Plus 7,900원 ≈ 분석 약 24회분. 요금 화면은 부록 A7 · 이전 판 장표(pricing.png)에서 뺌.
토스페이먼츠 계약 완료(11-11 사용자 지시, claims.md C3). ⛔ «구독 매출»·«매출»로 말하지 않음. ⛔ B2B 가격 숫자를 확정가처럼 말하지 않음. ⛔ «60% 절감» 비교 금지.
Q&A: «결제는 열려 있고 매출은 아직 0» (claims.md C3).''')

# ---------- B2B — DevFit Enterprise (11-10 사용자 지시: 서비스 소개서 기준) ----------
S.append(shell('Effect', 'DevFit Enterprise: B2C와 분리된 <span class="purple">면접관 전용 검증 도구</span> (개발 완료)', '''
<div class="ef-ent">
  <div class="ef-ent-l">
    <table class="ef-vs">
      <thead><tr><th></th><th>B2C 준비</th><th class="b">B2B Enterprise</th></tr></thead>
      <tbody>
        <tr><td>쓰는 사람</td><td>지원자 본인</td><td class="b">기업 면접관</td></tr>
        <tr><td>목적</td><td>내 코드로 면접 준비</td><td class="b">지원자가 알고 짰는지 검증</td></tr>
        <tr><td>질문 생성</td><td>내가 고른 공고 × 내 저장소</td><td class="b">지원서마다 따로 · 같은 입력 = 같은 결과</td></tr>
        <tr><td>보는 곳</td><td>지원자 앱</td><td class="b">면접관 콘솔만</td></tr>
        <tr><td>더하는 기능</td><td>모의면접 · 학습</td><td class="b">ATS(칸반 · 평가표 · 일정 메일) · 근거 커밋 Diff</td></tr>
      </tbody>
    </table>
    <div class="ef-leak"><h4>면접 질문이 유출되지 않는 구조</h4><ol>
      <li><b>공통 문제은행 없음</b>: 질문은 지원자 본인 커밋에서 지원서마다 생성</li>
      <li><b>데이터 분리</b>: 면접관 질문은 콘솔에서만, 지원자 화면 · B2C 질문과 공유하지 않음</li>
      <li><b>미리 준비해도 무방</b>: 늘어나는 건 자기 코드 설명력, 곧 검증하려는 역량</li>
    </ol></div>
  </div>
  <div class="ef-ent-r">
    <div class="ef-shot s1"><img src="assets/ef-ent-10.jpg" alt="DevFit Enterprise 면접 브리프 화면 — 프로젝트 요약과 핵심 질문"></div>
    <div class="ef-shot s2"><img src="assets/ef-ent-12.jpg" alt="DevFit Enterprise 커밋 근거 화면 — 지원자 커밋 Diff와 원본 링크"></div>
  </div>
</div>
<div class="ef-season"><div class="ef-season-r"><span>B2C</span><div class="m"><i class="">1월</i><i class="">2월</i><i class="on">3월</i><i class="on">4월</i><i class="">5월</i><i class="">6월</i><i class="">7월</i><i class="">8월</i><i class="on">9월</i><i class="on">10월</i><i class="">11월</i><i class="">12월</i></div><em>공채 시즌 약 4개월에 수요 집중</em></div><div class="ef-season-r b"><span>B2B</span><div class="bar">기업 수시 · 경력 채용은 연중</div><em>나머지 <b>8개월</b> 비성수기 보완</em></div></div>''', source='DevFit Enterprise 서비스 소개서(2026-11, devfit.app/enterprise.pdf) 6·10·12쪽 · 화면: 서비스 소개서(가상 데이터) · 분리 구조: BE recruit 패키지 · 공개 지원 API(/apply) 응답'))
S.note('''[≈20초] 기업용 DevFit Enterprise는 B2C와 쓰는 사람도, 목적도, 화면도 다릅니다. B2C는 지원자가 자기 코드로 준비하는 도구이고, Enterprise는 면접관이 지원자가 알고 짰는지 확인하는 도구입니다. 그래서 면접 질문이 지원자에게 새는 구조가 아닙니다. 공통 문제은행이 없고, 질문은 지원자 본인 커밋에서 지원서마다 따로 만들며, 면접관 콘솔에서만 보입니다. 지원자가 자기 코드를 미리 공부해 오면, 그게 바로 저희가 확인하려는 역량입니다. 채용 관리 기본 기능 위에 근거 커밋으로 하는 코드 면접을 얹었습니다. 면접관은 면접 10분 전에 브리프로 프로젝트 요약과 핵심 질문을 보고, 질문마다 근거가 된 커밋 diff와 GitHub 원본 링크를 확인합니다. 개발을 마쳤습니다. 개인 구직자 수요는 상·하반기 공채 시즌 약 4개월에 몰리고 나머지 8개월은 비성수기입니다. 기업 채용은 수시·경력 채용으로 1년 내내 이어지니, B2B가 이 8개월을 메웁니다.

비성수기 8개월: 11-11 사용자 지시(claims.md C12). 공채 시즌 = 상반기 3~4월 · 하반기 9~10월(대기업 공채 관행, 월 표기는 예시). 최종보고서도 «채용 시즌에 따른 사용량 변동»을 사업 위험으로 적음. 기업 수시·경력 채용 확대 근거: research/R4-hiring-market.md E6(한은 2026-08 «수시·경력직 선호»). DevFit 자체 월별 사용량 계절성 실측은 아직 4개월치라 수치로 말하지 않음.

출처: /Users/aiden/dev/teams/ASM/DevFit_enterprise_서비스소개서.pdf (2026-11 발행, 30쪽, devfit.app/enterprise.pdf). 포지셔닝 «ATS에 GitHub를 더하다»(표지) · 코드 면접 5요소(6쪽) · 면접 브리프(10쪽: 프로젝트 요약·핵심 질문 3~4개·관련 개념) · 커밋 근거(12쪽: 본인 커밋 필터링·Diff·해시·GitHub 원본 링크). 동의한 공개 저장소만 분석, AI는 합불을 판정하지 않음.
화면: 소개서 10·12쪽을 PDF에서 렌더해 잘라 씀(다시 그리지 않음). 소개서 고지 «본 소개서의 화면은 가상의 목업 데이터» → 화면 속 지원자·기업명은 실제 아님.
Q&A 비교(소개서 29쪽, 2026-11 각 사 공개 가이드 기준, DevFit vs 그리팅 · 나인하이어): GitHub 코드 분석 · 본인 커밋 Diff = DevFit만 제공 / 칸반 · 평가표 · 일정 메일 = 셋 다(나인하이어 평가표 일부) / 외부 채용 플랫폼 지원서 연동 = DevFit 제공 예정 / Google 캘린더 연동 = DevFit 미지원. 이 두 줄을 숨기지 않음.
상태(11-10 사용자 메타): «B2C·B2B 둘 다 개발 완료. B2B는 개발 완료한 지 얼마 안 돼 기업들에 서비스 소개서를 보내 보는 중.» 근거: 최종보고서 43쪽 «MVP 개발 완료, 서비스 소개서로 기업 평가와 시장 검증 진행». 현업 검토(면접관·게임사 대표)는 부록 A15 참조.
Q&A 전용(장표·발화에서는 말하지 않음): 운영은 아직 비공개(출시 예정), 유료 고객·LOI·계약 0 — 물으면 사실대로.
⛔ «고객 확보»·«파일럿 진행 중»·«LOI 체결» 금지. ⛔ 평가표 점수는 면접관이 매기는 것 — «점수로 합격 판정» 뉘앙스 금지. 허용 표현은 «합불 판정 없음 · 최종 판단은 사람».
유출 방어 근거(중간평가 심사의견 #17 «면접 질문을 면접자에게 유출하는 플랫폼» 대응, feedback/05_세션별분석/2026-08-20_중간평가_대응현황.md D-2 · 00_공방표 A7):
- 지원서마다 별도 생성: ApplicationAnalysisService → bedrock.generateRepositoryInterviewKit (EVALUATION 모드, 결정적 — 같은 입력 = 같은 결과).
- 데이터 분리: BE origin/main recruit 패키지는 B2C 질문 테이블(QuestionBank·StudySet·PrepAnalysis·InterviewPreparation)을 참조하지 않음(11-11 git grep 0건). 공개 지원 API ApplyController(/api/apply/{token})에 질문·interviewKit 응답 없음(11-11 확인). B2C·B2B 프론트는 S3 배포 분리.
- 한계(Q&A, 숨기지 않음): 면접관 수용성 데이터 0건. 같은 지원자가 B2C로 자기 저장소를 분석하면 비슷한 주제의 질문을 볼 수는 있음 → 답: 그 준비가 곧 자기 코드 설명력이고 외워서 통과할 수 없음, 꼬리질문은 면접관이 당일 답변을 보고 고름. 11-02 멘토 제안 «커버리지 어시스턴트» 재정의는 방향.
⛔ «유출 불가능»·«완벽 차단» 같은 절대 표현 금지 → «유출되지 않는 구조»까지.
''')

S.append(shell('Effect', '향후 6개월 목표: 가입 <span class="purple">275명</span>, B2B 첫 유료 1곳', f'''
<div class="ef-stage"><div class="ef-road">
  <div class="ef-num"><b>275<small>명</small></b><span>B2C 6개월 가입 목표<em class="ef-tag">추정치</em></span><i>범위 135~382명 · 지금 광고비 수준 전제</i></div>
  <div class="panel" style="padding:44px 46px"><div class="section-line"><span class="num" style="background:#005ce6">B</span><span>B2B 개발 완료 이후 계획</span></div>
    {steps([('2026-11', '회고형 파일럿 2곳'), ('2027-01~02', '실전 파일럿 2~3곳'), ('2027-03', '첫 유료 1곳')])}
    <div class="small-copy" style="margin-top:22px;text-align:center;font-size:22px">성과 지표: 면접관 질문 채택률</div></div>
</div></div>''', source='275명 = 최근 주 7.4명 × 26주 + 현재 83명 (추정) · B2B 로드맵은 계획 단계'))
S.note('''[≈15초] 앞으로 6개월 목표입니다. B2C는 지금 속도면 가입 275명이고, 범위는 135명에서 382명입니다. B2B는 개발을 마쳤고, 11월 회고형 파일럿 2곳에서 시작해 내년 3월 첫 유료 1곳까지 가고, 면접관이 우리 질문을 실제로 채택하는 비율을 잽니다.

출처: 275명 = 최근 주 7.4명 × 26주 + 83명, 범위 135~382, 현 수준 광고비 전제 · B2B 로드맵 collect/J. 가입자 답변률 목표 25% (Q&A용).
11/10 18시까지 의향서가 오면 «파일럿 의향서 1건(비구속)»으로 교체.
⛔ «고객 확보»·«파일럿 진행 중»·«MOU» 금지 (현재 LOI·MOU·계약 0).''')

S.append(shell('Effect', 'B2C(운영 중)와 B2B(개발 완료)를 잇는 <span class="purple">하나의 채용 플랫폼</span>: 엔진은 공유, 질문은 분리', f'''
<div class="ef-col">
  <div class="ef-vision"><img src="assets/vision-diagram.png" alt="DevFit Platform 비전 — B2C 준비와 B2B 검증을 하나의 개발자 채용 플랫폼으로"></div>
  <div class="ef-chips"><span>① B2C 준비 · 운영 중 · 결제 LIVE</span><span class="dev">② B2B Enterprise · 개발 완료</span><span>③ 공고 29곳 수집 · 지원 여정 트래커</span></div>
</div>''', source='비전 그림은 중간발표와 동일 · 초록 점 = 운영 중 · 빈 점 = 개발 완료'))
S.note('''[≈15초] 중간발표에서 말한 비전입니다. 지원자가 자기 코드로 준비하는 B2C와, 면접관이 근거로 검증하는 B2B를 같은 분석 엔진 위에서 하나의 개발자 채용 플랫폼으로 잇습니다. 엔진은 같지만 면접관 질문과 지원자 질문은 서로 공유하지 않습니다. B2C는 공고 수집과 지원 일정 관리까지 운영 중이고, B2B는 개발을 마쳤습니다.

출처: Devfit/brand/platform/vision-diagram.png (중간발표와 같은 그림). B2B는 «면접관이 빠뜨린 확인 관점을 알려 주는 커버리지 어시스턴트»로 재정의(중간평가 #17 질문 유출 우려 대응 + 11-02 멘토링 제안).''')

# ---------- 부록 A22~A26: DevFit Enterprise 사용 설명서 (11-11 사용자 지시 «b2b 상세 내용을 어펜딕스에 사용설명서처럼») ----------
def entm(pages, cols):
    cells = ''.join(f'<figure><img src="assets/ef-entm-{n:02d}.jpg" alt="DevFit Enterprise 서비스 소개서 {n}쪽"><figcaption>소개서 {n}쪽</figcaption></figure>' for n in pages)
    return f'<div class="ef-entm c{cols}">{cells}</div>'
ENTM_SRC = 'DevFit Enterprise 서비스 소개서(2026-11 발행, 30쪽, devfit.app/enterprise.pdf) 원본 페이지 · 화면은 가상 데이터'
ENTM = [
    ('A22', '사용 설명서 1: <span class="purple">ATS + GitHub</span> 구성과 분석 범위', [6, 7, 8, 14], 2,
     '코드 면접 5가지 조건(이력서·공고 매칭 · 저장소 선별 · 본인 커밋 추출 · 질문 의도와 평가 가이드 · 구조화된 평가) → ATS 필수 기능 위에 GitHub 분석을 더한 구성 → ATS 기본 기능 4가지와 GitHub가 더하는 4가지(저장소 자동 매칭 · 연관 저장소 분석 · 브리프 자동 생성 · 코드 근거 평가) → 지원자 사전 동의 · 공개 저장소만 · AI는 합불 판정을 하지 않음 · 블라인드.'),
    ('A23', '사용 설명서 2: <span class="purple">코드 면접</span> (브리프 · 질문 가이드 · 커밋 근거)', [10, 11, 12, 13], 2,
     '면접 브리프(면접 10분 전 프로젝트 요약 · 핵심 질문 3~4개 · 관련 개념 · 원클릭 복사) → 질문 의도와 평가 가이드(출제 의도 · 배경지식 · 우수 답변 기준 · 심화 꼬리질문) → 질문마다 실제 커밋 Diff와 GitHub 원본 링크 → 지원자 목록에서 바로 펼쳐 보는 질문.'),
    ('A24', '사용 설명서 3: <span class="purple">채용 관리(ATS)</span> 대시보드 · 지원 접수 · 전형 단계', [16, 17, 18, 19, 20, 21], 3,
     '맞춤형 대시보드 → 로그인 없는 지원 페이지(사전 동의 2건) → 지원자 리스트 → 칸반 단계 설정 → 칸반 보드 → 지원자 상세 뷰.'),
    ('A25', '사용 설명서 4: <span class="purple">협업 평가</span> 코멘트 · 평가표 · 일정 · 메일', [22, 23, 24, 25, 26, 27], 3,
     '팀 코멘트와 타임라인 → 맞춤형 평가표(척도 · 가중치) → 팀 평가 리포트 → 블라인드 평가와 평가 요청 → 면접 일정 관리 → 안내 메일.'),
    ('A26', '사용 설명서 5: <span class="purple">블라인드 채용</span>과 기존 ATS 비교', [28, 29], 1,
     '블라인드 채용 설정 → 기존 ATS(그리팅 · 나인하이어)와 기능 비교표. 비교표에서 «외부 채용 플랫폼 지원서 연동 = 제공 예정», «Google 캘린더 연동 = 미지원» 두 줄을 숨기지 않음.'),
]
for _a, _t, _pages, _cols, _flow in ENTM:
    APX.append(shell(f'Appendix · {_a}', 'DevFit Enterprise ' + _t, entm(_pages, _cols), source=ENTM_SRC))
    APX.note(f"""[부록 · Q&A용] DevFit Enterprise 서비스 소개서를 페이지 그대로 실은 사용 설명서입니다. 흐름: {_flow}

본편 B2B 장(Enterprise)과 같은 소개서. 상태는 «개발 완료» — ⛔ «운영 중»·«고객 확보»·«파일럿 진행 중» 금지. 화면 속 회사·지원자는 가상 데이터. 면접 질문은 면접관 콘솔에서만 보이고 지원자 화면·B2C 질문과 공유하지 않음(본편 B2B 장 노트 근거).""")

# ================= 부록 → s5_appendix.py (11-07 사용자: 부록은 ppt-start 전담) =================
