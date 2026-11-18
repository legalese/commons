# PROGRESS (disk memory for a context that may be compacted)

Run dst-bgg3: BGG chapter 3 (Art. 72 to 89), German text, L4 on the stable binary 1.6.110.
After any compaction: re-read this file, NOTES.md, BRIEF.md and the text, not a summary.

## How the files are produced

- Work area (not deposited): `../../work/` beside `deposit/` (`work/src/*.l4.in` templates, `work/expand.py`, `work/build.sh`, `work/chk.sh`).
- `{{cite LABEL | RANGES}}` in a template expands to `-- src:N | text` lines copied by `srcrefs.py quote` from the raw text, then one `@ref`.
  So every quotation is copied mechanically from the text file, and every locator is the line range quoted.
- Rebuild: `work/build.sh` (writes the .l4 files into this folder). Check one file: `work/chk.sh bgg3-xxx.l4`.
- The test file `bgg3-tests-public-scope.l4` is written by `work/gen_tests_scope.py` (fixture records only) from `work/tests-scope-body.txt` (hand-written assertions).
- The case file `bgg3-cases-seat.l4` is written by `work/gen_cases_seat.py` (Art 83 argument lists only) from `work/cases-seat-body.txt` (hand-written cases).
- `quotecheck.py` (deposited) checks that every quoted German fragment in a `--` comment is in the text.

## Design decisions (licence in brackets)

- Every layer-1 decision function answers `MAYBE BOOLEAN`: JUST TRUE / JUST FALSE / NOTHING (brief: the rule of 2026-10-29).
- One function per provision unit; composites per Article follow the text's own chapeau (E1 option C: per-section answers, no gathering across sections).
- Plain GIVEN parameters in layer 1 (no records, except `Art 83 facts`); the seat builds `Art 83 facts` from plain inputs.
- Borrowed facts (terms the chapter does not define, and other Acts' articles) are BOOLEAN or NUMBER inputs.
- Art 83 is a list of bars: each limb answers JUST FALSE where it bars, NOTHING otherwise (JUST TRUE only for limb (m)); a dispatcher over `Art 83 kind of decision` picks the limb.
- The seat asks Art 83 the other way round ("is my decision excluded?"): it swaps JUST TRUE and JUST FALSE and keeps NOTHING (seat layer only).

## Sections done / in progress / next

- [done] bgg3-nouns.l4
- [done] bgg3-civil.l4 (Art 72-77) + bgg3-tests-civil.l4 (150 asserted, 2 traces)
- [done] bgg3-criminal.l4 (Art 78-81) + bgg3-tests-criminal.l4 (74 asserted, 2 traces)
- [done] bgg3-public-scope.l4 (Art 82-83) + bgg3-tests-public-scope.l4 (199 asserted)
- [done] bgg3-public-limits.l4 (Art 84, 84a, 85) + bgg3-tests-public-limits.l4 (39 asserted)
- [done] bgg3-public-courts.l4 (Art 86-89) + bgg3-tests-public-courts.l4 (73 asserted, 6 traces)
- [done] bgg3-seat.l4 (33 questions) + bgg3-cases-seat.l4 (146 asserted)
- [done] check.sh over all 13 modules, both stable builds: 681 satisfied, 0 failed
- [done] quote check: every German fragment quoted in a comment is in the text (quotecheck.py)
- [done] coverage.py + coverage-map.tsv (COVERAGE OK: 163 units, 226 non-blank lines, each in exactly one row)
- [done] NOTES.md (generated from work/NOTES.md.in by work/make-notes.py), encoding.json, SOURCE-LICENSE.md
- [done] final check.sh run (13 modules, 681 satisfied, 0 failed, same on 1.6.109); srcrefs 0 problems; quotecheck 0 missing
- [next] only the final report

## Files written

bgg3-nouns.l4, bgg3-civil.l4, bgg3-criminal.l4, bgg3-public-scope.l4, bgg3-public-limits.l4, bgg3-public-courts.l4,
bgg3-tests-civil.l4, bgg3-tests-criminal.l4, bgg3-tests-public-scope.l4, bgg3-tests-public-limits.l4, bgg3-tests-public-courts.l4,
bgg3-seat.l4, bgg3-cases-seat.l4, check.sh, fetch-main-l4.sh, srcrefs.py, quotecheck.py, coverage.py, coverage-map.tsv, NOTES.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md, PROGRESS.md.

## 2026-11-18: independent reader's follow-up

Seat questions for Art 73 and Art 79 re-worded and swapped (JUST TRUE = excluded); Art 86(2) re-worded only.
One case added (Art 79, last cantonal instance); two expected values changed (NOTES.md, Seat polarity).
Whole pass re-run: check.sh both builds, srcrefs --refs and --strict, quotecheck, coverage, NOT-precedence check.
