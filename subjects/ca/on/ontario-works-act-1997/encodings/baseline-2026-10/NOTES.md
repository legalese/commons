# Ontario Works Act, 1997 and O. Reg. 134/98 (income assistance) — baseline encoding

© King's Printer for Ontario, 1997 (the Act) and 1998 (O. Reg. 134/98). The words quoted in the modules are from an unofficial reproduction of the consolidated law published on e-Laws: **NOT AN OFFICIAL VERSION**. Official copies are those described in the Legislation Act, 2006. See `SOURCE-LICENSE.md`.

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the regulation's own terms in `on-ow.l4`; the two date rules are in `on-ow-dates.l4`, so that only it and the seat import `daydate`. The applicant's or recipient's questions are in `on-ow-seat.l4`, which IMPORTs both and calls their rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Edition

- **Ontario Works Act, 1997** (S.O. 1997, c. 25, Sched. A): e-Laws consolidation from 2025-07-01 (last amendment 2024, c. 28, Sched. 25, s. 8) to the e-Laws currency date 2026-10-14, English, deposited at `../../registers/source-bundle/S.O.-1997-c.-25-Sched.-A.txt`. The 2021, c. 25, Sched. 21 amendments ("employment and life stabilization assistance") are printed as notes and are not in force; the encoding follows the text in force.
- **General, O. Reg. 134/98**: consolidation from 2026-08-13 (last amendment O. Reg. 276/26) to the same currency date, deposited at `../../registers/source-bundle/O.-Reg.-134-98.txt`. It states every rate used here, so nothing is an indexed input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `on-ow.l4`, `on-ow-dates.l4`, `on-ow-seat.l4` | `on-ow-cases.l4` | 52 written, 52 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Two `#TRACE`s carry their expected results in `-- expect:` comments: a breach by the administrator (the review completed 35 days after the request), and a lapse (no review requested) that ends FULFILLED. Every expected value was worked by hand from the text.

## Seat

**The applicant for, or recipient of, Ontario Works income assistance**: "Can I apply on my own behalf? What is my asset limit? What are my budgetary requirements? How much of my income counts? Am I eligible? How much would I get a month? By when must I ask for a review, and appeal?"

Provisions addressed to the administrator are encoded for what they mean to the person: the administrator "shall" complete an internal review within 30 days (s 70 (1)), a duty owed to the person; the administrator's determinations (special diet amounts, the value of items, approvals under s 39) are inputs.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers:** the Act and O. Reg. 134/98 (General). No other regulation under the Act is used.
- **The actors the text names:** the applicant or recipient and the administrator (the Social Benefits Tribunal appears only as the place an appeal is filed).
- **Judgments handed to others are answered conditionally:** the special diet amounts the administrator determines, the s 39 approvals, whether the information and other prescribed conditions are met — all inputs.
- **The regulation's own definitions are worked out from facts:** benefit unit, dependants other than a spouse, benefit unit size, budgetary requirements, the earnings included in income. **Borrowed or judgment-laden terms are asked as facts:** spouse (s 1 (1) (d) turns on the administrator's view of the relationship), dependent adult and financial independence (s 2 (1), (2)), resident in Ontario.
- **One case:** one benefit unit for one month.
- **The regulation's own terms**, quoted in the comment above each rule.
- **Machinery out:** delivery agents, cost sharing, the Tribunal's constitution, fraud control, regulation-making powers.

## Questions exported (8)

In `on-ow-seat.l4`, under `§` headings:

1. Can I apply on my own behalf (s 11 (1), (3))
2. What is my asset limit (s 38 (1))
3. What are my budgetary requirements (s 41 (1), s 42)
4. How much of my income counts (ss 48, 49)
5. Am I eligible for Ontario Works (Act s 7 (3))
6. How much Ontario Works a month (s 40 (1))
7. By when must I request an internal review (s 69 (1)) — for a person who has received a decision
8. By when must I appeal (s 72 (1), (2)) — likewise

Questions 5 and 6 take the answers to 1 to 4 as inputs (numbers and a yes/no), in the order the form asks them.

## Regulative rules (1)

`the internal review and appeal` (`on-ow.l4`; Act ss 27 (1), 28 (1); O. Reg. 134/98 ss 69 (1), 70 (1), 72 (1)): the applicant or recipient DOES request an internal review in writing WITHIN 30 days, HENCE the administrator MUST complete it WITHIN 30 days (LEST BREACH BY the administrator, BECAUSE …), HENCE the person DOES file a notice of appeal WITHIN 30 days. The person's steps are options: each is `DO … LEST FULFILLED`, because a `MAY` would move on to its `HENCE` even when unused, and a person who lets the time pass is in breach of nothing.

## Scope

**In:** Act s 7 (1)-(3); O. Reg. 134/98 s 1 (1) definitions as used, s 11 (1), (3), s 38 (1) (a)-(d), s 39 (1) (as the description of what the asset input leaves out), s 40 (1), s 41 (1) paras 1-6, s 42 (1), (2) paras 1-4, s 48 (1), s 49 (1) paras 1-4 (paras 5, 6 and 10 as the description of the earnings input), (2), (3), ss 52, 53 (as the description of what the income input leaves out), s 69 (1), s 70 (1), s 72 (1), (2).

**Out** (each a `not covered` answer where a question can reach it): board and lodging, long-term care homes, hostels and community residences (ss 43, 44); shared custody (s 44.2); the ss 46-47.2 reductions (custody, hospital, treatment, OCB retroactive payments); applicants for ODSP (s 38 (2)); applications on behalf of a child only (s 11 (2), (4), s 38 (1) (e)); sponsored immigrants living with the sponsor (s 51); boarder and rental income (s 50, part of the "other income" input if any); the first-month proration (s 40 (2)); benefits (Part VII), employment assistance (Parts I, III), emergency assistance, overpayment recovery; the not-in-force 2021 amendments.

Links: the Ontario Taxation Act encoding, `subjects/ca/on/taxation-act-2007/encodings/baseline-2026-10/` (the Ontario child benefit and Trillium Benefit it computes are exempt here under ss 52, 53); the federal Income Tax Act encoding, `subjects/ca/income-tax-act/` (the Canada child benefit and GST/HST credit, exempt here). Cross-folder IMPORT is not possible in the stable `l4`.

## What the regulation turns out to say

1. **Eligibility is a comparison, and the amount is the difference.** No one is eligible unless "the budgetary requirements of the person and any dependants exceed their income and their assets do not exceed the prescribed limits" (Act s 7 (3) (b)); assistance is the requirements less income (s 40 (1)). Asserted.
2. **A single person's maximum is $733 a month**: $343 for basic needs (s 41 (1) para 1) and up to $390 for shelter (s 42 (2) para 2). Asserted.
3. **The basic needs Table follows the adult dependants.** Read across its rows, the amount depends on how many dependants are 18 or older (and, with no spouse and no adult dependant, on whether there are children: $360 instead of $343). The rule for "each additional dependant" ($175 if 18 or older, $0 if under 18) is ambiguous for four or more dependants of mixed ages: for two adults and two children, treating the fourth as a child gives $781, treating it as an adult gives $623 + $175 = $798. Only the first reading gives the same answer whichever three dependants are put in the Table, so the encoding takes it. Interpretive. Asserted ($781).
4. **The earnings exemption in this text is $200 and half the rest.** Section 49 (1) para 1 takes off the required payroll deductions, then "$200 per adult member of the benefit unit with earnings", then "50 per cent" of the remainder, then allowed child care costs. Asserted ($1,000 gross, $100 deducted: $350 counts).
5. **Applicants do not get the exemption at first.** The $200 and the 50% are not applied in deciding whether an applicant is eligible, or for the first three months (para 3), unless the person had assistance for three months that was cancelled less than six months before, with earnings at the time (para 4). Asserted ($900 counts for the same earner applying).
6. **Heat can push shelter above the maximum.** If "the cost of energy for heat exceeds the maximum amount payable for shelter", shelter is the cost of heat (s 42 (2) para 4). Asserted (single, heat $420: shelter $420, not $390).
7. **The special diet allowance is capped per member** at $250 a month (s 41 (1) para 4 ii), whatever the administrator determines. Asserted.
8. **Child care for each child is capped at $600 unless licensed** (s 49 (1) para 2). Asserted.
9. **Employment insurance and CPP are income but not earnings** (s 49 (2), (3)), so they get no $200 or 50% exemption and count in full. Asserted ($800 of EI counts as $800).
10. **The Canada child benefit, the Ontario child benefit, the GST/HST credit, the Canada workers benefit, the Ontario Trillium Benefit and the Canada disability benefit are not income** (ss 52, 53). The income input is described to leave them out; not asserted.
11. **No appeal without an internal review.** "No appeal may be commenced unless an internal review has been requested" (Act s 27 (1)), within 30 days of receiving the decision (s 69 (1)); the appeal is due within 30 days of the decision becoming final (s 72 (1)) and never more than a year after the original decision (s 72 (2)). Asserted (the one-year limit can come first).
12. **The administrator's 30 days is a duty without a stated consequence.** Section 70 (1) prescribes "30 days from the day the administrator receives the request"; neither the Act nor the regulation says what follows if it is missed. The encoding records a breach by the administrator and nothing more. Asserted by `#TRACE` (an `-- expect:` comment).

## What would need doing before this is worth relying on

- **Shared custody (s 44.2)**, which needs a reading of "the amount payable for a child" in a Table that does not separate one out.
- **Board and lodging (s 44)**, long-term care (s 43) and the other reductions (ss 46-47.2).
- **Assets and income itemised**: the s 39 exclusions and the s 52-54 exemptions, now described in the inputs, worked out from facts.
- **The ODSP encoding**, for s 38 (2) and for comparison (`subjects/ca/on/ontario-disability-support-program-act-1997/`, not yet encoded).
- **An independent test pass**, and a check of finding 3 against ministry policy directives (none was read).
