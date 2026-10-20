# Independent test report: DFRB (Pension Increases) Act 1967 (Cth)

Expectations (`independent-expectations.md`) were fixed from BRIEF.md and the source text before reading `dfrb67-rules.l4`. `dfrb67-tests.l4` and NOTES.md were not read.

## Result

`L4=~/.local/bin/l4 ./check.sh .` on `tests-independent.l4`: **21 assertions, 21 satisfied, 0 failed**. There are no errors.

Scenarios covered: the s 4 base case; current rate equal to and just above the actual entitlement; the 30 June 1967 eligibility edge (29 / 30 June); s 5 scaling for a commutation and for an election; s 6 deduction, combined with s 5, and an earlier increase larger than the new one (floored at nil); s 7 (NOTHING); s 13 for a pensioner; s 10 suspended pension; s 8 widow at five-eighths and at one-half, with the s 5 commutation disregarded but an election still applied, with the husband's s 6 deduction, with s 13 not applying to her, and where the husband had no increase; s 9 widow (NOTHING).

## Disagreements

None.

## Observations
- s 6 "reduced by": I expected the result not to go below nil (moderate confidence), and the code agrees.
- s 13 applies to a pensioner but not to a widow. The s 13 exception is for "a pension payable to a person as a widow", and the code agrees.

## Coverage gaps
- The s 3 definitions (actual pension entitlement, basic pension entitlement with its 1961/1963 retirement limbs, pension at current rate, notional rate of annual pay) are taken as inputs, so none of the s 3 or s 3(2) deeming is tested.
- The code leaves the increase unscaled under s 5 when the "rate without the commutation or election" is 0 or less (a divide-by-zero guard). This was not tested; the source does not contemplate it.
- For a widow, eligibility is tested by the husband's pension commencement date. For a s 8(1)(a) widow (member died before retirement) no pension ever began, so how that date input should be filled is unclear. Not tested.
- s 8(3)/s 9 precedence and s 7 are modelled as a single class choice, so overlapping classes (for example, a s 7 pensioner who is also a Superannuation Act pensioner) cannot be expressed.
- s 10 is applied with the same date test as s 4. A suspended pension that began after 30 June 1967 was not tested.
- ss 11, 12, 14 and 15 are out of scope.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
