# Encoding brief: the Consumer Rights Act 2015 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Consumer Rights Act 2015** (2015 c. 15), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 6 April 2026, deposited at `../registers/source-bundle/ukpga-2015-15.txt` (Crown copyright, Open Government Licence v3.0). The conversion prints some sections twice (ss 19-24); the copies are identical.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a consumer bought goods (or services) that do not conform to the contract. Until when can they use the short-term right to reject; is the goods' non-conformity presumed to have existed at delivery; may they now use the final right to reject or a price reduction, and how much refund is due and by when; and for services, may they require repeat performance or a price reduction?*

1. **Short-term right to reject** (s 22(1)-(8)):
   - the last day to exercise it: 30 days beginning with the first day after transfer, delivery and (if any) the installation notice;
   - a shorter period for perishable goods;
   - the extension for a repair or replacement waiting period, and the 7-day rule where the repaired or replacement goods still do not conform.
2. **Tier-two remedies for goods** (ss 19(14)-(15), 20(15), 24(5), (8)-(11)):
   - the six-month presumption of non-conformity at delivery;
   - whether the final right to reject or a price reduction is available (s 24(5));
   - the refund on final rejection, with any deduction for use (none in the first 6 months unless a motor vehicle);
   - the last day for the refund.
3. **Services** (ss 54(3), 55(3), 56(3)-(4)): whether repeat performance can be required, whether a price reduction is available, and the last day for the refund.

Left out on purpose:
- the statutory terms themselves (ss 9-18, 49-53, which are inputs: whether the goods or service conform);
- digital content (Chapter 3);
- delivery and risk (ss 28-29);
- the hire, hire-purchase and severable-contract variants;
- partial rejection (s 21);
- unfair terms (Part 2);
- Parts 3-4 and the Schedules.

## Inputs, not worked out

- **Dates:** when ownership or possession passed, delivery, the installation notice, the request for and receipt of a repair or replacement, the day the fault appeared, when the final right was exercised, and when the trader agreed to refund.
- **Facts and amounts:** perishability, whether the goods are a motor vehicle, the price, and the deduction for use the trader claims.
- **Services:** whether the service conformed, whether completing it is impossible, and whether the trader failed to perform again within a reasonable time.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 22(3), "the end of 30 days beginning with the first day after these have all happened"**: the last of the events is day E; the period runs from E + 1 to E + 30.
- **s 22(6), (8): the waiting period "begins with the day the consumer requests ... and ends with the day on which the consumer receives" the goods**: its length counts both days. The 30 days stop running for that length, so the end moves later by that many days.
- **s 22(7)(a), "7 days after the waiting period ends"**: the day the goods are received + 7.
- **s 24(11), "6 months beginning with the first day after these have all happened"**: from E + 1 to the day before the corresponding date six months later.
- **s 19(14), "within the period of six months beginning with the day on which the goods were delivered"**: on or before the day before the corresponding date.
- **ss 20(15), 56(4), "within 14 days beginning with the day on which the trader agrees"**: by that day + 13.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`cra-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
