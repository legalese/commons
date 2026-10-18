# Independent test report: SSCBA 1992 (Class 1, SSP, SMP)

## Method

1. Read BRIEF.md and the Act's text (ss 5-9, 151-157, 164-166, 171) only.
2. Wrote `independent-expectations.md`: 15 Class 1 scenarios, 20 SSP scenarios and 27 SMP scenarios (62 in all), with the inputs, the expected answer and the Act's words, before opening any `.l4` file.
3. Then read `sscba-types.l4`, `sscba-rules.l4` and `sscba-goal.l4` for names and record shapes only (not `sscba-tests.l4`), and wrote `tests-independent.l4`.
4. Ran `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| | |
|---|---|
| Scenarios in the expectations file | 62 |
| Assertions in `tests-independent.l4` | 97 |
| Satisfied | 97 |
| Failed | 0 |
| Non-assertion errors | 0 |

`check.sh` total: 0 errors, 125 satisfied (28 from the encoder's own tests, 97 independent), 0 failed.

## Failures

None. The encoding matched every value fixed in advance. That includes:

- Class 1 exactly at the primary threshold, exactly at the upper earnings limit, £1 either side, a 0% secondary percentage, 13.8%, equal thresholds and monthly equivalents.
- The SSP weekly rate at the £154.0625 crossover, daily amounts for 1, 3, 4, 5, 6 and 7 qualifying days (as exact fractions), the 28× limit, and linking at 56 days between the periods (links) and 57 (does not).
- The SMP expected week for an expected date on every weekday, including Sunday (its own week) and Saturday (the previous Sunday); the 11th, 14th and 15th weeks before; the 26-week employment edge (EWC − 280 days qualifies, the day after does not); the LEL edge (equal qualifies); reaching the 11th week (its Sunday qualifies, the Saturday before does not); confinement before the 11th week; and the 90% and lower-of rates.
- The top-level goal's fields, including NOTHING where the facts are not given and JUST FALSE where the woman does not qualify.

## Remarks (not failures)

1. **s 164(2)(a) "but has ceased to work for him".** The revised text keeps this limb, but the encoding does not model it. The input `still employed in the 15th week before` covers continuity into the 15th week but not ceasing to work. It needs either a further input or a NOTES.md entry saying it was left out on purpose.
2. **Confinement is a Boolean, not a date.** `confined before the 11th week` skips the date-in-question check altogether. A woman whose confinement is recorded as TRUE qualifies on any question date, even a date before the confinement. A confinement date compared with the 11th week's Sunday and the question date would follow s 164(2)(c) more closely.
3. **SSP daily amount with 0 qualifying days** divides by zero, and the result is an evaluation error. The brief asks for `REFUSE "…"` where the source does not answer; s 157(3) has no answer for a week with no qualifying days.
4. **Linking with periods in the wrong order or overlapping.** `the periods of incapacity link for` returns TRUE when the "later" period begins before the earlier one ended, because the gap is negative. A guard or a REFUSE would be safer.
5. **s 155(3) "first reaches or passes".** Only the entitlement limit is encoded, not whether the maximum entitlement has been reached. That is within the brief's wording ("the entitlement limit"), but the reaching test at equality is the interesting edge, and it is not covered.
6. **Secondary percentage as a whole number.** The input is 15 for 15%, while the rule divides by 100. This is consistent, but a caller giving 0.15 would get a 100× error. The `@desc` should say "per cent, e.g. 15".
7. **Age conditions in s 6(1) (over 16) and s 6(3) (pensionable age)** are not inputs. This is acceptable under the brief's scope, but NOTES.md should record it.
8. **The goal reports £0 SMP rates when she is not entitled.** The goal's `@export` text says so. This is defensible because the source does answer: nothing is payable. It still flattens "not entitled" into a number; the Boolean beside it carries the reason.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md as known limits:
- "but has ceased to work";
- confinement as a flag;
- 0 qualifying days;
- overlapping periods;
- the maximum entitlement not tracked;
- the secondary percentage entered as a whole number;
- the s 6 age conditions;
- £0 SMP rates where not entitled.
