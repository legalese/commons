# Income Tax Act (Canada) -- baseline encoding, 2026-10

A seat baseline of the federal Income Tax Act for the individual: residence, income from the main heads, taxable income, the 2026 rates and the main non-refundable credits, the OAS recovery tax, the three benefits paid through the tax system (Canada child benefit, Canada workers benefit, GST/HST credit), and the duties to file, pay instalments, pay the balance and notify the Minister.

Not for public use as advice. Unofficial version: the deposited text is a reproduction of the Department of Justice consolidation, not the official version (see `SOURCE-LICENSE.md`). Contains information licensed under the Open Government Licence - Canada.

## Method

BASELINE, written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual, with the design defaults ruled on 2026-10-18. No longer encoding of the Act exists, so this is a separate baseline, not a seat layer.

- `ita-amounts.l4` -- the dated table of indexed 2026 amounts (from the CRA's indexation table, below).
- `ita-individual.l4` -- the seat-neutral core: computations as functions; the duties as `DEONTIC` rules.
- `ita-seat.l4` -- the individual's questions, each with `@export` and `@desc` inputs, built over the core.
- `ita-cases.l4` -- cases on the core: the three the brief asks for and one-rule tests.
- `ita-cases-seat.l4` -- the same three cases asked through the seat questions, with answers that agree with the core.

No `REFUSE`. A case outside the encoding answers `not covered` with a reason (the `Why not covered` list in the core), and tests assert those answers. Expected values are hand-worked from the text and the CRA table, with the arithmetic in each case's comment. No pipeline, no coverage table, no independent test pass, no human gate.

## Edition

- **Income Tax Act**, R.S.C., 1985, c. 1 (5th Supp.), Justice Laws consolidation current to 2026-09-30, last amended 2026-06-18, as deposited at `../../registers/source-bundle/R.S.C.-1985-c.-1-5th-Supp..txt` (justicecanada/laws-lois-xml commit `0507465393c224c0491fc8c17c88340217acc656`). English version; the French is equally authoritative.
- **Indexed amounts**: the CRA's "Indexation adjustment for personal income tax and benefit amounts" (page dated 2026-03-12), deposited 2026-10-24 at `../../registers/source-bundle/cra-indexation-adjustment-2026.txt`, 2026 column only. It is an official publication, not law. For the CCB, the 2026 column is used for the months July 2026 to June 2027 (base taxation year 2025), as the table's preamble says CCB increases take effect on 1 July.
- Amounts the Act states without indexation are taken from the Act: the $2,000 pension amount (s 118(3)), the CWB's $3,000 and $1,150 thresholds, 27% and 15% rates, and the GST/HST credit amounts of s 122.5(3.005), which s 117.1(2)(m.1) indexes only for taxation years that begin after 2026.
- The Income Tax Regulations are deposited beside the Act but not used: withholding (Part I) and the CCB's prescribed factors (Part LXIII) are asked as facts.

## Checks

Stable `l4` from VS Code extension legalese.l4-vscode 1.6.98 (`bin/win32-x64/l4.exe`), `JL4_LIBRARY_PATH` unset, `l4 run <file>` from this folder, 2026-10-24:

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ita-amounts.l4` | 0 | 0 | -- | -- |
| `ita-individual.l4` | 0 | 0 | -- | -- |
| `ita-seat.l4` | 0 | 0 | -- | -- |
| `ita-cases.l4` | 0 | 0 | 98 | 98 |
| `ita-cases-seat.l4` | 0 | 0 | 32 | 32 |

`l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A deliberately wrong assertion added to a copy of `ita-cases.l4` was reported as failed, so the assertions are not vacuous. Four `#TRACE`s in `ita-cases.l4` breach on purpose (late filing, a short payment of the balance, a late instalment, a late notice), each with an `-- expect:` comment; the diagnostics show each breach with the expected party and reason.

## Seat

**The individual** -- a person resident in Canada for 2026, alone or with a spouse or common-law partner, with or without children, who asks: am I resident; what does my return come to; how much OAS must I repay; must I file and by when; must I pay instalments; how much CCB, CWB and GST/HST credit do I get; how long do I have to tell the CRA about a change of spouse. Provisions addressed to the Minister (designations under s 122.5(5), s 122.7(5) and (10); demands under s 150(2); extensions under s 122.62(2)) are asked as facts the person can state. No other seat: the Act puts duties on employers and payers (withholding, s 153) that are outside this baseline.

### Defaults followed and departed from

- **The Act alone, with the instrument that sets its numbers**: followed, with the CRA's table standing in for the s 117.1 and s 122.61(5) adjustments, which no deposited instrument prints. The Regulations are not used (above).
- **Actors the text names**: "the individual", "the individual's guardian, committee or other legal representative" (s 150(1)(d)(i)), the cohabiting spouse or common-law partner, the qualified dependant, the Minister (as the receiver of returns and notices).
- **Judgments left to someone else, conditionally**: residence in the ordinary sense, the primary caregiver of a child (s 122.6 "eligible individual" (b), (f) to (h)), the disability certificate (s 118.3(1)(a.2), (a.3)) and the Minister's designations are asked as facts.
- **Definitions worked out from facts**: "income" (s 3), "taxable income" (s 2(2)), "basic personal amount" (s 118(1.1)), "eligible pension income" (s 118(7)), "working income" and "adjusted net income" (s 122.7(1)), "base taxation year" (s 122.6), "qualified dependant" (s 122.6, s 122.5(1)), "net tax owing" (s 156.1(1)), "balance-due day" (s 248(1)). Borrowed terms (residence, OAS and CPP amounts, EI premiums, CPP contributions, the RRSP deduction limit) are asked.
- **One case**: one individual's taxation year (the calendar year); for the CCB one month, for the GST/HST credit one specified month.
- **Machinery out**: agreements with provinces (ss 122.63, 122.71), Ministers' powers, administration.
- **Departure**: the CPP/EI amounts in s 118.7 are taken as already within the statutory maxima, as the CPP and EI encodings compute them; the cap is not re-applied.

## Scope

**In**: s 2(1), (2); s 3; s 5(1); s 8 (as one deduction figure); s 56(1)(a)(i)(A), (B), (a)(iv), (u); s 60(e.1), (i), (w); s 110(1)(f); s 117(2); s 146(5) (as the lesser of premiums and the limit); s 118(1)(a), (b), (c), (1.1), (2), (3), (4)(a), (5) (as a fact), (7), (8), (10), (11); s 118.3(1); s 118.7(a), (b); s 122.5(1), (2) (as a fact), (3.005), (4.5), (4.6), (5) (as a fact); s 122.6; s 122.61(1); s 122.62(1), (5) to (7); s 122.7(1), (1.3), (2), (3), (5); s 150(1)(d), (1.1)(b); s 156(1); s 156.1(1), (2)(b), (4); s 180.2(1), (2), (5); s 248(1) "appropriate percentage", "balance-due day"; s 250(1), (3); s 257.

**Not covered (explicit answers, asserted)**: taxation years other than 2026; CCB months outside July 2026 to June 2027; GST/HST credit months outside July 2026 to April 2028; non-residents (Division D) and part-year residents (s 114, s 118.91); residents of Quebec at the end of the year for the tax (the s 120(2) abatement); taxable capital gains; the return of a deceased individual (s 150(1)(b), s 70); shared-custody parents (s 122.61(1.1), s 122.5(3.06)); the CWB of a resident of Alberta, Quebec or Nunavut (s 122.71 agreements, not deposited); the CWB disability supplement where D(b) and D(c) both read (finding 4).

**Out (not encoded, no answer)**: s 118(1)(b.1), (d), (e) (caregiver amounts) and D(A)(II) for an infirm child under 18; ss 118.01 to 118.2 (adoption, medical, charitable gifts (the s 118(11) F is taken as nil)), 118.5 to 118.62 (tuition, student loans), 118.8 and 118.9 (transfers), 118.3(2) (a dependant's disability amount); s 117(2.1) and s 122.72 (CWB advance payments); s 122.5(3.1), (3.2) (lump sum when under $50); s 122.61(2) (the under-$20 lump sum); s 180.2(3), (4) (the monthly withholding: its $665 is indexed by s 117.1(2)(t) and the CRA table does not give it); s 164 refunds; s 161 interest and s 162, s 163 penalties; s 120.2 to 127 other credits; the EI benefit repayment under Part VII of the Employment Insurance Act (s 60(v.1)); provincial income tax (the provinces' encodings start from this taxable income).

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code:

- `../../../old-age-security-act/encodings/baseline-2026-10/` (another agent, today) -- the OAS pension, the Guaranteed Income Supplement and the allowances. Their amounts are this encoding's `OAS pension` and `OAS supplement or allowance`; s 56(1)(a)(i)(A) includes them in income, s 110(1)(f) deducts the supplement and allowances, and Part I.2 (s 180.2) claws the pension back. The OAS Act's "income" for the GIS is defined by reference to income under this Act.
- `../../../canada-pension-plan/encodings/baseline-2026-10/` (another agent, today) -- CPP contributions (base contributions under CPP s 8(1) feed s 118.7(b); enhanced contributions under s 8(1.1), (1.2) feed the s 60(e.1) deduction) and CPP benefits (s 56(1)(a)(i)(B)).
- `../../../employment-insurance-act/encodings/baseline-2026-10/` (another agent, today) -- EI premiums (s 118.7(a)) and EI benefits (s 56(1)(a)(iv)); the Part VII benefit repayment, which this encoding does not take.
- `../../../canada-disability-benefit-act/` -- eligibility turns on the s 118.3 disability tax credit certificate that this encoding asks as a fact.
- The provincial and territorial income tax encodings under `../../../<pp>/` -- they start from the taxable income computed here.

The folder names of the three federal benefit encodings are the ones the brief prescribes; check them when those encodings land.

## What the Act turns out to say

1. **The printed dollar amounts are base-year figures from different years, and the consolidation does not say which.** s 117(2)'s thresholds ($57,375, $114,750, $177,882, $253,414) are the CRA's 2025 figures; s 118(1.1)'s A of $12,298 is the 2020 amount; s 118(2) still prints $6,408 and $25,921, s 118.3 $6,000, s 122.61(1) $6,400 and $5,400, s 180.2 $50,000. s 117.1 and s 122.61(5) index each from the year its amending Act set, and those application rules are not in the consolidated text. A reader of the Act alone cannot compute any 2026 amount; the CRA table was deposited so the encoding could use the adjusted figures as a dated table.
2. **A person who owes no tax need not file, but cannot get the benefits without filing.** s 150(1.1)(b) lifts the duty to file unless tax is payable (or a capital gain, an HBP/LLP balance, or a demand). The CCB (s 122.61(1): "have filed a return of income"), the GST/HST credit (s 122.5(3.005): "who files a return of income") and the CWB (s 122.7(2): "who files a return of income") each need a return. Jordan, the single parent, is not required to file and would forgo $2,869 of CWB and the CCB and GST/HST credit by not filing. Asserted.
3. **The GST/HST credit for July 2026 to April 2031 is a new formula, not an indexed one.** s 122.5(3.005) sets $445, $234, $11,564 and $46,432; s 122.5(4.6) deems the old s 122.5(3) amount nil for those months; s 117.1(2)(m.1) indexes the new amounts only for taxation years beginning after 2026. So the months from July 2026 to April 2028 (taxation years 2025 and 2026) use the printed amounts, which match the CRA's 2026 column (where the credit is renamed the "Canada Groceries and Essentials Benefit"). Asserted (Jordan: $339.50 for July 2026).
4. **s 122.7(3) D(b) and D(c) overlap.** D(b) applies where the eligible spouse may not deduct a disability amount "or" the individual has an eligible dependant; D(c) applies where the eligible spouse may deduct one. A couple who both have the disability amount and have an eligible dependant meets both, at 15% and 7.5%. The encoding answers `not covered` rather than choose. Asserted.
5. **The consolidation has no 2025 rate of 14.5%.** s 117(2)(a) reads 14% "for taxation years after 2024", and s 118(11) D gives a 3.45% top-up for 2025. Whatever the 2025 lowest rate was, it is not in the deposited text; this encoding covers 2026 only, where 14% applies and the s 118(11) top-up is 7.14% (which brings credits whose base exceeds the first threshold back towards 15%). Not asserted for 2025; 2026 asserted.
6. **s 110(1)(f) deducts the GIS but not the OAS pension.** It deducts a "social assistance payment made on the basis of a means, needs or income test and included because of clause 56(1)(a)(i)(A)"; of the amounts in that clause only the supplement and the allowances are income-tested. The encoding reads it so. Asserted (OAS 8,900 + GIS 6,000 + CPP 4,000: income 18,900, taxable income 12,900).
7. **The OAS recovery tax is deducted in computing the income that the age amount is tested on.** s 60(w) deducts the Part I.2 tax, and s 180.2's adjusted income adds it back only for Part I.2 itself. For Margaret this lowers her income from 108,900 to 106,863.45 and leaves her $143.28 of age amount. Asserted.
8. **Whether the CWB reduces "net tax owing" for instalments is not clear.** s 156.1(1.1)(b) has the taxes determined "after deducting all tax credits to which the individual is entitled", but the CWB is a deemed payment on account of tax (s 122.7(2)), not styled a credit. The instalment question takes the person's own figures for tax and tax deducted and does not subtract the CWB.
9. **Three provinces' CWB is not the Act's.** s 122.71 lets a province reconfigure the CWB; the CRA table's footnote 8 names agreements with Alberta, Quebec and Nunavut, which are not deposited. The encoding answers `not covered` for those residents. Asserted (Alberta).

## Before relying on it

- Check the hand-worked cases against the CRA's own calculations (T1 and the benefit calculators); none has been.
- Deposit the Income Tax Regulations' Part LXIII factors and the CCB/CWB provincial agreements if the primary-caregiver and province questions are to be worked out rather than asked.
- Add the excluded credits that matter most to members of the public (medical expenses s 118.2, charitable gifts s 118.1, tuition s 118.5, caregiver s 118(1)(d)), the pension-splitting election (s 60.03) and the Quebec abatement.
- Replace the CPP/EI/OAS input amounts with the other encodings' outputs when a cross-folder import exists, and test the joins.
- Add a later CRA column (2027) when it is published, and the 2025 column if the 2025 return is wanted.
- An independent test pass, and the human gates, have not been done.
