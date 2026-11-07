# Health Ombudsman Act 2013 (Queensland) -- baseline encoding, the complainant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except
in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. Five files:

| File | What it holds |
|---|---|
| `hoq-common.l4` | dates and business days (built-in date functions, no daydate), the regulative vocabulary, the two regulative rules (decide-then-tell, ss 35, 49, 50, 278; tell, s 278) and their EVALTRACE helpers |
| `hoq-complaints.l4` | ss 7, 8, 20-23, 31, 32, 34, 35, 35A, 38(2), 39(2), 44, 47-50, 53-56, 278; 14 questions |
| `hoq-outcomes.l4` | ss 35K(3), 71, 84, 85, 90F, 95, 140, 145(4), 149, 150, 232, 261-263A, 264, 275; 10 questions |
| `hoq-cases-complaints.l4` | worked cases for the common and complaints modules |
| `hoq-cases-outcomes.l4` | worked cases for the outcomes module |

The duties with a numbered deadline in business days (s 35(1): decide and tell within 7 business days of receipt; s 49(1)
with s 50: complete the assessment within 22 business days, then tell; s 278(1): tell within 5 business days of a
decision) are regulative rules (`PARTY the health ombudsman MUST decide on day ... WITHIN ... HENCE PARTY ... MUST give
the complainant notice ... WITHIN ... LEST BREACH ... BECAUSE`), run by `EVALTRACE` inside exported questions that take
only plain facts (dates). The decision action carries its day, so the notice rule under HENCE counts its 5 business days
from it and, for s 35, also stops at the end of the 7 business days. The other periods (ss 47, 48, 53-55, 84, 85, 44)
are date arithmetic.

## Edition

- **Act:** Health Ombudsman Act 2013 (Qld), Act No. 36 of 2013 (`act-2013-036`), the version in force from 10 April
  2026, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2013-036.txt` (text sha256
  `6b40976fe42bc5f4fb74aecb49de8cef1f6f8aa28115b9c25ea4eceacb0ef8b7` per its `.meta.json`; a Windows checkout with CRLF
  line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the authorised
  PDF.
- **Numbers set elsewhere:** none needed. The Act's own numbers are used: 7, 5, 10 and 22 business days, 2 years, 1
  year, 3 months, 2 years, and the maximum penalties in penalty units (ss 48(3), 54(3), 150, 262, 263A(2), 264). The
  value of a penalty unit is not deposited, so penalties are stated in units. No Health Ombudsman Regulation is
  deposited; s 7(4)(c) and (5) (services a regulation includes or excludes) are asked as facts.
- **Not deposited and not read:** the Acts Interpretation Act 1954 (Qld), which defines "business day" and governs the
  counting of time; the readings taken are forks F1-F4, F9. The National Law (Health Practitioner Regulation National
  Law (Queensland)), whose terms (registered health practitioner, professional misconduct, notification) are asked as
  facts.

## Checks

Stable `l4` of the L4 VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), from this folder, `JL4_LIBRARY_PATH`
unset, at most two at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `hoq-common.l4` | 0 | 0 | 0 | 0 |
| `hoq-complaints.l4` | 0 | 0 | 0 | 0 |
| `hoq-outcomes.l4` | 0 | 0 | 0 | 0 |
| `hoq-cases-complaints.l4` | 89 | 89 | 0 | 0 |
| `hoq-cases-outcomes.l4` | 70 | 70 | 0 | 0 |
| **Total** | **159** | **159** | 0 | 0 |

Every exported question has cases, with the edges: the last business day and the day after, a weekend receipt, the
Christmas and New Year holidays of 2026-27 supplied and not supplied, the 10-business-day limit and one day over, an
extension over the maximum, the 2-year ground on the day and the day before (and from 29 February), the due day of an
investigation across 29 February 2028, the 1-year and 2-year marks of s 85, each "only if" limb on and off. One `#TRACE`
shows a breach of the s 35 rule (the stable `l4` cannot compare a breached trace with `EQUALS`; the questions use
`CONSIDER ... WHEN FULFILLED`). Expected values were worked by hand from the text and a calendar, never copied from
output.

## Seat

**The person who makes a health service complaint** (the complainant): the person who received the health service, or
a parent, guardian, family member of a person who died, or someone asked to complain for another -- for example a
patient weighing a claim against a practitioner or hospital who first goes to the health ombudsman. "Can I complain
about this? Will it be accepted, and by when must I be told? Is it too old? On what grounds can the ombudsman stop? Can it
go to local resolution or conciliation, where a settlement or compensation can be agreed? By when must I answer a
request, and must I? By when must the assessment, local resolution or investigation be done, and was I told in time?
What must I be told? When can conciliation start, and can what was said there be used in my claim? Was what was done to
me for complaining a reprisal I can sue for? Is my gagging agreement void? Am I protected for what I told the
ombudsman? Can I claim compensation for loss caused by the ombudsman's officers?" For ss 232, 261-263A and 275 the
seat is the person who gives information or is harmed for complaining, who may or may not be the complainant.

No seat is written for the health ombudsman, the director of proceedings, QCAT, Ahpra (the National Agency), a National
Board, the Minister or the parliamentary committee. Their duties appear as what the complainant must be given and by
when. A seat for the practitioner or health service provider (part 7 immediate action, part 8A prohibition orders,
part 8AA public statements, the s 86(3) right to answer adverse comment, the QCAT reviews of s 94(1)(a)) would be a
natural further layer.

The 2026-10-18 defaults:

- **The Act alone.** No instrument sets a number the encoded sections use. The National Law, the QCAT Act and the Acts
  Interpretation Act 1954 are named, not encoded.
- **The actors the text names:** the health ombudsman, the conciliator, the director of proceedings, QCAT, the National
  Agency (Ahpra), the National Boards, the Minister, the parliamentary committee, authorised persons, the State.
- **Judgments handed to others are answered conditionally:** every "is satisfied", "reasonably considers", "believes"
  and "reasonable excuse" is an input; whether a stated period is "reasonable" (ss 47(2), 48(2)) is not decided.
- **The Act's own definitions are worked out from facts:** health service (s 7), health service provider (s 8, in the
  standing choices), health service complaint (s 31), protected action (s 261(7)), non-disclosure agreement and
  relevant person (s 263A(3)), loss (s 232(8)). **Borrowed terms are asked:** registered health practitioner,
  professional misconduct, notification under the National Law, corresponding prior Act, business day (with public
  holidays as a list).
- **One case:** one complaint.
- **The Act's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines and the choices
  (the National Agency is glossed as Ahpra).
- **Machinery out** (Scope).

## Scope

**In:**

- Part 1: ss 7, 8, 20-23 (s 23(1)(a), (2) as a complaint on behalf of a person who died).
- Part 3: ss 31, 32, 34(4), (5) (in the s 35 days not counted), 35, 35A, 35K(3).
- Part 4: ss 38(2), 39(2), 44.
- Part 5: ss 47-50. Part 6: ss 53-56. Part 7: s 71. Part 8: ss 84, 85. Part 8A: s 90F.
- Part 10: s 95. Part 11: ss 140, 145(2), (4), 149, 150 (named in an answer).
- Part 15 division 6: s 232. Part 17: ss 261-263A, 264, 275. Part 19: s 278.

**Out, and why:**

- Part 1 ss 1-6, 9-19 (preliminary and overview: s 15 and s 17 restate ss 84, 85 and 278, which are encoded); Part 2,
  Part 13, Part 14, Part 16 (the ombudsman's office, the Minister, the committee: machinery).
- s 33 (how to complain: orally or in writing, with reasonable assistance on request) -- no question with an answer
  that varies; s 34(1)-(3) (what the ombudsman may ask). Could be added.
- Part 3 divisions 2A and 2B other than s 35K(3) (consultation between the ombudsman and Ahpra: officials; their days are
  the s 35(2)(b) and s 49(3) days not counted, asked as numbers); s 36, s 37 (notifications and referred matters
  dealt with as complaints: s 37(2) needs only the person's agreement).
- ss 38(1), (3), 39(1), 40-43A (the menu of relevant actions and the ombudsman's freedom to combine them).
- Part 7 other than s 71, Part 8A other than s 90F, Part 8AA, Part 10 divisions 1 (other than s 95) to 6 (immediate
  action, prohibition orders, public statements, QCAT's jurisdiction and orders, assessors): the practitioner's seat or
  officials. s 99 (QCAT may exclude a complainant witness until they give evidence) is QCAT's power.
- ss 80-83, 86-90 (the ombudsman's power to investigate and the report: s 87(2) leaves giving the report to the
  complainant to the ombudsman's discretion, so there is no answer for the complainant beyond "may"); Part 9 other than
  s 35K(3).
- Part 11 ss 134-139, 141-144, 146-148 (s 146: the parties "may enter into a contract in settlement", and s 139 the
  duty to negotiate in good faith, are noted in the answers; ss 147, 148 decisions are notified under s 278, encoded).
- Part 12 (inquiries), Part 15 other than s 232 (authorised persons' powers, warrants, seizure, internal review and
  appeal of s 235-244: for a person whose things are seized, a further seat).
- ss 265-271 (fines and offence proceedings; s 269's time limit binds the prosecutor), 272-274, 276 (confidentiality
  duties of officials, publication, privilege of reports), 277, 279-281 (notices to employers and Boards), Part 20 and
  later (transitional and regulation-making).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "business day" (ss 35, 47-49, 53-55, 278; not defined in this Act) -- `is a business day`, `the business day
  after` -- a day that is not a Saturday, Sunday or a public holiday the person lists; "within n business days after" a
  day ends with the n-th business day after it, the day itself not counted -- the Acts Interpretation Act 1954 (Qld)
  definition may also exclude other days (it was not read), and a receipt late in the day might count differently.
- **F2** s 85(1) "1 year ... after the decision", s 85(3) "3 months" -- `n months after` -- 12 months on, the same day
  number or the last day of a shorter month (29 February 2028 plus 1 year is 28 February 2029) -- 1 March, or the Acts
  Interpretation Act rule.
- **F3** s 35(2), s 49(3), s 55(3) "are not counted" -- `s 35 -- the last day to decide and tell me`, `ss 49, 55 -- the
  business days allowed` -- the days not counted are added to the period, as a number the person states -- the days are
  skipped where they fall, which gives the same day only if they fall within the period.
- **F4** s 44(1)(b)(iii) "at least 2 years before the complaint was made" -- `s 44(1)(b)(iii), (2) -- the 2-year ground
  is open` -- met when the complaint is made on or after the day 24 months after the later of the day the matter arose
  and the day the complainant became aware of it (29 February 2024 gives 28 February 2026) -- 1 March 2026; or counting
  to the day before.
- **F5** s 35A -- `s 35A -- grounds for not accepting` -- a list of the grounds open, empty when none is (the section
  does not say its grounds are the only ones, so an empty list is not "the complaint must be accepted") -- s 35(1)(a)(iii)
  is read as limited to the s 35A grounds.
- **F6** s 49(2), s 55(2) "a further period of up to 22 business days" -- `ss 49, 55 -- the business days allowed` -- a
  stated extension of more than 22 counts as 22 -- one extension only is allowed in each case; whether two extensions
  of up to 22 each may be made is not answered (the text says "a further period").
- **F7** s 49(1) "complete the assessment" and s 50 "After completing the assessment, ... decide" --
  `Was the assessment decided and notified in time question` -- the assessment is complete when the s 50 decision is
  made, so the decision must fall within the s 49 period; the s 278 notice then has its own 5 business days (s 35's
  "within 7 business days" for the notice too is not repeated in s 49 or s 50) -- the decision may follow a timely
  completion by any period.
- **F8** s 85(3) "each extension may not be more than 3 months" -- `s 85(3) -- the due day after the extensions` --
  each extension runs on from the due day then current, in whole months, and one stated as more than 3 months counts
  as 3 -- extensions add to the original due day as one total; an extension of more than 3 months is of no effect.
- **F9** s 85(4), (8) "not completed within 1 year [2 years] after the decision" -- `What follows from a long
  investigation question` -- completing on the day 12 (24) months on is within -- the day itself is outside.
- **F10** s 84(1) "at not less than 3 monthly intervals" -- `By when must I get the next progress report question` --
  a report at least every 3 months, so the next is due 3 months after the decision or the last report -- read literally,
  a minimum gap of 3 months between reports (finding 3).
- **F11** ss 71, 90F "If an ... order was issued in response to a complaint" (a condition introduced by "if") -- `Must I
  be told question` -- outside it the answer is no -- the Act's silence about orders issued otherwise.
- **F12** s 261(6) "it is sufficient if the unlawful ground is a substantial ground" -- `Can I sue for a reprisal
  question` -- a ground that is not substantial gives "not shown" (the provision says what is enough, not what is
  needed) -- a ground that is not substantial is not a reprisal.
- **F13** s 275(1) "This section applies to a person who, honestly and on reasonable grounds, gives information" --
  `Am I protected for giving information question` -- outside the condition, "s 275 gives no protection on these
  facts" (ruling of 2026-11-05 (b)), never "no protection at all".

## Rulings on negatives (recorded word for word, as the guide requires)

- **Periods, "where" and scope limits** (ruled 2026-11-05): "(a) a period the text fixes in its own words ...: outside
  the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a
  scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
- **Delegated definitions, defences and "until" bars** (ruled 2026-11-05), (b): "it is a defence ... to prove that X":
  when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence
  on these facts" and never "no defence at all".
- **Questions with no convention: decide case by case** (Meng, 2026-11-05): each such site gets a fork line (F5, F11,
  F12, F13 above).

The questions here return enumerations, not `MAYBE BOOLEAN`: the "no" answers are worded as the rulings direct ("no:
... only ...", "s 275 gives no protection on these facts"), and the silent cases say "the Act does not say on these
facts" or "s 35A gives no ground" rather than "no".

## What the Act turns out to say

1. **"Business day" is not defined in the Act.** Every complaint deadline (ss 35, 47-49, 53-55, 278) is in business
   days, and the definition is in the Acts Interpretation Act 1954 (Qld), not deposited (F1). The person supplies the
   public holidays.
2. **s 31 reaches "other service".** A health service complaint is "a complaint about a health service or other
   service provided by a health service provider", so a service a regulation excludes from s 7 (s 7(5)) can still be
   complained of if its provider provides some health service. Asserted.
3. **s 84(1) "at not less than 3 monthly intervals"** (and s 17(b)) reads literally as a minimum gap between progress
   reports; s 15 and s 17 make plain the scheme is a report at least every 3 months, which is the reading taken (F10).
4. **s 35(1)(b) puts the notice inside the 7 business days.** A decision on the 5th business day, notified on the 8th,
   is within s 278's 5 business days but outside s 35(1). Asserted (decided 10 November 2026, told 12 November).
   Nothing in s 50 or s 56 does the same for the later decisions, so there the notice has the full 5 business days.
5. **s 85(3) extensions compound month-end clamping.** Two 3-month extensions from 30 November 2027 give 29 February
   then 29 May 2028, not 30 May; the text measures each extension from the due day then current. Asserted.
6. **There is no time limit for complaining.** s 44(1)(b)(iii) only lets the ombudsman decide to take no further action
   when the matter arose, and the complainant knew of it, at least 2 years earlier, and s 44(2) takes even that away
   where professional misconduct or a ground for suspension or cancellation may exist. The awareness that counts is the
   complainant's, which for a complaint made for someone else (a parent, a family member of a person who died) is not
   the patient's.
7. **s 39(2) leaves withdrawal and local resolution or conciliation open.** It keeps every other power alive after a
   complaint is withdrawn, excepting these two, but no provision says they end. Answered "the Act says nothing more".
8. **s 56 and s 50 set no period for the decision itself** after local resolution fails or an assessment completes;
   only the s 278 notice has a deadline once the decision is made (F7).
9. **Drafting slips.** s 23, example 2, speaks of a "health service practitioner", a term the Act does not use or
   define (it means a health practitioner). s 81(3) says the ombudsman "must comply with the request", but s 81(1) is
   a direction. Neither changes an answer.
10. **s 140(2)(b)** lets conciliation start after immediate action at "the time that conciliation may start under
    subsection (3) to (5), whichever is relevant to the action taken ... after taking the immediate action": it is one
    input here ("the action's end point has been reached").
11. **s 149(3)** makes conciliation statements inadmissible even "in a proceeding to enforce a contract mentioned in
    section 146" -- the settlement contract must be proved by its own terms, without what was said in reaching it,
    unless everyone consents (s 149(4)).

## Before relying on it

- Read the Acts Interpretation Act 1954 (Qld) for "business day", the counting of days, months and years, and settle
  F1-F4 and F9.
- Have a reader check F5-F8 and F10-F13, and the wording of each answer, against the text.
- An independent test pass (cases written by someone who has not seen the encoding).
- A practitioner or provider seat, if wanted, as `hoq-seat-provider.l4` over a rule module for parts 7, 8A and 8AA.
