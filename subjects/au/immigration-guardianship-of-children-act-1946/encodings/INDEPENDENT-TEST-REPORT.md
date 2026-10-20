# Independent test report: Immigration (Guardianship of Children) Act 1946

Expectations were written to `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`check.sh`: tests-independent.l4: **29 satisfied, 1 failed**, no other errors.

## Scenarios

The 23 scenarios in `independent-expectations.md` cover each s 4AAA(2) companion, the s 4AAA(3) adoption-visa exception and its failure, the s 4AAA(4) direction route, the 18th-birthday edge (the day before and the day itself), leaving Australia permanently, the s 11 exemption, each s 6A/s 9 act with and without a lawful excuse, a child who is not a non-citizen child, and the s 11A 28-day and 45-day deadlines.

## Disagreement

**Scenario 13: the day guardianship ends.** I expected 1 June 2033, the 18th birthday. The encoding gives 31 May 2033, the day before. It names the field `the guardianship ends at the latest on`.

- Source: s 6(1) makes the Minister guardian "until the child reaches the age of 18 years". The child reaches 18 on 1 June 2033, which is the day the guardianship ends.
- The encoding's date is the **last day on which the Minister is guardian**. That is also defensible. The two readings agree on the law, because the encoding's `the Minister is guardian` is FALSE on the birthday (scenario 12 passes). They differ only on what the label means.
- Recommendation: rename the field to "the last day of guardianship", or return the 18th birthday. As it stands, a user who reads "ends on 31 May" may think the Minister is no longer guardian on 31 May.
- Confidence that this is a real (labelling) issue: moderate. Confidence that the substantive law is right: high.

## Agreements worth noting

- Scenario 17: helping a child leave without consent is an offence even with a "lawful excuse", because s 6A(3) has no lawful-excuse element and s 9 does. The encoding agrees.
- Scenario 15: the s 11 exemption removes guardianship and both offences. The encoding agrees, by making the child not a non-citizen child.
- Scenarios 22 and 23: notice + 28 days and receipt + 45 days. The encoding agrees.

## Coverage gaps

- The encoding folds s 4AAA(3)(b) (visa in force) and (3)(c) (adult will live in a declared State) into one boolean. So scenarios 7 and 8 could not be tested separately; both collapse to "FALSE", which passes.
- The s 4AAA(3) adult must be "not less than 21". The `another adult aged 21 or over` companion builds that in, so an adult under 21 (who would not satisfy (2)(b) or (3)) cannot be entered. That case falls to `no one`, which gives the same result.
- A relative under 21 cannot be represented. Under s 4AAA(2)(b) that child would be a non-citizen child, and the encoding can only express this as `no one`.
- s 11A(3)(a)(ii), the further period the Minister allows, is not modelled.
- s 6(1) "arrives after the commencement of this Act" is not an input, so any child is assumed to have arrived after 30 Dec 1946.
- The `the child may leave only with the Minister's written consent` field simply mirrors non-citizen-child status. It ignores whether the child has left permanently or the guardianship has ended for another reason. That is consistent with s 6A(1).

## Change after the pass (encoder)

- The disagreement was accepted: the guardianship's end is now given as the 18th birthday.
- The gaps are recorded as known limits in NOTES.md.
