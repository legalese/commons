# Civil Law (Wrongs) Act 2002 (ACT) -- baseline encoding, the person bringing a personal injury claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. The Act is large (450,321 characters, with a whole defamation code
and the professional standards scheme), so it is not encoded whole. Encoded: the personal injuries pre-court procedure
(chapter 5, nearly whole as it touches the claimant) and, from the rest of the Act, the provisions that decide whether a
claimant can sue, whom, for what, and how much is cut or capped: good samaritans and volunteers, apologies, survival of
actions, death claims, mental harm, terrorism and motor vehicles, precautions in negligence, part 7.1 exclusions and
presumptions, the earnings cap, domestic services, contributory negligence, proportionate liability (only to say a
personal injury claim is outside it), road authorities, institutional child abuse, and the cap on lawyers' costs.

No encoding of this Act existed, so this is a new baseline at `encodings/baseline-2026-11/`. Five files:

- `clwa-dates.l4` -- date helpers only (built-in date functions, no daydate, no `YMD`);
- `clwa-precourt.l4` -- chapter 5: 15 exported questions, four regulative rules (DEONTIC functions);
- `clwa-liability.l4` -- chapters 2, 3, 4, 7, 7A, 8, 8A and 14: 23 exported questions, one regulative rule;
- `clwa-precourt-cases.l4` and `clwa-liability-cases.l4` -- worked cases.

The duties with deadlines are regulative rules, run by `EVALTRACE` inside questions that take only plain facts:

- the claimant's notice of claim (`MUST give notice of claim WITHIN` the last day, `LEST` a continuing duty to give it,
  followed for the s 51 (3) period by a duty to give a reasonable excuse for the delay);
- the respondent's response under s 54 (`LEST BREACH` = conclusively presumed satisfied, s 54 (3));
- the respondent's duty to make an offer or settle within 6 months (s 61 (1)), `HENCE` the claimant's duty to answer the
  offer within 3 months (s 61 (4));
- the unincorporated body's 120 days to nominate a defendant (s 114D (3), as a `MAY`: when it passes unused the
  claimant's application under s 114E (1) (a) opens).

Time in those rules is counted in day serials (`DATE_SERIAL`), so a rule's deadline is the last day's serial.

## Edition

- **Act:** Civil Law (Wrongs) Act 2002 (ACT), A2002-40, Republication No 77 (R77), effective 16 May 2026, last amended by
  A2026-7, as deposited at `../../registers/source-bundle/A2002-40.txt` (converted 2026-11-06 from the register's DOCX,
  which the register marks as an unauthorised version; the authorised text is the register's PDF).
- **Commencement dates used:** division 8A.1A.2 (duty of organisations to prevent child abuse, ss 114BBB-114BBD) was
  inserted by the Civil Law (Wrongs) Amendment Act 2026 (A2026-7) s 10 (endnote 4), whose remainder commenced on
  16 May 2026 (endnote 3). The earlier Civil Law (Wrongs) (Organisational Child Abuse Liability) Amendment Act 2025
  (A2025-32, commenced 13 November 2025) inserted only pt 8A.1A, ss 114BB, 114BBA (then s 114BD), 114BC and 114BE.
  s 114BBB applies the division to abuse on or after 16 May 2026.
- **Numbers set elsewhere:** the Civil Law (Wrongs) Regulation 2003 (SL2003-20) is **not deposited**. Chapter 5 lets it
  prescribe the information and documents a notice must contain (s 51 (2)), excuses that are reasonable (s 51 (8)), and
  the periods for most steps; Chapter 14 lets it change the s 181 relevant amount ($10,000) and percentage (20%). Where
  the Act gives its own figure "if no period is prescribed" (or "if another amount is prescribed"), the Act's figure is
  used. A prescribed figure would change the answers (finding 3). Average weekly earnings (s 98) is an input.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read. Deliberately wrong assertions were run once in a scratch copy of each cases file, since deleted, and showed as
"assertion failed" (two in the pre-court file, one in the liability file).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clwa-dates.l4` | 0 | 0 | 0 | 0 |
| `clwa-precourt.l4` | 0 | 0 | 0 | 0 |
| `clwa-liability.l4` | 0 | 0 | 0 | 0 |
| `clwa-precourt-cases.l4` | 0 | 0 | 111 | 111 |
| `clwa-liability-cases.l4` | 0 | 0 | 146 | 146 |

Every exported question has cases, with the edges: the last day for a notice and the day after, each limb of s 51 (3)
deciding, month ends (31 May + 9 months = 28 February; 30 November 2027 + 3 months = 29 February 2028), across a year end,
a child whose legal disability ends at 18, the motor accident period; the respondent's month on its last day and the day
after, and from 31 January; a response a day late; the 1-month minimum to fix a notice on both sides; the 6-month offer
and the 3-month answer on their last days and the day after; every deadline step; a panel of 3, 2 and 1; 200 and 201
pages; age 15 and 16 for the presumptions; earnings at, below and just over 3 times AWE; reductions of 0%, 25% and
100% and a liability limit below, at and above the reduced figure, and a limit where no reduction is allowed; child abuse on 13 November 2025 and on 15 and 16 May 2026; the 120th day
after a proceeding started and the 121st; recoveries of $50,000 and $50,001 for the costs cap.

**No mirror cases.** One seat.

## Seat

**The claimant** (both modules): the person bringing a claim for damages for personal injury in the ACT -- the injured
person; after a death, a member of the dead person's family or the estate; for mental harm, the relative who suffered
it; for child abuse, the person abused as a child; for a child claimant, the parent or guardian who gives notice for
the child. "Does the pre-court procedure apply to me?", "By when must I give notice?", "Is my notice late, and what must
I add?", "Is the respondent taken to accept my notice?", "By when must the respondent answer me, or I answer it?",
"Must I see the respondent's doctor?", "Can I go to court yet?", "Whom can I sue for what the volunteer did?", "What can
the estate recover?", "Am I a member of the family?", "Can I get damages for my psychiatric injury?", "Is contributory
negligence presumed against me?", "How much of my earnings counts?", "How much are my damages cut?", "Is the
organisation taken to have breached its duty?", "What is the most my lawyer can charge?".

The respondent (the person sued, or its insurer), contributors, the organisation and the unincorporated body are named
as the text's actors; what they did is asked as a fact. No second seat was written: the respondent's duties appear as
what the claimant can expect and by when. The court and the taxing officer get no seat; their judgments are inputs.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed, except that the instrument that sets them
  (the Regulation) is not deposited: the Act's own fallback figures are used and the fact is recorded (finding 3).
- **The actors the text names.** Followed: claimant, respondent, the respondent's insurer, contributor, court, good
  samaritan, volunteer, community organisation, organisation, unincorporated body, lawyer.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs include: whether the court is
  satisfied of a reasonable excuse (s 62), of an urgent need (s 79), of an indictable offence and material contribution
  (s 94), that a case is exceptional (s 94 (2)); foreseeability and the reasonable person (ss 34, 43); the claimant's
  share of responsibility (s 102); whether the organisation proves reasonable precautions (s 114BBD); whether a role
  supplied the occasion (s 114BE); whether a period to fix a notice is reasonable (s 54 (2) (c)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: claim and the application of ch 5
  (ss 49, 50), member of a dead person's family (s 23), family member, parent and child for mental harm (s 32), act of
  terrorism (s 37), the s 51 (3) period, the respondent's required period (s 52 (6), s 54 (5)), apportionable claim
  (s 107B). Asked: legal disability (Limitation Act 1985), domestic partner (Legislation Act 2001), intoxicated (s 92,
  a matter of fact), community work and community organisation (ss 6, 7, fork F9), public or other authority (s 109,
  partly by regulation), consumer claim (s 107C, its ACL terms borrowed), average weekly earnings (ABS).
- **One case is the text's natural unit.** Followed: one claim by one claimant against one respondent (one death, one
  child abuse claim).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed, within the focus.

## Scope

**In.**
- Chapter 2: s 5 (good samaritans), ss 8, 9 (volunteers), ss 12-14 (apologies), ss 15, 16 (survival of actions).
- Chapter 3: s 23 (members of family), s 26 (amounts not deducted), s 27 (no reduction for contributory negligence in
  death claims, through s 102), ss 32, 34-36 (mental harm), ss 37, 38 (terrorism and motor vehicles).
- Chapter 4: s 41 (application), s 43 (precautions), s 47 (100% reduction, through s 102).
- Chapter 5: ss 49, 50, 51, 51A (deadline), 52, 54, 55 (3) (b) (deadline), 59, 60, 61, 62, 64 (deadlines), 66, 67, 68
  (deadlines), 71, 79.
- Chapter 7: ss 92-98 (part 7.1: exclusion for offences, the three presumptions, the earnings cap), s 100 (domestic
  services), s 102 (contributory negligence) with s 168 (3).
- Chapter 7A: ss 107B, 107C (whether a claim is apportionable).
- Chapter 8: ss 108, 109, 113 (roads).
- Chapter 8A: ss 114A, 114AA, 114BA, 114BB-114BBD (duty to prevent child abuse), 114BC, 114BE (vicarious liability),
  114D, 114E (nominated and appointed defendants for unincorporated bodies).
- Chapter 14: s 181 (maximum costs for claims of $50,000 or less).

**Out, and why.**
- Part 2.2 ss 10, 11 (the Territory assuming a community organisation's liability by the Minister's agreement, and
  directions about insurance): arrangements between government and organisations; whether an agreement is in force
  could be asked as a fact beside ss 8, 9. Part 2.4 ss 17, 18 (a cause of action against a person who died before or
  with the damage is taken to have existed; rights additional to part 3.1 and the Motor Accident Injuries Act 2019):
  tractable, could be added beside s 16.
- s 36 (2)-(6) (the court's directions where several family members sue, the action for all of them, damages
  proportional to the damage, and their division): the court's procedure and discretion; only s 36 (1) states who can
  claim.
- Part 7.3 ss 104, 105: s 104 (a third person's damages are reduced for the first person's contributory negligence, as
  for a s 36 claimant whose relative was partly at fault) could be added beside s 102 (the s 102 question takes the
  share as an input, so the first person's share can be entered there); s 105 is between wrongdoers.
- s 114D (3) "unless the court otherwise orders": no order is assumed; an order changing the 120 days is not taken as an
  input.
- Part 2.2A (food donors, s 11B) and part 2.5 (contribution between wrongdoers, ss 19-22): a narrow defence and rules
  between wrongdoers; tractable, could be added.
- ss 24, 25 (liability and damages for a death): they hand the amount to the court ("proportional to the damage");
  s 25 (4)-(6) (funeral and medical expenses) could be added beside s 16. s 33 (nervous shock no bar) and s 99
  (reference to earlier awards) state no test.
- ss 42, 44-46 (standard of care, other principles, causation, burden of proof) and ss 110-112, 114: principles the court
  applies, with no fact test a claimant could state beyond what s 43 and s 113 ask. s 48 (fraudulent claims): a remedy
  against fraud, not a claimant's question.
- Chapter 5: s 53, s 55 (1)-(3) (a) (adding later respondents needs a prescribed period, agreement or leave), s 56
  (multiple respondents), ss 57, 58, 69, 70 (respondents and contributors between themselves), s 63, s 65 (no
  obligation), ss 72-78, 80 (privilege, offences, use of undisclosed documents, enforcement).
- Chapter 7A beyond ss 107B, 107C, and chapter 8 beyond s 113: between wrongdoers, or principles for the court.
- Part 8A.2 ss 114C, 114F-114H (procedure once a defendant is nominated) and part 8A.3 (setting aside abuse settlement
  agreements: a court's discretion whose definition turns on the commencement of Limitation Act 1985 s 21C, which this
  text does not give).
- Chapter 9 (defamation, a code of its own), chapters 10, 11, 12 (other than s 168 (3)), 13, part 14.2 (lawyers'
  certificates), chapter 15 (mediation, the charge on insurance money, abolished actions, claim farming offences,
  machinery), the transitional chapters 19-22 (apart from the commencement date used), and schedules 1A-5.
- The Civil Law (Wrongs) Regulation 2003, the Legislation Act 2001 (how periods are counted, "domestic partner"), the
  Limitation Act 1985 (legal disability; its own encodings sit beside it), and the Motor Accident Injuries Act 2019 (the
  s 51 (4) days): not deposited here or not this Act. Asked as facts.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 49, s 50 (1) -- `s 50 -- does chapter 5 apply to my claim` -- a claim that is not for personal injury: NOTHING-kind
  (chapter 5 is limited to personal injury claims by its own wording, with no "only") -- JUST FALSE.
- **F2** "within 1 month after the day", "the day that is 9 months after" (ss 51-71) -- `the day ... months after` -- the day
  of the event excluded, ending on the corresponding day of the later month or that month's last day; a last day on a
  weekend or public holiday is not moved -- the Legislation Act 2001 (not deposited) may count otherwise or move the day.
- **F3** ss 51-71 "the period prescribed by regulation (or, if no period is prescribed ...)" -- every deadline -- the Act's
  own period -- a period in the Regulation, which is not deposited.
- **F4** s 60 (2), (3) -- `the counting day` -- every day a chapter 5 period counts from (accident, symptoms, lawyer,
  respondent identified, the s 51 (4) day) is moved to the day the legal disability ended if earlier -- only the accident
  day is replaced (s 60 (3) (a)), with the other limbs counted as usual.
- **F5** s 54 (5) (b) (ii) "the later of" (A) and (B) -- `s 54 -- is the respondent taken to be satisfied ...` -- one route is
  asked -- where both apply, the later day.
- **F6** s 54 (1), (3), a respondent that says nothing at all within the s 52 (1) month -- the same function -- treated as
  not giving a response within the required period: presumed satisfied -- s 54 never engaged (the respondent neither
  considered itself a respondent nor was told), so no presumption.
- **F7** s 61 (1) "make a written offer", s 61 (4) "after the day ... receives it" -- `s 61 -- where does the attempt ...` --
  the respondent's 6 months are met by the day the claimant receives the offer, and the claimant's 3 months run from that
  day -- the respondent's duty met on the day it makes (sends) the offer.
- **F8** s 51 (3) (b) before a lawyer is instructed -- `the s 51 (3) last day` -- limb (b) has not begun; the period ends on
  limb (a)'s day "as things stand" -- the period cannot be known until a lawyer is instructed.
- **F9** ss 6, 7 community work and community organisation -- `s 8, s 9 -- whom can I sue ...` -- asked as one fact -- worked
  out from the s 7 purposes and exclusions.
- **F10** s 23 "each of the following people is a member" -- `s 23 -- am I a member ...` -- read as closed: anyone else is
  the text's no -- NOTHING-kind (a list not closed by "only").
- **F11** s 37 (3) "whether or not subsection (1) (b) is satisfied" -- `an act of terrorism` -- dispenses with (1) (b)
  only; the cause in (1) (c) is still needed -- firearms or explosives make any (2) action terrorism.
- **F12** s 27 (2), s 102 (5) "subject to part 7.1" -- `s 102 -- my damages after contributory negligence` -- an unrebutted
  s 95-97 presumption reduces damages even in a death claim or for a breach of statutory duty -- "subject to" means only
  that part 7.1's exclusions and caps (s 94, s 98) still apply.
- **F13** s 16 (5) funeral expenses where the wrong did not cause the death -- `s 16 -- can the estate recover this` --
  NOTHING-kind -- recoverable as ordinary damages.
- **F14** s 262 "Division 8A.1A.3 applies to proceedings commenced but not finally decided before" commencement --
  `s 114BE -- is the organisation vicariously liable` -- s 114BE applies whenever the proceeding began (s 114BA) -- only to
  proceedings pending at commencement (finding 10).
- **F15** s 71 (2), (4) "the total number of pages" -- `s 71 -- what must I pay for copies` -- the pages of the copies the
  claimant requires -- the pages of all the relevant material.
- **F16** s 36 (1) "includes liability", s 113 (1), s 114BE (3), s 100 -- the four functions -- outside the provision's
  terms: NOTHING-kind (the common law may still give a claim) -- JUST FALSE.
- **F17** s 102 (1) the claimant's share -- `s 102 -- ...` -- a share outside 0-100% is read as the nearest bound -- an input
  error.
- **F18** s 59 (1) and s 54 (3) -- `s 59 -- can I proceed further with my claim` -- the presumption is asked as a fact (it
  is the s 54 question's answer) -- computed again inside s 59.
- **F19** s 102 (3) "the amount of damages awarded ... because of subsection (1)" -- `s 102 -- my damages after
  contributory negligence` -- the maximum limit caps only damages reduced under s 102 (1); where no reduction is allowed
  (s 27, s 102 (2)) the unreduced damages are answered, and the limit applies on its own terms outside s 102 -- the
  cap applies to every award in a contributory negligence case.
- **F20** s 114BBB "child abuse that happens ... on or after the day this division commences", abuse over a period that
  reaches that day -- `s 114BBD -- is the organisation taken to have breached its duty` -- asked by the abuse's last day:
  the division reaches the abuse on or after 16 May 2026 -- the whole course of abuse is outside the division if it began
  before.

Sites decided without a fork line: the "means" and "if" conditions of ss 5, 8, 37, 50 (2), 66, 67, 94-97, 107B, 113,
114BBB, 114BBD (3), 181 answer the text's no when they fail; s 14, s 26 and s 38 (1) are flat negatives ("is not",
"must not", "there is no right"), answered as the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries NOTHING-kind tags (forks F1, F13, F16; s 26 for unlisted payments; s 14 outside part 2.3; s 51 (7)
for motor accident claims; s 55 (3) (b) with no period in the Act; s 181 above $50,000; s 107B for other claims). Most
questions answer with a choice from a list rather than a MAYBE BOOLEAN: the answer marked "NOTHING-kind" is the NOTHING
answer, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **The death provisions no longer say who sues, or for whom.** s 25 (1) awards damages "to the people for whose
   benefit the action is brought (the beneficiaries)" but part 3.1 no longer names them: the sections that did ("One
   action for benefit of members of dead person's family", payment into court, special endorsement, powers of the court,
   once ss 28-31) were omitted by A2006-40 amdt 2.61 (endnote 4). The s 23 definition of "member" is now used only in
   s 16 (7), s 25 (6) and s 26 (e). The encoding answers whether a person is a member (s 23) and does not say who the
   beneficiaries are; presumably the Court Procedures Rules 2006 now say it, which this encoding does not read.
2. **The ACT text sets no threshold or cap on damages for personal injury except the earnings cap.** No injury
   threshold, no cap or scale for non-economic loss (s 99 only lets the court look at earlier awards), no gratuitous care
   threshold, no discount rate. The one limit is s 98: earnings above 3 times average weekly earnings a week are
   disregarded. Asserted (s 98 cases).
3. **The Regulation does much of chapter 5's work, and is not deposited.** The notice's content (s 51 (2)), reasonable
   excuses (s 51 (8)) and many periods are "prescribed by regulation"; two (s 55 (3) (b), s 57 (5)) have no period in
   the Act at all. The encoding uses the Act's fallback periods and answers no date for s 55 (3) (b). Asserted.
4. **s 51 (7) asks for a reasonable excuse only when the s 51 (3) period is missed.** A late notice of a motor accident
   claim (s 51 (4)) needs no excuse under the Act; only the continuing duty (Legislation Act s 152, cited in the notes)
   remains. Asserted (the motor accident case a day late).
5. **The s 51 (3) period can be far shorter than 9 months.** Limb (b) ends 4 months after the later of instructing a
   lawyer and identifying the respondent: a claimant who sees a lawyer in the week of the accident has about 4 months,
   not 9. Before a lawyer is instructed, limb (b) has not begun, so the last day can move earlier once one is (fork F8).
   Asserted (1 July 2026 instead of 15 October 2026).
6. **The s 54 (3) presumption is conclusive, and a late response does not undo it.** A respondent that responds a day
   after its required period is presumed satisfied whatever its response says. Asserted. Whether a respondent that never
   engages at all is caught is fork F6.
7. **s 97 gives no way to rebut the helmet presumption.** s 97 (2) allows rebuttal "only as provided in subsections (3)
   and (4)", which deal with the seatbelt (1) (a) and the passenger compartment (1) (b) (ii); nothing covers (1) (b) (i),
   the helmet. The helmet ground already requires that not wearing one contributed to the accident or the injury.
   Asserted.
8. **s 97 does not require the defendant to claim contributory negligence**, unlike ss 95 (1) (b) and 96 (1) (c). Encoded
   as written: s 97 asks no such fact.
9. **The s 181 costs cap is always $10,000 on the Act's own numbers.** The cap is the greater of 20% of the amount
   recovered and $10,000, but s 181 applies only where $50,000 or less is recovered, and 20% of $50,000 is $10,000. So the
   percentage limb can never win unless a regulation changes the figures. Asserted at $30,000, $50,000 and $0; above
   $50,000 there is no s 181 cap.
10. **s 262 reads as if division 8A.1A.3 (vicarious liability) applied only to proceedings pending on 13 November 2025.**
    It says the division "applies to proceedings commenced but not finally decided before" that day; it is presumably
    meant to extend the division to pending proceedings as well as later ones (s 114BA applies chapter 8A whenever the
    abuse happened). Encoded on the second reading (fork F14).
11. **s 168 (3) takes away s 102 (2) for claims against occupiers.** An occupier's duty is itself statutory (s 168), so
    without s 168 (3) contributory negligence could never reduce an occupier claim for personal injury. Asserted.
12. **"Subject to part 7.1" in s 27 (2) and s 102 (5) is not explained.** Whether an unrebutted s 95-97 presumption, which
    says damages "must be reduced", overrides the rule that a death claim is not reduced (s 27 (1)) is not said (fork
    F12).
13. **Division 8A.1A.2 starts on 16 May 2026**, six months after the rest of part 8A.1A (13 November 2025), and its
    reversed onus (the organisation is taken to have breached its duty unless it proves reasonable precautions,
    s 114BBD (3)) does not reach earlier abuse; s 114BE (vicarious liability) does. The note to s 114BA says the same.
    Asserted (13 November 2025, 15 and 16 May 2026). Abuse that went on across that day is fork F20.

## Before this is worth relying on

- The Civil Law (Wrongs) Regulation 2003 (SL2003-20): the notice's content, reasonable excuses, prescribed periods, and
  any change to the s 181 figures (findings 3, 9).
- The Legislation Act 2001 (ACT) for counting periods and moving a last day off a weekend or holiday (fork F2), and for
  "domestic partner".
- The Court Procedures Rules 2006 (deposited as its own subject) for who brings a death claim and for whom (finding 1).
- A lawyer's view on forks F4, F6, F7, F10, F11, F12, F14, F19, F20 and on findings 1, 7, 10 and 12; an independent test pass and a
  human gate.
- Read with: the Limitation Act 1985 (ACT) encodings beside this one (the limitation periods themselves, legal
  disability, s 21C for child abuse, s 30A for injuries to children), the Motor Accident Injuries Act 2019 (ACT)
  baseline (the WPI days in s 51 (4), and its own limits on common law damages), and the Workers Compensation Act 1951
  (ACT) baseline (which ss 41, 50, 93 put outside this Act).
