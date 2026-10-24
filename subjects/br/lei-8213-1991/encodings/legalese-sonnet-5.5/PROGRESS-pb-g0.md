# PROGRESS: keel pb-g0, Lei nº 8.213/1991

Kept current. If context is compacted, re-read this file, `NOTES.md` and the text, not a summary.

## Status

- [x] Read the brief, both skills, `dialects.md`, `drafting-patterns.md`, phrasebook areas 1, 3, 4, 6, 9.1 and 11, `gotchas.md`, the encoding guide and the Commons CLAUDE.md.
- [x] Read the section index and the headings, and the Law in samples (arts. 9-27, 28-41-A, 42-58, 59-80, 86-124-A, 125-156), then re-read the structural articles from a live-lines-only listing.
- [x] Probed the stable binary (1.6.98): accented identifiers, `add months`, `add years`, records with accented backticked fields, `§` headings through an import, the `YMD` shim through an import, duplicate-name diagnostics, a regulative rule over `Parte`.
- [x] `pb-core.l4` written (quotation lines pasted by `srcrefs.py quote`; `srcrefs.py check --refs` 0 problems).
- [x] `pb-core-tests-vocabulario.l4` written (47 assertions, all satisfied).
- [x] Advisor review done; its fixes applied (an `@ref` on every declaration of the core after the first of a run, the footer no longer quoted, a row for the class of a dependant, F-9 for the day count, the check.sh paragraph corrected).
- [x] `NOTES.md` written under all the required headings.
- [x] `check.sh`: 0 errors, 47 satisfied, 0 failed, 0 refused.
- [x] Importability probe run and deleted; `deposit/probe/` deleted.
- [x] Final report (the last message).

## Decisions taken, and the provision that licenses each

| decision | licensed by |
| --- | --- |
| `Categoria de segurado` has six constructors, the live ones; incisos III and IV of art. 11 are revoked and get none | art. 11 (I, II, V, VI, VII), art. 13 |
| `Prestação` is art. 18's list (12 live items) plus `abono de permanência em serviço`, which arts. 80 and 124 III still name | art. 18; art. 80; art. 124 III |
| `tempo de serviço` and `tempo de contribuição`, `auxílio-doença` and `auxílio por incapacidade temporária`, `aposentadoria por invalidez` and `aposentadoria por incapacidade permanente` are one constructor each, named as art. 18 names them (F-3) | art. 18 I a, c, e; art. 29 I; arts. 52-56, 97; art. 101 |
| the core holds the Law's two dates (24.7.1991 in the title, 25.7.1991 in force) because pb2 and pb3 both read "a data de vigência desta Lei" (F-1) | title (line 5); art. 155; footer (line 1765) |
| `Valores de referência` is a three-field record | arts. 22, 29 § 2, 33, 39, 48 § 4, 73 |
| time limits are `Prazo` (quantity + unit); one helper gives the last day on which an act is in time | arts. 15, 49, 74, 103 |
| `Parte` constructors carry no article, so they never meet the standard input `o segurado` | naming only |
| `Segurado` and `Dependente` are records with the few facts several pieces read | arts. 10, 16 |

## Traps found while reading (all are in NOTES.md for the pieces)

- `⟦STRUCK:` spans run over several lines; a whole-line `grep -v` shows struck incisos as live. NOTES.md carries a command that lists live lines (checked against a regular-expression version: identical, 1157 lines).
- `srcrefs.py` needs a contiguous slice, so a line with a mid-line wrapper (line 152) is quoted whole or from after the wrapper.
- Duplicate rule or type names across modules are an error at the use; duplicate constructor names are accepted and resolved by the expected type.
- Art. 86 has seven opener lines (only line 1134 is live); art. 60, art. 74 § 2 and art. 101 have struck spans over several lines.
- 27 articles have no live opener line at all (listed per piece in NOTES.md, Instructions 4).
