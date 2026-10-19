# Independent expectations: Parliamentary Retiring Allowances (Increases) Act 1971

Written from BRIEF.md and `../registers/source-bundle/C1971A00075.txt` only, before any `.l4` file was opened.

Amounts in dollars. "NOTHING" means the Act gives no increase (or no rate) for that input.

| # | Scenario | Expected | Working / Act's words |
|---|----------|----------|-----------------------|
| 1 | s 3(1) pension $48.16 a week | increase $13.98 a week | s 3(1) table row 1 |
| 2 | s 3(1) pension $56.89 a week | $16.78 | row 2 |
| 3 | s 3(1) pension $57.79 a week | $16.78 | row 3 |
| 4 | s 3(1) pension $63.79 a week | $16.78 | row 4 |
| 5 | s 3(1) pension $50.00 a week (not in table) | NOTHING | the table lists rates only; "in accordance with the following table" |
| 6 | s 3(2) widow | pension at $62.14 a week | "at the rate of Sixty-two dollars fourteen cents a week" |
| 7 | s 4(1) $2,729.17 / $3,275.00 / $3,587.86 a year | $729.16 / $875.00 / $875.00 | s 4(1) table |
| 8 | s 4(2) widow | $3,458.33 a year | "Three thousand four hundred and fifty-eight dollars thirty-three cents a year" |
| 9 | s 5(1) $2,916.67 / $3,500.00 / $3,812.86 a year | $729.16 / $875.00 / $875.00 | s 5(1) table |
| 10 | s 5(2) widow | $3,645.83 a year | "Three thousand six hundred and forty-five dollars eighty-three cents a year" |
| 11 | s 6(1) $15.00 / $18.00 / $20.00 / $23.33 / $28.00 a week | $7.12 / $8.54 / $10.33 / $11.36 / $13.63 | s 6(1) table |
| 12 | s 6(2) widow, husband's pension $28.00 a week | increase 5/6 x 13.63 = 1363/120 = $11.358333... a week (exact; the Act gives no rounding rule) | "increased by five-sixths of the rate at which her deceased husband's pension was increased" |
| 13 | s 6(2) widow, husband's pension $18.00 | 5/6 x 8.54 = 427/60 = $7.11666... | as above |
| 14 | s 6(2) widow, husband's pension $19.00 (not in table) | NOTHING (husband had no s 6(1) increase) | as above |
| 15 | s 7 $1,050 / $1,260 / $2,500 / $3,000 a year | $183.75 / $220.50 / $437.50 / $525.00 | s 7 table (each is 17.5% of the pension) |
| 16 | s 7 $2,000 a year (not in table) | NOTHING | as for 5 |
| 17 | s 8 widow of former PM, pension $1,000 a year, payable before 1 March 1959 | increase $500 | "is increased by one-half" |
| 18 | s 8 pension $1,234.57 | increase 123457/200 = $617.285 (exact) | one-half; no rounding stated |
| 19 | s 12 start: commencement 1 Oct 1971, first fortnightly payment input e.g. 14 Oct 1971 | increases have effect from and including 14 Oct 1971; a payment on 13 Oct 1971 or earlier carries no increase; one on 14 Oct carries it | s 12(1) "from and including the first fortnightly payment ... made after the date of commencement" |

## Where my reading differs from, or goes beyond, the brief

- **s 12 does not mention ss 3(2), 4(2), 5(2) or 6(2).** The widow rates are not "increases" under subsection (1); they simply fix the rate of a widow's pension that arises when a husband dies, so no s 12 start date applies to them. If the encoding gates them on the first fortnightly payment date, that is an addition the Act does not make.
- **s 12(2) covers s 7 only for a pension "to which a person became entitled before the date of commencement".** For someone entitled to an s 7 pension after commencement, the increase applies from entitlement and s 12 says nothing. The brief treats s 12 as a single input date for everything.
- **s 8 condition**: the pension must have become payable before 1 March 1959. A s 19A(2) pension that became payable on or after that date gets no increase. (Edge: payable 28 Feb 1959 -> increase; 1 Mar 1959 -> NOTHING.)
- **s 7 condition**: ceased to be office-holder before 1 December 1968 (edge: 30 Nov 1968 -> increase; 1 Dec 1968 -> NOTHING), if the encoding models that date.
- Rounding: the Act states none, so s 6(2) and s 8 results are kept as exact fractions.
