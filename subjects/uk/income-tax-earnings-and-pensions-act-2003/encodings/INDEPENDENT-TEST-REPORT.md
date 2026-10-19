# Independent test report: ITEPA 2003 encoding

## Method

1. I read BRIEF.md and the source sections it names (ss 120-121, 132-134, 139-144, 175, 180-183, 401-404) in `../registers/source-bundle/ukpga-2003-1.txt`. I took the three missing formulas from the brief.
2. I wrote `independent-expectations.md` (63 scenarios: 31 for the car, 10 for loans, 22 for termination) before opening any `.l4` file.
3. I then read `itepa-types.l4`, `itepa-rules.l4` and `itepa-goal.l4`, but not `itepa-tests.l4`, and wrote `tests-independent.l4`. It has 100 `#ASSERT`s, including four through the top-level goal. I did not change any expected value to fit the code.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| itepa-tests.l4 | 0 | 46 | 0 |
| tests-independent.l4 | 0 | 100 | 0 |
| TOTAL (5 modules) | 0 | 146 | 0 |

`fails.sh tests-independent.l4` prints nothing.

## Failing assertions

None. Every expectation I worked out from the Act and the brief matches the code. The tests cover:
- the CO2 edges 74, 74.9, 75, 79, 79.9 and 80, the 37% cap, and the diesel cap at 125, 140 and 160 g/km;
- the £5,000 cap on contributions, tested at £0, £5,000 and £7,000;
- unavailability at the start, at the end, in a 45-day gap, in an exact 30-day gap, all three combined, and in the leap year 2023-24 (Y = 366, answer £7,250);
- payments for private use made on 6 July (counts), on 7 July (does not count) and in excess of the provisional sum (gives nil);
- the £10,000 loan threshold at £10,000 and at £10,001;
- interest paid below, equal to and above the official amount, and an exception;
- an averaged balance below £10,000 when the highest balance was above it;
- termination: non-notice and notice cases, nil and negative PENP, s 402D(6) whole months (3 and 2), s 402D(6A) 30.42 by days, a nil minimum notice, month-end clamping (28 Feb, and 29 Feb 2028), redundancy and approved contractual parts, and earlier amounts against the £30,000 threshold.

## Readings and gaps (not failures)

1. **s 144(1)(b), "pays that amount".** The encoding has no field for the amount required. It deducts whatever was paid by 6 July if a payment was required. If the employee pays only part of what is required, the literal words say there is no deduction ("pays that amount" is not met), while HMRC practice deducts the part paid. The code follows practice by construction. I did not assert either reading. This should be stated in NOTES.md.
2. **s 143(2), how the days are entered.** The code adds the days before the first day available, the days after the last day available, and an input count of days in long periods. Nothing stops a long period overlapping the days before or after, which would count those days twice. Nothing checks that each period entered is at least 30 days. A 29-day gap must be entered as 0, so the "30 days or more" rule lives in the input, not in the code.
3. **s 402D(6), whole months near month ends.** Whole months are found by `add months` from the last day of employment, which clamps the day. Take a last day of 28 Feb 2026 and an earliest lawful termination date of 31 Mar 2026, from 3 months' notice given on 31 Dec 2025. `add months` gives 28 Mar, so the code finds no whole month and uses s 402D(6A) (31 days ÷ 30.42). One could argue the period is one whole month, end of month to end of month. This is a small edge and the Act does not settle it. I did not assert it.
4. **s 402E(2)(b), a notice case with no notice date.** The code silently falls back to the last day of employment. A `REFUSE`, or NOTHING, would fit the brief's rule better.
5. **s 402D(5), no pay period before the trigger date.** This is covered only because the caller supplies basic pay and the length of the period. Nothing marks the case.
6. **s 402D(6) and (6A), "the last pay period ... is a month".** The code relies only on the "paid monthly in equal instalments" flag. It ignores the days-in-pay-period input in those cases. That is acceptable, but it should be documented.
7. **s 180(1)(b) and (3), the threshold for non-qualifying loans.** Not encoded. Only the normal threshold, s 180(1)(a), is applied. Section 175(2)(a), "the loan is outstanding and the employee holds the employment", is assumed. The brief accepts both.
8. **s 402C(2), relevant awards.** These are given already split from redundancy pay and the approved contractual part. The code does not work out the approved-contractual comparison.
9. **s 404(5), cash before non-cash benefits within a year.** Not modelled. Section 404(4), earlier years first, is reduced to a single input for earlier amounts. That is adequate for the goal as briefed.
10. **s 139(2)(a) and (4).** The code floors to a whole number and then to a multiple of 5. That is correct for both the 74.9 and 79.9 edges.

## Change after the pass (encoder)

- No disagreements to resolve.
- The points listed above are recorded as known limits in NOTES.md.
