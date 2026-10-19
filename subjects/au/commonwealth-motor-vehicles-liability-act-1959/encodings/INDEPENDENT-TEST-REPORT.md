# Independent test report: Commonwealth Motor Vehicles (Liability) Act 1959

Expectations: `independent-expectations.md` (written from BRIEF.md and the source before reading the rules).
Tests: `tests-independent.l4`, run with `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 18 | 0 |

Scenarios 1-11 and 13 asserted; all agree with the encoding.

## Failures

None.

## Gaps (expectations the encoding cannot express)

- **Scenario 12, s 5(1)(b) contribution claims.** The record has a single "claim against the Commonwealth or an authority" flag; a contribution claim *by* the Commonwealth is not distinguished. Setting the flag TRUE for a contribution claim gives the s 5 presumption (right) but also gives s 6 (which, on my reading, covers only a damages claim against the Commonwealth). Not asserted.
- **Scenario 14, s 6 "proceedings in a Court of a State or Territory".** No input for the forum; s 6 is answered TRUE for any forum.
- **s 5(3) and s 6 for pre-commencement occurrences.** The encoding applies s 6 regardless of date; the Act extends only s 5 back to 9 September 1958. Not asserted either way (I treat it as an open question).
- **s 5(1A) "at all relevant times"** is collapsed into one boolean, so a partial registration must be entered as FALSE by the user; the encoding's field name says so, which is adequate.
- The "Commonwealth authority" definition (s 3(1), including the ACT/NT and incorporated company exclusions) is left to the user; there is no input for it.
- s 5(2) (no ratification) is not encoded; it has no computable consequence for the seat.

## Change after the pass (encoder)

- No disagreements.
- The coverage gaps are recorded as known limits in NOTES.md.
