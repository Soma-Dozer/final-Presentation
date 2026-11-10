# -*- coding: utf-8 -*-
# 2부 — Development (5파트 + 수행과정) + 부록 A1·A6·A7·A8·A10·A12·A13·A14
# 담당: ppt-dev · 공용 헬퍼/CSS는 core.py (ppt-start 관리) — 고칠 일이 있으면 ppt-start에 요청
# 장표 추가: S.append(shell(...)) 다음 줄에 S.note('''발표자 노트''') · 부록은 APX.append(shell('Appendix · A<n>', ...))
# 구성 (2026-11-06 사용자 지시): ① 질문 생성 로직(하네스) ② 기출 ③ 공고 캐싱 ④ 모의면접 ⑤ 그 외 → 수행과정
# 아이템마다 «개요 장들 → 발전과정 장들(1차·2차·3차)» 순서 (11-06 사용자 지시, 작년 우수팀 덱 Dev 구성 참고). 발전과정 장 안은 «문제 → 해결 → 결과». 수치는 origin/prod(d84cb1c, 11-06) 코드와 last-dance/collect 근거로 대조함
# 이전 단일본: _legacy/s2_dev.before-5part.py
from core import *

S = Slides()    # 본편 — 이 파일 순서 그대로 들어간다
APX = Slides()  # 부록 — A번호 순으로 자동 정렬
PARK = Slides()  # 보류 — 덱에 안 들어감 (11-06 사용자: 지표 최신화 전까지 빼 둠)
CSS = r"""
.dv-wf{display:grid;margin:auto 0;align-content:center;align-items:stretch;max-width:1500px;width:100%;align-self:center}
.dv-wf .n{position:relative;min-width:0;min-height:190px;background:#fff;border:2px solid #ece9f1;border-radius:22px;padding:24px 22px 20px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:7px}
.dv-wf .n.on{border-color:var(--purple);background:var(--purple-pale)}
.dv-wf .n.dim{background:transparent;border-style:dashed;opacity:.6}
.dv-wf .n .ic{color:var(--purple);margin-bottom:2px}
.dv-wf .n .no{position:absolute;top:14px;left:16px;width:28px;height:28px;border-radius:50%;background:var(--purple-pale);color:var(--purple);font-size:15px;font-weight:900;display:flex;align-items:center;justify-content:center}
.dv-wf .n.on .no{background:var(--purple);color:#fff}
.dv-wf .n b{font-size:25px;font-weight:900;letter-spacing:-.04em;line-height:1.25}
.dv-wf .n span{font-size:17px;font-weight:700;color:var(--muted);line-height:1.45;word-break:keep-all}
.dv-wf .n em{font-style:normal;font-size:15px;font-weight:900;color:var(--purple);background:#fff;border:1.5px solid var(--purple-soft);border-radius:99px;padding:4px 12px;margin-top:4px;white-space:nowrap}
.dv-wf .n em.llm{background:var(--purple);color:#fff;border-color:var(--purple)}
.dv-wf .loop{border:2px dashed var(--purple-soft);border-radius:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:var(--purple);text-align:center;padding:20px}
.dv-wf .loop b{font-size:32px;line-height:1}.dv-wf .loop span{font-size:18px;font-weight:900;word-break:keep-all}.dv-wf .loop small{font-size:15px;font-weight:700;color:var(--muted)}
.dv-wf .a{display:flex;align-items:center;justify-content:center;color:var(--purple);font-size:28px;font-weight:900}
.dv-out{display:flex;flex-direction:column;gap:8px;width:100%;margin-top:6px}
.dv-out i{font-style:normal;border-radius:12px;padding:8px 6px;font-size:17px;font-weight:900}
.dv-out .k{background:#e7f6ee;color:#1d8a52}.dv-out .q{background:#fff4dc;color:#a36a00}.dv-out .d{background:#fdeaec;color:#c4283a}
.dv-cards{display:grid;gap:26px;flex:1;min-height:0;margin-top:8px}
.dv-card{background:#f3f1f6;border-radius:26px;padding:30px 30px 26px;display:flex;flex-direction:column;gap:14px;min-width:0}
.dv-card h3{margin:0;font-size:27px;font-weight:900;letter-spacing:-.04em;line-height:1.3;word-break:keep-all}
.dv-card h3 small{display:block;font-size:17px;color:var(--purple);font-weight:900;margin-bottom:6px;letter-spacing:0}
.dv-card p{margin:0;font-size:19px;line-height:1.5;font-weight:600;color:#4a4552;word-break:keep-all}
.dv-card p b{color:var(--ink);font-weight:900;margin-right:6px}
.dv-card .r{margin-top:auto;background:#fff;border-radius:18px;padding:16px 20px;font-size:32px;font-weight:900;color:var(--purple);letter-spacing:-.045em;line-height:1.15}
.dv-card .r small{display:block;font-size:15px;color:var(--muted);font-weight:700;margin-top:6px;letter-spacing:0;line-height:1.4}
.dv-card.on{background:var(--purple-pale)}
.dv-vs{display:flex;align-items:center;justify-content:center;gap:56px;margin:auto 0}
.dv-vs .v{text-align:center}
.dv-vs .v b{display:block;font-size:118px;font-weight:900;letter-spacing:-.06em;line-height:1}
.dv-vs .v.before b{color:#b9b3c0}
.dv-vs .v.after b{color:var(--purple)}
.dv-vs .v span{display:block;font-size:22px;font-weight:800;color:var(--muted);margin-top:16px;word-break:keep-all}
.dv-vs .arr{font-size:72px;color:var(--purple);font-weight:900}
.dv-q{background:var(--purple-pale);border-radius:22px;padding:22px 32px;font-size:25px;font-weight:800;line-height:1.45;letter-spacing:-.03em;word-break:keep-all}
.dv-q small{display:block;margin-top:6px;font-size:16px;color:var(--muted);font-weight:700;letter-spacing:0}
.dv-psr{display:grid;grid-template-columns:1fr 56px 1.25fr 56px 1fr;align-items:stretch;margin:auto 0}
.dv-psr .c{border-radius:24px;padding:30px 30px;display:flex;flex-direction:column;gap:14px;min-width:0}
.dv-psr .c.p{background:#fdf0f1}.dv-psr .c.s{background:#f3f1f6}.dv-psr .c.r{background:var(--purple-pale)}
.dv-psr .ar{display:flex;align-items:center;justify-content:center;font-size:34px;color:var(--purple);font-weight:900}
.dv-k{font-size:17px;font-weight:900;letter-spacing:.02em;color:var(--muted)}
.dv-psr .p .dv-k{color:var(--red)}.dv-psr .r .dv-k{color:var(--purple)}
.dv-big{font-size:60px;font-weight:900;letter-spacing:-.05em;line-height:1.05}
.dv-big.pu{color:var(--purple)}.dv-big.rd{color:var(--red)}
.dv-t{font-size:20px;font-weight:700;line-height:1.5;color:#4a4552;word-break:keep-all}
.dv-li{display:flex;flex-direction:column;gap:10px}
.dv-li div{background:#fff;border-radius:14px;padding:12px 16px;font-size:19px;font-weight:800;line-height:1.35;word-break:keep-all}
.dv-li div small{display:block;font-size:15px;color:var(--muted);font-weight:700;margin-top:2px}
.dv-days{display:flex;flex-direction:column;gap:14px;margin:auto 0}
.dv-days .row{display:grid;grid-template-columns:420px 1fr 120px;align-items:center;gap:22px}
.dv-days .who{font-size:20px;font-weight:800;line-height:1.35;word-break:keep-all}
.dv-days .who small{display:block;font-size:15px;color:var(--muted);font-weight:700}
.dv-days .bar{height:34px;border-radius:10px;background:var(--purple);min-width:34px}
.dv-days .bar.same{background:#1d8a52}
.dv-gantt .ev{display:block;flex:none;gap:0;margin-top:0;min-height:auto}
.dv-days .d{font-size:26px;font-weight:900;letter-spacing:-.04em;text-align:right}
.dv-tools{display:grid;grid-template-columns:repeat(5,1fr);gap:20px;margin:auto 0}
.dv-tl{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin:auto 0}
.dv-tl>div{background:#fff;border:2px solid #ece9f1;border-radius:22px;padding:28px 30px;display:grid;grid-template-columns:64px 1fr;column-gap:20px;row-gap:8px;align-items:center;min-width:0}
.dv-tl>div.on{border-color:var(--purple);background:var(--purple-pale)}
.dv-tl img{width:64px;height:64px;object-fit:contain;grid-row:1}
.dv-tl b{font-size:27px;font-weight:900;letter-spacing:-.04em;line-height:1.2;word-break:keep-all}
.dv-tl span{grid-column:1/-1;font-size:21px;font-weight:700;color:#4a4552;line-height:1.5;word-break:keep-all;margin-top:10px}
.dv-tl em{grid-column:1/-1;font-style:normal;font-size:17px;font-weight:900;color:var(--purple)}
.dv-tools>div{background:#fff;border:2px solid #ece9f1;border-radius:22px;padding:28px 20px;display:flex;flex-direction:column;gap:10px;min-width:0}
.dv-tools>div.on{border-color:var(--purple);background:var(--purple-pale)}
.dv-tools b{font-size:27px;font-weight:900;letter-spacing:-.04em}
.dv-tools span{font-size:18px;font-weight:700;color:#4a4552;line-height:1.45;word-break:keep-all}
.dv-tools em{font-style:normal;margin-top:auto;font-size:16px;font-weight:900;color:var(--purple)}
.dv-big-one{margin:auto 0;text-align:center}
.dv-big-one b{display:block;font-size:150px;font-weight:900;letter-spacing:-.06em;color:var(--purple);line-height:1}
.dv-big-one span{display:block;margin-top:22px;font-size:28px;font-weight:800;color:var(--ink);word-break:keep-all}
.dv-big-one small{display:block;margin-top:14px;font-size:20px;font-weight:700;color:var(--muted)}
"""

PARTS = ['질문 생성 로직 (하네스)', '실기업 기출', '공고 캐싱', '모의면접', '그 외']
PSUB = ['공고 × 내 커밋 → 근거 대조', '에이전트 수집 → pgvector 검색', '29곳 수집 · 1초 응답', '텍스트 · 음성', 'GA4 · GSC · SEO · Clarity · Sentry · 관리자 콘솔']
HARN = ['공고 JD', '내 커밋만', '근거 diff', '질문 생성', '근거 대조']  # 7장(Key Features 하네스)과 같은 이름

def wf(nodes, per=None, loop=None):
    """워크플로 노드: (아이콘|None, 제목, 설명, 도구라벨, 'on'|'dim'|'', llm여부)
    4개 이상이면 두 줄 ㄹ자 배치 — 윗줄 →, 오른쪽 끝에서 ↓, 아랫줄 ← (세로 공간을 채움)"""
    n = len(nodes)
    per = per or (n if n <= 3 else (n + 1) // 2)
    rows = 1 if n <= per else 2
    out = []
    for i, nd in enumerate(nodes):
        icn, t, d, tool, st, llm = (tuple(nd) + ('', '', '', '', False))[:6]
        r, c = divmod(i, per)
        if r == 1: c = per - 1 - c
        gc, gr = 2 * c + 1, 1 if r == 0 else 3
        ic_html = ic(icn, 34) if icn else ''
        em = f'<em class="{"llm" if llm else ""}">{tool}</em>' if tool else ''
        no = '' if st == 'dim' else f'<i class="no">{i + 1}</i>'
        out.append(f'<div class="n {st}" style="grid-column:{gc};grid-row:{gr}">{no}{ic_html}<b>{t}</b><span>{d}</span>{em}</div>')
        if i < n - 1:
            nr = (i + 1) // per
            if nr == r:
                out.append(f'<div class="a" style="grid-column:{gc + 1 if r == 0 else gc - 1};grid-row:{gr}">{"→" if r == 0 else "←"}</div>')
            else:
                out.append(f'<div class="a" style="grid-column:{gc};grid-row:2">↓</div>')
    if loop and rows == 2 and n % per:   # 아랫줄 빈칸 = 처음으로 되돌아가는 반복 표시
        lt, ls = loop
        out.append(f'<div class="a" style="grid-column:2;grid-row:3">←</div><div class="loop" style="grid-column:1;grid-row:3"><b>↺</b><span>{lt}</span><small>{ls}</small></div>')
    cols = ' 52px '.join(['1fr'] * per)
    rws = 'auto' if rows == 1 else 'auto 44px auto'
    return f'<div class="dv-wf" style="grid-template-columns:{cols};grid-template-rows:{rws}">' + ''.join(out) + '</div>'

def cards(items, cols=None):
    """1차/2차/3차 카드: (머리, 제목, 문제, 해결, 결과, 결과보조, on)"""
    h = []
    for it in items:
        head, title, prob, sol, res, rs, on = (tuple(it) + ('', False))[:7]
        rsm = f'<small>{rs}</small>' if rs else ''
        h.append(f'<div class="dv-card {"on" if on else ""}"><h3><small>{head}</small>{title}</h3><p><b>문제</b>{prob}</p><p><b>해결</b>{sol}</p><div class="r">{res}{rsm}</div></div>')
    return f'<div class="dv-cards" style="grid-template-columns:repeat({cols or len(items)},1fr)">' + ''.join(h) + '</div>'

def psr(p, s, r):
    """문제 → 해결 → 결과 3칸. 각 칸 = HTML"""
    return f'<div class="dv-psr"><div class="c p"><div class="dv-k">문제</div>{p}</div><div class="ar">→</div><div class="c s"><div class="dv-k">해결</div>{s}</div><div class="ar">→</div><div class="c r"><div class="dv-k">결과</div>{r}</div></div>'

def li(rows): return '<div class="dv-li">' + ''.join(f'<div>{a}' + (f'<small>{b}</small>' if b else '') + '</div>' for a, b in rows) + '</div>'

# ================= Development =================
S.append(divider('03 · 개발', 'Development', '방금 본 화면의 뒷면 — 다섯 갈래와 수행과정'))
S.note('''[구분] Development — 질문 생성 로직 · 실기업 기출 · 공고 캐싱 · 모의면접 · 그 외, 그다음 수행과정 순서로 넘어갑니다.''')

# ───────────────── 1. 질문 생성 로직 (하네스) ─────────────────
S.append(shell('Development · 질문 생성 - 하네스 구조', '하네스 5단계 — <span class="purple">규칙과 LLM을 칸마다 나눠</span> 사용', f'''
{wf([('link', '공고 JD', '29곳에서 본문 수집 · 직무·역량 정리', 'LLM 추출', '', True),
     ('shield', '내 커밋만', '본인 1.0 · 공동 0.70 · 남의 커밋 제외', '규칙 + 판정 모델', '', True),
     ('doc', '근거 diff', '작업 단위 4~10개 · 조각당 72줄', '규칙', ''),
     ('chat', '질문 생성', '의도 7유형 · 작업당 최대 4문항', 'GLM-5', '', True),
     ('search', '근거 대조', '인용 코드 ↔ 실제 전송 코드', '서버 대조', 'on'),
     ('mic', '학습실 · 음성', '피드백 · 꼬리질문', '하네스 밖', 'dim')])}''',
    source='운영 브랜치 origin/prod (2026-11-06) · 보라 라벨 = LLM 호출 칸 · 모델·스택 전체는 부록 A12'))
S.note('''[≈20초] 첫 번째, 질문 생성 로직입니다. 하네스는 다섯 칸입니다. 공고에서 직무와 역량을 뽑고, 내 커밋만 남기고, 질문할 코드 조각을 묶고, 질문을 만들고, 마지막으로 질문이 인용한 코드가 실제로 보낸 코드에 있는지 서버가 대조합니다. 보라색 라벨이 LLM을 부르는 칸입니다. 커밋 선별에도 판정 모델을 섞습니다.

근거(origin/prod d84cb1c): ContributionOwnershipService(LEAD 1.0 / PARTIAL 0.70 / NOT_MINE 0.0) · QuestionBankService MAX_QUESTIONS_PER_EPISODE=4 · application.yml evidence-patch-lines 72, reasoning=zai.glm-5(temperature 0.2) · 커밋 판정 gpt-6-luna(application.yml:336-354).
⛔ «커밋 선별 LLM 0회» 금지 — 판정 모델을 섞는다. 5단계 이름은 8장(«차이는 하네스», s1) 그대로. 하네스는 팀 주장(claims.md C2) — 배경: 11-02 김동현 멘토 녹취 02:08–02:10(장표엔 인용하지 않음).
Q&A 외부 근거(research/R2): 같은 GPT-4 Turbo로 하네스만 바꿔 SWE-bench Lite 11.0% → 18.0%(SWE-agent, NeurIPS 2024) — 8장(s1 «차이는 하네스»)에 이미 있음. 허용선 «모델이 같아도 하네스에 따라 크게 달라진다»까지. ⛔ «모델보다 하네스가 중요» 단정 금지(같은 하네스에 모델만 바꿔도 22→33→49%).''')

S.append(shell('Development · 질문 생성 - 커밋 선별', '커밋 1,000개에서 <span class="purple">내가 짠 코드만</span> 남김', f'''
{psr(f'<div class="dv-big rd">전부 동점</div><div class="dv-t">메시지 점수만 쓰면 팀 저장소 커밋이 같은 점수 — GitHub 최신순이 그대로 남음</div>',
     li([('잡음 커밋 제외', 'merge · bump · dependabot · docs · lint'), ('규칙 0.4 : 판정 모델 0.6', '모델이 25초 넘기거나 절반도 못 채점하면 규칙만으로'), ('본인 기여 가중치', '본인 1.0 · 공동 0.70 · 남의 커밋 0'), ('동점은 sha 순서', '같은 입력이면 같은 순서')]),
     f'<div class="dv-big pu">1,000 → 96 → 4~10</div><div class="dv-t">커밋 → 상세 diff → 작업 단위. 작업당 질문은 최대 4개</div><div style="margin-top:auto">{badge("특허 출원 10-2026-0214808")}</div>')}''',
    source='origin/prod GithubService(DETAIL_POOL 96 · 레포당 최소 16) · CommitDecisionBlend · application.yml(keyword 0.40 / specificity 0.60 · message-weight 0.6 · repo-deadline 25초) · B2C 분석 경로'))
S.note('''[≈15초] 팀 프로젝트 저장소에서 메시지 점수만 쓰면 커밋이 전부 동점이 됐고, GitHub가 준 최신순이 그대로 남았습니다. 그래서 잡음 커밋을 빼고, 규칙 점수에 커밋 판정 모델을 섞고, 본인 기여도를 곱하고, 동점은 sha 순서로 깹니다. 결과적으로 커밋 1,000개가 상세 diff 96개, 작업 단위 4~10개로 좁혀집니다.

근거: GithubService.java:107(DETAIL_POOL=96), :116(MIN_DETAIL_PER_REPO=16) · application.yml:294-295(0.40/0.60), :348(25초), :353-354(0.6/0.5) · ContributionOwnershipService:53-55.
⛔ «1,000 → 12 → 6»은 B2B 경로 숫자 — 쓰지 않음. 판정 모델 비중 0.6은 설정값(실험 근거는 diagnostics 로그).''')

S.append(shell('Development · 질문 생성 - 근거 대조', '질문이 인용한 코드가 없으면 <span class="purple">서버가 폐기</span>', f'''
{wf([('chat', '질문 생성', '질문마다 근거 코드 한 줄을 12자 이상 그대로 인용', 'GLM-5', '', True),
     ('doc', '실제 전송 코드', '모델에 보낸 압축 근거 그대로 · diff 기호·주석 제외', '서버', ''),
     ('search', '대조', '인용이 그 코드에 있는가 · 식별자가 코드 밖인가', 'LLM 0회', 'on'),
     (None, '판정', '<div class="dv-out"><i class="k">유지</i><i class="q">재질의 1회</i><i class="d">폐기</i></div>', '', '')])}
<div class="dv-q" style="margin-top:28px">실행 1회 — 63개 생성 → <strong>5개 폐기</strong> → 58개 저장. 답변 가이드도 모델 서술이 아니라 검증된 인용으로 서버가 조립<small>레포 1개 · 1회 실행 (flag-ab-test 2026-09-08)</small></div>''',
    source='origin/prod BedrockService(evidenceQuote ≥12자) · QuestionGrounding(KEEP / REASK / DISCARD) · QuestionBankService:1053-1066 · 특허 출원 10-2026-0214809'))
S.note('''[≈15초] 모델은 질문마다 근거 코드 한 줄을 그대로 인용해야 합니다. 서버는 그 인용이 실제로 보낸 코드에 있는지 대조해서, 유지하거나 한 번 다시 묻거나 버립니다. 이 단계는 LLM을 부르지 않습니다. 한 번 돌리면 63개 중 5개가 여기서 버려졌습니다.

근거: BedrockService.java:233·572(evidenceQuote 스키마·지시) · QuestionGrounding.java:31-35(KEEP/DISCARD/REASK — 재생성 예산이 없으면 KEEP로 강등) · collect/C §1-4(63 → 5 폐기 → 58, 레포 1개 1회).
⛔ «인용 46/46 일치» 금지(정의상 100%). 운영 30일 84건 차단은 s1 8장(«차이는 하네스») 노트에 있음. 인용 존재가 질문 전제의 정확성까지 증명하진 않음(문서에 명시).''')

S.append(shell('Development · 질문 생성 - 발전과정 ①', '질문 생성 단계는 <span class="purple">세 번 수정</span>', f'''
{cards([('1차 · 근거가 잘림', '모델에 코드가 거의 안 감', '파일당 14줄만 넣어 원본 변경 줄의 8.4%만 프롬프트에 도달', '판단 경계(분기·예외·재시도)에 가점 · 조각을 자르지 않고 72줄 보존', '14줄 → 72줄', '파일당 근거 줄 수'),
        ('2차 · 묶음 호출 실패', '한 번에 많이 만들다 깨짐', '작업 2개를 한 호출로 묶으면 배치 실패율 52%', '작업 1개당 호출 1번으로 분리 · 실패 시 근거를 50%·25%로 줄여 재시도', '52% → 22%', '배치 실패율 · 34배치'),
        ('3차 · 느리고 잘림', '출력이 길어 잘림', '7유형을 한 호출에 몰아 평균 93.7초 · 출력 잘림 발생', '유형을 4 + 3으로 나눠 병렬 요청 후 병합', '93.7초 → 49.1초', '질문 생성 단계 · 잘림 1 → 0 · 사례 3개 × 2회', True)])}''',
    source='collect/C §2 · results.md §6.2·§7.1 · REPOSITORY_ANALYSIS_PERFORMANCE.md:72-82 · question-generation-logic.md (v13, 10-16)'))
S.note('''[≈15초] 여기까지가 구조고, 지금 모양이 되기까지 질문 생성 단계는 세 번 고쳤습니다. 처음엔 파일당 14줄만 넣어서 변경된 코드의 8%만 모델에 갔습니다. 72줄로 늘렸습니다. 작업 두 개를 한 번에 만들면 절반이 깨져서 한 개씩 나눴더니 실패율이 52%에서 22%로 줄었습니다. 마지막으로 유형을 나눠 병렬로 요청해 93.7초가 49.1초가 됐습니다.

출처: collect/C §2-1(14줄→72줄, 8.4% = 20,310줄 중 1,703줄 · 개선 후 도달률은 재측정 안 함), §2-1(배치 52% → 22%, 34배치), §2-2(93.70s → 49.07s, 고정 사례 3개 × 2회, 입력 토큰 +54.2% — 전체 분석 시간 아님).
Q&A: v13 벤치마크에선 실행당 60.29 → 83.95초(다른 벤치마크라 직접 비교 불가).''')

S.append(shell('Development · 질문 생성 - 발전과정 ②', '"쉬운 질문이 사실 확인뿐" → <span class="purple">2일 만에</span> 추론형으로', f'''
{psr('<div class="dv-q" style="background:#fff">"쉬움 질문이 코드 사실 확인뿐이다"<small>한유일 멘토 · 09-07 실사용 검증</small></div><div class="dv-t">원인: 난이도가 질문 유형의 별칭 — 114문항 중 예외 0</div>',
     '<div class="dv-big">난이도 ⟂ 유형</div><div class="dv-t">난이도를 근거 두께·추론 부담으로 다시 정의 · 쉬운 구간에도 가정형(만약 ~라면) 허용</div><div class="dv-t" style="margin-top:auto"><b>09-09 운영 반영</b> (피드백 2일 뒤)</div>',
     '<div class="dv-big pu">1/8 → 7/9</div><div class="dv-t">쉬운 구간 질문 중 추론형</div>')}''',
    source='collect/C 검증표 · mentor-4-final-report-2026-09-09 · 단일 레포 각 1회 실행 · BE 32e25e9 → prod #47'))
S.note('''[≈15초] 한유일 멘토님이 실사용 검증에서 쉬운 질문이 코드 사실 확인뿐이라고 지적하셨습니다. 원인은 난이도가 사실상 질문 유형의 다른 이름이었던 것입니다. 114문항 중 예외가 없었습니다. 난이도를 근거 두께와 추론 부담으로 다시 정의해 2일 만에 운영에 반영했고, 쉬운 구간 9문항 중 7문항이 추론형이 됐습니다.

출처: collect/C 검증표(기준 1/8, H1 7/9 — 분모 표기 필수) · 08-타임라인(09-07 → 09-09 prod #47 6cf2a7e).
⛔ «12% → 78%» 금지. Q&A: 최종 배포본(H2)에선 레포 1개 실행에서 난이도 1·2가 아예 안 나옴 → 이 지표는 «구조를 끊었다»의 사례로만 씀.''')

# ───────────────── 2. 실기업 기출 ─────────────────
S.append(shell('Development · 실기업 기출 - 수집 원칙', '그 회사가 실제로 묻는 것 — <span class="purple">공개 출처에서만</span> 수집', psr(
    '<div class="dv-q" style="background:#fff">"그 회사의 면접 리뷰가 중요한 거 같아요"<small>사용자 요청 (VOC)</small></div><div class="dv-t">내 코드 근거만으로는 그 회사가 실제로 무엇을 묻는지 모름</div>',
    '<div class="dv-big">공식 경로 0곳</div><div class="dv-t">기업 면접 질문을 사 오거나 받아 올 공식 API 없음 · 사이트 약관·판례상 긁어 와 그대로 쓸 수도 없음 (08-16 사전조사)</div>',
    '<div class="dv-big pu">공개 출처 + URL</div><div class="dv-t">공개 후기만, 출처 URL과 함께 보존 · robots가 막은 곳과 AI 수집을 막은 블로그는 제외</div>'),
    source='collect/D VOC · Devfit/docs/interview-data-sourcing/00_executive_summary.md (2026-08-16) · 수집 원칙 상세는 부록 A8'))
S.note('''[≈10초] 두 번째, 실기업 기출입니다. 사용자는 그 회사의 실제 면접 후기를 원했습니다. 그런데 기업 면접 질문을 사 오거나 받아 올 공식 경로는 없었습니다. 그래서 공개된 후기만, 출처 URL과 함께 모으기로 했습니다.

출처: collect/D-growth-voc.md:167(요청 6건 중 1건) · interview-data-sourcing/00_executive_summary.md(공식 API 0건, 판례·약관 검토).
Q&A(저작권): 원문 대신 주제·링크 위주가 사전조사 권고였고, 지금은 원문 질문과 출처 URL을 함께 저장해 질문 옆에 보여 준다 — 법률 검토 의견은 확보 안 됨.''')

S.append(shell('Development · 실기업 기출 - 수집 워크플로', '수집 워크플로 — <span class="purple">웹 접근은 한 곳에서만</span>', f'''
{wf([('link', '열거', '목록 API로 후기 글 URL 수집', '결정론', ''),
     ('shield', '캐시', 'robots 확인 · 도메인당 1.5초 · 원문 1회 저장', '결정론', 'on'),
     ('doc', '추출', '캐시만 읽고 질문 추출 · 웹 접근 없음', '에이전트', '', True),
     ('chat', '의미 리뷰', '코딩 문제·주제 라벨만 있는 항목 거절', '에이전트', '', True),
     ('search', '원문 대조', '질문 근거 문장이 원문에 그대로 있는가', '스크립트', ''),
     ('db', '적재', '(URL + 원문) 해시 키 · 출처 URL 보존', 'DB', '')])}''',
    source='progress.md Wave 3 (fetch_cache.py · source_check.py) · 추출 raw 819 → 리뷰 거부 31 → 순증 763 (3차 내 velog·티스토리분)'))
S.note('''[≈10초] 웹에 접근하는 건 캐시 단계 하나뿐입니다. 거기서 robots를 확인하고 도메인당 1.5초 간격으로 원문을 한 번만 받습니다. 추출과 리뷰 에이전트는 그 캐시만 읽고, 마지막에 스크립트가 근거 문장이 원문에 그대로 있는지 대조합니다.

출처: progress.md Wave 3 · 제외: robots가 Claude 수집을 명시 차단한 채용 사이트, AI 수집을 막은 블로그, 해외 후기, 필기·코테.
Q&A: 일부 사이트 robots 정책 판단은 미결(progress.md §90).''')

S.append(shell('Development · 실기업 기출 - 기출 검색', '표현이 달라도 같은 기출을 찾도록 — <span class="purple">벡터로 넓히고 어휘로 판정</span>', f'''
{wf([('chat', '생성된 질문', '학습실에서 질문을 열 때', '', ''),
     ('search', 'pgvector 후보 100', 'Cohere Embed v3 · 1024차원 · 코사인 거리', '임베딩', 'on', True),
     ('doc', '어휘 판정', '0.6 × Jaccard + 0.4 × 포함률 ≥ 0.72', '규칙', 'on'),
     ('db', '비슷한 실제 기출', '질문 옆에 출처 URL과 함께 표시', '', '')])}
<div class="dv-q" style="margin-top:28px">생성 프롬프트에는 남의 질문을 넣지 않음 — <strong>출처와 함께 옆에 보여 줄 뿐</strong><small>벡터가 없으면 어휘 매칭으로 폴백</small></div>''',
    source='origin/prod InterviewQuestionVectorSearch(CANDIDATE_LIMIT 100) · InterviewQuestionSimilarity(MIN_SCORE 0.72) · V87 · prod BE#159 c680990 (11-02)'))
S.note('''[≈12초] 기출 검색은 두 단계입니다. pgvector로 의미가 가까운 후보 100개를 넓게 뽑고, 최종 판정은 어휘 점수로 합니다. 그리고 남의 질문을 생성 프롬프트에 넣지 않습니다. 질문 옆에 출처와 함께 보여 줄 뿐입니다.

근거: InterviewQuestionVectorSearch.java:21(100) · InterviewQuestionSimilarity.java:29·101·105(0.72, 길이 2.5배 이상이면 0.2J+0.8C) · V87(vector 확장, interview_question_vector 1024) · docs/interview-question-evidence.md(«질문 생성 프롬프트에는 기업 질문을 넣지 않는다»).
🔴 확인 필요: 벡터 경로 플래그 기본값이 false(APP_INTERVIEW_EVIDENCE_VECTOR_ENABLED) — 운영에서 켰는지 저장소로 확인 못 함. 켜져 있지 않으면 «운영 반영»은 «코드 운영 배포»로만 말할 것.
⛔ «RAG로 질문을 생성» 금지(생성 단계 RAG 아님). 적중률·연결 수 측정값 없음. Q&A: 11-05 감사에서 엉뚱한 매칭 사례(회사 필터 없음) → 개선 과제.''')

S.append(shell('Development · 실기업 기출 - 발전과정', '수집은 <span class="purple">결정론 열거</span>로, 검색은 <span class="purple">하이브리드</span>로', cards([
    ('1차 · 10월 · 운영', '공개 후기 수집', '회사별 실제 질문이 하나도 없음', '공개 출처에서 수집 · (출처 URL + 원문) 해시로 중복 방지 · LLM 보조 정제로 한국어 사용본', '853건 · 41개사', '출처 URL 304개 · 검수 진행 중'),
    ('2차 · 11-02 · 멘토링', '기출 검색 하이브리드', '단어 겹침만 봐서 표현이 다르면 같은 기출을 못 찾음', '"정확 매칭 + 임베딩 하이브리드로" 조언 → pgvector 후보 100 + 어휘 판정', '당일', '운영 배포 · prod BE#159'),
    ('3차 · 11-05 · 에이전트 웹검색', '직군별 에이전트 9개', '직군별로 더 넓게 모아야 함', '직군별 에이전트가 웹검색으로 수집 → 원문을 다시 받아 대조하는 스크립트로 검증', '247건 → 63건', '같은 비용에 수확이 1/4 · 검색 쿼터 소진 → 포화'),
    ('4차 · 11-05 · 결정론 열거', '열거 · 캐시 · 추출 분리', '에이전트가 검색까지 하면 비싸고 겹침', '목록 API로 글을 열거 → robots 확인·도메인당 1.5초 간격 캐시 → 추출 에이전트는 캐시만 읽음', '1,073건', '원문 대조 1,073/1,073 일치 · 개발 DB 적재', True)]),
    source='1차: interview-evidence-audit-2026-10-11 · production-upload-result-2026-10-11.json · 2차: prod BE#159 c680990 (11-02) · 3·4차: Devfit/research/interview-evidence/reports/progress.md (2026-11-05, 사용자 지시로 크롤링 중단)'))
S.note('''[≈20초] 기출은 이렇게 바뀌어 왔습니다. 처음엔 공개 후기 853건, 41개사를 모아 운영에 올렸습니다. 11월 2일 멘토링에서 정확 매칭과 임베딩을 섞으라는 조언을 받아 검색을 당일 하이브리드로 바꿨습니다. 수집을 더 넓히려고 직군별 에이전트 9개에게 웹검색을 시켰더니 1차 247건, 2차 63건으로 같은 비용에 수확이 4분의 1로 줄었습니다. 그래서 방법을 바꿨습니다. 목록 API로 글을 먼저 다 열거하고, robots를 확인하며 천천히 캐시한 뒤, 추출 에이전트는 캐시만 읽게 했습니다. 1,073건을 더 모았고 원문 대조는 전부 일치했습니다.

출처: 1차 853건·41개사·URL 304(10-08 PR #89 운영, 10-11 정제 = 신규 0 · 갱신 799 · 변경 없음 54) / 2차 wave1 수락 247(원문 247/247 일치) → wave2 순증 63, 약 250만 subagent 토큰 / 3차 링커리어·velog·티스토리 열거 → 1,073건(DIRECT 818 · TOPIC 255), 원문 대조 1,073/1,073. dev DB 삽입 1,027행(차이 사유 미확인) — 운영 반영 전.
⛔ «검증된 853건» 금지(사람 검수 REVIEWED 0 · NEEDS_REVIEW 158). «운영에 1,926건» 금지(1,073은 개발 DB).
🔴 2차(벡터 검색) 플래그 기본값 false — 운영에서 켰는지 미확인. 말로는 «당일 운영 배포»까지만.''')

# ───────────────── 3. 공고 캐싱 ─────────────────
S.append(shell('Development · 공고 캐싱 - 구조', '공고 URL 하나로 <span class="purple">29곳</span>에서 본문을 받고, <span class="purple">두 층으로 캐시</span>', f'''
{wf([('link', '공고 URL', '채용 플랫폼 5 + 기업 채용 사이트 24', '', ''),
     ('doc', '사이트 판별', '사이트 1곳 = 클래스 1개 + 등록 1줄', '레지스트리', ''),
     ('shield', '안전 수집', '홉마다 허용 호스트 재검사 · 응답 8MB 상한', 'SafeFetcher', ''),
     ('search', '이미지 공고', '본문 200자 미만이면 OCR', 'OCR', '', True),
     ('db', '캐시 2층', '본문(사이트·공고 키) + LLM 결과(본문 해시 키) · 30일', 'read-through', 'on'),
     ('chat', '준비 카드', '캐시 히트 시 네트워크·LLM 0회', '', '')])}
<div class="dv-q" style="margin-top:28px">기업 공채 사이트 22곳 중 <strong>10곳은 본문이 이미지 1장</strong> — 그래서 OCR이 수집 경로 안에 들어감<small>사용자 공고의 22%가 기업 사이트 (내부 제외 83건 중 18건)</small></div>''',
    source='origin/prod prep/corporate (CorporateSite · CorporateSiteRegistry · SafeFetcher · CorporateParsing.withOcrFallback) · prep/cache (V59·V60, TTL 30일) · 22곳 중 10곳: corporate-boards-2/STATUS.md'))
S.note('''[≈15초] 세 번째, 공고 캐싱입니다. 공고 URL 하나를 넣으면 채용 플랫폼 5곳과 기업 채용 사이트 24곳, 모두 29곳에서 본문을 받습니다. 사이트 하나가 클래스 하나라서 새 사이트는 파일 하나와 등록 한 줄로 붙습니다. 기업 공채는 절반 가까이가 본문을 이미지 한 장으로 올려서 짧은 본문은 OCR로 읽고, 본문과 LLM 결과를 두 층으로 캐시합니다.

근거(origin/prod): CorporateSite 인터페이스 · sites/*Site.java 24개 · CorporateSiteRegistry · SafeFetcher(CorporateSiteSourceRulesTest가 Jsoup.connect 0건 잠금) · CorporateParsing.withOcrFallback(200자 미만 · OCR이 더 길 때만) · JobPostingReadThroughService · InterviewPreparationInsightCacheTest · 크롤 일일 예산 LLM 1,000 · OCR 300, 응답 못 받은 호출은 예산 환급, 비개발 공고는 skip_reason으로 재과금 안 함.
⛔ 회사명·로고·«제휴» 금지. «공고 1,450건 사전 수집» 본편 금지(직업안정법 표현 리스크, K-compliance O5).''')

S.append(shell('Development · 공고 캐싱 - 발전과정', '공고 카드 생성, <span class="purple">17~34초에서 1초로</span>', cards([
    ('1차 · 07-19', '공고 URL · 이미지 입력', '공고 단위로 준비하려면 공고 본문이 먼저 필요', '채용 플랫폼 HTML 파싱 + 이미지 입력 · LLM으로 직무·역량 정리', '공고 1개 = 카드 1장', '공고 단위 준비의 시작'),
    ('2차 · 09-15', '기업 채용 사이트', '기업 공채는 플랫폼에 없고 22곳 중 10곳이 본문 이미지 1장', '사이트 1곳 = 클래스 1개 + 등록 1줄 · SafeFetcher · 200자 미만 OCR · 09-18 토스 추가', '29곳', '플랫폼 5 + 기업 채용 사이트 24'),
    ('3차 · 09-18', '공고 캐시 2층', '사람마다 같은 공고를 다시 받고 다시 분석 — 카드 1장 17~34초', '본문 + LLM 결과 read-through 캐시 · 09-21 오만료·비개발 공고 재과금 방지', '1.0초', '캐시 공고 카드 · 네트워크·LLM 0회', True)]),
    source='커밋일(origin/prod): 74b9f18(07-19) · ee304b2·b7cd360(09-15) · 5b45b2d·0794272(09-18) · 8250405(09-21) · 지연: 운영 11-05 · 공고 4건 · 내부 계정 (collect/F §2·§3)'))
S.note('''[≈15초] 공고 처리는 세 번 바뀌었습니다. 7월에 공고 URL과 이미지를 받는 것으로 시작했고, 9월 15일에 기업 채용 사이트를 «파일 하나 + 등록 한 줄» 구조로 붙였습니다. 그래도 공고마다 본문을 받고 LLM으로 분석하느라 카드 하나에 17초에서 34초가 걸려서, 9월 18일에 본문과 LLM 결과를 캐시했습니다. 캐시된 공고는 1초에 카드가 만들어지고 네트워크도 LLM도 부르지 않습니다.

근거: 커밋일 기준(운영 배포일 아님) — 74b9f18 «채용공고 URL·이미지 인풋» · ee304b2 «파일 1개 + 레지스트리 1줄» · b7cd360 SafeFetcher OCR · 5b45b2d 캐시 코어 V59 · 0794272 V60 보강 · 8250405 오만료 수정.
Q&A: 캐시 적중 20건(1건에 39회 몰림)·마지막 크롤 9/30 → 적중률은 쓰지 않음. 지연 비교는 표본 4건.''')

# ───────────────── 4. 모의면접 ─────────────────
S.append(shell('Development · 모의면접 - 텍스트', '텍스트 — 답하면 <span class="purple">피드백과 꼬리질문</span>으로 이어짐', f'''
{wf([('chat', '본 질문', '내 코드 근거 · 의도 7유형', '', ''),
     ('doc', '내 답변', '텍스트 입력', '', ''),
     ('search', '피드백', '질문이 요구한 확인점으로 채점 · 묻지 않은 것은 감점 안 함', 'Qwen3-Coder', 'on', True),
     ('chat', '꼬리질문', '대안 → 실패·엣지 → 검증 순으로 깊어짐', 'LLM', '', True),
     ('shield', '최대 5단', '답할 때마다 다음 꼬리질문 2~3개', '', '')], loop=('2번으로 — 꼬리질문에 다시 답변', '체인 최대 5단'))}''',
    source='origin/prod BedrockService evaluateAnswer(code 모델, temperature 0.15, JSON Schema) · StudySetService MAX_FOLLOW_UP_CHAIN=5 · BE c5a3ac7 → prod 9a808a2 (09-07)'))
S.note('''[≈15초] 네 번째, 모의면접입니다. 텍스트 모의면접은 답을 쓰면 피드백과 꼬리질문이 나오고, 꼬리질문에 답하면 또 이어집니다. 최대 5단까지 갑니다.

출처: 녹취 docs/feedback/record/260907-한유일멘토님.txt:104 · BE c5a3ac7 → prod 9a808a2(09-07) · StudySetService.java:44.
측정값 없음: 피드백 지연 전후 수치(«이후 잘림 재현 없음»은 정성 서술). 점수는 본인만 보는 «답변 준비도»(헌법 1). Q&A: 텍스트 세트 완료 4.4%(182 중 8) → 완주가 다음 병목.''')

S.append(shell('Development · 모의면접 - 음성', '음성 — <span class="purple">말로 답하면, 답을 듣고 되물음</span>', f'''
{wf([('mic', '브라우저 녹음', '48kHz → 16kHz PCM · 답변 최대 3분', 'AudioWorklet', ''),
     ('shield', 'WebSocket 프록시', '세션·소유권 검증 · 동시 4세션', 'Spring', ''),
     ('doc', 'STT', '자막은 작은 모델로 약 0.9초마다 · 저장은 큰 모델로 확정', '음성 사이드카', 'on'),
     ('chat', '꼬리질문', '내 답변을 보고 60자 이하 1개 · 검토 후 1회 재작성', 'GLM-5', '', True),
     ('spk', 'TTS로 되묻기', '세트 생성 때 미리 합성 · 최대 5문항', '', '')], loop=('1번으로 — 되물음에 말로 답변', '최대 5문항'))}''',
    source='origin/prod public/pcm-worklet.js · speech-local(STT 하이브리드 b929ec4) · generateVoiceFollowUp(reasoning, 0.2) · VoiceDialogue.MAX_QUESTIONS 5 · 특허 출원 10-2026-0214811'))
S.note('''[≈15초] 음성 모의면접은 말로 답합니다. 브라우저에서 16kHz로 녹음해 서버로 보내고, 자막은 작은 모델로 빠르게 띄우고 저장용 글은 큰 모델로 확정합니다. 그 답을 보고 꼬리질문을 하나 만들어 음성으로 되묻습니다. 최대 5문항입니다.

출처: 녹취 260907-한유일멘토님.txt:251-254 · prod 98ebb0f(09-16 «음성 모의면접 Supertonic 전환») · speech-local/README.md(whisper small 자막 · large-v3-turbo 확정, 8초 넘으면 발화 경계에서 확정).
🔴 확인 필요: 운영 STT provider(env APP_SPEECH_PROVIDER). 코드 기본값·09-16 릴리스는 자체 사이드카(faster-whisper STT + Supertonic TTS), AwsSpeechProvider(Transcribe·Polly)는 대체 경로. 확인 전엔 «Transcribe»라고 말하지 말 것.
⛔ 자체 음성 모델 주장 금지(오픈소스 모델 사용). Q&A: 음성 세트 18건 생성·완료 0건 · 개인정보처리방침에 음성 항목 없음(K-compliance) → 발표 전 확인.''')

S.append(shell('Development · 모의면접 - 발전과정 ①', '멘토 시연 하루에 나온 두 가지 — <span class="purple">당일, 9일 만에</span> 반영', cards([
    ('09-07 · 텍스트', '피드백 타임아웃', '"유저가 10초 이상 기다리다가 타임아웃 나와서… 실패로" (한유일 멘토 시연)', 'AI 피드백 출력 한도 1,280 → 8,192 토큰', '당일', '운영 반영 09-07'),
    ('09-16 · 음성 1차', '말로 답하기', '"실제 면접을 할 때도 텍스트로 하지 않고 말로 하니까" (한유일 멘토)', '음성 모의면접 출시 — 녹음 · STT · 답을 보고 꼬리질문 · TTS로 되묻기', '9일', '운영 반영 09-16', True)]),
    source='녹취 260907-한유일멘토님.txt:104 · :251-254 · BE c5a3ac7 → prod 9a808a2 (09-07) · prod 98ebb0f (09-16)'))
S.note('''[≈12초] 모의면접은 이렇게 바뀌어 왔습니다. 9월 7일 한유일 멘토님 시연에서 텍스트 피드백이 타임아웃으로 실패했고, 출력 한도를 올려 당일 운영에 반영했습니다. 같은 자리에서 실제 면접은 말로 하니까 음성이 편하겠다고 하셔서, 9일 뒤 음성 모의면접을 냈습니다.

출처: 녹취 docs/feedback/record/260907-한유일멘토님.txt:104 · :251-254 · BE c5a3ac7 → prod 9a808a2(09-07) · prod 98ebb0f(09-16 «음성 모의면접 Supertonic 전환»).
측정값 없음: 피드백 지연 전후 수치(«이후 잘림 재현 없음»은 정성 서술).''')

S.append(shell('Development · 모의면접 - 발전과정 ②', '음성은 출시 후 <span class="purple">세 번 더 수정</span>', cards([
    ('09-18 · 2차', '답변 끝에서 멈춤', '말을 끝내도 전사가 끝나지 않아 종료가 타임아웃', '수신 종료와 전사 완료를 분리 · 타임아웃을 사이드카 40초 < 서버 45초 < 브라우저 60초로 정렬', '답변 3분까지', '종료 타임아웃 해결과 함께 확대'),
    ('09-22 · 3차', '자막이 늦음', '큰 모델 하나로 자막까지 만들면 화면이 늦게 따라옴', '자막은 작은 모델로 약 0.9초마다, 저장은 큰 모델로 청크 확정 (하이브리드)', '자막 ≈ 0.9초', '갱신 간격 (설정값)'),
    ('10-09 · 4차', '꼬리질문이 답과 무관', '미리 만든 꼬리질문이 내 답변을 안 봄', '실제 답변의 주장·선택·설명 부족을 보고 60자 이하 질문 1개 · 중복이면 1회 재작성', '1/4 → 4/4', '꼬리질문 반환 · 코드 1개 × 합성 답변 2개 × 2회', True)]),
    source='prod 반영: 08abfcb(09-18) · fcb5b41(09-22) · 9f7b934(10-09) · speech-local/README.md · question-logic-v13-2026-10-16.md:12'))
S.note('''[≈10초] 음성은 출시하고 세 번 더 고쳤습니다. 말을 끝내도 멈추지 않던 문제는 수신과 전사를 분리하고 타임아웃 순서를 맞춰 풀었습니다. 자막이 늦던 문제는 자막과 저장을 다른 모델로 나눠 풀었습니다. 꼬리질문이 내 답을 안 보던 문제는 답변을 보고 만들게 바꿨습니다.

출처: 54001a2·917876f → 08abfcb(09-18) · b929ec4 → fcb5b41(09-22) · c4f7169·1e9193a → 9f7b934(10-09).
⛔ 1/4 → 4/4는 운영 성공률이 아님(fixture). 음성 지연·STT 정확도(CER) 측정값 없음 — 평가 스크립트만 있음.''')

# ───────────────── 5. 그 외 ─────────────────
S.append(shell('Development · 그 외 - 운영 도구', '도구 여섯 개를 붙이고, <span class="purple">숫자의 정본은 관리자 DB</span>로 지정', '''
<div class="dv-tl">
  <div><img src="assets/dv-logo-ga4.svg" alt="GA4"><b>GA4</b><span>동의한 방문자의 퍼널 측정 — 로그인 → 공고 → 분석 → 완료 · Consent Mode v2</span></div>
  <div><img src="assets/dv-logo-gsc.svg" alt="Google Search Console"><b>Google Search Console</b><span>구글 검색어·노출·색인 상태 확인 · sitemap 제출</span></div>
  <div><img src="assets/dv-logo-naver.svg" alt="네이버 서치어드바이저"><b>네이버 서치어드바이저</b><span>네이버 검색 소유 확인 · 수집 요청 · sitemap·RSS 제출</span></div>
  <div><img src="assets/dv-logo-clarity.png" alt="Microsoft Clarity"><b>Microsoft Clarity</b><span>세션·유입 경로로 이탈 지점 확인 · 화면 전체 마스킹 · 운영 B2C만</span></div>
  <div><img src="assets/dv-logo-sentry.svg" alt="Sentry"><b>Sentry</b><span>FE·BE·분석 워커 오류 수집과 알림 · Replay 끔</span></div>
  <div class="on"><img src="assets/icon.svg" alt="DevFit 관리자 콘솔"><b>관리자 콘솔 (자체 개발)</b><span>회원·B2C 지표·LLM 원가 원장·실패·공고 캐시·기출 · 18화면</span></div>
</div>''', source='FE 3255a69 · 3372511 · fff2768(네이버 소유 확인 08-21) · 7aa25dc · f42c9e7 · 67e5238 / BE 00a4c31 · 56c55b7 (운영 반영일 기준) · 도구별 숫자 차이는 부록 A4'))
S.note('''[≈12초] 다섯 번째, 그 외입니다. 개발 바깥에는 도구 여섯 개를 붙였습니다. GA4는 동의를 받은 사람의 퍼널, 구글 Search Console과 네이버 서치어드바이저는 각 검색엔진의 노출과 색인, Clarity는 행동, Sentry는 오류를 봅니다. 도구마다 숫자가 달라서, 숫자의 정본은 직접 만든 관리자 콘솔의 DB로 정했습니다.

출처: collect/A·metrics/README · GA4 동의 배너·처리방침 고지 3255a69(08-12) → Consent Mode v2 기본 denied 2ab4773(09-01 운영) · Clarity 7aa25dc(08-12, data-clarity-mask) · Sentry FE f42c9e7 → 1470a36(10-08) · 관리자 콘솔 FE 67e5238(08-28) · BE V45 llm_usage_event(56c55b7).
Q&A: GA는 하한(가입 이벤트 40 vs DB 83명) · GA 설정 감사 10항목은 제안 단계.''')

PARK.append(shell('Development · 그 외', 'Clarity로 <span class="red">가장 큰 이탈</span> 발견 — Instagram 인앱', f'''
<div class="panel" style="padding:26px 34px;flex:1;display:flex;flex-direction:column;min-height:0"><div class="small-copy" style="font-weight:900;color:var(--ink)">세션 1,000개당 가입 수 (괄호: Instagram 인앱 비중)</div>
{bars(['8월 (12%)', '9월 (91%)', '10월 (86%)', '11/1–4 (광고 중단)'], [15.0, 3.6, 2.2, 12.3], 1500, 520, colors=['#a79bfa', '#f22f46', '#f22f46', '#a79bfa'], fmt='{:.1f}', vmax=18, label_size=20, val_size=30)}
<div class="small-copy" style="font-size:20px;margin-top:10px">Instagram 인앱 유입 가입 전환 <b>0.10~0.15%</b> vs 그 외 <b>1.2~1.5%</b> — 약 <b>10배</b> 차이</div></div>''',
    source='방문: Microsoft Clarity (2026-08-01 ~ 11-04, 봇 제외) · 가입: 관리자 DB · 월 비교는 통제 실험이 아님 · 인앱 OAuth 제약: RFC 8252 §8.12 · Google 2021-09-30 웹뷰 OAuth 차단'))
PARK.note('''[≈15초] Clarity로 방문 2만 2천 명이 어디서 빠지는지 봤습니다. Instagram 인앱 브라우저로 들어온 사람의 가입 전환이 다른 유입의 약 10분의 1이었습니다. 광고를 멈춘 11월 1~4일에는 세션 1,000개당 가입이 12.3으로 8월 수준에 가까웠습니다.

출처: collect/D §1·§4 · 04-DB지표.md(세션 23,763 · instagram.com 20,025세션 · 인앱 86%). 방문 = Clarity, 가입 = 관리자 DB → 도구가 달라 «약»으로만. 8월은 팀·멘토 가입 포함, 11월은 표본 작음.
Q&A: 인앱 웹뷰에 GitHub 로그인 세션이 없어 OAuth에서 이탈한다는 건 추정 — 입증 아님, 정합적 가설. 근거는 RFC 8252 §8.12(웹뷰 OAuth 비권장)·Google 2021-09-30 웹뷰 OAuth 차단이고 GitHub에 특정된 근거는 없음. 우리 격차(약 10배)가 외부 인앱 전환 격차(1.4~3.4배, research/R3)보다 커서 OAuth 외 요인도 섞였을 수 있음 · 인앱 감지 코드는 아직 없음(다음 과제).''')

PARK.append(shell('Development · 그 외', 'GA4·Search Console로 본 것 — <span class="purple">모바일은 거의 움직이지 않음</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;margin:auto 0">
  {kpi('1.01 vs 0.12', '1인당 주요 이벤트 — 데스크톱 vs 모바일 (GA4)', '기기', 'soft', 'purple', 'padding:40px 44px')}
  {kpi('devfit뿐', '검색어가 사실상 브랜드 검색 하나 — 클릭 37 · 노출 88 (8/4~11/2) → 유입은 광고가 전부', '검색 (GSC)', '', '', 'padding:40px 44px')}
</div>''', source='GA4 9/1~11/3 (동의한 사용자 · 하한값) · Google Search Console 3개월 · metrics/README.md (11-04 조회)'))
PARK.note('''[≈10초] GA4로 보니 모바일 사용자 1인당 주요 이벤트가 데스크톱의 10분의 1이었습니다. 앞의 인앱 이탈과 같은 방향입니다. Search Console에서는 검색어가 사실상 우리 브랜드 이름 하나뿐이었습니다. 자연 검색 유입이 거의 없고, 유입은 광고가 전부라는 뜻입니다.

출처: metrics/README.md:27(07_device_gap) · :83(GSC 클릭 37 · 노출 88 · 브랜드 클릭 25/노출 57).
Q&A: 준비 카드 → 분석 시작 9월 88% → 10월 52%(p=0.017) · GA 실수집은 9/1부터 · GA4-GSC 연결 0건.''')

S.append(shell('Development · 그 외 - 발전과정 · 검색 노출', '구글에 <span class="red">0건</span>이던 사이트 — <span class="purple">알리는 일부터</span> 시작', psr(
    '<div class="dv-big rd">site: 0건</div><div class="dv-t">09-17 Google site:devfit.app 결과 0 · 브랜드 검색에도 안 나옴 — 원인은 코드가 아니라 구글에 알린 적이 없던 것</div>',
    li([('기술 SEO 기반', 'metadata · sitemap · robots · JSON-LD · llms.txt (07-27~)'), ('CS 지식백과 + 질문 색인', '「개발자 기술면접」 검색어 공략 · 875문항'), ('Search Console · 네이버 · IndexNow 제출', '08-21 네이버 소유 확인 · 09-17 IndexNow 209 URL · 09-18 sitemap 4종'), ('색인 대상 172편 → 55편', '11-05 본문 보강 · 나머지는 noindex · 11-06 재제출')]),
    '<div class="dv-big pu">SEO 100</div><div class="dv-t">Lighthouse 모바일 (Perf 99) · 09-17</div><div class="dv-big" style="margin-top:14px">색인 1 → 재측정</div><div class="dv-t">지금 색인은 홈 1페이지 · 11-05 재정비 효과는 2~3주 뒤 GSC로</div>'),
    source='GSC·curl 실측 (11-06) · FE 1891ad2 · fdcdd87 · 3832cea · 11505c1 · a4cda5a · 4f5aaf6 · #212→#218 (모두 origin/prod) · GSC 11-04 색인 1 / 미색인 224'))
S.note('''[≈12초] 9월 17일에 구글에서 우리 사이트를 검색하면 0건이었습니다. 코드 문제가 아니라 구글에 사이트를 알린 적이 없었습니다. 메타데이터와 sitemap, 구조화 데이터를 깔고, 「개발자 기술면접」 검색어를 노려 CS 지식백과를 만들고, Search Console과 IndexNow로 제출했습니다. 그래도 지금 색인은 홈 한 페이지입니다. 새 도메인이라 구글이 우선순위를 낮게 둔 것으로 보고, 172편을 55편으로 줄여 보강한 뒤 11월 6일에 다시 제출했습니다. 효과는 2~3주 뒤에 잽니다.

근거(seo 세션, git·curl·GSC 확인): 07-27 1891ad2 기반 · 08-20 fdcdd87(CsHub·구획 sitemap 3종)·3372511(검증 메타) · 09-16 3832cea(#73 타깃 메타·h1)·11505c1(#76 canonical → apex) · 09-17 a4cda5a(#80 질문 색인 875)·4f5aaf6(#83 도해 이미지 sitemap 49) · 11-03 OG 교체 · 11-05 #218 prod(sitemap-cs 193→76, 문서 186KB→117KB, /cs/feed.xml) · 11-06 GSC 재제출 feed 56·sitemap 93·sitemap-cs 76 «성공». GSC 11-04: 크롤 목적 신규 발견 4% / 새로고침 96%.
⛔ «devfit 검색 1위»·순위·노출 증가 주장 금지 — 측정값 없음. devfit.co가 같은 카테고리를 점유(동명). sameAs에 미확인 URL 금지.
Q&A: «결국 색인 1페이지?» → 맞다. 172편을 만들었지만 구글이 색인하지 않아 55편으로 줄이고 나머지는 noindex. 효과는 11월 말 재측정. · 운영 404가 아직 403(CloudFront 설정이 레포 밖 Terraform) · 네이버 서치어드바이저 새 sitemap 미재제출 · 명조 웹폰트 433KB(라이선스로 못 줄임) · 중복 주제 8쌍 301 미처리.''')

S.append(shell('Development · 그 외 - 발전과정 · 오류 수집', '오류는 Sentry로 모으고, <span class="purple">그 SDK로 무거워진 랜딩은 다시 경량화</span>', f'''
<div class="dv-vs">
  <div class="v before"><b>377KB</b><span>Sentry 도입 직후 랜딩 초기 JS (gzip)</span></div>
  <div class="arr">→</div>
  <div class="v after"><b>296KB</b><span>SDK 지연 로딩 후</span></div>
</div>
<div class="dv-q" style="text-align:center">FE·BE·분석 워커 오류를 한곳에 — 관리자 콘솔에서 바로 조회<small>도입 10-08 · 지연 로딩 10-12</small></div>''',
    source='FE f42c9e7 → prod 1470a36 (10-08) · 47e660b (10-12) · BE 00a4c31 · 5985868 · 관리자 조회 BE 6629aee · FE 5d17f02'))
S.note('''[≈8초] 10월 8일에 FE와 BE, 분석 워커까지 Sentry를 붙였습니다. 그런데 SDK 때문에 랜딩 초기 스크립트가 무거워져서, 지연 로딩으로 377KB를 296KB로 되돌렸습니다. 오류는 관리자 콘솔에서 바로 봅니다.

출처: collect/A §7-4 · docs/SENTRY.md(Tracing·Replay 끔).
Q&A: 14일 미해결 이슈 25개(BE 22 · FE 3), 대부분 10-28·11-04 두 번의 DB 연결 장애 — 원인 미확인(비밀번호 회전 추정). 10-08 이전은 오류 수집 공백.''')


PARK.append(shell('Development · 그 외', '내부 4명이 공고의 46% — <span class="purple">내부 계정을 빼고</span> 집계', f'''
<div class="dv-vs">
  <div class="v before"><b>46%</b><span>내부 4명이 만든 공고 비중<br>(답변은 63%)</span></div>
  <div class="arr">→</div>
  <div class="v after"><b>76%</b><span>내부를 뺀 가입자 79명 중<br>공고를 등록한 60명</span></div>
</div>''', source='관리자 DB (2026-11-05 조회) · 내부 = 팀원·테스트 계정 4개 · Effect 지표는 모두 내부 제외 기준'))
PARK.note('''[≈8초] 관리자 콘솔로 보니 팀원 네 명이 공고의 46%, 답변의 63%를 만들고 있었습니다. 그대로 두면 지표가 부풀려지니, 발표의 모든 숫자는 내부 계정을 뺀 값으로 셉니다. 그렇게 세도 가입자 79명 중 60명, 76%가 실제 공고로 준비를 시작했습니다.

출처: collect/A §2·§4(외부 79명 중 60명) · 04-DB지표.md.
Q&A: 대시보드 자체는 내부 계정을 뺄 수 없고 회원 목록 기준으로 뺀다 · 결제 0건.''')

# ───────────────── 수행과정 ─────────────────
DAYS = [('09-07 한유일 멘토', '모의면접 피드백 타임아웃', 0), ('09-22 CI/CD 멘토링', '배포 완료를 알림으로 받기', 0), ('11-02 멘토링', '기출 검색 하이브리드', 0),
        ('09-07 한유일 멘토', '쉬운 질문이 사실 확인뿐', 2), ('09-07 한유일 멘토', '음성으로 답하기', 9),
        ('08-07 자유 멘토링', '"연동하면 털리나" → 레포 범위 선택', 16), ('09-22 CI/CD 멘토링', '분석 실패 이유 안내', 27)]
drows = ''.join(f'<div class="row"><div class="who">{b}<small>{a}</small></div><div><div class="bar {"same" if d == 0 else ""}" style="width:{max(d/27*100, 3):.1f}%"></div></div><div class="d">{"당일" if d == 0 else f"{d}일"}</div></div>' for a, b, d in DAYS)
S.append(shell('Development · 수행과정', '피드백을 받은 날과 <span class="purple">운영에 반영한 날</span>이 가까움', f'<div class="dv-days">{drows}</div>',
    source='반영일 = 운영 브랜치 배포 기준 · 08-타임라인.md · 전체 간트는 부록 A13'))
S.note('''[≈12초] 멘토 피드백을 받은 날과 운영에 반영한 날입니다. 세 건은 당일, 쉬운 질문 문제는 2일, 음성은 9일 걸렸습니다. 가장 오래 걸린 실패 사유 안내도 27일입니다.

출처: 08-타임라인.md «피드백 → 반영 짝»(c5a3ac7 · 0770825 · c680990 · 32e25e9 · 98ebb0f · baebd8d · 741df1e).''')

S.append(shell('Development · 수행과정', '중간평가 심사의견 <span class="purple">19건 중 18건</span> 대응', '''
<div class="dv-big-one"><b>18 / 19</b><span>완료 5 · 부분 10 · 소명 3 · 미반영 1</span><small>미반영 1건(#15 대학 B2B2C)은 사유 기록 — 전체 표는 부록 A1</small></div>''',
    source='collect/I-feedback-patterns.md · 최종보고서 "중간점검 반영표"와 같은 분류'))
S.note('''[≈8초] 중간평가 심사의견 19건 중 18건에 대응했습니다. 미반영 1건은 대학 취업지원실 B2B2C인데, 대학 예산 주기와 연수 종료 시점이 맞지 않는다는 사유를 남겼습니다. 전체 표는 부록 A1에 있습니다.

출처: collect/I-feedback-patterns.md.''')


S.append(shell('Development · 수행과정', '출시 후 <span class="purple">14주 연속</span>, 매주 운영 배포', f'''
<div class="panel" style="padding:24px 32px;flex:1;display:flex;flex-direction:column;min-height:0">
  <div style="display:flex;justify-content:space-between"><div class="small-copy" style="font-weight:900;color:var(--ink)">주별 운영 배포 성공 횟수 (주 시작일) · 합계 <span class="purple">138회</span></div><div class="small-copy"><span style="color:#6c5ce7">■</span> FE  <span style="color:#a79bfa">■</span> BE</div></div>
  {bars(['8/3','8/10','8/17','8/24','8/31','9/7','9/14','9/21','9/28','10/5','10/12','10/19','10/26','11/2'], [[2,2],[6,4],[10,3],[3,4],[4,5],[4,3],[11,6],[2,3],[8,7],[5,5],[11,10],[1,3],[4,4],[4,4]], 1540, 500, stacked=['#6c5ce7', '#a79bfa'], label_size=17, val_size=20, vmax=24)}
</div>''', source='GitHub Actions prod 배포 성공 (2026-08-03 ~ 11-04) · collect/data/dora_prod_deploys_weekly.csv'))
S.note('''[≈10초] 출시 후 14주 동안 한 주도 빠짐없이 운영에 배포했습니다. 총 138회입니다.

출처: collect/B · dora_prod_deploys_weekly.csv. 본편에서 뺀 수치: 배포 실패율 14.3% → 1.7% · 자동 테스트 2,890개(BE 2,000 · FE 807 · E2E 83, 11-05) · 커밋 1,467개 중 중간평가 이후 919개(63%) · 운영 승격 PR 29 → 125.
⛔ «500회+» · «1,515» · «리드타임 단축» 금지.''')


# ================= 부록 (이 파트 담당) =================

MID19 = [("1", "늦은 피봇을 범위 축소로 만회(긍정)", "유지", "B2C 주축, B2B는 MVP. 운영 승격 PR 29 → 125"),
 ("2", "기능 확장보다 질문 품질과 기업 파일럿", "부분", "8축 평가 → 결함 31건 수정 → 난이도 분리 → v11~v13. 저난도 추론형 1/8 → 7/9. 파일럿 0건"),
 ("3", "커밋·diff 연결과 무근거 폐기(긍정)", "강화", "근거 대조·사유 코드 노출(10-19). 출처 353/353, 품질 필터 30일 84건"),
 ("4", "라벨·문항분석으로 정확성·변별도 검증", "부분", "3-state 라벨 UI 복구(09-08). 근거 특정성 81.9%. 변별도 실측 0건(표본 부족)"),
 ("5", "질문 품질 자동 검증", "완료", "평가 하네스(09-06): 8축 루브릭 · 결정적 지표 13개 · 회귀 게이트"),
 ("6", "설계·본인 작업 검증 등 의도별 질문", "완료", "의도 7유형, 난이도 분리, 본인 기여 필터(1.0 / 0.70 / 제외). 09-09 운영"),
 ("7", "코딩 외 전인적 역량 평가", "부분·소명", "자동 합불 금지선 → 준비 지원: 음성 모의면접, 자소서·포트폴리오 작업실, 블라인드 평가"),
 ("8", "기업 파일럿으로 채택률·절감 확인", "부분·착수", "기업 대표 서면 회신 1건, 리드 43사, 로드맵. 수치·LOI 없음"),
 ("9", "시장 분석 세밀화, 포커스 결정", "부분", "출처 등급제(인용 금지 6건 제거), B2C 신입·주니어 포커스"),
 ("10", "기존 취업 사이트 대비 우위", "부분", "공고 × 내 실제 코드. 근거 실존 28/28 vs 0/18"),
 ("11", "경쟁사 직접 사용", "부분", "직접 9 · 인접 43 · 모바일 12종 캡처. 유료 전체 플로우 기록 없음"),
 ("12", "B2C·B2B 동시 공략은 욕심", "소명", "투입은 B2C 집중, B2B는 같은 엔진 MVP"),
 ("13", "일정상 B2C 집중", "완료", "B2C 출시 → 음성 → 단건 결제 LIVE(11-02)"),
 ("14", "중견기업 타겟", "부분", "리드 규모 32~618명. 발송 전 미검증"),
 ("15", "대학 취업지원실 B2B2C", "미반영", "박람회 현장 마케팅만. 대학 예산 주기와 연수 종료 시점 불일치"),
 ("16", "시즌성 때문에 수익모델 재검토", "부분", "공고 단위 단건 1,900원 추가 · LIVE. 매출 0"),
 ("17", "질문 유출 플랫폼은 기업이 싫어함", "소명", "본인 코드 기반 · 지원서별 생성. B2B 커버리지 어시스턴트로 재정의"),
 ("18", "개인정보 보호조치", "부분", "토큰 AES-256-GCM, 세션 해시, numeric id 신원, 증분 동의, 블라인드 평가"),
 ("19", "개발·운영 환경 통합(비용)", "소명", "결제 TEST 격리 필요로 분리 유지. 원가의 94%가 LLM")]
BC = {'완료': 'green', '강화': 'green', '유지': 'neutral', '부분': '', '부분·소명': 'amber', '부분·착수': '', '소명': 'amber', '미반영': 'red'}
APX.append(shell('Appendix · A1', '중간평가 심사의견 19건 — 완료 5 · 부분 10 · 소명 3 · 미반영 1', table(['#', '심사의견', '구분', '조치'], [[a, b, badge(c, BC[c]), d] for a, b, c, d in MID19], 'xs left plain a1'), source='반영일·근거 커밋은 운영 브랜치 포함 여부 확인'))
APX.note('''출처: collect/I-feedback-patterns.md (반영일·근거 커밋은 운영 브랜치 포함 여부 확인). 최종보고서 «중간점검 반영표»와 같은 내용.
멘토 피드백 31행 표는 collect/I 원본 참조 — 필요 시 A1-2로 추가.''')

APX.append(shell('Appendix · A6', '최소 권한으로 연결하고, <span class="purple">토큰은 암호화</span>', table(['우려', '조치'], [
 ['"GitHub 연동하면 내 코드 털리나"', '기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의'],
 ['분석 범위', '분석할 레포를 사용자가 직접 선택 (08-07 피드백 → 08-23 반영)'],
 ['토큰 유출', 'GitHub access token AES-256-GCM 암호화 저장'],
 ['세션 탈취', '세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능 · HttpOnly 쿠키'],
 ['계정 선점', 'GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)'],
 ['공고 수집 경로 악용 (SSRF)', '홉마다 허용 목록을 다시 검사하는 SafeFetcher · 응답 8MB 상한'],
 ['B2B 지원자 정보', '블라인드 평가 · 지원 시 동의 2건 필수']], 'sm left plain')))
APX.note('''근거 코드: auth/GithubTokenCipher(AES-256-GCM) · user_session(SHA-256 해시) · V38 github_user_id · prep/corporate/SafeFetcher. 레포 범위 선택은 08-07 피드백 후 16일 만(08-23) 반영.''')

APX.append(shell('Appendix · A7', '분석 1회 약 133원, 단건 <span class="purple">1,900원</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px">{kpi('약 133원', '분석 1회 LLM 원가 ≈ $0.095 (단가 설정 호출 기준) · 미설정 호출 포함 추정 약 150원', '분석 1회', 'soft', 'purple')}{kpi('약 252원', '공고 1건 LLM 원가 — 원가의 81%가 학습 질문 생성', '공고 1건')}{kpi('94%', '전체 원가 중 LLM 비중 — 개발 DB·서버는 정지 운영', '원가 구조')}</div>
<div class="small-copy" style="margin-top:18px;font-size:23px">원가 산출: 08-15 손 곱셈(CloudWatch × DB × 요금표) → LLM 호출마다 원장 기록(V45·V46) + 콘솔 단가표(09-06) · 90일 5,391건</div>
<div style="margin-top:26px">{table(['상품', '가격', '상태'], [['Free', '무료 (사용 한도 있음)', '운영 중'], ['추가생성권 (공고 단위 단건)', '1,900원', '토스페이먼츠 LIVE (2026-11-02)'], ['Plus', '월 7,900원', '정기결제 심사 중 · 출시 기념 3개월 무료 개방'], ['B2B', '파일럿 후 결정', '콘솔 구현 완료 · 고객 0']], 'sm left plain')}</div>
<div class="callout" style="margin-top:20px">채용 시즌에만 사는 구조에 맞춰 월 구독 외에 <strong>공고 단위 단건 상품</strong> 추가 (중간평가 #16)</div>''', source='관리자 콘솔 LLM 호출 원장 (90일, 단가가 설정된 호출 2,881건 $32.77) · 분석 346회 · 공고 182건 · 1 USD = 1,400원'))
APX.note('''출처: collect/A §5. 133원 = $0.095 × 1,400원, 8/30~ 단가 설정 호출만. gpt-6-luna 2,349회(단가 미설정)를 glm-5 단가로 넣으면 분석당 약 150원(추정). 8월 330원과 «60% 절감» 비교 금지.
원가의 94%가 LLM(인프라는 개발 DB·서버 정지 운영). 작업별 비중: 학습 질문 생성 81% · 어필 포인트 약 12% · 꼬리질문 보정 약 5%, 모델로는 GLM-5가 약 99%. Plus 정기결제는 심사 중.
근거: docs/ops/llm-cost-model.md(08-15 수동 산출) · BE V45 56c55b7 · 단가표 08639f8(09-06). 🔴 gpt-6-luna 호출 ↔ 개인정보처리방침 8조 국외 이전 고지 확인.''')

APX.append(shell('Appendix · A8', '기출은 <span class="purple">공개 출처</span>만, 출처 URL과 함께 보존', f'''
<div class="panel apx-lg" style="padding:44px 50px">{ul(['운영: 공개 출처 URL 304개 · 41개사 · 853건 (사람 검수 진행 중)', '개발 DB: 2차 수집 1,073건 — 원문 대조 1,073/1,073 일치, 운영 반영 전', '수집 규칙: robots 확인 · 도메인당 1.5초 간격 · 원문 1회 캐시 · robots가 막은 사이트와 AI 수집을 막은 블로그 제외', '출처 URL을 질문과 함께 보존 · (URL + 원문) 해시로 중복 방지', '생성 프롬프트에 넣지 않고, 학습실 질문 옆에 비슷한 실제 기출로 출처와 함께 표시'])}</div>'''))
APX.note('''근거: interview-evidence-audit-2026-10-11 · production-upload-result-2026-10-11.json · Devfit/research/interview-evidence/reports/progress.md · docs/interview-question-evidence.md. 11-02 전략멘토링 대응 기록: «저작권·직업정보제공사업 문제로 공개 정보 위주로 간다».
⛔ «검증된 853건» 금지(REVIEWED 0 · NEEDS_REVIEW 158 · 302건은 주제 보고). 법적 검토 의견은 확보된 것이 없음.''')

team = [('박천웅', '팀장 · DevSecOps &amp; Full Stack', '인증·보안, AWS 인프라·CI/CD·운영 배포, FE·BE 통합, 결제·사업자 행정', 'team-park-cheonwoong.jpg'),
        ('김건우', 'PM &amp; Frontend', '문제 정의·제품 방향·BM, Next.js 프론트엔드(B2C·B2B·관리자 콘솔), 마케팅·유입 계측', 'team-kim-gunwoo.jpg'),
        ('노재원', 'Backend · Core Logic &amp; AI', 'GitHub 커밋 선별 알고리즘, 근거 묶음·질문 생성 핵심 로직, Spring Boot 백엔드', 'team-noh-jaewon.jpg')]
tc = ''.join(f'<div class="panel" style="padding:40px 32px;display:flex;gap:26px;align-items:center;min-height:300px"><img src="assets/{p}" alt="{n}" style="width:140px;height:140px;border-radius:50%;object-fit:cover"><div><div style="font-size:30px;font-weight:900">{n}</div><div class="badge" style="margin-top:8px">{r}</div><div class="small-copy" style="margin-top:14px;font-size:20px">{d}</div></div></div>' for n, r, d, p in team)
APX.append(shell('Appendix · A10', '세 명이 나눠 맡고, <span class="purple">게이트로 품질</span> 유지', f'''
<div style="display:flex;flex-direction:column;height:100%"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;flex:1.3">{tc}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:28px;flex:1">{kpi('2,890개', 'CI 자동 테스트 (BE 2,000 · FE 807 · E2E 83)', '테스트')}{kpi('13건 · 유출 0', 'staging → prod 승격 게이트가 막은 운영 push', '승격 게이트', 'soft', 'purple')}{kpi('72%', 'PR 본문에 검증 내역을 적은 비율', 'PR 기록')}</div></div>'''))
APX.note('''Q&A: PR 리뷰 0건·96% 작성자 병합 → «사람 승인 대신 CI와 승격 게이트로 막았다(운영 push 13건 차단, 운영 유출 0). PR 본문 72%에 검증 내역». ⛔ «공동대표» 금지.''')

# --- A12 모델 라우팅 · 스택 ---
APX.append(shell('Appendix · A12', '역할별 모델 라우팅과 <span class="purple">서비스 스택</span>', '''
<div class="hero" style="grid-template-columns:1.1fr .9fr;margin:auto 0">
  <div class="panel" style="padding:30px 34px"><div class="infra-summary-title">LLM · 역할별 라우팅 (Bedrock 5종 + 외부 2종)</div>
    <div class="mchips">
      <div><small>추론 · 질문 생성</small><b>GLM-5</b></div><div><small>코드 · 답변 피드백</small><b>Qwen3-Coder-Next</b></div><div><small>추출</small><b>GLM-4.7-Flash</b></div>
      <div><small>비전 · 공고 OCR</small><b>Nova 2 Lite</b></div><div><small>사업자 OCR</small><b>Qwen3-VL</b></div><div><small>커밋 판정</small><b>gpt-6-luna</b></div>
      <div><small>임베딩 · 기출 검색</small><b>Cohere Embed v3</b></div>
    </div></div>
  <div class="panel" style="padding:30px 34px"><div class="infra-summary-title">서비스 · 검색 · 음성</div>
    <div class="ilist"><div><small>FE</small>Next.js 16 정적 export → S3 + CloudFront</div><div><small>BE</small>Spring Boot 3.4 · Java 21 · ECS Fargate</div><div><small>큐</small>DB 큐 + 워커 원자 선점 · 지수 백오프</div><div><small>DB</small>PostgreSQL · Flyway · pgvector</div><div><small>음성</small>자체 음성 사이드카 (STT · TTS)</div></div></div>
</div>''', source='origin/prod application.yml bedrock.models.* · app.commit-decision · interview-evidence.vector (2026-11-06)'))
APX.note('''출처: origin/prod application.yml:103-127(bedrock.models reasoning/code/extraction/vision/business-ocr) · :336-354(커밋 판정 gpt-6-luna, OpenAI) · :167-169(cohere.embed-multilingual-v3) · BedrockService evaluateAnswer=code 모델.
🔴 OpenAI(커밋 판정 · 조건부 TTS) 호출이 개인정보처리방침 국외 이전에 미고지(R1) — 발표 전 정리. 음성 provider 운영값 확인 필요(s2 음성 장 노트).''')

# --- A13 전체 타임라인 (간트) ---
d0, d1 = dt.date(2026, 6, 29), dt.date(2026, 11, 6)
def X(m, d): return (dt.date(2026, m, d) - d0).days / (d1 - d0).days * 100
lanes = [('엔진·품질', 70), ('제품·인프라', 250), ('마케팅·사업', 430)]
evs = [(0, 6, 29, '개발 착수', '06-25 피봇 승인'), (0, 9, 6, '평가 하네스 도입', ''), (0, 9, 9, '난이도·유형 분리', '← 09-07 한유일 멘토 (2일)', 82), (0, 10, 8, '실기업 기출 운영', '853건 · 41개사'),
       (1, 8, 3, 'B2C 출시', '첫 운영 배포'), (1, 8, 23, '레포 범위 선택', '← 08-07 "연동하면 털리나" (16일)'), (1, 9, 16, '음성 모의면접', '운영 반영'), (1, 9, 22, '비동기 배포·Slack', '← 09-22 멘토링 (당일)', 82), (1, 11, 2, '결제 LIVE · 기출 검색', '← 11-02 멘토링 (당일)'),
       (2, 8, 24, 'Google 광고 시작', ''), (2, 9, 3, '사업자등록', '도저랩스'), (2, 10, 15, '토스페이먼츠 TEST 결제 연동', ''), (2, 11, 1, '특허 3건 출원', '')]
g = ['<div class="gantt dv-gantt">']
for m, lab in [(7, '7월'), (8, '8월'), (9, '9월'), (10, '10월'), (11, '11월')]:
    g.append(f'<div class="month" style="left:calc(220px + (100% - 300px) * {X(m,1)/100:.4f})">{lab}</div>')
for name, top in lanes:
    g.append(f'<div class="lane" style="top:{top}px"></div><div class="lane-name" style="top:{top+14}px">{name}</div>')
for e in evs:
    li_, m, d, t, c = e[:5]
    top = lanes[li_][1] + 30 + (e[5] if len(e) > 5 else 0)
    cc = f'<div class="c">{c}</div>' if c else ''
    g.append(f'<div class="ev" style="left:calc(220px + (100% - 300px) * {X(m,d)/100:.4f});top:{top}px"><span class="d">{m:02d}-{d:02d}</span><div class="t">{t}</div>{cc}</div>')
g.append(f'<div class="mid" style="left:calc(220px + (100% - 300px) * {X(8,20)/100:.4f});top:40px;bottom:0"><span>★ 08-20 중간평가 · 피드백 19건</span></div></div>')
APX.append(shell('Appendix · A13', '전체 타임라인 — 06-29 착수부터 <span class="purple">11-06</span>까지', f'''
<div class="panel" style="padding:30px 40px 20px;flex:1;display:flex;flex-direction:column;min-height:0">{''.join(g)}</div>''', source='2026-06-29 ~ 11-06 · 운영 반영일은 운영 브랜치 배포 기준 · 08-타임라인.md'))
APX.note('''출처: 08-타임라인.md · collect/B. 사업자등록 푸터 고지 커밋 7050d0a. 기출 운영 반영 10-08 PR #89(10-11은 정제 갱신). ⛔ «공동대표» 금지.''')

APX.append(shell('Appendix · A14', 'staging을 거치지 않은 변경은 <span class="purple">운영에 나가지 않음</span>', f'''
<div class="hero" style="grid-template-columns:1.25fr .75fr;margin:auto 0">
  <div class="panel dep">
    <div class="fb2-k">배포 경로 — 숫자는 게이트가 실제로 막은 횟수</div>
    <div class="dp">
      <div><b>기능 브랜치 → main</b><span>테스트 · FE↔BE API 계약 대조</span><em>112회</em></div><i>↓</i>
      <div><b>staging → prod PR</b><span>head가 staging인가</span><em>18회</em></div><i>↓</i>
      <div class="on"><b>prod push</b><span>병합된 승격 PR 확인 · 개발 문서 유출 차단</span><em>13회</em></div><i>↓</i>
      <div><b>운영 배포</b><span>GitHub Actions(OIDC) → AWS · Slack 알림</span></div>
    </div>
  </div>
  <div class="dv-big-one" style="margin:auto 0"><b style="font-size:130px">0건</b><span>막힌 13건 중 운영에 나간 변경</span></div>
</div>''', source='GitHub Actions 실패 실행 140건 jobs API 집계 (collect/B §6) · 13건 = 승격 11 · 유출 1 · 테스트 1 · 테스트 112회는 FE·BE 합산'))
APX.note('''배포 경로마다 게이트가 있습니다. main에서 112번, prod PR에서 18번, 운영 push 직전에 13번 막았고, 그 13건 중 운영에 나간 변경은 0건입니다.

출처: collect/B §6(scripts/gates.py). 배포 잡 429–488초 → 145–260초는 같은 기간 실측일 뿐 원인 단정 금지.
⛔ «SBOM 차단» 금지(main에만 있고 운영 미반영). Q&A: PR 리뷰 0건·96% 작성자 병합 → 사람 승인 대신 CI·승격 게이트, PR 본문 72%에 검증 내역.''')
