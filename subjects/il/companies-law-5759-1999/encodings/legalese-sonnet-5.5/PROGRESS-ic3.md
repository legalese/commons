# PROGRESS: piece ic3 (Part 6 chapters 2 to 5, Part 7), lines 1685-2080

Status, 2026-10-25: every file listed under "Files written" was run, in a last run made after the last edit of any `.l4` file, and is green under `check.sh` (`L4_TARGET=unstable`: 0 errors, 1,259 assertions satisfied, 0 failed, 0 refused; the assertions written, counted with `grep -c '^#ASSERT'`, are also 1,259), and `srcrefs.py check --refs` and `--strict` report 0 problems on the ic3 files.
Nothing in this file is claimed beyond that.
Not done: no independent test pass (the brief allows none), no run on any build other than the one at `L4_BIN`.

## Method

- Templates with `@@Q n m` placeholder lines and the build script live in `ic/ic3/work/`, outside the deposit, so the deposit holds only deliverables. `build.py` expands each `@@Q n m` line with `srcrefs.py quote`, so no Hebrew quotation is typed by hand.
- Constitutive BOOLEAN predicates for what the text decides; `MAYBE`/`NOTHING` for a case the text does not settle; the approvals of a transaction as a record of the organs required (core party enumeration).
- Rule names: `סעיף N - …` (section label in ASCII digits, Hebrew letter if any), so no name can collide with another piece after the merge. Types: specific names starting `עובדות על …` or `סעיף N - …`.
- No section `GIVEN`, no `REFUSE`, no `TYPICALLY`, no regulative rule on the stable build; deadlines are date arithmetic returning BOOLEAN.
- Layer 2 is the seat of a person who founds, directs or holds shares in a company; one question per provision that gives that person a claim, privilege, power or immunity, or puts a duty or liability on them.

## Files written

| module | sections | lines | assertions |
| --- | --- | --- | --- |
| `ic3-part6-ch2-appointment.l4` | 250, 251, 251א | 1685-1694 | tests: 22 |
| `ic3-part6-ch3-duties.l4` | 252-264 | 1696-1777 | tests: 155 |
| `ic3-part6-ch4-director-rights.l4` | 265-267 | 1779-1792 | tests: 30 |
| `ic3-part6-ch4a-compensation-policy.l4` | 267א, 267ב (267ג: no rule) | 1794-1816 | tests: 44 |
| `ic3-part6-ch5-interested-transactions.l4` | 268-284 | 1818-1923 | tests: 100 and 148 |
| `ic3-part7-ch1-securities.l4` | 285-300 | 1925-1997 | tests: 86 |
| `ic3-part7-ch2-distributions.l4` | 301-313 | 1999-2079 | tests: 121 |
| `ic3-tests-*.l4` (eight files and the fixtures) | one per module | | 706 in all |
| `ic3-seat.l4`, `ic3-cases-seat.l4` | the seat: 129 questions; 553 cases | | 553 |
| `NOTES.md`, `PROGRESS.md` | | | |

## Decisions taken (with the section that licenses each)

The forks F1 to F17 and the reading taken in each are in the fork register of `NOTES.md`; the licensing text is quoted there.
Two choices of the seat, not forks of the text: the questions about approvals answer with a record (organs in the order the text gives them, the two special majorities, the articles' own way) and not with a list of booleans; the questions that the text answers with several results are split into one question each (for example 280(ב) and 281, and the three limbs of 283).

## Work files (outside the deposit)

`ic/ic3/work/`: `build.py` (expands the `@@Q n m` lines of `src/*.l4.in` into `-- src:` quote lines), `ck.sh <module>` (build, run, print diagnostics), `cases_gen.py` with `cases_spec.py` (the case file), `coverage_gen.py` with `coverage_spec.py` (the coverage table and its line check), `jural_gen.py` (the relations table), `notes.py` with `notes/` (assembles `NOTES.md`). The `.l4` files in the deposit are generated; edit the templates, never the generated file.
