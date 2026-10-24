# PROGRESS -- cb4 (Parts XV to XVIII, src:2096-2861)

Last updated: 2026-10-22, all sections done; final gates run (see "What check.sh prints" in NOTES.md).

## How this folder is built (read this first after a compaction)

- The deposit folder (`deposit/encodings/legalese-sonnet-5.5/`) holds the OUTPUT only. The sources of my `cb4-*.l4` files are TEMPLATES in `cbca/cb4/work/tpl/` (a line `--Q N M` stands for the quote lines of raw lines N to M; `work/build.py [file]` expands them into the deposit). Edit the template, then run `python3 work/build.py`, never the deposit copy.
- `work/run.sh FILE...` runs `l4 run` on a deposit file and prints diagnostics. `work/units.py` lists the provision units of the range.
- NOTES.md is assembled by `work/assemble.py` from `work/notes/*.md` and the TSVs `work/coverage.tsv`, `work/jural.tsv`, `work/xrefs.tsv`. Edit those, then run `python3 work/assemble.py`.
- Final checks: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` and `python3 -I srcrefs.py check --refs <raw> cb4-*.l4`.

## Module plan (all flat, all `cb4-`)

| module | sections | status |
| --- | --- | --- |
| cb4-common | shared types and helpers | DONE |
| cb4-amendment | ss 173-180 | DONE + tests + seat part 10 + cases |
| cb4-amalgamation | ss 181-186.1 | DONE + tests + seat part 20 + cases |
| cb4-continuance | ss 187-188 | DONE + tests + seat 30 + cases |
| cb4-borrowing-sale | s 189 | DONE + tests + seat 40 + cases |
| cb4-dissent | s 190 | DONE + tests + seat 50 + cases |
| cb4-reorg-arrangement | ss 191-192 | DONE + tests + seat 60 + cases |
| cb4-going-private | Part XVI, ss 193-194 (195-205 repealed) | DONE + tests + seat 70 + cases |
| cb4-takeover | Part XVII, ss 206-206.1 | DONE + tests + seat 80 + cases |
| cb4-dissolution | ss 207-213 | DONE + tests + seat 90 + cases |
| cb4-court-liquidation | ss 214-220 | DONE + tests + seat 91 + cases |
| cb4-liquidator | ss 221-225 | DONE + tests + seat 92 + cases |
| cb4-after-dissolution | ss 226-228 | DONE + tests + seat 93 + cases |
| cb4-seat, cb4-cases-seat | layer 2 | DONE: 299 questions, 714 assertions |

## Decisions taken (with the section that licenses each)

- Duties and powers become BOOLEAN predicates; "passive may" is an eligibility predicate; an official's duty is encoded for what it means to the person (it arises on receipt). Licensed by the "shall"/"may" wording throughout.
- "Does not invalidate / unaffected" clauses return a named enum (`Effect on validity of leaving out the dissent statement`) or `MAYBE BOOLEAN` (JUST TRUE or NOTHING). Licensed by ss 175(2), 179(2), 174(7).
- "Includes" lists return `JUST TRUE` for a listed item and `NOTHING` for another. Licensed by ss 192(1), 206(1), 209(6), 226(1).
- A judgment handed to an official ("satisfactory to the Director") is a plain BOOLEAN input.
- Forks F1 to F8 are in NOTES.md "Fork register" (F1 cumulative class vote, F2 "ceases on the date shown", F3 s 188(7) points at a repealed subsection, F4 "a further period of twenty days", F5 a one-year default, F6 form of liquidator's financial statements, F7 reliance in good faith, F8 the gate at the head of s 217).
- Every time limit is the keel's `Time limit` with the keel's counting; no rule invents a convention.
- A class vote is passed in as one BOOLEAN (`every class ... has approved by special resolution`) so the seat has plain inputs; the tally rules are in `cb4-common`.
- My own first draft of one test (cb4-tests-going-private: a 0-0 tally "signed by all" for an ordinary resolution) expected TRUE by copying the special-resolution rule; the s 2(1) definition has no signed-by-all route for an ordinary resolution, so the expectation was wrong; the assertion now says NOT, with a comment recording the first draft. NOTES finding 1; s 142(1)(a) (outside the range) gives a written route the keel does not model.
- Names that collide with the prelude (`the day before`) were renamed (`the day immediately before`).
- Six enumeration constructors that collided with a keel constructor or with each other were renamed so that every top-level name is unique (the keel's rule 3): `a director`, `an officer`, `a person who is none of these` in cb4-borrowing-sale; `a shareholder`, `a person who is none of these` in cb4-after-dissolution; `an order of another kind` in cb4-dissolution and cb4-liquidator; `any other order the court thinks fit` in cb4-court-liquidation and cb4-takeover. `work/namecheck.py` (not a deliverable) reported 0 duplicates after the renames.

## Files written

- Layer 1: `cb4-common.l4`, `cb4-amendment.l4`, `cb4-amalgamation.l4`, `cb4-continuance.l4`, `cb4-borrowing-sale.l4`, `cb4-dissent.l4`, `cb4-reorg-arrangement.l4`, `cb4-going-private.l4`, `cb4-takeover.l4`, `cb4-dissolution.l4`, `cb4-court-liquidation.l4`, `cb4-liquidator.l4`, `cb4-after-dissolution.l4`.
- Tests: `cb4-tests-amendment.l4`, `cb4-tests-amalgamation.l4`, `cb4-tests-continuance.l4`, `cb4-tests-borrowing-sale.l4`, `cb4-tests-dissent.l4`, `cb4-tests-reorg-arrangement.l4`, `cb4-tests-going-private.l4`, `cb4-tests-takeover.l4`, `cb4-tests-dissolution.l4`, `cb4-tests-court-liquidation.l4`, `cb4-tests-liquidator.l4`, `cb4-tests-after-dissolution.l4`.
- Layer 2: `cb4-seat.l4`, `cb4-cases-seat.l4`.
- Reports: `NOTES.md`, `PROGRESS.md`.
- Not edited: `cbca-core*.l4`, `check.sh`, `srcrefs.py` (lead-provided).
- Sources of the generated files (templates, specs, tables, scripts) are in `cbca/cb4/work/`, outside the deposit.
