# Health Complaints Act 1995 (Tas) -- baseline encoding, the complainant

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The date helpers are in a small module
(`hca-dates.l4`, built-in date functions only, no daydate), the rules in `hca-rules.l4`, and the complainant's questions
in `hca-seat.l4`, which imports the rules and restates none. The cases are in `hca-cases.l4`. The shape follows the
Fatal Accidents Act 1934 (Tas) and Limitation Act 1974 (Tas) baselines.

**Why this Act, in a claims set.** The focus was a claims route not named in the list of claims work (workplace and road
injury, medical negligence and the rest). A complaint to the Health Complaints Commissioner is the main non-court route
for a patient harmed by a health service in Tasmania, and it runs beside a medical negligence claim: the Commissioner
cannot award damages, but conciliation can end in a binding agreement (s 39), a complaint must be dismissed once a court
has commenced to hear a proceeding on the same subject (s 25(5)(f)), and what is said in conciliation cannot be used in
court (s 37). The subject was deposited under the heading "health complaints and health records Acts"; Tasmania has no
separate health records Act in the deposit, and the Act's own records route is the s 23(1)(h) ground (access to the
user's records), encoded here. The Personal Information Protection Act 2004 (Tas) is deposited separately.

## Edition

- **Act:** Health Complaints Act 1995 (Tas), No. 95 of 1995, consolidated version published 2025-01-02 and current at
  point in time 2026-11-06, as deposited at `../../registers/source-bundle/act-1995-095.txt` (text sha256
  a46780a6...a5d7c5), retrieved from legislation.tas.gov.au on 6 November 2026. It includes the Health Complaints
  Amendment Act 2018 (No. 19 of 2018, in force 31 December 2024: health care workers, codes of conduct, prohibition
  orders, s 22A, s 25(5)(ca)).
- **Numbers set elsewhere:** none used. The Act fixes its own periods (2 years, 45, 14 and 15 days, 48 hours, 6 months)
  and its fines in penalty units. The value of a penalty unit (Penalty Units and Other Penalties Act 1987) is not
  deposited: fines are given in units. The regulations (codes of conduct, services prescribed as not health services,
  prescribed providers, witness expenses) are not deposited: where a rule depends on them, the fact is asked.
- **Borrowed terms asked as facts:** "registered health practitioner" and "health care worker" (registration under the
  Health Practitioner Regulation National Law); "power of attorney"; "care of the affairs ... under any other law or an
  order of a court"; "code of conduct" (prescribed by regulation); "reprisal" beyond the s 68(2) examples.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hca-dates.l4` | 0 | 0 | 0 | 0 |
| `hca-rules.l4` | 0 | 0 | 0 | 0 |
| `hca-seat.l4` | 0 | 0 | 0 | 0 |
| `hca-cases.l4` | 0 | 0 | 137 | 137 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; each
s 22 category, with the patient at 13, 14, 17 and 18; the last day of the 2 years and the day after (10 / 11 March 2026
for awareness on 10 March 2024; 28 February / 1 March 2026 for awareness on 29 February 2024), and both clocks for a
health care worker; the 14th day after a warning and the day after, a requirement met late, and a warning given before
or on the last day of the period; 45 days, 45 + 45, an extension of 60 (counted as 45) and an extra (1CA) extension;
48 and 47 hours, and across a month end; a written agreement on the 14th and 15th day; the provider's 45th day and the
day after, 15 days' extension and 20 (counted as 15); the s 68(5) defence with and without its third limb; the s 71 6
months from 31 August (to 28 February).

## Seat

**The complainant** (`hca-seat.l4`): the person who complains to the Health Complaints Commissioner about a health
service -- usually the patient (the "health service user"), or a parent, appointee, attorney, carer or other person s 22
lets complain for the patient, or anyone complaining under s 22A that a health care worker breached a code of conduct.
"Is this a health service?", "Can I complain?", "Is this a ground?", "What form?", "By when must I complain, and am I in
time?", "Must my complaint be dismissed?", "By when must I meet a requirement after a warning, and can I be dismissed
for not meeting it?", "By when must it be assessed and must I be told?", "If I withdraw, by when must the provider be
told?", "Can it go to conciliation, must I attend, can I be represented, can what is said be used in court, is our
agreement binding?", "Do I get the report, the statement of decision?", "By when must the provider answer the notice,
and has it?", "Must my identity be kept from the provider?", "Can I be sued for complaining?", "Was the intimidation or
reprisal an offence, and by when must it be prosecuted?".

No seat for the health service provider or the health care worker in this baseline (each could have one beside it: the
provider's s 32A, s 56(3) and s 66 duties; the worker's prohibition orders, public warning statements and the one-month
appeal of s 56AAG), nor for the Commissioner, a conciliator, a registration board, the Minister or a court (officials):
their opinions, satisfactions and beliefs are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; the regulations
  (not deposited) set none that is used.
- **The actors the text names.** Followed: the complainant, the health service user, the health service provider, the
  health care worker, the Commissioner, the conciliator, the parties to a conciliation.
- **Judgments answered conditionally.** Followed: every "satisfied", "of the opinion", "considers", "believes on
  reasonable grounds", "good faith", "reasonable excuse" and "reasonable ground" is an input.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "health service" (s 3 with Schedule 1) and
  "child" (s 3) are worked out; "health care worker" and the borrowed terms above are asked.
- **One case.** One complaint by one complainant.
- **The Act's terms with plain glosses.** Followed, in each `@desc` ("health service user" glossed as the patient).
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 ("health service", "child") with Schedule 1; ss 22, 22A (who may complain); s 23(1) with s 25(5)(b)
(grounds); s 23(3)-(5) (form); s 25(5)(c), (ca), (6) (the 2-year limit); s 25(5)(d)-(j) (other grounds for mandatory
dismissal); ss 24, 25(7) (requirement for further information); s 25(1), (1C), (1CA) and s 27 (assessment and notice);
s 30(1), (2) (withdrawal); s 25(1A)(b)(i), (4) (referral to conciliation); s 32A (initial meeting); s 33
(representation); s 37(1) (conciliation not admissible); s 39 (binding agreement); s 40(1) with s 55(2)(f) (the report
to the complainant); s 56AAD(2)(a) (the statement of decision); s 56(3), (4) with s 13(4)(b) (the provider's answer);
s 64 (identity); ss 67, 68 (intimidation, reprisals); s 71 (prosecution time); s 73 (protection from civil actions).

**Regulative rules:** four, each run by EVALTRACE inside an exported question that takes only plain facts.
- s 25(5)(c), (ca): `PARTY the complainant MUST make the complaint WITHIN` the days to the last day of the 2 years,
  `LEST BREACH ... BECAUSE` the Commissioner must dismiss; run in `Is my complaint in time`.
- s 25(7): `PARTY the complainant MUST satisfy the Commissioner's requirement WITHIN 14` from the warning; run in `Can my
  complaint be dismissed for not meeting the requirement on this day`.
- s 39(2): `PARTY the parties to the conciliation MUST put the agreement in writing WITHIN 14`; run in `Is our
  conciliation agreement binding`.
- s 56(3): `PARTY the health service provider MUST advise the Commissioner of the action taken WITHIN` 45 (up to 60)
  days; run in `Has my provider answered the notice in time`.

**Out, and why:**
- Machinery: ss 1, 2, 4, 5-16 (the Commissioner, staff, committees, reports to Parliament, delegation, protection of
  officers), ss 17-21 (making the Charter), s 77, s 79, s 81 and Schedule 3; ss 76, 80 and Schedule 2 are repealed or
  spent.
- s 23(2) (complaints about circumstances before commencement): the commencement day is proclaimed and not in the
  deposit, and the provision is spent in practice.
- s 23(6), (7) (telling the Commissioner of a change of name or address): a bare duty with no period or consequence;
  noted, not asked.
- Powers exercised over the complainant only as one of many persons: s 26 (enquiries), ss 43-54 (investigation powers,
  search warrants, privilege, Supreme Court applications), s 46(3), s 70 (offences of not providing information), s 48
  (witness expenses: the amounts are prescribed and not deposited).
- The Commissioner's internal steps that give the complainant nothing to ask: ss 24A, 25(1B), (2), (2A), (3), 25A, 28,
  29, 29A, 29B, 31, 32, 34-36, 38, 41, 42, 49, 50, 59-62D, 63, 65, 72, 74, 75, 78. s 35(3) (a copy of the conciliator's
  results report "as soon as practicable") and s 56(1)(b) (advice that a notice was given: a "may") have no period.
- Division 5 of Part 6 (codes of conduct, interim prohibition orders, prohibition orders, public warning statements,
  s 56AAF, the s 56AAG appeal) as they bear on the health care worker: a worker seat, not the complainant's; only
  s 56AAD(2)(a) is in. s 66 (returns by prescribed providers): a provider duty, and the providers and particulars are
  prescribed.
- Part 7 (registration boards) and s 56AA: dealings between the Commissioner and the boards and the National Law.
- Damages: the Act gives none. A negligence claim is the general law's, with its time limit in the Limitation Act 1974
  (Tas) (encoded at `subjects/au/tas/limitation-act-1974/encodings/baseline-2026-11/`).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 25(5)(c), (ca) "more than 2 years before"; s 71 "within 6 months after" -- `the corresponding day ... months
  after` -- the period ends on the same day of the month 2 years (6 months) later, or that month's last day if shorter
  (awareness on 29 February 2024: last day 28 February 2026) -- the last day the day before (the Acts Interpretation Act
  1931 (Tas), not deposited, governs).
- **F2** s 22(k) -- `ss 22, 22A -- I am entitled to complain` -- a person outside (a)-(j) whom the Commissioner has not
  permitted gets JUST FALSE ((k) exhausts "a person other than ... (a) to (j)", and s 25(5)(a) dismisses a complaint by
  a person not entitled) -- NOTHING (a list not closed with "only").
- **F3** ss 22A, 23(1), 25(5)(b) -- `ss 23(1), 25(5)(b) -- the complaint discloses a ground` -- a complaint that is only
  of a code-of-conduct breach gets NOTHING (the text conflicts, finding 2) -- JUST FALSE (s 25(5)(b) read literally) or
  JUST TRUE (s 22A read as adding a ground).
- **F4** s 25(1C) "an additional period not exceeding 45 days" -- `s 25(1) -- the last day for assessment` -- an
  extension stated as more than 45 days counts as 45; (1CA) extensions add without limit -- the excess extension void
  as a whole.
- **F5** s 30(2)(a) "notify that provider of the withdrawal within 14 days" -- `s 30(2)(a) -- the last day to tell the
  provider` -- 14 days counted from the complainant's written notice of withdrawal -- from the Commissioner's receipt of
  it (the Act does not say).
- **F6** s 32A "must attend an initial meeting, but ... either party may withdraw from the conciliation process at any
  time" -- `s 32A -- I must attend` -- the initial meeting is a duty (JUST TRUE) -- "at any time" read as letting a party
  withdraw before the initial meeting.
- **F7** s 33 "may not be represented ... except where" -- `s 33 -- I may be represented at conciliation` -- the
  exception once met gives JUST TRUE -- NOTHING (the exception only lifts the bar; the Commissioner's allowance is still
  needed). Exactly 48 hours counts ("not less than").
- **F8** s 39(1), (2) "may be put in a form that is binding ... not binding unless" -- `s 39 -- our conciliation
  agreement is binding` -- in writing within 14 days and put in a binding form: JUST TRUE; in writing in time but not in
  a binding form: NOTHING (the general law of contract) -- JUST TRUE once (2) is met.
- **F9** s 56(4) -- `s 56(3), (4) -- the days the provider has` -- an extension counts only if the provider's written
  request reached the Commissioner before the 45 days ended, and at most 15 days -- an extension granted on a late
  request still effective.
- **F10** s 25(7)(d) "the requirement is unsatisfied" -- `s 25(7) -- the Commissioner may dismiss my complaint on that
  day` -- read on the day asked about, so a requirement met late (after the 14 days) but before that day bars dismissal
  -- read at the end of the 14 days.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definition of "health service" with its "excluding" and "does not include" (JUST FALSE); the
"if" and "where" conditions of ss 22(b)-(f), (k), 25(1A), 25(5), 25(7), 32A, 55(2)(f), 56AAD(2)(a), 64 (JUST FALSE when
they fail, except as the forks say); the flat negatives of s 25(4) ("must not refer"), s 33 ("may not be represented"),
s 37(1) ("not admissible") and s 39(2) ("not binding unless"); the periods of ss 25(5)(c), 25(7), 39(2), 56(3). The
s 67(2) and s 68(5) defences answer "this section gives the person a defence on these facts" or, when not made out, the
offence (never "no defence at all"). `NOTHING` is answered for a s 22A-only ground (F3), a statement made outside
conciliation (s 37: silent), an agreement outside conciliation or not put in a binding form (s 39(3), F8: points
outside), an interim prohibition order (s 56AAD: silent), the identity question without the Commissioner's belief
(s 64: silent), s 73 without good faith (points outside), and the s 30 date where the provider was never notified (no
duty).

## What the Act turns out to say

1. **Any patient may complain, whatever their age; a parent of a 14- to 17-year-old may not.** s 22(a) entitles "the
   health service user" with no age limit, so s 22(b)(iii) (a child the Commissioner thinks capable) adds nothing on its
   face. A parent or guardian is entitled only for a child under 14 (b)(ii); for a child of 14 to 17 the parent needs the
   child's appointment (b)(i) or the Commissioner's permission (k). Asserted.
2. **A code-of-conduct complaint and the grounds do not line up.** s 22A (2018) lets "any person" complain that a health
   care worker breached a code of conduct, and s 25(5)(a) and (ca) were amended for it, but s 25(5)(b) still makes the
   Commissioner dismiss a complaint that "does not disclose a subject matter of complaint referred to in section 23",
   and s 23(1) is limited to persons entitled "under section 22". A complaint only of a code breach is, read literally,
   to be dismissed. Most code breaches will also be a s 23 ground; the investigation power of s 40(1)(e) runs "with or
   without a complaint" anyway. Possibly a drafting gap. Asserted as NOTHING (F3).
3. **Two clocks for a complaint about a health care worker.** s 25(5)(c) (the user's awareness) is not limited to
   complaints about registered providers, so for a complaint about a health care worker it runs beside (ca) (the
   complainant's awareness), and the earlier ends the time. (ca) can only shorten the time, never lengthen it: a
   complainant who learned of it later than the patient is still bound by (c). Asserted.
4. **Suing ends the complaint only once the hearing starts.** s 25(5)(f) requires dismissal when "a court has commenced
   to hear" a proceeding on the subject matter, not when one is filed. A patient may complain and sue in parallel until
   trial; s 37 keeps conciliation admissions out of the suit. Asserted.
5. **A complainant whose complaint leads to a code-of-conduct investigation is not on the report list.** s 55(2)(f)
   gives the complainant a copy only for investigations under s 40(1)(b) or (c), not (e), though s 56AAD(2)(a) gives the
   complainant the statement of decision if a prohibition order results. Asserted.
6. **Schedule 1 includes services not for anyone's health.** Item 11A (temporary storage of human remains at a hospital)
   and item 5 (laundry, catering) are "included", so a complaint about them lies, though the s 3 head speaks of "the
   benefit of human health". The compensation opinions (workers compensation, asbestos) are excluded by Part 2: an
   injured worker cannot complain under this Act about an independent medical opinion for the claim. Asserted.
7. **Either 6 months will do for a prosecution.** s 71 gives two alternatives, so the later governs: an offence the
   Commissioner learns of late can be prosecuted up to 6 months after learning of it, without outer limit. Asserted.
8. **No penalty for missing the initial conciliation meeting.** s 32A says the parties "must attend" but attaches no
   penalty, and s 70 penalises failures to attend only "for the purpose of providing information". Not asserted.
9. **No penalty units value in the Act.** Fines are in penalty units; the dollar amount is set elsewhere (not deposited).

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The Acts Interpretation Act 1931 (Tas) for reckoning periods (F1, F5) and the Health Complaints Regulations (codes of
  conduct, prescribed services and providers), if deposited.
- A lawyer's view on forks F2, F3, F6-F10 and findings 1-5; an independent test pass and a human gate.
- Seats for the health service provider and the health care worker, if wanted.
