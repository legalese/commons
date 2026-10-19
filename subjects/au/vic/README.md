# victoria/

Victorian Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register are in `tools/topics/`. No statute text has been deposited and nothing is encoded yet.

## Social security and benefits, and personal income tax (indexed 2026-10-20)

A Priority 3 sample: the Victorian law a resident meets on top of the Commonwealth law for these two topics.
On 2026-10-20 eleven instruments were added and the three already here were checked for currency.
**All fourteen are indexed (metadata only); none is sourced.** The reason is the terms, below.

### Why Victorian law, and how it connects to the Commonwealth subjects

In Australia, personal income tax and the main social security payments are Commonwealth law, and those Acts are already sourced in [`subjects/au/`](../):
[`income-tax-assessment-act-1997`](../income-tax-assessment-act-1997/), [`income-tax-assessment-act-1936`](../income-tax-assessment-act-1936/), [`income-tax-rates-act-1986`](../income-tax-rates-act-1986/), [`medicare-levy-act-1986`](../medicare-levy-act-1986/), [`social-security-act-1991`](../social-security-act-1991/), [`social-security-administration-act-1999`](../social-security-administration-act-1999/), [`a-new-tax-system-family-assistance-act-1999`](../a-new-tax-system-family-assistance-act-1999/), [`veterans-entitlements-act-1986`](../veterans-entitlements-act-1986/) and [`first-home-super-saver-tax-act-2017`](../first-home-super-saver-tax-act-2017/).
Victoria levies no income tax and pays no age pension or unemployment payment.
What a Victorian meets on top is of two kinds.

- **State payments**: compensation schemes that pay weekly amounts or lump sums (workers' compensation, transport accident benefits, financial assistance for victims of crime), and concessions on household bills. These connect to the Commonwealth layer in both directions. Compensation payments are income for Commonwealth tax and are caught by the compensation rules of the Social Security Act 1991, which can reduce or preclude a pension; and the Victorian concessions are, as administered, keyed to Commonwealth cards (Pensioner Concession Card and Health Care Card under the social security law, the DVA Gold Card under the veterans' law). Check the exact eligibility links against the texts when they can be read.
- **State taxes that fall on individuals rather than businesses**: land tax (with the principal place of residence exemption), transfer duty on buying a home (first home buyer and pensioner exemptions and concessions), the first home owner grant, and the emergency services levy on every landowner. These connect to each other through one fact pattern (buying, owning and living in a home), are administered together by the State Revenue Office under the Taxation Administration Act 1997 (assessments, objections, review), and meet the Commonwealth layer at the home: the Commonwealth First Home Super Saver scheme funds the same first purchase, and land tax and the levy are deductible under the Income Tax Assessment Act 1997 only for land that produces income.

### The set

Versions read from each landing page's version-history table, 2026-10-19T17:03Z to 17:09Z (2026-10-20, 04:03 to 04:09 AEDT).

| Subject | No. | Current version | Why it is in the set |
|---|---|---|---|
| **Benefits** | | | |
| [`victims-of-crime-financial-assistance-scheme-act-2022`](victims-of-crime-financial-assistance-scheme-act-2022/) | Act 21/2022 | 002, effective 1 Dec 2025 | The financial assistance scheme for victims of crime, in operation from 18 Nov 2024: who may apply and what can be paid. *New.* |
| [`victims-of-crime-financial-assistance-scheme-regulations-2024`](victims-of-crime-financial-assistance-scheme-regulations-2024/) | SR 127/2024 | 001, effective 18 Nov 2024 | Regulations made for the scheme's start; may carry prescribed amounts and procedure (not verified, text unread). *New.* |
| [`workplace-injury-rehabilitation-and-compensation-act-2013`](workplace-injury-rehabilitation-and-compensation-act-2013/) | Act 67/2013 | 054, effective 2 Oct 2026 | Workers' compensation: weekly payments, step-downs, medical and like services, lump sums. *Already here; currency checked.* |
| [`workplace-injury-rehabilitation-and-compensation-regulations-2024`](workplace-injury-rehabilitation-and-compensation-regulations-2024/) | SR 35/2024 | 001, effective 26 May 2024 | The regulations under that Act (content not verified, text unread). *New.* |
| [`transport-accident-act-1986`](transport-accident-act-1986/) | Act 111/1986 | 158, effective 2 Oct 2026 | No-fault benefits after a road accident: loss of earnings, impairment, medical. *Already here; currency checked.* |
| [`transport-accident-regulations-2017`](transport-accident-regulations-2017/) | SR 40/2017 | 002, effective 23 Oct 2018 | The general regulations under that Act (content not verified, text unread). *New.* |
| [`state-concessions-act-2004`](state-concessions-act-2004/) | Act 82/2004 | 003, effective 22 June 2011 | The statutory frame for concessions on energy, water and municipal rates for pensioners and low-income households. *New.* |
| **Personal tax** | | | |
| [`land-tax-act-2005`](land-tax-act-2005/) | Act 88/2005 | 086, effective 1 May 2026 | Land tax, the principal place of residence exemption, the rate scales, vacant residential land tax. *New.* |
| [`land-tax-regulations-2025`](land-tax-regulations-2025/) | SR 149/2025 | 001, effective 16 Dec 2025 | Regulations under the Land Tax Act (content not verified, text unread). *New.* |
| [`duties-act-2000`](duties-act-2000/) | Act 79/2000 | 141, effective 24 June 2026 | Transfer duty on buying a home, with the first home buyer, principal place of residence and pensioner exemptions and concessions. *Already here; currency checked.* |
| [`first-home-owner-grant-and-home-buyer-schemes-act-2000`](first-home-owner-grant-and-home-buyer-schemes-act-2000/) | Act 5/2000 | 053, effective 26 Nov 2025 | The first home owner grant: eligibility, the amount, the residence requirement, repayment. *New.* |
| [`first-home-owner-grant-and-home-buyer-schemes-regulations-2021`](first-home-owner-grant-and-home-buyer-schemes-regulations-2021/) | SR 176/2021 | 002, effective 25 June 2025 | Regulations under the grant Act (content not verified, text unread). *New.* |
| [`emergency-services-and-volunteers-fund-act-2012`](emergency-services-and-volunteers-fund-act-2012/) | Act 58/2012 | 035, effective 1 July 2026 | The levy on every landowner, formerly the Fire Services Property Levy Act 2012 (the site's URL keeps the old name); pensioner concession. *New.* |
| [`taxation-administration-act-1997`](taxation-administration-act-1997/) | Act 40/1997 | 092, effective 26 Nov 2025 | What the State Revenue Office may do to a taxpayer and what the taxpayer may do back: assessments, objections, review, penalty tax, interest. *New.* |

Where the current numbers live: the land tax rate scales are in the Land Tax Act itself; the duty rates and the first home buyer thresholds in the Duties Act; the grant amount in the grant Act.
The indexed amounts of the two compensation schemes (maximum weekly payments, impairment lump sums) are changed each year by notices in the Victoria Government Gazette, not by amending the Acts; those notices are not indexed here (see the terms below).

### Terms (read before any text was requested)

All requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` and at least 3 seconds between requests.

- **legislation.vic.gov.au** -- not openly licensed.
  - https://www.legislation.vic.gov.au/copyright, read 2026-10-19T17:03:22Z: "No part may be reproduced by any process except in accordance with the provisions of the Copyright Act 1968 of the Commonwealth." The Government Printer owns copyright in all Victorian legislation; authorised electronic versions are published under s 62 of the Interpretation of Legislation Act 1984 "for personal use only". Enquiries to the Office of the Chief Parliamentary Counsel, ocpc@ocpc.vic.gov.au. (The same notice was recorded in each existing subject's SOURCE-LICENSE.md on 2026-09-22; it has not changed.)
  - https://www.legislation.vic.gov.au/robots.txt, read 2026-10-19T17:03:09Z: `Crawl-delay: 2`; `Disallow: /oauth/*`, `/preview/*`, `/share-link`; and `Disallow: /sites/default/files/*.pdf`, `*.doc`, `*.xls`, `*.csv`, `*.txt`, `*.ppt`, `*.dot`, `*.tif`, `*.eps`, `*.zip`, `*.ics`, `*.rtf`. The authorised PDF and Word texts are served from `/sites/default/files/`, so a crawler may not fetch them even for reading. Only the landing pages (version histories), the sitemap and the terms pages were fetched.
  - /disclaimer and /authorised-versions were also read: information only, no warranty; an authorised version carries "Authorised Version" at its head and a digital signature.
- **Victoria Government Gazette** (gazette.vic.gov.au), where the annual indexation notices appear -- not openly licensed. robots.txt (read 2026-10-19T17:04:50Z) allows all; the disclaimer page (https://www.gazette.vic.gov.au/gazette_bin/disclaimer.cfm, read 2026-10-19T17:05:17Z) says the Gazette "is subject to copyright. No part may be reproduced by any process except in accordance with the provisions of the Copyright Act 1968." No notice was fetched.
- **AustLII** (austlii.edu.au) -- robots.txt (read 2026-10-19T17:04:18Z) allows `*` but declares `Content-Signal: search=yes,ai-train=no,use=reference`; its copyright and disclaimer pages answered **403** to our User-Agent (2026-10-19T17:04:37Z and 17:04:41Z). We stopped there and fetched nothing else. AustLII does not own the copyright in Victorian legislation in any case, so it could not license it.

### Gaps and flags

- **No text is deposited for any Victorian instrument.** Sourcing needs written permission from OCPC (ocpc@ocpc.vic.gov.au), or a ruling that some statutory exception covers deposit. Both are decisions for a person, not for the fetcher.
- The content notes in the table for the regulations are deliberately hedged: the texts could not be read, so what numbers each regulation sets is not verified.
- **Victims of Crime Assistance Act 1996** (Act 81/1996) is still listed in force (version 070, effective 18 Nov 2024, the day the new scheme began), presumably for applications made before then. Not indexed as a subject; add it if transitional claims matter.
- Not indexed, considered: the Gazette indexation notices for the two compensation schemes; the Housing Act 1983 (public housing rent is set by policy rather than in the Act); the Taxation Administration Regulations 2017 (SR 111/2017, version 002, 3 June 2026); the Accident Compensation Act 1985, which still governs older workplace injuries.
- Commonwealth law is the larger half of both topics; ask questions there first.
