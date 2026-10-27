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
# Env:    L4        the l4 binary                          (default: `l4` on PATH)
#         L4_TARGET the dialect the encoding is written for (printed; this encoding targets `unstable`
#                   as the run command names it, and is written for the main dialect of l4 1.6.98)
#         SRC_DIR   the folder holding the two source texts S.C.-2023-c.-17.txt and SOR-2025-35.txt
#                   (default: ../../registers/source-bundle relative to this script)
#
# What this copy adds to the skill's script: a WARNINGS column (any DiagnosticSeverity_Warning makes
# the run red), a WRITTEN column (the #ASSERT lines in the file, which must equal satisfied + failed +
# refused: a written assertion that is never reported is a silent loss), and the srcrefs check at the
# end (every quotation verbatim, every @ref locator covered; the Act files are checked against the Act
# and every other file against the Regulations).
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
    # tests-red.l4) echo 3 ;;
    *) echo 0 ;;
  esac
}

if ! command -v "$L4" >/dev/null 2>&1; then
  echo "check.sh: no l4 binary at '$L4'. Set L4=/path/to/l4 or put l4 on PATH." >&2
  exit 2
fi

SRC_DIR="${SRC_DIR:-$DIR/../../registers/source-bundle}"
echo "check.sh: L4=$L4  L4_TARGET=${L4_TARGET:-unset}  SRC_DIR=$SRC_DIR"
status=0 total_err=0 total_warn=0 total_ok=0 total_bad=0 total_ref=0 total_wr=0 n=0
printf '%-40s %7s %9s %9s %7s %8s %9s %8s\n' module errors warnings satisfied failed refused expected written
for f in "$DIR"/*.l4; do
  [ -e "$f" ] || { echo "check.sh: no .l4 files in $DIR" >&2; exit 2; }
  m="$(basename "$f")"
  out="$("$L4" run "$f" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  warn=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Warning')
  wr=$(grep -c '^#ASSERT' "$f")
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  exp=$(expected_failed "$m")
  printf '%-40s %7d %9d %9d %7d %8d %9d %8d\n' "$m" "$err" "$warn" "$ok" "$bad" "$ref" "$exp" "$wr"
  [ $((err - bad)) -eq 0 ] && [ "$warn" -eq 0 ] && [ "$ref" -eq 0 ] && [ "$bad" -eq "$exp" ] || status=1
  [ "$wr" -eq $((ok + bad + ref)) ] || { echo "  ^ $m: $wr #ASSERT lines written but $((ok + bad + ref)) reported" ; status=1; }
  total_err=$((total_err + err)) total_warn=$((total_warn + warn)) total_ok=$((total_ok + ok)) total_bad=$((total_bad + bad)) total_ref=$((total_ref + ref)) total_wr=$((total_wr + wr)) n=$((n + 1))
done
printf '%-40s %7d %9d %9d %7d %8d %9s %8d\n' "TOTAL ($n modules)" "$total_err" "$total_warn" "$total_ok" "$total_bad" "$total_ref" "" "$total_wr"
echo "(a failed assertion is also an error; any other error or warning, any refused assertion, or any written assertion that was not reported, makes the run red)"

# The srcrefs pass: the Act files against the Act, everything else against the Regulations.
if [ -f "$SRC_DIR/S.C.-2023-c.-17.txt" ] && [ -f "$SRC_DIR/SOR-2025-35.txt" ] && [ -f "$DIR/srcrefs.py" ]; then
  act_files=$(ls "$DIR"/cdba-act*.l4 2>/dev/null)
  reg_files=$(ls "$DIR"/*.l4 | grep -v '/cdba-act[^/]*$')
  echo "srcrefs (Act files):         $(python3 -I "$DIR/srcrefs.py" check --refs "$SRC_DIR/S.C.-2023-c.-17.txt" $act_files 2>&1 | tail -1)"
  python3 -I "$DIR/srcrefs.py" check --refs "$SRC_DIR/S.C.-2023-c.-17.txt" $act_files >/dev/null 2>&1 || status=1
  echo "srcrefs (Regulations files): $(python3 -I "$DIR/srcrefs.py" check --refs "$SRC_DIR/SOR-2025-35.txt" $reg_files 2>&1 | tail -1)"
  python3 -I "$DIR/srcrefs.py" check --refs "$SRC_DIR/SOR-2025-35.txt" $reg_files >/dev/null 2>&1 || status=1
else
  echo "srcrefs: NOT RUN (set SRC_DIR to the folder holding S.C.-2023-c.-17.txt and SOR-2025-35.txt)"
  status=1
fi
exit $status
