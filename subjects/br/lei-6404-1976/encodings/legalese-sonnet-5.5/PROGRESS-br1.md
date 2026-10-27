# PROGRESS: br1 (Capítulos I a IV, lines 1-371)

Written by the piece agent `br1`. Re-read this file, `NOTES.md` and the text (not a summary) after any compaction.

## State (2026-10-22)

- Everything the brief asks for is written: layer 1 (nine modules, nine test files, 228 rules, 759 assertions satisfied), layer 2 (`br1-seat.l4`, 165 questions; `br1-cases-seat.l4`, 477 cases, all satisfied) and every section of `NOTES.md` (coverage table of 191 rows, fork register F12 to F45, jural relations of 171 rows, cross-references, needs from the core, 24 findings, binary findings, the `check.sh` table, caveats).
- `check.sh` with `L4_TARGET=unstable`: 21 modules, 0 errors, 1236 assertions satisfied, 0 failed, 0 refused (the table is pasted in `NOTES.md`).
- Mechanical checks run at the end (after the last edit to any `.l4`): `python3 -I srcrefs.py check --refs <raw text> br1-*.l4` printed "216 src: lines, 163 runs, 242 locators, 0 problems"; the coverage check (191 rows, 318 live non-blank lines all covered, no line in two rows, a row for each of the 51 live article headings); the canonical `@desc` strings equal the KEEL table verbatim (12 of its 16 names are asked in this range).
- The temporary `zz-*` helpers and `__pycache__` were deleted on 2026-10-22; an `ls` afterwards showed 25 entries: `br-core.l4`, `check.sh`, `srcrefs.py`, `NOTES.md`, `PROGRESS.md` and 20 `br1-*.l4` files (nine modules, nine test files, `br1-seat.l4`, `br1-cases-seat.l4`).
- Nothing is left to do except the final report.

## Plan (modules, one per Chapter or Section group of the source)

| module | articles | lines | tests file | state |
| --- | --- | --- | --- | --- |
| br1-cap1-natureza | title block, Arts. 1-4-A | 1-38 | br1-tests-cap1-natureza | done |
| br1-cap2-capital | Arts. 5-10 | 39-64 | br1-tests-cap2-capital | done |
| br1-cap3-secoes1-2-numero-e-preco | Arts. 11-14 | 65-84 | br1-tests-cap3-secoes1-2 | done |
| br1-cap3-sec3-especies-e-classes | Arts. 15-19 | 85-147 | br1-tests-cap3-sec3 | done |
| br1-cap3-secoes4-5-forma-e-certificados | Arts. 20-27 | 148-193 | br1-tests-cap3-secoes4-5 | done |
| br1-cap3-sec6-propriedade-e-circulacao | Arts. 28-38 | 194-252 | br1-tests-cap3-sec6 | done |
| br1-cap3-secoes7-9-onus-custodia-deposito | Arts. 39-43 | 253-305 | br1-tests-cap3-secoes7-9 | done |
| br1-cap3-sec10-resgate-e-reembolso | Arts. 44-45 | 306-331 | br1-tests-cap3-sec10 | done |
| br1-cap4-partes-beneficiarias | Arts. 46-51 | 332-371 | br1-tests-cap4 | done |
| br1-seat, br1-cases-seat | the seat layer (165 questions, 477 cases) | | | done |

## Decisions taken (with the provision that licenses each)

- Layer 1 style: constitutive BOOLEAN or value rules, each with `@ref` and quote lines; a "not covered" case is a `MAYBE` asserted `NOTHING`; a prohibition is a rule that is TRUE when the forbidden thing holds; deadlines are checks on dates through the core's `Prazo` rules; no regulative `PARTY ... MUST` and no `#TRACE` (the policy is stated in NOTES.md `## Seat`).
- Durations that are caps and not deadlines (Art. 37's 15 and 90 days) are numbers of days (fork F38).

## Files written

- PROGRESS.md (this file); NOTES.md
- br1-cap1-natureza, br1-cap2-capital, br1-cap3-secoes1-2-numero-e-preco, br1-cap3-sec3-especies-e-classes, br1-cap3-secoes4-5-forma-e-certificados, br1-cap3-sec6-propriedade-e-circulacao, br1-cap3-secoes7-9-onus-custodia-deposito, br1-cap3-sec10-resgate-e-reembolso, br1-cap4-partes-beneficiarias, each with its br1-tests-* file
