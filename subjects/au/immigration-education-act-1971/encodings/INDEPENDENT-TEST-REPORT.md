# Independent test report: Immigration (Education) Act 1971 (`ie-rules.l4`)

## Method

An earlier tester left `independent-expectations.md` (scenarios 1-21) and `tests-independent.l4` (lines 1-92) but no report. I reviewed both against BRIEF.md and `../registers/source-bundle/C1971A00003.txt` alone, before opening `ie-rules.l4`. Every expected value in scenarios 1-21 matches my reading of ss 3, 4A, 4B, 4C and 4D, so none was changed. I added scenarios 22-26 (under-18 registration window, start extension both sides, no deadlines for a VCD on 1 Oct 2020, adult 6-month limit), then read `ie-rules.l4` for names only and added the assertions at lines 93-106.

Period convention (applies throughout): "the period of N months starting on" day D includes D and ends the day before the corresponding day N months later (VCD 1 Mar 2023: 6 months ends 31 Aug 2023, 12 months ends 29 Feb 2024, 5 years ends 29 Feb 2028). An extension of N days moves the last day N days later.

## Scenarios

Scenarios 1-26 are listed in `independent-expectations.md`. Together they cover all four s 4A(1)(a) routes plus "none", vocational English (s 4A(1)(b)), every s 4B(1) limb (a)-(e) and the "while he or she is eligible" condition, the 18th-birthday edge on the VCD, both sides of the 6-month, 12-month and 5-year limits, all three extensions, and the 1 October 2020 commencement edge (ss 4C(1A), 4D(1A)).

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, **44 satisfied, 0 failed**. ie-tests.l4: 17 satisfied, 0 failed.

## Disagreements

None.

## Coverage gaps and observations

- **s 4B(1)(b) age date and the s 3 VCD are not the same day.** s 4B(1)(b) measures age on the first day in Australia after the *permanent* visa came into effect. The s 3 VCD is the *earlier* of that day and the specified-temporary-visa day. The encoding uses the VCD for both. They differ only for someone who held a specified temporary visa before their permanent visa, and that case can't be expressed with these inputs (status is a single value), so it isn't tested.
- **History is a single status.** s 4C(1) and s 4D(1) apply if the person has *ever* held a permanent or specified temporary visa. Status (iv) (a child of a permanent-visa parent) is treated as outside ss 4C and 4D. That fits a child who holds no visa of their own. A child who also once held a permanent visa can't be represented. Not tested.
- "Is in Australia" (s 4A(1)(a)) is folded into the status input. Vocational English and the extensions are inputs, as the brief says. The s 4C(4) and 4D(4) application windows are out of scope.
- No test asks about a day before the VCD.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
