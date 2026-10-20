# Independent test report: Judges (Long Leave Payments) Act 1979 (Cth)

Expectations (`independent-expectations.md`) were fixed from BRIEF.md and the source text before reading `jllp-rules.l4`. `jllp-tests.l4` and NOTES.md were not read.

## Result

`L4=~/.local/bin/l4 ./check.sh .` on `tests-independent.l4`: **24 assertions, 23 satisfied, 1 failed**. There are no other errors.

Scenarios covered: the 10-year threshold (9.9 / 10); the 52-week cap (10, 12 years); qualifying service shorter than service (long leave taken); completed-year flooring (10.9 → 10, 9.9 → 9); death with each payee (spouse, dependants, legal personal representative); death with under one completed year; compulsory age with 6 / 5.9 / 9 / 20 years (s 4(2A) against s 4(1)); a disability certificate (s 4(2B)) and resignation without one; removal with and without a Governor-General direction (s 7); consecutive appointment (s 3A); an excluded office (High Court); Judge limbs (b) and (c); a different salary.

## Disagreements

### 1. Payee when the amount on death comes to zero (scenario 10)
A Judge dies with 0.5 years of qualifying service and leaves a spouse. s 4(1)(b) makes an amount payable "whether or not he or she has completed 10 years' service", and s 4(2)(b) computes it as 0 weeks (no completed year). I expected the payee to be the surviving spouse (s 5(2)(a): "An amount payable under section 4 on the death of a Judge is payable to ... that surviving spouse"). The code returns `no one` because its `the recipient for` returns `no one` whenever the weeks are 0. With a nil amount there is no practical consequence. Confidence: moderate on the reading, but the stakes are low. It is a matter of presentation: the code conflates "nothing is payable" (s 7, s 3A, under 10 years) with "a nil amount is payable".

## Observations (agreements)
- s 4(2A)/(2B) amounts are not capped at 52 weeks (s 4(2C)). In practice the cap could not bind, because s 4(2A)/(2B) apply only when s 4(1) does not, so service is under 10 years.
- A Judge removed under s 72 with a Governor-General direction is paid under s 4(1)(a) if they have 10 years. A removal with a direction and under 10 years gives nothing (not tested; agreed by reading).
- A disability certificate on retirement with 10+ years: s 4(1) applies and the cap applies (agreed by reading, not tested).

## Coverage gaps
- The code accepts qualifying service greater than service. No test covers this, because the source treats qualifying service as a subset of service.
- Death in office where a new appointment flag is set (meaningless combination) was not tested.
- s 4(2A)(a) requires that the Judge "is to cease to hold office upon attaining a particular age". The input is a single `Ceasing` value, so there are no tests for a Judge who has no compulsory age.
- s 5(2A)-(4) distribution directions are out of scope.

## Change after the pass (encoder)

- The disagreement was accepted: a nil amount payable on death is now paid to the spouse.
- The gaps are recorded as known limits in NOTES.md.
