# -*- coding: utf-8 -*-
# 부록 전체 (A1~A12) — 담당: ppt-start (11-07 사용자 지시 «앞으로 어펜딕스는 니가 전담해»)
# 원래 s1(A2·A3) · s2(A1·A18·A6·A7·A9·A11·A13·A12) · s3(A4·A5·A8·A10)에 있던 블록을 그대로 옮겼다.
# 부록이 쓰는 CSS·헬퍼는 각 원래 파일(s2 dv-/a10 · s3 ef-)에 남아 있고 여기서 import한다 — 이름을 바꾸면 이 파일이 깨진다.
# 장표 추가: APX.append(shell('Appendix · A<n>', ...)) 다음 줄에 APX.note('''…''') · 순서는 gen.py가 A번호로 정렬
from core import *
from s1_intro import *
from s2_dev import *
from s3_effect import *
S = Slides()    # 본편 없음
APX = Slides()
CSS = ''

# ================= s1_intro 출신 (A2 · A3) =================
APX.append(shell('Appendix · A2', '범용 AI 비교: 레포를 clone하면 범용 에이전트도 <span class="purple">근거를 찾음</span>', f'''
{table(['군', 'n', 'SHA 실존', '파일 실존', '근거 3종 모두 실존', '본인 커밋'], [['DevFit (운영 prod)', '28', '28 (100%)', '28 (100%)', '28 (100%)', '28 (100%)'], ['Claude Code + 레포 clone', '32', '32 (100%)', '32 (100%)', '30 (94%)', '32 (100%)'], ['범용 AI, 레포 링크만', '18', '0 (0%)', '0 (0%)', '0 (0%)', '0 (0%)']], 'sm plain')}
<div class="body-copy" style="margin:16px 0">DevFit은 레포를 읽고 대조하는 절차를 사용자가 프롬프트를 짜지 않아도 서버가 매번 강제하고, 공고 단위 흐름과 본인 커밋 필터를 더함</div>
{table(['서비스', '입력', '본인 코드·커밋 분석', '질문 근거 표시', '특정 공고 맞춤', '음성', '한국어'], [['DevFit', '공고 URL/이미지 + GitHub', '본인 커밋·PR만', '질문마다 diff + 원문 링크', '플랫폼 5 + 기업 24곳', 'O', 'O'], ['Greenroom (해외)', 'GitHub 레포 · 목표 직무', '레포 단위 O (Pro) · 본인 커밋 구분 확인 안 됨', '확인 안 됨', '확인 안 됨', 'O', '확인 안 됨'], ['Final Round AI (해외)', '이력서 + JD', 'X', '–', 'O', 'O', '명시 없음'], ['사람인 AI 모의면접', '이력서 + 사람인 공고', 'X', '–', '사람인 공고 한정', 'O', 'O'], ['꼬꼬면', '이력서 · 포트폴리오', '언급 없음', '문항 은행 기반', '–', 'O', 'O'], ['범용 AI', '사용자 지시', '연동 시 열람 가능', '사용자가 검증', '사용자가 지시', '일부', 'O']], 'xs')}''', source='실험: 2026-11-05 파일럿, 공개 레포 4개 · 군별 1회 · 결정론 채점 · 기능 비교: 각 서비스 공개 페이지(2026-11-05 확인)'))
APX.note('''출처: collect/E-compare.md (2026-11-05, 레포 4개, 군별 1회, 결정론 채점 LLM 0회). 파일럿이므로 승률로 말하지 말고 비율과 n을 같이.
B1 실패 2건은 API 키를 일부러 가린 인용(지어낸 인용 0). 구체성 proxy(레포 고유 앵커)는 Claude Code 30/32 > DevFit 16/28 — «DevFit이 더 정확하다»는 말하지 않음.''')

APX.append(shell('Appendix · A3', '평가 하네스: <span class="purple">LLM 심판 점수의 편차</span>와 보완 지표', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;flex:1;min-height:0">
  <div class="panel" style="padding:30px 36px"><div class="section-line"><span class="num">1</span><span>평가 하네스 구성</span></div>{ul(['운영 파이프라인을 직접 호출해 질문 생성', '8축 루브릭 (LLM 심판)', '결정적 지표 13개: 출처 연결 · 공고별 중복 · 식별자 실존 등', '회귀 게이트: 질문 로직 버전(v1 → v13)마다 측정'])}</div>
  <div class="panel" style="padding:30px 36px"><div class="section-line"><span class="num">2</span><span>LLM 심판 점수의 편차</span></div>{table(['측정', '값', 'n'], [['심판 2종 간 문항별 점수 차', '17.8점', '91'], ['같은 심판 재채점 차', '12.2점', '24'], ['LLM 심판 vs 사람', '사람보다 약 1점 후함', '18'], ['근거 특정성 (우연 25%)', '81.9%', '177'], ['질문 출처 연결', '353/353', '전수']], 'sm')}</div>
</div>'''))
APX.note('''출처: collect/C-quality.md. 17.82점(n=91) = Kimi·DeepSeek 문항별 차 평균, 12.23점(n=24) = 같은 심판 재채점 차, «LLM 심판이 사람보다 약 1점 후함»(n=18).''')

# ================= s2_dev 출신 (A1 · A18 · A6 · A7 · A9 · A11 · A13 · A12) =================
MID19 = [("1", "늦은 피봇을 범위 축소로 만회(긍정)", "완료", "B2C 주축, B2B 개발 완료. 운영 승격 PR 29 → 125"),
 ("2", "기능 확장보다 질문 품질과 기업 파일럿", "부분", "8축 평가 → 결함 31건 수정 → 난이도 분리 → v11~v13. 저난도 추론형 1/8 → 7/9. 파일럿 0건"),
 ("3", "커밋·diff 연결과 무근거 폐기(긍정)", "완료", "근거 대조·사유 코드 노출(10-19). 출처 353/353, 품질 필터 30일 84건"),
 ("4", "라벨·문항분석으로 정확성·변별도 검증", "부분", "3-state 라벨 UI 복구(09-08). 근거 특정성 81.9%. 변별도 실측 0건(표본 부족)"),
 ("5", "질문 품질 자동 검증", "완료", "평가 하네스(09-06): 8축 루브릭 · 결정적 지표 13개 · 회귀 게이트"),
 ("6", "설계·본인 작업 검증 등 의도별 질문", "완료", "의도 7유형, 난이도 분리, 본인 기여 필터(1.0 / 0.70 / 제외). 09-09 운영"),
 ("7", "코딩 외 전인적 역량 평가", "완료", "자동 합불 금지선 → 준비 지원: 음성 모의면접, 자소서·포트폴리오 작업실, 블라인드 평가"),
 ("8", "기업 파일럿으로 채택률·절감 확인", "부분", "기업 대표 서면 회신 1건, 리드 43사, 로드맵. 수치·LOI 없음"),
 ("9", "시장 분석 세밀화, 포커스 결정", "완료", "출처 등급제(인용 금지 6건 제거), B2C 신입·주니어 포커스"),
 ("10", "기존 취업 사이트 대비 우위", "완료", "공고 × 내 실제 코드. 근거 실존 28/28 vs 0/18"),
 ("11", "경쟁사 직접 사용", "부분", "직접 9 · 인접 43 · 모바일 12종 캡처. 유료 전체 플로우 기록 없음"),
 ("12", "B2C·B2B 동시 공략은 욕심", "소명", "투입은 B2C 집중, B2B는 같은 엔진으로 개발 완료"),
 ("13", "일정상 B2C 집중", "완료", "B2C 출시 → 음성 → 단건 결제 LIVE(11-02)"),
 ("14", "중견기업 타겟", "부분", "리드 규모 32~618명. 검증 수치 없음"),
 ("15", "대학 취업지원실 B2B2C", "미반영", "대학 취창업지원실과 컨택 및 협력 시도 (기술적 사유 아님). 박람회 현장 마케팅만"),
 ("16", "시즌성 때문에 수익모델 재검토", "완료", "공고 단위 단건 1,900원 추가 · LIVE. 매출 0"),
 ("17", "질문 유출 플랫폼은 기업이 싫어함", "소명", "본인 코드 기반 · 지원서별 생성. B2B 커버리지 어시스턴트로 재정의"),
 ("18", "개인정보 보호조치", "완료", "토큰 AES-256-GCM, 세션 해시, numeric id 신원, 증분 동의, 블라인드 평가"),
 ("19", "개발·운영 환경 통합(비용)", "소명", "결제 TEST 격리 필요로 분리 유지. 원가의 94%가 LLM")]
BC = {'완료': 'green', '강화': 'green', '유지': 'neutral', '부분': '', '부분·소명': 'amber', '부분·착수': '', '소명': 'amber', '미반영': 'red'}
APX.append(shell('Appendix · A1', '중간평가 심사의견 19건: 완료 10 · 부분 5 · 소명 3 · 미반영 1', table(['#', '심사의견', '구분', '조치'], [[a, b, badge(c, BC[c]), d] for a, b, c, d in MID19], 'xs left plain a1'), source='반영일·근거 커밋은 운영 브랜치 포함 여부 확인'))
APX.note('''판정 기준(11-07 재분류): 완료 = 조언 핵심을 실행해 운영 반영 · 부분 = 조치 칸에 0건·없음·미검증이 남은 것(#2 파일럿 0 · #4 변별도 실측 0 · #8 수치·LOI 없음 · #11 유료 전체 플로우 기록 없음 · #14 발송 전 미검증) · 소명 3 · 미반영 1은 그대로. collect/I 원분류(완료 5 · 부분 10)와 다름.
출처: collect/I-feedback-patterns.md (반영일·근거 커밋은 운영 브랜치 포함 여부 확인). 최종보고서 «중간점검 반영표»와 같은 내용.
멘토 피드백 31행 표는 collect/I 원본 참조 — 필요 시 A1-2로 추가.''')

APX.append(shell('Appendix · A19', '최소 권한으로 연결하고, <span class="purple">토큰은 암호화</span>', table(['우려', '조치'], [
 ['"GitHub 연동하면 내 코드 털리나"', '기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의'],
 ['분석 범위', '분석할 레포를 사용자가 직접 선택 (08-07 피드백 → 08-23 반영)'],
 ['토큰 유출', 'GitHub access token AES-256-GCM 암호화 저장'],
 ['세션 탈취', '세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능 · HttpOnly 쿠키'],
 ['계정 선점', 'GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)'],
 ['공고 수집 경로 악용 (SSRF)', '홉마다 허용 목록을 다시 검사하는 SafeFetcher · 응답 8MB 상한'],
 ['B2B 지원자 정보', '블라인드 평가 · 지원 시 동의 2건 필수']], 'sm left plain')))
APX.note('''근거 코드: auth/GithubTokenCipher(AES-256-GCM) · user_session(SHA-256 해시) · V38 github_user_id · prep/corporate/SafeFetcher. 레포 범위 선택은 08-07 피드백 후 16일 만(08-23) 반영.''')

APX.append(shell('Appendix · A6', '분석 1회 약 330원, 단건 <span class="purple">1,900원</span> · Plus 월 7,900원', f'''
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px">{kpi('약 330원', '분석 1회 변동비 · 저장소 3개 기준 · 공고 구조화와 질문 생성 포함', '저장소 3개', 'soft', 'purple')}{kpi('약 1,404원', '저장소 20개 상한 기준 최대치', '저장소 20개')}{kpi('0원', '코드 변경 없는 재분석 · 최신 커밋 지문이 같으면 결과 재사용', '재분석')}</div>
<div class="small-copy" style="margin-top:18px;font-size:23px">Plus 1인 월 7,900원 = 저장소 3개 기준 분석 약 24회분의 변동비</div>
<div style="margin-top:26px">{table(['상품', '가격', '상태'], [['Free', '무료 (사용 한도 있음)', '운영 중'], ['추가 생성권 (공고 단위 단건)', '1,900원', '토스페이먼츠 단건 결제 승인 (2026-11-02)'], ['Plus', '월 7,900원', '출시 기념 3개월 무료 개방']], 'sm left plain')}</div>
<div class="callout" style="margin-top:20px">채용 시즌에만 사는 구조에 맞춰 월 구독 외에 <strong>공고 단위 단건 상품</strong> 추가 (중간평가 #16)</div>''', source='CloudWatch 실측 · 운영 요금표 · 최종보고서 「단위 경제성」 표와 같은 기준'))
APX.note('''출처: 최종보고서 단위 경제성 표 · docs/ops/llm-cost-model.md(330원 = 공고 1 + 레포 3 + 어필 + 퀴즈 10, 20개 1,404원).
Q&A 대비: LLM 호출 원장(08-30~11-05, 단가 설정 호출 $32.77 / 분석 346회)으로 나누면 분석당 약 133원(미설정 호출 포함 추정 약 150원) — 기준이 다른 값이라 장표에는 보고서 기준 330원만 씀. ⛔ 330원과 133원을 이어 «60% 절감»으로 말하지 말 것.
원가의 대부분이 LLM(인프라는 개발 DB·서버 정지 운영). Plus 정기결제는 심사 중 — «구독 매출» 금지.''')
APX.append(shell('Appendix · A7', '기출은 <span class="purple">공개 출처</span>만, 출처 URL과 함께 보존', f'''
<div class="panel apx-lg" style="padding:44px 50px">{ul(['운영: 기출 1,880건 (1차 853건(41개사 · 출처 URL 304개) + 2차 1,027건) · 전부 임베딩', '2차 수집 1,073건 원문 대조 1,073/1,073 일치 → 1,027건 반영', '수집 규칙: robots 확인 · 도메인당 1.5초 간격 · 원문 1회 캐시 · robots가 막은 사이트와 AI 수집을 막은 블로그 제외', '출처 URL을 질문과 함께 보존 · (URL + 원문) 해시로 중복 방지', '생성 프롬프트에 넣지 않고, 학습실 질문 옆에 비슷한 실제 기출로 출처와 함께 표시'])}</div>'''))
APX.note('''근거: interview-evidence-audit-2026-10-11 · production-upload-result-2026-10-11.json · Devfit/research/interview-evidence/reports/progress.md · docs/interview-question-evidence.md. 11-02 전략멘토링 대응 기록: «저작권·직업정보제공사업 문제로 공개 정보 위주로 간다».
⛔ «검증된 853건» 금지(REVIEWED 0 · NEEDS_REVIEW 158 · 302건은 주제 보고). 법률: 11-05 소마 법률 멘토링 구두 검토 의견(claims C7) — «법률의견서»·«합법 확인» 금지.
11-08 운영 DB 실측(gichul): 기출 1,880 / 벡터 1,880 · 누락 0 (853 + 2차 1,027).''')

team = [('박천웅', '팀장 · DevSecOps &amp; Full Stack', '인증·보안, AWS 인프라·CI/CD·운영 배포, FE·BE 통합, 결제·사업자 행정', 'team-park-cheonwoong.jpg'),
        ('김건우', 'PM &amp; Frontend', '문제 정의·제품 방향·BM, Next.js 프론트엔드(B2C·B2B·관리자 콘솔), 마케팅·유입 계측', 'team-kim-gunwoo.jpg'),
        ('노재원', 'Backend · Core Logic &amp; AI', 'GitHub 커밋 선별 알고리즘, 근거 묶음·질문 생성 핵심 로직, Spring Boot 백엔드', 'team-noh-jaewon.jpg')]
tc = ''.join(f'<div class="a10-m"><img src="assets/{p}" alt="{n}"><div><b>{n}</b><span class="badge">{r}</span><em class="{"hs" if n == "김건우" else ""}">{"고등학생 · 학교 병행" if n == "김건우" else "학교 병행"}</em><small>{d}</small></div></div>' for n, r, d, p in team)
import csv as _csv
_HM = list(_csv.DictReader(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','collect','data','commit_heatmap_weekday_hour_kst.csv'), encoding='utf8')))
_KO = {'Mon': '월', 'Tue': '화', 'Wed': '수', 'Thu': '목', 'Fri': '금', 'Sat': '토', 'Sun': '일'}
_hmax = max(int(r[f'h{h:02d}']) for r in _HM for h in range(24))
_hm_total = sum(int(r['total']) for r in _HM)
_hm_class = sum(int(r[f'h{h:02d}']) for r in _HM if r['weekday'] not in ('Sat', 'Sun') for h in range(9, 17))
_hm_off = round((1 - _hm_class / _hm_total) * 100)
_cells = ''.join(f'<i class="d">{_KO[r["weekday"]]}</i>' + ''.join(
    f'<i style="background:rgba(108,92,231,{(0.06 + 0.94 * int(r[f"h{h:02d}"]) / _hmax) if int(r[f"h{h:02d}"]) else 0:.2f})" title="{int(r[f"h{h:02d}"])}"></i>' for h in range(24)) for r in _HM)
_hours = '<i class="h"></i>' + ''.join(f'<i class="h">{h if h % 3 == 0 else ""}</i>' for h in range(24))
heat = f'<div class="a10-hm"><div class="grid">{_cells}{_hours}</div></div>'
APX.append(shell('Appendix · A9', '팀 구성과 역할: 3명 모두 <span class="purple">학교 병행</span>, 1명은 <span class="purple">고등학생</span>', f'''
<div class="a10">
  <div class="banner"><b>3명 모두 학교 병행 · 1명은 고등학생</b><span>수업이 끝난 저녁과 주말에 개발 · 14주 연속 매주 운영 배포</span></div>
  <div class="team">{tc}</div>
  <div class="panel a10-hp"><div class="hd"><b>커밋 기록: 요일 × 시간 (KST)</b><span>커밋 {_hm_total:,}개 중 <strong>{_hm_off}%</strong>가 평일 9~17시 밖</span></div>{heat}</div>
</div>''', source='collect/data/commit_heatmap_weekday_hour_kst.csv (BE+FE 원격 브랜치 전체, 병합 커밋 506개 제외 · scripts/pattern.py) · 학교 병행은 팀 진술(claims.md)'))
APX.note('''세 명 모두 학교를 다니면서 만들었고, 김건우는 고등학생(단국대 SW고 6기, 소마 17기 최연소)입니다. 커밋 961개 중 약 61%가 평일 낮 9~17시 밖, 수업이 끝난 저녁과 주말에 찍혔습니다. 그래도 출시 후 14주 연속 매주 운영에 배포했습니다.
뺀 수치(필요하면 말로): CI 자동 테스트 2,890개(BE 2,000 · FE 807 · E2E 83) · staging → prod 승격 게이트가 막은 운영 push 13건 · 유출 0 · PR 본문 검증 내역 72%.
⚠️ «평일 9~17시 밖»은 커밋 시각 기준일 뿐 작업 시간 전체가 아님. 나머지 2명의 학교 병행은 사용자 진술(claims.md 등록 요청).
Q&A: PR 리뷰 0건·96% 작성자 병합 → «사람 승인 대신 CI와 승격 게이트로 막았다(운영 push 13건 차단, 운영 유출 0). PR 본문 72%에 검증 내역». ⛔ «공동대표» 금지.''')

# --- A11 모델 라우팅 · 스택 ---
APX.append(shell('Appendix · A11', '역할별 모델 라우팅과 <span class="purple">서비스 스택</span>', '''
<div class="hero" style="grid-template-columns:1.1fr .9fr;margin:auto 0">
  <div class="panel" style="padding:30px 34px"><div class="infra-summary-title">LLM · 역할별 라우팅 (Bedrock 5종 + 외부 2종)</div>
    <div class="mchips">
      <div><small>추론 · 질문 생성</small><b>GLM-5</b></div><div><small>코드 · 답변 피드백</small><b>Qwen3-Coder-Next</b></div><div><small>추출</small><b>GLM-4.7-Flash</b></div>
      <div><small>비전 · 공고 OCR</small><b>Nova 2 Lite</b></div><div><small>사업자 OCR</small><b>Qwen3-VL</b></div><div style="outline:3px solid var(--purple);border-radius:14px"><small>커밋 판정 · Decision Model</small><b>OpenAI Decisions</b></div>
      <div><small>임베딩 · 기출 검색</small><b>Cohere Embed v3</b></div>
    </div></div>
  <div class="panel" style="padding:30px 34px"><div class="infra-summary-title">서비스 · 검색 · 음성</div>
    <div class="ilist"><div><small>FE</small>Next.js 16 정적 export → S3 + CloudFront</div><div><small>BE</small>Spring Boot 3.4 · Java 21 · ECS Fargate</div><div><small>큐</small>DB 큐 + 워커 원자 선점 · 지수 백오프</div><div><small>DB</small>PostgreSQL · Flyway · pgvector</div><div><small>음성</small>자체 음성 사이드카 (STT · TTS)</div></div></div>
</div>''', source='origin/prod application.yml bedrock.models.* · app.commit-decision · interview-evidence.vector (2026-11-06)'))
APX.note('''출처: origin/prod application.yml:103-127(bedrock.models reasoning/code/extraction/vision/business-ocr) · :336-354(커밋 판정 gpt-6-luna, OpenAI) · :167-169(cohere.embed-multilingual-v3) · BedrockService evaluateAnswer=code 모델.
🔴 OpenAI(커밋 판정 · 조건부 TTS) 호출이 개인정보처리방침 국외 이전에 미고지(R1) — 발표 전 정리. 음성 provider 운영값 확인 필요(s2 음성 장 노트).''')

APX.append(shell('Appendix · A12', 'staging을 거치지 않은 변경은 <span class="purple">운영에 나가지 않음</span>', f'''
<div class="hero" style="grid-template-columns:1.25fr .75fr;margin:auto 0">
  <div class="panel dep">
    <div class="fb2-k">배포 경로 (숫자는 게이트가 실제로 막은 횟수)</div>
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
SBOM 게이트는 11-05 운영 반영 → «HIGH·CRITICAL 1건 이상이면 배포 잡 중단 · 백엔드만»까지, ⛔ «취약점 0건 = 안전»·«FE 포함» 금지. Q&A: PR 리뷰 0건·96% 작성자 병합 → 사람 승인 대신 CI·승격 게이트, PR 본문 72%에 검증 내역.''')

# ================= s3_effect 출신 (A4 · A5 · A8 · A10) =================
APX.append(shell('Appendix · A4', '측정 도구별 수치 차이 (<span class="purple">기준: 관리자 DB</span>)', f'''
<div style="display:grid;grid-template-columns:1.25fr .75fr;gap:30px;flex:1;min-height:0">
  <div class="shot"><img src="assets/14_measurement_gap.png" alt="측정 도구별 수치 차이" style="object-fit:contain"></div>
  <div style="display:flex;flex-direction:column;gap:20px">{kpi('22,360명', 'Microsoft Clarity 방문자 · 동의와 무관하게 수집, 봇 제외', 'Clarity')}{kpi('235명', 'GA4 사용자 · 쿠키 동의한 사람만 → 하한', 'GA4', 'red-soft', 'red')}{kpi('83명', '관리자 DB 가입 · 기준 수치 (내부 4명 포함)', '관리자 DB', 'soft', 'purple')}</div>
</div>''', source='기간 2026-08-01 ~ 11-04 · 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4'))
APX.note('''출처: metrics/charts/14_measurement_gap.png · collect/D §1. GA4는 쿠키 동의 게이트 때문에 하한(가입 이벤트가 실제 가입의 약 절반만 잡힘). 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4.''')

APX.append(shell('Appendix · A5', '유료 광고 ₩347.5만: 클릭 1회 ₩110~563, <span class="red">가입 1명당 최소 ₩4.2만</span>', f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{kpi('₩347.5만', 'Meta ₩233.8만 + Google ₩113.7만', '유료 광고 합계')}{kpi('최소 ₩4.2만', '가입 1명당 광고비 (하한, 상한 추정 ₩12.9만)', '가입 단가', 'red-soft', 'red')}{kpi('브랜드 검색뿐', 'Search Console 클릭 37건, 대부분 "devfit"', '자연 검색')}</div>
<div style="margin-top:26px">{table(['지표', 'Meta', 'Google'], [['지출', '₩2,338,208', '₩1,136,972'], ['노출', '666,197', '116,041'], ['클릭', '21,318 (링크 클릭)', '2,018'], ['클릭 1회', '₩110', '₩563'], ['랜딩 1회', '₩151 (Meta 랜딩 조회)', '—']], 'sm plain')}</div>''', source='Meta 광고 관리자(8/1~11/3) · Google Ads(8/24~11/3) · ₩4.2만 = 광고비 ÷ 전체 가입 83명(전원 광고 유입 가정)'))
APX.note('''출처: collect/D §2. ₩4.2만은 하한(가입 전원이 광고로 들어왔다고 가정) — «상한»이라 쓰지 말 것. 상한 추정 ₩12.9만. Meta·Google의 «전환»과 DB «가입»은 정의가 다름.''')

APX.append(shell('Appendix · A8', '특허 3건 출원: <span class="purple">선별 · 생성 · 음성</span>', f'''
{table(['출원번호', '발명의 명칭', '보호하는 것 (요지)', '관련 장표'], [
 ['<span class="patent">10-2026-0214808</span>', '코드 저장소 기반 면접 질문 선별 방법 및 시스템', '본인 기여 커밋을 골라 가중(본인 1.0 · 공동 0.70 · 타인 제외)하고 질문 대상 지점을 선별', 'Key Features 경쟁사 비교(본인 커밋만) · Development 점수식'],
 ['<span class="patent">10-2026-0214809</span>', '코드 저장소 기반 면접 질문 생성 방법 및 시스템', '근거 코드 묶음에서 질문을 만들고, 질문 속 식별자를 코드와 대조해 유지·폐기·재질의하는 게이트', 'Key Features 반론(근거 대조)'],
 ['<span class="patent">10-2026-0214811</span>', '음성 대화 기반 면접 답변 평가 방법 및 시스템', '음성 답변을 받아 적고 답변에 기반한 꼬리질문으로 되묻는 모의면접', 'Development 기출·음성']], 'left plain a9')}
<div class="body-copy" style="margin-top:20px">출원일 2026-11-01 · 출원인 김건우 · 발명자 김건우, 박천웅, 노재원</div>'''))
APX.note('''출원인 김건우(개인), 발명자 김건우·박천웅·노재원. 심사청구 무 · 공개신청 무(통지서 기준). ⛔ «등록»·«회사 특허» 금지.
«관련 장표» 열은 장 제목으로 표기(쪽번호 금지 규칙). 최종 표기는 Dev 슬림화 후 ppt-start와 맞춤 — 0214809는 Development 입력·출력 게이트 장이 남으면 덧붙임.
청구항 요지 원문: Devfit/docs/patent/ 명세서 (⛔ 삭제 금지, 공지예외 12개월 시한 진행 중).''')

APX.append(shell('Appendix · A10', '시장 규모: 개발 직군 구직자 <span class="purple">약 38.8만 명</span>', f'''
{table(['구분', '값', '근거'], [
 ['연간 개발 직군 입사지원 (A)', '약 520만 건', '사람인·점핏 2025 상반기 약 260만 건 × 2 ⚙'],
 ['적극 구직자 1인 평균 입사지원 (B)', '13.4회', '한국경제인협회 2025 조사'],
 ['<b>연간 추정 구직자 (A ÷ B)</b>', '<b>약 38.8만 명</b>', '중복 지원 보정'],
 ['유료 1인 매출 ⚙', '23,700원', '3개월 무료 체험 후 Plus 3개월 구독']], 'sm left plain')}
<div style="margin-top:26px">{table(['구직자 대비 유료 전환', '유료 사용자', '연 매출 (1인 3개월 구독)', '비고'], [
 ['1.0%', '약 3,881명', '<b>약 9,200만 원</b>', '초기 목표, 공채 시즌 2회'],
 ['2.0%', '약 7,761명', '<b>약 1.84억 원</b>', '대학과 부트캠프 제휴 포함'],
 ['5.0%', '약 19,403명', '<b>약 4.6억 원</b>', '기업용 제품 연계 시']], 'sm left plain')}</div>
<div class="small-copy" style="margin-top:18px;font-size:19px">⚙ = 내부 가정 · 실제 전환율은 결제 활성화 이후 측정</div>''', source='사람인·점핏 2025 상반기 개발자 채용 리포트 · 한국경제인협회 2025 구직자 조사 · 최종보고서 「시장 규모와 수익 구조」와 같은 계산'))
APX.note('''예상 질문: «시장 크기는?»
- 계산은 최종보고서와 같다: 520만 건 ÷ 13.4회 = 약 38.8만 명. 유료 1인 = 3개월 무료 체험 후 3개월 구독(7,900원 × 3 = 23,700원) 가정.
- A: 점핏 리포트 원값 지원 2,601,390건(2025 1~6월) × 2 — 하반기 동일 가정(⚙). 플랫폼 2곳 한정이라 과소.
- 직접 시장은 B2C(면접을 준비하는 개발자 지원자). 기업용은 같은 엔진의 확장 시장으로만 말함 — B2B 시장 규모 수치는 장표·발표에서 쓰지 않음.
⛔ «매출»은 시나리오 표의 가정값으로만, 실적처럼 말하지 말 것. 5년 SOM 27억 · TAM $2.8B 금지.''')


