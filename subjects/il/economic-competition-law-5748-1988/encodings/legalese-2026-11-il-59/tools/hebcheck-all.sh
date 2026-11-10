#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for rows il-48, il-52 and il-59. hebcheck.py takes one deposit; this row quotes four excerpts of consolidations, so the four are joined in a temporary file
# and every run of Hebrew in the given files must occur in the joined text.
# A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/economic-competition-law-5748-1988.he.wiki.excerpt.txt" \
    "$SB/competition-fees-regulations-5749-1989.he.wiki.excerpt.txt" \
    "$SB/police-station-order-5760-2000.he.wiki.excerpt.txt" \
    "$SB/regulations-5724-1964-power-line.he.wiki.excerpt.txt" > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
