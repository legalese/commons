# Home Team Science and Technology Agency Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/HTSTAA2019.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. It is marked as the informal consolidation in force from
13 January 2022. The latest amendment annotated in the text and in the Legislative
History is G.N. No. S 26/2022 (Variable Capital Companies (Consequential Amendments
to Other Acts) Order 2022, in force 13 January 2022). That Order added the company
and VCC director disqualifications to s 11(2)(d). The ARRANGEMENT OF SECTIONS at the
top of the deposit is column-shifted for ss 18-20 and 40-43. The encoding follows
the body's numbering.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0174** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

Most of the Act sets up a statutory board. This row takes the provisions that bind
or protect a person: the symbol offence (s 8), secrecy (s 31), personal immunity
(s 32), officers' and partners' liability for an organisation's offence (ss 40(2),
41(2)), and service of documents (s 42). It also takes the rules that decide
whether a member validly holds office and whether a decision was validly made:
size (s 9), disqualification (ss 11(2), 12(1), 14(3)), when appointment, removal
and resignation take effect (ss 10(3), 15(3), 16(2)), the term (s 18), losing office
(s 20), quorum and voting (ss 23, 25). Last, it takes who was moved across in the
2019 staff transfer (ss 44, 46(1), (2)).

Not encoded: establishment, functions and powers (ss 3-6), ministerial directions
(s 7), the Chairperson's term and the Deputy's powers, vacancies, validity of acts,
remuneration, meetings procedure, presiding, the seal, committees, the Chief
Executive and staff, the financial provisions (ss 33-39), the evidence rules in
ss 40(1) and 41(1), regulations (s 43), and the transfer of assets, liabilities and
records and the rest of the employees' protections (ss 45, 46(3)-(6), 47-49).

## What the Act turns out to say

### 1. A thin meeting can pass a resolution only if nobody objects

s 23 sets the quorum at one-third of the members, with no floor. s 25(3) passes a
resolution "if it is agreed by all members present without dissent, or if a majority
of the members who are entitled to vote on the matter cast votes in favour of it".
The encoding reads "members who are entitled to vote" as all members not prevented
from voting, present or not. On that reading, a 20-member Agency meeting with 7
present can act unanimously, but if one person dissents the other 6 votes are not a
majority of 20 and the resolution fails. s 25(4) presumes that a member present
voted in favour unless he or she expressly dissents. The reading of "entitled to
vote" needs a lawyer's view. Asserted.

### 2. Permission excuses only an identical copy of the symbol, not a look-alike

s 8(2)(a) makes it an offence to use a symbol identical to the Agency's "without the
prior written permission of the Agency". Limb (b), using a symbol that resembles it
closely enough to be likely to deceive or confuse, has no permission exception in the
words. A licensed partner who uses an adapted version of the logo is therefore caught
on a literal reading. Neither limb requires intent. The maximum is $10,000 or
6 months or both. Asserted.

### 3. Personal immunity needs reasonable care as well as good faith

s 32 protects members, committee members, the Chief Executive, employees and anyone
acting under the Agency's direction only for acts done "in good faith and with
reasonable care". A careless act done honestly is not protected. By contrast,
s 12 of the Defence Science and Technology Agency Act 2000 (sibling row) asks for
good faith alone. The Agency itself can be sued
(s 4(1)(c)). Asserted.

### 4. The secrecy duty is in the present tense and needs intent or negligence

s 31(1) binds "A member of the Agency, an employee of the Agency, the Chief Executive
or a committee member, who has information" that would not otherwise be available
to him or her. It does not say "is or has been", so whether a former employee is
bound is not said. The encoding asks only whether the person held the position when
the information came to them, which is an inference. The disclosure must be
"intentionally or negligently" made. Information that was already available to the
person in some other way is outside the section. A contractor's staff are not
listed. There are six exceptions, including prior authorisation and a court order.
The maximum is $2,000 or 12 months or both. Asserted.

### 5. A registered letter is served 2 days after posting even if it comes back

s 42(5)(c): service by prepaid registered post takes effect "2 days after the day the
document was posted (even if it is returned undelivered)". Email service is allowed
only with the person's prior consent (s 42(6)). Section 42 does not apply to court
documents (s 42(7)). For personal delivery, leaving and affixing, the Act does not
say when service takes effect. The encoding takes the day of delivery, which is an
inference. Asserted.

### 6. A director or manager can be guilty for failing to stop the company's offence

ss 40(2) and 41(2) make an officer, partner or influential manager guilty of the same
offence as the company, association or partnership. That applies if the person
consented, connived or conspired, was knowingly concerned, or "knew or ought
reasonably to have known" of the offence and failed to take all reasonable steps to
prevent it. This applies "whether or not the corporation is convicted" (s 40(5)).
For a business, the only offences under this Act are the symbol and secrecy offences.
Asserted.

### 7. Disqualification turns on sentence length, not on the kind of offence

s 11(2) disqualifies an undischarged bankrupt or someone who "has an arrangement"
with creditors, a Judge or judicial officer, anyone sentenced to 6 months or more
without a free pardon, anyone within a period of company or VCC director
disqualification, and anyone lacking capacity. There is no separate bar for a
dishonesty conviction. "Has an arrangement" is present tense, and the encoding
reads it as not covering an arrangement that has ended. The Chairperson must be a
member other than the Chief Executive (s 12(1)(a)). An acting appointee must not be
disqualified (s 14(3)). Asserted.

### 8. Removal needs no reason, and leaving office brings no compensation

The Minister may remove a member "at any time and without giving any reason"
(s 15(1)). The notice may not take effect before the member receives it (s 15(3)).
A member leaves office automatically after missing 3 consecutive meetings without
the Agency's approval, or after failing to disclose an interest once a notice of the
default has gone to the Minister (s 20(1)(f), (g)). s 20(2) says no compensation is
payable "for any reason". The term is at most 3 years (s 18); the encoding caps a
longer stated term at 36 months, which is a reading. Asserted.

### 9. The 2019 transfer was not a redundancy and paid nothing

s 46(2) says the transfer of Science and Technology Group officers on 1 December 2019
did not interrupt service, was not a retrenchment or redundancy, and gave no right to
any payment. Section 18A of the Employment Act 1968 does not apply (s 46(5)). Anyone
on the Minister's list of excluded individuals was not transferred (s 44). Asserted
(transfer and no payment).

## What would need doing before this is worth anything

- No regulations under s 43, and no case law, were retrieved.
- The Public Sector (Governance) Act 2018 governs directions, interests, the Chief
  Executive and meetings. It was not read.
- The readings in findings 1, 2, 4 and 8 need a lawyer's view, especially the
  denominator in s 25(3) and the rounding of a one-third quorum.
- The Official Secrets Act and other laws that may reach outsiders who disclose
  Agency information were not read.
