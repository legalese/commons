# Encoding brief: the Income Tax Act 2007 (New Zealand), personal income tax, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Income Tax Act 2007**: New Zealand, Public Act 2007 No 97. The source is the version as at 4 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2007_97.txt` (sha256 `c5e7176227b9c086a1558ed3e56f0652b0c411b21357492a5d8802c182a7d93d`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Section and paragraph labels inside sections; every formula; and every table. In particular **Schedule 1, part A, table 1** (the personal income tax brackets) survives only as "How to use this table", so the brackets are an input (the thresholds $15,600, $53,500, $78,100 and $180,000 are quoted elsewhere in the Act, e.g. s RD 17(2) and the ESCT rate threshold rows in schedule 1, and the tests may use the 2026-27 table built from them); the **LC 13-LC 15 formula** for the independent earner tax credit, read as *(person's credit − full year abatement) × credit period months ÷ 12* (LC 13) or *× credit period days ÷ the days in the tax year* (LC 14-LC 15); and **Schedule 1, clause 1's formula**, read as *tax under table 1*.

## Scope: personal income tax of a natural person

The Act runs to about 38,000 lines. This encoding covers only the personal income tax calculation for a natural person:

- **Residence**: s YD 1 (permanent place of abode, the 183-day and 325-day rules, Government service, part days), and s YD 1B's non-resident visitor test (275 days) as it limits YD 1(3).
- **The liability**: ss BC 1-BC 8 (non-filing and filing taxpayers, annual gross income, total deduction, net income and net loss, taxable income, the liability, schedular income, satisfaction by credits and terminal tax).
- **The rate**: Schedule 1, part A, clause 1 (with table 1 as an input), and the flat rates for other persons in clauses 2-7, 15-16 as text.
- **Independent earner tax credit**: ss LC 13-LC 15.
- **Using credits**: ss LA 2-LA 7 (the order of use, terminal tax, and the treatment of remaining credits: refundable credits refunded, non-refundable credits extinguished).
- **Secondary tax codes**: Schedule 2, part A, clauses 3-9 (the flat rates for non-notified, S, SH, ST, SA, SB, CAE/EDW and NSW codes).

Everything else in the Act (income and deduction rules, Parts C-I, PIEs, trusts, companies, FBT, RWT, Working for Families) is out of scope; amounts it determines (assessable income, deductions, tax losses, credits) are inputs.

## The top-level goal, and the goals under it

Top level: *for a natural person and a tax year, are they resident, what is their taxable income and income tax liability, what is their independent earner tax credit, and what terminal tax do they owe or what refund are they due?*

1. **Residence**: YD 1, YD 1B.
2. **Taxable income and liability**: BC 1-BC 7, Schedule 1 cl 1.
3. **Credits, terminal tax and refunds**: BC 8, LA 2-LA 7, LC 13-LC 15.
4. **Secondary tax codes**: Schedule 2, part A, cls 3-9.

Inputs, not worked out: assessable income and deductions (and how they are allocated to years); available tax losses; schedular income and its liability; credits of each kind (PAYE, RWT, imputation, non-refundable); the days present and absent; the Schedule 1 table 1 brackets; benefits, pensions and WFF entitlement for LC 13.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`it-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
