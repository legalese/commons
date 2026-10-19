# Independent test report: Human Rights (Sexual Conduct) Act 1994 (Cth)

Expectations were written in `independent-expectations.md` from BRIEF.md and the source only, before `hrsc-rules.l4` was read. Tests: `tests-independent.l4`.

## Counts (`L4=~/.local/bin/l4 ./check.sh`)

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 2 (both are the failed assertions) | 23 | 2 |

No syntax or type errors. All adulthood edges agree: 18th birthday, the day before and after, 31 December, and the 29 February birthday (adult on 28 February of a common year, not on 27 February), for births in 2008 and 2000.

## Failures

1. **No one involved (empty list of dates of birth), line 56.** I expected *not protected*. The code says *protected*, because `all` over an empty list is TRUE. The Act does not contemplate "sexual conduct" involving nobody. Calling it protected is vacuous truth, not something the Act says. Suggested fix: require at least one person, or return NOTHING. Low practical weight, but a caller could get "protected" from an empty form.

2. **Interference not under a law of the Commonwealth, a State or a Territory, line 67.** I expected `JUST FALSE`: s 4 does not bar it, because s 4 covers only interference "by or under any law of the Commonwealth, a State or a Territory". The code returns `NOTHING`. Both readings are defensible. The code's NOTHING says "s 4 does not speak", which matches the brief's "where the source does not answer, give NOTHING". Mine says "s 4 does not bar it", which is also something the source does answer. The two clash because the field is named "barred", and the Act clearly does not bar it. This needs a drafting decision. I did not change my expected value.

## Agreements worth noting

- A minor involved, or no consent, or not private: not protected, and arbitrary interference is not barred (`JUST FALSE`). This matches my reading that s 4 simply does not apply. Note that "not barred by s 4" should not be presented to the user as "the law may interfere".
- Interference that is not arbitrary: `JUST FALSE`.
- Solo conduct and three-person conduct: protected.

## Gaps

- **29 February rule.** The Act is silent. The brief and the code use 28 February, which the encoding does through `add months b 216`. Some Australian age-of-majority approaches give 1 March. This is a policy choice, and it should be flagged in NOTES.md as not reviewed.
- **Commencement (s 2).** The source does not give the Royal Assent date, so conduct before commencement is not handled. No test.
- **External Territories (s 3)** are folded into the single "Territory law" input. They can't be tested separately.
- Whether the law is a "law of the Commonwealth, a State or a Territory" and whether the interference is "arbitrary" are inputs, so the Article 17 meaning is untested by design.

## Change after the pass (encoder)

- **Line 56 (nobody involved).** Accepted: an empty list is not protected (F4).
- **Line 67 (another law).** Accepted: s 4 does not bar it, FALSE rather than NOTHING (F3). One of the encoder's tests was updated, with a comment.
- The other notes are recorded as known limits in NOTES.md.
