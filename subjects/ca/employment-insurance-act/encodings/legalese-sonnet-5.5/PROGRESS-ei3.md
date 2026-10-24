# PROGRESS: piece ei3 (Act lines 1127-1803: Parts III, IV, V)

Working log of the `ei3` agent (Sonnet 5.5), 2026-10-24.
Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Working method

- The Act's lines are quoted by a helper that reads the raw file: a marker line `--@@ N M` in a draft `.l4` is expanded in place by `../../registers/source-bundle/ei3-expand.py` (it calls `srcrefs.py quote`).
- Commands: `L4=<L4_BIN>`; run each file with `$L4 run FILE`; whole folder with `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`; citations with `python3 -I srcrefs.py check --refs <Act raw file> ei3-*.l4`.
- Throwaway probe files are named `ei3-probe-*.l4` and must be deleted before the end.

## Decisions taken (with the text that licenses each)

1. One seat only (the insured person / claimant, as the brief says). Director liability (s 83), responsible representative (s 86(3), (4), (7)) and corporate officers (s 107) are encoded in layer 1 and in the Jural relations table, not asked in the seat. Questions that bind "any person" (s 88(5), s 88(2), s 88(13), s 106(4)) stay in the seat.
2. Regs Parts III and III.1 (regs 62 to 76.45, piece er4) exercise s 69; they are cross-referenced, not encoded here. The Insurable Earnings and Collection of Premiums Regulations (SOR/97-33) are not deposited, so every "prescribed" amount, time, rate or person in ss 82 to 96 is a plain input.
3. Spent provisions (s 96(6) to (8.98), s 98(2) and (3), s 73.1) are in-force text and are encoded, with the year as a literal condition.
4. Only regulation-making powers are `inert` (66.1(2), 66.2(2), 69(3), 80.1(1), 108(1)(a)-(b),(d)-(p), 109) and headings (pure titles). Official-duty and evidence subsections are encoded as small rules.
5. Refund rules return a tagged union (`ei3 Refund` ...) or `MAYBE NUMBER`; never 0 for "no refund".
6. Seat question names carry the section in the backtick name.

## Files written

Layer 1 DONE (13 modules, each with a tests file; `check.sh` 0 errors, 969 assertions satisfied in the tests files; `srcrefs.py check --refs` 0 problems):
- `ei3-part3-premium-rate.l4` (65.21-66.6), `ei3-part3-premiums.l4` (67-70.1), `ei3-part3-account.l4` (70.2-80.1)
- `ei3-part4-deduction.l4` (81-84), `ei3-part4-assessment.l4` (85-86), `ei3-part4-records-inspection.l4` (87-89), `ei3-part4-rulings-appeals.l4` (90-94)
- `ei3-part4-refunds.l4` (95-96), `ei3-part4-administration.l4` (97-102), `ei3-part4-review.l4` (103-105), `ei3-part4-offences.l4` (106-107), `ei3-part4-regulations.l4` (108)
- `ei3-part5-pilot-projects.l4` (109 inert; 110 encoded)
- NOTES.md coverage, jural and fork rows are written for every module above.

Seat layer DONE: `ei3-seat.l4` (88 questions, each `@export` + `@desc`) and `ei3-cases-seat.l4` (218 assertions, at least one case per question, checked by script).
NOTES.md is complete (all ten headings; every `<!-- ROWS -->` marker removed).
Last full run: `check.sh` (L4_TARGET=unstable) errors 0, satisfied 1187, failed 0, refused 0 over 32 modules; `srcrefs.py check --refs` 483 src lines, 0 problems.

## Sections: status

Every section of the range is DONE in layer 1 and in the NOTES coverage table (Parts III, IV, V: 65.21 to 110).

## Findings (all written up in NOTES.md)

- binary: `JUST 20%` reads as `(JUST 20)%`, write `JUST (20%)`; `x NOT EQUALS y` does not parse, write `NOT (x EQUALS y)`; a constructor pattern with a field is `WHEN ctor x THEN`, not `WHEN ctor WITH x`; `add years`/`add months` are backticked names (`add years` d n); top-level rules may be used before they are defined.
- text: s 82(8) interest quantum is prescribed (not computed); s 99(a) in the converted text reads "152. 24" (a stray space): read as s 152.24; s 66(3) "[No subsection (3)]".
- no seat questions for director (s 83), responsible representative (s 86), officers (s 107), employer-only duties.

## Next

Nothing left to write. Remaining: a last `check.sh` and `srcrefs.py` run after any change, the final report.
