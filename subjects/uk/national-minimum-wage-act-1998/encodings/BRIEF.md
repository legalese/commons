# Encoding brief: the National Minimum Wage Act 1998 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**National Minimum Wage Act 1998** (1998 c. 39), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 7 April 2026, deposited at `../registers/source-bundle/ukpga-1998-39.txt` (converted from the CLML XML; `ukpga-1998-39.meta.json` records the hashes). Crown copyright, Open Government Licence v3.0.

In that version, ss 13-16 and 19-22F (officers, notices of underpayment, penalty notices) are shown as repealed: they print as dots. The encoding follows the text as deposited and does not encode them.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for this individual and this work, do they qualify for the national minimum wage; for the pay reference periods in which they were paid less than it, how much additional remuneration are they entitled to at the time of determination; and, if they asked to see their employer's records, by when must the records be produced, by when must a complaint be presented, and what does the tribunal award?*

1. **Who qualifies**: ss 1(1)-(2), 28(1) (the presumption), 34 (agency workers), 35 (home workers), 37, 37A, 40 (mariners), 43, 44, 44A, 45, 45A, 45B, and 54(3) (worker). Section 3 regulations that prevent a person from qualifying are an input.
2. **Arrears (s 17)**: the higher of (a) the shortfall A and (b) A ÷ R1 × R2, reduced by the additional remuneration already paid, and nothing more once it has been paid in full (s 17(5)-(6)). The conversion loses the formula in s 17(4). Its printed form is A/R1 × R2, with A, R1 and R2 as defined in that subsection.
3. **Access to records (ss 10, 11, 11A)**:
   - the last day for production (s 10(9));
   - the last day to present a s 11 complaint, including the extension for early conciliation (s 11A);
   - the award of 80 times the hourly rate in force when the award is made (s 11(2)).

Left out on purpose: the Low Pay Commission (ss 5-8), the regulation-making powers (ss 2-4, 9, 12, 41, 42, 47, 51), detriment and dismissal (ss 23-26, which apply the Employment Rights Act 1996), offences (ss 31-33), agricultural workers (ss 46-47), contracting out (s 49), and the supplementary sections (ss 50-53, 55-56).

## Inputs, not worked out

- **The rates and hours.** The national minimum wage rate (s 1(3)) and the rate for each age band under s 3 regulations, both in each pay reference period and at the time of determination. The hours, and the remuneration that counts, are worked out under the s 2 regulations.
- **Status facts.** Whether a contract is a worker's contract within s 54(3), and the other facts each exclusion needs.
- **Conciliation dates.** For s 11A, Day A (the worker contacts ACAS) and Day B (the worker receives the certificate).

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule, so do not move any date. Read the periods as follows:

- **"Before the end of the period of fourteen days following the date of receipt"**: the period starts the day after receipt, so the last day is receipt + 14.
- **"The period of three months following" a day**: the corresponding date three months later, or the last day of that month if it has no corresponding date.
- **"One month after Day B"**: the same corresponding-date rule.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`nmw-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
