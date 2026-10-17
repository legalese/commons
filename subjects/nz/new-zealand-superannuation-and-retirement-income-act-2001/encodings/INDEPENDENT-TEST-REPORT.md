# Independent test pass — New Zealand Superannuation and Retirement Income Act 2001

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_2001_84.txt`, wrote `independent-expectations.md` from those alone (about 130 scenarios), and only then opened the rule modules (not `nzs-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

116 assertions: **112 satisfied, 4 failed**.

| scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- |
| the Pacific rate with fewer than 10 years' residence | s 32(1) | refused | 0 | **fixed**: s 32 gives no rate below 10 years, so the encoding refuses |
| the s 8 example person, meeting the requirement on 1 July 2036, applying 1 January 2036 | s 11(1) | commences 1 July 2036 | 1 January 2036 | **fixed**: new input `residential qualification first met on, if after 65`; commencement is the latest of the 65th birthday, that day and the application |
| the s 8A refugee example (arrived at 50 on 1 January 2025) | s 8A(3)(a) | 15 years | 14.998 years | **fixed** (fork F1 changed): whole calendar years, with only remaining days divided by 365.25 |
| born 29 February 1960, assessed 28 February 2025 | s 7 | 64 (65 on 1 March) | 65 (on 28 February) | **kept** as fork F6: the Act is silent and the author's view is weak; 1 assertion stays failing as a recorded disagreement |

## Not expressible (recorded in `independent-expectations.md`)

The limbs of s 4A; s 17(2)(b)-(c); s 19(1), (5), (7)-(9); s 22's exclusion of people paid under s 26; who counts under s 23; s 24's displacement condition; s 25; when ss 26 and 31 apply and the 26- and 52-week tests; the s 26(6) amount itself (proportion × rate); s 32(1)(c); s 33 commencement; s 8(1)(a)'s s 31(4) exception; s 15 adjustment; and absence in the top-level goal. These are listed in `NOTES.md` as inputs or text.

## After the fixes

The `Applicant` constructions in the independent file were ported to the new field (NOTHING, and the date the D4 scenario gives in that one call, marked `[Ported …]`; no expected value changed). The encoder's tests that encoded the rejected readings (the refugee years, the Pacific rate below 10 years) were changed and marked. `check.sh`: `tests-independent.l4` 115 satisfied, 1 failed (the F6 disagreement); `nzs-tests.l4` 78 satisfied; all 7 modules 193 satisfied, 1 failed, 0 other errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the latest date for the Fund's next performance review (s 71(3)). No independent assertion was affected. `check.sh`: `tests-independent.l4` 115 satisfied, 1 failed.
