# PROGRESS (sgg): Part 11 Divisions 1 and 2, ss 365 to 386, lines 23608-25371

Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Method (so a resumed session does not rediscover it)

- Authoring is by templates: `work/src/NAME.l4.in` (in DEPOSIT/../work/, not shipped) -> `python3 work/build.py` writes `DEPOSIT/encodings/legalese-sonnet-5.5/NAME.l4`.
  Macros: `@@Q a-b` (quote lines, page furniture and amendment marks skipped), `@@R label :: a-b` (an `@ref` snapped to quoted lines), `@@QR label :: a-b` (both).
  Edit the `.in`, never the built `.l4`.
- Binary: L4=<scratchpad>/bin/l4-main-110; second build l4-main-109 for check.sh.
- Party type for regulative rules: own `s 365 party` (core `Party` has no foreign company or authorised representative): see NEEDS-CORE.md.

## Layout (planned)

| module | sections |
| --- | --- |
| sgg-scope.l4 | 365, 366, 367, and the shared types `s 365 party`, `s 365 role` |
| sgg-lodging.l4 | 368, 368A, 368B, 369, 370, 370A, 371 |
| sgg-returns.l4 | 372, 373, 374 |
| sgg-identity.l4 | 375, 376 |
| sgg-cessation.l4 | 377, 377A, 377B, 377C, 377D |
| sgg-names.l4 | 378 |
| sgg-registers.l4 | 379 to 386 |
| sgg-tests-*.l4 | one per module |
| sgg-seat.l4, sgg-cases-seat.l4 | layer 2 |

## Decisions taken (with the text that licenses each)

(filled in as the modules are written; the fork register in NOTES.md is the long form)

## Done / in progress / next

- [x] sgg-scope (+ sgg-tests-scope: 38 asserts)
- [x] sgg-lodging (+ sgg-tests-lodging: 127 asserts, 20 traces)
- [x] sgg-returns (+ sgg-tests-returns: 132 asserts, 16 traces)
- [x] sgg-identity (+ sgg-tests-identity: 37 asserts, 6 traces)
- [x] sgg-cessation (+ sgg-tests-cessation: 125 asserts, 11 traces)
- [x] sgg-names (+ sgg-tests-names: 118 asserts, 6 traces)
- [x] sgg-registers (+ sgg-tests-registers: 79 asserts, 20 traces)
- [x] seat + cases (sgg-seat.l4: 177 questions, 0 diagnostics; sgg-cases-seat.l4: 375 cases satisfied)
- [x] NOTES.md (coverage by script: 1248 non-blank lines, 329 rows, 0 unassigned; findings checked against the text)
- [x] NEEDS-CORE.md
- [x] check.sh both builds: 24 modules, 1031 satisfied, 0 failed, 0 refused, same on both, exit 0; srcrefs --refs and --strict: 0 problems in all seven modules; traces: 79 on both builds, 0 mismatches

## Conventions fixed while writing (do not change without changing every module)

- Helper scripts in work/: build.py (templates), run.sh FILE [check|run] (diagnostics, assertion counts, srcrefs --strict), traces.py FILE (every `-- EXPECT` against both stable builds).
- Answers: JUST FALSE for a duty, bar, deeming or the provision's own question when its own gate/element fails ("if", "where", "when", "upon", "unless", "until"; the offence elements: fork F-S1);
  NOTHING for a grant ("may") gated by "if" (grant rule limit 1), a scope limit without "only", "includes", silence, points outside; a "may" gated by "upon/on application/where": JUST FALSE (periods ruling (b); counted in Split sites (ii), fork F-S3).
- A bar is answered in the bar's direction ("is barred": JUST TRUE = barred; NOTHING when the "unless" is met).
- Penalty records per offence section: offence applies / maximum fine / maximum term (NOTHING when the text states none) / default penalty (NOTHING unless stated).
- "within N days after X" for a duty: `period: the date is not later than the end of a period after` (fork F-P1: an act on X itself is in time).
- Regulative rules: party `s 365 party`; WITHIN n counts days from the trace start; a duty with no time limit is listed under "Rules with no breach path".
- Input names: a fact keeps one name across modules.
- Fork ids (final; each stands for one reading, defined in the NOTES.md fork register): F-D1 (a gate not met: JUST FALSE), F-P1 ("within N after X": not later than the last day), F-P3 ("at least N has passed": later than the last day), F-S1 (split site (i), an unmet offence element: JUST FALSE), F-S3 (split site (ii), a "may" gated by where/when/upon/on application: JUST FALSE), F-E1 (an "entitled" function, s 373(8)), F-I1 (a date left to another Act, s 370A(6)), F-O1 (a director is an officer, ss 378(7), 386), F-O2 (s 372(1)(ca) "other than" the residential address), F-T1 and F-T2 (s 377(2) further time; notice of a liquidator's appointment), F-L1 (s 378(3)(a) "and"), F-U1 (s 378(1) "as provided in subsection (2)"), F-U2 (s 370(2)(c) "until"), F-B1 (s 368(3) names no bearer).
- Marginal readings noted: "Ltd" without the full stop is not one of the four endings of s 375(1)(c); the "further period of 60 days" of s 378(15)(a) is read as one further period.
- Text quirks (findings): s 378(1) refers to "subsection (2)" as providing an exception, but subsection (2) only adds refusals (the exception is in (3)); the only "or" before s 378(2)(f) stands at the end of (e)(ii); s 375(1)(a) is deleted but (b),(c) keep their letters.
