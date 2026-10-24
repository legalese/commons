# maryland/

Maryland (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Maryland General Assembly - Statute Text (Annotated Code of Maryland), official legislative site; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Statute text was deposited later (see below); two baseline encodings were added on 2026-10-24.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 12 requests in total (the Statutes landing page, the Home page for the footer, the Privacy Notice, and section pages for Labor and Employment 3-501, 3-505, 3-1301, 8.3-101 and 11-301, State Personnel and Pensions 21-101, Human Services 5-101, Tax-General 10-101, Insurance 27-303, Public Utilities 7-307 and Real Property 8-203). All returned 200; no block, challenge or rate limit. Two quirks worth recording: https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText with no query string renders 'File Not Found', and the article/section pages carry no printed as-at date, effective-date note or version label - the only currency control is the site's 'include enactments of the last session' toggle (the URLs recorded here use enactments=false, i.e. the text in force rather than the text as it will read after the last session's enactments commence).

## Topics with no legislation here

- **Passenger compensation**: No Maryland statute. Air passenger rights are federal (49 U.S.C. 41712; 14 C.F.R. Part 250 oversold flights, Part 259 tarmac delays) and state regulation of air carrier prices, routes and services is pre-empted by 49 U.S.C. 41713; intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Maryland's MARC and MTA services set passenger rights by tariff and regulation, not by statutory compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.

## Benefits and personal income tax sample (deposited 2026-10-20)

Statute text was deposited on 2026-10-20 for a Priority 3 sample: personal income tax and benefits, from the seat of the Maryland resident who asks "What State and county income tax do I owe, and what credits and benefits can I get?". Source: the General Assembly's Statute Text pages (mgaleg.maryland.gov), with the register's "include enactments of the last session" option on, i.e. **the Code as in effect on 1 October 2026** (after the 2026 Regular Session). Every text is an unofficial conversion and says so at its top. 119 sections, 535,097 characters in 5 files.

| Subject | File | What it holds |
|---|---|---|
| `annotated-code-of-maryland-tax-general-article-title-10-income` (existing) | `tax-general-title-10-subtitles-1-2-rates-and-maryland-taxable-income` | Tax-Gen. ss 10-101 to 10-223: definitions, State rates (s 10-105, 2%-6.5% plus the 2% capital-gain addition), county rates (s 10-106), Maryland adjusted gross income, additions (s 10-204), subtractions (s 10-207, incl. Social Security and Railroad Retirement benefits; s 10-208), pension exclusion (s 10-209), exemptions (s 10-211), deductions |
| same | `tax-general-title-10-subtitle-7-individual-credits` | 13 credits an individual meets: earned income credit (s 10-704), poverty-level credit (s 10-709), child and dependent care (s 10-716), child tax credit (s 10-751), senior credit (s 10-754), taxes paid to other states (s 10-703), others |
| `annotated-code-of-maryland-labor-and-employment-article-title-8-unemployment-insurance` (new) | `labor-and-employment-title-8-subtitles-1-8-9-10-unemployment-insurance-benefits` | Lab. & Empl. ss 8-101 to 8-111, 8-801 to 8-910, 8-1001 to 8-1009: definitions, eligibility, the schedule of benefits (s 8-803, as a table), dependants' allowance, deductions and withholding, claims, disqualification |
| `annotated-code-of-maryland-human-services-article-title-5` (existing) | `human-services-title-5-subtitle-3-family-investment-program` | Hum. Servs. ss 5-301 to 5-323: the Family Investment Program and its temporary cash assistance |
| `annotated-code-of-maryland-tax-property-article-title-9-subtitle-1-state-property-tax-credits` (new) | `tax-property-title-9-subtitle-1-renters-homeowners-homestead-credits` | Tax-Prop. ss 9-101 to 9-105.1: renters' tax credit (s 9-102), homeowners' tax credit (s 9-104), homestead credit (s 9-105) |

**How the pieces connect** (read in the deposited texts unless marked):

- State income tax starts from federal adjusted gross income "as determined under the Internal Revenue Code" (Tax-Gen. s 10-101(e)), so it rests on `subjects/us/internal-revenue-code-of-1986` (26 U.S.C. 62).
- Social Security benefits taxed federally under 26 U.S.C. 86 are subtracted for Maryland: s 10-207 subtracts benefits "under Title II of the Social Security Act" and Railroad Retirement benefits (`subjects/us/social-security-act`, Title II).
- The State earned income credit is a percentage of the federal earned income credit "allowable ... under s 32 of the Internal Revenue Code" (s 10-704: 50% non-refundable, a refundable percentage, 100% for an individual without a qualifying child); the poverty-level credit (s 10-709) uses earned income as defined in IRC s 32(c)(2); the child and dependent care credit (s 10-716) is keyed to the federal credit under IRC s 21; the child tax credit (s 10-751) uses the IRC s 152 dependant.
- Unemployment insurance is construed so that the US Secretary of Labor certifies the title under IRC s 3304 (FUTA) (Lab. & Empl. s 8-103), and claimants may elect federal income tax withholding from benefits (Subtitle 8). That benefits are federally taxable under 26 U.S.C. 85: unverified (general knowledge), in the IRC subject.
- Temporary cash assistance is "the cash assistance component of the FIP that is funded wholly or partly through Title IV, Part A, of the Social Security Act" (Hum. Servs. s 5-301), and FIP eligibility excludes SSI benefits (Title XVI). SNAP is federal (`subjects/us/food-and-nutrition-act-of-2008`).
- The renters' and homeowners' credits are income-tested property-tax relief paid by the State, separate from the income tax.

**Terms**: clean. mgaleg.maryland.gov has no robots.txt (404) and states no copyright, licence or terms of use; it serves the bare Code, not the LexisNexis or West annotated editions. The About page says the Session Laws are the official law and the Code is evidence of it. Details in each subject's `SOURCE-LICENSE.md`.

**Gaps**: Maryland supplements federal SSI only through programmes outside this sample (no State supplementary payment statute was sourced). The county income tax rates each county sets by local law are not here; s 10-106 gives only the limits. COMAR (regulations) was not used: dsd.maryland.gov answered 403 to robots.txt at set-up. The register's section pages have no catchlines or subtitle headings; the files group sections by subtitle number only.

## Administrative rules: sourcing attempt 2026-10-20 (nothing deposited)

Maryland sets the Temporary Cash Assistance (TCA) benefit levels, the Temporary Disability Assistance and Public Assistance to Adults amounts, and the state supplement in COMAR, mainly Title 07 (Department of Human Services; COMAR 07.03.03 for TCA, unverified (general knowledge)). Those regulations were **not deposited**.

- **COMAR host blocked.** The official COMAR host is the Division of State Documents, https://dsd.maryland.gov. On 2026-10-19 at 18:45 UTC it answered **HTTP 403** to a request for `/robots.txt` with the commons User-Agent, as it did at set-up. Under the access rules, an unreadable robots.txt counts as a disallow, so the host was stopped. No other request was made to it, and no mirror, vendor copy or other identity was tried. **Index only; flagged.**
- **Agency pages.** https://dhs.maryland.gov allows crawling (robots.txt read 2026-10-19). Its TCA page says only that income "cannot exceed the benefit level paid for the assistance unit size" and gives no figures. The DHS manuals page linked no TCA manual, and the transmittals pages were not searched. No official notice of current TCA benefit levels was found, so nothing was deposited.

**Remaining gaps.**
- TCA, TDAP and PAA benefit levels (COMAR Title 07) are not in commons.
- The UI weekly benefit amounts come from the schedule of benefits in Labor and Employment 8-803, which is already deposited as rows, so no rule is needed for them.
- To unblock COMAR: ask the Division of State Documents for access or written permission for the commons fetcher. Alternatively, accept text from the Maryland Register in print.

## Tax and benefits encodings (2026-10-24)

Two baseline encodings, written from the deposited text with the stable l4 (1.6.98), each with its own `NOTES.md` (findings, scope, what to do before relying on it):

| Encoding | Seat | What it answers |
|---|---|---|
| [`annotated-code-of-maryland-tax-general-article-title-10-income/encodings/baseline-2026-10`](annotated-code-of-maryland-tax-general-article-title-10-income/encodings/baseline-2026-10) | the full-year resident taxpayer | residence; Maryland AGI, exemptions, standard or itemized deduction, Maryland taxable income; State tax (with the 2% capital-gain addition) and county tax; the earned income, poverty-level and child tax credits; who must file, joint returns, the due date (also a regulative rule). 9 questions, 60 assertions. |
| [`annotated-code-of-maryland-human-services-article-title-5/encodings/baseline-2026-10`](annotated-code-of-maryland-human-services-article-title-5/encodings/baseline-2026-10) | the applicant for, or recipient of, temporary cash assistance | eligibility for TCA under the Family Investment Program; work activity exemptions and hours; time limits; sanctions and the 30-day rules (two regulative rules); transitional assistance; SSI excluded. 8 questions, 41 assertions. |

**Deposited for the tax encoding:** Tax-General Title 10, Subtitle 8 (ss 10-804 to 10-823: who must file, joint returns, due dates), fetched 2026-10-24 from mgaleg.maryland.gov under the same clean terms (robots.txt still 404, no terms of use). Recorded in the subject's `SOURCE-LICENSE.md`.

**Inputs, not deposited:** federal AGI and the federal earned income credit (link: `subjects/us/internal-revenue-code-of-1986/`), county income tax rates, the Comptroller's 2026 cost-of-living adjustment to the standard deduction, the HHS poverty guideline, and the TCA grant amounts and income and resource tests (COMAR, still blocked: see above).

**Main findings:** the child tax credit's phase-out (s 10-751(c)) can never operate because (b) admits only incomes below the threshold; the poverty-level credit cites s 10-704(a)(1), a definitions paragraph, for the earned income credit; the FIP 24-month limit (s 5-313(a)(2)) has no exemption for an adult exempt from work activity; the two TCA sanctions are not said to compound.
