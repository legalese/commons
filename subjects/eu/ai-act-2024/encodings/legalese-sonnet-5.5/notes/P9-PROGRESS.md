# PROGRESS (P9: Articles 80 to 110 and 112)

State: every deliverable is written and was run, and the follow-up pass (FOLLOWUP-1: seat audit, fork authorities, seam S14) is done; the last full `check.sh` is printed at the end of `NOTES.md`.

How I work: templates in `../../../work/tpl/*.l4t` (outside the deposit) are expanded by `../../../work/build.py` into the layer-1 `.l4` files here
(quote lines come from `srcrefs.py quote`; `@@DUTY` builds a regulative rule from a decision function). `../../../work/run1.sh` runs a file on both builds;
`../../../work/tracecheck.py` compares every `#TRACE` with its `-- EXPECT` comment on both builds. `../../../work/seats.py` writes the seat modules and case files
from the layer-1 signatures (`../../../work/sigs.py`) and the layer-1 tests; `../../../work/coverage.py` builds the coverage table; `../../../work/notes.py` assembles `NOTES.md`.

Binaries: L4_BIN 1.6.110 (main, e51181d), L4_MAIN 1.6.109 (main, 4c887e0). Baseline before my files: `check.sh` printed the keel's modules, 0 assertions (4 on the first pass: aia-annex-x, aia-core, aia-definitions, aia-timeline; 5 now, `aia-scope` having joined the folder for the follow-up pass).

## Decisions taken (assumed, not ruled)
- Commencement IN (the brief); the keel's one gate `Art 113 the provision group applies` is called through `P9-gate.l4` with the group fixed.
- Groups: General for Arts 80-98, 101, 112; `Notified bodies, GPAI, governance, penalties and Art 78` for 99, 100; `Articles 102 to 110`.
- JUST FALSE only where the text says no in its own words (a "where" condition not met, "only if", "means", a flat negative); NOTHING otherwise.
- Articles 97 and 98: inert (2), a rule-making power and a committee; Articles 102 to 109: inert (2), amendments of other instruments; Article 110: encoded for what it means to a person; Article 112: encoded, with deadline rules that have breach traces.
- S14 (Art 2(2)) is wired: 18 layer-1 functions in Arts 81, 82, 83, 99 and 100 call `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` (fork F-S14-reach, assumed, not ruled, listed under Marginal readings); Arts 80 and 86 are not in reach (an Annex III system), nor are Arts 84, 85, 87-98, 101, 110, 112.
- The role questions for the person and the product manufacturer are still not written: their keel functions are in `aia-scope`, which is in the folder now, but the follow-up pass changes nothing but its three tasks.
- Seat cases re-ask the layer-1 tests' facts (expected values hand-written there) and add hand-written role and applicability cases; Art 99(4)(b)-(f) cases borrow the facts of the infringement the text treats the same way.

## Done
- P9-gate.l4
- Art 80: P9-art-80.l4, P9-tests-art-80.l4 (45 assertions, 12 traces)
- Art 81: P9-art-81.l4, P9-tests-art-81.l4 (65 assertions, 16 traces)
- Arts 82-84: P9-art-82-84.l4, P9-tests-art-82-84.l4 (99 assertions, 18 traces)
- Arts 85-87: P9-art-85-87.l4, P9-tests-art-85-87.l4 (36 assertions, 4 traces)
- Arts 88-94: P9-art-88-94.l4, P9-tests-art-88-94.l4 (131 assertions, 13 traces)
- Arts 95-96: P9-art-95-96.l4, P9-tests-art-95-96.l4 (89 assertions, 16 traces); Arts 97 and 98 inert (reason 2)
- Art 99: P9-art-99.l4, P9-tests-art-99.l4 (136 assertions, 8 traces)
- Arts 100-101: P9-art-100-101.l4, P9-tests-art-100-101.l4 (104 assertions, 5 traces)
- Arts 102-110: P9-art-102-110.l4 (Art 110 only; Arts 102-109 inert, reason 2), P9-tests-art-102-110.l4 (6 assertions)
- Art 112: P9-art-112.l4, P9-tests-art-112.l4 (54 assertions, 39 traces)
- Seat layer: nine seats, 87 questions, 423 case assertions (person 7/29, provider 20/103, deployer 17/82, importer 7/37, distributor 7/38, rep 7/37, manufacturer 3/19, gpai 15/61, notified 4/17)
- NOTES.md (coverage 228 rows, fork register 45 entries, each split site naming its Guide line, jural relations, marginal readings, seams, split sites, rules with no breach path, versions, seats, findings, binary notes, check.sh output)

## Follow-up 1 (2026-11-17)
- Task 1, seat audit: 87 questions read against the function each calls; 0 retitled (direction 0, subject 0); no seat file changed for it.
- Task 2, fork authorities: 32 fork entries at split sites now end with the line of `inputs/ENCODING-GUIDE.md` section 5, or the dated ruling in it, that the answer relies on, quoted (each fragment is asserted against the Guide by `work/notes.py`); 6 are marginal and listed under Marginal readings (F-88-1, F-90-2, F-92-1a, F-93-3, F-99-7, F-101-4), with F-S14-reach 7. No answer changed.
  The earlier text called the grant rule a "ruling of 2026-11-12"; the Guide in `inputs/` has no ruling of that date (PLAN.md mentions one), so every such mention (NOTES, fork register, three comments in `P9-art-85-87.l4` and `P9-art-88-94.l4`) now cites the Guide's grant rule by its own words.
- Task 3, S14: 29 layer-1 functions take the two Section B facts (7 + 5 in Art 81, 9 + 6 in Arts 82 and 83, Art 99 one, Art 100 one); 26 seat questions in seven seats ask them; 16 `JUST FALSE` branches and 2 regulative rules cut off; new layer-1 cases for each function and for every infringement of Arts 99 and 100; every one of those seats' case files holds a `JUST FALSE` Section B case and its control; six new traces.

## Next
Nothing is open. After a compaction: re-run `L4=<110> L4_MAIN=<109> ./check.sh` from this folder, `python3 -I srcrefs.py check --refs` and `--strict` with the consolidated file as RAW, and `work/tracecheck.py` over the ten P9-tests-art files; then send the final report.

## Traps met
- `NOT` must be parenthesised inside OR/AND (a bare `NOT x OR y` is `NOT (x OR y)`); a block of quote runs and `@ref`s must sit directly above the first function it governs; a duty with no time limit and no consequence stays PENDING (an open obligation) when nobody acts, it is never BREACH.
- BSD `sed -i` needs a suffix argument on this machine: use Python for in-place edits.
