# PROGRESS.md (scja2): ss 30-72, lines 2310-4320

Status 2026-11-05: layer 1, layer 2, tests, NOTES.md, NEEDS-CORE.md written, and the fix round (F8 follows ruling (b); QB functions answer NOTHING and are renamed "... as the section requires"; Judgment calls section; forks F11-F19) applied. check.sh run on 1.6.109 and 1.6.108 after the last edit: 22 modules, 0 errors, 1108 satisfied, 0 failed, 0 refused, every module "same" (baseline: scja-core.l4 only, 0 assertions). srcrefs --refs, --strict and plain, each alone: 0 problems (1326 src: lines, 275 runs, 275 locators). The final report is the last message of the session.

Paths (session-specific): RUN = <scratch>/<job>/runs/iaw-scja2 ; DEPOSIT = RUN/deposit ; folder = DEPOSIT/encodings/legalese-sonnet-5.5 ; work dir (not shipped) = RUN/work ; inputs = RUN/inputs.
L4 = <bin>/l4-main-109 ; L4_MAIN = <bin>/l4-main-108.

## Method
- Layer 1 is written as templates in work/tpl/*.l4t with `@@Q` / `@@U` macros; work/gen.py expands them into the deposit folder; `cd work && python3 -I build.py <name>` rebuilds one (general civil appeals criminal capital-defs capital officers seat cases-seat tests-general tests-civil tests-appeals tests-criminal tests-capital-defs tests-capital tests-officers). The generated .l4 files are the artefact.
- NOTES.md is assembled by `python3 -I work/assemble.py` from work/notes/*.md, work/coverage.md (from `python3 -I work/cov.py`, which reads work/units.tsv and lines.tsv from `python3 -I work/units.py`) and work/notes/rulings.md (the four rulings, extracted from BRIEF.md by grep and pasted by the script). The jural table is rendered by work/jural.py. Edit the pieces in work/notes, never NOTES.md.
- Answer convention: MAYBE BOOLEAN; JUST FALSE only where the text says no in its own words; a prohibition with no gate is phrased as the permission it negates, one with a gate or an exception as the bar ("the bar ... applies"); forks F1-F19 are in NOTES.md, the case-by-case calls in its Judgment calls section.

## Done
- Layer 1: ss 30-34 / 48-52 (general), 35-45 / 53-60C (civil), 46-47 (appeals), 60D-60E (criminal), 60F (capital-defs), 60G-60M (capital), 61-72 (officers), each with tests; 21 regulative rules (23 traces), eleven of them SHANT rules derived under N2.
- Layer 2: scja2-seat.l4 (77 exported questions over 75 sections) and scja2-cases-seat.l4 (233 assertions, 71 NOTHING).
- NOTES.md: coverage (422 units; 218 line rows), fork register (F1-F19), Judgment calls (QA to QF), jural relations (138 rows), marginal readings M0-M10, reading a result, seams (rows 12-20 asked, row 11 answered), findings 1-7 and the list of what the text does not answer, main-binary list, check.sh output, dependencies, unstable-dialect line.
- NEEDS-CORE.md: one item (Hearing cannot count Judges unable to continue).

## Decisions taken (with licensing section) - all in NOTES.md fork register
- K1 (SICC as General Division): F1. K4 (quasi-criminal): F2. s 41(10)(b)/59(10)(b) 7 days: F3. s 60F relevant date and stray (ii): F4. s 67(1): F5. Panel sizes: F6, F10. s 66(1): F7. Gates, "unless" and "subject to" on bars, duties, powers: F8 (an unmet gate follows ruling (b) on the bar function and answers NOTHING on a grant-named function; a met "unless" answers NOTHING on the permission function and JUST FALSE on the bar function). "when" stages: F9. Bare "must" not done: F11. Schedules: F12. "Other than": F13. Civil input: F14. Closed lists: F15. 2-Judge panel losing a Judge: F16. Appointing outside the named class: F17. A single Judge taking evidence: F18. The 2022 Act's commencement date: F19.
- Seat helpers are prefixed `scja2 seat:`.

## If resumed
Nothing is pending but the final report of the fix round. Do not edit a .l4 file without re-running check.sh, srcrefs and the diagnostics comparison (work/diag-109.txt, diag-108.txt).
