# Independent test pass — Social Security Act 2018, main benefits

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and the provisions in scope in `../registers/source-bundle/act_public_2018_32.txt`, wrote `independent-expectations.md` (about 95 scenarios) from those alone, and only then opened the rule modules (not `ss-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

128 assertions: **126 satisfied, 2 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 334 | CM-20: sole parent support applied for 29 days after entitlement | s 316(2)-(3) | no rule: refuse | the s 316(3) "later of" date | **fixed**: s 316(2) needs an application within 28 days, and s 316(3) covers only benefits not listed in s 316(2), so the encoding now refuses |
| 336 | CM-21: the same for a supported living payment | s 316(2)-(3) | refuse | the s 316(3) date | **fixed**: as CM-20 |

The author wrote these as "not equal to the s 316(3) date". With the fix they are **refused** (the outcome the author expected), which `check.sh` counts neither as satisfied nor as failed.

## Not expressible (recorded in `independent-expectations.md`)

The s 40(2) 28-day continuation (SL-20); the s 32(2)-(3) priority and court-order rules (SP-21: split care is one input); s 33(2)-(3) replacement by jobseeker support (SP-24); MSD's discretion over the childcare disregard (RS-08); ss 313-315 and 316(4) (CM-22 to CM-25). SL-13 (a carer of their own spouse) became expressible with the fix below.

## Differences the author noted without a failing assertion

1. s 316(1)(a)(ii) counts employment ending only "before the person applied": **fixed**, a new input.
2. s 40(1)(a) excludes caring for one's own spouse or partner: **fixed**, a new input.
3. The $20 childcare disregard is taken from combined income; the input is earnings used for childcare, which are personal earnings, so the result is the same (fork F6).
4. Residence is a number of years (fork F7); s 22 availability and the s 26 bars are single inputs; s 24 reads combined income (fork F3, the author's reading too).

## After the fixes

The `Supported living facts` and `Commencement facts` constructions in the independent file were ported to the new fields (FALSE and TRUE, marked `[Ported …]`; no expected value changed). The encoder's test of sole parent support applied for late was removed (the refusal cannot be asserted) and marked; tests of both new inputs were added. `check.sh`: `tests-independent.l4` 126 satisfied, 0 failed, 2 refused as expected; `ss-tests.l4` 66 satisfied; 8 modules, 192 satisfied, 0 failed, 0 other errors.
