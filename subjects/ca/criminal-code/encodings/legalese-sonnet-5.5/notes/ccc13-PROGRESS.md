# PROGRESS.md -- ccc13 (Criminal Code (Canada), lines 7145-7874: Parts X and XI)

State: layer 1, the seat layer, the cases, NOTES.md and NEEDS-CORE.md are written; the gates below passed on the last run.
This file is the memory across compactions: re-read it, NOTES.md and the text, not a summary.

## Gates (last run; NOTES.md ends with the full check.sh output)
- `check.sh` (stable 1.6.110 against stable 1.6.109, `JL4_LIBRARY_PATH` unset): TOTAL (30 modules) 2215 satisfied, 0 errors, 0 failed, 0 refused, every module `same` on both builds. `ccc13-cases-seat.l4`: 1010 of 1010.
- `srcrefs.py check --refs` and `--strict` over every `ccc13-*.l4`: 709 src: lines, 210 runs, 417 locators, 0 problems.
- `work/verify-quotes.py`: 193 FALSE-kind quotations, 73 NOTHING-kind tags, 0 problems.
- `#TRACE` outputs of the two builds: six files, 36 directives, byte-identical.

## Pipeline (scripts outside the deposit, in ../../work/ relative to the deposit folder = runs/dst-ccc13/work)
- `work/units.py` splits lines 7145-7874 into 495 coverage units; `work/coverage.py` maps each to the layer-1 names whose `@ref` source range overlaps it.
- `work/src/*.l4.in` are the layer-1 and test templates; `work/build.py NAME` expands them (`@@Q`, `@@R`, `@@PUN`, `@@PUNQ` directives) into the deposit.
- `work/gen_seat.py` (with `seat_spec.py`) writes `ccc13-seat.l4`; `work/gen_cases.py` (with `seat_cases.py`) writes `ccc13-cases-seat.l4`.
- `work/notes.py` (with `notes_static.py`, `jural.py`) writes `NOTES.md` and `NEEDS-CORE.md`; `work/scan_cases.py` scans the cases against the layer-1 code.
- To change a `.l4` file: edit the template or the spec, rebuild, then rerun check.sh, srcrefs in both modes, verify-quotes and the TRACE comparison, then `work/notes.py` (it reads `work/check-final.log`).

## Decisions taken (each licensed by the brief unless stated; every fork is in NOTES.md)
- D1. Offence elements unmet: JUST FALSE (reading (a), fork F1); "No person shall" prohibitions: JUST TRUE when met, NOTHING otherwise (reading (b)).
- D2. Penalty: a section with both limbs answers two Punishments; "punishable on summary conviction" with no penalty stated takes the s 787(1) input.
- D3. The three-valued helpers `ccc13 all of`, `ccc13 any of`, `ccc13 not` are in `ccc13-logic.l4` and listed in NEEDS-CORE.md.
- D4. Layer 1 imports `ccc-definitions` and calls the keel's `s 2 ...` functions (the brief overrides PLAN section 1).
- D5. Court powers are `MAY` with no `LEST`, duties `MUST`, prohibitions `SHANT`; a saving is its own function and the offence takes its answer as a `MAYBE BOOLEAN`.
- D6. A power named "may" with an "if" gate answers NOTHING when the gate fails (rule of 2026-11-12; F5, F7); the where/when/upon-gated ones (3) and the "entitled" ones (0) are listed, not decided.
- D7. The exceptions of s 445.2(2.2), (3), (3.1) answer JUST FALSE for "no exception on these facts" (F12).
- D8. At the seat, "is it a testamentary instrument?" is a plain yes/no (F13, seam S4).

## Files in the deposit
`ccc13-logic.l4`, ten layer-1 modules (`fraud`, `securities-title`, `fares-minerals`, `documents-identity`, `trademarks`, `wreck-stores`, `contract-intimidation`, `mischief`, `arson-property`, `animals`), `ccc13-index.l4`, the matching `ccc13-tests-*.l4`, `ccc13-seat.l4`, `ccc13-cases-seat.l4`, `NOTES.md`, `NEEDS-CORE.md`, `PROGRESS.md`, and the supplied `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `ccc-core.l4`, `ccc-definitions.l4`, `ccc-interpretation.l4`.

## Next
Nothing is open in this part. The final report is the last message of the session.
