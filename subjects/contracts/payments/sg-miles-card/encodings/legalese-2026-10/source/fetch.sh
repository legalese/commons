#!/usr/bin/env bash
# Fetches the issuer documents this row encodes, from the issuers' own URLs.
# Nothing here redistributes them: registers/source-bundle.json pins each by
# url + sha256, and this script refuses any file whose bytes differ, so an
# issuer's silent revision is a loud failure here rather than a quiet change
# under the encoding.
#
# Writes raw/<id>.pdf and its `pdftotext -layout` rendering raw/<id>.txt.
# raw/ is ignored by git.
#
# Five documents are web pages, not PDFs: sc-smart-promo-tnc and
# sc-cc-retail-exclusions (the Standard Chartered Singapore site),
# trust-miles-redemption-tnc and trust-freedom-miles-page (trustbank.sg), and
# heymax-trust-welcome-bonus-tnc (help.heymax.ai). A page's
# bytes change on every request (session tokens, navigation), so the digest in
# the bundle is of the CLAUSE TEXT that html2text.py extracts between two
# marker lines, and raw/<id>.html keeps the whole page for reference.
#
# Exit status: 0 every document matched its digest; 1 at least one did not.
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p raw
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
bad=0

# id -> start line, end line, of the clause text on the page
page_markers() {
  case "$1" in
    sc-smart-promo-tnc)
      START='Standard Chartered Smart Credit Card Promotion Terms and Conditions'
      END='All information is correct at the time of printing or posting online.' ;;
    sc-cc-retail-exclusions)
      START='Standard Chartered Credit Cards Retail Transaction Exclusions'
      END='any other charge, fees or payments as we may stipulate from time to time.' ;;
    trust-miles-redemption-tnc)
      START='Eligibility'
      END='Last updated on: 21 September 2026, Version: 1' ;;
    trust-freedom-miles-page)
      START='Stack Miles. Not fees.'
      END='T&Cs apply.' ;;
    heymax-trust-welcome-bonus-tnc)
      START='Terms and Conditions'
      END='HeyMax may amend these terms in accordance with applicable requirements.' ;;
    *) return 1 ;;
  esac
}

while IFS=$'\t' read -r id url sha; do
  if page_markers "$id"; then
    curl -sSL --max-time 60 -A "$UA" -o "raw/$id.html" "$url" || { echo "FETCH FAILED  $id  $url"; bad=1; continue; }
    python3 html2text.py "$START" "$END" < "raw/$id.html" > "raw/$id.txt" || { echo "EXTRACT FAILED $id — the page no longer carries the marker lines"; bad=1; continue; }
    got=$(shasum -a 256 "raw/$id.txt" | cut -c1-64)
    kind="clause text"
  else
    curl -sSL --max-time 60 -A "$UA" -o "raw/$id.pdf" "$url" || { echo "FETCH FAILED  $id  $url"; bad=1; continue; }
    got=$(shasum -a 256 "raw/$id.pdf" | cut -c1-64)
    kind="bytes"
  fi
  if [ "$got" = "$sha" ]; then
    [ -f "raw/$id.pdf" ] && pdftotext -layout "raw/$id.pdf" "raw/$id.txt"
    echo "ok            $id ($kind)"
  else
    echo "DIGEST DIFFERS $id ($kind)  recorded $sha  got $got  — the issuer has revised it; re-read before trusting the encoding"
    bad=1
  fi
done < <(python3 -c '
import json
for d in json.load(open("../registers/source-bundle.json"))["documents"]:
    print(d["id"], d["url"], d["integrity"]["sha256"], sep="\t")')
exit $bad
