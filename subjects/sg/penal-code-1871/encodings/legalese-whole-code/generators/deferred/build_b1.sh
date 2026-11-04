#!/bin/sh
# Rebuild pc-body-b-deferred.l4 from its generators (run from the encoding folder).
set -e
G=generators/deferred
{ cat $G/head_b1.l4; for s in spec_b1 spec_b2 spec_b3; do python3 -I $G/gen_offences.py $G/$s.py $G/after_b1.l4; done; } > pc-body-b-deferred.l4
python3 -I $G/expand.py pc-body-b-deferred.l4
