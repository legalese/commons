# Progress

Encoding of the Paid Parental Leave Act 2010 (Commonwealth), Chapter 2 Parts 2-1 to 2-3 Division 4 (sections 7 to 44), from compilation C2026C00425.

## Done

- Part 2-1 (sections 7 to 11D): `ppl-key-provisions.l4`, with section 11D in `ppl-time.l4`.
- Part 2-2 (sections 12 to 29): `ppl-determinations.l4`, with the dates and counts in `ppl-time.l4`.
- Part 2-3 Division 1 (section 30): a guide, not operative.
- Part 2-3 Division 2 (sections 31AA to 31A): `ppl-eligibility.l4`, with the limits and the waiting period count in `ppl-time.l4`.
- Part 2-3 Division 3 (sections 32 to 36AA): `ppl-work-test.l4`, with the work test period in `ppl-time.l4`.
- Part 2-3 Division 4 (sections 37 to 44): `ppl-income-test.l4` and `ppl-time.l4`.
- The Dictionary entries those provisions use: `ppl-definitions.l4`.
- The provision index and the cross-reference rows: `ppl-provisions.l4`, `ppl-xrefs.l4`.
- The seat layer: `ppl-seat.l4` and `ppl-cases-seat.l4`.
- `NOTES.md`, `encoding.json` and `SOURCE-LICENSE.md`.

## In progress

Nothing.
Every module and case file runs clean on the writing build and on the main build, and the source-reference checker reports no problems.

## Next

The items in the last section of `NOTES.md`: expert reading against the authorised text, the PPL rules as inputs, Divisions 5 and 6 and Part 2-4, the Consumer Price Index numbers, rulings on the forks, and a wider work test form.

## Decisions taken

Each is a fork-register entry or a convention in `NOTES.md`, with the licensing section named there; the main ones, with the section that licenses each:

- A rule answers `JUST TRUE` or `JUST FALSE` where the text says so in its own words and `NOTHING` where it is silent (the rulings in the brief).
- A bar answers `JUST FALSE` when it applies and `NOTHING` when it does not (sections 11B, 11C, 18, 19B, 20, 21).
- A duty or a grant stated with an unmet "if" answers `NOTHING`; sections 13(6) and 14(4) answer `JUST FALSE` because the text states the converse (F20).
- "The Secretary is satisfied that X" is X on the facts as stated (sections 13(2), 14(2), 26A; F2).
- Hours counted on an ordinary day: paid work plus paid leave, each only if at least one hour (section 34(1)(a)-(b); F9).
- 104 weeks is 728 days (section 31A(2)-(4); F6).
- "Between 1 July X and 30 June Y" includes both days (section 31ABA; F7).
- Facts the Act borrows from other instruments are inputs (sections 31A, 34, 35, 38, 43 and the Dictionary).

## How the files were made

Written by hand: the rule modules, the record declarations, the hand-derived expected values, and the seat questions.
Assembled by script from hand-written parts: the Dictionary table in `ppl-definitions.l4`, the quoted `-- src:` lines above each `@ref`, the tests that vary one field of a base record, the cases of the eligibility question, `ppl-provisions.l4` and `ppl-xrefs.l4`, and the coverage table and the fork register in `NOTES.md`.
The scripts are kept outside this folder.

## Files written

`ppl-provisions.l4`, `ppl-xrefs.l4`, `ppl-logic.l4`, `ppl-time.l4`, `ppl-nouns.l4`, `ppl-definitions.l4`, `ppl-key-provisions.l4`, `ppl-determinations.l4`, `ppl-eligibility.l4`, `ppl-work-test.l4`, `ppl-income-test.l4`, `ppl-seat.l4`, with `ppl-tests-logic.l4`, `ppl-tests-time.l4`, `ppl-tests-definitions.l4`, `ppl-tests-key-provisions.l4`, `ppl-tests-determinations.l4`, `ppl-tests-eligibility.l4`, `ppl-tests-work-test.l4`, `ppl-tests-income-test.l4` and `ppl-cases-seat.l4`; `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`.

## Facts established on the writing binary

- `Date day month year` rolls an impossible day forward: `Date 29 2 2023` is 1 March 2023.
- `DATE PLUS n` and `DATE MINUS n` give a date.
- `x MODULO y` needs integers.
- `WITH` constructs a record and does not update one.
- The binary-specific limits are listed in `NOTES.md`.
