# National Arts Council Act 1991 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The latest amending Act annotated in the text and the
Legislative History is Act 2 of 2020. Deposited at
`../../registers/source-bundle/NACA1991.txt`.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0188** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance (statutory boards,
institutions, government finance and pensions). The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is almost entirely about how the Council is set up. This row takes what an
artist, arts company, creditor or Council member actually meets: funding and fees
(ss 2, 6(2)(d), (h)), where the money may go (ss 12(4), (5), 13, First Schedule
para 11), who may be sued (ss 3, 24), size, terms and office-holders (s 4, First
Schedule paras 2, 3), disqualification and losing a seat (paras 8, 10), meetings
(para 12), the financial year and accounts deadline (Second Schedule), the
Government's pension share for transferred officers (s 20(3)) and pension moneys
out of creditors' reach (Third Schedule paras 1-4). Not encoded: the functions list
(s 5) beyond the definition of "the arts", patrons, ministerial directions, staff
appointments, shares (s 12A), the 1991 transfer of the National Theatre Trust and
its staff (ss 15-19, 21-23), temporary appointments, revocation and resignation, and
the pension-trustee provisions (Third Schedule paras 5-8).

## What the Act turns out to say

### 1. No one has a right to a grant, and the Act sets no eligibility test

s 6(2)(d) lets the Council "extend grants, contributions, loans or scholarships to
any person or organisation connected with the arts, subject to such conditions as
the Council thinks fit". There is no criterion, amount, residence or citizenship
condition, and no entitlement or appeal anywhere in the Act. Every rule for an
applicant lives in the Council's own conditions. The encoding can only say when
funding is permitted. That nothing makes it owed is an inference from "may" and from
the absence of any duty. Asserted (permission only).

### 2. The Endowment Fund's capital is locked, its income is not

s 13(4): the Singapore Arts Endowment Fund must not, without the Minister's prior
written approval, be applied "otherwise than as specified in section 12(2) and (3)",
which cover bank accounts and investment. So a grant out of Fund capital needs the
Minister's written approval. s 13(2) credits the Fund's income to the Council's
general funds, so a grant out of that income does not. The second step is an
inference from (2) and (3). Asserted.

### 3. The shield from suit is personal; the Council itself can be sued

s 24(1) bars proceedings against a member, employee or person acting under the
Council's directions for anything done "in good faith" in the execution or purported
execution of the Act. It does not mention the Council, which s 3 makes capable of
"suing and being sued". Bad faith, or acts outside the Act, lose the shield. Asserted.

### 4. Having once compounded with creditors disqualifies, with no time limit

First Schedule para 10(b) disqualifies a person who "is an undischarged bankrupt
or has made any arrangement or composition with his or her creditors". Bankruptcy
stops counting on discharge, but on the words an arrangement made at any time still
counts. Para 10(c) disqualifies a conviction for dishonesty, fraud or moral turpitude
unless a free pardon has been given, with no spent period. Missing 3 consecutive
meetings without leave vacates the seat (para 8(b)). Asserted.

### 5. A quorum is "half" the members, with no rule for an odd number

Para 12(2): "a quorum consists of half the total number of members appointed for the
time being". With 15 members appointed, half is 7.5. The encoding reads the rule as
at least half, so 8 are needed. That reading is an inference. Ties go to the casting
vote of the Chairperson, or of whoever presides (para 12(3)). Asserted.

### 6. Members may be paid, but never by way of profit

s 12(4) bars any dividend, bonus or other profit payment to members. First Schedule
para 11 still pays them "salaries, fees and allowances as the Minister may
determine". s 12(5) preserves good-faith pay for employees. Asserted.

### 7. Smaller points

- The Council has 11 to 27 members (s 4(1)), each for up to 3 years with no limit on
  re-appointment. The Chief Executive may be a member but not Chairperson or Deputy
  (First Schedule paras 1(3), 3(1)). Asserted.
- Financial year 1 April to 31 March. Audited statements reach the Minister by
  30 November (Second Schedule). Asserted.
- Under s 20(3), the Government's share of a transferred officer's pension is split
  by pensionable **emoluments**, not by years of service. Asserted.
- Third Schedule: s 20 scheme moneys are out of reach of creditors and the Official
  Assignee, except for debts owed to the Council or the Government. Asserted.
- The deposit's arrangement of sections misnumbers Part 5. It prints "Transfer of
  assets and liabilities" and "Existing agreements" with no number, puts "15." against
  "Pending legal proceedings", and leaves "22." and "23." blank. The body runs from
  s 15 (transfer) to s 23 (misconduct before transfer). The encoding follows the body.

## What would need doing before this is worth anything

- The Council's actual grant conditions, which are where an applicant's rules live,
  were not retrieved. Nor were the s 20 pension scheme rules, any subsidiary
  legislation or any case law.
- The Public Sector (Governance) Act 2018 governs ministerial directions and the
  Chief Executive here. It was not read.
- The quorum reading for an odd number needs a source.
