# Civil Proceedings Act 2011 (Queensland), Part 13A -- baseline encoding, the person with a claim in a representative proceeding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The focus is **Part 13A (representative
proceedings in the Supreme Court, ss 103A-103ZC)**, encoded whole, with s 111 (the transitional provision that says
which proceedings Part 13A reaches). The rest of the Act (Parts 1-13 and 14-19: interest, damages discount, enforcement,
money in court and so on) is outside this focus and is left for other encodings beside this one.

Files: the dates in `cpq13a-dates.l4` (built-in date functions only, no daydate), the rules and the exported questions
in `cpq13a-member.l4` (each exported question calls a rule defined beside it or is the rule), and the worked cases in
`cpq13a-cases-member.l4`.

## Edition

- **Act:** Civil Proceedings Act 2011 (Qld), Act No. 45 of 2011 (`act-2011-045`), the version in force from
  29 October 2026, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2011-045.txt` (text
  sha256 `34fbd8d61aa4d587bb1e9250b7ce8a087137fcd057a29443cc4bc6cba169d1a8` per its `.meta.json`; a Windows checkout
  with CRLF line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the
  authorised PDF.
- **Numbers set elsewhere:** none. Part 13A's own numbers are in the text: 7 persons (s 103B(1)(a), s 103I), 6 months
  (s 103W(3)(c)), 21 days (s 103Y(3)). Every other date is fixed by the court (the opt-out date, the fund claim date,
  the date in a s 103H leave) or by rules of court (the time for appealing): asked.
- **Not deposited, and asked as facts:** the commencement of Part 13A (inserted by the Limitation of Actions (Child
  Sexual Abuse) and Other Legislation Amendment Act 2016; s 111(1)), asked as yes/no (fork F1); "person under a legal
  incapacity" (Supreme Court of Queensland Act 1991, borrowed by s 103E(3)); the time for starting an appeal (Uniform
  Civil Procedure Rules 1999, deposited under its own subject but not imported); the limitation period of the member's
  claim (Limitation of Actions Act 1974 or another law), whose last day is asked.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied"; the other two files give no
diagnostics.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cpq13a-dates.l4` | 0 | 0 | 0 | 0 |
| `cpq13a-member.l4` | 0 | 0 | 0 | 0 |
| `cpq13a-cases-member.l4` | 0 | 0 | 166 | 166 |

Every exported question has cases, with the edges: 6 and 7 persons (s 103B(1)(a)); each limb of s 103B(1) failing and
s 111; each kind of person in s 103D(2) with and without written consent; opt-out notice on the day before the date, on
the date, on the day the proceeding started, the day before it started, and against a later date (s 103G); a hearing
the day before and on the opt-out date (s 103G(4)); a cause of action accruing on the start day, the day after, the day
before and on the date fixed under s 103H; every state of the proceeding for s 103Z, with the new last day, the day
after it, a period with no days left, and a period already over before the proceeding started; a fund claim date exactly
6 months after the order (31 August to 28 February, and to 29 February in a leap year) and a day short; a fund claim on
the last day, the date itself, late with and without leave, and after full distribution; an excess of costs of 1 dollar,
none, and a shortfall (s 103ZC); every costs role; every notice matter with and without damages, dispensation and
orders; each s 103K ground including the s 103K(2) "merely because" case; a group member's appeal on the representative
party's last day, the next day, the 21st further day and the 22nd, across a year end.

## Seat

**The person with a claim** (`cpq13a-member.l4`): an individual whose claim against a defendant is, or could be,
pursued in a representative proceeding (class action) in the Queensland Supreme Court -- usually a **group member**,
and, for the questions that say so (starting the proceeding, its originating process, carrying on after one's own claim
ends, settling one's own claim, withdrawing, carrying on after the proceeding is declassed), the **representative
party**, who is a group member who starts and runs the proceeding. Both are individuals with a claim of their own, and
the Act gives them the same rules from two positions, so one seat module serves both (a role is asked where it
matters). "Can a class action be brought for my claim?", "Am I in the group?", "By when can I opt out?", "Is my time to
sue running?", "Am I bound?", "Can I be made to pay costs?", "By when must I claim from the fund?", "Can I appeal if the
representative party does not?".

The defendant meets the same rules from the other side; no defendant seat is written. No seat for the court or the
Court of Appeal.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. Part 13A's numbers are in the text; no
  instrument sets them. The commencement of Part 13A is asked (F1).
- **The actors the text names.** Followed: the representative party, group members, sub-group members and their
  representative party, the defendant, the court.
- **Judgments answered conditionally.** Whether circumstances are "related", an issue "substantial" and "common", a
  representative "not able adequately to represent", distribution costs "excessive", a ground "in the interests of
  justice", notice given "in sufficient time", an assessment "reasonably accurate", costs "reasonably incurred" and
  "likely" to exceed: all asked, never decided. Each "may" of the court is answered as what the court may do.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: s 103A "group member" (with s 103D and
  s 103G), "representative party", "representative proceeding" (s 103B). Asked: "person under a legal incapacity",
  "standing" (s 103C(1)), the limitation period of the claim.
- **One case.** One person's claim in one representative proceeding.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input ("class action" is used as a gloss of
  "representative proceeding", never in the rules).
- **Operative sections in; machinery out.** s 103ZA (general power to make orders) and the court's own procedure (form
  of notices, directions) are out; see Scope.

## Scope

**In (29 exported questions):** s 111 and s 103B (can a representative proceeding be started); s 103C(1), (2) (can I
start it); s 103C(3) (can I carry on after my claim ends); s 103F (the originating process); ss 103A, 103D (am I a group
member); s 103E (litigation guardian); s 103G(1)-(3) (have I opted out in time; the last day to opt out); s 103G(4) (can
the hearing start before the opt-out date); s 103H (joining when the cause of action accrued later); s 103Z (is my
limitation period suspended; by when must I start my own proceeding; am I in time to do so); s 103X with s 103U(8) (am I
bound); s 103V(1)(f), (3) (aggregate damages); s 103W(3)(c) (is the fund claim date lawful) and (3)(b)-(c), (4) (am I in
time to claim from the fund); s 103ZC (the most paid from the damages for the representative party's costs);
s 103ZB with ss 103M(3), 103N(2) (can I be ordered to pay costs); s 103T (must I be given notice); s 103R (settlement or
discontinuance); s 103S(1) (settling the representative party's own claim); s 103S(2), (4) (withdrawing); s 103P and
s 103S(3) (replacing the representative party); ss 103I, 103J, 103K (declassing); s 103L (what then); s 103Q (stay of
execution); s 103Y(3) (a group member's appeal, and its last day).

**Regulative rules:** four, each run by EVALTRACE inside an exported question that takes only plain facts (a CONSIDER on
an EVALTRACE matches FULFILLED only):
- s 103G: I DO give written notice that I opt out WITHIN the days to the day before the date fixed;
- s 103W: I DO make a claim for payment from the fund WITHIN the days to the day before the date stated;
- s 103Y(3): the representative party DOES start an appeal WITHIN its time, LEST I DO start one WITHIN a further 21 days;
- s 103Z: once the period runs again, I DO start my own proceeding WITHIN the days left.
Each BREACH marks only that the time passed; not opting out, not claiming, not appealing and not suing are not wrongs.

**Out, and why:**
- s 103M(1), (2), s 103N(1), s 103O (directions on remaining issues, sub-groups, individual issues, other proceedings):
  the court's management; what they mean for the person (costs) is in through ss 103M(3), 103N(2).
- s 103U(1)-(7) (form, content and manner of notices; who gives them): the court's order; s 103U(8) is in.
- s 103V(1)(a)-(e), (g), (2), (4) and s 103W(1), (2), (3)(a), (d), (5) (the kinds of judgment, administration of the fund,
  interest, the distribution date, payment of what is left to the defendant): the court's orders, giving the person no
  question they can answer from facts beyond the ones in scope. Noted: under s 103W(5) money left in the fund after the
  distribution date may be paid back to the defendant.
- s 103Y(1), (2), (4)-(6) (who the parties to an appeal are; notice of appeal; Part 13A on appeal): procedure; s 103Y(2)
  is used only to say that a representative party's appeal is the group's.
- s 103ZA (general power to make orders): machinery.
- The rest of the Act: outside this focus.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 111(1) "started after the commencement" -- `ss 103B(1), 111 -- a representative proceeding may be started` --
  asked as yes/no (the amending Act's commencement is not in the deposited text) -- fix the day once the commencement is
  deposited.
- **F2** s 103B(1)(b), (c) "same, similar or related circumstances", "substantial common issue" -- same function --
  asked as facts, in the end the court's view -- worked out from facts (no test in the text to work them from).
- **F3** s 103C(1) "has a sufficient interest ... if the person has standing" -- `Can I start a representative
  proceeding` -- a condition introduced by "if": "no" without a claim or standing -- "not covered" (s 103C(1) gives a
  sufficient condition and does not say "only if").
- **F4** s 103C(3) "a person who has started" -- `Can I carry on after my own claim ends` -- a representative party who
  did not start it (substituted under s 103P or s 103S(3)) and whose claim has ended: NOTHING -- read "a person who has
  started" as any representative party, given s 103A's definition (finding 3).
- **F5** s 103A "group member" with s 103G -- `Am I a group member` -- a person who has opted out is no longer a group
  member -- they remain a "group member" who has opted out (s 103X(b) speaks of "a person who has opted out", and
  s 103Z(2)(a) of "the member opts out").
- **F6** s 103G(2) "before the date fixed" -- `Have I opted out in time`, `What is the last day I can opt out` -- the
  last day is the day before the date; notice is "given" on the day the person gives it -- notice given when received
  by whoever the court's order names.
- **F7** s 103H(2) "accrued after the start ... but before the date fixed" -- `Can I be added to the group after my cause
  accrued` -- outside the limits "not covered by s 103H" (a grant limited in its own words, no "only": ruling (c)) --
  "no" (JUST FALSE kind). A cause accruing on the day the proceeding started is not "after the start".
- **F8** s 103Z counting -- `s 103Z -- the new last day` -- the days left are those from the day the proceeding started
  to the old last day (the starting day counted as used); the period runs again on the day of the opt-out or decision,
  and the new last day is that day plus the days left; a period over before the proceeding started stays over -- the
  starting day not used (one day more); the period running again from the day after the event (one day more); or "start
  running again" read as a fresh period (finding 2). Declassing and approved settlement: NOTHING (finding 1).
- **F9** s 103W(3)(c) "at least 6 months after" -- `s 103W(3)(c) -- at least 6 months after the order` -- the
  corresponding day 6 months on (the last day of the month where it has no such day) is enough -- the day after it
  (counting "after" as excluding the corresponding day), or the first of the next month where the month is short.
- **F10** s 103X(b) "binds the group members described, other than a person who has opted out" -- `Am I bound by the
  judgment` -- opted out: JUST FALSE ("other than" read as the text's no); not described: NOTHING -- opted out: NOTHING
  ("other than" an exception to a grant, the Act not saying such a person is free of the judgment by other law).
- **F11** s 103ZB(b) "other than under section 103M or 103N" -- `Can I be ordered to pay costs` -- a sub-group
  representative party and an individual allowed to appear may be ordered to pay the costs those sections make them
  liable for, and only those -- they may be ordered to pay costs generally once either section applies. A
  representative party who is also appointed sub-group representative party is answered as representative party.
- **F12** s 103S(1) "with the leave of the court", s 103S(2) "seeking leave to settle, or who has settled" -- `Can I
  settle my own claim as representative party`, `Can I withdraw as representative party` -- without leave JUST FALSE; a
  representative party not settling their claim: "not covered" -- "no" (s 103S(2) as the only route to withdraw).
- **F13** s 103Y(3) "within a further 21 days" -- `Can I appeal on behalf of the group`, `By when must I appeal on
  behalf of the group` -- the 21 days run from the end of the representative party's last day (the trace waits half a
  day past it); an appeal by a group member on or before that last day is "not yet" -- the 21 days counted from the day
  after, ending a day later.
- **F14** s 103T(2) "may dispense ... if the relief sought ... does not include a claim for damages" -- `Must I be given
  notice` -- a dispensation where damages are claimed is treated as not available, and notice must be given -- the
  dispensation stands as the court's order until set aside.
- **F15** s 103K(1)(e), (2) "merely because" -- `Can the proceeding stop being a representative proceeding` -- when the
  only reason is that the group leaves others out or is aggregated for a funding arrangement, s 103K does not apply --
  the court may still find another ground; the person picks the court's ground from a list.
- **F16** s 103W(4) "if the fund has not been fully distributed" -- `Am I in time to claim from the fund` -- a late claim
  once the fund is fully distributed: "no" (a condition introduced by "if") -- "not covered".

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 103B(1)'s, s 103C(1)'s and s 103W(4)'s "if" conditions, s 103D(2)'s "only if", s 111(1)'s "only",
s 103F's "must", s 103G(4)'s and s 103R(1)'s flat negatives, s 103V(3)'s "must not ... unless" and s 103ZB(b)'s "may not"
give "no" or `JUST FALSE`; s 103H's limits and s 103S(2)'s settling condition give "not covered" (F7, F12); s 103X's
"other than" and s 103ZB's "other than" are the case-by-case sites F10 and F11; s 103Z(2)'s unnamed events give "not
covered" (F8).

## What the Act turns out to say

1. **s 103Z is silent on declassing and on settlement.** The limitation period "does not start running again unless"
   the member opts out or the proceeding "and any appeal" is "decided without finally disposing of the member's claim".
   An order under s 103I, 103J or 103K that the proceeding no longer continue under Part 13A does not decide it (s 103L
   lets it go on as the representative party's own proceeding), and a settlement or discontinuance approved under
   s 103R is not a decision in terms. Read literally, a group member whose claim is left out of a declassed proceeding
   has a period that never starts again. The encoding answers "not covered" for both. Asserted (`gap`).
2. **"Start running again" does not say from where.** s 103Z(2) is read as resuming the period with the days that were
   left when the proceeding started (F8); a fresh full period is the other reading. The section also does not say what
   happens if the period had already expired when the proceeding started; the encoding leaves the old last day
   standing. Asserted.
3. **A substituted representative party is outside s 103C(3).** s 103A defines "representative party" as "a person who
   starts a representative proceeding", yet ss 103P(1)(a) and 103S(3)(a) substitute "another group member as the
   representative party". The substitute did not start the proceeding, so s 103C(3)'s protection ("a person who has
   started ... retains standing ... even if the person ceases to have a claim") does not reach them in its words.
   Asserted (`Can I carry on after my own claim ends` FALSE TRUE is NOTHING).
4. **Consent is not needed, and no notice is needed to be bound.** s 103D(1) makes membership opt-out for everyone but
   government bodies, and s 103U(8) says a member's failure to receive a notice does not affect a judgment. A person can
   be bound by a judgment (s 103X) without having known of the proceeding. Asserted.
5. **Seven is the floor at the start, and again later.** s 103B(1)(a) needs 7 or more persons to start; s 103I lets the
   court continue or end the representative form if it later appears likely there are fewer than 7 group members. The
   count at the start includes the representative party; the s 103I count is of "group members", whom s 103A defines
   as the persons on whose behalf the proceeding is started -- whether the representative party is one of them is not
   said.
6. **A group member's appeal has a fixed window, but its start is set elsewhere.** s 103Y(3) gives "a further 21 days"
   after "the time for starting the appeal", which is set by rules of court (not this Act). The encoding asks the
   representative party's last day. s 103Y(5) applies Part 13A to an appeal "other than section 103G": there is no
   fresh right to opt out on appeal.
7. **The fund claim date has a floor and no ceiling.** s 103W(3)(c) requires the date to be "at least 6 months after"
   the order; late claims depend on the court and on money being left (s 103W(4)); after the distribution date, what is
   left may go back to the defendant (s 103W(5)).
8. **A sub-group representative party is not "a representative party" for s 103ZB.** The Act defines the two terms
   separately (s 103A). s 103ZB(b) therefore protects a sub-group representative party from costs except under s 103M,
   which makes them liable for the sub-group's issues. Asserted.
9. **Dispensing with notice is tied to the relief, not to the matter.** s 103T(2) lets the court dispense with the
   s 103T(1) notices only where no damages are claimed. For settlement (s 103T(4)) the test is different: whether the
   court considers it just. Asserted.
10. **No cost-sharing order beyond s 103ZC.** Part 13A has no group costs order or commission on damages; the only way
    the representative party's unrecovered costs come out of the group's damages is s 103ZC, capped at the excess of
    costs reasonably incurred over costs recoverable. Asserted.
11. **The commencement of Part 13A is not in the text** (F1). s 111 speaks of "the commencement" of the 2016 amending
    Act, which the deposited conversion does not date.

## Before this is worth relying on

- Deposit the commencement of the Limitation of Actions (Child Sexual Abuse) and Other Legislation Amendment Act 2016,
  Part 13A provisions, and fix the day in s 111 (F1).
- Check the conversion against the authorised PDF.
- A lawyer's view on findings 1, 2, 3 and 5 and forks F4, F5, F8, F10, F11 and F13; case law on s 103Z and on the
  Federal Court of Australia Act 1976 Part IVA provisions it follows (not deposited) may settle F8 and finding 1.
- Link to the Limitation of Actions Act 1974 encoding for the old last day, and to the Uniform Civil Procedure Rules 1999
  for the time for appealing, once IMPORT can reach another subject.
- An independent test pass and a human gate.
