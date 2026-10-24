# PROGRESS.md: Interpretation Act 1978 encoding, row legalese-sonnet-5.5

Single Sonnet 5.5 agent, working alone from BRIEF.md.
This file is the memory across a context compaction: after one, re-read this file, NOTES.md and ../../registers/source-bundle/ukpga-1978-30.txt, not any summary.

## Standing facts

- L4_BIN = /Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4, sha256 2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7 (verified); `l4 --version` prints `dev`.
  JL4_LIBRARY_PATH is unset for every run.
- Target compiler: unstable (the brief mandates `@lang en`, `REFUSE`, `#ASSERT REFUSED ... BECAUSE`, which main rejects).
  Run: `cd` to this directory, then `env -u JL4_LIBRARY_PATH L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
- The statute is silent on counting periods of days, weeks, months and years, on days of rest, recess and holiday, and on which language version has authority.
  Those are named REFUSEs, asserted by the tests; no computed date is given for the six worked period cases.

## Status

All deliverables are written and checked.

- [x] uk-interpretation-time.l4 (imports prelude and daydate only) and tests-time.l4
- [x] uk-interpretation-service.l4 and tests-service.l4
- [x] uk-interpretation-repeals.l4 and tests-repeals.l4
- [x] uk-interpretation-construction.l4 and tests-construction.l4
- [x] uk-interpretation-application.l4 and tests-application.l4
- [x] tests-red.l4 (7 failing expectations, registered in check.sh and encoding.json)
- [x] NOTES.md (coverage table, fork register, answer table, check.sh output, mutation check, open questions)
- [x] encoding.json, SOURCE-LICENSE.md, BRIEF.md, check.sh, srcrefs.py
- [x] srcrefs check --refs over every module: 0 problems
- [x] the 24 mutations were re-run after the last change to the time module (all caught); the scratch directory is deleted and DEPOSIT holds only encodings/legalese-sonnet-5.5

## Decisions taken, with the section that licenses each

- Commencement: the moment is the text's own words (`the beginning of the day`), s 4(a), (b); a GMT clock reading is a separate function on reading A of fork F6, s 9.
- s 4(b) does not reach subordinate legislation: s 23(1) excepts it and Sch 2 para 6 lists s 4(a) only; so silent subordinate legislation refuses.
- A day "to be fixed later", once fixed, is a particular day (s 4(a)); until fixed, refuse.
- "Passed" for an Act is the day of Royal Assent (s 4(b)); "published" is not a trigger anywhere in the text.
- Counting periods and rest days: refuse; daydate's `add months` clamp is not used.
- Sch 1 marks bar a definition only for Acts passed before the commencement (s 22(1), Sch 2 para 4); Sch 2 Part I is read as the whole extent for earlier Acts.

## Files

BRIEF.md, check.sh, srcrefs.py, encoding.json, NOTES.md, PROGRESS.md, SOURCE-LICENSE.md,
uk-interpretation-time.l4, uk-interpretation-service.l4, uk-interpretation-repeals.l4, uk-interpretation-construction.l4, uk-interpretation-application.l4,
tests-time.l4, tests-service.l4, tests-repeals.l4, tests-construction.l4, tests-application.l4, tests-red.l4.
