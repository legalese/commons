# Independent test pass — Holidays Act 2003

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_2003_129.txt`, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `ha-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`.

## Result as first run

298 assertions: **294 satisfied, 4 failed**.

| line | scenario | expected (author) | encoding gave | provision |
| --- | --- | --- | --- | --- |
| 170 | notice on 1 Dec requiring annual holidays from 15 Dec | valid | not valid | s 19(2) "not less than 14 days' notice" |
| 258 | closedown notice on 8 Dec for a closedown from 22 Dec | valid | not valid | s 32(3) |
| 406 | notice on 1 Dec fixing an alternative holiday on 15 Dec | valid | not valid | s 57(3) |
| 564 | employment ends before the first entitlement; 2 public holidays entered for the notional holiday | $2,400 (the 8% only) | $2,800 | s 40(2)(b) "the employee is entitled to annual holidays" |

## What was done

| finding or remark | outcome |
| --- | --- |
| s 40(3) pay is added for an employee not yet entitled (line 562) | **fixed**: `the final holiday pay for` adds it only where the employee has become entitled |
| the cash-up (s 28B, via s 21(2)) and the closedown rate ignore s 16(3) | **fixed**: both take an absences list and use the reduced divisor |
| a cash-up is not limited to the entitlement not yet taken | **fixed**: `Payout request` carries the weeks not taken; a request for more is not one the employer may agree to |
| 14 days' notice (lines 170, 258, 406) | **kept**, as fork F4: 14 clear days, by the Legislation Act 2019's rule for "not less than" a number of days between 2 events. The author thought the encoding probably right but could not apply an Act outside the bundle. These 3 assertions stay failing as a recorded disagreement |
| s 63(1)(b) hours test not computed | kept; the date the test was first met is an input (`NOTES.md` §1) |
| no constructor for a pregnancy ended by abortion services | kept: the s 69(2)(c), (d) constructors say "miscarriage or still-birth", which s 69(4) defines to exclude it |
| whether the employee is entitled at the end of employment is an input | kept |
| the s 28 series-of-fixed-terms provision is not modelled; subsection labels in s 28 may be shifted | kept; noted. The labels follow the encoder's reading of the unlabelled text |
| s 75 list depends on how the caller classifies the breach | kept; noted |

The author agreed with the other forks as encoded, including F1, F3, F5, F7, F8, F10 and F11.

## After the fixes

`Payout request` and `Closedown` calls in the independent file were ported to the new fields (marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 295 satisfied, 3 failed (the F4 disagreements); all 9 modules 587 satisfied, 3 failed, 0 other errors.
