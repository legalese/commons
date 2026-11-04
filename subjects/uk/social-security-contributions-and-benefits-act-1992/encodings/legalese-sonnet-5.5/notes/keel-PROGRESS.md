# PROGRESS -- keel agent, row iaw-ssc-k (Social Security Contributions and Benefits Act 1992, UK)

Status (2026-11-04): all deliverables written and checked; the keel stops here.
Text: `inputs/ukpga-1992-4.txt` (5744 lines), a plain-text rendering by a converter script, not the official text.
Keel ranges: line 1; lines 4331-4453 (Part XIII, ss 172-177).
Binary: stable 1.6.98; second build (for the main check): 1.6.108.

## Done
- Read the brief, both skills and their references, the Commons guide, and the seat example.
- Read the headings of the whole Act and the definition sections; built the defined-term ownership map and the cross-part reference matrix (scratchpad scripts, not deliverables).
- Wrote `ssc-core.l4` (nouns and two constants; imports prelude and daydate only).
- Wrote `ssc-definitions.l4` (ss 172, 173, 174, 177(2)) and `ssc-definitions-tests.l4` (165 assertions: 81 hand-written from the text, 84 generated name-resolution checks over the core's constructors).
- Wrote `PLAN.md` (rules, core names, ownership table, per-part blocks, seams S1-S37 plus K1-K3, each with its asking sentence read except that for S4 only the headings of ss 11 and 13 were checked, and the pattern-found appendix whose sentences were not read).
- Wrote `NOTES.md` (coverage table for the keel range, fork register, FALSE/NOTHING reading, marginal readings, Hohfeld table, what the stable binary does not accept, converter-text caveat).

## Decisions (with the section that licenses each)
- Core holds nouns only.
  Regulation-supplied numbers (the s 5 limits, Schedule 4 rates, "prescribed" figures) are inputs, because ss 5 and 122(1) send them to regulations and Schedule 4's tables are omitted from this text.
- Two constants only: the upper accrual point (s 122(1), src:2623) and the 24 weeks of pregnancy (ss 35(6), 171(1), 171ZA(5), 171ZZ15).
- `daydate` defines `Monday` to `Sunday`, `January` to `December` and `May` as NUMBER constants (measured: a constructor named `Monday` fails to check), so the core uses none of those words.
- "Pensionable age" is borrowed from the Pensions Act 1995 (Schedule 4 paragraph 1; src:2597, 2825, 3070, 5691): the core's `Person` carries the date the person attains it.
- "Week" has six meanings across the Act, all in `Week convention` with quotes (the sixth, Schedule 7 at src:5421, was added after a recount).
- `Sex` has two values because ss 37, 48B and 164 speak of a "woman" and a "man" (s 140A(5) defines "woman" for that section alone; no section defines "man").
- Own range: ss 172, 173, 174 and s 177(2) are encoded; s 175, s 176, s 177(1), (3)-(6) and the headings are inert (machinery or not operative); line 1 is inert (enacting words); s 175(1A)(b) is blank in this text.
- The 29 February anniversary is a fork (F1): answered `NOTHING` on 28 February only, because the two readings agree on every other day.
- Failed "if" in s 173(a), (b) counted as the text's no (marginal reading (a), `NOTES.md`); "where appropriate" in s 177(2) is a plain input whose failure is `NOTHING` (marginal reading (b)).

## Corrections made along the way
- The core wrongly said the Act never defines "woman" or "man"; s 140A(5) defines "woman" (src:2918).
  Corrected and quoted.
- A citation of s 44 for woman/man was wrong; replaced by ss 37, 48B, 164.
- The `Kind of employer` comment over-attributed "the Crown" to s 7(1); corrected to s 7(1)(b) for offices and ss 115, 161, 169, 171ZH for the Crown.
- "Week" was said to have five meanings; a recount found a sixth (Schedule 7, src:5421), now in the core and in the tests.
- A table-omission list named "Schedule 3 Part I paragraph 5(5)"; the paragraph number cannot be known (numbers are dropped), so it now cites src:4861.
- A cross-reference matrix hit on ss 36 and 37 for s 62 was a false positive (the National Insurance Act 1965); the same for s 81, s 105, s 159 and s 63(1) in other Acts. `PLAN.md` lists them.

## Last verification (2026-11-04)
- `check.sh` (L4 = stable 1.6.98, L4_MAIN = 1.6.108): ssc-core 0/0/0/0 same; ssc-definitions-tests 0 errors, 165 satisfied, 0 failed, 0 refused, main same; ssc-definitions 0/0/0/0 same; TOTAL 0 errors, 165 satisfied, 0 failed, 0 refused; exit 0.
- `l4 run` on each file: no `DiagnosticSeverity_Error` or `_Warning`.
- `srcrefs.py check --refs` and `--strict`: 30 src: lines, 9 runs, 28 locators, 0 problems.

## Files written (all under DEPOSIT/encodings/legalese-sonnet-5.5/)
- `ssc-core.l4`
- `ssc-definitions.l4`
- `ssc-definitions-tests.l4`
- `PLAN.md`
- `NOTES.md`
- `PROGRESS.md`
(`check.sh`, `fetch-main-l4.sh` and `srcrefs.py` were already there.)
