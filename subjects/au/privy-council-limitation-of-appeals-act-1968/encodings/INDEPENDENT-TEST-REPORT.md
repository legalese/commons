# Independent test report: Privy Council (Limitation of Appeals) Act 1968

Expectations written from BRIEF.md and the source only (`independent-expectations.md`), then encoded in `tests-independent.l4` against `pcla-rules.l4`.

## Counts (`L4=~/.local/bin/l4 ./check.sh`)

| module | errors | satisfied | failed |
|---|---|---|---|
| pcla-rules.l4 | 0 | 0 | 0 |
| pcla-tests.l4 | 0 | 7 | 0 |
| tests-independent.l4 | 1 | 11 | 1 |

The one error is the one failed assertion; no syntax or type errors.

## Failure

**Scenario 10 (line 29): a decision of "another court" (e.g. a State Supreme Court).**
Expected `this Act does not bar it`; the encoding gives `this Act does not apply`.

Reasoning: s 3 speaks only of the High Court and s 4 only of a Federal Court (other than the HC) or a Territory Supreme Court. For any other court the Act says nothing, so it does not bar asking. The brief says "Where it does not bar asking, the answer is that this Act does not bar it", which I read as covering this case. The encoding adds a third value, `this Act does not apply`, which the brief does not list as an outcome. This is a difference of presentation rather than of law: both say the Act puts no limit on asking. But a caller who checks only "is it barred?" gets the same answer either way, while a caller who checks for "does not bar" gets a different one. **For the encoder to decide:** keep the third value and add it to the brief, or fold it into `this Act does not bar it`. I did not change the expected value.

## Agreements worth noting

- s 4 has no pre-commencement saving; the encoding correctly bars a Federal Court or Territory Supreme Court decision even when the proceeding began before commencement (scenarios 8, 9b).
- s 3(2) saves a pre-commencement HC proceeding whatever its content (scenario 7).
- Both limbs of s 3(1) are required (scenarios 2-6).

## Gaps

- The three alternatives in s 3(1)(b) (Constitution / Commonwealth law / instrument) are a single boolean input, so scenarios 2-4 are the same test; the encoding cannot tell which one applied. Acceptable for the question asked.
- Limb (a) is likewise one boolean, so "HC original jurisdiction" and "appeal from State SC in federal jurisdiction" (5, 6) are indistinguishable inputs.
- Nothing tests whether a decision is "a Federal Court"; the court category is an input.
- Commencement date (proclaimed, Note 1: assent proclaimed 6 Aug 1968; commencement date not in text) is an input, as the brief says.

## Change after the pass (encoder)

- **Line 29 (a decision of another court).** Accepted. The Act does not bar it; the separate "does not apply" outcome was removed (F1). One of the encoder's tests was updated, with a comment.
- The input gaps listed above are recorded as known limits in NOTES.md.
