# Independent test report: Gas Act 1986 encoding

## Method

1. Read BRIEF.md and the source (ss 10-11, 30G-30O, 37; Sch 2B paras 7, 11, 19, 24, 28) only. Wrote `independent-expectations.md` (89 scenario rows across C1-C26, D1-D30, R1-R33) before opening any module.
2. Read gas-types, gas-connection, gas-cutoff, gas-redress and gas-goal (not gas-tests). Wrote `tests-independent.l4`. No expected value was changed to fit the code.
3. Ran `L4=~/.local/bin/l4 ./check.sh` and `fails.sh tests-independent.l4`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 1 | 96 | 1 |
| whole encoding (7 modules) | 1 | 206 | 1 |

There are no syntax or type errors. The one error is the failed assertion. gas-tests.l4 still passes (110/110).

## The failing assertion

### D3: payment made late, but before the cut-off (tests-independent.l4 line 106)

- **Scenario:** written demand on 1 Mar 2026. The consumer pays on 30 Mar 2026, one day after the 28 days. The supplier gives notice of intention on 30 Mar 2026 and cuts off on 6 Apr 2026. The supplier is the current supplier and nothing is in dispute.
- **Expected:** `JUST (Date 6 4 2026)`, meaning the power is exercisable from 6 Apr 2026.
- **Code:** `NOTHING`. Rule F3 in `the day the power arises for` ends the power once the payment is made on or before the day the supplier acts.
- **Source:** para 7(1): "Sub-paragraphs (3) and (4) below apply where (a) a demand in writing is made ...; and (b) the consumer does not make those payments within 28 days after the making of the demand." Para 7(3): "he may, after giving not less than 7 days' notice of his intention ... cut off the supply."
- **My view:** read literally, the Act favours my expectation. The condition in 7(1)(b) is fixed at the end of the 28th day. Nothing in para 7 says the power lapses when a late payment arrives. Para 19(2)(a) does show that paying matters, because once the default is made good the bar on restoring is lifted. But it does not take away a cut-off that 7(3) had already allowed. The code's F3 is a purposive, pro-consumer reading. Cutting off for a debt already paid serves no purpose, and supply licence conditions probably forbid it. It is defensible, but it is a gloss on the statute, not its words. It should at least be stated in NOTES.md as a deliberate departure, or replaced by the literal rule with the licence-condition point left as an unmodelled qualification. The 7(1)-level test for the same facts (`the day para 7(1) applies from for`, line 104) passes. So both readings agree that the 7(1) conditions are met, and differ only on whether a later payment ends the power.

## Readings I flagged that the code shares (no failure)

- **D11, notice given before the power arises.** The brief says the para 7(3) notice must be given once (1) or (2) applies. The code does the same (F2). The Act only says "after giving not less than 7 days' notice of his intention". It does not say when the notice must be given. I followed the brief, and the test passes. This is a point of construction to keep in NOTES.md.
- **Para 7(3), "not less than 7 days' notice".** The brief and the code take notice day + 7. A clear-days reading would give notice day + 8. I followed the brief.
- **s 30M(5), a late application.** The code suspends compliance only for an application made within the 42 days. I agree: an application out of time is not "an application ... under this section".

## Gaps in the encoding

1. **s 10(3), a connection no longer required (C9).** `already connected` bundles "connected" with "still required". With FALSE, the case is treated as a new connection request, and the result is "must connect" or "no valid notice yet" rather than "no duty to maintain". There is no outcome for "connected, but no longer required, so no duty".
2. **s 10(5), (5A), the licence condition and the amount (C20-C22).** `the connection charge for` returns only which kind of cost may be charged. It has no input for "the transporter so requires and the conditions of his licence so allow", and no amount. So C21 (licence does not allow, consumer pays nothing) cannot be expressed.
3. **s 10(6), the vesting date (C23).** Vesting is a boolean. The day the pipe vests ("at that time", the connection day) is not an output.
4. **s 10(9)(b) is one input.** "Danger" and "took all reasonable steps" are merged into one boolean, so the two-limb structure is not tested by the rule.
5. **Para 11(1)(a)-(c) exception (D22).** `restoring the supply myself is an offence for` depends only on consent. It does not ask under which power the supply was cut off, so a cut-off under paras 20-22 (gas escapes) or under the safety regulations still makes self-restoration an offence under para 11. The Act excludes those cases. Para 11(2)(b) (supplier may cut off again) is also not output.
6. **Para 24(3), affixed notice (D30).** Unoccupied premises whose owner cannot be found, with notice affixed at least 48 hours before entry, are not modelled. Para 24(2) notice "to the owner of the premises if they are unoccupied" is folded into hours of notice.
7. **s 37(2)(b), a percentage reduction (R30).** The reduced maximum is an input (`maximum price without the information`). A direction that reduces by an amount or percentage is not computed. The user must work out 900 themselves.
8. **s 30N(4).** The commencement of Sch 14 to the Energy Act 2013 is a boolean input, not a date compared with the contravention. That is reasonable, because the date is not in the deposited text.
9. **s 30N(1) after an appeal.** When an appeal is determined and compensation is still unpaid, interest runs from the day after the original compliance date. Any substituted date under s 30M(6)-(7) is not modelled. This is acceptable because those are court discretions, but it may be worth a note.
10. **s 30G(1)(b).** "One or more consumers have suffered loss ..." is encoded from the seat as "I suffered". That fits the seat, but the order could be made where other consumers suffered and this one did not.

## Change after the pass (encoder)

- **D3 (a late payment).** Accepted. The power under para 7(3) no longer ends when the consumer pays after the 28 days (F3). The assertion passes; three of the encoder's own tests that took the old reading were updated, with a comment.
- The gaps listed above are recorded as known limits in NOTES.md.
