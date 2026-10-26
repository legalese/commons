#!/usr/bin/env bash
# check.sh: run every module of this encoding of the Charities (Jersey) Law 2014 and print, per module, the numbers that matter, then the checks that no single `l4 run` can make.
# Started from the encoding-a-subject skill's assets/check.sh and the fleet's template check.sh; extended for the nine groups and the integration layer.
#
# What it does, in order.
#   1. For every .l4 file in this directory it runs `l4 run` and counts, from the diagnostics and not from the exit code: error diagnostics, assertions satisfied, failed, refused,
#      and warnings (both the `Severity: DiagnosticSeverity_Warning` blocks and the bare `Warning |` import lines).  A refused assertion is also reported as a warning.
#      A module is RED if it has an error other than a failed assertion, a number of failed assertions other than expected_failed says, a number of refused assertions other than expected_refused says,
#      or a number of warnings other than expected_refused says (so any warning that is not a refusal is red).
#      A refused assertion (an #ASSERT whose expression refuses) is also reported as a Warning, so a module that is meant to refuse has as many warnings as refusals.
#      Only the independent authors' ambiguous and disagree files are meant to refuse (the refusal is the finding); every other module has none.
#   2. The l4 binary and domain.l4 are checked against their sha256 (the numbers below were produced with exactly these two).
#   3. Every module has an ASCII name, does not start with `@lang en`, and a group module (g1- to g9-) imports only prelude, daydate, domain and modules of its OWN group.
#      Only int- modules import across groups.
#   4. srcrefs.py `check --refs` over every module against the Law's text file (the quotations and the locators).
#   5. check-traces.py over every module that has a #TRACE.  A DEONTIC value cannot be compared in #ASSERT, so without this the traces guard nothing.
#      Every trace must carry an `-- EXPECT:` comment and must meet it; a trace with none is reported as UNGUARDED and fails the run.
#   6. The two l4 notices `follows code on its line` and `is at the end of the file` (an @ref attached to nothing), which `l4 run` prints and does not count as warnings.
#
# Environment.
#   L4        the l4 binary (default: ../bin/l4 beside this directory, else l4 on PATH).  Leave JL4_LIBRARY_PATH unset: the standard library is compiled into the binary.
#   RAW       the Law's text file (default: ../inputs/charities-jersey-law-2014-2026-10-02.txt)
#   SRCREFS   srcrefs.py (default: the copy beside this script)
#   TRACES    check-traces.py (default: the copy beside this script)
#   If RAW or SRCREFS is not found, step 4 is reported as NOT RUN, and the run says so at the end.  A run with a step not run is not a full check.
# The run takes a long time (about 160 modules, one after another, under nice).
#
# Exit status: 0 only if every step that ran passed.  2 if there is no l4.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FLEET="${FLEET:-$DIR/..}"
if [ -z "${L4:-}" ]; then
  if [ -x "$FLEET/bin/l4" ]; then L4="$FLEET/bin/l4"; else L4="$(command -v l4 || true)"; fi
fi
RAW="${RAW:-$FLEET/inputs/charities-jersey-law-2014-2026-10-02.txt}"
# In the commons the Law's text is the subject's source/ directory, two levels above this one.
[ -f "$RAW" ] || RAW="$DIR/../../source/charities-jersey-law-2014-2026-10-02.txt"
SRCREFS="${SRCREFS:-$DIR/srcrefs.py}"
TRACES="${TRACES:-$DIR/check-traces.py}"
L4_SHA="18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475"
DOMAIN_SHA="af1703908b8f62922ed36a9984104231b93b41703deec7c1e45f1fef84399d66"

# A module that is MEANT to fail is listed here with its exact count, and named in encoding.json `expected_red`.
# G1 has no such module.  The eight group red files are the groups' own (their counts are the groups' FRAGMENTs'); int-tests-red.l4 is the integrator's;
# the ind-*-tests-ambiguous and ind-*-tests-disagree files are the independent test authors' (NOTES.md, section 11, "Independent tests").
expected_failed() {
  case "$1" in
    g2-tests-red.l4) echo 15 ;;
    g3-tests-red.l4) echo 12 ;;
    g4-tests-red.l4) echo 14 ;;
    g5-tests-red.l4) echo 16 ;;
    g6-tests-red.l4) echo 24 ;;
    g7-tests-red.l4) echo 15 ;;
    g8-tests-red.l4) echo 19 ;;
    g9-tests-red.l4) echo 19 ;;
    int-tests-red.l4) echo 6 ;;
    ind-a-tests-ambiguous.l4) echo 4 ;;
    ind-a-tests-disagree.l4) echo 2 ;;
    ind-b-tests-ambiguous.l4) echo 2 ;;
    ind-c-tests-ambiguous.l4) echo 8 ;;
    *) echo 0 ;;
  esac
}

# A module that is MEANT to refuse is listed with its exact count; a refusal in any other module makes the run red.
expected_refused() {
  case "$1" in
    ind-a-tests-ambiguous.l4) echo 5 ;;
    ind-b-tests-disagree.l4) echo 1 ;;
    ind-c-tests-ambiguous.l4) echo 4 ;;
    *) echo 0 ;;
  esac
}

if [ -z "$L4" ] || [ ! -x "$L4" ]; then
  echo "check.sh: no l4 binary. Set L4=/path/to/l4." >&2
  exit 2
fi
status=0
skipped=""
echo "check.sh of $DIR"
l4sum="$(shasum -a 256 "$L4" | cut -d' ' -f1)"
if [ "$l4sum" = "$L4_SHA" ]; then echo "l4 binary: $L4 (sha256 matches the fleet's binary $L4_SHA)"; else echo "l4 binary: $L4 (sha256 $l4sum is NOT the fleet's binary $L4_SHA: the numbers below may differ)"; status=1; fi
dsum="$(shasum -a 256 "$DIR/domain.l4" | cut -d' ' -f1)"
if [ "$dsum" = "$DOMAIN_SHA" ]; then echo "domain.l4: sha256 matches the pin ($DOMAIN_SHA)"; else echo "domain.l4: sha256 $dsum DIFFERS from the pin $DOMAIN_SHA"; status=1; fi
echo

# ---- 1. every module ----------------------------------------------------------------------------------------------------
total_err=0 total_ok=0 total_bad=0 total_ref=0 total_warn=0 total_exp=0 total_expref=0 n=0 notices=0
g_ok=0 g_bad=0 g_exp=0 g_n=0 i_ok=0 i_bad=0 i_exp=0 i_n=0 d_ok=0 d_bad=0 d_exp=0 d_ref=0 d_expref=0 d_n=0
printf '%-40s %7s %9s %7s %8s %9s %9s %9s\n' module errors satisfied failed refused warnings exp.fail exp.refuse
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$(cd "$DIR" && nice -n 15 "$L4" run "$m" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  warn=$(( $(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Warning') + $(printf '%s\n' "$out" | grep -c '^Warning |') ))
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  nt=$(printf '%s\n' "$out" | grep -cE 'is at the end of the file|follows code on its line')
  exp=$(expected_failed "$m")
  expref=$(expected_refused "$m")
  printf '%-40s %7d %9d %7d %8d %9d %9d %9d\n' "$m" "$err" "$ok" "$bad" "$ref" "$warn" "$exp" "$expref"
  { [ $((err - bad)) -eq 0 ] && [ "$ref" -eq "$expref" ] && [ "$warn" -eq "$expref" ] && [ "$bad" -eq "$exp" ]; } || { status=1; echo "  ^ RED: $m"; }
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) total_warn=$((total_warn + warn)) total_exp=$((total_exp + exp)) total_expref=$((total_expref + expref)) n=$((n + 1)) notices=$((notices + nt))
  case "$m" in
    g[1-9]-*) g_ok=$((g_ok + ok)) g_bad=$((g_bad + bad)) g_exp=$((g_exp + exp)) g_n=$((g_n + 1)) ;;
    int-*) i_ok=$((i_ok + ok)) i_bad=$((i_bad + bad)) i_exp=$((i_exp + exp)) i_n=$((i_n + 1)) ;;
    ind-*) d_ok=$((d_ok + ok)) d_bad=$((d_bad + bad)) d_exp=$((d_exp + exp)) d_ref=$((d_ref + ref)) d_expref=$((d_expref + expref)) d_n=$((d_n + 1)) ;;
  esac
done
printf '%-40s %7d %9d %7d %8d %9d %9d %9d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref" "$total_warn" "$total_exp" "$total_expref"
echo "of which the group modules g1- to g9- ($g_n): satisfied $g_ok, failed $g_bad (expected $g_exp)"
echo "of which the integration modules int- ($i_n): satisfied $i_ok, failed $i_bad (expected $i_exp)"
echo "of which the independent authors' modules ind- ($d_n): satisfied $d_ok, failed $d_bad (expected $d_exp), refused $d_ref (expected $d_expref)"
echo "(a failed assertion is also an error and a refused assertion is also a warning; any other error, any refusal or warning beyond the module's expected_refused, and any failed count other than its expected_failed, make the run red)"
echo "@ref notices (follows code on its line / end of the file): $notices"
[ "$notices" -eq 0 ] || status=1
echo

# ---- 2/3. the shape of the modules and of the import graph ------------------------------------------------------------------------
shape_bad=0
for f in "$DIR"/*.l4; do
  m="$(basename "$f")"
  case "$m" in *[!A-Za-z0-9._-]*) echo "  $m: name is not ASCII-safe"; shape_bad=1 ;; esac
  case "$(head -c 200 "$f")" in "@lang en"*) echo "  $m: starts with @lang en"; shape_bad=1 ;; esac
  case "$m" in
    g[1-9]-*)
      grp="${m:0:2}"
      for imp in $(grep -E '^IMPORT' "$f" | sed -E 's/^IMPORT[[:space:]]+//; s/`//g'); do
        case "$imp" in
          prelude|daydate|domain) ;;
          "$grp"-*) ;;
          *) echo "  $m: imports $imp, which is not prelude, daydate, domain or a $grp- module"; shape_bad=1 ;;
        esac
      done ;;
  esac
done
if [ "$shape_bad" -eq 0 ]; then echo "shape: every module has a plain name and starts without @lang en, and no group module imports another group's"; else status=1; fi

# ---- 4. quotations and locators against the Law's text ---------------------------------------------------------------------------------
if [ -f "$SRCREFS" ] && [ -f "$RAW" ]; then
  res="$(python3 -I "$SRCREFS" check --refs "$RAW" "$DIR"/*.l4 2>&1)"; rc=$?
  printf '%s\n' "$res" | tail -n 5
  [ $rc -eq 0 ] || { echo "srcrefs: PROBLEMS (see above)"; status=1; }
else
  echo "srcrefs: NOT RUN (set SRCREFS to srcrefs.py and RAW to the Law's text file)"
  skipped="$skipped srcrefs"
fi

# ---- 5. the traces -------------------------------------------------------------------------------------------------------------------------
tracefiles=()
for f in "$DIR"/*.l4; do grep -q '^#TRACE' "$f" && tracefiles+=("$f"); done
if [ "${#tracefiles[@]}" -gt 0 ]; then
  python3 -I "$TRACES" --l4 "$L4" --require-all --quiet "${tracefiles[@]}"
  [ $? -eq 0 ] || { echo "traces: PROBLEMS (see above)"; status=1; }
fi

echo
if [ "$status" -eq 0 ]; then
  if [ -n "$skipped" ]; then echo "check.sh: GREEN for what ran; NOT RUN:$skipped"; else echo "check.sh: GREEN"; fi
else
  echo "check.sh: RED"
fi
echo "(a green run is the integrator's: it says nothing about whether a domain expert agrees with any reading in NOTES.md; no domain expert has read this encoding against the Law)"
exit $status
