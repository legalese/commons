# Interpretation Act 1984 (Western Australia), whole-Act encoding with a seat layer

Row `legalese-sonnet-5.5` (subject `au/wa`, Act No. 12 of 1984).
Encoder: Claude Sonnet 5.5, working alone, no subagents.
Status: draft.
Not reviewed: no domain expert has read this encoding against the text.
Every expected value was written by the encoder from the text of `../../registers/source-bundle/mrdoc_49111.txt`.
An independent test author, who had not read this file, ran 565 assertions against the first version (the lead's report: 557 satisfied, 8 failed because the encoding answered NOTHING, 0 refused, 34 gaps); the encoder did not see those assertions.
This version answers the fix list that came out of that pass; the changes are under "Changes to existing modules".
Target compiler: `main`.
Written with `l4 1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
`check.sh` compared every module with `1.6.102 (main, e4f2553, 2026-10-26)`.
The numbers below are a point-in-time record of one run on 2026-10-29; nothing re-runs them.

The text is a converter's plain-text rendering of the WA Legislation website's compilation, not the official text.
The edition encoded is the one that notice (State of Western Australia 2025) describes: the last row of its compilation table is the Legal Profession Uniform Law Application Act 2022 Pt. 17 Div. 10 (assented 14 Apr 2022, commenced 1 Jul 2022), and its uncommenced table lists one provision, of the Assisted Reproductive Technology and Surrogacy Act 2025 (Pt. 17 Div. 12), to be proclaimed.
Citations `src:N` are line numbers of that rendering.
The body and the index at the end of the text disagree on hyphenation: the body reads "public halfholiday", "ValuerGeneral" and "bylaw" where the index reads "public half-holiday", "Valuer-General" and "by-law"; the body also reads "firstmentioned" and "reenacts".
The cause is not known (a converter artefact is a guess); the encoding follows the body text, and the index rows are inert.

Layout: layer 1 is the whole Act as modules in the Act's order, each rule quoting its words above it as `-- src:N | ...` lines and citing them with `@ref`.
Layer 2 is `wa-seat.l4` and `wa-cases-seat.l4` and nothing else; they import layer 1 and call its rules, and no layer-1 module changes to suit them.

## Seat

The seat is a person who has a time limit to meet under a Western Australian Act (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.

Why this seat.
The Interpretation Act is the Act every other Western Australian Act is read through, and the part of it an individual meets is its clock: how a period of days, months or years is counted, which days do not count, when an Act or regulation begins, what happens when a deadline is missed, and when a posted document is taken to have arrived.
The seat is the position of the person the law is applied to.
There is no seat for an official.
Provisions that address only an official (the Governor's powers, the quorum of a board, delegation) are encoded in layer 1 for what they decide, and appear in layer 2 only for what they mean to the person: whether a decision made by an acting officer or by a bare majority stands, whether a vacancy invalidates it, whether the authority is free to refuse, whether a right of appeal survives.

Layer 2 has 32 exported questions in the Act's order under `§§` groups.
Four groups arise only in a situation the person may not be in (a provision they rely on being repealed, regulations that affect them, a conviction for a continuing failure, an Act passed before 1 July 1984 that adopts the 1918 Act's Second Schedule), and a comment under each heading says so, so a form can ask "Has this happened to you?" first.
Every question takes plain inputs (yes or no, a number, a date, a list of dates, or the modules' own short choices), each with an `@desc` worded as the person would be asked.
Holidays are two lists of dates, because that is how a person knows them; the Act treats a public holiday, a bank holiday and a public service holiday alike (s 61(2)), so which list a date sits on changes no answer.
The Act's own figures (1 July 1984, 28 days, 21 days, the $1000 and $50 amounts) are used as the Act states them.
Where the text does not answer the facts given, the question returns NOTHING, and a case asserts it.
`wa-cases-seat.l4` has 109 assertions, at least one per question, including the seven worked cases and the cases that return NOTHING.

## What is encoded and what is not

Encoded: every section, subsection, paragraph, defined term, and the text of notes 1 and 4 (section 11 of the Interpretation Act 1918, and section 47 and the Second Schedule of that Act, kept alive by s 77(2) and (4)).
The coverage table below has one row for every one of the 790 units found in the 1105 non-blank lines of the text, each with exactly one disposition.
There is no out-of-scope row and no deferred row.

Modules, in reading order (each `wa-tests-*.l4` file is the tests for the module with the matching name; the three test files added in pass 2 are named in the rows they belong to):

| file | holds |
|---|---|
| `wa-interpretation-time.l4` | all the time rules, in one module that imports only `prelude` and `daydate`: ss 2, 3(3), 5 (year, month, financial year), 20-23, 25(3), 27, 41(1)(b) and (2), 48A, 61, 62, 63, 64, 75(1), and the Second Schedule sections B to E of the 1918 Act (s 77(4)); since pass 2 also the other reading of s 61(1)(c) with (e) (fork F3), tested with fork F13 in `wa-tests-time-forks.l4` |
| `wa-interpretation-nouns.l4` | the one type the part modules share |
| `wa-interpretation-part1.l4` | ss 3(1), (2), 4 |
| `wa-interpretation-part2.l4` | ss 6-19, including the section-local definitions in ss 13, 13A, 13C, 13CA, 13D, 15A, 17 |
| `wa-interpretation-part3.l4` | ss 25(1), (2), (4), (5), 26 |
| `wa-interpretation-part4.l4` | ss 28-32 |
| `wa-interpretation-part5.l4` | ss 33-39 |
| `wa-interpretation-part6.l4` | ss 40-47, including the sitting-day arithmetic of s 42; the constituents of the s 45A(4) lists are tested in `wa-tests-part6-45a4.l4` |
| `wa-interpretation-part7.l4` | ss 48-60 |
| `wa-interpretation-part8.l4` | s 65, distance |
| `wa-interpretation-part9.l4` | ss 66-72 |
| `wa-interpretation-part10.l4` | ss 73-77 and notes 1 and 4 |
| `wa-interpretation-s5-definitions.l4` | the 106 terms defined in s 5, one entry each, and a lookup; a term defined by `means` stores the meaning as printed and, for a pair of alternatives, each constituent (tested in `wa-tests-s5-meanings.l4`) |
| `wa-seat.l4`, `wa-cases-seat.l4` | layer 2 |

Not encoded, and why: nothing is out of scope, but several things are borrowed facts the person or caller must state, because the Act points outside itself.
The public holidays and bank holidays of an area (the Public and Bank Holidays Act 1972) and the public service holidays (the Public Service Act 1978) are lists of dates the caller supplies.
Sitting days of a House (s 42) are a list the caller supplies.
How long the ordinary course of post takes (s 75(1)) is a date the caller supplies.
The commencement day of the Australia Acts (s 76A) and of the Interpretation Act Amendment Act 1975 (note 1) are not in the text, so each is a yes or no the caller supplies.
Whether a deviation "materially" affects the substance (s 74) and whether a power is "reasonably necessary" (s 50(1)) are plain inputs, not answered.
Meanings that live in another Act (chief executive officer, alternative offence, the Corporations Law, and so on) are table entries that name the Act and the provision; the encoding does not reproduce them.

The time module is the answer to "other encodings need executable answers from this Act".
Its functions each cite their section with `@ref`, take a `Holidays that make an excluded day` record, and return `MAYBE` where the Act is silent.

## Jural relations

Hohfeld's correlatives: a claim answers a duty, a privilege a no-right, a power a liability, an immunity a disability.
The table has one row for each provision that creates such a relation; every other section, subsection, note and schedule row of the text is listed once in the last row as `none`.
The rows the coverage table marks inert (title, contents, headings, history notes, the compilation and uncommenced tables, the index of defined terms, the copyright notice) create no relation either, so the table covers the whole text.
In an interpretation Act most provisions create no relation: they define a word, say how to read a phrase, or count a period.

| provision | holds the right, privilege, power or immunity | bears the duty, no-right, liability or disability | relation | L4 rule |
|---|---|---|---|---|
| s 4: every Act binds the Crown | any person who has a claim under an Act | the Crown (a duty to comply) | claim / duty | wa-interpretation-part1.l4 `the Crown is bound by this Act` |
| s 25: powers exercisable before an Act's provision commences; instruments made early | the person the Act empowers to make an instrument, give a notice, appoint or establish a body | those the instrument, notice or appointment affects (a liability); the maker has a disability: an instrument made early takes effect no earlier than the commencement day (s 25(3)) | power / liability; disability | wa-interpretation-part3.l4 `the power may be exercised before the provision commences`; wa-interpretation-time.l4 `the day an instrument or notice made early takes effect` |
| s 36: things in existence under a repealed and re-enacted provision continue | the body, office-holder or document that existed at the commencement of the repealing law (an immunity from lapse) | the repealing law (a disability: it cannot end them by repealing) | immunity / disability | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` |
| ss 37 and 39: repeal or expiry does not affect accrued rights, liabilities, penalties and proceedings | the person with a right, interest, power, privilege or status accrued before the repeal (an immunity); the State with an accrued proceeding or penalty (a power to continue it) | the repealing law (a disability); the person under an accrued duty or liability, who stays bound | immunity / disability; power / liability; claim / duty | wa-interpretation-part5.l4 `the repeal affects`, `it may still be instituted, continued, enforced or imposed as if the repealing law had not been passed or made`, `the expiry or lapse of an enactment affects` |
| s 38: subsidiary legislation continues after its Act is repealed and re-enacted, and may be amended | the person who relies on the continuing subsidiary legislation (a claim); the repealing Act's rule-maker (a power to amend or repeal it) | those subject to it (a duty, and a liability to its amendment) | claim / duty; power / liability | wa-interpretation-part5.l4 `the subsidiary legislation continues in operation as if made under the repealing Act`, `the continuing subsidiary legislation may be amended or repealed as if made under the repealing Act` |
| s 40: the Governor makes subsidiary legislation | the Governor, or the person the written law names (a power) | those subject to the subsidiary legislation (a liability) | power / liability | wa-interpretation-part6.l4 `who makes the subsidiary legislation` |
| s 42(1): regulations are laid before each House | each House of Parliament (a claim that they be laid within 6 sitting days) | the maker of the regulations (a duty to lay them) | claim / duty | wa-interpretation-part6.l4 `the last day for laying the regulations before the House` |
| s 42(2), (3): a House may disallow regulations | either House (a power to disallow, on notice within 14 sitting days after they are laid) | the regulations and their maker (a liability: they cease to have effect) | power / liability | wa-interpretation-part6.l4 `the last day for giving notice of a resolution disallowing the regulations`, `the regulations cease to have effect` |
| s 42(4): both Houses may amend or substitute regulations | both Houses together (a power) | the maker and those subject to the regulations (a liability) | power / liability | wa-interpretation-part6.l4 `the first day the amended or substituted regulations take effect` |
| s 42(5): notice of a resolution is published within 21 days | not named by the text | not named by the text (the Act does not say who must publish) | duty / claim; both parties unnamed | wa-interpretation-part6.l4 `the last day for publishing notice of the resolution` |
| s 43(1): inconsistent subsidiary legislation is void to the extent of the inconsistency | the person subject to it (an immunity from the inconsistent part) | its maker (a disability) | immunity / disability | wa-interpretation-part6.l4 `the subsidiary legislation is void to the extent of the inconsistency` |
| s 43(4), (7), (8): the power to make includes the power to amend, repeal and to vary the way it is used | the maker of subsidiary legislation (a power) | those subject to it (a liability) | power / liability | wa-interpretation-part6.l4 `the power includes a power to amend or repeal the subsidiary legislation, in the like manner and on the like conditions`, `the power may be exercised` |
| s 43(6): a fine under regulations, rules, local laws or bylaws is at most $1000 | the person subject to the subsidiary legislation (an immunity from a larger fine) | the maker (a disability: it cannot fix a larger fine) | immunity / disability | wa-interpretation-part6.l4 `the most a fine may be under regulations, rules, local laws or bylaws` |
| ss 45, 45A: fees and charges | the maker (a power to provide for fees, their reduction, waiver or refund; to prescribe a licence fee covering the costs of the scheme) | those who pay or are excused (a liability) | power / liability | wa-interpretation-part6.l4 `subsidiary legislation may provide for`, `a power to prescribe a fee allows it to recover the expenditure` |
| s 48: a power may be exercised from time to time | the holder of a power (a privilege to use it again) | those it affects (a no-right to object that it was used before) | privilege / no-right | wa-interpretation-part7.l4 `the power may be exercised and the duty performed from time to time as occasion requires` |
| s 48A: judicial acts and service of process on any day | the person who acts judicially, serves a document or process, or executes a warrant (a privilege to do so on a Saturday, Sunday or public holiday) | the person it is done to (a no-right to object to the day) | privilege / no-right | wa-interpretation-time.l4 `the power may be exercised on` |
| s 49: an acting officer may exercise the office's powers | the person holding, acting in or performing the functions of the office (a power) | those subject to the power (a liability) | power / liability | wa-interpretation-part7.l4 `the person may exercise the power and must perform the duty of the public office` |
| s 50: powers reasonably necessary, and the powers a power includes | the holder of the power (a power) | those it affects (a liability) | power / liability | wa-interpretation-part7.l4 `the other power is also deemed conferred`, `the power includes the other power` |
| s 51(1): a power to issue or refuse a licence or permit is discretionary | the authority (a privilege to grant or to refuse) | the applicant (a no-right to a grant) | privilege / no-right | wa-interpretation-part7.l4 `the person empowered has a discretion to grant or to refuse` |
| s 51(2): a right of appeal or review of a refusal is left in place | the applicant, where another written law gives a right to appeal, apply or seek review (a power; this section creates none) | the appeal or review body (a liability) | power / liability; the section creates none | wa-interpretation-part7.l4 `the right to appeal against or seek review of a refusal is left in place` |
| s 52: a power to appoint includes removal, suspension, acting appointment and period; acting appointee's acts are not open to challenge on the ground the occasion had not arisen | the appointing authority (a power); the person dealing with an acting appointee, and the appointee (an immunity from challenge, s 52(3)) | the appointee (a liability); anyone who would challenge (a disability) | power / liability; immunity / disability | wa-interpretation-part7.l4 `a power to appoint includes the power`, `the validity of the thing done can be called in question on that ground` |
| s 53: an appointment may be by name or by office | the appointer (a power to appoint by office) | the person who holds the office from time to time (a liability) | power / liability | wa-interpretation-part7.l4 `the appointment is of the person from time to time holding, acting in, or performing the functions of the office` |
| s 54: majority and quorum of a statutory body | a majority of the members (a power to act for the body; the quorum, the power to act as the association) | the members in the minority and those the body's act affects (a liability) | power / liability | wa-interpretation-part7.l4 `the function may be performed by those who agree`, `the act is deemed done by the association` |
| s 55: an administrative or executive power may be used again to correct an error | the power-holder (a power to correct) | those the act affects (a liability) | power / liability | wa-interpretation-part7.l4 `the power or duty may be exercised again as often as is necessary to correct an error or omission` |
| s 56: may confers a discretion; shall imposes a duty | for may: the power-holder (a privilege to exercise or not); for shall: the person the function benefits (not named by the text, a claim) | for may: others (a no-right); for shall: the function-holder (a duty) | privilege / no-right; claim / duty | wa-interpretation-part7.l4 `what the word means` |
| s 57: a body's powers are not affected by vacancies and minor irregularities | the body (an immunity) | anyone who would challenge its act on those grounds (a disability) | immunity / disability | wa-interpretation-part7.l4 `the powers of the body are affected by` |
| ss 58, 59: delegates perform functions, and delegations | the delegator (a power to delegate, to amend and revoke, and to act still); the delegate (a power on the delegate's own opinion) | the delegate (a liability to the delegator's conditions); those affected (a liability) | power / liability | wa-interpretation-part7.l4 `whose opinion, belief or state of mind counts`, `a delegation has the feature`, `the act is regarded as effectually done` |
| s 60: the Governor acts with the advice and consent of the Executive Council | the Executive Council (a power of consent) | the Governor (a disability: cannot act without it) | power / disability | wa-interpretation-part7.l4 `it is done by the Governor with the advice and consent of the Executive Council` |
| s 61(1)(e), (h): a time that ends on an excluded day, or an act directed for one, may be met on the next day that is not | the person who has the time limit (a privilege to act on the next day that is not an excluded day) | the authority or other party (a no-right to treat that act as late) | privilege / no-right | wa-interpretation-time.l4 `the next day that is not an excluded day, counting the day itself` |
| s 63: where no time is fixed, an act is done with all convenient speed and as often as occasion arises | not named by the text (the person for whose benefit the act is required) | the person who must act (a duty) | claim / duty; claimant unnamed | wa-interpretation-time.l4 `the act or thing must be done with all convenient speed and as often as occasion arises` |
| s 64: a power to extend a time may be used after the time has run out | the court or authority (a power to extend); the applicant (a privilege to apply late) | the other party bound by the time (a liability); the court or authority (no-right to refuse an application only for lateness) | power / liability; privilege / no-right | wa-interpretation-time.l4 `an application to extend may be made after the time has expired` |
| s 66(2), (3): the rule-making authority may make rules of court for the purposes of a written law and for new jurisdiction | the rule-making authority (a power) | parties before the court (a liability) | power / liability | wa-interpretation-part9.l4 `the authority's power includes making rules of court for the purpose of the written law`, `the authority may make rules or orders, including about costs, for the practice and procedure in exercising the jurisdiction` |
| s 69: penal laws reach bodies corporate; a penalty payable to a party aggrieved is payable to a body corporate | (1) the State, to prosecute a body corporate (a claim); (2) a body corporate that is the party aggrieved (a claim to the penalty or sum) | (1) the body corporate (a duty and liability); (2) whoever must pay (a duty) | claim / duty | wa-interpretation-part9.l4 `the enactment refers to the person`, `the penalty or sum is payable to the body corporate` |
| s 71: a continuing failure is a continuing offence, $50 a day unless otherwise provided | the State (a claim that the act be done, and a power to charge each further day) | the person who has not done it (a duty that continues; a liability to a further offence for each day) | claim / duty; power / liability | wa-interpretation-part9.l4 `the obligation to do the act or thing continues`, `the number of separate and further offences`, `the penalty for each separate and further offence` |
| s 72: a penalty stated at the foot of a section is the penalty for contravening it | the State (a claim to the penalty on conviction) | the person who contravenes (a duty not to, and a liability to the penalty) | claim / duty | wa-interpretation-part9.l4 `what is an offence with the penalty specified`, `the penalty on conviction` |
| s 74: a minor deviation from a prescribed form does not invalidate it | the person who used the form (an immunity from invalidity) | anyone who would challenge the form (a disability) | immunity / disability | wa-interpretation-part10.l4 `the deviation invalidates the form used` |
| s 75: service by post, registered post and certified mail | the person serving (a power to serve by post or, for registered post, by certified mail) | the person served (a liability to be treated as served) | power / liability | wa-interpretation-time.l4 `the day service by post is deemed effected`; wa-interpretation-part10.l4 `service may be effected either by registered post or by certified mail` |
| s 76: service generally | the person serving (a power to choose among the manners) | the person served (a liability) | power / liability | wa-interpretation-part10.l4 `service may be effected in the manner` |
| s 76A: pre-Australia Acts enactments have the effect and validity they would have had | the person who relies on such a provision (an immunity from invalidity) | anyone who would challenge it (a disability) | immunity / disability | wa-interpretation-part10.l4 `the provision has the effect and validity it would have had if the Australia Acts had been in operation then` |
| s 77(2), (4), notes 1 and 4: section 11 and section 47 of the 1918 Act continue for Acts passed before 1 July 1984 | the holder of a power conferred by an Act not yet in operation (a power to use it after the passing); the person who relies on an exercise validated by s 11(2) (an immunity) | those affected (a liability, but no right or obligation arises before commencement except as necessary or expedient: a disability of the power-holder) | power / liability; immunity / disability | wa-interpretation-part10.l4 `the power may be exercised at any time after the passing of the Act`, `the exercise may confer a right or impose an obligation before the Act comes into operation` |
| note 4, Second Schedule B to E: complaint within one, three, six or twelve months of the offence | the accused (an immunity from a complaint after the time) | the complainant (a disability to begin proceedings after the time) | immunity / disability | wa-interpretation-time.l4 `the last day to make the complaint and commence the proceedings` |
| note 4, Second Schedule F: an order or warrant is not quashed for want of form only | the court and the enforcing officer (an immunity of the order) | the convicted person (a disability to have it quashed or removed by certiorari for want of form) | immunity / disability | wa-interpretation-part10.l4 `the proceeding may be quashed, vacated or removed on that ground` |
| note 4, Second Schedule G: protection of persons acting in execution of the Act (tender of amends, costs) | the defendant who acted in execution of the Act (an immunity from recovery after tender or payment into court; a claim to full costs) | the plaintiff (a disability to recover; a duty to pay the defendant's costs) | immunity / disability; claim / duty | wa-interpretation-part10.l4 `the plaintiff recovers in the action`, `the defendant recovers full costs as between solicitor and client`, `the plaintiff who obtained a verdict has costs against the defendant` |
| note 4, Second Schedule H: no action against officers executing the Act unless corruption or malice is directly proved | the officer or person acting under one (an immunity from action) | the would-be plaintiff (a disability) | immunity / disability | wa-interpretation-part10.l4 `an action lies against the defendant`, `the Court may award the defendant treble costs or such portion of them as it thinks fit` |
| **none**: s1, s2, s3 (all subsections), s5, s6, s7, s8, s9, s10, s11, s12, s13 (all subsections), s13A (all subsections), s13B, s13CA (all subsections), s13C, s13D (all subsections), s14, s15 (all subsections), s15A (all subsections), s16 (all subsections), s17, s18, s19 (all subsections), s20 (all subsections), s21, s22, s23, s26 (all subsections), s27, s28, s29, s30, s31 (all subsections), s32 (all subsections), s33, s34, s35, s41 (all subsections), s42(6), s42(7), s42(8), s43(2), s43(3), s43(5), s43(9), s44 (all subsections), s46 (all subsections), s47, s61(1)(a) to (d), s61(1)(f), s61(1)(g), s61(2), s62 (all subsections), s65, s66(1), s67 (all subsections), s73, s77(1), s77(3), fn2, fn3, fn4-schedule, fn4-schedule-A, fn5 | not applicable | not applicable | none (definitions, rules of reading, counting rules, scope, commencement, repeal-and-citation machinery, classification, notes) | encoded or inert; see the coverage table |

## Coverage table

Built by `coverage.py` from the text (a script, not by hand), with the dispositions in `coverage_data.py`, which a second script wrote from the `@ref` annotations in the modules so that a row is `encoded` only when some rule cites it.
Every non-blank line of the text falls in exactly one row; a parent row holds only its own heading and lead-in lines.

Audit (`python3 -I coverage.py ../../registers/source-bundle/mrdoc_49111.txt audit`):

```
non-blank lines in the text: 1105
lines owned by a row:        1105
non-blank lines in NO row:   0 []
lines in more than one row:  0 []
blank lines in a row:        0
rows by kind: {'contents': 1, 'deleted': 4, 'example': 5, 'footnote': 12, 'heading': 11, 'history': 27, 'index-row': 136, 'note': 2, 'paragraph': 162, 'schedule': 9, 'section': 83, 'section-deleted': 3, 'subparagraph': 21, 'subsection': 125, 'table-header': 3, 'table-row': 53, 'term': 131, 'title': 2}
rows total: 790 (of which embedded defined terms: 18 )
```

Rows before and after: there was no earlier table in this row; the table was built once at the start (790 rows, 1105 lines) and again after the last module change, with the same counts.
Pass 2 ran it again: still 790 rows and 1105 lines, and no row was added, removed or moved; three dispositions changed their reason (below).
The `where` column of the s 5 term rows names the tests of the first version; `wa-tests-s5-meanings.l4` adds tests for the entries it names.

Dispositions: {'inert': 241, 'encoded': 529, 'fork': 13, 'repealed': 7}; by reason: {'encoded': 529, 'fork (F1)': 4, 'fork (F10)': 1, 'fork (F2)': 1, 'fork (F3)': 1, 'fork (F4)': 1, 'fork (F5)': 1, 'fork (F6)': 1, 'fork (F7)': 1, 'fork (F8)': 1, 'fork (F9)': 1, 'inert (1)': 238, 'inert (2)': 2, 'inert (3)': 1, 'repealed or blank in this text': 7}

Inert rows and their reasons (1 not operative, 2 machinery, 3 repealed or blank): reason 1 covers the title, contents, Part headings, 27 history notes, the compilation table (its header and 52 rows), the index of defined terms (136 rows, each a pointer to a term encoded above), the copyright notice, the notes heading, the Second Schedule heading and note 2 (a cross-reference), and, since pass 2, the uncommenced table's header and its one row (a provision of another Act marked 'To be proclaimed', not in force) and note 5 (a note about a transitional provision of another Act).
Reason 2 covers s 1 (short title) and s 77(1) (repeal of the 1918 Act).
In the first version the uncommenced table's header and row and note 5 were reason 2, with the reason "amends nothing yet and affects no one now", which is not a reason of machinery; pass 2 relabelled them reason 1 with a plain reason.
Reason 3 covers note 3 (shows the Australian Citizenship Act 1948 repealed).
Rows planned as inert and then encoded: s 2 (first thought machinery; the Act's own day is a constant the time module uses) and the s 5 lead-in "In this Act and every other written law" (first thought a lead-in; now `a definition in section 5 applies to the words`).
Rows the self-audit found unencoded or only described in a comment, now `encoded` with a function and a test: the s 13(1) definitions ("Commonwealth Act", "law of the State"), the s 13CA(1) definition and s 43(9).
No row is `out-of-scope` or `deferred`.
The Act is silent, and the encoding returns NOTHING with a test, on: weeks; time counted back in months or years; an Act reserved before 1 July 1984; a heading where a marginal note exists; a quorum for fewer than 3 members (rows s 61, s 62, s 20(3), s 32(2) and s 54 carry them).

| row | kind | lines | disposition | where / reason |
|---|---|---|---|---|
| front | title | 1-5 | inert (1) | title: not operative |
| contents | contents | 6-104 | inert (1) | table of contents: not operative |
| long-title | title | 107-109 | inert (1) | title: not operative |
| part-I | heading | 110 | inert (1) | heading: not operative |
| s1 | section | 111-112 | inert (2) | short title (machinery) |
| s2 | section | 113-114 | encoded | wa-interpretation-time.l4 `the day this Act came into operation` (tests: wa-tests-time.l4) |
| s3 | section | 115 | encoded | wa-interpretation-part1.l4, its subsections (tests: wa-tests-part1.l4) |
| s3(1) | subsection | 116 | encoded | wa-interpretation-part1.l4 `this Act applies to the written law` (tests: wa-tests-part1.l4) |
| s3(1)(a) | paragraph | 117 | encoded | wa-interpretation-part1.l4 `this Act applies to the written law` (tests: wa-tests-part1.l4) |
| s3(1)(b) | paragraph | 118 | encoded | wa-interpretation-part1.l4 `this Act applies to the written law` (tests: wa-tests-part1.l4) |
| s3(1)(c) | paragraph | 119 | encoded | wa-interpretation-part1.l4 `this Act applies to the written law` (tests: wa-tests-part1.l4) |
| s3(2) | subsection | 120 | encoded | wa-interpretation-part1.l4 `this Act is treated as an Act passed after its own commencement` (tests: wa-tests-part1.l4) |
| s3(3) | subsection | 121 | fork (F4) | a law passed or made ON 1 July 1984 counts as after the commencement; fork register F4; rule: wa-interpretation-time.l4 `counts as passed or made after the commencement for ss 17, 25, 43(6), 50 and 64` (tests: wa-tests-time.l4) |
| s3-history | history | 122 | inert (1) | history note recording amendments: not operative |
| s4 | section | 123-124 | encoded | wa-interpretation-part1.l4 `the Crown is bound by this Act` (tests: wa-tests-part1.l4) |
| part-II | heading | 125 | inert (1) | heading: not operative |
| s5 | section | 126-127 | encoded | wa-interpretation-s5-definitions.l4 `a definition in section 5 applies to the words` (lead-in), then one entry per term |
| s5[act] | term | 128 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: act` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Act] | term | 129 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Act (line 129)` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[affidavit] | term | 130 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: affidavit` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[alternative offence] | term | 131 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: alternative offence` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[amend] | term | 132 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: amend` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[ASIC Law and ASIC Regulations] | term | 133 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: ASIC Law` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Auditor General] | term | 134 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Auditor General` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Australia] | term | 135 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Australia` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Australia Acts] | term | 136 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Australia Acts` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Australia Acts](a) | paragraph | 137 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Australia Acts](b) | paragraph | 138 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[bank holiday] | term | 139 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: bank holiday` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[bankrupt and bankrupt or a person whose affairs are under insolvency laws] | term | 140 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: bankrupt` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[book] | term | 141 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: book` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[book](a) | paragraph | 142 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[book](b) | paragraph | 143 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[British possession] | term | 144 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: British possession` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[bylaw] | term | 145 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: bylaw` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[chief executive officer] | term | 146 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: chief executive officer` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[chief executive officer](a) | paragraph | 147 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[chief executive officer](a)(i) | subparagraph | 148 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[chief executive officer](a)(ii) | subparagraph | 149-150 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[chief executive officer](b) | paragraph | 151 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Children’s Court] | term | 152 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Children’s Court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[commencement] | term | 153 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: commencement`; also wa-interpretation-time.l4 (`what the Act says a word for a length of time means`, s 21 and s 62 functions) (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Commissioner of State Revenue] | term | 154 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Commissioner of State Revenue` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Commonwealth] | term | 155 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Commonwealth` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Commonwealth Act or Act of the Commonwealth] | term | 156 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Commonwealth Act` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Consolidated Account] | term | 157 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Consolidated Account` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[contravene] | term | 158 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: contravene` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Corporations Law and Corporations Regulations] | term | 159 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Corporations Law` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Court of Appeal] | term | 160 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Court of Appeal` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[court of summary jurisdiction] | term | 161 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: court of summary jurisdiction` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[death] | term | 162 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: death` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[de facto partner and de facto relationship] | term | 163 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: de facto partner` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[definition] | term | 164 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: definition` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[District Court] | term | 165 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: District Court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[District Court judge] | term | 166 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: District Court judge` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[document] | term | 167 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: document` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[enactment] | term | 168 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: enactment` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[estate] | term | 169 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: estate` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Family Court or Family Court of Western Australia] | term | 170 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Family Court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[financial year] | term | 171 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: financial year`; also wa-interpretation-time.l4 (`what the Act says a word for a length of time means`, s 21 and s 62 functions) (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[function] | term | 172 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: function` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Gazette or Government Gazette] | term | 173 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Gazette` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Gazette or Government Gazette](a) | paragraph | 174 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Gazette or Government Gazette](a)(i) | subparagraph | 175 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Gazette or Government Gazette](a)(ii) | subparagraph | 176-177 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Gazette or Government Gazette](b) | paragraph | 178 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Government] | term | 179 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Government` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Government Printer] | term | 180 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Government Printer` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Governor] | term | 181 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Governor` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Her Majesty, His Majesty, Queen, King, or Crown] | term | 182 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Her Majesty` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Imperial Act] | term | 183 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Imperial Act` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[indictable offence] | term | 184 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: indictable offence` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[individual] | term | 185 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: individual` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[judge] | term | 186 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: judge` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[justice of the peace or justice or JP] | term | 187 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: justice of the peace` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[land] | term | 188 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: land` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[lawyer] | term | 189 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: lawyer` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[legal practitioner] | term | 190 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: legal practitioner` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[local government] | term | 191 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: local government` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[local government district] | term | 192 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: local government district` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[local law] | term | 193 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: local law` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[magistrate] | term | 194 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: magistrate` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Magistrates Court] | term | 195 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Magistrates Court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Minister] | term | 196 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Minister` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Minister for Public Sector Management] | term | 197 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Minister for Public Sector Management` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[month] | term | 198 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: month`; also wa-interpretation-time.l4 (`what the Act says a word for a length of time means`, s 21 and s 62 functions) (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[oath] | term | 199 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: oath` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[parent] | term | 200 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: parent` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[parent](a) | paragraph | 201 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[parent](b) | paragraph | 202 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[parent](c) | paragraph | 203 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[Parliament] | term | 204 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Parliament` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[penalty] | term | 205 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: penalty` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[perform] | term | 206 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: perform` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[person or any word or expression descriptive of a person] | term | 207 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: person` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[police officer] | term | 208 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: police officer` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[power] | term | 209 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: power` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[prescribed] | term | 210 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: prescribed` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[prescribed](a) | paragraph | 211 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[prescribed](b) | paragraph | 212 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[proclamation] | term | 213 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: proclamation` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[public halfholiday] | term | 214 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: public halfholiday` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[public holiday] | term | 215 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: public holiday` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Public Sector Commissioner] | term | 216 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Public Sector Commissioner` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Public Service] | term | 217 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Public Service` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[public service holiday] | term | 218 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: public service holiday` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[public service officer] | term | 219 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: public service officer` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[publication] | term | 220 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: publication` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[publication](a) | paragraph | 221 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[publication](b) | paragraph | 222 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[publication](c) | paragraph | 223 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[publication](d) | paragraph | 224 | encoded | wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means`; wa-interpretation-time.l4 `what the Act says a word for a length of time means` (tests: wa-tests-time.l4) |
| s5[regional local government] | term | 225 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: regional local government` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[regional subsidiary] | term | 226 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: regional subsidiary` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[regulation] | term | 227 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: regulation` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[repeal] | term | 228 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: repeal` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Royal Assent] | term | 229 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Royal Assent` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[rule] | term | 230 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: rule` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[rules of court] | term | 231 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: rules of court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[sell] | term | 232 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: sell` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[sign] | term | 233 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: sign` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[simple offence] | term | 234 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: simple offence` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[sitting days] | term | 235 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: sitting days` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[spouse] | term | 236 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: spouse` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Standards Australia] | term | 237 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Standards Australia` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[State] | term | 238 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: State` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[State Administrative Tribunal] | term | 239 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: State Administrative Tribunal` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[statutory declaration] | term | 240 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: statutory declaration` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[subsidiary legislation] | term | 241 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: subsidiary legislation` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[summary conviction] | term | 242 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: summary conviction` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[summary conviction penalty] | term | 243 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: summary conviction penalty` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Supreme Court] | term | 244 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Supreme Court` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[swear] | term | 245 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: swear` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[Territory] | term | 246 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: Territory` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[the State or this State] | term | 247 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: the State` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[under] | term | 248 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: under` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[United Kingdom] | term | 249 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: United Kingdom` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[ValuerGeneral] | term | 250 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: ValuerGeneral` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[WA legislation website] | term | 251 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: WA legislation website` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[will] | term | 252 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: will` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[words] | term | 253 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: words` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[writing] | term | 254 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: writing` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[written law] | term | 255 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: written law` (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5[year] | term | 256 | encoded | wa-interpretation-s5-definitions.l4 `section 5 term: year`; also wa-interpretation-time.l4 (`what the Act says a word for a length of time means`, s 21 and s 62 functions) (tests: wa-tests-s5-definitions.l4, wa-tests-s5-key-terms.l4) |
| s5-history | history | 257 | inert (1) | history note recording amendments: not operative |
| s6 | section | 258-259 | encoded | wa-interpretation-part2.l4 `a definition or rule of interpretation applies to the provision` (tests: wa-tests-part2.l4) |
| s7 | section | 260-261 | encoded | wa-interpretation-part2.l4 `the extent of validity of an enactment` (tests: wa-tests-part2.l4) |
| s8 | section | 262-263 | encoded | wa-interpretation-part2.l4 `a present tense provision applies to the circumstance as it arises` (tests: wa-tests-part2.l4) |
| s9 | section | 264-265 | encoded | wa-interpretation-part2.l4 `the word has a corresponding meaning` (tests: wa-tests-part2.l4) |
| s10 | section | 266-267 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s10(a) | paragraph | 268 | encoded | wa-interpretation-part2.l4 `a word indicating a person of a particular gender or sex includes` (tests: wa-tests-part2.l4) |
| s10(a)(i) | subparagraph | 269 | encoded | wa-interpretation-part2.l4 `a word indicating a person of a particular gender or sex includes` (tests: wa-tests-part2.l4) |
| s10(a)(ii) | subparagraph | 270 | encoded | wa-interpretation-part2.l4 `a word indicating a person of a particular gender or sex includes` (tests: wa-tests-part2.l4) |
| s10(b) | deleted | 271 | repealed or blank in this text | the text shows: [(b)	deleted] |
| s10(c) | paragraph | 272 | encoded | wa-interpretation-part2.l4 `the numbers a word in this number covers` (tests: wa-tests-part2.l4) |
| s10-history | history | 273 | inert (1) | history note recording amendments: not operative |
| s11 | section | 274-275 | encoded | wa-interpretation-part2.l4 `the Sovereign meant by the reference` (tests: wa-tests-part2.l4) |
| s12 | section | 276-277 | encoded | wa-interpretation-part2.l4 `the Ministers a reference to the Minister covers` (tests: wa-tests-part2.l4) |
| s12(a) | paragraph | 278 | encoded | wa-interpretation-part2.l4 `the Ministers a reference to the Minister covers` (tests: wa-tests-part2.l4) |
| s12(b) | paragraph | 279 | encoded | wa-interpretation-part2.l4 `the Ministers a reference to the Minister covers` (tests: wa-tests-part2.l4) |
| s12(c) | paragraph | 280 | encoded | wa-interpretation-part2.l4 `the Ministers a reference to the Minister covers` (tests: wa-tests-part2.l4) |
| s13 | section | 281 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s13(1) | subsection | 282 | encoded | wa-interpretation-part2.l4 `the Act that Commonwealth Act means in section 13`; wa-interpretation-part2.l4 `it is a law of the State` (tests: wa-tests-part2.l4) |
| s13(1)[Commonwealth Act] | term | 283 | encoded | wa-interpretation-part2.l4 `the Act that Commonwealth Act means in section 13`; wa-interpretation-part2.l4 `it is a law of the State` (tests: wa-tests-part2.l4) |
| s13(1)[law of the State] | term | 284 | encoded | wa-interpretation-part2.l4 `the Act that Commonwealth Act means in section 13`; wa-interpretation-part2.l4 `it is a law of the State` (tests: wa-tests-part2.l4) |
| s13(2) | subsection | 285 | encoded | wa-interpretation-part2.l4 `a reference to a British subject is read as a reference to the person` (tests: wa-tests-part2.l4) |
| s13(3) | subsection | 286 | encoded | wa-interpretation-part2.l4 `a reference to a British subject is read as a reference to the person`; wa-interpretation-part2.l4 `a rule of law about British subjects applies to the person as if a British subject` (tests: wa-tests-part2.l4) |
| s13A | section | 287 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s13A(1) | subsection | 288 | encoded | wa-interpretation-part2.l4 `a de facto relationship exists between two persons` (tests: wa-tests-part2.l4) |
| s13A(2) | subsection | 289 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(a) | paragraph | 290 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(b) | paragraph | 291 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(c) | paragraph | 292 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(d) | paragraph | 293 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(e) | paragraph | 294 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(f) | paragraph | 295 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(g) | paragraph | 296 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(h) | paragraph | 297 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(2)(i) | paragraph | 298 | encoded | wa-interpretation-part2.l4 `the number of indicators present` (tests: wa-tests-part2.l4) |
| s13A(3) | subsection | 299 | encoded | wa-interpretation-part2.l4 `a de facto relationship exists between two persons` (tests: wa-tests-part2.l4) |
| s13A(3)(a) | paragraph | 300 | encoded | wa-interpretation-part2.l4 `a de facto relationship exists between two persons` (tests: wa-tests-part2.l4) |
| s13A(3)(b) | paragraph | 301 | encoded | wa-interpretation-part2.l4 `a de facto relationship exists between two persons` (tests: wa-tests-part2.l4) |
| s13A(4) | subsection | 302 | encoded | wa-interpretation-part2.l4 `a person is a de facto partner` (tests: wa-tests-part2.l4) |
| s13A(5) | subsection | 303 | encoded | wa-interpretation-part2.l4 `the other person is the de facto partner of the first person` (tests: wa-tests-part2.l4) |
| s13A-history | history | 304 | inert (1) | history note recording amendments: not operative |
| s13B | section | 305-306 | encoded | wa-interpretation-part2.l4 `the body a reference to the Standards Association of Australia is read as` (tests: wa-tests-part2.l4) |
| s13B-history | history | 307 | inert (1) | history note recording amendments: not operative |
| s13CA | section | 308 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s13CA(1) | subsection | 309 | encoded | wa-interpretation-part2.l4 `it is a local government district` (tests: wa-tests-part2.l4) |
| s13CA(1)[local government district] | term | 310 | encoded | wa-interpretation-part2.l4 `it is a local government district` (tests: wa-tests-part2.l4) |
| s13CA(2) | subsection | 311 | encoded | wa-interpretation-part2.l4 `the local government district a name refers to` (tests: wa-tests-part2.l4) |
| s13CA-example | example | 312 | encoded | wa-interpretation-part2.l4 `the local government district a name refers to` (tests: wa-tests-part2.l4) |
| s13CA-example(1) | example | 313 | encoded | wa-interpretation-part2.l4 `the local government district a name refers to` (tests: wa-tests-part2.l4) |
| s13CA-example(2) | example | 314 | encoded | wa-interpretation-part2.l4 `the local government district a name refers to` (tests: wa-tests-part2.l4) |
| s13CA-history | history | 315 | inert (1) | history note recording amendments: not operative |
| s13C | section | 316-317 | encoded | wa-interpretation-part2.l4 `the person has died` (tests: wa-tests-part2.l4) |
| s13C(a) | paragraph | 318 | encoded | wa-interpretation-part2.l4 `the person has died` (tests: wa-tests-part2.l4) |
| s13C(b) | paragraph | 319 | encoded | wa-interpretation-part2.l4 `the person has died` (tests: wa-tests-part2.l4) |
| s13C-history | history | 320 | inert (1) | history note recording amendments: not operative |
| s13D | section | 321 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s13D(1) | subsection | 322 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt` (tests: wa-tests-part2.l4) |
| s13D(2) | subsection | 323 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |
| s13D(2)(a) | paragraph | 324 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |
| s13D(2)(b) | paragraph | 325 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |
| s13D(2)(c) | paragraph | 326 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |
| s13D(2)(d) | paragraph | 327-328 | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |
| s13D-history | history | 329 | inert (1) | history note recording amendments: not operative |
| s14 | section | 330-331 | encoded | wa-interpretation-part2.l4 `the portions up to and including`; wa-interpretation-part2.l4 `the portions a reference covers` (tests: wa-tests-part2.l4) |
| s15 | section | 332 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s15(1) | subsection | 333 | encoded | wa-interpretation-part2.l4 `an internal reference points at` (tests: wa-tests-part2.l4) |
| s15(2) | subsection | 334 | encoded | wa-interpretation-part2.l4 `an internal reference points at` (tests: wa-tests-part2.l4) |
| s15(3) | subsection | 335 | encoded | wa-interpretation-part2.l4 `an internal reference points at` (tests: wa-tests-part2.l4) |
| s15(4) | subsection | 336 | encoded | wa-interpretation-part2.l4 `an internal reference points at`; wa-interpretation-part2.l4 `section 15(1) to (3) applies to the written law with the necessary modifications` (tests: wa-tests-part2.l4) |
| s15A | section | 337 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s15A(1) | subsection | 338 | encoded | wa-interpretation-part2.l4 `a reference to a paragraph includes` (tests: wa-tests-part2.l4) |
| s15A(1)[paragraph] | term | 339 | encoded | wa-interpretation-part2.l4 `a reference to a paragraph includes` (tests: wa-tests-part2.l4) |
| s15A(2) | subsection | 340 | encoded | wa-interpretation-part2.l4 `a reference to a paragraph includes the conjunction` (tests: wa-tests-part2.l4) |
| s15A-history | history | 341 | inert (1) | history note recording amendments: not operative |
| s16 | section | 342 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s16(1) | subsection | 343 | encoded | wa-interpretation-part2.l4 `the reference includes the law as it may from time to time be amended` (tests: wa-tests-part2.l4) |
| s16(2) | subsection | 344 | encoded | wa-interpretation-part2.l4 `the reference includes the law as it may from time to time be amended` (tests: wa-tests-part2.l4) |
| s16(3) | subsection | 345 | encoded | wa-interpretation-part2.l4 `the reference includes the law as it may from time to time be amended` (tests: wa-tests-part2.l4) |
| s17 | section | 346-347 | encoded | wa-interpretation-part2.l4 `the word is read disjunctively and not as implying similarity` (tests: wa-tests-part2.l4) |
| s18 | section | 348-349 | encoded | wa-interpretation-part2.l4 `the construction preferred` (tests: wa-tests-part2.l4) |
| s19 | section | 350 | encoded | wa-interpretation-part2.l4, its subsections (tests: wa-tests-part2.l4) |
| s19(1) | subsection | 351 | encoded | wa-interpretation-part2.l4 `consideration may be given to the material` (tests: wa-tests-part2.l4) |
| s19(1)(a) | paragraph | 352 | encoded | wa-interpretation-part2.l4 `consideration may be given to the material` (tests: wa-tests-part2.l4) |
| s19(1)(b) | paragraph | 353 | encoded | wa-interpretation-part2.l4 `consideration may be given to the material` (tests: wa-tests-part2.l4) |
| s19(1)(b)(i) | subparagraph | 354 | encoded | wa-interpretation-part2.l4 `consideration may be given to the material` (tests: wa-tests-part2.l4) |
| s19(1)(b)(ii) | subparagraph | 355 | encoded | wa-interpretation-part2.l4 `consideration may be given to the material` (tests: wa-tests-part2.l4) |
| s19(2) | subsection | 356 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(a) | paragraph | 357 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(b) | paragraph | 358 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(c) | paragraph | 359 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(d) | paragraph | 360 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(e) | paragraph | 361 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(f) | paragraph | 362 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(g) | paragraph | 363 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(2)(h) | paragraph | 364 | encoded | wa-interpretation-part2.l4 `material of this kind is among the material that may be considered` (tests: wa-tests-part2.l4) |
| s19(3) | subsection | 365 | encoded | wa-interpretation-part2.l4 `the matters regard must be had to when deciding whether to consider material, and what weight to give it` (tests: wa-tests-part2.l4) |
| s19(3)(a) | paragraph | 366 | encoded | wa-interpretation-part2.l4 `the matters regard must be had to when deciding whether to consider material, and what weight to give it` (tests: wa-tests-part2.l4) |
| s19(3)(b) | paragraph | 367 | encoded | wa-interpretation-part2.l4 `the matters regard must be had to when deciding whether to consider material, and what weight to give it` (tests: wa-tests-part2.l4) |
| s19-history | history | 368 | inert (1) | history note recording amendments: not operative |
| part-III | heading | 369 | inert (1) | heading: not operative |
| s20 | section | 370 | encoded | wa-interpretation-time.l4 `the day an Act comes into operation` (tests: wa-tests-time.l4) |
| s20(1) | subsection | 371 | encoded | wa-interpretation-time.l4 `the day an Act comes into operation` (tests: wa-tests-time.l4) |
| s20(2) | subsection | 372 | encoded | wa-interpretation-time.l4 `the day an Act comes into operation` (tests: wa-tests-time.l4) |
| s20(3) | subsection | 373 | encoded | wa-interpretation-time.l4 `the day an Act comes into operation` (tests: wa-tests-time.l4) |
| s21 | section | 374-375 | encoded | wa-interpretation-time.l4 `the moment a written law comes into operation`; wa-interpretation-time.l4 `a written law is in operation at` (tests: wa-tests-time.l4) |
| s22 | section | 376-377 | encoded | wa-interpretation-time.l4 `the day the proclamation provision and the short title come into operation` (tests: wa-tests-time.l4) |
| s23 | section | 378-379 | encoded | wa-interpretation-time.l4, its subsections (tests: wa-tests-time.l4) |
| s23(a) | paragraph | 380 | encoded | wa-interpretation-time.l4 `the power to fix a day extends to a day not prior to publication` (tests: wa-tests-time.l4) |
| s23(b) | paragraph | 381-382 | encoded | wa-interpretation-time.l4 `the power to fix a day extends to the number of different days fixed` (tests: wa-tests-time.l4) |
| s23-history | history | 383 | inert (1) | history note recording amendments: not operative |
| s24 | section-deleted | 384 | repealed or blank in this text | the text shows: [24.	Deleted: No. 13 of 2021 s. 52.] |
| s25 | section | 385 | encoded | wa-interpretation-part3.l4, its subsections (tests: wa-tests-part3.l4) |
| s25(1) | subsection | 386 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(1)(a) | paragraph | 387 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(1)(b) | paragraph | 388 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(1)(c) | paragraph | 389 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(1)(d) | paragraph | 390 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(1)(e) | paragraph | 391-392 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2) | subsection | 393 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(a) | paragraph | 394 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b) | paragraph | 395 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b)(i) | subparagraph | 396 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b)(ii) | subparagraph | 397 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b)(iii) | subparagraph | 398 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b)(iv) | subparagraph | 399 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(2)(b)(v) | subparagraph | 400-401 | encoded | wa-interpretation-part3.l4 `the power may be exercised before the provision commences` (tests: wa-tests-part3.l4) |
| s25(3) | subsection | 402 | encoded | wa-interpretation-time.l4 `the day an instrument or notice made early takes effect` (tests: wa-tests-time.l4) |
| s25(3)(a) | paragraph | 403 | encoded | wa-interpretation-time.l4 `the day an instrument or notice made early takes effect` (tests: wa-tests-time.l4) |
| s25(3)(b) | paragraph | 404-405 | encoded | wa-interpretation-time.l4 `the day an instrument or notice made early takes effect` (tests: wa-tests-time.l4) |
| s25(4) | subsection | 406 | encoded | wa-interpretation-part3.l4 `the appointee may act in the office, or the body may meet and perform its functions`; wa-interpretation-part3.l4 `the earliest day the term of office of an early appointee begins` (tests: wa-tests-part3.l4) |
| s25(5) | subsection | 407 | encoded | wa-interpretation-part3.l4 `section 25 applies to the Act` (tests: wa-tests-part3.l4) |
| s26 | section | 408 | encoded | wa-interpretation-part3.l4, its subsections (tests: wa-tests-part3.l4) |
| s26(1) | subsection | 409 | encoded | wa-interpretation-part3.l4 `a citation is sufficient for all purposes` (tests: wa-tests-part3.l4) |
| s26(1)(a) | paragraph | 410 | encoded | wa-interpretation-part3.l4 `a citation is sufficient for all purposes` (tests: wa-tests-part3.l4) |
| s26(1)(b) | paragraph | 411 | encoded | wa-interpretation-part3.l4 `a citation is sufficient for all purposes` (tests: wa-tests-part3.l4) |
| s26(2) | subsection | 412 | encoded | wa-interpretation-part3.l4 `a citation is sufficient for all purposes` (tests: wa-tests-part3.l4) |
| s26(3) | subsection | 413 | encoded | wa-interpretation-part3.l4 `a citation or reference is made as the Act requires` (tests: wa-tests-part3.l4) |
| s26(4) | deleted | 414 | repealed or blank in this text | the text shows: [(4)	deleted] |
| s26-history | history | 415 | inert (1) | history note recording amendments: not operative |
| s27 | section | 416-417 | encoded | wa-interpretation-time.l4 `the day a reference to commencement means` (tests: wa-tests-time.l4) |
| part-IV | heading | 418 | inert (1) | heading: not operative |
| s28 | section | 419-420 | encoded | wa-interpretation-part4.l4 `an Act is deemed a public Act and judicially noticed as such` (tests: wa-tests-part4.l4) |
| s29 | section | 421-422 | encoded | wa-interpretation-part4.l4 `a section of an Act takes effect as a substantive enactment` (tests: wa-tests-part4.l4) |
| s30 | section | 423-424 | encoded | wa-interpretation-part4.l4 `an Act may be amended or repealed` (tests: wa-tests-part4.l4) |
| s31 | section | 425 | encoded | wa-interpretation-part4.l4, its subsections (tests: wa-tests-part4.l4) |
| s31(1) | subsection | 426 | encoded | wa-interpretation-part4.l4 `forms part of the written law under section 31`; wa-interpretation-part4.l4 `a preamble is construed as intended to assist in explaining the written law's purport and object` (tests: wa-tests-part4.l4) |
| s31(2) | subsection | 427 | encoded | wa-interpretation-part4.l4 `forms part of the written law under section 31` (tests: wa-tests-part4.l4) |
| s32 | section | 428 | encoded | wa-interpretation-part4.l4, its subsections (tests: wa-tests-part4.l4) |
| s32(1) | subsection | 429 | encoded | wa-interpretation-part4.l4 `forms part of the written law under section 32` (tests: wa-tests-part4.l4) |
| s32(2) | subsection | 430 | fork (F8) | with a marginal note present the text does not say whether a heading is part of the law: NOTHING; fork register F8; rule: wa-interpretation-part4.l4 `forms part of the written law under section 32` (tests: wa-tests-part4.l4) |
| s32-history | history | 431 | inert (1) | history note recording amendments: not operative |
| part-V | heading | 432 | inert (1) | heading: not operative |
| s33 | section | 433-434 | encoded | wa-interpretation-part5.l4 `the provisions repealed along with a repealed written law` (tests: wa-tests-part5.l4) |
| s34 | section | 435-436 | encoded | wa-interpretation-part5.l4 `the repeal of a repealing enactment revives the enactment previously repealed` (tests: wa-tests-part5.l4) |
| s35 | section | 437-438 | encoded | wa-interpretation-part5.l4 `the repealed enactment remains in operation on` (tests: wa-tests-part5.l4) |
| s36 | section | 439-440 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s36(a) | paragraph | 441 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s36(b) | paragraph | 442 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s36(c) | paragraph | 443 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s36(d) | paragraph | 444 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s36(e) | paragraph | 445-446 | encoded | wa-interpretation-part5.l4 `the thing subsists and continues as if made or done under the repealing law` (tests: wa-tests-part5.l4) |
| s37 | section | 447 | encoded | wa-interpretation-part5.l4, its subsections (tests: wa-tests-part5.l4) |
| s37(1) | subsection | 448 | encoded | wa-interpretation-part5.l4 `it may still be instituted, continued, enforced or imposed as if the repealing law had not been passed or made` (tests: wa-tests-part5.l4) |
| s37(1)(a) | paragraph | 449 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(1)(b) | paragraph | 450 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(1)(c) | paragraph | 451 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(1)(d) | paragraph | 452 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(1)(e) | paragraph | 453 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(1)(f) | paragraph | 454-455 | encoded | wa-interpretation-part5.l4 `the repeal affects` (tests: wa-tests-part5.l4) |
| s37(2) | subsection | 456 | encoded | wa-interpretation-part5.l4 `section 37 still operates` (tests: wa-tests-part5.l4) |
| s37-history | history | 457 | inert (1) | history note recording amendments: not operative |
| s38 | section | 458 | encoded | wa-interpretation-part5.l4, its subsections (tests: wa-tests-part5.l4) |
| s38(1) | subsection | 459 | encoded | wa-interpretation-part5.l4 `the subsidiary legislation continues in operation as if made under the repealing Act` (tests: wa-tests-part5.l4) |
| s38(1)(a) | paragraph | 460 | encoded | wa-interpretation-part5.l4 `the subsidiary legislation continues in operation as if made under the repealing Act` (tests: wa-tests-part5.l4) |
| s38(1)(b) | paragraph | 461-462 | encoded | wa-interpretation-part5.l4 `the subsidiary legislation continues in operation as if made under the repealing Act` (tests: wa-tests-part5.l4) |
| s38(2) | subsection | 463 | encoded | wa-interpretation-part5.l4 `the continuing subsidiary legislation may be amended or repealed as if made under the repealing Act` (tests: wa-tests-part5.l4) |
| s39 | section | 464-465 | encoded | wa-interpretation-part5.l4 `the expiry or lapse of an enactment affects` (tests: wa-tests-part5.l4) |
| part-VI | heading | 466 | inert (1) | heading: not operative |
| s40 | section | 467-468 | encoded | wa-interpretation-part6.l4 `who makes the subsidiary legislation` (tests: wa-tests-part6.l4) |
| s41 | section | 469 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s41(1) | subsection | 470 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s41(1)(a) | paragraph | 471 | encoded | wa-interpretation-part6.l4 `the subsidiary legislation is published as section 41(1)(a) requires` (tests: wa-tests-part6.l4) |
| s41(1)(b) | paragraph | 472 | encoded | wa-interpretation-time.l4 `the day subsidiary legislation comes into operation` (tests: wa-tests-time.l4) |
| s41(2) | subsection | 473 | encoded | wa-interpretation-time.l4 `the power to fix a day for subsidiary legislation extends to the number of different days fixed` (tests: wa-tests-time.l4) |
| s41-history | history | 474 | inert (1) | history note recording amendments: not operative |
| s42 | section | 475 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s42(1) | subsection | 476 | encoded | wa-interpretation-part6.l4 `the last day for laying the regulations before the House` (tests: wa-tests-part6.l4) |
| s42(2) | subsection | 477 | encoded | wa-interpretation-part6.l4 `the last day for giving notice of a resolution disallowing the regulations`; wa-interpretation-part6.l4 `the regulations cease to have effect`; wa-interpretation-part6.l4 `the thing done in the meantime is valid after the regulations cease to have effect` (tests: wa-tests-part6.l4) |
| s42(3) | subsection | 478 | encoded | wa-interpretation-part6.l4 `the last day for giving notice of a resolution disallowing the regulations` (tests: wa-tests-part6.l4) |
| s42(4) | subsection | 479 | fork (F5) | 'after the expiration of 7 days from' publication: first day of effect is the 8th day after it; fork register F5; rule: wa-interpretation-part6.l4 `the first day the amended or substituted regulations take effect` (tests: wa-tests-part6.l4) |
| s42(4)(a) | paragraph | 480 | encoded | wa-interpretation-part6.l4 `the first day the amended or substituted regulations take effect` (tests: wa-tests-part6.l4) |
| s42(4)(b) | paragraph | 481 | encoded | wa-interpretation-part6.l4 `the first day the amended or substituted regulations take effect` (tests: wa-tests-part6.l4) |
| s42(5) | subsection | 482 | fork (F6) | 'within 21 days of the passing': 'of' read like 'from', the day of passing excluded; fork register F6; rule: wa-interpretation-part6.l4 `the last day for publishing notice of the resolution` (tests: wa-tests-part6.l4) |
| s42(6) | subsection | 483 | encoded | wa-interpretation-part6.l4 `the first day the previous regulations are revived` (tests: wa-tests-part6.l4) |
| s42(6)(a) | paragraph | 484 | encoded | wa-interpretation-part6.l4 `the first day the previous regulations are revived` (tests: wa-tests-part6.l4) |
| s42(6)(b) | paragraph | 485-486 | encoded | wa-interpretation-part6.l4 `the first day the previous regulations are revived` (tests: wa-tests-part6.l4) |
| s42(7) | subsection | 487 | encoded | wa-interpretation-part6.l4 `subsection (1) applies to the regulations` (tests: wa-tests-part6.l4) |
| s42(8) | subsection | 488 | encoded | wa-interpretation-part6.l4 `section 42 treats it as regulations` (tests: wa-tests-part6.l4) |
| s42(8)(a) | paragraph | 489 | encoded | wa-interpretation-part6.l4 `section 42 treats it as regulations` (tests: wa-tests-part6.l4) |
| s42(8)(b) | paragraph | 490 | encoded | wa-interpretation-part6.l4 `section 42 treats it as regulations` (tests: wa-tests-part6.l4) |
| s42-history | history | 491 | inert (1) | history note recording amendments: not operative |
| s43 | section | 492 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s43(1) | subsection | 493 | encoded | wa-interpretation-part6.l4 `the subsidiary legislation is void to the extent of the inconsistency` (tests: wa-tests-part6.l4) |
| s43(2) | subsection | 494 | encoded | wa-interpretation-part6.l4 `it is deemed to be made in exercise of the power` (tests: wa-tests-part6.l4) |
| s43(3) | subsection | 495 | encoded | wa-interpretation-part6.l4 `all conditions and preliminary steps precedent to making it are presumed complied with` (tests: wa-tests-part6.l4) |
| s43(4) | subsection | 496 | encoded | wa-interpretation-part6.l4 `the power includes a power to amend or repeal the subsidiary legislation, in the like manner and on the like conditions` (tests: wa-tests-part6.l4) |
| s43(5) | subsection | 497 | encoded | wa-interpretation-part6.l4 `the listing of special purposes limits the power for the general purpose` (tests: wa-tests-part6.l4) |
| s43(6) | subsection | 498 | encoded | wa-interpretation-part6.l4 `the most a fine may be under regulations, rules, local laws or bylaws`; wa-interpretation-part6.l4 `a fine is within the limit section 43(6) allows` (tests: wa-tests-part6.l4) |
| s43(7) | subsection | 499 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(7)(a) | paragraph | 500 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(7)(b) | paragraph | 501 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(7)(b)(i) | subparagraph | 502 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(7)(b)(ii) | subparagraph | 503 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8) | subsection | 504 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(a) | paragraph | 505 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(a)(i) | subparagraph | 506 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(a)(ii) | subparagraph | 507-508 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(b) | paragraph | 509 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(b)(i) | subparagraph | 510 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(b)(ii) | subparagraph | 511-512 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(c) | paragraph | 513 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(8)(d) | paragraph | 514 | encoded | wa-interpretation-part6.l4 `the power may be exercised` (tests: wa-tests-part6.l4) |
| s43(9) | subsection | 515 | encoded | wa-interpretation-part6.l4 `the power may be exercised`; wa-interpretation-part6.l4 `it is specified for section 43(7) and (8)` (tests: wa-tests-part6.l4) |
| s43-history | history | 516 | inert (1) | history note recording amendments: not operative |
| s44 | section | 517 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s44(1) | subsection | 518 | encoded | wa-interpretation-part6.l4 `the Act a reference in subsidiary legislation to the Act means`; wa-interpretation-part6.l4 `the word has the same meaning as in the written law under which the subsidiary legislation is made` (tests: wa-tests-part6.l4) |
| s44(2) | subsection | 519 | encoded | wa-interpretation-part6.l4 `the Act a reference in subsidiary legislation to the Act means` (tests: wa-tests-part6.l4) |
| s45 | section | 520 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s45(1) | subsection | 521 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(a) | paragraph | 522 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(b) | paragraph | 523 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(c) | paragraph | 524 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(d) | paragraph | 525 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(e) | paragraph | 526 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(1)(f) | paragraph | 527 | encoded | wa-interpretation-part6.l4 `subsidiary legislation may provide for` (tests: wa-tests-part6.l4) |
| s45(2) | subsection | 528 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(2)(a) | paragraph | 529 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(2)(b) | paragraph | 530 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(2)(c) | paragraph | 531 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(2)(d) | paragraph | 532 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(2)(e) | paragraph | 533-534 | encoded | wa-interpretation-part6.l4 `a reduction, waiver or refund may be expressed to apply` (tests: wa-tests-part6.l4) |
| s45(3) | deleted | 535 | repealed or blank in this text | the text shows: [(3)	deleted] |
| s45-history | history | 536 | inert (1) | history note recording amendments: not operative |
| s45A | section | 537 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s45A(1) | subsection | 538 | encoded | wa-interpretation-part6.l4 `a power to prescribe a fee allows it to recover the expenditure` (tests: wa-tests-part6.l4) |
| s45A(2) | subsection | 539 | encoded | wa-interpretation-part6.l4 `expenditure is relevant to the scheme or system under which the licence is issued` (tests: wa-tests-part6.l4) |
| s45A(2)(a) | paragraph | 540 | encoded | wa-interpretation-part6.l4 `expenditure is relevant to the scheme or system under which the licence is issued` (tests: wa-tests-part6.l4) |
| s45A(2)(b) | paragraph | 541 | encoded | wa-interpretation-part6.l4 `expenditure is relevant to the scheme or system under which the licence is issued` (tests: wa-tests-part6.l4) |
| s45A(3) | subsection | 542 | encoded | wa-interpretation-part6.l4 `a power to prescribe a fee allows it to recover the expenditure` (tests: wa-tests-part6.l4) |
| s45A(4) | subsection | 543 | encoded | wa-interpretation-part6.l4 `it is within the meaning of the word in section 45A` (tests: wa-tests-part6.l4) |
| s45A(4)[fee] | term | 544 | encoded | wa-interpretation-part6.l4 `it is within the meaning of the word in section 45A` (tests: wa-tests-part6.l4) |
| s45A(4)[issue] | term | 545 | encoded | wa-interpretation-part6.l4 `it is within the meaning of the word in section 45A` (tests: wa-tests-part6.l4) |
| s45A(4)[licence] | term | 546 | encoded | wa-interpretation-part6.l4 `it is within the meaning of the word in section 45A` (tests: wa-tests-part6.l4) |
| s45A-history | history | 547 | inert (1) | history note recording amendments: not operative |
| s46 | section | 548 | encoded | wa-interpretation-part6.l4, its subsections (tests: wa-tests-part6.l4) |
| s46(1) | subsection | 549 | encoded | wa-interpretation-part6.l4 `the reference includes subsidiary legislation made under it` (tests: wa-tests-part6.l4) |
| s46(1a) | subsection | 550 | encoded | wa-interpretation-part6.l4 `the reference includes subsidiary legislation made under it` (tests: wa-tests-part6.l4) |
| s46(2) | subsection | 551 | encoded | wa-interpretation-part6.l4 `the reference includes subsidiary legislation made under it` (tests: wa-tests-part6.l4) |
| s46-history | history | 552 | inert (1) | history note recording amendments: not operative |
| s47 | section | 553-554 | encoded | wa-interpretation-part6.l4 `the act is deemed done under the written law under which the subsidiary legislation was made` (tests: wa-tests-part6.l4) |
| part-VII | heading | 555 | inert (1) | heading: not operative |
| s48 | section | 556-557 | encoded | wa-interpretation-part7.l4 `the power may be exercised and the duty performed from time to time as occasion requires` (tests: wa-tests-part7.l4) |
| s48A | section | 558-559 | encoded | wa-interpretation-time.l4 `the power may be exercised on` (tests: wa-tests-time.l4) |
| s48A(a) | paragraph | 560 | encoded | wa-interpretation-time.l4 `the power may be exercised on` (tests: wa-tests-time.l4) |
| s48A(b) | paragraph | 561-562 | encoded | wa-interpretation-time.l4 `the power may be exercised on` (tests: wa-tests-time.l4) |
| s48A-history | history | 563 | inert (1) | history note recording amendments: not operative |
| s49 | section | 564-565 | encoded | wa-interpretation-part7.l4 `the person may exercise the power and must perform the duty of the public office` (tests: wa-tests-part7.l4) |
| s50 | section | 566 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s50(1) | subsection | 567 | encoded | wa-interpretation-part7.l4 `the other power is also deemed conferred` (tests: wa-tests-part7.l4) |
| s50(2) | subsection | 568 | encoded | wa-interpretation-part7.l4 `the power includes the other power` (tests: wa-tests-part7.l4) |
| s50(2)(a) | paragraph | 569 | encoded | wa-interpretation-part7.l4 `the power includes the other power` (tests: wa-tests-part7.l4) |
| s50(2)(b) | paragraph | 570 | encoded | wa-interpretation-part7.l4 `the power includes the other power` (tests: wa-tests-part7.l4) |
| s50(2)(c) | paragraph | 571 | encoded | wa-interpretation-part7.l4 `the power includes the other power` (tests: wa-tests-part7.l4) |
| s50(2)(d) | paragraph | 572 | encoded | wa-interpretation-part7.l4 `the power includes the other power` (tests: wa-tests-part7.l4) |
| s50(3) | subsection | 573 | encoded | wa-interpretation-part7.l4 `the other power is also deemed conferred` (tests: wa-tests-part7.l4) |
| s51 | section | 574 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s51(1) | subsection | 575 | encoded | wa-interpretation-part7.l4 `the person empowered has a discretion to grant or to refuse` (tests: wa-tests-part7.l4) |
| s51(2) | subsection | 576 | encoded | wa-interpretation-part7.l4 `the right to appeal against or seek review of a refusal is left in place` (tests: wa-tests-part7.l4) |
| s51-history | history | 577 | inert (1) | history note recording amendments: not operative |
| s52 | section | 578 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s52(1) | subsection | 579 | encoded | wa-interpretation-part7.l4 `a power to appoint includes the power` (tests: wa-tests-part7.l4) |
| s52(1)(a) | paragraph | 580 | encoded | wa-interpretation-part7.l4 `a power to appoint includes the power` (tests: wa-tests-part7.l4) |
| s52(1)(b) | paragraph | 581 | encoded | wa-interpretation-part7.l4 `a person may be appointed to act temporarily` (tests: wa-tests-part7.l4) |
| s52(1)(c) | paragraph | 582 | encoded | wa-interpretation-part7.l4 `a power to appoint includes the power` (tests: wa-tests-part7.l4) |
| s52(2) | subsection | 583 | encoded | wa-interpretation-part7.l4 `the cause is included in section 52(1)(b)` (tests: wa-tests-part7.l4) |
| s52(2)(a) | paragraph | 584 | encoded | wa-interpretation-part7.l4 `the cause is included in section 52(1)(b)` (tests: wa-tests-part7.l4) |
| s52(2)(b) | paragraph | 585 | encoded | wa-interpretation-part7.l4 `the cause is included in section 52(1)(b)` (tests: wa-tests-part7.l4) |
| s52(2)(c) | paragraph | 586 | encoded | wa-interpretation-part7.l4 `the cause is included in section 52(1)(b)` (tests: wa-tests-part7.l4) |
| s52(3) | subsection | 587 | encoded | wa-interpretation-part7.l4 `the validity of the thing done can be called in question on that ground` (tests: wa-tests-part7.l4) |
| s52(4) | subsection | 588 | encoded | wa-interpretation-part7.l4 `the powers in section 52(1)(a) to (c) are exercisable` (tests: wa-tests-part7.l4) |
| s52(5) | subsection | 589 | encoded | wa-interpretation-part7.l4 `section 52 affects the tenure` (tests: wa-tests-part7.l4) |
| s52-history | history | 590 | inert (1) | history note recording amendments: not operative |
| s53 | section | 591-592 | encoded | wa-interpretation-part7.l4 `the appointment is of the person from time to time holding, acting in, or performing the functions of the office` (tests: wa-tests-part7.l4) |
| s53(a) | paragraph | 593 | encoded | wa-interpretation-part7.l4 `the appointment is of the person from time to time holding, acting in, or performing the functions of the office` (tests: wa-tests-part7.l4) |
| s53(b) | paragraph | 594 | encoded | wa-interpretation-part7.l4 `the appointment is of the person from time to time holding, acting in, or performing the functions of the office` (tests: wa-tests-part7.l4) |
| s53(c) | paragraph | 595-596 | encoded | wa-interpretation-part7.l4 `the appointment is of the person from time to time holding, acting in, or performing the functions of the office` (tests: wa-tests-part7.l4) |
| s54 | section | 597 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s54(1) | subsection | 598 | encoded | wa-interpretation-part7.l4 `the function may be performed by those who agree` (tests: wa-tests-part7.l4) |
| s54(2) | subsection | 599 | encoded | wa-interpretation-part7.l4 `the least number of members that make a quorum, with a fixed number of members` (tests: wa-tests-part7.l4) |
| s54(2)(a) | paragraph | 600 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s54(2)(a)(i) | subparagraph | 601 | fork (F9) | 'at least one half' of an odd number rounds up to whole members; fork register F9; rule: wa-interpretation-part7.l4 `the least number of members that make a quorum, with a fixed number of members` (tests: wa-tests-part7.l4) |
| s54(2)(a)(ii) | subparagraph | 602-603 | encoded | wa-interpretation-part7.l4 `the least number of members that make a quorum, with a range of members` (tests: wa-tests-part7.l4) |
| s54(2)(b) | paragraph | 604 | encoded | wa-interpretation-part7.l4 `the act is deemed done by the association` (tests: wa-tests-part7.l4) |
| s55 | section | 605-606 | encoded | wa-interpretation-part7.l4 `the power or duty may be exercised again as often as is necessary to correct an error or omission` (tests: wa-tests-part7.l4) |
| s56 | section | 607 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s56(1) | subsection | 608 | encoded | wa-interpretation-part7.l4 `what the word means` (tests: wa-tests-part7.l4) |
| s56(2) | subsection | 609 | encoded | wa-interpretation-part7.l4 `what the word means` (tests: wa-tests-part7.l4) |
| s57 | section | 610-611 | encoded | wa-interpretation-part7.l4 `the powers of the body are affected by` (tests: wa-tests-part7.l4) |
| s57(a) | paragraph | 612 | encoded | wa-interpretation-part7.l4 `the powers of the body are affected by` (tests: wa-tests-part7.l4) |
| s57(b) | paragraph | 613 | encoded | wa-interpretation-part7.l4 `the powers of the body are affected by` (tests: wa-tests-part7.l4) |
| s57(c) | paragraph | 614 | encoded | wa-interpretation-part7.l4 `the powers of the body are affected by` (tests: wa-tests-part7.l4) |
| s57(d) | paragraph | 615 | encoded | wa-interpretation-part7.l4 `the powers of the body are affected by` (tests: wa-tests-part7.l4) |
| s58 | section | 616-617 | encoded | wa-interpretation-part7.l4 `whose opinion, belief or state of mind counts` (tests: wa-tests-part7.l4) |
| s59 | section | 618 | encoded | wa-interpretation-part7.l4, its subsections (tests: wa-tests-part7.l4) |
| s59(1) | subsection | 619 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(a) | paragraph | 620 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(b) | paragraph | 621 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(c) | paragraph | 622 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(d) | paragraph | 623 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(e) | paragraph | 624 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(1)(f) | paragraph | 625 | encoded | wa-interpretation-part7.l4 `a delegation has the feature` (tests: wa-tests-part7.l4) |
| s59(2) | subsection | 626 | encoded | wa-interpretation-part7.l4 `the other function is deemed delegated too` (tests: wa-tests-part7.l4) |
| s59(3) | subsection | 627 | encoded | wa-interpretation-part7.l4 `the act is regarded as effectually done` (tests: wa-tests-part7.l4) |
| s60 | section | 628-629 | encoded | wa-interpretation-part7.l4 `it is done by the Governor with the advice and consent of the Executive Council` (tests: wa-tests-part7.l4) |
| part-VIII | heading | 630 | inert (1) | heading: not operative |
| s61 | section | 631 | encoded | wa-interpretation-time.l4, its subsections (tests: wa-tests-time.l4) |
| s61(1) | subsection | 632 | encoded | wa-interpretation-time.l4, its subsections (tests: wa-tests-time.l4) |
| s61(1)(a) | paragraph | 633 | fork (F1) | where the named day goes when s 62 starts counting months; fork register F1; rule: wa-interpretation-time.l4 `the first day of a period`; wa-interpretation-time.l4 `reckon a period` (tests: wa-tests-time.l4) |
| s61(1)(b) | paragraph | 634 | fork (F1) | 'from' or 'after' a day excludes it; s 62 then starts on the next day (other reading kept as a second column); fork register F1; rule: wa-interpretation-time.l4 `the first day of a period`; wa-interpretation-time.l4 `reckon a period` (tests: wa-tests-time.l4) |
| s61(1)(c) | paragraph | 635 | fork (F3) | a time before a day whose last day is an excluded day rolls forward to the named day itself; fork register F3; rule: wa-interpretation-time.l4 `the time within a time before a day` (tests: wa-tests-time.l4) |
| s61(1)(d) | paragraph | 636 | encoded | wa-interpretation-time.l4 `the end of a period expressed to end on` (tests: wa-tests-time.l4) |
| s61(1)(e) | paragraph | 637 | fork (F2) | the roll applies to periods in months and years as well as days; fork register F2; rule: wa-interpretation-time.l4 `the next day that is not an excluded day, counting the day itself`; wa-interpretation-time.l4 `the end of a period whose last day by the calendar is` (tests: wa-tests-time.l4) |
| s61(1)(f) | paragraph | 638 | encoded | wa-interpretation-time.l4 `the number of days counted between two events` (tests: wa-tests-time.l4) |
| s61(1)(g) | paragraph | 639 | encoded | wa-interpretation-time.l4 `the number of days counted between two events` (tests: wa-tests-time.l4) |
| s61(1)(h) | paragraph | 640 | encoded | wa-interpretation-time.l4 `the next day that is not an excluded day, counting the day itself` (tests: wa-tests-time.l4) |
| s61(2) | subsection | 641 | encoded | wa-interpretation-time.l4 `is an excluded day` (tests: wa-tests-time.l4) |
| s62 | section | 642 | encoded | wa-interpretation-time.l4 `reckon a period`; wa-interpretation-time.l4 `reckon a period counting the named day as its first day, the other reading` (tests: wa-tests-time.l4) |
| s62(1) | subsection | 643 | encoded | wa-interpretation-time.l4 `reckon a period`; wa-interpretation-time.l4 `reckon a period counting the named day as its first day, the other reading` (tests: wa-tests-time.l4) |
| s62(2) | subsection | 644 | fork (F1) | month 'beginning on' a date: which date is the beginning of a period 'from' a day; fork register F1; rule: wa-interpretation-time.l4 `the last day of a period of months beginning on` (tests: wa-tests-time.l4) |
| s62(2)-example | example | 645 | encoded | wa-interpretation-time.l4 `the last day of a period of months beginning on` (tests: wa-tests-time.l4) |
| s62(3) | subsection | 646 | fork (F1) | as s 62(2) for 2 or more months; fork register F1; rule: wa-interpretation-time.l4 `the last day of a period of months beginning on` (tests: wa-tests-time.l4) |
| s62(3)-example | example | 647 | encoded | wa-interpretation-time.l4 `the last day of a period of months beginning on` (tests: wa-tests-time.l4) |
| s63 | section | 648-649 | encoded | wa-interpretation-time.l4 `the last day for an act or thing when no time may be fixed`; wa-interpretation-time.l4 `the act or thing must be done with all convenient speed and as often as occasion arises` (tests: wa-tests-time.l4) |
| s64 | section | 650 | encoded | wa-interpretation-time.l4 `an application to extend may be made after the time has expired` (tests: wa-tests-time.l4) |
| s64(1) | subsection | 651 | encoded | wa-interpretation-time.l4 `an application to extend may be made after the time has expired` (tests: wa-tests-time.l4) |
| s64(2) | subsection | 652 | encoded | wa-interpretation-time.l4 `an application to extend may be made after the time has expired` (tests: wa-tests-time.l4) |
| s65 | section | 653-654 | encoded | wa-interpretation-part8.l4 `the distance measured for the purposes of a written law between` (tests: wa-tests-part8.l4) |
| part-IX | heading | 655 | inert (1) | heading: not operative |
| s66 | section | 656 | encoded | wa-interpretation-part9.l4, its subsections (tests: wa-tests-part9.l4) |
| s66(1) | subsection | 657 | encoded | wa-interpretation-part9.l4 `they are rules of court` (tests: wa-tests-part9.l4) |
| s66(2) | subsection | 658 | encoded | wa-interpretation-part9.l4 `the authority's power includes making rules of court for the purpose of the written law` (tests: wa-tests-part9.l4) |
| s66(3) | subsection | 659 | encoded | wa-interpretation-part9.l4 `the authority may make rules or orders, including about costs, for the practice and procedure in exercising the jurisdiction` (tests: wa-tests-part9.l4) |
| s67 | section | 660 | encoded | wa-interpretation-part9.l4, its subsections (tests: wa-tests-part9.l4) |
| s67(1) | subsection | 661 | encoded | wa-interpretation-part9.l4 `the kind of offence it is` (tests: wa-tests-part9.l4) |
| s67(1a) | subsection | 662 | encoded | wa-interpretation-part9.l4 `the kind of offence it is` (tests: wa-tests-part9.l4) |
| s67(2) | subsection | 663 | encoded | wa-interpretation-part9.l4 `the kind of offence it is` (tests: wa-tests-part9.l4) |
| s67(3) | subsection | 664 | encoded | wa-interpretation-part9.l4 `the Act that sets out the procedure for prosecuting and dealing with offences` (tests: wa-tests-part9.l4) |
| s67(4) | deleted | 665 | repealed or blank in this text | the text shows: [(4)	deleted] |
| s67(5) | subsection | 666 | encoded | wa-interpretation-part9.l4 `section 67 limits the operation of Part 3 of the Children's Court of Western Australia Act 1988` (tests: wa-tests-part9.l4) |
| s67-history | history | 667 | inert (1) | history note recording amendments: not operative |
| s68 | section-deleted | 668 | repealed or blank in this text | the text shows: [68.	Deleted: No. 78 of 1995 s. 56.] |
| s69 | section | 669 | encoded | wa-interpretation-part9.l4, its subsections (tests: wa-tests-part9.l4) |
| s69(1) | subsection | 670 | encoded | wa-interpretation-part9.l4 `the enactment refers to the person` (tests: wa-tests-part9.l4) |
| s69(2) | subsection | 671 | encoded | wa-interpretation-part9.l4 `the penalty or sum is payable to the body corporate` (tests: wa-tests-part9.l4) |
| s69-history | history | 672 | inert (1) | history note recording amendments: not operative |
| s70 | section-deleted | 673 | repealed or blank in this text | the text shows: [70.	Deleted: No. 78 of 1995 s. 56.] |
| s71 | section | 674 | encoded | wa-interpretation-part9.l4, its subsections (tests: wa-tests-part9.l4) |
| s71(1) | subsection | 675 | encoded | wa-interpretation-part9.l4 `the provisions of section 71(1)(d) to (f) have effect` (tests: wa-tests-part9.l4) |
| s71(1)(a) | paragraph | 676 | encoded | wa-interpretation-part9.l4 `the provisions of section 71(1)(d) to (f) have effect` (tests: wa-tests-part9.l4) |
| s71(1)(b) | paragraph | 677 | encoded | wa-interpretation-part9.l4 `the provisions of section 71(1)(d) to (f) have effect` (tests: wa-tests-part9.l4) |
| s71(1)(c) | paragraph | 678-679 | encoded | wa-interpretation-part9.l4 `the provisions of section 71(1)(d) to (f) have effect` (tests: wa-tests-part9.l4) |
| s71(1)(d) | paragraph | 680 | encoded | wa-interpretation-part9.l4 `the obligation to do the act or thing continues` (tests: wa-tests-part9.l4) |
| s71(1)(e) | paragraph | 681 | encoded | wa-interpretation-part9.l4 `the number of separate and further offences`; wa-interpretation-part9.l4 `the person is guilty of separate and further offences` (tests: wa-tests-part9.l4) |
| s71(1)(f) | paragraph | 682 | encoded | wa-interpretation-part9.l4 `the penalty for each separate and further offence` (tests: wa-tests-part9.l4) |
| s71(2) | subsection | 683 | encoded | wa-interpretation-part9.l4 `the number of separate and further offences`; wa-interpretation-part9.l4 `the daily offences of section 71(2) arise` (tests: wa-tests-part9.l4) |
| s71(2)(a) | paragraph | 684 | encoded | wa-interpretation-part9.l4 `the number of separate and further offences`; wa-interpretation-part9.l4 `the daily offences of section 71(2) arise` (tests: wa-tests-part9.l4) |
| s71(2)(b) | paragraph | 685 | encoded | wa-interpretation-part9.l4 `the number of separate and further offences`; wa-interpretation-part9.l4 `the daily offences of section 71(2) arise` (tests: wa-tests-part9.l4) |
| s71(2)(c) | paragraph | 686-687 | encoded | wa-interpretation-part9.l4 `the number of separate and further offences`; wa-interpretation-part9.l4 `the daily offences of section 71(2) arise` (tests: wa-tests-part9.l4) |
| s72 | section | 688 | encoded | wa-interpretation-part9.l4, its subsections (tests: wa-tests-part9.l4) |
| s72(1) | subsection | 689 | encoded | wa-interpretation-part9.l4 `what is an offence with the penalty specified` (tests: wa-tests-part9.l4) |
| s72(1)(a) | paragraph | 690 | encoded | wa-interpretation-part9.l4 `what is an offence with the penalty specified` (tests: wa-tests-part9.l4) |
| s72(1)(b) | paragraph | 691 | encoded | wa-interpretation-part9.l4 `what is an offence with the penalty specified` (tests: wa-tests-part9.l4) |
| s72(1)(c) | paragraph | 692-693 | encoded | wa-interpretation-part9.l4 `what is an offence with the penalty specified` (tests: wa-tests-part9.l4) |
| s72(2) | subsection | 694 | encoded | wa-interpretation-part9.l4 `the penalty on conviction` (tests: wa-tests-part9.l4) |
| s72(3) | subsection | 695 | encoded | wa-interpretation-part9.l4 `a reference to a section or subsection of an Act in section 72 includes` (tests: wa-tests-part9.l4) |
| s72(4) | subsection | 696 | encoded | wa-interpretation-part9.l4 `section 72 applies to it, with any modifications that are necessary` (tests: wa-tests-part9.l4) |
| s72-history | history | 697 | inert (1) | history note recording amendments: not operative |
| part-X | heading | 698 | inert (1) | heading: not operative |
| s73 | section | 699-700 | encoded | wa-interpretation-part10.l4 `the day the State is deemed to have been established, for the applicability of Imperial Acts`; wa-interpretation-part10.l4 `the Imperial Act was enacted before the State is deemed to have been established` (tests: wa-tests-part10.l4) |
| s74 | section | 701-702 | encoded | wa-interpretation-part10.l4 `the deviation invalidates the form used` (tests: wa-tests-part10.l4) |
| s75 | section | 703 | encoded | wa-interpretation-time.l4, its subsections (tests: wa-tests-time.l4) |
| s75(1) | subsection | 704 | fork (F7) | if the contrary is proved the Act gives no rule; the proved day is taken; fork register F7; rule: wa-interpretation-time.l4 `the day service by post is deemed effected` (tests: wa-tests-time.l4) |
| s75(2) | subsection | 705 | encoded | wa-interpretation-part10.l4 `service may be effected either by registered post or by certified mail` (tests: wa-tests-part10.l4) |
| s75(3) | subsection | 706 | encoded | wa-interpretation-part10.l4 `service may be effected either by registered post or by certified mail`; wa-interpretation-part10.l4 `section 75(1) applies` (tests: wa-tests-part10.l4) |
| s76 | section | 707-708 | fork (F10) | manners (a) to (c) are open to every person, a corporation included; fork register F10; rule: wa-interpretation-part10.l4 `service may be effected in the manner` (tests: wa-tests-part10.l4) |
| s76(a) | paragraph | 709 | encoded | wa-interpretation-part10.l4 `service may be effected in the manner` (tests: wa-tests-part10.l4) |
| s76(b) | paragraph | 710 | encoded | wa-interpretation-part10.l4 `service may be effected in the manner` (tests: wa-tests-part10.l4) |
| s76(c) | paragraph | 711 | encoded | wa-interpretation-part10.l4 `service may be effected in the manner` (tests: wa-tests-part10.l4) |
| s76(d) | paragraph | 712 | encoded | wa-interpretation-part10.l4 `service may be effected in the manner` (tests: wa-tests-part10.l4) |
| s76A | section | 713 | encoded | wa-interpretation-part10.l4, its subsections (tests: wa-tests-part10.l4) |
| s76A(1) | subsection | 714 | encoded | wa-interpretation-part10.l4 `the provision has the effect and validity it would have had if the Australia Acts had been in operation then` (tests: wa-tests-part10.l4) |
| s76A(1)(a) | paragraph | 715 | encoded | wa-interpretation-part10.l4 `the provision has the effect and validity it would have had if the Australia Acts had been in operation then` (tests: wa-tests-part10.l4) |
| s76A(1)(b) | paragraph | 716-717 | encoded | wa-interpretation-part10.l4 `the provision has the effect and validity it would have had if the Australia Acts had been in operation then` (tests: wa-tests-part10.l4) |
| s76A(2) | subsection | 718 | encoded | wa-interpretation-part10.l4 `subsection (1) is to be given effect so as to bring it about` (tests: wa-tests-part10.l4) |
| s76A(2)(a) | paragraph | 719 | encoded | wa-interpretation-part10.l4 `subsection (1) is to be given effect so as to bring it about` (tests: wa-tests-part10.l4) |
| s76A(2)(b) | paragraph | 720 | encoded | wa-interpretation-part10.l4 `subsection (1) is to be given effect so as to bring it about` (tests: wa-tests-part10.l4) |
| s76A-history | history | 721 | inert (1) | history note recording amendments: not operative |
| s77 | section | 722 | encoded | wa-interpretation-part10.l4, its subsections (tests: wa-tests-part10.l4) |
| s77(1) | subsection | 723 | inert (2) | repeals the Interpretation Act 1918 (repeal of another Act: machinery, no rule for a person) |
| s77(2) | subsection | 724 | encoded | wa-interpretation-part10.l4 `section 11 of the Interpretation Act 1918 continues to apply to the Act` (tests: wa-tests-part10.l4) |
| s77(3) | subsection | 725 | encoded | wa-interpretation-part10.l4 `the enactment is presumed to have amended the law so as to affect the construction of the earlier law` (tests: wa-tests-part10.l4) |
| s77(4) | subsection | 726 | encoded | wa-interpretation-part10.l4 `section 47(2) and the Second Schedule of the Interpretation Act 1918 continue to apply to the Act`; wa-interpretation-time.l4 `the last day to make the complaint and commence the proceedings` (tests: wa-tests-part10.l4, wa-tests-time.l4) |
| notes | note | 729-730 | inert (1) | notes: not operative |
| compilation-header | table-header | 731-735 | inert (1) | table heading: not operative |
| compilation-row-1 | table-row | 736-739 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-2 | table-row | 740-743 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-3 | table-row | 744-747 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-4 | table-row | 748-751 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-5 | table-row | 752-755 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-6 | table-row | 756-759 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-7 | table-row | 760-763 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-8 | table-row | 764 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-9 | table-row | 765-768 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-10 | table-row | 769-772 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-11 | table-row | 773-776 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-12 | table-row | 777-780 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-13 | table-row | 781-784 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-14 | table-row | 785-788 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-15 | table-row | 789 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-16 | table-row | 790-793 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-17 | table-row | 794-797 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-18 | table-row | 798-801 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-19 | table-row | 802-805 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-20 | table-row | 806-809 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-21 | table-row | 810-813 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-22 | table-row | 814 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-23 | table-row | 815-818 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-24 | table-row | 819-822 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-25 | table-row | 823-826 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-26 | table-row | 827-830 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-27 | table-row | 831-834 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-28 | table-row | 835 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-29 | table-row | 836-839 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-30 | table-row | 840-843 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-31 | table-row | 844-847 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-32 | table-row | 848-851 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-33 | table-row | 852-855 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-34 | table-row | 856-859 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-35 | table-row | 860 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-36 | table-row | 861-864 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-37 | table-row | 865-868 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-38 | table-row | 869-872 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-39 | table-row | 873-876 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-40 | table-row | 877-880 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-41 | table-row | 881 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-42 | table-row | 882-885 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-43 | table-row | 886-889 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-44 | table-row | 890-893 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-45 | table-row | 894-897 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-46 | table-row | 898-901 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-reprint-47 | table-row | 902 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-48 | table-row | 903-906 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-49 | table-row | 907-910 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-50 | table-row | 911-914 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-51 | table-row | 915-918 | inert (1) | compilation table: publication history of the Act, creates no rule |
| compilation-row-52 | table-row | 919-922 | inert (1) | compilation table: publication history of the Act, creates no rule |
| uncommenced-header | table-header | 923-928 | inert (1) | not operative: a provision of another Act (Assisted Reproductive Technology and Surrogacy Act 2025 Pt 17 Div 12) marked 'To be proclaimed', not in force |
| uncommenced-row-1 | table-row | 929-932 | inert (1) | not operative: a provision of another Act (Assisted Reproductive Technology and Surrogacy Act 2025 Pt 17 Div 12) marked 'To be proclaimed', not in force |
| other-notes-heading | heading | 933 | inert (1) | heading: not operative |
| fn1 | footnote | 934 | encoded | wa-interpretation-part10.l4 `section 11 of the Interpretation Act 1918 continues to apply to the Act` (tests: wa-tests-part10.l4) |
| fn1-s11 | footnote | 936 | encoded | wa-interpretation-part10.l4, its subsections (tests: wa-tests-part10.l4) |
| fn1-s11(1) | footnote | 937 | encoded | wa-interpretation-part10.l4 `the power may be exercised at any time after the passing of the Act`; wa-interpretation-part10.l4 `the exercise may confer a right or impose an obligation before the Act comes into operation` (tests: wa-tests-part10.l4) |
| fn1-s11(2) | footnote | 938 | encoded | wa-interpretation-part10.l4 `the exercise is deemed as valid and effectual as if section 11 as re-enacted in 1975 had been in operation` (tests: wa-tests-part10.l4) |
| fn1-s11(3) | footnote | 939 | encoded | wa-interpretation-part10.l4 `a reference to an Act in section 11 includes it` (tests: wa-tests-part10.l4) |
| fn2 | footnote | 941 | inert (1) | note 2: a cross-reference ('Now see the Public Sector Management Act 1994'), creates no rule |
| fn3 | footnote | 942 | inert (3) | note 3: shows the Australian Citizenship Act 1948 repealed ('Repealed by the Australian Citizenship (Transitionals and Consequentials) Act 2007 s. 42') |
| fn4 | footnote | 943 | encoded | wa-interpretation-part10.l4 `section 47(2) and the Second Schedule of the Interpretation Act 1918 continue to apply to the Act` (tests: wa-tests-part10.l4) |
| fn4-s47 | footnote | 945 | encoded | wa-interpretation-part10.l4, its subsections (tests: wa-tests-part10.l4) |
| fn4-s47(1) | footnote | 946 | encoded | wa-interpretation-part10.l4 `the section of the Second Schedule is incorporated as an enactment in the Act` (tests: wa-tests-part10.l4) |
| fn4-s47(2) | footnote | 947 | encoded | wa-interpretation-part10.l4 `the reference is deemed to be to the corresponding section of the Second Schedule to the Interpretation Act 1918` (tests: wa-tests-part10.l4) |
| fn4-schedule | schedule | 948 | inert (1) | heading 'The Second Schedule.': not operative |
| fn4-schedule-A | schedule | 949-950 | encoded | wa-interpretation-part10.l4 `the Act by which section A of the Second Schedule says informations, complaints and proceedings are heard and penalties enforced` (tests: wa-tests-part10.l4) |
| fn4-schedule-B | schedule | 951-952 | encoded | wa-interpretation-time.l4 `the period the Second Schedule section allows` (tests: wa-tests-time.l4) |
| fn4-schedule-C | schedule | 953-954 | encoded | wa-interpretation-time.l4 `the period the Second Schedule section allows` (tests: wa-tests-time.l4) |
| fn4-schedule-D | schedule | 955-956 | encoded | wa-interpretation-time.l4 `the period the Second Schedule section allows` (tests: wa-tests-time.l4) |
| fn4-schedule-E | schedule | 957-958 | encoded | wa-interpretation-time.l4 `the period the Second Schedule section allows` (tests: wa-tests-time.l4) |
| fn4-schedule-F | schedule | 959-960 | encoded | wa-interpretation-part10.l4 `the proceeding may be quashed, vacated or removed on that ground` (tests: wa-tests-part10.l4) |
| fn4-schedule-G | schedule | 961-962 | encoded | wa-interpretation-part10.l4 `the plaintiff recovers in the action`; wa-interpretation-part10.l4 `the defendant recovers full costs as between solicitor and client`; wa-interpretation-part10.l4 `the plaintiff who obtained a verdict has costs against the defendant` (tests: wa-tests-part10.l4) |
| fn4-schedule-H | schedule | 963-964 | encoded | wa-interpretation-part10.l4 `an action lies against the defendant`; wa-interpretation-part10.l4 `the Court may award the defendant treble costs or such portion of them as it thinks fit` (tests: wa-tests-part10.l4) |
| fn5 | footnote | 966 | inert (1) | not operative: note 5 is a note about a transitional provision of another Act (Sunday Observance Laws Amendment and Repeal Act 1997 s 4(2)) and states no rule of this Act |
| index-heading | table-header | 969-972 | inert (1) | table heading: not operative |
| idx[act] | index-row | 973 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Act] | index-row | 974 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Act of the Commonwealth] | index-row | 975 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[affidavit] | index-row | 976 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[alternative offence] | index-row | 977 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[amend] | index-row | 978 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[ASIC Law] | index-row | 979 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[ASIC Regulations] | index-row | 980 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[association] | index-row | 981 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Auditor General] | index-row | 982 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Australia] | index-row | 983 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Australia Acts] | index-row | 984 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[bank holiday] | index-row | 985 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[bankrupt and bankrupt or a person whose affairs are under insolvency laws] | index-row | 986 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[book] | index-row | 987 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[British possession] | index-row | 988 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[by-law] | index-row | 989 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[cause] | index-row | 990 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[chief executive officer] | index-row | 991 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Children’s Court] | index-row | 992 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[commencement] | index-row | 993 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Commissioner of State Revenue] | index-row | 994 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Commonwealth] | index-row | 995 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Commonwealth Act] | index-row | 996 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Consolidated Account] | index-row | 997 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[contravene] | index-row | 998 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Corporations Law] | index-row | 999 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Corporations Regulations] | index-row | 1000 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Court of Appeal] | index-row | 1001 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[court of summary jurisdiction] | index-row | 1002 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Crown] | index-row | 1003 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[death] | index-row | 1004 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[de facto partner] | index-row | 1005 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[de facto relationship] | index-row | 1006 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[definition] | index-row | 1007 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[District Court] | index-row | 1008 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[District Court judge] | index-row | 1009 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[document] | index-row | 1010 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[enactment] | index-row | 1011 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[estate] | index-row | 1012 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[excluded day] | index-row | 1013 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Family Court] | index-row | 1014 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Family Court of Western Australia] | index-row | 1015 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[fee] | index-row | 1016 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[financial year] | index-row | 1017 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[first person] | index-row | 1018 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[function] | index-row | 1019 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Gazette] | index-row | 1020 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Government] | index-row | 1021 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Government Gazette] | index-row | 1022 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Government Printer] | index-row | 1023 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Governor] | index-row | 1024 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Her Majesty] | index-row | 1025 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[His Majesty] | index-row | 1026 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Imperial Act] | index-row | 1027 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[indictable offence] | index-row | 1028 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[individual] | index-row | 1029 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[issue] | index-row | 1030 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[JP] | index-row | 1031 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[judge] | index-row | 1032 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[justice] | index-row | 1033 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[justice of the peace] | index-row | 1034 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[King] | index-row | 1035 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[land] | index-row | 1036 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[law of the State] | index-row | 1037 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[lawyer] | index-row | 1038 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[legal practitioner] | index-row | 1039 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[licence] | index-row | 1040 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[local government] | index-row | 1041 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[local government district] | index-row | 1042 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[local law] | index-row | 1043 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[magistrate] | index-row | 1044 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Magistrates Court] | index-row | 1045 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[may] | index-row | 1046 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Minister] | index-row | 1047 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Minister for Public Sector Management] | index-row | 1048 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[month] | index-row | 1049 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[oath] | index-row | 1050 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[or] | index-row | 1051 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[other] | index-row | 1052 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[otherwise] | index-row | 1053 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[paragraph] | index-row | 1054 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[parent] | index-row | 1055 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Parliament] | index-row | 1056 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[penalty] | index-row | 1057 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[perform] | index-row | 1058 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[person] | index-row | 1059 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[police officer] | index-row | 1060 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[power] | index-row | 1061 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[prescribed] | index-row | 1062 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[proclamation] | index-row | 1063 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[publication] | index-row | 1064 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[public half-holiday] | index-row | 1065 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[public holiday] | index-row | 1066 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Public Sector Commissioner] | index-row | 1067 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Public Service] | index-row | 1068 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[public service holiday] | index-row | 1069 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[public service officer] | index-row | 1070 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Queen] | index-row | 1071 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[regional local government] | index-row | 1072 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[regional subsidiary] | index-row | 1073 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[regulation] | index-row | 1074 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[regulations] | index-row | 1075 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[repeal] | index-row | 1076 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Royal Assent] | index-row | 1077 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[rule] | index-row | 1078 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[rules of court] | index-row | 1079 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[sell] | index-row | 1080 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[shall] | index-row | 1081 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[sign] | index-row | 1082 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[simple offence] | index-row | 1083 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[sitting days] | index-row | 1084 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[specified] | index-row | 1085 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[spouse] | index-row | 1086 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Standards Australia] | index-row | 1087 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[State] | index-row | 1088 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[State Administrative Tribunal] | index-row | 1089 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[statutory declaration] | index-row | 1090 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[subsidiary legislation] | index-row | 1091 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[summary conviction] | index-row | 1092 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[summary conviction penalty] | index-row | 1093 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Supreme Court] | index-row | 1094 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[swear] | index-row | 1095 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Territory] | index-row | 1096 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[the Act] | index-row | 1097 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[the State] | index-row | 1098 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[this State] | index-row | 1099 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[under] | index-row | 1100 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[United Kingdom] | index-row | 1101 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[Valuer-General] | index-row | 1102 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[WA legislation website] | index-row | 1103 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[will] | index-row | 1104 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[words] | index-row | 1105 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[writing] | index-row | 1106 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[written law] | index-row | 1107 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| idx[year] | index-row | 1108 | inert (1) | index of defined terms: repeats terms defined (and encoded) elsewhere, creates no rule |
| copyright | note | 1111-1119 | inert (1) | copyright notice: not operative |
| s13(1)[Commonwealth Act]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `the Act that Commonwealth Act means in section 13`; wa-interpretation-part2.l4 `it is a law of the State` (tests: wa-tests-part2.l4) |
| s13A(1)[de facto relationship]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `a de facto relationship exists between two persons` (tests: wa-tests-part2.l4) |
| s13A(4)[de facto partner]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `a person is a de facto partner` (tests: wa-tests-part2.l4) |
| s13A(5)[first person]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `the other person is the de facto partner of the first person` (tests: wa-tests-part2.l4) |
| s15A(1)[paragraph]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `a reference to a paragraph includes` (tests: wa-tests-part2.l4) |
| s17[or, other, otherwise]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `the word is read disjunctively and not as implying similarity` (tests: wa-tests-part2.l4) |
| s42(8)[regulations]#def | term | (embedded) | encoded | wa-interpretation-part6.l4 `section 42 treats it as regulations` (tests: wa-tests-part6.l4) |
| s43(9)[specified]#def | term | (embedded) | encoded | wa-interpretation-part6.l4 `the power may be exercised`; wa-interpretation-part6.l4 `it is specified for section 43(7) and (8)` (tests: wa-tests-part6.l4) |
| s44(2)[the Act]#def | term | (embedded) | encoded | wa-interpretation-part6.l4 `the Act a reference in subsidiary legislation to the Act means` (tests: wa-tests-part6.l4) |
| s52(2)[cause]#def | term | (embedded) | encoded | wa-interpretation-part7.l4 `the cause is included in section 52(1)(b)` (tests: wa-tests-part7.l4) |
| s54(2)[association]#def | term | (embedded) | encoded | wa-interpretation-part7.l4 `the least number of members that make a quorum, with a fixed number of members` (tests: wa-tests-part7.l4) |
| s56(1)[may]#def | term | (embedded) | encoded | wa-interpretation-part7.l4 `what the word means` (tests: wa-tests-part7.l4) |
| s56(2)[shall]#def | term | (embedded) | encoded | wa-interpretation-part7.l4 `what the word means` (tests: wa-tests-part7.l4) |
| s61(2)[excluded day]#def | term | (embedded) | encoded | wa-interpretation-time.l4 `is an excluded day` (tests: wa-tests-time.l4) |
| s62(1)[month]#def | term | (embedded) | encoded | wa-interpretation-time.l4 `reckon a period`; wa-interpretation-time.l4 `reckon a period counting the named day as its first day, the other reading` (tests: wa-tests-time.l4) |
| s66(1)[rules of court]#def | term | (embedded) | encoded | wa-interpretation-part9.l4 `they are rules of court` (tests: wa-tests-part9.l4) |
| s13D(1)[bankrupt]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `the person is a bankrupt` (tests: wa-tests-part2.l4) |
| s13D(2)[a person whose affairs are under insolvency laws]#def | term | (embedded) | encoded | wa-interpretation-part2.l4 `the person is a bankrupt or a person whose affairs are under insolvency laws` (tests: wa-tests-part2.l4) |

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the licensing text (with `src:` line numbers of `../../registers/source-bundle/mrdoc_49111.txt`), the readings, the one taken, and where it is encoded and tested.
Where a case is settled by the text, it is not a fork; the last note lists the ones a reader might expect to find here.
F11 to F20 and the second instance under F3 were added in pass 2, from the independent test pass.
Their coverage rows keep the disposition `encoded` (the `fork` disposition belongs to the rows of F1 to F10, assigned in the first version and not re-run), with the function and tests in the `where` column; each entry names its rows.
Fork-list items that were already forks are cross-referenced in the table after F20.

**F1. What day a period "from" or "after" a day starts on, and what s 62 counts months from.**
Text: s 61(1)(b) (src:634) "where a period of time is expressed to be reckoned from, or after, a specified day, that day shall not be included in the period"; s 61(1)(a) (src:633) a period that "begins at, on, or with" a day includes it; s 62(2) (src:644) a period of one month "shall be reckoned from the date on which it is to begin to the date in the next month numerically corresponding, less one"; s 62(3) (src:646) the same for 2 or more months.
Reading A (taken): "the date on which it is to begin" is the first day of the period as s 61 fixes it, which is the day after the named day for a period "from" or "after" it; s 62 then counts from that day.
So a month "from 15 January" begins on 16 January and ends on 15 February.
Reading B: s 62 counts from the named day itself, so a month "from 15 January" ends on 14 February.
Rows: s 61(1)(a), s 61(1)(b), s 62(2), s 62(3).
Encoded: `reckon a period` (reading A); `reckon a period counting the named day as its first day, the other reading` (reading B), kept so the answer table can print both columns.
Tested in `wa-tests-time.l4` for both readings.
Of the seven worked cases the readings give a different final day for two (cases 2 and 4); the other five converge once a Saturday or Sunday end is moved.

**F2. Does the rule that moves a last day off an excluded day apply to periods in months and years?**
Text: s 61(1)(e) (src:637) "where the time limited for the doing of a thing expires or falls upon an excluded day, the thing may be done on the next day that is not an excluded day".
Reading A (taken): it applies to every period, whatever its unit, because the text has no limit.
Reading B: only to periods in days.
Rows: s 61(1)(e).
Encoded: `the end of a period whose last day by the calendar is`, used by every unit.
Tested: `wa-tests-time.l4` (1 year from 29 Feb 2024 with 28 Feb 2025 a holiday ends on Monday 3 March 2025), and cases 1, 3, 4 and 5 below.

**F3. A time "before" a day whose last day is an excluded day.**
Text: s 61(1)(c) (src:635) "where anything is to be done within a time before a specified day, the time shall not include that day"; s 61(1)(e) as in F2.
Reading A (taken): (e) applies as written, so a time that ends on the Sunday before a Monday hearing may be met on the Monday, which is the named day itself.
Reading B: (c) wins and the act must be done by the last non-excluded day before the named day.
Rows: s 61(1)(c).
Encoded: `the time within a time before a day`, whose end uses the same roll as F2.
Tested: `wa-tests-time.l4` (7 days before Monday 10 March 2025: first day 3 March, last day by the calendar 9 March, last day for doing the thing 10 March), `wa-cases-seat.l4`.
The reading is the least comfortable one in the encoding, because it lets the act be done on the day the text says the time does not include; the text does not resolve it.

Second instance, found by the independent test pass: 10 days before Sunday 11 February 2024 are 1 to 10 February, and the last day by the calendar is Saturday 10 February.
Reading A (taken) lets the thing be done on Monday 12 February, which is the day AFTER the named day.
Reading B ends the time on Friday 9 February.
Encoded: `the time within a time before a day` is reading A, the default; `the time within a time before a day, rolling back from an excluded last day, the other reading` is reading B, built on `the previous day that is not an excluded day, counting the day itself`.
Tested for both in `wa-tests-time-forks.l4`; the seat layer calls reading A only.
Why A is the default: s 61(1)(e) applies to "the time limited for the doing of a thing" that "expires or falls upon an excluded day" and has no exception for a time counted back from a named day, and (c) says only what the time does not include.
Reading B's date is never later than reading A's, so a person who acts by reading B's date meets the deadline on either reading.

**F4. A written law passed or made on 1 July 1984.**
Text: s 3(3) (src:121) "passed or made after the commencement of this Act"; s 2 (src:114) "This Act shall come into operation on 1 July 1984"; s 21 (src:375) a written law comes into operation at the beginning of its commencement day.
Reading A (taken): the Act is in operation from the first moment of 1 July 1984, so a law passed or made on that day is passed after the commencement.
Reading B: only a law passed from 2 July 1984.
Rows: s 3(3).
Encoded: `counts as passed or made after the commencement for ss 17, 25, 43(6), 50 and 64`.
Tested: `wa-tests-part3.l4`, `wa-tests-part6.l4`, `wa-tests-part7.l4`, `wa-cases-seat.l4`.

**F5. "After the expiration of 7 days from the publication" (s 42(4)).**
Text: s 42(4)(a), (b) (src:480, 481).
Reading A (taken): the publication day is excluded ("from", s 61(1)(b)), the 7 days are the next 7 days, and the regulations take effect on the day after they expire, the 8th day after publication.
Reading B: they take effect on the 7th day after publication.
Rows: s 42(4).
Encoded: `the first day the amended or substituted regulations take effect`.
Tested: `wa-tests-part6.l4`, `wa-cases-seat.l4`.

**F6. "Within 21 days of the passing of the resolution" (s 42(5)).**
Text: src:482.
Reading A (taken): "of" is read like "from": the day of passing is excluded and the 21st day after it is the last.
Reading B: the day of passing counts, and the last day is the 20th day after it.
Rows: s 42(5).
Encoded: `the last day for publishing notice of the resolution`.
Tested: `wa-tests-part6.l4`.

**F7. Service by post when the contrary is proved (s 75(1)).**
Text: src:704 "unless the contrary is proved, to have been effected at the time when the letter would have been delivered in the ordinary course of post".
The Act does not say what follows once the contrary is proved.
Reading A (taken): the day proved is the day of service.
Reading B: the Act gives no answer and the result is NOTHING.
Rows: s 75(1).
Encoded: `the day service by post is deemed effected`; the Act does not say how long the ordinary course of post takes, so the caller supplies that day.
Tested: `wa-tests-time.l4`, `wa-cases-seat.l4`.

**F8. A heading to a section where a marginal note exists (s 32(2)).**
Text: src:430 a marginal note or footnote is not part of the written law, and "in a context where there is no marginal note with respect to the relevant provision" a heading to a section is not part of it either.
Reading A: with a marginal note present, a heading is part of the written law (by implication).
Reading B (taken): the text says nothing about that case, so the answer is NOTHING.
Rows: s 32(2).
Encoded: `forms part of the written law under section 32`; tested in `wa-tests-part4.l4`.

**F9. "At least one half" of an odd number of members (s 54(2)(a)(i)).**
Text: src:601 "a number of members of the association equal to at least one half of the number of members provided for by the written law".
Reading A (taken): whole members, so one half of 5 (2.5) rounds up and the quorum is 3.
Reading B: 2.5, which no number of members equals, so no quorum could be formed.
Rows: s 54(2)(a)(i).
Encoded: `the least number of members that make a quorum, with a fixed number of members`; tested in `wa-tests-part7.l4` and `wa-cases-seat.l4`.

**F10. Who may be served in the manners of s 76 (a) to (c).**
Text: src:708 to 712: service "may be effected on the person to be served" by (a) delivering to them personally, (b) post, (c) leaving it at their usual or last known place of abode (or, for a principal of a business, place of business), (d) "in the case of a corporation or of an association of persons", delivering, leaving or posting it at its principal place of business or office in the State.
Reading A (taken): (a) to (c) are open for every person, a corporation included; (c)'s business limb needs a principal of a business; (d) needs a corporation or association.
Reading B: a corporation is served only under (d).
Rows: s 76.
Encoded: `service may be effected in the manner`; tested in `wa-tests-part10.l4` and `wa-cases-seat.l4`.

**F11. What "made under any written law and having legislative effect" qualifies in the definition of "subsidiary legislation" (s 5).**
Text: s 5 (src:241) "subsidiary legislation means any proclamation, regulation, rule, local law, bylaw, order, notice, rule of court, local or region planning scheme, resolution, or other instrument, made under any written law and having legislative effect".
Reading A: the qualifier governs every item in the list, so a proclamation or notice that is not made under a written law, or has no legislative effect, is not subsidiary legislation; the comma before "made" sets the qualifier apart from the last item alone.
Reading B: it governs only "other instrument".
Taken: neither is computed.
The entry lists each named kind, and the last item with its qualifier ("other instrument made under any written law and having legislative effect"), so asking whether a proclamation is among the things the definition lists is TRUE on both readings; whether a particular proclamation was made under a written law and has legislative effect is asked nowhere.
Rows: s5[subsidiary legislation].
Encoded: `section 5 term: subsidiary legislation`, whose list also holds the printed meaning as one member and "local planning scheme" and "region planning scheme" (the distribution of "local or region planning scheme").
Tested: `wa-tests-s5-definitions.l4`, `wa-tests-s5-meanings.l4`.

**F12. "14 sitting days" in s 42(2) against "the period of 14 days" in s 42(3).**
Text: s 42(2) (src:477) notice given "within 14 sitting days of such House after such regulations have been laid before it"; s 42(3) (src:478) "the period of 14 days referred to in that subsection, or part of that period, does not occur in the same session of Parliament or during the same Parliament".
Reading A (taken): the period is 14 sitting days of the House, as (2), the operative text, says; (3) calls the same period "14 days" without the word "sitting".
Reading B: (3) shows that the period is 14 calendar days.
The last day for the notice is the 14th sitting day after the laying under A and the 14th day after it under B.
Rows: s 42(2), s 42(3).
Encoded: `the last day for giving notice of a resolution disallowing the regulations` (the 14th of the sitting days after the laying; the caller lists the sitting days, because s 5 "sitting days" means days on which the House actually sits).
Tested: `wa-tests-part6.l4`.

**F13. May subsidiary legislation name a day before it is published (s 41(1)(b))?**
Text: s 41(1)(b) (src:472) subsidiary legislation comes into operation "on the day of publication, or where another day is specified or provided for in the subsidiary legislation, on that day"; s 23(a) (src:380) for an Act, a power to fix a commencement day "does not include power to fix a day prior to the day on which the proclamation fixing the day is published", unless express provision is made.
Section 41(2) (src:473) repeats s 23(b) (different days for different provisions) for subsidiary legislation; nothing repeats s 23(a).
Reading A (taken): s 41(1)(b) puts no limit on the specified day, so a day before publication is returned as the day of coming into operation.
Reading B: the bar of s 23(a) applies to subsidiary legislation by analogy.
The reason for A is the drafting: s 41(2) copies s 23(b) and s 41 does not copy s 23(a), which reads as deliberate; the text does not say that it is.
Rows: s 41(1)(b).
Encoded: `the day subsidiary legislation comes into operation` returns the specified day whatever it is; the bar is encoded for Acts only, in `the power to fix a day extends to a day not prior to publication`.
Tested: `wa-tests-time-forks.l4` (a day before publication), `wa-tests-time.l4`.

**F14. "Unless" constructions: what follows when the exception is met.**
Text: Second Schedule G (src:962) the plaintiff "shall not have costs against the defendant unless the Judge before whom the trial is held shall certify his approbation of the action and of the verdict obtained thereon"; Second Schedule H (src:964) "No action shall lie against any Justice of the Peace ... unless there is direct proof of corruption or malice"; the 1918 Act s 11(1) (src:937, note 1) the power "may, unless the Act otherwise provides, be exercised at any time after the passing".
Reading A (taken): an "unless" states an exception and no more; when it is met the text does not say that the opposite holds (that the plaintiff has costs, that an action lies, that the power may not be exercised), so the answer is NOTHING.
Reading B: "unless" is read as "if and only if not", so the opposite is TRUE.
Rows: fn4-schedule-G, fn4-schedule-H, fn1-s11(1).
Encoded: `the plaintiff who obtained a verdict has costs against the defendant` (JUST FALSE without the certificate, NOTHING with it); `an action lies against the defendant` (JUST FALSE when the defendant is one the paragraph protects, the thing was done in carrying the provisions into effect and there is no direct proof of corruption or malice; NOTHING otherwise); `the power may be exercised at any time after the passing of the Act` (JUST TRUE when the conditions hold and the Act does not otherwise provide, NOTHING otherwise).
Tested: `wa-tests-part10.l4`.

**F15. FALSE or NOTHING for a law that a s 3(3)-gated section does not reach (ss 17, 25, 43(6), 50, 64).**
Text: s 3(3) (src:121) a reference in s 17, 25, 43(6), 50 or 64 to a law "passed or made after the commencement of this Act" does not include an enactment which continues or directly amends, but does not repeal entirely, the text of an existing written law; s 17 (src:347), s 25(5) (src:407), s 43(6) (src:498), s 50(3) (src:573), s 64 (src:650).
Reading A (taken): for a law that does not count as passed or made after the commencement, the section says nothing about it, so the answer is NOTHING.
Reading B: the section does not apply to it, so what the section would allow or deem is FALSE (the power may not be exercised, the fine is not capped at $1 000, and so on).
Rows: s17, s25(5), s43(6), s50(3), s64.
Encoded: each of the five functions has `IF counts as passed or made after the commencement for ss 17, 25, 43(6), 50 and 64 ... ELSE NOTHING`.
Tested: `wa-tests-part2.l4` (s 17), `wa-tests-part3.l4` (s 25(5)), `wa-tests-part6.l4` (s 43(6)), `wa-tests-part7.l4` (s 50(3)) and `wa-tests-time.l4` (s 64); each has a test with the date 30 June 1984 and a test with the continuing-text input TRUE, and both give NOTHING.

**F16. Does a law that repeals an earlier law and re-enacts its text "continue" that text (s 3(3))?**
Text: s 3(3) (src:121) "any enactment which continues or directly amends, but does not repeal entirely, the text of an existing written law".
Reading A: a re-enactment carries the old words on, so it "continues" the text and falls outside the five gated sections.
Reading B: it repeals the old law entirely, so the exception ("but does not repeal entirely") does not fit it and it counts as passed after the commencement.
The text does not decide.
Taken: neither; every one of the five gated functions takes `it continues or directly amends, but does not repeal entirely, the text of an existing written law` as a yes-or-no input, and the seat layer asks it as "Does that enactment only continue, or directly amend, the text of an earlier written law (without repealing it entirely)?", so the caller decides for a re-enacting law.
Rows: s3(3).
Encoded: `counts as passed or made after the commencement for ss 17, 25, 43(6), 50 and 64`.
Tested: as F15, with the input TRUE.

**F17. A body whose number of members is a range, and the number in office is outside the range (s 54(2)(a)(ii)).**
Text: s 54(2)(a)(ii) (src:602) "if the number of members provided for by the written law is not a fixed number but is within a range having a maximum or minimum, at least one half of the number of members in office if that number is within the range".
Reading A (taken): when the number in office is outside the range, the sub-paragraph gives no quorum, so the answer is NOTHING.
Reading B: a fallback to one half of the nearest limit of the range, or of the fixed number in (i); the text gives none.
Rows: s54(2)(a)(ii).
Encoded: `the least number of members that make a quorum, with a range of members`, whose second input says whether the number in office is within the range; the caller says.
Tested: `wa-tests-part7.l4` (7 and 8 in the range give 4; outside it gives NOTHING).

**F18. Is the day on which the act or thing is finally done a day of failure (s 71(1)(e), s 71(2))?**
Text: s 71(1)(e) (src:681) and s 71(2) (src:687) a separate and further offence "in respect of each day after the day of the conviction during which the failure to do that act or thing continues".
Reading A: the day on which the thing is done is not a day during which the failure continues, so the last failure day is the day before it.
Reading B: the failure continues during that day until the thing is done, so it counts.
Taken: neither is decided by code; `the number of separate and further offences` counts the days after the conviction up to and including the last day the caller names as a day on which the failure continues, and gives 0 where that day is not after the conviction.
The caller applies A or B when choosing that day.
Rows: s71(1)(e).
Tested: `wa-tests-part9.l4` (conviction on 6 January 2025; last failure day 10 January gives 4; 7 January gives 1; 6 January or earlier gives 0).

**F19. "Includes" is not exhaustive: s 19(2) and the `includes` terms of s 5.**
Text: s 19(2) (src:356) the material that may be considered "includes —" eight kinds; s 5 (src:128 onward) the many terms defined by "includes".
Reading A (taken): a thing that is not listed is neither inside nor outside, so the answer is NOTHING.
Reading B: the list is closed in effect and an unlisted thing is outside (FALSE), as with a term defined by `means`.
Rows: s19(2) and the `includes` terms of s 5, among them s5[act], s5[document], s5[land], s5[person or any word or expression descriptive of a person], s5[power].
Encoded: `material of this kind is among the material that may be considered` returns NOTHING for `material of some other kind`; the s 5 table marks `the list is complete` FALSE for an `includes` term, so `the definition of the word lists the thing` returns NOTHING for an unlisted thing and JUST FALSE only where a term defined by `means` has a complete list.
Tested: `wa-tests-part2.l4`, `wa-tests-s5-definitions.l4`, `wa-tests-s5-meanings.l4`.

**F20. An item the Act does not name under "perform", "sign", "sell" and "penalty" (s 5).**
Text: s 5 "perform, in relation to functions, includes the exercise of a power, responsibility, authority or jurisdiction" (src:206); "sign includes the affixing or making of a seal, mark or thumbprint" (src:233); "sell includes barter, exchange, offer to sell and expose for sale" (src:232); "penalty means a fine, imprisonment, or other form of punishment, including the suspension or cancellation of a licence, registration or permit and disqualification from obtaining a licence, registration or permit" (src:205).
The question is whether a typed signature is signing, a gift is selling, or suspension of something other than a licence, registration or permit is a penalty.
Reading A (taken): the Act's list is not exhaustive and gives no test for an unlisted item, so the answer is NOTHING.
Reading B: the listed items mark the limit, so an unlisted item is outside.
This is F19 applied to four terms.
Rows: s5[perform], s5[sign], s5[sell], s5[penalty].
Encoded: as F19.
Tested: `wa-tests-s5-meanings.l4` (a typed signature, a gift, the abandonment of a power, the suspension of a driving licence and a caution all give NOTHING).

Items on the fix list that are already forks, so are cross-referenced and not repeated.

| fix-list item | fork | where |
|---|---|---|
| s 61(1)(e) backwards from a day under s 61(1)(c) | F3 | second instance and second function added in pass 2 |
| s 62(2) and s 61(1)(b), "after 15 January" | F1 | the text covers a period "from, or after" a day; a month after 15 January ends on 15 February under A and 14 February under B |
| s 42(5), the passing day | F6 | "of" is read like "from" |
| s 42(4), the first effective day | F5 | the 8th day after publication under A |
| s 32(2), a heading where a marginal note exists | F8 | NOTHING |

Not forks, settled by the text: that the last day is inside the period (s 61(1)(d), src:636: a period expressed to end at, on or with a day, or to continue to or until it, includes that day); that a period "after" an event excludes that day as "from" does (s 61(1)(b)); that a "year" is 12 months (s 5, src:256) so that "5 years" is 60 months for s 62(3); that a public halfholiday is not an excluded day (s 61(2), src:641, does not list it, though s 5 defines it, src:214).

## Answer table: the seven worked cases

"From" a day: the day itself is left out (s 61(1)(b)).
A year is 12 months (s 5, src:256).
A month is a calendar month, reckoned under s 62.
An end on a Saturday, Sunday or holiday moves to the next day that is not one (s 61(1)(e)).
No holiday is assumed in this table; `wa-cases-seat.l4` shows how a listed holiday moves a day.
Weekdays were worked out by hand and are written in the comments of `wa-cases-seat.l4` and `wa-tests-time.l4`.
The right-hand column is reading B of F1, computed by `reckon a period counting the named day as its first day, the other reading`; the text does not choose between them.

| # | case | first day that counts | last day by the calendar | last day to act (reading A, taken) | last day to act (reading B) | sections |
|---|---|---|---|---|---|---|
| 1 | three years from 2025-07-16 | 2025-07-17 | 2028-07-16 (Sunday) | **2028-07-17** (Monday) | 2028-07-17 | 5, 61(1)(b), 62(3), 61(1)(e) |
| 2 | five years from 2025-01-15 | 2025-01-16 | 2030-01-15 (Tuesday) | **2030-01-15** | 2030-01-14 | 5, 61(1)(b), 62(3) |
| 3 | five years from 2025-09-01 | 2025-09-02 | 2030-09-01 (Sunday) | **2030-09-02** (Monday) | 2030-09-02 | 5, 61(1)(b), 62(3), 61(1)(e) |
| 4 | thirty days from 2026-01-01 | 2026-01-02 | 2026-01-31 (Saturday) | **2026-02-02** (Monday) | 2026-01-30 | 61(1)(b), 61(1)(e) |
| 5 | two months from 2025-12-31 | 2026-01-01 | 2026-02-28 (Saturday) | **2026-03-02** (Monday) | 2026-03-02 | 61(1)(b), 62(3), 61(1)(e) |
| 6 | one month from 2024-01-31 | 2024-02-01 | 2024-02-29 (Thursday) | **2024-02-29** | 2024-02-29 | 61(1)(b), 62(1), 62(2) |
| 7 | one year from 2024-02-29 | 2024-03-01 | 2025-02-28 (Friday) | **2025-02-28** | 2025-02-28 | 5, 61(1)(b), 62(3) |

How each is reached, under reading A.
Case 5: 31 December is left out, so the two months begin on 1 January 2026; s 62(3) reckons from that date to the date numerically corresponding in the second month, 1 March, less one, which is 28 February 2026, a Saturday, so the thing may be done on Monday 2 March.
Case 6: 31 January is left out, the month begins on 1 February 2024, which is the first day of a month, so s 62(2) (for a month beginning on any other date) does not apply and the period is the calendar month of s 62(1), ending on the last day of February, the 29th.
Case 7: 29 February 2024 is left out, the 12 months begin on 1 March 2024 and end on 28 February 2025; the date "numerically corresponding, less one" is 1 March 2025 less one.
All seven are asserted under reading A in `wa-cases-seat.l4` (as the seat's questions) and in `wa-tests-time.l4`, and under reading B in `wa-tests-time.l4`.
The text is not silent on any of the seven.
It is silent on "N weeks": no section defines a week or counts one, so a period in weeks returns NOTHING (asserted in `wa-tests-time.l4` and `wa-cases-seat.l4`).

## What the text turns out to say (numbered findings)

Each finding ends "Asserted." where a test or case asserts it, with the file.

1. A period "from" or "after" a day starts on the next day, and a period in months or years then ends on the date with the same number as the named day: five years from 15 January 2025 end on 15 January 2030, not on 14 January (F1, reading A).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
2. The rule that moves a last day off a Saturday, Sunday or holiday applies to periods in months and in years as much as in days (s 61(1)(e)): three years from 16 July 2025 end on Sunday 16 July 2028 and the last day to act is Monday 17 July 2028 (F2).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
3. Thirty days from 1 January 2026 end on Saturday 31 January and the last day to act is Monday 2 February 2026; if that Monday is a public holiday, Tuesday 3 February (s 61(1)(b), (e), (2)).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
4. A period in months that begins on a day with no match in the month it runs to ends on that month's last day (a month beginning on 30 or 31 January ends on 28 February, or 29 in a leap year; s 62(2)'s own example), and one that begins on the first day of a month ends on the last day of a month: one month from 31 January 2024 ends on 29 February 2024; one year from 29 February 2024 ends on 28 February 2025 (ss 62(2), (3), 5).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
5. The Act never defines or counts a week: a period in weeks has no answer in this Act.
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4` (NOTHING).
6. A period expressed to end at, on or with a day, or to continue to or until it, includes that day (s 61(1)(d)); so "until 31 March" includes 31 March.
Asserted: `wa-tests-time.l4`.
7. "At least" or "not less than" a number of days between two events, and "clear days", leave out both event days; any other number of days leaves out the first and includes the second (s 61(1)(f), (g)): between 1 and 15 March 2025 there are 13 clear days and 14 days.
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
8. A time "within N days before" a day leaves out the named day, but when that makes the last day a Sunday, s 61(1)(e) read as written moves it forward to the Monday, which is the named day (F3).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
9. A public halfholiday is not an excluded day: s 61(2) lists Saturday, Sunday, a public service holiday, a bank holiday and a public holiday, and s 5 defines the halfholiday without s 61 using it.
Not asserted; the module has no half-holiday input by design, so no case can give one.
10. An Act assented to on or after 1 July 1984 and naming no day of its own comes into operation on the 28th day after the day of assent (10 March 2025 gives 7 April 2025); one assented to before 1 July 1984, on the day of assent; one reserved on or after 1 July 1984, on the day the assent is proclaimed (s 20).
For an Act reserved before 1 July 1984 the text says nothing.
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4` (including the NOTHING).
11. A written law is in operation from the first moment of its commencement day (s 21): at midnight at the start of that day, not from some later hour.
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
12. A law passed or made on 1 July 1984 is "after the commencement" for ss 17, 25, 43(6), 50 and 64, unless it only continues or directly amends existing text (F4).
Asserted: `wa-tests-part3.l4`, `wa-tests-part6.l4`, `wa-tests-part7.l4`.
13. An instrument or notice made early under s 25 takes effect on the later of the commencement day and the day it would have taken effect had the provision already commenced (s 25(3)).
Asserted: `wa-tests-part3.l4`, `wa-cases-seat.l4`.
14. Regulations amended or substituted by both Houses take effect on the 8th day after the notice is published, not the 7th (s 42(4), F5); notice of the resolution must be published within 21 days of the passing, the 21st day after it being the last (s 42(5), F6).
Asserted: `wa-tests-part6.l4`, `wa-cases-seat.l4`.
15. The sixth sitting day after the publication day is the last day to lay regulations, and the fourteenth after the laying is the last day for notice of disallowance; the days counted are the House's own sitting days, which the Act does not list, so the caller supplies them (s 42(1), (2)).
Asserted: `wa-tests-part6.l4`.
16. A regulation, rule, local law or bylaw can fine up to $1000, but only where the enactment that gives the power was passed or made on or after 1 July 1984 and does not merely continue or directly amend existing text; otherwise the Act gives no limit (s 43(6)).
Asserted: `wa-tests-part6.l4`, `wa-cases-seat.l4`.
17. After a conviction for failing to do a required act, each day after the day of conviction on which the failure continues is a separate and further offence, $50 each unless the written law provides otherwise: convicted on Monday 6 January 2025 and still not done on Friday 10 January, four further offences (s 71).
Asserted: `wa-tests-part9.l4`, `wa-cases-seat.l4`.
18. The power to issue or refuse a licence is discretionary, and s 51(2) creates no right to appeal or seek review; it only leaves in place a right that another written law gives (s 51).
Asserted: `wa-tests-part7.l4`, `wa-cases-seat.l4` (NOTHING when no other law gives one).
19. A court document may be served, and a warrant executed, on a Saturday, Sunday or public holiday (s 48A).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
20. A power to extend a time may be used after the time has expired, but only for written laws passed or made after the commencement and not merely continuing existing text; for others the Act says nothing (s 64).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
21. Service by post is deemed effected at the time the letter would have been delivered in the ordinary course of post, which the Act does not quantify, and if the contrary is proved the Act gives no rule (F7).
Asserted: `wa-tests-time.l4`, `wa-cases-seat.l4`.
22. A board of five with a fixed number decides by a quorum of three, because one half of five is 2.5 and the Act speaks of "equal to at least one half" of the number of members; four present with two agreeing is not a majority of four (F9).
Asserted: `wa-tests-part7.l4`, `wa-cases-seat.l4`.
23. Under the 1918 Act's Second Schedule (kept alive by s 77(4) for older Acts), a complaint must be made within one, three, six or twelve months of the offence by sections B, C, D, E; one month after an offence on Wednesday 15 January 2025 ends on Saturday 15 February and, with the Monday a public holiday, the complaint can be made on Tuesday 18 February.
Asserted: `wa-tests-part10.l4`, `wa-cases-seat.l4`.
24. A word is looked up in s 5 under any of its names ("this State" as well as "the State", "JP" as well as "justice of the peace") and `act` and `Act` are two entries.
A hand-written test caught what the generated per-entry tests could not: the table's first draft named the `person` entry "person or any word or expression descriptive of a person", because the term-splitting rule took everything before "includes", and the generated assertions agreed with it because they used the same names.
Fixed with a names override; the hand-written `person` test is what failed.
Asserted: `wa-tests-s5-definitions.l4`, `wa-tests-s5-key-terms.l4`.
25. The Act's definitions of "Commonwealth Act" differ: s 5 says an Act passed by the Parliament of the Commonwealth, and s 13(1), for that section only, the Australian Citizenship Act 1948.
Asserted: `wa-tests-part2.l4` (s 13(1)) and `wa-tests-s5-definitions.l4` (s 5).

## What the text does not answer

Each of these returns an explicit not-covered value (NOTHING) or asks the caller, and a test asserts it where noted.
1. A period in weeks (asserted).
2. A period in months or years counted back from a day, as in "within 2 months before a hearing": s 62 reckons forward only (asserted in `wa-tests-time.l4`).
3. An Act reserved for Her Majesty's pleasure before 1 July 1984: s 20(3) speaks only of Acts reserved on or after that date (asserted in `wa-tests-time.l4`, `wa-cases-seat.l4`).
4. How long the ordinary course of post takes, and what follows once the contrary is proved (s 75(1)).
5. Which days are public holidays, bank holidays or public service holidays: s 61(2) and s 5 point to the Public and Bank Holidays Act 1972 and the Public Service Act 1978, which are not among the sources.
6. The day the Australia Acts commenced (s 76A) and the day the Interpretation Act Amendment Act 1975 came into operation (note 1).
7. What follows from the date of 1 June 1829 in s 73: the section fixes a date for deciding which Imperial Acts apply and does not say which do (asserted: the module returns only the date comparison).
8. Whether a heading is part of a written law where a marginal note exists (s 32(2), F8; asserted).
9. What a quorum is for a body of fewer than 3 members (s 54; asserted).
10. Who must publish the notice in s 42(5), and who is the claimant under s 56(2) and s 63: the text names no one.
11. When service by leaving a document at an address is complete (s 76 gives the manners, not a deemed time).
12. A period counted in hours or minutes: the Act counts days, months and years (ss 61, 62); the only part of a day it speaks of is the moment a law commences (s 21).

## Reading a result: FALSE and NOTHING

The rule in force for this row, from 2026-10-29 (assumed, not ruled by a lawyer). This row had already answered `NOTHING` for an "includes" list and for silence; the rule makes the test the text's own words.

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if", "as long as" or "unless", or a list the text closes with "only" or an equivalent. Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the function answers `NOTHING`, and a comment on that branch names which of those it is. The function's name carries the scope its `FALSE` claims ("under section 47 ...", not "may I ..."), and a seat question that asks Act-wide inherits `NOTHING` wherever the Act points outside itself.

In plain words: `JUST FALSE` is the Act's own "no"; `NOTHING` is "the Act does not say". A caller must not read `NOTHING` as "no".

**Checked on 2026-10-29 under this rule.** A second reader read the 15 literal `JUST FALSE` lines in 12 functions and 10 further rows in 9 functions whose `FALSE` is computed (65 module `MAYBE BOOLEAN` bodies and 11 in the seat), against the text. Changed to `NOTHING` (14 assertions restated, each with a `-- RECONCILED 2026-10-29` comment quoting the original; three of them are in the independent test author's file, where the author had written `JUST FALSE`): the lookup `the definition of the word lists the thing` for three entries whose list the text does not close, "chief executive officer" ("has the meaning given by the Public Sector Management Act 1994 and" adds limbs), "prescribed" (limb (b) "includes") and "publication" (limb (c) is a descriptive catch-all; this follows the module's own rule for a descriptive meaning), by setting `the list is complete` to FALSE; s 19(2) ("includes ... Without limiting the generality of subsection (1)") for the three kinds of material tied to "before the time when the provision was enacted"; s 54(1) ("may be performed by a majority", no "only"); and the seat question on s 54(2)(b) for a decision made with a quorum present that a majority did not make. Kept, because the text's own words say no: the 14 other literal lines (a flat "shall not", "does not ... unless", "no ... shall ... unless", "not exceeding") and the eight "means" entries. Nine of those 14 rest on a flat "shall not" with none of the rule's four words, which the reader counted as the text saying no in its own words; that is a reading for a lawyer to confirm.

**Marginal, kept, for a lawyer:** s 76(c) and (d) (`service may be effected in the manner`; an "if" inside a list of permissions that nothing closes with "only"); the no-quorum limb of s 54(2)(b) (a plain "if" in a deeming); s 50(1) (`the other power is also deemed conferred`; "as are reasonably necessary"); s 45A (`a power to prescribe a fee allows it to recover the expenditure`; the text's "unless" is about relevance, the name asks the wider question); and the seat question `Am I in time if I do it on a given day` (s 61(1)(h), "if"), which a reader would have answered `NOTHING` because the period itself is fixed by other law.

**Not changed, and open:** three plain-`BOOLEAN` functions answer `FALSE` for a catch-all value (`a person with none of those statuses`, s 13(2); `for some other reason`, s 19(1); `any other expenditure`, s 45A(2)); under the rule they would be `MAYBE BOOLEAN` with `NOTHING`. The names of the four Second Schedule functions (`the proceeding may be quashed, vacated or removed on that ground`, `the plaintiff recovers in the action`, `the plaintiff who obtained a verdict has costs against the defendant`, `an action lies against the defendant`) and of several others do not carry their section, so as named they claim more than the text; their `FALSE` rests on the text's own "no ... shall" and "unless", and a rename, not a change of answer, is what the rule asks. Function names were not changed in this pass.

## Known limits (stated, not modelled)

Each of these is a place where the encoding does less than the text says, or does it in a way a reader might not expect.
None is reworked in this version; each is recorded so that it is not mistaken for coverage.
They are sorted by how they show.

Silent, because the encoding returns an answer and nothing marks the limit:
- A bundle held as one yes-or-no input: s 25(1)(a) to (e) (`the power is of a kind the section lists` stands for the five powers in the list), s 76(d) (one input for "a corporation or an association of persons, incorporated or not"), and the persons of Second Schedule H (one input, `the defendant is one of the persons the paragraph names, or a person acting for or under one of them`, for the Justice of the Peace, Officer of Police, Policeman, Constable, Peace Officer and any other person in the Government's employ authorised to carry the provisions into effect).
  The caller decides whether the facts fit the printed list, and a wrong yes gives a confident TRUE.
- s 13A(2): the nine indicators are counted (`the number of indicators present`) and do not enter `a de facto relationship exists between two persons`, so the encoding cannot be asked whether a given indicator is essential (the text says none is), and s 13A(1)'s "2 persons" is built in, so a relationship between three persons cannot be asked.
- s 72(1): `what is an offence with the penalty specified` takes the place the penalty is written (the foot of a section, of a subsection, or of a section for specified subsections) and returns "a contravention of the subsection" without saying which subsection; the identity of the subsection is not an input.
- A lookup in the s 5 table is by exact string.
  No article, plural or case is normalised, so "a natural person" is listed under "individual" and "natural person" is not; a thing that is a paraphrase of a listed meaning answers NOTHING.

Loud, because there is no way to ask the question (no constructor exists for it, or the call must name the whole printed list):
- A bundle held as one constructor, so one item of the printed list cannot be asked about alone: s 15(1) to (3) (each of the three kinds is one constructor holding its printed list, "a Part, Chapter, section, schedule, appendix or form" and so on), s 19(1)(b) ("ambiguous or obscure", and "manifestly absurd or is unreasonable", each one constructor), s 50(2)(b) (the eight things a licence-like power may grant are one constructor), s 52(1) ("to remove or suspend" and "to reappoint or reinstate" are one constructor each), s 57(b) (a defect in the appointment or qualification of a member, deputy or alternate is one constructor), s 59(1)(e) ("amended or revoked" is one constructor), s 61(1)(a), (b), (d) and (f) ("begin at, on, or with" is one constructor, "reckoned from, or after" is one, the "end at, on, or with ... continue to or until" of (d) is one function, and "at least" and "not less than" are one constructor, beside "clear days").
  The Act's own words treat the members of each list alike, which is why they are held together; where they would differ, the encoding does not see it.
- Tables that are not rules: the compilation table, the uncommenced provisions table and the bracketed note under "Defined terms" ("The list is not part of the law") are rows in the coverage table (inert, reason 1) and are not modelled; the uncommenced provision (Assisted Reproductive Technology and Surrogacy Act 2025 Pt. 17 Div. 12) is not applied.
- Dates and units the text does not give: the commencement day of the Australia Acts (s 76A), which is not in the text, so the caller says whether a provision came before it; no unit for hours, a business day or a time zone, because the Act counts days, months and years only.
- s 75(1): the encoding invents no postal interval.
  The Act does not say how long the ordinary course of post takes, and the caller supplies the day (fork F7).

## What the stable binary does not accept (found while writing)

These are things this encoding had to be written around on `l4 1.6.98` (and `1.6.102`, which agrees on every module).
Loud, because the compiler errors:
- A constructor pattern with record fields, `WHEN ctor WITH field`, is rejected; patterns bind positionally, `WHEN ctor x THEN`.
- A constructor named `A` in `DECLARE ... IS ONE OF` was rejected (the article of `IS A` is the likely clash); other single letters were not tried.
- A record built on one line needs commas between fields (`WITH a IS 1, b IS 2`); without them the parse stops at the second `IS`.
- `YMD` is missing from the prelude; every module writes dates as `Date day month year`, and this encoding defines no shim for it.
- `find`, `length`, `head` and `last` are absent; `filter`, `map`, `elem`, `sum`, recursion and `CONSIDER ... WHEN c FOLLOWED BY rest` / `WHEN EMPTY` do the same work.
- An inline `CONSIDER` cannot sit in a one-line `#ASSERT`; each such test calls a small helper function instead.
- In a mixfix name the parameters must appear in the `GIVEN` in the order they appear in the name; a mismatch is an error naming the function.
- `Day (x's f)` needs its parentheses, because function application binds tighter than the genitive.
Silent, because nothing errors:
- `add months` clamps to the last day of a shorter month rather than running into the next; the module therefore compares the day of the month before subtracting one for "less one", and this is the kind of thing a wrong rule would still compile.
- `l4 run` prints each assertion twice (once as a diagnostic, once as an `Evaluation[n]` block), so counting the lines "assertion satisfied" gives twice the number of assertions; count the `Evaluation[` lines, as `check.sh` does.
- `check.sh` counts assertions and errors only; it does not see a different TRACE outcome, and the encoding contains no trace.

## What `check.sh` prints

Run as `L4=<l4-stable-98> L4_MAIN=<l4-stable-102> ./check.sh` in this folder, on 2026-10-29 after the fix list was applied, exit status 0.
The first version's run, the baseline for this one, was 28 modules, 1213 satisfied, 0 failed, 0 refused, 0 expected red, every module `same`; this run adds three test files and 274 assertions (1487 in all), and no module is red, refused or different on the main build.
After that run the lead rewrote every date as `Date day month year` and removed the shim, together with the one assertion that tested it (`YMD shim` in `wa-tests-time.l4`); that leaves `wa-tests-time.l4` at 160 and the total at 1486, with every other count as printed here.
Also run: `python3 -I srcrefs.py check --refs ../../registers/source-bundle/mrdoc_49111.txt wa-*.l4` and the same with `--strict`, which each printed `srcrefs check: 606 src: lines, 350 runs, 432 locators, 0 problems`.
The first version had run `--refs` only (521 src: lines, 273 runs, 350 locators, 0 problems); `--strict` found 11 problems in it, all of them in this encoding's own text (a locator narrower than its run, or a locator with no quote above it in its block), and they are fixed.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.102 (main, e4f2553, 2026-10-26)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wa-cases-seat.l4                               0       109       0        0         0 |      0       109       0        0  same
wa-interpretation-nouns.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part1.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part10.l4                    0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part2.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part3.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part4.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part5.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part6.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part7.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part8.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-part9.l4                     0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-s5-definitions.l4            0         0       0        0         0 |      0         0       0        0  same
wa-interpretation-time.l4                      0         0       0        0         0 |      0         0       0        0  same
wa-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
wa-tests-part1.l4                              0        12       0        0         0 |      0        12       0        0  same
wa-tests-part10.l4                             0        85       0        0         0 |      0        85       0        0  same
wa-tests-part2.l4                              0       116       0        0         0 |      0       116       0        0  same
wa-tests-part3.l4                              0        23       0        0         0 |      0        23       0        0  same
wa-tests-part4.l4                              0        24       0        0         0 |      0        24       0        0  same
wa-tests-part5.l4                              0        38       0        0         0 |      0        38       0        0  same
wa-tests-part6-45a4.l4                         0        11       0        0         0 |      0        11       0        0  same
wa-tests-part6.l4                              0       113       0        0         0 |      0       113       0        0  same
wa-tests-part7.l4                              0       100       0        0         0 |      0       100       0        0  same
wa-tests-part8.l4                              0         9       0        0         0 |      0         9       0        0  same
wa-tests-part9.l4                              0        58       0        0         0 |      0        58       0        0  same
wa-tests-s5-definitions.l4                     0       305       0        0         0 |      0       305       0        0  same
wa-tests-s5-key-terms.l4                       0        60       0        0         0 |      0        60       0        0  same
wa-tests-s5-meanings.l4                        0       246       0        0         0 |      0       246       0        0  same
wa-tests-time-forks.l4                         0        17       0        0         0 |      0        17       0        0  same
wa-tests-time.l4                               0       161       0        0         0 |      0       161       0        0  same
TOTAL (31 modules)                             0      1487       0        0           |      0      1487       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Before this encoding is worth relying on

1. A domain expert (a Western Australian lawyer) should read it against the official text, not the converter's rendering: the reading choices F1 to F20 are the places to start, and F1, F2 and F3 are the ones that change a deadline.
2. The public holidays, bank holidays and public service holidays of an area are not encoded; a caller must supply them, or a later encoding of the Public and Bank Holidays Act 1972 and the Public Service Act 1978 must supply them.
3. The case law on time computation is not here by design: the text governs, and where it is silent the encoding returns NOTHING.
4. The expected values were written by the encoder who wrote the rules.
   An independent test pass was run on the first version, as the lead reported it (the encoder did not see the assertions), and this version answers its fix list; no adversarial reading and no second independent pass of this version has been done.
5. The text is a converter rendering (`../../registers/source-bundle/mrdoc_49111.meta.json`); line numbers in the `src:` quotations are lines of that rendering and move if it is regenerated.
6. Nothing re-runs these numbers.
7. The seat layer's inputs have not been shown to anyone in the seat; the `@desc` wording is the encoder's.

## Process notes

`peeked`: nothing.
No existing encoding was read: not commons, not canon, not another run's directory, nothing under `~/.claude/`.
`inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` and `skills/encoding-a-subject/references/canon-deposit.md` of the repository were read, as the brief allows.

Early probe files were first written to the shared scratchpad directory outside `deposit/` by mistake; they were moved under `deposit/scratch/` the same hour, the empty stray directory was removed, and `deposit/scratch/` (templates, generator scripts, probes) was deleted before the report was returned.
The `.l4` modules are the output of those generators plus the hand-written test and seat files; the deposit holds the output, not the templates.

Two things went wrong during writing and are recorded here, neither being a finding about the Act.
A hand-written expected value in `wa-tests-part6.l4` (the sixth sitting day after publication on 3 March 2025) was first written as 13 March, a miscount of the list; the code returned 18 March, a recount of the list (4, 5, 11, 12, 13, 18 March) confirmed 18 March, and the expected value was corrected with a comment in the file.
This is the only expected value edited after a run in the first version.
The first draft of `wa-interpretation-part7.l4` guarded the range quorum of s 54(2)(a)(ii) with "at least 3 members in office"; the text has no such guard ("if that number is within the range"), so it was removed before the tests were written.

Other changes made after the first full run, so the record is honest about them: the fork numbering was made consecutive (F1 to F10) after the comments had used gaps; `NOT` was parenthesised everywhere; `wa-interpretation-part2.l4` gained the s 13(1) and s 13CA(1) definitions and `wa-interpretation-part6.l4` the s 43(9) definition, which an earlier pass had left to a neighbouring rule; the s 5 lead-in gained its own function.

Pass 2 (the fix list from the independent test pass, 2026-10-29): the scripts that rewrote the s 5 member lists and wrote `wa-tests-s5-meanings.l4` were run from `deposit/scratch-pass2/` and deleted with it.
The member lists were generated from the text of `../../registers/source-bundle/mrdoc_49111.txt`, not by hand: for each of the 55 entries the meaning phrase is the words after the first " means " on the entry's line, up to the closing semicolon or full stop, with non-breaking spaces turned into plain spaces as in the quote lines; the constituents are slices of that phrase, or a shared frame distributed over a printed list, and the choice of which entries to split was made by reading each phrase.
The tests for those 55 entries read the same lines by a different route (a split on " means "), and the whole file was run against the first version of the module as a control: 153 of its 246 assertions fail on it, and all 246 pass on the new one.
No independent test file was seen; only the lead's summary of it.
No existing encoding was read in pass 2 either.

## Changes to existing modules

The first version of this deposit was returned on 2026-10-29 with 28 modules and 1213 assertions satisfied.
This version answers the fix list that came from the independent test pass.
Every file named here changed since the first version; any file not named is byte-identical to it (checked with `diff -rq` against a copy taken before the first edit).

Sorted by how a reader meets the change:

Behaviour changes (a phrase the Act prints, which was answered NOTHING, or FALSE for an entry with a complete list, is now answered TRUE; every assertion of the first version still passes unedited):
- `wa-interpretation-s5-definitions.l4`: 55 entries that defined a term by `means` stored only the word; each now stores the meaning phrase exactly as printed (the words after "means", up to the semicolon) as its first member, and, where the printed meaning is a pair of alternatives, each constituent.
  Entries extended: the 55 (Act, affidavit, Auditor General, Australia, bank holiday, British possession, bylaw, Children's Court, commencement, Commissioner of State Revenue, Commonwealth, Commonwealth Act, Consolidated Account, Court of Appeal, definition, District Court, Family Court, financial year, Government, Government Printer, Imperial Act, individual, justice of the peace, lawyer, legal practitioner, local government, local law, magistrate, Magistrates Court, Minister for Public Sector Management, oath, Parliament, police officer, proclamation, public halfholiday, public holiday, Public Sector Commissioner, public service holiday, regional local government, regional subsidiary, regulation, Royal Assent, rule, sitting days, spouse, State, State Administrative Tribunal, statutory declaration, summary conviction, Supreme Court, Territory, the State, United Kingdom, ValuerGeneral, year).
  Constituents were added for affidavit, statutory declaration and oath (the two limbs, each also with its head noun), British possession (the two limbs, "any part of Her Majesty's dominions outside the United Kingdom" and the deeming rider) and public service holiday (the phrase without the converter's footnote marker "2", beside the phrase as printed).
  Entries checked and left holding the printed phrase alone, because the printed meaning is one qualified concept and not a list: the other 50 of the 55, among them Act (the "or by any Council" limb qualifies the same "Act or Ordinance", so it is no free-standing alternative), Government Printer, proclamation (a conjunction of two conditions) and Minister for Public Sector Management.
  The same fix, found by a sweep of the other `means` entries and not on the fix list, is applied to the `means` limb of three `means and includes` entries (Governor, Her Majesty, Standards Australia) and to the printed meaning of seven `means` entries that already listed constituents (amend, court of summary jurisdiction, District Court judge, enactment, judge, written law, subsidiary legislation) and the head phrase of Gazette.
  Entry `amend` also gained a limb it had lacked, "the doing of any 2 or more of such things simultaneously or by the same written law", which matters because its list is flagged complete.
  Held-as-one-string members extended under item 2 of the fix list: person (the printed phrase, "public body", "company", "association", "body of persons", with and without the article, and the printed third item), land (the printed phrase, "buildings", "other structures", "estate", "interest", "easement", "servitude", "right in or over land", with and without the article where it reads naturally), penalty (the printed phrase, "suspension", "cancellation", "disqualification", and "the suspension of a licence", "the cancellation of a registration", "disqualification from obtaining a permit" and so on for each of licence, registration and permit), estate ("any legal estate", "any legal interest", "any equitable estate", "any equitable interest"), perform ("the exercise of a power", "... of a responsibility", "... of an authority", "... of a jurisdiction", and the four nouns), sign ("the affixing of a seal", "the making of a mark" and so on, and the printed phrase) and subsidiary legislation ("local planning scheme", "region planning scheme").
  Checked and left whole as one concept, with the reason: act ("a series of acts or omissions" and "a series of acts and omissions" are each one thing, a series), amend ("substitute, in whole or in part"), book (each limb is one method or system with its approver), contravene, document (the long limb is one matter recorded by those means), Her Majesty ("the heirs and successors of the Sovereign" is a doublet naming one line of succession), parent (each limb is one relationship), prescribed, publication (limbs (b) and (c) are one contrivance or thing each, qualified as a whole by "by means of which any words or ideas may be ... conveyed"), writing.
  `the list is complete` is unchanged for every entry: a descriptive meaning stays incomplete, so an unlisted thing is NOTHING, and the 11 entries with a complete list (amend, Australia Acts, chief executive officer, court of summary jurisdiction, District Court judge, enactment, Gazette, judge, prescribed, publication, written law) still answer FALSE for an unlisted thing.
  A comment above the first entry says what a list holds.
- `wa-interpretation-part6.l4`: the type `Thing named in section 45A(4)` gained nine constructors, one for each constituent of the printed lists ("to grant", "to give", "to renew" for issue; "a registration", "a right", "a permit", "an authority", "an approval", "an exemption" for licence); the three bundle constructors and the function are unchanged.
- `wa-interpretation-time.l4`: two functions added after `the time within a time before a day` (`the previous day that is not an excluded day, counting the day itself` and `the time within a time before a day, rolling back from an excluded last day, the other reading`, fork F3); no existing function changed.

Documentation and bookkeeping changes (no behaviour):
- `wa-interpretation-time.l4`: a comment on s 41(1)(b) citing fork F13; extra `@ref` lines and quote lines on s 23, s 41(1), s 61(1)(e), s 62(1) so that `srcrefs.py check --strict` is clean.
- `wa-interpretation-part2.l4`: three locators widened to the whole quoted run (s 10(a), s 13CA(2), s 15A(1)).
- `wa-interpretation-part5.l4`: an `@ref s 37(1) (src:448)` added.
- `wa-interpretation-part6.l4`: the quote run of s 45(1) and (2) split into two runs, each above its own rule; a comment citing fork F12 instead of "finding in NOTES.md".
- `wa-interpretation-part7.l4`: two `@ref` lines added to s 54(2)(a)(i).
- `wa-interpretation-part9.l4`: the quote line of s 71(1)(e) repeated above the second rule that cites it.
- `coverage_data.py`: three rows relabelled (below).
- `NOTES.md`: this document.
- `encoding.json`: the module and test lists, the check numbers, and the `not_reviewed` statement.
- `PROGRESS.md`: a pass-2 status.

New files: `wa-tests-s5-meanings.l4` (246 assertions), `wa-tests-part6-45a4.l4` (11) and `wa-tests-time-forks.l4` (17).
No test of the first version was edited, and no expected value of the first version changed.

Rows relabelled in the coverage table: `uncommenced-header` and `uncommenced-row-1` (lines 923 to 932) and `fn5` (line 966), from `inert (2)` to `inert (1)`, with a plain reason ("not operative: ..."); the old reason, "amends nothing yet and affects no one now", was not a reason of machinery.
`s77(1)` and `s1` stay `inert (2)`.
The row count stays 790, and the dispositions stay 529 encoded, 241 inert, 13 fork, 7 repealed or blank; the inert reasons move from 235, 5 and 1 to 238, 2 and 1.

- **2026-10-29, the rule in "Reading a result: FALSE and NOTHING":** five layer-1 and seat changes from `JUST FALSE` to `NOTHING` (the three `the list is complete` flags in `wa-interpretation-s5-definitions.l4`; s 19(2) in `wa-interpretation-part2.l4`; s 54(1) in `wa-interpretation-part7.l4`; the s 54(2)(b) question in `wa-seat.l4`), and 14 assertions restated in `wa-tests-s5-definitions.l4` (3), `wa-tests-part2.l4` (3), `wa-tests-part7.l4` (3), `wa-cases-seat.l4` (2) and `tests-independent.l4` (3). `check.sh` after the change: 32 modules, 2,051 satisfied, 0 failed, 0 refused, every module `same` on 1.6.102.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage.py`, `coverage_data.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 417 numbered scenarios over the Act.
It then wrote `tests-independent.l4`: 565 assertions (496 for the scenarios and 69 for the seat questions), and ran it against the first version of this encoding with the stable binary.
`ANSWERS.md` is not kept in this folder; the scenario numbers in the `-- N.` comments of `tests-independent.l4` refer to it.
The encoder answered the test author's fix list without seeing the assertions.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the first version | 565 | 557 | 8 | 0 |
| after the repairs below and the reconciliation | 565 | 565 | 0 | 0 |

The 34 scenarios the encoding has no function for are the `-- GAP N.` lines at the end of the test file, with the scenario as the test author wrote it; the lead added them from `ANSWERS.md` by script, and the count is checked against the author's report.
The author counted 21 of its assertions as `NOT (... EQUALS JUST TRUE)` and 39 as `EQUALS NOTHING`, which pass for more than one answer; its positive control (an assertion written to fail) did fail, and 31 month-end cases of s 62 matched a small Python model it wrote, which checks that two programs agree on one reading and not that the reading is right.

**What the eight disagreements turned out to be.**

- **Two led to a repair (scenarios 15 and 34).**
  55 of the 106 s 5 entries are "X means Y" and the table stored an empty list for them, so the encoding recorded that a word is defined and not what it means.
  All 55 now store the printed meaning phrase as a member (written by script from the source line and read back by a test by a different route), with constituents added for affidavit, statutory declaration, oath and British possession; `wa-tests-s5-meanings.l4` (246 assertions) tests them, and 153 of those fail against the first version's s 5 module.
  The same sweep extended the lists the author found held as one string (person, land, penalty, estate, perform, sign, subsidiary legislation, and nine constructors for s 45A(4)); ten entries were checked and left whole, each with its reason in "Changes to existing modules".
- **One is a genuine fork (39b), registered as F11:** whether "made under any written law and having legislative effect" qualifies only "other instrument" (the encoding's reading) or the whole list in the s 5 definition of "subsidiary legislation".
- **Five were the test author's expectation, not the encoding (121, 166d, 355a, 356b, 358b).**
  Each expected `JUST FALSE` where the text says nothing or only lifts a bar ("shall not ... unless"), or where an "includes" list is open; the encoding answers `NOTHING`.

The six reconciled assertions are rewritten in place to `EQUALS NOTHING`, each with a `-- RECONCILED` comment that quotes the author's original and gives the reason; none is deleted.

The author also found that "within N days before a day" (s 61(1)(e)) rolls forward past an excluded last day: 10 days before Sunday 11 February 2024 gives 12 February, after the named day.
That reading is kept as the default (it follows the section as written) and registered as a second instance of F3; the other reading is a separate function, and `wa-tests-time-forks.l4` tests both.
The encoder registered F12 to F20 from the author's other ambiguities, relabelled the uncommenced-provisions rows from machinery to not operative, and brought `srcrefs.py check --strict` to 0 problems.

**Independence caveat.** No file of the lead's session was delivered into the test author's session.
The encoder's session received, after a context summary, the paths only of five other rows' triage files (AU, BC, CA, SG, UK), and a search of its tool calls finds no read of any of them.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 32 modules, 2051 satisfied, 0 failed, 0 refused, and every module `same` on the 1.6.102 build, run on 2026-10-29.
Dates in the author's file are written `Date day month year`, as in the encoding.
