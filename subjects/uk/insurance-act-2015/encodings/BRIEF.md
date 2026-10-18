# Encoding brief: the Insurance Act 2015 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Insurance Act 2015** (2015 c. 4), United Kingdom, passed on 12 February 2015. The source is the revised text on legislation.gov.uk, point in time 4 May 2017, deposited at `../registers/source-bundle/ukpga-2015-4.txt` (Crown copyright, Open Government Licence v3.0).

The conversion drops the paragraph numbers of the Schedules and the formula in Schedule 1. Schedule 1 Part 1 is:

- para 1, general;
- para 2, deliberate or reckless;
- para 3, other breaches;
- para 4, not on any terms;
- para 5, different terms;
- para 6, a higher premium, where X = (premium actually charged ÷ higher premium) × 100.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a business (non-consumer) insured has made a claim for a loss. Do Parts 2-4 apply to the contract; did the insured breach the duty of fair presentation, and what may the insurer do about it; was the insurer's liability suspended by a breach of warranty, or excluded by non-compliance with a risk-reducing term; and is the claim, or the contract, affected by fraud? What, in the end, must the insurer pay on this claim?*

1. **Application** (ss 1, 2(1), 22(1)-(3)): a non-consumer insurance contract entered into after the end of the relevant period, the 18 months beginning with 12 February 2015.
2. **Fair presentation and remedies** (ss 3, 7(3), 8; Sch 1 Part 1):
   - whether the duty was breached, circumstance by circumstance;
   - whether the breach is a qualifying breach, and whether it is deliberate or reckless;
   - the insurer's remedy, and the amount payable on the claim.
3. **Warranties, other terms and fraud** (ss 10, 11, 12):
   - whether the insurer is liable for a loss given a breach of warranty and its remedy;
   - whether the insurer may rely on non-compliance with a term under s 11;
   - the effect of a fraudulent claim, and of terminating for one, on this claim.

Left out on purpose:
- variations (s 2(2), Sch 1 Part 2);
- the detail of what the insured or insurer knows (ss 4-6, which are inputs);
- warranties created by basis clauses (s 9);
- group insurance (ss 13, 18);
- late payment (s 13A: "reasonable time" is evaluative);
- good faith (s 14);
- contracting out (ss 15-17);
- Part 6 and Sch 2.

## Inputs, not worked out

- **Each material circumstance:**
  - whether the insured knows or ought to know it (ss 4, 6);
  - whether it was disclosed, or enough was disclosed to put a prudent insurer on notice;
  - whether the insurer enquired;
  - whether an exception in s 3(5) applies.
- **The presentation as a whole:** whether it was reasonably clear and accessible, and whether the representations were substantially correct and made in good faith.
- **What the insurer would have done**, the premiums, and the claim under the actual and the different terms.
- **The dates:** the warranty breach and its remedy, and the loss; the fraudulent act and the event the claim is for.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"The period of 18 months beginning with" 12 February 2015**: ends on 11 August 2016, so the Act applies to contracts entered into from 12 August 2016.
- **s 10(2) "after a warranty ... has been breached but before the breach has been remedied"**: a loss on a day strictly after the day of breach and strictly before the day of remedy.
- **s 12(2)(a) "a relevant event occurring after the time of the fraudulent act"**: an event on a day strictly after the day of the fraudulent act.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ia-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
