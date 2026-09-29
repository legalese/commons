#!/usr/bin/env bash
# Run .l4 modules in this encoding and print, per module, the three numbers that
# matter: error diagnostics, assertions satisfied, assertions failed.
# From the encoding-a-subject skill's assets/check.sh, plus one argument: a
# filename PREFIX, so an encoder can check only its own modules
# (`./check.sh . cp-g2-`) while others are being written beside them.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT fails. The
# failure is a DiagnosticSeverity_Error line whose message is "assertion failed".
#
# Usage:  check.sh [DIR] [PREFIX]   (DIR defaults to this script's directory,
#                                    PREFIX to "cp-")
# Env:    L4   the l4 binary        (default: `l4` on PATH)
# Exit status: 0 only when every module has zero errors and zero failed assertions.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
PREFIX="${2:-cp-}"
L4="${L4:-l4}"

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

total_err=0 total_ok=0 total_bad=0 n=0
printf '%-44s %7s %9s %7s\n' module errors satisfied failed
for f in "$DIR"/"$PREFIX"*.l4; do
  [ -e "$f" ] || { echo "check.sh: no $PREFIX*.l4 files in $DIR" >&2; exit 2; }
  out="$("$L4" run "$f" 2>&1)"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$out" | grep -cE '^[[:space:]]*Message:[[:space:]]+assertion satisfied')
  bad=$(printf '%s\n' "$out" | grep -cE '^[[:space:]]*Message:[[:space:]]+assertion failed')
  printf '%-44s %7d %9d %7d\n' "$(basename "$f")" "$err" "$ok" "$bad"
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) n=$((n + 1))
done
printf '%-44s %7d %9d %7d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad"
echo "(a failed assertion also counts as an error; errors minus failed = everything else)"
[ "$total_err" -eq 0 ] && [ "$total_bad" -eq 0 ]
