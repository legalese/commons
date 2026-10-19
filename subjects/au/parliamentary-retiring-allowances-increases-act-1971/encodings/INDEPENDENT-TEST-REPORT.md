# Independent test report: Parliamentary Retiring Allowances (Increases) Act 1971

Expectations were written in `independent-expectations.md` from BRIEF.md and the Act before any `.l4` file was opened; `tests-independent.l4` asserts them against `pra71-rules.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, 34 assertions satisfied, 0 failed. (The author's pra71-tests.l4 has 14 satisfied, 0 failed.)

Covered: every row of the s 3(1), 4(1), 5(1), 6(1) and s 7 tables; an amount outside each table (NOTHING); the three fixed widow rates (ss 3(2), 4(2), 5(2)); s 6(2) five-sixths as exact fractions (1363/120, 427/60) and a husband not in the table; s 8 one-half (including an exact non-terminating case, 123457/200); a class outside the Act; s 12 date carried for an increase and NOTHING when there is no increase or only a fixed widow rate.

## Failures

None.

## Gaps and reading differences (not tested, because the module has no input for them)

- **s 8 date limb**: an s 19A(2) pension gets the half only if it "became payable before the first day of March, One thousand nine hundred and fifty-nine". The module takes no "payable from" date, so the 28 Feb / 1 Mar 1959 edge cannot be tested; class membership stands in for the condition.
- **s 7 date limb**: ceasing to be an office-holder "before the first day of December, 1968" is likewise folded into the class; no edge test possible.
- **s 7 and s 12(2)**: s 12(2) dates only s 7 increases on pensions to which the person became entitled before commencement. A person who becomes entitled to an s 7 pension after commencement has the increase from entitlement, but the module returns the first-fortnightly-payment date for every s 7 case.
- **s 6(2) widow and s 12**: s 12(1) lists s 6(1) but not s 6(2). The module returns the first-fortnightly-payment date for an s 6(2) widow's increase; the Act gives that increase no start date of its own (it arises when the husband dies). Not asserted, flagged here.
- **Rounding**: the Act states none; the module keeps exact fractions, which agrees with my reading.
- The weekly/annual unit is implicit in the class; the module does not check that an amount is in the right unit.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
