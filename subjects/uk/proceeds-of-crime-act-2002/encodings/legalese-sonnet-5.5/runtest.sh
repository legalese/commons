#!/usr/bin/env bash
# usage: runtest.sh FILE.l4 [build]   -- counts for one test file on one build (default 109); prints the first errors
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
B=${2:-109}
OUT="$(mktemp "${TMPDIR:-/tmp}/rt.XXXXXX")"
"$L4DIR/l4-main-$B" run "$HERE/$1" > "$OUT" 2>&1
echo "$1 build $B: errors $(grep -c 'Severity: DiagnosticSeverity_Error' "$OUT") satisfied $(grep -c 'Message:  assertion satisfied' "$OUT") failed $(grep -c 'Message:  assertion failed' "$OUT") written $(grep -c '^#ASSERT' "$HERE/$1")"
grep -B4 -A14 'DiagnosticSeverity_Error\|assertion failed' "$OUT" | head -${3:-60}
rm -f "$OUT"
