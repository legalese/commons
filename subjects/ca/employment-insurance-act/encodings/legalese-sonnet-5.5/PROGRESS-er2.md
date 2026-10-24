# PROGRESS: piece er2 (Regulations 19 to 34, lines 340 to 539 of SOR-96-332.txt)

Agent: er2 (Sonnet 5.5). Started and finished 2026-10-24. Binary: l4 1.6.98 (main), run as `L4=<bin> L4_TARGET=unstable ./check.sh`.
After a compaction: re-read this file, NOTES.md and the text (`sed -n '340,539p' SOR-96-332.txt` in chunks); do not trust a summary.

HOW THE FILES ARE MADE. The layer-1 modules are generated from templates with `@@Q N [M]` marker lines (and `@@TABLE5`, `@@TABLE7` for the two
tables of reg 34) by a small script that calls `srcrefs.py quote` and reads the raw file, so the quotation is copied and never typed. The templates
and the script are scratch (`<scratchpad>/er2-probes/templates/` and `<scratchpad>/er2-probes/gen.py`; NOTES.md is built by
`<scratchpad>/er2-probes/build_notes.py` from `notes_prose.md` and `notes_skeleton.md`). They are not part of the deposit. Edit a template, not a generated
module, then run `python3 gen.py <template name>`. Test files and the seat files are written directly into this folder.
`<scratchpad>` is a scratch folder outside this folder (not committed)

## Status: all deliverables written and checked

| file | regs | status |
| --- | --- | --- |
| `er2-common.l4` | helpers (later of two days, days two periods share ...) | done; tested inside `er2-tests-allocation.l4` |
| `er2-record-of-employment.l4` | 19 to 21 | done; tests 58 satisfied |
| `er2-allocation.l4` | 22 to 24.3 | done; tests 118 satisfied |
| `er2-claims.l4` | 25 to 28 | done; tests 129 satisfied |
| `er2-full-working-week.l4` | 29 to 32 | done; tests 95 satisfied |
| `er2-teachers.l4` | 33 | done; tests 34 satisfied |
| `er2-family-supplement.l4` | 34 | done; tests 64 satisfied |
| `er2-seat.l4` | layer 2 | done; 61 `@export` questions, every input with an `@desc` (checked by script) |
| `er2-cases-seat.l4` | layer 2 cases | done; 162 satisfied; every question has at least one case |
| `NOTES.md` | all ten headings; 156 coverage rows (106 encoded, 29 fork, 19 inert headings, 2 repealed); 24 forks | done |

Last check.sh: TOTAL (19 modules) errors 0, satisfied 660, failed 0, refused 0. `srcrefs.py check --refs` on all `er2-*.l4`: 163 src lines, 71 runs, 131 locators, 0 problems.
`l4 check` on each er2 file: no warning, no error, no annotation note.

## Decisions taken (and the text that licenses each)

- Deadlines are DATE-valued rules plus BOOLEAN "in time" rules, not DEONTIC: `check.sh` cannot count a `#TRACE` outcome.
- Counting convention for "within n days after d": the keel's fork F4 (the last day is d + n and counts).
- Rules for "may"/"shall" with an official as subject (reg 28, 19(6), 27) answer what the person is owed or exposed to.
- The brief's `inert` list is closed: deemings, definitions and reading rules are encoded; only the 19 headings (division titles) are inert, and the two repealed regs (24.2, 34(2.1)) are repealed-or-blank rows.
- `(NOT (x) OR y)` parses as `NOT (x OR y)` on the stable binary: every NOT that meets AND/OR is wrapped as `((NOT (x)) OR y)` (found by a failing test of reg 27(6)).
- Not-covered values are NOTHING / MAYBE, asserted: reg 22 outside "partially within", reg 23(3) with nothing left to allocate over, reg 26.1(1) for benefits it does not name, reg 30 when (1) does not describe the work, reg 31 for a claimant of reg 29 or 30, reg 34 for an income with cents or above $25,921 and a benefit period before 1997.
- Forks F1 to F24 are in NOTES.md `## Fork register`.

## Files written (this folder)

er2-common, er2-record-of-employment, er2-allocation, er2-claims, er2-full-working-week, er2-teachers, er2-family-supplement (.l4);
er2-tests-record-of-employment, er2-tests-allocation (also tests er2-common), er2-tests-claims, er2-tests-full-working-week, er2-tests-teachers,
er2-tests-family-supplement (.l4); er2-seat.l4, er2-cases-seat.l4; NOTES.md; PROGRESS.md.
`check.sh`, `srcrefs.py` and the keel's `eia-core*.l4` are the lead's, unchanged. No git add, commit or push was done.
