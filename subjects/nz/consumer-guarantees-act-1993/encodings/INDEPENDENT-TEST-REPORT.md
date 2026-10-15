# Independent test pass — Consumer Guarantees Act 1993

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_1993_91.txt`, wrote `independent-expectations.md` from those alone (about 190 scenarios), and only then opened the rule modules (not `cga-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

153 assertions: **145 satisfied, 6 failed, 2 refused by the encoding**.

| scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- |
| a charity supplies for the recipient's benefit; manufacturing defect | s 41(2), Part 3 | manufacturer remedies | none | **fixed**: s 41(2) bars redress only "against a charitable organisation"; the manufacturer stays answerable (`the Act applies to the supply to` is now separate from `the Act gives redress for the supply to`) |
| remediable but substantial goods failure, supplier refused | s 18(2)(b)(ii), (3)(a) | "reject" once | twice | **fixed**: remedies are listed once |
| the same for a service | s 32(a)(ii)(B), (b)(i) | "cancel" once | twice | **fixed** |
| remediable service failure, supplier refused, no contract with the supplier | s 32(a)(ii)(B) | no cancellation | cancellation | **fixed**: cancelling needs a contract to cancel, under (a) as under (b) |
| s 28 failure leaving the product unfit for a made-known purpose | s 36(c) | substantial | not | **fixed**: "where section 29 applies" read as the s 29 guarantee being engaged, as s 21(c) reads s 8(1) |
| a repairer in trade acquiring a household service | s 2 consumer (b)(iii) | consumer | not | **fixed**: the repair limb is "in the case of goods" |
| a s 6 claim on reticulated electricity | s 7B(4) | no remedies | refused | **fixed**: a guarantee that does not fit what was supplied gives no remedies |
| a work-and-materials contract recorded as services; the goods fail | ss 15, 34 | goods remedies | refused | **fixed**: a goods failure on a services supply is answered as goods |

## Not expressible (recorded in `independent-expectations.md`)

Whether each guarantee is engaged and has failed (ss 5(3)-(5), 5A(1), 7(2)-(4), 7A(2)-(4), 8(2), 9(2), 10, 11(1), 12, 14, 29, 30) is an input; s 42(2) and s 17's limbs are single inputs; the s 2 definitions beyond the building rule; ss 19, 22, 23 mechanics, 23A, 24, 27(3), 37(3), 38(1)(b)-(c), 39, 39A, 43(4)-(7), 43A, 44-46A, and the s 47(3), (5) order limits. These are listed in `NOTES.md` as inputs or text.

## After the fixes

No independent assertion needed porting. The encoder's tests that encoded the rejected readings (s 41(2), s 36(c), and the two refusals) were changed, each marked in `cga-tests.l4`, and tests were added for the other fixes. `check.sh`: `tests-independent.l4` 153 satisfied, 0 failed; `cga-tests.l4` 115 satisfied; all 7 modules 268 satisfied, 0 failed, 0 errors.
