# PROGRESS.md -- part agent ccc2 (Criminal Code, lines 850-1248: Part II, ss 46 to 83)

Written to disk as the work goes; re-read this, NOTES.md and the text after any compaction, not a summary.
State on 2026-11-16 (resumed after the weekly-limit stop): all deliverables are written; `check.sh` is green (TOTAL of 23 modules: 0 errors, 950 assertions satisfied, none failed or refused, every module `same` on both stable builds, before and after the two follow-up tasks); `srcrefs.py check` (plain, `--refs`, `--strict`) reports 0 problems each.
The two follow-up tasks of 2026-11-12 are done: the second seat-question audit pass (107 read, 8 retitled, 99 read and left; 18 assertions restated with `-- RECONCILED 2026-11-12`) and the name-test sweep (flipped 1, kept 0, listed `may` 1, listed `entitled` 0; `it is lawful` scoped 0, unscoped 0). Both are written up in NOTES.md (`## Seat questions`, `### Name-test sweep of 2026-11-12`).

## Method (so that a resumed session can continue)
- Sources of the modules are in `DEPOSIT/../work/src/*.l4.in`; `DEPOSIT/../work/expand.py` expands the macros `--QR a-b | cite` (quote lines copied from the raw text plus one @ref spanning them), `--R a-b | cite` (an @ref only) and `--Q` (quote only) into `DEPOSIT/encodings/legalese-sonnet-5.5/*.l4`. Edit the `.in` file, never the deposited `.l4`.
- `work/run1.sh <module-stem>...` expands, runs with the stable binary (1.6.110) and prints errors, warnings, assertions satisfied and failed.
- `work/rows.py` builds the coverage rows (lines 850-1248) from the text and asserts that every non-blank line is in exactly one row.
- `work/gen_seat.py` (with `work/gen_q1.py` to `gen_q4.py`) writes `ccc2-seat.l4` and `ccc2-cases-seat.l4`; constructor names are read from the modules, expected values are written by hand in the `gen_q*.py` files. The `RETITLE` table in `gen_seat.py` (key: new title; value: old title and reason) is what makes the generator restate every assertion of a retitled question with a `RECONCILED` comment; it also writes `work/retitled.json` for NOTES.md.
- `work/notes_data.py` (provision to encoding names, forks, jural kind) and `work/notes_gen.py` write `NOTES.md`; the generator asserts that every name it cites exists in a module, and computes the tag counts, the marginal-reading tables, the seams and the srcrefs lines from the files. Re-run `python3 -I notes_gen.py` after any change to a module.
- Binary: 1.6.110 (main, e51181d, 2026-11-11); second stable build 1.6.109 (main, 4c887e0, 2026-11-04) for `check.sh`.

## Decisions taken (assumed, not ruled; each has a fork or marginal-reading line in NOTES.md)
- Offence-creating clauses: an unmet element answers NOTHING (F1). JUST FALSE only where the text says no: "means"/"is" definitions, "unless" once met, flat negatives, periods fixed in the text's own words, "where"/"when" gates by ruling.
- Summary limbs: the penalty is s 787(1)'s, a seam input `s 787(1) the general penalty for an offence punishable on summary conviction` (a `Punishment`) (F20).
- Layer 1 imports `ccc-core` only and takes each s 2 answer as a `MAYBE BOOLEAN` input (PLAN.md style); layer 2 imports `ccc-definitions` and calls the keel's functions. The brief says layer 1 imports `ccc-definitions`: this is a stated departure for the lead (NOTES.md, "Departures").
- Regulative rules (ss 50(1)(b), 67, 68(b), 70(1), 79) are run with `#TRACE`; the same duty is also a decision function, asserted.

## Modules (layer 1), tests (assertions satisfied, as `check.sh` prints them)
| module | sections | assertions |
| --- | --- | --- |
| ccc2-treason.l4 + ccc2-tests-treason.l4 | 46, 47, 48 | 76 |
| ccc2-prohibited-acts.l4 + ccc2-tests-prohibited-acts.l4 | 49 to 56 | 121 |
| ccc2-official-documents.l4 + ccc2-tests-official-documents.l4 | 56.1, 57, 58 | 88 |
| ccc2-sedition.l4 + ccc2-tests-sedition.l4 | 59 to 62 | 57 |
| ccc2-riots.l4 + ccc2-tests-riots.l4 | 63 to 69 | 93 |
| ccc2-drilling-entry.l4 + ccc2-tests-drilling-entry.l4 | 70 to 73 | 38 |
| ccc2-piracy-air-sea.l4 + ccc2-tests-piracy-air-sea.l4 | 74 to 78.1 | 105 |
| ccc2-explosives.l4 + ccc2-tests-explosives.l4 | 79 to 82.1 | 58 |
| ccc2-nuclear-prize-fights.l4 + ccc2-tests-nuclear-prize-fights.l4 | 82.2 to 83 | 77 |
| ccc2-seat.l4 + ccc2-cases-seat.l4 | the seat layer: 107 questions | 237 |
| NOTES.md, NEEDS-CORE.md | coverage (285 rows), forks, jural relations, marginal readings, seams, findings | |

## Findings (details in NOTES.md)
- `NOT a AND b` on one line parses as `NOT (a AND b)`: caught by three failing tests in `s 78.1(5) the thing is a ship`; every `NOT` followed by `AND` or `OR` is now `(NOT x)`.
- A regulative rule cannot be asserted (`#ASSERT ... AT 0 WITH ... EQUALS FULFILLED` is a parse error): the rules are run with `#TRACE`.
- `ROR`, `WAITUNTIL n` and `WITHIN 30` work on the stable build; the trace outputs are in NOTES.md.
- s 55 names "section 47 or sections 50 to 53" and not section 46; s 63(2) adds no case beyond s 63(1); s 78.1(4) names (2)(a), (b) and (c) only; s 80 states a penalty only if an explosion results.

## Left for the lead
- Whether layer 1 should import `ccc-definitions` and call the keel (the brief) rather than take `s 2` inputs (PLAN.md).
- `NEEDS-CORE.md`: seven `Party` constructors for the officials of s 67.
- The fork register entries for a lawyer: F8, F9, F11 (the "may" and "when" groups), F12, F14, F18.
