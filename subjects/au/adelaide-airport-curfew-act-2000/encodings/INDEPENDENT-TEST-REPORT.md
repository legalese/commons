# Independent test report: Adelaide Airport Curfew Act 2000

Expectations were written in `independent-expectations.md` from BRIEF.md and the source text before reading any L4. Then I read `aac-rules.l4` for names and input shapes only and wrote `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **24 satisfied, 1 failed** (its one error is that failed assertion; there are no syntax errors). The encoder's own aac-tests.l4 gives 15 satisfied.

## Scenarios

Curfew edges: 22:59 is out, 23:00 is in, 05:59 is in, 06:00 is out (s 3). An unpermitted "other aircraft" in the curfew commits an offence with a maximum of 200 penalty units (s 6). The shoulder permission works at 23:30 and 05:00 but not at 00:30 or 04:59 (ss 3, 9). LNHF with permission, a propeller aircraft of 34,000 kg or less and a specified jet are all permitted (ss 11-13). Taxi clearance before 11 pm permits a take-off but not a landing (s 14). An emergency, resumption by take-off, a dispensation and a national emergency are each permitted (s 16). The s 15(3) return deadline is landing day + 7: 25 Dec 2024 gives 1 Jan 2025, and 26 Feb 2024 gives 4 Mar 2024 (leap year).

## Disagreement

**tests-independent.l4 line 60 (scenario 17):** a *landing* at 01:00 by another aircraft with the special circumstance "resuming a flight interrupted by such an emergency". I expect it not to be permitted, so it is an offence with a maximum of 200 penalty units. The encoding permits it, because `it is permitted` treats any special circumstance other than `none` as a permission, whatever the movement.

Source, s 16: "An aircraft may take off from, or land at, Adelaide Airport ... if: ... (b) the aircraft is **taking off** from Adelaide Airport in order to resume the flight interrupted by such an emergency". Limb (b) is confined to take-off. Paragraphs (a), (c) and (d) cover both movements.

Confidence: high on the text. Practically this is a narrow edge, because a landing in that situation would usually fall under (a) itself. Still, the input shape allows the case, and the encoding answers it wrongly.

## Coverage gaps

- The s 15(3) return deadline is computed whenever a weather-landing date is supplied, even for a take-off or for "another aircraft" with no s 15(1)/(2) permission, and outside the curfew. Section 15(3) applies only to landings "in the circumstances referred to in subsection (1) or (2)". I did not assert those negative cases.
- Outside the curfew, `it is permitted under Part 3` is FALSE for an unlisted aircraft. That is harmless, since there is no offence, but it can read oddly. I asserted only the offence and penalty fields there.
- The s 9(6)/11(6) permission conditions (runway 23 for take-off, runway 05 or the weather, idle reverse thrust) are not modelled. A shoulder permission used at 23:30 is treated as complying with them.
- The four s 17 emergency limbs were spot-checked on one of them only (in-flight emergency).
- Penalty units are not converted to dollars (the Act defers to Crimes Act s 4AA).

## Change after the pass (encoder)

- The disagreement was accepted: resuming an interrupted flight permits only a take-off (s 16(b)).
- The gaps are recorded as known limits in NOTES.md.
