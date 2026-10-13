# Guardianship and Administration Act 1990 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 49107,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_49107.txt`. The deposit names no compilation
number. Its compilation table ends with the Births, Deaths and Marriages Registration
Amendment (Sex or Gender Changes) Act 2024 Pt 4 Div 9 (in force 30 May 2025); the last
reprint listed is Reprint 5 as at 5 March 2010. The uncommenced provisions table lists
the Acts Amendment (Consent to Medical Treatment) Act 2008 s 11 (so far as it inserts
ss 110RA, 110ZAA-110ZAC) and s 12, and the Assisted Reproductive Technology and
Surrogacy Act 2025 Pt 17 Div 10; neither is shown or encoded.

**Checks:** one module (`gaa-instruments.l4`), one case file
(`gaa-cases-instruments.l4`), 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0006** (priority 1), raised **8 times** by the three Western
Australian cradle-to-grave lives: Chloe **c025** (turns 18), **c082** (enduring powers of
attorney, "who may be an attorney?"), **c091** (enduring guardians, "what may an
enduring guardian decide?"), **c095** (an advance health directive at 70, "who may make
one; when does it operate?"); Jake **k092** (an enduring power of attorney and
enduring guardianship to Ruby after his stroke, "who decides for him if he cannot?"),
**k096** (a directive); Daniel **d085** (enduring powers of attorney and guardianship),
**d090** (a directive).

So the row takes the three instruments a person makes for their own future
incapacity — Part 9 (ss 104, 104B, 104C, 105, 106, 107), Part 9A (ss 110B-110G) and
Part 9B (ss 110P-110T) — with the s 3 definitions they use, the s 45 list of a plenary
guardian's functions and limits that s 110G(1) gives an enduring guardian, and the
orders of priority in s 110ZJ (treatment) and s 119 (other personal matters).

Not encoded: guardianship and administration orders and the Tribunal's procedure
(Parts 2-8); recognition of interstate and foreign instruments (ss 104A, 110O, 110ZA);
s 108 and most of s 109; the Tribunal's declarations and directions (ss 110J-110N,
110V-110Z); who is the "person responsible" (Part 9C, s 110ZD); urgent treatment and
abortion (Part 9D Subdivisions 1 and 3); medical research (Part 9E). The forms for an
enduring power of guardianship and a directive are prescribed by regulations, and
Schedule 3 (the enduring power of attorney forms) is not in the deposit; following the
form is an input. "Full legal capacity" and "unable to make reasonable judgments" are
not defined; both are inputs.

## What the Act turns out to say

### 1. Jake's instruments two months after his stroke stand or fall on his capacity, which the life does not state

Jake has a stroke on 2063-03-14 (k090) and gives an enduring power of attorney and an
enduring power of guardianship to Ruby on 2063-05-15 (k092). Each may be made only by a
person who "has reached 18 years of age and has full legal capacity" (ss 104(1a), 110B).
s 3 says a "mental disability includes ... an acquired brain injury". The Act does not
define full legal capacity, and the scenario does not say whether Jake had it. If he
did not, neither instrument exists: for treatment, s 110ZJ then passes over the
enduring guardian to a guardian (if any) and then the person responsible; for other
personal matters, s 119 names only a guardian.
Both readings are asserted. Ruby, at 30, is eligible to be appointed (ss 104C, 110D).
Asserted.

### 2. At eighteen, all three instruments switch on, not only Part 9

c025 lists only Part 9 (an enduring power of attorney at 18). The same test — 18 years
and full legal capacity — governs the enduring power of guardianship (s 110B) and the
advance health directive (s 110P). Chloe could make all three on 2021-03-14 and none
on 2021-03-13. Asserted.

### 3. The directive outranks the enduring guardian, whichever is made first

In all three lives the directive comes years after the enduring guardian is appointed
(Chloe 2063 then 2073; Jake 2063 then 2075; Daniel 2065 then 2074). For treatment the
person cannot judge, s 110ZJ(2) puts a treatment decision in a directive first; the
enduring guardian decides only if the directive does not cover the treatment (s
110ZJ(3)), and then only if authorised, reasonably available and willing. s 110T deals
with the reverse order: a later enduring power of guardianship does not by itself
revoke a directive. Either way the directive governs what it covers. This encoding
reads s 110ZJ(2) with s 110S, so a decision that does not operate does not take
priority (an inference). Asserted.

### 4. The duty to encourage advice cannot invalidate a directive

s 110Q(1)(b) makes a directive "not valid unless ... the maker is encouraged to seek
legal or medical advice"; s 110Q(2) then says validity "is not affected by a failure to
comply with subsection (1)(b)". The requirement has no consequence on the text.
Asserted.

### 5. An enduring guardian decides about the person, not the property

s 110G(1) gives an enduring guardian a plenary guardian's functions under s 45(1)-(2):
where and with whom the appointor lives, work, treatment, education, association, and
legal proceedings "except proceedings relating to the estate". s 45(3), (3A) and (4)
withhold voting, consent to adoption, marriage formalities, any decision about an
abortion, and making a will. The guardian has effect only while the appointor "is
unable to make reasonable judgments in respect of matters relating to his or her
person" (s 110F), and the power may narrow the functions (s 110G(2), (3)). Selling the
appointor's house is, on this reading, an estate matter for an attorney under Part 9
or an administrator, not a guardian (an inference). Asserted.

### 6. Who may be an attorney, and how the power is made

Any person 18 or over with full legal capacity (s 104C): in 2041 (c082) Liam (41) can
be Chloe's attorney; Oliver (10) and Ella (7) cannot. Nothing excludes a spouse or a
beneficiary. The instrument needs two witnesses, both authorised to take declarations
or one authorised and one adult who is not a donee or substitute donee (s 104(2), (3)),
and a statement of acceptance signed by each donee and substitute donee (s
104(2)(b)). Unlike Parts 9A and 9B, s 104 says nothing about the witnesses signing in
one another's presence. A donee may not renounce while the donor is legally incapable
except through the Tribunal (s 107(1)(c), s 109(2)); failing to keep records carries a
penalty of $2 000 (s 107(1)). Asserted.

### 7. A continuing power works now; a springing one waits for the Tribunal

The donor declares either that the power "will continue in force notwithstanding his
subsequent legal incapacity" or that it is in force only while a Tribunal declaration
under s 106 is in force (s 104(1)(b)). The first, on this encoding's inference, is in
force from execution; the second only after the Tribunal declares that the donor,
"by reason of a mental disability", cannot make reasonable judgments about the estate
(s 106(2)). Asserted.

### 8. A directive can stop operating without being revoked

A treatment decision operates only while the maker cannot judge the treatment, and
only in the circumstances it specifies (s 110S(1), (2)). It does not operate where
circumstances arise that the maker "would not have reasonably anticipated" and that
would have changed a reasonable person's mind (s 110S(3)); the matters to weigh
include the maker's age when the directive was made and when it would operate, and
the time between (s 110S(4)). Chloe makes hers at 70 and dies at 85; that weighing is
an input here. Asserted (operation and revocation, not the weighing).

## What would need doing before this is worth anything

- Retrieve the regulations that prescribe the forms for an enduring power of
  guardianship and a directive (ss 110E(1)(a), 110Q(1)(a)) and Schedule 3's Forms 1 and 2,
  which the deposit omits.
- Say who is "authorised by law to take declarations" (another Act) rather than taking
  a count as input.
- Encode Part 9C (the person responsible) and s 110ZIB, so s 110ZJ can name a person.
- Encode s 108 and s 109 (how an administration order or the Tribunal ends or varies a
  power), and the recognition sections for a life that moves between States.
- Read decided cases on "full legal capacity" before answering Jake's k092.
