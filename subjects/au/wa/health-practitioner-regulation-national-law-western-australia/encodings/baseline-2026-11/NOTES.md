# Health Practitioner Regulation National Law (Western Australia) — baseline encoding, the notifier's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the laws behind compensation and other civil claims, here under medical negligence and health: the provisions a person harmed by a health practitioner meets when raising it with the regulator, alongside (or after settling) a negligence claim. The National Law is large (about 540,000 characters), so the Parts the focus needs are encoded and the rest is listed below. There was no earlier encoding of the National Law as applied in Western Australia to keep. No ledger entry was open for it.

The list this run worked from named the "Health Practitioner Regulation National Law (WA) Act 2010". That Act was repealed by the Health Practitioner Regulation National Law Application Act 2024 (WA) s 38; since 15 May 2024 the National Law applies in Western Australia under the 2024 Act, and the law a notifier meets is the National Law itself. So the encoding sits under `health-practitioner-regulation-national-law-western-australia`, and uses the 2024 Act for its Western Australian modifications (ss 19, 27, 28).

There are 21 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Law's order of events:

- can a notification be made about this person (ss 138–139B);
- can I make a voluntary notification (ss 144, 145);
- must Ahpra help me, and is my notification properly made (ss 146, 147);
- was someone else required to notify (ss 140–143; arises only where a practitioner, employer or education provider knew);
- by when must the Board assess it, and did it (s 149); will the health complaints entity be told (s 150); can the Board take no further action (s 151); will the practitioner be told (s 152);
- what I must or may be told at each later stage, by when I must next hear how an investigation is going, by when for a panel decision, and can I make a submission to a panel (ss 159A, 161(3), 167A, 177A, 180, 187, 189, 192; arises only once something has been decided);
- did the practitioner have to be insured, and by when must a lapse be reported (ss 129, 130);
- my protection from liability (s 237), from reprisals and the most the reprisal can be fined (s 237A), and from confidentiality clauses, with the offence of entering one without the carve-out (s 237B).

**Regulative rules.** Three duties the Law states in days are written as `PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE`: the Board's preliminary assessment within 60 days of receipt (s 149(1)); the Board's notice of a panel decision to the notifier within 30 days (s 192(2)(b)); the practitioner's notice to the Board within 7 days of becoming aware that indemnity insurance has lapsed (s 130(1), (3)(c)). Each period is written once, as a named deadline (`the s 149 assessment deadline for a notification received on`, `the s 192 notice deadline for a panel decision on`, `the s 130 insurance notice deadline from`), and both the seat questions and the rules' `WITHIN` use it. The seat questions take plain dates and give the last day; the case file asserts the rules through `CONSIDER EVALTRACE ... WHEN FULFILLED` (the last day, the day after, a period extended past a weekend, and an event that is not the duty's action).

Date arithmetic is kept in one small module, `hpnl-dates.l4`, the only one that imports `daydate`.

## Edition

The compilation of the Health Practitioner Regulation National Law (Western Australia) on the Western Australian Legislation website (mrdoc_49311), retrieved 7 September 2026, as deposited at `../../registers/source-bundle/mrdoc_49311.txt`. It is the Law as applied and modified by the Application Act 2024, with the Queensland amendments of 2022 (Act 22 of 2022) and 2025 (Act 6 of 2025) that have commenced in Western Australia; the last listed commencement is 10 April 2026. Sections 237A and 237B were inserted by Act 6 of 2025 (Qld) s 22, in Part 3 of that Act, which commenced on 1 December 2025 (compilation table). The Health Practitioner Regulation National Law Application Act 2024 (WA) is the compilation at mrdoc_49650 in `../../../health-practitioner-regulation-national-law-application-act-2024/registers/source-bundle/`.

The approved registration standards on professional indemnity insurance (which give "appropriate professional indemnity insurance arrangements" its content, s 5) and the national regulations are not deposited. No number this encoding uses is set by a regulation.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `hpnl-dates.l4`, `hpnl-notifier.l4` | `hpnl-cases-notifier.l4` | 136 written, 136 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text; weekdays were worked by hand from 1 January 2026 (a Thursday) and 1 January 2028 (a Saturday). Edges asserted: the 60th day after receipt and the 61st; a 60th day on a Saturday and on a Sunday (moved to Monday by Sch 7 cl 31(3)); a period running to 29 February 2028; the 30-day panel notice on a Saturday; the 7-day insurance notice from a Saturday and from a Monday; 3 months from 30 November running to 28 February (a Sunday, so 1 March); a student offence punishable by exactly 12 months and by 11; conduct on 1 December 2025 (the day ss 237A and 237B commenced) and on 30 November 2025; both limbs of s 151(1)(c) and (f) with one limb missing.

## Seat

**The notifier**: usually a patient, or a patient's family member, harmed by or worried about a registered health practitioner's care or conduct, who may also be bringing or settling a negligence claim. "Can I complain to Ahpra about my surgeon? Will the surgeon be told? By when must the Board look at it? Can my settlement's confidentiality clause stop me? Was the surgeon required to be insured?" A notifier who is a nurse or other employee asks the reprisal questions too. The National Law puts duties on practitioners, employers and education providers (mandatory notifications, insurance, reprisals, non-disclosure agreements); those duties are encoded for what they mean to the notifier. No second seat (the practitioner's) is written here; the Victorian Application Act's baseline (`subjects/au/vic/health-practitioner-regulation-national-law-victoria-act-2009/encodings/`) has a practitioner's seat over that Act only.

The 2026-10-18 defaults:

- **The Law alone**, with the 2024 Application Act for the WA modifications and the responsible tribunal (s 19: the State Administrative Tribunal). The registration standards, the health complaints entity's own Act (in WA the Health and Disability Services Complaints Act 1995), the Health Insurance Act 1973 (Cth) and the corresponding prior Acts are named, not encoded; what they decide is asked as a fact.
- **The actors the text names:** the notifier, the registered health practitioner, the student, the National Agency, the National Board, the health complaints entity, the employer, the education provider, the panel, a relevant person.
- **Judgments handed to others are answered conditionally:** "reasonably believes" (ss 141, 142, 143, 151, 152), "in good faith" (ss 237, 237A, 237B), "frivolous, vexatious, misconceived or lacking in substance", "not practicable", "not in the public interest", "dealt with adequately", "appropriate steps" (s 151), "leave of the panel" (s 187), "would also provide a ground for a complaint" (s 150) are inputs.
- **The Law's own definitions are worked out from facts:** "notifiable conduct" (s 140), "registered health practitioner" and "student" (s 5, and s 129(5)), "protected action" (s 237A(2)), "non-disclosure agreement" and "relevant person" (s 237B(3)), the s 144 grounds, the s 141(4) exceptions. "Impairment", "health complaints entity", "corresponding prior Act" and "appropriate professional indemnity insurance arrangements" are asked.
- **One case:** one notification about one practitioner or student.
- **The Law's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines ("notification" is glossed as a complaint, the National Agency as Ahpra).
- **Machinery out:** the Ministerial Council, Agency, Boards, accreditation, finance, regulations and transitional provisions.

## Scope

**In:** s 5 (the definitions the questions use); s 129; s 130(1), (2), (3) para (c) of "relevant event"; ss 138, 139 (named in an answer), 139A, 139B; Part 8 Divisions 2–4 (ss 140–143, with the WA s 141(4)(ca) and the deletion of ss 141(2A), 141A–141C by the Application Act ss 27, 28; ss 144–147); Division 5 ss 149(1), 150(1)–(4), 151(1)–(4), 152; the notifier's provisions in Divisions 7–11: ss 159A, 161(3)(b), (4), 167A, 177A, 180(1)(b), (2), 187, 189, 192(2)(b), (4); ss 237, 237A, 237B, with s 329 (the application of s 237B(1)); Schedule 7 cl 31(2), (3) for reckoning time; Application Act s 19.

**Out, and why:**

- Parts 1–7 except as above: the Ministerial Council, the Agency and Boards, accreditation, and registration (eligibility, applications, renewal, endorsement) are the practitioner's and the regulator's, not the notifier's. The title and practice protections (ss 113–123A, including WA's s 123A on birthing practices) concern unregistered or holding-out conduct; a claimant meets them, but they are a separate body of offences and are left to a later encoding. Advertising (s 133) likewise.
- s 130(3) paragraphs (a), (b), (d)–(i) of "relevant event" (charges, convictions, withdrawn hospital rights, Medicare disqualification, scheduled-medicine authority, a complaint to a s 219 entity, overseas registration) and the student's relevant events: s 130 is encoded only for the insurance lapse, the event that bears on whether a patient's claim has an insurer to meet it. The other events are the practitioner's reporting duties to the Board; the notifier learns nothing from them and cannot see whether they were given. They would each be the same 7-day rule with a different trigger.
- s 151(1A) (no further action on part of a notification whose subject matter the Board referred to another entity under s 150 or 150A): it turns on a referral the notifier does not control, and s 150A is out. The s 151 question asks about the notification as a whole; where the whole was referred, s 151(1)(e)(ii) answers it, and a referral of part only is not asked.
- Part 8 Division 5 ss 148, 149(2), (3), 149A, 149B, 150(5)–(8), 150A, and Divisions 6–14 apart from the notifier provisions: the Board's and the tribunal's procedure and powers (immediate action, interim prohibition orders, public statements, investigations, assessments, panels, the tribunal, appeals). The notifier is not a party to an appeal (s 199 gives appeal rights to the practitioner or student), so nothing there is the notifier's question.
- Parts 9–12 apart from ss 237–237B and s 329: finance, privacy, registers, the protection of persons exercising functions (s 236), inspectors, proceedings, regulations, the other transitional provisions.
- The rest of the Application Act 2024. Part 1 and Part 2 Divisions 1–2 (ss 1–17): commencement, application of the Law and the national regulations, tabling and disallowance; machinery. s 18 (generic terms such as "magistrate"): used by no question here. s 20 (the Act prevails over the Law): no inconsistency arises in the provisions encoded. s 21 (no double jeopardy): it limits punishment for an offence already punished in another participating jurisdiction; it would qualify the s 237A and s 237B(2) answers only where the same act was punished elsewhere, which is the offender's question, not the notifier's. s 22 (exclusion of WA legislation): machinery. Part 3 modifications other than ss 27, 28: s 24 (s 3A, objectives, wording only), s 25 (s 113, adds "physician" as a protected title) and s 26 (inserts s 123A, restricted birthing practices) are in the title and practice protections, out above; ss 29, 30 (ss 159B, 159P, Divisions 7A and 7B, refer to s 123A) are in unencoded Divisions; s 31 (a note to s 206, information about employment) is the Board's power; s 32 (deletes s 241A), s 33 (replaces s 242, proceedings for offences are summary and some may be begun at any time) and s 34 (deletes ss 246, 247) are about prosecuting offences, which the notifier does not do. Part 4: s 35 (police criminal history information) and s 37 (local regulations) are the regulator's; s 36 (review by the State Administrative Tribunal) concerns appeals, which s 199 gives to the practitioner or student, not the notifier. Part 5: s 38 repeals the 2010 Act (see above); ss 39–49 are transitional. Of these, s 42 matters to a notifier who notified before 15 May 2024: a notification pending under the former Law "continues and must be dealt with under the new Law as if it arose under the new Law" (s 42(2)), and things done under the former Law are taken to have been done under the new Law (s 42(4)). So the questions answer such a notification as if it were made under the Law now in force; that is not asked separately. Part 6: consequential amendments.

## Fork register (questions with no convention, decided case by case)

The 2026-11-04 and 2026-11-05 rulings were followed in choosing between "no" and `not covered`:

- s 139A for a former practitioner's behaviour after registration ended: `not covered` (a scope limit, "in relation to behaviour that occurred while the person was registered", with no "only"). The other reading: "no".
- s 139B(3) when no notification could have been made under the prior Act: "no" ("applies only to the extent").
- ss 138–139B for a person never registered: `not covered`; Part 8 Division 7A and Part 7 Division 10 deal with unregistered persons and are not encoded.
- s 144 when none of the listed grounds is believed: `not covered`. s 144 says a notification "may be made ... on any of the following grounds" without "only"; s 149(1)(b) leaves it to the Board to decide whether a notification relates to a ground. The other reading: "no", since s 145 permits only an entity that believes a ground exists.
- s 147 when help is not asked for and (2) does not apply: "not unless you ask" (s 147(1) "if asked").
- s 140 for conduct outside paragraphs (a)–(d): "no" (a "means" definition).
- s 141(1) for a belief formed outside the course of practising: "no" ("This section applies to a registered health practitioner who, in the course of practising ..., forms"), read as a "where" condition. The other reading: `not covered` (a scope limit with no "only").
- Division 2 for anyone not named in it (a patient, a relative, a manager who is not the employer): `not covered`. The other reading: "no", since a "mandatory notification" is one "an entity is required to make" under Division 2 and nobody else is required.
- s 142 for an employer and a student: "no" (s 142 speaks of "an employer of a registered health practitioner"; a student is excluded from that term by s 5).
- s 143 for an education provider and a practitioner who is not a student: `not covered`.
- s 150(1), (2) when their "if" fails: "no".
- s 151 when none of (a)–(f) holds: "no" ("may decide ... if"). s 150(6) (no further action while a health complaints entity deals with it) is not separately asked; it overlaps s 151(1)(e)(ii).
- s 152(3): "not necessarily" (the Board "is not required", which leaves it free to tell).
- s 129 for a student: "no" (the s 5 definition excludes a student); for a person not registered: "no"; while not practising: "no" (the duty is "must not practise unless").
- s 237 without good faith: "no" ("applies to a person who, in good faith").
- s 237A before 1 December 2025: `not covered`; s 237B(2) for an agreement made before 1 December 2025: "no" (a person cannot have contravened "must not enter into" before the duty existed).
- s 237B(1) for an agreement made before 1 December 2025: void like any other, because s 329 (inserted by the same Act, No. 6 of 2025 (Qld) s 23) applies s 237B(1) to an agreement "whether entered into before or after the commencement", and to conduct whether it "occurred before or after the commencement". Not a fork: the text settles it, so the question does not ask the date.
- s 237B(2) where several parties sign: the `@desc` asks for the first relevant person; each relevant person who enters the agreement commits the offence.
- s 161(3) "at not less than 3 monthly intervals": read as at least every 3 months, counted from the decision to investigate or the last notice, ending on the same day number 3 months on (or the last day of a shorter month) (finding 2).
- Sch 7 cl 31(3): only Saturdays and Sundays are moved past. Public holidays depend on "the place in which the thing is to be or may be done", which the Law does not fix for a National Board (finding 6).

## What the Law turns out to say

1. **In Western Australia a practitioner treating another practitioner never has to notify, whatever the conduct.** The Application Act 2024 s 27 inserts s 141(4)(ca) ("in the course of providing health services to the second health practitioner") and deletes s 141(2A), and s 28 deletes ss 141A–141C (the National Law's own provisions on treating practitioners; their text is not deposited, so what they would have required is not encoded). So a doctor who learns, while treating a colleague, of that colleague's sexual misconduct with patients is not required to notify in WA. The employer's duty (s 142) has no such exception. Asserted.
2. **A notifier has no right to be told the outcome at most stages, but must hear how an investigation is going.** After immediate action, an investigation or an assessment, the Board "may" inform the notifier (ss 159A, 167A, 177A). Only no further action (s 151(3): with the reason), action after show cause (s 180(1)(b): as soon as practicable) and a panel's decision (s 192(2)(b): within 30 days) must be notified, and even then the reasons are optional (ss 180(2), 192(4)), except for no further action. The Law names the notifier in no provision on a tribunal's decision. During an investigation the Board "must, at not less than 3 monthly intervals", give the notifier written notice of its progress (s 161(3)(b)); the s 161(4) exceptions (prejudice, risk) are for notices to the practitioner only, so the notifier's notices have none. "At not less than 3 monthly intervals" read literally means intervals of 3 months or more (no more often than quarterly); the evident purpose is at least every 3 months, and that is what is encoded. Asserted.
3. **Good faith is required for a notification, but not for giving information, in ss 237A and 237B.** "Protected action" in s 237A(2) is "(a) making a notification, in good faith ... or (b) giving information, documents or other assistance", and s 237B(1)(a), (b) are drafted the same way; s 237(1) requires good faith for both. So a reprisal against a person who gave information in bad faith is still an offence, and a confidentiality clause is void against it. Asserted. Whether this is deliberate is not clear.
4. **A confidentiality clause binding only the patient and the indemnity insurer is outside the s 237B(2) offence.** A "relevant person" is a practitioner, an employer or former employer, or a health service provider (s 237B(3)); an insurer is none of these. The clause is still void to the extent s 237B(1) says, whoever made it. In practice a settlement deed usually names the practitioner, who is a relevant person. Asserted.
5. **s 237A creates offences, not a right to compensation.** The Law gives the person who suffered a reprisal no civil remedy; any claim for loss would rest on other law (employment, discrimination, tort). The reprisal penalties ($60,000 individual, $120,000 body corporate) are asserted.
6. **Where the Board's 60 days end is uncertain at the margin.** Sch 7 cl 31(3) moves a last day that is "not a business day in the place in which the thing is to be or may be done"; a National Board is a single national entity (s 7) and the Law does not say where its preliminary assessment is done, so which public holidays count is unclear. Weekends are moved past; public holidays are not.
7. **A late preliminary assessment has no stated consequence.** s 149(1) says "must, within 60 days", but nothing in the Law says what follows if the Board is late; the notifier's recourse would be a complaint to the National Health Practitioner Ombudsman (s 235 applies the Ombudsman Act; not encoded) or proceedings outside this Law. The regulative rule records a breach and nothing more.
8. **Practising without insurance is not an offence.** s 129(4) makes a breach of s 129(1) only "behaviour for which health, conduct or performance action may be taken". For a patient, this means the Law does not itself ensure there is an insurer to meet a negligence claim; that a breach is a ground for a notification (s 144(1)(e)) is asserted.
9. **Notifiable conduct does not cover a single poor outcome.** s 140(d) needs "a significant departure from accepted professional standards" placing the public at risk of harm; a negligent operation without more need not trigger any mandatory notification, but it is a voluntary ground (s 144(1)(b)). Asserted.
10. **s 147(2)(b) speaks of "the individual's notification"** although the section is about "an entity", which includes an unincorporated body (s 5). Harmless, but a drafting slip.
11. **s 148(2) and (3) in the deposited text read "the National Agenc —" and "the National Agency mus —"**: letters were lost in the conversion. The provisions are not encoded.

## Raised in the ledger

Nothing. No ledger entry named this Law, and no scenario life cites it.

## What would need doing before this is worth relying on

- **The professional indemnity insurance registration standards**, for what "appropriate" arrangements are.
- **The Health and Disability Services Complaints Act 1995 (WA)**, for the health complaints entity's side of s 150 and the patient's complaint there.
- **The title and practice protections (ss 113–123A) and Part 8 Divisions 7A and 7B**, for practitioners who are not, or claim falsely to be, registered.
- **The rest of Part 8** (investigations, panels, the State Administrative Tribunal's powers under s 196), if a notifier's questions about outcomes are wanted.
- **The Limitation Act 2005 (WA) and the Civil Liability Act 2002 (WA)**, for the negligence claim itself; this Law gives a patient no right to compensation.
- An independent test pass and a human review.
