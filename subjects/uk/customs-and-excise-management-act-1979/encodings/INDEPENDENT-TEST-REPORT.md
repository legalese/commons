# Independent test report: CEMA 1979 encoding

## Method

1. Read BRIEF.md and the Act only (s 146A, s 149, s 170, Schedule 1, Schedule 3), and wrote `independent-expectations.md`: 64 scenarios across the three goals, each with the Act's words, plus seven recorded ambiguities. This was done before any `.l4` file was opened.
2. Then read `cema-types.l4`, `cema-forfeiture.l4`, `cema-penalties.l4`, `cema-time-limits.l4` and `cema-goal.l4` for names and record shapes. `cema-tests.l4` was not read.
3. Wrote `tests-independent.l4` asserting the pre-recorded values. No expected value was changed after the run.

## Counts

| | |
|---|---|
| Scenarios in expectations file | 64 (F1-F11, C1-C10, D1-D9, O1-O11, P1-P19, T1-T6, S1-S11) |
| Assertions in `tests-independent.l4` | 90 (including 8 on the top-level goal) |
| Satisfied | 90 |
| Failed | 0 |
| Non-assertion errors | 0 |
| `check.sh` total across all modules | 0 errors, 126 satisfied, 0 failed |

A deliberately wrong assertion was appended to a scratch copy and failed as expected, so the assertions really do evaluate.

## Failures

None.

## Scenarios that could not be tested as written

The input model is coarser than the Act in three places, so some scenarios could not be expressed:

- **F2-F11 (Sch 3 para 1(2) presence exceptions).** All of them collapse into one boolean, `seized in the presence of the offender, owner, possessor, master or driver`. I could test the boolean in both directions, and the para 1(1) "owner known" condition. I could not test the conditions inside (c) and (d):
  - F8: master present, goods seized from a vehicle;
  - F10: driver present, goods seized from a ship.

  In both, the Act requires notice: the master or commander counts only "in the case of any thing seized on or from any ship or aircraft", and the driver only for a thing seized "on or from a vehicle". The field name lists "master or driver" without these qualifications, so a caller could set it TRUE and wrongly get "notice not required". I suggest either one field per limb plus a "seized from ship/aircraft/vehicle" field, or a field comment that states the qualifications.
- **O9 and O10 (s 170 kinds of goods and limbs).** The model has no inputs for the s 170(1)(a)(i)-(iii) categories, for which limb of (1) or (2) applies, or for whether the case concerns a prohibition or restriction.
  - s 170(5) is applied whenever the "corresponding offence" flag is set. The Act limits it to an offence "in connection with a prohibition or restriction". A corresponding offence under "the enactment ... imposing the prohibition" presupposes a prohibition, so the risk in practice is small.
  - Goods outside (i)-(iii) (O10) can only be modelled by the caller setting the knowledge flags FALSE.

## Remarks

1. **Every date reading matches the brief.** This covers:
   - Sch 3 para 3: the one-month clamp on 31 Jan, both leap and non-leap.
   - s 146A(2): 20 years, including an offence on 29 Feb with a valid corresponding date, and 1 Mar 2004 ending on 29 Feb 2024.
   - s 146A(3): the earlier of the two summary limits, in both directions, including ties at the boundary and the six-month clamp to 28 or 29 Feb.
2. **Ambiguity 3 (offence on 29 Feb, summary limit).** The 3-year period from 29 Feb 2020 has no corresponding date. The helper `the last day of the n months beginning with` gives 28 Feb 2023, which matches my reading (S8). It reaches this because the clamped date's day differs from the start day, so it does not subtract a day. The behaviour is right, but it depends on that day-mismatch test. A comment in the helper would make the 29 Feb case explicit.
3. **Evidence after the 3-year period (S10).** The goal returns the 3-year end date, which is earlier than the evidence date, so proceedings were already barred. That matches the Act's "subject to that". A caller may misread it as a live deadline, and a note in the `@export` text would help.
4. **Penalties.** The Act's text is followed:
   - Class C ignores the fixed sum (P13: £3,000, not £20,000) and has the £500 floor.
   - Seal skins take the fixed sum alone, with no three-times-value alternative.
   - "Any amount" on indictment is NOTHING.

   One assumption: s 170(4B)'s "statutory maximum £20,000" is taken to be the same input as s 170(3)'s "prescribed sum £20,000". This is reasonable given how the bundle prints both, but it should be recorded in NOTES.md.
5. **Para 3 is per claimant.** It speaks of a notice "served on him". The model holds one notice date per seizure, which is fine for a single claimant.
6. **Top-level goal.** It correctly gives NOTHING for the maximum penalties when no offence is made out, and NOTHING for every field whose input is absent.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md:
- the para 1(2) exceptions are one input (F4);
- s 170(5) is applied as an input (F7);
- a barred summary prosecution (F6);
- the seal-skins sum is the same input as the fixed sum (F2).
