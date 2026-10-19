# Independent test report: Common Informers (Parliamentary Disqualifications) Act 1975 (Cth)

Expectations were written in `independent-expectations.md` from BRIEF.md and the source only, before `cipd-rules.l4` was read. Tests: `tests-independent.l4`.

## Counts (`L4=~/.local/bin/l4 ./check.sh`)

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 1 (the failed assertion) | 17 | 1 |

There are no syntax or type errors.

## Failure

**The same day listed twice, line 51.** Sittings `[23 Jun 2026, 23 Jun 2026]`, served 22 Jun. I expected $200; the code gives $400. Section 3(1)(b) says "$200 for every **day** ... on which he or she is proved ... to have so sat". The code counts list entries, not distinct days (`sum (map (GIVEN d YIELD 1) after)`). A senator who sits twice on one day (for example, two sittings of the chamber, or a duplicated entry) would be charged twice for one day. That also offends s 3(3) ("penalized more than once in respect of any ... day of sitting"). Suggested fix: deduplicate the counted days before counting, for example with `nub`. Otherwise the input needs to be documented as distinct days.

## Agreements

- Not incapable gives $0. With no sittings, $0.
- (a) is a single $200 for any number of sittings on or before service. The service day itself falls under (a), not (b). Sittings after service are $200 each. The order of the list does not matter.
- The 12-month edge: a sitting exactly 12 months before institution (15 Jun 2025 for 15 Jun 2026) counts, and the day before does not. Where institution is on 29 Feb 2028, a sitting on 28 Feb 2027 counts and one on 27 Feb 2027 does not. `add months` with -12 clamps to the month end, as the brief requires.
- Days already penalised are excluded from both (a) and (b). Where the only pre-service sitting was already penalised, (a) is not due. This matches my reading of s 3(3) (scenario 13), which the brief left ambiguous.
- s 4: no suit under s 46 (always FALSE).

## Gaps and reading notes

- s 3(3) is a refusal to *make an order* "in the opinion of the Court". The encoding reduces the sum by the already-penalised days instead of refusing the order. That is a reasonable simplification, but it is not the Act's mechanism. The Court's opinion is also not modelled.
- A service date before the institution date, or sittings after the trial, are not validated. Nothing stops a "proved" sitting after the date of judgment.
- Commencement (s 2): the assent date is not in the source. Section 4 is hard-coded FALSE, which is right for any present-day suit.
- s 5 (High Court exclusive jurisdiction) is a note only, and is not tested.

## Change after the pass (encoder)

- **Line 51 (a day listed twice).** Accepted: each day counts once (F5).
- The reading notes are recorded as known limits in NOTES.md.
