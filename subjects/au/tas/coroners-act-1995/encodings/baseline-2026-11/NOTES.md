# Coroners Act 1995 (Tas) -- baseline encoding, the family of the person who died

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Focus: the provisions a person bringing or
answering a claim meets -- here, the family of a person whose death (often a workplace or road death, or a death in care
or custody) goes to the coroner, and who may later claim compensation or damages. The dates and times are in a small
module (`tco-dates.l4`, built-in date functions only, no daydate), the rules in `tco-rules.l4`, and the family's
questions in `tco-seat.l4`, which imports the rules and restates none. The cases are in `tco-cases.l4`. The shape
follows the Limitation Act 1974 (Tas) baseline in `subjects/au/tas/`.

## Edition

- **Act:** Coroners Act 1995 (Tas), No. 73 of 1995, consolidated version published 2025-12-01 and current at point in
  time 2026-11-06, as deposited at `../../registers/source-bundle/act-1995-073.txt` (text sha256 as recorded in the
  `.meta.json`, fc128fbe...a1a60f5371), retrieved from legislation.tas.gov.au on 6 November 2026. It includes s 3B and
  s 58B (No. 5 of 2023) and s 58C (No. 17 of 2025, applied 1 December 2025).
- **Numbers set elsewhere:** none that the encoded provisions need. The Act fixes its own periods (14 days, 28 days,
  48 hours, 12 months) and penalties. The value of a penalty unit (Penalty Units and Other Penalties Act 1987) is not
  deposited, so penalties are answered in penalty units. The Coroners Rules and Regulations (fees, the s 58B
  information, the s 34 and s 49 notices) are not deposited and set no number used here.
- **Borrowed terms asked as facts:** "spouse", "significant relationship" and "caring relationship" (Relationships Act
  2003), "person held in care" and "person held in custody" (defined in s 3 by reference to other Acts), "medical
  practitioner", "Aboriginal person", "illicit", "sufficient interest", "not available", "charged before justices".

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
a deliberately wrong assertion was run once in a scratch file to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range. Before the
rules were written, a probe confirmed how the stable `l4` treats a deadline: `MUST ... WITHIN 14` is FULFILLED by the
step at 14 and breached at 15; `SHANT ... WITHIN 48` is breached by the act at 48 and FULFILLED by the act at 49.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tco-dates.l4` | 0 | 0 | 0 | 0 |
| `tco-rules.l4` | 0 | 0 | 0 | 0 |
| `tco-seat.l4` | 0 | 0 | 0 | 0 |
| `tco-cases.l4` | 0 | 0 | 204 | 204 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the
14th day after notice and the 15th (17 / 18 March 2026), the day of notice itself and the day before, across a year end
(25 December 2026 to 8 January 2027) and across 29 February (20 February to 5 March 2028); 48 hours to the minute and one
minute over (14:30 on 10 March to 14:30 on 12 March 2026), across a month end (23:15 on 30 April to 23:15 on 2 May);
the autopsy and exhumation bars at 47 hours 59 minutes and at 48 hours; 28 days to the day and the day after, an agreed
longer period, a copy given late, and a copy given after the day asked about; 12 months to the anniversary and the day
after; every penalty.

## Seat

**The family member** (`tco-seat.l4`): the individual the Act is applied to when someone has died -- above all the
**senior next of kin** (s 3A), whom the Act notifies and lets go to the Supreme Court -- and any other person a coroner
considers has a **sufficient interest** in a death, fire or explosion, including the person whose property the coroner
or the police hold. "Am I the senior next of kin?", "Is it a reportable death, and must I report it?", "Must there be an
inquest?", "Will it wait for the criminal case?", "By when can I go to the Supreme Court?", "Can the autopsy or
exhumation go ahead yet?", "When can the body be released?", "What can I do at the inquest?", "Can what was said there
be used in my claim?", "Must I be given the records, and by when?", "Can the findings be reopened or voided?", "What
happens to my property?", "What is the most I can be fined?". No seat for the coroner, the Chief Magistrate, the
Attorney-General, the State Forensic Pathologist, the police or the Supreme Court: their judgments and orders are asked
as facts. s 19 and the offences are asked from the same seat (the family member who finds the death, enters a scene or
publishes a report).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no instrument sets a number used here (see
  Edition).
- **The actors the text names.** Followed: the senior next of kin, the person with a sufficient interest, the person who
  requested, the coroner, the Chief Magistrate, the Attorney-General, the Supreme Court, the coronial authority, the
  police officer, the Commissioner of Police, the person to whom s 60 applies.
- **Judgments answered conditionally.** Followed: "appears to the coroner" (s 21(1)), "suspects" (s 24(1)(a)), "not
  satisfied ... natural causes" (s 24(1)(ea)), "satisfied ... not contrary to the public interest" (s 26A(3)), "reason to
  the contrary" and "sufficient cause" (s 25), "considers has a sufficient interest" (ss 27, 37, 42, 52, 58), "believes
  ... immediately" (s 38(2)), "satisfied it is not possible" (s 39(2)), "satisfied, on reasonable grounds" (s 58C(5)),
  "satisfied that" a ground (ss 58, 58A), "likely to be required" (s 61), "not available" (s 3A) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "reportable death" (s 3), "senior next of kin"
  (s 3A), "coronial record" (s 58C(1)) and the offences listed in s 25(2) are worked out from facts.
- **One case.** One death (or one fire or explosion), from one family member's position.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 3 ("reportable death", "death", "spouse"), 3A, 3B, 19 (except (2)), 20(1), 21, 23(4), 24, 24A, 25, 26, 26A,
27, 29(2), 32, 34(3), 37, 38, 39, 42(1), (3), 44, 46(2), 49(3), 52, 53(4), 54, 57(2), 58, 58A, 58C (the power to forbid
publication, (7) and (8), only as the offence in (9)), 59A(3)(c), (4), 60, 61, 62, 63, 64, 65, 66.

**Regulative rules:** three, each run by EVALTRACE inside questions that take only plain facts.
- The 14-day and 48-hour steps (ss 26(2), 26A(2), 27(3), 37(3), 38(3), 39(4), 44(2)) as what the person must do to keep
  the right: `PARTY the person entitled to take the step MUST take the step WITHIN` the days or minutes, `LEST BREACH ...
  BECAUSE` the time has passed (fork F1).
- The coronial authority's duty to provide a copy within 28 days or the agreed period (s 58C(4)): `PARTY the coronial
  authority MUST provide a copy of the record WITHIN` the days, `LEST BREACH BY the coronial authority BECAUSE` -- the
  failure the senior next of kin may appeal (s 58C(10)(b)).
- The 48-hour bars on autopsy and exhumation (ss 38(2), 39(2), (3)): `PARTY the person who would perform it SHANT perform
  the autopsy or exhumation WITHIN 2879` minutes, `LEST BREACH ... BECAUSE` it was done too early (fork F2).

**Out, and why:**
- ss 1, 2, 4, Part 2 (ss 5-16), Part 3 (ss 17-18A), ss 22, 41, 50, 67, 68, 69, 69A, 70-73: commencement, the courts and
  offices, directions, validation, protection of officials, rules, regulations, annual report, repeal, transitional,
  administration (machinery). s 68 is noted in finding 5.
- ss 19(2), 20(2), 30, 47, 48, 53A, 59B: duties and powers of officials that give the family no right or step (s 53A
  deferral of Right to Information access is a direction to an agency).
- s 23(1)-(3), (5): the referral of possible Aboriginal remains is between the coroner and an approved organisation; only
  the end of jurisdiction (s 23(4)) is in.
- ss 28, 31, 33, 35, 36, 45, 51, 53(1)-(3), (5), (6), 55, 56, 59(1)-(7): what the coroner must find and the coroner's
  powers; they give the family no step with a time or a test. s 28(4) and s 45(3) (no finding that a person is guilty)
  and s 28(5) (a report on care in custody) are noted here only.
- s 34(1), (2), (4)-(7), s 49(1), (2), (4)-(7): restricting access to a scene. Only the offence of entering is in; the
  review by the Chief Magistrate turns on rules and the Chief Magistrate's procedure, not deposited.
- ss 40, 43: when a fire or explosion may or must be investigated or have an inquest, which turns wholly on the
  coroner's belief or a direction; the request, the duty to inform and the appeal (ss 42, 44) are in.
- s 57(1), (3): the power to forbid publication is the coroner's; only the offence in (2) is in.
- s 58B: the information the Chief Clerk must give the senior next of kin is "specified in the regulations", which are not
  deposited.
- s 59A(1)-(3)(b): the police power itself; only what then happens to the thing is in.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 26(2), 26A(2), 27(3), 37(3), 38(3), 39(4), 44(2) "may apply" within a time -- `the step must be taken within`
  -- a permission lost when the time passes, modelled as an obligation to keep it (`MUST ... LEST BREACH`) -- a `MAY` with
  no consequence, which cannot make the time bite.
- **F2** ss 38(2), 39(3) "until 48 hours after", s 39(2) "at least 48 hours' notice" -- `the 48-hour bar is broken by
  acting at` -- counted in minutes; barred to 47 hours 59 minutes, allowed from exactly 48 hours -- allowed only after
  48 hours (from 48 hours 1 minute), or counted in whole hours.
- **F3** "within 14 days after receiving notice" (ss 26(2), 26A(2), 27(3), 44(2)), "within 28 days after the request"
  (s 58C(4)) -- `the 14-day window for`, `the s 58C(4) last day for` -- the day of notice or request is not counted, so the
  last day is the 14th (28th) day after it, and a step on the day of notice itself is in time -- the Acts Interpretation
  Act 1931 (Tas) rule, not deposited, may be read to the same effect or to end a day earlier.
- **F4** s 38(2) "Where a request has been made ... unless the coroner believes that an autopsy needs to be performed
  immediately" -- `s 38 -- the autopsy is barred` -- no request, or the coroner's belief, gives `JUST FALSE` (s 38 does not
  bar it) -- `NOTHING` (s 38 silent).
- **F5** s 54 "other than a prosecution for perjury", and use against someone other than the witness -- `ss 29, 46, 54, 64
  -- it can be used in my court case` -- `NOTHING` (s 54 does not stop it; whether it is admissible is for the law of
  evidence) -- `JUST TRUE`.
- **F6** s 58C(10)(b) "a failure to provide a copy ... as required under subsection (4)" -- `s 58C(4), (10)(b) -- the
  authority has failed to provide the copy` -- a copy given after the time is a failure, and nothing is a failure before
  the time ends -- a late copy curing the failure.
- **F7** s 59A(4) "within 12 months of the power being exercised" -- `s 59A -- what happens to the item the police took` --
  an investigation that commences on the anniversary is in time; from 29 February the anniversary is 28 February; an
  investigation that commences after the day asked about does not yet count -- the day before the anniversary as the
  last day.
- **F8** s 3A(i), the appropriate person by Aboriginal custom, which has no "if [the persons above are] not available" --
  `s 3A -- am I the senior next of kin` -- a person ranked senior under (a)-(h) is answered first; otherwise the
  appropriate person "may be" the senior next of kin -- (i) displacing (a)-(h) whenever the deceased was Aboriginal.
- **F9** s 3A "a child", "a parent", "a sibling", "an executor", and (c) "another spouse" -- same -- several people in the
  same place are "equally placed" and the Act does not choose; the partner in a registered caring relationship ("the
  person") is singular -- one of them (the eldest, the first to act) being chosen.
- **F10** s 21(2) "need not investigate a death if an investigation or inquest is held in another State" against the
  s 24(1) duty -- `ss 21-26A -- must there be an inquest` -- s 21(2) relieves the duty unless the Attorney-General
  directs, and an Attorney-General's direction of an inquest (s 24(1)(g)) counts as directing otherwise -- s 24(1)
  prevailing.
- **F11** s 25(1)(a) "in the absence of reason to the contrary" -- `s 25 -- is the inquest adjourned for the criminal
  case` -- where there is such a reason, s 25 does not require the adjournment -- the coroner still bound to adjourn
  unless the reason is recorded.
- **F12** s 26A(3) "despite section 24(1)(ea)" -- `ss 21-26A -- must there be an inquest` -- it lifts only (ea): where
  another head also applies, the inquest is still required -- the request ending the duty altogether.
- **F13** s 32(2), (4) -- `s 32 -- the disposal certificate is barred` -- whether the s 27 or s 37 time is still running is
  an input (the 14-day and 48-hour questions answer it); s 32(4) reaches only the s 27 time -- s 32(4) reaching the s 37
  time too.
- **F14** s 37(1) "If a coroner has jurisdiction to investigate a death" -- `ss 27, 37, 42 -- I may ask the coroner` --
  required for an autopsy request only; s 27(1) and s 42(1) have no such words -- the same condition read into s 27(1).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags and encodes "until" bars. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 and s 58C(1), the "if" conditions of ss 3B, 58A(3), the "where" of s 38(2),
the periods of ss 26(2), 26A(2), 27(3), 37(3), 38(3), 39(4), 44(2), 58C(4), and the flat negatives "is not evidence"
(ss 29(2), 46(2)), "is not admissible" (s 54), "is not a compellable witness" (s 64), "is not to exercise" (s 58(3)) and
"must not issue" (s 32(2), (3)) give `JUST FALSE`; the three "until" bars (ss 32(2), 38(2), 39(3)) and the "at least 48
hours' notice" of s 39(2) are encoded as bars under ruling (d). `NOTHING` is answered for a person outside the grant of
ss 26(2), 26A(2), 27(1), (3), 37(1), (3), 38(3), 39(4), 42(1), 44(2), 52(4) and for an investigation without an inquest
under s 58A (*a grant limited in its own wording*), and for s 54 outside its words (*the text is silent*, F5).

## What the Act turns out to say

1. **Evidence given at the inquest cannot be used against the witness in a later damages claim, and the coroner's record
   is not evidence of its facts.** s 54 bars any civil or criminal use of a witness's inquest evidence against that witness
   (perjury apart), and ss 29(2) and 46(2) say the record "is not evidence in any court of any fact asserted in it"; s 64
   makes the coroner non-compellable. A family that wants to rely on what an employer's witness said at a workplace death
   inquest must prove it again. Asserted.
2. **The body can be released while the senior next of kin's own application time is running.** s 32(2) holds the
   disposal certificate back only for applications "under section 27 or 37" (a requester's inquest or autopsy
   application); it says nothing of the senior next of kin's application under s 26(2) after a decision not to hold an
   inquest, or of an objection to autopsy under s 38(3). Encoded as written (the s 32 question asks only about s 27 and
   s 37).
3. **The 48-hour application window and the 48-hour bar end together, with no stay.** Under s 38(2) and (3), and s 39(3)
   and (4), the autopsy or exhumation is barred for 48 hours and the senior next of kin has 48 hours to apply to the
   Supreme Court; the Act gives no stay while an application made in time is undecided. An application filed at hour 47
   does not of itself stop an autopsy at hour 48. Asserted (the autopsy is not barred at exactly 48 hours, F2).
4. **s 39(4) points to the wrong subsection.** It runs from "notice of the order under subsection (2)", but the order to
   exhume is made under subsection (1); subsection (2) is the notice. Read as the notice of the s 39(1) order.
5. **s 68 leaves out one older and the newer applications.** It requires applications "under sections 26 (2), 37 (3), 38
   (3), 39 (4), 44 (2), 58A(1) and 63" and the s 58(7) appeal to follow the Supreme Court rules, but not the s 27(3)
   application (though its twins s 26(2) and s 44(2) are listed), the s 3B appeal (2023) or the s 58C appeals (2025).
   Not encoded (machinery).
6. **s 3A(c) asks for the approval of a spouse who is "not available".** A second spouse may act only "if the spouse
   referred to in paragraph (b) is not available" and "has the approval of" that same spouse. Encoded as written (both
   facts asked); the approval may be impossible to get.
7. **s 3A does not choose among equals, nor place paragraph (i).** "A child", "a parent", "a sibling" and "an executor"
   may each be several people; (i) has no "not available" condition linking it to (a)-(h). s 3B (2023) assumes "a
   decision made under this Act specifying who is the senior next of kin", but no section says who makes it or how
   (F8, F9). "Not available" is undefined. Asserted.
8. **Only the senior next of kin can stop a workplace death inquest, and only under that head.** s 26A lets the senior
   next of kin ask, within 14 days, that a s 24(1)(ea) inquest not be held; it does not reach a workplace death that also
   falls under another head (homicide suspected, a death in custody), nor any other family member. Asserted (F12).
9. **Reporting a death or asking for a fire investigation carries a duty to inform.** A person who reports a death
   (s 20(1)) or asks the coroner to investigate a fire or explosion (s 42(3)) "must give to the coroner any information
   which may help", on pain of 10 penalty units. Asserted in the penalty questions.
10. **A family member has no duty to report a death in custody.** s 19(1) excludes the deaths in s 19(4), which only the
   custodian or the officer must report. Asserted.
11. **Drafting:** s 3 (a)(vi) and s 28(1)(f) are omitted paragraphs; s 28(1)(e) ends with a full stop before the omitted
   (f); "Coroner" is capitalised in s 59B(3) only. No effect on the encoding.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The Acts Interpretation Act 1931 (Tas) rule for reckoning days and hours (F2, F3, F7), the Penalty Units and Other
  Penalties Act 1987 for the value of a penalty unit, and the Coroners Rules and Regulations (s 58B information, notices,
  the review procedure under ss 34(7) and 49(7)).
- A lawyer's view on findings 2, 3, 5 and 7 and forks F1, F2, F5, F8, F10 and F12; an independent test pass and a human
  gate.
