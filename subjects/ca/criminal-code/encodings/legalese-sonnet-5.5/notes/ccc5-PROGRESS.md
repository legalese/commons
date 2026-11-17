# PROGRESS (ccc5) -- lines 2382-2989: Part III from s 110.4 to s 117.15, and Part IV (ss 118-149)

Final state, 2026-11-16. Re-read this file, NOTES.md and the text after any compaction, not a summary of them.

## How the work is built

- The authoring sources are in `../../../work/` (not shipped): `units.py` (the 408 coverage units, mechanical), `lib.py` (the rule generator), `proc.py` (shared procedural builders), `m_*.py` (one specification per module), `scen.py` and `scenarios.py` (hand-written cases), `build.py` / `rebuild.sh` (write every `.l4` and run it), `coverage.py` (every unit has a function), `notes.py` (writes NOTES.md), `seatlist.py` (every seat question and the function it calls).
- To regenerate everything: `work/rebuild.sh`, then `check.sh`, then (after `work/check-final.log` is current) `work/notes.py`. Always rebuild all seven modules together: the seat file is written from the modules passed to `build.py`.
- Quote lines come from `srcrefs.py quote`, never typed.

## Status (all done)

- [x] orientation, probes (regulative rules, both keel imports together, `DATE MINUS n`, BRANCH, unused GIVEN, `@export` with no GIVEN)
- [x] 408 units (units.py): every non-blank line of 2382-2989 in exactly one unit; coverage.py finds every unit covered by a function except the three inert ones
- [x] module `ccc5-s110-4-to-117` (ss 110.4-117), `ccc5-s117-01-to-117-012`, `ccc5-s117-02-to-117-06`, `ccc5-s117-07-to-117-15`, `ccc5-s118-to-130-1`, `ccc5-s131-to-143`, `ccc5-s144-to-149`, each with `ccc5-tests-<same>.l4`
- [x] `ccc5-seat.l4` (268 exported questions, all "Under section N,") and `ccc5-cases-seat.l4` (generated cases for every question, and 11 hand-written persons)
- [x] NOTES.md: coverage (408 rows), fork register (91 rows), jural relations (64 rows), marginal readings, FALSE and NOTHING, seams, findings, binary notes, check.sh output, seat question list, direction sweep
- [x] NEEDS-CORE.md (three optional constructors)
- [x] `srcrefs.py check`, `--refs`, `--strict` over every `ccc5-*.l4`: 603 src lines, 350 runs, 361 locators, 0 problems at each level
- [x] `check.sh` (target main, 1.6.110 against 1.6.109): 19 modules, 0 errors, 2260 assertions satisfied, 0 failed, 0 refused, the same on both builds (re-run 2026-11-16 after the sweep edits; the traces of both builds were compared by hand on the 2026-11-13 files and not compared again)
- [x] second seat-question audit pass (2026-11-12, tightened test): 268 questions read against the function bodies, 4 retitled (`s 117.05(1)`, `s 117.14(1)`, `s 127(1)`, `s 131(3)`), 0 put back; each earlier assertion restated in place with `-- RECONCILED 2026-11-12: was ...` (NOTES.md, "Second seat-question audit pass of 2026-11-12")
- [x] name-test sweep (2026-11-12): 12 answer NOTHING on a failed "if" gate (all built so; the sweep flipped none), 3 kept JUST FALSE (gate closed by the text), 20 listed with a where/when/upon-kind gate, 0 "entitled"; "it is lawful": 0 scoped, 0 unscoped retitled (NOTES.md, "Name-test sweep of 2026-11-12")

## Decisions taken (with the text that licenses each)

- Offence limb: all elements -> JUST TRUE, exceptions first -> JUST FALSE, otherwise NOTHING (the 2026-10-29 rule; FALSE and NOTHING in NOTES.md).
- "May" powers: NOTHING when an "if" gate fails (ruling of 2026-11-12); JUST FALSE when the gate is "where" (ruling (b) of 2026-11-05), listed in the fork register and in the name-test sweep subsection, not flipped (20 such functions: ruling (b) of 2026-11-05 says JUST FALSE, the line on grants points to NOTHING, and the question is for the maintainer or a lawyer).
- Section 2 terms are MAYBE BOOLEAN inputs; `ccc-definitions.l4` is not imported (every `s 2` function there takes a capacity enum).
- Summary limbs take `s 787(1) the general penalty ...` as an input.
- Permissions with a time limit and a consequence for another party (ss 117.03(2), 117.05(1)) are `DO ... WITHIN n HENCE (...) LEST FULFILLED`: a lapsed `MAY` with a `HENCE` chain enters the HENCE obligation on 1.6.109 and 1.6.110 (NOTES.md, binary notes).

## Seat questions and the layer-1 function each returns

See NOTES.md, "Seat questions (ccc5)" (268 rows, written by `work/notes.py` from `ccc5-seat.l4`).
