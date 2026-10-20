# Independent test report: Services Trust Funds Act 1947

Expectations were written from BRIEF.md and the source text (`independent-expectations.md`) before any L4 was read; `stf-rules.l4` was then read for names and input shapes only.

## Result

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **29 assertions, 29 satisfied, 0 failed**, no other errors.

## Scenarios

15 scenarios: each of the three funds with a matching arm (ss 26, 29, 32); arm/fund mismatches (Army member to the Navy fund, Navy canteen staff to the Army fund, Navy member to the Air Force fund); every s 4 member category including "none of these"; the member applying in person, a person the trustees consider a dependant, and a person who is neither; s 14 bars for a trustee and a trustee's dependant; a "dependant" of a non-member.

## Disagreements

None.

## Observations (not failures)

- The third output, `whether and how much is for the trustees`, is a BOOLEAN that is TRUE only when I am in the class and not barred. Its name reads as "the trustees decide" (always true under s 8(a)) rather than "I may be considered for a benefit". I tested it as "may receive, subject to the trustees" and it behaved so, but the label may mislead a reader; the brief's question "Who decides whether I get anything?" is not answered by a named party in the output.

## Coverage gaps

- s 9 delegation (a regional committee or delegate forming the opinion) is not modelled; the dependant opinion is a single input.
- s 14 is input-level only ("trustee of the fund or a trustee's dependant"); a trustee of a *different* fund (who s 14 does not bar from this fund) cannot be expressed separately, so the per-fund scope of s 14 is untested.
- The regulations under ss 26, 29, 32 ("subject to and in accordance with the regulations") are outside the source bundle.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
