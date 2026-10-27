# PROGRESS -- piece dg4 (8 Del. C. ss 204-205, 211-220; src lines 671-889)

Re-read this, NOTES.md and the text after any compaction (not a summary).

## Workflow (how files are made)
- L4 sources are written as TEMPLATES in `<scratchpad>/dg4tools/src/NAME.l4.t` (scratchpad = a scratch folder outside this folder (not committed)). A line `--Q N` or `--Q N | start phrase | end phrase` is expanded by `dg4tools/build.py` into `-- src:N | <text copied from the raw file>` (so no quotation is retyped). The deposit `.l4` files are the build output.
- `dg4tools/go.sh [NAME...]` = build + `l4 check` of every module + check.sh + srcrefs gate + warnings grep. `dg4tools/cover.py` lists non-blank lines 671-889 not named by a coverage row. `dg4tools/setwhere.py FILE.json` fills `where`/`note` cells of NOTES.md rows (see w204.json).
- Stable binary: L4_BIN=<scratchpad>/stable/extension/bin/darwin-arm64/l4 (1.6.98).
- If the templates are lost, the deposit `.l4` files are still complete (only the `-- src:` lines would need re-copying with `srcrefs.py quote`).

## L4 lessons (stable 1.6.98)
- Parenthesise a genitive used as an argument: `JUST (x's f)`, mixfix arg `after (x's f)`; otherwise "unexpected AT" / type errors.
- `WHEN x FOLLOWED BY rest` takes ONE name. `max a b` works on NUMBER. `LIST a, b, c` literal works. Recursion on lists works.
- DateTime/Time constructors are not available on this build: times are days (fork F-T).
- Constructor with a field: `WHEN Ctor day THEN` works.
- check.sh counts one satisfied per #ASSERT line.

## Layer 1: DONE (all 12 modules + 10 test files, 746 assertions satisfied, 0 failed, srcrefs 0 problems, coverage table has no TODO)
Modules: dg4-s204-ratification, dg4-s205-validity, dg4-s211-meetings, dg4-s212-voting-proxies (ss 212 + 214), dg4-s213-record-dates, dg4-s216-quorum-vote, dg4-s215-nonstock-members (imports 212, 216; also holds the s 114-based applicability rules for ss 217-219), dg4-s217-fiduciary-voting, dg4-s218-voting-trusts, dg4-s219-stockholder-list, dg4-s220-inspection ((a),(b)), dg4-s220-court-orders ((c)-(h)).
Tests: dg4-tests-s204, s205, s211, s212, s213, s215, s216, s217, s218, s219, s220 (s220 covers both s220 modules).

## Forks taken (ids to use in NOTES.md fork register)
- F-T times of day: DATE only; comparison turning on order within one day returns NOTHING (s 204(b)(1) abandonment, (f), (h)(5)/(6)).
- F-B s 204(b)(1) board quorum/vote: need = max(now-requirement, earlier-larger-requirement MINUS directors elected by extinct class/former stockholder); portions worked out to numbers by the person.
- F-C s 204(c) speaks of (b)(1) ratifications; (b)(2) initial-board ratification is not sent to stockholders (FALSE).
- F-D "at least 20 days before" / "within 60 days after" / 120 days / 60 days before / 10 days: the Nth day counts (inclusive both ends).
- F-D2 s 211(c) "for a period of 30 days after D" / "13 months after L" has run when application day >= D+30 / L+13 months (clamped).
- F-E s 204(d)(4)c.: s 203(a)(3) vote ADDITIONAL to the other requirements.
- F-P s 204(g) "prompt" no figure: fact the person states.
- F-R composite "ratified in accordance with this section" inferred from (b)-(f),(h)(6); (g) notice does not undo it.
- F-V s 204(h)(6)b. time specified preceding adoption: text forbids; NOTHING.
- F-O s 211(c) "not held ... or ... not taken": read as both (neither the meeting nor a consent in lieu).
- F-Q s 216 specified quorum below 1/3: floored at 1/3 (not ineffective).
- F-L plurality tie for the last seat: NOTHING.
- F-U s 213(c): text bounds record date only from below (60 days prior to action); no upper bound relative to action.
- F-N s 114(b)(2)/(c)(2) reading of ss 217-219 for nonstock kinds (dg1's section, read at src:200-207 only).
- F-M s 220(a)(3): member of a nonstock corporation = stockholder (s 114(a); words of (b)(5)).
- F-3Y s 220(a)(1)c.,d.,g.: 3-year window applied to the record's own date (meeting/communication date; fiscal year end).
- F-B5 s 220(c) "5 business days": count of business days ended is an input (no business-day unit in core).
- F-E2 s 220(e): limits orders about "books and records" (defined), ledger/list orders under (c) stay.
Findings to record under "What the text turns out to say": s 219(a) examination window ends the day before the meeting (nothing about the day itself); s 215(d) no waiting period (unlike s 211(c)'s 30 days/13 months); s 220(f) does not reach (a)(1)i. for an unlisted corporation; s 204(d)(3) says "within 120 days from the applicable VET" while (g)/205(f) say later of VET and notice; s 216 vs 215(c): floor of 1/3 only for stock corporations; s 204(c) does not apply to (b)(2).

## Cross-references out of range (inputs made) - to list in NOTES
s 103 (dg1): filing/effective date of certificate; s 103(c)(3) filing date; s 108 (dg1) initial board; s 116 (dg1) documents; s 122(18) (dg2) agreement (a)(1)h; s 104 (dg1) certificate of incorporation; subchapter II (dg2) power of corporation; s 161 (dg3) power to issue; s 203(a)(3) (dg3) vote; s 224 (dg5) stock ledger recording; s 227 (dg5) Court meeting powers; s 228(d),(e) (dg5) consents/notice; s 222, 229, 230, 232, 233 (dg5) notice; 15 U.S.C. 78m, 77n, 78o(d) Securities Exchange Act; "the vote required for the type of act" (various).

## Layer 2: DONE
- dg4-seat.l4: 164 questions with @export and @desc, generated by dg4tools/seatgen/gen.py from header.txt and parts_a.py to parts_h.py; compiles clean.
- dg4-cases-seat.l4: 425 assertions written, 425 satisfied; every question has at least one case; NOTHING (not covered) cases are asserted for the nonstock gates, ties, zero-person quorums, `s 218(d)` and `s 220(b)(4)a.`.
- Cases were hand-derived before running; a mutation test (39 expected values flipped on a copy) printed 39 failures, so the assertions bite.

## Coverage table
- 107 rows: 57 encoded, 25 fork (the rows whose note names a fork), 25 inert (12 section headings and the Subchapter VII heading, 12 History lines); dg4tools/cover.py: 0 uncovered lines, 0 lines named twice.

## Status
- DONE (as of 2026-10-25): layer 1 (12 modules, 11 test files), layer 2, NOTES.md with all ten headings filled, `check.sh` green (see NOTES.md `## What check.sh prints`), srcrefs 0 problems.
- Advisor review done on 2026-10-25; its three drift items (the s 114 line range, the F-D `where` cell, this status) are fixed. The probe copies in the scratchpad are deleted. Nothing remains but the final report.
- If NOTES.md is edited again, rerun dg4tools/notes/verify_quotes.py (every quoted string must be in the source, every backticked name in a .l4).
