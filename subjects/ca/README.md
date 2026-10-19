# canada/

Canada (federal) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the Justice Laws Website (Department of Justice Canada); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Statute text has since been deposited for five of them, on social security and benefits and on personal income tax (below); nothing is encoded yet.

**Licence category: conditional.** The Reproduction of Federal Law Order (SI/97-5) permits reproduction on two conditions (due diligence over accuracy; not represented as an official version), but does not expressly grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an adaptation. The Department of Justice also publishes the same consolidation as XML at [justicecanada/laws-lois-xml](https://github.com/justicecanada/laws-lois-xml), and that repository is licensed under the Open Government Licence - Canada 2.0, which does permit adaptation, with attribution ("Contains information licensed under the Open Government Licence - Canada.") and without suggesting official status. The deposits below were taken from that repository. **Confirm before quoting text in an encoding** whether the Open Government Licence is to be relied on -- a human decision recorded here.

## Topics with no legislation here

- **Insurance claims**: Insurance contracts and claims (policy conditions, claim handling, auto no-fault) are provincial, in the Insurance Acts and Civil Code of Quebec. The federal Insurance Companies Act (S.C. 1991, c. 47, confirmed on the register) covers only prudential regulation of insurers, not claims.
- **Utility billing**: Electricity, gas and water billing is provincial or municipal. The only federal element is telecom, listed under the Telecommunications Act.
- **Consumer/tenancy**: Residential tenancy is entirely provincial; there is no federal tenancy Act. General consumer protection Acts are also provincial.

## Sourced: social security and benefits, and personal income tax (2026-10-19)

Five federal Acts, each with the regulation that sets the numbers or conditions a person needs, chosen so that a member of the public can be told which federal benefits they can get and how much, and how much federal income tax they owe. Each regulation is deposited in its Act's subject, beside the Act. All ten texts are the Justice Laws consolidation **current to 2026-09-30**, English version, converted from the official XML at repository commit `0507465393c224c0491fc8c17c88340217acc656` ("Laws Site Update 2026-10-15"). Each subject's `SOURCE-LICENSE.md` records the terms read, and each `registers/source-bundle/<id>.meta.json` the URL, dates and sha256 of download and text.

| Subject | Instrument | Citation | Last amended | Characters |
|---|---|---|---|---|
| `canada-pension-plan` | Canada Pension Plan | R.S.C., 1985, c. C-8 | 2024-12-17 | 477,685 |
| | Canada Pension Plan Regulations | C.R.C., c. 385 | 2026-01-01 | 151,436 |
| `old-age-security-act` | Old Age Security Act | R.S.C., 1985, c. O-9 | 2025-10-01 | 171,490 |
| | Old Age Security Regulations | C.R.C., c. 1246 | 2026-06-12 | 55,423 |
| `employment-insurance-act` | Employment Insurance Act | S.C. 1996, c. 23 | 2026-06-18 | 476,140 |
| | Employment Insurance Regulations | SOR/96-332 | 2026-04-01 | 332,948 |
| `income-tax-act` | Income Tax Act | R.S.C., 1985, c. 1 (5th Supp.) | 2026-06-18 | 7,237,487 |
| | Income Tax Regulations | C.R.C., c. 945 | 2026-06-18 | 2,375,829 |
| `canada-disability-benefit-act` | Canada Disability Benefit Act | S.C. 2023, c. 17 | 2024-06-22 | 12,326 |
| | Canada Disability Benefit Regulations | SOR/2025-35 | 2026-09-01 | 40,386 |

The Income Tax Act is deposited whole (14.1 MB of XML, 7.2 million characters of text); so are the Income Tax Regulations.

### Why these connect

- **Income Tax Act** is the hub. It computes the tax a person owes (Division E, s. 117 rates and the s. 118 credits) and also delivers benefits: the **Canada child benefit** (ss. 122.6 to 122.63) is a deemed overpayment of tax, paid monthly and income-tested on adjusted family net income, and the Canada workers benefit and GST/HST credit sit beside it. Its **Part I.2** (s. 180.2) is the **OAS recovery tax** ("clawback") on Old Age Security pension above an income threshold. CPP and OAS benefits and EI benefits are taxable income under it (s. 56), and CPP contributions and EI premiums give credits or deductions.
- **Income Tax Regulations** set withholding at source (Part I) and the prescribed factors for who receives the Canada child benefit (Part LXIII).
- **Old Age Security Act** gives the basic pension, the **Guaranteed Income Supplement** and the allowances; "income" for the GIS is defined by reference to income under the Income Tax Act (s. 2), with CPP and EI contributions deducted. The **Old Age Security Regulations** carry the residence, evidence and indexation rules.
- **Canada Pension Plan** sets contributions on earnings and the retirement, disability, survivor and death benefits; contributions are collected with income tax, and the benefits count as income for OAS/GIS and income tax. The **Canada Pension Plan Regulations** fill in contribution collection and benefit rules.
- **Employment Insurance Act** sets premiums and benefits, and its **Part VII** benefit repayment claws back regular benefits from higher-income claimants through the income tax return. The **Employment Insurance Regulations** fix the regions, regional unemployment rates and earnings rules that, with the Act's Schedule I, decide weeks and amounts of benefit.
- **Canada Disability Benefit Act** is a framework Act; the **Canada Disability Benefit Regulations** set eligibility, amount and the income-tested reduction. Eligibility depends on holding the disability tax credit certificate under s. 118.3 of the Income Tax Act and on filing income tax returns, and the reduction is computed on income as assessed under that Act.

Provincial Acts (provincial income tax, provincial benefits, the Quebec Pension Plan) are not part of this set.

