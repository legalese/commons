# Coroners Act 2008 (Vic) -- baseline encoding, the family of the person who died

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Four modules:

- `cor-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`);
- `cor-rules.l4` -- the law more than one question uses: the s 3 definitions (senior next of kin, immediate family, person
  placed in custody or care), s 4 (reportable death) and s 5 (reviewable death) over one record of death facts, the deaths
  ss 17 and 17A reach, the two duties with deadlines as regulative rules (ss 42(3), 52(6)) with their trace helpers, and the
  Part 7 appeals table (who may appeal, the last day, s 86);
- `cor-seat.l4` -- the 42 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in
  the Act's order. Where a section is used by one question only, the question applies its words there and quotes them;
- `cor-cases.l4` -- the cases.

## Edition

- **Act:** Coroners Act 2008, Act No. 77/2008, Version No. 046, incorporating amendments as at 1 November 2026 (the
  register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/coroners-act-2008.txt` (sha256 e85ac715...46deff as committed), a plain-text conversion
  of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and `subjects/au/vic/README.md`). Not
  checked against the authorised PDF, which was not saved. This version includes the amendments of Act No. 14/2026
  (ss 17A, 17B, 17C, 84A, the new s 77(1), (1A), and the repeal of s 16(1A)).
- **Numbers set elsewhere:** the Act fixes its own periods (48 hours, 28 and 90 days, 3 and 6 months, 50 and 100 years).
  The regulations under s 117 (prescribed classes and circumstances for s 4(2)(j) and s 52(2)(d), the prescribed persons of
  s 3 "person placed in custody or care" (l), the prescribed information of s 21) and the rules of the Coroners Court are not
  deposited: each is a yes/no input.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cor-dates.l4` | 0 | 0 | 0 | 0 |
| `cor-rules.l4` | 0 | 0 | 0 | 0 |
| `cor-seat.l4` | 0 | 0 | 0 | 0 |
| `cor-cases.l4` | 0 | 0 | 286 | 286 |

Every expected value was worked by hand from the text, with the edges: every exported question at least three times; each
hour period at the 48th hour and just after; the 50- and 100-year limits on the day exactly 50 or 100 years before the
report and the day before; each month period from the 30th or 31st of a month into February (28 February 2027, 29
February 2028); each day period on its last day and the next; each regulative rule done on the last day, done the day
after, still open on the last day and late the day after; every s 4(2) head alone, with (h) and (i) on both sides of the
Victorian border; each senior-next-of-kin paragraph with and without someone higher available.

## Seat

**The family member** (`cor-seat.l4`): the senior next of kin or another member of the immediate family of the person who
died, or another person with an interest in the death (who reported it, asked for an autopsy, an inquest or a re-opening,
applied for the body, was notified of an exhumation, or was given leave to take part as an interested party). "Am I the
senior next of kin?", "Was it a reportable death?", "Must a coroner investigate, and hold an inquest?", "Can the coroner stop
on natural causes?", "Can I object to the autopsy, and is it held back?", "Has the coroner answered my request for an
inquest in time?", "Will I get the coronial brief?", "Must the coroner find how my family member died, and will it be
published?", "Is an apology an admission?", "Can I apply to re-open or set aside the findings?", "May I appeal, by when, and
on the merits?". Three questions (ss 42, 50, 57) are asked by anyone the coroner calls on, as a witness or for a document;
the family member often is one.

No seat for the coroner, the State Coroner, the Coroners Court, the Supreme Court, the Institute, police or the registrar:
their decisions, beliefs, satisfaction and leave are asked as facts; their duties to the family (s 52(6) advice, s 115(1)
notice and brief, s 57 certificate, s 73 publication) are encoded as what the person must be given, and by when.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; the regulations and
  rules it defers to are not deposited and are inputs.
- **The actors the text names.** Followed: the senior next of kin, immediate family, spouse and domestic partner,
  executor, personal representative, interested party, witness, the person who reported the death or made a request, the
  coroner, the State Coroner, the Coroners Court, the Supreme Court, a medical investigator, a pathologist, an interstate
  coroner.
- **Judgments answered conditionally.** Followed: "suspects homicide", "satisfied", "considers natural causes", "sufficient
  interest", "appropriate", "public interest", "reasonable grounds", "exceptional circumstances", "interests of justice",
  "acted unreasonably", leave and orders are inputs. Departed from in one respect (fork F6): where the Act says "it appears
  to the coroner" or "the coroner determines" that a fact in s 4 holds (ss 15, 17, 17A, 52(3)(a)), the fact as the person
  states it is used, so the facts are asked once.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "senior next of kin", "immediate family", "domestic
  partner", "person placed in custody or care", "reportable death", "reviewable death", "apology" (s 70(1)) are worked
  out; "medical procedure", "registered relationship", "designated mental health service", "still-birth", "voluntary
  assisted dying substance", "indictable offence" are asked.
- **One case.** One death (or one decision about it), seen by one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The focus: reportable deaths, investigations, inquests and findings, and the claims machinery around them (the family's
rights, time limits and appeals). Parts 3 to 7 are encoded where they give the person a fact test; Parts 1 and 2 for their
definitions; Parts 8 to 10 only for s 115(1).

**In:** ss 3(1), (3) (senior next of kin, immediate family, domestic partner, person placed in custody or care, child,
death and note 1), 4, 5, 12, 14, 15, 16(5) (and 16(1), (3) in the answer), 17(1), 17A(1), (5), 17B(1), (2), (4), 26(2),
(4), (5), 27, 42(2), (3), 46(5), 48(2), (3), 50, 52(2) to (6), 53(2), (3), 56, 57(1) to (8), 66(3), 67(1), (2), 69, 70, 71,
73(1), (1A), (1B), 74(1) to (3), 76A(1), (3), 77(1), (1A), (2), (5), (6), 78 to 85 (standing and periods), 86, 87(1), (1A),
87A, 115(1), (7).

**Regulative rules:** two. s 52(6) (and s 53(3)): the coroner MUST advise the person who asked for an inquest, in writing,
WITHIN the days from receipt to the day 3 months later, LEST breach; run by EVALTRACE inside `Has the coroner answered my
inquest request in time`. s 42(3): the person required MUST give the coroner the document or prepared statement WITHIN the
days from service to the last day of the period specified, LEST breach (20 penalty units without a lawful excuse); run
inside `Have I met the coroner's requirement in time`. Both questions take only dates and yes/no facts.

**Out, and why:**
- ss 1, 2, 6 to 9 (purposes, commencement, objectives): guidance with no fact test.
- ss 10, 11, 13 (reporting duties of a doctor present at the death, of the person responsible for someone in custody or
  care, and the reviewable-death duties): duties of a practitioner or custodian, not the family's; s 13(3) has the shape
  of s 12(1) and could be added. ss 10(3), 11(1A), 12(3), 13(4) are the Institute's.
- ss 15A, 16(1) to (4), (6), 16A, 17(2), 17A(2) to (4), 17C, 18 to 20, 22 to 25, 28, 29, 29A: the coroner's, State
  Coroner's and registrar's powers and administration. s 21 (prescribed information to the senior next of kin) needs the
  regulations, not deposited. s 26(1), (3) are in through the s 26(4) question.
- Part 4 Division 2 (fires: ss 30, 31, 34, 35) and s 68: outside the focus; the fire appeal (s 80) and the request for an
  inquest into a fire (s 53) share the machinery and are in.
- ss 32, 33, 36 (duties to assist the coroner): in only through the s 50 excuse; ss 37, 38 (restricted places, 60 penalty
  units), 39 to 41 (entry and search), 42(1), 42A, 58 (Evidence Act privileges, borrowed), 43 to 45, 46(1) to (4), 47, 49,
  51: powers of the coroner or police, or administration.
- ss 53(1), 54, 55, 59 to 65, 66(1), (2): the coroner's powers and the conduct of the inquest, with no fact test for the
  person (s 59 warrants could be added for a witness).
- ss 72 (recommendations and the 3-month response duty of a public statutory authority), 74A, 75, 76: the authority's,
  the coroner's and the Court's; s 75 (protection) adds no fact test.
- ss 87(2) to (5), 88: the Supreme Court's powers on appeal.
- Parts 8, 9 and 10 (the Court, the Council, contempt, rules, s 114 return of things, s 115(2) to (6), (8) release of
  documents at the coroner's discretion, s 116 registers, s 117 regulations, s 118 fees, transitional provisions and
  Schedule 1): machinery, or a discretion with no fact test. s 115(4), (5) (conditions on released documents, 60 penalty
  units) could be added.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(1) "senior next of kin" (c) to (g) "if a spouse, domestic partner, son or daughter is not available" -- `s 3 --
  I am the senior next of kin` -- "son or daughter" read as one qualifying under (b), of or over 18, so a child under 18
  does not displace a parent, sibling, executor or personal representative -- read literally, any son or daughter.
- **F2** s 3(1) "death", note 1 ("A still-birth ... is not a death") -- `s 4 -- a reportable death`, `s 5 -- a reviewable
  death` -- a still-birth: FALSE -- whether the note is operative is for the Interpretation of Legislation Act 1984; the
  Births, Deaths and Marriages Registration Act 1996 gives the same answer.
- **F3** "within 3 months" (ss 12(2), 52(6), 76A(3), 81(4), 82(2)), "within 6 months" (s 83(3)) -- `the date` n `months on
  from` -- the same day of the month n months later or earlier, or that month's last day where it is shorter (30 November
  2026 plus 3 months is 28 February 2027), the last day included -- 1 March 2027 (rolling over), or the last day excluded.
- **F4** s 12(1) "A person who has reasonable grounds to believe" -- `Must I report the death` -- the "who"-clause unmet:
  JUST FALSE (ruling (b) of 2026-11-05) -- NOTHING (a scope limit).
- **F5** s 83(1) "the findings ... after an investigation" -- `Part 7 -- I may appeal` -- includes findings after an inquest
  (an inquest is part of the investigation, as s 77(1) "whether or not an inquest has been held" shows), so a person with a
  sufficient interest may appeal inquest findings too -- after an inquest only an interested party (s 83(2)).
- **F6** ss 15, 17(1)(a), (ab), (d), 17A(1)(a), (d), 52(3)(a) "it appears to the coroner", "the coroner determines",
  "believes ... probably" -- `Must a coroner investigate the death`, `Can the investigation stop on natural causes`, `Must
  the coroner hold an inquest` -- the s 4, s 5 and date facts as the person states them -- each as a separate input of the
  coroner's view.
- **F7** s 46(5) "48 hours after ... or any further period specified by the State Coroner"; s 81(2) the same -- `Is the
  exhumation still held back`, `May I still appeal the exhumation authorisation` -- the further period added to the 48
  hours -- a longer period replacing them.
- **F8** s 66(3) "or, with the permission of the coroner, by any other person" -- `May this person represent me at the
  inquest` -- a non-lawyer without permission: JUST FALSE (the condition read as "if") -- NOTHING.
- **F9** s 26(2) "Within 48 hours after receiving notice" against s 26(4)(a) "until ... 48 hours after the required notice
  has been given" -- `May I ask the coroner to reconsider the autopsy`, `s 26(4) -- ...` -- the 48th hour itself is within
  s 26(2) (TRUE) and is the moment the direction takes effect under s 26(4) (no longer held back) -- either end excluded.
- **F10** s 48(3) "should be released to" -- `Do the principles point to releasing the body to me` -- JUST FALSE where the
  principles point to another applicant -- NOTHING (the principles guide; s 48(2) "better claim" decides).
- **F11** s 115(1)(a) where no medical examination reports were given -- `Must I be told about the medical reports` --
  NOTHING (nothing to notify; the Act is silent) -- JUST FALSE.
- **F12** s 57(1) "This section applies if a witness objects" -- `Must I be given a certificate for my evidence` -- no
  objection: JUST FALSE ("if") -- NOTHING.
- **F13** ss 17B(2), 76A(1), 77(1A) "The following persons are specified" / "may apply" -- the three application questions --
  a person outside the list: NOTHING (a list not closed with "only") -- JUST FALSE.
- **F14** s 52(3A) "not required ... in the circumstances set out in subsection (2)(b) if ... natural causes" -- `Must the
  coroner hold an inquest` -- natural causes removes only head (b); a custody death with the identity unknown still
  requires an inquest under (c) -- (3A) relieves the whole inquest.
- **F15** s 81(1) "the senior next of kin and any other person who received notice under section 46(3)" -- `Part 7 -- I may
  appeal` -- the senior next of kin has standing whether or not notified -- only if notified.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 and the "is a reportable death if" and "is a reviewable death if" of ss 4, 5
answer plain TRUE/FALSE; "is not a reportable death" (s 4(3)), "is not a reviewable death" (s 5(2)), "is not required" and
"need not" (ss 17(1), 17A(5), 52(3), (3A), 67(2), 71), "must not" (ss 17B(4), 69(1), 77(5)), "does not constitute an
admission" (s 70(2)), "cannot be used ... However, this does not apply" (s 57(7)), "it is not a reasonable excuse" (s 50(2)),
"unless otherwise ordered" (ss 73(1), 115(1)), the "if" conditions of ss 12(2), 52(2), 56, 57(4), (5), (6), 86, 87A and the
periods of ss 12(2), 26(2), 76A(3), 79(2), (4), 81(2), 85(2) and Part 7 give `JUST FALSE`. `NOTHING` is answered where a
grant of standing or an application right does not reach the person (ss 12(2), 17B, 26(2), 66(3), 76A, 77, 78 to 85, 86,
115(1)) (*limited by its own wording*), where s 48 hands the choice to the common law (*points outside the sources*), and
where the Act does not speak (ss 50, 57(4), 70, 115(1)(a)) (*silent*). Two "until" bars (s 26(4), s 46(5)) answer TRUE
while the direction or authorisation is held back and FALSE after, never that the autopsy or exhumation has happened.

## What the Act turns out to say

1. **Two senior next of kin at once.** s 3 "senior next of kin" (a) names the spouse or domestic partner with no
   "available" condition, while (b) makes an adult son or daughter senior next of kin "if the spouse or domestic partner
   is not available". Where a spouse is unavailable, both are senior next of kin on the words. Encoded as written. Asserted.
2. **"Son or daughter" loses its age limit.** (b) requires a son or daughter "of or over the age of 18 years"; (c) to (g)
   ask whether "a spouse, domestic partner, son or daughter is not available" with no age. Read literally, a deceased
   parent's 10-year-old child would keep the deceased's own parents, siblings, executor and personal representative from
   being senior next of kin, leaving none until a coroner determines one. Encoded as an adult son or daughter (F1). Asserted.
3. **One "the senior next of kin", several people.** Paragraphs (b) to (d) can name several people at once (two adult
   children), and s 48(3)(c) expects "2 or more applicants who are the senior next of kin", but ss 26, 45, 46(5), 79(1) and
   115(1)(a) speak of "the senior next of kin" in the singular: who is notified, who may object or waive, and whose waiver
   counts is not said. Not resolved; each question asks whether "you are the senior next of kin".
4. **ss 17 and 17A reach the same deaths.** s 17(1)(a) and (ab), by exclusion, and s 17A(1)(a), by "only because", both
   cover a reportable death that is unexpected, or under s 4(2)(h) or (i), and nothing else. They differ in the medical
   step (a medical examination report, against a preliminary examination and a pathologist willing to notify the
   Registrar) and in effect: only s 17A carries the re-opening right (s 17B) and the release from findings (s 17A(5)).
   Both may be open at once. Asserted.
5. **The time to object to an autopsy and the time it takes effect run from different moments.** The senior next of kin may
   ask for reconsideration "within 48 hours after receiving notice" (s 26(2)); the direction takes effect "48 hours after the
   required notice has been given" (s 26(4)(a)), and an appeal "must be made before the direction takes effect" (s 79(2)).
   Where notice is received later than it is given, the direction can take effect, and the appeal right end, while the time
   to ask the coroner to reconsider is still running. Asserted by the two questions at the 48th hour. And where the coroner,
   on reconsideration, does not confirm the direction, no s 26(3) notice is given and s 26(4)(b)(i) never lets it take
   effect; the Act does not say the direction lapses. Encoded as still held back. Asserted.
6. **No time limit to re-open or set aside.** An application to re-open a discontinued investigation (s 17B) or to set aside
   findings (s 77) has no time limit, while an application to amend the wording of a decision has 3 months (s 76A(3)) and an
   appeal against a refusal to re-open has 90 days (ss 84(2), 84A(2)). Encoded as written.
7. **s 87A names appellants that ss 82, 84 and 84A do not.** s 87A(1) lets a merits appeal "be made under section 82(1) ...
   or section 84(1) or 84A(1)" if made by "the senior next of kin" or "a person with sufficient interest", but those
   sections give standing only to "the person who requested" the inquest or re-opening. Read as an added condition, not a
   grant of standing: a senior next of kin who made no request has no standing under s 82 (NOTHING). Asserted.
8. **s 73(1B) has no "unless otherwise ordered".** A finding that a person in custody or care died of natural causes "must
   be published", even where an inquest was held and the coroner ordered otherwise under s 73(1). Asserted.
9. **"Lawful excuse" and "reasonable excuse".** s 42(3) makes it an offence to fail to comply "without a lawful excuse";
   ss 32, 33 and 34 have no excuse words; s 50 supplies a "reasonable excuse" for self-incrimination "for the purposes of"
   all four. Read as s 50 applying to them all. Asserted (s 50 question).
10. **A stale cross-reference.** s 78(1) still reads "If a coroner determines under section 16(1) or (1A)", but s 16(1A)
    was repealed by No. 14/2026 s 11(1) (and s 4(1A) by s 10). Encoded as s 16(1).
11. **s 74 "costs" and "expenses".** The heading speaks of costs and s 74(3) of a person "awarded costs", but s 74(2) lets
    the coroner order payment of "expenses (other than economic loss)"; s 74(1) binds only persons "represented by an
    Australian lawyer". Encoded as expenses less economic loss. Asserted.
12. **s 70 reaches the coroner's findings only.** An apology or fee waiver "does not constitute an admission ... for the
    purposes of findings that are made under section 67 or 68"; it says nothing of a civil claim (the Wrongs Act 1958 deals
    with apologies there; see its own encoding). The question says so.
13. **Conversion.** s 17(1)(ab) and s 26(4)(b) print without the indent of their neighbours; the text is otherwise as the
    Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The regulations under s 117 (prescribed classes and circumstances for ss 4(2)(j), 52(2)(d), prescribed persons in custody
  or care, the prescribed information of s 21) and the rules of the Coroners Court (s 26(2)(b) waiver, s 52(3B) reports,
  publication), none deposited.
- A lawyer's view on findings 1, 2, 3, 5 and 7 and forks F1, F5, F6, F7 and F14, an independent test pass and a human gate.
