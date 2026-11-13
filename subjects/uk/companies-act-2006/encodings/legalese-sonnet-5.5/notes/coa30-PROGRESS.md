# PROGRESS (coa30: Companies Act 2006, lines 20017-20928, Schedules 10 to 16)

Written for the agent itself: after any compaction, re-read this file, NOTES.md and the text, not a summary.

## Method (settled 2026-11-12)

- Source of truth for the L4 is `work/src/*.in` (under `DEPOSIT/../work/`, not shipped). `python3 -I work/build.py` expands the macros `@@Q lo hi | label` (quote lines + `@ref`) and writes the `.l4` files into this folder, so no source text is ever retyped.
- `work/segment.py` splits lines 20017-20928 into coverage rows (`work/rows.json`); `work/map_rows.py` gives each row its disposition and L4 name; `work/gen_notes.py` writes the coverage, jural-relations and fork tables of NOTES.md and refuses to run if a row has no disposition or a line is unclaimed.
- Dialect: stable binary 1.6.110 (main). No REFUSE, no sets, no section GIVEN, no `AFTER ... WITHIN`, no `MAY ... LEST`, no YMD. Dates are `Date day month year`.

## Decisions (with the text that licenses each)

- "Beginning with" is inclusive: the period of three months beginning with 1 January ends on 31 March (sch 10 paras 3(5), 3(2) etc.). Helper in the Part 1 module computes "the first day after the period".
- Seat for this range: an individual who deals with a company as its statutory auditor or would-be auditor, as someone holding or seeking a recognised professional qualification, or as a director of an audited company (assumed, not ruled).
- Open-textured judgments ("adequate", "appears to him", "fair and reasonable") are plain BOOLEAN inputs.

## Sections done / in progress / next (updated 2026-11-12, after the layer-1 modules)

Done, each compiles with 0 errors and 0 warnings on 1.6.110 and its tests are all satisfied (`work/run1.sh FILE`):
- Sch 10 Part 1 (paras 1-5): `coa30-sch10-part1.l4` + `coa30-tests-sch10-part1.l4` (95 assertions)
- Sch 10 Part 2 paras 5A-8: `coa30-sch10-part2-a.l4` + tests (107); paras 9-20A: `coa30-sch10-part2-b.l4` + tests (263)
- Sch 11 (paras 1-11): `coa30-sch11.l4` + tests (146)
- Sch 11A (tables for Parts 1 and 2, Part 3 functions): `coa30-sch11a.l4` + tests (131)
- Sch 12: `coa30-sch12.l4` + tests (34); Sch 13: `coa30-sch13.l4` + tests (101)
- Regulative rules for the duties: `coa30-regulative.l4` + `coa30-tests-regulative.l4` (17 traces, no assertion lines; results recorded in NOTES.md)
- Generators: `work/gen_part2a.py`, `gen_part2b.py`, `gen_sch11.py`, `gen_sch11a.py`, `gen_sch12.py`, `gen_sch13.py` (the Part 1 and regulative modules are hand-written `.in` files in `work/src/`); forks are collected in `work/forks_*.json`.

Also done: the seat layer `coa30-seat.l4` (43 questions) and `coa30-cases-seat.l4` (135 cases, all satisfied); the coverage mapping and NOTES generators (`work/gen_notes.py`, `work/finish_notes.py`: run `work/rebuild.sh`, then `python3 -I work/gen_notes.py && python3 -I work/finish_notes.py`); NOTES.md (coverage of all 823 rows, forks, jural relations, marginal readings, seams, findings, traces, tests disclosure, check.sh output) and NEEDS-CORE.md.

Final checks, run after the last rebuild: `check.sh` (target main, 1.6.110 against 1.6.109) prints 20 modules, 0 errors, 1012 satisfied, 0 failed, 0 refused, every module `same` on main; `srcrefs.py check --refs` and `--strict` on every `coa30-*.l4`: 659 quote lines, 224 runs, 232 locators, 0 problems; no `DiagnosticSeverity_Warning` or `_Error` on any coa30 module; the regulative traces print identically on both builds.

Nothing remains `deferred`. Left for a human: a second reader's independent test pass, a lawyer's review of the marginal readings, and the open questions at the end of NOTES.md.

Decisions taken (assumed, not ruled; each has a fork line in NOTES.md):
- Sch 10 Part 3 (paras 21-27) is blank in this text; Schedules 14, 15, 16 are inert (reason 2: amendments and repeals of other Acts); Sch 13 paras 3, 5, 7(3), 11(2)-(4), 12 inert (reason 2); Sch 12 para 6(2) inert (reason 2); Sch 10 para 7(1) and the signposts inert (reason 1).
- Month-end rule for "N months beginning with": corresponding date, clamped to the last day of a short month (fork F1).
- "must have" requirement functions answer JUST FALSE when a limb is unmet (fork F-must); gated limbs are vacuously met when the gate is unmet.

## Files written

All under `DEPOSIT/encodings/legalese-sonnet-5.5/`: `coa30-*.l4` as listed above, PROGRESS.md; the keel's `coa-core.l4`, `coa-definitions.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` are supplied and unchanged.
