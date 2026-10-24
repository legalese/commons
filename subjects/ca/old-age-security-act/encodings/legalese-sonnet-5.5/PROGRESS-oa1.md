# Progress: piece oa1 (OAS Act: title and s 1, Part I, Part IV, Related Provisions, Amendments Not in Force)

Status line: COMPLETE for the brief, pending only the lead's decisions on the licence (STUB-SOURCE-LICENSE.md) and on the two inert rows flagged in NOTES.md. All layer-1 modules, their tests, the seat, the seat cases and NOTES.md are written; check.sh: 0 errors, 980 assertions satisfied over 34 modules, 0 failed, 0 refused; srcrefs.py check: 0 problems.
Peeked: nothing.

## How I work (so a compacted context can resume)

- Scratch (not deliverables) lives in `../../../work/` (that is `oa1/work/`): `tpl/<module>.l4.tpl` are the sources; a line `@@Q N M@@` in a template is replaced by `srcrefs.py quote` lines of the Act file; `python3 -I work/expand.py <module> ...` writes `deposit/encodings/legalese-sonnet-5.5/<module>.l4` (no argument writes them all). `work/chk.sh <file> ...` (file names relative to the deposit folder) runs files and prints errors, warnings and the satisfied count.
- The seat is generated: `python3 -I work/genseat.py` reads `work/seat/seat_a.py` to `seat_h.py` (question specs with hand-worked cases) and writes `oa1-seat.l4` and `oa1-cases-seat.l4`. Edit the specs, never the generated files.
- `work/mkrows.py` lists the `@ref` rules and the lines of the Act's ranges they do not cover; the coverage table in NOTES.md is built from it.
- Edit the `.tpl`, never the generated `.l4`.
- Names I declare begin with the provision label, as the keel asks: `s 3(1): ...`, `2010, c. 12, s. 1828: ...`. Helpers that belong to no provision begin `oa1: `. Test-file helpers begin `oa1 test: `.
- Tests are in `oa1-tests-*.l4`; expected values are worked by hand in the comment beside the assertion. A test that failed because I had worked the expected value wrongly was corrected on re-reading the text, not on the output (s 28.1(2)(c)(ii): an application in the month the person ceased to be incapable is in time).
- Fork numbers cited in comments are this piece's own, `OA1-F1` to `OA1-F24`, tabulated in NOTES.md; the keel's F5 (age attained) is cited as "the keel".

## Module plan

| module | provisions | state |
| --- | --- | --- |
| `oa1-helpers.l4` | the later and the earlier of two dates | done |
| `oa1-nouns.l4` | fact records for Part I | done |
| `oa1-part1-eligibility.l4` | ss 3(1), 3(2), 4, 4.1, 5(1), 5(2), 5(3), 5.1, 6 | done, tests 95 satisfied |
| `oa1-part1-waiver.l4` | ss 5(4) to 5(8) | done, tests 23 satisfied |
| `oa1-part1-amount.l4` | ss 3(3) to 3(5), 7, 7.1 | done, tests 47 satisfied |
| `oa1-part1-payment.l4` | ss 8, 9, 9.1, 9.2, 9.3 | done, tests 77 satisfied |
| `oa1-part4-applications.l4` | ss 26.1, 26.2, 28.1, 29, 30, 31, 32 | done, tests 61 satisfied |
| `oa1-part4-appeals.l4` | ss 27, 27.1, 28 | done, tests 39 satisfied |
| `oa1-part4-information.l4` | ss 33, 33.1, 35, 35.1 (34, 34.2 are inert) | done, tests 31 satisfied |
| `oa1-part4-recovery.l4` | ss 36, 37 | done, tests 53 satisfied |
| `oa1-part4-offences.l4` | ss 44, 44.1 | done, tests 51 satisfied |
| `oa1-part4-administration.l4` | ss 38 to 43, 45 to 47 (40(2) and 42(3) to (6) inert) | done, tests 58 satisfied |
| `oa1-part4-inspections.l4` | s 44.2 | done, tests 64 satisfied |
| `oa1-related.l4` | Related Provisions (s 1830 and the amendments not in force are inert rows) | done, tests 19 satisfied |
| `oa1-seat.l4`, `oa1-cases-seat.l4` | layer 2: 131 questions, 362 case assertions | done, 362 satisfied |

## Decisions taken (with the provision that licenses each)

See NOTES.md, "Fork register" (OA1-F1 to OA1-F23) and "What the text turns out to say".

## Files written

See the table above; every layer-1 `.l4` is generated from `work/tpl/<name>.l4.tpl`, and the seat files from `work/genseat.py`.

## Still to do

Nothing in the brief. If the lead rules on the licence or on the two inert rows outside the brief's list (s 33(2), 2010 c. 12 s 1830), the coverage rows in NOTES.md change; regenerate them with `work/mkrows.py`, `work/mkcov.py` and `work/assemble.py` (NOTES.md is assembled from `work/notes/part_*.md`, `coverage.md`, `jural.md` and `xref.md`; edit those, not NOTES.md).
To re-verify: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (several minutes; the seat cases are the slow file), then `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/R.S.C.-1985-c.-O-9.txt oa1-*.l4`.
