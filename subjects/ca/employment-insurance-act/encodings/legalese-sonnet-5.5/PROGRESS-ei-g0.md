# PROGRESS (ei-g0, the keel)

Kept current as I go.
If the context is compacted, re-read this file, NOTES.md and the text, not a summary.

## Status (2026-10-24): the keel is written and checking green

- Written: `eia-core.l4`, `eia-core-interpretation.l4`, `eia-core-maximum-earnings.l4`, `eia-core-insurable-employment.l4`, four tests files (`eia-core-tests-core.l4`, `-interpretation`, `-maximum-earnings`, `-insurable-employment`), `NOTES.md` with all eight required headings, this file.
- `check.sh` (`L4_TARGET=unstable`, binary 1.6.98 main 7689b0d): 0 errors, 218 satisfied, 0 failed, 0 refused over 8 modules (39 + 61 + 82 + 36 assertions in the four tests files).
- `srcrefs.py check --refs` against `S.C.-1996-c.-23.txt`: 113 `src:` lines, 60 runs, 91 locators, 0 problems.
- `l4 check` on each module prints only `Check succeeded.`; the two layout warnings (`follows code on its line`, `is at the end of the file`) do not appear.
- Importing `prelude`, `daydate` and all four keel modules in one file, plus a downstream piece's own record that uses `Reason for benefits` and `Part of the Act`, ran clean in a throwaway file (7 assertions); it is deleted.
- A failing expected value was shown to be caught (one `Minister` assertion flipped on a copy: 81 satisfied, 1 failed); the copy is deleted.
- The scratch folder `deposit/scratch/` (probes, the quote expander, the module templates and the NOTES generator) is deleted before the last check.

## Decisions that are mine, not the text's (assumed, not ruled; each is a fork in NOTES.md)

- F1 s 4(3) has no floor after the first year above $39,000.
- F2 s 5(2)(c) to (e) take an "included by regulations" input, because regs 2(1) and 3(1) say "except for paragraph 5(2)(c) / (d) and (e)".
- F3 a rate produced on the day of the Commission's final determination counts as "most recently produced".
- F4 "within n days after d" ends on d plus n, inclusive; weeks are 7 days; months and years clamp.
- F5 s 5(2)(b) takes the portion of the voting shares the person controls as one number.
- F6 "common-law partner" is measured to the day the question is asked.
- F7 "casual nature" is a BOOLEAN input; the Regulations do not define it.

## Findings about the binary and the text that shaped the work

- `YMD` is not defined even after `IMPORT daydate` on 1.6.98; the core carries the one shim.
- `Day d MODULO 7` is 0 for a Sunday; the Act's week begins on Sunday (s 2(1)).
- A percent literal as a bare argument is read as `%` applied to the next token: write `f (6.5%)`.
- A record type whose name has spaces is backticked before `OF`; `(f x)'s field` does not parse.
- On `daydate` names: a probe file importing only `eia-core` used `Days in a week` and `add years` without `IMPORT daydate`; prelude names were not tested that way, so the instruction to pieces (import `prelude` and `daydate` explicitly) stands.
- My range, lines 1 to 132 of the Act, holds s 1, s 2 (1) to (5), s 3 (1) to (4), s 4 (1) to (5) and s 5 (1) to (7); the brief's one-line description says "sections 1 to 3", its section-label column says 1 to 5.
- No assent or commencement date appears in lines 1 to 132; s 190 (line 3171, piece ei6) carries them.
- Ss 2(3) and 2(4) are reading rules that create no fact; they are `inert` in the coverage table and the Instructions tell every piece to apply them.

## Not done, on purpose

- No seat layer, no `@export`, no `encoding.json`, `SOURCE-LICENSE.md` or README (the brief rules them out for the keel).
- Nothing was added to git.
