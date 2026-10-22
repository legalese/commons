# PROGRESS: br2 (Capítulos V a IX of the Lei das Sociedades por Ações, lines 372-807)

Written by the piece agent `br2`. Updated after each unit landed. After a compaction, re-read this file, `NOTES.md` and the text, not any summary.

## State (2026-10-22)

- Layer 1 is written for the whole range (Art. 52 to Art. 105): nine modules, nine test modules.
- Layer 2 is written: `br2-seat.l4` (47 questions under six `§§` headings) and `br2-cases-seat.l4` (136 assertions).
- `NOTES.md` carries all ten required headings. The coverage table has 155 rows, none left `TODO`.
- `check.sh` (`L4_TARGET=unstable`): TOTAL (21 modules), 0 errors, 845 satisfied, 0 failed, 0 refused. Assertions written: 845.
- `srcrefs.py check` over `br2-*.l4`: 0 problems.

## Method decisions (taken before writing; each is licensed by the brief or the keel notes)

1. **No regulative rules.** `#ASSERT` cannot compare a `DEONTIC` value and `check.sh` counts only assertions, so a duty with a time limit is written as a compliance rule over the core's `Prazo` (`o ato foi praticado dentro do prazo`), which is assertable and which the seat layer can call.
2. **One rule per provision**, named for what it decides and ending in its citation; every rule carries `@ref art. N (src:A-B)` whose quote lines are copied mechanically from the raw file (`srcrefs.py quote`), live lines only (a line holding the struck marker is never quoted).
3. **A faculty with no condition** ("A companhia poderá ...") is a rule over an enumeration of the acts that provision lists, answering TRUE for each; a faculty with conditions is a rule over those conditions.
4. **No input shares a name with a core constructor or core rule** (measured: `GIVEN `o fundador`` clashes with the core's `Parte` constructor: "multiple definitions").
5. **No date is built.** The range holds neither the enactment date (br1) nor the entry into force (br7).
6. **Chapter and section headings** (CAPÍTULO V to IX, SEÇÃO I to X) are `§` headings, not coverage rows.

## Units

| unit | articles | module | tests | state |
| --- | --- | --- | --- | --- |
| Cap. V, Seções I e II | 52-58 | `br2-cap5-debentures-caracteristicas.l4` | `br2-tests-cap5-caracteristicas.l4` (95) | done |
| Cap. V, Seções III a V | 59-65 | `br2-cap5-debentures-emissao.l4` | `br2-tests-cap5-emissao.l4` (118) | done |
| Cap. V, Seção VI | 66-70 | `br2-cap5-agente-fiduciario.l4` | `br2-tests-cap5-agente-fiduciario.l4` (96) | done |
| Cap. V, Seções VII a X | 71-74 | `br2-cap5-debentures-assembleia-extincao.l4` | `br2-tests-cap5-assembleia-extincao.l4` (84) | done |
| Cap. VI | 75-79 | `br2-cap6-bonus-subscricao.l4` | `br2-tests-cap6-bonus-subscricao.l4` (28) | done |
| Cap. VII, Seções I e II | 80-87 | `br2-cap7-constituicao-requisitos.l4` | `br2-tests-cap7-constituicao-requisitos.l4` (107) | done |
| Cap. VII, Seções III e IV | 88-93 | `br2-cap7-constituicao-particular.l4` | `br2-tests-cap7-constituicao-particular.l4` (38) | done |
| Cap. VIII | 94-99 | `br2-cap8-formalidades.l4` | `br2-tests-cap8-formalidades.l4` (51) | done |
| Cap. IX | 100-105 | `br2-cap9-livros.l4` | `br2-tests-cap9-livros.l4` (92) | done |
| seat | 47 questions | `br2-seat.l4` | `br2-cases-seat.l4` (136) | done |
| notes | `NOTES.md` | all ten headings | | done |

## Files written

`br2-cap5-debentures-caracteristicas.l4`, `br2-cap5-debentures-emissao.l4`, `br2-cap5-agente-fiduciario.l4`, `br2-cap5-debentures-assembleia-extincao.l4`, `br2-cap6-bonus-subscricao.l4`, `br2-cap7-constituicao-requisitos.l4`, `br2-cap7-constituicao-particular.l4`, `br2-cap8-formalidades.l4`, `br2-cap9-livros.l4`; the nine `br2-tests-*.l4`; `br2-seat.l4`, `br2-cases-seat.l4`; `NOTES.md`; `PROGRESS.md`. The keel's `br-core.l4`, `check.sh` and `srcrefs.py` were already in the folder and are untouched.
