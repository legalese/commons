# PROGRESS.md -- ccc9 (Criminal Code, lines 5032-5568: ss 270 to 278.31)

Status 2026-11-16 (resumed): layer 1, tests, layer 2, NOTES.md and NEEDS-CORE.md are written; `check.sh` is green (14 modules, 0 errors, 1047 satisfied, the same on both stable builds). Re-read this file, NOTES.md and the text after any compaction, not a summary.

## What exists
- Layer 1: `ccc9-support.l4` (three-valued helpers), `ccc9-assault-officer.l4` (ss 270 to 270.1), `ccc9-sexual-assault.l4` (ss 271 to 275, 278), `ccc9-sexual-evidence.l4` (ss 276 to 277), `ccc9-records.l4` (ss 278.1 to 278.31).
- Tests: `ccc9-tests-assault-officer.l4` (84), `ccc9-tests-sexual-assault.l4` (243), `ccc9-tests-sexual-evidence.l4` (247, 49 traces), `ccc9-tests-records.l4` (307, 93 traces; the sexual-assault file has 6 traces, the assault-officer file 3): 881 assertions, 151 traces.
- Layer 2: `ccc9-seat.l4` (68 `@export` questions under five `§` headings in the text's order), `ccc9-cases-seat.l4` (166 cases).
- `NOTES.md` (assembled by `work/assemble_notes.py` from `work/notes/*.md`, `work/coverage.md` and the logs in `work/final/`), `NEEDS-CORE.md`.

## How the files are made (scratch, not deposited: `../../../work/` (that is `DEPOSIT/../work/`))
- `units.py` -> `units.json`: the 372 units of the range; every non-blank line of the 537 lines (526 non-blank) lies in one.
- `src/*.l4.t` templates -> `build.py` (expands `@@Q n-m | citation` into verbatim `-- src:` lines from `srcrefs.py quote` plus an `@ref`) -> the layer-1 file; `mk.sh <template>` builds, runs `srcrefs.py check --strict` and `runl4.py`.
- Generators: `mod3.py` and `mod4.py` (with `dutygen.py`, `lk.py`) write the templates of the sexual-evidence and records modules (the two parallel record families, the five publication bans, the judge's duties); `ccc9-assault-officer` and `ccc9-sexual-assault` are hand-written templates.
- Seat: `mkseat.py`, `seat2.py`, `seat3.py`, `seat4.py` (questions) run by `seatrun.py`; `casegen.py` writes the cases and refuses to finish while any question has none.
- Checks: `runl4.py` (compact counts), `check-traces.py` (every `#TRACE` result against its `-- TRACE-EXPECT:` comment, `L4=` selects the build), `coverage.py` (joins `-- COVERS[...]` markers, `forks.tsv`, units; 0 problems), `lint-kinds.py` (every `JUST FALSE`/`NOTHING` branch has a kind comment and every quoted fragment is in lines 5032-5568), `marginal.py` (table of every kind-commented branch), `sigs.py` (function signatures, used to write the seat calls).
- Final logs in `work/final/`: `check.log`, `traces.log`, `lint.log`, `srcrefs-refs.log`, `srcrefs-strict.log`, `warnings.log`.

## Decisions taken (with the text that licenses each; the full list is the fork register in NOTES.md)
- Brief governs over PLAN.md on imports: layer 1 imports `ccc-core` only and takes every section 2 answer as a `MAYBE BOOLEAN` input (PLAN.md section 4); the seat imports `ccc-definitions` and computes `s 2 peace officer`, `s 2 public officer`, `s 2 weapon` from plain facts.
- An offence's "who" clause is read like an "if": `JUST FALSE` when no limb holds, for that section only (F2).
- "may" functions with an "if" or described gate answer `NOTHING` (ruling of 2026-11-12; 22 functions, F6); duties with an "if" gate in the text answer `JUST FALSE` (F7); duties with no gate in the text answer `NOTHING` outside their scope (F26).
- A summary-conviction limb that states no penalty takes `s 787(1)` as an input (9 punishment functions); the seat passes a fixed placeholder it does not read.

## Corrections made while finishing (so a later reader does not undo them)
- Line citations in the seat's case comments were removed: they had been written from memory and were not checked; the cases name the section instead.
- The expected value of the `s 276.07(1)` case for a judge's order was wrong (my error): the order reaches only paragraph (c), the determination and reasons, so a judge's order leaves paragraph (a) prohibited; the case now says so.
- The seat question for `s 278.12(4)` took a list of enum values; it now takes eleven plus one yes/no inputs, one per assertion, so every seat input is a plain fact.

## Second seat audit and name-test sweep (resumed 2026-11-16, under the tightened files)
- Seat audit: 67 questions read against the bodies of the functions they call. An earlier pass (before the tightening) had retitled 11; under the tightened "What counts as a mismatch" 3 stand (direction 0, subject 3): `Under section 273.1(1.1), was there consent present at the time the sexual activity took place` (renamed), `Under section 273.3(1), is what I did prohibited` (renamed), and the `@export` of `Under section 274, is no corroboration required for a conviction` (second limb removed). 8 were put back to their original text (1 name, `Under section 273.3(2) ... for removing a young person from Canada`; 7 exports). 8 `-- RECONCILED 2026-11-12` comments in `ccc9-cases-seat.l4` (7 for the retitles, 1 for the put-back). Backups of the state before any second-pass edit: `work/final/ccc9-seat.l4.before`, `work/final/ccc9-cases-seat.l4.before`.
- Name-test sweep: 35 names read (30 functions, 5 rules); flipped 0; 22 already answer `NOTHING` under F6; 8 kept `JUST FALSE`; where/when/upon 0; entitled 0; "it is lawful": scoped 0, unscoped and retitled 0. F6's breakdown: 11 "if" powers, 2 described-scope powers, 5 eligibility tests, 4 permissions to appear. Written up in NOTES.md ("Name-test sweep of 2026-11-12").

## s 278.2(3), second limb (added 2026-11-16, at the team lead's request after the independent review of ccc7 to ccc12)
- Option (a): the sentence's second limb, "but, in doing so, the prosecutor shall not disclose its contents", is its own bar. Function `s 278.2(3) the prosecutor shall not disclose the contents of the record in notifying the accused` (`JUST TRUE` when the record is in the prosecutor's possession or control, is not produced under (2) and the notice discloses the contents; `NOTHING` otherwise, with a `NOTHING-kind (limited by its own wording)` comment), and rule `s 278.2(3) the prosecutor's prohibition on disclosing the contents of the record in notifying the accused` (`SHANT`, act `s 278.2(3) disclose the contents of the record in notifying the accused`), written like `s 278.16(6)`.
- Four assertions and three traces for it in `ccc9-tests-records.l4`; one seat question (the 68th, read against the body of its function: no mismatch) and three cases; the coverage row of `s 278.2(3)` lists all four names (it stays under fork F26, whose text now names the second function and the other readings); the jural-table row names both rules.
- The existing duty function, its rule and act, and the seat question for the first limb are unchanged.

## Not done
- No independent test pass (no subagent). No comparison with any other encoding (none was opened).
- The sections 278.32 onwards (ccc10) and the definitions of section 2 are not encoded here.
