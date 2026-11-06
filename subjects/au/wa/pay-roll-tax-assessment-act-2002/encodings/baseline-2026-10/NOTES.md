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
- **Pay-roll Tax Act 2002** (No. 47 of 2002), s 5 and Part 3 ss 6 and 10 (the rate, with the sliding scale).
  Deposited at `subjects/au/wa/pay-roll-tax-act-2002/registers/source-bundle/mrdoc_38731.txt`
  (retrieved 2026-09-07). The two Acts and the Taxation Administration Act 2003 are
  "to be read ... as if they formed a single Act" (s 3).
- **Pay-roll Tax Assessment Regulations 2003**, rr 5-6 (the one class of contract
  prescribed under s 9AA(1)(c)), version 03-j0-00, currency from 1 July 2022.
  Deposited at `subjects/au/wa/pay-roll-tax-assessment-regulations-2003/registers/source-bundle/mrdoc_45213.txt`
  (retrieved 2026-10-20). The thresholds are in the Act itself (s 8), not the
  regulations.
- **The formulas.** The deposited `.txt` drops every formula of the Act (Word
  equation markup in the original), leaving only the "where --" glosses. All 25 are
  transcribed by hand from the authorised Word rendering of the same document
  (mrdoc 42096, fetched 2026-10-21) in
  `../../registers/source-bundle/mrdoc_42096.formulas.md`; those of ss 8(4), 10(2),
  10(4), 11A and 17(3A) are encoded. The rate formulas of the Pay-roll Tax Act
  ss 6-11 (the 2018-2023 sliding scale), also missing from that Act's deposit, are
  transcribed the same way from its Word rendering (mrdoc 38731, fetched 2026-10-21) in
  `subjects/au/wa/pay-roll-tax-act-2002/registers/source-bundle/mrdoc_38731.formulas.md`;
  the annual ones (ss 6(2), (3) and 10(3), (4)) are encoded. See findings 1 and 5.

## Checks

- One module (`prt-payroll.l4`) and one case file (`prt-cases-payroll.l4`).
- **46 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98 (re-run 2026-10-21 after the Assessment Act formulas, and again
  after the Pay-roll Tax Act sliding-scale formulas, were recovered).
- The case file is built by `gen_wa_pay-roll-tax-assessment-act-2002_baseline.py`
  in the session scratchpad. Every expected value was written by hand from the text,
  or from the recovered formula where the `.txt` drops one (those cases say
  FORMULA).
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

1. **The taper, from the recovered formulas.** The `.txt` lost every formula; the
   authorised Word text (`mrdoc_42096.formulas.md`) gives tapering value =
   AT / (UT − AT) (s 8(4)); deductable amount = AT − [(W − AT) × TV] (s 10(2)), or
   AAT − [(W − AAT) × TV] for a part-year (s 10(4)); apportioned amounts AT × (P / Y)
   and UT × (P / Y) (s 11A); and for a group (AT − [(TW − AT) × TV]) × (W / TW)
   (s 17(3A)). These are the forms the first version of this baseline had inferred.
   The deduction reaches nil exactly at the upper threshold, where s 10(1)(b) takes
   over. The s 13(3), (5) and s 17(3A), (5) equations are printed with an unmatched
   closing bracket; the only reading that parses is used. Asserted.
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
   5.5% for wages up to $100 million, scaled for a part-year. Above that the Pay-roll
   Tax Act s 6(2), (3) (s 10(3), (4) for a group) give, from the sidecar,
   [(5 500 000 × Y) + 0.06 (W − 100 000 000 × Y)] / W × 100 up to $1.5 billion × Y and
   [(89 500 000 × Y) + 0.065 (W − 1 500 000 000 × Y)] / W × 100 above, "to 4 decimal
   places" (read as rounding half up, an inference). $200 million in 2021-22 gives
   5.75% ($11,500,000 of tax); $3 billion gives 6.2333%. Asserted.
6. **A group tests its Australia-wide wages against one threshold, and pays WA tax
   only on its WA share** (s 17(2), (3A)). Above the upper threshold the rate falls
   on all the group's WA wages. Asserted.
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

- Encode the sliding-scale rates for progressive return periods (Pay-roll Tax Act
  ss 7, 9, 11; the s 7 formulas are transcribed in the sidecar).
- Check the tapered amounts against a RevenueWA calculator or ruling.
- Encode interstate nongroup employers (ss 13-16), the monthly progressive
  calculation (ss 11, 12, 19) and annual reconciliation (ss 16, 20).
- Encode Part 5 exempt wages head by head, at least parental leave (s 41A) and
  apprentices (s 41D).
- Encode tracing of interests (ss 34-37) and the DGE (s 39) for larger groups.
- An independent test pass and the human gates.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026, after the model of the Graffiti Vandalism Act 2016 encoding's seat layer (its design decisions D2, D4 and D8). The baseline's files are unchanged: the layer is added, nothing is replaced. Two new files:

- `prt-qa.l4` imports `prelude` and `prt-payroll`. It has 27 exported questions.
- `prt-qa-cases.l4` imports the same and `prt-qa`. It has 148 cases.

### Roles

`DECLARE Role IS ONE OF`:

- `I employ people, or pay directors, through my business (an employer)`: the baseline's seat, the employer-founder (25 questions, one for each baseline export).
- `I place workers with clients and pay them (an employment agent)`: the employment agent of s 4, taken to pay its placed workers' wages "as an employer" (s 9GA) (27 questions: the same 25, and 2 of its own).

Why: the Act puts the tax on "an employer who pays or is liable to pay WA taxable wages" (s 7(1)), and "employer ... includes ... an employment agent" (s 4). So every employer question is the agent's question too, and arises for both roles; only the agent's own two (am I an employment agent; what s 9GA makes my wages) are asked of the agent alone, and answer `does not arise for you` for the employer without reading anything else. The Commissioner is never a seat. The worker, who pays no payroll tax, is not one either, and a group member is a situation of either role rather than a seat. Every exported question takes `my role` IS A Role first, with `@desc Which of these describes you`.

### The situation input

One input, shared by both roles with one name, type and `@desc`, always second: `the kind of employer I am`, of type `Kind of employer`:

- `a local nongroup employer: not in a group, and paying taxable wages only in WA`
- `an interstate nongroup employer: not in a group, and paying taxable wages in WA and in another State or Territory`
- `a member of a group of employers under Part 4`

The Act ties each annual liability to one of these (s 4 "local nongroup employer", "interstate nongroup employer", "nongroup employer"; s 17 and s 7(2) for a group).

| Questions | Arise for | Does not arise for |
|---|---|---|
| `What is my annual threshold for the year`, `Which band of s 10 is my business in`, `What is my deductable amount for the year`, `How much payroll tax must my business pay for the year`, `Does my business pay any payroll tax for the year` (ss 10, 11A) | a local nongroup employer | an interstate nongroup employer; a member of a group |
| `Which band of s 17 is my group in`, `What is my group's deductable amount for the year`, `How much WA payroll tax must my group pay for the year` (s 17), `Can I be made to pay payroll tax owed on another group member's wages` (s 7(2)) | a member of a group | a local or an interstate nongroup employer |

9 questions take it. The other 18 arise in every situation: wages (Part 2 Div 2), WA taxable wages (s 6A), the grouping questions (ss 30-33, 38, which are how a business finds out whether it is in a group), the thresholds and the rate, registration and returns (Part 3), and the agent's two.

### Decisions

- **Q1. The agent is a seat although it is also an employer.** The brief's alternative, a single seat with the agent as a situation, would hide nothing, since every employer question is also the agent's. The second role lets the form show the agent's two questions only to agents, and states the s 4 inclusion in the role list. Michael may prefer one role.
- **Q2. An interstate nongroup employer gets no annual tax answer.** ss 13-16 are not encoded (baseline, "What would need doing"). For that value the s 10 questions answer `does not arise for you`, which is right (s 10 does not apply to it) but leaves the business with no answer. Said here so the form's silence is not read as nil tax.
- **Q3. The baseline's -1 is said in words.** The two tax-for-the-year questions answer `Tax for the year`: `tax of` the baseline's amount, or `not encoded: this assessment year` where the baseline answers -1 (a year before 2020-21). Every other answer is the baseline export's own, wrapped (`Yes or no`, `Amount`, `Days`, `Rate, if it arises`, `Band, if it arises`).
- **Q4. The grouping fact is asked twice.** `My month` (registration and returns) carries its own `I am a member of a group`, from the baseline; the layer does not change the baseline's record, so the form may ask it again beside `the kind of employer I am`. The two should agree; the layer does not check that they do.
- **Q5. s 9GA's condition is a helper in the layer.** The baseline counts an agent's payment as wages without asking s 9GA's condition, that the agent "receives payment ... in relation to the period during which the services are performed". The agent's question asks it first; if it does not hold the answer is `not wages under s 9GA`. Where it holds, the amount is the baseline's wages rule on a `My payment` built in the layer, with fixed placeholders, commented, for the four fields that rule does not read for an agent's payment. The s 4 definition of "employment agent" is also a helper (four facts).

### Not covered for the employment agent

- Whether the client, as well as the agent, can be liable (the Act says only that the agent is taken to be the employer, s 9GA); s 43 (agents and trustees); interstate placements (ss 13-16).
- Everything the baseline leaves out for any employer: Part 5 exempt wages head by head, the monthly progressive calculation, annual reconciliation, tracing of interests and the designated group employer.

### Cases

148 in `prt-qa-cases.l4`, all satisfied, with 0 errors and 0 warnings:

- 2 ask the agent's two questions for the employer, every other input ASSUMEd: `does not arise for you`;
- 24 ask each situation question, for both roles, with each value of `the kind of employer I am` under which it does not arise, the year, group year or membership ASSUMEd: `does not arise for you`;
- 28 assert that an answer equals the baseline export's on the same facts (every one of the 25 employer questions, three of them twice, and the agent's s 9GA amount);
- 2 mirror cases ask the same facts from both seats;
- 92 are worked by hand from the text (or from the recovered formulas, marked FORMULA), for both roles, on d044 and the baseline's fixtures (copied into the case file, since a case file cannot be imported without running its assertions).

Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset: `prt-qa.l4`, `prt-qa-cases.l4`, and the baseline's `prt-payroll.l4` and `prt-cases-payroll.l4` (46 of 46, unchanged) give 0 errors and 0 warnings; `l4 check prt-qa.l4` succeeds. A script listed every `@export` of `prt-qa.l4` with its inputs and checked that `my role` is first in all 27, that `the kind of employer I am` has one name, type and `@desc` in all 9 questions that take it, and that no input is DEONTIC or EVENT. A negative control (a wrong group tax, and the five interstate cases given a local nongroup employer with the year still ASSUMEd) gave 6 failures out of 148.
