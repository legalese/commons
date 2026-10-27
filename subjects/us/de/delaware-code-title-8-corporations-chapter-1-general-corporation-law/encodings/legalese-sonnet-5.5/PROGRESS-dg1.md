# PROGRESS -- dg1 (title lines and Subchapter I, sections 101 to 116)

State: every deliverable is written and the last full check is recorded in `NOTES.md` under `## What check.sh prints`.
Nothing is in progress.

Paths (no shell variable survives a compaction, so they are written out).

- W = `a scratch folder outside this folder (not committed: dg1)`
- INPUTS = `W/inputs`; DEPOSIT folder D = `W/deposit/encodings/legalese-sonnet-5.5`
- L4 = `l4`
- RAW = `W/../../registers/source-bundle/de-code-t8-ch1-2026-10-01.txt`, my lines 1-239, 220 of them non-blank
- Helpers that are not part of the deposit are in `W/inputs/work/`:
  `src/*.l4.src` are the layer-1 modules and the seat with quote directives (`@@Q`, `@@REC`); `gen.py` expands them into D, so a change is made in the `.src` and never in the generated `.l4`.
  `chk.sh` expands, runs `check.sh`, `srcrefs.py` and a grep for warnings.
  `build_notes.py` assembles `NOTES.md` from `work/notes/` (the coverage table is `work/notes/coverage.tsv`).
  `dupnames.py` lists names defined in more than one file; `pairs.py` lists same-typed seat inputs that no case gives different values.
  `make_progress.py` wrote this file from the check output.
  `mutation/` holds the mutation harness and its results.
- The test files and the cases are written directly in D, with no quote lines.

## Files in D

| layer-1 module | sections | tests | result of the last check |
| --- | --- | --- | --- |
| `dg1-s101-formation.l4` | 101, 104, 105, 106, 107 | `dg1-tests-s101-formation.l4` | 57 satisfied, 0 failed, 0 errors |
| `dg1-s102a-required-contents.l4` | 102(a) | `dg1-tests-s102a-required-contents.l4` | 103 satisfied, 0 failed, 0 errors |
| `dg1-s102b-optional-provisions.l4` | 102(b), (c), (d), (f) | `dg1-tests-s102b-optional-provisions.l4` | 97 satisfied, 0 failed, 0 errors |
| `dg1-s102e-name-reservation.l4` | 102(e) | `dg1-tests-s102e-name-reservation.l4` | 41 satisfied, 0 failed, 0 errors |
| `dg1-s103-filing.l4` | 103 | `dg1-tests-s103-filing.l4` | 168 satisfied, 0 failed, 0 errors |
| `dg1-s108-organization.l4` | 108 | `dg1-tests-s108-organization.l4` | 55 satisfied, 0 failed, 0 errors |
| `dg1-s109-bylaws-and-emergency-powers.l4` | 109, 110, 112, 113 | `dg1-tests-s109-bylaws-and-emergency-powers.l4` | 127 satisfied, 0 failed, 0 errors |
| `dg1-s111-s115-jurisdiction-and-forum.l4` | 111, 115 | `dg1-tests-s111-s115-jurisdiction-and-forum.l4` | 35 satisfied, 0 failed, 0 errors |
| `dg1-s114-nonstock.l4` | 114 | `dg1-tests-s114-nonstock.l4` | 94 satisfied, 0 failed, 0 errors |
| `dg1-s116-documents.l4` | 116 | `dg1-tests-s116-documents.l4` | 48 satisfied, 0 failed, 0 errors |

- `dg1-seat.l4`: the seat, 147 questions with `@export` and `@desc`; check: 0 errors.
- `dg1-cases-seat.l4`: 507 assertions satisfied, 0 failed, 0 errors; at least one case for each of the 147 questions.
- `dg1-cases-seat-first-reading.l4`: one assertion that is meant to fail (the author's first reading of section 110(i), F32); `check.sh` lists it in `expected_failed` with the count 1; check: 1 errors, 1 failed, expected 1.
- TOTAL: 24 modules, 1 errors, 1332 satisfied, 1 failed, 0 refused; the one error and the one failed are that registered assertion, and `check.sh` exits 0.
- `NOTES.md` (written by `build_notes.py` from the parts in `work/notes/`) and this file.
- `srcrefs.py` and `dg-core.l4` were in D at the start and are unchanged; `check.sh` has one line added, in `expected_failed`.

## Decisions (each is recorded with its licence in `NOTES.md`)

- The keel recommends no seat layer and an `inert` row for the "facts" sentence of section 102(d); the brief wins on both: the seat is written and section 102(d) is encoded (`NOTES.md`, F18).
- The coverage table has one row for every heading, every provision and every History line; the readings are the 32 entries F1 to F32 of the fork register; a row whose rule carries a recorded reading is marked `fork`.
- Dates are carried as dates; the time of day is not (F6); "business days" is an input (F15).
- Hohfeld correlatives are recorded in `NOTES.md` (`## Jural relations`) and not as second rules.
- Out-of-range rules are plain inputs with a comment `-- out of range: section N (piece X)`; the list is `## Cross-references out of my ranges`.
- Officials' judgments (waivers, findings, the court's sanction) are inputs.

## What changed after the first complete version

- Six constructor names that were defined in two files (one of them also in the core) were renamed after `inputs/work/dupnames.py` found them; `check.sh` had printed 0 errors throughout.
- Fifteen seat question names with no distinctive noun were given an "Under section ..." prefix.
- 104 cases were added to the seat (one fact varied at a time), and one layer-1 test; one of the new cases failed when first run and became fork F32.
- The first expectation of the F32 case is kept in `dg1-cases-seat-first-reading.l4`, registered in `check.sh`, as the brief says to keep an expectation meant to fail.
- Fork numbering: F1 to F32, and seven rows of the coverage table were changed to `fork` to match the register.
- The seat header no longer says records are built positionally (they are built with `WITH`).

## Still to do

Nothing in this piece.
The report to the lead is the last message.
