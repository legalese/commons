# PROGRESS: coa23 (Companies Act 2006, lines 14666-15484: Part 34, and Part 35 up to s 1092B)

Re-read this, NOTES.md and the text after any compaction, not a summary.

## Working method

- Sources of truth on disk: the L4 modules in this folder; `../../work/src/*.l4.in` are the templates they are built from by `../../work/build.py` (macros `@@Q a-b | citation` quote raw lines mechanically and write the `@ref`); `../../work/units.py` enumerates the units of the range (772 units after the audit added 56 list rows to the 716 of the first pass; every one of the 819 non-blank lines in one); `../../work/coverage-map.py` holds the disposition, L4 name and note for each unit and builds the coverage table and the Jural relations table of NOTES.md; `../../work/notes-parts/*.md` holds the hand-written parts of NOTES.md; `../../work/assemble-notes.py` joins them into NOTES.md.
- Dev loop: `../../work/r.sh <module-name>` (build, run, summarise errors and assertion counts).
- Trace outcomes (a `#TRACE` cannot be asserted on this binary) are checked by `../../work/check-traces.py`, which reads the `-- EXPECT:` comment above each `#TRACE` and compares it with the binary's output.

## Layer 1 modules (written; each compiles clean; srcrefs --strict 0 problems)

| file | lines of the text | sections | tests |
| --- | --- | --- | --- |
| `coa23-nouns.l4` | - | types used by more than one module (registrar, any person, acts of a person) | - |
| `coa23-part34.l4` | 14666-14866 | Part 34, ss 1044-1059 | `coa23-tests-part34.l4` (133 asserts) |
| `coa23-part35-registrar.l4` | 14867-15079 | ss 1059A-1071 | `coa23-tests-part35-registrar.l4` (316 asserts, 12 traces) |
| `coa23-part35-delivery.l4` | 15080-15229 | ss 1072-1079B | `coa23-tests-part35-delivery.l4` (240 asserts, 4 traces) |
| `coa23-part35-register.l4` | 15230-15484 | ss 1080-1092B | `coa23-tests-part35-register.l4` (267 asserts, 19 traces) |

Generators in ../../work: gen_tests_*.py write work/src/*tests*.l4.in (expected values typed there from the text), gen_1059A.py, gen_1078.py, gen_1087.py write the table fragments; `work/r.sh <module>` builds and runs; `work/check-traces.py <file>` checks `#TRACE` outcomes against the `-- EXPECT:` lines.

## Status (2026-11-13)

- [x] units enumerated (work/units.py: 772 units, 819 lines, every line in a row) and coverage map filled (work/coverage-map.py; table generated into NOTES.md: 802 rows)
- [x] part34, part35-registrar, part35-delivery, part35-register, nouns + four test files (977 assertions, 34 traces)
- [x] seat (52 questions) + cases (165 assertions)
- [x] check.sh green on both builds (1142 assertions satisfied, 0 failed, 0 refused); srcrefs --refs and --strict 0 problems on every coa23 file; traces 34/34 on both builds
- [x] NOTES.md assembled by work/assemble-notes.py (re-run it after any change: it re-runs check.sh and the gates and embeds their output); NEEDS-CORE.md written
- [ ] open: the lead's review; the independent test pass (skill step 8) was not run

## Decisions taken (with the provision that licenses each)

- Regulation-making and rule-making powers (and their procedure subsections) are inert, reason 2; what the regulations MUST contain or MUST NOT contain is encoded (fork F1).
- A "means" definition, a failed "if"/"where"/"on"/"upon"/"when", a flat negative, a period fixed by the text: JUST FALSE (but a failed "if" in a function named for a grant answers NOTHING: forks F28 to F31; the grants gated by "on", "after" or "provided" keep JUST FALSE and are listed in F32 to F37). Scope limits by relative clause and grants limited by their wording: NOTHING. "unless"/"except" once met: JUST FALSE for the bar (fork F9). A bare "must" not done: JUST FALSE in a function named for compliance (fork F5).
- Every `NOT` is parenthesised (a missing pair hid a bug in s 1074(2) and s 1073(5); both fixed and tested).
- `s 1072 the document meets the requirements for proper delivery` and `s 1071 the day the registrar received the document` carry the names of inputs/PLAN.md 4.2 (PLAN 4.2 says "day", PLAN 6 says "date": the 4.2 spelling is used).
- A #TRACE cannot be asserted on this binary (`#ASSERT <deontic> EQUALS FULFILLED` is an error: unsupported equality); each regulative rule has a decision-function twin that is asserted, and each trace carries an `-- EXPECT:` line checked by work/check-traces.py.
- Text anomalies, logged as findings and forks (not repaired): s 1054(3)(b) two wordings joined; s 1059A(2) "sections 1068 1067A to 1071"; s 1083(1) "This is subject to" twice; s 1084(3) cites (2A) but the text has (2AA); s 1091 has no (2); "accountsand" in ss 1049(1)(a) and 1050(3)(a); a double comma in s 1080(1)(a); "..." and ". . . ." blanks.

## Repair of 2026-11-13 (lead's request)

- Seat audit of all 52 questions for direction and subject: five renamed (s 1079(1), s 1079(3), s 1070(3), s 1084(1A), s 1087A(3)); fork F27; `-- RENAMED 2026-11-12` above each in the seat and the cases.
- s 1092B(1): an excused person now answers NOTHING, decided case by case (fork F26; the other reading, JUST FALSE, is in the fork register and the marginal readings); two assertions restated in place with `-- RECONCILED 2026-11-12` (one in `coa23-tests-part35-register.l4`, one in `coa23-cases-seat.l4`).
- Name-test sweep of 2026-11-12: 43 grant-named functions scanned; 4 flipped to NOTHING (s 1073A(1), s 1074(5), s 1081(4), s 1087C(2); forks F28 to F31; 10 assertions restated in place with `-- RECONCILED 2026-11-12`), 7 kept JUST FALSE as flat negatives, 6 listed not flipped (F32 to F37), 0 "entitled". See the subsection in NOTES.md.
