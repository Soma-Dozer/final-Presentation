# -*- coding: utf-8 -*-
# DevFit 최종발표 완성본 생성기 — 중간평가 덱(Devfit/Mid_Presentation/irdeck_new.html) 디자인 시스템 그대로 사용
# 구조: last-dance/06-최종구성.md v1.3 · 수치 정본: last-dance/collect/00-통합보고.md
import re, datetime as dt
MID = '/Users/aiden/dev/teams/ASM/Devfit/Mid_Presentation/irdeck_new.html'
OUT = '/Users/aiden/dev/teams/ASM/last-dance/final-deck/index.html'
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
    return f'''<section class="slide {cls}" data-order="{order[0]}" data-title="{re.sub('<[^>]+>','',title)[:40]}">
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

S = []
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

# ================= 02 목차 =================
toc = [('01', '소개', '문제 · 솔루션 · 차별점', 'p3–8', '결과물 50'), ('02', '시연', 'Live Demo 5분', 'p9', '결과물 50'),
       ('03', '개발', '기술 3.1–3.8 · 수행과정 3.9–3.13', 'p11–22', '결과물 50 · 수행과정 20'),
       ('04', 'Effect', '지금까지 4.1–4.3 · 앞으로 4.4', 'p24–28', '기대효과 30'), ('05', '마무리', '', 'p29', '')]
rows = ''.join(f'''<div style="display:grid;grid-template-columns:120px 300px 1fr 160px 300px;align-items:center;padding:38px 0;border-bottom:1px solid var(--line)">
 <div style="font-size:44px;font-weight:900;color:var(--purple)">{a}</div><div style="font-size:40px;font-weight:900;letter-spacing:-.04em">{b}</div>
 <div class="body-copy" style="font-size:25px">{c}</div><div class="small-copy" style="font-size:21px;font-weight:800">{d}</div><div>{badge(e) if e else ''}</div></div>''' for a, b, c, d, e in toc)
# (목차 장표 제거 2026-11-05)

# ================= 1. 소개 =================
S.append(shell('Problem', 'AI가 코드를 같이 짜면서, 기술면접은 <span class="red">경험</span>을 묻습니다', f'''
<div class="pflow">
  <div class="panel pf"><div class="pf-n">1</div><div class="pf-k">AI로 코드를 짜는 게 기본이 됐다</div><div class="pf-m"><span class="metric" style="font-size:76px">84%</span><span class="metric-label">AI 도구를 쓰거나<br>쓸 계획인 개발자</span></div></div>
  <i class="pf-a">→</i>
  <div class="panel pf on"><div class="pf-n">2</div><div class="pf-k">그래서 기술면접은 <span style="color:var(--red)">경험 위주</span>로 묻는다</div><div class="body-copy" style="font-size:24px;margin-top:14px">«무엇을 만들었나»보다 <b>«왜 그렇게 짰나 · 어디서 막혔나 · 무엇을 바꿨나»</b></div></div>
  <i class="pf-a">→</i>
  <div class="panel pf"><div class="pf-n">3</div><div class="pf-k">지원자는 <span style="color:var(--red)">무엇을 물을지</span> 모른다</div><div class="body-copy" style="margin-top:14px"><span class="quote" style="font-size:26px">«1달 전에 짠 코드<br>잘 기억이 안 나거든요»</span><div class="quote-who" style="margin-top:6px">현직 개발자 인터뷰</div></div></div>
</div>
<div style="display:grid;grid-template-columns:1.25fr .75fr;gap:34px;margin-top:34px;flex:1;min-height:0">
  <div class="panel soft" style="padding:30px 40px;display:flex;align-items:center;gap:40px">
    <div class="metric purple" style="font-size:110px">60%</div>
    <div class="body-copy" style="font-size:27px;font-weight:700;color:var(--ink)">미국 채용 담당자 60%가 «AI 때문에 지원자의 실제 역량을 평가하기가 더 어려워졌다»고 답했습니다</div></div>
  <div class="panel" style="padding:30px 36px;display:flex;flex-direction:column;justify-content:center;text-align:center">
    <div class="metric red">46%</div><div class="metric-label">AI 결과의 정확도를<br>신뢰하지 않는 개발자</div></div>
</div>''', cls='problem', source='WGU, Workforce Decoded 2026 (미국 채용 실무자 n=3,128) · Stack Overflow Developer Survey 2025 · 현직 개발자 인터뷰(2026-09-07)'))

S.append(shell('Problem', '«Claude Code에 GitHub 링크 주면 <span class="red">되지 않나요?</span>»', f'''
<div style="display:grid;grid-template-columns:.9fr 1.1fr;gap:38px;flex:1;min-height:0">
  <div style="display:flex;flex-direction:column;gap:22px">
    <div class="panel" style="padding:28px 32px"><div class="quote">«이미 내가 쓰는 AI로<br>다 준비하는 부분»</div><div class="quote-who">개발자 사용자 인터뷰</div></div>
    <div class="panel" style="padding:28px 32px"><div class="quote">«GitHub 링크를 Claude Code에<br>넘기면 된다»</div><div class="quote-who">IT 기업 대표 · 서면 회신(10-26)</div></div>
    <div class="body-copy" style="font-size:22px;margin-top:auto">그래서 직접 실험했습니다 — <strong>공개 레포 4개 · 같은 공고 · 같은 지시</strong></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:22px">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
      <div class="panel red-soft kpi"><div class="kpi-k">레포 링크만 받은 채팅형 AI</div><div class="metric red" style="font-size:92px">0 / 18</div><div class="metric-label">제시한 근거 중 실존 0개<br>«레포를 확인해 보니»라고 쓰고 없는 커밋·파일을 만들었습니다</div></div>
      <div class="panel soft kpi"><div class="kpi-k">DevFit</div><div class="metric purple" style="font-size:92px">28 / 28</div><div class="metric-label">제시한 근거 전부 실존<br>커밋 SHA · 파일 · 코드</div></div>
    </div>
    {table(['', 'AI 모의면접 (사람인·Final Round 등)', 'DevFit'], [['입력', '이력서', '공고 URL + 내 GitHub'], ['본인 커밋만 골라 읽기', '<span class="no">✕</span>', '<span class="yes">✓</span>'], ['한국 채용 공고 맞춤', '일부', '29곳 (플랫폼 5 + 기업 24)']], 'sm plain')}
  </div>
</div>
<div class="callout" style="margin-top:26px">차이는 모델이 아니라, <strong>레포를 읽고 대조하는 절차를 서버가 매번 강제하는가</strong>입니다</div>''', cls='problem', source='범용 AI 비교 파일럿 (2026-11-05, 결정론 채점) · 기능 비교: 각 서비스 공개 페이지 기준'))

S.append(shell('Solution', '공고 URL 하나와 <span class="purple">내 GitHub</span>면 그 공고용 면접이 준비됩니다', f'''
<div style="display:grid;grid-template-columns:1.25fr .75fr;gap:38px;flex:1;min-height:0">
  <div style="display:flex;flex-direction:column;gap:26px;min-height:0">
    {steps([('공고 URL 붙여넣기', '플랫폼 5곳 · 기업 채용사이트 24곳'), ('내 레포 선택', '공개/비공개 범위를 직접 선택'), ('공고 맞춤 질문', '질문마다 «이 질문이 나온 내 코드»'), ('텍스트·음성 연습', '답변 피드백 · 꼬리질문')])}
    <div class="browser" style="flex:1;min-height:0"><div class="browser-bar"><i></i><i></i><i></i><span class="browser-url">devfit.app</span></div><img src="assets/q-list.jpg" alt="공고 맞춤 예상 면접 질문 화면"></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:22px">
    {kpi('0개', '같은 레포에 공고만 바꿨을 때<br>문장이 같은 질문 (115문항)', '공고마다 다른 질문', 'soft', 'purple', 'flex:1')}
    {kpi('29곳', '채용 플랫폼 5곳 + 기업 채용사이트 24곳<br>공고 자동 수집', '공고 수집', '', '', 'flex:1')}
    <div class="callout" style="font-size:23px"><strong>합불 판정·랭킹 없음</strong> — 최종 판단은 사람</div>
  </div>
</div>''', source='화면: 팀원 본인 레포(Signify) × 프론트엔드 공고 실제 분석 결과 · 채용 플랫폼: 잡코리아·사람인·원티드·링커리어·인크루트'))

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

S.append(shell('Key Features', '근거 코드가 없으면 <span class="purple">묻지 않습니다</span>', f'''
{sb(('0 / 18', '레포 링크만 받은 범용 AI가 낸 근거 중 실존한 것'), '질문 속 식별자를 근거 diff와 <b>대조</b>', ('353 / 353', '모든 질문에 커밋 · 파일 출처'))}
<div class="hero" style="grid-template-columns:1.22fr .78fr">
  <div class="browser" style="min-height:0"><div class="browser-bar"><i></i><i></i><i></i><span class="browser-url">devfit.app · 예상 면접 질문 3 — 실제 분석 결과</span></div><img src="assets/q3.jpg" alt="질문과 근거 코드" style="object-fit:contain"></div>
  <div class="panel gate">
    <div class="gate-k">출력 게이트</div>
    <div class="gate-q">질문 속 식별자<div class="chips"><span>useCamera</span><span>useEffect</span><span>cancelled</span></div></div>
    <div class="gate-arrow">↓ 근거 diff와 대조</div>
    <div class="gate-out">
      <div class="go keep"><b>유지</b><span>전부 코드에 있음</span></div>
      <div class="go ask"><b>재질의</b><span>일부만 있음</span></div>
      <div class="go drop"><b>폐기</b><span>코드에 없는 이름</span></div>
    </div>
    <div class="gate-num"><div><b>84건</b><span>운영 30일 차단</span></div><div><b>5 / 63</b><span>실행 1회 폐기</span></div></div>
    <div style="margin-top:auto">{badge('특허 출원 10-2026-0214809')}</div>
  </div>
</div>''', source='0/18: 범용 AI 비교 파일럿(공개 레포 4개, 2026-11-05, 부록 A2) · 353/353: 평가 세트 전수 · 84건: 관리자 콘솔 최근 30일'))

# ---------- Key ② ----------
dots = ''.join('<i></i>' for _ in range(8))
S.append(shell('Key Features', '팀 프로젝트에서도 <span class="purple">내가 짠 코드</span>만 봅니다', f'''
{sb(('91 / 677', '여러 명이 쓴 공개 OSS에서 그 사용자의 커밋'), '커밋을 작성자로 귀속한 뒤 <b>본인 커밋만</b> 근거로', ('8 / 8', 'DevFit 질문 근거가 본인 커밋'))}
<div class="hero" style="grid-template-columns:1.45fr .55fr">
  <div class="panel own">
    <div class="own-row"><div class="own-k">공개 OSS · 커밋 677개</div>
      <div class="own-bar"><div class="me" style="width:13.4%">91</div><div class="other">다른 기여자 586 — 87%는 남이 짠 코드</div></div></div>
    <div class="own-arrow">↓ 작성자 귀속 (GitHub numeric id)</div>
    <div class="own-w">
      <div class="w me"><span class="av"></span><div><b>1.0</b><small>본인 author</small></div></div>
      <div class="w co"><span class="av"></span><div><b>0.70</b><small>Co-authored-by</small></div></div>
      <div class="w ot"><span class="av"></span><div><b>제외</b><small>다른 팀원</small></div></div>
    </div>
    <div class="own-arrow">↓ 남은 커밋만 점수화 (p12)</div>
    <div class="own-row"><div class="own-k">DevFit 질문 근거 8개</div><div class="own-dots">{dots}<b>8 / 8 본인 커밋</b></div></div>
  </div>
  <div class="panel" style="padding:36px 36px;display:flex;flex-direction:column;justify-content:center">
    <div style="font-size:34px;font-weight:900;letter-spacing:-.04em;line-height:1.38">남이 짠 코드로<br>질문을 받으면<br>면접에서 <span style="color:var(--red)">설명할 수<br>없습니다</span></div>
    <div style="margin-top:26px">{badge('특허 출원 10-2026-0214808')}</div>
  </div>
</div>''', source='677/91: pallets/itsdangerous 공개 이력, 로그인 mitsuhiko 기준 · 8/8: 비교 파일럿 n=8(부록 A2) · 가중치 운영 반영 2026-09-09'))

# ---------- Key ③ ----------
opts = ''.join(f'<div class="opt{" hit" if k == "C" else ""}"><b>{k}</b><span>작업 {k} 요약</span>{"<em>원래 작업</em>" if k == "C" else ""}</div>' for k in 'ABCD')
S.append(shell('Key Features', '질문이 내 코드에 붙어 있는지 <span class="purple">숫자로</span> 잽니다', f'''
{sb((None, '질문이 «내 코드» 질문인지, 아무 레포에나 맞는 <b>일반론</b>인지 가릴 방법이 없었다'), '심판에게 <b>질문만</b> 주고 원래 작업을 고르게 한다', ('81.9%', '맞힌 비율 (n=177) · 우연 25%'))}
<div class="hero" style="grid-template-columns:1fr 1fr">
  <div class="panel quiz">
    <div class="quiz-q">{ic('chat', 30)}<div><small>AI 심판이 보는 것</small><b>DevFit 질문 1개 — 근거 코드는 가림</b></div></div>
    <div class="quiz-a">↓ 이 질문은 어느 작업에서 나왔나?</div>
    <div class="opts">{opts}</div>
    <div class="small-copy" style="margin-top:auto">정답이 정해져 있어 <b>우연(25%)</b>과 바로 비교됩니다. 1~5점 심판 점수는 심판만 바꿔도 흔들립니다(p14).</div>
  </div>
  <div class="panel" style="padding:20px 30px;display:flex;align-items:center;justify-content:center">
    {bars(['우연 (4지선다)', 'DevFit 질문'], [25, 81.9], 640, 520, colors=['#c9c4d0', '#6c5ce7'], fmt='{:.1f}', vmax=100, unit='%', val_size=40, label_size=24)}
  </div>
</div>''', source='질문 품질 평가 하네스 · 4지선다 식별 과제 · 우연 기준선 25%'))

# ================= 2. 시연 =================
S.append(raw('dark-slide', f'''<div class="dark-grid"></div><div class="slide-shell" style="padding:0">
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding-left:118px;z-index:2">
  <div style="font-size:30px;color:#b9b0ff;font-weight:900;margin-bottom:24px">02 · 시연</div>
  <div style="color:#fff;font-size:150px;font-weight:900;letter-spacing:-.06em;line-height:1">Live Demo</div>
  <div style="margin-top:40px;color:#d9d5dd;font-size:44px;font-weight:800;letter-spacing:-.03em">https://devfit.app</div>
  <div style="margin-top:34px;color:#8f8996;font-size:26px;font-weight:700">공고 URL 붙여넣기 → 레포 선택 → 질문과 근거 코드 → 음성 답변 · 꼬리질문</div>
</div><div class="folio" style="left:118px;color:#6d6774"></div></div>''', 'Live Demo'))

# ================= 3. 개발 =================
S.append(divider('03 · 개발', 'Development', '방금 본 화면의 뒷면 — 기술과 수행과정'))

# ---------- 3.1 ----------
S.append(shell('Development', '<span class="purple">규칙</span>으로 좁히고, LLM은 꼭 필요한 곳에만 씁니다', f'''
<div class="panel" style="padding:34px 36px 28px">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px"><div class="small-copy" style="font-weight:800">B2C 분석 파이프라인 · DB 큐 + 워커 원자 선점 + 지수 백오프 재시도 (비동기)</div><div class="small-copy"><span class="lg-l"></span> LLM 호출 &nbsp; <span class="lg-r"></span> 규칙 · LLM 0회</div></div>
  <div class="arch">
    <div class="an l"><b>공고 수집</b><span>29곳 · OCR 폴백</span><em>비전 · 추출</em></div><div class="aa">→</div>
    <div class="an"><b>레포 수집</b><span>본인 커밋 · PR만</span></div><div class="aa">→</div>
    <div class="an l"><b>커밋 선별</b><span>규칙 + 모델 판정</span><em>gpt-6-luna</em></div><div class="aa">→</div>
    <div class="an"><b>근거 묶음</b><span>작업 단위 4~10</span></div><div class="aa">→</div>
    <div class="an"><b>게이트</b><span>입력 · 출력 대조</span></div><div class="aa">→</div>
    <div class="an l"><b>질문 생성</b><span>의도 7유형 × 난이도</span><em>추론 · 코드</em></div><div class="aa">→</div>
    <div class="an l"><b>학습실 · 음성</b><span>피드백 · 꼬리질문</span><em>STT · TTS</em></div>
  </div>
</div>
<div class="hero" style="grid-template-columns:1.2fr .8fr;margin-top:24px">
  <div class="panel" style="padding:28px 32px"><div class="infra-summary-title">역할별 모델 라우팅 · Bedrock 5종 + OpenAI</div>
    <div class="mchips">
      <div><small>추론</small><b>GLM-5</b></div><div><small>코드</small><b>Qwen3-Coder-Next</b></div><div><small>추출</small><b>GLM-4.7-Flash</b></div>
      <div><small>비전</small><b>Nova 2 Lite</b></div><div><small>사업자 OCR</small><b>Qwen3-VL</b></div><div><small>커밋 판정</small><b>gpt-6-luna</b></div>
    </div></div>
  <div class="panel" style="padding:28px 32px"><div class="infra-summary-title">서비스 · 검색 · 음성</div>
    <div class="ilist"><div><small>FE</small>Next.js 16 정적 export → S3 + CloudFront</div><div><small>BE</small>Spring Boot 3.4 · Java 21 · ECS Fargate</div><div><small>DB</small>PostgreSQL · Flyway · pgvector</div><div><small>검색</small>Cohere Embed v3 + 어휘 매칭</div><div><small>음성</small>Amazon Transcribe 스트리밍 STT · TTS</div></div></div>
</div>''', source='운영 브랜치 기준 (2026-11-03)'))

# ---------- 3.2 funnel ----------
S.append(shell('Development', '커밋 1,000개를 질문 4개까지 <span class="purple">좁혀서</span> 넣습니다', f'''
{sb(('1,000개', '한 레포에서 읽는 커밋 — 전부 LLM에 넣으면 문맥·원가를 감당 못 함'), '규칙 점수로 4단 압축한 <b>뒤에만</b> 질문 생성', ('≤ 4', '작업당 질문'))}
<div class="panel funnel">
  <div class="fr"><div class="fb" style="width:100%"><b>커밋 최대 1,000</b><span>내가 쓴 커밋 · PR만</span></div><div class="ft"></div></div>
  <div class="fr"><div class="fb" style="width:72%"><b>diff 최대 96</b><span>로직 밀도 · 기술 키워드 · 시간 분산</span></div><div class="ft"></div></div>
  <div class="fr"><div class="fb" style="width:48%"><b>작업 단위 4~10</b><span>질문 가치가 높은 묶음</span></div><div class="ft g"><b>입력 게이트</b>근거가 얇으면 «왜»·«트레이드오프»만</div></div>
  <div class="fr"><div class="fb on" style="width:30%"><b>작업당 질문 ≤ 4</b><span>의도 7유형 × 난이도</span></div><div class="ft g"><b>출력 게이트</b>식별자 대조 → 유지 · 재질의 · 폐기 (p5)</div></div>
</div>''', source='B2C 분석 경로 기준 · 각 단계 값은 상한 · 막대 길이는 개념 표현(비례 아님)'))

# ---------- 3.3 weights ----------
S.append(shell('Development', '규칙 점수가 뼈대이고, <span class="purple">모델 판정은 섞기만</span> 합니다', f'''
{sb((None, '메시지 점수만 쓰면 팀 저장소 커밋이 <b>전부 동점</b> — GitHub 최신순이 그대로 남았다'), '백분위 정규화 + 모델 판정 섞기 + 동점은 sha 순서', ('0.4 : 0.6', '규칙 : 모델 판정'))}
<div class="hero" style="grid-template-columns:1.3fr .7fr">
  <div class="panel wts">
    <div class="wk">0 · 잡음 제외</div>
    <div class="chips2"><span>merge</span><span>bump</span><span>dependabot</span><span>docs</span><span>lint</span><span>format</span></div>
    <div class="wk" style="margin-top:26px">1 · 커밋 우선순위 = 가중 합</div>
    <div class="wbar"><div class="r" style="width:40%"><b>규칙 0.4</b></div><div class="m" style="width:60%"><b>모델 판정 0.6</b><small>gpt-6-luna · 커밋 메시지 채점</small></div></div>
    <div class="wsub" style="width:40%"><div style="width:40%">키워드 0.40</div><div style="width:60%">구체성 0.60</div></div>
    <div class="wk" style="margin-top:26px">2 · 파일 단계</div>
    <div class="wline"><b>로직 줄 × 2 + 기술 키워드</b> · 패치 판정으로 품질 <b>× 0.5 ~ 1.5</b> · 동점은 sha 사전순</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:22px;min-height:0">
    <div class="panel soft fb2"><div class="fb2-k">모델이 빠지면?</div>
      <div class="fb2-r"><span>키 없음</span><span>25초 초과</span><span>채점 50% 미만</span></div>
      <div class="fb2-to">↓</div><div class="fb2-res">규칙 <b>1.0</b>으로 끝까지 진행</div></div>
    <div class="panel" style="padding:26px 30px;flex:1"><div class="fb2-k">GitHub 호출 예산</div>
      <div class="body-copy">커밋 요약 <b>1,000</b> · 상세 diff <b>96</b>을 레포 수로 나눠 씁니다.</div>
      <div style="margin-top:14px">{badge('특허 출원 10-2026-0214808')}</div></div>
  </div>
</div>''', source='운영 브랜치 GithubService · CommitDecisionBlend · application.yml (2026-11-03) · 가중치는 설정값'))

# ---------- 3.4 posting pipeline ----------
tiles = ''.join(f'<i class="{"p" if i < 5 else ""}"></i>' for i in range(29))
S.append(shell('Development', '사이트 하나 추가 = <span class="purple">클래스 1개 + 등록 1줄</span>', f'''
{sb(('22곳 중 10곳', '기업 공채 사이트에서 공고 본문이 이미지 1장'), '사이트 어댑터 + OCR 폴백 + 공고 캐시', ('22%', '사용자 공고 중 기업 사이트 (18 / 83)'))}
<div class="panel pipe">
  <div class="pn"><div class="pi">{ic('link', 40)}</div><b>공고 URL</b><span>사용자 입력</span></div>
  <div class="pa">→</div>
  <div class="pn wide"><div class="tiles">{tiles}</div><b>사이트 어댑터 29</b><span><i class="lg p"></i>채용 플랫폼 5 · <i class="lg"></i>기업 채용 사이트 24</span></div>
  <div class="pa">→</div>
  <div class="pn hi"><div class="pi">{ic('shield', 40)}</div><b>SafeFetcher</b><span>홉마다 허용 호스트 재검사 · SSRF 차단</span></div>
  <div class="pa">→</div>
  <div class="pn split"><div class="sp">{ic('doc', 30)}<div><b>본문 텍스트</b><span>그대로 사용</span></div></div><div class="sp img">{ic('img', 30)}<div><b>이미지 1장</b><span>200자 미만 → OCR</span></div></div></div>
  <div class="pa">→</div>
  <div class="pn"><div class="pi">{ic('db', 40)}</div><b>공고 캐시</b><span>30일 · 히트 시 호출 0회</span></div>
</div>
<div class="hero" style="grid-template-columns:1fr 1fr;margin-top:22px;flex:none">
  <div class="code" style="font-size:20px;line-height:1.7;white-space:pre;padding:22px 30px">interface CorporateSite {{  <span style="color:#8f86a3">// 새 사이트 = 이 구현 1개 + 레지스트리 1줄</span>
  label() · hostSuffixes() · requireSupportedUrl(uri)
  fetch(uri, SafeFetcher) · enumerate(SafeFetcher)
}}</div>
  <div class="panel" style="padding:22px 30px;display:flex;align-items:center;gap:40px">
    <div><div class="metric" style="font-size:54px">1,000</div><div class="metric-label">일일 LLM 예산 (캐시 채우기)</div></div>
    <div><div class="metric" style="font-size:54px">300</div><div class="metric-label">일일 OCR 예산 · 넘치면 다음 실행으로</div></div>
  </div>
</div>''', source='22곳 중 10곳: 2차 기업 사이트 조사 · 22%: 관리자 DB 내부 제외 공고 83건 · 운영 브랜치 prep/corporate · prep/cache'))

# ---------- 3.5 speed + harness ----------
S.append(shell('Development', '빨라졌고, <span class="purple">점수를 믿지 않는 이유</span>도 숫자로 압니다', f'''
<div class="hero" style="grid-template-columns:1fr 1fr;margin-top:0">
  <div class="panel duo">
    <div class="duo-k"><span class="num">1</span>속도 — 질문 생성 단계</div>
    {mini([('p', '93.7초', '평균 · 출력 잘림 1건'), ('s', None, '한 번에 만들던 생성 호출을 나눠서 요청 (v10 → v11)'), ('n', '49.1초', '잘림 0건 · 대신 입력 토큰 +54.2%')])}
    <div class="hb"><div class="hb-r"><span>전</span><div class="hb-b" style="width:100%;background:#c9c4d0">93.7초</div></div><div class="hb-r"><span>후</span><div class="hb-b" style="width:52.4%;background:var(--purple)">49.1초</div></div></div>
    <div class="small-copy" style="margin-top:auto">고정 사례 3개 × 2회 평균 · 전체 분석 시간이 아님</div>
  </div>
  <div class="panel duo">
    <div class="duo-k"><span class="num">2</span>품질 — 평가 하네스</div>
    {mini([('p', '17.8점', '심판 모델만 바꿔도 흔들린 문항당 점수 (n=91)'), ('s', None, '심판 절대 점수 대신 결정적 지표 13개 + 8축 루브릭 + 회귀 게이트'), ('n', 'v1 → v13', '같은 평가 세트로 버전마다 회귀 측정')])}
    <div class="scale"><div class="sc-line"></div><div class="sc-gap" style="left:52%;width:17.8%"><span>17.8점</span></div><div class="sc-d a" style="left:52%">심판 A</div><div class="sc-d b" style="left:69.8%">심판 B</div><div class="sc-0">0</div><div class="sc-100">100</div></div>
    <div class="small-copy" style="margin-top:auto">같은 심판 재채점도 12.2점 차(n=24) → 지표는 우연 대비 정답률 81.9%(p7) · 출처 100%</div>
  </div>
</div>''', source='collect/C · REPOSITORY_ANALYSIS_PERFORMANCE.md · 17.8점 = 심판 2종 문항별 차 평균 · 척도 그림은 개념 표현'))

# ---------- 3.6 RAG + voice ----------
S.append(shell('Development', '실제 기출로 맥락을 더하고, <span class="purple">말로 답하면 되묻습니다</span>', f'''
<div class="hero" style="grid-template-columns:1fr 1fr;margin-top:0">
  <div class="panel duo">
    <div class="duo-k"><span class="num">1</span>기출 RAG <span class="badge green" style="margin-left:10px">11-02 운영</span></div>
    {mini([('p', None, '내 코드 근거만으로는 그 회사가 실제로 묻는 것을 모른다'), ('s', None, '공개 출처 기출을 출처 URL과 함께 모아 하이브리드 검색'), ('n', '304개', '공개 출처')])}
    <div class="vflow"><div>{ic('doc', 30)}<b>공개 출처</b><span>URL 보존</span></div><i>→</i><div>{ic('search', 30)}<b>pgvector + 어휘</b><span>하이브리드</span></div><i>→</i><div class="on">{ic('chat', 30)}<b>질문에 연결</b><span>실제 면접 맥락</span></div></div>
  </div>
  <div class="panel duo">
    <div class="duo-k"><span class="num">2</span>음성 모의면접 <span class="badge green" style="margin-left:10px">09-16 운영</span></div>
    {mini([('p', None, '텍스트로만 답하면 말로 설명하는 연습이 안 된다 — 09-07 멘토 제안'), ('s', None, '음성 답변을 받아 적고, 답변을 보고 꼬리질문으로 되묻는다'), ('n', '9일', '제안부터 운영 반영까지')])}
    <div class="vflow"><div>{ic('mic', 30)}<b>16kHz 녹음</b><span>브라우저</span></div><i>→</i><div>{ic('doc', 30)}<b>STT</b><span>Transcribe 스트리밍</span></div><i>→</i><div class="on">{ic('chat', 30)}<b>꼬리질문</b><span>답변 기반</span></div><i>→</i><div>{ic('spk', 30)}<b>TTS</b><span>되묻기</span></div></div>
    <div style="margin-top:14px">{badge('특허 출원 10-2026-0214811')}</div>
  </div>
</div>''', source='기출: 공개 출처 304개, 출처 URL 보존 · 음성: Amazon Transcribe 스트리밍 + TTS · 멘토링 기록 09-07'))

# ---------- 3.7 deploy ----------
S.append(shell('Development', 'staging을 거치지 않은 변경은 <span class="purple">운영에 나가지 않습니다</span>', f'''
{sb((None, '검증 안 된 변경이 운영으로 바로 나갈 수 있었다'), '병합된 staging→prod PR이 없으면 <b>배포 전에 차단</b>', ('13건', '배포 전에 막은 운영 push · 운영 유출 0'))}
<div class="hero" style="grid-template-columns:1.25fr .75fr">
  <div class="panel dep">
    <div class="fb2-k">배포 경로 — 단계마다 게이트, 숫자는 실제로 막은 횟수</div>
    <div class="dp">
      <div><b>기능 브랜치 → main</b><span>테스트 · FE↔BE API 계약 대조 · 개발 배포</span><em>112회</em></div><i>↓</i>
      <div><b>staging → prod PR</b><span>승격 출처 검사 (head가 staging인가)</span><em>18회</em></div><i>↓</i>
      <div class="on"><b>prod push</b><span>승격 검증 · 개발용 문서 유출 차단</span><em>11 · 3회</em></div><i>↓</i>
      <div><b>운영 배포</b><span>GitHub Actions(OIDC) → AWS · Slack 결과 알림</span></div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:22px">
    {kpi('13건', '배포 직전에 막힌 운영 push<br>승격 11 · 유출 1 · 테스트 1', '차단', 'soft', 'purple')}
    {kpi('0건', '그중 실제로 운영에 나간 변경', '유출')}
    <div class="small-copy">운영 배포 잡 <b>429–488초 → 145–260초</b> (같은 기간 실측, 원인 분리 안 함)</div>
  </div>
</div>''', source='GitHub Actions 실패 실행 140건 jobs API 집계 · 테스트 112회는 FE·BE 합산 · 배포 시간: deploy-production 잡 실측'))

# ---------- 3.8 cost ----------
S.append(shell('Development', 'LLM 호출마다 <span class="purple">원가를 기록</span>합니다', f'''
{sb((None, '분석 1회에 실제로 얼마가 드는지 알 수 없었다'), 'LLM 호출마다 모델 단가 × 토큰을 <b>원가 원장</b>에 기록', ('약 133원', '분석 1회 LLM 원가'))}
<div class="hero" style="grid-template-columns:1.05fr .95fr">
  <div class="panel cost">
    <div class="fb2-k">원가 vs 단건 가격</div><div class="cbw">
    <div class="cb"><span>분석 1회</span><div class="cb-b c" style="width:7%"></div><b>약 133원</b></div>
    <div class="cb"><span>공고 1건</span><div class="cb-b c" style="width:13.3%"></div><b>약 252원</b></div>
    <div class="cb"><span>가격</span><div class="cb-b p" style="width:100%"><b>1,900원 · 공고 1건 추가생성권</b></div></div></div>
    <div class="ledger"><div><b>5,391건</b><span>90일 LLM 호출 원장</span></div><div><b>99.3%</b><span>호출 성공률</span></div></div>
  </div>
  <div class="panel cost">
    <div class="fb2-k">원가는 어디에 쓰이나 — 작업별 비중</div>
    <div style="margin:auto 0"><div class="stk" style="height:96px"><div style="width:81%;background:var(--purple)">학습 질문 81%</div><div style="width:12%;background:#a79bfa">어필</div><div style="width:5%;background:#d6d0fb"></div><div style="width:2%;background:#ece9f1"></div></div>
    <div class="stk-l"><span><i style="background:var(--purple)"></i>학습 질문 생성 81%</span><span><i style="background:#a79bfa"></i>어필 포인트 약 12%</span><span><i style="background:#d6d0fb"></i>꼬리질문 보정 약 5%</span></div></div>
    <div class="ledger"><div><b>GLM-5</b><span>원가의 약 99% · 추론 모델</span></div><div><b>$32.77</b><span>단가 설정 호출 2,881건 합계</span></div></div>
    <div class="small-copy" style="margin-top:14px">하한값입니다 — 단가 미설정 커밋 판정 호출 2,349건을 넣으면 분석 1회 약 150원 추정</div>
  </div>
</div>''', source='관리자 콘솔 LLM 호출 원장 (90일, 단가가 설정된 호출) · 분석 346회 · 공고 182건 · 1 USD = 1,400원 · 막대는 가격 대비 비율'))

# --- 3.6 타임라인 (gantt) ---
d0, d1 = dt.date(2026, 6, 29), dt.date(2026, 11, 6)
def X(m, d): return (dt.date(2026, m, d) - d0).days / (d1 - d0).days * 100
lanes = [('엔진·품질', 70), ('제품·인프라', 250), ('마케팅·사업', 430)]
evs = [(0, 6, 29, '개발 착수', '06-25 피봇 승인'), (0, 9, 6, '평가 하네스 도입', ''), (0, 9, 9, '난이도·유형 분리', '← 09-07 한유일 멘토 (2일)'), (0, 10, 11, '실기업 기출 업로드', ''),
       (1, 8, 3, 'B2C 출시', '첫 운영 배포'), (1, 8, 23, '레포 범위 선택', '← 08-07 «연동하면 털리나» (16일)'), (1, 9, 16, '음성 모의면접', '운영 반영'), (1, 9, 22, '비동기 배포·Slack', '← 09-22 멘토링 (당일)'), (1, 11, 2, '결제 LIVE · 기출 RAG', '← 11-02 멘토링 (당일)'),
       (2, 8, 10, '유료 광고 시작', 'Meta · Google'), (2, 9, 3, '사업자등록', '도저랩스'), (2, 10, 15, '토스페이먼츠 계약', ''), (2, 11, 1, '특허 3건 출원', '')]
g = ['<div class="gantt">']
for m, lab in [(7, '7월'), (8, '8월'), (9, '9월'), (10, '10월'), (11, '11월')]:
    g.append(f'<div class="month" style="left:calc(220px + (100% - 300px) * {X(m,1)/100:.4f})">{lab}</div>')
for name, top in lanes:
    g.append(f'<div class="lane" style="top:{top}px"></div><div class="lane-name" style="top:{top+14}px">{name}</div>')
for li, m, d, t, c in evs:
    top = lanes[li][1] + 30
    cc = f'<div class="c">{c}</div>' if c else ''
    g.append(f'<div class="ev" style="left:calc(220px + (100% - 300px) * {X(m,d)/100:.4f});top:{top}px"><span class="d">{m:02d}-{d:02d}</span><div class="t">{t}</div>{cc}</div>')
g.append(f'<div class="mid" style="left:calc(220px + (100% - 300px) * {X(8,20)/100:.4f});top:40px;bottom:0"><span>★ 08-20 중간평가 · 피드백 19건</span></div></div>')
S.append(shell('Development', '피드백을 받은 날과 <span class="purple">운영에 반영한 날</span>이 가깝습니다', f'''
<div class="panel" style="padding:30px 40px 20px;flex:1;display:flex;flex-direction:column;min-height:0">{''.join(g)}</div>''', source='2026-06-29 ~ 11-04 · 운영 반영일은 운영 브랜치 배포 기준'))

LOOPS = [
      ('한유일 멘토 · 09-07', '«쉬운 질문이 사실 확인뿐»', '난이도와 유형이 1:1로 묶임 (114문항 중 예외 0)', '난이도를 근거 두께·추론 부담으로 분리 · 2일 만에 운영', '쉬운 질문 추론형 1/8 → 7/9'),
      ('사용자', '«실제 기출이 필요»', '공고·내 코드 기반 질문만 제공', '공개 출처 304개 기출 → pgvector RAG', '11-02 운영 반영'),
      ('멘토링 · 09-22', '«배포를 기다리지 말라»', '운영 배포 대기를 사람이 지켜봄', 'Step Functions 이관 + Slack 알림 · 당일', '배포 잡 429–488초 → 145–260초')]
LOOP_HTML = ''
for who, fb, a, b, c in LOOPS:
    LOOP_HTML += ('<div style="display:grid;grid-template-columns:280px 1fr;gap:24px;align-items:stretch"><div class="panel soft" style="padding:18px 22px;display:flex;flex-direction:column;justify-content:center">'
                  f'<div style="font-size:21px;font-weight:900;color:var(--purple-deep)">{who}</div><div class="small-copy" style="font-size:18px;color:var(--ink);font-weight:700;margin-top:4px">{fb}</div></div>'
                  + flow([('원인', a), ('수정', b), ('측정', c, 'accent')]) + '</div>')
S.append(shell('Development', '피드백을 받으면 <span class="purple">원인 → 수정 → 측정</span>까지 갑니다', f'''
<div style="display:flex;flex-direction:column;gap:18px">
  {LOOP_HTML}
</div>
<div class="callout" style="margin-top:auto">중간평가 심사의견 <strong>19건 중 18건 대응</strong> — 완료 5 · 부분 10 · 소명 3 · 미반영 1(#15 대학 B2B2C, 사유 기재) · 전체 표는 부록 A1</div>''', source='1/8 → 7/9: 단일 레포 1회, 저난도 문항 중 추론형 비율'))

S.append(shell('Development', '출시 후 <span class="purple">14주 연속</span>, 매주 운영에 배포했습니다', f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">
  {kpi('138회', '운영 배포 · 14주 연속 매주', '배포', 'soft', 'purple')}{kpi('14.3% → 1.7%', '배포 실패율', '안정성')}{kpi('2,890개', '자동 테스트 (중간평가 BE 488 → 2,000)', '테스트')}
</div>
<div style="display:grid;grid-template-columns:1.35fr .65fr;gap:26px;margin-top:26px;flex:1;min-height:0">
  <div class="panel" style="padding:22px 28px;display:flex;flex-direction:column">
    <div style="display:flex;justify-content:space-between"><div class="small-copy" style="font-weight:900;color:var(--ink)">주별 운영 배포 성공 횟수 (주 시작일)</div><div class="small-copy"><span style="color:#6c5ce7">■</span> FE  <span style="color:#a79bfa">■</span> BE</div></div>
    {bars(['8/3','8/10','8/17','8/24','8/31','9/7','9/14','9/21','9/28','10/5','10/12','10/19','10/26','11/2'], [[2,2],[6,4],[10,3],[3,4],[4,5],[4,3],[11,6],[2,3],[8,7],[5,5],[11,10],[1,3],[4,4],[4,4]], 1060, 330, stacked=['#6c5ce7', '#a79bfa'], label_size=15, val_size=18, vmax=24)}
  </div>
  <div class="panel" style="padding:28px 30px">{ul(['승격 게이트가 막은 운영 push <strong>13건</strong> · 운영 유출 <strong>0</strong>', '커밋 1,467개 중 중간평가 이후 <strong>919개 (63%)</strong>', '운영 승격 PR <strong>29 → 125</strong>', '중간평가 이후 운영 기능 <strong>50여 개 · 10개 영역</strong>'], 'sm')}</div>
</div>''', source='GitHub Actions prod 배포 성공 (2026-08-03 ~ 11-04) · 커밋: BE+FE 원격 기준 · 테스트: BE 2,000 · FE 807 · E2E 83'))

S.append(shell('Development', '현업은 «결정 이유»를 묻고, <span class="purple">DevFit도 그걸 묻습니다</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">
  <div class="panel soft" style="padding:30px 36px"><div class="quote">«중간이나 어려움 수준에서 지금 나오는 질문들은 충분히 괜찮아 보이긴 한 것 같아요.»</div><div class="quote-who">한유일 멘토 · 09-07 실사용 검증</div></div>
  <div class="panel" style="padding:30px 36px"><div class="quote">«왜 선택했는지나 왜 그 상황에서 그 선택이 최선이였는지 많이 물어봅니다.»</div><div class="quote-who">IT 기업 대표 · 10-26 서면 회신 → DevFit «결정 이유»·«트레이드오프» 질문 유형</div></div>
</div>
<div style="display:grid;grid-template-columns:1.3fr .7fr;gap:30px;margin-top:28px;flex:1;min-height:0">
  <div class="shot" style="padding:22px 26px;display:flex;align-items:center"><img src="assets/ceo_mail_body.png" alt="IT 기업 대표 서면 회신 본문" style="height:auto;object-fit:contain"></div>
  <div class="panel red-soft" style="padding:28px 32px;display:flex;flex-direction:column;justify-content:center">
    <div class="kpi-k">같은 대표의 반론</div><div style="font-size:26px;font-weight:900;line-height:1.45">«github 링크를 클로드코드에게 넘기면 된다»</div>
    <div class="body-copy" style="margin-top:14px">→ p3 실험으로 답했습니다 · 근거 실존 <strong>0/18</strong> vs <strong>28/28</strong></div></div>
</div>''', source='서면 회신 원문 캡처 — 이름·회사·메일 주소는 잘라냄'))

S.append(shell('Development', '가장 큰 이탈을 <span class="red">숫자로 찾았습니다</span>', f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">
  {kpi('약 0.4%', '방문 2.2만 명 → 가입 · 가장 큰 이탈', '퍼널', 'red-soft', 'red')}
  {kpi('약 10배', 'Instagram 인앱 유입 가입 전환 0.10~0.15%<br>vs 그 외 유입 1.2~1.5%', '원인 후보')}
  {kpi('12.3', '광고 중단 기간(11/1–4) 세션 1,000개당 가입<br>9~10월 2.2~3.6', '대조')}
</div>
<div style="display:grid;grid-template-columns:1.2fr .8fr;gap:26px;margin-top:26px;flex:1;min-height:0">
  <div class="panel" style="padding:22px 30px;display:flex;flex-direction:column"><div class="small-copy" style="font-weight:900;color:var(--ink)">세션 1,000개당 가입 수 (괄호: Instagram 인앱 비중)</div>
    {bars(['8월 (12%)', '9월 (91%)', '10월 (86%)', '11/1–4 (광고 중단)'], [15.0, 3.6, 2.2, 12.3], 940, 330, colors=['#a79bfa', '#f22f46', '#f22f46', '#a79bfa'], fmt='{:.1f}', vmax=18, label_size=17, val_size=24)}</div>
  <div class="panel" style="padding:28px 30px">{ul(['세션당 활성 시간: 8월 2.3분 → 9월 12초', '인앱 웹뷰에는 GitHub 로그인 세션이 없어 OAuth에서 이탈하는 것으로 추정'], 'sm')}</div>
</div>''', source='방문: Microsoft Clarity (2026-08-01 ~ 11-04, 봇 제외) · 가입: 관리자 DB · 월 비교는 통제 실험이 아님'))

# ================= 4. Effect =================
S.append(divider('04 · Effect', 'Effect', '지금까지 만든 효과 4.1~4.3 → 앞으로의 효과 4.4'))

S.append(shell('Effect', '가입한 사람의 <span class="purple">76%</span>가 실제 공고로 준비를 시작했습니다', f'''
<div style="display:grid;grid-template-columns:.8fr 1.2fr;gap:30px;flex:1;min-height:0">
  <div style="display:flex;flex-direction:column;gap:20px">
    {kpi('60 / 79명', '외부 가입자 중 실제 공고로 준비 시작 (76%)<br>외부 공고 83건 · 내부 4명 제외', '활성화', 'soft', 'purple', 'flex:1.2')}
    {kpi('최대 126명', '공고를 직접 등록해 본 사람 (회원 64 + 비회원 62)', '첫 행동', '', '', 'flex:1')}
    {kpi('30%', '가입이 밤 9시 ~ 새벽 1시 — 취준생은 밤에 준비합니다', '가입 시간대', '', '', 'flex:1')}
  </div>
  <div class="panel" style="padding:26px 30px;display:flex;flex-direction:column">
    <div class="section-line"><span class="num">1</span><span>누적 회원 8/7 7명 → 11/4 83명</span></div>
    <div style="flex:1;display:flex;align-items:center">{line(['8/7','8/16','8/23','8/30','9/6','9/13','9/20','9/27','10/4','10/11','10/18','10/25','11/1','11/4'], [7,9,11,15,23,28,35,40,58,63,70,71,82,83], 1000, 560)}</div>
    <div class="small-copy">관리자 DB 성장 차트 판독값 ±1명 · 누적 83명은 내부 4명 포함</div>
  </div>
</div>''', source='관리자 DB (2026-11-05 00:38 조회, 내부 계정 제외) · 🔄 제출 직전 11/11 재조회'))

S.append(shell('Effect', '지표를 추측하지 않으려고 <span class="purple">관리자 콘솔</span>을 직접 만들었습니다', f'''
<div style="display:grid;grid-template-columns:300px 1fr;gap:30px;flex:1;min-height:0">
  <div class="shot" style="padding:10px"><img src="assets/admin_menu.png" alt="관리자 콘솔 메뉴" style="object-fit:contain"></div>
  <div style="display:flex;flex-direction:column;gap:26px;min-height:0">
    <div class="shot" style="padding:12px 14px"><img src="assets/admin_llm_usage_90d_20261105-0043.png" alt="LLM 사용량 카드" style="height:auto;object-fit:contain"></div>
    <div class="body-copy" style="font-size:26px;color:var(--ink);font-weight:800">앞 장의 숫자는 모두 이 콘솔에서 나왔습니다</div>
    {table(['기능', '하는 일'], [['B2C 대시보드 · 회원 관리', '가입 → 공고 → 분석 → 답변 퍼널, 내부 계정 제외 집계'], ['사용자 행동 분석', '텍스트·음성 모의면접 사용 흐름'], ['LLM 사용량 · 모델 단가', '호출별 토큰·원가 원장 — 90일 5,391건, 성공률 99.3%'], ['캐싱 공고 · 면접 기출', '기업 채용사이트 공고 캐시와 기출 데이터 운영']], 'sm left plain')}
  </div>
</div>''', source='관리자 콘솔 캡처 (2026-11-04 ~ 05) · 계정 정보 영역은 잘라냄'))

def docimg(src, alt, ratio, cap=''):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="docimg" style="aspect-ratio:{ratio}"><img src="assets/{src}" alt="{alt}">{c}</div>'

import os as _os
if _os.path.exists(_os.path.join(_os.path.dirname(OUT), 'assets', 'cert-biz.png')):
    import subprocess as _sp
    _o = _sp.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', _os.path.join(_os.path.dirname(OUT), 'assets', 'cert-biz.png')], capture_output=True, text=True).stdout
    _w = int(_o.split('pixelWidth:')[1].split()[0]); _h = int(_o.split('pixelHeight:')[1].split()[0])
    BIZ_RATIO = f'{_w}/{_h}'; BIZ = docimg('cert-biz.png', '사업자등록증', BIZ_RATIO, '사업자등록증 · 2026-09-02')
else:
    BIZ_RATIO = '210/297'; BIZ = '<div class="bizslot"><b>사업자등록증</b><span>원본 넣을 자리<br>assets/cert-biz.png</span></div>'
def docfig(src, alt, cap, h):
    if not src:
        return f'<div class="docfig"><div class="bizslot" style="height:{h}px;width:{round(h*0.707)}px"><b>사업자등록증</b><span>원본 넣을 자리</span></div><div class="dcap">{cap}</div></div>'
    return f'<div class="docfig"><img src="assets/{src}" alt="{alt}" style="height:{h}px"><div class="dcap">{cap}</div></div>'
BIZ_SRC = 'cert-biz.png' if _os.path.exists(_os.path.join(_os.path.dirname(OUT), 'assets', 'cert-biz.png')) else ''
def stackdoc(src, alt, cap, left, top, rot, z):
    return f'<div class="sd" style="left:{left}px;top:{top}px;transform:rotate({rot}deg);z-index:{z}"><img src="assets/{src}" alt="{alt}"><span class="tag">{cap}</span></div>'
pat = [('patent-a.png', '10-2026-0214808', '선별'), ('patent-b.png', '10-2026-0214809', '생성'), ('patent-c.png', '10-2026-0214811', '음성')]
pimgs = ''.join(docimg(f, n + ' 출원번호통지서', '634/390', k + ' · ' + n) for f, n, k in pat)
S.append(shell('Effect', '돈을 받을 수 있는 <span class="purple">사업자</span>와, 기술을 지킬 <span class="purple">특허</span>를 갖췄습니다', f'''
<div class="ev">
  <div class="ev-a">
    {stackdoc(BIZ_SRC, '사업자등록증', '① 사업자등록증', 18, 48, -2.2, 1)}
    {stackdoc('cert-job.png', '직업정보제공사업 신고확인증', '② 직업정보제공사업 신고확인증', 268, 16, 0, 2)}
    {stackdoc('cert-mail.png', '통신판매업 신고증', '③ 통신판매업 신고증', 518, 48, 2.2, 3)}
  </div>
  <div class="ev-b">
    {''.join(f"""<div class="sd p" style="left:{i*30}px;top:{16+i*196}px;z-index:{i+1}"><img src="assets/{f}" alt="{n} 출원번호통지서"><span class="tag">특허 출원 · {k} · {n}</span></div>""" for i, (f, n, k) in enumerate(pat))}
  </div>
</div>''', source='증빙 원본 스캔·캡처 그대로 (자르거나 가리지 않음) · 특허는 출원 단계'))

S.append(shell('Effect', '공고 10만 건에 지원 260만 건, <span class="purple">검증 수단</span>이 모자랍니다', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px">
  {kpi('약 10만 건', '국내 개발자 채용공고 (2025 상반기)', '공고', '', '')}
  {kpi('약 260만 건', '같은 기간 지원 · 신입 비중 공고 0.8% vs 지원 29.5%', '지원', 'soft', 'purple')}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr .9fr;gap:26px;margin-top:26px;flex:1;min-height:0">
  <div class="panel" style="padding:28px 32px"><div class="section-line"><span class="num">1</span><span>B2C</span></div><div class="body-copy">공고마다 준비하는 개발 취준생 <strong>약 2~4만 명</strong> (내부 추정)</div><div class="small-copy" style="margin-top:10px">일반기업 취업 준비 청년 약 20만 명 중</div></div>
  <div class="panel b2b" style="padding:28px 32px"><div class="section-line"><span class="num" style="background:#005ce6">2</span><span>B2B</span></div><div class="body-copy">면접관이 빠뜨린 확인 관점을 알려 주는 <strong>커버리지 어시스턴트</strong> (콘솔 구현 완료)</div><div class="small-copy" style="margin-top:10px">정답지가 아니라 «확인할 항목» — 질문 유출 우려(중간평가 #17) 대응</div></div>
  <div class="panel dark" style="padding:28px 32px;display:flex;flex-direction:column;justify-content:center"><div class="kpi-k" style="color:#bdb4ff">국내 상향식 (B2B)</div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid #3a3540;padding:10px 0"><span style="font-size:22px">SAM</span><span style="font-size:44px;font-weight:900">약 104억</span></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0"><span style="font-size:22px">3년 SOM</span><span style="font-size:44px;font-weight:900;color:#bdb4ff">약 3억 원대</span></div></div>
</div>''', source='사람인·점핏 2025 상반기 리포트(언론 보도 경유) · 국가데이터처 청년층 부가조사(2026-05) · SAM/SOM: 내부 가격 앵커 기준 상향식 추정'))

S.append(shell('Effect', '조각 세 개가 운영 중이고, <span class="purple">하나의 채용 플랫폼</span>으로 잇습니다', f'''
<div style="display:grid;grid-template-columns:1.05fr .95fr;gap:30px;flex:1;min-height:0">
  <div style="display:flex;flex-direction:column;gap:20px;min-height:0">
    <div class="shot" style="flex:1;min-height:0"><img src="assets/vision-diagram.png" alt="DevFit Platform 비전" style="object-fit:contain"></div>
    <div class="chip-row">{badge('① B2C 준비 · 결제 LIVE', 'green')}{badge('② B2B 면접관 콘솔', 'green')}{badge('③ 공고 29곳 수집 · 지원 여정 트래커', 'green')}</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:22px">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{kpi('275명', 'B2C 6개월 가입 목표 (추정)<br>범위 135~382 · 현 광고비 전제', 'B2C 목표', 'soft', 'purple')}{kpi('25%', '가입자 답변률 목표', 'B2C 목표')}</div>
    <div class="panel" style="padding:30px 34px;flex:1"><div class="section-line"><span class="num" style="background:#005ce6">B</span><span>B2B 로드맵 · 현재 콘솔 완성, 고객 0</span></div>
      {steps([('2026-11', '회고형 파일럿 2곳'), ('2027-01~02', '실전 파일럿 2~3곳'), ('2027-03', '첫 유료 1곳')])}
      <div class="small-copy" style="margin-top:20px;text-align:center">재는 것: 면접관 질문 채택률</div></div>
  </div>
</div>''', source='275명 = 최근 주 7.4명 × 26주 + 현재 83명 · 비전 그림은 중간발표와 동일'))

# ================= 마무리 =================
S.append(raw('dark-slide', f'''<div class="dark-grid"></div><div class="slide-shell" style="padding:0">
<div style="position:absolute;inset:0;display:grid;grid-template-columns:58% 42%">
  <div style="padding:0 0 0 118px;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2">
    <div style="font-size:28px;color:#9c96a3;font-weight:700;margin-bottom:30px">05 · 마무리</div>
    <h1 style="margin:0;color:#fff;font-size:66px;font-weight:900;line-height:1.35;letter-spacing:-.055em">AI가 만든 면접 질문을,<br><span style="color:#b9b0ff">지원자 본인의 코드</span>로 증명하고<br>숫자로 검증합니다</h1>
    <div style="display:flex;align-items:center;gap:22px;margin-top:50px"><img src="assets/icon.svg" alt="" style="width:66px;height:66px;border-radius:16px"><div style="font-size:50px;font-weight:900;letter-spacing:-.055em;color:#fff">Dev<span style="color:#b9b0ff">Fit</span></div></div>
    <div style="margin-top:28px;color:#d9d5dd;font-size:25px;font-weight:700">B2C devfit.app · B2B enterprise.devfit.app</div>
    
    <div style="margin-top:22px;color:#78717d;font-size:19px">팀 Dozer · 박천웅, 김건우, 노재원</div>
  </div>
  <div style="position:relative;overflow:hidden">
    <div class="shot" style="position:absolute;width:700px;height:420px;right:-80px;top:120px;transform:rotate(2deg);opacity:.92"><img src="assets/q-list.jpg" alt=""></div>
    <div class="shot" style="position:absolute;width:660px;height:394px;left:10px;bottom:150px;transform:rotate(-2deg)"><img src="assets/q3.jpg" alt=""></div>
  </div>
</div>
<div style="position:absolute;left:118px;right:118px;bottom:26px;color:#6d6774;font-size:13px;line-height:1.5;z-index:3">{ACK}<br>{ACK_EN}</div>
<div class="folio" style="left:auto;right:88px;color:#6d6774"></div></div>''', '마무리'))

S.append(raw('', '''<div class="slide-shell"><div class="slide-content" style="margin:0;align-items:center;justify-content:center">
<img src="assets/Dozer_일러스트.png" alt="팀 Dozer" style="width:980px;max-width:74%;display:block;margin-top:-40px">
<div style="font-size:48px;font-weight:900;letter-spacing:-.045em;margin-top:-150px">감사합니다</div>
<div class="small-copy" style="font-size:22px;margin-top:14px">팀 Dozer, 박천웅, 김건우, 노재원 · Q&amp;A</div></div><div class="folio"></div></div>''', '감사합니다'))

# ================= 부록 =================
apx = [('A1', '중간평가 심사의견 19건 반영표'), ('A2', '범용 AI 비교 실험 · 유사 서비스'), ('A3', '평가 하네스 상세'), ('A4', '측정 도구별 수치 차이'), ('A5', '유료 광고 집행과 효율'), ('A6', '보안'), ('A7', '원가와 가격'), ('A8', '기출 데이터 수집'), ('A9', '특허 3건'), ('A10', '팀 역할 · 품질 보증')]
qs = ['멘토·심사 의견을 어떻게 반영했나', '범용 AI랑 뭐가 다른가', '품질을 어떻게 믿나', 'GA는 235명인데 왜 2.2만인가', '마케팅 효율은', '내 코드 털리는 거 아닌가', '돈은 어떻게 버나', '크롤링 문제없나', '특허는 뭘 보호하나', '누가 뭘 했나 · 리뷰는']
S.append(shell('Appendix', '부록 — Q&amp;A에서 <span class="purple">쪽번호로</span> 바로 엽니다', table(['쪽', '장표', '예상 질문'], [[f'<b style="color:var(--purple)">{a}</b>', b, q] for (a, b), q in zip(apx, qs)], 'left plain')))

MID19 = [("1", "늦은 피봇을 범위 축소로 만회(긍정)", "유지", "B2C 주축, B2B는 MVP. 운영 승격 PR 29 → 125"),
 ("2", "기능 확장보다 질문 품질과 기업 파일럿", "부분", "8축 평가 → 결함 31건 수정 → 난이도 분리 → v11~v13. 저난도 추론형 1/8 → 7/9. 파일럿 0건"),
 ("3", "커밋·diff 연결과 무근거 폐기(긍정)", "강화", "근거 대조·사유 코드 노출(10-19). 출처 353/353, 품질 필터 30일 84건"),
 ("4", "라벨·문항분석으로 정확성·변별도 검증", "부분", "3-state 라벨 UI 복구(09-08). 근거 특정성 81.9%. 변별도 실측 0건(표본 부족)"),
 ("5", "질문 품질 자동 검증", "완료", "평가 하네스(09-06): 8축 루브릭 · 결정적 지표 13개 · 회귀 게이트"),
 ("6", "설계·본인 작업 검증 등 의도별 질문", "완료", "의도 7유형, 난이도 분리, 본인 기여 필터(1.0 / 0.70 / 제외). 09-09 운영"),
 ("7", "코딩 외 전인적 역량 평가", "부분·소명", "자동 합불 금지선 → «준비» 지원: 음성 모의면접, 자소서·포트폴리오 작업실, 블라인드 평가"),
 ("8", "기업 파일럿으로 채택률·절감 확인", "부분·착수", "기업 대표 서면 회신 1건, 리드 43사, 로드맵. 수치·LOI 없음"),
 ("9", "시장 분석 세밀화, 포커스 결정", "부분", "출처 등급제(인용 금지 6건 제거), B2C 신입·주니어 포커스"),
 ("10", "기존 취업 사이트 대비 우위", "부분", "«공고 × 내 실제 코드». 근거 실존 28/28 vs 0/18"),
 ("11", "경쟁사 직접 사용", "부분", "직접 9 · 인접 43 · 모바일 12종 캡처. 유료 전체 플로우 기록 없음"),
 ("12", "B2C·B2B 동시 공략은 욕심", "소명", "투입은 B2C 집중, B2B는 같은 엔진 MVP"),
 ("13", "일정상 B2C 집중", "완료", "B2C 출시 → 음성 → 단건 결제 LIVE(11-02)"),
 ("14", "중견기업 타겟", "부분", "리드 규모 32~618명. 발송 전 미검증"),
 ("15", "대학 취업지원실 B2B2C", "미반영", "박람회 현장 마케팅만. 대학 예산 주기와 연수 종료 시점 불일치"),
 ("16", "시즌성 때문에 수익모델 재검토", "부분", "공고 단위 단건 1,900원 추가 · LIVE. 매출 0"),
 ("17", "질문 유출 플랫폼은 기업이 싫어함", "소명", "본인 코드 기반 · 지원서별 생성. B2B «커버리지 어시스턴트» 재정의"),
 ("18", "개인정보 보호조치", "부분", "토큰 AES-256-GCM, 세션 해시, numeric id 신원, 증분 동의, 블라인드 평가"),
 ("19", "개발·운영 환경 통합(비용)", "소명", "결제 TEST 격리 필요로 분리 유지. 원가의 94%가 LLM")]
BC = {'완료': 'green', '강화': 'green', '유지': 'neutral', '부분': '', '부분·소명': 'amber', '부분·착수': '', '소명': 'amber', '미반영': 'red'}
S.append(shell('Appendix · A1', '중간평가 심사의견 19건 — 완료 5 · 부분 10 · 소명 3 · 미반영 1', table(['#', '심사의견', '구분', '조치'], [[a, b, badge(c, BC[c]), d] for a, b, c, d in MID19], 'xs left plain a1'), source='반영일·근거 커밋은 운영 브랜치 포함 여부 확인'))

S.append(shell('Appendix · A2', '레포를 읽게 하면 범용 에이전트도 찾습니다 — <span class="purple">차이는 절차</span>', f'''
{table(['군', 'n', 'SHA 실존', '파일 실존', '근거 3종 모두 실존', '본인 커밋'], [['DevFit (운영 prod)', '28', '28 (100%)', '28 (100%)', '28 (100%)', '28 (100%)'], ['Claude Code + 레포 clone', '32', '32 (100%)', '32 (100%)', '30 (94%)', '32 (100%)'], ['범용 AI, 레포 링크만', '18', '0 (0%)', '0 (0%)', '0 (0%)', '0 (0%)']], 'sm plain')}
<div class="body-copy" style="margin:16px 0">DevFit은 레포를 읽고 대조하는 절차를 사용자가 프롬프트를 짜지 않아도 서버가 매번 강제하고, 공고 단위 흐름과 본인 커밋 필터를 붙였습니다.</div>
{table(['서비스', '입력', '본인 코드·커밋 분석', '질문 근거 표시', '특정 공고 맞춤', '음성', '한국어'], [['DevFit', '공고 URL/이미지 + GitHub', '본인 커밋·PR만', '질문마다 diff + 원문 링크', '플랫폼 5 + 기업 24곳', 'O', 'O'], ['Greenroom (해외)', 'GitHub 레포 · 목표 직무', 'O (Pro)', '확인 안 됨', '확인 안 됨', 'O', '확인 안 됨'], ['Final Round AI (해외)', '이력서 + JD', 'X', '–', 'O', 'O', '명시 없음'], ['사람인 AI 모의면접', '이력서 + 사람인 공고', 'X', '–', '사람인 공고 한정', 'O', 'O'], ['꼬꼬면', '이력서 · 포트폴리오', '언급 없음', '문항 은행 기반', '–', 'O', 'O'], ['범용 AI', '사용자 지시', '연동 시 열람 가능', '사용자가 검증', '사용자가 지시', '일부', 'O']], 'xs')}''', source='실험: 2026-11-05 파일럿, 공개 레포 4개 · 군별 1회 · 결정론 채점 · 기능 비교: 각 서비스 공개 페이지(2026-11-05 확인)'))

S.append(shell('Appendix · A3', 'LLM 심판 점수를 <span class="purple">그대로 믿지 않습니다</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;flex:1;min-height:0">
  <div class="panel" style="padding:30px 36px"><div class="section-line"><span class="num">1</span><span>평가 하네스 구성</span></div>{ul(['운영 파이프라인을 직접 호출해 질문 생성', '8축 루브릭 (LLM 심판)', '결정적 지표 13개 — 출처 연결 · 공고별 중복 · 식별자 실존 등', '회귀 게이트 — 질문 로직 버전(v1 → v13)마다 측정'])}</div>
  <div class="panel" style="padding:30px 36px"><div class="section-line"><span class="num">2</span><span>심판을 믿지 않는 근거</span></div>{table(['측정', '값', 'n'], [['심판 2종 간 문항별 점수 차', '17.8점', '91'], ['같은 심판 재채점 차', '12.2점', '24'], ['LLM 심판 vs 사람', '사람보다 약 1점 후함', '18'], ['근거 특정성 (우연 25%)', '81.9%', '177'], ['질문 출처 연결', '353/353', '전수']], 'sm')}</div>
</div>'''))

S.append(shell('Appendix · A4', '측정 도구마다 숫자가 다른 이유 — <span class="purple">정본은 관리자 DB</span>', f'''
<div style="display:grid;grid-template-columns:1.25fr .75fr;gap:30px;flex:1;min-height:0">
  <div class="shot"><img src="assets/14_measurement_gap.png" alt="측정 도구별 수치 차이" style="object-fit:contain"></div>
  <div style="display:flex;flex-direction:column;gap:20px">{kpi('22,360명', 'Microsoft Clarity 방문자 · 동의와 무관하게 수집, 봇 제외', 'Clarity')}{kpi('235명', 'GA4 사용자 · 쿠키 동의한 사람만 → 하한', 'GA4', 'red-soft', 'red')}{kpi('83명', '관리자 DB 가입 · 정본 (내부 4명 포함)', '관리자 DB', 'soft', 'purple')}</div>
</div>''', source='기간 2026-08-01 ~ 11-04 · 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4'))

S.append(shell('Appendix · A5', '유료 광고 ₩347.5만 — 랜딩은 쌌고 <span class="red">가입은 비쌌습니다</span>', f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{kpi('₩347.5만', 'Meta ₩233.8만 + Google ₩113.7만', '유료 광고 합계')}{kpi('최소 ₩4.2만', '가입 1명당 광고비 (하한, 상한 추정 ₩12.9만)', '가입 단가', 'red-soft', 'red')}{kpi('브랜드 검색뿐', 'Search Console 클릭 37건, 대부분 «devfit»', '자연 검색')}</div>
<div style="margin-top:26px">{table(['지표', 'Meta', 'Google'], [['지출', '₩2,338,208', '₩1,136,972'], ['노출', '666,197', '116,041'], ['클릭', '21,318 (링크 클릭)', '2,018'], ['클릭 1회', '₩110', '₩563'], ['랜딩 1회', '₩151 (Meta 랜딩 조회)', '—']], 'sm plain')}</div>''', source='Meta 광고 관리자(8/1~11/3) · Google Ads(8/24~11/3) · ₩4.2만 = 광고비 ÷ 전체 가입 83명(전원 광고 유입 가정)'))

S.append(shell('Appendix · A6', '최소 권한으로 연결하고, <span class="purple">토큰은 암호화</span>합니다', table(['우려', '조치'], [
 ['«GitHub 연동하면 내 코드 털리나»', '기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의'],
 ['분석 범위', '분석할 레포를 사용자가 직접 선택 (08-07 피드백 → 08-23 반영)'],
 ['토큰 유출', 'GitHub access token AES-256-GCM 암호화 저장'],
 ['세션 탈취', '세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능 · HttpOnly 쿠키'],
 ['계정 선점', 'GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)'],
 ['공고 수집 경로 악용 (SSRF)', '홉마다 허용 목록을 다시 검사하는 SafeFetcher · 응답 8MB 상한'],
 ['B2B 지원자 정보', '블라인드 평가 · 지원 시 동의 2건 필수']], 'sm left plain')))

S.append(shell('Appendix · A7', '분석 1회 약 130원대, 단건 <span class="purple">1,900원</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px">{kpi('약 130원대', '분석 1회 LLM 원가 ≈ $0.095 (단가 설정 호출 기준) · 미설정 호출 포함 추정 약 150원', '원가', 'soft', 'purple')}{kpi('94%', '전체 원가 중 LLM 비중 — 개발 DB·서버는 정지 운영', '원가 구조')}</div>
<div style="margin-top:26px">{table(['상품', '가격', '상태'], [['Free', '무료 (사용 한도 있음)', '운영 중'], ['추가생성권 (공고 단위 단건)', '1,900원', '토스페이먼츠 LIVE (2026-11-02)'], ['Plus', '월 7,900원', '정기결제 심사 중 · 출시 기념 3개월 무료 개방'], ['B2B', '파일럿 후 결정', '콘솔 구현 완료 · 고객 0']], 'sm left plain')}</div>
<div class="callout" style="margin-top:auto">채용 시즌에만 사는 구조에 맞춰 월 구독 외에 <strong>공고 단위 단건 상품</strong>을 추가했습니다 (중간평가 #16)</div>''', source='관리자 콘솔 LLM 호출 원장(2026-08-30~) · 1 USD = 1,400원'))

S.append(shell('Appendix · A8', '기출은 <span class="purple">공개 출처</span>만, 출처 URL과 함께 보존합니다', f'''
<div class="panel apx-lg" style="padding:44px 50px">{ul(['수집 대상: 공개된 면접 후기·기출 출처 304개', '출처 URL을 질문과 함께 보존해 원문을 확인할 수 있게 함', '공개 정보 위주 수집 — 비공개·로그인이 필요한 자료는 수집하지 않음', '원문을 그대로 노출하지 않고, 지원자 코드 질문의 맥락 보강에 사용'])}</div>'''))

S.append(shell('Appendix · A9', '특허 3건 출원 — <span class="purple">선별 · 생성 · 음성</span>', f'''
{table(['출원번호', '발명의 명칭', '보호하는 것 (요지)', '관련 장표'], [
 ['<span class="patent">10-2026-0214808</span>', '코드 저장소 기반 면접 질문 선별 방법 및 시스템', '본인 기여 커밋을 골라 가중(본인 1.0 · 공동 0.70 · 타인 제외)하고 질문 대상 지점을 선별', 'p6 · p12'],
 ['<span class="patent">10-2026-0214809</span>', '코드 저장소 기반 면접 질문 생성 방법 및 시스템', '근거 코드 묶음에서 질문을 만들고, 질문 속 식별자를 코드와 대조해 유지·폐기·재질의하는 게이트', 'p5 · p11'],
 ['<span class="patent">10-2026-0214811</span>', '음성 대화 기반 면접 답변 평가 방법 및 시스템', '음성 답변을 받아 적고 답변에 기반한 꼬리질문으로 되묻는 모의면접', 'p15']], 'left plain a9')}
<div class="body-copy" style="margin-top:20px">출원일 2026-11-01 · 출원인 김건우 · 발명자 김건우, 박천웅, 노재원</div>'''))

team = [('박천웅', '팀장 · DevSecOps &amp; Full Stack', '인증·보안, AWS 인프라·CI/CD·운영 배포, FE·BE 통합, 결제·사업자 행정', 'team-park-cheonwoong.jpg'),
        ('김건우', 'PM &amp; Frontend', '문제 정의·제품 방향·BM, Next.js 프론트엔드(B2C·B2B·관리자 콘솔), 마케팅·유입 계측', 'team-kim-gunwoo.jpg'),
        ('노재원', 'Backend · Core Logic &amp; AI', 'GitHub 커밋 선별 알고리즘, 근거 묶음·질문 생성 핵심 로직, Spring Boot 백엔드', 'team-noh-jaewon.jpg')]
tc = ''.join(f'<div class="panel" style="padding:40px 32px;display:flex;gap:26px;align-items:center;min-height:300px"><img src="assets/{p}" alt="{n}" style="width:140px;height:140px;border-radius:50%;object-fit:cover"><div><div style="font-size:30px;font-weight:900">{n}</div><div class="badge" style="margin-top:8px">{r}</div><div class="small-copy" style="margin-top:14px;font-size:20px">{d}</div></div></div>' for n, r, d, p in team)
S.append(shell('Appendix · A10', '세 명이 나눠 맡고, <span class="purple">게이트로 품질</span>을 지켰습니다', f'''
<div style="display:flex;flex-direction:column;height:100%"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;flex:1.3">{tc}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:28px;flex:1">{kpi('2,890개', 'CI 자동 테스트 (BE 2,000 · FE 807 · E2E 83)', '테스트')}{kpi('13건 · 유출 0', 'staging → prod 승격 게이트가 막은 운영 push', '승격 게이트', 'soft', 'purple')}{kpi('72%', 'PR 본문에 검증 내역을 적은 비율', 'PR 기록')}</div></div>'''))

html = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#121016"><title>DevFit 최종발표 — Team Dozer</title>
<style>{CSS}{EXTRA}</style></head><body>
<noscript><style>.slide:first-of-type{{display:block}}</style></noscript>
<div id="progress"></div><main id="stage" aria-live="polite">
{chr(10).join(S)}
</main>
<nav id="hud" aria-label="슬라이드 탐색"><button id="prev" type="button" aria-label="이전 슬라이드">‹</button><span id="counter">1 / 1</span><button id="next" type="button" aria-label="다음 슬라이드">›</button><button id="fullscreen" type="button" aria-label="전체 화면">⛶</button></nav>
{JS}
</body></html>'''
open(OUT, 'w', encoding='utf8').write(html)
print('slides', order[0])
