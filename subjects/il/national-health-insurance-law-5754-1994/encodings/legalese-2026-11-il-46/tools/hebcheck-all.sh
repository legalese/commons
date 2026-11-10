#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for row il-46. hebcheck.py takes one deposit; this row quotes three (the National Health Insurance Law,
# the National Insurance Law and the 1999 Order consolidations), so the three are joined in a temporary file and every run of Hebrew in the given
# files must occur in the joined text. A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/national-health-insurance-law-5754-1994.he.wiki.txt" "$SB/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt" "$SB/regulations/national-insurance-reduced-rates-of-insurance-contributions-order-5759-1999.he.wiki.txt" > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
