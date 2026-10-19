# Independent test report: Customs Undertakings (Penalties) Act 1981

`tests-independent.l4`: **11 assertions, 11 satisfied, 0 failed**, no errors.

## Coverage

All 11 scenarios in `independent-expectations.md` pass:

- s 4(1) penalty = prescribed percentage x the value of the goods.
- No breach gives a nil penalty.
- s 4(2)(a) proportional reduction by quantity, and s 4(2)(b) by value.
- s 3(2) value from the unit value, including combined with a reduction.
- Edge reductions of 0 and 999/1000.

## Disagreements

None.

## Gaps

- **The s 4(2) conditions are not rules.** "During the period, or each of the periods, specified" and "under an item ... to which the undertaking relates" are not checked by the module. The caller must count only the qualifying entries in `entered in partial compliance`. So scenarios 6 and 7 (entries outside the period, or under an unrelated item) can be expressed only as entered = 0, and they test nothing in the code.
- **Quantity versus value is not checked.** s 4(2)(a) and (b) are told apart only by what the caller puts in `required for full compliance` and `entered in partial compliance`. Nothing checks that the two are in the same unit.
- **Entered more than required.** The module caps the share at 1, so the penalty is nil. The Act is silent; this was not asserted.
- **Required = 0.** The module gives no reduction. This is reasonable, but it was not asserted.
- **s 3(1) "Customs undertaking".** The ss 267(1) and 268(2) undertakings, and varied ones, are not distinguished by any input. Scenario 10 just checks the arithmetic.
- **No rounding.** No rounding rule was assumed.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded in NOTES.md.
