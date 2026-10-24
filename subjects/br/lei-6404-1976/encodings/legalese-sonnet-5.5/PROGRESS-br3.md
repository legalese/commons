# PROGRESS: piece br3 (Arts. 106 to 137)

Last updated: 2026-10-22, at the end of the work.
State: finished and handed over; nothing is in progress.

## Where the source of truth is now

The scratch directory `work/` (templates `src/*.l4t`, the expander, the seat generator, the coverage and notes scripts) was deleted before the final report.
The `.l4` files in this folder are therefore the only source: edit them directly.
The seat files `br3-seat.l4` and `br3-cases-seat.l4` were generated and are now plain hand-edited files; the 191 questions and their 553 cases are listed in `## Seat` of NOTES.md.

## Modules (layer 1; each has a tests file `br3-tests-<same suffix>.l4`)

| module (file stem) | articles | assertions satisfied |
| --- | --- | --- |
| `br3-nomes` | the enumerations of the range (types only) | 0 (no rules) |
| `br3-cap10-sec1-capital` | 106-108 | 67 |
| `br3-cap10-sec2-direitos-essenciais` | 109 | 15 |
| `br3-cap10-sec3-voto` | 110, 111-115 | 95 |
| `br3-cap10-sec3-voto-plural` | 110-A | 78 |
| `br3-cap10-sec4-controlador` | 116, 116-A, 117 | 53 |
| `br3-cap10-sec5-acordo` | 118 | 37 |
| `br3-cap10-sec6-7-exterior-suspensao` | 119, 120 | 10 |
| `br3-cap11-sec1-competencia-convocacao` | 121-124 | 111 |
| `br3-cap11-sec1-instalacao-deliberacao` | 125-131 | 90 |
| `br3-cap11-sec2-ago` | 132-134 | 69 |
| `br3-cap11-sec3-age-quorum` | 135, 136, 136-A (and two routing rules for the quorum) | 102 |
| `br3-cap11-sec3-retirada` | 137 (and two routing rules for the right to withdraw) | 81 |
| `br3-seat` / `br3-cases-seat` | layer 2: 191 questions | 553 |

Total: 808 assertions in the twelve test files and 553 in the seat cases, 1,361 satisfied, 0 failed, 0 refused, 0 errors (the whole `check.sh` output is in NOTES.md, `## What check.sh prints`).
Coverage: 164 rows for 142 provision-start lines (three of those lie inside struck spans and have no row); 129 `encoded`, 31 `fork`, 3 `repealed or blank in this text`, 1 `inert`.

## Decisions taken (details in the fork register of NOTES.md)

- Rules are constitutive (BOOLEAN, NUMBER, DATE, MAYBE) unless the text names a party, an act and a consequence; few regulative rules, traced by hand.
- Where the text is silent between two readings, the rule returns MAYBE and NOTHING between them rather than picking one (F-br3-1, -2, -3, -9, -13, -21, -24, and others); where it simply does not say, the answer is NOTHING.
- A rule with many same-typed inputs takes a record of facts, built by name (`WITH`) so a swap cannot happen silently; short rules with distinct input names take them positionally.
- Counting convention: the core's (event day is day 0; the last day is inside the period); "mais de" and "há menos de" are strict.
- A percentage of the capital is counted in shares (F-br3-20); a quorum stated in votes counts the plural vote (Art. 110-A, § 9º).
- Every top-level name ends with a citation `(art. N, ...)`; seat question rules start with a capital letter and carry no citation.

## What is still open (none of it blocks anything)

- The fork readings are the author's own and have not been ruled by anyone (F-br3-1 to F-br3-30).
- Nothing was compared with the official text, and no lawyer has read the rules or the seat questions.
- The 17 cross-references into other pieces' ranges are taken as inputs where a value is needed (and as nothing where the right is only named); when the other pieces land, a merge pass should look at replacing them with calls where the names line up (`## Cross-references out of my ranges`).
- Two additions to the core would help and neither was asked for (`## Needs from the core`).
