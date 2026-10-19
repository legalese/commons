# Independent test report: Superannuation (Distribution of Surplus) Act 1974

Expectations written first in `independent-expectations.md` (from BRIEF.md and the source only), then asserted in `tests-independent.l4` against `sds-rules.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| sds-rules.l4 | 0 | 0 | 0 |
| sds-tests.l4 | 0 | 10 | 0 |
| tests-independent.l4 | 1 | 20 | 1 |

The one error is the one failed assertion; no syntax or type errors.

## Failure

**L20, A4: became a pensioner on 1 July 1962.** Expected eligible contributor; the code says not eligible.

`within the window` uses `d GREATER THAN the relevant period starts` with the start set at 1 July 1962, so the first day of the period is excluded. The Act says "after the commencement of the relevant period" (s 3(1)(b) and (c)). The relevant period is "the period of 10 years that ended on 30 June 1972", so it begins at the start of 1 July 1962. An event during 1 July 1962 happens after the period has commenced. The brief says "after 1 July 1962", and the code follows the brief, so the disagreement goes back to how the brief paraphrased the Act. The fix would be `d AT LEAST the relevant period starts`, or to treat the start as 30 June 1962 with a strict comparison. The same off-by-one applies to limb (c), deaths on 1 July 1962. This matters only for events on that single day, and a lawyer should confirm the reading.

## Agreements worth noting

- Before 11 April 1974 is strict: an event on assent day is out and the day before is in (A5, A5b).
- The limb (c) dependant condition, the s 119W exclusion, the non-contributory exclusion, the s 3(2) deeming, and the s 6(2) widow/Board split all behave as I expected.
- A person excluded as a contributor by s 119W but deemed a pensioner by s 3(2) is still paid (A17b).

## Gaps

- **s 4 amounts are not encoded.** The brief names $52,525,000 and $17,490,000 (total $70,015,000), but the module has no definitions for them, so A19 could not be asserted.
- **Several date tests are booleans in the model.** These facts are taken as yes/no answers: when the obligation to contribute arose (before the end of the period), whether deferred benefits were applicable "on or before 30 June 1972", and whether a pension was payable in the period. So the 30 June / 1 July 1972 boundaries (A9, A10, A11, A12, A16) are the user's job and cannot be tested in the code. A10 and A12 are untestable. A9, A11 and A16 are tested only at the level of the flags.
- **The model allows inconsistent inputs.** For example, `deferred benefits not yet payable on 30 June 1972` can be TRUE while `deferred benefits applicable by 30 June 1972` is FALSE, and nothing checks for it. Dates of becoming a pensioner and of death can also both be given.
- s 5 allocation and s 7 assignment are out of scope, as the brief says.

## Change after the pass (encoder)

- **A4 (a pensioner from 1 July 1962).** Accepted: the period's first day is inside the window (F1).
- The gaps are recorded as known limits in NOTES.md.
