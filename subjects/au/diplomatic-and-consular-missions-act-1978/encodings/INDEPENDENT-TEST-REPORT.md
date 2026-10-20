# Independent test report: Diplomatic and Consular Missions Act 1978

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 29 assertions, 28 satisfied and 1 failed. The failed assertion is the only error, so there are no syntax errors.

## Scenarios

1-4 s 4(2)(a)/(b) for a consented mission: a sign at other premises, a sign at the mission's premises, a sign that implies nothing, and a representation (caught, but no s 5 warrant). 5/6 the s 4(2)(c)-(d) carve-out for DOM staff, tested once because the input folds "staff in an authorised capacity" and "at the request of staff" together. 7-9 s 4(2A): caught, at DOM premises, and the (e) carve-out. 10-11 s 4(2B) and its (c) carve-out. 12 no mission. 13-15 s 4(5)/(6) findings: likely only gives an injunction but no warrant; neither finding gives no injunction. 16-19 s 5(5) last day of a warrant: an ordinary month, month-end clamping, a leap year, and no warrant.

## Disagreement (1)

**Scenario 16. Warrant issued 15 Jan 2026: last day in force.** I expected 15 Jul 2026. The encoding gives 14 Jul 2026.

- Source: s 5(5): "a period not exceeding 6 months". The Act does not say when the period begins or how a month is counted.
- My reading: the warrant may run for 6 calendar months from the day of issue, through the corresponding day.
- The encoding's reading: the period begins on the day of issue and ends at the end of the day before the corresponding day (as Acts Interpretation Act 1901 s 2G would compute it). It clamps to the month-end when there is no corresponding day.
- Confidence in my reading: low to moderate. The encoding's reading is defensible under AIA s 2G, but s 2G is not in the source bundle. If the period were taken to begin the day after issue (AIA s 36 "from" convention), my answer would follow. Someone should rule on which convention applies.
- Consequence: the two readings agree at month-ends (scenarios 17-18: 28 Feb 2026, 29 Feb 2024) and differ by one day otherwise. Under the encoding, warrants issued on 30 Aug and on 31 Aug 2023 both end on 29 Feb 2024, while one issued on 29 Aug 2023 ends on 28 Feb 2024.

## Coverage gaps

- s 4(2)(c) and (d) are one boolean, and so are s 4(2A)(e)(i) and (ii). The "in an authorised capacity" condition is assumed inside the boolean, so a DOM staff member acting outside that capacity cannot be tested.
- s 4(2A)(d) and (2B) "a capacity that corresponds to an authorised capacity" is folded into the general "implies another mission" boolean.
- Interim injunctions (s 4(3), (5)(b), (6)(b)) are out of scope, and so is the s 5(1) power for interim proceedings.
- s 4(1)(b)-(d) (aiding, inducing, being a party) has no input.

## Change after the pass (encoder)

- One disagreement is left open: the tester reads a 6-month warrant as running through the corresponding day (`tests-independent.l4` line 48). The encoding keeps the day before (F4); the assertion is expected to fail.
- The gaps are recorded as known limits in NOTES.md.
