# PROGRESS (keel agent, row iaw-mlr-k)

Written first, kept up to date.
After a compaction re-read this file, NOTES.md and the text, not a summary.

## Status (2026-11-05): all deliverables written; final check run recorded in the report

1. PROGRESS.md and the NOTES.md skeleton -- DONE
2. mlr-core.l4 (266 lines) -- DONE; compiles clean on 1.6.109 and 1.6.108
3. mlr-definitions.l4 -- DONE for lines 1-232 (regs 2 to 7); compiles clean
4. mlr-definitions-tests.l4 -- DONE: 462 assertions, hand-written expected values, 0 failed
5. PLAN.md -- DONE (naming rule, seam typing, core, seams S-1..S-19 and S-K1..S-K4, per part, pointers left to parts, difficulties)
6. NOTES.md -- DONE (coverage table for every line 1-232, fork register F1-F5, E1 and N2 verbatim, Jural relations, Marginal readings (a)-(d), Reading a result, Unstable dialect, What the main binary does not accept)
7. srcrefs check over the two modules -- 0 problems; check.sh -- same counts on both main builds

## Scope (lines 1-232 of uksi-2017-692.txt = title block, enacting words, Part 1 = regs 1 to 7)

Owner of a regulation by line number (PARTS.md): mlr1 233-1008, mlr2 1009-1585, mlr3 1586-2199, mlr4 2200-3054, mlr5 3055-3808.

## Decisions taken (with the text that licenses each)

- Label form is `reg N(..)` for every name (brief, "Label form").
- reg 1(2) commencement date is a core constant (read at lines 639, 886-894, 1142, 1858, 2009, 2946).
- reg 1(1) citation, the enacting words, headings and chapeaus are inert; reg 2 is a pointer function; blank `...` rows are "repealed or blank in this text".
- Forks (NOTES.md): F1 listed company in reg 5(1) -> NOTHING; F2 reg 6(7) vs reg 6(9) -> 6(9) yes = TRUE, 6(7) only = NOTHING, neither = FALSE; F3 "working day" in reg 3(2)(b) -> rate is an input; F4 Schedule 2 point numbering -> core names the items and numbers none; F5 "manager" (means + includes) -> FALSE, flagged.
- Hand-gathered functions (ruling E1, option B): reg 4(1) to (3); reg 6(2) with reg 6(4)(b); reg 6(7) with reg 6(9).
- Marginal readings tags in code: (a) failed "if" / flat negative -> FALSE; (b) limited by own wording -> NOTHING; (c) a "must" not done -> FALSE (reg 7(3)); (d) "means ... and includes" (manager).
- Seam inputs that carry another section's answer are `MAYBE BOOLEAN`, passed through; plain facts are BOOLEAN or core types (PLAN.md section 2).
- A part's constructors begin with the section label too, so they cannot collide with the keel's plain-phrase constructors in mlr-definitions.l4.
- gen.py strips a trailing "; and" / "; or" from copied limbs.

## Files written (all under DEPOSIT)

mlr-core.l4, mlr-definitions.l4, mlr-definitions-tests.l4, PLAN.md, NOTES.md, PROGRESS.md.
Pre-existing and untouched: check.sh, fetch-main-l4.sh, srcrefs.py.

## How the files were built (scratchpad keel-work/, not deposited)

mlr-core.l4 from mlr-core.l4.tpl; mlr-definitions.l4 from defs-1..5.tpl via gen.py (expands `@@Q a b` with srcrefs quote and `{{AFTER n key}}` with words copied from the raw line); tests from tests-1..4.tpl (copied, hand-written); NOTES.md by mknotes.py (coverage table from @ref locators); PLAN.md by mkplan.py (ranges from PARTS.md, core listing, use counts).
Rebuild: `. env.sh; cat defs-1.tpl defs-2.tpl defs-3.tpl defs-4.tpl defs-5.tpl > defs-all.tpl; python3 gen.py defs-all.tpl $DEP/mlr-definitions.l4`.

## Peeked

Nothing outside INPUTS_DIR, the two skills, and my own run directory was opened.
