# Encoding brief: the Employment Rights Act 2025 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Employment Rights Act 2025** (2025 c. 36), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 1 July 2026, deposited at `../registers/source-bundle/ukpga-2025-36.txt` (Crown copyright, Open Government Licence v3.0).

Most of the Act amends other Acts. The encoding uses the amended rules as the Act states them:

- **SSCBA 1992 Part 11, as amended by ss 10-11:** statutory sick pay with no waiting days; a weekly rate of the lower of £118.75 and 80% of normal weekly earnings; no lower earnings limit.
- **ERA 1996 s 108, as amended by s 25:** a six-month qualifying period for unfair dismissal, and no cap on the compensatory award (s 124 omitted).
- **ERA 1996 s 27BH, inserted by s 1:** the time limits for guaranteed-hours complaints.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for a worker: what weekly statutory sick pay are they due, and from which day of incapacity; can they complain of unfair dismissal under the six-month qualifying period; and, for a guaranteed-hours complaint, by when must it be presented?*

1. **Statutory sick pay** (ss 10-11, amending SSCBA ss 151-157 and Sch 11):
   - the weekly rate: the lower of £118.75 and 80% of normal weekly earnings;
   - no lower earnings limit;
   - payable from the first qualifying day of a period of incapacity of one day or more (no waiting days; a period of entitlement begins with the first day of incapacity).
2. **Unfair dismissal qualifying period** (s 25, amending ERA 1996 s 108):
   - continuous employment of six months ending with the effective date of termination (one month in a s 64(2) case is unchanged), or none where s 108(3)-(5) applies;
   - the compensatory award is no longer capped.
3. **Guaranteed-hours complaints** (ERA 1996 s 27BH(1)-(8), (10)): the last day to present each kind of complaint under s 27BG, with the s 207B early conciliation extension.

Left out on purpose:
- the guaranteed-hours duty itself, and its reference periods and offers (ss 27BA-27BF, which depend on regulations);
- shifts and payments for cancelled shifts;
- flexible working;
- leave rights;
- harassment;
- fire and rehire;
- collective redundancy;
- outsourcing;
- the Social Care Negotiating Body;
- trade union reforms;
- the Fair Work Agency;
- everything else.

## Inputs, not worked out

- **Statutory sick pay:** normal weekly earnings.
- **Unfair dismissal:** the start of continuous employment, the effective date of termination (as extended by ERA 1996 s 97(2)), and the s 64(2) and s 108(3)-(5) facts.
- **Complaints:** the kind of complaint, its trigger day, and the early conciliation Day A and Day B.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"Six months ending with the effective date of termination"**: the EDT is on or after the last day of the six months beginning with the start of continuous employment.
- **s 27BH: "the period of six months beginning with the day after" day X**: from X + 1 to the day before the corresponding date six months after X + 1, or the last day of that month if it has none. For s 27BH(8), "beginning with the day on which the worker first becomes aware", the period starts on that day.
- **ERA 1996 s 207B(3)-(4)**: the conciliation days from the day after Day A to Day B are not counted, so far as they fall within the period. If the limit would then expire between Day A and one month after Day B, it expires one month after Day B instead.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`era25-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
