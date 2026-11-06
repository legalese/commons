# NOTES -- Terrorism Act 2000, Part III (Terrorist Property), United Kingdom -- legalese-sonnet-5.5

**Status: draft.**
Written on 2026-11-05 by a single Sonnet 5.5 agent working alone from `BRIEF.md`, with no ontology agent, integrator, independent test author or subagent.
**Not reviewed:** no domain expert has read this encoding against the text, and nobody has run it past a lawyer.
Target compiler: **main**.
Written with `l4` 1.6.109 (main, 4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb` (checked with `shasum -a 256` on 2026-11-05); `check.sh` compared it with `l4` 1.6.108 (main, 2ae7c9b, 2026-11-02).
The source is `ukpga-2000-11-part-3.txt`, a plain-text rendering made by a converter script from the legislation.gov.uk data for Part III, version of 2026-07-08 (a point-in-time revised text), retrieved 2026-11-05.
**It is a converter rendering, not the official text, and nothing here has been verified against the official text.**
The converter's own caveat is that the revised text "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish".
The licence note is in `SOURCE-LICENSE.md`, which points at the subject-level `STUB-SOURCE-LICENSE.md` written when the text was deposited.

The encoding has two layers.
Layer 1 is the law: ten modules in the Act's order (`ta-nouns`, `ta-logic`, `ta-interpretation`, `ta-offences`, `ta-disclosure`, `ta-regulated-sector`, `ta-voluntary-disclosure`, `ta-tipping-off`, `ta-information-orders`, `ta-forfeiture`; `ta-logic` holds only the connectives that carry `NOTHING` through) and one test file per module (`ta-tests-*.l4`).
Layer 2 is the seat: `ta-seat.l4` (55 questions) and `ta-cases-seat.l4` (181 worked cases).
Every rule carries `@ref` to the lines it implements, written by script from the source file; `python3 -I srcrefs.py check --refs ukpga-2000-11-part-3.txt ta-*.l4` reports 0 problems.

## Seat

The seat is: **a person who handles, funds or deals in money or other property that may be terrorist property, asking on facts they can state whether they commit an offence under Part III or have a defence, and what they must disclose to whom and when.**

Why this seat.
Part III speaks to that person almost throughout.
Sections 15 to 18 and 22 say what they must not do and what it can cost them.
Sections 19 to 21ZC and 21A to 21C say what they must tell, may tell, and when telling protects them.
Sections 21CA to 21CF say when they may pass information to another business.
Sections 21D to 21H say what they must not tell others.
Sections 22B to 22F say what they can be ordered to hand over.
Sections 23 to 23B say what they can lose on conviction.
Provisions addressed to an official (the constable who must pass a disclosure on to the National Crime Agency, s 21C; the court that hears a forfeiture, s 23B) are in layer 1 for what they decide, and reach layer 2 only for what they mean to this person, for instance whether the court must hear them before forfeiting property they claim (s 23B(1)).
There is no seat for an official.

Shape.
`ta-seat.l4` has 55 questions in eight groups under `§§` headings, in the Act's order: s 14 (2 questions); ss 15 to 18 and 22 (10); ss 19 to 21ZC (15, including the notice-period date); ss 21A to 21C (4); ss 21CA to 21CF (6); ss 21D to 21G (8); ss 22B to 22F (8); ss 23 to 23B (2).
Every question has `@export`, every input has `@desc` worded as the person would be asked, and every question is a thin wrapper that builds the layer-1 records from plain inputs and calls one layer-1 rule.
The seat restates no rule, and no layer-1 module was changed to suit it.
(One thing moved the other way: two enumerations that I had first put in `ta-nouns.l4` in anticipation of the seat, and that no layer-1 rule uses, were taken out of layer 1; the seat's own answer type is now declared in `ta-seat.l4`.)
Each answer is `MAYBE BOOLEAN` (or a date, a number, a court, or the one answer type described below), so every question can say "yes", "no" or "the Act does not answer on these facts".
The inputs are plain `BOOLEAN`s, `DATE`s and `NUMBER`s, except one: in "What must I tell the police, and to whom, and when" the fact that the information came in the course of a business in the regulated sector is asked as Yes, No or "I am not sure", because Schedule 3A decides it and Schedule 3A is not among the sources; "I am not sure" becomes `NOTHING` and the question answers "the Act does not answer on these facts".

How the seat applies E1 (see F5).
Each question answers one section on its own (option C).
The seat does **not** combine an offence with the protections and defences that may answer it, so "do I commit an offence" and "am I protected" are separate questions and the person asks both.
Three questions gather by hand (option B as guidance): "Do I commit an offence by not disclosing in the regulated sector (s 21A)?" (which calls a layer-1 function that brings s 21A(1) and (5) together), "What must I tell the police, and to whom, and when" (ss 19(1), 19(5), 21A(2), (3) and (5)), and "Could the court order this property forfeited after my conviction" (ss 23(2) to (7)).

Not asked in the seat, with the reason.
Conditions 2 to 4 of s 22B (an external request from a foreign authority or foreign FIU, and the National Crime Agency's own analysis purposes) are encoded in layer 1 but not asked: they turn on facts the respondent usually cannot state.
Section 23A (forfeiture after other terrorism offences and offences with a terrorist connection) is encoded in layer 1 and not asked, because the person in this seat is asking about the Part III offences.
Provisions that address the constable, the applicant or the court (for example s 21C, s 22B(1) and (2), s 22B(12), s 23B(2) and (3)) are in layer 1 only.

### Reading a result: FALSE and NOTHING

This is the rule of 2026-10-29 as the brief states it (assumed, not ruled by a lawyer), put in this Act's terms.
**A "no" is `JUST FALSE`.**
It is given only where Part III says no in its own words: a definition that says "means" (for example s 21CF(10), "Terrorist financing offence" means an offence under any of sections 15 to 18); a condition the text introduces with "if", "where", "applies where", "applies only where", "only so far as" or "does not apply if" (for example s 19(1), s 19(4), s 21(1), s 21(3), s 21CA(1), s 21CD(2), s 21ZB(2), s 22B(1), s 23(2)); a period the text fixes in its own words, outside the period (s 21ZA(2), s 21CC(4)(d)); or a flat negative ("does not", "may not", "must not", "shall not": for example s 19(5), s 22E(1), s 23B(3)); or a defence the text asks the person to "prove", when the person has not proved it (ss 18(2), 19(3), 19(4), 21(5), 21ZC), where `JUST FALSE` says only that this section gives no defence on these facts and never that there is no defence at all, because another provision may still give one.
"When", "upon" and "whenever" are read as "where", and a definition the text hands to a closed list answers `JUST FALSE` for a case in none of its heads (F23).
The period, "where", scope-limit, defence and delegated-definition rules follow Meng's two rulings of 2026-11-05, in the fork register below.
So "no, you do not commit the offence in s 19(2)" means the text itself gives the answer no on those facts.
**"Not covered" is `NOTHING`** (or, in the one gathered answer, the constructor `the Act does not answer on these facts`).
It is given where Part III lists without closing the list, says "includes" (for the two items s 14(2) extends), leaves a term undefined, is silent, points outside the sources (Schedule 3A, the statutory maximum, level 5, the Banking and Financial Dealings Act 1971, the 2002 Directive on groups), or limits a grant, a defence or a protection by its own wording and the case falls outside the limit (for example the offences a defence names, such as the inviter under s 15(1), whom s 21(5) does not name, or a person not charged under the section a defence is for (F18); the permission in s 20(1); the "which" clauses that limit the property in s 23(2) to (7); a scope limit with no "only", such as s 19(5), s 22C(1) or s 22E(1), which says nothing about what is outside it).
So "the Act does not answer" is not "no": a person told `NOTHING` has not been told they are safe.
A caller never turns `NOTHING` into `FALSE`; the connectives in `ta-logic.l4` (`the conjunction ... and also ...`, `the disjunction ... or else ...`, `the negation of`) carry it through.
Every branch that says no carries `-- FALSE-kind (the text says no in its own words): "<quote>"` and every branch that says "not covered" carries `-- NOTHING-kind (<why>)`; the quoted words are generated from the source file and appear in the table under "Marginal readings for a lawyer".
Penalties are always ceilings (`Penalty ceiling`), never amounts: the text says "not exceeding".
The one exception that looks like an amount is the £5,000 in s 22B(8), which is the text's own ceiling and is overridden by an input where regulations under s 22B(10) have substituted another sum.

## What is encoded and what is not

Everything in the deposited text has a row in the coverage table below, with exactly one disposition.
The generated counts are in the table's header line; the reasons for the inert rows are in the table (reason 1: headings; reason 2: machinery, the rule-making, order-making and regulation-making powers and the code-of-practice machinery of s 22F; reason 3: none, because the repealed sections are shown as `repealed or blank in this text`).
Nothing is `deferred` and nothing is `out-of-scope`.
Sections 24 to 31 are shown repealed in the text and have `repealed` rows only.
Not encoded because it is not in the sources: Schedule 3A (what a business in the regulated sector is), the Banking and Financial Dealings Act 1971 (bank holidays), the standard-scale amounts, Part I's definition of "terrorism" and Part II's "proscribed organisation", the Money Laundering Regulations 2017 (supervisory authority) and Schedule 4 (s 23B(4) points at it).
Each is a plain input.

## Fork register

Each entry has the readings, the one taken, and the text that licenses it.
The two rulings that bind this row come first, word for word as printed in `BRIEF.md`.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**F1. s 14(1) and (2): is "terrorist property" a closed list?**
Readings: (a) s 14(1) says "means", which closes the definition; s 14(2) begins "In subsection (1)" and extends only the two items it names ("proceeds of an act", read inside limbs (b) and (c), and "an organisation’s resources", read inside limb (a)), so property that fits none of the three limbs is not terrorist property (`JUST FALSE`); (b) s 14(2)(a) and (b) say "includes", so the list is open and the unmet case is not covered (`NOTHING`).
Taken: (a).
Rejected: (b), which was the reading first taken.
The reason: "includes" in s 14(2) widens the meaning of the two items inside the limbs and does not add a limb, and the limbs already consult it.
`s 14(2)(a)` and `s 14(2)(b)` themselves still answer `NOTHING` when no extension fact is given, because "includes" is not a closed list there; `s 14(1)` turns that into `JUST FALSE` only after reading all three limbs.
Licence: "In this Act “terrorist property” means—" (s 14(1)); "a reference to proceeds of an act includes a reference to any property which wholly or partly, and directly or indirectly, represents the proceeds of the act" (s 14(2)(a)); "the reference to an organisation’s resources includes a reference to any money or other property which is applied or made available" (s 14(2)(b)).
Marginal: yes.
Consequence: an arrangement over property that is not terrorist property misses the last element of s 18(1) and answers `JUST FALSE`.

**F2. s 19(2): what the offence is.**
Readings: (a) the person commits the offence unless both (a) the belief or suspicion and (b) the information are disclosed, and promptly; (b) the offence is committed only if neither is disclosed.
Taken: (a).
Licence: "The person commits an offence if he does not disclose to a constable as soon as is reasonably practicable— (a) his belief or suspicion, and (b) the information on which it is based."

**F3. s 21ZA(2) and (3): how the notice period is counted.**
Readings for the first day: (a) "starting with the first working day after the person makes the disclosure" means that first working day is day 1 of the 7; (b) it is day 0.
Taken: (a).
Readings for "before the end of the notice period": a notice of refusal that reaches the person on the last day of the period (a) counts, because that day is in the period; (b) arrives too late.
Taken: (a); and on the last day itself, or any day before it, the period has not ended, so the "if before the end of the notice period" is not yet met and the person is not "treated as having" consent (`JUST FALSE`, ruling of 2026-11-05 (a); the reading first taken was `NOTHING`).
Licence: "The notice period is the period of 7 working days starting with the first working day after the person makes the disclosure."; "A person is treated as having an authorised officer's consent if before the end of the notice period the person does not receive notice from an authorised officer that consent is refused."
Asserted by date: disclosure on Mon 2 Nov 2026 gives Wed 11 Nov 2026; disclosure on Mon 21 Dec 2026 with 25 Dec, 28 Dec and 1 Jan excluded gives Mon 4 Jan 2027.

**F4. s 21ZA(4): which days are not working days.**
The text excludes "a Saturday, a Sunday, Christmas Day, Good Friday or a day that is a bank holiday under the Banking and Financial Dealings Act 1971 (c.80) in the part of the United Kingdom in which the person is when making the disclosure".
Neither that Act nor the date of Easter is among the sources, so Good Friday and the bank holidays are one input list of dates, asked of the person; Saturdays, Sundays and Christmas Day are computed.
If the person's list omits a holiday, the answer follows the list (asserted in the seat cases: the same disclosure gives 1 Jan 2027 with a list that omits 1 January and 4 Jan 2027 with a list that has it).

**F5. E1: where this encoding gathers by hand (option B as guidance).**
Everything else answers one section on its own (option C).
The hand-gathering is in three layer-1 functions and three seat questions.
Layer 1: `s 21A(1) and (5) the person commits an offence under section 21A` (the offence with its own exceptions in the same section); `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances`; and `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` (takes the exceptions' answers as inputs).
Seat: "Do I commit an offence by not disclosing in the regulated sector (s 21A)?", "What must I tell the police, and to whom, and when (ss 19(2) and 21A(4))?", and "Could the court order this property forfeited after my conviction (ss 23(2) to (7))?".
The seat does not gather an offence with the protections that may answer it (ss 18(2), 19(3), 19(4), 21, 21ZA, 21ZB, 21ZC, 21E to 21G): the person asks the offence question and then each protection question.
Reason: gathering them would be the "much magic" Meng's note on E1 declines, and the combination depends on which protection the person invokes.
No language construct that gathers by name was looked for or proposed.

**F6. The mental element in ss 15 to 17.**
Sections 15(1)(b), 15(2)(b) and 16(2)(b) say "intends that it should be used, or has reasonable cause to suspect that it may be used", and ss 15(3)(b) and 17(b) say "knows or has reasonable cause to suspect that it will or may be used".
The record `Mind about use for terrorism` has one field for "reasonable cause to suspect that it will or may be used", used for both.
Reading (a): the two wordings differ only in how the suspicion is put; (b): "may" and "will or may" are different thresholds.
Taken: (a) in the record, with each rule reading only the fields its own section names, so the difference between "intends" (15(1), 15(2), 16(2)) and "knows" (15(3), 17) is kept.
Marginal: the merged field.

**F7. "sections 15 to 18" and "16 to 18" include section 17A.**
Section 17A lies between 17 and 18, so a range that runs through it takes it in: ss 21(5) ("any of sections 15(2) and (3) and 16 to 18"), 21CF(10), 22B(14), 23(1) and 23(7).
Reading (a): the range includes 17A; (b): the range means ss 15, 16, 17 and 18 only.
Taken: (a).
Rows: s 21(5), s 21CF(10), s 22B(14), s 23(1), s 23(7).

**F8. s 21CA(1)(b): "where applicable, condition 5 is also met".**
Condition 5 (s 21CA(6)) is that the person making the request has notified a constable that the request is to be made.
"Where applicable" is read as: in every case except the one s 21CA(7) names, "Condition 5 does not apply where the disclosure request concerned is made by a constable".
Other reading: it applies only where the text says it does.
Taken: the first.

**F9. s 21CC(4)(d): "before the end of the applicable period".**
Reading (a): a report sent on the last day of the period is sent before the period ends; (b): it must be sent on an earlier day.
Taken: (a).
Where a constable made the request but set no period, the Act points to a period it does not state and the answer is `NOTHING`.

**F10. s 21CC(8): varying the 28 days.**
"A constable may vary the period of 28 days (whether by lengthening or shortening it) by giving written notice to the person who made the required notification."
Taken: a variation by a written notice, given by a constable to that person, changes the period (`s 21CC(8) the notice varies the period of 28 days` answers `JUST TRUE`); without a notice the 28 days stand.
A notice of a different period given any other way (for example by telephone), by someone who is not a constable, or to someone else, is outside the grant and the Act says nothing of its effect, so that rule answers `NOTHING` and the seat answers "the Act does not answer" for the last day and for whether a report is in time (a scope limit with no "only": ruling of 2026-11-05 (c)).
Other reading: such a notice does not vary the period, so the 28 days stand (`JUST FALSE`).
The 28 days begin with the day of the notification, which is day 1 (s 21CC(7)(b), "beginning with the day on which the notification is made").
Asserted: notification on Mon 2 Nov 2026 gives Sun 29 Nov 2026; varied to 14 days, Sun 15 Nov 2026; an oral notice, no answer.

**F11. Flush-left closing words.**
The converter's plain text has no indentation, so closing words that follow a list ("that person, as well as the body corporate, is guilty of the offence ...", "it is a defence for him to prove that he disclosed the matters specified in that subsection in accordance with the procedure", "so far as the information is in the possession, or under the control, of the respondent") sit on their own lines.
For the coverage table each such line belongs to the row that is open when it is reached; the L4 rules read it as the closing words of the whole provision it follows (so s 19(4)'s defence and s 22B(3)'s "so far as" qualify the whole subsection).
Other reading: the words qualify only the last paragraph.
Taken: the whole provision.

**F12. s 22F (the code of practice) is inert, reason 2.**
Readings: (a) the duty to make, consult on, lay and bring into operation a code of practice, and the power to combine codes, are rule-making machinery; (b) a code the National Crime Agency must follow reaches a person served with an information order.
Taken: (a) for s 22F(1) to (6) and (9).
The part that reaches the respondent is the requirement that the applicant "has had regard to the code of practice under section 22F" (ss 22B(6A)(c), (d) and 22B(6B)(e), (f)), which is encoded.
A judgement about reason 2, flagged for a lawyer.

**F13. s 23A(6): "applies only in relation to offences committed after the order comes into force".**
Reading (a): "only" closes the list, so for an earlier offence the answer is `JUST FALSE`; (b): a limit on an order-making power is limited by its own wording and the answer is `NOTHING`.
Taken: (a), following the brief's list ("a list the text closes with “only”").

**F14. s 22B(3): "so far as the information is in the possession, or under the control, of the respondent".**
Reading (a): outside the respondent's possession or control the order simply does not require the information (`JUST FALSE`); (b): the text limits a requirement by its own wording and does not say no (`NOTHING`).
Taken: (b).

**F15. The seat's yes and no.**
A seat answer of `JUST FALSE` is the text's no on the facts as stated; the person is told nothing about facts they did not state.
Plain `BOOLEAN` inputs are used throughout so that every fact is stated; the one tri-state input is the Schedule 3A fact in the gathered question (see Seat).

**F16. How the ruling of 2026-11-05 was applied, and where the class of a clause was not clear.**
(a) A period the text fixes in its own words: the notice period of s 21ZA(2) and (3) (not yet ended, so the "if" is not met: `JUST FALSE`) and the applicable period of s 21CC(4)(d) and (7) (after the last day: `JUST FALSE`, as before).
The only periods the text counts are 7 working days (s 21ZA(3)) and 28 days (s 21CC(7)(b)); "as soon as is reasonably practicable" and "as soon as is practicable" (ss 19(2), 21(3)(c), 21A(4), 21B(4), 21C, 21CD(9), 21ZB(2)(b)) fix no period in the text's own words and are asked of the person as a yes or no.
Where a constable sets the period (s 21CC(7)(a)) and none is given, the period is outside the sources and the answer stays `NOTHING`.
(b) A "where" condition not met, `JUST FALSE`: s 19(4) (the three "Where" conditions), s 21CB(3) and (4) ("If the request states"), s 21CE(3)(a) and (b) ("In a case where"), s 23(2) to (6) ("Where a person is convicted of an offence under"); s 17A(4) ("If an offence under this section is committed by a Scottish partnership"), s 20(4), s 21(6), s 21CB(2) and s 21CD(1), (4) already answered `JUST FALSE`.
The same follows for "if" conditions on a power or permission: s 21CA(1) and (8), s 22B(1), (1A) and (8), and for "only so far as": s 21CD(2), (5), (7), (8)(a), (10).
(c) A scope limit with no "only", `NOTHING` outside the scope: s 17A(3), s 19(5), s 20(1) to (3), s 21(5) (the named offences), s 21CC(2) and (3), s 21CD(3), (6), (8)(b), (11), s 21CE(1) and (2), s 22B(3) and (9), s 22C, s 22D, s 22E, s 23(1), s 23B.
Meng's second ruling of 2026-11-05 (defences, "when", and definitions handed to a list) is applied in F18 and F23.
Clauses whose class I could not tell, and the one I took: s 21CA(8) ("if, and to the extent that": taken as an "if", `JUST FALSE`, with the extent not worked out); s 22B(3) ("so far as" without "only": taken as (c)); s 21CC(2) and (3) ("is to be treated as satisfying", good faith: taken as (c)).

**F17. s 21B(1): "A disclosure which satisfies the following three conditions".**
Readings: (a) a disclosure that does not satisfy all three conditions is outside the protection (`JUST FALSE`, like the three condition rules s 21B(2), (3) and (4)); (b) the protection is a grant limited by its own wording and the Act does not say such a disclosure breaches a restriction (`NOTHING`).
Taken: (a), as a condition the text states is not met.
Marginal: yes.

**F18. The defences worded "it is a defence ... to prove that" (ruled 2026-11-05, (b)).**
Sites: s 18(2) (L53, both limbs: did not know; had no reasonable cause to suspect), s 19(3) (L64), s 19(4) (L65-69, the proof in the closing words), s 21(5) (L108-110, both limbs), s 21ZC (L138-140, both limbs).
Ruled: when the condition is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" in the comment on each function and in the `@export` description of each seat question, and never "no defence at all", because another provision (one of the other four, or a protection such as s 21(2), s 21ZA or s 21ZB) may still protect the person.
Readings before the ruling were (a) `NOTHING` and (b) `JUST FALSE`; the encoding had taken (a).
Assumed, not ruled: the words "a person charged with an offence under ..." (ss 18(2), 19(3), 21ZC) and the offences named in s 21(5) are a scope limit with no "only" (ruling (c)), so a person not so charged, and a person charged under s 15(1) for s 21(5), still get `NOTHING`; only an unproved condition gets `JUST FALSE`.
The "where" conditions of s 19(4) are separate and answer `JUST FALSE` when not met (F16).
Other wording examined and not changed because it is not a "prove" defence: s 17A(2) and (4) ("is proved to have been committed with the consent or connivance of", L37 and L42, the liability of officers and partners); s 21A(5)(a) ("a person does not commit an offence under this section if ... he has a reasonable excuse", L153, a flat negative); s 21ZB(2) ("applies only where there is a reasonable excuse", L129-131, an "only where" condition); s 23A(4)(b) ("it has been proved, in accordance with section 31 of that Act", L591, a condition of scope).

**F19. Property clauses in the forfeiture powers (s 23(2) to (7), L555-570; s 23A(1), L571-576).**
Readings: (a) a clause that begins "which" or "in relation to which the following conditions are met" limits the property the court may forfeit, so property outside it is not mentioned and the answer is `NOTHING`; (b) it is a condition and failing it is `JUST FALSE`.
Taken: (a) for s 23(2) to (7) and s 23A(1) (reading M2).
Reviewer expected JUST FALSE; open question.

**F20. s 23A(2): is the list of offences closed?**
Readings: (a) "This section applies to an offence under—" followed by a list is a scope statement that does not say an unlisted offence is outside it (`NOTHING`); (b) the list is closed (`JUST FALSE`).
Taken: (a).
Reviewer expected JUST FALSE; open question.

**F21. s 21A(6)(b), L162: is the list of "relevant guidance" closed?**
Readings: (a) guidance that is "(a) issued by a supervisory authority or any other appropriate body, (b) approved by the Treasury, and (c) published in a manner it approved" is what the court must consider, and guidance outside the three is not addressed (`NOTHING`); (b) the three are the whole of "relevant guidance" (`JUST FALSE`).
Taken: (a).
Reviewer expected JUST FALSE; open question.

**F22. Left as encoded: s 21(2) and s 22B(12).**
Section 21(2) protects a person who "discloses to a constable"; no clause of s 21 counts an authorised National Crime Agency officer as a constable (unlike ss 19(7B), 20(5) and 21B(7)), and the encoding does not extend it, so a disclosure to such an officer is a plain "no" input.
Section 22B(12) bars a constable, a National Crime Agency officer or a counter-terrorism financial investigator who relies on Condition 1 or 2 unless senior or authorised; it does not name procurators fiscal, and the encoding does not add them.
Reviewer expected JUST FALSE; open question.

**F23. "When", "upon", "whenever", "until", and definitions handed to a list (ruled 2026-11-05, (a), (c), (d)).**
"When" occurs seven times in the deposited text, and "upon", "whenever" and "until" occur in none of it (checked by search).
Not conditions, so not "where" and no change: s 19(7)(b), s 21A(11)(b) ("at the time when he took the action", L79, L177) and s 21ZA(4) ("the part of the United Kingdom in which the person is when making the disclosure", L122) say when or where an act is judged and are not conditions; s 21CC(7)(a) ("specified by the constable when making the request", L274) and s 21CD(8)(a) ("after the time when the required notification was made", L300) are relative clauses that identify a period or a moment.
A real "when" condition, read as "where" (unmet is `JUST FALSE`), but not encoded: s 22F(5) ("When the Secretary of State has laid a draft of the code before Parliament the Secretary of State may bring it into operation by regulations", L546) is code-of-practice machinery and inert, reason 2 (F12); if it were encoded, a draft not yet laid would answer `JUST FALSE`.
Already answering as the ruling asks: s 23B(3)(a) ("in proceedings on indictment, when the prosecutor moves for sentence", L600) is inside the exception to a flat bar ("must not make an order ... except on the application of the prosecutor"), so an application made at any other time leaves the bar in force (`s 23B(3) the court in Scotland is barred from making the order` answers `JUST TRUE`).
"Until" does not occur, so rule (d) changed nothing.
Definitions handed to a list (rule (a)): a case in none of the heads answers `JUST FALSE` where the text says "means" and lists the heads, and that was already so for "terrorist property" (s 14(1)), "nominated officer" (s 21CF(5)), "relevant undertaking" (s 21CF(6)), "required disclosure" (s 21CF(7)), "law enforcement officer" and "senior law enforcement officer" (s 22B(14)).
Schedule 3A (s 19(7A), s 21A(10), s 21B(6), s 21CF(3), s 21CF(9)(a), s 21H(1) and (2), s 22B(13)) is handed the definition of a business in the regulated sector, of a supervisory authority and of a credit institution, but Schedule 3A is not among the sources, so the encoding takes "the answer Schedule 3A gives" as an input: it answers `JUST FALSE` when the caller says Schedule 3A gives no, and `NOTHING` when no answer is given (a pointer outside the text).
Bare lists with no such hand-off, left at `NOTHING`: s 22A(a) ("means any employment ... and includes", an open list), s 23A(2) and s 21A(6)(b) (F20, F21), and s 22B(14) "terrorist financing", which is defined only for Conditions 3 and 4 of s 22B, so for Conditions 1 and 2 the term is not defined and the answer is `NOTHING` (a scope limit with no "only", ruling (c)).

## What the text turns out to say

Numbered findings.
"Asserted." means a case in `ta-cases-seat.l4` or a `ta-tests-*.l4` file asserts it; where I did not assert it I say so.

1. **"Terrorist property" is a closed definition.** Section 14(1) says “means”, and s 14(2)(a), (b) extend only the two items they name, so property that fits none of the three limbs is not terrorist property (F1); an arrangement over such property misses the last element of s 18(1). Asserted (`Is this terrorist property`, all four inputs false, answers `JUST FALSE`; `Do I commit an offence by a laundering arrangement`, not terrorist property, answers `JUST FALSE`).
2. **The mental element differs from section to section.** Sections 15(1)(b), 15(2)(b) and 16(2)(b) are "intends ... or has reasonable cause to suspect that it may be used"; ss 15(3)(b) and 17(b) are "knows or has reasonable cause to suspect that it will or may be used"; s 16(1) needs no state of mind beyond using the property for the purposes of terrorism; s 17A(1)(c) is "the insurer or the person authorising the payment ... knows or has reasonable cause to suspect"; s 18(1) names none (F6). Asserted for each section.
3. **To provide is to give, lend or otherwise make available, "whether or not for consideration" (s 15(4)),** so a loan, and a payment for value, are both provision. Asserted (`Do I commit an offence by providing`: lent, for consideration).
4. **Section 18(2) is a defence the person must "prove":** if they do not prove both limbs, this section gives no defence on these facts (`JUST FALSE`, ruled 2026-11-05, F18); that does not say they have no defence at all, because another provision may give one. A person not charged under s 18(1) gets `NOTHING`. Asserted.
5. **Section 19(2) needs both the belief or suspicion and the information, and promptly (F2).** A person who tells a constable the belief but not the information on which it is based commits the offence. Asserted.
6. **Section 19(1A) takes regulated-sector information out of s 19** ("this section does not apply if the information came to the person in the course of a business in the regulated sector"); such a person is under s 21A instead. Asserted.
7. **The defences in s 19(3) and (4) are things the person must prove,** and when they are not proved those sections give no defence on these facts (`JUST FALSE`, F18). Asserted.
8. **Section 19(5) lifts the duty only for a "professional legal adviser" who obtained the information in privileged circumstances.** For anyone else, or for non-privileged information, s 19(5) is silent (`NOTHING`). Asserted.
9. **The permission in s 20(1) is limited to a disclosure to a constable** (or, under s 20(4), by the employer's procedure); telling someone else is outside it (`NOTHING`). Asserted.
10. **Acting with the express consent of a constable is a complete answer to ss 15 to 18 (s 21(1)).** A person who is not acting with consent gets `JUST FALSE` from this question, which says only that s 21(1) does not help them, not that they commit an offence. Asserted.
11. **Section 21(2) is protected only if all three conditions in s 21(3) hold** (after becoming concerned in the transaction, on the person's own initiative, as soon as reasonably practicable), and s 21(4) takes the protection away from a person who carries on after a constable forbids it. Asserted.
12. **The defence in s 21(5) names “any of sections 15(2) and (3) and 16 to 18”;** an inviter under s 15(1) is not named, so the defence is not given to them (`NOTHING`, a scope limit), and 17A is taken to be inside "16 to 18" (F7). For a named offence whose limbs are not proved the answer is `JUST FALSE` (F18). Asserted for s 15(1).
13. **The notice period in s 21ZA(3) is 7 working days, counted from the first working day after the disclosure, with Christmas Day, weekends, Good Friday and bank holidays left out (F3, F4).** Asserted by date, including a Christmas case.
14. **A person is "treated as having" consent only after the notice period ends without a notice of refusal;** a refusal received on or before the last day counts, and on the last day, or before it, the "if before the end of the notice period" is not met, so the answer is `JUST FALSE` (F3). Asserted.
15. **Sections 21ZB and 21ZC protect a later or intended disclosure,** on conditions: reasonable excuse for the earlier silence, the person's own initiative, as soon as reasonably practicable, and not carrying on once forbidden (s 21ZB(2), (3)); an intended disclosure with a reasonable excuse (s 21ZC, a defence to prove: `JUST FALSE` for that section when either limb is not proved, F18). Asserted.
16. **Two clocks, one for each duty.** Section 19(2) says "as soon as is reasonably practicable" and s 21A(4) says "as soon as is practicable after it comes to him". Neither fixes a number of days, so the seat asks the person whether they told in time as a fact. The gathered question returns the two clocks in two different answers. Asserted.
17. **Section 21A has three conditions and three exceptions.** The offence is not committed by a person who disclosed as soon as practicable, who has a reasonable excuse, or who is a legal or relevant professional adviser holding the information in privileged circumstances or an assistant to one (s 21A(5), (5A)). Asserted.
18. **Whether the duty falls under s 19 or s 21A turns on Schedule 3A, which is not among the sources.** A person who is not sure whether their business is in the regulated sector is told "the Act does not answer on these facts". Asserted.
19. **The protection in s 21B(1) is for "a disclosure which satisfies the following three conditions";** a disclosure that misses one is outside it (`JUST FALSE`, F17). Asserted.
20. **Tipping off (s 21D) is two offences.** Section 21D(1) is disclosing that a disclosure has been made (via a constable, the employer's procedure, a nominated officer or an authorised National Crime Agency officer) where that is likely to prejudice an investigation and the information came in the regulated sector; s 21D(3) is disclosing that an investigation is under way, on the same two further conditions. The exceptions in ss 21E to 21G each answer separately. Asserted.
21. **Condition 5 does not apply where a constable made the request (s 21CA(7)),** so a constable's request needs conditions 1 to 4 only (F8). Asserted.
22. **The applicable period for a joint disclosure report is whatever a constable specified when asking, or 28 days beginning with the notification day (day 1),** variable only by written notice (F9, F10). A report sent on the last day is in time. Asserted: 2 Nov to 29 Nov; 14 days to 15 Nov; sent 29 Nov in time, 30 Nov out of time.
23. **Section 21CD(9) has no number of days:** the notice that no report is being made is due "as soon as reasonably practicable after the period ends". Asserted as a decision and traced as an obligation (`ta-tests-voluntary-disclosure.l4`).
24. **Section 21CE(2) bars including information from a UK law enforcement agency unless the agency consents;** information from elsewhere is not addressed (`NOTHING`). Asserted.
25. **An information order reaches only what is in the respondent's possession or control (s 22B(3));** the court's discretion to ask for more is limited by that (F14). The magistrates' court's amount for non-compliance is a ceiling of £5,000 unless regulations have substituted another sum (s 22B(8), (10)). Asserted.
26. **Privilege is protected twice:** s 22E(1) says an information order does not confer a right to require privileged information (flat negative, `JUST FALSE` where the person would be entitled to refuse), and s 22E(3) says what is provided under an order is not taken to breach any restriction on disclosure. Asserted.
27. **The route of appeal depends on the court that decided:** the Crown Court from a magistrates' court in England and Wales, a county court from one in Northern Ireland, the Sheriff Appeal Court from the sheriff (s 22D(3)). Asserted.
28. **The penalty is a ceiling, and part of it is outside the Act.** Section 22 gives 14 years on indictment (and "a fine", with no ceiling stated) and six months and "a fine not exceeding the statutory maximum" on summary conviction; the amount of the statutory maximum is an input. Asserted.
29. **Forfeiture is a power, not a duty, and each subsection is tied to named offences:** s 23(2) (ss 15(1), 15(2), 16), (3) (s 15(3)), (4) (ss 17, 18), (5) (s 17), (5A) (s 17A), (6) (s 18), (7) (any of ss 15 to 18, for a payment or reward). A conviction for an offence a subsection does not name is that subsection's `JUST FALSE` ("Where a person is convicted of an offence under ..."). Where the offence fits but the property does not, or no subsection gives the power on the stated facts, the Act does not say the court may not forfeit, so the answer is `NOTHING` (F19). Asserted.
30. **A person claiming an interest in property that may be forfeited has a right to be heard, except the convicted person (s 23B(1)).** Asserted.
31. **An order adding an offence to s 23A(2) applies only to offences committed after it comes into force (s 23A(6)).** Asserted in `ta-tests-forfeiture.l4`; not in the seat.
32. **The sections 24 to 31 shown in the text are repealed and blank;** they have rows and no rules.
33. **The range "sections 15 to 18" takes in s 17A (F7).** A reader who counts four offences in that range has left out the insurer's. Asserted in `ta-tests-disclosure.l4` (s 21(5)) and `ta-tests-voluntary-disclosure.l4` (s 21CF(10)); not in the seat.
34. **A permission or power given "if" conditions is `JUST FALSE` when they fail:** s 21CA(1) (a disclosure within the regulated sector needs conditions 1 to 4 and, where applicable, 5), s 22B(1) and (1A) (an information order needs the right applicant and condition 1 or 2, or 3 or 4), s 22B(8) (the amount for non-compliance needs a failure to comply with an order of a magistrates' court). Asserted.
35. **"Only so far as" limits are `JUST FALSE` outside them:** s 21CD(2), (5), (7), (8)(a) and (10) say how far s 21CC(2) and (3) reach, and a matter outside is not covered. Asserted.
36. **Section 19(4)'s three "Where" conditions (in employment; the employer has a procedure; charged) are `JUST FALSE` when not met,** and the proof the person must make is also `JUST FALSE` when not made, as "this section gives no defence on these facts" (F16, F18). Asserted.
37. **A constable's notice varying the 28 days of s 21CC(8) is covered only if it is in writing, from a constable, to the person who made the required notification;** any other notice is `NOTHING` (F10). Asserted.

## Marginal readings for a lawyer

The brief marks two readings as "for a lawyer, not for you to decide", and this encoding takes them as the status quo.
(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
Every branch that rests on (a) is tagged M1 in the table; the other reading is that the text is silent on the case that fails the condition and the answer is `NOTHING`.
(b) A prohibition or grant limited by its own wording does not give a no.
Every branch that rests on (b) is tagged M2 in the table; the other reading is that the case outside the limit is the text's no and the answer is `JUST FALSE`.
Meng's ruling of 2026-11-05 (in the fork register) settles three classes the first version of this encoding had put under (b): a period the text fixes in its own words, a "where" condition, and an "only so far as" limit now answer `JUST FALSE`, while a scope limit with no "only" stays `NOTHING`.
The table below is regenerated from the code and shows the position after that ruling.
Rows marked "a definition that says it means" are not marginal, and neither are the `NOTHING` rows tagged includes, silent, points outside the text, undefined term or list not closed: those follow the brief's rule directly and are listed so that a lawyer can see them, not because they rest on a reading.

<!-- MARGINAL:BEGIN -->

Generated by `coverage.py` from the `-- FALSE-kind` and `-- NOTHING-kind` comments in the modules (243 tagged branches): FALSE M1: 133; FALSE a definition that says it means (not marginal): 25; NOTHING M2: 51; NOTHING NOTHING includes: 13; NOTHING NOTHING points outside the text: 16; NOTHING NOTHING silent: 4; NOTHING NOTHING undefined term: 1.

| rule | where | tag | the text's words | other reading |
|---|---|---|---|---|
| `s 22A(a) the work is employment` | ta-disclosure.l4:34 | NOTHING (includes) | "“employment” means any employment (whether paid or unpaid) and includes—" | - |
| `s 22A(b) the person is the employer` | ta-disclosure.l4:46 | NOTHING (undefined term) | "“employer” has a corresponding meaning" | - |
| `s 19(1) this section applies to the person` | ta-disclosure.l4:65 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This section applies where a person—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(1A) this section does not apply to the person` | ta-disclosure.l4:76 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "But this section does not apply if the information came to the person in the course of a business in the regulated sector." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(7A) the business is a business in the regulated sector` | ta-disclosure.l4:84 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 19(2) the person commits an offence by not disclosing to a constable` | ta-disclosure.l4:96 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "But this section does not apply if the information came to the person in the course of a business in the regulated sector." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(2) the person commits an offence by not disclosing to a constable` | ta-disclosure.l4:99 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The person commits an offence if he does not disclose to a constable as soon as is reasonably practicable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(3) the person has a defence` | ta-disclosure.l4:126 | M2: a grant or prohibition limited by its own wording does not give a no | "a person charged with an offence under subsection (2)" (a person not so charged is outside the grant: a scope limit with no "only", ruling of 2026-11-05, (c); assumed, not ruled, that this limb is a scope limit and not part of the proof, fork F18) | the case outside the limit is the text’s no: JUST FALSE |
| `s 19(3) the person has a defence` | ta-disclosure.l4:131 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "It is a defence for a person charged with an offence under subsection (2) to prove that he had a reasonable excuse" (the proof is not made: ruling of 2026-11-05, (b); this section gives no defence on these facts) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(4) the person has a defence` | ta-disclosure.l4:151 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where— (a) a person is in employment, (b) his employer has established a procedure for the making of disclosures of the matters specified in subsection (2), and (c) he is charged with an offence under that subsection," (a "where" condition that is not met: ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(4) the person has a defence` | ta-disclosure.l4:156 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "it is a defence for him to prove that he disclosed the matters specified in that subsection in accordance with the procedure" (the "where" conditions hold and the proof is not made: ruling of 2026-11-05, (b); this section gives no defence on these facts) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(6) the information is obtained by the adviser in privileged circumstances` | ta-disclosure.l4:173 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "information is obtained by an adviser in privileged circumstances if it comes to him, otherwise than with a view to furthering a criminal purpose" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(5) subsection (2) requires the professional legal adviser to disclose` | ta-disclosure.l4:190 | M2: a grant or prohibition limited by its own wording does not give a no | "by a professional legal adviser of— (a) information which he obtains in privileged circumstances" (outside the adviser's privileged information the subsection says nothing) | the case outside the limit is the text’s no: JUST FALSE |
| `s 19(7) the person is treated as having committed an offence under one of sections 15 to 18` | ta-disclosure.l4:204 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a person shall be treated as having committed an offence under one of sections 15 to 18 if" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 19(7B) the person is a constable for the purposes of s 19` | ta-disclosure.l4:215 | NOTHING (includes) | "The reference to a constable includes a reference to a National Crime Agency officer authorised" | - |
| `s 19(8) the ceiling of the penalty for an offence under s 19` | ta-disclosure.l4:228 | NOTHING (silent) | "to a fine or to both" states no ceiling for the fine | - |
| `s 20(1) the person may disclose to a constable` | ta-disclosure.l4:247 | M2: a grant or prohibition limited by its own wording does not give a no | "A person may disclose to a constable—" (a disclosure of another kind, or to another person, is outside the grant) | the case outside the limit is the text’s no: JUST FALSE |
| `s 20(2) the person may make a disclosure to a constable in the circumstances mentioned in s 19(1) and (2)` | ta-disclosure.l4:269 | M2: a grant or prohibition limited by its own wording does not give a no | "A person may make a disclosure to a constable in the circumstances mentioned in section 19(1) and (2)" | the case outside the limit is the text’s no: JUST FALSE |
| `s 20(3) a restriction on disclosure imposed by statute or otherwise does not prevent the disclosure` | ta-disclosure.l4:281 | M2: a grant or prohibition limited by its own wording does not give a no | "Subsections (1) and (2) shall have effect notwithstanding any restriction" (a disclosure outside (1) and (2) is outside the override) | the case outside the limit is the text’s no: JUST FALSE |
| `s 20(4) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` | ta-disclosure.l4:299 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where— (a) a person is in employment, and (b) his employer has established a procedure" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 20(5) the person is a constable for the purposes of s 20` | ta-disclosure.l4:310 | NOTHING (includes) | "References to a constable include references to a National Crime Agency officer authorised" | - |
| `s 21(1) the person does not commit an offence under any of sections 15 to 18 by acting with the express consent of a constable` | ta-disclosure.l4:323 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under any of sections 15 to 18 if he is acting with the express consent of a constable." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(3) subsection (2) applies to the person's disclosure` | ta-disclosure.l4:339 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsection (2) applies only where a person makes a disclosure" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(4) subsection (2) does not apply to the person` | ta-disclosure.l4:352 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsection (2) does not apply to a person if" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(2) the person does not commit an offence under any of sections 15 to 18 by involvement in the transaction` | ta-disclosure.l4:369 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a person does not commit an offence under any of sections 15 to 18 by involvement in a transaction or arrangement relating to money or other property if he discloses to a constable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(5) the person has a defence` | ta-disclosure.l4:385 | M2: a grant or prohibition limited by its own wording does not give a no | "any of sections 15(2) and (3) and 16 to 18" (section 15(1) is not named: a scope limit with no "only", ruling of 2026-11-05, (c)) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21(5) the person has a defence` | ta-disclosure.l4:391 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "It is a defence for a person charged with an offence under any of sections 15(2) and (3) and 16 to 18 to prove that— (a) he intended to make a disclosure of the kind mentioned in subsections (2) and (3), and (b) there is reasonable excuse for his failure to do so" (either limb is not proved: ruling of 2026-11-05, (b); this section gives no defence on these facts) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(6) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` | ta-disclosure.l4:409 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where— (a) a person is in employment, and (b) his employer has established a procedure" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21(7) the involvement is in a transaction or arrangement relating to money or other property` | ta-disclosure.l4:421 | NOTHING (includes) | "includes a reference to use or possession" | - |
| `s 21ZA(4) the day is a working day` | ta-disclosure.l4:433 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A working day is a day other than a Saturday, a Sunday" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(4) the day is a working day` | ta-disclosure.l4:435 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A working day is a day other than ... Christmas Day" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(4) the day is a working day` | ta-disclosure.l4:437 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A working day is a day other than ... Good Friday or a day that is a bank holiday under the Banking and Financial Dealings Act 1971" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(2) the person is treated as having the authorised officer's consent` | ta-disclosure.l4:473 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person is treated as having an authorised officer's consent if before the end of the notice period the person does not receive notice" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(2) the person is treated as having the authorised officer's consent` | ta-disclosure.l4:479 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person is treated as having an authorised officer's consent if before the end of the notice period the person does not receive notice" (the period has not yet ended, so the "if" is not met: ruling of 2026-11-05, (a); fork F3) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed first and had consent` | ta-disclosure.l4:494 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under any of sections 15 to 18 by involvement in a transaction or an arrangement relating to money or other property if, before becoming involved" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZA(5) the person is an authorised officer` | ta-disclosure.l4:505 | a definition that says it means (not marginal) | "“authorised officer” means a National Crime Agency officer authorised for the purposes of this section by the Director General of that Agency" | - |
| `s 21ZA(6) the involvement is in a transaction or arrangement relating to money or other property` | ta-disclosure.l4:517 | NOTHING (includes) | "includes a reference to use or possession" | - |
| `s 21ZB(2) section 21ZB applies to the person` | ta-disclosure.l4:534 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This section applies only where" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZB(3) section 21ZB does not apply to the person` | ta-disclosure.l4:547 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This section does not apply to a person if" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZB(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed afterwards` | ta-disclosure.l4:563 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under any of sections 15 to 18 by involvement in a transaction or an arrangement relating to money or other property if, after becoming involved" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21ZB(4) the person is an authorised officer` | ta-disclosure.l4:574 | a definition that says it means (not marginal) | "“authorised officer” means a National Crime Agency officer authorised for the purposes of this section by the Director General of that Agency" | - |
| `s 21ZB(5) the involvement is in a transaction or arrangement relating to money or other property` | ta-disclosure.l4:586 | NOTHING (includes) | "includes a reference to use or possession" | - |
| `s 21ZC the person has a defence` | ta-disclosure.l4:603 | M2: a grant or prohibition limited by its own wording does not give a no | "a person charged with an offence under any of sections 15 to 18" (a person not so charged is outside the grant: a scope limit with no "only", ruling of 2026-11-05, (c); assumed, not ruled, that this limb is a scope limit and not part of the proof, fork F18) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21ZC the person has a defence` | ta-disclosure.l4:609 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "It is a defence for a person charged with an offence under any of sections 15 to 18 to prove that— (a) the person intended to make a disclosure of the kind mentioned in section 21ZA or 21ZB, and (b) there is a reasonable excuse for the person's failure to do so" (either limb is not proved: ruling of 2026-11-05, (b); this section gives no defence on these facts) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(1) the court may make a forfeiture order` | ta-forfeiture.l4:24 | M2: a grant or prohibition limited by its own wording does not give a no | "The court by or before which a person is convicted of an offence under any of sections 15 to 18 may make a forfeiture order in accordance with the provisions of this section." (a court that did not convict is not said to lack the power) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(2) the court may order the forfeiture of the property` | ta-forfeiture.l4:40 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 15(1) or (2) or 16" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(2) the property is within the subsection` | ta-forfeiture.l4:59 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of any money or other property which, at the time of the offence, the person had in their possession or under their control and which— (a) had been used for the purposes of terrorism, or (b) they intended should be used, or had reasonable cause to suspect might be used" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(3) the court may order the forfeiture of the property` | ta-forfeiture.l4:76 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of any money or other property which, at the time of the offence, the person had in their possession or under their control and which— (a) had been used for the purposes of terrorism, or (b) ... they knew or had reasonable cause to suspect would or might be used" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(3) the court may order the forfeiture of the property` | ta-forfeiture.l4:78 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 15(3)" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(4) the court may order the forfeiture of the property` | ta-forfeiture.l4:100 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of any money or other property which, at the time of the offence, the person had in their possession or under their control and which— (a) had been used for the purposes of terrorism, or (b) was, at that time, intended by them to be used for those purposes" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(4) the court may order the forfeiture of the property` | ta-forfeiture.l4:106 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of any money or other property which, at the time of the offence, the person had in their possession or under their control and which— (a) had been used for the purposes of terrorism, or (b) was, at that time, intended by them to be used for those purposes" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(4) the court may order the forfeiture of the property` | ta-forfeiture.l4:108 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 17 or 18" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(5) the court may order the forfeiture of the property` | ta-forfeiture.l4:130 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of the money or other property to which the arrangement in question related, and which— (a) had been used for the purposes of terrorism, or (b) at the time of the offence, the person knew or had reasonable cause to suspect would or might be used" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(5) the court may order the forfeiture of the property` | ta-forfeiture.l4:132 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 17" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(5A) the court may order the forfeiture of the amount` | ta-forfeiture.l4:151 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of the amount paid under, or purportedly under, the insurance contract" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(5A) the court may order the forfeiture of the amount` | ta-forfeiture.l4:153 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 17A" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(6) the court may order the forfeiture of the property` | ta-forfeiture.l4:172 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of the money or other property to which the arrangement in question related" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23(6) the court may order the forfeiture of the property` | ta-forfeiture.l4:174 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a person is convicted of an offence under section 18" (a "where" condition that is not met: the person was convicted of a different offence; ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23(7) the court may order the forfeiture of the payment or reward` | ta-forfeiture.l4:194 | M2: a grant or prohibition limited by its own wording does not give a no | "the court may order the forfeiture of any money or other property which wholly or partly, and directly or indirectly, is received by any person as a payment or other reward in connection with the commission of the offence" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23A(2) this section applies to the offence` | ta-forfeiture.l4:229 | M2: a grant or prohibition limited by its own wording does not give a no | "This section applies to an offence under— (a) any of the following provisions of this Act ... (b) any of the following provisions of Part 1 of the Terrorism Act 2006" (subsections (3) and (4) extend the section to other offences) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23A(3) this section applies to the ancillary offence` | ta-forfeiture.l4:240 | M2: a grant or prohibition limited by its own wording does not give a no | "This section applies to any ancillary offence (as defined in section 94 of the Counter-Terrorism Act 2008) in relation to an offence listed in subsection (2)." (other offences are dealt with by subsections (2) and (4)) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23A(4) this section applies to the offence with a terrorist connection` | ta-forfeiture.l4:253 | M2: a grant or prohibition limited by its own wording does not give a no | "This section also applies to an offence ... as to which— (a) in England and Wales, the court dealing with the offence has determined ... (b) in Scotland, it has been proved" (the subsection is silent on Northern Ireland) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23A(1) the court may order the forfeiture of the property` | ta-forfeiture.l4:274 | M2: a grant or prohibition limited by its own wording does not give a no | "The court by or before which a person is convicted of an offence to which this section applies may order the forfeiture of any money or other property in relation to which the following conditions are met" (property outside the conditions is not said to be immune from forfeiture) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23A(6) the order adding the offence to subsection (2) applies to the offence` | ta-forfeiture.l4:284 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "An order adding an offence to subsection (2) applies only in relation to offences committed after the order comes into force." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23B(1) the court must give the person an opportunity to be heard` | ta-forfeiture.l4:297 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "to any person, other than the convicted person, who claims to be the owner or otherwise interested" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23B(1) the court must give the person an opportunity to be heard` | ta-forfeiture.l4:301 | M2: a grant or prohibition limited by its own wording does not give a no | "Before making an order under section 23 or 23A, a court must give an opportunity to be heard to any person ... who claims to be the owner or otherwise interested" (a person who makes no claim is not said to have the right) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23B(2) the court shall have regard to the value of the property and the effects on the convicted person` | ta-forfeiture.l4:322 | M2: a grant or prohibition limited by its own wording does not give a no | "In considering whether to make an order under section 23 or 23A in respect of any property, a court shall have regard to—" | the case outside the limit is the text’s no: JUST FALSE |
| `s 23B(3) the court in Scotland is barred from making the order` | ta-forfeiture.l4:350 | M2: a grant or prohibition limited by its own wording does not give a no | "A court in Scotland must not make an order under section 23 or 23A except on the application of the prosecutor" (courts elsewhere are outside the subsection) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23B(3) the court in Scotland is barred from making the order` | ta-forfeiture.l4:352 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "except on the application of the prosecutor— (a) in proceedings on indictment, when the prosecutor moves for sentence, and (b) in summary proceedings, before the court sentences the accused" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 23B(3) the order of a Scottish court is a sentence for the purposes of any appeal or review` | ta-forfeiture.l4:380 | M2: a grant or prohibition limited by its own wording does not give a no | "for the purposes of any appeal or review, an order under either of those sections made by a court in Scotland is a sentence" (an order made elsewhere is outside the clause) | the case outside the limit is the text’s no: JUST FALSE |
| `s 23B(4) Schedule 4 makes further provision for the order` | ta-forfeiture.l4:390 | NOTHING (points outside the text) | "Schedule 4 makes further provision in relation to forfeiture orders under section 23 or 23A", and Schedule 4 is not among the sources, so what it provides is not answered | - |
| `s 22B(4) condition 1 is met` | ta-information-orders.l4:34 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 1 for the making of an information order is met if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(5) condition 2 is met` | ta-information-orders.l4:54 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 2 for the making of an information order is met if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(6) the request is an external request` | ta-information-orders.l4:67 | a definition that says it means (not marginal) | "“external request” means a request made by an authority of a foreign country which has responsibility in that country for carrying out investigations" | - |
| `s 22B(6A) condition 3 is met` | ta-information-orders.l4:96 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 3 for the making of an information order is met if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(6B) condition 4 is met` | ta-information-orders.l4:128 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 4 for the making of an information order is met if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(1) the court may make an information order` | ta-information-orders.l4:141 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "may, on an application made by a law enforcement officer, make an information order if satisfied that either condition 1 or condition 2 is met" (a power given "if" a condition is met: when the applicant is not a law enforcement officer, or neither condition is met, the "if" fails; ruling of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(1A) the court may make an information order` | ta-information-orders.l4:163 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "may, on an application made— (a) in the case of a magistrates' court, by the Director General of the National Crime Agency or an authorised NCA officer, and (b) in the case of the sheriff, by a procurator fiscal, make an information order if satisfied that either condition 3 or condition 4 is met" (a power given "if" a condition is met: when the applicant is not the person the paragraph names, or neither condition is met, the "if" fails; ruling of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(2) the application has the content the subsection requires` | ta-information-orders.l4:186 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The application must— (a) specify or describe the information sought under the order, and (b) specify the person from whom the information is sought" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(3) the order requires the respondent to provide the information` | ta-information-orders.l4:203 | M2: a grant or prohibition limited by its own wording does not give a no | "so far as the information is in the possession, or under the control, of the respondent" (information outside the respondent's possession or control is outside what the order requires, but the subsection does not say the respondent need not answer for it) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22B(7) the order has the content the subsection requires` | ta-information-orders.l4:231 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "An information order must specify— (a) how the information required under the order is to be provided, and (b) the date by which it is to be provided." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(8) the magistrates court may order the person to pay an amount` | ta-information-orders.l4:243 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If a person fails to comply with an information order made by a magistrates' court, the magistrates' court may order the person to pay" (a power given "if": no failure to comply, or an order made by the sheriff, and the "if" fails; ruling of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(9) the sum is treated as adjudged to be paid by a conviction of the court` | ta-information-orders.l4:264 | M2: a grant or prohibition limited by its own wording does not give a no | "The sum mentioned in subsection (8) is to be treated as adjudged to be paid by a conviction of the court" (any other sum is outside the deeming) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22B(12) the officer is barred from making the application` | ta-information-orders.l4:277 | M2: a grant or prohibition limited by its own wording does not give a no | "A law enforcement officer who is a constable, a National Crime Agency officer or a counter-terrorism financial investigator may not make an application under this section in reliance on Condition 1 or 2" (a procurator fiscal, or an application on Condition 3 or 4, is outside the bar) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22B(12) the officer is barred from making the application` | ta-information-orders.l4:279 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "unless the officer is a senior law enforcement officer or is authorised to do so by a senior law enforcement officer" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(13) the business is a business in the regulated sector` | ta-information-orders.l4:298 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 22B(14) the person is an authorised NCA officer` | ta-information-orders.l4:309 | a definition that says it means (not marginal) | "“authorised NCA officer” means an officer of the National Crime Agency authorised by the Director General (whether generally or specifically) for the purposes of this section" | - |
| `s 22B(14) the requirement is a corresponding disclosure requirement` | ta-information-orders.l4:320 | a definition that says it means (not marginal) | "“corresponding disclosure requirement” means a requirement to make a disclosure under the law of the foreign country concerned that corresponds to a requirement imposed by virtue of this Part" | - |
| `s 22B(14) the offence is a corresponding terrorist financing offence` | ta-information-orders.l4:332 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "“corresponding terrorist financing offence” means an offence under the law of the foreign country concerned that would, if done in the United Kingdom, constitute an offence under any of sections 15 to 18" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22B(14) the function is the criminal intelligence function` | ta-information-orders.l4:340 | NOTHING (points outside the text) | "“the criminal intelligence function” has the meaning given by section 1(5) of the Crime and Courts Act 2013", which is not among the sources; with no answer from it, NOTHING | - |
| `s 22B(14) the place is a foreign country` | ta-information-orders.l4:350 | a definition that says it means (not marginal) | "“foreign country” means a country or territory outside the United Kingdom" | - |
| `s 22B(14) the body is a foreign FIU` | ta-information-orders.l4:361 | a definition that says it means (not marginal) | "“foreign FIU” means a body in a foreign country carrying out the functions of a financial intelligence unit" | - |
| `s 22B(14) the person is a law enforcement officer` | ta-information-orders.l4:378 | a definition that says it means (not marginal) | "“law enforcement officer” means— a constable, a National Crime Agency officer authorised ..., a counter-terrorism financial investigator, or a procurator fiscal" | - |
| `s 22B(14) the person is a senior law enforcement officer` | ta-information-orders.l4:393 | a definition that says it means (not marginal) | "“senior law enforcement officer” means— a police officer of at least the rank of superintendent; the Director General of the National Crime Agency; any other National Crime Agency officer authorised" | - |
| `s 22B(14) the act is terrorist financing` | ta-information-orders.l4:411 | M2: a grant or prohibition limited by its own wording does not give a no | "“terrorist financing” means— for the purposes of subsection (6A), ...; for the purposes of subsection (6B), ..." (the term is defined for conditions 3 and 4 only) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22C(1) the statement may not be used in evidence against the person` | ta-information-orders.l4:426 | M2: a grant or prohibition limited by its own wording does not give a no | "A statement made by a person in response to an information order may not be used in evidence against the person in criminal proceedings." (a statement made otherwise, or used in other proceedings, is outside the bar) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22C(2) subsection (1) does not apply` | ta-information-orders.l4:442 | M2: a grant or prohibition limited by its own wording does not give a no | "Subsection (1) does not apply— (a) in the case of proceedings under this Part, (b) on a prosecution for perjury, or (c) ..." (in any other case the subsection says nothing) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22C(3) the statement may not be used by virtue of subsection (2)(c)` | ta-information-orders.l4:458 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A statement may not be used by virtue of subsection (2)(c) unless— (a) evidence relating to it is adduced, or (b) a question relating to it is asked" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22C(4) the prosecution is a prosecution for perjury` | ta-information-orders.l4:474 | NOTHING (silent) | the subsection names the offence for England and Wales and for Northern Ireland and nothing for Scotland | - |
| `s 22D(1) an appeal lies to the relevant appeal court` | ta-information-orders.l4:486 | M2: a grant or prohibition limited by its own wording does not give a no | "An appeal from a decision on an application for an information order lies to the relevant appeal court." (a decision on anything else is outside the subsection) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22D(2) the person may bring the appeal` | ta-information-orders.l4:496 | M2: a grant or prohibition limited by its own wording does not give a no | "An appeal under this section lies at the instance of any person who was a party to the proceedings on the application." (a person who was not a party is not said to lack a right of appeal) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22D(4) the relevant appeal court may make, discharge or vary the order` | ta-information-orders.l4:521 | M2: a grant or prohibition limited by its own wording does not give a no | "On an appeal under this section the relevant appeal court may— (a) make or (as the case may be) discharge an information order, or (b) vary the order." (the power is given for an appeal under this section only) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22E(1) the information order confers the right to require the information` | ta-information-orders.l4:532 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "An information order does not confer the right to require a person to provide privileged information." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22E(1) the information order confers the right to require the information` | ta-information-orders.l4:534 | M2: a grant or prohibition limited by its own wording does not give a no | "does not confer the right to require a person to provide privileged information" (for other information the subsection says nothing; the right comes from s 22B(3)) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22E(2) the information is privileged information` | ta-information-orders.l4:545 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "“Privileged information” is information which a person would be entitled to refuse to provide on grounds of legal professional privilege" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22E(3) the provision of the information does not breach any restriction on disclosure` | ta-information-orders.l4:555 | M2: a grant or prohibition limited by its own wording does not give a no | "Information provided in pursuance of an information order is not to be taken to breach any restriction on the disclosure of information (however imposed)." (information provided otherwise is outside it) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22E(4) the application may be heard and determined in private` | ta-information-orders.l4:565 | M2: a grant or prohibition limited by its own wording does not give a no | "An application for an information order may be heard and determined in private." (a permission only) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22F(7) the failure of itself makes the person liable to criminal or civil proceedings` | ta-information-orders.l4:576 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A failure by a person to comply with a provision of the code does not of itself make the person liable to criminal or civil proceedings." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22F(7) the failure of itself makes the person liable to criminal or civil proceedings` | ta-information-orders.l4:578 | M2: a grant or prohibition limited by its own wording does not give a no | "A failure by a person to comply with a provision of the code" (nothing is said where there is no failure) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22F(8) the code is admissible and is to be taken into account` | ta-information-orders.l4:589 | M2: a grant or prohibition limited by its own wording does not give a no | "The code is admissible in evidence in criminal or civil proceedings and is to be taken into account by a court or tribunal in any case in which it appears to the court or tribunal to be relevant." (the subsection does not say the code is inadmissible elsewhere) | the case outside the limit is the text’s no: JUST FALSE |
| `s 22F(10) the term has the meaning given in s 22B(14)` | ta-information-orders.l4:599 | M2: a grant or prohibition limited by its own wording does not give a no | "In this section “authorised NCA officer” has the meaning given in section 22B(14)." (terms elsewhere are not touched) | the case outside the limit is the text’s no: JUST FALSE |
| `s 14(2)(a) the property is proceeds of the act` | ta-interpretation.l4:27 | NOTHING (includes) | "includes a reference to any property which wholly or partly, and directly or indirectly, represents the proceeds of the act" | - |
| `s 14(2)(b) the property is among the organisation's resources` | ta-interpretation.l4:38 | NOTHING (includes) | "includes a reference to any money or other property which is applied or made available, or is to be applied or made available, for use by the organisation" | - |
| `s 14(1) the property is terrorist property` | ta-interpretation.l4:77 | a definition that says it means (not marginal) | "In this Act “terrorist property” means—" (a definition that says "means" is closed; s 14(2) begins "In subsection (1)" and extends only the two items it names, "proceeds of an act" and "an organisation’s resources", which the limbs already consult, so property that fits no limb is outside the definition: fork F1, reading (a)) | - |
| `s 15(4) the person provides money or other property` | ta-offences.l4:24 | a definition that says it means (not marginal) | "is a reference to its being given, lent or otherwise made available, whether or not for consideration" | - |
| `s 15(1) the person commits an offence by inviting another to provide money or other property` | ta-offences.l4:40 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 15(2) the person commits an offence by receiving money or other property` | ta-offences.l4:56 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 15(3) the person commits an offence by providing money or other property` | ta-offences.l4:73 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 16(1) the person commits an offence by using money or other property for the purposes of terrorism` | ta-offences.l4:86 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he uses money or other property for the purposes of terrorism." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 16(2) the person commits an offence by possessing money or other property` | ta-offences.l4:102 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 17 the person commits an offence by a funding arrangement` | ta-offences.l4:121 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 17A(1) the insurer commits an offence by paying under the contract` | ta-offences.l4:141 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The insurer under an insurance contract commits an offence if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 17A(2) the officer is guilty of the offence as well as the body corporate` | ta-offences.l4:159 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If an offence under this section committed by a body corporate is proved to have been committed" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 17A(3) the person is the body corporate's director for the purposes of s 17A(2)` | ta-offences.l4:171 | a definition that says it means (not marginal) | "is a reference to a member of the body corporate" (a person who is not a member is not the reference) | - |
| `s 17A(3) the person is the body corporate's director for the purposes of s 17A(2)` | ta-offences.l4:174 | M2: a grant or prohibition limited by its own wording does not give a no | "in relation to a body corporate whose affairs are managed by its members" (any other body corporate is outside the subsection) | the case outside the limit is the text’s no: JUST FALSE |
| `s 17A(4) the partner is guilty of the offence as well as the partnership` | ta-offences.l4:192 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If an offence under this section is committed by a Scottish partnership and is proved to have been committed" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 17A(5) the contract is an insurance contract` | ta-offences.l4:204 | a definition that says it means (not marginal) | "“insurance contract” means a contract under which" | - |
| `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` | ta-offences.l4:226 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if he enters into or becomes concerned in an arrangement which facilitates" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 18(2) the person has a defence` | ta-offences.l4:238 | M2: a grant or prohibition limited by its own wording does not give a no | "a person charged with an offence under subsection (1)" (a person not so charged is outside the grant: a scope limit with no "only", ruling of 2026-11-05, (c); assumed, not ruled, that this limb is a scope limit and not part of the proof, fork F18) | the case outside the limit is the text’s no: JUST FALSE |
| `s 18(2) the person has a defence` | ta-offences.l4:244 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "It is a defence for a person charged with an offence under subsection (1) to prove that he did not know and had no reasonable cause to suspect" (the proof is not made, on either limb: ruling of 2026-11-05, (b); this section gives no defence on these facts) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 22 the ceiling of the penalty for an offence under any of sections 15 to 18` | ta-offences.l4:259 | NOTHING (silent) | "to a fine or to both" states no ceiling for the fine | - |
| `s 21A(2) the first condition is satisfied` | ta-regulated-sector.l4:27 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The first condition is that he—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(3) the second condition is satisfied` | ta-regulated-sector.l4:41 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The second condition is that the information or other matter" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(4) the third condition is satisfied` | ta-regulated-sector.l4:52 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The third condition is that he does not disclose the information or other matter to a constable or a nominated officer as soon as is practicable after it comes to him." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(1) the person commits an offence if each of the three conditions is satisfied` | ta-regulated-sector.l4:65 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if each of the following three conditions is satisfied." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(5A) subsection (5A) applies to the person` | ta-regulated-sector.l4:81 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This subsection applies to a person if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(5) the person does not commit an offence under section 21A` | ta-regulated-sector.l4:98 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "But a person does not commit an offence under this section if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(1) and (5) the person commits an offence under section 21A` | ta-regulated-sector.l4:126 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "But a person does not commit an offence under this section if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(6) the guidance is relevant guidance the court must consider` | ta-regulated-sector.l4:145 | M2: a grant or prohibition limited by its own wording does not give a no | "the court must consider whether he followed any relevant guidance which was at the time concerned— (a) issued ... (b) approved ... (c) published" (guidance outside (a) to (c) is not said to be irrelevant) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21A(7) the disclosure is a disclosure to a nominated officer` | ta-regulated-sector.l4:172 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A disclosure to a nominated officer is a disclosure which—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` | ta-regulated-sector.l4:188 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Information or other matter comes to a professional legal adviser or relevant professional adviser in privileged circumstances if it is communicated or given to him—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(9) subsection (8) does not apply to the information or other matter` | ta-regulated-sector.l4:199 | M2: a grant or prohibition limited by its own wording does not give a no | "But subsection (8) does not apply to information or other matter which is communicated or given with a view to furthering a criminal purpose." (any other communication is outside this subsection) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` | ta-regulated-sector.l4:212 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "But subsection (8) does not apply to information or other matter which is communicated or given with a view to furthering a criminal purpose." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(10)(a) the business is a business in the regulated sector` | ta-regulated-sector.l4:224 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 21A(10)(b) the body is a supervisory authority` | ta-regulated-sector.l4:234 | NOTHING (points outside the text) | Schedule 3A decides what is a supervisory authority and is not among the sources; with no answer from it, NOTHING | - |
| `s 21A(11) the person is to be taken to have committed an offence mentioned in s 21A(2)` | ta-regulated-sector.l4:248 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a person is to be taken to have committed an offence there mentioned if" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(12) the ceiling of the penalty for an offence under s 21A` | ta-regulated-sector.l4:261 | NOTHING (silent) | "or to a fine or to both" states no ceiling for the fine | - |
| `s 21A(13) the body is an appropriate body` | ta-regulated-sector.l4:272 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "An appropriate body is any body which regulates or is representative of" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21A(14) the person is a constable for the purposes of s 21A` | ta-regulated-sector.l4:283 | NOTHING (includes) | "The reference to a constable includes a reference to a National Crime Agency officer authorised" | - |
| `s 21A(15) the person is a relevant professional adviser` | ta-regulated-sector.l4:299 | a definition that says it means (not marginal) | "“relevant professional adviser” means an accountant, auditor or tax adviser who is a member of a professional body" | - |
| `s 21B(2) the first condition is satisfied` | ta-regulated-sector.l4:312 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The first condition is that the information or other matter disclosed came to the person making the disclosure" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21B(3) the second condition is satisfied` | ta-regulated-sector.l4:327 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The second condition is that the information or other matter" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21B(4) the third condition is satisfied` | ta-regulated-sector.l4:339 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The third condition is that the disclosure is made to a constable or a nominated officer as soon as is practicable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21B(1) the disclosure is not to be taken to breach any restriction on the disclosure of information` | ta-regulated-sector.l4:352 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A disclosure which satisfies the following three conditions is not to be taken to breach any restriction" (a disclosure that does not satisfy all three is outside the protection: a condition the text states is not met; marginal, fork F17) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21B(5) the disclosure is a disclosure to a nominated officer` | ta-regulated-sector.l4:367 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A disclosure to a nominated officer is a disclosure which—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21B(6) the business is a business in the regulated sector` | ta-regulated-sector.l4:375 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 21B(7) the person is a constable for the purposes of s 21B` | ta-regulated-sector.l4:386 | NOTHING (includes) | "The reference to a constable includes a reference to a National Crime Agency officer authorised" | - |
| `s 21C(1) the constable must pass the disclosure in full to an authorised National Crime Agency officer` | ta-regulated-sector.l4:399 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a disclosure is made under a provision of this Part to a constable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21C(2) the constable must pass the section 21 disclosure in full to an authorised National Crime Agency officer` | ta-regulated-sector.l4:419 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Where a disclosure is made under section 21 (cooperation with police) to a constable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `What must I tell and to whom` | ta-seat.l4:420 | NOTHING (points outside the text) | whether the information came in the course of a business in the regulated sector turns on Schedule 3A, which is not among the sources; s 19(1A) and s 21A(3) both turn on it | - |
| `By what day must the report be sent` | ta-seat.l4:508 | M2: a grant or prohibition limited by its own wording does not give a no | "by giving written notice" (s 21CC(8): the Act gives a constable the power to vary the 28 days by written notice and says nothing of any other notice, so the end date is not answered) | the case outside the limit is the text’s no: JUST FALSE |
| `Was my report sent in time` | ta-seat.l4:531 | M2: a grant or prohibition limited by its own wording does not give a no | "by giving written notice" (s 21CC(8): the Act says nothing of a variation that is not written, so whether the report is in time is not answered) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21D(2) the matter is within subsection (2)` | ta-tipping-off.l4:34 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "The matters are that the person or another person has made a disclosure under a provision of this Part" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21D(1) the person commits an offence by tipping off` | ta-tipping-off.l4:46 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21D(3) the person commits an offence by disclosing an investigation` | ta-tipping-off.l4:66 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person commits an offence if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21E(1) the person does not commit an offence under s 21D` | ta-tipping-off.l4:107 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "does not commit an offence under section 21D if the disclosure is to an employee, officer or partner of the same undertaking" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` | ta-tipping-off.l4:124 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under section 21D in respect of a disclosure by a credit institution or a financial institution if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21E(3) the institutions belong to the same group` | ta-tipping-off.l4:132 | NOTHING (points outside the text) | "“group” has the same meaning as in Directive 2002/87/EC", which is not among the sources; with no answer from it, NOTHING | - |
| `s 21E(4) the adviser does not commit an offence under s 21D` | ta-tipping-off.l4:149 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A professional legal adviser or a relevant professional adviser does not commit an offence under section 21D if—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21F(1) this section applies to the disclosure` | ta-tipping-off.l4:169 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This section applies to a disclosure—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21G(1) the person does not commit an offence under s 21D` | ta-tipping-off.l4:217 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under section 21D if the disclosure is—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21G(2) the adviser does not commit an offence under s 21D` | ta-tipping-off.l4:234 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A professional legal adviser or a relevant professional adviser does not commit an offence under section 21D if the disclosure—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21G(3) the person does not commit an offence under s 21D(1)` | ta-tipping-off.l4:245 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under section 21D(1) if the person does not know or suspect that the disclosure is likely to have the effect" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21G(4) the person does not commit an offence under s 21D(3)` | ta-tipping-off.l4:256 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person does not commit an offence under section 21D(3) if the person does not know or suspect that the disclosure is likely to have the effect" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21H(1)(a) the business is a business in the regulated sector` | ta-tipping-off.l4:269 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 21H(1)(b) the body is a supervisory authority` | ta-tipping-off.l4:280 | NOTHING (points outside the text) | Schedule 3A decides what is a supervisory authority and is not among the sources; with no answer from it, NOTHING | - |
| `s 21H(2) the undertaking is a credit institution` | ta-tipping-off.l4:289 | NOTHING (points outside the text) | "“credit institution” has the same meaning as in Schedule 3A", which is not among the sources; with no answer from it, NOTHING | - |
| `s 21H(2) the undertaking is a financial institution` | ta-tipping-off.l4:300 | a definition that says it means (not marginal) | "“financial institution” means an undertaking that carries on a business in the regulated sector by virtue of any of paragraphs (b) to (i) of paragraph 1(1) of that Schedule." | - |
| `s 21H(3) the disclosure counts as a disclosure by or to the institution` | ta-tipping-off.l4:310 | NOTHING (includes) | "References in those sections to a disclosure by or to a credit institution or a financial institution include disclosure by or to an employee, officer or partner of the institution acting on its behalf." | - |
| `s 21H(4) the country or territory imposes equivalent money laundering requirements` | ta-tipping-off.l4:320 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a country or territory imposes “equivalent money laundering requirements” if it imposes requirements equivalent to those laid down in Directive 2015/849/EU" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21H(5) the person is a relevant professional adviser` | ta-tipping-off.l4:336 | a definition that says it means (not marginal) | "“relevant professional adviser” means an accountant, auditor or tax adviser who is a member of a professional body" | - |
| `s 21CA(2) condition 1 is met` | ta-voluntary-disclosure.l4:31 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 1 is that—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(3) condition 2 is met` | ta-voluntary-disclosure.l4:45 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 2 is that—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(4) condition 3 is met` | ta-voluntary-disclosure.l4:56 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 3 is that, before A makes the disclosure, the required notification has been made to a constable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(5) condition 4 is met` | ta-voluntary-disclosure.l4:70 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 4 is that A is satisfied that the disclosure of the information will or may assist" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(6) condition 5 is met` | ta-voluntary-disclosure.l4:81 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 5 is that, before making the disclosure request, the person making the request" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(7) condition 5 does not apply` | ta-voluntary-disclosure.l4:92 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Condition 5 does not apply where the disclosure request concerned is made by a constable." (a failed \"where\": fork F8 reads it as the only case in which condition 5 is not applicable) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(1) A may disclose information to one or more other persons` | ta-voluntary-disclosure.l4:114 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A person (A) may disclose information to one or more other persons if—" (a permission given "if" conditions 1 to 4 and, where applicable, 5 are met; ruling of 2026-11-05 on "if" conditions) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CA(8) the person may disclose information to A for the purposes of making a disclosure request` | ta-voluntary-disclosure.l4:125 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "if, and to the extent that, the person has reason to believe" (the "if" is not met; the extent of the permission is not worked out here) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(1) the disclosure request has the content the section requires` | ta-voluntary-disclosure.l4:147 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A disclosure request must—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(2) subsections (3) and (4) apply to the request` | ta-voluntary-disclosure.l4:158 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsections (3) and (4) apply where the disclosure request is made by a person mentioned in section 21CA(3)(b)." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(3) the request states the grounds or other information` | ta-voluntary-disclosure.l4:169 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If the request states that it is made in connection with a suspicion that a person is involved in the commission of a terrorist financing offence, the request must also—" (the "if" is not met: ruling of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(3) the request states the grounds or other information` | ta-voluntary-disclosure.l4:172 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the request must also— (a) set out the grounds for the suspicion, or (b) provide such other information" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(4) the request provides the other information` | ta-voluntary-disclosure.l4:184 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If the request states that it is made in connection with the identification of terrorist property or of its movement or use, the request must also provide" (the "if" is not met: ruling of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(4) the request provides the other information` | ta-voluntary-disclosure.l4:187 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the request must also provide such other information as the person making the request thinks appropriate" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(5) the required notification is made by the person the subsection names` | ta-voluntary-disclosure.l4:202 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "in the case of a disclosure request made by a constable, by the person who is to disclose information under section 21CA" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(5) the required notification is made by the person the subsection names` | ta-voluntary-disclosure.l4:205 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "in the case of a disclosure request made by a person mentioned in section 21CA(3)(b), by the person who made the request" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(6) the notification has the content the subsection requires` | ta-voluntary-disclosure.l4:216 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the required notification must state that information is to be disclosed under section 21CA" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(7) the notification has the content the subsection requires` | ta-voluntary-disclosure.l4:238 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the required notification must— (a) state that a disclosure request has been made; (b) specify the person to whom the request was made" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CB(8) the notification has the content the subsection requires` | ta-voluntary-disclosure.l4:256 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "A notification for the purposes of condition 5 in subsection (6) of section 21CA must—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(1) section 21CC applies` | ta-voluntary-disclosure.l4:275 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "This section applies if in any proceedings a question arises as to whether the required disclosure has been made" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(2) the required notification satisfies the requirement to make the required disclosure` | ta-voluntary-disclosure.l4:288 | M2: a grant or prohibition limited by its own wording does not give a no | "The making of a required notification in good faith is to be treated as satisfying any requirement" (a notification not made in good faith is not said to fail to satisfy it) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CC(3) the joint disclosure report satisfies the requirement to make the required disclosure` | ta-voluntary-disclosure.l4:301 | M2: a grant or prohibition limited by its own wording does not give a no | "The making of a joint disclosure report in good faith is to be treated as satisfying any requirement" (a report not made in good faith is not said to fail to satisfy it) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CC(5) the report has the content required for a suspicion` | ta-voluntary-disclosure.l4:340 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the requirements as to content are that the report must—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(6) the report has the content required for terrorist property` | ta-voluntary-disclosure.l4:358 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "the requirements as to content are that the report must—" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(8) the notice varies the period of 28 days` | ta-voluntary-disclosure.l4:371 | M2: a grant or prohibition limited by its own wording does not give a no | "A constable may vary the period of 28 days (whether by lengthening or shortening it) by giving written notice to the person who made the required notification." (a notice by another person, or one that is not written, or one given to someone else, is outside the grant; the text does not say it fails to vary the period: fork F10, scope limit with no "only", ruling of 2026-11-05 (c)) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CC(7) the last day of the applicable period` | ta-voluntary-disclosure.l4:395 | NOTHING (points outside the text) | "whatever period may be specified by the constable when making the request" (the constable's period is not in the Act; with none given, NOTHING) | - |
| `s 21CC(4)(d) the report is sent to the constable before the end of the applicable period` | ta-voluntary-disclosure.l4:415 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "is sent to the constable before the end of the applicable period" (fork F9: the last day counts as inside the period) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(4)(d) the report is sent to the constable before the end of the applicable period` | ta-voluntary-disclosure.l4:417 | NOTHING (points outside the text) | the period is the constable's, so with none given the text does not answer | - |
| `s 21CC(9) the joint disclosure report is approved and signed as required` | ta-voluntary-disclosure.l4:431 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If there is no nominated officer the report must be approved and signed by another senior officer." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CC(10) the person counts as A, B or C` | ta-voluntary-disclosure.l4:445 | NOTHING (includes) | "References in this section to A, B or C include—" | - |
| `s 21CD(1) subsections (2) and (3) apply` | ta-voluntary-disclosure.l4:457 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsections (2) and (3) apply in a case where the required notification is made by A" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(2) section 21CC(2) covers the matter, where A made the notification` | ta-voluntary-disclosure.l4:471 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "has effect in the case of A, B or C only so far as relating to" (a matter outside what the subsection names is outside its effect: "only so far as", rulings of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(3) section 21CC(2) removes the requirement for the matter, where A made the notification` | ta-voluntary-disclosure.l4:480 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "section 21CC(2) does not remove any requirement to make the required disclosure in relation to anything known, suspected or believed that does not result only from the making of the disclosure request" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(4) subsections (5) to (8) apply` | ta-voluntary-disclosure.l4:492 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsections (5) to (8) apply in a case where the required notification is made by B" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(5) section 21CC(2) covers the matter for A or C, where B made the notification` | ta-voluntary-disclosure.l4:506 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "has effect in the case of A or C only so far as relating to" (a matter outside what the subsection names is outside its effect: "only so far as", rulings of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(6) section 21CC(2) removes the requirement for the matter, where B made the notification` | ta-voluntary-disclosure.l4:515 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "section 21CC(2) does not remove any requirement to make the required disclosure in relation to anything known, suspected or believed that does not result only from the making of the notification" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(7) section 21CC(2) covers the matter for B` | ta-voluntary-disclosure.l4:531 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "has effect in the case of B only so far as relating to" (a matter outside what the subsection names is outside its effect: "only so far as", rulings of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(8)(a) section 21CC(2) covers the requirement` | ta-voluntary-disclosure.l4:545 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "has effect only so far as relating to any requirement to make the required disclosure that would have otherwise arisen within that period" (a matter outside what the subsection names is outside its effect: "only so far as", rulings of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(8)(b) section 21CC(2) removes the requirement` | ta-voluntary-disclosure.l4:558 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "does not remove a requirement to make the required disclosure so far as arising after the end of that period" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(9) the person who made the required notification must notify a constable that a report is not being made` | ta-voluntary-disclosure.l4:573 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "If a joint disclosure report is not made before the end of the applicable period, the person who made the required notification must notify a constable" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(10) section 21CC(3) covers the matter` | ta-voluntary-disclosure.l4:596 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Section 21CC(3) has effect only so far as relating to" (a matter outside what the subsection names is outside its effect: "only so far as", rulings of 2026-11-05) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CD(11) the term has the same meaning as in s 21CC` | ta-voluntary-disclosure.l4:606 | M2: a grant or prohibition limited by its own wording does not give a no | "Terms used in this section have the same meanings as in section 21CC." (terms elsewhere are not touched) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CE(1) the relevant disclosure does not breach an obligation of confidence or any other restriction` | ta-voluntary-disclosure.l4:623 | M2: a grant or prohibition limited by its own wording does not give a no | "A relevant disclosure made in good faith does not breach" (a disclosure not made in good faith is not said to breach anything) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CE(2) the relevant disclosure is barred from including the information` | ta-voluntary-disclosure.l4:635 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "unless that agency consents to the disclosure" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(2) the relevant disclosure is barred from including the information` | ta-voluntary-disclosure.l4:638 | M2: a grant or prohibition limited by its own wording does not give a no | "may not include information obtained from a UK law enforcement agency" (information from elsewhere is outside the bar) | the case outside the limit is the text’s no: JUST FALSE |
| `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` | ta-voluntary-disclosure.l4:660 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "In a case where a person is acting on behalf of another (“the undertaking”) as a nominated officer" (the "case where" is not met: ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` | ta-voluntary-disclosure.l4:663 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a relevant disclosure by the undertaking must be made by the nominated officer on behalf of the undertaking" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` | ta-voluntary-disclosure.l4:677 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "In a case where a person is acting on behalf of another (“the undertaking”) as a nominated officer" (the "case where" is not met: ruling of 2026-11-05, (b)) | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` | ta-voluntary-disclosure.l4:680 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "a relevant disclosure to the undertaking must be made to that officer" | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(4) subsection (1) applies whether or not the conditions were met` | ta-voluntary-disclosure.l4:692 | M1: a failed “if”, “where”, “is that” or “must—” condition, or a flat negative, counts as the text’s no | "Subsection (1) applies whether or not the conditions in section 21CA were met in respect of the disclosure if the person making the disclosure did so in the reasonable belief that the conditions were met." | the text is silent on the case that fails the condition: NOTHING-kind (silent) |
| `s 21CE(5) the disclosure is a relevant disclosure` | ta-voluntary-disclosure.l4:705 | a definition that says it means (not marginal) | "“relevant disclosure” means any disclosure made in compliance, or intended compliance, with section 21CA" | - |
| `s 21CE(5) the body is a UK law enforcement agency` | ta-voluntary-disclosure.l4:722 | a definition that says it means (not marginal) | "“UK law enforcement agency” means—" | - |
| `s 21CF(2) the person is a constable for the purposes of ss 21CA to 21CE` | ta-voluntary-disclosure.l4:736 | NOTHING (includes) | "References to a constable include references to a National Crime Agency officer authorised" | - |
| `s 21CF(3) the business is a business in the regulated sector` | ta-voluntary-disclosure.l4:744 | NOTHING (points outside the text) | Schedule 3A decides what is a business in the regulated sector and is not among the sources; with no answer from it, NOTHING | - |
| `s 21CF(4) the request is a disclosure request` | ta-voluntary-disclosure.l4:754 | a definition that says it means (not marginal) | "“Disclosure request” means a request made for the purposes of condition 2 in section 21CA(3)." | - |
| `s 21CF(5) the person is a nominated officer` | ta-voluntary-disclosure.l4:764 | a definition that says it means (not marginal) | "“Nominated officer” means a person nominated to receive disclosures under section 21A." | - |
| `s 21CF(6) the person is a relevant undertaking` | ta-voluntary-disclosure.l4:783 | a definition that says it means (not marginal) | "“Relevant undertaking” means any of the following—" | - |
| `s 21CF(7) the disclosure is a required disclosure` | ta-voluntary-disclosure.l4:798 | a definition that says it means (not marginal) | "“Required disclosure” means a disclosure that is made—" | - |
| `s 21CF(8) the notification is a required notification` | ta-voluntary-disclosure.l4:808 | a definition that says it means (not marginal) | "“Required notification” means a notification made for the purposes of condition 3 in section 21CA(4)." | - |
| `s 21CF(9)(a) the undertaking is a credit institution` | ta-voluntary-disclosure.l4:819 | NOTHING (points outside the text) | "“credit institution” has the same meaning as in Schedule 3A", which is not among the sources; with no answer from it, NOTHING | - |
| `s 21CF(9)(b) the undertaking is a financial institution` | ta-voluntary-disclosure.l4:832 | a definition that says it means (not marginal) | "“financial institution” means an undertaking that carries on a business in the regulated sector by virtue of any of paragraphs (b) to (i) of paragraph 1(1) of that Schedule" | - |
| `s 21CF(10) the offence is a terrorist financing offence` | ta-voluntary-disclosure.l4:844 | a definition that says it means (not marginal) | "“Terrorist financing offence” means an offence under any of sections 15 to 18." | - |

<!-- MARGINAL:END -->

## Jural relations

Hohfeld's correlatives: a right (claim) is the other party's duty; a privilege (liberty) is the other party's no-right; a power is the other party's liability (being subject to the power); an immunity is the other party's disability.
One row per provision that creates a relation; a definition, a counting rule or a rule of reading is listed once as `none`.
Checked by script on 2026-11-05: every section row and every subsection row of the coverage table has a row here (s 21H(1) through its two paragraphs).
Following ruling N2, a flat negative is the text's no in the person-facing answer, a prohibition (`SHANT`) is derived from that answer where the text names its bearer, and the Hohfeld kind is recorded here and not typed into any answer.

<!-- JURAL:BEGIN -->

| provision | holder of the right, privilege, power or immunity | kind | bearer of the correlative duty, no-right, liability or disability | correlative | L4 rule |
|---|---|---|---|---|---|
| s 14(1) | none (a definition of terrorist property) | none | none | none | s 14(1) |
| s 14(2) | none (an inclusion rule for terrorist property) | none | none | none | s 14(2)(a) ;; s 14(2)(b) |
| s 15(1) | the State (prosecuting authority) | power (to prosecute and punish) | a person who invites another to provide money or other property intending it, or having reasonable cause to suspect it, to be used for the purposes of terrorism | liability to be prosecuted and punished | s 15(1) |
| s 15(2) | the State (prosecuting authority) | power (to prosecute and punish) | a person who receives money or other property intending it, or having reasonable cause to suspect it, to be used for the purposes of terrorism | liability to be prosecuted and punished | s 15(2) |
| s 15(3) | the State (prosecuting authority) | power (to prosecute and punish) | a person who provides money or other property knowing or having reasonable cause to suspect it will or may be used for the purposes of terrorism | liability to be prosecuted and punished | s 15(3) |
| s 15(4) | none (a meaning of 'provide') | none | none | none | s 15(4) |
| s 16(1) | the State (prosecuting authority) | power (to prosecute and punish) | a person who uses money or other property for the purposes of terrorism | liability to be prosecuted and punished | s 16(1) |
| s 16(2) | the State (prosecuting authority) | power (to prosecute and punish) | a person who possesses money or other property intending it, or having reasonable cause to suspect it, to be used for the purposes of terrorism | liability to be prosecuted and punished | s 16(2) |
| s 17 | the State (prosecuting authority) | power (to prosecute and punish) | a person who enters into or becomes concerned in an arrangement by which money or other property is made available, knowing or having reasonable cause to suspect it may be used for the purposes of terrorism | liability to be prosecuted and punished | s 17 |
| s 17A(1) | the State (prosecuting authority) | power (to prosecute and punish) | an insurer who reimburses a payment made in response to a terrorist demand, knowing or having reasonable cause to suspect it was | liability to be prosecuted and punished | s 17A(1) |
| s 17A(2) | the State (prosecuting authority) | power (to prosecute and punish) | an officer of a body corporate whose offence is proved to have been committed with the officer's consent, connivance or neglect | liability to be prosecuted and punished | s 17A(2) |
| s 17A(3) | none (a meaning of 'director') | none | none | none | s 17A(3) |
| s 17A(4) | the State (prosecuting authority) | power (to prosecute and punish) | a partner of a Scottish partnership whose offence is proved to have been committed with the partner's consent, connivance or neglect | liability to be prosecuted and punished | s 17A(4) |
| s 17A(5) | none (a meaning of 'insurance contract') | none | none | none | s 17A(5) |
| s 18(1) | the State (prosecuting authority) | power (to prosecute and punish) | a person who enters into or becomes concerned in an arrangement that facilitates the retention or control of terrorist property | liability to be prosecuted and punished | s 18(1) |
| s 18(2) | the person charged | immunity (a defence the person must prove) | the State (prosecuting authority) | disability (cannot secure a conviction against a person who proves it) | s 18(2) |
| s 19(1) | none (a scope rule: when s 19 applies) | none | none | none | s 19(1) |
| s 19(1A) | a person who learns the information in the course of a business in the regulated sector | immunity | the State (prosecuting authority) and constables | disability (cannot hold the person liable or the disclosure a breach) | s 19(1A) |
| s 19(2) | a constable (acting for the State) | claim-right | a person who believes or suspects, from information obtained in trade, profession, business or employment, that another has committed an offence under ss 15 to 18; the duty is to disclose as soon as reasonably practicable | duty | s 19(2) |
| s 19(3) | the person charged with an offence under s 19(2) | immunity (a defence the person must prove) | the State (prosecuting authority) | disability (cannot secure a conviction against a person who proves it) | s 19(3) |
| s 19(4) | the employee who disclosed under the employer's procedure | immunity (a defence the person must prove) | the State (prosecuting authority) | disability (cannot secure a conviction against a person who proves it) | s 19(4) |
| s 19(5) | a professional legal adviser | immunity | constables | disability (cannot hold the person liable or the disclosure a breach) | s 19(5) |
| s 19(6) | none (a meaning of 'privileged circumstances') | none | none | none | s 19(6) |
| s 19(7) | none (a deeming rule for acts abroad) | none | none | none | s 19(7) |
| s 19(7A) | none (a pointer to Schedule 3A) | none | none | none | s 19(7A) |
| s 19(7B) | none (a meaning of 'constable') | none | none | none | s 19(7B) |
| s 19(8) | the State (prosecuting authority) | power (to prosecute and punish) | a person convicted of an offence under s 19(2) | liability to be prosecuted and punished | s 19(8) |
| s 20(1) | a person who has information about a suspected offence under ss 15 to 18 or about terrorist property | privilege (liberty to disclose) | the State (prosecuting authority) and anyone owed confidence | no-right (cannot require the person not to, or complain of it) | s 20(1) |
| s 20(2) | a person who believes or suspects an offence under ss 15 to 18 | privilege (liberty to disclose) | the State (prosecuting authority) | no-right (cannot require the person not to, or complain of it) | s 20(2) |
| s 20(3) | a person who discloses to a constable | immunity | a person owed a duty of confidence or other restriction | disability (cannot hold the person liable or the disclosure a breach) | s 20(3) |
| s 20(4) | none (a deeming rule: the employer's procedure counts as a disclosure to a constable) | none | none | none | s 20(4) |
| s 20(5) | none (a meaning of 'constable') | none | none | none | s 20(5) |
| s 21(1) | a person who acts with the express consent of a constable | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21(1) |
| s 21(2) | a person who discloses before involvement, or after it on the stated conditions | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21(2) |
| s 21(3) | none (a condition of the s 21(2) immunity) | none | none | none | s 21(3) |
| s 21(4) | none (a condition of the s 21(2) immunity) | none | none | none | s 21(4) |
| s 21(5) | the person charged with an offence under ss 15(2), (3) and 16 to 18 | immunity (a defence the person must prove) | the State (prosecuting authority) | disability (cannot secure a conviction against a person who proves it) | s 21(5) |
| s 21(6) | none (a deeming rule: the employer's procedure counts as a disclosure to a constable) | none | none | none | s 21(6) |
| s 21(7) | none (a meaning of 'transaction or arrangement') | none | none | none | s 21(7) |
| s 21ZA(1) | a person who disclosed to an authorised officer before becoming involved and had consent | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21ZA(1) |
| s 21ZA(2) | a person who disclosed and received no notice of refusal before the end of the notice period | immunity | the State (prosecuting authority) and the authorised officer | disability (cannot hold the person liable or the disclosure a breach) | s 21ZA(2) |
| s 21ZA(3) | none (a counting rule for the notice period) | none | none | none | s 21ZA(3) |
| s 21ZA(4) | none (a meaning of 'working day') | none | none | none | s 21ZA(4) |
| s 21ZA(5) | none (a meaning of 'authorised officer') | none | none | none | s 21ZA(5) |
| s 21ZA(6) | none (a meaning of 'transaction or arrangement') | none | none | none | s 21ZA(6) |
| s 21ZB(1) | a person who disclosed after becoming involved on the stated conditions | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21ZB(1) |
| s 21ZB(2) | none (a condition of the s 21ZB(1) immunity) | none | none | none | s 21ZB(2) |
| s 21ZB(3) | none (a condition of the s 21ZB(1) immunity) | none | none | none | s 21ZB(3) |
| s 21ZB(4) | none (a meaning of 'authorised officer') | none | none | none | s 21ZB(4) |
| s 21ZB(5) | none (a meaning of 'transaction or arrangement') | none | none | none | s 21ZB(5) |
| s 21ZC | the person charged with an offence under ss 15 to 18 | immunity (a defence the person must prove) | the State (prosecuting authority) | disability (cannot secure a conviction against a person who proves it) | s 21ZC |
| s 22 | the State (prosecuting authority) | power (to prosecute and punish) | a person guilty of an offence under ss 15 to 18, as to the penalty | liability to be prosecuted and punished | s 22 |
| s 22A | none (a meaning of 'employment' and 'employer') | none | none | none | s 22A(a) ;; s 22A(b) |
| s 21A(1) | the State (prosecuting authority) | power (to prosecute and punish) | a person in the regulated sector who fails to disclose a known or suspected offence under ss 15 to 18 | liability to be prosecuted and punished | s 21A(1) |
| s 21A(2) | none (the first condition of the s 21A offence) | none | none | none | s 21A(2) |
| s 21A(3) | none (the second condition of the s 21A offence) | none | none | none | s 21A(3) |
| s 21A(4) | none (the third condition of the s 21A offence) | none | none | none | s 21A(4) |
| s 21A(5) | a person with a reasonable excuse, a professional adviser holding privileged information, or an assistant to such an adviser | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21A(5) |
| s 21A(5A) | none (a condition of the s 21A(5) exception) | none | none | none | s 21A(5A) |
| s 21A(6) | a person charged under s 21A | claim-right | the court, which must consider whether the person followed relevant guidance | duty | s 21A(6) |
| s 21A(7) | none (a deeming rule: a disclosure to a nominated officer) | none | none | none | s 21A(7) |
| s 21A(8) | none (a meaning of 'privileged circumstances') | none | none | none | s 21A(8) |
| s 21A(9) | none (an exclusion from 'privileged circumstances') | none | none | none | s 21A(9) |
| s 21A(10) | none (a pointer to Schedule 3A) | none | none | none | s 21A(10)(a) ;; s 21A(10)(b) |
| s 21A(11) | none (a deeming rule for acts abroad) | none | none | none | s 21A(11) |
| s 21A(12) | the State (prosecuting authority) | power (to prosecute and punish) | a person convicted of an offence under s 21A, as to the penalty | liability to be prosecuted and punished | s 21A(12) |
| s 21A(13) | none (a meaning of 'appropriate body') | none | none | none | s 21A(13) |
| s 21A(14) | none (a meaning of 'constable') | none | none | none | s 21A(14) |
| s 21A(15) | none (a meaning of 'relevant professional adviser') | none | none | none | s 21A(15) |
| s 21B(1) | a person in the regulated sector who makes a protected disclosure | immunity | a person owed a duty of confidence or other restriction | disability (cannot hold the person liable or the disclosure a breach) | s 21B(1) |
| s 21B(2) | none (a condition of the s 21B(1) immunity) | none | none | none | s 21B(2) |
| s 21B(3) | none (a condition of the s 21B(1) immunity) | none | none | none | s 21B(3) |
| s 21B(4) | none (a condition of the s 21B(1) immunity) | none | none | none | s 21B(4) |
| s 21B(5) | none (a deeming rule: a disclosure to a nominated officer) | none | none | none | s 21B(5) |
| s 21B(6) | none (a pointer to Schedule 3A) | none | none | none | s 21B(6) |
| s 21B(7) | none (a meaning of 'constable') | none | none | none | s 21B(7) |
| s 21C(1) | the National Crime Agency | claim-right | a constable who receives a disclosure under this Part | duty | s 21C(1) |
| s 21C(2) | the National Crime Agency | claim-right | a constable who receives a section 21 disclosure | duty | s 21C(2) |
| s 21CA(1) | a business in the regulated sector that is a relevant undertaking (A) | privilege (liberty to disclose) | the State, the person asked and anyone owed confidence | no-right (cannot require the person not to, or complain of it) | s 21CA(1) |
| s 21CA(2) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(2) |
| s 21CA(3) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(3) |
| s 21CA(4) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(4) |
| s 21CA(5) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(5) |
| s 21CA(6) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(6) |
| s 21CA(7) | none (a condition of the s 21CA(1) privilege) | none | none | none | s 21CA(7) |
| s 21CA(8) | a person who has reason to believe A holds information that will or may assist | privilege (liberty to disclose) | the State (prosecuting authority) and anyone owed confidence | no-right (cannot require the person not to, or complain of it) | s 21CA(8) |
| s 21CB(1) | the person asked to disclose (A) | claim-right | the person making a disclosure request, who must include the stated content | duty | s 21CB(1) |
| s 21CB(2) | the person asked to disclose (A) | claim-right | a requester under s 21CA(3)(b), as to the extra content in (3) and (4) | duty | s 21CB(2) |
| s 21CB(3) | the person asked to disclose (A) | claim-right | a requester stating a suspicion | duty | s 21CB(3) |
| s 21CB(4) | the person asked to disclose (A) | claim-right | a requester stating a property connection | duty | s 21CB(4) |
| s 21CB(5) | a constable | claim-right | the person who must make the required notification (A for a constable's request, B for another's) | duty | s 21CB(5) |
| s 21CB(6) | a constable | claim-right | A, who must state that information is to be disclosed under s 21CA | duty | s 21CB(6) |
| s 21CB(7) | a constable | claim-right | B, who must give the stated content | duty | s 21CB(7) |
| s 21CB(8) | a constable | claim-right | a requester giving advance notice (condition 5) | duty | s 21CB(8) |
| s 21CC(1) | none (a scope rule: when s 21CC applies) | none | none | none | s 21CC(1) |
| s 21CC(2) | A, B and C who make a required notification in good faith | immunity | a constable and the State | disability (cannot hold the person liable or the disclosure a breach) | s 21CC(2) |
| s 21CC(3) | the persons who jointly make a report in good faith | immunity | a constable and the State | disability (cannot hold the person liable or the disclosure a breach) | s 21CC(3) |
| s 21CC(4) | none (a meaning of 'joint disclosure report') | none | none | none | s 21CC(4) |
| s 21CC(5) | none (the content of a joint disclosure report) | none | none | none | s 21CC(5) |
| s 21CC(6) | none (the content of a joint disclosure report) | none | none | none | s 21CC(6) |
| s 21CC(7) | none (a counting rule for the applicable period) | none | none | none | s 21CC(7) |
| s 21CC(8) | a constable | power | the person who made the required notification (the 28 days may be varied by written notice) | liability (being subject to the power) | s 21CC(8) |
| s 21CC(9) | a constable | claim-right | the nominated officer of each person making the report, who must approve and sign it | duty | s 21CC(9) |
| s 21CC(10) | none (a meaning of 'A, B or C') | none | none | none | s 21CC(10) |
| s 21CD(1) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(1) |
| s 21CD(2) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(2) |
| s 21CD(3) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(3) |
| s 21CD(4) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(4) |
| s 21CD(5) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(5) |
| s 21CD(6) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(6) |
| s 21CD(7) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(7) |
| s 21CD(10) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(10) |
| s 21CD(11) | none (a limit on the s 21CC(2) or (3) immunity; it creates no relation of its own) | none | none | none | s 21CD(11) |
| s 21CD(8) | none (a limit on the s 21CC(2) immunity; it creates no relation of its own) | none | none | none | s 21CD(8)(a) ;; s 21CD(8)(b) |
| s 21CD(9) | a constable | claim-right | the person who made the required notification, who must notify that no report is being made | duty | s 21CD(9) |
| s 21CE(1) | a person making a relevant disclosure in good faith | immunity | a person owed a duty of confidence or other restriction | disability (cannot hold the person liable or the disclosure a breach) | s 21CE(1) |
| s 21CE(2) | a UK law enforcement agency | claim-right (that its information not be included without its consent) | the person making a relevant disclosure | duty (not to include it) | s 21CE(2) |
| s 21CE(3) | the undertaking | claim-right | the people disclosing for or to it, who must use the nominated officer | duty | s 21CE(3)(a) ;; s 21CE(3)(b) |
| s 21CE(4) | a person who made a disclosure in the reasonable belief that the conditions were met | immunity | a person owed a duty of confidence or other restriction | disability (cannot hold the person liable or the disclosure a breach) | s 21CE(4) |
| s 21CE(5) | none (meanings of 'relevant disclosure' and 'UK law enforcement agency') | none | none | none | s 21CE(5) |
| s 21CF(1) | none (the application of the interpretation section) | none | none | none | s 21CF(2) |
| s 21CF(2) | none (an interpretation rule) | none | none | none | s 21CF(2) |
| s 21CF(3) | none (an interpretation rule) | none | none | none | s 21CF(3) |
| s 21CF(4) | none (an interpretation rule) | none | none | none | s 21CF(4) |
| s 21CF(5) | none (an interpretation rule) | none | none | none | s 21CF(5) |
| s 21CF(6) | none (an interpretation rule) | none | none | none | s 21CF(6) |
| s 21CF(7) | none (an interpretation rule) | none | none | none | s 21CF(7) |
| s 21CF(8) | none (an interpretation rule) | none | none | none | s 21CF(8) |
| s 21CF(10) | none (an interpretation rule) | none | none | none | s 21CF(10) |
| s 21CF(9) | none (an interpretation rule) | none | none | none | s 21CF(9)(a) ;; s 21CF(9)(b) |
| s 21D(1) | the State (prosecuting authority) | power (to prosecute and punish) | a person in the regulated sector who discloses a protected matter likely to prejudice an investigation | liability to be prosecuted and punished | s 21D(1) |
| s 21D(2) | none (a meaning of the protected matters) | none | none | none | s 21D(2) |
| s 21D(3) | the State (prosecuting authority) | power (to prosecute and punish) | a person in the regulated sector who discloses that an investigation is contemplated or under way, likely to prejudice it | liability to be prosecuted and punished | s 21D(3) |
| s 21D(4) | the State (prosecuting authority) | power (to prosecute and punish) | a person convicted of an offence under s 21D, as to the penalty | liability to be prosecuted and punished | s 21D(4) |
| s 21D(5) | none (a cross-reference: s 21D is subject to ss 21E to 21G) | none | none | none | s 21D(5) |
| s 21E(1) | an employee, officer or partner disclosing within the same undertaking | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21E(1) |
| s 21E(2) | a credit or financial institution disclosing within a group | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21E(2) |
| s 21E(3) | none (a pointer to Directive 2002/87/EC for 'group') | none | none | none | s 21E(3) |
| s 21E(4) | a professional adviser disclosing between undertakings under common ownership, management or control | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21E(4) |
| s 21F(1) | none (a scope rule: when s 21F applies) | none | none | none | s 21F(1) |
| s 21F(2) | an institution or adviser making a permitted disclosure to a peer | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21F(2) |
| s 21G(1) | a person disclosing to a supervisory authority, in good faith under s 21CA, or for the detection, investigation or prosecution of an offence | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21G(1) |
| s 21G(2) | a professional adviser dissuading a client | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21G(2) |
| s 21G(3) | a person who does not know or suspect that the disclosure is likely to prejudice an investigation | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21G(3) |
| s 21G(4) | a person who does not know or suspect that the disclosure is likely to prejudice the investigation | immunity | the State (prosecuting authority) | disability (cannot hold the person liable or the disclosure a breach) | s 21G(4) |
| s 21H(1)(a) | none (an interpretation rule) | none | none | none | s 21H(1)(a) |
| s 21H(1)(b) | none (an interpretation rule) | none | none | none | s 21H(1)(b) |
| s 21H(2) | none (an interpretation rule) | none | none | none | s 21H(2) |
| s 21H(3) | none (an interpretation rule) | none | none | none | s 21H(3) |
| s 21H(4) | none (an interpretation rule) | none | none | none | s 21H(4) |
| s 21H(5) | none (an interpretation rule) | none | none | none | s 21H(5) |
| s 22B(1) | a magistrates court or the sheriff, on a law enforcement officer's application | power | the respondent (a business in the regulated sector) | liability (being subject to the power) | s 22B(1) |
| s 22B(1A) | a magistrates court or the sheriff, on an NCA or procurator fiscal application | power | the respondent | liability (being subject to the power) | s 22B(1A) |
| s 22B(2) | the court | claim-right | the applicant, who must specify the information and the respondent | duty | s 22B(2) |
| s 22B(3) | the applicant authority | claim-right | the respondent, who must provide the information the order requires | duty | s 22B(3) |
| s 22B(4) | none (a condition for making an information order, or a meaning) | none | none | none | s 22B(4) |
| s 22B(5) | none (a condition for making an information order, or a meaning) | none | none | none | s 22B(5) |
| s 22B(6) | none (a condition for making an information order, or a meaning) | none | none | none | s 22B(6) |
| s 22B(6A) | none (a condition for making an information order, or a meaning) | none | none | none | s 22B(6A) |
| s 22B(6B) | none (a condition for making an information order, or a meaning) | none | none | none | s 22B(6B) |
| s 22B(7) | the respondent | claim-right | the court, which must specify how and by when the information is to be provided | duty | s 22B(7) |
| s 22B(8) | a magistrates court | power | a person who fails to comply with an information order | liability (being subject to the power) | s 22B(8) |
| s 22B(9) | none (a deeming rule: the sum is treated as adjudged by a conviction) | none | none | none | s 22B(9) |
| s 22B(10) | none (machinery: power to substitute the sum by regulations (inert, reason 2)) | none | none | none | s 22B(10) |
| s 22B(11) | none (machinery: annulment of the regulations (inert, reason 2)) | none | none | none | s 22B(11) |
| s 22B(12) | the respondent | claim-right | a constable, NCA officer or counter-terrorism financial investigator who may apply on Condition 1 or 2 only if senior or authorised | duty | s 22B(12) |
| s 22B(13) | none (a pointer to Schedule 3A) | none | none | none | s 22B(13) |
| s 22B(14) | none (definitions) | none | none | none | s 22B(14) |
| s 22C(1) | a person who made a statement in response to an information order | immunity | a prosecutor and the court (the statement may not be used against the person) | disability (cannot hold the person liable or the disclosure a breach) | s 22C(1) |
| s 22C(2) | none (limits on the s 22C(1) immunity) | none | none | none | s 22C(2) |
| s 22C(3) | a person whose statement is sought to be used under s 22C(2)(c) | immunity | a prosecutor, unless the person adduced evidence or asked a question | disability (cannot hold the person liable or the disclosure a breach) | s 22C(3) |
| s 22C(4) | none (a meaning of 'prosecution for perjury') | none | none | none | s 22C(4) |
| s 22D(1) | a party to the proceedings on the application | power | the relevant appeal court (an appeal lies) | liability (being subject to the power) | s 22D(1) |
| s 22D(2) | a party to the proceedings on the application | power | the relevant appeal court | liability (being subject to the power) | s 22D(2) |
| s 22D(3) | none (a rule naming the relevant appeal court) | none | none | none | s 22D(3) |
| s 22D(4) | the relevant appeal court | power | the parties to the appeal | liability (being subject to the power) | s 22D(4) |
| s 22E(1) | a respondent holding privileged information | immunity | the applicant authority | disability (cannot hold the person liable or the disclosure a breach) | s 22E(1) |
| s 22E(2) | none (a meaning of 'privileged information') | none | none | none | s 22E(2) |
| s 22E(3) | a person who provides information in pursuance of an information order | immunity | a person owed a duty of confidence or other restriction | disability (cannot hold the person liable or the disclosure a breach) | s 22E(3) |
| s 22E(4) | the court hearing the application | power | the parties (the hearing may be in private) | liability (being subject to the power) | s 22E(4) |
| s 22E(5) | none (machinery: rules of court (inert, reason 2)) | none | none | none | s 22E(5) |
| s 22F(1) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(1) |
| s 22F(2) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(2) |
| s 22F(3) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(3) |
| s 22F(4) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(4) |
| s 22F(5) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(5) |
| s 22F(6) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(6) |
| s 22F(9) | none (machinery for the code of practice (inert, reason 2)) | none | none | none | s 22F(9) |
| s 22F(7) | a person who fails to comply with a provision of the code | immunity | the State (prosecuting authority) and other parties (no liability of itself) | disability (cannot hold the person liable or the disclosure a breach) | s 22F(7) |
| s 22F(8) | a party to proceedings in which the code is relevant | claim-right | the court, which is to take the code into account | duty | s 22F(8) |
| s 22F(10) | none (a pointer to s 22B(14)) | none | none | none | s 22F(10) |
| s 23(1) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(1) |
| s 23(2) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(2) |
| s 23(3) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(3) |
| s 23(4) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(4) |
| s 23(5) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(5) |
| s 23(5A) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(5A) |
| s 23(6) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(6) |
| s 23(7) | the court that convicted the person | power | the convicted person (liability to forfeiture of the stated property) | liability (being subject to the power) | s 23(7) |
| s 23A(1) | the court that convicted the person | power | the convicted person | liability (being subject to the power) | s 23A(1) |
| s 23A(2) | none (a list of offences) | none | none | none | s 23A(2) |
| s 23A(3) | none (a rule extending s 23A to ancillary offences) | none | none | none | s 23A(3) |
| s 23A(4) | none (a rule extending s 23A to offences with a terrorist connection) | none | none | none | s 23A(4) |
| s 23A(5) | none (machinery: power to amend the list by order (inert, reason 2)) | none | none | none | s 23A(5) |
| s 23A(6) | a person who committed an offence before the order adding it came into force | immunity | the court (no forfeiture under s 23A on that ground) | disability (cannot hold the person liable or the disclosure a breach) | s 23A(6) |
| s 23B(1) | a person, other than the convicted person, who claims to be the owner or otherwise interested | claim-right | the court, which must give an opportunity to be heard | duty | s 23B(1) |
| s 23B(2) | the convicted person | claim-right | the court, which shall have regard to the value of the property and the effects of the order | duty | s 23B(2) |
| s 23B(3) | an accused in Scotland | immunity | a Scottish court (no order except on the prosecutor's application at the stated time) | disability (cannot hold the person liable or the disclosure a breach) | s 23B(3) |
| s 23B(4) | none (a pointer to Schedule 4) | none | none | none | s 23B(4) |

<!-- JURAL:END -->

## Coverage table

Built from the text by `coverage.py` (one row per heading, section, subsection, paragraph, sub-paragraph, defined term and table row), from the label-to-disposition map `coverage-map.tsv`; `python3 -I coverage.py <source> --audit --names` checks that every non-blank line is in exactly one row and that every encoded rule named in the map exists in a module and is asserted.
Run it with the source path as the first argument; `--notes NOTES.md` regenerates this table, the marginal-readings table and the jural-relations table in this file.

<!-- COVERAGE:BEGIN -->

Counts, from `coverage.py --audit`: text lines: 612 (non-blank 612); rows: 615; lines owned by exactly one row: 612; encoded 548, inert 22, fork 37, repealed 8, deferred 0; inert by reason 1: 6, 2: 16.

| text lines | row | kind | disposition | where |
|---|---|---|---|---|
| 1 | heading: Part III — Terrorist Property | heading | inert | reason 1: heading |
| 2 | heading: Interpretation | heading | inert | reason 1: heading |
| 3 | s 14 | section | encoded | `s 14(1) the property is terrorist property` ; `s 14(2)(a) the property is proceeds of the act` ; `s 14(2)(b) the property is among the organisation's resources` |
| 4 | s 14(1) | subsection | fork | F1 ; `s 14(1) the property is terrorist property` |
| 4 | s 14(1) term “terrorist property” | term | fork | F1 ; `s 14(1) the property is terrorist property` |
| 5 | s 14(1)(a) | paragraph | fork | F1 ; `s 14(1)(a) the property is likely to be used for the purposes of terrorism, or is a proscribed organisation's resources` ; `s 14(2)(b) the property is among the organisation's resources` |
| 6 | s 14(1)(b) | paragraph | fork | F1 ; `s 14(1)(b) the property is proceeds of the commission of acts of terrorism` ; `s 14(2)(a) the property is proceeds of the act` |
| 7 | s 14(1)(c) | paragraph | fork | F1 ; `s 14(1)(c) the property is proceeds of acts carried out for the purposes of terrorism` ; `s 14(2)(a) the property is proceeds of the act` |
| 8 | s 14(2) | subsection | encoded | `s 14(2)(a) the property is proceeds of the act` ; `s 14(2)(b) the property is among the organisation's resources` |
| 9 | s 14(2)(a) | paragraph | encoded | `s 14(2)(a) the property is proceeds of the act` |
| 10 | s 14(2)(b) | paragraph | encoded | `s 14(2)(b) the property is among the organisation's resources` |
| 11 | heading: Offences | heading | inert | reason 1: heading |
| 12 | s 15 | section | encoded | `s 15(1) the person commits an offence by inviting another to provide money or other property` ; `s 15(2) the person commits an offence by receiving money or other property` ; `s 15(3) the person commits an offence by providing money or other property` ; `s 15(4) the person provides money or other property` |
| 13 | s 15(1) | subsection | encoded | `s 15(1) the person commits an offence by inviting another to provide money or other property` |
| 14 | s 15(1)(a) | paragraph | encoded | `s 15(1) the person commits an offence by inviting another to provide money or other property` |
| 15 | s 15(1)(b) | paragraph | encoded | `s 15(1) the person commits an offence by inviting another to provide money or other property` |
| 16 | s 15(2) | subsection | encoded | `s 15(2) the person commits an offence by receiving money or other property` |
| 17 | s 15(2)(a) | paragraph | encoded | `s 15(2) the person commits an offence by receiving money or other property` |
| 18 | s 15(2)(b) | paragraph | encoded | `s 15(2) the person commits an offence by receiving money or other property` |
| 19 | s 15(3) | subsection | encoded | `s 15(3) the person commits an offence by providing money or other property` |
| 20 | s 15(3)(a) | paragraph | encoded | `s 15(3) the person commits an offence by providing money or other property` |
| 21 | s 15(3)(b) | paragraph | encoded | `s 15(3) the person commits an offence by providing money or other property` |
| 22 | s 15(4) | subsection | encoded | `s 15(4) the person provides money or other property` |
| 23 | s 16 | section | encoded | `s 16(1) the person commits an offence by using money or other property for the purposes of terrorism` ; `s 16(2) the person commits an offence by possessing money or other property` |
| 24 | s 16(1) | subsection | encoded | `s 16(1) the person commits an offence by using money or other property for the purposes of terrorism` |
| 25 | s 16(2) | subsection | encoded | `s 16(2) the person commits an offence by possessing money or other property` |
| 26 | s 16(2)(a) | paragraph | encoded | `s 16(2) the person commits an offence by possessing money or other property` |
| 27 | s 16(2)(b) | paragraph | encoded | `s 16(2) the person commits an offence by possessing money or other property` |
| 28-29 | s 17 | section | encoded | `s 17 the person commits an offence by a funding arrangement` |
| 30 | s 17(a) | paragraph | encoded | `s 17 the person commits an offence by a funding arrangement` |
| 31 | s 17(b) | paragraph | encoded | `s 17 the person commits an offence by a funding arrangement` |
| 32 | s 17A | section | encoded | `s 17A(1) the insurer commits an offence by paying under the contract` ; `s 17A(2) the officer is guilty of the offence as well as the body corporate` ; `s 17A(3) the person is the body corporate's director for the purposes of s 17A(2)` ; `s 17A(4) the partner is guilty of the offence as well as the partnership` ; `s 17A(5) the contract is an insurance contract` |
| 33 | s 17A(1) | subsection | encoded | `s 17A(1) the insurer commits an offence by paying under the contract` |
| 34 | s 17A(1)(a) | paragraph | encoded | `s 17A(1) the insurer commits an offence by paying under the contract` |
| 35 | s 17A(1)(b) | paragraph | encoded | `s 17A(1) the insurer commits an offence by paying under the contract` |
| 36 | s 17A(1)(c) | paragraph | encoded | `s 17A(1) the insurer commits an offence by paying under the contract` |
| 37 | s 17A(2) | subsection | encoded | `s 17A(2) the officer is guilty of the offence as well as the body corporate` |
| 38 | s 17A(2)(a) | paragraph | encoded | `s 17A(2) the officer is guilty of the offence as well as the body corporate` |
| 39-40 | s 17A(2)(b) | paragraph | encoded | `s 17A(2) the officer is guilty of the offence as well as the body corporate` |
| 41 | s 17A(3) | subsection | encoded | `s 17A(3) the person is the body corporate's director for the purposes of s 17A(2)` |
| 42 | s 17A(4) | subsection | encoded | `s 17A(4) the partner is guilty of the offence as well as the partnership` |
| 43 | s 17A(4)(a) | paragraph | encoded | `s 17A(4) the partner is guilty of the offence as well as the partnership` |
| 44-45 | s 17A(4)(b) | paragraph | encoded | `s 17A(4) the partner is guilty of the offence as well as the partnership` |
| 46 | s 17A(5) | subsection | encoded | `s 17A(5) the contract is an insurance contract` |
| 46 | s 17A(5) term “insurance contract” | term | encoded | `s 17A(5) the contract is an insurance contract` |
| 46 | s 17A(5) term “the policyholder” | term | encoded | `s 17A(5) the contract is an insurance contract` |
| 47 | s 18 | section | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` ; `s 18(2) the person has a defence` |
| 48 | s 18(1) | subsection | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` |
| 49 | s 18(1)(a) | paragraph | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` |
| 50 | s 18(1)(b) | paragraph | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` |
| 51 | s 18(1)(c) | paragraph | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` |
| 52 | s 18(1)(d) | paragraph | encoded | `s 18(1) the person commits an offence by an arrangement that facilitates retention or control of terrorist property` |
| 53 | s 18(2) | subsection | encoded | `s 18(2) the person has a defence` |
| 54 | s 19 | section | encoded | `s 19(1) this section applies to the person` ; `s 19(1A) this section does not apply to the person` ; `s 19(2) the person commits an offence by not disclosing to a constable` ; `s 19(2) the person must disclose to a constable` ; `s 19(3) the person has a defence` ; `s 19(4) the person has a defence` ; `s 19(5) subsection (2) requires the professional legal adviser to disclose` ; `s 19(6) the information is obtained by the adviser in privileged circumstances` ; `s 19(7) the person is treated as having committed an offence under one of sections 15 to 18` ; `s 19(7A) the business is a business in the regulated sector` ; `s 19(7B) the person is a constable for the purposes of s 19` ; `s 19(8) the ceiling of the penalty for an offence under s 19` |
| 55 | s 19(1) | subsection | encoded | `s 19(1) this section applies to the person` |
| 56 | s 19(1)(a) | paragraph | encoded | `s 19(1) this section applies to the person` |
| 57 | s 19(1)(b) | paragraph | encoded | `s 19(1) this section applies to the person` |
| 58 | s 19(1)(b)(i) | sub-paragraph | encoded | `s 19(1) this section applies to the person` |
| 59 | s 19(1)(b)(ii) | sub-paragraph | encoded | `s 19(1) this section applies to the person` |
| 60 | s 19(1A) | subsection | encoded | `s 19(1A) this section does not apply to the person` |
| 61 | s 19(2) | subsection | fork | F2 ; `s 19(2) the person commits an offence by not disclosing to a constable` ; `s 19(2) the person must disclose to a constable` |
| 62 | s 19(2)(a) | paragraph | fork | F2 ; `s 19(2) the person commits an offence by not disclosing to a constable` ; `s 19(2) the person must disclose to a constable` |
| 63 | s 19(2)(b) | paragraph | fork | F2 ; `s 19(2) the person commits an offence by not disclosing to a constable` ; `s 19(2) the person must disclose to a constable` |
| 64 | s 19(3) | subsection | encoded | `s 19(3) the person has a defence` |
| 65 | s 19(4) | subsection | encoded | `s 19(4) the person has a defence` |
| 66 | s 19(4)(a) | paragraph | encoded | `s 19(4) the person has a defence` |
| 67 | s 19(4)(b) | paragraph | encoded | `s 19(4) the person has a defence` |
| 68-69 | s 19(4)(c) | paragraph | encoded | `s 19(4) the person has a defence` |
| 70 | s 19(5) | subsection | encoded | `s 19(5) subsection (2) requires the professional legal adviser to disclose` |
| 71 | s 19(5)(a) | paragraph | encoded | `s 19(5) subsection (2) requires the professional legal adviser to disclose` |
| 72 | s 19(5)(b) | paragraph | encoded | `s 19(5) subsection (2) requires the professional legal adviser to disclose` |
| 73 | s 19(6) | subsection | encoded | `s 19(6) the information is obtained by the adviser in privileged circumstances` |
| 74 | s 19(6)(a) | paragraph | encoded | `s 19(6) the information is obtained by the adviser in privileged circumstances` |
| 75 | s 19(6)(b) | paragraph | encoded | `s 19(6) the information is obtained by the adviser in privileged circumstances` |
| 76 | s 19(6)(c) | paragraph | encoded | `s 19(6) the information is obtained by the adviser in privileged circumstances` |
| 77 | s 19(7) | subsection | encoded | `s 19(7) the person is treated as having committed an offence under one of sections 15 to 18` |
| 78 | s 19(7)(a) | paragraph | encoded | `s 19(7) the person is treated as having committed an offence under one of sections 15 to 18` |
| 79 | s 19(7)(b) | paragraph | encoded | `s 19(7) the person is treated as having committed an offence under one of sections 15 to 18` |
| 80 | s 19(7A) | subsection | encoded | `s 19(7A) the business is a business in the regulated sector` |
| 81 | s 19(7B) | subsection | encoded | `s 19(7B) the person is a constable for the purposes of s 19` |
| 82 | s 19(8) | subsection | encoded | `s 19(8) the ceiling of the penalty for an offence under s 19` |
| 83 | s 19(8)(a) | paragraph | encoded | `s 19(8) the ceiling of the penalty for an offence under s 19` |
| 84 | s 19(8)(b) | paragraph | encoded | `s 19(8) the ceiling of the penalty for an offence under s 19` |
| 85 | s 20 | section | encoded | `s 20(1) the person may disclose to a constable` ; `s 20(1) the person may disclose to a constable, as a permission` ; `s 20(2) the person may make a disclosure to a constable in the circumstances mentioned in s 19(1) and (2)` ; `s 20(3) a restriction on disclosure imposed by statute or otherwise does not prevent the disclosure` ; `s 20(4) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` ; `s 20(5) the person is a constable for the purposes of s 20` |
| 86 | s 20(1) | subsection | encoded | `s 20(1) the person may disclose to a constable` ; `s 20(1) the person may disclose to a constable, as a permission` |
| 87 | s 20(1)(a) | paragraph | encoded | `s 20(1) the person may disclose to a constable` ; `s 20(1) the person may disclose to a constable, as a permission` |
| 88 | s 20(1)(b) | paragraph | encoded | `s 20(1) the person may disclose to a constable` ; `s 20(1) the person may disclose to a constable, as a permission` |
| 89 | s 20(2) | subsection | encoded | `s 20(2) the person may make a disclosure to a constable in the circumstances mentioned in s 19(1) and (2)` |
| 90 | s 20(3) | subsection | encoded | `s 20(3) a restriction on disclosure imposed by statute or otherwise does not prevent the disclosure` |
| 91 | s 20(4) | subsection | encoded | `s 20(4) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 92 | s 20(4)(a) | paragraph | encoded | `s 20(4) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 93-94 | s 20(4)(b) | paragraph | encoded | `s 20(4) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 95 | s 20(5) | subsection | encoded | `s 20(5) the person is a constable for the purposes of s 20` |
| 96 | s 21 | section | encoded | `s 21(1) the person does not commit an offence under any of sections 15 to 18 by acting with the express consent of a constable` ; `s 21(2) the person does not commit an offence under any of sections 15 to 18 by involvement in the transaction` ; `s 21(3) subsection (2) applies to the person's disclosure` ; `s 21(4) subsection (2) does not apply to the person` ; `s 21(5) the person has a defence` ; `s 21(6) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` ; `s 21(7) the involvement is in a transaction or arrangement relating to money or other property` |
| 97 | s 21(1) | subsection | encoded | `s 21(1) the person does not commit an offence under any of sections 15 to 18 by acting with the express consent of a constable` |
| 98 | s 21(2) | subsection | encoded | `s 21(2) the person does not commit an offence under any of sections 15 to 18 by involvement in the transaction` |
| 99 | s 21(2)(a) | paragraph | encoded | `s 21(2) the person does not commit an offence under any of sections 15 to 18 by involvement in the transaction` |
| 100 | s 21(2)(b) | paragraph | encoded | `s 21(2) the person does not commit an offence under any of sections 15 to 18 by involvement in the transaction` |
| 101 | s 21(3) | subsection | encoded | `s 21(3) subsection (2) applies to the person's disclosure` |
| 102 | s 21(3)(a) | paragraph | encoded | `s 21(3) subsection (2) applies to the person's disclosure` |
| 103 | s 21(3)(b) | paragraph | encoded | `s 21(3) subsection (2) applies to the person's disclosure` |
| 104 | s 21(3)(c) | paragraph | encoded | `s 21(3) subsection (2) applies to the person's disclosure` |
| 105 | s 21(4) | subsection | encoded | `s 21(4) subsection (2) does not apply to the person` |
| 106 | s 21(4)(a) | paragraph | encoded | `s 21(4) subsection (2) does not apply to the person` |
| 107 | s 21(4)(b) | paragraph | encoded | `s 21(4) subsection (2) does not apply to the person` |
| 108 | s 21(5) | subsection | fork | F7 ; `s 21(5) the person has a defence` |
| 109 | s 21(5)(a) | paragraph | fork | F7 ; `s 21(5) the person has a defence` |
| 110 | s 21(5)(b) | paragraph | fork | F7 ; `s 21(5) the person has a defence` |
| 111 | s 21(6) | subsection | encoded | `s 21(6) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 112 | s 21(6)(a) | paragraph | encoded | `s 21(6) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 113-114 | s 21(6)(b) | paragraph | encoded | `s 21(6) a disclosure in accordance with the employer's procedure counts as a disclosure to a constable` |
| 115 | s 21(7) | subsection | encoded | `s 21(7) the involvement is in a transaction or arrangement relating to money or other property` |
| 116 | s 21ZA | section | encoded | `s 21ZA(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed first and had consent` ; `s 21ZA(2) the person is treated as having the authorised officer's consent` ; `s 21ZA(3) the last day of the notice period` ; `s 21ZA(3) the working day numbered` ; `s 21ZA(4) the day is a working day` ; `s 21ZA(5) the person is an authorised officer` ; `s 21ZA(6) the involvement is in a transaction or arrangement relating to money or other property` |
| 117 | s 21ZA(1) | subsection | encoded | `s 21ZA(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed first and had consent` |
| 118 | s 21ZA(1)(a) | paragraph | encoded | `s 21ZA(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed first and had consent` |
| 119 | s 21ZA(1)(b) | paragraph | encoded | `s 21ZA(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed first and had consent` |
| 120 | s 21ZA(2) | subsection | fork | F3 ; `s 21ZA(2) the person is treated as having the authorised officer's consent` |
| 121 | s 21ZA(3) | subsection | fork | F3 ; `s 21ZA(3) the last day of the notice period` ; `s 21ZA(3) the working day numbered` |
| 122 | s 21ZA(4) | subsection | fork | F4 ; `s 21ZA(4) the day is a working day` |
| 123 | s 21ZA(5) | subsection | encoded | `s 21ZA(5) the person is an authorised officer` |
| 123 | s 21ZA(5) term “authorised officer” | term | encoded | `s 21ZA(5) the person is an authorised officer` |
| 124 | s 21ZA(6) | subsection | encoded | `s 21ZA(6) the involvement is in a transaction or arrangement relating to money or other property` |
| 125 | s 21ZB | section | encoded | `s 21ZB(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed afterwards` ; `s 21ZB(2) section 21ZB applies to the person` ; `s 21ZB(3) section 21ZB does not apply to the person` ; `s 21ZB(4) the person is an authorised officer` ; `s 21ZB(5) the involvement is in a transaction or arrangement relating to money or other property` |
| 126 | s 21ZB(1) | subsection | encoded | `s 21ZB(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed afterwards` |
| 127 | s 21ZB(1)(a) | paragraph | encoded | `s 21ZB(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed afterwards` |
| 128 | s 21ZB(1)(b) | paragraph | encoded | `s 21ZB(1) the person does not commit an offence under any of sections 15 to 18 by involvement, having disclosed afterwards` |
| 129 | s 21ZB(2) | subsection | encoded | `s 21ZB(2) section 21ZB applies to the person` |
| 130 | s 21ZB(2)(a) | paragraph | encoded | `s 21ZB(2) section 21ZB applies to the person` |
| 131 | s 21ZB(2)(b) | paragraph | encoded | `s 21ZB(2) section 21ZB applies to the person` |
| 132 | s 21ZB(3) | subsection | encoded | `s 21ZB(3) section 21ZB does not apply to the person` |
| 133 | s 21ZB(3)(a) | paragraph | encoded | `s 21ZB(3) section 21ZB does not apply to the person` |
| 134 | s 21ZB(3)(b) | paragraph | encoded | `s 21ZB(3) section 21ZB does not apply to the person` |
| 135 | s 21ZB(4) | subsection | encoded | `s 21ZB(4) the person is an authorised officer` |
| 135 | s 21ZB(4) term “authorised officer” | term | encoded | `s 21ZB(4) the person is an authorised officer` |
| 136 | s 21ZB(5) | subsection | encoded | `s 21ZB(5) the involvement is in a transaction or arrangement relating to money or other property` |
| 137-138 | s 21ZC | section | encoded | `s 21ZC the person has a defence` |
| 139 | s 21ZC(a) | paragraph | encoded | `s 21ZC the person has a defence` |
| 140 | s 21ZC(b) | paragraph | encoded | `s 21ZC the person has a defence` |
| 141 | s 21A | section | encoded | `s 21A(1) and (5) the person commits an offence under section 21A` ; `s 21A(1) the person commits an offence if each of the three conditions is satisfied` ; `s 21A(2) the first condition is satisfied` ; `s 21A(3) the second condition is satisfied` ; `s 21A(4) the third condition is satisfied` ; `s 21A(5) the person does not commit an offence under section 21A` ; `s 21A(5A) subsection (5A) applies to the person` ; `s 21A(6) the court must consider whether the person followed the relevant guidance` ; `s 21A(6) the guidance is relevant guidance the court must consider` ; `s 21A(7) the disclosure is a disclosure to a nominated officer` ; `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(9) subsection (8) does not apply to the information or other matter` ; `s 21A(10)(a) the business is a business in the regulated sector` ; `s 21A(10)(b) the body is a supervisory authority` ; `s 21A(11) the person is to be taken to have committed an offence mentioned in s 21A(2)` ; `s 21A(12) the ceiling of the penalty for an offence under s 21A` ; `s 21A(13) the body is an appropriate body` ; `s 21A(14) the person is a constable for the purposes of s 21A` ; `s 21A(15) the person is a relevant professional adviser` |
| 142 | s 21A(1) | subsection | encoded | `s 21A(1) and (5) the person commits an offence under section 21A` ; `s 21A(1) the person commits an offence if each of the three conditions is satisfied` |
| 143 | s 21A(2) | subsection | encoded | `s 21A(2) the first condition is satisfied` |
| 144 | s 21A(2)(a) | paragraph | encoded | `s 21A(2) the first condition is satisfied` |
| 145-146 | s 21A(2)(b) | paragraph | encoded | `s 21A(2) the first condition is satisfied` |
| 147 | s 21A(3) | subsection | encoded | `s 21A(3) the second condition is satisfied` |
| 148 | s 21A(3)(a) | paragraph | encoded | `s 21A(3) the second condition is satisfied` |
| 149-150 | s 21A(3)(b) | paragraph | encoded | `s 21A(3) the second condition is satisfied` |
| 151 | s 21A(4) | subsection | encoded | `s 21A(4) the third condition is satisfied` |
| 152 | s 21A(5) | subsection | encoded | `s 21A(5) the person does not commit an offence under section 21A` |
| 153 | s 21A(5)(a) | paragraph | encoded | `s 21A(5) the person does not commit an offence under section 21A` |
| 154 | s 21A(5)(b) | paragraph | encoded | `s 21A(5) the person does not commit an offence under section 21A` |
| 155 | s 21A(5)(c) | paragraph | encoded | `s 21A(5) the person does not commit an offence under section 21A` |
| 156 | s 21A(5A) | subsection | encoded | `s 21A(5A) subsection (5A) applies to the person` |
| 157 | s 21A(5A)(a) | paragraph | encoded | `s 21A(5A) subsection (5A) applies to the person` |
| 158 | s 21A(5A)(b) | paragraph | encoded | `s 21A(5A) subsection (5A) applies to the person` |
| 159 | s 21A(5A)(c) | paragraph | encoded | `s 21A(5A) subsection (5A) applies to the person` |
| 160 | s 21A(6) | subsection | encoded | `s 21A(6) the court must consider whether the person followed the relevant guidance` ; `s 21A(6) the guidance is relevant guidance the court must consider` |
| 161 | s 21A(6)(a) | paragraph | encoded | `s 21A(6) the court must consider whether the person followed the relevant guidance` ; `s 21A(6) the guidance is relevant guidance the court must consider` |
| 162 | s 21A(6)(b) | paragraph | encoded | `s 21A(6) the court must consider whether the person followed the relevant guidance` ; `s 21A(6) the guidance is relevant guidance the court must consider` |
| 163 | s 21A(6)(c) | paragraph | encoded | `s 21A(6) the court must consider whether the person followed the relevant guidance` ; `s 21A(6) the guidance is relevant guidance the court must consider` |
| 164 | s 21A(7) | subsection | encoded | `s 21A(7) the disclosure is a disclosure to a nominated officer` |
| 165 | s 21A(7)(a) | paragraph | encoded | `s 21A(7) the disclosure is a disclosure to a nominated officer` |
| 166 | s 21A(7)(b) | paragraph | encoded | `s 21A(7) the disclosure is a disclosure to a nominated officer` |
| 167 | s 21A(8) | subsection | encoded | `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` |
| 168 | s 21A(8)(a) | paragraph | encoded | `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` |
| 169 | s 21A(8)(b) | paragraph | encoded | `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` |
| 170 | s 21A(8)(c) | paragraph | encoded | `s 21A(8) and (9) the information or other matter comes to the adviser in privileged circumstances` ; `s 21A(8) the information or other matter comes to the adviser in privileged circumstances` |
| 171 | s 21A(9) | subsection | encoded | `s 21A(9) subsection (8) does not apply to the information or other matter` |
| 172 | s 21A(10) | subsection | encoded | `s 21A(10)(a) the business is a business in the regulated sector` ; `s 21A(10)(b) the body is a supervisory authority` |
| 173 | s 21A(10)(a) | paragraph | encoded | `s 21A(10)(a) the business is a business in the regulated sector` ; `s 21A(10)(b) the body is a supervisory authority` |
| 174 | s 21A(10)(b) | paragraph | encoded | `s 21A(10)(a) the business is a business in the regulated sector` ; `s 21A(10)(b) the body is a supervisory authority` |
| 175 | s 21A(11) | subsection | encoded | `s 21A(11) the person is to be taken to have committed an offence mentioned in s 21A(2)` |
| 176 | s 21A(11)(a) | paragraph | encoded | `s 21A(11) the person is to be taken to have committed an offence mentioned in s 21A(2)` |
| 177 | s 21A(11)(b) | paragraph | encoded | `s 21A(11) the person is to be taken to have committed an offence mentioned in s 21A(2)` |
| 178 | s 21A(12) | subsection | encoded | `s 21A(12) the ceiling of the penalty for an offence under s 21A` |
| 179 | s 21A(12)(a) | paragraph | encoded | `s 21A(12) the ceiling of the penalty for an offence under s 21A` |
| 180 | s 21A(12)(b) | paragraph | encoded | `s 21A(12) the ceiling of the penalty for an offence under s 21A` |
| 181 | s 21A(13) | subsection | encoded | `s 21A(13) the body is an appropriate body` |
| 182 | s 21A(14) | subsection | encoded | `s 21A(14) the person is a constable for the purposes of s 21A` |
| 183 | s 21A(15) | subsection | encoded | `s 21A(15) the person is a relevant professional adviser` |
| 183 | s 21A(15) term “relevant professional adviser” | term | encoded | `s 21A(15) the person is a relevant professional adviser` |
| 184 | s 21A(15)(a) | paragraph | encoded | `s 21A(15) the person is a relevant professional adviser` |
| 185 | s 21A(15)(b) | paragraph | encoded | `s 21A(15) the person is a relevant professional adviser` |
| 186 | s 21B | section | encoded | `s 21B(1) the disclosure is not to be taken to breach any restriction on the disclosure of information` ; `s 21B(2) the first condition is satisfied` ; `s 21B(3) the second condition is satisfied` ; `s 21B(4) the third condition is satisfied` ; `s 21B(5) the disclosure is a disclosure to a nominated officer` ; `s 21B(6) the business is a business in the regulated sector` ; `s 21B(7) the person is a constable for the purposes of s 21B` |
| 187 | s 21B(1) | subsection | encoded | `s 21B(1) the disclosure is not to be taken to breach any restriction on the disclosure of information` |
| 188 | s 21B(2) | subsection | encoded | `s 21B(2) the first condition is satisfied` |
| 189 | s 21B(3) | subsection | encoded | `s 21B(3) the second condition is satisfied` |
| 190 | s 21B(3)(a) | paragraph | encoded | `s 21B(3) the second condition is satisfied` |
| 191-192 | s 21B(3)(b) | paragraph | encoded | `s 21B(3) the second condition is satisfied` |
| 193 | s 21B(4) | subsection | encoded | `s 21B(4) the third condition is satisfied` |
| 194 | s 21B(5) | subsection | encoded | `s 21B(5) the disclosure is a disclosure to a nominated officer` |
| 195 | s 21B(5)(a) | paragraph | encoded | `s 21B(5) the disclosure is a disclosure to a nominated officer` |
| 196 | s 21B(5)(b) | paragraph | encoded | `s 21B(5) the disclosure is a disclosure to a nominated officer` |
| 197 | s 21B(6) | subsection | encoded | `s 21B(6) the business is a business in the regulated sector` |
| 198 | s 21B(7) | subsection | encoded | `s 21B(7) the person is a constable for the purposes of s 21B` |
| 199 | s 21C | section | encoded | `s 21C(1) the constable must disclose it in full to an authorised National Crime Agency officer` ; `s 21C(1) the constable must pass the disclosure in full to an authorised National Crime Agency officer` ; `s 21C(2) the constable must pass the section 21 disclosure in full to an authorised National Crime Agency officer` |
| 200 | s 21C(1) | subsection | encoded | `s 21C(1) the constable must disclose it in full to an authorised National Crime Agency officer` ; `s 21C(1) the constable must pass the disclosure in full to an authorised National Crime Agency officer` ; stated gap: the text puts the duty on "the constable" to whom the disclosure was made and states no consequence of a failure to pass it on; the duty is asserted over the facts and traced, and no remedy is invented |
| 201 | s 21C(2) | subsection | encoded | `s 21C(2) the constable must pass the section 21 disclosure in full to an authorised National Crime Agency officer` |
| 202 | s 21CA | section | encoded | `s 21CA(1) A may disclose information to one or more other persons` ; `s 21CA(2) condition 1 is met` ; `s 21CA(3) condition 2 is met` ; `s 21CA(4) condition 3 is met` ; `s 21CA(5) condition 4 is met` ; `s 21CA(6) condition 5 is met` ; `s 21CA(7) condition 5 does not apply` ; `s 21CA(8) the person may disclose information to A for the purposes of making a disclosure request` |
| 203 | s 21CA(1) | subsection | fork | F8 ; `s 21CA(1) A may disclose information to one or more other persons` |
| 204 | s 21CA(1)(a) | paragraph | fork | F8 ; `s 21CA(1) A may disclose information to one or more other persons` |
| 205 | s 21CA(1)(b) | paragraph | fork | F8 ; `s 21CA(1) A may disclose information to one or more other persons` |
| 206 | s 21CA(2) | subsection | encoded | `s 21CA(2) condition 1 is met` |
| 207 | s 21CA(2)(a) | paragraph | encoded | `s 21CA(2) condition 1 is met` |
| 208 | s 21CA(2)(b) | paragraph | encoded | `s 21CA(2) condition 1 is met` |
| 209 | s 21CA(2)(c) | paragraph | encoded | `s 21CA(2) condition 1 is met` |
| 210 | s 21CA(3) | subsection | encoded | `s 21CA(3) condition 2 is met` |
| 211 | s 21CA(3)(a) | paragraph | encoded | `s 21CA(3) condition 2 is met` |
| 212 | s 21CA(3)(b) | paragraph | encoded | `s 21CA(3) condition 2 is met` |
| 213 | s 21CA(4) | subsection | encoded | `s 21CA(4) condition 3 is met` |
| 214 | s 21CA(5) | subsection | encoded | `s 21CA(5) condition 4 is met` |
| 215 | s 21CA(5)(a) | paragraph | encoded | `s 21CA(5) condition 4 is met` |
| 216 | s 21CA(5)(b) | paragraph | encoded | `s 21CA(5) condition 4 is met` |
| 217 | s 21CA(6) | subsection | encoded | `s 21CA(6) condition 5 is met` |
| 218 | s 21CA(7) | subsection | encoded | `s 21CA(7) condition 5 does not apply` |
| 219 | s 21CA(8) | subsection | encoded | `s 21CA(8) the person may disclose information to A for the purposes of making a disclosure request` |
| 220 | s 21CB | section | encoded | `s 21CB(1) the disclosure request has the content the section requires` ; `s 21CB(2) subsections (3) and (4) apply to the request` ; `s 21CB(3) the request states the grounds or other information` ; `s 21CB(4) the request provides the other information` ; `s 21CB(5) the required notification is made by the person the subsection names` ; `s 21CB(6) the notification has the content the subsection requires` ; `s 21CB(7) the notification has the content the subsection requires` ; `s 21CB(8) the notification has the content the subsection requires` |
| 221 | s 21CB(1) | subsection | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 222 | s 21CB(1)(a) | paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 223 | s 21CB(1)(a)(i) | sub-paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 224 | s 21CB(1)(a)(ii) | sub-paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 225 | s 21CB(1)(b) | paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 226 | s 21CB(1)(c) | paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 227 | s 21CB(1)(d) | paragraph | encoded | `s 21CB(1) the disclosure request has the content the section requires` |
| 228 | s 21CB(2) | subsection | encoded | `s 21CB(2) subsections (3) and (4) apply to the request` |
| 229 | s 21CB(3) | subsection | encoded | `s 21CB(3) the request states the grounds or other information` |
| 230 | s 21CB(3)(a) | paragraph | encoded | `s 21CB(3) the request states the grounds or other information` |
| 231 | s 21CB(3)(b) | paragraph | encoded | `s 21CB(3) the request states the grounds or other information` |
| 232 | s 21CB(4) | subsection | encoded | `s 21CB(4) the request provides the other information` |
| 233 | s 21CB(5) | subsection | encoded | `s 21CB(5) the required notification is made by the person the subsection names` |
| 234 | s 21CB(5)(a) | paragraph | encoded | `s 21CB(5) the required notification is made by the person the subsection names` |
| 235 | s 21CB(5)(b) | paragraph | encoded | `s 21CB(5) the required notification is made by the person the subsection names` |
| 236 | s 21CB(6) | subsection | encoded | `s 21CB(6) the notification has the content the subsection requires` |
| 237 | s 21CB(7) | subsection | encoded | `s 21CB(7) the notification has the content the subsection requires` |
| 238 | s 21CB(7)(a) | paragraph | encoded | `s 21CB(7) the notification has the content the subsection requires` |
| 239 | s 21CB(7)(b) | paragraph | encoded | `s 21CB(7) the notification has the content the subsection requires` |
| 240 | s 21CB(7)(c) | paragraph | encoded | `s 21CB(7) the notification has the content the subsection requires` |
| 241 | s 21CB(7)(d) | paragraph | encoded | `s 21CB(7) the notification has the content the subsection requires` |
| 242 | s 21CB(8) | subsection | encoded | `s 21CB(8) the notification has the content the subsection requires` |
| 243 | s 21CB(8)(a) | paragraph | encoded | `s 21CB(8) the notification has the content the subsection requires` |
| 244 | s 21CB(8)(b) | paragraph | encoded | `s 21CB(8) the notification has the content the subsection requires` |
| 245 | s 21CB(8)(c) | paragraph | encoded | `s 21CB(8) the notification has the content the subsection requires` |
| 246 | s 21CB(8)(d) | paragraph | encoded | `s 21CB(8) the notification has the content the subsection requires` |
| 247 | s 21CC | section | encoded | `s 21CC(1) section 21CC applies` ; `s 21CC(2) the required notification satisfies the requirement to make the required disclosure` ; `s 21CC(3) the joint disclosure report satisfies the requirement to make the required disclosure` ; `s 21CC(4) the report is a joint disclosure report` ; `s 21CC(5) the report has the content required for a suspicion` ; `s 21CC(6) the report has the content required for terrorist property` ; `s 21CC(7) the last day of the applicable period` ; `s 21CC(8) the length in days of the period of 28 days` ; `s 21CC(8) the notice varies the period of 28 days` ; `s 21CC(9) the joint disclosure report is approved and signed as required` ; `s 21CC(10) the person counts as A, B or C` |
| 248 | s 21CC(1) | subsection | encoded | `s 21CC(1) section 21CC applies` |
| 249 | s 21CC(1)(a) | paragraph | encoded | `s 21CC(1) section 21CC applies` |
| 250 | s 21CC(1)(b) | paragraph | encoded | `s 21CC(1) section 21CC applies` |
| 251 | s 21CC(1)(c) | paragraph | encoded | `s 21CC(1) section 21CC applies` |
| 252-253 | s 21CC(2) | subsection | encoded | `s 21CC(2) the required notification satisfies the requirement to make the required disclosure` |
| 254-255 | s 21CC(3) | subsection | encoded | `s 21CC(3) the joint disclosure report satisfies the requirement to make the required disclosure` |
| 256 | s 21CC(4) | subsection | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 257 | s 21CC(4)(a) | paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 258 | s 21CC(4)(b) | paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 259 | s 21CC(4)(c) | paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 260 | s 21CC(4)(c)(i) | sub-paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 261 | s 21CC(4)(c)(ii) | sub-paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 262 | s 21CC(4)(d) | paragraph | fork | F9 ; `s 21CC(4) the report is a joint disclosure report` |
| 263 | s 21CC(5) | subsection | encoded | `s 21CC(5) the report has the content required for a suspicion` |
| 264 | s 21CC(5)(a) | paragraph | encoded | `s 21CC(5) the report has the content required for a suspicion` |
| 265 | s 21CC(5)(b) | paragraph | encoded | `s 21CC(5) the report has the content required for a suspicion` |
| 266 | s 21CC(5)(c) | paragraph | encoded | `s 21CC(5) the report has the content required for a suspicion` |
| 267 | s 21CC(5)(d) | paragraph | encoded | `s 21CC(5) the report has the content required for a suspicion` |
| 268 | s 21CC(6) | subsection | encoded | `s 21CC(6) the report has the content required for terrorist property` |
| 269 | s 21CC(6)(a) | paragraph | encoded | `s 21CC(6) the report has the content required for terrorist property` |
| 270 | s 21CC(6)(b) | paragraph | encoded | `s 21CC(6) the report has the content required for terrorist property` |
| 271 | s 21CC(6)(c) | paragraph | encoded | `s 21CC(6) the report has the content required for terrorist property` |
| 272 | s 21CC(6)(d) | paragraph | encoded | `s 21CC(6) the report has the content required for terrorist property` |
| 273 | s 21CC(7) | subsection | fork | F9 ; `s 21CC(7) the last day of the applicable period` |
| 274 | s 21CC(7)(a) | paragraph | fork | F9 ; `s 21CC(7) the last day of the applicable period` |
| 275 | s 21CC(7)(b) | paragraph | fork | F9 ; `s 21CC(7) the last day of the applicable period` |
| 276 | s 21CC(8) | subsection | fork | F10 ; `s 21CC(8) the length in days of the period of 28 days` ; `s 21CC(8) the notice varies the period of 28 days` ; stated gap: only a written notice given by a constable to the person who made the required notification is covered; the Act says nothing of a notice given any other way, so that case is NOTHING (s 21CC(8) the notice varies the period of 28 days) |
| 277 | s 21CC(9) | subsection | encoded | `s 21CC(9) the joint disclosure report is approved and signed as required` |
| 278 | s 21CC(9)(a) | paragraph | encoded | `s 21CC(9) the joint disclosure report is approved and signed as required` |
| 279-280 | s 21CC(9)(b) | paragraph | encoded | `s 21CC(9) the joint disclosure report is approved and signed as required` |
| 281 | s 21CC(10) | subsection | encoded | `s 21CC(10) the person counts as A, B or C` |
| 282 | s 21CC(10)(a) | paragraph | encoded | `s 21CC(10) the person counts as A, B or C` |
| 283 | s 21CC(10)(b) | paragraph | encoded | `s 21CC(10) the person counts as A, B or C` |
| 284 | s 21CD | section | encoded | `s 21CD(1) subsections (2) and (3) apply` ; `s 21CD(2) section 21CC(2) covers the matter, where A made the notification` ; `s 21CD(3) section 21CC(2) removes the requirement for the matter, where A made the notification` ; `s 21CD(4) subsections (5) to (8) apply` ; `s 21CD(5) section 21CC(2) covers the matter for A or C, where B made the notification` ; `s 21CD(6) section 21CC(2) removes the requirement for the matter, where B made the notification` ; `s 21CD(7) section 21CC(2) covers the matter for B` ; `s 21CD(8)(a) section 21CC(2) covers the requirement` ; `s 21CD(8)(b) section 21CC(2) removes the requirement` ; `s 21CD(9) the person who made the required notification must notify a constable` ; `s 21CD(9) the person who made the required notification must notify a constable that a report is not being made` ; `s 21CD(10) section 21CC(3) covers the matter` ; `s 21CD(11) the term has the same meaning as in s 21CC` |
| 285 | s 21CD(1) | subsection | encoded | `s 21CD(1) subsections (2) and (3) apply` |
| 286 | s 21CD(2) | subsection | encoded | `s 21CD(2) section 21CC(2) covers the matter, where A made the notification` |
| 287 | s 21CD(2)(a) | paragraph | encoded | `s 21CD(2) section 21CC(2) covers the matter, where A made the notification` |
| 288 | s 21CD(2)(b) | paragraph | encoded | `s 21CD(2) section 21CC(2) covers the matter, where A made the notification` |
| 289 | s 21CD(3) | subsection | encoded | `s 21CD(3) section 21CC(2) removes the requirement for the matter, where A made the notification` |
| 290 | s 21CD(4) | subsection | encoded | `s 21CD(4) subsections (5) to (8) apply` |
| 291 | s 21CD(5) | subsection | encoded | `s 21CD(5) section 21CC(2) covers the matter for A or C, where B made the notification` |
| 292 | s 21CD(5)(a) | paragraph | encoded | `s 21CD(5) section 21CC(2) covers the matter for A or C, where B made the notification` |
| 293 | s 21CD(5)(b) | paragraph | encoded | `s 21CD(5) section 21CC(2) covers the matter for A or C, where B made the notification` |
| 294 | s 21CD(6) | subsection | encoded | `s 21CD(6) section 21CC(2) removes the requirement for the matter, where B made the notification` |
| 295 | s 21CD(7) | subsection | encoded | `s 21CD(7) section 21CC(2) covers the matter for B` |
| 296 | s 21CD(7)(a) | paragraph | encoded | `s 21CD(7) section 21CC(2) covers the matter for B` |
| 297 | s 21CD(7)(b) | paragraph | encoded | `s 21CD(7) section 21CC(2) covers the matter for B` |
| 298 | s 21CD(8) | subsection | encoded | `s 21CD(8)(a) section 21CC(2) covers the requirement` ; `s 21CD(8)(b) section 21CC(2) removes the requirement` |
| 299 | s 21CD(8)(a) | paragraph | encoded | `s 21CD(8)(a) section 21CC(2) covers the requirement` ; `s 21CD(8)(b) section 21CC(2) removes the requirement` |
| 300 | s 21CD(8)(b) | paragraph | encoded | `s 21CD(8)(a) section 21CC(2) covers the requirement` ; `s 21CD(8)(b) section 21CC(2) removes the requirement` |
| 301 | s 21CD(9) | subsection | encoded | `s 21CD(9) the person who made the required notification must notify a constable` ; `s 21CD(9) the person who made the required notification must notify a constable that a report is not being made` |
| 302 | s 21CD(10) | subsection | encoded | `s 21CD(10) section 21CC(3) covers the matter` |
| 303 | s 21CD(10)(a) | paragraph | encoded | `s 21CD(10) section 21CC(3) covers the matter` |
| 304 | s 21CD(10)(b) | paragraph | encoded | `s 21CD(10) section 21CC(3) covers the matter` |
| 305 | s 21CD(11) | subsection | encoded | `s 21CD(11) the term has the same meaning as in s 21CC` |
| 306 | s 21CE | section | encoded | `s 21CE(1) the relevant disclosure does not breach an obligation of confidence or any other restriction` ; `s 21CE(2) the person making the relevant disclosure shall not include information from a UK law enforcement agency` ; `s 21CE(2) the relevant disclosure is barred from including the information` ; `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` ; `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` ; `s 21CE(4) subsection (1) applies whether or not the conditions were met` ; `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 307 | s 21CE(1) | subsection | encoded | `s 21CE(1) the relevant disclosure does not breach an obligation of confidence or any other restriction` |
| 308 | s 21CE(1)(a) | paragraph | encoded | `s 21CE(1) the relevant disclosure does not breach an obligation of confidence or any other restriction` |
| 309-310 | s 21CE(1)(b) | paragraph | encoded | `s 21CE(1) the relevant disclosure does not breach an obligation of confidence or any other restriction` |
| 311 | s 21CE(2) | subsection | encoded | `s 21CE(2) the person making the relevant disclosure shall not include information from a UK law enforcement agency` ; `s 21CE(2) the relevant disclosure is barred from including the information` |
| 312 | s 21CE(3) | subsection | encoded | `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` ; `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` |
| 312 | s 21CE(3) term “the undertaking” | term | encoded | `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` |
| 313 | s 21CE(3)(a) | paragraph | encoded | `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` ; `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` |
| 314 | s 21CE(3)(b) | paragraph | encoded | `s 21CE(3)(a) the disclosure by the undertaking is made as the subsection requires` ; `s 21CE(3)(b) the disclosure to the undertaking is made as the subsection requires` |
| 315 | s 21CE(4) | subsection | encoded | `s 21CE(4) subsection (1) applies whether or not the conditions were met` |
| 316 | s 21CE(5) | subsection | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 317 | s 21CE(5) “relevant disclosure” | definition | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 318 | s 21CE(5) “UK law enforcement agency” | definition | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 319 | s 21CE(5) “UK law enforcement agency” item 1 | item | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 320 | s 21CE(5) “UK law enforcement agency” item 2 | item | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 321 | s 21CE(5) “UK law enforcement agency” item 3 | item | encoded | `s 21CE(5) the body is a UK law enforcement agency` ; `s 21CE(5) the disclosure is a relevant disclosure` |
| 322 | s 21CF | section | encoded | `s 21CF(2) the person is a constable for the purposes of ss 21CA to 21CE` ; `s 21CF(3) the business is a business in the regulated sector` ; `s 21CF(4) the request is a disclosure request` ; `s 21CF(5) the person is a nominated officer` ; `s 21CF(6) the person is a relevant undertaking` ; `s 21CF(7) the disclosure is a required disclosure` ; `s 21CF(8) the notification is a required notification` ; `s 21CF(9)(a) the undertaking is a credit institution` ; `s 21CF(9)(b) the undertaking is a financial institution` ; `s 21CF(10) the offence is a terrorist financing offence` |
| 323 | s 21CF(1) | subsection | encoded | `s 21CF(2) the person is a constable for the purposes of ss 21CA to 21CE` |
| 324 | s 21CF(2) | subsection | encoded | `s 21CF(2) the person is a constable for the purposes of ss 21CA to 21CE` |
| 325 | s 21CF(3) | subsection | encoded | `s 21CF(3) the business is a business in the regulated sector` |
| 326 | s 21CF(4) | subsection | encoded | `s 21CF(4) the request is a disclosure request` |
| 326 | s 21CF(4) term “Disclosure request” | term | encoded | `s 21CF(4) the request is a disclosure request` |
| 327 | s 21CF(5) | subsection | encoded | `s 21CF(5) the person is a nominated officer` |
| 327 | s 21CF(5) term “Nominated officer” | term | encoded | `s 21CF(5) the person is a nominated officer` |
| 328 | s 21CF(6) | subsection | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 328 | s 21CF(6) term “Relevant undertaking” | term | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 329 | s 21CF(6)(a) | paragraph | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 330 | s 21CF(6)(b) | paragraph | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 331 | s 21CF(6)(c) | paragraph | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 332 | s 21CF(6)(d) | paragraph | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 333 | s 21CF(6)(e) | paragraph | encoded | `s 21CF(6) the person is a relevant undertaking` |
| 334 | s 21CF(7) | subsection | encoded | `s 21CF(7) the disclosure is a required disclosure` |
| 334 | s 21CF(7) term “Required disclosure” | term | encoded | `s 21CF(7) the disclosure is a required disclosure` |
| 335 | s 21CF(7)(a) | paragraph | encoded | `s 21CF(7) the disclosure is a required disclosure` |
| 336 | s 21CF(7)(b) | paragraph | encoded | `s 21CF(7) the disclosure is a required disclosure` |
| 337 | s 21CF(8) | subsection | encoded | `s 21CF(8) the notification is a required notification` |
| 337 | s 21CF(8) term “Required notification” | term | encoded | `s 21CF(8) the notification is a required notification` |
| 338 | s 21CF(9) | subsection | encoded | `s 21CF(9)(a) the undertaking is a credit institution` ; `s 21CF(9)(b) the undertaking is a financial institution` |
| 339 | s 21CF(9)(a) | paragraph | encoded | `s 21CF(9)(a) the undertaking is a credit institution` |
| 339 | s 21CF(9)(a) term “credit institution” | term | encoded | `s 21CF(9)(a) the undertaking is a credit institution` |
| 340 | s 21CF(9)(b) | paragraph | encoded | `s 21CF(9)(b) the undertaking is a financial institution` |
| 340 | s 21CF(9)(b) term “financial institution” | term | encoded | `s 21CF(9)(b) the undertaking is a financial institution` |
| 341 | s 21CF(9)(c) | paragraph | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 341 | s 21CF(9)(c) term “relevant professional adviser” | term | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 342 | s 21CF(10) | subsection | fork | F7 ; `s 21CF(10) the offence is a terrorist financing offence` |
| 342 | s 21CF(10) term “Terrorist financing offence” | term | fork | F7 ; `s 21CF(10) the offence is a terrorist financing offence` |
| 343 | s 21D | section | encoded | `s 21D(1) the person commits an offence by tipping off` ; `s 21D(2) the matter is within subsection (2)` ; `s 21D(3) the person commits an offence by disclosing an investigation` ; `s 21D(4) the ceiling of the penalty for an offence under s 21D` ; `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` |
| 344 | s 21D(1) | subsection | encoded | `s 21D(1) the person commits an offence by tipping off` |
| 345 | s 21D(1)(a) | paragraph | encoded | `s 21D(1) the person commits an offence by tipping off` |
| 346 | s 21D(1)(b) | paragraph | encoded | `s 21D(1) the person commits an offence by tipping off` |
| 347 | s 21D(1)(c) | paragraph | encoded | `s 21D(1) the person commits an offence by tipping off` |
| 348 | s 21D(2) | subsection | encoded | `s 21D(2) the matter is within subsection (2)` |
| 349 | s 21D(2)(a) | paragraph | encoded | `s 21D(2) the matter is within subsection (2)` |
| 350 | s 21D(2)(b) | paragraph | encoded | `s 21D(2) the matter is within subsection (2)` |
| 351 | s 21D(2)(c) | paragraph | encoded | `s 21D(2) the matter is within subsection (2)` |
| 352-353 | s 21D(2)(d) | paragraph | encoded | `s 21D(2) the matter is within subsection (2)` |
| 354 | s 21D(3) | subsection | encoded | `s 21D(3) the person commits an offence by disclosing an investigation` |
| 355 | s 21D(3)(a) | paragraph | encoded | `s 21D(3) the person commits an offence by disclosing an investigation` |
| 356 | s 21D(3)(b) | paragraph | encoded | `s 21D(3) the person commits an offence by disclosing an investigation` |
| 357 | s 21D(3)(c) | paragraph | encoded | `s 21D(3) the person commits an offence by disclosing an investigation` |
| 358 | s 21D(4) | subsection | encoded | `s 21D(4) the ceiling of the penalty for an offence under s 21D` |
| 359 | s 21D(4)(a) | paragraph | encoded | `s 21D(4) the ceiling of the penalty for an offence under s 21D` |
| 360 | s 21D(4)(b) | paragraph | encoded | `s 21D(4) the ceiling of the penalty for an offence under s 21D` |
| 361 | s 21D(5) | subsection | encoded | `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` |
| 362 | s 21D(5)(a) | paragraph | encoded | `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` |
| 363 | s 21D(5)(b) | paragraph | encoded | `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` |
| 364 | s 21D(5)(c) | paragraph | encoded | `s 21D(5) an exception in s 21E, s 21F or s 21G displaces the offence` |
| 365 | s 21E | section | encoded | `s 21E(1) the person does not commit an offence under s 21D` ; `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` ; `s 21E(3) the institutions belong to the same group` ; `s 21E(4) the adviser does not commit an offence under s 21D` |
| 366 | s 21E(1) | subsection | encoded | `s 21E(1) the person does not commit an offence under s 21D` |
| 367 | s 21E(2) | subsection | encoded | `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` |
| 368 | s 21E(2)(a) | paragraph | encoded | `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` |
| 369 | s 21E(2)(b) | paragraph | encoded | `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` |
| 370 | s 21E(2)(c) | paragraph | encoded | `s 21E(2) the person does not commit an offence under s 21D by a disclosure within a group` |
| 371 | s 21E(3) | subsection | encoded | `s 21E(3) the institutions belong to the same group` |
| 371 | s 21E(3) term “group” | term | encoded | `s 21E(3) the institutions belong to the same group` |
| 372 | s 21E(4) | subsection | encoded | `s 21E(4) the adviser does not commit an offence under s 21D` |
| 373 | s 21E(4)(a) | paragraph | encoded | `s 21E(4) the adviser does not commit an offence under s 21D` |
| 374 | s 21E(4)(b) | paragraph | encoded | `s 21E(4) the adviser does not commit an offence under s 21D` |
| 375 | s 21E(4)(c) | paragraph | encoded | `s 21E(4) the adviser does not commit an offence under s 21D` |
| 376 | s 21F | section | encoded | `s 21F(1) this section applies to the disclosure` ; `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 377 | s 21F(1) | subsection | encoded | `s 21F(1) this section applies to the disclosure` |
| 378 | s 21F(1)(a) | paragraph | encoded | `s 21F(1) this section applies to the disclosure` |
| 379 | s 21F(1)(b) | paragraph | encoded | `s 21F(1) this section applies to the disclosure` |
| 380 | s 21F(1)(c) | paragraph | encoded | `s 21F(1) this section applies to the disclosure` |
| 381 | s 21F(1)(d) | paragraph | encoded | `s 21F(1) this section applies to the disclosure` |
| 382 | s 21F(2) | subsection | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 383 | s 21F(2)(a) | paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 384 | s 21F(2)(a)(i) | sub-paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 385 | s 21F(2)(a)(ii) | sub-paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 386 | s 21F(2)(a)(iii) | sub-paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 387 | s 21F(2)(b) | paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 388 | s 21F(2)(c) | paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 389 | s 21F(2)(d) | paragraph | encoded | `s 21F(2) the person does not commit an offence under s 21D in respect of the disclosure` |
| 390 | s 21G | section | encoded | `s 21G(1) the person does not commit an offence under s 21D` ; `s 21G(2) the adviser does not commit an offence under s 21D` ; `s 21G(3) the person does not commit an offence under s 21D(1)` ; `s 21G(4) the person does not commit an offence under s 21D(3)` |
| 391 | s 21G(1) | subsection | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 392 | s 21G(1)(a) | paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 393 | s 21G(1)(aa) | paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 394 | s 21G(1)(b) | paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 395 | s 21G(1)(b)(i) | sub-paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 396 | s 21G(1)(b)(ii) | sub-paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 397 | s 21G(1)(b)(iii) | sub-paragraph | encoded | `s 21G(1) the person does not commit an offence under s 21D` |
| 398 | s 21G(2) | subsection | encoded | `s 21G(2) the adviser does not commit an offence under s 21D` |
| 399 | s 21G(2)(a) | paragraph | encoded | `s 21G(2) the adviser does not commit an offence under s 21D` |
| 400 | s 21G(2)(b) | paragraph | encoded | `s 21G(2) the adviser does not commit an offence under s 21D` |
| 401 | s 21G(3) | subsection | encoded | `s 21G(3) the person does not commit an offence under s 21D(1)` |
| 402 | s 21G(4) | subsection | encoded | `s 21G(4) the person does not commit an offence under s 21D(3)` |
| 403 | s 21H | section | encoded | `s 21H(1)(a) the business is a business in the regulated sector` ; `s 21H(1)(b) the body is a supervisory authority` ; `s 21H(2) the undertaking is a credit institution` ; `s 21H(2) the undertaking is a financial institution` ; `s 21H(3) the disclosure counts as a disclosure by or to the institution` ; `s 21H(4) the country or territory imposes equivalent money laundering requirements` ; `s 21H(5) the person is a relevant professional adviser` |
| 404 | s 21H(1) | subsection | encoded | `s 21H(1)(a) the business is a business in the regulated sector` ; `s 21H(1)(b) the body is a supervisory authority` |
| 405 | s 21H(1)(a) | paragraph | encoded | `s 21H(1)(a) the business is a business in the regulated sector` ; `s 21H(1)(b) the body is a supervisory authority` |
| 406-407 | s 21H(1)(b) | paragraph | encoded | `s 21H(1)(a) the business is a business in the regulated sector` ; `s 21H(1)(b) the body is a supervisory authority` |
| 408 | s 21H(2) | subsection | encoded | `s 21H(2) the undertaking is a credit institution` ; `s 21H(2) the undertaking is a financial institution` |
| 409 | s 21H(2) “credit institution” | definition | encoded | `s 21H(2) the undertaking is a credit institution` ; `s 21H(2) the undertaking is a financial institution` |
| 410 | s 21H(2) “financial institution” | definition | encoded | `s 21H(2) the undertaking is a credit institution` ; `s 21H(2) the undertaking is a financial institution` |
| 411 | s 21H(3) | subsection | encoded | `s 21H(3) the disclosure counts as a disclosure by or to the institution` |
| 412 | s 21H(4) | subsection | encoded | `s 21H(4) the country or territory imposes equivalent money laundering requirements` |
| 412 | s 21H(4) term “equivalent money laundering requirements” | term | encoded | `s 21H(4) the country or territory imposes equivalent money laundering requirements` |
| 413 | s 21H(5) | subsection | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 413 | s 21H(5) term “relevant professional adviser” | term | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 414 | s 21H(5)(a) | paragraph | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 415 | s 21H(5)(b) | paragraph | encoded | `s 21H(5) the person is a relevant professional adviser` |
| 416-417 | s 22 | section | encoded | `s 22 the ceiling of the penalty for an offence under any of sections 15 to 18` |
| 418 | s 22(a) | paragraph | encoded | `s 22 the ceiling of the penalty for an offence under any of sections 15 to 18` |
| 419 | s 22(b) | paragraph | encoded | `s 22 the ceiling of the penalty for an offence under any of sections 15 to 18` |
| 420-421 | s 22A | section | encoded | `s 22A(a) the work is employment` ; `s 22A(b) the person is the employer` |
| 420-421 | s 22A term “employment” | term | encoded | `s 22A(a) the work is employment` ; `s 22A(b) the person is the employer` |
| 422 | s 22A(a) | paragraph | encoded | `s 22A(a) the work is employment` |
| 422 | s 22A(a) term “employment” | term | encoded | `s 22A(a) the work is employment` |
| 423 | s 22A(a)(i) | sub-paragraph | encoded | `s 22A(a) the work is employment` |
| 424 | s 22A(a)(ii) | sub-paragraph | encoded | `s 22A(a) the work is employment` |
| 425 | s 22A(a)(iii) | sub-paragraph | encoded | `s 22A(a) the work is employment` |
| 426 | s 22A(b) | paragraph | encoded | `s 22A(b) the person is the employer` |
| 426 | s 22A(b) term “employer” | term | encoded | `s 22A(b) the person is the employer` |
| 427 | heading: Information orders | heading | inert | reason 1: heading |
| 428 | s 22B | section | encoded | `s 22B(1) the court may make an information order` ; `s 22B(1A) the court may make an information order` ; `s 22B(2) the application has the content the subsection requires` ; `s 22B(3) the order requires the respondent to provide the information` ; `s 22B(3) the respondent must provide the information the order requires` ; `s 22B(4) condition 1 is met` ; `s 22B(5) condition 2 is met` ; `s 22B(6) the request is an external request` ; `s 22B(6A) condition 3 is met` ; `s 22B(6B) condition 4 is met` ; `s 22B(7) the order has the content the subsection requires` ; `s 22B(8) the ceiling of the amount the court may order the person to pay` ; `s 22B(8) the magistrates court may order the person to pay an amount` ; `s 22B(9) the sum is treated as adjudged to be paid by a conviction of the court` ; `s 22B(12) the law enforcement officer shall not make an application unless senior or authorised` ; `s 22B(12) the officer is barred from making the application` ; `s 22B(13) the business is a business in the regulated sector` ; `s 22B(14) the act is terrorist financing` ; `s 22B(14) the body is a foreign FIU` ; `s 22B(14) the function is the criminal intelligence function` ; `s 22B(14) the offence is a corresponding terrorist financing offence` ; `s 22B(14) the person is a law enforcement officer` ; `s 22B(14) the person is a senior law enforcement officer` ; `s 22B(14) the person is an authorised NCA officer` ; `s 22B(14) the place is a foreign country` ; `s 22B(14) the requirement is a corresponding disclosure requirement` |
| 429 | s 22B(1) | subsection | encoded | `s 22B(1) the court may make an information order` |
| 430 | s 22B(1A) | subsection | encoded | `s 22B(1A) the court may make an information order` |
| 431 | s 22B(1A)(a) | paragraph | encoded | `s 22B(1A) the court may make an information order` |
| 432-433 | s 22B(1A)(b) | paragraph | encoded | `s 22B(1A) the court may make an information order` |
| 434 | s 22B(2) | subsection | encoded | `s 22B(2) the application has the content the subsection requires` |
| 435 | s 22B(2)(a) | paragraph | encoded | `s 22B(2) the application has the content the subsection requires` |
| 436 | s 22B(2)(b) | paragraph | encoded | `s 22B(2) the application has the content the subsection requires` |
| 436 | s 22B(2)(b) term “the respondent” | term | encoded | `s 22B(2) the application has the content the subsection requires` |
| 437 | s 22B(3) | subsection | encoded | `s 22B(3) the order requires the respondent to provide the information` ; `s 22B(3) the respondent must provide the information the order requires` |
| 438 | s 22B(3)(a) | paragraph | encoded | `s 22B(3) the order requires the respondent to provide the information` ; `s 22B(3) the respondent must provide the information the order requires` |
| 439-440 | s 22B(3)(b) | paragraph | encoded | `s 22B(3) the order requires the respondent to provide the information` ; `s 22B(3) the respondent must provide the information the order requires` |
| 441 | s 22B(4) | subsection | encoded | `s 22B(4) condition 1 is met` |
| 442 | s 22B(4)(a) | paragraph | encoded | `s 22B(4) condition 1 is met` |
| 443 | s 22B(4)(b) | paragraph | encoded | `s 22B(4) condition 1 is met` |
| 444 | s 22B(4)(c) | paragraph | encoded | `s 22B(4) condition 1 is met` |
| 445 | s 22B(4)(c)(i) | sub-paragraph | encoded | `s 22B(4) condition 1 is met` |
| 446 | s 22B(4)(c)(ii) | sub-paragraph | encoded | `s 22B(4) condition 1 is met` |
| 447 | s 22B(4)(d) | paragraph | encoded | `s 22B(4) condition 1 is met` |
| 448 | s 22B(5) | subsection | encoded | `s 22B(5) condition 2 is met` |
| 449 | s 22B(5)(a) | paragraph | encoded | `s 22B(5) condition 2 is met` |
| 450 | s 22B(5)(b) | paragraph | encoded | `s 22B(5) condition 2 is met` |
| 451 | s 22B(5)(c) | paragraph | encoded | `s 22B(5) condition 2 is met` |
| 452 | s 22B(5)(d) | paragraph | encoded | `s 22B(5) condition 2 is met` |
| 453 | s 22B(5)(e) | paragraph | encoded | `s 22B(5) condition 2 is met` |
| 454 | s 22B(6) | subsection | encoded | `s 22B(6) the request is an external request` |
| 454 | s 22B(6) term “external request” | term | encoded | `s 22B(6) the request is an external request` |
| 455 | s 22B(6A) | subsection | encoded | `s 22B(6A) condition 3 is met` |
| 456 | s 22B(6A)(a) | paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 457 | s 22B(6A)(a)(i) | sub-paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 458-459 | s 22B(6A)(a)(ii) | sub-paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 460 | s 22B(6A)(b) | paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 461 | s 22B(6A)(c) | paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 462 | s 22B(6A)(d) | paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 463 | s 22B(6A)(d)(i) | sub-paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 464 | s 22B(6A)(d)(ii) | sub-paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 465 | s 22B(6A)(e) | paragraph | encoded | `s 22B(6A) condition 3 is met` |
| 466 | s 22B(6B) | subsection | encoded | `s 22B(6B) condition 4 is met` |
| 467 | s 22B(6B)(a) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 468 | s 22B(6B)(b) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 469 | s 22B(6B)(b)(i) | sub-paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 470-471 | s 22B(6B)(b)(ii) | sub-paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 472 | s 22B(6B)(c) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 473 | s 22B(6B)(d) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 474 | s 22B(6B)(e) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 475 | s 22B(6B)(f) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 476 | s 22B(6B)(f)(i) | sub-paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 477 | s 22B(6B)(f)(ii) | sub-paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 478 | s 22B(6B)(g) | paragraph | encoded | `s 22B(6B) condition 4 is met` |
| 479 | s 22B(7) | subsection | encoded | `s 22B(7) the order has the content the subsection requires` |
| 480 | s 22B(7)(a) | paragraph | encoded | `s 22B(7) the order has the content the subsection requires` |
| 481 | s 22B(7)(b) | paragraph | encoded | `s 22B(7) the order has the content the subsection requires` |
| 482 | s 22B(8) | subsection | encoded | `s 22B(8) the ceiling of the amount the court may order the person to pay` ; `s 22B(8) the magistrates court may order the person to pay an amount` |
| 483 | s 22B(9) | subsection | encoded | `s 22B(9) the sum is treated as adjudged to be paid by a conviction of the court` |
| 484 | s 22B(10) | subsection | inert | reason 2: power to substitute another sum by regulations: the figure it would change is an input to s 22B(8); stated gap: the text names the Secretary of State as the one who may substitute another sum, by regulations made by statutory instrument; the encoding takes the substituted sum as an input to s 22B(8) and has no function for who may change it |
| 485 | s 22B(11) | subsection | inert | reason 2: annulment procedure for regulations |
| 486 | s 22B(12) | subsection | encoded | `s 22B(12) the law enforcement officer shall not make an application unless senior or authorised` ; `s 22B(12) the officer is barred from making the application` |
| 487 | s 22B(13) | subsection | encoded | `s 22B(13) the business is a business in the regulated sector` |
| 488 | s 22B(14) | subsection | encoded | `s 22B(14) the act is terrorist financing` ; `s 22B(14) the body is a foreign FIU` ; `s 22B(14) the function is the criminal intelligence function` ; `s 22B(14) the offence is a corresponding terrorist financing offence` ; `s 22B(14) the person is a law enforcement officer` ; `s 22B(14) the person is a senior law enforcement officer` ; `s 22B(14) the person is an authorised NCA officer` ; `s 22B(14) the place is a foreign country` ; `s 22B(14) the requirement is a corresponding disclosure requirement` |
| 489 | s 22B(14) “authorised NCA officer” | definition | encoded | `s 22B(14) the person is an authorised NCA officer` |
| 490 | s 22B(14) “corresponding disclosure requirement” | definition | encoded | `s 22B(14) the requirement is a corresponding disclosure requirement` |
| 491 | s 22B(14) “corresponding terrorist financing offence” | definition | fork | F7 ; `s 22B(14) the offence is a corresponding terrorist financing offence` |
| 492 | s 22B(14) “the criminal intelligence function” | definition | encoded | `s 22B(14) the function is the criminal intelligence function` |
| 493 | s 22B(14) “foreign country” | definition | encoded | `s 22B(14) the place is a foreign country` |
| 494 | s 22B(14) “foreign FIU” | definition | encoded | `s 22B(14) the body is a foreign FIU` |
| 495 | s 22B(14) “law enforcement officer” | definition | encoded | `s 22B(14) the person is a law enforcement officer` |
| 496 | s 22B(14) “law enforcement officer” item 1 | item | encoded | `s 22B(14) the person is a law enforcement officer` |
| 497 | s 22B(14) “law enforcement officer” item 2 | item | encoded | `s 22B(14) the person is a law enforcement officer` |
| 498 | s 22B(14) “law enforcement officer” item 3 | item | encoded | `s 22B(14) the person is a law enforcement officer` |
| 499 | s 22B(14) “law enforcement officer” item 4 | item | encoded | `s 22B(14) the person is a law enforcement officer` |
| 500 | s 22B(14) “senior law enforcement officer” | definition | encoded | `s 22B(14) the person is a senior law enforcement officer` |
| 501 | s 22B(14) “senior law enforcement officer” item 1 | item | encoded | `s 22B(14) the person is a senior law enforcement officer` |
| 502 | s 22B(14) “senior law enforcement officer” item 2 | item | encoded | `s 22B(14) the person is a senior law enforcement officer` |
| 503 | s 22B(14) “senior law enforcement officer” item 3 | item | encoded | `s 22B(14) the person is a senior law enforcement officer` |
| 504 | s 22B(14) “terrorist financing” | definition | fork | F7 ; `s 22B(14) the act is terrorist financing` |
| 505 | s 22B(14) “terrorist financing” item 1 | item | fork | F7 ; `s 22B(14) the act is terrorist financing` |
| 506 | s 22B(14) “terrorist financing” item 2 | item | fork | F7 ; `s 22B(14) the act is terrorist financing` |
| 507 | s 22C | section | encoded | `s 22C(1) the statement may not be used in evidence against the person` ; `s 22C(2) subsection (1) does not apply` ; `s 22C(3) the statement may not be used by virtue of subsection (2)(c)` ; `s 22C(4) the prosecution is a prosecution for perjury` |
| 508 | s 22C(1) | subsection | encoded | `s 22C(1) the statement may not be used in evidence against the person` |
| 509 | s 22C(2) | subsection | encoded | `s 22C(2) subsection (1) does not apply` |
| 510 | s 22C(2)(a) | paragraph | encoded | `s 22C(2) subsection (1) does not apply` |
| 511 | s 22C(2)(b) | paragraph | encoded | `s 22C(2) subsection (1) does not apply` |
| 512 | s 22C(2)(c) | paragraph | encoded | `s 22C(2) subsection (1) does not apply` |
| 513 | s 22C(3) | subsection | encoded | `s 22C(3) the statement may not be used by virtue of subsection (2)(c)` |
| 514 | s 22C(3)(a) | paragraph | encoded | `s 22C(3) the statement may not be used by virtue of subsection (2)(c)` |
| 515-516 | s 22C(3)(b) | paragraph | encoded | `s 22C(3) the statement may not be used by virtue of subsection (2)(c)` |
| 517 | s 22C(4) | subsection | encoded | `s 22C(4) the prosecution is a prosecution for perjury` |
| 518 | s 22C(4)(a) | paragraph | encoded | `s 22C(4) the prosecution is a prosecution for perjury` |
| 519 | s 22C(4)(b) | paragraph | encoded | `s 22C(4) the prosecution is a prosecution for perjury` |
| 520 | s 22D | section | encoded | `s 22D(1) an appeal lies to the relevant appeal court` ; `s 22D(2) the person may bring the appeal` ; `s 22D(3) the relevant appeal court` ; `s 22D(4) the relevant appeal court may make, discharge or vary the order` |
| 521 | s 22D(1) | subsection | encoded | `s 22D(1) an appeal lies to the relevant appeal court` |
| 522 | s 22D(2) | subsection | encoded | `s 22D(2) the person may bring the appeal` |
| 523 | s 22D(3) | subsection | encoded | `s 22D(3) the relevant appeal court` |
| 523 | s 22D(3) term “relevant appeal court” | term | encoded | `s 22D(3) the relevant appeal court` |
| 524 | s 22D(3)(a) | paragraph | encoded | `s 22D(3) the relevant appeal court` |
| 525 | s 22D(3)(b) | paragraph | encoded | `s 22D(3) the relevant appeal court` |
| 526 | s 22D(3)(c) | paragraph | encoded | `s 22D(3) the relevant appeal court` |
| 527 | s 22D(4) | subsection | encoded | `s 22D(4) the relevant appeal court may make, discharge or vary the order` ; stated gap: s 22D gives no further appeal from the relevant appeal court (the Crown Court, a county court or the Sheriff Appeal Court); the text is silent, so no further appeal is encoded and none is invented |
| 528 | s 22D(4)(a) | paragraph | encoded | `s 22D(4) the relevant appeal court may make, discharge or vary the order` ; stated gap: s 22D gives no further appeal from the relevant appeal court (the Crown Court, a county court or the Sheriff Appeal Court); the text is silent, so no further appeal is encoded and none is invented |
| 529 | s 22D(4)(b) | paragraph | encoded | `s 22D(4) the relevant appeal court may make, discharge or vary the order` ; stated gap: s 22D gives no further appeal from the relevant appeal court (the Crown Court, a county court or the Sheriff Appeal Court); the text is silent, so no further appeal is encoded and none is invented |
| 530 | s 22E | section | encoded | `s 22E(1) the information order confers the right to require the information` ; `s 22E(2) the information is privileged information` ; `s 22E(3) the provision of the information does not breach any restriction on disclosure` ; `s 22E(4) the application may be heard and determined in private` |
| 531 | s 22E(1) | subsection | encoded | `s 22E(1) the information order confers the right to require the information` |
| 532 | s 22E(2) | subsection | encoded | `s 22E(2) the information is privileged information` |
| 532 | s 22E(2) term “Privileged information” | term | encoded | `s 22E(2) the information is privileged information` |
| 533 | s 22E(3) | subsection | encoded | `s 22E(3) the provision of the information does not breach any restriction on disclosure` |
| 534 | s 22E(4) | subsection | encoded | `s 22E(4) the application may be heard and determined in private` |
| 535 | s 22E(5) | subsection | inert | reason 2: rule-making power for the practice and procedure of the courts |
| 536 | s 22F | section | encoded | `s 22F(7) the failure of itself makes the person liable to criminal or civil proceedings` ; `s 22F(8) the code is admissible and is to be taken into account` ; `s 22F(10) the term has the meaning given in s 22B(14)` |
| 537 | s 22F(1) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice; stated gap: the text puts the duty to make the code on the Secretary of State; the code itself is not among the sources and no function for who makes it is encoded |
| 538 | s 22F(1)(a) | paragraph | inert | reason 2: machinery for making, laying and bringing into operation a code of practice; stated gap: the text puts the duty to make the code on the Secretary of State; the code itself is not among the sources and no function for who makes it is encoded |
| 539 | s 22F(1)(b) | paragraph | inert | reason 2: machinery for making, laying and bringing into operation a code of practice; stated gap: the text puts the duty to make the code on the Secretary of State; the code itself is not among the sources and no function for who makes it is encoded |
| 540 | s 22F(2) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 541 | s 22F(2)(a) | paragraph | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 542 | s 22F(2)(b) | paragraph | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 543 | s 22F(2)(c) | paragraph | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 544 | s 22F(3) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 545 | s 22F(4) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 546 | s 22F(5) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice; stated gap: "When the Secretary of State has laid a draft of the code before Parliament the Secretary of State may bring it into operation by regulations" is a "when", read as "where" (ruling of 2026-11-05, (c)): with no draft laid the answer would be JUST FALSE; no function is encoded because the machinery is inert (F12, F23) |
| 547 | s 22F(6) | subsection | inert | reason 2: machinery for making, laying and bringing into operation a code of practice |
| 548 | s 22F(7) | subsection | encoded | `s 22F(7) the failure of itself makes the person liable to criminal or civil proceedings` |
| 549 | s 22F(8) | subsection | encoded | `s 22F(8) the code is admissible and is to be taken into account` |
| 550 | s 22F(9) | subsection | inert | reason 2: power to combine two codes of practice |
| 551 | s 22F(10) | subsection | encoded | `s 22F(10) the term has the meaning given in s 22B(14)` |
| 551 | s 22F(10) term “authorised NCA officer” | term | encoded | `s 22F(10) the term has the meaning given in s 22B(14)` |
| 552 | heading: Forfeiture | heading | inert | reason 1: heading |
| 553 | s 23 | section | fork | F7 ; `s 23(1) the court may make a forfeiture order` ; `s 23(2) the court may order the forfeiture of the property` ; `s 23(2) the property is within the subsection` ; `s 23(3) the court may order the forfeiture of the property` ; `s 23(4) the court may order the forfeiture of the property` ; `s 23(5) the court may order the forfeiture of the property` ; `s 23(5A) the court may order the forfeiture of the amount` ; `s 23(6) the court may order the forfeiture of the property` ; `s 23(7) the court may order the forfeiture of the payment or reward` |
| 554 | s 23(1) | subsection | fork | F7 ; `s 23(1) the court may make a forfeiture order` |
| 555 | s 23(2) | subsection | encoded | `s 23(2) the court may order the forfeiture of the property` ; `s 23(2) the property is within the subsection` |
| 556 | s 23(2)(a) | paragraph | encoded | `s 23(2) the court may order the forfeiture of the property` ; `s 23(2) the property is within the subsection` |
| 557 | s 23(2)(b) | paragraph | encoded | `s 23(2) the court may order the forfeiture of the property` ; `s 23(2) the property is within the subsection` |
| 558 | s 23(3) | subsection | encoded | `s 23(3) the court may order the forfeiture of the property` |
| 559 | s 23(3)(a) | paragraph | encoded | `s 23(3) the court may order the forfeiture of the property` |
| 560 | s 23(3)(b) | paragraph | encoded | `s 23(3) the court may order the forfeiture of the property` |
| 561 | s 23(4) | subsection | encoded | `s 23(4) the court may order the forfeiture of the property` |
| 562 | s 23(4)(a) | paragraph | encoded | `s 23(4) the court may order the forfeiture of the property` |
| 563 | s 23(4)(b) | paragraph | encoded | `s 23(4) the court may order the forfeiture of the property` |
| 564 | s 23(5) | subsection | encoded | `s 23(5) the court may order the forfeiture of the property` |
| 565 | s 23(5)(a) | paragraph | encoded | `s 23(5) the court may order the forfeiture of the property` |
| 566 | s 23(5)(b) | paragraph | encoded | `s 23(5) the court may order the forfeiture of the property` |
| 567 | s 23(5A) | subsection | encoded | `s 23(5A) the court may order the forfeiture of the amount` |
| 568 | s 23(6) | subsection | encoded | `s 23(6) the court may order the forfeiture of the property` |
| 569 | s 23(7) | subsection | fork | F7 ; `s 23(7) the court may order the forfeiture of the payment or reward` |
| 570 | s 23A | section | encoded | `s 23A(1) the court may order the forfeiture of the property` ; `s 23A(2) this section applies to the offence` ; `s 23A(3) this section applies to the ancillary offence` ; `s 23A(4) this section applies to the offence with a terrorist connection` ; `s 23A(6) the order adding the offence to subsection (2) applies to the offence` |
| 571 | s 23A(1) | subsection | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 572 | s 23A(1)(a) | paragraph | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 573 | s 23A(1)(b) | paragraph | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 574 | s 23A(1)(b)(i) | sub-paragraph | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 575 | s 23A(1)(b)(ii) | sub-paragraph | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 576 | s 23A(1)(b)(iii) | sub-paragraph | encoded | `s 23A(1) the court may order the forfeiture of the property` |
| 577 | s 23A(2) | subsection | encoded | `s 23A(2) this section applies to the offence` |
| 578 | s 23A(2)(a) | paragraph | encoded | `s 23A(2) this section applies to the offence` |
| 579 | s 23A(2)(a) item 1 | item | encoded | `s 23A(2) this section applies to the offence` |
| 580 | s 23A(2)(a) item 2 | item | encoded | `s 23A(2) this section applies to the offence` |
| 581 | s 23A(2)(a) item 3 | item | encoded | `s 23A(2) this section applies to the offence` |
| 582 | s 23A(2)(a) item 4 | item | encoded | `s 23A(2) this section applies to the offence` |
| 583 | s 23A(2)(b) | paragraph | encoded | `s 23A(2) this section applies to the offence` |
| 584 | s 23A(2)(b) item 1 | item | encoded | `s 23A(2) this section applies to the offence` |
| 585 | s 23A(2)(b) item 2 | item | encoded | `s 23A(2) this section applies to the offence` |
| 586 | s 23A(2)(b) item 3 | item | encoded | `s 23A(2) this section applies to the offence` |
| 587 | s 23A(2)(b) item 4 | item | encoded | `s 23A(2) this section applies to the offence` |
| 588 | s 23A(3) | subsection | encoded | `s 23A(3) this section applies to the ancillary offence` |
| 589 | s 23A(4) | subsection | encoded | `s 23A(4) this section applies to the offence with a terrorist connection` |
| 590 | s 23A(4)(a) | paragraph | encoded | `s 23A(4) this section applies to the offence with a terrorist connection` |
| 591 | s 23A(4)(b) | paragraph | encoded | `s 23A(4) this section applies to the offence with a terrorist connection` |
| 592 | s 23A(5) | subsection | inert | reason 2: power to amend the list of offences in subsection (2) by order; stated gap: the text lets the Secretary of State amend subsection (2) by order; the list in subsection (2) is encoded as it stands and no function for who may change it is encoded |
| 593 | s 23A(6) | subsection | encoded | `s 23A(6) the order adding the offence to subsection (2) applies to the offence` |
| 594 | s 23B | section | encoded | `s 23B(1) the court must give an opportunity to be heard` ; `s 23B(1) the court must give the person an opportunity to be heard` ; `s 23B(2) the court must have regard to the value and effects` ; `s 23B(2) the court shall have regard to the value of the property and the effects on the convicted person` ; `s 23B(3) the court in Scotland is barred from making the order` ; `s 23B(3) the court in Scotland shall not make the order except on the prosecutor's application` ; `s 23B(3) the order of a Scottish court is a sentence for the purposes of any appeal or review` ; `s 23B(4) Schedule 4 makes further provision for the order` |
| 595 | s 23B(1) | subsection | encoded | `s 23B(1) the court must give an opportunity to be heard` ; `s 23B(1) the court must give the person an opportunity to be heard` |
| 596 | s 23B(2) | subsection | encoded | `s 23B(2) the court must have regard to the value and effects` ; `s 23B(2) the court shall have regard to the value of the property and the effects on the convicted person` |
| 597 | s 23B(2)(a) | paragraph | encoded | `s 23B(2) the court must have regard to the value and effects` ; `s 23B(2) the court shall have regard to the value of the property and the effects on the convicted person` |
| 598 | s 23B(2)(b) | paragraph | encoded | `s 23B(2) the court must have regard to the value and effects` ; `s 23B(2) the court shall have regard to the value of the property and the effects on the convicted person` |
| 599 | s 23B(3) | subsection | encoded | `s 23B(3) the court in Scotland is barred from making the order` ; `s 23B(3) the court in Scotland shall not make the order except on the prosecutor's application` ; `s 23B(3) the order of a Scottish court is a sentence for the purposes of any appeal or review` |
| 600 | s 23B(3)(a) | paragraph | encoded | `s 23B(3) the court in Scotland is barred from making the order` ; `s 23B(3) the court in Scotland shall not make the order except on the prosecutor's application` ; `s 23B(3) the order of a Scottish court is a sentence for the purposes of any appeal or review` |
| 601-602 | s 23B(3)(b) | paragraph | encoded | `s 23B(3) the court in Scotland is barred from making the order` ; `s 23B(3) the court in Scotland shall not make the order except on the prosecutor's application` ; `s 23B(3) the order of a Scottish court is a sentence for the purposes of any appeal or review` |
| 603 | s 23B(4) | subsection | encoded | `s 23B(4) Schedule 4 makes further provision for the order` ; stated gap: Schedule 4, which s 23B(4) says makes further provision in relation to forfeiture orders under s 23 or 23A, is not among the sources, so what it contains is not encoded |
| 604 | heading: Seizure of terrorist cash | heading | inert | reason 1: heading |
| 605 | s 24 | repealed | repealed | blank in this text |
| 606 | s 25 | repealed | repealed | blank in this text |
| 607 | s 26 | repealed | repealed | blank in this text |
| 608 | s 27 | repealed | repealed | blank in this text |
| 609 | s 28 | repealed | repealed | blank in this text |
| 610 | s 29 | repealed | repealed | blank in this text |
| 611 | s 30 | repealed | repealed | blank in this text |
| 612 | s 31 | repealed | repealed | blank in this text |

<!-- COVERAGE:END -->

## Dependencies

No other row's code is imported; `IMPORT` finds only modules beside it and no module of another subject is among the sources.
Each entry below is an Act or instrument the deposited text borrows from and that is not among the sources (status "not staged"); the encoding names it as an input, to be filled later.
The same list, with the line numbers of the borrowing provisions in the deposited text, is the `dependencies` key of `encoding.json`.

- **Terrorism Act 2000, Schedule 3A (what a business in the regulated sector, a credit institution, a financial institution and a supervisory authority are).** Status: named input; to fill later (from: not staged). Taken as an input: whether the information came in the course of a business in the regulated sector, and whether a person is a credit institution, a financial institution or a supervisory authority, each stated as a fact; in the seat, the regulated-sector fact in the question about what to tell and to whom can be answered "I am not sure", which is NOTHING. Borrowing provisions: s 19(7A) (line 80); s 21A(10) (line 172); s 21B(6) (line 197); s 21CF(3) (line 325); s 21CF(6)(e) (line 333); s 21H(1) (lines 407, 409); s 22B(13) (line 487).
- **Terrorism Act 2000, Parts I and II (the meaning of "terrorism" and of "proscribed organisation").** Status: named input; to fill later (from: not staged). Taken as an input: whether property is likely to be used for the purposes of terrorism, is the proceeds of acts of terrorism, or belongs to a proscribed organisation, each stated as a fact. Borrowing provisions: s 14(1) (lines 4, 5, 6, 7); s 15 (lines 15, 18, 21); s 16 (lines 24, 27); s 17 (line 31); s 17A(1)(b) (line 35); s 22B(14) (lines 486, 498); s 23(2) to (7) (lines 556, 559, 562, 565, 570); s 23A(1) and (2) (lines 574, 575, 576, 580, 582, 586).
- **Banking and Financial Dealings Act 1971 (bank holidays) and the date of Good Friday.** Status: named input; to fill later (from: not staged). Taken as an input: one list of dates, asked of the person (Saturdays, Sundays and Christmas Day are computed from the calendar). Borrowing provisions: s 21ZA(4) (line 122).
- **The statutory maximum and level 5 on the standard scale (amounts of fines).** Status: named input; to fill later (from: not staged). Taken as an input: the amount of the fine, as a number the person states; penalties are always ceilings. Borrowing provisions: s 19(8)(b) (line 84); s 21A(12)(b) (line 180); s 21D(4)(a) (line 359); s 22(b) (line 419).
- **Directive 2002/87/EC (the meaning of "group").** Status: named input; to fill later (from: not staged). Taken as an input: whether two institutions belong to the same group, stated as a fact. Borrowing provisions: s 21E(3) (line 371).
- **Directive 2015/849/EU ("equivalent money laundering requirements").** Status: named input; to fill later (from: not staged). Taken as an input: whether a country or territory imposes equivalent money laundering requirements, stated as a fact. Borrowing provisions: s 21F(2)(c) (line 388); s 21H(4) (line 412).
- **The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (who is a person's supervisory authority).** Status: named input; to fill later (from: not staged). Taken as an input: whether the disclosure is to the authority that is the person's supervisory authority, stated as a fact. Borrowing provisions: s 21G(1)(a) (line 392).
- **Proceeds of Crime Act 2002 (section 412, legal privilege in Scotland; investigations and court orders under that Act; section 339ZL, a combined code of practice).** Status: named input; to fill later (from: not staged). Taken as an input: whether the information would be privileged, and whether a disclosure is for an investigation or order under that Act, each stated as a fact. Borrowing provisions: s 21G(1)(b)(ii), (iii) (lines 396, 397); s 22E(2) (line 532); s 22F(9) (line 550).
- **Crime and Courts Act 2013, section 1(5) (the criminal intelligence function).** Status: named input; to fill later (from: not staged). Taken as an input: whether the provision of information is for the purposes of the criminal intelligence function, stated as a fact. Borrowing provisions: s 22B(14) (line 492).
- **Counter-Terrorism Act 2008, sections 30, 31 and 94, and the Sentencing Code, section 69 (ancillary offences; a terrorist connection).** Status: named input; to fill later (from: not staged). Taken as an input: whether an offence is an ancillary offence, and whether a court has determined or proved that an offence has a terrorist connection, each stated as a fact. Borrowing provisions: s 23A(3) (line 588); s 23A(4) (lines 590, 591).
- **Terrorism Act 2000, Schedule 4 (further provision in relation to forfeiture orders).** Status: named input; to fill later (from: not staged). Taken as an input: nothing: what Schedule 4 provides is not encoded (a stated gap under the coverage row for s 23B(4)). Borrowing provisions: s 23B(4) (line 603).

The Interpretation Act 1978 is not among the sources (Commons holds a row for it that targets unstable, which a main build cannot read).
Part III counts two periods from an event, and the text counts both itself (7 working days, s 21ZA(3); 28 days, s 21CC(7)(b)); no other period in the deposited text is counted in months or years, so nothing was taken from that Act.
To fill later: the Act's rules of reading ("he" includes "she"; "person") are assumed and not encoded.

## Unstable dialect

I looked at time (the periods counted from events in ss 21ZA and 21CC; no rule in the deposited text applies on different dates, and the text is a single point-in-time version of 2026-07-08), at versions (the converter's caveat that the revised text may carry several extent versions and prospective provisions it does not distinguish; I had no way to tell them apart from this text) and at workarounds (the one on main is a holiday list for working days; plain `Date` arithmetic and a list input need no dialect feature), and found no shape that earned a second encoding; I did not run the unstable build.

## What the main binary does not accept

Loud (an error that teaches) and silent (a wrong answer with a clean exit), sorted that way because the silent ones cost more.

**Silent.**
- `NOT a OR b` parses as `NOT (a OR b)`. I hit it: the all-true test for s 21CC(5) failed until every `NOT` was parenthesised. A probe on 1.6.109 confirmed it (`NOT a OR b` with a and b both true answers FALSE). Every `NOT` in the modules is now parenthesised.
- `check.sh` counts assertion lines and error diagnostics only. It does not see a different `#TRACE` outcome. I ran all 14 `#TRACE`s on 1.6.109 and 1.6.108 and read both outcomes: they agree (see below).
- `#ASSERT REFUSED ... BECAUSE` parsed on 1.6.109 (a probe printed "expected a refusal, but the expression produced a value") and is rejected on 1.6.108 ("unexpected BECAUSE"). The brief says it is not available on main, and this encoding uses none of it.
- `YMD` is defined in `daydate` on 1.6.109 and is not defined on 1.6.108 (probe: "I could not find a definition"). I use `Date day month year` throughout, which both builds read the same way.

**Loud.**
- A deontic value cannot be compared: `#ASSERT r EQUALS r` on a `DEONTIC` answers "Trying to check equality on types that do not support it". So the regulative rules (`PARTY ... MUST/MAY/SHANT ... HENCE ... LEST ...`) are run with `#TRACE`, whose outcome (FULFILLED, BREACH, or the residual obligation) I read by eye, and each duty is also encoded as a decision function over the facts, which is asserted. There are 14 traces: 8 end FULFILLED; 4 end in a BREACH (s 22B(3) with the date passed, s 22B(12), s 21CE(2) and s 23B(3)); 2 leave the obligation standing because the event in the trace is by another party (s 19(2) and s 21CE(2)).
- A constructor named like a keyword fails to parse (`A`, `B`, `AT`, `IN`, `OF`): "unexpected A". I renamed such constructors.
- A function argument named like a constructor clashes, so regulative rules in this encoding use no `GIVEN` named `the person`.
- A name the prelude owns cannot be reused (`either`).
- A `§§` title that contains `?` must be backticked.
- Not used because the brief and the dialect notes say main does not take them: sets, `EVERY`, `TYPICALLY`, `AFTER ... WITHIN`. Plain `WITHIN n` works and is used. None of these was re-measured here beyond the probes above.

## What `check.sh` prints

Run from this folder as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` with `JL4_LIBRARY_PATH` unset, target `main`.
No earlier encoding of this row existed, so no earlier `check.sh` numbers were replaced.
This session's own earlier full runs were 19 modules and 861 assertions satisfied when layer 1 was complete, and 21 modules and 1,031 before the s 19(1A) question and the Christmas notice-period case were added; the run just before Meng's ruling of 2026-11-05 was applied was 21 modules and 1,034 assertions.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ta-cases-seat.l4                               0       181       0        0         0 |      0       181       0        0  same
ta-disclosure.l4                               0         0       0        0         0 |      0         0       0        0  same
ta-forfeiture.l4                               0         0       0        0         0 |      0         0       0        0  same
ta-information-orders.l4                       0         0       0        0         0 |      0         0       0        0  same
ta-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
ta-logic.l4                                    0         0       0        0         0 |      0         0       0        0  same
ta-nouns.l4                                    0         0       0        0         0 |      0         0       0        0  same
ta-offences.l4                                 0         0       0        0         0 |      0         0       0        0  same
ta-regulated-sector.l4                         0         0       0        0         0 |      0         0       0        0  same
ta-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
ta-tests-disclosure.l4                         0       172       0        0         0 |      0       172       0        0  same
ta-tests-forfeiture.l4                         0        83       0        0         0 |      0        83       0        0  same
ta-tests-information-orders.l4                 0       134       0        0         0 |      0       134       0        0  same
ta-tests-interpretation.l4                     0        19       0        0         0 |      0        19       0        0  same
ta-tests-logic.l4                              0        23       0        0         0 |      0        23       0        0  same
ta-tests-offences.l4                           0        72       0        0         0 |      0        72       0        0  same
ta-tests-regulated-sector.l4                   0        90       0        0         0 |      0        90       0        0  same
ta-tests-tipping-off.l4                        0        85       0        0         0 |      0        85       0        0  same
ta-tests-voluntary-disclosure.l4               0       195       0        0         0 |      0       195       0        0  same
ta-tipping-off.l4                              0         0       0        0         0 |      0         0       0        0  same
ta-voluntary-disclosure.l4                     0         0       0        0         0 |      0         0       0        0  same
TOTAL (21 modules)                             0      1054       0        0           |      0      1054       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

All 14 `#TRACE` outcomes were also read on both builds by hand, and they are the same.
Total: the 1,054 assertions are 873 in the layer-1 tests and 181 in the seat cases, and none fails or is refused.

## What would need doing before this encoding is worth relying on

1. A lawyer who knows the Terrorism Act 2000 should read every row of "Marginal readings for a lawyer", above all the failed "if" reading (a), and the forks F1, F2, F3, F7, F12, F13 and F14, and the open questions F19 to F22 on which a reviewer expected `JUST FALSE`.
2. Someone should check the converter's text against the official text: the converter notes that it may carry more than one extent version and prospective provisions it does not mark, and this encoding cannot tell them apart.
3. Schedule 3A, the Banking and Financial Dealings Act 1971 and the standard scale should be added (or each input should be backed by an authority) so that the seat's borrowed facts are not left to the person.
4. The seat should be tried on real users: the wording of each `@desc` has not been tested on anyone.
5. Conditions 2 to 4 of s 22B, s 22C(2), s 23A and ss 23B(2), (3) have no seat question; a seat for the National Crime Agency and for courts is deliberately not built.
6. The seat's offence questions do not apply the defences and protections; a person must ask both. If Commons wants one combined answer that is E1 option B across sections, and that is Meng's call, not this encoding's.
7. The unstable dialect might express the notice period and the 28-day period better; I did not look beyond the sections named under "Unstable dialect".

## Files

- Layer 1: `ta-nouns.l4`, `ta-logic.l4`, `ta-interpretation.l4`, `ta-offences.l4`, `ta-disclosure.l4`, `ta-regulated-sector.l4`, `ta-voluntary-disclosure.l4`, `ta-tipping-off.l4`, `ta-information-orders.l4`, `ta-forfeiture.l4`, with `ta-tests-logic.l4`, `ta-tests-interpretation.l4`, `ta-tests-offences.l4`, `ta-tests-disclosure.l4`, `ta-tests-regulated-sector.l4`, `ta-tests-voluntary-disclosure.l4`, `ta-tests-tipping-off.l4`, `ta-tests-information-orders.l4`, `ta-tests-forfeiture.l4`.
- Layer 2: `ta-seat.l4`, `ta-cases-seat.l4`.
- Tools and data: `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`, `coverage.py`, `coverage-map.tsv`, `jural.tsv`.
- Records: `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.
