# Independent test report: First Home Super Saver Tax Act 2017 (Cth)

Expectations were written in `independent-expectations.md` from `BRIEF.md` and the source text alone, before any `.l4` file was opened. `tests-independent.l4` then asserted those expectations against `fhss-rules.l4`. No expected value was changed after the tests ran.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| fhss-rules.l4 | 0 | 0 | 0 |
| fhss-tests.l4 | 0 | 6 | 0 |
| tests-independent.l4 | 0 | 8 | 0 |

There are 8 independent assertions. All 8 pass, with no failures and no errors.

## Failures

None. The encoding agrees with my reading on these points:
- the 20% rate (s 4)
- the s 3 gate ("payable under section 313-60")
- the commencement boundary: 30 June 2018 gives NOTHING and 1 July 2018 gives tax
- a nil amount gives JUST 0
- no rounding: 1234.56 gives 246.912
- no cap

## Points of interpretation (not failures)

- The encoding hard-codes 1 July 2018 as the commencement date. Strictly, that date is in column 3 of the s 2 table, which s 2(2) says "is not part of this Act". The legal trigger is the commencement of Schedule 1 to the Treasury Laws Amendment (Reducing Pressure on Housing Affordability Measures No. 1) Act 2017. As a matter of fact the date is right, but the comment "s 2: the Act commenced on 1 July 2018" overstates what s 2 itself says.
- The date gate rests on the release date, as the brief directs. The Act does not mention release dates.

## Gaps

- I did not test a negative assessable amount. It is not meaningful under the ITAA 1997, and the encoding would return a negative tax.
- The encoding has no separate "is the tax imposed" predicate (s 3) apart from the amount. I tested imposition only through JUST/NOTHING.
- The ITAA 1997 concepts (s 313-60 liability, how the assessable FHSS released amount is worked out, the release caps) are inputs. They are out of scope and untested.

## Change after the pass (encoder)

- No disagreements in the results. The commencement comment was corrected (column 3 is not part of the Act).
- The gaps are recorded as known limits in NOTES.md.
