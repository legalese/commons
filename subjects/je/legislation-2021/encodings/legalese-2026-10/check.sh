#!/usr/bin/env bash
# Run every .l4 module in this encoding and print, per module, the numbers that matter:
# error diagnostics, warnings, assertions satisfied, assertions failed, assertions refused.
# Then check the quotations and locators against the source text, and the module headers.
#
# Why not trust the exit code: `l4 run` exits 0 when an #ASSERT refuses, an l4 built before
# legalese/l4-ide#518 exits 0 when one fails too, and no exit code says which assertion failed
# or how many ran. An encoding that "ran green" by exit code can be carrying any of those.
#
# Why read the line AFTER "Message:": l4 prints some outcomes on the Message line itself
# ("Message:  assertion failed") and others on the next one:
#   * `#ASSERT REFUSED e` where e produces a value: "assertion failed: expected a refusal, but
#     the expression produced a value" (Error severity);
#   * `#ASSERT e` where e REFUSES: "assertion refused: ..." (Warning severity, so it never shows
#     up as an error at all).
# A script that greps the Message line alone undercounts the first and never sees the second.
#
# The target is `unstable` (Meng, 2026-10-28: nobody will run this row on a `main` build), so the
# template's comparison with a main build is not here, and no `main` build has read this deposit.
#
# Usage:  check.sh [DIR]          (DIR defaults to the directory this script is in)
# Env:    L4         the l4 binary                   (default: `l4` on PATH)
#         L4_TARGET  unstable                        (default: unstable; anything else exits 2)
#         RAW        the plain-text source that the quotations and @ref locators are checked against
#                    (default: ../../source/l_8_2021.current.txt, beside this directory's parent)
#
# Every l4 run is `nice -n 15`, one at a time.
#
# Exit status: 0 only when
#   - no module has an error other than its expected failed assertions,
#   - no module has a warning,
#   - each module fails exactly as often as expected_failed says and refuses exactly as often as
#     expected_refused says,
#   - srcrefs.py check --refs finds no problem in any module,
#   - no module starts with `@lang en` and every file name is ASCII.
# 2 when a step could not be run: no l4, a bad L4_TARGET, no srcrefs.py or no source text.
# A run with a step missing is not a full check, so it does not return 0 or 1.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIR="${1:-$HERE}"
L4="${L4:-l4}"
TARGET="${L4_TARGET:-unstable}"
RAW="${RAW:-$HERE/../../source/l_8_2021.current.txt}"
PINNED_SHA256="18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475"

# A module that is MEANT to fail (a draft's test cases run against the text as made, say) is
# listed here with its exact count, and named in encoding.json `expected_red`. None is.
expected_failed() {
  case "$1" in
    # je21-tests-example.l4) echo 3 ;;
    *) echo 0 ;;
  esac
}

# A module that is MEANT to have assertions that refuse (as a Warning, `assertion refused`) is
# listed here. The refusals this row tests are written `#ASSERT REFUSED ... BECAUSE "..."`,
# which count as satisfied, so none is expected.
expected_refused() {
  case "$1" in
    # je21-tests-example.l4) echo 2 ;;
    *) echo 0 ;;
  esac
}

# Every real `l4 run` prints "Checking succeeded." or, when it has anything to say, a block that
# starts with "File:" or "Evaluation[". Output with none of them did not come from an l4 that ran
# the module (a stub, `true`, a crash), and a count of zero from it is not a reading of the module.
produced_output() {
  printf '%s\n' "$1" | grep -a -q -E '^(Checking succeeded|File:|Evaluation\[)'
}

if [ "$TARGET" != unstable ]; then
  echo "check.sh: this row is written for the unstable compiler; L4_TARGET must be unstable, not '$TARGET'. No main build has read it." >&2
  exit 2
fi
if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 (the prerelease unstable-20261026-6325439 or a later unstable)." >&2
  exit 2
fi
if [ ! -f "$HERE/srcrefs.py" ]; then
  echo "check.sh: srcrefs.py is not beside this script." >&2
  exit 2
fi
if [ ! -f "$RAW" ]; then
  echo "check.sh: the source text '$RAW' is not there. Set RAW=/path/to/l_8_2021.current.txt." >&2
  exit 2
fi

resolved="$(command -v "$L4")"
version="$(env -u JL4_LIBRARY_PATH "$L4" --version 2>/dev/null | tr -d '\000' | head -n 1)"
sha="$(shasum -a 256 "$resolved" 2>/dev/null | awk '{print $1}')"
echo "l4: $resolved"
echo "version: ${version:-unknown}"
echo "sha256: ${sha:-unknown}"
if [ "$sha" != "$PINNED_SHA256" ]; then
  echo "check.sh: note: this is not the binary the row was written with (sha256 $PINNED_SHA256, unstable-20261026-6325439)." >&2
fi

status=0 total_err=0 total_warn=0 total_ok=0 total_bad=0 total_ref=0 n=0
printf '%-48s %7s %8s %9s %7s %8s %9s %9s\n' module errors warnings satisfied failed refused "exp.fail" "exp.refus"
for f in "$DIR"/je21-*.l4; do
  [ -e "$f" ] || { echo "check.sh: no je21-*.l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$(env -u JL4_LIBRARY_PATH nice -n 15 "$L4" run "$f" 2>&1)"
  if ! produced_output "$out"; then
    echo "check.sh: your l4 ('$L4') printed nothing it recognises for $m, so no count from it means anything." >&2
    exit 2
  fi
  msgs="$(printf '%s\n' "$out" | grep -a -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -a -c 'DiagnosticSeverity_Error')
  warn=$(( $(printf '%s\n' "$out" | grep -a -c 'DiagnosticSeverity_Warning') + $(printf '%s\n' "$out" | grep -a -c '^Warning |') ))
  ok=$(printf '%s\n' "$msgs" | grep -a -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -a -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -a -cE 'assertion refused')
  expf=$(expected_failed "$m")
  expr=$(expected_refused "$m")
  # A refused assertion is a Warning, so it is also counted in $warn; it is judged by expected_refused, not twice.
  [ $((err - bad)) -eq 0 ] && [ $((warn - ref)) -eq 0 ] && [ "$ref" -eq "$expr" ] && [ "$bad" -eq "$expf" ] || status=1
  total_err=$((total_err + err)) total_warn=$((total_warn + warn)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) n=$((n + 1))
  printf '%-48s %7d %8d %9d %7d %8d %9d %9d\n' "$m" "$err" "$warn" "$ok" "$bad" "$ref" "$expf" "$expr"
done
printf '%-48s %7d %8d %9d %7d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_warn" "$total_ok" "$total_bad" "$total_ref"
echo "(a failed assertion is also an error; any other error, any warning, or any refused assertion not in expected_refused, makes the run red)"

# --- the source text: quotations and @ref locators ---------------------------------------------
echo
echo "srcrefs: every quotation and every @ref locator against $(basename "$RAW")"
refs_out="$(python3 -I "$HERE/srcrefs.py" check --refs "$RAW" "$DIR"/je21-*.l4 2>&1)"; refs_rc=$?
printf '%s\n' "$refs_out" | tail -n 25
[ "$refs_rc" -eq 0 ] || status=1
case "$(printf '%s\n' "$refs_out" | tail -n 1)" in
  *" 0 problems") ;;
  *) status=1 ;;
esac

# --- headers and names -------------------------------------------------------------------------
echo
lang=0 nonascii=0
for f in "$DIR"/*; do
  b="$(basename "$f")"
  if printf '%s' "$b" | LC_ALL=C grep -q '[^ -~]'; then echo "check.sh: file name is not ASCII: $b" >&2; nonascii=$((nonascii + 1)); fi
done
for f in "$DIR"/je21-*.l4; do
  first="$(grep -a -v -E '^[[:space:]]*$' "$f" | head -n 1)"
  case "$first" in
    "@lang en"*) echo "check.sh: $(basename "$f") starts with @lang en" >&2; lang=$((lang + 1)) ;;
  esac
done
echo "headers: $lang module(s) start with @lang en; $nonascii file name(s) are not ASCII"
[ "$lang" -eq 0 ] && [ "$nonascii" -eq 0 ] || status=1

if [ "$status" -eq 0 ]; then echo "RESULT: green"; else echo "RESULT: RED (read the lines above)"; fi
exit $status
