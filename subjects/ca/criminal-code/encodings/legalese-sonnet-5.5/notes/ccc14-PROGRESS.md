# PROGRESS.md -- ccc14 (Criminal Code, lines 7875-8523: Parts XII, XII.1, XII.2, XIII)

Status log (updated as work lands; after a compaction re-read this, NOTES.md and the text).

## Plan (decided before writing)
- Layer 1 modules (flat, `ccc14-` prefix): helpers; part12-currency (ss 448-462); part122-offence (462.3, 462.31); part122-warrants (462.32-462.36); part122-forfeiture (462.37-462.46, 462.371); part122-disclosure (462.47-462.5); part13-attempts (463-467); part13-criminal-organization (467.1-467.14, 467.2).
- Tests: one `ccc14-tests-*.l4` per module. Seat: `ccc14-seat.l4`, `ccc14-cases-seat.l4`.
- Inputs from other parts are named for the section that answers them (PLAN s4, R4).
- Quote lines are expanded by `work/build.py` from `work/src/*.l4.in` templates (`@@Q a b`); coverage rows come from `work/units.py` (439 rows).
- Offence functions: element unmet -> NOTHING-kind (limited by its own wording); an "if" gate unmet -> JUST FALSE; punishments are `LIST OF Punishment` (one per limb).

## Done (module + tests, all assertions satisfied, srcrefs --strict 0 problems, work/lint.py 0 problems)
- ccc14-helpers.l4 (Kleene combinators, prefix `ccc14 `, hoist candidates)
- Part XII ss 448-462, PART XII.1 repealed: ccc14-part12-currency.l4 + ccc14-tests-part12-currency.l4 (159 asserts)
- Part XIII ss 463-467: ccc14-part13-attempts.l4 + tests (112 asserts)
- ss 467.1-467.2: ccc14-part13-criminal-organization.l4 + tests (88 asserts)
- ss 462.3-462.31: ccc14-part122-offence.l4 + tests (55 asserts)

- ccc14-part122-warrants.l4 + tests (462.32-462.36; 269 asserts; regulative rules 462.32(4)(b), 462.321(4)(c) traced)
- ccc14-part122-forfeiture.l4 + tests (462.37-462.46 incl. 462.371; 243 asserts; regulative 462.42(1) MAY WITHIN 30 traced)
- ccc14-part122-disclosure.l4 + tests (462.47-462.5; 145 asserts; regulative 462.48(15) SHANT traced)
- check.sh (both stable builds): 18 modules, 1071 satisfied, 0 failed, 0 refused, 0 errors, all "same" on main-109.
- Test files for the large modules are typed by work/gen_tests_*.py (expectations in the generator's tables, hand-written from the text).
- A real bug the tests caught: `NOT (x) AND y` parses as NOT (x AND y) (s 462.37(2.02)); every NOT in the layer-1 modules was re-read for this.

## Resumed 2026-11-16 (after the weekly-limit stop of 2026-11-12): state
- Baseline before any edit: check.sh 20 modules, 1295 satisfied, 0 failed, same on 1.6.110 and 1.6.109.
- Done: second seat-question audit (101 read; 6 retitled; 95 left), name-test sweep (1 flipped to NOTHING; 5 kept JUST FALSE; 20 listed where/when/upon; 0 "entitled"; 0 "it is lawful"), 13 assertions restated (RECONCILED 2026-11-12) in the sweep and 14 for the retitled questions, 14 assertions added (NEW 2026-11-16), local `s 462.48 party` for the SHANT of s 462.48(15), NEEDS-CORE.md, NOTES.md regenerated (once, each section once).
- Final check.sh: 20 modules, 1309 satisfied, 0 failed, 0 refused, 0 errors, same on both builds; srcrefs --refs and --strict 0 problems over the 17 ccc14 files; lint 0 problems; 11 traces identical on both builds.
- Nothing in progress. The final report goes to the lead.

## Decisions taken (with the section that licenses each)
- Offence element unmet -> NOTHING-kind (limited by its own wording); an "if"/"unless" gate unmet -> JUST FALSE; "may" power with "if" gate -> NOTHING (ruling 2026-11-12), "may" with "where/when/upon" -> JUST FALSE (ruling (b)) and counted in fork register.
- s 465(1)(b) (i)/(ii) overlap: (ii) for a longest term below 14 years, (i) for life or exactly 14 years (fork + finding).
- s 463/464/465: hybrid offences: 463(d) gives both limbs; 464 and 465(1)(c) hybrid -> NOTHING (points outside the text: text names indictable and summary only).
- s 467.1(1) serious offence: hybrid counts via its indictable limb (fork).
- Seams provided with the PLAN names: `s 467.1(1) the group is a criminal organization`, `s 467.1(1) the offence is a serious offence`; `s 462.34 the review of the special warrant or restraint order has been applied for` still to write.
