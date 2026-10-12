# Republic Polytechnic Act 2002 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/4/2024"), as deposited at `../../registers/source-bundle/RPA2002.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the latest
amendment annotated is Act 4 of 2008 (Statutes (Miscellaneous Amendments) Act 2008),
annotated "wef 01/04/2024" and given a commencement of 1 April 2024 in the legislative
history. Section numbers follow the body of the Act, not the arrangement at the top.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0201** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short and mostly constitutional: it sets up the Polytechnic and its Board
and Senate. This row takes what a student, fee-payer, donor, lender or counterparty
meets: late-payment charges and their validation (ss 5(2)(c), 5A), who may receive a
diploma (s 12; Constitution s 1), who may end a student's studies (Constitution
ss 6(3)(c), 11(j)), when regulations take effect (Constitution ss 6(4), 12(2)), the
Students' Union (s 16; Constitution s 19), execution under seal (s 4), borrowing
(s 15), and the governance rules that decide whether a Board or Senate decision was
validly made (Constitution ss 2(5), 5, 7, 8, 9, 10), the financial year (s 14) and
donations (ss 17, 18). Not encoded: the general objects and powers, the Board's and
Senate's lists of powers beyond ending studies, examinations, grants, shares issued to
the Minister for Finance, officers' duties and estimates. The regulations made under
the Constitution (admission, fees, discipline) were not retrieved.

## What the Act turns out to say

### 1. A 2008 amendment came into force in 2024, and it validated every earlier late-payment charge

s 5(2)(c), the power to charge "for the late payment of any such fee or charge", and
s 5A both carry the annotation "[Act 4 of 2008 wef 01/04/2024]", and the legislative
history gives the Statutes (Miscellaneous Amendments) Act 2008 a commencement of
1 April 2024. s 5A deems every amount collected before that date "as, or purportedly
as" a late-payment charge "to be and always to have been validly collected", and "no
legal proceedings shall lie" over it. So a late charge collected on 31 March 2024 is
beyond challenge; one collected on 1 April 2024 stands or falls under s 5(2)(c) and the
Board's regulations, not s 5A. That the 2008 Act waited sixteen years is read from the
deposit's dates; why is not stated. Asserted.

### 2. Senate rules wait a semester; Board rules bite the day they are made

Senate regulations — admission, award conditions, courses, examinations, scholarships —
"come into operation not earlier than one semester after the day on which they are
made, unless otherwise approved by the Board" (Constitution s 12(2)). Board
regulations — which include student discipline, suspension and expulsion, and fees —
come into operation "on the day on which they are made unless otherwise provided by the
Board" (s 6(4)). Neither is subsidiary legislation (s 10(3) of the Act). Asserted.

### 3. Two bodies can end a student's studies, on different grounds

The Senate may "require any student on academic grounds to terminate his or her
studies" (Constitution s 11(j)); suspension and expulsion for discipline are for the
Board's regulations (s 6(3)(c)). Neither the Act nor the Constitution says a student
may be removed for not paying fees; the encoding returns "not settled by the Act" for
that ground, which is its own reading. Asserted.

### 4. Diplomas are not only for registered students

s 12(b) lets the Polytechnic open programmes to "persons who are not registered
students" and award them diplomas, certificates and other distinctions. That the
Senate's decision on who is qualified (Constitution s 11(g)) governs those awards too is
an inference: s 11(g) is not limited to registered students. Asserted.

### 5. A tied Board vote fails if both chairs are absent

The Board has 12 to 18 members (a Chairperson, a Deputy Chairperson, the Principal and
"not less than 9 and not more than 15" others) and a quorum of 6 (Constitution
ss 5(1), 9(2)). Decisions go by simple majority of those present and voting, with a
casting vote for the Chairperson "or, in his or her absence, the Deputy Chairperson"
(s 9(3)). If both are absent, an elected member presides (s 9(5)) but is given no
casting vote; the encoding reads a tie then as not carried, which is an inference.
The Senate's quorum is one quarter of its members and it must meet at least twice a
semester (s 10). Asserted.

### 6. The seal needs the Principal or a Deputy Principal, plus another Board member

s 4(2): sealed instruments "must be signed by the Principal or a Deputy Principal and by
another member of the Board". A Deputy Principal and the Principal will do (the
Principal is a Board member); the Chairperson and Deputy Chairperson together will not;
nor will a Deputy Principal with the Board's Secretary, who is an officer and not a
member (Constitution s 3(4)). Asserted.

### 7. The Students' Union is under the Societies Act, and students pay for it

s 16(1) applies the Societies Act 1966 to the Students' Union and its constituent bodies
"Despite anything to the contrary" in that Act, subject to a Gazette exemption by the
Minister for societies (s 16(2)). The Polytechnic may collect fees from "the students or
any class of students" for the Union and apply them "in any manner that the Polytechnic
thinks fit" for its purposes (Constitution s 19(3), (4)). Asserted.

### 8. The arrangement of sections is out of step with the body

The arrangement at the top of the deposit lists "2. Short title", "3. Interpretation",
and so on, one ahead of the body, where s 1 is the short title and s 3 establishes the
Polytechnic (as s 2's definition "established under section 3" confirms). The
encoding follows the body. Not asserted.

## What would need doing before this is worth anything

- The Board's and Senate's regulations (admission, fees and late charges, discipline,
  the Students' Union) were not retrieved; they are where a student's rights actually
  sit, and s 10(3) means they are not published as subsidiary legislation.
- The Statutes (Miscellaneous Amendments) Act 2008 was not read; the 1 April 2024
  commencement is taken from the legislative history.
- No case law was searched.
- The tie-vote and non-payment readings (findings 3 and 5) are the encoder's and need
  a lawyer's view.
