#!/usr/bin/env bash
# Written for row il-47 (2026-11-10), from the il-43 script. hebcheck.py takes one deposit; this row quotes the National Insurance Law
# consolidation and seven regulation consolidations, so they are joined in a temporary file and every run of Hebrew in the given files
# must occur in the joined text. A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
T="$(mktemp "${TMPDIR:-/tmp}/hebcheck-all.XXXXXX")" || exit 2
trap 'rm -f "$T"' EXIT
cat "$SB/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt" "$SB"/aids/*.he.wiki.txt > "$T"
python3 -I "$HERE/hebcheck.py" "$T" "$@"
