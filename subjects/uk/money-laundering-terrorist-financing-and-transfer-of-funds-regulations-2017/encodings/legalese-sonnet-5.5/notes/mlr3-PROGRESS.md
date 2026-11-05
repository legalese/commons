# PROGRESS -- mlr3 (lines 1586-2199 of uksi-2017-692.txt)

STATUS (2026-11-05): finished for the main build, and updated after the independent review (the follow-up is described under "After the review" below).
Each "done" line says how it was checked; the source is a plain-text rendering, not the official text, and nothing here is verified against the official text.

## Method (so a resumed session can rebuild)
- Work dir (not shipped): `iaw-mlr3/work/`.
  Sources of the modules are `work/src/*.l4.in`; `work/build.py` expands `{{REF label a b}}` into verbatim `-- src:` quote lines plus an exact `@ref`, writes the real files into the deposit folder, and runs `srcrefs.py check --refs` and `--strict` over them.
- The seat layer is generated: `work/seatgen.py` reads `work/seatspec1.py` (regs 53 to 56B), `seatspec2.py` (57 to 60B), `seatspec3.py` (61 to 64H) and `seat-part1.in` / `seat-cases-part1.in`, and writes `work/src/mlr3-seat.l4.in` and `work/src/mlr3-cases-seat.l4.in`.
  Every expected value in the cases is written in the spec by hand from the text.
- Coverage: `work/mkmap.py` writes `work/coverage-map.tsv`; `work/cov.py` (modes `rows`, `check`, `table OUT.md`) parses lines 1586-2199 into rows and fails if a non-blank line is in no row or a cited L4 name is not a top-level name.
- NOTES.md is assembled by `work/notes-build.py` from `work/notes/jural.py`, the coverage table, `BRIEF.md` (E1 and N2, copied by script; the two 2026-11-05 bullets are written in `notes-build.py`) and `work/notes/check-output.txt` (the last `check.sh` output).
- `work/tracecheck.py` checks the `-- EXPECT FULFILLED|BREACH` comment above each `#TRACE` against the printed outcome (not shipped, because `#TRACE` outcomes cannot be asserted on main).
- `work/chk.py FILE` runs the main binary on a deposit file and prints error and assertion counts.

## Done (and how it was checked)
- Layer 1, four modules in the text's order: `mlr3-supervision.l4` (45A to 52B), `mlr3-registration.l4` (53 to 60B), `mlr3-transfer-of-funds.l4` (61 to 64), `mlr3-cryptoasset-transfers.l4` (64A to 64H).
  Checked by `check.sh`: 0 errors on both binaries, and by a scan of every file on both binaries for Warning and Error diagnostics (none; the scan was given a positive control, which found its 4 warnings and 1 error).
- Tests, one file per module: 294, 395, 82 and 217 assertions satisfied, and 24, 24, 5 and 14 `#TRACE`s.
  Checked by `check.sh` (0 failed, 0 refused) and `tracecheck.py` (67 of 67 traces match their `-- EXPECT`, re-run after the follow-up).
  A positive control was run earlier: an expected value flipped in a copy of the seat cases file made the count show `failed 1`; the copy was deleted.
- Seat layer: `mlr3-seat.l4` (143 questions, every one `@export` and named "Under regulation N, ..."; all 549 inputs carry `@desc`, counted over the inputs of the exported questions; one `§` and eight `§§` headings in the text's order) and `mlr3-cases-seat.l4` (511 assertions satisfied).
- Coverage: `work/cov.py check` reports 614 rows for 614 non-blank lines, 0 problems; encoded 485, fork 58, inert 44 (all reason 1), repealed or blank in this text 27 (after the follow-up the rows of regs 46(5), 49(3)(b), 50(2), 54(2), 60(4), 62(1), 62(2), 64(3), 64C(6)(b), 64D(2)(c)(i) and 64E(2)(b)(i) name forks F12 to F15, which moved 32 rows from encoded to fork; before it: encoded 517, fork 26).
- Source quotes: `srcrefs.py check --refs` and `--strict` each report 560 `src:` lines, 205 runs, 299 locators, 0 problems.
- NOTES.md: all headings the brief asks for; the markdown tables have equal column counts in every row; E1 and N2 are present word for word (each found once by exact line match against `BRIEF.md`), and the two bullets of 2026-11-05 are in short words with Meng's typed times; the markdown tables were re-checked for equal column counts after the follow-up (5 tables, 0 bad rows).
- `check.sh` last run: TOTAL 11 modules, 0 errors, 1499 satisfied (1376 before the review follow-up), 0 failed, 0 refused on both builds, every module "same" (full output at the end of NOTES.md).
- `mlr-core.l4` was not edited (it is read-only, and its modification time is the same as the supplied `check.sh`).

## Decisions taken (with the provision that licenses each)
- The three rulings (E1 option C with hand-gathering reported; N2 flat negatives are JUST FALSE with SHANT derived; the 2026-11-05 periods, "where" and scope limits) are applied everywhere, per `BRIEF.md`; the fork register in NOTES.md lists each place where I could not tell which letter a clause is.
- F1 reg 54(1A) printed twice (lines 1804-1806 and 1807-1813): both encoded, the seat asks the second.
- F2 reg 50(4) and reg 63(10): the "and" between the EEA and non-EEA authorities joins two kinds of authority.
- F3 reg 64B "working day": for Part 7A only (the text says "In this Part").
- F4 reg 56B(2)(a): the "full commencement day" is in an instrument the text does not give, so it is an input.
- F5 reg 64C(2): the request day does not count in "within three working days of the request".
- F6 reg 56(5): an unmet "where" on a prohibition, in a function named for the permitted act, answers NOTHING.
- F7 reg 59(2) and 59(3A): the period starts at the application, or where applicable at the further information.
- F8 reg 52B(3): the word between (a) and (b) is missing; one limb alone answers NOTHING.
- F9 reg 51(2): "on request" is read as "upon request", which counts as "where", so no request answers JUST FALSE (changed from NOTHING).
- F10 to F15 (added in the follow-up): assumed sites and the yes/no twins (F10), early acts before a "beginning with" period (F11), reg 62(1) giving JUST FALSE for a provider in none of its classes (F12), the "must delay" functions (F13), relative-clause and bare-list scope limits the reviewer expected JUST FALSE (F14), reg 49(3)(b) and overseas authorities (F15).
- Marginal readings (a) to (j) are in NOTES.md with the other reading stated for each.

## After the review (2026-11-05)
- An independent reviewer found 13 failures (all answered NOTHING) and 14 gaps.
  Meng's rulings of 2026-11-05 (typed 04:30:00.322Z and 06:04:54.553Z) were applied everywhere in the range; the changes are listed by item in the final message, and each changed branch carries the ruling's letter in its layer-1 comment.
- Re-run after the follow-up: `check.sh` on both builds (1499 satisfied, 0 failed, 0 refused, every module "same"); `srcrefs.py` `--refs` and `--strict` (560 `src:` lines, 205 runs, 299 locators, 0 problems); `cov.py check` (614 rows, 0 problems); `tracecheck.py` (67 of 67); a scan for Warning and Error diagnostics over every file on both binaries (none; a positive control was run again and its file deleted); a seat audit (143 questions, 549 inputs, every one with `@desc`).
- `work/patches/` holds the patch scripts used for the follow-up, in order (p1 to p22); not shipped.

## Files written
All under `iaw-mlr3/deposit/encodings/legalese-sonnet-5.5/`:
- `mlr3-supervision.l4`, `mlr3-registration.l4`, `mlr3-transfer-of-funds.l4`, `mlr3-cryptoasset-transfers.l4`
- `mlr3-tests-supervision.l4`, `mlr3-tests-registration.l4`, `mlr3-tests-transfer-of-funds.l4`, `mlr3-tests-cryptoasset-transfers.l4`
- `mlr3-seat.l4`, `mlr3-cases-seat.l4`
- `NOTES.md`, `PROGRESS.md`
- Supplied and left as they were: `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `mlr-core.l4`.
- `NEEDS-CORE.md` was not written.

## Not done
- No second (unstable) encoding was written; see "Unstable dialect" in NOTES.md for why.
- Nothing was git-added, committed or pushed.
