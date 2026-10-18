# Independent test report: Pensions Act 2014 (UK)

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act text (ss 1-5, 17, 30-31, Sch 1) before any `.l4` file was opened. `pa14-tests.l4` was not read.

## Counts

| | |
|---|---|
| Scenarios in `independent-expectations.md` | 79 (13 entitlement, 7 full/reduced, 15 transitional, 11 whole weeks, 8 increase, 25 bereavement; a few bereavement rows share one assertion) |
| Assertions in `tests-independent.l4` | 90 |
| Satisfied | 90 |
| Failed | 0 |
| Non-assertion errors | 0 |

`L4=~/.local/bin/l4 ./check.sh`: all 7 modules 0 errors, 128 satisfied (38 encoder, 90 independent), 0 failed.

The assertions do catch wrong answers: a copy with two values deliberately changed (152.5 → 152; B1 negated) failed on exactly those lines.

## Failures

None. Every value fixed from the Act matched the encoding, including:

- s 1(2) edge: pensionable age 5 April 2016 → none under Part 1; 6 April 2016 → transitional.
- s 4(3): 1 pre-commencement year + 40 post → transitional, not full.
- Sch 1 Step 2 with contracting-out deduction (incl. a negative Step 2, where Step 3 takes Step 1); Step 4 revaluation at, below and above the 2016 full rate (excess × 1.10); s 5(1) cap at the full rate and the (b) floor (197 > 175).
- s 17(3) whole weeks counting both days (7 days → 1, 6 → 0, 365/366 → 52, 29 Feb); the 1% floor at exactly 1% (5 weeks × 0.2%, 9 weeks × 1/9 %) gives the increase, just under gives 0.
- s 30(1)(b) death on the claimant's pensionable-age day → not entitled; s 31(1)(b) earnings factor exactly 25 × LEL → met; LEL per tax year; credited-but-not-paid contributions → not met; s 31(3) industrial death → met.

## Remarks

1. **s 30(6) is a boolean input, not a date.** The encoding cannot apply the commencement date (6 April 2017, from the commencement order; the Act does not print it). Scenarios B22/B23 could only test that the flag is respected. Acceptable under the brief, but `NOTES.md` should name the date so users set the flag correctly.
2. **No entitlement gives a weekly rate of 0.** Where s 1(2) or the minimum-years test excludes the person, `the weekly state pension for` returns 0. The Act does say "not entitled", so this is not a gap in the source, but 0 cannot be told apart from a real rate. The kind (`none ...`) shows it; a `MAYBE NUMBER` would be cleaner. I did not assert a rate for these cases.
3. **The reduced rate uses post-commencement years only.** That is right only because the reduced rate is reachable only with 0 pre-commencement years (any pre-commencement year sends the person to s 4). Correct as written, but it depends on that branch order; summing all years would match s 3(2)'s "number of qualifying years" more literally.
4. **One minimum for ss 2(3) and 4(2).** The Act lets regulations set the two separately; the brief gives one input. Fine for today's regulations (10 for both).
5. **"Has reached pensionable age" (ss 2(1)(a), 4(1)(a)) is assumed.** The kind is computed as at pensionable age; no input says whether the person has reached it yet. Consistent with the brief.
6. **A deferral whose last day is before its first gives 0 weeks** rather than `REFUSE`. Minor; the brief prefers `REFUSE` where the source does not answer.
7. s 30(1A)-(1D) (several claimants for one death) are out of scope and stated as such in the `@export` text.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md:
- s 30(6) is an input;
- no entitlement gives a weekly rate of 0, shown by the kind;
- the reduced rate depends on the branch order;
- one minimum serves ss 2(3) and 4(2);
- a deferral ending before it starts gives 0 weeks.
