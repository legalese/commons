# Independent test pass — Tax Administration Act 1994

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md`, the provisions in scope in `../registers/source-bundle/act_public_1994_166.txt` and the Income Tax Act definitions the brief names, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `taa-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. The session was interrupted by a usage limit after the expectations were written and resumed with them unchanged. It changed no expected value after reading the encoding.

## Result as first run

157 assertions: **155 satisfied, 2 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 220 | SP3: unacceptable tax position, $10,000 shortfall | s 141B(1D) | no penalty | $2,000 | **fixed**: an unacceptable income tax position is penalised only where the shortfall is more than both $50,000 and 1% of the total tax figure |
| 223 | SP6: unacceptable tax position, $50,000 shortfall | s 141B(1D) | no penalty | $10,000 | **fixed**: as SP3 |

## Not expressible (recorded in `independent-expectations.md`)

PAYE intermediaries (EG8); s 23M's "intending that the cessation is permanent" (CE5); the 0.45 tax amount itself (NN8); s 108 as a yes/no on a date (TB4); s 139A(5)-(9) notices and the $250 monthly maximum (LF9-LF11); the details of s 141FB disqualification (PB1-PB6); s 141A(3) reliance on a tax adviser (RA1-RA2). The 1% total tax figure limb (SP7-SP8) became expressible with the fix.

## Differences the author noted without a failing assertion

1. The timing of the 4% initial penalty: the author left the 6th day unasserted. **Changed by the encoder before commit**: the 4% is added at the end of that day, so a payment on it comes in time (fork F4).
2. How the s 141G, 141H and 141I reductions combine (the encoding takes the larger; the author would combine them): recorded as fork F5.
3. No input for an "unacceptable interpretation" (s 141G(3)(a)(i), s 141J): a known limit.
4. The early balance date relies on the caller's tax year: a known limit.
5. The top-level goal's late filing test ignores any extension: a known limit.

## After the fixes

The `Shortfall facts` constructions in the independent file were ported to the two new fields (TRUE and 0, marked `[Ported …]`; no expected value changed). The encoder's test of a $10,000 unacceptable tax position was changed and marked, and tests of the threshold added. `check.sh`: `tests-independent.l4` 157 satisfied, 0 failed; `taa-tests.l4` 97 satisfied; 8 modules, 254 satisfied, 0 failed, 0 other errors.
