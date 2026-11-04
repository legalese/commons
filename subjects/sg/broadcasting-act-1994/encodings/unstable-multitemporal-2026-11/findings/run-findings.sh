#!/usr/bin/env bash
# Run every reproducer in this folder with the unstable dev build and write NAME.out beside it.
# Each .out starts with the binary and the clock, then prints one line per diagnostic: range, severity, message.
#
# Usage:  L4=/path/to/l4 [L4_MAIN=/path/to/main/l4] ./run-findings.sh
#   L4       the unstable build to run (default: `l4` on PATH)
#   L4_MAIN  a main build; when given, f09 is also run on it (f09-stable-build-main-build.out)
#
# The clock is pinned with --fixed-now so that a file that reads the wall clock (f06, f07) prints the same thing
# each time it is run.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
L4="${L4:-l4}"
NOW="${FIXED_NOW:-2026-11-03T04:00:00Z}"

# One line per diagnostic: "range  severity  message", the message cut at the first blank line or the next record.
summarise() {
  awk '
    /Range:/    { r = $2 }
    /Severity:/ { s = $2 }
    /Message:/  {
      sub(/^ *Message: */, ""); m = $0; acc = ""
      if (m == "") {
        n = 0
        while (n < 3 && (getline m) > 0) {
          if (m ~ /^(File|Info)/) break
          sub(/^ +/, "", m)
          if (m != "") { acc = acc (n ? " | " : "") m; n++ }
        }
        m = acc
      }
      sub(/DiagnosticSeverity_/, "", s)
      print r "  " s "  " m
    }'
}

cd "$HERE" || exit 2

for f in f*.l4 alt-*.l4; do
  case "$f" in f08a-*) continue ;; esac     # a library for f08b, not a reproducer
  {
    echo "-- $f, run with $("$L4" --version | head -1) ; --fixed-now=$NOW"
    "$L4" run --fixed-now="$NOW" "$f" 2>&1 | summarise | sort -t: -k1,1n -u
  } > "${f%.l4}.out"
done

# f06 twice, with two clocks.
for t in 2012-08-01T04:00:00Z 2026-11-03T04:00:00Z; do
  echo "-- f06 under --fixed-now=$t"
  "$L4" run --fixed-now="$t" f06-unpinned-reading-day-is-the-wall-clock.l4 2>&1 | summarise | sort -u
done > f06-two-clocks.out

# The same smallest file on the stable build, when one is given.
if [ -n "${L4_MAIN:-}" ]; then
  {
    echo "-- f09-stable-build-temporal-only.l4, run with the MAIN build $("$L4_MAIN" --version | head -1)"
    "$L4_MAIN" run f09-stable-build-temporal-only.l4 2>&1 | summarise | sort -u
  } > f09-stable-build-main-build.out
fi
