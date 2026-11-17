# PROGRESS.md -- part ccc18 (Criminal Code, lines 10275-10956: sections 490.02 to 492.2)

Status header: written 2026-11-16 by part agent `ccc18` at the end of the resumed run; every number below was printed by a command run in that session (`check.sh` log `work/check-final.out`, trace comparison `work/trace-summary.txt`).
The first pass ended on 2026-11-13 at the weekly limit with NOTES.md, NEEDS-CORE.md and this file not yet written; they are written now.

## State: finished

| item | state |
| --- | --- |
| `ccc18-soira-notice` + `ccc18-tests-soira-notice` | done: 190 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-soira-foreign` + `ccc18-tests-soira-foreign` | done: 174 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-soira-itoa` + `ccc18-tests-soira-itoa` | done: 119 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-soira-offences` + `ccc18-tests-soira-offences` | done: 69 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-soira-additional` + `ccc18-tests-soira-additional` | done: 87 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-forfeiture` + `ccc18-tests-forfeiture` | done: 198 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-weapons-evidence` + `ccc18-tests-weapons-evidence` | done: 120 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-tracking` + `ccc18-tests-tracking` | done: 119 assertions, run clean on 1.6.110 and 1.6.109 |
| `ccc18-seat`, `ccc18-cases-seat` | done: 58 questions under 8 `§` headings, 171 assertions (8 restated by the second audit pass) |
| NOTES.md | done: coverage (497 rows), fork register (F1-F19), name-test sweep, jural relations, marginal readings (189 functions), seams, findings, binary traps, check.sh output; each heading appears once (asserted by the generator) |
| NEEDS-CORE.md | done: 8 one-constructor bearer types (fork F1) |

## The resumed pass (2026-11-16)

1. Baseline `check.sh` on both builds before any edit: `TOTAL (21 modules) 0 1247 0 0 | 0 1247 0 0`.
2. The generators were regenerated into the deposit and compared with it byte for byte (all 18 `ccc18-*.l4` files identical) before any change, so no earlier hand fix was lost.
3. Seat audit (second pass): 58 questions read against the bodies of the functions; 3 retitled (13, 54, 58), 55 read and left; 8 assertions restated in place with `-- RECONCILED 2026-11-12`.
4. Name-test sweep: 91 functions matched; 0 flipped; 16 kept JUST FALSE; 10 listed with a where/when/upon-kind gate (6 alone, 4 mixed); 0 "entitled"; "it is lawful" 0 scoped and 0 unscoped.
   `s 490.026(4)` and `s 490.02912(3.1)` (gate "once") changed from NOTHING to JUST FALSE with `[may-where]`; these are the only answer changes of the pass and they rest on reading "once" as "when", which is this part's own extension of the instruction's list of equivalents, so the lead can overrule them; their two assertions are restated in place.
5. Final `check.sh`: `TOTAL (21 modules) 0 1247 0 0 | 0 1247 0 0`.
6. Traces: 1163 evaluations on each build (1076 assertions and 87 trace outcomes), identical, JL4_LIBRARY_PATH unset on both sides.
7. `srcrefs.py check --refs` and `--strict` over all `ccc18-*.l4`: 0 problems; `work/lint.py`: 8 modules, 146 FALSE-kind answers, 175 NOTHING-kind answers, 66 marginal-(a) tags, 0 problems.

## How the files are made (read this first after a compaction)

- Work area `../work/` (not shipped): `gen.py` (quote and `@ref` generator reading the raw text), `fam.py` (helpers: `cond_duty`, `satisfied_duty`, `factors`, `appeal_may`, `appeal_powers`, `gate`), `mod_*.py` (one spec per layer-1 module: L4 text and tests as Python strings), `b.sh <mod>` (regenerate a module and its tests and run both), `bs.sh` (the seat), `mod_seat.py` and `seat_q1..q4.py` (the seat questions; `RENAMED` carries the second audit pass's retitles and writes the RECONCILED comments), `units.py` (the 497 coverage rows), `sweep.py` (the name-test classification, cross-checked against the code), `lint.py`, `trace_cmp.py`, `mknotes.py` (NOTES.md, NEEDS-CORE.md, this file).
- Regenerate everything: `python3 mod_X.py`-style via `b.sh mod_notice` etc., `bs.sh`, then `python3 mknotes.py` after a `check.sh` run (it reads `check-final.out`, `check-baseline-1116.out`, `trace-summary.txt`).
- Quote lines are never typed: `gen.Module.unit(label, ranges, code...)` reads them from the raw text.

## Decisions taken (with the text that licenses each)

See the Fork register in NOTES.md (F1-F19) and the Marginal readings section; the three that matter most for a reviewer:
- A "may"-named function whose "if" gate fails answers NOTHING (brief, ruling of 2026-11-12 (1)); fork F5, 59 functions.
- A "may" function whose gate is of the where/when/upon kind answers JUST FALSE and is listed, not decided (ruling (b); the lead's instruction of 2026-11-12); fork F18, 10 functions.
- A failed "if" on a duty or a flat statement counts as the text's no (marginal reading (a)), tagged `[marginal (a)]`; a judgment of a court is a BOOLEAN input; one local single-constructor `party` type per regulative rule whose bearer the core lacks (NEEDS-CORE.md).
