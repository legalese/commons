# Independent test report: Superannuation (Pension Increases) Act 1971

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text only, before any L4 was read. `tests-independent.l4` asserts them against `spi71-rules.l4`.

## Result

`check.sh`: tests-independent.l4 — 0 errors, **15 satisfied, 0 failed**.

## Scenarios asserted

Expectations 1-5, 7-13, 15 and 20, all agree with the module:
- s 4 both sides of the threshold (adjusted > / = / < actual), 1 and 2 additional units.
- s 5 scaling (130 x 600/800 = 97.50).
- s 6 deferred scaling, with and without s 6(2) units.
- s 7 reduction, including reduction below nil floored at $0, and the order s 5 then s 7.
- s 8 five-eighths and one-half, and five-eighths of the s 7-reduced figure.
- s 9 exclusion, for a pensioner and for a widow.

## Disagreements

None.

## Coverage gaps (not testable through the module's inputs)

- Expectations 17-19 (the s 3 "actual unit entitlement" rules: greater of scale and actual contribution for contributors; lesser of scale and four units for non-contributing pensioners) cannot be tested: actual unit entitlement is a raw input. Likewise "adjusted unit entitlement" and the notional annual salary are inputs (the Treasurer's determination).
- Expectation 6 (s 5 does not apply to a deferred pension) is enforced structurally by the one-of `Scaling case`; the caller must choose. Whether a case falls within s 5(1)(a)-(e) is not modelled.
- Expectation 14 (election made but revoked) and 16 (s 57 pension with State Fund contributions is not excluded) reduce to the caller's choice of spouse case / the `an excluded pension` flag; no rule distinguishes them.
- Observation, not a disagreement: where the s 5 denominator or the s 6 unit figure is 0, the module returns the unscaled s 4 increase. The Act gives no answer for a zero denominator; this is a defensive default.
- s 8(2)-(4), s 10 (Schedule pensions) and ss 11-13 are out of scope per the brief.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
