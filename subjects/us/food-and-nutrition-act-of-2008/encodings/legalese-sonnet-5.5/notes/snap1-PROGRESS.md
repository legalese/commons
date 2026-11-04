# PROGRESS (snap1)

Status: 2026-11-04, finished. Layer 1, its tests, the seat layer and its cases, NOTES.md and SEAMS.md are written; `check.sh` is green on the stable binary 1.6.98 and the main build 1.6.108 with the same counts (the last run is in NOTES.md, "Checks").
After any compaction re-read this file, NOTES.md and the text, not a summary.

## HOW THE FILES ARE MADE (read this first)

- The `snap1-*.l4` files in this folder are GENERATED from `work/src/*.l4` by `work/build.sh` (macro lines `--REF N-M | cite`, `--REF N | cite | start | end`, `--INCLUDE file` from `work/gen/`). NEVER edit a file here: edit `work/src/`, then run `work/build.sh` (it refuses to overwrite a hand-edited file, and it runs `srcrefs.py check --refs`, `--strict` and `verify-quotes.py`). The `work/` folder is scratch beside the deposit and is not part of it.
- `work/gen/*.l4` is made by `work/tools/gen_tables.py` from the USDA file (figures are copied, not typed).
- `snap1-cases-seat.l4` is made by `work/tools/gen_seat_cases.py` from a table of hand-written expected values; it reads the question names from the seat.
- `NOTES.md` and `SEAMS.md` are made by `work/tools/make_notes.py` from `work/notes-template.md`, `work/seams-template.md`, the coverage script `work/tools/coverage.py`, the Hohfeld rows `work/tools/jural_rows.py`, the modules and the last `check.sh` output (`work/check-out.txt`). Re-run it after any change.
- `work/run.sh FILE.l4` runs one file on the stable build and prints counts (each assertion is printed twice by `l4 run`, so "satisfied-lines(x2)" is twice the assertions).
- Full check: `L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh` in this folder.

## Conventions decided

- Layer 1 names begin with the section label (`s 2014(e)(6)(B) ...`); helpers are `snap1 ...` in `snap1-logic.l4` (Kleene `both`, `either`, `not`, `known`, `is definitely yes/no`).
- `JUST FALSE` only on the text's own no (a `FALSE-kind` comment quoting the words); `NOTHING` with a `NOTHING-kind` comment. Readings (a) and (b) are listed in NOTES.md.
- A `DEONTIC` value cannot be compared by `#ASSERT`: every duty has a `#TRACE` plus an asserted decision-function twin.
- Parenthesise every `NOT`; a multi-line `LIST` of `OF` records needs each element in parentheses.
- The seat: questions "Under section N, ..."; unknown answers are two plain inputs, passed on as `NOTHING`; FY2027 USDA figures fixed.

## Done

- Layer 1: `snap1-logic`, `snap1-s2012a`, `snap1-s2013`, `snap1-s2014-abc`, `-d`, `-e1`, `-e2`, `-f`, `-g`, `-hn`, `snap1-s2014a`, `snap1-s2018`, `snap1-s2019`, each with `snap1-tests-*` (the e1 and e2 share one test file).
- Layer 2: `snap1-seat.l4` (44 questions) and `snap1-cases-seat.l4`.
- The coverage audit (NOTES.md, "Coverage"): found 13 body units no rule quoted; quoted them; added two rules (`s 2018(i)(1)(D) the report includes the recommendations`, `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application`).
- NOTES.md: coverage, fork register (13 forks), Hohfeld table, marginal readings, reading a result, seams, seat, 20 findings, what the stable binary does not accept, PLAN.md versus the brief, checks. SEAMS.md: ASKS and ANSWERS.

## After the independent review (2026-11-04)

- The reviewer's tests failed 87 assertions in my range; after the lead's triage against the brief's lists of grounds, 60 pass and 27 differ (NOTES.md, "After the independent review").
- Changed: the gross monthly income limit is the published USDA Table 2 figure (`s 2014(c)(2) the gross monthly income limit for the household`, same name and type; new rule `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit`, used by the seat); eight rules whose failed "if" or "except" answered `NOTHING` now answer `JUST FALSE` (`s 2014(a)` second and third sentences, `s 2014(c)(2)`, `s 2014(d)(6)`, `(d)(12)`, `(d)(19)`, `s 2018(h)(2)(A)` and `(h)(2)(B)`); `s 2018(c) the sentence is within the limits the subsection sets` answers `JUST TRUE` inside the limits (assumed, not ruled; NOTES.md says how to revert it alone).
- `check.sh` after the change: 28 modules, 1198 satisfied (was 1165), 0 failed, 0 refused, all "same" on the main build.

## Left for the lead

- The merge: fold the household-level `s 2012(j)` and `s 2012(l)` inputs from the per-member core functions; decide what a missing poverty line means for `s 2012(m)(3)` (`s 2014(c)(1) the poverty line for the household` returns `MAYBE NUMBER`); give the plain `BOOLEAN` inputs (`s 2020(e)(25)`, `s 2021(a)`, the three `s 2012(k)` ones, `s 2012(o)(4)`) answering functions that do not turn `NOTHING` into `FALSE`.
- Nothing is committed, added or pushed.
