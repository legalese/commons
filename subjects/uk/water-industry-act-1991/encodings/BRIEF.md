# Encoding brief: the Water Industry Act 1991 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Water Industry Act 1991** (1991 c. 56), United Kingdom (England and Wales). The source is the revised text on legislation.gov.uk, point in time 30 July 2026, deposited at `../registers/source-bundle/ukpga-1991-56.txt` (Crown copyright, Open Government Licence v3.0). The conversion drops the paragraph numbers in the Schedules: Schedule 4A ("Premises that are not to be disconnected for non-payment of charges") runs 1 dwellings, 2 houses in multiple occupation, 3 accommodation for the elderly, 4 hospitals, 5 medical premises, 6 dental premises, 7 NHS primary care premises, 8 care homes and independent hospitals, then children's homes, secure accommodation, schools, 16 to 19 Academies, further and higher education, childcare, prisons and removal centres, police, fire and rescue, and ambulance premises.

## Seat

The encoding is written from the seat of **the water customer**: the owner or occupier who wants a connection, is supplied and charged, or faces disconnection (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the customer's words: *"Must the water company connect my premises to its main, by when, and what conditions can it impose; what interest is due on my deposit; can the sewerage company still refuse my drain? Can my water be cut off for non-payment, from when; can a limiting device be used on my home? When I move out, until when am I liable for charges; can I insist on a meter, revoke it, or be put on one against my will?"*

1. **Connections** (ss 45(1)-(2), 47(1)-(3), 48(1), 51(1)-(3), (6), 106(1), (3)-(4)):
   - whether the duty to connect arises (a building, domestic purposes, not a trunk or non-domestic main, conditions satisfied);
   - whether a condition was imposed in time (s 47(3));
   - the relevant day and the last day for the connection (s 51);
   - the interest on a deposit (s 48: every 50p, every three months);
   - the last day the sewerage undertaker can refuse a communication with the public sewer (s 106(4)).
2. **Disconnection for non-payment** (ss 61(1), (1ZA), (1A), (2)-(3), 63(3), 63A(1), Schedule 4A):
   - whether the premises are protected by Schedule 4A;
   - the earliest day the supply can be cut off for non-payment after the notice, and the effect of a counter-notice;
   - whether a cut-off on a given day is lawful, and whether it would be an offence (s 63(3));
   - whether a limiting device would be an offence (s 63A).
3. **Charges** (ss 144(2)-(7), 144A(1)-(3), (5)-(7), 144B(1)-(3)):
   - after leaving the premises: whether I can still be charged, and the last day of liability;
   - after a s 62 notice: from when I am no longer liable;
   - whether I may require charging by volume (a meter), whether the undertaker must give effect to it, and the last day to revoke;
   - whether the undertaker may move my home to metered charges without my notice or consent.

Left out on purpose: the regulators, licensing, enforcement and special administration (Part II); water resources, bulk supplies and requisitions; quality and fluoridation; sewerage beyond s 106; trade effluent; works powers; the Schedules other than 4A.

## Inputs, not worked out

- **Working days (s 144(7)):** Saturdays, Sundays, Christmas Day, Good Friday and the bank holidays in England and Wales are disregarded. The bank holidays are an input list; Good Friday is computed.
- Connections: the kind of premises and purpose, the main, the dates of the connection notice, any pipe-laid notice and the satisfying of conditions, the counter-notice imposing conditions, whether the pipe was already laid; the deposit, rate and dates; the day the sewerage undertaker received the s 106 notice and any refusal.
- Disconnection: the kind of premises and whether it is someone's only or principal home; the day the notice requiring payment was served, the day of payment, any counter-notice and its day, whether a judgment is enforceable or a settlement agreement is in breach; the cut-off day.
- Charges: the days I informed the undertaker and ceased to occupy, the next normal meter reading day, the day a new occupier informed it; the s 62 notice and its expiry; whether a person has a home in the premises and the charges are unmeasured; the findings under s 144A(3); the day measured charging began and the conditions of s 144A(6)-(7); whether I gave notice or consent, and whether occupation changed with no charges yet demanded.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 47(3), "before the end of the period of fourteen days beginning with the day after the service"**: by the service day + 14.
- **s 51(6)**: the relevant day is the day after the latest of the notice, any pipe-laid notice and the satisfying of the conditions.
- **s 51(1)(b), "before the end of the period of fourteen days beginning with the relevant day"**: by the relevant day + 13. **(2), "twenty-one days beginning with the relevant day"**: by the relevant day + 20 (a presumption).
- **s 61(1ZA)(b), "before the end of the period of seven days beginning with the day after he is served"**: payment by the service day + 7 is in time; the cut-off can come from the service day + 8.
- **s 106(4), "within twenty-one days after" receipt**: by the receipt day + 21.
- **s 144(3)(a), (6)(b), (7), "two working days"**: 48 hours disregarding the excluded days. At the level of days: informing is in time if the day of ceasing to occupy is on or after the second working day after the day of informing; the end of "two working days beginning with the service" is the second working day after the day of service.
- **s 144(4)(a), "the twenty-eighth day after he so informs"**: the day of informing + 28.
- **s 144A(5), "before the end of the period of twelve months beginning with the day"**: the day before the corresponding date, or the last day of the month where there is none.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`wia-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
