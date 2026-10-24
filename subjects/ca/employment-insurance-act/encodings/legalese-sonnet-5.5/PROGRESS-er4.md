# PROGRESS: piece er4 (Regulations Part II, Part III, Part III.1, Part III.2; lines 993-1393 of SOR-96-332.txt)

Written for the agent itself: after a compaction, re-read this file, NOTES.md and the text, not a summary.

## Range, as the section index gives it

- Part II National Employment Service: regs 58, 59 (lines 993-1008).
- Part III Reduction of Premium for Employers with Wage-Loss Plans: regs 60 to 76 (lines 1009-1171).
- Part III.1 Reduction of Premiums for Employees Covered by a Provincial Plan and for their Employers: regs 76.01 to 76.3, Divisions 1 to 5 (lines 1172-1320).
- Part III.2 Reduction of Premium for Self-Employed Persons Covered by a Plan Established Under a Provincial Law: regs 76.31 to 76.45 (lines 1321-1392).
  The brief's one-line description of the piece names Parts II, III and III.1 only; the line range (993-1393) and the section labels (58 to 76.45) include Part III.2, so it is encoded here.
- Line 1393 is blank; Part IV opens at line 1394 (piece er5).

## Files (all in this folder; the keel's `eia-core*.l4`, `check.sh`, `srcrefs.py` were already here and are not mine)

Layer 1, regs 58 to 76.45: `er4-nouns.l4`, `er4-part2-national-employment-service.l4` (58, 59), `er4-part3-reduction.l4` (60-62), `er4-part3-reg63-weekly-indemnity-plan.l4` (63), `er4-part3-regs64-66-other-plans.l4` (64-66), `er4-part3-qualifying-plan.l4` (67), `er4-part3-application.l4` (68-76), `er4-part3-1-premium-reduction.l4` (76.01-76.08), `er4-part3-1-entitlement.l4` (76.09-76.18, 76.22, 76.23), `er4-part3-1-weeks.l4` (76.19-76.21), `er4-part3-1-premiums-and-administration.l4` (76.24-76.3), `er4-part3-2-self-employed.l4` (76.31-76.45).
Tests, one file per module: `er4-tests-part2`, `-part3-reduction`, `-part3-reg63`, `-part3-regs64-66`, `-part3-reg67`, `-part3-application`, `-part3-1-premium-reduction`, `-part3-1-entitlement`, `-part3-1-weeks`, `-part3-1-premiums-and-administration`, `-part3-2-self-employed` (all `.l4`).
Layer 2: `er4-seat.l4` (45 `@export` questions), `er4-cases-seat.l4`.
Reports: `NOTES.md`, `PROGRESS.md`.

## Status

DONE. Every coverage row in NOTES.md is set (none `deferred`), all ten required NOTES headings are written, and the final `check.sh` output is pasted in NOTES under "What check.sh prints".
The decisions and forks are in NOTES.md (Fork register F1 to F24); this file does not repeat them.
The throwaway helper `er4-tools.py` has been deleted.
