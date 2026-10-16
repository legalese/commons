# Independent expectations: ERA 2000 dismissal and personal grievances

Written from BRIEF.md, the Act (as at 10 July 2026) and the Legislation Act 2019 ss 13, 54-56, before any `.l4` file was opened. Expected values below are fixed and must not be changed after the encoding is read.

## Readings taken

- **R-a. Period "beginning with" a date** (s 114(7)): the start day is counted (Legislation Act s 54 table, lost from the conversion, but its standard rule is that a period "beginning with/on" a day includes that day). A 90-day period beginning with D ends at the close of D + 89. A 12-month period beginning with D ends under s 56 "immediately before the corresponding day in the ending month", i.e. the close of the day before the anniversary, or the close of the last day of the month if there is no corresponding day.
- **R-b. "within N days after" a day** (s 120(1), (2)): the day itself is excluded (s 54: "after" a day starts the next day; s 54 example item 3: notice within 10 days of 1 August must be given by the close of 11 August). Last day = D + N.
- **R-c. "more than 3 years after the date"** (s 114(6)) and "more than 6 years after the date" (s 142): the period starts the day after D (s 54, "after"), and under s 56 ends immediately before the corresponding day, so the last day to commence is the anniversary date itself. 3 years after 29 Feb 2028: period starts 1 Mar 2028, ends immediately before 1 Mar 2031, last day 28 Feb 2031.
- **R-d. Trial period** (s 67A(2)(a)): "a specified period (not exceeding 90 days), starting at the beginning of the employee's employment" counts the first day of employment. A 90-day trial starting D ends at the close of D + 89. Notice given on D + 89 is "before the end of the trial period" (s 67B(1)); notice on D + 90 is not.
- **R-e. Legislation Act s 55** ("A thing that, under legislation, must or may be done ... within a limited period of time may, if ... the last day of that period is not a working day, be done on the next working day"): I apply it to raising a grievance (s 114(1)), requesting reasons (s 120(1)), providing the statement (s 120(2)), commencing an action within 3 years (s 114(6)) and within 6 years (s 142). The last two are phrased negatively ("No action may be commenced ... more than"), but commencing an action is still a thing that may be done only within a limited period, so I treat s 55 as applying. I do NOT apply s 55 to the trial notice: notice under a trial provision is given under the employment agreement, not "under legislation", and the end of the trial period is fixed by the agreement; it is a cut-off, not a time to do something.
- **R-f. Grounds (l) and (m)** of s 103(1) (remuneration disclosure; protected-disclosure retaliation). ss 67B(3)(b) and 113A(3)(b) save only grounds "(c) to (k)". Ambiguous: possibly a drafting lag. Literal reading taken: a grievance on ground (l) or (m) that is "in respect of the dismissal" is barred by s 67B(2) / s 113A(2); one that is not in respect of the dismissal is not barred (the bar only reaches grievances "in respect of the dismissal").
- **R-g. s 67I(4)** per BRIEF: annual remuneration = remuneration x 364 / days held. Days held of 0 gives no answer (should refuse).
- **R-h. s 113B(3)-(4)** per BRIEF: percentage = (given - last) / last x 100; new threshold = old threshold x (1 + pct/100), rounded to the nearest whole number (dollar). I read "the amount that results from the percentage increase" as the new threshold (s 113B(5) says that amount "takes effect as the specified remuneration threshold"). Exact halves: ambiguous; I take round-half-up (ordinary rounding convention).
- **R-i. s 128 with s 124**: "subject to ... section 124, ... order ... the lesser of a sum equal to that lost remuneration or to 3 months' ordinary time remuneration". I read the reduction as applying to the sum that would otherwise be ordered (the lesser), so the order = lesser x (1 - reduction%). (Alternative: reduce the lost remuneration first, then take the lesser - this gives a different answer when lost > 3 months' OTR.)
- **R-j. Threshold "meets or exceeds"**: equality bars.

Working days (Legislation Act s 13 "working day"), computed by hand/script: Sat/Sun, Waitangi Day, Good Friday, Easter Monday, Anzac Day, Sovereign's birthday (1st Mon June), Matariki (10 Jul 2026, 25 Jun 2027), Labour Day (4th Mon Oct), 25 Dec - 2 Jan, Mondayised 1 Jan / Waitangi / Anzac.

## Goal 1: trial, probation, high earners

| id | inputs | expected | provision |
|---|---|---|---|
| T01 | new employee (never previously employed by employer), written trial provision, 90 days from start of employment | valid trial provision | s 67A(1) "an employee who has not previously been employed by that employer"; (2)(a) "not exceeding 90 days" |
| T02 | as T01, but employee previously employed by that employer | not a valid trial provision | s 67A(1) |
| T03 | as T01, trial 91 days | not a valid trial provision | s 67A(2)(a) "(not exceeding 90 days)" |
| T04 | as T01, trial 30 days | valid | s 67A(2)(a) |
| T05 | as T01, trial provision not in writing | not valid | s 67A(2) "a written provision" |
| T06 | as T01, trial period does not start at the beginning of employment | not valid | s 67A(2)(a) "starting at the beginning of the employee's employment" |
| T07 | valid 90-day trial, employment starts 1 Feb 2027; trial last day | 1 May 2027 (Saturday; no s 55 extension) | s 67A(2)(a), R-d, R-e |
| T08 | T07, notice of termination given 1 May 2027, ground (a) unjustified dismissal | barred | s 67B(1) "notice ... before the end of the trial period"; (2)(a) |
| T09 | T07, notice given 2 May 2027 | not barred | s 67B(1) |
| T10 | T07, notice given 3 May 2027 (next working day) | not barred (s 55 does not extend a trial) | R-e |
| T11 | T07, notice 20 Apr 2027, termination takes effect 10 May 2027 (after trial) | barred | s 67B(1) "whether the termination takes effect before, at, or after the end of the trial period" |
| T12 | 90-day trial from 2 Mar 2026, notice 30 May 2026 (last day, Saturday) | barred | R-d |
| T13 | as T12, notice 2 Jun 2026 | not barred | R-d |
| T14 | trial-barred dismissal, ground (b) relating to the dismissal | barred | s 67B(2)(b) |
| T15 | trial-barred dismissal, ground (b) not relating to the dismissal | not barred | s 67B(3)(a) |
| T16 | trial-barred dismissal, ground (c) discrimination | not barred | s 67B(3)(b) "(c) to (k)" |
| T17 | trial-barred dismissal, ground (d) sexual harassment | not barred | s 67B(3)(b) |
| T18 | trial-barred dismissal, ground (k) health and safety | not barred | s 67B(3)(b) |
| T19 | trial-barred dismissal, ground (m) protected-disclosure retaliation, in respect of the dismissal | barred (literal reading; ambiguous) | s 67B(2), (3)(b); R-f |
| T20 | trial-barred dismissal, ground (l) remuneration disclosure, in respect of the dismissal | barred (literal; ambiguous) | R-f |
| T21 | invalid trial (employee previously employed), notice within the period, ground (a) | not barred | s 67B(1) applies only to "a trial provision under section 67A" |
| T22 | trial-barred dismissal: is employer required to comply with a s 120 request? | no | s 67B(5)(b) |
| T23 | no trial; probation period specified in writing; dismissed during probation, ground (a) | not barred | s 67(1)(b) "neither the fact that the probation period is specified ... affects the application of the law relating to unjustifiable dismissal" |
| H01 | remuneration $200,000, days held 364 | annual remuneration $200,000 | s 67I(4), R-g |
| H02 | remuneration $100,000, days held 182 | $200,000 | R-g |
| H03 | remuneration $100,000, days held 183 | 100000 x 364 / 183 = $198,907.10 (approx; exact 36400000/183) | R-g |
| H04 | remuneration $50,000, days held 0 | refuse / no answer | R-g |
| H05 | annual $200,000, threshold $200,000, dismissed, no opt-out, ground (a) | barred | s 113A(1)(b) "meets or exceeds"; (2)(a) |
| H06 | annual $199,999, threshold $200,000 | not barred | s 113A(1)(b) |
| H07 | remuneration $100,000 over 182 days (=200,000), ground (a) | barred | s 67I(4), s 113A |
| H08 | remuneration $100,000 over 183 days, ground (a) | not barred | as above |
| H09 | annual $250,000, written opt-out agreed under s 67J, ground (a) | not barred | s 67J "may agree in writing ... that both sections 67I and 113A do not apply" |
| H10 | annual $250,000, opt-out agreed but not in writing, ground (a) | barred | s 67J "in writing" |
| H11 | threshold in force $211,111, annual $205,000, ground (a) | not barred | s 113B(1)(b) |
| H12 | threshold $211,111, annual $211,111 | barred | s 113A(1)(b) |
| H13 | high earner, ground (b) relating to dismissal | barred | s 113A(2)(b) |
| H14 | high earner, ground (b) not relating to dismissal | not barred | s 113A(3)(a) |
| H15 | high earner, ground (c) | not barred | s 113A(3)(b) |
| H16 | high earner, ground (f) racial harassment | not barred | s 113A(3)(b) |
| H17 | high earner, ground (m) in respect of the dismissal | barred (literal; ambiguous) | R-f |
| H18 | high earner dismissed: must employer comply with s 120 request? | no | s 67I(1), (3) |
| H19 | high earner with written opt-out: must employer comply with s 120? | yes | s 67J, s 120(2) |
| H20 | employee at $250,000 not dismissed (s 113A(1)(a) fails), ground (b) disadvantage | not barred by s 113A | s 113A(1)(a) "the employee is dismissed" (may not be expressible if the inputs assume a dismissal) |
| B01 | threshold $200,000, AOWE given year $1,900, last increase year $1,800 | increase; pct 5.5556%; new threshold $211,111 (211,111.11 rounded) | s 113B(2)-(4), R-h |
| B02 | given $1,850, last $1,800 | new threshold $205,556 (205,555.56 rounded up) | s 113B(4) |
| B03 | given $1,800, last $1,800 | no increase; threshold stays $200,000 | s 113B(2) "is more than" |
| B04 | given $1,700, last $1,800 | no increase; $200,000 | s 113B(2) |
| B05 | given $2,000.005, last $2,000 (increase of exactly $0.50) | $200,001 (round half up; ambiguous) | s 113B(4), R-h |
| B06 | percentage given $1,900, last $1,800 | 5.5555... (= 50/9) | s 113B(3), BRIEF |
| B07 | threshold of an increase takes effect 1 July of the given year | not expressible as a test unless the encoding takes a date | s 113B(5)(a) |

## Goal 2: raising and time limits

Notification period (s 114(7)): 90 days beginning with the later of occurrence and notice; 12 months for s 103(1)(d).

| id | inputs | expected | provision |
|---|---|---|---|
| N01 | ground (a), occurred and noticed 3 Feb 2027 | period ends 3 May 2027 (Mon, working day); last day to raise 3 May 2027 | s 114(7)(b) "90 days beginning with the date"; R-a |
| N02 | ground (a), occurred 1 Mar 2027, noticed 15 Mar 2027 | runs from 15 Mar; ends 12 Jun 2027 (Sat); last day to raise 14 Jun 2027 (Mon) | s 114(7)(b) "whichever is later"; s 55 |
| N03 | ground (a), occurred 15 Mar 2027, noticed 1 Mar 2027 (earlier) | runs from 15 Mar; last day 14 Jun 2027 | "whichever is later" |
| N04 | ground (a), occurred/noticed 12 Apr 2026 | ends 10 Jul 2026 (Matariki); last day 13 Jul 2026 | s 55, LA s 13 |
| N05 | ground (a), 4 Jan 2026 | ends 3 Apr 2026 (Good Friday); last day 7 Apr 2026 (Tue, after Easter Monday) | s 55 |
| N06 | ground (a), 27 Sep 2026 | ends 25 Dec 2026; last day 5 Jan 2027 (4 Jan 2027 is the Monday after Friday 1 Jan) | s 55; LA s 13 "if 1 January falls on a Friday, the following Monday" |
| N07 | ground (a), 28 Jan 2026 | ends 27 Apr 2026 (Mondayised Anzac Day); last day 28 Apr 2026 | LA s 13 |
| N08 | ground (a), 2 Mar 2026 | ends 30 May 2026 (Sat); last day 2 Jun 2026 (1 Jun is Sovereign's birthday) | LA s 13, s 55 |
| N09 | ground (a), 26 Apr 2026 | ends 24 Jul 2026 (Fri, working day); last day 24 Jul 2026 | R-a |
| N10 | N09; raised 24 Jul 2026 | raised in time | s 114(1) |
| N11 | N09; raised 25 Jul 2026, no consent, no leave | not validly raised | s 114(1) |
| N12 | N09; raised 25 Jul 2026, employer consents | validly raised | s 114(1) "unless the employer consents" |
| N13 | N09; raised 25 Jul 2026, no consent, Authority grants leave | validly raised | s 114(3), (4) |
| N14 | N04; raised 13 Jul 2026 (Mon) | in time | s 55 |
| N15 | N04; raised 14 Jul 2026, no consent or leave | out of time | s 55 |
| N16 | ground (d) sexual harassment, 9 Aug 2026 | 12 months; ends 8 Aug 2027 (Sun); last day 9 Aug 2027 | s 114(7)(a); LA s 56; s 55 |
| N17 | ground (d), 1 Mar 2027 | ends 29 Feb 2028 (Tue, leap year) | s 56 "immediately before the corresponding day" |
| N18 | ground (d), 29 Feb 2028 | ends 28 Feb 2029 (Wed) | s 56 "(if there is no such day) at the close of the last day of the ending month" |
| N19 | ground (d), 1 Mar 2027, raised 1 Jun 2027 (after 90 days but within 12 months) | in time | s 114(7)(a) |
| N20 | ground (a), 1 Mar 2027, raised 1 Jun 2027 | out of time (ends 29 May 2027 Sat -> 31 May Mon) | s 114(7)(b) |
| N21 | ground (f) racial harassment, 26 Apr 2026 | 90 days, not 12 months: last day 24 Jul 2026 | s 114(7)(b) "any other personal grievance" |
| N22 | ground (d), occurred 1 Mar 2027 noticed 10 Mar 2027 | ends 9 Mar 2028 | "whichever is later" |
| L01 | grievance raised 10 Mar 2027 | last day to commence 10 Mar 2030 (Sun) -> 11 Mar 2030 | s 114(6), R-c, R-e |
| L02 | raised 29 Feb 2028 | last day 28 Feb 2031 (Fri) | R-c, LA s 56 |
| L03 | raised 10 Mar 2027, action commenced 11 Mar 2030 | in time (s 55) | R-e |
| L04 | raised 10 Mar 2027, action commenced 12 Mar 2030 | out of time | s 114(6) |
| L05 | raised 29 Feb 2028, commenced 1 Mar 2031 | out of time | s 114(6) |
| P01 | non-grievance problem, cause arose 15 Jun 2026 | last day 15 Jun 2032 (Tue) | s 142 "more than 6 years after the date" |
| P02 | cause arose 7 Feb 2026 | 7 Feb 2032 (Sat) -> 9 Feb 2032 | s 142, s 55 |
| P03 | cause arose 6 Feb 2026 | 6 Feb 2032 (Waitangi Day, Fri) -> 9 Feb 2032 | s 142, s 55 |
| P04 | cause 15 Jun 2026, commenced 16 Jun 2032 | out of time | s 142 |
| S01 | dismissed 1 Sep 2026, aware same day | request by 31 Oct 2026 (Sat) -> 2 Nov 2026 | s 120(1) "within 60 days after"; R-b; s 55 |
| S02 | dismissed 1 Sep 2026, aware 10 Sep 2026 | 9 Nov 2026 | s 120(1) "whichever is the later" |
| S03 | dismissed 27 Aug 2026, aware same day | 26 Oct 2026 (Labour Day) -> 27 Oct 2026 | s 55 |
| S04 | S01, request made 2 Nov 2026 | in time | s 55 |
| S05 | S01, request made 3 Nov 2026 | out of time | s 120(1) |
| S06 | request received 20 Oct 2026 | statement due 3 Nov 2026 | s 120(2) "within 14 days after the day on which the request is received" |
| S07 | request received 15 Oct 2026 | 29 Oct 2026 | s 120(2) |
| S08 | request received 18 Dec 2026 | 1 Jan 2027 -> 5 Jan 2027 | s 55, LA s 13 |
| S09 | request received 11 Jun 2027 | 25 Jun 2027 (Matariki) -> 28 Jun 2027 | s 55 |

## Goal 3: remedies

| id | inputs | expected | provision |
|---|---|---|---|
| M01 | grievance established; employee contributed; contribution was serious misconduct | no remedy at all (reinstatement, reimbursement, compensation all unavailable); reimbursement ordered = 0 | s 123B "must not provide for any remedy" |
| M02 | contributed, not serious misconduct | no reinstatement, no compensation; reimbursement available | s 123C(a), (c) |
| M03 | no contribution | reinstatement, reimbursement, compensation all available | s 123 |
| M04 | serious misconduct found but not contributing | s 123B not engaged; all remedies available | s 123B(a) and (b) both required |
| M05 | lost $10,000, 3 months' OTR $15,000, reduction 0% | $10,000 | s 128(2) "the lesser of" |
| M06 | lost $20,000, OTR $15,000, 0% | $15,000 | s 128(2) |
| M07 | lost $15,000, OTR $15,000, 0% | $15,000 | s 128(2) |
| M08 | lost $20,000, OTR $15,000, reduction 20% | $12,000 (R-i; alternative reading gives $15,000) | s 128(2) "subject to ... section 124"; s 124(1)(b) |
| M09 | lost $10,000, OTR $15,000, reduction 25% | $7,500 | s 124 |
| M10 | lost $10,000, OTR $15,000, reduction 100% | $0 | s 124(2) "by up to 100%" |
| M11 | reduction 120% | refuse / invalid | s 124(2) |
| M12 | grievance, but no remuneration lost (lost $0) | s 128 does not apply; reimbursement $0 | s 128(1)(b) |
| M13 | no personal grievance found | s 128 does not apply; $0 | s 128(1)(a) |
| M14 | contributed + serious misconduct, lost $10,000, OTR $15,000 | $0 | s 123B overrides s 128 (s 128(2) itself is "subject to" only s 124 and (3); I read s 123B "Despite section 123 ... must not provide for any remedy" as covering the s 128 order, which is a reimbursement remedy under s 123(1)(b)) |
| M15 | s 128(3) discretion to award more | not expressible (discretion) | s 128(3) |

## Top-level combined

| id | inputs | expected | provision |
|---|---|---|---|
| G01 | not high earner, no trial, ground (a), dismissed and aware 3 Feb 2027, raised 3 May 2027 | may be brought; raised in time; proceedings by 3 May 2030 (Fri) | ss 114(1), (6) |
| G02 | valid trial, notice on last day, ground (a) | may not be brought | s 67B |
| G03 | high earner $200,000 full year, no opt-out, ground (a) | may not be brought | s 113A |
| G04 | G01 with lost $20,000, OTR $15,000, contributed (not serious), reduction 20% | reinstatement and compensation unavailable; reimbursement $12,000 | ss 123C, 124, 128 |

## Not expressible as an input/output test

- s 103A justification and the size of remedies other than s 128 (out of scope per BRIEF).
- s 114(4) whether circumstances are "exceptional" / s 115 - a finding, taken as an input (leave granted or not).
- s 114(2) whether a grievance has been "raised" (reasonable steps) - taken as an input date.
- s 113B(6) publication and (7) corrections.
- s 128(3) discretion.
- B07 effective date of an increase, unless the encoding takes a date.

## Added after reading the encoding (no expected value above changed)

Not expressible against the encoding's functions and inputs, so not in tests-independent.l4:
- T06 (trial not starting at the beginning of employment): no input; the encoding assumes it does.
- T11 is tested only on the notice date; when termination takes effect is not an input.
- T22, H18, H19 (whether the employer must answer a s 120 request after a trial or high-earner dismissal): no function.
- T23 probation: no input; tested only as "no trial provision".
- H20 (employee not dismissed): the inputs assume a dismissal.
- B06 (the percentage itself) and B07 (1 July effective date): no function / no date input.
- M13 (no grievance found) and M15 (s 128(3) discretion): no input.
- H04 (0 days held) and M11 (reduction 120%): expected a refusal, which an #ASSERT cannot state; checked by #EVAL instead (H04 refuses; M11 is clamped to 100% and gives 0 - a difference).

Lettering: the conversion stripped paragraph labels and I lettered s 103(1) positionally (a)-(m). The encoding uses (a)-(d), (da), (e)-(j), (ja), (k), i.e. inserted paragraphs; on that lettering "(c) to (k)" in ss 67B(3)(b) and 113A(3)(b) covers every ground, and my reading R-f (T19, T20, H17) rests on my positional lettering. The expected values are left as written.
