# PROGRESS (pass 2: completion to "whole"; Sonnet 5.5, single encoder)

The disk is my memory. After any compaction re-read this file, NOTES.md, BRIEF.md (the pass-2 brief is at <RUN>/BRIEF.md; pass 1's is BRIEF-pass1.md) and the statute text (`../../registers/source-bundle/RSBC-1996-c.-238.txt`, also INPUTS_DIR/RSBC-1996-c.-238.txt), not a summary.

Paths: RUN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-bc ; INPUTS_DIR = RUN/inputs ; DEPOSIT = RUN/deposit ; row dir = DEPOSIT/encodings/legalese-sonnet-5.5
L4_BIN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528 (sha256 0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d; `--version`: unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28))
Run: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`. Probes and the scripts that built NOTES.md and encoding.json lived in a scratch directory that was deleted at the end. No git. Write only under DEPOSIT.

## Baseline (step 1), run before any change, with the pass-2 binary

```
module                                    errors satisfied  failed  refused  expected
bc-interpretation-definitions.l4               0         0       0        0         0
bc-interpretation-repeal.l4                    0         0       0        0         0
bc-interpretation-time.l4                      0         0       0        0         0
bc-tests-alt-readings-expected-fail.l4        16         0      16        0        16
bc-tests-definitions.l4                        0        73       0        0         0
bc-tests-repeal.l4                             0        26       0        0         0
bc-tests-time-commencement.l4                  0        45       0        0         0
bc-tests-time-holidays.l4                      0        81       0        0         0
bc-tests-time-periods.l4                       0       118       0        0         0
bc-tests-time-words.l4                         0        33       0        0         0
TOTAL (10 modules)                            16       376      16        0
```
Same numbers as pass 1 recorded with its own binary (376 satisfied, 16 failed by design, 0 refused).
At the end every one of these must still hold, plus additions.

## Status (2026-10-29, end of pass 2 work)

- [x] read brief, skills, guide, pass-1 NOTES and modules
- [x] baseline (above); still holds in the final run (376 satisfied, 16 failed by design, 0 refused)
- [x] count and audit (units.py, coverage.py audit; the audit section of NOTES.md)
- [x] new modules: terms, reading, powers, commencement, periods, replacement (+ tests, + bc-tests-alt-readings-2-expected-fail.l4 = 5 failures in check.sh)
- [x] coverage-dispositions.tsv (416 units, no catch-all) and jural.tsv (whole text); both checked by coverage.py
- [x] NOTES.md complete (assembled by a scratch script that was deleted at the end; the file is the deliverable, the script is not)
- [x] encoding.json 0.2.0, check.sh updated, SOURCE-LICENSE.md points at ../../SOURCE-LICENSE.md
- [x] srcrefs --strict: 0 problems on every module (572 src lines, 357 runs, 401 locators)
- [x] advisor reviews: two before this line, the second one's items applied (pass-1 FALSE defaults changed to named refusals, jural duplicates removed, s 2(3) and s 41(1)(a) refuse, fork cross-check, s 25.x rows attached to forks)
- [x] final check.sh: 25 modules, 1439 satisfied, 21 failed (16 + 5, all by design), 0 refused (after the fix round below; 1428 before it)
- [x] scratch directory and __pycache__ deleted; final report written (it is the last message, not a file)
- [x] fix round after the independent test pass (lead's list, six items): s 18(1), 18(2)(c), 18(2)(d) and s 38 refuse instead of FALSE; the quorum of s 18(2) is a whole number and the raw threshold is a second function; the refusal of the catalogue's membership rule is chosen by the verb; fork F-limit-or-scope states the rule that separates s 41(1)(e) from (f); forks registered or extended: F-clear (month and year cases), F-clear-ends, F-government, F-saturday, F-affidavit, F-deemed-service, F-established, F-means-and-includes, F-limit-or-scope; known limits and the restored structure of the three displaced entries in NOTES.md
- [x] scratch of the fix round (a `_probe` directory) deleted again at the end

## Plan (decided before writing any new L4)
New modules (layer 1), all `@lang en`, unstable dialect, each IMPORTs what it reuses:
- bc-interpretation-terms.l4: the catalogue of defined terms (s 1, 8.1(1), 29, 29.1(1), 29.2, 32(1)), generated from the text; membership rule ("includes" is open, "means" is closed); a few computable definitions; the Schedule as data.
- bc-interpretation-reading.l4: rules of reading and form (ss 2(2),(3), 6, 7, 8, 8.1(2),(3), 9, 10, 11(1),(2), 12, 13, 15, 28(2)-(4), 30, 31, 33(2)-(6), 39, 40, 43, 44).
- bc-interpretation-powers.l4: capacities, offices, powers (ss 17, 19, 21, 22, 23, 27, 41).
- bc-interpretation-commencement.l4: ss 3(4), 5(2), 16(1),(3), 20(1),(2),(5).
- bc-interpretation-periods.l4: s 25(1),(2).
- bc-interpretation-replacement.l4: ss 34, 36(1)(b),(c), 37.
Tests: bc-tests-<same topic>.l4, plus bc-tests-alt-readings-2-expected-fail.l4 (new rivals; the pass-1 file stays at 16).
Decisions are recorded in NOTES.md (fork register, findings) as they are taken.

## How the pieces are reproduced
- `python3 -I units.py ../../registers/source-bundle/RSBC-1996-c.-238.txt` counts the 416 units.
- `python3 -I coverage.py <raw> audit | check | table | jural` : the audit against pass 1's table; the gap detector (every unit has a disposition, every encoded or fork unit's line is cited by an `@ref`); the coverage table of NOTES.md; the Hohfeld table of NOTES.md. Inputs: `coverage-dispositions.tsv`, `jural.tsv`, `terms-data.py`.
- `python3 -I gen-terms.py <raw>` rewrites the generated blocks of `bc-interpretation-terms.l4` and `bc-tests-terms.l4` from `terms-data.py`.
- `python3 -I srcrefs.py check --strict <raw> bc-interpretation-*.l4` checks every quotation and locator.
- `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` runs everything.
The other new modules were written from templates with quote markers that a scratch script expanded into `-- src:N | text` lines; that scratch was deleted, and the modules are plain files.

## Files written or changed in pass 2
New modules: bc-interpretation-terms.l4, -reading.l4, -powers.l4, -commencement.l4, -periods.l4, -replacement.l4.
New tests: bc-tests-terms.l4 (generated), bc-tests-terms-rules.l4, bc-tests-reading.l4, bc-tests-powers.l4, bc-tests-commencement.l4, bc-tests-periods.l4 (19 assertions after the fix round), bc-tests-replacement.l4, bc-tests-definitions-refusals.l4, bc-tests-alt-readings-2-expected-fail.l4.
New tools and data: units.py, coverage.py, coverage-dispositions.tsv, jural.tsv, gen-terms.py, terms-data.py, NOTES-pass1.md (pass 1's NOTES, frozen).
Changed: NOTES.md, PROGRESS.md, encoding.json (0.2.0), check.sh (one expected_failed row), SOURCE-LICENSE.md.
Changed to fix a defect against the text (logged in NOTES.md under "Changes to existing modules"): bc-interpretation-definitions.l4 (s 24 twice, s 28(1), then s 18(1), s 18(2)(c), s 18(2)(d), s 38, and the quorum of s 18(2) made a whole number), bc-interpretation-repeal.l4 (s 4(4)), bc-tests-definitions.l4 (thirteen assertions turned into refusals, one expected value changed, nine added: 82 assertions), bc-tests-repeal.l4 (one assertion); the functions now refuse by name where they used to answer FALSE with the text silent.
Also changed in the fix round (pass-2 files): bc-interpretation-terms.l4, gen-terms.py, bc-tests-terms.l4 (regenerated), bc-tests-terms-rules.l4, bc-tests-periods.l4, coverage.py, coverage-dispositions.tsv, encoding.json, NOTES.md.
Unchanged: bc-interpretation-time.l4, the four bc-tests-time-*.l4, bc-tests-alt-readings-expected-fail.l4 (still 16 failures), srcrefs.py, BRIEF-pass1.md.
