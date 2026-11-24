#!/usr/bin/env bash
# Check the household encoding: run every module with the newest unstable l4 and with a stable (main) l4, prove the proofs file,
# and check that the copied modules are byte for byte the ones they were copied from.
#
# Usage:  L4=/path/to/unstable/l4 L4_MAIN=/path/to/main/l4 ./check.sh
#   L4        the unstable l4 (default: l4 on PATH). Also runs `l4 prove`.
#   L4_MAIN   a build from main, e.g. the one in the L4 VS Code extension. The skill's fetch-main-l4.sh prints a path.
#
# Why not trust the exit code: the stable `l4` exits 0 when an #ASSERT fails (the unstable one exits 1). The counts are read from the diagnostics:
# errors (DiagnosticSeverity_Error), assertions satisfied, assertions failed.
#
# sg-household-tests-proofs.l4 is for `l4 prove` only (a stable l4 has no `prove` and does not read its section GIVEN); it is proved with
# the unstable build and never run.
#
# Exit status: 0 only when every module ran with both builds, with no error and no failed assertion, with the expected number of
# assertions satisfied, with every obligation of the proofs file proved, and with every copied module identical to its source.
#   1  something failed        2  a step did not run (no L4_MAIN, a missing source folder): that is not a pass.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
MAIN="${L4_MAIN:-}"

# Expected assertions satisfied, per module; a module not listed has none. Update with the files.
expected() {
  case "$1" in
    sg-household-tests.l4) echo 71 ;;
    sg-household-tests-properties.l4) echo 53 ;;
    tests-independent.l4) echo 204 ;;
    tests-independent-supplement.l4) echo 26 ;;
    sg-household-tests-iras.l4) echo 174 ;;
    *) echo 0 ;;
  esac
}
EXPECTED_PROVED=5

rc=0
if ! command -v "$L4" >/dev/null 2>&1; then echo "check.sh: no l4 at '$L4'. Set L4=/path/to/l4." >&2; exit 2; fi
if [ -z "$MAIN" ] || ! command -v "$MAIN" >/dev/null 2>&1; then
  echo "check.sh: the main step did not run: set L4_MAIN to a build from main (see the header). Exit status 2." >&2
  rc=2
fi

count() { # BIN FILE -> "errors satisfied failed"
  local out
  out="$("$1" run "$2" 2>&1)"
  if ! printf '%s\n' "$out" | grep -a -q -E '^(Checking succeeded|File:|Evaluation\[)'; then echo "NOOUT 0 0"; return; fi
  printf '%s %s %s\n' \
    "$(printf '%s\n' "$out" | grep -a -c 'DiagnosticSeverity_Error')" \
    "$(printf '%s\n' "$out" | grep -a -c -E '^[[:space:]]*Message:[[:space:]]+assertion satisfied')" \
    "$(printf '%s\n' "$out" | grep -a -c -E '^[[:space:]]*Message:[[:space:]]+assertion failed')"
}

printf '%-30s %-22s %-22s\n' module "unstable (err/sat/fail)" "main (err/sat/fail)"
tot_u=0 tot_m=0
for f in "$HERE"/*.l4; do
  b="$(basename "$f")"
  case "$b" in *-proofs.l4) continue ;; esac
  exp="$(expected "$b")"
  read -r ue us uf <<<"$(count "$L4" "$f")"
  if [ -n "$MAIN" ] && command -v "$MAIN" >/dev/null 2>&1; then read -r me ms mf <<<"$(count "$MAIN" "$f")"; else me="-" ms="-" mf="-"; fi
  note=""
  if [ "$ue" != 0 ] || [ "$uf" != 0 ] || [ "$us" != "$exp" ]; then note="  <- unstable differs from expected $exp"; rc=1; fi
  if [ "$me" != "-" ] && { [ "$me" != 0 ] || [ "$mf" != 0 ] || [ "$ms" != "$exp" ]; }; then note="$note  <- main differs from expected $exp"; rc=1; fi
  printf '%-30s %-22s %-22s%s\n' "$b" "$ue/$us/$uf" "$me/$ms/$mf" "$note"
  case "$us" in ''|*[!0-9]*) ;; *) tot_u=$((tot_u + us)) ;; esac
  case "$ms" in ''|*[!0-9]*) ;; *) tot_m=$((tot_m + ms)) ;; esac
done
echo "assertions satisfied: unstable $tot_u, main $tot_m"

# the proofs
for f in "$HERE"/*-proofs.l4; do
  [ -e "$f" ] || continue
  out="$("$L4" prove "$f" --timeout 60 2>&1)"
  proved=$(printf '%s\n' "$out" | grep -a -c -E '^[[:space:]]+proved ')
  refuted=$(printf '%s\n' "$out" | grep -a -c -E '^[[:space:]]+refuted ')
  unknown=$(printf '%s\n' "$out" | grep -a -c -E '^[[:space:]]+unknown ')
  note=""
  if [ "$proved" != "$EXPECTED_PROVED" ] || [ "$refuted" != 0 ] || [ "$unknown" != 0 ]; then note="  <- expected $EXPECTED_PROVED proved, 0 refuted, 0 unknown"; rc=1; fi
  printf '%-30s proved %s, refuted %s, unknown %s%s\n' "$(basename "$f")" "$proved" "$refuted" "$unknown" "$note"
done

# the copied modules
pair() { # COPY SOURCE
  local src="$HERE/$2"
  if [ ! -e "$src" ]; then echo "copied $1: source $2 not found (not checked)"; [ "$rc" = 0 ] && rc=2; return; fi
  if cmp -s "$HERE/$1" "$src"; then echo "copied $1: identical to $2"; else echo "copied $1: DIFFERS from $2"; rc=1; fi
}
ITA="../legalese-aswathy"
CPF="../../../central-provident-fund-act-1953/encodings/baseline-2026-10"
pair ita-types.l4 "$ITA/ita-types.l4"
pair ita-rates.l4 "$ITA/ita-rates.l4"
pair ita-reliefs.l4 "$ITA/ita-reliefs.l4"
pair cpf-contributions.l4 "$CPF/cpf-contributions.l4"
pair cpf-wages-year.l4 "$CPF/cpf-wages-year.l4"

case "$rc" in 0) echo "check.sh: all passed" ;; 1) echo "check.sh: FAILED" ;; 2) echo "check.sh: a step did not run" ;; esac
exit "$rc"
