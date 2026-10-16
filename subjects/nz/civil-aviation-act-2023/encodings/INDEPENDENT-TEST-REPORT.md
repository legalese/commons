# Independent test pass — Civil Aviation Act 2023, domestic carriage

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and ss 269-283 of `../registers/source-bundle/act_public_2023_10.txt`, wrote `independent-expectations.md` (about 70 scenarios) from those alone, and only then opened the rule modules (not `caa-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result

76 assertions: **76 satisfied, 0 failed**. The contestable points it agreed with: 2 years after 29 February ends on 28 February; a special contract below 10 times the fare leaves the cap (s 278); no cap for recklessness; free carriage gives a cap of 0; without arrival, the later of the expected arrival and the stop.

## Differences noted without an assertion

1. In successive carriage the contracting carrier was always answerable; s 275 makes only the carrier for the delayed stage liable. **Fixed**: a new input, with tests.
2. s 273(b): a special contract raising the limit should not bind an actual carrier that did not agree. A known limit.
3. s 278(4) (terms more favourable to the passenger) has no input. A known limit.
4. Negative amounts and missing stage information are computed rather than refused; `ought to have arrived on` is required even after arrival; s 281(2) gives only the last day. Known limits.

## Not expressible (recorded in `independent-expectations.md`)

s 278(4) (C-16, C-17); s 273(b) per carrier (C-18); the limbs folded into single inputs (L-09, L-10, A-05, A-06, A-09, A-12); the court's discretions and s 283(2)-(4), ss 274(3), 277(3), 280, 282.

## After the review

`Carrier facts` gained `carriage by successive carriers`; the independent file's constructions were ported (FALSE, marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 76 satisfied; `caa-tests.l4` 30 satisfied; 5 modules, 106 satisfied, 0 failed, 0 other errors.
