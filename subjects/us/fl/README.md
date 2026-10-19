# florida/

Florida (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Online Sunshine — The Florida Legislature, The 2026 Florida Statutes; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTP/HTTPS GETs with an honest UA, about 10 requests spaced ~1.8 s apart. No block, challenge or rate limit. The site is plain server-rendered ColdFusion; chapter pages are addressed as index.cfm?App_mode=Display_Statute&URL=<range>/<chapter>/<chapter>.html. Every chapter page is headed 'The 2026 Florida Statutes', which is the currency marker; the site offers a year selector back to 1997.

## Topics with no legislation here

- **Leave/holiday pay**: No general state statute. Florida mandates no annual leave, sick leave, family leave or holiday pay, and § 218.077 and § 448.077 preempt local ordinances on employment benefits. The only statutory leave mandate is three days of domestic-violence leave under Fla. Stat. § 741.313, which is too narrow to stand as the principal statute for the topic. Family and medical leave generally is federal (FMLA, 29 U.S.C. ch. 28).
- **Termination/severance**: No state statute. Florida is an at-will state with no severance entitlement and no mini-WARN Act. Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq. The statutory consequence of job loss is reemployment assistance under Fla. Stat. ch. 443.
- **Personal tax/withholding**: No such tax exists. Florida levies no personal income tax and the state constitution forbids one without an amendment (Fla. Const. art. VII, § 5(a)), so there is no state withholding regime. Personal income tax and wage withholding are federal (26 U.S.C. §§ 1, 3401-3406).
- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250).
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Florida's own immigration provisions (Fla. Stat. § 448.095, mandatory E-Verify) enforce the federal scheme rather than conferring permission to work.

## Statute text deposited 2026-10-20: state benefits and the taxes and reliefs that fall on individuals

Florida levies **no personal income tax**. The deposited Constitution says why: art. VII, s 5(a) bars any state tax "upon the income of natural persons who are residents or citizens of the state ... in excess of the aggregate of amounts which may be allowed to be credited upon or deducted from any similar tax levied by the United States or any state". That federal credit is nil today, so in practice no tax can be levied -- unverified (general knowledge); no Florida statute imposing one was found. The sample is therefore state benefits plus the property-tax reliefs an individual can claim. Five files, in five subjects, were deposited as unofficial plain text from Online Sunshine (www.leg.state.fl.us), **The 2026 Florida Statutes**, fetched 2026-10-19 UTC.

| Subject | File | What it gives a person | Characters |
| --- | --- | --- | --- |
| `the-2026-florida-statutes-title-xxxi-chapter-443-reemployment` (new) | `fla-stat-ch443` | Fla. Stat. ch. 443, Reemployment Assistance: weekly benefit amount 1/26 of the high quarter, $32-$275 (s 443.111(3)); total benefits 25% of base-period wages, capped at $6,325, with weeks indexed to the state unemployment rate (s 443.111(5)); eligibility (s 443.091); disqualification (s 443.101); claims (s 443.151) | 340,901 |
| `the-2026-florida-statutes-title-xxx-chapter-414-family-self` (existing; text added) | `fla-stat-ch414` | Fla. Stat. ch. 414, temporary cash assistance (TANF): eligibility, work requirements, the three-tier shelter payment standard table (s 414.095(10)), the $200-plus-half earned income disregard (s 414.095(11)), time limits (s 414.105) | 134,348 |
| `the-2026-florida-statutes-title-xxx-section-409-212-optional-supplementation` (new) | `fla-stat-s409-212` | Fla. Stat. s 409.212: optional state supplementation of SSI for people in assisted living, adult family-care homes and similar placements | 4,373 |
| `the-2026-florida-statutes-title-xiv-chapter-196-exemption` (new) | `fla-stat-ch196` | Fla. Stat. ch. 196, property tax exemptions: homestead (s 196.031), additional exemption for persons 65+ on limited household income (s 196.075), disabled veterans (ss 196.081, 196.091, 196.24), total and permanent disability (s 196.101), widows, widowers, blind and disabled (s 196.202), annual application (s 196.011) | 251,570 |
| `florida-constitution-article-vii-finance-and-taxation` (new) | `fla-const-art7` | Fla. Const. art. VII: the income tax limit (s 5), homestead exemptions and their inflation adjustment (s 6), household-goods exemption for widows, widowers and disabled persons (s 3(b)), assessment limits (s 4) | 49,643 |

**How the pieces connect, as read in the deposited texts:**

- **Constitution to statute.** Art. VII s 6 grants the homestead exemption and authorises the extra exemptions for persons 65 and older; ch. 196 carries them out, and s 196.075(2) says it is enacted "In accordance with s. 6(d), Art. VII of the State Constitution".
- **Federal income tax.** For the 65+ exemption, "household income" means "the adjusted gross income, as defined in s. 62 of the United States Internal Revenue Code" (s 196.075(1)(b)); an audited applicant must sign IRS Form 8821 or 4506. IRC s 62 is in `subjects/us/internal-revenue-code-of-1986` (`usc26-ch1-schB-ptI-III.txt`).
- **Social Security disability.** A "totally and permanently disabled person" is one certified as such by two Florida physicians, the US Department of Veterans Affairs, or the Social Security Administration (s 196.012(11); the same wording in s 196.202(1)). Disabled first responders may prove disability with SSA documentation (s 196.102).
- **Reemployment assistance and federal law.** Ch. 443 is to be construed to meet the requirements of SSA Title III and FUTA (s 443.031); s 443.036 defines reemployment assistance by reference to 26 U.S.C. 3301-3311 and 42 U.S.C. 501-504. New claimants must be told that "Reemployment assistance is subject to federal income tax" and may elect federal withholding (s 443.151). Retirement benefits under the Social Security Act to which the claimant contributed may not reduce benefits for that contribution (s 443.101). IRC s 85 is deposited in the IRC subject; FUTA (IRC ch. 23) is indexed there but not deposited.
- **TANF.** "Temporary cash assistance" means cash assistance under the state programme certified under Title IV-A of the Social Security Act (s 414.0252(12)); the chapter does not create an entitlement under Title IV-A (s 414.025(2)). Where the only parent (or both parents) receive SSI under Title XVI, SSI recipients are excluded from the household in fixing the amount of cash assistance, to the extent federal law permits (s 414.045). Title IV-A is indexed in `subjects/us/social-security-act` but not deposited there.
- **SSI supplement.** S 409.212 pays optional supplementation to a person "receiving a Supplemental Security Income check", requires facilities to comply with 42 U.S.C. 1382e(e), and raises the rate with the federal cost-of-living adjustment. SSA Title XVI, including s 1616 (42 U.S.C. 1382e), is deposited in `subjects/us/social-security-act` (`usc42-ch7-schXVI.txt`).
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`); ch. 414 refers to "food assistance" sanctions run under federal regulations.

**Terms.** Read 2026-10-19 (UTC). There is no terms-of-use page; the privacy statement (https://www.leg.state.fl.us/cgi-bin/View_Page.pl?File=privacy.html&Directory=welcome/&Location=app&Tab=info_center&Submenu=4) covers only data collection, and every page carries the footer "Copyright (c) 1995-2026 The Florida Legislature". robots.txt: `User-agent: *` disallows only /employees/; Drifter and SemrushBot are barred; no Crawl-delay. Verdict: **clean** in practice (a bare site copyright notice, no permission requirement, no ban on modification). The text itself is uncopyrightable (*Georgia v. Public.Resource.Org*, 2020). The History lines are kept; the Legislature's editorial "Note." paragraphs and their footnote markers are omitted.

**Gaps.**
- The editorial notes omitted from the texts sometimes carry effective-date or contingency information; consult Online Sunshine for any section that had a footnote.
- The Save Our Homes assessment cap (Fla. Stat. s 193.155) and the senior "granny flat" and deferral provisions (ch. 197) are not deposited; ch. 193 is too large for this sample.
- The OSS base rate is set by the department within appropriations (s 409.212(2)) and is not in statute. Florida Administrative Code (flrules.org) was not reachable for the plan (HTTP 522 at robots.txt) and is not sourced.
- The 2026 edition is the Legislature's annual compilation; laws from the 2026 session that take effect later may not be reflected.

## Administrative rules and official standards checked 2026-10-20

The question was where Florida sets the **amounts** a person gets: the TCA grant, the state SSI supplement (OSS), and the UI maximum weekly benefit.

**Added:** `florida-dcf-ess-program-policy-manual-appendix-a-5-and-a-12-cash-assistance-and-oss-standards` (new). It holds two appendices of the Department of Children and Families' ESS Program Policy Manual, deposited as unofficial text from the DCF PDFs, downloaded 2026-10-19 UTC.

| File | What it sets | Currency | Characters |
| --- | --- | --- | --- |
| `fl-ess-appendix-a-12-state-funded-programs-standards` | **Optional State Supplementation** (OSS). "Protected" cases (RTF not enrolled for ACS, and the 2001 "Gap" group): income standard and provider rate $1,179 for an individual / $2,261 for a couple; personal needs allowance $160; asset limit $2,000 / $3,000; **maximum OSS payment $345 / $690**. "Redesign" cases (ALF, AFCH, and RTF enrolled for ACS): income standard $1,072.40 / $2,047.80; provider rate $1,018.40 / $1,939.80; **maximum OSS payment $184.40 / $386.80**. Also Home Care for Disabled Adults limits and the SSI federal benefit rate ($994 / $1,491). | headed 01/01/2026; columns for January 2025 and January 2026 | 2,676 |
| `fl-ess-appendix-a-5-tca-income-standards` | **Temporary Cash Assistance**: the gross income limit (185% of FPL) and the consolidated need standard (100% of FPL), both effective April 2026; the Tier I/II/III payment standards (July 1996) by filing-unit size from 0.5 to 24, with the add-person increments | April 2026 / July 1996 | 3,924 |

**Which amounts now come from deposited text:**
- The OSS amounts. Fla. Stat. s 409.212(2) leaves the base rate to the department "within funds appropriated"; Appendix A-12 gives the figures. Read with care: the arithmetic Maximum OSS Payment = provider rate + $160 personal needs allowance - $994 federal benefit rate holds for both columns ($1,179 + $160 - $994 = $345), but that relationship is inferred, not stated in the appendix.
- The TCA payment standards were already in deposited statute (s 414.095(10); 1 person: $95 / $153 / $180). Appendix A-5 adds the current income tests and the half-person (Family Cap) rows. The two agree for sizes 1-10 as read.
- The UI maximum, $275 a week, is in the deposited statute, s 443.111(3).

**Terms.** DCF publishes no terms of use, copyright notice or licence on the pages read, and the PDFs carry none. Florida public-records law is generally taken to bar agency copyright without statutory authority: unverified (general knowledge). robots.txt: none on www.myflfamilies.com or ffic.myflfamilies.com (404). Verdict: clean.

**Not sourced:**
- **Florida Administrative Code** (flrules.org, incl. ch. 65A-1 and 65A-2). Its robots.txt returned HTTP 522 on 2026-10-19, so it was treated as disallowing everything; the same thing happened in the 2026-10-19 statute pass. FloridaCommerce (floridajobs.org) answered HTTP 403 to robots.txt and was not used.

**Remaining gaps:** the rule text of 65A-1 and 65A-2 F.A.C.; any mental-health supplement to the OSS amounts (s 409.212(2) and s 429.075), which A-12 does not show.
