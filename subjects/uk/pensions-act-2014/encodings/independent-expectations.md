# Independent expectations: Pensions Act 2014 (state pension, deferral, bereavement support payment)

Written from BRIEF.md and the Act text (ss 1-5, 17, 30-31, Sch 1) only, before any `.l4` file was opened.

## Fixed numbers used throughout (chosen so answers are exact)

- Full rate on 6 April 2016 (`F16`): **140**.
- Full rate on the day of pensionable age (`FPA`): **175** (a 25% increase since 6 April 2016).
- Revaluing percentage for prices (Sch 1 para 6(5)(b)): **10%**.
- Minimum number of qualifying years (ss 2(3), 4(2)): **10** unless stated.
- Pensionable age day: **1 June 2030** unless stated.

## Readings adopted

1. s 1(2) "reaches pensionable age before 6 April 2016": strictly before. A person reaching it on 6 April 2016 is inside Part 1.
2. s 2 "qualifying years" counts every qualifying year, pre- and post-commencement (s 2(4) defines a qualifying year by earnings factor, without a date limit). So a person with pre-commencement years who fails s 4 also fails s 2 (the minimum is the same number).
3. s 4(1)(b) "the minimum number of qualifying years" is measured over pre + post years (s 4(5) adds reckonable years, which are counted inside the pre-commencement input).
4. s 4(3): a person within s 4 is never on s 2, even if they have 35+ years.
5. Sch 1 para 4(2)/(3): the 35-year test and the N/35 proportion use the pre-commencement years only.
6. Sch 1 para 6(4): "increasing it by the same percentage as any increase in the full rate" in the period 6 April 2016 to pensionable age = multiply by FPA / F16.
7. Sch 1 para 6(3): the part up to F16 is revalued with the full rate (so becomes FPA); the excess over F16 becomes excess × (1 + revaluing percentage).
8. Sch 1 para 7: post amount = FPA if 35+ post years, otherwise (N/35) × FPA.
9. s 5(1): rate = max( min(pre amount + post amount, FPA), pre amount ).
10. s 17(3): whole weeks = floor((last day − first day + 1) / 7) (brief).
11. s 17(2): the increase is not given if it is *less than* 1% of the weekly rate; exactly 1% counts.
12. s 17(4): increment = percentage × weekly rate (the rate before the end of deferral is the input weekly rate); increase = weeks × increment.
13. s 30(1)(b) "under pensionable age when the [partner] dies": a person whose pensionable age day is the day of the death has reached it, so is not under it. Death the day before → under.
14. s 31(1)(b) "equal to or greater than 25 times the lower earnings limit": equality meets it.
15. s 31(1)(a) "actually paid": credited (not paid) contributions do not count.
16. s 30(6): the section came fully into force on **6 April 2017** (Pensions Act 2014 (Commencement No. 10) Order 2017). The Act does not print this date; it is an external fact. Death 5 April 2017 → not entitled; 6 April 2017 → entitled (if otherwise eligible).
17. s 30(6B): two people are cohabiting partners only if NOT married to / civil partners of each other but living together as if they were. A cohabiting partner needs (aa): pregnant or entitled to child benefit. A spouse/civil partner does not.

## Ambiguities

- A1. s 30(6): commencement date not in the text (reading 16). An encoding might take it as input or `REFUSE`; I assert 6 April 2017 where the API allows.
- A2. s 2 vs s 4 minimum: two separate regulation-set numbers; the brief has one input. I use one.
- A3. Step 2 can be negative after the contracting-out deduction; Step 3 takes the higher of Steps 1 and 2, so the foundation is Step 1. (No floor at 0 needed when Step 1 ≥ 0.)
- A4. s 1(2) person not entitled: is that "none" or REFUSE? It is a positive "not entitled" in the Act: **none**.
- A5. Whether a deferral period that is not a whole week yields an increment: s 18(1) regulations may treat part weeks as whole; out of scope, so floor.

## Goal 1: entitlement kind (PA = pensionable age day; pre / post = qualifying years)

| # | PA day | pre | post | min | Expected | Act |
|---|---|---|---|---|---|---|
| E1 | 5 Apr 2016 | 0 | 40 | 10 | none | s 1(2) "before 6 April 2016 is not entitled" |
| E2 | 5 Apr 2016 | 35 | 0 | 10 | none | s 1(2) |
| E3 | 6 Apr 2016 | 35 | 0 | 10 | transitional | s 1(2) strictly before; s 4(1) |
| E4 | 1 Jun 2030 | 0 | 35 | 10 | full | s 2(1)(b) "35 or more" |
| E5 | 1 Jun 2030 | 0 | 40 | 10 | full | s 2(1) |
| E6 | 1 Jun 2030 | 0 | 34 | 10 | reduced | s 2(2)(b) "fewer than 35" |
| E7 | 1 Jun 2030 | 0 | 10 | 10 | reduced | s 2(2)(b) "at least the minimum" |
| E8 | 1 Jun 2030 | 0 | 9 | 10 | none | s 2(2)(b) |
| E9 | 1 Jun 2030 | 1 | 9 | 10 | transitional | s 4(1)(b),(c) |
| E10 | 1 Jun 2030 | 1 | 8 | 10 | none | s 4(1)(b) fails; s 2(2)(b) fails |
| E11 | 1 Jun 2030 | 1 | 40 | 10 | transitional (not full) | s 4(3) |
| E12 | 1 Jun 2030 | 0 | 7 | 7 | reduced | min 7 |
| E13 | 1 Jun 2030 | 0 | 0 | 10 | none | |

## Goal 1: weekly rate

Reduced / full (s 3(2): N/35 × full rate; FPA = 175):

| # | pre | post | Expected rate | Working |
|---|---|---|---|---|
| R1 | 0 | 20 | 100 | 20/35 × 175 |
| R2 | 0 | 10 | 50 | 10/35 × 175 |
| R3 | 0 | 34 | 170 | 34/35 × 175 |
| R4 | 0 | 35 | 175 | full |
| R5 | 0 | 40 | 175 | full |
| R6 | 0 | 9 | none / no rate | not entitled |
| R7 | 0 | 12 (FPA 200) | 480/7 (= 12 × 200 / 35) | non-terminating |

Transitional (F16 = 140, FPA = 175, revaluing 10%, old = Step 1 input, COD = contracting-out amount):

| # | pre | post | old | COD | Step 2 | Foundation | Pre amount (Step 4) | Post amount | Expected rate |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 35 | 0 | 120 | 0 | 140 | 140 | 175 | 0 | 175 |
| T2 | 35 | 0 | 120 | 20 | 120 | 120 | 150 | 0 | 150 |
| T3 | 28 | 5 | 100 | 10 | 102 | 102 | 127.5 | 25 | 152.5 |
| T4 | 20 | 10 | 90 | 0 | 80 | 90 | 112.5 | 50 | 162.5 |
| T5 | 35 | 0 | 160 | 10 | 130 | 160 | 175 + 20×1.1 = 197 | 0 | 197 (5(1)(b)) |
| T6 | 35 | 3 | 160 | 10 | 130 | 160 | 197 | 15 | 197 (sum 212 capped 175; (b) 197 higher) |
| T7 | 30 | 10 | 0 | 0 | 120 | 120 | 150 | 50 | 175 (cap) |
| T8 | 1 | 9 | 3 | 0 | 4 | 4 | 5 | 45 | 50 |
| T9 | 10 | 5 | 50 | 50 | −10 | 50 | 62.5 | 25 | 87.5 |
| T10 | 5 | 35 | 20 | 0 | 20 | 20 | 25 | 175 | 175 (cap) |
| T11 | 40 | 0 | 100 | 0 | 140 (35+ branch) | 140 | 175 | 0 | 175 |
| T12 | 35 | 0 | 150 | 0 | 140 | 150 | 175 + 10×1.1 = 186 | 0 | 186 |
| T13 | 14 | 0 | 50 | 0 | 56 | 56 | 70 | 0 | 70 |
| T14 | 35 | 0 | 150 | 0 (FPA = 140) | 140 | 150 | 140 + 11 = 151 | 0 | 151 |
| T15 | 10 | 3 | 30 | 0 | 40 | 40 | 50 | 15 | 65 |

Component checks (where the encoding exposes them): T3 Step 2 = 102, foundation 102, pre amount 127.5, post 25. T5 pre amount 197. T9 foundation 50.

## Goal 2: deferral (s 17)

Whole weeks (counting both days):

| # | first day | last day | days | weeks |
|---|---|---|---|---|
| W1 | 1 Jan 2025 | 7 Jan 2025 | 7 | 1 |
| W2 | 1 Jan 2025 | 6 Jan 2025 | 6 | 0 |
| W3 | 1 Jan 2025 | 1 Jan 2025 | 1 | 0 |
| W4 | 1 Jan 2025 | 31 Dec 2025 | 365 | 52 |
| W5 | 1 Jan 2024 | 31 Dec 2024 | 366 | 52 |
| W6 | 1 Feb 2024 | 28 Feb 2024 | 28 | 4 |
| W7 | 1 Feb 2024 | 29 Feb 2024 | 29 | 4 |
| W8 | 1 Mar 2025 | 14 Mar 2025 | 14 | 2 |
| W9 | 1 Mar 2025 | 13 Mar 2025 | 13 | 1 |
| W10 | 6 Apr 2030 | 5 Apr 2031 | 365 | 52 |
| W11 | 1 Jan 2025 | 4 Jan 2027 | 734 | 104 |

Increase (weekly rate 175):

| # | weeks (dates) | increment % | Expected increase | Expected increased rate | Act |
|---|---|---|---|---|---|
| I1 | 52 (W4) | 0.2 | 18.2 | 193.2 | s 17(1),(3),(4) |
| I2 | 4 (W6) | 0.2 | 0 (1.4 < 1.75) | 175 | s 17(2) |
| I3 | 5 (1-35 Jan... 1 Jan-4 Feb 2025, 35 days) | 0.2 | 1.75 (exactly 1%) | 176.75 | s 17(2) "less than" |
| I4 | 9 (63 days: 1 Jan-4 Mar 2025) | 1/9 | 1.75 (exactly 1%) | 176.75 | |
| I5 | 8 (56 days: 1 Jan-25 Feb 2025) | 1/9 | 0 | 175 | |
| I6 | 52 (W4) | 1/9 | 91/9 | 175 + 91/9 | |
| I7 | 0 (W2) | 0.2 | 0 | 175 | |
| I8 | 104 (W11), rate 200 | 1/9 | 2080/90 = 208/9 | 200 + 208/9 | |

Increment amount (s 17(4)) at 175 and 0.2%: 0.35.

## Goal 3: bereavement support payment (ss 30-31)

Base case B0: spouse died 1 June 2025; claimant's pensionable age 1 June 2040; resident in GB; deceased paid Class 1 in one year with earnings factor 10 000 and LEL 6 396 × ... (use LEL 100, EF 3000 ≥ 2500); not pregnant, no child benefit. Expected **entitled**.

| # | Variation from B0 | Expected | Act |
|---|---|---|---|
| B1 | none | entitled | s 30(1) |
| B2 | civil partner | entitled | s 30(1)(a) |
| B3 | cohabiting partner, not pregnant, no child benefit | not entitled | s 30(1)(aa) |
| B4 | cohabiting partner, pregnant | entitled | s 30(1)(aa) |
| B5 | cohabiting partner, entitled to child benefit | entitled | s 30(1)(aa) |
| B6 | spouse, no child benefit (as B1) | entitled — (aa) applies only to cohabiting partner | |
| B7 | claimant's PA day = day of death (1 June 2025) | not entitled | s 30(1)(b) "under pensionable age" |
| B8 | claimant's PA day = 2 June 2025 | entitled | |
| B9 | claimant's PA day before death (1 Jan 2025) | not entitled | |
| B10 | not ordinarily resident in GB or specified territory | not entitled | s 30(1)(c) |
| B11 | resident in a specified territory (not GB) | entitled | s 30(1)(c) |
| B12 | EF exactly 2500 (= 25 × 100) | entitled | s 31(1)(b) "equal to or greater" |
| B13 | EF 2499 | not entitled | s 31(1)(b) |
| B14 | EF 3000 but contributions not actually paid (credited) | not entitled | s 31(1)(a) |
| B15 | Class 2 actually paid, EF 2500 | entitled | s 31(1)(a) |
| B16 | two years: (paid, 2000) and (paid, 2600); LEL 100 | entitled | "at least one tax year" |
| B17 | two years: (paid, 2400), (not paid, 5000) | not entitled | |
| B18 | no contribution year; deceased employed earner, died from industrial injury (s 94) | entitled | s 31(3)(a) |
| B19 | no contribution year; employed earner, prescribed industrial disease (s 108) | entitled | s 31(3)(b) |
| B20 | no contribution year; not employed earner, industrial-type injury | not entitled | s 31(3) "was an employed earner" |
| B21 | no contribution year; employed earner, no industrial cause | not entitled | |
| B22 | death 5 April 2017 | not entitled | s 30(6) |
| B23 | death 6 April 2017 | entitled | s 30(6) (commencement 6 April 2017) |
| B24 | LEL differs per year: year (paid, EF 3000, LEL 130) fails (3250); year (paid, EF 2000, LEL 80) meets (2000) | entitled | "for the tax year" |
| B25 | cohabiting partner, pregnant, but contribution condition fails | not entitled | s 30(1)(d) |
