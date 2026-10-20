# Independent test report: Statutory Declarations Act 1959

Expectations were written from BRIEF.md and the source text (`independent-expectations.md`) before any L4 was read; `sd-rules.l4` was then read for names and input shapes only.

## Result

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **25 assertions, 23 satisfied, 2 failed**, no other errors.

## Scenarios

- Validity (ss 7A, 8, 9, 9A(1)): 15 scenarios covering the base s 9 in-person case; approved form missing (both routes); the video-link true-copy route and its unavailability in person; no signature by the prescribed person; the s 9A route and each of its missing elements; neither route; each limb of s 7A (identification, reliability/proof, manner of signing); electronic signing under video-link observation.
- Use (s 6): Commonwealth law with and without contrary intention; Department administration (no proviso); evidence in court; another use; an invalidly made declaration (6).
- False statement (s 11): yes and no (2 scenarios, 4 assertions).

## Disagreements

### 1. Use as evidence in a judicial proceeding (U4, line 75)
- Code: `this Act authorises the use` is NOTHING (undetermined).
- My reading: JUST FALSE. s 6(3): "Subsection (2) does not authorise a statutory declaration to be used as evidence in a judicial proceeding but nothing in this section prevents a statutory declaration from being so used." The Act's answer to "does this Act authorise it?" is expressly no; it is the separate question "is it prevented?" whose answer is also no.
- Confidence: medium-high on the text. The encoding's NOTHING appears to be a deliberate signal of "neither authorised nor prevented"; this is a representation choice more than a wrong result, but a consumer of a MAYBE BOOLEAN named "authorises" would read NOTHING as "unknown", which the Act does not leave unknown.

### 2. Another use (U5, line 77)
- Code: NOTHING.
- My reading: JUST FALSE. s 6(2) lists the uses it authorises ((a)-(c)); a use outside those is not authorised by this Act (s 6(1) lets a person *make* a declaration about any matter, but says nothing about use).
- Confidence: medium. Same representation question as #1.

## Coverage gaps

- The signing manner is not cross-checked against the route: e.g. a declaration "completed and signed on an approved online platform" but signed "by hand on a physical form" is accepted. s 9A(1)(a)(ii) implies electronic signing on the platform; not tested.
- s 7A(2)(b)(i) and (ii) are one input; the two limbs cannot be tested separately.
- s 11 is treated as applying regardless of whether the declaration was validly made; whether a false statement in a defectively made declaration is "in a statutory declaration" is untested (I did not form a confident expectation).
- s 6(2)(b) ("in connection with any matter arising under" a law) is merged with (a) in one input value.
- s 10 (declarations under other laws) is out of scope.

## Change after the pass (encoder)

- Both disagreements were accepted: s 6 does not authorise use as evidence in court or for other purposes (FALSE).
- The gaps are recorded as known limits in NOTES.md.
