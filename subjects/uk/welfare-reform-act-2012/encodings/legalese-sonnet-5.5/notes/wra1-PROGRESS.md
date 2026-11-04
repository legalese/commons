# PROGRESS (wra1): the Welfare Reform Act 2012 (United Kingdom), ranges 2-517, 2630-2922, 3050-3173

Status at each update is by running the files, not by memory.
Last updated 2026-11-04: complete; waiting only for the lead.

## How the work is built (read this first after a compaction)

- Sources are authored in `../../../work/src/*.l4` (relative to this folder: `runs/iaw-wra1/work/src`), with markers `@@REF label N M` (expands to quote lines from `srcrefs.py quote` plus `@ref label (src:N-M)`), `@@AREF` (ref only) and `@@Q` (quote only).
  `build.py` drops a quote line that is only dots (srcrefs rejects it as "no text"); the locator still spans it.
- `python3 work/build.py` writes the deposit `.l4` files; `work/r.sh FILE...` builds, runs with the stable binary and prints counts and diagnostics.
- NOTES.md is assembled by `work/make_notes.py` from `work/notes/*.md` and four generated tables (`coverage.py table`, `make_jural.py`, `marginal.py`, `seatlist.py`); edit the pieces and re-run it, not the NOTES.md.
- Coverage rows are in `work/coverage.tsv` and `work/coverage-b.tsv` (the latter written by `work/make_coverage_b.py`); `work/coverage.py check` proves every non-blank line of the three ranges is in exactly one row.
- Principle P1: a regulation-supplied value enters as MAYBE (NOTHING in gives NOTHING out). Class E (an exception power: s 4(2), s 6(3), s 9(3), s 10(4), s 11(5)(a)) makes a "no" provisional (NOTHING unless the exception input is JUST FALSE); class D (deeming or specifying regulations: s 4(5)-(7), s 39(3), s 24(6), Sch 1 para 5, 7, 8) overrides only when supplied (JUST x), and with NOTHING the Act's own words apply.
- Names: every top-level name begins with the provision label (`s 4(1)(a) ...`, `sch 6 para 5(4) ...`), including types and constructors. Schedule 2 has no derived paragraph numbers: its labels are `sch 2 <host Act> <host provision>`.

## Done (compiled and tested on the stable binary and the main build; assertions satisfied / asserted)

- wra1-three-valued + tests: 19/19
- wra1-ch3-general (ss 30-43) + tests: 103/103
- wra1-ch1-entitlement (ss 1-12) + tests: 171/171
- wra1-ch2-responsibilities (ss 13-29) + tests: 335/335 and 11 #TRACE runs (the stable binary prints a #TRACE outcome and cannot assert it; each duty has a decision-function twin that is asserted)
- wra1-sch1 (Schedule 1) + tests: 48/48
- wra1-sch2 (Schedule 2) + tests: 116/116
- wra1-sch5-6 (Schedules 5, 6) + tests: 110/110
- wra1-seat (48 exported questions) + wra1-cases-seat: 199/199
- check.sh with both binaries: TOTAL (18 modules) 1101 satisfied, 0 errors, 0 failed, 0 refused, every row "same" (keel baseline: 3 modules, 38 satisfied)
- srcrefs `--refs` and `--strict` over all wra1 files: 0 problems
- coverage.py check: 933 non-blank lines, all covered once, 431 rows, 0 problems; audit.py: 189 FALSE/NOTHING branches, 0 without a kind comment
- NOTES.md: Coverage, Fork register, Reading a result, Jural relations, Marginal readings, Seams, seat, findings, what the stable binary does not accept, check.sh output, peeked

## Next

Nothing for wra1. The final report is the last message of the run.
