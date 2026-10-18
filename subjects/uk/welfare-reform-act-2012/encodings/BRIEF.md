# Encoding brief: the Welfare Reform Act 2012 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Welfare Reform Act 2012** (2012 c. 5), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 1 July 2026, deposited at `../registers/source-bundle/ukpga-2012-5.txt` (Crown copyright, Open Government Licence v3.0). In this version, the benefit cap annual limits in s 96(5A) are:

- £25,323 or £16,967 for persons resident in Greater London;
- £22,020 or £14,753 for other persons.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for a claimant or couple: are they entitled to universal credit, and how much is the award; is a person entitled to personal independence payment, and to which components and rates; and does the benefit cap reduce their benefits, and by how much?*

1. **Universal credit** (ss 3, 4(1), 5, 8(1)-(3)):
   - entitlement: the basic conditions for each claimant (judged on a given day) and the financial conditions;
   - the award: the maximum amount (the elements in ss 9-12, which are inputs), less the earned and unearned income deductions (inputs), and not below nothing.
2. **Personal independence payment** (ss 77(4), 78(1)-(2), 79(1)-(2), 81(1), 82(2)-(4), 83(1)-(2)):
   - the daily living and mobility components at the standard or enhanced rate, from the assessment findings and the required period condition (previous 3 months and next 9 months, as inputs);
   - the terminal illness rule;
   - no entitlement after the "relevant age", the later of pensionable age and 65.
3. **Benefit cap** (s 96(2), (5), (5A)):
   - the annual limit by residence (Greater London or not) and by which of the two limits applies (an input, set by regulations);
   - the relevant amount for a reference period (annual limit × days ÷ 365, with no rounding);
   - the reduction (the excess of total welfare benefits over the relevant amount).

Left out on purpose:
- claimant responsibilities, requirements and sanctions (ss 13-28);
- the abolition and migration provisions;
- the jobseeker's allowance, employment and support allowance and income support amendments (Part 2);
- the other parts of Part 3;
- the PIP assessment itself (s 80) and claims (ss 84-95);
- the remaining Parts.

## Inputs, not worked out

- **Universal credit:** each claimant's date of birth and their qualifying age for state pension credit (the date it is reached); presence in Great Britain, education, and acceptance of the claimant commitment; capital and the prescribed capital limit; the amounts of the elements and of the deductions; the prescribed minimum award.
- **PIP:** the person's date of birth; the date they reach pensionable age; the assessment findings; whether the required period condition is met; terminal illness and how the claim was made; whether they are entitled to the Scottish payments; the mobility age condition; the day in question.
- **Benefit cap:** residence, which limit applies, the length of the reference period in days, and the total welfare benefits for it.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 4(1)(a), "at least 18 years old"**: from the 18th birthday.
- **s 4(1)(b), "has not reached the qualifying age"**: before that date.
- **s 83(1), "for any period after the person reaches the relevant age"**: no entitlement on any day after the later of the day of pensionable age and the 65th birthday.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`wra-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
