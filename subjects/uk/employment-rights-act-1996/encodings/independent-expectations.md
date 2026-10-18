# Independent expectations: Employment Rights Act 1996 (text at 29 July 2026)

Written from BRIEF.md and the source text only, before any `.l4` file was opened.
Dates worked by hand on a calendar (spot-checked with a date library for day additions only).

## Readings taken

R1. "A period of N months/years beginning with X" ends on the day before the corresponding date N months/years later; if the month has no corresponding date, on the last day of that month (brief). So 29/30/31 Jan + 1 month all end 28 Feb (non-leap), 28 Jan + 1 month ends 27 Feb.

R2. "Continuously employed for a period of not less than N ending with E": E is on or after the last day of the N-period beginning with the start day (brief). The same test counts complete years for s 86 and for ss 119/162 ("years of employment").

R3. s 86 lengths are judged on the period of continuous employment ending with the day notice is given (brief; s 211(1)(b)). Under one month s 86 requires no notice: I expect 0 weeks (the Act answers: nothing is required), not a refusal.

R4. Notice of N weeks given on d expires at the end of d + 7N (brief).

R5. s 97(2): employer termination; later of the s 97(1) EDT and (material date + s 86 notice) is the EDT for ss 108(1), 119(1), 227(3) only. Not for s 111. s 97(4): same for termination by the employee, unless the material date falls in an employer's notice period. s 145(5): employer termination only (no equivalent of s 97(4)); applies for ss 155, 162(1), 227(3) and NOT s 164.

R6. **Age bands (ambiguous).** "A year of employment in which the employee was not below the age of forty-one" — I read this as: the employee was 41 or over throughout that year, i.e. had attained 41 on or before the first day of the year (years reckoned backwards from the EDT/relevant date). A birthday falling on the first day of the year counts; one day later does not. The alternative reading ("at any time in the year", i.e. age at the end of the year) would give the higher rate for the year in which the birthday falls. The brief's edge ("birthdays exactly on and one day after the start of a year of employment") matches my reading. Same for 22. A person attains an age on the anniversary of birth (no 29 Feb birthdays used).

R7. Year k reckoned backwards (k = 1 latest) runs from the day after (E minus k years) to (E minus (k-1) years). Cases straddling 29 Feb in the reckoning-back are avoided except where both readings agree.

R8. s 207B(3)-(4): limit L; if Day A <= L, L' = L + (Day B - Day A) days; if L' falls in [Day A, Day B + 1 month] (corresponding date; if none, last day of that month - my reading of R1 applied to "one month after"), it becomes Day B + 1 month. If Day A > L, nothing changes. If Day A = L, (4) catches it either way.

R9. s 164(5) applies s 207B only to s 164(1)(c) (reference to a tribunal) and s 164(2). A written claim to the employer (1)(b) or a s 111 complaint (1)(d) is not extended by s 164(5).

R10. Basic award: s 119 sum, then s 120 minimum (before s 122), then s 122(4) deduction of any redundancy payment, floor 0. s 121 replaces the amount with two weeks' (capped) pay.

R11. s 227 cap £751 applies to every week's pay in the basic award and the redundancy payment, including s 121's two weeks.

## Goal 1: minimum notice (s 86)

| # | Start of continuous employment | Notice given | Employer weeks | Employee weeks | Earliest employer expiry | Act |
|---|---|---|---|---|---|---|
| N1 | 1 Mar 2026 | 30 Mar 2026 | 0 | 0 | (none; = notice day) | s 86(1) "continuously employed for one month or more" — one month beginning 1 Mar ends 31 Mar |
| N2 | 1 Mar 2026 | 31 Mar 2026 | 1 | 1 | 7 Apr 2026 | s 86(1)(a), (2) |
| N3 | 31 Jan 2026 | 27 Feb 2026 | 0 | 0 | - | one month beginning 31 Jan ends 28 Feb (no 31 Feb) |
| N4 | 31 Jan 2026 | 28 Feb 2026 | 1 | 1 | 7 Mar 2026 | s 86(1)(a) |
| N5 | 1 Jan 2024 | 30 Dec 2025 | 1 | 1 | 6 Jan 2026 | (a) "less than two years" |
| N6 | 1 Jan 2024 | 31 Dec 2025 | 2 | 1 | 14 Jan 2026 | (b) "two years or more"; employee still 1 (s 86(2)) |
| N7 | 1 Feb 2023 | 31 Dec 2025 | 2 | 1 | 14 Jan 2026 | (b) "one week for each year" — 2 complete years |
| N8 | 1 Jan 2014 | 30 Dec 2025 | 11 | 1 | 17 Mar 2026 | (b) 11 years |
| N9 | 1 Jan 2014 | 31 Dec 2025 | 12 | 1 | 25 Mar 2026 | (c) "twelve years or more" |
| N10 | 1 Jan 2000 | 1 Jun 2026 | 12 | 1 | 24 Aug 2026 | (c) capped at twelve |
| N11 | 29 Feb 2024 | 27 Feb 2026 | 1 | 1 | 6 Mar 2026 | two years beginning 29 Feb 2024 end 28 Feb 2026 |
| N12 | 29 Feb 2024 | 28 Feb 2026 | 2 | 1 | 14 Mar 2026 | (b) |
| N13 | 29 Feb 2024 | 27 Mar 2024 | 0 | 0 | - | one month beginning 29 Feb 2024 ends 28 Mar 2024 |
| N14 | 29 Feb 2024 | 28 Mar 2024 | 1 | 1 | 4 Apr 2024 | (a) |
| N15 | 1 Jan 2027 | 25 Feb 2028 | 1 | 1 | 3 Mar 2028 | expiry crosses 29 Feb 2028 |
| N16 | 15 May 2019 | 13 May 2026 | 6 | 1 | 24 Jun 2026 | 7th year ends 14 May 2026 |
| N17 | 15 May 2019 | 14 May 2026 | 7 | 1 | 2 Jul 2026 | (b) |

## Goal 2a: qualifying period (s 108, with s 97(2)/(4))

Unless stated, the dismissal is by the employer with notice at least as long as s 86 requires (so s 97(2) adds nothing), no s 108(2)-(5) reason.

| # | Start | Facts | Expected qualifies? | Act |
|---|---|---|---|---|
| Q1 | 1 Jan 2024 | EDT 31 Dec 2025 (notice given 1 Dec 2025, expiring 31 Dec) | yes | s 108(1): two years beginning 1 Jan 2024 end 31 Dec 2025 |
| Q2 | 1 Jan 2024 | EDT 30 Dec 2025 (notice given 1 Dec 2025) | no | s 86 notice on 1 Dec = 1 week, 8 Dec < 30 Dec so s 97(2) adds nothing |
| Q3 | 29 Feb 2024 | EDT 28 Feb 2026 (notice given 1 Feb 2026) | yes | two years end 28 Feb 2026 (no 29 Feb 2026) |
| Q4 | 29 Feb 2024 | EDT 27 Feb 2026 (notice given 1 Feb 2026) | no | |
| Q5 | 31 Aug 2024 | EDT 30 Aug 2026 (notice given 1 Aug 2026) | yes | corresponding date 31 Aug 2026 exists; two years end 30 Aug 2026 |
| Q6 | 10 Jan 2024 | employer dismisses without notice, 2 Jan 2026 | yes | s 97(2): 1 week from 2 Jan expires 9 Jan 2026 = last day of two years |
| Q7 | 10 Jan 2024 | employer dismisses without notice, 1 Jan 2026 | no | 97(2) date 8 Jan 2026 < 9 Jan |
| Q8 | 10 Jan 2024 | employer gives 3 days' notice on 4 Jan 2026, expiring 7 Jan 2026 | yes | s 97(2)/(3)(a): 1 week from 4 Jan = 11 Jan >= 9 Jan |
| Q9 | 8 Jan 2024 | employee terminates without notice for employer's conduct, 2 Jan 2026 (no employer notice running) | yes | s 97(4): 1 week from 2 Jan = 9 Jan >= 7 Jan 2026 |
| Q10 | 8 Jan 2024 | same, but 2 Jan 2026 falls during a period of notice given by the employer (employer notice expiring 31 Jan 2026 hypothetically irrelevant; EDT 2 Jan) | no | s 97(4)(b) not met; EDT stays 2 Jan < 7 Jan |
| Q11 | 1 Mar 2026 | s 64(2) dismissal, EDT 31 Mar 2026 | yes | s 108(2) "one month" |
| Q12 | 1 Mar 2026 | s 64(2) dismissal without notice, 30 Mar 2026 | no | 1 month ends 31 Mar; s 86 requires nothing under one month so s 97(2) adds nothing |
| Q13 | 31 Jan 2026 | s 64(2), EDT 28 Feb 2026 | yes | one month ends 28 Feb |
| Q14 | 31 Jan 2026 | s 64(2), without notice 27 Feb 2026 | no | |
| Q15 | 1 Jan 2026 | s 108(3)(c) (s 100 health and safety) reason, EDT 31 Mar 2026 | yes | s 108(3) "Subsection (1) does not apply" |
| Q16 | 1 Jan 2026 | political opinions, EDT 31 Mar 2026 | yes | s 108(4) |
| Q17 | 1 Jan 2026 | reserve forces membership, EDT 31 Mar 2026 | yes | s 108(5) |
| Q18 | 1 Jan 2026 | s 104F blacklist, EDT 31 Mar 2026 | yes | s 108(3)(gl) |
| Q19 | 1 Jan 2026 | no special reason, EDT 31 Mar 2026 | no | s 108(1) |

## Goal 2b: last day to present a complaint (s 111(2)(a), (2A), s 207B)

The period runs from the s 97(1) EDT (s 97(2) does not apply to s 111).

| # | EDT | Day A / Day B | Last day | Working |
|---|---|---|---|---|
| T1 | 15 Jan 2026 | none | 14 Apr 2026 | corresponding 15 Apr, day before |
| T2 | 30 Nov 2025 | none | 28 Feb 2026 | no 30 Feb 2026 -> last day of Feb |
| T3 | 29 Nov 2025 | none | 28 Feb 2026 | no 29 Feb 2026 |
| T4 | 28 Nov 2025 | none | 27 Feb 2026 | |
| T5 | 30 Nov 2027 | none | 29 Feb 2028 | leap year, no 30 Feb |
| T6 | 29 Nov 2027 | none | 28 Feb 2028 | 29 Feb 2028 exists |
| T7 | 31 Mar 2026 | none | 30 Jun 2026 | no 31 Jun |
| T8 | 31 Dec 2025 | none | 30 Mar 2026 | |
| T9 | 15 Jan 2026 | A 1 Feb, B 15 Feb 2026 | 28 Apr 2026 | (3): 14 days (2-15 Feb) added; 28 Apr outside [1 Feb, 15 Mar] |
| T10 | 15 Jan 2026 | A 1 Apr, B 10 Apr 2026 | 10 May 2026 | (3): +9 -> 23 Apr; in [1 Apr, 10 May] -> (4) |
| T11 | 15 Jan 2026 | A 13 Mar, B 20 Mar 2026 | 21 Apr 2026 | +7 -> 21 Apr; window ends 20 Apr |
| T12 | 15 Jan 2026 | A 14 Mar, B 20 Mar 2026 | 20 Apr 2026 | +6 -> 20 Apr = window end |
| T13 | 15 Jan 2026 | A 15 Mar, B 20 Mar 2026 | 20 Apr 2026 | +5 -> 19 Apr; (4) -> 20 Apr |
| T14 | 15 Jan 2026 | A 13 Apr, B 20 Apr 2026 | 20 May 2026 | +7 -> 21 Apr; in window -> 20 May |
| T15 | 15 Jan 2026 | A 14 Apr, B 20 Apr 2026 | 20 May 2026 | Day A on the limit; (4) |
| T16 | 15 Jan 2026 | A 15 Apr, B 20 Apr 2026 | 14 Apr 2026 | Day A after the limit: s 207B cannot revive it |
| T17 | 15 Jan 2026 | A 14 Apr, B 14 Apr 2026 | 14 May 2026 | nothing excluded; 14 Apr in [14 Apr, 14 May] |
| T18 | 15 Jan 2026 | A 16 Jan, B 15 Mar 2026 | 11 Jun 2026 | +58 days; outside window ending 15 Apr |
| T19 | 30 Nov 2025 | A 20 Feb, B 27 Feb 2026 | 27 Mar 2026 | 28 Feb +7 = 7 Mar; window ends 27 Mar |
| T20 | 1 Nov 2025 | A 20 Jan, B 31 Jan 2026 | 28 Feb 2026 | limit 31 Jan; +11 -> 11 Feb; one month after 31 Jan has no corresponding date -> 28 Feb (reading R8; ambiguous) |
| T21 | EDT for s 111 is the actual date: employer summarily dismisses 2 Jan 2026 (S 10 Jan 2024) | none | 1 Apr 2026 | s 97(2) is "for the purposes of sections 108(1), 119(1) and 227(3)" only |

## Goal 2c: basic award (ss 119-122, 227)

All are unfair dismissals with EDT reached by adequate employer notice unless stated.

| # | Start | EDT | DOB | Pay | Other | Expected | Working |
|---|---|---|---|---|---|---|---|
| B1 | 1 Jan 2016 | 31 Dec 2025 | 15 Jun 1980 | 500 | | 6000 | 10 years; years starting 1 Jan 2022-2025 at 41+ (4 x 1.5) + 6 x 1 = 12 wks. (The "age at end of year" reading would give 12.5 = 6250.) |
| B2 | same | same | same | 1000 | | 9012 | s 227 cap 751 x 12 |
| B3 | 1 Mar 2020 | 28 Feb 2026 | 1 Mar 1984 | 400 | | 2600 | 6 years; turns 41 on 1 Mar 2025 = first day of latest year -> 1.5 + 5 = 6.5 wks |
| B4 | 1 Mar 2020 | 28 Feb 2026 | 2 Mar 1984 | 400 | | 2400 | turns 41 one day after start of latest year -> 6 x 1 |
| B5 | 1 Mar 2020 | 28 Feb 2026 | 1 Mar 2003 | 400 | | 1400 | turns 22 on first day of latest year -> 1 + 5 x 0.5 = 3.5 |
| B6 | 1 Mar 2020 | 28 Feb 2026 | 2 Mar 2003 | 400 | | 1200 | 6 x 0.5 |
| B7 | 1 Jan 2000 | 31 Dec 2025 | 1 Jan 1960 | 900 | | 22530 | 26 years, only last 20 count (s 119(3)), all at 41+: 30 x 751 |
| B8 | 1 Jan 2000 | 31 Dec 2025 | 1 Jan 1980 | 600 | | 13500 | last 20 years start 1 Jan 2006-2025; 41+ at start for 2021-2025 (5 x 1.5) + 15 x 1 = 22.5 |
| B9 | 1 Sep 2020 | 31 Aug 2025 | 1 Sep 2003 | 300 | | 750 | 5 years, ages at start 17-21 -> 2.5 wks |
| B10 | 1 Jan 2020 | 30 Jun 2025 | 1 Jan 1990 | 500 | | 2500 | 5 complete years (part year ignored), ages 30-34 |
| B11 | 3 Mar 2014 | employer dismisses without notice 28 Feb 2026 | 1 Jan 1970 | 500 | | 9000 | s 97(2): 11 years at 28 Feb -> 11 wks -> 16 May 2026; 12 years, all 41+ -> 18 wks |
| B12 | 1 Jan 2025 | 30 Jun 2025 | 1 Jan 1980 | 500 | s 100 reason (s 120(1)) | 9157 | 0 years -> minimum |
| B13 | as B7 | | | 900 | s 100 reason | 22530 | minimum not reached; s 120 is a floor |
| B14 | 1 Jan 2025 | 30 Jun 2025 | 1 Jan 1980 | 500 | s 104F (s 120(1C)) | 5000 | |
| B15 | as B1 | | | 500 | redundancy reason, s 141 unreasonable refusal (s 121(b)) | 1000 | two weeks' pay |
| B16 | as B1 | | | 800 | s 121(b) | 1502 | two weeks capped |
| B17 | as B1 | | | 500 | redundancy payment 6000 paid (s 122(4)) | 0 | 6000 - 6000 |
| B18 | as B1 | | | 500 | redundancy payment 2000 paid | 4000 | |
| B19 | as B1 | | | 500 | enhanced redundancy payment 8000 paid | 0 | cannot go below 0 |
| B20 | as B12 (s 100 reason) | | | 500 | payment 1000 by employer on ground of redundancy | 8157 | minimum is "before any reduction under section 122" |

## Goal 3: redundancy payment (ss 135-164)

Unless stated: employer dismisses with adequate notice; reason redundancy (or presumed under s 163(2)); no s 140/141 exclusion; claim made within six months; s 145(2) relevant date = EDT.

| # | Facts | Entitled | Amount | Act |
|---|---|---|---|---|
| P1 | as B1 (S 1 Jan 2016, rd 31 Dec 2025, DOB 15 Jun 1980, pay 500) | yes | 6000 | ss 135(1)(a), 155, 162 |
| P2 | as B2, pay 1000 | yes | 9012 | s 227(1)(c) |
| P3 | as B7 (26 years, pay 900) | yes | 22530 | s 162(3) |
| P4 | as B3 / B4 birthday edges | yes | 2600 / 2400 | s 162(2) |
| P5 | as B5 / B6 | yes | 1400 / 1200 | s 162(2) |
| P6 | dismissed, reason not shown to be other than redundancy | yes | as P1 | s 163(2) presumption |
| P7 | dismissed, employer proves reason was conduct (not redundancy) | no | 0 | s 163(2) "unless the contrary is proved" |
| P8 | employee resigns with notice, not entitled to terminate without notice | no | | s 136(1): not dismissed |
| P9 | constructive dismissal (s 136(1)(c)), S 1 Jan 2016, rd 31 Dec 2025 | yes | 6000 | s 136(1)(c) |
| P10 | limited-term contract expires, S 1 Jan 2016, rd 31 Dec 2025 | yes | 6000 | s 136(1)(b) |
| P11 | S 8 Jan 2024, constructive dismissal without notice 2 Jan 2026 | no | | s 155 two years end 7 Jan 2026; s 145(5) only applies where "terminated by the employer" |
| P12 | S 10 Jan 2024, employer dismisses for redundancy without notice 2 Jan 2026, DOB 1 Jan 1990, pay 500 | yes | 1000 | s 145(5): rd 9 Jan 2026 -> 2 years at ages 34, 35 |
| P13 | S 10 Jan 2024, employer dismisses without notice 1 Jan 2026 | no | | s 145(5) rd 8 Jan |
| P14 | S 3 Mar 2014, employer dismisses for redundancy without notice 28 Feb 2026, DOB 1 Jan 1970, pay 500 | yes | 9000 | s 145(5) -> 16 May 2026, 12 years x 1.5 |
| P15 | s 140(1) summary dismissal for conduct | no | | s 140(1)(a) |
| P16 | s 141(2) unreasonable refusal of suitable offer | no | | s 141(2) |
| P17 | S 1 Jan 2024, rd 30 Dec 2025 (notice given 1 Dec) | no | | s 155 |
| P18 | S 1 Jan 2024, rd 31 Dec 2025, DOB 1 Jan 1990, pay 500 | yes | 1000 | 2 years |
| P19 | rd 15 Mar 2026; written claim to employer 14 Sep 2026 | yes | | s 164(1)(b): six months end 14 Sep 2026 |
| P20 | rd 15 Mar 2026; written claim 15 Sep 2026; tribunal finds just and equitable | yes | | s 164(2): second period 15 Sep 2026 - 14 Mar 2027 |
| P21 | rd 15 Mar 2026; written claim 15 Sep 2026; not just and equitable | no | | s 164(1) |
| P22 | rd 15 Mar 2026; written claim 15 Mar 2027; just and equitable | no | | outside both periods |
| P23 | rd 31 Aug 2026; written claim 28 Feb 2027 | yes | | no 31 Feb -> six months end 28 Feb 2027 |
| P24 | rd 31 Aug 2026; written claim 1 Mar 2027, not J&E | no | | |
| P25 | rd 30 Aug 2027; claim 29 Feb 2028 | yes | | no 30 Feb 2028 -> 29 Feb 2028 |
| P26 | rd 29 Aug 2027; claim 29 Feb 2028, not J&E | no | | corresponding 29 Feb 2028 exists -> ends 28 Feb 2028 |
| P27 | rd 15 Mar 2026; tribunal reference 10 Oct 2026; Day A 1 Sep, Day B 10 Sep 2026; not J&E | yes | | s 164(5)/207B: +9 -> 23 Sep, in [1 Sep, 10 Oct] -> 10 Oct |
| P28 | as P27, reference 11 Oct 2026, not J&E | no | | |
| P29 | as P27 but the step is a written claim to the employer on 10 Oct 2026, not J&E | no | | s 164(5) applies s 207B only to (1)(c) and (2) |
| P30 | employer summary (non-conduct) dismissal 2 Jan 2026, S 10 Jan 2024; written claim 5 Jul 2026, not J&E | no | | s 164 runs from s 145(2) date 2 Jan (ends 1 Jul 2026); s 145(5) is not for s 164 |
| P31 | payment agreed and paid within six months | yes | | s 164(1)(a) |

## Points of doubt

- R6 (age at the start vs at any time in the year) is the largest. B1/B3-B6/P4-P5 discriminate.
- R8: one month after a Day B on 31 Jan (T20).
- Whether "notice given" under one month should give 0 or REFUSE (N1, N3, N13). The Act answers it: s 86 imposes nothing.
- s 164(2) with s 207B: whether the second six months start after the extended first period. Not tested.

## Top-level goal (derived from B1/P1, written with the tests)

G1. S 1 Jan 2016, DOB 15 Jun 1980, pay 500, employer notice given 1 Dec 2025 expiring 31 Dec 2025, complaint presented 1 Feb 2026, found unfair, ordinary reason, written redundancy claim 1 Feb 2026: employer notice 9 weeks (9 whole years on 1 Dec 2025), employee 1; EDT 31 Dec 2025; qualifies; last day 30 Mar 2026; basic award 6000; redundancy entitled, 6000; s 164(1) period ends 30 Jun 2026. Same with the complaint presented 31 Mar 2026 and no late allowance: basic award 0 (s 111(2)).

## Probes added AFTER reading the encoding (expected values still from the Act)

These were added once the code showed where its arithmetic could part from the Act. The expected values are worked from the Act, not from the code.

| # | Facts | Expected | Act / working |
|---|---|---|---|
| T22 | EDT 15 Jan 2026; Day A 1 Jan, Day B 20 Jan 2026 (ACAS contacted during notice) | 20 Apr 2026 | s 207B(3): the days 2-20 Jan are "not to be counted"; only 15-20 Jan (6 days) were ever going to be counted in the three months, so 14 Apr + 6 = 20 Apr. (4): window 1 Jan - 20 Feb; 20 Apr outside. Reading point: the alternative (add all B - A = 19 days -> 3 May) counts days before the period began. |
| T23 | EDT 15 Jan 2026; Day A 1 Jan, Day B 10 Jan 2026 (conciliation finished before the EDT) | 14 Apr 2026 | none of 2-10 Jan falls in the three months, so (3) adds nothing; (4) window ends 10 Feb. Same reading point. |
| B21 | S 1 Mar 2024, EDT 28 Feb 2025 (notice given 1 Feb 2025), DOB 1 Mar 1983, pay 400 | 600 | one year of employment, 1 Mar 2024 - 28 Feb 2025 (s 119(1)(b) years "falling within that period"); 41 on 1 Mar 2024, its first day -> 1.5 weeks |
| B22 | S 1 Mar 2020, EDT 28 Feb 2026 (notice 1 Jan 2026), DOB 1 Mar 1979, pay 400 | 3600 | six years, the earliest beginning 1 Mar 2020 (start of employment), the day he turned 41 -> 6 x 1.5 = 9 weeks |
| P32 | as B21 for a redundancy payment | 600 | s 162(1)-(2), same words |
