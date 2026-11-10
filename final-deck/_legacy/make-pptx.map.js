const fs = require("fs"), path = require("path"), pptxgen = require("pptxgenjs");
const B = __dirname;
const IMG = B + "/img";
const src = fs.readFileSync(B + "/notes-source.js", "utf8");
const re = /S\(\s*("(?:[^"\\]|\\.)*"|`[^`]*`|'[^']*')\s*,\s*("(?:[^"\\]|\\.)*"|`[^`]*`)\s*,\s*("(?:[^"\\]|\\.)*"|`[^`]*`)/g;
const N = []; let m; while ((m = re.exec(src))) N.push(eval(m[3]));
const extra = [...src.matchAll(/s\.addNotes\(("(?:[^"\\]|\\.)*")\)/g)].map(x => eval(x[1]));
if (N.length !== 34 || extra.length < 2) throw new Error(`notes parse: ${N.length} / ${extra.length}`);
const fix = t => t
  .replace("결정론 알고리즘이 본인 커밋을 고르고", "규칙 점수로 본인 커밋을 고르고(커밋 판정 모델은 섞기만 하고)")
  .replace("이 압축은 LLM 없이 결정론 점수로 합니다.", "압축의 뼈대는 규칙 점수이고, 커밋 판정 모델은 섞기만 합니다. 모델이 실패해도 규칙식만으로 끝까지 돕니다.")
  .replace("결정론 점수 = 로직 밀도", "규칙 점수 = 로직 밀도");
const map = { 1: extra[0], 29: extra[1] };
[[2,0],[3,1],[4,2],[5,3],[6,4],[7,5],[8,6],[9,7],[11,8],[12,9],[15,10],[16,11],[17,12],[18,13],[19,14],[20,15],[21,16],[22,17],[24,18],[25,19],[26,20],[27,21],[28,22],[31,23]].forEach(([f, c]) => map[f] = fix(N[c]));
for (let i = 32; i <= 41; i++) map[i] = N[i - 8];
map[10] = "[구분] Development — 기술 3.1~3.7 → 수행과정 3.8~3.12 순서로 넘어갑니다.";
map[13] = "[9:00–9:10] 커밋을 고르는 점수식입니다. 잡음 커밋을 빼고, 메시지를 기술 키워드와 구체성으로 순위를 매긴 뒤, 커밋 판정 모델 점수를 섞습니다. 모델이 없거나 늦거나 절반도 채점하지 못하면 규칙식만으로 끝까지 갑니다. 동점은 sha 순서로 깨서 같은 입력이면 같은 순서가 나옵니다.\n\n근거: 운영 브랜치 GithubService.orderCommitProbes · CommitDecisionBlend · application.yml(keyword 0.40 / specificity 0.60 / message-weight 0.6 / patch-weight 0.5, repo-deadline 25초, MIN_COVERAGE 0.5). 패치 판정은 품질 점수를 0.5~1.5배로 조정.\n⛔ «커밋 선별 LLM 0회» 금지 — 운영은 OpenAI gpt-6-luna 판정을 섞는다(R1 국외 이전 고지 확인).\nQ&A: 왜 모델 비중 0.6? → 설정값이고 실패 시 규칙식으로 떨어지는 구조가 핵심. 가중치 근거 실험은 diagnostics 로그.";
map[14] = "[9:10–9:20] 공고는 29곳에서 받습니다. 기업 채용 사이트는 사이트 하나가 클래스 하나이고, 등록은 한 줄입니다. 모든 접속은 SafeFetcher를 거쳐 리다이렉트마다 허용 호스트를 다시 검사합니다. 이미지로만 된 공고는 OCR로 읽고, 접수 중 공고는 미리 캐시해 두어 다시 들어오면 네트워크도 LLM도 부르지 않습니다.\n\n근거: prep/corporate(CorporateSite 인터페이스, CorporateSiteRegistry, SafeFetcher, CorporateSiteSourceRulesTest가 Jsoup.connect 0건 잠금) · prep/cache(V59~V60, TTL 30일, 일일 LLM 1,000·OCR 300). OCR 폴백은 본문 200자 미만일 때만.\n⛔ 회사 로고·«제휴» 표현 금지 — 회사명도 장표에 넣지 않음. ⛔ «공고 1,450건 사전 수집» 본편 금지.";
map[23] = "[구분] Effect — 결과와 기대효과.";
map[30] = "Q&A로 넘어갑니다. 부록은 쪽번호로 바로 엽니다(31장 목차).";
// 목차(2장) 제거: 2장 노트 버리고 3장 이후를 한 칸씩 당긴다
{ const m2 = {}; for (const k of Object.keys(map)) { const n = +k; if (n === 2) continue; m2[n > 2 ? n - 1 : n] = map[k]; } for (const k of Object.keys(map)) delete map[k]; Object.assign(map, m2); }
map[29] = "Q&A로 넘어갑니다. 부록은 쪽번호로 바로 엽니다(30장 목차).";
// 4.3 = 사업자 + 특허 한 장 (2026-11-05)
map[25] = (map[25] || "") + "\n\n[증빙] 직업정보제공사업 신고확인증(서울청 제2026-31호, 신고일 10-19)·통신판매업 신고증(제2026-서울서초-3702호, 11-02)·특허 출원번호통지서 3건(11-01) 원본 그대로(자르지 않고 가리지 않음). 오른쪽 아래 띠 = devfit.app 푸터 사업자 정보 고지(사업자등록번호 640-21-02214).\n⛔ «특허 등록»·«회사 특허» 금지 — 출원인은 김건우 개인, 출원 단계.";
// 3.7 원가 분리 + 다음 조치·미구현 제거 (2026-11-05)
{ const m2 = {}; for (const k of Object.keys(map)) { const n = +k; m2[n >= 17 ? n + 1 : n] = map[k]; } for (const k of Object.keys(map)) delete map[k]; Object.assign(map, m2); }
map[16] = "[9:40–9:50] 배포 경로마다 게이트가 있습니다. main에서는 테스트와 FE·BE API 계약 대조가 112번 막았고, prod PR은 head가 staging인지 검사해 18번 막았습니다. prod push에서는 병합된 staging→prod PR이 없으면 배포 전에 멈춥니다. 이렇게 배포 직전에 막힌 운영 push가 13건이고, 그중 실제로 운영에 나간 변경은 0건입니다.\n\n출처: collect/B §6(실패 실행 140건 jobs API, scripts/gates.py). 13건 = 승격 11 + 유출 1 + 테스트 1. 배포 잡 429–488초 → 145–260초는 같은 기간 실측일 뿐 원인 단정 금지.\n⛔ «SBOM 차단» 금지(main에만 있고 운영 미반영).";
map[17] = "[9:50–10:00] LLM 호출마다 모델 단가와 토큰을 원장에 남겨서 원가를 셉니다. 분석 1회 약 133원, 공고 1건 약 252원이고 단건 가격은 1,900원입니다. 원가의 81%가 학습 질문 생성, 모델로는 GLM-5가 약 99%입니다.\n\n출처: collect/A §5. 90일 원장 5,391건(성공 99.3%), 단가 설정 호출 2,881건 $32.77, 분석 346회 · 공고 182건, 1 USD = 1,400원. 하한값: 단가 미설정 gpt-6-luna 2,349건 포함 시 분석 1회 약 150원 추정. 원가의 94%가 LLM.\n⛔ 8월 330원 대비 «60% 절감» 금지(정의 다름).\nQ&A: 마진? → 원가 대비 가격이 10배 이상이지만 인프라·결제 수수료 별도.";
map[22] = "[12:10–12:30] 가장 큰 이탈은 방문에서 가입입니다. 원인을 좁혀 보니 Instagram 인앱 브라우저로 들어온 사람의 가입 전환이 다른 유입의 약 10분의 1이었습니다. 광고를 멈춘 11월 1~4일에는 세션 1,000개당 가입이 12.3으로 8월 수준에 가까웠습니다.\n\n출처: collect/D §1·§4. 방문 = Clarity(봇 제외), 가입 = 관리자 DB → 도구가 달라 0.4%는 «대략»으로만. 월 비교는 자연 실험(통제 실험 아님), 8월은 팀·멘토 가입 포함, 11월은 표본 작음.";
for (const k of Object.keys(map)) map[k] = map[k].replace(/\n블라인드 사람 채점 78문항 진행 중[^\n]*/, "").replace(/\n🔄 블라인드 사람 채점[^\n]*/, "");
map[30] = "Q&A로 넘어갑니다. 부록은 쪽번호로 바로 엽니다(31장 목차).";
map[26] = map[26].replace("[증빙] ", "[증빙] 사업자등록증(640-21-02214, 개업 2026-09-02, 서초세무서)·");
// Problem = 경험 위주 기술면접 주장, 면접관 제외 (2026-11-06)
map[2] = "[0:20–1:00] AI가 코드를 같이 짜는 게 기본이 됐습니다. 그래서 기술면접은 무엇을 만들었느냐보다, 왜 그렇게 짰는지·어디서 막혔는지·무엇을 바꿨는지, 즉 경험 위주로 묻습니다. 그런데 지원자는 자기 코드에서 무엇을 물을지 모릅니다.\n\n주장: «AI 발전으로 경험 위주 기술면접이 늘었다»는 팀 주장(last-dance/claims.md C1) — 이를 직접 재는 수치는 없음. 받치는 근거만 숫자로: 84%·46% = Stack Overflow Developer Survey 2025, 60% = WGU Workforce Decoded 2026(미국 채용 실무자 n=3,128, 반드시 «미국» 표기). 인용 = collect/D P1(현직 개발자, 09-07 녹취).\n⛔ «연봉 30%» 금지. ⛔ «경험 면접 N% 증가» 같은 수치 지어내기 금지.";
const html = fs.readFileSync("/Users/aiden/dev/teams/ASM/last-dance/final-deck/index.html", "utf8");
const titles = html.match(/data-title="[^"]*"/g).map(t => t.slice(12, -1).replace(/&amp;/g, "&"));
const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE";
pres.title = "DevFit 최종발표 — Team Dozer"; pres.author = "Team Dozer";
const imgs = fs.readdirSync(IMG).filter(f => f.endsWith(".jpg")).sort();
if (imgs.length !== titles.length) throw new Error(`imgs ${imgs.length} vs titles ${titles.length}`);
imgs.forEach((f, i) => {
  const s = pres.addSlide();
  s.addImage({ path: path.join(IMG, f), x: 0, y: 0, w: 13.333, h: 7.5, altText: titles[i] });
  if (map[i + 1]) s.addNotes(map[i + 1]);
});
pres.writeFile({ fileName: "/Users/aiden/dev/teams/ASM/last-dance/11-최종발표-완성본.pptx" })
  .then(f => console.log("ok", f, imgs.length, "notes", Object.keys(map).length));
