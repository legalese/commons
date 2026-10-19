# Independent test report: Charities Act 2013

Expectations: `independent-expectations.md` (written from BRIEF.md and the source before reading the rules).
Tests: `tests-independent.l4`, run with `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 26 | 0 |

23 of the 25 scenarios asserted (all s 5 limbs (a)-(d); s 6 found/not found; s 7 presumption with and without evidence to the contrary; s 8 both ways; s 10(1) and (2); s 11(a) and (b); s 12(1)(l) and (i); incidental purposes), plus three extras (s 10 does not lift s 5(c) or 5(d); empty purpose list). All agree with the encoding.

## Failures

None.

## Gaps and observations

- **s 9 (native title / traditional rights), scenarios 20-21: not encoded.** There is no input for "directed to Indigenous individuals only", "fails only because of relationships", or "the entity receives, holds or manages native-title benefits". The only way to reach the s 9 result is for the user to enter "found to be for the public benefit" = TRUE, which hides the s 9 test. The brief lists s 9 in scope, so this is a coverage gap.
- **s 10 is one boolean** ("an open self-help group or contemplative order under s 10"). The five s 10(1) criteria and the s 10(2) "regularly undertakes prayerful intervention at the request of members of the general public" condition are not separately tested; the user must evaluate them. Scenario 23 (one s 10(1) criterion failing) could only be tested by entering FALSE.
- **s 11 disqualifying purposes** are one kind; (a) unlawful/contrary to public policy and (b) promoting or opposing a party/candidate are not distinguished, and the s 11(b) example (distributing information about party policies is not disqualifying) is left to the user's classification. Correct in outcome.
- **s 12(1)** non-presumed purposes (culture, reconciliation, human rights, security, animals, environment, analogous, and (l) advocacy) are one kind, "another charitable purpose under s 12(1)"; the (l) conditions (change in furtherance of (a)-(k)) and s 12(2) are left to the user. Scenario 16 therefore tests only the plumbing.
- **s 8 kind** is separate from s 7(c) "relieving poverty, distress or disadvantage"; a purpose that is both must be entered as one or the other. Either gives a result, but via different tests.
- **s 7 "found to be for the public benefit" = FALSE** is read as "no finding" rather than "found not to be"; with no evidence to the contrary a presumed purpose still passes. That is consistent with s 7 (a contrary finding presupposes contrary evidence), but users should set "evidence to the contrary" whenever there is a negative finding.
- **s 5(b)(ii) incidental purposes** are not tied to a specific qualifying purpose; the encoding requires at least one charitable purpose and that every purpose qualify, which yields the right result in every case I could construct (scenarios 11, 13).
- ss 13-17 are out of scope per the brief.

## Change after the pass (encoder)

- No disagreements.
- The coverage gaps are recorded as known limits in NOTES.md.
