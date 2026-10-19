# queensland/

Queensland Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register were made with tools that now live outside this repository. Each of those subjects has its text deposited (retrieved 2026-09-22); nothing is encoded yet.

## Social security and benefits, and personal income tax (sourced 2026-10-20)

A Priority 3 sample: the Queensland law a resident meets on these two topics, chosen so that a member of the public could get useful determinations from it. Eleven instruments: two whose text was already here, nine added on 2026-10-20.

### How the set connects to the Commonwealth

Personal income tax and the main social security payments are **Commonwealth** law, already sourced one level up: [`income-tax-assessment-act-1997`](../income-tax-assessment-act-1997/) and [`income-tax-assessment-act-1936`](../income-tax-assessment-act-1936/) (what is taxable income), [`income-tax-rates-act-1986`](../income-tax-rates-act-1986/) and [`medicare-levy-act-1986`](../medicare-levy-act-1986/) (the rates), [`taxation-administration-act-1953`](../taxation-administration-act-1953/) (PAYG withholding, assessments, objections), [`social-security-act-1991`](../social-security-act-1991/) and [`social-security-administration-act-1999`](../social-security-administration-act-1999/) (pensions, allowances, means tests), and [`a-new-tax-system-family-assistance-act-1999`](../a-new-tax-system-family-assistance-act-1999/). Queensland levies no income tax and pays no general income support. What a Queensland resident meets **on top of** the Commonwealth layer is:

- **State benefits** that pay money to an individual: financial assistance to victims of violence, workers' compensation weekly payments and lump sums, and the first home owner grant.
- **State taxes that fall on individuals** rather than businesses: land tax (with the home exemption) and transfer duty (with the home and first home concessions), both administered under one Act.

The two layers, and the Queensland instruments among themselves, touch at named points that an encoding of either side will need:

- **Workers' compensation and social security.** Weekly compensation is "compensation" for the Social Security Act's compensation preclusion and income tests (Social Security Act 1991, Part 3.14), and is assessable income under the ITAA 1997. The Queensland weekly rate is capped and indexed by QOTE (Workers' Compensation Act, s 10A), which the QOTE Notice sets each financial year.
- **Victims assistance and the other schemes.** The Victims of Crime Assistance Act 2009 deals with its relationship to workers' compensation and to motor accident insurance in its Chapter 3 Parts 3 and 3A (pointing at [`workers-compensation-and-rehabilitation-act-2003`](workers-compensation-and-rehabilitation-act-2003/) and [`motor-accident-insurance-act-1994`](motor-accident-insurance-act-1994/)), and reduces assistance by other payments received for the same harm (s 86).
- **The home.** One fact, "this is my home", drives several rules: the land tax home exemption (Land Tax Act 2010, Part 6 Division 1), the transfer duty concessions for homes and first homes (Duties Act 2001, Chapter 2 Part 9), the first home owner grant's residence requirement (FHOG Act, s 15), the Commonwealth CGT main residence exemption (ITAA 1997, Subdivision 118-B) and the principal home's place in the social security assets test (Social Security Act 1991, s 11). The Queensland and Commonwealth definitions are not the same, and an encoding should keep them apart.
- **One revenue administration.** The Taxation Administration Act 2001 names the Duties Act and the Land Tax Act as revenue laws (s 6) and governs their assessments, interest, penalty tax, objections and appeals: it is the Queensland counterpart of the Commonwealth Taxation Administration Act 1953 for these taxes. The first home owner grant is paid by the same Commissioner of State Revenue but carries its own objection and review provisions (FHOG Act, Part 5).

### The instruments

| Subject | Instrument | Topic | Why it is in the set | Version (in force from) | Retrieved | Characters |
|---|---|---|---|---|---|---|
| [`victims-of-crime-assistance-act-2009`](victims-of-crime-assistance-act-2009/) | Victims of Crime Assistance Act 2009 (act-2009-035) | benefits | Financial assistance to primary, parent secondary, witness secondary and related victims, and funeral expenses; Schedule 2 sets the special assistance amounts. | 2024-09-02 | 2026-10-20 | 265,339 |
| [`workers-compensation-and-rehabilitation-act-2003`](workers-compensation-and-rehabilitation-act-2003/) | Workers' Compensation and Rehabilitation Act 2003 (act-2003-027) | benefits | Weekly payments for incapacity, lump sums, QOTE (s 10A). Already deposited; not re-fetched. | 2025-01-01 (still current on 2026-10-20) | 2026-09-22 | see its meta |
| [`workers-compensation-and-rehabilitation-regulation-2025`](workers-compensation-and-rehabilitation-regulation-2025/) | Workers' Compensation and Rehabilitation Regulation 2025 (sl-2025-0116) | benefits | Lump sum and graduated-scale amounts, injury scale values, caring allowance, pneumoconiosis compensation. | 2025-09-01 | 2026-10-20 | 347,327 |
| [`workers-compensation-and-rehabilitation-qote-notice-2026`](workers-compensation-and-rehabilitation-qote-notice-2026/) | Workers' Compensation and Rehabilitation (QOTE) Notice 2026 (sl-2026-0044) | benefits | QOTE for 2026-27: $1,994.50 a week. | 2026-07-01 | 2026-10-20 | 1,808 |
| [`first-home-owner-grant-and-other-home-owner-grants-act-2000`](first-home-owner-grant-and-other-home-owner-grants-act-2000/) | First Home Owner Grant and Other Home Owner Grants Act 2000 (act-2000-014) | benefits / home | Eligibility criteria, amount, residence requirement, objections and repayment of the grant. | 2026-07-01 | 2026-10-20 | 104,327 |
| [`first-home-owner-grant-and-other-home-owner-grants-regulation-2021`](first-home-owner-grant-and-other-home-owner-grants-regulation-2021/) | First Home Owner Grant and Other Home Owner Grants Regulation 2021 (sl-2021-0018) | benefits / home | Further relevant interests in land, persons who are not interested persons, instalment interest. | 2021-03-19 | 2026-10-20 | 6,385 |
| [`land-tax-act-2010`](land-tax-act-2010/) | Land Tax Act 2010 (act-2010-015) | tax | Land tax on individuals, the home exemption, and the individual rate scale with its $600,000 threshold (Schedule 1). | 2025-08-01 | 2026-10-20 | 165,307 |
| [`land-tax-regulation-2021`](land-tax-regulation-2021/) | Land Tax Regulation 2021 (sl-2021-0019) | tax | Primary production activities, eligible-tenant asset and income limits, clearance certificates, instalments. | 2023-07-01 | 2026-10-20 | 6,663 |
| [`duties-act-2001`](duties-act-2001/) | Duties Act 2001 (act-2001-071) | tax | Transfer duty and its concessions for homes, first homes and first home vacant land. Already deposited; not re-fetched. | 2026-08-01 (still current on 2026-10-20) | 2026-09-22 | see its meta |
| [`duties-regulation-2023`](duties-regulation-2023/) | Duties Regulation 2023 (sl-2023-0104) | tax | Transfer duty concessions for electronic (ELN) transfers, fees, other prescribed matters. | 2025-05-01 | 2026-10-20 | 16,415 |
| [`taxation-administration-act-2001`](taxation-administration-act-2001/) | Taxation Administration Act 2001 (act-2001-072) | tax | Assessments, interest, penalty tax, objections and appeals for duty and land tax. | 2025-02-28 | 2026-10-20 | 161,412 |

Characters are of the deposited `.txt`, including the notice at its top. Each new `.meta.json` records the source URL, the version, the retrieval time (UTC), the sha256 of the download and of the text, the character count, and how the text was converted. Regulations and the notice are subjects of their own, each with a `made_under` pointer to its Act.

### Terms read before fetching (2026-10-20)

- **Copyright**, https://www.legislation.qld.gov.au/copyright (page "Last updated 1 July 2022"): "Unless otherwise noted, all copyright material available on or through this website is licensed under a Creative Commons Attribution 4.0 International licence (CC BY 4.0)." Use is permitted "for any purpose, even commercially"; the copyright notice must be kept and the State of Queensland attributed. Changed content must carry: "Based on content from the Queensland Legislation website at [full date of download]. For the latest information on Queensland Government legislation please go to https://www.legislation.qld.gov.au." Excluded from the licence: the coat of arms and logos, trade marks, third-party material, and material under other licences.
- **Disclaimer**, https://www.legislation.qld.gov.au/disclaimer (last updated 1 July 2022): no responsibility for accuracy or completeness; website aids such as links have no legal effect.
- **Authorisation** (status note on each legislation page): PDF versions produced from 23 September 2013 are authorised by the Queensland Parliamentary Counsel. The deposits here come from the HTML view and are unofficial; each says so at its top.
- **robots.txt**, https://www.legislation.qld.gov.au/robots.txt: for all agents, `Disallow: /admin/`, `/view/html/compare/`, `/view/xml/compare` and `/view/pdf/`; eleven named crawlers (GPTBot, Bytespider and others) are blocked entirely; no Crawl-delay. Texts were fetched from the allowed `/view/whole/html/inforce/current/<id>` path, never from `/view/pdf/`, at least 3 seconds apart, under the user agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. Every request returned 200; there was no block or challenge.

The deposited texts are adapted in form (plain text, amendment-history notes and links removed), so each carries the "Based on content from" attribution at its top and in its `SOURCE-LICENSE.md`.

### Gaps

- **Concessions for pensioners and seniors.** Queensland's electricity, water and council-rates rebates for pensioners and seniors, and the Seniors Card, are administrative schemes: no Act or regulation sets their amounts or eligibility, so there is nothing to source. The registration-fee concessions for pensioners sit in the Transport Operations (Road Use Management—Vehicle Registration) Regulation 2021 (sl-2021-0113), not sourced in this pass.
- **Victims assistance amounts.** No regulation under the Victims of Crime Assistance Act 2009 is in force; the special assistance amounts and the caps are in the Act itself.
- **Social housing.** The Housing Act 2003 (act-2003-052) and the Housing Regulation 2026 (sl-2026-0120) govern public housing assistance, but eligibility and rent are set by policy rather than by the instruments; not sourced.
- **Older deposits.** The Duties Act 2001 and Workers' Compensation and Rehabilitation Act 2003 texts are from 2026-09-22 and were converted by an earlier tool: their meta files are in an older shape (no retrieval time, no conversion note) and their texts carry no notice at the top. A check on 2026-10-20 found both still at the version they were taken from.
- The Taxation Administration Regulation 2022 (sl-2022-0108) is left out as administrative.
