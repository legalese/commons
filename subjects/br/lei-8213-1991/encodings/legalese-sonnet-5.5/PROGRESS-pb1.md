# PROGRESS: pb1 (Lei nº 8.213/1991, lines 1-454)

Status as of 2026-10-24: every deliverable of the brief is written and checked.
The decisions and the evidence are in `NOTES.md`; this file only says what exists and how it was checked.

## Paths and tools

- RAW (the source text): `../../registers/source-bundle/lei-8213-1991.pt.txt`
- L4 (stable 1.6.98): `l4`
- Check: `L4=<the path above> L4_TARGET=unstable ./check.sh`, and `python3 -I srcrefs.py check --refs RAW pb1-*.l4`.
- The temporary helpers (`zz-l4`, `zz-expand.py`, and the scripts that generated the coverage table and the fork register) have been deleted; `grep -c '@@Q' pb1-*.l4` prints 0 for every file.

## What was checked, after the last edit of any `.l4` file

- `check.sh`: 24 modules, 0 errors, 762 assertions satisfied (171 in `pb1-cases-seat.l4`, 591 in the nine test files), 0 failed, 0 refused, none expected to fail.
- `l4 run` on each of the 24 files: no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`.
- `srcrefs.py check --refs` and `--strict`: `313 src: lines, 143 runs, 197 locators, 0 problems`.
- Every line 1 to 454 falls inside the `src:` range of at least one row of the coverage table (192 rows), and so does each of the 242 live labelled units.
- Every one of the 81 seat questions has `@export`, every input has `@desc`, and every question has at least one case.

## Files

Layer 1: `pb1-titulo-i-principios`, `pb1-titulo-ii-regimes`, `pb1-art-10-14-beneficiarios`, `pb1-art-11-i-ii-vi-empregado-domestico-avulso`, `pb1-art-11-v-contribuinte-individual`, `pb1-art-11-vii-segurado-especial`, `pb1-art-11-segurado-obrigatorio`, `pb1-art-15-qualidade-de-segurado`, `pb1-art-16-17-dependentes-inscricao`, `pb1-art-18-prestacoes`, `pb1-art-19-23-acidente-do-trabalho`, `pb1-art-24-27a-carencia` (all `.l4`).
Tests: `pb1-tests-art-01-14`, `pb1-tests-art-11-i-ii-vi`, `pb1-tests-art-11-v-e-caput`, `pb1-tests-art-11-vii`, `pb1-tests-art-15`, `pb1-tests-art-16-17`, `pb1-tests-art-18`, `pb1-tests-art-19-23` (three `#TRACE`), `pb1-tests-art-24-27a`.
Layer 2: `pb1-seat.l4` and `pb1-cases-seat.l4`.
Reports: `NOTES.md` (ten headings) and this file.

## Forks

`pb1-F-1` to `pb1-F-27` are registered in `NOTES.md`, "Fork register", each with the readings seen, the one taken and the text that licenses it.
`pb1-F-19` to `pb1-F-27` were added late; their ids are in the comments of the modules beside the rule they govern.

## Corrections made while closing

- The input for the art. 39 sole-paragraph proof had a name that stated a content (twelve months) that is not in my range; it was renamed to `a segurada especial fez a prova a que se refere o parágrafo único do art. 39` (and the seat's `fiz a prova a que se refere o parágrafo único do art. 39`), with its `@desc`.
- A test comment cited `pb1-F-7` for the "menor benefício"; the fork is keel F-7 (pb1-F-7 is "de imediato" in art. 22).
- Coverage-table rows that quoted the seat questions from memory were replaced by the names of the `DECIDE`s in `pb1-seat.l4`, read from that file.
