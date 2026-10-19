# vermont/

Vermont (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Vermont Statutes Online - Vermont General Assembly (Office of Legislative Counsel); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over plain HTTPS with curl and an honest self-identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon corpus; metadata only)'). About 17 requests, spaced ~2 seconds apart: the statutes index, title pages for Titles 3, 8, 9, 21, 30, 32 and 33, chapter pages for 3 V.S.A. ch. 15 and ch. 16, 8 V.S.A. ch. 129, 9 V.S.A. ch. 137, 21 V.S.A. ch. 5, 30 V.S.A. ch. 5, 32 V.S.A. ch. 151 and 33 V.S.A. ch. 11, plus the site-wide disclaimers page. All returned HTTP 200 as server-rendered HTML - no JavaScript shell, no bot challenge, no 403, no rate limiting. Title URLs are zero-padded (/statutes/title/03, /08, /09); unpadded forms return HTTP 404, which is how three first attempts failed. Subchapter-level URLs do not exist, so the citable register page for a subchapter is its chapter page, which prints the subchapter heading and its section list. IMPORTANT CURRENCY CAVEAT: the site states it is current only through the 2025 session, so 2026-session acts are not yet merged - 21 V.S.A. s 346 still shows the forward-looking marker '[Repealed effective July 1, 2026]' even though that date has passed.

## Topics with no legislation here

- **Passenger compensation**: Federal matter, and largely regulation rather than statute. Air passenger rights are pre-empted by the Airline Deregulation Act, 49 U.S.C. s 41713, and administered by the US Department of Transportation under 14 C.F.R. parts 250 and 259; rail passenger rights arise under 49 U.S.C. subtit. V. There is no state-level passenger compensation statute.
- **Customs/duties**: Federal matter. Customs duties and import procedure are exclusively federal (U.S. Const. art. I, s 8, cl. 1; Tariff Act of 1930, 19 U.S.C. ch. 4; Harmonized Tariff Schedule). No US state legislates on customs.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and 8 C.F.R. part 274a. States may not issue work permits.

## Statute text deposited 2026-10-20: personal income tax and benefits

Five chapters of the Vermont Statutes were deposited as unofficial plain text, for a sample on personal income tax and state benefits. Each chapter is whole. The source is **Vermont Statutes Online** (Office of Legislative Counsel), fetched 2026-10-19 (UTC). The pages now say: "The Statutes below now include the actions of the 2026 session of the General Assembly" (the 2025-session caveat in *Register access* above is out of date). **The online text is unofficial**: "The Vermont Statutes Online is an unofficial copy of the Vermont Statutes Annotated that is provided as a convenience." The official Vermont Statutes Annotated is published by LexisNexis and was not used.

| Subject | Chapter | What it gives a person | Characters |
| --- | --- | --- | --- |
| `vermont-statutes-annotated-title-32-taxation-and-finance` (existing; text added) | 32 V.S.A. ch. 151 | State income tax owed: taxable income from federal AGI with Vermont modifications (5811(21)), the rate tables (5822), the earned income tax credit (5828b), the child and dependent care credit (5828c), the Social Security exclusion (5830e), the child tax credit (5830f), withholding (subch. 4) | 321,436 |
| `vermont-statutes-annotated-title-32-chapter-154-homestead-property-tax-credit-and-renter-credit` (new) | 32 V.S.A. ch. 154 | The homeowner's property tax credit and the renter credit, scaled to household income (6061, 6066, 6066a) | 104,364 |
| `vermont-statutes-annotated-title-21-chapter-17-unemployment-compensation` (new) | 21 V.S.A. ch. 17 | Unemployment benefits: qualifying wages and the weekly benefit amount (1338), partial benefits (1339), disqualifications (1344), claims (1346) | 288,156 |
| `vermont-statutes-annotated-title-33-human-services-chapter-11` (existing; text added) | 33 V.S.A. ch. 11 | Reach Up, Vermont's TANF cash assistance: eligibility and benefit levels (1103), the 60-month limit (1108), work requirements (1113), sanctions (1116) | 72,940 |
| `vermont-statutes-annotated-title-33-chapter-13-aid-to-the-aged-blind-and-disabled` (new) | 33 V.S.A. ch. 13 | Aid to the Aged, Blind, and Disabled, the state supplement for people on SSI (1301-1307) | 8,924 |

**How the pieces connect, as read in the deposited texts:**

- **Federal income tax.** For an individual, Vermont "taxable income" is federal adjusted gross income, increased and decreased by listed items, less a Vermont personal exemption and standard deduction (5811(21)). The federal income tax laws are adopted "as in effect on December 31, 2025, but without regard to federal income tax rates under 26 U.S.C. § 1" (5824), a fixed conformity date. The federal text is in `subjects/us/internal-revenue-code-of-1986`.
- **Social Security benefits.** Vermont excludes federally taxable Social Security benefits in full for federal AGI up to $55,000 (single, married filing separately, head of household and surviving spouse) or $70,000 (married filing jointly), phased out over the next $10,000 (5830e(a), with 5811(21)(B)(iv)). The federal inclusion rule is IRC s86 (deposited in the IRC subject, `usc26-ch1-schB-ptI-III.txt`).
- **Earned income tax credit.** A Vermont resident who is entitled to the federal EITC gets a refundable credit of 38% of it with qualifying children, or 100% without (5828b(a)). IRC s32 is deposited in the IRC subject. The child and dependent care credit is 72% of the federal credit (5828c).
- **Child tax credit.** The Vermont child tax credit is open to a person entitled to the federal child tax credit, or who would be but for a missing taxpayer identification number. It phases out above $125,000 AGI and is disregarded as income or resources for benefits, as the federal EITC is (5830f).
- **Property tax credit and renter credit.** "Household income" starts from federal AGI and adds back, among other things, cash public assistance and "payments received under the federal Social Security Act" (6061(5)(B)). The renter credit uses its own measure of income, also built on federal AGI (6061(18)). So the benefits in this set raise the income that the credits are measured against.
- **Unemployment insurance.** Definitions are keyed to the Federal Unemployment Tax Act (1301(6)). A claimant may elect federal income tax withholding from benefits; one who does also has Vermont tax withheld at 24% of the federal rate (1338). Federal tax on benefits is IRC s85 (deposited in the IRC subject). Vermont's own treatment of benefits follows from starting at federal AGI; no ch. 151 subtraction for benefits was found (unverified (general knowledge) beyond that search).
- **Reach Up.** TANF is defined as the block grant under Part A of Title IV of the Social Security Act, and work activities count only as Title IV-A allows (1101(26), (28)). Title IV-A is indexed in `subjects/us/social-security-act`, but its text is **not deposited** there.
- **Aid to the Aged, Blind, and Disabled.** An applicant must be "a recipient of federal Supplemental Security Income, if eligible" (1301), the resource limit is SSI's (1305), and the State may have the federal government administer the supplement under Title XVI (1309). SSA Title XVI is deposited in `subjects/us/social-security-act` (`usc42-ch7-schXVI.txt`).
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`); no Vermont SNAP provisions were sourced.

**Terms.** Read 2026-10-19 (UTC) at https://legislature.vermont.gov/home/site-resources/disclaimers. The page gives liability and accuracy disclaimers ("The website is not intended to replace any official source.") and bars tampering with the site; it sets no condition on copying the statutes. The footer says "Copyright 2026 State of Vermont. All rights reserved." robots.txt sets `Crawl-delay: 30` and disallows only bill-status loaders; requests were spaced at least 31 seconds apart, 10 in all. Verdict: **conditions**, met. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020). The history lines and effective-date notes are the Office of Legislative Counsel's; there are no vendor annotations. Each subject's SOURCE-LICENSE.md has the detail.

**Gaps.**
- The text is unofficial. Compare it with the Vermont Statutes Annotated before relying on a result.
- The inflation-adjusted personal exemption, standard deduction and bracket amounts for the current tax year are set by the Commissioner of Taxes (5811(21)(D), 5822) and are not sourced.
- Chapter 154 is printed in two versions (the one in force until a contingency is met, and the one effective July 1, 2029 if it is met), with several subdivisions also split at July 1, 2027. All versions are kept. The site prints 39 of these section versions twice, word for word; each is deposited once.
- Agency rules (Reach Up and AABD standards and payment levels, Department of Labor UI rules) are not sourced. The official rules are hosted by LexisNexis, whose terms bar automated access.
- Other Title 33 programmes (Medicaid; General Assistance and emergency assistance) are not deposited; their chapter numbers were not checked.
