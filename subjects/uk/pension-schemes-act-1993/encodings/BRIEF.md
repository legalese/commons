# Encoding brief: the Pension Schemes Act 1993 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Pension Schemes Act 1993** (1993 c. 48), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 31 July 2026, deposited at `../registers/source-bundle/ukpga-1993-48.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a member of an occupational pension scheme leaves pensionable service before normal pension age. Are they entitled to preserved short service benefit, payable from what age at the latest; or, if not, to a cash transfer sum or contribution refund, and how much is the refund; and if they ask to transfer their cash equivalent, by when must they apply and by when must the trustees carry it out?*

1. **Early leavers** (ss 71(1), (3), (7), (10)-(11), 101AA(1)-(2), 101AB(1), (4)):
   - short service benefit: at least 2 years' qualifying service; or 30 days if all of it would be money purchase benefit and no relevant service began before s 36 of the Pensions Act 2014 came into force; or a transfer in from a personal pension;
   - otherwise, with at least three months' pensionable service, a cash transfer sum or contribution refund;
   - the refund amount (s 101AB(4));
   - the latest age from which short service benefit must be payable (s 71(3)).
2. **Cash equivalent transfers** (ss 93A(4), 94, 95(1A), 98(1), 99(2), (3), (7)):
   - the last day to apply after a statement of entitlement;
   - whether the right is lost;
   - the trustees' deadline (6 months from the guarantee date or the application date, extended where forfeiture proceedings run);
   - whether they must notify the Regulator.

Left out on purpose:
- contracting out and guaranteed minimum pensions (Part III);
- revaluation and the computation of short service benefit (ss 74, 83-86);
- the calculation of cash equivalents (s 97);
- the transfer destinations (s 95(2)-(6));
- Part 4ZA (the GMP conversion);
- the Pensions Ombudsman;
- everything else.

## Inputs, not worked out

- **The member:** the start and end of their latest pensionable service, and the days of earlier service that count; whether all benefit would be money purchase; whether any relevant service began before s 36 PA 2014 commenced; a transfer-in from a personal pension; their normal pension age, and the date they reach it.
- **The refund:** employee contributions, and contributions relating to a transfer payment, with the transfer payment.
- **The transfer:** the guarantee date, whether the benefits are money purchase or flexible, the application date, any forfeiture proceedings and their conclusion, and the date the transfer was carried out.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Qualifying service of "2 years", "30 days" and "three months"**: the earlier counting days are added before the start of the latest period. A duration of N months is met if its last day is on or after the last day of the N months beginning with that adjusted start; 30 days is met at the adjusted start + 29.
- **s 95(1A)(a), "within the period of 3 months beginning with the guarantee date"**: on or before the day before the corresponding date. (b): "no later than the date that falls one year before the member attains normal pension age", the corresponding date one year earlier.
- **s 99(2), "within 6 months beginning with"**: on or before the day before the corresponding date. (3): "before the end of the period of 3 months after the conclusion" of proceedings, which ends on the corresponding date three months later.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`psa93-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
