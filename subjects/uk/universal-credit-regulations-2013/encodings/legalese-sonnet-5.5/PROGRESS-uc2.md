# PROGRESS (uc2: Part 6, Part 7, Schedule 10 of the Universal Credit Regulations 2013)

Written by the piece agent `uc2`. Re-read this file and NOTES.md after any compaction, then the text (lines 845-1358 and 2814-2872 of ../../registers/source-bundle/uksi-2013-376.txt).

## State

- 2026-10-22: the encoding is finished. Layer 1 (nine modules, eight test files) and layer 2 (`uc2-seat.l4` with 130 questions, `uc2-cases-seat.l4` with 666 cases) are written.
- The last `check.sh` run (`L4_TARGET=unstable`, run alone, started after the last edit to any `.l4` file) printed 23 modules, 0 errors, 1510 satisfied, 0 failed, 0 refused, exit 0. NOTES.md `## What check.sh prints` has the exact output.
- `srcrefs.py check --refs` and `--strict` over all `uc2-*.l4`: 1410 src: lines, 303 runs, 285 locators, 0 problems.
- NOTES.md has its ten required headings, no leftover markers, and a coverage table of 250 rows (206 encoded, 30 inert, 11 repealed or blank in this text, 3 fork) for the 42 regulations, 27 Schedule 10 paragraphs and 14 headings of my ranges. A script confirms no non-blank line of the 573 in my ranges is left without a row.
- What is left: the last advisor call and the report to the team lead.

## Corrections made late (so a later reader does not trust an older note)

- An earlier note of mine said `references/source-patterns/` was absent from the skills copy. It is present. NOTES.md says which entries I read and that the rest were not read.
- Four coverage rows first marked `inert` (reg 55(1), reg 57(1), reg 82(4), reg 82(5)) were moved to `encoded`: they state rules that the rule names or input names carry, and the brief's list of reasons for `inert` does not cover them.

## Peeked

- I read my own agent transcript (`~/.claude-work/projects/.../subagents/agent-at2-uc2-....jsonl`), which the context summary pointed me to, to recover details lost in a compaction. A directory listing there also showed the file names of other agents; I opened none of them.
- One recursive `grep` run from the folder above the pieces printed lines from other pieces' files (`cbca/cb1` to `cb4` `BRIEF.md` line 23, a table row naming the pieces of another encoding, and a comment line of `br6404/br3/work/srcrefs.py`). It was a mistake in how I scoped the command. Nothing from it was used.
- `ps` and `lsof`, while I was stopping my own stray processes, showed other pieces' process names and working directories (for example uc3's deposit folder and probe file names). No file contents.

## Plan (modules, one per Part/Chapter/natural group; all names start `uc2-`)

| module | provisions | status |
| --- | --- | --- |
| uc2-domain.l4 | shared records and helper (`uc2 helper — a provision is an enactment`) | DONE |
| uc2-part6-ch1-capital.l4 | regs 45-50 | DONE: tests uc2-tests-part6-ch1.l4 (50 assertions) |
| uc2-part6-ch2-earned-income.l4 | regs 51-56, 60, 61 | DONE: tests uc2-tests-part6-ch2-earned-income.l4 (88) |
| uc2-part6-ch2-self-employed.l4 | regs 57, 57A, 58, 59 | DONE: tests uc2-tests-part6-ch2-self-employed.l4 (80) |
| uc2-part6-ch2-surplus-and-floor.l4 | regs 54A, 62, 63, 64 | DONE: tests uc2-tests-part6-ch2-surplus-and-floor.l4 (80) |
| uc2-part6-ch3-unearned-income.l4 | regs 65-74 | DONE: tests uc2-tests-part6-ch3.l4 (158) |
| uc2-part6-ch4-misc.l4 | regs 75-77 | DONE: tests uc2-tests-part6-ch4-misc.l4 (94) |
| uc2-part7-benefit-cap.l4 | regs 78-83 | DONE: tests uc2-tests-part7-benefit-cap.l4 (141) |
| uc2-sch10-capital-disregards.l4 | Schedule 10 paras 1-24 (incl. 18ZA, 18ZB, 18A) | DONE: tests uc2-tests-sch10.l4 (153) |
| uc2-seat.l4 | layer 2: 130 questions with `@export` and `@desc` | DONE (generated; the generator is a helper in inputs/.work/seat, not a deliverable) |
| uc2-cases-seat.l4 | layer 2: worked cases, expected values hand-written | DONE: every question covered, true and false for every yes-or-no question |

## Decisions taken (with the provision that licenses each)

- Rule names: `reg N(x) — ...` / `Sch 10 para N — ...`, em dash U+2014, as the keel does.
- The two formulas lost in conversion (reg 54A(6) nil UC threshold; reg 73(2A) apportionment by days) are NOT reconstructed: the nil UC threshold is a stated input; reg 73(2A) returns NOTHING (not covered). See fork register F-A1, F-U1.
- Rounding: every final calculated amount through `core — an amount rounded to the nearest penny` (reg 6(1)); reg 82(1)(a) through `core — an amount with any fraction of a pound disregarded` (reg 6(1A)).
- Reg 2 definitions come from the keel: `reg 2 — paid work` (regs 52, 55(4A), 82(2)(b)), `reg 2 — local welfare provision` and `reg 2 — enactment` (Sch 10 paras 17, 18A), `reg 2 — close relative` (Sch 10 para 2), `reg 2 — local authority` (para 17).
- "partner" in reg 77 is the business sense (the keel excludes reg 77 from its definition); nothing is defined.
- Seat: one question per decision a claimant would ask; each calls the layer-1 rule and restates nothing; the simplifications are listed in NOTES.md under `## Seat`.
- The seat question on how much of a benefit counts as unearned income (reg 66(1)) calls the item-level rule, not the listed-benefit amount rule, so that a benefit not listed in reg 66(1)(b) counts for nothing (found and corrected while writing the cases).

## Files written

Layer 1: uc2-domain.l4, uc2-part6-ch1-capital.l4, uc2-part6-ch2-earned-income.l4, uc2-part6-ch2-self-employed.l4, uc2-part6-ch2-surplus-and-floor.l4, uc2-part6-ch3-unearned-income.l4, uc2-part6-ch4-misc.l4, uc2-part7-benefit-cap.l4, uc2-sch10-capital-disregards.l4.
Tests: uc2-tests-part6-ch1.l4, uc2-tests-part6-ch2-earned-income.l4, uc2-tests-part6-ch2-self-employed.l4, uc2-tests-part6-ch2-surplus-and-floor.l4, uc2-tests-part6-ch3.l4, uc2-tests-part6-ch4-misc.l4, uc2-tests-part7-benefit-cap.l4, uc2-tests-sch10.l4.
Layer 2: uc2-seat.l4, uc2-cases-seat.l4.
Report files: NOTES.md, PROGRESS.md.
Helper scripts (not deliverables) live in inputs/.work: expand.py (macro @@Q N M -> quote lines), run1.sh, notes_add.py, notes_fill.py, covcheck.py (coverage completeness), and the seat generator in inputs/.work/seat (seatlib.py, build_seat.py, build_cases.py, spec_*.py, cases_*.py).
