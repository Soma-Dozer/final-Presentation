# -*- coding: utf-8 -*-
# 1부 — 표지 · Problem ①② · Solution ③④ · Key Features ⑤⑥⑦ · Live Demo (본편 1~9장) + 부록 A2·A3
# 담당: ppt-start · 공용 헬퍼/CSS는 core.py (ppt-start 관리) — 고칠 일이 있으면 ppt-start에 요청
# 장표 추가: S.append(shell(...)) 다음 줄에 S.note('''발표자 노트''') · 부록은 APX.append(shell('Appendix · A<n>', ...))
# 이 파일 전용 CSS는 아래 CSS 문자열에 넣는다 (클래스 이름 앞에 접두사 권장: in-)
from core import *

S = Slides()    # 본편 — 이 파일 순서 그대로 들어간다
APX = Slides()  # 부록 — A번호 순으로 자동 정렬
CSS = r"""
/* 장당 핵심 1개 — 큰 글자·한 장면 (참고: ASM/최종발표_ppt.pdf) */
.in-stage{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.in-chat{display:grid;grid-template-columns:1fr 1fr;gap:90px;align-items:center;width:100%}
.in-who{font-size:24px;font-weight:900;color:var(--muted);margin-bottom:18px;letter-spacing:-.02em}
.in-qs{display:flex;flex-direction:column;gap:22px}
.in-q{align-self:flex-start;background:#fff;border:2px solid var(--line);border-radius:28px 28px 28px 6px;padding:26px 40px;font-size:46px;font-weight:900;letter-spacing:-.045em;box-shadow:var(--shadow)}
.in-q:nth-child(2){margin-left:80px}
.in-q{font-size:40px;line-height:1.3}
.in-qw{display:block;margin-top:10px;font-size:20px;font-weight:800;color:var(--muted);letter-spacing:-.02em}
.in-a{background:var(--red-soft);border-radius:28px 28px 6px 28px;padding:48px 54px;font-size:56px;font-weight:900;line-height:1.35;letter-spacing:-.05em;color:var(--ink)}
.in-a em{font-style:normal;color:var(--red)}
.in-nums{display:grid;grid-template-columns:1fr 1fr;gap:120px;width:100%;padding:0 40px}
.in-num b{display:block;font-size:220px;font-weight:900;line-height:1;letter-spacing:-.06em;color:var(--purple)}
.in-num b.r{color:var(--red)}
.in-num span{display:block;margin-top:26px;font-size:34px;font-weight:800;line-height:1.4;letter-spacing:-.04em;color:var(--ink);word-break:keep-all}
.in-num small{display:block;margin-top:12px;font-size:22px;font-weight:700;color:var(--muted)}
.in-trio{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;width:100%}
.in-t{background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:44px 40px;text-align:center}
.in-t .k{font-family:var(--mono);font-size:58px;font-weight:900;color:var(--purple);letter-spacing:-.03em}
.in-t .v{margin-top:14px;font-size:34px;font-weight:900;letter-spacing:-.045em}
.in-eq{margin-top:60px;text-align:center;font-size:44px;font-weight:900;letter-spacing:-.045em}
.in-eq span{color:var(--purple)}
.in-col{display:flex;flex-direction:column;width:100%;height:100%}
.in-vs{display:grid;grid-template-columns:1fr 1fr;gap:40px;width:100%}
.in-v{border-radius:30px;padding:56px 60px;text-align:center}
.in-v.r{background:var(--red-soft)}.in-v.p{background:var(--purple-pale)}
.in-v .k{font-size:30px;font-weight:900;color:var(--muted)}
.in-v b{display:block;margin:16px 0 10px;font-size:180px;font-weight:900;line-height:1;letter-spacing:-.06em}
.in-v.r b{color:var(--red)}.in-v.p b{color:var(--purple)}
.in-v span{font-size:30px;font-weight:800;color:var(--ink)}
.in-line{margin-top:46px;text-align:center;font-size:38px;font-weight:900;letter-spacing:-.045em}
.in-line span{color:var(--purple)}
.in-sub{text-align:center;font-size:26px;font-weight:700;color:var(--muted);margin-bottom:34px}
.in-cmp{width:100%;border-collapse:separate;border-spacing:0 16px}
.in-cmp th{font-size:28px;font-weight:900;color:var(--muted);padding:0 30px 6px;text-align:left}
.in-cmp th.d{color:var(--purple)}
.in-cmp td{background:#fff;padding:30px;font-size:36px;font-weight:800;letter-spacing:-.04em;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.in-cmp td:first-child{border-left:1px solid var(--line);border-radius:20px 0 0 20px;color:var(--muted);font-size:28px;width:24%}
.in-cmp td:last-child{border-right:1px solid var(--line);border-radius:0 20px 20px 0;background:var(--purple-pale);color:var(--purple-deep);font-weight:900}
/* 보강 (2026-11-06 v2) */
.in-lv{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;gap:12px;align-items:stretch;word-break:keep-all}
.in-lv>div{background:#fff;border:1px solid var(--line);border-radius:24px;padding:32px 26px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:12px;min-height:380px}
.in-lv em{font-style:normal;font-size:24px;font-weight:900;color:var(--muted)}
.in-lv h4{margin:6px 0 0;font-size:36px;line-height:1.3;font-weight:900;letter-spacing:-.05em}
.in-lv p{margin:auto 0 0;font-size:22px;font-weight:800;line-height:1.4;letter-spacing:-.03em}
.in-lv p b{font-size:30px;color:var(--purple)}
.in-lv small{font-size:16px;color:var(--muted);font-weight:700}
.in-lv>div.on{background:var(--red-soft);border-color:transparent}.in-lv>div.on h4,.in-lv>div.on p b{color:var(--red)}
.in-lv i{font-style:normal;font-size:28px;font-weight:900;color:var(--muted);align-self:center}
.in-lvbar{margin-top:30px;background:var(--dark);color:#fff;border-radius:20px;padding:26px 34px;display:flex;align-items:center;gap:24px;word-break:keep-all}
.in-lvbar b{font-size:28px;font-weight:900;color:#b9b0ff;white-space:nowrap}
.in-lvbar span{font-size:27px;font-weight:800;letter-spacing:-.035em;line-height:1.4}
.in-lvbar em{font-style:normal;color:#ff8a8a}
.in-lvbar small{margin-left:auto;font-size:16px;color:#9a93a0;font-weight:600;white-space:nowrap}
.in-grow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1.2fr;gap:14px;align-items:end}
.in-grow>div{background:#fff;border:1px solid var(--line);border-radius:24px;padding:26px 28px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:6px;min-height:calc(330px * var(--s))}
.in-grow em{font-style:normal;font-size:22px;font-weight:800;color:var(--muted)}
.in-grow b{font-size:calc(96px * var(--s));font-weight:900;letter-spacing:-.05em;line-height:1;margin-top:auto}
.in-grow small{font-size:18px;color:var(--muted);font-weight:700}
.in-grow>div.on{background:var(--red-soft);border-color:transparent}.in-grow>div.on b{color:var(--red)}
.in-grow i{font-style:normal;font-size:30px;font-weight:900;color:var(--muted);align-self:center}
.in-growcap{margin-top:16px;font-size:19px;color:var(--muted);font-weight:700;text-align:right}
.in-grow2{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:30px}
.in-grow2>div{background:var(--dark);color:#fff;border-radius:20px;padding:24px 32px;display:flex;align-items:center;gap:26px}
.in-grow2 b{font-size:46px;font-weight:900;letter-spacing:-.05em;color:#b9b0ff;white-space:nowrap}
.in-grow2 span{font-size:22px;font-weight:800;line-height:1.4;letter-spacing:-.03em}
.in-grow2 small{font-size:16px;color:#9a93a0;font-weight:600}
.in-mkt{display:grid;grid-template-columns:1fr 1fr 1.1fr;gap:24px}
.in-mkt>div{background:#fff;border:1px solid var(--line);border-radius:26px;padding:38px 34px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:12px;min-height:380px}
.in-mkt h5{margin:0;font-size:24px;font-weight:900;color:var(--muted)}
.in-mkt b{font-size:84px;font-weight:900;letter-spacing:-.055em;line-height:1.05}
.in-mkt span{font-size:26px;font-weight:800;line-height:1.4;letter-spacing:-.035em}
.in-mkt small{margin-top:auto;font-size:18px;color:var(--muted);font-weight:700}
.in-mkt>div.on{background:var(--red-soft);border-color:transparent}.in-mkt>div.on b,.in-mkt>div.on h5{color:var(--red)}
.in-iv{display:grid;grid-template-columns:1.05fr 1fr;gap:60px;align-items:start}
.in-ivq{display:flex;flex-direction:column;gap:22px}
.in-ivq .in-q{font-size:36px}
.in-ivc{display:flex;flex-direction:column;gap:16px}
.in-ivc>div:not(.in-who){background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px 28px;box-shadow:var(--shadow);display:grid;grid-template-columns:150px 1fr auto;gap:16px;align-items:center}
.in-ivc b{font-size:26px;font-weight:900}
.in-ivc span{font-size:23px;font-weight:800;letter-spacing:-.03em;line-height:1.35}
.in-ivc small{font-size:17px;color:var(--muted);font-weight:700}
.in-grow,.in-mkt,.in-iv{word-break:keep-all}
.in-scn{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1.15fr;gap:14px;align-items:stretch}
.in-scn>div{background:#fff;border:1px solid var(--line);border-radius:26px;padding:40px 32px;min-height:400px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:12px}
.in-scn b{width:52px;height:52px;margin-bottom:10px;border-radius:50%;background:var(--ink,#121016);color:#fff;display:grid;place-items:center;font-size:20px;font-weight:900}
.in-scn h4{margin:0;font-size:38px;line-height:1.3;font-weight:900;letter-spacing:-.045em}
.in-scn p{margin:0;font-size:25px;margin-top:auto;color:var(--muted);font-weight:700;line-height:1.4}
.in-scn small{display:block;font-size:18px;margin-top:6px;color:var(--muted);font-weight:600}
.in-scn>div.on{background:var(--red-soft);border-color:transparent}
.in-scn>div.on b{background:var(--red)}.in-scn>div.on h4{color:var(--red)}.in-scn>div.on p{color:var(--ink,#121016)}
.in-scn i{font-style:normal;font-size:30px;font-weight:900;color:var(--muted);align-self:center}
.in-scnbar{margin-top:44px;background:#121016;color:#fff;border-radius:20px;padding:32px 40px;font-size:36px;font-weight:800;letter-spacing:-.04em}
.in-scnbar em{font-style:normal;color:#ff8a8a}
.in-scnbar small{font-size:19px;color:#9a93a0;margin-left:14px;font-weight:600}
.in-flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:20px;align-items:center;margin-top:50px}
.in-flow div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 24px;text-align:center;font-size:25px;font-weight:800;letter-spacing:-.03em}
.in-flow div.on{background:var(--red-soft);border-color:transparent;color:var(--red)}
.in-flow i{font-style:normal;font-size:30px;font-weight:900;color:var(--muted)}
.in-nums3{display:grid;grid-template-columns:1fr 1fr .8fr;gap:60px;width:100%;align-items:end}
.in-num.s b{font-size:150px;color:var(--ink)}
.in-num.s span{font-size:28px}
.in-p5{display:grid;grid-template-columns:1.15fr 1fr;gap:72px;width:100%;align-items:stretch}
.in-p5 .st{display:flex;flex-direction:column;gap:56px;justify-content:center}
.in-p5 .row{display:grid;grid-template-columns:340px 1fr;align-items:center;gap:40px}
.in-p5 .row b{font-size:150px;font-weight:900;line-height:1;letter-spacing:-.06em;color:var(--purple)}
.in-p5 .row b.r{color:var(--red)}
.in-p5 .row span{display:block;font-size:32px;font-weight:800;line-height:1.4;letter-spacing:-.04em;color:var(--ink);word-break:keep-all}
.in-p5 .row small{display:block;margin-top:10px;font-size:21px;font-weight:700;color:var(--muted)}
.in-p5 .qt{display:flex;flex-direction:column;justify-content:center;padding:56px 60px;background:#fff;border-radius:8px;box-shadow:0 2px 24px rgba(20,16,40,.06)}
.in-p5 .qt .mk{font-size:120px;font-weight:900;line-height:.6;color:var(--red);height:56px}
.in-p5 .qt blockquote{margin:0;font-size:44px;font-weight:800;line-height:1.45;letter-spacing:-.045em;color:var(--ink);word-break:keep-all}
.in-p5 .qt small{display:block;margin-top:28px;font-size:22px;font-weight:700;color:var(--muted)}
.in-num.q blockquote{margin:0;padding-left:28px;border-left:8px solid var(--red);font-size:36px;font-weight:800;line-height:1.45;letter-spacing:-.04em;color:var(--ink);word-break:keep-all}
.in-bar{margin-top:56px;background:var(--dark);color:#fff;border-radius:20px;padding:26px 36px;text-align:center;font-size:32px;font-weight:900;letter-spacing:-.04em}
.in-bar span{color:#b9b0ff}
.in-gh{display:grid;grid-template-columns:.85fr 1.15fr;gap:46px;width:100%;height:100%;min-height:0;align-items:stretch}
.in-gh .in-t{display:flex;align-items:center;gap:30px;text-align:left;padding:30px 36px}
.in-gh .in-t .k{width:170px;font-size:46px}
.in-gh .in-t .v{margin:0;font-size:32px}
.in-gh .in-t small{display:block;font-size:20px;font-weight:700;color:var(--muted);margin-top:6px}
.in-stack{display:flex;flex-direction:column;gap:22px;justify-content:center}
.in-arrow{text-align:center;font-size:26px;font-weight:900;color:var(--purple)}
.in-shot{display:flex;flex-direction:column;min-height:0}
.in-shot .cap{font-size:22px;font-weight:900;color:var(--purple-deep);margin-bottom:12px}
.in-shot .browser{flex:1;min-height:0}
.in-dp-pipe{flex:1;display:grid;grid-template-columns:470px 110px 1fr 90px 560px;align-items:center;margin-top:6px;min-height:0}
.in-dp-pin{display:flex;flex-direction:column;gap:56px}
.in-dp-src{display:flex;gap:20px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:24px;padding:26px;box-shadow:var(--shadow)}
.in-dp-srcic{flex:none;width:74px;height:74px;border-radius:20px;background:var(--purple-pale);color:var(--purple);display:grid;place-items:center}
.in-dp-srcic.gh{background:#1f1d24}.in-dp-srcic.gh img{width:42px}
.in-dp-src>div:last-child{flex:1;min-width:0}
.in-dp-srck{font-size:28px;font-weight:900;letter-spacing:-.03em;margin-bottom:12px}
.in-dp-doc{display:flex;flex-direction:column;gap:9px}
.in-dp-doc i{display:block;height:10px;border-radius:5px;background:#eceaf2}.in-dp-doc i:last-child{width:62%}
.in-dp-doc mark{background:var(--amber-soft);color:var(--ink);border-radius:8px;padding:6px 12px;font-size:22px;font-weight:800;letter-spacing:-.03em;width:fit-content}
.in-dp-doc mark.g{background:var(--green-soft)}
.in-dp-pa{height:520px}.in-dp-pa svg{width:100%;height:100%;display:block}
.in-dp-eng{background:linear-gradient(160deg,#5b4bd6,#3c2f9e);color:#fff;border-radius:32px;padding:38px 34px;box-shadow:0 24px 60px rgba(76,60,200,.32)}
.in-dp-engh{display:flex;align-items:center;gap:14px;font-size:36px;font-weight:900;margin-bottom:26px}.in-dp-engh img{width:52px;height:52px;border-radius:14px;background:#fff;padding:6px}
.in-dp-eng ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:18px}
.in-dp-eng li{display:flex;gap:16px;align-items:center;font-size:27px;font-weight:800;letter-spacing:-.03em;line-height:1.3;background:rgba(255,255,255,.12);border-radius:16px;padding:16px 18px}
.in-dp-eng li b{flex:none;width:40px;height:40px;border-radius:50%;background:#fff;color:#4b3cc4;display:grid;place-items:center;font-size:22px}
.in-dp-pout{display:flex;flex-direction:column;gap:24px}
.in-dp-q{background:#fff;border:3px solid var(--purple);border-radius:28px;padding:30px 32px;box-shadow:var(--shadow)}
.in-dp-qk{font-size:23px;font-weight:900;color:var(--purple)}
.in-dp-qb{font-size:36px;font-weight:900;line-height:1.35;letter-spacing:-.04em;margin:14px 0 18px;color:var(--ink)}
.in-dp-qref{display:inline-block;background:var(--green-soft);border-radius:10px;padding:8px 14px;font-size:21px;font-weight:800;color:var(--ink)}
.in-dp-loop{display:flex;align-items:center;gap:12px;justify-content:center;font-size:24px;font-weight:800}
.in-dp-loop span{display:flex;align-items:center;gap:8px;color:var(--purple-deep);padding:4px 0}
.in-dp-loop i{font-style:normal;color:var(--muted);font-weight:900}.in-dp-loop em{font-style:normal;font-size:34px;color:var(--purple);font-weight:900}
.in-hn{display:grid;grid-template-columns:1fr 470px;gap:28px;width:100%;height:100%;align-items:stretch;padding-top:10px;word-break:keep-all}
.in-hnl{display:flex;flex-direction:column;gap:26px;justify-content:center}
.in-lane{border-radius:28px;padding:28px 32px;display:grid;grid-template-columns:1fr 250px;grid-template-rows:auto 1fr;column-gap:20px;row-gap:22px;align-items:center}
.in-lane.bad{background:var(--red-soft)}
.in-lane.good{background:#fff;border:3px solid var(--purple);box-shadow:var(--shadow)}
.in-lanek{grid-column:1/-1;font-size:28px;font-weight:900;letter-spacing:-.03em}
.in-lane.bad .in-lanek{color:var(--red)}.in-lane.good .in-lanek{color:var(--purple-deep)}
.in-lanef{display:flex;align-items:center;gap:10px}
.in-lanef>span,.in-har span{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 16px;font-size:22px;font-weight:800;letter-spacing:-.03em;white-space:nowrap}
.in-lanef i{font-style:normal;font-size:26px;font-weight:900;color:var(--muted)}
.in-lanef span.llm,.in-har span.llm{background:#1f1d24;color:#fff;border-color:transparent}
.in-har{flex:1;background:var(--purple-pale);border:2px dashed var(--purple);border-radius:18px;padding:12px 14px}
.in-har em{display:block;font-style:normal;font-size:18px;font-weight:900;color:var(--purple);margin-bottom:10px}
.in-har>div{display:flex;flex-wrap:nowrap;gap:7px}
.in-har span{padding:9px 11px;font-size:19px}
.in-har span.chk{border:2px solid var(--purple);color:var(--purple-deep)}
.in-laner{display:flex;flex-direction:column;align-items:flex-end;text-align:right}
.in-laner b{font-size:80px;font-weight:900;letter-spacing:-.05em;line-height:1}
.in-lane.bad .in-laner b{color:var(--red)}.in-lane.good .in-laner b{color:var(--purple)}
.in-laner small{margin-top:10px;font-size:19px;font-weight:700;color:var(--muted);line-height:1.4}
.in-hnr{display:flex;flex-direction:column;gap:26px;justify-content:center}
.in-hnc{background:#121016;color:#fff;border-radius:28px;padding:40px 36px;font-size:46px;font-weight:900;letter-spacing:-.045em;line-height:1.25}
.in-hnc em{font-style:normal;color:#b9b0ff}
.in-hnc small{display:block;margin-top:20px;font-size:21px;font-weight:700;color:#c9c4d4;line-height:1.5;letter-spacing:-.02em}
.in-hne{background:#fff;border:1px solid var(--line);border-radius:28px;padding:28px 36px;box-shadow:var(--shadow)}
.in-hnek{font-size:20px;font-weight:900;color:var(--muted)}
.in-hnen{display:flex;align-items:baseline;gap:16px;margin:10px 0}
.in-hnen b{font-size:60px;font-weight:900;letter-spacing:-.05em;color:var(--muted)}.in-hnen b.p{color:var(--purple)}
.in-hnen i{font-style:normal;font-size:36px;font-weight:900;color:var(--muted)}
.in-hne small{font-size:18px;font-weight:700;color:var(--muted);line-height:1.45}
.in-chips{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:24px}
.in-chips span{background:#fff;border:1px solid var(--line);border-radius:6px;padding:12px 24px;font-size:23px;font-weight:800;letter-spacing:-.03em}
.in-chips span b{color:var(--purple)}
.in-quotes{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:34px}
.in-quotes div{background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px 28px;font-size:26px;font-weight:800;letter-spacing:-.03em}
.in-quotes small{display:block;margin-top:6px;font-size:18px;color:var(--muted);font-weight:700}
.in-gate{display:flex;gap:16px;justify-content:center;align-items:center;margin-top:30px;font-size:24px;font-weight:800}
.in-gate span{border-radius:14px;padding:12px 22px}
.in-gate .k{background:var(--green-soft);color:var(--green)}.in-gate .a{background:var(--amber-soft);color:var(--amber)}.in-gate .d{background:var(--red-soft);color:var(--red)}
.in-gate em{font-style:normal;color:var(--muted)}
.in-h{display:grid;grid-template-columns:1fr 1.1fr;gap:50px;width:100%;align-items:center}
.in-quiz{background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:36px 40px}
.in-quiz .q{background:var(--purple-pale);border-radius:16px;padding:20px 24px;font-size:26px;font-weight:900}
.in-quiz .q small{display:block;font-size:18px;color:var(--muted);font-weight:700;margin-bottom:4px}
.in-quiz .ar{text-align:center;margin:16px 0;font-size:22px;font-weight:800;color:var(--muted)}
.in-quiz .op{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.in-quiz .op div{border:2px solid var(--line);border-radius:14px;padding:16px 20px;font-size:22px;font-weight:800}
.in-quiz .op div.hit{border-color:var(--purple);background:var(--purple-pale);color:var(--purple-deep)}
.in-own{display:flex;gap:16px;justify-content:center;margin-top:28px;font-size:24px;font-weight:800;align-items:center}
.in-own span{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 22px}
.in-own b{color:var(--purple)}
/* 6장 — 하네스가 차별점 (11-02 멘토 근거) */
.in-mq{background:var(--purple-pale);border-radius:28px;padding:34px 46px;display:grid;grid-template-columns:auto 1fr;gap:34px;align-items:center}
.in-mq .mk{font-size:120px;font-weight:900;line-height:.7;color:var(--purple);font-family:Georgia,serif}
.in-mq .t{font-size:38px;font-weight:900;line-height:1.42;letter-spacing:-.045em;color:var(--ink);word-break:keep-all}
.in-mq .t em{font-style:normal;color:var(--purple)}
.in-mq .mw{margin-top:12px;font-size:21px;font-weight:800;color:var(--muted)}
.in-hk{margin:34px 0 12px;font-size:24px;font-weight:900;color:var(--purple-deep)}
.in-pipe{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.in-pipe div{position:relative;background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 18px;text-align:center;box-shadow:var(--shadow)}
.in-pipe div b{display:block;font-size:26px;font-weight:900;letter-spacing:-.04em}
.in-pipe div span{display:block;margin-top:6px;font-size:18px;font-weight:700;color:var(--muted)}
.in-pipe div.g{border:2px solid var(--purple)}
.in-pipe div:not(:last-child)::after{content:'→';position:absolute;right:-14px;top:50%;transform:translate(50%,-50%);font-size:22px;font-weight:900;color:var(--muted);z-index:2}
.in-ext{margin-top:14px;font-size:20px;font-weight:700;color:var(--muted)}.in-ext b{color:var(--ink,#121016);font-weight:900}.in-ext span{font-size:16px}
.in-ghx{gap:0;justify-content:center}
.in-ghx,.in-scn,.in-col{word-break:keep-all}
.in-ghtop{display:grid;grid-template-columns:330px 1fr;gap:56px;align-items:center}
.in-ghlogo{background:#24292e;border-radius:28px;height:330px;display:flex;align-items:center;justify-content:center}
.in-ghlogo img{width:190px;height:190px}
.in-ghcopy .lead{font-size:31px;font-weight:700;line-height:1.5;margin:0;letter-spacing:-.02em}.in-ghcopy .lead b{color:var(--purple);font-weight:900}
.in-ghcopy .aud{font-size:22px;color:var(--muted);font-weight:700;margin:14px 0 0}
.in-ghstats{display:flex;gap:64px;margin-top:30px}.in-ghstats b{display:block;font-size:56px;font-weight:900;letter-spacing:-.04em;line-height:1.1}.in-ghstats span{font-size:20px;font-weight:800;color:var(--muted)}
.in-ghsteps{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:44px}
.in-ghsteps div{background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px 26px;box-shadow:var(--shadow);position:relative}
.in-ghsteps div:not(:last-child)::after{content:"→";position:absolute;right:-17px;top:50%;transform:translateY(-50%);color:var(--muted);font-weight:900;font-size:18px}
.in-ghsteps em{font-style:normal;font-family:ui-monospace,Menlo,monospace;font-size:20px;font-weight:800;color:var(--purple)}
.in-ghsteps b{display:block;font-size:25px;font-weight:900;margin-top:6px}.in-ghsteps span{display:block;font-size:18px;color:var(--muted);font-weight:700;margin-top:4px}
.in-ghcall{margin-top:26px;background:var(--ink,#121016);color:#fff;border-radius:18px;padding:20px 30px;font-size:26px;font-weight:900;text-align:center}
.in-proof{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:30px}
.in-proof div{border-radius:20px;padding:20px 30px;display:flex;align-items:center;gap:26px}
.in-proof div.r{background:var(--red-soft)}.in-proof div.p{background:#fff;border:2px solid var(--purple)}
.in-proof b{font-size:64px;font-weight:900;letter-spacing:-.05em;line-height:1}
.in-proof div.r b{color:var(--red)}.in-proof div.p b{color:var(--purple)}
.in-proof span{font-size:22px;font-weight:800;line-height:1.4}
.in-proof small{display:block;font-size:17px;color:var(--muted);font-weight:700}
.in-claim{background:var(--dark);color:#fff;border-radius:26px;padding:30px 44px;font-size:40px;font-weight:900;line-height:1.4;letter-spacing:-.045em;text-align:center}
.in-claim em{font-style:normal;color:#b9b0ff}
.in-claim small{display:block;margin-top:8px;font-size:22px;font-weight:700;color:#c9c4d0;letter-spacing:-.02em}
"""

# ================= 01 표지 =================
S.append(raw('cover', f'''<div class="slide-shell"><div class="cover-grid">
  <div class="cover-copy">
    <div class="cover-kicker">GitHub 커밋 기반<br>공고 맞춤 기술면접 준비</div>
    <div class="cover-wordmark"><img src="assets/icon.svg" alt=""><span>Dev<b>Fit</b></span></div>
    <div class="cover-tagline">내 <b>코드</b>로 준비하는 공고 맞춤 기술면접</div>
    <div class="cover-meta">AI·SW마에스트로 17기 최종평가<br><strong>팀 Dozer</strong> 박천웅, 김건우, 노재원</div>
  </div>
  <div class="cover-visual" aria-hidden="true"><img class="cover-device" src="assets/dual_macbook_mac1_mac2_transparent.png" alt=""></div>
  <div style="position:absolute;left:112px;right:112px;bottom:30px;z-index:3;color:#6f6878;font-size:13px;line-height:1.5">{ACK}<br>{ACK_EN}</div>
</div></div>''', '표지'))
S.note('''[0:00–0:10] 안녕하세요, 내 코드로 준비하는 공고 맞춤 기술면접 DevFit, Team Dozer입니다.

사사문구 국문·영문: 00-평가안내.md §사사문구 원문 그대로.''')

# ================= 1. 소개 — 장당 핵심 1개 (2026-11-06 재구성) =================
# 흐름: ①AI 발전 → ②채용 시장 → ③기술면접 → ④문제 근거 → ③ 솔루션 = GitHub → ④ 솔루션 소개 → ⑤ 차별점-반론 → ⑥ 차별점-하네스 → ⑦ 경쟁사

# ① 문제상황 1 — AI 발전으로 무엇이 가능해졌나 (research/R5 장1, 11-07 사용자 지시: 문제 정의 4장 · «뭐까지 가능해졌는지» 구체화)
S.append(shell('Problem', 'AI가 해내는 일은 코드 몇 줄에서 <span class="red">팀의 몇 주치 일</span>까지 늘었습니다', f'''
<div class="in-col" style="justify-content:center">
  <div class="in-lv">
    <div><em>2023</em><h4>코드 몇 줄을<br>채워 줌</h4><p>사람이 <b>4분</b> 걸리는 작업까지</p><small>GPT-4 · METR</small></div>
    <i>→</i>
    <div><em>2024</em><h4>실제 버그를<br>찾아 고침</h4><p>GitHub 이슈 <b>49%</b>를 혼자 해결</p><small>Claude 3.5 Sonnet · SWE-bench Verified</small></div>
    <i>→</i>
    <div><em>2025</em><h4>기능 하나를<br>통째로 구현</h4><p>사람이 <b>1시간~5시간</b> 걸리는 작업</p><small>Claude 3.7 Sonnet → Opus 4.5 · METR</small></div>
    <i>→</i>
    <div class="on"><em>2026</em><h4>팀이 몇 주 걸릴<br>일을 하루 만에</h4><p><b>68만 줄</b> 코드 이전을 하루 안에</p><small>Claude Opus 5.5 · GPT-6 Astra · 고객 사례</small></div>
  </div>
  <div class="in-lvbar"><b>그래서</b><span>1년 새 GitHub에 합류한 신규 개발자 <em>3,600만 명</em>, 그중 80%가 첫 주부터 AI와 함께 코드 작성</span><small>GitHub Octoverse 2025</small></div>
</div>''', cls='problem', source='METR time horizon (원시 데이터 benchmark_results_1_1.yaml, 블로그 2025-03-19) · SWE-bench Verified: Anthropic 2024-10 · 2026: Anthropic Claude Opus 5.5 발표 (2026-09-22) 고객 사례 · GitHub Octoverse 2025 (2025-10-28)'))
S.note('''[0:10–0:22] 먼저 AI가 어디까지 왔는지입니다. 2023년의 AI는 코드 몇 줄을 채워 주는 수준이었습니다. 사람이 4분이면 하는 일입니다. 2024년엔 실제 GitHub 버그의 절반을 혼자 찾아 고쳤고, 2025년엔 사람이 몇 시간 걸리는 기능 하나를 통째로 구현합니다. 그리고 지금, 올해 9월에 나온 Claude Opus 5.5와 GPT-6 Astra 세대에서는 엔지니어 팀이 몇 주 걸릴 68만 줄짜리 코드 이전을 하루 안에 끝냈다는 사례가 나옵니다. 혼자 18시간 넘게 쉬지 않고 작업했다는 사례도 있습니다. 그래서 이제 코드를 짜는 일은 누구나 합니다. 지난 1년 GitHub에 새로 들어온 개발자가 3,600만 명이고, 그중 80%가 첫 주부터 AI와 함께 코드를 씁니다.

근거: last-dance/research/R5-ai-capability-interview.md 장 1.
- METR 50% time horizon(사람 전문가 소요 시간 기준, 성공률 50%, 약 7개월마다 2배): GPT-4(2023-03) 약 4분 · Claude 3.7 Sonnet(2025-02) 약 60분 · Claude Opus 4.5(2025-11) 약 293분(4.9시간) · Claude Opus 4.6(2026-02) 약 719분(95% CI 317~3,634분). https://metr.org/assets/benchmark_results_1_1.yaml
- SWE-bench Verified: Claude 3.5 Sonnet 49.0%(2024-10, Anthropic 발표). 이후 Claude Sonnet 4.5 77.2%(2025-09).
- Octoverse 2025: 신규 개발자 3,600만+(+23%), 신규 개발자 80%가 첫 주에 Copilot 사용.
2026 칸 (사용자 지시 11-07: «2026년은 지금 나온 opus 5.5, astra 기준으로», 근거 research/R6-ai-2026-models.md):
- Claude Opus 5.5 공식 발표 2026-09-22(anthropic.com/news/claude-opus-5-5). 68만 줄·18시간은 발표문에 실린 고객 사례(«680,000-line code migration in less than a day—work that would have taken an engineering team weeks», Clio «stayed on task for over 18 hours»). 🏷 벤더가 고른 일화이고 측정값 아님 — 2023~2025 칸의 METR 값과 같은 잣대가 아니다. 68만 줄 사례는 회사명 없음.
- GPT-6 Astra = OpenAI, 2026-09-03 출시(Google Project Astra 아님). 일화는 Opus 5.5 것이므로 «Astra가 68만 줄을 했다»로 말하지 말 것. 같은 시험 비교: Terminal-Bench 4.0 Opus 5.5 66.4% · GPT-6 Astra 57.9%(Anthropic 발표 표, Astra 값은 «as reported by OpenAI», 벤더 측정).
- METR time horizon: Opus 5.5·Astra 모두 미공개(METR 2026-09-22 사전 평가 블로그에 시간 값 없음, time-horizons 페이지는 2026-09-08 이후 갱신 중단, «16시간 초과 측정은 신뢰 불가»). 직전 METR 측정값은 Opus 4.6 약 12시간(2026-02) — Q&A에서 «측정 기준으로는 하루치(12시간)»로 받는다.
⛔ «Opus 5.5 48시간»(X 비공식 외삽) 금지 · 블로그의 «SWE-bench Pro 89.9%» 금지(발표문에 SWE-bench 없음).
⚠ 단계 이름(«코드 몇 줄 → 버그 수정 → 기능 구현 → 팀 몇 주치 일»)은 팀이 붙인 설명이다. 2023~2025 숫자는 측정값 그대로이고, 2026은 고객 사례다. «성공률 50%» 단서를 Q&A에서 먼저 말할 것.
⛔ 2026년 SWE-bench 96~97%(서드파티) 금지 · Claude Mythos 17시간 금지(METR 스스로 신뢰 불가) · YC «95% AI 코드»를 비전공자 근거로 쓰지 말 것.
반대 근거(Q&A): METR RCT에서 숙련 개발자가 AI를 쓰면 19% 느려짐 · Veracode AI 생성 코드 45%에 보안 취약점 → «그래서 쓴 코드를 이해하는지가 더 중요해짐»으로 받는다.''')

# ② 문제상황 2 — 개발자 채용 시장의 변화 (research/R4, 사용자: 수요 감소는 인정, 경험 중요로 연결)
S.append(shell('Problem', '개발자는 덜 뽑고, 뽑을 때는 <span class="red">경험</span>을 봅니다', f'''
<div class="in-col" style="justify-content:center">
  <div class="in-mkt">
    <div><h5>덜 뽑음</h5><b>6개 중 5개</b><span>원티드 공고 7.3만 건 중 유의하게 줄어든 직군이 개발자</span><small>원티드랩 · 2025-01~2026-04</small></div>
    <div><h5>신입 자리는 더 좁음</h5><b>0.8%</b><span>개발 공고 중 신입 대상 (지원자의 29.5%는 신입)</span><small>사람인·점핏 · 2025 상반기</small></div>
    <div class="on"><h5>뽑을 때 보는 것</h5><b>81.6%</b><span>신규채용 최우선 평가 요소 "직무 관련 업무 경험"</span><small>경총 신규채용 실태조사 2025 · 500개사</small></div>
  </div>
  <div class="in-scnbar">"이력서에 적어둔 프로젝트에 대해 물어보면 <em>답변을 못하는 분들을 많이 봤다</em>"<small>IT 채용 담당자 · OKKY 설문 2025</small></div>
</div>''', cls='problem', source='원티드랩 공고 72,793건 분석(중앙일보 2026-06-11) · 사람인·점핏 2025 상반기(이투데이 2025-08-27) · 경총 2025 신규채용 실태조사(2025-03-20) · OKKY×바이라인네트워크 2025-02-28'))
S.note('''[0:22–0:34] 그런데 채용 시장은 반대로 갑니다. 원티드 공고 7만 3천 건을 보면 유의하게 줄어든 직군 6개 중 5개가 개발자입니다. 신입 자리는 더 좁아서, 개발 공고 중 신입 대상은 0.8%인데 지원자의 30%가 신입입니다. 그래서 뽑을 때는 경험을 봅니다. 기업 81.6%가 신규채용에서 가장 중요하게 보는 게 직무 관련 업무 경험입니다. 한 채용 담당자의 말처럼, 이력서에 적은 프로젝트를 물으면 답을 못 하는 지원자가 많습니다.

근거: last-dance/research/R4-hiring-market.md.
- 원티드: 2025-01~2026-04 공고 72,793건, 유의하게 감소한 직군 6개 중 5개가 개발자(중앙일보 2026-06-11, 원티드 원자료 미확인). 보조: 미국 Indeed SW 개발 공고 지수 81.6(2026-10-30, 2020-02=100) → 약 −18%(FRED).
- 사람인·점핏 개발 직군 2025 상반기: 신입 공고 0.8% vs 신입 지원 29.5% · 5~10년차 공고 39.7%(이투데이 2025-08-27). 보조: 전 직군 공고 82%가 «경력만»(대한상의 2025-06 — «기업의 82%» 아님, «공고의 82%»).
- 경총 2025 신규채용 실태조사: 100인 이상 500개사, «가장 중요한 평가 요소 직무 관련 업무 경험 81.6%» — 전 직군 수치(개발자 한정 아님). 2023→2025 상승 추세(58.4→74.6→81.6)는 원기사 미확인이라 쓰지 않음.
- 인용: OKKY×바이라인네트워크 2025-02-28, IT 전문가 71명 — 소표본.
⛔ 표현 한계: «AI 때문에 줄었다» 단독 원인 금지(한은: 경력직 선호 등 기존 추세를 AI가 가속). 수요 감소 → 경험 중시는 인과가 아니라 «같이 나타나는 흐름». «계속 줄고 있다» 현재형 단정 금지 — 2026 반등 신호 있음(인크루트 대졸 신입 채용계획 73.4%, 미국 SW 공고 저점 대비 +15% — 단 증가분 71%가 시니어).
⛔ 고용24 IT 공고 −71%는 대표성 없음(중소기업 위주) → 쓰지 않음.''')

# ③ 문제상황 3 — 개발자 기술면접의 변화 (R1 + R5 장3)
S.append(shell('Problem', '기술면접은 <span class="red">"왜 그렇게 짰나"</span>를 묻습니다', f'''
<div class="in-col" style="justify-content:center">
  <div class="in-iv">
    <div class="in-ivq"><div class="in-who">실제 개발자 면접 질문 (2026년 5~6월)</div>
      <div class="in-q">"왜 이 코드를 썼는지<br>코드적으로 설명해 주세요"<small class="in-qw">이스트소프트 백엔드</small></div>
      <div class="in-q">"다른 방법은 왜<br>선택하지 않았나요?"<small class="in-qw">비바리퍼블리카 시스템엔지니어</small></div></div>
    <div class="in-ivc"><div class="in-who">채용 방식 변화</div>
      <div><b>넥슨</b><span>인턴 코딩테스트 폐지 → AI 활용 역량 평가</span><small>2026-09</small></div>
      <div><b>CJ올리브영</b><span>경력 개발 라이브 코딩 폐지 → 과정을 보는 AI 과제</span><small>2026-07</small></div>
      <div><b>Meta</b><span>일부 코딩 면접에서 AI 어시스턴트 허용</span><small>2025-07</small></div>
      <div><b>Canva</b><span>CS 기초 스크리닝 → AI 허용 면접</span><small>2025-06</small></div>
      <div><b>컬리</b><span>개발자 공채 코딩테스트에서 ChatGPT 사용 허용</span><small>2025-06</small></div></div>
  </div>
  <div class="in-scnbar">지원자 인터뷰 <em>"1달 전에 짠 코드 잘 기억이 안 나거든요"</em><small>현직 개발자 인터뷰 (2026-09-07) 발췌</small></div>
</div>''', cls='problem', source='면접 질문: 잡플래닛 면접 리뷰 큐레이션 (2026-07-01) · 넥슨: 바이라인네트워크 2026-09-02 · CJ올리브영: 아시아경제 2026-07-21 · Canva 공식 블로그 2025-06-11 · Meta: 404 Media 2025-07-29 · 컬리: 중앙일보 2025-06-10 · 지원자 인용: 현직 개발자 인터뷰 (2026-09-07)'))
S.note('''[0:34–0:46] 그래서 기술면접도 바뀝니다. 실제 올해 면접 리뷰를 보면 «왜 이 코드를 썼는지 코드적으로 설명해 달라», «다른 방법은 왜 선택하지 않았냐»를 묻습니다. 넥슨은 코딩테스트를 없애고 AI 활용 역량을 보고, CJ올리브영은 라이브 코딩 대신 과정을 보는 AI 과제를 냅니다. «AI를 쓰냐»가 아니라 «쓴 코드를 이해하고 설명할 수 있냐»를 확인하는 쪽입니다. 그런데 정작 지원자는 자기 코드를 기억하지 못합니다. «1달 전에 짠 코드 잘 기억이 안 나거든요.»

주장: claims.md C1 — 직접 재는 수치 없음 → «경험 면접 N% 증가» 같은 수치 금지. «경험 위주로 바뀌었다» 단정 대신 «"왜·어떻게"를 캐묻는 쪽으로 바뀌는 중».
면접 질문: 잡플래닛 «토스·무신사 개발자 면접 질문, 실제로 이랬다»(2026-07-01, https://www.jobplanet.co.kr/contents/news-8309) — 에디터 큐레이션, AD 표기, 대표성 없음 → «사례»로만.
기업 사례: 넥슨 인턴십 «넥토리얼» 코딩테스트 폐지·AI 면접·AI 활용 역량평가(바이라인네트워크 2026-09-02, 채용팀장 인용) · CJ올리브영 경력 개발 직군 라이브 코딩 폐지 → 크래프톤 «코파 프로브» AI 과제로 전 과정 평가(아시아경제 2026-07-21, 법인명 재확인) · Canva(공식 블로그 2025-06-11) · Meta 일부 코딩 면접 AI 어시스턴트 허용(404 Media 2025-07-29, 내부 공지 보도 — «Meta 전체 면접 AI 허용» 확대 금지) · 컬리 개발자 공채 코테 ChatGPT 허용, 창립 후 처음(중앙일보 단독 2025-06-10, «2025년 1월»은 오기) — R1 E10~E13·E16, R5 장3.
반대 근거(Q&A): Karat 2026 — 62%는 여전히 면접에서 AI 금지 · 그렙 고객도 개발 직군은 코테 유지 · Pulse #146에서 알고리즘 질문을 버린 면접관 0명. → «코테가 사라졌다» 금지, «과정·이해를 묻는 방식이 늘고 있다»까지.
인용: 현직 개발자 인터뷰 2026-09-07(collect/D P1).''')

# ④ 문제 근거 — 취준생은 전에 짠 코드를 다시 보기도, 기억하기도 어렵다 (11-10 사용자 지시, research/R10)
S.append(shell('Problem', '취준생은 전에 짠 코드를 <span class="red">다시 보기도, 기억하기도</span> 어렵습니다', f'''
<div class="in-col" style="justify-content:center">
  <div class="in-p5">
    <div class="st">
      <div class="row"><b class="r">30일</b><div><span>개발자가 자기 파일 내용의<br>절반을 잊는다고 답한 기간 (중앙값)</span><small>오픈소스 개발자 n=60 · Krüger et al. 2018</small></div></div>
      <div class="row"><b>66%</b><div><span>경력 3년 미만 개발자가 코드를<br>이해하는 데 쓰는 시간 (전체 58%)</span><small>현업 n=78, 3,148시간 실측 · Xia et al. 2018</small></div></div>
    </div>
    <div class="qt"><div class="mk">"</div><blockquote>스스로 이력서에 적어둔 프로젝트에 대해 물어보면 답변을 못하는 분들을 많이 봤다</blockquote><small>채용 담당자 · OKKY×바이라인네트워크 2025 (n=71)</small></div>
  </div>
  <div class="in-bar">그런데 면접에서는 그 코드를 <span>왜 그렇게 짰는지</span> 설명해야 합니다</div>
</div>''', cls='problem', source='Krüger et al., 「Do You Remember This Source Code?」, ICSE 2018. · Xia et al., 「Measuring Program Comprehension: A Large-Scale Field Study with Professionals」, IEEE TSE 2018. · 바이라인네트워크(OKKY 공동 조사), 「개발자 채용 설문」, 2025.'))
S.note('''[0:46–0:55] 문제는 지원자 쪽에도 있습니다. 개발자들은 자기가 쓴 파일도 한 달쯤 지나면 절반은 잊는다고 답했습니다. 코드를 다시 읽는 일도 가볍지 않습니다. 경력 3년 미만 개발자는 일하는 시간의 66%를 코드를 이해하는 데 씁니다. 취준생은 레포가 여러 개이고 커밋도 많아서 전부 다시 보기가 어렵습니다. 그래서 채용 담당자들은 이력서에 적은 프로젝트를 물어보면 답하지 못하는 지원자를 많이 봤다고 말합니다. 그런데 면접은 바로 그 코드를 왜 그렇게 짰는지 묻습니다.

출처 (research/R10-recall-own-code.md, 접근 2026-11-10):
- 30일 = Krüger, Wiemann, Fenske, Saake, Leich, ICSE 2018, 오픈소스 개발자 60명(GitHub 10개 프로젝트). 원문 «forget half of their files after 30 days in the median and 40 days on average». ⚠ 측정값이 아니라 본인 추정치. ⚠ 같은 파일을 여러 번 고쳤거나 직접 쓴 비율이 높으면 더 오래 기억함 → Q&A에서는 «한 번 짜고 다시 안 본 코드일수록 빨리 잊는다». https://jacobkrueger.github.io/assets/papers/Krueger2018Remember.pdf
- 66%·58% = Xia, Bao, Lo, Xing, Hassan, Li, IEEE TSE 44(10) 2018, 현업 78명·3,148 작업시간 자동 기록. 저경력(3년 미만) 66.37%, 전체 58%. ⚠ 자기 코드에 한정한 수치가 아니라 코드 이해 일반. https://xin-xia.github.io/publication/TSE17.pdf
- 인용 = OKKY×바이라인네트워크 2025-02-28, IT 전문가 71명, 채용 담당자 발언(R4 V2). ⚠ 표본 작음. https://byline.network/2025/02/27-431/
⛔ «취준생 N%가 자기 코드를 기억 못 한다» 류 설문 수치 없음(국내·해외 못 찾음) → 만들지 말 것. ⛔ 취준생 레포·커밋 규모 통계 없음 → 노트의 «레포가 여러 개이고 커밋도 많아서»에 숫자 붙이지 말 것. ⛔ Minelli 70% 쓰지 말 것.
Q&A 보조: Anthropic 2026-01, 52명 무작위 실험 — AI로 코딩한 그룹의 이해도 퀴즈 50% vs 손코딩 67% (작업 직후 측정, 벤더 자체 연구).
삭제한 이전 장(84%·WGU 60%·Big Tech 58%) 수치는 Q&A용: Stack Overflow 2025 · WGU Workforce Decoded 2026(미국 n=3,128) · Pragmatic Engineer Pulse #146(interviewing.io n=63).''')


# ③ 솔루션 = GitHub — GitHub 자체를 소개 (중간평가 덱 «GitHub 소개» 장 구성)
S.append(shell('Solution', '그 경험은 이미 <span class="purple">내 GitHub</span>에 남아 있습니다', f'''
<div class="in-col in-ghx">
  <div class="in-ghtop">
    <div class="in-ghlogo"><img src="assets/github_mark.svg" alt="GitHub 로고"></div>
    <div class="in-ghcopy">
      <p class="lead">GitHub는 개발자가 코드를 올리고 함께 고치는 플랫폼. 코드가 바뀔 때마다 <b>누가, 언제, 무엇을, 왜</b> 바꿨는지가 저장소에 그대로 남습니다</p>
      <p class="aud">개인 프로젝트, 팀 협업, 기업 제품 개발 모두 같은 방식으로 기록이 남습니다</p>
      <div class="in-ghstats">
        <div><b>1억 8천만 명</b><span>전 세계 GitHub 개발자</span></div>
        <div><b>6억 3천만 개</b><span>GitHub에 쌓인 저장소</span></div>
      </div>
    </div>
  </div>
  <div class="in-ghsteps">
    <div><em>diff</em><b>코드 변경</b><span>바뀐 파일과 코드 줄이 남음</span></div>
    <div><em>commit</em><b>변경 이유 기록</b><span>작성자와 시점도 함께 남음</span></div>
    <div><em>PR</em><b>동료 검토</b><span>질문 · 수정 요청 · 답변이 모임</span></div>
    <div><em>merge</em><b>검토 뒤 반영</b><span>최종 결정과 결과가 남음</span></div>
  </div>
  <div class="in-ghcall">면접관이 묻는 구현 이유는 커밋과 PR 기록에 남아 있습니다</div>
</div>''', source='자료: GitHub Docs · GitHub Octoverse 2025'))
S.note('''[0:55–1:15] 그런데 그 경험은 사라진 게 아닙니다. GitHub는 전 세계 1억 8천만 명의 개발자가 쓰는 코드 플랫폼이고, 코드를 바꾸면 diff가, 이유를 적으면 커밋이, 동료가 검토하면 PR이, 반영하면 병합 기록이 남습니다. 누가·언제·무엇을·왜 바꿨는지가 그대로 남아 있습니다. 면접관이 묻는 경험의 원본이 바로 지원자의 GitHub입니다. DevFit은 여기서 출발합니다.

⛔ «AI가 짰는가» 판정(authorship) 프레임 금지 — 판별 기준은 «알고 짰는가».
수치: GitHub Octoverse 2025 — 개발자 1억 8천만+, 저장소 6억 3천만 (중간평가 덱 7장과 동일 출처·동일 수치). 로고: GitHub 공식 mark(흰색), 중간평가 덱 deck_assets/github_mark_dark.svg.\nDevFit 화면(Q3 useCamera)은 사용자 지시(11-06)로 이 장에서 뺐다 — 다음 장·시연에서 보여 준다.''')

# ④ 솔루션 소개
S.append(shell('Solution', '공고 URL 하나와 <span class="purple">내 GitHub</span>면 그 공고용 면접 준비가 끝납니다', f'''
<div class="in-col">
  <div class="in-dp-pipe">
    <div class="in-dp-pin">
      <div class="in-dp-src"><div class="in-dp-srcic">{ic('doc',40)}</div><div><div class="in-dp-srck">지원할 공고</div><div class="in-dp-doc"><i></i><i></i><mark>대용량 트래픽 경험 우대</mark><i></i></div></div></div>
      <div class="in-dp-src"><div class="in-dp-srcic gh"><img src="assets/github_mark.svg" alt=""></div><div><div class="in-dp-srck">내 GitHub 코드</div><div class="in-dp-doc"><i></i><mark class="g">로그인이 느려서 캐시를 붙임</mark><i></i><i></i></div></div></div>
    </div>
    <div class="in-dp-pa"><svg viewBox="0 0 120 520" preserveAspectRatio="none"><defs><marker id="inar" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#7c6cf0"/></marker></defs><path d="M0,140 C60,140 60,260 112,260" stroke="#7c6cf0" stroke-width="5" fill="none" stroke-dasharray="10 8" marker-end="url(#inar)"/><path d="M0,380 C60,380 60,260 112,260" stroke="#7c6cf0" stroke-width="5" fill="none" stroke-dasharray="10 8" marker-end="url(#inar)"/></svg></div>
    <div class="in-dp-eng">
      <div class="in-dp-engh"><img src="assets/icon.svg" alt=""><span>DevFit</span></div>
      <ol><li><b>1</b>공고에서 회사가 원하는 경험을 뽑고</li><li><b>2</b>내가 직접 짠 커밋만 골라 읽고</li><li><b>3</b>둘이 만나는 지점을 질문으로</li></ol>
    </div>
    <div class="in-dp-pa"><svg viewBox="0 0 100 520" preserveAspectRatio="none"><path d="M0,260 L88,260" stroke="#7c6cf0" stroke-width="5" fill="none" marker-end="url(#inar)"/></svg></div>
    <div class="in-dp-pout">
      <div class="in-dp-q"><div class="in-dp-qk">이 공고 맞춤 예상 질문</div><div class="in-dp-qb">"로그인에 캐시를 왜 넣었나요? 사용자가 10배로 늘면요?"</div><div class="in-dp-qref">근거 · 내 커밋 "로그인 캐시 추가"</div></div>
      <div class="in-dp-loop"><span>{ic('mic',26)} 답변</span><i>→</i><span>피드백</span><i>→</i><span>꼬리질문</span><em>↻</em></div>
    </div>
  </div>
</div>''', source='공고·커밋·질문 문구는 흐름을 보여 주는 예시 · 0개: 같은 레포 × 공고 2개, 115문항'))
S.note('''[1:15–1:45] 쓰는 법은 네 단계입니다. 지원할 공고 URL을 붙여넣고, 분석할 내 레포를 고르면, 그 공고에 맞춘 면접 질문이 나옵니다. 질문마다 그 질문이 나온 내 코드가 붙어 있고, 텍스트나 음성으로 답하면 피드백과 꼬리질문이 이어집니다.

본편에서 뺀 수치(Q&A용): 같은 레포에 공고만 바꾸면 문장이 같은 질문 0개(115문항, collect/C §2-1) · 공고 수집 29곳(플랫폼 5 + 기업 24).
하단 칩 3개(29곳·0개·합불 판정·랭킹 없음)는 사용자 지시(11-07)로 장표에서 뺌 — 위 수치로 Q&A 대응.
화면 문구(캐시 커밋·10배 질문)는 흐름 설명용 예시 — 실제 결과 화면은 시연에서 보여 준다(11-07 사용자 지시로 캡처 뺌).
⛔ «주제가 겹치지 않는다»로 확대 금지(문장 기준 0개일 뿐). ⛔ «점수·랭킹 없음» 금지 → «합불 판정·랭킹 없음 — 최종 판단은 사람»까지만.''')

# ⑤ 차별점 — 반론에 답하기: 같은 LLM이라도 차이는 하네스 (claims.md C2)
S.append(shell('Key Features', '"Claude Code에 GitHub 링크 주면 <span class="red">되지 않나요?</span>"', f'''
<div class="in-hn">
  <div class="in-hnl">
    <div class="in-lane bad">
      <div class="in-lanek">레포 링크만 받은 채팅형 AI</div>
      <div class="in-lanef"><span>GitHub 링크</span><i>→</i><span class="llm">같은 LLM</span><i>→</i><span>질문</span></div>
      <div class="in-laner"><b>0 / 18</b><small>제시한 근거 중 실존<br>없는 커밋·파일을 지어냄</small></div>
    </div>
    <div class="in-lane good">
      <div class="in-lanek">DevFit</div>
      <div class="in-lanef"><span>공고 + 레포</span><i>→</i><div class="in-har"><em>하네스 (서버가 매번 실행)</em><div><span>공고 정리</span><span>내 커밋만</span><span>근거 diff</span><span class="llm">같은 LLM</span><span class="chk">근거 대조</span></div></div><i>→</i><span>질문</span></div>
      <div class="in-laner"><b>28 / 28</b><small>제시한 근거 전부 실존<br>같은 레포 4개 · 공고 · 지시</small></div>
    </div>
  </div>
  <div class="in-hnr">
    <div class="in-hnc">같은 LLM이라도,<br>차이는 <em>하네스</em><small>DevFit은 같은 절차를 서버에서 매번 실행해 질문 품질을 일정하게 유지합니다</small></div>
    <div class="in-hne"><div class="in-hnek">외부 근거 · 같은 GPT-4 Turbo</div><div class="in-hnen"><b>11.0%</b><i>→</i><b class="p">18.0%</b></div><small>하네스만 바꾼 SWE-bench Lite 해결률<br>SWE-agent, NeurIPS 2024</small></div>
  </div>
</div>''', source='범용 AI 비교 파일럿 (2026-11-05, 공개 레포 4개, 결정론 채점) · 부록 A2 · Yang et al., SWE-agent, NeurIPS 2024, Table 1 (Shell-only vs SWE-agent)'))
S.note('''[1:45–2:25] 가장 많이 들은 반론입니다. «Claude Code에 GitHub 링크 주면 되지 않나요?» 저희 답은 이렇습니다. 같은 LLM이라도 차이는 하네스입니다. DevFit은 공고를 정리하고, 내 커밋만 고르고, 근거 diff를 묶고, 질문을 만든 뒤, 질문 속 코드 이름을 실제 diff와 대조해 없으면 버립니다. 이 절차를 사용자가 매번 프롬프트로 짜는 게 아니라 서버가 매번 강제합니다. 이건 저희만의 얘기가 아닙니다. 같은 GPT-4 Turbo로도 하네스만 바꾸면 SWE-bench 해결률이 11%에서 18%로 오릅니다. 실제로 같은 레포·같은 공고·같은 지시로 비교했더니, 레포 링크만 받은 채팅형 AI는 «레포를 확인해 보니»라고 쓰고는 근거 18개를 전부 지어냈고, DevFit은 28개 모두 실존했습니다. 그럼 직접 보여 드리겠습니다.

주장: claims.md C2 «범용 LLM과의 차이는 모델이 아니라 하네스» — 팀 주장으로 말한다(장표에 멘토 인용 넣지 않음, 사용자 지시 2026-11-06). Q&A에서 «누가 그러냐»가 나오면: 11-02 김동현 멘토 멘토링에서 같은 지적을 받음.
인용 원문(STT, feedback/01_녹취/2026-11-02_멘토링_AI면접MVP_B2C-B2B전략.txt, 참석자 2): 02:08:15 «내가 같은 범용 LLM을 써 … 그걸 매번 일정한 quality로 뽑아내는 것들은 … 차이가 분명히 있는 거랑 그 이야기를 해줘야 돼» · 02:08:57 «엔진은 있지만 그거에 관련된 하네싱 … 은 필요한 거라고» · 02:09:50 «매번 동일한 답변과 수준을 위해서는 … 맞춰줘야 되는데 매번 그거를 끌어다가 … 넣어주고 이런 걸 하겠냐고». 장표 인용은 STT 오인식을 다듬은 요지 — «녹취 요지»로 표기. 주장 등록: last-dance/claims.md C2.
멘토 실명 표기 OK (소마 멘토는 실명 사용 가능 — 사용자 확인 2026-11-06).
기존 인용(Q&A용): «이미 내가 쓰는 AI로 다 준비하는 부분»(개발자 사용자) · «GitHub 링크를 Claude Code에 넘기면 된다»(IT 기업 대표, 10-26 서면 회신).

출처: collect/E-compare.md (2026-11-05 파일럿, 결정론 채점·LLM 0회). 게이트: 모든 질문 출처 353/353(collect/C 평가 세트 전수) · 운영 최근 30일 84건 차단(관리자 콘솔, collect/A §7) · 실행 1회 63개 중 5개 폐기. 특허 출원 10-2026-0214809(생성·게이트).
외부 근거(R2, last-dance/research/R2-harness-and-stats.md): SWE-agent arXiv:2405.15793 Table 1 — GPT-4 Turbo · SWE-bench Lite, Shell-only 11.00% vs SWE-agent 18.00%. Anthropic «swe-bench-sonnet»: «can vary significantly based on this scaffolding, even when using the same underlying AI model». Epoch AI(2025-12-23): scaffold만으로 GPT-5 최대 11%p 차. ⚠ 반대 근거: 같은 Anthropic 글에서 스캐폴드 고정·모델만 교체 시 22%→33%→49% → «모델보다 하네스가 중요» 단정 금지. Q&A «모델이 더 중요하지 않나?» → «모델도 중요합니다. 다만 모델이 같아도 하네스에 따라 크게 달라지고, 모델은 저희가 바꿔 끼울 수 있지만 하네스는 저희가 만든 것입니다».
Q&A 대비: clone한 Claude Code는 30/32 실존 → «잘 지시하면 찾는다. 그 지시와 대조를 사용자가 매번 해야 한다. DevFit은 서버가 매번 강제 + 공고 단위 흐름 + 본인 커밋 필터 + 음성 모의면접». Greenroom(GitHub 레포 분석 모의면접) 존재 — 부록 A2.
⛔ «유일»·«최초»·«AI는 레포를 못 읽는다»·«Claude보다 정확» 금지. ⛔ «46/46 일치» 금지.
🔴 인용 실명은 동의 후에만 — 현재 역할만 표기.
(11-10 삭제한 장표 2개 → Q&A용) 질문 귀속 4지선다 81.9% vs 우연 25%, n=177 — 부록 A3 · AI 모의면접 비교(이력서 vs 내 커밋, 본인 1.0/공동 0.70/타인 제외, 공고 29곳) — 부록 A2.''')

# ================= 2. 시연 =================
S.append(raw('dark-slide', f'''<div class="dark-grid"></div><div class="slide-shell" style="padding:0">
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding-left:118px;z-index:2">
  <div style="font-size:30px;color:#b9b0ff;font-weight:900;margin-bottom:24px">02 · 시연</div>
  <div style="color:#fff;font-size:150px;font-weight:900;letter-spacing:-.06em;line-height:1">Live Demo</div>
  <div style="margin-top:40px;color:#d9d5dd;font-size:44px;font-weight:800;letter-spacing:-.03em">https://devfit.app</div>
  <div style="margin-top:34px;color:#8f8996;font-size:26px;font-weight:700">공고 URL 붙여넣기 → 레포 선택 → 질문과 근거 코드 → 음성 답변 · 꼬리질문</div>
</div><div class="folio" style="left:118px;color:#6d6774"></div></div>''', 'Live Demo'))
S.note('''[3:20–8:20] 라이브 시연 5분 — 대본·체크리스트 정본: collect/F-audit-demo.md
''')

# ================= 부록 → s5_appendix.py (11-07 사용자: 부록은 ppt-start 전담) =================
