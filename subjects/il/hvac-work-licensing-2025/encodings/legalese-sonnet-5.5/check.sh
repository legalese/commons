#!/usr/bin/env bash
# Run every .l4 module in an encoding and print, per module, the numbers that matter:
# error diagnostics, assertions satisfied, assertions failed, assertions refused.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT refuses, an l4
# built before legalese/l4-ide#518 exits 0 when one fails too, and no exit code
# says which assertion failed or how many ran. An encoding that "ran green" by
# exit code can be carrying any of those.
#
# Why read the line AFTER "Message:": l4 prints some outcomes on the Message line
# itself ("Message:  assertion failed") and others on the next one:
#   * `#ASSERT REFUSED e` where e produces a value: "assertion failed: expected a
#     refusal, but the expression produced a value" (Error severity);
#   * `#ASSERT e` where e REFUSES: "assertion refused: ..." (Warning severity, so it
#     never shows up as an error at all).
# A script that greps the Message line alone undercounts the first and never sees the
# second; a refusing assertion then looks green.
#
# Usage:  check.sh [DIR]          (DIR defaults to the directory this script is in)
# Env:    L4   the l4 binary      (default: `l4` on PATH)
#
# Exit status: 0 only when no module has an error other than its expected failed
# assertions, no assertion refused, and each module fails exactly as often as
# expected_failed says.
set -u
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
L4="${L4:-/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    hvac-tests-red.l4) echo 13 ;;
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

status=0 total_err=0 total_ok=0 total_bad=0 total_ref=0 n=0
printf '%-40s %7s %9s %7s %8s %9s\n' module errors satisfied failed refused expected
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$("$L4" run "$f" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  exp=$(expected_failed "$m")
  printf '%-40s %7d %9d %7d %8d %9d\n' "$m" "$err" "$ok" "$bad" "$ref" "$exp"
  [ $((err - bad)) -eq 0 ] && [ "$ref" -eq 0 ] && [ "$bad" -eq "$exp" ] || status=1
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) n=$((n + 1))
done
printf '%-40s %7d %9d %7d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref"
echo "(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)"
# The vendored time module must stay byte-identical to the Interpretation Law subject's copy,
# which is the canonical one: edit it there, then copy it here.
CANON="$DIR/../../../interpretation-law-1981/encodings/legalese-sonnet-5.5/il-interpretation-time.l4"
if [ -f "$CANON" ]; then
  if cmp -s "$DIR/il-interpretation-time.l4" "$CANON"; then
    echo "il-interpretation-time.l4: identical to the Interpretation Law subject's copy"
  else
    echo "il-interpretation-time.l4: WRONG: differs from $CANON"; status=1
  fi
else
  echo "il-interpretation-time.l4: canonical copy not found beside this row; byte-identity not checked"
fi
exit $status
