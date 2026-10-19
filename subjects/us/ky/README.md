# kentucky/

Kentucky (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Kentucky Revised Statutes, Legislative Research Commission (official); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 8 requests in total (the KRS title/chapter index three times for verbatim chapter titles, footer links and the Chapter 304 subtitle list, plus chapter pages for 337, 278, 383, 61 and 304.12). All returned 200. IMPORTANT: two hosts serve this register. apps.legislature.ky.gov/law/statutes/ serves the statute text and worked every time. The SharePoint host legislature.ky.gov returned HTTP 403 Forbidden for the policy pages (https://legislature.ky.gov/policies-security/Pages/Disclaimers.aspx and https://legislature.ky.gov/Pages/disclaimer.aspx), so the formal disclaimer/terms page could not be read; I stopped rather than retrying or changing client identity. Note also that the index page's own hrefs point at the 403-ing legislature.ky.gov host, so the working apps.legislature.ky.gov URLs are recorded here instead.

## Topics with no legislation here

- **Passenger compensation**: No Kentucky statute. Air passenger rights are federal (49 U.S.C. 41712 and 14 C.F.R. Part 250, oversold flights / Part 259, tarmac delays, administered by the US Department of Transportation), and intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Kentucky regulates intrastate motor carriers under KRS Chapter 281 but sets no passenger compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.

## Benefits and personal income tax sample (text deposited 2026-10-20)

Unannotated statute text was deposited on 2026-10-20 for a connected set on personal income tax and state benefits. It was taken from the LRC's statute host, apps.legislature.ky.gov: 49 section PDFs, all HTTP 200. That host has no robots.txt (404). The policy host, legislature.ky.gov, was not contacted. Every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`.

| Subject | File in `registers/source-bundle/` | Sections | What it gives a person |
| --- | --- | --- | --- |
| `kentucky-revised-statutes-chapter-141-income-taxes` (existing) | `krs-141-individual-income-tax.txt` | 19 | Kentucky income tax owed: definitions and the IRC conformity date (141.010), adjusted gross income (141.019), the rate (141.020), pension exclusions (141.021, 141.0215), order of credits (141.0205), family size credit (141.066), dependent care and tuition credits, credit for tax paid to other states, standard deduction (141.081), returns, payment, withholding |
| `kentucky-revised-statutes-chapter-341-unemployment-compensation` (new) | `krs-341-unemployment-compensation-benefits.txt` | 17 | Unemployment benefits: definitions, base period and benefit year (341.090), suitable work (341.100), qualification (341.350, 341.355), disqualification and its length (341.360, 341.370), weekly rate and maximum (341.380), duration (341.385), deductions, tax-withholding notice (341.395), overpayment recovery (341.415), appeals |
| `kentucky-revised-statutes-chapter-205-public-assistance-and` (existing) | `krs-205-public-assistance-ktap-ssp.txt` | 12 | Public assistance (K-TAP): definitions, eligibility (205.200), the Title IV-A standard of need (205.2001), work and SNAP rules (205.2003, 205.2005), amount (205.210), payments exempt from levy (205.220), appeals (205.231), cash assistance disqualification (205.232), state supplementation of SSI (205.245) |
| `kentucky-revised-statutes-chapter-132-section-810-homestead-exemption` (new) | `krs-132-810-homestead-exemption.txt` | 1 | Homestead property-tax exemption for owners aged 65 or over or totally disabled |

**How the pieces connect.**

- *Read in the deposited text:*
  - "Internal Revenue Code" means, for taxable years beginning on or after 1 January 2026, the IRC in effect on 31 December 2025 (141.010). Adjusted gross income is gross income less the deductions allowed by IRC section 62, with Kentucky adjustments (141.019(1)).
  - Social Security and railroad retirement benefits subject to federal income tax are excluded (141.019(1)(e)), against 26 U.S.C. 86.
  - The rate is 4% for taxable years 2024 and 2025 and 3.5% from 1 January 2026. Further cuts depend on budget conditions and an Act of the General Assembly (141.020(2)(e)-(g)).
  - The family size tax credit is keyed to the federal poverty guidelines under 42 U.S.C. 9902(2) and to the qualifying-child definition in IRC section 152(c) (141.066).
  - 205.2001 defines the "Public assistance under Title IV-A of the Federal Social Security Act standard of need".
  - 205.245 makes the state's payments to the needy aged, blind and disabled a "Mandatory state supplementation of the supplemental security income program", which is federal SSI under SSA Title XVI (`subjects/us/social-security-act`).
  - 341.395 requires new UI claimants to be told about the deduction and withholding of income tax from benefits.
  - 132.810 implements the homestead exemption in Ky. Const. sec. 170: $6,500 in 1972 dollars, adjusted every two years by the cost-of-living index. Disability can be shown under the Social Security Administration's rules.
- *Unverified (general knowledge):*
  - K-TAP is Kentucky's TANF programme under SSA Title IV-A (42 U.S.C. 601 ff.).
  - SNAP is federal under the Food and Nutrition Act of 2008.
  - UI benefits are federally taxable under 26 U.S.C. 85.
  - Kentucky has no state earned income credit.

**Terms.** Verdict: *conditions*, met for the unannotated text.
- The statute host's footer reads "Copyright ... Kentucky Legislative Research Commission All rights Reserved".
- The formal disclaimer is on legislature.ky.gov, whose robots.txt answers 403. That host was not contacted, so the disclaimer is unread.
- Statutes are not copyrightable (*Georgia v. Public.Resource.Org*, 2020). LRC Notes are omitted. Catchlines are kept, although the register says they are not part of the law.
- Details are in each subject's SOURCE-LICENSE.md.

**Currency.** The register says it "Includes enactments through the 2026 Regular Session" and that the KRS database was last updated on 10/19/2026 (read 2026-10-20). The text is an unofficial version: the LRC offers "Certified Versions" separately.

**Gaps.**
- Not deposited:
  - the rest of ch. 141 (corporation and pass-through taxes, business credits);
  - ch. 341 employer contributions and trust-fund provisions;
  - ch. 205 Medicaid provisions;
  - the Kentucky Administrative Regulations (921 KAR), which set K-TAP payment standards and SSP amounts.
- Ky. Const. sec. 170, which grants the homestead exemption, is not deposited.
- An incident during the fetch: one connection was dropped by the server, then local DNS failures followed. The fetcher stopped and resumed at 8 s spacing. Every deposited file is from an HTTP 200 response.
