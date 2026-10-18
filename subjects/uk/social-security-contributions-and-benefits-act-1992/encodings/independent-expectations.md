# Independent expectations: SSCBA 1992 (Class 1, SSP, SMP)

Written from BRIEF.md and the revised text (point in time 8 July 2026) only, before any `.l4` file was opened.

## Common inputs (chosen for the tests)

- Class 1 (weekly): primary threshold PT = £242, upper earnings limit UEL = £967, secondary threshold ST = £96. Secondary percentage 15% unless stated.
- SSP: cap £123.25 (s 157(1)(a)).
- SMP: lower earnings limit LEL = £129; prescribed weekly rate = £194.32.

## A. Class 1 contributions (ss 6(1), 8(1)-(2), 9(1)-(2))

Act: s 8(1) "the aggregate of (a) the main primary percentage [8%] of so much of the earner's earnings ... as (i) exceeds the current primary threshold ... but (ii) does not exceed the current upper earnings limit ...; and (b) the additional primary percentage [2%] of so much of those earnings as exceeds the current upper earnings limit". s 9(1) "the relevant percentage of so much of the earnings ... as exceeds the current secondary threshold". s 6(1): payable only "if the amount paid exceeds" the threshold; otherwise none is payable (taken as £0 due).

| # | Earnings | Expected primary | Expected secondary (15%) | Working |
|---|---|---|---|---|
| A1 | 0 | 0 | 0 | nothing exceeds any threshold |
| A2 | 50 | 0 | 0 | below ST and PT |
| A3 | 96 (= ST) | 0 | 0 | "exceeds" is strict; nothing above ST |
| A4 | 200 | 0 | 15.6 | 15% × 104 |
| A5 | 242 (= PT) | 0 | 21.9 | 15% × 146 |
| A6 | 243 | 0.08 | 22.05 | 8% × 1; 15% × 147 |
| A7 | 500 | 20.64 | 60.6 | 8% × 258; 15% × 404 |
| A8 | 967 (= UEL) | 58 | 130.65 | 8% × 725, nothing above UEL; 15% × 871 |
| A9 | 968 | 58.02 | 130.8 | 58 + 2% × 1 |
| A10 | 1000 | 58.66 | 135.6 | 58 + 2% × 33; 15% × 904 |
| A11 | 2000 | 78.66 | 285.6 | 58 + 2% × 1033; 15% × 1904 |
| A12 | 1000, secondary percentage 0% (s 9(1A)(aa) / 9A) | — | 0 | 0% × 904 |
| A13 | 500, secondary percentage 13.8% | — | 55.752 | 0.138 × 404 |
| A14 | 300, PT=ST=242 (equal thresholds) | 4.64 | 8.7 | 8% × 58; 15% × 58 |
| A15 | Monthly prescribed equivalents PT 1048, UEL 4189, earnings 5000 | 267.5 | — | 8% × 3141 = 251.28; 2% × 811 = 16.22 |

## B. Statutory sick pay (ss 152(2)-(3), 155(2)-(4), 157(1), (3))

s 157(1): "the lower of (a) £123.25, and (b) 80% of the employee's normal weekly earnings."

| # | NWE | Expected weekly rate |
|---|---|---|
| B1 | 200 | 123.25 (80% = 160) |
| B2 | 154.0625 | 123.25 (80% = 123.25 exactly; both limbs equal) |
| B3 | 154.0626 | 123.25 |
| B4 | 154 | 123.2 |
| B5 | 100 | 80 |
| B6 | 0 | 0 |

s 157(3): "the weekly rate applicable on that day divided by the number of days which are, in the week (beginning with Sunday) in which that day falls, qualifying days".

| # | NWE | Qualifying days | Expected daily amount |
|---|---|---|---|
| B7 | 200 | 5 | 24.65 |
| B8 | 200 | 7 | 123.25/7 |
| B9 | 200 | 3 | 123.25/3 |
| B10 | 200 | 1 | 123.25 |
| B11 | 100 | 4 | 20 |
| B12 | 154 | 6 | 123.2/6 |

s 155(4): "an amount equal to 28 times the weekly rate".

| # | NWE | Expected entitlement limit |
|---|---|---|
| B13 | 200 | 3451 |
| B14 | 100 | 2240 |
| B15 | 154 | 3449.6 |

s 155(3): maximum entitlement reached on the day the amount "first reaches or passes the entitlement limit". If the encoding has a "reached" predicate: aggregate 3451 with limit 3451 → reached; 3450.99 → not reached; 3500 → reached.

s 152(3): "Any two periods of incapacity for work which are separated by a period of not more than 8 weeks shall be treated as a single period". Reading (brief): days strictly between the end of the first and the start of the second ≤ 56.

| # | First period ends | Second begins | Days between | Link? |
|---|---|---|---|---|
| B16 | Mon 1 Mar 2027 | Tue 27 Apr 2027 | 56 | yes |
| B17 | Mon 1 Mar 2027 | Wed 28 Apr 2027 | 57 | no |
| B18 | Mon 1 Mar 2027 | Tue 2 Mar 2027 | 0 | yes (contiguous) |
| B19 | Mon 1 Mar 2027 | Mon 8 Mar 2027 | 6 | yes |
| B20 | Mon 1 Mar 2027 | Mon 1 Nov 2027 | 244 | no |

## C. Statutory maternity pay (ss 164(2), 165(2), 166(1)-(2), 171(1A))

s 171(1A): "'week' means a period of 7 days beginning with Sunday". Expected week of confinement (EWC) = the Sunday on or before the expected date.

| # | Expected date | Weekday | EWC begins |
|---|---|---|---|
| C1 | 3 Jan 2027 | Sunday | 3 Jan 2027 |
| C2 | 4 Jan 2027 | Monday | 3 Jan 2027 |
| C3 | 6 Jan 2027 | Wednesday | 3 Jan 2027 |
| C4 | 8 Jan 2027 | Friday | 3 Jan 2027 |
| C5 | 9 Jan 2027 | Saturday | 3 Jan 2027 |
| C6 | 10 Jan 2027 | Sunday | 10 Jan 2027 |
| C7 | 5 Jan 2027 | Tuesday | 3 Jan 2027 |
| C8 | 7 Jan 2027 | Thursday | 3 Jan 2027 |

Nth week before = EWC − 7N days. For EWC 3 Jan 2027: 11th week before begins **Sun 18 Oct 2026**; 14th week **Sun 27 Sep 2026**; 15th week (the week immediately preceding the 14th) **Sun 20 Sep 2026**. For EWC 10 Jan 2027 (expected Sunday 10 Jan or Monday 11 Jan): 11th week **25 Oct 2026**, 15th week **27 Sep 2026**.

s 165(2): "the maternity pay period shall begin with the 11th week before the expected week of confinement" → earliest start for expected date 6 Jan 2027 = **18 Oct 2026**; for 9 Jan 2027 (Saturday) = 18 Oct 2026; for 10 Jan 2027 (Sunday) = **25 Oct 2026**.

s 164(2)(a): "a continuous period of at least 26 weeks ending with the week immediately preceding the 14th week before". The 26 weeks are the 40th to 15th weeks before; the earliest is EWC − 280 days. For EWC 3 Jan 2027 that is **Sun 29 Mar 2026**.

Baseline (qualifying) SMP case: expected 6 Jan 2027, employment began 1 Jan 2025, NWE 300, LEL 129, prescribed rate 194.32, question date 1 Nov 2026, not confined.

| # | Variation | Entitled? |
|---|---|---|
| C9 | baseline | yes |
| C10 | employment began 29 Mar 2026 (exactly 26 weeks) | yes |
| C11 | employment began 30 Mar 2026 | no |
| C12 | employment began 28 Mar 2026 | yes |
| C13 | NWE 129 (= LEL; "not less than") | yes |
| C14 | NWE 128.99 | no |
| C15 | question date 18 Oct 2026 (start of 11th week: "has reached ... the commencement") | yes |
| C16 | question date 17 Oct 2026 (Saturday before) | no |
| C17 | question date 10 Oct 2026, confined 5 Oct 2026 ("been confined before reaching") | yes |
| C18 | question date 17 Oct 2026, confined 17 Oct 2026 | yes |
| C19 | expected 10 Jan 2027 (Sunday), employment began 5 Apr 2026 (EWC − 280) | yes |
| C20 | expected 10 Jan 2027, employment began 6 Apr 2026 | no |
| C21 | expected 9 Jan 2027 (Saturday), employment began 5 Apr 2026 | no (EWC is 3 Jan; the limit is 29 Mar 2026) |
| C22 | expected 10 Jan 2027, question date 24 Oct 2026 | no (11th week begins 25 Oct) |

Rates. s 166(2): "a weekly rate equivalent to 90 per cent of a woman's normal weekly earnings"; s 166(1)(b) "whichever is the lower of the earnings-related rate and such weekly rate as may be prescribed".

| # | NWE | Prescribed | First 6 weeks | Remaining weeks |
|---|---|---|---|---|
| C23 | 300 | 194.32 | 270 | 194.32 |
| C24 | 200 | 194.32 | 180 | 180 |
| C25 | 215.91 | 194.32 | 194.319 | 194.319 |
| C27 | 1000 | 194.32 | 900 | 194.32 |
| C28 | 129 | 194.32 | 116.1 | 116.1 |

## Ambiguities and readings

1. Class 1 when earnings do not exceed a threshold: s 6(1) says no contribution is payable; I expect £0 (the encoding might REFUSE or return NOTHING; a numeric £0 is the natural "amount due").
2. Earnings above the UEL but the UEL below PT is not tested (incoherent input).
3. SSP daily amount with 0 qualifying days is undefined (division by zero); untested; expect REFUSE.
4. s 152(3) "not more than 8 weeks": 56 days between the periods links; 57 does not (brief's reading). Whether "week" here is the Sunday week of s 171-equivalent for Part XI is not addressed; the brief reads it as a span of days.
5. s 164(2)(c) "reached, or been confined before reaching": confinement on any date before the 11th week satisfies it; the question date is then irrelevant for limb (c). I assume confinement on or before the question date.
6. SMP rate remaining weeks when 90% equals the prescribed rate: either is the same number.
7. Employment edge: employment that began on the Sunday that starts the 40th week before (EWC − 280) gives exactly 26 weeks → qualifies.
8. The SMP "earliest start" is the Sunday starting the 11th week, regardless of the question date (s 165(2)).
