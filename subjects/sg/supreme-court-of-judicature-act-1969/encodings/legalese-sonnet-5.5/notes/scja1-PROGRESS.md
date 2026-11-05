# PROGRESS.md (scja1)

Updated: 2026-11-05, fix round complete (Act-wide convention for a bare "must"; findings from an independent test pass).

## State

Everything the brief asks for is written and checked.
- Layer 1: ten modules `scja1-part*.l4` and ten test files `scja1-tests-*.l4` (862 assertions, written equal to satisfied).
- Seat: `scja1-seat.l4` (58 `@export` questions in nine `§§` groups) and `scja1-cases-seat.l4` (172 assertions, written equal to satisfied).
- `NOTES.md` (coverage 347 rows, fork register F1 to F19 and K1 to K3, QA to QE sites (37 hand-written lines), jural relations, marginal readings, reading a result, seams, dependencies, unstable-dialect line, findings, what the binary does not accept, what check.sh prints) and `NEEDS-CORE.md`.
- `check.sh` (main 1.6.109 against main 1.6.108): 24 modules, 0 errors, 1034 satisfied, 0 failed, 0 refused; every module "same" on both builds.
- `srcrefs.py check --refs` and `check --strict` over the 22 `scja1-*.l4` files: 979 src lines, 172 runs, 213 locators, 0 problems.
- `l4 check` over every `scja1-*.l4`: no "is at the end of the file", "follows code on its line" or "Unknown annotation" warning.
- Trace outcomes (27 traces in 6 test files) read from both builds: the same.

## Fix round (2026-11-05)

Act-wide: a bare "must" or "is to be" not done answers `NOTHING` (F7 rewritten; ss 11(2), 17C(2), 18G, 18H(2), 18I(2), 22B(2); s 18H(2) "is to appoint" was found by a scan and not tagged QB before); the Judgment calls are hand-written lines, one per function.
Reviewer findings: s 10(5) polarity and a "may sit" twin (F15); s 17A(3) matter limb now `JUST FALSE` like the parties limb (F8); s 29C(2) takes the Sixth Schedule's `JUST TRUE` over fork K1; ss 21(1) and 29A(1) keep `NOTHING` for a case in no limb (F14) and the seat says what that means; ss 17B(2) and 22A(2) answer `JUST TRUE` when the "unless" is met, s 28(2) keeps `NOTHING` and gets a bar twin and seat question (F16); s 28A(1) takes the court as an input (F17); forks F17 to F19 and the gap lines added.

## Tooling (under work/, not shipped)

env.sh, units.py -> units.json (343 units), build.py (expands the `@@Q` macros in work/src/*.l4.in into the deposit), run.sh, sigs.py, gen-coverage.py (coverage table and audit), gen-sites.py (the marginal readings, and a list of the QA to QE functions that the hand-written work/notes/25-sites.md is checked against), gen-notes.py (assembles NOTES.md from work/notes/*.md and the generated tables).
To regenerate NOTES.md after an edit to a `.l4` file: rerun check.sh into work/check-out.txt, gen-coverage.py, gen-sites.py, gen-notes.py (usage at the head of each).

## Decisions taken (with the licensing text)

All in NOTES.md "Fork register (scja1)".
Assumed, not ruled: F3 (means/includes), F7 (bare must), F12 (before the 15th day), F13 (a ceiling), F14 to F19, K1 to K3 (the keel's).

## Not done, on purpose

- No git use. No `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` or `README.md` (the lead's).
- No second, unstable encoding: nothing in lines 46 to 2309 earned one (NOTES.md "Unstable dialect").
- Scratchpad tidied: no binaries were copied into it.

## Opened by accident

Nothing forbidden.
Three fix-round messages written for other rows were attached to my context by the harness in a system reminder; I did not open or use them.
