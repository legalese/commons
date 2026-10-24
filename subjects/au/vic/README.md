# victoria/

Victorian Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register are in `tools/topics/`. No statute text has been deposited and nothing is encoded yet.

## Social security and benefits, and personal income tax (indexed 2026-10-20)

A Priority 3 sample: the Victorian law a resident meets on top of the Commonwealth law for these two topics.
On 2026-10-20 eleven instruments were added and the three already here were checked for currency.
**All fourteen are indexed (metadata only); none is sourced.** The reason was first the terms, below.
Since 24 October 2026 the owner's ruling allows deposit (see the terms), but robots.txt still keeps a fetcher off the files that hold the texts, so they wait to be saved by hand (see [Sourcing, 2026-10-24](#sourcing-2026-10-24)).
One instrument outside the fourteen is sourced: the workers' compensation indexation notice for 1 July 2026, from the Government Gazette.

### Why Victorian law, and how it connects to the Commonwealth subjects

In Australia, personal income tax and the main social security payments are Commonwealth law, and those Acts are already sourced in [`subjects/au/`](../):
[`income-tax-assessment-act-1997`](../income-tax-assessment-act-1997/), [`income-tax-assessment-act-1936`](../income-tax-assessment-act-1936/), [`income-tax-rates-act-1986`](../income-tax-rates-act-1986/), [`medicare-levy-act-1986`](../medicare-levy-act-1986/), [`social-security-act-1991`](../social-security-act-1991/), [`social-security-administration-act-1999`](../social-security-administration-act-1999/), [`a-new-tax-system-family-assistance-act-1999`](../a-new-tax-system-family-assistance-act-1999/), [`veterans-entitlements-act-1986`](../veterans-entitlements-act-1986/) and [`first-home-super-saver-tax-act-2017`](../first-home-super-saver-tax-act-2017/).
Victoria levies no income tax and pays no age pension or unemployment payment.
What a Victorian meets on top is of two kinds.

- **State payments**: compensation schemes that pay weekly amounts or lump sums (workers' compensation, transport accident benefits, financial assistance for victims of crime), and concessions on household bills. These connect to the Commonwealth layer in both directions. Compensation payments are income for Commonwealth tax and are caught by the compensation rules of the Social Security Act 1991, which can reduce or preclude a pension; and the Victorian concessions are, as administered, keyed to Commonwealth cards (Pensioner Concession Card and Health Care Card under the social security law, the DVA Gold Card under the veterans' law). Check the exact eligibility links against the texts when they can be read.
- **State taxes that fall on individuals rather than businesses**: land tax (with the principal place of residence exemption), transfer duty on buying a home (first home buyer and pensioner exemptions and concessions), the first home owner grant, and the emergency services levy on every landowner. These connect to each other through one fact pattern (buying, owning and living in a home), are administered together by the State Revenue Office under the Taxation Administration Act 1997 (assessments, objections, review), and meet the Commonwealth layer at the home: the Commonwealth First Home Super Saver scheme funds the same first purchase, and land tax and the levy are deductible under the Income Tax Assessment Act 1997 only for land that produces income.

### The set

Versions read from each landing page's version-history table, 2026-10-19T17:03Z to 17:09Z (2026-10-20, 04:03 to 04:09 AEDT).
Read again 2026-10-24T04:26Z to 04:29Z: every current version is unchanged.
The fifteenth row, the Gazette notice, was added on 2026-10-24.

| Subject | No. | Current version | Why it is in the set |
|---|---|---|---|
| **Benefits** | | | |
| [`victims-of-crime-financial-assistance-scheme-act-2022`](victims-of-crime-financial-assistance-scheme-act-2022/) | Act 21/2022 | 002, effective 1 Dec 2025 | The financial assistance scheme for victims of crime, in operation from 18 Nov 2024: who may apply and what can be paid. *New.* |
| [`victims-of-crime-financial-assistance-scheme-regulations-2024`](victims-of-crime-financial-assistance-scheme-regulations-2024/) | SR 127/2024 | 001, effective 18 Nov 2024 | Regulations made for the scheme's start; may carry prescribed amounts and procedure (not verified, text unread). *New.* |
| [`workplace-injury-rehabilitation-and-compensation-act-2013`](workplace-injury-rehabilitation-and-compensation-act-2013/) | Act 67/2013 | 054, effective 2 Oct 2026 | Workers' compensation: weekly payments, step-downs, medical and like services, lump sums. *Already here; currency checked.* |
| [`workplace-injury-rehabilitation-and-compensation-regulations-2024`](workplace-injury-rehabilitation-and-compensation-regulations-2024/) | SR 35/2024 | 001, effective 26 May 2024 | The regulations under that Act (content not verified, text unread). *New.* |
| [`workers-compensation-annual-indexation-notice`](workers-compensation-annual-indexation-notice/) | Gazette S 363/2026 | 30 June 2026, rates from 1 July 2026 | The indexed amounts under that Act (maximum weekly payments, death benefits, impairment lump sums, damages thresholds), with the Accident Compensation Act 1985 and Workers Compensation Act 1958 notices in the same Gazette. *Added 2026-10-24; text deposited.* |
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
The indexed amounts of the two compensation schemes (maximum weekly payments, impairment lump sums) change each year without amending the Acts.
For workers' compensation the indexed amounts are published each June in a notice in the Victoria Government Gazette; the notice for 1 July 2026 is deposited in [`workers-compensation-annual-indexation-notice`](workers-compensation-annual-indexation-notice/).
For transport accidents no Gazette notice for 1 July 2026 was found (see Sourcing, below).

### Terms (read before any text was requested)

All requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` and at least 3 seconds between requests.

- **legislation.vic.gov.au** -- not openly licensed.
  - https://www.legislation.vic.gov.au/copyright, read 2026-10-19T17:03:22Z: "No part may be reproduced by any process except in accordance with the provisions of the Copyright Act 1968 of the Commonwealth." The Government Printer owns copyright in all Victorian legislation; authorised electronic versions are published under s 62 of the Interpretation of Legislation Act 1984 "for personal use only". Enquiries to the Office of the Chief Parliamentary Counsel, ocpc@ocpc.vic.gov.au. (The same notice was recorded in each existing subject's SOURCE-LICENSE.md on 2026-09-22; it has not changed.)
  - https://www.legislation.vic.gov.au/robots.txt, read 2026-10-19T17:03:09Z: `Crawl-delay: 2`; `Disallow: /oauth/*`, `/preview/*`, `/share-link`; and `Disallow: /sites/default/files/*.pdf`, `*.doc`, `*.xls`, `*.csv`, `*.txt`, `*.ppt`, `*.dot`, `*.tif`, `*.eps`, `*.zip`, `*.ics`, `*.rtf`. The authorised PDF and Word texts are served from `/sites/default/files/`, so a crawler may not fetch them even for reading. Only the landing pages (version histories), the sitemap and the terms pages were fetched.
  - /disclaimer and /authorised-versions were also read: information only, no warranty; an authorised version carries "Authorised Version" at its head and a digital signature.
- **Victoria Government Gazette** (gazette.vic.gov.au), where the annual indexation notices appear -- not openly licensed. robots.txt (read 2026-10-19T17:04:50Z) allows all; the disclaimer page (https://www.gazette.vic.gov.au/gazette_bin/disclaimer.cfm, read 2026-10-19T17:05:17Z) says the Gazette "is subject to copyright. No part may be reproduced by any process except in accordance with the provisions of the Copyright Act 1968." No notice was fetched.
- **AustLII** (austlii.edu.au) -- robots.txt (read 2026-10-19T17:04:18Z) allows `*` but declares `Content-Signal: search=yes,ai-train=no,use=reference`; its copyright and disclaimer pages answered **403** to our User-Agent (2026-10-19T17:04:37Z and 17:04:41Z). We stopped there and fetched nothing else. AustLII does not own the copyright in Victorian legislation in any case, so it could not license it.

#### Owner's ruling, 24 October 2026

These terms were put to Michael, the owner of Legalese Commons, with the warning that nothing could be deposited without permission.
They were the Government Printer's notice above (no reproduction except in accordance with the Copyright Act 1968; authorised electronic versions "for personal use only") and the Gazette's copyright notice.
On 24 October 2026 he answered, in chat:

> "On NT, Vic and SA, yes please go ahead."

**The ruling:** Legalese Commons may deposit Victorian legislation and quote it in L4 encodings, keeping the copyright notice, the Government Printer's attribution and a notice that the version is unofficial.
The Victoria Government Gazette's notices, including the annual indexation notices, come under the same ruling.
The ruling is about the licence only. **It does not lift robots.txt:** nothing is fetched from a path that robots.txt disallows.
The ruling is recorded in the SOURCE-LICENSE.md of each of the fifteen subjects in the table above.
It covers the other thirteen Victorian subjects here too (payroll tax, tenancies and the rest).
Their SOURCE-LICENSE.md files were not changed on 2026-10-24 and still carry the earlier "do not deposit" wording; the ruling replaces that wording.

Terms read again on 2026-10-24, same User-Agent, at least 3.5 seconds between requests:

- https://www.legislation.vic.gov.au/copyright, read 2026-10-24T05:01:15Z: the same wording as on 2026-10-19.
- https://www.legislation.vic.gov.au/robots.txt, read 2026-10-24T04:20:18Z: the same as on 2026-10-19 (`Crawl-delay: 2`; `/sites/default/files/*.pdf`, `*.doc`, `*.rtf`, `*.txt` and the other file types disallowed).
- The PDF and Word links on each version page point to **content.legislation.vic.gov.au**, a second host. Its robots.txt (https://content.legislation.vic.gov.au/robots.txt, read 2026-10-24T04:29:38Z) has `User-agent: *` and `Disallow: /`, so a crawler may fetch nothing at all there.
- https://www.gazette.vic.gov.au/robots.txt, read 2026-10-24T04:30:02Z: `User-agent: *`, `Allow: /`. The Gazette disclaimer, read 2026-10-24T05:01:21Z, has the same copyright wording as on 2026-10-19.

### Sourcing, 2026-10-24

**Deposited (one subject):**

- [`workers-compensation-annual-indexation-notice`](workers-compensation-annual-indexation-notice/), file `registers/source-bundle/GG2026S363.txt`.
  It is Victoria Government Gazette No. S 363 of Tuesday 30 June 2026, from https://www.gazette.vic.gov.au/gazette/Gazettes2026/GG2026S363.pdf, retrieved 2026-10-24T04:42:30Z.
  The whole 20-page issue is deposited: the Accident Compensation Act 1985 notice (pages 1-8), the Workers Compensation Act 1958 notice (pages 9-10) and the Workplace Injury Rehabilitation and Compensation Act 2013 notice (pages 11-18).
  It was converted with pdftotext -table, so each row keeps its section, provision and both rates (before and from 1 July 2026) on one line.
  The copyright notice, the Government Printer's attribution and an unofficial-version notice head the file. Hashes and the line range of each notice are in its `.meta.json`.
  *Currency:* rates from 1 July 2026; a new notice is due for 1 July 2027 and goes beside this one as a new file.
  The notice says weekly payments "are indexed on the anniversary of the entitlement to weekly payments", so the date that matters for a worker's own weekly payment is that anniversary.

**How the notice was found.** The Gazette's archive page lists each 2026 issue by number and date only.
Its search is a POST form, which was not used.
So every General Gazette G17 to G30 (23 April to 23 July 2026) and every Special Gazette S260 to S402 (26 May to 10 July 2026) was downloaded and read: 157 PDFs.
The workers' compensation notice is in S 363.
**No Transport Accident Act notice of indexed amounts for 1 July 2026 was found in that range.**
There are three possibilities: the Transport Accident Commission does not gazette its indexation, it gazetted outside those dates, or its notice does not contain the words "transport accident", which each issue's text was searched for. The Act's text, once deposited, will show whether a Gazette notice is required.
Until then, the transport accident encoding has to take the indexed amounts as inputs.

**Not deposited (all fourteen in the set), because of robots.txt.**
Neither the landing pages nor the version pages render the text of an Act or statutory rule: they carry the version history and links to the files.
The text exists only in the authorised PDF and the Word file under `/sites/default/files/`, served from content.legislation.vic.gov.au, which robots.txt disallows on both hosts.
None was fetched.
Each subject's SOURCE-LICENSE.md and `.meta.json` (`recheck_2026_10_24.hand_download`) list the files.
Saved by hand into `C:\Users\micha\Downloads\vic-legislation`, they can be converted and deposited under the ruling. These are the current versions as read on 2026-10-24:

| Subject | Version | Word file | Authorised PDF |
|---|---|---|---|
| `victims-of-crime-financial-assistance-scheme-act-2022` | 002, 1 Dec 2025 | https://content.legislation.vic.gov.au/sites/default/files/2025-12/22-21a002.docx | https://content.legislation.vic.gov.au/sites/default/files/2025-12/22-21aa002-authorised.pdf |
| `victims-of-crime-financial-assistance-scheme-regulations-2024` | 001, 18 Nov 2024 | https://content.legislation.vic.gov.au/sites/default/files/2024-11/24-127sr001.docx | https://content.legislation.vic.gov.au/sites/default/files/2024-11/24-127sra001-authorised.pdf |
| `workplace-injury-rehabilitation-and-compensation-act-2013` | 054, 2 Oct 2026 | https://content.legislation.vic.gov.au/sites/default/files/2026-10/13-67a054.docx | https://content.legislation.vic.gov.au/sites/default/files/2026-10/13-67aa054-authorised.pdf |
| `workplace-injury-rehabilitation-and-compensation-regulations-2024` | 001, 26 May 2024 | https://content.legislation.vic.gov.au/sites/default/files/2024-05/24-35sr001.docx | https://content.legislation.vic.gov.au/sites/default/files/2024-05/24-35sra001-authorised.pdf |
| `transport-accident-act-1986` | 158, 2 Oct 2026 | https://content.legislation.vic.gov.au/sites/default/files/2026-10/86-111a158.docx | https://content.legislation.vic.gov.au/sites/default/files/2026-10/86-111aa158-authorised.pdf |
| `transport-accident-regulations-2017` | 002, 23 Oct 2018 | https://content.legislation.vic.gov.au/sites/default/files/6cfa1271-b08c-36b7-9474-03ccbf778d7a_17-40sr002.docx | https://content.legislation.vic.gov.au/sites/default/files/ffee8252-91f8-3920-98c5-7e21c78a89d4_17-40sra002%20authorised.pdf |
| `state-concessions-act-2004` | 003, 22 June 2011 | https://content.legislation.vic.gov.au/sites/default/files/50b02137-7372-3c4c-80ce-774c24f9a9eb_04-82a003.docx | https://content.legislation.vic.gov.au/sites/default/files/175ee2b5-f4a6-3a2c-a288-16de746d15b8_04-82aa003%20authorised.pdf |
| `land-tax-act-2005` | 086, 1 May 2026 | https://content.legislation.vic.gov.au/sites/default/files/2026-05/05-88a086.docx | https://content.legislation.vic.gov.au/sites/default/files/2026-05/05-88aa086-authorised.pdf |
| `land-tax-regulations-2025` | 001, 16 Dec 2025 | https://content.legislation.vic.gov.au/sites/default/files/2025-12/25-149sr001.docx | https://content.legislation.vic.gov.au/sites/default/files/2025-12/25-149sra001-authorised.pdf |
| `duties-act-2000` | 141, 24 June 2026 | https://content.legislation.vic.gov.au/sites/default/files/2026-06/00-79a141.docx | https://content.legislation.vic.gov.au/sites/default/files/2026-06/00-79aa141-authorised.pdf |
| `first-home-owner-grant-and-home-buyer-schemes-act-2000` | 053, 26 Nov 2025 | https://content.legislation.vic.gov.au/sites/default/files/2025-11/00-5a053.docx | https://content.legislation.vic.gov.au/sites/default/files/2025-11/00-5aa053-authorised.pdf |
| `first-home-owner-grant-and-home-buyer-schemes-regulations-2021` | 002, 25 June 2025 | https://content.legislation.vic.gov.au/sites/default/files/2025-06/21-176sr002.docx | https://content.legislation.vic.gov.au/sites/default/files/2025-06/21-176sra002-authorised.pdf |
| `emergency-services-and-volunteers-fund-act-2012` | 035, 1 July 2026 | https://content.legislation.vic.gov.au/sites/default/files/2026-07/12-58a035.docx | https://content.legislation.vic.gov.au/sites/default/files/2026-07/12-58aa035-authorised.pdf |
| `taxation-administration-act-1997` | 092, 26 Nov 2025 | https://content.legislation.vic.gov.au/sites/default/files/2025-11/97-40a092.docx | https://content.legislation.vic.gov.au/sites/default/files/2025-11/97-40aa092-authorised.pdf |

Saving the Word file is enough for conversion. The authorised PDF is the version to check the conversion against.
A version page also lists a bookmarked PDF for the State Concessions Act, which is not needed.

### Gaps and flags

- **No Act or statutory rule text is deposited.** Until 2026-10-24 the obstacle was the terms; the owner's ruling of that day removed it. What remains is robots.txt, which the ruling does not lift: the files listed under Sourcing must be saved by hand before they can be converted and deposited. The only Victorian text deposited is the Gazette notice in `workers-compensation-annual-indexation-notice`.
- The content notes in the table for the regulations are deliberately hedged: the texts could not be read, so what numbers each regulation sets is not verified.
- **Victims of Crime Assistance Act 1996** (Act 81/1996) is still listed in force (version 070, effective 18 Nov 2024, the day the new scheme began), presumably for applications made before then. Not indexed as a subject; add it if transitional claims matter.
- The Transport Accident Act's indexed amounts for 1 July 2026 were not found in the Gazette (see Sourcing). The workers' compensation notice is now indexed and deposited.
- Not indexed, considered: the Housing Act 1983 (public housing rent is set by policy rather than in the Act); the Taxation Administration Regulations 2017 (SR 111/2017, version 002, 3 June 2026); the Accident Compensation Act 1985, which still governs older workplace injuries.
- Commonwealth law is the larger half of both topics; ask questions there first.
