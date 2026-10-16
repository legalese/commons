# Independent test pass — Customs and Excise Act 2018

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md`, the provisions in scope in `../registers/source-bundle/act_public_2018_4.txt` and the Legislation Act 2019 working day, wrote `independent-expectations.md` (about 100 scenarios) from those alone, and only then opened the rule modules (not `cea-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

100 assertions: **99 satisfied, 1 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 251 | F8: duty paid 16 March 2026; the 4 years end on Saturday 16 March 2030; application Monday 18 March 2030 | s 142(1)(b); Legislation Act 2019 s 55 | refund due | not due | **fixed**: s 55 lets a thing to be done within a period be done on the next working day when the last day is not one |

## Gaps found without a failing assertion

- **s 124(7)** (an earlier time for payment by notice) had no payment occasion, though s 160(5) applies s 159 to it: **fixed**, a new occasion.
- cl 4(4) (the chief executive must first seek an explanation before leaving the transaction value for doubt): folded into the input; a known limit.

## Not expressible (recorded in `independent-expectations.md`)

The sub-limbs of related persons and of cl 5's exceptions (single inputs); the choice of qualifying cl 7 amounts (the caller supplies them); cl 9 before cl 10, and the cl 2(3) preference for the same producer (M8-M11: one list of values); excise under Schedule 3 (L13); the s 143(1) conditions (V4-V6); the choice between review and appeal (A4, A7); M7 (refused, as the author expected, not asserted).

## After the fixes

`Refund facts` gained a Matariki list for s 55; the independent file's construction was ported (EMPTY, marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 100 satisfied, 0 failed; `cea-tests.l4` 52 satisfied; 8 modules, 152 satisfied, 0 failed, 0 other errors.
