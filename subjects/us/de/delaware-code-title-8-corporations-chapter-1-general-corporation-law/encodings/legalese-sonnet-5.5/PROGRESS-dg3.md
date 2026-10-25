# PROGRESS -- dg3 (Delaware GCL, ss 151-174 and 201-203)

How the files are made (for a resumed session): the `.l4` files here are generated from templates in the session scratchpad
(`dg3work/templates/*.l4`, expanded by `dg3work/build.py`, which copies quotation lines mechanically from the raw text); the seat is concatenated from `dg3work/parts/dg3-seat-*.l4`
and the cases from `dg3work/parts/dg3-cases-seat-*.l4` (part 06 is written by `dg3work/gen_cases_06.py`); `NOTES.md` is assembled by `dg3work/mknotes.py` from `dg3work/notes_parts/*.md` and `dg3work/cov_rows.py`
(`dg3work/final.py` also runs `check.sh` and writes the "What check.sh prints" section). Edit the templates and the parts, not the generated files. `dg3work/go.sh <file>` builds, runs and gates one file.

## Done (all green: `check.sh` prints 0 errors, 0 failed, 0 refused over 16 modules; `srcrefs.py check --refs` 0 problems on every module)

| module | sections | tests | assertions |
| --- | --- | --- | --- |
| dg3-stock-issue.l4 | 151-153, 155-158, 161 | dg3-tests-stock-issue.l4 | 215 |
| dg3-capital-dividends.l4 | 154, 170-174 | dg3-tests-capital-dividends.l4 | 91 |
| dg3-own-stock.l4 | 159, 160, 169 | dg3-tests-own-stock.l4 | 73 |
| dg3-subscriptions.l4 | 162-166 | dg3-tests-subscriptions.l4 | 59 |
| dg3-certificates.l4 | 167-168 | dg3-tests-certificates-transfers.l4 | 69 (with transfers) |
| dg3-transfers.l4 | 201-202 | (same file) | |
| dg3-s203.l4 | 203 | dg3-tests-s203.l4 | 256 |
| dg3-seat.l4 | 156 questions, each `@export`, every input `@desc` | dg3-cases-seat.l4 | 669 |

Layer-1 tests: 763. Worked cases: 669 (at least 2 per question). NOTES.md: all ten headings written; coverage 178 of 178 non-blank lines in 181 rows (125 encoded, 56 inert: 29 headings and 27 History lines).

## Next

Nothing in this piece is waiting. The lead's merge needs: wire the out-of-range inputs listed in NOTES.md (sections 103, 218(a), 243, 244, 245, 251(f), 251(g), 325, 364) to the other pieces' rules, and decide whether to promote the "facts ascertainable outside the instrument" device (NOTES.md, "Needs from the core").

## Decisions taken (and the text that licenses each)

- The "facts" sentences (s 151(a), 152(c), 157(d)) are encoded, as an inclusive definition: the occurrence of an event is a fact (JUST TRUE), anything else is NOTHING.
  The keel advised `inert`, but the brief's list of reasons for `inert` does not contain "no case fact answers it". (s 151(a), s 152(c), s 157(d))
- Forks F1 to F21: see NOTES.md. F15 to F21 were added after the layer-1 tests were written, when the cases showed readings that had not been labelled (F16 s 170(a)(2); F17 s 203(b)(4); F18 s 203(b)(3); F19 s 160(c); F20 s 203(b)(6); F21 s 153(d) and s 203(b)(3)).
- A judgment the text hands to someone else is a plain BOOLEAN input: actual fraud (152(d)), a reasonable time (151(f)), "as soon as practicable" (203(b)(5)), "not manifestly unreasonable" (202(c)(5)),
  "if the court is satisfied" (168(b)), good faith and reasonable belief (172), wilful or negligent (174(a)), a proper purpose (171).
- Dates are data: 2 February 1988 (s 203(b)(2)) and 23 December 1987 (s 203(c)(5)) are named constants with `@ref`. This range has no commencement rule of its own.
- Added late, to cover every sentence: `s 155 the board may cause scrip or warrants to be issued subject to the condition` (the three kinds of condition in the fourth sentence of s 155) and `s 160(a) the corporation may deal in its own shares` (the grant in the lead-in of s 160(a)); each has tests, and the first has a seat question.
- The seat answers a percentage on the 0 to 100 scale it takes percentages in (`What percentage of the voting stock do these votes represent`), not as a proportion.

## Files written

dg3-stock-issue.l4, dg3-capital-dividends.l4, dg3-own-stock.l4, dg3-subscriptions.l4, dg3-certificates.l4, dg3-transfers.l4, dg3-s203.l4,
dg3-tests-stock-issue.l4, dg3-tests-capital-dividends.l4, dg3-tests-own-stock.l4, dg3-tests-subscriptions.l4, dg3-tests-certificates-transfers.l4, dg3-tests-s203.l4,
dg3-seat.l4, dg3-cases-seat.l4, NOTES.md, PROGRESS.md.
