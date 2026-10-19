# Independent test report: Customs Securities (Penalties) Act 1981

`tests-independent.l4`: **11 assertions, 11 satisfied, 0 failed**, no errors.

## Coverage

All 10 scenarios in `independent-expectations.md` pass:

- s 4 penalty = prescribed percentage x the value of the goods.
- The tender-accepted limb, and the refused-or-failed-when-required limb.
- s 3(2) value from the unit value. Where a unit value is set, it overrides any stated total value.
- Exact arithmetic with fractions (0.75), and the 0% and 100% edges.

## Disagreements

None.

## Gaps

- **Several s 4(b) limbs share one input.** "Refuses, or fails", "when required by a Collector under section 42" and "a security for payment of any penalty ... under the Customs Undertakings (Penalties) Act" are all one boolean. So scenarios 2, 4 and 5 test only that boolean. A demand under some other section, or for some other security, cannot be told apart.
- **Units with no unit value.** When there is no unit value, the module ignores `units`, which is correct. When there is one, it ignores `value of the goods`. Callers may not expect that, but it matches s 3(2).
- **No rounding.** The Act gives no rounding rule, and none was assumed.

## Change after the pass (encoder)

- No disagreements.
- The gap is recorded in NOTES.md.
