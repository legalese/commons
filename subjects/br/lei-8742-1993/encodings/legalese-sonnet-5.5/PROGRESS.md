# PROGRESS — Lei nº 8.742/1993 (LOAS), encoding `legalese-sonnet-5.5`

Written for myself across context compactions. After a compaction: re-read this file, NOTES.md and the text, not a summary.

## State

- Started 2026-10-24.  Read in full: the brief, ENCODING-GUIDE, COMMONS-CLAUDE, the example seat, both skills, the whole text (534 lines).
- Binary: version 1.6.98 (from the extension's package.json), sha256 82ea44ad...263e (matches the brief).  The commit of the build is not known: the skills quote `1.6.98 (main, 7689b0d, 2026-10-19)` only as an example of `l4 --version` output, and the binary was not asked.
  Run check as `L4=<bin> L4_TARGET=unstable ./check.sh`; srcrefs as `python3 -I srcrefs.py check --refs <raw> lo-*.l4`.
- Rule: write files only under this folder; NO probe files may stay (delete `lo-zz-*.l4` before finishing).
- Method: I write modules with `@@Q n m` (quote lines) and `@@S n [m]` (verbatim string) placeholders, then expand them
  with an inline `python3 -I -` heredoc that calls `srcrefs.py quote` (never retype a source line).  The expander is
  not kept as a file (nothing outside this folder, and no stray file in it).

## Everything is written; last verification run

- `check.sh`: TOTAL (19 modules), 0 errors, 508 satisfied, 0 failed, 0 refused.
- `srcrefs.py check --refs`: 207 src: lines, 121 runs, 152 locators, 0 problems.
- NOTES.md has all nine headings; the coverage table has 214 rows (98 encoded, 33 fork, 72 inert, 11 repealed or blank), every source line 1-534 is in exactly one row and every one of the 71 articles has a row (both checked by script).
- Every backticked rule name in NOTES.md was checked by script against the names in the `.l4` files.
- 16 `-- out of text:` comments sit above the outside-the-text inputs in layer 1 (added after the first full run; check.sh and srcrefs were re-run after adding them: same 508 satisfied, 0 problems).
- The fork register has 21 entries (F-21 added for the art. 6º-B / 6º-C caput overlap); art. 26-G § 1º is `inert` (budget administration), with its open question kept in F-14.

## Layer 1 (all green)

| module | arts | tests |
|---|---|---|
| lo-nouns | types, enumerations (DECLARE only) | - |
| lo-datas | date of the Law, publication, art. 41, deadlines of arts. 28 §2, 32, 33, 34, 40 §2 | lo-tests-cap5-cap6 |
| lo-cap1-2-principios | arts. 1-4 (art. 5 inert) | lo-tests-cap1-2 |
| lo-cap3-organizacao | arts. 6-A..6-F, 9, 12-15 (table), 19 p.u. | lo-tests-cap3 |
| lo-bpc-concessao | arts. 20, 20-B, 37, 40-B | lo-tests-bpc-concessao |
| lo-bpc-manutencao | arts. 21, 21-A, 21-B, 40-C | lo-tests-bpc-manutencao |
| lo-eventuais-servicos | arts. 22-25 | lo-tests-eventuais |
| lo-auxilio-inclusao | arts. 26-A..26-H | lo-tests-auxilio-inclusao |
| lo-cap5-financiamento | arts. 28, 30 | lo-tests-cap5-cap6 |
| lo-cap6-gerais | arts. 29 p.u./35, 31, 36, 40, 40-A | lo-tests-cap5-cap6 |

## Layer 2 (all green)

`lo-seat.l4`: 82 `@export` questions in 14 `§§` groups.  `lo-cases-seat.l4`: 149 assertions, at least one per question.

## Decisions taken (with the provision that licenses each)

- Minimum wage is a plain input everywhere (the text never gives it): art. 20 caput, § 3º, § 11-A; 22 § 2º; 26-A I a); 26-B.
- Per capita income limit: 1/4 (art. 20 § 3º) unless the regulation widens it (§ 11, § 11-A, art. 20-B); a widened fraction is cut to [1/4, 1/2].
- A family with no member has no per capita income: NOTHING / `o texto não permite responder` (art. 20 § 1º makes the applicant a member).
- Art. 3 caput: "sem fins lucrativos" qualifies all three kinds (F-01).
- Art. 21-B: "pequeno porte" = municipality of 50,000 inhabitants or fewer (complement of inciso II) (F-11).
- Art. 21-A § 2º: apprentice, up to 24 months of concurrent receipt, not suspended; after that the caput applies (F-10).
- Art. 26-A § 1º: "5 anos imediatamente anteriores" = last receipt not later than the activity start and not more than 5 years before it.
- Purpose/definition provisions that decide nothing are carried (typed lists, or verbatim strings with @@S) and marked `encoded`, not `inert`.
- Arts. 5 and 6 (directives and organisation of the Suas) are `inert` as machinery ("organises the system", brief line 57), although art. 4 (principles) is carried; a reviewer may prefer art. 5 carried as a typed list too.

## Files written

PROGRESS.md, NOTES.md, lo-nouns.l4, lo-datas.l4, lo-cap1-2-principios.l4, lo-cap3-organizacao.l4,
lo-bpc-concessao.l4, lo-bpc-manutencao.l4, lo-eventuais-servicos.l4, lo-auxilio-inclusao.l4, lo-cap5-financiamento.l4,
lo-cap6-gerais.l4, lo-seat.l4, lo-cases-seat.l4, lo-tests-cap1-2.l4, lo-tests-cap3.l4, lo-tests-bpc-concessao.l4,
lo-tests-bpc-manutencao.l4, lo-tests-eventuais.l4, lo-tests-auxilio-inclusao.l4, lo-tests-cap5-cap6.l4
(+ check.sh, srcrefs.py given).
