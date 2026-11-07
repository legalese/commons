# Civil Law (Wrongs) Act 2002 (ACT), chapter 8A, with Limitation Act 1985 s 21C -- baseline encoding, the person abused as a child

## Method

**Baseline, added as a layer.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

The focus asked for: the ACT's equivalents of the child abuse reforms made across Australia -- the removal of the
limitation period for child abuse claims, and the amendments that make organisations liable for child abuse (a duty to
prevent it with a reversed onus, vicarious liability for employees and people akin to employees, a proper defendant for
unincorporated bodies, and setting aside old settlements). In the ACT these are chapter 8A of this Act (inserted by
A2018-38, A2022-21, A2025-32 and A2026-7) and the Limitation Act 1985 s 21C (inserted by A2016-53). Chapter 8A is
encoded whole as it touches the claimant, with s 21C beside it.

The Act already has an encoding, `../baseline-2026-11/` (the claimant's pre-court procedure and liability questions,
which include ss 114BBD, 114BE and 114E). It stays untouched. This is a new folder beside it, `baseline-2026-11b/`,
reusing nothing by editing; the stable `l4` cannot import across folders, so the few rules both need are written again
here (departure D2). Three files:

- `clca-dates.l4` -- date helpers and the four commencement dates (built-in date functions only, no daydate, no `YMD`);
- `clca-child-abuse.l4` -- chapter 8A and s 21C: 15 exported questions, one regulative rule (a DEONTIC function);
- `clca-cases.l4` -- worked cases.

The duty with a deadline is a regulative rule run by `EVALTRACE` inside a question that takes only plain facts: the
unincorporated body's duty to tell the court about its related trusts within 28 days of the plaintiff's application
(s 114E (3): `MUST ... WITHIN ... LEST BREACH BY the unincorporated body BECAUSE ...`). Time is counted in day serials.

## Edition

- **Act:** Civil Law (Wrongs) Act 2002 (ACT), A2002-40, Republication No 77 (R77), effective 16 May 2026, last amended by
  A2026-7, as deposited at `../../registers/source-bundle/A2002-40.txt` (converted 2026-11-06 from the register's DOCX,
  which the register marks as an unauthorised version; the authorised text is the register's PDF).
- **Limitation Act 1985 (ACT)**, A1985-66, Republication No 28 (R28), effective 26 November 2025, as deposited at
  `../../../limitation-act-1985/registers/source-bundle/A1985-66.txt` (s 21C and its endnotes only).
- **Commencement dates used** (from the endnotes): Limitation Act s 21C, 26 August 2016 (A2016-53 pt 3); part 8A.3,
  10 December 2022 (A2022-21 pt 3); part 8A.1A (ss 114BB, 114BC, 114BE), 13 November 2025 (A2025-32); division 8A.1A.2
  (ss 114BBB-114BBD, the duty to prevent child abuse), **16 May 2026** (A2026-7 s 10; finding 1).
- **Numbers set elsewhere:** the Civil Law (Wrongs) Regulation 2003 is **not deposited**. It may prescribe further
  associated individuals and exclusions (s 114BBC (1) (c), (2)), further matters for reasonable precautions
  (s 114BBD (4) (f)), and circumstances in which someone is or is not akin to an employee (s 114BC (2) (b), (3)). None is
  used; a prescribed circumstance would change the answers.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read. Two deliberately wrong assertions were run once in a scratch copy of the cases file, since deleted, and showed as
"assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clca-dates.l4` | 0 | 0 | 0 | 0 |
| `clca-child-abuse.l4` | 0 | 0 | 0 | 0 |
| `clca-cases.l4` | 0 | 0 | 105 | 105 |

Every exported question has cases, with the edges: each kind of abuse, conduct justified or excused, abuse after 18;
witnessing for s 21C; every limb of s 114BBA, s 114BBC, s 114BC and s 114B (2) alone; abuse on 15 and 16 May 2026 and on
13 November 2025; precautions proved; abuse in 1990; the 28 days from 1 March 2027 (29 March), from 15 February 2028
(14 March, a leap year) and from 20 December 2026 (17 January 2027), with notice on the last day and the day after; a
trustee's liability below, at and $1 over the trust property; settlements made the day before and the day of each
commencement (25 and 26 August 2016, 9 and 10 December 2022, 12 and 13 November 2025); every s 114L category with the
settlement set aside and not.

**No mirror cases.** One seat.

## Seat

**The person abused as a child** who brings, or wants to bring, a claim for it: the plaintiff, and under part 8A.3 the
applicant. "Is my claim a child abuse claim?", "Is there a time limit?", "Was the organisation responsible for me?",
"Was the abuser associated with it, or its employee?", "On what grounds can I hold it liable?", "Is this trust a related
trust?", "Whom do I sue when the body is unincorporated?", "By when must the body tell the court about its trusts, and has
it?", "How much can I get from the trustee?", "Is my old settlement an abuse settlement agreement, and can it be set
aside?", "Can the court set aside the deed and the consent judgment too?", "Must I pay back what I was paid?".

The organisation, the unincorporated body, the nominee, the related trust and its trustee are the text's actors; what
they did is asked as a fact. They get no seat here. The court gets no seat; its judgments are inputs.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Departed from once (D1): Limitation Act 1985 s 21C is
  brought in, because the focus names the limitation removal, s 51 note 2 points to it, and s 114J (1) (a) is defined by
  it. The Regulation is not deposited (above).
- **The actors the text names.** Followed: the person abused, the organisation, the individual associated with it, the
  employee, the unincorporated body, the nominee, the related trust and its trustee, the court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the organisation establishes
  reasonable precautions (s 114BBD (3)); whether a role supplied the occasion (s 114BE (1) (a), with the (2) factors in
  the `@desc`); whether the agreement is not just and reasonable (s 114J (1) (b) (ii), s 114K (3) (b)); whether there were
  legal barriers to full compensation (s 114K (3) (a)). "May" stays a discretion and is said as "may".
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: child abuse claim and child abuse
  (ss 114A, 114AA), related trust (s 114B), responsible (s 114BBA), associated (s 114BBC), employee (s 114BC), abuse
  settlement agreement (s 114J), liability for s 114G (5). Asked: personal injury, employed (common law), unincorporated,
  administrative unit and territory authority (Legislation Act 2001), whether a limitation period had ended.
- **One case is the text's natural unit.** Followed: one child abuse claim by one person against one organisation (or
  one unincorporated body); one settlement agreement.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (s 263 expiry, s 114G (4) corporations displacement out).

## Scope

**In.**
- Part 8A.1: ss 114A, 114AA (child abuse claim, child abuse), s 114B (related trust), s 114BA (whenever the abuse happened).
- Part 8A.1A: ss 114BB, 114BBA (organisation, responsible), ss 114BBB-114BBD (the duty to prevent child abuse, from 16 May
  2026), s 114BC (employee and akin), s 114BE (vicarious liability), with s 262 (fork F4).
- Part 8A.2: s 114C (1) (as the scope of the "whom do I sue" question), s 114D (4), s 114E (3) (the 28-day duty, a
  regulative rule) and (5), s 114F, s 114G (3) (a) with (5).
- Part 8A.3: ss 114I-114M whole: the abuse settlement agreement, the application and the grounds, the other things the
  court may and must not set aside, and the effect (void only as to the applicant; nothing to repay).
- Limitation Act 1985 s 21C (no limitation period), with its (4) definitions.

**Out, and why.**
- s 114D (1)-(3) and s 114E (1), (2) (the body's 120 days to nominate, and when the plaintiff may apply for a related trust
  to be appointed): already answered by `../baseline-2026-11/` (`s 114E -- can I ask for a related trust to be appointed
  defendant`, with its own regulative rule); not repeated.
- s 114BBD (4) and s 114BE (2) (the matters the court may or must consider): factors for a judgment that is asked as a
  fact; s 114BE (2)'s three are named in the `@desc`.
- s 114C (2), (3) (who may act for the body: any management member) and s 114E (4) (the court's choice of trust): nothing
  the claimant states or is given.
- s 114G (1), (2), (3) (b), (4) (the trustee's powers, protection from breach of trust, corporations displacement) and
  s 114H (the nominee may rely on the body's defences and insurance): about the defendant's side, with no fact test the
  claimant states beyond whether a defendant has been nominated. They could be added as one more answer to the "whom do I
  sue" question.
- s 114I (object) and s 114K (4) (factors for the court); s 114K (5) (settlement negotiations admissible) is said in the
  question's text, as it has no test.
- s 51 (5), (6) (notice of a child abuse claim within a reasonable time before suing; a parent may give it): answered by
  `../baseline-2026-11/`.
- s 263 (expiry of chapter 21) and the rest of the Act.
- The Civil Law (Wrongs) Regulation 2003 and the Legislation Act 2001: not deposited (fork F3).
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Departures

- **D1** Limitation Act 1985 s 21C is encoded here, in a folder of this Act, from the Limitation Act's deposited text. The
  Limitation Act's own encodings (`../../../limitation-act-1985/encodings/`) also answer it, as "no last day"; the two
  agree. It is here because the focus is the limitation removal and because s 114J (1) (a) is defined by it.
- **D2** `ch 8A -- on what grounds can I hold the organisation liable` covers ground that `../baseline-2026-11/` covers in
  two questions (s 114BBD, s 114BE). It is written again because the stable `l4` cannot import across folders, and it
  answers differently for abuse from 13 November 2025 to 15 May 2026 (finding 1).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 114AA (2) "sexual abuse ... includes" -- `s 114A -- is my claim a child abuse claim` -- sexual abuse other than an
  offence or misconduct of a sexual nature: NOTHING-kind; in `Limitation Act s 21C -- is there a time limit on my claim`
  the same case is read as outside s 21C -- in both, within "sexual abuse" in its ordinary meaning.
- **F2** s 114BBA (2) -- `s 114BBA -- is the organisation responsible for me` -- an organisation that delegated all care is
  still responsible -- only an organisation that keeps some care is.
- **F3** s 114E (3) "within 28 days of the application being made" -- `s 114E (3) -- the last day ...` -- the day of the
  application excluded, the last day the 28th day after it, not moved off a weekend or holiday -- the Legislation Act 2001
  (not deposited) may count otherwise or move the day.
- **F4** s 262 "applies to proceedings commenced but not finally decided before" 13 November 2025 -- `ch 8A -- on what
  grounds ...` -- s 114BE applies in every proceeding, pending or later (s 114BA) -- only in pending proceedings (as
  `../baseline-2026-11/` fork F14 and finding 10).
- **F5** s 114J (1) (b) (i)-(iii) -- `s 114J -- is my settlement an abuse settlement agreement` -- where more than one limb
  holds, the first in the text's order is named -- all are named.
- **F6** s 114J (1) (b) (ii) "is not just and reasonable in the circumstances" and s 114K (3) (b) "when the application is
  made ... not a just and reasonable agreement" -- `s 114K -- can my settlement be set aside` -- one fact serves both --
  they are judged at different times, and could differ (finding 2).
- **F7** s 114J (1) (b) (iii) "would have been an employee of an organisation if that part had been in force" --
  both part 8A.3 questions -- "employee" in the s 114BC sense (including akin), asked as one fact -- the ordinary meaning
  (finding 4).
- **F8** s 114BBB "child abuse that happens ... on or after" 16 May 2026 -- `ch 8A -- on what grounds ...` -- abuse over a
  period is dated by its first day -- the part on or after 16 May 2026 is caught.
- **F9** s 114G (5) "liability ... includes" -- `s 114G -- the most I can recover from the trustee` -- the three listed
  amounts are added; nothing else is counted -- other amounts may be liability too.
- **F10** s 114BBC (1) (b) -- `s 114BBC -- is the abuser associated ...` -- "personnel" of an organisation that is not
  religious, or of a religious organisation without a role: NOTHING-kind -- the text's no.
- **F11** s 114D (4) (a), s 114E (5) (a) "may be brought against the nominee / appointee" -- `s 114F -- whom do I sue ...`
  -- after a nomination or appointment the answer names the nominee or trust -- the claim may still also run in the body's
  name.
- **F12** s 114BB "organisation includes" -- `s 114BBA -- is the organisation responsible for me` -- an individual:
  NOTHING-kind -- the text's no (an individual is plainly not an organisation).

Sites decided without a fork line: the "means" definitions (ss 114A, 114AA (1), 114B (1), 114J (1)), the "if" conditions
(ss 114B (2), 114BBA, 114BC (2), 114BE (1), 114K (1), (3), 114L (1)) and the period in s 114E (3) answer the text's no
when they fail; s 114AA (2) "does not include" and s 114L (2) "must not" are flat negatives, answered as the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries NOTHING-kind tags (forks F1, F10, F12; s 114BBC and s 114BC outside their lists; s 114BE (3) where
neither route holds; part 8A.2 outside its scope; s 114L for things that do not give effect to the settlement; s 114M
before a settlement is set aside). The questions answer with a choice from a list rather than a MAYBE BOOLEAN: the answer
marked "NOTHING-kind" is the NOTHING answer, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **The duty to prevent child abuse (division 8A.1A.2) began on 16 May 2026, not 13 November 2025.** The endnotes show
   ss 114BBB-114BBD and the division heading inserted by A2026-7 s 10, whose remainder commenced 16 May 2026; A2025-32
   (13 November 2025) inserted only part 8A.1A's heading and ss 114BB, 114BC, 114BD (now 114BBA) and 114BE. s 114BBB
   applies the division to abuse "on or after the day this division commences", so abuse from 13 November 2025 to 15 May
   2026 gets vicarious liability but not the reversed onus. The encoding beside this one (`../baseline-2026-11/`, its
   finding 13 and `s 114BBD -- is the organisation taken to have breached its duty`) uses 13 November 2025 and so says
   "breach taken" for abuse in that window; it was left untouched, as layers are never edited, and is flagged here for its
   reviewer. Asserted (13 November 2025 and 15 May 2026: no duty route; 16 May 2026: duty route).
2. **"Not just and reasonable" is a gate and a ground at once.** An agreement made before 10 December 2022 is an abuse
   settlement agreement only if it "is not just and reasonable in the circumstances" (s 114J (1) (b) (ii)), and the court
   may set it aside if, when the application is made, it is "not a just and reasonable agreement" (s 114K (3) (b)). On one
   reading every (b) (ii) agreement already meets ground (3) (b); s 114J does not say at what time its test is applied.
   One fact serves both here (fork F6). Asserted (a 2018 settlement: set aside on ground (b)).
3. **s 21C and chapter 8A use "subjected" differently.** The Limitation Act s 21C (4) says "subjected, in relation to
   child abuse, includes witness"; s 114A of this Act has no such extension. A person who only witnessed abuse as a child
   has no limitation period (s 21C) but no "child abuse claim", so chapter 8A (the organisation's duty, vicarious
   liability, defendants for unincorporated bodies, setting aside settlements) is not open to them; and s 114J (1) (a)
   needs both (it settles a child abuse claim and bars an action to which s 21C applies). The two questions ask the two
   facts separately.
4. **s 114J (1) (b) (iii) leans on a definition that has moved.** It asks whether the abuser "would have been an employee
   of an organisation if [part 8A.1A] had been in force". A2025-32 defined "employee" for the whole part in s 114BB;
   A2026-7 s 8 omitted that definition and s 114BC now defines "employee" for division 8A.1A.3 only. The definition the
   paragraph needs (including people akin to employees) is presumably still s 114BC's; read so (fork F7).
5. **An agreement "happened".** s 114J (1) (b) (i)-(iii) speak of an agreement that "happened before" each commencement.
   Read as "was made before". Asserted at each commencement day and the day before: a settlement made on the commencement
   day itself is outside the limb.
6. **The body's 28-day duty in s 114E (3) has no stated consequence.** If the unincorporated body does not tell the court
   about its related trusts within 28 days, the Act says nothing more; the court may appoint "other related trusts" anyway
   (s 114E (4)). The regulative rule ends in BREACH by the body and the answer says what (4) allows. Asserted.
7. **The trustee's cap includes costs.** s 114G (5) counts costs as part of the trustee's liability, and s 114G (3) (a)
   caps the whole at the total value of the trust property, so costs can eat into what the claimant recovers from the
   trust. Asserted ($200,000 settlement and $20,000 costs against $150,000: $150,000).
8. **Nothing paid under a set-aside settlement is recoverable**, even though the agreement becomes void (as to the
   applicant); the court may only take it into account in assessing damages (s 114M (3)). Asserted.
9. **A National Redress Scheme deed of release can never be set aside** under part 8A.3 (s 114L (2) (a)), nor an
   insurance contract or a cross-claim or indemnity between defendants, whether or not the settlement itself is set
   aside. Asserted.

## Before this is worth relying on

- The Civil Law (Wrongs) Regulation 2003: any prescribed associated individuals, exclusions, precaution factors and
  "akin to an employee" circumstances (ss 114BBC, 114BBD (4) (f), 114BC (2) (b), (3)).
- The Legislation Act 2001 (ACT) for counting the 28 days (fork F3), and for administrative unit and territory authority.
- A lawyer's view on forks F2, F4, F6, F7, F8, F11 and on findings 1-4; a correction of the commencement date in
  `../baseline-2026-11/` if finding 1 is right; an independent test pass and a human gate.
- Read with: `../baseline-2026-11/` (notice of a child abuse claim, s 51 (5); the 120 days and the application for a
  related trust, ss 114D, 114E (1), (2)); the Limitation Act 1985 (ACT) encodings (the limitation periods themselves and
  s 21C as "no last day").
