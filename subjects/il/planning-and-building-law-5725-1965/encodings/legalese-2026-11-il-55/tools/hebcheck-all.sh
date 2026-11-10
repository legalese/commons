#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for rows il-48, il-49 and il-55 (2026-11-10). This row quotes four deposits of unofficial consolidations (two excerpts of the Law and of regulations, one whole regulation page),
# so every run of Hebrew in the given files must occur in one of them (hebcheck.py is run against the four joined). A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
JOINED="$(mktemp)"
trap 'rm -f "$JOINED"' EXIT
cat "$SB/planning-and-building-law-5725-1965.he.wiki.excerpt.txt" "$SB/planning-licensing-regulations-5776-2016.he.wiki.excerpt.txt" \
    "$SB/planning-arbitrator-pay-regulations-5769-2009.he.wiki.excerpt.txt" "$SB/planning-arbitrator-procedure-regulations-5769-2008.he.wiki.txt" > "$JOINED"
python3 -I "$HERE/hebcheck.py" "$JOINED" "$@"
