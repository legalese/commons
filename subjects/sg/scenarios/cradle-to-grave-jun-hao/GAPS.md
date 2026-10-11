# Gap register for Jun Hao's scenario

What [`SCENARIO.md`](SCENARIO.md) needs that the repository does not hold on 11 October 2026, in the six sections of Simone's register, and a seventh for the seams between the two lives. Statuses were read from `subjects/sg/*/encodings/` on the day; the library gained rows all day while this was written, so run `check-status.py` before trusting anything here.

Entries for the gaps that a simulation would emit are in the requirement ledger at [`../../requirements.jsonl`](../../requirements.jsonl), priority 1, raised by hand and tagged with this scenario's event ids.

## A. Acts the scenario touches that have no encoding row

Only two remain, and neither decides anything in the life.

| Act | where | what to encode |
| --- | --- | --- |
| **Institute of Technical Education Act 1992** | Ch 3 | constitutive; low priority, record as touched |
| **Skills and Workforce Development Agency Act 2026** | Ch 8 (retrenchment at 49) | constitutive; the credit itself is administrative policy |

## B. Encoded Acts where the scenario's question falls outside the row

Ranked by how much of the life turns on them.

| Act and row | what the scenario asks | what the row does not cover |
| --- | --- | --- |
| **Children and Young Persons Act 1993** `naive-2026-10` | which court tries a fifteen-year-old, with what powers, and what it may order instead of a conviction (Ch 2) | the row holds ss 2, 5-8 (protection and offences against children); Part 3, ss 38-48 (the Youth Court: constitution, jurisdiction, procedure, powers on proof of an offence) is the next cut, and the single most consequential gap in this life |
| **Platform Workers Act 2024** `naive-2026-10` | the operator's CPF contribution and the rider's share, phased by birth year (Ch 4) | scoped to coverage; Part 3 (contributions) and the Ninth Schedule's work-injury provisions are outside it. WICA's full row carries the latter |
| **Central Provident Fund Act 1953** `naive-2026-10` | self-employed Medisave liability (Ch 4), Home Protection (Ch 7), CPF LIFE (Ch 9), the platform-worker rates (Ch 4) | the row's standing gap, as in Simone's register: everything from Part 3A on, and the Schedules |
| **Women's Charter 1961** `naive-2026-10` | enforcement of a maintenance order in arrears (Ch 7); division of matrimonial assets (Ch 7, where there are none) | ss 14, 15, 22 were added for Simone's REQ-0005 and REQ-0006; s 71 (enforcement, attachment of earnings) and Part 10 Chapter 4A (division) are not in the row |
| **Casino Control Act 2006** `naive-2026-10` | who may apply for a family exclusion order, on what grounds, and who decides (Ch 8) | the row holds s 162 (terms) and the patron provisions; ss 159-161 and 163A (application, grounds, provisional orders) are outside it. The Committee's decision is a discretion the Act confers, which a row can state but not make |
| **Registration of Births and Deaths Act 2021** `naive-2026-10` | registering the father's particulars when the parents are not married (Ch 5) | the row's sections are 7, 8, 10, 19-23 and the penalties; the unmarried-father provision is outside them |
| **Road Traffic Act 1961** `naive-2026-10` | the Class 2B licence at 18 (Ch 3); speeding and demerit points (Ch 8) | driving offences only; s 63 is encoded only as it feeds the repeat-offender test |
| **Credit Bureau Act 2016** `naive-2026-10` | how long the bureau keeps the Debt Repayment Scheme on his record (Ch 7) | retention periods are in the Act's subsidiary legislation and the bureau's rules |
| **MediShield Life Scheme Act 2015** `naive-2026-10` | what the scheme pays for a three-week stroke admission (Ch 9) | the claim limits are in the MediShield Life Scheme Regulations |
| **Workplace Safety and Health Act 2006** `naive-2026-10` | the employer's duty to the officer who fell on the wet stairwell (Ch 8) | s 12 (employer's duties) is outside the listed sections |
| **Environmental Public Health Act 1987** `naive-2026-10` | licensing of the cleaning business that employs him (Ch 8) | Part 5A is outside the row, which holds public-cleansing offences |
| **Family Justice Act 2014** `naive-2026-10` | the Youth Court as a division of the Family Justice Courts (Ch 2) | Youth Courts are outside the row |
| **Enlistment Act 1970** `naive-2026-10` | enlistment itself at 18 (Ch 3) | s 10 is outside the listed sections; ss 12-15 and 32-33 are in |

## C. Subsidiary legislation the scenario needs

- Moneylenders Rules (the 4% monthly cap and permitted fees) — Ch 4. The cap mechanism is encoded; the number is not.
- Customs (Duties) Order: no duty-free allowance for cigarettes — Ch 4.
- Banking (Credit and Charge Card) Regulations 2013 — Ch 4 (shared with Simone's REQ-0003 class).
- Platform Workers (CPF contributions) regulations and the phase-in by birth cohort — Ch 4.
- Road Traffic (Motor Vehicles, Driving Licences) Rules; the Driver Improvement Points System — Ch 3, 8.
- Insolvency, Restructuring and Dissolution (Debt Repayment Scheme) Regulations: the debt ceiling and the plan's terms — Ch 6.
- Credit Bureau regulations on retention — Ch 7.
- Casino Control (Family Exclusion Orders) regulations and the Committee's procedure — Ch 8.
- Work Injury Compensation (Medical Report) and the assessment guide for permanent incapacity — Ch 4, 8. The Table is encoded; the clinical assessment that feeds it is not law.
- MediShield Life Scheme Regulations (claim limits, premiums, subsidies) — Ch 9.
- CareShield Life (Assessment) regulations: who assesses, and how a borderline activity is scored — Ch 9.
- Silver Support Scheme Regulations: the thresholds and payout amounts — Ch 9.
- Public Trustee rules: the value limit for summary administration — Ch 9.
- Registration of Criminals (Spent Records) rules, if any, on the forms that may and may not ask — Ch 8.

## D. Administrative policy with legal effect and no instrument

| area | the policy | chapter |
| --- | --- | --- |
| MOE | posting groups after PSLE | 1 |
| HDB | the singles scheme: age 35, the $7,000 income ceiling, the Enhanced CPF Housing Grant (Singles), 2-room Flexi lease lengths and the refund of an unexpired lease | 7, 9 |
| MOM and TAFEP | the Tripartite Advisory on retrenchment benefit (the Act sets no amount); Workfare Income Supplement; the Progressive Wage Model for cleaners | 8 |
| MSF | ComCare long-term assistance; the National Council on Problem Gambling's counselling | 8, 9 |
| CPF Board | platform-worker contribution rates; the Matched Retirement Savings Scheme | 4, 8 |
| SkillsFuture Singapore | SkillsFuture Credit at 49 | 8 |

## E. Common law and case law the scenario depends on

| doctrine | where | note |
| --- | --- | --- |
| sentencing of young offenders: when probation rather than a recorded conviction | Ch 2 | the Probation of Offenders Act gives the power; the practice is in the Youth Court's decisions |
| the welfare principle in custody and care and control | Ch 7 | Guardianship of Infants Act s 3 names it; the cases apply it |
| quantum of child maintenance | Ch 7 | Women's Charter s 69 gives the factors; $600 is a figure the court sets |
| residential tenancy | Ch 5, 7 | no statute; the HDB's consent is the only statutory touch |
| whether a lawful act under one Act can be an offence under another: the PAB on the footpath, the cigarettes at the checkpoint | Ch 4 | each is decided inside its own Act; the simulation needs an ordering rule for an act that engages two |
| the clinical judgement behind a statutory test: permanent incapacity percentages, activities of daily living | Ch 4, 8, 9 | not law at all, but the simulation must model it as an input with a declared uncertainty, which is what "flagged for a human" means in practice |

## F. Seams

1. **With Simone's facts.** Their parents' deaths are hers: the will to the mother in 2052, the intestacy in 2060 with equal shares. This file states the same dates and outcomes and adds nothing to hers. The one reach into her life is the family exclusion order she applies for in May 2046, which her facts file does not carry; when the two scenarios are run together the application must appear in both or the interaction is one-sided. Her file should gain the event, not this one lose it.
2. **Two WICA rows.** The full row carries the platform-worker provisions and the 2025 floors and caps; the naive row carries ss 7-16 and the Tables. Chapter 4 needs the full row and Chapter 8 either. Run both and treat a disagreement as a finding.
3. **Two Penal Code rows.** Both carry ss 378-380. Same treatment.
4. **Nature mode's rule, exercised.** Five unlawful acts, each permitted by nature and answered by law. A replay that blocks any of them is wrong; a replay that fails to raise the consequence is wrong too.
5. **Discretion as a first-class outcome.** Two events are decided by a discretion the Act confers on a person: the Official Assignee's suitability determination under the Debt Repayment Scheme, and the Committee's family exclusion order. A row can state the factors and the limits; the simulation must record the decision as a human input, not compute it. The same applies to the two clinical assessments (permanent incapacity; activities of daily living), which are not even law. These are the model for the "human judgement" stops the screenplay is to carry.
