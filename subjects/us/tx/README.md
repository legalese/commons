# texas/

Texas (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the Texas Constitution and Statutes (Texas Legislative Council); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Topics with no legislation here

- **Personal tax/withholding**: Texas has no personal income tax. Texas Constitution art. VIII, § 24-a (verified on the register at CN.8: 'INDIVIDUAL INCOME TAX PROHIBITED', added Nov. 5, 2019) forbids the legislature from taxing individuals' net incomes. Income tax withholding is federal (Internal Revenue Code).
- **Passenger compensation**: Federal. Air passenger rights come from US DOT regulations (14 CFR Part 250, 259) and federal preemption of state airline regulation (Airline Deregulation Act, 49 U.S.C. 41713). There is no Texas statute on passenger compensation.
- **Customs/duties**: Federal. Customs and import duties are exclusively federal (19 U.S.C., CBP). Texas statutes only touch port-of-entry authorities and trade zones, which do not govern duties.
- **Work permits/immigration**: Federal (Immigration and Nationality Act, 8 U.S.C.). Government Code chs. 752-753 ('IMMIGRATION') cover local cooperation with federal immigration enforcement, not work authorisation, so they are not listed.

## Statute text deposited 2026-10-20: state benefits and the taxes and reliefs that fall on individuals

Texas has **no personal income tax**, confirmed in the deposited text: Tex. Const. art. VIII, s 24-a, "INDIVIDUAL INCOME TAX PROHIBITED" ("The legislature may not impose a tax on the net incomes of individuals ..."; added Nov. 5, 2019). So the sample is state benefits plus the property-tax reliefs an individual homeowner can claim. Six files, in five subjects, were deposited as unofficial plain text. The source is the Texas Legislative Council's own "Zipped Chapter HTML" downloads (https://tcss.legis.texas.gov/resources/Zips/<CODE>.htm.zip, linked from the Download page of statutes.capitol.texas.gov), fetched 2026-10-19 UTC. The chapter pages on statutes.capitol.texas.gov are now a JavaScript app with no text in the HTML; the download files are the same text.

| Subject | File | What it gives a person | Currency (file date; latest credit) | Characters |
| --- | --- | --- | --- | --- |
| `labor-code-title-4-subtitle-a-texas-unemployment-compensation` (existing; text added) | `tex-lab-code-ch201-general-provisions` | Tex. Lab. Code ch. 201: the Act's definitions (base period, benefit year, wages, employment) | 2026-05-14; 88th Leg. R.S. (2023) | 48,597 |
| same | `tex-lab-code-ch207-benefits` | Tex. Lab. Code ch. 207: weekly benefit amount (1/25 of the highest base-period quarter, s 207.002), maximum benefits (s 207.005), eligibility (s 207.021), disqualifications incl. pensions (s 207.050) | 2026-05-14; 89th Leg. R.S. (2025) | 55,521 |
| `human-resources-code-chapter-31-financial-assistance-and` (existing; text added) | `tex-hum-res-code-ch31` | Tex. Hum. Res. Code ch. 31: TANF cash assistance -- eligibility, the personal responsibility agreement and sanctions (ss 31.0031-31.0033), time limits, work programmes | 2026-09-01; no session credit after 86th Leg. found | 90,034 |
| `tax-code-chapter-11-taxable-property-and-exemptions` (new) | `tex-tax-code-ch11` | Tex. Tax Code ch. 11: residence homestead exemption ($140,000 school, plus $60,000 if 65 or older or disabled, s 11.13(b)-(c)), disabled veterans (ss 11.22, 11.131), school-tax ceiling for 65+/disabled (s 11.26), applications (s 11.43) | 2026-09-01; 89th Leg. R.S. (2025) | 329,902 |
| `tax-code-section-33-06-tax-deferral-on-residence-homestead` (new) | `tex-tax-code-ss33-06-33-065` | Tex. Tax Code ss 33.06 and 33.065 only: deferring or abating tax on the homestead of a person 65 or older, disabled, or a disabled veteran; deferral on an appreciating homestead | 2026-09-01; 89th Leg. R.S. (2025) | 16,973 |
| `texas-constitution-article-8-taxation-and-revenue` (new) | `tex-const-art8` | Tex. Const. art. VIII: homestead exemptions and the 65+/disabled tax limitation (s 1-b), the income tax prohibition (s 24-a), capital gains tax prohibition (s 24-b) | 2026-07-31; amendments credited to 2025 | 93,589 |

**How the pieces connect, as read in the deposited texts:**

- **Constitution to statute.** Art. VIII s 1-b authorises the homestead exemptions and the freeze on school taxes for the elderly and disabled; Tax Code ss 11.13 and 11.26 carry them out. Art. VIII s 24-a is why there is no state income tax to source.
- **Federal disability definition.** For the homestead exemptions, "disabled" means under a disability for purposes of payment of disability insurance benefits under Federal Old-Age, Survivors, and Disability Insurance (Tax Code s 11.13(m)(1)). That is Social Security Title II, deposited in `subjects/us/social-security-act` (`usc42-ch7-schII.txt`).
- **UI and Social Security.** A permanently disabled person receiving disability insurance benefits under 42 U.S.C. 423 can be treated as able and available for part-time work (Lab. Code s 207.0211). Pensions reduce benefits, but a payment under the federal Social Security Act may not reduce the weekly benefit amount (s 207.050(b)); s 207.050(d) says the section is enacted because FUTA, 26 U.S.C. 3304(a)(15), requires it. Ch. 201 keys its "employer" definitions to FUTA (26 U.S.C. 3301 ff., 3306). IRC s 85 (UI benefits are federally taxable) is deposited in `subjects/us/internal-revenue-code-of-1986` (`usc26-ch1-schB-ptI-III.txt`); FUTA (IRC ch. 23) is indexed there but its text is not deposited.
- **TANF.** Ch. 31 refers to employment programmes "established under Part A, Subchapter IV, Social Security Act (42 U.S.C. Section 601 et seq.)" and to the Title IV-D (child support) agency. Title IV-A is indexed in `subjects/us/social-security-act` but its text is not deposited there, so the federal side of this link is not yet in commons.
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`); Texas's own SNAP chapter (Hum. Res. Code ch. 33) is indexed only.
- **State SSI supplement.** None sourced. Texas has no statutory optional state supplementary payment for SSI recipients in general -- unverified (general knowledge).

**Terms.** Read 2026-10-19 (UTC) at https://capitol.texas.gov/resources/policies.aspx: a disclaimer only -- "The information obtained from this site is not intended to replace official versions of that information and is subject to revision." No copyright notice, no licence, no reuse restriction. robots.txt: statutes.capitol.texas.gov serves its app shell at /robots.txt (no robots file); tcss.legis.texas.gov returns 404 (none); capitol.texas.gov disallows only admin and search paths. Verdict: **clean**. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020; *Veeck v. SBCCI*, 5th Cir. 2002). The enactment and amendment credits kept in the texts are the Council's own; there are no vendor annotations.

**Gaps.**
- Statutes changed by the 89th Legislature's 2025 called sessions may not all be reflected in the LA files (dated 2026-05-14).
- The TANF grant amounts and the UI maximum weekly benefit are set by rule or administrative figure, not in the deposited chapters; Texas Administrative Code (titles 1 and 40) is not sourced.
- Labor Code ch. 208 (claims and appeals), Tax Code ch. 23 (the 10% homestead appraisal cap, s 23.23) and Hum. Res. Code ch. 33 (SNAP) are not deposited.
