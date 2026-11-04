# PROGRESS -- ssc4 (lines 1912-2443 of ukpga-1992-4.txt: Parts III, IV, V ss 63-111)

Written as I go; re-read this, NOTES.md and the text after any compaction.

## Plan (decided 2026-11-04)
Layer 1 modules (flat folder, `ssc4-` prefix), each with a tests module `ssc4-tests-<name>.l4`:
1. `ssc4-attendance-allowance.l4`  ss 63-67
2. `ssc4-carers-allowance.l4`      ss 68-70 (68, 69 blank)
3. `ssc4-disability-living-allowance.l4` ss 71-76
4. `ssc4-guardians-and-aged.l4`     ss 77-79
5. `ssc4-increases.l4`             ss 80-93 (80-86, 90 blank)
6. `ssc4-industrial-injuries-general.l4` ss 94-101
7. `ssc4-disablement.l4`           ss 102-111 (102, 111 blank)
Layer 2: `ssc4-seat.l4`, `ssc4-cases-seat.l4`.
Build: sources in `../../../work/src/*.in` (macro %%REF expands quote lines + @ref via srcrefs.py quote); `work/build.py` writes the deposit .l4 files. Coverage: `work/units.py` seeds ~493 units; dispositions in `work/cov/*.txt`.

## Conventions taken
- Result type `MAYBE BOOLEAN`; BAR POLARITY: a "shall not be entitled" function answers "is the person barred?": JUST TRUE = the text says not entitled, JUST FALSE = the text says no bar (a failed "if", an "unless" met), NOTHING = silent or outside its own wording.
- Inputs from regulations/outside the text: `MAYBE BOOLEAN` in layer 1, plain BOOLEAN asked in the seat.
- K2 age inputs named `s 173(a) the person is over 80` etc. (MAYBE BOOLEAN).
- Schedule 4 rates are `MAYBE NUMBER` inputs named `sch 4 pt III para 1 ...` (table omitted from the text).

## Done (re-run `work/chk.sh <file>` to see current numbers)
- `ssc4-attendance-allowance.l4` (ss 63-67; includes regulative s 65(6)(a)) + tests (121 satisfied, 0 failed)
- `ssc4-carers-allowance.l4` (s 70) + tests (80 satisfied, 0 failed)
- `ssc4-disability-living-allowance.l4` (ss 71-76) + tests (166 satisfied, 0 failed)
- `ssc4-guardians-and-aged.l4` (ss 77-79) + tests (80 satisfied, 0 failed)
- `ssc4-increases.l4` (ss 86A-93) + tests (66 satisfied, 0 failed)
- `ssc4-industrial-injuries-general.l4` (ss 94-101) + tests (131 satisfied, 0 failed)
- `ssc4-disablement.l4` (ss 103-110) + tests (213 satisfied, 0 failed)

- `ssc4-seat.l4` (143 questions) + `ssc4-cases-seat.l4` (355 satisfied, 0 failed)
- `NOTES.md` (coverage 523 rows, fork register F1-F14, jural relations, marginal readings, seams, findings, check.sh output)
- `check.sh` (target main) run 2026-11-04 on the final tree: 17 modules, 1212 satisfied, 0 failed, 0 refused, main (1.6.108) agrees; exit 0. `srcrefs.py check --refs` and `--strict` over the seven layer-1 modules: 495 src lines, 190 runs, 190 locators, 0 problems.

## In progress / next
- Nothing open. The advisor reviewed the work before the last edits; its findings were acted on (s 104(2) and s 105(2) encoded instead of left inert; the reach of the seat computed by `work/reach.py` and 29 more seat questions added; counts in NOTES computed by `work/covhead.py`, `work/rendercov.py` and `work/marg.py`). The seat questions are placed under their section headings (checked by `work/placement.py`: 143 questions, 0 outside their heading, 0 out of order) and `check.sh` was rerun on the final tree with identical output (exit 0, 1212 satisfied). Final report next. Scratchpad tidy: nothing copied (the two l4 binaries in `scratchpad/bin` were supplied, not copied).

## Decisions taken (all "assumed, not ruled")
- A "shall be (the period)" sentence that states what a thing is but has no "if/only if/unless" answers NOTHING when its conditions fail (s 65(1)); s 64(1) holds the "if".
- Month arithmetic: same day of month k months from d; NOTHING when the target month lacks that day (fork F2). Uses `Date`, never `add months`.
- "until" is inclusive of the last day named (fork F3, s 70(1A)).
- A week is Sunday-start (s 122(1), core Week convention 1); anchor Sunday 5 Jan 2025 in `s 70(1A) the days since the last Sunday`.
- Helper `s 65(1)(b) the same day of the month some months from` is imported by later modules.
- F4 (s 75(1) "after he attains"): the day of attaining pensionable age counts as after (s 173: age attained at the start of the anniversary day).
- F14 (s 77(9)): the woman may elect that payment is not made to the man: regulative rule without WITHIN.
- F1 (ss 65(1), 72(1), 73(1)): a "shall be (the period)" grant with no if/only if/unless answers NOTHING when its conditions fail.
- F5 (s 93 "between"): the two named days are outside the run: strictly after the last day payable and strictly before the day entitled again.
- F6 (ss 94(3), 98-101 deeming "if" or "in the absence of"; s 94(3) joined F6 after the independent review of 2026-11-04): the functions answer "does THIS SECTION treat the accident as arising out of and in the course of the employment"; a failed "if" limb is JUST FALSE for the section only, not for the accident (ordinary law is not in the text).
- F7 (ss 94(1), 105(1), 108(1) "where" with no "if"): failure of a limb is NOTHING, not FALSE.
- F8 (s 94(5) "while"): an accident inside Great Britain gives JUST FALSE (no bar) because the bar is written "while ... outside Great Britain".
- F9 (s 97(2)): the direction needs a claim or application, a direction by the Secretary of State and one of the two illegalities; TRUE only then.
- F10 (s 95A(3)): the cross-reference to "section 95(4)" is read as the definition in s 95(5).
- F11 (s 103(3)): an assessment outside the cases (3) names stands as assessed (the function returns it, not NOTHING).
- F12 (s 104(1)): an amount above the Schedule 4 para 2 figure is capped at the figure.
- F13 (s 103(6)): 90 days disregarding Sundays = 90 days that are not Sundays, counted from the accident day.
