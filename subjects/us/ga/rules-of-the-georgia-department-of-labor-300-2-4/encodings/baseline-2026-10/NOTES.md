# Georgia unemployment insurance claimant duties (Rules 300-2-4): baseline, October 2026

## Method

This baseline was written straight from the deposited rules, from the seat of the claimant, with the design defaults ruled on 2026-10-18. It was checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. There was no pipeline, no coverage table, no independent test pass and no human gate.

**Why rules and not the statute.** Georgia's unemployment insurance statute is the Employment Security Law, O.C.G.A. Title 34, Chapter 8. It sets the weekly benefit amount, qualifying wages and disqualifications. It could not be deposited: the O.C.G.A. public access site puts every section behind a CAPTCHA, and no session law restates those sections. Georgia has no TANF or state supplement text in the Secretary of State's rules either. The Department of Human Services rules (Department 290) have no TANF chapter.

The Department of Labor's own rules on claims are published openly by the Secretary of State. They state most completely what a claimant must do, and by when, so they are the benefits half of the Georgia sample.

## Edition

Rules 300-2-4-.01 to -.13, as published at https://rules.sos.ga.gov/gac/300-2-4 and retrieved on 2026-10-24. The page shows no currency date and no administrative history.

Encoded:
- Rule .02 (registering for work);
- Rule .03 (weekly certification, work search, reporting, good cause);
- Rule .08 (overpayments and waiver).

## Checks

| file | errors | warnings | assertions | satisfied |
|---|---|---|---|---|
| `ga-ui-claimant.l4` | 0 | 0 | 0 | 0 |
| `ga-ui-claimant-cases.l4` | 0 | 0 | 38 | 38 |

Three `#TRACE`s cannot be asserted on the stable `l4`. Each has an `-- expect:` line, and each gave the outcome it says:
- the registration breach;
- the weekly-request breach;
- the repayment still owed after a late waiver application.

## Seat

**The claimant**: an individual who has filed a total or part-total claim for regular unemployment insurance benefits. Their questions are:
- must I register for work;
- can I still ask to be paid for this week;
- will I have to reopen my claim;
- do my benefits stay payable on my work search;
- will my late report be accepted;
- can I apply for a waiver of an overpayment;
- can it be waived;
- is collection suspended;
- by when must I appeal.

The Department and the Commissioner appear only for what they must give the claimant: a written waiver decision, and a pause in collection.

## Defaults followed, and departures

- **Scope.** The followed default would be the Act alone. **Departure:** the Act is not deposited, so this baseline encodes the rules adopted under it. The amounts the Act sets are out of scope, not guessed.
- **Actors.** The ones the text names: the claimant, the Department and the Commissioner.
- **Judgments.** Judgments left to the Department are answered conditionally:
  - "for reasons found to constitute good cause ... may be permitted" (Rule .03(3));
  - the extension of the 15-day waiver limit "upon a showing of extenuating circumstances" (Rule .08(3)(b)1);
  - "satisfactory evidence" of hardship (Rule .08(3)(d)3);
  - the Commissioner's waiver decision.
- **Definitions.** "Immediate family member" (Rule .03(3)(b)(ii)) and the fault test (Rule .08(3)(d)2) are worked out from facts.
- **One case.** One claim, one benefit week, one overpayment notice.

## Scope

In scope:
- Rule .02(2), (4);
- Rule .03(1)(a)-(c), (3);
- Rule .08(1), (3)(a), (b)1, (c), (d), (e) (as the facts the claimant must show), (g).

Out of scope:
- Rule .01 beyond context;
- Rule .02(3) referrals beyond the rule text, and (5)-(6);
- Rule .03(2) (employer-filed claims) and (4) (appeal limits in Chapter 300-2-5, not deposited);
- Rules .04-.07 and .09-.13;
- Rule .08(2) (collection methods), (3)(b)2 (the Covid-19 special rule: `not covered`), (3)(f), (h), (i) and (4);
- every amount: the weekly benefit amount, the maximum, and the base period, all in O.C.G.A. 34-8, not deposited.

## Questions exported

9 questions, each with `@export` and `@desc`, in four `§§` groups. Two of the groups are marked as situations: "only if you missed a date the department set for you to report" and "only if the department has sent you a Notice of Overpayment".

## Regulative rules

There are 3 `DEONTIC` rules:
- **Rule .02(2).** I must register within the time the Department directs. The number of days is an input. Breach: ineligible for the weeks the requirement is unmet.
- **Rule .03(1)(a).** I must request payment for a week within 14 days after it ends. Breach: ineligible for that week.
- **Rule .08(1), (3)(b), (g).** This is a sequence:
  - I may apply for a waiver within 15 days (DO ... LEST: if I don't, I must repay);
  - the Commissioner must then notify me in writing;
  - if the waiver is refused, I may appeal within 15 days (DO ... LEST: if I don't, I must repay).

## What the rules turn out to say (findings)

1. **The published cross-references are empty.** Rule .01 reads "as provided in GDOL Rule and report to the department on the claim as provided in GDOL Rule ." Rule .02(4)(b) reads "as described in Rule ;". Rule .02(6) reads "See GDOL Rule for the allocation". The rule numbers are missing from the Secretary of State's HTML itself, not lost in conversion. The deposited text keeps the gaps.
2. **The rules carry no amounts.** Everything a claimant receives is in O.C.G.A. 34-8, which is not deposited. The benefits half of the Georgia sample therefore answers "what must I do and by when", not "how much".
3. **"Two weeks after the end of such benefit week"** is read as 14 calendar days after the last day of the week. A request on that 14th day is in time; the 15th is late. "Must wait until a benefit week has ended" is read as: not on the last day of the week itself. Asserted.
4. **Good cause is open-ended.** Rule .03(3) defines good cause as "circumstances beyond the claimant's control, such as" three listed cases. A circumstance outside the list is good cause only if the Department so finds, and the encoding says that. Asserted (a car breakdown).
5. **A death waives the requirement; it is not merely good cause.** "The reporting requirements shall be waived for the day of the death and for four (4) consecutive calendar days thereafter" (Rule .03(3)(b)(i)). Within those five days nothing turns on when the claimant then reports. After them, a death is still a listed good cause, within the two-day window. Asserted both ways.
6. **The waiver window is 15 calendar days from the release date of the notice.** The appeal window is 15 days from the date the decision "was mailed or otherwise delivered". These are two different starting points. Asserted.
7. **Not applying for a waiver, and not appealing, are no breach.** They only leave the repayment owed under Rule .08(1), which sets no deadline for repayment. Asserted with `#TRACE` (a late application leaves the repayment owed).
8. **Collection is suspended while a waiver application is pending** (Rule .08(3)(c)). A waiver, once granted, does not bring back what was already collected, unless federal law requires a refund ((3)(h), not encoded).

## Before relying on it

- Deposit O.C.G.A. 34-8 (at least 34-8-190 to 34-8-197) from a source that permits it, and encode the weekly benefit amount and the disqualifications.
- Deposit Chapter 300-2-5 (appeals).
- Have the Secretary of State or the Department supply the missing rule numbers in the cross-references.
- Ask Michael to confirm the deposit despite the Fastcase all-rights-reserved footer (SOURCE-LICENSE.md).
- Run an independent test pass.
