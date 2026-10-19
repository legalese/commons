# Encoding brief: the Taxation (Cross-border Trade) Act 2018 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Taxation (Cross-border Trade) Act 2018** (2018 c. 22), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 18 March 2026, deposited at `../registers/source-bundle/ukpga-2018-22.txt` (Crown copyright, Open Government Licence v3.0). The conversion drops the paragraph numbers in the Schedules. Schedule 6 runs, in order:

- para 1, enforcement needs notification;
- para 2, notification;
- para 3, regulations;
- para 4, the time limit for notification;
- then payment, guarantees and repayment.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *goods arrive in the United Kingdom. Are they chargeable; is a liability to import duty incurred, and when; who is liable; how much ad valorem duty is due; and by when must HMRC notify the liability for it to be enforceable?*

1. **Liability** (ss 2(1), 3(3)-(4), 4(1)-(4), 5(1)-(2)):
   - goods are chargeable unless they are domestic goods;
   - when a liability arises: on acceptance of a free-circulation declaration; for storage, transit or inward processing, only on an unentitled declaration or a breach; for authorised use or temporary admission, on acceptance (at the reduced rate if entitled, otherwise the normal rate); for goods not presented or not declared, when they become liable to forfeiture.
2. **Persons liable** (s 6(1)-(4), (7)):
   - the declarant, or for unpresented goods whoever was in possession or control on entry;
   - also the person on whose behalf the declaration was made, and anyone otherwise involved in a breach knowing or with reason to know of it;
   - all of them jointly and severally.
3. **Amount and notification** (ss 7, 16(2)-(3); Sch 6 paras 1, 4):
   - ad valorem duty: the applicable rate × the transaction value (the rate after preferences, quotas, suspension or remedies is an input);
   - the last day for notification: before the end of the 3 years beginning with the day the liability was incurred, or 20 years where an officer thinks an offence was committed;
   - liability is enforceable only once notified within that time.

Left out on purpose:
- the content of the customs tariff;
- preferences, quotas and trade remedies (ss 8-15, Schedules 4-5), whose outcome is an input rate;
- origin;
- currency;
- reliefs (as an input rate);
- customs agents and AEOs;
- Northern Ireland (ss 30A-30C);
- export duty;
- VAT and excise (Parts 2-3);
- the other Schedules.

## Inputs, not worked out

- **The goods:** whether they are domestic goods; the procedure declared; whether there was an entitlement to make the declaration; the dates of acceptance, any breach, and liability to forfeiture.
- **Persons:** who made the declaration, for whom, who possessed the goods on entry, and who was involved with the requisite knowledge.
- **Amount:** the applicable rate (as a percentage) and the transaction value.
- **Notification:** whether an officer thinks an offence was committed, and the date of any notification.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Sch 6 para 4: "before the end of the period of 3 years beginning with the day on which the liability was incurred"**: on or before the day before the corresponding date three years later (or 20 years), or the last day of that month if it has none.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`tcta-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
