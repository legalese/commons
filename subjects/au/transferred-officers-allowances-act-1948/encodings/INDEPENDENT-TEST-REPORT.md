# Independent test report: toa-rules.l4

Expectations were written in `independent-expectations.md` from BRIEF.md and the source only, before the rules were read. Tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **76 satisfied, 0 failed**, and 0 errors. The existing toa-tests.l4 has 18 satisfied and 0 failed.

The 76 assertions cover 17 pension levels and 8 date or widow cases. For each pension level there are four checks: the s 4, s 5 and s 6 allowances separately, plus the total.

## Failures

None.

## Edges covered

- **s 4:** P = 288 (quarter), 300 (top-up to 360), 360 (nil).
- **s 5:** S = 260 exactly (one-fifth) and 262.5 (£52); P = 650 (£52), 651 (£51), 702 (nil, since s 5(1) is reached but (5) needs less than 702), 800 (nil).
- **s 6:** T = 150 and 156 (£52); 180 (£56); 312 (£78 by the one-sixth formula); 314.5, 412 and 448 (£78); 449 (£77); 472 (£54); 500 (£52); 652 and above (£52, with no pension ceiling).
- **s 6 dates:** 11 Nov 1955 (none), 12 Nov 1955 (applies), 31 Dec 1956 (applies), 1 Jan 1957 (none).
- **Dates generally:** 30 Oct 1953 gives NOTHING; 31 Oct 1953 gives ss 4 and 5.
- **s 7 widow:** half of each allowance.

## Gaps

- **s 7.** The widow's own pension is not an input. The husband's notional pension stands in, as the brief directs.
- **Rates before 31 Oct 1953.** The 1948 and 1951 rates are not in the text, so those dates answer NOTHING. This is by design.
- **s 6(3) end date.** I read "until 31 December 1956 ... and no longer" as including 31 December, and so does the code.

## Change after the pass (encoder)

- No disagreements.
- The widow's pension gap is recorded in NOTES.md (F3).
