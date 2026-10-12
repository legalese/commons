# School Boards (Incorporation) Act 1990 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SBIA1990.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. Its Legislative History lists Act 4 of 1990 and the 1991 and 2013
Revised Editions only. No amending Act is annotated.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0202** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet.

The Act has 16 sections and the row covers most of them: aided schools and the
founder's consent (ss 2, 7), what an order may hand to a board (s 3(4)(h), (i)),
varying a constitution (s 4), the seal and proof of documents (s 6), governors'
immunity (s 8), discontinuance (s 9), the Minister's takeover (s 10), winding up
(s 11) and deemed registration (ss 13, 14). Not encoded: the rest of s 3, the
list of powers in s 5, the contents of a winding-up order beyond s 11(2)(c), grants
(s 12), the Education Act saving (s 15) and transfers of property (s 16).

## What the Act turns out to say

### 1. The Act gives a board nothing over fees, admissions or staff: the order does

Parents dealing with a school board meet its control of fees, admissions and staff.
The Act does not confer any of it. s 3(4)(h) says only that a Minister's order
"may make provisions ... conferring upon the governing board full discretion" over
(i) recruitment, promotion, dismissal and discipline of teachers and staff,
(ii) "the policy or conditions for the admission of pupils ... and the dismissal of
pupils" and (iii) "the fees payable by the pupils"; (i) lets the order allow the
board to keep the fees. The curriculum is not on that list (though s 3(4) opens
"Without limiting subsection (1)"). No order was retrieved, so what any real board
may do is unknown here. Asserted.

### 2. There are no offences, no penalties and no rights of appeal for anyone outside

The Act creates no offence and no penalty. A parent, pupil or teacher gets no
remedy from it. The only person given a say is the board's chairperson, who
"may make representations to the Minister within 60 days" of a takeover notice
(s 10(2)). Not asserted (it is an absence).

### 3. A takeover needs 90 days' written notice, but representations close at 60

The Minister may appoint the Director-General to run a school where the board "has
failed to conduct the school efficiently" or the pupils' education "is not being
promoted in a proper manner", but only after "not less than 90 days' notice in
writing to the chairperson" (s 10(1), (2)). While the order stands, governors lose
the powers it covers (s 10(3)), and the Director-General's costs come out of the
board's own funds (s 10(4)). Counting the periods from the day of service is an
inference. Asserted.

### 4. Twelve months of takeover lets the Minister wind the board up

s 11(1) allows a winding-up order where discontinuance proposals were approved, the
school's registration under the Education Act 1957 is cancelled, or the
Director-General has run the school "for a period exceeding 12 months". The order
may require the board to give its staff notice terminating their contracts
(s 11(2)(c)). Exactly 12 months is not enough. Asserted.

### 5. Governors are shielded for good-faith acts and do not answer for the board's debts

s 8: no governor, merely by holding office, must contribute to the school's debts
or the costs of a winding up, takes any interest in the board's property, or can be
sued personally "for anything which is in good faith done or intended to be done"
in conducting the school or "in the execution or purported execution of this Act".
Bad faith, or an act outside both, is not covered. Asserted.

### 6. An aided school's founder can veto a board; a Government school's cannot

s 7: the Minister "must not establish a governing board" for an aided school unless
whoever established it agrees. The text sets no such condition for a Government
school (an inference from silence). Under s 4 the Minister must only "consult" a
board before varying its constitution: the board's objection does not stop it.
Asserted.

### 7. A school cannot just close, and a board's papers prove themselves

The board "must not discontinue the school except in pursuance of proposals approved
by the Director-General" (s 9). A document purporting to be under the board's seal,
or signed by an authorised person, is treated as the board's "without further proof
... unless the contrary is shown" (s 6(2)). The seal needs two governors present who
sign (s 6(1)); reading "2" as "at least 2" is an inference. Asserted.

## What would need doing before this is worth anything

- No order under s 3(1) for any school was retrieved: the board's actual powers over
  fees, admissions and staff depend on them.
- The Education Act 1957, which ss 11, 13, 14 and 15 lean on, is not encoded here.
- No case law was searched.
