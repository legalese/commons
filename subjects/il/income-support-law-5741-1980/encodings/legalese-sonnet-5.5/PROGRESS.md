# PROGRESS -- iaw-isl (Income Support Law 5741-1980, Israel), encoding legalese-sonnet-5.5

Re-read this file, NOTES.md and the text after any compaction; do not trust a summary.
RAW = <the lead's scratchpad>/runs/iaw-isl/inputs/income-support-law-5741-1980.he.wiki.txt
L4 = .../scratchpad/bin/l4-stable-98   (1.6.98 main 7689b0d; sha256 82ea44ad...263e)    L4_MAIN = .../scratchpad/bin/l4-main-108
Check line: L4=<L4> L4_MAIN=<L4_MAIN> ./check.sh        Refs line: python3 -I srcrefs.py check --refs RAW isl-*.l4        Coverage: python3 -I isl-coverage.py RAW check

## Conventions pinned (do not change; names would drift)
- Numbering is a gloss of the Hebrew numbering: section 3א = `s 3A`, 9א = `s 9A`, 12ב = `s 12B`; subsections (א)(ב)(ג)(ד)(ה)(ו)(ז) = (a)(b)(c)(d)(e)(f)(g); (ב1) = (b1); (2א) = (2A); (3א) = (3A); schedules = `sch N`; schedule items = `sch 1 item 7`; table rows = `sch 2 row 3`.
- Every decision function is named `s N(x)(y) <what the section says>` or `sch N item M <what it says>`, and returns a `MAYBE` (JUST TRUE / JUST FALSE / NOTHING; JUST n / NOTHING for amounts).
- FALSE-kind and NOTHING-kind comments on EVERY branch that answers no / not covered (greppable).
- No section GIVEN. No REFUSE. Every NOT parenthesised. One-line #ASSERT. Date day month year, never a YMD of our own.
- Figures the Law leaves to others (basic amount now, average wage, child basic amount, pension point, vehicle thresholds, s 7 determining amount, minister's periods) are INPUTS. The `{{ח:הערה}}` 2026 figures are Wikisource annotations, not the Law.
- Names unique across the whole folder (seat imports all modules).
- Nouns/shared helper defined once, in isl-nouns.l4.

## Module plan (flat folder, all isl-*.l4)
isl-nouns, isl-s01-definitions, isl-p2-eligibility (ss 2,3,3A,3B,3C,4), isl-sch1-young (Sch 1), isl-p3-rates (ss 5-8, Sch 2, Sch 4, s 30A),
isl-p4-income (ss 9-12B, Sch 3, 9A), isl-p5-claims-payment (ss 13-18), isl-p5-duties (ss 19-21A, 20B, Sch 5), isl-p5-misc (ss 22-32),
isl-tests-<module>.l4 per module, isl-seat.l4, isl-cases-seat.l4.

## Status (2026-11-04, final pass)
All deliverables written. The scratch generator (templates, case spec, notes parts) was deleted on 2026-11-04 at the lead's request, so the files here are the source of truth and later edits are by hand.
- [x] layer 1: nine modules, 225 functions and values, 6 regulative rules, 1,130 assertions in eight test files (all satisfied)
- [x] layer 2: isl-seat.l4 (99 questions, 14 groups, @export and @desc on all), isl-cases-seat.l4 (404 cases, 99 of 99 questions covered, all satisfied)
- [x] coverage: 456 rows, 509 of 509 non-blank lines, 0 problems (encoded 307, fork 46, inert1 69, inert2 20, repealed 14)
- [x] srcrefs: 0 problems under both --refs and --strict (365 src lines, 212 runs, 226 locators)
- [x] check.sh (target main): 19 modules, 0 errors, 1,534 satisfied, 0 failed, 0 refused, all same on main 1.6.108
- [x] NOTES.md all sections; encoding.json; SOURCE-LICENSE.md; BRIEF.md copy
- Forks F1 to F19 are in NOTES.md; the tokens are backticked names in the .l4 comments.
- Review pass (2026-11-04): F11 gained reading (iv), which paragraph (1) the independent parent's amount subtracts in s 12A(a)(2) and s 12B(a)(2) (taken: the section's own paragraph (1); the other reading, s 12(a)(1), is not asserted against it); NOTES.md now discloses that five seat questions (s 17(a), s 17(c) twice, s 21(c), s 22) are asked by someone other than the claimant; "moved out of inert" corrected to none (the coverage map was built once); finding 18 reworded. Comments only changed in layer 1; check.sh counts are unchanged.
- Scratch: the probe directory and four output logs removed; l4-stable-98 and l4-main-108 kept.
- Peeked: opened jl4/examples/ok/elem.l4 and list-vertical-block.l4 in the l4-ide repo (language examples, to learn the vertical LIST syntax); the libraries prelude.l4 and daydate.l4 (allowed). No other encoding opened; nothing under ~/.claude or another runs/ directory.
- Lead's findings pass (2026-11-04): (1) item 7 pregnancy: new `s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule` (fork F19), the seat question uses it, the `s 2` route function's (d)(2) input now carries either route; (2) Third Schedule: `sch 3 which row of the table applies to the household` is now a MAYBE NUMBER and answers NOTHING where two rows fit, new `sch 3 the rate of deduction for the household`, fork F17 renamed `schedule-3-overlap-is-nothing`; (3) same words: s 2(a)(9) answers NOTHING for a stay of 30 days or fewer; item 10 and s 9A(c)(2) unchanged with the reason in the code and in NOTES. check.sh 1,516 satisfied on both builds; srcrefs 365 src lines, 212 runs, 226 locators, 0 problems under --refs and --strict.
- Household split pass (2026-11-04, lead's ruling): `Household` now has four fields (spouse, children, widow, independent parent); `sch 2 which row of the table applies to the household` is a MAYBE NUMBER that sends an independent parent to rows 7 and 8 (s 5(a)(3), src:137) and answers NOTHING for a widow alone with a child (fork F4, token `second-schedule-widow-overlap-is-nothing`); `s 5(a)` and `s 30A(b)` take the row through a CONSIDER; the seat questions for s 5(a) and s 30A(b) now ask widow and independent parent as two inputs. check.sh 1,534 satisfied on both builds; srcrefs 365 / 212 / 226, 0 problems under --refs and --strict.

- Correction pass (2026-11-10, s 15(a)): corrected to the text as amended by SH 1892 p.474 s 67(4) (NOTES.md, "Correction note, 2026-11-10: s 15(a)"); `s 15(a) the 1 April before the day of death` and the seat question for it are removed and `s 15(a) the amount of the death grant` takes one input (forks F20 and F21 added). The 2026-11-04 counts above are out of date: layer 1 has 224 functions and values and 1,125 assertions, the seat has 98 questions and 401 cases, coverage is encoded 306 and fork 47 (changed by hand: `isl-coverage.py` is not shipped), srcrefs is 364 src lines, 211 runs, 225 locators with 0 problems under --refs and --strict, and check.sh (target main, l4 1.6.98, main build 1.6.109) reads 20 modules, 2,131 satisfied, 0 failed, 0 refused, every module the same on main. Three official page extracts and four cropped images of lines of a fourth page (SH 1892 p.474) are in registers/source-bundle/official/, listed with their hashes in registers/source-bundle/SOURCES.json.

Note added 2026-11-04, after the run: `isl-coverage-map.tsv`, `isl-coverage.py` are named above as they were during the run and are not shipped with this folder; NOTES.md, "Generators and checkers used and not shipped", says what stands in for them.
