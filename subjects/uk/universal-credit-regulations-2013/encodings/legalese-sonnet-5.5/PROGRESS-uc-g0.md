# PROGRESS (keel agent uc-g0, Universal Credit Regulations 2013, regulation 2)

If this context is compacted: re-read this file, `NOTES.md`, and lines 12-117 of `../../registers/source-bundle/uksi-2013-376.txt`, not any summary.

## Status

- [x] Read the brief, both skills, `dialects.md`, source-patterns 01/03/04/06/11, the Commons guides, the example seat layer.
- [x] Read lines 12-117 (regulation 2) in full; sampled the regulations the definitions point to, to choose the types.
- [x] Counted which pieces use each defined term (the "Used outside regulation 2" figures in NOTES.md are from that count).
- [x] Probed the stable binary (1.6.98): `add months` / `add years` exist, `YMD` does not, `TRUNC` takes two arguments, imports are transitive, hyphenated modules need backticks, name collisions between imported modules (types and rules fail; bare constructor words fail only when untyped; fields are fine).
- [x] `uc-core.l4` written and checks clean.
- [x] `uc-core-persons.l4`, `uc-core-bodies.l4`, `uc-core-payments.l4` written and check clean.
- [x] `uc-core-tests-core.l4`, `-persons`, `-bodies`, `-payments` written: expected values by hand from the text; a positive control (one flipped expected value) was reported as failed.
- [x] `srcrefs.py check --refs` and `--strict`: 0 problems.
- [x] `check.sh`: 0 errors, 0 failed, 0 refused.
- [x] No `DiagnosticSeverity_Warning` or `_Error` from `l4 run` on any module.
- [x] Importability probe for every module (each alone, then all four together): passed; the throwaway files were deleted.
- [x] `NOTES.md` written with all eight required headings (generated, with the tables laid out from hand-written rows).
- [x] Deleted `deposit/probe/` (templates and generators) and `deposit/usage.py`; the deposit holds only the deliverables, `check.sh` and `srcrefs.py`.

## Decisions taken, and what licenses each

| decision | licensed by |
| --- | --- |
| the core is vocabulary plus six small helpers; every other reg 2 definition is a rule in a topic module | brief items 1-2 |
| `Benefit` has 24 constructors, one per benefit or payment that reg 2 names | reg 2 lines 17-116; used by all four pieces (usage count) |
| `Claim basis` has three constructors | regs 3(3), 22(3), 78(2) (lines 123, 474, 1268-1270) |
| `Nation of Great Britain` | foster parent, local authority (lines 49-51, 62-65) |
| `Element of an award` | reg 23(1) and (2) (lines 499-508) |
| `Work-related group` | reg 90(1) and (2) (lines 1412-1415) |
| `Capability for work` (three BOOLEANs) | regs 38, 39(1), 40(1), 40A(1) (lines 745-785) |
| `Assessment period` record and the number of days in it | reg 21(1) (line 432) |
| `Time limit` (quantity, unit) and the date it reaches | brief item 1 ("the one way a time limit is written"); lines 149, 289 |
| `Payment interval` and the monthly equivalent | the same table in reg 73(2), Sch 4 para 7(2), Sch 5 para 13(3) (lines 1189-1192, 2195-2199, 2684-2688) |
| rounding helpers in the core (assumed, not ruled: reg 6 is uc1's) | reg 6(1), 6(1A) (lines 172-176); fork F1 |
| `YMD` shim in the core, and nowhere else | brief ("Smaller gaps") |
| no `@export`, no seat layer, no dates (none in lines 12-117) | brief |

## Files

`uc-core.l4`, `uc-core-persons.l4`, `uc-core-bodies.l4`, `uc-core-payments.l4`, `uc-core-tests-core.l4`, `uc-core-tests-persons.l4`, `uc-core-tests-bodies.l4`, `uc-core-tests-payments.l4`, `NOTES.md`, `PROGRESS.md`.

## Slips to remember

- I deleted `uc-core-tests-persons.l4` once by a chained `cd ... && rm` that ran in the wrong folder; it was regenerated at once from the table that wrote it. Use absolute paths for any `rm`.
- I listed the names inside `porridge/stable/extension/` (two entries: `bin`, `package.json`) and searched that tree for a `daydate.l4` file (none found) while looking for the date library; I opened no file there except by running the binary. Reported under `peeked`.
