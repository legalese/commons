# Health and Disability Services (Complaints) Act 1995 (WA) -- baseline encoding, the person making a complaint

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`hdsc-dates.l4`,
built-in date functions only, no daydate), the rules and the 19 exported questions in `hdsc-complaints.l4`, and the
worked cases in `hdsc-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act is a complaints scheme, not a compensation scheme: it sits
in the claims set (medical negligence and health) because a person harmed by a health or disability service often
complains to the Director before, or instead of, suing, and the Act decides what that complaint can do and how it
touches a later court claim. So the claimant here is the complainant, and the encoding follows a complaint from the
right to make it (Part 3 Division 1), through its time limit, screening and acceptance (Division 2), settlement and
conciliation (Part 3A), the decision after investigation and the provider's duty to report remedial action (Part 3C), to
what happens when court proceedings start (s 52), with the provisions that matter for a court claim: the inadmissibility
of the provider's response, settlement talk and conciliation (ss 36BA, 36C, 42), the bar on suing for breach of the
guiding principles (s 4(4)), and the duty of confidence (s 71). Three duties with deadlines are regulative rules run by
EVALTRACE inside exported questions: the complainant's (s 24, complain within 24 months; s 27(5), give further
information within the time fixed) and the provider's the complainant waits on (s 51, report remedial action within 45
days).

## Edition

- **Act:** Health and Disability Services (Complaints) Act 1995 (WA), Act No. 75 of 1995 (formerly the Health Services
  (Conciliation and Review) Act 1995), as compiled on the Western Australian Legislation website when retrieved on
  7 September 2026, including the amendments of the Health and Disability Services (Complaints) Amendment Act 2022
  (No. 35 of 2022), in operation from 27 July 2023: `../../registers/source-bundle/mrdoc_46372.txt`. The only uncommenced
  provision listed is the State Superannuation (Transitional and Consequential Provisions) Act 2000 s 75 (Schedule 2,
  not encoded).
- **Numbers set elsewhere:** none deposited. No regulations under s 77 are deposited: prescribed services (s 3 health
  service (h)), codes of conduct (s 77A), prescribed offences (ss 52B, 52H, 52R) and prescribed circumstances (s 71(1)(e))
  are asked as facts. The Act fixes its own periods and penalties.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 24 last day for an incident on 7 November 2024 asserted to be 8 November 2026) was
run once in a scratch file in this folder, since deleted, and showed "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hdsc-dates.l4` | 0 | 0 | 0 | 0 |
| `hdsc-complaints.l4` | 0 | 0 | 0 | 0 |
| `hdsc-cases.l4` | 0 | 0 | 178 | 178 |

Every exported question has cases, with the edges: the s 24 last day for an ordinary day, 31 December, 28 February, 29
February (in 2024 and 2000) and 1 March; a complaint on the day 24 months on, the day before and the day after, with and
without good reason, made and not yet made, and a complaint date before the incident; the regulative rule alone on day
0, the last day and the day after; further information on day 0, the last day and the day after; each ground of
rejection alone and in the order the text needs; each kind of person under ss 19-22 with each condition of s 20(2),
s 20(3) and s 22 failing in turn, and a relative with a financial interest; each path under s 34(4)-(5A); each deadline,
with extensions at, above and below the caps and a negative extension; the s 51 report on the last day and the day
after, with and without an extension asked for in time; each s 52 condition; each conduct in the penalty table, with
and without an excuse.

**No mirror cases.** One seat.

## Seat

**The person making a complaint** (`hdsc-complaints.l4`): the user of a health or disability service (the patient, the
person treated, the subject of research), or someone complaining for them (a representative, a carer, a provider),
who brings a complaint to the Director of the Health and Disability Services Complaints Office. "Can I complain about
this?", "By when must I complain?", "Will my complaint be rejected?", "What happens to it next, and by when?", "Can what
was said in conciliation be used in my court case?", "Can I sue for breach of the guiding principles?", "What is the
most a person can be fined for victimising me?".

The Director, the conciliator and the Minister get no seat: their opinions and decisions (good reason for delay,
vexatious, suitable for conciliation, recognising a representative) are asked as facts. The provider and the health care
worker under a prohibition order are parties the Act puts duties on; no seat was written for them here (see "Before this
is worth relying on").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number this encoding
  needs; the regulations that fill out definitions are not deposited and are asked as facts.
- **The actors the text names.** Followed: the user, the user's representative, the carer, the provider, the manager,
  the health care worker, the Director, the conciliator, the registration board.
- **Judgments handed to someone else are answered conditionally.** Followed. Every "in the Director's opinion", "if the
  Director is satisfied" and "the Director considers" is an input; so is "acted unreasonably" in s 25(1), which is for
  the Director to decide after investigation (s 48(1)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: health service and excluded service
  (s 3), user (s 3, including "not ... merely because he or she has arranged a health service"), relative (s 20(4)).
  Asked: carer (Carers Recognition Act 2004 s 4), applicable organisation and Carers Charter, code of conduct (regulations),
  registration board (Health Practitioner Regulation National Law), provider (an "includes" definition; the person
  complaining says who the provider is).
- **One case is the text's natural unit.** Followed: one complaint by one person about one matter.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 3 (health service, excluded service, user), s 4(4); ss 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 32A, 33(a),
34(1), (3)-(6), 35(1), 36A(3), (6), 36B(3)-(5), 36BA, 36C, 37(1), 39, 40(2)(a), 40(4), 41, 42, 43, 44(2), 50(2), 51, 52A(1),
52, 58; the offences a complainant meets, or is protected by: ss 21, 51, 52G, 52N, 52Q(2), 61, 62, 71, 72, 73 (and
s 36A(6), which says a provider's failure to respond is no offence).

**Out, and why.**
- Part 1 machinery (ss 1, 2, 3A, 5), s 4(1)-(3): the guiding principles guide providers and the Director's judgment of
  "unreasonable" conduct, which is an input; only s 4(4) speaks to the person.
- Part 2 (ss 6-18) and Schedule 2: administration of the Office.
- s 23: referral of complaints made to public providers under the Minister's administrative instructions, which are not
  deposited (the person's position is the same as a s 19 complaint, s 23(2)).
- ss 31, 32, 33(b), 35(2)-(4), 36, 38, 40(1)-(3), 44A, 45, 47, 48, 50(1), (2A), (3), (4), 52A(2)-(4): the Director's
  and conciliator's procedure, with nothing for the person to state or decide beyond what is encoded (s 32(2), referral
  only with the complainant's consent, is noted here and not asked).
- Part 3D (interim prohibition orders, prohibition orders, interstate orders) and Part 3E (public health warning
  statements), except the offences (ss 52G, 52N, 52Q) in the penalty question and the complaint grounds (s 25(1)(i)-(k)):
  these are addressed to the health care worker, a different seat.
- Part 4 (ss 59-67, the Director's powers) except the offences in ss 61 and 62; ss 56, 57 (reports to Parliament);
  ss 68, 68A, 68B, 69, 70, 71A, 74, 75, 76, 77, 77A, 78 (transitional, for services before 1996), 79, 79A, 80.
- No requirement-ledger entry exists for this Act in `subjects/au/wa/requirements.jsonl`, and none was raised: no
  scenario life has reached it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 24 "occurred more than 24 months before the complaint is made" -- `s 24 -- the last day to complain without
  showing good reason`, `s 24 -- is my complaint in time` -- a complaint on the day 24 months after the incident is in
  time; the next day is late -- the 24 months ending the day before that day.
- **F2** s 24, an incident on 29 February -- `24 months after` (hdsc-dates.l4) -- the period ends on 28 February two
  years on (the last day of the month, there being no 29th) -- it ends on 1 March.
- **F3** s 24 "the complaint is made" -- `s 24 -- is my complaint in time` -- the day the complaint is first made, orally
  or in writing (s 27(1)) -- the day an oral complaint is confirmed in writing (s 27(2)).
- **F4** s 19 lists who "may" complain without "only" -- `ss 19-22 -- may I make this complaint` -- a person the list does
  not name for the matter (a carer on a matter other than (h), anyone else on (a)-(h)) is answered NOTHING-kind, with the
  representative route pointed out -- JUST FALSE, Division 1 being the only conferral of the right to complain ("Right
  to complain conferred").
- **F5** s 20(1) "may recognize" -- the same function -- recognition is asked as a fact; an unrecognised person answers
  "not yet" (NOTHING-kind) -- the text's no.
- **F6** s 34(4)(a) "attempt to settle it in accordance with Part 3A Division 1" -- `s 34 -- what happens to my accepted
  complaint` -- open when the Director thinks the complaint suitable for Division 1 (the test s 34(4)(c)(i) and
  s 34(6)(b) use) -- open whatever the Director thinks.
- **F7** s 34(1) and (3) -- `ss 32A-52 -- the last day for this step` -- the s 34(1) extension is capped at 28 days; an
  extension under s 34(3) for a delay in getting information has no limit, so no last day is given (NOTHING) -- s 34(3)
  read as capped too.
- **F8** s 51(2), (3) -- `s 51 -- has the provider reported in time` and the deadline question -- an extension counts only
  if asked for within the 45 days, and never beyond 15 days -- an extension the Director grants on a late request
  counting all the same.
- **F9** s 52(1) "must, within 14 days, give written notice" -- the deadline question -- 14 days from stopping -- 14 days
  from becoming aware of the ground.
- **F10** s 52(3) "withdrawn or abandoned legal proceedings" -- `s 52 -- what happens to my complaint if proceedings are
  begun` -- only the legal proceedings of s 52(1)(a) -- also tribunal proceedings under s 52(1)(b).
- **F11** s 52(4) "Despite ... may refer that complaint for conciliation" -- the same function -- the Director must stop
  dealing with the issue but may refer the complaint for conciliation with both consents until the hearing begins --
  conciliation suspending the duty to stop.
- **F12** s 43 when the parties reach agreement in conciliation -- `s 43 -- after conciliation` -- NOTHING-kind (the Act
  sets no further step; s 41(3) has the Director stop once aware the complaint is resolved) -- the Director stops (s 41(3)).
- **F13** s 71(5)(d) and (b) -- `s 71 -- may I record, disclose or use this information` -- a person in none of the s 71(5)
  situations is answered NOTHING (s 71 does not reach them; the Act says no more) -- JUST TRUE.
- **F14** s 71(2) "Subject to subsection (1)(c), (d) or (e), the prohibition ... extends to the giving of evidence ... to a
  court" -- the same function -- in court only (c), (d) and (e) excuse; "in the course of duty" and "required or allowed
  by ... any other law" do not -- (b) still excusing a disclosure that another law compels in court.
- **F15** ss 24, 26, 27, 28, 30 order -- `ss 24-30 -- will my complaint be rejected` -- an excluded service first (s 26(3)
  keeps s 28 apart), then the "must reject" grounds (ss 24, 26(1), 26(2)), then the "may reject" grounds (ss 27(6), 30) --
  all grounds reported together.
- **F16** s 29(2) -- `s 29 -- if I withdraw my complaint` -- the Director's decision to proceed with a complaint on
  s 25(1)(i)-(k) is a fact; without it the Director must stop -- none.

Sites decided without a fork line: "means" definitions (health service, excluded service, user) answer the text's no when
they fail; s 20(3) ("is not to recognize ... unless"), s 20(2) and s 22 ("if"), s 39(1) ("may not ... unless"), s 43(1)
("must not ... unless"), s 52(1A) ("does not apply"), and the flat negatives of ss 4(4), 36BA, 36C, 42 ("not
admissible") answer the text's no; a matter outside s 25(1) is the text's no ("must allege"). The evidence question
answers NOTHING for statements made in an investigation or elsewhere: the Act is silent.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags in the s 19 question (F4, F5) and the s 43 question (F12), and NOTHING answers
in the deadline question (F7), the s 58 question, the evidence question, the s 4(4) question and the s 71 question (F13).
The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (s 24's 24 months, s 27(5)'s time fixed, s 51's 45 days) are regulative rules (`MUST ...
WITHIN`, `LEST BREACH`), run by EVALTRACE inside the questions; outside each period the answer is the consequence the
text gives (must reject, may reject, an offence).

## What the Act turns out to say

1. **"health service" joins its paragraphs with "and".** s 3 defines a health service as "any service provided by way of
   (a) ... and (b) ... and (ba) ... and (bb) ... and (c) ... and (d) ...". Read literally a service would have to be all
   of diagnosis, health care, dispensing, a screening programme and research at once. Read, as it must be, as
   alternatives. Asserted (each kind alone is a health service).
2. **The Act gives no compensation and no right to sue.** s 4(4): the guiding principles create no duty that may found
   an action for breach of statutory duty. What a justified complaint yields is the Director's notice of the action the
   provider ought to take (s 50(2)), the provider's duty to report what it did within 45 days (s 51, an offence), and a
   report to the Minister if it does not (s 52A). Negligence and other claims are outside the Act. Asserted.
3. **What is said in the complaint process is largely kept out of a later claim.** The provider's written response
   (s 36BA), anything said or admitted in negotiation (s 36C) and in conciliation (s 42) is "not admissible in
   proceedings before a court or tribunal". Nothing says the same of evidence gathered in an investigation. Asserted
   both ways.
4. **A participant cannot carry what they learned into court, unless the person it concerns authorises it.** s 71 binds
   participants in conciliation or investigation and people given notices (which includes the complainant who receives
   ss 33, 37 and 50 notices); by s 71(2) only exceptions (c), (d) and (e) reach evidence in a court, so "required or
   allowed by ... any other law" does not let a participant give it in a negligence trial; the written authority of the
   person the information relates to does (fork F14). Asserted.
5. **Two tests for a user who cannot complain.** A representative the user did not choose may be recognised if the user
   "is unable to complain ... and unable to choose a person to complain" (s 20(2)(a)(ii)); a provider may complain if,
   "because of the user's state of health or general situation, it would be difficult or impossible for the user to make
   a complaint" (s 22). The provider's test is the easier one. Asked as two facts.
6. **s 24 is not a limitation period for a claim.** It only obliges the Director to reject a complaint about an incident
   more than 24 months old, unless good reason is shown; the time limit for suing is in the Limitation Act 2005, not
   here. A complaint does not stop that clock (nothing in the Act says so). Noted, not asserted.
7. **s 58 saves some time limits and not others.** A failure to observe ss 33, 34(1), 35(1), 37, 40(4) and 50(2) does not
   affect validity; ss 32A, 36A(3), 36B(3), 44(2), 51 and 52(1) are not listed, and the Act does not say what follows. The
   s 58 question answers NOTHING for them. Asserted.
8. **A provider's failure to respond is no offence, but its failure to report remedial action is.** s 36A(6) says a
   provider that does not give a required response "does not commit an offence"; s 51(1) carries a penalty of $2 500.
   Asserted.
9. **Drafting and conversion slips (not law; not encoded):** s 52O(1) reads "As soon practicable" (missing "as"); the
   deposited text drops the hyphen in "Director-initiated" ("Directorinitiated"), and "decisionmaking" in s 4(1)(d); the
   compilation table cites the 2022 amending Act as "s. 343", where the section notes cite ss 4-43 of No. 35 of 2022.
   Sections are numbered out of order (s 36 follows s 36C; s 52 follows s 52U), as the Act's own amendments placed them.

## Before this is worth relying on

- The Health and Disability Services (Complaints) Regulations (prescribed services, codes of conduct, prescribed offences,
  prescribed circumstances under s 71(1)(e)), deposited and brought in.
- The Minister's administrative instructions under s 23, for complaints first made to a public provider.
- A provider seat (`hdsc-seat-provider.l4`) for ss 36A, 50, 51, 52A and 66, and a health care worker seat for Parts 3D and
  3E, drawing on the same rules.
- A lawyer's view on forks F1-F4, F11, F13 and F14, and on findings 3 and 4; an independent test pass and a human gate.
