# Independent test pass — Fair Trading Act 1986

Run on 2026-10-15 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and `../registers/source-bundle/act_public_1986_121.txt`, wrote `independent-expectations.md` from those alone (about 230 scenarios, with working-day cases across Labour Day, Easter and the Christmas break), and only then opened the rule modules (not `fta-tests.l4` or `NOTES.md`) to learn their names, and wrote `tests-independent.l4`. It changed no expected value after reading the encoding. For working days it assumed the Legislation Act 2019 definition, entering the non-working weekdays in the calendar input.

## Result as first run

239 assertions: **237 satisfied, 2 failed**.

| scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- |
| a compulsory recall notice, conduct not in trade | s 32(1), (2), (5) "has in trade supplied goods"; "shall not, in trade, supply" | no contravention | contravention | **fixed**: s 32 added to the provisions that need conduct in trade |
| failing to offer at the advertised price, advertiser not in trade | s 19(2) "Any person who has advertised" | contravention | none | **fixed**: s 19 split; s 19(2) applies to any person, s 19(1) only in trade. The independent call was ported to the new constructor (marked `[Ported …]`) |

## Other remarks by the author, and what was done

| remark | outcome |
| --- | --- |
| s 36V(2)(a): no cooling-off for a warranty that is a condition of a consumer credit contract | **added**: `may cancel the extended warranty…` |
| s 36Q(1)(b): "10 working days beginning with the date" counts the notice day | **added**: `the last day of the 10 working days beginning with…` |
| s 21A(2) (the trader's duty to inform) not in the provision list | **added** as a prohibition (in trade; Part 1 offence) |
| s 31(2): 18 months only for a s 31(1) notice | **noted** in the function's comment; a s 31(1A) notice has no statutory expiry |
| s 5D(1)(b) bars only parties to the agreement | kept; the s 43 flag assumes the applicant is a party (`NOTES.md` §1) |
| ss 41, 42, 46H, 46I(1), 4(2) who may apply; s 40(2) aggregate cap; ss 3, 5, 5B; Schedule 1AA cl 1; ss 37(e), 38(c) | kept as text |
| s 46C: one occasion; s 40(1B) offences; director liability; overseas prohibition | kept; the function takes two s 40(1)/(1A) occasions |
| gift cards: no in-trade or consumer input; s 36WA exclusions | kept as inputs to the caller |
| single booleans for s 36N(2)/36V(2)(b) "minor", s 36ZF(2) "unless agreed", s 46L(4) insurance terms | kept as inputs |
| s 14A, s 26, s 28A not in the provision list | kept: s 14A is a s 13 price representation; s 26 and s 28A are import and regulation provisions |

The author agreed with the encoding on the remaining 237 assertions, including its readings of s 43A (29 February), s 46C (exactly 10 years) and s 36RA(5).

## After the fixes

`check.sh`: `tests-independent.l4` 239 satisfied, 0 failed; `fta-tests.l4` 162 satisfied; all 8 modules 401 satisfied, 0 failed, 0 errors.

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the 3-year limit for applying for orders under s 43 (s 43A); the deadlines already counted in working days (ss 31A, 36Q-36R, 36ZF) end on working days. 1 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 238 satisfied, 1 failed.
