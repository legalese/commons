# Uniform Civil Procedure Rules 2005 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 3 February 2025). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the rules are applied, with the design defaults
ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in
its own words; `NOTHING`, or a "not covered" constructor, with a `NOTHING-kind` comment, where it does not answer). Three
time limits are written as regulative rules (`PARTY ... MUST ... WITHIN ... LEST BREACH ... BECAUSE`) and run by
`EVALTRACE` inside exported questions that take only plain facts: service of originating process (r 6.2(4)), the defence
(r 14.3) and payment under an accepted offer (r 20.26(8)). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in
`LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the rules; nothing existing was touched. The rules are very large (59 Parts and many
Schedules, about 1.1 million characters), so the whole instrument is not encoded: the encoding takes the provisions a
claimant meets on the way from filing to judgment and costs (see Scope). The parent Act, the Civil Procedure Act 2005, is
a separate subject (`subjects/au/nsw/civil-procedure-act-2005/`); the time limits for starting a claim are in the
Limitation Act 1969 (`subjects/au/nsw/limitation-act-1969/`).

## Edition

- **Rules:** Uniform Civil Procedure Rules 2005 (2005-418), corpus document `nsw_legislation:2025-02-03/sl-2005-0418`
  (in force 3 February 2025), deposited at `../../registers/source-bundle/sl-2005-0418.txt`, taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text.
- **Facts not in the rules:** which days the registry is closed (weekends, public holidays, the Christmas closure) and the
  Reserve Bank cash rate (r 36.7) are inputs. The cases use illustrative holidays.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; a
deliberately wrong assertion was checked to be reported as failed.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ucpr-time.l4` | 0 | 0 | 0 | 0 |
| `ucpr-proceedings.l4` | 0 | 0 | 0 | 0 |
| `ucpr-offers-costs.l4` | 0 | 0 | 0 | 0 |
| `ucpr-cases-proceedings.l4` | 0 | 0 | 102 | 102 |
| `ucpr-cases-offers-costs.l4` | 0 | 0 | 70 | 70 |

Every expected value was worked by hand from the text (with a calendar for days of the week), with the edges: the last
day of each period and the day after; a last day falling on a Saturday, a Sunday or a holiday; a one-month period from 31
January and a six-month period ending in a leap February; r 1.11(3)'s 5-day rule against a 6-day period; the affidavit
sworn 14 and 15 days before filing; "over 5 months" on the day exactly 5 months later and the day after; an offer made
exactly two months before trial; a closing date 28 and 27 days after the offer; a judgment equal to the offer, one dollar
under and one dollar over; post-offer interest taking a judgment below the offer (r 42.16); judgments of $499,999 and
$500,000, $39,999 and $40,000; claims of $999 and $1,000 in the Local Court.

## Seat

**The claimant**: the plaintiff bringing a civil claim (a personal injury, compensation, debt or other money claim) in a
NSW court. Every exported question is one the claimant would ask ("Until what day can I serve my statement of claim?",
"Is the defendant in default?", "What default judgment can I apply for?", "Must I serve a statement of particulars?",
"If I discontinue, must I pay the defendant's costs?", "What costs order follows the offer?", "Does winning less than
$500,000 in the Supreme Court stop my costs?"). Duties the rules put on the defendant (the defence, payment under an
accepted offer, medical examination expenses) are encoded as what they mean for the claimant. The court gets no seat;
its powers (to dismiss, to extend time, to order otherwise) appear as what may be done to the claimant. A defendant's
seat would be a natural second layer (the same rules from the other side) and is not written here.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed. The rules set their own numbers; the cash rate (r 36.7)
  is a published fact, asked.
- **The actors the text names.** Followed: the plaintiff, the defendant, the offeror and offeree, the court and the
  registry.
- **Judgments answered conditionally.** Followed: whether a closing date is "reasonable in the circumstances" (r
  20.26(5)(b)), whether the court is "satisfied" the offeror was willing and able (r 42.17) or that a higher court was
  "warranted" (r 42.34, 42.35), whether a party "satisfies the court" (r 12.8(3)(c)), leave, special circumstances and
  every "unless the court orders otherwise" are inputs or are stated in the answer.
- **The rules' definitions worked out; borrowed terms asked.** Followed: "in default" (r 16.2), "offer", "period of
  acceptance" (r 20.25) and r 1.11's reckoning are worked out; "liquidated claim", "personal injuries", "step in the
  proceedings" and the registry's closed days are asked.
- **One case.** One set of proceedings, one plaintiff, one defendant (or one offer).
- **The rules' terms with plain glosses.** Followed, in each `@desc`.
- **Operative rules in; machinery out.** Followed (see Scope).

## Scope

**In (the claimant's path):**

- r 1.11 (reckoning of time: the given day not counted; periods of 5 days or less skip closed days; a closed last day
  moves to the next open day), r 1.12 (an extension, taken as an input);
- r 6.2 (commencement; originating process valid for service for 6 months, or one month in most District Court cases;
  fresh proceedings after lapse);
- r 12.1, 12.3, 12.4 (discontinuance and fresh proceedings) with r 42.19 (its costs); r 12.8, 12.9 (dismissal of stalled
  proceedings);
- r 14.3 (28 days for the defence), r 14.4 (reply, 14 days; Local Court only by leave);
- r 15.12, 15.13, 15.14(4), 15.17 (statement of particulars in personal injury and death claims; final statement 42 days
  before the hearing);
- r 16.1-16.10 (default: when the defendant is in default, the judgment available, the 14-day affidavit);
- r 20.25-20.29 (offers of compromise: content, closing date, the 14-day notice, payment within 28 days of acceptance,
  withdrawal of acceptance, judgment or striking out on default);
- r 23.1-23.3 (expenses of a medical examination the defendant asks for);
- r 36.7 (interest rate under s 101 of the Civil Procedure Act 2005; no interest up to judgment in the Local Court below
  $1,000);
- r 42.1 (costs follow the event, as the fallback answer), r 42.13-42.17 (costs consequences of offers), r 42.20 (costs
  on dismissal or striking out), r 42.34, 42.35 (costs where the claim belonged in a lower court).

**Out, and why:** Parts 2-5 (case management, electronic filing, document form, preliminary discovery: addressed to the
court and registry, or form); Part 7 (parties and representation, including tutors for persons under legal incapacity:
large and procedural; a candidate for a later layer); Parts 8-11A (venue, cross-claims, the mechanics of service in and
outside Australia); Part 13 (summary disposal: the court's power); Part 14 except r 14.3, 14.4 and Part 15 except the
personal injury particulars (form of pleadings); Parts 17-19 (admissions, motions, amendment); Part 20 Divisions 1-3
(mediation, arbitration and referees: the court's powers); Parts 21-35 (discovery, interrogatories, the rest of medical
examinations, evidence, subpoenas, affidavits); Part 36 except r 36.7 (judgments and orders: the court's machinery); Parts
37-41 (enforcement: the judgment debtor's seat); Part 42 Division 6 onwards except r 42.34, 42.35 (security for costs and
other costs machinery); Parts 43-59 (interpleader, transfer, specialist lists, appeals, matters under particular Acts);
the Schedules (forms and specialist lists). r 15.12(3)-(7) and 15.13(2) say what the statement must contain; the encoding
says which statement is due and when, not its contents. Interest up to judgment (s 100) and interim payments (s 82) are
in the Civil Procedure Act 2005.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** r 1.11(3), (4) "a day on which the registry is closed" -- every date question -- asked as facts (weekends, and a
  list of other closed days); the search for the next open day stops after 60 days -- weekends assumed closed.
- **F2** r 6.2(4), 12.8, 12.9, 20.26(5) "n months after" -- `plus months` -- the day with the same number n calendar
  months later, or the last day of that month if it is shorter (31 January plus one month is 28 February) -- the first
  day of the next month.
- **F3** r 15.14(4) "at least 42 days prior to the date fixed for hearing" with r 1.11(4) -- `By when must I file my final
  statement of particulars` -- 42 days before; a closed last day moves to the next open day, as r 1.11(4)'s words say,
  even though that leaves fewer than 42 days -- move back to the previous open day.
- **F4** r 6.2(4) validity for service with r 1.11(4) -- `Until when can I serve my originating process` -- r 1.11(4)
  applies to service, though service is not done at the registry -- r 1.11(4) applies only to things done at the
  registry.
- **F5** r 16.3(4) "sworn within 14 days before the date on which the application is filed" --
  `Is my affidavit in support recent enough` -- sworn on the filing day counts -- it must be sworn before that day.
- **F6** r 23.3 "must, on request by the first party, pay" -- `Must the defendant pay my medical examination expenses` --
  no request, `JUST FALSE` -- the duty exists and only its performance waits on a request (`NOTHING`).
- **F7** r 12.1(1) "may ... discontinue ... (a) with the consent of each other active party ..., or (b) with the leave of
  the court" -- `Can I discontinue my proceedings` -- without consent or leave, `NOTHING` (a grant limited in its own
  wording) -- `JUST FALSE`, reading the list as closed.
- **F8** r 42.19(2) "Unless the court orders otherwise or the notice ... otherwise provides" --
  `Must I pay the defendant's costs if I discontinue` -- where either provides otherwise, `NOTHING` (what it provides
  governs) -- `JUST FALSE`.
- **F9** r 12.9(2) "(a) a defence or cross-claim is not filed, or (b) an application for default judgment is not filed,
  or (c) the proceedings are not otherwise disposed of, within 9 months" -- `Can the court dismiss my proceedings for lack
  of progress` -- read as one condition: none of the three happened within 9 months -- the literal "or", under which
  nearly every proceeding qualifies (finding 3).
- **F10** r 12.8 "for over 5 months", "for over 9 months"; r 12.9 "within 9 months" -- the same function -- "over" is
  strict (the day exactly 5 months on is not over); r 1.11(4) is applied to the end of r 12.9's 9 months (a period for
  doing the listed things) but not to r 12.8 (no thing is to be done) -- r 1.11 applied to both, or to neither.
- **F11** r 20.26(2) "must identify ... must not include an amount for costs ... must bear a statement ... must specify"
  -- `Does the offer meet rule 20.26` -- a requirement not met answers `JUST FALSE`: not an offer under r 20.26, so Part 42
  Division 3 does not follow it -- `NOTHING`, leaving the effect of a defective offer to the court.
- **F12** r 20.26(5)(a) "an offer made two months or more before the date set down for commencement of the trial" --
  `What is the earliest closing date for my offer`, `Does the offer meet rule 20.26` -- with no trial date set, (a)
  cannot apply, so (b) "reasonable in the circumstances" governs -- (a)'s 28-day minimum applies whenever the trial is not
  within two months, including when none is set (finding 4).
- **F13** r 16.2(2)(c) "filed a defence after the time limited ... but before a default judgment is given" --
  `Is the defendant in default` -- the question is asked before any default judgment, so a late defence filed by "today"
  takes the defendant out of default; a defence dated after "today" is not yet filed -- a further input for a default
  judgment already given.
- **F14** r 42.14(1), 42.15(1) "no less favourable", "no more favourable" -- `What costs order follows the offer` --
  compared by amount, money offers and money judgments only, after r 42.16's deduction; equal amounts satisfy both
  phrases -- other terms compared as well (they answer "not worked out here").
- **F15** r 42.17(3) "If the court is not satisfied" -- the same function -- only where the offeree made the r 42.17(1)
  request; no request, r 42.14 and 42.15 stand -- the offeror must always show it was willing and able.
- **F16** r 42.14(2)(b) "the day following the day on which the offer was made" -- `From when do indemnity costs run` --
  the next calendar day, not moved by r 1.11(4) (nothing is to be done on it) -- moved to the next open day.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags and follows these rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "if" and "only if" conditions (r 16.2, 16.3(4), 20.26(4), 42.13-42.15A, 42.34, 42.35), flat negatives
("may not", "must not": r 36.7(2), 42.34(2)) and periods the rules fix (r 6.2(4), 14.3, 14.4(3), 20.26(4), (8)) answer
no when they fail; scope limits with no "only" (r 12.8(1), 12.9(1), 14.4, 15.12(1), 16.1, 23.1(1)) answer `NOTHING` (or
the "not covered" constructor); the sites with no convention (a bare "must" not done, "on request", "unless the court
orders otherwise", a grant limited in its own words) each have a fork line above (F6, F7, F8, F11).

## What the rules turn out to say

1. **The corpus version is dated 3 February 2025.** Amendments after it are missing, and the deposited text is not the
   authorised one.
2. **r 1.11(3) makes a 5-day period longer than a 6-day one.** Closed days are left out only of periods of 5 days or
   less, so 5 days after a Thursday ends the next Thursday (weekend skipped), while 6 days after it ends the Wednesday.
   Asserted (13 March against 12 March 2025).
3. **r 12.9(2) read literally lets the court dismiss almost any District or Local Court proceedings at 9 months.** Its
   three limbs are joined by "or": a defence filed means no default judgment application, so limb (b) is met, and any
   proceedings still running meet limb (c). The evident intent is that none of the three happened. Fork F9; the encoding
   takes the intent.
4. **The 28-day minimum closing date in r 20.26(5)(a) needs a trial date.** An offer made before any trial date is set is
   not "two months or more before the date set down", so (b) ("reasonable in the circumstances") governs it. Fork F12;
   asserted (`NOTHING` for the earliest closing date).
5. **r 42.17(3) disapplies r 42.14 and 42.15 but not r 42.15A.** If the court is not satisfied that the defendant was
   willing and able to carry out its offer, the plaintiff loses nothing under r 42.15 but still pays indemnity costs
   under r 42.15A when it loses outright. r 42.17(1) and (4) likewise name only r 42.14 and 42.15. Asserted.
6. **r 42.35 has no defamation exception.** r 42.34 (Supreme Court, under $500,000) excludes defamation proceedings;
   r 42.35 (District Court, under $40,000) does not. Asserted.
7. **r 36.7(1)(a) and (b) give the same formula.** Both half-years are "6% above the cash rate last published ... before
   that period commenced"; the split only fixes which published rate is used. The question takes that rate as an input.
8. **Counting back with r 1.11(4) shortens the period.** "At least 42 days prior to the date fixed for hearing"
   (r 15.14(4)) with a closed last day lets the final statement be filed on the next open day, 41 days before the hearing
   or fewer. Fork F3; asserted.
9. **r 1.11(4) is written for the registry but reaches every "last day".** Service of originating process (r 6.2(4)) and
   payment under an accepted offer (r 20.28(1)(a)) are not done at the registry, yet r 1.11(1) brings every period in the
   rules (and in orders and documents) under r 1.11. Forks F4 and F10; the encoding applies it where there is a thing to
   be done.

## Questions (exported)

`ucpr-time.l4` (1): `What is my last day` (r 1.11).

`ucpr-proceedings.l4` (15), in the rules' order of steps: `Until when can I serve my originating process`,
`Was my originating process served in time` (r 6.2, regulative); `By when must the defendant file a defence`,
`Is the defendant in default` (r 14.3, 16.1, 16.2, regulative); `Is my affidavit in support recent enough` (r 16.3(4));
`What default judgment can I ask for` (r 16.4-16.10); `May I file a reply`, `By when must I file my reply` (r 14.4);
`Must I serve a statement of particulars`, `By when must I file my final statement of particulars` (r 15.12-15.17);
`Must the defendant pay my medical examination expenses` (r 23.3); `Can I discontinue my proceedings`,
`Must I pay the defendant's costs if I discontinue`, `Can I claim the same relief again after discontinuing` (r 12.1,
12.3, 12.4, 42.19); `Can the court dismiss my proceedings for lack of progress` (r 12.8, 12.9).

`ucpr-offers-costs.l4` (10): `What is the earliest closing date for my offer`, `Does the offer meet rule 20.26`,
`Can I give notice that I cannot assess the offer` (r 20.26); `Has the defendant paid under the accepted offer`
(r 20.26(8), 20.28, 20.29, regulative); `What costs order follows the offer`, `From when do indemnity costs run`
(r 42.13A-42.17); `Who pays the costs on dismissal or striking out` (r 42.20);
`Does the lower court costs rule stop my costs order` (r 42.34, 42.35); `What is the interest rate on my judgment`,
`Can the court order interest up to judgment` (r 36.7).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Have a lawyer review the forks, especially F3 and F4 (r 1.11(4) beyond the registry), F9 (r 12.9), F11 (defective
  offers) and F12 (offers before a trial date).
- Encode the personal injury particulars' contents (r 15.12(3)-(7)), Part 7 (tutors for child and incapable claimants)
  and the parent Act's ss 100, 101 (interest) as further layers.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
