# Independent reader: triage of the section 121 row

An independent reader, who had only the text of section 121 and then the layer-1 and seat modules (no tests, notes or plans), wrote 130 scenarios before it opened any module, plus six repair scenarios and four seat scenarios afterwards, and asserted them in `s121-tests-independent.l4`: 130 assertions, 14 of them the reader's first seat assertions and 4 its seat assertions for the inputs added after the first run.
On the first run 117 of 123 assertions were satisfied and 6 failed.
The file now passes (130 satisfied, 0 failed, 0 refused).
**The reader's triage below the line is the reader's first-run triage, unchanged; this note records what happened to each line afterwards.**

**One was a real finding, repaired by the encoder (scenario 92).**
Under (d)(9)(A) the electing individual's 5-year period is suspended during any period that "such individual or such individual's spouse is serving" on qualified official extended duty; the first version did not count a spouse's service in the electing taxpayer's own window, although it did for (b)(5)(C)(ii)(II).
The encoder fixed it (fork F30, reading (i), the stated spouse's service on any return; the stakes are in the fork line in `NOTES.md`), and the reader's expectation of 100,000 now passes unchanged.

**Five were the reader's own mistakes (scenarios 6, 56, 95, 96 and 97).**
The reader let ownership begin before use, which is nonqualified use under (b)(5)(C)(i), and in one case left out a former spouse's use.
Those five assertions are commented out in the file, each marked `WITHDRAWN` and replaced by the reader's repair scenario (R6, R56, R95, R96, R97), which passes; the triage lists them as the reader first wrote them.

**Eight amounts differ by reading, not by formula (scenarios 38, 39, 43, 44, 48, 49, 52 and 54).**
In each the reader's amount counts whole years or months and the encoding counts calendar days.
The reader's amount against the encoding's: S38 160,000 against 160,032.85; S39 120,000 against 120,023.46; S43 150,000 against 150,092.37; S44 120,000 against 120,024.64; S48 120,000 against 120,024.64; S49 and S52 125,000 against 125,342.47; S54 125,000 against 124,657.53.
S38, S39, S44 and S48 are the (b)(5) ratio in calendar days with spans inclusive of both ends and no rounding (forks F5 and F9); S43 counts the 2-year absence cap as the days in the 2 calendar years ending on the sale (F10); S49 and S52 count "1 year of use" as 366 days (both ends of 30 June to 30 June) over the 730 days of the 2 calendar years ending on the sale (F4, F5, F6); S54 counts the period between the two sales as the days strictly between them (F25).
The lead confirmed each by a one-off probe that shifts the dates by a day or two so that the day counts equal the reader's: the same encoding then returns the reader's amount exactly, and the eight probe assertions (P-S38, P-S39, P-S43, P-S44, P-S48, P-S49, P-S52, P-S54) are at the end of the file.
They keep the reader's own expected amounts, but the shifted dates are the lead's, not the reader's.
Each of the eight lines in the file carries a `DIFFERS BY READING` comment with both amounts.
The eight lines keep a `near` assertion (within a stated tolerance of the reader's amount) so that the reader's expectation is still on record; they are not a failure.

**Gaps.**
Four seat gaps of the first run were closed after the reader returned: a surviving spouse asking the amount left out (S127, S128), the amount after an election under (f) (S129), and a stay in a care facility (S130).
The encoder added those facts to the amount questions, and the reader's four new seat assertions for them (N1 to N4) pass.
Twelve scenarios still cannot be asked and are not repaired: age (the text has none), what an earlier sale "to which (a) applied" is (an input), a named "unforeseen circumstance" (the text defers to regulations), and silent cases with nothing to ask (tax rates, State tax, net investment income tax, how the gain is computed, the deadline for the election in (f), a duty to report, and land sold separately).
These are known limits of this row.

**Edits to the reader's file by the lead, all marked in comments:** the five `WITHDRAWN` lines, the eight `DIFFERS BY READING` notes and the eight probe assertions with the header comment about them.
The reader's four amount questions were updated to the new seat inputs by the reader itself.

---

The reader's own triage follows, unchanged.

# Triage: 26 U.S.C. section 121, independent tests

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset; diagnostics read, not the exit code.
Record of the run: `run3.out` (123 assertions: 117 `assertion satisfied`, 6 `assertion failed`, 0 `assertion refused`).
Line numbers are lines of `enc/tests-independent.l4`.
Format: scenario | file line | provision | expected | encoding answered | verdict | note.

## Failed assertions

- S6 | line 335 | (a) with (b)(5)(C)(i) | JUST 100000 | JUST 36472.35 | SCENARIO | I let ownership begin 2018-01-01 but use began 2018-12-01 and stopped for 2.5 years in the middle; those unused stretches are after 2008, so they are nonqualified use and the encoding correctly allocates about 64 percent of the gain to them. The two-year test itself is met: R6 (the (a) test alone) is satisfied.
- S56 | line 402 | (d)(3)(A) with (b)(5)(C)(i) | JUST 100000 | JUST 54197.08 | SCENARIO | I did not state the husband's (former spouse's) use of the home, a fact the encoding asks for (`periods a spouse or former spouse used the property as the principal residence`); without it his 2.75 years of ownership before she moved in count as nonqualified use. With the fact stated, R56 gives 100000.
- S92 | line 456 | (d)(9)(A), joint return | JUST 100000 | JUST 0 | ENCODER | The text suspends the electing individual's 5-year period during any period that "such individual or such individual's spouse is serving"; the electing taxpayer's own record lists no service and the spouse's record does, and the taxpayer's window ignores the spouse's record, although the same assembly merges both spouses' service for (b)(5)(C)(ii)(II) (`dutyDays` in s121-whole.l4). Minor, because the caller can state the spouse's service in the taxpayer's own list (R92b gives 100000), and the seat question cannot say whose service it is at all.
- S95 | line 462 | (d)(10) day after the 5-year period | JUST 100000 | JUST 40043.76 | SCENARIO | Same mistake as S6: I let ownership begin at the 2020-01-01 acquisition but use only in the last 2 years, so 3 of 5 years are nonqualified use. The (d)(10) bar did not fire, which is what I expected for 2025-01-01. R95 (lived in it throughout) gives 100000.
- S96 | line 463 | (d)(10) 5 years 6 months after | JUST 100000 | JUST 36454.18 | SCENARIO | Same mistake as S95. R96 gives 100000.
- S97 | line 464 | (d)(10) ordinary purchase, no 1031 exchange | JUST 100000 | JUST 44552.65 | SCENARIO | Same mistake as S95. R97 gives 100000.

## Gaps: scenarios that cannot be asked of the encoding

- S11 | none | (a) age | JUST 100000 for a 72-year-old | no input for age | GAP | The encoding takes no age; that is consistent with the text (no age condition), so nothing could disagree.
- S28 | none | (b)(3) earlier sale where the taxpayer elected under (f) | no bar, JUST 100000 | no function | GAP | The encoding takes "dates of other sales to which (a) applied" as an already-decided input; whether an earlier sale was one to which (a) applied (election out, failed test) is the caller's call.
- S29 | none | (b)(3) earlier sale where (a) failed or there was a loss | no bar, JUST 100000 | no function | GAP | Same input as S28.
- S53 | none | (c)(2)(B) a divorce as an "unforeseen circumstance" | NOTHING | no function | GAP | The encoding asks the caller a yes/no for "unforeseen circumstances, to the extent provided in regulations"; it cannot say NOTHING for a named circumstance.
- S107 | none | (a) tax rate on gain above the ceiling | NOTHING | no function | GAP | Silent case; nothing to ask.
- S109 | none | (a) whether a vacation cabin is a "principal residence" | NOTHING | no function | GAP | "Principal residence" is a fact the caller states, not a function.
- S110 | none | (a) State income tax treatment | NOTHING | no function | GAP | Silent case; nothing to ask.
- S111 | none | (a) how gain is computed (amount realized less adjusted basis) | NOTHING | no function | GAP | The gain is an input.
- S112 | none | (a) net investment income tax | NOTHING | no function | GAP | Silent case; nothing to ask.
- S113 | none | (f) deadline for the election not to apply the section | NOTHING | no function | GAP | Silent case; nothing to ask.
- S114 | none | (a) a duty to report the sale on a return | NOTHING | no function | GAP | Silent case; nothing to ask.
- S115 | none | (a) land sold separately from the house | NOTHING | no function | GAP | Silent case; nothing to ask.
- S127 amount | none | seat: widow's amount excluded (the limit question S127 is satisfied) | 400000 left out, 0 taxed | seat has no question for the amount of a surviving spouse | GAP | `Filing alone, how much of my gain is left out` builds the taxpayer as not widowed; only `Is my limit 500,000 as a surviving spouse` is askable.
- S128 amount | none | seat: widow's amount excluded when the sale is after 2 years (S128 limit question satisfied) | 250000 left out, 150000 taxed | same | GAP | Same.
- S129 amount | none | seat: amount excluded after electing out under (f) (S129 reach question satisfied) | 0 left out, 100000 taxed | same | GAP | The amount questions take no (f) election; only `Does section 121 reach my sale at all` does.
- S130 | none | seat: incapable of self-care, 1 year of use then a licensed nursing home | 100000 left out, 0 taxed | seat asks only for the days the stay counts | GAP | The layer-1 equivalent S73 and S77 are satisfied.

## Notes (not findings)

- Assertions that pass only within a stated tolerance, because the encoding counts days: S38 160032.85, S39 120023.46, S43 150092.37, S44 120024.64, S48 120024.64, S49 125342.47, S52 125342.47, S54 124657.53 (my values 160000, 120000, 150000, 120000, 120000, 125000, 125000, 125000). Each difference is a day-count artefact of at most 0.3 percent.
- The two day-count edges (a) 2 years exactly (S3), (b)(3) first day and day before the 2-year period (S26, S27), (d)(10) last day (S94) and day after (R95) all agree with my inclusive reading.
- The six repairs (R6, R56, R92b, R95, R96, R97) are new scenarios with expected values written in the addendum of ANSWERS.md before they were run; the six originals stay failing.
- While writing the tests I mistyped the argument order of my own date helper in eight assertions (S41 to S48); that made them fail for a reason that was mine alone, I corrected the dates in my test file and left every expected value as written, and they now agree with the encoding.
- Where the encoding signals "not covered" (`NOTHING`) both of my silent scenarios that can be asked agree: S68 (a gift is not a listed event) and S108 (a loss).
