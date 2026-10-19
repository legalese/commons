# united-kingdom/

United Kingdom Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register are in `tools/topics/` (moved to the workbench). Statute text for those Acts was deposited on 2026-09-22 (see each subject's `registers/source-bundle/*.meta.json`), and some now have encodings.

## Benefits and personal income tax: a connected set (sourced 2026-10-19)

Chosen so that one person can get answers across both topics: what benefits can I claim and how much, how much income tax do I owe, and how the two meet (taxable benefits, Universal Credit and earnings, Child Benefit and the High Income Child Benefit Charge, the State Pension).

**Principal Acts**

| Subject | Why it is in the set | Text |
|---|---|---|
| `income-tax-act-2007` | The income tax calculation (s 23), rates and bands, the personal allowance and its taper (s 35) | deposited 2026-09-22 |
| `income-tax-earnings-and-pensions-act-2003` | Tax on employment income, pensions (the State Pension at s 577) and social security income: which benefits are taxable (Table A, s 660) or exempt (Table B, s 677), and the High Income Child Benefit Charge (ss 681B-681H) | deposited 2026-09-22 |
| `income-tax-trading-and-other-income-act-2005` | The rest of a person's taxable income: self-employment profits, property income, savings interest and dividends, and exempt income (Part 6) | **new** |
| `finance-act-2026` | Sets the numbers for the year: charges income tax for 2026-27 and sets its main, default and savings rates (ss 1-3); raises the dividend rates (s 4) | **new** |
| `social-security-contributions-and-benefits-act-1992` | Contributory and non-contributory benefits, NIC classes and contribution conditions, Child Benefit (Part IX) | deposited 2026-09-22 |
| `welfare-reform-act-2012` | Universal Credit (Part 1: entitlement, the award, the earnings deduction, the benefit cap) and Personal Independence Payment (Part 4) | deposited 2026-09-22 |
| `pensions-act-2014` | The new State Pension: qualifying years, full and reduced rates, deferral | deposited 2026-09-22 |
| `state-pension-credit-act-2002` | Pension Credit, the means-tested benefit for people over State Pension age, who are outside Universal Credit | **new** |
| `social-security-administration-act-1992` | Claims, the annual up-rating (s 150), overpayments and recovery | deposited 2026-09-22 |

**Statutory instruments that set the numbers and dates** (all new)

| Subject | Why |
|---|---|
| `universal-credit-regulations-2013` (S.I. 2013/376) | The UC amounts (reg 36 table), work allowance (reg 22), earnings and capital rules, housing costs element |
| `personal-independence-payment-regulations-2013` (S.I. 2013/377) | PIP weekly rates (reg 24) and the activities, descriptors and points (Sch 1) |
| `state-pension-regulations-2015` (S.I. 2015/173) | The detail of the new State Pension under the Pensions Act 2014 |
| `child-benefit-rates-regulations-2006` (S.I. 2006/965) | Weekly Child Benefit rates (enhanced and other); revised to 2026-04-06 |
| `social-security-benefits-up-rating-order-2026` (S.I. 2026/148) | The 2026-27 rates of benefits under the 1992 Act, Pension Credit and UC. The text as made (an amending order; there is no revised version) |

Not taken: the Social Security (Contributions) Regulations 2001 (NIC thresholds; more payroll than personal tax, and very long); the Tax Credits Act 2002 (tax credits ended in April 2025). The Taxes Management Act 1970, Pension Schemes Act 1993 and Pensions Act 2008 are already deposited here.

**Terms read on 2026-10-19, before fetching**

- https://www.legislation.gov.uk/robots.txt -- `User-agent: *`, `Crawl-delay: 5`; disallows `*/data.pdf`, `*/data.docx` and `/defralex`. `data.xml` is not disallowed.
- https://www.legislation.gov.uk/fair-use-policy -- you "must identify yourself ... with a legitimate user agent string"; follow robots.txt and its crawl-delay; no more than 1,500 requests in any 5 minutes; The National Archives "encourage the downloading of data for re-use".
- https://www.legislation.gov.uk/help -- every page: "All content is available under the Open Government Licence v3.0 except where otherwise stated". All Acts are kept up to date. UK SIs made from 1.1.2014 onwards are brought up to date, plus selected older items, mainly DWP ones. Outstanding effects are flagged under "Changes to Legislation".
- https://www.legislation.gov.uk/contributors -- the "otherwise stated" exceptions are EU law derived from EUR-Lex and pre-1987 SIs as made, contributed by Westlaw. Neither applies to anything here.
- https://www.legislation.gov.uk/developer and https://www.legislation.gov.uk/developer/limitations -- the API is free to reuse, and unapplied effects are listed in `<ukm:UnappliedEffects>`. The limitations page also says secondary legislation is not revised. That page is older than the help page, and the data agree with the help page: every SI here except the up-rating order has a revised `dct:valid` date.
- https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ -- a "worldwide, royalty-free, perpetual, non-exclusive licence" to copy, publish, distribute and transmit. Attribution: "Contains public sector information licensed under the Open Government Licence v3.0". Includes a non-endorsement clause.

Every request identified itself as `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, and they were sent one at a time. The first three page fetches were 2 seconds apart, before robots.txt had been read; after that the gap was at least 5 seconds (6 seconds for the data downloads). There were 25 requests to legislation.gov.uk in all, and none was refused.

**Currency.** Each new meta file records `outstanding_effects`, the effects the register lists as in force on or before 2026-10-19 that its editors have not yet applied, and `prospective_unapplied_effects`. On 2026-10-19 the outstanding effects were:

- ITTOIA 2005: 14, including Finance Act 2022 Sch 1 changes to ss 31A-31C from 6 April 2024.
- Universal Credit Regulations: 12. Ten are against the table of contents only; two are against reg 99(6), from the revoked 2024 Administrative Earnings Threshold amendment.
- State Pension Credit Act: 1 (s 3A(5)(a), from 2018).
- PIP Regulations: 1 (Sch 1 Pt 3 table, from 2017).
- The other new items: none.

For the Acts deposited on 2026-09-22, the register's current version date has not changed since deposit. Their contents data list these outstanding effects:

- ITA 2007: 8 (latest due 2019).
- ITEPA 2003: 5 (latest 2021).
- SSCBA 1992: 63 (latest 2024, mostly transitional SIs for legacy benefits).
- SSAA 1992: 21 (latest 2020).
- WRA 2012: 15 (all from the 2012 commencement order).
- Pensions Act 2014: none.
