#!/bin/sh
# Rebuild pc-general-moved.l4 and the generated test modules of completion pass 2026-11-04 (from the encoding folder):
#   sh generators/deferred/build_tests.sh
# Each test module is a head + the structural cases (gen_struct_tests.py) + the hand-written cases, expanded by gen_tests.py.
# The .l4 files are the source of truth once built; this script is kept so the build can be seen.
set -e
G=generators/deferred
cat_files() { python3 -I -c 'import sys; sys.stdout.write("\n".join(open(p, encoding="utf-8").read() for p in sys.argv[1:]))' "$@"; }

for s in b1 b2 b3; do python3 -I $G/gen_struct_tests.py $G/spec_$s.py > $G/tests_struct_$s.in; done
python3 -I $G/gen_struct_tests.py $G/spec_b4.py $G/spec_defs_b4.py > $G/tests_struct_b4.in

cat_files $G/tests_b_head.in $G/tests_struct_b1.in $G/tests_struct_b2.in $G/tests_struct_b3.in $G/tests_b_hand.in > $G/tests_b_all.in
python3 -I $G/gen_tests.py $G/tests_b_all.in pc-body-b-deferred-tests.l4 pc-body-b-deferred.l4 pc-body-b-sexual.l4

cat_files $G/tests_images_head.in $G/tests_struct_b4.in $G/tests_images_hand.in > $G/tests_images_all.in
python3 -I $G/gen_tests.py $G/tests_images_all.in pc-body-b-deferred-images-tests.l4 pc-body-b-deferred-images.l4

python3 -I $G/gen_struct_tests.py $G/spec_a_tests.py > $G/tests_struct_a.in
cat_files $G/tests_a_head.in $G/tests_struct_a.in $G/tests_a_hand.in > $G/tests_a_all.in
python3 -I $G/gen_tests.py $G/tests_a_all.in pc-body-a-deferred-tests.l4 pc-body-a-deferred.l4 pc-body-a-life.l4 pc-exceptions-private-defence.l4

python3 -I $G/autoq.py $G/moved.in pc-general-moved.l4
python3 -I $G/expand.py pc-general-moved.l4
cat_files $G/tests_moved_head.in $G/tests_moved_punish.in $G/tests_moved_hand.in > $G/tests_moved_all.in
python3 -I $G/gen_tests.py $G/tests_moved_all.in pc-general-moved-tests.l4 pc-exceptions-general.l4 pc-body-a-life.l4 pc-exceptions-private-defence.l4
