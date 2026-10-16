# Independent test pass — Employment Relations Act 2000, dismissal and personal grievances

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md`, the provisions in scope in `../registers/source-bundle/act_public_2000_24.txt` and Legislation Act 2019 ss 13, 54-56, wrote `independent-expectations.md` (about 100 scenarios) from those alone, and only then opened the rule modules (not `era-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding.

## Result as first run

105 assertions: **100 satisfied, 5 failed**.

| line | scenario | provision | author | encoding | outcome |
| --- | --- | --- | --- | --- | --- |
| 87, 89, 126 | T19, T20, H17: a dismissal grievance for whistleblower retaliation or a remuneration disclosure reason, after a trial or above the threshold | ss 67B(3)(b), 113A(3)(b) | barred | not barred | **kept as a recorded disagreement**: the conversion lost the s 103(1) letters; the author lettered the grounds by position (a)-(m), so "(c) to (k)" left out the last two; the encoding uses the inserted letters (da), (ja), so "(c) to (k)" covers all. The author thinks the encoding is probably right; the PCO's lettering decides it |
| 137 | B05: s 113B rounding of an exact half | s 113B(4) | rounds up | rounds to even | **fixed**: halves round up |
| 176 | N18: 12 months beginning 29 February 2028 | s 114(7)(a); Legislation Act s 56 | ends 28 February 2029 | 27 February 2029 | **fixed**: the s 56 month rule |

## Not expressible (recorded in `independent-expectations.md`)

A trial not starting with the employment (T06); when termination takes effect (T11); whether a s 120 request must be answered after a trial or high-earner dismissal (T22, H18, H19); probation (T23); an employee not dismissed (H20); the s 113B percentage and its 1 July effect (B06, B07); no grievance found (M13); the s 128(3) discretion (M15).

## Differences noted without an assertion

- A reduction over 100% under s 124(2) was clamped; the author expected a refusal. **Changed**: it now refuses (and a negative one too).
- Matariki Observance Days are an input list.

## After the fixes

`check.sh`: `tests-independent.l4` 102 satisfied, **3 failed (the recorded lettering disagreement)**; `era-tests.l4` 38 satisfied; 7 modules, 140 satisfied, 3 failed, 0 other errors. The encoder's test that a 150% reduction gives 0 was removed (now refused) and marked; tests for the half-up rounding and the s 56 month end were added.
