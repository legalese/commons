# Rhode Island Works Program Rules and Regulations (218-RICR-20-00-2) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18.

- **The core, `ri-works.l4`.** Written in the rule's own actors and terms, with no seat.
  - **Regulative rules.** The duties with a deadline are `PARTY … MUST … WITHIN … LEST BREACH`. They are: reporting a change within ten days, reporting a child's absence within five days (s 2.21.2), and returning the Interim Report by the fifth day of the sixth month and within ten days of a warning notice (ss 2.22.1, 2.22.2). The two hearing rights, within 30 days and within 10 days for continued benefits (s 2.11.12), are `MAY` rules.
  - **Functions.** Eligibility tests and amounts are functions.
- **The seat layer, `ri-works-seat.l4`.** It asks the parent's or caretaker's questions, each with `@export` and a `@desc` on every input. It calls the core and restates no rule.

There is no REFUSE, and no question reaches anything outside the encoding. Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

## Edition

- **Encoded.** 218-RICR-20-00-2 as in force on 24 October 2026: a Technical Revision, effective 16 February 2025 to 10 November 2026. It is deposited at `../../registers/source-bundle/218-ricr-20-00-2-2025-02-16.txt` (the Department of State's HTML rendering; the page calls the PDF the official Final Regulation).
- **Also deposited.** The Amendment effective 10 November 2026, from the FY27 budget, is deposited beside it. Among the encoded rules it changes only the child support exclusion, which this encoding applies by month: $50 before 10 November 2026, then $100 for one child or $200 for two or more. Its other changes are wording, definitions, the post-employment benefit, and the fixed table row noted in finding 9.
- **Not deposited.** The enabling statute, R.I. Gen. Laws ch. 40-5.2, is not deposited: rilegislature.gov did not respond (see `../../../README.md`). The rule quotes and cites it throughout (for example § 40-5.2-10 for the standards and § 40-5.2-16 for the $10 minimum), but the statute itself could not be checked.

All the figures used are in the rule itself: the standards table, the disregards, the $5,000 resource limit, the 60 months and the $105 penalty. No annual publication is needed. One input is not: the 185 per cent of the federal poverty level that ends the earned income set aside is part of the "set aside applies" fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ri-works.l4`, `ri-works-seat.l4` | `ri-works-cases.l4` | 52 written, 52 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Three `#TRACE` breach checks were read as `BREACH`, with the party and reason their `-- expect:` comments give:
- a change reported on day 12;
- a child's absence reported on the sixth day;
- no Interim Report within ten days of the warning.

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the text.

## Seat

**The parent or caretaker relative** who applies for, or receives, RI Works cash assistance. Questions:
- "Does my child count by age?"
- "How much of our property counts, and is it within $5,000?"
- "What is our payment standard?"
- "How much of our income counts?"
- "How much will we get?"
- "Where do I stand on the 60-month limit?"
- "Do I meet a hardship criterion?"
- "How much is cut if I don't keep my employment plan?"
- "When can a cut start?"
- "Does my cash continue if I appeal?"

DHS's duties are encoded as what they mean for the person: the ten days' notice, and continued benefits pending a hearing.

Defaults:
- **The rule alone**, in its two deposited versions. The statute is not deposited.
- **The actors the text names:** the adult family member, the household, the recipient, the applicant, the Department (DHS).
- **Judgments left to others are asked as facts.** These are the hardship extension (DHS grants it), a DHS supervisor's approval under s 2.6.3(A)(5), good cause (assumed absent in the penalty question), and the parent's portion of the benefit for families other than two.
- **Definitions worked out from facts:** the eligible child by age, countable resources with the vehicle exclusion, net adjusted income, the payment, and the time-limit position. **Asked as facts:** plan size (the assistance unit rules, ss 2.4 and 2.18.3), what is excluded income under s 2.15.3, and whether the earned income set aside applies this month.
- **One case:** one assistance unit, in one month.
- **Terms:** the rule's own ("assistance plan", "net adjusted income", "cash assistance standard"), glossed.
- **Machinery out:** EBT, case records, error cases and claims.

## Read with

`subjects/us/social-security-act/`: federal Title IV-A (TANF), whose 60-month limit (42 U.S.C. 608(a)(7)) is the frame for s 2.6. Cross-folder IMPORT is not possible in the stable `l4`.

## Scope

**In:**
- the eligible child by age: ss 2.5.2(A) and 2.18.3(A)(1)(b);
- resources: ss 2.14.1(A), 2.14.2(F)(1)(a), (2);
- income and the payment: ss 2.15.3(D) (both versions), (E); 2.15.5(A), (B)(1)–(2); 2.18.1, 2.18.2, 2.18.3(A)(5), 2.18.5(A)–(B);
- the time limit: ss 2.6(A), (D), 2.6.1, 2.6.3(A), 2.6.4(A);
- the work penalty: s 2.11.11(A)–(B);
- reporting and the Interim Report: ss 2.21.2(A)–(B), 2.22.1(A), 2.22.2(B);
- notice and hearing: ss 2.11.12(A), 2.29.1(B), (C)(4), 2.29.3(A).

**Out:**
- who is in the assistance unit (s 2.4), so plan size is an input;
- non-financial requirements other than age, such as relationship, residence and Social Security numbers;
- non-citizens and sponsor deeming (s 2.17);
- child support cooperation (s 2.7);
- employment plans and work activities (ss 2.10, 2.11.1–2.11.10);
- minor parents (s 2.12) and domestic violence waivers (s 2.13);
- trusts, real property and income-producing property other than vehicles, which the person leaves out of the inputs;
- self-employment and rental income, and deemed income (ss 2.15.9, 2.16);
- first-month proration (s 2.18.5(C)) and the post-closure bonus (s 2.18.6);
- EBT, overpayments and claims (ss 2.19, 2.24–2.28).

## What the rule turns out to say

1. **RI Works sets its whole benefit computation in the rule, not in a manual.** It has a monthly standard for each plan size, from $510 for one person to $2,365 for fifteen plus $125 for each further person (s 2.18.1). The standard is cut by $65 in subsidized housing (s 2.18.2). The family gets the standard less net adjusted income (s 2.18.3(A)(5)), provided net adjusted income is "less than" the standard (s 2.15.5(B)). A mother and child in October 2026, with $1,125 of earnings, $200 of child care for a three-year-old and $150 of child support, get $476 a month. Asserted.
2. **The earned income disregard is $525 plus half the rest, for each eligible earner.** Children's earnings are disregarded entirely (s 2.15.5(B)(1)). Earnings of $525 or less count for nothing. Two earning adults each get the disregard. Asserted.
3. **A new job can be wholly set aside for six months.** The earnings of an adult "who gains employment while an active RI Works household member" are excluded, at the household's request, for six months or until household income passes 185 per cent of the federal poverty level (s 2.15.3(E)). Asserted: $1,500 of new earnings set aside leaves the payment at $601.
4. **The resource limit is $5,000, and up to two vehicles are excluded.** One vehicle per adult, up to two per household, is excluded (s 2.14.2(F)(1)(a)). The rule does not say which vehicles are the excluded ones when there are more vehicles than exclusions. The encoding takes them in the order the person lists them, so the person can name the most valuable. The text says the family is ineligible if resources "exceed" $5,000, so exactly $5,000 is within the limit. Asserted.
5. **The time limit is 60 months, but it does not apply where the parents are on SSI or the caretaker is a relative outside the payment.** Months in other states since 1997 count, and so do months under sanction, but not months as a child (s 2.6(D)). The exceptions are in s 2.6.1. Hardship extensions run six months at a time, need one of five criteria, and are DHS's to grant (ss 2.6.3, 2.6.4). Asserted.
6. **Dependent care comes off earnings only, and only up to the caps.** The caps are $200 a month for a child under two, and $175 for an older child or an incapacitated adult (s 2.15.5(B)(2)). Net adjusted income is unearned income "plus any amount remaining from earned income after deducting the earned income disregards and any allowable dependent care disregards" (s 2.15.5(A)). The encoding therefore lets the care disregard bring earnings down to nil but not below, so it never reduces unearned income. Asserted (two infants, $450 of care: $400 allowed; $300 of Social Security still counts in full).
7. **The child support exclusion rises on 10 November 2026.** It goes from the first $50 a month to $100 for one child or $200 for two or more children, with only one such amount per family (s 2.15.3(D) in each version). Asserted for October and December 2026.
8. **Payments under $10 are not made, but the family stays a recipient.** Where the monthly payment would be less than $10, none is made, but the family remains a recipient "for all other purposes" (s 2.18.5(A), (B)(2)). Months with no payment presumably do not count towards the time limit, since s 2.3 counts months "in which a cash payment is made, or supportive services are accessed", but this is not encoded. The boundary is asserted: a $6 payment is not made and a $10 one is.
9. **The standards table in the version in force has a typo.** For plan size 10, the semi-monthly column reads "$724.50870.00". The monthly standard, $1,740, is unaffected, and half of it is $870.00, which the Amendment of 10 November 2026 prints. The encoding uses monthly figures only.
10. **The $105 parent's portion for a family of two does not fit the current table.** Section 2.11.11(B) computes the penalty for a family of two "utilizing a family size of three (3), in which the parent's portion equals one hundred five dollars ($105.00)". The current standards for three and two people differ by $164 ($865 − $701). The $105 looks like a figure kept from an earlier table. The encoding applies $105 as written. For other family sizes the rule never says how the parent's portion is found, so it is an input. Asserted.
11. **Continued benefits pending a hearing are for recipients only, and need a request within ten days.** A hearing may be asked for within 30 days of the notice, but continued benefits need a request within 10 days (s 2.11.12(A)). They are "not available for applicants" (s 2.29.1(C)(4)). They are not continued where the cut comes from a change in law for a class of recipients, unless the appeal says the grant was computed wrongly (s 2.29.3(A)). Asserted.
12. **The five-day period for reporting a child's absence counts the first day.** It "begins with the date that the adult family member(s) becomes aware" (s 2.21.2(A)(1)), so the day of awareness is day 1 and the report is late on day 6. The ten-day period for other changes runs "within ten (10) days of the change". Traced.

## Before relying on it

- Deposit R.I. Gen. Laws ch. 40-5.2 when rilegislature.gov can be reached, and check the rule against it. This matters most for the standards (§ 40-5.2-10), the time limit and the set aside.
- Encode the assistance unit (s 2.4) so that plan size is worked out rather than asked.
- Check finding 10 with DHS.
- An independent test pass.
