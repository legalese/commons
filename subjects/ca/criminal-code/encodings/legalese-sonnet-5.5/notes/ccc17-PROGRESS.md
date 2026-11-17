# PROGRESS.md -- ccc17 (Criminal Code of Canada, lines 9544-10274: ss 487.05 to 490.019)

State on 2026-11-16, after the resume that followed the weekly-limit stop of 2026-11-12. The disk is the memory: NOTES.md is the record; this file says what was done, in what order, and what each decision rests on.

## Done

- [x] Brief, PLAN.md, the Commons guide and the two skills read; prototypes of `Date PLUS n`, `add years`, `elem` over `Provision of the Code`, `CONSIDER` on a `MAYBE`, `DEONTIC` with `#TRACE`.
- [x] Master list of text units (524 rows in 43 sections; each of the 726 non-blank lines of the range in exactly one row).
- [x] Seven layer-1 modules and seven tests files (1,110 assertions): `dna-orders`, `dna-samples`, `warrants`, `journalists`, `privilege`, `seizure`, `sor`.
- [x] Seat layer `ccc17-seat.l4` (52 questions) and `ccc17-cases-seat.l4` (147 assertions).
- [x] Coverage (524 rows: 405 encoded, 107 fork, 4 inert, 8 repealed; no `deferred`, no uncovered), jural relations, marginal readings, fork register F1 to F14 and groups G1 and G2, seams, findings, what the binary does not accept: all in NOTES.md.
- [x] `check.sh` on 1.6.110 and 1.6.109: 19 modules, 0 errors, 1,257 assertions satisfied, same on both builds; before and after the second-pass edits.
- [x] `srcrefs.py check --refs` and `--strict`: 0 problems over all 16 `ccc17-*` files.
- [x] The `#TRACE` outputs of the two builds compared, `JL4_LIBRARY_PATH` unset: identical.
- [x] Second seat-question audit pass (2026-11-12 instruction): 52 read, 12 retitled, 40 read and left, 13 assertions restated in place.
- [x] Name-test sweep (2026-11-12 instruction): 0 flipped, 13 kept `JUST FALSE`, 12 listed (group G1), 0 "entitled", 0 "it is lawful"; the 86 functions that match the name test were read, and the 27 conditioned grants that answer `NOTHING` on a failed condition carry fork F1 (answers unchanged).

## Decisions taken, and the text or ruling that licenses each

- Layer 1 imports `ccc-core` and `ccc-definitions` (the brief governs over PLAN.md section 1); only `s 2 day` and `s 2 night` are called directly (s 488); every other section 2 answer is a seam input `s 2 <term>: ...` of type `MAYBE BOOLEAN`.
- A "may" whose "if", "where" or other stated condition fails answers `NOTHING` (ruling of 2026-11-12, limit (1); fork F1, 27 functions); a grant limited only by a scope (who, where, which thing) answers `NOTHING` with no fork line. "only if", "may not ... unless" and flat negatives answer `JUST FALSE`. A "may" gated by "where", "when", "upon" or an equivalent stays `JUST FALSE` and is listed (G1).
- A duty ("shall") is encoded as "the section imposes the duty on these facts": `JUST TRUE`; `JUST FALSE` where the text's own "if", "unless" or "where" fails (marginal reading (a)); `NOTHING` where the person or case lies outside the persons the text names.
- An offence function answers `JUST TRUE` when every element is met, `NOTHING` when an element of the offence is missing ("without reasonable excuse", "fails to comply"), and `JUST FALSE` where the text itself excludes ("unless a charge has been laid").
- A regulative rule only where the text names a party, an act and a time limit (two: `s 487.053(2)(a)`, `s 490.0132(a)`); `#TRACE` is read, not asserted, and each duty is also a decision function with its period boundaries asserted.
- Seat questions: one per rule the person can ask about, named "Under section N, ..."; the layer-1 modules are never restated. The seat's question names follow the rule that a name asks what its body answers (second pass of 2026-11-12: 12 retitled).

## How to rebuild (not shipped: `work/` is outside the deposit)

`work/src/*.l4.in` are the templates; `work/build.py` expands them into the deposit; `work/coverage.py` and `work/notes.py` regenerate the tables of NOTES.md; `work/lint.py` checks the quotes and tags. Edit the templates, never the built files.
