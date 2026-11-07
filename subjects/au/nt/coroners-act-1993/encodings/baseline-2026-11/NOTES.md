# Coroners Act 1993 (NT) -- baseline encoding, the family of the person who died

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`cornt-dates.l4`,
built-in date functions only, no daydate), the rules and exported questions in `cornt-family.l4`, and the worked cases in
`cornt-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act sits in the claims set because a coronial investigation
often comes before a claim after a death (a dependants' claim, a workplace or road death, a death in care or custody,
a medical death). What a family member meets is: who the senior next of kin is; whether the death is reportable and
must be reported; whether the coroner must investigate and hold an inquest; the decisions they must be told of; the
fixed windows for going to the Supreme Court (14 days after a decision not to hold an inquest; 48 hours after an
autopsy refusal, an autopsy decision over their objection, or an exhumation order); the holds on autopsy, exhumation and
disposal of the body; their rights at the inquest, as a witness, and over publication of the name; the route to a new
inquest; and, for a later claim, that the coroner's record is not evidence of what it records and the coroner cannot be
called as a witness. The windows to the Supreme Court are one regulative rule (`MUST apply WITHIN`, `LEST BREACH`) run by
EVALTRACE inside the exported questions, in days for s 16(2) and hours for ss 21(3), 23(3) and 24(4).

## Edition

- **Act:** Coroners Act 1993 (NT), Act No. 30 of 1993, commenced 3 April 1994. The deposited text is reprint REPC019,
  "as in force at 28 November 2022" (last amended by the Burial and Cremation Act 2022), the current reprint on the NT
  Legislation register when retrieved on 6 November 2026:
  `../../registers/source-bundle/Coroners-Act-1993-NT-current-reprint-REPC019.txt`.
- **Numbers set elsewhere:** none used. Every period and penalty is in the Act. The Coroners Regulations (s 47) are not
  deposited and set none of the numbers encoded here. Penalty units are given as units; their dollar value is set under
  the Penalty Units Act 2009 (NT), not deposited.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (an application on the 15th day after notice asserted to be in time) was run once in a
scratch copy, since deleted, and showed as "assertion failed" (169 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cornt-dates.l4` | 0 | 0 | 0 | 0 |
| `cornt-family.l4` | 0 | 0 | 0 | 0 |
| `cornt-cases.l4` | 0 | 0 | 170 | 170 |

Every exported question has cases, with the edges: each paragraph of the senior next of kin definition, at 17 and 18
years, with a higher-ranked person available and not, and for an Aboriginal person with and without a customary person;
each head of reportable death and each kind of custody and care, a resident's death elsewhere certified and not; the
s 15 heads one by one, "care and custody" against care only and custody only; the 14 days on day 0, day 14, day 15, an
application before notice, across a year end and into 29 February; the 48 hours at 0, 47, 48, 48.5, 49 and 50 hours;
the s 37 latest day across a year end and onto 29 February, published on it, before it and the day after; each
maximum penalty. The regulative rule alone is asserted on days 0, 13, 14, 15, a negative day, and hours 48 and 49.

**No mirror cases.** One seat.

## Seat

**The family of the person who died** (`cornt-family.l4`): usually the senior next of kin, or another relative or
close person who may be the senior next of kin, may have to report the death, may be told of decisions, may take part
in the inquest or be called as a witness there, and may later bring a claim. "Am I the senior next of kin?", "Is this
a reportable death?", "Must I report it?", "Must there be an inquest?", "By when must I go to the Supreme Court?", "Can
the autopsy go ahead yet?", "Can the body be exhumed yet?", "Can I use the coroner's findings in my claim?".

The coroner, the coroner's clerk, the police, the Attorney-General, agencies and the Supreme Court get no seat. Their
duties (to investigate, to hold an inquest, to notify, to advertise, to suppress) are encoded for what they mean to the
family; their judgments (the coroner's suspicion, belief, opinion or satisfaction; the Court's discretion) are inputs.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number used here.
- **The actors the text names.** Followed: the senior next of kin, "a person", the coroner, the coroner's clerk, the
  Supreme Court, a witness, a person with a sufficient interest.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: the coroner suspects unlawful
  killing (s 15(1A)); believes an autopsy must be performed immediately (s 23(2)); is satisfied notice of exhumation
  cannot be given (s 24(2)); considers a relationship sufficient (s 3(f)) or an interest sufficient (s 40(3)); reasonably
  believes a report would disclose the name (s 43(1)); the person's own reasonable grounds (s 12(2)). The Court's
  satisfaction under s 44(3) is not decided: the answer says on which grounds it may act.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "senior next of kin", "married",
  "spouse" (s 3); "reportable death", "person held in care", "person held in custody" (s 12(1), (1A)). Asked: "not
  available", "Aborigine", "ordinarily resided", the CEO's care under the Care and Protection of Children Act 2007,
  custody under the Mental Health and Related Services Act 1998, "custodial correctional facility", certification by a
  "legally qualified medical practitioner" elsewhere. **Departure (fork F8):** the questions under ss 16, 22, 23 and 24
  ask "Are you the senior next of kin?" as a yes/no, with the s 3 question beside them, rather than repeat its ten inputs
  in each; the reportable-death questions (ss 12, 14, 15, 17) do repeat the seven facts of s 12(1).
- **One case is the text's natural unit.** Followed: one death.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 3 (senior next of kin, married, spouse); s 11(2); s 12(1), (1A), (2); s 13(1); s 14; s 15; s 16; s 17; s 21;
s 22; s 23; s 24 (as to the senior next of kin); s 37; s 38(2), (3); s 40(2), (3); s 43(1)(c), (2); s 44 (and s 44A(1) in
the answer text); s 45; the maximum penalties of ss 12(2), 13(1), 19(4), 32(2), 33(4), 36(2), 41(3), 43(2) and 46.

**Out, and why.**
- ss 1, 2, 4 to 10, 11(1), 11A, 47, 48, 49, Schedules 1 and 2: machinery (offices, appointments, delegation, records,
  regulations, repeal, transitional).
- s 12(3) to (5), s 13(2), s 25: duties of medical practitioners, custodians and police; not the family's seat (a
  further seat could take them).
- ss 18, 19(1) to (3), 20, 33(1) to (3), 41(1), (2), (4), 42, 39: the coroner's powers; met by the family only as
  inputs or not at all. Their offences (ss 19(4), 33(4), 41(3)) are in the penalty questions.
- ss 26, 27, 35, 46A, 46B: reports and recommendations to the Attorney-General and agencies, and their responses
  (s 46B(4) lets the coroner give the senior next of kin a copy: a permission to the coroner, not encoded).
- s 34: what the coroner must find; no question of the family turns on it. (s 34(3), no statement of guilt, is a
  limit on the coroner.)
- Part 5 (disasters, ss 28 to 33): not a death claimant's machinery, except the s 32(2) offence.
- s 43(1)(a), (b) and the rest of (c): the coroner's own grounds for non-publication; only the name, which the senior
  next of kin's request brings in, is encoded.
- No requirement ledger exists for the Northern Territory; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(e) -- `s 3 -- am I the senior next of kin` -- (e) stands beside (a) to (d): for an Aboriginal person the
  customary appropriate person is senior next of kin, and so is the person (a) to (d) name -- (e) displaces (a) to (d),
  or yields to them.
- **F2** s 3(c), (d) "where a spouse, son or daughter is not available" -- the same -- a son or daughter under 18 does
  not block a parent or sibling ((b)'s age carried over) -- any child, of whatever age, blocks them.
- **F3** s 12(2) -- `s 12 -- must I report the death` -- with no reasonable grounds to believe it unreported, the text's
  no for s 12(2) -- NOTHING (a duty whose condition is unmet).
- **F4** s 14(1), (2) "it appears to the coroner that the death is or may be a reportable death" -- `s 14 -- must the
  coroner investigate`, `s 15 -- must there be an inquest` -- a death reportable on the facts appears so; one that is
  not is answered "not required" with the "may be" route named -- the coroner's appearance asked as an input.
- **F5** s 15(1)(a) "held in care and custody" -- `s 15 -- must there be an inquest` -- encoded as written; a person in
  only one gets an answer giving both readings -- "and" read as "or" (finding 1).
- **F6** ss 16(2), 21(3), 23(3), 24(4) "may apply ... within" -- `apply to the Supreme Court within the time allowed` --
  a MUST with LEST BREACH, the end of the period inclusive (day 14 and hour 48 in time), an application before receipt
  counted as at time 0 -- a MAY (which can never breach), or the period ending before its last unit.
- **F7** s 16(2) "the person" and "notice of the decision mentioned in subsection (1)(b)" -- `s 16 -- am I in time to
  apply for an inquest` -- any person notified under s 16(1)(c); the notice is the written notice of the decision and
  reasons; the day of receipt not counted, the last day 14 days after it (Interpretation Act 1978 (NT) not deposited) --
  the senior next of kin only; the day of receipt counted.
- **F8** ss 16, 22, 23, 24 -- the questions there -- "Are you the senior next of kin?" asked as a yes/no -- its ten s 3
  facts asked in each question.
- **F9** s 17(2) -- `s 17 -- is the body under the coroner's control` -- encoded as written, no end to the bar; the answer
  says so -- read as "until the inquest is finished".
- **F10** s 22 "a deceased person who was a person held in custody" -- `s 22 -- must the coroner tell me of the autopsy`
  -- immediately before death, as s 12(1)(vii) -- at any time.
- **F11** ss 23(2), 24(2), 24(3) "until 48 hours after" / "at least 48 hours" -- the s 23 and s 24 "yet" questions -- at
  48 hours exactly the bar has lifted -- it lifts only after 48 hours.
- **F12** s 23(2) "Unless the coroner believes ..." and s 24(2) "unless the coroner is satisfied ..." -- the same --
  once met, the bar or notice requirement does not apply (the text's no for the bar) -- NOTHING.
- **F13** s 37 "not less than 14 days before" -- `s 37 -- the latest day to advertise the inquest` -- plain subtraction
  (published on the 1st for an inquest on the 15th is in time) -- 14 clear days (published by the 31st or 28th before).
- **F14** s 38(3) "other than on a prosecution for perjury" -- `s 38 -- can my answers be used against me` -- NOTHING-kind
  on a perjury prosecution -- JUST TRUE (admissible).
- **F15** s 46 "Maximum penalty: 40 penalty or imprisonment for 6 months" -- `the maximum fine in penalty units` -- 40
  penalty units -- no fine fixed.
- **F16** s 15, a person held in custody only (or care only) where the coroner also suspects unlawful killing -- `s 15 --
  must there be an inquest` -- the "care and custody" answer is given (it names s 15(2); s 15(1A) applies too) -- the
  s 15(1A) answer.
- **F17** s 43(1)(c) "including, where the senior next of kin ... have so requested, the name" -- `s 43 -- must the
  coroner suppress the name` -- without the request, NOTHING-kind ("including" leaves the list open) -- the text's no.

Sites decided without a fork line: "means" definitions (s 3 senior next of kin, s 12(1) reportable death) answer the
text's no when no paragraph is met; s 11(2) "is not admissible", s 45(1) "must not be called", s 38(2) "no longer
entitled", s 23(3) and s 24(4) court orders are flat negatives; "where" conditions (ss 16(1), 17(1), 22) failing are the
text's no (ruling (b)); the 14-day and 48-hour periods are periods the text fixes (ruling (a)); the "until" bars
(ss 17(1), 23(2), 24(3)) follow ruling (d); grants limited in their own wording to the senior next of kin (ss 16(1)(c),
22, 23(3), 24) or to a person of sufficient interest (s 40(3)) answer NOTHING-kind for anyone else.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding answers with choices from lists rather than MAYBE BOOLEANs: the answers marked "NOTHING-kind" are the
NOTHING answers, and those marked "the text's no" are JUST FALSE. NOTHING-kind tags appear in the questions under
ss 11(2), 16(1), 22, 23(3), 24, 38, 40(3), 43 and 45. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The "until" bars (ss 17(1), 23(2), 24(3)) answer "not yet" before the event and "no longer holds it back" after, and
never say the body has been released or the autopsy may lawfully proceed on other grounds. The deadlines to the Supreme
Court run through the regulative rule by EVALTRACE, as the note on ruling (d) asks.

## What the Act turns out to say

1. **s 15(1)(a) says "held in care and custody".** s 12(1)(vii) makes a death reportable for "a person held in care or
   custody", and s 6(4)(a), s 26 and s 41(2)(b) treat a death in custody as calling for an inquest-level process. Read as
   written, s 15(1)(a) makes an inquest mandatory only for a person held in both care and custody (a mental-health
   patient in police custody, say); a death in prison from natural causes with no injury in custody would not attract
   a mandatory inquest. "And" is probably meant as "or" (likely drafting error). Encoded as written, with both readings
   in the answer. Asserted.
2. **s 16(2) points to the wrong paragraph and has no clear subject.** It runs from "receiving notice of the decision
   mentioned in subsection (1)(b)"; (1)(b) is the duty to specify reasons, and the notice is given under (1)(c). "The
   person" has no antecedent: it may be the senior next of kin (who must be notified) or any person notified under
   (1)(c)(ii). Fork F7.
3. **s 17(2) has no end point.** Once the Supreme Court orders an inquest under s 16(3), "a coroner or coroner's clerk
   must not issue a certificate" permitting disposal; read literally, never, even after the inquest. Fork F9. Asserted.
4. **s 24(4) refers to "notice of the order under subsection (2)".** The exhumation order is made under s 24(1); s 24(2)
   is the notice. Read as notice of the order.
5. **Penalty typos.** s 46 reads "40 penalty or imprisonment for 6 months" (no "units", fork F15); s 41(3) reads "40
   penalty units. or imprisonment for 6 months" (a stray full stop). Asserted as 40 units and 6 months.
6. **The 48-hour holds give no time after the window.** Under s 23 the autopsy hold (until 48 hours after notice) and the
   window to apply to the Supreme Court (within 48 hours after notice) end together, and nothing in the Act stays the
   autopsy while an application is pending; where the coroner believes the autopsy must be done immediately, there is no
   hold at all. s 24 is the same for exhumation (the request hold runs from the request, not the notice). s 21 gives the
   applicant 48 hours after a refusal, with no hold on disposal of the body meanwhile unless the Court so orders.
7. **Senior next of kin can be more than one person.** Paragraphs (b) to (d) name a class ("son or daughter", "parent",
   "brother or sister") without ranking within it, and (e) is not ranked against (a) to (d) (fork F1). "Where a person is
   an Aborigine" presumably means the person who died. "Not available" is undefined.
8. **The coroner's record cannot prove what it records.** s 11(2) makes the record of findings, evidence and comments
   inadmissible as evidence of a matter contained in it, and s 45 bars calling the coroner as a witness. A family that
   wants to use the coroner's findings in a later claim must prove the facts again. Asserted.
9. **No time limit to challenge findings.** s 44(1) lets "a person" apply to have findings declared void, with no period,
   while s 16(2) allows only 14 days against a decision not to hold an inquest at all. Asserted.
10. **s 12(1)(b) reaches only Territory residents who die elsewhere uncertified.** A resident's violent death interstate
    whose cause was certified there is not reportable in the Territory (no Territory link for (a)). Asserted.
11. **The reprint is of 28 November 2022.** REPC019 was the current reprint on 6 November 2026. If a later amendment
    exists that the reprint does not show, this encoding would miss it.

## Before this is worth relying on

- The Interpretation Act 1978 (NT) for counting the 14 days (s 16(2), s 37) and for any rule moving a last day that
  falls on a weekend or holiday (forks F7, F13), not deposited.
- A lawyer's view on forks F1, F2, F5, F7, F9 and F13, and on findings 1 to 3; an independent test pass and a human gate.
- A check of the NT register that no amendment post-dates REPC019 (finding 11).
- The Coroners Regulations, if the family's notices or forms are to be encoded.
