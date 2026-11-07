# Law Reform (Miscellaneous Provisions) Act 1956 (NT) -- baseline encoding, the estate and the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus asked for was **survival**: Part II
(survival of causes of action on death), which is encoded whole. The Act is short, so the claims machinery in the other
Parts is encoded too, section by section, where a person bringing or answering a claim meets it.

- `lrnt-dates.l4`: the dates (built-in date functions only, no daydate), including "12 months after" and "12 months
  before" a day.
- `lrnt-survival.l4`: Part II (ss 5 to 9), with the one regulative rule (s 7(1)(b)).
- `lrnt-claims.l4`: Parts IV to X.
- `lrnt-survival-cases.l4`, `lrnt-claims-cases.l4`: the worked cases.

The duty with a deadline -- taking proceedings in tort against a dead wrongdoer's estate within 12 months after probate
or letters of administration are taken out, or a further period the Supreme Court allows (s 7(1)(b)) -- is a regulative
rule (`PARTY ... MUST ... WITHIN ... LEST BREACH`) run by EVALTRACE inside an exported question that takes only plain facts.

## Edition

- **Act:** Law Reform (Miscellaneous Provisions) Act 1956 (NT), first made as the Law Reform (Miscellaneous Provisions)
  Ordinance 1956 (No. 31 of 1956), commenced 28 June 1956. The deposited text is reprint **REPL004, as in force at
  6 December 2018**, the current reprint on the NT Legislation register when retrieved on 6 November 2026:
  `../../registers/source-bundle/Law-Reform-Miscellaneous-Provisions-Act-1956-NT-current-reprint-REPL004.txt`.
- **Dates used, from the endnotes:** 28 June 1956 (commencement; also s 21(b)); 1 January 1992 (s 29A, Act No. 44 of
  1991); 1 August 2001 (Law Reform (Miscellaneous Provisions) Amendment Act 2001, which replaced s 16 and inserted s 21A);
  7 November 2007 (Law Reform (Dust Diseases) Amendment Act 2007, which inserted s 6(2)-(4)).
- **Numbers set elsewhere:** none that the encoding needs. The Act's only amount is the $5,000 of s 29A(4). The value of
  a penalty unit (s 35) is set by the Penalty Units Act 2009 (NT), not deposited: the answer gives the units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 29A cap asserted as 5,001 on damage of 5,001) was run once in a scratch file in this
folder, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lrnt-dates.l4` | 0 | 0 | 0 | 0 |
| `lrnt-survival.l4` | 0 | 0 | 0 | 0 |
| `lrnt-claims.l4` | 0 | 0 | 0 | 0 |
| `lrnt-survival-cases.l4` | 0 | 0 | 56 | 56 |
| `lrnt-claims-cases.l4` | 0 | 0 | 85 | 85 |

Every exported question has cases, with the edges: a death on 27 and on 28 June 1956; each s 5(2) exception, each way; s 8
for and against; a dust-disease death on the day of determination and the day before, on 6 and 7 November 2007, and an
action determined on 6 and on 7 November 2007; a cause of action arising exactly 12 months before the death and one day
earlier (also across 29 February); proceedings on the anniversary of the grant and the day after; a further period's last
day, the day before and the day after; proceedings before any grant; the regulative rule alone on day 0, the last day and
the day after; a wrong on 27 and 28 June 1956, 31 July and 1 August 2001; a s 16 limit equal to the reduced amount and one
dollar below it, reductions of 0% and 100%; the s 29A cap below, at and one dollar over $5,000, and damage on
31 December 1991 and 1 January 1992; the s 28 policy sum one dollar under the liability.

**No mirror cases.** One seat per question.

## Seat

**The individual a death or a claim touches.** Part II, from two sides (`lrnt-survival.l4`):

- the **executor or administrator** of a person who has died, bringing or continuing that person's claim for the estate:
  "Does the claim survive?", "What can the estate recover?", "Does a dust-disease claim keep its damages for pain and
  suffering?" (the last can also be asked by a person living with a dust disease about their own action);
- a **person with a claim against someone who has died**: "Does my claim survive their death?", "Can I still sue the
  estate?", "By when must I take proceedings?".

The other Parts (`lrnt-claims.l4`): mostly the **person bringing the claim** (the injured person, a dependant, a person
who suffers loss through the injured person, a worker, a family member in shock, a person whose property a child damaged,
a person hurt by a dog, a blind or deaf person with an assistance dog). Where the Act addresses another individual, that
individual: the **employee** who committed a tort at work (s 22A) and the **person who killed or injured a dog**
(ss 33, 34). No official gets a seat: what a court would find, allow or think just is asked as a fact.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number used. The
  Compensation (Fatal Injuries) Act 1974, the Personal Injuries (Liabilities and Damages) Act 2003, the Limitation Act
  1981 and the Youth Justice Act 2005 are not brought in: their effects are asked as facts or noted.
- **The actors the text names.** Followed: the deceased, the executor or administrator, the estate, the claimant, the
  tort-feasors, the employer and employee, the insured and insurer, the child, parent, detainee and Territory, the dog's
  owner, the court, the Supreme Court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: the damages a court would assess
  (s 6, s 16(3)), the reduction it thinks just and equitable (s 16(1)(b)), whether it is satisfied it is reasonable to
  let proceedings continue (s 7(2)), whether it allowed a further period (s 7(1)(b)), whether there was reasonable ground
  for a later action (s 12(3)(b)), whether misconduct was serious and wilful or gross (s 22A(3)), whether an insurer may
  disclaim (s 27(3)), reasonable grounds and reasonable cause (ss 33, 34).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "dust disease" (s 6(4)), "wrong"
  (s 15), "member of the family", "parent", "child" (s 23), "child" (s 29A(1)), "dog" (s 31). Asked: "dependant" (by the
  Compensation (Fatal Injuries) Act), "detainee" (Youth Justice Act 2005), "tort", "cause of action", "determined".
- **One case is the text's natural unit.** Followed: one death and one claim (Part II), one claim (the other Parts).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed: ss 1, 3, 4 out.

## Scope

**In.**
- **Part II (the focus), whole:** s 5 (survival), s 6 (damages for the estate, with the dust-disease rule of s 6(2)-(4)),
  s 7 (conditions for proceedings in tort against an estate), s 8 (a person liable who dies before or at the damage),
  s 9(1) (Compensation (Fatal Injuries) Act claims are brought within the "against the estate" rules).
- **Part IV:** s 11(b), s 12(2), s 12(3) (several actions for the same damage: the cap and costs).
- **Part V:** s 15, s 16, s 17(2), s 18, s 21, s 21A (contributory negligence, for the claimant, a dependant and a third
  person).
- **Part VI:** s 22, s 22A. **Part VII:** s 23, s 24, s 25. **Part VIII:** s 26(1), (2), s 27, s 28.
  **Part VIIIA:** s 29A. **Part X:** s 31 to s 35.

**Out, and why.**
- s 1, s 3, s 4: machinery (short title, a repeal, binding the Crown).
- s 9(1) first limb and s 9(2): savings ("in addition to, and not in derogation of" the dependants' rights and the Motor
  Vehicles Ordinance); they change no answer here. Noted in the s 7 and s 6 comments.
- s 12(4), (5), s 13, s 14, s 19: contribution between wrongdoers, a question between defendants, decided by the court's
  view of what is just and equitable.
- s 17(1): Part IV's application to several wrongdoers liable under s 16 (between defendants). s 20: jury procedure.
- s 21A(3), (4): the s 16 in force before 1 August 2001 is not deposited; the answer says the earlier text applies and is
  not encoded.
- s 26(3): the ranking of several claimants' charges on the same insurance money; one claim is the unit.
- s 29: Part VIII does not affect the Workmen's Compensation Ordinance 1921 or Part V of the Motor Vehicles Ordinance
  1974 (a saving; both stale, see finding 3).
- The Personal Injuries (Liabilities and Damages) Act 2003, the Compensation (Fatal Injuries) Act 1974 and the Limitation
  Act 1981, which bear on the same claims (deposited beside this Act at `subjects/au/nt/`): not this Act.
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 5, 22(2), 24, 25 "after the commencement of this Ordinance" -- `s 5 -- does the claim survive the death`,
  `s 22 -- ...`, `s 25 -- ...` -- an event on 28 June 1956 itself is after the commencement (the Ordinance was in force
  from the start of that day) -- only an event from 29 June 1956.
- **F2** s 6(2) "dies ... before the action is determined" -- `died before the action was determined` -- a death on the day
  of determination is not before it -- a death earlier on the same day is before it (time of day not asked).
- **F3** s 6(3) "remains undetermined at the date of commencement of that subsection" -- `undetermined at 7 November
  2007` -- an action determined on 7 November 2007 still counts as undetermined at that date -- determined on that day is
  not undetermined at it.
- **F4** s 6(1)(c)(i) "a sum in respect of funeral expenses may be included" -- `s 6 -- how much can the estate recover`
  -- the funeral expenses assessed are recoverable -- a discretion in the court whether to include them.
- **F5** s 6(1) -- the same function -- the amounts are the court's assessment apart from s 6; s 6 only takes heads out;
  where the death was not caused by the wrong, everything assessed (other than exemplary damages) is kept -- s 6 read as
  also fixing what is assessed.
- **F6** s 7(1)(b) "12 months before" and "12 months after" -- `the corresponding day ... years from` -- the same day of
  the month; from 29 February, 28 February -- 1 March.
- **F7** s 7(1) "a cause of action in tort" -- `s 7 -- can I take proceedings against the estate` -- a claim not in tort
  (and not under the Compensation (Fatal Injuries) Act) is outside s 7, which says nothing about it (NOTHING-kind) -- the
  text's no on s 7.
- **F8** s 7(1)(b) "within such further period as the Supreme Court ... allows" -- `the s 7 last day` -- the later of the
  12-month day and the end of the further period -- the further period as stated, even if it ends sooner.
- **F9** s 7(1)(b) proceedings "taken ... not later than 12 months after" the grant -- the s 7 question -- proceedings taken
  before any grant are in time (counted as day 0) -- premature, which is a question for the rules of court.
- **F10** s 22A(1)(b) "unless the employee is otherwise entitled to indemnity" (an "unless" once met) -- `s 22A -- who
  bears the liability for my tort at work` -- the employer then need not indemnify, and s 22A(2) subrogates it -- the
  employer indemnifies only the part the other indemnity does not cover.
- **F11** s 26(1), s 28 -- `s 28 -- the most I can recover from the insurer` -- the liability, capped at the policy sum
  less the insurer's payments made without notice of the charge -- payments without notice reduce only what is owed to
  the insured, not the cap.
- **F12** s 17(2) "reduced to a proportionate extent", s 18 -- the s 16 questions -- the same percentage reduction as for
  the injured person -- a different proportion for the dependants' or third person's heads of loss.
- **F13** s 29A(3) -- `the s 29A answer` -- a detainee need not be under 18; the Territory is liable for damage on or after
  1 January 1992 -- only from 1 August 2006, when the Youth Justice Act 2005 definition began (finding 7).
- **F14** s 33(1)(a), (3) -- `s 33 and s 34 -- ...` -- an occupier, or a person there with the occupier's authority, is
  not a trespasser; s 33(3) gives such a person a rebuttable defence even where the attack facts are not shown -- s 33(3)
  only shifts the burden once the attack facts are raised.
- **F15** s 5(1) "all causes of action subsisting" -- `s 5 -- ...` -- no cause of action at the death (and s 8 not met): the
  text's own limit, NOTHING-kind -- the text's no.

Sites decided without a fork line: s 5(2), s 16(2), s 21 and s 22A(3) are flat negatives (the text's no); s 6(4), s 15
and s 23 are "means" definitions (FALSE when an element fails); the "if" of s 6(2), s 12(3) and s 16(1), and the "where"
of s 22, s 22A(1), s 25(1)(b) and s 29A(2), (3), failing are the text's no; s 33 is "a defence ... if", answered "these
sections give no defence on these facts" under ruling (b) on defences.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

Most questions answer with a choice from a list: the answers marked "(the text's no)" are the JUST FALSE answers and the
answers marked "NOTHING-kind" are the NOTHING answers. Three questions answer NOTHING directly: `s 7 -- by when must I
take proceedings against the estate` (no grant, so no date yet), `s 16 -- how much can I recover after the reduction`
(s 16 does not apply, so it fixes no amount) and `s 32 -- is the dog's owner liable` (outside s 32). The rulings it
follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The s 7(1)(b) period is the regulative rule (`MUST take proceedings against the estate WITHIN` the days from the grant
to the last day, `LEST BREACH`), run by EVALTRACE inside the question; outside it the answer is "out of time (the text's
no)", with the Supreme Court's power to allow a further period noted.

## What the Act turns out to say

1. **A tort claim against a dead wrongdoer's estate has a second clock.** Unless proceedings were already pending, s 7
   requires the cause of action to have arisen no earlier than 12 months before the death and proceedings to be taken
   within 12 months after probate or administration is granted (or a further period the Supreme Court allows, on an
   application made before or after the period ends). s 7(3) keeps the ordinary limitation law running alongside, so the
   earlier deadline binds. Asserted (anniversary in time, the day after out of time).
2. **s 7(2) relaxes only half of s 7(1)(b).** A court satisfied it is reasonable can let a claim that arose more than
   12 months before the death go on, but nothing in s 7(2) relaxes the 12 months after the grant. Asserted.
3. **Stale cross-references.** s 9(1), s 11, s 15 and s 17(2) still name the "Compensation (Fatal Injuries) Ordinance
   1974" (now an Act); s 9(2) names "Part V of the Motor Vehicles Ordinance 1949" and s 29 "Part V of the Motor Vehicles
   Ordinance 1974" (the same Ordinance given two years); s 29 also saves the "Workmen's Compensation Ordinance 1921",
   long repealed. Several sections still say "this Ordinance". Noted; the encoding reads "this Ordinance" as the Act and
   its commencement as 28 June 1956.
4. **The dust-disease rule needs the person to have sued.** s 6(2) keeps damages for pain and suffering only where the
   person "commences an action" and dies before it is determined. If they die before commencing, the estate's claim has
   no such damages. Asserted.
5. **s 21 says "and" where it means "or".** "Section 16 does not apply to: (a) a claim to which section 259 of the
   Navigation Act 1912 ... applies; and (b) a case where the wrong ... occurred before 28 June 1956." Read as two separate
   exclusions, each sufficient. Asserted (each excludes on its own).
6. **The damages in Part II and Part V are subject to the Personal Injuries (Liabilities and Damages) Act 2003.** That Act
   (deposited beside this one, not encoded here) limits damages for personal injury; the s 6 and s 16 amounts are taken as
   the court would assess them, and this encoding does not apply its limits.
7. **s 29A(3) and the date.** The Territory's liability for a detainee is "after the commencement of this section"
   (1 January 1992), but "detainee, within the meaning of the Youth Justice Act 2005" exists only from 1 August 2006, and
   nothing requires the detainee to be under 18. Encoded as written (fork F13).
8. **s 12(3)(a) caps by the first judgment, not the largest.** If the judgment given first is the smallest, later and
   larger judgments are cut down to it in aggregate. Asserted (a first judgment of 0 caps the total at 0).
9. **The reprint is the 2018 text.** REPL004 is "as in force at 6 December 2018" and was current on 6 November 2026; an
   amendment after that date that the register has not reprinted would be missed.

## Before this is worth relying on

- The Personal Injuries (Liabilities and Damages) Act 2003 read with s 6 and s 16 (finding 6), and the Limitation Act
  1981 read with s 7 (finding 1).
- The pre-2001 s 16 (s 21A(3)), the Interpretation Act 1978 (NT) on commencement and month counting (forks F1, F6), and
  the Penalty Units Act 2009 for s 35.
- A lawyer's view on forks F2 to F5, F8, F9, F11, F13 and F14; an independent test pass and a human gate.
