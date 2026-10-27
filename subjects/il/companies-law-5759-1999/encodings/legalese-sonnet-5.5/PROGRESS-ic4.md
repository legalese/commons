# PROGRESS: piece ic4 (Part 8, Part 8A, the opening of Part 9), lines 2081-2515

Status line: layer 1, its tests, the seat layer, the cases and NOTES.md are written and checked; what remains is an independent test pass (not done) and the lead's merge.
Re-read this file, NOTES.md and the text (not a summary) after any compaction.

## Done (written, compiled, srcrefs 0 problems, tests green)

Layer 1 (every rule cited with `@ref`, quote lines copied mechanically):

- `ic4-nouns.l4`: helpers only (timing enums, two counting rules, builders of core records).
- `ic4-part8-merger.l4` (ss 314-327), `ic4-part8-special-tender-offer.l4` (ss 328-335), `ic4-part8-forced-sale.l4` (ss 336-342א).
- `ic4-part8a-general-court.l4` (ss 342ב-342כג), `ic4-part8a-voluntary.l4` (ss 342כד-342מ), `ic4-part8a-fast-track-misc.l4` (ss 342מא-342נד).
- `ic4-part9-changing-types.l4` (ss 343-345).

Tests of layer 1, 707 assertions: `ic4-tests-part8-merger.l4` (134), `ic4-tests-part8-special-tender-offer.l4` (95), `ic4-tests-part8-forced-sale.l4` (71), `ic4-tests-part8a-general-court.l4` (153), `ic4-tests-part8a-voluntary.l4` (127), `ic4-tests-part8a-fast-track-misc.l4` (79), `ic4-tests-part9-changing-types.l4` (48).

Layer 2:

- `ic4-seat.l4`: 163 questions in 18 groups, each with `@export` and `@desc` (Hebrew, ` / `, English); every question calls a layer-1 rule by name.
- `ic4-cases-seat.l4`: 627 assertions, at least one case for every question, both sides of every threshold, the not-covered answers asserted.

NOTES.md: all ten headings; the coverage table has 190 rows (146 encoded, 29 inert, 15 fork) and every non-blank line of src:2081-2515 is in exactly one row.

## Tooling (outside the deposit, under `<INPUTS_DIR>/_work/`)

- `expand.py`: replaces a line `@@Q N-M` in a `.l4` file with the mechanical `-- src:N |` quote lines.
- `coverage_rows.py` + `coverage.py`: the coverage rows; the script regenerates `_work/notes/05-coverage-rows.md` and fails if a non-blank line is uncovered or an encoded row names no rule.
- `seat-*.l4` + `snippets.txt` + `seat_build.py`: the staged parts of `ic4-seat.l4` and the shared input blocks; `ic4-seat.l4` is GENERATED, edit the parts and run `python3 -I seat_build.py`.
- `cases_data.py` + `cases_gen.py` (+ `seatq.py`, `old_qnames.json`): the hand-written cases and the generator of `ic4-cases-seat.l4`; the generator checks the number and kind of each case's inputs and computes no expected value.
- `build_notes.py` + `build_notes_text.py` + `jural_rows.py`: assemble NOTES.md (it also runs `check.sh` and pastes its output).

## Decisions taken (each with the section that licenses it); the forks are F1 to F17 in NOTES.md

- Time limits: "within N days" is inclusive of day N (F1); 317(ב)'s creditor-notice duty has no limit of its own (F2); the directions power of 319 needs the request but not the finding (F3).
- 320(א1)(2)(ב): the caller supplies the fraction (F4); class meetings are still needed after (א1) (F5); 323 "have passed" is at least N (F6).
- 327(א) and 342ב: "a majority of three quarters" is at least 3/4 of for plus against, abstentions not counted (F7, F13).
- 328(א): "becomes" and "rises above" mean crossing the line in this purchase (F8); 333(ב) takes the lower cap (F9); 334 "a year" is twelve months (F10).
- 338: accepted under either route; the waiver is for 337 only (F11); 341(א): the caller states the fraction, excluded persons out of the numerator (F12).
- 342ו: a year is twelve months (F14); 342לו(ב): the calendar year of the first anniversary counts (F15); 342מז(א): the duty arises at ten working days, no later limit (F16); 345(ג): three quarters of those who voted, by members (F17).
- Seat (ruled by the brief): the individual who founds, directs or holds shares; officials get no seat; other parties' facts are inputs (Hohfeld).
- Input names follow the keel's naming rules: none equals a constructor of `צד` or a rule, type or field name, and a yes-or-no input that would begin with the article ה and a party noun carries `אם` in front (`_work/rename_inputs.py`, `rename_inputs2.py`, `namecheck.py`).

## Open

- No independent test pass has been done: the cases were written by the encoder who wrote the rules.
- Nothing in the folder has been verified against the official text; the source is the Hebrew Wikisource consolidation.

## Files written

ic4-nouns.l4; ic4-part8-merger.l4; ic4-part8-special-tender-offer.l4; ic4-part8-forced-sale.l4; ic4-part8a-general-court.l4; ic4-part8a-voluntary.l4; ic4-part8a-fast-track-misc.l4; ic4-part9-changing-types.l4; the seven ic4-tests-*.l4; ic4-seat.l4; ic4-cases-seat.l4; NOTES.md; PROGRESS.md.
