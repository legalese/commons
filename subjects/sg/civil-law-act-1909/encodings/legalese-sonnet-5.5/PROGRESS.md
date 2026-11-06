# PROGRESS (Civil Law Act 1909, whole, main) -- the author's working log

Work files outside the deposit (scratchpad): <run>/work/
  env.sh (source it before every command), src/*.l4t -> expand.py -> deposit modules; seatgen.py -> cla-seat.l4 and cla-cases-seat.l4;
  scanrefs.py + mkcov.py -> work/gen/*.md (coverage, audit, jural, forks, marginal) from units.tsv, jural.txt, forks.txt; mknotes.py -> NOTES.md.

## State at the last update (2026-11-05): ALL DELIVERABLES WRITTEN AND CHECKED

- Layer 1: cla-nouns, cla-p01 .. cla-p12 (846 asserts, 16 traces); the two Interpretation Act modules copied unchanged.
- Layer 2: cla-seat.l4 (55 questions, 7 `§§` headings, @export + @desc) and cla-cases-seat.l4 (165 asserts).
- check.sh final run (target main; 1.6.109 against 1.6.108): 17 modules, 1011 satisfied, 0 failed, 0 refused, 0 errors, every row `same`. Output is pasted in NOTES.md.
- srcrefs over cla-nouns.l4 and cla-p*.l4: 0 problems. `l4 run` over all 17 files: 0 warnings, 0 errors.
- Traces: 16, outputs identical on 1.6.109 and 1.6.108 (0 differing lines in each of the four modules; re-measured after the last edit to cla-p08).
- NOTES.md written by mknotes.py (all required headings present once; four rulings pasted word for word; 55 seat questions listed; module table has no unread rows).
- encoding.json, SOURCE-LICENSE.md, BRIEF.md written.
- Unstable second encoding: not written; the reason is under `## Unstable dialect` in NOTES.md.

## Fix round after an independent review (2026-11-05)
- F-DATE-GATE added (s 8, s 31(1), s 31(2), s 32(3) answer NOTHING outside a date gate; s 34(4), s 19(4), s 35(1), (2), (6) answer JUST FALSE; s 35(2) flagged as the site the criterion does not separate cleanly). F-S8 and F-23 point at it.
- s 18 bar twin: JUST FALSE for the action in which judgment is first given (QE line added; the entitlement function stays NOTHING). s 4(10A): NOTHING kept, QE line says why it differs from s 4(10D).
- New functions: s 4(8) day asked and good discharge (p03); s 31(2)(b) last day of the 21-year term and day within it (p10, uses the Interpretation Act module's s 50(b)). New seat questions: three (55 in all); one new seat case for a 3-year lease.
- New fork lines: F-S2, F-S4-8, F-S31-21, F-S15-1, F-21-2. New NOTES section "What the text does not answer"; Source note on the Arrangement of Sections numbering.

## Last edits made after layer 1 first went green
- p03 s 4(11): MARGINAL (b) F-W2 tag. s 4(7): the joint-contract branch is now JUST FALSE (a permission lifted by "unless", fork QA). QA tags on s 4(3) and s 4(5). QE tags on s 9(5), s 19(6), s 35(3)(a).
- MARGINAL (a) tags on the where/when FALSE branches of s 9(6)(e) and s 21(2).
- Chapeau quotes added for s 5(3A) and s 9(6) so that every operative line of the Act is quoted by some rule.
- The hand-written month helpers in p08 were replaced by the main builtin `add months` (same clamping; the old helper and the builtin agreed on 9,861 date and month pairs).

## If the work is resumed
Re-run: expand.py for any changed template, seatgen.py, scanrefs.py, mkcov.py, check.sh (save its output to work/check-final.txt), then `python3 -I mknotes.py work/check-final.txt`.
