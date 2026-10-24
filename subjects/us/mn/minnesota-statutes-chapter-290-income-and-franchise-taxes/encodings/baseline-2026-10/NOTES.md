# Minnesota individual income tax (Minnesota Statutes ch. 290) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `mnit.l4`: the statute's terms (resident, net income, taxable net income, the standard deduction, the dependent exemption, the Social Security subtraction, the rate schedules, the child tax credit and working family credit and their joint phaseout) and, under `§§ Questions for the taxpayer` and the credit heading, the exported questions, each calling those rules. The commissioner's duty to refund the excess of the refundable credits is a regulative rule. One case file, `mnit-cases.l4`; expected values worked out by hand.

There was no earlier encoding of this subject.

## Edition

**Minnesota Statutes 2025**, chapter 290, from the Office of the Revisor of Statutes (retrieved 2026-10-19), deposited 2026-10-20 at `../../registers/source-bundle/mn-stat-ch-290-2025.txt`. The file's header lists 43 provisions the Revisor flags as affected by the **2026 Regular Session**, among them 290.01, subd. 19, 290.0132 (new subdivisions) and 290.06, subd. 2c (the rate schedules). Those amendments are not in the deposited text and **not in this encoding**: for taxable year 2026 the answers may be wrong until the 2026 session laws are deposited.

**Inflation adjustment.** Each dollar amount is adjusted by the commissioner "as provided in section 270C.22" from a statutory year: 2019 for the brackets (290.06, subd. 2d) and the dependent exemption (290.0121, subd. 3); 2023 for the standard deduction and its limit (290.0123, subd. 6), the Social Security phaseout thresholds (290.0132, subd. 26(j)), the credit phaseout thresholds (290.0661, subd. 7(b)) and the working family credit amounts (290.0671, subd. 7); 2025 for the child tax credit (290.0661, subd. 7(a)). Section 270C.22 and the commissioner's published amounts are **not deposited**. The encoding takes one factor per statutory year as an input and applies each provision's own rounding; with factor 1 it gives the statutory-year figure unrounded. The cases mostly use factor 1, so their figures are statutory-year figures, not any one year's return.

## Checks

- `mnit-cases.l4`: 32 assertions written, 32 satisfied, 0 errors, 0 warnings. One `#TRACE` (a refund of the wrong amount) leaves the commissioner's obligation open, as its `-- expect:` comment says.
- `mnit.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The individual Minnesota resident**, or the married couple filing jointly: "Am I a resident? How much Minnesota income tax do I owe? How much child tax credit and working family credit do I get back?"

Defaults:

- **The Act with the instruments that set its numbers.** The Act's figures are used; the commissioner's annual adjustment is an input factor (270C.22 not deposited).
- **The actors the text names.** The taxpayer, the spouse, the commissioner of revenue.
- **Borrowed terms asked as facts.** Federal AGI, IRC s 32 eligibility and qualifying children, IRC s 86 provisional income and taxable benefits, IRC ss 151, 152 dependants.
- **One case is one return.**
- **Departure.** Itemized deductions are taken as one figure after the limit of 290.0122, subd. 2, rather than built from subds. 3 to 9.

## Scope

In: 290.01, subds. 7, 19(b), 22(1); 290.0121; 290.0123, subds. 1, 2, 5, 6; 290.0132, subds. 19, 20, 26; 290.06, subds. 2c(a) to (c), 2d; 290.0661, subds. 1 to 4, 6, 7; 290.0671, subds. 1(a) to (d), 1a, 4, 7.

Out: nonresidents and part-year residents; dependants of another taxpayer (290.0123, subd. 3); a separate filer whose spouse itemizes (290.0123, subd. 4); the tax tables (290.06, subd. 2c(d)); advance payments and the minimum credit (290.0661, subds. 8, 9); the earned-income allocation (290.0671, subd. 1(e)); the other additions and subtractions (totals); all other credits; the alternative minimum tax; filing and payment (ch. 289A, not deposited, so no filing duty is encoded).

## Link to the federal encoding

Net income starts from federal adjusted gross income (290.01, subd. 19(b)), with the Internal Revenue Code "as amended through May 1, 2023" (subd. 19(f)); the credits rest on IRC s 32 and the Social Security subtraction on IRC s 86. Those come from `subjects/us/internal-revenue-code-of-1986/` and are inputs here.

## What the Act turns out to say

1. **The 2026 amendments are missing.** The deposited 2025 edition omits the 2026 session's changes to 290.06, subd. 2c and 42 other provisions. This baseline answers for the law as printed in 2025.
2. **A cross-reference in the separate-return Social Security subtraction points nowhere.** 290.0132, subd. 26(h) reduces the separate filer's maximum by 20% of provisional income "over one-half the threshold amount specified in paragraph (d)". Paragraph (d) specifies no threshold (it sets the $2,000 step for the simplified subtraction). The encoding reads it as half the paragraph (f) threshold ($44,315), the parallel of (f) and (g).
3. **The adjustment clause names amounts it does not adjust.** Subd. 26(j) adjusts only "the phaseout threshold amounts in paragraph (c), clauses (1) and (2)", then says "The maximum subtraction and threshold amounts as adjusted must be rounded". Nothing adjusts the maximum subtractions or the provisional-income thresholds in (f) and (g); the encoding leaves them unadjusted.
4. **Some adjusted amounts have no rounding rule.** The credit phaseout thresholds (290.0661, subd. 7(b)) and the working family credit amounts (290.0671, subd. 7) are adjusted with no rounding stated; the encoding does not round them. The child tax credit is rounded "to the nearest $60", with no rule for a value exactly halfway (taken up).
5. **Three statutory years.** The brackets are adjusted from 2019, the standard deduction from 2023 and the child tax credit from 2025, so the deposited figures never describe one tax year together. A person cannot check a return against the Act's own numbers without the commissioner's tables.
6. **The 9% phaseout.** 290.0671, subd. 1(d) applies a 9% phaseout rate "for a taxpayer with one or more qualifying older children who did not qualify for the credit under section 290.0661". The encoding reads "who" as the taxpayer and applies 9% where the taxpayer has qualifying older children and no qualifying child under 18. Asserted.
7. **The child tax credit is $1,750 a child and refundable, for anyone eligible for the working family credit "except a taxpayer whose earned income was insufficient"** (290.0661, subd. 2): a family with no earnings but otherwise qualifying gets it. The joint phaseout uses the greater of earned income and AGI.

## Before relying on it

- Deposit the 2026 session laws (ch. 128 of 2026 and others) and the commissioner's inflation-adjusted amounts for 2025 and 2026, and section 270C.22.
- Deposit ch. 289A for the filing duty and due date.
- Encode the federal inputs from the IRC encoding; add part-year residents and the other subtractions.
- An independent test pass.
