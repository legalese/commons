# PROGRESS -- dg7 (Subchapter IX, 8 Del. C. ss 255 to 262, source lines 1172 to 1276)

State at the end of the run (2026-10-25): finished; nothing is pending in this folder.

## Done

- Layer 1: `dg7-governing-provisions.l4`, `dg7-nonstock-mergers.l4` (ss 255 to 258), `dg7-merger-effects.l4` (ss 259 to 261), `dg7-appraisal-rights.l4` (s 262(a) to (c)), `dg7-appraisal-procedure.l4` (s 262(d) to (f)), `dg7-appraisal-proceeding.l4` (s 262(g) to (l)).
- Tests: `dg7-tests-nonstock-mergers.l4` (219), `dg7-tests-merger-effects.l4` (82), `dg7-tests-appraisal-rights.l4` (107), `dg7-tests-appraisal-procedure.l4` (157), `dg7-tests-appraisal-proceeding.l4` (79).
- Layer 2: `dg7-seat.l4` (121 `@export` questions) and `dg7-cases-seat.l4` (354 assertions; every question name appears in it).
- `NOTES.md` with the ten headings the brief fixes.
- Gates, last run 2026-10-25: `check.sh` 0 errors, 998 satisfied, 0 failed, 0 refused over 14 modules; `srcrefs.py check --refs` 0 problems over 253 quote lines; `l4 check` on each `dg7-*.l4` file prints no error, warning or layout message; every non-blank source line 1172 to 1276 is named by a coverage row (97 of 97).

## How the files were made

- The five generated layer-1 modules come from templates in `td/dg/dg7/tools/src/*.l4.in` through `td/dg/dg7/tools/build.py`, which copies every `-- src:N |` quote from the raw text. The seat, the cases, the tests and `dg7-governing-provisions.l4` are hand-written.
- `NOTES.md` is assembled from `td/dg/dg7/tools/notes/*.md` by `td/dg/dg7/tools/mknotes.py`, which also checks the coverage table against the raw lines. These tools sit beside this folder, not in it, and are not part of the deliverable.
- The keel files `dg-core.l4`, `check.sh` and `srcrefs.py` are unchanged.

## If the folder is changed later

- Edit the template or the notes part, not the generated file, then rebuild with `python3 -I tools/build.py` and `python3 -I tools/mknotes.py`, and run the gates above.
- All 26 forks are in the register in `NOTES.md`. F-facts-1 (the open list in the "facts" sentence) was added last, at the lead's direction; F-261-1 (the lead-in of s 261(a)) is the one most in need of a lawyer's ruling: its two readings give opposite answers for the nonstock mergers of ss 255 to 258; the reading taken is the list-of-sections one.
