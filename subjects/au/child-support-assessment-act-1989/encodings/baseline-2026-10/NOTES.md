# Child Support (Assessment) Act 1989 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use as advice.

**Edition:** the Act as compilation register id C2026C00269, deposited at `../../registers/source-bundle/C2004A03872.txt` (retrieved 2026-10-13).
The Child Support (Assessment) Regulations 2018, Compilation No. 2 (14 October 2024, F2024C01070), deposited at `../../../child-support-assessment-regulations-2018/registers/source-bundle/F2018L00307.txt`; only reg 6 is used.

**Checks:** one module (`csa-formula.l4`, 18 questions exported for Legalese Cloud), one case file (`csa-cases-formula.l4`): 69 assertions, 69 satisfied, 0 errors, 0 warnings, with the stable `l4` of VS Code extension 1.6.98.

## Seat

**The parent assessed**: the liable parent, who pays.
In Jake's life he is Ruby's father after separating from Tahlia in June 2038.
His question is "How much child support must I pay, and when can that change?"
Part 5 is written as the Registrar's method, but every step is a figure about the paying parent: his income, his care, his percentage, his rate.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The deposited Regulations set none of the formula's numbers: reg 6 (WA and SA child welfare law) is used, and reg 14 (the daily rate) has lost its formula.
  The figures published outside the Act are inputs: the annualised MTAWE figure, the self-support amount, the indexed minimum annual rate and low income rate, and the pension PP (single) maximum basic amount.
- **The actors the text names.** Followed: the parent, the other parent, the Registrar and the court.
- **Judgments handed to others are answered conditionally.** Followed. The Registrar's satisfaction (s 98C grounds and justice, s 56(2A)(c) special circumstances) and the s 65B determination are inputs.
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed for percentage of care, regular and shared care, cost percentage, child support income and percentage, and the costs of the children.
  Adjusted taxable income is taken as a total; its components are tax-law terms. Eligibility under ss 19-21 is asked as a fact.
- **One case is the natural unit.** One child support case. One departure: the same nights of care are taken for every child in the case.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed.

## The lives

- **Jake, k071, 15 June 2038: a child support assessment by the formula.** The question is "How much child support must I pay?". It is answered by `How much child support must I pay` on the fixture `Jake in 2038 (k071)`.
  The scenario gives no incomes and no care arrangement, so the figures are illustrative: Jake earns $70,000, Tahlia $50,000, and Ruby (5) is with Jake every second weekend, 52 nights a year.
  The answer is $4,224 a year by the formula, with income percentage 66.67, care 14%, cost percentage 24, child support percentage 42.67 and costs of the child $9,900. The published figures are also illustrative.
  The fixtures' later variants show what changes the answer: lower income, sharing care, becoming the main carer, an agreement.
  The departure-reach test is anchored on his assessment day.

## Why this scope

Formula 1 is the case the life presents: two parents, one child, no other children.
Around it sit what a paying parent meets in practice:

- whether the child can be assessed at all;
- the low income and minimum rates;
- the five ways the assessment changes: a change of care, an income estimate, an amended tax assessment, post-separation income, and departure in special circumstances.

Formulas 2 to 6 are out. So are relevant dependent children and multi-case allowances, the Registrar's care determinations and interim periods, reconciliation, s 66A, agreements and court orders. They are listed in the module header.

## What the Act turns out to say

1. **The deposited text has lost every formula set as an image**: s 35 step 8, ss 41(1)-(4), 45, 55B, 55D(1), 55E(2), 65A(4), 66(6), 66A(3)-(3A), 153A(2), and reg 14(1).
   Only the words around them survive. Three of the lost formulas are reconstructed from the simplified outlines, which survive, and are marked INFERENCE:
   - child support income is adjusted taxable income less the self-support amount (s 40E, s 46 step 1);
   - the income percentage is my income over the combined income (s 55A);
   - the child support percentage is "the difference between the parent's income percentage and his or her cost percentage", and the rate is "that percentage of the costs of the child" (s 55A).

   The self-support amount itself is an input; the deposit never states it. Asserted.
2. **The cost percentage table steps unevenly.** Under 14% care a parent is credited with nothing. From 14% to under 35% the credit is a flat 24%. From 35% it climbs 2 points per point of care, levels at 50% between 48% and 52%, and climbs again from 53% at 51%. It is flat at 76% to 86%, then 100%.
   Moving from 13% to 14% care changes the assessment; moving from 14% to 30% does not (s 75(2)(a)). Asserted.
3. **Care is rounded away from 50%.** Above 50% a fraction rounds up, below 50% it rounds down (s 54D). Two parents with 182 and 183 nights get 49% and 51%; both cost percentages are 50%, and equal incomes give nil (s 40D). Asserted.
4. **The costs of the children are a marginal scale on the combined income**, in bands of half the annualised MTAWE figure, and stop rising above 2.5 times MTAWE (Schedule 1 clauses 2-3).
   With more than 3 children only the 3 oldest set the row, but the costs are divided among all of them (ss 55G(4), 55H). Asserted.
5. **A low-income parent pays the flat s 65A rate whatever the formula gives.** The conditions are adjusted taxable income under the pension PP (single) maximum basic amount, no income support payment, and less than shared care. The total is capped at three times the rate.
   On income support, or after a s 65B determination, the parent falls instead to the minimum annual rate if the formula gives less (s 66(1), (2)). Asserted.
6. **If the other parent has less than 35% care, the paying parent's rate is nil**, even with a positive child support percentage (s 40C). Asserted.
7. **An income estimate must be no more than 85% of the last year's adjusted taxable income** (s 60(1)(b)). A post-separation income determination can cut adjusted taxable income by at most 30% (s 44(3)(a)). Asserted.
8. **An amended tax assessment reaches back to the start of the year if income went up**, or if the parent applied promptly (s 56(2A)). Otherwise it only runs forward. Asserted.
9. **A departure cannot take the rate below the minimum annual rate** unless the parent has at least regular care (s 98SA).
   It cannot reach more than 18 months back without a court's leave, and leave cannot reach back 7 years (ss 98S(3B), 111(1)). Asserted.
10. **Contact costs count as "high" only above 5% of the parent's adjusted taxable income for the period**, and with regular care only travel counts (s 117(2B), (2C)). The same 5% applies to child care costs, for a child under 12 (s 117(3A), (3B)). Asserted.
11. **Reg 6 takes a child in the custody or guardianship of a person under Western Australian or South Australian child welfare law out of the scheme**, so no assessment can be applied for (s 22, s 24(1)). Asserted.

## What would need doing before this is worth anything

- Retrieve the formulas the deposit lost, from the PDF or the authorised compilation, and replace the three INFERENCES. Above all, retrieve s 45 so the self-support amount can be worked out rather than asked.
- Retrieve the gazetted figures (s 155) for real child support periods and replace the illustrative inputs.
- Encode Formulas 2-6, relevant dependent children and multi-case allowances. A parent who re-partners with children of the new household needs them.
- Encode the care determinations and interim periods (ss 49-54L), reconciliation (ss 64-64AH) and the 28-day tail of s 66(4).
- An independent test pass against Services Australia's published worked examples.
