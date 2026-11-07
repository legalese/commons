# Uniform Civil Procedure Rules 1999 (Qld) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the Rules are applied, with the design defaults
ruled on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of the Rules; nothing existing was touched. The focus asked for is the provisions a
claimant meets: a person bringing a personal injury, compensation, debt or other claim in the Supreme Court, the
District Court or a Magistrates Court. The Rules run to 24 chapters, about 1 000 rules and three scales of costs; most
are the courts' machinery, enforcement, probate, corporations and special proceedings, so the whole instrument is not
tractable as one baseline. Encoded are the rules that fix a claimant's dates, thresholds, amounts and costs
consequences across the life of a claim: the claim's life and renewal, the defendant's notice of intention to defend
and default judgment with its fixed costs, pleadings and the notice to admit, disclosure, the personal injury
statements of Chapter 14 Part 2, settlement by a person under a legal incapacity, discontinuance, offers to settle,
delay, minor claims in a Magistrates Court, the Magistrates Courts scale, costs for suing in a higher court, and the
time to appeal. What is out is listed below with the reason.

Modules:
- `ucpr-dates.l4` -- day, month and anniversary arithmetic (the only module that imports `daydate`);
- `ucpr-rules.l4` -- the rules, by chapter, and the one regulative rule (rr 547, 550);
- `ucpr-seat.l4` -- the claimant's 32 questions, each `@export` with `@desc` inputs, importing the rules and
  restating none;
- `ucpr-cases.l4` -- the cases.

## Edition

Uniform Civil Procedure Rules 1999 (SL 1999 No. 111), the version in force from 29 October 2026 (current on 6 November
2026), deposited at `../../registers/source-bundle/sl-1999-0111.txt`, a plain-text conversion of the Queensland
Legislation HTML "whole" view retrieved 6 November 2026. It is not the authorised (PDF) version.

Not deposited and not applied: the Acts Interpretation Act 1954 (s 38, reckoning of time, to which the note to r 7
points; see fork F1); the Civil Proceedings Act 2011 (interest, s 58 practice directions); the Service and Execution of
Process Act 1992 (Cwlth); the Magistrates Courts Act 1921 and District Court of Queensland Act 1967 (the courts'
monetary limits, asked in r 697); the QCAT Act (asked in r 514); the Public Trustee Act 1978; practice directions and
approved forms.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, at most two
processes at a time (run one at a time). `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
one deliberately wrong assertion was run once in a scratch file, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ucpr-dates.l4` | 0 | 0 | 0 | 0 |
| `ucpr-rules.l4` | 0 | 0 | 0 | 0 |
| `ucpr-seat.l4` | 0 | 0 | 0 | 0 |
| `ucpr-cases.l4` | 0 | 0 | 116 | 116 |

The cases file also runs one `#TRACE` of the rr 547/550 chain (FULFILLED). Every exported question has cases, with the
edges: a claim filed on 29 February; a renewal ending the day before the fifth anniversary, one crossing it and one
starting on it; a default judgment request on the last day for the notice of intention to defend and the day after;
every kind of claim in rr 283-288 and the mortgage exception; each Magistrates scale column at its upper edge and one
cent over; a disputing notice on the 14th and 15th day; both statements on the 28th day and one a day late; an offer
accepted and withdrawn on its closing day and the day after; judgments one cent under and exactly equal to an offer,
from both sides; a step on the first and second anniversaries of the last step and the day after each; a month's
notice from 31 January; $25 000 and $25 000.01 for a minor claim.

## Seat

**The claimant** (`ucpr-seat.l4`): the individual who brings a claim in a Queensland court, usually the plaintiff who
is injured or owed money (in the Rules' words, the plaintiff), and the same person where the Rules give them a step to
answer: a reply to the defence, an answer to a counterclaim against them, a disputing notice. Questions are worded
"Can I ...", "By when must I ...", "Must I ...", "By when must the defendant ..." (what the defendant owes the claimant,
by when).

No seat for the court, a registrar or a costs assessor. No separate defendant layer was written; the defendant's
deadlines that matter to the claimant (the notice of intention to defend, the statement of expert and economic
evidence) are asked from the claimant's side.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed: the Rules fix their own periods and amounts (1 year,
  5 years, 28, 14 and 7 days, $25 000, the scales in Schedules 1 and 2). The Acts Interpretation Act 1954 is not
  deposited; see fork F1.
- **The actors the text names.** Followed: plaintiff, defendant, the court, the registrar, the Court of Appeal, the
  public trustee, the offeror and offeree, an insurer defending in the defendant's name (r 554, noted only).
- **Judgments answered conditionally.** Followed: the registrar's satisfaction (r 24(2)), the court's leave (rr 24(4),
  303, 304, 355), its satisfaction that the offeror was "willing and able" (rr 360-361A), a party showing "another order
  for costs is appropriate", approval of a settlement (rr 98, 359) are inputs. A yes about a power means it can be
  exercised, not that it will be. r 7 (extending time) stands behind every date.
- **The instrument's definitions worked out; borrowed terms asked.** Followed: "minor claim" (Schedule 3) and the
  close of pleadings (r 169) are worked out; "debt or liquidated demand", "unliquidated damages", "person under a legal
  incapacity", the QCAT minor civil dispute and the courts' jurisdiction are asked.
- **One case.** One proceeding, one claimant, one defendant (rr 363, 364 on several defendants are out).
- **The text's terms with plain glosses.** "Discontinue" glossed "drop"; "liquidated demand" glossed "a fixed sum
  owed"; "unliquidated damages" glossed "compensation to be assessed".
- **Operative rules in; machinery out.** Followed (see Scope).

## Scope

**In:** rr 24 (all subrules except (5), the seal), 98(1), 137, 138 (as the effect of a late notice), 164(1)-(2), 169,
189(2)-(3), 214(2)(a), (d), (e) and (3), 281(1), 282, 283(1)-(2) with 694 and Schedule 1 items 19-20 and Schedule 2
Part 2 items 1 and 4 and Part 3 items 19-20, 284-288, 303(1), 304(1)-(3), 307, 309(1), 355(1)-(3), (6), 358(1)-(3), 359(2), 360, 361, 361A,
362 (in the input's wording), 389, 514, Schedule 3 "minor claim", 545, 546, 547(1)-(2), 550(2), 557 (in the breach
reason), 558(1), (2), (4), 681 (the default answer), 691(3)-(4) with Schedule 2's columns, 697, 748. 32 exported
questions.

**Regulative rule:** one. rr 547(1) and 550(2) as a chain: the plaintiff MUST serve a statement of loss and damage
WITHIN 28 days of the close of pleadings, HENCE the defendant MUST serve a statement of expert and economic evidence
WITHIN 28 days, each LEST BREACH BY that party BECAUSE (naming r 557). Run by EVALTRACE inside "Were the statements
served in time?", which takes plain dates only; one `#TRACE` in the cases.

**Out, and why:**
- Chapter 1 except r 7 (as a caveat): machinery. Chapter 2 except r 24: the form and place of starting, applications,
  cross-vesting.
- Chapter 3 except rr 98 and the incapacity part of r 359: joinder, representative proceedings, partnerships; the
  litigation guardian mechanics.
- Chapter 4 (service): how to serve; dates of deemed service are not asked (the questions take the day served).
- Chapter 5 except r 137: the defendant's form of notice; r 144 (conditional notice) and r 281(2) are the defendant's
  route and not encoded.
- Chapter 6 except rr 164, 169, 189: the content of pleadings, particulars, deemed admissions by failure to plead
  (r 166, a question of pleading not dates), third party proceedings.
- Chapter 7 except r 214: preliminary disclosure, non-party disclosure, inspection; r 214(2)(b)-(c) (summary decision
  and amended pleadings) left out for size.
- Chapters 8, 9A, 12, 15, 19-24 and Schedules 1A and 4: preservation orders, arbitration, the registrar's jurisdiction,
  probate, enforcement, foreign judgments, interpleader, registry, corporations, transitional rules.
- Chapter 9 Part 2 (summary judgment, the court's), Part 4 (ADR: the court's referral; the stay in r 321 is noted
  only), and in Part 5 rr 352-354, 356, 357, 362A, 363-365 (form, without-prejudice status, wrongful death
  apportionment, several defendants, contribution, enforcing an accepted offer).
- Chapter 10 except r 389: directions, amendment, non-compliance.
- Chapter 11 (evidence, experts, affidavits): procedure without a date the claimant computes beyond the business-day
  periods of applications, which would need the Acts Interpretation Act's business days.
- Chapter 13 except rr 514-515: trial listing (r 467's readiness, which in a personal injury claim includes Part 2
  of Chapter 14, is noted in the r 547 question), assessment of damages procedure, employment claims (Division 2A),
  settlement conferences.
- Chapter 14 except Part 2: accounts, money in court, judicial review, habeas corpus, trans-Tasman. In Part 2, the
  content of the statements (rr 547(3), 548, 551) and the conference (r 553) are lists without a computable answer;
  r 549 (the statement must be accurate; a supplement on a "significant change" before a trial date is set; further
  documents "as soon as practicable" after) has no date or number to compute, only judgments of change and promptness.
- Chapter 9 Part 1 Division 2, r 289 (judgment for costs alone where the defendant in default satisfies the claim):
  a further request on the same entitlement as rr 281-283, with no date of its own; its costs are not fixed by
  r 283(2)(b), so it adds no computable answer. r 290 (setting aside) is the court's.
- Chapter 16 (orders), Chapter 17 (security for costs, the defendant's application), Chapter 17A except rr 681, 691,
  694, 697: costs assessment procedure, the Legal Profession Act assessments.
- Chapter 18 except r 748: appeal procedure and powers.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind`
answers:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: rr 98(1) "ineffective unless" and 359(2) "not binding ... unless" without approval; rr 355, 358 an
  acceptance after the period the offer fixes (period, rule (a)), or after leave to withdraw is given.
- `NOTHING`: rr 98, 359 for a claimant not under a legal incapacity (scope limit, F8); r 214(2)(a) where an order sets
  the times (points outside the sources, F9). (The fixed default-judgment costs over $50 000 in a Magistrates Court
  are not NOTHING: Schedule 2 Part 3 fixed cost items 19 and 20 set $1,698.00 and $446.40; corrected 2026-11-07 after
  the independent verification.)
- The date questions return a date and the enumerated questions a value of the text's own list; where a rule's
  conditions fail, the enumeration says so in words ("rule 697 does not reduce my costs", "the offer rules do not
  apply ...").

## Forks

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | r 7 note, Acts Interpretation Act 1954 s 38 (not deposited) | every date question | The day of the event is not counted; a year or month ends on the corresponding day (29 February's anniversary is 28 February); no last day moves for a weekend, holiday or closed registry | s 38 moves a last day on which the registry is closed to the next day it is open; answers near weekends and holidays may be a day or more early |
| F2 | r 558(2) "at least 21 days before" | `r 558(2) -- ...` | The act's own day is the 21st day before the assessment, that day not counted | 21 clear days, one day earlier |
| F3 | r 389 "for 1 year from the time the last step was taken" | `r 389 -- ...` | A step on the anniversary is within the year; notice is needed from the day after | The year is complete on the anniversary itself |
| F4 | r 389(1) "a month's notice" | `r 389(1) -- the first day ...` | The month ends on the corresponding day of the next month (or its last day); the step may be taken the day after | The step may be taken on the corresponding day |
| F5 | r 558(4) "7 days before the date set" | `r 558(4) -- ...` | Read as a latest day, like (2) | Exactly on that day, or 7 clear days |
| F6 | r 283(2)(b)(i) "costs for issuing the claim" | `r 283(2)(b) -- ...` | Schedule 2 Part 2 item 1 ("Instructions to sue--claim and statement of claim and service") and item 4; over $50 000, Schedule 2 Part 3 items 19 (the same words) and 20; Schedule 1 items 19 and 20 | Item 1 covers more than issuing; the registrar fixes a lesser figure under r 694 |
| F7 | rr 360, 361 "no less favourable" / "less favourable" | `rr 360-362 -- ...` | Money offers compared by amount, the judgment leaving out interest after the day of service (r 362) | Non-money terms and costs inclusions make the comparison a judgment for the court |
| F8 | rr 98, 359 for a party with capacity | `rr 98, 359 -- ...` | NOTHING (scope limit) | JUST TRUE (binding in the ordinary way) |
| F9 | r 214(2)(a) "the times stated in the order" | `r 214(2) -- ...` | NOTHING (outside the sources) | The 28 days of (e) apply where the order is silent |
| F10 | r 189(2) a disputing notice | `r 189 -- ...` | Served on or before the 14th day after service of the notice to admit counts | Served on the 14th day is late if "within 14 days" excludes it |
| F11 | r 361(3) offer served at trial | `rr 360-362 -- ...` | (3) displaces (2) whenever served on or after the first trial day, subject only to the court ordering otherwise; a party "showing another order" under (2) is not asked | A party may still show another order under (2) |

## What the Rules turn out to say

1. **A renewal can be split at the fifth anniversary.** r 24(4) requires leave only for a renewal period "any part of
   which falls on or after the fifth anniversary"; a registrar can renew without leave up to the day before it, and
   only the rest needs the court. Asserted.
2. **A judgment equal to the plaintiff's offer triggers indemnity costs; one equal to the defendant's offer triggers
   nothing.** r 360 needs an order "no less favourable" than the plaintiff's offer, r 361 one "less favourable" than the
   defendant's. Asserted for both, with a one-cent difference.
3. **These Rules have no Christmas break and no business-day rule for their day periods.** Unlike the Federal Court
   Rules (r 1.61), the UCPR count calendar days and leave the rest to the Acts Interpretation Act 1954 s 38 (F1). A
   notice of intention to defend for a claim served on 15 December 2026 is due on 12 January 2027. Asserted.
4. **r 361(3) has its own saving words.** It applies "unless the court otherwise orders", while (2) applies "Unless a
   party shows another order for costs is appropriate"; the encoding gives (3) precedence for offers served at trial
   (F11).
5. **Possible drafting slip in r 144(6).** It speaks of "a conditional notice of defence" becoming "an unconditional
   notice of intention to defend"; everywhere else the Rules say "conditional notice of intention to defend". Not
   encoded (out of scope); noted.
6. **Two definitions of "minor claim" in the deposit.** Schedule 3 sets $25 000; r 998(3) keeps the old $7 500 for
   proceedings started before the 2009 QCAT amendments. The encoding uses Schedule 3. Asserted at $25 000 and
   $25 000.01.
7. **The personal injury statements have no direct sanction.** Part 2 of Chapter 14 attaches no consequence to a late
   statement beyond costs (r 557), the bar on evidence not identified (rr 548(4), 551(4)) and the trial-date gate (rr
   547(2), 550(2), 467(4)(g)); the breach reasons say so.
8. **A late notice of intention to defend still blocks default judgment.** r 138 lets a defendant file "at any time
   before judgment, even if the defendant is in default", and r 281(1) applies only where the notice "has not" been
   filed. Asserted.
9. **r 283(2) fixes the costs, the scale fixes the figures.** Default-judgment costs in a Magistrates Court depend on
   the column of the amount up to $50 000; over $50 000 Schedule 2 Part 3, though mostly discretionary (item 1, care
   and conduct, is what the registrar or a costs assessor considers reasonable), still has fixed cost items 19 and 20
   ($1,698.00 + $446.40). Asserted at each edge.

## Before relying on it

- Deposit the Acts Interpretation Act 1954 (s 38) and apply its registry-closed rule (F1); answers on a weekend or
  public holiday can be a day or more early.
- A lawyer to confirm the forks, especially F1 (including a claim filed on 29 February, taken to end on 27 February
  the next year), F2 (r 558(2) "at least 21 days before", taken as not clear days), F3, F4, F6 and F11.
- An independent test pass, and the human gates HG1 and HG2.
- Further layers: deemed service (Chapter 4), r 214(2)(b)-(c), summary judgment, security for costs, the costs
  assessment rules, and a defendant's seat.

## Licence

The L4 is Apache-2.0. The quoted text is (c) The State of Queensland, CC BY 4.0: "Based on content from the Queensland
Legislation website at 6 November 2026. For the latest information on Queensland Government legislation please go to
https://www.legislation.qld.gov.au." See `SOURCE-LICENSE.md`.
