# Independent test report — National Minimum Wage Act 1998

## Method

1. Read BRIEF.md and the Act (ss 1, 10, 11, 11A, 17, 28, 34-45B, 54) only.
2. Wrote `independent-expectations.md`, about 95 scenarios across qualification, s 17 arrears, s 10(9), s 11(3), s 11A and s 11(2), and saved it before opening any `.l4`. Dates were worked out on the calendar with their weekdays. Ten more scenarios went into an addendum after reading the record shapes and before any run. Their values come from the Act alone.
3. Read nmw-types, nmw-qualification, nmw-arrears, nmw-records and nmw-goal. Did not read nmw-tests. Wrote `tests-independent.l4`.
4. Ran `L4=~/.local/bin/l4 ./check.sh`.

## Result

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 103 | 0 |

**103 assertions, 103 pass, 0 fail, and no non-assertion errors.** (The whole encoding is 160 satisfied and 0 errors, counting the encoder's own 57.)

The tests cover the following:
- **Qualification (39):** every exclusion, with each limb of s 44, s 44A and s 40 flipped; and the s 28(1) presumption with the contrary established on school age, on worker status and on an exclusion.
- **Arrears (18):** the higher of A and A/R1 × R2, including a falling rate; s 17(6) part payments; s 17(5) full payment at an earlier R2 and then a rate rise; two payments at different times, both cleared and not cleared; overpayment; payment exactly equal to the entitlement; and a sum over several periods.
- **s 10(9) (6):** year end; 29 Feb 2028; a non-leap February; a Saturday with no move; and an agreed later day.
- **s 11(3) (11):** 31 Jan → 30 Apr; 30 Nov → 29 Feb 2028 and 28 Feb 2027; 28 Feb 2028 → 28 May; 29 Feb → 29 May; 31 Dec → 31 Mar; agreed later days.
- **s 11A (13):** Day A after the limit, on the limit, and the day before it; the (2) result exactly at Day A, exactly at B + 1 month, and one day past it; B = 31 May → 30 Jun; B = 31 Jan → 29 Feb 2028 and 28 Feb 2027.
- **Award (9):** different rates, presented on the last day, a day late, s 11(4) allowance, not well-founded, and in time and out of time under s 11A.
- **The top-level goal (9).**

## Failures

None.

## Cases that could not be asserted

- **Outside civil proceedings, with a s 1(2) fact not established, the encoding REFUSEs.** A probe confirmed it: "s 28(1) presumes qualification only in civil proceedings…". I agree with this reading of s 28(1).
- **Q39, not an individual (s 1(2) "an individual").** No input for it; the encoding assumes an individual.
- **P7/P8/C9, when the s 10(9)(b) agreement was made.** `later day agreed for production` carries no date of agreement. The caller must give it only if it was agreed "during that period". An agreement made after the 14 days cannot be represented to show that it is ineffective.
- **S15, payments in the wrong order.** Payments carry no date, so list order is taken as the order in which they were made. Callers must sort the payments.

## Remarks on the encoding (tests pass, but worth noting)

1. **The top-level goal refuses as a whole when qualification refuses.** This is the case outside civil proceedings with an unestablished fact. The s 10(9) production date, the s 11 time limit and the award do not depend on s 1(2) qualification; ss 10-11 speak of a "worker". Yet they are lost, because `qualifies` is evaluated (strictly or not) inside the same record. The probe confirmed that the whole position REFUSEs. Consider computing the records fields independently of `qualifies`.
2. **Many limbs are folded into single input booleans.** These include s 54(3)(a)/(b) and its client/customer test; s 34(1)(a)-(c); s 35 ("would be a worker if…"); s 37A(1)(b) Crown employment; s 44(1)(a)/(1A), (1)(b)/(3) training; and s 44A(3)(a)/(b). The rules are therefore only as good as the caller's reading of those inputs, and tests on those limbs are close to tautologies. This is acceptable under the brief ("status facts ... are inputs"), but the s 44 and s 44A limbs are broken out while these are not. The difference is a little uneven.
3. **The s 34 and s 35 flags bypass s 28(1).** They are plain BOOLEANs, so in civil proceedings an agency or home-worker status that is unknown is simply FALSE. The worker's-contract MAYBE then carries the presumption. This is harmless, because the presumption on `has a worker's contract` already gives TRUE when it is unknown.
4. **s 11A(2) is gated on Day A being strictly before the limit.** This matches my reading R-e. When Day A equals the limit, s 11A(2) adds nothing, but s 11A(3) then always applies, so the result is the same under either reading. I tested this (E4, E5).
5. **s 11(3) is read as "corresponding date of the end day".** This follows the brief. It differs from a Dodds v Walker style count only when the end day is the last day of a short month, e.g. 28 Feb 2027 → 28 May 2027, against 31 May on the other reading. I asserted the brief's reading (C5), and that reading is a deliberate choice that should be recorded in NOTES.md.
6. **s 17(6) is applied as max(A, A/R1 × R2) − paid.** That reduces the computed amounts, not the A inside the formula. I took the same reading (R-f). The other reading, (A − paid)/R1 × R2, gives a different answer whenever R2 ≠ R1, e.g. S9: 30 here, 0 on the other. This should be stated as a choice in NOTES.md.
7. **s 17 is computed as rate × hours.** The arrears function works out A as R1 × hours − received, which treats the s 2 hourly rate as remuneration ÷ hours. That is reasonable for the brief's scope, but the s 2 regulations can do otherwise (e.g. output work).
8. **s 11 well-foundedness includes s 10(2) reasonable belief.** This is right as a precondition of the rights. Section 10(3) (purpose) and s 10(5) (a production notice was given) are implicit in there being a receipt date.
9. **No rounding in s 17(4).** The Act gives none, and I used exact inputs. With real rates (e.g. 100/10.42 × 12.21) the result is a long rational, and a caller will need to know that no rounding is applied.

## Change after the pass (encoder, 2026-10-17)

- **Remark 1 adopted.** In the top-level position, `qualifies` and `additional remuneration owed` are now MAYBE. They are NOTHING when qualification cannot be decided: outside civil proceedings, with a s 1(2) condition not established and no exclusion established. The records fields are computed regardless.
- **Four independent assertions ported to the new shape.** These are the ones on `posQ` and `posP`. Each value is wrapped in JUST, the expected values are unchanged, and each is marked `[Ported by the encoder…]`.
- **Encoder tests.** Five encoder assertions were added for the undecided, agency-worker and excluded cases.
- **Remark 3 recorded.** Its two readings are forks F10 (s 17(6)) and F11 (s 11(3), Dodds v Walker) in NOTES.md.
- **Remarks 2 and 4 noted, not changed.** The single-boolean limbs are inputs within the brief, and A as R1 × hours − remuneration follows the s 2 regulations given as inputs.

After the change: 165 satisfied, 0 failed (62 encoder, 103 independent).
