# -*- coding: utf-8 -*-
# 최종발표 덱 공용 코어 — CSS·JS(중간평가 덱에서 읽음)·EXTRA CSS·헬퍼
# 🔒 관리: ppt-start 세션. 다른 세션은 직접 고치지 말고 요청한다 (모든 장표에 영향)
# 수치 정본: last-dance/collect/00-통합보고.md
import os, re, datetime as dt
MID = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor', 'irdeck_new.html')  # 중간평가 덱 사본 (CSS·JS 원본)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
src = open(MID, encoding='utf8').read()
CSS = src[src.find('<style>') + 7:src.find('</style>')]
JS = src[src.find('<script>'):src.find('</script>') + 9]

EXTRA = r"""
.source{display:block;position:absolute;right:88px;bottom:28px;max-width:1380px;text-align:right;color:#a19ba7;font-size:15px;font-weight:600;line-height:1.4;letter-spacing:-.01em}
.title.wrap{white-space:normal}
.eyebrow .badge{font-size:17px;margin-left:4px}
.slide.problem .eyebrow{color:var(--red)}
.todo{display:inline-block;padding:10px 16px;border:2px dashed var(--amber);border-radius:12px;background:var(--amber-soft);color:#7a4a00;font-size:18px;font-weight:800;line-height:1.4}
.quote{font-size:30px;font-weight:800;line-height:1.45;letter-spacing:-.035em;color:var(--ink);word-break:keep-all}
.quote-who{margin-top:14px;color:var(--muted);font-size:19px;font-weight:700}
.divider{background:radial-gradient(1200px 940px at 106% 110%,rgba(96,73,221,.45) 0,rgba(96,73,221,0) 64%),radial-gradient(820px 620px at -6% -10%,rgba(255,255,255,.9) 0,rgba(255,255,255,0) 60%),linear-gradient(118deg,#f2effa 0%,#ddd6f3 45%,#a89ae6 100%)}
.divider::after{display:none}
.divider-copy{position:absolute;left:118px;top:50%;transform:translateY(-50%)}
.divider-kicker{color:var(--purple-deep);font-size:30px;font-weight:900;letter-spacing:-.03em}
.divider-title{margin-top:18px;font-size:120px;font-weight:900;letter-spacing:-.06em;line-height:1}
.divider-sub{margin-top:30px;color:var(--ink-2);font-size:32px;font-weight:700;letter-spacing:-.03em}
.kpi{padding:30px 34px;display:flex;flex-direction:column;justify-content:center}
.kpi .metric{font-size:72px}
.kpi .metric-label{font-size:21px}
.kpi .kpi-k{color:var(--muted);font-size:20px;font-weight:800;margin-bottom:14px}
.list{margin:0;padding:0;list-style:none}
.list li{position:relative;padding-left:26px;margin:0 0 14px;color:var(--body);font-size:23px;line-height:1.5;letter-spacing:-.02em;word-break:keep-all}
.list li::before{content:"";position:absolute;left:4px;top:15px;width:9px;height:9px;border-radius:50%;background:var(--purple)}
.list.sm li{font-size:19px;margin-bottom:10px}
.list.sm li::before{top:12px}
.matrix.sm{font-size:17px}
.matrix.sm th,.matrix.sm td{padding:11px 14px}
.matrix.xs{font-size:14.5px}
.matrix.xs th{font-size:14.5px}
.matrix.xs th,.matrix.xs td{padding:6px 10px;line-height:1.28}
.matrix.plain th:nth-child(2),.matrix.plain td:nth-child(2){background:inherit;color:inherit;font-weight:inherit}
.matrix.plain th:nth-child(2){background:#f0eef2;font-weight:900}
.matrix.left td,.matrix.left th{text-align:left}
.gantt{position:relative;flex:1;min-height:0}
.gantt .lane{position:absolute;left:0;right:0;border-top:1px solid var(--line)}
.gantt .lane-name{position:absolute;left:0;font-size:20px;font-weight:900;color:var(--ink)}
.gantt .ev{position:absolute;transform:translateX(-50%);text-align:center;width:180px}
.gantt .ev .d{display:inline-block;padding:4px 10px;border-radius:999px;background:var(--purple-soft);color:var(--purple-deep);font-size:15px;font-weight:900}
.gantt .ev .t{margin-top:6px;font-size:15.5px;font-weight:700;line-height:1.32;color:var(--ink);word-break:keep-all}
.gantt .ev .c{margin-top:3px;font-size:13.5px;color:var(--purple);font-weight:800;line-height:1.3;word-break:keep-all}
.gantt .ev::before{content:"";position:absolute;left:50%;top:-13px;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:var(--purple)}
.gantt .mid{position:absolute;top:0;bottom:0;width:0;border-left:3px dashed var(--red)}
.gantt .mid span{position:absolute;top:-6px;left:10px;white-space:nowrap;color:var(--red);font-size:17px;font-weight:900}
.gantt .month{position:absolute;top:0;color:var(--muted);font-size:17px;font-weight:900}
.chip-row{display:flex;gap:14px;flex-wrap:wrap}
.matrix.a1{font-size:14px}
.matrix.a1 th,.matrix.a1 td{padding:5px 10px;line-height:1.25}
.matrix.a1 th:nth-child(1){width:44px}.matrix.a1 th:nth-child(2){width:470px}.matrix.a1 th:nth-child(3){width:110px}
.matrix.a1 .badge{font-size:13px;padding:5px 10px}
.matrix.a9 th{padding:22px 26px;font-size:20px}.matrix.a9 td{padding:44px 26px;font-size:24px;line-height:1.45}.matrix.a9 .patent{font-size:20px;white-space:nowrap}.matrix.a9 th:nth-child(1){width:250px}.matrix.a9 th:nth-child(2){width:420px}.matrix.a9 th:nth-child(4){width:150px}.matrix.a9 td:nth-child(4){white-space:nowrap}
.big-flow .flow-node{padding:48px 24px}.big-flow .flow-node{font-size:32px}.big-flow .flow-node .sub{font-size:21px;margin-top:10px}
.apx-lg .list li{font-size:28px;margin-bottom:22px}
.apx-lg .list li::before{top:17px}
.psn{display:grid;grid-template-columns:1fr 46px 1fr 46px 1fr;align-items:stretch;position:relative}
.psn-c{padding:24px 28px;display:flex;flex-direction:column;justify-content:center;min-height:178px}
.psn-k{font-size:17px;font-weight:900;letter-spacing:.08em;margin-bottom:10px;color:var(--muted)}
.psn-c.red-soft .psn-k{color:var(--red)}.psn-c.soft .psn-k{color:var(--purple-deep)}
.psn-m{font-size:56px;font-weight:900;letter-spacing:-.05em;line-height:1;margin-bottom:10px}
.psn-m.red{color:var(--red)}.psn-m.purple{color:var(--purple)}
.psn-t{font-size:22px;font-weight:700;line-height:1.45;color:var(--ink);letter-spacing:-.02em}
.psn-t b{font-weight:900}
.psn-a{display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900;color:var(--purple)}
.psn.sm .psn-c{min-height:320px;padding:30px 34px}.psn.sm .psn-m{font-size:62px}.psn.sm .psn-t{font-size:23px}
.psn-tag{position:absolute;left:-2px;top:-16px;z-index:2;font-size:15px;font-weight:900;color:#fff;background:var(--purple);border-radius:999px;padding:4px 12px}
.sb{display:grid;grid-template-columns:1.2fr 40px 1fr 40px .95fr;align-items:center;background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:20px 28px;min-height:118px}
.sb-c{display:flex;align-items:center;gap:16px;min-width:0}
.sb-k{flex:none;font-size:15px;font-weight:900;padding:6px 12px;border-radius:999px;letter-spacing:.04em}
.sb-c.p .sb-k,.mn.p .sb-k{background:var(--red-soft);color:var(--red)}
.sb-c.s .sb-k,.mn.s .sb-k{background:#efedf2;color:var(--ink)}
.sb-c.n .sb-k,.mn.n .sb-k{background:var(--purple);color:#fff}
.sb-m{flex:none;font-size:46px;font-weight:900;letter-spacing:-.05em;line-height:1}
.sb-c.p .sb-m{color:var(--red)}.sb-c.n .sb-m{color:var(--purple)}
.sb-t{font-size:20px;font-weight:700;line-height:1.4;letter-spacing:-.02em;color:var(--ink)}
.sb-t b{font-weight:900}
.sb-a{color:var(--purple);font-size:30px;font-weight:900;text-align:center}
.hero{display:grid;gap:26px;margin-top:24px;flex:1;min-height:0}
.ic{display:inline-flex;align-items:center;justify-content:center;color:var(--purple-deep)}
/* mini P/S/N */
.mns{display:flex;flex-direction:column;gap:12px;margin:18px 0 6px}
.mn{display:flex;align-items:center;gap:14px;font-size:22px;font-weight:700;color:var(--ink);line-height:1.35}
.mn-m{font-size:34px;font-weight:900;letter-spacing:-.04em;flex:none}
.mn.p .mn-m{color:var(--red)}.mn.n .mn-m{color:var(--purple)}
/* gate (key1) */
.gate{padding:28px 30px;display:flex;flex-direction:column;gap:14px}
.gate-k{font-size:18px;font-weight:900;color:var(--purple-deep);letter-spacing:.04em}
.gate-q{font-size:19px;font-weight:800;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.chips span,.chips2 span{font-family:var(--mono);font-size:18px;font-weight:700;padding:6px 12px;border-radius:10px;background:var(--purple-pale);color:var(--purple-deep)}
.chips2{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}.chips2 span{background:#efedf2;color:#6d6774;text-decoration:line-through}
.gate-arrow,.own-arrow,.quiz-a{font-size:18px;font-weight:800;color:var(--purple)}
.gate-out{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.go{border-radius:16px;padding:14px 12px;text-align:center}.go b{display:block;font-size:24px;font-weight:900}.go span{font-size:15px;font-weight:700;color:var(--muted)}
.go.keep{background:var(--green-soft)}.go.keep b{color:var(--green)}.go.ask{background:var(--amber-soft)}.go.ask b{color:var(--amber)}.go.drop{background:var(--red-soft)}.go.drop b{color:var(--red)}
.gate-num{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px}
.gate-num div{border-top:2px solid var(--line);padding-top:12px}.gate-num b{display:block;font-size:40px;font-weight:900;letter-spacing:-.04em}.gate-num span{font-size:16px;font-weight:700;color:var(--muted)}
/* ownership (key2) */
.own{padding:34px 40px;display:flex;flex-direction:column;justify-content:space-between}
.own-k{font-size:18px;font-weight:900;color:var(--muted);margin-bottom:10px}
.own-bar{display:flex;height:64px;border-radius:16px;overflow:hidden;font-weight:900}
.own-bar .me{background:var(--purple);color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px}
.own-bar .other{flex:1;background:#e6e2ea;color:#6d6774;display:flex;align-items:center;padding-left:22px;font-size:20px}
.own-w{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.w{display:flex;align-items:center;gap:16px;border-radius:18px;padding:16px 20px;background:#f6f5f7}
.w b{display:block;font-size:38px;font-weight:900;letter-spacing:-.04em;line-height:1}.w small{font-size:16px;font-weight:700;color:var(--muted)}
.av{width:46px;height:46px;border-radius:50%;flex:none}
.w.me .av{background:var(--purple)}.w.me b{color:var(--purple)}
.w.co .av{background:linear-gradient(90deg,var(--purple) 50%,#d6d1dc 50%)}
.w.ot .av{background:#d6d1dc}.w.ot b{color:var(--red)}
.own-dots{display:flex;align-items:center;gap:12px}.own-dots i{width:40px;height:40px;border-radius:50%;background:var(--purple)}.own-dots b{margin-left:14px;font-size:30px;font-weight:900;color:var(--purple)}
/* quiz (key3) */
.quiz{padding:30px 34px;display:flex;flex-direction:column;gap:16px}
.quiz-q{display:flex;gap:16px;align-items:center;border-radius:18px;background:var(--purple-pale);padding:18px 22px}.quiz-q small{display:block;font-size:15px;font-weight:800;color:var(--purple-deep)}.quiz-q b{font-size:22px;font-weight:900}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.opt{position:relative;border:2px solid var(--line);border-radius:16px;padding:18px 18px;display:flex;align-items:center;gap:14px;background:#fff}
.opt b{width:38px;height:38px;border-radius:50%;background:#efedf2;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:900}
.opt span{font-size:19px;font-weight:700;color:var(--muted)}
.opt.hit{border-color:var(--purple);background:var(--purple-pale)}.opt.hit b{background:var(--purple);color:#fff}.opt.hit span{color:var(--ink)}
.opt em{position:absolute;right:12px;top:-12px;font-style:normal;font-size:14px;font-weight:900;color:#fff;background:var(--purple);border-radius:999px;padding:3px 10px}
/* arch (3.1) */
.arch{display:grid;grid-template-columns:1fr 34px 1fr 34px 1fr 34px 1fr 34px 1fr 34px 1fr 34px 1fr;align-items:stretch}
.an{border-radius:18px;background:#fff;border:1px solid var(--line);padding:22px 10px 18px;text-align:center;display:flex;flex-direction:column;justify-content:center;gap:6px}
.an b{font-size:23px;font-weight:900;letter-spacing:-.03em}.an span{font-size:15px;font-weight:700;color:var(--muted);line-height:1.35}
.an em{font-style:normal;font-size:13px;font-weight:900;color:#fff;background:var(--purple);border-radius:999px;padding:3px 9px;align-self:center;margin-top:4px}
.an.l{background:var(--purple-pale);border-color:#ddd7ff}.an.l b{color:var(--purple-deep)}
.aa{display:flex;align-items:center;justify-content:center;color:var(--purple);font-weight:900;font-size:24px}
.lg-l,.lg-r{display:inline-block;width:16px;height:16px;border-radius:5px;vertical-align:-2px;margin-left:12px}.lg-l{background:var(--purple-pale);border:1px solid #c9c0ff}.lg-r{background:#fff;border:1px solid var(--line)}
.mchips{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px}
.mchips div{border-radius:14px;background:#f6f5f7;padding:14px 16px}.mchips small{display:block;font-size:14px;font-weight:800;color:var(--muted)}.mchips b{font-size:21px;font-weight:900;color:var(--purple-deep)}
.ilist{display:flex;flex-direction:column;gap:12px;margin-top:16px}.ilist div{font-size:19px;font-weight:700;display:flex;gap:14px}.ilist small{flex:none;width:52px;font-size:14px;font-weight:900;color:var(--purple-deep);padding-top:3px}
/* funnel (3.2) */
.funnel{margin-top:24px;flex:1;padding:34px 44px;display:flex;flex-direction:column;justify-content:space-around}
.fr{display:grid;grid-template-columns:1fr 430px;gap:30px;align-items:center}
.fb{height:96px;border-radius:20px;background:linear-gradient(90deg,#efedf8,#e2ddf8);display:flex;flex-direction:column;justify-content:center;padding:0 30px;margin:0 auto}
.fb b{font-size:30px;font-weight:900;letter-spacing:-.04em}.fb span{font-size:17px;font-weight:700;color:var(--muted)}
.fb.on{background:var(--purple)}.fb.on b,.fb.on span{color:#fff}
.ft.g{border-left:4px solid var(--purple);padding:6px 0 6px 18px;font-size:18px;font-weight:700;color:var(--muted);line-height:1.4}.ft.g b{display:block;font-size:22px;font-weight:900;color:var(--ink)}
/* weights (3.3) */
.wts{padding:30px 38px}
.wk{font-size:18px;font-weight:900;color:var(--purple-deep);letter-spacing:.02em}
.wbar{display:flex;height:110px;border-radius:20px;overflow:hidden;margin-top:12px}
.wbar>div{display:flex;flex-direction:column;justify-content:center;padding:0 24px}.wbar b{font-size:30px;font-weight:900}.wbar small{font-size:16px;font-weight:700;opacity:.85}
.wbar .r{background:#e2ddf8;color:var(--purple-deep)}.wbar .m{background:var(--purple);color:#fff}
.wsub{display:flex;height:46px;margin-top:8px;border-radius:12px;overflow:hidden}.wsub div{display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;color:var(--purple-deep);background:#f0eefb}.wsub div+div{background:#e6e2fa}
.wline{margin-top:12px;font-size:21px;font-weight:700;line-height:1.5}
.fb2{padding:26px 30px}.fb2-k{font-size:18px;font-weight:900;color:var(--purple-deep);margin-bottom:14px}
.fb2-r{display:flex;flex-wrap:wrap;gap:8px}.fb2-r span{font-size:17px;font-weight:800;background:#fff;border-radius:10px;padding:6px 12px}
.fb2-to{font-size:26px;font-weight:900;color:var(--purple);margin:8px 0}.fb2-res{font-size:24px;font-weight:800}.fb2-res b{color:var(--purple);font-size:30px}
/* pipeline (3.4) */
.pipe{margin-top:24px;padding:30px 30px;display:grid;grid-template-columns:.8fr 34px 1.35fr 34px 1fr 34px 1.15fr 34px .95fr;align-items:stretch;flex:1}
.pn{border-radius:20px;border:1px solid var(--line);background:#fff;padding:20px 16px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:8px}
.pn b{font-size:23px;font-weight:900;letter-spacing:-.03em}.pn>span{font-size:15px;font-weight:700;color:var(--muted);line-height:1.4}
.pi{width:70px;height:70px;border-radius:20px;background:var(--purple-pale);display:flex;align-items:center;justify-content:center}
.pn.hi{background:var(--purple-pale);border-color:#ddd7ff}.pn.hi .pi{background:#fff}
.pa{display:flex;align-items:center;justify-content:center;color:var(--purple);font-weight:900;font-size:26px}
.tiles{display:grid;grid-template-columns:repeat(8,22px);gap:6px;margin-bottom:6px}.tiles i{width:22px;height:22px;border-radius:6px;background:#d9d4f7}.tiles i.p{background:var(--purple)}
.lg{display:inline-block;width:12px;height:12px;border-radius:3px;background:#d9d4f7;margin:0 5px 0 2px;vertical-align:-1px}.lg.p{background:var(--purple)}
.pn.split{padding:12px;gap:10px}.sp{width:100%;flex:1;display:flex;align-items:center;gap:12px;border-radius:14px;background:#f6f5f7;padding:10px 14px;text-align:left}.sp b{display:block;font-size:19px}.sp span{font-size:14px;font-weight:700;color:var(--muted)}.sp.img{background:var(--amber-soft)}.sp.img .ic{color:var(--amber)}
/* duo panels (3.5, 3.6) */
.duo{padding:30px 36px;display:flex;flex-direction:column}
.duo-k{display:flex;align-items:center;gap:12px;font-size:26px;font-weight:900;letter-spacing:-.03em}
.hb{display:flex;flex-direction:column;gap:16px;margin:auto 0}.hb-b{height:70px!important}.hb-r{display:flex;align-items:center;gap:14px}.hb-r>span{width:30px;font-size:17px;font-weight:900;color:var(--muted)}
.hb-b{height:58px;border-radius:14px;color:#fff;font-size:24px;font-weight:900;display:flex;align-items:center;justify-content:flex-end;padding-right:18px}
.scale{position:relative;height:120px;margin:auto 0}
.sc-line{position:absolute;left:0;right:0;top:56px;height:8px;border-radius:4px;background:#e6e2ea}
.sc-gap{position:absolute;top:50px;height:20px;border-radius:10px;background:var(--red-soft);border:2px solid var(--red)}.sc-gap span{position:absolute;left:50%;transform:translateX(-50%);top:-40px;font-size:24px;font-weight:900;color:var(--red);white-space:nowrap}
.sc-d{position:absolute;top:84px;transform:translateX(-50%);font-size:15px;font-weight:800;color:var(--muted)}
.sc-d::before{content:'';position:absolute;left:50%;top:-30px;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:var(--ink)}
.sc-0,.sc-100{position:absolute;top:84px;font-size:14px;font-weight:800;color:var(--muted)}.sc-0{left:0}.sc-100{right:0}
.vflow{display:flex;align-items:stretch;gap:8px;margin:auto 0;height:230px}
.vflow>div{flex:1;border-radius:18px;background:#f6f5f7;padding:18px 10px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:6px}
.vflow>div b{font-size:19px;font-weight:900}.vflow>div span{font-size:14px;font-weight:700;color:var(--muted)}
.vflow>div.on{background:var(--purple-pale)}.vflow>i{font-style:normal;display:flex;align-items:center;color:var(--purple);font-weight:900;font-size:22px}
/* cost + deploy (3.7) */
.cost,.dep{padding:30px 36px;display:flex;flex-direction:column}
.cb{display:grid;grid-template-columns:56px 1fr;align-items:center;gap:14px;margin-top:18px}.cb>span{font-size:17px;font-weight:900;color:var(--muted)}
.cb>b{grid-column:2;font-size:30px;font-weight:900;margin-top:-6px}
.cb-b{height:66px;border-radius:14px}.cb-b.c{background:var(--ink)}.cb-b.p{background:var(--purple);display:flex;align-items:center;padding-left:22px}.cb-b.p b{color:#fff;font-size:24px;font-weight:900}
.ledger{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:auto}.ledger div{border-top:2px solid var(--line);padding-top:12px}.ledger b{display:block;font-size:40px;font-weight:900;letter-spacing:-.04em}.ledger span{font-size:16px;font-weight:700;color:var(--muted)}
.dp{display:flex;flex-direction:column;gap:6px;margin-top:6px}.dp>div{border-radius:14px;background:#f6f5f7;padding:12px 20px;display:flex;justify-content:space-between;align-items:center}.dp>div b{font-size:21px;font-weight:900}.dp>div span{font-size:15px;font-weight:700;color:var(--muted)}
.dp>div.on{background:var(--purple-pale)}.dp>div.on b{color:var(--purple-deep)}.dp>i{font-style:normal;text-align:center;color:var(--purple);font-weight:900;font-size:18px;line-height:1}
/* documents (4.3) */
.sitefoot{background:#121016;border-radius:18px;padding:16px 26px;display:flex;align-items:center;gap:26px}.sf-k{flex:none;font-size:14px;font-weight:900;color:#b9b0ff;letter-spacing:.04em;width:130px;line-height:1.35}.sf-t{font-size:15.5px;font-weight:600;color:#d9d5dd;line-height:1.75}.sf-t i{display:inline-block;width:22px}
.cbw .cb{display:flex;align-items:center;margin-top:24px}.cbw .cb>span{width:96px;flex:none}.cbw .cb>b{margin:0 0 0 18px;font-size:30px}.cbw .cb-b{height:72px;flex:none}.cbw .cb-b.p{flex:1}
.stk{display:flex;height:66px;border-radius:14px;overflow:hidden;margin-top:6px}.stk>div{display:flex;align-items:center;padding-left:16px;color:#fff;font-size:20px;font-weight:900;white-space:nowrap;overflow:hidden}
.stk-l{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:16px;font-size:17px;font-weight:800;color:var(--muted)}.stk-l i{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:8px;vertical-align:-1px}
.dp>div em{font-style:normal;flex:none;margin-left:16px;background:var(--red);color:#fff;font-size:18px;font-weight:900;border-radius:999px;padding:4px 14px}
.bizslot{height:100%;border:3px dashed #b9b0ff;border-radius:14px;background:#f7f5ff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center}.bizslot b{font-size:26px;font-weight:900;color:var(--purple-deep)}.bizslot span{font-size:16px;color:var(--muted);line-height:1.5}
.docfig{display:flex;flex-direction:column;gap:8px;flex:none}.docfig img{display:block;width:auto;border-radius:10px;border:1px solid var(--line);box-shadow:var(--shadow);background:#fff}.dcap{font-size:16px;font-weight:800;color:var(--ink);text-align:center}
.ev{flex:1;min-height:0;position:relative;display:grid;grid-template-columns:1040px 1fr;gap:30px;margin-top:-6px}
.ev-a,.ev-b{position:relative}
.sd{position:absolute;border-radius:10px;background:#fff;box-shadow:0 18px 40px rgba(28,20,48,.22),0 2px 6px rgba(28,20,48,.12);border:1px solid var(--line)}
.sd img{display:block;height:690px;width:auto;border-radius:10px}
.sd.p img{height:auto;width:600px}
.sd .tag{position:absolute;left:14px;top:-16px;background:var(--ink);color:#fff;font-size:16px;font-weight:800;padding:6px 14px;border-radius:999px;white-space:nowrap}
.sd.p .tag{background:var(--purple-deep)}
.pflow{display:grid;grid-template-columns:1fr auto 1.15fr auto 1fr;align-items:stretch;gap:18px}
.pf{padding:28px 32px;display:flex;flex-direction:column}.pf.on{border:3px solid var(--red);box-shadow:0 14px 34px rgba(242,47,70,.14)}
.pf-n{width:38px;height:38px;border-radius:50%;background:var(--ink);color:#fff;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center;margin-bottom:14px}.pf.on .pf-n{background:var(--red)}
.pf-k{font-size:30px;font-weight:900;letter-spacing:-.04em;line-height:1.3}.pf-m{display:flex;align-items:center;gap:18px;margin-top:14px}
.pf-a{font-style:normal;align-self:center;font-size:40px;font-weight:900;color:var(--muted)}
.docimg{position:relative;border-radius:14px;overflow:hidden;box-shadow:var(--shadow);background:#fff;border:1px solid var(--line)}
.docimg img{display:block;width:100%;height:auto}
.docimg .mask{position:absolute;background:#2b2730;border-radius:4px}
.docimg .cap{position:absolute;left:0;right:0;bottom:0;background:rgba(18,16,22,.82);color:#fff;font-size:15px;font-weight:800;padding:8px 12px}
.st{padding:18px 24px;display:flex;flex-direction:column;gap:4px}.st small{font-size:14px;font-weight:900;color:var(--purple-deep);letter-spacing:.04em}.st b{font-size:26px;font-weight:900;letter-spacing:-.03em}.st span{font-size:16px;font-weight:700;color:var(--muted)}
.patent{font-family:var(--mono);font-size:16px;color:var(--purple-deep);font-weight:700}
"""

def esc(s): return s
order = [0]
def shell(eyebrow, title, content, cls='', source='', brand=True, wrap=False):
    order[0] += 1
    b = '<div class="brand"><img src="assets/icon.svg" alt="">Dev<b>Fit</b></div>' if brand else ''
    return f'''<section class="slide {cls}" data-order="{order[0]}" data-title="{re.sub('<[^>]+>','',title)[:40].replace('"','&quot;')}">
  <div class="slide-shell">
    {b}
    <header class="topline"><div class="eyebrow">{eyebrow}</div><h1 class="title{' wrap' if wrap else ''}">{title}</h1></header>
    <div class="slide-content">{content}</div>
    <div class="folio"></div>
    <div class="source">{source}</div>
  </div>
</section>'''

def raw(cls, inner, title):
    order[0] += 1
    return f'<section class="slide {cls}" data-order="{order[0]}" data-title="{title}">{inner}</section>'

def divider(kicker, title, sub):
    return raw('divider', f'''<div class="slide-shell"><div class="divider-copy"><div class="divider-kicker">{kicker}</div><div class="divider-title">{title}</div><div class="divider-sub">{sub}</div></div><div class="folio"></div></div>''', title)

def kpi(metric, label, k='', cls='', mcls='', style=''):
    kk = f'<div class="kpi-k">{k}</div>' if k else ''
    return f'<div class="panel kpi {cls}" style="{style}">{kk}<div class="metric {mcls}">{metric}</div><div class="metric-label">{label}</div></div>'

def badge(t, c=''): return f'<span class="badge {c}">{t}</span>'
def ul(items, cls=''): return f'<ul class="list {cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def table(head, rows, cls=''):
    h = ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table class="matrix {cls}"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'
def flow(nodes, cols=None):
    parts = []
    for i, n in enumerate(nodes):
        if isinstance(n, tuple): t, sub, acc = (n + ('',))[:3]
        else: t, sub, acc = n, '', ''
        s = f'<span class="sub">{sub}</span>' if sub else ''
        parts.append(f'<div class="flow-node {acc}">{t}{s}</div>')
        if i < len(nodes) - 1: parts.append('<div class="flow-arrow">→</div>')
    g = ' 56px '.join(['1fr'] * len(nodes))
    return f'<div style="display:grid;grid-template-columns:{g};align-items:stretch">{"".join(parts)}</div>'
def steps(items):
    return '<div class="step-strip" style="grid-template-columns:repeat(%d,1fr)">' % len(items) + ''.join(
        f'<div class="step"><div class="dot">{i+1}</div><div class="t">{t}</div><div class="s">{s}</div></div>' for i, (t, s) in enumerate(items)) + '</div>'
def todo(t): return f'<span class="todo">【{t}】</span>'

# ---------- SVG charts ----------
FONT = 'font-family="Pretendard,Apple SD Gothic Neo,sans-serif"'
def bars(labels, values, w, h, colors=None, fmt='{:g}', vmax=None, label_size=17, val_size=22, stacked=None, unit=''):
    n = len(labels); pad_l, pad_b, pad_t = 10, 46, 40
    vmax = vmax or max((sum(v) if isinstance(v, (list, tuple)) else v) for v in values) * 1.12
    cw = (w - pad_l * 2) / n; bw = min(cw * 0.58, 160)
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>']
    base = h - pad_b
    out.append(f'<line x1="{pad_l}" y1="{base}" x2="{w-pad_l}" y2="{base}" stroke="#c9c4d0" stroke-width="2"/>')
    for i, (lab, v) in enumerate(zip(labels, values)):
        cx = pad_l + cw * i + cw / 2
        segs = v if isinstance(v, (list, tuple)) else [v]
        y = base
        for j, sv in enumerate(segs):
            bh = (h - pad_b - pad_t) * sv / vmax
            col = (stacked[j] if stacked else (colors[i] if colors else '#6c5ce7'))
            out.append(f'<rect x="{cx-bw/2:.1f}" y="{y-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="6" fill="{col}"/>')
            y -= bh
        tot = sum(segs)
        out.append(f'<text x="{cx:.1f}" y="{y-10:.1f}" text-anchor="middle" font-size="{val_size}" font-weight="900" fill="#151218">{fmt.format(tot)}{unit}</text>')
        out.append(f'<text x="{cx:.1f}" y="{h-14}" text-anchor="middle" font-size="{label_size}" font-weight="700" fill="#746f7b">{lab}</text>')
    out.append('</svg>')
    return ''.join(out)

def line(labels, values, w, h):
    pad_l, pad_r, pad_b, pad_t = 30, 30, 44, 46
    vmax = 95; n = len(values)
    xs = [pad_l + (w - pad_l - pad_r) * i / (n - 1) for i in range(n)]
    ys = [h - pad_b - (h - pad_b - pad_t) * v / vmax for v in values]
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
    area = f'{xs[0]:.1f},{h-pad_b} ' + pts + f' {xs[-1]:.1f},{h-pad_b}'
    o = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>',
         f'<polygon points="{area}" fill="rgba(108,92,231,.12)"/>',
         f'<polyline points="{pts}" fill="none" stroke="#6c5ce7" stroke-width="5" stroke-linejoin="round"/>',
         f'<line x1="{pad_l}" y1="{h-pad_b}" x2="{w-pad_r}" y2="{h-pad_b}" stroke="#c9c4d0" stroke-width="2"/>']
    for i, (x, y, v, l) in enumerate(zip(xs, ys, values, labels)):
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#fff" stroke="#6c5ce7" stroke-width="4"/>')
        if i in (0, n - 1) or v in (40, 58):
            o.append(f'<text x="{x:.1f}" y="{y-18:.1f}" text-anchor="middle" font-size="{30 if i==n-1 else 20}" font-weight="900" fill="{"#4d3fc9" if i==n-1 else "#151218"}">{v}</text>')
        if i % 2 == 0 or i == n - 1:
            o.append(f'<text x="{x:.1f}" y="{h-12}" text-anchor="middle" font-size="16" font-weight="700" fill="#746f7b">{l}</text>')
    o.append('</svg>')
    return ''.join(o)

ACK = '이 성과는 2026년도 과학기술정보통신부의 재원으로 정보통신기획평가원의 지원을 받아 수행된 결과물임 (IITP-2026-AI·SW마에스트로)'
ACK_EN = 'This work was supported by the Institute of Information &amp; Communications Technology Planning &amp; Evaluation(IITP) grant funded by the Ministry of Science and ICT(MSIT) (IITP-2026-AI·SW Maestro)'


# ---- 문제 → 해결 → 수치 (PSN) ----
def psn(prob, sol, num, sm=False, tag=''):
    """prob/num = (metric or None, text). sol = text."""
    c = ' sm' if sm else ''
    def card(kind, label, metric, text, mcls):
        m = f'<div class="psn-m {mcls}">{metric}</div>' if metric else ''
        return f'<div class="panel psn-c {kind}"><div class="psn-k">{label}</div>{m}<div class="psn-t">{text}</div></div>'
    t = f'<div class="psn-tag">{tag}</div>' if tag else ''
    return (f'<div class="psn{c}">{t}'
            + card('red-soft', '문제', prob[0], prob[1], 'red')
            + '<div class="psn-a">→</div>'
            + card('', '해결', None, sol, '')
            + '<div class="psn-a">→</div>'
            + card('soft', '수치', num[0], num[1], 'purple')
            + '</div>')

# ===== 기술 장표 v3 — 장표마다 중심 도식 1개 + 상단 «문제 → 해결 → 수치» 한 줄 =====
def sb(prob, sol, num):
    """story bar. prob/num = (metric|None, text)"""
    def cell(cls, label, metric, text):
        m = f'<div class="sb-m">{metric}</div>' if metric else ''
        return f'<div class="sb-c {cls}"><span class="sb-k">{label}</span>{m}<div class="sb-t">{text}</div></div>'
    return ('<div class="sb">' + cell('p', '문제', prob[0], prob[1]) + '<div class="sb-a">→</div>'
            + cell('s', '해결', None, sol) + '<div class="sb-a">→</div>' + cell('n', '수치', num[0], num[1]) + '</div>')

def mini(rows):
    """panel 안의 작은 문제/해결/수치 3줄. rows = [(kind, metric|None, text)]"""
    lab = {'p': '문제', 's': '해결', 'n': '수치'}
    out = []
    for k, m, t in rows:
        mm = f'<b class="mn-m">{m}</b>' if m else ''
        out.append(f'<div class="mn {k}"><span class="sb-k">{lab[k]}</span>{mm}<span class="mn-t">{t}</span></div>')
    return '<div class="mns">' + ''.join(out) + '</div>'

ICON = {
 'shield': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 'db': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13"/><path d="M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/></svg>',
 'mic': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0013 0M12 17.5V21"/></svg>',
 'spk': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M16 9a4 4 0 010 6M18.5 6.5a7.5 7.5 0 010 11"/></svg>',
 'doc': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg>',
 'img': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3.5" y="4.5" width="17" height="15" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M20.5 16l-5-5-9 8.5"/></svg>',
 'link': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/></svg>',
 'search': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>',
 'chat': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></svg>',
 'coin': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="8.5"/><path d="M9 9.5c0-1 1.3-1.8 3-1.8s3 .8 3 1.8-1.3 1.6-3 2-3 1-3 2 1.3 1.8 3 1.8 3-.8 3-1.8M12 6v1.7M12 16.3V18"/></svg>',
}
def ic(name, s=34, cls=''): return f'<span class="ic {cls}">' + ICON[name].replace('{s}', str(s)) + '</span>'

class Slides(list):
    """장표 목록. append(html) 후 note(text)로 바로 앞 장표에 발표자 노트를 붙인다."""
    def __init__(self):
        super().__init__(); self.notes = {}
    def note(self, text):
        assert len(self), 'note()는 append() 다음에'
        self.notes[len(self) - 1] = (self.notes.get(len(self) - 1, '') + ('\n\n' if len(self) - 1 in self.notes else '') + text)


# ---------- 내비게이션 (2026-11-06, ppt-start) ----------
NAV_CSS = r"""
.nav{display:flex;gap:10px;align-items:stretch;margin:0 0 22px}
.nav span{flex:1;padding:12px 14px;border-radius:12px;background:#ece9f1;color:#a19ba7;font-size:19px;font-weight:900;letter-spacing:-.03em;text-align:center;white-space:nowrap}
.nav span.on{background:var(--purple);color:#fff}
.nav span.tail{flex:.8;background:transparent;border:2px dashed #d9d4e0}
.nav span.tail.on{border-color:var(--purple);color:var(--purple);background:var(--purple-pale)}
.navs{flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px;padding:0 140px}
.navs div{display:flex;align-items:center;gap:30px;padding:26px 40px;border-radius:24px;background:#ece9f1;color:#b3adba;font-size:52px;font-weight:900;letter-spacing:-.05em}
.navs div b{font-size:34px;width:60px}
.navs div.on{background:var(--purple);color:#fff;box-shadow:0 18px 40px rgba(108,92,231,.28)}
.navs div small{margin-left:auto;font-size:24px;font-weight:800;opacity:.85}
"""
EXTRA += r"""
/* 11-07 사용자 지시: 알약(pill)형 UI 금지 → 남겨야 할 라벨은 6px 사각 태그로. 섹션 CSS보다 우선하도록 !important */
.badge,.gantt .ev .d,.psn-tag,.sb-k,.opt em,.an em,.dp>div em,.sd .tag{border-radius:6px!important}
"""
EXTRA += NAV_CSS

def _on(i, name, current):
    cur = current if isinstance(current, (list, tuple)) else [current]
    return i in cur or name in cur

def nav(items, current, tail=None):
    """장 상단 띠. items: 단계 이름 리스트 · current: 인덱스/이름(여러 칸이면 리스트, None이면 전부 흐림) · tail: 흐린 꼬리 칸 이름"""
    out = [f'<span class="{"on" if current is not None and _on(i, n, current) else ""}">{n}</span>' for i, n in enumerate(items)]
    if tail:
        out.append(f'<span class="tail{" on" if current is not None and _on(len(items), tail, current) else ""}">{tail}</span>')
    return '<div class="nav">' + ''.join(out) + '</div>'

def nav_slide(eyebrow, title, items, current, subs=None, source=''):
    """장 하나 전체를 쓰는 파트 전환 장 (ASAP «콘텐츠 생성 과정» 방식). subs: 항목별 보조 문구 리스트(선택)"""
    rows = ''.join(f'<div class="{"on" if _on(i, n, current) else ""}"><b>{i+1}</b>{n}' + (f'<small>{subs[i]}</small>' if subs and subs[i] else '') + '</div>' for i, n in enumerate(items))
    return shell(eyebrow, title, f'<div class="navs">{rows}</div>', source=source)
