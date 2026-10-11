# Merchant Shipping (Maritime Labour Convention) Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MSMLCA2014.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31 December
2021. The latest amending Act annotated in the body is 16/2020. The arrangement of
sections at the top of the deposit is out of step with the body (for example, it lists
"Wages" against 18). This row follows the body's numbering.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0107**: Tier 2 of the remaining Singapore Acts,
ordered by everyday-life relevance. The requirement asks what the Act decides for a
person or business it applies to. No scenario has asked a sharper question yet.

Parts 3, 4 and 6 apply to Singapore ships "ordinarily engaged in commercial
activities" and the seafarers on them (s 3(2)). This row takes the employment terms a
seafarer or shipowner deals with: minimum ages and young seafarers (ss 2, 5, 6,
17–19), medical certificates (ss 7–9), notice (s 14), hours of rest (s 16), late wages
(s 20), annual leave (s 22), repatriation (s 23), wages after a wreck or sale (s 24),
sickness and injury (ss 35, 36, 38, 39), and four maximum fines (ss 5, 12, 16, 34).

Not encoded:
- exemptions (s 4);
- recruitment-service regulation, apart from the fee ban (s 12);
- crew lists (s 15);
- wage accounts and allotment notes (ss 20(4)–(7), 21);
- catering (Part 5);
- medical provision on board (ss 28–33);
- financial security, apart from the fine (ss 34, 34A);
- burial costs (s 37);
- health and safety (Part 7);
- certification, complaints and port inspection (Parts 8–10);
- Part 11.

The Convention itself and the regulations made under the Act were not read.

## What the Act turns out to say

### 1. Piracy does not end the contract or the wages

If a seafarer is held captive after piracy or armed robbery, the employment agreement
"continues to have effect during the period of captivity". This holds even if its expiry
date has passed or either party has given notice (s 14(13)). Wages, other entitlements
and allotments "must continue to be paid during the entire period of captivity". They
stop only when the seafarer is released and repatriated, or dies (s 20(8)). Release
from captivity is a ground on which the shipowner must repatriate the seafarer
(s 23(2)(e)). All three provisions came in with Act 16/2020. Asserted for repatriation;
the continuing wages are quoted but not modelled.

### 2. Two months of unpaid wages counts as abandonment, and late wages cost a day's pay per day

The shipowner must repatriate a seafarer whose ties it has "unilaterally severed",
"including where the shipowner has failed to pay the seafarer's contractual wages for a
period of at least 2 months" (s 23(2)(d)(ii)). Wages are due monthly, by the last day of
the month. For every day they stay unpaid, the seafarer is owed "wages at the rate last
payable" (s 20(2)). There is no extra pay if the delay came from a reasonable dispute,
from the seafarer's own default, or from another cause that was not the payer's wrongful
act (s 20(3)). Asserted.

### 3. Hours of rest are a floor that cannot be bought out

The minimum is 10 hours in any 24 and 77 in any 7 days (s 16(2)). The rest may be split
into no more than two periods, one of them at least 6 hours, with no more than 14 hours
between them (s 16(3)). So a 5 + 5 split fails even though it adds up to 10 hours. No
one may "cause or permit payment to be made in lieu of hours of rest" (s 16(5)). The
shipowner's maximum fine is $10,000 (s 16(11)). Asserted.

### 4. No one may charge a seafarer for a job

"Despite any written law to the contrary", no one may demand or receive any payment
from a seafarer, or from someone seeking work as one, "for providing the prospective
employee with employment". The maximum penalty is $5,000, 2 years, or both (s 12(2),
(3)). Asserted (the fine).

### 5. Young seafarers: three limits, and one carries no penalty

The minimum age on board is 16 (s 5). A ship's cook must be 18 (s 6). A young seafarer
(16 or 17) may not do night work between 9 p.m. and 6 a.m. without the Director's
approval (s 18). They also may not do any of eleven kinds of hazardous work (s 19), a
list that includes the "cleaning of catering machinery". The 8-hour-day and 40-hour-week
limit in s 17 can be set aside on the master's opinion about training or watchkeeping.
Unlike ss 18 and 19, s 17 has no offence subsection: none appears in the section as read.
Asserted.

### 6. Annual leave is 2.5 days a month, rounded half up, and lost after a year

Leave accrues at "at least 2.5 days per month of continuous service" (s 22(1)), pro rata
for completed months (s 22(3)). A fraction of half a day or more counts as a whole day
(s 22(11)). So 5 months gives 13 days and 4 months gives 10. Leave not taken within 12
months after the end of each 12 months of service is lost (s 22(9)). Public holidays,
sick time and time awaiting repatriation do not count as annual leave (s 22(4)).
Asserted, apart from s 22(4).

### 7. Sickness and injury: 16 weeks, less work-injury compensation, with three exclusions

The shipowner pays expenses reasonably incurred for sickness or injury arising during
employment, or caused by events during it. That duty runs for 16 weeks from onset
(s 35(1), (4)). The shipowner also makes up the gap between wages received and full
wages (s 36). Both duties are reduced by what the seafarer has already been paid under
the Work Injury Compensation Act 2019 (s 39). Section 38 excludes three cases: an injury
incurred "otherwise than in the service of the ship", wilful misconduct, and a condition
that existed when the seafarer signed and was deliberately concealed. Section 38 says it
excludes s 37 (burial costs) too, but each of its three conditions refers only to the
injury or sickness "mentioned in section 35 or 36". How it applies to s 37 is unclear,
and s 37 is not encoded. Asserted for ss 35, 36, 38 and 39.

### 8. Medical certificates and notice

A medical fitness certificate lasts at most 1 year if the holder is under 18 and 2 years
otherwise (s 9). A certificate that expires mid-voyage may be worked on until the first
port where an examination is possible, but for no more than 3 months (s 7(3)). Notice to
end the agreement must be the same for both sides and at least 7 days, unless a
prescribed exception applies (s 14(10)). The day the notice is given counts (s 14(11)).
Asserted.

## What would need doing before this is worth anything

- Read the Convention's Standards and the regulations made under ss 12, 14, 16 and 34.
  Many of the duties encoded here are "as may be prescribed".
- Model the interval between rest periods over a real 24-hour log rather than as given
  numbers. Model "months" in ss 7, 22 and 23 as calendar dates.
- Encode application (s 3), exemption (s 4) and the definitions of "ship" and "seafarer".
  This row assumes the Act applies.
- Resolve how s 38 applies to s 37.
- No case law was searched.
