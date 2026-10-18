# Encoding brief: the Pensions Act 2008 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Pensions Act 2008** (2008 c. 30), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 29 June 2026, deposited at `../registers/source-bundle/ukpga-2008-30.txt` (Crown copyright, Open Government Licence v3.0). In this version:

- the earnings trigger (s 3(1)(c)) is £10,000;
- the qualifying earnings band (s 13(1)) is £6,240 to £50,270.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *for one worker and one pay reference period: are they a jobholder, and must the employer automatically enrol them, or may they opt in or ask to join; what are their qualifying earnings and the minimum contributions a money purchase scheme must take; and, if the Regulator issues penalty notices, what are the limits and dates?*

1. **Workplace pension status** (ss 1(1), 3(1)-(4), (6B), 7(1)-(2), 9(1)), on the first day of the pay reference period. The status is one of:
   - an eligible jobholder to be automatically enrolled;
   - a jobholder who may opt in;
   - a worker without qualifying earnings who may ask to join;
   - none of these.
2. **Qualifying earnings and contributions** (ss 13(1)-(2), 20(1)(a)-(c)):
   - qualifying earnings for a period of any length (pro rata);
   - the minimum employer contribution (3%) and total (8%);
   - whether a UK money purchase scheme's contributions meet them.
3. **Penalty notices** (ss 40(4)-(5), 41(2), (4)-(6)):
   - the maximum fixed penalty (£50,000) and the earliest payment date (at least 4 weeks after issue);
   - whether an escalating penalty notice may be issued;
   - the escalating penalty: at most £10,000 a day, from the stated date until compliance.

Left out on purpose:
- re-enrolment (ss 5-6);
- opt-out mechanics (s 8);
- information duties (ss 10-11A);
- defined benefit, hybrid and personal pension quality tests (ss 21-28);
- Master Trust approval and asset allocation (ss 28A-28L), including Condition 1 and 2 of s 20(1A), which is an input;
- transitional periods (ss 29-30);
- the compliance notices themselves (ss 35-37);
- Parts 2-6.

## Inputs, not worked out

- **The worker:** date of birth, the day they reach pensionable age, whether they work or ordinarily work in Great Britain under a worker's contract, and the s 3(3)-(4) exceptions.
- **The pay reference period:** its length in months, the earnings in it, and its first day.
- **Contributions:** the employer's and the jobholder's.
- **Penalty notices:** the issue date, the escalating start date, the daily rate, the compliance date, and any pending review or reference.

## Dates and amounts, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Ages:** a person is "aged at least 16" from their 16th birthday, and "under 75" before their 75th birthday. "Has not reached pensionable age" means before that day.
- **s 3(6B), 13(2): "proportionately less or more"**: multiply by (months ÷ 12), with no rounding (s 15A rounding orders are not applied).
- **s 3(1)(c): "more than £10,000"**: strictly more.
- **s 40(5)(b): "at least 4 weeks after the date on which the notice is issued"**: the issue date + 28.
- **s 41(6)(e): the escalating penalty is payable at the daily rate "until the date on which the person complies"**: the days from the stated start date up to but not including the compliance date.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`pa08-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
