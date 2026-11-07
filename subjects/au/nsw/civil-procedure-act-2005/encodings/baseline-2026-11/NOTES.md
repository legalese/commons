# Civil Procedure Act 2005 (NSW), Part 10 -- baseline encoding, the person with a claim in a class action

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 1 July 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Three regulative rules (opting out, s 162(2);
claiming on the fund, s 178(3)(c); appealing for the group, s 180(3)), each run by `EVALTRACE` inside an exported
question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline,
no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is Part 10 (representative proceedings
in the Supreme Court, ss 155-184), which is encoded nearly whole; the rest of the Act is out (see Scope).

## Edition

- **Act:** Civil Procedure Act 2005 No 28, corpus document `nsw_legislation:2024-07-01/act-2005-028` (in force 1 July
  2024), deposited at `../../registers/source-bundle/act-2005-028.txt` (text sha256 cd1e6add...4350853 as recorded in its
  `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Uniform Civil Procedure Rules 2005 and the Supreme Court's practice notes, which set the form of
  an opt-out notice and the time for instituting appeals; the Limitation Act 1969, which sets a group member's own
  limitation period. Each is asked as a fact (the opt-out date the Court fixes, the last day of the ordinary appeal time,
  the last day of the person's own limitation period).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cpa-p10.l4` | 0 | 0 | 0 | 0 |
| `cpa-p10-cases.l4` | 0 | 0 | 124 | 124 |

Every expected value was worked by hand from the text, with the edges: 6 and 7 persons (s 157(1)(a)); each s 159(2)
class with and without written consent; an opt-out notice given the day before the date fixed, on it and after it, and
the last day across a month end, a year end and 29 February 2028 (s 162); a hearing listed the day before the opt-out
date with and without leave, and on it (s 162(4)); a cause of action accruing on the day the class action started, the
day after, the day before the date the Court fixes and on it (s 163); each ground under ss 164-166, including the s 166(2)
"merely because" case; each part a person can hold, for ss 167, 180(3) and 181; the fund's claim day exactly six months
on, a day short, from 31 August into a common and a leap February, and across a year end (s 178(3)(c)); a fund claim on
the day fixed and the day after, with the fund distributed and not (s 178(4)); an appeal on the last ordinary day, the
day after, the 21st further day and the 22nd (s 180(3)); a limitation period ending the day before the class action
started and on that day, resuming on opt-out, on determination and on the earlier of both, and a remainder running
across 29 February 2028 (s 182); reimbursement costs equal to, one dollar over and well over the recoverable costs
(s 184).

## Seat

**The person with a claim in a class action**: a group member (or sub-group member), and the group member who starts the
class action and so becomes the representative party. Every exported question is one that person would ask ("Can I start
a class action?", "Am I a group member even though I was not asked?", "What is the last day I can opt out?", "Will the
judgment bind me?", "Can I be made to pay costs?", "Is my own time limit suspended?", "Is my claim on the fund in time?",
"Can I appeal for the group?"). The representative party is a group member with a claim of its own, so it shares the
seat; questions that differ by role take the role as an input. The defendant is a party the Part puts liabilities on
(ss 165, 178(2), (5)), but a defendant seat is not written in this baseline. The Court gets no seat: what it must or may
do is encoded as what it means for the group member.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Part sets its own numbers (7 persons,
  6 months, 21 days); the rules of court and the Limitation Act are not brought in, and their dates are inputs.
- **The actors the text names.** Followed: group member, sub-group member, representative party, sub-group
  representative party, defendant, the Court.
- **Judgments answered conditionally.** Followed: "substantial common question" (s 157(1)(c)), "appears to the Court"
  (ss 164, 171), "concludes ... excessive" (s 165), "satisfied ... interests of justice" (s 166), "satisfied ... just"
  (ss 174(4), 175(4)), "it is just" (s 178(4)), "reasonably accurate assessment" (s 177(3)), "reasonably incurred" and
  "likely to exceed" (s 184) are inputs or stated in the answer ("the Court may allow it if it is just").
- **The Act's definitions worked out; borrowed terms asked.** s 155 "group member", "representative party", "sub-group
  member" and "sub-group representative party" are the roles; "group member" as a "means" definition decides s 159.
  "Legal incapacity", "standing", "limitation period", "local rules" are asked.
- **One case.** One group member, in one class action.
- **The Act's terms with plain glosses.** Followed, in each `@desc` ("class action" glosses "representative
  proceedings").
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 155 (definitions, as the roles); ss 157-158 (commencement and standing); s 159 (consent); s 160 (legal
incapacity); s 162 (opting out, and the hearing bar in (4)); s 163 (later causes of action); ss 164-166 (grounds for
ending the class action) and s 167 (what follows); s 169(2) with s 181 (costs); s 171 (substituting the representative);
s 172 (stay of execution); s 173(1) and s 175(4) (settlement); s 174(4) (the representative party's withdrawal); s 175(1),
(2), (3), (5) (notices); s 176(8) (failure to receive a notice); s 177(3) (aggregate damages); s 178(3)(c), (4) (the fund's
claim day and late claims); s 179 (who the judgment binds); s 180(3) (appeal by another member); s 182 (suspension of
limitation periods); s 184 (reimbursement of the representative party out of the damages).

**Out, and why:**
- s 156 (application to proceedings commenced after the Part commenced): transitional; every class action now meets it.
- s 157(2), s 158(2), (3): they say what does **not** stop a class action (kinds of relief, separate transactions,
  several defendants, the representative losing its own claim); no input is needed for them. Stated in comments.
- s 161 (contents of the originating process) and s 180(6): drafting duties of the representative party's lawyers.
- ss 168(1), (2), 169(1), 170, 177(1), (2), (4), 178(1), (2), (3)(a), (b), (d), (5), 183: open powers to give
  directions and make orders, with nothing the group member can be told in advance beyond "the Court may".
- s 166(3), (4) (bar on the defendant re-applying): the defendant's position.
- s 174(1)-(3), s 180(1), (2), (4), (5): the representative party's own settlement, and the form of appeals; s 174(3)
  substitution is covered by s 171's question.
- s 175(6), s 176(1)-(7): the timing ("as soon as practicable") and the form of notices, which the Court controls;
  "as soon as practicable" has no number to encode.
- The note to s 178 (the registrar's 2.5% deduction from fund interest under s 18A) and the rest of the Act (Parts 1-9,
  Schedules): outside the focus. Part 6 Division 5 (interim payments) and Part 7 Divisions 2-3 (costs, interest) are
  claims machinery that a later layer could add.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 157(1) "by one or more of those persons" with s 158(1) -- `Can I start a class action` -- the person starting
  it must be one of the 7 or more with a claim, and is counted among them -- the 7 may exclude the representative party.
- **F2** s 159(2) "unless the person gives consent in writing" -- `Am I a group member` -- once written consent is given
  the listed person is a group member if within the description (`JUST TRUE`) -- consent only removes the bar, leaving
  membership to the Court's description.
- **F3** s 162(2) "before the date so fixed" -- `The last day to opt out`, `Have I opted out in time` -- a notice given
  on the date fixed is too late; the last day is the day before -- the date fixed is itself included.
- **F4** s 162(4) "must not commence earlier than" -- `Can the hearing start then` -- on or after the date, or with
  leave, the section is no bar (`JUST TRUE`) -- `NOTHING`, since other rules may still delay the hearing.
- **F5** s 163(1), (2) -- `Can the group be widened to include me` -- without leave the description is not altered
  (`JUST FALSE`); a person outside (2)(a) or (b) answers `NOTHING` (a grant limited in its own wording) -- `JUST FALSE`
  for (2)(a), (b) too, reading "so as to include a person" as closed.
- **F6** s 167(1)(b) "a person who was a group member" -- `What can I do after the class action ends` -- a sub-group
  representative party is a group member and may apply to be joined -- it continues on its own behalf like the
  representative party.
- **F7** s 181 "except as authorised by sections 168 and 169" -- `Can I be made to pay costs` -- only s 169(2) authorises
  costs; a sub-group representative party is not "a representative party" (s 155) and is protected -- s 168 directions
  may carry costs, and a sub-group representative party is exposed like the representative party.
- **F8** s 175(2) "may dispense ... if the relief sought ... does not include any claim for damages" -- `Must I be given
  notice` -- a dispensation where damages are claimed is outside the power and the duty stands (`JUST TRUE`) -- the
  Court's order stands until set aside.
- **F9** s 178(3)(c) "6 months or more after the day" -- `Does the claim day give six months` -- the same day of the
  month six months on, or that month's last day where it is shorter -- the day after that (Interpretation Act 1987 not
  deposited).
- **F10** s 179(b) "binds all such persons" -- `Will the judgment bind me` -- a person the judgment does not identify is
  `NOTHING` (left to the general law) -- `JUST FALSE`, reading the list as closed.
- **F11** s 180(3) "within a further 21 days" -- `The last day for my appeal for the group`, `Can I appeal for the group`
  -- the 21 days run from the day after the last day of the ordinary appeal time; an appeal by another member on or
  before that last day is "not yet" -- the 21 days run from the judgment, or another member may appeal at any time once
  the representative party has said it will not.
- **F12** s 182(3) "immediately before the commencement ... was barred by the expiration of that period" -- `Is my
  limitation period suspended`, `My last day now` -- a period whose last day is the day the class action started was not
  expired, and is suspended with 0 days left -- it was barred.
- **F13** s 182(1), (2) "suspended", "begin to run again" -- `My last day now` -- the days from the start of the class
  action to the old last day are added to the day the period resumes, which is the earlier of the opt-out and the final
  determination -- the period resumes on the day after; or the opt-out runs from the date fixed for opting out, not the
  day the notice was given.

## What the Act turns out to say

1. **s 181 relies on s 168 for costs, but s 168 says nothing about costs.** Only s 169(2) makes a group member liable
   for costs. The cross-reference to s 168 adds nothing on its words (fork F7). Asserted: a group member not permitted to
   appear under s 169 has no costs exposure.
2. **s 182 does not say when an opted-out member's period resumes, or what happens if the class action is stopped
   under ss 164-166.** "Opts out ... under section 162" could be the day the notice is given or the date fixed. And an
   order that proceedings "no longer continue under this Part" is not a determination "without finally disposing of the
   group member's claim", so on the words a member's period stays suspended after such an order (the encoding asks the
   person to answer "decided without finally disposing" only for a determination). Forks F13; the s 164-166 gap is not
   asserted.
3. **s 182 does not say how the suspended time is counted.** "Suspended" read as stopping the clock with the remainder
   kept (fork F13); asserted, including a remainder that crosses 29 February 2028.
4. **s 180(3) does not say from when the further 21 days run.** Read as after the ordinary appeal time ends (fork F11).
   Asserted on the 21st and 22nd days.
5. **s 175(2) dispensation is narrow.** Notice of the start of the class action, of a want-of-prosecution application,
   and of the representative party's withdrawal can be dispensed with only where no damages are claimed; most class
   actions claim damages, so in them the notices cannot be dispensed with. Asserted (fork F8).
6. **s 162 fixes no minimum opt-out period.** The Court must fix a date, and the hearing cannot start before it without
   leave (s 162(4)), but the Part sets no length; the s 175(6) notice must be "as soon as practicable". Nothing to assert.
7. **s 163(2)(b)'s "with the consent of the person"** only makes sense for the persons in s 159(2) who join only with
   written consent; the encoding folds it into one input ("would have been in the group, with your consent where it is
   needed").
8. **No provision on litigation funding commissions or contingency fees for group costs** appears in this version of
   Part 10 (s 166(2)(b) mentions "a litigation funding arrangement" only to say it does not make a class action
   inappropriate). Whether later amendments added any is not known from the deposited text.
9. **Parts 1-9 and the 2.5% deduction under s 18A** affect a group member's money in a fund (the note to s 178) but are
   outside this baseline.

## Questions (exported)

`cpa-p10.l4` (27), in the Act's order: `Can I start a class action` (ss 157, 158); `Am I a group member` (ss 155, 159);
`Do I need a tutor to be a group member` (s 160(1)); `Can I take a step without my tutor` (s 160(2)); `The last day to
opt out` (s 162); `Have I opted out in time` (s 162, rule); `Can the hearing start then` (s 162(4)); `Can the group be
widened to include me` (s 163); `Could the class action be stopped` (ss 164-166); `What can I do after the class action
ends` (s 167); `Can I be made to pay costs` (ss 169, 181); `Can the Court replace our representative` (s 171); `Can my
award be stayed` (s 172); `Can the settlement be decided now` (ss 173, 175(4)); `Can it be settled` (s 173(1)); `Can our
representative withdraw` (s 174(4)); `Must I be given notice` (s 175); `Does missing a notice undo anything` (s 176(8));
`Can damages be awarded in aggregate` (s 177(3)); `Does the claim day give six months` (s 178(3)(c)); `Is my fund claim
in time` (s 178(3), (4), rule); `Will the judgment bind me` (s 179); `The last day for my appeal for the group`
(s 180(3)); `Can I appeal for the group` (s 180(3), rule); `Is my limitation period suspended` (s 182); `My last day now`
(s 182); `The most the representative can be reimbursed` (s 184).

The s 182 group arises only for a group member who has a limitation period of their own; the s 167 group only once the
Court has ordered that the class action not continue; the s 180(3) group only after judgment; the s 178 group only
where the Court has set up a fund.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation and
  whether Part 10 has been amended since 1 July 2024.
- Deposit the Uniform Civil Procedure Rules 2005 (opt-out notices, appeal times) and the Limitation Act 1969, and replace
  the date inputs where they settle them.
- Have a lawyer review the forks, especially F11 and F13 (the counting of the appeal and limitation periods) and F7
  (costs).
- A defendant seat, an independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
