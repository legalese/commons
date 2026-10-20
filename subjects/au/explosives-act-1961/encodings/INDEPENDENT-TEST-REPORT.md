# Independent test report: Explosives Act 1961

Expectations: `independent-expectations.md` (12 scenarios, written from BRIEF.md and the source before any L4 was read).
Tests: `tests-independent.l4` (19 assertions against `the explosives position for`).

## Result

`L4=~/.local/bin/l4 ./check.sh .` : tests-independent.l4 — **19 satisfied, 0 failed**, no other errors.

## Disagreements
None on computed values.

## Observations (not failures)
- **Input label "days the offence continues after conviction"**: s 20(a) says "a fine not exceeding 2 penalty units for each day during which the offence continues"; the words "after conviction" are not in the Act. The arithmetic (10 + 2 x days) matches my reading, but the label narrows the days counted to post-conviction days, which the source does not say. Recommend relabelling to "days during which the offence continues". Confidence: medium.
- **Lesser prescribed penalty (s 20(b))**: the encoding returns 0 months and 0 units with `a lesser prescribed penalty applies instead` = TRUE. The flag is correct; the zeros could be misread as "no penalty". I did not assert the numbers (the Act does not quantify a prescribed penalty).
- s 20 applies to any contravention of the regulations whether or not Part II reaches the explosives (scenario 12: anyone else's explosives, e.g. Part III explosives-area regulations): the encoding agrees — the offence is not gated on s 9.

## Coverage gaps
- Scenario 9 (contravening an order rather than the regulations) is a single input with the regulations case, so it could not be distinguished; it is covered by scenario 5.
- s 9(b) without Commonwealth approval, or not for a defence purpose, cannot be expressed: the enum value bundles "here with approval for defence"; such explosives must be entered as `anyone else's`.
- s 8 (naval vessels excluded from "vessel" in Part II) and the s 5 definition of explosives are folded into the inputs.
- "or both" (imprisonment and fine together) is implicit in giving both maxima; not separately asserted.

## Change after the pass (encoder)

- No disagreements. The continuing-days input was relabelled (it was not limited to after conviction).
- The gaps are recorded as known limits in NOTES.md.
