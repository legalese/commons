# Encoding brief: the Immigration Act 2009 (New Zealand), eligibility, unlawful status, work and deportation, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Immigration Act 2009**: New Zealand, Public Act 2009 No 51. The source is the version as at 10 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2009_51.txt` (sha256 `cfae93a719c45de36b16b4979514a0e70dd3c7ed526d69278ad8901822bd31f6`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels, and the **s 179 table** of periods of prohibition on entry after deportation; those periods are not encoded. Work visa criteria themselves are in immigration instructions (s 22), not the Act, and are out of scope.

## Scope

- **Eligibility for a visa**: s 15 (convictions with 5-year and 12-month sentences, prohibition, deportation and exclusion, with the s 15(2) sentence rules applied by the caller and the s 15(3) exceptions), s 16 (the Minister's belief, an input), s 17 (special directions and s 83).
- **Unlawful status and work**: s 9 (when a person is unlawfully in New Zealand, and from when), s 21 (no right to work), s 154 (liability and the 42-day humanitarian appeal), s 185 (reconsideration within 14 days).
- **Deportation liability**: s 157 (temporary visa holders: 14 days to give reasons, 28 days to appeal), s 161 (residence class visa holders convicted of offences within 2, 5 and 10 years of first holding the visa, those periods excluding imprisonment; the 28-day appeal), s 167 (the 10-year period of liability, excluding imprisonment and suspension).
- **Employers**: s 350 (allowing a person to work knowing they are not entitled; knowledge deemed by written notice within 12 months; the notice-period defence).

## The top-level goal, and the goals under it

Top level: *for a person who is not a New Zealand citizen, on a date: are they eligible for a visa, are they unlawfully in New Zealand (and so barred from working), are they liable for deportation under s 161, until when, and by when must any appeal be lodged?*

1. **Eligibility**: ss 15-17.
2. **Unlawful status and work**: ss 9, 21, 154, 185.
3. **Deportation liability**: ss 157, 161, 167.
4. **Employers**: s 350.

Inputs, not worked out: convictions, their dates and sentences (aggregated under ss 15(2) and 161(4)), the maximum penalties, visa grants and expiries, entry permission, time in imprisonment, suspensions, special directions, the Minister's beliefs and determinations, notices and their service dates.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`imm-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
