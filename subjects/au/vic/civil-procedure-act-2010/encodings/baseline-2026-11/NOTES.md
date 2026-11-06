# Civil Procedure Act 2010 (Vic) -- baseline encoding, the party

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`cpa-rules.l4`), the
dates in a small one (`cpa-dates.l4`), and the party's questions in `cpa-seat.l4`, which imports the rules and restates
none. The cases are in `cpa-cases.l4`.

## Edition

- **Act:** Civil Procedure Act 2010, Act No. 47/2010, Version No. 022, incorporating amendments as at 30 September 2026,
  deposited at `../../registers/source-bundle/civil-procedure-act-2010.txt` (sha256 5fc62048...dbb3921d as committed), a
  plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act fixes one period of its own (2 years, s 41(5)(a)(ii)). The rules of court may set
  another (asked, in months), and the penalty interest rate of s 29(1)(c)(i) comes from the Penalty Interest Rates Act 1983
  (not deposited; no question computes interest). No regulations under s 4(4) prescribing an excluded Act are deposited:
  asked as a fact. The rules of court (Supreme Court (General Civil Procedure) Rules 2025, County Court and Magistrates'
  Court rules) are not deposited: each place the Act defers to them is an input.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cpa-dates.l4` | 0 | 0 | 0 | 0 |
| `cpa-rules.l4` | 0 | 0 | 0 | 0 |
| `cpa-seat.l4` | 0 | 0 | 0 | 0 |
| `cpa-cases.l4` | 0 | 0 | 188 | 188 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the s 41(5)
window on its first day (15 March 2025 for a case begun 15 March 2027), the day before, the day of commencement and the day
after, with a 12-month rules period, and from 29 February 2028 (window opens 28 February 2026); the s 26(2) disclosure on
the day of awareness, the last reasonable day and the day after, still open on the last day and late the day after, and
against a court-directed day; each s 3 exclusion that overlaps an inclusion; each sanction against the side it names and the
other side.

## Seat

**The party** (`cpa-seat.l4`): the individual who is a party to a civil proceeding in the Supreme, County or Magistrates'
Court of Victoria, whether bringing the claim (an injured person, worker, claimant, beneficiary, employee) or answering
it. "Does the Act apply to my case?", "Which overarching obligations bind me?", "Am I forbidden to make this claim, or take
this step?", "Must I try to settle, and narrow the issues?", "Must I disclose this document, and was I in time?", "May I use
what was disclosed to me?", "Can I still seek orders for the other side's breach?", "Is this a substantive document, who
certifies, and who files the proper basis certification?", "What can the court do to me for a case management or discovery
breach?", "May I apply for summary judgment, and can it be given against me?", "Must I seek directions about expert
evidence, and may I call another expert?", "Can I be sent to mediation without my consent?".

The s 10 question can also be asked by an individual who is a witness, an expert witness, or a person helping a party (a
relative paying the costs): its first input is the role. No seat for the court, the lawyers, the insurer or a litigation
funder: the court's findings, satisfaction, leave and orders are asked as facts; what a lawyer must do (ss 41(5)(b), 42) is
encoded as what the party must see done.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: none is deposited; the rules-of-court period and
  every deferral to the rules of court are inputs.
- **The actors the text names.** Followed: the party (plaintiff, defendant, by counterclaim), witness, expert witness,
  single joint and court appointed experts, legal practitioner, litigation guardian, person in control by statute or
  insurance, the court.
- **Judgments answered conditionally.** Followed: "satisfied", "reasonably believes", "reasonable basis", "proper basis",
  "frivolous", "vexatious", "abuse of process", "critical", "interests of justice", "earliest reasonable time", leave and
  orders are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "civil proceeding", "court", "substantive
  document", "overarching obligations" (s 3), and who the obligations bind (s 10) are worked out; "privilege", "affidavit of
  documents", "litigation guardian", "legal practitioner" are asked.
- **One case.** One civil proceeding, seen by one party.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 3 (civil proceeding, court, overarching obligations, substantive document), 4, 10, 18, 19, 22, 23, 26, 27, 29,
30, 31, 41, 42, 44, 45, 51, 55A(4), (5), 56, 57, 60, 61, 62, 63, 64, 65G, 65J(4), 65L(6), 65N, 65O, 65P(1), (4), 66(2), 67.
ss 16, 17, 20, 21, 24, 25 are in through the s 10 question (who they bind); ss 28 and 46 (the court may take a breach or a
failure to certify into account, in costs and otherwise) are in the descriptions of the s 29 and s 45 questions.

**Regulative rule:** one. s 26(2): the person MUST disclose the document's existence to each party WITHIN the days from
becoming aware to the earliest reasonable time (an input) or the time the court directed, LEST breach. Run by EVALTRACE
inside the exported question `Is my disclosure in time`, which takes only dates and yes/no facts, through a helper in the
shape of the Supreme Court Act 1986 encoding's.

**Out, and why:**
- ss 1, 2, 5, 6 (purposes, commencement, Crown, Charter and privilege preserved): machinery and interpretation.
- ss 7, 8, 9 (the overarching purpose, the court's duty to give effect to it, the objects and matters it regards): they
  govern how the court exercises its powers; no fact test for the party.
- ss 11-15 (the obligations' reach over a proceeding, their priority, legal practitioners' duties): ss 11, 12 add no fact
  the party states (s 11 is folded into "in relation to a civil proceeding"); ss 13-15 are the lawyer's, who has no seat.
- ss 16, 17, 20, 21, 24, 25 as questions of their own: each is a standard ("honestly", "cooperate", "reasonable
  endeavours", "promptly") whose only fact is whether the person met it, which is the court's judgment under s 29.
- ss 47-50A, 52, 53 (case management powers, statement of issues): powers of the court with no fact test; their sanction
  (s 51) is in.
- ss 54, 55, 55A(1)-(3), (6), (7), 55B, 55C, 58, 59 (discovery orders, affidavit of document management, oral
  examination): powers of the court; the party's duties under them come from the order and the rules of court.
- s 65 and Part 4.5 (ss 65A-65E, costs memoranda and costs orders): powers of the court, not in the focus; s 65C(2A) lists
  matters the court may consider when capping costs, with no test.
- ss 65F, 65H, 65I, 65J(1)-(3), 65K, 65L(1)-(5), (7), 65M, 65N(1), 65P(2), (3), 65Q: the court's powers over experts and
  how their evidence is given; the party's bars and duties (ss 65J(4), 65L(6), 65N(2), 65O, 65P(1), (4)) are in. s 65J(1)
  (conference content not referred to at a hearing) is an evidence rule like s 67 and could be added.
- ss 66(1), (3), 68, 69 (referral power, judicial immunity, interaction): the court's.
- ss 70, 71 (rules of court, regulations): machinery.
- ss 72-87 (transitional): spent. They applied the Act's Parts to proceedings begun before 2011, 2013 and 2015.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 10(1)(d) "in so far as that person exercises ... control ... or any influence" -- `s 10 -- the overarching
  obligation applies to me` -- a helper with no control or influence: NOTHING (a scope limit without "only") -- JUST FALSE.
- **F2** s 10(3) "(other than the overarching obligations specified in sections 18, 19, 22 and 26)" -- same function --
  an expert witness and one of those four: JUST FALSE -- NOTHING (the "other than" leaves them unaddressed for experts).
- **F3** s 19 "must not take any step ... unless the person reasonably believes" -- `s 19 -- I must not take the step` --
  the "unless" met: JUST FALSE (s 19 does not forbid it) -- NOTHING.
- **F4** s 23 "If a person ... cannot resolve a dispute wholly by agreement" -- `s 23 -- I must try to narrow the issues` --
  the "if" unmet (wholly resolved): JUST FALSE -- NOTHING.
- **F5** s 41(5)(a) "within ... 2 years prior to the current proceeding" -- `s 41(5)(a) -- my earlier certification is
  within the period` -- counted back from the day the current proceeding was commenced, the first day of the window
  included, and the commencement day itself included -- counted from the party's own first substantive document, or with
  the first day excluded.
- **F6** the same, month arithmetic -- `the date` n `months before` -- the same day of the month n months earlier, or that
  month's last day where it is shorter (29 February 2028 less 24 months is 28 February 2026) -- 1 March 2026.
- **F7** s 45 "Unless a court otherwise orders, a court may not prevent ..." -- `s 45 -- the court may stop my filing for
  want of certification` -- the "unless" met (the court has so ordered): JUST TRUE -- NOTHING (s 45 merely stops barring).
- **F8** "who"-clauses read as "where" conditions: s 55A(5) "A party who excludes any privileged documents", s 65L(6) "Any
  party who knows" -- `s 55A(5) -- I must give a list of the privileged documents`, `s 65L(6)(a) ...`, `s 65L(6)(b) ...` --
  the clause unmet: JUST FALSE (ruling (b) of 2026-11-05) -- NOTHING (a scope limit).
- **F9** s 64 "Despite anything to the contrary in this Part ..., a court may order that a civil proceeding proceed to
  trial" -- `ss 63, 64 -- the court may give summary judgment against me` -- once the s 64 order is made, JUST FALSE --
  the order displaces summary judgment only for the part it names (asked as one fact).
- **F10** s 41(3), (4), (5) -- `s 41 -- who makes my overarching obligations certification` -- the exemption of (5) first,
  then the person in control under (4), then the litigation guardian under (3), each a "may" (the party may still certify
  personally) -- another order where both (3) and (4) hold.
- **F11** s 42(1)(c), (d) with (1C) -- `s 42 -- who files the proper basis certification` -- the administrative exemption
  of (1C) ("Despite subsections (1) to (1B)") prevails even over a court direction under (1)(d) -- a direction prevails.
- **F12** s 26(2) "at -- (a) the earliest reasonable time ...; or (b) such other time as a court may direct" -- `s 26(2) --
  what became of my disclosure` -- a direction replaces the earliest reasonable time, and disclosure on the last day of
  either is in time -- disclosure must be at, not by, the time (earlier disclosure is impossible before awareness, so the two
  agree).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 (civil proceeding, court, substantive document), "does not apply" (s 4(2),
(3), (4), s 10(2), s 26(3), s 65G(2)), "must not" (ss 18, 19, 65L(6)(a)), "may not" (s 45, s 65J(4), s 65O), "except by
leave" and "without leave" (ss 65J(4), 65O, 65P(4)), "unless" (ss 22, 23, 57, 65G(1), 65P(1), 67), the "if" conditions of
ss 23, 29, 31(2), 44, 51, 56, 63, 64, 65N and 66(2), and the period "prior to the engagement" (s 65L(6)(a)) give `JUST
FALSE`. `NOTHING` is answered where s 10(1)(d), s 18, s 26(1), s 29(2), s 42(1), s 51(b), (c), s 55A(4), s 56(2)(b), (c),
(j), ss 61-62, s 67 or Part 4.6 do not reach the case (*limited by its own wording*, *silent*), and where the rules of
court or the rules of evidence decide (s 27(4), s 66(2)) (*points outside the text*).

## What the Act turns out to say

1. **s 41(5): one earlier certification or two, and which "jurisdiction".** The exemption needs the party to be "involved
   in more than one civil proceeding" and to have certified "in other civil proceedings [plural] in the same
   jurisdiction". Read literally the plural asks for two earlier certifications; read with "more than one" (which counts
   the current one) one earlier certification is enough. "The same jurisdiction" is undefined: the same court, or Victoria.
   Encoded: one earlier certification suffices; "same jurisdiction" asked as a fact. Asserted.
2. **s 41(5)(a)(ii) counts "2 years prior to the current proceeding",** not prior to a date. Encoded from the day the
   current proceeding was commenced (F5). Asserted at the edges.
3. **s 3 "substantive document" includes and excludes the same things.** (a) "an originating motion" and (z) "any
   originating motion filed under Chapter III of the Rules of the Supreme Court"; (m) "an application which commences a
   civil proceeding" and (u) "an application under section 299 of the Workplace Injury Rehabilitation and Compensation Act
   2013". The "but does not include" is taken to prevail. "The Rules of the Supreme Court" is not defined; the Supreme Court
   (General Civil Procedure) Rules 2015 were replaced by the 2025 Rules from 1 January 2026 (see
   `subjects/au/vic/README.md`), so which "Chapter III" (z) means is for a lawyer. Asserted.
4. **s 51(b) and (c) are not tied to the person in breach.** (d) to (f) speak of "the person" who contravened, but (b)
   "strike out or limit any claim made by a plaintiff" and (c) "strike out or limit any defence ... filed by a defendant,
   and give judgment accordingly" do not. Read literally, a plaintiff's breach would let the court strike out a defence.
   Encoded only as against the party's own claim or defence; the other side's: `NOTHING`. Asserted.
5. **Experts and s 23.** s 10(3) spares expert witnesses s 22 (trying to resolve the dispute) but not s 23 (narrowing the
   issues "if a person ... cannot resolve a dispute wholly by agreement"), which presupposes the person is in the dispute.
   Encoded as the text reads: s 23 binds an expert. Asserted.
6. **s 27(4) makes discovery necessary, not sufficient.** Documents exchanged under s 26 are "required to be discovered
   ... to be admissible"; whether a discovered one is admitted is for the rules of evidence. Not discovered: `JUST FALSE`;
   discovered: `NOTHING`. Asserted.
7. **s 31(2) refers to "the period specified in section 30(2)",** but s 30(2) specifies no period, only a point
   ("prior to the finalisation"), which s 30(3) moves to the day of the last order, including a costs order. Read as "until
   after the proceeding was finalised". Whether an application is in time cannot be known until the last order is made;
   asked as one fact. Asserted.
8. **s 4(2)(h) still excludes the Victims of Crime Assistance Act 1996** and does not name the Victims of Crime Financial
   Assistance Scheme Act 2022 that replaced its scheme from 18 November 2024 (`subjects/au/vic/README.md`). Encoded as
   written: only the 1996 Act is listed. Asserted.
9. **s 26(2) has no fixed time.** "The earliest reasonable time after the person becomes aware" is a judgment; the encoding
   takes its last day as an input and runs the duty from there (one regulative rule). s 65G ("as soon as practicable") and
   s 44(2) (the same) were left as yes/no duties for the same reason.
10. **Conversion.** s 4(2)(ea) and (ja) and s 70(1)(ea)-(ed) print without the indent of their neighbours; the text is
    otherwise as the Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Supreme Court (General Civil Procedure) Rules 2025, the County Court Civil Procedure Rules and the Magistrates' Court
  General Civil Procedure Rules (discovery, certification periods and forms, expert directions, administrative exemptions),
  none deposited.
- Any regulations under s 4(4) prescribing excluded Acts; the Penalty Interest Rates Act 1983 for s 29(1)(c)(i).
- A lawyer's view on findings 1, 3, 4 and 7 and forks F1, F7, F8, an independent test pass and a human gate.
