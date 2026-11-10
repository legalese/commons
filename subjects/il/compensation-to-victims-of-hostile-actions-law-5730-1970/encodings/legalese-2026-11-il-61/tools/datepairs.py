#!/usr/bin/env python3
# Written for row il-60 (2026-11-10), adapted for row il-61. Runs the routine in hebcal.py on its own control first, then on the date pairs the row types in ha61-cross-references.l4.
"""Print, and check, the Hebrew-calendar conversions this row relies on.

Month numbers in hebcal.py: Nisan=1 ... Elul=6, Tishri=7, Cheshvan=8, Kislev=9, Tevet=10, Shvat=11, Adar=12.
The control comes first: if it fails, nothing after it is a reading.

Usage: python3 -I tools/datepairs.py     exit 1 if the control or any pair differs from the date expected.
"""
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hebcal  # noqa: E402

CASES = [
    ("control: 30 Kislev 5785", (5785, 9, 30), datetime.date(2024, 12, 31)),
    ("footer of printed p. 614 of Sefer HaChukim 3072: 14 Av 5783", (5783, 5, 14), datetime.date(2023, 8, 1)),
    ("footer of printed p. 799 of Sefer HaChukim 3549: 5 Av 5786", (5786, 5, 5), datetime.date(2026, 7, 19)),
    ("footer of printed p. 36 of Sefer HaChukim 2118: 15 Kislev 5768", (5768, 9, 15), datetime.date(2007, 11, 25)),
    ("footer of printed pp. 272 to 273 of Sefer HaChukim 3493: 10 Shvat 5786", (5786, 11, 10), datetime.date(2026, 1, 28)),
    ("footer of printed p. 1160 of Sefer HaChukim 2573: 7 Av 5776", (5776, 5, 7), datetime.date(2016, 8, 11)),
    ("footer of printed pp. 992 to 993 of Sefer HaChukim 2307: 26 Tammuz 5771", (5771, 4, 26), datetime.date(2011, 7, 28)),
    ("date in the text of printed p. 993 of Sefer HaChukim 2307: 2 Tishri 5761", (5761, 7, 2), datetime.date(2000, 10, 1)),
]
bad = 0
for name, (y, m, d), want in CASES:
    got = hebcal.conv(y, m, d)
    ok = got == want
    bad += 0 if ok else 1
    print(f"{'ok ' if ok else 'BAD'} {name} = {got} (expected {want})")
sys.exit(1 if bad else 0)
