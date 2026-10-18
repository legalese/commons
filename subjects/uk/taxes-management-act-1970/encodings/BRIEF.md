# Encoding brief: the Taxes Management Act 1970 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Taxes Management Act 1970** (1970 c. 9), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 25 June 2026, deposited at `../registers/source-bundle/ukpga-1970-9.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for an individual's income tax self-assessment for a tax year: by when must they notify chargeability, file the return, and amend it; until when may HMRC open an enquiry; what payments on account and balancing payment are due and when; and until when may HMRC make an assessment?*

1. **Returns** (ss 7(1), (1A), (1C)(a), 8(1D)-(1G), 9ZA(2)-(3), 9A(2)):
   - the last day to notify chargeability;
   - the filing date for a paper or electronic return, including the two exceptions for late notices;
   - the last day to amend the return;
   - the last day for a notice of enquiry, including the quarter-day rule for late or amended returns.
2. **Payment** (ss 59A(1)-(2), 59B(1), (3)-(4), (6)):
   - whether payments on account are due, and each one's amount and date;
   - the balancing payment and its date;
   - the due date of tax under another assessment.
3. **Assessment time limits** (ss 34(1), 36(1), (1A), 36A(2)): the last day for an assessment:
   - 4 years after the end of the tax year;
   - 6 where the loss of tax was careless;
   - 12 where it involves an offshore matter or transfer;
   - 20 where it was deliberate, or a s 7 failure, or a tax avoidance scheme disclosure failure.

Left out on purpose:
- partnership, trustee and company returns;
- the substance of enquiries and their completion;
- appeals;
- claims;
- recovery, interest and penalties (ss 86-107);
- PAYE;
- Schedule 3ZA;
- the rest.

## Inputs, not worked out

- **The tax year:** written as the calendar year in which it begins (2024 for 2024-25).
- **Notices and returns:** whether and when a notice to file was given; whether the return is paper or electronic; the date it was delivered; any amendment date.
- **Amounts:** the assessed amount for the previous year, the tax deducted at source, the prescribed minimum and proportion for payments on account, the self-assessed tax for the year, and the payments made.
- **Assessments:** how any loss of tax was brought about, and the date of any other notice of assessment.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Tax years:** the year of assessment Y runs from 6 April Y to 5 April Y+1, and "Year 2" is the following tax year. So "31st October in Year 2" is 31 October Y+1, and "31st January in Year 2" is 31 January Y+2.
- **s 7(1C)(a), "the period of 6 months from the end of the year of assessment"**: ends on 5 October Y+1.
- **"The period of 3 months beginning with the date of the notice"**: the day before the corresponding date three months later, or the last day of that month if it has none.
- **s 9ZA(2), "not more than twelve months after the filing date"**: on or before the corresponding date. s 9A(2)(a), "up to the end of the period of twelve months after the day on which the return was delivered": the corresponding date. s 9A(2)(b)-(c): the next quarter day (31 January, 30 April, 31 July, 31 October) after the first anniversary.
- **s 59B(6), "the day following the end of the period of 30 days beginning with the day on which the notice of assessment is given"**: notice date + 30.
- **ss 34, 36, 36A, "not more than N years after the end of the year of assessment"**: on or before 5 April Y+1+N.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`tma-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
