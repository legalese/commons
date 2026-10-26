#!/usr/bin/env bash
# usage: verify.sh g4   -- re-run one Jersey group's modules in a clean copy (never the encoder's own work dir);
# print the skill's check table and per-file warning/kill counts.  Jersey adaptation of the HVAC fleet-private/verify.sh.
F=/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full
L4=$F/bin/l4
g=$1; D=$F/deposit; V=$F/work/verify/$g
rm -rf "$V"; mkdir -p "$V"
cp "$D"/$g-*.l4 "$D"/domain.l4 "$V"/ || exit 3
echo "files: $(ls "$V" | wc -l); domain.l4 sha256 $(shasum -a 256 "$D"/domain.l4 | cut -c1-16); l4 $($L4 --version)"
env -u JL4_LIBRARY_PATH L4=$L4 nice -n 15 bash $F/skills/encoding-a-subject/assets/check.sh "$V" 2>&1 | grep -v "^domain.l4"
for f in "$V"/$g-*.l4; do
  out=$(env -u JL4_LIBRARY_PATH nice -n 15 $L4 run "$f" 2>&1)
  w=$(printf '%s\n' "$out" | grep -c "DiagnosticSeverity_Warning"); t=$(printf '%s\n' "$out" | grep -c -i "terminated\|killed")
  [ "$w" -ne 0 -o "$t" -ne 0 ] && echo "$(basename $f): warnings=$w killed=$t"
done
echo "(files listed above have warnings or kill markers; none listed = none)"
