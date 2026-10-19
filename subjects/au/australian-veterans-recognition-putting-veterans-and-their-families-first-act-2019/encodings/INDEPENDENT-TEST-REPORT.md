# Independent test report: Australian Veterans' Recognition (Putting Veterans and their Families First) Act 2019

Expectations: `independent-expectations.md` (written from BRIEF.md and the source before reading the rules).
Tests: `tests-independent.l4`, run with `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 11 | 0 |

Scenarios 1-7 and 9 asserted (plus a same-day receipt and a no-claim case); all agree with the encoding, including the "beginning on" inclusive count (X + 89), the "whichever occurs later" rule when the information arrives before the claim, and a leap-year February.

## Failures

None.

## Gaps

- **Scenario 8, non-MRC claims.** There is no input saying which Act the claim is under. A Veterans' Entitlements Act or DRCA claim entered with a received date gets a 90-day date, although s 7(3) covers only MRC Act claims (others get only the s 7(2)(b) "proportionate to the complexity" commitment). The output's field name says "MRC Act claim", so the user is told; but a guard input would be safer.
- **Scenarios 10-11, s 9 pins, cards and artefacts** (veterans and family members) are in the brief's scope but not encoded; there is no family-member input or s 9 output.
- s 10 is encoded as a constant FALSE, which is right; s 10(2) (validity unaffected) and s 10(3) (no proceeding) are folded into that one flag.
- "Permanent Forces"/"Reserves" (Defence Act 1903 meanings) are a single user input; fine for a seat-level tool.
- Claims received before commencement (31 October 2019) are not distinguished; the Act is silent, not asserted.

## Change after the pass (encoder)

- No disagreements.
- The coverage gaps are recorded as known limits in NOTES.md.
