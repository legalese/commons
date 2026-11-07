# Rules of the Supreme Court 1971 (WA) -- baseline encoding, the plaintiff bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Rules; nothing existing was touched. The Rules are large (about 90 Orders, a million
characters), so the whole instrument is not taken: the encoding takes the Orders a person bringing a claim meets on the
way from writ to judgment or settlement, chosen with personal injury and other damages claims in mind, and lists the
rest below as out, with the reason. (The class-action baseline of the Civil Procedure (Representative Proceedings) Act
2022 already hand-works O. 18A; it is not repeated here.)

Modules:
- `rsc-dates.l4` -- the date arithmetic: O. 3 (reckoning days, the 24 December to 15 January exclusion, closed days),
  calendar months (O. 3 r. 1) and O. 68 r. 5 (the days the Central Office is closed, with Easter computed); the only
  module that imports `daydate`;
- `rsc-rules.l4` -- the rules, by Order and rule, and three regulative rules;
- `rsc-seat.l4` -- the plaintiff's questions, each `@export` with `@desc` inputs, importing the rules and restating none;
- `rsc-cases.l4` -- the cases.

## Edition

Rules of the Supreme Court 1971 (WA), made under the Supreme Court Act 1935, consolidated version 09-am0-00 (currency
from 11 December 2025), deposited at `../../registers/source-bundle/mrdoc_49048.txt`, a plain-text conversion of the
Word file from the Western Australian Legislation website (mrdoc 49048), retrieved 6 November 2026. Amendments after
retrieval are not in the text. No other instrument was needed to set a number the encoded rules use; where a rule
points elsewhere (the Service and Execution of Process Act 1992 (Cth) for interstate service, O. 5 r. 11(2); "Public
Service holidays", O. 68 r. 5) the answer is NOTHING or the gap is a fork.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, at most two
processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a deliberately wrong
assertion was run once to confirm a failure is reported).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `rsc-dates.l4` | 0 | 0 | 0 | 0 |
| `rsc-rules.l4` | 0 | 0 | 0 | 0 |
| `rsc-seat.l4` | 0 | 0 | 0 | 0 |
| `rsc-cases.l4` | 0 | 0 | 195 | 195 |

The cases file also runs three `#TRACE`s (the statement of claim served on day 14 of 14, the offer acknowledged on day
3 of 3, the sum paid on day 28 of 28: each FULFILLED). Every exported question has cases, with the edges: a last day on
a weekend, on Good Friday and over Easter, on Christmas Day; a pleading period straddling 24 December to 15 January and
one ending on 23 December; 6 days against 7 days under O. 3 r. 2(2); 299/300 and 599/600 km from Perth; a writ issued on
29 February; the extension application on the expiry day and the day after; the strike-out direction on the last day of
the 6 months and the day after, with the hearing 6 and 7 days after the direction; default judgment on the last day to appear and the day after; each kind of claim under
O. 13; offers accepted on the 28th and 29th day, with a stated time below the 28-day floor; payment on day 28 and 29;
a judgment equal to the offer, one dollar over, with post-offer interest taken out, and a claim lost (no judgment); every costs outcome of r. 10;
service proved by indorsement and affidavit, by the solicitor accepting, and through foreign officials (O. 10
Division 4, no indorsement needed); every security ground; every person under disability; inactivity periods across month ends and a leap year.

## Seat

**The plaintiff** (`rsc-seat.l4`): the person bringing a claim in the Supreme Court of Western Australia by writ (for
example a claim for damages for personal injury), including, through O. 70, a child or other person under disability
suing by a next friend. Questions: "What is the last day of my period?", "Must I give notice of intention to proceed?",
"What is the earliest day I can proceed after my notice?", "How many days must my writ give to appear?", "Until when is
my writ valid for service?", "Can the Court extend my writ?", "What is the latest day one extension can reach?", "Can my
unserved writ be struck out?", "By when must service be indorsed on the writ?", "What is the last day for the defendant
to appear?", "What default judgment can I enter?", "By when must I serve my statement of claim?", "Did I serve my
statement of claim in time?", "By when must the defendant serve a defence?", "By when must I serve my reply?", "When do
the pleadings close?", "By when can I apply for summary judgment without leave?", "By when must I acknowledge the
offer?", "Did I acknowledge the offer in time?", "Can I accept the offer?", "Was the accepted offer paid in time?", "Can
I withdraw my acceptance?", "What costs follow the offer?", "Can I have the defence struck out for breach of the accepted
offer?", "Can I discontinue without leave?", "Must I pay the defendant's costs if I discontinue?", "Can my new action be
stayed until I pay the old costs?", "Can I be ordered to give security for costs?", "Is my action stayed until I give
security?", "Must I attend the defendant's medical examination?", "Must the defendant pay my examination expenses?",
"Can I get an order for the medical report?", "Must I sue by a next friend?", "Is my settlement valid without the
Court's approval?", "Where will the money recovered for me be paid?", "From when is my case taken to be inactive?", "Has
my case been dismissed for inactivity?" (37 questions).

No seat for the Court, a master, the Principal Registrar or the case manager. No defendant seat was written; one would
ask the appearance, defence, offer and security rules from the other side (O. 12, O. 20 r. 4, O. 24A, O. 25).

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed: every number and date is in the Rules themselves
  (O. 3, O. 5 r. 11, O. 68 r. 5). The interstate appearance time (Service and Execution of Process Act 1992 (Cth)) is not
  deposited here and answers NOTHING.
- **The actors the text names.** Followed: plaintiff, defendant, offeror, offeree, next friend, the Court, master,
  Public Trustee.
- **Judgments answered conditionally.** Followed: the Court allowing a late extension application (O. 7 r. 1(2)), being
  satisfied of a good reason (O. 7 r. 4(2)), being satisfied the offeror was willing and able and that non-acceptance was
  unreasonable, the interests of justice and "unless the Court otherwise orders" (O. 24A r. 10), special cause (r. 8),
  leave (r. 5), ordering no stay (O. 25 r. 6), ordering that an examination need not take place (O. 28 r. 1(2A)), a
  judge permitting a child to sue alone (O. 70 r. 2(4)), approval and contrary orders (O. 70 rr. 10, 12) are inputs.
- **Definitions worked out; borrowed terms asked.** Followed: "person under disability" (O. 70 r. 1, a "means"
  definition), the time limited for appearing, the closed days of the Central Office (O. 68 r. 5, with Easter computed),
  "month" (O. 3 r. 1) are worked out; "infant" (under 18, Age of Majority Act 1972), "represented person" (Guardianship
  and Administration Act 1990), "procedural step", "material" condition and "liquidated demand" are asked.
- **One case.** One action begun by writ, one defendant (O. 24A r. 9 asks about jointly liable defendants as a fact).
- **The Rules' terms with plain glosses.** Followed: "next friend" glossed as a litigation representative; "unliquidated
  damages" as a personal injury claim; "indemnity basis" and "ordinary basis" for party and party.
- **Operative rules in; machinery out.** Followed (see Scope).

## Scope

**In:** O. 3 rr. 1-4, 7; O. 4A rr. 24, 28; O. 5 r. 11; O. 7 rr. 1(1), (2), 4; O. 9 r. 1(2), (4); O. 13 rr. 1-9; O. 14 r.
1(1); O. 20 rr. 1, 4, 5(4), 20(1); O. 23 rr. 2, 4; O. 24A rr. 3, 4, 5(1), 8, 9, 10(3)-(7A); O. 25 rr. 1, 2, 6; O. 28 r.
1(1), (2), (2A), (4), (5); O. 68 r. 5 (closed days); O. 70 rr. 1, 2(1), (4), 10, 11, 12(1).

**Regulative rules:** three, each a `MUST ... WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE` counted in days, run by
`EVALTRACE` inside an exported question that takes only plain dates: O. 20 r. 1 (the plaintiff serves the statement of
claim), O. 24A r. 3(4) (the plaintiff, as offeree, acknowledges receipt of the defendant's offer), O. 24A r. 4 (the
defendant pays the sum in an accepted offer). The other periods (appearance, defence, reply, acceptance) are computed as
dates.

**Out, and why:**
- O. 1 (but r. 4's definitions where used), O. 2, O. 4, O. 4A Divisions 1-4 (case management conferences, timetables,
  mediation, the CMC List): the Court's machinery; the inactive-case consequences (Division 5) are in.
- O. 4AA and O. 13 rr. 6, 7 in detail (mortgage actions): not a claims matter; the default-judgment kind is named.
- O. 5 rr. 1-10, O. 6, O. 8, O. 9 rr. 2-, O. 10, O. 11, O. 11A, O. 72 (forms of writ, indorsements, solicitors, the
  manner of service in and out of Australia): the drafting and serving of documents; the dates they set are inputs.
- O. 12 (appearance), O. 16-19 (defendant's summary judgment, interpleader, joinder, third parties), O. 20 rr. 2, 3,
  6-19, 21-24 (the form and content of pleadings), O. 21 (amendment): the defendant's side or drafting.
- O. 14 rr. 2-6: the summary judgment procedure after the application.
- O. 24 (payment into and out of court): Registry machinery; O. 24 r. 8 (small intestate estates, $7 500) is not a
  claimant's question.
- O. 24A rr. 1, 2, 3A, 6, 7, 3(9), 10(1), (2), 5(2), (3): who may offer, form, without prejudice, disclosure, and
  orders after acceptance or withdrawal; nothing to compute for the plaintiff beyond what is in.
- O. 25 rr. 3-5, 7, 8: the Court's discretion, form and payment out of security.
- O. 26, 26A, 27 (discovery, pre-action discovery, interrogatories): large and mostly the Court's orders; a next layer.
- O. 28 r. 1(2B), (3), r. 2: costs of an unreasonable party and the Court's sanctions (named in the question's text);
  inspection of objects.
- O. 30-45 (admissions, trial, evidence, experts, subpoenas, judgments), O. 46 and O. 61 (enforcement), O. 51-60A
  (receivers, injunctions, freezing and search orders, committal, judicial review, originating summonses, chambers,
  masters, registrars), O. 65 (appeals to the General Division), O. 66 (costs scales and taxation), O. 67-69, O. 71,
  O. 71A (office, sittings, paper, partners, contact details): outside the claimant's path from writ to settlement, or
  machinery.
- O. 70 rr. 3-9, 13: appointment, removal and service of next friends and guardians ad litem (machinery).
- O. 73 (probate actions) and O. 75 (Family Provision Act 1972 rules): procedure only; the family provision time limit
  is in the Act, not here.
- O. 75A-85 (admission of lawyers, notaries, other Acts' rules, sheriff, cross-vesting, federal jurisdiction).
- O. 1 r. 4C (solicitors notify settlement): a solicitor's duty, not the plaintiff's.
- Within the encoded Orders, also out (added after verification, 2026-11-07):
  - O. 3 rr. 5, 6 (the Court extending or abridging time; the automatic extension while security is pending): the
    Court's order or a pending application sets the new date, which is then an input; the computed deadlines assume no
    extension.
  - O. 4A rr. 22, 23, 25-27 (show cause before the Inactive Cases List, removal from it, and r. 26's limit on filing
    while a case is on it): the Court's procedure on the list; only the r. 24 and r. 28 dates are computed.
  - O. 13 rr. 10-14 (judgment for costs only after payment or satisfaction, the plaintiff serving a default judgment,
    setting aside): steps after judgment is entered, and setting aside is the defendant's application.
  - O. 20 r. 5(1)-(3) and r. 5(4)'s 14 days for a defence to counterclaim: the reply is computed; a counterclaim (where
    the plaintiff is a defendant to it) is the defendant seat's layer.
  - O. 23 rr. 1, 3, 5 (when leave is needed in other cases, judgment for costs not paid within 4 days after taxation,
    withdrawal of an appearance): r. 3 runs from taxation under O. 66, which is out.
  - O. 24A r. 3(1), (2), (6), (7) (who may offer, offers on part of a claim, an offer not withdrawable while open, the
    effect of an offer on other proceedings): the plaintiff's questions take the offer's terms as given; r. 3(6) would
    only confirm that an open offer can still be accepted.
  - O. 28 r. 1(6): the Court's further orders on an examination.
  - O. 70 r. 2(2), (3), (5), r. 10(2), (3), r. 10A, r. 12(2): the next friend's own steps and filings, the Court's
    directions on approval and the investment of money recovered; the plaintiff's questions are whether a next friend
    is needed, whether a settlement binds and where money is paid.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: O. 3 r. 7 "Where a year or more has elapsed"; O. 4A r. 28 "If"; O. 7 r. 1(2) "Where ... if"; O. 7 r. 4
  "If"; O. 23 r. 4 "If"; O. 24A r. 3(5) the acceptance period (ruling (a)) and r. 3(8); r. 5(1) "where ... or where";
  rr. 8, 9 "unless"; O. 25 r. 1 "no order shall be made merely on account of ... poverty"; O. 25 r. 6 "Where ...
  unless"; O. 28 r. 1(1) "Where" (fork F10), r. 1(2) "on demand", r. 1(5) "If ... or if"; O. 70 r. 10 "No settlement ...
  is valid unless".
- `NOTHING`: O. 5 r. 11(2) interstate (points outside the sources) and r. 11(3) a Court order; O. 20 r. 1 where the
  statement of claim is on the writ or leave was given (no duty to compute); O. 20 r. 4(2) after a summary judgment
  summons (the order sets the time); O. 23 r. 2(3) a discontinuance by leave (the Court sets costs); O. 24A r. 3 an
  acceptance dated before the offer; r. 4 unpaid while time runs; r. 5 a sum paid directly in time (fork F9); r. 10
  "unless the Court otherwise orders"; O. 70 r. 10 for an adult, before proceedings (r. 11, fork F12) and for an appeal.

### Forks

- **F1** O. 3 r. 2(1), `O. 3 -- the last day of n days after`: every period here is read as days "not expressed to be
  clear days" (exclusive of the first day, inclusive of the last); clear days are not modelled.
- **F2** O. 68 r. 5, `the Central Office is closed on`: Saturdays, Sundays, Good Friday, Easter Monday and Christmas Day
  are computed; "Public Service holidays" (New Year's Day, Australia Day, Labour Day, Anzac Day, WA Day, the King's
  Birthday, Boxing Day and substitute days) are not, so a period ending on one (for example 28 December 2026) is a day
  early. Asserted (29 December 2026 for a writ served 23 December). Other reading: compute the WA public holidays.
- **F3** O. 3 r. 1, `the last day of n months beginning with`: a period of months ends the day before the corresponding
  date, or, where the month has no corresponding date, on its last day (as Interpretation Act 1984 s 62(3)); so a writ
  issued 29 February 2028 is valid to 28 February 2029. Other reading: to 1 March 2029, rolling the missing date
  forward.
- **F4** O. 3 r. 3, `between 24 December and 15 January`: both 24 December and 15 January are excluded. Other reading:
  "between" excludes the end days.
- **F5** O. 3 r. 4, `O. 3 -- the last day of n days after`: the extension to the next open day is applied to the
  defendant's steps (appearance, defence), not to the plaintiff's own (indorsement of service, statement of claim, reply,
  summary judgment, acknowledgment): the safer date from the plaintiff's seat. r. 4 extends only an act that "cannot be
  done" because the office is closed, and r. 4(2) excludes documents that must be filed electronically, so whether it
  applies turns on how the document is filed. The generic question takes it as an input. Other reading: apply r. 4 to
  every filing, never to service.
- **F6** O. 20 r. 20, `O. 20 r. 20 -- the day the pleadings close`: plain day counting, with neither the r. 3 exclusion
  nor r. 4 (the close is not a time "for filing, serving or amending" a pleading). Other reading: r. 3 applies.
- **F7** O. 3 r. 7, O. 4A rr. 24, 28, O. 7 r. 4: "a year or more has elapsed since", "for 12 months", "for 6 continuous
  months after", "after 6 months after" are met from the day after the last day of the period counted from the day after
  the event. Other reading: met on the anniversary itself.
- **F8** O. 24A r. 3(3), `O. 24A r. 3(5) -- the last day to accept`: a stated time under 28 days is read as 28 days (the
  rule says the time "shall not be less than 28 days" but gives no consequence). Other reading: the offer is not a valid
  O. 24A offer (NOTHING).
- **F9** O. 24A r. 5(1)(a), `O. 24A r. 5 -- I can withdraw my acceptance`: a sum paid to the plaintiff directly within
  the 28 days, not into Court, answers NOTHING (finding 1). Other reading: JUST TRUE, as written ("not paid into Court").
- **F10** O. 28 r. 1(1), `O. 28 r. 1 -- I must submit to the examination`: without notice, or where the condition is not
  material, JUST FALSE (the "Where"). Other reading: NOTHING, the rule being silent about examinations asked for without
  a notice.
- **F11** O. 25 r. 1, `O. 25 rr. 1, 2 -- the Court can order me to give security`: a reason outside the r. 2 list answers
  JUST TRUE under r. 1's general power ("Without limiting the generality of rule 1"). Other reading: NOTHING.
- **F12** O. 70 r. 11, `O. 70 rr. 10, 11 -- the settlement is valid`: an unapproved settlement made before proceedings
  answers NOTHING (r. 11 makes approval optional, "if ... it is desired"; r. 10 speaks of a cause or matter). Other
  reading: JUST FALSE, r. 10's "whenever entered into" reaching back.
- **F13** O. 13 r. 1(2), `O. 5 r. 11, O. 3 -- the last day to appear`: "the time limited for appearing" is the time the
  writ states (at least the O. 5 r. 11 minimum), from the day after service, extended by O. 3 r. 4 where it ends on a
  closed day; default judgment only from the following day.

## What the Rules turn out to say

1. **Payment of an accepted offer: two rules, two tests.** O. 24A r. 4 deems an offer of money to be an offer to pay
   "within 28 days after acceptance", unless the offer says otherwise; r. 5(1)(a) lets the plaintiff withdraw the
   acceptance where the sum "is not paid into Court within 28 days". Read as written, an offer giving 60 days to pay can
   be withdrawn from after day 28, and a sum paid to the plaintiff directly and on time leaves the right to withdraw
   (fork F9). Asserted.
2. **No judgment for want of a defence.** Order 15 was deleted in 1996 and Order 13 deals only with default of
   appearance, but Form 2's note still tells a defendant "If you do not file a defence, judgment may be entered against
   you without notice". The note also gives "14 days after the last day of the time limit for entering an appearance",
   where O. 20 r. 4(1) adds "or after the statement of claim is served ..., whichever is the later" (the same day for a
   writ indorsed with its statement of claim). The plaintiff's routes are summary judgment (O. 14) and case management
   orders.
3. **Three kinds of non-day.** O. 3 r. 2(2) drops days the Central Office is "closed for business" (O. 68 r. 5: weekends,
   Good Friday, Easter Monday, Christmas Day, "Public Service holidays"); O. 1 r. 4 defines a "working day" as one that is
   not a weekend or "a public holiday throughout the State"; and O. 3 r. 3 drops 24 December to 15 January for pleadings
   only, while O. 68 r. 3's Christmas Vacation runs to the second Monday in January. A statement of claim due over
   Christmas gains three weeks; the defendant's time to appear does not. Asserted.
4. **Short periods skip weekends; 7 days does not.** O. 3 r. 2(2) applies only to "less than 7 days", so a 6-day period
   from a Friday ends a day later than a 7-day one. Asserted.
5. **The medical report's week has no start.** O. 28 r. 1(5) gives an order "If default be made for one week in serving
   the copy" but does not say from when (the examination, or the report reaching the party who required it); the
   question asks the fact. The subrules also run (1), (2A), (2B), (2), (3): (2A) and (2B) were inserted before (2).
6. **The offer floor has no consequence.** O. 24A r. 3(3): a time "shall not be less than 28 days", but nothing says what
   follows if an offer states less (fork F8).
7. **A settlement for a child before proceedings.** O. 70 r. 10 invalidates an unapproved settlement "in any cause or
   matter", and r. 11 offers approval of a pre-action settlement only "if ... it is desired": the Rules do not say
   whether an unapproved pre-action settlement binds (fork F12). Asserted (NOTHING).
8. **Interest after the offer is ignored, and so is the judgment's sum at the margin.** O. 24A r. 10(7) disregards
   interest for the time after the day of the offer when comparing; a judgment equal to the defendant's offer is "not
   more favourable" and shifts costs, and one equal to the plaintiff's offer is "no less favourable" and earns them.
   Asserted.

## Before relying on it

- Check for amendments to the Rules after 11 December 2025.
- Compute the WA Public Service holidays (fork F2) and settle when O. 3 r. 4 applies to electronically filed documents
  (fork F5).
- A defendant seat (appearance, defence, offers, security) and the discovery Orders (O. 26, 26A, 27).
- An independent test pass and a human gate; a lawyer's view on forks F5, F7, F8, F9 and F12.
