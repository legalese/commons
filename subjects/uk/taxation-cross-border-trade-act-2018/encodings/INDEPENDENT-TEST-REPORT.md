# Independent test report: TCTA 2018 Part 1

Independent tests: `tests-independent.l4`, from `independent-expectations.md` (written from BRIEF.md and the source text before any `.l4` file was read). Run with `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 2 (both the failed assertions) | 60 | 2 |
| tcta-tests.l4 (author's) | 0 | 23 | 0 |

62 independent assertions. They cover liability for each procedure (L1-L17), persons liable (P1-P9 plus P3b), the amount (A1-A4), the last day to notify (N1-N9: leap day, 1 March into a leap year, month and year ends, 3 and 20 years), enforceability on the day before, the day of and the day after each limit (E1-E11), and end-to-end cases (T1-T3). All the date arithmetic agrees with my reading of Sch 6 para 4 and with the brief.

## Disagreements (failing assertions)

### 1. P8: persons "liable" where no liability is incurred (line 122)

- **Scenario:** goods declared by A on behalf of B for a storage procedure, with entitlement and no breach.
- **Expected:** no one is liable (EMPTY).
- **Code:** `LIST "A", "B"`.
- **Source:** s 4(2) "the general rule is that a liability to import duty is not incurred"; s 6(1) "the person in whose name the declaration is made is the person liable to import duty"; s 6(7) "If two or more persons are liable to import duty in any case".
- **View:** s 6 says who bears a liability. It does not create one. Where s 4(2) means no liability is incurred, nobody is liable to import duty, so I think my reading is right. `the persons liable for` never checks whether `the import duty liabilities for` is non-empty. Suggested fix: return EMPTY when there are no liabilities.

### 2. T3: the same issue in the top-level goal (line 190)

- **Scenario:** end-to-end storage, entitled, no breach, A declarant.
- **Expected:** `persons liable` EMPTY. The code's liabilities, duty (0) and last day (NOTHING) are correct.
- **Code:** `LIST "A"`.
- **Source and view:** as for item 1. The top-level position names a person liable to a liability that does not exist.

## Gaps noticed (not asserted, or passing only because the point is an input)

- **Joint and several (s 6(7))** is not an output. The goal returns a list of names, so the "jointly and severally" status is only implicit.
- **s 6(4) knowledge test** is collapsed into one input boolean (`otherwise liable under s 6(3)`). Tests P5/P6 only check that the flag passes through. The four limbs of s 6(4) and "knew, or ought reasonably to have known" are not modelled.
- **Notification before the liability was incurred** is treated as enforceable, because the check is only `notified on AT MOST last day`. Sch 6 para 2 presupposes that HMRC "consider that a person is liable". I would REFUSE or reject this case. Not asserted.
- **Not presented, with no forfeiture date given:** this returns EMPTY. s 5(1) says the goods are liable to forfeiture "at the time of importation", so a liability does exist and only its date is missing. REFUSE would fit the brief better than silently returning no liability. The same goes for authorised use or temporary admission with a breach but no acceptance date: this returns EMPTY, and I would expect REFUSE.
- **Top-level amount:** one figure (rate × value) is reported even when there are two liabilities (s 4(4)(d), the normal rate less the earlier liability). The further liability's amount and its own notification limit are not computed. Only the first liability's last day and enforceability are reported.
- **20-year extension:** one flag on the duty facts applies to every liability in the case, though para 4(2) turns on the circumstances of each liability.

## Change after the pass (encoder)

- **P8, T3 (persons liable with no liability).** Accepted. `the persons liable for` now returns no one when `the import duty liabilities for` finds no liability (s 4(2); s 6 only allocates a liability that exists). Both assertions pass.
- The gaps listed above are recorded as known limits in NOTES.md.
