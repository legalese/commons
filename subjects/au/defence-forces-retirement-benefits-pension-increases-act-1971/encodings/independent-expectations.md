# Independent expectations: Defence Forces Retirement Benefits (Pension Increases) Act 1971

Written from BRIEF.md and `../registers/source-bundle/C1971A00074.txt` only, before any `.l4` file was opened. Pension rates are annual dollar figures chosen for the test; the s 3 definitions that turn on the DFRB Act's scales are inputs.

| # | Scenario | Inputs | Working | Expected increase |
|---|----------|--------|---------|-------------------|
| 1 | s 5 basic case | current 1400, actual 1000, basic 700 | "where the pension at current rate ... exceeds his actual pension entitlement ... five-sevenths of the difference between the pension at current rate ... and his basic pension entitlement": 5/7 x (1400 - 700) | 500 |
| 2 | s 5, exact fraction | current 1300, actual 1200, basic 1000 | 5/7 x 300 | 1500/7 (= 214.2857...) |
| 3 | s 5 trigger not met: current equals actual | current 1000, actual 1000, basic 700 | "exceeds" is strict | none |
| 4 | s 5 trigger not met: current below actual | current 1000, actual 1050, basic 700 | | none |
| 5 | s 8 commutation | case 1 + commuted: payable 800, uncommuted 1000 | 500 x 800/1000 | 400 |
| 6 | s 8 election under s 61A/61B | as 5 | same proportion | 400 |
| 7 | s 10 earlier increases | case 1 + earlier increases 120 | 500 - 120 | 380 |
| 8 | s 10 earlier increases exceed | case 1 + earlier 600 | reduced to nil (the brief: not below nil) | 0 / none |
| 9 | s 8 then s 10 | case 5 + earlier 120 | s 10 reduces "any increase ... under the preceding provisions", which include s 8: 400 - 120 | 280 (not (500 - 120) x 0.8 = 304) |
| 10 | s 11 reduced-pension pensioner | any | Minister for Finance determines the rate | NOTHING |
| 11 | s 12(1) widow | husband: current 1400, actual 1000, basic 700 | 5/8 x 500 | 312.5 |
| 12 | s 12(1) widow, husband commuted under s 74 | husband as 11, payable 800 / uncommuted 1000 | s 8 "disregarded in so far as it applies by reason of the commutation": 5/8 x 500 | 312.5 |
| 13 | s 12(1) widow, husband had earlier increases 120 | | s 10 is not disregarded: 5/8 x 380 | 237.5 |
| 14 | s 12(2) election widow | husband as 11 | one-half x 500 | 250 |
| 15 | s 12 widow, husband's s 5 trigger not met | husband current 1000 = actual 1000 | husband would get no increase | none |
| 16 | s 13 widow | any | Minister determines | NOTHING |
| 17 | s 21 date of effect | first fortnightly payment after commencement (input) | "from and including the first fortnightly payment of pensions made after the commencing date" | that date |

## Where my reading differs from, or goes beyond, the brief

- **s 12 and a husband's s 61A/61B election.** s 12(1) disregards s 8 only "in so far as it applies by reason of the commutation" under s 74. If the husband's s 8 reduction came from an election under s 61A or s 61B, s 8 still applies to the widow's figure: e.g. husband as in case 11 with an election, payable 800 / without election 1000 -> his increase 400 -> widow 5/8 x 400 = 250. The brief's wording ("computed without s 8 for his commutation") is consistent, but an encoding that drops s 8 entirely for widows would get 312.5.
- **s 10 floor.** The Act says the increase "shall be reduced by the amount of that first-mentioned increase" and does not say "not below nil". I follow the brief's floor at nil (a negative increase would reduce the base pension, which the section's heading "Adjustment" does not suggest), but flag it as a reading.
- **Order of s 8 and s 10.** Both are "subject to this Act"; s 10 refers to the increase "under the preceding provisions of this Act", which include s 8, so s 10 comes after s 8 (case 9).
- **s 18** (no increase for a person also entitled under the Superannuation Act 1922-1971, other than a widow or child) and **s 9** (commutation on or after commencement) are outside the brief's scope; not tested unless the module models them.
- No rounding is stated; results are exact.
