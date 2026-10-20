# Independent test report: National Rental Affordability Scheme Act 2008

Expectations were written from BRIEF.md and the source text (`independent-expectations.md`) before any L4 was read; `nras-rules.l4` was then read for names and input shapes only.

## Result

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **36 assertions, 35 satisfied, 1 failed**, no other errors.

## Scenarios

- Rental dwelling (s 4): all four kinds, and rent not payable (5).
- Incentive period end (s 4): starts 1 July 2008, 1 May 2010, 15 March 2012, 29 February 2012 (4).
- NRAS year (s 4): the day before the first year, both ends of the short first year, both sides of each later 1 May boundary, a mid-year day (14 assertions, 7 days).
- Allocation conditions (s 7(2), (5)): rent exactly 20% below market and one dollar over; mixed charges where one fails; s 7(5) disapplication, including that it does not rescue non-prescribed tenants; the newness condition and its unfit-then-made-fit route; vacancy at and above the allowed maximum; a year not rented with non-prescribed tenant input (irrelevant); a rented year with an over-long vacancy (13). The "meets the Act's conditions" answer is taken as the conjunction of the three condition outputs.

## Disagreements

### 1. Incentive period starting on 29 February (line 73)
- Code: a period starting 29 February 2012 ends **27 February 2022** (it adds 120 months, which clamps to 28 February 2022, and takes the day before).
- My reading: it ends **28 February 2022**. s 4 says "a 10 year period that starts on" the day; a ten-year period from 29 Feb 2012 has no corresponding day in 2022, and the usual rule for periods with no corresponding day (cf. Acts Interpretation Act 1901 s 2G for months) is that it runs to the end of the last day of that month. The code's period is one day short of ten years, and the day 28 February 2022 falls in no period.
- Confidence: low-medium. The Act gives no leap-day rule; the encoding's choice is defensible but shortens the period. Only leap-day starts are affected; all other starts agreed.

## Coverage gaps

- The encoding has no output saying whether the start date is a valid incentive period (on or after 1 July 2008). A start of 30 June 2008 (scenario P2, expected "not an incentive period") could not be asserted; the code silently computes an end date for it.
- There is no single "the Act's conditions are met this year" output; I combined the three outputs myself.
- s 7(2)(b)/(c) and an NRAS year "that falls within the incentive period": the encoding does not check that the day asked about, or the year being tested, falls inside the incentive period. Not testable.
- s 7(3) (converted buildings) is folded into the "lived in before" input.
- Market value rent is a single number for the year; a market rent that changes during the year cannot be expressed.

## Change after the pass (encoder)

- The disagreement was accepted: a period starting on 29 February ends on 28 February ten years on.
- The gaps are recorded as known limits in NOTES.md.
