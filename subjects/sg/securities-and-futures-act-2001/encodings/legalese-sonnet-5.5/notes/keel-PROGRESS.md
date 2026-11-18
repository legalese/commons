# PROGRESS (keel, sfa) -- the disk is the memory; re-read this after any compaction

Updated: 2026-11-19, final state.

## State
The work is complete: every file below is written, and the final check passed.

- `check.sh` (both stable builds): 26 modules, 1069 assertions satisfied, 0 failed, 0 refused, 0 errors, the four counts the same on 1.6.110 and 1.6.109 (the output is in NOTES.md, "What `check.sh` prints").
- `srcrefs.py check --refs` and `check --strict`: 184 locators, 1731 quote lines, 0 problems.
- Coverage: 209 rows partition the 3113 non-blank lines of `SFA2001.txt` 1 to 4224 exactly once: 199 `encoded`, 7 `inert`, 3 `fork`, 0 `repealed or blank in this text`.

## Method
The modules are GENERATED from Python specs in `../../../work/gen/` (path from this folder: DEPOSIT/../work/gen), so that every `-- src:N | text` quote line is copied mechanically from the text and every `@ref` locator is computed.
`python3 build_all.py` (run inside `work/gen`, not with `-I`) regenerates every module, tests module and the coverage table (`coverage.json`).
`docs_notes.py` and `docs_plan.py` write NOTES.md and PLAN.md from the generated modules, so a name in either document cannot drift from the code.
The generated `.l4` files in this folder are the deliverable; the generator is scratch and is not in the deposit.

## Decisions taken (with what licenses each)
- Result convention `MAYBE BOOLEAN`, `JUST FALSE` only where the text says no in its own words: the brief and the Guide's section 5.
- Periods ruling of 2026-11-05 rule (b) (a failed "where" gives `JUST FALSE`) and rule (c) (a scope limit with no "only" gives `NOTHING`); N2 (a flat negative counts as the text's no); Guide line 87 (a rule limited by its own wording gives `NOTHING` outside the limit).
  The two marginal readings for a lawyer are in NOTES.md, "Marginal readings".
- One split site, S1 (s 3(1)(b) "except that"), kind (ii), answered `NOTHING`.
- Forks F1 to F3 and the period conventions P1 to P8 and P10: NOTES.md, "Fork register".
  "business day" is not defined in Part 1 of this text (NOTES.md finding 1), so P8 is a convention.
- "relevant person" is not a term of s 4A (NOTES.md finding 2).
- Combining functions take the limbs' answers as `MAYBE BOOLEAN` inputs, so an unanswered limb stays `NOTHING`.
- `ELSE IF` after `ELSE` fails to parse: `BRANCH` is used.
  A call compared with `EQUALS` is bracketed.
  Every `NOT` is bracketed.

## Files written (all in this folder)
- Core and periods: `sfa-core.l4` (127 lines), `sfa-periods.l4`, `sfa-periods-tests.l4`.
- Definitions of s 2(1) to (6): `sfa-definitions-products`, `-schemes`, `-persons`, `-markets`, `-benchmarks`, `-rest`, each with a `-tests` module.
- s 3, s 4, s 4A, s 4B: `sfa-associates`, `sfa-interests`, `sfa-investors`, `sfa-application`, each with a `-tests` module.
- Seat: `sfa-seat-keel.l4` (31 questions) and `sfa-cases-seat-keel.l4`; the comparison with the earlier pass: `sfa-cases-earlier-pass.l4`.
- Documents: `PLAN.md` (8 numbered sections), `NOTES.md`, `NEEDS-CORE.md`, this file.
- Provided and unchanged: `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`.

## Next
Nothing: the keel stops here.
The part agents read PLAN.md; the lead hoists anything in a part's NEEDS-CORE.md at the merge.
