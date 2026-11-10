#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for row il-48 and again for row il-49 (2026-11-10). This row quotes one consolidation, and deposits an excerpt of it,
# so every run of Hebrew in the given files must occur in the excerpt (hebcheck.py). A `src:`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
python3 -I "$HERE/hebcheck.py" "$SB/securities-law-5728-1968.he.wiki.excerpt.txt" "$@"
