# Commonwealth Electoral Act 1918 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive encodings (the `writing-l4-rules` skill was not available in the
session that wrote it). No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use.

**Edition:** Compilation No. 81, compilation date 1 July 2026, includes amendments
up to Act No. 16, 2025 (register id C2026C00260, in two volumes), as deposited at
`../../registers/source-bundle/C1918A00027.txt`.

**Checks:** one module (`cea-elections.l4`), one case file
(`cea-cases-elections.l4`): 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0003** in `subjects/au/requirements.jsonl`, priority 1, raised
**11 times** by the three Western Australian cradle-to-grave lives: Chloe c022
(turns 17: may she enrol?), c025 (turns 18), c031 and c047 (federal elections: must
she vote?), c084 (Oliver turns 18 and enrols); Jake k033 (turns 18: must he enrol?)
and k034 (neither enrols nor votes: what happens?); Daniel d021 (turns 18, enrols,
votes), d061 (nomination, the deposit, the checklist, disclosure), d063 (41% of
first preferences, the deposit, the return) and d070 (Luca turns 18 and enrols).

The encoding is scoped to those questions: ss 93, 99, 100, 101, 163, 164, 166, 170,
172, 173, 245, 287(9), 294 and 310A. The scenarios' own facts are cases (Chloe at 17,
19 and 22; Jake 246 days after turning 18; Daniel at 17 and at 44; a 41% vote).
Not encoded: the Rolls and Subdivisions, overseas, itinerant and Antarctic electors
beyond their exclusion from s 245, citizenship applicants (ss 99A, 99B), direct
enrolment (ss 103A, 103B) beyond its bar on proceedings, objections, polling,
scrutiny, registered parties, gift and expenditure caps, donation disclosure, every
Part XX return but a candidate's, and section 44 of the Constitution (a separate
subject). The value of a penalty unit and the indexed funding amounts (s 321) are
not in this Act and are inputs.

## What the Act turns out to say

### 1. There is no $20 penalty notice for failing to enrol

Jake's scenario (k034) expects "a penalty notice for failing to enrol" and puts $20
on it. The penalty notice and the $20 belong to s 245, and s 245 binds an
**elector**, which s 4(1) defines as "any person whose name appears on a Roll as an
elector". Jake is not on the Roll, so s 245 does not reach him: no duty to vote, no
penalty notice. What he commits is the s 101(4) offence (still not enrolled 21 days
after becoming entitled), an absolute-liability offence (s 101(6AB)) with "a fine not
exceeding 1 penalty unit" on conviction (s 101(6)). Section 101 has no penalty-notice
route. No proceedings may be brought once he sends a claim (s 101(7)) or the
Commissioner enrols him under s 103A or 103B (s 101(8)). Asserted.

### 2. Daniel cannot have voted at an election polled before his 18th birthday

d021 sits on Daniel's 18th birthday, 9 April 2014, and says he votes in the 2014
Senate re-run. Under s 93(3) and (4) a person who "has not attained 18 years of age
on the date fixed for the polling" is not entitled to vote and is not taken to be
enrolled for that election, even if on the Roll by a s 100 claim. The re-run's
polling day is not in the deposit. If it was before 9 April 2014 (outside
knowledge, not verified here), he could not vote at it. The rule at 17 is asserted.

### 3. The Commissioner cannot reject an unqualified candidate

s 163(2): a person not qualified "is not entitled to be nominated". But s 172(1)
says a nomination is rejected "if, and only if" ss 166, 167, 170 or 171 are not
complied with, and s 170A(3)(e) says the Commissioner has "no power to determine
whether ... the person is qualified". s 170(1A): a wrong answer on the
qualification checklist does not affect validity. A nomination that is in order is
accepted whoever makes it, and eligibility goes to the Court of Disputed Returns. A
missing checklist answer, a late deposit, or (s 170(1B)) a claim to have renounced a
foreign citizenship without the supporting documents does make it invalid. Daniel,
who renounced his Italian citizenship, must lodge those documents with the
nomination. Asserted.

### 4. "Provisional enrolment" at 17 is called something else, and it is optional

The scenario's "provisional enrolment" at 17 (c022) is, in the Act, a claim for "age
16 enrolment" (s 100): open from 16 to under 18 to a person who would be entitled if
18, which includes a month at the address (s 99(1)). This Act uses "provisional
enrolment" for applicants for citizenship (s 99B). Enrolling at 16 or 17 is a right,
not a duty: s 101(1) excludes a person entitled "by virtue of section ... 100". At 18
the duty arises only for a person not already on the Roll, so Chloe, enrolled at 17,
has nothing to do at 18 (c025). Asserted.

### 5. The $20 is written into the Act and not indexed, and religion is a reason

To keep a failure to vote out of court the elector may pay "a penalty of $20" (s
245(5)(c)(iii), (9)); the offence itself carries 1 penalty unit (s 245(15)).
Believing it a religious duty to abstain "constitutes a valid and sufficient reason"
(s 245(14)). No notice need go to a person absent from Australia on polling day (s
245(4)(b)). Asserted.

### 6. A pre-1984 British subject may vote but may not stand

s 93(1)(b)(ii) keeps the franchise for a non-citizen British subject who was on a
roll immediately before 26 January 1984. s 163(1)(b) requires a candidate to be "an
Australian citizen". Asserted.

### 7. The deposit is $2,000, flat; the return is annual

s 170(2)(b): $2,000, not indexed (s 321 does not list it). s 173: returned if
elected or on at least 4% of first preferences; in the Senate a grouped candidate
can rely on the group's sum. Daniel's 41% (d063) gets it back. The same 4% opens
election funding for an unendorsed candidate (s 294): $5 a vote, capped at accepted
expenditure above $10,000, both figures indexed and so inputs. The candidate's
return under Part XX Division 5 (s 310A) is annual: due "within 8 weeks of the end of
the calendar year", so for a 2040 candidacy by 25 February 2041 (hand count), and
not required if there were no gifts, no electoral expenditure and no Commonwealth
discretionary benefits, or if an endorsing party's return covers it. Candidacy ends
7 days after polling day (s 287(9)(b)). Asserted.

### 8. A long-term prisoner stays entitled to enrolment but may not vote

s 93(8AA) removes the vote from a person serving 3 years or longer; s 93(1) and (8)
leave the enrolment. That such a person has no duty to vote under s 245 is an
inference from s 245(4)(c) ("ineligible to vote"), not an express rule. Asserted as
the encoding's reading.

## What would need doing before this is worth anything

- Section 44 of the Constitution, which decides Daniel's candidacy, is a separate
  subject; nothing here checks it.
- The value of a penalty unit and the s 321 indexed figures come from outside this
  Act and have to be supplied.
- The 21-day boundary in s 101(4) ("upon the expiration of 21 days") is read as more
  than 21 days and not tested at the edge.
- Formal-defect leniency (s 172(2)), bulk nominations, Senate group funding, the
  disclosure threshold that starts a candidacy, Form DB itself (alterable by
  regulations), and the gift and expenditure caps that now bind candidates (Division
  3A, 3AB) are not encoded.
- No case law or AEC practice was consulted.
