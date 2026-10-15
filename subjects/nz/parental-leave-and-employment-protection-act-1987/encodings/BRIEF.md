# Encoding brief: the Parental Leave and Employment Protection Act 1987 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Parental Leave and Employment Protection Act 1987**: New Zealand, Public Act 1987 No 129. The source is the version as at 1 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_1987_129.txt` (sha256 `e1f5f5cefb4890cfa44e2f2d2c27567bbf87852133f1d5d8b2a6ba1c37cc68d1`), converted from the PCO's XML on 2026-10-13 (`act_public_1987_129.meta.json` beside it). There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** The paragraph labels ((a), (b), (i) …) are not in the text; a provision's place in its list gives its label. Repealed sections appear as headings with no text.

What the Act covers:
- **ss 1-7**: purpose, interpretation, multiple employments and children, the 6-month, 12-month and payment threshold tests (s 2BA), comprehensive agreements (s 4), the 6-month gap between children (s 6), and who is the primary carer (s 7).
- **Part 1, ss 8-16**: primary carer leave (up to 26 weeks; when it starts; special leave of 10 days).
- **Part 2, ss 17-22**: partner's leave (1 or 2 weeks; when it starts).
- **Part 3, ss 23-29**: extended leave (26 or 52 weeks less primary carer leave, shared with the spouse or partner, within an end date).
- **Part 3A, ss 30A-30J**: negotiated carer leave requests.
- **Parts 4-7, ss 31-71**: notices, keeping the position open, holiday pay after leave, ending or extending leave, protection from dismissal and its defences, complaints and their time limits, irregularities, Labour Inspectors.
- **Part 7A, ss 71A-71ZB**: parental leave payments (eligibility, average weekly income, the weekly rate and its cap, start and end, preterm baby payments, keeping-in-touch days, transfer, applications, overpayments, offences, review).
- **Part 8 and Schedules**: succession on death, s 72A counting hours, transitional provisions (Schedule 1AA), and change of employer (Schedule 1).

## The top-level goal, and the goals under it

Top level: *for this person and this child, which leave may the person take and for how long, are they entitled to parental leave payments, at what weekly rate, for how many weeks (with any preterm baby payments), and by when must they apply?*

1. **Eligibility**: ss 2, 2B, 2BA, 4-7, 72A.
2. **Leave**: Parts 1-3A.
3. **Notices, the position, and protection**: Parts 4-7.
4. **Parental leave payments**: Part 7A and ss 72B-72C.

Inputs, not worked out:
- who is an employee (ERA s 6), a self-employed person, a spouse or partner;
- the average weekly hours with the same employer over the 6 and 12 months (after s 72A), and each week's hours and earnings in the 52 weeks;
- ordinary weekly pay (Holidays Act 2003, s 8) and net income from self-employment;
- the maximum weekly rate in force (s 71M as adjusted under s 71N) and the minimum wage, since both change each 1 July;
- the date on which the 36th week of gestation would have ended;
- agreements, consents, employer decisions and Labour Inspector determinations.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`pl-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
