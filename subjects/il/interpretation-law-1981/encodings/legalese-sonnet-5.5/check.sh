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
L4="${L4:-l4}"

# A module that is MEANT to fail (a draft's test cases run against the text as made,
# say) is listed here with its exact count, and named in encoding.json `expected_red`.
expected_failed() {
  case "$1" in
    tests-red.l4) echo 12 ;;   # twelve rejected readings, see the header of tests-red.l4 and NOTES.md
    tests-red-completion.l4) echo 14 ;;   # fourteen rejected readings found in pass 2 (F27 to F34), see the header of tests-red-completion.l4 and NOTES.md
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

# --- Beyond the skill's stock check.sh: the checks specific to this encoding -----------------------------------
# (1) filenames are ASCII; (2) l4 check warnings that check.sh's
# counts do not show; (3) srcrefs.py: every `-- src:` quotation is a verbatim slice of the source, and every
# `@ref` locator lies inside a quotation in the same file.
echo
echo "extra checks"
for f in "$DIR"/*.l4; do
  m="$(basename "$f")"
  case "$m" in *[!A-Za-z0-9._-]*) echo "  FAIL $m: filename is not ASCII-safe"; status=1;; esac
done
echo "  all modules have ASCII filenames"

warn="$(for f in "$DIR"/*.l4; do "$L4" check "$f" 2>&1; done | grep -E 'is at the end of the file|follows code on its line|Not attached' || true)"
if [ -n "$warn" ]; then echo "  FAIL l4 check warnings:"; printf '%s\n' "$warn" | sed 's/^/    /'; status=1; else echo "  l4 check: no stray @ref warnings"; fi

SRC="$DIR/../../source"
if [ -f "$SRC/law.wiki" ] && [ -f "$SRC/ordinance.wiki" ] && command -v python3 >/dev/null 2>&1; then
  stage="$(mktemp -d)"
  cp "$SRC/law.wiki" "$stage/law.txt"; cp "$SRC/ordinance.wiki" "$stage/ordinance.txt"   # srcrefs.py resolves src:ordinance:N to ordinance.txt beside the raw file
  gate="$(python3 -I "$DIR/srcrefs.py" check --refs "$stage/law.txt" "$DIR"/*.l4 2>&1)"; grc=$?
  rm -rf "$stage"
  printf '%s\n' "$gate" | sed 's/^/  srcrefs: /'
  [ "$grc" -eq 0 ] || status=1
else
  echo "  srcrefs: skipped (needs ../../source/law.wiki, ordinance.wiki and python3)"
fi

exit $status
