# Independent test report: Defence (Parliamentary Candidates) Act 1969

Expectations were written from BRIEF.md and the source text (`independent-expectations.md`) before any L4 was read; `dpc-rules.l4` was then read for names and input shapes only.

## Result

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **38 assertions, 38 satisfied, 0 failed**, no other errors.

## Scenarios

- Routes out (ss 7-9): officer, enlisted, Reserve on CFTS, another member, Chief not satisfied (5).
- Last day to apply (ss 10(1), 11(1), 12(1)): 15 Mar 2020, 31 Dec 2019 (leap-year month-end), 31 Dec 2020 (month-end), 30 Nov 2020 (4).
- Application in time: on the last day, one day after, late with the Chief's further period (3).
- Compulsory reinstatement (ss 13-14): officer with notice on the last permitted day (15 April) and one day late; enlisted with notice in time (deemed applied and re-enlisted, with s 11(2) LSL and s 17 repayment following) and late; CFTS member (no s 13/14 power); elected member; no notice; member who applied himself.
- Time away and gratuity (ss 10-12, 17): reinstated officer, enlisted, CFTS; not reinstated.

## Disagreements

None.

## Coverage gaps

- ss 10(3), 11(3): the time away does not count toward an officer's fixed-term appointment or an enlisted member's engagement. No output covers this; untested.
- s 17(3): "gratuity" excludes a gratuity under the Defence Forces Retirement Benefits Act; the input is a single amount, so the exclusion cannot be tested.
- s 6 (the declared date itself, including the 30-days-after-return-of-writ rule in s 6(3)) is an input; untested.
- The inputs `my service`, `I have left under the Act` and `I have been reinstated` are independent, so inconsistent combinations (e.g. "another member" who "has left under the Act") are accepted without complaint; I did not test them.
- The application deadline uses the same "two months after" rule for all three routes; tested only once per route.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
