# Independent test report: Defence Forces Retirement Benefits (Pension Increases) Act 1971

Expectations were written in `independent-expectations.md` from BRIEF.md and the Act before any `.l4` file was opened; `tests-independent.l4` asserts them against `dfrb71-rules.l4`. The module returns `JUST 0` where s 5's trigger is not met, so "none" is asserted as `JUST 0` there and `NOTHING` where the Minister determines the rate.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 16 assertions, 15 satisfied, 1 failed (the 1 error is that failure). The author's dfrb71-tests.l4: 10 satisfied, 0 failed.

Covered: s 5 with a whole and an exact-fraction result (1500/7); the trigger failing when the current rate equals and when it is below the actual entitlement; s 8 scaling; s 10 reduction and its nil floor; ss 11, 13 and ss 4/6/7 as NOTHING; s 12 five-eighths, with the husband's commutation disregarded, with his earlier increases still deducted, the s 12(2) one-half, and a husband with no increase.

## Failures

1. **L30, order of s 8 and s 10.** Pensioner: current 1400, actual 1000, basic 700 (s 5 gives 500), commuted (payable 800, uncommuted 1000), earlier increases 120. Expected 400 - 120 = **280**; the module gives (500 - 120) x 800/1000 = **304**. The module deducts s 10 first and then scales by s 8. s 8(1) replaces "the increase to which, but for this section, he would have been entitled in accordance with [the preceding provisions]", that is ss 4-7, which means the s 5 figure before s 10. s 10 then reduces "any increase in the rate of his pension to which he is entitled under the preceding provisions of this Act", and those provisions include s 8. So s 8 applies to the s 5 figure and s 10 to the result. The two readings give the same answer only when there is no commutation or no earlier increase. (The brief lists s 8 before s 10 but does not state an order.)

## Gaps and reading differences

- **s 12 and the husband's s 61A/61B election.** s 12(1) disregards s 8 only "in so far as it applies by reason of the commutation" under s 74. Where the husband's s 8 reduction came from an election under s 61A or 61B, s 8 should still reduce the widow's figure (my example: husband 400 after s 8 -> widow 250). The module ignores the s 8 inputs for every s 12 widow and has no input saying whether the reduction was a commutation or an election, so I could not test this; the module would return 312.5.
- **s 10 floor at nil**: the Act does not say "not below nil"; the module and the brief floor it. I agree it is the sensible reading but it is an inference.
- **s 21 date of effect** (first fortnightly payment after commencement) is not an input or output of the module; not testable.
- **s 18** (no increase for someone also entitled under the Superannuation Act 1922-1971, other than a widow or child), **s 9** (commutation on or after commencement), **s 15** (suspended pensions) and eligibility (pension payable before 30 June 1971) are not modelled; outside the brief's scope.
- The s 5 trigger result is `JUST 0` rather than `NOTHING`, so "not entitled under s 5" and "entitled to nil after s 10" look the same.
- When `rate without commutation` is 0 the module skips s 8 silently; a caller who leaves both rates at 0 gets the unscaled figure.

## Change after the pass (encoder)

- **The order of s 8 and s 10.** Accepted: s 8 scales the s 5 increase, and s 10 then deducts earlier increases (F1).
- The gaps are recorded as known limits in NOTES.md.
