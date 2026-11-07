# Federal Court Rules 2011 (Cth) -- baseline encoding, the party to a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the Rules are applied, with the design defaults
ruled on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of the Rules; nothing existing was touched. The focus asked for is courts, procedure, time
limits, damages and costs, as met by a person bringing or answering a claim (personal injury, compensation,
employment, discrimination and other claims that reach the Federal Court). The Rules run to 43 Parts and about 600
rules, most of them the Court's machinery or special classes of proceeding, so the whole instrument is not tractable as
one baseline. Encoded are the rules that fix a claimant's dates, thresholds, amounts and costs consequences, across
the life of a claim: counting time, starting and serving the claim, the defence and default, medical examinations,
offers to settle, ending a claim early, damages calculated by a Registrar, appeals, judgments and interest, and costs.
What is out is listed below with the reason.

Modules:
- `fcr-dates.l4` -- r 1.61 (calculation of time) and the Dictionary's "business day"; the only module that imports
  `daydate`;
- `fcr-rules.l4` -- the rules, by Part, and the two regulative rules;
- `fcr-seat.l4` -- the party's questions, each `@export` with `@desc` inputs, importing the rules and restating none;
- `fcr-cases.l4` -- the cases.

## Edition

Federal Court Rules 2011 (F2011L01551), Compilation No. 11 (compilation date 11 June 2026, register id F2026C00512,
includes amendments up to F2026L00616), deposited at `../../registers/source-bundle/F2011L01551.txt`, a plain-text
conversion of the Word file from the Federal Register of Legislation, retrieved 6 November 2026. Amendments after the
compilation date are not in the text.

Not deposited and not applied: the Federal Court of Australia Act 1976 provisions the Rules serve (s 51A prejudgment
interest, s 52 judgment interest, s 56 security for costs, s 43 costs; that Act has its own baseline beside this one,
for Part IVA); the Civil Dispute Resolution Act 2011 (whether Part 2 applies is asked); the Acts Interpretation Act
1901; State and Territory public holiday laws (see fork F1); the approved Forms and the Court's practice notes.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, at most two
processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; one deliberately wrong
assertion was run once in a scratch file, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `fcr-dates.l4` | 0 | 0 | 0 | 0 |
| `fcr-rules.l4` | 0 | 0 | 0 | 0 |
| `fcr-seat.l4` | 0 | 0 | 0 | 0 |
| `fcr-cases.l4` | 0 | 0 | 196 | 196 |

The cases file also runs one `#TRACE` of the r 16.32 duty (a defence on day 28 of 28: FULFILLED). Every exported
question has cases, with the edges: the rule's own r 1.61 Example (Wednesday plus 3 days is Monday); 5- and 6-day
periods from the same Friday; the Christmas break at each end; a last day on a Saturday and on Australia Day, for a
filing and for service; the 4.30 pm filing cut-off; the seventh business day for post; r 8.06 counted back across the
break; a defence filed on and a day after the last day, none filed on and after the last day, and each other head of
r 5.22; every r 5.23(2) outcome; every r 23.21 basis; offers open exactly 14 days and one day short, acceptance on and
after the closing day, withdrawal on day 14 and day 15; payment on and after day 28 and across the break; every cell of
the r 25.14 matrix, including a judgment exactly as favourable as the offer; discontinuance the day before and the day
of the first directions hearing, on pleadings open and closed, after judgment and as a representative; $99 999.99,
$100 000 and $100 000.01 under r 40.08; taxation at exactly 115% and 85% of the estimate and one dollar beyond.

## Seat

**The individual party to a claim in the Federal Court** (`fcr-seat.l4`): usually the applicant who brings it (an
injured person, an employee, a person discriminated against, a claimant for compensation or a debt); and the same
person where the Rules put the step on them as the one answering (a respondent filing a defence, a respondent to an
appeal, the party paying a costs bill), with the role asked where it matters. Questions are worded "Can I ...", "By
when must I ...", "Must I ...".

No seat for the Court, a Registrar or a taxing officer. No separate respondent or business seat layer was written; the
defence, appeal-respondent and costs-payer questions already take that side's facts, and a business respondent's layer
would ask the same rules.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed: the Rules fix their own periods and amounts ($2 000
  security, $100 000, 115%, 85%, 6% above the cash rate). The cash rate is an input. Public holidays are not
  deposited; see fork F1.
- **The actors the text names.** Followed: applicant, respondent, offeror, offeree, appellant, the Court, a Registrar,
  a taxing officer, a medical expert, a litigation representative, a representative party.
- **Judgments answered conditionally.** Followed: the Court's leave (rr 25.07, 25.09, 26.12), its satisfaction that
  damages are "substantially a matter of calculation" (r 30.41), whether the applicant "unreasonably fails to accept"
  (r 25.14(2)), whether a proceeding "could more suitably have been brought in another court or tribunal" (r 40.08) and
  "due diligence" (r 5.22(d)) are inputs worded "if the Court ...". A yes about a power of the Court means it can act,
  not that it will. Rules 1.35 (orders inconsistent with the Rules) and 1.39 (extending or shortening time) stand
  behind every answer and are said so in the seat module's header and the appeal questions.
- **The instrument's definitions worked out; borrowed terms asked.** Followed: business day, the calculation of time,
  default (r 5.22), medical expert (r 23.21(8)), the day of filing (r 2.25(3)) and of service (r 10.32) are worked
  out; "debt or liquidated damages", "Part 2 of the Civil Dispute Resolution Act applies", "statement of claim",
  "entered" and "Admiralty proceeding" are asked.
- **One case.** One proceeding, and the one party asking.
- **The text's terms with plain glosses.** Followed: "offer to compromise" glossed "offer to settle"; "discontinue"
  glossed "drop"; "liquidated damages" glossed "a fixed or calculable sum"; "exemplary" glossed "punitive".
- **Operative rules in; machinery out.** Followed (see Scope).

## Scope

**In:** rr 1.61 (with the Dictionary's "business day" and "file"), 2.25(3), 5.22, 5.23(2), 8.02(1), 8.03(2) item 4 and
(3), 8.05(1), (2), 8.06, 10.32, 16.32, 16.33, 23.21, 25.04, 25.05(3), 25.07, 25.08, 25.09(1), 25.12, 25.13(2) (the
cut-off only), 25.14, 26.01(3), 26.12(2), (4), (7), 26.14, 26.15, 30.41(1), 30.42, 30.43, 35.13, 35.15, 36.03,
36.04(2), 36.07, 36.10, 36.22, 36.24, 39.02, 39.03(2), 39.04, 39.05, 39.06, 40.04, 40.08, 40.13, 40.21, 40.23(4),
40.32(1), 40.33(1), 40.34(4). 49 exported questions.

**Regulative rules:** two. r 16.32 ("A respondent must file a defence ... within 28 days") as `MUST ... WITHIN ... LEST
BREACH ... BECAUSE` naming r 5.22(a), run by EVALTRACE inside "Is the respondent in default?"; and r 25.04 (the sum
offered "will be paid within 28 days after acceptance") as the offeror's `MUST`, `LEST BREACH` naming rr 25.09 and
25.10, run inside "Can I withdraw my acceptance?". Both exported questions take plain dates only. The other periods
are permissions or periods for a single act and are computed as last days.

**Out, and why:**
- Part 1 except r 1.61, Part 3 (Registrars), Part 4 (lawyers), Part 6 (vexatious proceedings, devices,
  livestreaming), Part 43 and the Schedules' forms: machinery.
- Part 2 except r 2.25(3): lodging mechanics, custody of documents, money in Court.
- Division 5.1 (directions), r 5.21 and r 5.23(1) (orders sought against a defaulting applicant: the respondent's
  side), Division 5.3.
- Part 7 (preliminary discovery, freezing and search orders, approval of a settlement for a person under a legal
  incapacity): pre-action orders, all the Court's discretion. Division 7.2 matters to child and incapable claimants
  and is the first candidate for a further layer.
- Part 9: Division 9.3 (class actions under Part IVA) is already in the Federal Court of Australia Act baseline, which
  hand-works rr 9.33, 9.34 and 36.03; the rest (joinder, partnerships, business names, litigation representatives)
  are party mechanics.
- Part 10 except r 10.32, Parts 11-15: how to serve, service abroad, address for service, submitting notices,
  jurisdiction challenges, preservation of property, cross-claims.
- Part 16 except rr 16.32, 16.33: the content of pleadings, particulars, amendment.
- Parts 17, 18, 20-22, 24, 27-29: interlocutory applications, interpleader, discovery, interrogatories, admissions,
  subpoenas, transfer, ADR, evidence: procedure without a date, number or consequence the claimant can compute.
- Part 19 (security for costs): the respondent applies; r 19.01(3) lists what its affidavit "should state", with s 56
  of the Act deciding; nothing to compute.
- Division 23.1, 23.2 (court and party experts): content of reports.
- rr 25.01-25.03, 25.05(1), (2), (4), 25.06, 25.09(2), 25.10, 25.11, 25.13(1): form and confidentiality of offers,
  enforcement of an accepted offer (applications to the Court), offers between contributor respondents (the
  respondents' side; only the cut-off day is shared).
- r 26.01(1), (2), (4), (5), r 26.11, r 26.13: grounds and effect of summary judgment (the Court's), withdrawal of a
  plea, service of the notice.
- Part 30 except Division 30.4, r 30.44: trial management; r 30.44 is an application with no condition beyond "no
  notice", noted in the r 30.42 question.
- Chapter 3 (judicial review, taxation and tribunal appeals, Fair Work, human rights, native title, intellectual
  property): special classes of proceeding whose time limits sit mainly in their own Acts (for example the Fair Work Act
  2009 and the Australian Human Rights Commission Act 1986, which have baselines of their own).
- Part 35 except rr 35.13, 35.15; Part 36 except rr 36.03, 36.04(2), 36.07, 36.10, 36.22, 36.24; Part 38: forms,
  service methods, appeal books, the Court's case management. Extensions of time (rr 35.14, 36.05, 36.23) are the
  Court's and are named in the questions.
- Part 39 except rr 39.02-39.06: entry and authentication of orders, consent orders, undertakings.
- Part 40 except the rules above: contents of a bill, the conduct of taxation, short form bills (Corporations and
  migration), maximum costs orders (r 40.51; the Court's).
- Part 41 (enforcement), Part 42 (contempt): after judgment and outside the claims focus.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind`
tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: r 5.22 (read as a definition, F6); r 25.08(1) "must not be less than"; r 25.08 outside the time
  stated, after judgment or once withdrawn; r 25.07 within 14 days without leave or a better offer ("only if"); r 25.09
  "if" (a) and (b); r 26.12(7) "unless"; rr 26.15, 39.03(2) "if"; r 30.41 "if"; r 36.10 outside its 28-day period;
  rr 39.04, 39.05 "if" (F17); r 40.08 "if" and "other than" Admiralty (F18); r 40.13 "until"; r 40.33 "unless";
  r 23.21(4) before a request (F9); rr 8.02, 8.03(2) with the condition unmet (F4).
- `NOTHING`: r 23.21 outside subrule (1) (scope limit); a duty to attend on a notice alone (silent, F8); an expert who
  is not a "medical expert" (grant's wording); expenses and the report for an examination on the Court's order alone
  (silent); r 25.07 after the 14 days (silent, F12); r 40.33 for a party who did not object (scope limit).
- The date questions return a date, and the enumerated questions a value of the text's own list; where a rule's
  conditions fail, the enumeration says so in words ("rule 25.14 does not apply", "no order on default ...").

## Forks

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | Dictionary "business day" | `is a business day` | Not Saturday, Sunday, 1 Jan, 26 Jan, 25 Apr, 25 or 26 Dec; no substitute days, no Easter or State holidays, no Registry closures | The full public holiday list of the place, by year (not deposited); answers can be a day early near other holidays |
| F2 | rr 8.06, 26.01(3) "at least n days before" | `r 1.61 -- the last day at least n days before` | The act's own day is the nth counted day before the hearing, the hearing day not counted | n clear days, so one day earlier |
| F3 | r 1.61(4)(b) "may only be done on a ... business day" | `the last day to file` | Filing (r 2.25(3)) and giving a notice to a Registrar are business-day acts, so a last day on a non-business day moves on | Electronic lodging any day is "doing" the act, so no move |
| F4 | rr 8.02(1), 8.03(2) "if ... must" | `r 8.02 -- ...`, `r 8.03(2) -- ...` | Condition unmet: JUST FALSE (the rule imposes nothing) | NOTHING (the rule is silent outside its condition) |
| F5 | Division 10.1 | `r 10.32 -- the day I am taken to be served` | Personal service is service on the day of handing over | Division 10.1 timing rules not encoded |
| F6 | r 5.22 "is in default if" | `r 5.22 -- the respondent is in default` | A definition: no head met, JUST FALSE | An open "if": NOTHING |
| F7 | r 5.22(a) "to do an act in the time required" | `rr 5.22(a), 16.32 -- ...` | A defence filed late leaves the respondent in default | Default ends when the defence is filed |
| F8 | r 23.21(2) "a notice requesting" | `r 23.21 -- I must submit to the examination` | NOTHING on a notice alone | An implied duty to attend on notice |
| F9 | r 23.21(4) "on request" | `r 23.21(4) -- ...` | Not yet requested: JUST FALSE | NOTHING |
| F10 | rr 25.04, 25.05(3), 25.07, 25.08(1) | offer periods | r 1.61, including the Christmas break, applies to these periods "fixed by these Rules" | They are terms of the offer, counted in plain days |
| F11 | r 25.08(1) a stated time under 14 days | `r 25.08 -- I can accept the offer` | Read up to the earliest lawful closing day | The notice is defective and the offer open until judgment |
| F12 | r 25.07 after 14 days | `r 25.07 -- I can withdraw my offer` | NOTHING (the rule is silent) | Free withdrawal after day 14; or none before a stated closing day |
| F13 | rr 25.12, 25.13(2), 25.14 | cost cut-offs | Plain days (r 25.12) and business days in the rule's words (r 25.14), without r 1.61(5) | r 1.61 applies to these too |
| F14 | rr 35.13, 36.03 "within 28 days ... or on or before a date fixed" | appeal deadlines | Either satisfies: the later of the two | A fixed date replaces the default period even if earlier |
| F15 | r 36.03(a)(ii) | `r 36.03 -- ...` | For an appeal by leave the 28 days run from the grant of leave | From whichever of (i) and (ii) is later |
| F16 | r 39.02 | `r 39.02 -- ...` | r 1.61(4) not applied: not every ordered act is a business-day act | Move a non-business last day on |
| F17 | rr 39.04, 39.05 | `rr 39.04, 39.05 -- ...` | Out of time and no ground: JUST FALSE under these rules | NOTHING, since r 39.04(5) keeps other powers |
| F18 | r 40.08 "other than in a proceeding under the Admiralty Act 1988" | `r 40.08 -- ...` | JUST FALSE | NOTHING (scope limit) |

## What the Rules turn out to say

1. **A 5-day period can end after a 6-day period from the same day.** r 1.61(3) leaves out non-business days only for
   periods of 5 days or less. From Friday 6 November 2026, 5 days end Friday 13 November and 6 days end Thursday 12
   November. Asserted.
2. **The Christmas break stretches money deadlines.** r 1.61(5) applies to any "period of time for doing an act or
   thing fixed by these Rules"; r 25.04 fixes the 28 days for paying an accepted offer, so an offer accepted on 10
   December 2026 need not be paid until 29 January 2027 (F10). Asserted.
3. **A judgment exactly as favourable as an unaccepted offer has no r 25.14 consequence.** Subrule (1) needs "less
   favourable" and (3) "more favourable". Asserted for both offerors.
4. **r 25.14(2) asks about reasonableness, r 25.14(1) does not.** An applicant who refuses a respondent's offer and
   then wins less loses costs automatically; one whose claim is dismissed pays only if the refusal was unreasonable.
   Asserted.
5. **Withdrawing an offer after 14 days is not dealt with.** r 25.07 restricts withdrawal "within 14 days"; nothing
   says whether an offer stating a later closing day may be withdrawn after day 14 (F12). Answered NOTHING.
6. **A medical examination notice is only a request.** r 23.21(2) lets a party serve a notice "requesting" an
   examination; the duty to cooperate in (7) attaches only to a Court order, and no sanction for ignoring a notice is
   stated (F8). Answered NOTHING.
7. **"File" means "file and serve", yet r 35.15 gives 2 more days to serve.** The Dictionary makes every filing period
   a service period too; r 35.15 then allows service of a leave application "within 2 days of filing". Encoded as the
   text says; the two readings are not reconciled.
8. **Discontinuance without leave is gone on the day of the first directions hearing.** r 26.12(2)(a)(i) says "before
   the earlier of" the two hearings, so on that day itself consent or leave is needed. Asserted.
9. **Thresholds are strict.** r 40.08 "less than $100 000" excludes an award of exactly $100 000; r 40.33 "more than
   115%" and "less than 85%" leave an objector who lands exactly on either line paying the costs of taxation. Asserted.
10. **r 39.06's "6% above the cash rate"** is read as six percentage points, the usual reading; the text does not say.

## Before relying on it

- Supply real public holidays and Registry closures (F1): the business-day answers near Easter, State holidays and
  substitute days can be wrong by a day or more.
- A lawyer to confirm the forks, especially F2, F3, F7, F10 and F14, which move deadlines by a day or more.
- An independent test pass, and the human gates HG1 and HG2.
- Further layers: Division 7.2 (settlements for children and incapable persons), Part 19 security for costs with s 56
  of the Act, and Part 41 enforcement.

## Licence

The L4 is Apache-2.0. The quoted text is (c) Commonwealth of Australia, CC BY 4.0: "Based on content from the Federal
Register of Legislation". See `SOURCE-LICENSE.md`.
