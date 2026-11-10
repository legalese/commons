#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for rows il-48 and il-52. hebcheck.py takes one deposit; this row quotes two excerpts of consolidations, so the two are joined in a temporary file
# and every run of Hebrew in the given files must occur in the joined text.
# A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/prohibition-on-money-laundering-law-5760-2000.he.wiki.excerpt.txt" \
    "$SB/prevention-of-infiltration-offences-and-jurisdiction-law-5714-1954.he.wiki.excerpt.txt" > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
