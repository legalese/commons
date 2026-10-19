# tasmania/

Tasmanian Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register are in `tools/topics/`. Until 2026-10-20 no statute text had been deposited; nothing is encoded yet.

## Sourced 2026-10-20: social security and benefits, and personal tax

A Priority 3 sample: fifteen instruments, text deposited, on two topics, chosen so that a Tasmanian resident could get useful determinations. Eight are principal Acts or orders; seven are the regulations that set the numbers a person needs.

### The Australian twist: what is Commonwealth and what is Tasmanian

Personal income tax and the main social security payments are Commonwealth law, and are already sourced beside this folder:
[`income-tax-assessment-act-1997`](../income-tax-assessment-act-1997/), [`income-tax-assessment-act-1936`](../income-tax-assessment-act-1936/), [`income-tax-rates-act-1986`](../income-tax-rates-act-1986/), [`medicare-levy-act-1986`](../medicare-levy-act-1986/), [`social-security-act-1991`](../social-security-act-1991/), [`social-security-administration-act-1999`](../social-security-administration-act-1999/), [`a-new-tax-system-family-assistance-act-1999`](../a-new-tax-system-family-assistance-act-1999/), [`veterans-entitlements-act-1986`](../veterans-entitlements-act-1986/) and [`military-rehabilitation-and-compensation-act-2004`](../military-rehabilitation-and-compensation-act-2004/).
Tasmania levies no income tax and pays no pension of its own. So this sample is the state law a resident meets **on top of** the Commonwealth layer: state payments when something goes wrong (a crime, a work injury, a road accident), state concessions for pensioners and low-income households, and the state taxes and grants that fall on an individual buying or owning a home.

How the layers join:

- **Commonwealth cards open Tasmanian concessions.** The council rates remission (Rates and Charges Remissions Regulations 2024, reg 4), the electricity concessions (Concession Order 2016), the land tax exemption for a pensioner's home (Land Tax Act 2000 s 19(a)-(b), with Land Tax Regulations 2021 reg 5) and the pensioner duty concession (Duties Act 2001 Ch 2 Pt 5 Div 2B) turn on a Pensioner Concession Card or Health Care Card under the Social Security Act 1991, or a DVA card or pension under the Veterans' Entitlements Act 1986 or the Military Rehabilitation and Compensation Act 2004. A Tasmanian determination therefore often starts from a Commonwealth one.
- **Tasmanian compensation feeds back into Commonwealth payments and tax.** Workers compensation weekly payments and MAIB disability allowances replace earnings and are dealt with under Commonwealth income tax law, and compensation from either scheme is "compensation" for the Social Security Act 1991's compensation-recovery and preclusion-period rules. A Tasmanian award can change a Commonwealth pension.
- **Commonwealth indices set Tasmanian numbers.** The maximum rates remission and the victims-of-crime maximum awards are indexed by the Hobart CPI published under the Census and Statistics Act 1905 of the Commonwealth.
- **The tax side connects within the State.** The Duties Act 2001 borrows its "first home" terms from the First Home Owner Grant Act 2000 (a previous grant disqualifies a buyer from the duty concession, s 46C), and the "principal residence land" that the Land Tax Rating Act 2000 rates at nil is classified under the Land Tax Act 2000. The Commonwealth's Help to Buy shared-equity scheme is carved out of the joint-owner rules of the land tax and grant instruments alike.

### The instruments

Benefits and support payments:

| Subject | Source id | Version published | Characters | Why |
|---|---|---|---|---|
| [`victims-of-crime-assistance-act-1976`](victims-of-crime-assistance-act-1976/) | act-1976-032 | 2023-12-08 | 59,059 | Award of compensation to a victim of crime: who may apply, time limits, what is paid. |
| [`victims-of-crime-assistance-regulations-2021`](victims-of-crime-assistance-regulations-2021/) | sr-2021-116 | 2021-12-14 | 11,720 | The maximum awards (primary, secondary, related victims), indexed by Hobart CPI. |
| [`workers-rehabilitation-and-compensation-act-1988`](workers-rehabilitation-and-compensation-act-1988/) | act-1988-004 | 2025-12-01 | 510,993 | Weekly payments and their step-downs, medical and other expenses, impairment and death lump sums. Subject existed; text added. |
| [`workers-rehabilitation-and-compensation-regulations-2021`](workers-rehabilitation-and-compensation-regulations-2021/) | sr-2021-049 | 2022-02-18 | 21,321 | Burial, cremation and counselling maxima, travel rate, hearing-loss table, notice of the right to claim. |
| [`motor-accidents-liabilities-and-compensation-act-1973`](motor-accidents-liabilities-and-compensation-act-1973/) | act-1973-071 | 2026-01-28 | 115,114 | The MAIB no-fault scheme: entitlement to scheduled benefits, exclusions. Subject existed; text added. |
| [`motor-accidents-liabilities-and-compensation-regulations-2020`](motor-accidents-liabilities-and-compensation-regulations-2020/) | sr-2020-007 | 2021-06-15 | 38,486 | Schedule 1: the scheduled benefits themselves (medical, funeral, death, disability allowances, care, counselling). |
| [`local-government-rates-and-charges-remissions-act-1991`](local-government-rates-and-charges-remissions-act-1991/) | act-1991-008 | 2019-05-23 | 19,574 | The pensioner remission of council rates and charges. |
| [`local-government-rates-and-charges-remissions-regulations-2024`](local-government-rates-and-charges-remissions-regulations-2024/) | sr-2024-055 | 2024-10-16 | 7,309 | Who is an "eligible pensioner"; the indexed maximum remission (base for 2024-25: $379.41 for a water and sewerage customer, $558.50 otherwise). |
| [`electricity-supply-industry-concession-order-2016`](electricity-supply-industry-concession-order-2016/) | sr-2016-049 | 2026-07-01 | 32,573 | Annual electricity, life support and medical heating/cooling concessions (daily amounts as set from 1 July 2026); made under s 43D of the [Electricity Supply Industry Act 1995](electricity-supply-industry-act-1995/), which stays indexed only. |

Personal (household) state taxes and grants:

| Subject | Source id | Version published | Characters | Why |
|---|---|---|---|---|
| [`land-tax-act-2000`](land-tax-act-2000/) | act-2000-074 | 2026-10-14 | 109,379 | Liability, principal residence classification, the pensioner exemption (s 19), foreign investor land tax. |
| [`land-tax-rating-act-2000`](land-tax-rating-act-2000/) | act-2000-073 | 2024-07-12 | 6,143 | Nil rate on principal residence land; the Schedule 1 scale for general land. |
| [`land-tax-regulations-2021`](land-tax-regulations-2021/) | sr-2021-096 | 2021-12-01 | 3,491 | DVA gold card (war widow/er) treated as a Pensioner Concession Card for s 19. |
| [`duties-act-2001`](duties-act-2001/) | act-2001-015 | 2026-10-13 | 419,314 | Transfer duty scale; first home buyer concession and exemption; pensioner duty concession; motor vehicle duty. Subject existed; text added. |
| [`first-home-owner-grant-act-2000`](first-home-owner-grant-act-2000/) | act-2000-019 | 2026-10-14 | 82,187 | Eligibility, the grant amount for each period (s 18), residence requirement, repayment. |
| [`first-home-owner-grant-regulations-2021`](first-home-owner-grant-regulations-2021/) | sr-2021-033 | 2026-06-11 | 3,416 | Exclusions from the joint-owner rule (Homes Tasmania; the Commonwealth and Housing Australia under Help to Buy). |

Total: 15 texts, 1,440,079 characters (each count includes the notice block at the head of the file).

### Terms, as read on 2026-10-20

- **Copyright and disclaimer notice**, https://www.legislation.tas.gov.au/copyrightanddisclaimer, read 2026-10-19T17:03:37Z (04:03 AEDT on 20 October); the page says it was last updated on 12 February 2023. Key lines: "Copyright in the material provided on this website is owned by the State of Tasmania." "Unless otherwise noted, all material provided on this website is licensed under a Creative Commons Attribution 4.0 International licence (CC BY 4.0)." "You must keep the copyright notice on the material and attribute the State of Tasmania as the source of the material." Changed material must carry "Based on material from the Tasmanian Legislation website at [full date of download]. For the latest information on Tasmanian Government legislation please go to www.legislation.tas.gov.au." Not under the licence: the coat of arms and government logos, trade-mark material, third-party material, material under other licences.
- **robots.txt**, https://www.legislation.tas.gov.au/robots.txt, read 2026-10-19T17:03:26Z: `User-agent: *` / `Disallow: /admin/`, two sitemaps, no Crawl-delay.
- **How the site was used**: User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` on every request; at least 2 seconds (in practice 3) between requests; no disallowed path requested; no block, challenge or error met. Titles and ids were found through the site's own browse data source (`/projectdata?ds=EnAct-BrowseDataSource`), and texts taken from `/view/whole/html/inforce/current/<id>`. Nine formula images (`/image/*.gif`) were fetched to transcribe them; they are not deposited.
- Each deposited text opens with the copyright notice, the CC BY 4.0 licence, the site's "Based on material ..." attribution (the conversion to plain text changes the form) and an **unofficial version** warning. Each subject's `SOURCE-LICENSE.md` repeats the terms; each `<id>.meta.json` records the URL, version, retrieval time, the SHA-256 of the download and of the text, the character count and the conversion.

### Currency

All texts are the consolidations the site served as current at point in time 2026-10-20, retrieved between 2026-10-19T17:09:34Z and 17:10:42Z. "Version published" above is the site's publication date for that consolidation. Uncommenced amendments are not in a consolidation; the site's uncommenced-legislation feed was not checked.

### Gaps and flags

- **Numbers that live outside the text.** The rates remission maximum and the victims-of-crime maxima are indexed each year by the Hobart CPI; only base figures are in the law, so the current year's figure needs the ABS index. Workers compensation lump sums are multiples of "basic salary", defined as $311.30 for 1991 varied each year by a "relevant percentage", so the current figure is not in the text.
- **Formulas shown as images.** Twelve formulas (nine distinct images) in the Workers Rehabilitation and Compensation Act, the Duties Act, the MAIB Regulations and the Rates Remissions Regulations appear in the source only as images; they are transcribed by hand in square brackets with the image URL and should be checked against the image.
- **Layout quirk.** Where an amendment note attaches to a lettered paragraph, the label can sit on its own line followed by the note and then the text (for example, Land Tax Act s 19(a)).
- **Not sourced, deliberately.** The Electricity Supply Industry Act 1995 itself (an industry Act; only its concession order matters here); the Victims of Crime Compensation Act 1994 (offender compensation orders, not a payment scheme); the Taxation Administration Act 1997 (procedure); the Duties Regulations 2021; and the Duties (Concession Extension) Order 2023, whose two operative clauses are already incorporated in the Duties Act consolidation. Concessions given by policy rather than by an instrument on the statute book are outside this sample.
- **A dangling Commonwealth reference.** The Rates Remissions Regulations cite the Aged Care Act 1997 of the Commonwealth, which has no subject under `subjects/au/`.
