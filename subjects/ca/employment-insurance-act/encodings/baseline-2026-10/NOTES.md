# Employment Insurance Act: baseline encoding for the insured person claiming regular benefits

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit value (hours below Schedule I answer `no regular benefits: I do not qualify`), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`ei-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the insured person", "the claimant", "the Commission"). The tables of ss 7(2), 7.1(1) and 14(2) and the whole of **Schedule I** are written in as data; Schedule I was transcribed from the deposited text by a script (41 rows of 12 entries), not retyped. Qualification, weeks, rate, disqualification, premium and benefit repayment are functions. Where the text says "shall" or sets a period, there is a regulative rule (`DEONTIC`): four in all.
- **`ei-seat.l4`**, the claimant's seat: 8 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings (qualifying and how long and how much, both marked as the situation of having lost a job; premium; benefit repayment, marked as the situation of a higher-income year). It builds the answers from plain inputs and restates no rule.

No earlier encoding of this Act existed. No requirement ledger covers Canada, so no ledger line is closed.

## Edition

- **Act:** Employment Insurance Act, S.C. 1996, c. 23, Justice Laws consolidation **current to 2026-09-30**, last amended 2026-06-18, deposited at `../../registers/source-bundle/S.C.-1996-c.-23.txt` (from justicecanada/laws-lois-xml commit `0507465393c2`). The Part VIII.5-VIII.6 temporary measures have expired and are not encoded; the amendments not in force (2026, c. 22, s. 38, on s 12(2.3)) touch only the seasonal-worker rule, which is out.
- **Regulations:** Employment Insurance Regulations, SOR/96-332, same consolidation, last amended 2026-04-01, at `../../registers/source-bundle/SOR-96-332.txt`. Used for the regional rate (s 17, as a fact) and the time for claims (s 26).
- **Figures are inputs:** the maximum yearly insurable earnings (s 4, indexed each year to Statistics Canada's Average Weekly Earnings), the premium rate (s 66, set each year by the Commission) and the regional rate of unemployment (Regulations s 17, the three-month average for the claimant's economic region). None is deposited. The case file uses **hypothetical** values and says so.

Unofficial reproduction; not an official version. Contains information licensed under the Open Government Licence - Canada.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ei-core.l4`, `ei-seat.l4` | `ei-cases-claimant.l4` | 49 written, 49 satisfied |

In addition, 4 `#TRACE`s carry an `-- expect:` line: three breaches by the claimant and one obligation of the Commission still pending. Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text and its tables, with the arithmetic in the comment above the assertion.

## Seat

**The insured person**: the employee who pays premiums and, having lost or left a job, claims regular benefits. They ask: "How many hours do I need?", "Do I qualify?", "Am I disqualified because of how my job ended?", "For how many weeks, and how much a week?", "What premium do I pay?", "Must I repay benefits at tax time?".

The Act's decisions are the Commission's. They are encoded for what they mean to the claimant: the findings of misconduct and of "no reasonable alternative to leaving" are asked as facts (the Commission gives the benefit of the doubt where the evidence is balanced, s 49(2)); the claimant's duty to claim each week, to repay and to return overpayments are regulative rules; and the reconsideration the claimant may ask for carries the Commission's duty to reconsider (s 112(2)). The employer (premiums at 1.4 times, s 68; the Record of Employment) is not given a seat.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers**: the Regulations for the regional rate and the time for claims. The annual figures are inputs.
- **The actors the text names:** the claimant and the Commission.
- **Judgments left to others are answered conditionally, as inputs:** misconduct; just cause (s 29(c), "no reasonable alternative ... having regard to all the circumstances"); the kind of violation (from the notice of violation, s 7.1(4)-(5)); the hours and earnings (the Records of Employment).
- **The Act's own definitions are worked out from facts:** the hours required, the weeks, the calculation period and weekly insurable earnings, the rate and its maximum, the disqualification, the hours usable after it, the benefit repayment. Borrowed terms are asked as facts: income under the Income Tax Act (s 144).
- **One case:** one claimant and one benefit period (or one taxation year, for Part VII).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Commission, the Operating Account and the premium-rate setting (ss 66-66.6, 70.2-80.1), employment support measures (Part II), employers' collection duties (Part IV), offences, the Social Security Tribunal.

## Scope

**In:**

- s 6(1) "major attachment claimant"; s 6(2) rounding
- s 7(2) and s 7.1(1) (qualifying hours, with violations)
- s 12(2) and Schedule I (weeks of regular benefits); s 13 (the one-week waiting period, as a constant and in the answers' wording)
- s 14(1)-(2), (4) and s 17 (the rate of weekly benefits)
- s 29(b)-(c), s 30(1)-(2), (5)-(6) (disqualification for misconduct or leaving without just cause, and the hours that may then be used)
- s 67 with s 82(2) (the employee's premium, one employer)
- Part VII: s 144 "income" (as a fact), s 145(1)-(2) (benefit repayment)
- Duties: s 50(4) with Regulations s 26; s 145(4) with s 146; s 44; s 112(1)-(2), as regulative rules

**Out:**

- special benefits (maternity, parental, sickness, compassionate care, critically ill family members: ss 12(3)-(7), 22-23.3), the 33% extended parental rate, work-sharing (s 24), the family supplement (s 16)
- the s 12(2.3) seasonal-worker table (Schedule V), the benefit period's length and extensions (s 10(2), (10)-(15)), late and antedated claims (s 10(4)-(5)), the extension of the qualifying period (s 8(2)-(7)): the hours in the qualifying period are a fact
- disentitlement (ss 18, 21, 31-33, 36-37: availability, suspension, leave, labour disputes, prison, being outside Canada), and the s 30(3), (7) rules for an event during a benefit period
- earnings while on claim (s 19), allocation of separation monies (Regulations ss 35-36), the calculation-period regulations
- self-employed persons (Part VII.1) and fishers (Part VIII), the premium reduction for wage-loss plans (s 69), refunds of premium overpayments (s 96)
- penalties and violations' values (ss 38-41.1, 7.1(5)-(6)), recovery (ss 43-47)

## Read with the Income Tax Act encoding

`../../../income-tax-act/encodings/baseline-2026-10/` (being encoded on 2026-10-24 by another session) answers this encoding's borrowed terms and uses its answers:

- **"income" for Part VII** (s 144) is income under the Income Tax Act without the deductions under ITA 60(v.1), (w), (y), (z) and without the s 79 gain and the 56(1)(q.1)/56(6) amounts.
- **The benefit repayment** is collected with the income tax return (s 146, s 149 applying ITA provisions); the repayment is itself deductible under ITA 60(v.1), and EI benefits are income under ITA 56(1)(a)(iv).
- **EI premiums** give the employee a credit under ITA s 118.7.

Also read with `../../../old-age-security-act/encodings/baseline-2026-10/` (EI premiums are deducted from income for the GIS, OAS Act s 2(a)(ii)). The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

## What the Act turns out to say

1. **Schedule I is a two-way table with blanks, and its blanks are the qualifying rule.** Below the hours s 7(2) requires at a given regional rate, the Schedule I cell is empty: 420 hours give 26 weeks at 13.5% and nothing at 5%. The weeks rise by two for each point of the regional rate and, above 700 hours, by one for each 70 hours (then each 35 hours from 1,435), to a cap of 45. Asserted at several cells.
2. **Qualifying hours fall by 35 for each point of the regional rate, from 700 to 420.** Section 7(2). A violation raises them (s 7.1(1)), to as much as 1,400 for a subsequent violation where unemployment is 6% or under. Asserted.
3. **The weekly rate divides by a fixed number of weeks, whether or not the claimant worked that many.** Section 14(2) divides the earnings of the best weeks by "the number of weeks determined in accordance with the following table" (22 at 6% or under, down to 14 above 13%). A claimant with ten weeks of $1,500 where unemployment is 5% has $15,000 divided by 22: a weekly rate of $375, not $825. The table also shortens the divisor where unemployment is high. Asserted.
4. **Rounding is to the dollar, half up.** Section 6(2) rounds "an amount equal to a percentage or fraction of earnings or benefits". The encoding rounds the weekly insurable earnings (a fraction of earnings) and the rate (a percentage): $750.50 becomes $751, and 55% of it, $413.05, becomes $413. The rounding of weekly insurable earnings is a reading. The s 17 maximum is rounded the same way. Asserted.
5. **For an initial claim, being dismissed for misconduct or quitting without just cause is decided by the hours.** Section 30(5) bars using hours "before the employment was lost or left" to qualify, and s 30(1)(a) lifts the disqualification once the claimant has had, since then, the hours s 7 requires. On an initial claim the two tests are the same number. So the claimant either qualifies on the later hours and is not disqualified, or does not qualify at all. The disqualification "for each week of the claimant's benefit period following the waiting period" (s 30(2)) bites in practice when the event happens during a benefit period (s 30(3), (7)), which is not encoded. Asserted (the 300-hour and 800-hour cases).
6. **The benefit repayment reaches only regular benefits, and spares a first-time claimant.** Section 145(1) takes 30% of the lesser of regular benefits and income over 1.25 times the maximum yearly insurable earnings; special benefits are excluded, and s 145(2) excuses a claimant paid regular benefits for less than a week in the previous ten years. Asserted.
7. **A week must be claimed within three weeks, or within one week after a gap of four or more.** Regulations s 26. A claim out of time is not paid (s 50(1)) unless antedated for good cause (s 10(5), not encoded). The rule's breach is that consequence. Asserted by `#TRACE`.
8. **The premium stops at the maximum for each employer, not for the person.** Section 82(2) bars a deduction once "the insurable earnings paid by the employer" reach the maximum; a person with two employers can overpay and is refunded under s 96 (not encoded). The encoding assumes one employer. Asserted.
9. **Reconsideration must be asked within 30 days** (s 112(1)), against 90 days under the Old Age Security Act (s 27.1) and the Canada Pension Plan (s 81). The Commission "must reconsider" with no period: the trace stays pending. "Without delay" in s 44 likewise sets no period.
10. **30 April is taken as day 120 of the following year** for the s 145(4)(b) deadline, counting from 31 December (not a leap year): a reading of the clock, not of the law.

## Before relying on it

- Deposit the year's maximum yearly insurable earnings, premium rate and regional rates (ESDC and the Commission publish them; the regional rates change monthly) and encode them as dated tables.
- Encode disentitlement (ss 18, 31-33, 36-37), earnings during a claim (s 19) and the allocation of separation monies, which decide how much of the maximum is actually paid; and special benefits.
- An independent test pass against Service Canada's published decisions and the Social Security Tribunal's case law on misconduct and just cause.
