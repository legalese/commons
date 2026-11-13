# PROGRESS (coa18: Companies Act 2006, lines 10757-11596, ss 791-859)

Written 2026-11-12 by part agent coa18 (Sonnet 5.5). Read this file, NOTES.md and the text after any compaction, not a summary.
Status: every deliverable below is written; the numbers are those of the last `check.sh` run (see NOTES.md, "What `check.sh` printed").

## Layout
- layer 1 (each imports prelude, daydate, `coa-core`): coa18-part22-notice (ss 791-807), coa18-part22-register (808-819), coa18-part22-interest (820-828), coa18-part23-ch1 (829-835), coa18-part23-ch2 (836-840; imports ch1), coa18-part23-ch3 (841-853; imports ch1), coa18-part24 (853A-859); each has a coa18-tests-<same> twin.
- layer 2: coa18-seat.l4 (65 questions, all "Under section N, ...") and coa18-cases-seat.l4.
- NOTES.md, NEEDS-CORE.md (two entries: the "greater of" fine limit; the shared accounts-kind type).
- scratch and scripts, not shipped, in ../work/: expand.py (macros to quote lines), gentests.py (tests from work/tests/*.py), coverage.py (coverage table and audit), forks.py (fork register), jural.py (Hohfeld table), build-notes.py (assembles NOTES.md), check-quotes.py (every quoted piece of the comments and fork licences against the raw text), run.sh NAME (expand, run, srcrefs --strict).

## Status
- [x] part22-notice  [x] part22-register  [x] part22-interest  [x] part23-ch1  [x] part23-ch2  [x] part23-ch3  [x] part24 (all with tests, all 0 errors and 0 warnings on 1.6.110 and 1.6.109)
- [x] seat + cases-seat (every question has a case; checked by script)
- [x] NOTES.md: coverage (806 rows, 0 UNCOVERED), fork register (48 forks and note N1; F42 to F48 from the name-test sweep), jural relations, marginal readings (generated from the branch tags), reading a result, seams, findings, binary, check.sh
- [x] NEEDS-CORE.md
- [x] final check.sh (exit 0), srcrefs --refs and --strict (0 problems over all coa18 files)

## Decisions (with the licensing section; every one is also a fork-register entry or a marginal reading in NOTES.md)
- s 791 "applies only to public companies" closes (JUST FALSE for a private company); s 831(1) "A public company may only" does not (NOTHING for a private company): F1, F20.
- s 827: the working-day stepper takes the keel's "working day" rule as a FUNCTION input (it does not restate it) and applies to Part 22 only; the duty functions take the count of working days as an input and each has a last-day function: F11.
- The 14 days of ss 806(1), 809(4), 853A(1), 853L(1) are calendar days: F10, F33.
- "who" relative clauses on an offence subject answer NOTHING when the person is outside the description; a failed "if" or "where" answers JUST FALSE (marginal reading (a)); "limited by its own wording" answers NOTHING (marginal reading (b)).
- "must not ... unless" is encoded as the bar itself (JUST TRUE barred, JUST FALSE once the "unless" is met) and as a regulative rule: F5.
- The "greater of GBP 500 and one-tenth of level 4" fine limit has no core constructor: declared under the s 853L prefix, recorded in NEEDS-CORE.md; the pounds a level on the standard scale stands for is an input.
- Seams are inputs, never imports; an answering section's NOTHING stays NOTHING.
- Regulative rules are run with #TRACE; a regulative value cannot be compared with EQUALS on this binary unless it reduces to FULFILLED, so the duty is also a decision function that is asserted.

## Seat audit of 2026-11-12
- All 65 seat questions read against their functions; 3 retitled or reworded (ss 797(1)(d) @export, 807(1), 847(2)); assertions restated in place with RECONCILED comments; check.sh TOTAL unchanged at 18 modules, 1171 satisfied, 0 failed, 0 refused; see NOTES.md "Seat audit of 2026-11-12".

## Name-test sweep of 2026-11-12
- 59 functions named may/permitted/power/entitled/authorised read; 7 flipped to NOTHING (F42 to F48: ss 793(2)(b), 794(2), 799(3), 812(6), 816, 817(4), 818(3)); 11 kept JUST FALSE; 14 "may" with where/when/upon and 7 "entitled" listed in the fork register; 11 assertions restated in place (RECONCILED) in the part22 tests and the seat cases.
