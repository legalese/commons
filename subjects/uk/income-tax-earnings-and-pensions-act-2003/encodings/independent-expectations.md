# Independent expectations: ITEPA 2003, car, cheap loan and termination goals

Written from BRIEF.md and the source text only, before reading any `.l4` file.
Figures are exact; fractions are given where the Act's formula does not come out whole.

Tax years used: 2025-26 runs 6 April 2025 to 5 April 2026 (365 days). 2023-24 runs 6 April 2023 to 5 April 2024 and contains 29 February 2024 (366 days).

## A. Company car (ss 120, 121, 132, 139, 141, 143, 144)

Base car unless stated: list price £30,000, accessories £1,000, capital contributions £2,000, CO2 120 g/km, petrol, available all of 2025-26, no private-use payments.

Appropriate percentage (s 139(3)-(4): "21% plus one percentage point for each 5 grams per kilometre ... by which the CO2 emissions figure exceeds 75" and "at most 37%"; "if a CO2 emissions figure is not a multiple of 5, round it down to the nearest multiple of 5"; s 141(2) step 3 "+4 points ... and 35%"):

| # | Facts | Expected | Source |
|---|-------|----------|--------|
| A1 | CO2 75, petrol | 21% | s 139(3)(a): exceeds 75 by 0 |
| A2 | CO2 79.9, petrol | 21% | s 139(4): rounds down to 75 |
| A3 | CO2 79, petrol | 21% | s 139(4) |
| A4 | CO2 80, petrol | 22% | s 139(3)(a) |
| A5 | CO2 120, petrol | 30% | 21 + 9 |
| A6 | CO2 155, petrol | 37% | 21 + 16 = 37, at the cap |
| A7 | CO2 160, petrol | 37% | 21 + 17 = 38, capped by s 139(3)(b) |
| A8 | CO2 74.9, petrol | NOTHING | "less than 75" — s 139(1) table, not supplied (brief) |
| A9 | CO2 74, petrol | NOTHING | s 139(1) table |
| A10 | CO2 75, diesel (s 141 applies) | 25% | 21 + 4 |
| A11 | CO2 120, diesel | 34% | 30 + 4 |
| A12 | CO2 125, diesel | 35% | 31 + 4 = 35, at the cap |
| A13 | CO2 140, diesel | 35% | 34 + 4 = 38, capped by s 141(2) step 3(b) |
| A14 | CO2 160, diesel | 35% | s 139 gives 37; 37 + 4 = 41, capped at 35 |
| A15 | CO2 74, diesel | NOTHING | step 2 takes the s 139(1) table figure, which is missing |

Interim sum and cash equivalent (s 121(1) steps 1-8; s 132(3) "the lesser of ... the total of the capital sums ... and £5,000"):

| # | Facts | Expected | Source |
|---|-------|----------|--------|
| A16 | Base car | interim £29,000; cash equivalent £8,700 | 29,000 × 30% |
| A17 | Contributions £7,000 | interim £26,000; cash £7,800 | s 132(3)(b) cap £5,000 |
| A18 | Contributions exactly £5,000 | interim £26,000; cash £7,800 | lesser of equal amounts |
| A19 | Contributions nil | interim £31,000; cash £9,300 | |
| A20 | First available 6 May 2025 (U = 30, 6 Apr-5 May) | cash 8,700 − (30/365)×8,700 = 582900/73 (≈ £7,984.93) | s 143(2)(a), (3) (U/Y)×A |
| A21 | Last available 5 Jan 2026 (U = 90, 6 Jan-5 Apr) | 8,700 − (90/365)×8,700 = 478500/73 (≈ £6,554.79) | s 143(2)(b) |
| A22 | One gap of 45 days not available | 8,700 − (45/365)×8,700 = 556800/73 | s 143(2)(c) |
| A23 | One gap of 29 days not available | £8,700 (no deduction) | s 143(2)(c) "30 days or more" |
| A24 | One gap of exactly 30 days | 582900/73 (same as A20) | 30 is "30 days or more" |
| A25 | Start 30 + end 90 + gap 45 days (U = 165) | 8,700 × 200/365 = 348000/73 | all three limbs added |
| A26 | Leap year 2023-24, first available 6 Jun 2023 (U = 61, Y = 366) | 8,700 − 61/366 × 8,700 = £7,250 | Y "the number of days in that year" |
| A27 | Required £1,200 for private use, paid 6 July 2026 | £7,500 | s 144(1)(b) "on or before 6 July following that year" |
| A28 | Same, paid 7 July 2026 | £8,700 | out of time |
| A29 | Same, paid 1 Dec 2025 (in the year) | £7,500 | before 6 July following |
| A30 | Required and paid £10,000 by 6 July 2026 | £0 | s 144(2): equal to or exceeds the provisional sum, nil |
| A31 | U = 30 at start (A20) and £1,200 paid in time | 582900/73 − 1,200 = 495300/73 | s 144 deducts from the provisional sum after s 143 |

Open question, not asserted: the employee is required to pay £1,200 and pays only £1,000 in time. Read literally, s 144(1)(b) "pays that amount" is not met, so no deduction; HMRC practice deducts the £1,000. I do not assert either.

## B. Cheap loans (ss 175, 180, 182)

Official rate 3.75% (input). Tax year 2025-26. No s 176-179 exception unless stated.
Step 3 formula (brief): A × I × (M ÷ 12); A = (opening + closing) ÷ 2.

| # | Facts | Expected | Source |
|---|-------|----------|--------|
| B1 | £20,000 open and close, 12 months, highest £20,000, no interest paid | official interest £750; taxable; cash equivalent £750 | s 182, s 175(3) |
| B2 | As B1, interest paid £300 | £450 | s 175(3)(b) |
| B3 | As B1, interest paid £800 (above official) | not a taxable cheap loan; nothing charged (0 in earnings) | s 175(2)(b) "less than" |
| B4 | As B1, interest paid exactly £750 | not taxable; nothing charged | "less than" fails on equality |
| B5 | £10,000 open and close, highest £10,000 | threshold not exceeded; nothing charged | s 180(2) "does not exceed £10,000" |
| B6 | £10,001 open and close, highest £10,001 | taxable; cash 10,001 × 0.0375 = 375.0375 | threshold exceeded |
| B7 | Made in year: £30,000 on the day made, £10,000 at 5 April, 8 whole months, highest £30,000 | A = 20,000; 20,000 × 0.0375 × 8/12 = £500 | s 182 step 1(1), M |
| B8 | As B1 but an exception in ss 176-179 applies | not taxable; nothing charged | s 175(2)(c) |
| B9 | Opening £8,000, closing £8,000, but highest £12,000 in the year | threshold exceeded; taxable; 8,000 × 0.0375 = £300 | s 180(2) "at all times" vs step 1 averaging |
| B10 | Average rate 2.5% (step 2), £20,000, 6 months | 20,000 × 0.025 × 6/12 = £250 | s 182 step 2 |

## C. Termination (ss 402A-402E, 403, 404)

Default weekly-paid employee: basic pay £700 for a last pay period of 7 days, not monthly. No T, no redundancy, no earlier payments, unless stated.

Dates (s 402E(2), (5)-(7); brief: trigger + notice days, or the corresponding date months later):

| # | Facts | Expected | Source |
|---|-------|----------|--------|
| C1 | Non-notice; last day 31 Mar 2026; min notice 30 days | trigger 31 Mar 2026; ELTD 30 Apr 2026; PENP days 30; PENP 700×30/7 = £3,000 | s 402E(2)(a), (7); s 402D(1),(3) |
| C2 | C1, T = £1,000 | PENP £2,000 | ((BP×D)/P) − T |
| C3 | C1, T = £5,000 | PENP nil (0) | s 402D(2) negative is nil |
| C4 | C1, relevant awards £50,000 | s 402B part £3,000; s 403 above threshold: 47,000 − 30,000 = £17,000 | s 402C(4), 402A(3), 403(1) |
| C5 | C3 with awards £50,000 | s 402B £0; s 403 £20,000 | s 402C(4) needs PENP "not nil"; else all to 403 |
| C6 | Notice case; notice given 1 Mar 2026; min notice 84 days; last day 31 Mar 2026 | trigger 1 Mar; ELTD 24 May 2026; days 54; PENP 700×54/7 = £5,400 | s 402E(2)(b), (7) |
| C7 | Notice case; notice 1 Mar 2026; min notice 30 days; last day 31 Mar 2026 | ELTD 31 Mar 2026; days nil; PENP 0 | s 402E(6) |
| C8 | Notice case; worked longer than notice: notice 1 Mar 2026, 14 days, last day 31 Mar | ELTD 15 Mar; days nil; PENP 0 | s 402E(6) "or precedes" |
| C9 | Minimum notice nil days; non-notice; last day 31 Mar 2026 | ELTD 31 Mar; PENP 0 | |
| C10 | Monthly equal instalments £3,000; notice in 3 whole months, contractual; notice case, notice 15 Jan 2026, last day 15 Jan 2026 | ELTD 15 Apr 2026; PENP period = 3 months; D = 3, P = 1; PENP £9,000 | s 402D(6) |
| C11 | As C10 but last day 15 Feb 2026 | PENP period 2 whole months (16 Feb-15 Apr); PENP £6,000 | s 402D(6) "otherwise a whole number of months" |
| C12 | As C10 but last day 1 Feb 2026 | not a whole number of months; s 402D(6A): D = 73 days (2 Feb-15 Apr), P = 30.42; PENP 3,000×73/30.42 = 3650000/507 (≈ £7,199.21) | s 402D(6A) |
| C13 | Monthly equal instalments £3,000; min notice 56 days (8 weeks); non-notice; last day 31 Mar 2026 | ELTD 26 May 2026; D = 56; PENP 3,000×56/30.42 = 2800000/507 (≈ £5,522.68) | s 402D(6A) |
| C14 | Month notice from a month end: trigger 31 Jan 2026, 1 month | ELTD 28 Feb 2026 | brief: corresponding date months later |
| C15 | Leap: trigger 31 Jan 2028, 1 month | ELTD 29 Feb 2028 | |
| C16 | Awards £30,000 relevant, PENP £3,000 (C1) | s 402B £3,000; s 403 £27,000 below threshold → £0 | |
| C17 | Statutory redundancy £10,000 + other £20,000; PENP £3,000 | relevant awards £20,000; s 402B £3,000; s 403 gets 10,000 + 17,000 = £27,000 → £0 above | s 402C(2)(a) |
| C18 | C17 with earlier payments counted against threshold £5,000 | 27,000 + 5,000 = 32,000 → £2,000 above | s 403(4), 404(4) |
| C19 | Relevant awards £40,000; PENP nil (C7); earlier £25,000 | s 403 above: 40,000 − 5,000 = £35,000 | s 404(4) earlier years first |
| C20 | Relevant £40,000; PENP nil; earlier £35,000 | £40,000 above | threshold used up |
| C21 | PENP £9,000 (C10) ≥ relevant awards £8,000 | s 402B all £8,000; s 403 £0 | s 402C(3) |
| C22 | Approved contractual £15,000 of which £12,000 is within the redundancy amount; nothing else; PENP £3,000 | relevant £3,000; s 402B £3,000; s 403 gets £12,000 → £0 above | s 402C(2)(b) |
