#!/usr/bin/env bash
# Check Section A's two join modules, from this directory.
#
# 1. The copies. The joins import VN-10's and VN-29's modules by bare name, and `l4` looks for an IMPORT only beside the
#    main file and beside the importing file (setting JL4_LIBRARY_PATH instead hides the built-in prelude), so every
#    module they reach sits here. COPIES lists each with its sha256 and its original's path in legalese/commons. A file
#    here that differs from its digest fails the check; so does one that differs from its original, wherever the
#    original is in the same repository. Where it is not, the line says so.
# 2. The joins. `l4 run` exits 0 even when an #ASSERT fails or refuses, so this reads each "Message:" line and the line
#    after it. A CONSIDER in a join module that leaves out a constructor only warns in `l4`; here it fails the check.
#    Warnings from a module a join imports are counted in the last column and do not fail it.
#
# Usage:  bash check.sh            Env: L4, the l4 binary (default: `l4` on PATH)
# Exit status: 0 only when every copy matches and no join module has an error, a failed or refused assertion, or a
# CONSIDER that is not total.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
command -v "$L4" >/dev/null 2>&1 || { echo "check.sh: no l4 binary at '$L4'." >&2; exit 2; }
ROOT="$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null || echo "")"
status=0 copies=0 against=0 elsewhere=0
while read -r f digest orig; do
  case "$f" in ''|'#'*) continue ;; esac
  copies=$((copies+1))
  got="$(shasum -a 256 < "$HERE/$f" 2>/dev/null | cut -d' ' -f1)"
  if [ "$got" != "$digest" ]; then echo "copy $f: sha256 ${got:-missing}, COPIES says $digest" >&2; status=1; continue; fi
  if [ -n "$ROOT" ] && [ -f "$ROOT/$orig" ]; then
    against=$((against+1))
    cmp -s "$HERE/$f" "$ROOT/$orig" || { echo "copy $f: differs from $orig; refresh the copy and its digest in COPIES" >&2; status=1; }
  else
    elsewhere=$((elsewhere+1))
  fi
done < "$HERE/COPIES"
echo "copies: $copies match their digests; $against compared with the original in this repository; $elsewhere whose original is not in it"
printf '%-36s %7s %9s %7s %8s %14s %13s\n' module errors satisfied failed refused not-total-warn imported-warn
for m in nd67-law08-join.l4 nd67-law08-mirrorball-join.l4; do
  out="$(cd "$HERE" && "$L4" run "$m" 2>&1)"
  msgs="$(printf '%s\n' "$out" | grep -A1 -E '^[[:space:]]*Message:')"
  err=$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')
  ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
  bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
  ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
  nt=$(printf '%s\n' "$out" | awk -v m="$m" '/^File:/{file=$2} /branches still need to be considered/{ if (file==m) c++ } END{print c+0}')
  nti=$(printf '%s\n' "$out" | awk -v m="$m" '/^File:/{file=$2} /branches still need to be considered/{ if (file!=m) c++ } END{print c+0}')
  printf '%-36s %7d %9d %7d %8d %14d %13d\n' "$m" "$err" "$ok" "$bad" "$ref" "$nt" "$nti"
  [ "$err" -eq 0 ] && [ "$bad" -eq 0 ] && [ "$ref" -eq 0 ] && [ "$nt" -eq 0 ] || status=1
done
echo "(a copy that does not match, any error, a failed or refused assertion, or a CONSIDER in a join module that is not total, makes the run red)"
exit $status
