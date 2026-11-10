#!/bin/zsh
# 최종발표 덱 전체 빌드: gen.py → index.html → PDF → PPTX(이미지+노트)
# 여러 세션이 동시에 돌리면 build/img가 섞이므로 잠금을 건다. HTML 미리보기만 필요하면 `python3 gen.py`.
# 필요: python3 · Google Chrome · poppler(pdftoppm, pdfinfo) · node + pptxgenjs(npm i -g pptxgenjs)
set -e
D=$(cd "$(dirname "$0")/.." && pwd)
B=$D/build
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
LOCK=$B/.lock
if ! mkdir $LOCK 2>/dev/null; then echo "다른 세션이 빌드 중 ($(cat $LOCK/who 2>/dev/null)) — 잠시 후 다시"; exit 1; fi
echo "${1:-unknown} $(date +%H:%M:%S)" > $LOCK/who
trap "rm -rf $LOCK" EXIT
python3 $D/gen.py
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000 --print-to-pdf=$B/final.pdf file://$D/index.html 2>/dev/null
rm -rf $B/img && mkdir $B/img
pdftoppm -jpeg -jpegopt quality=92 -scale-to-x 2560 -scale-to-y 1440 $B/final.pdf $B/img/s
NODE_PATH=$(npm root -g) node $B/make-pptx.js
cp $B/final.pdf "$D/../11-최종발표-완성본.pdf"
echo "done: $(pdfinfo $B/final.pdf | grep Pages)"
