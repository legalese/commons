# Charter of Human Rights and Responsibilities Act 2006 (Victoria) -- baseline encoding, the injured person

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`
(none is used). No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The dates are in `chr-dates.l4` (built-in
date functions only, no daydate), the rules in `chr-core.l4`, the injured person's exported questions in `chr-seat.l4`
(each calls a rule in `chr-core.l4`), and the worked cases in `chr-cases.l4`.

Among the claims laws the Charter is the least direct. It gives no claim and no damages of its own (s 39(1), (3)). What
it does for a person injured in custody or care, or by a public body, is threefold: it makes it unlawful for a public
authority to act incompatibly with a human right or to decide without proper consideration of one (s 38); it lets that
unlawfulness ride as an extra ground on a claim the person already has apart from the Charter (s 39(1)), while keeping
any damages that other claim gives (s 39(4)); and it requires the court to read every Victorian statute in the case
(a limitation period, an immunity, a power to detain or restrain) compatibly with human rights so far as possible
(s 32). The encoding answers those questions, and asks, right by right, whether what happened limited the rights a
person in custody or care most often relies on.

## Edition

- **Act:** Charter of Human Rights and Responsibilities Act 2006, Act No. 43/2006, Version No. 015, incorporating
  amendments as at 1 June 2022, deposited at
  `../../registers/source-bundle/charter-of-human-rights-and-responsibilities-act-2006.txt` (text sha256
  e623948a...0ad82e per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on
  7 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Version 015 was the current version
  ("In force") on 2026-11-07. Not checked against the authorised PDF, which was not saved.
- **Numbers and dates set elsewhere:** none that the encoding needs. The Charter's days are its own commencements
  (s 2: 1 January 2007; Divisions 3 and 4 of Part 3, ss 32-39, on 1 January 2008, which the endnotes confirm) and the
  life of an override declaration (s 31(7)).
- **Not deposited, and asked as facts:** the Charter of Human Rights and Responsibilities Regulations (which entities are
  declared to be, or not to be, public authorities, s 4(1)(h), (k), s 46(2); the prescribed form of a s 35 notice); the
  Public Administration Act 2004 and the Local Government Act 2020 (what a "public official" and a "Council" are); the
  Interpretation of Legislation Act 1984 ("Act", "subordinate instrument"); the other law that gives the person a claim
  apart from the Charter. Related Victorian baseline encodings beside this subject (Wrongs Act 1958, Limitation of
  Actions Act 1958, Equal Opportunity Act 2010, Mental Health and Wellbeing Act 2022, Supreme Court Act 1986) cannot be
  imported (IMPORT does not reach another subject's folder); nothing from them is restated here.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `chr-dates.l4` | 0 | 0 | 0 | 0 |
| `chr-core.l4` | 0 | 0 | 0 | 0 |
| `chr-seat.l4` | 0 | 0 | 0 | 0 |
| `chr-cases.l4` | 0 | 0 | 194 | 194 |

Every exported question has cases, with the edges: every kind of body in s 4(1), each exclusion beating an inclusion,
the two examples in s 4 (the private prison operator and the non-government school) and the note to s 4(1)(j) (a
warrant); each limb of ss 9, 10, 13, 21, 22, 23 and 24 alone, together, and not met; age 17 and 18 for s 23; an act on
31 December 2007 and on 1 January 2008 (s 49(3)); a proceeding commenced on 31 December 2006 and on 1 January 2007
(s 49(2)); a reading on 31 December 2007 and on 1 January 2008 (s 2(2)); an override declaration the day before its
operation, in force the day before its 5th anniversary and expired on it, with an earlier expiry date (the day before
and the day of it), with a "earlier" date later than the anniversary, and from 29 February 2024; each s 35 combination
of court, referral and parties, and each combination of notices given.

## Seat

**The injured person** (`chr-seat.l4`): a person injured in State custody or care, or by a public body -- a prisoner
(including in a privately run prison), a person held by police, a child in youth justice custody or out-of-home care, a
patient detained or restrained under mental health law, a person hurt by a council or a State agency -- who has, or may
have, a cause of action of their own apart from the Charter (in negligence, for false imprisonment or battery, under a
compensation statute, or for judicial review). "Is the body that hurt me a public authority?", "Which of my rights did
what happened limit?", "Was the act unlawful under the Charter?", "Can I add a Charter ground to my claim?", "Can I get
damages for the breach?", "Must the court read the statute in my case compatibly with my rights?", "Must I notify the
Attorney-General and the Commission, and have I?".

The Charter puts its duties on public authorities (s 38), Parliament and the courts; officials get no seat. A public
authority's own seat (what s 38 requires of it) is not written: the same answers tell it whether an act would be
unlawful, and a second seat would add nothing but mirror cases. The one duty the Charter puts on the person is s 35
(notice as a party), which is encoded from the person's seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: no instrument sets a number the encoding uses;
  the regulations (not deposited) only declare entities and prescribe forms, and are asked.
- **The actors the text names.** Followed: the person, the public authority (by its s 4 kind), the court or tribunal,
  the Attorney-General, the Commission, the State, Parliament.
- **Judgments answered conditionally.** Every judgment the Charter leaves to a court is asked as "whether a court would
  find ...": functions of a public nature (s 4(2), (3)), on behalf of the State (s 4(4), (5)), administrative capacity
  (s 4(1)(g), (j)), cruel, inhuman or degrading (s 10(b)), unlawful or arbitrary (ss 13, 21(2)), promptly and without
  unreasonable delay (s 21(4), (5)), reasonably necessary (s 22(2)), humanity and dignity (s 22(1)), fair hearing
  (s 24(1)), demonstrably justified (s 7(2)), private nature (s 38(3)), could not reasonably have acted differently
  (s 38(2)), proper consideration (s 38(1)). None is decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "child" (s 3, from age), "person" and s 6(1),
  "statutory provision" (s 3, from the kind of law), "public authority" (s 4, from the kind of body and the judgments),
  "act" includes a failure to act and a proposal to act (s 3, in the wording of the questions). Asked: "public official",
  "Council", "Act", "subordinate instrument", the regulations, and whether the other law gives a claim.
- **One case.** One act, failure or decision of one body, as it affected one person; for ss 32 and 35, one proceeding.
- **The Act's terms with plain glosses.** Followed, in every `@desc`.
- **Operative sections in; machinery out.** Out: s 1 (purpose), ss 28-30 (statements of compatibility, scrutiny of
  Bills), s 31(1)-(5), (9) (how Parliament makes an override, beyond its effect), ss 33-34, 36(1)-(4), (6), (7), 37
  (referrals, intervention, the Supreme Court's declaration procedure and the Minister's response), Part 4 (the
  Commission), ss 44-46 (reviews, regulations), s 47 (repealed), s 49(4).

## Scope

**In:** s 2 (the commencement days ss 49(2), (3) count from); s 3 (child, person, statutory provision, act); s 4 (public
authority, every limb and exclusion); s 6(1) (only persons have human rights); Part 2: ss 9, 10, 13, 21, 22, 23 and 24
limb by limb, and every right in ss 8-27 named in `Charter right` and reachable through the s 38 question (whether the act
limited it is the court's finding); s 7(2) (a limit must be under law and demonstrably justified); s 31(2), (6)-(8)
(the effect and life of an override declaration, for s 32); s 32 (interpretation); s 35 (notice: the one regulative
rule); s 36(5) (a declaration of inconsistent interpretation gives no right or cause of action, in the s 32 answer);
s 38 (unlawfulness, with (2)-(5)); s 39 (a Charter ground rides on another claim; no damages; other damages kept);
s 49(1)-(3).

**Regulative rule:** one. s 35(1): I MUST give notice in the prescribed form to the Attorney-General RAND to the
Commission (or to the one s 35(2) leaves). No WITHIN (the Act sets no time) and no LEST (the Act says nothing of what
follows a failure). It is run by EVALTRACE inside `Have I given the notices`, which takes only yes/no facts; a CONSIDER
on an EVALTRACE matches FULFILLED only, so a notice still owed shows as "still to give".

**Out, and why:**
- The other Part 2 rights limb by limb (ss 8, 11, 12, 14-20, 25-27): further from injury claims; each is named and
  reachable through the s 38 question with its limitation asked as a finding. Encoding them limb by limb is the next
  step if a scenario needs it.
- The machinery listed under Seat above: duties of Parliament, the Supreme Court, the Attorney-General, the Minister and
  the Commission, which change nothing the person can claim (s 36(5), s 29, s 31(9)).
- s 5 (other rights not abrogated) and s 48 (abortion savings): no rule a person applies; s 5 is noted in the s 39
  answers' sense (other rights and remedies stay).
- The other law that gives the claim (negligence, false imprisonment, judicial review, the Wrongs Act 1958 and the
  Limitation of Actions Act 1958, which have their own baseline encodings beside this subject): asked as a fact.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4(1)(a), (e) "public official within the meaning of the Public Administration Act 2004", "Council ... within
  the meaning of the Local Government Act 2020" -- `Kind of body` -- the person picks the kind -- the borrowed definitions
  (not deposited) may include or exclude bodies the person would not expect (for example certain public entity staff).
- **F2** s 4(1) "a public authority is-- (a) ... (h)" -- `s 4 -- public authority` -- a closed, "means"-like list: a body
  in none of (a)-(h) is not one ("no", JUST FALSE kind); and a court or tribunal acting in an administrative capacity is
  taken to be one (under (b) where established by statute) -- the list is read as open; or the (j) exception only lifts
  the exclusion and a court must still be shown to fall within (a)-(h).
- **F3** s 9 -- `s 9 -- limbs limited` -- the first limb (the right to life) is limited only where a court would so find
  (asked); the second limb needs a death -- the first limb is read narrowly as the second (only arbitrary deprivation of
  life), which would make s 9 unavailable to a person injured but alive.
- **F4** s 21(4), (7) -- `s 21 -- arrest and detention limbs limited` -- "at the time" and "promptly" are asked as whether
  it was done; the court's duties in (7) count only where the person applied -- "at the time" is read strictly (the same
  moment); (7) read as a free-standing right whether or not an application was made.
- **F5** s 38(1), s 7(2) "incompatible with a human right" -- `ss 7(2), 38(1) -- incompatible with a human right` -- an act
  is incompatible when it limits a right and the limit is not under law and demonstrably justified -- incompatibility is
  a separate question from s 7(2) justification (a reading the cases have discussed; not deposited).
- **F6** s 3 "statutory provision means an Act ... or a subordinate instrument" -- `s 3 -- a statutory provision` -- a
  Victorian Act or an instrument made under one; a Commonwealth law, the common law and the law of another place are not
  ("no", JUST FALSE kind) -- "Act" read more widely (the Interpretation of Legislation Act 1984 is not deposited).
- **F7** s 39(1) "otherwise than because of this Charter, a person may seek any relief or remedy ... on the ground that
  the act or decision was unlawful" -- `s 39(1) -- a Charter ground` -- whether the person's other claim (judicial review,
  false imprisonment, battery, negligence, a statutory claim) is one "on the ground that the act or decision was
  unlawful" is asked -- read narrowly, a claim in negligence (a duty of care breached) may not be a claim on a ground of
  unlawfulness, and then s 39(1) adds nothing to it. The answer turns on case law not deposited.
- **F8** s 35 -- `s 35(1) -- my duty to notify` -- no WITHIN and no LEST: the duty waits until done -- court rules or
  practice notes may fix a time (not deposited); the Supreme Court's own duty under s 36(3), (4) means a declaration
  cannot be made without notice, which is a consequence the person meets indirectly.
- **F9** s 31(7) "expires on the 5th anniversary" -- `the 5th anniversary of`, `s 31(6), (7) -- an override declaration is
  in force` -- the declaration is in force up to the day before the anniversary and expired on it; the anniversary of
  29 February is 28 February (never a leap year five years on) -- it expires at the end of the anniversary day; or the
  anniversary of 29 February is 1 March.
- **F10** s 49(2) with s 2(2) -- `s 32 -- reading compatibly` -- a proceeding commenced on or after 1 January 2007 is
  affected by the Charter, but s 32 only operates on a reading on or after 1 January 2008 -- s 32 governs only
  proceedings commenced on or after 1 January 2008.
- **F11** s 22(1) "deprived of liberty" -- `s 22 -- limbs limited` -- reaches care and treatment settings as well as
  custody (asked) -- custody only. s 22(2), (3) reach only an accused person who is detained and a person detained
  without charge.
- **F12** s 38(2)-(4), s 49(3), s 4 -- `s 38 -- unlawful` -- the first reason found, in the order s 4, s 49(3), s 38(3),
  s 38(2), s 38(4), is the one given -- the reasons are cumulative (the answer "no" is the same; only the reason shown
  differs).
- **F13** s 24(1) -- `s 24 -- limbs limited` -- the limb is limited if the court or tribunal was not competent,
  independent and impartial, or the hearing was not fair, or (unless another law permitted it) not public -- s 24(2)
  read as reaching only "members of media organisations or other persons", not the whole hearing.
- **F14** s 21(5)(c) "must be released if paragraph (a) or (b) is not complied with" -- `s 21 -- criminal charge limbs
  limited` -- (b) "not complied with" when the person was not brought to trial without unreasonable delay -- (b) is a
  right, not a duty, so "complied with" may reach only (a).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 3 "child" and "person" and s 4 (F2) are "means" definitions; s 6(1) and s 7(2) say "only"; s 38(2),
(3), s 39(3), s 49(2), (3) and s 4(1)(i)-(k) are flat negatives; s 39(1), s 35(1) and s 31(6) are "if" conditions: each
gives a "no" constructor with its section. s 38(1) says only what is unlawful: where its limbs are not met the answer is
worded "s 38(1) not met" on these facts, never "lawful". The Part 2 questions list the limbs the facts meet; an empty
list means "no limb of this section on these facts", not that the right is unlimited in every way (the general limbs
s 9 and s 21(1) are asked as findings). s 38(4) ("does not require") is an "except once met" site (Meng's rule): taken
as "no" with its reason (F12).

## What the Act turns out to say

1. **No claim and no damages of its own.** s 39(1) lets a Charter ground ride only on relief the person can seek apart
   from the Charter; s 39(3) bars damages "because of a breach of this Charter"; s 39(4) keeps damages the person has
   otherwise. So for an injury claim the Charter never adds money: it can add a ground (and so perhaps a declaration or
   other relief the other claim gives) and change how statutes in the case are read. Asserted (`damages kept`,
   `damages none`, `ground no claim`).
2. **Whether a negligence claim is a "ground that the act was unlawful" is not in the text.** s 39(1) speaks of relief
   sought "on the ground that the act or decision was unlawful". A claim for false imprisonment or battery plainly
   alleges unlawful conduct; a claim in negligence alleges breach of a duty of care, which may or may not count. The
   encoding asks it (F7); it is the single most important open question for this seat.
3. **A declaration of inconsistent interpretation gives the person nothing to claim.** s 36(5)(b): it does not "create in
   any person any legal right or give rise to any civil cause of action", and s 32(3) keeps an incompatible Act valid.
   Asserted, in the wording of the s 32 answer.
4. **s 23(1) has no "reasonably necessary" exception; s 22(2) has one.** A detained child must be segregated from all
   detained adults, with no exception in the text; an unconvicted adult detainee must be segregated from convicted
   persons "except where reasonably necessary". Asserted (a 17-year-old held with adults: `L23-1`, with no input for
   necessity).
5. **s 23(1) does not reach a convicted child.** It covers "an accused child who is detained or a child detained without
   charge"; a convicted child held with adults is protected only by s 23(3) (treatment appropriate to age) and s 22(1).
   Asserted.
6. **s 21(5)(c) speaks of "complied with" for a right.** Paragraph (a) is a duty ("must be promptly brought"), paragraph
   (b) a right ("has the right to be brought to trial without unreasonable delay"); (c) requires release if "(a) or (b)
   is not complied with". The encoding treats (b) as not complied with when the trial was unreasonably delayed (F14).
7. **s 31(7) expires the provision, not only the declaration.** "A provision of an Act containing an override
   declaration expires on the 5th anniversary": the provision that contains the declaration expires; where the
   declaration overrides the Charter for a provision of another Act (s 31(1)), the overridden provision itself does not
   expire, but the declaration does. The encoding treats the declaration as no longer in force from the anniversary
   (F9).
8. **The commencement split matters for old acts.** Division 4 (ss 38, 39) does not apply to an act or decision before
   1 January 2008 (s 49(3)), and the endnotes confirm ss 32-39 commenced that day. A Charter ground is unavailable for an
   injury caused in 2007 even though Part 2 (the rights) was in force. Asserted (31 December 2007 and 1 January 2008).
9. **s 4(1)(j) excludes a court "except when it is acting in an administrative capacity", but no paragraph of s 4(1)
   names courts.** A court acting administratively becomes a public authority only through another paragraph, usually
   (b) (a body established by statute with public functions). The encoding answers yes (F2); a lawyer should confirm.
10. **The prescribed form and the time for a s 35 notice are not in the Act.** The form is in regulations (not deposited)
    and no time is fixed (F8).

## Before this is worth relying on

- Check the conversion against the authorised PDF (Version No. 015).
- Deposit the Charter regulations (declared entities, the prescribed form), the Public Administration Act 2004 and the
  Interpretation of Legislation Act 1984, and work F1, F6 and the regulations inputs out from them.
- A lawyer's view on findings 2, 6, 7 and 9 and forks F2, F3, F5, F7, F10 and F14 (several turn on case law that is not
  deposited), an independent test pass and a human gate.
- Encode the remaining Part 2 rights limb by limb if a scenario life needs them.
