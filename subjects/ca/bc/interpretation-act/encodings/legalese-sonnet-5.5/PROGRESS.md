# PROGRESS (Sonnet 5.5, single encoder)

The disk is my memory. After any compaction re-read this file, NOTES.md, BRIEF.md and the statute text (INPUTS_DIR/RSBC-1996-c.-238.txt), not a summary.

Paths (scratchpad = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad):
- INPUTS_DIR = <scratchpad>/interp-wave/bc/inputs ; DEPOSIT = <scratchpad>/interp-wave/bc/deposit ; row dir = DEPOSIT/encodings/legalese-sonnet-5.5
- L4_BIN = /Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 (sha256 2d912dd2...07d7, verified)
- Target compiler: unstable (the brief mandates REFUSE; main rejects it). Run: `L4=<L4_BIN> ./check.sh` (check.sh defaults L4_TARGET to unstable in this row).

## Status: complete on disk; `_probe/` deleted. The final report is the run's last message.

- [x] read brief, skills, source, daydate
- [x] bc-interpretation-time.l4 (periods, holidays, spans, moments, commencement, regulations, proclamations, appointments, age, s 29 time words)
- [x] bc-interpretation-definitions.l4, bc-interpretation-repeal.l4
- [x] tests: periods 118, holidays 81, commencement 45, words 33, definitions 73, repeal 26 (376 satisfied), expected-fail 16 (failed by design)
- [x] check.sh (default target unstable; expected_failed 16 for the expected-fail file) run: 0 other errors, 0 refused
- [x] srcrefs.py check --strict clean on the three modules
- [x] NOTES.md: scope, coverage (57 rows), fork register, answer tables 3.1-3.3, check.sh output, open questions
- [x] encoding.json, SOURCE-LICENSE.md, BRIEF.md copy
- [x] `_probe/` deleted (it held the templates and generators; the .l4 modules and NOTES.md are the deliverables)

## Decisions taken (with the section that licenses each): see NOTES.md section 2
Counting: reference day excluded, last day inside (s 25.2(2)(a)). s 25(3) reaches days, weeks, months and years (it names ss 25.2-25.4), only for "a period for doing an act", and moves both ends. "Clear" periods are refused where the date of s 25.3(1) or 25.4(1) does not occur. Moment: beginning of the day (s 4(1)) in Pacific Time, UTC-7 all year (s 26). Regulation silent: exempt class -> day enacted (s 3(5)); other -> refusal. Passed/published is not assent (refusal). Mailed document: delivered on deposit; receipt refused.

## Changes made late, each tested
- A whole-number guard on every count: anything else is refused, since the text speaks of one or more whole units.
- Both ends of a period for doing an act now move off a holiday (fork F-near-end); rival reading is Rival 11.
- Named refusal for "passed or published" in place of a silent input.
- A regulation of either class that names a day: the day is passed through, registered in fork F-regulation-silent and in open question 7 (the advisor pointed out that the stated-day case had no licence in the text).

## Files in the row
bc-interpretation-time.l4, bc-interpretation-definitions.l4, bc-interpretation-repeal.l4, bc-tests-time-periods.l4, bc-tests-time-holidays.l4, bc-tests-time-commencement.l4, bc-tests-time-words.l4, bc-tests-definitions.l4, bc-tests-repeal.l4, bc-tests-alt-readings-expected-fail.l4, check.sh, srcrefs.py (helper from the skill, unedited), NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md.
