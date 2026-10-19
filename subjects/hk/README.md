# hong-kong/

Hong Kong SAR legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the Hong Kong e-Legislation (HKeL), Department of Justice; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: not-open.** **Do not deposit statute text here, or quote it in an encoding, without written permission.** The terms allow accurate copying and distribution but grant no right to adapt, and reuse in a product is licensed separately. This directory holds metadata only until permission is obtained.

## Topics with no legislation here

- **Government benefits**: Hong Kong's main cash benefits are administrative schemes funded by Legislative Council appropriation, not statute: Comprehensive Social Security Assistance, the Social Security Allowance Scheme (Old Age Allowance, Old Age Living Allowance, Disability Allowance) and the Working Family Allowance. There is no principal benefits Ordinance to encode; scheme rules are published by the Social Welfare Department and the Working Family and Student Financial Assistance Agency.

## Social security and personal income tax (sourced 2026-10-19)

A connected set for two questions a member of the public asks: *what benefits or contributions apply to me, and how much?* and *how much salaries tax do I owe?*, including where the two meet. **No text has been deposited.** Each instrument was retrieved and its current version identified and hashed. The text was converted only in the fetching session's scratchpad. Each subject's `registers/source-bundle/*.meta.json` records the source URL, version date, retrieval time, sha256 of the download and of the converted text, character count and converter, so a deposit made after a licence decision can be checked against it.

### The instruments, and why they connect

| Subject | Instrument | Kind | Current version | Why it is in the set |
|---|---|---|---|---|
| `inland-revenue-ordinance` | Inland Revenue Ordinance (Cap. 112) | Ordinance | 22 May 2026 | Salaries tax (Part 3: charge s 8, deductions s 12, calculation s 13), the deduction for MPF mandatory contributions (s 26G, capped by Schedule 3B), allowances (Part 5, ss 27-33), personal assessment (Part 7). It also sets the numbers: Schedule 1 standard rate (two tiers from 2024/25: 15% on the first $5,000,000, 16% on the rest), Schedule 2 progressive rates, Schedule 4 allowances, and the one-off reduction Schedules. |
| `mandatory-provident-fund-schemes-ordinance` | Mandatory Provident Fund Schemes Ordinance (Cap. 485) | Ordinance | 5 October 2026 | Who must join and contribute (s 7A), exempt persons (Schedule 1), minimum and maximum relevant income (s 9, Schedules 2 and 3), and s 12A, under which severance and long service payments are paid from accrued benefits. Mandatory contributions are deductible for salaries tax (Cap. 112 s 26G). |
| `mandatory-provident-fund-schemes-general-regulation` (new) | Mandatory Provident Fund Schemes (General) Regulation (Cap. 485A) | subsidiary legislation | 5 October 2026 | When a person can draw their MPF: at 65 (s 159), early retirement at 60 (s 160), death (s 161), permanent departure (s 163), total incapacity (s 164), terminal illness (s 164A), small balance (s 165); lump sum or instalments (ss 35A-35B). |
| `employment-ordinance` | Employment Ordinance (Cap. 57) | Ordinance | 14 May 2026 | Severance payment (Part VA) and long service payment (Part VB), with Part VC. The "transition date" (s 2) and ss 31I, 31Y, 31YAA and 31ZEA give effect to the abolition of offsetting these payments against MPF contributions for service after 1 May 2025, made by 4 of 2022. |
| `comprehensive-social-security-assistance-scheme` (new) | CSSA Scheme, Social Welfare Department | **admin-policy, not statute** | rates from 1 February 2026; pages revised up to 27 July 2026 | The means-tested safety net: residence (1 year), income and asset tests, asset limits, standard rates, supplements and special grants. |
| `social-security-allowance-scheme` (new) | SSA Scheme: Old Age Allowance, Old Age Living Allowance, Disability Allowance, Social Welfare Department | **admin-policy, not statute** | amounts from 1 February 2026; pages revised up to 5 October 2026 | Non-contributory allowances: OAA at 70 (HK$1,675 a month), OALA at 65 with income and asset limits (HK$4,345), Normal and Higher Disability Allowance (HK$2,140 and HK$4,280), Transport Supplement (HK$345), and the Guangdong and Fujian Schemes. |
| `working-family-allowance-scheme` (new) | WFA Scheme, Working Family and Student Financial Assistance Agency | **admin-policy, not statute** | not fetched | A household allowance for low-income working families, with working-hour requirements and income and asset limits. Indexed only: its terms forbid reproduction. |

How they connect: an employee's salary bears MPF mandatory contributions (Cap. 485, with the bands in its Schedules 2 and 3), and the employee's mandatory contributions are deductible for salaries tax up to the Schedule 3B cap (Cap. 112 s 26G). MPF benefits paid on retirement and the other statutory grounds are excluded from salaries tax (Cap. 112 s 8(2)(cb)). When the employment ends, Cap. 57 gives severance or long service payments, which are partly met from MPF benefits for pre-2025 service (Cap. 485 s 12A; Cap. 57 s 31ZEA). The MPF benefits are paid out under Cap. 485A. In old age or need, the non-statutory SWD schemes take over. CSSA and OALA means-test the income and assets that the statutes produce, and receiving one SSA allowance or CSSA excludes the others.

Hong Kong has no contributory social insurance statute. CSSA, the SSA allowances and WFA are administrative schemes funded by Legislative Council appropriation. Their rules and rates are what the department publishes, and they can change without legislation. Appeals go to the Social Security Appeal Board, which is also non-statutory.

### Terms read (2026-10-19)

Every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 2 seconds apart.

- **www.elegislation.gov.hk/robots.txt**: `User-agent: *` / `Allow: /$` / `Allow: /sitemap` / `Disallow: /`. Only named search engines may crawl the site, and there is no Crawl-delay. **Nothing else was requested from HKeL**: not the legislation, the copyright page or the terms page. The HKeL copyright terms in each `SOURCE-LICENSE.md` are those recorded on 2026-09-22.
- **DATA.GOV.HK** (no robots.txt): the Department of Justice publishes HKeL's current legislation as weekly XML zips (dataset `hk-doj-hkel-legislation-current`, last modified 12 October 2026). The files are hosted at resource.data.one.gov.hk, which has no robots.txt. The members needed were read with HTTP Range requests, so the zips (236 MB and 561 MB) were not downloaded whole. Each resource's description links to the **HKeL Terms of Use and Copyright Policy**. The portal's own terms (Version 1.2, 26 May 2025) allow users to "browse, download, distribute, reproduce, hyperlink to, and print the Data for both commercial and non-commercial purposes", with attribution and an indemnity, but say nothing of adaptation. This README takes the HKeL policy to govern.
- **www.swd.gov.hk** (no robots.txt; Important Notices at `/en/importantnotice/`): information "may be re-disseminated or reproduced, provided that the Social Welfare Department (SWD), as the source of information, is acknowledged and that the re-dissemination or reproduction is for non-commercial use". Commercial reproduction or adaptation needs SWD's written authorisation.
- **www.wfsfaa.gov.hk** (no robots.txt; `/en/important_notices.htm`): reproduction, adaptation, distribution or making available to the public is prohibited without WFSFAA's written authorisation. Download is allowed only for personal or non-commercial internal use.
- **www.ird.gov.hk** (no robots.txt; `/eng/notices.htm`; read, but nothing taken from IRD, because the rates and allowances are in Cap. 112 itself): commercial reproduction is prohibited without IRD's written authorisation, and non-commercial re-dissemination is allowed with acknowledgement.

### Currency

Statute versions are the HKeL version dates in the XML (`dc:date`): Cap. 112 22 May 2026; Cap. 57 14 May 2026; Cap. 485 and Cap. 485A 5 October 2026. All are "In effect". SWD rates and limits are those effective from 1 February 2026. Each page's own revision date is recorded in its meta file.

### Gaps and flags

- **Licence.** Nothing here is cleared for deposit. Depositing the four statutes needs either written permission from the Department of Justice (HKeL), or a recorded decision that the DATA.GOV.HK terms permit it despite the dataset's pointer to the HKeL policy. The SWD texts need a decision on non-commercial-only terms, or SWD's authorisation. WFA needs WFSFAA's authorisation.
- **HKeL robots.txt** excludes all but named search engines. The 2026-09-22 index records say HKeL pages were checked in a browser pane; future checks should use the DATA.GOV.HK XML route.
- **WFA rules and rates** were not fetched (terms).
- **Not in the set:** the Protection of Wages on Insolvency Ordinance (Cap. 380, version 1 May 2025; an indexed subject here) and the Employees' Compensation Ordinance (Cap. 282) also pay statutory benefits but are outside these two questions. The Guangdong and Fujian Scheme sub-sites, and SWD's Support for Self-reliance Scheme rules for able-bodied CSSA recipients, were not read.
- **Chinese text.** Only the English texts were read. English and Chinese texts of an Ordinance are equally authentic.
