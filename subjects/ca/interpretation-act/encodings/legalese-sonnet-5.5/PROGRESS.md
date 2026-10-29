# PROGRESS (row legalese-sonnet-5.5, Interpretation Act (Canada), R.S.C., 1985, c. I-21), pass 2 ("whole") and pass 3 (corrections)

Pass 2 is a completion pass on the pass-1 draft, to the standard of `BRIEF.md` (Meng's ruling of 2026-10-22).
Binary: `l4-unstable-0528`, `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`.
Run as `L4=<that binary> L4_TARGET=unstable ./check.sh`.

## pass 3 (2026-10-29): corrections after an independent test pass

The lead sent back the items of an independent test pass that were this encoding's (list A to E in NOTES.md `## Pass 3`).
Backup of the deposit taken before any edit, in the session scratchpad (not in this folder); `cmp` against it gives the list of files that changed.

- Defects fixed and logged (`## Changes to existing modules`): the affirmed regulation of s 39(1)(a), (b) (`ca-interpretation-time.l4`, `ca-tests-other.l4`); the numbers between the ends of s 41(1) (`ca-interpretation-rules.l4`, `ca-tests-rules.l4`).
- A row wrongly inert: the Related Provisions item, 1998, c. 30, s. 10, is encoded (`ca-interpretation-commencement.l4`, `ca-tests-transition.l4`, relation R1998-10); every other inert row re-audited and kept (only the Related Provisions item moved).
- New rules: s 39(1)(a) to (d) by expression (`ca-interpretation-resolutions.l4`, `ca-tests-resolutions.l4`); s 7's permission and s 5(4)'s precondition (commencement module); s 3(1) by kind of instrument (definitions module).
- Forks: 6 new class A (F-5-3-THAT, F-32, F-24-DEPUTY, F-8-2-TERRITORIES, F-WRITING, F-HOLIDAY-PLACE), F-39-AFFIRM moved from class B to class A, F-YEAR and F-22 extended; 2 new class B (C-3-1-GATE, S-3-1-KIND); S-HOLIDAY-PLACE replaced.
- NOTES.md edited through a script that locates each target by an exact anchor (a heading, the start of a line, or a string asserted to occur exactly once) and compares the heading list before and after every edit; every heading of the pass-2 file is still present (8 added), and the coverage table has 354 rows.
- Final `check.sh`: 24 modules, 1288 satisfied, 10 failed (all in `ca-tests-red.l4`, expected 10), 0 refused, srcrefs 645 / 328 / 378 / 0 problems, exit 0; `coverage.py check --strict`: 354 units, 0 problems (encoded 261, fork 47, inert 40, repealed 6).
- The baseline numbers below hold or grow by added assertions, except the two that change by replacement: `ca-tests-other.l4` 59 to 60 and `ca-tests-rules.l4` 120 to 133 (a refusal asserted wrongly in pass 1 was replaced by the correct assertions).
- Positive control for the new tests: wrong assertions appended to scratch copies of `ca-tests-transition.l4` and `ca-tests-resolutions.l4` were counted as failed (4) and refused (1) as intended; the copies were deleted.

## baseline (before any change, pass-2 binary, 2026-10-29)

```
module                                    errors satisfied  failed  refused  expected
ca-interpretation-calendar.l4                  0         0       0        0         0
ca-interpretation-repeal.l4                    0         0       0        0         0
ca-interpretation-rules.l4                     0         0       0        0         0
ca-interpretation-time.l4                      0         0       0        0         0
ca-tests-commencement.l4                       0        60       0        0         0
ca-tests-counting.l4                           0        73       0        0         0
ca-tests-holidays.l4                           0       105       0        0         0
ca-tests-other.l4                              0        59       0        0         0
ca-tests-periods.l4                            0       193       0        0         0
ca-tests-red.l4                               10         0      10        0        10
ca-tests-repeal.l4                             0        53       0        0         0
ca-tests-rules.l4                              0       120       0        0         0
TOTAL (12 modules)                            10       663      10        0
srcrefs check: 381 src: lines, 157 runs, 179 locators, 0 problems
```

The same numbers as pass 1 recorded with its own binary (663 satisfied, 10 failed in the red file, 0 refused; 381 / 157 / 179 / 0).
At the end every one of these must still hold, plus the additions, unless a defect fix is logged under `## Changes to existing modules` in NOTES.md.

## plan

1. `units.py` counts the units of the text from the raw file (354).
2. `dispositions.txt` gives one disposition per unit; `coverage.py` checks that every unit has exactly one and prints the coverage table and the counts.
3. NOTES.md: `## Re-disposition audit` first, then new modules, tests, bookkeeping.

## decisions taken (design, written before the new L4)

- **Units.** `units.py RAW` prints 354 units: title block 3, group headings 35, sections 23, subsections 83, paragraphs 56, subparagraphs 5, closing words 3, s 2(1)/s 35(1) definition entries 56, definition paragraphs 31, definition closing 1, repealed definition entries 5, Schedule heading 1, Schedule rows 51, Related Provisions item 1.
  104 marginal notes are labels of their provisions, not units (s 14 of the Act: marginal notes form no part of the enactment); the audit says so and keeps the count visible.
- **Disposition rule for `fork`** (uniform): a unit is `fork` when the fork register has an entry whose licensing text is that unit and whose readings give different outcomes; the row points at the entry and at the rule that encodes the chosen reading (or the named refusal).
  Encoder conventions (F-LANG, F-TARGET, F-NEGATIVE, F-BOUNDS, F-HOLIDAYS) and silences (F-WEEK, F-SERVICE) are register entries of class B and make no unit a fork.
  Pass 1 marked fork-bearing rows `encoded`; they move to `fork` where the rule says so.
- **`not applicable` is not a disposition.** s 1 (short title) is inert reason 2; Related Provisions (1998, c. 30, s. 10) is inert reason 2 (a transitional provision for proceedings begun before 1998 amendments commenced; it affects no one now: a judgment, said in the audit).
- **Tooling.** `dispositions.txt` (regex on unit id -> disposition, reason, forks, rule names, test file, relation key); `coverage.py` joins it to `units.py`, refuses to emit unless every unit has exactly one line, checks that each cited rule name occurs in its module and each cited test heading occurs in its test file, and prints the coverage table, counts and the jural-relations table.
- **New modules** (names match the srcrefs gate glob `ca-interpretation-*.l4`; tests `ca-tests-*.l4`):
  1. `ca-interpretation-nouns.l4` (nouns only: kinds of instrument, parts of an enactment, grammatical features, ways of citing), imported by 2 to 4.
  2. `ca-interpretation-definitions.l4`: s 2(1) and s 35(1): a table `the definition of` t (form, members named, what it points at) plus predicates for fact-based terms (bank, broadcasting, public officer, oath, province, holiday kinds, lieutenant governor in council by place, superior court by place, the zones by state).
  3. `ca-interpretation-reading.l4`: ss 3(2), 3(3), 4, 5(1), 8(3), 8.1, 8.3, 10, 12, 13, 14, 15, 16, 18(1)(2), 21(2), 25(2), 33, 36, 38, 40, 41(2)-(5), 42, 45.
  4. `ca-interpretation-powers.l4`: ss 23(4), 24, 31, 34.1.
  Tests: `ca-tests-definitions.l4`, `ca-tests-reading.l4`, `ca-tests-powers.l4`.
- **A rule with a stated condition and no stated alternative returns `REFUSE` for the other case** (pass-1 F-NEGATIVE); a `FALSE` is used only where the text itself says "shall not be deemed" / "does not include" / "need not".
- **Mixfix traps (pass-1 NOTES section 8):** a head that ENDS with a keyword is not recognised across an import; two operators sharing a head keyword clash. Grep existing heads before naming.
- Not done on purpose: no seat layer is added (the brief asks for none); NOTES.md says so under what would need doing.

## sections done / in progress / next

Pass 2, 2026-10-29. Everything in the plan is written and checked.

**Done**

- Audit (`## Re-disposition audit` in NOTES.md), written before any new L4: 354 units, 39 with no pass-1 row, all 30 pass-1 inert rows moved.
- `ca-interpretation-nouns.l4`; `ca-interpretation-reading.l4` (23 sections); `ca-interpretation-powers.l4` (ss 23(4), 24, 31, 34.1); `ca-interpretation-definitions.l4` (every defined term of ss 2(1) and 35(1) that pass 1 did not encode; the chapeaux).
- `ca-tests-definitions.l4` (279), `ca-tests-reading.l4` (152), `ca-tests-powers.l4` (49), `ca-tests-schedule.l4` (55, generated from the text).
- `dispositions.txt`, `relations.txt`, `units.py`, `coverage.py`: `coverage.py check --strict` gives 354 units, 0 problems.
- NOTES.md rebuilt (audit, coverage table of 354 rows, jural relations, findings, fork register with 8 new class A entries, check.sh output); `encoding.json` 0.2.0; `SOURCE-LICENSE.md` points at the stub; `check-output.txt` refreshed.
- `_probes/` deleted; no scratch file left in this folder.
- Final `check.sh`: 20 modules, 1198 satisfied, 10 failed (all in `ca-tests-red.l4`, expected 10), 0 refused, srcrefs 608 / 311 / 347 / 0 problems, exit 0.

**In progress**: nothing.

**Next**: nothing for this run; the final report goes to the team lead.

**Decisions taken in the writing (with the section that licenses each)**

- Section 3(2) is read as flat (F-3-2): s 3(1) has "unless a contrary intention appears" and s 3(2) does not.
- "Queen's" is read as the body now styled for the King in s 25(2), s 35(1) "Governor in Council" and s 35(1) "superior court" (c) (F-QUEENS).
- "As amended" in s 40(2) is read as amended up to the day the citation is read and applied (F-40-2-DATE).
- An `includes` definition answers a refusal for a thing it does not name; a `means` definition answers FALSE (s 35(1)).
- A mixfix head always ends on a parameter (the keyword trap of pass 1, hit again).


## Pass 1 (kept for the record)


Updated: see the timestamp at the foot of this file.

## Plan (decided before any L4 was written)

1. NOTES.md first: coverage table (every section, subsection group and the Schedule), answer table with the EXPECTED values for the worked cases, written from the text before any module existed.
2. `ca-interpretation-time.l4`: the reusable time module (imports only `prelude` and `daydate`).
3. `ca-interpretation-calendar.l4`: ss 29, 35(1) "holiday" and "standard time" helpers (imports the time module).
4. `ca-interpretation-repeal.l4`: ss 2(2), 39(2), 42-46.
5. `ca-interpretation-rules.l4`: the other computable rules (ss 3, 8, 9, 11, 17, 19, 20, 22, 23(1), 25, 31, 32, 34, 36, 41(1) ...).
6. Tests: `ca-tests-*.l4`; deliberately failing expectations only in `ca-tests-red.l4`.
7. `check.sh` with `L4_TARGET=unstable` (the brief never names a target; it requires `REFUSE`, `@lang en` and `#ASSERT REFUSED`, which `main` does not read).
8. `encoding.json`, `SOURCE-LICENSE.md`, final report.

## Decisions taken (with the licensing text)

- Holidays, days of rest and recess are an INPUT (a function `DATE -> BOOLEAN`), never computed in the time module (brief).
- "From a day" and "after a day" exclude that day: s 27(4), s 27(5); s 28(b) for months.
- A year is twelve consecutive months (s 37(1)), so N years after a day is s 28 with 12N months.
- Weeks: the text has no provision (no occurrence of "week"); named REFUSE.
- Commencement: the day is s 5(2) / s 6(1); the moment is "the expiration of the previous day" (s 6(1), s 6(2)).
- s 26 moves the last day on which a thing may be done, not the period; it names "holiday" only (Saturday is not a holiday in s 35(1)).

## Sections done

All modules WRITTEN, typecheck clean (one Hint each: the linter says `@lang en` can go, which the brief requires, so it stays), `srcrefs.py check --strict` clean:

- `ca-interpretation-time.l4`: ss 2(1) "regulation", 5, 6, 7, 18(3), 23(2)(3)(5), 26, 27, 28, 30, 35(1) "month", 37, 39(1), weeks/service refusals.
- `ca-interpretation-calendar.l4`: s 35(1) "holiday" (the three days the text dates, the rest an input), "commencement", "standard time", "local time", s 29.
- `ca-interpretation-repeal.l4`: ss 2(2), 39(2), 43, 44, 46.
- `ca-interpretation-rules.l4`: ss 3(1), 8(1) 8(2) 8(2.1) 8(2.2) 8.2, 9, 11, 17, 19, 20, 21, 22, 23(1), 25(1), 32, 34, 35(1) "corporation" and "security", 41(1), Schedule, 35(2).
- Tests, all passing: `ca-tests-periods.l4` (193), `ca-tests-counting.l4` (73), `ca-tests-holidays.l4` (105), `ca-tests-commencement.l4` (60), `ca-tests-other.l4` (59), `ca-tests-rules.l4` (120), `ca-tests-repeal.l4` (53); `ca-tests-red.l4`: ten deliberately failing expectations, `expected_failed` = 10 in check.sh.
- check.sh: `expected_failed` set; the `srcrefs.py check --strict` step added (raw text from SRC_TXT or `../../source/`).

## Sections in progress

None. Everything in the plan is written.

## Done

- NOTES.md complete: sections 0 to 8 (source, what is encoded, coverage table of 94 rows, 36 forks, expected answers, answer table, the real check.sh output, open questions, process notes).
- `encoding.json` and `SOURCE-LICENSE.md` written; the licence question is recorded as open, not decided.
- `_probes/` deleted; no `zz-*.l4` left.
- Final check.sh run saved in `check-output.txt`: 12 modules, 663 satisfied, 10 failed (all in `ca-tests-red.l4`, expected 10), 0 refused, 0 other errors; srcrefs gate 381 quotation lines, 0 problems; exit 0.

## Next

Nothing, for this run. Final report to the team lead.

## Files written

Pass 1: BRIEF-pass1.md (copy of the pass-1 brief), check.sh and srcrefs.py (from the encoding-a-subject skill; check.sh edited as above), requote.py, `ca-interpretation-{time,calendar,repeal,rules}.l4`, `ca-tests-{periods,counting,holidays,commencement,other,rules,repeal,red}.l4`, NOTES.md, encoding.json, SOURCE-LICENSE.md, check-output.txt, this file.
Pass 2 added: `ca-interpretation-{nouns,reading,powers,definitions}.l4`, `ca-tests-{definitions,reading,powers,schedule}.l4`, `units.py`, `coverage.py`, `dispositions.txt`, `relations.txt`; and rewrote NOTES.md, encoding.json, SOURCE-LICENSE.md, check-output.txt and this file.
Pass 3 added: `ca-interpretation-{commencement,resolutions}.l4`, `ca-tests-{transition,resolutions}.l4`; edited `ca-interpretation-{time,rules,definitions,powers,reading}.l4`, `ca-tests-{other,rules,definitions,reading}.l4`, `dispositions.txt`, `relations.txt`, NOTES.md, encoding.json, SOURCE-LICENSE.md, check-output.txt and this file.
No pass-1 module or test was edited in pass 2; pass 3 edited two modules and two tests, logged in NOTES.md under `## Changes to existing modules`.
last update: 2026-10-29 (after the pass-3 check.sh run)
