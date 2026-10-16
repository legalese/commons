# Independent test pass — Credit Contracts and Consumer Finance Act 2003

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md`, the provisions in scope in `../registers/source-bundle/act_public_2003_52.txt` and Legislation Act 2019 ss 54-56, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `cccfa-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

162 assertions: **159 satisfied, 3 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 111 | D09: a non-revolving statement opening 31 August 2026 | s 18(2)(b); Legislation Act s 56 | may close 28 February 2027 | 27 February 2027 | **fixed**: the s 56 month rule |
| 235 | A08: previous application 10 February 2026, new one 10 June 2026 | s 55(3)(a); Legislation Act ss 54, 56 | not allowed (first allowed 11 June) | allowed | **fixed** (fork F6): the 4 months run from the day after the previous application |
| 281 | K10: information requested after the s 57A(1)(b) deadline | s 57A(2) | no extension | extended | **fixed**: only a request "in accordance with subsection (1)(b)" extends the time |

## Not expressible (recorded in `independent-expectations.md`)

Whether a s 40 term is permitted (R01-R05: only the base for default interest is computed); what the first advance excludes (E05); the s 45F/45G defence and the s 29, s 45I and s 57 limbs folded into single inputs (F06, F07, C37-C41, Q02, B04); s 45H prepayments and default fees (P05, P06); sums of non-simultaneous breaches and unlisted provisions under s 89 (S27-S29).

## Differences noted without an assertion

s 39 takes rates as fractions and s 45C as percentages; s 45E's further costs are floored at 0 (no s 48 refund figure); s 57A(2) refuses if information was requested and never received; the $6,000 for revolving credit without a limit is applied only to the "any other breach" limb (the author's reading too).

## After the fixes

`check.sh`: `tests-independent.l4` 162 satisfied, 0 failed; `cccfa-tests.l4` 61 satisfied; 9 modules, 223 satisfied, 0 failed, 0 other errors. The encoder's test of a further hardship application exactly 4 months later was changed (fork F6) and marked; tests of the s 56 month end and the late information request were added.
