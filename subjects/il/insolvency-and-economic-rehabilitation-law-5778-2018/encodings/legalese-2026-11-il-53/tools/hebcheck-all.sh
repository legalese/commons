#!/usr/bin/env bash
# Written for row il-43 (2026-11-10), adapted for row il-48 and again for row il-53. hebcheck.py takes one deposit; this row has one, the excerpt of the Execution Law
# consolidation, so the script only names it. A `src:N |`, `ext:[tag] N |` or `ext:[SH ... p.N...] |` line is skipped by hebcheck.py.
# Usage (from the row folder): tools/hebcheck-all.sh *.l4 NOTES.md
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SB="$HERE/../../../registers/source-bundle"
python3 -I "$HERE/hebcheck.py" "$SB/execution-law-5727-1967-excerpt-rev3099076.he.wiki.txt" "$@"
