# -*- coding: utf-8 -*-
# 2부 — Development (기술 · 수행과정) + 부록 A1·A6·A7·A8·A10
# 담당: ppt-dev · 공용 헬퍼/CSS는 core.py (ppt-start 관리) — 고칠 일이 있으면 ppt-start에 요청
# 장표 추가: S.append(shell(...)) 다음 줄에 S.note('''발표자 노트''') · 부록은 APX.append(shell('Appendix · A<n>', ...))
# 이 파일 전용 CSS는 아래 CSS 문자열에 넣는다 (클래스 이름 앞에 접두사 권장: dv-)
from core import *

S = Slides()    # 본편 — 이 파일 순서 그대로 들어간다
APX = Slides()  # 부록 — A번호 순으로 자동 정렬
CSS = r"""
"""

# ================= 3. 개발 =================
S.append(divider('03 · 개발', 'Development', '방금 본 화면의 뒷면 — 기술과 수행과정'))
S.note('''[구분] Development — 기술 → 수행과정 순서로 넘어갑니다.''')

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
S.note('''[8:20–8:40] 공고와 레포를 수집하고, 규칙 점수로 본인 커밋을 고르고(커밋 판정 모델은 섞기만 하고) 근거로 묶은 다음, 게이트를 통과한 질문만 내보냅니다. LLM은 역할별 5개 모델로 나눠 쓰고, 분석은 DB 큐와 워커로 비동기 처리합니다.

그림: 운영 브랜치 기준 시스템 구성도(2026-11-03, 최종보고서 그림 1과 동일).
모델: Bedrock reasoning GLM-5 · code Qwen3-Coder-Next · extraction GLM-4.7-Flash · vision Nova 2 Lite · business-ocr Qwen3-VL / 임베딩 Cohere Embed Multilingual v3 / 커밋 근거 가치 판정 OpenAI gpt-6-luna.
🔴 OpenAI 호출이 개인정보처리방침 국외 이전에 미고지(R1) — 발표 전 정리.''')

# ---------- 3.2 funnel ----------
S.append(shell('Development', '커밋 1,000개를 질문 4개까지 <span class="purple">좁혀서</span> 넣습니다', f'''
{sb(('1,000개', '한 레포에서 읽는 커밋 — 전부 LLM에 넣으면 문맥·원가를 감당 못 함'), '규칙 점수로 4단 압축한 <b>뒤에만</b> 질문 생성', ('≤ 4', '작업당 질문'))}
<div class="panel funnel">
  <div class="fr"><div class="fb" style="width:100%"><b>커밋 최대 1,000</b><span>내가 쓴 커밋 · PR만</span></div><div class="ft"></div></div>
  <div class="fr"><div class="fb" style="width:72%"><b>diff 최대 96</b><span>로직 밀도 · 기술 키워드 · 시간 분산</span></div><div class="ft"></div></div>
  <div class="fr"><div class="fb" style="width:48%"><b>작업 단위 4~10</b><span>질문 가치가 높은 묶음</span></div><div class="ft g"><b>입력 게이트</b>근거가 얇으면 «왜»·«트레이드오프»만</div></div>
  <div class="fr"><div class="fb on" style="width:30%"><b>작업당 질문 ≤ 4</b><span>의도 7유형 × 난이도</span></div><div class="ft g"><b>출력 게이트</b>식별자 대조 → 유지 · 재질의 · 폐기 (p5)</div></div>
</div>''', source='B2C 분석 경로 기준 · 각 단계 값은 상한 · 막대 길이는 개념 표현(비례 아님)'))
S.note('''[8:40–9:00] 커밋 최대 1,000개에서 diff 96개, 작업 단위 4~10개로 좁힌 뒤 작업당 질문을 최대 4개 만듭니다. 압축의 뼈대는 규칙 점수이고, 커밋 판정 모델은 섞기만 합니다. 모델이 실패해도 규칙식만으로 끝까지 돕니다. 앞뒤에 게이트가 있습니다.

출처: collect/C (B2C 경로). 규칙 점수 = 로직 밀도·기술 키워드·시간 희소성.
⛔ «1,000 → 12 → 6»은 B2B 경로 숫자 — 이 장표에 쓰지 않음.
Q&A: 입력 게이트 실발동은 THIN 3/227로 적음 → «출력 게이트·운영 품질 필터(30일 84건)로 답».''')

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
S.note('''[9:00–9:10] 커밋을 고르는 점수식입니다. 잡음 커밋을 빼고, 메시지를 기술 키워드와 구체성으로 순위를 매긴 뒤, 커밋 판정 모델 점수를 섞습니다. 모델이 없거나 늦거나 절반도 채점하지 못하면 규칙식만으로 끝까지 갑니다. 동점은 sha 순서로 깨서 같은 입력이면 같은 순서가 나옵니다.

근거: 운영 브랜치 GithubService.orderCommitProbes · CommitDecisionBlend · application.yml(keyword 0.40 / specificity 0.60 / message-weight 0.6 / patch-weight 0.5, repo-deadline 25초, MIN_COVERAGE 0.5). 패치 판정은 품질 점수를 0.5~1.5배로 조정.
⛔ «커밋 선별 LLM 0회» 금지 — 운영은 OpenAI gpt-6-luna 판정을 섞는다(R1 국외 이전 고지 확인).
Q&A: 왜 모델 비중 0.6? → 설정값이고 실패 시 규칙식으로 떨어지는 구조가 핵심. 가중치 근거 실험은 diagnostics 로그.''')

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
S.note('''[9:10–9:20] 공고는 29곳에서 받습니다. 기업 채용 사이트는 사이트 하나가 클래스 하나이고, 등록은 한 줄입니다. 모든 접속은 SafeFetcher를 거쳐 리다이렉트마다 허용 호스트를 다시 검사합니다. 이미지로만 된 공고는 OCR로 읽고, 접수 중 공고는 미리 캐시해 두어 다시 들어오면 네트워크도 LLM도 부르지 않습니다.

근거: prep/corporate(CorporateSite 인터페이스, CorporateSiteRegistry, SafeFetcher, CorporateSiteSourceRulesTest가 Jsoup.connect 0건 잠금) · prep/cache(V59~V60, TTL 30일, 일일 LLM 1,000·OCR 300). OCR 폴백은 본문 200자 미만일 때만.
⛔ 회사 로고·«제휴» 표현 금지 — 회사명도 장표에 넣지 않음. ⛔ «공고 1,450건 사전 수집» 본편 금지.''')

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
S.note('''[9:20–9:35] 질문 생성 단계를 93.7초에서 49.1초로 줄였습니다. 품질은 평가 하네스로 잽니다. 그런데 심판 모델만 바꿔도 같은 문항 점수가 17.8점 흔들렸습니다. 그래서 LLM 심판 점수가 아니라 우연 대비 정답률 81.9%를 지표로 씁니다.

출처: collect/C — 속도 = 질문 생성 단계, 사례 3개 × 2회 평균 / 17.8점 = Kimi·DeepSeek 문항별 차 평균 17.82점(n=91), 같은 심판 재채점 차 12.23점(n=24).
Q&A: v11→v13 QI 하락 → 심판 교체만으로 17.8점이 흔들려 QI를 개선 지표로 안 쓴다.''')

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
S.note('''[9:35–9:50] 공개 출처 304개에서 실기업 기출을 모아 pgvector로 검색해 붙입니다(11-02 운영). 음성 모의면접은 16kHz 음성을 Transcribe 스트리밍으로 받아 적고, 꼬리질문을 음성으로 되묻습니다(09-16 운영).

출처: collect/B·08-타임라인. 특허 10-2026-0214811 «음성 대화 기반 면접 답변 평가 방법 및 시스템».
⛔ «검증된 853건» 금지 · 자체 음성 모델 주장 금지. Q&A: 음성 완료 0건(시작 18) → 완주가 다음 병목.''')

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
S.note('''[9:50–10:00] 배포 경로마다 게이트가 있습니다. main에서는 테스트와 FE·BE API 계약 대조가 112번 막았고, prod PR은 head가 staging인지 검사해 18번 막았습니다. prod push에서는 병합된 staging→prod PR이 없으면 배포 전에 멈춥니다. 이렇게 배포 직전에 막힌 운영 push가 13건이고, 그중 실제로 운영에 나간 변경은 0건입니다.

출처: collect/B §6(실패 실행 140건 jobs API, scripts/gates.py). 13건 = 승격 11 + 유출 1 + 테스트 1. 배포 잡 429–488초 → 145–260초는 같은 기간 실측일 뿐 원인 단정 금지.
⛔ «SBOM 차단» 금지(main에만 있고 운영 미반영).''')

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
S.note('''[10:00–10:10] LLM 호출마다 모델 단가와 토큰을 원장에 남겨서 원가를 셉니다. 분석 1회 약 133원, 공고 1건 약 252원이고 단건 가격은 1,900원입니다. 원가의 81%가 학습 질문 생성, 모델로는 GLM-5가 약 99%입니다.

출처: collect/A §5. 90일 원장 5,391건(성공 99.3%), 단가 설정 호출 2,881건 $32.77, 분석 346회 · 공고 182건, 1 USD = 1,400원. 하한값: 단가 미설정 gpt-6-luna 2,349건 포함 시 분석 1회 약 150원 추정. 원가의 94%가 LLM.
⛔ 8월 330원 대비 «60% 절감» 금지(정의 다름).
Q&A: 마진? → 원가 대비 가격이 10배 이상이지만 인프라·결제 수수료 별도.''')

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
S.note('''[10:10–10:40] 6월 29일 착수, 8월 3일 첫 운영 배포, 8월 20일 중간평가에서 피드백 19건을 받았습니다. 그 뒤로 피드백이 들어오면 며칠 안에, 어떤 건 당일에 운영에 반영했습니다.

출처: 08-타임라인.md · collect/B. 사업자등록 푸터 고지 커밋 7050d0a.
비주얼 의도: 4단계(착수–출시–중간평가–고도화) × 레인 3개 간트로 디자인. 표의 «레인» 열이 그대로 레인 배치.
⛔ «공동대표» 금지.''')

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
S.note('''[10:40–11:20] 대표 사례 세 가지입니다. 한유일 멘토가 «쉬운 질문이 코드 사실 확인뿐»이라고 지적했고, 원인은 난이도와 질문 유형이 1:1로 묶여 있던 것이었습니다. 이를 분리하고 2일 만에 운영에 반영했고, 쉬운 질문 9개 중 7개가 추론형이 됐습니다. 중간평가 심사의견 19건 중 18건에 대응했고, 전체 표는 부록 A1에 있습니다.

출처: collect/I-feedback-patterns.md · collect/C (1/8 → 7/9, 단일 레포 1회 — 분모 표기 필수).
🔴 한유일 멘토 실명 동의 확인. ⛔ «12% → 78%» 금지(분모 표기로). 와이어프레임의 «당일 반영 3건»은 멘토 피드백 기준이라 중간평가 19건과 섞이지 않게 뺌.''')

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
S.note('''[11:20–11:50] 출시 후 14주 동안 한 주도 빠짐없이 운영에 배포했습니다. 총 138회입니다. 배포 실패율은 14.3%에서 1.7%로 떨어졌고, 승격 게이트가 운영 push 13건을 막아 운영 유출은 0건입니다. 자동 테스트는 2,890개, 커밋의 63%가 중간평가 이후입니다.

출처: collect/B · collect/data/dora_prod_deploys_weekly.csv (GitHub Actions prod 배포 성공, 08-03~11-04). 테스트 2,890 = BE 2,000 · FE 807 · E2E 83 (2026-11-05).
⛔ «500회+» · «1,515» · «리드타임 단축» 금지. Q&A: PR 리뷰 0건 → 사람 승인 대신 CI·승격 게이트(13건 차단), PR 본문 72%에 검증 내역.''')

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
S.note('''[11:50–12:10] 현업 개발자이신 한유일 멘토는 중간·어려움 질문을 «충분히 괜찮다»고 평가했습니다. IT 기업 대표는 «왜 그 기술을 선택했는지, 그 선택이 최선이었는지를 묻는다»고 답했는데, 이게 우리 «결정 이유» 질문 유형입니다. 같은 분의 반론 «Claude Code에 넘기면 된다»는 앞의 실험으로 답했습니다.

출처: collect/D V1(09-07 녹취) · 대표 서면 회신 원문(10-26, 캡처는 이름·회사·메일 주소를 잘라냄).
김종욱 멘토(10-25): 발언 기록 0건 → 기록 확보 시에만 추가, 지어내지 않음.
🔴 실명 동의: 한유일 멘토 · 기업 대표.''')

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
S.note('''[12:10–12:30] 가장 큰 이탈은 방문에서 가입입니다. 원인을 좁혀 보니 Instagram 인앱 브라우저로 들어온 사람의 가입 전환이 다른 유입의 약 10분의 1이었습니다. 광고를 멈춘 11월 1~4일에는 세션 1,000개당 가입이 12.3으로 8월 수준에 가까웠습니다.

출처: collect/D §1·§4. 방문 = Clarity(봇 제외), 가입 = 관리자 DB → 도구가 달라 0.4%는 «대략»으로만. 월 비교는 자연 실험(통제 실험 아님), 8월은 팀·멘토 가입 포함, 11월은 표본 작음.''')

# ================= 부록 (이 파트 담당) =================

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
APX.append(shell('Appendix · A1', '중간평가 심사의견 19건 — 완료 5 · 부분 10 · 소명 3 · 미반영 1', table(['#', '심사의견', '구분', '조치'], [[a, b, badge(c, BC[c]), d] for a, b, c, d in MID19], 'xs left plain a1'), source='반영일·근거 커밋은 운영 브랜치 포함 여부 확인'))
APX.note('''출처: collect/I-feedback-patterns.md (반영일·근거 커밋은 운영 브랜치 포함 여부 확인). 최종보고서 «중간점검 반영표»와 같은 내용.
멘토 피드백 31행 표는 collect/I 원본 참조 — 필요 시 A1-2로 추가.''')

APX.append(shell('Appendix · A6', '최소 권한으로 연결하고, <span class="purple">토큰은 암호화</span>합니다', table(['우려', '조치'], [
 ['«GitHub 연동하면 내 코드 털리나»', '기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의'],
 ['분석 범위', '분석할 레포를 사용자가 직접 선택 (08-07 피드백 → 08-23 반영)'],
 ['토큰 유출', 'GitHub access token AES-256-GCM 암호화 저장'],
 ['세션 탈취', '세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능 · HttpOnly 쿠키'],
 ['계정 선점', 'GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)'],
 ['공고 수집 경로 악용 (SSRF)', '홉마다 허용 목록을 다시 검사하는 SafeFetcher · 응답 8MB 상한'],
 ['B2B 지원자 정보', '블라인드 평가 · 지원 시 동의 2건 필수']], 'sm left plain')))
APX.note('''근거 코드: auth/GithubTokenCipher(AES-256-GCM) · user_session(SHA-256 해시) · V38 github_user_id · prep/corporate/SafeFetcher. 레포 범위 선택은 08-07 피드백 후 16일 만(08-23) 반영.''')

APX.append(shell('Appendix · A7', '분석 1회 약 130원대, 단건 <span class="purple">1,900원</span>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px">{kpi('약 130원대', '분석 1회 LLM 원가 ≈ $0.095 (단가 설정 호출 기준) · 미설정 호출 포함 추정 약 150원', '원가', 'soft', 'purple')}{kpi('94%', '전체 원가 중 LLM 비중 — 개발 DB·서버는 정지 운영', '원가 구조')}</div>
<div style="margin-top:26px">{table(['상품', '가격', '상태'], [['Free', '무료 (사용 한도 있음)', '운영 중'], ['추가생성권 (공고 단위 단건)', '1,900원', '토스페이먼츠 LIVE (2026-11-02)'], ['Plus', '월 7,900원', '정기결제 심사 중 · 출시 기념 3개월 무료 개방'], ['B2B', '파일럿 후 결정', '콘솔 구현 완료 · 고객 0']], 'sm left plain')}</div>
<div class="callout" style="margin-top:auto">채용 시즌에만 사는 구조에 맞춰 월 구독 외에 <strong>공고 단위 단건 상품</strong>을 추가했습니다 (중간평가 #16)</div>''', source='관리자 콘솔 LLM 호출 원장(2026-08-30~) · 1 USD = 1,400원'))
APX.note('''출처: collect/A §5. 133원 = $0.095 × 1,400원, 8/30~ 단가 설정 호출만. gpt-6-luna 2,349회(단가 미설정)를 glm-5 단가로 넣으면 분석당 약 150원(추정). 8월 330원과 «60% 절감» 비교 금지.
원가의 94%가 LLM(인프라는 개발 DB·서버 정지 운영). Plus 정기결제는 심사 중.''')

APX.append(shell('Appendix · A8', '기출은 <span class="purple">공개 출처</span>만, 출처 URL과 함께 보존합니다', f'''
<div class="panel apx-lg" style="padding:44px 50px">{ul(['수집 대상: 공개된 면접 후기·기출 출처 304개', '출처 URL을 질문과 함께 보존해 원문을 확인할 수 있게 함', '공개 정보 위주 수집 — 비공개·로그인이 필요한 자료는 수집하지 않음', '원문을 그대로 노출하지 않고, 지원자 코드 질문의 맥락 보강에 사용'])}</div>'''))
APX.note('''근거: 기출 RAG 11-02 운영(공개 출처 304개). 11-02 전략멘토링 대응 기록: «저작권·직업정보제공사업 문제로 공개 정보 위주로 간다».
⛔ «검증된 853건» 금지(승인 0건). 법적 검토 의견은 확보된 것이 없음 → 【】 칸은 확보 시에만 채우고, 없으면 삭제.''')

team = [('박천웅', '팀장 · DevSecOps &amp; Full Stack', '인증·보안, AWS 인프라·CI/CD·운영 배포, FE·BE 통합, 결제·사업자 행정', 'team-park-cheonwoong.jpg'),
        ('김건우', 'PM &amp; Frontend', '문제 정의·제품 방향·BM, Next.js 프론트엔드(B2C·B2B·관리자 콘솔), 마케팅·유입 계측', 'team-kim-gunwoo.jpg'),
        ('노재원', 'Backend · Core Logic &amp; AI', 'GitHub 커밋 선별 알고리즘, 근거 묶음·질문 생성 핵심 로직, Spring Boot 백엔드', 'team-noh-jaewon.jpg')]
tc = ''.join(f'<div class="panel" style="padding:40px 32px;display:flex;gap:26px;align-items:center;min-height:300px"><img src="assets/{p}" alt="{n}" style="width:140px;height:140px;border-radius:50%;object-fit:cover"><div><div style="font-size:30px;font-weight:900">{n}</div><div class="badge" style="margin-top:8px">{r}</div><div class="small-copy" style="margin-top:14px;font-size:20px">{d}</div></div></div>' for n, r, d, p in team)
APX.append(shell('Appendix · A10', '세 명이 나눠 맡고, <span class="purple">게이트로 품질</span>을 지켰습니다', f'''
<div style="display:flex;flex-direction:column;height:100%"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;flex:1.3">{tc}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:28px;flex:1">{kpi('2,890개', 'CI 자동 테스트 (BE 2,000 · FE 807 · E2E 83)', '테스트')}{kpi('13건 · 유출 0', 'staging → prod 승격 게이트가 막은 운영 push', '승격 게이트', 'soft', 'purple')}{kpi('72%', 'PR 본문에 검증 내역을 적은 비율', 'PR 기록')}</div></div>'''))
APX.note('''Q&A: PR 리뷰 0건·96% 작성자 병합 → «사람 승인 대신 CI와 승격 게이트로 막았다(운영 push 13건 차단, 운영 유출 0). PR 본문 72%에 검증 내역». ⛔ «공동대표» 금지.''')
