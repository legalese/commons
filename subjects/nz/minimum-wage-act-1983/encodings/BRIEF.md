# Encoding brief: the Minimum Wage Act 1983 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Minimum Wage Act 1983**: New Zealand, Public Act 1983 No 115. The source is version 38 as at 20 December 2023, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

What the Act covers:
- **ss 1-3**: title, interpretation, application of amendments, the Crown is bound.
- **ss 4, 4A, 4B**: the Governor-General's power to prescribe, by Order in Council, a minimum adult rate (workers aged 16 or older), minimum starting-out rates (workers aged 16-19, by class) and a minimum training rate (workers aged 20 or older on training contracts), with the limits on each.
- **s 5**: the Minister's annual review.
- **s 6**: the entitlement to be paid at not less than the minimum rate.
- **s 7**: deductions for board, lodging and time lost.
- **s 8**: minimum wage exemption permits.
- **s 9**: workers to whom the Act does not apply.
- **ss 10, 11, 11AA, 11A**: penalties, recovery of wages, recovery from a person involved, compliance orders.
- **s 11B**: the 40-hour, 5-day week.
- **ss 12-14, Schedules 1AA and 1**: regulations, saving, repeals, transitional provisions.
- Reprinted with the Act: **s 6 of the Minimum Wage Amendment Act 2007** (under-rate workers' permits) and **s 7 of the Minimum Wage (Starting-out Wage) Amendment Act 2013** (the old new entrant rate).

The source is `../source/MWA1983.txt`, text extracted from the PCO's PDF; `../source/PROVENANCE.md` records it. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

## The top-level goal, and the goals under it

Top level: *for this worker and this pay period, does the Act apply; which minimum rate applies and what is it; what must the employer pay, after the deductions the Act allows; and how much is owed?*

1. **The rate**: ss 4, 4A, 4B, 8, 9 — which prescribed rate (or permit rate) governs the worker, and whether an Order's rate is within the power.
2. **What must be paid**: ss 6, 7 — the minimum for the period, allowable deductions, and the shortfall.
3. **Enforcement**: ss 10, 11, 11AA, 11A — who is liable, who may recover what, from whom.
4. **Hours**: s 11B.
5. **Administration and transition**: ss 5, 8 (issuing, in force, revocation), 13, Schedule 1AA, the 2007 and 2013 transitional provisions.

Inputs, not worked out:
- **the rates in the Minimum Wage Order** in force, and the classes it defines (ss 4, 4A, 4B are powers; the Act fixes no figure);
- a Labour Inspector's satisfaction under s 8 and the permit's terms;
- whether a person is "involved" under s 142W of the Employment Relations Act 2000;
- whether a person is a "worker" (ERA s 6) and the facts of age, benefits, employment, training and supervision.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`. Where the Act itself names an absent case (a worker under 16 belongs to no prescribed class), answer `NOTHING`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`mwa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
