// DevFit 최종발표 — 콘텐츠 완성본 (디자인 미적용). 구조 = 06-최종구성.md v1.3 / 07-구성-와이어프레임.pptx 26장 + 부록 A1~A10
const pptxgen = require("pptxgenjs");
const path = require("path");
const IMG = (f) => path.join(__dirname, "img", f);
const OUT = process.argv[2] || path.join(__dirname, "deck.pptx");

const THEME = {
  name: "DevFit Content Draft", headFontFace: "Pretendard", bodyFontFace: "Pretendard",
  colors: { dk1: "111111", lt1: "FFFFFF", dk2: "444444", lt2: "F2F2F2", accent1: "6C5CE7", accent2: "9A9A9A",
    accent3: "D63031", accent4: "005CE6", accent5: "CCCCCC", accent6: "555555", hlink: "005CE6", folHlink: "6C5CE7" },
};
const HEX = { line: "BBBBBB", grid: "E5E5E5", mute: "777777", acc: "6C5CE7", grey: "9A9A9A" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "DevFit 최종발표 (콘텐츠 완성본)";
pres.author = "Team Dozer";
const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: "CONTENT", background: { color: "FFFFFF" },
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: 0.6, y: 0.35, w: 12.1, h: 0.4, fontSize: 13, color: C.text2, margin: 0 }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.75, w: 12.1, h: 0.95, fontSize: 30, bold: true, color: C.text1, margin: 0, valign: "top", align: "left" }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: "777777", align: "right" },
});
pres.defineSlideMaster({
  title: "COVER", background: { color: "FFFFFF" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.2, w: 11.7, h: 1.4, fontSize: 54, bold: true, color: C.text1, margin: 0, align: "left" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.7, w: 11.7, h: 1.6, fontSize: 22, color: C.text2, margin: 0, valign: "top" }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: "777777", align: "right" },
});

const ACK = "이 성과는 2026년도 과학기술정보통신부의 재원으로 정보통신기획평가원의 지원을 받아 수행된 결과물임 (IITP-2026-AI·SW마에스트로)";
const ACK_EN = "This work was supported by the Institute of Information & Communications Technology Planning & Evaluation(IITP) grant funded by the Ministry of Science and ICT(MSIT) (IITP-2026-AI·SW Maestro)";

// ---------- helpers ----------
let sec = "";
function S(kicker, title, notes) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: sec });
  if (kicker) s.addText(kicker, { placeholder: "kicker" });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  return s;
}
function T(s, text, o) { s.addText(text, Object.assign({ isTextBox: true, fontSize: 16, color: C.text1, valign: "top", margin: 0.05 }, o)); }
function bullets(s, items, o) {
  const arr = items.map((t, i) => {
    const sub = typeof t === "object" && t.sub;
    const txt = typeof t === "object" ? t.t : t;
    return { text: txt, options: { bullet: sub ? { indent: 18 } : true, indentLevel: sub ? 1 : 0, breakLine: i < items.length - 1, fontSize: sub ? 13 : (o && o.fontSize) || 16, color: sub ? C.text2 : C.text1 } };
  });
  s.addText(arr, Object.assign({ isTextBox: true, valign: "top", paraSpaceAfter: 6, margin: 0.05 }, o));
}
function box(s, x, y, w, h, name) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: "FFFFFF" }, line: { color: HEX.line, width: 1 }, objectName: name });
}
function stat(s, x, y, w, big, label, o) {
  o = o || {};
  if (o.box !== false) box(s, x, y, w, o.h || 1.7, "stat " + big);
  s.addText(big, { isTextBox: true, x: x + 0.15, y: y + 0.12, w: w - 0.3, h: 0.85, fontSize: o.size || 40, bold: true, color: C.text1, margin: 0, valign: "middle", fit: "shrink" });
  s.addText(label, { isTextBox: true, x: x + 0.15, y: y + 0.98, w: w - 0.3, h: (o.h || 1.7) - 1.05, fontSize: o.lsize || 13, color: C.text2, margin: 0, valign: "top" });
}
function source(s, text, y) { s.addText(text, { isTextBox: true, x: 0.6, y: y || 6.85, w: 11.5, h: 0.4, fontSize: 10, color: "777777", margin: 0, valign: "bottom" }); }
function todo(s, text, x, y, w, h) {
  s.addText("【" + text + "】", { isTextBox: true, x, y, w, h: h || 0.45, fontSize: 13, color: C.text1, highlight: "FFFF00", margin: 0.05, valign: "middle" });
}
function badge(s, x, y, w, text) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h: 0.5, rectRadius: 0.08, fill: { color: "F2F2F2" }, line: { color: HEX.line, width: 1 }, objectName: "badge " + text });
  s.addText(text, { isTextBox: true, x, y, w, h: 0.5, fontSize: 13, bold: true, align: "center", valign: "middle", color: C.text1, margin: 0 });
}
function table(s, head, rows, o) {
  const H = head.map((t) => ({ text: t, options: { bold: true, fill: { color: "F2F2F2" } } }));
  s.addTable([H].concat(rows.map((r) => r.map((c) => (typeof c === "object" ? c : { text: String(c) })))),
    Object.assign({ x: 0.6, y: 1.9, w: 12.1, fontSize: 13, color: "111111", border: { type: "solid", pt: 0.75, color: HEX.line }, valign: "middle", margin: 0.06, fontFace: "Pretendard" }, o));
}
function flow(s, steps, x, y, w, h, o) {
  o = o || {};
  const gap = 0.35, n = steps.length, bw = (w - gap * (n - 1)) / n;
  steps.forEach((t, i) => {
    const bx = x + i * (bw + gap);
    box(s, bx, y, bw, h, "flow " + i);
    s.addText(t, { isTextBox: true, x: bx + 0.08, y, w: bw - 0.16, h, fontSize: o.fontSize || 15, align: "center", valign: "middle", color: C.text1, margin: 0 });
    if (i < n - 1) s.addShape(pres.shapes.RIGHT_ARROW, { x: bx + bw + 0.06, y: y + h / 2 - 0.12, w: gap - 0.12, h: 0.24, fill: { color: "999999" }, line: { color: "999999" }, objectName: "arrow " + i });
  });
}
function quote(s, x, y, w, h, q, who) {
  box(s, x, y, w, h, "quote");
  s.addText([{ text: q, options: { fontSize: 17, italic: true, breakLine: true } }, { text: "— " + who, options: { fontSize: 12, color: C.text2 } }],
    { isTextBox: true, x: x + 0.15, y: y + 0.1, w: w - 0.3, h: h - 0.2, valign: "middle", margin: 0, paraSpaceAfter: 6 });
}
const chartBase = (title) => ({ showTitle: !!title, title, titleFontSize: 13, titleFontFace: "+mn-lt", catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", dataLabelFontFace: "+mn-lt",
  catAxisLabelColor: "444444", valAxisLabelColor: "777777", catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, valGridLine: { color: "E5E5E5", size: 0.5 }, catGridLine: { style: "none" }, dataLabelFontSize: 11, dataLabelColor: "111111" });

// ================= 표지 · 목차 =================
sec = "표지 · 목차"; pres.addSection({ title: sec });
{
  const s = pres.addSlide({ masterName: "COVER", sectionTitle: sec });
  s.addText("DevFit", { placeholder: "title" });
  s.addText([{ text: "내 코드로 준비하는 공고 맞춤 기술면접", options: { breakLine: true } }, { text: "Team Dozer · 박천웅 · 김건우 · 노재원 · SW Maestro 17기 최종평가", options: { fontSize: 16 } }], { placeholder: "body" });
  s.addText([{ text: ACK, options: { breakLine: true } }, { text: ACK_EN }], { isTextBox: true, x: 0.8, y: 6.3, w: 11.7, h: 0.8, fontSize: 10, color: "777777", margin: 0, valign: "bottom" });
  s.addNotes("[0:00–0:10] 안녕하세요, 내 코드로 준비하는 공고 맞춤 기술면접 DevFit, Team Dozer입니다.\n\n사사문구 국문·영문: 00-평가안내.md §사사문구 원문 그대로.");
}
{
  const s = S("", "목차", "[0:10–0:20] 소개 → 시연 → 개발(기술·수행과정) → 효과 순서로 말씀드립니다.\n배점: 결과물 50 · 수행과정 20 · 기대효과 30 (00-평가안내.md)");
  const items = [["1", "소개", "1.1 문제 · 1.2 솔루션 · 1.3 차별점", "p3–8"], ["2", "시연", "Live Demo 5분", "p9"], ["3", "개발", "3.1–3.5 기술 · 3.6–3.10 수행과정", "p10–19"], ["4", "Effect", "4.1–4.3 지금까지 · 4.4 앞으로", "p20–24"], ["5", "마무리", "", "p25"]];
  items.forEach((it, i) => {
    const y = 1.95 + i * 0.82;
    T(s, it[0], { x: 0.6, y, w: 0.6, h: 0.6, fontSize: 26, bold: true });
    T(s, it[1], { x: 1.3, y, w: 2.6, h: 0.6, fontSize: 22, bold: true });
    T(s, it[2], { x: 4.0, y: y + 0.07, w: 6.0, h: 0.5, fontSize: 15, color: C.text2 });
    T(s, it[3], { x: 10.3, y: y + 0.07, w: 1.4, h: 0.5, fontSize: 13, color: C.text2 });
  });
  table(s, ["배점", "결과물 50", "수행과정 20", "기대효과 30"], [["해당 장표", "1.3 차별점 ~ 3.5 기술 (+ 시연)", "3.6 ~ 3.10", "4. Effect"]], { x: 0.6, y: 6.15, w: 12.1, fontSize: 12, colW: [1.6, 4.0, 3.0, 3.5] });
}

// ================= 1. 소개 =================
sec = "1. 소개"; pres.addSection({ title: sec });
{
  const s = S("1.1 문제", "면접은 이제 «짰나»가 아니라 «알고 짰나»를 묻는다",
    "[0:20–1:00] AI가 코드를 짜 주는 시대가 됐습니다. 그래서 면접은 구현했느냐보다, 알고 구현했느냐를 묻습니다. 그런데 지원자는 자기 코드에서 무엇을 물을지 모르고, 면접관은 지원자 코드를 다 읽을 시간이 없습니다.\n\n출처: 인용 = collect/D P1(현직 개발자, 09-07 녹취). 통계 = WGU Workforce Decoded 2026(미국 채용 실무자 n=3,128) — 반드시 «미국» 표기. 보조 = Stack Overflow Developer Survey 2025.\n⛔ «연봉 30%» 금지.");
  box(s, 0.6, 1.95, 5.9, 1.55, "card 지원자");
  T(s, [{ text: "지원자", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "자기 코드에서 무엇을 물을지 모른다", options: { fontSize: 16 } }], { x: 0.8, y: 2.05, w: 5.5, h: 1.35 });
  box(s, 6.8, 1.95, 5.9, 1.55, "card 면접관");
  T(s, [{ text: "면접관", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "지원자 코드를 읽을 시간이 없다", options: { fontSize: 16 } }], { x: 7.0, y: 2.05, w: 5.5, h: 1.35 });
  quote(s, 0.6, 3.75, 5.9, 1.6, "«1달 전에 짠 코드 잘 기억이 안 나거든요»", "현직 개발자 인터뷰");
  stat(s, 6.8, 3.75, 5.9, "60%", "미국 채용 담당자 «AI 때문에 지원자의 실제 역량 평가가 더 어려워졌다»", { h: 1.6 });
  T(s, "보조: 개발자 84% AI 도구 사용(또는 계획) · 46% AI 결과 정확도 불신", { x: 0.6, y: 5.6, w: 12.1, h: 0.45, fontSize: 14, color: C.text2 });
  source(s, "출처: WGU, Workforce Decoded 2026 (미국 채용 실무자 n=3,128) · Stack Overflow Developer Survey 2025 · 현직 개발자 인터뷰(2026-09-07)");
}
{
  const s = S("1.1 문제", "«Claude Code에 GitHub 링크 주면 되지 않나요?»",
    "[1:00–1:40] 실제로 가장 많이 들은 반론입니다. 그래서 실험했습니다. 공개 레포 4개, 같은 공고, 같은 지시. 레포 링크만 받은 채팅형 AI는 «레포를 확인해 보니»라고 쓰고는 근거 18개를 전부 지어냈습니다. DevFit은 28개 모두 실존했습니다. 차이는 모델이 아니라 절차입니다.\n\n출처: collect/E-compare.md (2026-11-05 파일럿, 결정론 채점·LLM 0회).\nQ&A 대비(덱 미기재): clone한 Claude Code는 30/32 실존·식별자 짚기는 더 높음 → «잘 지시하면 찾는다. 그 지시와 대조를 사용자가 매번 해야 한다. DevFit은 서버가 매번 강제 + 공고 단위 흐름 + 본인 커밋 필터 + 음성 모의면접». Greenroom(GitHub 레포 분석 모의면접) 존재.\n⛔ «유일»·«최초»·«AI는 레포를 못 읽는다»·«Claude보다 정확» 금지.\n🔴 인용 실명은 동의 후에만 — 현재 역할만 표기.");
  quote(s, 0.6, 1.9, 5.9, 1.15, "«이미 내가 쓰는 AI로 다 준비하는 부분»", "개발자 사용자 인터뷰");
  quote(s, 6.8, 1.9, 5.9, 1.15, "«GitHub 링크를 Claude Code에 넘기면 된다»", "IT 기업 대표 (서면 회신, 10-26)");
  T(s, "실험 — 공개 레포 4개 · 같은 공고 · 같은 지시", { x: 0.6, y: 3.25, w: 12.1, h: 0.4, fontSize: 15, bold: true });
  stat(s, 0.6, 3.7, 5.9, "0 / 18", "레포 링크만 받은 채팅형 AI — 제시한 근거 중 실존 0개 («레포를 확인해 보니»라고 쓰고 없는 커밋·파일을 만듦)", { h: 1.75 });
  stat(s, 6.8, 3.7, 5.9, "28 / 28", "DevFit — 제시한 근거 전부 실존 (커밋 SHA · 파일 · 코드)", { h: 1.75 });
  table(s, ["", "입력", "본인 커밋만 골라 읽기", "한국 채용 공고 맞춤"], [["AI 모의면접 (사람인·Final Round 등)", "이력서", "X", "일부"], ["DevFit", "공고 URL + GitHub", "O", "29곳 (플랫폼 5 + 기업 24)"]], { y: 5.55, fontSize: 11, colW: [3.6, 2.6, 2.6, 3.3], rowH: 0.27 });
  T(s, "차이는 모델이 아니라, 레포를 읽고 대조하는 절차를 서버가 매번 강제하는가입니다.", { x: 0.6, y: 6.62, w: 11.5, h: 0.38, fontSize: 14, bold: true });
}
{
  const s = S("1.2 솔루션   |   결과물 50", "공고 URL 하나 + 내 GitHub → 그 공고용 면접 질문 → 음성 모의면접",
    "[1:40–2:10] 공고 URL 하나와 내 GitHub만 있으면 됩니다. 그 공고에 맞춘 질문이 나오고, 질문마다 그 질문이 나온 내 코드가 붙고, 음성으로 연습까지 합니다. 같은 레포라도 공고만 바꾸면 질문이 달라집니다.\n\n출처: collect/C §2-1 (같은 레포 × 공고 2개, 115문항, 문장 동일 0개).\n⛔ «주제가 겹치지 않는다»로 확대 금지(문장 기준 0개일 뿐). ⛔ «점수·랭킹 없음» 금지 → «합불 판정·랭킹 없음»까지만.");
  flow(s, ["① 공고 URL 붙여넣기\n(또는 이미지)", "② 내 GitHub 레포 선택\n(공개/비공개 범위 선택)", "③ 공고 맞춤 질문\n+ «이 질문이 나온 내 코드»", "④ 텍스트·음성 모의면접\n+ 꼬리질문"], 0.6, 2.0, 12.1, 1.5);
  stat(s, 0.6, 3.95, 5.9, "0개", "같은 레포에 공고만 바꿨을 때 문장이 같은 질문 (115문항)", { h: 1.6 });
  stat(s, 6.8, 3.95, 5.9, "29곳", "공고 자동 수집 — 채용 플랫폼 5곳 + 기업 채용사이트 24곳", { h: 1.6 });
  T(s, "합불 판정·랭킹 없음 — 최종 판단은 사람", { x: 0.6, y: 5.8, w: 12.1, h: 0.45, fontSize: 16, bold: true });
  source(s, "채용 플랫폼: 잡코리아·사람인·원티드·링커리어·인크루트 · 수치: 질문 품질 평가 세트(2026-11)");
}
{
  const s = S("1.3 차별점 ①   |   결과물 50", "근거가 없으면 묻지 않는다",
    "[2:10–2:40] 첫째, 근거가 없으면 묻지 않습니다. 질문 속에 나오는 코드 이름이 실제 코드에 없으면 서버가 그 질문을 버립니다. 그래서 모든 질문에 커밋과 파일 출처가 붙어 있고, 운영에서도 최근 30일 동안 84건을 실제로 걸러냈습니다.\n\n화면: 팀원 본인 레포(Signify) × 토스 FE 공고, Q3 useCamera — 질문 식별자 4개가 근거 diff에 모두 보임 (collect/screens/F-02).\n출처: 353/353 = collect/C 평가 세트 전수 · 84건 = 관리자 콘솔 운영 품질 필터 최근 30일(collect/A §7) · 63개 중 5개 = 출력 게이트 실행 1회.\n⛔ «46/46 일치» 금지. ⛔ «근거가 부족하면 LLM을 부르지도 않는다» 삭제(입력 게이트 실발동 THIN 3/227로 미미).");
  s.addImage({ path: IMG("q3.jpg"), x: 0.6, y: 1.9, w: 7.2, h: 7.2 * 672 / 1127, altText: "질문과 근거 코드 화면 (Signify Q3 useCamera)" });
  T(s, "질문 속 식별자(useCamera · useEffect · cancelled 등)가 아래 근거 diff에 그대로 보인다", { x: 0.6, y: 6.25, w: 7.2, h: 0.5, fontSize: 12, color: C.text2 });
  stat(s, 8.1, 1.9, 4.6, "353 / 353", "모든 질문에 커밋·파일 출처", { h: 1.45 });
  stat(s, 8.1, 3.5, 4.6, "84건", "운영 품질 필터가 실제로 걸러낸 질문 (최근 30일)", { h: 1.45 });
  stat(s, 8.1, 5.1, 4.6, "63 중 5", "출력 게이트가 폐기한 질문 (실행 1회)", { h: 1.25 });
  badge(s, 8.1, 6.5, 4.6, "특허 출원 10-2026-0214809");
}
{
  const s = S("1.3 차별점 ②   |   결과물 50", "내가 짠 코드만 본다",
    "[2:40–3:05] 둘째, 내가 짠 코드만 봅니다. 팀 프로젝트라면 남이 짠 코드로 질문을 만들면 안 되겠죠. 본인 커밋은 1.0, 공동 작성은 0.70으로 가중하고, 남의 커밋은 아예 제외합니다.\n\n출처: GithubService 귀속 가중치(본인 1.0 / 공동 작성 0.70 / 타인 제외), 09-09 운영 반영.\n특허: 10-2026-0214808 «코드 저장소 기반 면접 질문 선별 방법 및 시스템» (출원인 김건우 개인, 발명자 3명). ⛔ «특허 등록»·«회사 특허» 금지.");
  stat(s, 0.6, 2.1, 3.8, "1.0", "본인 커밋", { h: 1.9, size: 54 });
  stat(s, 4.75, 2.1, 3.8, "0.70", "공동 작성 커밋", { h: 1.9, size: 54 });
  stat(s, 8.9, 2.1, 3.8, "제외", "남의 커밋", { h: 1.9, size: 54 });
  T(s, "팀 프로젝트에서 남이 짠 코드로는 출제하지 않는다", { x: 0.6, y: 4.4, w: 12.1, h: 0.6, fontSize: 20, bold: true });
  badge(s, 0.6, 5.3, 4.6, "특허 출원 10-2026-0214808");
}
{
  const s = S("1.3 차별점 ③   |   결과물 50", "품질을 숫자로 잰다",
    "[3:05–3:20] 셋째, 품질을 숫자로 잽니다. AI 심판에게 질문만 보여 주고 작업 요약 4개 중 이 질문이 어디서 나왔는지 맞히게 했더니 81.9%를 맞혔습니다. 우연이면 25%입니다. 질문이 그만큼 특정 코드에 붙어 있다는 뜻입니다.\n\n출처: collect/C (n=177, 4지선다, 우연 25%).\n⛔ «근거 코드 4개 중» 표기 금지(정확히는 «작업 4개 요약 중»). ⛔ QI(점수) 상승 주장 금지.");
  stat(s, 0.6, 2.0, 5.6, "81.9%", "AI 심판이 질문만 보고 작업 4개 요약 중 원래 작업을 맞힌 비율 (n=177)", { h: 2.4, size: 72 });
  s.addChart(pres.charts.BAR, [{ name: "정답률", labels: ["우연(4지선다)", "DevFit 질문"], values: [25, 81.9] }],
    Object.assign(chartBase("근거 특정성 — 정답률(%)"), { x: 6.6, y: 1.9, w: 6.1, h: 4.4, barDir: "col", chartColors: ["9A9A9A", "6C5CE7"], showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.0\"%\"", valAxisMaxVal: 100, valAxisMinVal: 0, showLegend: false, varyColors: true }));
  source(s, "측정: 질문 품질 평가 하네스, 4지선다 식별 과제 · 우연 기준선 25%");
}

// ================= 2. 시연 =================
sec = "2. 시연"; pres.addSection({ title: sec });
{
  const s = S("2. 시연   |   결과물 50", "Live Demo",
    "[3:20–8:20] 라이브 시연 5분 — 대본·체크리스트 정본: collect/F-audit-demo.md\n" +
    "0:20 캐시된 토스 공고 URL 붙여넣기 → 약 1초 수집\n0:50 Aiden-WEB × 토스증권 FE 플랫폼 라이브 분석 시작 (분석 55초~196초 편차)\n1:15 사전 분석 카드 Signify × 토스 FE (d0a79334) Q3 useCamera — 근거 코드 펼치기 · 꼬리질문\n2:45 음성 모의면접 질문 1개 답변 → 꼬리질문\n3:45 라이브 카드 Q2·Q5만 열기 (72%에서 정체 시 예비 카드 bf264e16로 전환)\n4:25 지원 여정 캘린더\n\n시연 전 체크: 진행 중 분석 0개(플로팅 버튼이 «분석» 버튼을 덮음) · 리뷰 팝업·동의 배너 미리 처리 · 당일 아침 캐시된 공고 확인.\n⛔ Ddareungi 레포 라이브 금지(API 엔드포인트 노출) · 근거 파일 어긋난 문항·기출 매칭 블록은 열지 않음.\n영상은 실시간 시연으로 인정되지 않음 → 장애 시 미리 분석한 카드로 전환.");
  T(s, "https://devfit.app", { x: 0.6, y: 3.0, w: 12.1, h: 1.0, fontSize: 40, bold: true, align: "center", valign: "middle" });
  T(s, "공고 URL 붙여넣기 → 레포 선택 → 질문과 근거 코드 → 음성 답변 · 꼬리질문", { x: 0.6, y: 4.2, w: 12.1, h: 0.6, fontSize: 18, color: C.text2, align: "center" });
}

// ================= 3. 개발 — 기술 =================
sec = "3. 개발 — 기술"; pres.addSection({ title: sec });
{
  const s = S("3.1 아키텍처   |   결과물 50", "공고와 내 코드를 근거로 묶고, 게이트를 통과한 질문만 내보낸다",
    "[8:20–8:40] 공고와 레포를 수집하고, 결정론 알고리즘이 본인 커밋을 고르고 근거로 묶은 다음, 게이트를 통과한 질문만 내보냅니다. LLM은 역할별 5개 모델로 나눠 쓰고, 분석은 DB 큐와 워커로 비동기 처리합니다.\n\n그림: 운영 브랜치 기준 시스템 구성도(2026-11-03, 최종보고서 그림 1과 동일).\n모델: Bedrock reasoning GLM-5 · code Qwen3-Coder-Next · extraction GLM-4.7-Flash · vision Nova 2 Lite · business-ocr Qwen3-VL / 임베딩 Cohere Embed Multilingual v3 / 커밋 근거 가치 판정 OpenAI gpt-6-luna.\n🔴 OpenAI 호출이 개인정보처리방침 국외 이전에 미고지(R1) — 발표 전 정리.");
  s.addImage({ path: IMG("arch.png"), x: 0.6, y: 1.85, w: 8.2, h: 8.2 * 1350 / 2400, altText: "DevFit 시스템 구성도" });
  flow(s, ["공고 수집", "레포 수집", "커밋 선별", "근거 묶음", "게이트", "질문 생성", "학습실·음성"], 0.6, 6.6, 12.1, 0.55, { fontSize: 12 });
  table(s, ["역할", "모델"], [["추론", "GLM-5"], ["코드", "Qwen3-Coder-Next"], ["추출", "GLM-4.7-Flash"], ["비전", "Nova 2 Lite"], ["사업자 OCR", "Qwen3-VL"]], { x: 9.1, y: 1.85, w: 3.6, fontSize: 12, colW: [1.3, 2.3] });
  T(s, "모델 5종 역할별 라우팅 (Amazon Bedrock)\nDB 큐 + 워커 원자 선점 + 지수 백오프 재시도", { x: 9.1, y: 4.5, w: 3.6, h: 1.4, fontSize: 13 });
}
{
  const s = S("3.2 커밋 선별 + 입력·출력 게이트   |   결과물 50", "커밋 1,000개를 질문 4개까지 좁히는 동안 LLM은 마지막에만 쓴다",
    "[8:40–9:00] 커밋 최대 1,000개에서 diff 96개, 작업 단위 4~10개로 좁힌 뒤 작업당 질문을 최대 4개 만듭니다. 이 압축은 LLM 없이 결정론 점수로 합니다. 앞뒤에 게이트가 있습니다.\n\n출처: collect/C (B2C 경로). 결정론 점수 = 로직 밀도·기술 키워드·시간 희소성.\n⛔ «1,000 → 12 → 6»은 B2B 경로 숫자 — 이 장표에 쓰지 않음.\nQ&A: 입력 게이트 실발동은 THIN 3/227로 적음 → «출력 게이트·운영 품질 필터(30일 84건)로 답».");
  flow(s, ["커밋\n최대 1,000", "diff\n최대 96", "작업 단위\n4~10개", "작업당 질문\n최대 4개"], 0.6, 2.0, 12.1, 1.4, { fontSize: 20 });
  T(s, "결정론 점수 (LLM 0회): 로직 밀도 · 기술 키워드 · 시간 희소성", { x: 0.6, y: 3.5, w: 9.0, h: 0.4, fontSize: 13, color: C.text2 });
  box(s, 0.6, 4.15, 5.9, 2.2, "input gate");
  T(s, [{ text: "입력 게이트", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "근거 코드가 20줄 미만이면 «왜»·«트레이드오프» 유형만 허용 — 얇은 근거로 사실 확인형 질문을 지어내지 않게", options: { fontSize: 15 } }], { x: 0.8, y: 4.25, w: 5.5, h: 2.0 });
  box(s, 6.8, 4.15, 5.9, 2.2, "output gate");
  T(s, [{ text: "출력 게이트", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "질문 속 식별자를 실제 코드와 대조 → 유지 / 폐기 / 재질의", options: { fontSize: 15, breakLine: true } }, { text: "실행 1회에서 63개 중 5개 폐기", options: { fontSize: 15, bold: true } }], { x: 7.0, y: 4.25, w: 5.5, h: 2.0 });
  source(s, "B2C 분석 경로 기준 · 각 단계 값은 상한");
}
{
  const s = S("3.3 생성 속도 + 평가 하네스   |   결과물 50", "점수를 믿지 않는 이유를 숫자로 안다",
    "[9:00–9:20] 질문 생성 단계를 93.7초에서 49.1초로 줄였습니다. 품질은 평가 하네스로 잽니다. 그런데 심판 모델만 바꿔도 같은 문항 점수가 17.8점 흔들렸습니다. 그래서 LLM 심판 점수가 아니라 우연 대비 정답률 81.9%를 지표로 씁니다.\n\n출처: collect/C — 속도 = 질문 생성 단계, 사례 3개 × 2회 평균 / 17.8점 = Kimi·DeepSeek 문항별 차 평균 17.82점(n=91), 같은 심판 재채점 차 12.23점(n=24).\nQ&A: v11→v13 QI 하락 → 심판 교체만으로 17.8점이 흔들려 QI를 개선 지표로 안 쓴다.");
  s.addChart(pres.charts.BAR, [{ name: "초", labels: ["개선 전", "개선 후"], values: [93.7, 49.1] }],
    Object.assign(chartBase("질문 생성 단계 소요 시간(초)"), { x: 0.6, y: 1.9, w: 5.6, h: 4.3, barDir: "col", chartColors: ["9A9A9A", "6C5CE7"], varyColors: true, showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.0\"초\"", valAxisMinVal: 0, showLegend: false }));
  T(s, "평가 하네스", { x: 6.6, y: 1.9, w: 6.1, h: 0.45, fontSize: 18, bold: true });
  bullets(s, ["8축 루브릭", "결정적 지표 13개", "회귀 게이트", "운영 파이프라인을 직접 호출해 측정"], { x: 6.6, y: 2.4, w: 6.1, h: 1.9 });
  stat(s, 6.6, 4.45, 6.1, "17.8점", "심판 모델만 바꿔도 흔들리는 문항당 점수 → 그래서 우연 대비 정답률(81.9%)과 결정론 지표(출처 100%)를 쓴다", { h: 1.75 });
  source(s, "속도: 질문 생성 단계, 사례 3개 × 2회 평균 · 17.8점: 심판 2종 문항별 차 평균(n=91)");
}
{
  const s = S("3.4 기출 RAG + 음성 모의면접   |   결과물 50", "실제 기출로 맥락을 보강하고, 말로 답하면 꼬리질문으로 되묻는다",
    "[9:20–9:40] 공개 출처 304개에서 실기업 기출을 모아 pgvector로 검색해 붙입니다(11-02 운영). 음성 모의면접은 16kHz 음성을 Transcribe 스트리밍으로 받아 적고, 꼬리질문을 음성으로 되묻습니다(09-16 운영).\n\n출처: collect/B·08-타임라인. 특허 10-2026-0214811 «음성 대화 기반 면접 답변 평가 방법 및 시스템».\n⛔ «검증된 853건» 금지 · 자체 음성 모델 주장 금지. Q&A: 음성 완료 0건(시작 18) → 완주가 다음 병목.");
  box(s, 0.6, 1.95, 5.9, 4.3, "rag");
  T(s, [{ text: "기출 RAG", options: { bold: true, fontSize: 20, breakLine: true } }, { text: "11-02 운영", options: { fontSize: 13, color: C.text2 } }], { x: 0.8, y: 2.05, w: 5.5, h: 0.8 });
  T(s, "304개", { x: 0.8, y: 2.9, w: 5.5, h: 0.9, fontSize: 48, bold: true });
  T(s, "공개 출처에서 실기업 기출 수집 → pgvector + 어휘 매칭 하이브리드 검색 → 질문에 실제 면접 맥락 연결 (출처 URL 보존)", { x: 0.8, y: 3.85, w: 5.5, h: 1.6, fontSize: 15 });
  box(s, 6.8, 1.95, 5.9, 4.3, "voice");
  T(s, [{ text: "음성 모의면접", options: { bold: true, fontSize: 20, breakLine: true } }, { text: "09-16 운영", options: { fontSize: 13, color: C.text2 } }], { x: 7.0, y: 2.05, w: 5.5, h: 0.8 });
  flow(s, ["16kHz\n음성", "Transcribe\n스트리밍 STT", "꼬리질문\n생성", "TTS로\n되묻기"], 7.0, 3.1, 5.5, 1.3, { fontSize: 12 });
  badge(s, 7.0, 5.0, 4.0, "특허 출원 10-2026-0214811");
}
{
  const s = S("3.5 운영 인프라   |   결과물 50", "배포는 빠르게, 운영 유출은 0으로, 분석 원가는 숫자로",
    "[9:40–10:00] 운영 배포 잡을 429~488초에서 145~260초로 줄였고, 배포 대기는 Step Functions로 옮겼습니다. staging에서 prod로 가는 승격 게이트와 OIDC 배포를 씁니다. 분석 1회 LLM 원가는 약 130원대입니다.\n\n출처: collect/B(배포 잡 시간) · collect/A §5(원가 $0.095 ≈ 133원, 8/30~ 단가 설정 호출 기준, 1 USD=1,400원). 원인 단정 금지(«Step Functions 덕분에 줄었다»로 단정하지 않음).\n⛔ «SBOM 차단» 삭제(main에만 있고 운영 미반영). ⛔ 8월 330원과 비교한 «60% 절감» 금지(정의 다름, gpt-6-luna 단가 미설정분 제외된 하한).");
  stat(s, 0.6, 1.95, 5.9, "429–488초 → 145–260초", "운영 배포 잡 소요 시간 · 배포 대기는 Step Functions로 이관", { h: 1.9, size: 34 });
  stat(s, 6.8, 1.95, 5.9, "약 130원대", "분석 1회 LLM 원가 (10월~, 단가가 설정된 호출 기준)", { h: 1.9 });
  flow(s, ["GitHub Actions\n(OIDC)", "staging", "승격 게이트\n(staging → prod PR 확인)", "prod 배포\n+ Slack 알림"], 0.6, 4.3, 12.1, 1.4, { fontSize: 14 });
  source(s, "배포: GitHub Actions 운영 배포 잡 실측 · 원가: 관리자 콘솔 LLM 호출 원장(2026-08-30~), 1 USD = 1,400원 가정");
}

// ================= 3. 개발 — 수행과정 =================
sec = "3. 개발 — 수행과정"; pres.addSection({ title: sec });
{
  const s = S("3.6 타임라인   |   수행과정 20", "6/29 착수 → 11/4, 피드백을 받은 날짜와 고친 날짜",
    "[10:00–10:40] 6월 29일 착수, 8월 3일 첫 운영 배포, 8월 20일 중간평가에서 피드백 19건을 받았습니다. 그 뒤로 피드백이 들어오면 며칠 안에, 어떤 건 당일에 운영에 반영했습니다.\n\n출처: 08-타임라인.md · collect/B. 사업자등록 푸터 고지 커밋 7050d0a.\n비주얼 의도: 4단계(착수–출시–중간평가–고도화) × 레인 3개 간트로 디자인. 표의 «레인» 열이 그대로 레인 배치.\n⛔ «공동대표» 금지.");
  table(s, ["날짜", "레인", "한 일", "계기 · 걸린 시간"], [
    ["06-29", "엔진·품질", "개발 착수", "06-25 피봇 승인"],
    ["08-03", "제품·인프라", "첫 운영 배포 (B2C 출시)", ""],
    ["8월", "마케팅·사업", "유료 광고 시작 (Meta·Google)", ""],
    [{ text: "08-20", options: { bold: true } }, "—", { text: "★ 중간평가 — 심사위원 피드백 19건", options: { bold: true } }, ""],
    ["08-23", "제품·인프라", "레포 범위 선택", "← 08-07 «GitHub 연동하면 털리나» (16일)"],
    ["~09-03", "마케팅·사업", "사업자등록 (도저랩스)", ""],
    ["09-06", "엔진·품질", "평가 하네스 도입", ""],
    ["09-09", "엔진·품질", "난이도·유형 분리 — 쉬운 질문 추론형 1/8 → 7/9", "← 09-07 한유일 멘토 (2일)"],
    ["09-16", "제품·인프라", "음성 모의면접 운영 반영", ""],
    ["09-22", "제품·인프라", "비동기 배포 · Slack 알림", "← 09-22 멘토링 (당일)"],
    ["10-11", "엔진·품질", "실기업 기출 운영 업로드", ""],
    ["10월 중순", "마케팅·사업", "토스페이먼츠 계약", ""],
    ["11-01", "마케팅·사업", "특허 3건 출원", ""],
    ["11-02", "제품·인프라", "단건 결제 LIVE · 기출 RAG", "← 11-02 멘토링 (당일)"],
  ], { y: 1.85, fontSize: 11, colW: [1.2, 1.7, 5.6, 3.6], rowH: 0.33 });
}
{
  const s = S("3.7 피드백 → 원인 → 수정 → 측정   |   수행과정 20", "피드백을 받으면 원인을 찾고, 고치고, 다시 쟀다",
    "[10:40–11:20] 대표 사례 세 가지입니다. 한유일 멘토가 «쉬운 질문이 코드 사실 확인뿐»이라고 지적했고, 원인은 난이도와 질문 유형이 1:1로 묶여 있던 것이었습니다. 이를 분리하고 2일 만에 운영에 반영했고, 쉬운 질문 9개 중 7개가 추론형이 됐습니다. 중간평가 심사의견 19건 중 18건에 대응했고, 전체 표는 부록 A1에 있습니다.\n\n출처: collect/I-feedback-patterns.md · collect/C (1/8 → 7/9, 단일 레포 1회 — 분모 표기 필수).\n🔴 한유일 멘토 실명 동의 확인. ⛔ «12% → 78%» 금지(분모 표기로). 와이어프레임의 «당일 반영 3건»은 멘토 피드백 기준이라 중간평가 19건과 섞이지 않게 뺌.");
  table(s, ["피드백", "원인", "수정", "측정"], [
    ["한유일 멘토 (09-07)\n«쉬운 질문이 사실 확인뿐»", "난이도와 유형이 1:1로 묶임\n(114문항 중 예외 0)", "난이도를 근거 두께·추론 부담으로 분리\n09-09 운영 반영 (2일)", { text: "쉬운 질문 추론형\n1/8 → 7/9", options: { bold: true } }],
    ["사용자\n«실제 기출이 필요»", "레포·공고 기반 질문만 제공", "공개 출처 304개 기출 → pgvector RAG\n11-02 운영 반영", { text: "기출 연결\n11-02 LIVE", options: { bold: true } }],
    ["멘토링 (09-22)\n«배포를 기다리지 말라»", "운영 배포 대기를 사람이 지켜봄", "배포 대기 Step Functions 이관 + Slack 알림\n당일 반영", { text: "배포 잡\n429–488초 → 145–260초", options: { bold: true } }],
  ], { y: 1.85, fontSize: 12, colW: [3.0, 3.0, 3.6, 2.5], rowH: [0.4, 0.95, 0.95, 0.95] });
  stat(s, 0.6, 5.55, 12.1, "19건 중 18건 대응", "중간평가 심사의견 — 완료 5 · 부분 10 · 소명 3 · 미반영 1 (#15 대학 B2B2C, 사유 기재) → 전체 표 부록 A1", { h: 1.3, size: 30 });
}
{
  const s = S("3.8 실행력   |   수행과정 20", "14주 연속, 매주 운영에 배포했다",
    "[11:20–11:50] 출시 후 14주 동안 한 주도 빠짐없이 운영에 배포했습니다. 총 138회입니다. 배포 실패율은 14.3%에서 1.7%로 떨어졌고, 승격 게이트가 운영 push 13건을 막아 운영 유출은 0건입니다. 자동 테스트는 2,890개, 커밋의 63%가 중간평가 이후입니다.\n\n출처: collect/B · collect/data/dora_prod_deploys_weekly.csv (GitHub Actions prod 배포 성공, 08-03~11-04). 테스트 2,890 = BE 2,000 · FE 807 · E2E 83 (2026-11-05).\n⛔ «500회+» · «1,515» · «리드타임 단축» 금지. Q&A: PR 리뷰 0건 → 사람 승인 대신 CI·승격 게이트(13건 차단), PR 본문 72%에 검증 내역.");
  stat(s, 0.6, 1.9, 3.9, "138회", "운영 배포 · 14주 연속 매주", { h: 1.45 });
  stat(s, 4.7, 1.9, 3.9, "14.3% → 1.7%", "배포 실패율", { h: 1.45, size: 32 });
  stat(s, 8.8, 1.9, 3.9, "2,890개", "자동 테스트 (중간평가 BE 488 → 2,000)", { h: 1.45 });
  const w = ["W32", "W33", "W34", "W35", "W36", "W37", "W38", "W39", "W40", "W41", "W42", "W43", "W44", "W45"];
  const lab = ["8/3", "8/10", "8/17", "8/24", "8/31", "9/7", "9/14", "9/21", "9/28", "10/5", "10/12", "10/19", "10/26", "11/2"];
  s.addChart(pres.charts.BAR, [
    { name: "FE", labels: lab, values: [2, 6, 10, 3, 4, 4, 11, 2, 8, 5, 11, 1, 4, 4] },
    { name: "BE", labels: lab, values: [2, 4, 3, 4, 5, 3, 6, 3, 7, 5, 10, 3, 4, 4] },
  ], Object.assign(chartBase("주별 운영 배포 성공 횟수 (주 시작일, FE+BE)"), { x: 0.6, y: 3.55, w: 7.4, h: 3.25, barDir: "col", barGrouping: "stacked", chartColors: ["6C5CE7", "9A9A9A"], showValue: true, dataLabelPosition: "ctr", dataLabelFontSize: 9, showLegend: true, legendPos: "b", legendFontSize: 10, legendFontFace: "+mn-lt" }));
  bullets(s, ["승격 게이트가 막은 운영 push 13건 · 운영 유출 0", "커밋 1,467개 — 중간평가 이후 919개 (63%)", "운영 승격 PR 29 → 125 (중간평가 전 → 후)", "중간평가 이후 운영 기능 50여 개 · 10개 영역"], { x: 8.3, y: 3.6, w: 4.4, h: 3.2, fontSize: 15 });
  source(s, "GitHub Actions prod 배포(08-03~11-04) · 커밋: BE+FE 원격 기준 · 테스트: 2026-11-05 저장소 기준");
}
{
  const s = S("3.9 현장 검증   |   수행과정 20", "현업이 본 DevFit",
    "[11:50–12:10] 현업 개발자이신 한유일 멘토는 중간·어려움 질문을 «충분히 괜찮다»고 평가했습니다. IT 기업 대표는 «왜 그 기술을 선택했는지, 그 선택이 최선이었는지를 묻는다»고 답했는데, 이게 우리 «결정 이유» 질문 유형입니다. 같은 분의 반론 «Claude Code에 넘기면 된다»는 앞의 실험으로 답했습니다.\n\n출처: collect/D V1(09-07 녹취) · 대표 서면 회신 원문(10-26, 캡처는 이름·회사·메일 주소를 잘라냄).\n김종욱 멘토(10-25): 발언 기록 0건 → 기록 확보 시에만 추가, 지어내지 않음.\n🔴 실명 동의: 한유일 멘토 · 기업 대표.");
  quote(s, 0.6, 1.9, 5.9, 1.55, "«중간이나 어려움 수준에서 지금 나오는 질문들은 충분히 괜찮아 보이긴 한 것 같아요.»", "한유일 멘토 (09-07 실사용 검증)");
  quote(s, 6.8, 1.9, 5.9, 1.55, "«왜 선택했는지나 왜 그 상황에서 그 선택이 최선이였는지 많이 물어봅니다.»", "IT 기업 대표 (10-26 서면 회신)");
  T(s, "= DevFit «결정 이유»·«트레이드오프» 질문 유형", { x: 6.8, y: 3.5, w: 5.9, h: 0.4, fontSize: 14, bold: true });
  s.addImage({ path: IMG("ceo_mail_body.png"), x: 0.6, y: 4.05, w: 8.8, h: 8.8 * 582 / 2117, altText: "IT 기업 대표 서면 회신 본문 (이름·회사·메일 주소 제외)" });
  T(s, "같은 대표의 반론 «github 링크를 클로드코드에게 넘기면 된다» → p4 실험으로 답함 (근거 실존 0/18 vs 28/28)", { x: 0.6, y: 6.6, w: 12.1, h: 0.4, fontSize: 13, color: C.text2 });
}
{
  const s = S("3.10 우리가 찾은 약점과 다음 조치   |   수행과정 20", "약점을 숫자로 찾고, 다음 조치를 정했다",
    "[12:10–12:30] 가장 큰 이탈은 방문에서 가입입니다. 원인을 좁혀 보니 Instagram 인앱 브라우저로 들어온 사람의 가입 전환이 다른 유입의 약 10분의 1이었습니다. 다음 조치는 인앱을 감지해 외부 브라우저로 넘기는 것이고, 아직 구현 전입니다.\n\n출처: collect/D §1·§4. 방문 = Clarity(봇 제외), 가입 = 관리자 DB → 도구가 달라 0.4%는 «대략»으로만. 월 비교는 자연 실험(통제 실험 아님), 8월은 팀·멘토 가입 포함, 11월은 표본 작음.\n기대 효과는 가설: IG 전환 0.10~0.15% → 0.25~0.40%, 9~10월 세션에 적용 시 가입 +21~+60명(추정).");
  stat(s, 0.6, 1.9, 3.9, "약 0.4%", "방문 2.2만 명 → 가입 — 가장 큰 이탈", { h: 1.6 });
  stat(s, 4.7, 1.9, 3.9, "약 10배", "Instagram 인앱 유입 가입 전환 0.10~0.15% vs 그 외 1.2~1.5%", { h: 1.6 });
  box(s, 8.8, 1.9, 3.9, 1.6, "next action");
  T(s, [{ text: "다음 조치 (미구현)", options: { bold: true, fontSize: 16, breakLine: true } }, { text: "인앱 브라우저 감지 → 외부 브라우저로 전환 · 기대 효과는 가설", options: { fontSize: 13 } }], { x: 8.95, y: 2.0, w: 3.6, h: 1.4 });
  s.addChart(pres.charts.BAR, [{ name: "세션 1,000개당 가입", labels: ["8월 (인앱 12%)", "9월 (인앱 91%)", "10월 (인앱 86%)", "11/1–4 (광고 중단)"], values: [15.0, 3.6, 2.2, 12.3] }],
    Object.assign(chartBase("월별 세션 1,000개당 가입 수 (괄호: Instagram 인앱 비중)"), { x: 0.6, y: 3.75, w: 7.6, h: 3.05, barDir: "col", chartColors: ["6C5CE7"], showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.0", valAxisMinVal: 0, showLegend: false }));
  bullets(s, ["세션당 활성 시간: 8월 2.3분 → 9월 12초", "인앱 웹뷰에는 GitHub 로그인 세션이 없음 (가설)", "검증: Clarity 인앱 필터 → 2주 A/B"], { x: 8.5, y: 3.85, w: 4.2, h: 2.9, fontSize: 14 });
  source(s, "Clarity(2026-08-01~11-04, 봇 제외) · 관리자 DB 가입 · 월 비교는 통제 실험이 아님");
}

// ================= 4. Effect =================
sec = "4. Effect"; pres.addSection({ title: sec });
{
  const s = S("4.1 B2C 운영지표 — 지금까지   |   기대효과 30", "가입한 사람의 76%가 실제 공고로 준비를 시작했다",
    "[12:30–13:10] 외부 가입자 79명 중 60명, 76%가 실제 지원할 공고를 넣고 준비를 시작했습니다. 가입하지 않고 공고를 넣어 본 사람까지 합치면 최대 126명입니다. 8월 7일 7명에서 11월 4일 83명이 됐고, 가입의 30%가 밤 9시부터 새벽 1시 사이입니다.\n\n출처: collect/A·04-DB지표 (관리자 DB, 2026-11-05 00:38 조회, 내부 계정 user id 1·5·7·11 제외). 누적 83명은 내부 4명 포함.\n🔄 제출 직전(11/11) 재조회 후 갱신.\n⛔ «400명대»·«393명»(비로그인 세션) · 내부 포함 64명/77.1% 금지. Q&A: 외부 답변 9명·33건 → 답변 전환이 다음 목표.");
  stat(s, 0.6, 1.9, 4.6, "60 / 79명 (76%)", "외부 가입자 중 실제 공고로 준비 시작 (외부 공고 83건, 내부 4명 제외)", { h: 1.65, size: 32 });
  stat(s, 0.6, 3.7, 4.6, "최대 126명", "공고를 직접 등록해 본 사람 (회원 64 + 비회원 62)", { h: 1.5 });
  stat(s, 0.6, 5.35, 4.6, "30%", "가입이 밤 9시 ~ 새벽 1시 (21~01시 25명 / 83명)", { h: 1.45 });
  const lab = ["8/7", "8/16", "8/23", "8/30", "9/6", "9/13", "9/20", "9/27", "10/4", "10/11", "10/18", "10/25", "11/1", "11/4"];
  s.addChart(pres.charts.LINE, [{ name: "누적 회원", labels: lab, values: [7, 9, 11, 15, 23, 28, 35, 40, 58, 63, 70, 71, 82, 83] }],
    Object.assign(chartBase("누적 회원 8/7 7명 → 11/4 83명 (관리자 DB, 내부 4명 포함)"), { x: 5.5, y: 1.9, w: 7.2, h: 4.9, chartColors: ["6C5CE7"], lineSize: 3, lineDataSymbol: "circle", lineDataSymbolSize: 6, showValue: true, dataLabelPosition: "t", dataLabelFontSize: 9, valAxisMinVal: 0, showLegend: false }));
  source(s, "관리자 DB · 성장 차트 판독값 ±1명 · 조회 2026-11-04~05");
}
{
  const s = S("4.2 어드민   |   기대효과 30", "지표를 추측하지 않으려고 관리자 콘솔을 만들었다",
    "[13:10–13:30] 앞 장의 숫자는 모두 우리가 직접 만든 관리자 콘솔에서 나왔습니다. 내부 계정을 빼고 회원을 세고, LLM 호출 하나하나의 원가를 기록하고, 공고 캐시를 운영합니다.\n\n이미지: 관리자 콘솔 메뉴(회원 이메일 영역 잘라냄) · LLM 사용량 카드(90일, 2026-11-05 00:43).\n디자인 시 캡처를 더 넣을 경우: metrics/screenshots/admin_b2c_*·admin_behavior_*·admin_llm_usage_* — 🔴 이메일·브라우저 북마크·«393» 비로그인 세션 카드 가림.\n⛔ «공고 1,450건 사전 수집»은 직업정보 DB로 읽힐 수 있어 본편 제외.");
  s.addImage({ path: IMG("admin_menu.png"), x: 0.6, y: 1.9, w: 1.65, h: 1.65 * 1217 / 408, altText: "관리자 콘솔 메뉴" });
  s.addImage({ path: IMG("admin_llm_usage_90d_20261105-0043.png"), x: 2.6, y: 1.9, w: 10.1, h: 10.1 * 313 / 1254, altText: "관리자 콘솔 LLM 사용량 (90일)" });
  table(s, ["기능", "하는 일"], [
    ["B2C 대시보드 · 회원 관리", "가입·공고 등록·분석·답변 퍼널, 내부 계정 제외 집계"],
    ["사용자 행동 분석", "텍스트·음성 모의면접 사용 흐름"],
    ["LLM 사용량 · 모델 단가", "호출별 토큰·원가 원장 (90일 호출 5,391건, 성공률 99.3%)"],
    ["캐싱 공고 · 면접 기출문제", "기업 채용사이트 공고 캐시와 기출 데이터 운영"],
    ["Sentry 운영 오류 · 오류 관리", "운영 장애 추적"],
  ], { x: 2.6, y: 4.6, w: 10.1, fontSize: 13, colW: [3.4, 6.7] });
}
{
  const s = S("4.3 그 외 — 서비스를 할 수 있는 상태   |   기대효과 30", "돈을 받고 서비스를 할 수 있는 상태를 갖췄다",
    "[13:30–13:50] 사업자등록을 마쳤고, 토스페이먼츠 단건 결제가 11월 2일부터 LIVE입니다. 특허 3건을 출원했습니다. 추가생성권은 1,900원, 분석 1회 원가는 약 130원대라 팔수록 밑지지 않습니다.\n\n🔴 직업정보제공사업 신고 배지: 11-06 서류 수령 예정(박천웅) → 받으면 신고번호·신고일 기입, 못 받으면 배지 삭제 (증빙 없으면 허위 실적).\n⛔ 정기결제(Plus)는 심사 중 — «계약 완료»로 묶지 않음. ⛔ «매출» · «공동대표» · 특허 «등록»·«회사 특허» 금지 (출원인 김건우 개인, 발명자 3명, 심사청구 무).\nQ&A: 결제 0건 → «LIVE»까지만 말함.");
  badge(s, 0.6, 2.0, 3.9, "사업자등록 · 도저랩스 (대표 박천웅)");
  badge(s, 4.7, 2.0, 3.9, "토스페이먼츠 단건 결제 LIVE (11-02)");
  badge(s, 8.8, 2.0, 3.9, "특허 3건 출원 (11-01)");
  todo(s, "직업정보제공사업 신고 — 증빙 수령 시 신고번호·신고일 기입, 없으면 이 배지 삭제", 0.6, 2.75, 12.1, 0.5);
  T(s, "단위 경제성", { x: 0.6, y: 3.55, w: 12.1, h: 0.45, fontSize: 18, bold: true });
  stat(s, 0.6, 4.05, 5.9, "1,900원", "추가생성권 (공고 단위 단건 결제)", { h: 1.6 });
  stat(s, 6.8, 4.05, 5.9, "약 130원대", "분석 1회 LLM 원가 (10월~, 단가 설정 호출 기준)", { h: 1.6 });
  table(s, ["특허 출원번호", "발명의 명칭"], [["10-2026-0214808", "코드 저장소 기반 면접 질문 선별 방법 및 시스템"], ["10-2026-0214809", "코드 저장소 기반 면접 질문 생성 방법 및 시스템"], ["10-2026-0214811", "음성 대화 기반 면접 답변 평가 방법 및 시스템"]], { y: 5.85, fontSize: 11, colW: [2.6, 9.5], rowH: 0.3 });
}
{
  const s = S("4.4 비전 & B2B — 시장   |   기대효과 30", "공고는 10만 건, 지원은 260만 건 — 검증 수단이 모자란 시장",
    "[13:50–14:20] 국내 개발자 채용공고는 반년에 약 10만 건, 지원은 약 260만 건입니다. B2C는 공고마다 준비하는 개발 취준생 약 2~4만 명이 대상이고, B2B는 면접관이 빠뜨린 확인 관점을 알려 주는 커버리지 어시스턴트로 갑니다. 국내 상향식으로 B2B 유효시장 약 104억 원, 3년 목표 약 3억 원대입니다.\n\n출처: 사람인·점핏 2025 상반기 리포트(언론 보도 경유) · 국가데이터처 청년층 부가조사 2026-05 · 계산식 collect/H-market.md. B2B 재정의는 중간평가 #17(질문 유출 우려) 대응 + 11-02 멘토 제안.\n⛔ 5년 SOM 27억 · TAM $2.8B 제거(재현 불가). 글로벌 리포트는 $0.34B~$3.15B 범위로만, 부록.");
  stat(s, 0.6, 1.9, 5.9, "약 10만 건", "국내 개발자 채용공고 (2025 상반기)", { h: 1.5 });
  stat(s, 6.8, 1.9, 5.9, "약 260만 건", "같은 기간 지원 수 — 신입 비중 공고 0.8% vs 지원 29.5%", { h: 1.5 });
  box(s, 0.6, 3.65, 5.9, 2.0, "B2C");
  T(s, [{ text: "B2C", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "공고마다 준비하는 개발 취준생 약 2~4만 명 (내부 추정)", options: { fontSize: 15, breakLine: true } }, { text: "일반기업 취업 준비 청년 약 20만 명 중", options: { fontSize: 13, color: C.text2 } }], { x: 0.8, y: 3.75, w: 5.5, h: 1.8 });
  box(s, 6.8, 3.65, 5.9, 2.0, "B2B");
  T(s, [{ text: "B2B", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "면접관이 빠뜨린 확인 관점을 알려 주는 커버리지 어시스턴트 (콘솔 구현 완료)", options: { fontSize: 15 } }], { x: 7.0, y: 3.75, w: 5.5, h: 1.8 });
  table(s, ["국내 상향식 (내부 가격 앵커 기준)", "규모"], [["B2B 유효시장 (SAM)", "약 104억 원"], ["3년 목표시장 (SOM)", "약 3억 원대"]], { y: 5.85, fontSize: 13, colW: [8.1, 4.0] });
  source(s, "사람인·점핏 2025 상반기 리포트 · 국가데이터처 청년층 부가조사(2026-05) · 계산식: 팀 내부 시장 추정 문서", 6.95);
}
{
  const s = S("4.4 비전 & B2B — 앞으로의 효과   |   기대효과 30", "DevFit Platform — 하나의 개발자 채용 플랫폼으로",
    "[14:20–14:50] 중간발표에서 말한 비전입니다. 지원자 준비, 근거 기반 검증, 공고와 지원 흐름을 하나의 개발자 채용 플랫폼으로 잇는 것이고, 그 조각 세 개가 이미 운영 중입니다. 앞으로 6개월 B2C 가입 275명, 가입자 답변률 25%가 목표이고, B2B는 11월 회고형 파일럿 2곳에서 시작해 3월 첫 유료 1곳까지 갑니다.\n\n출처: 비전 그림 = Devfit/brand/platform/vision-diagram.png(중간발표 p05와 같은 그림) · 275명 = 최근 주 7.4명 × 26주 + 83명, 범위 135~382, 현 수준 광고비 전제 · B2B 로드맵 collect/J.\n11/10 18시까지 의향서가 오면 «파일럿 의향서 1건(비구속)»으로 교체.\n⛔ «고객 확보»·«파일럿 진행 중»·«MOU» 금지 (현재 LOI·MOU·계약 0).");
  s.addImage({ path: IMG("vision-diagram.png"), x: 0.6, y: 1.85, w: 6.4, h: 6.4 * 1824 / 3360, altText: "DevFit Platform 비전 다이어그램" });
  T(s, "이미 운영 중인 조각", { x: 0.6, y: 5.45, w: 6.4, h: 0.4, fontSize: 15, bold: true });
  bullets(s, ["① B2C 공고 맞춤 준비 · 결제 LIVE", "② B2B 면접관 콘솔", "③ 공고 29곳 수집 · 지원 여정 트래커"], { x: 0.6, y: 5.85, w: 6.4, h: 1.0, fontSize: 13 });
  stat(s, 7.3, 1.85, 2.6, "275명", "B2C 6개월 가입 목표 (추정, 범위 135~382)", { h: 1.75, size: 32 });
  stat(s, 10.1, 1.85, 2.6, "25%", "가입자 답변률 목표", { h: 1.75, size: 32 });
  T(s, "B2B 로드맵 (현재: 콘솔 완성, 고객 0)", { x: 7.3, y: 3.85, w: 5.4, h: 0.4, fontSize: 15, bold: true });
  table(s, ["시점", "단계"], [["2026-11", "회고형 파일럿 2곳"], ["2027-01~02", "실전 파일럿 2~3곳"], ["2027-03", "첫 유료 1곳"]], { x: 7.3, y: 4.3, w: 5.4, fontSize: 13, colW: [1.9, 3.5] });
  T(s, "재는 것: 면접관 질문 채택률", { x: 7.3, y: 5.75, w: 5.4, h: 0.4, fontSize: 14 });
  source(s, "275명 = 최근 주 7.4명 × 26주 + 현재 83명 (현 수준 광고비 전제)");
}

// ================= 마무리 =================
sec = "5. 마무리"; pres.addSection({ title: sec });
{
  const s = pres.addSlide({ masterName: "COVER", sectionTitle: sec });
  s.addText("AI가 만든 면접 질문을, 지원자 본인의 코드로 증명하고 숫자로 검증합니다.", { isTextBox: true, x: 0.8, y: 1.4, w: 11.7, h: 2.2, fontSize: 36, bold: true, color: C.text1, margin: 0, valign: "bottom" });
  s.addText([{ text: "B2C https://devfit.app · B2B https://enterprise.devfit.app", options: { breakLine: true } }, { text: "Team Dozer · 박천웅 · 김건우 · 노재원", options: {} }], { isTextBox: true, x: 0.8, y: 3.9, w: 11.7, h: 1.1, fontSize: 20, color: C.text2, margin: 0, valign: "top" });
  todo(s, "테스트 계정 ID / PW", 0.8, 5.3, 5.0, 0.5);
  s.addText([{ text: ACK, options: { breakLine: true } }, { text: ACK_EN }], { isTextBox: true, x: 0.8, y: 6.3, w: 11.7, h: 0.8, fontSize: 10, color: "777777", margin: 0, valign: "bottom" });
  s.addNotes("[14:50–15:00] DevFit은 AI가 만든 면접 질문을, 지원자 본인의 코드로 증명하고 숫자로 검증합니다. 감사합니다.\n\n테스트 계정은 GitHub OAuth 전용이라 심사위원용 계정 필요 — 제출 전 시크릿 창에서 로그인 재확인.");
}

// ================= 부록 =================
sec = "부록 (Q&A)"; pres.addSection({ title: sec });
{
  const s = S("부록", "부록 (Q&A)", "Q&A 때 쪽번호로 이동. 답변 원고: collect/00-통합보고.md §3.");
  table(s, ["쪽", "장표", "예상 질문"], [
    ["A1", "중간평가 심사의견 19건 반영표", "멘토·심사 의견을 어떻게 반영했나"],
    ["A2", "범용 AI 비교 실험 · 유사 서비스 비교", "범용 AI랑 뭐가 다른가"],
    ["A3", "평가 하네스 상세", "품질을 어떻게 믿나"],
    ["A4", "측정 도구별 수치 차이", "GA는 235명인데 왜 2.2만인가"],
    ["A5", "유료 광고 집행과 효율", "마케팅 효율은"],
    ["A6", "보안", "내 코드 털리는 거 아닌가"],
    ["A7", "원가와 가격", "돈은 어떻게 버나"],
    ["A8", "기출 데이터 수집", "크롤링 문제없나"],
    ["A9", "특허 3건", "특허는 뭘 보호하나"],
    ["A10", "팀 역할 · 품질 보증", "누가 뭘 했나 · 리뷰는"],
  ], { y: 1.9, fontSize: 13, colW: [0.9, 5.4, 5.8], rowH: 0.42 });
}
{
  const s = S("A1", "중간평가 심사의견 19건 — 완료 5 · 부분 10 · 소명 3 · 미반영 1",
    "출처: collect/I-feedback-patterns.md (반영일·근거 커밋은 운영 브랜치 포함 여부 확인). 최종보고서 «중간점검 반영표»와 같은 내용.\n멘토 피드백 31행 표는 collect/I 원본 참조 — 필요 시 A1-2로 추가.");
  const R = [
    ["1", "늦은 피봇을 범위 축소로 만회(긍정)", "유지", "B2C 주축, B2B는 MVP. 운영 승격 PR 29 → 125"],
    ["2", "기능 확장보다 질문 품질과 기업 파일럿", "부분", "8축 평가 → 결함 31건 수정 → 난이도 분리 → v11~v13. 저난도 추론형 1/8 → 7/9. 파일럿 0건"],
    ["3", "커밋·diff 연결과 무근거 폐기(긍정)", "강화", "근거 대조·사유 코드 노출(10-19). 출처 353/353, 품질 필터 30일 84건"],
    ["4", "라벨·문항분석으로 정확성·변별도 검증", "부분", "3-state 라벨 UI 복구(09-08). 근거 특정성 81.9%. 변별도 실측 0건(표본 부족)"],
    ["5", "질문 품질 자동 검증", "완료", "평가 하네스(09-06): 8축 루브릭·결정적 지표 13개·회귀 게이트"],
    ["6", "설계·본인 작업 검증 등 의도별 질문", "완료", "의도 7유형, 난이도 분리, 본인 기여 필터(1.0/0.70/제외). 09-09 운영"],
    ["7", "코딩 외 전인적 역량 평가", "부분·소명", "자동 합불 금지선 → «준비» 지원: 음성 모의면접, 자소서·포트폴리오 작업실, 블라인드 평가"],
    ["8", "기업 파일럿으로 채택률·절감 확인", "부분·착수", "기업 대표 서면 회신 1건, 리드 43사, 로드맵. 수치·LOI 없음"],
    ["9", "시장 분석 세밀화, 포커스 결정", "부분", "출처 등급제(인용 금지 6건 제거), B2C 신입·주니어 포커스"],
    ["10", "기존 취업 사이트 대비 우위", "부분", "«공고 × 내 실제 코드». 근거 실존 28/28 vs 0/18"],
    ["11", "경쟁사 직접 사용", "부분", "직접 9·인접 43·모바일 12종 캡처. 유료 전체 플로우 기록 없음"],
    ["12", "B2C·B2B 동시 공략은 욕심", "소명", "투입은 B2C 집중, B2B는 같은 엔진 MVP"],
    ["13", "일정상 B2C 집중", "완료", "B2C 출시 → 음성 → 단건 결제 LIVE(11-02)"],
    ["14", "중견기업 타겟", "부분", "리드 규모 32~618명. 발송 전 미검증"],
    ["15", "대학 취업지원실 B2B2C", "미반영", "박람회 현장 마케팅만. 대학 예산 주기와 연수 종료 시점 불일치"],
    ["16", "시즌성 때문에 수익모델 재검토", "부분", "공고 단위 단건 1,900원 추가·LIVE. 매출 0"],
    ["17", "질문 유출 플랫폼은 기업이 싫어함", "소명", "본인 코드 기반·지원서별 생성. B2B «커버리지 어시스턴트» 재정의"],
    ["18", "개인정보 보호조치", "부분", "토큰 AES-256-GCM, 세션 해시, numeric id 신원, 증분 동의, 블라인드 평가"],
    ["19", "개발·운영 환경 통합(비용)", "소명", "결제 TEST 격리 필요로 분리 유지. 원가의 94%가 LLM"],
  ];
  table(s, ["#", "심사의견", "구분", "조치"], R, { y: 1.75, fontSize: 10, colW: [0.45, 3.6, 1.15, 6.9], rowH: 0.26, margin: 0.03 });
}
{
  const s = S("A2", "범용 AI 비교 실험 (파일럿) — 차이는 절차에서 난다",
    "출처: collect/E-compare.md (2026-11-05, 레포 4개, 군별 1회, 결정론 채점 LLM 0회). 파일럿이므로 승률로 말하지 말고 비율과 n을 같이.\nB1 실패 2건은 API 키를 일부러 가린 인용(지어낸 인용 0). 구체성 proxy(레포 고유 앵커)는 Claude Code 30/32 > DevFit 16/28 — «DevFit이 더 정확하다»는 말하지 않음.\n블라인드 사람 채점 78문항 진행 중 — 결과 나오면 이 장에 추가.");
  table(s, ["군", "n", "SHA 실존", "파일 실존", "근거 3종 모두 실존", "본인 커밋"], [
    ["DevFit (운영 prod)", "28", "28 (100%)", "28 (100%)", "28 (100%)", "28 (100%)"],
    ["Claude Code + 레포 clone", "32", "32 (100%)", "32 (100%)", "30 (94%)", "32 (100%)"],
    ["범용 AI, 레포 링크만", "18", "0 (0%)", "0 (0%)", "0 (0%)", "0 (0%)"],
  ], { y: 1.85, fontSize: 13, colW: [3.4, 0.8, 1.9, 1.9, 2.3, 1.8] });
  T(s, "레포를 읽게 하면 범용 에이전트도 근거를 찾는다. DevFit은 그 읽기·대조 절차를 사용자가 프롬프트를 짜지 않아도 서버가 매번 강제하고, 공고 단위 흐름과 본인 커밋 필터를 붙였다.", { x: 0.6, y: 3.45, w: 12.1, h: 0.75, fontSize: 14 });
  table(s, ["서비스", "입력", "본인 코드·커밋 분석", "질문 근거 표시", "특정 공고 맞춤", "음성", "한국어"], [
    ["DevFit", "공고 URL/이미지 + GitHub", "본인 커밋·PR만", "질문마다 diff + 원문 링크", "플랫폼 5 + 기업 24곳", "O", "O"],
    ["Greenroom(해외)", "GitHub 레포·목표 직무", "O (Pro)", "확인 안 됨", "확인 안 됨", "O", "확인 안 됨"],
    ["Final Round AI(해외)", "이력서 + JD", "X", "–", "O", "O", "명시 없음"],
    ["사람인 AI 모의면접", "이력서 + 사람인 공고", "X", "–", "사람인 공고 한정", "O", "O"],
    ["꼬꼬면", "이력서·포트폴리오", "언급 없음", "문항 은행 기반", "–", "O", "O"],
    ["범용 AI", "사용자 지시", "연동 시 열람 가능", "사용자가 검증", "사용자가 지시", "일부", "O"],
  ], { y: 4.35, fontSize: 10, colW: [1.9, 2.1, 1.7, 2.0, 1.9, 0.9, 1.6], rowH: 0.3 });
  source(s, "기능 비교: 각 서비스 공개 페이지 기준(2026-11-05 확인) · 실험: 공개 레포 4개 · 같은 공고 · 같은 지시");
}
{
  const s = S("A3", "평가 하네스 — LLM 심판 점수를 그대로 믿지 않는다",
    "출처: collect/C-quality.md. 17.82점(n=91) = Kimi·DeepSeek 문항별 차 평균, 12.23점(n=24) = 같은 심판 재채점 차, «LLM 심판이 사람보다 약 1점 후함»(n=18).\n🔄 블라인드 사람 채점(78문항, 평가자 3명) 결과가 나오면 «사람 기준선» 칸 갱신.");
  bullets(s, ["운영 파이프라인을 직접 호출해 질문 생성", "8축 루브릭 (LLM 심판)", "결정적 지표 13개 — 출처 연결, 공고별 중복, 식별자 실존 등", "회귀 게이트 — 질문 로직 버전(v1 → v13)마다 측정"], { x: 0.6, y: 1.9, w: 6.0, h: 3.0 });
  table(s, ["측정", "값", "n"], [
    ["심판 2종 간 문항별 점수 차", "17.8점", "91"],
    ["같은 심판 재채점 차", "12.2점", "24"],
    ["LLM 심판 vs 사람", "사람보다 약 1점 후함", "18"],
    ["근거 특정성 (우연 25%)", "81.9%", "177"],
    ["질문 출처 연결", "353/353", "전수"],
  ], { x: 6.9, y: 1.9, w: 5.8, fontSize: 13, colW: [3.0, 2.0, 0.8] });
  todo(s, "블라인드 사람 채점 결과 (78문항 · 평가자 3명) — 결과 수령 후 기입", 0.6, 5.3, 12.1, 0.5);
  T(s, "결론: 절대 점수 대신 우연 대비 정답률과 결정론 구조 지표를 개선 지표로 쓴다", { x: 0.6, y: 6.0, w: 12.1, h: 0.5, fontSize: 15, bold: true });
}
{
  const s = S("A4", "측정 도구마다 숫자가 다른 이유",
    "출처: metrics/charts/14_measurement_gap.png · collect/D §1. GA4는 쿠키 동의 게이트 때문에 하한(가입 이벤트가 실제 가입의 약 절반만 잡힘). 정본 우선순위: 관리자 DB > Clarity > 광고 관리자 > GA4.");
  s.addImage({ path: IMG("14_measurement_gap.png"), x: 0.6, y: 1.85, w: 7.6, h: 7.6 * 1080 / 1920, altText: "측정 도구별 수치 차이 차트" });
  table(s, ["도구", "값", "기준"], [
    ["Microsoft Clarity", "방문자 22,360명", "동의와 무관하게 수집, 봇 제외 (8/1~11/4)"],
    ["Google Analytics 4", "사용자 235명", "쿠키 동의한 사람만 → 하한"],
    ["관리자 DB", "가입 83명", "정본 (내부 4명 포함)"],
  ], { x: 8.5, y: 1.85, w: 4.2, fontSize: 11, colW: [1.3, 1.2, 1.7] });
  T(s, "회원·공고·분석 수치는 관리자 DB만 정본으로 쓴다", { x: 8.5, y: 4.7, w: 4.2, h: 0.8, fontSize: 14, bold: true });
}
{
  const s = S("A5", "유료 광고 ₩347.5만 — 랜딩은 싸고 가입은 비쌌다",
    "출처: collect/D §2. ₩4.2만은 하한(가입 전원이 광고로 들어왔다고 가정) — «상한»이라 쓰지 말 것. 상한 추정 ₩12.9만. Meta·Google의 «전환»과 DB «가입»은 정의가 다름.");
  stat(s, 0.6, 1.9, 3.9, "₩347.5만", "유료 광고 합계 (Meta ₩233.8만 + Google ₩113.7만)", { h: 1.6 });
  stat(s, 4.7, 1.9, 3.9, "최소 ₩4.2만", "가입 1명당 광고비 (하한)", { h: 1.6 });
  stat(s, 8.8, 1.9, 3.9, "브랜드 검색뿐", "자연 검색 유입 (Search Console 클릭 37건, 대부분 «devfit»)", { h: 1.6, size: 28 });
  table(s, ["지표", "Meta", "Google"], [
    ["지출", "₩2,338,208", "₩1,136,972"],
    ["노출", "666,197", "116,041"],
    ["클릭", "21,318 (링크 클릭)", "2,018"],
    ["클릭 1회", "₩110", "₩563"],
    ["랜딩 1회", "₩151 (Meta 랜딩 조회)", "—"],
  ], { y: 3.75, fontSize: 13, colW: [3.0, 4.6, 4.5] });
  source(s, "Meta 광고 관리자(8/1~11/3) · Google Ads(8/24~11/3) · 관리자 DB 가입 83명");
}
{
  const s = S("A6", "보안 — 최소 권한으로 연결하고, 토큰은 암호화한다",
    "근거 코드: auth/GithubTokenCipher(AES-256-GCM) · user_session(SHA-256 해시) · V38 github_user_id · prep/corporate/SafeFetcher. 레포 범위 선택은 08-07 피드백 후 16일 만(08-23) 반영.");
  table(s, ["우려", "조치"], [
    ["«GitHub 연동하면 내 코드 털리나»", "기본 로그인 권한은 read:user · user:email만. 비공개 레포는 사용자가 원할 때만 증분 동의"],
    ["분석 범위", "분석할 레포를 사용자가 직접 선택 (공개/비공개 범위 선택)"],
    ["토큰 유출", "GitHub access token AES-256-GCM 암호화 저장"],
    ["세션 탈취", "세션 토큰 원문 대신 SHA-256 해시만 저장 → 즉시 폐기 가능, HttpOnly 쿠키"],
    ["계정 선점", "GitHub 신원 기준 키를 불변 numeric id로 (username 선점 차단)"],
    ["공고 수집 경로 악용 (SSRF)", "홉마다 허용 목록을 다시 검사하는 SafeFetcher, 응답 8MB 상한"],
    ["B2B 지원자 정보", "블라인드 평가, 지원 시 동의 2건 필수"],
  ], { y: 1.9, fontSize: 13, colW: [3.8, 8.3], rowH: 0.55 });
}
{
  const s = S("A7", "원가와 가격 — 분석 1회 약 130원대, 단건 1,900원",
    "출처: collect/A §5. 133원 = $0.095 × 1,400원, 8/30~ 단가 설정 호출만. gpt-6-luna 2,349회(단가 미설정)를 glm-5 단가로 넣으면 분석당 약 150원(추정). 8월 330원과 «60% 절감» 비교 금지.\n원가의 94%가 LLM(인프라는 개발 DB·서버 정지 운영). Plus 정기결제는 심사 중.");
  stat(s, 0.6, 1.9, 5.9, "약 130원대", "분석 1회 LLM 원가 (≈ $0.095, 단가 설정 호출 기준 · 미설정 호출 포함 추정 약 150원)", { h: 1.8 });
  stat(s, 6.8, 1.9, 5.9, "94%", "전체 원가 중 LLM 비중", { h: 1.8 });
  table(s, ["상품", "가격", "상태"], [
    ["Free", "무료 (사용 한도 있음)", "운영 중"],
    ["추가생성권 (공고 단위 단건)", "1,900원", "토스페이먼츠 LIVE (2026-11-02)"],
    ["Plus", "월 7,900원", "정기결제 심사 중, 출시 기념 3개월 무료 개방"],
    ["B2B", "파일럿 후 결정", "콘솔 구현 완료, 고객 0"],
  ], { y: 4.0, fontSize: 13, colW: [3.6, 3.2, 5.3] });
  T(s, "채용 시즌에만 사는 구조를 위해 월 구독 외에 공고 단위 단건 상품을 추가 (중간평가 #16 대응)", { x: 0.6, y: 6.2, w: 12.1, h: 0.5, fontSize: 14 });
}
{
  const s = S("A8", "기출 데이터 — 공개 출처만, 출처 URL을 같이 보존한다",
    "근거: 기출 RAG 11-02 운영(공개 출처 304개). 11-02 전략멘토링 대응 기록: «저작권·직업정보제공사업 문제로 공개 정보 위주로 간다».\n⛔ «검증된 853건» 금지(승인 0건). 법적 검토 의견은 확보된 것이 없음 → 【】 칸은 확보 시에만 채우고, 없으면 삭제.");
  bullets(s, ["수집 대상: 공개된 면접 후기·기출 출처 304개", "출처 URL을 질문과 함께 보존해 원문을 확인할 수 있게 함", "공개 정보 위주 수집 — 비공개·로그인 필요 자료는 수집하지 않음", "질문은 원문을 그대로 노출하지 않고 지원자 코드 질문의 맥락 보강에 사용"], { x: 0.6, y: 1.9, w: 12.1, h: 3.0 });
  todo(s, "저작권·이용약관 검토 결과 (검토 주체·일자) — 확보 시에만 기입, 없으면 이 칸 삭제", 0.6, 5.2, 12.1, 0.5);
}
{
  const s = S("A9", "특허 3건 출원 (2026-11-01)",
    "출원인 김건우(개인), 발명자 김건우·박천웅·노재원. 심사청구 무 · 공개신청 무(통지서 기준). ⛔ «등록»·«회사 특허» 금지.\n통지서 원본 캡처에는 출원인 코드가 있어 덱에 넣지 않음 — 필요하면 출원번호·명칭만 표기.\n청구항 요지 원문: Devfit/docs/patent/ 명세서 (⛔ 삭제 금지, 공지예외 12개월 시한 진행 중).");
  table(s, ["출원번호", "발명의 명칭", "보호하는 것 (요지)", "관련 장표"], [
    ["10-2026-0214808", "코드 저장소 기반 면접 질문 선별 방법 및 시스템", "본인 기여 커밋을 골라 가중(본인 1.0 · 공동 0.70 · 타인 제외)하고 질문 대상 지점을 선별", "p7"],
    ["10-2026-0214809", "코드 저장소 기반 면접 질문 생성 방법 및 시스템", "근거 코드 묶음에서 질문을 만들고, 질문 속 식별자를 코드와 대조해 유지·폐기·재질의하는 게이트", "p6 · p11"],
    ["10-2026-0214811", "음성 대화 기반 면접 답변 평가 방법 및 시스템", "음성 답변을 받아 적고 답변에 기반한 꼬리질문으로 되묻는 모의면접", "p13"],
  ], { y: 1.9, fontSize: 13, colW: [2.2, 3.4, 5.3, 1.2], rowH: 0.9 });
  todo(s, "청구항 요지 문구는 명세서 독립항과 대조해 확정", 0.6, 5.3, 12.1, 0.5);
}
{
  const s = S("A10", "팀 역할 · 품질 보증",
    "Q&A: PR 리뷰 0건·96% 작성자 병합 → «사람 승인 대신 CI와 승격 게이트로 막았다(운영 push 13건 차단, 운영 유출 0). PR 본문 72%에 검증 내역». ⛔ «공동대표» 금지.");
  table(s, ["이름", "역할", "담당"], [
    ["박천웅 (팀장)", "DevSecOps & Full Stack", "인증·보안, AWS 인프라·CI/CD·운영 배포, FE·BE 통합, 결제·사업자 행정"],
    ["김건우", "PM & Frontend", "문제 정의·제품 방향·BM, Next.js 프론트엔드(B2C·B2B·관리자 콘솔), 마케팅·유입 계측"],
    ["노재원", "Backend (Core Logic·AI)", "GitHub 커밋 선별 알고리즘, 근거 묶음·질문 생성 핵심 로직, Spring Boot 백엔드"],
  ], { y: 1.9, fontSize: 13, colW: [2.2, 3.0, 6.9], rowH: 0.7 });
  T(s, "품질 보증", { x: 0.6, y: 4.95, w: 12.1, h: 0.45, fontSize: 18, bold: true });
  bullets(s, ["CI 자동 테스트 2,890개 (BE 2,000 · FE 807 · E2E 83)", "staging → prod 승격 게이트 — 운영 push 13건 차단, 운영 유출 0", "PR 본문의 72%에 검증 내역 기재 · 평가 하네스 회귀 게이트"], { x: 0.6, y: 5.4, w: 12.1, h: 1.5 });
}

pres.writeFile({ fileName: OUT }).then(async () => {
  const { applyTheme } = require("/Users/aiden/.claude/skills/synced/7d77c031-ebb2-409d-bb56-8e8bb28d95ec_d21841c1-b4de-4d28-8737-44603c48d9f0/pptx/scripts/apply_theme.js");
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
});
