# Encoding brief: the Holidays Act 2003 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Holidays Act 2003**: New Zealand, Public Act 2003 No 129. The source is the version as at 20 December 2023, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2003_129.txt` (sha256 `45dffd4b6d07021220d7a66622da1252481f4e211b13f6fbd45cb70d12c31fa5`). It was converted from the PCO's XML on 2026-10-13 (`act_public_2003_129.meta.json` beside it). There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** The paragraph labels ((a), (b), (i) …) are not in the text; a provision's place in the list gives its label. The two formulas, in s 8(2) and s 9A(2), have lost their symbols: only the definitions of the variables survive. As enacted they are `(a − b) ÷ c` (s 8(2)) and `a ÷ b` (s 9A(2)), and the variables are defined in that order.

What the Act covers:
- **Part 1, ss 1-14**: commencement, purpose, interpretation; the Act is a minimum (s 6); the pay measures: ordinary weekly pay (s 8), relevant daily pay (s 9), average daily pay (s 9A), board and lodgings (s 10), gross earnings (s 14); whether a day would otherwise be a working day (ss 12, 13).
- **Part 2 subpart 1, ss 15-40**: annual holidays. Entitlement after each 12 months of continuous employment (s 16), taking them (ss 17-20), holiday pay (ss 21-26), when it is paid (ss 27, 28), cashing up to 1 week (ss 28A-28F), closedowns (ss 29-35), and their relation to other leave and to public holidays (ss 36-40).
- **Subpart 3, ss 43-61A**: public holidays. The days (s 44), transfers (ss 44A-44C), Mondayisation (ss 45, 45A), pay for not working and for working (ss 46-55), alternative holidays (ss 56-61), sickness on a public holiday (s 61A).
- **Subpart 4, ss 62-72**: sick leave and bereavement leave.
- **Subpart 5, ss 72A-72J**: family violence leave.
- **Part 3, ss 73-91**: good faith, who may enforce, penalties and their time limits, arrears, recovery from a person involved, the holiday and leave record, interest, re-employment within 1 month, and the transitional provisions. Schedule 1AA: the 2016, 2018 and 2021 amendments.

## The top-level goal, and the goals under it

Top level: *for this holiday or leave event (an annual holiday, the end of the employment, a public holiday, an alternative holiday, a day of sick, bereavement or family violence leave, a closedown, or a cash-up), is the employee entitled, how much must the employer pay, when, and does the employee earn an alternative holiday?*

1. **The pay measures**: ss 8-11, 14.
2. **Annual holidays**: ss 16-40.
3. **Public holidays and alternative holidays**: ss 44-61A.
4. **Sick leave and bereavement leave**: ss 63-72.
5. **Family violence leave**: ss 72A-72J.
6. **Enforcement and records**: ss 73-86, Schedule 1AA.

Inputs, not worked out:
- who is an employee (ERA s 6) and who is "involved" (ERA s 142W);
- whether a day would otherwise be a working day (s 12), except where the calendar computes it from the weekdays the employee usually works;
- the pay the employee would have received on a day, and the gross earnings over a period, as amounts already summed by kind;
- the date of Matariki Observance Day (it is set by Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022, not by this Act) and of the local anniversary day;
- determinations by a Labour Inspector, agreements between employer and employee, and whether an employer's reason is genuine.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`ha-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
