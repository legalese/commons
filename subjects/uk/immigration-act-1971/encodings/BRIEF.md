# Encoding brief: the Immigration Act 1971 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Immigration Act 1971** (1971 c. 77), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 5 January 2026, deposited at `../registers/source-bundle/ukpga-1971-77.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for a person: do they have the right of abode, and do they need leave to enter or remain; if they applied to extend limited leave, is that leave still extended on a given day under s 3C; and for an immigration offence under s 24 or s 24B, is it committed, what is the maximum imprisonment, and by when may summary proceedings be brought under s 28?*

1. **Right of abode and the need for leave** (ss 1(1)-(3), 2(1), 3(1), 3ZA):
   - the right of abode: a British citizen, or a Commonwealth citizen with it before 1983 who has remained one;
   - the need for leave: none for a person with the right of abode, for an Irish citizen not within s 3ZA(2)-(4), or on a local journey within the common travel area, except an Irish citizen within s 3ZA(2)-(4).
2. **Continuation of leave** (s 3C(1)-(3)): whether limited leave is extended on a given day. It is extended where the application was made before the leave expired, while the application is undecided, while an in-country appeal or administrative review could be brought or is pending, and so long as the applicant has not left the United Kingdom.
3. **Offences** (ss 24(A1)-(F1), (G1), (1)(b)-(c), (1A), (3), 24B(1)-(4), 28(1)(a), (1A)(a)):
   - which offence is committed;
   - the maximum imprisonment on indictment and on summary conviction, by jurisdiction;
   - the last day for summary proceedings in England and Wales on the extended time limits.

Left out on purpose:
- leave and its conditions (ss 3-3B, 3D-4);
- deportation (ss 5-7);
- exemptions (ss 8-8B);
- the common travel area beyond s 1(3) (ss 9-11D);
- appeals (ss 12-23);
- facilitation and other offences (ss 25-27);
- powers of arrest and search (ss 28A-28Q);
- Parts IV-V and the Schedules.

## Inputs, not worked out

- **The person's status:** British citizen, Commonwealth citizen with the pre-1983 right, Irish citizen, and the s 3ZA(2)-(4) facts.
- **For s 3C:** the dates of expiry and of the application, the decision, the end of appeal or review rights, and departure.
- **For offences:** the facts (knowledge, entry, overstaying), the date of the offence, the evidence date certified under s 28(1)(a), the first arrest date for s 28(1A), and the general limit in a magistrates' court (England and Wales).

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 3C(1)(b), "made before the leave expires"**: the application date is on or before the last day of the leave.
- **s 3C(2)**: the leave is extended on a day after expiry while the application is undecided, or while an appeal or review could be brought or is pending (the last day of those rights is an input). It lapses from the day the applicant leaves.
- **s 28(1)(a), "within six months after the commission"**: on or before the corresponding date six months later. "Within three years after ... and not more than two months after the date certified": on or before both the corresponding date three years later and the corresponding date two months after the certified date. The last day is the later of the two routes.
- **s 28(1A)(a), "within the period of six months beginning with the date of the commission", or "three months beginning with the date when the person is first arrested ... if that period expires after the end of" the first**: the last day of whichever period ends later.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ia71-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
