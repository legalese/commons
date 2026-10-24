# South Carolina Income Tax Act (S.C. Code ch. 12-6), the individual income tax — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE: questions outside the encoding answer `not covered`, and tests assert it. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

There was no earlier encoding of this chapter. No requirement ledger exists for US states.

## Edition

South Carolina Code of Laws Unannotated, Title 12, Chapter 6 (South Carolina Income Tax Act), "current through the 2025 Session of the General Assembly", as deposited at `../../registers/source-bundle/sc-code-title-12-chapter-6-income-tax-act.txt` (retrieved 2026-10-19 UTC). The 2025 rate figures are the "2025 TAX COMPUTATION SCHEDULE" that the Legislative Council prints in the Editor's Note under s 12-6-510, which is part of the deposited text. Nothing else is brought in.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sc-income-tax.l4` | `sc-income-tax-cases.l4` | 47 written, 47 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Three `#TRACE`s check breaches (late return without and with an extension; late payment), each with an `-- expect:` comment; all three gave the expected breach. Every expected value was worked by hand from the formulas in the text.

## Seat

**The individual taxpayer**, a resident of South Carolina alone or with a spouse on a joint return. Questions: "Must I file?", "By when, and by when must I pay if I have an extension?", "Joint or separate?", "What is my South Carolina taxable income?", "What is the tax on it?", "How much is my EITC / two wage earner credit?", "How much do I owe after credits?".

The Department of Revenue's powers (extensions, tax tables, indexing) are encoded for what they mean to the taxpayer: the extended due date, and the indexed figures as inputs.

Defaults followed:
- **The Act alone.** The 2025 schedule comes from the Editor's Note in the deposited text. Indexed figures for other years (the brackets under s 12-6-520, the dependent exemption under s 12-6-1140(13)) are inputs. For 2026 and later the core function takes the department's published schedule; the exported question has no input for it and answers `not covered` (finding 1).
- **Borrowed federal terms asked as facts:** federal taxable income, gross income, the IRC s 63 standard deduction, the s 151(d) exemption amount, the federal EITC (IRC s 32), the IRC s 21 creditable expenses, net capital gain (IRC s 1222), dependency (IRC ss 151, 152). The federal Internal Revenue Code encoding being written at `subjects/us/internal-revenue-code-of-1986/` answers those; cross-folder IMPORT is not possible in the stable `l4`, so the link is recorded here only.
- **The actors the text names:** the taxpayer and the department.
- **One case:** one return (one individual, or a married couple on a joint return).
- **Machinery out:** Article 1 administration, withholding (ch. 12-8), penalties (ch. 12-54), the Revenue and Fiscal Affairs Office's forecast process.

## Scope

**In:** s 12-6-30(2), (3); s 12-6-40(A)(1)(a) (as the starting point); s 12-6-510(B)(1) and the 2025 schedule; s 12-6-1110; s 12-6-1120(1), (2), (4); s 12-6-1130(2); s 12-6-1140(13); s 12-6-1150(A); s 12-6-1160; s 12-6-1170(A)(1), (2), (B); s 12-6-3330(A), (B); s 12-6-3380 (first paragraph); s 12-6-3632; s 12-6-4910(1); s 12-6-4970(A), (E); s 12-6-4980(A), (B); s 12-6-4990; s 12-6-5000.

**Out:** nonresidents and part-year residents (ss 12-6-1710, 12-6-1720: `not covered`, asserted; s 12-6-4910(1)(d) is in); rate schedules for 2022 to 2024 (the phase-down of s 12-6-510(B)(3): `not covered`, asserted); the surviving-spouse limb of s 12-6-1170 and s 12-6-1171 (military retirement); s 12-6-1120(3), (5)-(11) and s 12-6-1130 other than (2); s 12-6-1140 items other than (13); the other Article 25 credits; estates, trusts, partnerships, corporations; estimated tax (s 12-6-3910).

## Regulative rules

Two `DEONTIC` rules in days from the end of the taxable year: the duty to file by the fifteenth day of the fourth month, or the extended date where an extension is allowed (ss 12-6-4970(A), 12-6-4980(A)); and the duty to pay by the original due date regardless of any extension (ss 12-6-4980(B), 12-6-4990). Penalties are in ch. 12-54, not deposited; each breach is named with its reason only.

## What the Act turns out to say

1. **For 2025 the top rate is fully phased down to 6%.** Section 12-6-510(B)(3) phases the top rate down from 6.5% (2022) by 0.1 point a year on a revenue trigger "until the top marginal rate equals 6%". The Legislative Council's 2025 schedule printed under the section shows "6.0% times the amount minus $642" from $17,830, with 3% from $3,560 (less $107). The encoding uses that schedule for 2025. The 2023 and 2024 rates depend on the trigger, which the text does not resolve (`not covered`). From 2026 only the brackets are indexed, so a schedule supplied by the department is enough. Asserted.
2. **The printed schedule goes a few cents below zero at the bottom of the 3% bracket.** 3% of $3,560 is $106.80, less $107 is −$0.20. Nothing makes a negative amount payable or refundable, so the encoding floors it at zero. The subtracted amounts are rounded whole dollars, so the schedule differs by under a dollar from a marginal-rate reading (3% of the excess over $3,560). The encoding follows the schedule as printed. Asserted ($3,560 gives 0; $17,830 gives $427.80).
3. **The filing threshold is "at least" for a single filer but "more than" for a joint return.** Section 12-6-4910(1)(a) requires a return where gross income is "at least" the exemption amount plus the basic standard deduction; (b) requires one where joint gross income "is more than" twice the exemption amount plus the standard deduction. Encoded as written: a single filer exactly at the threshold must file; a couple exactly at it need not. Asserted.
4. **A married person filing separately whose spouse itemizes falls under (c), not (a).** Item (a) covers married filing separately only where the spouse "does not itemize". Where the spouse itemizes, the standard deduction is zero (IRC s 63(c)(6)(A), borrowed), which is (c)(iii): file if gross income exceeds the exemption amount. Asserted.
5. **On a joint return, the age 65 deduction is reduced spouse by spouse.** Section 12-6-1170(B) allows "fifteen thousand dollars reduced by any amount the taxpayer deducts pursuant to subsection (A)", with a $30,000 maximum on a joint return where both spouses are 65. It does not say whether one spouse's (A) deduction reduces the other's $15,000. The encoding applies each spouse's (A) deduction against that spouse's $15,000 only. An interpretive choice. Asserted (retired couple case).
6. **Only the EITC is said to be nonrefundable.** Section 12-6-3632 calls its credit "nonrefundable". Sections 12-6-3330 (two wage earner) and 12-6-3380 (child and dependent care) say nothing either way. None is said to be refundable, so all three are applied against the tax and the result is floored at zero. Asserted.
7. **Social Security is taken out entirely.** Gross income is computed "without application of Internal Revenue Code Section ... 86" (s 12-6-1120(4)), so whatever part of Social Security was federally taxable is subtracted. Asserted.
8. **The state income tax add-back is capped.** Section 12-6-1130(2) disallows the deduction for state and local income taxes, but "limited for individual taxpayers to the excess of itemized deductions over the standard deduction that would be allowed". Asserted ($6,000 of income tax, $5,000 excess: $5,000 added back).
9. **The due date assumes a taxable year that ends at a month end.** "The fifteenth day of the fourth month following the taxable year" is computed from the day after the year ends; a 52-53 week year ending mid-month is not handled.

## Before relying on it

- Deposit the Department of Revenue's published 2026 schedule and indexed dependent exemption, if their terms allow, and add them as figures.
- Link the federal inputs to the IRC encoding when cross-folder imports are possible.
- Encode nonresidents and part-year residents (Article 13), s 12-6-1171 and the surviving-spouse rules, and the credit for taxes paid to another state (s 12-6-3400).
- An independent test pass.
