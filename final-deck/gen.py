# -*- coding: utf-8 -*-
# 최종발표 덱 조립기 — 섹션 파일을 순서대로 합쳐 index.html을 만든다.
# 🔒 관리: ppt-start 세션. 섹션 내용은 각 파일에서 고친다 (이 파일은 건드리지 않는다).
#   core.py       공용 CSS·헬퍼            ppt-start
#   s1_intro.py   본편 1부 + 부록 A2·A3     ppt-start
#   s2_dev.py     Development + A1·A6·A7·A8·A10   ppt-dev
#   s3_effect.py  Effect + A4·A5·A9         ppt-effect
#   s4_closing.py 마무리·감사·부록 목차      ppt-start
#   s5_appendix.py 부록 A1~A14 전체           ppt-start (11-07~)
# 미리보기: python3 gen.py && open -a "Google Chrome" index.html   (PDF/PPTX까지는 build/build.sh)
import os, re, sys, html as _html, importlib
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import core
SECTIONS = ['s1_intro', 's2_dev', 's3_effect', 's4_closing', 's5_appendix']

main, apx, css = [], [], []
for name in SECTIONS:
    m = importlib.import_module(name)
    css.append(f'/* ---- {name} ---- */\n' + getattr(m, 'CSS', ''))
    for lst, dst in ((m.S, main), (m.APX, apx)):
        for i, h in enumerate(lst):
            dst.append((name, h, lst.notes.get(i, '')))

def akey(h):
    k = re.search(r'<div class="eyebrow">Appendix · A(\d+)', h[1])
    if not k: sys.exit(f'부록 장표에 «Appendix · A<n>» eyebrow가 없음: {h[0]}')
    return int(k.group(1))
apx.sort(key=akey)
dup = [k for k in {akey(a) for a in apx} if [akey(a) for a in apx].count(k) > 1]
if dup: sys.exit(f'부록 A번호 중복: {dup}')

slides = []
for n, (name, h, note) in enumerate(main + apx, 1):
    h = re.sub(r'data-order="\d+"', f'data-order="{n}"', h, count=1)
    # 장표 오른쪽 하단 출처 줄은 화면에서 지우고 발표자 노트 끝으로 옮긴다 (사용자 지시 2026-11-06)
    srcs = [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(r'<div class="source">([\s\S]*?)</div>', h)]
    h = re.sub(r'<div class="source">[\s\S]*?</div>', '', h)
    srcs = [_html.unescape(x) for x in srcs if x]
    if srcs:
        note = (note + '\n\n' if note else '') + '[장표 출처 — 화면에서는 뺌] ' + ' / '.join(srcs)
    if note:
        h = h[:h.rindex('</section>')] + f'<template class="notes">{_html.escape(note, quote=False)}</template></section>'
    slides.append(h)

# 부록 목차의 {{PAGE:A<n>}} 자리를 실제 쪽번호로 채운다 (Dev·Effect 장 수가 바뀌어도 자동)
_apage = {f'A{akey(a)}': len(main) + i for i, a in enumerate(apx, 1)}
slides = [re.sub(r'\{\{PAGE:(A\d+)\}\}', lambda m: f'p{_apage[m.group(1)]}', h) for h in slides]
if any('{{PAGE:' in h for h in slides): sys.exit('부록 목차 쪽번호 치환 실패')

page = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#121016"><title>DevFit 최종발표 — Team Dozer</title>
<style>{core.CSS}{core.EXTRA}{chr(10).join(css)}</style></head><body>
<noscript><style>.slide:first-of-type{{display:block}}</style></noscript>
<div id="progress"></div><main id="stage" aria-live="polite">
{chr(10).join(slides)}
</main>
<nav id="hud" aria-label="슬라이드 탐색"><button id="prev" type="button" aria-label="이전 슬라이드">‹</button><span id="counter">1 / 1</span><button id="next" type="button" aria-label="다음 슬라이드">›</button><button id="fullscreen" type="button" aria-label="전체 화면">⛶</button></nav>
{core.JS}
</body></html>'''
tmp = core.OUT + f'.{os.getpid()}.tmp'
open(tmp, 'w', encoding='utf8').write(page); os.replace(tmp, core.OUT)
cnt = {}
for name, *_ in main: cnt[name] = cnt.get(name, 0) + 1
print('slides', len(slides), '· 본편', len(main), cnt, '· 부록', len(apx))
