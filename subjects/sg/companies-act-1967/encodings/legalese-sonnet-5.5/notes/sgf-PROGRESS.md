# PROGRESS (sgf: ss 216, 216A and 216B of the Companies Act 1967; lines 21698-21885 of CoA1967.txt)

State: finished and checked on the last run of `work/gen_notes.py`; the numbers below are read from that run, and `NOTES.md` carries the full detail.

## Done (checked with `L4=bin/l4-main-110 L4_MAIN=bin/l4-main-109 ./check.sh`)
- Layer 1: `sgf-s216.l4` (s 216), `sgf-s216a.l4` (s 216A), `sgf-s216b.l4` (s 216B), each with quotations (`-- src:`) and `@ref` locators; `srcrefs.py check --refs` and `--strict`: 0 problems.
- Tests: `sgf-tests-s216.l4` (87 assertions, 11 traces), `sgf-tests-s216a.l4` (65), `sgf-tests-s216b.l4` (29).
- Layer 2: `sgf-seat.l4` (39 questions, generated from one table of inputs, so one fact keeps one name and one @desc), `sgf-cases-seat.l4` (119 cases, every question at least once).
- check.sh: 300 assertions satisfied on each build, 0 errors, 0 failed, 0 refused (16 modules); baseline before any sgf file: 0 assertions over 8 keel modules.
- Coverage: 42 rows over lines 21698-21885: 8 encoded, 31 fork, 3 inert (reason 1, headings), 0 repealed.
- NOTES.md written in full (edition, coverage, fork register with the rulings word for word, jural relations, marginal readings, split sites, seams, no-breach-path list, findings, what the binary does not accept, what check.sh prints).

## Decisions taken, with the text that licenses each
- Grant-named functions answer NOTHING when the "if" gate or the named class fails (ruling of 2026-11-12, limit 1): 17 functions, listed in the fork register.
- "Where"-gated duties and rules of application answer JUST FALSE (periods ruling (b)): s 216(3), s 216A(6); "where"-gated "may" (split site ii): s 216A(4); "upon"-gated "may": s 216B(3) accountable.
- A bar answers JUST TRUE when its conditions hold and NOTHING outside the limit it sets for itself ("without", "by reason only", a named scope): s 216(4), s 216B(1), s 216B(2); JUST FALSE where its own opening "where" fails (s 216(4)) or its "unless" is met (s 216A(3)).
- "Within 14 days after" a duty to lodge is counted as "not later than the end of" 14 days; "14 days' notice" before an application is counted as "not less than 14 days before" (sg-periods P5).
- No seat for the Minister: s 216(1) and s 216A(1)(b) are encoded in layer 1, and the seat asks only what the Minister's power means for a member's company.
- The Minister's limb is tied to the declared-company fact, not to s 4(1) "company" (finding 1, F-216-1).

## If work resumes
- Re-run check.sh and the srcrefs gates after any edit; the layer-1 and test files are generated from `work/src/*.l4.t` by `work/gen.py`, the seat by `work/gen_seat.py`, the cases by `work/gen_cases.py`, NOTES.md and this file by `work/gen_notes.py` (`work/` is not shipped; the generated files are the deliverable).
- Trace outcomes are compared on both builds by `work/gen_notes.py` (check.sh cannot see them).

## Files
sgf-s216.l4, sgf-s216a.l4, sgf-s216b.l4, sgf-tests-s216.l4, sgf-tests-s216a.l4, sgf-tests-s216b.l4, sgf-seat.l4, sgf-cases-seat.l4, NOTES.md, PROGRESS.md.
