# Electoral Act 1907 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else (the skill itself was not available in this session).
No pipeline, no coverage table, no independent test pass, no human gate. Not for
public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 47953,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_47953.txt`. The deposit names no compilation
number or compilation date. Its compilation table ends with the Electoral Amendment
(Names of Registered Political Parties) Act 2024 (No. 46 of 2024, in force
16 November 2024). The last reprint listed is Reprint 17 as at 9 December 2016.

**Checks:** one module (`ea-voting.l4`), one case file (`ea-cases-voting.l4`),
54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0013** (priority 1), raised **3 times** by the Western
Australian cradle-to-grave lives:

- Chloe **c024** (2021-03-13): "The State election, the day before her eighteenth
  birthday: too young by a day". The question is "Who may vote in a State election?",
  and the scenario cites s 17.
- Chloe **c046** (2025-03-08): "First State election". The question is "Compulsory?",
  and the scenario cites s 156.
- Jake **k045** (2029-03-08): "The State election: enrolled by then, does not vote;
  a fine". The scenario cites s 156.

The ledger names "s 156 (compulsory voting); s 17 (entitlement to enrol: 18)". So the
encoding takes s 17 (entitlement to be enrolled and to vote, including enrolment on
polling day), s 17AA (enrolment at 16 and 17), s 18 (people barred), and Part IV
Division 7 (s 155AB and s 156: the duty, the non-voters' list, the penalty notice, the
modified-penalty caps, the infringement notice, the offences, and removal from the
register). It also takes the definitions in s 4 (elector, election) and s 16C (whole
of State electorate).

Not encoded: administration, districts, the register and claims procedure, ss 17A,
17B and 17(4), s 18(1)(ca)-(cd), how votes are cast, nominations, polling, scrutiny,
s 156AA, and everything after it. The "prescribed period" for sending penalty notices
and the modified penalty the Commissioner actually sets are not stated in the Act and
are not encoded. The Act states only the caps.

## What the Act turns out to say

### 1. The 2021 election (c024) is judged against a text that did not yet exist

The deposit is the current compilation. Its history notes show that s 17AA (enrolment
at 16 and 17) was inserted by No. 30 of 2023 (Part 2 in operation 1 July 2024), s 16C
(the whole of State electorate) by No. 20 of 2021 (assented 24 November 2021), and
that ss 17, 18 and 156 were all amended in 2021 or 2023. The text in force on
13 March 2021 was not deposited. The outcome for Chloe would not change: s 17(1)(b)
("has attained 18 years of age") is old. But the route through s 17AA is anachronistic
for c024. Asserted on the current text only.

### 2. Chloe is too young by a day, and polling-day enrolment does not help

She was born on 2003-03-14. On 2021-03-13 she is 17: she is not entitled to be
enrolled under s 17(1). Even if she were enrolled at 17 (s 17AA in today's text), she
"is taken not to be an elector" and "is not entitled to vote" until 18
(s 17AA(2)). The polling-day enrolment route in s 17(2), (3) also needs s 17(1)(b).
That she attains 18 at the start of her birthday is an inference. The Act does not
say. Asserted.

### 3. Jake's "fine" is first a penalty notice, capped at $50

On the facts of k045 (enrolled, did not vote, no reason), the Commissioner must send
a penalty notice (s 156(4)). It offers three ways to keep the matter out of court:
show he voted, give a valid and sufficient reason, or pay a modified penalty. The
modified penalty may not exceed $50 for a first matter "under this section" and $75
otherwise (s 156(8)). His 2025 federal penalty under the Commonwealth Electoral Act
s 245 is not under this section, so the $50 cap applies. If he ignores the notice, an
infringement notice "may" follow (s 156(12), (13A)), with the same caps. Only after
that does a court come in, for a fine of $200 (s 156(16)). The scenario's "a fine" is
the end of a three-step path, not its start. Asserted.

### 4. The duty to vote is laid on an elector, not on a person entitled to vote

s 156(1): "An elector must vote", and s 4: "elector means a person who is enrolled".
A prisoner serving a year or more stays enrolled (s 18(2) does not list s 18(1)(c))
but is not entitled to vote (s 18(1)(c)). Read literally, s 156(1) still binds him.
The section's only relief is that the Commissioner "does not have to" send a penalty
notice to an elector who "was ineligible to vote" (s 156(5)(c)). Asserted literally;
flagged.

### 5. Absence from the State excuses the duty, and religious belief excuses the offence

s 156(1) excuses an elector "prevented ... by absence from the State" or by mental or
physical impairment on the voting days. The offence in s 156(16) is failing to vote
"without a valid and sufficient reason", which "includes an honest belief ... that
abstaining from voting is part of their religious duty" (s 156(1A)). The two lists
differ. The encoding reads the offence as needing the s 156(1) duty, which is an
inference. Chloe in 2025 (c046), enrolled and in the State, must vote. Asserted.

### 6. Section 156(14) cites a paragraph that does not exist

Paying an infringement notice bars proceedings "for a contravention of subsection
(16)(a)". But s 156(16) has no paragraphs in this compilation. The encoding reads it
as (16).

### 7. Not answering can cost the enrolment

At the end of an election the Commissioner must check whether a person who failed to
respond to a penalty or infringement notice still lives at the roll address. If
satisfied they do not, the Commissioner must remove the name, and a new claim is
needed (s 156(15), (15A)). Asserted.

### 8. The scenario's age for Chloe in c046 is off by one

The c046 title says "at 22". On 2025-03-08 Chloe, born 2003-03-14, is 21, as the
event's own `ages` field says. Asserted (`age in completed years`).

## What would need doing before this is worth anything

- Retrieve the compilation in force on 13 March 2021 and encode c024 against it.
- Encode the register and claims (Part III Division 2 onwards), so that "is enrolled"
  is derived rather than supplied, and s 17A, 17B and 18(1)(ca)-(cd).
- Retrieve the Electoral Regulations 1996 (WA) for the prescribed period and forms,
  and the Commissioner's practice on the modified penalty actually set.
- Search case law on "valid and sufficient reason" and on whether an ineligible
  elector commits the s 156(16) offence.
- An independent test pass.
