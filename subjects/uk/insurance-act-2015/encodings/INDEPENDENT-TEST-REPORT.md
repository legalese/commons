# Independent test report: Insurance Act 2015 encoding

- Expectations: `independent-expectations.md`, written from BRIEF.md and the source text before any `.l4` file was opened.
- Tests: `tests-independent.l4` (imports prelude, daydate, ia-types, ia-presentation, ia-terms-and-fraud, ia-goal).
- Run: `L4=~/.local/bin/l4 ./check.sh`.

## Result

| | count |
|---|---|
| assertions | 109 |
| satisfied | 108 |
| failed | 1 |
| non-assertion errors | 0 (check.sh's 1 error for this module is the failed assertion) |

Coverage: application and the 11/12 August 2016 edge (A1-A8); each circumstance with every s 3(5) exception, with and without enquiry, notice under s 3(4)(b), and immateriality (B1-B16); the s 3(3)(b) and (c) limbs (C1-C6); qualifying breach and deliberate/reckless (D1-D9); Sch 1 paras 2, 4, 5, 6 with worked numbers, including paras 5 and 6 together (E1-E12); s 10 with losses before, on, between and after the breach and remedy days, never-remedied breaches, a year-end and a leap-day edge, and each s 10(3) exception (F1-F17); s 11 (G1-G5); s 12 including the same-day event (H1-H8); and the overall amount payable (I1-I17).

## Failure

### L240: E4' — para 5 different terms that would raise the payout

- **Scenario:** innocent qualifying breach; but for it the insurer would have contracted on different non-premium terms at the same premium (£10,000). Under the actual terms the claim is £100,000; under the different terms it would be £120,000.
- **My expected value:** £100,000.
- **The encoding's value:** £120,000. `the remedy for the presentation in ... given ... and ...` always pays the claim under the different terms when `different terms, other than the premium` is TRUE.
- **The Act:** Sch 1 para 5: "the contract is to be treated as if it had been entered into on those different terms **if the insurer so requires**." Para 6(2) likewise uses the different terms only "if applicable".
- **View:** the Act is right and the encoding is wrong. Para 5 is the insurer's election and a remedy for the insurer. The encoding says its answer is "the most the insurer may do", but on these facts that is to stay on the actual terms and pay £100,000. The encoding needs either an input for whether the insurer requires the different terms, or the lower of the two amounts as "the most the insurer may do". With the current code, the insured's breach increases what the insurer must pay. The same applies when paras 5 and 6 are combined (X% of the larger figure).

## Remarks on the encoding

1. **Consumer contracts and Parts 3-4.** `Parts 2 to 4 apply to` is FALSE for a consumer contract. Only Part 2 is limited to non-consumer contracts (s 2(1)). Sections 10-12 speak of "a contract of insurance", and s 22(2) limits Parts 3 and 4 only by date. So for a consumer contract entered after 11 Aug 2016, the top-level goal ignores a fraudulent claim, a s 10 suspension and s 11, and pays the full claim. The brief is about a business insured, so this is out of scope, but the name and the `@export` text overstate it. The goal should either refuse consumer contracts or apply ss 10-12 to them. I did not assert this (reading R2).
2. **Act does not apply → full claim.** Where the contract predates 12 Aug 2016, `amount payable on the claim` returns the claim under the actual terms. The `@export` text says so, but the brief's rule is to use `REFUSE` where the source does not answer. The old law (avoidance ab initio, warranty discharge) could give a quite different figure. I recorded this as R13 rather than as an assertion.
3. **Para 5 election not modelled** (see the failure). Para 4 and para 2 avoidance are also treated as exercised ("may avoid"). That is consistent with "the most the insurer may do", but para 5 is the only remedy where exercising it can hurt the insurer.
4. **Dates.** The relevant period (computed as `add months` then minus one day, giving 11 Aug 2016), the s 10 strict-after/strict-before reading, the never-remedied case and the s 12 same-day reading all match my expectations, including at month, year and leap-day boundaries.
5. **s 3 per circumstance.** This is faithful: enquiry switches off only s 3(5), and notice under s 3(4)(b) still works after enquiry. "Knows or ought to know" is one flag, which is acceptable because ss 4-6 are inputs.
6. **s 8(6) burden.** The burden of proof is folded into the input `the insured knew of the breach or did not care`. That is acceptable, but the field could say "as shown by the insurer".
7. **s 12(2)(b) and Sch 1 para 2(b).** Premium retention is modelled only for Sch 1 (`must return the premiums paid`). For termination for fraud, s 12(2)(b) "need not return any of the premiums" is not output. This is minor.
8. **s 10 "attributable to something happening".** A single date stands for both the loss and the thing it is attributable to. The goal tests the claim's event date. This is fine for the brief, but a loss occurring after remedy that is attributable to something during the breach would be paid. The input description should tell users to give the earlier date.

## Change after the pass (encoder)

- **Line 240 fixed (Sch 1 para 5, "if the insurer so requires").** The different terms are now applied only when they lower the claim. That case now passes (NOTES F4).
- **Consumer contracts.** The encoding now has `Parts 3 and 4 apply to` (s 22(2), date only), and the top-level goal applies ss 10-12 to consumer contracts. Part 2 still applies only to non-consumer contracts, because for consumers the 2012 Act governs disclosure, which is not applied here.
- **Contracts before 12 August 2016.** For these, the top-level amount now REFUSEs: the law before the Act is not encoded.
- **The minor gaps** (the s 8(6) burden, the s 12(2)(b) premiums output, one date for s 10) are recorded in NOTES.md as known limits. None of the independent assertions was changed.
- After the change, `check.sh` shows 6 modules: 177 assertions satisfied, 0 failed, 0 errors (68 encoder, 109 independent).
