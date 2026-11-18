#!/usr/bin/env bash
# traces.sh FILE.l4 : run FILE with $L4 (your l4) and with $L4_MAIN (the main build check.sh compares with), in this folder, and diff every
# Evaluation block of the two runs.  check.sh compares COUNTS only, so a difference in what a #TRACE prints between the two builds does not turn it
# red; this is the by-hand comparison NOTES.md refers to.  It prints "identical (N blocks)" or the first lines of the difference.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
: "${L4:?set L4 to the l4 binary}" "${L4_MAIN:?set L4_MAIN to the main build}"
T="$(mktemp -d "$HERE/.traces.XXXXXX")"
trap 'rm -rf "$T"' EXIT
"$L4" run "$1" 2>&1 | sed -n '/^Evaluation\[/,$p' | grep -v '^$' > "$T/a.txt"
"$L4_MAIN" run "$1" 2>&1 | sed -n '/^Evaluation\[/,$p' | grep -v '^$' > "$T/b.txt"
n=$(grep -c '^Evaluation\[' "$T/a.txt")
if [ "$n" -eq 0 ]; then echo "NO evaluation blocks from $1: the run did not happen"; exit 1; fi
if diff -q "$T/a.txt" "$T/b.txt" >/dev/null; then echo "$1: evaluation blocks identical on both builds ($n blocks)"; else echo "$1: DIFFERENT:"; diff "$T/a.txt" "$T/b.txt" | head -20; exit 1; fi
