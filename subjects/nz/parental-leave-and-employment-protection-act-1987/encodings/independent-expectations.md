# Independent expectations: Parental Leave and Employment Protection Act 1987 (NZ)

Written from the source text (`../registers/source-bundle/act_public_1987_129.txt`, version as at 1 July 2026) and `BRIEF.md` only, **before** any `pl-*.l4` module was opened. `pl-tests.l4` and `NOTES.md` were not read.
Each scenario gives the facts, the expected answer, and the provision and words that give it. Phase-2 notes (how each was or was not asserted in `tests-independent.l4`) are at the end.

## Conventions used throughout

- **Paragraph labels** are reconstructed from list position (BRIEF.md).
- **"N weeks after date X"** is X + 7N days (26 weeks = 182 days). **"The period of 26 weeks beginning with the day after X"** runs from X+1 to X+182 inclusive.
- **"Within N days after X"** covers X+1 .. X+N (Legislation Act 2019 s 54: a period "after" a day excludes that day). The Nth day after X is inside.
- **"At least 3 months before D"**: compliant if given on or before the same day-number 3 calendar months earlier (EDD 15 Sep 2026: on or before 15 Jun 2026).
- **"Not less than 21 days' notice" / "at least 14 days before"**: I treat the requirement as met when (event date - notice date) >= 21 (or >= 14). *Ambiguity*: a "clear days" reading (exclude both end days) would need 22 / 15. I prefer the simple difference because the Act's own phrase in s 31(3)/s 33 is "before", and Legislation Act 2019 s 54 does not adopt clear days generally.
- **"Before the earliest of" a date** (s 71I): an act on that date is late.
- **Average of 10 hours a week**: exactly 10.0 meets; 9.99 fails ("at least").
- Rates in dollars; the maximum weekly rate and the minimum wage are inputs (BRIEF). Unless stated, cap = $811.05 (the figure printed in s 71M), minimum wage = $23.95/h (so s 71N(4) minimum = $239.50).

---

## A. Eligibility: ss 2, 2A-2BA, 4-7, 72A

### Who is the primary carer (s 7)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 1 | Biological mother, pregnant. | Primary carer. | s 7(1)(a) "a female (the biological mother) who is pregnant or has given birth". |
| 2 | Biological mother who has given birth. | Primary carer. | s 7(1)(a). |
| 3 | Mother's partner; no succession, no transfer; child 3 months old; partner has taken permanent primary responsibility to exclusion of mother; mother had not applied for PLP. | Primary carer under (b)(iii). | s 7(1)(b)(iii) all three limbs true. |
| 4 | As 3, but child is 13 months old. | Not primary carer under (b)(iii) (child not "under 1 year"). | s 7(1)(b)(iii)(A). |
| 5 | As 3, but mother had already applied for and qualified for PLP when partner took responsibility. | Not primary carer under (b)(iii). | s 7(1)(b)(iii)(C) "had not applied for, or did not qualify to apply for". |
| 6 | As 5 but mother had applied and did *not* qualify. | Primary carer ("or did not qualify"). | s 7(1)(b)(iii)(C), read disjunctively. |
| 7 | Mother's partner to whom mother has transferred part of PLP under s 71E. | Primary carer (for the transferred period). | s 7(1)(b)(ii). |
| 8 | Mother's partner who succeeded under s 72B. | Primary carer. | s 7(1)(b)(i). |
| 9 | Mother's partner, no succession/transfer, has *not* taken permanent primary responsibility to the exclusion of the mother. | Not primary carer. | s 7(1)(b)(iii)(B). |
| 10 | Aunt takes permanent primary responsibility for a 4-year-old. | Primary carer. | s 7(1)(c); Example 1. |
| 11 | Same, child aged exactly 6 years. | Not primary carer ("under the age of 6 years"). | s 7(1)(c). |
| 12 | Same, child aged 5 years 364 days. | Primary carer. | s 7(1)(c). |
| 13 | Temporary foster placement of a 2-year-old. | Not primary carer (not permanent). | s 7(1)(c); Example 3. |
| 14 | Grandmother minds child daily while parents work. | Not primary carer. | s 7(1)(c); Example 4. |
| 15 | Two adoptive parents both meet (c); they nominate A. | A is primary carer; B is not entitled to primary carer leave or PLP. | s 7(2)(a),(b). |
| 16 | Two adoptive parents both meet (c), no nomination yet. | Not determinable (refuse) - the Act says only the nominated person is entitled; without a nomination neither is. Best reading: neither is yet the primary carer. | s 7(2). Ambiguity noted. |

### Multiple children (s 2B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 17 | Twins from one pregnancy. | Treated as one child (one entitlement, not two). | s 2B(2). |
| 18 | Person becomes primary carer of two unrelated adopted children 20 days apart. | Treated as primary carer of only the youngest. | s 2B(3). |
| 19 | Same, 28 days apart (4 weeks). | Within "a 4-week period" - treated as one (youngest). | s 2B(3). |
| 20 | Same, 29 days apart. | Two separate children (s 6 / s 71F then bites on the second). | s 2B(3). |

### 6-month and 12-month employment tests (s 2BA(1)), s 72A

| # | Facts | Expected | Provision |
|---|---|---|---|
| 21 | Employed by same employer 6 months before EDD, average 10.0 h/week. | Meets 6-month test. | s 2BA(1)(a) "at least an average of 10 hours". |
| 22 | Same, average 9.9 h/week. | Fails 6-month test. | s 2BA(1)(a). |
| 23 | Employed 5 months 29 days with that employer at EDD, 40 h/week. | Fails 6-month test (not employed for the whole 6 months). | s 2BA(1)(a) "employed by the same employer ... in the 6 months immediately preceding". |
| 24 | Employed 12 months, average 10 h over 12 months. | Meets 12-month test. | s 2BA(1)(b). |
| 25 | Employed 11 months, 40 h/week. | Meets 6-month, fails 12-month. | s 2BA(1). |
| 26 | Employed 12 months, avg 12 h in months 1-6, 8 h in months 7-12 (12-month avg 10, 6-month avg 8). | Meets 12-month test; fails 6-month. Entitled via the 12-month test (s 8(1)(b) "or"). Durations follow the 12-month test. | s 2BA(1); s 8(1)(b); s 19(a). |
| 27 | Employee on paid annual leave for 3 of the weeks, would normally work 20 h. | Those hours count. | s 72A(1)(a). |
| 28 | Employee on ACC weekly compensation for 2 months. | Hours count as employed. | s 72A(1)(c). |
| 29 | Pregnant employee on primary carer leave before EDD (s 6 not engaged). | Hours count. | s 72A(1)(e). |
| 30 | Employee on unpaid parental leave (for an earlier child) during the window. | Does **not** count under (b) ("other than parental leave"). | s 72A(1)(b). |
| 31 | Business transferred to new owner 2 months before EDD; employee employed 8 months in total. | Same employer; meets 6-month test. | s 2BA(2); Sch 1 cl 1. |
| 32 | Employee returned from parental leave for an earlier child 4 months before the new EDD (worked 3 years before that). | Period of employment begins on resumption: only 4 months - fails 6-month test. | s 6A(2) (overrides s 43). |
| 33 | Teacher employed by two State school boards consecutively, 3 months each, 20 h/week. | Treated as 1 employment; meets 6-month test. | s 2AC(1). |
| 34 | Employee with two employers (non-teacher), 4 months each, 20 h. | Each employment separately; fails 6-month test with each. | s 2A. |

### Parental leave payment threshold test (s 2BA(4))

| # | Facts | Expected | Provision |
|---|---|---|---|
| 35 | Employee: 26 of the 52 weeks at exactly 10 h, other 26 weeks 0 h. | Meets. | s 2BA(4)(a). |
| 36 | Employee: 25 weeks at 40 h, 27 weeks at 0 h. | **Fails (revised, see note R1).** The person must have been "employed as an employee ... for any 26 of the 52 weeks", and the 26 weeks are then averaged. Only 25 weeks of employment here. (Phase-1 draft said "meets" on a pure best-26-average reading.) | s 2BA(4)(a); s 2 "employee" (b) "an employee for any 26 of the 52 weeks". |
| 37 | Employee: 26 weeks at 9.9 h, rest 0. | Fails (best-26 average 9.9). | s 2BA(4)(a). |
| 38 | Employee: worked only 30 weeks of 52, all at 12 h; with no single employer for 6 months. | Meets payment threshold test (any employer, any 26 weeks), though fails 6-month test. Can request negotiated carer leave (Part 3A). | s 2BA(4)(a); s 30B. |
| 39 | Self-employed 26 of 52 weeks at 10 h. | Meets. | s 2BA(4)(b). |
| 40 | Self-employed 20 weeks working + 6 weeks on ACC weekly compensation (normally 15 h). | ACC weeks count (s 71CB(2)(a)) -> 26 weeks -> meets. | s 2BA(6); s 71CB(2). |
| 41 | Employee 13 weeks at 20 h + self-employed 13 weeks at 20 h (no week with both). | **Ambiguous.** s 2AD(2) says employment and self-employment are treated separately; neither limb alone reaches 26 weeks. Best reading: fails both limbs. | s 2AD; s 2BA(4). |

### Section 4 (comprehensive agreements), s 5, s 6, s 76

| # | Facts | Expected | Provision |
|---|---|---|---|
| 42 | Employment agreement at least as favourable and comprehensive (all 5 matters). | Parts 1-5 do not apply; Parts 6-7A still apply. | s 4(1), (2), (4). |
| 43 | Agreement more favourable but silent on procedural requirements. | Not comprehensive -> its parental-leave provisions of no effect; Parts 1-5 apply. | s 4(2)(e), (3). |
| 44 | Comprehensive but less favourable overall. | Parts 1-5 apply. | s 4(1)(a). |
| 45 | Previous parental leave (other child) ended 31 Jan 2026; new leave sought from 31 Jul 2026. | Not entitled (less than 6 months elapsed since 1 Feb 2026). | s 6(b). |
| 46 | Same, new leave from 1 Aug 2026. | Entitled (6 months have elapsed). | s 6(b). |
| 47 | Previous leave was under an employment agreement (non-statutory), ended 31 Jan 2026; new leave 15 Mar 2026. | Not entitled. | s 6(a)(ii). |
| 48 | EDD 31 Dec 1987. | No leave under this Act. | s 76(1). |
| 49 | Spouse took 40 weeks' leave under an employment agreement; employee (12-month test, combined maximum 52) seeks 20 weeks. | Capped: only 12 weeks under this Act (aggregate may not exceed the Act's total). | s 5. |

---

## B. Leave: Parts 1-3A

### Primary carer leave (ss 8-14)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 50 | Primary carer, meets 6-month test. | May take primary carer leave, max 26 weeks. | s 8(1); s 9(1). |
| 51 | Primary carer, meets 12-month test. | Max 26 weeks (same as 6-month). | s 9(1). |
| 52 | Primary carer, fails both employment tests. | No primary carer leave. | s 8(1)(b). |
| 53 | Not the primary carer (e.g. the partner), meets 12-month test. | No primary carer leave. | s 8(1)(a). |
| 54 | Primary carer who already took primary carer leave for this child. | Not entitled again. | s 8(2)(a). |
| 55 | Partner who became primary carer under s 7(1)(b)(iii) after previously taking partner's leave for the same child. | Entitled (s 8(2) disapplied). | s 8(3). |
| 56 | Leave began under s 13 certificate 10 weeks before EDD. | Entitled to at least 20 weeks after EDD -> total 30 weeks; 4 weeks excess still primary carer leave. | s 9(2), (3). |
| 57 | Leave began under s 14 employer direction 7 weeks before EDD. | Total 27 weeks (20 after EDD); excess 1 week. | s 9(2). |
| 58 | Leave began under s 11 (employee's option) 6 weeks before EDD. | s 9(2) does not apply; max 26 weeks total (only 20 after EDD). | s 9(1),(2) (only s 13/s 14 starts). |
| 59 | Leave began under s 13 certificate 4 weeks before EDD. | 26 weeks covers 22 after EDD; no extension needed; total 26. | s 9(2) "if necessary". |
| 60 | Preterm baby, 5 weeks of preterm baby payments. | Those weeks are additional; primary carer leave still up to 26 weeks besides them (31 weeks total). | s 9(4). |
| 61 | Child born to the employee; no early start. | Primary carer leave begins on date of confinement. | s 10(a). |
| 62 | Adoption; employee becomes primary carer 1 Apr 2026. | Begins 1 Apr 2026. | s 10(c). |
| 63 | EDD 15 Sep 2026; employee elects to start 4 Aug 2026 (42 days earlier). | Permitted (not more than 6 weeks). | s 11(a). |
| 64 | Same, elects 3 Aug 2026 (43 days earlier). | Not permitted under s 11 (needs agreement s 12, certificate s 13 or direction s 14). | s 11. |
| 65 | Same, employer agrees to start 1 Jun 2026. | Permitted. | s 12(a) "any date before". |
| 66 | Certificate date 1 Aug 2026, but confinement 20 Jul 2026. | Begins 20 Jul 2026 (earlier of). | s 13(2). |
| 67 | Certificate date 1 Aug 2026, confinement 10 Aug 2026. | Begins 1 Aug 2026. | s 13(2). |
| 68 | Employer directs start 10 weeks before EDD (no other suitable work). | Permitted (s 14 allows > 6 weeks); s 9(2) gives 20 weeks after EDD. | s 14; s 9(2). |

### Special leave (s 15)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 69 | Pregnant employee asks for special leave, 10 days in total. | Entitled (unpaid). | s 15(1). |
| 70 | Asks for 11th day. | Not entitled under s 15. | s 15(1) "a total of up to 10 days". |
| 71 | After she has started primary carer leave. | Not available ("before taking primary carer leave"). | s 15(1). |
| 72 | Took 8 days special leave; 12-month test; 26 weeks primary carer leave. | Extended leave still 26 weeks (special leave not counted). | s 15(2); s 26(4). |
| 73 | Male employee whose partner is pregnant. | No special leave (female pregnant employee only). | s 15(1). |

*s 15 does not require any employment test.* The section says "A female employee who is pregnant is entitled". Best reading: no 6-month test needed, though Part 1 applies only where s 4 does not oust it.

### Partner's leave (ss 17-22)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 74 | Spouse of primary carer, intends to care, 6-month test. | Partner's leave up to 1 week. | s 17(1); s 19(b). |
| 75 | Same, 12-month test. | Up to 2 weeks. | s 19(a). |
| 76 | Same, 5 months' employment. | No partner's leave. | s 17(1)(c); s 1B(3)(c). |
| 77 | Spouse who does not intend to assume care. | No partner's leave. | s 17(1)(b). |
| 78 | Already took partner's leave for this child. | Not again. | s 17(2)(a). |
| 79 | Biological mother who transferred PLP to partner under s 71E. | No partner's leave. | s 17(2)(b). |
| 80 | EDD 10 Mar 2026, born 1 Mar 2026, employee elects to start 17 Feb 2026 (21st day before EDD). | Permitted. | s 21(a)(i). |
| 81 | Same, start 16 Feb 2026. | Not permitted under s 21 (needs agreement s 22). | s 21(a)(i). |
| 82 | Born 1 Mar 2026, start 22 Mar 2026 (21st day after delivery). | Permitted (window ends at close of 21st day). | s 21(a)(ii). |
| 83 | Same, start 23 Mar 2026; baby discharged 15 Mar. | Not permitted under s 21. | s 21(a)(ii). |
| 84 | Born 1 Mar 2026, baby in NICU until 10 Apr 2026, start 10 Apr. | Permitted (discharge > 21 days after delivery extends window). | s 21(a)(ii). |
| 85 | Same, start 11 Apr 2026. | Not permitted. | s 21(a)(ii). |
| 86 | Any date by agreement with employer. | Permitted. | s 22. |
| 87 | Adoption: spouse intends to become primary carer 1 May 2026; employee starts 10 Apr 2026 (21 days before). | Permitted. | s 21(b). |

### Extended leave (ss 23, 26-29)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 88 | Primary carer, 12-month test, took 26 weeks primary carer leave. | Extended leave = 52 - 26 = 26 weeks. | s 26(1)(b), (3). |
| 89 | Primary carer, 6-month test, took 26 weeks primary carer leave. | Extended leave = 0. | s 26(1)(a), (3). |
| 90 | Primary carer, 12-month, took 10 weeks primary carer leave. | 42 weeks. | s 26(3). |
| 91 | 12-month, primary carer leave of 30 weeks (4 excess under s 9(2)). | 52 - 26 = 26 (excess not deducted). | s 9(3); s 26(3). |
| 92 | Partner, 12-month, took 2 weeks partner's leave; primary carer (12-month) took 26 weeks PCL. | Combined 52 - 26 = 26; partner's leave does not reduce. | s 26(2)(b), (3), (5). |
| 93 | Both 6-month test; PCL 26 weeks. | Combined 26 - 26 = 0. | s 26(2)(a), (3). |
| 94 | Primary carer 12-month (took 26 PCL), partner 6-month. | Combined 52 - 26 = 26; partner may take at most 26 of it. | s 26(2)(c), (3). |
| 95 | Primary carer 6-month (took 26 PCL), partner 12-month. | Combined 52 - 26 = 26; primary carer's own individual max 26 - 26 = 0, so all 26 remaining weeks to partner. | s 26(1)(a), (2)(c), (3); s 28(1)(a). |
| 96 | Primary carer 6-month, PCL 10 weeks; partner 12-month. | Combined 52 - 10 = 42. Primary carer individual: 26 - 10 = 16; partner individual 52 - 10 = 42 (ambiguity: whether partner's individual max is also reduced by the other's PCL; s 26(3) says "the employee and his or her spouse or partner are entitled ... reduced" so yes). | s 26(3). |
| 97 | Neither parent takes PCL; both 12-month. | Combined 52; each up to 52 individually, total <= 52. | s 26(2)(b); s 28(2)(b). |
| 98 | Spouse/partner who does not intend to assume care. | No extended leave. | s 23(1)(a)(ii). |
| 99 | 5 months' employment. | No extended leave. | s 23(1)(b). |
| 100 | Already took 26 weeks extended leave (6-month test). | No further extended leave. | s 23(2). |
| 101 | Preterm baby, 6 weeks preterm baby payments, 12-month test, PCL 26. | Extended leave still 26 (preterm weeks additional). | s 26(6). |
| 102 | Child born 10 Feb 2026; 6-month test (both parents). | Extended leave must end by 10 Aug 2026 (child attains 6 months). | s 27(3) applicable end date (a)(i). |
| 103 | Same, 12-month test. | End date 10 Feb 2027. | s 27(3) (b)(i). |
| 104 | Adoption: first became primary carer 15 Jan 2026; 12-month. | End date 15 Jan 2027. | s 27(3) (b)(ii). |
| 105 | Employee 6-month, spouse 12-month. | **Ambiguous**: both (a) and (b) of "applicable end date" are engaged ("if the employee, or the employee's spouse or partner, qualifies"). Best reading: the later (12-month) end date, since (b) is satisfied and Part 3's combined 52 weeks under s 26(2)(c) could not otherwise be used. | s 27(3). |
| 106 | Extended leave sought to start the day after the applicable end date. | Not allowed. | s 27(4)(a). |
| 107 | Employee ceases to have care of the child mid-leave. | Cannot continue extended leave. | s 27(4)(b). |
| 108 | PCL ended 30 Aug 2026; applicable start date for extended leave. | 30 Aug 2026 ("date of expiry"). | s 27(3) applicable start date (a). |

### Negotiated carer leave (Part 3A)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 109 | Employee not entitled to PCL but meets payment threshold test and is primary carer; EDD 15 Sep 2026; request on 15 Jun 2026. | May request; in time. | s 30B(1), (3)(a). |
| 110 | Same, request on 16 Jun 2026. | Out of time. | s 30B(3)(a). |
| 111 | Adoption, intends to become primary carer 15 Sep 2026; request 1 Sep 2026 (14 days before). | In time. | s 30B(3)(c). |
| 112 | Same, request 2 Sep 2026. | Out of time. | s 30B(3)(c). |
| 113 | Employee who *is* entitled to PCL. | Part 3A does not apply. | s 30B(1)(a). |
| 114 | Employer received request 10 Mar 2026; decision due by. | 10 Apr 2026 (1 month). | s 30D. |
| 115 | Employer refuses on ground "inability to recruit additional staff". | Valid ground. | s 30E(2)(b). |
| 116 | Refuses because "employee is too junior". | Not a permitted ground; refusal invalid (but s 30F(1): employee cannot challenge a refusal; can challenge only non-compliance with s 30D). | s 30E(1); s 30F. |
| 117 | Employer notified refusal on 1 Apr 2026, within 1 month of request (10 Mar). Last day for ERA application. | 1 Apr 2027 (12 months after the notification). | s 30I(3), (4)(a). |
| 118 | Employer never responded to 10 Mar 2026 request. Relevant date. | 10 Apr 2026; application by 10 Apr 2027. | s 30I(4)(b). |
| 119 | Penalty for breach of s 30D. | Max $2,000, payable to employee. | s 30J. |

---

## C. Notices, position, protection: Parts 4-7

| # | Facts | Expected | Provision |
|---|---|---|---|
| 120 | EDD 15 Sep 2026; notice given 15 Jun 2026. | In time. | s 31(3)(a). |
| 121 | Same, notice 16 Jun 2026. | Late -> no extended leave unless 3 months pass from notice or employer agrees (subject to s 68). Primary carer leave itself not lost by s 35. | s 35(1). |
| 122 | Adoption: intends to become primary carer 1 Oct 2026; notice 17 Sep 2026 (14 days before). | In time. | s 33(b). |
| 123 | Same, notice 18 Sep 2026. | Late. | s 33(b). |
| 124 | Primary carer under s 7(1)(b)(iii): notice within a reasonable period after becoming primary carer. | 3-month rule displaced. | s 31(4). |
| 125 | Late notice given 16 Jun 2026; 3 months from notice end. | Extended leave available once 3 months from 16 Jun 2026 have expired (from 16 Sep 2026). | s 35(1)(a). |
| 126 | Incomplete notice given in time. | s 35 does not bar extended leave. | s 35(2). |
| 127 | Employer learns notice is incomplete on 1 Jun 2026. | Must notify by 8 Jun 2026 (7 days); employee then has 14 days after receipt. | s 34(2), (3). |
| 128 | Employer receives s 31 notice 1 Jun 2026. | Must reply by 22 Jun 2026 (21 days); also s 71T PLP notice by the same date. | s 36(1); s 71T. |
| 129 | Employee wants PCL to start early under s 11 on 4 Aug 2026; notice given 14 Jul 2026. | Exactly 21 days -> sufficient (see conventions). | s 37(2). |
| 130 | Same, notice 15 Jul 2026 (20 days). | Insufficient. | s 37(2). |
| 131 | Leave began 1 Mar 2026; employer's s 38 notice due by. | 22 Mar 2026. | s 38. |
| 132 | Leave ends 30 Aug 2026; position kept open; s 39(1) notice of return due by. | 9 Aug 2026 (not later than 21 days before). | s 39(1). |
| 133 | First period of parental leave, 2 weeks, proper notice. | Presumed position kept open; rebuttable only by redundancy. | s 40(1). |
| 134 | Same but 5 weeks. | s 41 applies: rebuttable by key position or redundancy. | s 40(1)(a); s 41. |
| 135 | 4 weeks exactly, second period for the child. | s 41 applies (not first period). | s 40(1)(b). |
| 136 | Employer pay during parental leave. | Not obliged to pay remuneration. | s 42(1). |
| 137 | Annual holiday falls due 6 months after return to work. | Holiday pay at average weekly earnings over the 12 months before the end of the last pay period. | s 42(2)(c). |
| 138 | Employee on leave, employer consents, wants to end early. | May return early (with 21 days' notice under s 39(2)). | s 45(1)(e), (f). |
| 139 | Extend PCL by consent from 20 to 28 weeks (no s 9(2)). | Capped at 26 weeks under s 45(3)-(4). | s 45(4)(a). |
| 140 | Extend partner's leave to 2 weeks when only 6-month test met. | Not beyond 1 week. | s 45(4)(b). |
| 141 | Position kept open; employee fails without good cause to return. | Employment deemed ended from the day leave began (subject to agreement). | s 46(a). |
| 142 | Offered similar position on 1 Oct 2026, leave ended 30 Jun 2026; doesn't take it up by 8 Oct without excuse. | Employment deemed ended from day leave began (offer within 26 weeks: 1 Jul - 29 Dec 2026). | s 47. |
| 143 | Dismissal on 29 Dec 2026, leave ended 30 Jun 2026, no other reason. | Prohibited (within 26 weeks beginning 1 Jul 2026). | s 49(1)(b)(iii). |
| 144 | Dismissal on 30 Dec 2026, same facts, not for a pregnancy/leave reason. | Not caught by s 49(1)(b)(iii). | s 49(1)(b)(iii). |
| 145 | Dismissal during leave with the employee's consent. | Not a contravention. | s 49(2)(a). |
| 146 | Dismissal during leave; employer proves s 51 (a), (b), (c). | Defence made out. | s 51. |
| 147 | Dismissal during leave; employer proves redundancy but had reduced seniority. | No defence (s 51(c) fails). | s 51(c). |
| 148 | Dismissal for a substantial reason unrelated to pregnancy/leave (serious misconduct) outside protected period. | Lawful. | s 54. |
| 149 | Dismissal 1 Mar 2026; application for interim order 1 May 2026. | Within "the preceding 2 months" - may apply (2 months after 1 Mar is 1 May). | s 55(1). |
| 150 | Same, application 2 May 2026. | Out of time. | s 55(1). |
| 151 | Interim order made 1 Jun 2026; EDD 1 Mar 2027. | Expiry may be up to the later of 30 Nov 2026 and 30 Aug 2027 -> latest 30 Aug 2027. | s 55(2). |
| 152 | Complaint: subject arose 1 Mar 2026; EDD 1 Apr 2026; leave ended 30 Sep 2026. Deadline. | Latest of 30 Aug 2026, 30 Sep 2026, 25 Nov 2026 -> 25 Nov 2026. | s 56(2). |
| 153 | Complaint: subject arose 1 Dec 2026; EDD 1 Apr 2026; no leave taken. | Latest of 1 Jun 2027 and 30 Sep 2026 -> 1 Jun 2027. | s 56(2)(a). |
| 154 | Complaint lodged the day after the latest deadline. | Out of time. | s 56(2). |
| 155 | Objection to Labour Inspector determination served 1 Jun 2026; lodged 29 Jun 2026. | In time (28 days). | s 70C(2). |
| 156 | Same, lodged 30 Jun 2026. | Out of time; a demand notice then has s 70D consequences. | s 70C(2), (3). |
| 157 | Employer fails to allow PLP rights because of employee's late notice given in good faith and reasonable. | ERA must grant relief. | s 68(4). |

---

## D. Parental leave payments: Part 7A

### Eligibility (ss 71CA, 71D, 71F, 71G)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 158 | Primary carer, meets threshold test, takes leave. | Entitled. | s 71CA; s 71D(1). |
| 159 | Primary carer, meets threshold test, keeps working (no leave). | Not entitled. | s 71D(1)(b). |
| 160 | Primary carer, fails threshold test. | Not entitled. | s 71CA(b). |
| 161 | Not primary carer (e.g. partner without transfer), meets threshold. | Not entitled (except via transfer/succession). | s 71D(1)(a). |
| 162 | Employee covered by comprehensive agreement (s 4). | Ignored for PLP eligibility; still entitled. | s 71CA(2); s 4(4). |
| 163 | Previously received PLP for this child. | Not entitled. | s 71D(2)(a). |
| 164 | Spouse previously received PLP for this child; person's entitlement arises from s 71E transfer. | Entitled (exception). | s 71D(2)(b). |
| 165 | s 7(1)(b)(iii) primary carer whose partner (mother) received PLP. | s 71D(2) disapplied; entitled. | s 71D(3). |
| 166 | Previous PLP period for another child ended 31 Jan 2026; new child's period would start 31 Jul 2026. | **Ambiguous** "fewer than 6 months have elapsed after the end". Previous period ended 31 Jan; 6 months after = 31 Jul. On 31 Jul exactly 6 months have elapsed -> not fewer -> entitled. On 30 Jul -> not entitled. (Contrast s 6, which counts from the day after.) Measured at the start of the new payment period. | s 71F(a). |
| 167 | Received parental tax credit for the child. | Loses entitlement. | s 71G(2). |
| 168 | Spouse received PTC for the child. | Loses entitlement. | s 71G(2). |
| 169 | Self-employed primary carer meeting threshold, temporarily not working. | Entitled. | s 71CB; s 71D(1). |

### Average weekly income (ss 71CAA, 71CBA)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 170 | Employee: 52 weekly earnings, 26 weeks at $1,000, 26 at $500. | $1,000. | s 71CAA(1). |
| 171 | Employee: 10 weeks at $2,600, 42 weeks at $0. | $26,000 / 26 = $1,000 (divide by 26 regardless). | s 71CAA(1)(b). |
| 172 | Employee earns from two employers in same week ($300 + $400). | Weekly gross $700 ("from all employments"). | s 71CAA(1)(a). |
| 173 | Self-employed, elects 12-month, net income $52,000, no excluded weeks. | $1,000. | s 71CBA(2). |
| 174 | Same, 4 complete weeks on ACC. | $52,000 / 48 = $1,083.33. | s 71CBA(4). |
| 175 | Self-employed elects 6-month, net income $13,000, 0 excluded. | $500. | s 71CBA(3). |
| 176 | Same, 6-month with 6 excluded weeks. | $13,000 / 20 = $650. | s 71CBA(4). |
| 177 | Self-employed, net loss (-$5,000). | AWI negative; rate is the s 71N(4) minimum. | s 71M(1A)(b)(ii). |

### Rate (s 71M)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 178 | Employee: OWP $900, AWI $700, cap $811.05. | $811.05. | s 71M(1). |
| 179 | Employee: OWP $500, AWI $650. | $650 (greater). | s 71M(1)(b). |
| 180 | Employee: OWP $650, AWI $500. | $650. | s 71M(1)(b). |
| 181 | Employee: OWP $811.05 exactly. | $811.05. | s 71M(1). |
| 182 | Employee: OWP $100, AWI $120. | $120 (no minimum for employees). | s 71M(1). |
| 183 | Self-employed: AWI $150; min wage $23.95. | $239.50 (10 h x min wage). | s 71M(1A); s 71N(4). |
| 184 | Self-employed AWI $500. | $500. | s 71M(1A). |
| 185 | Self-employed AWI $2,000. | $811.05. | s 71M(1A)(a). |
| 186 | Both employee and self-employed: employee limb $600, self-employed limb $400. | **Ambiguous**: s 71M(1B) sets only the cap; combined rate presumably sum ($1,000) capped -> $811.05. Best reading: the sum, capped. | s 71M(1B). |
| 187 | Cap adjusted (input) to $850; employee AWI $900. | $850. | s 71M(1)(a) "or any adjusted amount". |

### Start, end, duration (ss 71J-71L)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 188 | Birth-mother; leave begins 1 Mar 2026; confinement 15 Mar. | Payment starts 1 Mar 2026. | s 71K(1)(a). |
| 189 | Leave begins 20 Mar 2026; confinement 15 Mar 2026. | Starts 15 Mar 2026. | s 71K(1)(a). |
| 190 | Adoption, primary carer from 1 Apr 2026. | Starts 1 Apr 2026. | s 71K(1)(b). |
| 191 | Employee takes 2 weeks paid leave at start of parental leave (to 14 Mar 2026) and elects. | Starts 15 Mar 2026. | s 71K(3). |
| 192 | s 7(1)(c) primary carer stops working 10 Apr 2026. | Starts 11 Apr 2026 (day after). | s 71K(2)(c). |
| 193 | Start 1 Mar 2026, no return to work. | Ends 30 Aug 2026 (26 weeks after). | s 71L(1)(a). |
| 194 | Start 1 Mar 2026, returns to work 1 Jun 2026. | Ends 1 Jun 2026. | s 71L(1)(b). |
| 195 | Start 1 Mar 2026, adoptive primary carer ceases to be primary carer 1 May 2026. | Ends 1 May 2026. | s 71L(1)(c). |
| 196 | Biological mother; child dies 1 May 2026; start 1 Mar 2026; no return. | Continues to 30 Aug 2026. | s 71L(2)(b). |
| 197 | 26 weeks shared by transfer: mother 16, partner 10. | Valid. | s 71J(1)(b). |
| 198 | Mother 16, partner 12. | Exceeds 26 -> invalid. | s 71J(1)(b). |

### Preterm baby payments (s 71DA), keeping in touch (ss 71CE, 71DB)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 199 | Born alive 1 Jun 2026; 36th week would have ended 3 Aug 2026 (63 days). | 9 weeks preterm baby payment; period 1 Jun - 3 Aug 2026. | s 71DA(1)-(4). |
| 200 | 36th week ends 20 weeks after birth (extremely preterm). | 13 weeks (cap). | s 71DA(2). |
| 201 | Born after the 36th week ended (term). | No preterm baby payment. | s 71DA(1)(b). |
| 202 | Born on the last day of the 36th week. | **Edge**: "before the end of the 36th week" - born on the last day is before the *end* of it; number of weeks between = 0 -> entitled in principle but to 0 weeks. Expected weeks = 0. | s 71DA(1)(b), (2). |
| 203 | Stillborn before 36 weeks. | No preterm baby payment ("born alive"). | s 71DA(1)(b). |
| 204 | 30 days between birth and 36-week date. | **Ambiguous** partial weeks: 4 2/7 weeks. The payment period ends on the 36-week date (s 71DA(4)(a)), so the person is paid for 30 days. If whole weeks required: 4. I would assert 4 complete weeks only if the encoding uses whole weeks; my preferred answer is the actual 30-day period. | s 71DA(2), (4). |
| 205 | Preterm, not entitled to PLP (fails threshold). | No preterm baby payment. | s 71DA(1)(a). |
| 206 | Keeping-in-touch: 64 h total, not within 28 days of birth. | Not treated as returned to work. | s 71CE(1). |
| 207 | 65 h. | Treated as returned to work; later PLP recoverable. | s 71CE(3)(b). |
| 208 | Born 1 Mar 2026; KIT work on 29 Mar 2026 (28th day after). | Within 28 days -> treated as returned to work. | s 71CE(2)(b), (3)(a). |
| 209 | Same, KIT on 30 Mar 2026. | Permitted. | s 71CE(2)(b). |
| 210 | Preterm baby; KIT work on day 5 after birth. | Permitted (28-day rule disapplied). | s 71CE(4). |
| 211 | Preterm payment period 9 weeks: additional KIT hours. | 27 h in addition to 64. | s 71DB(1)(a), (2). |
| 212 | Exceeds 27 h in preterm period. | Returned to work the day after excess; preterm payments after recoverable; PLP entitlement not affected. | s 71DB(4). |

### Applications, review, recovery, offences, succession

| # | Facts | Expected | Provision |
|---|---|---|---|
| 213 | Child born 1 Mar 2026; no return to work; application deadline. | Must be before 1 Mar 2027; application on 28 Feb 2027 in time, 1 Mar 2027 late. | s 71I(2)(a)(ii). |
| 214 | Same but returns to work 1 Oct 2026. | Before 1 Oct 2026. | s 71I(2)(a)(i). |
| 215 | Adoption, first primary carer date 15 Jan 2026. | Before 15 Jan 2027. | s 71I(2)(a)(iii). |
| 216 | s 7(1)(b)(iii) primary carer. | Before or within a reasonable period after the earliest of return to work / first anniversary. | s 71I(3). |
| 217 | Late application, in good faith, not disputed with employer. | Department may approve (s 71IA), discretionary. | s 71IA. |
| 218 | Overpayment, error not by recipient, good faith, position changed. | Not recoverable. | s 71Y. |
| 219 | Overpayment, recipient contributed intentionally. | Recoverable. | s 71X; s 71Y. |
| 220 | Overpayment, good faith but position not altered. | Recoverable. | s 71Y(b). |
| 221 | Offence under s 71Z: max fine. | $15,000. | s 71Z(3). |
| 222 | Offence known to department 1 Mar 2026, should reasonably have been known 1 Jan 2026. | Charging document by 1 Jul 2026 (6 months after the earlier). | s 71Z(4). |
| 223 | Department decision notified 10 Mar 2026; review deadline. | 10 Mar 2027 (12 months after). | s 71ZB(2). |
| 224 | Employee dies 1 May 2026; spouse's bereavement leave expires 5 May. | Date of succession 5 May 2026. | s 72C(1). |
| 225 | Death 1 May 2026, no bereavement leave. | 1 May 2026. | s 72C(1). |

### Schedule 1AA

| # | Facts | Expected | Provision |
|---|---|---|---|
| 226 | EDD 30 Jun 2020, born 1 Jul 2020. | 2017 Amendment Part 2 applies (born on or after 1 Jul 2020). | Sch 1AA cl 5(1)(a)(ii). |
| 227 | EDD 15 Jul 2020, born 28 Jun 2020. | Applies (EDD on or after). | cl 5(1)(a)(i). |
| 228 | EDD 29 Jun 2020, born 28 Jun 2020. | Does not apply; the version of the Act encoded (2026) does not state the earlier law -> refuse. | cl 5(1). |
| 229 | Adoption, primary carer from 1 Jul 2020. | Applies. | cl 5(1)(b). |
| 230 | Adoption, primary carer from 30 Jun 2020. | Does not apply. | cl 5(1)(b). |

(230 scenarios; the brief asked for about 150.)

---

## Ambiguities, and the readings chosen

1. **s 2BA(4) "average ... for any 26 of the 52 weeks"** (scenarios 36, 41): there must be 26 weeks in which the person was employed (or self-employed), and the average over 26 such weeks must be at least 10 hours. Weeks with no employment cannot be among the 26. Alternative readings: (i) the 26 busiest weeks averaged, counting zero-hour weeks (the encoding's reading); (ii) 26 weeks each of 10+ hours.
2. **s 7(2) no nomination** (16): neither is entitled until nominated.
3. **s 27(3) mixed tests** (105): the 12-month end date.
4. **s 26(3) reduction applies to both partners' individual maxima** (96).
5. **s 71DA partial weeks** (204): actual days; whole-weeks answer 4 would be defensible.
6. **s 71F "fewer than 6 months have elapsed after the end"** (166): counted from the end date itself, unlike s 6.
7. **s 71M(1B)** (186): sum of the two limbs, capped.
8. **Day counts** "not less than 21 days" (129): simple difference.
9. **s 2AD** (41): employment and self-employment hours are not pooled.


---

## R1. Revision made during phase 2 (disclosed)

While mapping scenario 41 to the encoding's inputs I saw that my phase-1 answers to 36 and 41 were inconsistent: on the pure "best 26 weeks averaged" reading I gave for 36, scenario 41 (13 weeks at 20 h) would *meet* the test, yet I had answered "fails". Reconciling them from the Act (s 2BA(4)(a) "employed as an employee ... for any 26 of the 52 weeks"; s 2 "employee" para (b), "an employee for any 26 of the 52 weeks"), the employment itself must cover 26 weeks. I therefore revised 36 to **fails**. This moves my answer *away* from the encoding, not towards it, and no other expected value was changed after the encoding was read.

## Phase-2 additions (values from the Act; scenarios suggested by the encoding's shape)

| # | Facts | Expected | Provision |
|---|---|---|---|
| 10b | Aunt is the only person who took permanent primary responsibility for a 4-year-old; there is no s 7(2) nomination because there is no second person. | Primary carer under (c). s 7(2) applies only "If 2 or more persons meet the criterion". | s 7(1)(c), (2). |
| 4b | Mother's partner takes responsibility when the child is exactly 12 months old. | Not (b)(iii) ("under 1 year"). | s 7(1)(b)(iii)(A). |
| 24c | Employed 12 months, 12-month average 9.9, 6-month average 10. | 6-month test. | s 2BA(1). |
| 37b-d | 52 weeks at 9 h: fails. 22 weeks at 12 + 30 at 9: meets. 1 week at 135 + 26 at 5 (27 weeks employed): meets (26 employed weeks averaging 10). | s 2BA(4). |
| 46b | Previous parental leave (other child) ended 31 Jan 2026; EDD 25 Jul 2026; child born 2 Aug 2026 and primary carer leave begins 2 Aug 2026. | s 6 does **not** bar: by 2 Aug, 6 months have elapsed since 1 Feb. s 6 asks whether the employee is "entitled to parental leave"; the natural time to measure the elapsed period is when the leave is taken, not the EDD. | s 6(b); s 10(a). |
| 6-ext | s 6 bars this child's leave (previous leave ended 31 Jan 2026, EDD 15 Mar 2026). | No extended leave either: "parental leave" includes extended leave (s 2), and s 6 removes entitlement to "parental leave in respect of a child". | ss 2, 6. |
| 6-partner | The partner (12-month test) whose own previous parental leave for another child ended 31 Jan 2026; this child due 15 Mar 2026. | No partner's leave and no extended leave (s 6 applies to all parental leave, including partner's leave). | ss 2, 6, 17. |
| 148b/c | Dismissal during parental leave (1 May 2026), or on the last day of the 26 weeks after it (29 Dec 2026), for a substantial reason unrelated to the pregnancy, child, or rights under the Act; no s 51/52 defence. | Not a contravention: "Nothing in this Act shall affect any right of an employer to dismiss an employee for a substantial reason not related to" those matters. | s 54; s 49(1)(c). |
| 164 | Mother transferred part of her PLP under s 71E to her partner; the mother has already received payments for the child; the partner (meets threshold, stops work) claims. | Entitled: s 71D(2)(b) excepts a spouse whose "entitlement arises from a transfer under section 71E". | s 71D(2)(b). |
| 166b | Previous PLP period (other child) ended 31 Jan 2026; EDD 25 Jul 2026; born and payments begin 2 Aug 2026. | Entitled: by 2 Aug, 6 months have elapsed "after the end of the period". s 71F is about entitlement to a payment, which starts on 2 Aug (s 71K(1)(a)). | s 71F(a); s 71K. |
| 186b | Employee and self-employed: ordinary weekly pay $300, earnings $300/wk, self-employed net $10,400 for 12 months ($200/wk, so the s 71N(4) minimum of $239.50 applies). | $539.50 (sum, below the cap). | s 71M(1), (1A), (1B). |
| 153b | Complaint: subject arose 1 Jan 2026; EDD 1 Apr 2026; no leave. | 30 Sep 2026 (the EDD limb is latest). | s 56(2)(b). |
| 102b | EDD 1 Feb 2026, born 10 Feb 2026, 6-month test. | End date 10 Aug 2026 (child "attains the age of 6 months", which runs from birth). | s 27(3). |
| 118b | NCL request received 10 Mar 2026, refusal notified late, 15 Apr 2026. | Relevant date 10 Apr 2026; ERA application by 10 Apr 2027. | s 30I(4)(b). |

## Phase-2 notes: scenarios the encoding cannot express

- **s 2B** (17-20: twins, children within 4 weeks), **s 2A, 2AC** (33-34: multiple employments), **s 6A** (32), **s 72A** (27-30), **Schedule 1** (31): the encoding takes the averages and dates as inputs; nothing to test.
- **s 5** (49: aggregation with the spouse's non-statutory leave): carried as text only.
- **s 4** is a free-standing function; the top-level goal takes no input for a comprehensive agreement, so a s 4-ousted employee still gets primary carer, partner's and extended leave from the goal. (42-44 tested on the function only.)
- **s 7(2)** nomination: the input `is the person nominated under s 7(2)` is required for every (c) carer, including a sole carer (10b fails).
- **ss 10, 12-14** start dates, **s 13(2)** earlier-of (66-67), **s 9(4)/s 26(6)** preterm weeks not counting (60, 101): only s 9(1)-(2) and s 11 are encoded.
- **s 15(1)** "before taking primary carer leave" and "female ... pregnant" (71, 73): only the number 10 is encoded; s 15(2)/s 26(4) (72) holds trivially since special leave is not an input.
- **s 21** with the s 22 agreement, **s 27(4)(b)** ceasing care (107), **s 27(3)** applicable start date (108): not encoded.
- **s 30B(3)(b)** reasonable period for (b)(iii) carers; **ss 30F-30H**: text only.
- **s 31(4), s 33(a),(c), s 34(1), s 36(3), s 37(1)**: not encoded; dates only.
- **s 45(4)(c)** extended leave extension cap: not encoded (only (a) and (b)).
- **s 47** "within 7 days" of the specified date and the 26-week offer window (142): inputs, not dates.
- **s 51 / s 52** elements: a single boolean `defence proved`; the s 40(1) vs s 41 branch of s 51(a) is not distinguished.
- **s 55(2)** interim order expiry (151), **s 68(4)** mandatory relief (157), **s 70A-70G**: not encoded.
- **s 71CE(2)(b)** 28-day window (208-209): a boolean input; the date edge (29 Mar vs 30 Mar for a 1 Mar birth) cannot be tested.
- **s 71DB(4)(c)** (PLP entitlement unaffected by excess preterm hours): the encoding returns a single "treated as returned to work" flag, so this distinction cannot be expressed.
- **s 71D(4), s 71K(2)(b)-(c)** designated start dates for (b)(iii) and (c) carers (192): not encoded except through the s 71K(3) paid-leave route.
- **s 71I(3)** reasonable period for (b)(iii) carers (216), **s 71IA** (217): not encoded.
- **s 71J(1)(b)** split between transferor and transferee (197-198): only the constant 26.
- **s 76** (48): pre-1988 children are refused by the 2020 cut-off, which is the right result for a different reason.
