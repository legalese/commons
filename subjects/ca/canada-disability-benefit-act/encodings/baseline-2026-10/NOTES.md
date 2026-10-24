# Canada Disability Benefit Act: baseline encoding for the person applying for the benefit

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A person who is not eligible gets an explicit answer naming the condition not met, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The Act is a framework. Section 4 makes a person eligible "if they meet the eligibility criteria set out in the regulations", and s 5 obliges the Minister to pay "in accordance with the regulations". So the rules encoded are the Regulations', read through the Act.

It is written in two layers:

- **`cdb-core.l4`**, the seat-neutral core, in the instruments' own actors and terms ("the applicant", "the beneficiary", "the cohabiting spouse or common-law partner", "the Minister"). Eligibility, the indexing factor, the reduction based on income, the basic amount, the supplemental amount and the start month are functions. Where the text says "must" or sets a period, there is a regulative rule (`DEONTIC`): five in all.
- **`cdb-seat.l4`**, the applicant's seat: 5 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings (eligibility; amount). It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed. No requirement ledger covers Canada, so no ledger line is closed.

## Edition

- **Act:** Canada Disability Benefit Act, S.C. 2023, c. 17, Justice Laws consolidation **current to 2026-09-30**, last amended 2024-06-22, deposited at `../../registers/source-bundle/S.C.-2023-c.-17.txt` (from justicecanada/laws-lois-xml commit `0507465393c2`).
- **Regulations:** Canada Disability Benefit Regulations, SOR/2025-35, same consolidation, last amended 2026-09-01 (a related provision of SOR/2026-123 bears on the supplemental amount), at `../../registers/source-bundle/SOR-2025-35.txt`.
- **Figures.** The Regulations fix every amount ($2,400 a year, the $23,000 and $32,500 thresholds, the $10,000 and $14,000 working-income exemptions, 20% and 10%, $150) and index them by `CPImax / CPI2024` (s 6(5)). **For the payment period beginning July 2025 the factor is exactly 1**, because 2024 is the only year in the range, so that period needs no outside figure. For later periods the two annual Consumer Price Index figures are inputs (Statistics Canada; not deposited). The case file's later-period CPI figures are **hypothetical** and say so.

Unofficial reproduction; not an official version. Contains information licensed under the Open Government Licence - Canada.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cdb-core.l4`, `cdb-seat.l4` | `cdb-cases-applicant.l4` | 44 written, 44 satisfied |

In addition, 2 `#TRACE`s carry an `-- expect:` line: both are obligations still pending (the applicant's, and the Minister's). Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The person with a disability applying for, or receiving, the Canada disability benefit** (or their representative, Regulations s 15). They ask: "Am I eligible this month?", "How much a month, after the income reduction?", "Is it paid as a lump sum?", "Do I get the $150 supplement?", "From when is it paid?".

The Minister's duties (to pay, s 5; to reconsider "within a reasonable time", Regulations s 18(4); to allow an extension in listed situations, s 19(3)) are encoded for what the person is owed: the regulative rules on reconsideration and its extension carry the Minister's duty as the HENCE branch.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers**: here the Regulations are most of the law.
- **The actors the text names:** the applicant or beneficiary and the Minister. The estate's duty to notify a death (Regulations s 12) is not the individual's and is out.
- **Judgments left to others are answered conditionally, as inputs:** the Minister's waiver of the spouse's filing condition (s 2(5), "if the Minister is satisfied"), the Minister's requirement of information (Act s 6).
- **The Regulations' own definitions are worked out from facts:** "payment period", the indexing factor, the reduction for each household, the basic amount. Borrowed terms are asked as facts: "DTC-eligible individual" (ITA s 146.4(1)), "cohabiting spouse or common-law partner" and "adjusted income" (ITA s 122.6), "working income" (ITA s 122.7(1), with the listed business incomes), residence for the Income Tax Act, and immigration status.
- **One case:** one person and one month (within one payment period).
- **The instruments' own terms**, quoted in the comment above each rule.
- **Machinery out:** agreements (Act s 8), the regulation-making power and its consultation duties (ss 11-11.2), parliamentary review, the Tax Court references (Regulations ss 21-29), inspections and penalties (ss 32-36), debt recovery machinery (ss 38-40).

## Scope

**In:**

- Act ss 4, 5, 6
- Regulations s 1; s 2(1)-(6) (eligibility); ss 2.1, 6.1, 9.1 (the supplemental amount); s 5 (approval date and the 24-month limit); s 6(1)-(7) (the basic amount, the three reductions, the waiver rule, the indexing factor); s 7 (first month); s 8(2) (lump sum); s 11(3); ss 18-19 (reconsideration and extension); s 37(1)
- Duties: Act s 6; Regulations ss 11(3), 18, 19(1), 37(1), as regulative rules

**Out:**

- the first payment's arrears (s 9) and monthly payment mechanics (s 8(1)); suspension by the Minister (s 10); applications before 18 (s 4(3)) and new applications (s 4(4))
- death of a beneficiary and presumption of death (ss 12-14), representatives (ss 15-16), administrative errors (s 31)
- appeals to the Social Security Tribunal (Act s 10.1; Regulations ss 20-29), compliance, penalties and offences (ss 32-36), recovery (ss 37(2)-40)

## Read with the Income Tax Act encoding

`../../../income-tax-act/encodings/baseline-2026-10/` (being encoded on 2026-10-24 by another session) answers every borrowed term this encoding asks as a fact:

- **"DTC-eligible individual"** (ITA s 146.4(1)): a person for whom a disability tax credit certificate under ITA s 118.3 has been filed and accepted; the supplemental amount turns on certificates under s 118.3(1)(a.2) and (a.3).
- **"adjusted income"** and **"cohabiting spouse or common-law partner"** (ITA s 122.6, the Canada child benefit definitions): the reduction is computed on adjusted family income, as the Canada child benefit is.
- **"working income"** (ITA s 122.7(1), the Canada workers benefit definition, paragraphs (a) and (b)).
- **Filing a return of income** for the last taxation year before the payment period (s 2(1)(e), (4)) is an ITA s 150 return.

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

## What the Regulations turn out to say

1. **"Not more than 65 years of age" would cover the whole year of age 65, but s 2(2) assumes it stops at 65.** Section 2(1)(a) admits a person "at least 18 years of age but not more than 65 years of age"; a person is 65 years of age until the 66th birthday. Yet s 2(2) adds, "Despite paragraph (1)(a)", eligibility "for the month in which they turn 65", which would be needless on the literal reading. The encoding reads (1)(a) as under 65, so that s 2(2) does the work its "despite" says it does: eligible through the month of the 65th birthday, not after. That is a reading; the literal one would pay a year longer. Asserted.
2. **The first payment period needs no index.** For July 2025 to June 2026, `CPImax / CPI2024` is CPI2024 over itself, 1. Every figure is then the Regulations' own: $200 a month at most. Asserted.
3. **The benefit runs out at modest incomes, and the Regulations do not say what a negative amount means.** The reduction is floored at zero (s 6(2)-(4), "the greater of zero and"), but the basic amount `((2,400 x A) - B) / 12` is not. A single person with $45,000 of non-working income has a reduction of $4,400, more than the $2,400; the encoding pays nothing rather than a negative amount (a reading). A single person with no working income receives nothing from $35,000 of adjusted income; with at least $10,000 of working income, from $45,000. Asserted.
4. **Two beneficiaries living together each have the reduction halved.** Where the spouse is also a beneficiary, the rate is 10% instead of 20% (s 6(4)), applied to the same family income: $350 instead of $700 at $50,000, so $170.83 a month instead of $141.67. Asserted.
5. **A single person's income excludes a spouse's; a couple's is the family's.** For a person with no cohabiting spouse, C is adjusted income "without taking into account the income" of a spouse at the end of the year (s 6(2)); otherwise E is adjusted income, which under ITA s 122.6 is the couple's. Where the Minister waives the spouse's filing condition, the single formula applies (s 6(4.1)): a beneficiary separated from a violent spouse is assessed on their own income. Asserted.
6. **A cohabiting spouse who does not file blocks the benefit.** Section 2(4) makes eligibility for any month depend on the spouse's return for the last taxation year, "despite" every other criterion, unless the Minister waives it (s 2(5)). Asserted.
7. **$20 a month or less is paid in one sum for the rest of the period** (s 8(2)): $16.67 a month is paid as a lump sum. Asserted.
8. **The benefit can reach back at most 23 months before the application month.** The application is deemed approved on the earliest day of eligibility, but not more than 24 months before it is made (s 5), and the allocation starts with the month after approval (s 7). Asserted. The 24 months are read in months.
9. **Reconsideration has 180 days, and an extension must be allowed for listed hardships.** Section 18(1) gives 180 days from the written notice (against 30 days under the Employment Insurance Act and 90 under the Old Age Security Act and the Canada Pension Plan); s 19 lets the person ask for more time up to 185 days after that, and the Minister "must allow" it for an emergency, disaster, civil disturbance, public-service disruption, serious accident or illness, or emotional or mental distress. The Minister's own duty runs "within a reasonable time", which sets no number of days: the trace stays pending.
10. **The $150 supplemental amount is not indexed and is paid once per qualifying certificate** (ss 2.1, 6.1, 9.1): the certificate must be one under ITA s 118.3(1)(a.2) or (a.3), an allocation must be paid after it is obtained, and the person's DTC status at that payment must rest on it. Asserted.

## Before relying on it

- Deposit Statistics Canada's annual CPI for 2024 and 2025 and encode the indexing factor for the period beginning July 2026 as a dated figure.
- Confirm finding 1 (the age-65 reading) against ESDC practice.
- Encode the arrears of the first payment (s 9), suspension by the Minister (s 10) and the death rules (ss 12-13).
- An independent test pass against ESDC's published benefit estimator.
