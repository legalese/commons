#!/usr/bin/env python3
# Written for row il-60 (2026-11-10). Runs the routine in hebcal.py on its own control first, then on the two date pairs the row types in cp60-cross-references.l4.
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
    ("printed end of the paragraph: 6 Av 5785", (5785, 5, 6), datetime.date(2025, 7, 31)),
    ("footer of printed p. 1017: 7 Tammuz 5782", (5782, 4, 7), datetime.date(2022, 7, 6)),
]
bad = 0
for name, (y, m, d), want in CASES:
    got = hebcal.conv(y, m, d)
    ok = got == want
    bad += 0 if ok else 1
    print(f"{'ok ' if ok else 'BAD'} {name} = {got} (expected {want})")
sys.exit(1 if bad else 0)
