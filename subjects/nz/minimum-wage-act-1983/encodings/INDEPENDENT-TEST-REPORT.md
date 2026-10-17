# Independent test pass — Minimum Wage Act 1983

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../source/MWA1983.txt`, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `mwa-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`.

## Result as first run

126 assertions: **125 satisfied, 1 failed**.

| line | scenario | expected (author) | encoding gave | provision |
| --- | --- | --- | --- | --- |
| 120 | class A worker, 17, on the day 6 months' continuous employment with the current employer are completed | the starting-out rate, $20 | the adult rate, $25 | s 4A(3)(a)(i): "only until ... the date on which the worker has completed 6 months'"; limb (ii)'s "the day before" shows "until" includes the date named |

## Other remarks by the author, and what was done

| remark | outcome |
| --- | --- |
| s 4A(3)(a)(i) is a date test, but the encoding took month counts | **fixed**: `Worker` now carries the first day of each employment period; `the date the worker completes the employment that ends the rate` works out the completion date; the rate is paid on that date (fork F11) |
| the 2016 date gate is applied to s 10 but not to s 11, which the 2016 Act also replaced | **fixed**: `may recover the wages under s 11` takes the conduct date and refuses before 1 April 2016 |
| s 11AA returns 0 before 2016 while s 10 refuses | kept: s 11AA did not exist before 2016, whereas ss 10 and 11 replaced earlier sections (fork F10) |
| a deduction above the s 7(1) ceiling is only capped, never flagged | **fixed**: `a board or lodging deduction exceeds what s 7(1) allows, under … from` and a field in the top-level answer |
| F2 (a factor (i)-only class counts employment with any employer since the benefit run) | kept; an open question in `NOTES.md` |
| the 2013 transitional rate takes the 16-17 starting-out rate as an input | kept |
| s 13 and the 2007 permit transition are text only | kept |

## After the fixes

The independent file's worker helpers were ported to the new date inputs (marked `[ported …]`; no expected value changed). `check.sh`: `tests-independent.l4` 126 satisfied, 0 failed; all 7 modules 257 satisfied, 0 failed, 0 errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the Minister's annual review (s 5(1)), which read literally may then be done on the first working day of the following January. 2 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 124 satisfied, 2 failed.
