# -*- coding: utf-8 -*-
# 4부 — 마무리 · 감사합니다 · 부록 목차
# 담당: ppt-start · 공용 헬퍼/CSS는 core.py (ppt-start 관리) — 고칠 일이 있으면 ppt-start에 요청
# 장표 추가: S.append(shell(...)) 다음 줄에 S.note('''발표자 노트''') · 부록은 APX.append(shell('Appendix · A<n>', ...))
# 이 파일 전용 CSS는 아래 CSS 문자열에 넣는다 (클래스 이름 앞에 접두사 권장: cl-)
from core import *

S = Slides()    # 본편 — 이 파일 순서 그대로 들어간다
APX = Slides()  # 부록 — A번호 순으로 자동 정렬
CSS = r""".cl-idx{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}.cl-idx td{padding-top:5px;padding-bottom:5px;line-height:1.25}.cl-idx th{padding-top:6px;padding-bottom:6px}.cl-q{color:var(--muted,#777);font-size:.85em}

"""

# ================= 마무리 =================
S.append(raw('dark-slide', f'''<div class="dark-grid"></div><div class="slide-shell" style="padding:0">
<div style="position:absolute;inset:0;display:grid;grid-template-columns:58% 42%">
  <div style="padding:0 0 0 118px;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2">
    <div style="font-size:28px;color:#9c96a3;font-weight:700;margin-bottom:30px">05 · 마무리</div>
    <h1 style="margin:0;color:#fff;font-size:66px;font-weight:900;line-height:1.35;letter-spacing:-.055em">AI가 만든 면접 질문을,<br><span style="color:#b9b0ff">지원자 본인의 코드</span>로 증명하고<br>숫자로 검증</h1>
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
S.note('''[14:50–15:00] DevFit은 AI가 만든 면접 질문을, 지원자 본인의 코드로 증명하고 숫자로 검증합니다. 감사합니다.

테스트 계정은 GitHub OAuth 전용이라 심사위원용 계정 필요 — 제출 전 시크릿 창에서 로그인 재확인.''')

S.append(raw('', '''<div class="slide-shell"><div class="slide-content" style="margin:0;align-items:center;justify-content:center">
<img src="assets/Dozer_일러스트.png" alt="팀 Dozer" style="width:980px;max-width:74%;display:block;margin-top:-40px">
<div style="font-size:48px;font-weight:900;letter-spacing:-.045em;margin-top:-150px">감사합니다</div>
<div class="small-copy" style="font-size:22px;margin-top:14px">팀 Dozer, 박천웅, 김건우, 노재원 · Q&amp;A</div></div><div class="folio"></div></div>''', '감사합니다'))
S.note('''Q&A로 넘어갑니다. 부록은 쪽번호로 바로 엽니다(맨 뒤 부록 목차).''')

# ================= 부록 =================
apx = [('A1', '중간평가 심사의견 19건 반영표'), ('A2', '범용 AI 비교 실험 · 유사 서비스'), ('A3', '평가 하네스 상세'), ('A4', '측정 도구별 수치 차이'), ('A5', '유료 광고 집행과 효율'), ('A6', '원가와 가격'), ('A7', '기출 데이터 수집'), ('A8', '특허 3건'), ('A9', '팀 역할 · 품질 보증'), ('A10', '시장 규모 상향식 계산'), ('A11', '모델 라우팅 · 서비스 스택'), ('A12', '배포 게이트'), ('A13', '현업 검토 · 멘토 피드백 반영'), ('A14', '공고 수집과 캐시 구조'), ('A15', '공고 캐시 발전과정'), ('A16', '오류 수집 (Sentry)'), ('A17', '검색 노출 (SEO)'), ('A18', '서비스 보안'), ('A19', '커밋 선별 발전과정'), ('A20', '질문 생성 호출 분할 · 난이도 세부'), ('A21', '자기소개서와 포트폴리오')]
qs = ['멘토·심사 의견을 어떻게 반영했나', '범용 AI랑 뭐가 다른가', '품질을 어떻게 믿나', 'GA는 235명인데 왜 2.2만인가', '마케팅 효율은', '돈은 어떻게 버나', '크롤링 문제없나', '특허는 뭘 보호하나', '누가 뭘 했나 · 리뷰는', '시장 숫자는 어떻게 나왔나', '어떤 모델을 왜 쓰나', '검증 안 된 코드가 운영에 나가나', '현업은 써 보고 뭐라 했나', '공고는 어떻게 가져오나', '같은 공고를 매번 다시 분석하나', '오류는 어떻게 아나', '검색 유입은 어떻게 만드나', 'GitHub 토큰과 세션은 안전한가', '커밋 선별은 어떻게 바뀌었나', '질문 생성은 어떻게 나눠 부르나', '면접 말고 또 뭘 하나']
_rows = [[f'<b style="color:var(--purple)">{{{{PAGE:{a}}}}}</b> <span class="cl-q">{a}</span>', f'{b}<br><span class="cl-q">{q}</span>'] for (a, b), q in zip(apx, qs)]
S.append(shell('Appendix', '부록 목차', '<div class="cl-idx">' + table(['쪽', '장표 · 예상 질문'], _rows[:11], 'left plain') + table(['쪽', '장표 · 예상 질문'], _rows[11:], 'left plain') + '</div>'))
S.note('''Q&A 때 쪽번호로 이동. 답변 원고: collect/00-통합보고.md §3.''')
