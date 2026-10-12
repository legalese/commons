# Encoding brief: the Accident Compensation Act 2001 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Accident Compensation Act 2001**: New Zealand, Public Act 2001 No 49. The source is version 249 as at 10 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

What the Act covers:
- **Part 1**: definitions, including earnings, New Zealand and ordinary residence.
- **Part 2**: cover — accident, personal injury, mental injury, treatment injury, work-related, motor vehicle and gradual process injury, and dates of injury.
- **Part 3**: the Code of ACC Claimants' Rights and claims.
- **Part 4**: entitlements and disentitlements.
- **Part 5**: reviews and appeals.
- **Part 6**: the Accounts and levies.
- **Part 7**: the Corporation.
- **Part 8**: injury information.
- **Part 9**: miscellaneous provisions, offences and proceedings.
- **Parts 10 and 11**: transitional provisions.
- **Schedules**: Schedule 1 sets out the entitlements (rehabilitation, weekly compensation, lump sums and fatal injuries); Schedules 2, 3 and 3A list occupational diseases, offences and birth injuries; Schedules 4–8 deal with levy deductions and the Corporation.

The source is `../source/ACC2001.txt`, text extracted from the PCO's PDF; `../source/PROVENANCE.md` records it. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

## The top-level goal, and the goals under it

Top level: *for this injury, does the person have cover; what kind of injury is it and which Account pays; and what weekly compensation is payable after the first five weeks?*

1. **Cover and classification**: Part 2, s 17, and the Accounts.
2. **Claims and decisions**: Part 3.
3. **Entitlements**: Part 4 and Schedule 1.
4. **Reviews and appeals**: Part 5.
5. **Levies and the Scheme**: Part 6.
6. **Offences and proceedings**: Part 9.

Inputs:
- the Corporation's, the Minister's and the courts' discretions and findings;
- regulations, including lump sum amounts and levy rates;
- indexed amounts;
- minimum weekly earnings;
- the classification of facts under Schedules 2, 3 and 3A.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`acc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
