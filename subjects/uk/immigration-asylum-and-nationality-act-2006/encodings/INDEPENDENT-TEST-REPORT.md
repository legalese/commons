# Independent test report: IANA 2006 ss 15-25

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act (ss 15-25) before any `.l4` file was opened. `iana-tests.l4` was not read.

## Counts

- `tests-independent.l4`: **75 assertions, 75 satisfied, 0 failed**, 0 other errors.
- Whole encoding (`L4=~/.local/bin/l4 ./check.sh`): 7 modules, 0 errors, 120 satisfied (45 in `iana-tests.l4`, 75 here), 0 failed.
- Coverage: goal 1 — 18 assertions (every immigration position incl. both s 24 bail cases, 16th birthday edges incl. 29 Feb births in leap 2024 and non-leap 2100, contract for services vs service/apprenticeship); goal 2 — 31 (s 15(2) maximum incl. equality, the four (3)-(4) combinations, payable amount, six s 15(6)(c) dates across month ends and leap years, eleven s 17(4A)-(4E) cases incl. no objection, cancellation, increase, reduction/no action, no decision, and 2100); goal 3 — 22 (s 21(1), (1A), neither, not-disqualified-but-believed, bail, under-16, contractor, not subject to control, s 21(2)/(4) sentences by jurisdiction around 2 May 2022); top-level goal — 7 on one whole case.

## Failures

None. Every value I derived from the Act matched the encoding.

## Remarks on the encoding

1. **Adulthood over a period.** `the employee is an adult during the employment` tests the 16th birthday against `employed until`, so an employment that starts at 15 and continues past the 16th birthday is wholly "contrary to s 15". The Act makes it contrary to employ "an adult", so only the part from the 16th birthday is caught; the boolean answer (was there some contrary employment) is defensible, but the NOTES should say so. `employed from` is declared and never used.
2. **s 21 reuses the s 15 predicate.** `an offence under s 21 is committed` calls `the employment is contrary to s 15 in`. This is correct (s 21(1B) repeats s 15(1)'s words and ss 24-25 apply to both), but the shared rule's name hides that it is also the s 21(1B) test; a named `disqualified` predicate would read more isomorphically. The goal also does not say which subsection, (1) or (1A), is engaged, though their sentences are the same.
3. **s 22 is purely an input.** The body-corporate attribution (s 22(1)-(1A)) is folded into the `knew` / `had reasonable cause` booleans; there is no rule for it. Acceptable given the brief, but a scenario-level test cannot distinguish an individual employer from a body.
4. **`the penalty payable` returns 0** when no notice may be given, when excused, or when cancelled. The brief says never to answer 0 where the source does not answer; here 0 is arguably a real answer ("nothing payable"), but it conflates "excused" with "amount 0". Also, after a reduction on objection the caller must supply the reduced amount as `the amount specified`; after an increase the earliest pay-by date is still computed from the original notice's date unless the caller re-enters the new notice. Worth stating in NOTES.
5. **Date arithmetic** is exactly as the brief reads it (+28 for s 15(6)(c), +27 for s 17(4B)), with no working-day roll-over; the leap-year and 2100 cases all pass.
6. **Sentences.** Indictment 60 months; summary E&W uses the general limit from 2 May 2022 and 6 months before; Scotland and NI 6 months at any date. The top-level goal returns NOTHING for the maximum sentences when no offence is committed, which is a sensible choice.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md:
- adulthood is tested against the last day of the employment, so `employed from` is unused;
- s 22 is an input;
- the penalty is 0 when the employer is not liable, is excused, or the penalty was cancelled;
- after an objection, the caller enters the new amount.
