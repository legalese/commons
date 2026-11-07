# Health Practitioner Regulation National Law Act 2009 (Qld) — baseline encoding, the complainant's seat

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below).
There is no REFUSE, no `#ASSERT REFUSED` and no BECAUSE except in `LEST BREACH`; a question that reaches a gap answers `not covered` with a reason, and the cases assert it.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

It was written in a run of baseline encodings of the laws behind compensation and other civil claims, here under medical negligence and health. The focus was **the Act as host of the National Law**. Queensland is the host jurisdiction: the Health Practitioner Regulation National Law is the schedule to this Act, and s 4 applies it, "as modified by part 4", as the Health Practitioner Regulation National Law (Queensland). So the encoding takes:

- the Act's own local application provisions (Parts 1–3: ss 1–10);
- the Part 4 modifications (ss 11–59), which turn Queensland into a co-regulatory jurisdiction where complaints go to the health ombudsman;
- the National Law (Queensland) as those modifications leave it, in the Parts a person harmed by a health practitioner meets.

The Law is about 510,000 characters, so the whole Act is not encoded; what is in and out is listed under Scope.
This is the first encoding of this subject; nothing existing was touched. No ledger entry was open for it.

Files:
- `hprnlq-dates.l4`: the date arithmetic, the only module that imports `daydate`;
- `hprnlq-complainant.l4`: the rules, the complainant's 16 exported questions and two regulative rules;
- `hprnlq-cases-complainant.l4`: the worked cases.

The 16 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Law's order:

- does this Queensland Act apply to the National Law (Queensland) (s 7 of the Act; s 146; s 9 of the Act);
- can a complaint be made about this person (ss 138–139B, with the Queensland (1A) and (2A));
- can I notify the health ombudsman (ss 143A–146);
- was another practitioner or the employer required to notify the health ombudsman (ss 139D–142). This arises only where one of them knew;
- after the health ombudsman refers the complaint to the National Board, which arises only then:
  - by when must the Board make its preliminary assessment, and did it (s 150);
  - can the Board take no further action (s 151);
- what I must or may be told later, by when I must next hear how an investigation is going, by when I must be told of a panel's decision, and can I make a submission to a panel (ss 159A, 161(3), 167A, 177A, 180, 187, 189, 192). This arises only once something has been decided;
- must the Board tell the health ombudsman of a serious matter (ss 193–193C), and which tribunal hears a Board referral (s 193B(3), with ss 6 and 9 of the Act). This arises only where the matter is serious;
- did the practitioner have to be insured (s 129);
- am I protected from liability (s 237), and does the Law itself protect me from a reprisal or a confidentiality clause (s 56AA of the Act).

**Regulative rules.** Two duties the Law states in days for the complainant's matter are written as `PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE`:
- the Board's preliminary assessment within 60 days after receipt of a referred matter (s 150(1));
- the Board's notice of a panel decision to the complainant within 30 days (s 192(2)(b)).

Each period is written once as a named deadline, and both the seat questions and the rules' `WITHIN` use it. The questions take plain dates. The cases assert the rules through `CONSIDER EVALTRACE ... WHEN FULFILLED`: the last day, the day after, a period moved past a weekend, and an event that is not the duty's action.

## Edition

- **The Act:** Health Practitioner Regulation National Law Act 2009 (Qld), the version in force from 10 April 2026, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2009-045.txt`. It is a plain-text conversion of the Queensland Legislation HTML view, not the authorised PDF.
- **The Law as modified:** the Health Practitioner Regulation National Law (Queensland) as Queensland Legislation publishes it (the Law with the Part 4 modifications applied, marked by editor's notes), in force from 10 April 2026, deposited at `../../registers/source-bundle/act-2009-hprnlq.txt`. Where the two differ, the published Law (Queensland) was encoded (finding 3).
- **Not deposited or not encoded:**
  - the national regulations and the registration standards. Professional indemnity insurance is the one that matters here; whether cover was "appropriate" is asked. No number this encoding uses comes from them.
  - the Health Ombudsman Act 2013. It is deposited at `subjects/au/qld/health-ombudsman-act-2013/` but not encoded, and IMPORT could not reach it anyway. It is named in the answers.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hprnlq-dates.l4` | 0 | 0 | 0 | 0 |
| `hprnlq-complainant.l4` | 0 | 0 | 0 | 0 |
| `hprnlq-cases-complainant.l4` | 0 | 0 | 123 | 123 |

Every exported question has cases. Expected values were written by hand from the text. Weekdays were worked from 1 January 2026 (a Thursday) and 1 January 2028 (a Saturday).

The edges asserted include:
- the 60th day after receipt, and the 61st;
- a 60th day on a Saturday and on a Sunday, each moved to Monday by Sch 7 cl 31(3);
- a period running to 29 February 2028;
- the 30-day panel notice falling on a Saturday;
- three months from 30 November, ending on 28 February that falls on a Saturday (2026) and on a Sunday (2027);
- a student offence punishable by exactly 12 months, and by 11;
- either Queensland link alone, and neither (s 143A);
- each s 151 two-limb ground with one limb missing;
- s 193(1A) against the panel route.

## Seat

**The complainant** (s 139C: "a person who makes a complaint", which in Queensland means a notification under Part 8 Division 2 or 3, or a health service complaint under the Health Ombudsman Act 2013). Usually this is a patient, or a patient's family member, harmed by or worried about a registered health practitioner's care or conduct in Queensland, who may also be bringing or settling a negligence claim. The questions are ones like:
- "Where do I complain about my surgeon?"
- "Did the hospital have to report her?"
- "By when must the Board look at it once the health ombudsman sends it on?"
- "Will I be told?"
- "Am I protected?"

The Law puts duties on practitioners, employers and the National Boards; those duties are encoded for what they mean to the complainant. No second seat is written. The practitioner's seat (registration, show cause, appeals to QCAT as a review under the QCAT Act, s 9) is left for a later layer. There is no seat for the health ombudsman, Ahpra, a National Board, a panel or QCAT.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act and the Law it hosts set every number used here: 60 days, 30 days, 3 months, 12 months. The Health Ombudsman Act 2013 governs most of a Queensland complaint's life but is a separate Act; it is named, not encoded.
- **The actors the text names.** Followed: the complainant (notifier), the registered health practitioner, the student, the treating practitioner, the employer, the health ombudsman, the National Agency, the National Board, the panel, QCAT.
- **Judgments answered conditionally.** "Reasonable belief" (ss 141, 141A, 141B, 142, 193), "in good faith" (s 237), "frivolous, vexatious, misconceived or lacking in substance", "not practicable", "not in the public interest", "dealt with adequately", "appropriate steps" (s 151), the panel's leave (s 187) and "satisfied the health ombudsman is aware" (s 193(1A)) are all inputs.
- **The Act's definitions worked out; borrowed terms asked.**
  - Worked out: "notifiable conduct" (s 140), "registered health practitioner" and "student" (s 5, and s 129(5)), the s 144 grounds, the s 141(4) and s 141C(2) exceptions (as one input), "this jurisdiction" (s 5 of the Act), and the responsible tribunal (s 6 of the Act).
  - Asked: "impairment", "professional misconduct", "principal place of practice", "corresponding prior Act" and "appropriate professional indemnity insurance arrangements".
- **One case.** One complaint about one practitioner or student.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input ("notification" is glossed as a complaint, the National Agency as Ahpra).
- **Operative sections in; machinery out.** See Scope.

## Scope

**In:**
- the Act:
  - s 3 (definitions);
  - s 4 (the Law applies as modified);
  - s 5 ("this jurisdiction" is Queensland);
  - s 6 (QCAT the responsible tribunal);
  - s 7 (excluded Acts);
  - ss 7A–7C (co-regulatory jurisdiction, authority and adjudication body: the reason the complaint goes to the health ombudsman, in the answers);
  - s 9 (an appeal to QCAT is a review under the QCAT Act);
  - Part 4 as it bears on the provisions below, in particular ss 15, 21, 22, 22A, 23–30, 32–34, 35A, 37, 37A, 40A, 42, 46–50, 56AA and 59.
- the National Law (Queensland):
  - s 5 (the definitions the questions use) and s 129;
  - Part 8 Division 1 (ss 138, 139A, 139B, 139C; s 139 named in an answer);
  - Division 2 (ss 139D, 140, 141, 141A, 141B, 141C, 142(1), (2));
  - Division 3 (ss 143A, 144, 145);
  - Division 4 (s 146);
  - Division 5 (ss 148, 149, 150(1), 151(1)–(4));
  - the complainant's provisions in Divisions 7–11 (ss 159A, 161(3)(b), (4), 167A, 177A, 180(1)(b), (2), 187, 189, 192(2)(b), (4));
  - Division 12 Subdivision 1 (ss 193, 193A(1), 193B(2)–(4), 193C(1) in one answer);
  - s 237;
  - Schedule 7 cl 12 ("business day", weekends only) and cl 31(2), (3).

**Out, and why:**
- **The Act, Parts 1–3 otherwise.**
  - s 1, s 2 (commencement: the Act commenced on 1 July 2010 other than Part 4, whose commencement the deposited text does not state): machinery.
  - s 8 (criminal history information to a Board): the regulator's.
  - s 9A (regulations), s 10 (repeal): machinery.
- **Part 4 otherwise.**
  - ss 16, 18, 19 (s 26A, the complaints element of registration fees paid to the health ombudsman), 20: the Agency's and the Boards' functions and finance.
  - ss 20A, 20B (registration renewal and conditions): the practitioner's.
  - ss 35 (ss 153, 154, dealing with matters together), 35B, 35C (interim prohibition orders for unregistered persons), 36, 38, 39, 41, 43–45: the Board's procedure.
  - s 51A (parties to reinstatement proceedings), s 51B (s 198D costs omitted), s 52 (ss 201–203 omitted), s 53, s 54, s 55 (ss 206A, 206B: the Board's notices to the health ombudsman), s 55A (register entries), s 56 (s 231 records): the regulator's and the practitioner's.
  - s 56A (s 241A, indictable offences): prosecution, which the complainant does not do.
  - s 57 (Part 12A, transitional provisions for the Health Ombudsman Act 2013, for notifications current when that Act commenced in 2014): a complaint that old is not asked about.
  - s 58 (s 328, reinstatement): the practitioner's.
- **The National Law (Queensland), Parts 1–7 otherwise:** the Ministerial Council, the Agency, the Boards, accreditation, registration, the title and practice protections (ss 113–123), advertising. As in the WA notifier encoding, these belong to the practitioner and the regulator, or are a separate body of offences.
- **s 130 (the practitioner's notice of relevant events, including an insurance lapse):** the WA encoding has it. Here only s 129 is encoded; s 130 is the practitioner's reporting duty and is left to a practitioner seat.
- **s 143 (mandatory notifications by education providers) and the student limbs of ss 139D(2), 141(1)(b), 141B(3), (4):** a complainant about a student practitioner meets them rarely. The question asks about a registered health practitioner's conduct only.
- **s 150(2), (3), ss 150A–150C, s 151(1A):** the Board's powers in the preliminary assessment. s 151(1A) (part of a matter) turns on a referral the complainant does not control.
- **Part 8 Divisions 6–14 otherwise:** the Board's and the tribunal's procedure and powers. s 199 gives appeal rights to the practitioner or student, not the complainant.
- **Parts 9–12 otherwise:** finance, privacy, registers, s 236 (protection of persons exercising functions), inspectors, offences, regulations, transitional provisions.
- **The Health Ombudsman Act 2013:** a separate Act. How the health ombudsman deals with a complaint, its time limits, its referral to Ahpra under part 9 division 1, prosecutions by the director of proceedings before QCAT, and its reprisal and non-disclosure provisions (ss 261–263A) are all there. It is named in the answers.

## Fork register (questions with no convention, decided case by case)

Each line gives the provision, the function, the answer taken, and the other reading.

- **F1** s 7 of the Act, an unlisted Act: `Does this Queensland Act apply to the National Law question`. Answer taken: `not covered` (the list is not closed with "only"). Other reading: "yes".
- **F2** s 139A for a former practitioner's behaviour after registration ended: `Can a complaint be made about this person question`. Answer taken: `not covered` (a scope limit with no "only"). Other reading: "no". s 139B(3) ("only to the extent") answers "no".
- **F3** s 143A, neither Queensland link: `Can I make a voluntary notification question`. Answer taken: "no" ("applies ... only if"). The Law as applied in another participating jurisdiction may still apply; the answer says so.
- **F4** s 144, no listed ground: same function. Answer taken: `not covered`, because s 144 says "may be made ... on any of the following grounds" without "only", and a health service complaint under the Health Ombudsman Act 2013 may still lie. Other reading: "no", since s 145 lets only an entity that believes a ground exists notify.
- **F5** s 141(1), a belief formed outside the course of practising: `the s 141 answer`. Answer taken: "no" ("This section applies to a registered health practitioner who, in the course of practising ..., forms", read as a "where" condition). Other reading: `not covered`.
- **F6** s 161(3) "at not less than 3 monthly intervals": `the last day of 3 months after`. Answer taken: at least every 3 months, ending on the same day number 3 months on (or the last day of a shorter month), moved past a weekend. Other reading: intervals of 3 months or more, that is no more often than quarterly (finding 8).
- **F7** s 150(1) "within 60 days after receipt of a referred matter under section 148": `the s 150 assessment deadline for a matter received on`. The 60 days run from the day the input gives as receipt. The Law does not say whose receipt, the Agency's (s 148) or the Board's (s 149). s 149's "immediately" usually makes them the same day; if not, the later day would govern on the Board's-receipt reading.
- **F8** Division 2, anyone it does not name (a patient, a relative): `Was someone required to notify question`. Answer taken: `not covered`. Other reading: "no", since a "mandatory notification" is one "an entity is required to make" under Division 2.
- **F9** ss 141, 142 without a reasonable belief: "no" (s 142 "If an employer ... reasonably believes"; s 141 "who ... forms a reasonable belief").
- **F10** s 141A(1) "is at risk of engaging" in sexual misconduct: for a treating practitioner, "yes" (s 141A); for anyone else, "no", because s 140(b) needs "engaging in" (finding 5).
- **F11** s 151 when none of (a)–(f) holds: "no" ("may decide ... if").
- **F12** s 193(1) when neither (a) nor (b) has happened: "no" ("as soon as practicable after"). s 193(1A) excuses only paragraph (a), so a panel's notice under s 190(2) must be passed on even when the health ombudsman already knows. That is the text, not a fork.
- **F13** s 237 without good faith: "no" ("applies to a person who, in good faith").
- **F14** s 129 for a student, a person not registered, a non-practising registrant and a practitioner not practising: "no" (s 5, s 129(5), and "must not practise unless").
- **F15** Sch 7 cl 31(3): only Saturdays and Sundays are moved past (finding 7).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they apply here:
- **"no", because the text says no in its own words:**
  - s 7's "do not apply" is a flat negative;
  - s 143A and s 139D are "only if";
  - s 140 is a "means" definition;
  - the 60-day and 30-day periods are fixed in the text's words;
  - s 56AA's omission leaves the Law (Queensland) without ss 237A and 237B.
- **`not covered`, because the case falls outside a scope limit with no "only", or the text is silent:**
  - an unlisted Act in s 7;
  - s 139A behaviour after registration ended;
  - s 144 with no listed ground;
  - a person Division 2 does not name.

## What the Act turns out to say

1. **In Queensland a complaint about a registered practitioner goes to the health ombudsman, not to Ahpra, and the Law itself says little about how it is handled.**
   - Section 7A of the Act takes Queensland out of Part 8 Divisions 3–12. Part 4 then:
     - redirects every notification to the health ombudsman (ss 25–30);
     - replaces s 146 with "the health ombudsman must deal with it under the Health Ombudsman Act 2013" (s 32);
     - omits s 147, so Ahpra has no duty to help a notifier (s 33);
     - replaces Division 5, so a National Board sees a complaint only if the health ombudsman refers it (s 34). s 152 (telling the practitioner) is gone from the Law in Queensland.
   - So the 60-day preliminary assessment runs from the referral, not from the complaint. Asserted.
   - Whatever time limits and rights the complainant has before the referral are in the Health Ombudsman Act 2013, not encoded.
2. **The reprisal and confidentiality-clause protections of the National Law do not exist in the National Law (Queensland).**
   - s 56AA of the Act omits ss 237A and 237B, and s 59 omits s 329.
   - The published Law (Queensland) prints "Sections 237A and 237B are not applicable in Queensland". Asserted.
   - The Health Ombudsman Act 2013 has its own provisions (ss 261–263A, not encoded). Its s 263 also makes a reprisal a tort giving damages, which the National Law's s 237A elsewhere does not.
   - A complainant reading the national version of the Law, or the WA encoding, would get the wrong answer for Queensland.
3. **The Act's own text of s 151 and the published National Law (Queensland) differ.**
   - In s 34 of the Act, s 151(1)(c) reads "has not been, or is no longer, registered by the Board", and (e) and (f) speak of "the referred matter".
   - The published Law (Queensland) reads "registered in a health profession for which the Board is established" in (c), and "the subject matter of the notification" and "the health practitioner to whom the notification relates" in (e) and (f).
   - The published text appears to carry later national amendments of s 151 into the Queensland substitute, half-converted. The published text was encoded. The answers do not change, but a "notification" in (e) and (f) of a provision that applies only to a "referred matter" is a drafting or compilation slip.
4. **The example to s 142(1) still says "The employer must notify the National Agency".** Part 4 s 26(1) changed s 142(1) to "health ombudsman" but left the example alone. Harmless, but wrong for Queensland.
5. **A treating practitioner need not report a colleague who practised drunk unless the risk is substantial.**
   - Practising while intoxicated is notifiable conduct whatever the risk (s 140(a)), and a non-treating practitioner or employer must notify it.
   - A treating practitioner is excluded from s 141 (s 141(2A)), and s 141B(1)(b) requires a belief that the public is at "substantial risk of harm". Asserted.
   - The other way round, s 141A makes a treating practitioner report a colleague merely "at risk of engaging" in sexual misconduct, which s 140(b) ("engaging in") does not make notifiable for anyone else. Asserted.
6. **Either Queensland link is enough for a voluntary notification (s 143A, "or").** A Brisbane-based practitioner's conduct in another State may be notified to the Queensland health ombudsman, and a New South Wales practitioner's conduct in Queensland may be too. The Law as applied in the other State may also apply; this encoding does not decide which forum takes it. Asserted on the Queensland side.
7. **Where a period's last day falls is uncertain at the margin.**
   - Sch 7 cl 31(3) moves a last day that is "not a business day in the place in which the thing is to be or may be done".
   - A National Board is a single national entity, and the Law does not fix where its assessment is done, so which public holidays count is unclear. Weekends are moved past; public holidays are not.
   - Section 7(a) of the Act shuts out the Acts Interpretation Act 1954, so its rules on reckoning time do not apply.
8. **"At not less than 3 monthly intervals" (s 161(3)), read literally, means no more often than quarterly.** The evident purpose is at least every 3 months, and that is what is encoded (F6). The s 161(4) exceptions are for notices to the practitioner only, so the complainant's notices have none.
9. **The complainant is told the outcome at few stages.**
   - After immediate action, an investigation or an assessment, the Board "may" tell the complainant (ss 159A, 167A, 177A).
   - Action after show cause (s 180(1)(b)) and a panel's decision (s 192(2)(b), within 30 days) must be notified, the reasons still optional (ss 180(2), 192(4)).
   - Only a decision to take no further action must give its reason (s 151(4)). Asserted.
10. **A late preliminary assessment has no stated consequence.** s 150(1) says "must, within 60 days", but nothing says what follows a late one; the regulative rule records a breach and nothing more.
11. **Section 7 shuts the Information Privacy Act 2009, the Right to Information Act 2009 and the Ombudsman Act 2001 out of the National Law (Queensland).** A patient cannot use them to get the scheme's records or to complain to the Queensland Ombudsman about a Board. What the Law itself offers is not encoded. Asserted.
12. **Practising without insurance is not an offence** (s 129(4)). It is a ground for a voluntary notification (s 144(1)(e)); the Law does not itself ensure there is an insurer to meet a negligence claim. Asserted.
13. **s 193(1A) excuses only paragraph (1)(a).** Where a panel tells the Board under s 190(2) that it believes there is professional misconduct, the Board must notify the health ombudsman even if the health ombudsman already knows. Asserted.

## Raised in the ledger

Nothing. Queensland has no requirement ledger, no ledger entry named this Act, and no scenario life cites it.

## Before this is worth relying on

- Check the conversions against the authorised PDFs, especially s 151 (finding 3).
- Encode the Health Ombudsman Act 2013, deposited beside this subject:
  - the complaint's life before any referral to Ahpra;
  - the director of proceedings' referrals to QCAT;
  - ss 261–263A on reprisals and non-disclosure agreements.
- Add a practitioner's seat over Part 8 and s 9 (reviews by QCAT), and the s 130 relevant events.
- A lawyer's view on findings 2, 3, 5 and 7 and forks F4, F6 and F7, an independent test pass, and a human gate.
