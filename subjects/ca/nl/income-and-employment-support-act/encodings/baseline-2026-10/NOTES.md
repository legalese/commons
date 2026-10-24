# Newfoundland and Labrador Income and Employment Support Act (income support) -- baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the Act's and Regulations' own terms in `nl-ies.l4`; the time limits and the regulative rules, which need dates, are in `nl-ies-deadlines.l4`. The applicant's questions are in `nl-ies-seat.l4`, which IMPORTs both and calls their rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Edition

- **Income and Employment Support Act**, SNL2002 cI-0.1, House of Assembly consolidation as amended to 2019 cS-29.02 s27, retrieved 2026-10-24: sections 2, 13 to 17, 41 and 43, deposited at `../../registers/source-bundle/SNL2002-cI-0.1-selected.txt`.
- **Income and Employment Support Regulations**, NLR 144/04, as amended to 106/25, retrieved 2026-10-24: Part I (ss 1 to 29) and s 45, deposited at `../../registers/source-bundle/NLR-144-04-part-i.txt`.

The amounts are those of the Regulations as amended to 106/25 (s 13(1) last amended by 88/25).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nl-ies.l4`, `nl-ies-deadlines.l4`, `nl-ies-seat.l4` | `nl-ies-cases.l4` | 48 written, 48 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Two `#TRACE`s show breaches (information given on day 31 of 30; a review performed 20 days after the request against 15), each with its expected result in an `-- expect:` comment; the run shows both breaches as expected. Every expected value was worked by hand from the text.

## Seat

**The applicant for, or recipient of, income support** (with a spouse or cohabiting partner, who is part of the application: Act s 2(d), (p)): "Can I get income support? What is the most I can get a month? What must I report? By when must I answer, ask for a review, or appeal?"

Officers, the minister, the internal reviewer and the appeal board appear only as what they may do to the person or must do for them.

The 2026-10-18 defaults:

- **The Act with the instrument that sets its numbers:** the Regulations, Part I.
- **The actors the text names:** the applicant or recipient, the officer, the internal reviewer, the appeal board.
- **Judgments handed to others answered conditionally:** an officer's approval of an absence (reg s 4(2)), an officer's authorizing an expenses deduction (reg s 11), the minister's child benefit adjustment (reg s 19(1)(g)), the certification of blindness, diabetes or need for supportive services, and the officer's extra days (reg s 5(3)) are inputs. The "up to" amounts are given as the most the Regulations allow (reg s 6(3)(a) also brings in the minister's policies, which are not law deposited here).
- **The Act's own definitions worked out from facts:** liquid assets counted (reg ss 8(b), 26), the exemption class (reg s 12(a)), living in the province (Act s 15, reg s 4). Borrowed terms (spouse, cohabiting partner, dependent) asked as facts.
- **One case:** one application, for one month.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** officers' appointment, information sharing, the appeal board's constitution and powers, regulation-making.

## Regulative rules

Three, in `nl-ies-deadlines.l4`:

1. `my duty to answer the request for information` (reg s 5(2), (3), (5)): the recipient MUST provide the information WITHIN 30 days (plus any extra the officer allows), `LEST BREACH ... BECAUSE` the officer may deny, vary, suspend or cancel. Asserted on days 25 and 35 (with 10 extra); breach on day 31 shown by `#TRACE`.
2. `my right to an internal review` (Act s 41(3), (5)): the recipient MAY request a review in writing WITHIN 60 days, HENCE the internal reviewer MUST perform it WITHIN 15 days. Asserted (request on day 50, review on day 62); the reviewer's breach (day 70) shown by `#TRACE`.
3. `my right to appeal` (Act s 43(2), (3)(e)): the recipient MAY appeal in writing WITHIN 60 days of receiving the review's outcome, HENCE the appeal board MUST hear it WITHIN 30 days. Asserted.

The duty to report changes "immediately" (Act s 17(5), reg s 7(1)) is a yes/no question rather than a timed rule, since "immediately" sets no number of days.

## Questions exported (9, in `nl-ies-seat.l4`)

Do I meet the basic conditions (Act ss 13, 15, regs ss 4, 9(5)); are my liquid assets within the limit (reg s 26); do I pass the income test (reg s 9(3)); the most monthly income support I can get (regs ss 12, 13, 16, 18, 19(1)); how much of my earnings is exempt (reg s 12(a)); must I report this change (Act s 17(5), reg s 7(1)); by when must I answer the officer (reg s 5(2)); by when must I ask for an internal review (Act s 41(3)); by when must I appeal (Act s 43(2)).

## Scope

**In:** Act ss 2 (definitions used), 13, 15, 17(5); reg ss 4(1), (2), 5(2), (3), (5), 7(1), (2), 8(b) (in outline), 9(2), (3), (5), 11, 12(a), 13, 16(1), (2), 18(1), 19(1)(a), (b), (f), (h), (i), (j), (p), 26; Act ss 41(3), (5), 43(2), (3)(e).

**Out:** employment support (Act s 14(2) to (4), Regulations Part II); emergency eligibility (Act s 16, reg s 28); the start-up allowance for victims of violence (reg s 17); the under-21 rules (reg s 18(2) to (4)); hospital and shelter stays (reg s 19(2) to (4)); the s 19(1) amounts set by an officer or the minister or paid once ((c), (d), (e), (g), (k), (l), (n), (o)) and s 19(5); special needs (regs ss 21 to 24); support trusts (s 25); funeral costs (s 27); lump sums (s 10); the exemptions in s 12(b), (d); the detailed lists of exempt and non-exempt income in s 8(a), (c), (d), which are left to the person when stating income; overpayment, recovery and garnishment (Act Part III); offences (Part V).

## What the Regulations turn out to say

1. **The basic amount is "up to $561" for each adult** (reg s 13(1), as amended by 88/25), reduced by $76, $49 or $27 (apartment or house) or $61, $49 or $12 (bed sitting room) where heat, electricity or both are included (s 13(2)). Asserted.
2. **Shelter is "up to $522" for one adult, alone or with a dependent, and $299 for each of two or more adults** (s 16(1)); where the basic amount was reduced for included utilities, the shelter maximum rises by the same amount, never above the actual shelter cost (s 16(2)). So for a renter with utilities included the two adjustments cancel up to the actual rent. Asserted (cases A, B, B2, F).
3. **"2 or more people" and "2 or more persons" are not defined.** The liquid-asset limit (s 26(1)(b)) and the earnings exemption (s 12(a)(ii)) both turn on them. The encoding counts everyone in the application, dependent children included; a reading that counts only adults would give a single parent the one-person limit ($6,000) and the $75 exemption. Asserted as encoded (case C: a single parent with two children gets the $150 exemption).
4. **Earnings keep the first $75 (one person) or $150 (two or more) and 20% of the rest** (s 12(a)); $150 and $250 where someone needs supportive services. Asserted.
5. **The application test subtracts the expenses deduction twice.** Section 9(3) compares BR + 40% of BR + CBA with "I - D", where I is net income "minus the deduction for expenses ... referred to in section 11" and D is "the deduction referred to in section 11". Read as written, an applicant with $1,700 of income and a $100 deduction is tested on $1,500. The encoding follows the text; it may be a drafting slip for I being gross income. Asserted.
6. **Income is deducted only from the basic and shelter amounts** (s 18(1): "from the total income support to which the applicant or recipient is entitled under section 13 and section 16"). The s 19(1) amounts (fuel, the $105 at 65, the $168 for a single parent, the $150 coastal Labrador amount, $89 for blindness, $60 for diabetes) are not reduced by income under the text. The encoding adds them after the deduction. Asserted (case D keeps $341 of s 19 amounts though income nearly uses up the rest).
7. **The fuel supplement is $132 in Labrador and $71 on the island**, where heat is not included in the rent (s 19(1)(a), (b)); a coastal Labrador household gets the Labrador fuel amount and the $150 coastal amount. Both are "up to" or fixed amounts that the encoding gives in full. Asserted.
8. **The liquid-asset limits are $6,000 and $11,000, and the first $20,000 of RRSPs is exempt** (s 26); only the excess, and only where the RRSPs "may be liquefied", counts. Asserted.
9. **A strike or lockout bars an application** (reg s 9(5)). Asserted.
10. **Absences:** up to 60 days for an approved purpose, longer only for approved medical reasons (reg s 4(2)). Asserted.
11. **Time limits:** 30 days to answer an officer's written request (reg s 5(2)), 60 days to ask for an internal review (Act s 41(3)), 15 days for the review (s 41(5)), 60 days to appeal from receipt of the outcome (s 43(2)), deemed received 7 business days after the decision (s 41(5)), and 30 days for the board to hear the appeal (s 43(3)(e)). Asserted, except the 7 business days (an input).
12. **Section 41(3) speaks of "the recipient"** although s 41(2) gives the right to "an applicant or recipient"; the encoding gives the 60 days to both.

## Before relying on it

- Michael to confirm that the House of Assembly's terms fall within the 24 October 2026 ruling (`SOURCE-LICENSE.md`).
- The department's policy manual, which s 6(3)(a) brings in, is not law and is not deposited; actual grants may be lower than the "up to" amounts.
- Settle findings 3, 5 and 6 against departmental practice, and add the s 8 income lists as a checklist if the form is to classify income for the person.
- An independent test pass.

## Access

The House of Assembly site was reachable over HTTPS with the honest user agent, at least 3 s between requests; robots.txt (`Disallow: /search` only) read first.
