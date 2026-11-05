# PROGRESS (State Courts Act 1970, main, legalese-sonnet-5.5)

Binary: L4_BIN = <bin>/l4-main-109 ; L4_MAIN = .../bin/l4-main-108.
Build tooling (NOT in deposit): <scratch>/sca-build/ (expand.py turns src/*.l4.in into the .l4 files here, expanding `@@Q a-b cite` into srcrefs quote lines + @ref).
Source text line numbers: body is lines 190-2509; Legislative History lines 2510-3721 (inert, "not part of the Act"). NOTE the Arrangement of Sections (lines 20-181) is garbled by the converter (headings misaligned with numbers): body numbering governs.

## Plan (modules)
sca-nouns, sca-p1-preliminary (ss 1-2), sca-p2-constitution (ss 3-8), sca-p3-appointments (ss 8A-18),
sca-p4-civil-district (ss 19-49B), sca-p4-magistrates-criminal (ss 50-54AA), sca-p4-transfers (ss 54A-54G),
sca-p5-administration (ss 57-69), sca-p6-supplemental (s 70, Schedule), sca-tests-*.l4, sca-seat, sca-cases-seat.

## Decisions
(see NOTES.md fork register)

## Status (final, before the advisor check)
DONE: layer 1 (ten modules), layer 2 (sca-seat.l4: 61 exported questions; sca-cases-seat.l4: 176 assertions), tests (712 assertions), NOTES.md, encoding.json, SOURCE-LICENSE.md.
Checks run last: check.sh (17 modules, 888 satisfied, 0 failed, 0 refused, main column `same` everywhere); l4 check: 0 diagnostics; srcrefs: 0 problems; coverage --check: COVERAGE OK (480 rows).
Build tooling is outside the deposit (scratchpad/sca-build): src/*.l4.in, expand.py, notes/, assemble_notes.py, notes_template.md.
Traps found: `NOT (a) OR b AT MOST c` parses as NOT ((a) OR ...); `JUST (call)` is a parse error; a multi-word record type needs backticks before OF.
Advisor completion check done; final report sent.

## Fix round (2026-11-05, after an independent test pass)
1. s 29(1) interpleader: each head is its own ground (assumed, not ruled); the limit is tested only on (b). Function `s 29(1) this section gives a District Court jurisdiction to grant relief by way of interpleader`; fork F-S29-AND rewritten; tests p4a (10 rows) and seat cases (8 rows); seat question text and its @desc for the amount.
2. The nine QB functions (ss 5, 6, 6A(3), 17(1), 17(3), 17(4), 49B(2), 59, 62(6)) now end "as the section requires"; every call site and test follows; no collision; answers unchanged.
3. New or extended forks: F-S17-2A, F-S25-B, F-S25-C (new), F-S39-LIMIT (extended), F-S29-AND (rewritten); new tests for s 25(b) and s 39(1).
4. NOTES: new sections `## Seams` and `## What the text does not answer`; the two source dates reconciled in the header.
Counts after the round: 17 modules, 906 assertions on each build (p4a 220, cases 181), seat 61 questions, srcrefs 0 problems, coverage OK.
