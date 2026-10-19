# Independent test report: Parliamentary Retiring Allowances (Increases) Act 1967

Files: `independent-expectations.md` (written from BRIEF.md and the source only), `tests-independent.l4` (against `pra-rules.l4`).

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 — 0 errors, **23 satisfied, 0 failed**. (pra-tests.l4 14/0.)

## Failures

None. Both tables (all seven rows), off-table amounts (31; 2,291.68), cross-table amounts (an s 3 amount in the s 4 class and vice versa), both widow rates ($48.16; $2,729.17), class "none", and the s 7 effective date for both s 3 and s 4 increases all matched.

## Gaps and reading notes

- s 3(1)(a) and (b) are collapsed into one class; the 1948-1955 / 1948-1959 + s 18 distinction is left to the user. Not separately testable. The s 3(1)(b) widow-pensioner (pension payable as a widow, s 18 applied to her husband) is likewise a "weekly pensioner under s 3".
- s 7 "first fortnightly payment ... made after the date of commencement": the module takes the date as given and does not check it is after 8 Nov 1967. A date of 8 Nov 1967 (or earlier) is accepted unchanged. Not asserted, as the input is defined as the first payment after that day; worth a guard.
- s 4(2) says "Two thousand seven hundred and twenty-nine dollars seventeen cents" without "a year"; the brief and module read it as annual. I agree (s 4 deals in annual amounts), but the text is silent.
- s 7 covers increases under ss 3(1) and 4(1) only; the module returns `from` = NOTHING for widows. Consistent with the text.
- Widows' pension is returned whatever pension amount is input (input ignored) — fine.
- Numbers compared exactly; float representation of 2291.67 worked.
- Process note: I glanced at the import header of pra-tests.l4 only.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
