# Independent test report: Circuit Layouts Act 1989 (Cth)

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the source text before `cla-rules.l4` was opened. `cla-tests.l4` and NOTES.md were not read. `tests-independent.l4` asserts those values against `the layout position for`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 39 | 0 |

**39 satisfied, 0 failed.** No disagreements with the encoding.

## Scenarios covered

Baseline: layout made 15 June 2000, first commercially exploited 2005, eligible maker, copy made 1 March 2015 without licence, Part II commenced 1 October 1990 (an assumed date; the Proclamation day is an input).

- Protection period, s 5: never exploited (ends 31 Dec 2010); exploited 2005 (31 Dec 2015); 2010, the last year "within 10 calendar years after" (31 Dec 2020); 2011, outside (31 Dec 2010); exploited in the year made (31 Dec 2010). Start edge: act the day before the layout was made (no infringement) and on the day made (infringes). End edge: 31 Dec 2015 infringes, 1 Jan 2016 does not.
- Eligible layout, ss 5 and 11: baseline; no creative contribution; commonplace; ineligible maker saved by first exploitation in an eligible country; ineligible maker with no such exploitation.
- Infringement, s 19: copying with and without licence; making an IC, including without knowledge of the missing licence (s 19(2) has no knowledge limb); commercial exploitation with and without knowledge (s 19(3)).
- Exceptions: s 20 (innocent acquirer; since aware without remuneration; since aware and paying); s 21 (private use; private use distributed to the owner's prejudice); s 22 (research copy, research IC); s 23(1)(a) (evaluation copy); s 24 (exhaustion); s 25 (Commonwealth defence).
- Action and remedies: act before Part II commenced (s 7: no action, no last day); action lies after commencement; s 27(3) innocent infringer (no damages, but the action still lies); aware infringer (damages); s 28 last day to sue for a 1 March 2015 infringement is 1 March 2021; no last day when there is no infringement.

## Coverage gaps

- s 28 for an infringement on 29 February: the encoding gives 28 February six years later. Whether the period ends on 28 February or 1 March is a reading question; not asserted.
- s 23(1)(b)-(d) and (2)(b)-(d) (a new original layout made from evaluation, and dealing in it): not modelled as inputs; a new original layout is a different layout, so this is outside the input shape rather than an error.
- "Authorises" limbs of s 19 and the s 9 exclusive right to authorise: not separate inputs.
- s 6 (temporary absence), s 13 (substantial part), s 15 (joint makers): folded into the boolean inputs; not testable separately.
- A first-exploitation year earlier than the year made (not possible on the facts) was not tested.
- s 27(4) additional damages: out of the brief's top-level question.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
