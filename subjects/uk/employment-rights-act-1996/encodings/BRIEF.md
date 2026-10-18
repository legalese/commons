# Encoding brief: the Employment Rights Act 1996 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Employment Rights Act 1996** (1996 c. 18), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 29 July 2026, deposited at `../registers/source-bundle/ukpga-1996-18.txt` (converted from the CLML XML; `ukpga-1996-18.meta.json` records the hashes). Crown copyright, Open Government Licence v3.0. In this version s 108(1) still requires two years, s 120(1) gives £9,157 and s 227(1) caps a week's pay at £751; the encoding uses the text as deposited.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *an employee's contract has ended. What notice did the Act require, can they complain of unfair dismissal and by when, what is the basic award, and are they entitled to a statutory redundancy payment and how much?*

1. **Minimum notice** (ss 86(1)-(2), 211(1)): the weeks of notice the employer must give and the employee must give, from the length of continuous employment on the day notice is given, and the earliest day the employer's statutory notice can expire.
2. **Unfair dismissal** (ss 95(1) as an input, 97(1)-(5), 108(1)-(5), 111(2), (2A), 119, 120(1), (1C), 121, 122, 207B, 227(1)):
   - whether the qualifying period is met (two years ending with the effective date of termination, extended by s 97(2)/(4); one month in a s 64(2) case; none where s 108(3)-(5) applies);
   - the last day to present a complaint (three months beginning with the effective date of termination, extended for early conciliation by s 207B);
   - the basic award, if the dismissal is found unfair.
3. **Redundancy payment** (ss 135(1)(a), 136(1), 139 as an input, 140, 141, 145, 155, 162, 163(2), 164, 207B, 227(1)): whether the employee is entitled, and the amount.

Left out on purpose: written particulars (Part I), protection of wages (Part II), guarantee payments, Sunday working, detriment, leave rights (Parts IVA-VIII), the fairness test of s 98 (an input: the tribunal's finding), the compensatory award (s 123: "just and equitable", no computation), lay-off and short-time (ss 147-154), the rules on continuity in ss 212-219 (the start of continuous employment is an input, already adjusted), and a week's pay under ss 221-229 except the s 227 cap (the week's pay is an input).

## Inputs, not worked out

- The employee's date of birth, the day continuous employment began (s 211(1)(a), after any s 211(3) postponement), and a week's pay (Chapter II of Part XIV, before the s 227 cap).
- How the contract ended (by the employer, by the employee in circumstances entitling them to terminate without notice, by the employee otherwise, or a limited-term contract expiring), the day notice was given (if any), and the day the termination took effect or the notice expired.
- Tribunal findings: the dismissal unfair; the reason for dismissal (redundancy, a s 120(1) reason, s 104F); a s 108(3)-(5) reason; s 140/141 exclusions; just and equitable reductions; late complaints allowed.
- Early conciliation Day A and Day B (s 207B).

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule, so do not move any date.

- **"A period of N months/years beginning with" day X**: ends on the day before the corresponding date N months later, or, if that month has no corresponding date, on the last day of that month.
- **"Continuously employed for a period of not less than two years ending with" day E**: the period from the start of continuous employment to E (both included) is at least two years, i.e. E is on or after the last day of the two years beginning with the start.
- **Notice of N weeks given on day d** expires at the end of day d + 7N (the notice runs from the day after it is given).
- **s 207B(3)-(4)**: leave out the days from the day after Day A to Day B; then, if the limit would expire between Day A and one month after Day B (the corresponding date), it expires one month after Day B.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`era-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
