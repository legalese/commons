# PROGRESS (P4)

Status 2026-11-17: finished; follow-up passes 1 and 2 (2026-11-17) done.
Written by the part agent P4 (Arts 28-39, Annex VII, Annex XIV).
Every count below was read from the files or from `check.sh` when this file was written; `NOTES.md` carries the full account.

## Done
- Layer 1: `P4-gate.l4`, `P4-art-28`, `P4-art-29-30`, `P4-art-31-32`, `P4-art-33-35`, `P4-art-36`, `P4-art-37-39`, `P4-annex-vii`, `P4-annex-xiv`, each with a `P4-tests-<same name>.l4` (826 test asserts, 150 traces compared on both builds; 6 of the 67 rules reach BREACH).
- Layer 2: `P4-seat-notified`, `P4-seat-provider`, `P4-seat-rep` with `P4-cases-seat-<slug>` (174 questions, 974 case asserts, mirror cases marked `-- MIRROR`). No person seat: no provision of my ranges addresses an affected person.
- `NOTES.md`: coverage table (197 rows over the 202 lines of the three ranges), fork register, reading of FALSE and NOTHING, jural relations, marginal readings, split sites, rules with no breach path, seams, versions, seats, findings, what the text does not answer, what the stable binary does not accept, what `check.sh` prints.
- `check.sh` (`L4=<l4-main-110> L4_MAIN=<l4-main-109>`): 28 modules (the keel's `aia-scope.l4` added), 0 errors, 1800 assertions satisfied, 0 failed, 0 refused, the same on the main build, every module `same`; exit 0. Before follow-up 1: 27 modules, 1761 satisfied; before follow-up 2: 28 modules, 1794.
- `srcrefs.py check --strict`: 0 problems on the layer-1, gate and test files (413 quote lines, 225 locators).

## Follow-up pass 1 (2026-11-17), from `inputs/FOLLOWUP-1.md`
- Task 1, seat audit: 174 questions read, 3 retitled (direction 0, subject 3): Article 39 (notified body), and two questions of Annex VII point 4.6 (provider). Each retitled question's case assertions carry `-- RECONCILED 2026-11-17: was ...; <reason>`.
- Task 2, fork authorities: every fork entry at a split site now quotes the Guide line (86, 87, 93, 94, 95) or the dated ruling it relies on. One answer changed because the Guide's line did not support it: Article 36(8) and Article 36(9) first subparagraph answer `JUST FALSE` when the "where" fails (periods ruling, rule (b)); it was `NOTHING` (fork F-36-where). Three of the four split-site (ii) gates ("In the circumstances", "In examining", "In the context of") fit no line literally: listed in Marginal readings M-a7.
- Task 3, seam S14: every function (43) and rule (18) of `P4-annex-vii.l4` that takes the gate inputs asks the keel's `Art 2(2)` about Article 43 through `P4-gate.l4`; `JUST FALSE` there gives `JUST FALSE` (rules: `FULFILLED`). Two more inputs (the Section B flag and the integration flag) in all of them and in their seat questions. Articles 28 to 39 and Annex XIV do not ask (notifying authorities and notified bodies); fork F-S14-reach, assumed, not ruled, with Marginal reading M-c1.

## Follow-up pass 2 (2026-11-17), from `inputs/FOLLOWUP-2.md`
- Article 32 (a presumption gated by "Where") now answers `JUST FALSE` when the "Where" fails (the body does not demonstrate conformity, or the references are not published) and `NOTHING` only for "in so far as the applicable harmonised standards cover those requirements" (periods ruling rules (b) and (c)); fork F-32-where. It was `NOTHING`. Two assertions restated in place (`P4-tests-art-31-32.l4`, `P4-cases-seat-notified.l4`); 3 new tests and their 3 seat cases; no question retitled.
- Other sites of the same shape were looked for (table in NOTES.md, Split sites (ii-b)): none to change. Three untagged duty branches (Art 28(7) second sentence, Art 28(8) first and second subparagraphs as amended) got their `fork F-unmet-where` tag, so that fork is 52 branches, not 49; no answer changed.

## Decisions taken (with the provision that licenses each)
- Annex VII follows Article 43 (group `General`); Annex XIV follows Article 30(2) (group of Articles 28 to 39): assumed, not ruled (PLAN.md section 3).
- A bare "shall" not done is `JUST FALSE` (F-bare-shall); an unmet "where" or "if" of a duty is `NOTHING` (F-unmet-where); both are case-by-case questions the Guide leaves to the encoder.
- A "may" gated by "where", "when", "in the circumstances", "in examining" or "in the context of" is `JUST FALSE` (split site (ii)): Art 36(9) second subparagraph, Art 37(4) second sentence, Annex VII 4.4 first sentence, Annex VII 5.3 second sentence; a validity gated by "where" is `JUST FALSE` too, and so is a presumption gated by "where" (F-36-where, F-32-where).
- A grant limited by a condition or a named complement is `NOTHING` (grant ruling of 2026-11-12): Art 28(2), Art 29(4) first subparagraph, Art 36(3) second sentence, Art 39.
- Months and years by the `daydate` library's `add months` and `add years` (F-months).
- The two seat questions that would take a list of codes (Annex XIV point 1 third sentence and point 4) are not offered; the stable binary accepts such a question (probed), so a reviewer can add them.

## If this is reopened
- The sources are `work/src/*.l4.in` (macros expanded by `work/build.py`; the Annex VII source is generated from `work/parts/annex-vii-head.txt` and `work/parts/annex-vii-tests-head.txt` by `work/gen_annex_vii.py`), `work/seat_spec.py` and `work/gen_seats.py`; `work/` is not shipped.
- To regenerate `NOTES.md`: rebuild, rerun `check.sh` into `work/check-full.log`, rerun `srcrefs.py` and `quotecheck.py` into `work/srcrefs-out.txt` and `work/quotecheck-out.txt`, then `python3 -I work/gen_notes.py`.
- Re-read `NOTES.md` and the text (lines 527-635, 1800-1839, 1958-2010 of the consolidated file), not a summary of them.
