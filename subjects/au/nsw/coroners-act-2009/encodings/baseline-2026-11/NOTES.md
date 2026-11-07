# Coroners Act 2009 (NSW) -- baseline encoding, the family of the person who died

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 21 November 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). One regulative rule (the senior next of kin's
48 hours to apply to the Supreme Court after the coroner's notice, s 97(1)) run by `EVALTRACE` inside two exported
questions that take only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline,
no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a claimant meets: a
family member whose relative died at work, on the road, in care, in custody or after medical treatment meets the coroner
before any claim, and the inquest, the post mortem and the coroner's file shape the evidence for that claim. The Act is
large (Chapters 1-10 and three Schedules); the Parts the family meets are encoded, and the rest is listed under Scope.

## Edition

- **Act:** Coroners Act 2009 No 41, corpus document `nsw_legislation:2024-11-21/act-2009-041` (in force 21 November
  2024), deposited at `../../registers/source-bundle/act-2009-041.txt` (sha256 c6bfae3d...a08dc79 as committed), taken
  from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge.
  Not the authorised text.
- **Not deposited:** the Coroners Regulation (excluded health-related procedures, s 6(3); the prescribed assistance of
  s 24(1)(f); specialist disability accommodation premises, s 24(3); the file-copy fee, s 65(2)(b); disposals the
  regulations authorise, s 100); the Births, Deaths and Marriages Registration Act 1995 (the documents s 100(3) names);
  the Children and Young Persons (Care and Protection) Act 1998 (reports, s 24(1)(b), (c)); the Crimes (Sentencing
  Procedure) Act 1999 (the value of a penalty unit). Each is asked as a fact, or the answer is given in penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cor-coroners.l4` | 0 | 0 | 0 | 0 |
| `cor-cases.l4` | 0 | 0 | 197 | 197 |

Every expected value was worked by hand from the text, with the edges: a death exactly 100 years before today and the day
before (s 19); a risk-of-harm report exactly 3 years before the death, the day before, and a report after the death
(s 24(1)(b), (c)); a child in care at 17 and at 18; an application to the Supreme Court at 48 hours and at 48.5 (s 97(1));
a post mortem at 47 and 48 hours after the notice, and a notice that wrongly gives less than 48 (s 96(4)(a)); an order to
resume 13 and 14 days after notice to the State Coroner, and 14 days across a year end (s 79(2A)); each tier of the
senior next of kin ladder with the tier above present and absent; a superseded spouse (s 4); each disposal document for
an adult and for a stillborn child (s 100(3)); each offence's maximum penalty.

## Seat

**The family member of the person who died**: the spouse or de facto partner, a parent, an adult child, a brother or
sister, a guardian, an executor -- whoever is a "relative" (s 5) or a "senior next of kin" (s 6A). Every exported
question is one that person would ask ("Am I the senior next of kin?", "Must there be an inquest?", "Will the coroner let
me appear?", "Can the post mortem go ahead now?", "Is my Supreme Court application in time?", "May I bury the body?",
"Can that witness's certified evidence be used in my claim?"). The Act's duties are almost all the coroner's, the State
Coroner's or the Supreme Court's; they are encoded as what they mean for the family member. The family member's own
duties (report a reportable death, s 35; not bury without authority, s 100; not publish in breach of an order, ss 74-76)
are encoded with their maximum penalties. Officials (the coroner, the State Coroner, the Minister, the police, the
Supreme Court) get no seat. No second seat is written: the Act puts duties on doctors (s 38) and witnesses (ss 53, 62),
but neither is a party to a claim in the sense of this work, and their duties appear here as what they mean for the
family.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the Coroners Regulation is not deposited, so
  what it prescribes is asked (see Edition).
- **The actors the text names.** Followed: coroner, assistant coroner, State Coroner, senior coroner, Minister, Supreme
  Court, medical practitioner, police officer, relative, senior next of kin.
- **Judgments answered conditionally.** Followed: "it appears to the coroner", "in the opinion of the coroner", "if the
  coroner is satisfied", "sufficient interest", "exceptional circumstances", "sufficiently disclosed", "necessary or
  desirable in the interests of justice" are inputs, and each `@desc` says whose judgment it is.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "spouse" (s 4), "relative" (s 5), "reportable
  death" (s 6), "senior next of kin" (s 6A), "child" (s 24(3)), the s 75(3) relatives, "appropriate disposal
  authorisation" (s 100(3)) are worked out; "de facto partner", "child in care" (beyond its age), "person in the relevant
  group", "next of kin" (s 54, undefined), "homicide" and the BDM Act documents are asked.
- **One case.** One death (or suspected death), and one family member asking.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 "spouse"; s 5 (relative); s 6 (reportable death); s 6A (senior next of kin); s 18 (connection with the State);
s 19 (100 years); s 21 (general jurisdiction); ss 22-24 (senior coroners' exclusive jurisdiction: custody, police
operations, children, disability); s 25 (dispensing); s 26 (reasons); s 27 (inquests required); ss 28-29 (directions);
s 35 (duty to report); s 38 (death certificates); s 54 (notice of the inquest); s 56 (the coroner's right to the body);
s 57 (leave to appear); s 60 (asking for a witness); s 61(7) (certified evidence in later proceedings); s 65 (the
coroner's file); s 75 (self-inflicted deaths); s 79 (resuming a suspended inquest); s 81 (findings); s 83 (fresh
inquests); ss 84-87 (Supreme Court orders); s 89(6) (dispensing with a post mortem); s 90(4)-(6) (whole organs); s 91
(exhumation); s 94 (protection of those conducting directed post mortems); ss 95-99 (objections by the senior next of
kin, and the 48-hour Supreme Court route); ss 100-101 (disposal of remains); the maximum penalties of ss 35(2), 44, 53(5),
62, 74(3), 75(7), 76, 100(1), (2) and 103A.

**Out, and why:**

- s 1, s 2, s 3 (name, commencement, objects), Chapter 2 (ss 7-16: coronial officers), ss 17, 20 (signposts), s 104,
  s 109, Schedule 1 and Schedule 3: machinery.
- Part 3.3 (ss 30-32: inquiries into fires and explosions): no death; the person affected is a property owner, a
  different seat.
- ss 33, 34, 36, 37 (referral between coroners; notices to the Registrar, the Ombudsman, the NDIS Commissioner and the
  Minister): duties between officials, giving the family nothing to ask.
- Chapter 5 (ss 39-45: coronial investigation scenes): police powers; only the s 44 penalty is encoded.
- ss 46-53, 55, 58, 59, 62-72 (procedure, juries, case management, directions, practice notes, production, subpoenas and
  warrants): the conduct of the inquest, addressed to the coroner and witnesses; only the ss 53 and 62 penalties are
  encoded. s 58(2) (a witness's privilege) and s 61(1)-(6), (8)-(10) (the certificate procedure) are the witness's seat;
  only s 61(7), which reaches the family's later claim, is encoded.
- ss 73, 74, 76, 77 (publication): orders against the media and the public; the penalties are encoded.
- ss 78, 80, 82 (suspension over an indictable offence, a finding that the person did not die, recommendations): what
  the coroner does; their effect on the family is encoded through ss 79, 81 and 83. s 82 gives the family no right (the
  record goes to officials and the bodies a recommendation is directed to).
- ss 88, 88A, 89(1)-(5), (7)-(9), 90(1)-(3), (7), 92, 93 (dignity, preliminary examinations, directions, reports, tissue,
  Coronial Medical Officers, fees): what investigators do; the family's points of entry (ss 89(6), 90(4)-(6), 94, 95-99)
  are encoded.
- Chapter 9A (ss 101A-101P: the Domestic Violence Death Review Team): a review body, no claim machinery.
- ss 102, 102A, 103, 105-107 (assistance, databases, contempt, service, procedure for offences, corporations): machinery.
- Schedule 2 (savings and transitional): deaths before the 2010 repeal of the 1980 Act, and deaths of the repealed
  s 6(1)(d) kind before its repeal (cl 26), are not covered. The text of repealed s 6(1)(d) is not in the deposit.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 6(1), 18, 23, 24(1) -- `Is it a reportable death`, `Which coroner can hold an inquest`, `Must an inquest be
  held` -- each list is asked as one choice ("pick the first that fits"); several limbs may hold at once and any one
  suffices, so the first is enough for every answer except s 27(1)(b), where a s 23 circumstance should be picked before
  a s 24 one -- one yes/no input per limb (more questions, no loss).
- **F2** s 6A(1)(c), (e) "did not have a spouse or child ... or a spouse or child is not available" -- `Am I the senior
  next of kin` -- a child (or brother or sister) under 18 bars the next tier only if "available", which the Act does not
  define; the answer is `NOTHING` where it turns on it -- a minor is never "available" (the parent or executor is senior
  next of kin), or always is (they are not).
- **F3** s 19 "within the last 100 years" -- `Which coroner can hold an inquest` -- a death on the same calendar day 100
  years before today is within -- it is outside (the period ends the day before).
- **F4** s 35(1) "This section applies to any person who ..." -- `Must I report the death` -- a person outside s 35(1),
  or a death already reported, answers `JUST FALSE` ("this section puts no duty on you") -- `NOTHING`, as a scope limit
  with no "only".
- **F5** s 81(1)(c) "in the case of an inquest that is being concluded" -- `Will the findings state the manner and cause
  of death` -- on a suspension, `JUST FALSE` (read as a "where" condition) -- `NOTHING`, as a scope limit.
- **F6** s 83(4) "must be held if" -- `Must a fresh inquest be held on my application` -- when the State Coroner is not
  of the opinion required, `JUST FALSE` (s 83(4) requires nothing; the coroner's other powers, s 83(2), (3), (8), remain)
  -- `NOTHING`, because a fresh inquest may still be held under those powers.
- **F7** s 97(1) "within 48 hours after the notice was given" -- `Is my Supreme Court application in time`, `Can the post
  mortem go ahead now` -- an application at exactly 48 hours is in time (the stable `l4` counts `WITHIN 48` inclusively)
  -- the 48th hour is outside.
- **F8** ss 96(1)-(3) -- `Can the post mortem go ahead now` -- after a senior next of kin's written objection and before
  the coroner decides and gives notice, "not yet" (s 96(3) presupposes the decision comes first) -- the Act does not
  forbid a post mortem already directed, so `NOTHING`.
- **F9** s 100(2) "remove human remains (other than cremated remains) from the State" -- `May I bury, cremate or remove
  the remains` -- taking cremated remains out of NSW answers `NOTHING` (a limit in the prohibition's own words) -- `JUST
  TRUE`, since nothing in the Act forbids it.
- **F10** s 75(3) "the following persons are relatives" -- `Can a non-publication order protect me` -- the list is not
  closed ("only" is absent), so a person outside it answers `NOTHING` -- a definition, closed, `JUST FALSE`.
- **F11** s 57(1) "may grant leave to any person, who in the opinion of the coroner has a sufficient interest" -- `Will I
  be given leave to appear` -- a non-relative without a sufficient interest gets "the Act gives me no leave on these
  facts" (a "not covered" answer) -- a firm no.
- **F12** s 96(5) with ss 96(3), (4), 97 -- `How can I object to the post mortem` -- a senior next of kin the coroner may
  refuse is told the objection "may" be refused, and the 48-hour route is not encoded as lost -- a refusal under s 96(5)
  ends the s 96(3) notice and the Supreme Court route for that person.

## What the Act turns out to say

1. **Who is senior next of kin depends on minors it does not rank.** s 6A(1)(b) and (d) make only adult children and
   adult brothers and sisters senior next of kin, but (c) and (e) are reached only if the deceased "did not have" a child
   (or brother or sister) "or [one] is not available" -- with no age limit. A parent of a person survived only by a young
   child is senior next of kin only if that child is "not available", which the Act never defines. Fork F2; asserted
   (`NOTHING`).
2. **s 6A(1)(c) says "either of the deceased person's parents", (d) and (e) "living parent".** Both parents are senior
   next of kin together; a dead parent bars (d) and (e) only through "not available". Encoded on the facts as "a parent is
   living and available".
3. **"next of kin" in s 54(1)(c) is not defined.** The Act defines "relative" (s 5) and "senior next of kin" (s 6A), but
   the duty to tell the family when and where the inquest will be held is owed to "the person's next of kin", a third
   term. It is asked as a fact.
4. **Three families.** s 5 "relative" (adults only; brothers and sisters only if there is no spouse, parent, guardian,
   child or person in loco parentis), s 6A "senior next of kin" (ranked) and s 75(3) "relatives" (no age limit, brothers
   and sisters alongside everyone else, and anyone living with the person as their spouse) each pick a different set of
   people; s 24(2) adds a fourth, "such family members as would be reasonably expected to have an immediate interest".
   Asserted: a brother is a s 75(3) relative even where he is not a s 5 relative.
5. **s 25(2) adds nothing to the power to dispense with an inquest.** s 25(1) already lets the coroner dispense whenever
   an inquest is not required; s 25(2) ("without limiting subsection (1)") names the family's wish as a ground but needs
   none of it. The family's wish matters only in the consultation it requires. s 89(6) does the same for the post mortem, which
   s 89(1) already leaves to the coroner's discretion. Encoded through `Must an inquest be held` (dispensing whenever no
   inquest is required) and `Can the coroner dispense with the post mortem at my family's wish` (`NOTHING` off the s 89(6)
   facts).
6. **The 48 hours run twice, from the same moment.** The post mortem may not be conducted until at least 48 hours after
   the s 96(3) notice (s 96(4)(a)), and the senior next of kin has 48 hours after the same notice to apply to the Supreme
   Court (s 97(1)); the application, not the objection, is what stays the direction (s 97(2)). An application made at the
   48th hour arrives at the earliest moment the post mortem may begin. For organ retention the notice gives no minimum
   time (s 96(4)(a) is about post mortems only), but the 48 hours to apply still run. Asserted at 47, 48 and 48.5 hours.
7. **s 100(1) and (2) set different tests.** Burying or cremating needs the person to "have been given, or [have] in his
   or her possession" the authorisation; handing remains over for research or taking them out of NSW needs only that one
   "has been issued". Asserted: a coroner's order not yet in the family's hands allows removal from NSW but not burial.
8. **A Registrar's certificate does not authorise disposing of a stillborn child.** s 100(3)(b) lists only the doctor's
   s 12(3) certificate or notice and a coroner's order. Asserted.
9. **Certified evidence cannot be used against the witness in the family's claim.** s 61(7) bars the use of evidence
   given under a s 61 certificate, and anything obtained in consequence, against the witness "in any proceeding in a NSW
   court" -- including a civil claim the family later brings against, say, the employer or the driver whose evidence was
   certified. Only a prosecution for the falsity of the evidence is excepted. Asserted.
10. **Findings cannot say who is to blame in criminal terms.** ss 81(3) and 82(3): the record "must not indicate or in any
    way suggest that an offence has been committed by any person". A family seeking a finding of fault for a later claim
    will not get one framed as an offence. Stated in the `@export` of `Will the findings state the manner and cause of
    death`.
11. **s 38(2)(b) cites a repealed paragraph.** It refers to "paragraphs (b)-(f) of the definition of reportable death in
    section 6(1)"; s 6(1)(d) is repealed and s 6 is not written as a "definition" (it says when a death "is" reportable).
    The encoding reads it as "reportable only under s 6(1)(a)".
12. **Penalties differ in "or" and "or both".** ss 74(3), 75(7) and 76 give "10 penalty units or imprisonment for 6
    months" (an individual), without "or both"; s 44 and s 103A say "or both". Encoded in the `fine and imprisonment both`
    field. s 79(4)(c) and (5) name "the Attorney General, and Minister for the Prevention of Domestic Violence", a
    ministerial title carried into the text by an administrative change; it is read as the Attorney General.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags and follows these rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
> The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
> Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

> - **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means"/"is" definitions (ss 5, 6, 6A, 100(3)), "if", "unless" and "only" conditions (ss 18, 19,
21, 26, 27, 38(2), 65(2), 83(4), (5), 84, 91(2), (3), 100) and periods the text fixes (ss 19, 24(1)(b), 79(2A), 79(3), (5),
97(1)) answer no when they fail; flat negatives (s 38(1), (3), s 61(7) "cannot", s 65(6), s 75(5), s 94 "does not",
s 100) answer no; scope limits with no "only" and lists left open (ss 38, 54(1)(d), 56, 60, 61(7), 75(3), 75(5), 89(6),
90(4), 94, 100(2)) answer `NOTHING` or a "not covered" constructor; the sites with no convention (a duty whose "if" is
unmet, "(other than X)", a grant limited in its own words) each have a fork line above (F4, F5, F6, F9, F11).

## Questions (exported)

`cor-coroners.l4` (31), in the Act's order: `Am I a relative` (s 5), `Am I the senior next of kin` (s 6A), `Is it a
reportable death` (s 6), `Which coroner can hold an inquest` (ss 18, 19, 21-24), `Must an inquest be held` (ss 25, 27-29,
87), `Must the coroner give me reasons for dispensing` (s 26), `Must I report the death` (s 35), `May the doctor certify
the cause of death` (s 38), `Must the coroner tell me when and where the inquest is` (s 54), `Does the coroner's right to
the body come first` (s 56), `Will I be given leave to appear` (s 57), `Must the coroner give me reasons for refusing my
witness` (s 60), `Can certified evidence be used against the witness` (s 61(7)), `Can I get a copy of the coroner's file`
(s 65), `Can a non-publication order protect me` (s 75(2), (3)), `May a report of the inquest be published` (s 75(5)),
`Can the suspended inquest be resumed` (s 79), `The earliest day the inquest may be ordered resumed` (s 79(2A)), `Will the
findings state the manner and cause of death` (s 81), `Can I apply for a fresh inquest` (s 83(5)), `Must a fresh inquest
be held on my application` (s 83(4)), `Can the Supreme Court order an inquest on my application` (ss 84-87), `Can the
coroner dispense with the post mortem at my family's wish` (s 89(6)), `Can the coroner keep a whole organ after the body
is released` (s 90), `Can the coroner order the body exhumed` (s 91), `Can I claim against the post mortem doctor` (s 94),
`How can I object to the post mortem` (ss 96, 98, 99), `Is my Supreme Court application in time` (s 97, with the
regulative rule), `Can the post mortem go ahead now` (ss 96, 97, with the regulative rule), `May I bury, cremate or remove
the remains` (s 100), `What is the maximum penalty` (penalty lines).

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 35(2) | any person with the grounds | duty | `Must I report the death` |
| s 38(1), (3) | the doctor | prohibition (the relative holds a power to trigger it) | `May the doctor certify the cause of death` |
| s 57(3) | the coroner | duty to the relative | `Will I be given leave to appear` |
| s 96(1) | the senior next of kin | power (request) | `How can I object to the post mortem` |
| s 97(1) | the senior next of kin | power with a time limit | regulative rule (`MUST ... WITHIN 48 ... LEST BREACH`, modelling the lapse) |
| s 94 | the post mortem doctor | immunity (the family's disability) | `Can I claim against the post mortem doctor` |
| s 100(1), (2) | anyone | prohibition | `May I bury, cremate or remove the remains` |

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Coroners Regulation and replace the inputs it settles (excluded procedures, prescribed assistance,
  specialist disability accommodation, fees, authorised disposals).
- Have a lawyer review the forks, especially F2 (minors and "available"), F8 and F12 (the post mortem before the
  coroner's decision, and after a s 96(5) refusal).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
