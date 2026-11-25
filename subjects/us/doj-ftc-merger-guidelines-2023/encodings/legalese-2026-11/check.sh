#!/usr/bin/env bash
# Check the 2023 Merger Guidelines encoding: run every module with the newest unstable l4 and with a stable (main) l4,
# and compare what each says with the counts expected below.
#
# Usage:  L4=/path/to/unstable/l4 L4_MAIN=/path/to/main/l4 ./check.sh
#   L4        the unstable l4 (default: l4 on PATH)
#   L4_MAIN   a build from main (default: whatever fetch-main-l4.sh, beside this script, prints)
#
# The target is main: a main build has to read every module. Both builds are run in this directory with
# JL4_LIBRARY_PATH unset, so each uses the prelude compiled into it.
#
# Why not trust the exit code: the stable `l4` exits 0 when an #ASSERT fails (the unstable one exits 1). The counts are
# read from the diagnostics, the line after every "Message:" included: errors (DiagnosticSeverity_Error), assertions
# satisfied, assertions failed (or that could not be evaluated), assertions refused.
#
# tests-independent.l4 is the independent test pass (NOTES.md section 10): written by another author from the text, and
# not edited by this encoding's builder.
#
# mg-tests-red.l4 holds positive controls: assertions written to be wrong, so that the harness is shown able to fail.
# Its failures are expected, counted below, and each is also an error diagnostic; any other error makes the run red.
#
# Exit status: 0 only when every module ran with both builds, with no refused assertion, with exactly the expected
# number satisfied and failed, and with no error other than the expected failed assertions.
#   1  something differs        2  a step did not run (no l4, no main build): that is not a pass.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
MAIN="${L4_MAIN:-}"

# Expected assertions satisfied and failed, per module; a module not listed has none. Update with the files.
expected_satisfied() {
  case "$1" in
    mg-tests.l4) echo 155 ;;
    mg-tests-boundaries.l4) echo 138 ;;
    mg-tests-red.l4) echo 0 ;;
    tests-independent.l4) echo 291 ;;
    *) echo 0 ;;
  esac
}
expected_failed() {
  case "$1" in
    mg-tests-red.l4) echo 19 ;;
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then echo "check.sh: no l4 at '$L4'. Set L4=/path/to/l4." >&2; exit 2; fi
if [ -z "$MAIN" ]; then
  if [ -x "$HERE/fetch-main-l4.sh" ]; then MAIN="$("$HERE/fetch-main-l4.sh")" || MAIN=""; fi
fi
if [ -z "$MAIN" ] || ! command -v "$MAIN" >/dev/null 2>&1; then
  echo "check.sh: the main step cannot run: set L4_MAIN to a build from main, or put fetch-main-l4.sh beside this script. Exit status 2." >&2
  exit 2
fi

count() { # BIN FILE -> "errors satisfied failed refused", or NOOUT when the binary printed nothing an l4 run prints
  local out msgs
  out="$(cd "$HERE" && env -u JL4_LIBRARY_PATH "$1" run "$2" 2>&1 | tr -d '\000')"
  if ! printf '%s\n' "$out" | grep -a -q -E '^(Checking succeeded|Check succeeded|File:|Evaluation\[)'; then echo "NOOUT - - -"; return; fi
  msgs="$(printf '%s\n' "$out" | grep -a -A1 -E '^[[:space:]]*Message:')"
  printf '%s %s %s %s\n' \
    "$(printf '%s\n' "$out" | grep -a -c 'DiagnosticSeverity_Error')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion satisfied')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion failed|assertion could not be evaluated')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion refused')"
}

echo "unstable: $(env -u JL4_LIBRARY_PATH "$L4" --version 2>/dev/null | head -n 1)"
echo "main:     $(env -u JL4_LIBRARY_PATH "$MAIN" --version 2>/dev/null | head -n 1)"
printf '%-26s %-26s %-26s %s\n' module "unstable err/sat/fail/ref" "main err/sat/fail/ref" "expected sat/fail"
rc=0 tot_u=0 tot_m=0
for f in "$HERE"/*.l4; do
  b="$(basename "$f")"
  es="$(expected_satisfied "$b")" ef="$(expected_failed "$b")"
  read -r ue us uf ur <<<"$(count "$L4" "$b")"
  read -r me ms mf mr <<<"$(count "$MAIN" "$b")"
  note=""
  if [ "$ue" = NOOUT ] || [ "$me" = NOOUT ]; then note="  <- a build printed nothing for this module"; rc=2
  else
    if [ "$us" != "$es" ] || [ "$uf" != "$ef" ] || [ "$ur" != 0 ] || [ $((ue - uf)) != 0 ]; then note="  <- unstable differs from expected"; [ "$rc" = 0 ] && rc=1; fi
    if [ "$ms" != "$es" ] || [ "$mf" != "$ef" ] || [ "$mr" != 0 ] || [ $((me - mf)) != 0 ]; then note="$note  <- main differs from expected"; [ "$rc" = 0 ] && rc=1; fi
    tot_u=$((tot_u + us)) tot_m=$((tot_m + ms))
  fi
  printf '%-26s %-26s %-26s %s%s\n' "$b" "$ue/$us/$uf/$ur" "$me/$ms/$mf/$mr" "$es/$ef" "$note"
done
echo "assertions satisfied: unstable $tot_u, main $tot_m"
case "$rc" in 0) echo "check.sh: all passed" ;; 1) echo "check.sh: FAILED" ;; 2) echo "check.sh: a step did not run" ;; esac
exit "$rc"
