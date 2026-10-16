# Encoding brief: the Employment Relations Act 2000 (New Zealand), dismissal and personal grievances, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Employment Relations Act 2000**: New Zealand, Public Act 2000 No 24. The source is the version as at 10 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2000_24.txt` (sha256 `af925fc3e0648f8caec8662d03fd04e42b5fd4a28369838b43b5b56fb2e5eb43`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels and two formulas.
- **s 67I(4)** (annual remuneration): its items are the remuneration paid in the pay periods within the 364 days before the pay period of notification, and the days the employee held the position in those 364 days. The encoding reads it as *remuneration × 364 ÷ days held*, so a full year gives the remuneration itself.
- **s 113B(3)** (the threshold increase): its items are the first-quarter average ordinary weekly earnings of the given year and of the year of last increase. The encoding reads it as *(given − last) ÷ last × 100* per cent.

## Scope

- **Trial and probation**: ss 67, 67A, 67B (a trial provision of up to 90 days for a new employee; notice of termination before the trial ends bars an unjustified dismissal grievance).
- **High earners**: ss 67I, 67J, 113A, 113B (annual remuneration of $200,000 or more, as increased, bars an unjustified dismissal grievance unless the parties agreed otherwise in writing).
- **Personal grievances**: s 103(1) (the grounds), s 114 (raising within 90 days, or 12 months for sexual harassment; consent and leave; no action more than 3 years after raising), s 120 (a request for a statement of reasons within 60 days; the statement within 14 days), s 142 (other actions: 6 years).
- **Remedies**: ss 123B, 123C, 124 (contributing behaviour), s 128 (reimbursement: the lesser of the lost remuneration and 3 months' ordinary time remuneration).

The test of justification (s 103A) and the size of remedies are matters for the Authority and are not encoded beyond the limits above.

## The top-level goal, and the goals under it

Top level: *for a dismissed employee's personal grievance: may it be brought at all, was it raised in time, by when must proceedings be commenced, which remedies are available, and what reimbursement must be ordered if it succeeds?*

1. **Trial, probation and high earners**: ss 67-67B, 67I-67J, 113A-113B.
2. **Raising and time limits**: ss 103, 114, 120, 142.
3. **Remedies**: ss 123B-124, 128.

Inputs, not worked out: dates of employment, notices, actions and awareness; the trial provision's terms; remuneration and days held; the threshold in force; consents and leave; findings of contribution and serious misconduct; the percentage reduction; lost remuneration and 3 months' ordinary time remuneration.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`era-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
