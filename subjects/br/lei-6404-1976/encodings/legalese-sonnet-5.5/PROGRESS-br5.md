# PROGRESS: piece br5 (Capítulos XV e XVI, lines 1555-1957, Arts. 175 to 205)

Written by the piece agent `br5`. Updated as work lands; re-read this file and NOTES.md after any compaction.
State: every module, test file, the seat, the cases and NOTES.md are written; the last `check.sh` run is green (see NOTES.md, "What check.sh prints").

## Working method

- Placeholders `##L A B` in a module expand to `-- src:N | text` quote lines (live lines only, copied by `srcrefs.py quote` from the raw file) with `inputs/work/expand.py`. `inputs/live-br5.txt` is the struck-stripped copy, line numbers equal the raw file's.
- Each module is run with `l4 run` right after it is written; the numbers come from `check.sh`.
- `inputs/work/env.sh` defines `L4`, `D` (this folder), `IN` (inputs) and a `run FILE` helper; `inputs/work/coverage.tsv` holds the coverage rows (edit with `setrows.sh`, render into NOTES.md with `render_coverage.py`).
- NOTES.md is assembled by `inputs/work/write_notes.py`, which reads every count from the files and runs the two source-reference checks, so the numbers in NOTES.md cannot drift from the code; the coverage block between its markers is left as rendered.

## Plan (modules, in order)

| module | articles | status |
| --- | --- | --- |
| br5-vocabulario.l4 | nouns used by several modules | done |
| br5-exercicio-social.l4 | 175 | done, tests pass (12) |
| br5-demonstracoes.l4 | 176, 177 | done, tests pass (75) |
| br5-balanco.l4 | 178 to 185 | done, tests pass (122) |
| br5-demonstracoes-contas.l4 | 186 to 188 | done, tests pass (67) |
| br5-lucro.l4 | 189 to 192 | done, tests pass (42) |
| br5-reservas.l4 | 193 to 200 | done, tests pass (97) |
| br5-dividendos.l4 | 201 to 205 | done, tests pass (121) |
| br5-seat.l4, br5-cases-seat.l4 | layer 2 | done: 76 questions, 186 cases, every question has a case |
| NOTES.md | all ten sections | written; coverage table has 110 rows, none deferred |

## What changed in the last pass (found by re-reading the text, not by a failing test)

- Art. 196, § 2º: "poderá ... revisado anualmente" was encoded as a duty (`deve`); it is a permission and only for a budget longer than one exercício, otherwise NOTHING. The rule was renamed `o orçamento de capital pode ser revisado anualmente (art. 196, § 2º)` and returns a `MAYBE BOOLEAN`; its two layer-1 assertions were rewritten from the text, and the coverage row and fork F-196-2 say so.
- Arts. 200, inciso V, and 201 cite "artigo 17, § 5º", which in the live Art. 17 is § 6º (fork F-17, finding 1 in NOTES.md). The inputs keep the citation and describe the fact by its content.
- Out-of-range comments (`-- out of range: ...`) were added to every input that stands for a provision of another piece: Art. 243 (three declarations), Art. 247, Arts. 248 to 250, Art. 248, Art. 17 (the capital-reserve dividend in two modules, the priority and cumulation of Art. 203 in one), Art. 161, Arts. 41 and 43; and the same comments sit above the seat questions that ask them.
- New rule `a participação no capital social de outra sociedade é avaliada pelo custo de aquisição (art. 183, inciso III)` carries the carve-out "ressalvado o disposto nos artigos 248 a 250" as a plain input (fork F-183-248), with two tests and a seat question with two cases.
- Fifteen seat questions were added (61 before, 76 now) so that a shareholder can ask what bears on dividends, retention and what the company may do to them, and the valuation of liabilities for symmetry with assets: Art. 176, § 2º; Art. 183, § 3º (two), § 4º and inciso III; Art. 184, incisos I to III; Art. 195, § 1º; Art. 196, §§ 1º and 2º (three); Art. 197, § 2º (two); Art. 199. 26 layer-1 rules remain without a seat question and NOTES.md lists them by citation.

## Decisions taken

See NOTES.md, "Fork register": each fork has its ID, the readings seen, the one taken and the text that licenses it. IDs cited in module comments are the same.
An earlier list of forks in this file named F-200, which has no entry in the register: no ambiguity could be substantiated for Art. 200 (the list is exhaustive by "somente poderão"), so none is recorded.

## Files written

Layer 1: br5-vocabulario.l4, br5-exercicio-social.l4, br5-demonstracoes.l4, br5-balanco.l4, br5-demonstracoes-contas.l4, br5-lucro.l4, br5-reservas.l4, br5-dividendos.l4.
Tests: br5-tests-exercicio-social.l4, br5-tests-demonstracoes.l4, br5-tests-balanco.l4, br5-tests-demonstracoes-contas.l4, br5-tests-lucro.l4, br5-tests-reservas.l4, br5-tests-dividendos.l4.
Layer 2: br5-seat.l4, br5-cases-seat.l4.
Notes: NOTES.md, PROGRESS.md.
Read-only, not mine: br-core.l4, check.sh, srcrefs.py.

## Remaining

Nothing in my range. Open points are in NOTES.md, "Before this is worth relying on".
