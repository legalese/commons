# PROGRESS (legalese-sonnet-5.5, State Pension Regulations 2015, S.I. 2015/173)

Run: porridge-uk-spr-b. One Sonnet 5.5 agent, working alone. Binary: stable `l4` 1.6.98.
Source: `uksi-2015-173.txt` (583 lines, version 2026-04-06). Authoring aid (outside the deposit): `INPUTS_DIR/work/` holds throwaway scripts; `expand.py` replaces `@@Q n m` lines in a `.l4` by `srcrefs.py quote` output once, so the quotations are copied from the text by script and the `.l4` is then the only source. The work directory is deleted before the final report.

## Plan (written 2026-10-22 before any L4)

Layer 1, one module per Part or natural group (flat folder, ASCII `spr-` names, no name defined twice across modules):

| module | text | lines of the source |
| --- | --- | --- |
| spr-nouns.l4 | shared nouns only (manner of giving notice, kind of choice, period) | n/a |
| spr-part1-general.l4 | preamble dates, reg 1 (1)-(5), Part 1A reg 1A (full rate) | 1-25 |
| spr-part2-prisoners.l4 | regs 2, 3 | 26-44 |
| spr-part3-deferral.l4 | regs 4-12A | 45-139 |
| spr-part4-qualifying-years.l4 | reg 13 | 140-143 |
| spr-part5-sharing.l4 | reg 14, Schedule paras 1-2 (what they mean for the person: inserted reg 6 timings) | 144-146, 519-583 |
| spr-part6-graduated.l4 | regs 15-20 | 147-273 |
| spr-part7-overseas.l4 | regs 21-23 | 274-307 |
| spr-part8-credits-general.l4 | regs 24-28 (interpretation, general, Chapter 2) | 308-352 |
| spr-part8-credits-post2016.l4 | regs 29-39 (Chapter 3) | 353-517 |

Layer 2: spr-seat.l4 (the person who is or will become entitled), spr-cases-seat.l4.
Tests for layer 1: spr-tests-*.l4 (one per module).

## Status (updated 2026-10-22, at the end of the run)

- [x] read brief, skills, text
- [x] spr-nouns.l4 (all Parts' nouns)
- [x] Part 1 and 1A: spr-part1-general.l4 + spr-tests-part1.l4 (23 assertions)
- [x] Part 2: spr-part2-prisoners.l4 + tests (34)
- [x] Part 3: spr-part3-deferral.l4 + tests (115)
- [x] Part 4: spr-part4-qualifying-years.l4 + tests (9)
- [x] Part 5 and the Schedule: spr-part5-sharing.l4 + tests (15)
- [x] Part 6: spr-part6-graduated.l4 + tests (94)
- [x] Part 7: spr-part7-overseas.l4 + tests (36)
- [x] Part 8, Chapters 1-2: spr-part8-credits-general.l4 + tests (49)
- [x] Part 8, Chapter 3: spr-part8-credits-post2016.l4 + tests (165)
- [x] coverage table: no row left `deferred` (162 encoded, 37 inert, 1 repealed or blank, 0 not applicable)
- [x] layer 2: spr-seat.l4 (59 questions, ten headings) and spr-cases-seat.l4 (every question has at least one case)
- [x] check.sh extended (warn and written columns); NOTES.md all sections; encoding.json; SOURCE-LICENSE.md; BRIEF.md copy
- [x] final check.sh and srcrefs run; INPUTS_DIR/work deleted

## Slips in the hand-written seat cases, caught on the first run (log, 2026-10-22)

The brief says a failing assertion is a finding and expectations are not edited to match output.
Two slips (four failing assertions in all) in `spr-cases-seat.l4` on first runs were mine, in the case, and neither moved the encoding:
1. The case for "From what date was I entitled to make my choice" expected the death date (1 March 2020) when my own comment said "the later of" my pensionable age (1 June 2025) and the death.
   1 June 2025 is later, so the encoding was right and my arithmetic was wrong.
   I changed the case's inputs (the pensionable age to 1 January 2019, so the death is the later), keeping the expectation the text gives; a second case with the death earlier was already there.
2. Three cases for regulation 30 (working tax credit) were written with the helper's default "it is paid to me" as false for a single person.
   Regulation 30(1) applies to a person to whom the credit is paid; the default is now true, and a new case asserts the couple case where it is paid to the other member (reg 30(2)(a)), which the encoding already answered as the text reads.
These were found only because the cases are run; they are a reminder that all cases here come from one author.

## Decisions taken (with the licensing text)

See the fork register in NOTES.md (F1 to F27 and F9b) for every reading taken and the words that license it.

## Files written

All under `deposit/encodings/legalese-sonnet-5.5/`: ten layer-1 modules (`spr-nouns.l4`, `spr-part1-general.l4`, `spr-part2-prisoners.l4`, `spr-part3-deferral.l4`, `spr-part4-qualifying-years.l4`, `spr-part5-sharing.l4`, `spr-part6-graduated.l4`, `spr-part7-overseas.l4`, `spr-part8-credits-general.l4`, `spr-part8-credits-post2016.l4`), nine test files (`spr-tests-part*.l4`), the seat (`spr-seat.l4`, `spr-cases-seat.l4`), `check.sh`, `srcrefs.py`, `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.
