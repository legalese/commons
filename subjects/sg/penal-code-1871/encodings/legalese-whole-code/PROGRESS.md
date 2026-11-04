# PROGRESS - completion pass iaw-pc42 (Penal Code 1871, the 42 deferred sections), 2026-11-04

Kept on disk because the context will be compacted.
After a compaction, re-read this file, `NOTES.md` and the text (`../../registers/source-bundle/PC1871.txt`), not a summary of them.

Agent: one Sonnet 5.5 agent, no subagents.
Binaries: stable 1.6.98 (main, 7689b0d, 2026-10-19), sha256 82ea44ad...263e; second stable build 1.6.108 (main, 2ae7c9b, 2026-11-02) for the main comparison.
Rule: write only under `deposit/` (this folder is `deposit/encodings/legalese-whole-code/`); logs under `deposit/logs/`.

## Baseline (step 1), before any change

Run: `L4=<stable-98> L4_MAIN=<main-108> ./check.sh` at the start, log `deposit/logs/baseline.log`.
What it printed (ended; `exit 1` only because `expected_failed` did not yet list the two expected failures; since then `check.sh` lists `pc-general-part-tests.l4) echo 2`):

```
target: main. ... main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
TOTAL (36 modules)   errors 2   satisfied 1390   failed 2   refused 0   |  main: errors 2  satisfied 1390  failed 2  refused 0
every one of the 36 modules reads "same" on the main build
```

Per module (stable-98): pc-body-a-tests 179, pc-body-b-tests 123, pc-documents-defamation-tests 172, pc-exceptions-tests 175, pc-general-part-tests 165 satisfied + 2 failed (the 2 errors), pc-general-tests 115, pc-justice-order-tests 92, pc-property-tests 218, pc-state-public-tests 151; the 27 encoding modules 0/0/0/0.
Sum of satisfied: 179+123+172+175+165+115+92+218+151 = 1390.
Every baseline number must still hold at the end, plus the additions.

## The 42 sections (derived from notes/body-a-coverage.md, notes/body-b-coverage.md, the Code's table of contents)

body-a (10): 301, 304B, 304C, 308A, 310, 311, 314, 315, 316, 335A.
body-b (32): 372, 373, 373A (3); 376B, 376C, 376D, 376E, 376EA, 376EB, 376EC, 376ED, 376EE, 376F, 376G, 376H (12); 377, 377B (2); 377BB, 377BC, 377BD, 377BE, 377BF, 377BG, 377BH, 377BI, 377BJ, 377BK, 377BL, 377BM, 377BN, 377BO (14); 377C (1).
Total 10 + 32 = 42.

## Plan / order (all done 2026-11-04)

1. [x] Audit scripts (unit counts, repealed rows show repeal text, inert rows have a reason); `## Re-disposition audit` in NOTES.md written BEFORE new L4.
2. [x] pc-body-a-deferred.l4 + pc-body-a-deferred-tests.l4 (429 assertions)
3. [x] pc-body-b-deferred.l4 (ss 372-377B) + tests (1,018)
4. [x] pc-body-b-deferred-images.l4 (ss 377BB-377BO, 377C) + tests (706)
5. [x] pc-general-moved.l4 (28 sections, 19 sub-provisions) + tests (208)
6. [x] srcrefs check --refs and --strict over all 44 pc-*.l4 (1,400 src lines, 83 runs, 397 locators, 0 problems; the first --strict run found 24 problems in two modules, mended afterwards), name-duplicate scan (0 of 1,640 names), mutation controls (18 of 18 caught), check.sh at the end
7. [x] NOTES.md, notes/deferred-forks.md, encoding.json 0.2.0, SOURCE-LICENSE.md, this file

## Final check.sh (stable 1.6.98, second build 1.6.108)

```
TOTAL (44 modules)   errors 2   satisfied 3751   failed 2   refused 0   |  main: errors 2  satisfied 3751  failed 2  refused 0
every module "same" on the main build; exit 0
```

Baseline replaced: 36 modules, errors 2, satisfied 1390, failed 2, refused 0.
3,751 = 1,390 + 2,361 new.
The 2 failed are the expected pair in `pc-general-part-tests.l4` (GP-14, GP-10).
Log: `deposit/logs/final.check.log`. Two earlier full runs are kept: `final.check.log.first-run.txt` (3,749 satisfied, before `s 335A(6)` was added) and `final.check.log.second-run.txt` (3,751, before every `NOT` was parenthesised); the numbers above are the third run, after the last change to any `.l4` file.

## Decisions taken (with the section that licenses each)

All are readings of the text; the ones that change a result are in NOTES.md "Marginal readings for a lawyer" and `notes/deferred-forks.md`.

- JUST FALSE only where the text says no in its own words, NOTHING otherwise: the 2026-10-29 rule in the brief (assumed, not ruled).
- s 1 and s 4B(3) stay inert, reason 2 (machinery): the brief's reason list.
- The 75 repealed rows stay `repealed or blank in this text`: each body shows "[Repealed by ...]" (audit.py, section 3 of the log).
- Borrowed facts (the Electronic Transactions Act 2010 meaning, the Organised Crime Act 2015 "group", the Criminal Procedure Code 2010 "sexual offence", "liable by law to be tried") are inputs: the brief says to ask the borrowed fact as input.
- The scope of ss 73(3) to 74D(4) is an input (DEF-M7).
- The `Punishment` record is read by one helper for the Magistrate's Court limit (DEF-M2).
- A sole `NOT` that is the whole of a condition, never `NOT (a) AND ...` on one line (finding 2).

## Files written or changed

Written (all under `deposit/encodings/legalese-whole-code/`):

- `pc-body-a-deferred.l4`, `pc-body-b-deferred.l4`, `pc-body-b-deferred-images.l4`, `pc-general-moved.l4`
- `pc-body-a-deferred-tests.l4`, `pc-body-b-deferred-tests.l4`, `pc-body-b-deferred-images-tests.l4`, `pc-general-moved-tests.l4`
- `generators/deferred/` (scripts, specs and sources of the above; `audit.py`; `count.sh`)
- `notes/deferred-forks.md`
- `PROGRESS.md` (this file), `NOTES.md` (rewritten where stale, new sections appended), `encoding.json` (0.2.0), `SOURCE-LICENSE.md`
- `check.sh`: one line added to `expected_failed` (`pc-general-part-tests.l4) echo 2`)

Not changed: every one of the 36 `.l4` files found, `notes/*-coverage.md`, `notes/*-forks.md`, `notes/PLAN.md`, the generators of 0.1.0, `srcrefs.py`, `fetch-main-l4.sh`, `check.sh.pass1`.

Logs under `deposit/logs/`: `baseline.log`, `final.check.log`, `audit.txt`, the `*.run.txt` files of the new tests, and small working files.


Note added 2026-11-04, after the run: `check.sh.pass1` is named above as it was during the run and is not shipped with this folder; NOTES.md, "Generators and checkers used and not shipped", says what stands in for it.
