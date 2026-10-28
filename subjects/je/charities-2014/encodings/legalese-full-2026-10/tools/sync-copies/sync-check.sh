#!/usr/bin/env bash
# sync-check.sh: diff each block copied into g7-interpretation-laws.l4 against the same block of its source module (comment lines and the text of @ref lines left out).
# See sync-check.py for what it does and for the environment variables.  Usage: sync-check.sh [COPY-MODULE]
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 -I "$HERE/sync-check.py" "$@"
