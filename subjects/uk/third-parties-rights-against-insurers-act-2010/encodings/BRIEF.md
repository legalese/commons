# Encoding brief: the Third Parties (Rights against Insurers) Act 2010 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Third Parties (Rights against Insurers) Act 2010** (2010 c. 10), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 4 January 2024, deposited at `../registers/source-bundle/ukpga-2010-10.txt` (Crown copyright, Open Government Licence v3.0). The conversion drops the paragraph numbers in the Schedules. Schedule 1 is:

- para 1, notices requesting information;
- para 2, provision of information;
- para 3, notices requiring disclosure (dissolved bodies);
- para 4, disclosure and inspection;
- para 5, avoidance;
- para 6, other rights;
- para 7, interpretation.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *someone (the third party) is owed a liability by an insured who is insolvent, has died insolvent, or has been dissolved. Have the insured's rights against its insurer been transferred to the third party; can the third party enforce them yet; how much can it recover from the insurer, and how much of the liability can it still enforce against the insured; which policy conditions bind it; and by when must information or a list of documents be provided?*

1. **Transfer of rights** (ss 1(1)-(2), (5), 4-7, 15, 16, Sch 3 paras 1 and 3): whether the rights transfer, given which relevant-person event it is, which route in s 1(1) applies, and the limits in ss 4(4), 5(1), 6(5)-(6), 6A(2)-(3) and 15. The 1930 Act case in Sch 3 para 3 is an input flag.
2. **What the third party can recover and enforce** (ss 1(3)-(4), 8, 9, 10, 14(1), (6)-(7)):
   - whether it may enforce yet (the liability is established);
   - the amount transferred (s 8), less set-off (s 10);
   - the amount it can still enforce against the insured (s 14);
   - whether a condition requiring information or assistance, or prior discharge by the insured, binds it (s 9(3)-(6)).
3. **Information and disclosure** (Sch 1 paras 1-4):
   - whether a notice may be given;
   - the last day to provide information (para 2), or to serve a list of documents (para 4(3)), each within "the period of 28 days beginning with the day of receipt".

Left out on purpose:
- the procedure for declarations (ss 2-3);
- limitation (s 12, which concerns defences in proceedings);
- jurisdiction (s 13);
- s 14(2)-(3) (arrangements);
- avoidance clauses (s 17, Sch 1 para 5);
- foreign elements (s 18);
- the power to make regulations (s 19);
- Schs 2 and 4.

## Inputs, not worked out

- **The relevant-person event:** its kind, and the day it took effect.
- **The liability:** the day it was incurred, and its amount.
- **The insurer:** its liability to the insured under the contract, the amount it may set off, and any shortfall from the insurer's own insolvency or a fund limit, with any FSCS claim and payment.
- **The facts for s 9.**
- **For Sch 1:** the reasonable beliefs, and the day a notice was received.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"The period of 28 days beginning with the day of receipt"**: ends on receipt + 27.
- **Section 1(1)(a) and (b):** on the same day, a relevant person incurring a liability is route (a), because the person "becomes" relevant no later than the liability.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`tprai-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
