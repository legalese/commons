# PROGRESS (sgi)  -- kept on disk; re-read this, NOTES.md and the text after any compaction

(The scripts named below, `work/`, are in `DEPOSIT/../work/` and are not shipped; NOTES.md is generated from them.)

Brief: runs/dst-sgi/BRIEF.md.  Text lines 4175-6134 (Part 3 Division 2, ss 23-42A).  Work dir: runs/dst-sgi/work (scripts, src/*.l4.in templates).
Pipeline: work/src/NAME.l4.in --(work/expand.py)--> deposit/encodings/legalese-sonnet-5.5/NAME.l4 ; work/go.sh NAME runs l4 (1.6.110) + srcrefs --strict ;
work/traces.py FILE compares every #TRACE with its `-- EXPECT` on both builds ; work/units.py audit = coverage-by-line check (380 rows).
`--REF label a-b` in a template = quote lines + `@ref label (src:..)`.

## Done (layer 1 + tests, 0 errors, srcrefs strict 0 problems)
- sgi-capacity (ss 23, 24)                 + sgi-tests-capacity (20 assertions)
- sgi-ultra-vires (ss 25, 25A, 25B)        + sgi-tests-ultra-vires (48)
- sgi-director-transactions (ss 25C, 25D)  + sgi-tests-director-transactions (78 assertions, 4 traces)
- sgi-alteration (ss 26, 26A)              + sgi-tests-alteration (58, 4 traces)
- sgi-objects (ss 33, 34)                  + sgi-tests-objects (73, 7 traces)
- sgi-names (s 27)                         + sgi-tests-names (130, 4 traces)
- sgi-name-changes (ss 28, 29, 29A)        + sgi-tests-name-changes (153, 10 traces)
- sgi-conversion (ss 30, 31, 32; seam answers for s 4(1) "private company")  + sgi-tests-conversion (116, 8 traces)
- sgi-constitution (ss 35-40)               + sgi-tests-constitution (64, 4 traces)
- sgi-contracts-seal (ss 41-42A)            + sgi-tests-contracts-seal (93, 2 traces)
  ALL LAYER-1 MODULES DONE 11-18 (834 assertions satisfied in 10 tests files after the s 38(1) case added at the end; 43 traces: 15 FULFILLED, 14 BREACH, 14 RESIDUAL)
- SEAT DONE 11-18: work/gen_seat.py (+ seatspec.py, seat_header.txt, cases_header.txt, seat_25d1.txt, cases_25d1.txt) writes deposit sgi-seat.l4 (232 questions) and sgi-cases-seat.l4 (502 cases, all pass); re-run `python3 -I gen_seat.py` after any layer-1 change; cases are copied from the layer-1 tests (first case of each distinct result, up to 4 per function)

## State at the end (11-18)
- NOTES.md is written by work/mknotes.py (python3 -I mknotes.py; tables come from the layer-1 files, cov.py and jural.py; prose is in mknotes.py). Re-run it after any layer-1 change and after a new check.sh log (work/check_final.log).
- Last edits: F-I32 (s 38(1) is the one provision the earlier pass also encodes; it answers FALSE where this part answers NOTHING), one added assertion for s 38(1), one `NOT` parenthesised in sgi-alteration.
- Final gates run after those edits: check.sh (work/check_final.log), srcrefs --refs and --strict (0 problems), traces.py on every tests file, scan for unbracketed NOT, no top-level name clashes with the keel.
- NEEDS-CORE.md: not needed (no type or constructor was missing from the core).

## Decisions taken (with licence)
- Duty "within N days after X": met by an act on any day up to and including the last day (P2 `not later than the end of a period after`)  F-I8
- Offence's own question with an unmet element: JUST FALSE (Guide line 98: "the provision's own question")  split site (i)  F-I10 etc.
- "may" gated by "on the application of" / "Where": NOTHING (grant ruling)  split site (ii)
- Duty with "Upon"/"On" gate: JUST FALSE (periods ruling (b),(c); grant ruling limit 2: a duty)
- A "where"/"if" gate on a status ("is voidable"): JUST FALSE (periods ruling item (b))
- 21 days' notice (s 33(2)): P5 (not later than 21 days before the meeting)  F-I12

## Fork lines added since the first five modules (register them in NOTES.md; the text of each is in the comment beside the code)
- F-I16 s 27(1B)(a)(i) and (ii) joined by "and": literal reading, both must hold (other reading: or)
- F-I17 "a period of at least N years has passed after the date": day asked after the last day of the N years (P1, P2)
- F-I18 "unless"/"except" once met: NOTHING (one of the case-by-case questions)
- F-I19 "where"-gated "may" (Registrar's power): NOTHING, split site (ii)
- F-I20 "such further period of 60 days": number of extensions is an input; text does not say whether more than one
- F-I21 duty/bar/status gated by "If"/"Where"/"that proposes" fails: JUST FALSE (grant ruling limit 2 / periods ruling (b)); the other reading is NOTHING
- F-I22 "while an approval is in force" read as a fixed period: outside it JUST FALSE (periods ruling (a))
- F-I23 s 29(6) revocation: precondition phrased as a duty (not "only if"): NOTHING where unmet
- F-I24 s 29(11)-(13) transitional: before 3 Jan 2016 JUST FALSE; not in force then NOTHING
- F-I25 s 29A(1) "subject to s 28(3) to (6)": answered by the s 28 functions, not computed in the s 29A(1) function
Also changed 11-18: s 27(5) and s 28(3D) take the day the Registrar made the decision (decisions before 3 Jan 2016: NOTHING).
- F-I26 s 30(3) "in such manner (if any)": no manner directed -> NOTHING whether publication still required
- F-I27 s 30(7) "with such modifications as may be necessary": applies answered, modifications not
- F-I28 s 32(3)(a),(b): status runs from the date specified in the order or notice; before it JUST FALSE
- F-I29 s 40(1): duty gated by the member's requirement, "(if any)" and payment: JUST FALSE where a gate fails
- F-I30 s 41(2): after ratification the subsection is silent (NOTHING, not JUST FALSE: the end of the period is an event; s 41(1) does not release the person)
- F-I31 s 41(7): the certificate has no time fixed: a person who has not yet certified is NOTHING, not failed
- F-I32 s 38(1): outside the avoidance NOTHING (periods ruling item (c): a scope limit with no "only"); the earlier pass (NAIVE-EVIDENCE) answers FALSE: three of four input combinations differ
