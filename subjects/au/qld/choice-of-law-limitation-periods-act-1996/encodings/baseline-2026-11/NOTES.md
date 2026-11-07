# Choice of Law (Limitation Periods) Act 1996 (Queensland) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The shape follows the baseline of the
Victorian twin, `subjects/au/vic/choice-of-law-limitation-periods-act-1993/encodings/baseline-2026-11/`, written afresh
for the Queensland text (nothing is imported from it: IMPORT cannot reach another subject's folder). The dates are in
`clpq-dates.l4` (built-in date functions only, no daydate), the rules and the claimant's exported questions in
`clpq-claimant.l4` (each exported question calls a rule defined beside it), and the worked cases in
`clpq-cases-claimant.l4`.

The Act is seven sections, so **the whole Act is encoded**. It is a gate in front of a limitation period: when the law of
another State, a Territory or New Zealand (a "relevant place") governs a claim before a court (or arbitrator) in
Queensland, that place's limitation law counts as substantive and the court applies it (s 5), and any discretion it
gives, such as a power to extend time, is exercised as that place's courts would (s 6). Unlike the Victorian and New
South Wales Acts, the Queensland Act does not reach New Zealand until a regulation declares that it does (s 3(2), (3)).
For a person injured interstate and suing in Queensland, this decides whether the Limitation of Actions Act 1974 or
the other place's limitation law sets the time to sue.

## Edition

- **Act:** Choice of Law (Limitation Periods) Act 1996 (Qld), Act No. 5 of 1996 (`act-1996-005`), the version in force
  from 1 November 1996, which was the current in-force version on 6 November 2026, deposited at
  `../../registers/source-bundle/act-1996-005.txt` (text sha256 `1a25ddb6...0cb0c5941960b7` of the committed file, per
  its `.meta.json`; a Windows checkout with CRLF line endings hashes differently). A plain-text conversion of the
  Queensland Legislation HTML view, not the authorised PDF.
- **Numbers set elsewhere:** none. The Act's one day is its commencement, fixed by proclamation (s 2). The proclamation
  is not deposited; 1 November 1996, the day the deposited version runs from, is taken as the commencement (fork F3).
- **Not deposited, and asked as facts:** whether a regulation under s 3(2) and s 7 has declared that the Act applies to
  New Zealand, and the day the declaration takes effect; the other place's limitation law (its period, the day the
  period runs from, whether it gives a discretion, and any extension the court grants under it); which place's
  substantive law governs the claim (the court's choice-of-law decision).
- **Deposited beside it, and named but not encoded here:** the Limitation of Actions Act 1974 (`act-1974-075`), whose
  s 43A makes Queensland's own limitation law part of Queensland's substantive law; the Workers' Compensation and
  Rehabilitation Act 2003, chapter 6 (choice of law for damages claims against an employer); the Jurisdiction of Courts
  (Cross-vesting) Act 1987, s 11.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clpq-dates.l4` | 0 | 0 | 0 | 0 |
| `clpq-claimant.l4` | 0 | 0 | 0 | 0 |
| `clpq-cases-claimant.l4` | 0 | 0 | 102 | 102 |

Every exported question has cases, with the edges: proceedings started on 31 October and 1 November 1996 (s 3(1)), a
cause of action arising on those days; New Zealand with no declaration, and with a declaration taking effect on an
invented day (1 July 2000), a proceeding started the day before and on that day (s 3(2), (3)); each kind of place and
each forum (s 5, s 6); a law with and without a discretion (s 6); the last day of the period, the day before and the
day after; an extended day and the day after it; a 29 February start (3, 4 and 6 years on), a 31 August start with a
6-month period, a period of no length, and a proceeding started before the period runs.

## Seat

**The claimant** (`clpq-claimant.l4`): the person who brings a claim before a court or an arbitrator in Queensland where
the law of another State, a Territory or New Zealand governs it -- typically someone injured in another State who sues
in Queensland. "Is the time limit I face a limitation law?", "Does the Act reach my proceeding?", "Whose limitation law
will the court apply?", "How will the court use a discretion under that law?", "Am I in time?", "By when must I start?".

The Act puts no duty or liability on any party; the person who answers the claim meets the same rules from the other
side (the same answers tell a defendant which limitation defence is available), so no second seat is written. No seat
for the court, the arbitrator, the Governor in Council or the courts of the other place.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, with a gap: the proclamation fixing the
  commencement and any New Zealand declaration are not deposited (F3; the declaration is asked).
- **The actors the text names.** Followed: a court of the State (including an arbitrator), the courts of the relevant
  place.
- **Judgments answered conditionally.** Which place's substantive law governs (the court's choice of law), whether the
  court extends time, and how it exercises a discretion "as far as practicable" in "comparable cases" are asked or
  stated, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: s 4 "limitation law" (from two facts),
  "relevant place" (from a choice of place) and "court includes arbitrator". Asked: "State", "Territory" (by choice
  from a list), "substantive law" and its governing place, and everything the other place's limitation law says.
- **One case.** One claim, one proceeding (or arbitration).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** s 1 (short title) and s 7 (regulation-making) are out; s 2 (commencement)
  is in, because s 3(1) turns on the day it gives; the s 3(2) declaration is in as an asked fact.

## Scope

**In:** s 2 (as the day s 3(1) counts from); s 3(1) (causes of action that arose earlier are reached; proceedings
started earlier are not); s 3(2) and (3) (New Zealand only once declared, and not for a proceeding started before the
declaration takes effect); s 4 (court, limitation law, relevant place); s 5 (a relevant place's limitation law is part
of its substantive law and is applied); s 6 (its discretions exercised as its courts would). What s 5 means for the
claimant in days -- in time or not under that place's period, and the last day -- is worked out from the period and
starting day asked as facts.

**Regulative rule:** one. s 5: I DO start my proceeding or arbitration WITHIN the days that place's limitation period
allows (counted from the day that law says the period runs from), LEST the period is not met. It is run by EVALTRACE
inside the exported questions, which take only dates, numbers, yes/no facts and choices (a CONSIDER on an EVALTRACE
matches FULFILLED only). The BREACH marks only that the period was not met: not suing is not a wrong.

**Out, and why:**
- s 1 (short title), s 7 (regulation-making power): machinery. The one regulation the Act contemplates (the s 3(2)
  declaration) is asked as a fact.
- The other place's limitation law (for example the Limitation Act 1969 of New South Wales, the Limitation Act 2010 of
  New Zealand): not this Act. Its period, starting day and discretions are inputs.
- The choice of law itself (which place's substantive law governs a claim): the Act takes it as given ("is to govern").
- Queensland's own limitation law where Queensland law governs (Limitation of Actions Act 1974 s 43A does that work),
  and the limitation law of any country other than New Zealand: this Act says nothing; the answers say "outside this
  Act".

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4 "court includes arbitrator", read into s 5 and s 6 "a court of the State" -- `ss 4, 5, 6 -- a court of the
  State` -- an arbitrator counts when the arbitration is in Queensland -- an arbitrator counts wherever seated, if
  Queensland law (and so this Act) is applied by them; or "of the State" limits the definition to Queensland courts.
- **F2** s 4 "relevant place means another State, a Territory or New Zealand" ("State" and "Territory" undefined in
  the Act) -- `Place`, `s 4 -- a relevant place` -- any Australian State other than Queensland, and any Australian
  Territory (the person picks) -- the Acts Interpretation Act 1954 (not deposited) may narrow "Territory" (for example
  to internal Territories).
- **F3** s 2 "a day to be fixed by proclamation" -- `the day this Act commenced` -- 1 November 1996, the day the
  deposited version is in force from -- a different proclaimed day (the proclamation is not deposited; if the first
  version on the site was not the as-commenced version, the day could differ).
- **F4** s 3(1) "started before the commencement" -- `s 3(1) -- started before the commencement` -- a proceeding
  started on 1 November 1996 is reached -- one started earlier on that day than the commencement is not.
- **F5** s 3(2) "until it is declared under a regulation to apply" and s 3(3)(b) "before the declaration takes effect"
  -- `ss 3(2), 3(3) -- New Zealand` -- one day: the Act reaches New Zealand law from the day the declaration takes
  effect, and a proceeding started on that day is reached -- "declared" in s 3(2) could be read as the day the
  regulation is made or notified, if earlier than the day it takes effect; then for a proceeding started between the
  two days s 3(2) would no longer bar it but s 3(3) still would, so the answers agree in every case.
- **F6** s 5 applied to a period of years and months -- `the date ... years and ... months after`, `started by the last
  day` -- the period ends at the end of the corresponding day (the day the period runs from is excluded), so starting
  on that day is in time and the day after is not -- the period ends the day before the corresponding day. How the
  other place counts its own period is that place's law, not deposited.
- **F7** same functions, a start on a day the end month lacks (29 February, 31 August plus 6 months) -- the last day of
  that month (28 February) -- the first day of the next month.
- **F8** `started by the last day` -- a proceeding started before the day the period runs from is in time -- "not
  covered" (a claim started before its cause of action accrues may fail for other reasons; that is not this Act).
- **F9** s 5 and s 6 "If ..." unmet -- `s 5 -- the limitation law the court applies`, `s 6 -- how the discretion is
  exercised` -- "s 5 (or s 6) does not apply" (a condition the text introduces with "if": JUST FALSE kind), with "which
  limitation law applies is outside this Act" -- "not covered" (NOTHING kind), since the Act is silent on what the court
  does instead.
- **F10** s 6 with s 3 -- `s 6 -- how the discretion is exercised` -- s 6 applies whenever a Queensland court exercises
  a discretion under a relevant place's limitation law, not only when s 5 brought that law in; and s 3(1), (2) and (3)
  limit s 6 as they limit the whole Act, s 3(3) being read as reaching a discretion under New Zealand's limitation law
  -- s 3(3) speaks only of a claim the substantive law of New Zealand "is to govern", so a discretion under New Zealand
  limitation law in a claim governed by other law is outside s 3(3) (and only s 3(2) applies).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 4 "limitation law" and "relevant place" are "means" definitions (`JUST FALSE` / FALSE when a limb
fails); s 3(1)'s and s 3(3)'s "does not apply" are flat negatives, and s 3(2)'s "until" a period the text fixes (all
"no" constructors); s 5's and s 6's "If" conditions, when unmet, give "does not apply" constructors (F9); the "by when"
question answers `NOTHING` where s 5 does not apply, because the Act then sets no period at all.

## What the Act turns out to say

1. **The Act decides whose limitation law, never what it says.** Every answer about time depends on the other place's
   limitation law, which is not this Act. The encoding asks its period and starting day, and so cannot tell a claimant
   what the period is (for example, whether the other place uses a discoverability start or an accrual start).
2. **New Zealand is out until a regulation brings it in.** s 3(2) keeps New Zealand outside the Act "until it is
   declared under a regulation to apply", although s 4 lists New Zealand as a relevant place. Whether such a
   regulation has been made is not known from the deposited sources (none is deposited under this subject), so it is
   asked. If none has been made, a Queensland court applying New Zealand law gets no help from this Act on limitation,
   and the common law's characterisation of the limitation law (case law, not deposited) decides instead. Asserted (`s5 NZ undeclared`). Check
   the Queensland register of subordinate legislation under this Act.
3. **Two moments for New Zealand, or one** (F5). s 3(2) speaks of being "declared", s 3(3) of the declaration "taking
   effect". On the reading taken the answers do not depend on the difference.
4. **s 3(3) is narrower than s 3(2)** (F10). s 3(3) bars the Act only where the substantive law of New Zealand governs
   the claim; it says nothing directly of s 6 discretions under New Zealand limitation law in a claim governed by
   other law. The encoding applies it to s 6 as to s 5.
5. **"Limitation or exclusion".** The Queensland definition (s 4) reaches a law that "limits or excludes" a liability,
   wider in words than the Victorian Act's "limitation of any liability"; it still names no law that extends time,
   though s 6 assumes one ("a discretion conferred under a limitation law"). The Workers' Compensation and
   Rehabilitation Act 2003 s 322(1)(b) is explicit: substantive law there includes a law prescribing the time to sue
   "including a law providing for the extension or abridgement of that time".
6. **A notice step is not a limitation law.** A requirement to give notice of a claim within a time bars nothing "by
   reference to the time when a proceeding ... is started", so s 4 does not make it one, and s 5 does not carry it
   across. Asserted (`Is this a limitation law` TRUE FALSE is JUST FALSE).
7. **Queensland's own law is in another Act.** Where Queensland law governs, this Act is silent; the Limitation of
   Actions Act 1974 s 43A, in the same words, makes "a limitation law of the State" part of Queensland's substantive
   law, with the same transitional rule (s 43A(3)). Nothing deposited deals with the limitation law of a country other
   than New Zealand.
8. **Work injury claims have a second gate.** For a damages claim against an employer for a work injury, the Workers'
   Compensation and Rehabilitation Act 2003 chapter 6 (s 324) makes the substantive law of the State whose workers'
   compensation scheme makes compensation payable govern the claim, and s 322(1)(b), (c) make time limits part of that
   substantive law. Where both Acts apply they point the same way; that chapter is another subject, not imported here.
9. **The commencement is not in the text** (F3). s 2 leaves it to proclamation, and the deposited conversion drops the
   history notes that would name the day.
10. **The Act's year.** The workflow that assigned this encoding named it the "Choice of Law (Limitation Periods) Act
    1993 (qld)". The Queensland Act is of 1996 (s 1 and the deposited title); the Victorian and New South Wales Acts are
    of 1993. The subject folder's slug is right.

## Before this is worth relying on

- Deposit the commencement proclamation (F3) and find out whether a s 3(2) declaration for New Zealand has been made
  (finding 2); if so, deposit it and fix the day rather than asking it.
- Check the conversion against the authorised PDF.
- Deposit and encode the limitation laws of the other States, the Territories and New Zealand, so that the period and
  its starting day can be worked out rather than asked.
- Deposit the Acts Interpretation Act 1954 and check F2, F4 and how a period is counted (F6, F7).
- A lawyer's view on findings 2, 4 and 5 and forks F1, F5, F9 and F10, an independent test pass and a human gate.
