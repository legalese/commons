# Encoding brief: the Consumer Guarantees Act 1993 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Consumer Guarantees Act 1993**: New Zealand, Public Act 1993 No 91. The source is the version as at 24 January 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_1993_91.txt` (sha256 `b501a441fee73906e125184cd57fd714bff0d4ff5350411f7cd465fafd851852`), converted from the PCO's XML on 2026-10-13 (`act_public_1993_91.meta.json` beside it). There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** The paragraph labels ((a), (b), (i) …) are not in the text; a provision's place in its list gives its label.

What the Act covers:
- **ss 1-4**: purpose; who is a consumer, a supplier, a manufacturer; what are goods and services; when goods and services are supplied.
- **Part 1, ss 5-15**: the guarantees for goods: title, delivery, acceptable quality (and for gas and electricity), fitness for a particular purpose, description, sample, price, repairs and spare parts, manufacturers' express guarantees.
- **Part 2, ss 16-24**: redress against the supplier: when it exists, the remedies (remedy, have it remedied elsewhere, reject, damages), loss of the right to reject, failures of a substantial character, refund or replacement, collateral credit, gifts.
- **Part 3, ss 25-27**: redress against the manufacturer and its exceptions; damages.
- **Part 4, ss 28-40**: the guarantees for services (care and skill, fitness, time, price) and the remedies (remedy, cancel, damages), cancellation and its effects.
- **Part 5, ss 41-56**: exceptions (not in trade; charities), repairs and parts notices, contracting out between businesses, hire purchase, representations by dealers, assignees and creditors, gas and electricity indemnity, which court or tribunal, and contracts made before 1 April 1994.

## The top-level goal, and the goals under it

Top level: *for this supply to this consumer, does the Act apply; which guarantees has it failed; against whom does the consumer have redress; and which remedies are open to them?*

1. **Scope**: ss 2, 41, 43, 43A, 56.
2. **Goods and the supplier**: Parts 1-2.
3. **Goods and the manufacturer**: Part 3, ss 12-14, 42.
4. **Services**: Part 4.
5. **Money, courts and liability**: ss 44-47.

Inputs, not worked out:
- what a reasonable consumer would regard as acceptable, reasonable, substantial or foreseeable, and whether a reasonable time has passed;
- whether goods are of a kind ordinarily acquired for personal, domestic or household use, and the other facts of who acquired what for what purpose;
- whether a failure can be remedied, and whether the supplier refused, neglected or failed to remedy it.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`cga-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
