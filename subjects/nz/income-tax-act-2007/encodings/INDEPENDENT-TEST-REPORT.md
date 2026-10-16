# Independent test pass — Income Tax Act 2007, personal income tax

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and the provisions in scope in `../registers/source-bundle/act_public_2007_97.txt` (and IA 2-IA 4, LE 3 for context), wrote `independent-expectations.md` (about 110 scenarios) from those alone, and only then opened the rule modules (not `it-tests.l4` or `NOTES.md`) to learn their names and wrote `tests-independent.l4`. It changed no expected value after reading the encoding (it corrected one arithmetic slip, L24, before opening it).

## Result as first run

120 assertions: **120 satisfied, 0 failed**.

## Findings without a failing assertion

| finding | provision | outcome |
| --- | --- | --- |
| The non-resident visitor test checked only YD 1B(2)(b)-(e): a person failing (f) family scheme, (g) lawful presence or (h) foreign residence or citizenship-based tax was still a visitor | s YD 1B(2)(f)-(h) | **fixed**: three new inputs, required for visitor status |
| Donation credits were pooled with other refundable credits and used against the liability | s LD 1(5): "excluded from the application of sections LA 2 to LA 6" | **fixed**: a separate input, refunded whole; family credits under LA 7 still go through LA 4 (the Act excludes only donation credits) |

## Not expressible (recorded in `independent-expectations.md`)

Part-day counting (R13-R15: day counts are inputs); YD 1(9C) and YD 1B(3)-(5) (R29-R31); trustees (R32); fractional dollars (L26: whole dollars are taxed, fork F1); the flat rates for other persons in Schedule 1 cls 2-7, 15-16 (F01-F09: carried as text); the two limbs of LC 13(1)(d) separately (X05-X06); supplementary dividends without figures (U14); R&D credits (U15); the refused M and ME codes (T10).

## After the fixes

The `Residence facts` and `Credits` constructions in the independent file were ported to the new fields (TRUE and 0, marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 120 satisfied, 0 failed; `it-tests.l4` 63 satisfied; 8 modules, 183 satisfied, 0 failed, 0 other errors.
