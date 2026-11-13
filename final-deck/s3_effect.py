# -*- coding: utf-8 -*-
# 3부 — Effect + 부록 A4·A5·A8·A10
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
.ef-d3{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;align-items:start;margin:auto 0}.ef-d3 figure{margin:0;text-align:center}.ef-d3 img{height:560px;max-width:100%;object-fit:contain;display:block;margin:0 auto;border:1px solid var(--line);box-shadow:0 18px 40px rgba(20,16,40,.14);background:#fff}.ef-d3 figcaption{margin-top:16px;font-size:16px;font-weight:700;color:var(--muted)}.ef-d3 figcaption b{display:block;font-size:22px;font-weight:900;color:var(--ink);margin-bottom:2px}
.ef-dj{display:grid;grid-template-columns:auto 1fr;gap:44px;align-items:center;margin:auto 0}.ef-dj .ef-law-doc{transform:none}.ef-dj .ef-law-doc img{height:600px;width:auto}.ef-dj .r{display:flex;flex-direction:column;gap:22px}.ef-dj .why{font-size:24px;font-weight:700;line-height:1.55;color:var(--ink);background:var(--purple-pale);border-radius:18px;padding:22px 28px;word-break:keep-all}.ef-dj .why small{display:block;font-size:16px;font-weight:900;color:var(--purple);margin-bottom:6px}.ef-dj .why b{color:var(--purple)}.ef-dj .ef-law-act p{font-size:17px}.ef-dj .src{display:block;margin-top:10px;font-size:14px;color:var(--muted);font-family:inherit}
.ef-dp{display:grid;grid-template-columns:1fr 1fr;gap:40px;flex:1;min-height:0}.ef-dp .l,.ef-dp .r{position:relative;min-height:620px}.ef-dp .hd{font-size:18px;font-weight:900;color:var(--purple)}.ef-dp .nt,.ef-dp .sp{position:absolute}.ef-dp .nt img{width:600px;display:block;border:1px solid var(--line);box-shadow:0 14px 34px rgba(20,16,40,.16);background:#fff}.ef-dp .sp img{height:560px;display:block;border:1px solid var(--line);box-shadow:0 14px 34px rgba(20,16,40,.16);background:#fff}.ef-dp .l .nt,.ef-dp .l .hd{margin-left:var(--ofl)}.ef-dp .r .sp,.ef-dp .r .hd{margin-left:var(--ofr)}.ef-dp .l{--ofl:calc((100% - 668px)/2)}.ef-dp .r{--ofr:calc((100% - 640px)/2)}.ef-dp .tag{position:absolute;left:12px;top:-14px;background:var(--ink);color:#fff;font-size:14px;font-weight:800;padding:5px 11px;border-radius:4px;white-space:nowrap}

/* 직업정보제공사업 장 법률 (11-11) */
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
CSS += '\n/* marketing revision: evidence and product metrics */\n.ef-mr-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;flex:1;min-height:0}\n.ef-mr-grid.wide{grid-template-columns:1.7fr 1fr}\n.ef-mr-card{background:white;border:1px solid var(--line);border-radius:18px;padding:30px 34px;min-height:0}\n.ef-mr-card h3{font-size:32px;margin:0 0 18px;line-height:1.3;font-weight:900}\n.ef-mr-card p{font-size:25px;line-height:1.55;margin:14px 0;color:var(--muted);font-weight:700}\n.ef-mr-card .label{color:var(--purple);font-size:23px;font-weight:900;margin-bottom:18px}\n.ef-mr-number{font-size:102px;line-height:1.1;font-weight:900;color:var(--purple-deep);letter-spacing:-.055em}\n.ef-mr-number small{font-size:30px;margin-left:10px;letter-spacing:-.02em}\n.ef-mr-card .sub{font-size:20px;color:var(--muted);line-height:1.55;margin-top:15px}\n.ef-mr-card .rule{border-top:1px solid var(--line);padding-top:22px;margin-top:23px}\n.ef-mr-pair{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:26px 0}\n.ef-mr-pair b{font-size:39px;display:block;margin-top:8px;color:var(--ink)}\n.ef-mr-pair span{font-size:22px;color:var(--muted);font-weight:700}\n.ef-mr-highlight{padding:20px 24px;background:var(--purple-pale);border-left:5px solid var(--purple);font-size:25px;font-weight:800;line-height:1.5;margin-top:20px}\n.ef-mr-chart{width:100%;height:540px;object-fit:contain;display:block}\n.ef-mr-chart.accounts{height:580px}\n.ef-mr-aside{display:flex;flex-direction:column;gap:22px}\n.ef-mr-aside .ef-mr-card{flex:1;display:flex;flex-direction:column;justify-content:center}\n.ef-mr-bars{display:flex;flex-direction:column;gap:25px;margin-top:28px}\n.ef-mr-bar{display:grid;grid-template-columns:160px 1fr 150px;align-items:center;gap:16px;font-size:25px;font-weight:800}\n.ef-mr-track{height:34px;background:#efedf6;border-radius:4px;overflow:hidden}\n.ef-mr-fill{height:100%;background:var(--purple)}\n.ef-mr-bar b{text-align:right;font-size:27px}\n.ef-mr-strip{display:flex;height:62px;border-radius:6px;overflow:hidden;margin:22px 0 30px;color:white;font-size:26px;font-weight:900}\n.ef-mr-strip div{display:flex;align-items:center;justify-content:center}\n.ef-mr-three{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;flex:1}\n.ef-mr-three .ef-mr-number{font-size:88px}\n.ef-mr-three .ef-mr-card{display:flex;flex-direction:column}\n.ef-mr-three .ef-mr-card .rule{margin-top:auto}\n.ef-mr-table{width:100%;border-collapse:collapse;font-size:24px}\n.ef-mr-table td,.ef-mr-table th{text-align:left;padding:17px 8px;border-bottom:1px solid var(--line)}\n.ef-mr-table th{font-size:21px;color:var(--muted)}\n.ef-mr-table td:last-child{text-align:right;font-weight:900;color:var(--purple-deep)}\n/* Presentation copy: secondary explanations are retained in speaker notes. */\n.ef-marketing-slide .folio{display:none}\n.ef-marketing-slide .ef-mkt-photo{gap:20px;justify-content:flex-start}\n.ef-marketing-slide .ef-mkt-photo .goods{height:390px;object-fit:contain;object-position:center;background:#eeecf2}\n.ef-marketing-slide .ef-mkt-photo .fair{height:330px;object-fit:contain;background:#eeecf2}\n.ef-marketing-slide .ef-mkt-photo .goods{height:auto;flex:1 1 0;min-height:0}\n.ef-mkt-photo .cap{flex:none;margin-top:-16px;font-size:13px;font-weight:600;line-height:1.3;color:var(--muted);text-align:center}\n.ef-marketing-slide .ef-mr-card p,.ef-marketing-slide .ef-mkt-channel p{color:var(--ink)}\n.ef-cash-head{font-size:80px;font-weight:900;color:var(--purple-deep);letter-spacing:-.045em;margin:22px 0 34px}\n.ef-cash-head span{color:#aba3bd;font-size:60px;margin:0 12px}\n.ef-cash-compare{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin:20px 0 35px}\n.ef-cash-compare h3{font-size:27px}\n.ef-cash-track{height:40px;background:#eeecf3;border-radius:4px;margin-bottom:20px}\n.ef-cash-track>div{height:100%;background:var(--purple);border-radius:4px}\n.ef-cash-compare b{font-size:42px;font-weight:900}\n.ef-cash-compare p{font-size:22px;line-height:1.5}\n.ef-cash-table{width:100%;border-collapse:collapse;margin-top:30px;font-size:26px}\n.ef-cash-table td,.ef-cash-table th{padding:21px 12px;text-align:right;border-bottom:1px solid var(--line)}\n.ef-cash-table td:first-child,.ef-cash-table th:first-child{text-align:left}\n.ef-cash-table th{font-size:24px}\n.ef-cash-table td:last-child{font-weight:900;color:var(--purple-deep)}\n.ef-cash-table .accent{background:var(--purple-pale);font-weight:900}\n.ef-perf-chart{width:100%;height:420px;object-fit:contain;display:block;margin:8px 0}\n.ef-perf-table{width:100%;border-collapse:collapse;font-size:24px;margin:26px 0}\n.ef-perf-table td,.ef-perf-table th{padding:20px 9px;border-bottom:1px solid var(--line);text-align:right}\n.ef-perf-table td:first-child,.ef-perf-table th:first-child{text-align:left}\n.ef-perf-table td:last-child{font-weight:900;color:var(--purple-deep)}\n.ef-perf-table th{font-size:23px}\n.ef-perf-note{font-size:23px;line-height:1.6;color:var(--ink);font-weight:700;margin-top:20px}\n.ef-performance-kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:25px}\n.ef-performance-kpis .ef-mr-card{padding:25px 30px}\n.ef-performance-kpis .metric{font-size:56px;font-weight:900;color:var(--purple-deep);line-height:1.25;letter-spacing:-.04em}\n.ef-performance-kpis .metric small{font-size:29px}\n.ef-performance-kpis .flow{font-size:27px;font-weight:800;margin-top:18px;color:var(--ink)}\n.ef-performance-kpis .change{font-size:25px;color:var(--purple-deep);font-weight:900;margin-top:14px}\n.ef-performance-summary{display:grid;grid-template-columns:1.6fr 1fr;gap:26px;flex:1}\n.ef-performance-summary .ef-mr-card{padding:25px 30px}\n\n.ef-ad-period{font-size:23px;font-weight:700;color:var(--ink);margin:0;line-height:1.4}\n.ef-ad-chart{width:100%;height:335px;object-fit:contain;display:block}\n.ef-ad-observations{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}\n.ef-ad-observation{border:1px solid var(--line);background:white;border-radius:14px;padding:23px 27px}\n.ef-ad-observation .label{font-size:23px;font-weight:900;color:var(--purple);margin-bottom:13px}\n.ef-ad-observation h3{font-size:29px;line-height:1.35;margin:0 0 12px;font-weight:900}\n.ef-ad-observation p{font-size:23px;line-height:1.5;margin:0;font-weight:700}\n.ef-ad-observation b{color:var(--purple-deep)}\n.ef-ad-ai{display:grid;grid-template-columns:0.9fr 1.6fr;gap:28px;flex:1;min-height:0}\n.ef-ad-ai .ef-mr-number{font-size:83px}\n.ef-ad-table{font-size:25px;width:100%;border-collapse:collapse;margin-top:15px}\n.ef-ad-table th,.ef-ad-table td{padding:16px 10px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}\n.ef-ad-table th{font-size:21px;font-weight:800}\n.ef-ad-table th:first-child,.ef-ad-table td:first-child{text-align:left}\n.ef-ad-table tr.selected{background:var(--purple-pale);color:var(--purple-deep);font-weight:900}\n.ef-ad-ai .ef-mr-highlight{font-size:25px;margin-top:28px}\n.ef-ad-region{display:grid;grid-template-columns:1fr 1.35fr;gap:28px;flex:1;min-height:0}\n.ef-ad-region .ef-mr-bar{grid-template-columns:150px 1fr 150px;margin:18px 0;font-size:25px}\n.ef-ad-region .ef-mr-bars{gap:25px;margin:35px 0}\n.ef-ad-region .ef-mr-track{height:40px}\n.ef-ad-region .ef-mr-number{font-size:94px;margin:25px 0 16px}\n.ef-feature-top{display:grid;grid-template-columns:1fr 1fr;gap:25px}\n.ef-feature-bottom{display:grid;grid-template-columns:repeat(3,1fr);gap:25px;flex:1}\n.ef-feature-card{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px}\n.ef-feature-card h3{font-size:29px;margin:0 0 14px;font-weight:900;line-height:1.4}\n.ef-feature-card p{font-size:23px;font-weight:700;margin:12px 0 0;line-height:1.5}\n.ef-feature-number{font-size:85px;line-height:1.1;font-weight:900;color:var(--purple-deep);letter-spacing:-.05em}\n.ef-feature-number small{font-size:28px;margin-left:10px}\n.ef-feature-top .ef-feature-card{display:grid;grid-template-columns:1.2fr 1fr;align-items:center;gap:20px;min-height:240px}\n.ef-feature-top .ef-feature-number{text-align:right;font-size:96px}\n.ef-feature-bottom .ef-feature-card{display:flex;flex-direction:column;justify-content:center;background:linear-gradient(180deg,#fff 25%,#f6f4ff 100%)}\n.ef-feature-bottom .ef-feature-number{margin:18px 0;font-size:96px}\n.ef-plan-grid{display:grid;grid-template-columns:1.12fr 1fr;gap:28px;flex:1;min-height:0}\n.ef-plan-creative{background:#30264e;border-radius:18px;padding:35px 38px;color:white;display:flex;flex-direction:column}\n.ef-plan-creative .label{font-size:24px;font-weight:800;color:#d8cdff;margin-bottom:23px}\n.ef-plan-creative h3{font-size:44px;line-height:1.3;margin:0 0 25px;font-weight:900}\n.ef-plan-scenes{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:10px 0 30px}\n.ef-plan-scene{border:1px solid #70638e;border-radius:10px;background:#40345e;padding:24px 23px;min-height:145px}\n.ef-plan-scene b{font-size:26px;display:block;margin-bottom:14px}\n.ef-plan-scene span{font-size:24px;line-height:1.5;display:block}\n.ef-plan-cta{font-size:28px;font-weight:900;color:#33264f;background:#e7ddff;border-radius:8px;padding:22px 25px;margin-top:auto;text-align:center}\n.ef-plan-measure{display:grid;grid-template-rows:1fr 1fr;gap:24px;min-height:0}\n.ef-plan-measure .ef-mr-card{flex:1;padding:29px 32px}\n.ef-plan-measure h3{font-size:31px}\n.ef-plan-measure .ef-mr-highlight{font-size:25px;margin-top:15px}\n.ef-mock-current{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px;display:flex;flex-direction:column}\n.ef-mock-current .label,.ef-mock-value .label,.ef-mock-next .label{font-size:23px;font-weight:900;color:var(--purple);margin-bottom:20px}\n.ef-mock-kpis{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin:12px 0 8px;flex:1}\n.ef-mock-kpi{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:24px;padding-right:28px;border-right:1px solid var(--line)}\n.ef-mock-kpi:last-child{border:0;padding-right:0}\n.ef-mock-kpi h3{font-size:29px;line-height:1.4;margin:0;font-weight:900}\n.ef-mock-kpi p{font-size:25px;line-height:1.4;margin:0;font-weight:700}\n.ef-mock-kpi .number{font-size:118px;line-height:1;font-weight:900;white-space:nowrap;color:var(--purple-deep);letter-spacing:-.05em}\n.ef-mock-kpi .number small{font-size:26px;letter-spacing:-.02em;margin-left:10px}\n.ef-mock-direction{display:grid;grid-template-columns:1fr 1.2fr;gap:28px;flex:1;min-height:0}\n.ef-mock-value{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 32px;color:var(--ink)}\n.ef-mock-value .label{color:var(--purple);margin-bottom:16px}\n.ef-mock-core-body{display:grid;grid-template-columns:1fr 1.2fr;gap:45px;align-items:center}\n.ef-mock-value h3{font-size:36px;line-height:1.3;font-weight:900;margin:0}\n.ef-mock-value p{font-size:24px;line-height:1.5;font-weight:700;margin:0}\n.ef-mock-value .emphasis{font-size:23px;line-height:1.5;font-weight:800;color:var(--purple-deep);margin-top:12px}\n.ef-mock-next{background:white;border:1px solid var(--line);border-radius:16px;padding:30px 34px;display:flex;flex-direction:column}\n.ef-mock-next h3{font-size:40px;line-height:1.35;font-weight:900;margin:8px 0 22px}\n.ef-mock-next p{font-size:25px;line-height:1.6;font-weight:700;margin:0 0 24px}\n.ef-mock-goal{font-size:28px;font-weight:900;line-height:1.4;background:var(--purple-pale);color:var(--purple-deep);border-left:5px solid var(--purple);padding:22px 24px;margin-top:auto}\n'
# MARKETING_REVISION_CSS_END

CSS += '\n/* User interview: summary, the unaltered source screenshot, and feedback. */\n.ef-interview{flex:1;min-height:0;display:flex;flex-direction:column;gap:14px}\n.ef-interview-profile{font-size:23px;font-weight:800;line-height:1.3;color:var(--ink)}\n.ef-interview-journey{display:grid;grid-template-columns:1fr 45px 1fr 45px 1fr;gap:12px;align-items:stretch;flex:none}\n.ef-interview-step{background:var(--purple-pale);border:1px solid #ded8f1;padding:13px 24px;border-radius:14px}\n.ef-interview-step>span{font-size:20px;font-weight:900;color:var(--purple-deep);line-height:1.2}\n.ef-interview-step h3{font-size:29px;font-weight:900;line-height:1.2;margin:7px 0}\n.ef-interview-step p{font-size:21px;font-weight:700;line-height:1.35;margin:0}\n.ef-interview-arrow{display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:900;color:var(--purple)}\n.ef-interview-original{margin:0;flex:none;width:100%;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}\n.ef-interview-original img{display:block;width:100%;height:auto;object-fit:contain}\n.ef-interview-findings{display:grid;grid-template-columns:1.05fr 1fr;gap:20px;flex:1;min-height:0}\n.ef-interview-card{background:white;border:1px solid var(--line);border-radius:14px;padding:16px 22px;display:flex;flex-direction:column;justify-content:center;min-height:0}\n.ef-interview-card h3{font-size:24px;font-weight:900;line-height:1.3;margin:0;color:var(--purple-deep)}\n.ef-interview-card blockquote{font-size:24px;font-weight:800;line-height:1.35;letter-spacing:-.025em;margin:10px 0 0;padding-left:16px;border-left:4px solid var(--purple)}\n.ef-interview-requests{display:grid;grid-template-columns:1fr 1.1fr;gap:20px;margin-top:12px}\n.ef-interview-request b{font-size:23px;font-weight:900;line-height:1.3;white-space:nowrap}\n.ef-interview-request p{font-size:20px;line-height:1.35;margin:7px 0 0;font-weight:700;white-space:nowrap}\n'

CSS += '\n/* 2026-11-13: region expansion flow and consolidated business evidence. */\n.ef-region-flow{display:grid;grid-template-columns:1fr 110px 1.35fr;gap:22px;flex:1;min-height:0}\n.ef-region-card{display:flex;flex-direction:column;padding:32px 30px}\n.ef-region-heading{display:flex;align-items:center;gap:18px;margin-bottom:12px}\n.ef-region-heading h3{font-size:33px;margin:0;line-height:1.25}\n.ef-region-step{display:inline-flex;background:var(--purple);color:white;font-size:29px;line-height:1.2;font-weight:900;padding:12px 18px;border-radius:10px;white-space:nowrap}\n.ef-region-card p.ef-region-period{font-size:23px;margin:0 0 26px;line-height:1.4}\n.ef-region-focus{margin:20px 0 12px}\n.ef-region-focus>span{font-size:28px;font-weight:800}\n.ef-region-card .ef-mr-number{font-size:94px;margin-top:12px}\n.ef-region-card p.ef-region-purpose{font-size:28px;line-height:1.5;margin:12px 0 24px}\n.ef-region-card .ef-mr-highlight{margin-top:auto;font-size:25px}\n.ef-region-arrow{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;color:var(--purple);font-size:25px;font-weight:900;line-height:1.4;text-align:center}\n.ef-region-arrow svg{width:96px;height:64px}\n.ef-region-card .ef-mr-bars{gap:32px;margin:42px 0 36px}\n.ef-region-card .ef-mr-bar{grid-template-columns:132px 1fr 116px;font-size:27px}\n.ef-region-card .ef-mr-track{height:42px}\n.ef-region-card .ef-mr-bar b{font-size:30px}\n.ef-region-card p.ef-region-definition{font-size:21px;margin:20px 0 0;line-height:1.4}\n.ef-foundation-grid{display:grid;grid-template-columns:1fr .94fr 1.24fr;gap:24px;flex:1;min-height:0}\n.ef-foundation-card{background:white;border:1px solid var(--line);border-radius:18px;padding:28px 26px;display:flex;flex-direction:column;min-width:0;min-height:0}\n.ef-foundation-kicker{font-size:24px;font-weight:900;color:var(--purple);margin-bottom:20px;line-height:1.3}\n.ef-foundation-card h3{font-size:32px;line-height:1.35;letter-spacing:-.035em;margin:0;font-weight:900}\n.ef-foundation-docs{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:16px;flex:1;min-height:0;margin:25px 0}\n.ef-foundation-docs.single{grid-template-columns:1fr}\n.ef-foundation-card figure{margin:0;min-width:0;text-align:center}\n.ef-foundation-docs img{display:block;object-fit:contain;width:100%;height:320px;background:#faf9fc}\n.ef-foundation-docs.single img{height:320px}\n.ef-foundation-docs figcaption{font-size:22px;line-height:1.4;margin-top:20px}\n.ef-foundation-docs figcaption b{display:block;font-weight:900}\n.ef-foundation-docs figcaption span{display:block;font-size:19px;margin-top:8px;white-space:nowrap}\n.ef-foundation-result{font-size:22px;line-height:1.4;font-weight:900;color:var(--purple-deep);padding:17px 10px;background:var(--purple-pale);border-radius:10px;text-align:center;margin-top:auto}\n.ef-foundation-trademark{display:flex;align-items:center;gap:24px;margin:0 0 26px}\n.ef-foundation-trademark img{width:150px;height:204px;object-fit:contain;background:#faf9fc;flex:none}\n.ef-foundation-trademark p{font-size:23px;line-height:1.4;margin:14px 0 0;font-weight:700}\n.ef-foundation-patents{border-top:1px solid var(--line);padding-top:22px;margin-bottom:20px}\n.ef-foundation-patents h3{font-size:31px}\n.ef-foundation-patents strong{font-size:40px;color:var(--purple-deep)}\n.ef-foundation-patent-docs{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:18px}\n.ef-foundation-patent-docs img{height:145px;width:100%;object-fit:contain;background:#faf9fc}\n.ef-foundation-patent-docs figcaption{font-size:21px;font-weight:800;line-height:1.4;margin-top:10px;white-space:nowrap}\n.ef-foundation-slide .folio{display:none}\n'

CSS += '\n/* 2026-11-13: account growth and returning users on one slide. */\n.ef-gr-grid{display:grid;grid-template-columns:1fr 1.07fr;gap:24px;flex:1;min-height:0;width:100%;height:100%}\n.ef-gr-panel{background:white;border:1px solid var(--line);border-radius:16px;padding:26px 26px 22px;min-width:0;min-height:0;display:flex;flex-direction:column}\n.ef-gr-panel h3{font-size:31px;font-weight:900;line-height:1.3;margin:0 0 10px;color:var(--ink)}\n.ef-gr-period{font-size:22px;font-weight:700;color:var(--muted);margin:0;line-height:1.4}\n.ef-gr-chart{width:100%;flex:1;min-height:0;object-fit:contain;display:block}\n.ef-gr-lead{font-size:27px;font-weight:700;line-height:1.3;margin:0 0 24px;color:var(--ink)}\n.ef-gr-lead b{color:var(--purple-deep);font-weight:900}\n.ef-gr-table{border-collapse:collapse;width:100%;font-size:23px;table-layout:fixed}\n.ef-gr-table th{font-size:19px;color:var(--muted);font-weight:800;text-align:right;padding:0 8px 14px;line-height:1.25;border-bottom:2px solid var(--ink)}\n.ef-gr-table td{padding:10px 8px;text-align:right;font-weight:700;color:var(--ink);white-space:nowrap;border-bottom:1px solid #e6e4ee;font-variant-numeric:tabular-nums;line-height:1.3}\n.ef-gr-table th:first-child,.ef-gr-table td:first-child{text-align:left}\n.ef-gr-table td:first-child{font-weight:900}\n.ef-gr-table td.d{color:var(--purple-deep)}\n.ef-gr-table td.d b{font-weight:900}\n.ef-gr-highlights{display:grid;grid-template-columns:1fr 1.2fr 1fr;gap:12px;margin-top:auto;padding-top:22px}\n.ef-gr-highlights>div{display:flex;flex-direction:column;gap:10px;padding:16px 8px 14px;background:#f6f3ff;border-radius:8px;text-align:center}\n.ef-gr-highlights strong{font-size:43px;line-height:1;font-weight:900;color:var(--purple-deep)}\n.ef-gr-highlights small{font-size:21px;font-weight:800;margin-left:5px}\n.ef-gr-highlights span{font-size:19px;line-height:1.3;font-weight:800;color:var(--ink);white-space:nowrap}\n'


# ================= 5. Effect =================
S.append(divider('05 · Effect', 'Effect', '사용자 유입, 운영 지표, 비즈니스 모델과 비전'))
S.note('''[구분] 협업과 수행 과정을 바탕으로 만든 서비스에서 어떤 성과를 확인했는지 소개합니다. 사용자 유입과 운영 지표, 비즈니스 모델, 비전으로 이어집니다.''')


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
  <div class="ef-mkt-photo"><img class="fair" src="assets/ef-fair.jpg" alt="숭실대 취업 박람회 DevFit 소개 현장"><small class="cap">숭실대 JobFair 현장 홍보</small><img class="goods" src="assets/ef-goods.jpg" alt="DevFit 팜플렛과 QR 클리커 굿즈"><small class="cap">함께 나눠준 팜플렛과 굿즈</small></div>
 </div>
</div>''', cls='ef-marketing-slide', source='Dozer, 「DevFit 최종보고서 마케팅」, 2026. Microsoft Clarity, 「CS 지식백과 진입 집계」, 2026. Meta·Google Ads, 「캠페인 내보내기」, 2026.'))
S.note('''[약 25초] 마케팅은 검색 콘텐츠, 유료 광고, SNS, 현장 홍보로 나눠 실행했습니다. CS 문서와 면접 질문에서 서비스를 접할 수 있게 했고, Meta와 Google 광고를 집행했습니다. SNS는 게시물별 유입 경로를 구분했고, 숭실대 취업 박람회에서는 팜플렛과 QR 굿즈로 직접 소개했습니다.

근거: final-report의 기존 마케팅 장표와 사진 원본. 콘텐츠 규모 172편·875문항·가이드 12종은 원본 보고서 기준. CS 진입 169세션은 cs_acquisition_summary.json, 2026-08-12~11-09 04:39 KST. 직접·내부·광고 등 모든 진입 포함이며 검색 성과로 주장하지 않음. 검색결과 referrer 확인 세션은 3건(네이버 Search Advisor 1건 제외). 박람회 날짜·배포량·가입 효과는 미확인.
광고비 3,501,256원=Meta 2,338,208+Google 1,163,048. 11/05 검증 CSV 기준이며 실제 카드 결제액·VAT 포함 청구액과 다름. 11/04 부록 A5의 광고비와 집계 시점이 다름.
기존 콜백 메일은 구축 근거만 있고 실제 발송·복귀 성과가 확인되지 않아 수행 실적 목록에 포함하지 않음.''')


S.append(shell('Effect', 'Meta 중심 집행, <span class="purple">유입 비용과 참여를 함께 고려</span>', '\n<div class="ef-mkt"><p class="ef-mkt-period">11/05 누적 집행 · Meta 233.8만 원 / Google 116.3만 원</p>\n<div class="ef-mr-strip"><div style="width:66.78%;background:#6c5ce7">Meta 66.8%</div><div style="width:33.22%;background:#3d354f">Google 33.2%</div></div>\n<div class="ef-mr-grid">\n <div class="ef-mr-card"><div class="label">Meta에 더 많은 비중을 둔 근거</div><h3>낮은 클릭 비용으로<br>서비스 유입 규모 확보</h3><div class="ef-mr-pair"><div><span>링크 클릭당 비용</span><b>110원</b></div><div><span>링크 클릭</span><b>21,318회</b></div></div><p>소재를 바꾸며 반응을 탐색하고<br>적은 단가로 넓은 접점 확보</p></div>\n <div class="ef-mr-card"><div class="label">Google에도 예산을 유지한 근거</div><h3>검색 의도가 있는 유입과<br>서비스 이용 가능성 확인</h3><div class="ef-mr-pair"><div><span>광고 클릭당 비용</span><b>571원</b></div><div><span>광고 클릭</span><b>2,038회</b></div></div><p>Google 광고로 처음 유입된<br>활성 사용자당 평균 참여 시간 <b>4분 38초</b></p></div>\n</div></div>', cls='ef-marketing-slide', source='Meta·Google Ads, 「11/05 캠페인 CSV」, 2026. Google Analytics 4, 「8/24~11/05 사용자 획득」, 2026.'))
S.note('[약 30초] 누적 집행액은 Meta가 약 3분의 2, Google이 약 3분의 1입니다. Meta는 클릭당 약 110원으로 폭넓게 서비스를 알리고 소재 반응을 탐색하는 데 활용했습니다. Google은 클릭 단가가 높지만 관측된 사용자 참여 시간이 길어, 검색 의도가 있는 유입을 함께 확인하는 채널로 설명할 수 있습니다. 실제 지표를 바탕으로 집행 비중의 타당성을 설명하는 것이며, 처음부터 2 대 1이 최적임을 실험으로 입증했다는 뜻은 아닙니다.\n근거: 03_Meta캠페인.csv 합계2,338,208원/21,318링크클릭;04_Google주별.csv 합계1,163,048원/2,038클릭. 합3,501,256원; Meta66.782%,Google33.218%. CPC109.68/570.68원. 예산계획서나 날짜별 배분 결정 로그는 미확인; 이 슬라이드는 사후 성과 해석에 따른 설명 근거. 광고 클릭 정의는 플랫폼별로 다름. GA4 05_GA4획득.csv 첫 사용자 소스/매체 ig/paid61명57초, google/cpc57명278초. 활성 사용자당 평균 참여 시간이며 세션 체류시간 아님. 측정 동의 범위의 표본이며 인과 실험 아님. Google PMax 전체를 검색광고라고 부르지 않음. Google 최신11/11 지출1,377,062원과 혼합하지 않고11/05 스냅샷 사용.')

S.append(shell("Effect", '가설 1. 새 광고를 주기적으로 추가하면 <span class="purple">노출이 늘어날 것이다</span>', '\n<div class="ef-mkt"><div class="ef-mr-card" style="padding:14px 25px"><div style="font-size:23px;font-weight:800;margin-bottom:4px">전체 광고의 일별 총 노출 · 광고 7개 집행 이력</div><img class="ef-ad-chart" style="height:380px" src="assets/mkt-ad-additions.svg" alt="전체 광고 일별 총 노출. 신규 광고 최초 노출 8/31, 9/2, 9/26, 9/29, 10/13, 10/25. 10/23 노출 재개."></div>\n<div class="ef-ad-observations">\n<div class="ef-ad-observation"><div class="label">08/31 시작 광고</div><h3>집행 초반 노출 집중</h3><p>2일 차 <b>3,172회</b><br>3일 차 273회</p></div>\n<div class="ef-ad-observation"><div class="label">10/13 신규 집행 광고</div><h3>첫날 대비 2일 차 노출 확대</h3><p>7,155회 → <b>13,635회</b><br>10/23 노출 재개 후 2일 차 34,239회</p></div>\n<div class="ef-ad-observation"><div class="label">10/25 시작 광고</div><h3>2일 차에 해당 광고 최대 노출</h3><p>15,854회 → <b>26,918회</b><br>첫날 대비 <b>69.8% 증가</b></p></div>\n</div></div>', cls="ef-marketing-slide"))
S.note("[약 35초] 먼저 집행한 광고에서 초반에 노출이 집중되는 사례를 보고, 일주일 단위로 새 소재를 넣어 초기 반응을 확보해 보자는 가설을 세웠습니다. 예를 들어 광고1은2일차3,172회였지만3일차에는273회로 줄었습니다. 이후 새 고객 광고와10월25일 광고를 추가했습니다. 새 고객 광고는첫날7,155회에서2일차13,635회로,10월25일 광고는15,854회에서2일차26,918회로 늘었습니다. 신규 광고의 집행 초반에 노출이 확대되는 현상을 다시 관찰했습니다.\n운영 의도: 사용자2026-11-11 설명의 일주일 단위 광고 추가 시도. 실제 최초 노출일은 새 고객 광고10/13,재집행10/23,10/25광고10/25. 두 광고 최초 집행일 간격은12일,재집행과10/25간격은2일이므로 정확히7일마다 집행했다고 발표하지 않음. 날짜는 업로드/편집 시각이 아닌 최초 실제 노출일. 재집행은10/15~22해당광고 노출없음 뒤10/23관측 재개를 뜻함.\ndata/troubleshooting/meta-ad-daily.csv는광고세트와광고이름·일별실적의실제Meta내보내기. 일별전체노출합666197. 그래프는광고전체합,하단은개별광고수치이므로10/25총노출26517과개별첫날15854를혼동하지않음. 새고객10/13:7155,10/14:13635,10/23:28223,10/24:34239,10/25:10663.10/25광고의10/26:26918은해당광고최대일노출. (26918/15854-1)*100=69.7868%.\n앞선모든광고에서1~2일최대였다는뜻은아님. test세트는3일차최대, test사본과오디세이는후반최대인반례도있음. 초반집중관찰사례를제시한것이며주간교체의보편적효과를입증한것이아님. 광고1중단및소재변경,예산,집행시간,타깃,학습상태를통제하지않았으므로노출감소를소재피로도만으로단정하거나플랫폼노출부스트라고설명하지않음.\n\n[2026-11-13 전체 집행 일자 대조]\nMeta 원본 CSV의 보고 기간은 2026-08-01~11-10. 집계행을 제외한 76개 광고×일 행, 광고 7개·광고 세트 6개. 노출 합계 666,197회·지출 합계 2,338,208원으로 원본 총계와 일치. 신규 광고는 해당 광고에서 처음 노출>0이 관측된 날을 뜻하며, 업로드·생성 시각이나 예약 시작일을 증명하는 자료는 아님. 08/31 광고 1, 09/02 오디세이, 09/26 test 세트의 광고, 09/29 test 사본 세트의 광고, 10/13 새 고객 광고와 새 트래픽 광고 2개, 10/25 광고. 09/02는 08/31과 같은 세트 안에서 추가된 별도 광고이므로 다음 장의 세트 비교에는 별도 행이 없음.\n09/07은 광고 1이 1회·7원으로 다시 관측된 기록. 원자료와 총 노출 합계에는 보존하되 사용자 요청으로 그래프의 별도 표시는 생략. 신규 광고 또는 수동 재집행으로 단정하지 않음. 10/23은 새 고객 광고가 10/15~22 노출이 없는 기간 후 다시 관측된 날이므로 '노출 재개'로 표시. 10/15 새 트래픽 광고와 11/01 10/25 광고에도 각각 1회 노출이 있으며 전체 일별 합계에 포함. 그래프 곡선은 모든 광고의 일별 총합이고, 각 사건 표식의 점도 그날 총합을 가리킴. 광고별 신규 일자와 첫날 노출 수를 혼동하지 않음.\n재현: scripts/build_meta_delivery_timeline.py. 근거: data/troubleshooting/meta-delivery-audit-20261113.json 및 meta-delivery-dates-20261113.csv. 모든 광고의 연속 노출 구간과 무노출 간격도 별도 기록.\n\n[최종 정정 · 2026-11-13 사용자 확인]\n10/13 신규 집행 광고는 '새 고객 광고'(10/13 광고 세트) 1개. '테스트' 세트의 새 트래픽 광고도 같은 날 처음 관측되지만 CSV의 최초 관측일만으로 신규 생성·집행을 추정할 수 없어, 이 비교표의 별도 10/13 ② 행에서 제외. 합산하지 않음.\n34쪽: 새 고객 광고 10/13 7,155회, 10/14 13,635회. 35쪽: 10/13~19 노출 20,790회, 지출 82,580원, CPM 3,972원. 전체 노출 그래프는 여전히 모든 광고를 합산한 실제 일별 총계이며 제외 기록을 총계에서 지우지 않음.\n이전 노트의 6개 세트·10/13 ①② 표기는 원자료와 이전 판의 조사 이력. 현재 비교표는 5개 세트(8/31·9/26·9/29·10/13·10/25), AI 광고 외 4개 세트 대비 비용을 재계산함.\n현재 다른 4개 세트 합산 CPM 3856.17988066원, 10/25 CPM 3340.48785984원, 감소율 13.37313188%. 공변량을 통제한 AI ON/OFF 실험이 아니라 관측 비교.\n")

S.append(shell("Effect", '가설 2. Meta AI 기능을 활용하면 <span class="purple">노출이 늘어날 것이다</span>', '\n<div class="ef-mkt"><div class="ef-ad-ai"><div class="ef-mr-card"><div class="label">10/25 캠페인에 적용</div><h3>AI 이미지 생성<br>+ 음악 추가</h3><p>Meta가 제공하는 기능을<br>활용해 광고 소재 제작</p><div class="rule"><div class="ef-mr-number">124,257<small>회</small></div><h3 style="margin-top:18px">첫 7일 노출 수 1위</h3></div><div class="ef-mr-highlight">1,000회 노출당 비용도 최저<br><b>3,340원</b></div></div>\n<div class="ef-mr-card"><div class="label">집행 시작일별 비교 · 첫 7일</div><table class="ef-ad-table"><thead><tr><th>집행 시작일</th><th>노출 수</th><th>집행액</th><th>1천 회당 비용</th></tr></thead><tbody><tr><td>08/31</td><td>40,047</td><td>13.5만</td><td>3,360원</td></tr><tr><td>09/26</td><td>51,552</td><td>19.1만</td><td>3,705원</td></tr><tr><td>09/29</td><td>58,213</td><td>25.0만</td><td>4,290원</td></tr><tr><td>10/13</td><td>20,790</td><td>8.3만</td><td>3,972원</td></tr><tr class="selected"><td>10/25</td><td>124,257</td><td>41.5만</td><td>3,340원</td></tr></tbody></table><div class="ef-mr-highlight">비교한 다른 4개 광고 세트 대비<br>1,000회 노출당 비용 <b>13.4% 낮음</b></div></div></div></div>', cls="ef-marketing-slide"))
S.note("[약 35초] 두 번째는Meta자체AI기능을활용하면노출확대에도움이될수있다는가설입니다.10월25일캠페인에는AI이미지생성과음악추가를활용했습니다. 비교한5개광고세트의최초노출일부터7일을비교한결과10월25일세트가124,257회로가장많이노출됐습니다. 집행액이서로다르므로1,000회노출당비용도함께봤습니다.10월25일세트는3,340원으로가장낮았고,나머지4개세트의합산기준보다13.4%낮았습니다. AI기능을활용한광고에서초기노출성과가좋았던사례입니다.\n음악추가·AI이미지생성을10/25캠페인에사용했다는사실은사용자2026-11-11운영설명에근거.기존확인자료meta-ad-settings.json은test1소재의현재설정이므로10/25의기능증빙으로전용하지않음. 음악추가가반드시AI로작곡한음악이라는뜻도아님.\n모집단:meta-ad-daily.csv의실제노출있는6개광고세트모두. 비교기준은각세트최초실노출일부터6일후까지7개달력일. 무집행일포함,서로다른광고가동일세트에있으면합산. 기간8/31~9/6,9/26~10/2,9/29~10/5,10/13~19두세트,10/25~31. scripts/analyze_ad_level.py와ad-set-first7-comparison.csv참조. 10/25노출124257,지출415079,CPM3340.48786;나머지합산CPM3863.38411,13.5347%낮음.단순CPM평균이아닌지출합/노출합.기본세트CPM3360.20176과의차이는약0.6%로근소함.10/25의총집행기간노출124258과1회차이는11/1잔여노출1회.\n첫7일의관측순위이며전체기간이나클릭률·클릭당비용까지1위라는뜻은아님. 전체기간CPM은기본세트2990.41원으로10/25보다낮음. 다른세트도AI기능을사용했을수있으며ON/OFF대조군없음. 예산·기간·타깃·소재·집행중단을통제하지않아AI사용자체의효과또는Meta의노출우대가증명됐다고말하지않음.기간선택은초기집행성과비교를위해모든세트에동일7일규칙적용;비용보정지표가인과통제를대체하지않음.\n\n[2026-11-13 집행 시작일로 행 이름 변경]\n행 이름은 광고 세트별 최초 실제 노출일. 08/31=추천 설정이 적용된 새로운 트래픽 광고 세트, 09/26=test, 09/29=test - 사본, 10/13 ①=10/13 광고 세트(새 고객 광고), 10/13 ②=테스트(새 트래픽 광고), 10/25=10/25 광고 세트. ①·②는 같은 날 시작한 서로 다른 세트를 구분하는 기호이며 집행 순위나 시간 순서를 뜻하지 않음. 첫 7일 비교 기간·노출·지출·CPM은 기존과 동일. 전체 광고 7개 중 08/31·09/02 광고 2개는 같은 세트에 속하므로 세트 비교는 6행. 원본 CSV에서 모든 행의 최초 노출일과 첫 7일 실적을 재계산하여 ad-set-first7-comparison.csv와 일치 확인. 자세한 매핑은 data/troubleshooting/meta-delivery-audit-20261113.json.\n\n[최종 정정 · 2026-11-13 사용자 확인]\n10/13 신규 집행 광고는 '새 고객 광고'(10/13 광고 세트) 1개. '테스트' 세트의 새 트래픽 광고도 같은 날 처음 관측되지만 CSV의 최초 관측일만으로 신규 생성·집행을 추정할 수 없어, 이 비교표의 별도 10/13 ② 행에서 제외. 합산하지 않음.\n34쪽: 새 고객 광고 10/13 7,155회, 10/14 13,635회. 35쪽: 10/13~19 노출 20,790회, 지출 82,580원, CPM 3,972원. 전체 노출 그래프는 여전히 모든 광고를 합산한 실제 일별 총계이며 제외 기록을 총계에서 지우지 않음.\n이전 노트의 6개 세트·10/13 ①② 표기는 원자료와 이전 판의 조사 이력. 현재 비교표는 5개 세트(8/31·9/26·9/29·10/13·10/25), AI 광고 외 4개 세트 대비 비용을 재계산함.\n현재 다른 4개 세트 합산 CPM 3856.17988066원, 10/25 CPM 3340.48785984원, 감소율 13.37313188%. 공변량을 통제한 AI ON/OFF 실험이 아니라 관측 비교.\n")

S.append(shell('Effect', '서울에서 시작해, <span class="purple">전국 16개 시도로 도달 확대</span>', '\n<div class="ef-mkt">\n  <p class="ef-ad-period">Meta 지역별 도달 수로 확인한 광고 대상 지역의 확장</p>\n  <div class="ef-region-flow">\n    <div class="ef-mr-card ef-region-card">\n      <div class="ef-region-heading"><span class="ef-region-step">1단계</span><h3>서울 우선 공략</h3></div>\n      <p class="ef-region-period">8/31~9/23 · 초기 기본 광고 세트</p>\n      <div class="ef-region-focus"><span>서울 도달 수</span><div class="ef-mr-number">138,998<small>명</small></div></div>\n      <p class="ef-region-purpose">서울을 중심으로<br>서비스 인지도 확보</p>\n      <div class="ef-mr-highlight">인접 경기 지역에도 <b>14,366명</b> 도달</div>\n    </div>\n    <div class="ef-region-arrow" aria-label="1단계에서 2단계로 광고 지역 확대">\n      <svg viewBox="0 0 100 64" aria-hidden="true"><path d="M6 32 H84 M62 10 L84 32 L62 54" fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>\n      <span>전국으로<br>확대</span>\n    </div>\n    <div class="ef-mr-card ef-region-card">\n      <div class="ef-region-heading"><span class="ef-region-step">2단계</span><h3>전국으로 접점 확대</h3></div>\n      <p class="ef-region-period">10/13~25 · 새 고객 광고</p>\n      <div class="ef-mr-bars">\n        <div class="ef-mr-bar"><span>서울</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:50.05%;background:#b7a7df"></div></div><b>15,014</b></div>\n        <div class="ef-mr-bar"><span>경기·인천</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:71.67%;background:#9580d2"></div></div><b>21,500</b></div>\n        <div class="ef-mr-bar"><span>비수도권</span><div class="ef-mr-track"><div class="ef-mr-fill" style="width:92.61%;background:#6c5ce7"></div></div><b>27,783</b></div>\n      </div>\n      <div class="ef-mr-highlight">전국 <b>16개 시도</b>에서 광고 도달 확인</div>\n      <p class="ef-region-definition">경기·인천 및 비수도권: 시도별 도달 수 합계</p>\n    </div>\n  </div>\n</div>', cls='ef-marketing-slide', source='Meta Ads, 「광고 세트×지역 도달 실적 CSV」, 2026-11-11. Dozer 운영자, 「서울→전국 타기팅 변경」, 2026-11-11.'))
S.note("[약30초] 처음에는서울을우선공략해서비스를알렸습니다. 초기기본광고세트에서서울도달수는138,998명이었습니다. 이후온라인서비스의이용가능지역에맞춰대한민국전체로타기팅을넓혔습니다. 새고객광고에서는서울15,014,경기·인천21,500,비수도권27,783의지역별도달을확인했습니다. 서울에서시작해전국16개시도로접점을넓힌운영과정입니다.\n실측:data/troubleshooting/meta-adset-region-reach.csv,Meta보고서광고세트×지역의도달지표.초기기본광고세트정식이름'추천 설정이 적용된 새로운 트래픽 광고 세트',8/31~9/23실제집행.서울138998,경기14366,인천0. 광고별도달을합산하지않고광고세트수준으로중복제거된지역별추정치를조회. 초기서울설정은사용자설명이나실제경기에도도달하므로서울밖0이라고말하지않음.\n전국확대사례는10/13광고세트/새고객광고,10/13~25실제노출일5일. 서울15014,경기18404,인천3096,나머지13개시도27783,Unknown4. 국가전체도달추정치63603과지역합계64301은일치하지않음:Meta의추정·중복등으로지역수치의단순합을중복제거된고유인원으로표현하면안됨. 화면에경기인천·비수도권은시도합계임을명시. 비수도권합계는서울경기인천및Unknown제외. 전국17개시도중세종별도행없음,도달확인16개. 10/25광고는4지역에서만도달이확인되므로전국확대성과로대체하지않음.\n비교는운영단계의대표광고세트로노출지역이다양해졌음을보임. 서로다른집행기간·비용으로도달규모증가율이나지역확대로인한가입상승을계산하지않음. 모든지역에균등분배됐다는뜻이아니며점차넓힌도달범위에관한설명.")


S.append(shell('Effect', '가입 계정 추이와 <span class="purple">이용자의 재방문</span>', '\n<div class="ef-gr-grid">\n  <div class="ef-gr-panel ef-gr-growth">\n    <h3>로그인·비로그인 계정 추이</h3>\n    <p class="ef-gr-period">8/03~11/11 05:42 KST</p>\n    <img class="ef-gr-chart" src="assets/mkt-account-retention-trend.svg" alt="로그인 파란 점선 86개, 비로그인 주황 점선 485개, 전체 보라 실선 571개. 11월 11일까지의 계정 추이.">\n  </div>\n  <div class="ef-gr-panel ef-gr-retention">\n    <h3>사용량 상위 8명의 재방문</h3>\n    <p class="ef-gr-lead">가입 후 <b>최대 69일째</b> 재방문</p>\n<table class="ef-gr-table"><thead><tr><th>회원</th><th>가입</th><th>최근<br>방문</th><th>분석한<br>날</th><th>걸친<br>주</th><th>저장소<br>분석</th><th>LLM<br>호출</th></tr></thead><tbody><tr><td>회원 A</td><td>09-03</td><td>11-11</td><td class="d"><b>8</b>일</td><td>3주</td><td>3회</td><td>49</td></tr><tr><td>회원 B</td><td>09-27</td><td>11-02</td><td class="d"><b>3</b>일</td><td>3주</td><td>1회</td><td>37</td></tr><tr><td>회원 C</td><td>10-09</td><td>11-06</td><td class="d"><b>2</b>일</td><td>2주</td><td>4회</td><td>147</td></tr><tr><td>회원 D</td><td>10-14</td><td>11-11</td><td class="d"><b>2</b>일</td><td>2주</td><td>4회</td><td>95</td></tr><tr><td>회원 E</td><td>09-27</td><td>10-22</td><td class="d"><b>1</b>일</td><td>1주</td><td>32회</td><td>247</td></tr><tr><td>회원 F</td><td>10-23</td><td>11-08</td><td class="d"><b>3</b>일</td><td>3주</td><td>6회</td><td>77</td></tr><tr><td>회원 G</td><td>10-26</td><td>11-11</td><td class="d"><b>2</b>일</td><td>1주</td><td>7회</td><td>371</td></tr><tr><td>회원 H</td><td>10-28</td><td>11-11</td><td class="d"><b>1</b>일</td><td>1주</td><td>2회</td><td>238</td></tr></tbody></table>\n    <div class="ef-gr-highlights">\n      <div><strong>6<small>/8명</small></strong><span>서로 다른 날 분석</span></div>\n      <div><strong>5<small>/8명</small></strong><span>2주 이상에 걸쳐 사용</span></div>\n      <div><strong>7<small>/8명</small></strong><span>11월에도 방문</span></div>\n    </div>\n  </div>\n</div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「회원·게스트 계정 생성일 집계」, 2026-11-11 05:42 KST. 관리자 콘솔 회원 목록 상위 8명, 2026-11-11 캡처(이름·메일 비공개).'))
S.note('[약 35초] 로그인 계정은 파란색, 비로그인 계정은 주황색, 전체는 보라색입니다. 11월 11일 기준 각각 86개, 485개, 합계 571개입니다. 오른쪽의 사용량 상위 8명은 가입 후 길게는 69일째에도 다시 방문했습니다. 6명은 서로 다른 날 분석했고, 5명은 2주 이상에 걸쳐 사용했으며, 7명은 11월에도 방문했습니다. 계정 수와 이 8명의 재방문 현황은 서로 다른 범위의 지표입니다.\n\n[계정 추이 집계]\n운영DB 읽기전용 트랜잭션,2026-11-11 05:42 KST. data/features/counts.sql 및counts.json. CANDIDATE계정 중 payment-test.invalid/review.invalid이메일제외. 내부운영자소유일반계정은추가제외하지않아기존관리자회원집계와일치. 사용자개별식별자는저장하지않음. 계정의created_at(UTC)+9시간KST가입일집계. 현재남아있는회원/게스트상태에따른계정생성추이이며일별로그인횟수나DAU가아님. 게스트→회원전환은현재회원으로분류되어과거곡선이재집계시바뀔수있음. 오늘은조회시점부분값이며이전날들과선연결. 전체연속날짜8/03~11/11. 합계는계정합이지동일인중복제거된사람수가아님.\n\n[상위 8명 집계]\n상위 8명 표 빈도 칸(11-11 관리자 콘솔 GET /api/admin/b2c/members/{id}?days=90, 읽기 전용): 분석한 날 = llm.daily에서 호출 1회 이상인 날짜 수(가입 후 전 기간, 창 08-14~) · 걸친 주 = 그 날짜들이 걸친 월요일 시작 주 수 · 저장소 분석 = activity.analyses.total. 회원별 분석한 날/주: A 8/3 · B 3/3 · C 2/2 · D 2/2 · E 1/1 · F 3/3 · G 2/1 · H 1/1 (합계 22일, 중앙값 2일). 최근 방문 = 콘솔 lastVisitedAt(로그인·페이지 방문 기준, 분석을 안 한 방문 포함). ⚠ Q&A: «매일 쓰나?» → 아니오, LLM을 쓴 날 기준 1~8일. 마지막 분석일은 A 09-17 · B 11-02 · C 10-30 · D 10-23 · E 09-27 · F 11-02 · G 10-28 · H 10-28 — 최근 방문과 다름. 학습 세트 답변 기록이 있는 회원은 D·E 2명. ⛔ «매일»·«주 N회»·«충성 고객»·«팬» 금지. 콘솔 «loyal» 정렬 원본은 앞에 8월 가입 계정 6개가 더 있음(캡처에 없음, 내부 계정 여부 미확인) — 표는 캡처와 같은 8명(가입 시각으로 대조).\n파워유저 표 원본(11-11 사용자 제공 관리자 콘솔 캡처): 순위는 콘솔 목록 순서 그대로(정렬 기준은 콘솔 기본값) · 8명 모두 상태 «사용 중»·제외 체크 없음(외부 회원). 회원 A~H = 순위 1~8. 가입 후 이용 = 최근 방문일 − 가입일(일). 누적 토큰 A 19만 · B 17.5만 · C 49.8만 · D 79.8만 · E 193.4만 · F 55.7만 · G 148.4만 · H 65.8만, 합계 629.4만. 11월 미방문 1명 = E(최근 10-22). ⛔ 이름·메일·GitHub ID를 장표·발화에 쓰지 않음(캡처 원본에 실명·메일 있음 — 원본 이미지 장표에 넣지 말 것).')



S.append(shell('Effect', '공고 분석부터 면접·피드백까지, <span class="purple">기능 이용 실적</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">로그인·비로그인 합산 · 테스트 계정 제외 · 11/11 05:42 KST</p>\n<div class="ef-feature-top">\n<div class="ef-feature-card"><div><h3>공고 분석 결과</h3><p>분석 결과를 보유한 준비 카드<br>서로 다른 공고 본문 141개</p></div><div class="ef-feature-number">234<small>건</small></div></div>\n<div class="ef-feature-card"><div><h3>레포지토리 코드 분석</h3><p>실제 코드 근거 생성 기준<br>고유 저장소 220개</p></div><div class="ef-feature-number">359<small>건</small></div></div>\n</div><div class="ef-feature-bottom">\n<div class="ef-feature-card"><h3>텍스트 면접 세트</h3><div class="ef-feature-number">66<small>세트</small></div><p>문항을 실제 열어본 세트<br>질문 학습 포함</p></div>\n<div class="ef-feature-card"><h3>음성 모의면접</h3><div class="ef-feature-number">20<small>세트</small></div><p>문항을 실제 열어본 세트<br>음성 인식 10세트 · 25회</p></div>\n<div class="ef-feature-card"><h3>문항 피드백 생성</h3><div class="ef-feature-number">91<small>개</small></div><p>문항별 답변 피드백<br>37개 세트에 제공</p></div>\n</div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「공고·레포 분석, 문항 열람, 음성 인식, 문항 피드백 집계」, 2026-11-11.'))
S.note('[약35초] 실제이용기록을기준으로대표기능의성과를한장에모았습니다. 공고분석결과를보유한준비카드는234건,코드근거가생성된레포분석은359건입니다. 고유저장소로는220개입니다. 문항을실제로열어본텍스트면접세트는질문학습을포함해66세트,음성모의면접은20세트였습니다. 문항별피드백은37개세트에서총91개생성됐습니다. 이수치는기능별이용기록이며고유사용자수와는다릅니다.\n통합전39·40페이지의동일DB집계. CANDIDATE계정중payment-test.invalid/review.invalid제외.일반내부계정추가제외없음. SQL읽기전용. 공고본문과insight결과존재234카드,md5본문141,전체준비252;캐시재사용포함,고유정규화공고141을뜻하지않음.레포분석snippet>0이고cs_only=false,READY49+PARTIAL310=359.실패58·CS전용65제외.저장소정규화이름lower기준220.359건모두완전성공이라고쓰지않음.\nset_id별viewed_at보유를1세트로집계.텍스트66=JD_MATCH33+PRIORITY31+MOCK_INTERVIEW2로질문학습포함. 운영화면의텍스트입력은JD_MATCH이고기본모의면접은PRIORITY로생성됨. MOCK_INTERVIEW라는DB유형명만으로텍스트모의면접을정의하면누락이생기므로모드분류는voice_enabled기준. 텍스트MOCK_INTERVIEW2세트는질문은행선택경로의일부이며텍스트모의면접전체가아님.음성MOCK_INTERVIEW20,STT보유10세트25건,음성답변저장9세트. 문항열람은재실행횟수/모든질문완료수와다름. 모의면접완료상태0.피드백attempt_feedback91행/37세트,그중MOCK_INTERVIEW8행/7세트. 피드백생성이지확인/열람횟수아님.각지표를사람수퍼널로연결하거나합산하지않음.')

S.append(shell("Effect", '광고로 유입된 사용자가 <span class="purple">면접 준비에 활용</span>했습니다', '\n<div class="ef-interview">\n  <div class="ef-interview-profile">게임 클라이언트 개발 직무 준비생 · 11/02 이메일 인터뷰</div>\n<figure class="ef-interview-original"><img src="assets/mkt-user-interview-email-original.png" alt="11월 2일 사용자 이메일 인터뷰 원본 캡처. 게임 클라이언트 개발 직무 준비, 광고 유입, 코드와 공고 기반 질문 활용 및 개선 요청에 대한 8개 응답."></figure>\n  <div class="ef-interview-findings">\n    <article class="ef-interview-card">\n      <h3>사용자의 긍정적 평가</h3>\n      <blockquote>“그 부분을 DevFit에서 미리 짚어준 점이<br>생각보다 놀라웠습니다.”</blockquote><p>놓칠 만한 포트폴리오 질문을 찾아<br>모의면접 연습에 추가했습니다.</p>\n    </article>\n    <article class="ef-interview-card ef-interview-improve">\n      <h3>개선 요청에 대응하는 기능</h3>\n      <div class="ef-interview-requests">\n        <div class="ef-interview-request"><b>꼬리질문 답변 학습</b><p>직접 답변하면<br>AI 피드백과 보완점 제공</p></div>\n        <div class="ef-interview-request"><b>기출 연결 방식 개선</b><p>의미·단어 유사도를 확인하고<br>유사·관련·참고 사례를 구분</p></div>\n      </div>\n    </article>\n  </div>\n</div>', cls='ef-marketing-slide ef-interview-slide', source='11/02 사용자 이메일 인터뷰 · DevFit FE/BE 운영 브랜치(2026-11-13 확인)'))
S.note('[약 20초] 인스타그램 광고로 유입된 게임 클라이언트 개발 직무 준비생을 인터뷰했습니다. GitHub 변경 이력과 공고에서 나온 질문이 도움이 됐고, 놓칠 만한 질문을 모의면접 연습에 추가했다고 답했습니다. 실제 면접에서 배열과 연결 리스트를 비교하는 기초 CS 질문을 받았고, DevFit이 이를 미리 짚어 준 점을 긍정적으로 평가했습니다. 개선 요청과 연결해 현재 기능을 확인했습니다. 꼬리질문에 직접 답하면 AI 피드백과 보완점을 받고, 기출은 의미 검색 후 단어 유사도를 확인해 유사·관련·참고 사례로 구분합니다.\n\n[출처] 사용자가 2026-11-13 제공한 이메일 인터뷰 캡처. 메일 표시 일시 11월 2일 (월) 오후 7:50. 사용자 요청(2026-11-13)에 따라 이메일 헤더와 본문이 포함된 원본 캡처를 장표 중앙에 그대로 수록. 요약 텍스트에는 이름·이메일을 별도로 반복하지 않음. 인터뷰 응답 1건을 정리한 정성적 사례이며 전체 사용자나 합격 성과를 대표하는 통계가 아님.\n\n[원문 응답 — 개인 식별 정보 제외]\n1. 기초 CS 개념들을 외우고, 모의 면접 등을 진행 중 입니다. 준비 중인 회사는 게임 회사쪽이고, 게임 클라이언트 개발자 포지션을 준비 중 입니다.\n2. 인스타에서 광고를 보고 알게 되었고, 제 포트폴리오 관련 질문을 준비하기에 좋겠다 생각했습니다.\n3. 제 Github 히스토리를 확인해서 코드를 분석하고 변경점에서 질문을 찾은 점과 특정 공고를 분석해서 그 공고에 대비하는 질문을 준비하는 점이 도움이 되었습니다.\n4. 포트폴리오 관련 질문에서 제가 놓칠 만한 질문들을 찾아서 그 부분을 모의 면접 때 추가해서 연습했습니다.\n5. 특정 자료구조의 특징을 받은 적이 있었습니다. 예를 들면 배열과 연결 리스트의 비교 입니다. 사실 질문 자체의 내용은 기초 CS 질문이라 나올 확률이 높았지만, 그 부분을 DevFit에서 미리 짚어준 점이 생각보다 놀라웠습니다.\n6. 공개하기 어렵습니다.\n7. 포트폴리오 관련 질문을 많이 준비하지 못했는데, DevFit을 활용하면 좀 더 도움이 될 거 같다고 생각했습니다.\n8. 예상 꼬리 질문에 대한 답변을 볼 수 있는 기능이 있다면 좋을 거 같고, 실제 면접 출제 사례가 해당 질문과 맞지 않는 점이 종종 있었습니다.\n\n[해석 범위] 4번의 모의면접 연습이 DevFit 내 기능 사용이라는 점은 확인되지 않으므로 기능 실행 횟수나 전환으로 집계하지 않음. 5번은 사용자가 경험한 기초 CS 질문의 유사성에 관한 응답이며 특정 기업의 비공개 면접 문항 적중, 설계 의도 검증 또는 합격 효과를 입증하지 않음. 화면 인용은 원문 일부를 발췌. 6번에서 공개하기 어렵다고 한 세부 대상은 캡처에 질문이 없어 알 수 없으며 해당 내용은 추정·공개하지 않음.\n\n[실제 기능 확인 · 2026-11-13 운영 브랜치]\nBE prod 9f5da6d7bcd18e4dad90fa36f1b087846796374a, FE prod 5a9b6b6bd95c34421080b03b71b3caf70260e5e0.\nStudySetService.followUpFeedback: 원 질문, 의도, 답변 가이드와 코드 근거를 활용해 사용자 꼬리질문 답변을 평가하고 피드백과 추가 꼬리질문을 저장. StudySetWorkspace: 사용자의 답변, AI 피드백, 보완점을 표시. 예상 꼬리질문의 모범답안 선제 제공은 확인되지 않아 그렇게 표현하지 않음.\nInterviewQuestionVectorSearch/InterviewQuestionEvidenceMatchService: 의미 검색 후보를 단어 유사도로 재검사. InterviewEvidenceCard: SIMILAR, RELATED, REFERENCE를 구분하고 참고만 있으면 직접 유사한 사례가 확인되지 않았다고 안내. 관련 없는 사례를 모두 폐기하거나 정확도가 완전히 해결됐다는 뜻은 아님.\n근거 코드 사본: data/interview-response-evidence/source-commits.json 및 각 소스 파일. 일부 기능은 인터뷰 이전부터 존재하므로 이 이메일 이후 새로 개발했다는 인과·시점 주장은 하지 않음. 사용자 요청에 대응하는 실제 기능을 설명한 장표.\n')

S.append(shell('Effect', '핵심 기능인 모의면접, <span class="purple">이용 확대에 맞춘 광고</span>', '\n<div class="ef-mkt"><p class="ef-ad-period">11/11 05:42 KST · 로그인·비로그인 합산 · 계정 기준 중복 제거</p>\n<div class="ef-mock-value"><div class="label">01 DevFit의 핵심 기능</div><div class="ef-mock-core-body"><h3>내 코드로 연습하는<br>텍스트·음성 모의면접</h3><div><p>코드 기반 질문에 직접 답하고<br>피드백으로 설명력을 점검하는 경험</p><div class="emphasis">핵심 기능의 가치를 알리고 실제 답변까지 이어지는 이용 확대</div></div></div></div>\n<div class="ef-mock-direction"><div class="ef-mock-current"><div class="label">02 이용 현황 · 모의면접 문항을 열어본 계정</div><div class="ef-mock-kpis">\n<div class="ef-mock-kpi"><h3>텍스트 모의면접</h3><div class="number">29<small>개 계정</small></div><p>66세트 문항 열람</p></div>\n<div class="ef-mock-kpi"><h3>음성 모의면접</h3><div class="number">5<small>개 계정</small></div><p>20세트 문항 열람</p></div>\n</div></div>\n<div class="ef-mock-next"><div class="label">03 앞으로의 광고 포커스</div><h3>앞으로는 모의면접 기능을<br>중점적으로 홍보합니다</h3><p>내 코드로 답변을 연습하고 피드백을 받는<br>텍스트·음성 모의면접의 가치를 알립니다.</p><div class="ef-mock-goal">목표 · 모의면접 기능 이용자 확대</div></div></div></div>', cls='ef-marketing-slide', source='DevFit 운영 DB, 「답변 모드별 문항 열람·답변 보유 계정 집계」, 2026-11-11. DevFit FE·BE, 「운영 브랜치 모드 분류 코드」, 2026-11-11.'))
S.note("[약25초] DevFit의 핵심 기능은 내 코드에서 나온 질문에 직접 답하고 피드백을 받는 텍스트·음성 모의면접입니다. 실제 이용 현황을 보면 문항을 열어본 계정은 텍스트 29개, 음성 5개입니다. 앞으로는 이 모의면접 기능을 중점적으로 홍보하겠습니다. 내 코드로 답변을 연습하고 피드백을 받는 가치를 알려, 핵심 기능을 이용하는 사용자를 늘리는 것이 목표입니다.\n정정: 이전40쪽의텍스트1개/답변2개는set_type='MOCK_INTERVIEW'로잘못한정한부분집계였다. 운영코드상텍스트입력선택은JD_MATCH,자동기본모의면접은PRIORITY로생성되므로두유형을제외하면실제텍스트이용을누락한다. 현재화면·관리자와같이voice_enabled=false를텍스트,true를음성으로분류하되이용지표는세트생성후실제문항최초열람을확인한계정으로집계. 생성수와문항열람수를혼동하지않음.\n코드근거: Devfit_FE prod 9b436df993d0a2d6e51db5b097abc0f52757d666의SetDashboard.tsx, ANSWER_MODE_OPTIONS의JD_MATCH=텍스트입력,MOCK_INTERVIEW=음성인식,카드표시voiceEnabled기준. Devfit_BE prod 88d6f3b8f0f2c0a78dbb64ac85adc9f6c7cec363의StudySetService.java는bootstrapDefaultSet에서PRIORITY로기본모의면접생성;AdminBehaviorService.java도voice_enabled로TEXT/VOICE분류. 저장사본data/features/*-prod.*. 관리자생성기준수치와차이가나는이유는관리자가created_at을집계하고이슬라이드는viewed_at까지확인하기때문. 제외계정기준도관리자기본과다를수있음.\n데이터근거:data/features/interview-mode-audit.sql, interview-mode-audit.json. 운영DB읽기전용집계,개인식별자·원문답변추출없음. 조회시각2026-11-10T22:07:33.706168+00:00. 이전39쪽과맞추기위해계정·세트생성및문항최초열람을2026-11-10 20:42:51.23812UTC(11/11 05:42:51KST)이하로제한. CANDIDATE중payment-test.invalid/review.invalid제외,내부일반계정포함. 현재보존데이터/현재guest상태기준. 답변은당시이전생성된question_attempt의현재비공백answer를집계하므로과거수정·삭제를완전히복원하는시점복구쿼리는아님.\n텍스트:201세트생성/87계정,66세트열람/29계정(회원21·게스트8),답변기록32세트/19계정. 열람세트유형JD_MATCH33·PRIORITY31·MOCK_INTERVIEW2. 유형별이용계정은20·17·1이며중복이있어단순합이아닌user_id중복제거로29. 음성:20세트열람/5계정(회원3·게스트2),답변기록10세트/2계정,STT10세트/2계정. 두모드이용중복5계정→합계29,답변계정중복2→합계19. 39쪽66세트와40쪽29계정은같은텍스트모드·문항열람범위. 기록보유계정이지고유자연인수는아님. 문항열람은전체면접완료나답변완료가아님. StudySetService.restoreArchivedAnswers로이전답변복원도가능하므로답변19는'신규답변제출자'대신'답변기록보유계정'으로표기.\n화면에서는 중복 제거 계정·답변 기록 합계와 하단 집계 설명을 삭제하고, 계정 수와 열람 세트 수를 확대 배치. 집계 정의와 원자료는 위 근거 노트에 보존. 3번은 모의면접 기능의 가치 홍보와 이용자 확대라는 향후 방향만 제시하며, 영상 제작·랜딩·CTA·광고비 등 구체적인 광고 방식 설명은 삭제. 향후 계획이며 집행 완료가 아님. 임의 목표 수치 없음. 이용이 적은 원인이 광고라고 입증한 것은 아님. 실제 광고 설정 변경·게시 없음.")

# ---------- 마케팅 끝 ----------


# ---------- ③ 지표 — 유저 · 실운영 ----------




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
장표에서 뺀 항목(2장 압축, 2026-11-07): 광고 수신 동의·약관 개정(09-09) · IT 기업 대표 서면 회신(10-26) · 김종욱 멘토 서비스 검증(10-25) · 전략 멘토링(11-02) — 멘토 건은 부록 A13(현업 검토)에서 다룸.
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
APX.append(shell('Appendix · A13', '현업 면접관·게임사 대표의 <span class="purple">서비스 검토와 반영</span>', f"""
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
S.append(shell('Effect', '사업 운영 기반을 갖추고, <span class="purple">상표·핵심 기술을 출원</span>했습니다', '\n<div class="ef-foundation-grid">\n  <article class="ef-foundation-card">\n    <div class="ef-foundation-kicker">사업 운영</div>\n    <h3>사업자등록·통신판매업<br>신고 완료</h3>\n    <div class="ef-foundation-docs">\n      <figure><img src="assets/cert-biz.png" alt="사업자등록증 전체"><figcaption><b>사업자등록</b><span>도저랩스 · 09/02 개업</span></figcaption></figure>\n      <figure><img src="assets/cert-mail.png" alt="통신판매업 신고증 전체"><figcaption><b>통신판매업 신고</b><span>11/02 신고</span></figcaption></figure>\n    </div>\n    <div class="ef-foundation-result">서비스 운영·결제를 위한 사업 기반</div>\n  </article>\n  <article class="ef-foundation-card">\n    <div class="ef-foundation-kicker">채용 정보 제공</div>\n    <h3>직업정보제공사업<br>신고 완료</h3>\n    <div class="ef-foundation-docs single">\n      <figure><img src="assets/cert-job.png" alt="직업정보제공사업 신고확인증 전체"><figcaption><b>서울청 제2026-31호</b><span>10/19 신고</span></figcaption></figure>\n    </div>\n    <div class="ef-foundation-result">직업정보제공사업자로 신고</div>\n  </article>\n  <article class="ef-foundation-card ef-foundation-ip">\n    <div class="ef-foundation-kicker">브랜드·기술 보호</div>\n    <div class="ef-foundation-trademark">\n      <img src="assets/ef-trademark.png" alt="DevFit 상표 출원공고결정서 전체">\n      <div><h3>DevFit 상표<br>출원공고 결정</h3><p>제42류 · 11/06</p></div>\n    </div>\n    <div class="ef-foundation-patents">\n      <h3>핵심 기술 <strong>3건</strong> 특허 출원</h3>\n      <div class="ef-foundation-patent-docs">\n        <figure><img src="assets/patent-a.png" alt="질문 선별 특허 출원번호통지서 10-2026-0214808"><figcaption>질문 선별</figcaption></figure>\n        <figure><img src="assets/patent-b.png" alt="질문 생성 특허 출원번호통지서 10-2026-0214809"><figcaption>질문 생성</figcaption></figure>\n        <figure><img src="assets/patent-c.png" alt="음성 답변 평가 특허 출원번호통지서 10-2026-0214811"><figcaption>음성 답변 평가</figcaption></figure>\n      </div>\n    </div>\n    <div class="ef-foundation-result">상표 출원공고 결정 · 특허 3건 출원</div>\n  </article>\n</div>', cls='ef-foundation-slide', source='사업자등록증·통신판매업 신고증·직업정보제공사업 신고확인증·상표 출원공고결정서·특허 출원번호통지서 3건'))
S.note('[약 13초] 사업자등록과 통신판매업·직업정보제공사업 신고를 마쳤습니다. DevFit 상표는 출원공고 결정을 받았고, 질문 선별·질문 생성·음성 답변 평가의 핵심 기술은 특허 3건으로 출원했습니다.\n\n[기존 33~35쪽 통합 · 증빙 및 질의응답 근거 보존]\n[사업자등록 · 통신판매업 신고 · 상표 출원]\n[증빙] 사업자등록증(640-21-02214, 개업 2026-09-02, 서초세무서) · 통신판매업 신고증(제2026-서울서초-3702호, 11-02) · 상표 출원공고결정서(DevFit, 제42류, 출원번호 40-2026-0177374, 지식재산처 2026-11-06 발송, 상표법 제57조, 출원인 박천웅, 원본 ASM/devfit_출원공고결정서.pdf 1쪽) 원본 그대로(자르지 않고 가리지 않음).\n상표: 출원공고 결정 = 심사 통과 후 공고 단계(이의신청 기간 남음), 등록 아님 → «출원공고 결정»까지만. ⛔ «상표 등록» 금지. ⛔ «매출» · «공동대표» 금지.\n\n[직업정보제공사업 신고]\n[직업정보제공사업 신고 · 법률 멘토링 메모 — Q&A용]\n직업정보제공사업 신고확인증: 서울청 제2026-31호(10-19). 근거 법조 직업안정법 제2조의2 제8호·제23조(법률 제20121호, 2024. 1. 23. 일부개정, 2024. 7. 24. 시행), law.go.kr에서 2026-11-06 그대로 복사. 신고확인증 본문에도 «직업안정법 제23조»가 적혀 있음. 공고 수(플랫폼 5 + 기업 사이트 24)는 prep/JobPostingFetchService BOARDS 5 + CorporateSiteRegistry 24.\n법률 멘토링: «법무법인 백상 김재철 변호사», 소마 공식 «[자유 멘토링] Dozer(도저)팀 법률멘토링» 2026-11-05(자문 계약 아님). «기출문제 크롤링·가공 = 저작권 침해 해당 없음»은 구두 검토 의견 → «법률 멘토 검토 의견»으로만. «출원 전 공개 기술 → 특허 공지예외주장 신청» 조언도 같은 멘토링의 구두 조언(특허법 제30조).\n개인정보 보호 조치: §30 처리방침 · §22 선택 동의 · §29 토큰 AES/GCM · §21 탈퇴 시 물리 삭제. ⛔ «개인정보 보호법 완전 준수»·«위반 없음»·«법률 검토 통과» 금지. 처리방침에 OpenAI 국외 이전 등 미반영(collect/K-compliance.md §1).\n순서 주의: 신고(10-19)가 멘토링(11-05)보다 먼저 → «멘토링 결과로 신고했다»고 말하지 않음. ⛔ 외부 법무법인 자문으로 말하지 않음 (claims.md C6). 같은 내용 Effect 직업정보제공사업 장.\n\n[핵심 기술 3건 특허 출원: 질문 선별 · 질문 생성 · 음성 답변 평가]\n[증빙] 출원번호통지서 3건(2026-11-01): 10-2026-0214808(코드 저장소 기반 면접 질문 선별 방법 및 시스템) · 10-2026-0214809(코드 저장소 기반 면접 질문 생성 방법 및 시스템) · 10-2026-0214811(음성 대화 기반 면접 답변 평가 방법 및 시스템). 출원인 김건우, 발명자 김건우 박천웅 노재원, 심사청구(무) 공개신청(무).\n명세서 이미지는 devfit/특허/ 아래 제출본 docx를 LibreOffice로 렌더링한 첫 장.\n⛔ 특허 «등록»·«회사 특허» 금지 (출원 단계, 출원인 김건우 개인). 청구항 요지는 부록 A8.')

# ---------- 시장 규모 (11-11 사용자 지시: TAM·SAM·SOM 표, B2C·B2B 하이브리드) ----------
S.append(shell("Effect", '<span class="purple">시장 규모</span>와 가격 선정 근거', '\n<div class="ef-one ef-market-pricing">\n  <div class="ef-circ">\n    <div class="c tam"><em>TAM</em><b>약 1,132억 원</b><span>개발자 채용 전체 · 구직자 준비 + 기업 검증</span><code>구직자 38.8만 명 × 23,700원<br>+ 입사지원 520만 건 × 2만 원</code></div>\n    <div class="c sam"><em>SAM</em><b>약 143억 원</b><span>돈을 쓰는 구간</span><code>취업 준비 지출 42.9% × 92억<br>+ 면접 단계 10% × 1,040억</code></div>\n    <div class="c som"><em>SOM</em><b>약 4억 원</b><span>3년 내 목표</span><code>B2C 전환 1%<br>+ B2B SAM 3%</code></div>\n  </div>\n  <div class="ef-one-r">\n    <div class="ef-one-k">\n      <div><small>연간 개발 직군 입사지원</small><b>약 520만 건</b><i>사람인 · 점핏 2025 상반기 260만 건 × 2</i></div>\n      <div class="op">÷ 13.4회</div>\n      <div class="hi"><small>면접을 준비하는 개발자 구직자</small><b>약 38.8만 명</b><i>1인 평균 입사지원 13.4회 (한경협 2025)</i></div>\n    </div>\n    <div class="ef-price-basis">\n      <article class="ef-price-card">\n        <div class="ef-price-label">B2C · 구직자의 지불 의향을 참고한 가격</div>\n        <div class="ef-price-amount">월 <b>7,900원</b><span>× 유료 이용 3개월 = 23,700원</span></div>\n        <p>구직자 인터뷰: 면접 1회 <strong>1만 원</strong>, 준비 기간 <strong>2만 원</strong> 지불 의향<br>월 구독으로 이용 부담을 낮추고, 시장 계산에는 유료 3개월을 가정</p>\n      </article>\n      <article class="ef-price-card">\n        <div class="ef-price-label">B2B · 지원자 단위 과금 모델</div>\n        <div class="ef-price-amount">지원자 1명당 <b>2만 원</b><span>시장 계산용 가정</span></div>\n        <p>코드 분석·면접 질문 준비를 지원자 단위로 제공<br>실제 기업 요금은 파일럿에서 이용 가치와 원가를 검증한 뒤 확정</p>\n      </article>\n      <div class="ef-price-cost"><b>분석 1회 변동비 약 330원</b><span>저장소 3개 기준 · B2C와 B2B가 분석 엔진 공유</span></div>\n    </div>\n  </div>\n</div>', cls='ef-market-slide', source='점핏 2025 개발자 채용 리포트 · 한경협 2025 구직자 조사 · 구직자 인터뷰 · 최종보고서 요금·단위 경제성 · B2B 가격은 내부 가정'))
S.note('[약 30초] 시장 규모는 구직자의 면접 준비와 기업의 지원자 검증을 합쳐 추산했습니다. 전체 약 1,132억 원, 실제 지출 구간 약 143억 원, 3년 내 목표 약 4억 원입니다. B2C는 구직자의 면접 1회 1만 원 지불 의향을 참고해 월 7,900원으로 구성했고, 시장 계산에는 유료 3개월을 가정했습니다. B2B의 지원자당 2만 원은 계산용 가정이며 실제 요금은 기업 파일럿에서 검증합니다. 두 서비스가 분석 엔진을 공유하며 저장소 3개 분석의 변동비는 약 330원입니다.\n\n분해(Q&A): TAM = B2C 92억 + B2B 1,040억 · SAM = B2C 39.5억(42.9% 지출층) + B2B 104억(면접 단계 10%) · SOM = B2C 0.92억(1%) + B2B 3.1억(SAM 3%). 11-11 사용자 지시 «하나의 TAM·SAM·SOM으로, 기존 지표(38.8만 명 · 전환 시나리오)도 살리고». 원 크기는 금액 비례 아님.\n\n계산: 2,601,390 × 2 ≈ 520만 건(하반기 동일 가정) ÷ 13.4회 ≈ 38.8만 명(최종보고서와 같은 계산).\nB2C: TAM 388,100 × 23,700원(3개월 무료 체험 후 7,900 × 3) ≈ 92.0억 · SAM × 42.9% ≈ 166,500명 ≈ 39.5억 · SOM 1% = 3,881명 × 23,700 ≈ 0.92억(최종보고서 시나리오와 같은 값, 2%·5%는 부록 A10).\nB2B: TAM 520만 × ₩2만 = 1,040억 · SAM × 10%(서류 통과율 가정) = 52만 건 = 104억 · SOM 3% ≈ 3.1억(3년). collect/H-market.md §3 «3년 SOM 약 3억 원대 방어 가능»(상향식 0.8~5.2억 · 내부 고객 수 기반 3.1억 일치).\n합산: TAM 92 + 1,040 = 1,132억 · SAM 39.5 + 104 = 143.5억 → «약 143억» · SOM 0.92 + 3.1 = 4.0억. 11-11 사용자 지시 «둘이 합쳐서 개발자 채용시장 전체, DevFit Platform 기준».\n보수안(₩1만·5%): B2B TAM 520억 · SAM 26억 · SOM 0.8억 → 플랫폼 TAM 612억 · SAM 65억 · SOM 1.7억 — Q&A용.\n출처 등급: 520만 건(점핏 리포트 직접, ×2는 가정) · 13.4회(한경협 2025) · 42.9%(잡코리아 콘텐츠LAB N=485, 비대표 표본 🟡) · ₩2만·10%·3%는 내부 가정(⚙, research/R1-ef-market.md #3 «써도 되나 가정 표기 유지»). 기간 주의: B2C SOM은 연 단위 1% 시나리오, B2B SOM은 3년 목표 → 합계는 «3년 내 목표»로만 말함.\n⛔ «매출 전망»으로 말하지 않음 — 시장 규모. ⛔ 5년 SOM 27억 · TAM $2.8B 금지(재현 불가). ⛔ «52만 명» 아님 → «52만 건».\n\n[금액 페이지 근거 보존]\nB2C 근거 원문: 중간평가 IR 덱(vendor/irdeck_new.html 1485~1501행) «지원자 A · 20세, 프론트엔드 인턴 지원 경험 · 1대1 인터뷰» — Q «얼마까지 결제할 의향이 있으신가요?» → A «면접 1회 기준 만원 정도, 준비기간 동안이면 2만원까지는 결제할 의향이 있습니다». 같은 덱 B2C 칸 «인터뷰 기준 지불 의향은 면접 1회 1만원, 준비기간 이용권 2만원». 원 녹취 파일은 저장소에서 찾지 못함 → 출처는 중간평가 덱 수록본. 화자는 역할로만.\n⚠️ 한계(Q&A): 인터뷰 1명의 진술 의향(실제 결제 아님). 보조 근거: 다른 구직자 인터뷰(feedback/04_사용자인터뷰)에서 «학원에 가서 도움을 받았다» · AI에 월 약 90만 원 지출 — 이미 취업 준비에 돈을 쓰는 층. 같은 인터뷰의 «이미 쓰는 AI로 준비하면 된다» 반론(O1)은 범용 AI 비교 실험(근거 실존 0/18 vs 28/28)으로 답.\nB2B 과금: collect/J-b2b-pilot.md «지원자 1명당 종량, 가격은 원가 ₩1,000~2,000에서 바텀업, 파일럿 결과로 확정». 시장 장의 1인 2만 원은 시장 크기 계산용 가정이지 확정 가격이 아님.\n변동비: 최종보고서 단위 경제성 — 약 330원(저장소 3개, CloudWatch 실측) · 20개 상한 약 1,404원 · 재분석 0원 · 월 구독료와 분석 원가는 사용량에 따라 달라 단순 이익률로 환산하지 않음. 요금 화면은 부록 A6 · 이전 판 장표(pricing.png)에서 뺌.\n토스페이먼츠 계약 완료(11-11 사용자 지시, claims.md C3). ⛔ «구독 매출»·«매출»로 말하지 않음. ⛔ B2B 가격 숫자를 확정가처럼 말하지 않음. ⛔ «60% 절감» 비교 금지.\nQ&A: «결제는 열려 있고 매출은 아직 0» (claims.md C3).\n[해석 정정] 월 7,900원은 인터뷰 1명의 지불 의향을 참고한 가격이며 시장 전체의 지불 의향을 검증한 결과가 아님. 유료 3개월 23,700원은 준비 기간 전체 2만 원 의향보다 크므로 그 범위 안이라고 표현하지 않음. 월 요금과 3개월 이용 가정은 별개. B2B 2만 원은 시장 산정 가정이며 330원 원가에서 산출된 확정 판매가가 아님. 330원은 저장소 3개 분석의 변동비로 인건비·전체 고정비를 포함한 총원가 아님. 기존 B2C 1/2/5% 전환 시나리오는 부록 A10에 유지. Free/Plus/추가 생성권과 결제 상세는 부록 및 이 노트에 보존.\n')

# ---------- 차별점 — 면접 대비 서비스 지형 + 개발자 서비스 비교 ---------- (근거: collect/G-competitors.md)
def df_row(name, sub, cells, me=False):
    tds = ''.join(f'<td class="n">{c}</td>' if c in ('–', '확인 안 됨') else f'<td>{c}</td>' for c in cells)
    return f'<tr class="{"me" if me else ""}"><td>{name}<small>{sub}</small></td>{tds}</tr>'

GEN = ['사람인 AI 모의면접', '잘봐요', '뷰인터', '티오(TIO)', 'Final Round AI', 'Huru', 'Yoodli', 'Big Interview']
DEV = ['점핏', '프로그래머스', '프로그래머스 비즈니스', '코드트리', '구름 Devth', '인프런 모의면접', '꼬꼬면', '테크톡', 'Tech Check', 'F-Lab']



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
DC_PRICES = ['<span class="dc-price">7,900원 / 월</span><span class="dc-price-detail">Plus · 3개월 체험</span>', '<span class="dc-price">14,900원 / 월~</span><span class="dc-price-detail">Lite 월간 · 무료 제공</span>', '<span class="dc-price">12,000원 / 회</span><span class="dc-price-detail">첫 1회 무료</span>', '<span class="dc-price">토큰 구매 방식</span><span class="dc-price-detail">금액: 로그인 후 확인</span>', '<span class="dc-price">US$10 / 월~</span><span class="dc-price-detail">Pro · 무료 월 1회</span>', '<span class="dc-price">US$179 / 회~</span><span class="dc-price-detail">사람 면접 · AI 무료</span>', '<span class="dc-price">US$79 / 월</span><span class="dc-price-detail">Pro 월간 · 무료 5회</span>']
def dc_table():
    head = '<tr><th>기능</th>' + ''.join(f'<th class="{"me" if i == 0 else ""}">{c}{DC_PRICES[i]}</th>' for i, c in enumerate(COLS)) + '</tr>'
    body = ''.join('<tr><td>' + f + '</td>' + ''.join(f'<td class="{DC_CLS[v]}{" me" if i == 0 else ""}">{DC_MARK[v]}</td>' for i, v in enumerate(vals)) + '</tr>' for f, vals in DC_ROWS)
    return f'<table class="dc-t"><thead>{head}</thead><tbody>{body}</tbody></table>'

S.append(shell('Effect', '개발자 대상 서비스 비교: <span class="purple">내 커밋 · 근거 코드 · 공고 가져오기</span>', f'''
<div class="dc-wrap dc-priced">
  <div class="dc-box">{dc_table()}</div>
  <div class="ef-line" style="margin-top:18px">채용·구직 서비스는 1,484곳이지만 <span class="purple">개발자 취업 준비 전용</span>은 국내 10곳</div>
</div>''', source='각 서비스 공개 페이지 기준 (2026-11-05 · 인프런 11-07 확인 · 티오 최종보고서 경쟁 표) · DevFit 칸은 운영 코드 기준'))
S.note('[≈15초] 개발자 서비스들도 질문은 기출 문항 은행이나 레포 단위에서 나옵니다. 인프런 모의면접은 기출 패턴과 이력서로 묻습니다. DevFit은 팀 프로젝트에서도 내가 짠 커밋만 골라, 질문마다 그 diff와 원문 링크를 붙입니다. 공고는 링크만 넣으면 본문을 바로 가져오고, 캡처 이미지여도 읽어 냅니다. 채용 플랫폼 5곳과 기업 채용 사이트 24곳, 29곳을 지원합니다.\n\n조사 범위: 국내외 36건(국내 18·해외 18), 2026-11 기준 — 최종보고서와 같음. 하단 문장은 보고서 «…서비스는 확인되지 않았다(2026년 11월 기준)»와 같은 수위. ⛔ «유일»·«최초»·«경쟁자 없음» 금지.\n- 티오(TIO): 일반 취업 준비 AI. 공고 링크 분석 O(✓), 질문 근거는 업로드한 경험 자료·자기소개서 → 코드 기반 질문 X. 그 밖의 행은 공개 페이지에서 확인 안 함(✕ = 부재 증명 아님). 출처: 최종보고서 각주 20 «티오(TIO) - 취업 준비 AI 어시스턴트» 서비스 소개 페이지.\n- 공고 행 이름을 «공고 링크로 본문 분석»으로 바꿈(티오도 링크 분석). DevFit의 29곳(플랫폼 5 + 기업 24) 지원은 노트로만.\n근거: last-dance/collect/G-competitors.md §1 (공개 페이지, 접근일 2026-11-05) · collect/G2-inflearn.md (2026-11-07). DevFit 칸은 운영 코드(BE origin/prod 500f4af · FE 2c46ce6) 기준.\n- 인프런 모의면접(inflearn.com/ai-interviews): AI 면접관, 개발자 전용(백엔드·FDE·프론트엔드), 기출 문항 은행 + 이력서·포트폴리오 PDF(선택), 음성·꼬리질문·아바타, 한국어. GitHub·커밋·공고 URL 입력은 공개 페이지에 없음. 첫 1회 무료, 이후 1회 12,000원. 출시 시점은 관계자 LinkedIn 글뿐(«2026년 하반기»로만). 인프랩이 랠릿을 운영하지만 연동 언급 없음.\n- DevFit «기출» = 공개 기출 1,880건(11-08 운영 DB, 1차 853 + 2차 1,027).\n- Greenroom(usegreenroom.app): Pro $10에 «GitHub repo analysis»(레포 단위 → «일부»), 음성. 본인 커밋 구분·질문별 근거·특정 공고·한국어는 공개 페이지에 없음. Q&A 최우선 대비.\n- 꼬꼬면(kokomen.kr): 개발자 특화, 이력서·포트폴리오 + 현직 출신 500+ 문항 은행, 음성, 한국어. GitHub 언급 없음.\n- interviewing.io: 익명 사람 모의면접 + AI 면접관, 오디오+채팅. Pramp(2021 Exponent 인수 → Aced): 동료 1:1 매칭(«일부»)·질문 은행.\n표 읽는 법(화면 범례는 사용자 지시로 뺌, 11-07 · ✓/✕ 표기도 사용자 지시): ✓ = 공개 페이지·운영 코드로 확인 · ✕ = 공개 페이지에서 확인되지 않음(기능 부재를 증명하지 않음) · △ = 부분 확인(사용자 지시 11-07): Greenroom 커밋 선별·비공개 레포·근거 코드·문항 은행은 레포를 읽는다는 것까지만 공개, Pramp는 동료 1:1(AI 꼬리질문 아님). 한국어 행은 사용자 지시로 뺌(인프런·꼬꼬면 O, Greenroom 확인 불가).\n행 근거(11-07 추가): GitHub 연동 = Greenroom «Ari reads your repos»(G1) · 본인 커밋 선별 = GithubService author: 필터(D3), Greenroom은 레포 단위까지만 공개 · 비공개 레포 = includePrivate 증분 동의(users.github_scopes, V38) · 공고 자동 수집 = prep/JobPostingFetchService BOARDS 5 + CorporateSiteRegistry 24(D1·D2) · 캡처 이미지 = /candidate/interview-preps/extract-image(vision OCR) — 경쟁 5곳 공개 페이지에 공고 URL·이미지 입력 언급 없음(사람인은 자사 공고 URL만 받지만 이 표에 없음) · 어필 포인트 = prep/AppealService · 지원 일정·마감 = journey/ 여정 트래커(운영 중) · 면접관 콘솔 = /recruit/*(Greenroom «For teams — Soon», interviewing.io «For employers» 링크만 → –).\n⛔ «AI는 레포를 못 읽는다» 금지(ChatGPT 커넥터·Claude 연동은 읽음). ⛔ 타사 비방 금지 — 공개 페이지 사실만, «–»는 부재가 아님.\n\n[2026-11-13 가격 조사 · 공식 공개 페이지]\n- DevFit: Free 제공. Plus는 3개월 무료 체험 후 별도 유료 전환 동의 시 월 7,900원. 추가 생성권 1회 1,900원. 출처: https://devfit.app/pricing\n- 티오(TIO): Free AI 일 5회, Lite 월간 14,900원, Pro 월간 19,900원. 반년 선결제 환산액을 월간 결제 가격과 혼동하지 않음. 출처: https://tiokorea.com/pricing\n- 인프런 모의면접: 공식 FAQ에서 첫 1회 무료, 이후 1회 12,000원 확인. 출처: https://www.inflearn.com/ai-interviews\n- 꼬꼬면: 공식 홈페이지 토큰 구매 링크가 /purchase이며 로그인 페이지로 이동. 익명 공개 화면에서 구매 금액을 확인하지 못했으므로 추정 금액을 기입하지 않음. 무료 체험은 홈페이지 제공. 출처: https://kokomen.kr/purchase\n- Greenroom: Free 월 1회, Pro 월 $10/10회, Premium 월 $20/30회. GitHub 레포 분석은 Pro에 기재. 출처: https://usegreenroom.app/#pricing\n- interviewing.io: 공식 FAQ: 사람 모의면접 $179부터, 주제·회사에 따라 달라짐. AI 면접 무료. 사람 전문가 가격과 AI 구독 가격은 동등한 상품 비교가 아님. 출처: https://interviewing.io/faq\n- Pramp · Aced: 공식 요금 페이지 Monthly 선택: Pro $79/월, Expert $99/월. Basic 동료 면접 월 5회 무료, Pro 동료 면접 무제한. Annually 선택 시 표시된 $12/$20는 월 환산 표시이므로 본 표에는 월간 결제 금액을 사용. Pramp는 Aced로 이전(공식 practice FAQ). 브라우저 확인 결과 data/aced-pricing-browser-20261113.json. 출처: https://www.aced.io/upgrade?src=nav\n비교표 가격은 통화·과금 단위를 그대로 표시. 구독, 건별 전문가 면접, 토큰 상품을 단순 최저가 순위로 해석하지 않음. 환율 환산 없음. 기능 표의 공개 페이지 확인 범위는 기존 근거를 유지.\n\n[삭제한 시장 분류 장표 근거 보존]\n[≈12초] 고용노동부에 신고된 채용·구직 정보 서비스만 1,484곳입니다. 면접 대비 서비스도 많지만 대부분 이력서와 자소서, 채용 공고를 보고 일반 직무 질문을 만듭니다. 개발자만을 위한 취업 준비 서비스는 저희가 찾은 국내 운영 중 서비스로 10곳이고, 채용 1곳, 코딩테스트 4곳, 기술면접 4곳, 멘토링 1곳입니다. 그중 지원자 본인의 GitHub 코드로 질문을 만드는 곳은 공개 페이지에서 확인되지 않았습니다.\n\n오른쪽 10곳 근거: collect/G4-dev-jobprep.md (research-2, 접근 2026-11-07, 공개 검색 기준 — 노트·Q&A에서는 «최소 10곳»). 채용 점핏 · 코딩테스트 프로그래머스 연습·프로그래머스 비즈니스(기업용)·코드트리·구름 Devth(기업용) · 기술면접 인프런 모의면접·꼬꼬면·테크톡(iOS 개인 앱)·Tech Check(iOS 개인 앱) · 멘토링 F-Lab. 기업 서비스만 세면 8곳. 제외: 랠릿(IT 전반)·프로그래머스 커리어(접속 불가)·백준(재오픈 연기)·solved.ac(403)·원티드·사람인·그룹바이·코멘토(범용)·부트캠프·강의·오픈소스·개인 레포. «0곳» = 국내 운영 중 10곳 공개 페이지 기준. F-Lab «Github 상시 코드 리뷰»는 사람 멘토 리뷰라 질문 생성 아님. 해외 Greenroom은 레포 단위 분석을 공개(다음 장 비교표) → ⛔ «세계 유일»·«GitHub 기반은 DevFit뿐». 1,484곳(신고 사업장)과 10곳(조사한 제품)은 세는 단위가 다름 → «1,484곳 중 10곳» 금지.\n\n근거: 1,484곳 = 공공데이터포털 «고용노동부_직업정보제공사업자 현황_20251031»(https://www.data.go.kr/data/15068779/fileData.do, 접근 2026-11-07, CSV 1,484행 직접 집계 — collect/G3-jobprep-count.md). 직업안정법 §23 신고 사업장 수 = 채용·구직 정보 사이트·앱·매체 운영자 전체(사람인·잡코리아·인크루트·링커리어·리멤버·코멘토·인프랩 포함, 건설 인력·지역 구인지도 포함). DevFit(제2026-31호)은 기준일 이후 신고라 미포함. ⛔ «취업 준비 서비스 1,484개»·«면접 대비 1,484곳» 금지 — 채용·구직 정보 서비스로만. 오른쪽 10곳과는 세는 단위가 다름.\n면접 대비 목록: last-dance/collect/G-competitors.md §1 (공개 페이지, 접근일 2026-11-05).\n- 일반 면접: 사람인(이력서+사람인 공고 한정) · 잘봐요(3자 블로그 출처) · 뷰인터(공식 본문 비어 있음) · Final Round AI · Huru · Yoodli · Big Interview. Google Interview Warmup은 2026-04 종료(3자 보도) → 취소선.\n- (이전 판) 개발자 기술면접 전용 5곳: 인프런 모의면접·꼬꼬면(국내) · Greenroom · interviewing.io · Pramp·Aced(해외) — 다음 장 비교표의 열.\n- 숫자 8(면접 대비)은 «조사 범위(G-competitors §1) 안의 개수»이지 시장 전체 집계가 아님 — Q&A에서 그렇게 답할 것. 범용 AI(ChatGPT·Claude)·고용주용(Emble·depthhire)·오픈소스는 세지 않음. 인프런 모의면접은 collect/G2-inflearn.md(2026-11-07, research-2) 반영.\n- 티오(TIO, 일반 취업 준비 AI): 공고 링크 분석 O, 업로드한 경험 자료·자기소개서 중심 → 코드 기반 질문 X (최종보고서 경쟁 표, 서비스 소개 페이지). 개발자 전용 아님이라 왼쪽 그룹.\n- 전체 조사 범위는 최종보고서와 같은 «국내외 36건(국내 18·해외 18), 2026-11 기준». 이 장의 9곳·10곳은 그중 화면에 올린 것.\n- 회사 로고는 쓰지 않음(BUILD.md 로고 예외는 멘토 소속 4개사뿐, 경쟁사 상표 사용 리스크).\n- «국내 상용 2곳» = 조사 범위 내 표현. techGiterview·Giterview(오픈소스·학생 프로젝트)는 상용 아님 — 질문 받으면 존재를 인정.\n⛔ «유일»·«최초»·«경쟁자 없음» 금지.')

# ---------- ④ 비즈니스 모델 (11-11 사용자 지시: B2C·B2B 하이브리드, B2C 근거 = 사용자 인터뷰) ----------


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
상태(11-10 사용자 메타): «B2C·B2B 둘 다 개발 완료. B2B는 개발 완료한 지 얼마 안 돼 기업들에 서비스 소개서를 보내 보는 중.» 근거: 최종보고서 43쪽 «MVP 개발 완료, 서비스 소개서로 기업 평가와 시장 검증 진행». 현업 검토(면접관·게임사 대표)는 부록 A13 참조.
Q&A 전용(장표·발화에서는 말하지 않음): 운영은 아직 비공개(출시 예정), 유료 고객·LOI·계약 0 — 물으면 사실대로.
⛔ «고객 확보»·«파일럿 진행 중»·«LOI 체결» 금지. ⛔ 평가표 점수는 면접관이 매기는 것 — «점수로 합격 판정» 뉘앙스 금지. 허용 표현은 «합불 판정 없음 · 최종 판단은 사람».
유출 방어 근거(중간평가 심사의견 #17 «면접 질문을 면접자에게 유출하는 플랫폼» 대응, feedback/05_세션별분석/2026-08-20_중간평가_대응현황.md D-2 · 00_공방표 A6):
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

# ---------- 부록 A23~A27: DevFit Enterprise 사용 설명서 (11-11 사용자 지시 «b2b 상세 내용을 어펜딕스에 사용설명서처럼») ----------
def entm(pages, cols):
    cells = ''.join(f'<figure><img src="assets/ef-entm-{n:02d}.jpg" alt="DevFit Enterprise 서비스 소개서 {n}쪽"><figcaption>소개서 {n}쪽</figcaption></figure>' for n in pages)
    return f'<div class="ef-entm c{cols}">{cells}</div>'
ENTM_SRC = 'DevFit Enterprise 서비스 소개서(2026-11 발행, 30쪽, devfit.app/enterprise.pdf) 원본 페이지 · 화면은 가상 데이터'
ENTM = [
    ('A23', '사용 설명서 1: <span class="purple">ATS + GitHub</span> 구성과 분석 범위', [6, 7, 8, 14], 2,
     '코드 면접 5가지 조건(이력서·공고 매칭 · 저장소 선별 · 본인 커밋 추출 · 질문 의도와 평가 가이드 · 구조화된 평가) → ATS 필수 기능 위에 GitHub 분석을 더한 구성 → ATS 기본 기능 4가지와 GitHub가 더하는 4가지(저장소 자동 매칭 · 연관 저장소 분석 · 브리프 자동 생성 · 코드 근거 평가) → 지원자 사전 동의 · 공개 저장소만 · AI는 합불 판정을 하지 않음 · 블라인드.'),
    ('A24', '사용 설명서 2: <span class="purple">코드 면접</span> (브리프 · 질문 가이드 · 커밋 근거)', [10, 11, 12, 13], 2,
     '면접 브리프(면접 10분 전 프로젝트 요약 · 핵심 질문 3~4개 · 관련 개념 · 원클릭 복사) → 질문 의도와 평가 가이드(출제 의도 · 배경지식 · 우수 답변 기준 · 심화 꼬리질문) → 질문마다 실제 커밋 Diff와 GitHub 원본 링크 → 지원자 목록에서 바로 펼쳐 보는 질문.'),
    ('A25', '사용 설명서 3: <span class="purple">채용 관리(ATS)</span> 대시보드 · 지원 접수 · 전형 단계', [16, 17, 18, 19, 20, 21], 3,
     '맞춤형 대시보드 → 로그인 없는 지원 페이지(사전 동의 2건) → 지원자 리스트 → 칸반 단계 설정 → 칸반 보드 → 지원자 상세 뷰.'),
    ('A26', '사용 설명서 4: <span class="purple">협업 평가</span> 코멘트 · 평가표 · 일정 · 메일', [22, 23, 24, 25, 26, 27], 3,
     '팀 코멘트와 타임라인 → 맞춤형 평가표(척도 · 가중치) → 팀 평가 리포트 → 블라인드 평가와 평가 요청 → 면접 일정 관리 → 안내 메일.'),
    ('A27', '사용 설명서 5: <span class="purple">블라인드 채용</span>과 기존 ATS 비교', [28, 29], 1,
     '블라인드 채용 설정 → 기존 ATS(그리팅 · 나인하이어)와 기능 비교표. 비교표에서 «외부 채용 플랫폼 지원서 연동 = 제공 예정», «Google 캘린더 연동 = 미지원» 두 줄을 숨기지 않음.'),
]
for _a, _t, _pages, _cols, _flow in ENTM:
    APX.append(shell(f'Appendix · {_a}', 'DevFit Enterprise ' + _t, entm(_pages, _cols), source=ENTM_SRC))
    APX.note(f"""[부록 · Q&A용] DevFit Enterprise 서비스 소개서를 페이지 그대로 실은 사용 설명서입니다. 흐름: {_flow}

본편 B2B 장(Enterprise)과 같은 소개서. 상태는 «개발 완료» — ⛔ «운영 중»·«고객 확보»·«파일럿 진행 중» 금지. 화면 속 회사·지원자는 가상 데이터. 면접 질문은 면접관 콘솔에서만 보이고 지원자 화면·B2C 질문과 공유하지 않음(본편 B2B 장 노트 근거).""")

# ================= 부록 → s5_appendix.py (11-07 사용자: 부록은 ppt-start 전담) =================

CSS += r"""
/* 2026-11-13: interview response, price rationale and hypothesis headings */
.ef-interview-findings{grid-template-columns:1fr 1.12fr;gap:20px}
.ef-interview-card{padding:24px 28px}
.ef-interview-card h3{font-size:28px}
.ef-interview-card blockquote{font-size:30px;line-height:1.4;margin-top:18px}
.ef-interview-card>p{font-size:24px;line-height:1.45;font-weight:700;margin:18px 0 0}
.ef-interview-requests{gap:22px;margin-top:24px;grid-template-columns:1fr 1.2fr}
.ef-interview-request b{font-size:26px;white-space:normal}
.ef-interview-request p{font-size:23px;line-height:1.5;white-space:normal}
.ef-market-pricing{grid-template-columns:680px 1fr;gap:30px;padding:0;align-items:center}
.ef-market-pricing .ef-circ{width:670px}
.ef-market-pricing .ef-one-r{gap:20px}
.ef-market-pricing .ef-one-k{margin:0;padding-bottom:18px}
.ef-price-basis{display:flex;flex-direction:column;gap:18px}
.ef-price-card{background:white;border:1px solid var(--line);border-radius:20px;padding:24px 28px}
.ef-price-label{font-size:24px;font-weight:900;color:var(--purple-deep)}
.ef-price-amount{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;font-size:27px;font-weight:800;margin:12px 0}
.ef-price-amount b{font-size:43px;line-height:1.1;letter-spacing:-.04em}
.ef-price-amount span{font-size:22px;color:var(--purple-deep)}
.ef-price-card p{font-size:22px;line-height:1.55;margin:0;font-weight:650;word-break:keep-all}
.ef-price-cost{background:var(--purple-pale);border-radius:15px;padding:20px 28px;display:flex;flex-direction:column;gap:7px}
.ef-price-cost b{font-size:27px;color:var(--purple-deep)}
.ef-price-cost span{font-size:22px;font-weight:700}
"""

CSS += r"""
.dc-priced .dc-box{padding:16px}
.dc-priced .dc-t th{padding:17px 8px;font-size:20px;line-height:1.35;vertical-align:top;color:var(--ink);word-break:keep-all}
.dc-priced .dc-t th:first-child{width:430px;padding-left:24px;vertical-align:middle}
.dc-priced .dc-t td{padding:9px 8px}
.dc-priced .dc-t td:first-child{font-size:23px;padding-left:24px}
.dc-price{display:block;color:var(--purple-deep);font-size:20px;font-weight:900;line-height:1.3;margin-top:13px;white-space:nowrap}
.dc-price-detail{display:block;font-size:16px;font-weight:700;color:var(--ink);line-height:1.4;margin-top:6px;white-space:normal}
.dc-priced .ef-line{font-size:30px;line-height:1.4;margin-top:12px!important;word-break:keep-all}
"""
