# Independent test report: Defence Forces Special Retirement Benefits Act 1960

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text only, before any L4 was read. `tests-independent.l4` asserts them against `dfsrb-rules.l4`.

## Result

`check.sh`: tests-independent.l4 — 0 errors, **42 satisfied, 0 failed**. (A first run had one L4 parse error from a multi-line record literal inside a field access; reformatted on one line, no expected value changed.)

## Scenarios asserted (all agreeing)

- s 4: prescribed period 1 Feb - 30 Apr 1961 (3 months) or to 31 Oct 1961 (Ordnance Corps, 9 months); discharge on 30 Apr vs 1 May; engagement expiring 30 Apr vs 1 May; 55th birthday before the proclaimed date, on it, inside the period, just after it, and inside the 9-month Ordnance period; officer, not declared, re-enlisted next day, not male/contributing, not discharged for the reduction.
- s 6: £20 x 5 = £100.
- s 7: 14 x (£2 + £0.525) x years at 6, 14 and 16 years (16 years without reaching 20 by 55 falls to s 7, not s 9).
- s 9: First Schedule max (cat 101 at 15 and 19 years, cat 105 at 17), full / partial / no contribution, reduced benefit contributor's Board maximum.
- Prescribed day one month after service (15 Jun -> 15 Jul 1961; 31 Jan -> 28 Feb 1962); payment the day before counts, payment on the prescribed day does not ("before the prescribed day").
- s 10(5)(a)-(f): both kinds of contributor, every payment band.
- No benefit when the Act does not apply.

## Disagreements

None.

## Coverage gaps and observations

- s 5 service for pension, the "would have completed 20 years by 55" test, the Board/Actuary figures and the s 10 maximum pension rate (a hypothetical s 41 rate) are inputs, so their derivation is not tested.
- A contribution greater than the maximum additional pension contribution: the Act provides only for "equal to" or "less than"; the module treats any larger payment as yielding the maximum rate. Not asserted; a reasonable reading but not licensed by the text.
- A late contribution is treated as no contribution (minimum rate); the Act is silent on what happens to the money (refund), which is out of scope.
- s 9(7)/10(7) (payment by widow after death, Board-allowed later day) are out of scope and untested.
- The month-end rule for "one month after" (31 Jan -> 28 Feb) agrees with my reading; confidence medium, since the Acts Interpretation Act month rule is not in the source bundle.
- Dates of birth on 29 February were not tested.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
