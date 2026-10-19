# Independent expectations: Superannuation (Pension Increases) Act 1961

Written from BRIEF.md and the deposited source only, before reading any `.l4` file. Amounts in pounds (£32 10s = 32.5).

## Readings of the Act

- s 4(1): increase arises only "where the adjusted unit entitlement ... exceeds his actual unit entitlement"; it equals prescribed amount × additional unit entitlement (adjusted − actual). Equal or lower adjusted → no increase.
- "the prescribed amount" (s 3(1)):
  - (a) 32.5, for anyone not within (b), (c) or (d).
  - (b) actual unit contribution < actual unit entitlement and s 52 did **not** apply: 32.5 × contribution / entitlement.
  - (c) s 52 applied **and** the pensioner neglected/elected not to contribute: 32.5 × contribution / (scale units under (a)(i) − s 52(1)(b) units).
  - (d) pension under the s 29 proviso, s 60M or s 60O(2)(a): the amount otherwise applicable × (actual annual pension / notional s 29 pension).
  - **Divergence from the brief**: the brief says the deposited text truncates (c) and (d). It does not: both are given in full above. They depend on extra facts (s 52(1)(b) units; the notional s 29 pension), so taking each as an input fraction is a reasonable modelling shortcut, but it is a choice, not a truncation.
  - Edge the Act creates: s 52 applied, no neglect, contribution < entitlement → neither (b) (excluded by s 52) nor (c) (needs neglect) applies, so (a) 32.5. Whether the encoding can express this depends on how the case is chosen.
- s 4(2): where increased under s 11 of the 1957 Act, entitlement only "to the extent that" the s 4(1) increase exceeds the 1957 increase → max(0, increase − 1957 increase).
- s 4(4): widow gets "five-eighths of the increase in pension to which her husband would have been entitled under that subsection" (s 4(1)). I read the base as the s 4(1) figure. Whether the husband's own s 4(2) 1957 reduction carries through is not clear from the text; I do not test that combination.
- s 4(6): no increase for (a) a child's pension; (b) s 57 pension unless State Fund contributions; (c) s 53 or s 58 pension.
- s 7(1): increases have effect "from and including the first fortnightly payment of pensions made after the commencing date".

## Scenarios

| # | Facts | Expected | Act's words |
|---|---|---|---|
| B1 | adjusted 10, actual entitlement 6, contribution 6, case (a) | 130 (32.5 × 4) | s 4(1); prescribed amount (a) |
| B2 | adjusted 6 = actual 6 | 0 | "exceeds" |
| B3 | adjusted 5 < actual 6 | 0 | "exceeds" |
| B4 | adjusted 10, entitlement 6, contribution 4, case (b) | prescribed 65/3; increase 260/3 | (b) "same proportion as his actual unit contribution bears to his actual unit entitlement" |
| B5 | B1 with 1957 increase 50 | 80 | s 4(2) "except to the extent that ... exceeds" |
| B6 | B1 with 1957 increase 200 | 0 (not negative) | s 4(2) |
| B7 | B1 with 1957 increase exactly 130 | 0 | s 4(2) |
| B8 | widow; husband's s 4(1) increase would be 130 (adjusted 10, actual 6, case (a)) | 325/4 (81.25) | s 4(4) "five-eighths" |
| B9 | B1 but a child's pension | 0 | s 4(6)(a) |
| B10 | B1 but s 58 pension | 0 | s 4(6)(c) |
| B11 | B1 but s 57 pension without State Fund contributions | 0 | s 4(6)(b) |
| B12 | case (c), input fraction 1/2, adjusted 10, actual 6 | prescribed 65/4; increase 65 | (c) |
| B13 | case (d), input fraction 3/4 on a base of (a), adjusted 10, actual 6 | prescribed 195/8; increase 195/2 | (d) |
| B14 | first fortnightly payment after commencement on a given date D | increase has effect from D | s 7(1) |
| B15 | s 52 applied, no neglect, contribution 4 < entitlement 6 | prescribed 32.5 (case (a)) | (b) excludes s 52; (c) needs neglect |
