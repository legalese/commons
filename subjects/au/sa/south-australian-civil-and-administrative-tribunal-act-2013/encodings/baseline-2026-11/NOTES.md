# South Australian Civil and Administrative Tribunal Act 2013 (SA) -- baseline encoding, the applicant

> **Edition.** The Act encoded is the register's version of 1 June 2025, and the South Australian Civil and
> Administrative Tribunal Regulations 2015 the register's version of 1 July 2020, both fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons they do **not** come from the Open Australian Legal Corpus (collected 10 March
> 2025), so that corpus's "may be out of date" warning does not apply to them; but the register's own note says
> references to other legislation and to bodies are not updated automatically, and the SACAT Rules, which fill in
> much of the procedure, are not deposited. Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults
ruled on 2026-10-18. One module of questions (`sacat-applicant.l4`), one small date module (`sacat-dates.l4`, built-in
date functions only, no daydate and no `YMD`), one case file (`sacat-cases-applicant.l4`). Answers are named outcomes
(enumerations), dates and numbers, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used: where the text says no in its
own words the outcome is a "no: ..." naming the provision; where the text is silent, or leaves the point to a relevant
Act or to the rules, the outcome says "not under s N", "this Act sets no bar" or "the relevant Act decides". That
follows the 2026-11-04 and 2026-11-05 rulings (ENCODING-GUIDE section 5) in substance. No REFUSE, no `#ASSERT REFUSED`,
no BECAUSE except in `LEST BREACH ... BECAUSE`. No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use as advice.

**Regulative rules (3).** The three duties with a deadline are `DEONTIC` rules run inside a question with `EVALTRACE`,
so no exported question takes a `DEONTIC` or an `EVENT`: s 35(2) with r 6 (the decision-maker MUST give the Tribunal
its reasons and documents WITHIN 21 days of notice, the 21 written once as `r 6 -- the days the decision-maker has` and
used by the deadline question, the rule and the not-yet-given branch); s 70(2) (I MUST apply for internal review WITHIN 1 month);
s 71(3) (I MUST institute the appeal WITHIN 1 month). Each `LEST BREACH ... BECAUSE` names the provision and who can
excuse the lateness.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** South Australian Civil and Administrative Tribunal Act 2013 (SA), version 1.6.2025, deposited at
  `../../registers/source-bundle/south-australian-civil-and-administrative-tribunal-act-2013.txt` (text sha256
  75447e49...6fd3e9 per its `.meta.json`).
- **Regulations (they set the Act's numbers and prescribed classes):** South Australian Civil and Administrative
  Tribunal Regulations 2015, version 1.7.2020, deposited at
  `../../../south-australian-civil-and-administrative-tribunal-regulations-2015/registers/source-bundle/` (text sha256
  09dcf966...a158448). Used: r 4 (interlocutory steps that are not "decisions"), r 5 (reviewable decisions), r 6 (21
  days), r 7 and r 11 (prescribed costs circumstances), r 9 (who may enforce), r 14(1)-(8) (fees, including (4), who pays a
referral fee). Not used: r 14(9) (the Registrar may require a deposit on account of fees: a Registrar's discretion),  r 8 (service), r 10
  (public access), rr 12, 13 (machinery).
- **Not deposited, so inputs:** the SACAT Rules (withdrawal without leave, s 47(2); time for an absence review, s 85(3);
  extensions, s 66); the Magistrates Court Act 1991's jurisdictional limit for contract claims (s 89(3)); the Supreme
  Court Rules (s 71(1a), (2b)); every relevant Act (s 4: it prevails over this Act); the Legislation Interpretation Act
  2021 (how periods are reckoned, fork F1). The fee amounts are in neither the Act nor the Regulations (r 14 says who
  pays; Schedule 1, which held the amounts, was deleted in 2017), so no amount is encoded.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `sacat-dates.l4` | 0 | 0 | 0 | 0 |
| `sacat-applicant.l4` | 0 | 0 | 0 | 0 |
| `sacat-cases-applicant.l4` | 0 | 0 | 221 | 221 |

Negative control: with the r 6 rule's `WITHIN 21` made `WITHIN 20` and s 47(4) dropped from the r 11 list, exactly the
3 predicted assertions failed (reasons given on the 21st day; the trace helper at day 21; a want-of-prosecution
dismissal under r 11); the module was restored and rechecked (202 of 202).

Fix of 2026-11-07, after an independent verification: r 14(4) (who pays a referral fee) and s 38I(1), (2) (purported
orders) added, the r 6 days written once, the header scope and the s 34(2)(b) input's description corrected; 19
assertions added (221 of 221). A second negative control, with the r 6 days made 20, failed exactly the 5 assertions
that turn on the 21st day (the deadline date, the rule at day 21, reasons given on day 21, not yet given on day 21, the
trace helper), showing all three uses read the one constant; it was restored and rechecked.

Edges asserted: the 21st and 22nd days after notice (r 6), given and not yet given; the last day of the month and the
day after for internal review and appeal, from 15 March, 31 January (in 2024 and 2025), 28 February, 31 October and 15
December; lodging with the Tribunal on the last day of a limitation period and a day after (s 38C(2)); a money order
equal to the Magistrates Court limit and one dollar over (s 89(3)); each limb of every "or" (s 34(2), r 5, r 7, r 11,
s 40(4)); and the order in which provisions displace one another (relevant Act before Tribunal order, s 37(3)(b);
transfer order before r 4 before s 70(1); s 56(4) before leave).

## Seat

**The applicant (required): the person who brings a claim or other matter before SACAT, or asks it to review a decision
made about them, and goes on to internal review, appeal or enforcement** (`sacat-applicant.l4`, 36 questions). Every
question is one that person would ask: "Is my matter in the review or the original jurisdiction?", "By when must the
decision-maker give its reasons?", "Does the review stop the decision?", "Can it be reviewed again?", "Does my
transferred claim count as made in time?", "Who can appear for me?", "Can what was said at mediation be used?", "Can I
withdraw?", "Can I start again?", "Who pays the costs?", "Can I have internal review, and by when?", "Where does my
appeal go, and by when?", "Can a decision made in my absence be reviewed?", "Where can I recover the money?", "What is
the largest fine?", "Must I pay the fee?". Most answers hold for any party; where a provision turns on whether the
person is the applicant (s 47, s 49(2)) the question says so.

No seat for the Tribunal, the President, a registrar, the decision-maker or the Supreme Court. A second party seat (the
respondent) would ask nearly the same questions with the same answers, so none is written.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulations (21 days, prescribed classes,
  fees) are in; the Rules and the Magistrates Court Act are not deposited, so their points are inputs.
- **The actors the text names.** Followed: applicant, party, decision-maker, Tribunal, President, Presidential member,
  legally qualified member, registrar, Registrar, Magistrates Court, Supreme Court, Court of Appeal, District Court.
- **Judgments answered conditionally.** Followed: "satisfied that it is just and reasonable", "believes", "reasonable
  excuse", "good reason", "considers appropriate", "frivolously or vexatiously" are inputs worded as findings.
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 34(2) "reviewable decision" with r 5 worked
  out; s 3(1) "decision" with r 4 worked out; s 89(3) "appropriate court"; s 85(1) "relevant hearing" (mediation
  excluded); s 91(1) "costs of proceedings". Borrowed: "relevant Act" content, "counsel", tenancy and park dispute
  terms (r 5(3) borrows them from their Acts), "limitation period".
- **One case:** one proceeding before the Tribunal, and the internal review or appeal from its decision.
- **The Act's terms with plain glosses:** in the `@desc`s and answers.
- **Machinery out:** see Scope.

## Scope

**In:** s 3(1) (applicant, decision, monetary order, as used), s 4 (as "the relevant Act decides"), s 29, ss 32-34 with
r 5, s 35(1), (2), (4)-(6) with r 6, s 36, s 37, s 38, s 38B(2), (5)-(7), s 38C(1), (2), s 40(4), s 41(3), ss 46-49,
s 38I(1), (2), s 50(10), (13), s 51(11), (12), s 56(1), (2), (4), s 57 with r 7, s 58(1), s 60(1), (2)(e), (3), s 62(4), s 66, s 70 with
r 4, s 71(1), (2), (2a), (2b), (3), s 73, s 84, s 85, s 89(1)-(3) with r 9, s 91 with r 11, s 93A, s 93B, r 14(1)-(8).

**Out, and why:**

- Part 2 except s 29 (establishment, objectives, members, appointment, constitution, presiding, streams, validity,
  delegation: ss 5-28, 30), Part 6 (staff: ss 74-78), ss 92-96 (reports, rules, regulations, review): machinery. s 8
  (objectives) and s 39 (no rules of evidence, equity and good conscience) bind the Tribunal and give the person no
  answer of their own.
- ss 38D-38H, s 38I(3)-(5) (how a transferred proceeding runs in the Magistrates Court): s 38D repeats the Tribunal's
  representation and costs limits for the Court, and ss 38E-38H give the Court its conference, bailiff and priority
  rules. s 38I(3) says an application to vary or revoke a purported order must be transferred to the Magistrates
  Court, a step the Tribunal must take that leaves the person nothing to decide; s 38I(4) is an immunity (see ss
  79-81). s 38I(1) and (2) are in: a purported order is one the Tribunal purportedly made, "whether before or after the
  commencement of this Part", that is invalid because the application involved federal jurisdiction (s 38I(5)); the
  person in whose favour a purported monetary order was made can recover it as a debt in the s 89 court (asked in
  `Where can I recover the money`), and not complying with any other purported order is an offence ($50 000 or 2
  years, in the offence questions).
- ss 40(1)-(3), (5), 41(1), (2), 42-45, 50 (other than (10), (13)), 51 (other than (11), (12)), 52-55, 58(2)-(4), 59,
  61, 63-65, 67-69, 72, 82, 83, 86-88, 89A, 90: the Tribunal's powers and procedure. They say what the Tribunal may do,
  at its discretion, and give the person nothing a question could decide from facts. Candidates for a later layer:
  s 53 (who is a party), s 54 (joinder), s 61 (preservation orders), s 69 (privilege), s 90 (public access, r 10).
- ss 79-81 (immunities): a party has a Supreme Court party's immunity (s 79(4)); no question turns on it.
- r 8 (service), r 10 (public access), rr 12, 13 (reports and register), r 14(9) (a deposit the Registrar may require).

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** ss 70(2), 71(3), r 6, `the last day of one month after`, `the date ... days after`: the day of the decision (or
  of notice) is excluded, and one month ends on the corresponding day of the next month, or the last day of that month
  if it has none (31 January -> 28 or 29 February; 28 February -> 28 March). The Legislation Interpretation Act 2021
  (SA) is not deposited; the other readings are a month that starts the day after and ends on the day before the
  corresponding day, and a last day on a weekend or public holiday moving to the next business day. Neither is applied.
- **F2** s 38C(2), `Does my transferred claim count as made in time`: lodging on the last day of the limitation period
  is "before the expiry of the period"; the other reading needs the day before.
- **F3** ss 46, 47, 62(4), `Can I start the proceeding again`: "this Act sets no bar", not "yes", because only ss 48(4)
  and 49(4) speak; the relevant Act, the limitation period and res judicata may still bar it.
- **F4** s 70(1a), `Can I apply for internal review`: a registrar's decision in the original jurisdiction is both
  (1)(a) and (1)(b); the answer names both kinds of leave rather than choosing one; the other reading takes (1)(b)'s
  Presidential leave as the more specific.
- **F5** s 70(1), `Can I apply for internal review`: a decision of Tribunal members in the review jurisdiction gets
  "not under s 70", not "no", because s 70(1) lists the reviewable decisions without "only"; s 71(2a) treats them as
  going straight to appeal, which supports the answer.
- **F6** s 56(4), `Who can appear for me`: a barred person cannot act even with leave or as counsel; the barred flag is
  ignored when the person appears for themself (s 56(4) is about acting "as a representative").
- **F7** s 29(b)(ii), `Can a member with a conflict hear my case`: "if a party ... does not consent" is any party, the
  applicant included; consent must be given by every party.
- **F8** r 14(5)(d), `Is my case on hold until I pay`: the listed review fees (Local Government, Valuation of Land,
  Lobbyists Acts) are folded into the application fee choice.
- **F9** s 85(5), `Can the decision made in my absence be reviewed`: when the Tribunal is not satisfied of a reasonable
  excuse the answer is that s 85(5) "does not require" a review, not that the Tribunal cannot review; the text is
  silent on that case.
- **F10** s 57(3), `Who pays the legal costs`: the "should" order is reported as falling on "the party the dismissal is
  directed against" (finding 1); the other reading is the party whose conduct led to the dismissal, which differs
  when s 49(2)(b) decides the proceedings for the applicant.

## What the Act turns out to say (findings)

1. **s 57(3)'s "the party against whom the action is directed" is unclear.** In a dismissal for want of prosecution
   (s 47(4)) or as frivolous (s 48(2)) the "action" is presumably the dismissal, aimed at the party whose proceeding
   falls (usually the applicant); but under s 49(2)(b) the Tribunal may decide *for* the applicant and the "action" is
   then directed at the other party. Encoded as "the party the dismissal is directed against" (F10). Not asserted
   beyond the answer's words.
2. **r 7 and r 11 differ on withdrawal.** r 11 lets the Tribunal order the costs of the proceedings against a party in
   the review jurisdiction after a s 47(3) dismissal on withdrawal; r 7 does not make withdrawal a circumstance in which
   party-and-party costs "should" follow. Asserted (both questions, s 47(3)).
3. **The fee amounts are not in the deposited instruments.** r 14 says who pays, who is exempt and when proceedings are
   stayed, but the Schedule of fees was deleted in December 2017; the amounts are fixed elsewhere (not deposited). No
   amount is encoded.
4. **s 70(1a) overlaps (F4).** A registrar or staff decision in the original jurisdiction falls in both s 70(1)(a) and
   (b), which call for leave from different members. Asserted.
5. **s 35(2) has two limits.** The decision-maker must act "within a reasonable period and in any event within" 21 days
   (r 6). Only the outer limit can be computed; an earlier "reasonable period" is the Tribunal's call. The question says
   so.
6. **s 71(1a) and (2b) let other instruments re-route appeals.** The Supreme Court Rules may send a Court of Appeal
   matter to a single judge "and vice versa", and may displace the internal-review-first rule; neither is deposited, so
   the appeal answer is s 71(1)'s default and displacement is asked as one fact.
7. **Numbering gaps.** s 2 (commencement), s 56(3) and s 90(2)(c) have been deleted; the gaps are what deletion left.
8. **Stale references in r 5.** r 5(1)(c) still names the Retirement Villages Act 1987 beside the 2016 Act that, to the
   encoder's knowledge (not from a deposited source), replaced it; both are encoded as written.
9. **s 36(2) lets the decision-maker stay its own decision**, not only the Tribunal; the stay question counts either.
10. **No person or body is prescribed under s 34(2)(b).** The Act lets the regulations prescribe persons or bodies
    whose decisions are reviewable, but r 5(2) prescribes classes of decision only. The choice `a person or body
    prescribed by the regulations` is kept for a later regulation or a relevant Act, and its `@desc` says that on the
    deposited Regulations it does not arise.
11. **r 14(4) moves the referral fee off the tenant or resident.** A fee for referring a matter under the Residential
    Parks Act 2007 s 29 or the Residential Tenancies Act 1995 s 63 or s 105M is paid by the park owner, landlord or
    rooming house proprietor, or, under s 29(6a), s 63(7) or s 105M(8) where no notice of dispute was lodged, by the
    third party those subsections name. Asserted, with the r 14(1) exemption (the Housing Trust as landlord) still
    applying.

## Before relying on it

Deposit the SACAT Rules, the Legislation Interpretation Act 2021 and the Magistrates Court Act 1991 and replace the
corresponding inputs; check the register for a version of the Act later than 1 June 2025 and of the Regulations later
than 1 July 2020; have a lawyer review the forks and findings 1, 2 and 4; run an independent test pass.
