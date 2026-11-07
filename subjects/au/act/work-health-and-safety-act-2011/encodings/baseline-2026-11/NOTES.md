# Work Health and Safety Act 2011 (ACT) -- baseline encoding, the worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

No encoding of this Act existed; this is the first. Focus: the provisions a person bringing or answering a claim meets.
The Act is large (278 sections and four schedules) and is mostly duties, participation machinery and enforcement powers;
it gives a worker only a few routes to a claim. The encoding takes those routes and what a worker meets on the way to
them, as whole Parts or Divisions where that is tractable (Part 3, Division 5.6, Part 6, Part 12, Divisions 2.6, 9.4, 13.1,
13.8, Schedule 4 penalties), and lists below what is out and why.

Modules:

- `whsact-dates.l4` -- the date helpers (built-in date functions only; no daydate, no `YMD`).
- `whsact-worker.l4` -- the worker's questions about being covered, an incident and its notification, stopping unsafe
  work, and what the Act does and does not give a worker (s 7, Part 3, Division 5.6, s 267, s 272, s 273).
- `whsact-claims.l4` -- the claims machinery: Part 6 civil proceedings and criminal-court orders, s 184 compensation from
  the Territory, Part 12 review, s 231 requests for prosecution, s 232 time for prosecutions, s 34A industrial
  manslaughter, and the Schedule 4 penalties.
- `whsact-worker-cases.l4`, `whsact-claims-cases.l4` -- the worked cases.

Three duties with fixed deadlines are regulative rules (`PARTY ... MUST ... WITHIN ... HENCE ... LEST BREACH ... BECAUSE`),
each run by EVALTRACE inside an exported question that takes only plain facts: the business's written notice of an incident
within 48 hours of the regulator's requirement (s 38 (4) (b), counted in hours); the applicant's commencement of a s 112
proceeding within 1 year (s 113 (1)); the regulator's written advice within 3 months of a request for a prosecution
(s 231 (2), encoded for what the person must be given and by when).

## Edition

- **Act:** Work Health and Safety Act 2011 (ACT), A2011-35, Republication No 30 (R30), effective 26 November 2025, last
  amended by A2025-30, as deposited at `../../registers/source-bundle/A2011-35.txt` (converted from the register's DOCX,
  which the register marks as an unauthorised version; the authorised text is the register's PDF).
- **Numbers set elsewhere:** the Act's own Schedule 4 sets the penalty amounts, the CPI indexation and the rounding; they
  are encoded. The Work Health and Safety Regulation 2011 (ACT), which prescribes further serious injuries and dangerous
  incidents (s 36 (1) (e), s 37 (1) (n)), the "prescribed purposes" of continuity (s 88), further reviewable decisions
  (table 223 item 15) and matters for s 184 (4), is **not deposited**: each answer that depends on it says so.
- **Legislation Act 2001 (ACT)** (time computation, "doctor", "nurse", "State"): not deposited; see fork F1.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 113 (1) last day one day late) was run once in a scratch copy, since deleted, and showed
as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `whsact-dates.l4` | 0 | 0 | 0 | 0 |
| `whsact-worker.l4` | 0 | 0 | 0 | 0 |
| `whsact-claims.l4` | 0 | 0 | 0 | 0 |
| `whsact-worker-cases.l4` | 0 | 0 | 70 | 70 |
| `whsact-claims-cases.l4` | 0 | 0 | 136 | 136 |

Every exported question has cases, with the edges: each limb of s 36 and the 48-hour edge (48 in, 49 out); each head of
s 35 with and without the "arising out of" condition and the serious-risk condition; written notice at hour 0, 48 and 49,
given and not given; the s 38 (7) record from 29 February; each condition of s 84 failing in turn and the prisoner bar;
each s 85 condition; every s 88 alternative-work case; every s 267 route; each element of s 112 and s 113 (presumption
rebutted, one and both limbs of the defence, the s 114 (3) bar, coercion and the s 108 (3) emergency direction); each
s 112 (3) order by kind of conduct and engagement, and the s 115 (b) bar; every s 115 case including a failed workers
compensation claim; s 113 (1) on the last day and the day after, from 29 February, and not yet commenced on the last day
and the day after; every table 223 class; internal review with a compliance period shorter, longer and equal to 14 days,
and a longer period allowed; ACAT review at 14 and 28 days and after a statement of reasons; every s 228 stay case; the
s 231 window on the day before 6 months, the first day, the last day and the day after, from 31 August (month-end) and
after an inquest; the regulator's 3 months from 30 November (ending 28 February) on the day and the day after; s 232 with
each period in turn the latest, industrial manslaughter, leave given and refused; each s 34A element missing in turn;
Schedule 4 for each category and the tiers used, with the s 4.5 rounding edges ($50 and $500 rounded down, $51 and $501
up, exactly $10 000).

**No mirror cases.** One seat.

## Seat

**The worker** (both modules): the person who carries out work for a business or undertaking in the ACT and is hurt, made
ill, put at risk, dismissed or disadvantaged there; the prospective worker refused a job; the person whose commercial
arrangement was ended (Part 6 covers them); and the family member asking about a worker who died (ss 34A, 231, 232).
"Am I a worker?", "Was my injury a serious injury?", "Did the business have to report it, and in time?", "May I stop unsafe
work, and what then?", "Can I sue under this Act?", "Can I take them to court for sacking me over a safety complaint, and
by when?", "What can the court order?", "Can I get the inspector's notice reviewed, and by when?", "Can I make the regulator
prosecute?", "How long have they got to prosecute?", "Could the death be industrial manslaughter?".

The business answering a Part 6 claim asks the same questions with the same answers; no second seat was written. The
regulator, the inspector, the DPP, the ACAT and the courts get no seat: their findings are asked as facts ("as the court
would find"), and their duties are encoded for what the worker must be given and by when.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. Schedule 4 is part of the Act. The Regulation is
  not deposited; where it would add to an answer the answer says so (NOTHING-kind).
- **The actors the text names.** Followed: the person conducting a business or undertaking, the officer, the worker, the
  health and safety representative, the regulator, the inspector, the DPP, the ACAT, the courts, the Territory.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether a concern is reasonable
  (ss 84, 85); whether it was too urgent to consult (s 85 (3)); whether a failure was unreasonable (s 88); what the
  defendant proves (s 113 (2), (3)); whether it is just to order compensation (s 184 (3)); the interests of justice
  (s 232 (3)); recklessness or negligence and substantial contribution (s 34A); the date one "ought to have known"
  (s 113 (1)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: worker (s 7, with s 5 (6)),
  serious injury or illness (s 36), dangerous incident (s 37), sexual assault incident (s 37A), notifiable incident (s 35),
  cease work (s 83), discriminatory conduct (s 105), prohibited reason (s 106), eligible person (s 112 (6), table 223),
  relevant time (s 224 (3)), causes death (s 34A (4)), the Schedule 4 amounts. Asked: "business or undertaking", whether
  someone has a "health and safety duty" (Part 2 not encoded), "doctor", "nurse", "officer", "category 1 or 2 offence"
  (s 231, as the person reasonably considers).
- **One case is the text's natural unit.** Followed: one worker and one incident, one dismissal, one decision, one offence.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed, within the focus.

## Scope

**In.**
- `whsact-worker.l4`: s 5 (6) and s 7 (worker); Part 3: ss 35, 36, 37, 37A, s 38 (4) (b), (7), (9); Division 5.6: ss 83-88,
  with s 103; s 267 (with s 260); s 272; s 273.
- `whsact-claims.l4`: Part 6: ss 105, 106, 108 (1) and (3), 111, 112, 113, 114 (2) and (3), 115; s 184; Part 12: ss 223
  (table 223), 224, 228, 229; Division 13.1: s 231 (1)-(2) and (3) (b), s 232; Division 2.6: s 34A (with s 34B named);
  penalties: s 31 and s 34A (imprisonment), Schedule 4 ss 4.1, 4.1A, 4.2 (tiers A, D, F as used by the sections named),
  4.4 and 4.5.

**Out, and why.**
- Part 2 duties (ss 13-29) and the offence elements of ss 31-33: they are the standards a business must meet, enforced by
  prosecution; the Act gives the worker no right of action for a breach (s 267, encoded). Whether a duty was owed and
  breached is asked as a fact in s 34A. A worker's damages claim is at common law or under the Workers Compensation Act
  1951 (which has its own encoding beside this one), not under this Act.
- s 104 and s 107 as offences, s 110 (proof in a prosecution), s 109 (misrepresentation: an offence only, with no civil
  route under s 112): the prosecutor's questions, not the worker's. Their maximum penalty is in the Schedule 4 question.
- Part 4 (authorisations), Divisions 5.1-5.5 and 5.7 (consultation, health and safety representatives and committees,
  issue resolution, provisional improvement notices) apart from s 85: participation machinery; a later layer could take
  them. s 85 is in because it decides whether a worker "ceased work under this division".
- Part 7 (WHS entry permits) and Division 13.7 (civil penalties): union and regulator proceedings; s 267 and s 260 are
  encoded for what they mean to the worker.
- Parts 8-11 (the regulator, inspectors' powers, notices, undertakings), apart from s 184 and the review of decisions.
- s 226, s 227 (the internal reviewer's own timetable), s 231 (2A) and (4)-(6) (updates and DPP advice "as soon as
  practicable", no fixed number), Divisions 13.2-13.6 (sentencing orders, infringement notices, corporate liability, the
  Territory and public authorities).
- Schedule 4 s 4.3 (civil penalty tiers), s 4.4 (3) (see fork F10), s 4.6; the tiers not used by the sections named.
- Schedules 1-3, the dictionary as such, regulation-making, approved forms, fees, codes of practice: machinery.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within N months/years after", "at least 6 months after", "within 14 days after" (ss 38 (7), 113 (1), 224, 229,
  231, 232) -- `whsact-dates.l4` -- the day itself excluded, the period ending on the same day of the month N months or
  years on, or that month's last day where it is shorter (29 February to 28 February) -- the Legislation Act 2001 (ACT)
  s 151 and following, not deposited, if they count otherwise.
- **F2** s 7 (2) -- `s 7 -- am I a worker` -- a police officer's answer is given first, whoever else they work for --
  the s 7 (1) answer for off-duty work for another business.
- **F3** s 36 (1) (e), s 37 (1) (n), s 35 -- `s 36 ...`, `s 35 ...` -- when (a) to (d) (or (a) to (m)) all fail,
  NOTHING-kind, because a regulation not deposited may add to the "means" definition -- the text's no.
- **F4** s 38 (4) (b) "within 48 hours" -- the regulative rule -- counted in hours from the requirement; hour 48 is in
  time -- counted in whole days.
- **F5** s 113 (1), s 231 (2) -- `s 113 (1) -- am I in time`, `s 231 (2) -- did the regulator answer in time` -- a step
  taken before the starting day is counted as taken on it (in time) -- premature.
- **F6** s 112 (6) -- `s 112 -- can the court make orders for me` -- a person who is neither affected nor an authorised
  representative: NOTHING-kind (a list not closed with "only") -- the text's no.
- **F7** s 223, table 223 -- `s 223 -- can I apply for review` -- the table read as closed: a worker not listed for the
  decision gets the text's no -- NOTHING-kind.
- **F8** s 228 (2), (3) -- `s 228 -- ...` -- for a prohibition or non-disturbance notice with no stay asked and none
  granted: "not stayed unless the reviewer stays it on its own initiative" -- "not stayed".
- **F9** s 232 (1) (c) -- `s 232 -- the last day for a prosecution` -- the person gives the latest of the three days
  (contravention, notice of it, agreed withdrawal); 6 months from that -- each day asked separately (same answer).
- **F10** Schedule 4 s 4.4 (3) -- `Schedule 4 -- the most the court can fine` -- not applied: the answer is this year's
  indexed amount even if lower than last year's -- the previous year's amount where higher; and for years before 1 July
  2024, NOTHING (earlier amounts are not in the deposited text).
- **F11** s 231 (1B) (b) -- `s 231 -- may I ask for a prosecution on this day` -- a request on the day the report is made
  or the inquest ends is in time -- only from the next day.
- **F12** s 224 (1) (b) "such longer period that the regulator allows" -- `s 224 and s 229 -- the last day ...` -- taken as
  a number of days from the day of notice, used where longer than the relevant time -- a period from another day.
- **F13** s 224 (3) (a) "the period specified in the notice for compliance" -- the same function -- asked as a number of
  days; the notice itself states a day (s 192 (1) (d)) -- counted from the day of issue rather than from notice.
- **F14** s 84 -- `s 84 -- may I stop unsafe work` -- a person who is not a worker: NOTHING-kind (a scope limit with no
  "only") -- the text's no.
- **F15** s 272, s 273 -- `s 272 -- is the term void`, `s 273 -- ...` -- outside the section's words: NOTHING (silent) --
  JUST TRUE / JUST FALSE by contrast.
- **F16** s 112 (3) (c) -- `s 112 (3) -- which orders ...` -- reinstatement or employment orders only for s 112 (2) (a)
  conduct and for an employee or prospective employee; a contractor gets neither -- reading "worker" in (c) (ii) widely.

Sites decided without a fork line: the "means" definitions in ss 7, 105, 106, 37A, 34A (4) answer FALSE when they fail;
flat negatives (s 38 (9) (b) "must not", s 103 "nothing in this part applies", s 114 (2), (3) "cannot", s 115 "cannot",
s 267 "nothing ... is to be construed", s 273 "must not") are the text's no; s 112 (4) "only if" and s 113 (3) "it is a
defence ... if the defendant proves" follow the 2026-11-05 rulings ((b) of the second: "this section gives no defence on
these facts" is the defence failing, so the claim proceeds).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` answers at s 36 and s 35 (F3), s 112 (6) (F6), s 84 (F14), table 223 item 15,
s 267 for Part 7, s 232 (4), s 38 (9) for incidents that are not sexual assault incidents, s 272 and s 273 (F15), and
Schedule 4 (F10). Most questions answer with a choice from a list; the answer marked "NOTHING-kind" is the NOTHING answer,
and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (1 year, 48 hours, 3 months, the s 231 window, the s 232 periods, the review periods) are
JUST FALSE ("out of time", "too late", "late") outside them under ruling (a).

## What the Act turns out to say

1. **The industrial manslaughter penalty is not indexed.** Schedule 4 s 4.4 (1) indexes "each monetary penalty set out in
   sections 4.1, 4.2 and 4.3"; the industrial manslaughter monetary penalty is in s 4.1A (inserted by A2024-15), which is
   not listed, so it stays $18 000 000 while the category 1 penalty for a body corporate ($10 425 000 before indexation)
   rises with the CPI. Asserted.
2. **Schedule 4 s 4.5 leaves exactly $10 000 out** ("less than $10 000" in (a), "more than $10 000" in (b)). Nothing turns
   on it, since $10 000 is a multiple of both $100 and $1 000. Asserted.
3. **Schedule 4 s 4.3 speaks of "an offence"** for the WHS civil penalty tiers, though a contravention of a civil penalty
   provision "is not an offence" (s 257). Not encoded (civil penalties are out); for the reviewer. s 4.1 (b) for category 1
   carries a stray comma (", ;"); harmless.
4. **s 228 (6) (a) refers to "the prescribed period for applying for an external review"**, but s 229 (2) fixes those
   periods in the Act itself; no period is "prescribed". Not encoded (s 228 (6)); for the reviewer.
5. **s 231 (3) mentions "an industrial manslaughter offence"**, but a request under s 231 (1) can only concern a category 1
   or category 2 offence, so (3) can only reach industrial manslaughter through the regulator's own advice. Encoded as
   written: the request window is for category 1 and 2 offences.
6. **s 112 (3) (c) speaks of "a worker who was or is an employee or prospective employee" and then of "the prospective
   worker"**, where s 111 (b) speaks of "a person who was or is an employee or prospective employee". Encoded alike (fork
   F16): reinstatement for an employee, employment for a prospective employee, neither for a contractor.
7. **The civil claim has a 1-year limit from knowledge** (s 113 (1)), much shorter than the general limitation periods,
   and s 115 (a) bars it while a Commonwealth or State claim "in relation to the same matter" is pending; s 115 (c) spares
   a failed workers compensation claim, but (a) does not spare a pending one. Whether a workers compensation claim is "the
   same matter" as a discriminatory dismissal is not said; the encoding takes the person's own answer. Asserted (the
   failed workers compensation claim does not bar).
8. **s 114 (3) bars a s 112 order only for conduct in s 112 (2) (a) and (b)**; coercion under s 108 has no s 111
   counterpart, so an earlier s 111 order does not stop a coercion claim. Asserted.
9. **s 232 does not apply to industrial manslaughter** (s 232 (4)); the Act sets no time limit for that prosecution.
   Asserted.
10. **s 38 (7)'s 5 years run "from the day that notice of the incident is given"**: if notice is never given, the Act sets
    no record-keeping period at all (the failure to notify is the offence). Not encoded beyond the question as asked.
11. **s 88 protects continuity only "for prescribed purposes"**, and the Regulation that prescribes them is not deposited;
    the answer says so.

## Before this is worth relying on

- The Work Health and Safety Regulation 2011 (ACT), for s 36 (1) (e), s 37 (1) (n), s 88, table 223 item 15 and s 184 (4).
- The Legislation Act 2001 (ACT), for the counting of periods (fork F1) and the terms asked as facts.
- The CPI numbers for each year (Schedule 4 s 4.4), and the regulator's notice of the indexed amounts (s 4.6), to check
  the penalty question against.
- A lawyer's view on forks F3, F6, F7, F10, F12, F13 and F16 and findings 3-7; an independent test pass and a human gate.
