# PROGRESS (keel agent, row iaw-snap-k)

Status, 2026-11-04: the keel's work is finished and the gates below were run on the files as they stand.
Source: `usc07-ch51.txt`, a plain-text rendering made by a converter script, not the official text. Nothing here is "verified against the official text".

## Scope found on reading

- The keel range is lines 1-135 only: s 2011 (policy, lines 18-21) and s 2012 (definitions (a) to (v), lines 23-134), plus blank lines 22 and 135.
- So `snap-definitions.l4` is s 2012, whole. No definition of s 2012 is left to a part. The Act's own definitions inside the parts' ranges are left to those parts and listed in `PLAN.md` section 5.
- The parts get only `snap-core.l4`. They cannot import `snap-definitions.l4`, so a part that needs a s 2012 answer takes it as an input named like the function that gives it (`PLAN.md` section 4).

## Decisions taken (with the text that licenses each)

1. Core = nouns only: 16 `DECLARE`s, 160 lines: Area, Kind of place, Immigration status, Individual, Income item, Household, Party, Kind of decision, Period of ineligibility, Form of benefit, Benefit, Certification period, Claim, and the three COLA row types. No rule, no directive. Test for membership: could a witness testify to this fact.
2. COLA figures: the core carries row types only. snap1 fills the s 2014 tables, snap3 the s 2017 tables (`PLAN.md` section 5).
3. A fact only one s 2012 definition reads is declared in `snap-definitions.l4` under a name that begins `s 2012(x)`.
4. FALSE and NOTHING: a "means" definition answers `JUST FALSE` outside its limbs (s 2012 chapeau and each "means"); "such as", a determination of the Secretary, and a reference to another section answer `NOTHING`. 68 `FALSE-kind` and 21 `NOTHING-kind` comments carry the reasons.
5. F-1 to F-5 (NOTES.md): (g) "issued in lieu of a coupon" (s 2012(g), line 35); (o) the "and" before paragraph (5) (lines 77-94); (m)(5)(A) one class or two (line 71); (u)(2)(I) what the 200 percent caps (line 122); (m)(4) against (m)(5) (lines 69-75). Each is "assumed, not ruled".
6. The (m)(4) function was renamed `s 2012(m)(4) the individual or group may constitute a household` after I saw that its old name ("is barred from") answered `JUST FALSE` when the group was barred, so the name contradicted the answer.

## Files

| file | state |
| --- | --- |
| `snap-core.l4` | 160 lines, compiles, types only |
| `snap-definitions.l4` | 1147 lines, s 2012 (a) to (v), 48 `MEANS` functions, compiles |
| `snap-definitions-tests.l4` | 503 lines, 265 `#ASSERT`, all 265 satisfied |
| `NOTES.md` | coverage table, fork register F-1 to F-5, reading a result, marginal readings (MA-1 to MA-16, MB-1 to MB-10), jural relations, what the stable binary does not accept, limits, check output |
| `PLAN.md` | the six parts, naming rules, the convention for asking a s 2012 answer, seams in three groups, difficulties |
| `tools/expand-quotes.py`, `tools/verify-quotes.py` | quoting and quote-checking scripts |

## Status

- [x] snap-core.l4
- [x] snap-definitions.l4
- [x] snap-definitions-tests.l4
- [x] NOTES.md
- [x] PLAN.md
- [x] check.sh run: 0 errors, 265 satisfied, 0 failed, 0 refused on the stable binary and on main 1.6.108 (the main columns match)
- [x] `srcrefs.py check --refs` over the three `.l4` files: 0 problems
- [x] `tools/verify-quotes.py`: 101 pieces checked, 0 not found

## Not done, and why

- No part-to-part seam was read in the bodies (group C of `PLAN.md` section 6 is from references only).
- No lawyer has read any fork or marginal reading.
- Nothing is checked against the official text.

## Independent review 2026-11-04

Seven failing assertions of the independent reviewer fall in lines 1-135 (items 6, 11b, 24, 33b, 34, 36, 54a). Verdicts are in NOTES.md, section "Independent review of the keel range". Only comments changed in `snap-definitions.l4`; two fixtures were renamed and five assertions added in the tests.
