# Encoding brief: the Nationality and Borders Act 2022 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Nationality and Borders Act 2022** (2022 c. 36), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 20 March 2026, deposited at `../registers/source-bundle/ukpga-2022-36.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Much of the Act amends other Acts. Its own operative rules for a person are in Part 2: the Refugee Convention tests and the priority removal notice regime. Top level: *for an asylum seeker, is the person a refugee under Article 1(A)(2) as the Act requires it to be decided (ss 30-35); could they claim Article 31(1) immunity from penalties for illegal entry (s 37); and, if a priority removal notice or evidence notice was served, was material provided late, until when is the notice in force, and must the decision-maker treat the lateness as damaging credibility and give the evidence minimal weight?*

1. **Refugee status** (ss 30(1), (5), 31(1)-(2), 32, 33(2)-(4), 34, 35(1)): the decision-maker's two-stage approach to a well-founded fear:
   - stage one, on the balance of probabilities: the characteristic and the fear;
   - stage two, on a reasonable likelihood: persecution and the lack of protection, with internal relocation considered;
   - the actors of persecution, the Convention reasons, the two-condition test for a particular social group, and protection.

   Each finding of fact is an input. The encoding applies the structure.
2. **Article 31(1) immunity** (s 37(1)-(4)): whether the refugee came "directly" and "presented themselves without delay", as the Act defines them, and whether the penalty relates to an attempt to leave.
3. **Priority removal notices and late evidence** (ss 20(3)(b), (5)-(7), 21(1), (3), 22(1)-(4), (7), 26(1)-(5)):
   - whether material was provided late (on or after the cut-off date);
   - the last day the notice is in force;
   - whether lateness must be taken as damaging credibility and the evidence given minimal weight, unless there are good reasons.

Left out on purpose:
- nationality (Part 1);
- accommodation, inadmissibility and designated places (ss 12-17);
- appeals and legal aid (ss 23-25, 27-29);
- s 36 (Art 1(F)) and s 38 (which amends s 72 of the 2002 Act);
- offences and maritime enforcement (Part 3);
- removals, age assessment, slavery and trafficking (Parts 4-5);
- visa penalties, ETAs and carriers (Part 6);
- the tribunal provisions and the general provisions.

## Inputs, not worked out

- **Refugee status:** every finding of fact (characteristic, fear, likelihood, who the actor is, the protection available, internal relocation), and the date the claim was made and the date s 30 came into force.
- **Article 31:** the travel and claim facts.
- **Notices:** the dates (service, cut-off, provision of material, appeal rights exhausted) and whether there were good reasons.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"On or after the PRN cut-off date"**: provided on the cut-off date itself is late.
- **s 21(1), "until the end of the period of 12 months beginning with" the later of the cut-off date and the day appeal rights are exhausted**: the day before the corresponding date 12 months later, or the last day of that month if it has none.
- **s 30(5), "made on or after the day on which this section comes into force"**: the in-force date is an input.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`nba-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
