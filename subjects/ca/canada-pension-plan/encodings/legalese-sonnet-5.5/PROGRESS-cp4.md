# PROGRESS: piece cp4

Read this first after any compaction, then NOTES.md, then the text (lines 1570-2251 of the Act file). Do not trust a summary of either.
NOTES.md is the record: the coverage table, the fork register (ids F-a to F-z), the cross-references, the findings and what `check.sh` printed are all there.

## Commands

- L4 = `l4`
- check (about seven minutes): `cd <encodings folder>; L4=$L4 L4_TARGET=unstable ./check.sh`
- refs: `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/R.S.C.-1985-c.-C-8.txt cp4-*.l4`
- A single file: `perl -e 'alarm 300; exec @ARGV' $L4 run FILE | grep -E "Severity|assertion"`; never run `l4` on a file that does not exist (it hangs).

## State

- Layer 1: fifteen modules, all typecheck, srcrefs reports 0 problems; eleven test files.
  - `cp4-nouns.l4`, `cp4-pension-index.l4`, `cp4-calendar.l4`, `cp4-incapacity.l4` (helpers shared by several sections)
  - `cp4-division-tail.l4` (s 55.2(5.2)-(10), s 55.3; s 55.2(11) inert)
  - `cp4-disability-pension.l4` (s 56), `cp4-death-benefit.l4` (s 57)
  - `cp4-survivors-pension.l4` (s 58(1)-(5), (9)), `cp4-survivors-pension-offsets.l4` (s 58(6)-(8.1))
  - `cp4-childrens-benefits.l4` (s 59), `cp4-post-retirement.l4` (s 59.1, 59.2)
  - `cp4-applications.l4` (s 60, 61, 62), `cp4-survivor-remarriage.l4` (s 63, 63.1; s 64 repealed)
  - `cp4-assignment.l4` (s 65, 65.1; reg 76.1 and reg 78.2 figures cited by ID locator), `cp4-overpayment.l4` (s 66, 66.1; reg 42 and reg 46.2 figures cited)
- Layer 2: `cp4-seat.l4` (102 questions, 15 `§§` groups) and `cp4-cases-seat.l4` (176 cases, at least one per question, an asserted NOTHING for every MAYBE question but the sum of the post-retirement portions).
- NOTES.md has all ten headings filled, the coverage table has 154 rows covering the 674 non-blank lines once.
- Shared helpers carry the `cp4 ` prefix in their names, and so do the fields of the records, so that no name can collide with another piece's module.

## Decisions taken (and what licenses each)

- Rule names are `s N(x) — what it decides` (em dash); never `reg N —` (cr2's prefix).
- The Pension Index is a `LIST OF NUMBER` beginning with 1986; the flat rate benefits are recursions on the previous year (ss 56(2), 58(1.1), 59(1), 59.2); NOTHING for a year before the anchor or beyond the list.
- The day section 63.1 came into force is not in the text: a stated DATE input; the tests use an invented 1 January 1987.
- A judgment handed to the Minister ("is satisfied", "may") is a conditional input; an outcome the text leaves open is NOTHING (never FALSE, never 0).
- The fork register in NOTES.md replaces the fork lists that stood in this file before: F-k and F-s were two lettered entries for two different parts of s 58(1)(a) and are two rows there.

## Scratch

The scratch folder `deposit/_build/` (the generators of the coverage table, of NOTES.md, of three test files and of `cp4-cases-seat.l4`, and the chunks `cp4-seat.l4` was assembled from) has been deleted.
The `.l4` files in this folder are the source from here on: edit them directly.
The last full run is recorded in NOTES.md under `## What check.sh prints`: 799 assertions satisfied over 33 modules, none failed or refused, and no warning on any `cp4-*.l4` file.

## Next, if anything is reopened

1. Change a rule: re-run its test file, then the whole `check.sh`, then `srcrefs.py check`.
2. Change a seat question: edit it in `cp4-seat.l4` and add or change its case in `cp4-cases-seat.l4`.
3. Replace the stand-in date for s 63.1 once the amending Act's date is available (F-q).
