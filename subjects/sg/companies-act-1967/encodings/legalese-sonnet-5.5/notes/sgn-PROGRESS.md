# PROGRESS (sgn: Companies Act 1967, Part 11A, ss 386AA to 386AP; text lines 25372-27069)

Written for the encoder's own use after a compaction.
Re-read this, NOTES.md and the text, not a summary.
State at the end of the work: every section below is done and the last gates are green (final numbers are in NOTES.md, "What check.sh prints").

## Pipeline

- Templates are in `../../../work/tpl/*.l4`; `../../../work/gen.py <name>` expands `%%Q`, `%%QREF`, `%%REF` directives into this folder, copying the quoted lines mechanically from `inputs/CoA1967.txt`.
- `../../../work/src/*.l4` (notices, nominees, registrar) go through `../../../work/pre.py` to `../../../work/tpl/` first.
- `../../../work/run.sh <file.l4>` counts errors, warnings, satisfied, failed and refused assertions for one file.
- `../../../work/traces.py <test file>` (with `L4` and `L4_MAIN` set) compares each `-- EXPECT` word with what the trace prints, on both builds.
  A trace is BREACH only when its message starts `DEONTIC BREACHED`; a residual obligation prints its own rule text, which contains "LEST BREACH".
- `../../../work/gen_rule_tests.py` writes `sgn-tests-nominees-rules.l4` (70 traces); `../../../work/seat/*.py` write `sgn-seat.l4` and `sgn-cases-seat.l4`.
- `../../../work/cov.py` writes `../../../work/cov.json` (the coverage partition) and prints the uncovered count; `../../../work/mknotes.py` writes NOTES.md from `cov.json`, `check-final.log`, `notes-head.md` and `notes-rest.md`.

## Sections

| section | module | tests | state |
| --- | --- | --- | --- |
| 386AA, 386AB, 386AC | sgn-application.l4 | sgn-tests-application.l4 (83) | done |
| 386AD, 386AE | sgn-evidence.l4 | sgn-tests-evidence.l4 (42) | done |
| 386AF, 386AFA | sgn-register.l4 | sgn-tests-register.l4 (138 assertions, 36 traces) | done |
| 386AG, 386AH, 386AI, 386AIA, 386AJ, 386AK | sgn-notices.l4 | sgn-tests-notices.l4 (166 assertions, 18 traces) | done |
| 386AKA, 386AL, 386ALA, 386ALB | sgn-nominees.l4 | sgn-tests-nominees.l4 (130 assertions), sgn-tests-nominees-rules.l4 (70 traces) | done |
| 386AM, 386AN, 386ANA, 386AO, 386AP | sgn-registrar.l4 | sgn-tests-registrar.l4 (107 assertions, 14 traces) | done |
| seat | sgn-seat.l4 (58 questions), sgn-cases-seat.l4 (150 assertions) | | done |
| NOTES.md | generated: coverage by script, fork register, jural relations, and the rest | | done |

## Decisions taken (each with the text that licenses it; the full list is the fork register in NOTES.md)

- An unmet element of an offence gives JUST FALSE (the provision's own question; split site (i), 21 sites, fork F-AF6).
- A "where" gate that fails gives JUST FALSE (periods ruling 2026-11-05 (b)); 8 sites; s 386AM(2) is the one "may" (split site (ii), F-AM1).
- A function named for a grant or a power answers NOTHING when its gate fails (the ruling of 2026-11-12, limit 1); 9 functions, F-GR1 to F-GR9.
- A prescribed thing (period, particulars, form, place, manner) is an input; a prescribed period is a number of days (F-AF4).
- A missing act before the last day gives NOTHING; a missing act after the last day gives JUST FALSE (periods ruling (a)); the one timing helper is `s 386AF(8) timing: the act was done in time` (F-AF5).
- "Subject to section 386AM" lifts a bar with JUST FALSE where the disclosure is under 386AM (s 386AF(11)); the bars answer NOTHING for a person who is not a member of the public (F-AF3).
- Where a company becomes subject to the Part later, subsection (3) governs over (1), (2) (F-AF1).
- The appointed day is an input date, one for each of ss 386AF(14), 386AL(9), 386ALB(8) (three different commencement sections of the 2024 Act; F-AL1).
- 13 `MUST` rules with no `WITHIN` and no consequence beyond a separate offence have only FULFILLED or RESIDUAL traces and are listed under "Rules with no breach path (sgn)".
- `s 386AE(2) "employer"` takes the s 6 answer as one fact under its own name, and does not call the keel's `s 4(1) "related corporation" ...` (NOTES.md, "Where this brief and PLAN.md differ").

## Files written

All in this folder: `sgn-application.l4`, `sgn-evidence.l4`, `sgn-register.l4`, `sgn-notices.l4`, `sgn-nominees.l4`, `sgn-registrar.l4`, the seven `sgn-tests-*.l4`, `sgn-seat.l4`, `sgn-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`.
No `NEEDS-CORE.md`: no type or constructor was missing.

## Gates (last run)

- `check.sh`: exit 0, 23 modules, 816 satisfied, 0 failed, 0 refused, the same four counts on both builds.
- `srcrefs.py check --refs` and `--strict`: 0 problems.
- `traces.py` over the four trace-bearing test files: 138 traces, 0 mismatches, on both builds.
- `cov.py`: 0 text lines uncovered.
