# georgia/

Georgia (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Official Code of Georgia Annotated, public access edition — published for the Georgia Code Revision Commission by LexisNexis (linked from the Georgia General Assembly site as 'Georgia Code'); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

legis.ga.gov is a JavaScript application that returns only a loading shell to scripted clients and to WebFetch, and its /laws/ path 404s, so the General Assembly home page was read in a browser; its single 'Georgia Code' link points to http://www.lexisnexis.com/hottopics/gacode, which redirects into an advance.lexis.com container. The table of contents was read in that browser: titles, chapters and article/section headings for Titles 33, 34, 44, 46, 47, 48 and 49 were expanded and recorded. Opening an individual section document then triggered a CAPTCHA ('Captcha Validation — We use CAPTCHA on this site to prevent automated software from overburdening the system'). I stopped there and did not attempt to solve or bypass it. Consequence: chapter and section headings are verified from the register's own TOC, but I could not read a 'current through' currency statement or an individual section's text, so no as-at date is recorded for Georgia.

## Topics with no legislation here

- **Termination/severance**: No state statute. Georgia is an at-will state (O.C.G.A. § 34-7-1) with no severance entitlement and no mini-WARN Act; the Title 34 table of contents shows no plant-closing or layoff-notice chapter (Chapters 11, 12, 13 and 15 are 'Reserved'). Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Georgia legislates around the edges of the federal scheme — the Georgia Security and Immigration Compliance Act requires public employers and their contractors to use E-Verify (O.C.G.A. § 13-10-91) and § 50-36-1 requires verification of lawful presence for public benefits — but no Georgia statute confers permission to work.

## Tax and benefits sample (2026-10-24)

A connected sample on personal income tax and benefits. The O.C.G.A. is still not deposited: its public access site (LexisNexis) puts each section behind a CAPTCHA, as recorded above. The sample was built from two other official sources, both read on 2026-10-24.

**The General Assembly's session laws.** www.legis.ga.gov serves each bill as a public PDF at `/api/legislation/document/<session>/<id>`. The document ids were read from the legislature's own bill pages in a browser. The site's data API answers 401 to scripted clients and was not used. The site footer reads "COPYRIGHT © 2026 THE GEORGIA GENERAL ASSEMBLY", and no terms of use page was found. Enacted bills are government edicts and not copyrightable (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)).

**The Secretary of State's Rules and Regulations of the State of Georgia.** These are at https://rules.sos.ga.gov, hosted by Fastcase. robots.txt allows `/gac/` with a 2-second crawl delay. The footer reads "Copyright © 2026 Fastcase, Inc - All rights reserved.", and no terms page was found. Agency rules are government edicts too. The footer is flagged for Michael.

| subject | deposited | encoding |
|---|---|---|
| [`official-code-of-georgia-annotated-title-48-revenue-and`](official-code-of-georgia-annotated-title-48-revenue-and) | HB 463 (2026, Act 465), the "Georgia Economic Growth and Tax Relief Act of 2026", as passed, with a sidecar recording its strike-through and underlining; HB 1000 (2026, Act 374), the one-time refund (48-7-20.4) | `encodings/baseline-2026-10/`, the individual taxpayer's seat: the 4.99% rate for 2026 and its annual steps to 3.99% with their delays, the standard deduction ($15,000 / $30,000 for 2026), the dependent exemption ($5,000), the retirement exclusion, the overtime and tips subtractions, the tax for a full-year resident, and the one-time refund ($250 / $375 / $500) |
| [`rules-of-the-georgia-department-of-labor-300-2-4`](rules-of-the-georgia-department-of-labor-300-2-4) (**new**) | Rules 300-2-4-.01 to -.13, Unemployment Insurance Benefit Payments | `encodings/baseline-2026-10/`, the claimant's seat: registering for work, the weekly request for payment and its two-week limit, work search, reporting late with good cause, and overpayment waivers and appeals |

**How they connect.** Georgia taxable net income starts from federal adjusted gross income (48-7-27(a)), which the Internal Revenue Code encoding answers (`../internal-revenue-code-of-1986/`). Unemployment compensation is federal gross income under 26 U.S.C. 85, so it reaches the Georgia tax through federal AGI.

**Benefits: why unemployment insurance and not TANF.** Georgia's TANF statute (O.C.G.A. 49-4-180 et seq.) is in the O.C.G.A. and so is not available. The Department of Human Services rules (Department 290) have no TANF chapter, and payment standards are set in the Department's manual. The Department of Labor's rules state the claimant's duties most completely. The amounts of unemployment insurance are in O.C.G.A. 34-8 (not deposited).

**Still to do.** Deposit O.C.G.A. 48-7 and 34-8 from a permitted source. That would bring in residency, the filing duty, the other subtractions and additions, and the weekly benefit amount.
