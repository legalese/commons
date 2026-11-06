# ea2 progress

Status as of the final write, checked by running `l4 run` on every file with l4-main-109 (0 errors, 0 warnings in every `ea2-*.l4`) and by `check.sh` (the numbers are in NOTES.md, "What `check.sh` prints").

## Files

| file | content | tests |
| --- | --- | --- |
| ea2-part-6a-8.l4 | ss 66A to 75 | ea2-tests-part-6a-8.l4 |
| ea2-part-9a.l4 | ss 76 to 80 | ea2-tests-part-9a.l4 |
| ea2-part-9b.l4 | ss 81 to 87 and the E1 option B hand-gathering | ea2-tests-part-9b.l4 |
| ea2-part-9c.l4 | s 87A | ea2-tests-part-9c.l4 |
| ea2-part-10-holiday-annual.l4 | ss 88, 88A | ea2-tests-part-10-holiday-annual.l4 |
| ea2-part-10-sick.l4 | ss 89, 90 | ea2-tests-part-10-sick.l4 |
| ea2-part-12-records.l4 | ss 95 to 96A | ea2-tests-part-12-records.l4 |
| ea2-part-12-returns.l4 | ss 97 to 102 | ea2-tests-part-12-returns.l4 |
| ea2-part-13.l4 | ss 103 to 107 | ea2-tests-part-13.l4 |
| ea2-part-14.l4 | ss 107A to 114 | ea2-tests-part-14.l4 |
| ea2-notification.l4 | S 200/2019 | ea2-tests-notification.l4 |
| ea2-duties.l4 | the duties as regulative rules, with `#TRACE` | ea2-tests-duties.l4 |
| ea2-seat.l4 | layer 2: 219 questions | ea2-cases-seat.l4 |
| sgia-interpretation-time.l4 | the Interpretation Act module, copied unchanged | (its own, not in this deposit) |
| NOTES.md, SEAMS-ANSWERED.md, SEAMS-FOUND.md, NEEDS-CORE.md | the write-up | |

## Done

Every section, subsection, paragraph, defined term and Notification paragraph and Schedule item of the range has one coverage row (NOTES.md, Coverage).
Layer 1, layer 2, the regulative rules, the coverage and jural-relations tables, the fork register and the findings are written.
`srcrefs.py check --refs` and `--strict` report 0 problems on every `ea2-*.l4`.
The rulings of 2026-11-05 on periods, "where" and scope limits, and on delegated definitions, defences and "until" bars, are applied across the range (NOTES.md, F18 and F19), with yes/no twins where a rule's type cannot say no.

## Decisions taken, and what licenses each

The forks F1 to F24 and the seat assumption A1 are in NOTES.md, "Fork register (ea2)", each with the readings, the one taken, and the text.
The brief governs where PLAN.md and the brief differ (the Notification is in ea2's range).

## Not done

- No second encoding in the unstable dialect (nothing in the range needs it).
- No test of a regulative value by `#ASSERT`: the main binary rejects it (NOTES.md, "What the main binary does not accept").
