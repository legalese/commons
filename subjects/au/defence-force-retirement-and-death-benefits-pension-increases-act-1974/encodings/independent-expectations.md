# Independent expectations: Defence Force Retirement and Death Benefits (Pension Increases) Act 1974

Written from BRIEF.md and `../registers/source-bundle/C2004A00163.txt` only, before any `.l4` file was opened. Index figures are hypothetical test inputs (the Act takes them from the Statistician).

## Prescribed percentage (s 3)

"whichever is the lower of (a) 1.4 times the percentage that represents A-B expressed as a percentage of B; or (b) the percentage that represents C-D expressed as a percentage of D", then s 3(3): a fraction of one-tenth "less than one-half of one-tenth" is disregarded, "not less than one-half" is treated as one-tenth. I read s 3(3) as applying to the prescribed percentage, i.e. after the lower is chosen.

| # | A, B, C, D | Working | Expected % |
|---|-----------|---------|-----------|
| P1 | 120, 100, 115, 100 | (a) 1.4 x 20 = 28; (b) 15; lower 15 | 15 |
| P2 | 104, 100, 110, 100 | (a) 1.4 x 4 = 5.6; (b) 10 | 5.6 |
| P3 | 120, 100, 104.25, 100 | (b) 4.25: fraction 0.05 is not less than half a tenth | 4.3 |
| P4 | 120, 100, 104.24, 100 | 4.24 -> 4.2 | 4.2 |
| P5 | 120, 100, 104.26, 100 | 4.26 -> 4.3 | 4.3 |
| P6 | 103.03, 100, 110, 100 | (a) 1.4 x 3.03 = 4.242 -> 4.2 | 4.2 |

## Gate (ss 7, 16)

| # | Inputs | Expected |
|---|--------|----------|
| G1 | A = B = 100 (C > D) | no increase under either Part ("exceeds" is strict) |
| G2 | C = D (A > B) | no increase |
| G3 | DFRB pension payable to or in respect of an eligible child (Part II) | no increase: s 7 "(not being a pension payable to or in respect of an eligible child)" |

## Amounts (with P1 indices, 15%, unless stated)

| # | Case | Inputs | Working | Expected annual increase |
|---|------|--------|---------|--------------------------|
| 1 | s 8 | before 1 Jul 1974 $2,000; before 1 Jul 1973 $1,800 | 15% x (2000 - 0.225 x 1800) = 15% x 1595 | $239.25 |
| 2 | s 8 at P3 (4.3%) | same | 4.3% x 1595 | $68.585 |
| 3 | s 9, payable from 1 Jul 1973 | $1,200 | 15% x 77.5% x 1200 = 139.5; 12 months | $139.50 |
| 4 | s 9, payable from 1 Jan 1974 | $1,200 | exactly 6 months | 139.5 x 6/12 = $69.75 |
| 5 | s 9, payable from 16 Jan 1974 | $1,200 | 5 whole months (16 Jan-15 Jun) + 16-30 Jun = 15 days of June's 30: not less than half -> 6 months | $69.75 |
| 6 | s 9, payable from 17 Jan 1974 | $1,200 | 5 months + 14 days (< 15) disregarded -> 5 | 139.5 x 5/12 = $58.125 |
| 7 | s 9, payable from 15 Jun 1974 | $1,200 | 16 days, less than 1 month -> 1 (s 9(4)) | 139.5/12 = $11.625 |
| 8 | s 9, payable from 16 Jun 1974 | $1,200 | "not being a pension that became payable after 15 June 1974": s 9 does not apply | no increase |
| 9 | s 17 member/widow | $1,400 | 15% x 71.43% x 1400 = 15% x 1000.02 | $150.003 |
| 10 | s 17 child's pension, additional pension $500 (total $900) | | 15% x 71.43% x 500 = 15% x 357.15 | $53.5725 |
| 11 | s 18 retirement 31 Dec 1973 | $1,400 | period from 1 Jan 1974 = 6 months | 150.003 x 6/12 = $75.0015 |
| 12 | s 18 retirement 1 Jul 1973 | $1,400 | from 2 Jul 1973: 11 months to 1 Jun + 2-30 Jun = 29 days -> 12 | $150.003 |
| 13 | s 18 death 14 Jun 1974 | $1,400 | from 15 Jun: 16 days -> 1 month | 150.003/12 = $12.50025 |
| 14 | s 18(1)(b) s 78 benefit payable from 1 Mar 1974 | $1,400 | from the day payable: 4 months | 150.003 x 4/12 = $50.001 |
| 15 | s 18 child's pension, retirement 31 Dec 1973, additional $500 | | 53.5725 x 6/12 | $26.78625 |

## Date of effect (ss 13, 22)

Every increase applies from the instalment due on the pension pay-day of 4 July 1974.

## Where my reading differs from, or goes beyond, the brief

- **s 18 start**: for s 18(1)(a) the period begins "on the day after the day on which the relevant retirement or death ... took place"; for s 18(1)(b) "on the day on which the pension benefit ... became payable". The brief says the input is "the first day of the counted period", which pushes the day-after step to the caller. I test both ways where the module allows.
- **s 18 cut-off**: the 15 June 1974 limit is on when the *benefit became payable*, not the retirement date. A retirement on 14 Jun 1974 with the benefit payable on 15 Jun is in; the module may not separate these.
- **s 8(2)(a)(ii),(iii) and (b)**: the 22.5% is of a notional 1973 amount (re-classification, commutation, widow whose husband retired before 1 Oct 1972). The caller supplies the 1973 figure; I assume the input is that notional amount.
- **Rounding of money**: none stated; results kept exact.
- **Part-month month**: s 9(5)/18(6) compare the days in the part month with "the number of days in that month". I take the month in which the part falls (June for periods ending 30 June counted forward).
