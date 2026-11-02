#!/usr/bin/env bash
# Run the Kinnim solver obligations with `l4 prove` (Z3) and check every verdict.
#
#   L4_PROVE=/path/to/an/l4/with/prove ./prove.sh
#
# `l4 prove` is in draft legalese/l4-ide#784 (not merged on 2026-11-02); it needs z3 on PATH or Z3_EXE.
# An IMPORT reaches only the importing file's own folder, so each obligations file is copied beside the
# kn- modules for the run, as "_prove-<name>", and removed afterwards, also on failure.  ../check.sh runs
# every *.l4 in that folder, so do not run it while this script is running: it would pick up the copy.
#
# Expected: every #ASSERT in kn-obligations.l4 and kn-fixed-arity.l4 is `proved` or `decided` (a ground
# witness the evaluator satisfies); every #ASSERT in kn-refutations.l4 is `refuted`.  Anything else, a
# timeout included (l4 prove's default, 10 s an obligation), is a failure.
# Exit 0 only when both hold.  The verdict lines are printed as l4 prints them.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENC="$(cd "$HERE/.." && pwd)"
L4P="${L4_PROVE:-l4}"
fail=0
tmpfiles=()
cleanup() { for f in "${tmpfiles[@]}"; do rm -f "$f"; done; }
trap cleanup EXIT

run() {  # $1 = file in prove/, $2 = the verdicts allowed
  local src="$HERE/$1" dst="$ENC/_prove-$1"
  cp "$src" "$dst"; tmpfiles+=("$dst")
  local out; out="$(cd "$ENC" && "$L4P" prove "_prove-$1" 2>&1)"; local rc=$?
  echo "== $1 (l4 prove exit $rc)"
  printf '%s\n' "$out" | grep -E '^  (proved|refuted|unknown|decided|ENCODING DEFECT)|^      (counterexample|the evaluator|by evaluation|not an obligation)|^coverage|^solver'
  local n_assert; n_assert=$(grep -c '^#ASSERT' "$src")
  local n_ok; n_ok=$(printf '%s\n' "$out" | grep -E -c "^  ($2) ")
  local n_decided; n_decided=$(printf '%s\n' "$out" | grep -c -E '^  decided ')
  local n_decided_sat; n_decided_sat=$(printf '%s\n' "$out" | grep -c 'by evaluation: assertion satisfied')
  local n_decided_bad=$(( n_decided - n_decided_sat ))
  echo "   $n_ok of $n_assert assertions are $2; decided-but-not-satisfied: $n_decided_bad"
  if [ "$n_ok" -ne "$n_assert" ] || [ "$n_decided_bad" -ne 0 ]; then fail=1; echo "   FAIL"; fi
}

run kn-obligations.l4 'proved|decided'
run kn-fixed-arity.l4 'proved|decided'
run kn-refutations.l4 'refuted'
[ "$fail" -eq 0 ] && echo "prove.sh: PASS" || echo "prove.sh: FAIL"
exit "$fail"
