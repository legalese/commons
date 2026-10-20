# Independent test report: Parliamentary Privileges Act 1987 (Cth)

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the source text before `pp-rules.l4` was opened. `pp-tests.l4` and NOTES.md were not read. `tests-independent.l4` asserts them against `the privileges position for`. Two extra s 14 scenarios (22b, 22c: two sitting days; a month boundary) were added while writing the tests; their values come from the text of s 14(1)(e), not from the code.

## Result

`L4=~/.local/bin/l4 ./check.sh .`

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 34 | 0 |

**34 satisfied, 0 failed.** No disagreements with the encoding.

## Scenarios covered

- ss 4, 6, 7 (House punishment): natural person with improper interference (may punish; 6 months; $5,000); corporation ($25,000); no improper interference (cannot punish; fine 0); only defamatory outside the House's presence (cannot, s 6(1)); in its presence (can, s 6(2)); interference that is not only defamatory (can).
- ss 12-13 (offences): s 12(1) witness intimidation by a natural person (offence, 6 months, 50 penalty units) and a corporation (250 units); s 12(2) injury on account of evidence; s 13 unauthorised in camera disclosure (offence, 6 months); in camera evidence already published by a House (no offence); no conduct (no offence, 0 units).
- s 14 (immunity), sitting day 10 March 2025: member on the day, 5 days after and before (immune), 6 days after and before (not immune); officer 5 and 6 days after; witness on the day required (immune) and the next day (not immune); no role (not immune); member with two sitting days; member across a month boundary.

## Notes and coverage gaps

- s 7(7) (no fine where imprisonment is imposed) is expressed by reporting two separate maxima; the "not both" rule is not itself a computed output, so it is not tested.
- Corporation's House imprisonment maximum: the code gives 0 months. s 7(1) speaks of "a person"; a corporation cannot in practice be imprisoned. Not asserted (my expectations did not fix a value).
- s 13 has two exits, "without the authority of a House or a committee" and "unless a House or a committee has published, or authorised the publication of" the evidence. The encoding has one input for the second; acting with a House's authority to disclose otherwise unpublished evidence (expectation 12) has no separate input, so scenario 12 was not asserted. Minor gap.
- s 14(1) distinguishes the member's own House meeting from a committee of which the member is a member; the encoding takes one list of sitting days, so it relies on the caller to list the right days. s 14(2)(c) for officers likewise.
- s 12 is satisfied whenever the conduct is selected; the elements (fraud, intimidation, improper means) are folded into the input.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
