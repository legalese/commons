# Independent test pass — Wages Protection Act 1983

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../source/WPA1983.txt`, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `wpa-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`.

## Result as first run

144 assertions: **143 satisfied, 1 failed**.

| line | scenario | expected (author) | encoding gave | provision |
| --- | --- | --- | --- | --- |
| 173 | 500 deducted to recover an overpayment of 300, every s 6(3) condition met | `the deduction was lawful` = FALSE | TRUE | s 6(2) "recover the amount of that overpayment", with ss 4 and 11(1)(a) |

## Other remarks by the author, and what was done

| remark | outcome |
| --- | --- |
| a s 6 deduction is never compared with the overpayment | **fixed**: `the lawful part of the deduction` caps a s 6 deduction at the overpayment; the excess is unlawful and recoverable under s 11(1)(a)(i) (fork F11) |
| s 11A(3)-(4) (premiums from a person involved) has no 2016 date gate | **fixed**: it takes the date of the conduct and gives 0 before 1 April 2016 |
| s 12A(2): `the worker` as claimant gets 0 | kept; noted in `NOTES.md` §4 |
| "vary" in ss 5(2), 9(2) cannot be expressed | kept; noted |
| a s 6 deduction's date and the overpayment's recovery date are not checked against each other | kept; noted |
| s 13 refuses before 1 April 2016 even for the employer | kept (the pre-2016 text is not carried); noted |

The author agreed with forks F1-F10 as encoded.

## After the fixes

The s 11A(3) calls in the independent file were ported to the new date input (marked `[Ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 144 satisfied, 0 failed; all 7 modules 284 satisfied, 0 failed, 0 errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the employer's 2 weeks to act on a withdrawal of consent or a request (ss 5(2), 9(2)) and the last day for notice of an overpayment (s 6(3)(c)). 4 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 140 satisfied, 4 failed.
