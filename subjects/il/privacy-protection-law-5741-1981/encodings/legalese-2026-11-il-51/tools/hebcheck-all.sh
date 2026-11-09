#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for row il-51. hebcheck.py takes one deposit; this row quotes seven consolidations (three deposited as excerpts, three whole,
# and the Interpretation Law, read in place from its own subject), so they are joined in a temporary file and every run of Hebrew in the given files must occur in the joined text.
# A `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
SUBJ="$HERE/../../../.."
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/excerpts/privacy-protection-law-5741-1981.he.wiki.excerpt.txt" "$SB/excerpts/eea-regulations-5783-2023.he.wiki.excerpt.txt" \
    "$SB/excerpts/public-bodies-regulations-5746-1986.he.wiki.excerpt.txt" "$SB/inspection-regulations-5741-1981.he.wiki.txt" \
    "$SB/transfer-abroad-regulations-5761-2001.he.wiki.txt" "$SB/fixed-fine-regulations-5764-2004.he.wiki.txt" \
    "$SUBJ/interpretation-law-1981/source/law.wiki" > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
