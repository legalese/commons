# PROGRESS (keel, Rules of Court 2021)

Written as I go so a compaction loses nothing.
After a compaction, re-read this file, `NOTES.md` and the text, not any summary.

## State at the end of the run (2026-11-05)

All six steps of the brief are done; nothing further is owed by the keel.

## Files (all under the deposit dir `encodings/legalese-sonnet-5.5/`)

- `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`: given, not edited.
- `roc-core.l4` (196 lines, `DECLARE` only), `roc-definitions.l4` (generated from templates in the keel's scratchpad by a script that quotes the text mechanically), `roc-definitions-tests.l4` (278 assertions).
- `PLAN.md`, `NOTES.md`, `RULE-INDEX.md`, `PROGRESS.md` (this file).

## Done

- Read the brief, both skills (SKILL.md of each), dialects.md, source-locators.md.
- Read: O 1 whole, O 3 whole, O 4 r 1-2, O 6, O 7, O 20, O 25 r 1-5, the First to Fourth Schedule beginnings, the first lines of the Table of Derivations.
- Part split is on whole-Order boundaries (see `PLAN.md` section 6).
- CORRECTION (rule 8): the first count of cross-Order citations (17 lines) was WRONG: the text writes `Order`, a NO-BREAK SPACE (U+00A0), then the number (330 times; 20 with a plain space). The mechanical list is `PLAN.md`'s Appendix.
- CORRECTION found by re-reading before finishing: Orders cited whole in `o 1 r 2(7)` ("Order 29A", "Order 55") and in the `o 1 r 2(11)` Table ("Order 28") matched only an empty rule number; fixed, six assertions added, positive control run (the old matching fails exactly those six).
- CORRECTIONS to `PLAN.md` before finishing: statements about what other Orders define or say that had been written from memory (O 21 r 1, O 22 r 1, O 28 r 1, the Fourth Schedule's citations, "O 15 r 22 and r 23") were removed or replaced by headings read from `RULE-INDEX.md`, by the Appendix, or by text the keel read; the 5.33% sites, the O 28 r 10 to 12 and O 25 r 2 statements, the First Schedule paragraphs and the O 59 r 11 / O 62 r 10 wording were each checked against the text file.
- Checks, last run (after the period change below): `check.sh` 3 modules, 0 errors, 289 assertions satisfied, 0 failed, 0 refused, the same on 1.6.109 and 1.6.108; `srcrefs.py check --refs` and `--strict` 0 problems.

- Period change (ruling (a) of 2026-11-05: a period the text fixes in its own words gives JUST FALSE outside it): `o 1 r 2(4)(a) the notice of appeal is filed and served within one month`, `o 1 r 2(4)(b) the notice of appeal is filed and served within the period after permission` and `o 1 r 2(4)(c) the application for permission to appeal is filed and served in time with its documents` now answer JUST FALSE outside the period (they answered NOTHING). Signatures unchanged; 11 assertions changed to JUST FALSE and 9 added at the boundaries (278 to 289). `o 1 r 2(3)(a)`, `(b)` and the date limb of `(10)` are scope limits and stay NOTHING (fork K17). Fork K10 and the marginal-readings table are rewritten.

## Decisions taken (with the section that licenses each)

- Core: one `Decision maker` enum with five constructors so that O 1 r 3(1) "Court" and "Judge" can be encoded over a `Sitting`.
- Main idioms verified by probe on 1.6.109 and 1.6.108: constructor pattern binding is positional with NO `WITH`; list membership is `elem x xs`; the prelude exports `count`, `any`, `all`, `elem`; `Magistrate's Court` works as a constructor; `#CHECK` on an overloaded name is an error.
- Time seam: each part states its period as a core `Period` and takes `o 3 r 3 the last day for doing the act` as a DATE input (O 3 r 3 read: it counts both after and before a date).
- O 1 r 2(1) revocation = inert reason 2 (fork K8); O 1 r 1 encoded as the constant used by r 2; r 2(2) to (13) encoded because the First Schedule still governs live pre-2022 proceedings.
- Distribution (2026-11-05): both `roc-core.l4` and `roc-definitions.l4` go to every part; the tests module does not. An earlier draft of `PLAN.md` assumed only the core was distributed and listed the Order 1 definitions as seams; that is replaced by `PLAN.md` section 4A (exact names and arguments) and 6.1 (per part). `roc-definitions.l4` was checked standalone (imports only `prelude`, `daydate`, `roc-core`).
- Unstable dialect: looked, found no shape, no second encoding (one line in `NOTES.md`).

## Next

Nothing for the keel. The lead merges `NOTES.md` rows, hoists `NEEDS-CORE.md` entries and wires the seams.
