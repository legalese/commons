# Encoding brief: the Residential Tenancies Act 1986 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Residential Tenancies Act 1986**: New Zealand, Public Act 1986 No 120. The source is the version as at 1 December 2025, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_1986_120.txt` (sha256 `8c351db65ccf0c71165c5e410af626779784dceaeacbd50371983814b6c81d97`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels; **Schedule 1A** (the maximum amounts of exemplary damages for each unlawful act) and **Schedule 1B** (the fines and infringement fees) — only their headings survive, so those amounts are inputs; and **the s 56B(5) formula** for the rent after a tenant withdraws for family violence, read as *rent × remaining tenants ÷ tenants before the withdrawal*.

What the Act covers (384 sections):
- **ss 1-11**: interpretation (including its own definition of **working day**), application and exclusions (s 5), short fixed terms (s 7), no contracting out (s 11).
- **Part 2, ss 12-66**: tenancy agreements: discrimination, writing and contents, key money and letting fees, **bonds** (ss 18-22F), **rent** (in advance, increases, market rent), records, rights and obligations of both parties (repairs, entry, quiet enjoyment, pets, minor changes, assignment, damage), and **termination** (notice periods, Tribunal orders, fixed terms becoming periodic, abandonment, goods left behind, possession orders).
- **Part 2A, ss 66A-66X**: boarding house tenancies.
- **Part 3, ss 67-124**: the Tenancy Tribunal: jurisdiction ($100,000), orders, mediation, hearings, enforcement, unlawful acts and exemplary damages (s 109).
- **Parts 4-5 and Schedules**: administration, the Residential Tenancies Fund, regulations, infringement offences, transitional provisions.

## The top-level goal, and the goals under it

Top level: *for this tenancy step (a notice to terminate, a rent increase, a bond, a demand for rent in advance, an entry, or an application about an unlawful act), is it lawful, and on what date does it take effect or must it be made by?*

1. **Application of the Act and working days**: ss 2, 5, 7.
2. **Bonds and rent**: ss 17-30, 49B, 56B.
3. **Termination**: ss 50-66.
4. **Entry, boarding houses**: ss 48, 66D, 66R-66X.
5. **The Tribunal**: ss 54, 77, 108, 109.

Inputs, not worked out:
- the facts behind each exclusion in s 5, and whether a ground for a shorter notice exists;
- Matariki Observance Day and the local anniversary day (for working days);
- rent, bonds, insurance excesses, market rent;
- the Schedule 1A and 1B amounts.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`rta-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
