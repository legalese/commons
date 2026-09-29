#!/usr/bin/env bash
# Run .l4 modules in this encoding and print, per module: error diagnostics, and
# what became of each #ASSERT (satisfied / failed / refused), against the number
# of #ASSERT lines.
# From the encoding-a-subject skill's assets/check.sh, plus one argument: a
# filename PREFIX, so an encoder can check only its own modules
# (`./check.sh . cp-g2a-`) while others are being written beside them.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT fails. The
# failure is a DiagnosticSeverity_Error line whose message is "assertion failed".
#
# Two columns were added by the conductor at g0's request (PLAN.md, trap T5):
#   refused  an #ASSERT whose expression REFUSEs is only a Warning
#            ("assertion refused: …"). The first version counted it nowhere, so a
#            broken vigência gate printed a clean TOTAL and exited 0.
#   asserts  the number of lines starting '#ASSERT'. satisfied + failed + refused
#            should equal it; a shortfall means an assertion produced no verdict,
#            and is printed as UNACCOUNTED.
#
# Usage:  check.sh [DIR] [PREFIX]   (DIR defaults to this script's directory,
#                                    PREFIX to "cp-")
# Env:    L4   the l4 binary        (default: `l4` on PATH)
# Exit status: 0 only when every module has zero errors, zero failed, zero
# refused and zero unaccounted assertions.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
PREFIX="${2:-cp-}"
L4="${L4:-l4}"

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

msg() { printf '%s\n' "$1" | grep -cE "^[[:space:]]*Message:[[:space:]]+assertion $2"; }

total_err=0 total_ok=0 total_bad=0 total_ref=0 total_n=0 unaccounted=0 n=0
printf '%-44s %7s %9s %7s %7s %7s\n' module errors satisfied failed refused asserts
for f in "$DIR"/"$PREFIX"*.l4; do
  [ -e "$f" ] || { echo "check.sh: no $PREFIX*.l4 files in $DIR" >&2; exit 2; }
  out="$("$L4" run "$f" 2>&1)"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(msg "$out" satisfied)
  bad=$(msg "$out" failed)
  ref=$(msg "$out" refused)
  nas=$(grep -cE '^#ASSERT' "$f")
  flag=""
  if [ $((ok + bad + ref)) -ne "$nas" ]; then
    flag="  UNACCOUNTED $((nas - ok - bad - ref))"
    unaccounted=$((unaccounted + 1))
  fi
  printf '%-44s %7d %9d %7d %7d %7d%s\n' "$(basename "$f")" "$err" "$ok" "$bad" "$ref" "$nas" "$flag"
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad))
  total_ref=$((total_ref + ref)) total_n=$((total_n + nas)) n=$((n + 1))
done
printf '%-44s %7d %9d %7d %7d %7d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref" "$total_n"
echo "(a failed assertion also counts as an error; errors minus failed = everything else)"
[ "$total_err" -eq 0 ] && [ "$total_bad" -eq 0 ] && [ "$total_ref" -eq 0 ] && [ "$unaccounted" -eq 0 ]
