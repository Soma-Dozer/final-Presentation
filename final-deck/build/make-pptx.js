// PPTX 생성: build/img/*.jpg(장표 이미지) + index.html 각 <section>의 <template class="notes">(발표자 노트)
// 노트는 섹션 파일(s*.py)의 S.note()/APX.note()가 정본이다. 여기서 장 번호로 매핑하지 않는다.
const fs = require("fs"), path = require("path"), pptxgen = require("pptxgenjs");
const D = path.dirname(__dirname), IMG = __dirname + "/img";
const html = fs.readFileSync(D + "/index.html", "utf8");
const un = s => s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
// 장표 = 최상위 <section class="slide …">. 장 안에 중첩 <section>이 있어도 세지 않는다.
const secs = html.match(/<section class="slide[\s\S]*?(?=<section class="slide|$)/g);
const slides = secs.map(s => ({
  title: un((s.match(/data-title="([^"]*)"/) || [, ""])[1]),
  notes: (m => (m ? un(m[1]) : ""))(s.match(/<template class="notes">([\s\S]*?)<\/template>/)),
}));
const imgs = fs.readdirSync(IMG).filter(f => f.endsWith(".jpg")).sort();
if (imgs.length !== slides.length) throw new Error(`imgs ${imgs.length} vs slides ${slides.length}`);
const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE";
pres.title = "DevFit 최종발표 — Team Dozer"; pres.author = "Team Dozer";
imgs.forEach((f, i) => {
  const s = pres.addSlide();
  s.addImage({ path: path.join(IMG, f), x: 0, y: 0, w: 13.333, h: 7.5, altText: slides[i].title });
  if (slides[i].notes) s.addNotes(slides[i].notes);
});
const missing = slides.map((s, i) => (s.notes ? null : i + 1)).filter(Boolean);
pres.writeFile({ fileName: path.resolve(D, "../11-최종발표-완성본.pptx") })
  .then(f => console.log("ok", f, imgs.length, "slides · 노트 없는 장:", missing.join(",") || "없음"));
