# south-africa/

South Africa legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the South African Government website (gov.za), Documents > Acts (run by GCIS); Department of Justice and Constitutional Development Acts list (justice.gov.za); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Nothing is encoded yet. On 2026-10-19 text was deposited for a social security and personal income tax sample (see below); the other subjects are still metadata only.

**Licence category: non-commercial (site terms, met: owner's ruling 2026-10-20); no copyright (statute).** The register's website terms allow only non-commercial use. Section 12(8)(a) of the Copyright Act 98 of 1978 says no copyright subsists in official texts of a legislative, administrative or legal nature. On 2026-10-19 that was confirmed from the Gazette copy of the Act on gov.za (see below). The sample deposited on that date relies on s 12(8)(a). On 2026-10-20 the owner ruled that Legalese Commons counts as non-commercial use, so the sites' non-commercial terms are met as well.

## Topics with no legislation here

- **Passenger compensation**: The only statutory coverage is carrier liability under the Carriage by Air Act, plus general Consumer Protection Act remedies. There is no dedicated statute for air, rail or bus passengers covering compensation for delay, cancellation or denied boarding. Any rules of that kind sit in civil aviation regulations or technical standards, not in primary legislation.

## Social security and personal income tax sample (deposited 2026-10-19)

This sample is meant to let a member of the public work out three things: what grants, unemployment benefits or injury compensation they can get, and how much; what they pay into the UIF; and how much income tax they owe.

### Instruments and why they connect

| Subject | Texts deposited | Why it is here |
| --- | --- | --- |
| `social-assistance-act-13-of-2004` | Act as enacted (2004); Amendment Acts 6 of 2008 and 16 of 2020; Regulations GN R. 2119 of 2022; grant increase notice GN R. 7287 of 23 March 2026 | The grants (older person's, disability, child support, foster child, care dependency, war veteran's, grant-in-aid, social relief of distress). The Act sets eligibility, the 2022 regulations set the means tests, and the 2026 notice sets the amounts: R2 400 for older persons, disability and care dependency; R580 child support; foster child R1 290, then R1 300 from October 2026. |
| `unemployment-insurance-act-63-of-2001` | Act as enacted (2001/2002); Amendment Act 10 of 2016; Labour Laws Amendment Act 10 of 2018 | UIF benefits: unemployment, illness, maternity, adoption, parental and dependant's benefits; the accrual of credits; the income replacement rate (Schedule 2, maximum 60% and minimum 38% after 2016). |
| `unemployment-insurance-contributions-act-4-of-2002` | Act as enacted (2002) | What the employee and employer pay to the UIF (1% each, s 6). The remuneration definition ties it to the Income Tax Act's Fourth Schedule, and SARS collects it. |
| `compensation-for-occupational-injuries-and-diseases-act-130-of` | Act as enacted (1993); Amendment Acts 61 of 1997 and 10 of 2022 (in force in stages from 23 January 2026); GN 4182 of 2026 (pensions up 4.1% from 1 April 2026, and the table of maximum and minimum compensation); GN 3910 of 2026 (maximum assessable earnings R668 000 from 1 March 2026) | Compensation for injury or disease at work, which is the other contributory scheme. Benefits are worked out from earnings, and how they relate to UIF illness benefits matters to the person claiming. |
| `rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026` (new) | Act as enacted (Gazette 54446, 1 April 2026) | The personal income tax table, fixed for years of assessment from 1 March 2025: 18% up to R237 100, rising in steps to 45% above R1 817 000. The table is rebuilt as pipe rows. |
| `income-tax-act-58-of-1962` | **none** | The charging Act: gross income, exemptions, deductions, the rebates in s 6 and PAYE in the Fourth Schedule. No permitted consolidated text exists (see its SOURCE-LICENSE.md). |

**How they interact.** The as-enacted UIA says in s 34 that benefits are not subject to taxation. The amendment history was not checked, and the Income Tax Act exemptions that cover UIF benefits, COIDA compensation and social grants (s 10) are not deposited, so the tax treatment of benefits needs a consolidated Income Tax Act before it is encoded. The grant means tests in the 2022 regulations count income. UIF contributions use the Income Tax Act's definition of "remuneration" (Fourth Schedule) and are collected by SARS through the PAYE system. COIDA compensation replaces the employee's common-law claim against the employer (s 35), and the UIA governs how illness benefits and COIDA benefits overlap.

### Terms

The terms were read on 2026-10-19, before any text was fetched, and are recorded in full in each subject's SOURCE-LICENSE.md:

- **gov.za**: non-commercial informational or reference use only; commercial use needs GCIS written permission. The terms also say they create no contract.
- **parliament.gov.za**: non-commercial informational or reference use. Used only for Act 3 of 2026, which was not on gov.za.
- **justice.gov.za**: same non-commercial terms. Not used for texts.
- **sars.gov.za**: no reproduction or distribution, and no crawlers. Not used.
- **lawlibrary.org.za**: CC BY-NC 4.0, no scraping, `ai-input=no`. Not used.
- **saflii.org**: Cloudflare bot challenge (HTTP 403) on robots.txt. Abandoned without a workaround, so no consolidations were obtained.
- **treasury.gov.za**: terms page unreadable without JavaScript. Not used.

Basis for the deposit: Copyright Act 98 of 1978 s 12(8)(a), read in the Gazette copy at https://www.gov.za/sites/default/files/gcis_document/201504/act-98-1978.pdf.

### Currency

All texts are **as published in the Government Gazette, not consolidated**. Each principal Act's meta file lists the amending Acts that are not applied to it.

| Text | As at |
| --- | --- |
| Grant amounts | 1 April 2026 and 1 October 2026 (notice of 23 March 2026) |
| COIDA compensation maxima and minima | 1 April 2026 (notice of 2 October 2026) |
| COIDA assessable earnings | 1 March 2026 |
| Income tax table | years of assessment from 1 March 2025, still in force on 2026-10-19 unless a 2026 Rates Act has been enacted; a draft 2026 Rates Bill was published on 25 February 2026, and its enactment was not checked |
| 2022 grant regulations | as published on 31 May 2022 |

### Counts

- **Deposited**: 15 texts in 5 subjects, 605,392 characters. That is 6 principal instruments (4 Acts as enacted, the 2022 regulations and the Rates Act), 6 amending Acts and 3 notices that set amounts.
- **Not deposited**:
  - Income Tax Act consolidation (no permitted source).
  - UIF remuneration ceiling notice (GN 475 of 28 May 2021, R17 712 a month; only on treasury.gov.za, whose terms are unreadable, and sars.gov.za).
  - COVID-19 SRD regulations and their 2 April 2026 amendment (image-only scan).
  - Social Assistance Amendment Act 5 of 2010.
  - Unemployment Insurance Amendment Act 32 of 2003.
  - UI Regulations.
  - The 2005 social assistance regulations, which were downloaded but are superseded.

### Gaps and cautions

- **The older Gazette copies are OCR scans**: the 2004, 2001, 2002 and 1993 Acts and the 1997 amendment. Their text has uncorrected OCR errors, and the worked table at the end of UIA Schedule 2 is garbled. Check figures against the PDF.
- **Amending Acts show deletions in [brackets], but insertions are not marked**, because underlining is lost in plain text.
- **There is no consolidation of any of these Acts.** Before encoding, read each principal Act together with its amending Acts, or obtain a consolidation under permitted terms.
