#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for row il-48. hebcheck.py takes one deposit; this row quotes four consolidations (the Minimum Wage Law and the
# Youth and Apprentices regulations, deposited in this subject; the National Insurance Law and the Interpretation Law, read in place from their own subjects),
# so the four are joined in a temporary file and every run of Hebrew in the given files must occur in the joined text.
# A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
SUBJ="$HERE/../../../.."
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/minimum-wage-law-5747-1987.he.wiki.txt" "$SB/youth-and-apprentices-regulations-5748-1987.he.wiki.txt" \
    "$SUBJ/national-insurance-law-consolidated-version-5755-1995/registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt" \
    "$SUBJ/interpretation-law-1981/source/law.wiki" > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
