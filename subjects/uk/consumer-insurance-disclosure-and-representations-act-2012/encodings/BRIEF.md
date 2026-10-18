# Encoding brief: the Consumer Insurance (Disclosure and Representations) Act 2012 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Consumer Insurance (Disclosure and Representations) Act 2012** (2012 c. 6), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 12 August 2016, deposited at `../registers/source-bundle/ukpga-2012-6.txt` (Crown copyright, Open Government Licence v3.0).

The conversion drops the paragraph numbers in the Schedules and the formula in Schedule 1. The paragraphs of Schedule 1 Part 1 are, in order:

- para 1, General;
- para 2, deliberate or reckless;
- para 3, careless: claims;
- para 4, what the insurer would have done;
- para 5, not on any terms;
- para 6, on different terms;
- para 7, a higher premium;
- para 8, "reduce proportionately", where X = (premium actually charged ÷ higher premium) × 100;
- para 9, treatment of the contract for the future.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a consumer made a misrepresentation before taking out insurance and has now made a claim. Does the Act apply; is it a qualifying misrepresentation, and is it deliberate or reckless, or careless; and what may the insurer do: avoid the contract, keep or return the premiums, rewrite the terms, cut the claim proportionately, or end the contract for the future?*

1. **Does the Act apply** (ss 1, 12(4)): a consumer insurance contract, entered into (or varied) after the Act came into force.
2. **Qualifying misrepresentation and its class** (ss 2(2), 3(5), 4(1), 5): breach of the duty of reasonable care (the care itself is a finding under s 3(1)-(4), and dishonesty always shows lack of it), inducement, then deliberate or reckless versus careless, with the burden and presumptions in s 5(4)-(5).
3. **The insurer's remedies** (s 4(3), Schedule 1 Part 1 paras 2, 4-9): for a contract (not a variation).

Left out on purpose: group insurance (s 7, Sch 1 Part 3), life of another (s 8), variations (Sch 1 Part 2), warranties (s 6), agents (s 9, Sch 2), contracting out (s 10), consequential amendments (s 11).

## Inputs, not worked out

- Whether the consumer took reasonable care (s 3(1)-(4) is evaluative), and whether the misrepresentation was dishonest.
- What the insurer would have done without it: not entered at all; or entered on different non-premium terms; and the premium it would have charged.
- The premium actually charged, the premiums paid, the amount of the claim under the actual terms and under the different terms, and any part of the premiums it would be unfair to keep.
- The consumer's state of mind, where shown, with the facts the presumptions in s 5(5) need.

## Dates

The remedies involve no periods. "Reasonable notice" in para 9 is not computed.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`cidra-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
