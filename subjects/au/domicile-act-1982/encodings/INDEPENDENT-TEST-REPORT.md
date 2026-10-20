# Independent test report: Domicile Act 1982 (Cth)

Expectations (`independent-expectations.md`) were fixed from BRIEF.md and the source text before reading `dom-rules.l4`. `dom-tests.l4` and NOTES.md were not read.

## Result

`L4=~/.local/bin/l4 ./check.sh .` on `tests-independent.l4`: **29 assertions, 27 satisfied, 2 failed**. There are no other errors.

Scenarios covered: commencement edge (30 June / 1 July 1982); the 18th-birthday edge (day before / on the day); married and previously married minors; mental incapacity; every s 9(1) limb (one parent + separated, together + other parent alive, together + other parent dead, home with both, home with neither, followed parent dead); adoption by 2 and by 1 parent; rescission; s 9(4) retention (both sides); domicile of choice (residence + intention, each one missing, a child); s 6 before and after commencement; s 7; the top-level goal.

## Disagreements

### 1. Sole adoptive parent reported under s 9(1), not s 9(2)(b) (scenario 15)
Child adopted by 1 parent only, principal home with that parent, no other living parent. Expected `the domicile my sole adoptive parent has from time to time` (s 9(2)(b)). The code returns `the domicile the parent I live with has from time to time` because it tests s 9(1) before s 9(2). With a single adoptive parent and no other living parent, s 9(1)(b) is always met, so whenever the home is recorded as "with one of my parents" an adoptee by one parent never reaches s 9(2)(b). Both answers name the same domicile, so the practical result is the same, but the provision cited is wrong. s 9(2) is the specific rule for adopted children ("Where a child is adopted, his or her domicile ... is"). Confidence that s 9(2)(b) should be the label here: moderate. When the home is recorded as "with neither parent" (scenario 15b), the code gives the s 9(2)(b) answer.

### 2. s 9(4) when there was no s 9 domicile (scenario 18)
A 19-year-old who had no s 9(1)/(2) domicile on ceasing to be a child. I expected `JUST FALSE` (s 9(4) does not keep anything for them). The code returns `NOTHING`. The brief says cases left to the common law are NOTHING, and the person's domicile then follows the common law, so the code's reading is defensible. Confidence in my value: **low**. This is mostly a question of design: does "do I keep my domicile from childhood" mean "does s 9(4) operate" (FALSE) or "is my childhood domicile kept" (unanswered by the Act)?

## Observations (agreements worth noting)
- The commencement day (1 July 1982) is treated as "after" commencement (s 5(2)). I agree, with moderate confidence. Strictly, s 5 says "before" and "after", and the day itself falls in neither.
- Before commencement, s 6 and s 7 return NOTHING, not FALSE, which agrees with s 5(1).

## Coverage gaps
- A birthday on 29 February (the code treats the 28 February anniversary as the 18th birthday in a common year) was not tested. The source is silent on this, so I formed no independent expectation.
- Overlap of s 9(1) with adoption by 2 parents (separated adoptive parents) was not tested. The code applies s 9(1) first there too, which is arguably right because s 9(2)(a) defers to "born in wedlock", which brings in s 9(1).
- s 9(3)'s cessation is modelled only as current facts (the home and whether the parents are together). No test covers a transition over time.
- s 9(5): the content of a rescission order is not modelled (out of scope).
- Pre-1982 dates combined with child or adoption questions were tested only for capacity and s 6.

## Change after the pass (encoder)

- Both disagreements were accepted: s 9(2)(b) now comes before s 9(1), and s 9(4) without a s 9 domicile gives FALSE.
- The gaps are recorded as known limits in NOTES.md.
