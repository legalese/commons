# Encoding brief: the Income Tax (Earnings and Pensions) Act 2003 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Income Tax (Earnings and Pensions) Act 2003** (2003 c. 1), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 15 July 2026, deposited at `../registers/source-bundle/ukpga-2003-1.txt` (Crown copyright, Open Government Licence v3.0).

**Formulas missing from the deposited text.** The conversion drops the formulas that legislation.gov.uk prints as images. Three are needed here; they are taken from the published Act and must be checked against it:

- **s 143(3):** the deduction for unavailability is (U ÷ Y) × A;
- **s 182, step 3:** the interest at the official rate is A × I × (M ÷ 12);
- **s 402D(1):** the post-employment notice pay is ((BP × D) ÷ P) − T.

The table in s 139(1) (cars with a CO2 emissions figure of less than 75) is missing too. It is not supplied, and such cars answer NOTHING.

## Seat

The encoding is written from the seat of **the employee** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the employee's words: *"How much is taxed on me for my company car this year? For my cheap or interest-free loan from my employer? And when my job ends, how much of my termination package is taxed as earnings (post-employment notice pay), and how much of the rest above £30,000?"*

1. **Company car** (ss 120(1), 121(1), 132(3), 133(2)-(3), 139(3)-(4), 141, 143(1)-(3), 144(1)-(3)):
   - the interim sum: the price and accessories, less capital contributions up to £5,000;
   - the appropriate percentage for a car with a CO2 emissions figure of 75 or more (21% plus 1 point per whole 5 g/km above 75, at most 37%), with the diesel supplement of s 141 (plus 4 points, at most 35%);
   - the deduction for days unavailable (before the first day available, after the last, or within a period of 30 days or more when not available);
   - the deduction for payments for private use made by 6 July following the year.
2. **Cheap loans** (ss 175(2)-(3), 180(1)-(2), 182):
   - whether the loan is a taxable cheap loan and the normal £10,000 threshold is exceeded;
   - the interest at the official rate by the averaging method (opening and closing balances; whole months from the 6th);
   - the cash equivalent: that interest less interest actually paid.
3. **Termination payments** (ss 402A-402E, 403(1), (4), 404(4)):
   - the trigger date, the earliest lawful termination date and the post-employment notice period;
   - the post-employment notice pay, including the whole-months and 30.42 cases of s 402D(6)-(6A);
   - the part of the relevant termination awards taxed as earnings under s 402B, and the amount above the £30,000 threshold under s 403.

Left out on purpose: residence and the remittance basis, general earnings, other benefits (vans, fuel, accommodation, vouchers), optional remuneration arrangements, the s 139(1) table, s 140 and s 142, the alternative method in s 183, the exceptions in ss 405-414A, share schemes, pensions and social security income, and PAYE.

## Inputs, not worked out

- Car: the list price and accessories, capital contributions to date, the CO2 emissions figure, whether s 141 applies, the first and last days available in the year, the days in periods of 30 days or more not available, the tax year's days, the payments required and paid for private use and the day paid.
- Loan: the balances at the opening and closing dates, the official rate (or the average rate), the whole months outstanding, the interest paid, the highest aggregate balance in the year, and whether an exception in ss 176-179 applies.
- Termination: whether it is a notice case, the day notice was given, the last day of employment, the minimum notice (in days or whole months), basic pay for the last pay period and its length, whether pay is monthly in equal instalments, the amount T, the relevant termination awards, the redundancy and approved contractual parts, and the earlier payments counted against the threshold.

## Dates, as the Act gives them

- **s 402E(7), "the last day of the period which (a) is equal in length to the minimum notice, and (b) begins at the end of the trigger date"**: the trigger date + notice days; for notice in months, the corresponding date that many months after the trigger date.
- **s 402E(5)-(6)**: the post-employment notice period runs from the day after the last day of employment to the earliest lawful termination date; its days are the difference, and nil if that date is on or before the last day.
- **s 144(1)(b), "on or before 6 July following that year"**: the payment counts only if made by 6 July after the tax year ends.
- **s 182, "a month begins on the sixth day of the calendar month"**: whole months are an input.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"` or NOTHING; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`itepa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
