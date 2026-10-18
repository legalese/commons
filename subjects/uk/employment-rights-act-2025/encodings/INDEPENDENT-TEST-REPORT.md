# Independent test report: ERA 2025 encoding

The expected values in `independent-expectations.md` come from BRIEF.md and the Act's text (ERA 2025 ss 1, 10, 11, 25; ERA 1996 ss 108, 207B). That file was written before any `.l4` file was opened. `era25-tests.l4` was not read.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 1 (the failed assertion; no other errors) | 62 | 1 |
| encoding total (5 modules) | 1 | 84 | 1 |

There are 63 assertions over 60 scenarios:
- SSP rate: 9
- SSP start: 3
- s 108 qualifying period: 19
- s 27BH without conciliation: 13
- s 207B: 15
- top-level goal: 4

## Failure

**L113, scenario 59: s 207B(3) days after the end of the limitation period are counted.**

- **Scenario.** A s 27BH(2) complaint with the offer made 15 Jan 2027, so the period runs 16 Jan to 15 Jul 2027. Day A is 1 Jun 2027 and Day B is 30 Jul 2027.
- **My value: 30 Aug 2027.** Only the days from 2 Jun to 15 Jul fall within the period: 44 days. 15 Jul + 44 = 28 Aug 2027. That falls within the s 207B(4) window (1 Jun to 30 Aug 2027), so the limit becomes 30 Aug 2027.
- **Encoding's value: 12 Sep 2027.** It counts every day from 2 Jun to 30 Jul (59 days), so 15 Jul + 59 = 12 Sep. That is outside the (4) window, so (4) does not apply.
- **The words.** s 207B(3): "the period beginning with the day after Day A and ending with Day B is not to be counted". The brief: "the conciliation days from the day after Day A to Day B are not counted, so far as they fall within the period."
- **My view.** This is a real departure from the brief's reading. In `era25-rules.l4`, `the limit … of a period from … extended by …`, the count `stopped` is clipped at the period's start (`the later of (Day A + 1) start`) but not at its end (`limit`). The rule's own comment says "so far as within the period". The fix is to count up to `the earlier of (Day B) limit`.
- **Impact.** It only shows when Day A is more than about a month before the original limit and Day B is after it. Then the over-count pushes the date past one month after Day B, where (4) would otherwise have applied. In every other case (4) absorbs the over-count; scenario 49 shows this.
- **Caveat.** Scenario 59 was added after reading the encoding's shapes. The expected value follows readings R4 and R5, which were fixed before then.

## Remarks

1. **SSP first payable day.** It is the first day of incapacity whenever there is at least one day. Qualifying days (s 154) are not an input, so "the first qualifying day" in the brief comes down to the first day of incapacity. That matches the brief's inputs, but it is a simplification worth a note in NOTES.md.
2. **NWE of 0.** This gives a weekly rate of £0, not a REFUSE. That is arithmetically what s 157(1)(b) says (ambiguity A1). I accept it.
3. **Month arithmetic.** Every month-end and leap-year case passed. This covers s 108 six-month and one-month periods, s 27BH start and last days, (8) starting on the day of awareness, and February 2027 and 2028. So does the s 207B(4) "one month after Day B" with clamping (31 Jan to 28 Feb; 31 Mar to 30 Apr).
4. **s 207B(4) window.** Both ends are inclusive, and the scenarios at Day A and at one month after Day B passed (50, 53). Conciliation wholly before the period (48) or wholly after it (51) leaves the limit unchanged.
5. **Overlapping the start.** Conciliation that overlaps the start of the period is clipped correctly (47: 25 Jul, not 30 Jul).
6. **s 108(3)-(5).** These are one boolean input. It overrides s 64(2) and the six-month test, as the Act requires.

## Change after the pass (encoder)

- **Line 113 (scenario 59) is left failing on purpose.** The encoder reads s 207B(3) differently from the tester. The Act says that "in working out when a time limit ... expires the period beginning with the day after Day A and ending with Day B is not to be counted". Read as a clock, the time limit stops running from Day A + 1 and restarts after Day B, so the days still to run when conciliation began are added after Day B. That is limit + (Day B − Day A) when Day A is within the period. The tester's reading would stop only the days up to the original limit. This is recorded as F5 and as an open question. The assertion is unchanged, and `encoding.json` records 1 expected failure.
- **Remarks:** the first SSP day ignores qualifying days (F2), and s 108(3)-(5) is one input. Both are recorded in NOTES.md.
