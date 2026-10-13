# Scenario: cradle to grave — Jake Harding (WA Sim Two, the alternative life)

Jun Hao's life, moved to Perth. Chloe's younger brother, born in 2006, dead at seventy-two in 2079. A shoplifting matter at fifteen that never reaches a court because the police refer it to a juvenile justice team; a vape at sixteen that is the shop's offence and not his; school left at sixteen for TAFE; no national service; a failure to enrol and a twenty-dollar penalty; seven years on an e-bike for a delivery platform as an employee-like contractor with no workers' compensation, so that a car door becomes a claim against the driver's insurer; a payday loan at the capped charges; a daughter born before the wedding to parents the law treats exactly as it treats married ones; a security job on an award with underpaid overtime recovered in the Magistrates Court; a loan shark at the door and a misconduct restraining order; a debt agreement under Part IX of the Bankruptcy Act; a child support assessment by the formula; a divorce after twelve months apart; an apartment off the plan with the grant and a low-deposit loan; the casino, and no family exclusion order to be had in Western Australia, so BetStop instead; a fall on a stairwell assessed one point below the common-law threshold; redundancy by the statutory scale and JobSeeker; a cleaner on an award; a stroke at fifty-six, the Disability Support Pension on a borderline rating, the NDIS; the Age Pension at sixty-seven, this time yes; and an estate small enough for the Public Trustee.

Nothing in it is villainous. He is never charged, never convicted, never imprisoned. Where Jun Hao's life ran through the Youth Court, probation and a spent record, Jake's runs through diversion, and the question "must I disclose it?" has the answer "there is nothing to disclose".

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — twenty beats, two a chapter, with ages.
- [`GAPS.md`](GAPS.md) — the encoding order this life sets for a library that holds the sources and no rows, and the seams with Chloe's and Daniel's files.
- [`facts.json`](facts.json) — the cast and 71 dated events with their law and status, ages at every event, the twenty beats flagged.
- [`check-status.py`](check-status.py) — re-derives the status column from the tree.

## Design rules

As for Chloe's scenario. Two particulars.

1. **Nature permits the unlawful.** Jake does five unlawful things, all small: the shop, the road, the passenger card, the speeding, the non-voting. Each is answered with a process and never a cell: a juvenile justice team, an infringement notice, a penalty notice, demerit points. A replay that blocks any of them is wrong; one that fails to raise the consequence is wrong too.
2. **Shared facts.** His parents, his sister and their deaths are Chloe's facts: the will to the mother in 2052, the intestacy in 2060 with equal shares. From 2034 he is the night officer in the tower where Daniel Rossi's company is a tenant, and his fall in 2053 is in that building. Chloe's file carries one reach into his life, her search for a family exclusion order in 2046; `GAPS.md` section F records the seams.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Jake Harding** | 30 Aug 2006, KEMH | the main character | citizen by birth; dies 18 Apr 2079 without a will |
| Tahlia Brooks | 11 Mar 2007 | partner from 2032, wife 2033 to 2039 | early childhood educator |
| Ruby Harding | 22 Jan 2033 | their daughter | born before the marriage; Australian law draws no distinction |
| Chloe Harding | 14 Mar 2003 | his sister | her own scenario |
| Graham and Sue Harding | 1970, 1972 | their parents | as in Chloe's facts |
| a delivery platform | — | 2027 to 2034 | he is an independent contractor and, from 2024, an employee-like worker |
| Sentinel Security Services Pty Ltd | — | his employer 2034 to 2055 | licensed security company; posts him to Jarrah's tower |
| Swan Clean Pty Ltd | — | his employer 2056 to 2063 | a cleaning contractor on the Cleaning Services Award |

---

## Chapter 0 — Born (2006)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2006-08-30 | birth at KEMH | Citizen by birth? | Australian Citizenship Act 2007 (Cth) s 12 | `NONE` |
| 2006-09-14 | registered on day fifteen | — | BDMR Act 1998 (WA) ss 12-13 | `NONE` |
| 2006-10 | the Maternity Payment of 2006; FTB for a second child | What did a second child bring? | Family Assistance Act 1999 (Cth) Part 3 | `NONE` (replayed; the 2006 rates are nowhere) |
| 2006-08-30 | Medicare | — | Health Insurance Act 1973 (Cth) s 3 | `NONE` |

## Chapter 1 — Primary school and the letter (2013–2018)

Year 1 in 2013. In Year 4 he is absent thirty-one days and the school's attendance officer writes to his parents, whose duty it is; the Department has an attendance panel and a responsible parenting agreement before it has a prosecution. A passport for a school trip. Year 7 at the local high school.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2013-02 | Year 1 | — | School Education Act 1999 (WA) ss 6, 9 | `NONE` |
| 2016-05-20 | 31 days absent; the letter | Whose duty; what before a prosecution? | School Education Act ss 23, 38, 39-40 | `NONE` |
| 2016-06 | first passport | — | Australian Passports Act 2005 (Cth) s 11 | `NONE` |
| 2018-10 | Year 7; NAPLAN | — | Department policy | `ADMIN-POLICY` |

## Chapter 2 — The shopping centre and the juvenile justice team (2021–2022)

A tax file number at fifteen. In November 2021, with two friends, a phone case and earbuds worth eighty-nine dollars, and a security officer at the door: stealing under the Criminal Code. He is fifteen; the police may caution, or refer, or charge, and they refer. A juvenile justice team in February: an apology, restitution, community work, and when the action plan is complete, no charge and no conviction. He leaves school at the end of the year he turns sixteen, for a pre-apprenticeship, which the participation requirement allows.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2021-08-30 | 15: TFN | — | Taxation Administration Act 1953 (Cth) Part VA | `NONE` |
| 2021-11-20 | takes $89 of goods | What offence? | Criminal Code (WA) ss 371, 378 (stealing) | `NONE` |
| 2021-11-20 | the police refer him | What may police do instead of charging; which court if they charge? | Young Offenders Act 1994 (WA) ss 7, 22-30; Children's Court of Western Australia Act 1988 s 19 | `NONE` |
| 2022-02-14 | the juvenile justice team | What does a completed action plan do? | Young Offenders Act ss 29-30 | `NONE` — no charge, no conviction |
| 2022-11 | leaves school at 16 for TAFE | May he? | School Education Act ss 6, 11B; Vocational Education and Training Act 1996 (WA) Part 7 | `NONE` |

## Chapter 3 — TAFE, a vape, and no national service (2023–2026)

A certificate course. A vape outside the campus: the seller offended, not the sixteen-year-old. A provisional licence at seventeen. At eighteen he does not enrol, and after the 2025 federal election a penalty notice arrives for the enrolment he never made. Bali at nineteen. Five years after the shopping centre, nothing becomes spent, because nothing was ever recorded.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2023-02 | TAFE | — | VET Act 1996 (WA) | `NONE` |
| 2023-06-02 | a vape | Is possession by a minor an offence; is the sale? | Tobacco and Other Products Control Act 2006 (WA) ss 6, 106; Therapeutic Goods Act 1989 (Cth) ss 41QD-41QE | `NONE` — the seller's offence |
| 2023-08-30 | 17: provisional licence | — | Road Traffic (Authorisation to Drive) Act 2008 (WA) s 8 | `NONE` |
| 2024-08-30 | 18: does not enrol | Must he? | Commonwealth Electoral Act 1918 (Cth) s 101 | `NONE` |
| 2025-05-03 | the federal election; a penalty notice | What happens to a person who neither enrols nor votes? | Commonwealth Electoral Act ss 101, 245 | `NONE` — $20 |
| 2026-05 | Bali | — | Australian Passports Act s 8 | `NONE` |
| 2026-11-20 | five years on: nothing to spend | Does a diversion leave a record? | Spent Convictions Act 1988 (WA) s 3, Part 2; Young Offenders Act s 30 | `NONE` — nothing was recorded |

## Chapter 4 — The platform years (2027–2032)

An e-bike, a delivery bag, an ABN. The Fair Work Act since 2024 calls him an employee-like worker and lets the Commission set minimum standards; the platform pays no superannuation because the contract is not wholly for his labour, unless an order says otherwise. On the footpath at ten kilometres an hour he is lawful; on a sixty road he is not, and an infringement notice follows. A sole trader's tax return, under the GST threshold. A car door in 2029: no workers' compensation for a contractor, so a claim against the driver's compulsory third party insurer under the Civil Liability Act's thresholds. He skips the 2029 State election and is fined. Three cartons from Bali and a false passenger card. Two credit cards under responsible lending, and a payday loan at the capped charges.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2027-03-06 | rides for a platform; an ABN | Employee, contractor, or employee-like? | Fair Work Act 2009 (Cth) s 15AA, Part 3A-2; ABN Act 1999 (Cth) s 8 | `NONE` |
| 2027-03-31 | no super from the platform | Is super payable to a contractor? | Superannuation Guarantee (Administration) Act 1992 (Cth) s 12(3); Fair Work Act Part 3A-2 Div 3 | `NONE` |
| 2027-07-14 | the footpath, then a 60 road | Where may an eRideable go? | Road Traffic Act 1974 (WA) Part 5; the Road Traffic Code 2000; Fines, Penalties and Infringement Notices Enforcement Act 1994 (WA) Part 3 | `NONE`; `REGS` |
| 2028-10 | a sole trader's return, $31,000 | Business income; GST; instalments | ITAA 1997 (Cth) s 6-5, Div 8; GST Act 1999 (Cth) s 23-5; Taxation Administration Act Sch 1 Part 2-10 | `NONE` |
| 2029-04-12 | a car door; a fractured wrist | Who pays for a contractor hurt by a car? | Workers' Compensation and Injury Management Act 2023 (WA) s 5; Motor Vehicle (Third Party Insurance) Act 1943 (WA) s 4; Civil Liability Act 2002 (WA) Part 2; Health Insurance Act | `NONE` |
| 2029-03-08 | the State election, unvoted | — | Electoral Act 1907 (WA) s 156 | `NONE` |
| 2031-01-15 | three cartons from Bali | The concession; the offence | Customs Act 1901 (Cth) ss 68, 234; the By-laws | `NONE`; `REGS` |
| 2031-06-30 | census night | — | Census and Statistics Act 1905 (Cth) s 14 | `NONE` |
| 2031-03 | two credit cards | What must the issuer assess? | National Consumer Credit Protection Act 2009 (Cth) ss 128-133, 133BE; Privacy Act 1988 (Cth) Part IIIA | `NONE` |
| 2032-08-20 | a $2,000 payday loan | The most a lender may charge | NCCP Act ss 31A-31B | `NONE` — 20% establishment, 4% a month |

## Chapter 5 — Tahlia, Ruby, and a marriage that changes nothing (2032–2033)

Ruby is born in January 2033 to parents who are not married; both sign the registration; the law has no word for illegitimacy and has not had one for fifty years. Tahlia's Paid Parental Leave has no marriage condition, and neither do Jake's reserved weeks as a self-employed partner, nor the Newborn payments, nor Family Tax Benefit. They marry in September anyway, by a civil celebrant, and nothing changes for Ruby. A unit in Gosnells, the bond lodged, a condition report at the start, rent that may rise once a year.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2033-01-22 | Ruby born; parents unmarried | Citizen; both parents registered; legitimate? | Australian Citizenship Act s 12; BDMR Act ss 13, 18; no status of illegitimacy | `NONE`; `CASE` |
| 2033-01-22 | Tahlia's PPL | Married or not? | PPL Act 2010 (Cth) Part 2-1 | `NONE` — no condition |
| 2033-01-22 | Jake's reserved weeks | A self-employed father? | PPL Act | `NONE` |
| 2033-02 | Newborn payments; FTB | The same for a child born outside marriage? | Family Assistance Act Part 3, Sch 1 | `NONE` — the same |
| 2033-08-10 | Notice of Intended Marriage | — | Marriage Act 1961 (Cth) s 42 | `NONE` |
| 2033-09-16 | married; nothing changes for Ruby | What does the marriage do for a child born before it? | Marriage Act ss 39, 45 | `NONE`; nothing `CASE` |
| 2033-11-01 | a unit in Gosnells, $420 a week | The bond; the condition report; rent increases | Residential Tenancies Act 1987 (WA) ss 27C, 29, 30 | `NONE` |

## Chapter 6 — The security job, the claim, and the debts (2034–2037)

A security officer's licence and a job at Sentinel on the Security Services Industry Award, posted to the tower where Jarrah Legal Technologies is a tenant. Thirteen months of overtime at ordinary time, recovered through the Fair Work Ombudsman and a small claim in the Magistrates Court. A friend's debt to an unlicensed lender brought to his door as paint and glue; the lending unlicensed, the damage an offence, a misconduct restraining order for the household. Collectors, the ACCC's guideline, a default on the credit file. A debt agreement under Part IX instead of bankruptcy: proposed by him, gated by the Official Receiver, accepted by a majority of creditors in value. Five years at $690 a month.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2034-02-01 | licence; Sentinel; the award | May he work unlicensed; what does the award give a twelve-hour shift? | Security and Related Activities (Control) Act 1996 (WA) ss 8, 15-16; Fair Work Act Part 2-3 and the Security Services Industry Award 2020; SG (Administration) Act s 16 | `NONE` |
| 2035-03-31 | overtime at ordinary time | What is owed; how far back? | Fair Work Act ss 45, 544 | `NONE` — $4,100; six years |
| 2036-03-10 | the Ombudsman, then a small claim | Where; what may be ordered? | Fair Work Act ss 545, 548; Magistrates Court Act 2004 (WA) | `NONE` |
| 2036-08-22 | a friend's loan shark | Enforceable; what offences; what order? | NCCP Act s 29; Criminal Code (WA) ss 338B, 444; Restraining Orders Act 1997 (WA) Part 3 | `NONE` |
| 2037-02-06 | $41,000; collectors | What may a collector do? | Competition and Consumer Act 2010 (Cth) Sch 2 s 50 and the ACCC/ASIC guideline; Privacy Act Part IIIA | `NONE` |
| 2037-04-20 | a debt agreement | Who proposes; who decides; what does it do? | Bankruptcy Act 1966 (Cth) Part IX ss 185C, 185EC, 185H | `NONE` — the creditors decide, by majority in value |
| 2037-06 | five years at $690 | — | Bankruptcy Act Part IX Div 3 | `NONE` |

## Chapter 7 — Separation, divorce, and an apartment (2038–2045)

Separation in June 2038 and a parenting plan under Part VII of the Family Law Act. A child support assessment by the formula on both incomes and the care percentage, collected by the Registrar from his wages when he falls behind. Divorce in August 2039 after twelve months apart, the only ground, with almost nothing to settle. An apartment off the plan in 2042: no age rule for a single buyer beyond eighteen, the first home owner grant for a new home, the first home owner rate of duty, a low-deposit loan from Keystart. The debt agreement completes and stays on the Index and the credit file for five years. Settlement in 2045 and the strata company.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2038-06-01 | separation; a parenting plan | Parental responsibility; where Ruby lives; what a plan is worth | Family Law Act 1975 (Cth) Part VII, s 63C | `NONE` |
| 2038-06-15 | a child support assessment | How much, on what? | Child Support (Assessment) Act 1989 (Cth) Part 5 ss 35-55 | `NONE` — the formula |
| 2039-01-15 | three missed payments | How is it enforced? | Child Support (Registration and Collection) Act 1988 (Cth) Parts IV-V | `NONE` |
| 2039-08-20 | divorce after twelve months | The ground; the children; the property | Family Law Act ss 48, 55A, 79 | `NONE` |
| 2042-02-18 | an apartment off the plan, $390,000 | The grant; the duty; the loan | First Home Owner Grant Act 2000 (WA) ss 6-13; Duties Act 2008 (WA); Keystart; Housing Act 1980 (WA) | `NONE`; `ADMIN-POLICY` — $10,000; duty nil |
| 2042-05-31 | the agreement completes | What stays on the Index and the file? | Bankruptcy Act s 185N; Privacy Act Part IIIA | `NONE` — five years |
| 2045-03-20 | settlement; the strata company | — | Transfer of Land Act 1893 (WA) s 68; Strata Titles Act 1985 (WA) Part 7 | `NONE` |

## Chapter 8 — BetStop, the stairwell, and the redundancy (2045–2060)

Lotto, the casino, betting apps. In 2046 Chloe looks for a family exclusion order and finds that Western Australia has none; the casino and the Commission may exclude, a family may not apply. He registers on BetStop, the national self-exclusion register, and self-excludes from Crown. A job form asks about convictions and the police certificate is blank. Speeding and demerit points. His father dies and leaves everything to his mother. In 2053 he falls on a wet stairwell on patrol in Jarrah's tower: income compensation, medical expenses, and a whole-person impairment assessed at fourteen per cent, one point under the threshold for a common-law claim. Redundant at forty-nine when the contract is lost: notice of five weeks, redundancy pay of twelve by the scale, JobSeeker with mutual obligations. A cleaner on the Cleaning Services Award, where Singapore had a policy and Australia has a law. His mother dies intestate; he and Chloe take equally; a hundred thousand into super.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2045-09 | Lotto, the casino, the apps | Which is lawful; any entry levy; what may an app offer? | Casino Control Act 1984 (WA) ss 21-22; Betting Control Act 1954 (WA) Part 2; Interactive Gambling Act 2001 (Cth) ss 15, 15AA | `NONE` — no entry levy in WA |
| 2046-05-08 | no family exclusion order in WA; BetStop | May a family member have him excluded? What can he do? | Casino Control Act s 25; Interactive Gambling Act Part 7A; Crown's self-exclusion program | `NONE`; `ADMIN-POLICY` |
| 2047-03-04 | a job form; a blank certificate | Must he disclose 2021? | Spent Convictions Act Part 3; Young Offenders Act s 30 | `NONE` — nothing to disclose |
| 2049-07-19 | speeding | — | Road Traffic Act s 59; Road Traffic (Authorisation to Drive) Act Part 4 | `NONE` |
| 2052-08-19 | his father dies | Does he take anything? | Wills Act 1970 (WA) s 8; Administration Act 1903 (WA) s 25 | `NONE` — no |
| 2053-10-05 | the stairwell; 14% whole-person impairment | What is paid; who assesses; what does 15% unlock? | Workers' Compensation and Injury Management Act 2023 (WA) Parts 2, 3, 7; Work Health and Safety Act 2020 (WA) ss 19-20 | `NONE` — the percentage is an approved specialist's |
| 2055-11-30 | redundant at 49 | Notice; redundancy pay for 21 years; JobSeeker | Fair Work Act ss 117, 119, 389; Social Security Act 1991 (Cth) Part 2.12 | `NONE` — 5 weeks; 12 weeks |
| 2056-02-01 | a cleaner on the award | The minimum rate, and where it is written | Fair Work Act Part 2-3; the Cleaning Services Award 2020; the annual wage review | `NONE`; `REGS` |
| 2060-01-27 | his mother dies intestate | — | Administration Act s 14 | `NONE` — half each |
| 2060-09 | $100,000 into super | Within the cap? | ITAA 1997 s 292-85 | `NONE` |

## Chapter 9 — The stroke, the pension, and the end (2063–2079)

A stroke at fifty-six, three weeks in a public hospital, nothing to pay. The Disability Support Pension on twenty impairment points, assessed at exactly twenty on a borderline table, so that the rule is exact and the rating is a clinical judgement at the margin. NDIS access under sixty-five; Ruby on Carer Allowance; an enduring power of attorney and enduring guardianship to her. Super accessible at sixty on permanent incapacity. At sixty-seven the Age Pension, which his father and his sister did not get, and the pensioner rebate on council rates. An advance health directive. He dies at seventy-two, on the Organ Donor Register since 2047; his daughter takes all by intestacy, the Public Trustee administers the small estate, and his super passes to her taxed as a non-dependant.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2063-03-14 | a stroke; a public hospital | What is covered? | Health Insurance Act Part II; Health Services Act 2016 (WA) Part 4 | `NONE` — nothing to pay |
| 2063-04-28 | Disability Support Pension, 20 points exactly | The test; who decides a borderline case? | Social Security Act s 94 and the Impairment Tables | `NONE` — the rating is a medical judgement |
| 2063-05-15 | NDIS access; Carer Allowance; EPA and guardianship to Ruby | Eligible under 65? The carer? Who decides for him? | NDIS Act 2013 (Cth) ss 21-25; Social Security Act Part 2.19; Guardianship and Administration Act 1990 (WA) Parts 9, 9A | `NONE` |
| 2065-05 | a review | — | Social Security Act s 94 | `NONE` |
| 2066-08-30 | turns 60 | Super on permanent incapacity | SIS Act and Regulations | `NONE` |
| 2073-08-30 | turns 67: the Age Pension; the rates rebate | Which pension; the rebate? | Social Security Act ss 43, 1064; Rates and Charges (Rebates and Deferments) Act 1992 (WA) ss 24-25 | `NONE` — yes |
| 2075-04 | advance health directive | — | Guardianship and Administration Act Part 9B | `NONE` |
| 2079-04-18 | dies at 72; kidneys donated | Consent presumed or given? | Human Tissue and Transplant Act 1982 (WA) s 22; BDMR Act Part 6 | `NONE` — given, on the Register |
| 2079-05-02 | no will; a small estate; the super | Who takes; a grant; the Public Trustee; the super to an adult child | Administration Act ss 14, 25; Public Trustee Act 1941 (WA) s 10; ITAA 1997 Div 302 | `NONE`; no inheritance tax `CASE` |

---

## What the scenario touches

Sixty-one subjects: twenty-seven Commonwealth and thirty-four Western Australian, none with a row on 13 October 2026. Against Jun Hao's life, the big substitutions are structural: diversion for the Youth Court, a CTP claim for work injury, the formula for a maintenance order, twelve months for three years, a debt agreement voted by creditors for a scheme determined by an official, BetStop for a family exclusion order that does not exist, the Disability Support Pension and the NDIS for CareShield, and the Age Pension for Silver Support. The library's first demands from this life are the Fair Work Act (nine events), the Social Security Act (six), the Bankruptcy Act (four), the Young Offenders Act, the two Child Support Acts, the National Consumer Credit Protection Act and the Workers' Compensation and Injury Management Act. [`GAPS.md`](GAPS.md) ranks them.

## Sample prompts for the chat demo

1. "I got caught taking stuff from a shop. I'm fifteen. Will I go to court?" — Young Offenders Act ss 22-30: a caution or a juvenile justice team first.
2. "Is it illegal for me to have a vape at sixteen?" — the seller's offence, not his.
3. "I never enrolled. Is that a crime?" — Commonwealth Electoral Act s 101: a penalty notice.
4. "Can I ride the e-bike on the footpath?" — yes, at ten kilometres an hour; not on a sixty road.
5. "A car door broke my wrist on a delivery. Is it workers' comp?" — no, a contractor; a CTP claim against the driver's insurer.
6. "The payday lender wants $400 a month on $2,000." — NCCP Act s 31A: the caps.
7. "Ruby was born before we married. Does it matter?" — not to any Australian law in this life.
8. "Can the landlord put the rent up again?" — Residential Tenancies Act s 30: once in twelve months.
9. "They've paid my overtime at ordinary time for a year." — Fair Work Act ss 45, 548: the Ombudsman, then a small claim.
10. "Someone glued our lock over a loan that isn't mine." — Restraining Orders Act Part 3; Criminal Code s 444.
11. "A creditor says I'll be bankrupt." — Bankruptcy Act Part IX: a debt agreement, if the creditors vote for it.
12. "How much child support will I pay?" — Child Support (Assessment) Act Part 5: the formula.
13. "My sister wants me banned from the casino." — Casino Control Act s 25: she cannot apply; he can self-exclude, and BetStop covers the apps.
14. "Does the job form need to know about 2021?" — nothing was recorded.
15. "Dad never got the pension. Will I?" — Social Security Act ss 43, 1064: yes, on his income and assets.
