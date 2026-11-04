# PROGRESS -- ssc8 (Social Security Contributions and Benefits Act 1992, lines 4454-5066)

Re-read this file, `NOTES.md` and the text (`inputs/ukpga-1992-4.txt` lines 4454-5066) after any compaction, not a summary of them.

## How the files are made

- Layer 1 modules and tests: `ssc8-*.l4` in this folder, expanded from templates by `work/build_l4.py` (`{{Q a b}}` quotes lines a to b, `{{R label | a b}}` quotes them and adds the `@ref`).
  Edit `work/src/<file>.tpl`, then `python3 -I work/build_l4.py <file>` from `work/`; never edit the `.l4` by hand.
- `NOTES.md` is BUILT, not hand-edited: `python3 -I work/build_notes.py` concatenates `work/notes/*.md` (hand-written fragments, numbered), the coverage table from `work/cov_rows.py`, the marginal-reading tables read from the `-- FALSE-kind` and `-- NOTHING-kind` comments in the modules, and the last `check.sh` output in `work/check-out.txt`.
  The generator also checks that the rows cover every non-blank line 4454-5066 exactly once.
- Scratch probes live in `work/` (not shipped).

## Binaries

- `L4_BIN` = `.../scratchpad/bin/l4-stable-98` (stable 1.6.98), `L4_MAIN` = `.../scratchpad/bin/l4-main-108` (1.6.108, 2ae7c9b).
- Run: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh`.

## Status

| unit | state |
| --- | --- |
| orientation (brief, PLAN, KEEL-NOTES, guide, skills, text) | done |
| coverage rows (287 rows, 613 non-blank lines, no gap or overlap; 281 before the audit split of Sch 1 para 8(1)) | done |
| ssc8-sch3.l4 + tests (172 assertions) | done |
| ssc8-sch4.l4 (seams S2, S34) + tests (8) | done |
| ssc8-sch4b.l4 + tests (53) | done |
| ssc8-sch4a.l4 + tests (94) | done |
| ssc8-sch2.l4 + tests (73) | done |
| ssc8-sch1a.l4 + tests (149 assertions, 5 traces) | done |
| ssc8-sch1b.l4 + tests (132 assertions, 1 trace) | done |
| ssc8-seat.l4 (27 questions) + ssc8-cases-seat.l4 (64 assertions) | done |
| NOTES.md (built from fragments) | done |
| check.sh | exit 0; 17 modules, 745 satisfied, 0 errors, 0 failed, 0 refused; every module the same on main 1.6.108 |
| srcrefs.py check and --strict | 496 src lines, 187 runs, 187 locators, 0 problems, both |

## Decisions taken (with the text that licenses each)

The fork register in `NOTES.md` has every reading taken, with the text that licenses each (F-S1-1, -3, -4, -5, -6, -7, -8, -9; F-S2-1; F-S3-1 to -5; F-S4B-1).
Other choices, each "assumed, not ruled":

- Schedule 4 rows are `repealed or blank in this text` (PLAN section 4 and the brief's four dispositions); its four rates are `MAYBE NUMBER` pass-throughs for seams S2 and S34.
- Every rate, band, percentage, threshold and order increase is an input; the numbers the Act states itself (25 and 50 times the lower earnings limit, 30 years, N = 0.5, 20, 10%, 44, 20%, 72.80, 93.60) are typed in.
- Schedule 3 paragraph 5A(1): the Category B limb ("in the cases provided for by any of sections 48A to 51ZA") answers `NOTHING` outside, as paragraph 5(1)(c) does with the same words; the Category A limb ("in a case where ... on or after 6th April 2010") answers `JUST FALSE` before 6 April 2010 (reading (a), listed under "Marginal readings").
- Triage after the independent review (2026-11-04): `sch 4A para 3(3) Part II does not apply because of the condition` had its polarity inverted (it answered `JUST FALSE` where the text says Part II does not apply); it now answers `JUST TRUE` when the condition holds in one or more tax weeks and `JUST FALSE` when it holds in none (reading (a), as in 3(1) and 2(1)). Three expectations of my own changed (`ssc8-tests-sch4a.l4` lines 123-125). The other five items are `NOTHING` by reading (b) and unchanged; see `runs/iaw-ssc8/TRIAGE-REPLY.md`.
- Paragraph labels counted from position are marked † in `NOTES.md` and listed in its head.

## Files written

- `ssc8-sch1a.l4`, `ssc8-sch1b.l4`, `ssc8-sch2.l4`, `ssc8-sch3.l4`, `ssc8-sch4.l4`, `ssc8-sch4a.l4`, `ssc8-sch4b.l4` and the tests `ssc8-tests-sch1a.l4`, `ssc8-tests-sch1b.l4`, `ssc8-tests-sch2.l4`, `ssc8-tests-sch3.l4`, `ssc8-tests-sch4.l4`, `ssc8-tests-sch4a.l4`, `ssc8-tests-sch4b.l4`.
- `ssc8-seat.l4`, `ssc8-cases-seat.l4`.
- `NOTES.md`, `PROGRESS.md`.
- No `NEEDS-CORE.md`: the core was enough (every type or constructor I lacked I declared under the `sch ...` prefix).
- `ssc-core.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`: supplied (read-only), unchanged.
