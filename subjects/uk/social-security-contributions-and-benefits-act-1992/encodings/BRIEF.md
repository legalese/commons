# Encoding brief: the Social Security Contributions and Benefits Act 1992 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Social Security Contributions and Benefits Act 1992** (1992 c. 4), Great Britain. The source is the revised text on legislation.gov.uk, point in time 8 July 2026, deposited at `../registers/source-bundle/ukpga-1992-4.txt` (Crown copyright, Open Government Licence v3.0). In this version:

- the main primary percentage is 8%, the additional primary percentage 2%, and the secondary percentage 15%;
- the weekly rate of statutory sick pay is the lower of £123.25 and 80% of normal weekly earnings (s 157(1));
- statutory sick pay has no waiting days.

The age-related secondary percentage table in s 9A(3) is lost in the conversion, so the secondary percentage that applies is an input.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for an employee: what Class 1 contributions are due on a week's earnings; what statutory sick pay is due for a day and in total; and is she entitled to statutory maternity pay, from when, and at what weekly rates?*

1. **Class 1 contributions** (ss 8(1)-(2), 9(1)-(2)):
   - primary: 8% of earnings above the primary threshold up to the upper earnings limit, plus 2% above the upper earnings limit;
   - secondary: the relevant percentage of earnings above the secondary threshold.

   The thresholds are inputs, as weekly amounts or prescribed equivalents.
2. **Statutory sick pay** (ss 152(2)-(3), 155(2)-(4), 157(1), (3)):
   - the weekly rate;
   - the amount for one day (the weekly rate divided by the qualifying days in that week);
   - the entitlement limit (28 × the weekly rate);
   - whether two periods of incapacity link (separated by not more than 8 weeks).
3. **Statutory maternity pay** (ss 164(2), 165(1)-(2), (8), 166(1)-(2), 171(1A)):
   - the expected week of confinement (the week, beginning with Sunday, containing the expected date);
   - the qualifying conditions: 26 weeks' continuous employment ending with the week before the 14th week before the expected week, normal weekly earnings not less than the lower earnings limit, and having reached the 11th week before;
   - the earliest start of the maternity pay period (the start of the 11th week before);
   - the weekly rate for the first 6 weeks (90% of normal weekly earnings) and for the rest (the lower of 90% and the prescribed rate, an input).

Left out on purpose:
- Classes 2, 3 and 4;
- the contributory benefits;
- non-contributory benefits;
- industrial injuries;
- income-related benefits;
- SSP and SMP recovery and supplementary provisions;
- statutory paternity, adoption, shared parental, bereavement and neonatal pay;
- everything else.

## Inputs, not worked out

- **Contributions:** the earnings in the week, the thresholds and limits, and the secondary percentage.
- **Statutory sick pay:** normal weekly earnings, the qualifying days in the week, and the days and dates of periods of incapacity.
- **Statutory maternity pay:** the expected date of confinement, the start of continuous employment, normal weekly earnings, the lower earnings limit, the prescribed weekly rate, and the date in question.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 171(1A): "week" means seven days beginning with Sunday.** The expected week of confinement is the Sunday-to-Saturday week containing the expected date.
- **"The Nth week before the expected week of confinement"**: the week beginning N × 7 days before the Sunday that starts the expected week.
- **"A continuous period of at least 26 weeks ending with the week immediately preceding the 14th week before"**, which is the 15th week before: employment began on or before the Sunday 25 weeks before that 15th week begins.
- **s 152(3): "separated by a period of not more than 8 weeks"**: the gap between the periods, counting the days between them, is at most 56 days.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`sscba-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
