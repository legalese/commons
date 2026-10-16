# Encoding brief: the Electricity Industry Act 2010 (New Zealand), supply obligation, disputes and enforcement, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Electricity Industry Act 2010**: New Zealand, Public Act 2010 No 116. The source is the version as at 30 March 2025, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2010_116.txt` (sha256 `8c046a4c499f3700876474ccd58233873f557a59bb53f5133788d63c354e5f31`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**Billing is not in the Act.** Retail billing, disconnection and consumer care rules are in the Electricity Industry Participation Code 2010 and regulations under s 113, which are secondary legislation and not in this source. This encoding covers the consumer-facing and enforcement rules the Act itself states.

**Working day**: the Act does not define it, so the Legislation Act 2019, s 13 applies (with s 55 extending a period that ends on another day).

## Scope

- **Supply obligation**: s 105 (a distributor's continuing obligation to supply line function services or electricity from an alternative source; the offence and its daily fine), s 106 (when it ends; when it is suspended), s 107 (at least 6 months' notice of a proposal to supply from an alternative source).
- **Disputes**: s 95(2) (who may complain), s 96 (membership of the dispute resolution scheme, exemptions, the $100,000 offence).
- **Enforcement**: s 52 (limitation: 3 years from discovery, 10 years from the breach), s 54(1)(d) (pecuniary penalties for Code breaches: $2 million and $10,000 a day), s 54(3) (related breaches as one), s 66 (appeals within 20 working days), s 80(2)-(3) (pecuniary penalties under Part 3: $500,000 for an individual; for a body corporate the greater of $10 million and 3 times the gain or 10% of turnover).

## The top-level goal, and the goals under it

Top level: *for a distributor and a place, or an industry participant and a breach: must supply continue, may a complaint be made and must the participant be in the scheme, may the Authority still act on a breach, what is the most penalty, and by when must an appeal be lodged?*

1. **Supply obligation**: ss 105-107.
2. **Disputes**: ss 95-96.
3. **Enforcement**: ss 52, 54, 66, 80.

Inputs, not worked out: whether s 105 applies to the distributor and place, written agreements and assignments, the reason supply ceased and whether it continues, the notice given, the complainant's status, exemptions, the dates of breach and discovery, gain and turnover.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`eia-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
