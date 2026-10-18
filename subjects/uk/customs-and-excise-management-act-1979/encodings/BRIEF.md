# Encoding brief: the Customs and Excise Management Act 1979 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Customs and Excise Management Act 1979** (1979 c. 2), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 29 April 2026, deposited at `../registers/source-bundle/ukpga-1979-2.txt` (Crown copyright, Open Government Licence v3.0).

The conversion drops the paragraph numbers in Schedules 1 and 3. Schedule 3 runs, in order:

- para 1, notice of seizure;
- para 2, service of the notice;
- para 3, notice of claim;
- para 4, contents of the claim;
- para 5, deemed condemnation;
- para 6, condemnation by the court;
- para 7, effect of condemnation.

The text of s 170(3)(a) and Schedule 1 prints "the prescribed sum £20,000" (two versions run together). The encoding takes the fixed sum as an input.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *goods were seized as liable to forfeiture, and someone may be prosecuted for fraudulent evasion. Must the Commissioners give notice of seizure; by when must a claim be made; are the goods deemed condemned or must the Commissioners take proceedings; what are the maximum penalties for an offence under s 170; and by when must proceedings for the offence be commenced?*

1. **Seizure and condemnation** (s 139(6) with Schedule 3 paras 1, 3, 5 and 6):
   - whether notice of seizure must be given (para 1(2) exceptions);
   - the last day for a notice of claim (para 3);
   - whether the thing is deemed condemned (para 5) or the Commissioners must take proceedings (para 6).
2. **Penalties for fraudulent evasion** (ss 170(1)-(4B), 149(1), Schedule 1): whether the offence is made out, and the maximum penalty and imprisonment on summary conviction and on indictment, by kind of goods:
   - ordinary goods;
   - Class A drugs, and Class B or temporary class drugs;
   - Class C drugs;
   - the s 170(4A) weapons;
   - the seal skins prohibition.

   The maximum aggregate term for imprisonment on summary conviction plus default (s 149(1)) is also given.
3. **Time limits** (s 146A(2)-(3)): the last day to commence proceedings for an indictable offence, and for a summary offence.

Left out on purpose: everything else (officers, ports and airports, importation and exportation procedure, warehouses, excise licences, powers of search and arrest, other offences, ss 50 and 68 apart from sharing Schedule 1, Schedules 2 and 4-7).

## Inputs, not worked out

- **The seizure:** the date, who was present, and whether a notice of seizure was served and when.
- **The claim:** the date of any claim, and whether it met para 4.
- **The goods and the offence:** the kind of goods, their value, the knowledge and intent, and the summary fixed sum.
- **Time limits:** the day the offence was committed, and the day sufficient evidence came to the prosecuting authority's knowledge.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Sch 3 para 3, "within one month of the date of the notice of seizure" (or of the seizure)**: on or before the corresponding date one month later, or the last day of that month if it has none.
- **s 146A(2), "the period of 20 years beginning with the day on which the offence was committed"**: ends on the day before the corresponding date.
- **s 146A(3), "the period of 3 years beginning with that day"**: ends on the day before the corresponding date. Within that, the proceedings must be commenced "within 6 months from the date on which sufficient evidence ... came to the knowledge of the prosecuting authority", which is on or before the corresponding date six months later. The last day is the earlier of the two.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`cema-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
