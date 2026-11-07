# Choice of Law (Limitation Periods) Act 1994 (NT) -- baseline encoding, the person bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`clpnt-dates.l4`,
built-in date functions only, no daydate), the rules and exported questions in `clpnt-claims.l4`, and the worked cases in
`clpnt-cases.l4`. The shape follows the Western Australian Act's baseline
(`subjects/au/wa/choice-of-law-limitation-periods-act-1994/encodings/baseline-2026-11/`) so the two can be read side by
side; nothing is imported from it (cross-folder IMPORT is not possible) and every rule was written again from the NT text.

The focus asked for: the provisions a claimant meets. The Act is six sections long, so the whole operative Act is encoded:
whether it applies to the proceedings (s 3), what a "limitation law" is and that "court" includes an arbitrator (s 4), that
the limitation law of a State, another Territory or New Zealand whose law governs the claim is applied as part of that law
(s 5), and how a discretion under that limitation law (typically to extend time) is exercised (s 6). The one duty with a
deadline the claimant meets -- to commence within the time the governing place's limitation law allows, which s 5 makes
part of the law the court applies -- is a regulative rule run by EVALTRACE inside an exported question.

The Act sits in the claims set because of its subject: time limits for claims tried in the Northern Territory under
another place's law, such as an injury suffered interstate and sued on in Darwin.

## Edition

- **Act:** Choice of Law (Limitation Periods) Act 1994 (NT), Act No. 45 of 1994, assented 20 September 1994, commenced
  7 November 1994 (Gaz G44, 2 November 1994, p 5). The deposited text is reprint REPC071, "as in force at 7 November
  1994", the current reprint on the NT Legislation register when retrieved on 6 November 2026; its list of legislation
  records no amendment: `../../registers/source-bundle/Choice-of-Law-Limitation-Periods-Act-1994-NT-current-reprint-REPC071.txt`.
- **Numbers set elsewhere:** none. The Act fixes no period, amount or fee. Its only date is its commencement.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (commencing the day after the last day asserted to be in time) was run once in a scratch
copy, since deleted, and showed as "assertion failed" (54 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clpnt-dates.l4` | 0 | 0 | 0 | 0 |
| `clpnt-claims.l4` | 0 | 0 | 0 | 0 |
| `clpnt-cases.l4` | 0 | 0 | 55 | 55 |

Every exported question has cases, with the edges: proceedings instituted on 6 and on 7 November 1994; not yet instituted
(today after, and a hypothetical today before, commencement); each element of the s 4 definition missing; each forum and
each governing law for s 5 and s 6, and the order in which they are checked; commencing on the last day the governing
limitation law allows, the day before, the day after, on the day time began and before it; not yet commenced with today
the last day and the day after; a period running from 29 February 2024; the regulative rule alone on day 0, the day
before the deadline, the deadline and the day after; each condition of s 6 failing in turn.

**No mirror cases.** One seat.

## Seat

**The person bringing a claim** (`clpnt-claims.l4`): the claimant whose claim is before a court of the Northern Territory
or an arbitrator and is governed by the law of an Australian State, another Territory or New Zealand. "Does this Act
apply to my proceedings?", "Is this time rule a limitation law?", "Whose time limit applies to my claim?", "Am I in
time?", "If I ask the court to extend time under that law, how must it decide?".

The Act speaks to the court ("applied accordingly by the court", "is to be exercised"); the encoding turns that into what
it means for the claimant. The court and the arbitrator get no seat: how the courts of the other place exercise the
discretion, and whether following them is practicable, are asked as facts. No second seat was written: the party
answering the claim asks the same questions with the same answers (the time limit that binds the claimant is the
defence the respondent raises).

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number. The limitation law
  of the other place is not brought in: its last day is the claimant's fact.
- **The actors the text names.** Followed: the court (including an arbitrator), the courts of the other place, the
  claimant (as "a claim" and "proceedings instituted").
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: which place's substantive law
  governs the claim (common-law choice of law, not stated in the Act); how the courts of that place exercise the
  discretion in comparable cases; whether following them is practicable (s 6).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "limitation law" (s 4), "court"
  including an arbitrator (s 4). Asked: "State", "Territory of the Commonwealth" (Interpretation Act 1978 (NT), not
  deposited), "substantive law", the other place's limitation period and its counting.
- **One case is the text's natural unit.** Followed: one claim in one proceeding or arbitration.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed: s 1 (short title) and s 2 (commencement) out, except for the
  commencement date that s 3 needs.

## Scope

**In.** ss 3, 4, 5 and 6: the whole operative Act. The commencement date under s 2, from the endnotes' list of legislation.

**Out, and why.**
- s 1 (short title), s 2 (commencement): machinery; the commencement date is used.
- The limitation laws of the States, the other Territories and New Zealand, and the Territory's own Limitation Act 1981
  (deposited at `subjects/au/nt/limitation-act-1981`, not encoded here): not this Act. The governing law's last day is
  asked; the encoding counts nothing for it. Read with the Limitation Act 1981 where Territory law governs (s 5 then
  does not apply).
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4 "unless the contrary intention appears" -- `s 4 -- is it a limitation law` and every question using "court" --
  no contrary intention found in ss 3, 5, 6; the definitions applied as written -- a contrary intention in s 3
  ("proceedings instituted"), which suits a court better than an arbitration.
- **F2** s 4 "court includes an arbitrator", read into "a court of the Territory" in ss 5, 6 -- `a court of the
  Territory` -- an arbitrator counts when the arbitration is held in the Northern Territory; an arbitrator elsewhere does
  not -- an arbitrator counts wherever seated if the arbitration is conducted under Territory law, or any arbitrator counts.
- **F3** s 5, the time the governing limitation law allows -- `s 5 -- am I in time` and the regulative rule -- the claimant
  states the day time began and the last day, read from that law; a commencement on the last day is in time, the day
  after is not -- the encoding counting the period itself (each place counts differently, and that counting is not this
  Act's).
- **F4** s 3 "proceedings instituted" -- `the day of institution` -- for proceedings not yet instituted, the day is today
  (they can be instituted no earlier), so s 3 never excludes them once the Act is in force; for an arbitration, the day
  the arbitration is commenced (the s 4 wording) -- asking for the intended date; the day of some later step.
- **F5** ss 5, 6 "another Territory of the Commonwealth" -- `a State or another Territory of the Commonwealth or New
  Zealand` -- any Territory other than the Northern Territory, internal (the Australian Capital Territory, the Jervis Bay
  Territory) or external (Norfolk Island and the others), asked as one choice -- the internal Territories only.
- **F6** s 5 "If ... is to govern a claim before a court of the Territory" -- `s 5 -- whose time limit applies to my
  claim` -- when the "if" fails, the text's no on s 5 (ruling (b) of 2026-11-05 read with "if"), with "this Act does not
  say which time limit applies" -- NOTHING, since the Act is silent on what applies instead.
- **F7** s 5, a commencement before time began to run -- `s 5 -- am I in time` -- in time (counted as day 0) -- premature,
  which is that law's question.
- **F8** s 6 "as far as practicable" -- `s 6 -- how must the court use a discretion under that limitation law` -- where
  following the other place's courts is not practicable, NOTHING ("s 6 says no more"; a limit in the section's own
  wording) -- JUST FALSE (the s 6 duty does not arise).
- **F9** s 6 "Where a court of the Territory exercises a discretion" -- the same function -- no discretion asked for, a
  court outside the Territory, or a limitation law of the Territory or a foreign country: the text's no (ruling (b) of
  2026-11-05, a "where" condition) -- NOTHING.

Sites decided without a fork line: s 3's "does not apply to proceedings instituted before that commencement" is a flat
negative, answered as the text's no; s 4's "means" definition answers FALSE when an element fails.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries one `NOTHING-kind` tag (s 6, F8). Most questions answer with a choice from a list rather than a
MAYBE BOOLEAN: the answer marked "NOTHING-kind" is the NOTHING answer, and the answers marked "the text's no" are JUST
FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The time the governing limitation law allows is the regulative rule (`MUST commence WITHIN` the days to its last day,
`LEST BREACH`), run by EVALTRACE inside the question; outside it the answer is "out of time ... only a discretion that law
gives the court can help (see s 6)".

## What the Act turns out to say

1. **The Act sets no time limit of its own.** It only decides whose limitation law a Territory court applies, and how it
   uses a discretion under it. A claimant's actual deadline is in the other place's Act. The encoding asks for that last
   day and does not compute it. Asserted (the in-time cases take it as a fact).
2. **The title year is 1994, not 1993.** The instrument was named to this encoding as the "Choice of Law (Limitation
   Periods) Act 1993 (NT)"; the register, s 1 and the endnotes give 1994 (Act No. 45 of 1994). The 1993 Act of that name
   is New South Wales's. The endnotes' list of legislation also misspells the title as "Choice of Law (Limitations
   Periods) Act 1994"; s 1 is correct. Not law; noted only.
3. **New Zealand is in from the start.** Unlike the Western Australian Act (its s 3(2), (3)), the NT Act needs no
   proclamation before it reaches New Zealand: ss 5 and 6 name New Zealand outright and s 3 has no New Zealand rule.
   Asserted (s 5 and s 6 cases with New Zealand law and no declaration input).
4. **"Another Territory of the Commonwealth" is not defined.** Whether it reaches the external Territories (Norfolk Island,
   Christmas Island and the others) or only the Australian Capital Territory and the Jervis Bay Territory turns on the
   Interpretation Act 1978 (NT), not deposited (fork F5).
5. **"Court includes an arbitrator", but ss 5 and 6 say "a court of the Territory".** Which arbitrators are "of the
   Territory" is not said (fork F2). s 3 speaks of "proceedings instituted", which reads awkwardly for an arbitration
   (fork F4).
6. **s 6 is not tied to s 5.** On its words it applies whenever a Territory court exercises a discretion under the
   limitation law of a State, another Territory or New Zealand, whether or not that place's law governs the claim.
   Encoded as written: the s 6 question asks for the place whose limitation law gives the discretion.
7. **s 3 looks at the day proceedings were instituted, not the day the cause of action arose.** A cause of action from
   before 7 November 1994 is reached ("extends to"); proceedings instituted before that day are not, even if still
   running. Asserted.
8. **The reprint is the 1994 text.** REPC071 is "as in force at 7 November 1994" and lists no amendment; the register
   showed it as current and in force on 6 November 2026. If an amendment exists that the reprint does not show, this
   encoding would miss it.

## Before this is worth relying on

- The Interpretation Act 1978 (NT) for "State" and "Territory" (finding 4, fork F5), not deposited.
- A check of the NT register's history listing that no amendment post-dates REPC071 (finding 8).
- A lawyer's view on forks F2, F4, F5, F6 and F8, and on finding 6; an independent test pass and a human gate.
