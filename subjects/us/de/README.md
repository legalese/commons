# delaware/

Delaware (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the The Delaware Code Online (Delaware General Assembly, Division of Research); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTPS GETs with an honest UA, about 20 requests spaced ~1.8 s apart. No block, challenge or rate limit; no robots obstruction encountered. Each title and chapter page offers an 'Authenticated PDF', which is the official electronic record under Delaware's Uniform Electronic Legal Material Act (1 Del. C. ch. 4, fetched and confirmed). The site publishes no explicit 'current through' banner; currency is shown per section by the session-law credits (e.g. '84 Del. Laws, c. 365').

## Topics with no legislation here

- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). The Title 26 railway and public-conveyance chapters (3, 5, 7) are all marked repealed on the register.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Delaware's Title 19 ch. 5 (Child Labor) covers minors' work permits, which is a different subject.

## Statute text deposited 2026-10-20: personal income tax and benefits

Four Delaware Code chapters (one in part) were deposited as unofficial plain text, for a sample on personal income tax and state benefits. The source is the Delaware Code Online (Division of Legislative Services). The site's notice says the text "includes all acts enacted as of September 10, 2026, up to and including 85 Del. Laws, c. 518." It was fetched 2026-10-19 (UTC). Each file joins the site's subchapter pages in order.

| Subject | Provisions | What it gives a person | Characters |
| --- | --- | --- | --- |
| `delaware-code-title-30-state-taxes-chapter-11-personal-income` (existing; text added) | 30 Del. C. ch. 11, whole | State income tax owed: rate schedules to 6.6% (1102), taxable income from federal AGI (1105), additions and subtractions including the pension and Social Security exclusions (1106), the earned income tax credit (1117), withholding (subchapter VII) | 139,256 |
| `delaware-code-title-19-labor-chapter-33-unemployment-compensation` (new) | 19 Del. C. ch. 33, whole | Unemployment benefits: weekly benefit amount and total benefits (3313), disqualification (3314), eligibility (3315); employer assessments, with the experience-rating tables | 476,892 |
| `delaware-code-title-31-welfare-chapter-5-state-public` (existing; text added) | 31 Del. C. ch. 5, whole | Public assistance: the categories of TANF, General Assistance for unemployable needy persons, Medicaid and child care (505); eligibility and amount (503); TANF eligibility (524) | 90,149 |
| `delaware-code-title-14-education-chapter-19-local-school-taxes` (new) | 14 Del. C. ch. 19, subch. I only | The senior school property tax credit for owner-occupiers aged 65 or more, with domicile conditions (1917(c)) | 76,181 |

The plan's "Rates; EITC" item (30 Del. C. 1102, 1117) is inside chapter 11 and is covered by that file. The Code prints two versions of 14 Del. C. 1917, one "[Effective until Aug. 12, 2028]" and one "[Effective Aug. 12, 2028]". Both are kept.

**How the pieces connect, as read in the deposited texts:**

- **Federal income tax.** Terms in chapter 11 have their federal meaning. References are to the Internal Revenue Code of 1986 "as the same may have been or shall become effective", which is rolling conformity (1101). A resident's taxable income is federal adjusted gross income with the modifications, deductions and exemptions of subchapter II (1105). The federal text is in `subjects/us/internal-revenue-code-of-1986`.
- **Social Security and pensions.** Delaware subtracts "Social Security benefits paid by the United States" and Railroad Retirement payments, to the extent they are in federal AGI (1106(b)(4)). It also excludes pensions: up to $2,000 under age 60, and up to $12,500 at 60 or older, including eligible retirement income (1106). Federal taxation of benefits is IRC s86, deposited in the IRC subject (`usc26-ch1-schB-ptI-III.txt`).
- **EITC.** From tax year 2022 the credit is either 20% of the federal EITC under IRC s32, not refundable, or 4.5% of it, refundable (1117(a)(2)). IRC s32 is deposited in the IRC subject.
- **Unemployment insurance.** Chapter 33 ties coverage and the taxable wage base to the Federal Unemployment Tax Act, 26 U.S.C. 3301 and following (3302). FUTA is not deposited. Federal tax on benefits is IRC s85, deposited in the IRC subject. Delaware's own treatment of benefits is unverified (general knowledge): they enter through federal AGI, and no chapter 11 subtraction for them was found.
- **Public assistance.** TANF eligibility and amounts are set by Department regulation (503(d), 505(1)). Medicaid follows SSA Titles IV-A, IV-E, XVI and XIX (503(b)). Title IV-A of the Social Security Act is indexed in `subjects/us/social-security-act`, but its text is **not deposited** there. Title XVI (SSI) is deposited (`usc42-ch7-schXVI.txt`). No Delaware state supplement to SSI was sourced. Whether Delaware pays one, and under what authority, is unverified.
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`).

**Terms.** Read 2026-10-19 (UTC). The home-page notice says the Code "is prepared by the Delaware Code Revisors and the editorial staff of LexisNexis in cooperation with the Division of Legislative Services ... and is considered an official version". The disclaimer covers warranty and liability only. The site has no terms-of-use or copyright page. robots.txt answers 404. The site is a State host, not vendor-hosted, and the pages carry no annotations, so none are reproduced. Verdict: **clean**. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020). Each subject's SOURCE-LICENSE.md has the detail.

**Gaps.**
- TANF, GA and child-care amounts are in Department of Health and Social Services regulations (the Delaware Social Services Manual), which were not sourced.
- The Division of Revenue's tax tables and regulations were not sourced.
- 14 Del. C. ch. 19, subchapter II (mobile homes) was left out.
- Delaware has no state SSP statute in this set.

## Administrative rules deposited 2026-10-20: benefit amounts

| Subject | Text | What it sets | Characters |
| --- | --- | --- | --- |
| `delaware-administrative-code-title-16-dssm-4000-financial-responsibility` (new; made under 31 Del. C. ch. 5) | Delaware Social Services Manual 4000, Financial Responsibility (16 Del. Admin. Code 4000), sections 4000-4011 as published; latest amendment cited 29 DE Reg. 530 (12/01/25) | TANF and General Assistance: budget group, resources, income and disregards (4001-4006); standards of need and payment standard (4007). GA payment standard equals its standard of need, set by Division notice (4007.1). TANF Fill the Gap table (4007.2), by number of people: payment standard 1 $201, 2 $270, **3 $338**, 4 $407, 5 $475, 6 $544, 7 $612, 8 $681, plus $69 for each person above eight; standard of need (75% FPL) and 185% of it. TANF and GA eligibility and grant computation (4008-4010) | 64,936 |

**Amounts that now come from deposited text.** The TANF payment standard, standard of need and 185% gross-income limit by family size, the disregards, and the grant computation. **Caution:** the 4007.2 table is headed "Current for 10/2002 - 9/30/2003". Sections 4007 and 4007.1 point to a Division of Social Services "COLA Administrative Notice" for current standards. That notice is not in the Administrative Code and was not sourced, so it is unverified whether the 4007.2 figures are still the amounts paid. The GA standard of need is set only by that notice, so no GA dollar figure is in commons.

**Terms.** https://regulations.delaware.gov is a State host and a single-page application. Its text was read through the site's own API (`/api/AdminCode/regulation`), the same request the page makes, with no browser automation. The site's About text calls the Administrative Code "the official version of the regulations for the State of Delaware". No copyright notice or terms of use were found. robots.txt answers with the application's HTML shell, so it was treated as absent. Verdict: **clean**.

**Remaining gaps.**
- The Division's current COLA Administrative Notice (TANF and GA standards).
- A Delaware state supplement to SSI, if one exists: not sourced, unverified.
- The UI weekly maximum in 19 Del. C. 3313 is statutory and already deposited. No rule was needed.
- Division of Revenue regulations: not sourced.

## Tax and benefits encodings (2026-10-24)

| Encoding | Seat | What it answers | Assertions |
|---|---|---|---|
| `delaware-code-title-30-state-taxes-chapter-11-personal-income/encodings/baseline-2026-10/` | the resident taxpayer | residency (1103); who must file (1161, $9,378 / $15,449); joint or separate (1162); pension, military pension and Social Security subtractions (1106(b)(2)-(4)); standard deduction (1108); rates (1102(a)(14)); personal credits (1110); the two EITC options (1117); the 30 April due date (1168) | 48 / 48 |
| `delaware-code-title-31-welfare-chapter-5-state-public/encodings/baseline-2026-10/` | the TANF applicant or recipient | the s 503 bars; resources; disregards; the gross and net income tests; the Fill the Gap grant (DSSM 4000, brought in as the instrument setting the Act's numbers); reporting (510); the 30-day appeal (520) | 38 / 38 |

The TANF standards printed in DSSM 4007.2 are dated 10/2002-9/2003; a grant question also takes current standards as inputs. Penalties for late filing are in 30 Del. C. ch. 5, not deposited.
