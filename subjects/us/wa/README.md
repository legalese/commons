# washington/

Washington (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Revised Code of Washington (RCW) - Washington State Legislature / Office of the Code Reviser; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

app.leg.wa.gov WORKED for this run - no 403. (An earlier wave of this job reported app.leg.wa.gov returning 403; that did not recur.) Fetched over plain HTTPS with curl and an honest self-identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon corpus; metadata only)'). 12 requests, spaced ~2 seconds apart: the RCW index at https://app.leg.wa.gov/RCW/, nine chapter/title pages via https://app.leg.wa.gov/RCW/default.aspx?cite=<cite> (49.48, 50A, 50.20, 41.40, 74.04, 48.30, 80.28, 59.18 and 82.87), and the site-wide disclaimer at https://leg.wa.gov/disclaimer/. All HTTP 200, server-rendered HTML, no bot challenge and no rate limiting. The ALTERNATIVE HOST was probed as the task instructed: https://leg.wa.gov/ answers (200) and carries the Legislature's disclaimer and privacy pages, but https://leg.wa.gov/code-reviser/revised-code-of-washington/ is a soft 404 ('Page not found' rendered with a 200 status), so leg.wa.gov does not itself serve RCW text - app.leg.wa.gov/RCW is the working RCW host. Every page displays a maintenance banner: 'The Legislature website will be offline intermittently between 7 AM - 7 PM on Saturday, September 26 for scheduled maintenance.'

## Topics with no legislation here

- **Personal tax/withholding**: Does not exist in Washington as a wage-withholding regime. Washington levies no personal income tax, so there is no state income tax withholding statute and no state counterpart to federal wage withholding under 26 U.S.C. ch. 24 (s 3401 et seq.), which is the operative law for a Washington employee. The only state tax imposed on an individual's income is the capital gains excise tax, chapter 82.87 RCW, which I did verify on the register (fetched https://app.leg.wa.gov/RCW/default.aspx?cite=82.87, HTTP 200, breadcrumb 'Home / State laws and rules / RCWs / Title 82 / Chapter 82.87', heading 'Chapter 82.87 RCW - CAPITAL GAINS TAX'): it is self-assessed and self-reported by the individual with no employer withholding, so it does not answer this topic. The payroll deductions that do exist in Washington are contributions rather than income tax withholding: Paid Family and Medical Leave premiums under chapter 50A.10 RCW and long-term services and supports premiums under chapter 50B.04 RCW.
- **Passenger compensation**: Federal matter, and largely regulation rather than statute. Air passenger rights are pre-empted by the Airline Deregulation Act, 49 U.S.C. s 41713, and administered by the US Department of Transportation under 14 C.F.R. parts 250 and 259; rail passenger rights arise under 49 U.S.C. subtit. V. There is no state-level passenger compensation statute.
- **Customs/duties**: Federal matter. Customs duties and import procedure are exclusively federal (U.S. Const. art. I, s 8, cl. 1; Tariff Act of 1930, 19 U.S.C. ch. 4; Harmonized Tariff Schedule). No US state legislates on customs.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and 8 C.F.R. part 274a. States may not issue work permits.

## Statute text deposited 2026-10-24: the personal tax Washington levies, and TANF

Washington levies **no personal income tax** on wages: none of the deposited chapters, and nothing found on the register, imposes one (the README's "Personal tax/withholding" note above). The one tax on an individual's income is the **capital gains excise tax**, chapter 82.87 RCW, which is deposited. For benefits, the TANF chapters and the state cash programme for aged, blind or disabled adults are deposited. Source: the full-chapter pages of app.leg.wa.gov/RCW, retrieved 2026-10-24 (UTC), converted to plain text (unofficial). 90 sections, about 141,500 characters in 4 files.

| Subject | Chapter | What it gives a person | Sections | Characters |
| --- | --- | --- | --- | --- |
| `revised-code-of-washington-chapter-82-87-capital-gains-tax` (new) | 82.87 RCW | the 7% tax on Washington capital gains over the standard deduction, and 2.9% more above $1,000,000 (82.87.040), exemptions (82.87.050), deductions (82.87.060-.080), allocation and the credit for other states' tax (82.87.100), returns, payment and amendment (82.87.110), joint filers (82.87.120), annual adjustment (82.87.150) | 18 | 45,490 |
| `revised-code-of-washington-chapters-74-12-and-74-08a-temporary-assistance-for-needy-families` (new) | 74.12 and 74.08A RCW | TANF: dependent child (74.12.010), eligibility (74.12.030, .035), the 60-month limit and hardship exemptions (74.08A.010), the earnings disregard (74.08A.230), SSI not counted (74.08A.039), work activities and sanctions (74.08A.260), good cause (74.08A.270), diversion (74.08A.210) | 22 + 46 | 22,146 + 63,039 |
| `revised-code-of-washington-chapter-74-62-aged-blind-or-disabled-assistance` (new) | 74.62 RCW | the aged, blind, or disabled assistance programme, pregnant women assistance, and essential needs and housing support (74.62.030) | 4 | 10,834 |

**Terms**: the Legislature's disclaimer says the Statute Law Committee "claims copyright" for the RCW and asks anyone "intending to obtain the Revised Code of Washington ... for the purpose of selling the same" to contact it; it sets no other condition. Commons is non-commercial (ruled 2026-10-20), so the text is deposited. app.leg.wa.gov has no robots.txt (404). Details in each subject's `SOURCE-LICENSE.md`.

**Gaps**: RCW 74.08.025 (the general eligibility conditions RCW 74.12.030 refers to), RCW 82.32 (administration, penalties for late payment), the payment standards and need standards (set by the Department of Social and Health Services in WAC 388-478, not deposited), and the Department of Revenue's published annual capital gains amounts (RCW 82.87.150) are not here. Unemployment compensation (Title 50) is still indexed only.

## Encodings added 2026-10-24: tax and benefits baselines

Two baseline encodings, written from the individual's seat with the 2026-10-18 defaults and checked with the stable `l4` (1.6.98). Each folder's `NOTES.md` has the method, scope and findings.

| Encoding | Seat | Questions | Regulative rules | Assertions |
| --- | --- | --- | --- | --- |
| [`revised-code-of-washington-chapter-82-87-capital-gains-tax/encodings/baseline-2026-10`](revised-code-of-washington-chapter-82-87-capital-gains-tax/encodings/baseline-2026-10) | the individual who sells long-term capital assets | does Washington tax my wages (no); am I a resident (82.87.020(11)); is the sale exempt (82.87.050); is the gain allocated to Washington (82.87.100(1)); how much tax (82.87.040-.080, .100(2), .160); must I file, jointly (82.87.110(1), .120); the late-filing penalty (82.87.110(6)) | 3 (file by the federal due date or matched extension; pay by the original date; amend within 90 days of a final federal change, 82.87.110) | 37 / 37 |
| [`revised-code-of-washington-chapters-74-12-and-74-08a-temporary-assistance-for-needy-families/encodings/baseline-2026-10`](revised-code-of-washington-chapters-74-12-and-74-08a-temporary-assistance-for-needy-families/encodings/baseline-2026-10) | the parent or relative applying for TANF | dependent child (74.12.010, .035); countable earnings and the grant (74.08A.230, .035, .039); the 60-month limit and exemptions (74.08A.010); transitional food assistance (74.08A.010(6)); good cause (74.08A.270); the work sanction (74.08A.260); diversion assistance (74.08A.210) | 1 (engage in work activities within two months, or by month twelve before termination, 74.08A.260(4)) | 42 / 42 |

Inputs, not deposited: the Department of Revenue's annual capital gains amounts and the DSHS payment standard and maximum earned income level.
