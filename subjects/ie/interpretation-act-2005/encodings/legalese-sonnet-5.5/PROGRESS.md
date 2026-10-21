# PROGRESS (Interpretation Act 2005, Ireland; row legalese-sonnet-5.5)

This file is the run's memory.
After a context compaction, re-read this file, `NOTES.md` and the statute text (`../../registers/source-bundle/No.-23-of-2005.txt`, sha256 0108a07d...), not a summary.

## Status

Written 2026-10-21; this version rewritten at the end of the run.
Everything in the brief is written: six Act modules (five answering the Act, one of labelled alternative readings), ten test files, `check.sh`, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.
`NOTES.md` sections 3 to 8 are complete; section 7 holds the final `check.sh` output.
Left to do: nothing in the deposit; the final report goes to the team lead.

## Toolchain facts, measured

- `L4_BIN` is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (checked, matches the brief); `l4 --version` prints `dev`.
- Target compiler: `unstable`, because the brief requires `@lang en`, `REFUSE` and `YMD`, which `main` rejects (`dialects.md`).
  `check.sh` defaults to `L4_TARGET=unstable`, which skips the main comparison.
- `@lang en` draws a Hint, "A module that declares nothing is English; this line can go."; the brief requires the line, so the hint stays.
- `Weekday of` (daydate): Sunday 0 ... Saturday 6; 2026-01-01 is a Thursday (4).
- `YMD 2024 2 30` refuses on this binary; `Date` rolls over; `add months` and `add years` clamp.
- A satisfied `#ASSERT` logs one `Message:` line on this binary; a refusing `#ASSERT` is a Warning, counted as "refused".
- DATETIME has no `<` or `>`; it supports `EQUALS`, and `Date dt` gives the UTC date.

## Design decisions (each with the text that licenses it); the full register is `NOTES.md` section 5

1. A period "from" a day counts that day: s 18(h) first limb. N days from D end on D + N - 1. (F1, F3)
2. A period "after" an event: the text is silent, so every such computation REFUSES. (F2)
3. "month" is a calendar month and "year" is 12 months beginning 1 January (Sch Pt 1), so N months or years from D is determinate only when D is the first day of a month, or 1 January; otherwise REFUSE. Weeks likewise: a week runs Sunday to Saturday (Sch Pt 1 "week" with "midnight"), so N weeks is determinate only from a Sunday. `daydate`'s `add months` clamps; the Act has no clamp rule, so it is used only in the labelled readings module. (F4 to F6)
4. The Act has no rule moving a last day off a day of rest, recess or holiday: the function returns the last day when it is not a rest day and REFUSES when it is. Rest days are an input (a function from a date to a boolean). (F8)
5. Commencement: s 16(1) (Act, nothing expressed) is the date of passing with NO moment; s 16(2), (3), (4) are at the end of the day before. The end of D-1 is the start of D (an assumption, F9). (F10 to F16)
6. "day" is not defined by the Act: a day is a calendar date of `daydate`. (F9)
7. Section 4(1) (contrary intention) is handled ONCE, as a precondition: `a provision of this Act applies to an enactment` in `ie-general.l4` takes the three places a contrary intention can appear, and the other modules state in their headers that they assume none appears. It is NOT a flag on the operative functions, and nothing REFUSES on account of it. (F17)
8. Which language text prevails: the English text says nothing; recorded as a fork, not decided. (F34)

## Files in the deposit

- Act modules: `ie-interpretation-time.l4` (imports only `prelude` and `daydate`), `ie-general.l4`, `ie-operation-and-construction.l4`, `ie-powers-and-service.l4`, `ie-repeal.l4`.
- Labelled alternative readings, NOT the Act's: `ie-month-year-readings.l4`.
- Tests: `tests-periods.l4`, `tests-rest-days-and-words.l4`, `tests-commencement.l4`, `tests-worked-cases.l4`, `tests-general.l4`, `tests-operation.l4`, `tests-powers-service.l4`, `tests-repeal.l4`, `tests-readings.l4`, and `tests-red-control.l4` (eight deliberately wrong expectations, counted).
- `check.sh` (adapted: unstable by default, `tests-red-control.l4` expects 8 failures, optional `SRC_RAW` quotation gate at `--strict`), `fetch-main-l4.sh` (copied beside it; unused for target unstable), `srcrefs.py`.
- `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.
- Scratch (`_work/`, `_probes/`) was deleted at the end.

## History, short

- Update 1: time module and period tests landed.
- Update 2: rest-day, commencement, readings and worked-case tests landed.
- Update 3: the other four Act modules and their tests landed.
- Update 4: red control, `check.sh` adaptation, strict quotation gate (quote runs generated from each `@ref`'s locators; 0 problems).
- Update 5: `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md` written.
  One change after the pre-registered answers: `the first day on which the enactment is in operation throughout` for an Act silent on commencement returned the day after the passing, which contradicted its neighbour's refusal for the passing day; it now refuses, and its test was changed with it. `NOTES.md` 2.3 discloses it.
