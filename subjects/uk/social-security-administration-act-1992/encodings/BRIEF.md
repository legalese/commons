# Encoding brief: the Social Security Administration Act 1992 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Social Security Administration Act 1992** (1992 c. 5), Great Britain. The source is the revised text on legislation.gov.uk, point in time 8 July 2026, deposited at `../registers/source-bundle/ukpga-1992-5.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a benefit overpayment has been made. Is it recoverable from the person under s 71, and how much; is an offence committed under s 111A (dishonest) or s 112 (false representation or failure to notify), and with what maximum sentence; and if a penalty is offered as an alternative to prosecution under s 115A, how much is it, and by when can the person withdraw their agreement?*

1. **Recoverable overpayments** (s 71(1), (3), (5A)):
   - it is recoverable if a person misrepresented or failed to disclose a material fact, whether fraudulently or not, and in consequence a payment was made;
   - recovery needs the awarding decision to have been revised, superseded or reversed on appeal (s 71(5A));
   - the amount is what would not have been paid but for it;
   - it is recoverable from the person who misrepresented or failed to disclose.
2. **Offences** (ss 111A(1)-(1B), (3)-(4), 112(1)-(1B), (2)):
   - s 111A: dishonestly making a false statement or providing false information, or dishonestly failing to notify a change of circumstances promptly (in Scotland, "knowingly");
   - s 112: knowingly making a false statement, or failing to notify a change (no dishonesty needed);
   - the maximum imprisonment: s 111A, six months summary and seven years on indictment; s 112, three months summary only.
3. **Penalty as an alternative to prosecution** (s 115A(1), (1A), (2)-(3A), (5)):
   - whether a penalty notice may be given;
   - the amount: 50% of the overpayment, rounded down to the nearest penny, at least £350 and at most £5,000; or £350 where no overpayment was made (s 115A(1A));
   - the last day to withdraw agreement (the 14 days beginning with the day of agreement).

Left out on purpose:
- claims and payments;
- work-focused interviews;
- decisions and appeals (mostly repealed);
- s 71ZB and the other recovery routes (beyond s 71);
- housing benefit;
- s 115B employers;
- other offences;
- the rest.

## Inputs, not worked out

- **The overpayment:** the facts of the misrepresentation or failure to disclose, whether the payment was made in consequence, whether the decision was revised, superseded or reversed, and the amount overpaid.
- **The offence:** the facts (dishonest or knowing, a false statement or a failure to notify, whether the change was excluded by regulations, promptness) and the jurisdiction (Scotland or not).
- **The penalty:** whether there are grounds for prosecution, whether the overpayment was attributable to the person's act or omission, and the day of agreement.

## Dates and amounts, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 115A(3): "rounded down to the nearest whole penny"**: the floor of 50% of the overpayment to two decimal places.
- **s 115A(5): "the period of 14 days beginning with the day on which he agrees"**: ends on that day + 13.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ssaa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
