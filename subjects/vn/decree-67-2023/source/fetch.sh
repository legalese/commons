#!/usr/bin/env bash
# Fetch the publisher's document(s), refuse any whose sha256 differs from the pinned one, and write
# raw/<id>.pdf plus raw/<id>.txt (`pdftotext -layout`). raw/ is git-ignored: this repository holds no copy
# of the source (ruling of 2026-10-01: cite an openly published document by URL and digest and fetch it).
# `src:N` in the encodings means line N of raw/<id>.txt.
# Pinned 2026-10-06; Decree 03/2021 and Circular 04/2021 added 2026-10-13 (the earlier regime, NOTES.md §1.5).
# Needs: curl, shasum, pdftotext (poppler); for Circular 04/2021, a scan, also pdftoppm, pdfinfo and tesseract 5. The text layer is a function of the poppler
# version; a different version can move line numbers, which is why the digest pins the PDF, not the text.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
mkdir -p raw
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
fetch() {  # id url sha256 [referer]
  local id="$1" url="$2" sha="$3" ref="${4:-}"
  local args=(-fsSL -m 120 -A "$UA")
  [ -n "$ref" ] && args+=(-e "$ref")
  curl "${args[@]}" -o "raw/$id.pdf" "$url"
  local got; got="$(shasum -a 256 "raw/$id.pdf" | cut -d' ' -f1)"
  if [ "$got" != "$sha" ]; then
    mv "raw/$id.pdf" "raw/$id.pdf.rejected"
    echo "fetch.sh: $id: sha256 $got, expected $sha (the publisher changed the file, or served an error page); kept as raw/$id.pdf.rejected" >&2
    return 1
  fi
  pdftotext -layout "raw/$id.pdf" "raw/$id.txt" 2>/dev/null
  echo "ok  $id  $(wc -l < "raw/$id.txt") lines"
}
fetch "nd67-congbao-1017-1018" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46430-1-20231017-101867-2023-nd-cp.pdf" "19a1de3a974866c90498f3478597798a08892ed6f73d4c461c3f1ef5f41253c8" "https://congbao.chinhphu.vn/"
fetch "nd67-congbao-1019-1020" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/9/40096/46433-1-20231019-102067-2023-nd-cp.pdf" "456cbc7d4cbf8a0eeb3db989ac2edadd0ac9bb3a1fcd024ef4359dcd73b79d59" "https://congbao.chinhphu.vn/"
fetch "nd220-2026-congbao-367" "https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/3/469840-1782964220_v1_1783040868_signed.pdf" "ab0e75cdd5de3b3bc0e0ebc6d3fb03b87b9a4eebfe2658b57b0b16b3c11f3a52" "https://congbao.chinhphu.vn/"

# Circular 04/2021/TT-BTC is published only as a scan (no text layer), so its text is read by OCR: each page at
# 200 dpi with tesseract 5 (`-l vie --psm 4`) and the tessdata_best Vietnamese model, pinned by sha256; the pages are
# joined with a form feed after each. `src:tt04-2021-btc:N` means line N of raw/tt04-2021-btc.txt. A different
# tesseract version can change the text, as a different pdftotext can; the digests pin the PDF and the model.
MODEL_URL="https://github.com/tesseract-ocr/tessdata_best/raw/main/vie.traineddata"
MODEL_SHA="b6b49293d95d0b6dbd8780174627e82c75be957b6f4ed9862155540d6b00bb45"
fetch_ocr() {  # id url sha256
  local id="$1" url="$2" sha="$3"
  local t; for t in pdfinfo pdftoppm tesseract; do
    command -v "$t" >/dev/null || { echo "fetch.sh: $id not fetched: it needs $t (tesseract 5 and poppler); the other sources are fetched" >&2; return 1; }
  done
  curl -fsSL -m 120 -A "$UA" -o "raw/$id.pdf" "$url"
  local got; got="$(shasum -a 256 "raw/$id.pdf" | cut -d' ' -f1)"
  if [ "$got" != "$sha" ]; then mv "raw/$id.pdf" "raw/$id.pdf.rejected"; echo "fetch.sh: $id: sha256 $got, expected $sha" >&2; return 1; fi
  mkdir -p raw/tessdata
  if [ ! -f raw/tessdata/vie.traineddata ] || [ "$(shasum -a 256 raw/tessdata/vie.traineddata | cut -d' ' -f1)" != "$MODEL_SHA" ]; then
    curl -fsSL -o raw/tessdata/vie.traineddata "$MODEL_URL"
    [ "$(shasum -a 256 raw/tessdata/vie.traineddata | cut -d' ' -f1)" = "$MODEL_SHA" ] || { echo "fetch.sh: vie.traineddata sha256 mismatch" >&2; return 1; }
  fi
  local n p f; n=$(pdfinfo "raw/$id.pdf" | awk '/^Pages:/{print $2}'); : > "raw/$id.txt"; mkdir -p "raw/$id.pages"
  for p in $(seq 1 "$n"); do
    f="raw/$id.pages/p$(printf %03d "$p")"
    pdftoppm -r 200 -gray -f "$p" -l "$p" -png -singlefile "raw/$id.pdf" "$f"
    TESSDATA_PREFIX="$PWD/raw/tessdata" OMP_THREAD_LIMIT=1 tesseract "$f.png" "$f" -l vie --psm 4 >/dev/null 2>&1
    rm -f "$f.png"; cat "$f.txt" >> "raw/$id.txt"; printf '\f' >> "raw/$id.txt"
  done
  echo "ok  $id  $(wc -l < "raw/$id.txt") lines (OCR, $n pages)"
}
fetch "nd03-congbao-125-126" "https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2021/1/33026/34365-1-2021125-12603-2021-nd-cp.pdf" "a5523188760d9a3d0d5b5d583d4648736bfc6c45c02c79e03df35220a5d047a7" "https://congbao.chinhphu.vn/"
fetch_ocr "tt04-2021-btc" "https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/03/04-btc.pdf" "e3d32a114944614e624ec36f06c2c787b5f55fd0b3468d24af51aba1b6dccf17"
