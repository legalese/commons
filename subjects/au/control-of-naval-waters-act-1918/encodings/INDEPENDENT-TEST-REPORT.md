# Independent test report: Control of Naval Waters Act 1918

Expectations: `independent-expectations.md` (23 scenarios, written from BRIEF.md and the source before any L4 was read).
Tests: `tests-independent.l4` (30 assertions against `the naval position for`).

## Result

`L4=~/.local/bin/l4 ./check.sh .` : tests-independent.l4 — **30 satisfied, 0 failed**, no other errors.

## Disagreements
None.

## What was covered
- s 2 exempt vessel: Commonwealth/Navy, declared foreign naval, other vessel.
- s 6(1)-(2): master of a non-exempt vessel in naval waters; direction given/not given; complied/not; not in command; exempt vessel; craft elsewhere; aircraft/vehicle in the waters (outside both ss 6 and 6A).
- s 6A(1)-(2): aircraft, vehicle, non-exempt vessel and exempt vessel on the foreshore.
- 10 penalty units maximum.
- s 8(1) liability with and without a removal.
- s 8(3) earliest sale day: ordinary month (15 Jan -> 16 Apr, and not 15 Apr), short-month roll-over in a leap year (30 Nov 2023 -> 1 Mar 2024), 31 Jan -> 1 May; no sale once paid.
- s 8(5)-(6): surplus, deficiency, exact break-even.

## Observations (not failures)
- `the surplus paid to me after a sale` / `the deficiency I still owe after a sale` are computed whenever a sale day exists, whether or not a sale has happened; there is no "it was sold" input. With proceeds 0 (no sale yet), the "deficiency" equals the whole expenses plus sale expenses. A reader could mistake this for a s 8(6) debt that has not yet arisen. Low significance.
- The amount payable under s 8(1) is not an output (only the boolean), so the $ figure in scenario 15 was not asserted.
- Strict liability (s 6(2A)) is not an output field; it applies only to s 6(2), not s 6A(2) — the encoding's comment groups them; nothing observable to test.
- The dollar value of a penalty unit is outside this Act and is not computed.

## Coverage gaps
- s 8(2) detention and s 8(4) deemed ownership have no outputs.
- A demand date with `NOTHING` while expenses are owed yields no sale day (correct: no demand, no clock) but was not asserted.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
