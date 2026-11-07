# Guardianship and Administration Act 2000 (Queensland) -- baseline encoding, the adult whose capacity for a claim is in question

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of this subject; nothing existing was touched. Seven files:

| File | What it holds |
|---|---|
| `gaq-common.l4` | dates (built-in date functions, no daydate), the regulative vocabulary and its EVALTRACE helper, sch 4 capacity, impaired capacity and paid carer, s 11, sch 2 ss 1, 2, 18; 4 questions |
| `gaq-appointment.l4` | chapter 3 and its neighbours: ss 12(1), (3), 13, 14(1)(b), (c), 15(2), (3), 21(1) (regulative), 26(1)(a)-(f), (2)(a), (3), 28(1), 29(1)(b), 31(2)-(5), 33(2), 155(1), (4), (6), 245 (with s 239); 14 questions |
| `gaq-administrator.l4` | chapter 4 remedies: ss 37, 47, 48, 54, 58, 59 (ss 59(5), (6) regulative), 60, 60A, 60C (s 60C(4) regulative), 152, 153; 12 questions |
| `gaq-tribunal.l4` | chapter 7 and chapter 11 part 4: ss 114B, 115, 118(1), (3), (5)-(7), 119, 123, 124(1), 125(1), 127(1), (2), 146, 147, 156-158, 163, 164, 247, 247A, 247C; 12 questions |
| `gaq-cases-appointment.l4`, `gaq-cases-administrator.l4`, `gaq-cases-tribunal.l4` | the worked cases (the gaq-common cases are with the appointment cases) |

Each exported question calls a rule defined beside it and named by section, so that a later seat layer (an
administrator, a family member) can import the rules. The three duties with a numbered deadline -- the administrator's
3 months to advise the registrar of titles (s 21(1)), and the applicant's 6 months to apply after a death (ss 59(5),
(6), 60C(4)) -- are regulative rules (`PARTY ... MUST ... WITHIN ... LEST BREACH ... BECAUSE`), run by `EVALTRACE`
inside exported questions that take only plain facts. Other periods (s 13 ages, s 28 reviews, s 118 notice, s 155
suspension, s 164 appeal) are date arithmetic.

## Edition

- **Act:** Guardianship and Administration Act 2000 (Qld), Act No. 8 of 2000 (`act-2000-008`), the version in force
  from 28 April 2026, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2000-008.txt` (text
  sha256 `2cf579740796434ee5bcf8240e42f2e27b685c7b88a81351ef301c82523f691f` per its `.meta.json`; a Windows checkout
  with CRLF line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the
  authorised PDF.
- **Numbers set elsewhere:** none needed. The Act's own numbers are used: 17 1/2, 18, 19 years and 5 years (s 13), 3
  months (ss 21(1), 155(4)), 5 years (s 28), 6 months (ss 59(5), (6), 60C(4)), 7 days (s 118(1)), 14 days (s 157(4)),
  28 days (s 164). No Guardianship and Administration Regulation is deposited; nothing encoded depends on one (the
  regulation prescribes special health care and recognised provisions, both out of scope).
- **Not deposited and not read:** the Acts Interpretation Act 1954 (Qld), which governs the counting of time; the
  readings taken instead are forks F1-F4. The QCAT Act and the Succession Act 1981, which ss 101, 115, 127(3), 163 and
  60(5) borrow from, are deposited as their own subjects but are not imported (the stable `l4` resolves IMPORT only
  within this folder).

## Checks

Stable `l4` of the L4 VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), from this folder, `JL4_LIBRARY_PATH`
unset, at most two at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `gaq-common.l4` | 0 | 0 | 0 | 0 |
| `gaq-appointment.l4` | 0 | 0 | 0 | 0 |
| `gaq-administrator.l4` | 0 | 0 | 0 | 0 |
| `gaq-tribunal.l4` | 0 | 0 | 0 | 0 |
| `gaq-cases-appointment.l4` | 85 | 85 | 0 | 0 |
| `gaq-cases-administrator.l4` | 55 | 55 | 0 | 0 |
| `gaq-cases-tribunal.l4` | 49 | 49 | 0 | 0 |
| **Total** | **189** | **189** | 0 | 0 |

Every exported question has cases, with the edges: the day before and the day of 17 1/2 and of 18 (s 13), a birthday
on 29 February and a month end that falls into February; the last day and the day after for each regulative rule, in
a common and a leap year; both deaths, with the first death setting the clock (s 59(6)); notice on the 7th day before
the hearing and on the 6th, with and without a reduced time (s 118); the later-of rule of s 164 across a year end and
into 29 February 2028; just over the s 60(4) cap; each "only if" limb on and off. Three `#TRACE` directives show a
breach of each regulative rule (the stable `l4` cannot compare a breached trace with `EQUALS`; the questions use
`CONSIDER ... WHEN FULFILLED`). Expected values were worked by hand from the text, never copied from output.

## Seat

**The adult whose capacity for a claim is in question** -- for example a person injured at work, on the road or by
medical treatment, with a brain injury or another impairment, whose compensation claim, settlement or damages award may
be run or managed by an administrator. "Do I have capacity for the claim, and must it be presumed? Is my claim a
financial matter? Can the tribunal, or the court approving my settlement, appoint an administrator, and who may it be?
What may my administrator do with the claim and the money, and can they be paid? When does the appointment end or get
reviewed? Can I get compensation from my administrator, and by when? Can I apply, take part with a lawyer, avoid costs,
get the decision and appeal? Can I get a declaration about my capacity to sign a release?" For ss 60, 60A and 60C the
seat is a person who takes from that adult's estate (a beneficiary or a personal representative); for s 59 after the
adult's death, the adult's estate; for ss 247-247C, a person (who may be the adult) who reports abuse or a contravention
to an official.

No seat is written for the tribunal (QCAT), the Supreme or District Court, the public guardian, the public trustee, the
public advocate or the registrar of titles. Their powers appear as what the person may ask for, what may be done to
them, and by when. An administrator seat (ss 33-60 from the administrator's side) and a family-member seat would be
natural further layers.

The 2026-10-18 defaults, all followed:

- **The Act alone.** No instrument sets a number the encoded sections use.
- **The actors the text names:** the tribunal, the court (the Supreme Court; in s 245 the Supreme or District Court; in
  s 59 any court), the administrator, the guardian, the public trustee, a trustee company, the registrar of titles, an
  interested person, an official (s 247(4)).
- **Judgments handed to others are answered conditionally:** every "is satisfied", "considers" and "suspects" of the
  tribunal or a court is an input, as are "interested person" (s 126 lets the tribunal decide it), "appropriate" (s
  14(1)(c)), "reasonable", "exceptional circumstances" and "honestly believes, on reasonable grounds".
- **The Act's own definitions are worked out from facts:** capacity and impaired capacity, paid carer, financial and
  personal matter, legal matter (sch 2 s 18, an "includes"), conflict transaction (s 37(2), (3)), active party (s 119),
  relevant person (s 156(7)), eligible person (s 163(3)), official (s 247(4)), reprisal (s 247A). **Borrowed or
  fact-like terms are asked:** bankrupt, health provider, residential service and service provider (Residential
  Services (Accreditation) Act 2002), trustee company, limitation order (s 110).
- **One case:** one adult and one matter (capacity is decided matter by matter).
- **The Act's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines and the choices.
- **Machinery out** (Scope).

## Scope

**In:** ss 11; 12(1), (3); 13 (its age gates and periods; the (1)(a)-(c) likelihoods as one fact); 14(1)(b), (c);
15(2), (3); 21(1) (the administrator's half); 26(1)(a)-(f), (2)(a), (3); 28(1); 29(1)(b); 31(2)-(5); 33(2); 37; 47;
48(1)-(3); 54; 58; 59; 60; 60A(1)-(3); 60C(1), (2), (4), (5); 114B; 115; 118(1), (3), (5)-(7); 119; 123; 124(1);
125(1); 127(1), (2); 146; 147; 152; 153; 155(1), (4), (6); 156; 157(4) (in an answer); 158; 163; 164; 239; 245; 247;
247A; 247C; sch 2 ss 1, 2, 18; sch 4 capacity, impaired capacity, paid carer, interested person.

**Out, and why:**

- Chapters 1, 2 and 2A (purpose, acknowledgements, the general and health care principles): guidance on how decisions
  are made, not a yes/no the claimant can ask; s 34 makes the principles binding on the administrator, and a breach
  reaches s 59.
- Chapter 3 provisions the claimant does not meet: ss 12A, 12B, 27A, 27B (missing persons), 13A and 80ZD (restrictive
  practices), 16-20 (the appointee's own advice, security and plan), 22-25 (enduring documents), 27, 30, 32-32B
  (withdrawal and notices between officials), s 26(1)(g), (2)(b), (2A), (4).
- Chapter 4 provisions with no yes/no for the adult, or reached already through s 59: ss 33(1), (3), 34-36, 38-46,
  49-51, 55-57, 60B. Sections 35 (honesty and diligence) and 50 (keep property separate) are offences whose breach is a
  "failure to comply with this Act" for s 59.
- Chapters 5, 5A, 5B (health care, sterilisation of a child, restrictive practices): health and disability decisions,
  not claims.
- Chapter 6 and chapter 7 part 1 (the tribunal's constitution, limitation orders), ss 121, 122, 126, 128-138A, 148-151,
  154, 155(2), (3), (5), 157(1)-(3), (5), 166-171; chapter 9 (the public advocate); chapter 11 parts 1, 2A, 4 (ss 248-249A,
  protections for officials and confidentiality duties of officials), 4A, 5; chapter 12 (transition). Section 247B (the
  offence) is named in an answer, not encoded.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 3 months of", "within 6 months after", "at least every 5 years", "not ... more than 3 months" (ss 21(1),
  28(1), 59(5), (6), 60C(4), 155(4)) -- `n months after` in gaq-common.l4 -- the same day number n months on, or the
  last day of a shorter month, and the act may be done on that day -- the Acts Interpretation Act 1954 (Qld) may count
  differently (not deposited).
- **F2** s 118(1) "At least 7 days before the hearing" -- `s 118(1) -- the last day for notice` -- notice on the hearing
  day minus 7 is enough (13 November for a 20 November hearing) -- 7 clear days, needing notice by the hearing day
  minus 8.
- **F3** s 164 "within 28 days after the later of" -- `s 164 -- the last day to appeal after a postponement` -- the
  later day plus 28 -- the same, with the day excluded and a closed-registry extension.
- **F4** s 13(1) "at least 17 1/2 years" -- `s 13 -- the day I turn 17 1/2` -- 210 months after birth (a birthday on
  29 February or a 31st falls on the last day of a shorter month) -- 17 years and 182 or 183 days.
- **F5** s 11(1) against s 11(3) -- `s 11 -- the presumption` -- the tribunal or court deciding capacity presumes capacity
  even while a declaration of impaired capacity is in force -- the declaration rebuts the presumption for them too.
- **F6** s 13(6)(b) "a period of not more than 5 years" -- `s 13(4)-(6) -- the latest end of the advance appointment` --
  the whole appointment, from the 18th birthday, so the latest end is the 23rd birthday -- 5 years more than the
  ordinary period (the 24th birthday).
- **F7** s 28(1) "(other than the public trustee or a trustee company ...)" -- `s 28(1) -- the next periodic review` --
  NOTHING (s 28 sets no periodic review for them; nothing says they are never reviewed) -- JUST "no review required".
- **F8** s 59(5), (6) while neither the adult nor the administrator has died -- `s 59(5), (6) -- the last day to apply`
  and `s 59(5)-(7) -- application in time` -- NOTHING and "s 59 sets no time limit" -- a general limitation period
  (outside the Act) applies.
- **F9** s 118(7) "failure to comply with the requirement to give notice to the adult" -- `s 118 -- notice to the adult`
  -- late notice is a failure to comply, so the hearing and decision are invalid -- only notice never given
  invalidates, and late notice is an irregularity.
- **F10** s 26(1), (2) as a closed list -- `s 26 -- automatic revocation` -- any other event leaves the appointment in
  place ("no: s 26 does not end it"), as "ends if" introduces the list and ss 27 and 31 are the other routes -- s 26 is
  silent on other events, which would answer NOTHING.
- **F11** s 37(3) "not ... merely because" -- `s 37 -- conflict transaction` -- a transaction whose only conflict is one
  of the (3) facts is not a conflict transaction -- a transaction with that fact and another conflict is one (encoded
  that way: the input asks whether it is the *only* conflict).
- **F12** s 13(1) with s 13(9) -- `s 13(1) -- advance appointment` -- not restricted to administrators; the answer is the
  same for a guardian for a personal matter -- s 13A governs restrictive practice guardians (out of scope).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **The settlement court can appoint the administrator itself, but only the Supreme and District Courts (s 245).** When
   one of them sanctions a settlement (including a compromise or taking money paid into court) or orders money paid to
   an adult it considers has impaired capacity, it has all the tribunal's chapter 3 powers. A Magistrates Court
   settlement for the same adult has no s 245 route; the tribunal must be asked under s 12. An out-of-court settlement
   that no court sanctions is not reached either. Asserted.
2. **Damages for gratuitous care do not make a family carer a "paid carer" (sch 4).** Limb (b)(ii) excludes
   "remuneration attributable to the principle that damages may be awarded by a court for voluntary services performed
   for the adult's care", so a parent paid from that head of the adult's damages can still be appointed administrator
   (s 14(1)(b)(i)) and keeps the appointment (s 26(1)(a)). Asserted.
3. **The 5-year cap on a longer advance appointment is ambiguous (s 13(6)(b)).** "A period of not more than 5 years" may
   be the whole appointment (from 18, so to 23) or the extension beyond 19 (to 24). Fork F6; the first is asserted.
4. **The public trustee and trustee companies escape periodic review (s 28(1)).** A claimant whose payout is managed by
   the public trustee gets no 5-yearly review; only a review the tribunal starts or someone asks for under s 29.
   Asserted (NOTHING).
5. **Two different time limits for neighbouring estate claims.** Section 60C(4) gives 6 months after the adult's death
   (extendable, s 60C(5)), while s 60(5) applies the Succession Act 1981 s 41(8), whose deposited text bars a hearing
   "unless the proceedings for such application be instituted within 9 months after the death", unless the court
   otherwise directs. A beneficiary who has both claims meets 6 months for one and 9 for the other. The 9 months is not
   encoded here (another subject); s 60C's 6 months is asserted.
6. **When both the adult and the administrator have died, ss 59(5) and (6) overlap.** Subsection (5) ("If the adult or
   appointee has died") reads on each death; (6) ("If the adult and appointee have died ... within 6 months after the
   first death") is taken as the specific rule. An application within 6 months of the later death but not the first is
   out of time unless extended (s 59(7)). Asserted.
7. **The presumption of capacity binds the tribunal and court even against a declaration in force (s 11).** Section
   11(3) lets "a person or other entity that performs a function ... under this Act" rely on a declaration of impaired
   capacity, but s 11(1) has no exception for the tribunal or court deciding capacity. Fork F5; asserted as read.
8. **Late notice of the hearing may invalidate the decision (s 118(7)).** The adult's notice is the only one whose
   failure invalidates the hearing and decision; whether "at least 7 days" late notice is such a failure is not said.
   Fork F9; asserted as invalid, unless the tribunal reduced the time (s 118(6)(b)) or excused notice (s 118(3)).
9. **Reprisal damages are outside workers' compensation (s 247C(6)) and have no time limit in the Act.** A worker
   dismissed for reporting abuse of an adult in care sues in tort, with exemplary damages available and no jury
   (s 247C(2), (3)); the limitation period is the general one, not encoded. Asserted.
10. **An appeal period is given only after a postponement order (s 164).** The ordinary period is the QCAT Act's (s 143(4)(b),
    28 days, not imported); s 164 runs 28 days from the later of the postponement's end and the reasons' date.
    Asserted.
11. **Only an applicant can be ordered to pay costs (s 127(2)).** The adult who is the subject of someone else's
    application bears only their own costs, whatever the circumstances. Asserted.

## Before this is worth relying on

- A lawyer's review of the forks, above all F2 and F9 (notice), F5 (the presumption) and F6 (the 5-year cap).
- Reading the Acts Interpretation Act 1954 (Qld) on the counting of time, and re-checking F1-F4.
- An independent test pass (a second reader writing cases from the text alone).
- A link, in a register outside the code, to the Succession Act 1981 s 41(8) (9 months, finding 5) and the QCAT Act s
  143 (28 days, finding 10), both deposited as their own subjects.
- Further seats: the administrator, and a family member applying for an appointment.
