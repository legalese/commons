# PROGRESS -- dg5 (Delaware General Corporation Law, 8 Del. C. ch. 1, ss 221-233 and 241-246)

Read this first after any compaction, then NOTES.md, then the text (`sed -n 'A,Bp'` on lines 890-1057).

## Tools (outside the deposit; they only read the text and write nothing but the .l4 files they are pointed at)

- `INPUTS_DIR/tools/expand.py RAW FILE...` expands `@@Q N :: start :: end` placeholder lines in a .l4 into mechanical `-- src:N | ...` quote lines (in place). Never type a quotation by hand.
- `INPUTS_DIR/tools/coverage.py RAW NOTES.md 890 1057` lists non-blank lines of the range that no coverage row names.
- L4 = the stable binary named in the brief. `check.sh` as `L4=<bin> L4_TARGET=unstable ./check.sh`.
- `python3 -I srcrefs.py check --refs RAW <files>` must print 0 problems.

## Plan (modules, in the order they will be written)

| module | sections |
| --- | --- |
| dg5-s232-s233-delivery-of-notice.l4 | 232, 233 |
| dg5-s222-s229-s230-notice-of-meetings.l4 | 222, 229, 230 |
| dg5-s221-s224-bonds-and-records.l4 | 221, 224 |
| dg5-s223-s225-s227-directors-and-courts.l4 | 223, 225, 226, 227 |
| dg5-s228-consent-in-lieu-of-meeting.l4 | 228 |
| dg5-s231-inspectors.l4 | 231 |
| dg5-s241-s242-amendment.l4 | 241, 242 |
| dg5-s243-s245-capital-and-restatement.l4 | 243, 244, 245 |
| dg5-seat.l4, dg5-cases-seat.l4 | layer 2 |
| dg5-tests-*.l4 | layer 1 tests, one file per module |

## Status

Done (layer 1 module + its tests, both clean; srcrefs --refs 0 problems on the module):
- dg5-s232-s233-delivery-of-notice.l4 + dg5-tests-delivery-of-notice.l4 (79 asserts satisfied)
- dg5-s222-s229-s230-notice-of-meetings.l4 + dg5-tests-notice-of-meetings.l4 (91 satisfied)
- dg5-s241-s242-amendment.l4 + dg5-tests-amendment.l4 (125 satisfied)
- dg5-s223-s225-s227-directors-and-courts.l4 + dg5-tests-directors-and-courts.l4 (127)
- dg5-s228-consent-in-lieu-of-meeting.l4 + dg5-tests-consent-in-lieu-of-meeting.l4 (62)
- dg5-s231-inspectors.l4 + dg5-tests-inspectors.l4 (43)
- dg5-s243-s245-capital-and-restatement.l4 + dg5-tests-capital-and-restatement.l4 (65)
- dg5-s221-s224-bonds-and-records.l4 + dg5-tests-bonds-and-records.l4 (28; s 221 takes the 242(b)(2) outcome as a BOOLEAN; the test imports dg5-s241-s242-amendment to compose it)
SEAT DONE: dg5-seat.l4 (118 @export questions, compiled clean, every input has @desc) and dg5-cases-seat.l4 (212 asserts, every question has a case, all satisfied). Generic constructors were renamed to section-specific phrases (someone else -> someone else, who may ...; the proxies -> the proxies the inspectors examine; etc.).
LAYER 1 IS COMPLETE (8 modules, 8 test files, 620 asserts, all satisfied). Next: NOTES.md (coverage table, fork register F1..F11, jural relations, cross-refs, findings), then dg5-seat.l4 and dg5-cases-seat.l4, then check.sh + srcrefs over everything.
Not yet done (old line kept for the record): NOTES.md (not yet written: coverage table, fork register F1.. as cited in the .l4 comments), seat, cases-seat.
Dialect lessons: a genitive used as an ARGUMENT of a mixfix rule must be in brackets `(a's `x`)`; a typed empty list is a rule with GIVETH (no `:` annotation); CONSIDER binds a payload as `WHEN JUST d THEN`, `WHEN `ctor` x THEN` (no WITH); run helper: inputs/tools/run1.sh FILE (never `2>&1 > file`).
Forks cited so far in comments (to write up in NOTES.md): F1 boundaries inclusive (222(b) 10/60 days; 222(c) strictly more than 30; 233(b) day 60 inside), F2 whole-day granularity for 'time', F3 233(b) last day, F4 222(c) failure of the three ways means notice required, F5 directors' majority counted against the whole board (241(b)), F6 242(b)(1) cumulative overall and class majorities, F7 242(d)(1)(B) proportionate increase as cross-product, F8 242(d)(2) 'exceed' is a comparison of two counts.

## Decisions taken (section that licenses each)

- Every "may" / "must" the person would ask about is a BOOLEAN decision, not a DEONTIC value (source-patterns 5.1, 5.2).
- A judgment the text gives the Court of Chancery is a conditional input ("if the Court so orders"); the rule answers whether the person may ask, and what follows if the Court does.
- A case the text does not answer is `MAYBE` with `NOTHING`, asserted.
- No dates or commencement rule in this range (checked: the only absolute date-like tokens are in History lines).

## Files written

Layer 1 (8 modules, 8 test files, 620 assertions):
- dg5-s221-s224-bonds-and-records.l4, dg5-tests-bonds-and-records.l4 (28)
- dg5-s222-s229-s230-notice-of-meetings.l4, dg5-tests-notice-of-meetings.l4 (91)
- dg5-s223-s225-s227-directors-and-courts.l4, dg5-tests-directors-and-courts.l4 (127)
- dg5-s228-consent-in-lieu-of-meeting.l4, dg5-tests-consent-in-lieu-of-meeting.l4 (62)
- dg5-s231-inspectors.l4, dg5-tests-inspectors.l4 (43)
- dg5-s232-s233-delivery-of-notice.l4, dg5-tests-delivery-of-notice.l4 (79)
- dg5-s241-s242-amendment.l4, dg5-tests-amendment.l4 (125)
- dg5-s243-s245-capital-and-restatement.l4, dg5-tests-capital-and-restatement.l4 (65)

Layer 2: dg5-seat.l4 (118 @export questions), dg5-cases-seat.l4 (212 assertions).
Notes: NOTES.md (ten headings), this file.

## DONE (all gates green on the final files)

- NOTES.md written with the ten required headings; inputs/tools/coverage.py: rows 139, non-blank lines in range 150, uncovered 0.
- check.sh (L4_TARGET=unstable): 19 modules, 0 errors, 832 satisfied, 0 failed, 0 refused.
- srcrefs --refs over every dg5 .l4: 171 src lines, 123 runs, 212 locators, 0 problems.
- l4 check on every dg5 file: no 'is at the end of the file', 'follows code on its line' or 'Unknown annotation'.
- 32 `-- out of range: section N (piece X)` comment lines added above the rules and records that take an outside outcome as an input.
- Items checked against the code while writing NOTES (names, fork numbers, test evidence); corrections made: rule names given in full, Q-number references replaced by file and section, a wrong row count, a wrong F-number, an unverified build string removed.
