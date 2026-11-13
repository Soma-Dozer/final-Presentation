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
APX.append(shell('Appendix · A2', '평가 하네스: <span class="purple">LLM 심판 점수의 편차</span>와 보완 지표', f'''
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

APX.append(shell('Appendix · A17', '최소 권한으로 연결하고, <span class="purple">토큰은 암호화</span>', table(['우려', '조치'], [
 ['"GitHub 연동하면 내 코드 털리나"', '기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의'],
 ['분석 범위', '분석할 레포를 사용자가 직접 선택 (08-07 피드백 → 08-23 반영)'],
 ['토큰 유출', 'GitHub access token AES-256-GCM 암호화 저장'],
 ['세션 탈취', '세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능 · HttpOnly 쿠키'],
 ['계정 선점', 'GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)'],
 ['공고 수집 경로 악용 (SSRF)', '홉마다 허용 목록을 다시 검사하는 SafeFetcher · 응답 8MB 상한'],
 ['B2B 지원자 정보', '블라인드 평가 · 지원 시 동의 2건 필수']], 'sm left plain')))
APX.note('''근거 코드: auth/GithubTokenCipher(AES-256-GCM) · user_session(SHA-256 해시) · V38 github_user_id · prep/corporate/SafeFetcher. 레포 범위 선택은 08-07 피드백 후 16일 만(08-23) 반영.''')

APX.append(shell('Appendix · A5', '분석 1회 약 330원, 단건 <span class="purple">1,900원</span> · Plus 월 7,900원', f'''
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px">{kpi('약 330원', '분석 1회 변동비 · 저장소 3개 기준 · 공고 구조화와 질문 생성 포함', '저장소 3개', 'soft', 'purple')}{kpi('약 1,404원', '저장소 20개 상한 기준 최대치', '저장소 20개')}{kpi('0원', '코드 변경 없는 재분석 · 최신 커밋 지문이 같으면 결과 재사용', '재분석')}</div>
<div class="small-copy" style="margin-top:18px;font-size:23px">Plus 1인 월 7,900원 = 저장소 3개 기준 분석 약 24회분의 변동비</div>
<div style="margin-top:26px">{table(['상품', '가격', '상태'], [['Free', '무료 (사용 한도 있음)', '운영 중'], ['추가 생성권 (공고 단위 단건)', '1,900원', '토스페이먼츠 단건 결제 승인 (2026-11-02)'], ['Plus', '월 7,900원', '출시 기념 3개월 무료 개방']], 'sm left plain')}</div>
<div class="callout" style="margin-top:20px">채용 시즌에만 사는 구조에 맞춰 월 구독 외에 <strong>공고 단위 단건 상품</strong> 추가 (중간평가 #16)</div>''', source='CloudWatch 실측 · 운영 요금표 · 최종보고서 「단위 경제성」 표와 같은 기준'))
APX.note('''출처: 최종보고서 단위 경제성 표 · docs/ops/llm-cost-model.md(330원 = 공고 1 + 레포 3 + 어필 + 퀴즈 10, 20개 1,404원).
Q&A 대비: LLM 호출 원장(08-30~11-05, 단가 설정 호출 $32.77 / 분석 346회)으로 나누면 분석당 약 133원(미설정 호출 포함 추정 약 150원) — 기준이 다른 값이라 장표에는 보고서 기준 330원만 씀. ⛔ 330원과 133원을 이어 «60% 절감»으로 말하지 말 것.
원가의 대부분이 LLM(인프라는 개발 DB·서버 정지 운영). Plus 정기결제는 심사 중 — «구독 매출» 금지.''')
CSS += r"""
.apx-gc{margin:auto 0;word-break:keep-all;width:100%}
.apx-gc .col{display:flex;flex-direction:column;gap:14px}
.apx-gc .ar{display:flex;align-items:center;justify-content:center;width:46px;font-size:34px;color:var(--purple);font-weight:700}
.apx-gc .wrap{display:grid;grid-template-columns:1.15fr 46px 1fr 46px 1.05fr;align-items:stretch}
.apx-gc .col>.panel{flex:1}
.apx-gc .k{font-size:24px;font-weight:700;color:var(--purple);margin-bottom:2px}
.apx-gc .panel{padding:30px 30px}
.apx-gc .raw{font-size:22px;line-height:1.5;color:var(--body)}
.apx-gc .raw small{display:block;font-size:19px;color:var(--muted);margin-top:8px}
.apx-gc .raw q{display:block;margin:10px 0;padding:10px 14px;background:#f3f1fa;border-radius:8px;font-size:21px;line-height:1.6;color:var(--ink);quotes:none}
.apx-gc .raw mark{background:#e4defb;color:var(--purple-deep);font-weight:700;padding:0 3px;border-radius:3px}
.apx-gc .st{display:grid;grid-template-columns:38px 1fr;gap:6px 12px;font-size:22px;line-height:1.42;color:var(--body)}
.apx-gc .st i{font-style:normal;font-weight:700;color:#fff;background:var(--purple);width:32px;height:32px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:18px;margin-top:2px}
.apx-gc .st b,.apx-gc .raw b{color:var(--ink);font-size:inherit;display:inline}
.apx-gc .st div{margin-bottom:12px}
.apx-gc .ui{border:1.5px solid #ddd6f6;border-radius:12px;padding:16px 18px;background:#faf9ff;font-size:21px;line-height:1.45;color:var(--body)}
.apx-gc .ui h4{margin:0 0 8px;font-size:18px;color:var(--purple);font-weight:700}
.apx-gc .ui p{margin:0}
.apx-gc .ui .q{margin-top:6px;padding-left:10px;border-left:3px solid #cfc6f3;color:var(--ink)}
.apx-gc .ui .meta{margin-top:6px;font-size:18px;color:var(--muted)}
.apx-gc .sm{font-size:18px;line-height:1.45;color:var(--muted);margin-top:6px}
.apx-gc-law{margin-top:22px;padding:18px 26px;border-left:6px solid var(--purple);background:#f6f4fd;border-radius:10px;font-size:21px;line-height:1.5;color:var(--body);word-break:keep-all}
.apx-gc-law b{color:var(--ink)}
.apx-gc code{font-size:.85em;background:#ece8fa;padding:0 4px;border-radius:4px}
.apx-gc-foot{margin-top:22px;font-size:21px;color:var(--muted);text-align:center;word-break:keep-all}
.apx-gc-foot b{color:var(--ink)}
"""
CSS += r"""
.apx-g2{display:grid;grid-template-columns:1.55fr .65fr;gap:26px;margin:auto 0;word-break:keep-all}
.apx-g2 table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 1px 0 #e9e6f3}
.apx-g2 th{font-size:20px;text-align:left;padding:12px 16px;background:#f3f1fa;color:var(--purple-deep)}
.apx-g2 td{font-size:20px;line-height:1.42;padding:11px 16px;border-top:1px solid #eeebf6;vertical-align:top}
.apx-g2 td.n{width:30px;font-weight:700;color:var(--purple);text-align:center}
.apx-g2 td.o{width:40%;color:var(--muted);font-size:18px}
.apx-g2 td.ko{color:var(--ink)}
.apx-g2 code{font-size:16px;background:#f3f1fa;padding:0 4px;border-radius:4px}
.apx-g2 .side{display:flex;flex-direction:column;gap:14px}
.apx-g2 .panel{padding:24px 26px}
.apx-g2 .k{font-size:22px;font-weight:700;color:var(--purple);margin-bottom:10px}
.apx-g2 .st{display:grid;grid-template-columns:28px 1fr;gap:6px 10px;font-size:19px;line-height:1.42;color:var(--body)}
.apx-g2 .st i{font-style:normal;font-weight:700;color:#fff;background:var(--purple);width:28px;height:28px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:16px;margin-top:1px}
.apx-g2 .st b{color:var(--ink);font-size:inherit;display:inline}
.apx-g2 .st div{margin-bottom:6px}
.apx-g2 .ui{border:1.5px solid #ddd6f6;border-radius:12px;padding:14px 16px;background:#faf9ff;font-size:19px;line-height:1.45;color:var(--ink)}
.apx-g2 .ui h4{margin:0 0 6px;font-size:16px;color:var(--purple);font-weight:700}
.apx-g2-meta{font-size:20px;color:var(--muted);margin:0 0 10px}
.apx-g2-meta b{color:var(--ink)}
"""
APX.append(shell('Appendix · A6', '공개된 면접 후기에서 내용만 뽑아 <span class="purple">직접 가공</span>', f'''
<div class="apx-gc"><div class="wrap">
  <div class="col"><div class="panel raw"><div class="k">1. 원문 (공개 면접 후기)</div>
    당근 Mini R&amp;D Engineer 인턴 기술 면접 (2022) 꼬리질문 중 하나
    <q>With Web Worker, it is possible to separate the mini app and the client app into separate threads. However, the Web Worker cannot access the DOM API if you do this. For example, you cannot use the DOM API called <code>getClientBoundingRect</code>. What should I do to solve this?</q>
    <small>출처 URL과 페이지 제목은 근거로 따로 보관</small></div></div>
  <div class="ar">→</div>
  <div class="col"><div class="panel"><div class="k">2. 직접 가공</div><div class="st">
    <i>1</i><div><b>질문 단위로 분리</b> · 한 단락에 이어진 꼬리질문 6개를 각각 한 건으로</div>
    <i>2</i><div><b>맥락 보강</b> · 앞 질문의 전제를 붙여 이 질문만 봐도 뜻이 통하게</div>
    <i>3</i><div><b>새 문장으로 작성</b> · 원문 문장을 옮기지 않고 한국어 면접관 말투로</div>
    <i>4</i><div><b>필드 정리와 대조</b> · 회사, 채용명, 연도를 나누고 출처와 비교</div></div></div></div>
  <div class="ar">→</div>
  <div class="col"><div class="panel"><div class="k">3. 서비스에 들어간 문장</div>
    <div class="ui"><p class="q">Web Worker를 사용하면 미니 앱과 클라이언트 앱을 각각 다른 스레드로 분리할 수 있습니다. 하지만 이렇게 하면 Web Worker에서 DOM API에 접근할 수 없습니다. 예를 들어 <code>getClientBoundingRect</code>라는 DOM API를 사용할 수 없습니다. 이를 해결하려면 어떻게 해야 하나요?</p></div>
    <div class="ui" style="margin-top:14px"><h4>학습실 카드</h4><p>실제 2022년 당근 Karrot Mini R&amp;D Engineer Intern 채용에서 비슷한 면접 질문이 출제되었어요.</p></div>
  </div></div>
</div>
<div class="apx-gc-law"><b>저작권법 제2조 제1호</b> "저작물"은 인간의 사상 또는 감정을 <b>표현한</b> 창작물을 말한다.<br><b>대법원 2000. 10. 24. 선고 99다10813 판결</b> 표현되어 있는 내용 즉 아이디어나 이론 등의 사상 및 감정 그 자체는 설사 그것이 독창성, 신규성이 있다 하더라도 원칙적으로 저작권의 보호 대상이 되지 않는다.</div></div>''', source='저작권법 제2조 제1호 · 대법원 2000. 10. 24. 선고 99다10813 판결 · cho.sh, 「Mini R&amp;D Engineer Job Interview」, 2022 · Devfit_BE interview-question-evidence.csv 운영 적재본'))
APX.note('''공개 면접 후기에는 면접 시간, 분위기, 본인 감상 같은 경험담이 섞여 있습니다. 여기서 어떤 질문을 받았는지라는 사실만 사람이 뽑아내고, 후기의 문장은 옮기지 않고 질문의 뜻만 남겨 새 문장으로 씁니다. 다시 쓴 질문이 원문 내용을 벗어나지 않았는지는 출처와 대조합니다.
장표 예시는 1차 기출 CSV의 실제 행(당근, source https://cho.sh/w/98410A, Karrot Mini R&D Engineer Intern, 2022, 같은 후기에서 6행 중 4번째 꼬리질문). 왼쪽은 question_original, 오른쪽은 normalized_question 전문 그대로. 카드 문구는 InterviewEvidenceCard.attribution 출력.
저작권 문구: 아이디어와 표현 이분법(저작권법은 표현을 보호하고 아이디어 자체는 보호하지 않으며, 이 점에서 산업재산권과 구분됨). 보조 출처: 문화체육관광부 저작권 상식 페이지("저작권법은 표현된 것을 보호하는 것이지 그 아이디어 자체를 보호하는 것은 아니며, 이 점에서도 산업재산권과 구분된다.")(https://www.mcst.go.kr/site/s_policy/copyright/knowledge/know03.jsp), 2026-11-13 검색 확인. 운영 기출 1,880건. 법률 판단은 11-05 소마 법률 멘토링 구두 의견 수준이므로 «합법 확인» 금지.
사람 가공 표시는 사용자 지시(2026-11-13). 수집 기록(progress.md)에는 2차 수집에 추출 에이전트 단계와 1차 LLM 보조 정제가 있으니, Q&A에서 범위를 물으면 기록대로 답할 것.
근거: interview-evidence-audit-2026-10-11 · production-upload-result-2026-10-11.json · Devfit/research/interview-evidence/reports/progress.md · docs/interview-question-evidence.md. 11-02 전략멘토링 대응 기록: «저작권·직업정보제공사업 문제로 공개 정보 위주로 간다».
⛔ «검증된 853건» 금지(REVIEWED 0 · NEEDS_REVIEW 158 · 302건은 주제 보고). 법률: 11-05 소마 법률 멘토링 구두 검토 의견(claims C7) — «법률의견서»·«합법 확인» 금지.
11-08 운영 DB 실측(gichul): 기출 1,880 / 벡터 1,880 · 누락 0 (853 + 2차 1,027).''')

# --- A11 모델 라우팅 · 스택 ---
APX.append(shell('Appendix · A10', '역할별 모델 라우팅과 <span class="purple">서비스 스택</span>', '''
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

# ================= s3_effect 출신 (A4 · A5 · A8 · A10) =================
APX.append(shell('Appendix · A3', '측정 도구별 수치 차이 (<span class="purple">기준: 관리자 DB</span>)', f'''
<div style="display:grid;grid-template-columns:1.25fr .75fr;gap:30px;flex:1;min-height:0">
  <div class="shot"><img src="assets/14_measurement_gap.png" alt="측정 도구별 수치 차이" style="object-fit:contain"></div>
  <div style="display:flex;flex-direction:column;gap:20px">{kpi('22,360명', 'Microsoft Clarity 방문자 · 동의와 무관하게 수집, 봇 제외', 'Clarity')}{kpi('235명', 'GA4 사용자 · 쿠키 동의한 사람만 → 하한', 'GA4', 'red-soft', 'red')}{kpi('83명', '관리자 DB 가입 · 기준 수치 (내부 4명 포함)', '관리자 DB', 'soft', 'purple')}</div>
</div>''', source='기간 2026-08-01 ~ 11-04 · 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4'))
APX.note('''출처: metrics/charts/14_measurement_gap.png · collect/D §1. GA4는 쿠키 동의 게이트 때문에 하한(가입 이벤트가 실제 가입의 약 절반만 잡힘). 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4.''')

APX.append(shell('Appendix · A4', '유료 광고 ₩347.5만: 클릭 1회 ₩110~563, <span class="red">가입 1명당 최소 ₩4.2만</span>', f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{kpi('₩347.5만', 'Meta ₩233.8만 + Google ₩113.7만', '유료 광고 합계')}{kpi('최소 ₩4.2만', '가입 1명당 광고비 (하한, 상한 추정 ₩12.9만)', '가입 단가', 'red-soft', 'red')}{kpi('브랜드 검색뿐', 'Search Console 클릭 37건, 대부분 "devfit"', '자연 검색')}</div>
<div style="margin-top:26px">{table(['지표', 'Meta', 'Google'], [['지출', '₩2,338,208', '₩1,136,972'], ['노출', '666,197', '116,041'], ['클릭', '21,318 (링크 클릭)', '2,018'], ['클릭 1회', '₩110', '₩563'], ['랜딩 1회', '₩151 (Meta 랜딩 조회)', '—']], 'sm plain')}</div>''', source='Meta 광고 관리자(8/1~11/3) · Google Ads(8/24~11/3) · ₩4.2만 = 광고비 ÷ 전체 가입 83명(전원 광고 유입 가정)'))
APX.note('''출처: collect/D §2. ₩4.2만은 하한(가입 전원이 광고로 들어왔다고 가정) — «상한»이라 쓰지 말 것. 상한 추정 ₩12.9만. Meta·Google의 «전환»과 DB «가입»은 정의가 다름.''')

APX.append(shell('Appendix · A7', '특허 3건 출원: <span class="purple">선별 · 생성 · 음성</span>', f'''
{table(['출원번호', '발명의 명칭', '보호하는 것 (요지)', '관련 장표'], [
 ['<span class="patent">10-2026-0214808</span>', '코드 저장소 기반 면접 질문 선별 방법 및 시스템', '본인 기여 커밋을 골라 가중(본인 1.0 · 공동 0.70 · 타인 제외)하고 질문 대상 지점을 선별', 'Key Features 경쟁사 비교(본인 커밋만) · Development 점수식'],
 ['<span class="patent">10-2026-0214809</span>', '코드 저장소 기반 면접 질문 생성 방법 및 시스템', '근거 코드 묶음에서 질문을 만들고, 질문 속 식별자를 코드와 대조해 유지·폐기·재질의하는 게이트', 'Key Features 반론(근거 대조)'],
 ['<span class="patent">10-2026-0214811</span>', '음성 대화 기반 면접 답변 평가 방법 및 시스템', '음성 답변을 받아 적고 답변에 기반한 꼬리질문으로 되묻는 모의면접', 'Development 기출·음성']], 'left plain a9')}
<div class="body-copy" style="margin-top:20px">출원일 2026-11-01 · 출원인 김건우 · 발명자 김건우, 박천웅, 노재원</div>'''))
APX.note('''출원인 김건우(개인), 발명자 김건우·박천웅·노재원. 심사청구 무 · 공개신청 무(통지서 기준). ⛔ «등록»·«회사 특허» 금지.
«관련 장표» 열은 장 제목으로 표기(쪽번호 금지 규칙). 최종 표기는 Dev 슬림화 후 ppt-start와 맞춤 — 0214809는 Development 입력·출력 게이트 장이 남으면 덧붙임.
청구항 요지 원문: Devfit/docs/patent/ 명세서 (⛔ 삭제 금지, 공지예외 12개월 시한 진행 중).''')

APX.append(shell('Appendix · A9', '시장 규모 계산 근거: <span class="purple">입력값 8개의 출처와 가정</span>', f'''
{table(['', '입력값', '값', '어디서 왔나', '종류'], [
 ['A', '글로벌 IT 인력공급 시장 (2025)', '1,233억 달러', 'Mordor Intelligence, 「IT Staffing Market」, 2026. 파견·계약직 인건비 포함', '출처'],
 ['B', 'SW 개발자 비중', '37.05%', '같은 보고서, 2025년 직무별 점유율', '출처'],
 ['C', '글로벌 코딩면접 준비 시장 (2025)', '38억 달러', 'DataIntelo, 「Coding Interview Preparation Market」. 온라인 강의·문제풀이·코칭·교재 포함', '출처'],
 ['D', '환율', '1,337원/달러', '2026-11-13 조회', '출처'],
 ['E', '국내 개발자 채용매칭 시장 (2025)', '약 6,500억 원', '대신증권, 원티드랩 기업분석, 2022-11. 2025년 전망치 (머니투데이방송 2023-02-23 보도)', '출처'],
 ['F', '국내 개발자 취업·면접 준비 시장', '약 100억 원', '개발자 구직·이직 준비자 20만 명 × 1인 5만 원', '⚙'],
 ['G', 'B2C 유료 이용자 (3년 차)', '3,881명 × 23,700원', '구직자 38.8만 명(점핏 2025 지원 520만 건 ÷ 한경협 1인 13.4회) × 1% · Plus 월 7,900원 × 3개월', '출처 + ⚙'],
 ['H', 'B2B 고객사 (3년 차)', '15곳 × 월 13만 원', '기획 문서 B2B 요금 티어의 고객사 평균(Team 월 12만 원·지원자 20명 포함, 미배포)', '⚙']], 'sm left plain')}
<div class="small-copy" style="margin-top:16px;font-size:20px;line-height:1.6"><b>TAM</b> A×B×D 61.1조 + C×D 5.1조 = <b>약 66조 원</b> · <b>SAM</b> E 6,500억 + F 100억 = <b>약 6,600억 원</b> · <b>SOM</b> G 0.92억 + H×12개월 2.34억 = <b>연 약 3.3억 원</b><br>⚙ = 내부 가정 · TAM·SAM은 조사기관 추정·전망치, SOM은 3년 차 목표이며 실적 아님</div>''', source='Mordor Intelligence IT Staffing Market(mordorintelligence.com/industry-reports/it-staffing-market) · DataIntelo Coding Interview Preparation Market(dataintelo.com/report/coding-interview-preparation-market) · 대신증권 원티드랩 기업분석 2022-11(머니투데이방송 2023-02-23 보도) · 점핏 2025 · 한국경제인협회 2025 · 기획 문서 B2B 요금 티어'))
APX.note('''예상 질문: «시장 크기는? 숫자 어디서 나왔나?» (11-13 사용자 지시: 본편 시장 규모 장을 TAM 66조·SAM 6,600억·SOM 연 3.3억으로 교체, 이 부록도 같은 계산으로 갱신)
URL: Mordor https://www.mordorintelligence.com/industry-reports/it-staffing-market (USD 123.30B 2025, Software Developers 37.05% — 2026–2031판) · DataIntelo https://dataintelo.com/report/coding-interview-preparation-market (USD 3.8B 2025 → 9.2B 2034) · 대신증권 전망 https://news.mtn.co.kr/news-detail/2023022310563781713 (원티드랩 리포트 2022-11-23, PDF 원문 수치 미확인) · 점핏 https://jumpit.saramin.co.kr/report/2025/recruit · 한경협 13.4회 https://www.mt.co.kr/industry/2025/12/09/2025120910041034451
주의:
- A×B는 파견·계약직 인건비가 포함된 인력공급 시장이라 채용중개 수수료 시장보다 넓다.
- C는 조사사마다 편차가 크다(Marketintelo는 같은 시장을 USD 2.1B로 봄).
- E는 2022년에 낸 2025년 전망치이지 실적이 아니다.
- F 20만 명·5만 원은 사업계획 가정, 공식 통계 아님.
- G 38.8만 명은 최종보고서와 같은 계산(13.4회는 대학생 대상 조사, 520만 건은 경력직 포함 → «개발 직군 구직자 추정치»). G의 0.92억은 최종보고서 1% 시나리오와 같은 값.
- H 15곳은 내부 목표, 13만 원은 미배포 기획 요금. B2B는 개발 완료·소개서 발송 단계.
- 최종보고서는 B2C 지출 기준 시장(38.8만 명 × 23,700원)만 계산했다 → Q&A: «보고서는 B2C 지출 기준, 발표는 채용 시장 전체로 넓혀 봤다».
⛔ «매출»은 목표 시나리오로만, 실적처럼 말하지 말 것. 5년 SOM 27억 · TAM $2.8B 금지.
[이전 판] TAM 1,132억(B2C 92억 + 지원 520만 건 × 2만 원) · SAM 143억 · SOM 4억 — 11-13 교체.''')




# ================= A23: 소마 이후 B2C 인프라 이전 계획 (11-13 사용자 지시) =================
CSS += r"""
.apx-mig{display:grid;grid-template-columns:1.3fr .7fr;gap:28px;word-break:keep-all;margin:auto 0;align-items:stretch}
.apx-mig .matrix{font-size:23px}
.apx-mig .matrix td,.apx-mig .matrix th{padding:12px 16px;line-height:1.38}
.apx-mig .matrix td:first-child{font-weight:700;color:var(--ink);white-space:nowrap}
.apx-mig .matrix td:nth-child(2){color:var(--muted)}
.apx-mig .matrix td:nth-child(3) b{color:var(--purple-deep)}
.apx-mig .matrix tr.keep td{background:#f6f4fd}
.apx-mig .side{display:flex;flex-direction:column;gap:18px}
.apx-mig .panel{padding:26px 30px}
.apx-mig .k{font-size:21px;font-weight:700;color:var(--purple);margin-bottom:10px}
.apx-mig ol{margin:0;padding-left:28px;font-size:22px;line-height:1.45;color:var(--body)}
.apx-mig ol li{margin-bottom:6px}
.apx-mig ol b{color:var(--ink)}
.apx-mig .fix{display:flex;align-items:baseline;gap:12px}
.apx-mig .fix b{font-size:58px;color:var(--purple-deep);line-height:1}
.apx-mig .fix span{font-size:22px;color:var(--body)}
.apx-mig .sm{font-size:20px;line-height:1.45;color:var(--muted);margin-top:8px}
"""
_MIG = [
    ['프런트', 'S3 + CloudFront, CloudFront Function 라우팅', '<b>Vercel</b> · Next.js 정적 export 그대로, 라우팅과 보안 헤더는 vercel.json'],
    ['API 진입', 'CloudFront /api → VPC Origin → 내부 ALB', '<b>Vercel rewrite /api</b> → Cloudflare Tunnel, VM 인바운드 포트 0'],
    ['API · 분석 worker · 음성', 'ECS Fargate x86 (0.5 + 1×2 + 4 vCPU)', '<b>Oracle Ampere A1 VM 1대</b> (4 OCPU, 24GB) · docker compose · arm64 이미지'],
    ['DB', 'RDS PostgreSQL db.t4g.small, 30GiB', '<b>같은 VM의 PostgreSQL + pgvector</b> · 블록 볼륨, Flyway 그대로'],
    ['업로드 · 백업', 'EFS, RDS 자동 백업', '<b>블록 볼륨</b> + 매일 pg_dump → <b>OCI Object Storage</b>'],
    ['비밀값', 'Secrets Manager', '<b>OCI Vault</b> · 컨테이너 기동 시 주입'],
    ['배포', 'GitHub Actions OIDC → ECR → ECS', '<b>GitHub Actions → GHCR</b> → compose pull, staging → prod 게이트 유지'],
    ['유지', 'Bedrock LLM, SES 메일, Cloudflare DNS, Sentry', '사용량 과금이라 그대로 · Bedrock은 API 키 방식(코드 지원)'],
]
APX.append(shell('Appendix · A21', '소마 이후 B2C 인프라: <span class="purple">AWS에서 Vercel과 Oracle Cloud로</span>', f'''
<div class="apx-mig">
  <div>{table(['구성', '현재 (AWS)', '이전 후'], _MIG, 'left plain').replace('<tr><td>유지<', '<tr class="keep"><td>유지<')}</div>
  <div class="side">
    <div class="panel"><div class="k">고정비</div>
      <div class="fix"><b>월 $20</b><span>Vercel Pro 1석</span></div>
      <div class="sm">유료 상품이 있어 비상업 한정인 Hobby 대신 Pro. Oracle VM, 블록 볼륨 200GB, Object Storage 20GB는 Always Free 범위</div></div>
    <div class="panel"><div class="k">전환 순서</div><ol>
      <li><b>병행 구축</b> · arm64 이미지 빌드, 음성 CER 재측정</li>
      <li><b>DB 이전</b> · 쓰기 중지 후 pg_dump → 복원, 행 수 대조</li>
      <li><b>트래픽 전환</b> · DNS를 Vercel로, AWS는 1주 대기</li>
      <li><b>AWS 정리</b> · RDS 최종 스냅샷 보관 후 삭제</li></ol>
      <div class="sm">되돌리기: DNS를 CloudFront로 복귀</div></div>
    <div class="panel"><div class="k">지금까지 AWS를 쓴 이유</div>
      <div class="sm" style="margin-top:0">소마 예산으로 쓸 수 있는 클라우드 중 서비스 폭이 가장 넓었고, 모델 비교 실험이 잦은 서비스라 여러 모델을 한 계정에서 바로 바꿔 부를 수 있는 Bedrock이 맞았음</div></div>
  </div>
</div>''', source='infra/terraform/prod terraform.tfvars, speech.tf (2026-11-13) · Oracle Cloud Free Tier, Vercel Pricing 공개 요금표'))
APX.note('''소마 지원(AWS 크레딧)이 끝나면 B2C를 Vercel과 Oracle Cloud Always Free로 옮기는 계획입니다. 프런트는 이미 정적 export라 Vercel에 그대로 올리고, API, 분석 worker, 음성 서버, DB를 Oracle Ampere VM 한 대에 compose로 모읍니다. 고정비는 Vercel Pro 월 20달러이고, LLM과 메일은 지금처럼 쓴 만큼 냅니다.

근거(현재 구성): infra/terraform/prod/terraform.tfvars = API 512 CPU/2048MB ×1, 분석 worker 1024/3072 ×2, RDS db.t4g.small 30GiB · speech.tf 기본값 4096/8192 ×1 · foundation nat_gateway_mode single · 전 컨테이너 X86_64. FE next.config.mjs 운영 빌드 output: "export". BE application.yml bedrock.api-key(BEDROCK_API_KEY) 지원 → IAM 역할 없이 호출 가능.
메모리 합계 API 2 + worker 3×2 + 음성 8 = 16GB, DB 포함 약 18GB로 A1 24GB 안. CPU는 4 OCPU라 worker를 1개로 줄이고 운영 지표 보고 조정.
Oracle Always Free: Ampere A1 합계 4 OCPU / 24GB, 블록 볼륨 200GB, Object Storage 20GB, Vault 비밀값 포함, 아웃바운드 월 10TB. 유휴 인스턴스 회수 정책과 A1 용량 부족 때문에 계정은 PAYG로 전환(무료 범위 안이면 0원).
Vercel: Hobby는 비상업 용도 한정, Pro 월 $20/석. /api rewrite로 same-origin 쿠키 유지.
Cloudflare Tunnel: VM이 바깥으로 연결을 열어 인바운드 포트를 열지 않음. 기존 X-Devfit-Origin-Verify 헤더 검사 대신 터널 인증으로 대체.
AWS를 쓴 이유(장표): 소마 예산 처리상 AWS가 쓸 수 있는 서비스가 가장 많았고, 역할별 모델 비교 실험(A10, Table 1 13개 모델)을 한 계정에서 바로 돌릴 수 있는 Bedrock이 서비스 특성에 맞았음.
이전 후 감수하는 것(Q&A용, 장표에서 뺌): VM 1대라 장애 시 전체 중단 · CPU가 Fargate 합계(6.5 vCPU)보다 작아 분석 worker 동시 실행 2 → 1.
⛔ 아직 실행하지 않은 계획. «이전 완료»·«비용 0원» 금지(Vercel Pro와 LLM 사용량은 계속 나감). 현재 AWS 월 청구액은 근거 자료가 없어 장표에 비교 수치를 쓰지 않음. B2B 콘솔은 이 장의 범위 밖.''')
