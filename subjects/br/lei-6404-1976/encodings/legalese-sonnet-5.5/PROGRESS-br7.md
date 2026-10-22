# PROGRESS: br7 (Lei das Sociedades por Ações, Capítulos XXI a XXVI, lines 2326-2593)

Written by the piece agent br7. Re-read this file, NOTES.md and the text after any compaction, not a summary of them.

## Plan, fixed on 2026-10-22 (advisor-checked)

- Layer 1: one module per chapter, in the flat folder, each starting `IMPORT prelude`, `IMPORT daydate`, ``IMPORT `br-core` ``.
- Layer 2: `br7-seat.l4` (questions) and `br7-cases-seat.l4` (cases, one per question at least).
- Tests: `br7-tests-<chapter>.l4`, one per layer-1 module.
- Every name a module defines ends with its citation in parentheses; no section `GIVEN`; no `REFUSE`; every `NOT` bracketed; each `#ASSERT` on one line.
- Booleans for duties and conditions; a `PARTY ... MUST` rule only where the 5.2 three-question test says a duty with an act and a consequence (art. 296).
- Cross-references out of range are plain inputs with the comment `-- out of range: section N (piece X)`, listed in NOTES.md.
- The coverage table in NOTES.md is filled from the L4 `@ref` locators at the end by script: for each row, `where` is the rules whose `@ref (src:A-B)` overlaps the row's lines. Do not hand-type `where` for 100 rows.

## Module list and state

| file | covers | state |
| --- | --- | --- |
| `br7-cap21-grupo-de-sociedades.l4` | arts. 265-277 | done, `l4 check` clean, srcrefs 0 problems; imports cap25 |
| `br7-cap22-consorcio.l4` | arts. 278-279 | done |
| `br7-cap23-comandita-por-acoes.l4` | arts. 280-284 | done |
| `br7-cap24-prescricao.l4` | arts. 285-288 | done |
| `br7-cap25-disposicoes-gerais.l4` | arts. 289-294-B | done |
| `br7-cap26-disposicoes-transitorias.l4` | arts. 295-300 and the publication date | done |
| `br7-tests-cap21.l4` ... `br7-tests-cap26.l4` | layer-1 tests | all six done: 157, 25, 47, 74, 105, 172 assertions, 580 in all, all satisfied |
| `br7-seat.l4`, `br7-cases-seat.l4` | layer 2 | done 2026-10-22: 120 questions in 14 `§` groups, 509 assertions, all satisfied; generated from `br7-tools/seat/` (scratch), positive control run (two wrong assertions fail) |
| `NOTES.md` | all ten headings | done 2026-10-22: 135 coverage rows with `where` filled by script, fork register B1-B49, 19 cross-reference inputs, 7 needs, 34 findings, the binary table, the `check.sh` table pasted, the caveats |

## Decisions taken (with the provision that licenses each)

- Art. 295 and line 2592: br7 names the publication date (17 Dec 1976, DOU footer) and the entry into force (60 days later, `o termo final do prazo`: 15 Feb 1977); the enactment date (line 5, and the signature line 2589) is br1's, so br7 defines no enactment-date name.
- Art. 288: read as a bar on consummation, not a suspension (fork); while the criminal outcome is pending the answer is "not prescribed", a definite value.
- Art. 287, II, g: the text states no starting event, so the start date is a plain input and the row is a fork.
- Arts. 281 and 282 both apply to a director whose name is also in the firm: unlimited, joint and subsidiary (fork B17); a person named only in the firm is unlimited and joint, and the subsidiarity field is NOTHING.
- Struck wording is never encoded; lines 2479 (art. 289, § 4º), 2486 and 2488 (§§ 6º, 7º) are live although a "(Vigência encerrada)" or "(Revogado pela Medida Provisória nº 892)" note sits beside the struck paragraph above each of them (fork B27).

- Art. 296, § 1º: the rule returns MAYBE BOOLEAN (changed 2026-10-22 from BOOLEAN, with its tests): for a person the paragraph does not name the text does not answer, so NOTHING, not FALSE.

## Last check.sh (2026-10-22, run after the last change to any `.l4` file): 15 modules, errors 0, satisfied 1089 (580 tests, 509 seat cases), failed 0, refused 0, exit 0.

`l4 run` on each of the 14 `br7-` files: 0 `DiagnosticSeverity_Error` and 0 `DiagnosticSeverity_Warning` lines in every one.

`srcrefs.py check --refs` over every layer-1 module, test file, the seat and the cases: 341 src: lines, 151 runs, 175 locators, 0 problems.
The keel's instruction-12 check (every `src:N` of every `@ref` walked up to its `Art.` heading): 175 locators, no label names the wrong article (NOTES.md, finding 34).
No probe or scratch file is in this folder; the probes of the binary's refusals were run in the session scratchpad.

## What remains

Nothing in this folder is pending.
The final report goes in the last message.

## Files in this folder

- `NOTES.md`, `PROGRESS.md`.
- The six layer-1 modules, their six test files, `br7-seat.l4` and `br7-cases-seat.l4`.
- `br-core.l4`, `check.sh` and `srcrefs.py` were given and are not mine.
- Scratch tools (not deliverables) live in the session scratchpad, `br7-tools/`: `expand.py`, `build.sh`, the seat generator under `seat/`, `fillwhere.py` and `assemble.py` (which built NOTES.md from the fragments in `notes/`).
