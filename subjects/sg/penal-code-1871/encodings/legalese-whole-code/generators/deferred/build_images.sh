#!/bin/sh
# Rebuild pc-body-b-deferred-images.l4 from its generators (run from the encoding folder).
# The .l4 is the source of truth once built; this is kept so the build can be seen.
set -e
G=generators/deferred
python3 -I $G/gen_defs.py $G/spec_defs_b4.py > $G/after_b4_gen.l4
cat $G/after_b4_gen.l4 $G/after_b4_hand.l4 > $G/after_b4.l4
{ cat $G/head_b4.l4; python3 -I $G/gen_offences.py $G/spec_b4.py $G/after_b4.l4; } > pc-body-b-deferred-images.l4
python3 -I $G/expand.py pc-body-b-deferred-images.l4
