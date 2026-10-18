# Encoding brief: the Pensions Act 2014 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Pensions Act 2014** (2014 c. 19), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 29 April 2026, deposited at `../registers/source-bundle/ukpga-2014-19.txt` (Crown copyright, Open Government Licence v3.0).

The conversion drops the formulas. Their printed forms are:

- **s 3(2)**: the reduced rate = (N ÷ 35) × the full rate, where N is the person's number of qualifying years.
- **Sch 1 para 4(4)**: the appropriate proportion = N ÷ 35, where N is the number of pre-commencement qualifying years.
- **Sch 1 para 7(3)**: the proportion = N ÷ 35, where N is the number of post-commencement qualifying years.

The Schedule paragraph numbers are also lost. In Sch 1 they are:

- para 1, introduction;
- para 2, the steps;
- para 3, Step 1;
- para 4, Step 2;
- para 5, contracting out;
- para 6, revaluation;
- para 7, post-commencement years.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for this person, which state pension under Part 1 are they entitled to (none, full, reduced or transitional) and at what weekly rate when they reach pensionable age; by how much is it increased if they defer it; and, if their spouse, civil partner or cohabiting partner has died, are they entitled to bereavement support payment?*

1. **State pension** (ss 1(2), 2, 3, 4, 5(1); Sch 1 paras 2, 4, 6, 7): entitlement and the weekly rate at pensionable age. The amount under the old system (Step 1) and the contracting-out amount (para 5) are inputs.
2. **Deferral** (s 17(1)-(4), (7)): the number of whole weeks deferred between two dates, the increments, and the 1% floor.
3. **Bereavement support payment** (ss 30(1), (5), (6B), 31): entitlement for a single claimant, with the contribution condition. The rates and periods are set by regulations and are out of scope.

Left out on purpose:
- survivor's pensions and inheritance (ss 7-10);
- reduced rate elections (ss 11-12);
- pension sharing (ss 13-15);
- up-rating after pensionable age (Sch 2);
- prisoners and overseas residents (ss 19-20);
- pensionable age itself (s 26 amends a table in the Pensions Act 1995 that the conversion drops, so the day a person reaches pensionable age is an input);
- Parts 2-6 apart from ss 30-31.

## Inputs, not worked out

- The day the person reaches pensionable age, and their numbers of qualifying years (pre- and post-commencement).
- The minimum number of qualifying years (set by regulations).
- The full rate on 6 April 2016 and on the day of pensionable age, the old-system rate, and the contracting-out amount.
- The revaluing percentage for prices (para 6(5)).
- For deferral: the first and last days of the deferral, the weekly rate, and the increment percentage set by regulations.
- For bereavement support: the facts of the death and of the claimant, and the deceased's contribution record (earnings factor and lower earnings limit for each tax year).

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 1(2), "reaches pensionable age before 6 April 2016"**: strictly before.
- **s 4(4)**: a post-commencement qualifying year begins on or after 6 April 2016.
- **s 17(3), "each whole week in the period"**: the number of days in the deferral period, counting both its first and last days, divided by 7 and rounded down.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`pa14-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
