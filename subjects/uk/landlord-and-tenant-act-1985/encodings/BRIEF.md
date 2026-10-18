# Encoding brief: the Landlord and Tenant Act 1985 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Landlord and Tenant Act 1985** (1985 c. 70), England and Wales. The source is the revised text on legislation.gov.uk, point in time 29 June 2026, deposited at `../registers/source-bundle/ukpga-1985-70.txt` (Crown copyright, Open Government Licence v3.0). Section 20ZA prints each line twice (two extent versions); they are identical.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for a residential lease, does the landlord's implied repairing covenant (s 11) apply, and the covenant of fitness for human habitation (s 9A, England), and from when; how much of a service charge demand is payable after ss 19, 20 and 20B, and may it be withheld under s 21B; and when must the landlord's identity, or a new landlord's notice of assignment, be given?*

1. **Repair and fitness** (ss 9A(1), 9B, 11(1), 13, 14):
   - whether s 11 applies to the lease (term under seven years, the s 13(2) rules, the extensions in s 13(1A)-(1AA), the exclusions in ss 13(1ZA), (1ZC) and 14);
   - whether s 9A applies, and the first day its covenant bites (s 9B(3)-(6), with the 12-month deferral for existing periodic and secure tenancies).
2. **Service charges** (ss 18, 19(1), 20(1), (3), (6)-(7), 20B, 21B):
   - for each item of relevant costs: the amount reasonably incurred (s 19, an input);
   - the 18-month rule in s 20B;
   - for qualifying works, the consultation cap in s 20 (the appropriate amount is an input);
   - the total payable, and whether it may be withheld for want of the s 21B summary.
3. **Information about the landlord** (ss 1(1), 3(1), (3A)-(3B), 22(2), (4)):
   - the last day to supply the landlord's name and address;
   - the last day for a new landlord's notice of assignment;
   - the end of the old landlord's continuing liability;
   - the window for requesting inspection of supporting accounts, and the latest start of the facilities.

Left out on purpose: rent books (ss 4-7), fitness in Wales (s 8-10), social housing hazards (ss 10A-10B), specific performance (s 17), s 20A grant deductions, s 20C, the building safety provisions (ss 20D-20F, 30C-30I), ss 20J-20K, service charge information regulations (s 21, 21A), insurance (s 30A and the Schedule), tenants' associations, and supplementary provisions.

## Inputs, not worked out

- **The lease:** its dates, its term, and the facts behind each exclusion.
- **Fitness:** the commencement date of the Homes (Fitness for Human Habitation) Act 2018 (s 9B(9)).
- **Each cost:** its amount, the reasonable part, and the dates it was incurred and notified.
- **Qualifying works:** the appropriate amount, and whether the consultation requirements were complied with or dispensed with.
- **Dates:** when a request was received, of an assignment and the next rent day, and of notices.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"The period of N days/months beginning with" day X**: N days end on X + N − 1. N months end on the day before the corresponding date N months later, or on the last day of that month if it has none.
- **s 20B(1), "incurred more than 18 months before a demand"**: the demand day is after the last day of the 18 months beginning with the day the costs were incurred.
- **s 3(1), "within two months of the assignment"**: a rent day on or before the corresponding date two months after the assignment.
- **s 22(2), "within six months of obtaining the summary"**: on or before the corresponding date six months later.
- **s 22(4), "beginning not later than one month after the request"**: on or before the corresponding date one month later.
- **A term "of less than seven years"**: the term, from the grant, ends before the last day of the seven years beginning with the grant.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`lta-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
