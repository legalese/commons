# Higher Education Support Act 2003 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 104, compilation date 1 July 2026 (includes
amendments up to Act No. 17, 2025), register id C2026C00297, deposited at
`../../registers/source-bundle/C2004A01234.txt`. The deposit leaves out the
formulas that the Register prints as images. The formulas in ss 93-5(1),
140-25(1), 140-26(2) and 154-25(2) are missing from the .txt.

**Checks:** one module (`hesa-help.l4`) and one case file (`hesa-cases-help.l4`),
57 assertions satisfied, 0 errors, 0 warnings. One deliberately wrong expected value
was run as a check, and it failed as it should.

## Why this Act, and why scoped

This encoding answers requirement **REQ-0016** in `subjects/au/requirements.jsonl`
(priority 1). The three Western Australian cradle-to-grave lives raise it 5 times:

- Chloe **c030** (2021-02-22): Bachelor of Commerce at UWA on HECS-HELP. What is deferred, and when must she repay?
- Chloe **c045** (2024-10-20): first return, 2023-24, on $27,500. The scenario expects no HECS repayment because she is under the threshold.
- Chloe **c048** (2025-10-25): second return, 2024-25, on $71,500. The compulsory repayment.
- Daniel **d020** (2014-02-24): Bachelor of Commerce at UWA on HECS-HELP. What is deferred?
- Daniel **d022** (2017-02-27): Juris Doctor at UWA on FEE-HELP. Is a postgraduate law degree Commonwealth-supported?

The scope is the provisions those events name, plus the definitions, conditions and
exceptions needed to answer them:

- the Commonwealth supported student test (ss 36-5, 36-10);
- HECS-HELP (ss 90-1, 90-5, 93-1, 93-10, 93-20, 96-1);
- FEE-HELP (ss 104-1, 104-5);
- the HELP balance (ss 128-15, 128-20);
- the HELP debt and its 20% cut (ss 137-5, 137-10, 137-19A, 140-26);
- the accumulated HELP debt (ss 140-5, 140-10, 140-25, 140-30);
- compulsory repayment (ss 154-1, 154-5, 154-10, 154-15, 154-20).

Not encoded:

- allocation of places and grant amounts;
- OS-HELP, SA-HELP, STARTUP-HELP and VET FEE-HELP;
- re-crediting;
- overseas debtors;
- location-preferred debtors;
- assessments and PAYG.

Amounts that indexation or another instrument sets are **inputs**: the current-year
loan limit and maximum contributions, CPI and WPI, the thresholds after 2025-26, and
the Medicare levy outcome.

## What the Act turns out to say

### 1. The deposited repayment rule is the 2025-26 rule, and Chloe's 2024-25 repayment ran on a text that is not deposited

The compiled s 154-10 sets the minimum repayment income at "$67,000". Section
154-20 charges the least of three amounts:

- 15% of repayment income between that figure and $125,000, plus 17% above $125,000;
- 10% of repayment income;
- the repayable debt.

The endnotes show that ss 154-10, 154-20 and 154-25 were substituted ("rs No 30,
2025") by the Universities Accord (Cutting Student Debt by 20 Per Cent) Act 2025,
which commenced on 3 August 2025. Section 154-25(2) indexes both figures from the
start of each income year "after the 2025-26 income year".

*Inference:* the compiled text speaks to 2025-26 onward. The application provisions
(Sch 2 items 33, 34 of that Act) are not in the compilation.

Event c048 is the **2024-25** return. The scenario expects "marginal rate on income
above the threshold", but that is the new rule. The old rule for 2024-25 is not in
the deposit, so this encoding cannot answer c048 as the law stood. Read literally
against the compiled text, $71,500 gives $675 (15% of $4,500). The cap of 10%, which
is $7,150, does not bind. Asserted, together with a flag that the compiled text does
not cover 2024.

A second consequence: the $67,000 is printed in a compilation dated 1 July 2026, yet
for 2026-27 it has already been replaced by an indexed amount that the text does not
state.

### 2. The 20% cut is in the text twice, and the census date decides which debts it reaches

- **s 140-26:** for the accumulated HELP debt incurred on 1 June 2025, Step 7 cuts the former accumulated debt by 20% before indexation. This reaches debts incurred before 2025, such as Chloe's 2021-23 HECS-HELP debts. On the Act's own Lorraine figures, at a factor of 1.030, the debt is $13,364.25 in an ordinary year and $10,691.40 in 2024-25.
- **s 137-19A:** debts incurred "during the period beginning on 1 January 2025 and ending on 1 June 2025" are cut by 20%.

A HELP debt is incurred "immediately after the census date" (ss 137-5(3),
137-10(3)). *Inference:* this encoding reads that as the next day. On that reading,
a census date of 31 December 2024 falls inside the window and one of 1 June 2025
falls outside. Asserted.

Section 140-26(2) also substitutes a formula for 2024-25 that is missing from the
deposit, so it is not encoded.

### 3. Whether a Juris Doctor is Commonwealth-supported is not a question the Act answers

Under s 36-5, a student is Commonwealth supported only if two things hold:

- the provider has "advised the person in writing" that they are;
- the provider was not barred from saying so (s 36-10: a funding agreement, residency, the Student Learning Entitlement, a student identifier, and so on).

Postgraduate places for a Table A provider depend on the Minister's allocation for
designated courses (ss 30-10, 30-12). That allocation is an input here.

The Act does make three points definite:

- FEE-HELP is available only if the student is **not** Commonwealth supported (s 104-1(1)(d)).
- A postgraduate FEE-HELP loan carries no loan fee: the debt is "the amount of the loan" (s 137-10(2)(c)).
- An undergraduate FEE-HELP loan carries a fee of 25% for census dates before 1 April 2020 and 20% from 2023.

Daniel, not advised that he is Commonwealth supported, gets FEE-HELP. Advised that he
is, he gets HECS-HELP instead. Asserted.

### 4. A permanent resident can hold a Commonwealth supported place but cannot defer it

Section 36-10(2)(c) lets a permanent visa holder be Commonwealth supported. The
HECS-HELP list in s 90-5 covers only:

- citizens;
- permanent humanitarian visa holders and Pacific engagement visa holders;
- certain New Zealand special category visa holders.

An ordinary permanent visa holder is therefore Commonwealth supported but not
entitled to HECS-HELP. Asserted.

### 5. Without a student identifier, Chloe would not be Commonwealth supported at all

Sections 36-10(1)(f) and 104-1(1)(ga) require a student identifier in two cases:

- census dates in 2021-22, for students who commenced on or after 1 January 2021;
- every census date from 2023.

Chloe enrolled in February 2021, so she needed one. Without it the provider may not
advise that she is Commonwealth supported, and she gets neither HECS-HELP nor
FEE-HELP. Daniel's 2014 enrolment is outside the requirement. Asserted.

### 6. What is deferred, and when the repayment starts

The HECS-HELP amount is the student contribution amount less up-front payments
(s 93-1). It is capped at the HELP balance (s 93-20), as in the Act's Kate example:
$2,400 of contributions against a $2,000 balance gives $2,000. The Commonwealth lends
that amount and pays it to the provider (s 96-1).

The debt is incurred immediately after the census date. It is rolled into an
accumulated HELP debt each 1 June and indexed by the lower of CPI and WPI
(s 140-10).

Repayment is owed only when two conditions hold (s 154-1(1)):

- repayment income exceeds the minimum repayment income;
- the person had an accumulated HELP debt on the preceding 1 June.

Section 154-1(2) adds an exception: there is no repayment if no Medicare levy is
payable, or the levy is reduced under s 8 of the Medicare Levy Act 1986. Chloe's
c045 year ($27,500, nil levy) fails on both grounds. Asserted.

### 7. The text is the 2026 text, not the one Daniel enrolled under

Parts of the compiled text came after 2014 and 2017:

- The HELP balance condition in s 90-1(ba) has transitional provisions in the Higher Education Support Legislation Amendment (Student Loan Sustainability) Act 2018.
- The student identifier condition runs only from census dates in 2021.
- The endnotes record amendments to s 36-5 in 2020 and to s 36-10 in 2020, 2022 and 2024.

*Inference:* the Student Learning Entitlement and genuine-student conditions are among
those later amendments. This was not checked against the amending Acts.

The d020 and d022 answers here apply today's text to past facts. That is the right
shape but not the law as it stood. Not asserted as history.

### 8. Two formulas had to be rebuilt

The s 140-25(1) formula for the accumulated HELP debt is absent from the deposit.
*Inference:* it was rebuilt from the s 140-1(3) outline, the defined terms and the
Act's Paula example ($20,000 + $1,500 = $21,500).

The s 93-5(1) formula for the student contribution amount is also absent. That
amount is taken as an input.

## What would need doing before this is worth anything

- Deposit the 2024-25 text of Division 154, or the application provisions of the Universities Accord (Cutting Student Debt by 20 Per Cent) Act 2025, so that c048 can be answered as the law stood. The same applies to the 2014 and 2017 texts for Daniel.
- Recover the image formulas (ss 93-5, 140-25, 140-26(2), 154-25) from the Register.
- Take the indexed figures (loan limit, maximum contributions, thresholds after 2025-26) from the published indexation instruments.
- Encode s 8 of the Medicare Levy Act 1986 and the tax-law components of repayment income, so that s 154-1(2) and s 154-5 stop being inputs.
- Check the census-date boundary reading in finding 2 against ATO or departmental guidance.
