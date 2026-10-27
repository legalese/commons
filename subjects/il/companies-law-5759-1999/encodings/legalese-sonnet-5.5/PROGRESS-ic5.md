# PROGRESS: piece ic5 (Part 9 chapter 1A, src:2516-2955)

How I work (read this first after any compaction).
- Templates of the layer-1 modules are `*.l4.in` files in `INPUTS_DIR/work/`; `INPUTS_DIR/work/expand.py` expands the `%%SRC N` / `%%SRC N-M` marker lines into `-- src:N | ...` quote lines read from the raw text by `srcrefs.py` and writes the `.l4` into this folder.
  Never edit an expanded layer-1 `.l4` here by hand: edit its `.l4.in` and run `python3 expand.py`.
  The seat, the cases and the tests carry no quotations: they are written directly in this folder.
- NOTES.md is assembled by `INPUTS_DIR/work/build_notes.py` from part files in `INPUTS_DIR/work/` (`coverage.tsv`, `jural.tsv`, `xref.tsv`, `forks.md`, `notes-text-says.md`, `needs.md`, `binary.md`, `checksh.md`, `before.md`, `notes-*.md`).
  Edit the parts, never NOTES.md itself. `INPUTS_DIR/work/cov_check.py` lists the non-blank lines of the range that no coverage row names.
- Binary: `L4_BIN` = the `l4` 1.6.98 named in the task. Check: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.

## Plan (modules, in the text's order)

| module | sections | status |
| --- | --- | --- |
| ic5-parties | the Registrar of Endowments, the Attorney General, any other person (shared party type) | done |
| ic5-a1-registration | 345א-345ד | done, tested (ic5-tests-a1), coverage/jural/xref/forks recorded |
| ic5-a2-articles-and-distribution | 345ה-345ז | done, tested (ic5-tests-a2), recorded |
| ic5-a3-audit | 345ח-345ט | done, tested (ic5-tests-a3), recorded |
| ic5-a4-pay-transactions-liability | 345י-345יג | done, tested (ic5-tests-a4), recorded |
| ic5-a5-claims-shares-merger | 345יד-345יח | done, tested (ic5-tests-a5), recorded |
| ic5-a6-winding-up | 345יט-345כג | done, tested (ic5-tests-a6), recorded |
| ic5-a7-reporting-supervision | 345כד-345כד5 | done, tested (ic5-tests-a7), recorded |
| ic5-a8-remedies-application | 345כה-345לג | done, tested (ic5-tests-a8), recorded |
| ic5-b1-fund-status | 345לד-345לח | done, tested (ic5-tests-b1), recorded |
| ic5-b2-fund-money | 345לט-345מא | done, tested (ic5-tests-b2), recorded |
| ic5-b3-fund-governance | 345מב-345מט | done, tested (ic5-tests-b3), recorded |
| ic5-b4-fund-misc | 345נ-345נג | done, tested (ic5-tests-b4), recorded |
| ic5-seat / ic5-cases-seat | all | done: 210 questions under 52 `§§` headings (ic5-seat.l4), 700 worked cases (ic5-cases-seat.l4), every question at least once; both written by scripts in INPUTS_DIR/work/seatgen from the spec*.py and case*.py files there (the files in this folder are the deliverable; the scripts are not) |

## Decisions taken (with the section that licenses each)

- Predicates, not deontic rules: every duty, power and approval is a BOOLEAN, DATE, NUMBER or enumeration-valued rule (no DEONTIC), because a DEONTIC cannot be asserted with `EQUALS` and check.sh does not see `#TRACE` outcomes. Judgments handed to an official or court ("persuaded that it is just and right") are BOOLEAN inputs named for the judgment.
- Rule names are `סעיף N(…) - …`, neutral about whose side asks; constructors of local enumerations carry the chapter or section in their names so no name is defined twice (the party type is `ic5-parties`: `רשם ההקדשות (פרק 1א)` etc.).
- Day counting (F1): event date + N days; the N-th day is inside the period.
- No date of enactment, assent or commencement is in src:2516-2955 (the chapter's amending years in the section templates, such as תשס״ז־2, are not dates the text fixes); nothing to carry.
- Regulation-making powers and the Wikisource `{{ח:הערה|פורסמו …}}` notes are `inert` (reasons in the coverage table).
- Forks F1-F23 are in the fork register (work/forks.md).
- Coverage: 201 rows, every non-blank line of src:2516-2955 named (cov_check.py prints 0 missing); 60 sections and 3 chapter or sub-chapter headings.

## Files written

Layer 1 (expanded from templates): ic5-parties.l4, ic5-a1-registration.l4, ic5-a2-articles-and-distribution.l4, ic5-a3-audit.l4, ic5-a4-pay-transactions-liability.l4, ic5-a5-claims-shares-merger.l4, ic5-a6-winding-up.l4, ic5-a7-reporting-supervision.l4, ic5-a8-remedies-application.l4, ic5-b1-fund-status.l4, ic5-b2-fund-money.l4, ic5-b3-fund-governance.l4, ic5-b4-fund-misc.l4.
Tests: ic5-tests-a1.l4 to ic5-tests-a7.l4, ic5-tests-a8.l4, ic5-tests-b1.l4 to ic5-tests-b4.l4.
Seat layer: ic5-seat.l4, ic5-cases-seat.l4.
Report: NOTES.md (assembled from the part files by build_notes.py; every heading the brief names, in its order), this PROGRESS.md.

## Status (end of the run)

- All sections of src:2516-2955 are encoded in layer 1 or marked `inert` / `repealed`, with a coverage row each; the 23 forks are in the register.
- `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`: 33 modules, 0 errors, 1550 assertions satisfied (850 in the twelve layer-1 test files, 700 in ic5-cases-seat.l4), 0 failed, 0 refused. The full output is in NOTES.md under "What check.sh prints".
- `python3 -I srcrefs.py check --refs` on all ic5-*.l4: 0 problems; `--strict` on the layer-1 modules: 0 problems.
- One seat case was written the wrong way round (345ב(ג): a resolution that would not bring the 345א(א) conditions about) and corrected to the text after the first run; it is recorded as a finding in NOTES.md.
- Not done, and not claimed: any review by a domain expert; any comparison with the official text; running the Legalese Interact form over the seat.
