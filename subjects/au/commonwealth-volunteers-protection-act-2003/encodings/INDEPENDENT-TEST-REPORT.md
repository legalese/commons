# Independent test report: Commonwealth Volunteers Protection Act 2003 (Cth)

Expectations were written first (`independent-expectations.md`, from BRIEF.md and the Act only). Then `tests-independent.l4` was written against the names in `cvp-types.l4` and `cvp-rules.l4`. `cvp-tests.l4` was not read.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| cvp-rules.l4 | 0 | 0 | 0 |
| cvp-tests.l4 | 0 | 30 | 0 |
| cvp-types.l4 | 0 | 0 | 0 |
| tests-independent.l4 | 0 | 35 | 0 |
| **TOTAL** | 0 | 65 | 0 |

The 35 independent assertions cover 33 scenarios: s 4(2) (1-4), s 4(3) (5-9), s 5 (10-11), s 6(1) (12-17), s 6(2)-(4) (18-23), s 7(1)-(2) (24-28), s 8 (29-31), s 9 (32-33). **No assertion fails.** My reading and the code's agree on every scenario I could express.

## Gaps: things the encoding's inputs cannot express

None of these is a failing assertion. Each is a scenario I wrote but could not test as I wrote it, or a reading point.

1. **Scenario 6 matches scenario 5.** `How I was paid` has one constructor, `my usual pay from my employer only`, covering s 4(3)(a)(i) and (a)(ii). `the work is usually done unpaid` is one boolean covering s 4(3)(b)(i) and (b)(ii). The limbs give the same result, so this is acceptable, but the sub-paragraphs can't be tested separately. Also, a person whose employer keeps paying them *and* who receives other pay at or above the prescribed amount can only be entered as `more than that`. That gives the right answer (not voluntary).
2. **s 4(1) "organised includes directed and supervised"** is folded into one boolean, `organised by them`. Scenario 15 (only directed) can only be entered as `organised = TRUE`. Correct, but the definition is left to the user.
3. **s 6(4) "knew or ought to have known"** is folded into `knowingly outside ...` / `knowingly contrary ...`. Scenario 22 (outside scope but did not know and could not have known) can only be entered as FALSE. Correct, but the encoding can't tell "acting outside scope" apart from the knowledge element.
4. **s 9 has no "indemnity given" input.** The brief lists "whether the volunteer gave an indemnity" as an input, but `Volunteer case` has no such field. `my indemnity has effect` therefore answers TRUE even when no indemnity was given. Also, where s 9 does not apply (scenario 33, defamation), the code says the indemnity "has effect" (TRUE). The Act only says when an indemnity has *no* effect. Outside s 9 its effect is a matter of general contract law. Under the brief's rule ("where the source does not answer, give NOTHING"), the answer there should arguably be NOTHING rather than TRUE. My assertion of TRUE for scenario 33 tests only that s 9 does not void the indemnity.
5. **The prescribed amount is an input category, not a number.** The regulations are not in the bundle. "Less than the amount, if any, prescribed" is entered as a category, so the case where no amount is prescribed (limb (ii) can never be met) is left to the user.
6. **s 7 outcome labels.** Where s 6 does not protect, the code says `I do`. The Act does not impose liability. It just does not remove it, and the rule's @export text says so. Where s 7(2) applies, the code says "no one under this Act". That matches my reading (point 1 in the expectations): the volunteer stays protected by s 6, and the authority is not made liable by s 7.
7. **s 8 "may incur".** The code ties the duty to assist to the case where the code's answer is that the Commonwealth or authority bears the liability. That matches my reading. But the facts are entered as settled, so a claim where it is still disputed whether s 6 applies ("may incur") can't be modelled.

## Disagreements with the brief

None that produce a different answer. The brief's input list includes an indemnity flag that the types do not carry (gap 4).

## Change after the pass (encoder)

- No disagreements to resolve.
- The brief's mention of an indemnity input was corrected: the answer says only whether s 9 would void an indemnity.
- The gaps listed above are recorded as known limits in NOTES.md.
