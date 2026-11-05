# PROGRESS -- mlr5 (lines 3055-3808 of uksi-2017-692.txt)

STATUS (2026-11-05): DONE, then REVISED the same day under Meng's rulings of 2026-11-05 (periods, "where", delegated definitions, defences, "until" bars; two bullets in the NOTES fork register). Layer 1, the seat layer, NOTES.md and NEEDS-CORE.md are written; the full `check.sh` (main 1.6.109, second run on 1.6.108) is clean; `srcrefs.py check --refs` and `--strict` report 0 problems on every `mlr5-*.l4` file.
The numbers are in NOTES.md ("What check.sh prints"); this file is the resume anchor if the work is reopened.
Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Units in my range (read by hand, lines 3055-3808)

| lines | unit | module |
| --- | --- | --- |
| 3055-3081 | Schedule 3ZA (all dots: blank) | none (repealed or blank in this text, reason 3) |
| 3082-3205 | Schedule 3A Excluded Trusts | mlr5-sch3a.l4 |
| 3206-3241 | Schedule 4 Supervisory Information (21 printed items) | mlr5-sch4.l4 |
| 3242-3255 | Schedule 5 Connected Persons | mlr5-sch5.l4 |
| 3256-3348 | Schedule 6 Meaning of relevant requirement | mlr5-sch6.l4 |
| 3349-3390 | Schedule 6A UK FIU (paragraph numbers 5-8, 10-12, 14-15 derived from cross-references) | mlr5-sch6a.l4 |
| 3391-3543 | Schedule 6B Changes in control of registered cryptoasset businesses | mlr5-sch6b.l4 |
| 3544-3794 | Schedule 7 Consequential amendments (3 inserted rules encoded: paras 3(2), 12, 18; the rest inert reason 2; para 27 blank) | mlr5-sch7.l4 |
| 3795-3808 | Explanatory note (not operative) | none (inert reason 1) |

## Done (all with `l4 run` of the main 1.6.109 binary: 0 errors, 0 warnings, assertions satisfied = assertions written)

| module | tests | assertions |
| --- | --- | --- |
| mlr5-sch3a.l4 | mlr5-tests-sch3a.l4 | 224 |
| mlr5-sch4.l4 | mlr5-tests-sch4.l4 | 131 |
| mlr5-sch5.l4 | mlr5-tests-sch5.l4 | 46 |
| mlr5-sch6.l4 | mlr5-tests-sch6.l4 | 207 |
| mlr5-sch6a.l4 | mlr5-tests-sch6a.l4 | 84 (+30 #TRACE, all FULFILLED, not counted) |
| mlr5-sch6b.l4 | mlr5-tests-sch6b.l4 | 219 |
| mlr5-sch7.l4 | mlr5-tests-sch7.l4 | 36 (+3 #TRACE: BREACHED, a residual obligation, FULFILLED) |
| mlr5-seat.l4 (67 questions) | mlr5-cases-seat.l4 | 199 |

Total 1146 assertions.
Positive control (every expected value changed, scratch copy): all 1146 then failed.
The #TRACE outcomes of the Schedule 6A and Schedule 7 tests are identical on 1.6.108 and 1.6.109.

## Scratch (not shipped), under ../work/

- `tmpl/*.l4` are the sources with `{{Q a b}}` quote macros; `build.py` expands them (via `srcrefs.py quote`) into this folder; `run1.sh name...` builds, runs and runs srcrefs --strict.
- `gen_sch3a.py` (+ `sch3a_spec.py`, `sch3a_bodies.py`, `sch3a_tests.py`), `gen_sch4.py`, `gen_sch6a.py`, `gen_sch6b.py` (+ `mlr5-sch6b.in`), `gen_sch7.py`, `gen_seat.py` generate the modules, tests and the seat layer; sch5 and sch6 were written directly in `tmpl/`.
- `coverage.py` (+ `coverage-extra.json`) builds the coverage table; `audit.py` and `branches.py` audit the FALSE/NOTHING tags; `ctl.py` is the positive control; `make_notes.py` assembles NOTES.md from what is on disk.

## Decisions taken (with the text that licenses each)

- Paragraph labels for unnumbered paragraphs: Sch 3A `sch 3A para N+k` by position (lines 3085-3088, 3123-3130, 3133-3135, 3177-3184); Sch 4 `sch 4 item N` by printed order; Sch 6 by print order; Sch 6A by the Schedule's own cross-references (lines 3365, 3368, 3370, 3375, 3383).
- Sch 3A, 6B, 6A: a description of a kind of trust or a duty limited by its own wording, with no "where", "if", period or "only", answers NOTHING outside it (brief, FALSE and NOTHING rule); `means`, `if`/`unless`, "where"/"upon", a period the text fixes and "only" answer JUST FALSE when unmet (rulings of 2026-11-05; forks S3A-F3, F7, F8, F9, S5-F2, S6A-F5, S6B-F4, S7-F3).
- Sch 6B: both vintages encoded; the split is on the date the business was entered on the register (25 October 2027), not on an as-at date; paragraph 5 governs paragraphs 1 and 3 and excludes a custodian wallet provider, the 191G insertion includes one (fork S6B-F1).
- Sch 7 paragraph 18(c), regulation 48(2): the flat negative names its bearer, so a SHANT rule is derived from the JUST FALSE answer (ruling N2).
- The seat has one whole-Schedule 3A question over the 94-fact record (first of the group, calling the combined function: S3A-F8) and one question per paragraph (ruling E1, option C).
- Combined Schedule 3A function: JUST TRUE if any paragraph; NOTHING only if an unknown relevant-supervised-person answer could still make paragraph 12 or 13 apply; otherwise JUST FALSE. This departs from "JUST FALSE only when every paragraph answers JUST FALSE" because the paragraphs with no trigger would then keep it NOTHING for almost every trust; one line to flip, noted in S3A-F8.
