# Supreme Court (General Civil Procedure) Rules 2025 (Vic) -- baseline encoding, the party

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the Rules are applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Rules; nothing existing was touched. The Rules are very large (about 1,030,000
characters, some 90 Orders), so the encoding takes the Orders a personal injury or group proceeding meets (see Scope). Six
modules:

- `scr-dates.l4` -- the date helpers and Order 3's counting rules (rr 3.01, 3.04, 3.08), used by every deadline.
- `scr-duties.l4` -- the steps a party must take within a time, as regulative rules (`PARTY ... MUST ... WITHIN ... HENCE
  ... LEST BREACH ... BECAUSE`), and the helper that runs one by `EVALTRACE` over what happened (the shape of the Civil
  Procedure Act 2010 encoding's helper). Nothing exported.
- `scr-process.l4` -- Orders 1, 3, 4, 5, 6, 7 (with r 8.04), 13, 14, 15 and 18A: 37 questions.
- `scr-judgment.l4` -- Orders 21, 22, 24, 25 and 26 Part 2: 22 questions.
- `scr-evidence.l4` -- Orders 29, 32, 33, 44, 48 and 51: 31 questions.
- `scr-costs.l4` -- Orders 62, 63 (Parts 1 to 3, with Appendix A Sections 1 and 4), 79 and 85: 22 questions.

The four question modules carry their own `@export` questions (as the Accident Compensation Act 1985 encoding's two
modules do), so each can be deployed on its own; each imports only the dates and duties modules and restates no rule of
another. The cases are one file per question module: `scr-cases-process.l4` (which also tests the date helpers),
`scr-cases-judgment.l4`, `scr-cases-evidence.l4`, `scr-cases-costs.l4`.

## Edition

- **Rules:** Supreme Court (General Civil Procedure) Rules 2025, S.R. No. 85/2025, Version No. 003, incorporating
  amendments as at 1 January 2026, deposited at `../../registers/source-bundle/supreme-court-general-civil-procedure-rules-2025.txt`
  (sha256 ee6404b9...ea2475 as committed), a plain-text conversion of the Word file the owner saved by hand on
  7 November 2026, reconverted the same day to restore the bullets of the note to r 7A.01 and the tick boxes in Forms
  42B, 42C and 42AA that the first conversion dropped (no provision encoded here changed; the first text's sha256 was
  5a7e31c5...f549ed) (see that file's `.meta.json`, the subject's `SOURCE-LICENSE.md` and `subjects/au/vic/README.md`). Not
  checked against the authorised PDF, which was not saved.
- **Commencement and the old Rules:** the Rules came into operation on 8 September 2025 (r 1.03(1)) and revoked the
  Supreme Court (General Civil Procedure) Rules 2015 (S.R. No. 103/2015) by r 1.03(2) and Schedule 1. r 1.05 applies them
  to every civil proceeding, begun before, on or after that day; r 1.05(3) keeps what was done under the 2015 Rules in a
  pending proceeding. The 2015 Rules are not deposited.
- **Parent and read-with law, restated narrowly** (a module cannot import across subjects): the Supreme Court Act 1986
  (the parent Act, `parent_act` in `subject.json`) ss 33E and 33J for Order 18A, where Part 4A sets the group proceeding
  law itself (encoded in `subjects/au/vic/supreme-court-act-1986/encodings/baseline-2026-11/`); the Legal Identity of
  Defendants (Organisational Child Abuse) Act 2018 ss 7(3) and 13 for Order 85 (encoded in
  `subjects/au/vic/legal-identity-of-defendants-organisational-child-abuse-act-2018/encodings/baseline-2026-11/`, whose
  counting of the 120 days and of r 85.02, 85.03 agrees with this one). The Civil Procedure Act 2010 (Part 4.4, summary
  judgment, which Order 22 serves) has its own encoding beside these; Order 22's tests are not restated here, only its
  times.
- **Numbers set elsewhere:** Appendix A (the scale, substituted by S.R. No. 127/2025 for work from 1 January 2026) is part
  of the deposited text and is encoded for its maxima. The penalty interest rate (r 79.06(2), Penalty Interest Rates Act
  1983) is not deposited: asked. Victorian public holidays (r 3.08(b)) are not deposited: asked where they matter (forks
  F2, F3).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read: a
deliberately wrong assertion (a junior counsel hourly maximum of $745), run once in a scratch file since deleted, showed as
`DiagnosticSeverity_Error`.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `scr-dates.l4` | 0 | 0 | 0 | 0 |
| `scr-duties.l4` | 0 | 0 | 0 | 0 |
| `scr-process.l4` | 0 | 0 | 0 | 0 |
| `scr-judgment.l4` | 0 | 0 | 0 | 0 |
| `scr-evidence.l4` | 0 | 0 | 0 | 0 |
| `scr-costs.l4` | 0 | 0 | 0 | 0 |
| `scr-cases-process.l4` | 0 | 0 | 168 | 168 |
| `scr-cases-judgment.l4` | 0 | 0 | 104 | 104 |
| `scr-cases-evidence.l4` | 0 | 0 | 110 | 110 |
| `scr-cases-costs.l4` | 0 | 0 | 85 | 85 |

467 assertions, all satisfied. Every expected value was worked by hand from the text, with the edges: every exported
question at least twice; every deadline on its last day and the day after; periods that run into the Christmas vacation
(24 December to 9 January, 17 days), with and without an order counting it; last days that fall on a weekend or (where
asked) a public holiday; periods of 5 days or less (weekends out) and of 7 days (weekends in); periods counted back from a
hearing or trial; months that end short (29 February); the r 26.08 comparison exactly at the offer, a dollar over, and with
post-offer interest taken out; the Appendix A bands at 5 and 10 years, 9.5 years, and the 30% increase and 31%.

## Seat

**The party** (all four question modules): the individual who is a party to a civil proceeding in the Supreme Court of
Victoria, usually the person bringing a personal injury claim (an injured worker, a road accident victim, a patient, a
survivor of child abuse, a group member in a class action, a minor or a person under disability through a litigation
guardian), and, where the Rules put a step on the other side, the individual answering the claim (an individual defendant:
the defence, discovery, the defendant's medical reports, a summary judgment affidavit). "Do the 2025 Rules apply to my
case?", "By when must I serve my statement of claim, my reports, my discovery?", "Has the defendant been served?", "Am I
taken to admit this?", "Must I sue through a litigation guardian, and is my settlement valid without the Court's
approval?", "Can I get judgment by default?", "Until when can I accept the offer, and what costs follow if I do not?",
"Which documents must I discover?", "Must I go to the defendant's doctor?", "Can I be made to give security for costs?",
"How much of my lawyer's hourly rate can I get back?", "Can the money paid into court for me be paid out?", "By when must
I name the proper defendant?".

No seat for the Court, the Associate Judges, the Prothonotary, the Senior Master, the Costs Court or the lawyers: their
orders, directions, leave, findings ("reasonable", "satisfied", "unreasonably", "special grounds", "genuine compromise")
and acts are asked as facts; what a lawyer may be made to pay (r 63.23) is asked from the client's seat.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed: Appendix A is in; the penalty interest rate and public
  holidays are inputs; the parent Act and the Legal Identity of Defendants Act are restated only where an Order's rule
  cannot be read without them, each with its section.
- **The actors the text names.** Followed: plaintiff, defendant, third party, applicant, group member, person under
  disability, litigation guardian, solicitor, barrister, medical expert, expert, non-party, NGO and proper defendant, the
  Court, the Prothonotary, the Senior Master, the judicial registrar, the Transport Accident Commission.
- **Judgments answered conditionally.** Followed (see above). A "reasonable time" for notice of trial (r 24.01(b)) and a
  pre-litigation offer (r 26.08.1(b)) are inputs.
- **The text's definitions worked out; borrowed terms asked.** Followed: "person under disability" (r 15.01), "pending
  proceeding" and "commencement date" (r 1.04), the documents required to be discovered (r 29.01.1(3), (4)), "business
  day" (r 26.01), "ordinarily applicable basis" (r 26.01, taken as the standard basis: no question reaches costs incurred
  before 1 April 2013), "bodily injury" (r 1.13, in a description) are worked out; "minor", "privilege", "tort",
  "domiciled", "unincorporated association" are asked.
- **One case.** One proceeding in the Supreme Court, seen by one party.
- **The text's terms with plain glosses.** Followed, in each `@desc`.
- **Operative rules in; machinery out.** Followed (see Scope).

## Scope

The focus was the whole of these Orders: 1 (r 1.05), 3, 4, 5, 6, 7, 13, 14, 15, 18A, 21, 22, 24, 25, 26, 29, 32, 33, 44,
48, 51, 62, 63, 79 and 85. Within them, every rule that gives a party a fact test, a time or an amount is in; rules that
only give the Court a power with no test, set a form, or run the Court's office are listed as out, with the reason.

**In (by Order):**

- **Order 1:** rr 1.03(1), 1.04, 1.05.
- **Order 3:** rr 3.01, 3.02(3) (with (1), (2) in the description), 3.04(1), 3.05(2), 3.06, 3.08.
- **Order 4:** rr 4.01, 4.04, 4.05, 4.06 (with r 1.12 and Order 58 as the exceptions).
- **Order 5:** rr 5.04(3), 5.08, 5.12.
- **Order 6:** rr 6.02, 6.03, 6.04(b), (c), 6.05, 6.07(4), (5), 6.09(2), 6.10, 6.11, 6.14, with r 3.05(2).
- **Order 7:** rr 7.01, 7.02 (heads (a), (g), (j), (k), (n) asked one by one, the others as one fact), 7.03(1), 7.06; and
  r 8.04 (the time for appearance, needed for default judgment).
- **Order 13:** rr 13.07(3), 13.10(4), 13.12, 13.13 (in the admission question).
- **Order 14:** rr 14.01, 14.02 (a regulative rule), 14.04 (a regulative rule), 14.05, 14.07, 14.08.
- **Order 15:** rr 15.01, 15.02(1), (3), (4), 15.03(1), (5), (6), 15.04, 15.06, 15.08(1), (2) (a regulative rule), (3), (5).
- **Order 18A:** rr 18A.02, 18A.04, 18A.05, with Supreme Court Act 1986 ss 33E and 33J(1)-(3) restated.
- **Order 21:** rr 21.01, 21.02, 21.03(1), (1.2), (2), (3), 21.04, with r 15.04.
- **Order 22:** rr 22.04(4), 22.05(3), 22.15, 22.18(4), 22.19(3), 22.23.
- **Order 24:** rr 24.01, 24.02, 24.03, with r 48.04.
- **Order 25:** rr 25.02, 25.03, 25.04, 25.05, 25.06, 25.07, 25.08.
- **Order 26:** rr 26.01, 26.02(3), (4), 26.03(3), (4), (5), 26.03.1, 26.05, 26.06, 26.07(1), 26.07.1, 26.07.2, 26.08,
  26.08.1, with r 63.16.
- **Order 29:** rr 29.01, 29.01.1, 29.02, 29.03 (a regulative rule), 29.04(1)(d) (in the description), 29.09(2), 29.12.1,
  29.15, with r 63.16.1.
- **Order 32:** rr 32.01, 32.02, 32.03, 32.04, 32.05, 32.06, 32.07.
- **Order 33:** rr 33.01, 33.04, 33.05, 33.06, 33.07, 33.08 (with 33.07 a regulative rule), 33.08.1, 33.09, 33.10, 33.11,
  33.12.
- **Order 44:** rr 44.02, 44.03(1), (3), 44.04, 44.05, 44.06(5), (6).
- **Order 48:** rr 48.01, 48.04 (with r 24.01), 48.05, 48.07(4).
- **Order 51:** rr 51.01, 51.02, 51.05, with rr 21.03(3), 22.09.
- **Order 62:** rr 62.02, 62.04 (62.05 in the description).
- **Order 63:** rr 63.03(2), (3), 63.13, 63.14, 63.15, 63.17, 63.18, 63.20, 63.20.1, 63.22, 63.23(1), (3), (7), 63.28,
  63.30, 63.30.1, 63.31, 63.34; Appendix A Sections 1 and 4.
- **Order 79:** rr 79.02, 79.04(3), 79.06, 79.10, 79.16(1), (2).
- **Order 85:** rr 85.02, 85.03 (a regulative rule), 85.04, with the Legal Identity of Defendants (Organisational Child
  Abuse) Act 2018 ss 7(3) and 13 restated.

**Regulative rules:** six, in `scr-duties.l4`: serve the statement of claim (r 14.02), serve the defence (r 14.04), file
the summons for approval of a compromise (r 15.08(2)), make discovery (r 29.03), serve the hospital and medical reports
(rr 33.07, 33.08), file and serve the amended process naming the proper defendant (r 85.03). Each is `MUST ... WITHIN` the
days from the starting event to the last day Order 3 gives, `LEST BREACH ... BECAUSE` what the Rules say follows. Each is
run by `EVALTRACE` inside an exported question that takes only dates and yes/no facts and answers "taken in time", "not
taken in time" or "still open".

**Out, and why:**

- **Order 1:** rr 1.01, 1.02, 1.03(2) and Schedule 1 (title, authority, revocation: machinery; the revocation is recorded in
  Edition), 1.06, 1.12 (as a rule of its own), 1.13 (definitions, used where needed), 1.14-1.19 (the Court's powers,
  corporations, solicitors, addresses: no fact test for the party).
- **Order 3:** rr 3.03 (the Court may fix a time), 3.04(2) (who serves an order about the vacation), 3.07, 3.09 (sittings,
  hours).
- **Order 4:** rr 4.02, 4.03 (summons, names of parties), 4.07, 4.08 (the Court's powers), 4.09-4.10 (certification forms
  and the Rules' 2-year period for the Civil Procedure Act s 41(5): the Civil Procedure Act encoding asks the period as an
  input; it is 2 years, r 4.09.1(1), and could be wired in there).
- **Order 5:** rr 5.01-5.03, 5.05-5.07, 5.10, 5.11 (forms, indorsements, filing, petitions); r 5.09 (debt-only writs: not a
  claims-for-injury rule).
- **Order 6:** rr 6.01, 6.04(a), (d), (e) (corporations, the Crown), 6.06-6.06.3 (addresses for service), 6.07(1)-(3.1),
  (6) (how ordinary service is done, beyond its day), 6.08, 6.12, 6.13, 6.15-6.17 (proof, agents, land, the Court's
  notices, affidavits of service).
- **Order 7:** rr 7.02 heads (b)-(f), (h), (i), (l), (m), (o)-(s) one by one (asked as one fact), 7.03(2)-(5), 7.04, 7.05,
  7.07-7.09 and Part 2 (rr 7.09.1 onward: service in a foreign country, the Court's discretion, forms and procedure).
- **Order 13:** rr 13.01-13.06, 13.08-13.11, 13.14, 13.15: the form and content of pleadings, with no answer a party
  computes beyond "plead it".
- **Order 14:** rr 14.03, 14.06, 14.09, 14.10 (the Court's orders, filing).
- **Order 15:** rr 15.03(2)-(4) (the Court's appointment powers; (2) is in the r 6.04(c) question), 15.05 (orders under
  r 9.09, Order 9 not in focus), 15.07, 15.08(2.1), (4), (6), 15.09, 15.10 (discovery by the guardian, evidence and forms on
  approval, execution against money in court, counterclaims).
- **Order 18A:** r 18A.01 (application). The group proceeding law itself (who may sue, who is a group member, opting out,
  settlement approval) is in the Supreme Court Act 1986 and its encoding.
- **Order 21:** rr 21.05-21.07 (continuing against others, counterclaims, setting aside: in descriptions).
- **Order 22:** rr 22.01-22.03, 22.04(1)-(3), 22.05(1), (2), 22.06-22.14, 22.16-22.22, 22.24: the procedure and the
  Court's powers; whether summary judgment may be given is Civil Procedure Act Part 4.4, in that Act's encoding.
- **Order 24:** rr 24.04-24.06 (counterclaims, inherent power, setting aside).
- **Order 25:** r 25.01 (withdrawing an appearance with leave).
- **Order 26:** rr 26.02(1), (2), 26.03(1), (2), (6), (7), 26.04 (without prejudice), 26.10 (contributor parties: between
  defendants), 26.11 (transitional, spent), Part 3 (offers on appeal, rr 26.12: appeals not in focus).
- **Order 29:** rr 29.04(1)(a)-(c), (2) (the affidavit's form), 29.05-29.08, 29.11, 29.12, 29.13, 29.14 (the Court's orders
  and committal), 29.06, 29.09(1), (3)-(6), 29.10 (copies and inspection procedure), 29.16.
- **Order 32:** rr 32.08-32.11 (procedure, costs and security: in descriptions).
- **Order 33:** rr 33.02, 33.03 (counterclaims, definitions used in descriptions).
- **Order 44:** rr 44.01 (definitions), 44.03(4) (signing and attachments), 44.06(1)-(4) (the Court's directions).
- **Order 48:** rr 48.02, 48.03, 48.04.1, 48.06, 48.07(1)-(3), (5) (the Court's fixing and vacating of dates, forms, fees).
- **Order 51:** rr 51.03, 51.04, 51.06, 51.07 (procedure; a continuing cause of action is assessed to the time of
  assessment).
- **Order 62:** rr 62.01 (definitions), 62.03, 62.05 (the Court's directions).
- **Order 63:** rr 63.01, 63.01.1, 63.02, 63.04-63.12, 63.19, 63.21, 63.26, 63.27 (the Court's powers, who taxes, gross
  sums, other courts, injunctions, trustees); Part 3A (pro bono costs), Parts 4 to 9 (the Costs Court, taxation procedure,
  solicitor-and-client costs, allowances, alternative assessment, review and appeal: procedure for the Costs Court and the
  lawyers, not in the claims focus); Appendix A Sections 2, 3 and 5-9 (reasonableness factors, non-hourly work, witnesses,
  winding up, travel, copying, disbursements: no figure a party computes).
- **Order 79:** rr 79.01, 79.03, 79.04(1), (2), 79.05, 79.06(3)-(5), 79.07-79.09 (common funds, investment, interest
  allocation by the Senior Master), 79.11-79.15, 79.16(3)-(6) (who decides payment out, and appeal procedure).
- **Order 85:** r 85.01 (definitions); r 85.02(1) (Form 85A, in a description).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** r 3.04(1) "In calculating the time fixed by these Rules ... the period from 24 December to 9 January ... shall be
  excluded" -- `the last counted day of ... months after`, and through it `Until when can my writ be served`, `Must I give a
  month's notice before going on`, `What happens to my inactive case now`, the month in r 79.16(1) -- applied to periods in
  months and years as well as days (a year from 15 March 2026 ends 1 April 2027) -- applied only to periods counted in days.
- **F2** r 3.01(4), r 3.05(2), r 6.07(4) "a day on which the office of the Court is closed" -- `counts towards the period`,
  `the open day of service for` -- Saturdays and Sundays only; public holidays are not computed, and are asked only for a
  last day (r 3.01(5)) and for the second business day -- every public holiday excluded.
- **F3** r 26.01 business day -- `the second business day after` -- one public holiday in the two weekdays is asked as a
  yes/no and moves the day by one -- each holiday counted.
- **F4** month arithmetic -- `the date ... months after` -- the same day of the month, or the month's last day where it is
  shorter (29 February 2028 plus 12 months is 28 February 2029; 12 months before 29 February 2028 is 28 February 2027) --
  1 March.
- **F5** r 3.04 and business days -- `the second business day after` -- r 3.04 not applied (a business day is a day the
  office is open, which it is in the vacation on weekdays) -- vacation days excluded.
- **F6** r 3.06, r 25.08 "a year or more has elapsed" -- `Must I give a month's notice before going on`, `What happens to my
  inactive case now` -- elapsed once the last day of the year (counted by Order 3) has passed -- elapsed on that last day.
- **F7** r 6.02(1) with no way of service made out -- `Has the defendant been served with my writ` -- JUST FALSE -- NOTHING
  (the rules on deemed service are not a closed list).
- **F8** r 6.07(5) "or on such other day as may be proved" -- `On what day was the document served` -- the deemed day only
  -- a day proved otherwise (an input).
- **F9** s 33J(2) "before the date so fixed" -- `Is my opt-out notice good` -- a notice on the fixed date is late -- on or
  before.
- **F10** r 3.01(5) for a period counted back ("not less than 14 days before the day for hearing", rr 22.04(4), 22.05(3),
  33.10, 33.11(4)(a), 44.03(1)(b), 51.02(2)) -- the "by when" questions -- a last day on a Saturday or Sunday moves forward to
  the next open day, as the rule reads (a hearing on 13 January 2027 gives 14 December 2026) -- moved back to the last open
  day before it, keeping the full period.
- **F11** r 25.02(2) after the close of pleadings without consent -- `May I discontinue without leave` -- NOTHING (a grant
  limited by its own terms) -- JUST FALSE (leave is then the only way the rule gives).
- **F12** r 26.03(3) a stated time "not ... less than 14 days" -- `r 26.03(4) -- the last day to accept` -- a shorter stated
  time is read as 14 days -- the stated time, or no Order 26 offer at all (the form question answers JUST FALSE for it).
- **F13** r 26.03(4)(b) "before ... verdict or judgment" -- the same -- the last day is the day before the day of the verdict
  -- acceptance earlier on the day of the verdict.
- **F14** r 26.08(2), (3) "no less favourable" / "not more favourable ... than the terms of the offer" -- `What costs order
  follows the unaccepted offer` -- compared as money, the judgment less post-offer interest (r 26.08(5)), on the footing the
  user gives -- terms other than money weighed by the Court.
- **F15** r 44.02(3) -- `Does Order 44 apply to this expert evidence` -- outside medical negligence, a doctor's report under
  Order 33 is also within Order 44 -- Order 33 alone governs medical reports in every injury claim.
- **F16** Appendix A 1.1 "10 or more years", "between 5 and 9 years", "less than 5 years" -- `What is the most per hour for
  this work` -- completed years (9.5 years is in the 5 to 9 band) -- 9.5 years outside every band.
- **F17** r 79.06(2) "applying to the money for the period of the loss the last rate" -- `What is the most interest for the
  delay` -- simple interest over a 365-day year -- another day count.
- **F18** Legal Identity of Defendants Act s 7(3) "within 120 days after the commencement" -- `By when may the NGO nominate a
  proper defendant` -- plain days, the first excluded, without r 3.04 or r 3.01(5) (a time fixed by an Act, not by the
  Rules) -- with them.
- **F19** r 26.08(4) "after the offer was made" where (2) and (3) say "served" -- `From when do the offer's costs
  consequences run` -- one day, counted from service, serves all three -- (4) counted from the day the offer was made.
- **F20** r 33.11(4), (5) a doctor who must attend and does not -- `Can the medical report be received in evidence` --
  NOTHING ("the Court may order that the medical report be not received") -- JUST FALSE.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means" definitions (rr 1.04, 15.01, 26.01) give their answers both ways; "unless" and "unless the Court
otherwise orders" (rr 3.02(3), 15.02(4), 15.03(5), 25.06, 26.05, 33.09, 33.12, 44.04, 44.05, 48.05, 63.14, 63.15, 63.17,
63.18, 63.20, 63.20.1, 63.22, 63.31), "if, but only if" (r 5.04(3)), "shall not" and "does not" (rr 1.05(2), 6.05(1),
15.03(6), 15.04, 15.08(1), 21.01(3), 26.07.2(1), 33.12, 44.03(3)(b), 44.05, 44.06(5), (6), 48.07(4), 62.02(2), 63.13,
63.23(3), 79.02(2)), the "where" and "if" conditions of rr 3.06, 24.03, 25.07, 25.08, 26.07, 32.03, 32.05, 33.04(2),
62.04, 63.18, 79.10 and s 33E(2), and the periods the Rules fix (rr 5.12, 18A.04 with s 33J(2), 26.03(4)) give `JUST
FALSE`. `NOTHING` is answered where a rule does not reach the case (*limited by its own wording*: rr 1.05, 1.05(3),
3.02(3), 6.04, 13.07(3), 13.10(4), 15.02, 15.04, 15.08, 18A.05, 21.01, 22.15, 24.01, 24.02, 25.02, 26.07.1, 26.08.1,
29.15, 32.07, 33.01, 33.05, 33.06, 33.08.1, 33.10, 33.11, 44.03(3), 48.01, 48.05, 62.02, 62.04, 63.03(3), 63.23, 79.06,
s 13), and where the answer lies in an Act, an order or the Court's discretion (*points outside the text*: rr 4.01, 7.01,
8.04(c), 22.05(3), 26.03.1, 29.01.1(1), 33.07(2)(b), 44.03(1), 85.03, s 7(3), Appendix A before 2026, r 33.11(4), (5)).

## What the Rules turn out to say

1. **r 3.04 stretches every period across Christmas, years included.** Read as written, "the period from 24 December to 9
   January ... shall be excluded" in calculating any "time fixed by these Rules", so a writ filed on 15 March 2026 is valid
   for service until 1 April 2027, not 15 March 2027 (r 5.12(1)), and a "year" of inactivity (rr 3.06, 25.08) is 382 days.
   Whether r 3.04 reaches periods in months and years is for a lawyer (F1). Asserted.
2. **r 3.01(5) on a period counted back shortens it.** "Where the last day for doing any act is a day on which the office
   of the Court is closed, the act may be done on the next day the office is open" applies, as written, to "not less than
   14 days before the day for hearing" too: a hearing on Wednesday 13 January 2027 makes Sunday 13 December 2026 the last
   day, so service on Monday 14 December gives only 13 counted days (F10). Asserted.
3. **An injury plaintiff who beats its own offer gets indemnity costs for the whole claim.** r 26.08(2)(a) gives costs "in
   respect of the claim taxed on an indemnity basis" with no cut-off at the offer, unlike (2)(b) for other claims, which
   switches to indemnity only from 11 am on the second business day after service. Asserted.
4. **r 26.08(4) counts from the offer "made"; (2) and (3) from the offer "served".** The difference may be deliberate (a
   defendant's offer made but served later) or a slip; encoded as service for all three (F19).
5. **r 26.03(3) says a stated time "shall not be less than 14 days" but not what follows if it is.** Encoded both ways: the
   form question says such an offer is not in proper form, and the acceptance question gives the offeree 14 days (F12).
   Asserted.
6. **Appendix A's experience bands leave a gap.** "10 or more years", "between 5 and 9 years" and "less than 5 years" say
   nothing of a lawyer with 9 years and some months. Encoded in completed years (F16). Asserted (9.5 years: $663).
7. **r 63.08(1) points to a scale item that is not there.** Costs on a default judgment entered under r 21.03(2) are "fixed
   ... in accordance with the scale in Appendix A", but the Appendix A substituted by S.R. No. 127/2025 has only hourly and
   reasonable-amount items (and a short-form bill for winding up), no fixed sum for a default judgment. Not encoded; for a
   lawyer.
8. **r 79.02(1)(d) still names the Victims of Crime Assistance Act 1996 s 70A** beside (da) the Victims of Crime
   (Financial Assistance Scheme) Act 2022 s 70(2) (the Civil Procedure Act encoding's finding 8 records the 1996 Act's
   replacement). Not asserted: no question turns on the list.
9. **r 33.11's paragraph (3) has no number.** The deposited text (line 2723) prints "Subject to paragraphs (4) and (5), a
   medical report may be used in evidence --" between (2) and (4) with no "(3)". A conversion slip or the Word file's own;
   to be checked against the authorised PDF. Encoded as paragraph (3).
10. **r 7.02(d)(ii) opens a bracket it does not close** ("(including, without limitation, interim or ancillary relief ...
    Commercial Arbitration Act 2011;"). No effect on the encoding.
11. **r 1.13(2)(c)** prints without the indent of its neighbours; the text is otherwise as the Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF (findings 9 to 11).
- Victorian public holidays (Public Holidays Act 1993), so that r 3.01(4), (5), r 3.05(2), r 6.07(4) and business days
  are computed rather than asked; the penalty interest rate (Penalty Interest Rates Act 1983).
- The 2015 Rules, for proceedings pending on 8 September 2025 (r 1.05(3)) and offers served before 1 September 2013
  (r 26.11).
- The Orders left out above, especially Orders 9-12 (joinder, counterclaims, third parties), 23 (summary stay and strike
  out), 30, 31 (interrogatories, oral discovery), 35, 36 (admissions, amendment), 40-43 (evidence, subpoenas, affidavits),
  49 (trial), 58 and 64 (appeals), 59-61 (judgments and instalments), 66-75 (enforcement) and 77 (Associate Judges).
- A lawyer's view on findings 1 to 7 and forks F1, F10, F11, F12, F13, F14, an independent test pass and a human gate.
