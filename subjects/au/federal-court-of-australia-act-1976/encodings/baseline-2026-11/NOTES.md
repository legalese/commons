# Federal Court of Australia Act 1976 (Cth), Part IVA -- baseline encoding, the claimant in a class action

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus asked for is Part IVA (representative
proceedings, called class actions here), the provisions a claimant meets. Part IVA is small enough to take whole: every
section of Divisions 1 to 6 is either encoded or listed below as out, with the reason. Section 43(1A), which sits in Part
VI but shields group members from costs, is brought in with it.

Modules:
- `fca4a-dates.l4` -- the date arithmetic, the only module that imports `daydate`;
- `fca4a-rules.l4` -- the rules, by section, and the one regulative rule;
- `fca4a-seat.l4` -- the claimant's questions, each `@export` with `@desc` inputs, importing the rules and restating none;
- `fca4a-cases.l4` -- the cases.

## Edition

- **Act:** Federal Court of Australia Act 1976, Compilation No. 59 (compilation date 11 December 2024, register id
  C2024C00819), deposited at `../../registers/source-bundle/C2004A01586.txt`, a plain-text conversion of the Word file
  from the Federal Register of Legislation, retrieved 13 October 2026. Part IVA was inserted by the Federal Court of
  Australia Amendment Act 1991 (No. 181, 1991) and, by the endnotes, is unamended since except s 33ZH (substituted by
  No. 103, 2010). Amendments after 11 December 2024 are not in the text.
- **Rules that set its numbers and forms:** Federal Court Rules 2011, Compilation No. 11 (11 June 2026, register id
  F2026C00512), deposited in `subjects/au/federal-court-rules-2011/registers/source-bundle/F2011L01551.txt` (retrieved
  6 November 2026). Used: r 1.61(2), (5) (counting time), r 9.33 (Form 20 consent), r 9.34 (Form 21 opt-out notice) and
  r 36.03 (28 days to appeal). The l4 cannot import across subjects, so these are hand-worked into the rules here, with
  the rule number; the Rules have no encoding of their own yet.
- **Not deposited and not applied:** the Acts Interpretation Act 1901 (s 36, reckoning of time, and s 2G, months), and
  the limitation laws whose periods s 33ZE suspends (the old last day is an input).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, at most two
processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two deliberately wrong
assertions were run once in a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `fca4a-dates.l4` | 0 | 0 | 0 | 0 |
| `fca4a-rules.l4` | 0 | 0 | 0 | 0 |
| `fca4a-seat.l4` | 0 | 0 | 0 | 0 |
| `fca4a-cases.l4` | 0 | 0 | 142 | 142 |

The cases file also runs one `#TRACE` of the s 33ZA(3)(c) duty (a claim on day 212 of 212: FULFILLED). Every exported
question has cases, with the edges: a cause arising on and the day before 4 March 1992; 6 and 7 claimants; each s 33C
limb and s 33G; each kind of person in s 33E(2) with and without consent; opt-out notices the day before, on and after
the opt-out date, unwritten, and in an appeal; a hearing on and the day before the opt-out date; claims accruing on the
commencement day, the day after, the day before and on the Court's cut-off; s 33ZE with each outcome, an expired period,
and a class action begun on the last day; every notice subject with dispensing, damages and orders; 6 and 7 likely group
members and each s 33M limb; every cell of the costs matrix; s 33ZJ at, under and just over the damages; the fund claim
day on, after and one day late, with and without s 33ZA(4); six months from 31 August in a common and a leap year; the
appeal window across the Christmas break and its first and last days.

## Seat

**The claimant in a class action** (`fca4a-seat.l4`): a group member, or a person with a claim who starts and runs the
class action as representative party (or sub-group representative). "Can my claim be brought in a class action?", "Can I
start the class action as representative party?", "Can I keep running the class action without a claim of my own?", "Am
I a group member?", "Must I consent to be a group member?", "Do I need a next friend or committee?", "Can I opt out of
the class action?", "By when must I opt out?", "Can the hearing start before my opt-out date?", "Will the judgment bind
me?", "Can the group be widened to include my later claim?", "What happens to my time limit?", "Must I be given notice
of this?", "Does missing a notice affect the class action?", "Can the representative party be replaced?", "Can the
representative party withdraw?", "Can the class action be stopped?", "Can I go on with my own claim after the class
action stops?", "Can I be ordered to pay costs?", "How much of the damages can go to the representative's costs?", "Can
the class action be settled?", "Can damages be awarded as a lump sum?", "Can my award be held back?", "What is the
earliest fund claim day?", "Can I claim from the fund?", "Am I a party for consumer law compensation orders?", "By when
can I appeal for the group?", "Can I appeal for the group?" (28 questions).

No seat for the Court. No respondent seat was written; one would ask several of the same rules (ss 33M, 33N, 33U,
33ZA(5)) from the other side.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Federal Court Rules 2011 supply the
  28-day appeal period, the counting rule and the forms. The limitation laws are not brought in; the old last day is
  asked.
- **The actors the text names.** Followed: group member, representative party, sub-group member, sub-group
  representative party, respondent, the Court.
- **Judgments answered conditionally.** Followed: a substantial common issue (s 33C(1)(c)), the Court's view of the
  likely number of group members (s 33L), excessive distribution cost (s 33M), the interests of justice (s 33N),
  adequacy of representation (s 33T), notice in sufficient time (s 33W(4)), "just" (ss 33X(4), 33ZA(4)), a reasonably
  accurate assessment (s 33Z(3)), and reasonable and recoverable costs (s 33ZJ) are inputs worded "if the Court ...". A
  yes about a power of the Court means it can act, not that it will.
- **The Act's definitions worked out; borrowed terms asked.** Followed: group member (s 33A with s 33E), representative
  proceeding (s 33C) are worked out; "sufficient interest", "under disability", "limitation period", "cross-vesting"
  jurisdiction and "want of prosecution" are asked.
- **One case.** One class action and one claimant in it.
- **The Act's terms with plain glosses.** Followed: "class action" glosses "representative proceeding"; "time limit"
  glosses "limitation period"; "litigation representative" glosses "next friend or committee".
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 33A, 33B, 33C(1) (with (2) noted: the kind of relief makes no difference, so it is not asked), 33D, 33E, 33F,
33G, 33J, 33K(1)-(3), 33L, 33M, 33N(1), 33P, 33Q(3), 33R(2), 33T, 33U, 33V(1), 33W(4), 33X(1)-(6), 33Y(8), 33Z(1)(f),
(3), 33ZA(3)(c), (4), 33ZB, 33ZC(6), (8), 33ZE, 33ZH, 33ZJ(1), (2); s 43(1A); Federal Court Rules 2011 rr 1.61(2), (5),
9.33, 9.34, 36.03.

**Regulative rule:** one. s 33ZA(3)(c), "on or before which the group members are to make a claim for payment out of
the fund", as `MUST ... WITHIN` the days from the fund order to the claim day, `LEST BREACH ... BECAUSE` naming s 33ZA(4);
run by EVALTRACE inside "Can I claim from the fund?", which takes only plain dates. The opt-out (s 33J(2)) and the
group member's appeal (s 33ZC(6)) are permissions with periods; a `MAY` never breaches, so they are computed as dates and
periods rather than run as traces.

**Out, and why:**
- s 33H (contents of the originating application), s 33Y(1)-(7) (form, who gives notice, means): the representative
  party's and the Court's drafting; the claimant meets their result in s 33X.
- s 33J(1), (3), s 33K(4): the Court fixing and extending dates; the dates are inputs.
- s 33N(2), (3) (no further application by the respondent): the respondent's side.
- s 33Q(1), (2), s 33R(1), s 33S (directions, sub-groups, separate proceedings): the Court's case management; the costs
  consequences in ss 33Q(3) and 33R(2) are in.
- s 33V(2), s 33Z(1)(a)-(e), (g), (2), (4), s 33ZA(1), (2), (3)(a), (b), (d), (5): the Court's powers over judgment and
  distribution; what the claimant meets (the lump sum bar, the claim day, late claims) is in.
- s 33W(1)-(3), (5): the representative's own settlement and leave; the preconditions in (4) are in.
- s 33ZC(1)-(5), (7), (9), s 33ZD: who the parties to an appeal are, and the High Court; the group member's own appeal
  right in (6) and the no-opt-out rule in (8) are in.
- s 33ZF, s 33ZG: the general power and the saving of other powers and laws; nothing to compute. s 33ZG(b) is noted in
  the stopping question (other powers to dismiss are not answered).
- s 43 other than (1A): costs in general.
- r 36.05 (extension of time to appeal) and r 1.61(3), (4) (short periods; weekends): an extension is the Court's; the
  28-day period is over 5 days, and whether filing "may only be done on a business day" (r 1.61(4)(b)) is not settled by
  the Rules deposited.
- Litigation funding, common fund orders and contingency fees: the Act says nothing about them; they are case law.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: s 33B "may only"; s 33C(1) "where" (a)-(c); s 33G "may not"; s 33A "means"; s 33E(2) "unless";
  s 33F(1) "not necessary"; s 33J(2) outside the period, s 33ZC(8) "does not apply"; s 33J(4) "must not"; ss 33L, 33M,
  33N "if"/"where"; s 33P "where"; s 43(1A) "may not ... except", and "and not the representative party" (ss 33Q(3),
  33R(2)); s 33T "if"; s 33W(4) "before granting ... must be satisfied"; s 33U "where"; s 33V(1) "may not"; s 33X(3)
  "if"; s 33X(4) "unless ... must not"; s 33Y(8) "does not affect"; s 33Z(3) "not ... unless"; s 33ZA(4) "if"; s 33ZB
  "other than"; s 33ZC(6) "if" and its period; s 33D(2) "where".
- `NOTHING`: s 33D(1) without a sufficient interest (silent); s 33F for a person not under disability (scope); s 33J(2)
  with an unwritten notice (grant's wording); s 33K outside (a) or (b) (grant's wording); s 33X(5) without an order
  (silent); s 33Z(3) under a settlement (silent); s 33ZB for a person the judgment does not describe (scope); a
  sub-group representative's other costs (silent); s 33ZH for a non-member (scope).

### Forks

- **F1** s 33B, `s 33B -- the cause of action arose after the 1991 commencement`: a cause arising on 4 March 1992 (the
  commencement day) arose "after the commencement" (JUST TRUE), since an Act commences at the start of its day; other
  reading: only from 5 March 1992.
- **F2** s 33D(2), `s 33D(2) -- I keep my standing without a claim`: a person who did not commence it answers JUST FALSE
  (the "where" fails); other reading: NOTHING (a substituted representative under s 33T or s 33W(3) may have the same
  interest on another footing).
- **F3** s 33J(2), `s 33J(2) -- I can opt out`: a notice in time but not written in Form 21 answers NOTHING (outside the
  grant's wording; the Court may accept a defective notice); other reading: JUST FALSE ("by written notice").
- **F4** s 33K, `s 33K -- the group can be altered to include me`: a claim accruing on the commencement day, or on or
  after the Court's cut-off, answers NOTHING; other reading: JUST FALSE ("after", "before" as periods under ruling (a)).
- **F5** s 43(1A) with s 33Q(3), `s 43(1A) -- costs can be awarded against me`: a sub-group representative's exposure
  to the group's general costs and another member's issue answers NOTHING; other reading: JUST TRUE (as a party
  "representing" others they fall under s 43(1)).
- **F6** s 33Q(3), same function: the representative party is never liable for sub-group issue costs; the text says so
  only "Where the Court appoints a person other than the representative party", so if the representative party is
  itself appointed sub-group representative it is liable; that case is not offered.
- **F7** s 33Z(3), `s 33Z(3) -- damages can be awarded as a lump sum`: under a settlement, NOTHING ("Subject to section
  33V" lifts the bar and says no more); other reading: JUST TRUE.
- **F8** s 33X(4), `s 33X -- I must be given notice`: the bar on deciding a settlement without notice is read as a duty
  to give notice unless the Court is satisfied; other reading: no duty, only a bar on deciding (NOTHING).
- **F9** s 33ZA(3)(c), `s 33ZA(3)(c) -- the earliest claim day`: "6 months ... after" a day that the sixth month lacks
  (31 August) is the last day of that month (daydate's `add months`); other reading: the first day of the next month.
- **F10** s 33ZB(b) "other than", `s 33ZB -- the judgment binds me`: an opted-out person answers JUST FALSE ("(other
  than X)" has no ruled convention); other reading: NOTHING.
- **F11** s 33ZJ(2), `s 33ZJ -- the most paid to the representative out of the damages`: the most is the excess, capped
  at the damages awarded; the text does not state the cap, but money must come "out of the damages awarded".
- **F12** r 36.03, `r 36.03 -- the representative's last day to appeal`: where the Court fixed a date, the later of that
  date and the 28 days ("(a) ... or (b)"); other reading: the fixed date replaces the 28 days.
- **F13** s 33ZC(6), `s 33ZC(6) -- my last day to appeal for the group`: the further 21 days are calendar days counted
  from the day after the representative's last day, the Christmas days included and no weekend roll-over; other
  reading: Acts Interpretation Act s 36(2) moves a last day falling on a weekend or holiday (not deposited).
- **F14** s 33ZE, `s 33ZE -- my limitation period`: the days left are counted from the day after the class action began
  to the old last day, and added to the day the period runs again; a class action begun on the old last day leaves that
  later day only; other reading: the day of commencement counts as a day left, adding one day.

## What the Act turns out to say

1. **The opt-out date itself is too late.** s 33J(2) requires notice "before the date so fixed", so the last day to opt
   out is the day before the date in the notice. A group member reading "opt out by 30 June" may miss it. Asserted.
2. **The 1991 commencement date is only in the endnotes.** s 33B ties Part IVA to causes of action "arising after the
   commencement of the Federal Court of Australia Amendment Act 1991"; the text gives no date, and the endnote table gives
   4 March 1992. Asserted.
3. **s 33ZE suspends but does not revive.** It suspends "the running of" a limitation period on commencement; a period
   that had already run out is not running and is not revived. It also does not say how the remaining days are counted
   (fork F14). Asserted.
4. **A group member's appeal window can fall wholly inside the Christmas break.** The representative's 28 days exclude
   24 December to 14 January (r 1.61(5), which governs periods "fixed by these Rules or by an order"), but the group
   member's "further 21 days" are fixed by the Act, so r 1.61(5) does not reach them. Judgment on 20 November 2025 gives
   the representative until 18 December 2025 and the group member 19 December 2025 to 8 January 2026. Asserted.
5. **Costs protection for group members is outside Part IVA.** s 43(1A) bars costs against a person on whose behalf the
   class action is brought, except under ss 33Q and 33R; Part IVA itself only says who "is liable" in those two cases.
   It is silent on a sub-group representative's share of the general costs (fork F5). Asserted.
6. **s 33X(4) is a bar, not a duty.** It says a settlement approval "must not be determined unless notice has been
   given", unlike s 33X(1), which says notice "must be given" (fork F8). And s 33X(1)(a) speaks of the date "fixed under
   subsection 33J(1)", not a date extended under s 33J(3), so notice of an extension rests on s 33X(5).
7. **No opt-out from an appeal, though the time limit stays suspended through it.** s 33ZC(8) disapplies s 33J to an
   appeal proceeding; s 33ZE(2) keeps the limitation period suspended until "any appeals" are determined. Asserted.
8. **s 33K(2)(b) lacks a comma.** "who would have been included in the group, or, with the consent of the person would
   have been included in the group" reads more easily with a comma after "person"; the encoding asks one question
   ("with your consent, where needed").

## Before relying on it

- Check for amendments after 11 December 2024 (a later compilation of the Act).
- Deposit the Acts Interpretation Act 1901 and settle forks F9, F13 and F14 against ss 2G and 36.
- Encode the Federal Court Rules 2011 Division 9.3 and Part 36 as their own encoding, and link this one to them.
- An independent test pass and a human gate; a lawyer's view on forks F3, F5, F8 and F12.
- A respondent seat (ss 33M, 33N, 33U, 33ZA(5)).
