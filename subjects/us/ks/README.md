# kansas/

Kansas (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Kansas Statutes on the Kansas Legislature's site (statutes compiled by the Office of Revisor of Statutes); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

BLOCK ENCOUNTERED AND RESPECTED, then an official alternative used. The Revisor's own site, https://www.ksrevisor.gov/, answers HTTP 200 but returns a bot-verification interstitial instead of content: the body of both https://www.ksrevisor.gov/statutes/ and the section page https://www.ksrevisor.gov/statutes/chapters/ch44/044_003_0013.html was only 'One moment, please... Loader Please wait while your request is being verified...' with no statute text and no real links. That challenge was NOT solved, bypassed or retried in a loop - two requests, then stop. Verification was done instead on the Kansas Legislature's own site, which publishes the same Revisor-compiled statutes as plain server-rendered HTML and served every request with HTTP 200 and no challenge. URL shapes used: chapter index https://www.kslegislature.gov/li/b2025_26/statute/<ccc>_000_0000_chapter/ (lists the articles with their names) and article page https://www.kslegislature.gov/li/b2025_26/statute/<ccc>_000_0000_chapter/<ccc>_<aaa>_0000_article/ (lists every section number and catchline). Currency: every page carries the heading '2026 Kansas Statutes'. About 17 requests in total, all with an honest user agent (canon-index-builder/1.0) and spaced 2 seconds apart. The statutes index also confirmed the chapter list (85 chapters, including 'Chapter 35 HOLIDAYS AND DAYS OF COMMEMORATION' and 'Chapter 44 LABOR AND INDUSTRIES').

## Topics with no legislation here

- **Leave/holiday pay**: No Kansas statute grants leave or holiday pay. Private-sector vacation, sick and holiday pay is a matter of contract or policy, enforceable only as wages under K.S.A. ch. 44, art. 3. For state employees, leave is set by regulation (K.A.R. art. 1-9) under the Kansas Civil Service Act, K.S.A. ch. 75, art. 29, whose only statutory leave hook is 75-2947 'Transfers; leaves of absence; reinstatements.' (verified on the register's 2026 article listing); K.S.A. 75-3707, which is sometimes cited for this, is in fact 'Functions of department in general.' and grants no leave. Chapter 35 'HOLIDAYS AND DAYS OF COMMEMORATION' (seen on the register's chapter index) only designates days and confers no pay entitlement. Family and medical leave is federal (FMLA, 29 U.S.C. 2601).
- **Passenger compensation**: Federal, and preempted. Air passenger rights come from US DOT rules (14 CFR Parts 250, 259, 260) and the Airline Deregulation Act (49 U.S.C. 41713) preempts state regulation of airline prices, routes and services. Kansas has no passenger-compensation statute.
- **Customs/duties**: Federal, and constitutionally exclusive. U.S. Const. art. I, sec. 10, cl. 2 bars a state from laying imposts or duties on imports or exports; customs law is 19 U.S.C., administered by CBP.
- **Work permits/immigration**: Federal. Work authorisation and immigration status are governed by the Immigration and Nationality Act, 8 U.S.C., and 8 C.F.R.; Kansas issues no work permits and its statutes touch immigration only through benefit eligibility screens.

## Benefits and personal income tax sample (text deposited 2026-10-20)

Unannotated statute text was deposited on 2026-10-20 for a connected set on personal income tax and state benefits. It was taken from the Office of Revisor of Statutes' own site, www.ksrevisor.gov: 84 section pages, all HTTP 200, with no bot challenge. robots.txt was honoured, and every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`.

| Subject | File in `registers/source-bundle/` | Sections | What it gives a person |
| --- | --- | --- | --- |
| `kansas-statutes-chapter-79-article-32-income-tax` (existing) | `ksa-79-32-individual-income-tax.txt` | 26 | Kansas income tax owed: definitions (79-32,109), rates (79-32,110 and 79-32,110b), Kansas AGI and its modifications (79-32,117), deductions (79-32,118 to 79-32,120), exemptions (79-32,121, 79-32,121b), part-year residents (79-32,128), returns and payment |
| same | `ksa-79-32-individual-credits-eitc-safesr-food.txt` | 4 | Refundable Kansas EITC (79-32,205), SAFESR senior property-tax credit (79-32,263), credit limits (79-32,264), food sales tax credit (79-32,271) |
| `kansas-statutes-chapter-79-article-45-homestead-property-tax-refund` (new) | `ksa-79-45-homestead-property-tax-refund-act.txt` | 22 | Homestead property tax refund for low-income homeowners and renters: who may claim, amount, maximum, deadlines |
| `kansas-statutes-chapter-44-article-7-employment-security-law` (new) | `ksa-44-7-employment-security-law-benefits.txt` | 16 | Unemployment benefits: definitions (44-703), amount and duration (44-704), extended benefits, eligibility (44-705), disqualification (44-706), claims and appeals (44-709), overpayments (44-719), tax information for claimants (44-773) |
| `kansas-statutes-chapter-39-article-7-social-welfare` (existing) | `ksa-39-7-public-assistance-tanf.txt` | 16 | Public assistance: eligibility for TANF, food assistance and child care subsidy (39-709), duty to report changes (39-719b), family-assistance rules 39-7,124 to 39-7,133, legislative approval of waivers (39-7,165) |

**How the pieces connect.**

- *Read in the deposited text:*
  - Kansas AGI "means such individual's federal adjusted gross income for the taxable year, with the modifications specified in this section" (79-32,117(a)), which ties it to the federal set at `subjects/us/internal-revenue-code-of-1986`.
  - For tax years beginning after 31 December 2023, Social Security benefits included in federal AGI are subtracted in full. Before that, the subtraction applied only up to federal AGI of $75,000 (79-32,117(c)(xviii)). This sits against 26 U.S.C. 86 and the federal Social Security Act.
  - The Kansas EITC is 17% of the federal earned income credit under IRC section 32 (tax year 2013 onward), and any excess over liability is refunded (79-32,205).
  - The rate schedule for 2024 onward is 5.2% / 5.58% (79-32,110(a)(1)(B) and (a)(2)(B)).
  - SAFESR gives 75% of property tax paid to residents aged 65 or over with household income at or below 120% of the federal poverty level (79-32,263).
  - 39-709 sets eligibility for "temporary assistance for needy families", the state's TANF programme.
  - The Employment Security Law defines covered employment by reference to the Federal Unemployment Tax Act (44-703), and 44-773 requires claimants to be told of the federal and state tax consequences of benefits.
- *Unverified (general knowledge):*
  - Kansas TANF is the state plan under Social Security Act Title IV-A (42 U.S.C. 601 ff.).
  - SNAP ("food assistance" in 39-709) is the federal programme under the Food and Nutrition Act of 2008.
  - UI benefits are federally taxable under 26 U.S.C. 85.
- *Read in the deposited text (homestead):* the homestead refund's income test counts federal Social Security payments, but at no more than 50% of them (79-4502).

**Terms.** Verdict: *conditions*, met. The plan recorded a site-wide "All rights reserved" footer. Today the ksrevisor.gov footer reads only "www.ksrevisor.gov 2026". The Kansas.gov portal claims the compilation of its content. Statutes are not copyrightable (*Georgia v. Public.Resource.Org*, 2020), so only the statutory text and history lines are deposited. Revisor's Notes, cross references and case annotations are omitted. Details are in each subject's SOURCE-LICENSE.md.

**Currency.** The register says its online statutes "include amendments and new laws enacted during the 2025 legislative session" (read 2026-10-20). The 2026-09-23 index check saw "2026 Kansas Statutes" headings on kslegislature.gov. Before relying on any figure, check whether a 2026 session law amended a deposited section. Every text is an unofficial version: the authenticated K.S.A. is the printed bound volumes and supplement.

**Gaps.**
- 79-32,110 and 79-32,110b are both marked "[See Revisor's Note]": the section was amended more than once in the 2025 session. Both versions are deposited, and the note itself is not. Read it on the register before encoding rates.
- Not deposited:
  - the rest of art. 32 (withholding, business and investment credits, apportionment);
  - the rest of ch. 44 art. 7 (employer contributions, administration);
  - the medical-assistance and child-support sections of ch. 39 art. 7;
  - the Kansas Administrative Regulations (K.A.R.), which set TANF payment standards.
- Kansas has no state supplementary payment statute in this set.
