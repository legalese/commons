# Income Tax Rates Act 1986 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 66, compilation date 1 July 2026, includes amendments
up to Act No. 50, 2026 (register id C2026C00300), as deposited at
`../../registers/source-bundle/C2004A03348.txt`.

**Checks:** one case file (`itra-cases-rates.l4`), 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0019** (priority 1), raised 3 times by the Western
Australian cradle-to-grave lives:

- **chloe c045** (2024-10-20). Her first tax return, for 2023-24, on taxable income of $27,500. The scenario expects nil tax.
- **chloe c048** (2025-10-25). Her second return, for 2024-25, on taxable income of $71,500. The scenario expects tax before offsets of $12,842.
- **daniel d04a** (2033-11-30). The first company return of Jarrah Legal Technologies Pty Ltd: "What rate?"

The encoding covers the provisions those events cite: Schedule 7 and s 23 (the
base rate entity). It adds what changes a Schedule 7 answer:

- the s 3 definitions (tax-free threshold, prescribed non-resident, resident
  taxpayer, ordinary taxable income);
- the superannuation and employment termination remainders, taxed at 45%;
- the working holiday maker rules (clause 4 of Parts I and II, and Part III);
- part-year residency (ss 16, 18 and 20(1));
- s 23(6), the ceiling on tax for a non-profit company.

**Not encoded:**

- the abnormal-income averaging in Schedule 7 clauses 2 and 3;
- trustees and minors (ss 12(4)–(13), 13–15);
- primary producers (s 12A);
- Schedules 8 to 12;
- RSA providers, PDFs, credit unions, life insurers, super funds and sovereign entities (s 23(3)–(5), (7), 23A, 25–30);
- s 23AB's list of passive income, which is an input here.

The low income tax offset, the Medicare levy and HELP repayments come from other
Acts. The loss carry-forward d04a also asks about is in the Income Tax Assessment Act 1997.

## What the Act turns out to say

### 1. The deposited compilation has no rates for 2023-24, the year c045 asks about

Schedule 7 Part I has three tables:

- "for the 2024-25 or 2025-26 year of income";
- "for the 2026-27 year of income";
- "for the 2027-28 year of income or a later year of income".

Nothing covers 2023-24 or earlier. So this compilation cannot answer Chloe's first
return. The encoding returns `NOTHING` for it. The scenario's answer of nil tax
also relies on the low income tax offset, which is outside this Act.

For comparison only: the 2024-25 table would put tax on $27,500 at $1,488 before
offsets. Asserted.

### 2. Chloe's 2024-25 tax before offsets comes to $12,238, not the scenario's $12,842

On $71,500 for 2024-25:

- 16% of $26,800 (from $18,200 to $45,000) is $4,288.
- 30% of $26,500 (from $45,000 to $71,500) is $7,950.
- The total is **$12,238**.

c048 records `tax_before_offsets: 12842`, a difference of $604. Nothing in the
deposited text produces $12,842. Asserted (12,238).

### 3. The first resident rate falls each year: 16%, then 15%, then 14%

The band from the threshold to $45,000 is taxed at:

- 16% for 2024-25 and 2025-26;
- 15% for 2026-27;
- 14% for 2027-28 and later years.

The other bands do not change: 30% to $135,000, 37% to $190,000, 45% above. On
$71,500 the tax is $12,238, then $11,970, then $11,702. Asserted.

### 4. A resident working holiday maker gets no tax-free threshold on visa income

Clause 4 counts working holiday taxable income "as the first parts (starting from
$0)" of ordinary taxable income, and the clause 1 table does not apply to it.
Part III taxes it at 15% from the first dollar, up to $45,000.

So a resident working holiday maker earning $30,000 on the visa pays $4,500. A
resident without the visa pays $1,888 on the same income. Only the income above the
visa income goes through the resident table. Asserted.

### 5. A non-resident all year can still be a "resident taxpayer" for the rates

A "prescribed non-resident" excludes anyone paid an assessable payment in the year
under the Veterans' Entitlements Act, the MRCA or the Social Security Act. Such a
person is a "resident taxpayer" under s 3 and gets the resident table, threshold
included: $1,888 on $30,000, against $9,000 at the non-resident rates. Asserted.

### 6. A base rate entity pays 25%, and both limits are strict

Under s 23(2), a base rate entity pays 25% and any other company pays 30%. Section
23AA sets two tests:

- passive income must be "no more than 80%" of assessable income, so exactly 80% qualifies;
- aggregated turnover must be "less than $50 million", so exactly $50 million does not.

Jarrah, with turnover under $3 million and trading income, is a base rate entity at
25%. In a loss year its taxable income is nil and so is its tax. Asserted.

The scenario does not give Jarrah's figures. The fixtures assume them.

### 7. A non-profit company's tax is capped at 55% of income over $416

Section 23(6) applies to non-profit companies with taxable income up to $762 (a
base rate entity) or $915 (any other company). Their tax is capped at 55% of the
excess over $416:

- nil tax on $416;
- $101.20 on $600 for a base rate entity, against $150 at 25%;
- no cap on $800 for a base rate entity, which pays $200.

Asserted.

### 8. The deposit drops the formulas

Every formula set as an image is missing. The words that introduce each one ("the
following formula:", "using the formula:", "the formula , where") are followed by
nothing. This affects:

- s 20(1), the pro-rated tax-free threshold for part-year residents;
- Schedule 7 clauses 2 and 3;
- ss 12(7), 12AA and 12A.

The pro-rated threshold is therefore an input. The October 2024 arrival case uses
an assumed $13,650. The encoding does apply s 18(2): an eligible pensioner has no
part-year residency period and keeps the full $18,200. Asserted.

## What would need doing before this is worth anything

- Retrieve the s 20 formula and the clause 2 and 3 formulas from the PDF or Word
  original, and encode them.
- Retrieve the 2023-24 rates from an earlier compilation, so that c045 can be
  answered. The endnotes would name the amending Act that replaced the table; they
  were not read for this encoding.
- Reconcile c048's $12,842 with the text, and correct whichever side is wrong.
- Encode s 23AB, so that base rate entity passive income is computed rather than taken as an input.
- Rounding to whole dollars, and the interaction with offsets in the Income Tax
  Assessment Act 1997 s 4-10, are not modelled.
