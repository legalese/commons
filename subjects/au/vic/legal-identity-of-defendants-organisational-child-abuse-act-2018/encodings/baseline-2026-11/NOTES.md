# Legal Identity of Defendants (Organisational Child Abuse) Act 2018 (Vic): baseline encoding for the survivor

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05.
It is the first encoding of this Act; nothing beside it was changed.
There is no REFUSE in it. A question the text does not answer returns `NOTHING`, with a `NOTHING-kind` comment, and the cases assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Four modules:

- **`lid-dates.l4`**: the dates, with built-in date functions only (no daydate): the Act's plain 120 days, and the Supreme Court Rules' way of counting (rr 3.01, 3.04, 3.05(2), 3.08), restated with their rule numbers and lines.
- **`lid-core.l4`**, seat-neutral: every operative section of the Act (ss 3-13), each rule with its section and deposited line; one regulative rule (`DEONTIC`) for the steps of s 7(3) and Order 85 (the NGO's nomination, its service, the plaintiff's amended process, or the plaintiff's s 8 application); and narrow restatements of the law the Act is read with (Wrongs Act 1958 s 88(ba) with s 93; Limitation of Actions Act 1958 ss 27O, 27P, 27Q; Supreme Court (General Civil Procedure) Rules 2025 Order 85).
- **`lid-seat.l4`**, the survivor's seat: 18 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the order a claim meets them. It restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`lid-cases.l4`**: every exported question with its edges, and the regulative rule by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

## Edition

**Legal Identity of Defendants (Organisational Child Abuse) Act 2018**, Act No. 18/2018, **Version No. 002, as at 1 May 2020** (the current version when the register was read on 2026-11-07), deposited at `../../registers/source-bundle/legal-identity-of-defendants-organisational-child-abuse-act-2018.txt` (sha256 `8a6d9175af466a67e9eba136ed870f5feb38b3de52c651454dee834bf6b2800c`, the blob as committed).
The owner saved the Word file by hand on 2026-11-07; the `.meta.json` beside the text records the file, its hash and the conversion, and `subjects/au/vic/README.md` records the deposit. Line numbers in the modules are lines of that text.
The Act came into operation on 1 July 2018 (endnote, line 143). Version 002 differs from the original in that ss 16-20 (amendments of other Acts) were repealed on 1 May 2020.

**Read with**, each restated narrowly in `lid-core.l4` or `lid-dates.l4`, because IMPORT cannot reach another subject:

| Instrument | Deposited at | Version | Provisions restated |
|---|---|---|---|
| Wrongs Act 1958 | `subjects/au/vic/wrongs-act-1958/registers/source-bundle/` (sha256 `cc5d5a7a30d972f6c30302100ce0d7b154dfd9fedde9336c678a37e262293083`) | No. 130, as at 25 February 2026 | s 88 "relevant organisation" para (ba) (lines 2238-2241), s 93 (line 2302) |
| Limitation of Actions Act 1958 | `subjects/au/vic/limitation-of-actions-act-1958/registers/source-bundle/` (sha256 `84e874841a2b4d3ad2348a1304bd7b36be7b23607bfb485db8d2ab886eb689bd`) | No. 113, 2 October 2026 | ss 27O(1), 27P(1), 27Q(1) (lines 683-721) |
| Supreme Court (General Civil Procedure) Rules 2025 | `subjects/au/vic/supreme-court-general-civil-procedure-rules-2025/registers/source-bundle/` (sha256 `5a7e31c55401557d05bbfb38d5a447cd585187b0d771b6b27dc5d2e692f549ed`) | No. 003, 1 January 2026 | rr 3.01, 3.04, 3.05(2), 3.08 (lines 162-198), Order 85 (lines 7895-7916) |

The Act prints no amounts, and no regulations are made under it (s 15): no other instrument sets its numbers.

## Checks

| Module | Assertions |
|---|---|
| `lid-dates.l4` | none (0 errors, 0 warnings) |
| `lid-core.l4` | none (0 errors, 0 warnings) |
| `lid-seat.l4` | none (0 errors, 0 warnings) |
| `lid-cases.l4` | 90 written, 90 satisfied (0 errors, 0 warnings) |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-07). A copy of the case file with two expected values changed was run first, to confirm that failures are reported (they were); it was not kept.
Every expected value was worked by hand from the deposited texts, with the count or reason in the comment above the assertion. The edges asserted include: ages 17 and 18; lawful force, and psychological abuse alone; each of the seven heads of control alone, none, and all without use; each s 4(2) condition failing; day 120 and day 121 (30 June and 1 July 2026 from 2 March 2026); a nomination on day 120 and on day 121; 120 days across the Christmas vacation; the Rules' 7 and 28 days across 24 December to 9 January, landing on a Saturday and on a Sunday; service before and after 4 pm and on a Saturday; the last day for the amended process and the day after, in a trace; a judgment below, equal to and $1 above the value of the trust property; abuse on 30 June and 1 July 2017.
Breached traces are asserted through a helper (`ends fulfilled`) and `NOT`, because `EVALTRACE ... EQUALS` cannot test a breach.

## Seat

**The survivor** (`lid-seat.l4`): a person who was abused as a child, now looking for an organisational defendant to sue, where the organisation is an unincorporated association (a church, club or other body with no legal personality of its own) that uses a trust to conduct its activities. In the Act's words, the plaintiff. *Is what happened to me child abuse under the Act? Is the organisation an NGO; is this trust an associated trust; does the Act apply to the organisation? Whom do I sue; can I sue the organisation in its own name; by when can it nominate a proper defendant; can I apply for my claim to proceed against the trustees; must the organisation identify its trusts; must it still meet its obligations in the proceeding? By when must it serve its nomination on me; by when must I file my amended originating process? What is the most I can recover from the trustees; may they pay from the trust property whatever the deed says; can the proper defendant rely on a defence; does the organisation's insurance cover the proper defendant? Is the organisation a relevant organisation under the Wrongs Act; can I bring my action at any time?*

The NGO, its nominee, the trustees, the insurer and the court get no seat: their powers appear only as what they mean for the survivor (whom to sue, by when, what can be recovered), and the court's judgments as conditional inputs. An NGO or trustee seat (what the NGO may nominate and must serve; what trustees may pay and are protected for) would draw on the same core.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Followed. No instrument sets a number for this Act. The Act is read with Wrongs Act Part XIII, Limitation Act Part IIA Division 5 and Order 85 of the Rules; each is restated narrowly, with its section and line, in its own `§§` of the core, and the questions on them say which law they come from. The Wrongs Act's own encoding (`subjects/au/vic/wrongs-act-1958/encodings/baseline-2026-11/`) has the rest of Part XIII.
- **The actors the text names.** Followed: the plaintiff, the NGO, its management members, the nominee (proper defendant), the trustees of the associated trust, the court; from the Rules, the Prothonotary.
- **A judgment handed to someone else answered conditionally.** Followed: whether the NGO would be capable of being sued and found liable but for being unincorporated (s 4(2)(b)), whether the nominee lacks sufficient assets (s 8(1)(b)), whether a defence would have been available to the incorporated NGO (s 10), and the court's orders under ss 7(3), 8(4) and r 85.03 are inputs. The court's discretion to make a s 8(4) order is not decided: the question is whether the survivor may apply.
- **Definitions worked out, borrowed terms asked.** The Act's own definitions in L4: child abuse (s 3), NGO (s 5), control (s 6), associated trust (s 3), the application of the Act (s 4(2)). Asked as facts: "non-government organisation" and "unincorporated association or body" (undefined), "minor" (as an age; see Readings), the trust's powers, "capable of being sued".
- **One case.** One claim by one survivor against one NGO, with one associated trust where a trust matters. Several trusts (s 8(6), (7)) are not summed: the s 9(2) question is asked once for each trust.
- **The Act's own terms with a plain gloss.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed: s 1 (purpose), s 2 (commencement), s 14 (Corporations Act displacement) and s 15 (regulations) are out.

**One departure in form.** The s 4(2) facts (the abuse, the NGO, liability but for being unincorporated, an associated trust) are asked in full by the s 4(2) question and its three helper questions; the later questions take its answer as one input ("Does the Act apply to the organisation (the s 4(2) question)?") rather than asking a dozen facts again. A form can chain them.

**Readings.**

- *Counting the Act's 120 days.* "Within 120 days after the commencement" (s 7(3)) and "within 120 days from the commencement" (s 8(1)(a)) both end on the 120th day after the day of commencement, that day excluded (the Interpretation of Legislation Act 1984 s 44, not deposited). No weekend or holiday roll is applied to the Act's own period.
- *Counting the Rules' 7 and 28 days.* Under r 3.01(2), (3) the day of the event is excluded and the last day included; r 3.04(1) excludes 24 December to 9 January; r 3.05(2) moves service after 4 pm or on a closed day to the next open day; r 3.01(5) moves a last day on a closed day to the next open day. r 3.08 closes the office on Saturdays, Sundays and public holidays. **Public holidays are not deposited and are not applied**, so a last day that falls on a public holiday comes out one day early. The service deadline itself (r 85.02(2)) is read on the actual day of service.
- *Minor.* Under 18 (Age of Majority Act 1977 s 3, not deposited).
- *Limitation Act "physical abuse".* Undefined there; a lawful exercise of force, which this Act's s 3 excludes, is answered `NOTHING` under s 27O.
- *The trace's clock.* Days by `DATE_SERIAL`; each event carries its date, and the event's time must be that date's serial. The rule counts the NGO's 120 days as plain days and does not take a court order under s 7(3).

## Scope

**In:** ss 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13: every operative section. With them: Wrongs Act s 88(ba), s 93; Limitation of Actions Act ss 27O(1), 27P(1), 27Q(1) (as the "no" of s 27P); Rules rr 3.01, 3.04, 3.05(2), 3.08, 85.02, 85.03, 85.04.

**Out, and why:**

- **Machinery:** s 1 (purpose; its words are in the seat's header), s 2 (commencement; the Act has been in operation since 1 July 2018), s 14 (Corporations legislation displacement, between the Act and the Corporations Act, not a fact the survivor states), s 15 (regulations; none made), ss 16-20 (repealed amending provisions).
- **Within the Act, as notes rather than questions:** s 3 "management member" (used only through s 5(3) and s 6(g), asked as a fact); s 5(2), (3) (no attribute is needed; any management member may exercise the NGO's powers, so a nomination by one is the NGO's); s 7(1)(b), s 8(5)(b) (the liability the proper defendant incurs, folded into "whom do I sue"); ss 7(4), 8(8) (the court determines the claim as if the NGO were incorporated; noted); s 8(6), (7) (more than one trustee or trust; one trust is asked at a time); s 12(2) (the NGO keeps its cover; in the `@export` text).
- **Read-with provisions not restated:** the rest of Wrongs Act Part XIII (ss 89-92: the duty, the reverse onus, the Wrongs Act s 92 nomination) and Part XIIIA, which the Wrongs Act's own encoding has; Limitation Act s 27F (discoverability) and the s 27Q date, ss 27OA, 27QA-27T (setting aside earlier judgments and settlements); r 85.01 (definitions), Form 85A and the address for service (r 85.02(1)), the sealing and service of the amended process (r 85.03(b)).

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects". The rulings it applies, copied word for word:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

In this row:

- **Plain BOOLEAN** where the text's own words give both answers: s 3 child abuse and associated trust ("means"); s 5 and s 6 ("has the meaning given in section ...", handing the term to the section; for s 6, the delegated-definitions ruling, (a)); s 4(2) ("applies to an NGO if"); s 8(1) ("This section applies to a claim if").
- **`JUST FALSE`:** s 13 once a proper defendant is in place ("Pending ...", a period the text fixes, periods ruling (a)) and where s 4(2) fails; Wrongs Act s 88(ba) where its conditions fail ("means"); Limitation Act s 27P for a Wrongs Act Part III action ("that is not an action that arises under Part III").
- **`NOTHING`**, each with its `NOTHING-kind` comment: whom to sue where the Act does not apply (s 4(2); the ordinary law decides); s 8(3) outside an application under s 8(2); ss 7(5), 8(9) with no proper defendant; ss 9(1), 11 outside a liability incurred as proper defendant; s 10 for a defence the incorporated NGO would not have had (a grant limited in its own wording); s 12 with no NGO policy; Wrongs Act s 88(ba) for abuse before 1 July 2017 (s 93); Limitation Act ss 27O, 27P outside Division 5.

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. s 8(1)(a), `s 8(1) -- section 8 applies to the claim`: the NGO "fails to nominate ... within 120 days" on the flat 120 days of (a), even where the court has extended the s 7(3) time; a nomination on day 121 is a failure. Other reading: (a) runs to the end of any time the court allowed under s 7(3).
2. s 7(1), s 8(1)(b), `ss 7, 8, 13 -- the defendant to sue`: a "nomination" of an entity that cannot be sued is no nomination under s 7(1), so the NGO stays the defendant in its own name (s 13) until a s 8 order; and after a s 8(4) order the answer is the trustees, without saying whether a nominee who lacked assets stays a defendant beside them. Other readings: the nominee is the defendant until an order; the nominee stays beside the trustees.
3. s 13(b), `s 13 -- the proceeding may be commenced or continue against the NGO in its own name`: read within s 4(2), so the Act gives no right to sue an NGO in its own name on a claim not founded on child abuse (`JUST FALSE`). Other reading: (b) is not limited to child abuse claims (it drops (a)'s words).
4. Wrongs Act s 88(ba), `Wrongs Act s 88(ba), s 93 -- the NGO is a relevant organisation`: "capable of being sued in accordance with that Act" is read as "this Act applies to the NGO" (s 4(2)), because s 13 then lets it be sued in its own name. Other reading: only once a proper defendant is nominated or appointed.

## What the Act turns out to say

1. **s 9(2) speaks of a proper defendant "under this section".** No one is a proper defendant under s 9; proper defendants are made under ss 7 and 8 (s 10 says "under section 7 or 8"; s 9(1) says "under this Act"). Read as "under this Act", so the cap reaches trustees nominated under s 7 as well as those appointed under s 8. Asserted (the cap at, below and above the trust's value).
2. **s 9 is not confined to trustees appointed under s 8.** An NGO may nominate the trustee of its associated trust under s 7; s 9(1) then lets that trustee pay from the trust property "despite any ... trust deed", and s 11 protects it. The question asks only whether the trustees are a proper defendant.
3. **The two 120-day clocks can part.** s 7(3) lets the court order a different time for the nomination; s 8(1)(a) keeps a flat 120 days. Fork line 1. Asserted (a nomination on day 120 does not open s 8; one on day 121 does).
4. **s 8(1)(b) contemplates a nominee "not capable of being sued"**, though s 7(1) lets an NGO nominate only "an entity that is capable of being sued". Fork line 2. Asserted.
5. **s 13(b) drops the words "founded on or arising from child abuse"** that (a) has. Fork line 3. Asserted (the Act not applying: no).
6. **The Act's 120 days do not stop for Christmas; the Rules' 7 and 28 days do.** A proceeding commenced on 1 December 2025 leaves the NGO until 31 March 2026, while a nomination served on 24 December 2026 leaves the plaintiff until 8 February 2027 (28 days counted from 10 January, ending on a Saturday). Asserted.
7. **"The value of the trust property" (s 9(2)) is not fixed at a time:** at the abuse, the judgment or the enforcement. It is an input.
8. **The Act reaches abuse at any time (s 4(3)); the Wrongs Act duty does not.** Through s 88(ba) an NGO may be a relevant organisation owing the Part XIII duty, but only for abuse on or after 1 July 2017 (s 93); for earlier abuse the survivor sues on the common law duty, through the same proper defendant. Asserted (30 June and 1 July 2017).
9. **Three definitions of the same abuse differ.** This Act's "child abuse" includes psychological abuse arising from physical or sexual abuse and "alleged" abuse, and excludes lawful force; Wrongs Act s 88 "abuse" has the same lawful-force exclusion but no psychological limb; Limitation Act s 27O has the psychological limb but no lawful-force exclusion. Asserted where encoded (lawful force: not child abuse here; outside s 27O as read).
10. **No limitation defence for the proper defendant to borrow.** s 10 lets a proper defendant rely on any defence the incorporated NGO would have had; for personal injury from child abuse the Limitation Act s 27P leaves no limitation period, so there is none to rely on (a Wrongs Act Part III death claim keeps a 3-year period, s 27Q). Asserted.
11. **s 6(g) reaches any member.** A power of a kind in (a)-(f) held under the trust deed by "a member of the NGO", not only a management member, makes the trust controlled. Asserted.

## Before relying on it

- An independent test pass, and a lawyer's review of the fork lines and findings.
- Public holidays for the Rules' counting (r 3.08(b)), if deposited.
- An NGO or trustee seat, drawing on the same core.
- The rest of Limitation Act Division 5 (setting aside earlier judgments and settlements, ss 27QA-27QF), which matters to survivors who settled or lost a claim before the dates those sections name.
- Several associated trusts (s 8(6), (7)) in one question.
