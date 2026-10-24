# northwest-territories/

Northwest Territories (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Legislation of the Northwest Territories - the consolidated statutes and regulations service of the Legislation Division, Department of Justice, Government of the Northwest Territories; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited at that date. Since 2026-10-20 seven texts on social security and personal income tax have been deposited; see the update at the end. Nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over plain HTTPS with an honest, self-identifying user agent ('canon-legislation-indexer/1.0 (legislation metadata indexing; contact address removed)'). No block, no bot challenge, no rate limiting, no CAPTCHA - every request returned 200. About 14 requests in total, spaced roughly 2 seconds apart: the A-Z index page (one page, 739 KB, carrying all 239 consolidated Acts plus their regulations as a file-browser list), both paginated halves of the site's terms of use (/en/terms-of-use/ and /en/terms-of-use/page/2/), the 'Acts of the Northwest Territories - Administering Departments' table (dated October 13, 2025), and the consolidated PDFs of the nine Acts listed below plus the Official Languages Act. The register publishes each consolidation only as a PDF; there is no per-Act HTML page. The index shows, for each consolidation, a 'Modified Date' - the date of that consolidation - and each PDF's cover page prints the Act's chapter citation, its commencement, and the full chain of amending chapters with their in-force dates. The site's own disclaimer states that 'These consolidations are updated monthly and may not be the most current version available' and that the consolidations 'have been prepared for convenience of reference only, and are not an official statement of the law'; the authoritative text is the Revised Statutes of the Northwest Territories, 1988 and the Annual Volumes of the Statutes of the Northwest Territories. CanLII was not used (it refuses this network).

## Topics with no legislation here

- **Passenger compensation**: Federal, not territorial. Air carriers and passenger compensation are governed by the Canada Transportation Act, S.C. 1996, c. 10 and the Air Passenger Protection Regulations, SOR/2019-150, administered by the Canadian Transportation Agency; interprovincial and international rail and bus carriage is likewise federal. The register's Motor Vehicles Act and Public Airports Act regulate vehicles and airport operations, not compensation for delayed or denied carriage.
- **Customs/duties**: Federal and exclusive. Constitution Act, 1867, s. 91(2)-(3) reserves trade and commerce and the raising of money by customs duties to Parliament; the operative statutes are the Customs Act, R.S.C. 1985, c. 1 (2nd Supp.) and the Customs Tariff, S.C. 1997, c. 36. A territory cannot legislate customs duties.
- **Work permits/immigration**: Federal. Entry, status and work authorisation are governed by the Immigration and Refugee Protection Act, S.C. 2001, c. 27 and the Immigration and Refugee Protection Regulations, SOR/2002-227. The Northwest Territories Nominee Program operates administratively under a federal-territorial immigration agreement; there is no territorial immigration statute on the register.

## Update 2026-10-20: owner's ruling, and the social security and income tax sample

**Licence decision (owner's ruling, 2026-10-20):** Legalese Commons counts as non-commercial use of the register's texts, so they may be deposited. The terms, re-read on 2026-10-20 at <https://www.justice.gov.nt.ca/en/terms-of-use/page/2/>, say: "Material may not be used or reproduced for commercial purposes without the prior written consent arranged by the Department's Communications Unit. If it is reproduced or redistributed for non-commercial purposes, the Government of the Northwest Territories copyright is to be acknowledged." Page 1 of the terms (<https://www.justice.gov.nt.ca/en/terms-of-use/>) is a disclaimer and a governing-law clause. The terms do not mention adaptation. The "Licence category: unclear / Metadata only" paragraph above is the record of 2026-09-23. The ruling replaces it for the subjects listed below. Every deposited text starts with the GNWT copyright acknowledgement and an "unofficial version" notice. Commercial use of these texts still needs the Department's written consent.

**Access, 2026-10-20.** User agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 2.5 s between requests, 11 requests in total, all 200: robots.txt, both pages of the terms, the A-Z listing at `/en/legislation/`, and seven PDFs. robots.txt (`User-agent: *`) disallows only `*.ind`, `/app/`, `/wp/wp-admin/`, `/wp/wp-login.php` and the French duplicate paths under `/fr/fichiers/`. `/en/files/legislation/` is allowed, and there is no crawl-delay. There was no block, challenge or rate limit.

### What was sourced (Priority 3 sample: social security and benefits, personal income tax)

| Subject | Instrument | Citation | Consolidation date (register) | Text file |
|---|---|---|---|---|
| `income-tax-act` (existing) | Income Tax Act | R.S.N.W.T. 1988, c.I-1 | 2023-11-23 | `income-tax.a.2023-11-23.txt` |
| `income-tax-regulations` (new) | Income Tax Regulations | R.R.N.W.T. 1990, c.I-1 | 2025-06-02 | `income-tax.r1.2025-06-02.txt` |
| `social-assistance-act` (existing) | Social Assistance Act | R.S.N.W.T. 1988, c.S-10 | 2018-11-21 | `social-assistance.a.2018-11-21.txt` |
| `income-assistance-regulations` (new) | Income Assistance Regulations | R-038-2024 | 2026-07-06 | `social-assistance.r1.2026-07-06.txt` |
| `income-assistance-for-seniors-and-persons-with-disabilities-regulations` (new) | Income Assistance for Seniors and Persons with Disabilities Regulations | R-037-2024 | 2026-07-06 | `social-assistance.r5.2026-07-06.txt` |
| `senior-citizens-benefits-act` (new) | Senior Citizens Benefits Act | R.S.N.W.T. 1988, c.S-7 | 2015-03-30 | `senior-citizens-benefits.a.2015-03-30.txt` |
| `senior-citizens-benefits-act` (new) | Amount of Benefit Regulations | R.R.N.W.T. 1990, c.S-7 | 2017-08-25 | `senior-citizens-benefits.r1.2017-08-25.txt` |

Each text is in the subject's `registers/source-bundle/`. A `.meta.json` sits beside it with the source URL, the consolidation date, the HTTP Last-Modified date, the retrieval time, the sha256 of both the PDF and the text, character counts, the conversion method and every editorial restoration. The 2026-09-23 `*.meta.json` index records in the existing subjects were left unchanged, so they still say `text_deposited: false`. Existing `subject.json` files were not touched.

**Conversion.** Each PDF prints English and French side by side. The conversion keeps only the English column and drops page headers, page numbers, printer lines and the table of contents. In the older consolidations the marginal notes become headings, and Part, Division and section numbering is kept. The two-column substitution table in s.1(7)(h) of the Income Tax Act and the four benefit tables in the Income Assistance Schedules are given as rows (`| a | b |`). The PDFs draw minus signs as short rules, not characters, and these were restored as `-`. Two stacked fractions in s.3.2 of the Income Tax Act are written inline. The Dene place names Łutselk'e and Kátł'odeeche were restored where the PDF's text layer drops or mis-maps a letter. Each of these restorations is listed in the `.meta.json`.

### Why these connect

What follows was read in the deposited texts unless it is marked otherwise.

- **Territorial income tax rides on the federal Income Tax Act** (`../income-tax-act/`, R.S.C. 1985, c. 1 (5th Supp.), with the federal Income Tax Regulations C.R.C. c. 945 beside it):
  - Tax is payable by an individual resident in the Northwest Territories on the last day of the taxation year (s.2). Tax is charged at four tier rates, 5.9%, 8.6%, 12.2% and 14.05%, with thresholds indexed to the Consumer Price Index (s.2.11). Many of the non-refundable credits in ss.2.13 to 2.31 are framed by reference to the corresponding federal credits, through "Application of federal Act" provisions.
  - "Federal Act" means the Income Tax Act (Canada) (s.1(1)). Federal provisions apply with modifications (s.1(7)).
  - Under a collection agreement (s.57), the Canada Revenue Agency and the Minister of National Revenue administer the tax. The NWT Income Tax Regulations set payroll withholding as 43/134 of the federal Table 410 amount (s.3).
- **NWT Child Benefit.** The benefit is a deemed overpayment of territorial tax, paid monthly (Income Tax Act ss.3.1 to 3.4). It uses the federal Act's "adjusted income" (s.122.6) and "earned income" (s.63(3)), and the parent must have filed a federal return. The amounts and the $30,000 / $80,000 thresholds are in the Income Tax Regulations, s.1.1.
- **Cost of Living Offset.** Income Tax Act s.3.5 applies federal s.122.5, the GST/HST credit machinery, with modifications. The zone amounts in Income Tax Regulations s.1.2 are currently $0 in all three zones (R-022-2023, R-022-2024, R-038-2025).
- **Income Assistance and federal benefits** (Income Assistance Regulations, made under the Social Assistance Act ss.16 and 17):
  - Applicants must use the financial resources open to them, including unemployment benefits and, from age 65, pension benefits (s.2(2)(d)). Employment insurance counts as earned income (s.22(4)(e)). The GST credit and tax refunds count as unearned income (s.22(5)(k), (m)).
  - The following are excluded from income: the Canada Child Benefit and the NWT Child Benefit, a child's Canada Pension Plan survivor's benefits, the federal Child Disability Benefit, the cost of living offset payment, the territorial carbon tax rebate, and registered disability savings plan funds (s.22(6)).
  - A monthly bridge benefit is available until the Canada Child Benefit begins (Schedule item 6).
  - Eligibility depends on status under the federal Immigration and Refugee Protection Act (s.3).
  - Maximum basic and room-and-board benefits are set by zone A to F and number of adults (Schedule tables).
- **Income Assistance for Seniors and Persons with Disabilities.** These regulations are a separate stream for a "senior" (60 or over) or a person the Director determines has a disability (ss.1 to 3). A recipient of one stream cannot be a person in need under the other (Income Assistance Regulations s.2(2)(e); these regulations s.3(2)(f)).
  - Net annual income starts from line 23600 of the federal notice of assessment, less territorial social assistance and Canada Pension Plan disability benefits (s.22(1)). $6,000 a year each is allowed to the applicant and to the spouse (s.22(4)).
  - An applicant is not required to draw pension benefits before 65 (s.3(3), s.20(5)). An applicant whose family holds more than $75,000 in bank deposits is not a person in need (s.3(2)(e)). Benefit tables are set by community.
- **Senior Citizens Benefits Act.** A monthly benefit is payable to a person receiving the Guaranteed Income Supplement or the spouse's allowance under the Old Age Security Act (Canada) "in the Territories and not elsewhere", who is ordinarily resident there (s.3). The amount is $196 a month (Amount of Benefit Regulations s.1, R-067-2017). Section 7 allows an agreement for Canada to pay the benefit together with OAS. See `../old-age-security-act/`, where the federal Act and regulations are deposited.
- **Federal benefits (unverified, general knowledge).** No deposited text names the Canada Disability Benefit (`../canada-disability-benefit-act/`) or OAS/GIS, so how they are treated in the seniors and disability stream's income test is not stated. They presumably fall inside line 23600. Whether the territorial supplement under the Senior Citizens Benefits Act is in fact paid through the federal OAS system under a s.7 agreement is also unverified. Employment Insurance (`../employment-insurance-act/`) and the Canada Pension Plan (`../canada-pension-plan/`) interact only as stated above.

### Currency

- The register's consolidation dates, also confirmed by each PDF's HTTP Last-Modified header, are in the table above. The register says its consolidations "are updated monthly and may not be the most current version available".
- The two Income Assistance regulations are current to 6 July 2026. Their last listed amendments are R-059-2025 and R-058-2025. Those amendments show no in-force date on the cover page, so check them.
- The Income Tax Act consolidation is dated 23 November 2023, and its last amendment is SNWT 2023, c.30. Any 2024 to 2026 amendments, for example to the tax rates, thresholds or credits, would not be in it.
- The Social Assistance Act is consolidated to 21 November 2018 (SNWT 2018, c.21).
- The Senior Citizens Benefits Act is consolidated to 30 March 2015, and its Amount of Benefit Regulations to 25 August 2017.

### Gaps

- The English version only. The French version is equally authoritative (Official Languages Act s.7(1)) and is in the same PDFs.
- Not sourced: the Social Assistance Appeals Regulations, the Social Assistance Appeal Committees Order, the Welfare Services Regulations, the Income Tax Act's Isolated Posts remission regulations, the Senior Citizens and Disabled Persons Property Tax Relief Act, the Payroll Tax Act, and the administrative "direction of the Director" that many Income Assistance amounts depend on.
- Not checked: whether the federal provisions the NWT texts cite still say what the NWT texts assume. For example, the federal Table 410 that payroll withholding refers to may no longer exist in that form.
- Nothing is encoded yet.

## Update 2026-10-24: encodings, and the CRA thresholds

**Ruling of 2026-10-24 (Michael):** Canadian texts whose terms permit reproduction but are silent on adaptation may be quoted in L4 encodings in Commons, with the attribution the publisher requires and an "unofficial version" notice. The GNWT terms are of that kind (they permit non-commercial reproduction and say nothing of adaptation), so the deposited texts above may be encoded.

- **`income-tax-act/encodings/baseline-2026-10/`**: the resident individual's territorial tax (s 2.11 rates and thresholds, the main non-refundable credits, the dividend deduction), filing and payment duties, the NWT Child Benefit (ss 3.1 to 3.3 with Regulations s 1.1) and the Cost of Living Offset (s 3.5 with Regulations s 1.2, currently $0). The 2026 tier thresholds are taken from the Canada Revenue Agency page "Current year tax rates and income brackets (2026)", deposited 2026-10-24 as `income-tax-act/registers/source-bundle/cra-tax-rates-brackets-2026.txt` under the Government of Canada's non-commercial reproduction terms. The indexed credit amounts are inputs: the CRA's TD1NT form and T4127 tables are in a folder that canada.ca's robots.txt disallows.
- **`social-assistance-act/encodings/baseline-2026-10/`**: the Social Assistance Act with its two regulations, the Income Assistance Regulations (R-038-2024) and the Income Assistance for Seniors and Persons with Disabilities Regulations (R-037-2024). It covers which stream an applicant falls in, eligibility, person in need, the IA monthly income and SPD net annual income tests, the zone and community benefit tables, the budget deficit, reporting duties and appeals. The Senior Citizens Benefits Act ($196 a month for GIS recipients) is deposited but not encoded.
