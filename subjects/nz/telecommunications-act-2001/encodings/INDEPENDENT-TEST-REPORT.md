# Independent test pass — Telecommunications Act 2001

Run on 2026-10-16 by a fresh session that had not seen the encoding being written. It read `BRIEF.md` and the provisions in scope in `../registers/source-bundle/act_public_2001_103.txt`, wrote `independent-expectations.md` (124 scenarios) from those alone, and only then opened the rule modules (not `tel-tests.l4` or `NOTES.md`) and wrote `tests-independent.l4`. It changed no expected value after reading the encoding, and confirmed with a deliberately wrong scratch assertion that the harness can fail.

## Result

107 assertions: **107 satisfied, 0 failed**.

## Differences noted without an assertion

- Where ss 69AC-69AD do not apply, the encoding answered that Chorus may stop supply; the author expected a refusal. **Changed**: it now refuses.
- A comment called the copper code's last submission day "the working day before"; the code takes the calendar day before, which the author also reads. **Comment corrected.**
- The Legislation Act s 55 helper in `tel-dates.l4` is unused (no deadline in scope ends on a non-working day); kept.
- Several Schedule 2A protections are single inputs; there is no function for ss 241-242 or for the scheme as appellant; s 69AE(b) has no function. Known limits.

## Not expressible (recorded in `independent-expectations.md`)

C13-C17 (now refused), Schedule 2A cl 1(3)(e) and (h) (P13, P14, P19), s 69AE(b) (T03, T04), ss 241-242 (D01-D09), the scheme as appellant (A04).

## After the review

The shared working-day module was also corrected for a Sunday 1 January (found by the Electricity Industry Act pass), with a regression test. `check.sh`: `tests-independent.l4` 107 satisfied; `tel-tests.l4` 29 satisfied; 7 modules, 136 satisfied, 0 failed, 0 other errors. The encoder's test that Chorus may stop a service outside ss 69AC-69AD was removed (now refused) and marked.
