# Independent test pass — Electricity Industry Act 2010

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md`, the provisions in scope in `../registers/source-bundle/act_public_2010_116.txt` and Legislation Act 2019 ss 13, 54-56, wrote `independent-expectations.md` (about 100 scenarios) from those alone, and only then opened the rule modules (not `eia-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

82 assertions: **80 satisfied, 2 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 70 | S33: notice on 1 January 2026 | s 107(1); Legislation Act ss 54, 56 | earliest supply 2 July 2026 | 1 July 2026 | **fixed** (fork F1): 6 months run from the day after the notice |
| 74 | S35: notice on 31 August 2026 | s 107(1); Legislation Act s 56 | earliest supply 1 March 2027 | 28 February 2027 | **fixed**: the period ends at the close of 28 February |

## Found without a failing assertion

- **A working-day bug shared with other encodings**: for a Sunday 1 January, Legislation Act s 13(d) excludes Monday 2 and Tuesday 3 January, but the module excluded 3 and 4 January (so Wednesday 4 January 2023 was wrongly a non-working day). **Fixed** here and in the Customs and Excise, CCCFA, Employment Relations and Telecommunications encodings, with regression tests.
- s 80(3)(b)(i) applies 3 times the gain only if the court is satisfied the contravention produced a commercial gain: **fixed**, a new input.
- The s 96(2) and s 105(4) fines return 0 or a maximum rather than a refusal; a known limit.

## Not expressible (recorded in `independent-expectations.md`)

The parts of s 106(1)(a) (one input); the mode of supply (S16, S17); "made aware" in s 105(4)(a) (S20); the fine's link to an offence (S29); who received the s 107 notice and s 107(3) (S36-S40); the s 96(3)(b) Gazette requirements (D15, D16); s 54(3) related breaches (E16, E17); s 66 extensions (E42).

## After the fixes

`Part 3 contravener` gained an input; the independent file's constructions were ported (TRUE, marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 82 satisfied, 0 failed; `eia-tests.l4` 45 satisfied; 8 modules, 127 satisfied, 0 failed, 0 other errors.
