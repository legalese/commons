# Independent test report: Defence Force Retirement and Death Benefits (Pension Increases) Act 1974

Expectations were written in `independent-expectations.md` from BRIEF.md and the Act before any `.l4` file was opened; `tests-independent.l4` asserts them against `dfrdb74-rules.l4`. The module returns 0 where the Act gives no increase, so "no increase" is asserted as 0.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 25 assertions, 23 satisfied, 2 failed (the 2 errors are those 2 failures; no other diagnostics). The author's dfrdb74-tests.l4: 10 satisfied, 0 failed.

Covered: s 3 lower-of with each limb winning; s 3(3) rounding at x.x4, x.x5 (half rounds up) and x.x6, and on the CPI limb (4.242 -> 4.2); the ss 7/16 gate failing on CPI equal and on AWE equal; the Part II child exclusion; s 8 at 15% and 4.3%; s 9 at 12 months, exact 6 months, a part month of exactly half (15 of June's 30 days, counted), one day short of half (dropped), and under a month (counted as 1); s 17 member and child (additional pension); s 18 at 12, 6, 4 and 1 months, and a child at 6 months.

## Failures

1. **L49, s 9 pension that became payable on 16 June 1974.** Expected 0; the module gives 139.5/12 = 11.625. s 9(1) applies only to an s 82ZB pension "not being a pension that became payable after 15 June 1974". For s 9 the period start *is* the day the pension became payable, so a start after 15 June 1974 means s 9 does not apply, and nor does s 8 (which needs the pension payable before 1 July 1973, or a widow's pension of a contributor who retired before 1 October 1972). The module has no 15 June cut-off; it relies on the caller not to pick the case. The brief names the limit ("not after 15 June 1974") but the code does not apply it.
2. **L64, s 18(1)(b) s 78 benefit that became payable on 20 June 1974.** Expected 0; the module gives 150.003/12 = 12.50025. Same reason: s 18(1)(a) and (b) both exclude "a pension benefit that became payable after 15 June 1974". For an s 18(1)(a) case the input (day after the retirement or death) is not the payable date, so the module cannot apply the cut-off without a further input; for s 18(1)(b) the start date is the payable date and the cut-off could be applied directly.

## Gaps and reading differences

- **s 18 start day**: the module takes "the first day of the counted period" as an input, so the "day after the day on which the relevant retirement or death ... took place" step (s 18(3)) is the caller's. My tests pass the day after (e.g. 2 Jul 1973 for a 1 Jul 1973 retirement). A caller passing the retirement date itself gets a different month count in edge cases.
- **Who falls in which case** (ss 8(1), 9(1), 17(1), 18(1)) is a caller choice; the module does not check the dates (before 1 July 1973, widow of a contributor who retired before 1 October 1972, contributing member on 30 June 1973, etc.).
- **s 8(2)(a)(ii),(iii), (b)**: the notional 1973 amount (after re-classification, commutation, or a husband deemed to die on 29 June 1973) is supplied by the caller as `annual amount before 1 July 1973`; not modelled.
- **s 7 child exclusion** is modelled as its own case returning 0; the module returns nothing distinguishing "not entitled" from "an increase of nil".
- **Dates of effect (ss 13, 22)**: the pay-day of 4 July 1974 appears only in the export description, not as an output; not testable.
- **Part-month day count**: the module measures the part month against the month starting on the part's first day (e.g. 16 Jun -> 16 Jul, 30 days). This agreed with my reading on every case tested; a part month spanning a month end (start on the 31st, or in February) was not tested.
- Money results are exact (no rounding), as the Act states none.

## Change after the pass (encoder)

- **The 15 June 1974 limit (two assertions).** Accepted: a pension or benefit payable after 15 June 1974 gets no increase (F5).
- The gaps are recorded as known limits in NOTES.md.
