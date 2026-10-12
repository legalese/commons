# Civil Service College Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CSCA2001.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amending Act annotated is Act 5 of 2018 (Public Sector
(Governance) Act 2018, s 55, in force 1 April 2018). The arrangement of sections at
the top of the deposit is out of step with the body for Part 5; the encoding follows
the body (s 18 financial year, s 19 estimates, s 20 funds ... s 25 investment).

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0162** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act mostly constitutes a statutory board. What it decides for someone outside the
College is a handful of offences (ss 38-40), composition (s 41), the shield from
personal suits (s 16) and the bar on suing over its functions (s 13(3)). Those are
encoded, with what the College may award (s 14(1)(d)), the Board's size, resignation,
quorum and voting (ss 5(2), 7(2), 9), the financial year (s 18) and two provisions on
the 2001 transfer of Government employees (ss 32(4), 33). Not encoded: incorporation
and the seal, delegation and committees, the functions and powers lists beyond those
two points, staff (s 15), the other finance provisions, the property transfer and
existing contracts (ss 30, 34), pre-transfer misconduct (s 36), regulations (s 42) and
the saving (s 43).

## What the Act turns out to say

### 1. Copying the College's certificate titles is an offence only if they are identical

s 38(2) catches a symbol that is identical **or** "so resembles" the College's as to
deceive or confuse, or be likely to. s 39(2) has no resemblance limb: the offence is
issuing or using, or causing or permitting the use of, titles "identical with those of
the College". A training provider using a near-copy of a College certificate title
commits no s 39 offence on the text. s 39 is also fine-only ($2,000), where s 38 adds up
to 6 months' imprisonment. Asserted.

### 2. The secrecy duty follows former staff and protects outsiders' information

s 40(1) binds a person who "is or has been" an officer, employee or agent, a member or a
committee member, and covers information about the College, the Board "or any other
person" obtained in the course of duties — so a course participant's assessment is
covered. The exceptions are disclosure in performing duties, when lawfully required by
a court, or where required or allowed by written law. Maximum: $2,000 or 12 months or
both — twice the imprisonment for copying the symbol. Asserted.

### 3. You cannot sue the College for failing to perform its functions

s 13(3): nothing in s 13 imposes "any form of duty or liability enforceable by
proceedings before any court". The College can still be sued generally (s 3(a)); the
contract claim in the cases is the encoding's illustration of a claim s 13(3) does not
reach. And s 16 bars personal suits against officers, employees, members and persons
acting under the College's direction for anything done in good faith in executing the
Act or other written law. Asserted.

### 4. Composition is capped at $500 but depends on regulations not retrieved

s 41(1): the Chief Executive or an authorised officer may compound an offence
"prescribed as a compoundable offence" for not more than $500; on payment no further
proceedings are taken (s 41(2)). No regulations under s 42 were retrieved, so whether any
of the ss 38-40 offences is actually compoundable is unknown. Asserted (the cap and
the conditions only).

### 5. The College may award certificates but not degrees

s 14(1)(d): tests, examinations, "certificates, awards and other qualifications (other
than degrees)". Asserted.

### 6. Quorum is the higher of one-third and three, and the text is silent on fractions

s 9(1), with the Chairperson counting as a member (s 2). With the largest lawful Board
(Chairperson plus 15, s 5(2)) one-third is 5⅓; the encoding treats 5 present as short
and 6 as enough. That is an inference: the Act does not say how a fraction is handled.
Ties go to the casting vote of the person presiding (s 9(5)). Asserted.

### 7. Transferred civil servants keep their pension, pro rata, but cannot claim abolition of office

s 33: a person transferred under s 31 cannot claim a Pensions Act 1956 benefit on the
ground of retirement for abolition or reorganisation of office caused by the College's
creation. s 32(4) makes the Government liable for a portion of the pension; its wording
is tangled, and the encoding reads it as a pro rata split by pensionable emoluments (an
inference). Asserted.

## What would need doing before this is worth anything

- Retrieve any regulations under s 42, especially any prescribing compoundable offences.
- The College's actual symbol and certificate titles, and any case on what "so
  resembles ... as to deceive" means here, were not looked for.
- The s 32(4) reading and the quorum-fraction reading are inferences that need a lawyer.
- The Public Sector (Governance) Act 2018, which now governs much of the Board and the
  Chief Executive (ss 9(7), 11(2), 13(2), 15), was not read.
