# Independent test report: spi67-rules.l4

Expectations were written in `independent-expectations.md` from BRIEF.md and the source only, before the rules were read. Tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **17 satisfied, 0 failed**, and 0 errors. The existing spi67-tests.l4 has 9 satisfied and 0 failed.

## Failures

None.

## Points of interpretation that the code shares with my reading

- **Widow and s 4(2) (scenario 13).** The module subtracts the earlier increases before applying the widow's one-half or five-eighths, which matches my reading. With $50 of earlier increases, the result is 5/8 × (130 − 50) = 50. The Act is not clear on this. s 4(2) speaks only of an "eligible pensioner", and a widow is not one. A reviewer should confirm.

## Gaps

- **s 4(4).** The exclusion is a single boolean. The s 57 "unless contributions were made to a State Fund" carve-out is left to the caller. Scenarios 14-17 only test the boolean.
- **s 3 "actual unit entitlement".** This is the greater of the scale units and the actual unit contribution, but it is taken as an input and not computed. The module also does not check that case (b) really has contribution below entitlement. If case (b) is chosen with contribution above entitlement, the relevant amount comes out above $65.
- **s 3 relevant amount (c)-(e).** These are a supplied fraction (as the brief says). Their internal formulas are not tested.
- **s 7(1).** "From the first fortnightly payment after the commencing date" is not modelled as a date. The commencing date (Royal Assent) is not in the deposited text.

## Change after the pass (encoder)

- No disagreements.
- The gaps and the widow question are recorded in NOTES.md.
