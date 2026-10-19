# ke/

Kenya legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

Laid out on 2026-10-19 as a Priority 3 sample on two linked topics: **social security and benefits**, and **personal income tax**.
The aim is a set of instruments that lets a member of the public get useful answers. What comes off my pay, and how much?
What benefits can I claim? How much income tax do I owe? How do the deductions interact? Nothing is encoded yet.

**Three texts are deposited and three Acts are indexed only.** The three principal money instruments (income tax, SHIF, the
housing levy) were found only on Kenya Law. Kenya Law's access conditions exclude this use (see [Terms](#terms)). Those three need
a human decision before any text can go in.

## The set, and why these instruments connect

A salaried employee's payslip in Kenya carries four statutory deductions. All four are worked out from gross pay, and three of
them change the PAYE figure:

| subject | instrument | what it answers | text |
| --- | --- | --- | --- |
| [`income-tax-act-16-of-1973`](income-tax-act-16-of-1973) | Income Tax Act (No. 16 of 1973), Cap. 470, with the Income Tax (P.A.Y.E.) Rules (LN 257 of 1973) and the Income Tax (NSSF) (Exemption) Rules 2026 (LN 162 of 2026) as companions | How much income tax do I owe? The PAYE bands and personal relief (Third Schedule Head B; s. 30), and how SHIF, the housing levy and pension contributions are treated for tax | **indexed only** |
| [`national-social-security-fund-act-45-of-2013`](national-social-security-fund-act-45-of-2013) | National Social Security Fund Act (No. 45 of 2013), Cap. 258 | What pension contribution comes off my pay? Tier I and Tier II at 6% + 6% of pensionable earnings between the Lower and Upper Earnings Limits (s. 20, Third Schedule), contracting out (s. 21, Fourth Schedule), and the benefits (Part V: retirement, survivors', invalidity, emigration, funeral grant) | deposited (revised edition as at 31 Dec 2022) |
| [`social-health-insurance-act-16-of-2023`](social-health-insurance-act-16-of-2023) | Social Health Insurance Act (No. 16 of 2023), with the Social Health Insurance Regulations (LN 49 of 2024, as amended) | What health contribution do I pay? Who must contribute (s. 27); the 2.75% of gross salary or household income (regs. 17-21); what the funds cover | **indexed only** |
| [`affordable-housing-act-2-of-2024`](affordable-housing-act-2-of-2024) | Affordable Housing Act (No. 2 of 2024), with the Affordable Housing Regulations 2025 (LN 114 of 2025) | What housing levy comes off my pay? 1.5% of gross salary, matched by the employer, or 1.5% of other gross income (ss. 4-5) | **indexed only** |
| [`employment-act-11-of-2007`](employment-act-11-of-2007) | Employment Act (No. 11 of 2007), Cap. 226 | Am I owed service pay when I leave? s. 35(5) gives service pay for every year worked; s. 35(6) takes it away from members of the NSSF or of a registered pension, provident or gratuity scheme. This is where NSSF membership and termination meet | deposited (**as enacted, 2007**) |
| [`social-protection-act-12-of-2025`](social-protection-act-12-of-2025) | Social Protection Act (No. 12 of 2025) | What non-contributory benefits can I get? Social protection for persons in need: under s. 28(3), orphans or vulnerable children, poor older members of society, persons with disabilities, persons in extreme poverty, persons affected by shocks, and unpaid or unsupported caregivers. Also the benefits, eligibility, application, review and appeal (Part III) | deposited (as enacted, Gazette of 5 Aug 2025) |

How they interact: NSSF, SHIF and the housing levy are worked out from gross pay. The Income Tax Act then decides how each one
bears on taxable income and PAYE: pension contributions are deductible, and the SHIF and housing-levy treatment was changed in
2024 when the housing relief in s. 30A was repealed by Act No. 12 of 2024. The PAYE Rules make the employer withhold. The
Employment Act's service pay is not due where the employee is in the NSSF. The Social Protection Act is the non-contributory side:
what someone outside formal employment can claim.

**Not included, deliberately.** The **Social Assistance Act 2013** (Cap. 258A) was repealed by the Social Protection Act 2025,
s. 49, and is replaced by it. The **Tax Procedures Act** (Cap. 469B) and the **Retirement Benefits Act** (Cap. 197) are machinery
here. The **Finance Act 2026** is the amending Act that sets the current tax numbers, but its amendments are consolidated
into the Income Tax Act expression of 1 July 2026. Kenya Law's amendment notes cite it as "Act No. 19 of ..."; the number was
seen only in a third-party index snippet and is not verified.

## Terms

All requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, spaced at
least 3 s apart. Each site's robots.txt was read before any document was fetched. Read on 2026-10-19:

- **The law.** Copyright Act, 2001 (No. 12 of 2001), s. 2, definition of "literary work": "... but does not include a written law
  or a judicial decision". Kenyan statutes carry no copyright.
- **Kenya Law, `https://new.kenyalaw.org/robots.txt`.** It timed out or returned 504 from 13:19 to 13:53 UTC and was read at
  13:57 UTC. For all user agents: `Content-Signal: ai-train=no, search=yes, ai-input=no`, `Crawl-delay: 5`, `Allow: /` with
  `/api/`, `/search/`, `/judgments/`, `/gazettes/` and `/akn/*/provision/*` disallowed. It states: "As a condition of accessing this
  website, you agree to abide by the following content signals". ClaudeBot, Claude-Web, anthropic-ai, GPTBot and others are
  disallowed from the whole site.
- **Kenya Law, `https://new.kenyalaw.org/terms-of-use/`** (notice dated 8 October 2025). "Scraping and bulk downloading from this
  website is strictly prohibited ... Please email us if you would like to access our data in bulk." Content is re-usable under
  **CC BY-NC 4.0**, "provided you credit Kenya Law as your source and your use is not for commercial gain." Kenya Law's own
  revised-edition PDFs say: "There is no copyright on the legislative content of this document"; the PDF copy is CC BY-NC-SA 4.0.
- **Decision.** No document page was requested from Kenya Law. AI agents read and encode these texts, and that use falls inside
  `ai-input=no`. The texts deposited here come from other official hosts that state no terms.
- **NSSF, `www.nssf.or.ke`.** robots.txt disallows only `/wp-admin/`. No terms page. It hosts Kenya Law's revised edition of
  Cap. 258, which carries the "no copyright on the legislative content" statement quoted above.
- **State Department for Labour, `www.labour.go.ke`.** Standard Drupal robots.txt with no crawl-delay. No terms page.
- **State Department for Social Protection, `www.socialprotection.go.ke`.** No robots.txt (HTTP 404). No terms page.
- **KRA, `www.kra.go.ke`.** Checked, not used. Its website terms grant a licence "for purposes of viewing" only and forbid
  "data mining, data harvesting, data extracting".
- **Parliament, `www.parliament.go.ke`.** Standard Drupal robots.txt, no terms page. It lists Bills only, mostly as large scans,
  not enacted Acts.
- **Also checked:** `www.health.go.ke` (only a draft of the SHI regulations), `www.sha.go.ke` (HTTP 404) and
  `www.housingandurban.go.ke` (no 2024 Act). Each subject's `SOURCE-LICENSE.md` records the details.

## Currency

| instrument | version held or indexed | gap |
| --- | --- | --- |
| NSSF Act | revised edition as at **31 Dec 2022** | the Third Schedule sets Lower and Upper Earnings Limits for years 1-4 and a formula for year 5 onward: LEL = the gazetted average minimum wage, UEL = 4 x National Average Earnings. The **figures now in force come from Gazette notices that are not sourced** |
| Employment Act | **as enacted, 2007** | amended since (Employment (Amendment) Acts 2021 and 2022, among others); Kenya Law lists a consolidation of 26 Apr 2024 |
| Social Protection Act | as enacted, Gazette of **5 Aug 2025**, in force 19 Aug 2025 | the Social Protection (General) Regulations 2026 (LN 68 of 2026) are not sourced |
| Income Tax Act | Kenya Law expression **1 Jul 2026** (indexed, from a third-party index) | the **Tax Laws (Amendment) Bill, 2026** was before the National Assembly in October 2026 |
| SHI Act / Regulations | Act expression 24 Nov 2023; Regulations 28 Feb 2025 (indexed) | |
| Affordable Housing Act | Kenya Law expression **1 Jul 2026** (indexed) | amended by the Finance Act 2026 |

## Gaps and flags

1. **The three money Acts have no text** (Income Tax Act, SHI Act and Regulations, Affordable Housing Act). Getting them needs a
   decision: write to Kenya Law (info@kenyalaw.org) asking permission for this use or for bulk access, or find another host
   whose terms permit it.
2. **The deposited texts are not current consolidations.** The Employment Act is as enacted in 2007. The NSSF Act is as at
   2022. The Social Protection Act is an OCR'd scan whose errors have not been corrected; its marginal notes are printed in
   [square brackets].
3. **The URLs and expression dates for the indexed Acts came from the Legal Data Hunter index** (source KE/KenyaLaw), used here for
   discovery, not from Kenya Law itself. They are not verified. That index serves Kenya Law content; whether using it fits
   Kenya Law's `ai-input=no` signal is also a question for the human decision in point 1.
4. **Seat.** For any encoding, the seat is the employee or the applicant: "What comes off my pay?", "What do I owe?",
   "Am I owed service pay?", "Can I get a cash transfer?"
