# Independent test report — CIDRA 2012 encoding

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the Act alone,
before any `.l4` file was opened. Tests are in `tests-independent.l4`. `cidra-tests.l4`
was not read.

## Result

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 106 | 0 |
| all modules | 0 | 150 | 0 |

**106 assertions, 106 pass, 0 fail, 0 non-assertion errors.**

### One correction to my own test inputs (not to an expected value)

The first run had 4 failures (R2 and R3, para 2). They came from my test inputs, not the
encoding: I passed £1,200 as the *premium actually charged* together with an insurer
that would have charged £400. That is not a higher premium, so there was no inducement
(s 4(1)(b)) and no qualifying misrepresentation. The scenario as written in the
expectations needs a qualifying misrepresentation with premiums *paid* of £1,200, so I
set premium charged to £300 and kept premiums paid at £1,200. The expected values
(avoid; pay £0; return £300 / £1,200) were not changed. Both scenarios now pass.

## Coverage of the expectations

- Goal 1 (A1-A13): tested through the encoding's booleans. The date scenarios (A8-A12:
  5/6/7 April 2013, 8 March 2012, 1 January 2013) **cannot be tested as dates**. The
  encoding takes `entered into after the Act came into force` as an input, so only the
  boolean outcome is asserted.
- Goal 2 (Q1-Q11, C1-C13): all tested. That includes inducement by a higher premium
  only (Q5) and an equal "higher" premium (Q9). It also includes dishonesty overriding a
  finding of reasonable care (Q3, Q10), the burden in s 5(4) (C7), presumptions
  5(5)(a) and (b), and the contrary being shown for each (C8-C11b).
- Goal 3 (R1-R18, F1-F5, F8, F9, T1-T4): all tested, with worked numbers for para 8:
  X = 75, 50, 33⅓, 99.9 and 25, and paras 6 and 7 together (X = 40 of a £6,000
  different-terms claim gives £2,400). The 33⅓ case comes out at exactly £3,000, so the
  numbers are exact rationals.
- **Not testable (no corresponding output):** F6, F7 (para 9(6), the consumer's right to
  terminate after the insurer's notice), F10 (para 9(7), refund for the balance of the
  term) and F11 (para 9(1)(b), an outstanding claim). There are no REFUSE cases.

## Remarks on the encoding

1. **Para 9(6)-(8) are not encoded.** The `Remedy` record gives only the insurer's para
   9(4) rights. It does not give the consumer's right under 9(6) to terminate on
   reasonable notice after the insurer's 9(4)(a) notice, a right the 9(5) life-insurance
   bar does not touch. It also does not give the insurer's duty under 9(7) to refund
   premiums for the balance of the term, or 9(8) (earlier claims unaffected). 9(7) is a
   real money consequence within the brief's goal 3 ("end the contract for the future").
   It could be an input amount, echoed as a refund when termination is available.
2. **Commencement is a boolean, not a date.** The Act does not state the commencement
   day (s 12(2) leaves it to a Treasury order; SI 2013/450 gives 6 April 2013), so taking
   the fact as an input is defensible. Still, nothing in the encoding applies the s 12(3)
   floor (no day before 8 March 2013). It also does not settle whether a contract made
   on 6 April 2013 is "after" commencement, which I read as yes. NOTES.md should say this.
3. **The exported goal-2 and goal-3 functions do not check the Act applies.** `is a
   qualifying misrepresentation …` and `the insurer's remedy for …` are both `@export`ed.
   Called directly on a company policyholder or a pre-commencement contract, they return
   remedies under the Act. Only the top-level goal gates them on `the Act applies to`.
   Either gate them too or say so in their `@desc`.
4. **The careless-remedy helper overstates para 9(4) when it is called on its own.** Given
   `the contract, on these terms` with no different terms and a premium not higher than
   the one charged, it returns notice TRUE / terminate TRUE. No para 6 or 7 right exists
   there. This cannot happen through the exported functions, because the qualifying test
   filters it out, and the helper is not exported. So it is latent only. Guard it on
   `different OR higher > charged`.
5. **Para 6 "if the insurer so requires" is not an input.** The encoding always reports
   the most the insurer may do: different terms applied and the claim measured under
   them. That is a stated, reasonable choice. A user whose insurer has not elected para 6
   gets a figure the insurer could claim, not one it has claimed.
6. **Dishonesty and class.** `made dishonestly` affects only breach (s 3(5)), not class.
   I agree, because class turns on s 5(2) alone. But the inputs allow incoherent
   combinations, such as dishonest = TRUE with `knew it untrue` = JUST FALSE, and nothing
   flags them.
7. **Para 9(1)(b) (outstanding claim).** The encoding gives para 9 rights whether or not
   a claim is outstanding. That matches my reading: 9(1)(b) limits what para 9 governs,
   it does not switch para 9 off. Worth a line in NOTES.md.
8. **Para 2(b) premiums to return** is passed through from `premiums unfair to retain`
   with no cap at premiums paid. This is harmless if the inputs are coherent.
9. Readings I agree with (tests pass): a higher premium alone is "different terms" under
   s 4(1)(b). An equal premium is not inducement. The s 5(5) presumptions apply only
   where the fact is not shown (NOTHING), and a JUST value rebuts them. Para 5 returns
   all premiums paid, ignoring the "unfair" figure. Para 9(4) is not available on a
   para 5 (no contract) case. Life insurance bars only 9(4)(b) termination, not notice,
   para 2 or para 5 avoidance.

## Change after the pass (encoder)

- **Remark 1, in part:** `Remedy` now has `consumer may terminate after the insurer's notice` (Sch 1 para 9(6)). It is TRUE whenever the insurer may give notice under 9(4)(a), and the life-insurance bar in 9(5) does not touch it. Paras 9(7)-(8) (refund for the balance of the term; earlier claims unaffected) are still not computed, and NOTES says so.
- **Remark 5, the para 2(b) refund:** this is now capped at the premiums paid.
- **Remark 3, the exported helpers:** these are left as they are. NOTES says that only the top-level goal checks that the Act applies.
- **Remark 2, commencement:** this stays a yes/no input, because the Act does not name the day. NOTES says so.
- The encoder added four assertions to `cidra-tests.l4`, all of which pass. None of the independent assertions was changed.
- After the change, `check.sh` shows 6 modules: 154 assertions satisfied, 0 failed, 0 errors (48 encoder, 106 independent).
