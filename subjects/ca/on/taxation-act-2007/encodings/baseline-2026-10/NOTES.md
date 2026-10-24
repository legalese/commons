# Ontario Taxation Act, 2007 (personal income tax and benefits) — baseline encoding

© King's Printer for Ontario, 2007. The statutory words quoted in the modules are from an unofficial reproduction of the consolidated law published on e-Laws: **NOT AN OFFICIAL VERSION**. Official copies are those described in the Legislation Act, 2006. See `SOURCE-LICENSE.md`.

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the Act's own terms in `on-pit.l4`; the one dated duty (instalments) is in `on-pit-dates.l4`, so that only it and the seat import `daydate`. The individual's questions are in `on-pit-seat.l4`, which IMPORTs both and calls their rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Edition

- **The Act**: e-Laws consolidation from 2026-07-01 to the e-Laws currency date 2026-10-14 (last amendment 2026, c. 2, Sched. 15), English, deposited at `../../registers/source-bundle/S.O.-2007-c.-11-Sched.-A.txt`. O. Reg. 37/09 is deposited beside it; nothing in it is used (it prescribes no s 23 adjustment).
- **The indexed amounts** (s 23), from two Canada Revenue Agency pages deposited on 2026-10-24 (see `SOURCE-LICENSE.md`):
  - `cra-t4127-jan-2026.txt` (T4127, 122nd edition, January 2026): 2026 bracket limits $53,891 and $107,785, basic personal amount $12,989, surtax thresholds $5,818 and $7,446, tax reduction $300 and $554 a dependant.
  - `cra-ontario-programs-2026-10.txt` (page modified 2026-07-30): July 2026 to June 2027 Ontario child benefit "up to $146.66 per month for each child", partial above $26,865; Ontario sales tax credit $378 a person, reduced by 4% above $29,047 (single) or $36,309 (family).
- **Inputs, because no deposited text gives them**: the 2026 Ontario spouse amount and its income floor, the age amount and its threshold, the pension maximum and the disability amount (all indexed under s 23 (1) para 2). The CRA forms that print them (ON428, TD1ON) are under a robots.txt-disallowed path and were not fetched.

The **tax year 2026** and the **benefit months July 2026 to June 2027** are covered; other years answer `not covered`.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `on-pit.l4`, `on-pit-dates.l4`, `on-pit-seat.l4` | `on-pit-cases.l4` | 87 written, 87 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. One `#TRACE` shows a breach (the December instalment paid on day 360 against a day-348 deadline), with its expected result in an `-- expect:` comment, because a breached `EVALTRACE` can be asserted neither way in the stable `l4`. Every expected value was worked by hand from the text and the deposited figures.

## Seat

**The individual taxpayer and benefit recipient, resident in Ontario**: "Am I liable for Ontario tax? How much Ontario income tax do I owe for 2026? Do I get the tax reduction and LIFT? What Health Premium do I pay? When are my instalments due? How much Ontario child benefit and sales tax credit do I get a month? Must I repay an overpaid child benefit?"

Provisions addressed to the Ontario Minister are encoded for what they mean to that person: the benefit is "deemed to be an overpayment" the Minister "shall pay" (s 104 (3)), so the person's question is how much they get; s 104 (8) is the person's duty to repay.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** No Ontario instrument sets the s 23 figures; the CRA's publications of them are brought in (above), and where none was deposited the figure is an input.
- **The actors the text names:** the individual and the Ontario Minister.
- **Judgments handed to others:** none is guessed. Whether the federal Act relieves the person of instalments (s 115 (7), ITA s 156.1) is asked as a fact.
- **The Act's own definitions are worked out from facts:** the s 4 (1) paragraphs, basic personal income tax, gross tax amount, personal amount (s 20 (3)), eligible individual for LIFT (s 21.1 (1), (2)), combined income (s 24 (0.1)), the s 104 (4) conditions. **Borrowed federal terms are asked as facts:** taxable income (the tax base, s 3 (1)), net income, adjusted income, employment income, the ITA s 118 entitlements, the s 118.7 premiums and contributions, eligible individual and qualified dependant (ITA s 122.6), the GST/HST credit eligibility (ITA s 122.5).
- **One case:** one individual for one taxation year (tax), or one benefit month (benefits).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** administration (Part VIII) apart from s 115, collection agreements, regulation-making powers.

## Questions exported (12)

In `on-pit-seat.l4`, under `§` headings in the Act's order:

1. Which paragraph of s 4 (1) applies to me
2. What is my Ontario basic tax (s 6 (1))
3. What are my Ontario non-refundable credits (s 9)
4. What is my Ontario surtax (s 16)
5. Do I qualify for LIFT (s 21.1 (1), (2))
6. What is my LIFT credit (s 21.1 (3.1))
7. What is my Ontario Health Premium (s 24)
8. How much Ontario tax do I owe (s 5 (1), s 4 (3); 2026)
9. When are my Ontario instalments due (s 115 (1) (a), (7))
10. How much Ontario child benefit a month (s 104 (4), (5), (5.1), (6.2)) — the group arises only for a parent who gets the Canada child benefit
11. How much Ontario child benefit must I repay (s 104 (8), (9))
12. How much Ontario sales tax credit a month (s 103.8)

Questions 4 and 8 take the person's non-refundable credit total from question 3, as a number.

## Regulative rules (2)

1. `the duty to pay Ontario instalments` (`on-pit-dates.l4`; s 115 (1) (a), (7)): the individual MUST pay each of the March 15, June 15, September 15 and December 15 instalments WITHIN the days from 1 January to that date, joined by RAND, each with `LEST BREACH ... BECAUSE`; FULFILLED where ITA s 156.1 relieves the person.
2. `the duty to repay an Ontario child benefit overpaid` (`on-pit.l4`; s 104 (8), (9)): where more than $2 for a July-to-June period was received than was due, the individual MUST repay the excess. No time is set in the Act.

## Scope

**In:** s 3 (1) (rates, tax base); s 4 (1), (3); s 5 (1); s 6 (1); s 9 (2), (3), (4), (8), (9), (10), (12) (the rest of s 9 an input, in dollars of credit); s 16 (1), (2); s 19.1 and s 21 as inputs; s 20 (1)-(7), (9); s 21.1 (1), (2), (3.1), (4); s 23 (as the source of the indexed record); s 24 (0.1), (1), (2); s 103.8 (2)-(4); s 104 (4), (5), (5.1), (6.2), (8), (9); s 115 (1) (a), (7).

**Out** (each a `not covered` answer where a question can reach it): income earned outside Ontario and non-residents (s 4 (1) paras 2, 3; s 6 (2), the Ontario allocation factor); trusts; split income (s 12.1); minimum tax (s 19.2) and the ss 14, 15 credits; subdivision f (ss 17-19); the disability supplement for an individual under 18 (s 9 (12) (a)); the seniors' income threshold in s 103.8 (5); tax years other than 2026 and benefit months outside July 2026 to June 2027; the Ontario energy and property tax credit and the Northern Ontario energy credit (ss 103.9-103.13, the other parts of the Trillium Benefit, s 103.3); every other refundable credit and grant in Part IV; bankruptcy and death returns beyond the s 20 (9) and s 21.1 (2) exclusions; s 115 (1) (b) and (2) (other instalment methods; the farming and fishing rule).

Read with the federal Income Tax Act encoding, `subjects/ca/income-tax-act/` (being encoded by another session on 2026-10-24): taxable income, net income, adjusted income, the s 118 entitlements, the s 118.7 base and the Canada child benefit eligibility are inputs here that it could supply. Cross-folder IMPORT is not possible in the stable `l4`.

## What the Act turns out to say

1. **Ontario tax starts from federal taxable income.** The "tax base" is "the individual's taxable income for the year" (s 3 (1)) and "Federal Act" means the Income Tax Act (Canada) (s 1 (1)); nearly every credit in s 9 turns on being "entitled to a deduction under" a federal provision. Asserted (the inputs are federal figures).
2. **The figures in the Act are not the ones in force.** Section 23 indexes the two lower bracket limits, most s 9 amounts, the surtax thresholds and the s 20 amounts every year, and the adjusted figures appear nowhere in the Act or O. Reg. 37/09. The 2026 figures come from the CRA's T4127. The $150,000 and $220,000 limits are not indexed (s 23 (1) para 1.1 excepts $150,000; para 4 of s 6 (1) is not listed). Asserted (both the written and the 2026 limits are tested).
3. **Some amounts are fixed.** LIFT (s 21.1: $875, $32,500, $65,000) and the Health Premium (s 24) are not in the s 23 (1) list and are not indexed. Asserted.
4. **The written s 20 amounts and the 2026 ones keep one ratio.** $205 and $379 (s 20 (4), (5)) against T4127's $300 and $554, and $8,881 (s 9 (2)) against $12,989, are all about 1.4626 apart, consistent with the 2017 amendment having restated s 20 in 2009 dollars indexed from 2010 like s 9. An observation from the two texts; nothing relies on it.
5. **The Health Premium is a sixth step, outside the tax.** It is Division C (s 24), added to the Division B tax (s 4 (3)), and is payable even when the Division B tax is nil. Each band is capped by "the lesser of", so it rises continuously to $900. The T4127's factor V2 agrees. Asserted (the $25,000 worker owes $300 of premium and no tax).
6. **The child benefit's 2026-27 amount is $1,760 a child a year.** The CRA page says "up to $146.66 per month"; s 23 (4) rounds the indexed "A" to a whole dollar, and $1,760 is the only whole-dollar amount whose twelfth lies between $146.66 and $146.67 ($1,759 gives $146.58). The encoding uses $1,760 and asserts that the monthly amount lies between those figures. The page states the monthly figure rather than "A", so this is a derivation, not a quotation.
7. **Three formulas can go below zero and the Act does not say "if any".** The spouse and dependant credits (s 9 (3), (4)), the child benefit (s 104 (5)) and the LIFT "(D - E) x F" (s 21.1 (3.1)) are read as nil when negative. Asserted (a spouse with $9,000 of income gives no credit; an income of $48,865 gives no child benefit; a $60,000 earner gets no LIFT).
8. **The tax reduction and LIFT cannot make tax negative.** Both are subdivision i credits, deducted at s 5 (1) para 8, which takes "the amount, if any". Asserted (case B: tax otherwise payable $530.81 against $944.19 of credits).
9. **Only the higher-income partner counts the children for the tax reduction.** Where the individual lives with a cohabiting spouse on December 31, a dependant is included only "if the individual's income for the year exceeds the income of the cohabiting spouse" (s 20 (2)). Asserted (case E).
10. **LIFT has two income tests.** "E" is 5% of the greater of personal adjusted income over $32,500 and family adjusted income over $65,000 (s 21.1 (3.1)), so a low earner in a higher-income family loses part of it. Asserted ($30,000 own, $70,000 family: $625).
11. **The sales tax credit's "A" is $260 for each person in the family.** The four clauses of s 103.8 (3) "A" come to the individual, a qualified relation, and each qualified dependant (the eligible-dependant clause and the per-dependant clause never count the same child). This matches the CRA's "for each adult and each child". Asserted.
12. **A shared-custody parent gets the average of two computations** for both the child benefit (s 104 (5.1)) and the sales tax credit (s 103.8 (4)), the second "as if the individual were not an eligible individual" for the shared children. Asserted.
13. **Small child-benefit amounts vanish.** A total under $2.01 for the July-to-June period is nil (s 104 (6.2)), and an overpayment of $2 or less need not be repaid (s 104 (9)). Asserted.
14. **Instalments follow the federal rule.** Section 115 (7) switches off the Ontario instalments whenever ITA s 156.1 does so for the federal ones, so the threshold is federal. The encoding gives each quarter its own act, so that one payment cannot discharge two. Asserted (a late December payment is a breach).

## What would need doing before this is worth relying on

- **The other indexed 2026 amounts** (spouse, age, pension, disability, and the rest of s 9) from a deposited official publication, so they need not be inputs. The CRA's ON428 and TD1ON carry them but sit under a robots.txt-disallowed path; an HTML source, or a permitted route to those forms, is needed.
- **Taxation years other than 2026**, each with its own deposited figures.
- **The Ontario allocation factor** (income earned outside Ontario, non-residents), split income, minimum tax, and the rest of s 9 itemised.
- **The other Trillium Benefit credits** (ss 103.9-103.13), which need property tax, rent and northern residence facts.
- **The federal inputs** from the Income Tax Act encoding, once it is published.
- **An independent test pass**, and a check of findings 4, 6 and 7 against CRA or Ministry of Finance guidance (none was read).
