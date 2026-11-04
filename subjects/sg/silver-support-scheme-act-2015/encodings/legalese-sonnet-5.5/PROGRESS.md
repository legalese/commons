# PROGRESS (Silver Support Scheme Act 2015, SG, row iaw-sssa)

Paths (do not retype from memory; re-read BRIEF.md in this folder):
- SCRATCH = <the lead's scratchpad>
- INPUTS_DIR = SCRATCH/runs/iaw-sssa/inputs ; text = INPUTS_DIR/SSSA2015.txt (955 lines)
- DEPOSIT dir (all files here, flat) = SCRATCH/runs/iaw-sssa/deposit/encodings/legalese-sonnet-5.5
- From inside the DEPOSIT dir: RAW=../../../inputs/SSSA2015.txt ; L4=../../../../../bin/l4-stable-98 ; L4_MAIN=../../../../../bin/l4-main-108
- Run the gate: L4=<abs l4-stable-98> L4_MAIN=<abs l4-main-108> ./check.sh   (no JL4_LIBRARY_PATH)
- Other gates (all from the DEPOSIT dir; set PYTHONDONTWRITEBYTECODE=1 and delete __pycache__ after):
  python3 -I srcrefs.py check --refs $RAW <files> (and --strict)   |   python3 -I kinds.py $RAW <layer-1 and seat files>
  python3 -I coverage.py check $RAW coverage-map.txt <all .l4>   |   python3 -I traces.py $L4 <modules with #TRACE>
  python3 -I expand-quotes.py $RAW <file>   (expands `-- @@QUOTE N M` placeholders; never retype a quotation)
- The scratch helpers (probe files, a counter script, the test and NOTES generators) lived in deposit/scratch-probes/ and were deleted on 2026-11-04, with __pycache__.
- Skills read: SCRATCH/skills/encoding-a-subject, SCRATCH/skills/writing-l4-rules

## Status log
- ALL DELIVERABLES WRITTEN (2026-11-04). Layer 1 (nouns + parts 1-4) and tests 1-4: 599 assertions satisfied; seat (33 questions, `sssa-seat.l4`) and cases (148 assertions, `sssa-cases-seat.l4`) satisfied; total 747 satisfied, 0 failed, 0 refused, same counts on main 1.6.108; 17 #TRACEs match their `-- EXPECT` on stable and main.
- coverage.py check: 684 non-blank lines, 199 units, encoded=141 fork=11 inert=47 (reason 1: 26, reason 2: 21), 0 problems.
- srcrefs --refs and --strict 0 problems (700 src: lines, 99 runs, 103 locators); kinds.py 0 problems; seatcheck.py 33 questions 0 problems.
- 2026-11-04, after the independent pass: s 10(1) reordered so that an unknown status does not block a determinate answer (+9 assertions: 7 in sssa-tests-part3.l4, 2 in sssa-cases-seat.l4; no earlier expected value changed); sweep of the same shape over all modules (NOTES.md, "Reading a result"); finding 24 (commencement not checked) and fork F-14 (s 9(3)(b)(ii)) added to NOTES.md.
- The NOTES.md builder and its template were deleted with scratch-probes on 2026-11-04; NOTES.md is now the record and is edited by hand.
  Its pasted gate output (the `check.sh` table and the other gates) is the output of the final run on 2026-11-04: if any module changes, re-run the gates and replace that output.
- Final state: 747 assertions satisfied (layer 1 tests 599, seat cases 148), 0 failed, 0 refused, same counts on main 1.6.108; 33 seat questions; 17 #TRACEs.
- Remaining: none; the final report is the last message.

## Decisions taken (with licence)
- Dialect: stable 1.6.98: NO section GIVEN, NO YMD, NO REFUSE, NO hierarchy, NO sets; Date day month year; WAITUNTIL; rule GIVEN on every rule.
- 6(2)(b): do NOT use `add years` (clamps 29 Feb to 28 Feb). Build Date d m (y+65); 29 Feb -> 1 Mar (y+65) explicitly.
- Result type convention: MAYBE BOOLEAN; JUST FALSE only where the text says no; offences give JUST TRUE or NOTHING; money results are NUMBER / MAYBE NUMBER with nil (0) as the text's own no.
- Regulative rules carry no invented deadlines: ss 8(1)(b), 8(2)(b), 17(3) have none (PARTY MUST, no WITHIN); 8(3), 9(5) are SHANT with LEST BREACH BY ... BECAUSE; 14(4) takes the requirer's days as a parameter. Each has a boolean twin that carries assertions (traces are not assertable on stable); traces.py checks the `-- EXPECT <OUTCOME>` comments.
- Arrangement lines 26-31 in the deposited text pair numbers 1-4 with the wrong titles (converter misalignment): body headings are authoritative. s14(1)(b) letter appears twice (line 657 is the closing words of (b)).
- Seat rules: plain inputs only (yes/no, number, date, choice); seat-local enums in first person for choices and for tri-state answers; maybe-inputs mapped in WHERE; a Birth facts built from year/month/day with 0 = not known.

## Files written (all in the DEPOSIT dir)
BRIEF.md (copy), check.sh / fetch-main-l4.sh / srcrefs.py (provided, unmodified), PROGRESS.md, coverage.py, coverage-map.txt, expand-quotes.py, kinds.py, traces.py,
sssa-nouns.l4, sssa-part1-preliminary.l4, sssa-part2-scheme.l4, sssa-part3-administration.l4, sssa-part4-miscellaneous.l4,
sssa-tests-part1.l4 .. sssa-tests-part4.l4.
sssa-seat.l4, sssa-cases-seat.l4, seatcheck.py, marginal.py, NOTES.md, encoding.json, SOURCE-LICENSE.md.


Note added 2026-11-04, after the run: `coverage-map.txt`, `coverage.py`, `expand-quotes.py`, `kinds.py`, `marginal.py`, `seatcheck.py`, `traces.py` are named above as they were during the run and are not shipped with this folder; NOTES.md, "Generators and checkers used and not shipped", says what stands in for them.
