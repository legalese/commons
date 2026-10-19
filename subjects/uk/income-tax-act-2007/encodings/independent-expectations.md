# Independent expectations: Income Tax Act 2007 (UK)

Written from BRIEF.md and the source text only (ss 6-16, 23-25, 35, 55A-55C, 58, 414-415; I also read ss 27-29 and 56 because 55B/55C refer to them). No `.l4` file was opened before this file was saved.

## Inputs and conventions used throughout

- Rates as inputs: basic 20%, higher 40%, additional 45%; savings basic 20%, savings higher 40%, savings additional 45%.
- Fixed by the Act: dividend nil 0%, ordinary 10.75%, upper 35.75%, additional 39.35% (s 8); starting rate for savings 0%, limit £5,000 (ss 7, 12(3)); savings nil rate 0% (s 7(2)); PA £12,570, taper threshold £100,000 (s 35); BRL £37,700, HRL 2 x 12,570 + 100,000 = £125,140 (s 10(5), (5A)); transferable amount 10% of 12,570 = 1,257 rounded up to a multiple of £10 = £1,260 (s 55B(4)(b), (5)).
- Gift Aid grossed up at the basic rate (ss 58(2), 415): gross = net / (1 - 0.20) = net x 1.25.
- Adjusted net income = net income - grossed-up Gift Aid - gross relief-at-source pension contributions (s 58(1) Steps 1-3).
- BRL and HRL each increased by grossed-up Gift Aid (s 414(2)(b)) and gross pension contributions (s 10(6)(b), FA 2004 s 192(4)).
- Band positions are measured on income left after Step 3 (s 23 Step 4; s 10(2) "income up to the basic rate limit"). Stacking: non-savings, then savings, then dividends (s 16(3)-(5)). Nil-rate income (starting rate, savings nil rate, dividend nil rate) still occupies its slice of the bands (s 12A(3)/(4) "rather than the basic, higher or additional rate"; s 13A "rather than the dividend ordinary rate ...").
- Tax is not rounded (no rounding rule in these sections); values are exact.
- s 29(2): a tax reduction is deducted only so far as there is tax at Step 5 to deduct it from.

## Readings where I depart from (or sharpen) the brief

R1. **Order of allowances between savings and dividends (s 25(2), (3A)).** (3A) only requires the allowance to go against non-savings income first. Between savings and dividends, s 25(2) governs: "deduct the reliefs and allowances in the way which will result in the greatest reduction in the taxpayer's liability". The brief says "non-savings first, then savings, then dividends". Where the savings fit inside the starting-rate band, setting the allowance against dividends instead gives less tax, and the Act requires that. Scenarios T34 and T36 test this; I expect the Act's answer and give the brief's figure beside it.

R2. **Relinquishing party: the net-income test (s 55C(1)(d), (2)).** The condition that hypothetical net income is less than the personal allowance applies only "where the individual meets the requirements of section 56 ... by reason of meeting the condition in subsection (3) of that section" (non-residents: s 56(2)(b), (3)). Our seat is UK resident (s 56(2)(a)), so for us the only income test is 55C(1)(c)/(ca): with the reduced allowance, no tax above basic rate / dividend ordinary rate. The brief's "my net income is below my personal allowance" is therefore not a condition for the seat. Scenarios M11 and M13 test this; I expect "may elect" = TRUE.

R3. **Savings income in the higher/additional band and s 12B(8).** Read literally, 12B(8)(a)(i)/(b)(i) list "higher rate, property higher rate, default higher rate or dividend upper rate" but not the *savings* higher rate (s 11D). A literal reading would leave someone whose only income above the basic rate limit is savings income with a £1,000 allowance. I read "higher-rate income" purposively as income falling in the higher-rate band (including savings income charged at the savings higher rate, and savings that would be so charged but for s 12A), and likewise for additional-rate income. Scenarios T17, T19, T22 depend on this; the literal alternative is noted on each.

R4. **Gaining party with savings in the higher band at the savings nil rate (s 55B(2)(b)).** (b) lists the savings nil rate among permitted rates, and (ba) has a "but for s 13A" test only for dividends; there is no "but for s 12A" test for savings. So a gaining party whose income above the basic rate limit is all savings covered by the savings nil rate is entitled to the reduction (M8).

R5. **55B(6)** reduces the relinquishing party's allowance only if the spouse is entitled to the reduction. The scenarios assume the spouse is entitled when the relinquishing side is tested.

## Goal 1: personal allowance (ss 35, 58, 55B(6))

Working: excess = ANI - 100,000; PA = 12,570 - excess/2, rounded up to £1 (s 35(3)), not below nil.

| # | Facts | ANI | Expected PA | Working |
|---|---|---|---|---|
| P1 | net income 50,000 | 50,000 | 12,570 | no excess, s 35(1) |
| P2 | 100,000 | 100,000 | 12,570 | "exceeds £100,000" not met |
| P3 | 100,001 | 100,001 | 12,570 | 12,569.50 rounded up (s 35(3)) |
| P4 | 100,003 | 100,003 | 12,569 | 12,568.50 rounded up |
| P5 | 110,000 | 110,000 | 7,570 | 12,570 - 5,000 |
| P6 | 125,139 | 125,139 | 1 | 0.50 rounded up |
| P7 | 125,140 | 125,140 | 0 | 12,570 - 12,570 |
| P8 | 150,000 | 150,000 | 0 | not below nil |
| P9 | net 105,000, Gift Aid net 4,000 (gross 5,000) | 100,000 | 12,570 | s 58 Step 2 |
| P10 | net 120,000, pension gross 10,000 | 110,000 | 7,570 | s 58 Step 3 |
| P11 | net 112,000, GA net 2,000 (gross 2,500), pension 4,000 | 105,500 | 9,820 | 12,570 - 2,750 |
| P12 | net 10,000, elected to transfer | 10,000 | 11,310 | 12,570 - 1,260 (s 55B(6)) |

## Goal 2: income tax liability (ss 10, 12, 12A, 12B, 13, 13A, 16, 23, 25, 414)

Notation: ns/sv/dv = non-savings/savings/dividend income; t = taxable after PA.

### Non-savings only, and taper

| # | Facts | Expected tax | Working |
|---|---|---|---|
| T1 | wages 12,570 | 0 | t = 0 |
| T2 | wages 30,000 | 3,486 | 17,430 x 20% |
| T3 | wages 50,270 | 7,540 | 37,700 x 20% (at the BRL exactly) |
| T4 | wages 60,000 | 11,432 | 7,540 + 9,730 x 40% |
| T5 | wages 100,000 | 27,432 | t 87,430: 7,540 + 49,730 x 40% |
| T6 | wages 110,000 | 33,432 | PA 7,570, t 102,430: 7,540 + 64,730 x 40% |
| T7 | wages 125,140 | 42,516 | PA 0, t 125,140: 7,540 + 87,440 x 40% |
| T8 | wages 150,000 | 53,703 | 42,516 + 24,860 x 45% (s 10(3A)) |

### Gift Aid and pensions moving both taper and bands

| # | Facts | Expected tax | Working |
|---|---|---|---|
| T9 | wages 60,000, GA net 2,000 (gross 2,500) | 10,932 | BRL 40,200; t 47,430: 40,200 x 20% + 7,230 x 40% |
| T10 | wages 110,000, pension gross 10,000 | 29,432 | ANI 100,000, PA 12,570; BRL 47,700; t 97,430: 9,540 + 49,730 x 40% |
| T11 | wages 150,000, GA net 8,000 (gross 10,000) | 51,203 | ANI 140,000, PA 0; BRL 47,700, HRL 135,140: 9,540 + 87,440 x 40% + 14,860 x 45% |
| T35 | wages 50,000, savings 1,000, GA net 800 (gross 1,000) | 7,486 | BRL 38,700; t 38,430 below it, so no higher-rate income and SA 1,000; 37,430 x 20%; savings all nil-rate |

### Savings: starting rate and savings allowance

| # | Facts | Expected tax | Working and source |
|---|---|---|---|
| T12 | wages 15,000, savings 3,000 | 486 | ns t 2,430 x 20%; savings at 2,430-5,430: 2,570 starting rate (s 12), 430 savings nil (s 12A(3), SA 1,000) |
| T13 | wages 13,000, savings 10,000 | 972 | ns t 430 -> 86; starting rate 4,570 (partly used by ns); nil 1,000; 4,430 x 20% = 886 |
| T14 | savings 17,570 only | 0 | PA against savings, t 5,000 all at starting rate; s 12A(1)(a) not met |
| T15 | savings 20,000 only | 286 | t 7,430: 5,000 starting, 1,000 nil, 1,430 x 20% |
| T16 | wages 40,000, savings 1,000 | 5,486 | ns 27,430 x 20%; total t 28,430 < BRL so SA 1,000 (s 12B(4)); savings nil |
| T17 | wages 50,000, savings 1,000 | 7,686 | ns t 37,430 -> 7,486; total t 38,430 > BRL so higher-rate income, SA 500 (s 12B(3)); nil on lowest 500 (270 basic band + 230 higher band); 500 x 40% = 200. (Literal 12B(8), R3: SA 1,000, tax 7,486.) |
| T18 | wages 50,000, savings 270 | 7,486 (SA 1,000) | total t 37,700 = BRL, nothing above it |
| T19 | wages 50,000, savings 271 | 7,486 (SA 500) | total t 37,701: £1 would be higher-rate but for s 12A (12B(8)(b)(ii)), SA 500; 271 <= 500 all nil |
| T20 | wages 130,000, savings 2,000 | 45,603 | PA 0; ns: 7,540 + 34,976 + 4,860 x 45% = 44,703; SA nil (s 12B(2)); 2,000 x 45% = 900 |
| T21 | savings 200,000 only | 75,203 | PA 0; first 5,000 at starting rate (would otherwise be basic rate, s 12(1)); SA nil; 32,700 x 20% + 87,440 x 40% + 74,860 x 45% = 6,540 + 34,976 + 33,687 |
| T22 | wages 125,140, savings 100 | 42,561 | ANI 125,240, PA 0; savings above HRL -> additional-rate income, SA nil; 42,516 + 100 x 45%. (Literal R3: SA 500 -> 42,516.) |

### Dividends

| # | Facts | Expected tax | Working and source |
|---|---|---|---|
| T23 | wages 20,000, dividends 400 | 1,486 | 7,430 x 20%; D = 400 < 500, Rule 1C nil |
| T24 | wages 20,000, dividends 5,000 | 1,969.75 | 1,486 + 4,500 x 10.75% (Rule 1A) |
| T25 | wages 60,000, dividends 5,000 | 13,040.75 | 11,432 + all upper: U 5,000, Rule 2A nil 500, 4,500 x 35.75% = 1,608.75 |
| T26 | wages 50,070, dividends 1,000 | 7,678.75 | ns t 37,500 -> 7,500; D = 200, U = 800; nil 200 of D (1C) + first 300 of U (2A); 500 x 35.75% = 178.75 |
| T27 | wages 140,000, dividends 10,000 | 52,941.25 | PA 0; ns 42,516 + 14,860 x 45% = 49,203; A = 10,000: nil 500 (3A), 9,500 x 39.35% = 3,738.25 |
| T28 | wages 124,940, dividends 1,000 | 42,632.75 | PA 0; ns 7,540 + 87,240 x 40% = 42,436; U = 200 (2C nil), A = 800: first 300 nil (3A), 500 x 39.35% = 196.75 |
| T29 | wages 30,000, dividends 30,000 | 9,089.75 | ns 17,430 -> 3,486; D = 20,270: 500 nil, 19,770 x 10.75% = 2,125.275; U = 9,730 x 35.75% = 3,478.475 |
| T30 | dividends 13,070 only | 0 | PA 12,570 against dividends; 500 nil |

### Savings and dividends together

| # | Facts | Expected tax | Working and source |
|---|---|---|---|
| T31 | wages 35,000, savings 2,000, dividends 1,000 | 4,739.75 | ns t 22,430 -> 4,486; total t 25,430 < BRL, SA 1,000; savings 1,000 nil + 1,000 x 20%; div 500 nil + 500 x 10.75% |
| T32 | wages 47,570, savings 2,000, dividends 1,000 | 7,428.75 | ns t 35,000 -> 7,000; total t 38,000: dividends (top) cross BRL, so higher-rate income, SA 500 (12B(8)(b)(i),(iii)); savings 500 nil + 1,500 x 20%; div D 700 (500 nil, 200 x 10.75% = 21.50), U 300 x 35.75% = 107.25 |
| T33 | wages 14,570, savings 6,000, dividends 2,000 | 961.25 | ns t 2,000 -> 400; savings 3,000 starting rate, 1,000 nil, 2,000 x 20%; div 500 nil, 1,500 x 10.75% |
| T34 | savings 5,000, dividends 20,000 | 744.975 | R1: PA against dividends (s 25(2)): savings 5,000 at starting rate; dividends t 7,430: 500 nil, 6,930 x 10.75%. (Brief order, PA against savings first: 1,282.475.) |
| T36 | savings 3,000, dividends 15,000 | 207.475 | R1: PA against dividends: dividends t 2,430: 500 nil, 1,930 x 10.75%; savings at starting rate. (Brief order: 529.975.) |

## Goal 3: marriage allowance (ss 55B, 55C)

| # | Facts | Expected | Working and source |
|---|---|---|---|
| M1 | transferable amount | 1,260 | 10% x 12,570 = 1,257, rounded up to £10 (55B(4)(b), (5)) |
| M1b | reduction amount | 252 | basic rate 20% x 1,260 (55B(1), (3)) |
| M2 | gaining, wages 20,000 | entitled; tax 1,234 | 1,486 - 252 |
| M3 | gaining, wages 13,000 | entitled; reduction 86; tax 0 | Step 5 tax 86 < 252; s 29(2) caps it |
| M4 | gaining, wages 50,270 | entitled; tax 7,288 | all at basic rate; 7,540 - 252 |
| M5 | gaining, wages 50,271 | not entitled; tax 7,540.40 | £1 at the higher rate (55B(2)(b)) |
| M6 | gaining, wages 50,070, dividends 200 | entitled; tax 7,248 | all dividends D, nil-rate; 7,500 - 252 |
| M7 | gaining, wages 50,070, dividends 300 | not entitled; tax 7,500 | 100 would be at the dividend upper rate but for s 13A (55B(2)(ba)) |
| M8 | gaining, wages 50,170, savings 400 | entitled; tax 7,268 | ns t 37,600 -> 7,520; SA 500; all 400 nil-rate, 300 above BRL but savings nil rate is a permitted rate and there is no "but for 12A" limb (R4); 7,520 - 252 |
| M17 | gaining, wages 12,570, savings 3,000 | entitled; reduction 0; tax 0 | only starting rate; nothing to deduct from |
| M9 | relinquishing, wages 10,000 | may elect; PA 11,310; tax 0 | |
| M10 | relinquishing, wages 12,000 | may elect; tax 138 | t 690 x 20% |
| M13 | relinquishing, wages 12,570 | may elect (R2); tax 252 | net income not below PA, but 55C(2) does not apply to a UK resident (55C(1)(d)); t 1,260 at basic rate. (Brief: may not elect.) |
| M14 | relinquishing, wages 10,000, dividends 2,000 | may elect; tax 20.425 | PA 11,310: ns t 0, div t 690: 500 nil, 190 x 10.75% |
| M11 | relinquishing, wages 49,000 | may elect (R2); tax 7,538 | reduced PA 11,310: t 37,690 <= BRL (55C(1)(c)). (Brief: may not elect, net income >= PA.) |
| M12 | relinquishing, wages 49,100 | may NOT elect | without the transfer t 36,530 (tax 7,306, all basic); with the reduced PA t 37,790, £90 above the BRL at the higher rate, so 55C(1)(c) fails |
