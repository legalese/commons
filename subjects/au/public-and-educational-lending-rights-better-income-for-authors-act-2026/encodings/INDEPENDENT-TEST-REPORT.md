# Independent test report: Public and Educational Lending Rights (Better Income for Authors) Act 2026

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. `tests-independent.l4` asserts them against `plr-rules.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`: tests-independent.l4: **27 satisfied, 2 failed** (the 2 errors are the 2 failed assertions; no syntax errors).

## Scenarios covered

s 5 Australian person/creator: citizen, PR, neither, non-individual; each contribution kind and none. s 5 Australian publisher (a)-(d), (c) with and without an Australian creator, not a publisher. s 33(2)(a) last request day (incl. a leap-year February), s 33(2)(b) longer period; s 33(5) last reconsideration day, including from a request received on the last day; s 33(8) notified on the last day / the day after / never; s 34(1)(a) Secretary personally, (b) actual and deemed reconsideration, no request yet; s 38(2)(c) earliest end of the payment period (incl. leap February). All date arithmetic agreed with my reading (a period "of N days beginning on" day D ends on D+N-1).

## Disagreements

**1. A late request still triggers deemed affirmance and Tribunal review.** Delegate decision notified 1 Jul 2027 (last day to request 28 Jul 2027); request received 29 Jul 2027; Secretary never responds.

| | Mine | Code |
|---|---|---|
| deemed affirmed (s 33(8)) | FALSE | TRUE |
| may apply to the ART (s 34(1)) | FALSE | TRUE |

Source: s 33(4) — "The Secretary, on receiving a person's request **made in accordance with subsections (2) and (3)**: (a) must reconsider ..."; s 33(5) runs the 90 days from receipt of "the request" in that context; s 33(8) deems affirmance by reference to "the period applicable under subsection (5)". A request outside the s 33(2) period (with no longer period allowed) is not a request made in accordance with s 33(2), so no duty to reconsider arises, no s 33(5) period runs, nothing is deemed under s 33(8), and s 34(1)(b) has no decision to attach to. The code computes the s 33(5) day from any received date without checking it against the s 33(2) deadline. Confidence: medium-high. (The Secretary could still allow a longer period after the fact under s 33(2)(b); the user would then enter that, and the request would be in time.)

## Coverage gaps

1. s 33(3) (reasons must be set out in the request) is not an input; a request without reasons is likewise not "in accordance with" s 33 and should not trigger (4)/(8). Same root as disagreement 1.
2. s 33(2) "in writing" is not an input.
3. The longer period under s 33(2)(b) is entered as an end date and taken as is; a "longer" period that actually ends before notified+27 would shorten the time. Not tested (would be a user input error).
4. s 34(1)(b) is granted whenever any reconsideration notification date is present, regardless of whether it preceded a valid request; minor.
5. s 5 publisher limbs (b) and (d) depend on rules not yet made; they are boolean-like enum values, so untestable beyond the label.
6. Commencement (s 2) is out of scope; dates before commencement are not checked.

## Change after the pass (encoder)

- One disagreement is left open: the tester reads a request received after the 28 days as late; the encoding has only the receipt day (`tests-independent.l4` lines 75, 78 are expected to fail).
- The gaps are recorded as known limits in NOTES.md.
