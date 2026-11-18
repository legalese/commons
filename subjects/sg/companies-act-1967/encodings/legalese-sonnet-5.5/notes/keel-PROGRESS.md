# PROGRESS (keel agent, Companies Act 1967 Singapore)

Written as I go so a compaction loses nothing. Re-read this, NOTES.md and the text after any compaction, not a summary.
State at the last update (2026-11-18): every deliverable is written and every gate is green; the keel is finished.

## Method (do not lose this)
- RUN = `<scratchpad>/runs/dst-sg-k`.
- The sources of the `.l4` modules are in `RUN/work/src/*.l4` with macros (`@@REF A B citation`, `@@AGAIN`, `@@QUOTE`, `@@REFALL`); `python3 RUN/work/build.py [names]` expands them into this folder (quote lines are copied mechanically from `inputs/CoA1967.txt`).
  EDIT THE SOURCES in `work/src`, then run build.py; never edit a generated `.l4` here that has a source.
- Generated upstream of `work/src`: `sg-definitions(.l4|-tests.l4)` by `work/gen_defs.py` (tables in gen_defs.py, `defs_hand.py`, `defs_header*.l4`, then build.py); `sg-seat-keel.l4` and `sg-cases-seat-keel.l4` by `work/gen_seat.py` (writes straight into this folder).
- Documents are generators too, so a count or a line number cannot drift: `PLAN.md` by `work/gen_plan.py`; `NOTES.md` by `work/gen_notes.py` (reads `work/coverage.py`, `work/scan_kinds.py`, the Guide, the earlier pass, `work/scratch/check.out` and `work/scratch/gates.out`).
  Run order at the end: edit, build, `check.sh` (capture to `work/scratch/check.out`), srcrefs, `coverage.py`, `traces.py`, then `gen_notes.py` last.
- Quick check of one file: `python3 RUN/work/q.py FILE [--evals]` (build 110).
- Full check: `L4=<bin>/l4-main-110 L4_MAIN=<bin>/l4-main-109 ./check.sh` in this folder.
- srcrefs: `python3 -I srcrefs.py check --strict RAW sg-*.l4` and `--refs`, RAW = absolute path of `inputs/CoA1967.txt`.
- Traces: `python3 RUN/work/traces.py` runs every `#TRACE` of the solvency and auditors tests on both builds against `-- EXPECT`.
- Compiler traps (each re-probed on 2026-11-18; the probe files are in `work/scratch/probe`): `NOT a AND b` is `NOT (a AND b)`; `length` does not exist (use `count`); `JUST x's f` must be `JUST (x's f)`; a vertical `LIST` has no commas; a continuation line starting with `(` at a smaller indent than its function is `parse/unexpected-open-paren`; `DECIDE name IF` needs a `BOOLEAN`.
  Two traps I had written down before were NOT confirmed by a probe and are no longer claimed: a comma-separated field list on one line checks fine, and an unused parameter is not rejected.

## Done (all green: check.sh 17 modules, 974 assertions satisfied, 0 failed, same on 109 and 110)
- `sg-core.l4` (116 lines); `sg-periods` + tests (70); `sg-groups` + tests (93); `sg-interests` + tests (76); `sg-solvency` + tests (48, 7 traces); `sg-auditors` + tests (32, 5 traces); `sg-definitions` + tests (399; 92 s 4(1) terms and s 4(2)); `sg-interpretation` + tests (81: s 4(1) opening words, (3) to (5A), (7) to (13)); `sg-seat-keel` + `sg-cases-seat-keel` (37 questions, 175 cases).
- `PLAN.md` (8 numbered sections) and `NOTES.md` (all sections the brief lists, 235 coverage rows: 169 encoded, 39 fork, 23 inert, 4 repealed or blank; checked by script that every non-blank line of lines 1-2389 and 2736-2801 is in exactly one row).
- Gates: srcrefs strict and refs 0 problems (845 src lines, 142 runs, 169 locators); traces 12, mismatches 0; every NOT bracketed; no diagnostics and no layout warning on either build; three mutations in a scratch copy turned tests red (2, 10 and 2+8 failed assertions).

## Decisions taken (with licence)
- Definition functions return MAYBE BOOLEAN: `JUST FALSE` only for a "means" closure, a "does not include" or a flat negative; `NOTHING` for "includes" or silence (Guide lines 86 and 87).
- Failed "where" gates answer `JUST FALSE` (periods ruling of 2026-11-05, item (b)): s 6, s 4(10) and (11), s 10(5) and (6).
- A date fixed in the text's own words: `JUST FALSE` outside it (item (a)): s 4(13)(a)(i) and (b); the grant in s 4(13)(a)(ii) stays `NOTHING` (grant rule, limit 1).
- Periods convention (P1 to P9) is assumed, not ruled (the Interpretation Act 1965 is not a source).
- Fork ids: C (terms), D (s 4 outside the list), G (ss 5 to 7A), S (the four split-site entries), P (periods). F-D6 is s 4(10) and (11); F-C3 is the terms that take their meaning from another Act. There is no F-D1.
- Split sites: type (i) 3 sites (s 7A(6) `JUST FALSE`; s 10(1) and s 10(3) `NOTHING`); type (ii) 3 sites, all `NOTHING` (s 7A(4)(b), s 7A(5), s 4(13)(a)(ii)).
- s 4(10), (11): inputs are the number of directors and whether the only director did the act; no list of directors.
- The seat asks chains-of-control questions through limb facts, not link lists.

## Files
- `sg-core.l4`, `sg-periods(.l4|-tests.l4)`, `sg-groups(...)`, `sg-interests(...)`, `sg-solvency(...)`, `sg-auditors(...)`, `sg-definitions(...)`, `sg-interpretation(...)`, `sg-seat-keel.l4`, `sg-cases-seat-keel.l4`, `PLAN.md`, `NOTES.md`, `PROGRESS.md`; `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` were given.
