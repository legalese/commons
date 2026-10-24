# General Statutes of Connecticut, chapter 229 (Income Tax): the resident individual — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it: a question outside the encoding answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

The General Statutes of Connecticut revised to January 1, 2025, chapter 229, deposited at `../../registers/source-bundle/cgs-chap-229-rev2025.txt`, read with the 2026 Supplement (revised to January 1, 2026) at `../../registers/source-bundle/cgs-chap-229-sup2026.txt`. Where a section is in both, the Supplement version is the one encoded: here s 12-701 (definitions) and s 12-704e (earned income tax credit, with the additional $250). Both retrieved 2026-10-19 from cga.ct.gov. Changes from the 2026 sessions are not in either.

Every figure is in the statute: the schedules, the exemptions, the credit tables, the EITC percentage. Nothing is indexed by regulation, so no figure is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ct-income-tax.l4` | `ct-cases-income-tax.l4` | 52 written, 52 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Two `#TRACE`s end in a breach, each with an `-- expect:` line; both were read and match. Every expected value was worked by hand from the text, with the working in the comment above the assertion.

## Seat

**The individual taxpayer, resident in Connecticut for the whole year.** Questions: "Am I a resident?", "What is my exemption?", "What is my tax before credits?", "What percentage does the personal credit take off?", "How much earned income tax credit do I get?", "How much do I owe, or get back?", "By when must I file and pay?", "What is added if I pay late, or file nothing?", "Until when may I claim a refund?". "Must I file?" answers `not covered` (finding 1).

The Commissioner of Revenue Services appears only as what the Commissioner may do to the taxpayer (make a return for them, s 12-735(b)) or must do for them (decide a refund claim within 90 days, s 12-732(a)(1)).

The 2026-10-18 defaults:

- **The Act alone.** Chapter 229 only. No regulation sets a figure the encoded sections need.
- **The actors the text names:** the taxpayer, the Commissioner of Revenue Services.
- **Judgments handed to others:** none needed in scope; reasonable-cause waiver (s 12-735(c)) is noted, not modelled.
- **Definitions:** "resident of this state" (s 12-701(a)(1)) and "Connecticut taxable income of a resident" (s 12-701(a)(8)) are worked out from facts. Borrowed terms are asked as facts: domicile; the federal filing status (IRC s 2); federal AGI and the earned income credit "claimed and allowed" under IRC s 32; "qualifying child for federal income tax purposes". **Departure:** Connecticut adjusted gross income (s 12-701(a)(20)) is the chapter's own term but is asked as an input, because its modifications run to dozens of items; that is the main thing to do next (see the last section).
- **One case:** one return for one taxable year.
- **Terms:** the chapter's own, quoted above each rule.
- **Machinery out:** s 12-740 and s 12-741 (administration, regulations), the special accounts for refund contributions, the reports.

## Read with the federal encodings

The Internal Revenue Code is being encoded at `subjects/us/internal-revenue-code-of-1986/` (a baseline under `encodings/baseline-2026-10/`, by another session on 2026-10-24). This encoding takes from it, as inputs: federal adjusted gross income (IRC s 62, the start of s 12-701(a)(20)), the federal filing status (IRC s 2), and the federal earned income credit (IRC s 32). The stable `l4` cannot IMPORT across subject folders, so the link is recorded here and in the module header.

## Scope

**In:** s 12-700(a) with (a)(10)(A) to (D) (taxable years from 2024); s 12-701(a)(1) and (a)(8); s 12-702(a)(1), (a)(2)(I), (b), (c) (the exemption amounts and phase-outs; the joint/separate election in (c)(1) only as the federal status carried over); s 12-703(a)(1), (a)(2)(I), (b), (c); s 12-704e(a) to (c) (2026 Supplement); s 12-719(a); s 12-732(a)(1) (first sentence and the 90-day decision; not the extension case or interest); s 12-735(a), (b).

**Out:** nonresidents and part-year residents (s 12-700(b), (c), ss 12-711, 12-717): `not covered`; taxable years before 2024 (the (a)(1) to (a)(9) schedules): `not covered`; fiscal years; trusts and estates; s 12-700a (alternative minimum tax); s 12-701(a)(20)'s modifications; credits other than ss 12-703 and 12-704e; withholding and estimated tax; pass-through entities; s 12-702a; s 12-723 extensions; assessments, protests and appeals; s 12-704e(d) (the EITC is not income for means-tested benefits; noted for the benefits encodings).

## What the chapter turns out to say

1. **Chapter 229 does not say who must file.** s 12-719(a) fixes when "the income tax return required under this chapter" is due, and speaks of "A person required to make and file a return", but no section deposited says who that is. s 12-740(c) lets the Commissioner "require any person, by regulation or notice served on such person, to make such returns". The filing threshold is therefore in regulations or the return instructions, not deposited. Asserted (`not covered`).
2. **The phase-out of the 2% bracket and the three recapture amounts run on Connecticut adjusted gross income, not on taxable income.** In each schedule, (ii) to (v) start where "the taxpayer's Connecticut adjusted gross income exceeds" a figure. So two people with the same taxable income can owe different tax. Asserted (unmarried, AGI $80,000: $3,650 by the schedule plus $125 under (ii)).
3. **Taxable income is AGI less the exemption, with no floor stated.** s 12-701(a)(8) says "reduced by the amount of the exemption". The encoding never lets it go below nil. Asserted (AGI $10,000: no tax).
4. **The s 12-703 schedules give a percentage without saying of what.** The text says the person "shall be entitled to a credit in determining the amount of tax liability ... in accordance with the following schedule", and the column is headed "Amount of Credit" with entries such as "75%". This encoding applies the percentage to the tax under s 12-700, including the (ii) to (v) amounts. An interpretive choice, not checked against the Department's forms. Asserted (unmarried, AGI $50,000: $2,000 less 10%).
5. **At the top, the recaptures stop $50 short of a flat 6.99% for an unmarried filer.** At AGI $600,000 the schedule gives $38,240; (ii) adds $250 and (iii) to (v) add their maxima of $250, $2,700 and $450: $41,890. A flat 6.99% of $600,000 is $41,940. Summing what each bracket saves against 6.99% gives $3,700, and the recaptures add $3,650. Whether the gap is meant is not for this encoding to say; it follows from the figures as enacted. Asserted.
6. **The married-filing-separately phase-out is twice as steep as the unmarried one.** (D)(ii) reduces the 2% bracket by $1,000 for each $2,500 over $50,250, where (A)(ii) uses $5,000 over $56,500, though (D)(i) and (A)(i) are the same schedule. Asserted (separate, AGI $60,000: four steps).
7. **The additional $250 is one amount per return, and only with a federal credit.** s 12-704e(b) (2026 Supplement) gives "an additional two hundred fifty dollars" to a taxpayer "eligible for the credit under this section" with "at least one qualifying child". The number of children does not change it, and with no federal earned income credit there is no state credit to add it to. Asserted.
8. **The earned income tax credit is refundable, and is the only refundable item in scope.** s 12-704e(b) refunds "such excess, without interest". The s 12-703 credit has no such words, so it takes the tax only down to nil. Asserted (AGI $20,000 with a $3,000 federal credit: balance -$1,410).
9. **"May file a claim for refund" is written as `DO ... LEST FULFILLED`.** In the stable `l4` the `HENCE` of a `MAY` also fires when its time runs out unused, which would start the Commissioner's ninety days on a claim never made. Asserted (no claim: fulfilled; a claim on day 300 not decided by day 390: breach, traced).
10. **The penalty for late payment and the addition for no return cannot both apply.** s 12-735(b): "No taxpayer shall be subject to a penalty under both subsections (a) and (b)". The two are separate questions here and are not added together.

## Before relying on it

- Encode s 12-701(a)(20), the modifications from federal AGI to Connecticut AGI, at least the Social Security subtraction and the pension and annuity subtraction, so that the person states federal AGI rather than Connecticut AGI.
- Source the Commissioner's rule or the Form CT-1040 instructions on who must file (finding 1).
- Check finding 4 against the Department's tax tables.
- Part-year residents and nonresidents (s 12-700(b), (c)) are common and should be next.
- An independent test pass.
