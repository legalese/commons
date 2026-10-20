# Pay-roll Tax Assessment Act 2002 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. There was no first-pass encoding of this Act to replace.

## Edition

- **The Act:** Pay-roll Tax Assessment Act 2002 (No. 48 of 2002), WA consolidation
  deposited at `../../registers/source-bundle/mrdoc_42096.txt` (retrieved 2026-09-07).
- **Pay-roll Tax Act 2002** (No. 47 of 2002), s 5 and Part 3 Table item 1 (the rate).
  Deposited at `subjects/au/wa/pay-roll-tax-act-2002/registers/source-bundle/mrdoc_38731.txt`
  (retrieved 2026-09-07). The two Acts and the Taxation Administration Act 2003 are
  "to be read ... as if they formed a single Act" (s 3).
- **Pay-roll Tax Assessment Regulations 2003**, rr 5-6 (the one class of contract
  prescribed under s 9AA(1)(c)), version 03-j0-00, currency from 1 July 2022.
  Deposited at `subjects/au/wa/pay-roll-tax-assessment-regulations-2003/registers/source-bundle/mrdoc_45213.txt`
  (retrieved 2026-10-20). The thresholds are in the Act itself (s 8), not the
  regulations.
- **The formulas are missing.** The deposited text drops the formula images in
  ss 8(4), 10(2), 10(4), 11A(1)-(2), 12 and 17(3A), (5), and the rate formulas in
  Pay-roll Tax Act ss 6-11. Only their "where --" glosses survive. See finding 1.

## Checks

- One module (`prt-payroll.l4`) and one case file (`prt-cases-payroll.l4`).
- **44 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98.
- The case file is built by `gen_wa_pay-roll-tax-assessment-act-2002_baseline.py`
  in the session scratchpad. Every expected value was written by hand from the text,
  or from the inferred formula where the text drops one (those cases say
  INFERRED FORMULA).
- An expected value was deliberately altered in a scratch copy (41,250 to 41,251,
  two assertions). The runner reported both as failing (42 of 44), so it does catch
  a wrong expectation.

Facts the life does not state are **assumptions**, labelled in the case file:

- the three salaries ($95,000, $85,000, $75,000; with super at 12%, $285,600 a year
  and $23,800 a month);
- that all the work is done in Perth;
- that Daniel controls no other business, so Jarrah is a local nongroup employer.

## Seat

**The employer-founder.** In the lives this is Daniel, founding Jarrah Legal
Technologies Pty Ltd and hiring its first three employees. The Act makes the
employer liable (s 7(1)): "An employer who pays or is liable to pay WA taxable wages
is liable to pay any payroll tax payable on the wages." The employer is the company,
so Daniel asks on its behalf, as the person who decides what it does. The questions
are his: "Must my company apply to register?", "How much payroll tax must my company
pay for the year?". Where the Act speaks to the Commissioner (registration under
s 25, exclusion from a group under s 38), the encoding says what it means for the
employer.

The 2026-10-18 defaults:

- **The Act alone, plus instruments that set its numbers.** Followed. The Pay-roll
  Tax Act 2002 sets the rate and is brought in. The regulations set the one
  contractor class and are brought in. The thresholds are in the Act.
- **The actors the text names.** Followed: the employer, group members, the
  Commissioner, employment agents, directors.
- **Judgments handed to someone else are answered conditionally.** Followed. The
  Commissioner's exclusion from a group (s 38) and exemption from monthly returns
  (s 29) are inputs.
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed.
  "Wages", "WA taxable wages", "local nongroup employer", "group" and "controlling
  interest" are worked out. Borrowed terms are asked: employee, related bodies
  corporate (Corporations Act), fringe benefit and exempt benefit (FBTA Act), GST.
  **Departed from** in one place: "exempt wages" (Part 5) is the Act's own term but
  is asked as a single fact, because its 20-odd heads (charities, schools, local
  government, parental leave, apprentices) are not this seat's question.
- **One case is the text's natural unit.** Followed: one employer (or group) and
  one assessment year, or one month for registration and returns, or one payment
  for what counts as wages.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed.

## The lives

- **Daniel, d044 (1 June 2031, age 35):** "First three employees: ... no payroll tax
  yet". Decisions asked:
  - `How much of this payment is wages`: a month's salary ($7,000) and the super on
    it ($840) are both wages;
  - `How much of this payment is WA taxable wages`: the salary for work in Perth is;
  - `Which band am I in` for 2031-32: nil, because $285,600 is under the $1,000,000
    annual threshold; `Does my company pay payroll tax for the year`: no;
  - `How much payroll tax must I pay for the year` for the part-year to 30 June 2031:
    nil (the threshold apportioned to 30 days is about $82,192);
  - `Must I apply to register for payroll tax` for June 2031: no, because $23,800
    does not exceed the $83,333 monthly threshold; nor must Jarrah lodge a return.

  The other cases follow Jarrah as it grows: to $1,650,000 of wages, into a group
  with a consulting practice Daniel owns, and into a month over the threshold.

## Why this scope

The life asks one question: when does my company start paying payroll tax? The
answer turns on four things the encoding covers:

- what counts as wages, including super and fringe benefits, and whether
  contractors' payments do (they mostly do not; finding 2);
- which wages are WA's (s 6A);
- whether the company is grouped with other businesses, so that the threshold is
  shared (Part 4);
- the threshold, the taper and the rate (s 8, ss 10, 17, the Pay-roll Tax Act).

Then what it must do once it crosses: register within 7 days of the month's end,
lodge monthly returns and pay with them. Interstate employers, the monthly
progressive calculation, reconciliation and the valuation detail are left out:
Jarrah is a single-State employer far under the threshold in the life.

## What the Act turns out to say

1. **The deposit drops every formula.** The formula images in ss 8(4), 10(2), 10(4),
   11A and 17(3A) did not survive conversion, leaving only "where -- AT is the
   annual threshold amount ...". The encoding uses inferred formulas, labelled in
   the module: tapering value = AT / (UT - AT); deductable amount =
   AT - ((W - AT) x TV); apportioned amounts = amount x P / Y; and for a group, its
   WA share (W / TW) of AT - ((TW - AT) x TV). They are the simple forms the glosses
   allow, and each makes the deduction reach nil exactly at the upper threshold,
   where s 10(1)(b) takes over. They must be checked against the gazetted text.
   Asserted (as inferences).
2. **WA payroll tax has no general contractor provisions.** "Wages" reaches a
   contractor only through s 9AA(1)(c), a class of contract prescribed by
   regulation. The only class prescribed (reg 5) is a ship or boat builder's
   contract for persons providing mainly labour. Reg 6 excludes fixed-fee contracts
   for a result, award-covered contracts, and others. Payments through an employment
   agent are wages of the agent (s 9GA). A freelance developer's invoice to Jarrah
   is not wages. Asserted.
3. **Super and fringe benefits are wages.** Employer super contributions are wages
   (s 9CB(1)). So is the value of a fringe benefit, unless it is an exempt benefit
   under the FBTA Act (s 9BA). GST is taken out of a payment the payee charged GST on
   (s 9HB(1)), but not out of a fringe benefit (s 9HB(2)). Asserted.
4. **The threshold is $1,000,000 a year, tapering to nothing at $7,500,000**
   (s 8(1), (3)). At or below the threshold the tax is nil; at or above the upper
   threshold it is the rate on every dollar. Asserted.
5. **The rate is 5.5% for wages paid on or after 1 July 2023** (Pay-roll Tax Act
   s 5(4)). In the sliding scale period (1 July 2018 to 30 June 2023) it was also
   5.5% for wages up to $100 million, scaled for a part-year. Asserted.
6. **A group tests its Australia-wide wages against one threshold, and pays WA tax
   only on its WA share** (s 17(2)). Above the upper threshold the rate falls on all
   the group's WA wages. Asserted (the taper by inference, finding 1).
7. **Common control groups businesses, and a sole owner controls.** Two businesses
   with the same person holding more than 50% of each (s 33) constitute a group
   (s 32(2)). Daniel's 70% of Jarrah and a practice he owns outright would be
   grouped. Exactly 50% is not control. Asserted.
8. **The Commissioner may exclude a business from a group, but not a related body
   corporate** (s 38(1), (2)). Asserted.
9. **Every group member is liable for the group's tax** (s 7(2)): "a debt due jointly
   and severally by each person who is a member of the group". Asserted.
10. **Registration is monthly, not annual, for a stand-alone employer.** A nongroup
    employer must apply when a month's WA and interstate taxable wages together
    exceed $83,333 (s 24(1)). A group member must apply as soon as it pays any WA
    taxable wages (s 24(2)). Either way the application is due within 7 days after
    the month, on pain of a fine of up to $20,000. Asserted.
11. **Returns are due 7 days after each month, 21 days for June, and the tax is due
    the same day** (ss 26(3), 6). Asserted.
12. **The life's answer holds.** Three employees costing $285,600 a year are well
    under the threshold; Jarrah need not register and pays no payroll tax. Asserted.

## What would need doing before this is worth anything

- Recover the formula images (ss 8(4), 10(2), (4), 11A, 12, 17(3A), (5), and the
  Pay-roll Tax Act ss 6-11) from the gazetted or authorised PDF and replace the
  inferences.
- Check the tapered amounts against a RevenueWA calculator or ruling.
- Encode interstate nongroup employers (ss 13-16), the monthly progressive
  calculation (ss 11, 12, 19) and annual reconciliation (ss 16, 20).
- Encode Part 5 exempt wages head by head, at least parental leave (s 41A) and
  apprentices (s 41D).
- Encode tracing of interests (ss 34-37) and the DGE (s 39) for larger groups.
- An independent test pass and the human gates.
