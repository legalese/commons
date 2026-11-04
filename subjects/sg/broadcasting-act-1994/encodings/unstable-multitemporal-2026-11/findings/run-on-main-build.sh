#!/usr/bin/env bash
# Run each sgbau-*.l4 module of the row on a STABLE (main) build and record, per module:
# the number of error diagnostics, and the distinct identifiers the build could not find.
# This is the forward-looking evidence: the modules that use the time built-ins are not readable on main.
# Usage: L4_MAIN=/path/to/main/l4 ./run-on-main-build.sh        (JL4_LIBRARY_PATH is unset for the run)
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROW="$(cd "$HERE/.." && pwd)"
L4_MAIN="${L4_MAIN:?set L4_MAIN to a main-build l4}"
cd "$ROW" || exit 2
echo "main build: $L4_MAIN ($(env -u JL4_LIBRARY_PATH "$L4_MAIN" --version 2>&1 | head -1))"
for f in sgbau-*.l4; do
  out="$(env -u JL4_LIBRARY_PATH "$L4_MAIN" run "$f" 2>&1)"
  n="$(printf '%s\n' "$out" | grep -c 'DiagnosticSeverity_Error')"
  names="$(printf '%s\n' "$out" | awk '
      /I could not find a definition for the identifier/ { want = 1; next }
      want && NF { gsub(/^ +| +$/, ""); print; want = 0 }' | sort | uniq -c | sort -rn | awk '{c=$1; $1=""; sub(/^ /,""); printf "%s (x%d); ", $0, c}')"
  printf '%-30s errors: %-4s not found: %s\n' "$f" "$n" "${names:-(none)}"
done
