# Independent test pass — Parental Leave and Employment Protection Act 1987

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_1987_129.txt`, wrote `independent-expectations.md` from those alone (230 scenarios), and only then opened the rule modules (not `pl-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`. It changed one expected value after reading the encoding (S36, to reconcile it with S41), away from what the encoding gave, and says so in its file.

## Result as first run

264 assertions: **250 satisfied, 14 failed**.

| scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- |
| S10b a sole carer (an aunt), not nominated | s 7(1)(c), (2) | primary carer | not | **fixed**: s 7(2) needs a nomination only "if 2 or more persons meet the criterion"; new input `another person also meets s 7(1)(c)` |
| S36 25 weeks at 40 hours; S41 13 weeks employed and 13 self-employed at 20 hours | s 2BA(4), s 2AD | threshold not met | met | **fixed** (fork F7): the person must have been employed (or self-employed) for 26 of the 52 weeks, averaging 10 hours over them |
| s 6 for extended leave; s 6 for a partner's leave (2 cases) | ss 2, 6 | barred | allowed | **fixed**: s 6 bars all parental leave, not only primary carer leave |
| S46b, S166b leave or payments starting after the due date | ss 6, 71F | allowed | barred | **fixed** (fork F4 changed): the 6 months are measured to the day the leave or payments start (the birth), not to the due date |
| S164 the transferee of a mother's payment claims | s 71D(2)(b) | entitled | not | **fixed**: a (b)(i) or (b)(ii) carer, whose entitlement arises by succession or transfer, is not barred by the spouse's earlier receipt |
| S148b, S148c dismissal for a substantial unrelated reason, during or after leave | ss 49(1)(c), 54 | no contravention | contravention | **fixed**: s 54 keeps the right to dismiss for a substantial reason unrelated to the pregnancy, the child or the employee's rights |
| S204 30 days between birth and the end of the 36th week | s 71DA(2) | 30/7 weeks | 5 | **fixed** (fork F6 changed): the exact weeks, since s 71DA(4)(a) ends the payment on that day |
| S111/S122 "at least 14 days" before 15 September 2026; S129 "not less than 21 days' notice" of 4 August 2026 | ss 30B(3)(c), 33(b), 37(2) | 1 September; 14 July | 31 August; 13 July | **kept** as fork F3 (clear days); 2 assertions stay failing as a recorded disagreement |

## Other remarks by the author

| remark | outcome |
| --- | --- |
| the top-level goal has no s 4 input (a comprehensive agreement) | kept; `Parts 1 to 5 apply…` answers it separately (`NOTES.md` §1) |
| s 8(2) reads only the "previously took parental leave" input, not partner's leave | kept; the input is documented as covering all parental leave for the child |
| the goal reports 26 weeks of primary carer leave without s 9(2) | kept; `the most primary carer leave…` answers s 9(2) |
| not expressible: ss 2A-2AC, 2B, 5, 6A, 10, 12-14, 15's conditions, 27(4)(b), 31(4), 33(a), (c), 36(3), 45(4)(c), the elements of ss 51-52, 55(2), 68(4), 70A-70G, 71I(3), 71IA, 71J(1)(b) split, 71CE date edge, 71DB(4)(c), Schedule 1 | kept as inputs or text; listed in `NOTES.md` |

## After the fixes

The `Carer facts` calls in the independent file were ported to the new field (marked `[Ported …]`; no expected value changed). The encoder's own tests that had encoded the readings now rejected (s 7(2), F7, s 54, F6) were changed, each marked in `pl-tests.l4`. `check.sh`: `tests-independent.l4` 262 satisfied, 2 failed (the F3 disagreements); `pl-tests.l4` 217 satisfied; all 8 modules 479 satisfied, 2 failed, 0 other errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the deadlines to decide or challenge a flexible-leave request (ss 30D, 30I), to apply for parental leave payments (s 71I), to file a charge (s 71Z), to apply for a review (s 71ZB), to act within n days after an event (ss 34, 36, 38), to apply for an interim order (s 55), to complain (s 70) and to object (s 70C) — not deadlines counted back from an event. 4 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 258 satisfied, 6 failed.
