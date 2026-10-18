# Independent test report: Immigration Act 1971 encoding

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the
Act (ss 1-3ZA, 3C, 24, 24B, 28) before any `.l4` file was opened. Tests are in
`tests-independent.l4`; `ia71-tests.l4` was not read.

## Counts

| | |
|---|---|
| Scenarios written | 94 (20 right of abode / leave, 19 s 3C, 14 commission, 18 maxima, 14 s 28(1)(a), 9 s 28(1A)(a)) |
| Scenarios testable against the encoding | 78 (the 14 commission scenarios and 2 s 3ZA(3) detail scenarios have no counterpart) |
| Assertions | 98 (incl. 10 on the top-level goal) |
| Satisfied | 98 |
| Failed | 0 |
| Non-assertion errors | 0 |

`L4=~/.local/bin/l4 ./check.sh`: 0 errors, 138 satisfied, 0 failed across 6 modules.

## Failures

None. The encoding agreed with every independently fixed value, including the
month-end and 29 February cases:

- s 28(1)(a): 31 Aug 2025 → 28 Feb 2026; 29 Feb 2024 + 3 years → 28 Feb 2027;
  certified 31 Dec 2023 → 29 Feb 2024; the three-year cap against cert + 2 months
  on both sides of the boundary (14 / 15 Nov / 1 Dec 2026 certifications).
- s 28(1A)(a): "beginning with" = the day before the corresponding date, or the
  month end where there is none (31 Aug 2025 → 28 Feb 2026; 1 Sep 2023 → 29 Feb
  2024; arrest 30 Nov 2023 → 29 Feb 2024), which matches my reading R2.
- s 3C: application on the expiry day counts; decision on the expiry day takes
  the case out of s 3C; departure day and day after rights end are not extended;
  decision day with no appeal/review right is not extended (my reading R6).

## Remarks

1. **"Which offence is committed" is not encoded.** The brief's goal 3 asks
   "is it committed", and its scope lists s 24(A1)-(E1A), (1)(b)-(c), (1A) and
   s 24B(1)-(2). The encoding takes the offence as an input enum and computes
   only maxima and time limits. There are no rules for knowledge ("knowingly"),
   "requires leave" (B1, linking to goal 1, e.g. an Irish citizen outside
   s 3ZA(2)-(4) cannot commit B1), "only a limited leave" (C1, and its link to
   s 3C: a person whose leave is extended is not remaining beyond it), E1A's
   water-journey-from-France/Belgium/Netherlands and dangerous-act limbs, the
   "not a British citizen" condition in s 24(1), s 24(1A)'s "first knows" day,
   or s 24B's disqualification (s 24B(2)) and "knows or has reasonable cause to
   believe". Scenarios 40-53 could not be tested. This is the main gap.
2. **s 3ZA(2)-(4) is one boolean.** The three limbs of s 3ZA(3) (directions
   issued, notice given, not withdrawn) are collapsed, so scenarios 12-13
   (no notice; withdrawn) rest on the caller. Acceptable as an input, but the
   Act's structure is not visible.
3. **Need for leave covers entry only.** The goal is `requires leave to enter`;
   s 3ZA(1) and s 3(1)(b) speak of leave to enter *or remain*, and s 1(3)'s
   local-journey exemption is for entry only. Fine for the brief, but the name
   should not be read as answering "need leave to remain".
4. **s 3C pending appeals** ((2)(c), (cb), (d)(ii)) are folded into a single
   "appeal or review rights end on" date. An appeal pending after the
   right-to-bring period would need the caller to supply its pending end date.
5. **Transitional readings are booleans**, not commencement dates against the
   offence date (s 24(G1), s 24B(4)). Correct as inputs; note that s 281(5)
   CJA 2003 has, as far as I know, never been commenced, so the 51-week
   default only bites if the caller says so.
6. **s 28(1)(a) with no certified date** returns the six-month day, and for a
   certified date after the three-year end it returns the three-year day
   (ambiguity A3); neither tested beyond the 20 Dec 2026 case.
7. s 28(1A) is applied to s 24(1)(h) via s 24(3A) — correct, though (1)(h) was
   not in the brief's offence list.
8. No `REFUSE` appears anywhere; nothing in the tested scope needed one.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. On remark 1: the brief's goal 3 named "which offence is committed", but the encoding takes the offence as an input. NOTES.md now says so plainly, and encoding.json's scope too. The other remarks are recorded in NOTES.md as known limits.
