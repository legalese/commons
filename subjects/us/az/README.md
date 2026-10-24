# arizona/

Arizona (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Arizona State Legislature - Arizona Revised Statutes; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text was deposited then; see the later sections. Two encodings were added on 2026-10-24.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Straightforward. Title indexes at https://www.azleg.gov/arsDetail/?title=<n> were fetched directly over HTTPS without a browser; six requests (titles 20, 23, 33, 38, 40, 43) plus the home page, spaced out. No block, no 403, no bot challenge, no rate limiting. Every title page carries the same currency and disclaimer statement, so the as-at position is uniform across the acts below.

## Topics with no legislation here

- **Passenger compensation**: Federal. Air passenger rights come from US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Arizona regulates motor carriers under Title 28 but has no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.

## Statute text deposited 2026-10-20: personal income tax and benefits

Selected sections of the Arizona Revised Statutes were deposited as unofficial plain text, for a sample on personal income tax and state benefits. The source is the Legislature's online A.R.S., fetched 2026-10-19 (UTC). The register says it is "updated to include the revised sections from the 57th Legislature, 2nd Regular Session" and that it "reflects the version of law that is effective on January 1st of the year following the most recent legislative session".

**The online text is unofficial.** The register says it is "primarily maintained for legislative drafting purposes" and that "The official version of the Arizona Revised Statutes is published by Thomson Reuters."

Whole chapters were out of reach. azleg.gov sets `Crawl-delay: 120` and publishes text one section per page; Title 43, chapter 10 alone has about 50 sections. The sections below were picked for what an individual needs to know.

| Subject | Sections | What it gives a person | Characters |
| --- | --- | --- | --- |
| `arizona-revised-statutes-title-43-taxation-of-income` (existing; text added) | 43-102, 43-104, 43-105 | Conformity: Arizona AGI is federal AGI, subject only to the title's modifications. The Internal Revenue Code applies as in effect on January 1, 2026, for taxable years from 2026 | 16,116 |
| same | 43-1001, 1002, 1011 (both versions), 1021-1023, 1041, 1042, 1071, 1072, 1072.01, 1073, 1073.01 | State income tax owed: rates; additions and subtractions, including Social Security; the age-65 and blind exemptions; deductions; the property tax credit for people aged 65 or over or on SSI; the excise tax credit; the family income tax credit; the dependent tax credit | 76,610 |
| `arizona-revised-statutes-title-23-chapter-4-employment-security` (existing; text added) | 23-605, 607, 609, 619.01, 621, 622, 771, 775-777, 779, 780, 791, 792 | Unemployment benefits: eligibility; disqualifications; the weekly benefit (1/25 of high-quarter wages, at most $320); duration (24 or 26 weeks, at most a third of base-period wages); reduction for pensions; tax withholding | 39,154 |
| `arizona-revised-statutes-title-46-chapter-2-article-5-temporary-assistance-for-needy-families` (new) | 46-101, 207, 207.01, 292, 294, 296, 298, 300 | Cash assistance (TANF): eligibility, amount, the 12-month limit and hardship extensions, minor parents, diversion, sanctions | 39,690 |
| `arizona-revised-statutes-title-46-chapter-2-article-3-supplemental-payment-programs` (new) | 46-251, 46-253 | The mandatory state supplement to SSI | 3,365 |
| `arizona-revised-statutes-title-42-property-tax-exemption-and-senior-tax-deferral` (new) | 42-11111, 42-17301-17303, 42-17311 | The property tax exemption for widows, widowers, people with disabilities and veterans with disabilities; deferral of residential property tax for owners aged 70 or older | 16,803 |

**How the pieces connect, as read in the deposited texts:**

- **Federal income tax.** The legislature intends the adjusted gross income an individual reports to the IRS to "be the identical sum reported to this state, subject only to modifications contained in this title" (43-102). "Federal adjusted gross income" is AGI computed under the Internal Revenue Code (43-1001). For taxable years beginning after December 31, 2025, the Code applies as in effect on January 1, 2026; earlier years use earlier dates (43-105). The federal text is in `subjects/us/internal-revenue-code-of-1986`.
- **Tax rate.** The register prints two versions of 43-1011, one from Laws 2021, ch. 411 and one from Laws 2021, ch. 412. The second sets a flat 2.5% "for taxable years beginning from and after December 31 of the year in which notice is provided to the department pursuant to section 43-243". Section 43-243 is not deposited. The plan says the flat 2.5% applies now; that is unverified (general knowledge). Settle it from 43-243 and the session laws before encoding the rate.
- **Social Security benefits.** Arizona subtracts "the amount included in federal adjusted gross income pursuant to section 86 of the internal revenue code" (43-1022). So whatever part of the benefits the federal government taxes, Arizona does not. IRC s86 is deposited in the IRC subject (`usc26-ch1-schB-ptI-III.txt`).
- **Credits.** The dependent tax credit is $125 for each dependent under 17 and $25 for each older dependent. It is reduced above $200,000 of *federal* AGI ($400,000 for a joint return) (43-1073.01). The family income tax credit and the excise tax credit depend on income thresholds (43-1073, 43-1072.01). The property tax credit is open to residents aged 65 or over and to "a recipient of public monies under title 16 of the social security act", that is, SSI (43-1072). SSA Title XVI is deposited in `subjects/us/social-security-act` (`usc42-ch7-schXVI.txt`). No state EITC appears in the sections read.
- **Unemployment insurance.** A new claimant is told that "unemployment compensation is subject to federal and state tax". The claimant may elect federal withholding, and state withholding at 10% of the federal amount (23-792). Federal tax on benefits is IRC s85, deposited in the IRC subject. 43-1022 as read has no subtraction for UI benefits, so the benefits stay in Arizona income through federal AGI. Benefits are reduced by certain pension payments (23-791). The federal-state frame (FUTA; SSA Titles III and IX) is unverified (general knowledge) here: the sections that define FUTA and the Internal Revenue Code for UI purposes (23-625.02 and others) were not fetched.
- **Cash assistance.** 46-101 defines two terms. "Temporary assistance for needy families" means assistance under section 403 of Title IV of the Social Security Act as it exists after August 21, 1996. "Cash assistance" means TANF paid to meet basic living expenses. For non-citizens, eligibility refers to PRWORA (Public Law 104-193) (46-292). Title IV-A is indexed in `subjects/us/social-security-act`, but its text is **not deposited** there.
- **State supplement to SSI.** The mandatory supplement goes to people who received the old state adult assistance in December 1973 and who receive SSI under Title XVI, or would but for their income (46-251). A person who refuses SSI they are eligible for is ineligible (46-253).
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`). Arizona's SNAP sections (46-219, 46-231) were not sourced.

**Terms.** Read 2026-10-19 (UTC) at https://www.azleg.gov/arstitle/. There is no separate terms page. Besides the disclaimer quoted above, the only statement is the footer: "(c) 2026 Arizona State Legislature. All Rights Reserved". It asks for no permission and does not forbid modification. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020). Only the unannotated statutory text is deposited: the section pages carry no publisher annotations, only the Legislative Council's short version notes. robots.txt allows the pages used and sets `Crawl-delay: 120`. Verdict: **conditions**, met. Each subject's SOURCE-LICENSE.md has the detail.

**Access record.** 55 requests to www.azleg.gov: robots.txt 3 times, the /arstitle/ page, 4 title indexes (titles 23, 42, 43 and 46) and 47 requests for the 46 section pages (54 answered HTTP 200). One request (43-104) failed on a local DNS lookup and succeeded when retried later. No 403, 429 or challenge.

**One crawl-delay breach.** At the start of the second run, robots.txt was re-read 67 seconds after the previous request (2026-10-19T17:52:16Z, then 17:53:23Z), short of the 120-second delay. The fetch script used a fixed 31-second delay for robots.txt before it had learnt the host's delay. The script was corrected, and the third run kept to the delay. Every other request came at least 121 seconds after the one before.

**Gaps.**
- The text is unofficial and covers selected sections, not whole chapters. Missing: Title 43 chapter 10 article 6 (nonresidents), the remaining credits, 43-243 (needed to settle the rate), chapter 4 (withholding), and most of Title 23 chapter 4.
- **The plan's "senior property valuation protection" citation (A.R.S. 42-17301 ff.) was wrong.** 42-17301 ff. is the *residential property tax deferral* for owners aged 70 or older, which is deposited instead. The Title 42 index shows no statutory article for the senior valuation protection option, which rests on Ariz. Const. art. IX, s 18. The Constitution was not fetched.
- The inflation-adjusted standard deduction and other dollar amounts the department adjusts are not sourced.
- The Arizona Administrative Code (DES rules on cash assistance and UI) is not sourced: apps.azsos.gov answered 403 to this user agent in the set-up check.

## Encodings: tax and benefits (2026-10-24)

Two baseline encodings, each from the seat of the individual and checked with the stable `l4` (1.6.98): 0 errors, 0 warnings, every assertion satisfied.

| Encoding | Seat | Questions | Assertions |
|---|---|---|---|
| [`arizona-revised-statutes-title-43-taxation-of-income/encodings/baseline-2026-10`](arizona-revised-statutes-title-43-taxation-of-income/encodings/baseline-2026-10) | the individual taxpayer (full-year resident) | resident, must I file, when to pay, exemptions, dependent credit, excise tax credit, tax owed after credits | 39 |
| [`arizona-revised-statutes-title-46-chapter-2-article-5-temporary-assistance-for-needy-families/encodings/baseline-2026-10`](arizona-revised-statutes-title-46-chapter-2-article-5-temporary-assistance-for-needy-families/encodings/baseline-2026-10) | the applicant for cash assistance | conditions (incl. the 12- and 60-month limits), counted earnings, dependent care disregard, the 130% child-only test, the statutory floor, diversion, sanctions | 38 |

**Rate settled in part.** The gap the 2026-10-20 deposit recorded (s 43-243 missing) is closed: ss 43-243, 43-301 and 43-501 were fetched on 2026-10-24 (4 requests, 125 seconds apart, all HTTP 200) and deposited as `arizona-revised-statutes-title-43-taxation-of-income/registers/source-bundle/az-ars-43-ss243-301-501-2026-10-24.txt`. Section 43-243 makes the flat 2.5% apply from the year after a revenue notice is received; the deposited law does not say when (or whether) it was, so the encoding asks for that year.

**Still missing for a person's full answer:** the department's inflation-adjusted standard deduction and brackets; the DES cash assistance amount by family size; DES rules on resources and work activities (s 46-299). The Arizona Administrative Code host (apps.azsos.gov) answered 403 in the 2026-10-19 set-up check and was not retried.
