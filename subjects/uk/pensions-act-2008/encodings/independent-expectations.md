# Independent expectations — Pensions Act 2008 (ss 1, 3, 7, 9, 13, 20, 40, 41)

Written from BRIEF.md and the revised text (point in time 29 June 2026) only, before any `.l4` file was opened.

## Readings adopted (from the brief, plus my own where the brief is silent)

- R1. Ages: "aged at least 16" holds from the 16th birthday; "aged at least 22" from the 22nd; "under 75" holds up to the day before the 75th birthday. "Has not reached pensionable age" holds strictly before the pensionable-age day. Everything is tested on the first day of the pay reference period (PRP).
- R2. Pro rata (s 3(6B), s 13(2)): amount × months / 12, no rounding. For a weekly PRP I take months = 12/52, so the factor is 1/52.
- R3. s 3(1)(c): "more than £10,000", strictly, after pro-rating.
- R4. s 13(1): qualifying earnings (QE) = the part of the earnings that is more than the lower limit and not more than the upper limit = max(0, min(E, U) − L).
- R5. s 1(1)(c) "qualifying earnings are payable": QE > 0, i.e. E strictly more than the pro-rated £6,240.
- R6. s 3(3)/(4): if either applies, s 3 still "applies" but s 3(2) does not, so no arrangements are required. Then s 7:
  - s 3(3) (active member of a qualifying scheme): s 7(1) fails, so the jobholder may not opt in. Status: none of these.
  - s 3(4) (ceased membership by their own act within the prescribed period, not now a member): s 7(1) holds and s 7(2)(a) does not bar, because no arrangements are required. Status: may opt in.
- R7. s 7: a jobholder who is not eligible under s 3 (age 16-21, at or past pensionable age, or earnings at or below the trigger) and is not an active member of a qualifying scheme may opt in. If they are an active member, the status is none of these.
- R8. s 9: GB, age 16 to 74, QE = 0, and not an active member of a scheme meeting s 9(7) gives "may ask to join". Under 16, 75 or older, or not working in GB gives none of these.
- R9. s 20(1)(a) "the jobholder's employer must pay contributions": I read this as the employer contribution being more than 0. If the employer pays nothing, the test fails even where QE = 0 (so 3% of QE is 0). This is an ambiguity, noted.
- R10. s 20(1)(b)-(c): "equal to or more than", so exact equality passes. The total is employer plus jobholder.
- R11. s 40(5)(b): earliest payment date = issue date + 28 days.
- R12. s 41(6)(d): the escalating start date must not be earlier than the s 40(5)(b) date. The same day is allowed.
- R13. s 41(6)(e): days = the days from the start date up to but not including the compliance date (0 if compliance is on or before the start date). Penalty = days × daily rate.
- R14. s 41(2)(a) bars issue only where the underlying notice is within s 41(1)(a)-(c) (s 35/36/37) and a review is pending. s 41(2)(b) bars for any s 41(1) notice where a tribunal reference on the related fixed penalty notice is pending.
- R15. s 40(4)(b) / s 41(5)(b): "must not exceed", so the limit itself is allowed (£50,000 and £10,000 a day).

## Figures used

| PRP | factor | trigger (s 3) | lower L | upper U |
|---|---|---|---|---|
| 12 months | 1 | 10000 | 6240 | 50270 |
| 6 months | 1/2 | 5000 | 3120 | 25135 |
| 1 month | 1/12 | 10000/12 = 833.33… | 520 | 50270/12 = 4189.166… |
| 1 week (12/52 months) | 1/52 | 10000/52 = 192.307… | 120 | 50270/52 = 966.73… |

## Goal 1 — status on the first day of the PRP

Base worker (unless stated otherwise): born 10 May 1990, pensionable age 10 May 2057, works in GB, no exceptions, not an active member of any scheme, 12-month PRP starting 1 June 2026. Act: s 1(1), s 3(1), (3), (4), (6B), s 7(1)-(2), s 9(1).

| # | Scenario | Expected |
|---|---|---|
| S1 | base, E = 30000 | auto-enrol (eligible jobholder) |
| S2 | E = 10000 exactly (not "more than £10,000") | opt in |
| S3 | E = 10000.01 | auto-enrol |
| S4 | E = 6240 (QE = 0) | ask to join (s 9) |
| S5 | E = 6240.01 (QE > 0, below the trigger) | opt in |
| S6 | E = 0 | ask to join |
| S7 | monthly PRP, E = 833 (at or below 10000/12) | opt in |
| S8 | monthly PRP, E = 834 | auto-enrol |
| S9 | monthly PRP, E = 520 (QE = 0) | ask to join |
| S10 | monthly PRP, E = 520.01 | opt in |
| S11 | weekly PRP (months 12/52), E = 192 | opt in |
| S12 | weekly PRP, E = 193 | auto-enrol |
| S13 | weekly PRP, E = 120 | ask to join |
| S14 | 6-month PRP, E = 5000 | opt in |
| S15 | 6-month PRP, E = 5000.01 | auto-enrol |
| S16 | age: PRP starts on the 16th birthday, E = 30000 | opt in (jobholder, under 22) |
| S17 | age: PRP starts the day before the 16th birthday, E = 30000 | none |
| S18 | age: the day before the 16th birthday, E = 5000 | none (s 9(1)(a) needs age 16+) |
| S19 | age: on the 22nd birthday, E = 30000 | auto-enrol |
| S20 | age: the day before the 22nd birthday, E = 30000 | opt in |
| S21 | on the pensionable-age day, E = 30000 | opt in |
| S22 | the day before pensionable age, E = 30000 | auto-enrol |
| S23 | age 74, past pensionable age, E = 30000 | opt in |
| S24 | on the 75th birthday, E = 30000 | none |
| S25 | the day before the 75th birthday, E = 5000 | ask to join |
| S26 | on the 75th birthday, E = 5000 | none |
| S27 | not working in GB, E = 30000 | none |
| S28 | not working in GB, E = 5000 | none |
| S29 | s 3(3): already an active member of a qualifying scheme, E = 30000 | none (s 7(1) fails) |
| S30 | s 3(4): ceased within the prescribed period by own act, E = 30000 | opt in |
| S31 | under 22, active member of a qualifying scheme, E = 30000 | none |
| S32 | QE = 0, already a member of a scheme meeting s 9 | none |
| S33 | the trigger is tested on gross earnings (s 13(3)), not on QE: E = 10001 → QE 3761 | auto-enrol |

## Goal 2 — qualifying earnings and s 20 contributions

QE = max(0, min(E, U) − L). Act: s 13(1)-(2), s 20(1)(a)-(c).

| # | Scenario | Expected QE |
|---|---|---|
| Q1 | 12 months, E = 30000 | 23760 |
| Q2 | 12 months, E = 6240 | 0 |
| Q3 | 12 months, E = 6241 | 1 |
| Q4 | 12 months, E = 50270 | 44030 |
| Q5 | 12 months, E = 60000 | 44030 |
| Q6 | 12 months, E = 0 | 0 |
| Q7 | 1 month, E = 2000 | 1480 |
| Q8 | 1 month, E = 5000 | 50270/12 − 520 |
| Q9 | 1 month, E = 520 | 0 |
| Q10 | 6 months, E = 20000 | 16880 |
| Q11 | 6 months, E = 30000 | 22015 |
| Q12 | 6 months, E = 3000 | 0 |
| Q13 | weekly, E = 500 | 380 |
| Q14 | weekly, E = 2000 | 50270/52 − 120 |

Minimums (s 20(1)(b) 3%, (c) 8%):

| # | Scenario | Expected |
|---|---|---|
| C1 | QE 23760: employer minimum | 712.8 |
| C2 | QE 23760: total minimum | 1900.8 |
| C3 | QE 44030: employer / total minimum | 1320.9 / 3522.4 |
| C4 | E 30000 annual, employer 712.8, jobholder 1188 (total 1900.8) | meets (both exact) |
| C5 | employer 712.79, jobholder 1500 | fails (b) |
| C6 | employer 712.8, jobholder 1187.99 (total 1900.79) | fails (c) |
| C7 | employer 1900.8, jobholder 0 | meets (all from the employer) |
| C8 | employer 0, jobholder 5000 | fails (a) and (b) |
| C9 | QE 0 (E 6000), employer 0, jobholder 0 | fails (a), under R9; ambiguous |
| C10 | QE 0, employer 1, jobholder 0 | meets |
| C11 | monthly E 2000 (QE 1480): employer 44.4, jobholder 74 | meets (44.4 = 3%, 118.4 = 8%) |
| C12 | monthly E 2000: employer 44.39, jobholder 100 | fails |

## Goal 3 — penalty notices

Act: s 40(4)-(5), s 41(2), (5), (6)(d)-(e).

| # | Scenario | Expected |
|---|---|---|
| P1 | maximum fixed penalty | 50000 |
| P2 | fixed penalty 50000 within limit? | yes |
| P3 | fixed penalty 50000.01 within limit? | no |
| P4 | issued 15 Jan 2026: earliest payment date | 12 Feb 2026 |
| P5 | issued 10 Feb 2026 | 10 Mar 2026 |
| P6 | issued 10 Feb 2024 (leap year) | 9 Mar 2024 |
| P7 | issued 20 Dec 2026 | 17 Jan 2027 |
| P8 | stated payment date = issue + 28: valid | yes |
| P9 | stated payment date = issue + 27: valid | no |
| P10 | escalating: compliance notice (s 35), no review, no reference | may issue |
| P11 | s 35 notice, review applied for and not completed | may not (s 41(2)(a)) |
| P12 | s 36 or s 37 notice, review pending | may not |
| P13 | s 72 PA 2004 notice, review pending (outside (1)(a)-(c)) | may issue |
| P14 | s 72 notice, tribunal reference pending | may not (s 41(2)(b)) |
| P15 | s 35 notice, review completed, reference determined | may issue |
| P16 | daily rate 10000 within limit | yes |
| P17 | daily rate 10000.01 | no |
| P18 | maximum daily rate | 10000 |
| P19 | FPN payment date 12 Feb 2026, escalating start 12 Feb 2026 | start valid |
| P20 | start 11 Feb 2026 | start invalid |
| P21 | start 1 Mar 2026, compliance 11 Mar 2026: days | 10 |
| P22 | same, rate 500: penalty | 5000 |
| P23 | start 1 Mar 2026, compliance 1 Mar 2026 | 0 days, penalty 0 |
| P24 | compliance 20 Feb 2026, before the start of 1 Mar 2026 | 0 days |
| P25 | start 28 Feb 2024, compliance 1 Mar 2024 (leap) | 2 days |
| P26 | start 28 Feb 2026, compliance 1 Mar 2026 | 1 day |
| P27 | start 1 Mar 2026, compliance 31 Mar 2026, rate 10000 | 30 days, 300000 |
| P28 | start 15 Dec 2026, compliance 5 Jan 2027, rate 250 | 21 days, 5250 |

## Ambiguities

- A1 (R9): s 20(1)(a), where the employer pays nothing and QE is 0.
- A2: "aged at least 16" for a person born on 29 February. Not tested.
- A3: a weekly PRP expressed as months: 12/52 vs 7/365×12. I use 12/52; the brief says "length in months".
- A4 (R6): s 3(4) → opt in follows from s 7(2)(a) once arrangements are not required. An encoder could reasonably return "none".
- A5: s 41(2)(b) "fixed penalty notice issued in relation to that notice": I treat it as a reference flag input.
