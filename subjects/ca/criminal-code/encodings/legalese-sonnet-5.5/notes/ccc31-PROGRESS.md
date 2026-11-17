# PROGRESS.md -- part ccc31 (Criminal Code (Canada), lines 18464-19055: Forms 24 to 54 and the heading RELATED PROVISIONS)

Read this first after any compaction. Then read NOTES.md and the text (`inputs/R.S.C.-1985-c.-C-46.txt`, lines 18464-19055), not a summary.

## Paths

- DEPOSIT (this folder): `.../runs/dst-ccc31/deposit/encodings/legalese-sonnet-5.5/`
- work dir (not shipped): `.../runs/dst-ccc31/work/` -- `coverage.py` (the coverage table, one row per unit; `python3 -I coverage.py [--names] [--table]` checks that every non-blank line of 18464-19055 is in exactly one row and lists the L4 names still to define), `build.py` (expands `--QUOTE N[-M]` macros in `work/src/*.l4.in` into the deposit `.l4` files by calling `srcrefs.py quote`), `notes/` (the pieces of NOTES.md, joined by `build-notes.py`), `baseline.txt` (what check.sh printed on the untouched folder), `probe/` (probes).
- binary: L4_BIN = `<scratchpad>/bin/l4-main-110` (1.6.110); L4_MAIN = `<scratchpad>/bin/l4-main-109` (1.6.109).

## Baseline (before any ccc31 file)

check.sh on the keel's three files (ccc-core, ccc-definitions, ccc-interpretation): 0 errors, 0 assertions on both builds, status same. Saved at `work/baseline.txt`.

## Decisions taken

- PLAN.md's "sections 1 to 9 (38 section headings)" for ccc31 is the keel's heading scan reading the forms' internal paragraphs ("1 You must report ...") as sections. They are not sections; the range is Forms 24-54 and the heading RELATED PROVISIONS (the brief governs; recorded in NOTES.md). Names are labelled `form N ...` (not `s N ...`) because `s 1` etc. belong to the keel and the cited sections (550, 708, 827 ...) belong to other parts.
- Seat questions begin "Under Form N," or "Under Form N paragraph M," (an extension of the brief's "Under schedule N paragraph M," to a Form; NOTES.md records the departure).
- A Form is encoded only where its text states a command, authorization, condition, period, right, prohibition or consequence. Captions, recitals that only identify, dates, signatures, seals, boxes for the declarant's wishes, and certificates/records are inert (reason 2). Recitals that are the stated grounds of a command are premises of the command's function.
- A failed premise ("Whereas ... This is therefore") answers NOTHING (limited by its own wording); a failed "if/while/unless/period" answers JUST FALSE; a bare "must" not done answers JUST FALSE for "the duty is met" (fork F5).
- A #TRACE cannot be asserted on the stable binary (tested: `#ASSERT <rule> EQUALS FULFILLED` is "could not be evaluated"; `#ASSERT (<rule> AT 0 WITH ...)` is a parse error), so each regulative rule is run with #TRACE and its duty is also a decision function, which carries the assertions.
- Trace output is the same on 1.6.110 and 1.6.109: the three test files that hold the 20 traces were run on both builds and the whole output diffed (identical). (An earlier note here, that 109 omits the `BY` line of a BREACH, was wrong: it came from a grep pattern that hid the line.)

## State at the end of the run (2026-11-13)

COMPLETE. Everything below was run in this session; the numbers are in NOTES.md ("What `check.sh` printed") and were produced by the commands named there.

- Coverage: 323 rows over 551 non-blank lines (158 encoded, 32 fork, 44 inert reason 1, 88 inert reason 2, 1 repealed); every line in exactly one row; every L4 name a row cites is defined and exercised (`work/coverage.py --names`, `work/check-asserted.py`).
- Layer 1 (6 modules): ccc31-forms-periods, -custody (Forms 24, 25, 26, 27, 30, 35, 39, 49, 50), -process (28, 29, 29.1, 32, 34, 40, 41), -statements (34.1, 34.2, 34.3, 48.2), -orders (46, 47, 48, 48.1, 51), -soira (52, 53, 54).
- Tests (6 files): ccc31-tests-periods, -custody, -process, -statements, -orders, -soira.
- Layer 2: ccc31-seat.l4 (56 questions, 7 groups) and ccc31-cases-seat.l4 (232 cases).
- check.sh: 16 modules, 0 errors, 760 assertions satisfied after tests-periods was added (see check-final in NOTES.md), identical counts on 1.6.110 and 1.6.109; a negative control turned it red.
- srcrefs `--refs` and `--strict`: 0 problems. verify-quotes: 0 problems. No Warning or Error severity on either build.
- NOTES.md has every required heading; NEEDS-CORE.md lists the constructors wanted.

## How to rebuild (the work dir is not shipped)

- `python3 -I work/build.py <module>` expands `--QUOTE` macros of `work/src/<module>.l4.in` into the deposit file; the statements and SOIRA modules, their tests, the seat and the seat cases are written by `work/gen-*.py`; NOTES.md is assembled by `work/build-notes.py` from `work/notes/*.md`, `work/coverage.py` and the saved outputs of the checks.
