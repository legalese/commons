# PROGRESS (iaw-fca: Frustrated Contracts Act 1959, whole, main)

Read this and NOTES.md after any compaction; do not trust a summary.

## State (update as you go)

- [x] Read brief, inputs, both skills (SKILL.md in full; dialects.md, source-locators.md, canon-deposit.md in full; source-patterns index + area 8 + entries 5.4, 2.2, 4.1, 4.2, 1.6, 7.1; drafting-patterns "Decision results" + deontic; gotchas selected sections; regulative.md first 120 lines).
- [x] Copied dependency sgia-p1-definitions.l4 UNCHANGED (blob ca5e2607c635962769a753d71154ad4ae6055f59 after dropping the 3-line header; sha256 of the copy 80441fd1745f75d4f142246c62213a229337a620ff5a35aeeac9732aae22af27).
- [x] fca-nouns.l4 (checks)
- [x] fca-definitions.l4 (checks; tests: fca-tests-definitions.l4, 20 asserts pass)
- [x] fca-s3-application.l4 (checks; fca-tests-s3.l4 64 asserts pass)
- [x] fca-s2-adjustment.l4 (checks; fca-tests-s2.l4 132 asserts pass (incl. the sums taken together))
- [x] fca-court.l4 (regulative; fca-tests-court.l4 13 asserts pass + 15 traces, outcomes as expected from text)
- [x] tests per layer-1 module (4 files)
- [x] fca-seat.l4 (32 questions, checks), fca-cases-seat.l4 (107 asserts pass)
- [x] NOTES.md (built from a template in the scratchpad by a script that pastes the coverage table, check.sh output and srcrefs line), encoding.json, SOURCE-LICENSE.md
- [x] check.sh run (336 satisfied, 0 failed, same on 1.6.108), srcrefs check (0 problems), mutation sanity check (3 runs, all red as expected)
- [x] advisor review done (rebuilt NOTES.md; @ref locators split per contiguous quote run; seat type renamed `Kind of matter I ask about`); gen-seat.py and the scratchpad probe folder deleted
- [ ] final report only

## Design decisions (with the text that licenses each)

- Dependency: only sgia-p1-definitions (Government s 3(2); court; party; "enactment" is inside IA "written law"). The IA time module is NOT copied: the Act counts no period; s 3(1)'s dates are fixed calendar dates compared, not counted.
- Sale of Goods Act 1979 s 7 (s 3(5)(c)) is not staged: asked as an input fact.
- "Where" condition unmet -> JUST FALSE (ruling 2026-11-05 (b)); scope limit with no "only" -> NOTHING (c); "before the time of discharge" taken as scope limit (c), fork recorded.
- Court discretion is an input (MAYBE BOOLEAN "the court considers it just"), never computed (phrasebook 8.4/8.5).
- Number-valued results (caps, net sums) are MAYBE NUMBER with a yes/no twin.
- s 3(5)(a) "except" / "(other than a charterparty)" = QE: NOTHING for X (limits a prohibition). s 3(5)(b) "except as is provided by s 2(6)" and s 2(6) "unless" = QA sites.

## Files written

BRIEF.md, check.sh, fetch-main-l4.sh, srcrefs.py, sgia-p1-definitions.l4 (given or copied); coverage.py; fca-nouns.l4, fca-definitions.l4, fca-s3-application.l4, fca-s2-adjustment.l4, fca-court.l4, fca-seat.l4; fca-tests-definitions.l4, fca-tests-s3.l4, fca-tests-s2.l4, fca-tests-court.l4, fca-cases-seat.l4; NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md.

## Next (in order)

1. Final report (files; check.sh output; coverage counts; forks; inert rows; failures: none; what the text does not answer; peeked: nothing).

NOTES.md was built from a template by a script that is now deleted; edit NOTES.md directly if anything changes (the check.sh block and the coverage table in it are pasted output, rerun them if a file changes).

## Lessons from the binary (main 1.6.109)

- `JUST (min x's amount 10)` is a parse error: bracket the genitive `(min (x's amount) 10)`.
- No inline CONSIDER inside an expression: use a helper function.
- No `length`: use `sum (map (GIVEN t YIELD 1) xs)`.
- DEONTIC outcomes cannot be asserted; #TRACE prints them.

## Fix round (2026-11-05)

- Added the sums taken together (s 2(3), fork F6): three functions and a helper at the end of fca-s2-adjustment.l4; 27 tests; 2 seat questions, 11 cases.
- F2: the time bound "before the time of discharge" now answers JUST FALSE in s 2(2), s 2(3) and s 2(4) (the number functions stay NOTHING, their twins say JUST FALSE).
- QE at s 2(4): the money-payment bracket now answers JUST FALSE.
- Seat: the s 3(5) questions say in words what no answer means; the "before" questions mention a payment on the day of the discharge.
- NOTES.md edited in place (the build script is gone): cites into fca-s2-adjustment.l4 are valid for the file as deposited; the new functions were appended at the end so no earlier line moved.
