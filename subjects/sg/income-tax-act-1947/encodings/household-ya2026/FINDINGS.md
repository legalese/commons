# Findings: this encoding against outside referees, and against Lexifina's Singapore model

2026-11-24.
Everything below was measured by running the encoding (`unstable-20261124-9d26421`) and each referee on the same households.
Where the two differ, the Act's text decides: the sections are quoted, and **no encoding figure was changed to match a referee**.
What is kept from the referees is figures, the addresses of IRAS's pages, the names of PolicyEngine-SG's files and variables, and a few short quotations of Lexifina's own findings (a CC0 repository); no sentence of IRAS's pages and no line of PolicyEngine-SG's code is copied here.

## 1. What was run

| referee | what it is | how it was run |
|---|---|---|
| Lexifina's Singapore model | 135 lines of Lean 4 in `lexifina/global-law` (CC0), built from IRAS and CPF Board web pages, "statute, partly official tables"; 5,523 of 11,009 exact against their five software referees | their executable `sgtax` (Lean 4.35.0, built from their clone at 6ae1c2dce06), one JSON household per line; the binary was copied before use |
| PolicyEngine-SG | the open-source Singapore tax and benefit model, clone at 66f5289 (March 2026) | see section 5 |
| IRAS | published tables and worked examples for YA 2026 | see section 4: numbers only, 60 example records |

The grid is 439 households in Lexifina's own input format: single adults aged 25 to 75 on wages from $0 to $2,000,000 (every age at or next to 55, 60, 65, 70), self-employed adults, a parent with up to four children aged 0 to 21, married couples (the second adult's wages $0, $8,000, $8,001 and up), couples with children, investment and rental income, and a spouse with a pension.
Wages are paid evenly over twelve months, as their model does, in whole dollars (the first `wages mod 12` months a dollar more).
Each adult is born in December of the year that gives the stated age at 31 December 2025; the child relief goes to the higher earner, as their model does, so that the question is the law and not the allocation.

## 2. Lexifina's model: 439 households

| | exact | within the dollar (our exact figure less their floored one, under $1 per adult) | differs |
|---|---|---|---|
| income tax | 229 | 198 | 12 |
| employee CPF | 439 | 0 | 0 |

**Employee CPF agrees on every household**: both models stop at the $7,400 Ordinary Wage Ceiling, both phase in from $500 to $750, and both use the 2025 age bands (the above-55 band 17%, above-60 11.5%, above-65 7.5%, above-70 5%).
Where the two disagree on tax, each of the 12 households is one of two kinds, and in both the Act's text decides for this encoding:

1. **A child who is 16 at the end of the year (10 households).**
   Lexifina's model gives qualifying child relief to a child "under 16".
   Section 39(2)(e)(i) gives it to a child "being below 16 years of age at any time during the year preceding the year of assessment", so a child who turns 16 during 2025 qualifies (born in 2009: $4,000, worth $280 to a taxpayer at 7%).
   This is fork H4 and case C2.
2. **A child born in the income year (2 households).**
   Section 42A(2A) gives a rebate of $5,000 against the tax payable, for the year of assessment following the child's birth, for a first child; $10,000 for a second; $20,000 for a third or fourth.
   Lexifina's model has no parenthood rebate, so its tax is $5,000 higher where the tax is large enough to use it (case C11, C12).
   It lists the working mother's child relief as not modelled, and does not mention this rebate.

The difference of cents is rounding: the Act has no rule that rounds tax (a search of the Income Tax Act's text for "round", "nearest dollar" and "fraction of a dollar" finds only the rounding of a prime lending rate to the nearest 0.5% in s 93(11) and nothing about the tax itself; the CPF First Schedule rounds, in para 5(b) and (c), the contributions, not tax), so this encoding is exact to the cent; their model drops the cents of each adult's tax.
**Their F1 is exact here too.**
Earner on $100,000 and a spouse on $8,000 against $8,001: $3,296.80 and $3,492.60, a step of **$195.80**; their S$196 is the same figure rounded (case G1; the scan in section 3).

## 3. Their findings F1, F2, W2-2, and what the Act says

**F1, the spouse relief cliff.**
Their entry says "ITA s. 39 (as published by IRAS)" and calls it new on the evidence of a search.
The provision is s 39(2)(a): a deduction of $2,000 where the individual "had a spouse, living with or maintained by him or her, whose income was ... not more than $8,000 in that year (where the year of assessment is 2025 or any subsequent year of assessment)" (Act 35 of 2024 wef 27/11/2024; it was $4,000 for the years 2010 to 2024, so the cliff is older than the $8,000 figure).
It is one of a family; the Act has the same $8,000 income test, with the same shape of cliff, in
- the child's income, Fifth Schedule para 3B: a child who is not incapacitated is excluded if "his or her income ... exceeded $8,000" (the $4,000 relief is worth $280 to a taxpayer at 7%; case G2);
- the parent's income, s 39(2)(i)(iv): $9,000 is lost (case G3: $560 at 7% and 3.5%);
- the grandparent caregiver's income, s 39(2)(p)(iii)(C): $3,000;
- the spouse's or sibling's income for CPF top-up relief, s 39(3AA)(b)(ii).
None of the four is in their model except the spouse's. Of the four, this encoding has the first three; s 39(3AA) is in no module of the Income Tax Act encoding yet, so the household's top-up inputs must be given after it (NOTES.md section 4).

**F2, the CPF phase-in band.**
The Act: First Schedule paragraph 1(a), second row: for total wages "exceeding $500 but not exceeding $750" the amount recoverable from the employee is "0.6 of the difference between the Total Wages and $500" (and nothing up to $500).
The same figures for older age bands are 0.51, 0.345, 0.225 and 0.15 (2025).
Scanning the encoding and their model together (single adult aged 40, annual wages $5,000 to $10,000 in steps of $50), both give a marginal employee CPF rate of 52% to 72% in 50-dollar steps with an average of 60%, because the monthly amount drops its fraction; the whole-tax-and-CPF marginal rate on annual wages between $6,000 and $9,000 is 59% to 62% in both.
It falls to 19% to 22% from $9,000 (the employee's 20% less the dropped fractions), rises to 25% to 27% from about $52,000 as the 7% band is added to the 20% CPF, and falls to 7% above $88,800 (12 x the $7,400 ceiling), then follows the bands of the Second Schedule.
The two models agree to within 0.2 of a percentage point in every region of a scan of wages from $0 to $400,000 in $500 steps.

**W2-2, PolicyEngine-SG.** See section 5.

## 4. IRAS's published figures and examples

Sixty worked examples were taken from IRAS's own pages on rates, reliefs, rebates and the sample calculations, fetched on 2026-11-24 (the pages are named by their addresses at the end of this section; none of their text is kept here).
Each example's published figures were turned into assertions in `sg-household-tests-iras.l4`: **numbers only, each one named by its example and page**.
The mapping was made by a separate agent from the published pages and the module's input types; no expected figure was edited to match the code.
Where the example gives only a result and the encoding offers only a function that includes it, the assertion is of the result; for the relief arithmetic the figures are asserted both from the Income Tax Act layer (the order of a child, say, supplied) and from the household layer (the order derived).

**The first run, before this section's fixes: 20 of 176 assertions failed.**
Ten were a defect of the household layer, found and fixed in the same session (a mother whose share of the child relief was nil was treated as not maintaining the child, so her working mother's child relief was nil; the case C13 now pins it).
Of the other ten:

| what failed | assertions | the Act | disposition |
|---|---|---|---|
| the $50,000 limit on the reliefs for one child | 4 | Fifth Schedule para 6(2): "all individuals", so every claimant's qualifying child relief counts | **encoding fault, fixed** in `ita-reliefs.l4` (the limit took only the claimant's own share) |
| shared parent relief: IRAS's figure for three claimants of one parent, one of whom lives with the parent | 1 | s 39(2)(i)(vii)(B): where at least one claimant lived with the dependant, the amount shared is the larger one | **encoding fault, fixed** (a new fact on the dependant) |
| NSman relief for a wife who is also a parent, and for an NSman who is also a parent | 2 | s 39(2)(m), (n): one claim excludes the other | **encoding fault, fixed** |
| the order of a mother's children when the first child is barred by Fifth Schedule para 3B | 1 | the Act leaves the ranking to the Comptroller (para 7(b)); para 1 is subject to para 3B yet speaks of "eligible children" | **a fork, labelled H3**: the encoding now counts a child within s 39(2)(e) in the order even when para 3B bars her from a deduction, which is the published example's reading; discriminating case H1 in `sg-household-tests.l4` |
| the employee CPF for a man aged 64 in 2025 on $250,000 | 2 | CPF First Schedule para 1, third column, 2025 bands: 11.5% above 60 to 65, 7.5% above 65 to 70 | **open, not asserted**: the page's relief figure of $7,650 is 7.5% of $102,000, which this encoding gives only to someone aged 65 or over all year (11,730 at 11.5%); the page gives no birth month and no pay layout, so the figure cannot be derived from it. Everything else in that example agrees when its CPF figure is taken as given (relief, chargeable income, tax) |

After the fixes, **174 assertions are satisfied and none fails** (both builds); the mapper counted 7 of the 156 assertions that passed on the first run as vacuous (the example hands the module the rule as an input, so nothing is tested); the file does not mark them and they count for nothing.
Not asserted at all: 27 figures the encoding does not compute (donations, which s 37 governs and this encoding leaves out; the contributions themselves of the self-employed and MediSave, where only the relief arithmetic is encoded; the years of assessment 2023 and earlier, for which the module says it is not encoded), and 13 examples wholly.
The rebate for the same example is shared by IRAS differently from the relief (a couple taking the relief all to the mother and the rebate half each): the household now takes two shares, one for the relief and one for the rebate (fork H2, case H2).

**The net.** IRAS's examples found three real faults that the module's own tests and the independent test pass had both missed, because the published examples contain claimants who share a child or a dependant, and a person who qualifies twice.
They are faults in the Income Tax Act encoding (`../legalese-aswathy/`), where they are fixed with their own assertions and recorded in its `NOTES.md`.

The pages used are under `https://www.iras.gov.sg/taxes/individual-income-tax/` (tax rates, the reliefs index and each relief, the personal and parenthood rebates, the sample calculations, the page for a newborn) and the donations page under `https://www.iras.gov.sg/taxes/other-taxes/charities/`; the YA 2026 tax calculator spreadsheet's macros were not run.

## 5. PolicyEngine-SG

PolicyEngine-SG (commit 66f5289, March 2026) was installed with `uv` into a throwaway virtual environment (Python 3.13.10, policyengine-core 3.37.2 from PyPI, policyengine-sg editable from the local clone), run on the same 439 households, and the environment deleted afterwards.
Its own tests reproduce there (tax 245 with CPF 12,000; and an IRAS-sample case at 26,701.30).
Only the numbers are kept.

**The year convention, which decides how the comparison is read.** PolicyEngine's income tax parameters are keyed by year of assessment, so its period 2026 is YA 2026 (income year 2025); its CPF parameters are keyed by the calendar year, so its period 2025 carries the rates in force in 2025.
It was run that way: tax from period 2026, CPF from period 2025.
At period 2025 (YA 2025) its tax is lower by the personal tax rebate of 60% capped at $200 a person (its `pit_rebate_rate.yaml`: 0.6 at 2025, 0 at 2026), so a grid run at period 2025 would look $200 or $400 better than the Act for YA 2026; it has no YA 2026 rebate, which agrees with the Act.

**Results.**

| | exact (to the cent) | differs |
|---|---|---|
| income tax | 206 | 233 |
| employee CPF | 141 | 298 |

Every difference falls into one of five causes:

1. **PolicyEngine caps employee CPF only at the $102,000 annual ceiling and never at the $7,400 monthly Ordinary Wage Ceiling** (184 households with an adult paid more than $88,800 = 12 x 7,400; CPF and then tax differ in every one).
   Its variable `cpf_employee_contribution` takes the year's income up to the annual ceiling and multiplies it by the rate for the age (`variables/gov/cpf/cpf_employee_contribution.py`, line 22 is the cap), and no variable of the package reads its own parameter for the monthly ceiling (a search of its Python files finds no use).
   The Act's First Schedule para 1, third column, takes "20% of the employee's ordinary wages for the month subject to a maximum of 20% of the Ordinary Wage Ceiling", $7,400 in 2025 (para 5(ea)(iii)).
   On $100,000 of wages PolicyEngine takes $20,000 where the Act takes $17,760; that overstates the CPF relief and understates the tax by $212.60 (a single adult aged 40).
   The gap is $396 at $150,000, $521 at $300,000, and $633.60 at $2,000,000 (ours $434,647.60; theirs $434,014).
2. **PolicyEngine has no nil band and no phase-in** (30 households): up to $500 a month the Act takes nothing from the employee and from $500 to $750 takes 0.6 of the excess over $500 (para 1, third column, first and second rows); PolicyEngine takes the flat rate from the first dollar (an adult on $5,000 a year pays $1,000 there, nothing here; a spouse on $8,000 pays $1,600 there, $1,196 here).
3. **Monthly dropped fractions** (84 households' CPF, 42 households' tax): the Act drops the fraction of a dollar of each month's amount (para 5(c)); PolicyEngine has no monthly step. The differences are under $12 a year of CPF and under $3 of tax a person.
4. **Child relief by age**: PolicyEngine has no child-age test, so the runner kept only children under 16, as Lexifina's model does, and the 16-year-old of H4 differs again (6 households whose difference is not already the CPF ceiling); a household with a child born in 2025 differs by the parenthood rebate, which PolicyEngine has but the runner could not feed (the grid has no field for it).
5. **Interest and dividends** are taxed by PolicyEngine's own headline; a variant with them (and the pension) withheld was used for the households that have them, since bank deposit interest is exempt for an individual (s 13(1)(zd); one-tier dividends were treated the same, and their exemption was not looked up here). This encoding takes exempt income as a given and does not test the exemptions.

**W2-2 in Lexifina's findings** ("PolicyEngine-SG caps ordinary wages at the annual ceiling (software error)") **is confirmed**, with the file and line, and it is bigger than described: the nil band and the phase-in of cause 2 are missing too.
Their remarks on the child relief (who claims it) and on married women's relief are allocation choices; this encoding makes the allocation an input (fork H2).
Where PolicyEngine and the Act agree: earned income relief at 55 (the $6,000 band), spouse relief at an income limit of $8,000, qualifying child relief of $4,000, the relief cap of $80,000 (not reached by this grid), and the Table 3 rates.
None of these differences has been filed upstream: filing an issue with PolicyEngine is an outward action and was not done.

## 6. What this encoding has that their model lacks

Additional wages and the $102,000 annual ceiling (First Schedule paras 2 and 4A); the CPF bands by birth month, not one band for the year; the 2026 vintage as well as 2025; the working mother's child relief in both regimes (Fifth Schedule para 5), with its caps (para 5(3), 6(2)); the parenthood rebate with its carry-forward; parent, sibling, NSman, SRS, CPF top-up and grandparent reliefs; the $5,000 life insurance and CPF rule; "not covered" answers for a non-resident adult, a permanent resident in the first two years, and a year of pay that is not twelve months; exact cents; every figure traced to a section or paragraph.
Their model has what this one does not: 197 other countries, and a test harness against software referees.

## 7. What was not checked

The IRAS calculator's macros; any income year but 2025 and 2026; CPF Board tables (the 2025 employee figures are the Act's, read from SSO's version as at 1 January 2025); couples where both adults are mothers or the spouse relief is claimed twice; the self-employed.
