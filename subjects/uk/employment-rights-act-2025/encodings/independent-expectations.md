# Independent expectations: ERA 2025 encoding (SSP, s 108 qualifying period, s 27BH time limits)

Written from BRIEF.md and the Act's text only, before any `.l4` file was opened.

## Readings adopted

- **R1 Month periods ("six months beginning with D").** The period runs from D to the day before the corresponding date six months later. If that month has no corresponding date, the period ends on the last day of that month (brief). Examples: 16 Jan to 15 Jul; 31 Aug 2027 to 29 Feb 2028; 29 Aug 2026 to 28 Feb 2027.
- **R2 s 108(1) "continuously employed for a period of not less than six months ending with the EDT".** The employee qualifies if the EDT is on or after the last day of the six months beginning with the start of continuous employment (brief). The s 64(2) one month works the same way.
- **R3 s 27BH(1)-(7) "beginning with the day after X".** The period starts on X + 1. Under (8), "beginning with the day on which the worker first becomes aware", it starts on X. "Presented before the end of the period" means the last day to present is the period's last day.
- **R4 s 207B(3).** The days from Day A + 1 to Day B are not counted, but only those that fall within the limitation period (brief: "so far as they fall within the period"). The extended limit is the original last day plus the number of such days.
- **R5 s 207B(4).** If the limit after (3) falls within [Day A, one month after Day B] (both ends inclusive), it becomes one month after Day B. "One month after Day B" is the corresponding date in the next month, or that month's last day if it has none (31 Jan 2027 gives 28 Feb 2027).
- **R6 SSP.** The weekly rate is min(£118.75, 0.8 x NWE). There is no lower earnings limit, so any positive NWE gives a rate. The period of entitlement starts on the first day of incapacity (s 153(1) "first"), and a one-day period counts (s 152(2) as amended). With no waiting days (s 155(1) omitted), SSP is payable from the first qualifying day of the period.

### Ambiguities

- **A1 NWE of 0.** The Act gives 80% of 0 = £0. Whether a period of entitlement arises at all is not addressed once the LEL is gone. I expect a rate of 0 (or a REFUSE) and record either as acceptable.
- **A2 s 207B(3) "so far as they fall within the period".** This qualification comes from the brief; s 207B(3) itself does not say it. Scenarios 47 and 49 discriminate between the two readings. I follow the brief.
- **A3 s 207B(4) "one month after Day B".** I use the corresponding-date rule with end-of-month clamping. An alternative reading ("the period of one month beginning with the day after Day B") would end one day earlier.
- **A4 s 64(2) with (3)-(5).** If (3)-(5) applies, no qualifying period is needed in any case.

## Scenarios

### SSP weekly rate (s 157(1) as substituted by s 11(2))

| # | NWE | Expected weekly rate | Act |
|---|-----|------|-----|
| 1 | 148.4375 | 118.75 (both limbs equal) | "the lower of (a) £118.75, and (b) 80%..." |
| 2 | 200 | 118.75 | (a) is lower |
| 3 | 1000 | 118.75 | (a) |
| 4 | 148 | 118.40 | (b) is lower |
| 5 | 148.50 | 118.75 | (a) |
| 6 | 100 | 80 | (b) |
| 7 | 10 (very low, below the old LEL) | 8 | Sch 11 para 2(c) omitted: no LEL |
| 8 | 50 | 40 | (b) |
| 9 | 0 | 0 (A1) | (b) |

### SSP start (ss 152(2), 153(1), 155(1) as amended by s 10)

| # | Facts | Expected | Act |
|---|------|------|-----|
| 10 | Incapacity of one day, Mon 4 Jan 2027, a qualifying day | a period of incapacity arises; SSP is payable for 4 Jan 2027 | s 152(2) "a period of one day which is..."; s 153(1) "first" |
| 11 | Incapacity from 4 Jan 2027 for 5 days | first payable day 4 Jan 2027 (no waiting days) | s 155(1) omitted |
| 12 | Incapacity from 4 Jan 2027 | the period of entitlement begins 4 Jan 2027 | s 153(1) "first day" |

### Unfair dismissal qualifying period (s 108 as amended by s 25)

| # | Start | EDT | Facts | Expected | Act |
|---|-------|-----|-------|----------|-----|
| 13 | 1 Jan 2027 | 30 Jun 2027 | ordinary | qualifies (six months ends 30 Jun) | s 108(1) "six months ending with the EDT" |
| 14 | 1 Jan 2027 | 29 Jun 2027 | ordinary | does not qualify | same |
| 15 | 1 Jan 2027 | 1 Jul 2027 | ordinary | qualifies | same |
| 16 | 31 Aug 2027 | 29 Feb 2028 | ordinary | qualifies (no 31 Feb; last day 29 Feb, a leap year) | R1 |
| 17 | 31 Aug 2027 | 28 Feb 2028 | ordinary | does not qualify | R1 |
| 18 | 29 Aug 2027 | 28 Feb 2028 | ordinary | qualifies (29 Feb 2028 exists, so the period ends 28 Feb) | R1 |
| 19 | 29 Aug 2027 | 27 Feb 2028 | ordinary | does not qualify | R1 |
| 20 | 29 Aug 2026 | 28 Feb 2027 | ordinary | qualifies (no 29 Feb 2027) | R1 |
| 21 | 29 Aug 2026 | 27 Feb 2027 | ordinary | does not qualify | R1 |
| 22 | 1 Mar 2027 | 31 Aug 2027 | ordinary | qualifies | R1 |
| 23 | 1 Mar 2027 | 30 Aug 2027 | ordinary | does not qualify | R1 |
| 24 | 1 Jan 2027 | 31 Jan 2027 | s 64(2) | qualifies (one month) | s 108(2) "one month" |
| 25 | 1 Jan 2027 | 30 Jan 2027 | s 64(2) | does not qualify | s 108(2) |
| 26 | 31 Jan 2027 | 28 Feb 2027 | s 64(2) | qualifies | R1 |
| 27 | 31 Jan 2027 | 27 Feb 2027 | s 64(2) | does not qualify | R1 |
| 28 | 1 Jan 2027 | 2 Jan 2027 | s 108(3) applies | qualifies (no period) | s 108(3) "Subsection (1) does not apply" |
| 29 | 1 Jan 2027 | 2 Jan 2027 | s 108(4) political opinions | qualifies | s 108(4) |
| 30 | 1 Jan 2027 | 2 Jan 2027 | s 108(5) reserve forces | qualifies | s 108(5) |
| 31 | 1 Jan 2027 | 1 Jan 2027 | ordinary | does not qualify | s 108(1) |

### s 27BH last day, no conciliation

| # | Subsection | Trigger day X | Start | Expected last day | Act |
|---|-----|------|------|------|-----|
| 32 | (1) | 15 Jan 2027 | 16 Jan 2027 | 15 Jul 2027 | "six months beginning with the day after the last day of the offer period" |
| 33 | (2) | 15 Jan 2027 | 16 Jan 2027 | 15 Jul 2027 | "...after the day when the offer ... is made" |
| 34 | (3) (27BG(3)) | 31 Jan 2027 | 1 Feb 2027 | 31 Jul 2027 | (3) |
| 35 | (3) (27BG(4)) | 30 Jun 2027 | 1 Jul 2027 | 31 Dec 2027 | (3) |
| 36 | (4) | 30 Aug 2027 | 31 Aug 2027 | 29 Feb 2028 (no 31 Feb) | (4) |
| 37 | (5) | 29 Aug 2027 | 30 Aug 2027 | 29 Feb 2028 (no 30 Feb) | (5) |
| 38 | (6) | 28 Aug 2027 | 29 Aug 2027 | 28 Feb 2028 (29 Feb 2028 exists) | (6) |
| 39 | (7) | 31 Aug 2027 | 1 Sep 2027 | 29 Feb 2028 | (7) |
| 40 | (6) | 28 Aug 2026 | 29 Aug 2026 | 28 Feb 2027 (no 29 Feb 2027) | (6) |
| 41 | (8) | 15 Jan 2027 | 15 Jan 2027 | 14 Jul 2027 | (8) "beginning with the day on which the worker first becomes aware" |
| 42 | (8) | 31 Aug 2027 | 31 Aug 2027 | 29 Feb 2028 | (8), R1 |
| 43 | (8) | 1 Sep 2027 | 1 Sep 2027 | 29 Feb 2028 | (8) |
| 44 | (7) | 31 Dec 2026 | 1 Jan 2027 | 30 Jun 2027 | (7) |

### s 27BH with s 207B (s 27BH(10)); period 16 Jan to 15 Jul 2027 unless stated (s 27BH(2), X = 15 Jan 2027)

| # | Day A | Day B | Days not counted (R4) | After (3) | (4) window | Expected | Act |
|---|-----|-----|-----|-----|-----|-----|-----|
| 45 | 1 Mar 2027 | 31 Mar 2027 | 30 | 14 Aug 2027 | 1 Mar-30 Apr | 14 Aug 2027 | 207B(3) |
| 46 | 1 Jul 2027 | 10 Jul 2027 | 9 | 24 Jul 2027 | 1 Jul-10 Aug | 10 Aug 2027 | 207B(4) |
| 47 | 10 Jan 2027 | 25 Jan 2027 (overlapping the start) | 10 (16-25 Jan) | 25 Jul 2027 | 10 Jan-25 Feb | 25 Jul 2027 (A2: 30 Jul if all 15 days counted) | 207B(3), R4 |
| 48 | 1 Jan 2027 | 10 Jan 2027 (before the start) | 0 | 15 Jul 2027 | 1 Jan-10 Feb | 15 Jul 2027 | R4 |
| 49 | 10 Jul 2027 | 20 Jul 2027 (overlapping the end) | 5 (11-15 Jul) | 20 Jul 2027 | 10 Jul-20 Aug | 20 Aug 2027 | 207B(4) |
| 50 | 15 Jul 2027 | 20 Jul 2027 (A = last day) | 0 | 15 Jul 2027 = Day A, the lower window boundary | 15 Jul-20 Aug | 20 Aug 2027 | 207B(4) "beginning with Day A" |
| 51 | 20 Jul 2027 | 30 Jul 2027 (after the period) | 0 | 15 Jul 2027 | 20 Jul-30 Aug, not reached | 15 Jul 2027 | 207B(4) not engaged |
| 52 | 14 Jun 2027 | 20 Jun 2027 | 6 | 21 Jul 2027 | 14 Jun-20 Jul, outside by 1 day | 21 Jul 2027 | 207B(4) upper boundary |
| 53 | 15 Jun 2027 | 20 Jun 2027 | 5 | 20 Jul 2027 = upper boundary | 15 Jun-20 Jul | 20 Jul 2027 | 207B(4) |
| 54 | 4 Jul 2027 | 5 Jul 2027 | 1 | 16 Jul 2027 | 4 Jul-5 Aug | 5 Aug 2027 | 207B(4) |
| 55 | s 27BH(1), X = 30 Aug 2027 (period 31 Aug 2027-29 Feb 2028); A 1 Feb 2028, B 10 Feb 2028 | | 9 | 9 Mar 2028 | 1 Feb-10 Mar 2028 | 10 Mar 2028 | 207B(3)-(4), February 2028 |
| 56 | same period; A 25 Feb 2028, B 31 Mar 2028 | | 4 (26-29 Feb) | 4 Mar 2028 | 25 Feb-30 Apr 2028 (no 31 Apr) | 30 Apr 2028 | R5 |
| 57 | s 27BH(2), X = 15 Aug 2026 (period 16 Aug 2026-15 Feb 2027); A 20 Jan 2027, B 31 Jan 2027 | | 11 | 26 Feb 2027 | 20 Jan-28 Feb 2027 | 28 Feb 2027 | R5 (no 31 Feb) |
| 58 | s 27BH(8), X = 15 Jan 2027 (period 15 Jan-14 Jul 2027); A 1 Mar 2027, B 31 Mar 2027 | | 30 | 13 Aug 2027 | | 13 Aug 2027 | 27BH(10) applies to (8) |
