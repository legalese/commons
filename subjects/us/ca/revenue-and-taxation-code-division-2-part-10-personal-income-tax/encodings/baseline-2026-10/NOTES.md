# Rev. & Tax. Code Part 10 (California personal income tax, 2025) — baseline encoding

## Method

**Baseline.** Written straight from the deposited Code and the Franchise Tax Board's deposited 2025 figures, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
The core rules use the Code's own terms; the taxpayer's questions (`@export`, `@desc`, under `§ Questions for the taxpayer`) are derived from them.
The chapters deposited state almost no duties with a time: the filing and payment duties are in Part 10.2, not deposited. Two regulative rules are written where the text speaks to the taxpayer: the standard deduction election (`MAY`, s 17073.5(a)) and the duty to identify dependents for the dependent credit (`MUST`, s 17054(d)(2)).
No REFUSE; a year other than 2025, and a part-year resident, answer `not covered`, and tests assert them.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not tax advice.**

## Edition

- The Code: the Legislative Counsel's official bulk database export (code tables updated 2026-10-03), deposited 2026-10-20 as unofficial plain text: Part 10 chapter 1 (ss 17014, 17016), chapter 2 (ss 17041, 17043, 17045, 17048, 17053.5, 17054, 17054.1) and chapter 3 (s 17073.5).
- The annual figures: the FTB's 2025 California Tax Rate Schedules and 2025 Form 540 booklet, **deposited for this encoding on 2026-10-24** (`../../registers/source-bundle/ftb-2025-540-*.txt`, with a `.formulas.md` transcription of the schedules), recorded in `../../registers/annual-figures.json`. They are public domain (State of California conditions of use).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ca-income-tax.l4` | `ca-income-tax-cases.l4` | 30 written, 30 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). On the first run five tax cases failed: a percentage literal written as the last argument of a function application (`` `the row` `ti` 41452 1022.01 6% ``) was not read as that argument by the stable `l4`. Each rate was put in brackets (`(6%)`); the hand-worked expected values did not change. This trap is not in guide section 5 and is worth adding there.

## Seat

**The individual taxpayer, resident in California all year.** Questions: "Am I a California resident?", "What are my exemption credits?", "What is my renter's credit?", "How much do I owe for 2025?".

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers:** Part 10, with the FTB's 2025 recomputed figures, which the Code tells the FTB to compute and publish.
- **The actors:** the taxpayer and the Franchise Tax Board.
- **Judgments left to others**, asked as facts: a "temporary or transitory purpose", whether the residence presumption is overcome, who is a dependent, who is a qualified renter.
- **Definitions** worked out: resident (ss 17014, 17016), the exemption credit phase-out, the renter's credit. Borrowed terms (federal AGI, dependent) asked as facts.
- **One case:** one return for 2025.
- **Machinery out:** the FTB's recomputation powers (used only through their published results), the Department of Industrial Relations' CPI transmission.

## Read with

- The federal encoding, `subjects/us/internal-revenue-code-of-1986/`: California AGI starts from IRC s 62 (s 17072) with California's own modifications (for example, s 17087: no IRC s 86, so Social Security is not taxed; s 17083: no IRC s 85, so unemployment benefits are not taxed). California AGI is an input here.
- The California unemployment encoding beside this one: `../../../unemployment-insurance-code-division-1-part-1-unemployment/encodings/baseline-2026-10/`.

## Scope

**In:** s 17014(a), (c), (d); s 17016; s 17041(a), (b), (h) via the 2025 schedules; s 17043; s 17045; s 17053.5(a), (c), (j), (k); s 17054(a)-(f), (i); s 17054.1; s 17073.5(a), (d).

**Out:** taxable years other than 2025 (`not covered`); part-year residents and nonresidents (`not covered`); California AGI (an input); itemized deductions item by item; the CalEITC (s 17052) and the Young Child Tax Credit (s 17052.1), which depend on an adjustment factor set in the annual Budget Act and on form FTB 3514 (neither deposited); the other credits; the alternative minimum tax; the s 17048 Tax Table; the standard deduction of a dependent (IRC s 63(c)(5) via s 17073.5(c)(2)); filing and payment (Part 10.2).

## What the Code turns out to say

1. **Almost every figure is recomputed by the FTB each year.** The Code's own amounts are decades old ($1,880 standard deduction, s 17073.5(a)(1); $52 personal credit, s 17054(a); brackets starting at $3,650, s 17041(a)); the law that applies to a person in 2025 is those amounts as recomputed by the FTB (ss 17041(h), 17054(i), 17054.1(f), 17053.5(j), 17073.5(d)). The encoding uses the FTB's published 2025 figures and says where each comes from.
2. **For taxable income of $100,000 or less the FTB's Tax Table, not the schedules, gives the tax** (s 17048(a): tables "in income progressions of not less than one hundred dollars"). The encoding computes from the schedules at every income, so below $100,000 its answer can differ from the table's by the effect of the $100 step (a few dollars at most). The Tax Table is in the deposited booklet but is not encoded.
3. **The exemption credit phase-out counts "each $2,500, or fraction thereof"** of federal AGI over the threshold ($1,250 for a married person filing separately), at $6 a step for each credit and $12 for the joint personal credit (s 17054.1(a)). Read as rounding up, as the FTB worksheet does. Asserted ($260,000 single: 4 steps).
4. **The 1% tax on taxable income over $1,000,000 takes no credits** (s 17043(c)(1)) and does not double for joint filers ((c)(2), (3)). The FTB booklet calls it the Behavioral Health Services Tax; the Code's text is unchanged. Asserted (case 5).
5. **A married couple filing separately share one renter's credit.** "If the spouses file separate returns, the credit may be taken by either or equally divided between them" (s 17053.5(a)(2)). The encoding gives each the equal half, $60; one spouse could instead claim the whole $120.
6. **The larger renter's credit from 2026 ($250, or $500 with a dependent) is zero unless a Budget Act bill specifies it**, in which case the old $60/$120 amounts apply (s 17053.5(a)(1)(A)(ii), (B)(ii), (k), added by Stats. 2025, Ch. 22). For 2026 a person cannot tell from the Code alone which amount applies. Not encoded (2026 is `not covered`).
7. **Residence has a 546-day safe harbour for work abroad** (s 17014(d)), lost if intangible income tops $200,000 in a contract year, and a nine-month presumption (s 17016) that "may be overcome by satisfactory evidence". Asserted.
8. **California AGI and federal AGI are different inputs on purpose**: the exemption credit phase-out uses federal AGI (s 17054.1(a)), the renter's credit and taxable income use California AGI (s 17053.5(a)). Asserted (case 6).

## Before relying on it

- Deposit FTB 3514 and the Budget Act adjustment factor, and encode the CalEITC and Young Child Tax Credit, which matter most to lower-income Californians.
- Deposit Part 10.2 (filing and payment) and the FTB's 2026 figures when published.
- Encode the s 17048 Tax Table, or confirm the schedule method is acceptable.
- An independent test pass.
