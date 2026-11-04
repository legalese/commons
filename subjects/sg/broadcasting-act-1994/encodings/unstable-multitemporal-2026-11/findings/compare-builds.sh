#!/usr/bin/env bash
# Run every reproducer on two unstable builds and say, per file, whether what they print is identical.
# What is compared: for each diagnostic, its range, severity and the first lines of its message (the same
# summary run-findings.sh writes).  Not a byte comparison of the raw output.
# Usage: L4_A=/path/to/shelf/l4 L4_B=/path/to/dev/l4 ./compare-builds.sh
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
A="${L4_A:?set L4_A}"; B="${L4_B:?set L4_B}"
NOW=2026-11-03T04:00:00Z
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
    }' | sort -u
}
cd "$HERE" || exit 2
echo "A: $("$A" --version | head -1)"
echo "B: $("$B" --version | head -1)"
same=0; diff=0
for f in f*.l4 alt-*.l4 walkthrough-main-probe*.l4; do
  case "$f" in f08a-*) continue ;; esac
  ra="$("$A" run --fixed-now="$NOW" "$f" 2>&1 | summarise)"
  rb="$("$B" run --fixed-now="$NOW" "$f" 2>&1 | summarise)"
  if [ "$ra" = "$rb" ]; then echo "same  $f"; same=$((same+1)); else echo "DIFF  $f"; diff=$((diff+1)); fi
done
for t in 2012-08-01T04:00:00Z 2026-11-03T04:00:00Z; do
  ra="$("$A" run --fixed-now="$t" f06-unpinned-reading-day-is-the-wall-clock.l4 2>&1 | summarise)"
  rb="$("$B" run --fixed-now="$t" f06-unpinned-reading-day-is-the-wall-clock.l4 2>&1 | summarise)"
  if [ "$ra" = "$rb" ]; then echo "same  f06 under --fixed-now=$t"; same=$((same+1)); else echo "DIFF  f06 under --fixed-now=$t"; diff=$((diff+1)); fi
done
echo "identical: $same   different: $diff"
