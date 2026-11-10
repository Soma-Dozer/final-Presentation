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
.ef-ent{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;width:100%;flex:1;min-height:0;align-items:center}
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
.ef-ent-r{position:relative;height:600px}
.ef-ent-r .ef-shot{position:absolute;padding:0;border-radius:18px}
.ef-ent-r .s1{left:0;top:0;width:86%;z-index:1}
.ef-ent-r .s2{right:0;bottom:0;width:62%;z-index:2;box-shadow:0 24px 60px rgba(20,16,40,.22)}
.ef-state{margin-top:14px;text-align:center;font-size:24px;font-weight:800;color:var(--muted);letter-spacing:-.03em}
.ef-state b{color:var(--ink);font-weight:900}

"""

# ================= 4. Effect =================
S.append(divider('04 · Effect', 'Effect', '6개월 수행 내용, 운영 지표, 비즈니스 모델, 비전'))
S.note('''[구분] Effect — 6개월 동안 무엇을 했고, 무엇이 남았는지.''')

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
장표에서 뺀 항목(2장 압축, 2026-11-07): 광고 수신 동의·약관 개정(09-09) · IT 기업 대표 서면 회신(10-26) · 김종욱 멘토 서비스 검증(10-25) · 전략 멘토링(11-02) — 멘토 건은 현업 검토 장표에서 다룸.
단건 결제 LIVE는 사용자 확인 완료(claims.md C3). 매출은 0.
⛔ 숭실대 취업박람회(09-09~10)는 실시일 미확인 → 넣지 않음. «1,880건 검증됨»·«검증된 기출» 금지(사람 검수 REVIEWED 0).
SBOM 차단 게이트 f7d2f42는 11-05 0fe63e1 승격으로 origin/prod 반영(merge-base 확인) → «HIGH·CRITICAL 1건 이상이면 배포 잡 중단 · 백엔드만»까지 허용, ⛔ «취약점 0건 = 안전»·«FE 포함» 금지.
⛔ «운영» 라벨 금지(main만): 11-02 멘토링 개선 4종 · 처리방침 OpenAI 고지 · Free 월 5회 축소.
토스 «계약 완료» 날짜(10-28)는 간접 → 장표에는 «결제 심사 연동(10-15)»만.''')

# ---------- ② 개발 외적으로 한 일 ---------- (근거: research/R2-ef-offdev.md · feedback/05_세션별분석)
def mrow(logo, alt, who, role, advice, works, todo=False):
    w = ''.join(f'<li>{x}</li>' for x in works)
    return f'''<div class="ef-mr{' todo' if todo else ''}">
  <div class="ef-mr-who"><b>{who}</b><small>{role}</small></div>
  <div class="ef-mr-adv">{advice}</div>
  <ul class="ef-mr-work">{w}</ul>
</div>'''
S.append(shell('Effect', '현업 면접관·게임사 대표의 <span class="purple">서비스 검토와 반영</span>', f"""
<div class="ef-mtab">
  <div class="ef-mh"><span>누구</span><span>조언</span><span>반영</span></div>
  {mrow('ef-logo-naver.png', 'NAVER', '김종욱 멘토', '네이버 검색 백엔드·AI', '10-25 Webex 약 2시간 서비스 검증. 지원자 분석 범위, 면접관 콘솔 완성도, 지원자 화면 동선까지 DevFit 전반을 실사용 관점에서 점검', ['조직 저장소 프로젝트도 지원자 분석 대상으로 연결', '면접관 콘솔 아이콘·공용 UI 정비, 모바일 하단 탭 추가', '면접관 랜딩에 콘솔 3단계 예시 데모 (채용 생성 → 접수·분석 → 면접 브리프)', '지원자 화면에서 모의면접을 준비의 첫 행동으로 배치'])}
  {mrow('ef-logo-kakao.svg', 'kakao', '한유일 멘토', '카카오 백엔드 · 면접관 경험', '중간·어려움 난이도는 "충분히 괜찮다"는 평가. 다만 쉬움 난이도는 코드 사실 확인 수준이라 실제 면접에서는 나오지 않는 질문. 면접관은 구조를 묻고 꼬리질문으로 파고든다는 조언', ['난이도·유형 분리로 저난도 추론형 질문 <b>1/8 → 7/9</b>', 'AI 코치 응답 잘림 수정 (출력 상한 1,280 → 8,192 토큰)', '모의면접 음성 답변·음성 꼬리질문 도입', '재로그인 시 비공개 레포 권한이 사라지던 문제 해소'])}
  {mrow('ef-logo-samsung.svg', 'SAMSUNG', '김한빛 멘토', '삼성전자 출신 · 팀 담당 멘토', '매주 정기 멘토링으로 질문 생성 로직·품질 평가 하네스·프롬프트 개선안을 주 단위로 검토. CI/CD 구성과 운영 비용 구조 점검', ['8축 루브릭 기반 질문 품질 평가 하네스 구축', '프롬프트 버전 A/B 비교 후 개선판 채택', '근거 diff 판별로 근거 밖 단정 질문 차단', '평가 결과를 다음 주 프롬프트 수정에 반영'])}
  {mrow('ef-logo-basakan.png', '바삭한소프트', '김준엽 대표', '바삭한소프트 공동대표 · 게임 개발', 'CS와 프로젝트 경험의 비중은 기업 인재상에 따라 상이. 포트폴리오 면접에서는 "왜 그 기술을 선택했는지, 그 선택이 최선이었는지"를 많이 물음. 자사는 이미 지원자 GitHub를 AI로 검토 중이라는 경쟁 관점의 지적', ['결정 이유·트레이드오프 질문 유형과 현업 평가 방식의 일치 확인', '"Claude Code에 링크를 넘기면 된다"는 반론을 비교 실험으로 검증', '본인 커밋만 선별 · 코드에 없는 식별자 질문 서버 폐기로 차별화'])}
</div>""", source='한유일 멘토 09-07 녹취(68분) · 김한빛 멘토 정기 멘토링 · 김종욱 멘토 10-25 Webex · 바삭한소프트 대표 10-26 이메일 회신'))
S.note('''[≈16초] 현업 면접관과 게임사 대표에게 서비스를 검토받고 반영했습니다. 카카오 한유일 멘토님이 쉬운 질문은 실제 면접에서 안 나온다고 지적하셔서 저난도 추론형 질문을 8개 중 1개에서 9개 중 7개로 늘렸습니다. 담당이신 삼성 출신 김한빛 멘토님과는 매주 만나 질문 품질 평가 하네스를 다듬었고, 기술면접이 까다로운 게임 개발 분야는 바삭한소프트 김준엽 대표님께 직접 여쭤 "왜 그 선택이었는지"를 묻는다는 답을 받았습니다.

근거: 한유일 멘토 09-07 녹취(feedback/01_녹취/2026-09-07_한유일멘토.txt, 68분) · 대응 feedback/05_세션별분석/2026-09-07_한유일멘토_대응현황.md (난이도·유형 분리 09-09 운영 반영, 저난도 반사실 질문 1/8→7/9 — ⛔ «12%→78%» 표기 금지(ppt-dev 관리), 음성 입력 BE 15e9e5d 등).
김한빛 멘토 = 팀 담당 멘토, 매주 정기 멘토링(사용자 확인 2026-11-06) · 09-22 CI/CD·비용 멘토링도 김한빛 멘토(사용자 확인). 반영 3건은 질문 품질 루프 기록: 8축 루브릭 평가(09-02) → 결함 31건 수정(09-08) → 프롬프트 v11·v12 A/B(10-15) → v13(10-16) · 근거 diff 판별 BE 48d58e7/f5bad96(10-24) — 출처 feedback/05_세션별분석/2026-08-20_중간평가_대응현황.md #2, 2026-09-22_CICD멘토링_대응현황.md #11. 개별 항목을 김한빛 멘토 한 분의 지적으로 단정하지 말 것(«정기 멘토링에서 함께 검토»).
김종욱 멘토 10-25 Webex «Dozer 팀 - 서비스 검증» 12:55~15:04 — 발언 기록 없음. 반영 4건은 사용자 지시(11-08)로 «미팅 직후 커밋»을 피드백 반영으로 넣은 것: 조직 저장소 연결 BE edeaee8(10-27, 박천웅) · 면접관 콘솔 정비 FE 6ec85b8(10-26) · 면접관 랜딩 데모 FE 4958c81(10-26) · 모의면접 우선 배치 FE c8a41b2(10-28) — 4건 모두 origin/prod 조상 확인(merge-base). 커밋 메시지에 멘토 언급 없음 → 미팅→반영 인과는 팀 주장(사용자 진술, claims.md C9 등록 11-08).
조언 칸(11-08 사용자 지시 «그냥 좀 써놔»): 발언 기록이 없어 반영 4건에서 거꾸로 적은 검토 주제(분석 범위·콘솔 완성도·화면 동선)임 — 멘토 발언 인용 아님, 따옴표 쓰지 않음.
⛔ 멘토 발언을 지어내 인용하지 말 것. Q&A «무슨 지적이었나» → «서비스 전반을 검증받고, 그 직후 면접관 콘솔과 지원자 분석 범위를 손봤다»까지만. 조언 칸에 멘토 발언 문장을 넣지 않음.
바삭한소프트: 김준엽 공동대표(이메일 서명 «바삭한소프트 김준엽», 공동대표 김준엽·차상근 — 아시아타임즈 2025-05-29·minimap 인터뷰). 10-23 한양대 청소년 비즈쿨 특강 → 10-26 이메일 회신. 회신 전제: 최근 1년은 기술면접을 직접 주도하지 않음 → 질문 품질 근거로 쓰지 않고 "현업 평가 방식"과 "경쟁 반론"으로만. 반론 비교 실험: 링크만 준 범용 AI 근거 0/18 · 레포를 읽힌 Claude Code 30/32 · DevFit 28/28 (collect/E-compare.md). 로고: 나무위키 문서의 회사 로고(원 출처 basakansoft.com, 현재 접속 불가).
로고: 회사 로고는 소속 표시로만 — 회사가 DevFit을 쓰거나 후원한다는 뜻이 아님. «각 회사에서 면접관 경험» · «전체 검토»는 claims.md C4. «기술면접이 까다로운 게임 개발» = C5 («가장» 금지).
추가 반영 항목 근거(collect/I-feedback-patterns.md §1-2): 한유일 09-07 → AI 코치 출력 상한 1280→8192 BE c5a3ac7(당일) · 음성 STT·TTS·음성 꼬리질문 BE 98ebb0f 등(09-16 운영) · private scope 보존 FE 61fbe10·BE 7399ff1(09-09·09-16). 김준엽 «CS·프로젝트 비중은 인재상 따라 상이»·«자사는 GitHub를 AI로 검토» = 10-26 회신 요지(05-현장검증.md §3). 김한빛 «주간 개선 루프»는 매주 멘토링 + 하네스 개선 이력(사용자 진술 11-06) 기반 서술.''')

# ---------- 법률 — 직업정보제공사업 신고 + 법률 멘토링 ----------
S.append(shell('Effect', '채용공고 서비스의 <span class="purple">직업정보제공사업 신고</span>와 법률 검토 · 개인정보 보호', """
<div class="ef-law">
  <div class="ef-law-l">
    <div class="ef-law-h"><b>직업정보제공사업 신고 완료</b></div>
    <div class="ef-law-stage">
      <div class="ef-law-doc"><img src="assets/cert-job.png" alt="직업정보제공사업 신고확인증"><span class="tag">신고확인증 · 서울청 제2026-31호</span></div>
      <div class="ef-law-act">
        <h4>직업안정법</h4>
        <p><b>제2조의2(정의)</b> 8. "직업정보제공사업"이란 신문, 잡지, 그 밖의 간행물 또는 유선ㆍ무선방송이나 컴퓨터통신 등으로 구인ㆍ구직 정보 등 직업정보를 제공하는 사업을 말한다.</p>
        <p><b>제23조(직업정보제공사업의 신고)</b> ① 직업정보제공사업을 하려는 자(제18조에 따라 무료직업소개사업을 하는 자와 제19조에 따라 유료직업소개사업을 하는 자는 제외한다)는 고용노동부장관에게 신고하여야 한다. 신고 사항을 변경하는 경우에도 또한 같다.</p>
        <p>② 제1항에 따른 신고 사항, 신고 절차, 그 밖에 신고에 필요한 사항은 대통령령으로 정한다.</p>
      </div>
    </div>
  </div>
  <div class="ef-law-r">
    <div class="ef-law-h"><b>서비스 전반 법률 검토 완료</b></div>
    <div class="ef-law-who"><span>⚖</span><div><b>법무법인 백상 김재철 변호사</b><small>소마 법률 멘토링 · 저작권 · 개인정보 · 특허·상표 · 직업정보 · 결제</small></div></div>
    <div class="ef-law-ops">
      <div class="ef-law-key"><small>법률 멘토 검토 의견 · 저작권</small>기출문제 크롤링·가공의 <span class="purple">저작권 침해 해당 없음</span></div>
      <div class="ef-law-key"><small>법률 멘토 조언 · 특허</small>출원 전 공개된 기술의 <span class="purple">공지예외주장 신청</span></div>
    </div>
    <div class="ef-law-pi"><small>개인정보 보호법에 따른 보호 조치 · 운영 코드 기준</small>
      <ul><li><i>§30</i>개인정보 처리방침 공개</li><li><i>§22</i>분석·광고 쿠키는 선택 동의로 분리</li><li><i>§29</i>GitHub 토큰 AES-256-GCM 암호화 · 세션 토큰 원문 미저장</li><li><i>§21</i>회원 탈퇴 시 계정 데이터 실제 삭제</li></ul></div>
  </div>
</div>""", source='신고확인증 원본 그대로 (자르거나 가리지 않음) · 직업안정법 [법률 제20121호, 2024. 1. 23., 일부개정] 국가법령정보센터 원문 · 법률 멘토링: 소마 공식 멘토링 게시판 기록'))
S.note('''[≈12초] DevFit은 채용공고를 모아 보여 주는 서비스라 직업안정법상 직업정보제공사업에 해당해서, 신고를 마쳤습니다. 그리고 소마 법률 멘토링에서 법무법인 백상 김재철 변호사님께, 기출문제를 크롤링하고 가공하는 것이 저작권 침해에 해당하지 않는다는 것을 포함해 서비스 전반을 검토받았고, 출원 전에 공개된 기술은 특허 공지예외주장을 신청하라는 조언도 받았습니다.

[증빙] 직업정보제공사업 신고확인증(서울청 제2026-31호, 신고일 2026-10-19) 원본 그대로. 법령 원문: 직업안정법 제2조의2 제8호 · 제23조, 법률 제20121호(2024. 1. 23. 일부개정, 2024. 7. 24. 시행), law.go.kr에서 2026-11-06 그대로 복사(개정 표기 «<개정 2010.6.4>»·«[전문개정 2009.10.9]»만 뺌). 신고확인증 본문에도 «직업안정법 제23조»가 적혀 있음.
법률 멘토링: 장표 표기 «법무법인 백상 김재철 변호사»(사용자 지시 2026-11-06). 소마 게시판 작성자 표기 «김재철»과 일치(사용자 확인 2026-11-06). 소마 멘토로서 진행한 멘토링이며 법무법인과의 자문 계약 아님. 소마 공식 «[자유 멘토링] Dozer(도저)팀 법률멘토링» — 2026-11-05 18:30~19:30 공식 일정(실제 약 2시간, 사용자 진술), 온라인 Webex, 작성자 김재철, 신청자 김건우·박천웅·노재원 (swmaestro.ai 멘토링 게시판, 사용자 캡처 11-06). 주제 크롤링·저작권 · 개인정보 · 특허·상표 · 직업정보·결제 · DevFit 전반(사용자 확인).
«기출문제 크롤링·가공 = 저작권 침해 해당 없음»은 멘토링 자리의 구두 검토 의견(사용자 진술 2026-11-06) — 서면 법률의견서·녹취 없음 → claims.md 등록 필요. Q&A에서 «법원 판단·법률의견서»로 말하지 않고 «법률 멘토 검토 의견»으로 답할 것.
«출원 전 공개 기술 → 특허 공지예외주장 신청» 조언도 같은 멘토링의 구두 조언(사용자 진술 2026-11-06, 서면·녹취 없음) → claims.md 등록 필요. 근거 법조: 특허법 제30조(공지 등이 되지 아니한 발명으로 보는 경우) — 공개일부터 12개월 이내 출원. 실제 신청 여부·대상 출원은 장표에서 말하지 않음.
개인정보 보호 조치(사용자 지시 11-07 추가) — 근거는 운영 코드(BE origin/prod d84cb1c · FE e9b4f2b, 2026-11-06): §30 처리방침 = devfit.app/privacy/(라이브 200, 2026-09-09 시행) · §22 선택 동의 = FE components/analytics/ConsentBanner.tsx «[선택] 이용 통계와 광고 성과 측정에 동의» · §29 = auth/GithubTokenCipher AES/GCM + auth/TokenStore «원문 토큰을 남기지 않고 SHA-256 지문만 저장» · §21 = user/UserDeletionService «비활성 표시가 아니라 물리 삭제»(채용 워크스페이스 소속 계정은 지원자 데이터 때문에 탈퇴 차단·안내).
⛔ «개인정보 보호법 완전 준수»·«위반 없음»·«법률 검토 통과» 금지. collect/K-compliance.md §1: 라이브 처리방침에 OpenAI(커밋 diff 국외 이전)·토스페이먼츠·Sentry·음성·업로드 문서가 아직 없음(11-07 curl 재확인, 시행일 9/9 그대로) → Q&A «비공개 코드가 어디로 가나요?»에 «AWS 안에서만»이라고 답하지 말 것. 처리방침 개정 전까지 장표는 «보호 조치»까지만.
순서 주의: 신고(10-19)가 멘토링(11-05)보다 먼저 → «멘토링 결과로 신고했다»고 말하지 않음. ⛔ 외부 법무법인 자문으로 말하지 않음 (claims.md C6).''')

def docimg(src, alt, ratio, cap=''):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="docimg" style="aspect-ratio:{ratio}"><img src="assets/{src}" alt="{alt}">{c}</div>'

import os as _os
BIZ_SRC = 'cert-biz.png' if _os.path.exists(_os.path.join(_os.path.dirname(OUT), 'assets', 'cert-biz.png')) else ''
def stackdoc(src, alt, cap, left, top, rot, z):
    return f'<div class="sd" style="left:{left}px;top:{top}px;transform:rotate({rot}deg);z-index:{z}"><img src="assets/{src}" alt="{alt}"><span class="tag">{cap}</span></div>'
pat = [('patent-a.png', '10-2026-0214808', '선별'), ('patent-b.png', '10-2026-0214809', '생성'), ('patent-c.png', '10-2026-0214811', '음성')]
S.append(shell('Effect', '결제를 위한 <span class="purple">사업자</span> 요건과 기술·이름 보호를 위한 <span class="purple">특허·상표</span> 출원', f'''
<div class="ev">
  <div class="ev-a">
    {stackdoc(BIZ_SRC, '사업자등록증', '① 사업자등록증', 0, 40, -2.2, 1)}
    {stackdoc('cert-mail.png', '통신판매업 신고증', '② 통신판매업 신고증', 270, 16, 0, 2)}
    {stackdoc('ef-trademark.png', 'DevFit 상표 출원공고결정서 (제42류, 출원번호 40-2026-0177374)', '③ 상표 출원공고 결정 · DevFit · 제42류', 540, 40, 2.2, 3)}
  </div>
  <div class="ev-b">
    {''.join(f"""<div class="sd p" style="left:{i*30}px;top:{16+i*196}px;z-index:{i+1}"><img src="assets/{f}" alt="{n} 출원번호통지서"><span class="tag">특허 출원 · {k} · {n}</span></div>""" for i, (f, n, k) in enumerate(pat))}
  </div>
</div>''', source='증빙 원본 스캔·캡처 그대로 (자르거나 가리지 않음) · 특허·상표는 출원 단계'))
S.note('''[≈12초] 결제를 받으려면 서류가 필요했습니다. 사업자등록과 통신판매업 신고를 마쳤고, DevFit 이름은 상표로, 핵심 기술은 특허 3건으로 출원했습니다.

[증빙] 사업자등록증(640-21-02214, 개업 2026-09-02, 서초세무서)·통신판매업 신고증(제2026-서울서초-3702호, 11-02)·특허 출원번호통지서 3건(11-01) · 상표 출원공고결정서(DevFit, 제42류, 출원번호 40-2026-0177374, 지식재산처 2026-11-06 발송, 상표법 제57조, 출원인 박천웅, 원본 ASM/devfit_출원공고결정서.pdf 1쪽) 원본 그대로(자르지 않고 가리지 않음).
상표: 출원공고 결정 = 심사 통과 후 공고 단계(이의신청 기간 남음), 등록 아님 → «출원공고 결정»까지만. ⛔ «상표 등록» 금지.
⛔ «매출» · «공동대표» · 특허 «등록»·«회사 특허» 금지 (출원인 김건우 개인, 발명자 3명, 심사청구 무). 특허 요지는 부록 A9.''')

# ---------- ③ 지표 — 유저 · 실운영 ----------
S.append(shell('Effect', '가입자 <span class="purple">90.4%</span>가 실제 공고로 준비 시작', '''
<div class="ef-stage"><div class="ef-two">
  <div class="ef-num"><b>90.4<small>%</small></b><span>가입 회원 83명 중 75명이<br>지원할 공고를 넣고 준비 카드 생성</span><i>게스트 체험 계정 제외</i></div>
  <div class="ef-num"><b class="k">81.9<small>%</small></b><span>가입 회원 83명 중 68명이<br>내 저장소 분석까지 도달</span><i>가입 대비 · 준비 카드 대비 90.7%</i></div>
</div></div>''', source='최종보고서 KPI (운영 DB, 2026-11-09 실측, 게스트 제외 GitHub 연동 회원 83명)'))
S.note('''[≈15초] 가입한 회원 83명 중 75명, 90.4%가 실제 지원할 공고를 넣고 준비 카드를 만들었습니다. 그중 68명, 가입 대비 81.9%가 자기 저장소 분석까지 갔습니다.

83명은 최종보고서 KPI와 같은 기준(게스트 체험 계정 제외 GitHub 연동 회원, 2026-11-09 실측). 퍼널: 가입 83 → 준비 카드 75(90.4%) → 저장소 분석 68(가입 대비 81.9% · 준비 카드 대비 90.7%). 원본 last-dance/kpi/kpi.html.
⚠ Dev 관리자 콘솔 캡처의 76 · 61 · 75.0%는 11-05 시점 내부 계정 포함 값 — 이 장과 기준이 다름. 발표 시 "앞 장 화면은 캡처 시점 값, 성과는 보고서 KPI 기준"으로 구분.
(이전 판 76% = 11-05 외부 79명 중 60명 · 126명 = 공고 등록 회원 64 + 비회원 62 — 보고서와 기준이 달라 뺌.)
Q&A용: 가입 30%가 밤 9시~새벽 1시 (자체 가입 데이터 기준 — «취준생은 밤에 준비한다» 같은 일반화는 하지 않음, 한국 외부 근거 없음).
Q&A용(장표에 넣지 않음): 모의면접 답변 작성은 15.7% — 보고서에도 다음 개선 과제로 적힌 수치. 질문 받으면 그대로 답하고, 답변 전환이 다음 목표라고 말함.
⛔ «400명대»·«393명»(비로그인 세션)을 활성화율 분모로 쓰지 않음.''')

S.append(shell('Effect', '출시 이후 <span class="purple">누적 가입자</span> 추이', '''
<div class="ef-col">
  <div class="ef-shot" style="width:100%;max-width:1600px"><img src="assets/ef-admin-growth.png" alt="관리자 콘솔 B2C 대시보드 — 누적 회원 수 8/7 7명에서 11/4 83명"></div>
  <div class="ef-line">관리자 콘솔 원본 화면 · 누적 회원 <span>8/7 7명 → 11/4 83명</span></div>
</div>''', source='관리자 콘솔 B2C 대시보드 "누적 회원 수" 패널 (2026-11-04 12:32 캡처, 패널만 잘라냄) · 캡처 시점 값 — 활성화 지표는 보고서 KPI(11-09, 게스트 제외 83명) 기준'))
S.note('''[≈15초] 앞의 숫자는 모두 우리가 만든 관리자 콘솔에서 셌습니다. 방문 분석 도구는 쿠키 동의나 봇 때문에 숫자가 크게 흔들려서, 가입·공고·분석·답변은 회원 DB를 정본으로 삼고 내부 계정을 빼고 셉니다. 8월 7일 7명에서 11월 4일 83명이 됐습니다.

이미지: metrics/screenshots/admin_b2c_growth_365d_20261104-1232.png 에서 «누적 회원 수» 패널만 자름(브라우저 주소창·북마크·계정 영역 제외).
측정 도구별 차이(Clarity 2.2만 · GA4 235 · DB 83)는 부록 A4. 계측 도구 구성 자체는 Development 파트 5에서 설명.''')

# ---------- 마케팅 · 유저 (11-10 ppt-start 요청 — 사용자: "마케팅, b2b, 유저") ----------
S.append(shell('Effect', '사용자 확보 경로 <span class="purple">5가지</span>: 검색 · 광고 · SNS · 현장 · 재방문', '''
<div class="ef-mk">
  <div class="ef-mk-list">
    <div class="ef-mk-row"><em class="k" style="font-style:normal">검색</em><b>CS 문서 172편<br>질문 875문항</b><span>직군 가이드 12종까지 페이지별 SEO · 문서에서 공고 분석으로 연결</span></div>
    <div class="ef-mk-row"><em class="k" style="font-style:normal">광고</em><b>₩347.5만</b><span>구글 + 메타 · 대기업 공채 시즌 집중 · 세부는 부록 A5</span></div>
    <div class="ef-mk-row"><em class="k" style="font-style:normal">SNS</em><b>UTM 캠페인 링크</b><span>스레드 · 인스타그램 게시물별 유입 · 가입 구분 (관리자 콘솔 생성기)</span></div>
    <div class="ef-mk-row"><em class="k" style="font-style:normal">현장</em><b>숭실대 취업 박람회</b><span>QR 3D 프린팅 클리커 굿즈 · 서비스 설명서 팜플렛 배포</span></div>
    <div class="ef-mk-row"><em class="k" style="font-style:normal">재방문</em><b>콜백 메일 · 알림</b><span>질문을 읽고 돌아오지 않은 회원 대상 메일 · 지원 일정 알림 · 면접 리뷰 안내</span></div>
  </div>
  <div class="ef-mk-ph">
    <figure class="a"><img src="assets/ef-fair.jpg" alt="숭실대학교 취업 박람회 현장 — DevFit 팜플렛을 건네는 모습"><figcaption>숭실대 취업 박람회 현장</figcaption></figure>
    <figure class="b"><img src="assets/ef-goods.jpg" alt="DevFit 팜플렛과 3D 프린팅 클리커 굿즈"><figcaption>팜플렛 · 클리커 굿즈</figcaption></figure>
  </div>
</div>''', source='최종보고서 «마케팅»(검색·광고·SNS·현장) · 광고비 Meta ₩233.8만 + Google ₩113.7만(부록 A5와 같은 값) · 사진: 최종보고서 그림 33 원본 · 팜플렛·굿즈 촬영본'))
S.note('''[≈15초] 사용자는 다섯 갈래로 모았습니다. CS 문서 172편과 면접 질문 875문항을 검색에 노출해 문서에서 공고 분석으로 이어지게 했고, 대기업 공채 시즌에 구글과 메타 광고를 집행했습니다. 스레드와 인스타그램은 게시물마다 캠페인 링크를 따로 만들어 어디서 가입했는지 구분했고, 숭실대 취업 박람회에서는 QR이 들어간 클리커 굿즈와 팜플렛을 나눴습니다. 한 번 쓰고 떠난 회원에게는 콜백 메일과 일정 알림으로 다시 부릅니다.

출처: 최종보고서 45쪽 «마케팅» 4갈래와 같은 범위 + 재방문(보고서 41쪽 관리자 콘솔 «콜백 메일» 화면, 여정 트래커 알림). 광고비 ₩347.5만 = Meta ₩233.8만 + Google ₩113.7만 — 부록 A5 «유료 광고»와 같은 값(가입 단가·자연 검색 한계는 A5에서).
사진: assets/ef-fair.jpg = 최종보고서 그림 33 왼쪽(박람회 현장) 원본 이미지 · assets/ef-goods.jpg = ~/Downloads/KakaoTalk_Photo_2026-11-07-23-47-28.jpeg(팜플렛 표지 + 클리커).
⚠ 박람회 날짜·배포 수량은 근거 없음 → 말하지 않음(보고서에도 없음).
⚠ 콜백 메일 규칙: 공고 질문을 처음 읽고 72시간 동안 다시 안 오면 발송 후보, 사용자별 14일에 최대 1건, 08~21시(callback-email-operations.md). 그 문서 시점엔 «운영 서버는 기능이 꺼져 있다» — 발송 건수·복귀율은 말하지 않음, «구축»까지만.
⛔ «바이럴»·«폭발적 유입» 같은 효과 주장 금지. 유입 효과 수치는 부록 A4·A5.''')

S.append(shell('Effect', '외부 회원이 준비한 공고 <span class="purple">83건</span> (토스 · 현대자동차 · 당근 등)', '''
<div class="ef-stage"><div class="ef-us">
  <div>
    <div class="ef-us-h">준비한 회사 · 고유 회원 수 (상위)</div>
    <div class="ef-bar"><span>토스 계열</span><i class="top" style="width:100%"></i><b>9명</b></div>
    <div class="ef-bar"><span>현대자동차</span><i style="width:44%"></i><b>4명</b></div>
    <div class="ef-bar"><span>롯데이노베이트</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-bar"><span>당근</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-bar"><span>SK하이닉스</span><i style="width:22%"></i><b>2명</b></div>
    <div class="ef-us-meta">포지션 <b>백엔드 34 · 프론트엔드 19</b> (공고의 64%)<br>출처 <b>채용 플랫폼 33</b>(원티드 16 · 잡코리아 12 · 사람인 5) · <b>기업 채용 사이트 18</b> · 텍스트 · 이미지 32</div>
  </div>
  <div class="ef-us-r">
    <div class="ef-num"><b>16<small>명</small></b><span>공고 2건 이상을 준비한 회원</span><i>공고 등록 회원의 27%</i></div>
    <div class="ef-num"><b class="k">14<small>명</small></b><span>가입 7일 뒤에도 다시 와서 활동</span><i>마지막 활동 시각 기준 근사치</i></div>
  </div>
</div></div>''', source='관리자 콘솔 회원별 상세 합산 (2026-11-04 집계, 내부 계정 4명 제외 외부 회원 79명 기준 · 게스트 공고 제외)'))
S.note('''[≈15초] 외부 회원들이 실제로 준비한 공고는 83건입니다. 토스 계열을 준비한 회원이 9명으로 가장 많고, 현대자동차, 롯데이노베이트, 당근, SK하이닉스가 뒤를 잇습니다. 백엔드와 프론트엔드가 공고의 64%입니다. 공고를 두 건 이상 준비한 회원이 16명, 가입하고 일주일이 지나서도 다시 와서 쓰는 회원이 14명입니다.

출처: collect/A-admin-usage.md §1-1·§4 (GET /b2c/members/{id} × 83명 합산, 2026-11-04, 내부 계정 user id 1·5·7·11 제외 → 외부 79명). 공고 83건 전부 집계(10건 초과 회원 없음). 게스트 공고 66건은 어드민 목록에 없어 제외.
기준 차이: 앞 활성화 장(83명·90.4%·81.9%)은 보고서 KPI(11-09, 게스트 제외 회원 83명) 기준, 이 장은 11-04 외부 79명 기준 — 숫자를 서로 섞지 않음. 공고 83건과 회원 83명은 우연히 같은 숫자.
회사: 고유 회원 수, 토스 계열 = 토스·토스증권·토스플레이스 등 합산. 1명짜리 회사명은 쓰지 않음(특정인 추정 방지), 회사 미입력 11명. 로고 쓰지 않음.
출처 구분: 채용 플랫폼 33(원티드 16 · 잡코리아 12 · 사람인 5) · 기업 채용 사이트 18(토스 7 · 현대차 4 · 롯데 2 · KT·풍산·그리팅·K뱅크·삼성 각 1) · URL 없음(텍스트 붙여넣기·이미지) 32.
16명 = 공고 2건 이상 등록 회원(공고 등록 회원 60명의 27%). 14명 = 가입 후 7일 이상 지나서도 활동 기록이 있는 회원(lastActivityAt 기준 재방문 근사치, 79명의 18%).
⛔ «팬 N명»·«열성 팬» 라벨 금지. ⛔ «토스 지원자가 많이 쓴다» 이상의 일반화 금지(칸 대부분 1~2명). 세트 완료·답변 수 같은 하위 수치는 넣지 않음.''')


# ---------- ④ 비즈니스 모델 ----------
S.append(shell('Effect', 'Plus 월 <span class="purple">7,900원</span>, 분석 약 24회분 변동비', '''
<div class="ef-stage"><div class="ef-bm">
  <div class="ef-shot"><img src="assets/ef-pricing.png" alt="devfit.app 요금 안내 화면 — DevFit Plus와 추가생성권 1,900원"></div>
  <div class="ef-rows">
    <div class="ef-row"><span>Plus 구독</span><b class="p">7,900원<small>/ 월</small></b></div>
    <div class="ef-row"><span>추가 생성권</span><b class="p">1,900원<small>/ 1회 · 11-02 LIVE</small></b></div>
    <div class="ef-row"><span>분석 1회 변동비</span><b>약 330원<small>저장소 3개</small></b></div>
    <div class="ef-row"><span>재분석</span><b>0원<small>코드 변경 없을 때</small></b></div>
  </div>
</div></div>''', source='요금 화면: devfit.app/pricing 운영 화면 · 변동비: 최종보고서 단위 경제성(CloudWatch 실측, 저장소 3개 기준) · 하루 무료 분석 10회는 그대로'))
S.note('''[≈17초] 무료로 시작하고, 음성 모의면접 같은 기능은 월 7,900원 Plus 구독으로, 같은 공고로 한 번 더 준비하고 싶을 때는 1,900원짜리 추가 생성권으로 씁니다. 분석 1회 변동비는 저장소 3개 기준 약 330원이고, 코드가 바뀌지 않았으면 재분석 비용은 들지 않습니다. Plus 한 달 요금이면 분석 약 24회분 변동비입니다. 추가 생성권 단건 결제는 11월 2일부터 열려 있습니다.

출처: 최종보고서 시장 규모와 수익 구조·단위 경제성 — 변동비 약 330원(저장소 3개, CloudWatch 실측, 공고 구조화·질문 생성 포함) · 저장소 20개 상한 약 1,404원 · 재분석 0원(최신 커밋 지문 같으면 결과 재사용) · Plus 7,900원 ≈ 분석 약 24회분(7,900 ÷ 330). Plus 3개월 무료 체험. 요금 화면 Devfit/.toss-build/prod-ppt-assets/pricing.png (2026-11-06 devfit.app/pricing 라이브 HTML과 문구 대조: 추가생성권·1,900·Plus 3개월 무료 체험 일치). 원가 상세는 부록 A7(330원 기준).
⛔ 정기결제(Plus)는 심사 중 — «계약 완료»·«구독 매출»로 말하지 않음. ⛔ «매출» 금지. ⛔ «60% 절감» 비교 금지(이전 판 «약 130원대»는 LLM 원장 08/30~ 기준이라 보고서와 기준이 달라 뺌).
Q&A: «결제는 열려 있고 매출은 아직 0» (claims.md C3, LIVE 사용자 확인).''')

# ---------- ⑤ 비전 ----------
S.append(shell('Effect', '면접을 준비하는 개발자 구직자 연간 <span class="purple">약 38.8만 명</span>', '''
<div class="ef-col">
  <div class="ef-num"><b>38.8<small>만 명</small></b><span>연간 개발 직군 지원 약 520만 건 ÷ 1인 평균 입사지원 13.4회</span><i>사람인 · 점핏 2025 상반기 260만 건 × 2 · 한국경제인협회 2025</i></div>
  <div class="ef-line" style="margin-top:20px">유료 전환 시나리오별 규모는 <span>부록 A11</span></div>
</div>''', source='점핏 "2025 상반기 개발자 채용 리포트" (jumpit.saramin.co.kr/report/2025/recruit) · 한국경제인협회 2025 구직자 조사(적극 구직자 평균 입사지원 13.4회) · 최종보고서 시장 규모와 수익 구조'))
S.note('''[≈15초] 저희 직접 시장은 면접을 준비하는 개발자 지원자입니다. 사람인과 점핏의 개발 직군 지원은 2025년 상반기에 약 260만 건이고, 하반기도 같은 규모라고 보면 한 해 약 520만 건입니다. 한 사람이 평균 13.4번 지원한다는 조사를 적용하면 연간 약 38만 8천 명의 구직자입니다.

계산: 2,601,390 × 2 ≈ 520만 건(하반기 동일 가정) ÷ 13.4회(한국경제인협회 2025, 적극 구직자 평균 입사지원 횟수) ≈ 38.8만 명. 최종보고서와 같은 계산.
출처: 점핏 리포트 원문 https://jumpit.saramin.co.kr/report/2025/recruit — 지원 2,601,390건(2025 1~6월, 사람인+점핏, 중복 제거 여부 미확인). research/R1-ef-market.md.
유료 전환 1/2/5% → 9,200만 / 1.84억 / 4.6억 원(1인 3개월 23,700원) 시나리오는 부록 A11. B2C 중심 — B2B 시장 수치는 쓰지 않음(보고서에도 없음).
(이전 판 «공고 9.2만·지원 260만» 장은 보고서 기준으로 교체.)
⛔ «매출 전망»으로 말하지 않음 — 시나리오 규모. ⛔ 5년 SOM 27억 · TAM $2.8B 금지(재현 불가).''')

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

# ---------- B2B — DevFit Enterprise (11-10 사용자 지시: 서비스 소개서 기준) ----------
S.append(shell('Effect', '채용 관리(ATS)와 GitHub 코드 면접을 합친 <span class="purple">DevFit Enterprise</span>', '''
<div class="ef-ent">
  <div class="ef-ent-l">
    <div class="ef-ent-box"><h4>채용 관리 (ATS)</h4><p>로그인 없는 지원 링크 · 전형 단계 칸반 · 맞춤형 평가표 · 팀 코멘트 · 블라인드 평가 · 면접 일정 · 안내 메일</p></div>
    <div class="ef-ent-plus">+</div>
    <div class="ef-ent-box cd"><h4>코드 면접</h4><ol><li>이력서 · 공고에 맞는 저장소 선별</li><li>지원자 본인 작성 커밋만 추출</li><li>질문 의도 · 평가 가이드 · 꼬리질문</li><li>구조화된 면접 평가</li><li>사전 동의 · 블라인드</li></ol></div>
  </div>
  <div class="ef-ent-r">
    <div class="ef-shot s1"><img src="assets/ef-ent-10.jpg" alt="DevFit Enterprise 면접 브리프 화면 — 프로젝트 요약과 핵심 질문"></div>
    <div class="ef-shot s2"><img src="assets/ef-ent-12.jpg" alt="DevFit Enterprise 커밋 근거 화면 — 지원자 커밋 Diff와 원본 링크"></div>
  </div>
</div>
<div class="ef-state"><b>개발 완료</b></div>''', source='DevFit Enterprise 서비스 소개서(2026-11 발행, 30쪽) 6·10·12쪽 · 화면: 서비스 소개서(가상 데이터)'))
S.note('''[≈15초] 기업용은 DevFit Enterprise입니다. 서류 접수부터 평가, 일정, 안내 메일까지 채용 관리 기본 기능 위에, 지원자 본인 커밋으로 하는 코드 면접을 얹었습니다. 면접관은 면접 10분 전에 브리프로 프로젝트 요약과 핵심 질문을 보고, 질문마다 근거가 된 커밋 diff와 GitHub 원본 링크를 확인합니다. 개발을 마쳤습니다.

출처: /Users/aiden/dev/teams/ASM/DevFit_enterprise_서비스소개서.pdf (2026-11 발행, 30쪽, devfit.app/enterprise.pdf). 포지셔닝 «ATS에 GitHub를 더하다»(표지) · 코드 면접 5요소(6쪽) · 면접 브리프(10쪽: 프로젝트 요약·핵심 질문 3~4개·관련 개념) · 커밋 근거(12쪽: 본인 커밋 필터링·Diff·해시·GitHub 원본 링크). 동의한 공개 저장소만 분석, AI는 합불을 판정하지 않음.
화면: 소개서 10·12쪽을 PDF에서 렌더해 잘라 씀(다시 그리지 않음). 소개서 고지 «본 소개서의 화면은 가상의 목업 데이터» → 화면 속 지원자·기업명은 실제 아님.
Q&A 비교(소개서 29쪽, 2026-11 각 사 공개 가이드 기준, DevFit vs 그리팅 · 나인하이어): GitHub 코드 분석 · 본인 커밋 Diff = DevFit만 제공 / 칸반 · 평가표 · 일정 메일 = 셋 다(나인하이어 평가표 일부) / 외부 채용 플랫폼 지원서 연동 = DevFit 제공 예정 / Google 캘린더 연동 = DevFit 미지원. 이 두 줄을 숨기지 않음.
상태(11-10 사용자 메타): «B2C·B2B 둘 다 개발 완료. B2B는 개발 완료한 지 얼마 안 돼 기업들에 서비스 소개서를 보내 보는 중.» 근거: 최종보고서 43쪽 «MVP 개발 완료, 서비스 소개서로 기업 평가와 시장 검증 진행». 현업 검토(면접관·게임사 대표)는 앞 «현업 검토» 장 참조.
Q&A 전용(장표·발화에서는 말하지 않음): 운영은 아직 비공개(출시 예정), 유료 고객·LOI·계약 0 — 물으면 사실대로.
⛔ «고객 확보»·«파일럿 진행 중»·«LOI 체결» 금지. ⛔ 평가표 점수는 면접관이 매기는 것 — «점수로 합격 판정» 뉘앙스 금지. 허용 표현은 «합불 판정 없음 · 최종 판단은 사람».''')

S.append(shell('Effect', 'B2C(운영 중)와 B2B(개발 완료)가 같은 분석 엔진을 쓰는 <span class="purple">하나의 채용 플랫폼</span>', f'''
<div class="ef-col">
  <div class="ef-vision"><img src="assets/vision-diagram.png" alt="DevFit Platform 비전 — B2C 준비와 B2B 검증을 하나의 개발자 채용 플랫폼으로"></div>
  <div class="ef-chips"><span>① B2C 준비 · 운영 중 · 결제 LIVE</span><span class="dev">② B2B Enterprise · 개발 완료</span><span>③ 공고 29곳 수집 · 지원 여정 트래커</span></div>
</div>''', source='비전 그림은 중간발표와 동일 · 초록 점 = 운영 중 · 빈 점 = 개발 완료'))
S.note('''[≈15초] 중간발표에서 말한 비전입니다. 지원자가 자기 코드로 준비하는 B2C와, 면접관이 근거로 검증하는 B2B를 같은 분석 엔진 위에서 하나의 개발자 채용 플랫폼으로 잇습니다. B2C는 공고 수집과 지원 일정 관리까지 운영 중이고, B2B는 개발을 마쳤습니다.

출처: Devfit/brand/platform/vision-diagram.png (중간발표와 같은 그림). B2B는 «면접관이 빠뜨린 확인 관점을 알려 주는 커버리지 어시스턴트»로 재정의(중간평가 #17 질문 유출 우려 대응 + 11-02 멘토링 제안).''')

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

# ================= 부록 → s5_appendix.py (11-07 사용자: 부록은 ppt-start 전담) =================
