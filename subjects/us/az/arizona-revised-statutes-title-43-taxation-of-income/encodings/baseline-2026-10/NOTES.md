# A.R.S. Title 43 (individual income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
The core rules use the statute's own actors and terms; the taxpayer's questions (`@export`, `@desc`, under `§ Questions for the taxpayer`) are derived from them.
Duties and elections the text states (file, pay by 15 April, elect and change the standard deduction) are regulative rules with the party as a parameter.
No REFUSE; cases outside the encoding answer `not covered`, and tests assert them.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not tax advice.**

Part of the Arizona "tax and benefits" sample, with TANF cash assistance at `../../../arizona-revised-statutes-title-46-chapter-2-article-5-temporary-assistance-for-needy-families/encodings/baseline-2026-10/`.

## Edition

The Legislature's online Arizona Revised Statutes (unofficial; "updated to include the revised sections from the 57th Legislature, 2nd Regular Session"):

- `../../registers/source-bundle/az-ars-43-ch1-general-provisions-sel-2026.txt` (ss 43-102, 43-104, 43-105; fetched 2026-10-19);
- `../../registers/source-bundle/az-ars-43-ch10-individuals-sel-2026.txt` (ss 43-1001 to 43-1073.01, selected; 2026-10-19);
- `../../registers/source-bundle/az-ars-43-ss243-301-501-2026-10-24.txt` (ss 43-243, 43-301, 43-501; **deposited for this encoding on 2026-10-24**, because the rate could not be settled without s 43-243).

**Inputs, not deposited:** federal AGI and the Social Security amount in it (IRC; `subjects/us/internal-revenue-code-of-1986/`); the department's inflation-adjusted standard deduction for any year other than 2025; the year the s 43-243(B)(2) revenue notice was received. The cases assume that notice was received in 2022 and a 2026 head-of-household standard deduction of $24,150, and say so.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `az-income-tax.l4` | `az-income-tax-cases.l4` | 39 written, 39 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). One `#TRACE` (tax unpaid by 15 April: breach) with an `-- expect:` comment that matched.
On the first run one case (E) failed: the net-tax formula had a `MINUS` at the start of a continuation line, which the stable `l4` attached inside the preceding bracket (the trap in guide section 5). The formula was rewritten with named parts under `WHERE`; the expected value, worked by hand, did not change.

## Seat

**The individual taxpayer, resident in Arizona all year.** Questions: "Am I a resident?", "Must I file?", "When must I pay?", "What are my exemptions?", "What is my dependent credit?", "What is my excise tax credit?", "How much do I owe?".

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers:** Title 43. The department's inflation adjustments and the revenue notices are not instruments that were deposited; they are inputs.
- **The actors the text names:** the taxpayer, the department, the directors who give the s 43-243 notices (as a fact only).
- **Judgments left to others** asked as facts: a "temporary or transitory purpose", whether the residence presumption is overcome, the notices.
- **Definitions** worked out: resident (s 43-104(19)), Arizona gross income, Arizona AGI, taxable income (s 43-1001). Borrowed terms (federal AGI, dependent, head of household) asked as facts.
- **One case:** one return for one taxable year.
- **Machinery out:** s 43-102 (intent), the department's rule-making, the board of tax appeals.

## Scope

**In:** s 43-104(19); s 43-301(A), (E); s 43-501; s 43-1001; s 43-1021 (one total); s 43-1022(1), (2), (10), (26) (the rest as one total); s 43-1023; s 43-1041(A), (C), (F), (G), (H), (I)(2); s 43-1011(A)(9) with s 43-243(C), (D); s 43-1072.01; s 43-1073; s 43-1073.01.

**Out:** nonresidents and part-year residents (`not covered`); taxable years before 2022 (`not covered`); s 43-1011(A)(7), (8) (indexed brackets, not deposited: `not covered`); s 43-1041(I)(1) (the 2025 charitable percentage, department-adjusted: `not covered` when it matters); s 43-1042 item by item; ss 43-1071 and 43-1072 (other-state credit; property tax credit); s 43-1013; the small business income tax.

## What the statute turns out to say

1. **The rate turns on a revenue notice that the statute does not record.** Paragraph 9 of s 43-1011(A) ("the tax is 2.5% of taxable income") applies "for taxable years beginning from and after December 31 of the year in which" the s 43-243(B)(2) notice (general fund revenue of $12,976,300,000 or more) is received (s 43-243(D)). Whether and when it was received is not in any deposited text. The person states the year; without it the answer is `not covered`. The 2026-10-20 plan's statement that 2.5% applies now remains unverified (general knowledge). Asserted (notice in 2025: not yet for 2025).
2. **The standard deduction figures in s 43-1041(A) are read as the 2025 figures.** They equal the federal 2025 basic standard deduction, and (H) adjusts them "for each taxable year beginning from and after December 31, 2019" in the same manner as the federal one. The statute cannot be both literally the 2020 base and these amounts; the encoding uses them for 2025 only and asks for the department's figure for other years.
3. **The charitable increase from 2026 names caps only for single or separate filers ($1,000) and joint filers ($2,000).** A head of household is described in (A)(2) as "a single person who is a head of a household", so the $1,000 cap is applied. Asserted (case C).
4. **The $2,500 public pension subtraction is read per return** (s 43-1022(2): "in an amount totaling not more than $2,500"). Whether each spouse on a joint return has $2,500 is not stated.
5. **The dependent credit's phase-out is read as five percent of the credit for each $1,000 or part of $1,000** of federal AGI at or over $200,000 ($400,000 joint) (s 43-1073.01(C)): "$125 minus five percent for each $1,000, or fraction thereof". Asserted ($210,500: 45% of the credit remains).
6. **Only the excise tax credit is stated to be refundable** (s 43-1072.01(D)). The family credit is capped at the tax (s 43-1073(B)(3)); the dependent credit says nothing, and is treated as nonrefundable. Asserted (cases C, E).
7. **The return's due date is not in the deposited text.** Section 43-301 says who "shall file", and s 43-501 says tax "shall be paid on the fifteenth day of April following the close of the calendar year". The filing duty has no `WITHIN`. Traced.
8. **Paragraphs 7 to 9 of s 43-1011(A) are each "subject to subsection F", but neither printed version of s 43-1011 has a subsection F.** A dangling reference in the register's text.
9. **The excise tax credit is enacted "if approved by the qualified electors"** (s 43-1072.01(A), with the register's "Caution: 1998 Prop 105 applies"). Nothing deposited records the vote; the credit is encoded as in force.
10. **Arizona does not tax Social Security**: it subtracts exactly the amount federal AGI includes under IRC s 86 (s 43-1022(10)). **Uniformed services retired pay is wholly subtracted from 2021** (s 43-1022(26)(c)). Asserted (cases D, F).
11. **The filing threshold is the standard deduction alone** (s 43-301(A)), whatever the person's exemptions, age or dependants. Asserted.
12. **Residence is presumed after more than nine months**, and the presumption can be overcome (s 43-104(19)(c)). Asserted.

## Before relying on it

- Deposit the s 43-243 notices (or a department publication of the rate in force) and the department's inflation-adjusted standard deduction and brackets.
- Add part-year residents and nonresidents, and the property tax credit (s 43-1072).
- An independent test pass.
