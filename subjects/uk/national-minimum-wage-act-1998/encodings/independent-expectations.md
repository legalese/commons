# Independent expectations — National Minimum Wage Act 1998

Written from BRIEF.md and the source text (ukpga-1998-39.txt, PiT 7 April 2026) only, before any `.l4` file was opened. Each scenario gives the inputs, the expected answer, and the words of the Act that give it.

## Readings taken (ambiguities)

- **R-a. s 11(3) "period of three months following" day X.** Following the brief, the last day is the corresponding date three months after X, or the last day of that month if no corresponding date exists. (Note: under the Dodds v Walker corresponding-date rule a period starting X+1 ends on the day before the corresponding date of X+1. That gives the same answer except where X is the last day of a short month that is not the last day of the target month, e.g. X = 28 Feb 2027 → brief 28 May 2027, Dodds-style 31 May 2027. I follow the brief.)
- **R-b. s 10(9)(a).** The period of 14 days "following the date of receipt" starts the day after receipt, so the last day for production is receipt + 14. No move for weekends or bank holidays.
- **R-c. s 10(9)(b).** A later time counts only if it was agreed "during that period" (on or before receipt + 14). Otherwise (a) governs, and so does s 11(3)(a).
- **R-d. s 11A(2) then (3).** First add the days from the day after Day A to Day B inclusive, i.e. (B − A) days. Then, if that date falls in [Day A, Day B + 1 month] (both ends inclusive), the limit becomes Day B + 1 month.
- **R-e. Day A after the s 11(3) limit has expired.** The time already expired, so nothing remains to stop and no extension applies: the limit is unchanged. (The literal text of s 11A(2) does not say so; this is the usual reading. ETA 1996 s 18A puts it the same way.)
- **R-f. s 17(6).** "The amounts described in subsections (2) and (4) ... regarded as reduced by" the payment. I read it as reducing each computed amount (A, and A/R1 × R2) by the payment, so the entitlement is max(A, A/R1 × R2) − paid. I do not read it as putting the reduced A back into the formula. Floor at 0.
- **R-g. s 17(5).** Payment ≥ the entitlement *at the time of that payment* (using R2 as at that time and net of earlier payments) ends s 17(1) for that period for good. Later rate rises do not revive it.
- **R-h. s 17 applies only where the worker was paid below the NMW (A > 0).** If A = 0 the entitlement is 0.
- **R-i. s 28(1).** In civil proceedings, qualification is presumed unless the contrary is established. A fact that is not established cannot defeat qualification there. Outside civil proceedings the presumption does not apply.
- **R-j. s 40.** The deeming covers only s 1(2)(b) (ordinarily works in the UK). If a carve-out applies (wholly outside the UK / not ordinarily resident), the s 1(2)(b) facts decide as normal.
- **R-k. Rounding.** The Act gives no rounding for s 17(4). I use inputs where the answer is exact.

## A. Who qualifies (ss 1(2), 28(1), 34, 35, 37, 37A, 40, 43, 44, 44A, 45, 45A, 45B, 54(3), s 3 regs)

Baseline B: individual; worker under a contract of employment; works in the UK; has ceased to be of compulsory school age; no exclusion facts; no s 3 regulation disqualifies.

| # | Inputs (variation from B) | Expected | Act |
|---|---|---|---|
| Q1 | baseline | qualifies | s 1(2)(a)-(c) |
| Q2 | still of compulsory school age | does not qualify | s 1(2)(c) "has ceased to be of compulsory school age" |
| Q3 | neither working nor ordinarily working in UK | does not | s 1(2)(b) |
| Q4 | not working in UK now but *ordinarily* works in UK | qualifies | s 1(2)(b) "is working, or ordinarily works" |
| Q5 | no contract of employment; other contract, personal service, other party not a client/customer | qualifies | s 54(3)(b) |
| Q6 | other contract, no personal-performance undertaking (not a home worker) | does not (not a worker) | s 54(3)(b) "personally" |
| Q7 | other contract, personal service, other party *is* a client or customer of the individual's business | does not | s 54(3)(b) "whose status is not ... client or customer" |
| Q8 | home worker, work "otherwise" than personally, other party not a client | qualifies | s 35(1) "(whether personally or otherwise)" |
| Q9 | home worker but other party is a client/customer | does not | s 35(1) only substitutes "personally"; the client limb stays |
| Q10 | agency worker: supplied by agent to principal, no worker's contract with either, not client/customer arrangement | qualifies | s 34(1)-(2) |
| Q11 | agency arrangement but the individual contracts with the principal as a client of his own business | does not | s 34(1)(c) |
| Q12 | mariner on UK-registered ship, not wholly outside UK, ordinarily resident in UK; otherwise not working in UK | qualifies | s 40 "shall be treated as ... ordinarily works in the United Kingdom" |
| Q13 | as Q12 but employment wholly outside UK | does not | s 40(a) |
| Q14 | as Q12 but not ordinarily resident in UK | does not | s 40(b) |
| Q15 | serving member of armed forces, in respect of that service | does not | s 37(1) |
| Q16 | Cadet Force Adult Volunteer (Army Cadet Force), assisting otherwise than in Crown employment | does not | s 37A(1) |
| Q17 | Cadet force member assisting *in the course of Crown employment* | qualifies | s 37A(1)(b) |
| Q18 | master/crew of fishing vessel paid only by share of profits | does not | s 43 |
| Q19 | fishing crew paid a wage plus a share | qualifies | s 43(b) "only by a share" |
| Q20 | worker for a charity, no money except expenses actually incurred, no benefits in kind | does not | s 44(1)(a)(i), (b) |
| Q21 | charity worker, expenses reasonably estimated, subsistence and reasonable accommodation only | does not | s 44(1)(a)(ii), (b) |
| Q22 | charity worker paid a wage | qualifies | s 44(1)(a) fails |
| Q23 | charity worker given a benefit in kind other than subsistence/accommodation (e.g. general training) | qualifies | s 44(1)(b), (3)(a) |
| Q24 | as Q23 but the only training is to improve ability to do the agreed work | does not | s 44(3)(b) |
| Q25 | unpaid worker for a commercial company (not charity, voluntary org, fund-raising or statutory body) | qualifies | s 44(1) employer types |
| Q26 | subsistence-only payments, placed through arrangements by a charity, work for a charity | does not | s 44(2) |
| Q27 | subsistence-only payments, no charity arrangement | qualifies | s 44(2)(a) fails |
| Q28 | worker for a statutory body, expenses only | does not | s 44(1) "a statutory body" |
| Q29 | residential member of a charity religious community, members live together for that purpose | does not | s 44A(1)-(2) |
| Q30 | as Q29 but the community is an independent school | qualifies | s 44A(3)(a) |
| Q31 | as Q29 but the community provides a course of further or higher education | qualifies | s 44A(3)(b) |
| Q32 | community member who does not live with them | qualifies | s 44A(4) |
| Q33 | community not a charity nor established by one | qualifies | s 44A(2)(a) |
| Q34 | prisoner doing work in pursuance of prison rules | does not | s 45(1) |
| Q35 | prisoner but work not in pursuance of prison rules | qualifies | s 45(1) |
| Q36 | work under a Courts Act 2003 Sch 6 work order | does not | s 45A |
| Q37 | person disqualified by IAA 1999 s 153A | does not | s 45B |
| Q38 | s 3 regulations disqualify | does not | s 3 (input) |
| Q39 | not an individual (a company) | does not | s 1(2) "an individual" |
| Q40 | civil proceedings, contrary not established | qualifies (presumed) | s 28(1) |
| Q41 | civil proceedings, contrary established (e.g. Q34 facts proved) | does not | s 28(1) "unless the contrary is established" |

## B. Arrears (s 17)

Notation: A = shortfall (s 17(2)), R1 = rate payable in the period, R2 = rate under the regulations in force at the time of determination. Entitlement = max(A, A/R1 × R2) − paid (R-f), 0 if ceased (R-g).

| # | Inputs | Expected | Act |
|---|---|---|---|
| S1 | received 900, would have received 1000 at NMW (A = 100), R1 = 10, R2 = 10 | 100 | s 17(1)-(4); equal |
| S2 | A = 100, R1 = 10, R2 = 12.5 | 125 | s 17(4) A/R1 × R2 = 100/10 × 12.5 |
| S3 | A = 200, R1 = 8, R2 = 12 | 300 | s 17(4) |
| S4 | A = 120, R1 = 12, R2 = 10 (rate fell) | 120 | s 17(1) "whichever is the higher"; (b) = 100 |
| S5 | received 1000, would have received 1000 (A = 0) | 0 | s 17(1) "less than" (R-h) |
| S6 | received 1100 > 1000 | 0 | s 17(1) |
| S7 | A = 100, R1 = 10, R2 = 12.5, one payment 50 made when R2 then = 12.5 | 75 | s 17(6) |
| S8 | A = 100, R1 = 10; payment 125 at t1 (R2 then 12.5); determination R2 = 13 | 0 | s 17(5) ceased |
| S9 | A = 100, R1 = 10; payment 100 at t1 (R2 then 12.5, entitlement 125) — not full; at determination R2 = 13 | 30 | s 17(6): 130 − 100 |
| S10 | A = 100, R1 = 10; payment 100 at t1 with R2 then = 10 (entitlement 100) — full; determination R2 = 13 | 0 | s 17(5) |
| S11 | A = 100, R1 = 10; t1 R2 = 11 pays 60 (ent 110); t2 R2 = 12 pays 60 (ent 120 − 60 = 60, full); determination R2 = 13 | 0 | s 17(5) at t2 |
| S12 | as S11 but t2 pays 50 | 20 | 130 − 110 |
| S13 | A = 100, R1 = 10, payment 200 at t1 (R2 then 11) | 0 | s 17(5) |
| S14 | A = 100, R1 = 10, payment 30 at t1 (R2 then 10), determination R2 = 10 | 70 | s 17(6) |
| S15 | payments listed out of chronological order (t2 before t1 in the list) — same as S12 | 20 | the Act runs on time, not list order |
| S16 | worker does not qualify (e.g. prisoner, contrary established), A = 100 | 0 | s 17(1) "a worker who qualifies" |
| S17 | two periods: S2 (125) + S3 (300) | 425 | s 17(1) per pay reference period |
| S18 | A from hours: 40 h × NMW 10 = 400 would-have; received 350 → A = 50; R1 = 10, R2 = 11 | 55 | s 17(2)/(4) |
| S19 | A = 100, R1 = 10, R2 = 12.5, payment exactly 125 at determination time (R2 12.5) | 0 | s 17(5) "paid ... to which he is at that time entitled" |

## C. Records: production date (s 10(9))

| # | Receipt of production notice | Expected last day | Note |
|---|---|---|---|
| P1 | Mon 1 Mar 2027 | Mon 15 Mar 2027 | receipt + 14 |
| P2 | Mon 20 Dec 2027 | Mon 3 Jan 2028 | over the year end |
| P3 | Tue 15 Feb 2028 | Tue 29 Feb 2028 | leap day |
| P4 | Mon 15 Feb 2027 | Mon 1 Mar 2027 | non-leap |
| P5 | Sat 17 Jan 2026 | Sat 31 Jan 2026 | no weekend move |
| P6 | 1 Mar 2027, later day 10 Apr 2027 agreed on 5 Mar 2027 | 10 Apr 2027 | s 10(9)(b) |
| P7 | 1 Mar 2027, later day 10 Apr 2027 agreed 15 Mar 2027 (last day of period) | 10 Apr 2027 | "during that period" inclusive |
| P8 | 1 Mar 2027, later day agreed 16 Mar 2027 (after period) | 15 Mar 2027 | R-c |

## D. Complaint limit (s 11(3))

| # | Receipt / agreed day | End of 14 days (X) | Expected limit | Note |
|---|---|---|---|---|
| C1 | 1 Mar 2027 | 15 Mar 2027 | Tue 15 Jun 2027 | plain |
| C2 | Sun 17 Jan 2027 | Sun 31 Jan 2027 | Fri 30 Apr 2027 | no 31 Apr |
| C3 | 16 Nov 2027 | Tue 30 Nov 2027 | Tue 29 Feb 2028 | leap year |
| C4 | 16 Nov 2026 | 30 Nov 2026 | Sun 28 Feb 2027 | non-leap |
| C5 | 14 Feb 2028 | 28 Feb 2028 | Sun 28 May 2028 | R-a (not 31 May) |
| C6 | 15 Feb 2028 | 29 Feb 2028 | Mon 29 May 2028 | |
| C7 | 17 Dec 2027 | 31 Dec 2027 | Fri 31 Mar 2028 | |
| C8 | 1 Mar 2027 with later day 31 Aug 2027 agreed in time | — | Tue 30 Nov 2027 | s 11(3)(b) from that later day |
| C9 | 1 Mar 2027 with agreement out of time (16 Mar) | 15 Mar 2027 | 15 Jun 2027 | R-c |
| C10 | 14 Oct 2027 | 28 Oct 2027 | 28 Jan 2028 | (used in E8) |
| C11 | 14 Oct 2026 | 28 Oct 2026 | 28 Jan 2027 | (used in E9) |

## E. Early-conciliation extension (s 11A)

| # | Base limit L | Day A | Day B | L + (B−A) | B + 1 month | Expected | Note |
|---|---|---|---|---|---|---|---|
| E1 | 15 Jun 2027 | 1 Jun 2027 | 15 Jun 2027 | 29 Jun | 15 Jul 2027 | Thu 15 Jul 2027 | (3) applies |
| E2 | 15 Jun 2027 | 1 May 2027 | 8 May 2027 | 22 Jun | 8 Jun | Tue 22 Jun 2027 | (2) only |
| E3 | 15 Jun 2027 | 16 Jun 2027 | 20 Jun 2027 | — | — | 15 Jun 2027 | Day A after limit, R-e |
| E4 | 15 Jun 2027 | 15 Jun 2027 | 15 Jun 2027 | 15 Jun = Day A | 15 Jul | 15 Jul 2027 | boundary exactly at Day A |
| E5 | 15 Jun 2027 | 15 Jun 2027 | 29 Jun 2027 | 29 Jun | 29 Jul | Thu 29 Jul 2027 | Day A on the limit |
| E6 | 15 Jun 2027 | 15 May 2027 | 20 May 2027 | 20 Jun | 20 Jun | Sun 20 Jun 2027 | exactly at B + 1 month (inclusive) |
| E7 | 15 Jun 2027 | 14 May 2027 | 20 May 2027 | 21 Jun | 20 Jun | Mon 21 Jun 2027 | one day past window |
| E8 | 15 Jun 2027 | 16 May 2027 | 20 May 2027 | 19 Jun | 20 Jun | 20 Jun 2027 | inside window |
| E9 | 30 Apr 2027 | 20 Apr 2027 | 31 May 2027 | 10 Jun | 30 Jun 2027 (no 31 Jun) | Wed 30 Jun 2027 | month-end |
| E10 | 28 Jan 2028 | 25 Jan 2028 | 31 Jan 2028 | 3 Feb | 29 Feb 2028 | Tue 29 Feb 2028 | leap |
| E11 | 28 Jan 2027 | 25 Jan 2027 | 31 Jan 2027 | 3 Feb | 28 Feb 2027 | Sun 28 Feb 2027 | non-leap |
| E12 | 15 Jun 2027 | 16 Mar 2027 | 20 Mar 2027 | 19 Jun | 20 Apr | Sat 19 Jun 2027 | (2) only |
| E13 | 15 Jun 2027 | 15 Jun 2027 | 15 Jun 2027 | via the full chain from receipt 1 Mar 2027 | | 15 Jul 2027 | end-to-end |

## F. Award (s 11(2))

| # | Hourly NMW in force when award made | Expected award | Act |
|---|---|---|---|
| F1 | 12.71 | 1016.80 | s 11(2)(b) "80 times the hourly amount ... (as in force when the award is made)" |
| F2 | 12.21 | 976.80 | |
| F3 | 10 | 800 | |
| F4 | rate in force at the breach 11.44, at the award 12.71 | 1016.80 (uses award-time rate) | "as in force when the award is made" |

## Addendum (written after reading the record shapes in step 3, before any test was run; values from the Act alone)

| # | Inputs | Expected | Act |
|---|---|---|---|
| S20 | A = 120 (R1 12), part payment 20 when R2 then 10, determination R2 10 | 100 | s 17(1), (6): max(120, 100) − 20 |
| E14 | limit 15 Jun 2027, Day A 14 Jun, Day B 15 Jun | 15 Jul 2027 | (2) gives 16 Jun, inside [14 Jun, 15 Jul] |
| F5 | receipt 1 Mar 2027, complaint presented 15 Jun 2027 (the last day) | award 1016.80 | s 11(3) "before the expiry" of the period ending 15 Jun |
| F6 | presented 16 Jun 2027, no s 11(4) finding | 0 (not considered) | s 11(3) |
| F7 | presented 16 Jun 2027, tribunal satisfied under s 11(4) | 1016.80 | s 11(4) |
| F8 | complaint not well-founded | 0 | s 11(2) "Where ... finds a complaint ... well-founded" |
| F9 | E1 conciliation, presented 15 Jul 2027 | 1016.80 | s 11A(3) |
| F10 | E1 conciliation, presented 16 Jul 2027 | 0 | s 11A(3) |
| G1 | baseline worker, one period (A 100, R1 10, R2 12.5), receipt 1 Mar 2027 | qualifies; 125; produce by 15 Mar 2027; complain by 15 Jun 2027; award 1016.80 | top-level goal |
| G2 | prisoner (prison rules work), civil proceedings, same period, no records request | does not qualify; 0 owed (S16); no dates or award | ss 45(1), 17(1) |

Not testable with the encoding's record shapes (noted in the report): Q39 (not an individual), P7/P8/C9 (when the s 10(9)(b) agreement was made), S15 (payments out of list order — payments carry no date).
