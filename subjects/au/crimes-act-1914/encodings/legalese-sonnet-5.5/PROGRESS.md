# Progress

Subject: Crimes Act 1914 (Cth), sections 4AA to 4N, with section 4A and the section 3 terms those sections use.
Edition: compilation C2026C00368, text lines 4332-4456 of `C1914A00012.txt`, and the section 3 lines the encoding uses (41, 144, 146, 151, 163, 189-196).

Status: draft.
This file states what exists on disk when it was last written; NOTES.md states what the encoding says.

## Done and gated (builds 1.6.98 and 1.6.110 agree on every count)

- Layer 1: `crm-time.l4`, `crm-defs.l4`, `crm-penalty-units.l4`, `crm-penalties.l4`, `crm-offences.l4`, `crm-liability.l4`.
- Tests of each: `crm-tests-time.l4`, `crm-tests-defs.l4`, `crm-tests-penalty-units.l4`, `crm-tests-penalties.l4`, `crm-tests-offences.l4`, `crm-tests-liability.l4`.
- Script-built: `crm-provisions.l4`, `crm-xrefs.l4`, `crm-tests-xrefs.l4`.
- Layer 2: `crm-seat.l4` (32 questions) and `crm-cases-seat.l4`.

## Decisions taken, with the provision that licenses each

- A "means" definition, a flat negative, "if", "unless", "only if" and a failed "where" give `JUST FALSE`; a list left open, "includes", a limit with no "only", and silence give `NOTHING` (section 5 of the guide).
- Each "unless the contrary intention appears" is a yes/no input of the rule it qualifies (ss 3(1), 4A, 4B, 4D, 4E, 4G, 4H, 4J(1), 4JA(3), 4K(1), 4L).
- Every judgment the text leaves to a court is a yes/no input (ss 4B(2), 4B(3), 4J(4)).
- Indexation inputs (the two index numbers and the amount just before the indexation day) are inputs because the text does not print them (s 4AA(3), (4)).
- The coverage table is built by `work/coverage.py` from the text file; the provision index and cross-reference rows are built by `work/gen_index.py`.

## Written after the gate

- NOTES.md (seat, scope, how dates are counted, jural relations, coverage table, fork register F1-F24, what the Act turns out to say, what the text does not answer, cross-references, what the stable binary does not accept, what `check.sh` prints, what would need doing).
- `encoding.json` and `SOURCE-LICENSE.md`.
- The final run of `check.sh` (the counts are in NOTES.md and `encoding.json`; every module has the same four counts on both builds), `srcrefs.py --refs` and `--strict` (0 problems), and a search for warnings and errors on both builds (none).

## Files

- Layer 1: `crm-time.l4`, `crm-defs.l4`, `crm-penalty-units.l4`, `crm-penalties.l4`, `crm-offences.l4`, `crm-liability.l4`, `crm-provisions.l4`, `crm-xrefs.l4`.
- Tests: `crm-tests-time.l4`, `crm-tests-defs.l4`, `crm-tests-penalty-units.l4`, `crm-tests-penalties.l4`, `crm-tests-offences.l4`, `crm-tests-liability.l4`, `crm-tests-xrefs.l4`.
- Layer 2: `crm-seat.l4`, `crm-cases-seat.l4`.
- Notes: `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`.
