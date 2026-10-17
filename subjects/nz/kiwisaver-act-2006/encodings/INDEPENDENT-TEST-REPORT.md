# Independent test pass — KiwiSaver Act 2006

Run on 2026-10-16 by a fresh session that had not seen the encoding being written (a first attempt the day before stopped on a usage limit before writing anything). It read `BRIEF.md` and `../registers/source-bundle/act_public_2006_40.txt`, wrote `independent-expectations.md` from those alone (about 190 scenarios), and only then opened the rule modules (not `ks-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

167 assertions: **160 satisfied, 5 failed, 2 refused by the encoding**.

| scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- |
| a contract of 28 days or less that ends within 28 days (2 assertions) | s 12(1)(b), (2)(b) | no enrolment, no opt-out window | enrolled | **fixed**: new input `the short contract continued to the 28th day`; only a contract that does becomes new employment, and the opt-out window then runs from the 28th day |
| a 17-year-old whose only guardian is an Oranga Tamariki guardian | s 35(3)-(4) | jointly with that guardian | alone | **fixed**: s 35(3) covers "a guardian or an Oranga Tamariki guardian" |
| a rate reduction 1 April to 1 July 2026 (92 days counting both) | s 101L(3) | granted | not | **fixed** (fork F6): the ending date is the last day of the reduction |
| a rate reduction 1 April 2026 to 1 April 2027 | s 101L(3) | not granted | granted | **fixed** (the same) |
| a notice choosing 5% | s 64(1)(a)(i), (2) | 3.5% | refused | **fixed**: not a s 64(2) notice, so the default applies |
| an employee still on a 2% rate chosen before April 2013 | s 64(1)(a)(iii) | 3.5% | refused | **fixed**: new `Rate history` cases for (a)(ii) and (a)(iii) |

## Other remarks by the author

| remark | outcome |
| --- | --- |
| s 112B(3) "within 92 days of giving" may bar day 92, unlike s 64(4) "less than 92 days apart" | kept; noted (the shared 92-day function follows s 64(4)) |
| Schedule 1 cl 17: tax-credit Crown contributions cannot be withdrawn without a residence declaration | kept; noted as a limit |
| not modelled: s 6(2)-(3), s 12(2)(a) end of casual agricultural work, s 62(a), (c), the s 101FB periods, s 101E, s 101L(1) and s 112B(1) eligibility, s 48, s 102(b)'s earliest of three dates, cl 14C(2)(a) and (4)(a), cls 14(2), 14B, cl 8 by date, s 18(2) "received" | kept as inputs or text; listed in `NOTES.md` |

## After the fixes

The `Employment` constructions in the independent file were ported to the new field (marked `[Ported …]`; no expected value changed). The encoder's tests that encoded the rejected readings (the rate-reduction days, the 5% refusal) were changed and marked, and tests were added for the other fixes. `check.sh`: `tests-independent.l4` 167 satisfied, 0 failed; `ks-tests.l4` 119 satisfied; all 7 modules 286 satisfied, 0 failed, 0 errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the deadlines to opt out (s 16), to give the information pack (s 42(1)(a)) and to pay a complying fund (s 101F(2)). 5 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 162 satisfied, 5 failed.
