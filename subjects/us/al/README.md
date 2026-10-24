# alabama/

Alabama (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the ALISON - Alabama Legislature Official Information System, Code of Alabama 1975; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text was deposited then; see the 2026-10-20 sample below for the text now deposited. Three encodings were added on 2026-10-24 (see the last section).

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

The code browser is a JavaScript single-page app (Next.js + a GraphQL endpoint with introspection disabled); a plain HTTP fetch returns only the page shell, and the legacy host alisondb.legislature.state.al.us no longer resolves (DNS failure). I therefore loaded the site in a real browser (Claude's browser pane, ordinary Chrome, no user-agent spoofing) and used its own navigation. Section pages load from https://alison.legislature.state.al.us/code-of-alabama?section=<n>-<n>-<n> and render a breadcrumb (Title / Chapter / Article / Section + catchline) plus the section text and source credits; the left table of contents shows chapter captions with section ranges when a title is expanded. About 12 page loads plus a handful of in-page clicks, spaced by seconds. No block, no bot challenge, no rate limiting. The site shows no 'as at' or 'current through' date anywhere, and no statement of which version is official.

## Topics with no legislation here

- **Payroll/wages**: No general state wage-payment or minimum-wage statute. The register's Title 25 table of contents lists no wages chapter (chapters run: Department of Labor, Unemployment Compensation, Workers' Compensation, Employer's Liability, Labor Unions and Labor Relations, Child Labor, Small Business Assistance, Directory of New Hires, boilers, elevators, PEOs, workforce boards). Private-sector minimum wage, overtime and recordkeeping are governed by the federal Fair Labor Standards Act, 29 U.S.C. s 201 et seq. Ala. Code 1975 s 25-7-41 (verified: 'Definitions; Limitations on Compensation and Employment Benefits Not Required by State or Federal Laws', Title 25, ch. 7, art. 2A - the Alabama Uniform Minimum Wage and Right-to-Work Act) works the other way: it bars local governments from imposing wage or benefit mandates.
- **Leave/holiday pay**: No state statute for private employers: Alabama mandates neither paid nor unpaid annual leave, holiday pay nor sick leave, and s 25-7-41 et seq. preempts local mandates. Job-protected family and medical leave comes from the federal FMLA, 29 U.S.C. s 2601 et seq. Leave for state merit-system employees is dealt with under Title 36 (Public Officers and Employees).
- **Termination/severance**: Employment is at will by common law and there is no statutory notice, severance or mass-layoff regime; plant-closing notice comes from the federal WARN Act, 29 U.S.C. s 2101 et seq. Alabama has no mini-WARN Act and no final-pay statute (compare the wage-payment statutes other states have). Statutory protection is issue-specific only, e.g. retaliatory discharge for workers' compensation claims in Title 25, ch. 5.
- **Passenger compensation**: Federal. Air passenger rights come from US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Alabama has no passenger compensation statute.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.

## Benefits and personal income tax sample (deposited 2026-10-20)

This deposit is part of the Priority 3 US-states sample. It holds a connected set of Alabama statutes, so that a member of the public can get determinations: the Alabama income tax they owe, and the state benefits and exemptions they can claim. The set plugs into the federal subjects in `subjects/us/`: `internal-revenue-code-of-1986`, `social-security-act` and `food-and-nutrition-act-of-2008`.

**Route and terms.** The Code is read from ALISON (Legislative Services Agency) through the site's own public GraphQL endpoint (`/graphql`). The query used is the one the site's print view sends. There was no browser automation and no key, login or CAPTCHA. The site has no robots.txt (the path returns the HTML shell) and no terms of use; its only policy page is a privacy statement, and the footer reads "© 2026". Verdict: clean. About 50 requests in all, every one logged: 3 pages (robots.txt, a section page, the privacy statement); 36 fetches of the site's 18 JavaScript bundles, read to find the query (the first pass threw the bodies away and had to be repeated); 1 title index; 10 GraphQL content requests. Details are in each subject's `SOURCE-LICENSE.md`.

**Currency.** ALISON publishes no 'current through' date. The text is what the site served on 2026-10-20; the 2026 Regular Session adjourned on 9 April 2026. The site's own notes flag three sections whose text may lag:

- s 40-18-14 (adjusted gross income of individuals): "AMENDED BY ACT 2026-551, EFFECTIVE MAY 1, 2026. SEE ACT FOR REVISED LANGUAGE".
- s 40-18-15 (deductions): the same note for Act 2026-604, effective 1 October 2026.
- s 40-18-19.4: a new section effective 1 January 2027, deposited and marked "not yet in force".

Read Acts 2026-551 and 2026-604 before relying on ss 40-18-14 and 40-18-15.

| Instrument | Subject | Files | Sections | Characters |
|---|---|---|---|---|
| Income tax, general provisions: individuals' tax and rates (s 40-18-5), adjusted gross income (s 40-18-14), deductions (s 40-18-15), standard deduction, personal and dependent exemptions (s 40-18-19), the severance and unemployment compensation exclusion (s 40-18-19.1) | `code-of-alabama-1975-title-40-chapter-18-income-taxes` | `ala-code-40-18-art1` | 90 | 233,657 |
| Income tax withholding from wages; estimated tax (ss 40-18-70 to 40-18-86) | same | `ala-code-40-18-art2-div1` | 20 | 29,167 |
| Unemployment compensation: definitions (art. 1), benefits (art. 4: weekly benefit amount, maximum entitlement, eligibility, disqualification), claims procedure (art. 5) | `code-of-alabama-1975-title-25-chapter-4-unemployment` | `ala-code-25-4-art1`, `-art4`, `-art5` | 34 | 155,763 |
| Public assistance and TANF cash assistance: definitions (ch. 1, incl. the TANF drug-screening and felony-eligibility rules), public assistance generally (ch. 4), the welfare employment programme (ch. 11A) | `code-of-alabama-1975-title-38-chapters-1-and-4-public-assistance` (new) | `ala-code-38-1`, `-38-4`, `-38-11a` | 27 | 51,289 |
| Homestead exemptions, incl. persons 65 or older or permanently and totally disabled (ss 40-9-19 to 40-9-21.3) | `code-of-alabama-1975-title-40-chapter-9-homestead-exemptions` (new) | `ala-code-40-9-homestead` | 7 | 18,791 |

Total: 9 files, 178 sections, 488,667 characters.

**How the pieces connect.** The links below were read in the deposited text unless marked otherwise.

- **Income tax and the IRC.** Chapter 18 borrows federal definitions by cross-reference. "Head of family" has the meaning of "head of household" in 26 U.S.C. s 2(b) (s 40-18-1(15)). Sections 40-18-1.1, 40-18-15, 40-18-24 and 40-18-25 refer to the Internal Revenue Code. Alabama computes its own adjusted gross income (s 40-18-14) instead of starting from the federal figure; unverified (general knowledge), and pending the Act 2026-551 amendment. Federal subject: `internal-revenue-code-of-1986`.
- **Rates and exemptions.** The bracket table is s 40-18-5: 2% / 4% / 5%, with thresholds of $500 / $3,000 for a single filer and $1,000 / $6,000 for a joint return. The personal exemption ($1,500 or $3,000) and the dependent exemption ($1,000, $500 or $300 by AGI band) are in s 40-18-19(a)(8)-(9). The same s 40-18-19 exempts state, federal civil-service and defined-benefit pensions.
- **Social Security benefits.** Alabama does not tax Social Security benefits: unverified (general knowledge). No exemption naming Social Security benefits was found in the deposited Article 1 text; it may sit in s 40-18-14, whose text is pending amendment. Compare 26 U.S.C. s 86 in the IRC subject.
- **Unemployment compensation.** Benefits are paid under the federal-state programme (SSA Titles III and IX; FUTA in IRC ch. 23). Section 25-4-70(e) appropriates Reed Act money "made available to this state under Section 903 of the Social Security Act". UI benefits are federally taxable under 26 U.S.C. s 85 (federal set). Alabama excludes some severance and unemployment compensation paid on a qualifying job loss from state income tax (s 40-18-19.1).
- **TANF.** TANF cash assistance and eligibility "shall conform with federal eligibility requirement standards as provided for in Title IV, Part A, of the Social Security Act" (s 38-4-4(b)). Applicants must first apply for three jobs, and recipients who refuse work without good cause lose eligibility (s 38-11A-2). The amount of assistance is set by Department of Human Resources rules (s 38-4-2), which are not deposited. Public assistance grants are exempt from taxes and from garnishment (s 38-4-8). SNAP is federal (`food-and-nutrition-act-of-2008`); s 38-1-8 restores TANF and SNAP eligibility for drug-felony offenders under 21 U.S.C. s 862a(d), and s 38-4-15 restricts SNAP purchases.
- **Homestead exemption and income tax.** The over-65 and disability exemption in s 40-9-21 is tested against "net annual taxable income of twelve thousand dollars"; its catchline calls this net annual federally taxable income, which links it to the IRC. Section 40-9-19 tests a related exemption against "an annual adjusted gross income of less than $12,000 as reflected on the most recent state income tax return", which links it to Chapter 18.

**Gaps.** Alabama has no state earned income credit (none appears in Article 1, and Article 4B was not deposited). The Department of Human Resources' TANF payment standards are in the Alabama Administrative Code, which was not fetched. Constitutional homestead provisions and county local acts are not deposited. The plan's "Rates" instrument (s 40-18-5 and the dependent exemption in s 40-18-19) sits inside Article 1 and so has no file of its own.

## Administrative rules deposited 2026-10-20

The question was where Alabama sets the **amounts** a person gets: the Family Assistance (TANF) grant, the state SSI supplement, and the UI maximum weekly benefit.

**Added:** `alabama-administrative-code-660-2-2-and-660-2-4-family-assistance-payment-and-state-supplementation` (new). It holds one file, `ala-admin-code-660-2-2-and-660-2-4` (9,913 characters), with seven Department of Human Resources rules from the Alabama Administrative Code (admincode.legislature.state.al.us), read 2026-10-19 UTC through the site's own public GraphQL endpoint:
- 660-2-2-.10 (amount of assistance payment), -.27 (need requirement), -.31 (payment standard) and -.32 (computation of grant);
- 660-2-4-.10 (amount of State Supplementation payment), -.19 (need requirement), and Appendix A attachments to chapter 660-2-4.

**What the deposited text settles, and what it does not:**
- **Family Assistance.** The payment is "the appropriate payment standard (as established by the Department based on availability of funds) minus the rounded total net available income", with a minimum grant of $10 and first-month proration (-.10, -.32). The standard "varies by family size" (-.31). **There is no dollar table in the current rules.** The attachment that held it, Attachment 660-2-2-.31 "Standards for Family Assistance (FA) Families", is listed in Appendix A as repealed 9/21/18. So the current FA payment standard is not in rule text. It remains unsourced.
- **State Supplementation.** The payment depends on "the kind of care he needs, subject to the funds available", and the person must be an SSI recipient (-.10, -.19). Attachment 660-2-4-.19a gives the special-needs amounts. For each payment it shows a "Monthly Amount To Be" and a "Maximum Budgeted" figure: FCMP nursing care $100 / $60; nursing care supplement $60 / $60; personal care supplement $60 (level A) or $56 (level B); personal or nursing care in foster care $110; care in a cerebral palsy treatment center $196. Attachment .19b gives the basic requirements for nursing-home cases. The appendix also carries a 1995 federal benefit rate chart marked "Reference Only"; it is not current.
- **UI maximum.** No rule is needed. The deposited statute, Code of Ala. s 25-4-72(5) (`ala-code-25-4-art4`), sets the weekly maximum at $275 for benefit years beginning on or after January 1, 2020.

**Terms.** The site has no terms of use. Its footer reads "Copyright (c) Alabama Legislative Services Agency. All rights reserved." and names LSA as "official publisher of the Alabama Administrative Code". Rules are law and carry no copyright. robots.txt: the path serves the HTML shell (treated as absent), and the page declares robots "all". Verdict: clean for the rule text. **Flag:** the footer's general "All rights reserved" claim may deserve a human ruling, as for Kentucky.

**Remaining gaps:** the current Family Assistance payment standard by family size (DHR sets it outside the Code); the current base State Supplementation amounts beyond the special-needs table.

## Encodings: tax and benefits (2026-10-24)

Three baseline encodings, each written from the seat of the individual and checked with the stable `l4` (1.6.98): 0 errors, 0 warnings, every assertion satisfied.

| Encoding | Seat | Questions | Assertions |
|---|---|---|---|
| [`code-of-alabama-1975-title-40-chapter-18-income-taxes/encodings/baseline-2026-10`](code-of-alabama-1975-title-40-chapter-18-income-taxes/encodings/baseline-2026-10) | the individual taxpayer | residence, must I file, standard deduction, exemptions, severance exemption, tax owed (tax years from 2022, residents), wage statement date | 43 |
| [`code-of-alabama-1975-title-25-chapter-4-unemployment/encodings/baseline-2026-10`](code-of-alabama-1975-title-25-chapter-4-unemployment/encodings/baseline-2026-10) | the unemployed worker | weekly benefit amount, base-period test, maximum total, partial-week payment, weekly eligibility, disqualification for how the job ended, requalifying, unsuitable work, pension offset, appeal days | 49 |
| [`code-of-alabama-1975-title-38-chapters-1-and-4-public-assistance/encodings/baseline-2026-10`](code-of-alabama-1975-title-38-chapters-1-and-4-public-assistance/encodings/baseline-2026-10) | the applicant for Family Assistance | eligibility, monthly grant, first-month grant, fair hearing | 27 |

What a person still cannot get from the deposited law: the Family Assistance payment standard (set by DHR outside any rule now in force, so an input), and the effect of Acts 2026-551 and 2026-604 on ss 40-18-14 and 40-18-15 (not deposited). Each encoding's NOTES.md lists its findings.
