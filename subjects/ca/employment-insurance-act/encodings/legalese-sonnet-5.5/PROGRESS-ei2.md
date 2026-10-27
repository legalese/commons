# PROGRESS: piece ei2 (Act lines 670-1126)

Last updated when the work reached the state below. After any compaction re-read this file, NOTES.md and the text, not a summary.
Build tooling is in `INPUTS_DIR/_work/` (templates `src/*.l4.in` with `@@Q N M` quote lines and `@@S N` string lines expanded from the raw Act by `gen.py`; `r.sh` runs one file; `mkcases.py` builds the cases file from a hand-written table; `assemble.sh` builds NOTES.md from `notes/*.md`; `seat/*.l4` are the chunks that make `ei2-seat.l4`). Edit those, not the generated files. The `.l4` files in this folder stand alone: the templates and scripts are build scaffolding that will not exist after the merge, and nothing in a `.l4` file depends on them.

## State

All deliverables are written and `check.sh` is green. Nothing was added to git.

| step | state |
| --- | --- |
| `ei2-nouns.l4` | done |
| `ei2-s23-3-division.l4` + tests (s 23.3(6) to (9)) | done |
| `ei2-work-sharing-and-courses.l4` + tests (ss 24 to 26) | done |
| `ei2-disqualification.l4` + tests (ss 27, 28) | done |
| `ei2-leaving-and-misconduct.l4` + tests (ss 29 to 35) | done |
| `ei2-labour-disputes-and-absence.l4` + tests (ss 36, 37) | done |
| `ei2-penalties.l4` + tests (ss 38 to 41.1) | done |
| `ei2-repayment.l4` + tests (ss 42 to 47) | done |
| `ei2-claim-procedure.l4` + tests (ss 48 to 53) | done |
| `ei2-hours-methods.l4` + tests (s 55(2) to (4); s 54 and s 55(1) inert in the coverage table) | done |
| `ei2-employment-support.l4` + tests (Part II, ss 56 to 65.2) | done |
| `ei2-seat.l4` (101 questions) and `ei2-cases-seat.l4` (296 assertions) | done |
| NOTES.md (all ten headings) | done |
| `check.sh` | 882 satisfied, 0 failed, 0 refused, 0 errors (586 in the ten test files, 296 in the cases file) |
| `srcrefs.py check --refs` | 0 problems |

## Files written

`ei2-nouns.l4`, `ei2-s23-3-division.l4`, `ei2-work-sharing-and-courses.l4`, `ei2-disqualification.l4`, `ei2-leaving-and-misconduct.l4`, `ei2-labour-disputes-and-absence.l4`, `ei2-penalties.l4`, `ei2-repayment.l4`, `ei2-claim-procedure.l4`, `ei2-hours-methods.l4`, `ei2-employment-support.l4`, `ei2-tests-<each rule module>.l4` (ten files), `ei2-seat.l4`, `ei2-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`.

## Decisions taken (with the section that licenses each)

- Deeming rules (ss 24(3), 25(1), 26, 28(6), 28(7), 35, 36(5), 42(1), 47(1), 49(2), 52(3)(a), 65.2(1)) and "no appeal" rules (ss 24(2), 25(2), 64) return MAYBE BOOLEAN: JUST TRUE when the provision applies, NOTHING when it does not, never FALSE (finding 1). The seat words the question so FALSE means "this provision does not apply".
- Judgments the Act leaves to someone (good cause, suitable, reasonable, in the opinion of the Commission, no reasonable alternative) are BOOLEAN inputs.
- No DEONTIC rules: `check.sh` cannot see a DEONTIC outcome; duties are BOOLEAN decision rules or the consequence the Act states.
- Every NOT is bracketed; every `#ASSERT` is on one line.
- Sections 56 and 57 are not `inert` (not on the brief's list of reasons): s 56 is a STRING, s 57 is predicates (finding 7).
- Section 54 has a row per paragraph (45 rows), each `inert` with what the paragraph lets be prescribed, or `repealed or blank` for (f.1) and (f.2).
- Sixteen forks, `ei2-F1` to `ei2-F16`, so they cannot collide with the keel's `F1` to `F7`.
- Dates: the range has no enactment, assent or commencement provision; nothing is defined with an `@ref`.

## What is not done (said in NOTES.md "Before this is worth relying on")

No independent test pass (no subagents); no employer seat; the other pieces' rules are not called, only their outcomes taken as inputs.
