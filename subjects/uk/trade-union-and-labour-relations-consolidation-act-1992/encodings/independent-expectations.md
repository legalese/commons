# Independent expectations: TULRCA 1992 (UK), three goals

Written from BRIEF.md and the source text only (ss 146-147, 152-156, 161, 188-192, 195A, 238-239, 292A of the revised text in `../registers/source-bundle/ukpga-1992-52.txt`), before any `.l4` file was opened.

Date conventions used (from the brief, which I accept unless noted):

- "three/six months beginning with D": last day = the day before the corresponding date; where the corresponding date does not exist, the last day of that month.
- s 292A(3): the days Day A + 1 .. Day B are not counted; the limit moves later by that many days. **(4)**: if the limit as extended falls in [Day A, Day B + 1 month], it becomes Day B + 1 month (month-end clamp where needed).
- s 161(2): last day = EDT + 7.
- s 188(1A): latest start = first dismissal - 45 (or - 30).
- s 189(4): last day of protected period = first day + days - 1, days at most 180.
- s 190(2): week's pay x days / 7.

## Goal 1: union membership and activities

### Protection (ss 146, 152, 153)

| # | Facts | Expected | Source |
|---|---|---|---|
| P1 | Worker subjected to detriment for sole or main purpose of penalising him for being a member of an independent union | protected | s 146(1)(a) |
| P2 | Detriment to penalise taking part in union activities outside working hours | protected | s 146(1)(b), (2)(a) |
| P3 | Same, activities inside working hours, no arrangement or consent | not protected | s 146(1)(b) "at an appropriate time", (2) |
| P4 | Same, inside working hours with employer's consent | protected | s 146(2)(b) |
| P5 | Detriment to compel him to become a member of a union | protected | s 146(1)(c) |
| P6 | Detriment to enforce a requirement to pay money if not a member | protected | s 146(3) |
| P7 | Employee; the detriment amounts to dismissal; reason membership | s 146 does not apply | s 146(5A) "the worker is an employee; and the detriment ... amounts to dismissal" |
| P8 | Worker who is not an employee; detriment amounts to termination; reason membership | s 146 applies (protected) | s 146(5A)(a) not met |
| P9 | Employee dismissed, principal reason membership | unfair under s 152 | s 152(1)(a) |
| P10 | Dismissed for union activities during working hours without consent | not unfair under s 152 | s 152(1)(b), (2) |
| P11 | Dismissed for refusing to pay sums in lieu of membership | unfair (treated as (1)(c)) | s 152(3)(a) |
| P12 | Dismissed for non-membership | unfair | s 152(1)(c) |
| P13 | Principal reason redundancy; others in similar positions not dismissed; selected for membership | unfair under s 153 | s 153(a), (b) |
| P14 | As P13 but no others in similar positions remain undismissed | not unfair under s 153 | s 153(a) |
| P15 | Unfair under s 152 or s 153 | qualifying period does not apply | s 154 |

### Minimum basic award (s 156(1))

| # | Basic award before reductions | Expected | Source |
|---|---|---|---|
| B1 | £5,000 | £9,157 | "shall be not less than £9,157" |
| B2 | £9,156 | £9,157 | |
| B3 | £9,157 | £9,157 | |
| B4 | £9,158 | £9,158 | |
| B5 | £20,000 | £20,000 | |

### s 147(1)(a) last day, no conciliation

| # | Act (or last of a series) | Expected last day | Note |
|---|---|---|---|
| L1 | 15 Mar 2026 | 14 Jun 2026 | presented 13 Jun / 14 Jun in time; 15 Jun out |
| L2 | 31 Jan 2026 | 30 Apr 2026 | no 31 April |
| L3 | 30 Nov 2025 | 28 Feb 2026 | no 30 February |
| L4 | 30 Nov 2027 | 29 Feb 2028 | leap year, no 30 February |
| L5 | 29 Nov 2027 | 28 Feb 2028 | 29 Feb 2028 exists, day before |
| L6 | 1 Dec 2025 | 28 Feb 2026 | corresponding 1 Mar, day before |
| L7 | Series 1 Feb 2026 .. 10 Mar 2026 | 9 Jun 2026 | "the last of them" |

### s 147 with s 292A (Day A, Day B)

| # | Act; base limit | Day A / Day B | Expected | Working |
|---|---|---|---|---|
| C1 | 15 Mar 2026; 14 Jun 2026 | 1 Apr / 15 Apr 2026 | 28 Jun 2026 | 14 days not counted; 28 Jun after 15 May so (4) does not bite |
| C2 | same | 1 Jun / 10 Jun 2026 | 10 Jul 2026 | 9 days -> 23 Jun; within [1 Jun, 10 Jul] -> 10 Jul |
| C3 | same | 14 Jun / 20 Jun 2026 (Day A on the limit) | 20 Jul 2026 | (3) adds nothing (days after the limit); limit 14 Jun is within [14 Jun, 20 Jul] -> 20 Jul |
| C4 | same | 15 Jun / 20 Jun 2026 (Day A the day after) | 14 Jun 2026 | limit already expired; neither (3) nor (4) applies |
| C5 | same | 13 Jun / 20 Jun 2026 (Day A the day before) | 20 Jul 2026 | (4) |
| C6 | 1 Dec 2027; 29 Feb 2028 | 20 Jan / 31 Jan 2028 | 11 Mar 2028 | 11 days -> 11 Mar; Day B + 1 month = 29 Feb 2028 (no 31 Feb, leap); 11 Mar is after it |
| C7 | 1 Nov 2026; 31 Jan 2027 | 20 Jan / 31 Jan 2027 | 28 Feb 2027 | 11 days -> 11 Feb; Day B + 1 month = 28 Feb 2027; within -> 28 Feb |
| C8 | 1 Mar 2026; 31 May 2026 | 5 Mar / 20 Jun 2026 | **15 Sep 2026** | see below |

C8 is where I may read the Act differently from the brief. s 292A(3): "the period beginning with the day after Day A and ending with Day B is not to be counted." Counting the three months from 1 Mar, the count is still running on 6 Mar, so every day 6 Mar .. 20 Jun (107 days) is skipped: 31 May + 107 = 15 Sep 2026. That is after Day B + 1 month (20 Jul), so (4) does not change it. The brief's words "so far as they fall within the period" could be read as clipping the skipped days to those up to the unextended limit (6 Mar .. 31 May = 87 days), giving 26 Aug 2026. I expect 15 Sep 2026.

## Goal 1: interim relief (s 161)

| # | Facts | Expected | Source |
|---|---|---|---|
| I1 | Relies on s 152(1)(c); EDT 10 Mar 2026; applies 17 Mar 2026 | in time (last day 17 Mar) | s 161(2) |
| I2 | Same; applies 18 Mar 2026 | out of time | |
| I3 | Same; applies 5 Mar 2026 (before EDT) | in time | "(whether before, on or after that date)" |
| I4 | EDT 26 Feb 2028 | last day 4 Mar 2028 | leap year |
| I5 | EDT 26 Feb 2026 | last day 5 Mar 2026 | |
| I6 | Relies on s 152(1)(b); applies 17 Mar, certificate 17 Mar (EDT 10 Mar) | in time | s 161(3) |
| I7 | Same; certificate 18 Mar | not entertained | "before the end of that period" |
| I8 | Same; no certificate | not entertained | |
| I9 | Relies on (1)(a), no certificate | not entertained | |
| I10 | Relies on (1)(ba), certificate on time | in time | |
| I11 | Relies on (1)(bb), offer under s 145A(1)(d), no certificate | in time | carve-out in s 161(3) |
| I12 | Relies on (1)(bb), offer under s 145B, no certificate | not entertained | |
| I13 | Relies on (1)(c), no certificate | in time (no certificate needed) | s 161(3) does not list (c) |
| I14 | Dismissal unfair only by s 153 (redundancy selection) | no interim relief | s 161(1) "unfair by virtue of section 152" |
| I15 | Contract ended by notice given 1 Feb 2026, EDT 1 Mar 2026 | "date of dismissal" for certificate = 1 Feb 2026; without notice = EDT | s 161(6) |

## Goal 2: collective redundancies

### Duty to consult and consultation start (ss 188(A1), (1A), 195A)

| # | Facts (within 90 days) | Expected | Source |
|---|---|---|---|
| R1 | 20 at one establishment; total 20; threshold 25 | duty applies; 30 days | (A1)(b) |
| R2 | 19 at one establishment; total 19; threshold 20 | no duty | |
| R3 | total 20 across sites (max 8 at one); threshold 20 | duty applies; 30 days | (A1)(a) "at least the threshold number" |
| R4 | total 24 (max 10 at one); threshold 25 | no duty | |
| R5 | total 25 (max 10 at one); threshold 25 | duty applies | on the threshold |
| R6 | total 99, 99 at one establishment | 30 days | (1A)(b) |
| R7 | total 100, 100 at one establishment | 45 days | (1A)(a) "100 or more" |
| R8 | total 120 (60 at one establishment); threshold 150 | duty applies via (b); **45 days** | (1A)(a) "100 or more employees as mentioned in subsection (A1)" — I read this as 100 or more proposed to be dismissed as redundant within 90 days, counted across the employer, not only at one establishment. Contestable. |
| R9 | first dismissal 1 Mar 2026; 45-day case | latest start 15 Jan 2026 | (1A) "at least 45 days ... before" |
| R10 | first dismissal 1 Mar 2026; 30-day case | latest start 30 Jan 2026 | |
| R11 | first dismissal 1 Mar 2028; 30-day case | latest start 31 Jan 2028 | leap year |
| R12 | first dismissal 1 Mar 2028; 45-day case | latest start 16 Jan 2028 | |
| R13 | 30-day case, first dismissal 1 Mar 2026; consultation began 29 Jan / 30 Jan / 31 Jan | in time / in time / late | |

### Protected period and remuneration (ss 189(4), 190(2))

| # | Facts | Expected | Source |
|---|---|---|---|
| A1 | first dismissal 1 Jun 2026; award 1 Sep 2026; 90 days | 1 Jun 2026 .. 29 Aug 2026 | s 189(4)(a) earlier date |
| A2 | first dismissal 1 Jun 2026; award 1 May 2026; 180 days | 1 May 2026 .. 27 Oct 2026 | award is earlier |
| A3 | as A2 but tribunal fixes 200 days | capped: 180 days, ends 27 Oct 2026 | "shall not exceed 180 days" |
| A4 | as A2, 181 days | 180 days | |
| A5 | 90 days, week's pay £700, none excluded | £9,000 | s 190(2) |
| A6 | 180 days, £700 | £18,000 | |
| A7 | 3 days, £700 | £300 | "reducing proportionately" |
| A8 | 90 days, £700, 20 days excluded under s 191 | £7,000 | |

### s 189(5) complaint

| # | Facts | Expected | Source |
|---|---|---|---|
| S1 | last dismissal 31 May 2026, no ACAS | last day 30 Aug 2026 (31 Aug exists; day before) | (5)(b) |
| S2 | last dismissal 15 Jun 2026 | 14 Sep 2026 | |
| S3 | complaint presented before the last dismissal | in time | (5)(a) |
| S4 | last dismissal 31 May 2026; Day A 1 Jul, Day B 15 Jul 2026 | 13 Sep 2026 | 14 days -> 13 Sep; Day B + 1 month 15 Aug; no (4) |

### s 192(2) complaint

| # | Facts | Expected | Source |
|---|---|---|---|
| T1 | last unpaid day 30 Nov 2026 | 28 Feb 2027 | (2)(a); no 30 Feb |
| T2 | last unpaid day 15 Jan 2027 | 14 Apr 2027 | |
| T3 | as T2; Day A 1 Apr, Day B 10 Apr 2027 | 10 May 2027 | 9 days -> 23 Apr; within [1 Apr, 10 May] |

## Goal 3: protected industrial action

| # | Facts | Expected | Source |
|---|---|---|---|
| X1 | took protected industrial action; principal reason for dismissal | unfair | s 238A(2)(a) (no 12-week condition: (b), (3)-(7D) repealed in this text) |
| X2 | took protected industrial action; reason something else | not unfair under s 238A | |
| X3 | did not take protected industrial action | not unfair under s 238A | s 238A(1) |
| X4 | qualifying period | does not apply | s 239(1) |
| X5 | no notice; EDT 15 Mar 2026 | last day 14 Sep 2026 | s 239(2)(a), 238(5)(b) |
| X6 | notice given 10 Jan 2026; EDT 10 Mar 2026 | 9 Jul 2026 | s 238(5)(a) notice date |
| X7 | notice given 31 Aug 2026 | 28 Feb 2027 | no 31 Feb |
| X8 | notice given 31 Aug 2027 | 29 Feb 2028 | leap year |
| X9 | no notice; EDT 15 Jan 2026; Day A 1 Jul, Day B 20 Jul 2026 | **14 Jul 2026** | In the deposited text s 239 has no subsection applying s 292A (or ERA s 207B) to (2)(a), so I expect no conciliation extension. If the code extends, that is a disagreement to check against the official text. |
