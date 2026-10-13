#!/usr/bin/env bash
# check.sh: run every module of this encoding and print, per module, the numbers that matter, then the checks that no single run
# of `l4 run` can make.  Started from the encoding-a-subject skill's assets/check.sh; extended for an eight-group fleet and its
# integration layer.
#
# What it does, in order.
#   1. For every .l4 file in this directory it runs `l4 run` and counts, from the diagnostics and not from the exit code:
#      error diagnostics, assertions satisfied, failed, refused, and warnings.  A refused assertion is also reported as a Warning,
#      so a module that is meant to refuse has as many warnings as refusals.  A module is red if it has an error other than a
#      failed assertion, a number of failed assertions other than expected_failed says, a number of refused assertions other than
#      expected_refused says, or a number of warnings other than expected_refused says (so any warning that is not a refusal is red).
#   2. The vendored time module is checked against its sha256 (the brief pins it).
#   3. Every module starts with `@lang en`, has an ASCII name, and imports only what its group may: a group module imports prelude,
#      daydate, il-interpretation-time, domain and modules of its OWN group; only int- modules (and their tests) and the ind- independent tests import across groups.
#   4. srcrefs.py `check --refs` over every module against the raw sources (quotations and locators).
#   5. check-traces.py over every module that has a #TRACE: a DEONTIC value cannot be compared in #ASSERT, so without this the traces
#      guard nothing.  Every trace must have an expectation (in the module or in int-trace-expect.tsv), and must meet it.
#
# Environment.
#   L4        the l4 binary (default: l4 on PATH).  The fleet's binary is
#             /Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4; leave JL4_LIBRARY_PATH unset.
#   INPUTS    the directory holding law.wiki, regulations-fees.wiki, kovetz-hatakanot-11951-p2116.txt and takanot-12383.txt (or kovetz-hatakanot-12383-p2062.txt); default: ../inputs, else ../../source
#   SRCREFS   the path of srcrefs.py; default: tools/srcrefs.py beside this script (the encoding-a-subject skill's assets/srcrefs.py, vendored)
#   If INPUTS or SRCREFS is not found, step 4 is reported as NOT RUN.  A run with a step not run is not a full check.
#
# Exit status: 0 only if every step that ran passed.  2 if there is no l4.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
# The raw sources: the fleet's own `inputs/` when this directory sits beside one, otherwise the subject's `source/` (two levels up).
if [ -z "${INPUTS:-}" ]; then
  if [ -d "$DIR/../inputs" ]; then INPUTS="$DIR/../inputs"; else INPUTS="$DIR/../../source"; fi
fi
# srcrefs.py: the copy vendored in tools/ (byte-identical to the encoding-a-subject skill's assets/srcrefs.py), unless SRCREFS says otherwise.
if [ -z "${SRCREFS:-}" ]; then
  if [ -f "$DIR/tools/srcrefs.py" ]; then SRCREFS="$DIR/tools/srcrefs.py"; else SRCREFS="/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/srcrefs.py"; fi
fi
# The two Kovetz HaTakanot text layers are named takanot-12383.txt in the fleet's inputs and kovetz-hatakanot-12383-p2062.txt in source/.
KT12383="$INPUTS/takanot-12383.txt"; [ -f "$KT12383" ] || KT12383="$INPUTS/kovetz-hatakanot-12383-p2062.txt"
TIME_SHA="d1552de57266d7dc7a5d2fca43b73e100b8814dc78f33fb755daeb2294cf671f"
L4_SHA="2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187"

# A module that is MEANT to fail is listed here with its exact count, and named in encoding.json `expected_red`.
# A module that is MEANT to refuse (an #ASSERT whose expression returns a named refusal) is listed in expected_refused with its exact
# count, and named in encoding.json `expected_refused`.
expected_failed() {
  case "$1" in
    g1-tests-red.l4) echo 19 ;;
    g2-tests-red.l4) echo 44 ;;
    g3-tests-red.l4) echo 19 ;;
    g4-tests-red.l4) echo 17 ;;
    g5-tests-red.l4) echo 19 ;;
    g6-tests-red.l4) echo 40 ;;
    g7-tests-red.l4) echo 19 ;;
    g8-tests-red.l4) echo 16 ;;
    int-tests-red.l4) echo 14 ;;
    ind-a-tests-ambiguous.l4) echo 2 ;;
    ind-b-tests-ambiguous.l4) echo 16 ;;
    ind-c-tests-ambiguous.l4) echo 2 ;;
    *) echo 0 ;;
  esac
}

expected_refused() {
  case "$1" in
    ind-b-tests-ambiguous.l4) echo 2 ;;
    ind-c-tests-ambiguous.l4) echo 10 ;;
    ind-c-tests-disagree.l4) echo 3 ;;
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi
status=0
skipped=""
l4sum="$(shasum -a 256 "$(command -v "$L4")" 2>/dev/null | cut -d' ' -f1)"
if [ "$l4sum" = "$L4_SHA" ]; then echo "l4 binary: $(command -v "$L4") (sha256 matches the fleet's binary)"; else echo "l4 binary: $(command -v "$L4") (sha256 $l4sum is NOT the fleet's binary $L4_SHA: the numbers below may differ)"; fi
echo

# ---- 1. every module ------------------------------------------------------------------------------------------------------
total_err=0 total_ok=0 total_bad=0 total_ref=0 total_warn=0 total_exp=0 total_expref=0 n=0
printf '%-40s %7s %9s %7s %8s %9s %9s %9s\n' module errors satisfied failed refused warnings exp.fail exp.refuse
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$(cd "$DIR" && nice -n 15 "$L4" run "$m" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  warn=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Warning')
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  exp=$(expected_failed "$m")
  expref=$(expected_refused "$m")
  printf '%-40s %7d %9d %7d %8d %9d %9d %9d\n' "$m" "$err" "$ok" "$bad" "$ref" "$warn" "$exp" "$expref"
  { [ $((err - bad)) -eq 0 ] && [ "$ref" -eq "$expref" ] && [ "$warn" -eq "$expref" ] && [ "$bad" -eq "$exp" ]; } || { status=1; echo "  ^ RED: $m"; }
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) total_warn=$((total_warn + warn)) total_exp=$((total_exp + exp)) total_expref=$((total_expref + expref)) n=$((n + 1))
done
printf '%-40s %7d %9d %7d %8d %9d %9d %9d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref" "$total_warn" "$total_exp" "$total_expref"
echo "(a failed assertion is also an error; a refused assertion is also a warning; any other error, any refusal or warning beyond the module's expected_refused, and any failed count other than its expected_failed, make the run red)"
echo

# ---- 2. the vendored time module --------------------------------------------------------------------------------------------
sum="$(shasum -a 256 "$DIR/il-interpretation-time.l4" | cut -d' ' -f1)"
if [ "$sum" = "$TIME_SHA" ]; then echo "il-interpretation-time.l4: sha256 matches the brief ($TIME_SHA)"; else echo "il-interpretation-time.l4: sha256 $sum DIFFERS from the brief's $TIME_SHA"; status=1; fi

# ---- 3. shape of the modules and of the import graph --------------------------------------------------------------------------
shape_bad=0
for f in "$DIR"/*.l4; do
  m="$(basename "$f")"
  first="$(head -n 1 "$f")"
  [ "$first" = "@lang en" ] || { echo "  $m: first line is not '@lang en'"; shape_bad=1; }
  case "$m" in *[!A-Za-z0-9._-]*) echo "  $m: name is not ASCII-safe"; shape_bad=1 ;; esac
  case "$m" in
    g[1-8]-*)
      grp="${m:0:2}"
      for imp in $(grep -E '^IMPORT' "$f" | sed -E 's/^IMPORT[[:space:]]+//; s/`//g'); do
        case "$imp" in
          prelude|daydate|il-interpretation-time|domain) ;;
          "$grp"-*) ;;
          *) echo "  $m: imports $imp, which is not in its group"; shape_bad=1 ;;
        esac
      done ;;
  esac
done
if [ "$shape_bad" -eq 0 ]; then echo "shape: every module starts with @lang en, has a plain name, and no group module imports another group's"; else status=1; fi

# ---- 4. quotations and locators against the sources ---------------------------------------------------------------------------
if [ -f "$SRCREFS" ] && [ -f "$INPUTS/law.wiki" ] && [ -f "$INPUTS/regulations-fees.wiki" ] && [ -f "$INPUTS/kovetz-hatakanot-11951-p2116.txt" ] && [ -f "$KT12383" ]; then
  raw="$(mktemp -d)"
  ln -s "$INPUTS/law.wiki" "$raw/law.txt"
  ln -s "$INPUTS/regulations-fees.wiki" "$raw/fees.txt"
  ln -s "$INPUTS/kovetz-hatakanot-11951-p2116.txt" "$raw/kt11951.txt"
  ln -s "$KT12383" "$raw/kt12383.txt"
  # the vendored time module quotes the Interpretation Law, a different raw source, and is pinned by its hash (step 2)
  mods=""; for f in "$DIR"/*.l4; do [ "$(basename "$f")" = "il-interpretation-time.l4" ] || mods="$mods $f"; done
  res="$(python3 -I "$SRCREFS" check --refs "$raw/law.txt" $mods 2>&1)"; rc=$?
  rm -rf "$raw"
  printf '%s\n' "$res" | tail -n 3
  [ $rc -eq 0 ] || { echo "srcrefs: PROBLEMS (see above)"; status=1; }
else
  echo "srcrefs: NOT RUN (set SRCREFS to srcrefs.py and INPUTS to the directory of the raw sources)"
  skipped="$skipped srcrefs"
fi

# ---- 5. the traces --------------------------------------------------------------------------------------------------------------
traces=""
for f in "$DIR"/*.l4; do grep -q '^#TRACE' "$f" && traces="$traces $f"; done
if [ -n "$traces" ]; then
  python3 -I "$DIR/check-traces.py" --l4 "$L4" --sidecar "$DIR/int-trace-expect.tsv" --require-all --quiet $traces
  [ $? -eq 0 ] || { echo "traces: PROBLEMS (see above)"; status=1; }
fi

echo
if [ "$status" -eq 0 ]; then
  if [ -n "$skipped" ]; then echo "check.sh: GREEN for what ran; NOT RUN:$skipped"; else echo "check.sh: GREEN"; fi
else
  echo "check.sh: RED"
fi
echo "(a green run is the integrator's: it says nothing about whether a domain expert agrees with any reading in NOTES.md)"
exit $status
