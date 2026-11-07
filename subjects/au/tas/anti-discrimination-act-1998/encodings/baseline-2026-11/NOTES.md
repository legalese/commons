# Anti-Discrimination Act 1998 (Tas) -- baseline encoding, the person aggrieved

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026 (State of Tasmania, CC BY 4.0).
Not the authorised version (see SOURCE-LICENSE.md). Not for public use as advice.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on
2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`tad-dates.l4`,
built-in date functions only, no daydate), the rules in `tad-rules.l4`, and the person aggrieved's questions in
`tad-seat.l4`, which imports the rules and restates none. The cases are in `tad-cases.l4`. The shape follows the NT
Anti-Discrimination Act 1992 baseline.

## Edition

- **Act:** Anti-Discrimination Act 1998 (Tas), No. 46 of 1998, consolidated version published 1 July 2025 and current
  at point in time 6 November 2026, as deposited at `../../registers/source-bundle/act-1998-046.txt` (text sha256
  07fbec41...cb21 as recorded in the `.meta.json`), retrieved from legislation.tas.gov.au on 6 November 2026. It includes
  the amendments of Act No. 7 of 2025 (1 July 2025: "non-acceptance"
  in ss 13, 65, 72, 109; s 98A(1)-(3) omitted).
- **Days the Act fixes:** none by date. The Act "commences on a day to be proclaimed" (s 2); the day is not in the
  deposited text, so s 108(1) (conduct that took place and concluded before commencement) is asked as a fact.
- **Numbers set elsewhere:** the fines are in penalty units (ss 89(1)(e), 99(3)); the value of a penalty unit is set
  under other Tasmanian law, not deposited. No regulations under s 109 are deposited; the Act's own numbers (12 months,
  42 and 28 days, 6 months, 20 and 10 penalty units, 5 adults, 12 and 18 years) need none.
- **Borrowed terms asked as facts:** "detriment" (s 3 "includes"), "public act" (s 3 "includes"), "organisation"
  (s 3 "includes"), "unreasonable in the circumstances", "genuine occupational qualification", "unjustifiable hardship",
  "reasonably necessary", "in good faith", "inherent requirements", "irrelevant medical record" (undefined, finding 1),
  and whether the person has an attribute (the s 3 definitions of disability, race, family responsibilities, gender
  identity, irrelevant criminal record and the rest are glossed in the descriptions).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read and the satisfied assertions counted.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tad-dates.l4` | 0 | 0 | 0 | 0 |
| `tad-rules.l4` | 0 | 0 | 0 | 0 |
| `tad-seat.l4` | 0 | 0 | 0 | 0 |
| `tad-cases.l4` | 0 | 0 | 156 | 156 |

Every expected value was worked by hand from the text. Every one of the 33 exported questions is asserted, with the
edges: the last day to complain and the day after (12 months; from 29 February 2024 to 28 February 2025; from 31
January), a complaint on the day of the conduct and the day before it; the s 64(2) 42 days across a month end; the
28-day review (last day, day after, day before receipt) and the 28-day appeal across a year end; s 93's 28 days in a
leap and a common February; s 78(2)'s 6 months from 31 August (28 February) and an agreed further period; shared
accommodation for 4 and 5 adults (s 27(1)(e)); a player of 11 and 12 (s 29); a child of 17 and a person of 18 (ss 39,
60(3)); disclosure to the Tribunal made and not made (ss 30(2), 44(2)); an enrolled and a not-enrolled student and a
non-religious ground (s 51A); the fine with and without a vexatious dismissal.

## Seat

**The person aggrieved** (`tad-seat.l4`): the individual against whom discrimination or prohibited conduct was
directed, who may complain to the Anti-Discrimination Commissioner -- a worker or job applicant, a student, a tenant, a
customer, a club member, a person seeking insurance or superannuation, a person dealing with a State agency. "Was I
discriminated against?", "Was I sexually harassed?", "Was I victimised?", "Can they rely on an exception?" (the
respondent must prove it, s 101), "Who else is liable?", "May I complain, and by when?", "By when must I ask for review,
or appeal?", "What can the Tribunal order?", "Can I enforce it?", "Am I protected for complaining?". No seat for the
respondent, the Commissioner, the Tribunal or the Supreme Court: their judgments and decisions are asked as facts. A
respondent's seat would be a welcome second layer (CLAUDE.md, 2026-10-21) but is not written.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no instrument sets a number the Act uses
  (penalty unit values are general law, not deposited).
- **The actors the text names.** Followed: the complainant, the respondent, the Commissioner, the Tribunal, the
  Supreme Court, the trade union, the organisation, the litigation guardian, the Minister.
- **Judgments answered conditionally.** Followed: "unreasonable", "reasonable person would have anticipated",
  "reasonably necessary", "unjustifiable hardship", "genuine occupational qualification", "in good faith", "satisfied",
  "in the opinion of the Commissioner", "fair", "public interest" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "prescribed attribute" (s 3, s 16), direct and
  indirect discrimination (ss 14, 15), sexual harassment (s 17(3)), victimisation (s 18(2)), "child" and "adult" (s 3,
  by age) are worked out from facts.
- **One case.** One course of conduct against one person, and one complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 3 (as used), 14, 15, 16, 17, 18, 19, 20, 21, 22; Part 5 Divisions 1-10 (ss 23-54) through one exception
question, and s 55; Division 11 as "an exemption granted covers it" and the s 59 review period; Part 6 as it meets the
complainant: ss 60, 60A, 62(1), 63, 64(1), (2), 65(3), (4), 66(1), 68(6), (7), 71(4), (5), 72, 73, 78(2), 78(4) with
100(2), 80(4), 89(1), (2), 90, 91(1), 92(1), 93, 94(4) and 76(4) (in enforcement), 99(3), 101; Part 7: ss 102, 104,
108(1).

**Regulative rules:** three, in `tad-rules.l4`.
- s 63: `PARTY the complainant MUST make the complaint WITHIN` the days to the last day, `LEST PARTY the Commissioner MAY
  accept the complaint out of time` (s 63(2)).
- ss 65(3), (4), 71(4), (5): `PARTY the complainant MUST apply to the Tribunal for review WITHIN 28`, `LEST BREACH ...
  BECAUSE` the complaint lapses (and s 73 bars another).
- s 100(2): `PARTY the complainant MUST appeal to the Supreme Court WITHIN 28`, `LEST BREACH ... BECAUSE` the time has
  passed.
Each is run by EVALTRACE inside an "on this day" question that takes plain dates; no exported question takes a DEONTIC
or an EVENT.

**Out, and why:**
- Parts 2 and 3 (the Commissioner's office and the Tribunal's functions), ss 1, 2, 4, 109-112, Schedules 1 and 2:
  machinery. Schedule 2 (complaints under the repealed Sex Discrimination Act 1994) and s 108(2) are long spent.
- ss 56-58 (applying for, granting and notifying exemptions): the applicant's process, not the person aggrieved's;
  only "an exemption in force covers it" (and the s 59 review period) is asked.
- ss 61, 62(2), 62A, 65A, 67, 68(1)-(5), 69, 70, 71(1)-(3), 74-77, 78(1), (3), 79, 79A, 81-85, 86A, 89(3)-(5), 91(2),
  92(2)-(4), 94(1)-(3), 96, 96A, 97, 98, 98A, 99(1), (2), 103, 103A, 107, 107A: the Commissioner's and the Tribunal's
  procedure and powers; where they matter to the person they are asked as facts (a referral, a dismissal, a finding).
- The offences (ss 75(2), 80(3), 92(4), 97(4), 98(4), 105, 106): prosecuted, not complained of; they bind the
  complainant as anyone else and could be a later layer.
- s 68(4)(c) and s 96 (costs under the Tasmanian Civil and Administrative Tribunal Act 2020): that Act is not
  deposited here.
- s 100(4) (appeals under the Supreme Court Civil Procedure Act 1932): procedure of another Act.
- Time stops: the Act has none for the s 63 limit; the Commissioner's late acceptance (s 63(2)) is the only way past it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 12 months after" (s 63(1)), "within 6 months after" (s 78(2)), "within N days after" (ss 59, 64(2),
  65(3), 71(4), 93(2), 100(2)) -- `the date n months after`, `the date n days after` -- the day of the event excluded,
  the last day the same day of the month n months later (the month's last day where it has no such day: 29 February
  2024 to 28 February 2025, 31 August to 28 February); D plus n days -- the event day included, or a month-end day
  rolling to the 1st of the next month. The Acts Interpretation Act 1931 (Tas) is not deposited.
- **F2** s 22(1) -- every question on discrimination and prohibited conduct other than inciting hatred -- outside the
  seven areas, NOTHING (a scope stated without "only") -- JUST FALSE.
- **F3** s 17(1), s 19 -- `s 17(1) -- offensive conduct`, `s 19 -- inciting hatred` -- prohibitions limited by their own
  words (the attribute or ground, the reasonable-person test, a public act, incitement): JUST TRUE inside, NOTHING
  outside -- JUST FALSE as flat negatives under ruling N2.
- **F4** s 18(1) "because" -- `s 18 -- victimisation` -- a detriment for another reason, NOTHING -- JUST FALSE.
- **F5** Part 5 -- `Part 5 -- the exception covers it` -- outside the ground or setting an exception names, NOTHING;
  its "if" failing, JUST FALSE; ss 23, 26, 29, 31, 35, 37, 38, 40, 43(a), 46, 52(a)-(c), 53 and a granted exemption have
  no "if" and answer only JUST TRUE or NOTHING -- every exception answering JUST FALSE outside its words ("this section
  gives no defence on these facts").
- **F6** s 104(1)(c), (3) -- `s 104 -- the organisation is liable` -- read literally: a contravention by a member,
  officer, employee or agent is itself a failure to "ensure that no member ... engages in" it, so the organisation is
  liable -- liability only where it also failed to make its people aware (1)(a) or to take reasonable steps (2).
- **F7** s 60(3) -- `s 60 -- the complaint may be made` -- a child (under 18) complaining without the Commissioner
  being satisfied of sufficient maturity, JUST FALSE ("may accept ... if") -- s 60(3) as only a power to accept, leaving
  the child's own complaint unanswered (NOTHING). A litigation guardian (s 60A) is not subject to it.
- **F8** s 62(1) "A complaint is to" -- `s 62 -- the complaint is in the required form` -- a bare "is to" not met,
  JUST FALSE -- NOTHING (the Act gives no consequence; the Commissioner may assist under s 62(2)).
- **F9** s 99(3) -- `s 99 -- the largest fine on the complainant in penalty units` -- not vexatious, 0 -- NOTHING (the
  Act is silent on other dismissals).
- **F10** ss 21, 102 -- `s 21 -- the helper is jointly liable`, `s 102 -- I am immune` -- outside their words (not
  knowingly; not in good faith; a claim not "only" because of the complaint), NOTHING -- JUST FALSE.
- **F11** s 64(1) -- `s 64 -- the Commissioner may reject the complaint` -- the Commissioner's opinion or satisfaction
  and the facts as one input ("the ground is made out") -- separate inputs for fact and opinion.
- **F12** s 29 -- the exception names no ground; read as reaching any ground (gender in practice) and only persons of
  12 or more: a person under 12, NOTHING -- confined to gender by its Division heading.
- **F13** s 89(1) -- `ss 89, 91, 92 -- the Tribunal may make the order` -- not substantiated after an inquiry, JUST
  FALSE for every order ("If the Tribunal finds"); s 91 (a duty, "is to refer") answered JUST TRUE where it applies --
  s 92's "substantiated complaint" read as not needing an inquiry (s 92 does not say "after an inquiry").
- **F14** s 90 -- `s 90 -- enforceable as a Supreme Court order` -- an agreement recorded by the Tribunal (s 94) is
  enforceable once filed, like a s 89(1) order (s 94(4)) -- s 90(1)(b) names only the s 76 record (finding 8).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.


Applied here: "prescribed attribute means" (s 3), "takes place if" (ss 14(2), 15(1), 17(3), 18(2)), "does not apply"
(ss 20(2), 51A(2), 55, 108(1)), "does not permit" (s 51A(3)), "only applies if" (ss 30(2), 33(2), 34(2), 44(2)), "may
not ... without" (s 60(4)), "is not entitled" (ss 68(6), 73), the "if" conditions of the exceptions and of ss 60(1),
60(3), 64(1), 80(4), 89, 90(2), 91(1), and the periods give `JUST FALSE`. `NOTHING` is answered where a prohibition,
grant or exception is limited by its own wording and the case falls outside it (*limited by its own wording*: ss 17(1),
18, 19, 20, 21, 102, 104, Part 5's grounds and settings, s 55's conduct, s 90's subject), outside the s 22(1) areas
(*scope limit without "only"*, F2), and for someone else complaining (*list not closed*, s 60(1)).

## What the Act turns out to say

1. **"Irrelevant medical record" is a prescribed attribute (s 16(r)) with no definition.** s 3 defines "irrelevant
   criminal record" at length but not its medical counterpart; it is asked as a fact.
2. **s 17(1) protects only some attributes, in an odd order.** It names "section 16(e), (a), (b), (c), (d), (ea), (eb)
   and (k), (f), (fa), (g), (h), (i) or (j)": offensive conduct based on industrial activity, political or religious
   belief or activity, an irrelevant criminal or medical record, or association (s 16(l)-(s)) is outside it, and the
   "and" between (eb) and (k) inside an "or" list reads as a drafting slip. Asserted (religious belief and industrial
   activity answer NOTHING).
3. **s 29 names no ground.** It sits in Division 2 ("Exceptions relating to certain attributes") but permits
   discrimination "in a competitive sporting activity by restricting participation to persons of one gender of 12 years
   of age or more", on any ground (F12). Asserted.
4. **s 104 makes an organisation liable for every contravention by its people, read literally.** (1)(c) requires it to
   "ensure that no member, officer, employee or agent ... engages in" discrimination, and (3) makes a non-complying
   organisation liable; a contravention is then always a non-compliance, and (2)'s "reasonable steps" never decides
   (F6). Asserted.
5. **The disclosure provisos differ.** ss 30(2) and 44(2) ask for the sources of the data "or" the relevant factors;
   ss 33(2) and 34(2) "and". s 30(2) applies to all of (1), including (1)(a) (prescribed standards), where no data are
   relied on; s 33(2) is confined to (1)(b). The encoding asks one "disclosed as required" fact for each.
6. **s 30(1)(a) misnames the Commonwealth Act** as the "Superannuation Industry Supervision Act 1993"; s 33(1)(a) has
   "Superannuation Industry (Supervision) Act 1993". The same Act is meant.
7. **s 107A(2) points to a provision that is gone.** It refers to "an inquiry held in public under section 85(1)", but
   s 85(1) was omitted in 2021 (No. 18 of 2021, s 16). Not encoded.
8. **s 90 does not fit a Tribunal agreement.** An agreement recorded by the Tribunal is enforceable "as if it were an
   order of the Tribunal under section 89(1)" (s 94(4)), but s 90(1) provides certification only for an order (by the
   presiding member) or a s 76 record (by the Commissioner). The encoding treats it as enforceable once filed (F14).
   Asserted.
9. **s 43(a) reads oddly:** the exception for "restricting participation to that person" on the ground of disability
   presumably means persons with the disability; it is asked as a setting.
10. **"Not accepted" is not defined.** Since 1 July 2025 the Act distinguishes a complaint "not accepted" from one
    "rejected" (ss 65, 72(1), (4)), but no section says when a complaint is not accepted rather than rejected (a late
    complaint the Commissioner declines under s 63(2) is the likely case). The review question takes the decision as a
    fact.
11. **"Political activity" and "religious activity" are circular** (s 3: "engaging in, not engaging in, or refusing to
    engage in, political activity"). Asked as facts.
12. **The referral clock runs from a notice the complainant does not receive.** s 78(2)'s 6 months run "after
    notification under section 67", which goes to the respondent; the complainant is asked for that day.
13. **The commencement day is not in the text** (s 2: "a day to be proclaimed"), so s 108(1) is asked as a fact.

## Before this is worth relying on

- An independent test pass and a lawyer's reading of the forks, above all F3 (s 17(1) and s 19 as NOTHING outside
  their words), F5 (the exceptions), F6 (s 104) and F7 (children).
- The Acts Interpretation Act 1931 (Tas) deposited, to settle how the periods are counted (F1), and the penalty unit
  value, so the fines can be given in dollars.
- The exceptions question is generic (a setting, a condition and a further condition, described per exception); a
  later pass could give each Division its own question with specific inputs.
- A respondent's seat (employers, service providers, clubs, schools), drawing on the same rules.
- The Tasmanian Civil and Administrative Tribunal Act 2020, which now governs the Tribunal's procedure, withdrawals
  (s 98A(4)) and costs (ss 68(4)(c), 96).
