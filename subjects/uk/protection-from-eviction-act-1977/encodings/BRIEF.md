# Encoding brief: the Protection from Eviction Act 1977 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Protection from Eviction Act 1977** (1977 c. 43), England and Wales. The source is the revised text on legislation.gov.uk, point in time 1 May 2026, deposited at `../registers/source-bundle/ukpga-1977-43.txt` (Crown copyright, Open Government Licence v3.0).

The revised text prints two versions of s 5(1)(b):

- the original, "(b) it is given not less than 4 weeks before the date on which it is to take effect";
- the version substituted by the Renters' Rights Act 2025, "(b) it satisfies subsection (1ZA)", with (1ZA)-(1ZD).

The encoding takes the version as an input (a vintage) and never merges the two.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for this occupier, must the owner go to court to recover possession; is this notice to quit valid and from when can it take effect; and, where the landlord unlawfully evicted or harassed the occupier, may a local housing authority impose a financial penalty, up to how much, and by when must each step in Schedule A1 be taken?*

1. **Eviction only by court proceedings** (ss 2, 3(1), (2A)-(2C), 3A, 8(1), (2), (5)): whether it would be lawful to recover possession otherwise than by proceedings in the court.
2. **Notices to quit** (s 5(1), (1ZA)-(1ZD), (1A)-(1C)): whether a notice to quit (or to end a periodic licence) is valid, and the earliest day on which it can take effect.
3. **Unlawful eviction and harassment, and the financial penalty** (ss 1(1)-(3C), (7), 1A(1)-(3), Schedule A1 paras 1-5, 10):
   - whether an offence under s 1 is made out;
   - whether a penalty may be imposed, and its maximum (£40,000);
   - the last day for the notice of intent, for representations, for payment and for an appeal.

Left out on purpose: penalties on conviction (s 1(4)), agricultural employees (s 4), the requirement for prescribed information in a notice (an input), s 5A, prosecution and service (ss 6, 7), and Schedules 1-3.

## Inputs, not worked out

- Facts about the letting: a tenancy or a licence; whether it is statutorily protected (s 8(1)); the facts behind each exclusion in s 3A; the dates.
- Facts about the conduct, and what the authority or court is satisfied of.
- The day the authority first has sufficient evidence, and the day the conduct last occurred.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule, so do not move any date.

- **"Given not less than 4 weeks before the date on which it is to take effect"**: the date of effect is at least 28 days after the day of giving.
- **"Not less than two months before"**: the date of effect is on or after the corresponding date two months after the day of giving, or the last day of that month if it has none.
- **"The period of 6 months beginning with" day X**: ends on the day before the corresponding date six months later, or the last day of that month if it has none.
- **"The period of 28 days beginning with the day after" day X**: ends on X + 28.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`pea-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
