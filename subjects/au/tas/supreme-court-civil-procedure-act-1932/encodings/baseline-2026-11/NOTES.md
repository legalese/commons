# Supreme Court Civil Procedure Act 1932 (Tas), Part VII -- baseline encoding, the person with a claim in a class action

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is Part VII (representative proceedings,
inserted by No. 14 of 2019 from 9 September 2019), as one of the instruments behind class actions in claims work. Part VII is
small enough to take whole. The rules are in one module (`rp-rules.l4`), the dates in another (`rp-dates.l4`, built-in date
functions only, no daydate), and the questions in one seat module that imports the rules and never restates one
(`rp-seat.l4`). The cases are in `rp-cases.l4`.

## Edition

- **Act:** Supreme Court Civil Procedure Act 1932 (Tas), No. 58 of 1932, the consolidated version published 1 October 2025
  and current on Tasmanian Legislation Online on 6 November 2026, deposited at
  `../../registers/source-bundle/act-1932-058.txt` (text sha256 2feabc52...79bff4ec per its `.meta.json`), converted from
  the site's whole-document HTML. Not checked against the authorised version.
- **Numbers set elsewhere:** none of Part VII's numbers is delegated. The time allowed for the representative party to
  appeal (s 89(3), through s 40 and the Rules of Court) and the member's own limitation period (s 89B, the Limitation Act
  1974) are set elsewhere and asked as dates. Neither instrument is deposited here.
- **Commencement:** Part VII applies to proceedings commenced after 9 September 2019 (s 65 and the history note).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as an error, "assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `rp-dates.l4` | 0 | 0 | 0 | 0 |
| `rp-rules.l4` | 0 | 0 | 0 | 0 |
| `rp-seat.l4` | 0 | 0 | 0 | 0 |
| `rp-cases.l4` | 0 | 0 | 157 | 157 |

Every exported question has cases, with the edges: a proceeding commenced on 9 September 2019 and the day before; 6 and 7
persons; an opt-out notice on the day before the date fixed, on the date fixed, on the day of commencement, and before an
extended date of 1 March 2028 (last day 29 February); a hearing on the opt-out date and the day before, with and without
leave; a cause of action accruing on the day of commencement, the next day, the day before the cut-off and on it; every
s 75 ground including the s 75(2) "merely because" case; the earliest fund claim day for orders on 15 January, 31 August
2026, 31 August 2027 (29 February 2028) and 1 September 2027; a fund claim on the order day, the claim day and the day
after; a group appeal on the representative party's last day, the first and last days of the further 21 days, and the day
after; the further period across a year end and across 29 February 2028; a limitation period ending the day before the
class action began (barred) and on that day (0 days left); 92 days carried across 29 February 2028; every constructor of
every choice.

**No mirror cases.** There is one seat.

## Seat

**The person with a claim** (`rp-seat.l4`): an individual with a claim against a defendant who either brings the class
action (the representative party) or is one of the group on whose behalf it is brought (a group member, or a sub-group
member). "Does the class action law apply?", "Can I start a class action?", "Can I carry on after my own claim ends?", "Am
I in the group without agreeing?", "Who takes steps for me if I am under a legal incapacity?", "By when can I opt out, and
have I?", "Can the hearing start before the opt-out date?", "Can I be added though my claim arose later?", "Can the Court
stop the class action, and what then?", "Can I be made to pay costs?", "Can my excess costs come out of the damages?",
"Can the representative party be replaced?", "Can I settle or withdraw as representative party?", "Can it be settled?",
"Must I be told?", "Does a missed notice undo anything?", "Can my award be stayed?", "Can damages be a lump sum?", "When is
the fund claim day, and is my claim in time?", "Am I bound by the judgment?", "Can I appeal for the group, and by when?",
"Is my limitation period running, and by when must I sue on my own?".

No seat for the Supreme Court. Its satisfactions, conclusions, leave, orders, approvals and directions are asked as facts.
The defendant is a party the Part puts duties on (notice, fund payments) and could have a further seat; it is not written
here (the brief's seat is the claimant).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; Part VII delegates no number. The Rules of Court
  (appeal time) and the Limitation Act 1974 are borrowed and asked as dates.
- **The actors the text names.** Followed: the representative party, group members, sub-group members and the sub-group
  representative party, the defendant, the substitute decision-maker, the Court.
- **Judgments answered conditionally.** Followed: "appears to the Court" (ss 73, 80), "concludes" (s 74), "satisfied"
  (ss 75, 82(3), 83(4), 89D), "just" (s 87(4)), "reasonably accurate assessment" (s 86(3)), "same, similar or related
  circumstances" and "substantial common question" (s 66(1)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "proceedings", "group member" (with s 68) and
  "substitute decision-maker" are worked out; standing, legal incapacity, accrual of a cause of action and the limitation
  period are asked.
- **One case.** One class action, seen by one person with a claim in it.
- **The Act's terms with plain glosses.** Followed, in the `@export` and `@desc` text ("representative proceeding (class
  action)", "stay of execution (hold back)").
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** the whole of Part VII except what is listed below as out: ss 64, 65 (application); s 66(1) with s 67(1)
(commencement and standing; s 66(2) noted, as it removes bars rather than adding conditions); s 67(3); s 68; s 69; s 70(1)(a),
(2) (only as the group description that s 68 relies on); s 71 (opting out, with s 71(2) as a regulative rule, and s 71(4));
s 72(1), (2); ss 73, 74, 75(1), (2), 76; ss 78(2), 89A (costs); ss 80, 83(3) (substitution); s 81 (stay); s 82(1), (3); s 83(1),
(2), (4); s 84(1)-(4); s 85(8); s 86(1)(f), (3); s 87(3)(c), (4) (with s 87(3)(c) as a regulative rule); s 88; s 89(3) (as a
two-step regulative rule); s 89B; s 89D(1), (2).

**Regulative rules:** three, each run by EVALTRACE inside an exported question that takes only dates and facts:
- s 71(2): the group member DOes give written notice WITHIN the days from commencement to the day before the date fixed,
  LEST BREACH (the "breach" is the loss of the right to opt out, not a wrong).
- s 87(3)(c): the group member DOes claim on the fund WITHIN the days from the order to the claim day, LEST BREACH (a late
  claim only with the Court's allowance under s 87(4)).
- s 89(3): the representative party DOes appeal WITHIN the time allowed, HENCE FULFILLED, LEST another member DOes appeal
  WITHIN the further 21 days, LEST BREACH.

**Out, and why:**
- s 66(2), s 67(2), s 70(1)(b)-(d): what a class action may claim and what the originating process must say; they impose no
  condition on the person with a claim beyond those encoded (s 67(2) is finding 4).
- s 71(1), (3), s 72(3), (4): the Court's powers to fix and extend dates; the dates are inputs.
- s 74's alternative stay of money relief, s 75(3), (4) (no further application by the defendant), s 77, s 78(1), s 79, s 80
  as to "other orders", s 82(2), s 85(1)-(7), s 86(1)(a)-(e), (2), (4), (5), s 87(1), (2), (3)(a), (b), (d), (5), s 89(1),
  (2), (4), (6), s 89C, s 89D(3): the Court's powers and the form of notices, orders and judgments; nothing in them is a
  test the person with a claim can apply to their own facts. s 85(5) (personal notice only if practicable and not unduly
  expensive) is a candidate for a later pass.
- s 89(5) (Part VII, other than s 71, applies to appeals): noted in finding 6; not encoded.
- s 84(5) "as soon as practicable": no fixed period, so not a regulative rule.
- The rest of the Act (Parts I-VI, VIII-XIV): outside the focus. The Act's other claims machinery (s 11 rules of law,
  Part IV trial, Part V appeals and the s 40 time for appeal) is not encoded; the appeal time is an input.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 65 -- `ss 64, 65 -- Part VII applies to the proceeding` -- a proceeding commenced on 9 September 2019, the day
  s 65 applied from, is "after the commencement" -- only proceedings commenced from 10 September 2019.
- **F2** s 66(1)(a) -- `ss 66(1), 67(1) -- I may commence a representative proceeding` -- the "7 or more persons" include the
  person commencing -- 7 others besides them.
- **F3** ss 64, 70 -- `ss 64, 68 -- I am a group member` -- a person outside the group as the originating process describes
  it is not a group member: JUST FALSE (the "means" definition) -- NOTHING (the description can be amended, s 72).
- **F4** s 72(2)(a) -- `s 72 -- the group may be altered to include me` -- a cause of action accruing on the day of
  commencement did not accrue "after" it: NOTHING -- it did (the proceeding began part way through the day).
- **F5** s 72(1) -- same function -- within s 72(2) but without leave: JUST FALSE (the description is altered only by an
  amendment with leave) -- NOTHING (a grant limited by its own wording).
- **F6** ss 73-75 -- `ss 73-75 -- the Court may order that the proceeding no longer continue as a class action` -- no route
  under ss 73-75: JUST FALSE -- NOTHING, because s 89C's general power to make "any order that the Court thinks appropriate
  or necessary to ensure that justice is done" might be read as a further route.
- **F7** ss 77, 89A -- `ss 78(2), 89A -- costs may be awarded against me` -- costs connected with a sub-group under s 77:
  NOTHING -- JUST TRUE (s 89A treats s 77 as authorising costs) or JUST FALSE (s 77 authorises none). Finding 3.
- **F8** s 83(1), (2) -- `s 83 -- I may do this as representative party` -- settling or withdrawing without leave: NOTHING (a
  grant limited by its own wording) -- JUST FALSE ("with the leave of the Court" as a condition).
- **F9** s 87(3)(c) and `rp-dates.l4` -- `s 87(3)(c) -- the earliest claim day the Court may specify` -- "not earlier than 6
  months after the day" allows the day exactly six calendar months later, the order day excluded, and where that month is
  shorter its last day -- the day after that.
- **F10** s 84(2) -- `s 84 -- notice of the matter must be given to group members` -- a dispensation where damages are
  claimed is not one s 84(2) allows, so notice is still due: JUST TRUE -- the Court's order stands until set aside.
- **F11** s 86(3) "Subject to section 82" -- `s 86(3) -- the Court may award aggregate damages` -- an aggregate award that
  gives effect to an approved settlement is free of the "reasonably accurate assessment" bar: JUST TRUE -- the words only
  preserve the Court's s 82 powers and the bar still applies.
- **F12** s 89(3) -- `s 89(3) -- the group's appeal` -- the "further 21-day period" begins the day after the representative
  party's time ends and ends 21 days after that last day; an appeal by a member before the representative party's time ends
  is not an s 89(3) appeal -- the period may run from the judgment, or overlap.
- **F13** s 89B(1), (3) -- `s 89B -- my limitation period`, `s 89B -- the last day to start my own proceeding` -- "suspended"
  stops the clock: the days from the day the class action was commenced to the original last day are added to the day the
  period runs again; a claim whose last day is the day of commencement was not "barred ... immediately before" it (0 days
  left) -- the day of commencement or of resumption counted differently (a day more or less).
- **F14** s 89B(2)(a) -- `s 89B -- the last day to start my own proceeding` -- the period runs again from the day the written
  opt-out notice is given -- from the date fixed under s 71(1) (the member is in the group until then).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 64 ("proceedings", "group member"), the "if" conditions of ss 66(1), 73, 74,
75(1), 80, 81, 83(3), 84(3), 89D(1), (2), "unless" in ss 68(2), 82(3), 86(3), "may not ... without" in s 82(1), "must not ...
except" in s 71(4), "until" in s 81, "other than" in ss 88, 89A, "is not inappropriate ... merely because" in s 75(2), "does
not affect" in s 85(8), the s 83(4) preconditions and the periods of ss 71(2), 87(3)(c), 89(3) give `JUST FALSE` or the
deadline; the sites listed under the fork register, and ss 65, 67(3), 72, 78/89A for the representative party, 84(4), 88
for a member not affected, and 89D(1) for a non-representative, give `NOTHING`.

## What the Act turns out to say

1. **The history notes in the deposited text mix two Part VIIs.** Most Part VII sections carry, besides "Inserted by No. 14
   of 2019, s. 10, Applied:09 Sep 2019", notes of amendments and repeals from 1934 to 2001 (for example s 74 "Repealed by
   No. 54 of 2000, Sched. 4, Applied:01 Dec 2001"; s 64 "Repealed by No. 14 of 1993"). These belong to the sections of the
   same numbers before 2019 (the old Part VII was repealed in 2001). They do not change the operative text, but a reader of
   the notes alone would think some sections repealed. Whether the site or the conversion put them there was not checked.
2. **An order that the proceeding no longer continue as a class action is not an s 89B(2) event.** s 89B(2) lets the
   limitation period run again only on opting out, discontinuance, or a determination that does not finally dispose of the
   member's claim. After an order under ss 73-75, the proceeding continues for the representative party (s 76(1)(a)), so it
   is arguably not "discontinued", and a group member who is not joined under s 76(1)(b) is left without a stated restart.
   Encoded as the Act not saying (NOTHING). Asserted.
3. **s 89A points to costs "authorised by section 77", but s 77 says nothing about costs.** Only s 78(2) makes a group
   member liable for costs. Encoded as NOTHING for sub-group costs (fork F7). Asserted.
4. **s 66(1)(a) and s 67(2) pull apart on "the same person".** s 66(1)(a) needs 7 or more persons with claims "against the
   same person"; s 67(2) allows a class action against several defendants "whether or not the person and each of those
   persons have a claim against every defendant". The encoding asks for the number with claims against the same defendant.
5. **"Before the date" and "not earlier than the date".** s 71(2) needs the opt-out notice "before" the date fixed, and
   s 71(4) lets the hearing begin on that date, so there is no day on which a member may still opt out and the hearing has
   begun. Asserted (29 and 30 June 2027).
6. **No opt-out on appeal.** s 89(5) applies Part VII to appeal proceedings "other than section 71", so a group member
   cannot opt out of a group appeal; not encoded, noted for a later pass.
7. **The further 21-day period of s 89(3) has no stated start.** Read as following the end of the representative party's
   time (fork F12).

## Before this is worth relying on

- Check the conversion against the authorised version on the site, and the history notes (finding 1).
- The Supreme Court Rules 2000 (Tas) (time for appeal, notices), the Limitation Act 1974 (Tas) (limitation periods) and the
  Acts Interpretation Act 1931 (Tas) (counting time), none deposited here.
- A lawyer's view on findings 2, 3 and 4 and forks F6, F9, F12, F13 and F14; an independent test pass and a human gate.
- A defendant's seat, if wanted.
