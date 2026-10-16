# Encoding brief: the Customs and Excise Act 2018 (New Zealand), Customs value, duty and refunds, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Customs and Excise Act 2018**: New Zealand, Public Act 2018 No 4. The source is the version as at 4 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2018_4.txt` (sha256 `10dc85c46aca08ef7233551d922114ebd3feacda218f4e566682397984171c2d`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels. Within the scope below, the text is complete. The rates of duty are in the Tariff (Tariff Act 1988), not this Act, and are inputs.

**Working day.** The Act does not define it, so the Legislation Act 2019, s 13 applies: not a Saturday, Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Matariki Observance Day or Labour Day; not 25 December to 2 January; the Monday after 1 January if it falls on a Friday; the Monday and Tuesday after it if it falls on a weekend; the Monday after Waitangi Day or Anzac Day if either falls on a weekend.

## Scope

- **Customs value**: s 101 and Schedule 4: definitions (cl 2, especially related persons in cl 2(2)), interest (cl 3), the primary basis and when the transaction value can be used (cls 4-5), the transaction value (cl 7), and methods 2 and 3 (cls 9-12: the lowest transaction value of identical, then similar, goods). Methods 4 to 6 and cl 6 evidence are not encoded.
- **Duty**: s 120 (proportionate duty), ss 122-124 (when duty must be paid, including 20 working days after an amended assessment, an assessment or a demand).
- **Late payment penalties**: ss 159-160 (1% after the payment date, a further 4% after the 7th day).
- **Refunds**: s 142 (paid in error: within 4 years, or on an application within 4 years), s 143 (provisional Customs value), and the 20-working-day appeal periods.

## The top-level goal, and the goals under it

Top level: *for an importation: what is the Customs value, how much duty is payable, by when must it be paid, what late payment penalty has accrued, and what refund is due?*

1. **Customs value**: Schedule 4 Parts 1-3.
2. **Duty and its payment**: ss 120, 122-124, with the Legislation Act working day.
3. **Late payment penalties**: ss 159-160.
4. **Refunds**: ss 142-143.

Inputs, not worked out: the price and each cl 7 amount (and whether it is supported by sufficient information), the restrictions and conditions in cl 5, the facts of relationship in cl 2(2), comparable transaction values, the Tariff rates, the payment events and dates, Matariki Observance Days.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`cea-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
