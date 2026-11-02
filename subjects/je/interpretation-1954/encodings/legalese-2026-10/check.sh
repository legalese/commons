#!/usr/bin/env bash
# check.sh: run every module of this encoding of the Interpretation (Jersey) Law 1954 and print, per module, the numbers that matter, then the checks that no single `l4 run` can make.
# Started from the encoding-a-subject skill's check.sh template, extended with the Charities row's warning count, expected_refused table, @ref notices and srcrefs step.
#
# What it does, in order.
#   1. For every .l4 file in this directory it runs `l4 run` (one at a time, under nice) and counts, from the diagnostics and not from the exit code: error diagnostics, assertions satisfied, failed, refused, and
#      warnings (the `Severity: DiagnosticSeverity_Warning` blocks and the bare `Warning |` import lines).  A refused assertion (an #ASSERT whose expression refuses) is also reported by l4 as a warning.
#      The outcome is read from the line AFTER `Message:`, because l4 prints some outcomes there and not on the Message line itself.
#      A module is RED if it has an error other than a failed assertion, a number of failed assertions other than expected_failed says, a number of refused assertions other than expected_refused says,
#      or a number of warnings other than expected_refused says (so any warning that is not a refusal is red).  Both tables below list nothing: every count is zero.
#      (The brief forbids a warning in the deposit.  A refusal that is the point of a test is written #ASSERT REFUSED ... BECAUSE ..., which counts as satisfied.)
#   2. The shape of the modules: ASCII names, the je54- prefix, no `@lang en` at the head, no module over 600 lines.
#   3. srcrefs.py `check --refs` over every module against the Law's current text (the quotations and the locators).  Any problem is red.
#   4. The two l4 notices `follows code on its line` and `is at the end of the file` (an @ref attached to nothing), which `l4 run` prints and does not count as warnings.
#
# Environment.
#   L4         the l4 binary (default: `l4` on PATH).  JL4_LIBRARY_PATH is unset by this script: the standard library is compiled into the binary.
#   L4_TARGET  unstable | main  (default: unstable, which is what this encoding is written for).
#              With `main`, each module is also run with a main build (L4_MAIN, or what fetch-main-l4.sh prints) and the four counts are compared; see the check.sh template of the encoding-a-subject skill (assets/check.sh).
#              No main build has read this encoding (NOTES.md section 3); the main branch of this script has been exercised only as far as refusing to start without a main binary.
#   RAW        the Law's current text (default: ../../source/l_17_1954.current.txt)
#   SRCREFS    srcrefs.py (default: the copy beside this script)
#   If RAW or SRCREFS is not found, step 3 is reported as NOT RUN, and the run says so at the end.  A run with a step not run is not a full check.
# The run takes several minutes (about 30 modules, one after another).
#
# Exit status: 0 only if every step that ran passed.  2 if there is no l4, or a step could not be run.
set -u
unset JL4_LIBRARY_PATH
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIR="${1:-$HERE}"
L4="${L4:-$(command -v l4 || true)}"
TARGET="${L4_TARGET:-unstable}"
MAIN_TIMEOUT="${L4_MAIN_TIMEOUT:-300}"
RAW="${RAW:-$HERE/../../source/l_17_1954.current.txt}"
SRCREFS="${SRCREFS:-$HERE/srcrefs.py}"
L4_SHA="18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475"
MAX_LINES=600

# A module that is MEANT to fail is listed here with its exact count, and named in encoding.json `expected_red`.  None is.
expected_failed() {
  case "$1" in
    *) echo 0 ;;
  esac
}

# A module that is MEANT to refuse (an #ASSERT whose expression refuses, outside #ASSERT REFUSED) is listed with its exact count.  None is.
expected_refused() {
  case "$1" in
    *) echo 0 ;;
  esac
}

# Every real `l4 run` prints "Checking succeeded." or, when it has anything to say, a block that starts with "File:" or "Evaluation[".
produced_output() {
  printf '%s\n' "$1" | grep -a -q -E '^(Checking succeeded|File:|Evaluation\[)'
}

first_error() {
  awk '
    /^File:/ { if (found) exit; src = ""; rng = "" }
    /^  Range:/ { rng = $2 }
    /^  Source:/ { src = $2 }
    /^  Severity: DiagnosticSeverity_Error/ { found = 1; next }
    found && /^  Message:/ { inmsg = 1; next }
    found && inmsg {
      line = $0
      if (line ~ /^ *[0-9]* *\|/) next
      if (line ~ /^ *$/) next
      sub(/^ +/, "", line); sub(/ +$/, "", line)
      text = text (taken ? " " : "") line; taken++
      if (taken >= ((src == "parser" || src == "lexer" || src ~ /^file:/) ? 1 : 3)) exit
    }
    END { if (found) printf "%s %s: %s\n", (src == "parser" || src == "lexer") ? "parse" : ((src == "check") ? "type" : ((src ~ /^file:/) ? "import" : src)), rng, substr(text, 1, 150) }
  '
}

kill_tree() { # kill_tree PID: PID and everything it started, children first, quietly
  local c
  if command -v pgrep >/dev/null 2>&1; then
    for c in $(pgrep -P "$1" 2>/dev/null); do kill_tree "$c"; done
  fi
  kill -9 "$1" 2>/dev/null
}
mpid="" wd="" mtmp=""
cleanup() {
  if [ -n "$wd" ]; then kill_tree "$wd"; wd=""; fi
  if [ -n "$mpid" ]; then kill_tree "$mpid"; mpid=""; fi
  if [ -n "$mtmp" ]; then rm -f -- "$mtmp" "$mtmp.timeout"; mtmp=""; fi
}
trap cleanup EXIT
trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM
trap 'cleanup; exit 129' HUP

if [ -z "$L4" ] || [ ! -x "$L4" ]; then
  echo "check.sh: no l4 binary. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

# --- the main binary, when the target is main --------------------------------------------------
MAIN="" MAIN_VERSION=""
case "$TARGET" in
  unstable) echo "check.sh: the target is unstable, so the main check was skipped." >&2 ;;
  main)
    case "$MAIN_TIMEOUT" in
      ""|*[!0-9]*) echo "check.sh: L4_MAIN_TIMEOUT must be a number of seconds, not '$MAIN_TIMEOUT'." >&2; exit 2 ;;
    esac
    MAIN="${L4_MAIN:-}"
    if [ -z "$MAIN" ]; then
      fetch="${L4_FETCH:-$HERE/fetch-main-l4.sh}"
      [ -x "$fetch" ] || fetch="$(command -v fetch-main-l4.sh 2>/dev/null || true)"
      if [ -z "$fetch" ] || [ ! -x "$fetch" ]; then
        echo "check.sh: the target is main, and there is no main-build l4 to compare with: L4_MAIN is not set and fetch-main-l4.sh was not found next to this script." >&2
        echo "          A run with this step missing is not a full check; this encoding is written for unstable, so set L4_TARGET=unstable." >&2
        exit 2
      fi
      MAIN="$("$fetch" ${L4_MAIN_BUILD:+"$L4_MAIN_BUILD"})" || {
        echo "check.sh: the target is main, and fetch-main-l4.sh could not get a main-build l4 (its message is above)." >&2
        exit 2
      }
    fi
    resolved="$(command -v "$MAIN" 2>/dev/null)" || resolved=""
    if [ -z "$resolved" ] || [ ! -x "$resolved" ]; then
      echo "check.sh: the target is main, and '$MAIN' is not an executable l4. A run with this step missing is not a full check." >&2
      exit 2
    fi
    case "$resolved" in
      /*) MAIN="$resolved" ;;
      *) MAIN="$(cd "$(dirname "$resolved")" && pwd)/$(basename "$resolved")" ;;
    esac
    MAIN_VERSION="$(env -u JL4_LIBRARY_PATH "$MAIN" --version 2>/dev/null | tr -d '\000' | head -n 1)"
    case "$MAIN_VERSION" in
      unstable-*)
        echo "check.sh: L4_MAIN is an unstable build ($MAIN_VERSION), not a main build. The target is main, so there is nothing to compare." >&2
        exit 2 ;;
      [0-9]*"(main,"*) ;;
      *) echo "check.sh: warning: cannot confirm that $MAIN is a main build (its --version says '${MAIN_VERSION:-nothing}')." >&2 ;;
    esac
    ;;
  *)
    echo "check.sh: L4_TARGET must be main or unstable, not '$TARGET'." >&2
    exit 2 ;;
esac

status=0
skipped=""
echo "check.sh of $DIR"
l4sum="$(shasum -a 256 "$L4" | cut -d' ' -f1)"
if [ "$l4sum" = "$L4_SHA" ]; then
  echo "l4 binary: $L4 (sha256 matches the binary the numbers in NOTES.md were produced with, $L4_SHA)"
else
  echo "l4 binary: $L4 (sha256 $l4sum is not the binary the numbers in NOTES.md were produced with, $L4_SHA: the numbers below may differ)"
fi
echo "target: $TARGET"
echo

# ---- 1. every module ----------------------------------------------------------------------------------------------------
total_err=0 total_ok=0 total_bad=0 total_ref=0 total_warn=0 total_exp=0 total_expref=0 n=0 notices=0
t_ok=0 t_n=0 r_n=0 differ=0 m_err=0 m_ok=0 m_bad=0 m_ref=0
if [ "$TARGET" = main ]; then
  echo "main build: ${MAIN_VERSION:-unversioned}"
  printf '%-44s %6s %9s %6s %7s %8s %8s %8s | %6s %9s %6s %7s  %s\n' module errors satisfied failed refused warnings exp.fail exp.ref "errors" satisfied failed refused "main"
else
  printf '%-44s %6s %9s %6s %7s %8s %8s %8s\n' module errors satisfied failed refused warnings exp.fail exp.ref
fi
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$(cd "$DIR" && nice -n 15 "$L4" run "$m" 2>&1)"; rc=$?
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  warn=$(( $(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Warning') + $(printf '%s\n' "$out" | grep -c '^Warning |') ))
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  nt=$(printf '%s\n' "$out" | grep -cE 'is at the end of the file|follows code on its line')
  exp=$(expected_failed "$m")
  expref=$(expected_refused "$m")
  if ! produced_output "$out"; then
    echo "check.sh: your l4 ('$L4') printed nothing it recognises for $m (it exited $rc), so a count of zero from it is not a reading of the module. A run with this step missing is not a full check." >&2
    exit 2
  fi
  if [ "$TARGET" = main ]; then
    # The same module, the same counting, with the main build, bounded by L4_MAIN_TIMEOUT.
    mtmp="$(mktemp "${TMPDIR:-$HERE}/check-main.XXXXXX")" || { echo "check.sh: cannot make a temporary file." >&2; exit 2; }
    ( cd "$DIR" && exec env -u JL4_LIBRARY_PATH "$MAIN" run "$m" >"$mtmp" 2>&1 ) &
    mpid=$!
    wd=""
    if [ "$MAIN_TIMEOUT" -gt 0 ]; then
      ( sleep "$MAIN_TIMEOUT"; kill_tree "$mpid" && touch "$mtmp.timeout" ) >/dev/null 2>&1 &
      wd=$!
    fi
    wait "$mpid" 2>/dev/null; mrc=$?
    mpid=""
    if [ -n "$wd" ]; then kill_tree "$wd"; wait "$wd" 2>/dev/null; wd=""; fi
    timedout=0; [ -e "$mtmp.timeout" ] && timedout=1
    mout="$(tr -d '\000' <"$mtmp")"
    rm -f -- "$mtmp" "$mtmp.timeout"; mtmp=""
    if [ "$timedout" = 0 ] && ! produced_output "$mout"; then
      echo "check.sh: the main build ('$MAIN') printed nothing it recognises for $m (it exited $mrc), so the main step could not run. A run with this step missing is not a full check." >&2
      exit 2
    fi
    mmsgs="$(printf '%s\n' "$mout" | grep -a -A1 -E '^[[:space:]]*Message:')"
    merr=$(printf '%s\n' "$mout" | grep -a -c 'DiagnosticSeverity_Error')
    mok=$(printf '%s\n' "$mmsgs" | grep -a -cE 'assertion satisfied')
    mbad=$(printf '%s\n' "$mmsgs" | grep -a -cE 'assertion failed|assertion could not be evaluated')
    mref=$(printf '%s\n' "$mmsgs" | grep -a -cE 'assertion refused')
    verdict="same"
    if [ "$timedout" = 1 ]; then
      verdict="reads differently on main (it did not finish in $MAIN_TIMEOUT s)"
    elif [ "$merr" -ne "$err" ] || [ "$mok" -ne "$ok" ] || [ "$mbad" -ne "$bad" ] || [ "$mref" -ne "$ref" ]; then
      verdict="reads differently on main"
    elif [ "$mrc" != 0 ] && [ "$merr" -eq 0 ] && [ "$rc" = 0 ]; then
      verdict="reads differently on main (it exited $mrc and printed no error)"
    fi
    [ "$verdict" = same ] || { status=1; differ=$((differ + 1)); }
    printf '%-44s %6d %9d %6d %7d %8d %8d %8d | %6d %9d %6d %7d  %s\n' "$m" "$err" "$ok" "$bad" "$ref" "$warn" "$exp" "$expref" "$merr" "$mok" "$mbad" "$mref" "$verdict"
    if [ "$verdict" != same ] && [ "$merr" -gt 0 ]; then
      printf '    main says: %s\n' "$(printf '%s\n' "$mout" | first_error)"
    fi
    m_err=$((m_err + merr)) m_ok=$((m_ok + mok)) m_bad=$((m_bad + mbad)) m_ref=$((m_ref + mref))
  else
    printf '%-44s %6d %9d %6d %7d %8d %8d %8d\n' "$m" "$err" "$ok" "$bad" "$ref" "$warn" "$exp" "$expref"
  fi
  { [ $((err - bad)) -eq 0 ] && [ "$ref" -eq "$expref" ] && [ "$warn" -eq "$expref" ] && [ "$bad" -eq "$exp" ]; } || { status=1; echo "  ^ RED: $m"; }
  total_err=$((total_err + err)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) total_warn=$((total_warn + warn)) total_exp=$((total_exp + exp)) total_expref=$((total_expref + expref)) n=$((n + 1)) notices=$((notices + nt))
  case "$m" in
    je54-tests-*) t_ok=$((t_ok + ok)) t_n=$((t_n + 1)) ;;
    *) r_n=$((r_n + 1)) ;;
  esac
done
if [ "$TARGET" = main ]; then
  printf '%-44s %6d %9d %6d %7d %8d %8d %8d | %6d %9d %6d %7d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref" "$total_warn" "$total_exp" "$total_expref" "$m_err" "$m_ok" "$m_bad" "$m_ref"
else
  printf '%-44s %6d %9d %6d %7d %8d %8d %8d\n' "TOTAL ($n modules)" "$total_err" "$total_ok" "$total_bad" "$total_ref" "$total_warn" "$total_exp" "$total_expref"
fi
echo "of which the tests modules je54-tests- ($t_n): satisfied $t_ok; the other $r_n modules carry no assertion"
echo "(a failed assertion is also an error and a refused assertion is also a warning; any other error, any refusal or warning beyond the module's expected_refused, and any failed count other than its expected_failed, make the run red)"
if [ "$TARGET" = main ]; then
  if [ "$differ" -eq 0 ]; then echo "(target main: every module has the same four counts on the main build)"; else echo "(target main: $differ module(s) read differently on main, so this encoding is not readable by main as it stands)"; fi
fi
echo "@ref notices (follows code on its line / end of the file): $notices"
[ "$notices" -eq 0 ] || status=1
echo

# ---- 2. the shape of the modules ------------------------------------------------------------------------------------------------------
shape_bad=0 longest=0 longest_name=""
for f in "$DIR"/*.l4; do
  m="$(basename "$f")"
  case "$m" in *[!A-Za-z0-9._-]*) echo "  $m: name is not ASCII-safe"; shape_bad=1 ;; esac
  case "$m" in je54-*) ;; *) echo "  $m: name does not start with je54-"; shape_bad=1 ;; esac
  case "$(head -c 200 "$f")" in "@lang en"*) echo "  $m: starts with @lang en"; shape_bad=1 ;; esac
  lines=$(wc -l <"$f" | tr -d ' ')
  if [ "$lines" -gt "$longest" ]; then longest=$lines; longest_name=$m; fi
  [ "$lines" -le "$MAX_LINES" ] || { echo "  $m: $lines lines, over $MAX_LINES"; shape_bad=1; }
done
if [ "$shape_bad" -eq 0 ]; then
  echo "shape: every module has a plain je54- name, starts without @lang en, and is at most $MAX_LINES lines (the longest is $longest_name, $longest lines)"
else
  status=1
fi

# ---- 3. quotations and locators against the Law's text ---------------------------------------------------------------------------------
if [ -f "$SRCREFS" ] && [ -f "$RAW" ]; then
  res="$(python3 -I "$SRCREFS" check --refs "$RAW" "$DIR"/*.l4 2>&1)"; rc=$?
  printf '%s\n' "$res" | tail -n 5
  [ $rc -eq 0 ] || { echo "srcrefs: PROBLEMS (see above)"; status=1; }
else
  echo "srcrefs: NOT RUN (set SRCREFS to srcrefs.py and RAW to the Law's current text)"
  skipped="$skipped srcrefs"
fi

echo
if [ "$status" -eq 0 ]; then
  if [ -n "$skipped" ]; then echo "check.sh: GREEN for what ran; NOT RUN:$skipped"; else echo "check.sh: GREEN"; fi
else
  echo "check.sh: RED"
fi
echo "(a green run says nothing about whether a domain expert agrees with any reading in NOTES.md; no domain expert has read this encoding against the Law)"
exit $status
