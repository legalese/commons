# PROGRESS (the encoder's memory across compactions): pass 2, the completion to "whole"

Row `legalese-sonnet-5.5`, subject `us/ca` interpretation cluster, file prefix `usca`.
After a compaction re-read, in this order: this file, `BRIEF.md` (kept at `../../../BRIEF.md` in the run directory, not in the deposit), `NOTES.md` (section `## Re-disposition audit`), the six statute `.txt` files in INPUTS_DIR.

## Fixed facts

- Target: `unstable`. Run `L4_TARGET=unstable L4=<L4_BIN> ./check.sh`.
- L4_BIN = `.../scratchpad/bin/l4-unstable-0528`, `l4 --version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`. `JL4_LIBRARY_PATH` UNSET.
- The `.txt` files are converter-made renderings, not the official text; nothing is checked against the official text.
- Do not git add, commit or push. Write only under DEPOSIT.

## Baseline (measured 2026-10-29 before any change, with the binary above)

```
module                                    errors satisfied  failed  refused  expected
test-usca-general.l4                           0        98       0        0         0
test-usca-holidays.l4                          0       627       0        0         0
test-usca-operation.l4                         0       123       0        0         0
test-usca-rules.l4                             0       334       0        0         0
test-usca-time.l4                              0       425       0        0         0
test-usca-worked.l4                            0        89       0        0         0
tests-red.l4                                   8         0       8        0         8
usca-general-provisions.l4                     0         0       0        0         0
usca-holidays.l4                               0         0       0        0         0
usca-interpretation-time.l4                    0         0       0        0         0
usca-operation-of-statutes.l4                  0         0       0        0         0
TOTAL (11 modules)                             8      1696       8        0
```

srcrefs.py check --refs, baseline (src: lines, runs, locators, problems): `usca-general-provisions.l4` 82/14/31/0; `usca-holidays.l4` 69/13/39/0; `usca-interpretation-time.l4` 67/18/76/0; `usca-operation-of-statutes.l4` 40/23/43/0.
Pass-1 coverage: 159 section rows (82 encoded, 29 inert, 48 not applicable), 7 absent numbers.

## Status

Pass 2 finished on 2026-10-29 (the completion to "whole"); nothing below is open. The repair after the independent test pass follows this section.

- Seven new modules, each with its test file: `usca-canons-of-reading.l4`, `usca-definitions.l4`, `usca-remedies-and-actions.l4`, `usca-proclaimed-days.l4`, `usca-deputies.l4`, `usca-assessed-value.l4`, `usca-further-limbs.l4`.
- `check.sh` (target unstable): 25 modules, 2,261 satisfied, 8 failed (all expected, `tests-red.l4`), 0 refused, exit 0. The eleven pass-1 files give their baseline numbers.
- `srcrefs.py check --refs`: 0 problems in each of the eleven modules.
- Coverage: 406 units, every one with one disposition (327 encoded, 58 fork, 14 inert, 7 repealed or blank); regenerate with `python3 -I coverage.py table`.
- No pass-1 module or test was edited.
- `NOTES.md` was rebuilt from the generated coverage table and the hand-written sections; `encoding.json` is version 0.2.0.
- Not done: the independent test pass, a mutation check of the seven new modules, any run against `main`, any review by a domain expert.

## Repair after the independent test pass (2026-10-29, version 0.2.1)

Done on the lead's fix list; the details are in `NOTES.md` ("Changes to existing modules", "Findings" 21-24, "Reading a result", the fork register's last subsection).

- A: `the statute that prevails when two statutes of one session amend the same section` (pass-1 module `usca-operation-of-statutes.l4`) now applies Gov. Code § 9605(b)(2) alone when the order of enactment is equal; `test-usca-operation.l4` (pass 1) has one flipped expected value and 11 more assertions.
- B: 53 of the 76 gaps are answered by `usca-further-asks.l4` and `test-usca-further-asks.l4` (181 assertions), plus two heading cases in `usca-canons-of-reading.l4`; 23 are left, each with its reason.
- C: a loud variant for the Section 135 days (four functions taking a `MAYBE`); the silent failure of every left-out list is stated in "Reading a result".
- D and E: eight fork entries added, F-9605b rewritten, the test author's Z1-Z19 cross-referenced; the "Reading a result" paragraph written.
- `check.sh` (target unstable): 27 modules, 2,455 satisfied, 8 failed (all expected, `tests-red.l4`), 0 refused, exit 0.
- `srcrefs.py check --refs`: 0 problems in each of the twelve modules; `--strict`: 41 (23 + 13 + 5, all in three pass-1 modules, unchanged), 0 in the other nine.
- Coverage: 406 units, 330 encoded, 55 fork, 14 inert, 7 repealed or blank (three rows moved from fork to encoded: Gov. Code § 6701(c)(1), (2), (3)).
- Not done: a second independent test pass on this version, a mutation check of the eight modules added since pass 1, any run against `main`, any review by a domain expert.
- Peeked: the test author's own files in the row's review folder (`review/ANSWERS.md`, `review/enc/tests-independent.l4`), to get the list of the 76 gaps and the reconciled assertions; and a scratch run of `tests-independent.l4` against a copy of this deposit.
  Nothing from the forbidden list was opened.

## Pass 1 PROGRESS (kept, from the copy this run started with)

# PROGRESS (the encoder's memory across compactions)

Row `legalese-sonnet-5.5`, subject `us/ca` interpretation cluster, file prefix `usca`.
Re-read after a compaction: this file, `NOTES.md`, the six statute `.txt` files in INPUTS_DIR, and `BRIEF.md`.

## Fixed facts

- Target: `unstable` (the brief requires `REFUSE` and `@lang en`, which `main` rejects). Run `L4_TARGET=unstable L4=<L4_BIN> ./check.sh`; the default target of this copy of `check.sh` is `unstable`.
- L4_BIN `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`, `l4 --version` prints `dev`.
- `JL4_LIBRARY_PATH` stays UNSET.
- The `.txt` files are a converter-made rendering, not the official text; nothing here was checked against the official text.

## Status

- [x] Coverage plan: 159 sections, every one has a row in the coverage table of `NOTES.md`.
- [x] `usca-interpretation-time.l4` (prelude + daydate only), `usca-holidays.l4`, `usca-operation-of-statutes.l4`, `usca-general-provisions.l4`: all compile with no diagnostics; `srcrefs.py check --refs` (the encoding skill's tool, /Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/srcrefs.py) reports 0 problems on each.
- [x] Tests: `test-usca-time.l4`, `test-usca-rules.l4`, `test-usca-holidays.l4`, `test-usca-operation.l4`, `test-usca-general.l4`, `test-usca-worked.l4`: all assertions satisfied (counts in the check output in `NOTES.md`).
- [x] `tests-red.l4`: 8 assertions meant to fail; counted in `check.sh` (`expected_failed`) and `encoding.json` (`expected_red`).
- [x] Answer table: 63 evaluations of the worked cases, 0 differences from the values written down before the first run.
- [x] `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`, `NOTES.md`.
- [x] Mutation check of the four modules (scratch script, not shipped): 366 mutants, 357 killed, 9 survivors, all read as equivalent; result in `NOTES.md`.
- [x] Final `check.sh` (2026-10-22, target `unstable`, exit 0): 11 modules, 8 errors, 1696 assertions satisfied, 8 failed (all in `tests-red.l4`, expected 8), 0 refused. Verbatim in `NOTES.md`.
- [ ] Not run: the skill's independent test pass (step 8; the brief allowed no subagents) and any run against `main`.

## Peeked

Nothing opened from the forbidden list.
Names of files and directories only, none opened: one `ls` of the scratchpad root early in the task, and one `ls` of the scratchpad root and of `interp-wave/` near the end (these listed other rows' directory names and loose files such as `BRIEF.template.md`, none of which was read).
Writes outside the row: a stray directory `scratchpad/us-ca-probe`, made outside DEPOSIT by mistake and removed with `rmdir`; a copy `scratchpad/ops-before.l4`, made outside DEPOSIT for a diff and removed; a stray output file `deposit/check-run-1.txt` in the DEPOSIT root, removed.
