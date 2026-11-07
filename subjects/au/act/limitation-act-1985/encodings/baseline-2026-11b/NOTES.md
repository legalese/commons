# Limitation Act 1985 (ACT), choice of law -- baseline encoding, the person bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The instrument was asked for as the ACT's "Choice of Law (Limitation Periods) Act 1993". The ACT has no Act of that name:
its counterpart of the States' Choice of Law (Limitation Periods) Acts is Division 4.4 (ss 55-57) of the Limitation Act
1985, inserted by the Limitation (Amendment) Act 1993 (A1993-82 s 6, commenced 30 November 1993), which is presumably
where the "1993" comes from. This encoding therefore covers the choice-of-law provisions of the Limitation Act 1985, and
nothing else in it.

The folder is `baseline-2026-11b`, not `baseline-2026-11`, because a separate baseline of this Act's own time limits
(Parts 2 and 3) was being written at the same time and takes the plain name. Nothing existing was touched; nothing is
imported from any other encoding. The dates are in one small module (`clact-dates.l4`, built-in date functions only, no
daydate), the rules and exported questions in `clact-claims.l4`, and the worked cases in `clact-cases.l4`. The shape
follows the Northern Territory Act's baseline (`subjects/au/nt/choice-of-law-limitation-periods-act-1994/encodings/
baseline-2026-11/`) so the two can be read side by side; every rule was written again from the ACT text.

The focus asked for: the provisions a claimant meets. Division 4.4 is three sections and is encoded whole: what a
"limitation law" is and that "court" includes an arbitrator (s 55), that the limitation law of a State, another Territory
or New Zealand whose law governs the claim is applied as part of that law (s 56), and how a discretion under that
limitation law is exercised (s 57). Two other sections of the Act are choice-of-law rules a claimant meets and are
encoded with it: s 54 (a revenue action against another State or Territory is barred once that place's own period has
ended) and s 21BC (3) (b) (the "first uploaded" date of an electronic publication does not decide the choice of law for
defamation). The one duty with a deadline -- to begin within the time the other place's limitation law allows -- is a
regulative rule run by EVALTRACE inside two exported questions (s 56 and s 54).

## Edition

- **Act:** Limitation Act 1985 (ACT), A1985-66, Republication No 28 (R28), effective 26 November 2025, last amended by
  A2025-29, as deposited at `../../registers/source-bundle/A1985-66.txt` (converted from the register's DOCX, which the
  register marks as an unauthorised version; the authorised text is the register's PDF).
- **History of the sections encoded:** Division 4.4 and ss 55-57 inserted by A1993-82 s 6 (commenced 30 November 1993),
  not amended since; s 54 inserted by A1993-82 s 6, amended by A2006-42 amdt 3.138; s 21BC inserted by A2021-15 amdt 1.2.
- **Numbers set elsewhere:** none. The sections encoded fix no period, amount or fee.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (beginning the day after the last day asserted to be in time) was run once in a scratch copy,
since deleted, and showed as "assertion failed" (62 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clact-dates.l4` | 0 | 0 | 0 | 0 |
| `clact-claims.l4` | 0 | 0 | 0 | 0 |
| `clact-cases.l4` | 0 | 0 | 62 | 62 |

Every exported question has cases, with the edges: each element of the s 55 definition missing; each forum and each
governing law for s 56 and s 57, and the order in which they are checked; beginning on the last day the governing
limitation law allows, the day before, the day after, on the day time began and before it; not yet begun with today the
last day and the day after; a period running from 29 February 2024; the regulative rule alone on day 0, the day before
the deadline, the deadline and the day after; each condition of s 57 failing in turn; for s 54, each element of "revenue
amount" failing, each kind of defendant, beginning on the last day of the other place's period, the day before and the
day after, and not yet begun; s 21BC with and without an electronic publication.

**No mirror cases.** One seat.

## Seat

**The person bringing a claim** (`clact-claims.l4`): the claimant whose claim is before a court of the ACT or an arbitrator
and is governed by the law of an Australian State, another Territory or New Zealand, or who sues another State or
Territory in the ACT to recover a tax, licence fee or duty. "Is this time rule a limitation law?", "Whose time limit
applies to my claim?", "Am I in time?", "If I ask the court to extend time under that law, how must it decide?", "Is the
money I want back a revenue amount?", "Can I still sue that State for it?", "Does the first-upload day decide the
choice of law for my defamation claim?".

The Act speaks to the court ("applied accordingly by the court", "is to be exercised"); the encoding turns that into what
it means for the claimant. The court and the arbitrator get no seat: how the courts of the other place exercise the
discretion, and whether following them is practicable, are asked as facts. No second seat was written: the party
answering the claim asks the same questions with the same answers (the time limit that binds the claimant is the defence
the respondent raises). The State sued under s 54 is a government and gets no seat.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number. The limitation law
  of the other place is not brought in: its last day is the claimant's fact.
- **The actors the text names.** Followed: the court (including an arbitrator), the courts of the other place, the
  claimant, the State or Territory sued and its officers, Ministers and authorities (s 54 (3)).
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: which place's substantive law
  governs the claim (common-law choice of law, not stated in the Act); how the courts of that place exercise the
  discretion in comparable cases; whether following them is practicable (s 57); whether the amount would have been owing
  had the provision been valid (s 54 (2)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "limitation law" and "court"
  including an arbitrator (s 55), "revenue amount" (s 54 (2)), the "relevant limitation period" as the other place's last
  day (s 54 (2)). Asked: "State", "Territory" (Legislation Act 2001, not deposited), "substantive law", the other place's
  limitation period and its counting.
- **One case is the text's natural unit.** Followed: one claim in one proceeding or arbitration.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed, within the focus.

## Scope

**In.** Division 4.4 whole (ss 55, 56, 57); s 54; s 21BC (3) (b), read with s 21BC (1) and (2).

**Out, and why.**
- Parts 1 to 3 (the Act's own limitation periods, the bars for personal injury, motor accident, workers compensation,
  defamation and child abuse claims, postponement and extension of the bar), Divisions 4.1 to 4.3 apart from s 54, and
  the rest of s 21BC: not the choice-of-law focus; they belong to the baseline of the Act's own time limits beside this
  one. Where ACT law governs, s 56 points the claimant there.
- s 21A (3) ("Subsection (1) is part of the substantive law of the Territory"): it characterises the ACT's own 6-month
  bar on revenue claims, so that it travels with ACT law into other forums; it is the mirror of s 54 but is part of
  s 21A, which belongs with the Act's own periods. Not encoded here.
- Division 4.5 (approved forms, regulation-making): machinery.
- The limitation laws of the States, the other Territories and New Zealand: not this Act. The governing law's last day is
  asked; the encoding counts nothing for it.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 55 definitions ("In this division") -- every question using "court" and "limitation law" -- applied as written
  in ss 56, 57 -- none (the Legislation Act's contrary-intention rule, s 155, was not found to bite).
- **F2** s 55 "court includes arbitrator", read into "a court of the Territory" in ss 56, 57 -- `a court of the Territory`
  -- an arbitrator counts when the arbitration is held in the ACT; an arbitrator elsewhere does not -- an arbitrator
  counts wherever seated if the arbitration is conducted under ACT law, or any arbitrator counts.
- **F3** s 56 and s 54 (2), the time the other place's limitation law allows -- `s 56 -- am I in time`, `s 54 -- can I
  still sue for the revenue amount` and the regulative rule -- the claimant states the day time began and the last day,
  read from that law; beginning on the last day is in time, the day after is not ("has ended" read as "the last day has
  passed") -- the encoding counting the period itself.
- **F4** s 54 (1) "has ended", for an action not yet begun -- `s 54 -- can I still sue for the revenue amount` -- measured
  at today: "still in time" until the last day passes -- measured at the day the action will be begun (the same answer
  once begun).
- **F5** ss 56, 57 and s 54 "another Territory" -- `a State, another Territory or New Zealand`, `Who I am suing` -- any
  Territory other than the ACT, internal (the Northern Territory, the Jervis Bay Territory) or external (Norfolk Island and
  the others), asked as one choice -- the internal Territories only.
- **F6** s 56 "If ... is to govern a claim before a court of the Territory" -- `s 56 -- whose time limit applies to my
  claim` -- when the "if" fails, the text's no on s 56; for ACT law the answer points to the Act's own periods (Parts 2
  and 3 apply to "an action" on their own terms); for a foreign country's law, "this Act does not say" (NOTHING-kind) --
  NOTHING in every case, since s 56 is silent on what applies instead.
- **F7** s 56 and s 54, an action begun before time began to run -- `the timing` -- in time (counted as day 0) --
  premature, which is that law's question.
- **F8** s 57 "as far as practicable" -- `s 57 -- how must the court use a discretion under that limitation law` -- where
  following the other place's courts is not practicable, NOTHING ("s 57 says no more"; a limit in the section's own
  wording) -- JUST FALSE (the s 57 duty does not arise).
- **F9** s 57 "If a court of the Territory exercises a discretion" -- the same function -- no discretion asked for, a court
  outside the ACT, or a limitation law of the ACT or a foreign country: the text's no (ruling (b) of 2026-11-05, "if" read
  as "where") -- NOTHING.
- **F10** s 54 (1), a defendant that is not another State or Territory (or its officer, Minister or authority) -- `s 54 --
  can I still sue for the revenue amount` -- NOTHING-kind (a scope limit with no "only": s 54 says nothing about other
  defendants) -- JUST FALSE ("s 54 does not bar the action").
- **F11** s 54 (1) "imposed, or purportedly imposed, under a law of the State or Territory" against s 54 (2) "under a law"
  -- `What I paid the money as` -- one choice, the tax imposed under a law of the State or Territory sued -- treating a
  tax imposed by another place's law, but sued for from this State, as within s 54 (2).

Sites decided without a fork line: s 55's and s 54 (2)'s "means" definitions answer FALSE when an element fails; s 21BC
(3) (b) "is not relevant for" is a flat negative, answered as the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries three `NOTHING-kind` tags (s 56 for a foreign country's law, F6; s 57, F8; s 54 for other
defendants, F10) and one more for s 21BC where the matter is not electronic. Most questions answer with a choice from a
list rather than a MAYBE BOOLEAN: the answer marked "NOTHING-kind" is the NOTHING answer, and the answers marked "the
text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The time the other place's limitation law allows is the regulative rule (`MUST begin WITHIN` the days to its last day,
`LEST BREACH`), run by EVALTRACE inside the questions; outside it the answer is "out of time ... only a discretion that law
gives the court can help (see s 57)", or, under s 54, "not maintainable".

## What the Act turns out to say

1. **There is no ACT "Choice of Law (Limitation Periods) Act 1993".** The ACT put its choice-of-law rule for limitation
   into the Limitation Act 1985 itself (Division 4.4), by the Limitation (Amendment) Act 1993. The 1993 Act of that name is
   New South Wales's. Not law; noted only.
2. **Division 4.4 sets no time limit of its own.** It only decides whose limitation law an ACT court applies, and how it
   uses a discretion under it. A claimant's actual deadline is in the other place's Act. Asserted (the in-time cases take
   the last day as a fact).
3. **No application or transitional rule is in the republication.** Unlike the NT Act (its s 3) and the WA Act, Division
   4.4 says nothing about proceedings begun, or causes of action that arose, before 30 November 1993. Any such rule would
   be in A1993-82 (itself amended by A1994-91), which is not deposited; the encoding asks no date for it.
4. **s 56 and s 21C pull against each other.** s 21C (2) says an action for personal injury from child abuse "is not
   subject to any limitation period under this Act, despite anything elsewhere in this Act or another territory law". It
   does not displace a State's limitation law, which s 56 makes part of the State's substantive law: if, say, another
   State's law governed such a claim, s 56 would apply that State's limitation law (whatever it says about child abuse),
   not s 21C. Not encoded beyond s 56 itself; for the reviewer.
5. **"Court includes arbitrator", but ss 56 and 57 say "a court of the Territory".** Which arbitrators are "of the
   Territory" is not said (fork F2).
6. **s 57 is not tied to s 56.** On its words it applies whenever an ACT court exercises a discretion under the limitation
   law of a State, another Territory or New Zealand, whether or not that place's law governs the claim. Encoded as
   written: the s 57 question asks for the place whose limitation law gives the discretion.
7. **s 54 uses "under a law of the State or Territory" in (1) and "under a law" in (2).** The two read together confine
   s 54 to a tax of the State or Territory sued (fork F11). s 54 also leaves open whether the general 6-year bar of s 11
   applies alongside it: s 11 (2) excludes a cause of action "in relation to which another limitation period is provided
   by this Act", and s 54 provides one only by reference to another place's law. The encoding answers only what s 54
   says ("as far as s 54 goes").
8. **s 54 reaches only States and "another Territory"**, with their officers, Ministers and authorities (s 54 (3)); a claim
   against the Commonwealth for an invalid Commonwealth tax is outside it (fork F10), and an ACT revenue claim is under
   s 21A, made substantive by s 21A (3).
9. **s 21BC (3) (b) keeps the electronic "first uploaded" date out of the choice of law for defamation**, so it cannot be
   used to say that the publication happened where (or when) the matter was first uploaded for any purpose other than
   when time begins. Asserted.

## Before this is worth relying on

- The Limitation (Amendment) Act 1993 (A1993-82) and A1994-91, for any transitional rule (finding 3), not deposited.
- The Legislation Act 2001 (ACT) for "State" and "Territory" (fork F5), not deposited.
- A lawyer's view on forks F2, F6, F8, F10 and F11, and on findings 4, 6 and 7; an independent test pass and a human
  gate.
