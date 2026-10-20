# Wills Act 1970 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 49116,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_49116.txt`. The deposit gives no compilation
number. Its compilation table ends with the Legal Profession Uniform Law Application
Act 2022 s 424 (in force 1 July 2022); the last reprint it lists is Reprint 5 as at
10 July 2015. One amendment is uncommenced and not shown: the Assisted Reproductive
Technology and Surrogacy Act 2025 Pt 17 Div 15.

**Checks:** one module (`wills-making.l4`) and one case file
(`wills-cases-making.l4`): 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0003** (priority 1) in `subjects/au/wa/requirements.jsonl`.
The three Western Australian cradle-to-grave lives raise it 9 times:

- Chloe: c025 (turns 18: s 7), c082 (wills: ss 8, 13), c087 (her father's will:
  ss 8, 13), c096 (Liam dies: s 8), c098 (Chloe dies: s 8);
- Jake: k084 (his father's will leaves everything to his mother: does he take
  anything?);
- Daniel: d074 (his father's Australian will and a house in Calabria), d085 (a will
  with a testamentary trust), d086 (his mother dies with a will).

The scope is those provisions and questions, plus what they need: s 6 (what a will
may do), s 11 (who cannot witness), s 10 (alterations), ss 14, 14A and 15
(revocation), the other routes to a formally valid will (s 17, s 20, Part XA, Part X
ss 32-33, Part XI s 40), and ss 26(1)(b), (g) and 27 (a beneficiary who dies first).
Not encoded: s 9, s 16, the construction rules other than s 26(1)(b), (g) and s 27,
Part IX, the Annex beyond one flag, ss 41-48 and s 50 (rectification).

## What the Act turns out to say

### 1. Section 13 is gone, and the deposit does not say what it was

Two of the lives (c082 and c087) ask about "s 13 (gifts to witnesses)". In the
deposit, s 13 appears only as "deleted: No. 28 of 2003 s. 211(1)". Its text is not
in the deposit, so this encoding does not say what it provided. Note 1 sets out
s 211(2) of the amending Act: the repeal applies to the will of anyone dying on or
after its commencement, which the compilation table gives as 1 July 2003. Every
death in the lives is after 2052, so the deleted section cannot apply to any of
them. Nothing left in ss 8 or 11 disqualifies a beneficiary as a witness. A will
witnessed by a beneficiary satisfies s 8 like any other will. Asserted (including a
fixture where a witness takes a gift).

### 2. Under 18, no will is valid, and the court cannot cure it

s 7: "Subject to section 17, a will made by a person under the age of 18 years is not
valid." s 17 saves only privileged wills made under the repealed s 18. There is no
exception for a married minor and no leave of the court. s 7 is not made subject to
Part X, so on the text a document the Supreme Court would accept under s 32 is still
invalid if its maker was 17. The court may not authorise a statutory will for someone
under 18 either (s 40(2)(b)). Chloe can make a valid will on 14 March 2021 (c025) and
could not on 13 March 2021. Asserted.

### 3. Two witnesses present together, and both able to see

s 8(c) requires at least 2 witnesses "present at the same time". s 11 says a person
"unable to see and attest that a testator has signed a document cannot act as a
witness". So a will with two witnesses, one of them unable to see, fails s 8. With
three witnesses, one unable to see, it passes. Nothing in s 8 calls for a form of
attestation. Asserted.

### 4. The Act decides form, not who inherits the Calabrian house (d074)

s 20 says only when a will "is taken to be properly executed": under the law of the
place of execution, domicile, habitual residence or nationality, or, for immovables,
under the law of the place where the property is (s 20(2)(b)). A Western Australian
will executed under s 8 is formally valid. Whether Italian forced heirship then
divides the house is a question of essential validity and choice of law, and this
Act says nothing about it. The scenario's `CASE` status for the Italian house stands.
The s 20 routes are asserted; the Italian question is not.

### 5. A child left out takes nothing under this Act (k084)

When a will leaves everything to the surviving spouse, the gift takes effect and the
Wills Act gives the child nothing. s 27 saves a gift only to "a child or other issue
of the testator" who dies first leaving children. A spouse who dies first is not
issue. On the encoding, a whole-estate gift to a spouse who has died is "not disposed
of by the will". Intestacy is the Administration Act, and any claim is the Family
Provision Act. Neither is in this Act. Asserted.

### 6. Equal shares to children: substitution, then accrual (c098)

If Oliver had died before Chloe leaving a child, s 27 would pass his half to his
surviving children. If he had died childless, s 26(1)(g) would accrue his half to
Ella's. A gift to a child as a joint tenant is outside s 27 (s 27(3)). Asserted.

### 7. Marriage revokes; divorce revokes; a spouse's death does not

s 14(1): marriage revokes a will unless it was made in contemplation of the marriage
(or is a qualifying appointment). Chloe and Liam's 2041 wills post-date their 2029
marriage, so s 14 does not touch them. s 14A(2): the ending of a marriage revokes the
will unless a contrary intention appears in it or is otherwise established. But
s 14A(3) lists only a divorce order taking effect, a decree of nullity, and a
recognised foreign dissolution or annulment. Separation does not end a marriage under
s 14A, and neither does the death of a spouse. s 14A applies only to marriages ending
on or after the commencement of the 2007 amendment. That date is taken as 9 February
2008, an INFERENCE from the table entry "Wills Amendment Act 2007 s. 324", read as
ss 3-24. Asserted.

### 8. What a will may do with a trust (d085)

s 6 lets a will dispose of property the testator is entitled to at death, exercise a
power of appointment, and appoint a guardian of an infant child. The Act never
mentions trusts. A gift to trustees is still a "disposition" (s 4), so (INFERENCE) a
testamentary trust falls within s 6(a). Its terms are general law. Whether a jointly
held home or a superannuation balance is property "to which at the time of the
person's death the person is entitled" is a question for the law governing that
property, so the encoding takes it as an input. Asserted only as to the categories.

### 9. The informal-will power is for the dead, and only since 2008

s 32 lets the Supreme Court accept a document as the will of "a deceased person", and
s 33(1) confines it to persons dying on or after the commencement of s 23 of the 2007
amendment (taken as 9 February 2008, as above). The encoding treats a living person's
informal document as not formally valid. Asserted.

## What would need doing before this is worth anything

- Retrieve the text of the former s 13 and the Acts Amendment (Equality of Status)
  Act 2003 Pt 62 to confirm the repeal date and what was repealed.
- Confirm the commencement of the Wills Amendment Act 2007 provisions (the table
  entry "s. 324" is garbled in the deposit).
- Read the uncommenced Assisted Reproductive Technology and Surrogacy Act 2025
  amendments, which will change this Act.
- Search case law on s 32 (informal wills), on s 7 and Part X, and on "in
  contemplation of" marriage.
- Encode the Administration Act 1903 and the Family Provision Act 1972, which answer
  the rest of k084, c087, c098, d074 and d085.
