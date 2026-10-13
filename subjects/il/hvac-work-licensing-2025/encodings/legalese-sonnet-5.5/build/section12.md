## 12. Verification of the date correction, and one decision (added by the launching session, 2026-10-13)

Everything in section 11 was written by the encoder; this section was added afterwards.
It is spliced in verbatim by `build/make_notes.py` from `build/section12.md`, like section 10.

**Re-run, with the binary named in section 10.**
`check.sh` printed the table the encoder reported: 15 modules, 347 assertions satisfied (15 in `hvac-tests-calendars.l4`, 76 in `hvac-tests-fees.l4`, 234 in `hvac-tests-law.l4`, 22 in `hvac-tests-simplex.l4`), 0 refused, and 13 failed, all in `hvac-tests-red.l4` and all expected.
The `#ASSERT` directive counts in those five files are 15, 76, 234, 22 and 13, and no module emits a warning.
`il-interpretation-time.l4` here is byte-identical to the Interpretation Law subject's copy.
The 22 `#TRACE` directives (2 in the fees tests, 20 in the law tests) are not counted by `check.sh`; the encoder says it read them all, and the launching session did not re-read them.

**What moved.**
Every as-run assertion that was removed or edited was paired with its closest replacement and compared for polarity and expected value.
Exactly two changed, both on fork F-N1: `the day the 5786 amendment commenced` went from a refusal to 2026-05-04, and `the vintage in force on` 2026-05-04 went from a refusal to `As amended`.
Fifty-nine assertions were added, and no other expectation changed, so the readings the first encoding took (the sunset on 2028-07-16, s.8's anniversary, s.16 at day 30, reg. 5 at 2025-07-16) already agreed with s.10.

**Decision on F-N1: kept.**
The encoder offered to revert F-N1 to a refusal to keep this pass to s.10.
It is kept, because the reason for the refusal has gone: the Interpretation Ordinance's s.17 now has an official text in this repository (`subjects/il/interpretation-law-1981/source/official/2_lsr_vn_525666.pdf`), and the launching session compared its s.17 with the Wikisource text this row quotes; the Hebrew wording is the same (in translation: regulations of legislative effect shall be published in Reshumot, and their commencement is the day of their publication, unless there is another provision in the matter).
So the sentence in F-N1 and in section 11 that the Ordinance rests on an unofficial text alone is out of date for s.17; every other section of the Ordinance is still read from Wikisource alone.
The rows `legalese` and `legalese-opus-5.5` took the same day, 4 May 2026, under the same section.
Still open for a domain expert: whether any other provision fixes when regulations under the Law commence (Q5), and whether the Fees Regulations are regulations of legislative effect in the sense of s.17, which the launching session believes but no one qualified has said.

**Readings that differ between sibling rows.**
This row does not apply s.10(c) to periods of validity (its F-X2), as `legalese` does not (its F7); `legalese-opus-5.5` does apply it to validity (its F31).
All three are open readings.
