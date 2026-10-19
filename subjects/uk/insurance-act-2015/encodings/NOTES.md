# Insurance Act 2015 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the claim position for` (`ia-goal.l4`). An insured has made a claim for a loss. The goal answers:

- whether Parts 2-4 (and Parts 3-4 alone) apply;
- whether a fair presentation was made, whether there was a qualifying breach, and the insurer's remedy;
- whether liability is suspended by a breach of warranty, or excluded by non-compliance with a term or by fraud;
- what the insurer may recover;
- the amount payable on the claim.

Three goals sit under it:

1. **Application** (`ia-presentation.l4`): ss 1, 2(1) and 22(1)-(3). The relevant period is computed as the 18 months beginning with 12 February 2015, ending on 11 August 2016.
2. **Fair presentation and remedies** (`ia-presentation.l4`):
   - s 3(1), (3)-(5), circumstance by circumstance;
   - s 7(3) as an input;
   - s 8;
   - Sch 1 Part 1 paras 2-6.
3. **Warranties, terms and fraud** (`ia-terms-and-fraud.l4`): ss 10(2)-(5), 11 and 12(1)-(3).

As the user asked, this covers only the sections those goals need. The rest of the Act was left out on purpose (see the table).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the business policyholder (the insured)**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "I have claimed for a loss. Did I present the risk fairly; if not, what can the insurer do; does a breached warranty or term, or fraud, stop my claim; and how much will I be paid?"

The facts it asks for are ones that person can state, or findings made about them.

The remedy and the s 10-12 answers are phrased from the insurer's side ("may avoid", "suspends liability"). For the insured, they are the reasons the payout may be reduced or refused. The amount payable is what the insured will receive.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| s 1, s 2(1) | encoded (goal 1) |
| s 2(2), Sch 1 Part 2 | out of scope: variations |
| s 3(1), (3)-(5) | encoded (goal 2) |
| ss 4-6 | input: what the insured knows or ought to know, and what the insurer knows, ought to know or is presumed to know |
| s 7(3) | input: materiality; (5) folded into "substantially correct" |
| s 8 | encoded (goal 2); the s 8(6) burden is folded into the input finding |
| s 9 | out of scope: basis clauses |
| s 10(1)-(6) | encoded (goal 3); (7) amends another Act |
| s 11 | encoded (goal 3) |
| s 12(1)-(3) | encoded (goal 3); (2)(b) premiums are not an output |
| s 13, s 18 | out of scope: group insurance |
| s 13A, s 16A | out of scope: "reasonable time" is evaluative |
| ss 14-17 | out of scope: good faith, contracting out |
| ss 19-21, Sch 2 | out of scope |
| s 22(1)-(3) | encoded (goal 1) |
| Sch 1 Part 1 paras 1-6 | encoded (goal 2) |

## Forks (readings taken)

- **F1, lost paragraph numbers and formula.** The conversion drops the Schedule paragraph numbers and the para 6 formula. The encoding uses the printed order (paras 1-6), and X = premium actually charged ÷ higher premium × 100, from the Act as published.
- **F2, s 22(3): the relevant period.** The 18 months beginning with 12 February 2015 end on 11 August 2016. Contracts entered into on or after 12 August 2016 are covered. The day of Royal Assent is taken from the Act's citation, because the text does not print it.
- **F3, s 8(1)(b): "different terms".** A higher premium is a different term.
- **F4, Sch 1 para 5: "if the insurer so requires".** The insurer requires the different terms only when they lower the claim. This was corrected after the independent pass. Para 6 then applies to whichever basis is used.
- **F5, s 10(2): "after ... breached but before ... remedied".** The loss is on a day strictly after the day of breach and strictly before the day of remedy. A breach never remedied suspends cover indefinitely.
- **F6, s 11.** Where the insurer may rely on non-compliance, the encoding takes it that the term excludes liability for this loss. Whether the term does so is a matter of the contract.
- **F7, s 12(2)(a): "after the time of the fraudulent act".** The event is on a day strictly after the day of the fraudulent act.
- **F8, consumer contracts.** Part 2 does not apply to them (s 2(1)); the 2012 Act governs disclosure and is not applied here. Parts 3-4 do apply (s 22(2)). This was corrected after the independent pass.
- **F9, contracts before 12 August 2016.** The top-level amount REFUSEs, because the law before the Act is not encoded.
- **F10, the remedy is the most the insurer may do** (paras 5-6 say "if the insurer so requires" and "may").

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18:

- 6 modules: 177 assertions satisfied, 0 failed, 0 other errors;
- 68 are the encoder's (`ia-tests.l4`);
- 109 are independent (`tests-independent.l4`).

The independent pass found one disagreement (para 5), which was fixed. No assertion is expected to fail.

## Open questions for a UK lawyer

- **F6:** for s 11, does the encoding's "excludes liability" overstate what the term does?
- **F5:** confirm the treatment of a loss on the day of breach or on the day of remedy.
