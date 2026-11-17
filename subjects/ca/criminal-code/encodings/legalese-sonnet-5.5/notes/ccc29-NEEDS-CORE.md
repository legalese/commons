# NEEDS-CORE.md (ccc29)

Nothing here blocks anything: the part compiles and its tests are green without the core changing.
The items are types this part declared for itself, under its own prefix, because the core lacks them or has a type it did not use; the lead may hoist or merge them.
Each claim was checked on 2026-11-17 against `ccc-core.l4` (the `Party` type is declared at line 49, its constructors at lines 57-78; `Province or territory` at line 29) and against the part's modules.

## Party constructors the core lacks

The core's `Party` already has every constructor this part uses from it: `a justice`, `a provincial court judge`, `the court`, `the clerk of the court`, `the keeper of a prison`, `the prosecutor`, `the informant`, `the Attorney General of Canada`.
It has no constructor for the following, which this part declared for itself.

| wanted | the text | declared here |
| --- | --- | --- |
| `the minister of justice of a territory` | s 810.3(1), (2) and (4): "the Attorney General of a province or the minister of justice of a territory" (the core has `the Minister of Justice`, line 81, which is not a territory's minister) | a constructor of `s 810.3 designating authority` (`ccc29-xxviii-3-peace-810-21.l4` line 112), beside `s 810.3 the Attorney General of a province` and `s 810.3 a person authorized by the Attorney General or minister` |
| `the Attorney General of a province` | the same | the same type, `s 810.3 the Attorney General of a province`; it is also used as a regulative actor (`PARTY` of two rules in the same module); the core's `the Attorney General` (line 58, "as s 2 defines it, which varies with the proceeding") exists and could stand for it; the reason this part declared its own is not recorded |
| `the appellant`, `the respondent` | ss 813 to 840 | `s 815 party` with `s 815 the appellant` and `s 815 the respondent` (`ccc29-xxviii-4-appeal-812.l4` line 233); the kinds of appellant in s 813 are `s 813 appellant` (line 96) |

## Duplicate of a core type

The core's `Province or territory` (13 constructors) and this part's `s 812(1) province or territory` (13 constructors, `ccc29-xxviii-4-appeal-812.l4` line 26) name the same thirteen provinces and territories.
This part uses its own in modules 4, 5 and 7 (`ccc29-xxviii-4-appeal-812.l4`, `ccc29-xxviii-5-appeal-829.l4`, `ccc29-xxviii-7-schedules.l4`) and not in the seat.
The reason for declaring it is not recorded; it is a duplicate, not a need.
If the lead prefers one type, replace `s 812(1) province or territory` by the core's in those three files.

## Used without a constructor

"The person having the custody of the appellant" (ss 816(1.1) and 819(1)) names no office; the regulative rules use the core's `the keeper of a prison` for it (marginal reading M-1 in NOTES.md).
