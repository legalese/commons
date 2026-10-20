# Independent test report: Submarine Cables and Pipelines Protection Act 1963

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 28 assertions, 27 satisfied and 1 failed. The failed assertion is the only error, so there are no syntax errors.

## Scenarios (20)

1-4 s 7(1) and (1A) penalties, on indictment and summarily (s 10(2)). 5 no fault. 6 a foreign ship. 7-8 the s 5(1)(a)/(b) limits. 9-11 the kinds of damage in s 7(1)(a)-(c), including a telegraph cable damaged in a way that would not interrupt communications. 12-14 the s 7(2) life-saving exception. 15-17 s 8 repair cost. 18-20 s 9 indemnity.

## Disagreement (1)

**Scenario 14. Conduct that resulted in the break (s 7(1)), done solely to save lives or the ship, with all necessary precautions taken.** I expected an offence. The encoding gives no offence.

- Source: s 7(2): "... the last preceding subsection does not apply in relation to the break or injury." Since s 7(1A) was inserted, the last subsection before (2) is (1A), the negligence offence. On its words, s 7(2) disapplies only (1A).
- The encoding's own comment (F1) reads "the last preceding subsection" as both (1) and (1A). That is a purposive reading: the words were probably drafted when (1) stood alone, and (1A) was inserted between them later. It is not what the text says.
- Confidence in my reading: moderate as a literal reading of the text. As a reading of what Parliament intended, the encoding's view is plausible. Outside the Act, the Criminal Code s 10.3 (sudden or extraordinary emergency) would probably excuse the s 7(1) conduct anyway, but s 5A and the Code are out of scope. The encoding should at least flag that its result departs from the literal words, and a lawyer should rule on it.

## Coverage gaps

- For s 8 and s 9, the tests cover only the s 5(1)(a) limit (not on the high seas or in the EEZ). The s 5(1)(b) limit (a protection-zone cable) was tested only against s 7.
- s 7(1) fault is modelled as "my conduct resulted in it". The Criminal Code's default fault elements (s 5A) are out of scope, so intention and recklessness are not tested.
- s 10(1) (no double punishment) is out of scope.
- s 7(2) "persons acting" assumes that "we" means the same persons as the accused. No input distinguishes them.

## Change after the pass (encoder)

- The disagreement was accepted: s 7(2) now disapplies only s 7(1A), as written (F1).
- The gaps are recorded as known limits in NOTES.md.
