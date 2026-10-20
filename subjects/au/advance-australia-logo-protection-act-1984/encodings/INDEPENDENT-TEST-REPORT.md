# Independent test report: Advance Australia Logo Protection Act 1984 (Cth)

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the source text before `aal-rules.l4` was opened. `aal-tests.l4` and NOTES.md were not read. `tests-independent.l4` asserts them against `the logo position for`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 21 | 0 |

**21 satisfied, 0 failed.** No disagreements with the encoding.

## Scenarios covered

- s 3(1) prescribed period: ends 12 October 1999; both edges of the start (12 and 13 October 1983) and the end (12 and 13 October 1999), tested through s 11(1)(a).
- s 11(1): (a) applying, with and without licence; neither design nor imitation involved; (b) selling an infringing article, with and without licence; (c) importing and (d) selling an imported article, each with and without licence. My independent literal reading was that (c) and (d) infringe even with the owner's licence, because those paragraphs lack the words "without the licence of the owner of the design". The encoding reads them the same way, so this matched. The result is commercially odd, which is why I put my confidence at medium. A reviewer should confirm it.
- s 19(2)-(3): no copyright infringement during the period (1 July 1990) and after it (1 July 2005); before the period s 19 gives no answer (NOTHING).
- s 15(2): use on 12 October 1983 under a purported licence (no action lies); the same day without one (s 15(2) does not apply); 13 October 1983 under a purported licence (does not apply).

## Coverage gaps and reading notes

- s 19(2) covers acts the design owner "has the exclusive right to do". The s 3(1) monopoly is defined only as the right to *apply* the design. Whether selling or importing is also within the owner's exclusive right (through s 11) is a reading question. The encoding gives JUST FALSE for every dealing from 13 October 1983, which takes the broad reading. Only applying was asserted.
- For fraudulent or obvious imitations, s 19(2) shelters only acts within the owner's exclusive right, and that right is in "the design". s 19(3) extends the shelter after the period to designs differing in immaterial details, but not to every imitation. The encoding shelters every dealing, imitations included. Not asserted, because the input cannot tell the design from an imitation. This is a possible over-breadth to review.
- Scenario 7 (an imitation) cannot be told apart from the design itself: both are the one input `the design or a fraudulent or obvious imitation is involved`.
- s 11(1)(b) requires the article to have been applied "in infringement of the monopoly". The encoding takes this from the dealing's label and does not check it.
- s 14 validation of pre-1983 licences and the s 15(1) immunity of the Commonwealth and the Company are out of scope.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
