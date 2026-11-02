# PROGRESS.md (pass 2, completion to "whole")

Pass 2 starts here; the pass-1 file follows below it unchanged.

## baseline

Taken 2026-10-29 before any change, with L4_BIN = unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28), sha256 0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d, JL4_LIBRARY_PATH unset, `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`:

```
module                                    errors satisfied  failed  refused  expected
tests-application.l4                           0       545       0        0         0
tests-construction.l4                          0       155       0        0         0
tests-red.l4                                   7         0       7        0         7
tests-repeals.l4                               0        42       0        0         0
tests-service.l4                               0        22       0        0         0
tests-time.l4                                  0       141       0        0         0
uk-interpretation-application.l4               0         0       0        0         0
uk-interpretation-construction.l4              0         0       0        0         0
uk-interpretation-repeals.l4                   0         0       0        0         0
uk-interpretation-service.l4                   0         0       0        0         0
uk-interpretation-time.l4                      0         0       0        0         0
TOTAL (11 modules)                             7       905       7        0
```

Baseline of the source gate, same day: `cd <this directory> && python3 -I srcrefs.py check --refs ../../registers/source-bundle/ukpga-1978-30.txt uk-interpretation-*.l4 tests-*.l4` printed `194 src: lines, 71 runs, 106 locators, 0 problems`.

Baseline numbers that must still hold at the end: 905 satisfied across the existing six test files (545 / 155 / 42 / 22 / 141, and 0 in tests-red), 7 failed in tests-red.l4 (expected), 0 refused, 0 errors other than those 7.

## pass 2: status (updated as each piece lands)

Final gates, run after the last edit to any `.l4` file: check.sh TOTAL (22 modules) errors 7, satisfied 2639, failed 7, refused 0; srcrefs 604 src: lines, 290 runs, 387 locators, 0 problems; coverage.py 436 units, 0 problems; gen_schedule1.py check 110 rows, 0 problems. All pass-1 files unmodified (mtime 15:06:23). Done; the report is the final message.

Plan, in order: (1) audit [done]; (2) `uk-interpretation-schedule1.l4` + `tests-schedule1.l4`, GENERATED from `tools/schedule1.tsv` by `tools/gen_schedule1.py`; (3) `uk-interpretation-definitions.l4` + tests (structured Schedule 1 entries, Sch 1 paragraph groups, Sch 2 paras 4(2),(3),(5),(6) and 5); (4) `uk-interpretation-general.l4` + tests (s 1, 14A(6), 22(2), 23(2), 23(3) 2nd limb, 25(2)); (5) `uk-interpretation-eu.l4` + tests (s 20(2A)-(6), 20A, the 22(1) carve-out); (6) `uk-interpretation-devolved.l4` + tests (ss 23ZA, 23A, 23B, 23C, 24); (7) bookkeeping: coverage.tsv `where` column, NOTES.md (stale pass-1 sections: "What is encoded", "What is not encoded", "What check.sh prints", counts), Jural relations, fork register F22+, encoding.json 0.2.0, check.sh unchanged except nothing.

- [x] audit: tools/units.py (436 units), tools/coverage.tsv (dispositions, `where` TBD), tools/coverage.py (render, audit, check, splice), tools/pass1-coverage.tsv (the 161 pass-1 rows, extracted before NOTES.md was rewritten); NOTES.md has `## Re-disposition audit` and the generated `## Coverage table`
- [x] `uk-interpretation-schedule1.l4` (110 entries/limbs/groups, generated) + `tests-schedule1.l4` (1033 assertions, all satisfied); `srcrefs check --refs` 0 problems; check.sh TOTAL after it: 1938 satisfied, 7 failed (the expected red), 0 refused
- [x] `uk-interpretation-definitions.l4` (expanded from S/work/definitions.tmpl.l4 by S/work/expand.py, which only copies `-- src:` quote lines from the raw text) + `tests-definitions.l4` (228 assertions, all satisfied on first run); schedule1.tsv `functions` column updated (writing, offences group)
- [x] `uk-interpretation-general.l4` + `tests-general.l4` (44), `uk-interpretation-eu.l4` + `tests-eu.l4` (58), `uk-interpretation-devolved.l4` + `tests-devolved.l4` (264), `tests-direct.l4` (94: direct assertions on pass-1 helpers the coverage table names); definitions now has 241 assertions (a combined "land" function for Sch 1 [1979] + para 5(b) was added)
- [x] coverage.tsv `where` filled (via S/work/wheremap.py from the @ref locators, pruned by hand); `tools/coverage.py check` 0 problems; forks F22-F27 in NOTES (rows marked fork: 21); mutation check on the new modules: 34 mutations, 33 caught, 1 equivalent
- [x] NOTES.md stale sections (what is encoded / not encoded / check.sh prints / mutation / open questions), new sections (numbered findings, Jural relations, Changes to existing modules, needed before relying), encoding.json 0.2.0, final gates, report

Decisions taken in pass 2 (assumed, not ruled):
- Existing modules are not edited; `Provision of the Act` is not widened (not a defect fix); new types are declared beside it in the new modules.
- A fork row is a row whose provision has a fork-register entry that is a genuine second reading of the text (F5, F6, F8, F9, F10, F11, F12, F14, F15, F18, F19, F20, F21, F3/F4 on "Month", F7); F13, F16, F17 are modelling notes and stay `encoded` / have no row.

---

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
