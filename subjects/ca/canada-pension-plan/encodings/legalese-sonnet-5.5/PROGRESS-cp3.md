# PROGRESS: piece cp3

Brief: BRIEF.md in the piece folder (one level above `deposit/`); the text is lines 921-1569 of the Act file (sections 42 to 55.2(5.1)).

## State

Layer 1 (nine module files plus the nouns), its tests, the seat layer (`cp3-seat.l4`, 86 questions) and its cases (`cp3-cases-seat.l4`) are written; NOTES.md carries all ten headings; the coverage table has 150 rows and none is `deferred`.
The result of the last full `check.sh` is in NOTES.md under "What check.sh prints".
Nothing here is committed or pushed (the brief forbids it).

## Files

- `cp3-nouns.l4`: the local types (kind of dependent child, month and year records, life events, the lookback records, when the Minister is informed of a conviction).
- Layer 1, each with a `cp3-tests-<name>.l4`:
  - `cp3-part2-interpretation.l4`: sections 42 (not the definitions the core holds), 43.
  - `cp3-benefits-payable.l4`: section 44(1). `cp3-minimum-qualifying-period.l4`: 44(2) to (5), with count-based rules for the seat. `cp3-benefits-not-payable.l4`: 44.1, 44.2.
  - `cp3-retirement-pension.l4`: 45, 46. `cp3-average-earnings.l4`: 47, 48 to 48.2. `cp3-contributory-period.l4`: 49 to 50.2.
  - `cp3-pensionable-earnings.l4`: 51 to 51.3. `cp3-deemed-contributions.l4`: 52 to 52.2. `cp3-unadjusted-earnings.l4`: 53 to 54.2.
  - `cp3-division.l4`: 55, 55.1, 55.11, 55.2 to (5.1).
- Layer 2: `cp3-seat.l4`, `cp3-cases-seat.l4`.
- `NOTES.md`, `PROGRESS.md`.

## Method notes (survive a compaction)

- Tooling that is not part of the deposit lives in the session scratchpad `work-cp3/`: `cov.py` keeps the coverage table (`coverage.tsv`, 150 rows) and renders it into NOTES.md; `expand.py FILE` replaces lines `@@Q N M` in a `.l4` file with `srcrefs.py quote` lines of the Act (source text is never retyped); `assemble.py` builds NOTES.md from `notes-parts/*.md` and then `cov.py render` fills the coverage table.
- Run: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` from this folder (several minutes on a loaded machine; run it in the background); `python3 -I srcrefs.py check --refs <Act file> cp3-*.l4`; one file: `<L4_BIN> run FILE`.
- Out-of-range dependencies are plain inputs with an `-- out of range:` comment at the rule; the table is NOTES.md "Cross-references out of my ranges".

## Decisions taken (each with the provision that licenses it)

- Month = DATE of its first day; ages only through the core's section 2(2) rule (`any other provision`; `paragraph 44(3)(a)` for the one place the actual birthday is used). Licence: section 2(2) and 44(3)(a).
- The Minister's judgments (approval, "informed and satisfied", "satisfied that", the determination of a disability) are plain BOOLEAN or DATE inputs, supplied conditionally. Licence: the Commons ruling of 2026-10-18.
- Counterfactuals ("a disability pension would have been payable if an application had been received earlier": 44(1)(b)(ii), (iii), (e)(ii), (iii), (h)(ii), (iii); 44(2.2)(c)) are plain BOOLEAN inputs.
- Figures the Regulations set are inputs, not encoded (piece cr2 owns them).
- Forks F1 to F27: NOTES.md "Fork register".
- No seat question for the rules that need a list or a record (NOTES.md "Seat").
