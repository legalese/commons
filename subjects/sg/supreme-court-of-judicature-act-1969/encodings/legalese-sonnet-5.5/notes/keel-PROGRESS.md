# PROGRESS (keel agent, Supreme Court of Judicature Act 1969)

Files this agent owns: `scja-core.l4`, `scja-core-tests.l4`, `PLAN.md`, `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md` (copied from `inputs/STUB-SOURCE-LICENSE.md`).
Raw text for `srcrefs.py`: `INPUTS_DIR/SCJA1969.txt` (7314 lines).
Scratch work (outside the deposit): `scratchpad/keel-work/` (compact reading copy of the text, `xref.py` and `xref2.py` cross-part reference finders, probe files).

## State: all steps of the brief done (2026-11-05)

- [x] Read brief, inputs, both skills, dialects.md, phrasebook 6 and 1.10 (the other phrasebook pages by headings only), the whole text.
- [x] Keel range is lines 1-45 only (title page, consolidation banner, Arrangement of Sections to s 8A). No definition falls in it. Decision: no `scja-definitions.l4` (s 2 is lines 378-433, scja1's; writing it here would define `s 2 ...` twice). PLAN.md says so.
- [x] `scja-core.l4`: 297 lines, DECLARE + 9 constants, checks clean on main 1.6.109 and 1.6.108.
- [x] `scja-core-tests.l4`: 23 assertions satisfied.
- [x] `PLAN.md`: ranges, section map, core table, 20 seams, twins, difficulties, reserved names.
- [x] `NOTES.md`: coverage of lines 1-45, ruling bullets verbatim, judgment-call lines QA-QF, forks K1-K5, jural relations, FALSE/NOTHING, dependencies, unstable dialect, main-binary findings, checks, open questions.
- [x] `check.sh` run: 2 modules, 0 errors, 23 satisfied, 0 failed, 0 refused, main columns the same.
- [x] `srcrefs.py check --refs` and `--strict`: 23 src lines, 13 runs, 14 locators, 0 problems.

## Decisions (with licence)

- Names avoided in the core because the staged sgia modules define them: Moment, `Period unit`, Days, Weeks, Months, Years, `Counting word`, From, After, `Reach of section 50(b)`, `every period`, `periods of days only`, `How the day of commencement is fixed` (+3 ctors), `Provision and its day`, `Time for doing a thing` (+ctor), `Kind of definition`, Means, Includes, `Means and includes`, `Has the meaning given by another law`, `Depends on where it is made`, `Rule of reading`, Definition. Checked by importing core + both modules in one file: no "multiple definitions".
- Seams are typed MAYBE where the answering section can say NOTHING (rule of 2026-10-29: a caller never turns NOTHING into FALSE). Recipe verified on main 1.6.109 (4 assertions).
- SICC is its own `Court` constructor (K1); the amount in `Decision` is `MAYBE NUMBER` (K2); appointment order is a date (K3); quasi-criminal is its own kind (K4).
- A speculative type `Step a court may take` was written and removed (no evidence two parts would share it); the core is 297 lines.
- A transient `check-out.txt` was written one level above `iaw-scja-k` (in `runs/`) by mistake and removed at once; nothing else was written outside the deposit and the scratchpad.
