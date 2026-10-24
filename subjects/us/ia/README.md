# iowa/

Iowa (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Iowa Legislature - Iowa Code (Legislative Services Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Clean, scriptable HTML over HTTPS, no blocking of any kind: no CAPTCHA, no bot challenge, no 403 and no rate limiting. Fetched with an honest user agent (canon-index-builder/1.0, identifying an indexing client and a contact address). The chapter section-listing pages used for verification have the form https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter=<chapter>&year=2026 and each one prints the Code year, the Title, the Chapter heading and every section number and catchline. Currency: the Iowa Code landing page shows 'Iowa Code - 2026, effective 1/1/2026 - 12/31/2026' as the current edition (a dropdown offers editions back to 2004), and every chapter page fetched carried the banner 'Iowa Code - 2026'. About 14 requests in total, issued sequentially and spaced 2 seconds apart.

## Topics with no legislation here

- **Passenger compensation**: Federal, and preempted. Air passenger rights come from US DOT rules (14 CFR Parts 250, 259, 260) and the Airline Deregulation Act (49 U.S.C. 41713) preempts state regulation of airline prices, routes and services. Iowa has no passenger-compensation statute.
- **Customs/duties**: Federal, and constitutionally exclusive. U.S. Const. art. I, sec. 10, cl. 2 bars a state from laying imposts or duties on imports or exports; customs law is 19 U.S.C., administered by CBP.
- **Work permits/immigration**: Federal. Work authorisation and immigration status are governed by the Immigration and Nationality Act, 8 U.S.C., and 8 C.F.R. Iowa's only related provisions are eligibility screens for state benefits (for example 239B.2B 'Eligibility of noncitizens.', seen in the ch. 239B listing), not any grant of work authorisation.

## Statute text deposited 2026-10-20: personal income tax and benefits

Five chapters of the Iowa Code were deposited as unofficial plain text, each one whole, for a sample on personal income tax and state benefits. The source is the Legislative Services Agency's **Iowa Code 2026** (official PDFs stamped 9 December 2025; laws through the 2025 session), the current edition when fetched on 2026-10-19 (UTC). The text was converted from the chapter XML the Agency publishes beside each PDF. **Acts of the 2026 session are not incorporated.**

| Subject | Chapter | What it gives a person | Characters |
| --- | --- | --- | --- |
| `iowa-code-chapter-422-individual-income-corporate-and-franchise` (existing; text added) | Iowa Code ch. 422 | State income tax owed: a flat 3.8% rate (422.5(1)(a)), net income from federal taxable income (422.7), the Social Security subtraction (422.7(8)), the earned income tax credit (422.12B), the child and dependent care credit (422.12C), withholding (422.16) | 430,645 |
| `iowa-code-chapter-96-employment-security-unemployment-compensation` (new) | Iowa Code ch. 96 | Unemployment benefits: the weekly benefit amount table by number of dependents, and duration (96.3); eligibility (96.4); disqualification (96.5); claims and appeals (96.6) | 252,751 |
| `iowa-code-chapter-239b-family-investment-program` (existing; text added) | Iowa Code ch. 239B | FIP, Iowa's TANF cash assistance: eligibility (239B.2), cash assistance (239B.3), disregards (239B.7), family investment agreements and the limited benefit plan (239B.8, 239B.9) | 55,653 |
| `iowa-code-chapter-249-state-supplementary-assistance` (new) | Iowa Code ch. 249 | State supplementary assistance for people on SSI: eligibility (249.3), amount of grant (249.4) | 18,761 |
| `iowa-code-chapter-425-homestead-tax-credits-exemptions-and-reimbursement` (new) | Iowa Code ch. 425 | The homestead credit; the property tax credit or rent reimbursement for elderly and disabled people, by household income (425.17, 425.23) | 82,506 |

The plan named "Iowa Code 422.5A" as the flat rate. That section is repealed for tax years from 2025. The 3.8% rate is in 422.5(1)(a).

**How the pieces connect, as read in the deposited texts:**

- **Federal income tax.** "Net income" is federal taxable income under IRC s63, with Iowa's adjustments (422.7). For tax years from 2020, "Internal Revenue Code" means the Code "as amended", which is rolling conformity (422.3(5)(b)). The federal text is in `subjects/us/internal-revenue-code-of-1986`.
- **Social Security benefits.** Iowa subtracts "the amount of social security benefits taxable under section 86 of the Internal Revenue Code" (422.7(8)). IRC s86 is deposited in the IRC subject (`usc26-ch1-schB-ptI-III.txt`).
- **EITC.** The Iowa earned income credit is 15% of the federal earned income credit under IRC s32, and it is refundable (422.12B). IRC s32 is deposited in the IRC subject.
- **Unemployment insurance.** "Benefits paid under this chapter are subject to federal and state income tax." A claimant may elect federal withholding and 5% Iowa withholding (96.3(10)). Federal taxation of benefits is IRC s85, deposited in the IRC subject. Because benefits sit in federal taxable income and no 422.7 subtraction for them was found, they are taxed in Iowa too. Chapter 96 also refers to FUTA (26 U.S.C. 3301 and following), which is not deposited.
- **FIP.** The department administers the federal TANF block grant under PRWORA (239B.4), and cooperation with child support follows 42 U.S.C. 608(a)(2) (239B.2(6)). Title IV-A of the Social Security Act is indexed in `subjects/us/social-security-act`, but its text is **not deposited** there.
- **State supplementary assistance.** The department may agree with the federal Secretary for federal administration of the supplement to SSI (249.2). The SSI and state-supplementation text (42 U.S.C. 1381 and following, including 1382e) is deposited in `subjects/us/social-security-act` (`usc42-ch7-schXVI.txt`).
- **Elderly and disabled credit.** Household "income" starts from Iowa net income under 422.7 and adds back items, including payments under the federal Social Security Act (425.17). So the chapter 422 computation and federal benefits both feed this credit.
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`). No Iowa SNAP statute was sourced.

**Terms.** All read 2026-10-19 (UTC):
- https://www.legis.iowa.gov/law/disclaimer says the site holds official PDF editions and unofficial editions in other formats. It restricts reuse only for photographs.
- https://www.legis.iowa.gov/law/officialAndUnofficialEditions says a version is official only if designated under Iowa Code 2B.17. It makes no copyright statement, and Iowa Code ch. 2B contains no copyright provision.
- robots.txt disallows only /chambers/.

Verdict: **clean**. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020). The history lines and footnotes kept in the texts are the Legislative Services Agency's, not a vendor's. Each subject's SOURCE-LICENSE.md has the detail.

**Gaps.**
- The 2026 session Acts are not applied.
- Benefit amounts and payment standards are set by rule or appropriation and are not sourced: FIP payment standards (IAC 441-41), state supplementary assistance amounts, and the Department of Revenue's inflation factors.
- Iowa Administrative Code rules are not sourced.
- Chapter 422's administration provisions for individual returns are in the deposit, but chapter 421 (the Department of Revenue) is not.

## Administrative rules deposited 2026-10-20: benefit amounts

Two new subjects from the Iowa Administrative Code (IAC), taken from the publication of 10/14/2026, the official edition current when fetched. The text was converted from the Legislature's word-processing download. The official edition is the chapter PDF, and its sha256 is recorded in each `.meta.json`.

| Subject | Text | What it sets | Characters |
| --- | --- | --- | --- |
| `iowa-administrative-code-441-chapters-40-41-family-investment-program-need-standards` (new; made under ch. 239B) | IAC 441—40.21 (definitions), 441—41.27 (income), 441—41.28 (need standards), whole rules | FIP: the **Schedule of Needs** by household size. The schedule of basic needs is the payment standard: 1 person $183, 2 $361, 3 $426, 4 $495, 5 $548 ... 10 $865, each additional person $87. Also set: the schedule of living costs (standard of need), 185% of living costs (gross income test), the 20% earned income deduction and 58% work incentive disregard (41.27(2)), and the grant = payment standard minus countable net income (41.27, 41.27(9)) | 68,343 |
| `iowa-administrative-code-441-chapter-52-state-supplementary-assistance-payment` (new; made under ch. 249) | IAC 441—52 (rule 52.1, assistance standards), whole chapter | State supplementary assistance: blind recipient not receiving another type of SSA $22 a month (52.1(4)); Medicare/Medicaid supplement $1 a month (52.1(7)). The other standards are "published on the department's website" and move each January 1 with the SSA COLA | 17,912 |

**Amounts that now come from deposited text.** The FIP payment standard, standard of need and 185% test by household size, the earned income deduction and disregard, and the grant formula are now in commons. With chapter 239B already deposited, an FIP grant can be computed for a family of any size. For state supplementary assistance, only the two fixed amounts above are in commons.

**Terms.** These are the same as for the statutes: https://www.legis.iowa.gov/law/disclaimer restricts reuse only for photographs, and robots.txt disallows only /chambers/. Verdict: **clean**. Every request returned HTTP 200.

**Remaining gaps.**
- The state supplementary assistance standards the department publishes on its website (dependent relative, residential care per diem, family-life home and personal allowances) are not sourced. They are not rule text.
- The unemployment insurance maximum weekly benefit for the current benefit year is computed by Iowa Workforce Development from the statewide average weekly wage (96.3). No official notice was located. The host workforce.iowa.gov allows crawling, but no page was guessed at.
- IAC 871 (Workforce Development) UI rules and the Department of Revenue's inflation factors are not sourced.

## Encodings, 24 October 2026: tax and benefits

| Encoding | Seat | What it answers | Assertions |
| --- | --- | --- | --- |
| [`iowa-code-chapter-422-individual-income-corporate-and-franchise/encodings/baseline-2026-10/`](iowa-code-chapter-422-individual-income-corporate-and-franchise/encodings/baseline-2026-10/) | the individual taxpayer | residence (422.4(14)); net income from federal taxable income with the main 422.7 adjustments (Social Security, pensions at 55, military pay); the 3.8% flat tax and the $9,000 / $13,500 and age-65 $24,000 / $32,000 limits with the 4.3% alternate (422.5); the personal exemption and tuition credits (422.12); the 15% refundable EITC (422.12B); the child care and early childhood credits (422.12C); who must file (422.13) and by when, with payment (422.21(1), 422.24(1)) | 46 / 46 |

Both are baselines: a seat-neutral core in the Code's own terms with regulative rules for the duties, and a seat layer with `@export` questions. Federal figures (federal taxable income, IRC s86, s32, s21) are inputs, answered by `subjects/us/internal-revenue-code-of-1986/`. Each encoding's NOTES.md lists its findings and what is `not covered`.
