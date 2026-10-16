# Encoding brief: the New Zealand Superannuation and Retirement Income Act 2001 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**New Zealand Superannuation and Retirement Income Act 2001**: New Zealand, Public Act 2001 No 84. The source is the version as at 10 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2001_84.txt` (sha256 `73080046cb9edf816753667acb6f8ffda590805f9770197f4e707ee539465cd9`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels; **every table and formula**:
- **the s 8(4) table** of total time requirements by date of birth (only its heading and the example survive). The requirement is an input.
- **the Schedule 1 rates** (only the row labels survive). Rates are adjusted every 1 April by Order in Council (s 15), so they are inputs in any case.
- **the s 32(1)(b) formula** for people in a specified Pacific country with 10 to 19 years' residence. Its items are "the base rate" and "the whole number of years the person has resided in New Zealand since turning 20"; it is read as *base rate × years ÷ 20*.
- **the s 43 formula** for the required annual capital contribution to the Fund. Its items are the contribution percentage, projected GDP and the expected net cost; it is read as *percentage × GDP − net cost*.

What the Act covers:
- **Part 1, ss 7-35A**: entitlement to New Zealand superannuation: age (s 7), residence (ss 8-10A), commencement (s 11), rates (s 12, Schedule 1), living alone (s 4A), annual adjustment (ss 15-16), long-term care and hospital (ss 17-19), absence and payment overseas (ss 21-35).
- **Part 2, ss 36-71**: the New Zealand Superannuation Fund and its Guardians: capital contributions and withdrawals (ss 42-47), governance, investment, reporting and reviews.
- **Part 3, ss 72-79A**: political commitment, transitional provisions.
- **Part 4, ss 80 on**: the Retirement Commissioner.
- **Schedules**: transitional provisions (Schedule 1AA), rates, specified Pacific countries, and others.

## The top-level goal, and the goals under it

Top level: *for this person, are they entitled to New Zealand superannuation, from when, at which rate, and how much is payable while they are overseas or in hospital?*

1. **Entitlement**: ss 4A, 7-12, 17-19.
2. **Absence and payment overseas**: ss 21-35.
3. **The Fund and the rates**: ss 15-16, 43-47, 71.

Inputs, not worked out:
- the total time requirement (the lost s 8(4) table), the periods resident and present since 20 and since 50, and periods treated as residence (ss 9-10A, which the chief executive decides);
- the rates in force (Schedule 1 as adjusted);
- relationship status, accommodation, hospital stays and long-term care, absences, intentions and the chief executive's decisions;
- GDP, net cost and contribution percentages for the Fund.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`nzs-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
