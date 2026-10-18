# Encoding brief: the Renters' Rights Act 2025 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Renters' Rights Act 2025** (2025 c. 26), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 22 June 2026, deposited at `../registers/source-bundle/ukpga-2025-26.txt` (Crown copyright, Open Government Licence v3.0).

Much of the Act inserts sections into other Acts. The text prints the inserted sections, so they are encoded from it:

- s 4A of the Housing Act 1988, inserted by s 1;
- s 4B of that Act, inserted by s 8;
- Sch 1 para 1(1A) to the Tenant Fees Act 2019, inserted by s 9.

The formula in s 4A(6) (a monthly rent from a non-permitted rent period) is lost in the conversion, so that amount is out of scope.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for an assured tenancy in England: does it run as a periodic tenancy, with which rent periods; is a rent payment due in advance, and if so when is it due instead; may rent be taken before the tenancy is entered into; and, for rental bidding and failing to state the rent, may a penalty be imposed, up to how much, and may an additional penalty be imposed?*

1. **Periodic tenancies and rent periods** (HA 1988 s 4A(1)-(5), (8)): whether fixed-term terms are of no effect, whether the rent periods are permitted (28 days or shorter, or monthly), and the substitute monthly periods.
2. **Rent in advance** (HA 1988 s 4B(1)-(7), (12); TFA 2019 Sch 1 para 1(1A)):
   - for one rent period and its due date: whether the term is of no effect;
   - the day the rent is due instead (the substitute rent day);
   - whether a payment before the tenancy is entered into is prohibited.
3. **Rental bidding** (ss 56, 57(1)-(4), (9)):
   - whether s 56(2) or (3) is breached;
   - the maximum penalty (£7,000);
   - whether an additional penalty may be imposed (a previous penalty for the same subsection within the five years ending with the date of the new one, not withdrawn or quashed).

Left out on purpose:
- the changes to grounds for possession and to s 8;
- rent increases (s 13 as amended);
- pets, discrimination, the database, the ombudsman and redress schemes;
- the financial penalty procedure in the Schedules;
- the Welsh and Scottish provisions;
- the s 4A(6) amount;
- everything that only amends.

## Inputs, not worked out

- **The tenancy:** whether it is assured, excepted, entered into before the commencement date, and its dates and rent periods.
- **For a rent period:** its first and last days, its due date under the terms, and any regular rent day within it.
- **For rental bidding:** what was advertised, offered and accepted, and the dates of penalties.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 4B(12), "the initial 28 day period": "the period of 28 days beginning with the first day of the first rent period"**: ends on that day + 27.
- **"Permitted pre-tenancy period"**: from the day the tenancy is entered into to the day before its first day, both included.
- **"Due in advance"**: due before the first day of the rent period.
- **s 57(2), "within the period of five years ending with the date on which that penalty was imposed"**: from the day after the corresponding date five years earlier, up to and including that date.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`rra-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
