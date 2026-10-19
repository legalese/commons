# Independent expectations: Superannuation (Pension Increases) Act 1967

Written from BRIEF.md and `../registers/source-bundle/C1967A00090.txt` only, before reading any `.l4` file.

## Working conventions

- additional unit entitlement = adjusted unit entitlement − actual unit entitlement, if positive (s 3).
- s 4(1): increase = relevant amount × additional units, only "where the adjusted unit entitlement ... exceeds his actual unit entitlement".
- relevant amount (s 3): (a) $65; (b) actual unit contribution < actual unit entitlement (s 52 not applied, (d)/(e) not applying): $65 × contribution ÷ entitlement; (c)-(e): a proportion of $65, taken as an input fraction (brief).
- s 4(2): the s 4(1) amount less the sum of earlier increases (s 11 of the 1957 Act, s 4 of the 1961 Act, s 26 of the 1963 Act), not below nil.
- s 4(3): widow: (c) one-half if the husband elected that s 26 of the 1922-1959 Act not apply and did not revoke; (d) otherwise five-eighths, of the husband's s 4(1) increase.
- s 4(4): no increase for a pension under s 53 or s 58, or s 57 unless contributions were made to a State Fund.

Unless stated: actual unit contribution 6, actual unit entitlement 6, adjusted 8, case (a), no earlier increases, not a widow, not excluded.

## Scenarios

| # | Facts | Expected increase ($ a year) | Working | Act's words |
|---|---|---|---|---|
| 1 | Defaults | 130 | additional 2; 65 × 2 | s 4(1) "the relevant amount ... multiplied by a number equal to the number of units ... in his additional unit entitlement"; s 3 relevant amount (a) "Sixty-five dollars" |
| 2 | adjusted 6 = actual 6 | 0 | adjusted does not exceed actual | s 4(1) "Where the adjusted unit entitlement ... exceeds" |
| 3 | adjusted 5 < actual 6 | 0 | no additional units | s 3 "additional unit entitlement ... by which ... exceeds" |
| 4 | case (b): contribution 4, entitlement 6, adjusted 9 | 130 | relevant amount 65 × 4/6 = 43⅓; × 3 = 130 | s 3 relevant amount (b) "the same proportion as his actual unit contribution bears to his actual unit entitlement" |
| 5 | case (b): contribution 5, entitlement 6, adjusted 7 | 325/6 (54.1666…) | 65 × 5/6 × 1 | s 3 (b) |
| 6 | case (c)-(e) with fraction 1/2, adjusted 8, actual 6 | 65 | 32.5 × 2 | s 3 (c)-(e) "such amount as bears to the amount of Sixty-five dollars the same proportion ..." |
| 7 | earlier increases total 50 | 80 | 130 − 50 | s 4(2) "except to the extent that the amount ... exceeds the sum" |
| 8 | earlier increases 30 + 20 + 10 (three Acts) | 70 | 130 − 60 | s 4(2) "the sum of the amounts ... respectively" |
| 9 | earlier increases 130 | 0 | 130 − 130; "exceeds" not met | s 4(2) |
| 10 | earlier increases 200 | 0 (not negative) | floor at nil | s 4(2) |
| 11 | widow, other case, husband's figures = defaults | 81.25 | 5/8 × 130 | s 4(3)(d) "five-eighths" |
| 12 | widow, husband elected s 26 not to apply, not revoked | 65 | 1/2 × 130 | s 4(3)(c) "one-half" |
| 13 | widow, other case, husband's earlier increases 50 | 50 | my reading: the husband "would have been entitled under subsection (1)" only to 130 − 50 = 80 (s 4(2) limits what he is entitled to under (1)); 5/8 × 80 = 50 | s 4(2), 4(3) |
| 14 | pension under s 53 | 0 | excluded | s 4(4)(b) |
| 15 | pension under s 58 | 0 | excluded | s 4(4)(b) |
| 16 | pension under s 57, no State Fund contributions | 0 | excluded | s 4(4)(a) |
| 17 | pension under s 57, State Fund contributions made | 130 | not excluded | s 4(4)(a) "not being a pension for which contributions were made to a State Fund" |
| 18 | widow, pension under s 58 | 0 | excluded | s 4(4) "The increases ... provided for by this section do not apply" |

## Where I read the Act differently from the brief, or the brief is silent

- **s 4(2) and widows (scenario 13).** The brief says s 4(2) reduces "the increase" but not whose. s 4(3) gives the widow a fraction of "the increase ... to which her husband would have been entitled under subsection (1)", and s 4(2) says a pensioner "is not entitled to an increase under the last preceding subsection except to the extent ...", so I take the husband's earlier increases to come off before the fraction is applied. Another reading (fraction first, then subtract increases on the widow's own pension) is possible; s 4(2) speaks only of an "eligible pensioner", which a widow is not. Flagged as an ambiguity.
- **Relevant amount (b) when contribution ≥ entitlement.** Falls back to (a): $65.
- **Actual unit entitlement** is defined as the greater of the scale units and the actual unit contribution, so contribution can never exceed entitlement; the brief treats it as an input.
- **s 7(1)** (effect from the first fortnightly payment after the commencing date): the commencing date (date of Royal Assent) is not in the deposited text, so I set no date expectation.
