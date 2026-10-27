# PROGRESS (piece uc4: UC Regulations 2013, Part 5, Part 8, Schedules 6-9, 11, 12)

Written as I go; after any compaction re-read this file, NOTES.md and the brief
(`../../../BRIEF.md` from this folder is `ucr/uc4/BRIEF.md`) and the text, not a summary.

## Working method

- Generator + templates live OUTSIDE the deposit, in the session scratchpad `uc4-work/` (`src/*.l4t` templates, `build.py`, `gen.py`, `verify.sh`, `diag.sh`, `notes_cov.py`, `assemble_notes.py`).
  The deposit holds only generated `.l4` and the two notes files.
  `build.py` expands `%%Q a-b` into mechanical quote lines (same normalisation as `srcrefs.py quote`), `%%QR` (quote plus locator), `%%R` (locator only; refuses lines not quoted above it in the same file) and `%%GEN` (generators for Sch 6/7 tables and for test fixtures).
- Run: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` and `python3 -I srcrefs.py check --refs <txt> uc4-*.l4`.
- `verify.sh` also compares `#ASSERT` lines written with assertions satisfied in each test file.
- Unique names: rules `reg N(...) — ...` / `Sch N para ... — ...`; types specific to provision.
- The coverage table in NOTES.md is generated from the source's structure plus the `@ref` locators in the modules, so its `where` column cannot drift from the code.

## Module plan (layer 1)

| module | provisions | state |
| --- | --- | --- |
| uc4-sch6-descriptors.l4 | Sch 6 (generated) | done, tested (uc4-tests-sch6.l4) |
| uc4-sch7-descriptors.l4 | Sch 7 (generated), diagnosis fields for reg 40A(3) | done, tested (uc4-tests-part5-capability.l4) |
| uc4-sch8-sch9-treated.l4 | Sch 8, Sch 9, regs 39(6)-(7), 40(5)-(6) | done, tested |
| uc4-part5-capability.l4 | regs 38, 39, 40, 40A | done, tested |
| uc4-part5-assessment.l4 | regs 41-44 | done, tested; 41(3) now rounds to the penny (F-41-1 reversed) |
| uc4-part8-ch1-carers-hours.l4 | regs 84-88 | done, tested |
| uc4-part8-ch1-groups.l4 | regs 89-92 | done, tested |
| uc4-part8-ch1-requirements.l4 | regs 93-98 | done, tested |
| uc4-part8-ch1-no-requirements.l4 | reg 99 | done, tested |
| uc4-part8-ch2-reduction-periods.l4 | regs 100-105 | done, tested |
| uc4-part8-ch2-reduction-effect.l4 | regs 106-111 | done, tested |
| uc4-part8-ch2-miscellaneous.l4 | regs 112-114 | done, tested |
| uc4-sch11-sanctions.l4, uc4-sch12-omitted.l4 | Sch 11, Sch 12 | done, tested (uc4-tests-sch11-sch12.l4) |
| uc4-part8-ch3-hardship.l4 | regs 115-119, signature line | done, tested |
| uc4-seat.l4 | layer 2: the seat's questions | done: 68 questions under one `§` and ten `§§` headings, each with `@export` and `@desc`; calls the layer-1 rules without restating them |
| uc4-cases-seat.l4 | layer 2: worked cases | done: 511 assertions over all 68 questions, expected values worked out from the text with the reasoning in a `-- Qn.` comment; includes asserted not-covered (`NOTHING`) cases |
| NOTES.md | all ten required headings | assembled from pieces: seat (68-question table, conventions, simplifications), jural relations (Part 5, Part 8, Sch 11, Sch 12), coverage table (254 rows, 0 problems), fork register (51 rows), cross-references (36), needs from the core (4), findings (24), binary notes (9), check.sh output, before-relying list |

## Decisions taken (with the provision that licenses each)

- F-points: the Sch 6 points cells are concatenated digits ("159960"); decoded by the unique non-increasing split ending in 0 (the descriptors are listed highest-first).
- F-sch7-1: one diagnosis (professional, qualification, NHS services) is taken to cover every descriptor in the diagnosed lists, reg 40A(3).
- Reg 40(2)(c) "not reasonable to require" is a BOOLEAN input (the text does not name who judges it).
- Reg 39(2) "some specific disease or bodily or mental disablement" is a BOOLEAN input.
- F-sch8-2: Sch 8 para 2(2) (residential rehabilitation programme) read as not subject to para 2(3) (24-hour advice).
- F-sch9-1: Sch 9 para 3 Secretary of State satisfaction qualifies all three limbs.
- F-41-1 reversed: a threshold computed from an hourly rate is an "amount for the purposes of these Regulations", so regulation 6(1) rounds it to the penny. Applied in 41(3), 109(1)(b)(ia), 118, 119(2)(c). Regulations 90 and 99(6) truncate to the pound by 6(1A).
- Sanction tables (regs 102 to 104): "within 365 days beginning with the date of the current failure" is read backward (F-102-1); a "–" cell is NOTHING.
- Reg 111: the 40% rate is taken of the unrounded amount of paragraph (1) and rounded once (F-111-1).
- Part 8 and Schedule 11 decisions are in the fork register of NOTES.md (F-86-1 to F-sch11-1, 38 rows), each with the text that licenses it; the ones that change a result most: F-102-1 (backward reading of the 365 and 14 day stretches), F-102-3 and F-110-2 (negative and below-nothing results are kept, not floored), F-111-1 (40% of the unrounded amount), F-109-1 (each route in its own case, every month must reach the amount).
- Layer 2: where the text gives no answer the question returns `NOTHING` or a constructor and a case asserts it (questions 11, 13, 25, 39 to 41, 45 to 49, 54, 55, 62 and 63 each assert at least one).

## Out-of-range comments

The brief asks for `-- out of range: section N (piece X)` above the input that stands for a provision outside my ranges.
84 such comments were added to the layer-1 modules after the first draft of the modules, by one script over the templates, from a table of patterns on the input lines; each names the provision, its piece where the table of pieces names one, and says the fact is a stated input.
The seat's own inputs carry no such comment: they repeat, in the person's words, the layer-1 inputs that do.

## Files written

check.sh, srcrefs.py and uc-core*.l4 were already here (not mine).
Mine: every `uc4-*.l4` in this folder (the fifteen layer-1 modules above, thirteen `uc4-tests-*.l4`, `uc4-seat.l4` and `uc4-cases-seat.l4`), PROGRESS.md and NOTES.md.
The generators that produced the Schedule 6 and 7 modules, the quotation lines, the seat and the cases are not here: they are in a scratch directory outside this folder (`uc4-work/`), which was a departure from "write files only under DEPOSIT" and is disclosed in the final report.

## Peeked

Nothing. No other piece's folder, no ~/.claude/, no existing encoding.
