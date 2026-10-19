# Independent test report: Communications Act 2003 (UK)

I wrote the expectations (`independent-expectations.md`, 67 scenarios across the three goals) from BRIEF.md and the source text before opening any `.l4` file. I then wrote `tests-independent.l4` against the names in `ca03-types.l4`, `ca03-rules.l4` and `ca03-goal.l4`. I did not read `ca03-tests.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| ca03-tests.l4 | 0 | 66 | 0 |
| tests-independent.l4 | 0 | 95 | 0 |
| TOTAL (5 modules) | 0 | 161 | 0 |

`fails.sh tests-independent.l4` prints nothing.

## Disagreements

There are none. All 95 independent assertions pass. They cover:

- day before / on / after each limit in s 127(5), with each of the two limits binding in turn;
- the month-end cases: no 31 February (28 Feb 2026), the leap year (29 Feb 2024), an offence on 29 February (last day 28 Feb 2027), and 28 August + 6 months (27 Feb);
- s 128(3) urgent (+7 days, also across a year end) and non-urgent (one month, including from 31 January in a common and a leap year);
- ss 129/130 "has expired": Ofcom may not act on the last day, and may act the day after;
- the s 124U(2) cap both ways, the equal case, and a fractional share (625/6);
- every exception: s 124U(1)(a) no equipment, s 124U(3) M2M, the s 124U(4) waiver (consumer, microbusiness, not-for-profit), s 124V, s 127(4), and s 363(5)-(6);
- s 365A(2) ages, including a 29 February birthday in a common year and in a leap year, a birthday on the month end, and a concession age of 75;
- s 366(4) month ends and the leap year;
- the £2,000,000 cap each way;
- the top-level goal.

One point I took as a matter of interpretation agrees with the code. In M23, the period Ofcom gave was shorter than the s 128(3) minimum, and I read the Act as saying Ofcom may not then act under ss 129(1)/130(1). The brief says nothing on this. The code requires the period to be long enough, which is the same reading.

## Gaps in the encoding (no assertion could test these)

1. **s 363(3) is not encoded.** This is the offence of having a receiver in your possession or under your control with intent to install or use it unlicensed, or knowing that someone else intends to. Scenario T9 had no function to test. It is within the end-user's question "do I need a TV licence".
2. **s 363(1) / 368(3) are collapsed into one input**, "I install or use a receiver for TV or BBC on-demand". So the code never decides two things the user asked about:
   - installation without use (T8: under s 363(1), "must not be installed or used", installing alone is an offence);
   - non-BBC on-demand use, which is not "use" (T4).

   The user decides both when they fill in the boolean, so my tests only confirm that the code passes the input through.
3. **The s 51(8) definition of a bundled contract is not computed.** It is an input. This is allowed by the brief's input list, but the brief puts s 51(8)-(9) in scope.
4. **The s 124U(2)(b) share is not guarded.** If `agreed contract months` is 0, the code divides by zero. If `unexpired months` exceeds `agreed contract months`, it gives a share above the agreed value. Under the brief's convention these inputs should be REFUSE.
5. **s 124V uses the same "right to terminate early" flag as s 124U(1).** s 124V(1)(b) asks for a right to terminate an element because it did not conform or was not supplied. The code requires both flags, which gives the right answer here. But a right to terminate for a different reason, together with a non-conforming element, would wrongly satisfy s 124V.
6. **s 127(5) only, not s 127(6).** The code models the time limit for England and Wales and Northern Ireland. s 127(6) has the same limits for Scotland, but proceedings there are deemed commenced under s 136(3) of the 1995 Act. The export text says "England and Wales or Northern Ireland", so this is a disclosed choice. The code also does not check for an information laid before the offence date or before the evidence date.
7. **s 366(4) gives only the last day.** Whether a given entry falls between the grant and that last day is left to the caller. My test helper `entry allowed` supplies it.
8. **s 365(5A)/(5B) are not modelled.** These are regulation-made concessions with an age below 65, and the residential-care concession. The brief scopes them out, apart from the "65 or higher" check.
9. **s 128(4) urgency is a single boolean.** It is not the conjunction of "continuing" and "must be stopped as soon as possible", so scenario M18 is only a pass-through.
10. **Penalties are only checked against the cap.** A negative or zero penalty is not checked. s 130(4)(a)-(b) (appropriate and proportionate) is left to Ofcom, which is acceptable.

## Change after the pass (encoder)

- No disagreements to resolve.
- The gaps listed above are recorded as known limits in NOTES.md.
