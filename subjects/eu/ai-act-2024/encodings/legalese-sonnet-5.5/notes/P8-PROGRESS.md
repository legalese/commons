# PROGRESS (P8: lines 1113-1313, Articles 72 to 79 with 75a to 75d)

Written for resumption after a compaction.
Re-read this file, NOTES.md and the text, not a summary.

## State (2026-11-17, after follow-up 2)
- DONE: layer 1 (`P8-gate`, `P8-art72` to `P8-art79`) and its tests (`P8-tests-*.l4`, 698 traces, all agree with their `-- EXPECT` on both builds).
- DONE: the nine seat layers (`P8-seat-<slug>.l4`, 260 questions) and their cases (`P8-cases-seat-<slug>.l4`, 836 assertions), every question asserted.
- DONE: NOTES.md (coverage, fork register of 81 lines, jural relations, marginal readings 1 to 11, reading a result, seams incl. S14, split sites (i) to (iv), rules with no breach path, versions, seats incl. the second audit, findings, binary, check.sh output); NEEDS-CORE.md.
- DONE, follow-up 1 (FOLLOWUP-1.md): seat audit (260 read, 8 retitled), a Guide line on every split-site fork entry, seam S14 (50 functions, 17 regulative rules, fork F-S14-reach, assumed, not ruled).
- DONE, follow-up 2 (FOLLOWUP-2.md, three tasks in order): (1) `Art 73(6) second subparagraph the provider is barred ...` is an "until" bar (ruling (d)): `JUST TRUE` before the competent authorities are informed, `JUST FALSE` after, `NOTHING` with no alteration that may affect the evaluation (fork F-73-6-until); (2) both Art 75c(8) barred functions answer `JUST FALSE` inside the five years and before the period begins, `JUST TRUE` after (ruling (a); fork F-75c-8-inside); (3) every duty site whose condition is unmet has a fork line, 42 in all, including `Art 75(1d) first sentence` (F-75-1d-first-duty); no answer of those 42 changed; 9 of them fit no Guide line verbatim (Marginal readings, item 11). The seat questions were checked for name and direction: none retitled.
- LAST STEP: `check.sh` on 1.6.110 and main 1.6.109 (49 modules, 1,833 satisfied, 0 errors, every module `same`); `srcrefs.py check --refs` and `--strict` (402 quote lines, 315 runs, 326 locators, 0 problems); `traces.py` over every `#TRACE` on both builds (698, 0 mismatches, outcomes identical to before); the final report.
- NOT DONE (outside the tasks): the role questions of the manufacturer and person seats (NEEDS-CORE.md; `aia-scope.l4` is in the folder now).

## Working set (outside the deposit, in `../../../work/`; not shipped)
- `src/*.l4.in` and `build.py`: sources of the FIRST-PASS layer-1 and test files; they carry neither follow-up. Do not rebuild from `src/`.
- Follow-up 1 was applied by script on top of `backup1/` (the accepted first-pass files): `s14wire.py`, `s14apply.py`, `s14tests.py`, then `genseat.py` with `seatspec.py`. **Do not run `s14apply.py` again**: it restores `backup1/` and would erase follow-up 2, which was edited directly into the deposit files (`backup2/` holds the deposit as it stood at the end of follow-up 1, for diffing).
- Follow-up 2 by hand: the three branches of the two Art 75c(8) functions and the Art 73(6) bar in `P8-art73.l4`, `P8-art75c.l4`; a `(fork F-...-duty)` tag on the unmet branch of each of 42 duty functions (`dutyscan.py` finds the sites, `dutyforks.py` names them and checks their quotations against the text); the tests of both articles with `-- RECONCILED` lines. `genseat.py` can still regenerate the seat files, but run `reconcile2.py` after it, because the seat cases that follow-up 2 changed carry their `-- RECONCILED` lines from it (it diffs against `backup2/`).
- `authority.py`: the Guide line of each split-site, duty-site and ruled-reading fork entry (`DUTY` lists the 42 duty sites with their kind of gate); every quotation is asserted against `inputs/ENCODING-GUIDE.md` and `BRIEF.md` when `mknotes.py` runs.
- `cov.py`, `forks.py`, `rules.py`, `notes_forks.py`, `mknotes.py`: build NOTES.md from the text, the sources and `check-final.log` and `traces-final.log`.
- `traces.py FILE...`: runs every `#TRACE` on both builds and compares with `-- EXPECT`.
- Order to rebuild NOTES.md: `check.sh` and `traces.py` into `check-final.log` and `traces-final.log`, then `python3 -I mknotes.py`.

## Decisions taken (each licensed by the brief unless noted)
- Parties of the regulative rules: one type `Arts 72 to 79 party` in `P8-gate.l4`; acts: one type per article.
- Gate: `Arts 72 to 79 the group General applies to the AI system` (the quartet) or `... on the date asked`; Art 78 has its own group helper; both only call the keel's `Art 113 the provision group applies`.
- A decision function answers `JUST FALSE` only where the text says no in its own words; otherwise `NOTHING` with `-- NOTHING-kind (...)`.
- Split site (ii): `JUST FALSE` (19 fork lines, 20 sites); the grant ruling's `NOTHING` for "if", "provided that", "as appropriate" gates; split site (i): `NOTHING` (2 sites); split site (iv), a duty whose condition is unmet: 42 sites, `JUST FALSE` where the text introduces the condition (38) and `NOTHING` where it limits the sentence to its own case (4).
- An "until" bar answers `JUST TRUE` before the event and `JUST FALSE` after it (Art 73(6) second subparagraph); a flat negative with no end answers `JUST TRUE` or `NOTHING`.
- A limitation period answers `JUST FALSE` inside it and before it begins, `JUST TRUE` after it (Art 75c(8)).
- Every `NOT` in a compound condition is parenthesised.
- Versions: the dead as-enacted branch is encoded as its own function and tested directly.
- Seam S14 (assumed, not ruled): the cut-off by Art 2(2) is answered before the provision's own date, Art 111(2) and classification checks; a function that returns a number answers `NOTHING`, a rule `FULFILLED`.
- The manufacturer and person seats have no role question: see NEEDS-CORE.md.
- Limitation period of Art 75c(8) ends on the fifth anniversary of its first day (assumed, not ruled).
