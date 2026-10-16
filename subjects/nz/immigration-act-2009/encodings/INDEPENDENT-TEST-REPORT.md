# Independent test pass — Immigration Act 2009

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and the provisions in scope in `../registers/source-bundle/act_public_2009_51.txt`, wrote `independent-expectations.md` (about 120 scenarios) from those alone, and only then opened the rule modules (not `imm-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result

93 assertions: **93 satisfied, 0 failed**. The author flagged the "preceding 10 years" (s 15(1)(b)) and "preceding 12 months" (s 350) edges as ambiguous and took the same reading as the encoding (fork F1); likewise for excluded time under ss 161(3) and 167(2) (fork F2).

## Differences noted without an assertion (recorded as known limits)

1. s 161(3): the encoding adds one total of days imprisoned to every window, so imprisonment after a window closed would extend it; the caller must give the days in prison within the relevant window.
2. The top-level goal's appeal deadline ignores any s 185 reconsideration and the s 154(5) exclusions.
3. s 350 subsection numbers: the converted text lost paragraph labels; the encoding cites deemed knowledge as s 350(3) and the notice-period defence as s 350(4), which a reviewer should check against the PCO's numbering.
4. s 9(1)'s "is in New Zealand" is assumed.

## Not expressible (recorded in `independent-expectations.md`)

The s 15(3) and s 16 limbs (single inputs); s 17(2)-(4); status on a given day under s 9, s 9(2)(c)-(d); s 154(1), (5) and s 167(3); the s 185(1) preconditions; s 157(1), (3) and the (4) visa types; whether the person holds a residence class visa and s 161(2)(b); the s 161(5) first-held date (an input).

`check.sh`: `tests-independent.l4` 93 satisfied; `imm-tests.l4` 46 satisfied; 7 modules, 139 satisfied, 0 failed, 0 other errors. No change was made after the pass.
