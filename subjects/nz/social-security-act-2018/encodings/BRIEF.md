# Encoding brief: the Social Security Act 2018 (New Zealand), main benefits, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Social Security Act 2018**: New Zealand, Public Act 2018 No 32. The source is the version as at 26 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2018_32.txt` (sha256 `58fe6d53a9a66d001bf593fe6ea0424e6bf3d64a59a9648df2f624dd6a88acc6`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels and most of the tables in **Schedule 4**. The Part 1 (jobseeker support) and Part 3 (supported living payment) rate tables are lost, together with the income test each rate is subject to, so for those benefits **the weekly base rate and its income test are inputs**. Part 2 (sole parent support: "$521.52 a week, subject to Income Test 1") survives. The definitions of **Income Tests 1-4** in Schedule 2 survive and are encoded. The **stand-down period** is set by regulations under s 440 and is an input.

## Scope: the three main benefits for adults

- **General**: s 16 (residential requirement), s 17 (rates), s 18 (no more than one main benefit), s 19 (unlawful presence and temporary visas).
- **Jobseeker support**: ss 20-24 (work gap, available for work, age, no or minimum income) and s 26 (ineligibility).
- **Sole parent support**: ss 29-30 (requirements, the sole parent requirement), s 32 (split care), s 33 (expiry when the youngest child turns 14).
- **Supported living payment**: ss 34-36 (restricted work capacity or total blindness: 15 hours a week) and s 40 (carers).
- **Rates**: Schedule 4 Part 2 cl 1 and the Income Tests in Schedule 2.
- **Commencement**: s 316 (the stand-down period and when the benefit starts).

Out of scope: youth and young parent payments, emergency benefits, supplementary assistance (accommodation supplement, etc.), obligations and sanctions, debt, reviews and appeals, and everything outside Part 2 except s 316.

## The top-level goal, and the goals under it

Top level: *for a person applying for a main benefit: are they entitled, at what weekly rate after the income test, and on what day does the benefit commence?*

1. **General requirements**: ss 16, 18, 19.
2. **Entitlement**: ss 20-24, 26, 29-30, 32-36, 40.
3. **Rate and commencement**: s 17, Schedule 4 Part 2, the Income Tests, s 316.

Inputs, not worked out: citizenship or visa, residence periods, whether MSD is satisfied of matters it must judge (availability for work, restricted capacity, the need for full-time care), the person's and partner's weekly income, the base rates and income tests lost from Schedule 4, and the stand-down period.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`ss-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
