# Independent expectations: Communications Act 2003 (UK)

Written from BRIEF.md and the source text only (`../registers/source-bundle/ukpga-2003-21.txt`), before any `.l4` file was opened. Amounts are in pounds. Dates are day month year.

Date conventions used (from the brief, which I read the same way as the Act except where noted):

- s 127(5): last day = day before the corresponding date, or the last day of the month where there is no corresponding date. Both (a) and (b) must be met.
- s 128(3): urgent: period end >= notification day + 7; otherwise: period end >= corresponding date one month after the notification day (last day of month where none).
- ss 129(1)(c), 130(1)(c): Ofcom may act only on a day after the last day of the period.
- s 365A(2): age measured on the last day of the month of issue; a 29 February birthday is attained on 28 February in a common year.
- s 366(4): entry allowed up to and including the corresponding date one month after grant (last day of month where none).

## Goal 1: ending a contract early (ss 124U, 124V, 51(8)-(9))

| # | Facts | Expected | Act |
|---|---|---|---|
| C1 | Consumer, right to terminate early, not M2M, keeps handset; remaining fees 240; agreed equipment value 600; contract 24 months, 12 unexpired | s 124U applies; max compensation 240 (fees lesser than 600 x 12/24 = 300) | s 124U(2) "whichever is the lesser of ... (a) the remaining part of any fee ... (b) a proportion of the value of the terminal equipment ... corresponding to the proportion of the agreed contract period that remains unexpired" |
| C2 | As C1 but remaining fees 400 | 300 (equipment proportion lesser) | s 124U(2)(b) |
| C3 | As C1 but remaining fees 300 | 300 (both equal) | s 124U(2) |
| C4 | Value 500, 24 months, 5 unexpired, fees 200 | 625/6 (= 104.1666..., i.e. 500 x 5/24) | s 124U(2)(b) |
| C5 | As C1 but end-user does not keep equipment | 0: nothing is due | s 124U(1)(a) "no compensation is to be due by the end-user, except compensation for any retained terminal equipment" |
| C6 | No right to terminate early | s 124U does not apply | s 124U(1) "Where an end-user has ... the right to terminate" |
| C7 | M2M service, small business (<=10 workers), right to terminate | applies | s 124U(3) "unless the end-user is a qualifying end-user" |
| C8 | M2M service, large business, right to terminate | does not apply | s 124U(3) |
| C9 | Not M2M, large business, right to terminate | applies (s 124U(1) covers any end-user) | s 124U(1) "an end-user" |
| C10 | M2M, consumer | applies | s 51(9) para (a) is a qualifying end-user |
| C11 | Bundle, consumer, has purported to waive | rights extend to all elements (waiver only counts for paras (b)/(c)) | s 124U(4)(a) "falls within paragraph (b) or (c)" and (b) "has waived" |
| C12 | Bundle, microbusiness, waived | do not extend | s 124U(4)(a)+(b) |
| C13 | Bundle, microbusiness, not waived | extend | s 124U(4)(b) |
| C14 | Bundle, small not-for-profit, waived | do not extend | s 124U(4)(a) para (c) |
| C15 | Not a bundled contract | s 124U(4) gives no extension (false) | s 124U(4) "Where the contract ... is, or is included in, a bundled contract" |
| C16 | s 124V: consumer, bundle, right to terminate one element for lack of conformity | may terminate all elements | s 124V(1)-(2) |
| C17 | s 124V: microbusiness, same facts | no s 124V right | s 124V(1)(a) "an individual, acting for purposes other than those of a business" |
| C18 | s 124V: consumer, bundle, no element non-conforming | no | s 124V(1)(b) |
| C19 | s 124V: consumer, not a bundle | no | s 124V(1)(a) "bundled contract" |

## Goal 2: TV licensing (ss 363, 365, 365A, 366, 368)

| # | Facts | Expected | Act |
|---|---|---|---|
| T1 | Uses receiver to watch live TV, no licence | offence | s 363(1)-(2) |
| T2 | Same, licensed | no offence | s 363(1) "unless ... authorised by a licence" |
| T3 | Uses receiver only for BBC on-demand programmes, no licence | offence | s 368(3)(b) |
| T4 | Uses device only for non-BBC on-demand, not live TV; no licence | no offence (not "using" a receiver) | s 368(3) |
| T5 | Dealer installs receiver on delivery, solely for that purpose, no licence | no offence | s 363(5)(a) |
| T6 | Dealer demonstrating/testing/repairing, solely | no offence | s 363(5)(b) |
| T7 | Exempted by s 363(6) regulations | no offence | s 363(6) |
| T8 | Installs receiver (not yet used), no licence | offence: installation alone contravenes | s 363(1) "must not be installed or used" |
| T9 | Possesses receiver intending to use it unlicensed | offence | s 363(3)(a) |
| T10 | Specified age 65; born 15 Mar 1961; issued 1 Mar 2026 | meets (65 on 15 Mar 2026, before 31 Mar) | s 365A(2) "at or before the end of the month in which the licence is issued" |
| T11 | Born 15 Mar 1961; issued 28 Feb 2026 | does not meet (64 on 28 Feb 2026) | same |
| T12 | Born 31 Mar 1961; issued 31 Mar 2026 | meets (birthday on the month end) | same |
| T13 | Born 1 Apr 1961; issued 31 Mar 2026 | does not meet | same |
| T14 | Born 29 Feb 1960; issued 10 Feb 2025 (common year) | meets (65 attained 28 Feb 2025) | same, brief convention |
| T15 | Born 29 Feb 1960; issued 10 Jan 2025 | does not meet | same |
| T16 | Born 29 Feb 1960; issued 10 Feb 2024 (leap) | does not meet (64 on 29 Feb 2024) | same |
| T17 | Specified age 75; born 10 Jun 1950; issued 5 Jun 2025 | meets | same |
| T18 | Specified age 75; born 1 Jul 1950; issued 30 Jun 2025 | does not meet | same |
| T19 | Specified age 64 / 65 / 75 | 64 not allowed; 65 and 75 allowed | s 365A(2) "which must be 65 or higher" |
| T20 | Warrant granted 15 Mar 2026 | last day 15 Apr 2026: entry 14 Apr yes, 15 Apr yes, 16 Apr no | s 366(4) "not ... at any time more than one month after the day on which the warrant was granted" |
| T21 | Granted 31 Jan 2026 | last day 28 Feb 2026; entry 1 Mar no | s 366(4) |
| T22 | Granted 31 Jan 2024 | last day 29 Feb 2024 | s 366(4) |
| T23 | Granted 30 Dec 2025 | last day 30 Jan 2026 | s 366(4) |
| T24 | Entry on the grant day itself | allowed | s 366(4) |

## Goal 3: misuse of a network (ss 127-130)

| # | Facts | Expected | Act |
|---|---|---|---|
| M1 | Sends grossly offensive message over public network | offence | s 127(1)(a) |
| M2 | Causes an indecent message to be sent | offence | s 127(1)(b) |
| M3 | Grossly offensive, but in the course of providing a programme service | no offence | s 127(4) |
| M4 | Sends message known false, to cause annoyance | offence | s 127(2)(a) |
| M5 | Sends message known false, no such purpose (and not grossly offensive etc.) | no offence | s 127(2) "for the purpose of causing annoyance ..." |
| M6 | Persistently uses network to cause needless anxiety | offence | s 127(2)(c) |
| M7 | Message merely offensive (not grossly), no purpose | no offence | s 127(1)(a) |
| M8 | False message for annoyance but in a programme service | no offence | s 127(4) |
| M9 | Offence 10 Mar 2023; evidence 1 Dec 2025; laid 9 Mar 2026 | in time (3-yr last day 9 Mar 2026; 6-month last day 31 May 2026) | s 127(5)(a) "before the end of the period of 3 years beginning with the day on which the offence was committed" |
| M10 | Same, laid 10 Mar 2026 | out of time: the 3-year limit binds | s 127(5)(a) |
| M11 | Offence 1 Jan 2025; evidence 15 Mar 2025; laid 13 / 14 / 15 Sep 2025 | in / in / out: 6-month last day 14 Sep 2025 binds | s 127(5)(b) "6 months beginning with the day on which evidence comes to the knowledge" |
| M12 | Offence 1 Jun 2025; evidence 31 Aug 2025; laid 28 Feb 2026 / 1 Mar 2026 | in / out (no 31 Feb: last day 28 Feb 2026) | s 127(5)(b) |
| M13 | Offence 1 Jun 2023; evidence 31 Aug 2023; laid 29 Feb 2024 / 1 Mar 2024 | in / out (leap year: last day 29 Feb 2024) | s 127(5)(b) |
| M14 | Offence 29 Feb 2024; evidence 1 Dec 2026; laid 28 Feb 2027 / 1 Mar 2027 | in / out (3-yr last day 28 Feb 2027) | s 127(5)(a) |
| M15 | Offence 1 Jan 2025; evidence 28 Aug 2025; laid 27 Feb / 28 Feb 2026 | in / out (corresponding date 28 Feb exists; last day 27 Feb) | s 127(5)(b) |
| M16 | Urgent (continuing and must stop asap); notified 1 Mar 2026 | minimum end 8 Mar 2026; period to 7 Mar too short; to 8 Mar long enough | s 128(3)(a) "seven days" |
| M17 | Urgent; notified 25 Dec 2025 | minimum end 1 Jan 2026 | s 128(3)(a) |
| M18 | Continuing but harm does not need it stopped asap | not urgent: one month applies | s 128(4)(a)+(b) |
| M19 | Not urgent; notified 15 Jan 2026 | min end 15 Feb 2026; 14 Feb too short | s 128(3)(b) "one month" |
| M20 | Not urgent; notified 31 Jan 2026 | min end 28 Feb 2026; 27 Feb too short; 28 Feb ok | s 128(3)(b) |
| M21 | Not urgent; notified 31 Jan 2024 | min end 29 Feb 2024 | s 128(3)(b) |
| M22 | Notified 15 Jan 2026, not urgent, period given to 15 Feb 2026; Ofcom acts 15 Feb / 16 Feb | may not / may | ss 129(1)(c), 130(1)(c) "has expired" |
| M23 | Urgent, notified 1 Mar 2026, period given to 7 Mar 2026 (too short), Ofcom acts 20 Mar 2026 | may NOT act (my reading: a period shorter than s 128(3) is not a valid opportunity under ss 129(1)(b)/130(1)(b); the brief is silent) | s 128(3) "must not be less than", s 130(1)(b) |
| M24 | Penalty 2,000,000 / 1,999,999 / 2,000,001 | within / within / not within | s 130(4) "not exceeding £2,000,000" |
