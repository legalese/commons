# PROGRESS (snap3): lines 913-1340 and 1796-1910 of usc07-ch51.txt

Status 2026-11-04: all deliverables are written and `check.sh` is green.
After a compaction re-read this file, `NOTES.md` and the text, not a summary.

## Paths

- DEPOSIT folder: `<the lead's scratchpad>/runs/iaw-snap3/deposit/encodings/legalese-sonnet-5.5/`
- Raw text: `.../runs/iaw-snap3/inputs/usc07-ch51.txt`.
- Work scripts (not shipped): `.../runs/iaw-snap3/work/` (`expand.py` template expander, `coverage.py` coverage table, `marginal.py` marginal-readings table, `seams_md.py` SEAMS.md generator, `assemble_notes.py` NOTES.md assembler, `verifyq.py` quote checker, `gen_cola.py` USDA table generator).
- L4 = `.../scratchpad/bin/l4-stable-98` (1.6.98); L4_MAIN = `.../scratchpad/bin/l4-main-108` (1.6.108).
- Templates (`*.l4.in`, with `--CITE a-b | text` lines) live in `work/src/`; the expanded `.l4` go to the deposit folder.
  NEVER edit an expanded `.l4` by hand: edit the template and re-run `python3 -I work/expand.py <name>.l4`.

## Done (2026-11-04)

Layer 1 and tests (errors 0, warnings 0, assertions satisfied = written, on the stable binary and the same on main):

- `snap3-logic.l4` (12 assertions);
- `snap3-s2016-a-to-g.l4` + tests (98), `snap3-s2016-h.l4` + tests (162, with 4 `#TRACE` outcomes), `snap3-s2016-i-to-k.l4` + tests (102);
- `snap3-s2016a.l4` + tests (82);
- `snap3-s2017-cola.l4` + tests (60), `snap3-s2017.l4` + tests (140);
- `snap3-s2022.l4` + tests (119), `snap3-s2023.l4` + tests (93), `snap3-s2024.l4` + tests (79).

Layer 2: `snap3-seat.l4` (36 questions, `@export` + `@desc`) and `snap3-cases-seat.l4` (102 assertions).

Documents: `NOTES.md` (all sections the brief names), `SEAMS.md` (ASKS and ANSWERS), this file.

Gates, run last on 2026-11-04:

- `check.sh`: 22 modules, 0 errors, 1049 satisfied, 0 failed, 0 refused; main columns equal on every module.
- `srcrefs.py check --refs` and `--strict`: 651 `src:` lines, 243 locators, 0 problems.
- `work/coverage.py check`: 537 non-blank lines, 396 units, 283 rows (184 encoded, 22 fork, 56 inert 1, 21 inert 2), 0 problems; plus 11 USDA rows added in NOTES.md.
- `work/verifyq.py`: 0 quotes not found.

## Not done / open

Nothing is open in my range.
Known deviations, all recorded in `NOTES.md`: 20 seam inputs that name a fact another section decides are not named for the answering section, and 17 of them are plain `BOOLEAN` rather than `MAYBE BOOLEAN` (SEAMS.md); the guidance power of section 2016a(a)(1) is filed inert (2) (Marginal readings); the two hortatory clauses of section 2016(h)(1) are encoded as always-`NOTHING` functions, not filed inert.

## Decisions taken (assumed, not ruled)

- Helper functions are named `snap3 ...` (unique by construction; not a provision).
- A prohibition or condition function answers `MAYBE BOOLEAN` with TRUE = the text affirmatively permits, FALSE = the text says no, NOTHING otherwise.
- The fourteen forks are in `NOTES.md`, Fork register, with the reading taken and the text that licenses each.
- The fiscal year 2027 tables come from `inputs/fna-snap-cola-fy2027.txt` by `work/gen_cola.py` and are replaceable inputs.

## Triage of the independent test pass (2026-11-04)

An independent reviewer's assertions failed 23 times in my range of the text.
`NOTES.md`, "Triage of the independent test pass", has one row per item with the text, the code location and the verdict.
Result: two are defects (348a and 348d, one function, fixed); one is a reviewer's slip (356), one is a fork (S3.27, new fork F-2024-3), and 19 are `NOTHING`-kind branches that I left as they were because no ruling has been made on readings (a) and (b).
One defect not on the reviewer's list was found and fixed: with a waiver (or a finding) supplied, `s 2016(h)(1)(A) ...` and `s 2016(h)(14)(C)(i) ...` returned `NOTHING` even when the date met the deadline, and they now return `JUST TRUE`.
Files changed: `snap3-s2016-h.l4` (those two functions), `snap3-tests-s2016-h.l4` (five assertions added, none changed), `snap3-s2016a.l4` (the period predicate answers `JUST TRUE` inside the period), `snap3-tests-s2016a.l4` (two of my expectations changed, lines 73 and 74), `snap3-s2024.l4` (comment lines only), `snap3-s2016-a-to-g.l4` (one comment line, 318, noting that the function answers subparagraph (A) alone), `NOTES.md`, `PROGRESS.md`, `SEAMS.md` (regenerated).
None of the reviewer's cases on those two functions changes its answer.
A second pass against the brief's own wording (BRIEF.md lines 55-56) and the other parts' rules found the period-predicate defect above and otherwise changed no code: it named the NOTHING ground for each of the 21 `NOTHING`-kind rows, found the 356 expectation to be an input slip (the cost of the thrifty food plan versus the published maximum allotment), and recorded the cap question as Marginal readings item 10, with the assertions that would change under either ruling.
