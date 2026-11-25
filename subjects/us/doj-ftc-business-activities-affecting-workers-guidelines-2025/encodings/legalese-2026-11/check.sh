#!/usr/bin/env bash
# Check the DOJ/FTC Antitrust Guidelines for Business Activities Affecting Workers (2025)
# encoding: run every .l4 module with your l4 (the unstable build it was written with) and with a
# build from main (the TARGET), and print, per module, the four numbers that matter on each:
# error diagnostics, assertions satisfied, assertions failed, assertions refused.
#
# Copied from the IP Licensing Guidelines (2017) row of this repository, itself adapted from the
# encoding-a-subject skill's assets/check.sh; only this header, the expected counts, the width of
# the module column and the wording of the TOTAL line differ from that copy. What differs from the
# skill's script:
#   * every module has an expected number of assertions SATISFIED as well as FAILED, and a run that
#     satisfies a different number is red (so a test file that silently stopped running, or lost an
#     assertion, is caught, not only one that fails);
#   * the main run's output is held in a variable, never in a temporary file, and its time limit is
#     perl's alarm (a run killed by it exits 142), so nothing is written outside this folder;
#   * both builds' --version lines are printed.
#
# Why not trust the exit code: the stable (main) `l4 run` exits 0 when an #ASSERT fails (the
# unstable one exits 1), and no exit code says how many assertions ran. The counts are read from
# the diagnostics, from the Message line and the line after it, as the skill's script does.
#
# Usage:  L4=/path/to/unstable/l4 L4_MAIN=/path/to/main/l4 ./check.sh
# Env:    L4         the l4 you write with                  (default: `l4` on PATH)
#         L4_MAIN    a main-build l4                          (default: what fetch-main-l4.sh, next to
#                    this script, prints: the newest main build, fetched from GitHub and cached)
#         L4_MAIN_BUILD    a main build number for fetch-main-l4.sh instead of the newest
#         L4_MAIN_TIMEOUT  seconds each module may take on main (default 300; 0 = no limit)
# The main run has JL4_LIBRARY_PATH unset: a library path newer than the binary breaks it with
# errors that look like the module's. Both runs happen in this folder.
#
# WHAT IT DOES NOT SEE. Equal counts on both builds can hide a different assertion failing on each
# side; there is no #TRACE in this encoding, so no trace outcome goes unseen.
#
# Exit status: 0 only when every module ran with both builds, with no error but its expected failed
# assertions, no refused assertion, exactly the expected satisfied and failed counts, and the same
# four counts on main.  1 something failed.  2 a step did not run (no l4, no main build, a build
# that printed nothing recognisable): that is not a pass.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
MAIN_TIMEOUT="${L4_MAIN_TIMEOUT:-300}"

# Expected assertions satisfied and failed, per module. A module not listed has none of either.
# wk-tests-red.l4 is the positive controls: every assertion in it is wrong on purpose and must fail
# (encoding.json `expected_red`). tests-independent.l4 is the independent test author's file: its
# expected failures are the assertions classified as genuine ambiguity, left failing on purpose
# (NOTES.md, Independent test pass; encoding.json `expected_failed_independent`). Update these
# with the files.
expected_satisfied() {
  case "$1" in
    wk-tests.l4) echo 49 ;;
    wk-tests-boundaries.l4) echo 122 ;;
    tests-independent.l4) echo 120 ;;
    *) echo 0 ;;
  esac
}
expected_failed() {
  case "$1" in
    wk-tests-red.l4) echo 9 ;;
    tests-independent.l4) echo 9 ;;
    *) echo 0 ;;
  esac
}

# Every real `l4 run` prints "Checking succeeded." or a block starting "File:" or "Evaluation[".
# Output with none of them did not come from an l4 that ran the module; a zero count from it is
# not a reading of the module.
produced_output() {
  printf '%s\n' "$1" | grep -a -q -E '^(Checking succeeded|Check succeeded|File:|Evaluation\[)'
}

counts() { # OUTPUT -> "errors satisfied failed refused"
  local msgs
  msgs="$(printf '%s\n' "$1" | grep -a -A1 -E '^[[:space:]]*Message:')"
  printf '%s %s %s %s\n' \
    "$(printf '%s\n' "$1" | grep -a -c 'DiagnosticSeverity_Error')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion satisfied')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion failed|assertion could not be evaluated')" \
    "$(printf '%s\n' "$msgs" | grep -a -c -E 'assertion refused')"
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi
case "$MAIN_TIMEOUT" in ""|*[!0-9]*) echo "check.sh: L4_MAIN_TIMEOUT must be a number of seconds." >&2; exit 2 ;; esac
if ! command -v perl >/dev/null 2>&1; then echo "check.sh: perl is needed for the main run's time limit." >&2; exit 2; fi

# --- the main build ---------------------------------------------------------------------------
MAIN="${L4_MAIN:-}"
if [ -z "$MAIN" ]; then
  fetch="$HERE/fetch-main-l4.sh"
  if [ ! -x "$fetch" ]; then
    echo "check.sh: the target is main, and there is no main-build l4: L4_MAIN is not set and fetch-main-l4.sh is missing. Exit status 2." >&2
    exit 2
  fi
  MAIN="$("$fetch" ${L4_MAIN_BUILD:+"$L4_MAIN_BUILD"})" || {
    echo "check.sh: the target is main, and fetch-main-l4.sh could not get a main-build l4 (its message is above). Set L4_MAIN. Exit status 2." >&2
    exit 2
  }
fi
resolved="$(command -v "$MAIN" 2>/dev/null)" || resolved=""
if [ -z "$resolved" ] || [ ! -x "$resolved" ]; then
  echo "check.sh: the target is main, and '$MAIN' is not an executable l4. Exit status 2." >&2
  exit 2
fi
case "$resolved" in /*) MAIN="$resolved" ;; *) MAIN="$(cd "$(dirname "$resolved")" && pwd)/$(basename "$resolved")" ;; esac
MAIN_VERSION="$(env -u JL4_LIBRARY_PATH "$MAIN" --version 2>/dev/null | tr -d '\000' | head -n 1)"
case "$MAIN_VERSION" in
  unstable-*) echo "check.sh: L4_MAIN is an unstable build ($MAIN_VERSION), not a main build. Exit status 2." >&2; exit 2 ;;
  [0-9]*"(main,"*) ;;
  *) echo "check.sh: warning: cannot confirm that $MAIN is a main build (its --version says '${MAIN_VERSION:-nothing}')." >&2 ;;
esac
L4_VERSION="$("$L4" --version 2>/dev/null | tr -d '\000' | head -n 1)"

echo "your l4:    ${L4_VERSION:-unversioned}"
echo "main build: ${MAIN_VERSION:-unversioned}"
printf '%-30s %4s %4s %4s %4s %9s | %4s %4s %4s %4s  %s\n' module err sat fail ref "expected" err sat fail ref "main"

status=0 n=0 tot_sat=0 tot_msat=0 tot_fail=0 tot_mfail=0
for f in "$HERE"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $HERE" >&2; exit 2; }
  m="$(basename "$f")"
  exs="$(expected_satisfied "$m")" exf="$(expected_failed "$m")"

  out="$(cd "$HERE" && "$L4" run "$m" 2>&1)"
  if ! produced_output "$out"; then
    echo "check.sh: your l4 ('$L4') printed nothing it recognises for $m. Exit status 2." >&2
    exit 2
  fi
  read -r err ok bad ref <<<"$(counts "$out")"

  # The main run, its exit status appended as a last line so that no temporary file is needed.
  mout="$(cd "$HERE" && { perl -e 'my $t = shift @ARGV; alarm $t if $t > 0; exec @ARGV or die "exec: $!\n"' "$MAIN_TIMEOUT" env -u JL4_LIBRARY_PATH "$MAIN" run "$m" 2>&1; echo "check.sh-exit:$?"; } | tr -d '\000')"
  mrc="${mout##*check.sh-exit:}"
  mout="${mout%check.sh-exit:*}"
  timedout=0
  if [ "$mrc" = 142 ]; then
    timedout=1          # killed by the alarm
  elif ! produced_output "$mout"; then
    echo "check.sh: the main build ('$MAIN') printed nothing it recognises for $m (it exited $mrc). Exit status 2." >&2
    exit 2
  fi
  read -r merr mok mbad mref <<<"$(counts "$mout")"

  note=""
  if [ $((err - bad)) -ne 0 ] || [ "$ref" -ne 0 ] || [ "$bad" -ne "$exf" ] || [ "$ok" -ne "$exs" ]; then
    note="differs from expected"; status=1
  fi
  if [ "$timedout" = 1 ]; then
    verdict="reads differently on main (it did not finish in $MAIN_TIMEOUT s)"; status=1
  elif [ "$merr" -ne "$err" ] || [ "$mok" -ne "$ok" ] || [ "$mbad" -ne "$bad" ] || [ "$mref" -ne "$ref" ]; then
    verdict="reads differently on main"; status=1
  else
    verdict="same"
  fi
  printf '%-30s %4d %4d %4d %4d %9s | %4d %4d %4d %4d  %s%s\n' "$m" "$err" "$ok" "$bad" "$ref" "$exs/$exf" "$merr" "$mok" "$mbad" "$mref" "$verdict" "${note:+  <- $note}"
  n=$((n + 1)) tot_sat=$((tot_sat + ok)) tot_msat=$((tot_msat + mok)) tot_fail=$((tot_fail + bad)) tot_mfail=$((tot_mfail + mbad))
done
echo "TOTAL ($n modules): satisfied unstable $tot_sat, main $tot_msat; failed (positive controls and expected failures) unstable $tot_fail, main $tot_mfail"
echo "(a failed assertion is also an error; the expected column is satisfied/failed)"
case "$status" in 0) echo "check.sh: all passed" ;; *) echo "check.sh: FAILED" ;; esac
exit "$status"
