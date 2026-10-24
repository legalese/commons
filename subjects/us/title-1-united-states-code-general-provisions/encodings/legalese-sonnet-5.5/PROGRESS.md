# PROGRESS: Title 1 U.S.C. (General Provisions), row legalese-sonnet-5.5

Written as the work goes, so a context compaction can resume from disk.
After a compaction: re-read this file, NOTES.md and `../../registers/source-bundle/usc01.txt`, not a summary.

## State

- Started 2026-10-21. Target compiler: `unstable` (the brief requires `REFUSE`, `#ASSERT REFUSED`, `YMD`, `@lang en`; `main` rejects all four). Run `check.sh` with `L4_TARGET=unstable`.
- L4_BIN = /Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4, sha256 2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7 (matches the brief).
- Source: ../../registers/source-bundle/usc01.txt, 39 sections, no schedules, no tables, no repealed or blank sections.
- Finished 2026-10-21. Eight rule modules, five test files, check.sh (target unstable: 13 modules, 0 errors, 462 satisfied, 0 failed, 0 refused) and the strict source-locator gate (102 quotation lines, 127 locators, 0 problems) are green. NOTES.md, encoding.json and SOURCE-LICENSE.md are written and `_probe/` is deleted.

## Finding that shapes everything

A search of the whole text for day, week, month, year, holiday, Sunday, Saturday, recess, commence, effective, in force, takes effect, serve, notice, deemed, hour found NO provision that counts a period, moves a last day, defines a time word, fixes when an Act or an instrument binds, or deems service.
So the six functions in us-interpretation-time.l4 are named REFUSEs, and the worked cases answer "the text is silent".
Title 1 does state a few periods in its own operative sections (s 106 last six days, s 204 the day preceding a session, s 112b and s 202(c) "N days/years after"); those are read in the ordinary sense, in Part B of the time module, as labelled forks.

## Plan, in order (all done)

1. us-nouns.l4                          done
2. us-interpretation-time.l4            done (Part A: refusals; Part B: ordinary-sense helpers, B.1 to B.5)
3. us-ch1-construction.l4               done  ss 1-8
4. us-ch2-repeals.l4                    done  ss 108-111 and the two named refusals
5. us-ch2-forms-of-acts.l4              done  ss 101-107, 106a, 106b, 114
6. us-evidence-of-law.l4                done  ss 112, 112a(a), 113, 204, 209
7. us-ch2-international-agreements.l4   done  ss 112a(b), 112b
8. us-ch3-codes.l4                      done  ss 201-203, 205-208, 210-213
9. tests-time, tests-ch1, tests-ch2, tests-112b, tests-ch3   done
10. NOTES.md, encoding.json, SOURCE-LICENSE.md                done
11. delete _probe/ before the final report                    done

## Decisions taken (with the section that licenses each)

- Time items 1 to 6 and deemed service and time words are named REFUSEs: no section of Title 1 governs them (search above).
- A definition that says "includes" is encoded as a scoped function (TRUE = the section says so, FALSE = the section does not say so): ss 1, 2, 3, 4, 112b(k)(4), 112b(k)(7).
- "unless the context indicates otherwise" (s 1) is an input that switches the limb off.
- s 112, 112a, 113, 204 weights of evidence are four separate functions: Title 1 does not rank them.
- Part B helpers read "N days after" and "N years after" in the ordinary sense; a start on 29 February with a year count is a refusal, because the same calendar date does not exist.
- Deadlines under s 112b are computed through those helpers; the date "of the enactment of this section" (s 112b(h)) is an input.

## Files written

BRIEF.md, check.sh, srcrefs.py, PROGRESS.md, NOTES.md, encoding.json, SOURCE-LICENSE.md,
us-nouns.l4, us-interpretation-time.l4, us-ch1-construction.l4, us-ch2-repeals.l4, us-ch2-forms-of-acts.l4,
us-evidence-of-law.l4, us-ch2-international-agreements.l4, us-ch3-codes.l4,
tests-time.l4, tests-ch1.l4, tests-ch2.l4, tests-112b.l4, tests-ch3.l4.
