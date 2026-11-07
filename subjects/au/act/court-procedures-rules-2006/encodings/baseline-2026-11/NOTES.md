# Court Procedures Rules 2006 (ACT) -- baseline encoding, the person bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the rules are applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The rules are very large (23,814 lines, 1.87 million characters): every civil, criminal and appellate procedure in the
ACT Supreme Court and Magistrates Court. Encoding the whole is not tractable, so this baseline takes the focus asked for
-- the provisions a claimant meets -- and encodes the claimant's path through Chapter 2: the day the proceeding starts;
keeping the originating process alive and the proceeding from being dismissed for delay; the defendant's time to defend
and default; offers of compromise and the costs that follow; interest up to and after judgment, with schedule 2's rates;
the fixed costs of schedule 3 that a debt claimant meets; r 1725, which cuts the costs of a small win in the Supreme
Court; and r 250, which says who may bring a death claim for the family. What is out, and why, is listed under Scope.

The dates are in one small module (`cpr-dates.l4`, built-in date functions only, no daydate), the rules and exported
questions in `cpr-claims.l4`, and the worked cases in `cpr-cases.l4`. The two duties with deadlines the plaintiff waits
on -- the defendant's defence (r 102, r 111, giving "default" under r 1117) and the offeror's payment after an offer is
accepted (r 1002 (6), giving the right to withdraw under r 1004 (1) (a)) -- are regulative rules run by EVALTRACE inside
exported questions that take only plain facts. No earlier encoding of these rules exists; nothing was touched or
imported from elsewhere.

## Edition

- **Rules:** Court Procedures Rules 2006 (ACT), SL2006-29, Republication No 73 (R73), effective 1 August 2026, last
  amended by SL2026-11, as deposited at `../../registers/source-bundle/SL2006-29.txt` (converted from the register's
  DOCX, which the register marks as an unauthorised version; the authorised text is the register's PDF).
- **Numbers:** the interest rates (schedule 2) and the fixed costs amounts (schedule 3, parts 3.1 and 3.2) are the rules'
  own schedules, in this republication. The Reserve Bank cash rate that schedule 2 uses after 30 June 2010 is not in the
  rules and is asked. The Magistrates Court determined fee (r 1725) is set under the Court Procedures Act 2004, part 3,
  not deposited: r 1725's answer names it without an amount.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong expected day (30 March 2026 for 29 March 2026, three assertions) was run once in a scratch copy
outside the repository and showed as three "assertion failed" (169 satisfied). After the verification fixes of
2026-11-07 the files were run again: 182 written, 182 satisfied.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cpr-dates.l4` | 0 | 0 | 0 | 0 |
| `cpr-claims.l4` | 0 | 0 | 0 | 0 |
| `cpr-cases.l4` | 0 | 0 | 182 | 182 |

Every exported question has cases, with the edges: the last day of validity and the day after; a renewal's last day
and the day after; 31 August plus 6 months in a leap and a common year; the rule's own r 75 example (1 July 2006 to
2 July 2007); each ground of r 75 on its last day and the day after, and r 76 (3) reinstatement on its last day and the
day after; $250 000 and $250 001 for r 55; 28 days over Christmas (25 December to 1 January not counted); each band edge
of schedule 3 ($9 999 / $10 000, $249 999 / $250 000) and costs at and $1 over the fixed amount; r 1725 at $49 999 /
$50 000, $99 999 / $100 000, $174 999 / $175 000; an offer exactly 2 months before trial and a day later, and an
acceptance period of 28 and 27 days; judgment equal to the offer, $1 under and $1 over, with post-offer interest
disregarded (r 1013); r 1619 (8) at exactly 110% and $1 over; sampled period boundaries in all four schedule 2 tables;
the 6-month line of r 250.

**No mirror cases.** One seat.

## Seat

**The person bringing a claim (the plaintiff)** (`cpr-claims.l4`): the injured person, the family of a person who died,
the creditor -- whoever brings a civil claim in the ACT Supreme Court or Magistrates Court. "On what day did my
proceeding start?", "Can I still serve my claim?", "Has my proceeding been dismissed for delay?", "By when must the
defendant defend?", "Is the defendant in default?", "What default judgment can I get?", "What must the defendant pay to
stop my debt claim?", "Is my offer's acceptance period long enough?", "Can I still accept?", "Can I withdraw my
acceptance?", "What costs follow the offer?", "Can I get interest after the defendant's offer?", "Will interest run on my
judgment?", "What rate?", "Can I start the death claim?".

The rules speak mostly to the parties as "plaintiff" and "defendant" (r 20) and to the court and registrar. The court
and the registrar get no seat: what the court decides (renewal, reasonableness, special circumstances, orders otherwise,
willing and able) is asked as a fact. A defendant's seat would be a natural second layer (time to defend, offers from the
other side); none was written.

The 2026-10-18 defaults:

- **The instrument alone, plus what sets its numbers.** Followed: schedules 2 and 3 are the rules' own. The Civil Law
  (Wrongs) Act 2002 ch 14 and the Road Transport (Third-Party Insurance) Act 2008 pts 4.8 and 4.9, to which Part 2.10 is
  subject (r 1000), are not brought in (fork F11).
- **The actors the text names.** Followed: plaintiff, defendant, offeror and offeree, personal representative,
  beneficiaries, the court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the court renewed the
  originating process and to when; whether an acceptance period is reasonable; special circumstances (r 1619 (7));
  whether the offeror was willing and able (r 1014); whether the court ordered otherwise; whether the Magistrates Court
  could have heard the proceeding (r 1102 (2), r 1725).
- **The rules' own definitions are worked out; borrowed terms are asked.** Worked out: "in default" (r 1117), "period of
  acceptance" (r 1001), "appropriate settlement amount" as far as r 1619 (8) goes, "prescribed costs amount" (r 1100 and
  schedule 3). Asked: "personal injury claim" (not defined in the rules), "debt or liquidated demand" as a classification,
  member of the family (Civil Law (Wrongs) Act 2002), "step" in the proceeding.
- **One case is the text's natural unit.** Followed: one proceeding, one plaintiff against one defendant, one offer.
- **The rules' own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative provisions in; machinery out.** Followed, within the focus.

## Scope

**In.** r 32 with r 74 (6) and r 76 (5); r 74; r 75 with r 76 (3); r 55; r 102 (1); r 111 (3)-(5); r 1116, r 1117,
r 1118 (1), r 1120 to r 1126 (which rule a default judgment goes under); r 1101, r 1102 and schedule 3 part 3.1; r 1121
and schedule 3 part 3.2; r 1725; Part 2.10: r 1001, r 1002 (5), (6), (9), r 1003 (1), r 1004 (1), r 1009 to r 1014;
r 1619 (7), (8); r 1620 (1), (2); schedule 2 (all four tables and the post-2010 formulas); r 250; r 6350 (3).

**Out, and why.**
- Chapter 1, Part 2.1 (apart from r 20's meaning of plaintiff), and the content rules for originating process
  (r 30, r 31, r 33-r 37, r 50-r 54, r 60-r 64, r 70-r 73): form and content, not decisions a claimant asks about; r 52
  and r 53 (what a motor vehicle or employment injury statement of claim must contain) are lists for the pleader.
- The rest of Part 2.3 (r 100, r 101, r 103-r 110, division 2.3.2): the defendant's side and possession of land. Also
  r 102 (2)-(5) (the court setting a time for a defence after a summary judgment application; the time for a notice of
  intention to respond in a proceeding started by originating application; sealing; serving the sealed copy on the
  plaintiff) and r 111 (1)-(2) (when a defendant must file a conditional notice; submission to the jurisdiction by an
  unconditional one): a court order, another kind of proceeding, or the defendant's side, not a claimant test.
- r 74 (2) (who may apply to renew) and r 74 (5) (stamping a renewed process before service): form, named in the answers
  but not encoded. r 76 (1), (2) (applying to reinstate; the court's interests-of-justice power): court
  powers, named in the answers. r 76 (4) (serving the reinstating document on each other active party within 3 days):
  a duty of form that does not change whether r 76 (3) reinstates. Only r 76 (3) and (5) are encoded.
- Part 2.4 apart from r 250, notably division 2.4.9 (people with a legal disability; court approval of settlements,
  r 282) and r 251 (adding a family member to a death claim -- named in an answer, not encoded): a claimant meets them,
  but they are court powers with no fixed test; a further layer could add them.
- Parts 2.5 to 2.9 (third parties, pleadings, amendment, disclosure, preliminary discovery, preservation): procedure
  without the entitlement, threshold, amount or time shape the focus asks for.
- The rest of Part 2.10 (r 1002 (1)-(4), (7), (8), (10), r 1004 (2), r 1005-r 1008): form and effect of offers that do
  not turn on facts a claimant states.
- The rest of Part 2.11 (r 1103, r 1104, division 2.11.2, r 1118 (2)-(6), r 1119, r 1127, r 1128, divisions 2.11.4 to
  2.11.7: partial defence, summary judgment, discontinuance, mediation): affidavit content and court powers.
- Parts 2.12 to 2.15 and schedule 1 (expert evidence and the expert code, pre-trial, court supervision, trial).
- The rest of Part 2.16, notably r 1619 (1)-(6), r 1620 (3)-(5) (interest on costs), r 1621, r 1622 (the usual order as to interest, with its Medicare and
  Centrelink recovery conditions) and r 1623: r 1619 (1) is a discretion; r 1622 depends on Commonwealth notices
  not deposited.
- Part 2.17 apart from r 1725 (costs generally, the scale of costs in schedule 4, assessment, security for costs):
  large, and mostly the court's and the assessor's.
- Parts 2.18 to 2.22 (enforcement, interpleader, trusts and accounts, solicitors), Chapter 3 (particular proceedings),
  Chapters 4 to 7, schedules 3 parts 3.3-3.5, 4 and 5. **Part 3.13 (workers compensation arbitrations)** is its own
  claims machinery (applications, medical referees, conciliation, awards) and would be best encoded as a second baseline
  beside this one, read with the Workers Compensation Act 1951 baseline. **Chapter 5's leave to appeal out of time** is
  likewise a candidate.
- The Legislation Act 2001 s 151A (a period ending on a non-working day ends on the next working day) and r 6350 (2)
  (registry-closed days in periods of 5 days or less): fork F5.
- No requirement ledger exists for the ACT, and none was raised.

## Rulings on negatives (2026-11-04 and 2026-11-05), as applied here

The rule of 2026-10-29, as the 2026-11-04 rulings settle it: a function answers the text's no only where the text itself
says no to the case in its own words (a "means" definition, a condition introduced with "if", "only if", "as long as" or
"unless", a list closed with "only", a flat negative); everywhere else it answers NOTHING (a list not closed, "includes",
an undefined term, silence, a pointer outside the sources, or a limit in the grant's own wording). Periods ruling: (a) a
period the text fixes in its own words: outside it, the text's no; (b) a "where" condition failing: the text's no; (c)
a scope limit with no "only": NOTHING. Most questions here return an enumeration whose wording says which kind of answer
it is: "(the text's no)" or "(NOTHING-kind)". Where a function returns MAYBE, NOTHING is the NOTHING-kind answer.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "personal injury claim" (r 1010, r 1011), undefined in the rules -- `Part 2.10 -- what costs follow the offer` --
  asked as a fact -- worked out from the Civil Law (Wrongs) Act 2002 definition of personal injury.
- **F2** r 74 (1) "valid for service for 1 year starting on the day it is filed" -- `r 74 (1) -- the last day of the
  first year of validity` -- the day before the same date a year on (filed 1 March 2026: last day 28 February 2027;
  filed 1 March 2027: 29 February 2028); filed on 29 February, the last day is 28 February -- the anniversary of the
  filing day itself. (Before the 2026-11-07 fix this was worked as the anniversary of the day before filing, which
  clamped at 28 February and lost 29 February 2028 for a filing on 1 March 2027.)
- **F3** periods in months and years (r 74, r 75, r 250, r 1002 (5)) -- `plus months` -- a day the month lacks becomes the
  last day of that month (31 August + 6 months = 28 or 29 February; a year from 29 February is 28 February) -- rolling
  forward to 1 March. A period "starting on" a day (r 74 (1), r 74 (3)) or running from the end of a day ("at the end of
  1 year after the day", r 75, r 76 (3)) is counted from its first day: its last day is the day before the same date n
  months on, or, where that later month lacks the date, that month's last day (`the last day of ... months starting
  on`). So a r 74 (3) renewal from 1 March 2027 can run to 31 August 2027, not 28 August.
- **F4** r 6350 (3) (25 December to 1 January excluded "in working out when the thing must or may be ... done") --
  applied to r 102, r 111, r 1002 (6)/r 1004 (1) (a) and r 1620 (2); not applied to r 74, r 75, r 76, r 250 or r 1002 (5)
  (validity, deeming, standing and the content of an offer, not something done within a period) -- applied to every
  period, or to the day-counted ones only.
- **F5** Legislation Act 2001 s 151A (period ending on a non-working day) and r 6350 (2) -- not applied (another Act; the
  day computed is the last day before any move to the next working day) -- applied, with a list of non-working days.
- **F6** r 75 (1) (a) "1 year after the day the originating process is issued" -- `r 75 -- is my proceeding taken to be
  dismissed` -- "issued" read as the day of filing and sealing -- the day the sealed copy is given back to the plaintiff.
- **F7** r 111 (4), (5) against r 102 (1) (b), for a conditional notice -- `r 102 -- by what day must the defendant file a
  defence` -- a lapsed conditional notice becomes unconditional on the day after the 28th day; when the r 40 application
  is refused, the r 111 (5) 14 days govern, as r 1117 (1) (a) (iii) says -- r 102 (1) (b)'s 7 days, or the later of the two.
- **F8** r 106 (submitting defendant) -- `r 1117 -- is the defendant in default` -- not covered; a submitting notice is
  treated like any notice of intention to respond (a defence is still looked for) -- treating it as an answer that
  prevents default.
- **F9** r 1122 "with or without another claim" and r 1126 (1) -- `r 1120 to r 1126 -- which default judgment can I ask
  for` -- a claim for unliquidated damages with any other claim goes under r 1122 alone -- r 1125 or r 1126 for the other
  claim.
- **F10** r 1121 (3) "subject to rule 1725" -- `r 1121 -- are my default judgment costs allowed without assessment` --
  NOTHING when r 1725 applies -- r 1121 (2) applied with r 1725's percentages on top.
- **F11** r 1000 (Part 2.10 subject to the Civil Law (Wrongs) Act ch 14 and the Road Transport (Third-Party Insurance)
  Act pts 4.8, 4.9) -- every Part 2.10 question -- those Acts not brought in; the answers may be displaced where they
  apply -- asking whether they apply and answering NOTHING.
- **F12** r 1002 (5) (a) where no trial date is set -- `r 1002 (5) -- is the acceptance period long enough` -- falls under
  (b) "any other case" (reasonable period) -- treated as made "2 months or more before" the trial (28-day floor).
- **F13** r 1004 (1) (a), money paid after the deadline -- `r 1004 -- can I withdraw my acceptance for non-payment` -- the
  right to withdraw, once arisen, survives a late payment -- a late payment before notice of withdrawal takes it away.
- **F14** r 1011 against r 1012 -- `Part 2.10 -- what costs follow the offer` -- r 1011 where the plaintiff obtains a
  judgment, r 1012 only where the defendant does (judgment for the defendant or dismissal) -- r 1012 also where the
  plaintiff's judgment is below the defendant's offer.
- **F15** r 250 (3) "at the end of 6 months after the day of the death" -- `r 250 -- can I start the death claim` -- a
  beneficiary may start from the day after the 6-month period ends -- from the last day of that period.
- **F16** r 1117 (1) "any further period agreed ... or allowed" -- `r 1117 -- is the defendant in default` -- an agreed or
  allowed day earlier than the rules' own last day is ignored (it is not a "further" period) -- applied as given.
- **F17** r 1009 (2), (3) "proposed a judgment in favour of the plaintiff / defendant" -- `Part 2.10 -- what costs follow
  the offer` -- an offer proposing an amount above 0 is in the plaintiff's favour; 0 is a judgment for the defendant --
  asked as a separate choice.

## What the rules turn out to say (findings)

1. **A $250 000 Magistrates Court claim has no fixed costs amount.** Schedule 3, tables 3.1 and 3.2 stop at "≥ $50 000 but
   < $250 000" for the Magistrates Court, while r 55 (2) (a) has a claimant "limit the claim to $250 000". A debt claim of
   exactly $250 000 falls in no band, so r 1102 and r 1121 have no amount to apply. The answer is NOTHING. Asserted.
2. **An offer made before the trial is set down has no 28-day minimum.** r 1002 (5) (a) applies to an offer made "2 months
   or more before the date set down for the start of the trial". Read literally, it cannot apply before a date is set, so
   an early offer falls under (b) and needs only a "reasonable" acceptance period. That is probably not what the drafter
   meant. Fork F12. Asserted.
3. **r 1012 moves to the higher costs earlier than r 1010 and r 1011.** For an offer made before the trial, r 1010 and
   r 1011 switch "from the day the period for acceptance of the offer ends", but r 1012 switches "on and from the day after
   the offer was made". So a defendant that wins after its offer is refused gets solicitor-and-client costs for the
   acceptance period too. Asserted (2 March against 29 March).
4. **Other claims joined to a damages claim have no default judgment rule.** r 1122 covers unliquidated damages "with or
   without another claim", and r 1126 is open only where the plaintiff "is not entitled to apply" under r 1120-r 1124. So
   a claim for damages plus (say) an injunction gets damages to be assessed, and no rule enters default judgment on the
   injunction. Fork F9. Asserted.
5. **r 75 (1) (a) dismisses even when the defendant has defended.** It turns only on whether an affidavit of service has
   been filed within a year after issue. A defendant who files a defence is taken to have been served (r 73), but if no
   affidavit is filed the proceeding is still taken to be dismissed. The rules have no exception for this. Asserted.
6. **Two periods for the same event.** When a r 40 application by a defendant who filed a conditional notice is refused,
   r 102 (1) (b) gives 7 days after the refusal and r 111 (5) gives 14 days after the notice becomes unconditional (which
   is on the refusal). r 1117 (1) (a) (iii) measures default for this case by r 111, so this encoding uses 14 days. Fork F7.
   Asserted (3 April 2026).
7. **"Appropriate settlement amount" is defined only one way.** r 1619 (8) says when an offer *is* appropriate (the
   judgment, with interest to the day of the offer, is not more than 10% above it). It does not say the offer is
   inappropriate otherwise. Where the judgment is more than 10% higher, the rules do not answer. NOTHING-kind. Asserted.
8. **r 1011 and r 1012 overlap on their words.** A judgment for the plaintiff for less than the defendant's refused offer is
   "no more favourable to the plaintiff" (r 1011) and also "no less favourable to the defendant" (r 1012), and the two
   give different costs. Read here as r 1012 needing a judgment the defendant obtains. Fork F14.
9. **"1 year" means two different days in r 74 and r 75.** Under r 74 (1) the originating process stops being valid for
   service on the day before the anniversary of filing. Under r 75 (1) (a) and (4) the proceeding is dismissed on the day
   after the anniversary of issue if no affidavit of service is filed. So there are two days between the end of
   validity and the dismissal. "Issued" is not defined (fork F6). Asserted (28 February 2027 against 2 March 2027).

## Before relying on it

- An independent test pass, and a lawyer's look at forks F4, F7, F12 and F14.
- The Legislation Act 2001 s 151 and s 151A, so the last days move off weekends and public holidays (fork F5).
- The usual order as to interest (r 1622) and r 1619 (1)-(6) with the Civil Law (Wrongs) Act limits on interest for
  personal injury damages.
- Part 3.13 (workers compensation arbitrations) and division 2.4.9 (claimants with a legal disability, settlement
  approval) as further layers.
- The Reserve Bank cash rate is asked; a published table of the half-yearly rates would let schedule 2 answer from the date
  alone.
