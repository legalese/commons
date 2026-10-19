# Independent test report: dfrb73-rules.l4

Expectations were written in `independent-expectations.md` from BRIEF.md and the source only, before the rules were read. Tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **27 satisfied, 2 failed**, and no other errors. The 2 errors check.sh reports are those two failed assertions. The existing dfrb73-tests.l4 has 15 satisfied and 0 failed.

## Failures

| Line | Assertion | Expected | Code gives | Reasoning |
|---|---|---|---|---|
| L60 | retirement 1 Oct 1972 | 0 | 46.5 (9/21 of 108.5) | s 4(1) "pension" means a pension "in respect of the retirement or death of a contributor on or before 30th September, 1972". A retirement on 1 October 1972 is not a "pension" under this Act, so s 5 gives no increase. The module has no s 4(1) cut-off. |
| L61 | retirement 20 June 1973 | 0 | about 5.17 (1/21 of 108.5, via s 7(4)) | Same point. Under the s 7(1)(a) limb, s 7(4) ("less than one month ... one month") can never apply to a "pension", because the period is always at least 9 months. Only the out-of-scope s 82ZB limb can reach it. |

Both failures are a disagreement with the Act, not with the brief. The brief does not list s 4(1) in scope. A one-line guard would fix it: no increase where `retirement or death on` is after 30 September 1972. Whether to add it is the encoder's decision.

## What agreed

- s 4(2): the lower of the two limbs, including a tie.
- s 4(4) rounding: 4.64 gives 4.6, and 4.65 (exactly half a tenth) gives 4.7. This holds on both the CPI limb and the earnings limb.
- s 5(1): both "exceeds" gates and the child's-pension exclusion.
- s 5(2): the 77.5 % factor.
- s 7: the 30 September / 1 October 1971 edge.
- s 7 month counts: 21 months (1 Oct 1971), 12 months (30 Jun 1972), 9 months (30 Sep 1972), and the part-month edges. The part month counts at exactly half (15 Mar 1972 gives 16 months) and is dropped below half (16 Mar 1972 gives 15 months).

## Gaps

- **s 4(5) widow.** The record has no widow or death-after-retirement field, so the caller must enter the right date (the retirement date, per s 4(5)). Scenarios 16 and 17 therefore only test the dates, not the deeming.
- **s 12.** The 5 July 1973 effective instalment appears only in the export description. No function returns or tests it.
- **Month counting.** The method used (anniversary months, then a tail measured against the next anniversary month) agrees with calendar counting on every scenario chosen. The Act does not fix the method, and I did not hunt for dates where the two methods diverge.
- **s 4(3)** (disregarding later revisions of the indices) is outside what the inputs can express.

## Change after the pass (encoder)

- **L60-L61 (retirement after 30 September 1972).** Accepted: such a pension is outside s 4(1), and the increase is 0 (F4).
- The gaps are recorded as known limits in NOTES.md.
