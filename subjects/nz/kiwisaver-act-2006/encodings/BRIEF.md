# Encoding brief: the KiwiSaver Act 2006 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**KiwiSaver Act 2006**: New Zealand, Public Act 2006 No 40. The source is the version as at 1 April 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2006_40.txt` (sha256 `b90bc375094c4fdbb56cade04a1b46871c4ed774a19d63b6ab8b65c4aea53781`), converted from the PCO's XML on 2026-10-13 (`act_public_2006_40.meta.json` beside it). There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** The paragraph labels ((a), (b), (i) …) are not in the text; a provision's place in its list gives its label. **The formulas** in ss 86, 87, 101D, 101T and the like have lost their symbols; only the definitions of their items survive. The compulsory employer contribution formula (s 101D(1)) is read as *payment of gross salary or wages × CEC rate − other contributions − hybrid schemes amount*, the items in the order the section defines them, and the result as "a positive amount" (never below 0).

What the Act covers:
- **Part 1, ss 1-8**: purpose, interpretation, who the Act applies to (s 6).
- **Part 2, ss 9-59D**: becoming a member: automatic enrolment on new employment (ss 10-15), opting out (ss 16-21), notices, opting in (ss 33-39), information packs, allocation to a scheme (ss 44-53), transfers (ss 54-59), and back-dated validation (ss 59A-59D).
- **Part 3, ss 60-114**: contributions: deductions from salary or wages and the contribution rate (ss 60-71), the holding account and interest (ss 72-91B), other contributions (ss 92-101AA), compulsory employer contributions (ss 101A-101K), rate reductions (ss 101L-101T), savings suspensions (ss 102-114).
- **Part 4, ss 115-220**: governance of schemes, default schemes, complying superannuation funds, exempt employers.
- **Part 5, ss 221-235**: general provisions.
- **Schedule 1, the KiwiSaver scheme rules**: fees, minimum contributions, the withdrawal age, first-home, death, hardship, serious illness, congenital condition and emigration withdrawals, suspensions, transfers, Crown contributions.

## The top-level goal, and the goals under it

Top level: *for this person and this employment, does automatic enrolment apply and until when may they opt out; what must be deducted from each pay and what must the employer contribute; and how much may they withdraw for the purpose they give?*

1. **Membership**: Part 2.
2. **Contributions**: Part 3.
3. **Withdrawals**: Schedule 1.

Inputs, not worked out:
- the person's residence, citizenship, age and the New Zealand superannuation qualification age (set by another Act);
- whether employment is new, temporary or with the same business; whether the employer is exempt;
- the gross salary or wages of each payment, the member's accumulation and its parts (Crown contributions, amounts from Australian schemes);
- whether a person is in financial hardship, seriously ill, has emigrated, or has held an estate in land, as decided by the manager or supervisor.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`ks-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
