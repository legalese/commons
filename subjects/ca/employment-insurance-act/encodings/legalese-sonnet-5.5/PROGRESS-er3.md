# PROGRESS: piece er3 (Regulations 35 to 57, lines 540-992 of SOR-96-332.txt)

State at delivery. After any compaction: re-read this file, NOTES.md and the text, not a summary.

## How the files were made
- The `er3-*.l4` files were generated from templates by a script that copied the quotation lines from `SOR-96-332.txt`.
- The templates and the script were scratch files under `inputs/work/`. That directory has been deleted, so the `.l4` files and NOTES.md in this folder are the only copies: edit them directly.
- Gates, run in this folder: `L4=<stable l4 1.6.98> L4_TARGET=unstable ./check.sh` and `python3 -I srcrefs.py check --refs SOR-96-332.txt er3-*.l4`.

## Status (last run: check.sh exit 0, srcrefs 0 problems)
- Layer 1: er3-nouns, er3-earnings (reg 35), er3-allocation (36), er3-plans (37, 38), er3-waiting-period (39, 39.1), er3-sickness-pregnancy (40, 41, 41.2), er3-division (41.6), er3-work-sharing (42-49), er3-measures-and-leaving (50, 51, 51.1), er3-work-stoppage (52, 53), er3-outside-canada (54, 55, 55.01), er3-information (55.1, 55.2), er3-recovery (56, 56.1, 57). Each has an `er3-tests-<name>.l4` (er3-nouns has none; it holds only enums).
- Layer 2: `er3-seat.l4` (91 questions under 18 `§` headings, each with `@export` and `@desc`) and `er3-cases-seat.l4` (200 assertions, at least one case for every question, and a NOTHING case for every question that returns a MAYBE).
- check.sh: 31 modules, 987 assertions satisfied (787 in the layer-1 tests, 200 in the seat cases), 0 errors, 0 failed, 0 refused.
- NOTES.md: the ten headings of the brief; coverage table of 239 rows; fork register F1 to F20; 57 cross-reference rows; 13 numbered findings.

## Decisions taken (assumed, not ruled; each is a fork in NOTES.md)
F1 reg 35(8) "is not a group plan if" read as the whole test; F2 reg 35(2)(a)-(f) brought in whether or not from an employment; F3 order among overlapping reg 36 subsections; F4 weeks "falling within" a period (input); F5 vacation pay that does not fit (reported, not allocated); F6 "$5,000 or 80%" either; F7 52 weeks after the benefit period starts: after the day, up to 364 days; F8 reg 36(17) sum truncated to the terms supplied; F9 reg 36(20) rounding applied to each amount; F10 reg 39.1(c) strictly after the commencement day; F11 "regular or usual employment or other suitable employment" = incapable of both; F12 reg 40(5): 19 weeks or fewer; F13 reg 41(1)(b) only after the birth; F14 reg 53(2)(a) work-force or activity; F15 reg 55(1.1) only funeral and visit of the same person cumulate; F16 reg 55(5)(a) or (b); F17 reg 55.2 (a) and (b) both; F18 reg 56.1(3) day counts are inputs (the seat cases use 365, assumed); F19 interest: the day of the event is the first day without interest; F20 the Commission's "may" (and reg 51(1)'s "may be paid"): the rules answer whether the conditions are met.

## Files in this folder
NOTES.md and PROGRESS.md (written for this piece); check.sh and srcrefs.py (supplied, not edited); the keel files eia-core.l4, eia-core-insurable-employment.l4, eia-core-interpretation.l4 and eia-core-maximum-earnings.l4 (not edited); er3-nouns.l4, er3-earnings.l4, er3-allocation.l4, er3-plans.l4, er3-waiting-period.l4, er3-sickness-pregnancy.l4, er3-division.l4, er3-work-sharing.l4, er3-measures-and-leaving.l4, er3-work-stoppage.l4, er3-outside-canada.l4, er3-information.l4, er3-recovery.l4, the twelve er3-tests-*.l4 files, er3-seat.l4 and er3-cases-seat.l4.

## Open
Done. After the advisor's review the @export wording of six seat questions in er3-seat.l4 was corrected (Q62 and Q63 polarity, Q50, Q78, Q85, Q87; no rule, input or decision name changed), and check.sh (exit 0, 31 modules, 987 satisfied, the same table as in NOTES.md) and the srcrefs gate (0 problems) were rerun after that last .l4 edit.
Nothing is waiting on a decision. What remains is the lead's review and the points in NOTES.md "Before this is worth relying on".
