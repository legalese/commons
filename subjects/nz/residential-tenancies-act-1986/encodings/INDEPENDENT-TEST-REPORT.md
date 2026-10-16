# Independent test pass — Residential Tenancies Act 1986

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_1986_120.txt`, wrote `independent-expectations.md` from those alone, and only then opened the rule modules (not `rta-tests.l4` or `NOTES.md`) to learn their names and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

246 assertions: **243 satisfied, 3 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 214 | B30: tenancy began 1 March 2026, increase from 1 March 2027 | s 24(1)(d) | unlawful | lawful | **fixed** (fork F2): a period "after" a day excludes it (Legislation Act 2019), so the anniversary is within the 12 months |
| 217 | B32: last increase 15 May 2026, next from 15 May 2027 | s 24(1)(e) | unlawful | lawful | **fixed**: as B30 |
| 314 | C26: family violence withdrawal posted Monday 7 September 2026 | ss 56B, 56C | effective 9 September | 13 September | **fixed**: s 56C treats a posted or delivered withdrawal notice as given that day, despite s 136(6)-(7) |

## Not expressible (recorded in `independent-expectations.md`)

Grounds whose underlying facts are folded into an input constructor (C14, C15, C19, C30, C33); the facts behind s 5 exclusions (A26-A31); bond receipts (B20), s 24A (B37), s 26 (B43); s 56B(2)-(3) (C27-C28); immediate disposal under ss 62(1), 62A(2) (C59-C60); s 56D on a periodic tenancy (C68); ss 60AA, 52 (C69, C72); entry by consent, showings and force (D10, D14, D15); boarding room emergencies and s 66Q (D19, D21); hour-level edges of ss 66W, 66X (D22, D23, D31); ss 54(6), 109A(3), 109B's list and time limit (E07, E20, E21, E25); an applicant other than a landlord, tenant or chief executive (E22).

## After the fixes

The encoder's tests that encoded the rejected reading of s 24(1)(d)-(e) were changed and marked; two s 56C tests were added. `check.sh`: `tests-independent.l4` 246 satisfied, 0 failed; `rta-tests.l4` 191 satisfied; 10 modules, 437 satisfied, 0 failed, 0 other errors.
