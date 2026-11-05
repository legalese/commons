# PROGRESS (disk memory; re-read this, NOTES.md and the text after any compaction)

Started 2026-11-05. Paths: DEPOSIT=.../runs/iaw-poca/deposit; this folder = DEPOSIT/encodings/legalese-sonnet-5.5; INPUTS=.../runs/iaw-poca/inputs; L4_BIN=<bin>/l4-main-109; L4_MAIN=<bin>/l4-main-108 (absolute paths in the task message and BRIEF.md).
Run checks: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> TMPDIR=<scratchpad>/tmp ./check.sh`; refs: `python3 -I srcrefs.py check --refs INPUTS/ukpga-2002-29-part-7.txt *.l4`; coverage: `RAW_DIR=INPUTS python3 -I coverage.py audit|check|write NOTES.md`; tags: `python3 -I tags.py *.l4`.

## Done
- Orientation: brief, guides, both skills, source-patterns 1,2,4,5,8,9,11 (parts), dialects, regulative, gotchas, builtins; sample seat read.
- Probes on 1.6.109: diamond imports work; BRANCH over MAYBE BOOLEAN with EQUALS JUST TRUE / NOTHING works; `is weekend` and Date arithmetic work.
- coverage.py written; audit: 994 non-blank lines (820 + 174) all owned by a row; 1006 rows (11 headings, 41 sections, 322 subsections, 502 paragraphs, 130 terms).
- Scaffolding: BRIEF.md, NOTES.md skeleton (E1/N2 verbatim in the fork register), PROGRESS.md.

## Plan (module order)
1. poca-nouns.l4  2. poca-sch9.l4  3. poca-interp.l4 (s 340)  4. poca-threshold.l4 (s 339A)  5. poca-dealing.l4 (ss 327-329, 334)
6. poca-consent.l4 (ss 335, 336, 336A-D)  7. poca-disclose.l4 (ss 337, 338, 339, 339ZA-339ZG)  8. poca-failure.l4 (ss 330-332, 333A-E)  9. poca-orders.l4 (ss 339ZH-339ZL)
10. tests per module (poca-tests-*.l4)  11. poca-seat.l4, poca-cases-seat.l4  12. NOTES.md full, encoding.json, SOURCE-LICENSE.md.

## Decisions taken (with licence)
(see NOTES.md fork register)

## In progress / next
- Write coverage-map.tsv as modules land.

## Log (newest last)
- poca-nouns.l4, poca-sch9.l4, poca-tests-sch9.l4 landed: 191 asserts written = 191 satisfied on 109; 0 errors on 108; srcrefs 0 problems.
  mkrefs.py expands `@@Q`/`@@R` macros into quote lines + `@ref` (it drops dots-only lines, which srcrefs rejects as "no text").
  coverage-map.tsv holds all Schedule 9 rows (76 entries; 0 unresolved sch9 rows).
- poca-interp.l4 (s 340), poca-threshold.l4 (s 339A), poca-consent.l4 (ss 335-336D) landed with tests: interp 70, threshold 24, consent 202 asserts, all satisfied on 109 and 108; srcrefs 0 problems (re-run at the end).
  poca-nouns.l4 now holds the penalty ceiling, party and act types.
  Tools: runtest.sh (counts for one test file), traces.sh (the #TRACE results, compared between builds by eye), covgen.py + coverage-manual.tsv -> coverage-map.tsv, mkrefs.py.
- poca-disclose.l4 (ss 337-339ZG) landed with poca-tests-disclose.l4 (211 asserts, all satisfied on 109 and 108; traces identical on both).
- poca-orders.l4 (ss 339ZH-339ZL) landed with poca-tests-orders.l4 (122 asserts, all satisfied on 109 and 108).
  Remaining before the seat layer: poca-dealing.l4 (ss 327-329, 334) and poca-failure.l4 (ss 330-333E).
- poca-dealing.l4 (ss 327-329, 334) landed with poca-tests-dealing.l4 (208 asserts, 8 traces, all satisfied on 109 and 108, traces identical).
- poca-failure.l4 (ss 330-332) landed with poca-tests-failure.l4 (217 asserts, 12 traces, identical on both builds).
  Next: poca-tipping.l4 (ss 333, 333A-333E), then the seat layer.
- poca-tipping.l4 (ss 333-333E) landed with poca-tests-tipping.l4 (105 asserts, 5 traces, identical on both builds).
  Coverage: 1006 rows, 0 unresolved, 0 forbidden dispositions.  Layer 1 is complete; next the seat layer (poca-seat.l4, poca-cases-seat.l4), tags.py, NOTES.md, encoding.json, check.sh run.
- Seat layer landed: poca-seat.l4 (first 36, then 47 questions in 11 groups after the advisor review found ss 339ZB to 339ZF and 339ZJ missing; all @export, every input @desc) and poca-cases-seat.l4 (281 cases, all satisfied on 109 and 108).
  s 336B(2) moved out of inert (encoded in poca-consent.l4, tests added); eight lead-in rows re-labelled inert reason 1 instead of reason 2.
- tags.py (FALSE/NOTHING audit; 223 quotations found in the source; 0 violations), marginal.py (generates the Marginal readings table), NOTES.md complete, encoding.json and SOURCE-LICENSE.md written.
- Final check.sh: 21 modules, 0 errors, 1633 satisfied, 0 failed, 0 refused, same on main.  srcrefs 0 problems.  Coverage 1006 rows, 0 unresolved.
  Advisor review done; its findings (missing seat questions, helper comment, honest record of two wrong hand expectations, l4_main sha256) are fixed.  Remaining: scratchpad tidy, final report.
- Ruling of 2026-11-05 (periods, "where" conditions, scope limits) applied rule-wide: s 337(1), 337(4A), 338(4A), 339(3), 339ZA, 339ZC(2)/(4)/(5), 339ZE(2)/(5)/(7)/(8)/(9), 339ZF(3)/(4), 336A(5), 336B(2), 327/328/329 "(2G)/(9)", 339A(4), 339ZH(8) now JUST FALSE when the condition fails; 336C(1)/(3) companions added; see NOTES fork F12.
  s 340(13) folded into s 335(1), 335(2)(a), 339ZA, 339A(3)/(4) (F13).  New rules: s 336A(7) calendar date and limit, s 339(1) who prescribes, sch 9 para 1(4)(d)(ii) limb, s 335(2)(a) from the recipient.
  Dependencies section written; encoding.json has "dependencies".
  Final check.sh: 21 modules, 0 errors, 1672 satisfied, 0 failed, 0 refused, same on main.  srcrefs 0 problems (888 src lines).  tags 0 violations (251 quotations).  Coverage 1006 rows, 0 unresolved (951 encoded, 42 inert, 2 fork, 11 repealed or blank).
