# PROGRESS (sfad: Securities and Futures Act 2001, Part 13 Division 1 Subdivisions 3, 4, 5; lines 41833-45043)

Status, 2026-11-19: every module, every tests file, the seat and its cases are written; `NOTES.md` is generated and read.
The numbers below were read from runs on 2026-11-19 (the full `check.sh` with `l4-main-110` and `l4-main-109`, `l4 check` on both builds, `srcrefs.py check --refs` and `--strict`, `work/trace_check.py`, `work/coverage.py`).

Method: layer-1 modules are written as templates in `DEPOSIT/../work/tpl/*.tpl` and expanded by `DEPOSIT/../work/expand.py`.
It copies the quote lines mechanically from `SFA2001.txt` with `srcrefs.py`'s own quote function, skipping page furniture and amendment marks.
Fragments of `NOTES.md` live in `DEPOSIT/../work/notes/` and `NOTES.md` is assembled by `DEPOSIT/../work/assemble_notes.py`.

## Module plan

| module | provisions | status |
| --- | --- | --- |
| `sfad-debentures.l4` (+ `sfad-tests-debentures.l4`) | ss 261-271 | DONE: 117 top-level MEANS, 0 errors 0 warnings on both builds, srcrefs strict 0 problems, 302 of 302 assertions satisfied, 41 traces all as EXPECTed, builds 109 and 110 agree on all 41 |
| `sfad-nocons-small-private.l4` (+ tests) | ss 272, 272A, 272B | DONE: 49 MEANS, 193 of 193 assertions, no traces, builds agree |
| `sfad-circumstances.l4` (+ tests) | s 273 | DONE: 51 MEANS, 175 of 175 assertions, 2 traces as EXPECTed, builds agree |
| `sfad-investor-exemptions.l4` (+ tests) | ss 274, 275, 276 | DONE: 24 MEANS, 121 of 121 assertions, builds agree |
| `sfad-ois-intl-gov-atm.l4` (+ tests) | ss 277-282 | DONE: 48 MEANS, 179 of 179 assertions, 2 traces as EXPECTed, builds agree; answers seam S3 |
| `sfad-directions.l4` (+ tests) | s 282AA | DONE: 10 MEANS, 29 of 29 assertions, 2 traces as EXPECTed, builds agree |
| `sfad-exemption-summary.l4` (+ tests) | seams S4 and S5 (BOOLEAN answers) | DONE: 3 MEANS, 12 of 12 assertions, builds agree |
| `sfad-seat.l4`, `sfad-cases-seat.l4` | layer 2, the seat | DONE: 40 questions (`@export`), 134 of 134 assertions in the cases file, 0 errors 0 warnings, builds agree; the seat imports the layer-1 modules and not the keel |

Whole deposit, `check.sh` TOTAL (28 modules, the keel's twelve included): 0 errors, 1145 assertions satisfied, 0 failed, 0 refused, main build `same` on every row.
Coverage, `work/coverage.py`: 244 cited provisions; 2072 text lines; 2029 in a locator; 43 in none (29 classified runs, all headings or repealed text); GAPS 0; encoded functions with no mention in any tests file: 0.
Forks: 120 entries (`-- FORK` lines).
Split sites: 12 of (i), all JUST FALSE; 12 of (ii), 10 JUST FALSE and 2 NOTHING (counts read from `grep SPLIT-SITE`, not from memory).

## Decisions taken (provision: reading)

The fork register of `NOTES.md` holds every one, with the other reading and the licence; this list is a pointer to the ones a reader meets first.

- Exemption functions (ss 272, 272A, 272B, 273, 274, 275): JUST TRUE where all limbs are met; JUST FALSE where a failed "if" limb is shown; NOTHING outside the scope the section names (periods ruling (c)).
- Limb results are inputs of type MAYBE BOOLEAN to the function for the section (the keel's way); the seat layer asks the limbs.
- "Immediately" is a promptness standard with no measure, so no `WITHIN` (forks s268-9i, s268A-3i, s268A-4i, s270-5i).
- Split sites (i), 12, all JUST FALSE: ss 261(1D), 265A(4), 268(7), 268(7A), 268A(5), 268A(8), 268A(10), 269(3), 273(8), 273(8B), 277(8), 282AA(4).
- Split sites (ii), 12: JUST FALSE (periods ruling (b)) at ss 266(2), 266(4), 266(5), 270(3), 270(5), 273(6), 276(6), 277(1AB), 277(1AD), 277(2); NOTHING (grant ruling) at ss 281(1) and 282AA(1), where the gate is the Authority's own opinion.

## Tooling (all under `DEPOSIT/../work/`, not shipped)

- `tpl/<module>.N.tpl`: chunks of a module, expanded by `build.sh` (`expand.py`: `@@REF`, `@@Q` and `@@AT` quote directives; `-- DEF X = text` macros; `{{X}}`).
- `tpl/<tests>.test.tpl`: tests, built and run on builds 110 and 109 by `runtests.sh` (`mktests.py`: `-- MODULES a b`, and `{{fn s 273(1)(cd)}}` expands to the backticked function name).
- `trace_check.py`: pairs `-- EXPECT word` with #TRACE results, counts assertions, compares two builds.
- `check_quotes.py`: the quoted fragments of FALSE-kind and NOTHING-kind comments occur in the text.
- `sig.py`: function signatures.
- `gen_seat.py`: writes `sfad-seat.l4` from a table of questions; `tpl/sfad-cases-seat.test.tpl` is the cases file.
- `notes/*.md`: fragments of `NOTES.md` (`macros.txt` holds the ruling tags such as `{P-b}` with the Guide line numbers; the `*.jural.md` and `*.nobreach.md` fragments; `findings.md`; `binary.md`).
- `assemble_notes.py`: collects the `-- FORK` lines of the modules into the fork register and writes `NOTES.md` with the coverage table, the split-site tables and the check output.
- `coverage.py`: builds the coverage rows from the `@ref` locators of the modules and checks every non-blank line of the range (`--table`, `--gaps`).
