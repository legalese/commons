# NEEDS-CORE (sga3): what the keel lacks for ss 76B to 78K

Written 2026-11-18. One request: the keel counts "N units after a day" (convention P1: the day of the event is not counted) and has no function for a period "beginning with" or "ending with" a named day, where the day named is day 1.
The text uses that wording in 16 rules of this range (see fork F-P1 in NOTES.md for the list): "the 6 months beginning with the day on which that contravention occurs" (s 76I(3)), "15 days ending with the date of the meeting" (s 76D(7)(a), s 76DA(4)(a)), "the period of 20 days ending with the resolution date" and "of 30 days" (s 78B(3), s 78C(3)), "the 6 weeks beginning with the resolution date" (ss 78B(4)(b), 78C(4)(b), 78D(2), 78E), "15 days beginning with the date" (s 78C(3)(c), s 78E, s 78F(4)) and "90 days beginning with the date the order is made" (s 78I(3)).

## What this part does now

It calls the keel's `period: the last day of a period after` and `period: the latest day for an act a period before` with the count less one, so the named day is day 1:
- "N days beginning with D": the last day is D plus (N minus 1) days.
- "N days ending with D": the first day is D minus (N minus 1) days.
- "N weeks": the same, in days (7 a week).
- "N months beginning with D": the keel steps D forward N months, which clamps to the last day of a short month (convention P4). The period ends the day before the same date N months on. When the step clamped (D is the 29th, 30th or 31st and the later month is shorter), subtracting one day from the clamped date is wrong by a day. The code tests the round trip: it steps the clamped date back N months and, if that returns D, takes the clamped date less one day, otherwise the clamped date itself. The tests: 15 January 2026 gives 14 July 2026; 31 August 2026 gives 28 February 2027; 31 December 2026 gives 30 June 2027; 28 February 2026 gives 27 August 2026 (`sga3-tests-76h-76k.l4`, the `s 76I(3)` assertions).

This is written out in `sga3-76h-76k.l4` for months, and as plain day counts elsewhere, so a reviewer finds it in each rule and a part that gets the keel function can drop its copy.

## What is asked

Two functions in `sg-periods.l4`, with the same arguments as the existing ones:
- `period: the last day of a period beginning with` (a day, a count, a unit): the last day of the period whose first day is the day given; counts the day given as day 1; for months, the round-trip rule above.
- `period: the first day of a period ending with` (a day, a count, a unit): the first day of the period whose last day is the day given.
Each with the convention recorded as a new P-line (P10) and a fork line in the keel's NOTES.md, because the Act does not say how a period "beginning with" a day is counted and the Interpretation Act 1965 is not among the sources.

## Why it matters

A part that counts "6 months beginning with the 31st" by "plus 6 months, minus 1 day" is wrong by a day in every month that is shorter than the start month, and no assertion on an ordinary date shows it (finding 1 in NOTES.md).
No type, constructor or other function is lacking.
