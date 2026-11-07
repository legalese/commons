# Health Care Complaints Act 1993 (NSW) -- baseline encoding, the complainant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 31 May 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the Commission's
assessment within 60 days, s 22; its written notice of the assessment decision within 14 days, s 28(1)), each run by
`EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except
in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a person bringing a
complaint about health care meets. The Act is mid-sized (about 173,000 characters); Part 2 (complaints) is encoded
nearly whole as far as it reaches the complainant, with the Part 7 protections and offences, and the rest is listed
under Scope with reasons.

## Edition

- **Act:** Health Care Complaints Act 1993 No 105, corpus document `nsw_legislation:2024-05-31/act-1993-105` (in force
  31 May 2024), deposited at `../../registers/source-bundle/act-1993-105.txt` (text sha256 65951a02...68187710, as its
  meta records), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Health Care Complaints Regulation (prescribed health services, s 4(l); organisations excluded
  from "relevant health organisation", s 4(d); modifications for the Commissioner's own complaints, s 8(3)); the
  Crimes (Sentencing Procedure) Act 1999 s 17 (the dollar value of a penalty unit); the Health Practitioner Regulation
  National Law (NSW); the Public Health Act 2010 Part 7. What they decide is asked as a fact, or the answer is given in
  penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hcc-dates.l4` | 0 | 0 | 0 | 0 |
| `hcc-complaints.l4` | 0 | 0 | 0 | 0 |
| `hcc-cases.l4` | 0 | 0 | 208 | 208 |

Every expected value was worked by hand from the text, with the edges: the 60th day of the assessment and the 61st,
from receipt and from the day set for further particulars, across a leap February, and at the widest reach of s 21
(particulars required on the 60th day for 60 days later: 180 days in all) (s 22); 60 and 61 days allowed for
particulars (s 21); the 14th and 15th day for notice of the assessment decision (s 28(1)), with and without the s 28(4)
excuse; the 28th day and the 29th for asking for a review (s 28(9)); five years to the day before the complaint and one
day more, and from 29 February (s 27(1)(f)); each s 23(1)(b) limb alone; each s 27(1) reason alone, with s 27(3) and
s 25A(2) against them; every route through s 28A; each consent missing alone under s 91A(5); each offence's penalty.

The two periods the regulative rules use (60 days, s 22; 14 days, s 28(1)) are each written once, as
`the days for the assessment (s 22)` and `the days for notice of the assessment decision (s 28(1))`, and used both
after `WITHIN` in the MUST rule and in the questions that give the last day or test whether the time has passed.

## Seat

**The complainant** (s 4): the person who lodges a complaint about a health practitioner or a health organisation, or
the client (the patient) on whose behalf a representative the client chose makes it; with them the client whose
treatment is complained of when someone else complains, and the client's recorded contact or family (s 28A). Every
exported question is one that person would ask ("Can I complain about this?", "Am I the complainant?", "Will the
practitioner be told who I am?", "Can I withdraw?", "By when must the Commission decide, and did it?", "Must it
investigate?", "Can it drop my complaint?", "Can I ask for a review, and by when?", "Must I go to conciliation, and can
I bring a lawyer?", "Can what was said at conciliation be used in my negligence claim?", "Can I be sued for
complaining?", "Was what my employer did to me for complaining an offence?").

The health practitioner or organisation complained about is the other party the Act puts duties on (submissions,
s 40; information, s 21A); a seat for them could be added beside this one. Officials (the Commission, the
Commissioner, the Director of Proceedings, the Registrar and conciliators, the professional councils, the Health
Secretary) get no seat: what they must do is encoded as what the complainant is owed and by when.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets its own periods (14, 28 and 60
  days; five years) and its penalties in penalty units; the dollar value of a penalty unit is set by another Act and is
  not computed.
- **The actors the text names.** Followed: the complainant, the client, the health practitioner, the health
  organisation, the Commission, the professional council, the Registrar and conciliator, the Director of Proceedings,
  the Health Secretary.
- **Judgments answered conditionally.** Followed: what "appears to the Commission" (ss 18(2), 23(1)(b), 27(3)), its
  "reasonable grounds" (ss 16(4)-(5), 16A, 28(4)-(5), 28A(6)-(7)), "sufficient reason" (s 27(1)(e)-(g)), frivolous or
  trivial (s 27(1)(a)-(b)), good faith (s 96(2)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: complainant, relevant health organisation and
  parties to a complaint (s 4) are worked out; "health service" (an open "includes" list), "public health organisation",
  "public hospital", "licensed private health facility", "authorised representative" and the Public Health Act
  offences are asked.
- **One case.** One complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 (complainant, relevant health organisation, parties); ss 7, 8(1), 9 (the right to complain, who, how);
s 11 (complaints made to a council); s 13(1) (with s 23); ss 16, 16A, 17 (who is told of the complaint and the
complainant's identity); s 18 (withdrawal); s 20(2) (confirming the allegations); ss 21, 22 (particulars; the 60-day
assessment); s 23 (must investigate); ss 25A(2), 25B(2), 27 (discontinuance); s 28 (notice of the assessment decision;
the 60-day review of a decision not to give notice, s 28(7); review) except s 28(2), (3), (6) (notice to the
practitioner's employer or facility, a partial form of notice: the Commission's side); s 28A (the client and the
client's contacts, with the s 28A(9) review) except s 28A(5) (the facility's duty to supply information); ss 39(1),
41, 42(1), 45 (outcomes, notice of results, review, the report); ss 41B(3)(a), 45D(3)(a) (a statement of a
prohibition-order or public-statement decision to the complainant); s 90CA (notice of the prosecution decision);
ss 47, 48, 50, 51, 52, 56 (both subsections) and 58D (conciliation and complaints resolution); s 91A(5)-(6) (the
expert's report in other proceedings); s 96(2) (no liability for complaining in good faith); ss 97A(d), 98, 99
(offences touching a complainant) and the penalties of ss 58 and 99A(1); s 99A(2)-(3) (the Commission cannot be
compelled to give evidence).

**Out, and why:**
- **ss 1-3A, 5, 6:** preliminary and explanatory (s 3A(6) says it affects nothing).
- **s 8(2)-(3) (the Commissioner's own complaints), ss 10, 12, 13(2)-(3), 14, 15 (liaison with councils), ss 19,
  20(1), 20A, 21A, 22A, 24, 25, 25A(1), 25B(1), 26 (the Commission's assessment powers and referrals):** the
  Commission's machinery; what they mean for the complainant enters through s 28 (the decision and its review) and
  s 27 (discontinuance after a referral). s 26(2) (must keep dealing after referral) repeats the s 18(2) limbs and is
  noted only.
- **Division 5 (ss 29-38, investigation powers), s 40 (the practitioner's submissions):** the investigation and the
  practitioner's side. s 29A(1) (an investigation "is to be conducted as expeditiously as the proper investigation of
  the complaint permits", particularly where the complainant or the client "is seriously ill") reaches the complainant
  but sets no period, so there is nothing to compute; it is noted only.
- **ss 41A, 41AA, 41B other than (3)(a), 41C-41E, 45A-45C, 45D other than (3)(a), 45E, 45F (prohibition orders):**
  the making of the orders, their contents and their review belong to the Commission and to the practitioner or
  organisation (only they can seek review, ss 41C, 45E). What reaches the complainant is encoded: the outcomes in
  `What can the Commission do at the end of the investigation`, and the complainant's statement of the decision
  (ss 41B(3)(a), 45D(3)(a)) in `Must I be given a statement of the prohibition decision`.
- **ss 43, 44 (the organisation's submissions; implementing the report), ss 46, 49, 53-55, 57, 58A, 58B, 58C:**
  machinery of the Commission and the Registry; s 53(3) (the parties get a copy of the conciliator's report) is noted
  only.
- **Parts 3, 3A (other investigations, compliance), 4 (Joint Committee), 5, 6, 6A except s 90CA (the Commission, the
  Registry, the Director of Proceedings):** machinery.
- **ss 91, 91A(1)-(4), 92-95, 96(1), 97, 97A(a)-(c), 97B, 99A(1) as a question, 99B, 100-104 and the Schedules:** machinery,
  officials' immunity, offences not met by the complainant, savings and transitional (Schedule 3 cl 4, complaints about
  conduct before 1994, is not encoded).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 16(1), 16(7), 21, 22, 27(1)(f), 28(1), 28(7), 28(9), 28A(9), 47 -- every date question -- a period of n days "after" a day
  ends n days later, the day it runs from not counted, and an act on the last day is in time; five years "before" the
  complaint is the same day of the month five years earlier, or that month's last day (29 February back five years is
  28 February) -- the Interpretation Act 1987 (not deposited) might give another reading.
- **F2** s 7(1) -- `Can I make a complaint about this` -- a matter outside (a), (a1) and (b) answers `NOTHING`: the list
  is not closed with "only" and the grant limits itself in its own words -- `JUST FALSE`, reading s 7(1) with the
  definition of "complaint" in s 4 as exhaustive.
- **F3** s 16A(1) -- `Must the practitioner's employer be told ...` -- with no current employer the duty has nothing to
  attach to: `JUST FALSE` -- `NOTHING`.
- **F4** s 18(1) -- `Can I withdraw my complaint` -- a person who is not the complainant (for example the client's
  chosen representative) answers `NOTHING` (a grant limited in its own words, no "only") -- `JUST FALSE`.
- **F5** s 21 "within such time, not exceeding 60 days" -- `Is the time for further particulars within the limit` --
  counted from the day the Commission requires the particulars -- from the day the complainant receives the requirement.
- **F6** ss 23(1), 56(2) -- `Must the Commission investigate my complaint`, `Must the Commission investigate after
  conciliation` -- where no limb holds, `JUST FALSE` (the section does not require it; the Commission may still choose
  to investigate under s 20(1), or under s 56(1) after conciliation) -- `NOTHING`.
- **F7** s 41(3) -- `Must the Commission review its decision after the investigation` -- for a health organisation
  (Division 7) the Act gives no review: `NOTHING` -- `JUST FALSE`.
- **F8** s 50 -- `May this person help me at the conciliation` -- a lawyer may not be the helper: `JUST FALSE` (s 50(1)
  "not entitled to be legally represented", s 50(2) "not being an Australian legal practitioner") -- the Registrar or
  conciliator could still allow it, s 50 saying only that a party is "not entitled".
- **F9** s 98 -- `Was it an offence under section 98` -- conduct outside the words of s 98 answers `JUST FALSE` ("this
  section makes no offence of it on these facts", not "no offence at all") -- `NOTHING`.
- **F10** ss 97A, 99 -- `What is the longest prison term in months` -- where the section's maximum penalty is a fine
  only, 0 -- `NOTHING`, leaving it to general sentencing law.
- **F11** ss 41(1), 45(1), 90CA -- `Must I be told the results of the investigation`, `May the Director of Proceedings
  tell me ...` -- a person who is not a party answers `NOTHING` (the Commission's discretion, ss 41(2), 45(2), 90CA(c))
  -- `JUST FALSE`.
- **F12** ss 99A(3), 91A(6) -- `Can the Commission be compelled to give its information in proceedings`, `Can the
  expert's report be compelled in proceedings` -- in the listed inquiries (s 99A(3)), or in proceedings under the Act
  and disciplinary proceedings under the National Law (s 91A(6)), the bar is lifted but the Act does not say
  production can be compelled: `NOTHING` -- `JUST TRUE`.
- **F13** s 28A(1) -- `Is the Commission to tell me the outcome of the assessment` -- for a deceased or incapable client
  the s 28A(1) duty does not arise ("unless"); the s 28A(6) risk is checked after s 28A(4) -- the risk first.
- **F14** ss 41B(1), 45D(1) -- `Must I be given a statement of the prohibition decision` -- an interim prohibition
  order (ss 41AA, 45B) is not a decision "under section 41A" or "under section 45C", so the duty to give the
  complainant a statement does not arise: `JUST FALSE` (a condition introduced by "if") -- `NOTHING` (the Act is
  silent about telling the complainant of an interim order). A person who is not the complainant answers `NOTHING`
  (as F11: the Commission may make the statement public, ss 41B(3)(c), 45D(3)(c)).

The ruling of 2026-11-05 (c) ("when", "upon" read as "where") is applied to s 17 ("On receiving a complaint against a
health organisation"): a complaint against a practitioner answers `JUST FALSE` for s 17.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 7, s 8(1) | any person | power to complain | `Can I make a complaint about this` |
| s 9(3) | Commission staff | duty to help on request | `Must the Commission's staff help me make my complaint` |
| s 16(1) | the Commission | duty with a deadline (14 days after assessment), excusable | `Must the person I complain about be told ...`, `By what day must the person I complain about be told` |
| s 16A, s 17 | the Commission | duty to tell the employer, the Health Secretary | `Must the practitioner's employer be told ...`, `Must the Health Secretary be told ...` |
| s 18(1) | the complainant | power to withdraw | `Can I withdraw my complaint` |
| s 18(2) | the Commission | duty to continue | `If I withdraw, must the Commission still deal with the matter` |
| s 22 | the Commission | duty with a deadline (60 days) | MUST rule; `Has the Commission assessed my complaint in time` |
| s 23(1) | the Commission | duty to investigate | `Must the Commission investigate my complaint` |
| s 27 | the Commission | power to discontinue; disability (s 27(3)) | `Can the Commission discontinue my complaint` |
| s 28(1) | the Commission | duty with a deadline (14 days) | MUST rule; `Was I told of the assessment decision in time` |
| s 28(9) | the Commission | duty to review if asked within 28 days | `Must the Commission review its assessment decision` |
| s 28(7), s 28A(9) | the Commission | duty to review a decision not to give notice, every 60 days | `When must the Commission first review its decision not to give notice of the investigation` |
| s 41(3) | the Commission | duty to review if asked | `Must the Commission review its decision after the investigation` |
| s 41B(3)(a), s 45D(3)(a) | the Commission | duty to give the complainant a statement of the decision | `Must I be given a statement of the prohibition decision` |
| ss 48, 58D | the parties | privilege not to take part | `Must I take part` |
| s 50 | the parties | no right to a lawyer | `May this person help me at the conciliation` |
| s 51 | everyone | disability: evidence inadmissible | `Can what was said at conciliation be used as evidence` |
| s 52(2) | the complainant | duty to notify without delay | `Must I tell the Registrar about our agreement` |
| s 56(2) | the Commission | duty to investigate on its or the council's opinion | `Must the Commission investigate after conciliation` |
| s 91A(5) | everyone | disability: the expert's report inadmissible in other proceedings without three consents | `Can the expert's report be used in these proceedings` |
| s 91A(6) | the expert, the Commission, the Commissioner | immunity from compulsion | `Can the expert's report be compelled in proceedings` |
| s 96(2) | the complainant | immunity | `Am I protected from being sued for complaining` |
| s 98 | anyone | duty not to | `Was it an offence under section 98` |
| s 99, s 97A(d) | the complainant (and anyone) | duty not to | `Could I commit an offence by what I tell the Commission` |
| s 99A(2) | Commission staff | immunity from compulsion | `Can the Commission be compelled to give its information in proceedings` |

## What the Act turns out to say

1. **A complainant's own lawyer, chosen to make the complaint, is not the complainant: the client is** (s 4(b)). But a
   parent who complains for a child is the complainant (s 4(a)), not the child, and a relative who complains without
   being chosen as representative is the complainant even though the treatment was the client's. The rights to
   withdraw (s 18) and to ask for a review (ss 28(9), 41(3)) follow. Asserted.
2. **The review notice and the review right do not match.** s 28(8)(a) requires the notice to mention a review only
   for decisions not to investigate, to refer, or to discontinue; but s 28(9) lets the complainant ask for a review of
   any "decision made after assessing a complaint", and obliges the Commission to review it if asked within 28 days. A
   decision to investigate (for example, of only some allegations) can be reviewed though the notice need not say so.
   And "not to investigate" sweeps in referrals to conciliation and to complaints resolution. Asserted.
3. **Suing may cost the complaint.** s 97 says legal proceedings do not stop the Commission, but s 27(1)(c) lets it
   discontinue where the subject matter "has been or is the subject of legal proceedings". A patient who starts a
   negligence claim gives the Commission a reason to stop, unless a significant public health issue appears
   (s 27(3)). Asserted.
4. **Two different reviews.** The review of an assessment decision must be asked for within 28 days to be mandatory
   (s 28(9)); the review of the decision after an investigation of a practitioner (s 41(3)) has no time limit. A
   complaint against a health organisation has no review at all after investigation (Division 7 is silent) (fork F7).
   Asserted.
5. **s 39 says "one or more"; s 42 says "or".** After investigating a practitioner the Commission may combine outcomes;
   after investigating an organisation, read literally, it picks one. The encoding lists the options without deciding
   whether they combine.
6. **No duty to tell the complainant whether the practitioner will be prosecuted.** s 41(1) tells the complainant of
   the referral to the Director of Proceedings, but the Director's later determination is notified only if the
   Director chooses (s 90CA "may"). Asserted as a power.
7. **The Commission's file is closed to a later civil claim by compulsion.** s 99A(2) stops anyone being compelled in
   legal proceedings to give evidence of, or produce, information obtained under the Act (outside the s 99A(3)
   inquiries), and s 51 makes conciliation evidence inadmissible without everyone's consent. The expert's report the
   Commission obtains is closed the same way: it may not be admitted or used in any other proceedings, a negligence
   claim included, without the consent of the expert, the complainant and the person complained about (s 91A(5)(b)),
   and the expert, the Commission and the Commissioner cannot be compelled to produce it or give evidence about it
   there (s 91A(6)). So the complainant holds a veto over the report's use, but cannot use it alone: the practitioner's
   consent is needed too. The Commission may still choose to disclose other material to a court or to the client
   (s 99B(1)(b), (i)), in the public interest. Asserted.
8. **Two clocks for one notice.** The person complained about is to be told of the complaint "not later than 14 days
   after the Commission's assessment" (s 16(1)), and the parties are to be told of the assessment decision "within 14
   days after the Commission takes that action or makes that decision" (s 28(1)); s 16(2) folds the one into the other.
   Where the decision follows the assessment by some days, the two deadlines differ. Both are given.
9. **s 21 sets a ceiling with no starting point.** The Commission may set a time "not exceeding 60 days" for further
   particulars, without saying from when (fork F5); s 22(b) then restarts the 60-day assessment from the day set.
   Nor does s 21 say by what point in the assessment particulars must be required. A requirement made on the 60th day,
   for particulars due 60 days later, puts the end of the assessment 180 days after receipt; a requirement made later
   still would stretch it further, though by then s 22(a)'s 60 days would have run. Asserted: received 1 March 2026,
   particulars required 30 April for 29 June, assessment due 28 August 2026 (180 days); and, less extreme, particulars
   specified for 15 May give 14 July (135 days).

## Questions (exported)

`hcc-complaints.l4` (48), in the Act's order: `Is it a relevant health organisation` (s 4); `Can I make a complaint about
this` (ss 7, 8); `Am I the complainant` (s 4); `Has my complaint been made` (ss 9(1), 11); `Must the Commission's staff
help me make my complaint` (s 9(3)); `Must the person I complain about be told of my complaint and who I am` (s 16);
`By what day must the person I complain about be told` (s 16(1)); `When must the Commission first review its decision
not to tell the person` (s 16(7)); `Must the practitioner's employer be told of my complaint and who I am` (s 16A);
`Must the Health Secretary be told of my complaint and who I am` (s 17); `Can I withdraw my complaint` (s 18(1)); `If I
withdraw, must the Commission still deal with the matter` (s 18(2)); `Must the Commission check the allegations with
me` (s 20(2)); `Is the time for further particulars within the limit` (s 21); `By what day must the Commission finish
assessing my complaint` (s 22); `Has the Commission assessed my complaint in time` (s 22, MUST rule); `Must the
Commission investigate my complaint` (ss 13(1), 23); `Did the matter happen more than 5 years before my complaint`
(s 27(1)(f)); `Can the Commission discontinue my complaint` (ss 25A(2), 25B(2), 27); `By what day must I be told the
assessment decision` (s 28(1)); `Was I told of the assessment decision in time` (s 28(1), (4), MUST rule); `Must the
notice tell me I can ask for a review` (s 28(8)); `When must the Commission first review its decision not to give
notice of the investigation` (ss 28(7), 28A(9)); `By what day must I ask for a review of the assessment decision`,
`Must the Commission review its assessment decision` (s 28(9)); `Is the Commission to tell me the outcome of the
assessment` (s 28A); `What can the Commission do at the end of the investigation` (ss 39, 42); `Must I be told the
results of the investigation` (ss 41(1), 45(1)); `Must the Commission review its decision after the investigation`
(s 41(3)); `Must I be given a statement of the prohibition decision` (ss 41B(3)(a), 45D(3)(a)); `Can I have the report on the
health organisation` (s 45(2A)); `May the Director of Proceedings tell me
whether my complaint will be prosecuted` (s 90CA); `By what day must the Registrar tell me about the conciliation`
(s 47); `Must I take part` (ss 48, 58D); `May this person help me at the conciliation` (s 50); `Can what was said at
conciliation be used as evidence` (s 51); `Has the conciliation ended` (s 52); `Must I tell the Registrar about our
agreement` (s 52(2)); `Can the Commission investigate after conciliation` (s 56(1)); `Must the Commission investigate after conciliation`
(s 56(2)); `Can the expert's report be used in these proceedings` (s 91A(5)); `Can the expert's report be compelled in
proceedings` (s 91A(6)); `Am I protected from being sued for
complaining` (s 96(2)); `Was it an offence under section 98`; `Could I commit an offence by what I tell the Commission`
(ss 97A(d), 99); `What is the largest fine in penalty units`, `What is the longest prison term in months` (ss 58, 97A,
98, 99, 99A); `Can the Commission be compelled to give its information in proceedings` (s 99A(2), (3)).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Health Care Complaints Regulation (prescribed services and excluded organisations) and the penalty unit
  value (Crimes (Sentencing Procedure) Act 1999 s 17) to give fines in dollars.
- Have a lawyer review the forks, especially F2 (what can be complained of), F6 (s 23), F7 (no review for
  organisations), F8 (a lawyer as helper) and finding 2 (the s 28(8)/(9) mismatch).
- Link the encoding to the Civil Liability Act 2002 and Health Records and Information Privacy Act 2002 baselines for the
  patient's negligence claim and access to records.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
