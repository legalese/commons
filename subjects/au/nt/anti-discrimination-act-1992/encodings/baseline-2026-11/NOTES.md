# Anti-Discrimination Act 1992 (NT) -- baseline encoding, the person aggrieved

UNOFFICIAL. Not an official version of the Anti-Discrimination Act 1992 (NT). Copyright in Northern Territory legislation
is owned by the Northern Territory. Quoted under the Northern Territory copyright policy of 8 October 1996 (see
SOURCE-LICENSE.md).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on
2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`nad-dates.l4`,
built-in date functions only, no daydate), the rules in `nad-rules.l4`, and the person aggrieved's questions in
`nad-seat.l4`, which imports the rules and restates none. The cases are in `nad-cases.l4`. The shape follows the NT
Limitation Act 1981 baseline.

## Edition

- **Act:** Anti-Discrimination Act 1992 (NT), reprint REPA027 as in force at 27 July 2026, as deposited at
  `../../registers/source-bundle/Anti-Discrimination-Act-1992-NT-current-reprint-REPA027.txt` (file sha256
  bb94528f...cca2fe), retrieved from legislation.nt.gov.au on 6 November 2026. It includes the Anti-Discrimination
  Amendment Act 2022 (3 July 2023, and 2 January 2024 for its ss 8, 9, 26-31, 33-35, 40, 42, 44) and the
  Anti-Discrimination Amendment Act 2025 (31 October 2025; Part 3 from 27 July 2026).
- **Days taken from the Act and its endnotes:** commencement 1 August 1993 (s 116, s 49(2)); 3 July 2023 (s 121); 31
  October 2025 (ss 126, 127); 27 July 2026 (s 128).
- **Numbers set elsewhere:** the maximum compensation the Tribunal may order is "an amount not more than that prescribed"
  (s 88(1)(b)), prescribed by regulation under s 117. The regulations are **not deposited**, so the maximum is an input
  (`the prescribed maximum`); the cases use an illustrative 60000. The value of a penalty unit (s 79(4): 100 penalty
  units) is set under other law and not deposited: the answer is in penalty units. There is no NT requirement ledger, so
  no ledger entry was raised for the regulations; depositing them is listed below.
- **Borrowed terms asked as facts:** "detriment", "associate", "harassment", "special need", "genuine occupational
  qualification", "inherent requirements", "legal incapacity", "systemic discrimination" (defined in s 4 by its effect,
  asked), "public place" (s 20A(4) "includes"), and whether a person has an attribute (the s 4 definitions of disability,
  race, relationship status, irrelevant criminal record and the rest are glossed in the descriptions).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read and
satisfied assertions counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `nad-dates.l4` | 0 | 0 | 0 | 0 |
| `nad-rules.l4` | 0 | 0 | 0 | 0 |
| `nad-seat.l4` | 0 | 0 | 0 | 0 |
| `nad-cases.l4` | 0 | 0 | 217 | 217 |

Every expected value was worked by hand from the text. Every exported question is asserted at least twice, with the
edges: the day before and the day of each commencement (31 July / 1 August 1993; 2 / 3 July 2023; 30 / 31 October 2025;
26 / 27 July 2026); a club of 29 and of 30 members; a child of 17 and a person of 18; a superannuation member joining on
1 August 1994 (12 months after commencement) and the day after; the last day to complain and the day after (12 and 24
months; from 29 February 2024; under s 126 with no late acceptance); a complaint on the day of the conduct and the day
before it; the s 66 60 and 90 days; the s 72 60 days (last day and day after); the s 81 21 days and an extended day
(last day and day after); compensation just under, at and just over the maximum; the s 106 28 days with and without a
request for reasons.

## Seat

**The person aggrieved** (`nad-seat.l4`): the individual treated badly who may complain to the Anti-Discrimination
Commissioner -- a worker or job applicant, a student, a tenant or would-be tenant, a customer, a club member, a person
seeking insurance or superannuation, a person dealing with a Territory agency. "Was I discriminated against?", "Was I
sexually harassed?", "Was I victimised for complaining?", "Did they fail to accommodate my special need?", "Can they rely
on an exemption?" (the respondent must prove it, s 91(2)), "Is the employer liable too?", "Can I complain, and by when?",
"By when must I ask for a hearing, and appeal?", "What can the Tribunal order?". No seat for the respondent, the
Commissioner, the Tribunal or the Supreme Court: their judgments and decisions are asked as facts. A respondent's seat
would be a welcome second layer (CLAUDE.md, 2026-10-21) but is not written.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, except that the regulations prescribing the
  compensation maximum are not deposited (the number is an input).
- **The actors the text names.** Followed: the complainant, the respondent, the Commissioner, the Tribunal, the Supreme
  Court, the educational authority, the club, the worker or agent.
- **Judgments answered conditionally.** Followed: "reasonable", "reasonably necessary", "reasonable, justifiable and
  proportionate", "in good faith", "genuine", "satisfied", "all reasonable steps", "unreasonable" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "attribute" (s 4, s 19), "child" (s 4), "club"
  (s 4, by its 30 members), discrimination (s 20(2)), sexual harassment (s 22(2)), victimisation (s 23(2)), the s 20A(3)
  deeming are worked out from facts.
- **One case.** One course of conduct against one person, and one complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 (attribute, child, club; the attribute definitions as glosses), ss 19, 20, 20A, 20B, 21, 22, 23, 24, 25, 26, 27,
28 and the areas of Part 4 (ss 29, 31-34, 38, 41, 46, 48, 49A, as the person's choice of area: every one of those
sections ends with less favourable treatment "in any way in connection with" the dealing, except s 48(1) and s 49A,
whose dealings are as wide); the exemptions of Part 4 (ss 30, 35, 35A, 35B, 36, 37, 40, 42-45, 47, 49) and s 39; Part 5
Division 1 (ss 50-58) and s 21(5); s 59 as a fact (an exemption in force); Part 6 as it meets the complainant: ss 60,
65, 66(1), 66D, 66F, 71(4), 72, 79, 80, 81, 86, 87(1), 88, 105, with ss 64, 89 and 91 in the descriptions; s 106(2);
the transitional provisions ss 116, 122, 123, 126, 127, 128.

**Regulative rules:** four, in `nad-rules.l4`.
- s 65: `PARTY the complainant MUST make the complaint WITHIN` the days to the last day, `LEST PARTY the Commissioner MAY
  accept the complaint out of time` (s 65(2)).
- s 126(2): the same, `LEST BREACH ... BECAUSE` the Commissioner cannot accept it late.
- s 72(2): `PARTY the complainant MUST indicate a wish to continue WITHIN` 60 days, `LEST BREACH ... BECAUSE` the
  complaint lapses.
- s 81(4), (6): `PARTY the complainant MUST request referral to the Tribunal WITHIN` 21 days (or the extended time),
  `LEST BREACH ... BECAUSE` the complaint lapses.
Each is run by EVALTRACE inside an "on this day" question that takes plain dates; no exported question takes a DEONTIC
or an EVENT.

**Out, and why:**
- Part 2 (the Commissioner's office), ss 1-3, 5, 5A, 117 and Parts 9-11 except as used: machinery.
- Part 2A (ss 18A-18D, the positive duty): enforced by the Commissioner's own investigation and enforceable undertakings,
  not by a complaint; a report under s 18D may be referred to in a complaint (s 18D(6), s 102), which needs no rule.
- The offences of Part 8 (ss 107A-110A, 109, 109A): prosecuted, not complained of, and directed at people dealing with
  the Commissioner, not at the person aggrieved; s 112 (prosecution time limits) is the prosecutor's.
- s 4A (assistance animals): a definition, used only through s 21(5) and the s 50 exemption, where it is asked as a fact.
- ss 62A and 62B (what a representative complaint is, and the Commissioner's guidelines): the person is asked whether
  their complaint is a representative one; the definition and the guidelines are machinery (with ss 61-64 below).
- ss 110B and 110C (enforceable undertakings and enforcement orders): the Commissioner's tools, used with Part 2A's
  positive duty, not remedies a complainant seeks.
- Part 9 (ss 118-120, the Justice Legislation Amendment Act 2015): complaints made before 2015, and offences, long spent
  and in any case governed by the Act as it stood before 3 July 2023 (s 122), which the first question already says.
- s 124 (offences before the 2022 amendments): offences, out with Part 8.
- s 31(3) (religious activity in working hours): a narrow head left for a later pass.
- The Commissioner's and the Tribunal's procedure: ss 61-64 (except in descriptions), 66B, 66C, 66E (except as a bar),
  67, 68, 73, 78, 82, 87A, 87B, 89A, 89B (investigation of representative complaints), 90, 94, 97, 98, 100, 101, 107,
  113-115.
- s 68(2): a stay stops every time limit running; the time-limit questions assume no stay (say so to the person).
- s 59's procedure (application, conditions, revocation, 3-year terms): only "an exemption in force covers it" is asked.
- Complaints made before 27 July 2026, and conduct before 3 July 2023, are governed by earlier texts not deposited: the
  first question says so and the rest do not answer for them.
- A complaint made before 31 October 2025 about an act under the old s 20A is outside s 126, which reaches only "a
  complaint made after the commencement" (s 126(1)(a)): the old s 20A governs it as the law then in force, and s 128
  sends it to the old Part 6. The first question says so; neither is encoded.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "not later than 12 months after" (s 65(1)), "24 months" (s 65(1A)), "not more than 12 months after that
  commencement" (s 49(2)) -- `the anniversary` -- the day of the event excluded, so the last day is the anniversary;
  from 29 February, 28 February; "within N days after" (ss 66, 72, 81, 106) is the day plus N -- the anniversary
  excluded, or 29 February running to 1 March. The NT Interpretation Act rule is not deposited.
- **F2** s 20(1), s 28 ("This Act applies to prohibited conduct in the areas of") -- `ss 19-21 -- I was discriminated
  against` -- outside every area, NOTHING (a scope stated without "only") -- JUST FALSE.
- **F3** s 22 with s 28 -- `s 22 -- I was sexually harassed` -- s 22 names no area, so sexual harassment is answered
  without one -- s 28 confining all prohibited conduct, sexual harassment included, to the seven areas.
- **F4** s 23(1) "because the other person" -- `s 23 -- I was victimised` -- a detriment for another reason, NOTHING --
  JUST FALSE as a flat negative.
- **F5** s 24 -- `s 24 -- they failed to accommodate my special need` -- no special need, NOTHING; reasonable provision,
  JUST FALSE ("takes place when") -- no special need as JUST FALSE.
- **F6** s 79(2) "must be in writing and specify the time ... and place" -- `ss 79, 80 -- what follows` -- a direction
  that is not is not a direction under s 79, so nothing follows -- an informal direction still binding.
- **F7** s 106(2)(a), (b) -- `s 106 -- the last day to appeal` -- where (b) applies, its later day is the limit --
  either day, the earlier binding.
- **F8** s 128 -- `transitional -- which law applies` -- any complaint made before 27 July 2026 treated as pending and
  individual -- a finally determined or representative complaint governed by the current Part 6.
- **F9** s 66D(1)(b) "the complainant cannot make another complaint" -- `s 60 -- the complaint may be made` -- applied
  to the person aggrieved and to anyone complaining for them -- only to the same complainant.
- **F10** s 35B(1)(a) -- `ss 35-37 -- the work exemption applies` -- the ground (religious belief or activity) is inside
  the "if", so another ground gives JUST FALSE, where the grounds of ss 35A, 36, 37, 43, 47, 55 are the grant's own
  wording and give NOTHING -- every ground answered the same way.
- **F11** s 35(1)(a) "by fixing reasonable terms and conditions if" -- same -- unreasonable terms are outside the grant
  (NOTHING); no restricted capacity fails the "if" (JUST FALSE) -- both JUST FALSE.
- **F12** s 54 "by reason only of" -- `Part 5 -- the general exemption applies` -- JUST FALSE where it is not the only
  reason -- NOTHING; s 56(3) "does not include" coaching, umpiring, administration: JUST FALSE -- NOTHING.
- **F13** s 4 "club" -- `ss 19-21 -- I was discriminated against` -- fewer than 30 members, NOTHING (the person may be in
  the goods and services area instead) -- JUST FALSE.
- **F14** s 49(1)(d)-(f) -- `s 49 -- the insurance exemption applies` -- where reasonable actuarial data exists but the
  insurer did not rely on it, (e) and (f) are not available -- (f) available whenever the discrimination is reasonable.

- **F15** s 127 "any person who works for an educational institution at the time section 5 of the amending Act
  commences" -- `ss 35-37 -- the work exemption applies` -- read as written: working for any educational institution on
  31 October 2025 (the person is asked about any, not only this one) -- only staff of the institution relying on s 35B.
- **F16** s 25 with s 28 -- `s 25 -- the advertisement was prohibited` -- s 25 names no area, so discriminatory
  advertising is answered without one (as F3 for s 22) -- s 28 confining it to the advertisement of a dealing in one of
  the seven areas.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "attribute means" (s 4), "takes place if" (ss 22(2), 23(2)), "does not apply" (ss 20A(2), 23(3), 26(2),
(3), 40(5), 105(2), 127, 56(2)), "does not prevent" (s 20B), "does not include" (s 56(3)), "cannot" / "shall not" (ss
66D, 66F, 71(4), 72(3), 81(6)), "only" (ss 54, 57(2)), the "if", "where" and "unless" conditions of the exemptions, and
the periods give `JUST FALSE`. `NOTHING` is answered where an exemption or prohibition is limited by its own wording and
the case falls outside it (the ground, the dealing, the kind of body: *limited by its own wording*), outside the Part 4
areas (F2), where s 20's "includes" is not met, for a body of fewer than 30 members (F13), for someone else complaining
(s 60's list grants), and after a s 67 or s 68 decline (*silent*, finding 6).

## What the Act turns out to say

1. **"Offensive behaviour" is prohibited conduct but appears nowhere else.** s 4's definition of prohibited conduct lists
   "(ca) offensive behaviour", but no section defines or prohibits it; s 20A (inciting hatred) is the likely target but
   uses other words. Encoded through s 20A only. Not asserted.
2. **s 114 cites a repealed section.** "It is not a reasonable excuse for the purposes of section 85(2) or 107B(2)": s 85
   was repealed by the Anti-Discrimination Amendment Act 2025 (endnotes), so the first reference is dead. Outside the
   seat's questions. Not asserted.
3. **Public health and HIV/hepatitis status.** s 55 lets a person discriminate "on the ground of disability" to protect
   public health; HIV/hepatitis status is a separate attribute (s 19(1)(ja)), though the presence of a disease-causing
   organism is also a "disability" (s 4(b)). On the HIV/hepatitis ground the encoding answers NOTHING; the person should
   also ask on the disability ground. Asserted.
4. **A "club" needs at least 30 members** (s 4). A smaller association is outside Division 6, and the encoding answers
   NOTHING for it as a club (F13); it may supply goods, services or facilities. Asserted at 29 and 30.
5. **The Commissioner's permission to complain again is uneven.** After a s 66E decline (s 66F) or a withdrawal
   (s 71(4)) the Commissioner may permit a fresh complaint; after a s 66 decline only a representative complaint may be
   remade (s 66D(2)); after a lapse under s 72(3) or s 81(6) there is no power at all. Asserted.
6. **No bar after a s 67 or s 68 decline.** Declining a complaint as frivolous, trivial, misconceived or dealt with
   elsewhere carries no stated bar on complaining again, unlike ss 66D, 66F. Answered NOTHING. Asserted.
7. **s 126 fixes 12 months even for a representative complaint.** For an act under the old s 20A, s 126(1)(b) keeps "the
   12-month limitation period in section 65(1)" and (2) takes away the s 65(2) power, so the 24 months of s 65(1A) do not
   apply. Asserted.
8. **A gap in the 2022 transitional provisions.** s 122 keeps the old Act for complaints made before 3 July 2023, but the
   2022 Act's complaint sections (its ss 26-31, changing ss 60-66D) commenced on 2 January 2024; a complaint made between
   those days has no saving rule. Grouped with "Part 6 as it stood when you made it". Not asserted.
9. **s 23(1)(b) lacks its "; or"** ("proceedings under this Act or"); the list still reads as alternatives. Not asserted.
10. **The compensation cap is in regulations not deposited** (s 88(1)(b) "not more than that prescribed"). The question
    takes the maximum as an input. Asserted at, under and over an illustrative figure.
11. **The religious school exemption excludes current staff.** s 127: s 35B "does not apply in respect of any person who
    works for an educational institution at the time section 5 of the amending Act commences" (31 October 2025). Read
    as written, that is anyone then working for any educational institution, not only the one relying on s 35B (F15).
    Asserted.

## Verification fixes (2026-11-07)

An independent verification found six minor issues; all were fixed:
- the method text in `encoding.json` and the `nad-seat.l4` header now say four regulative rules (s 126(2) is the fourth);
- `By when must I say I wish to continue` is now asserted twice (60 days across the end of February 2027);
- s 4A, ss 62A-62B, ss 110B-110C, Part 9 and s 124 are now in the out list with their reasons;
- the first question no longer cites s 126 for a complaint made before 31 October 2025 about an old s 20A act;
- s 127 is read as written (any educational institution), with fork F15;
- s 25 (discriminatory advertising) is now encoded, as prohibited conduct a person aggrieved may complain of (s 4(d)),
  with fork F16 and a new question, `Was the advertisement prohibited`.

## Before this is worth relying on

- Check the text against the authorised PDF of reprint REPA027 (retrieved 6 November 2026) and any later reprint.
- Deposit the Anti-Discrimination Regulations (NT) for the s 88 maximum, and the Interpretation Act 1978 (NT) rule for
  reckoning periods (F1); deposit the pre-27 July 2026 Part 6 if pending complaints matter.
- Encode s 31(3), and a respondent's seat if wanted.
- A lawyer's view on findings 1, 3, 5, 6, 8 and forks F2-F5, F10-F16; an independent test pass and a human gate.
