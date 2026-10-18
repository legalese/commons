# Independent test report: Employment Rights Act 1996 encoding

Test file: `tests-independent.l4`. Expected values: `independent-expectations.md`, written from BRIEF.md and the Act before any `.l4` file was opened.

## Counts

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **148 assertions, 143 satisfied, 5 failed, 0 other errors** (5 errors = the 5 failed assertions).

- The first pass had 143 assertions, all written before the encoding was read. All 143 pass. They cover s 86 at the one-month, two-year and twelve-year edges, s 108 with s 97(2)/(4), s 111 with s 207B, the basic award, the redundancy payment, and the top-level goal.
- Once I had read the code, I added 5 probes at places where its arithmetic could part from the Act. I worked their expected values from the Act, not from the code. **All 5 fail.**

The encoding's own `era-tests.l4` gives 97 satisfied and 0 failed.

## Failures

| Line | Scenario | My expected value | Encoding's value | Act | Which is right |
|---|---|---|---|---|---|
| L353 (T22) | EDT 15 Jan 2026; Day A 1 Jan, Day B 20 Jan 2026. ACAS was contacted during the notice, before the EDT. | 20 Apr 2026 | 3 May 2026 | s 207B(3) "In working out when a time limit ... expires the period beginning with the day after Day A and ending with Day B is not to be counted." | **Mine, on balance.** Only 15-20 Jan (6 days) fall inside the three months beginning with the EDT. The days 2-14 Jan were never going to be counted, so leaving them out cannot push the expiry later. The encoding adds all B − A = 19 days. This is a reading point and case law may settle it, but the Act's words point to 6 days. |
| L354 (T23) | EDT 15 Jan 2026; Day A 1 Jan, Day B 10 Jan 2026. Conciliation finished before the EDT. | 14 Apr 2026 | 23 Apr 2026 | same | **Mine.** None of the uncounted days falls within the limitation period, yet the encoding still adds 9 days. A certificate issued before the period starts should not extend it. |
| L356 (B21) | Start 1 Mar 2024, EDT 28 Feb 2025, DOB 1 Mar 1983, pay 400. Basic award. | 600 (1.5 weeks) | 400 (1 week) | s 119(1)(b) "the number of years of employment **falling within that period**"; s 119(2)(a) "a year of employment in which the employee was not below the age of forty-one" | **Mine.** The single year of employment is 1 Mar 2024 to 28 Feb 2025, and he was 41 throughout. The encoding works year 1 back from 28 Feb 2025 as `add months −12` + 1 day, so the year starts on 29 Feb 2024. That is before employment began and the day before his birthday, so it allows only 1 week. |
| L357 (B22) | Start 1 Mar 2020, EDT 28 Feb 2026, DOB 1 Mar 1979, pay 400. Basic award. | 3600 (9 weeks) | 3400 (8.5 weeks) | same | **Mine.** The forward count correctly finds 6 years. Reckoning back, though, the encoding starts year 6 on 29 Feb 2020 (28 Feb 2026 − 72 months + 1 day), the day before employment began and before he turned 41. It also starts year 2 on 29 Feb 2024 (a 366-day year), which does not matter here. |
| L358 (P32) | As B21, but for a redundancy payment (s 162). | 600 | 400 | s 162(1)(b), (2)(a), same words | **Mine.** Same cause: `the first day of year k counted back from e` in `era-periods.l4`. |

**Suggested fix for B21/B22/P32:** have the reckoning back agree with the forward count. For example, take the first day of year k as the later of the start of continuous employment and the day after `add months e (−12k)`. Or compute year boundaries forward from the start and take the last n of them. The defect only shows when the reckoning back crosses a 28 Feb that follows a leap day and a birthday falls on 1 Mar. It is narrow, but it gets the money wrong.

**Suggested fix for T22/T23:** in `the limit after s 207B(3)`, count only the uncounted days that fall on or after the first day of the period. That is: add max(0, Day B − max(Day A, EDT − 1)). This needs the period's start date passed in. The same function serves s 164(5), where the period begins with the relevant date.

## Points where the encoding and I agree, and the Act is open

- **Age bands (ss 119(2), 162(2)).** Both read "a year ... in which the employee was not below the age of 41" as 41 or over on the first day of the year. Tests B1 and B3-B6 confirm this, including a birthday on the first day versus one day later. The other reading (age at any time in the year) would give 6250 rather than 6000 in B1. Both readings are reasonable, and a UK lawyer should confirm which one is meant.
- **Less than one month (s 86).** Both give 0 weeks rather than REFUSE. I agree, since the Act answers this: s 86 requires nothing.
- **One month after Day B when Day B is 31 Jan (T20).** Both give 28 Feb.

## Remarks on the encoding (tests pass, but worth noting)

1. **s 111(5) (s 104F blacklist).** Here s 111(2)(b) does not apply, and a "just and equitable" extension takes its place. The encoding has one `late complaint allowed` flag for both, so it gives no sign that the test differs. This is acceptable as an input, but NOTES should say so.
2. **s 122(3).** In a redundancy case, a conduct reduction under s 122(2) may apply only to the part of the award that s 120 makes payable. `just and equitable reductions` is an unconstrained number, so nothing stops a reduction below the s 119 amount in an ordinary redundancy case. The tribunal-finding input carries the whole burden.
3. **s 111(3).** `withNotice` requires the complaint to be presented strictly after the day notice was given. A complaint presented later on that same day is "after the notice is given" under the Act, but the code excludes it.
4. **Reason for dismissal as a single enum.** It cannot express s 120(1)(a) ("in a redundancy case, for selecting the employee") together with redundancy. That case is handled correctly only because s 122(4) is a separate input. Nor can it express s 121(a) (s 138) separately from s 121(b). This is harmless, but it is coarse.
5. **s 97(4) for "terminated by the employee otherwise".** The encoding applies it to a plain resignation too. That is literally right (s 97(4)(a) says "terminated by the employee"), and it is harmless because the person is not dismissed. Since s 145(5) has no employee limb, test P11 confirms the encoding correctly treats a constructive dismissal differently for redundancy.
6. **Not modelled, though inside the brief's sections.** s 136(3) (the employee's counter-notice during the obligatory period), s 145(3)-(4) (relevant date in those cases), s 140(2)-(3) (strike, and the tribunal's appropriate payment), and s 141(4) is folded into one flag. NOTES.md should list these as out of scope if it does not already.
7. **s 164(2) with s 207B.** The second six-month period is computed from the unextended first period, then extended using the same Day A and Day B. That is a defensible reading, but I did not test it. Whether s 207B's (4) window should apply to both periods is open.
8. **Top-level goal.** The `weeks of notice` fields are computed on the material date, so for a constructive dismissal without notice they are the s 86 weeks on the day the employee left. That is fine, but the field name says "had to give", which over-states it for a contract the employee ended.

## Change after the pass (encoder)

- **B21, B22, P32: counting years back across 29 February.** Year k now begins on the later of two days: the day after the corresponding date k years before the end day, and the corresponding date, k years back, of the day after the end day. So the year ending 28 February 2025 begins on 1 March 2024 (NOTES F4). All three now pass.
- **T22, T23: s 207B(3).** Only the conciliation days that fall within the period the limit counts are stopped. These are the days from the later of (the day after Day A) and (the period's first day) to Day B. Conciliation before employment ended stops nothing, or only the part after it (NOTES F14). Both now pass.
- **Remark 4, s 111(3).** A complaint presented on the day notice is given now counts as presented "after the notice is given" (NOTES F13).
- The other remarks are recorded in NOTES.md as known limits. None of the independent assertions was changed.
- After the change, `check.sh` shows 8 modules: 245 assertions satisfied, 0 failed, 0 errors (97 encoder, 148 independent).
