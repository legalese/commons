# Independent test report: Epidemiological Studies (Confidentiality) Act 1981

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, 26 satisfied, 0 failed. (The whole encoding: 41 satisfied, 0 failed.)

## Scenarios (24, 26 assertions)

1-3 s 4 offence for divulging and recording, with the penalty of 6 months or 10 penalty units; the purpose-of-the-study exception. 4 s 3(2) only a subject. 5 a study that is not prescribed. 6 a declared Commonwealth study (s 3(1)(b), s 9). 7-11 the s 7 recipients (a)-(d), with the no-consent side of (c). 12-13 s 5 access with and without the Minister's authorisation. 14-15 s 6 information from s 5 access, with and without the purpose of either study. 16 my own affairs only. 17-18 s 11 publication that does or does not identify anyone. 19-21 s 8(1), s 8(2), and NOTHING where the Act is silent. 22-24 s 10 oath.

## Disagreements

None.

## Coverage gaps and observations

- s 11: an identifying publication is tested only as "the non-identifying flag is false". The encoding has no separate input for a publication that identifies someone, so 18 is the same case as 1. That is adequate, because s 11 only protects publications that identify no one.
- s 7 and making a record: s 7 speaks only of "giving information". The encoding never lets s 7 save a record, and I agree. I did not test it separately.
- s 7(c): consent is folded into the recipient enum. Without consent, the user must pick `someone else`, so the rule cannot see whether consent was given.
- s 8 for a prescribed-study assistant whose information came "otherwise" returns NOTHING, which I did not test. s 8(1)(a) covers documents "prepared or obtained in the course of the conduct of that study" whether or not I personally acquired them, so this may be arguable. Confidence that it matters: low.
- s 10 "is about to become" a person to whom s 4 applies: no input distinguishes it, so it was not tested.
- s 9 (State officer, employee, contractor, unpaid) is folded into one "assist" value, so the variants cannot be tested separately.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
