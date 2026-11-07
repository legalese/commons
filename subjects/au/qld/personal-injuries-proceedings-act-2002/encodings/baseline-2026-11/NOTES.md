# Personal Injuries Proceedings Act 2002 (Queensland) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The dates are in `pipa-dates.l4` (built-in
date functions only, no daydate), the rules and the claimant's exported questions in `pipa-claimant.l4` (each exported
question calls a rule defined beside it), and the worked cases in `pipa-cases-claimant.l4`.

The Act is the pre-court gate for most Queensland personal injury claims outside the motor vehicle and workers'
compensation schemes: public liability, medical negligence, assaults, institutional abuse. Before suing, the claimant
gives a notice of claim in two parts (s 9), within time limits, with a separate first step for medical negligence
(s 9A) and for a child injured by medical treatment (division 1A); the parties exchange documents (division 2); they
hold a compulsory conference and exchange mandatory final offers (division 4); the claimant then starts the proceeding
within a set time (s 42), may do so after the limitation period (s 59), and the costs follow the final offers (s 56).
The Act is large (four chapters, about 150 sections); the claims machinery a claimant meets in chapter 2 is encoded,
and the rest is listed below with reasons.

## Edition

- **Act:** Personal Injuries Proceedings Act 2002 (Qld), Act No. 24 of 2002 (`act-2002-024`), the version in force from
  29 October 2026, which was the current in-force version on 6 November 2026, deposited at
  `../../registers/source-bundle/act-2002-024.txt` (text sha256 `26911536f64d6d1db3d320371768305119def79a9003dc61854259a54e10aa62`
  of the committed file, per its `.meta.json`; a Windows checkout with CRLF line endings hashes differently). A
  plain-text conversion of the Queensland Legislation HTML view, not the authorised PDF.
- **Numbers set elsewhere, not deposited:**
  - the **Personal Injuries Proceedings Regulation**, which may prescribe periods the Act otherwise fixes by a fallback
    ("within the period prescribed under a regulation or, if no period is prescribed, within 1 month after ..."). The
    Act's fallback is taken everywhere (fork F3); a prescribed period would change those answers. The time to add
    another respondent (s 14(1)) and to notify the other parties (s 14(3)(b)) exist only in the regulation, so they are
    not encoded;
  - the **Minister's notice under s 75A** fixing the lower offer limit, the upper offer limit and the declared costs
    limit for each financial year (with s 91 carrying on the amounts last prescribed by regulation). Asked as numbers.
- **Borrowed, and asked as facts:** "legal disability" (the Limitation of Actions Act 1974, s 19(4)); the limitation
  period of the claim (Limitation of Actions Act 1974, s 59); which scheme applies to an injury (Motor Accident Insurance
  Act 1994, Workers' Compensation and Rehabilitation Act 2003 chapter 5, and the others in s 6(2), (3), (5)); "health
  service complaint" and its time (Health Ombudsman Act 2013 and its predecessors); "law practice", "community legal
  service" (Legal Profession Act 2007). All are deposited or indexed under their own subjects in `subjects/au/qld/` but
  not imported (IMPORT cannot reach another subject's folder).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied". A deliberately wrong
assertion added to a scratch copy of the case file was reported as an error, so the assertions do bite.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pipa-dates.l4` | 0 | 0 | 0 | 0 |
| `pipa-claimant.l4` | 0 | 0 | 0 | 0 |
| `pipa-cases-claimant.l4` | 0 | 0 | 189 | 189 |

Every exported question has cases, with the edges: the last day and the day after for part 1, the initial notice, the
parent's notice for a child, the claimant's disclosure, the final offer bar (day 14 and day 15), s 42 (day 60 and 61,
and a court-fixed limit) and s 59 (6 months on, from part 1 and from leave); month ends (31 January plus 1 month, 31 May
plus 9 months, 29 February plus 12 months and plus 6 years); a legal disability ending; a response to part 1 on the last
day and the day after; the lower offer limit exactly and one dollar over, the upper offer limit exactly and one dollar
over; 200 and 201 pages; a panel of 2 with and without 3 available.

## Seat

**The claimant** (`pipa-claimant.l4`): the injured person who seeks damages for personal injury in Queensland, or the
person who claims for them (a parent for a child, the dependants or estate for a death: "claimant means a person by
whom, or on whose behalf, a claim is made"). "Does the Act apply to me?", "To whom, and by when, must I give my notice of
claim?", "What if I am late?", "What must I give the respondent, and what must it give me?", "Must I go to its
examination?", "When can I call the compulsory conference?", "When may and should I start my proceeding?", "Can I sue
after the limitation period?", "Who pays the costs?".

The respondent (usually through its insurer) has duties the Act names, but they are encoded only as what the claimant
is owed and by when; no respondent seat is written in this baseline. No seat for the court, the Crown solicitor, the
Minister, the Legal Services Commissioner or the law practice.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Departed from where they are not deposited: the
  regulation (fork F3) and the Minister's s 75A notice (asked).
- **The actors the text names.** Followed: the claimant, the parent or legal guardian, the respondent, the proposed
  respondent, the court, the Crown solicitor, the health service chief executive.
- **Judgments answered conditionally.** Reasonable excuse, proper reason, "unreasonable or unnecessarily repetitious",
  "as soon as practicable", "ought reasonably to have known", urgent need, terminal condition, leave, waiver and the
  court's orders are asked, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "complying part 1 notice of claim" in its
  effect (s 18), "relevant day" (s 36(3)), "mandatory final offer" timing, "abuse" (offered in the choice), "medical
  incident" (offered in the choice). Asked: legal disability, the limitation period, the scheme that applies.
- **One case.** One claim by one claimant against one respondent (with the multi-respondent variants of s 36(3) and
  s 42(2) asked as facts).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Commencement, regulation-making, approved forms, the s 75A indexation
  procedure and the transitional chapter are out.

## Scope

**In (chapter 2, the claims procedure as the claimant meets it):**
- s 6 (application: what the Act covers and excludes; s 6(4) as it switches off s 56);
- s 9(1), (3), (3A), (5), (6), (8), (9A), (9C), s 9A(2), (4), (6), (6A), (7), (9) (the notices: to whom, by when, if
  late), with s 10(1) and s 13 as they fix the day part 2 runs from, s 18 (whether a defective part 1 stops the claim),
  s 19 (legal disability);
- division 1A, ss 20B-20J (a child injured by medical treatment: the parent's deadline and what follows lateness);
- s 20(1), (4) (the respondent's answer on liability and offer, and my answer to an offer);
- division 2: s 22(5), (6), (8) (my disclosure and its deadlines), s 24 (reimbursing a joint report), s 25 (examination
  at the respondent's request), s 27(2) and s 29A(5) (what the respondent owes me, by when, and the 50c a page), with
  s 32 and s 35 as consequences;
- division 4: s 36(2), (3) (calling the conference), s 37(1) (material 7 days before), s 39(1) and s 40(4), (9) (final
  offers and the bar while they are open), s 42 (time to start, and its consequences);
- division 5: ss 43, 44 (urgent proceedings), s 44(7) (the 7 days to answer);
- part 3: s 48(1) (interest and costs for my default), s 56 (costs by reference to the final offers), s 59 (starting
  after the limitation period).

**Regulative rules: six**, each run by EVALTRACE inside the exported questions, which take only dates, numbers, yes/no
facts and choices:
- s 9(3), (5): I DO give part 1 WITHIN the days; LEST I MUST give a reasonable excuse (the duty continues);
- s 9A(4), (6): the same for the initial notice;
- s 20C(1), 20D: my parent MUST give part 1 WITHIN the days; LEST the respondent MAY apply for the claim not to proceed;
- s 22: I MUST give the documents or information WITHIN the days; LEST BREACH (the consequences are worked out beside);
- s 40(4): I SHANT start my proceeding WITHIN 14 days of the final offers;
- s 42: I DO start my proceeding WITHIN the days; LEST BREACH (only that the time was not met: s 42(4) keeps the door
  open).

**Out, and why:**
- Division 1AA (ss 8A-8F), ss 9B, 9C, 13A, 61 (law practice certificates): duties on the claimant's lawyers, enforced by
  penalties and the Legal Services Commissioner. s 9B gives the claimant a refund of all fees within 14 days where the
  lawyer's failure to give a certificate leads the claimant to terminate the engagement; it is a claimant entitlement
  and a candidate for a later layer.
- ss 10(2)-(5), 11, 12, 14-17 (the respondent's responses in detail, adding respondents and contributors): s 14's time is
  set only by the regulation (not deposited); the rest is the respondent's and contributors' procedure. ss 10(1) and 13
  are in as they fix the part 2 day.
- ss 20(2), (3), (5), 21, 23 (other than as context), 28, 29, 30, 31, 33, 34: the respondent-contributor exchanges,
  privilege and the respondent's offence. s 29(2)(b) is the subject of finding 3.
- ss 37(2)-(5), 38, 40(1)-(3), (5)-(8), 41, 47, 48(2), 57, 60: the content of the certificate of readiness, the conduct
  of the conference (including the duty to attend and participate, s 38(6)), the form of offers, contribution offers,
  summary judgment, the respondent's default, fraud.
- Chapter 3 (advertising, touting, claim referrals, the s 71E costs cap, reporting, offences): conduct rules for
  lawyers and others, with penalties; the s 71E cap is the Legal Profession Act 2007 s 347 formula, not this Act's.
- Chapter 4 (transitional provisions for incidents before 2002-2006), s 75A (the indexation procedure), ss 1-5, 7, 8,
  74, 75: machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** every "within N days after X" -- `the day N days after` -- the day X is not counted; the last day is X + N --
  the Acts Interpretation Act 1954 (not deposited) governs, and could count otherwise in a case not tested here.
- **F2** every "N months after", "6 years after" -- `the date N months after` -- the same day of the month N months
  on; the last day of that month where it has no such day (31 May + 9 months = 28 February) -- the first day of the
  next month.
- **F3** every period "prescribed under a regulation or, if no period is prescribed, ..." (ss 9(7), 10(1), 20(1), (4),
  22(5), (6), 27(2)) -- the Act's fallback period -- a period prescribed by the regulation, not deposited.
- **F4** s 9(3)(b), 9A(4)(b) "the day the claimant first instructs a law practice ... and the person ... is identified"
  -- `ss 9(3), 9A(4), 19 -- the last day` -- 1 month from the later of the two days -- 1 month from the instruction
  only, with "and ... is identified" a condition that the limb applies at all.
- **F5** s 19(2) with s 9(3) -- same function -- under a legal disability, neither limb's period starts before the
  disability ends; with symptoms not immediately apparent, the 9 months run from the later of the first symptoms and
  the end of the disability -- the substitution in s 19(2) reaches only "the day the incident ... happened", leaving the
  1-month limb running from the instruction even during the disability.
- **F6** s 13 with s 9(3A)(b) -- `s 9(3A) -- the last day for part 2` -- the presumption arises on the day after the
  last day for a response; a late response is not compliance with s 10(1) -- the presumption arises on the last day
  itself (one day earlier).
- **F7** s 20C(1) "before the earlier of the following days" -- `s 20C(1) -- the last day for my parent` -- the last
  day is the day before that earlier day -- "before" read as "by" (one day later), as s 9(3) "within the period ending
  on" would give.
- **F8** s 22(8) "fails ... to comply fully with a request by a respondent under this section" -- `ss 22(8), 32, 35 --
  if I miss the time` -- costs liability only for the request duties (s 22(1)(b), (2)), not for the copies of
  s 22(1)(a) or the change notice of s 22(6) -- "request" read loosely to cover every s 22 duty (finding 1).
- **F9** s 36(2)(b) "if the relevant day has passed" -- `From when may I call the compulsory conference` -- from the
  day after the relevant day -- on the relevant day itself.
- **F10** s 37(1) "At least 7 days before the compulsory conference is held" -- `By when must I give my material
  before the conference` -- on or before the conference day minus 7 -- 7 clear days (minus 8).
- **F11** s 40(4) "must remain open for 14 days" -- `s 40(4) -- not while the offer is open` -- the day of the offer is
  day 0; open through day 14; a proceeding may be started from day 15 -- open from the moment made until the same time
  14 days on, so a start late on day 14 could be allowed.
- **F12** s 59(2)(a) "6 months after the complying part 1 notice is given or leave to start the proceeding is granted"
  -- `s 59(2) -- the last day` -- 6 months after the leave where leave was granted, otherwise after part 1 -- the
  later (or earlier) of the two (finding 6).
- **F13** s 56(2), (3) paragraphs (b) and (c) -- `s 56 -- costs` -- where my final offer is not above the respondent's,
  an award at or above mine and at or below theirs meets both; (b) is taken -- (c) taken; the text gives no order.
- **F14** s 6(2), (3), (5) -- `s 6 -- the Act applies` -- which scheme applies is asked as one choice; the exclusions
  are flat negatives ("no") -- each scheme's own test worked out (other Acts).
- **F15** s 25(2) a request that does not offer a panel of at least 3 (or 2), or not at the respondent's expense --
  `s 25 -- must I be examined` -- "no: the request does not meet s 25(2)" (no duty) -- a bare "must" not met by the
  request answered "not covered".
- **F16** s 18(1) "unless" once met -- `s 18 -- can I go on` -- "yes" with the route named -- "not prevented by s 18"
  only (the claim may still fail elsewhere). The yes answers mean only that s 18 does not stop the claim.
- **F17** s 9A(1) "a medical incident happening on or after the commencement of this section" -- the route choice
  `medical incident under s 9A` -- asked: the day s 9A commenced is not in the deposited text (the history notes were
  removed) -- worked out from a commencement day if one were deposited.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the periods the text fixes ("within 1 month", "9 months after", "before the earlier of") give "late"
answers outside them; s 6's exclusions and s 18's "prevents ... unless" are the text's no; s 24's and s 25's "if"
conditions, unmet, give "no" constructors; s 48(1)(b) "may only ... if" gives "no" without the excuse. The "by when"
questions answer `NOTHING` where the Act fixes no day: a claim for abuse as a child (s 9(9C)), a medical incident before
the respondent answers the initial notice (s 9A(9)(b)), a claim outside division 1A (s 20B), final offers the court
dispensed with (s 40(9)). The unmet "unless" of s 18, the unmet request terms of s 25 and the overlap in s 56 are
decided case by case (F13, F15, F16).

## What the Act turns out to say

1. **The costs sanction for my disclosure reaches only requests** (F8). s 22(8) makes the claimant liable for costs on
   failing "to comply fully with a request by a respondent under this section". The respondent's mirror, s 27(4), makes
   it liable on failing "to comply fully with this section". On its words the claimant's unrequested duties (copies of
   reports held, s 22(1)(a); telling of a change, s 22(6)) carry no s 22(8) costs, though s 32 and s 35 still reach
   them. Asserted (`What follows if I do not give documents or information in time`, the copies and change cases).
2. **One day more for several respondents** (s 36(3)(b)). With one person the relevant day is "6 months after the
   person gives notice"; with more than one it is "6 months after the day after the last person gives notice". The
   multi-respondent day is one day later than the single one. Asserted (`From when may I call the compulsory
   conference`, 2 August against 3 August 2026).
3. **A probable slip in s 29(2)(b).** The contributor must provide later material "within 7 days after it comes into
   the respondent's possession"; read with s 29(1) and ss 27(2)(a), 28(2)(b), "the contributor's possession" is meant.
   Section 29 is out of scope; not asserted.
4. **Abuse claims escape s 9(3) but not s 9A(4).** s 9(9C) disapplies s 9(3), (5) and (6) for a claim for abuse as a
   child, but says nothing of s 9A, whose initial-notice period (s 9A(4), (6)) is separate. A claim for abuse arising
   in medical treatment by a doctor would on the words keep the initial-notice period. The encoding's initial-notice
   questions take no abuse input and so apply s 9A(4) to such a claim.
5. **"Before" and "within the period ending on".** s 20C(1) requires the parent's part 1 "before" the earlier day; s 9(3)
   requires part 1 "within the period ending on" the earlier day. The first excludes that day, the second includes it
   (F7), so the child's parent has one day less than an adult claimant counting the same way. Asserted (28 February
   2026 against 1 March 2026).
6. **s 59(2)(a) runs from part 1 "or" leave** (F12). It does not say which applies when both happened, or when leave is
   needed; the encoding counts from the leave where leave was granted.
7. **s 42 is a "should".** Missing the 60 days does not stop the claim: the court may order costs of the delay unless
   there is a reasonable excuse, and may fix a time limit. Only missing that court-fixed limit bars the claim, despite
   the Limitation of Actions Act 1974 (s 42(5), (6)). Asserted.
8. **Lateness with the notice does not end the claim.** s 9(5) keeps the duty alive and demands an excuse; s 18 bars
   proceeding only for a notice that does not comply, and the respondent's silence for the prescribed period makes it
   comply (s 13). Asserted.
9. **The child's own disability does not stop the parent's clock.** s 19 suspends the claimant's obligations under
   division 1 while a child, but division 1A's s 20C runs against the parent from what the parent knew. A child injured
   by medical treatment therefore has two clocks: the parent's under s 20C (running now) and the claimant's own under
   s 9(3) (from 18). The encoding answers each separately.
10. **The numbers that decide costs are not in the Act.** The lower offer limit, upper offer limit and declared costs
    limit are fixed yearly by the Minister's notice under s 75A (and s 91 carries on the last regulation amounts). None
    is deposited, so the s 56 question asks for them.

## Before this is worth relying on

- Deposit the Personal Injuries Proceedings Regulation and the Minister's current s 75A notice; replace the fallback
  periods (F3) and the asked limits.
- Find the commencement of s 9A (F17) and fix the route by the date of the medical incident.
- Deposit the Acts Interpretation Act 1954 and check F1, F2, F9, F10 and F11.
- Add a seat layer for the respondent (its duties under ss 10, 12, 20, 27) and a layer for s 9B (the refund when the
  lawyer gives no certificate).
- Check the conversion against the authorised PDF.
- A lawyer's view on findings 1, 4, 5 and 9 and forks F4, F5, F8, F12 and F13; an independent test pass and a human
  gate.
