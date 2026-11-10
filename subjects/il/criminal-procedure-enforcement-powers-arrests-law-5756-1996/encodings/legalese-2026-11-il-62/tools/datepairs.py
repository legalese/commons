#!/usr/bin/env python3
# Written for row il-60 (2026-11-10), adapted for row il-62. Runs the routine in hebcal.py on its own control first, then on the two date pairs the row types in ar62-cross-references.l4.
"""Print, and check, the Hebrew-calendar conversions this row relies on.

Month numbers in hebcal.py: Nisan=1 ... Elul=6, Tishri=7, Cheshvan=8, Kislev=9, Tevet=10, Shvat=11, Adar=12.
The control comes first: if it fails, nothing after it is a reading.

Usage: python3 -I tools/datepairs.py     exit 1 if the control or either pair differs from the date expected.
"""
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hebcal  # noqa: E402

CASES = [
    ("control: 30 Kislev 5785", (5785, 9, 30), datetime.date(2024, 12, 31)),
    ("footer of printed p. 89 of Sefer HaChukim 1973: 29 Tevet 5765", (5765, 10, 29), datetime.date(2005, 1, 10)),
    ("footer of printed p. 927 of Sefer HaChukim 2556: 17 Sivan 5776", (5776, 3, 17), datetime.date(2016, 6, 23)),
]
bad = 0
for name, (y, m, d), want in CASES:
    got = hebcal.conv(y, m, d)
    ok = got == want
    bad += 0 if ok else 1
    print(f"{'ok ' if ok else 'BAD'} {name} = {got} (expected {want})")
sys.exit(1 if bad else 0)
