# Civil and Administrative Tribunal Act 2013 (NSW) -- baseline encoding, the party to a claim in NCAT

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 1 July 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer; case-by-case sites listed in the fork
register). Five regulative rules (making an application or appeal in time, s 40; requesting reasons, s 62(2); the
Tribunal providing them, s 62(2); renewing Consumer and Commercial proceedings, Sch 4 cl 8(2); instituting an appeal to a
court, s 84(2) and Sch 6 cl 14(2)), each run by `EVALTRACE` inside an exported question that takes only plain facts. No
REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Act is NCAT's constitution, so most of it is
machinery; the focus is the provisions a party bringing or answering a claim meets, and those are encoded across Parts
3, 3A, 4, 5 and 6 and the Division Schedules' practice and appeal clauses (see Scope).

## Edition

- **Act:** Civil and Administrative Tribunal Act 2013 No 2, corpus document `nsw_legislation:2024-07-01/act-2013-002`
  (in force 1 July 2024), deposited at `../../registers/source-bundle/act-2013-002.txt` (text sha256 523074c7...c81ff
  as recorded in its `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because
  legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Not deposited:** the Civil and Administrative Tribunal Rules 2014 and the Civil and Administrative Tribunal
  Regulation (the "procedural rules", which set the time for applications and internal appeals and may qualify Part 4);
  the Uniform Civil Procedure Rules 2005 (time for appeals to courts); the Administrative Decisions Review Act 1997
  (administrative review, stays and when review decisions take effect); the Interpretation Act 1987 (counting time); the
  Crimes (Sentencing Procedure) Act 1999 (the value of a penalty unit). Each is asked as a fact or left as `NOTHING`, as
  noted at the question.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ncat-claims.l4` | 0 | 0 | 0 | 0 |
| `ncat-claims-cases.l4` | 0 | 0 | 256 | 256 |

Every expected value was worked by hand from the text, with the edges: lodging on the last day, the day after, the day
before, across a year end and on 29 February 2028 (ss 40, 41); lodging with the Tribunal on the last day of the
limitation period and the day after (s 34C(2)); a request for reasons on the 28th and 29th day, from a notice in a leap
February and across a year end (s 62(2)); reasons provided on the 28th day after the request and the 29th, and not yet
provided on either side of the last day; renewal on the 12-month anniversary, the day after, on the last day of the
compliance period and the day after, and from 29 February 2028 (Sch 4 cl 8); proceedings for a contravention 12 and 24
months on, including from 29 February 2028 (ss 76(2), 77(5)); a Guardianship appeal on the 28th and 29th day after the
decision or the reasons, and in further time (Sch 6 cl 14(2)); every s 62(2A) exclusion with and without the costs
argument; every special kind of decision under the Division Schedules for internal and court appeals; each
representation route with each kind of representative; each s 50 exception, including an order made without first
hearing the parties.

## Seat

**The party to proceedings in NCAT**: usually the applicant bringing a claim (a tenant, a consumer, a home owner, a
retail lessee, a discrimination complainant, a person seeking review of a government decision such as a victims support
decision), and on appeal the appellant; a respondent answering a claim asks the same questions of the same rules.
Questions that differ by role (dismissal, disadvantage under Sch 4 cl 10) take the role as an input. The victim in an
offender's restitution review (Sch 3 cl 13B) is a witness, not a party, and is asked as such. Every exported question is
one that person would ask ("Is my application in time?", "Can I have a lawyer?", "Must there be a hearing?", "Will I have
to pay costs?", "By when must I ask for reasons?", "Can I appeal, and do I need leave?", "How do I enforce my order?",
"What is the most I can be fined for breaching an order?"). The Tribunal, registrars, the President, the authorised
official and the courts get no seat: what they must or may do is encoded as what it means for the party (for example
the Tribunal's duty to provide reasons within 28 days, s 62(2), as "By what day must NCAT give me reasons?").

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, but the instruments are not deposited: the
  procedural rules set the times for applications and internal appeals, the court rules set the times for most appeals
  to courts, so those last days are inputs. The Act's own numbers (28 days, 12 months, 2 years, $11,000, $22,000, 50 and
  100 penalty units, 12 months' imprisonment) are encoded.
- **The actors the text names.** Followed: party, applicant, appellant, the Tribunal, Appeal Panel, registrar,
  authorised court, Supreme Court, District Court, Land and Environment Court.
- **Judgments answered conditionally.** Followed: "special circumstances" (s 60), "reasonable explanation" (s 55(2)),
  "considers ... frivolous" and "want of prosecution" (s 55(1)), "of the opinion ... unreasonably disadvantages" (Sch 4
  cl 10), "satisfied ... power" (s 59), "satisfied ... substantial miscarriage of justice" (Sch 4 cl 12(1)), "lawful" and
  "reasonable excuse" (s 72), whether federal jurisdiction is involved (s 34B), the extension of time (s 41) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** The four kinds of jurisdiction (ss 29-31), "interlocutory
  decision" (s 4, glossed in the `@desc`), "appealable decision" (s 82), "designated order" (s 72(2)), "court" (Sch 4
  cl 5(1), (2), asked with its exclusions glossed). "Administratively reviewable decision", "federal jurisdiction",
  "jurisdictional limit", "lands legislation" and the Division a matter belongs to are asked.
- **One case.** One party, in one set of proceedings (or one appeal).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 28-31 (kinds of jurisdiction); ss 34B, 34C(1)(a), (2) (federal matters taken to the District or Local Court);
ss 40, 41 (time for applications, extensions); s 43 (effect of pending applications and appeals); s 45(1)-(3) with Sch 3
cl 9(1), Sch 4 cl 7, Sch 5 cl 27, Sch 6 cl 9 (representation); s 50 with Sch 6 cl 6 (hearings), and s 53(3), (4) as it
bears on s 50(3); s 55 (dismissal and reinstatement); s 59 (settlement); s 60 with Sch 3 cl 12(1), 13 (costs); s 61
(when decisions take effect); s 62(2), (2A) with Sch 6 cl 11 (reasons); s 71 (false statements); s 72 with ss 76(2),
77(3), (5) (contravening orders, maxima and time for proceedings); s 78 (enforcing money orders); s 32, s 80 with Sch 3
cl 15, 16, Sch 4 cl 12, Sch 5 cl 29(1), Sch 6 cl 12 (internal appeals and leave); ss 82, 83, 84(2) with Sch 3 cl 17, 18,
Sch 5 cl 29(2), (4), (6), (9), Sch 6 cl 12, 14 (appeals to courts, their effect and time); Sch 3 cl 13B (the victim not
compellable); Sch 4 cl 5 (the Tribunal and the courts), cl 8 (renewal), cl 10 (proceedings causing disadvantage).

**Out, and why:**
- Part 1 (other than the definitions used), Part 2 (establishment, members, Divisions, rules, constitution), Part 7
  (miscellaneous), Schedules 1 (savings and transitional, including cl 9-10 on unexercised rights before 2014), 2
  (members) and 7 (examples of rule-making powers): machinery.
- The Division allocation lists (Sch 3 cl 3, Sch 4 cl 3, Sch 5 cl 4, Sch 6 cl 3) and the special constitution clauses:
  the Division is asked instead; the lists run to dozens of Acts and the regulations may amend them (s 17(4)).
- s 33 and ss 73-75, 77(1), (2), (4), (6), (7): enforcement and contempt are begun by the Tribunal or an authorised
  official, never by the party; the party's exposure is encoded through ss 71, 72, 76(2), 77(3), (5).
- s 34 (the Supreme Court's discretion to refuse judicial review), s 34B(3)-(8), s 34C(1)(b), (3)-(7), s 34D: the
  court's powers and the form of the leave application.
- ss 35-39, 42, 44, 46-49, 51-52, 53(1), (2), 54, 56-58, 63: the Tribunal's procedure, powers and discretions, with no
  number or condition the party can be told in advance (s 36(3)'s duty to co-operate has no deadline, and bears on
  costs through s 60(3)(f)); s 47 witness allowances are set by regulations not deposited; s 63 corrections turn wholly
  on the member's satisfaction.
- ss 64-70 (information disclosure): orders in the Tribunal's discretion; contravening a s 64 order is encoded under
  s 72(1). s 65's publication offence binds everyone, not the party as such.
- s 79, s 81, s 83(3), (4), s 84(3), (4), Sch 5 cl 29(7), (8), Sch 6 cl 14(3), (4): what the Appeal Panel or court may
  order on an appeal (open powers).
- Sch 3 cl 9(2)-(4), 10, 11, 12(2)-(5), 13A, 14; Sch 4 cl 6, 9; Sch 5 cl 5-26, 28, 29(2)(a), (3), (5); Sch 6 cl 5, 6A,
  7, 8, 10, 13: rights of officials to appear, party substitution in discrimination complaints, fund costs, transfers by
  consent or direction, the Commissioner's assistance, the professions' disciplinary machinery, Aboriginal Land Rights
  vacancy orders and the Legal Profession Uniform Law Application Act s 89(2) exclusion, and guardianship procedure.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 29(1)(b), 30, 31 -- `Which kind of jurisdiction is my matter in` -- external appeal is taken before
  administrative review where legislation provides both -- administrative review first; the Act sets no order between
  them.
- **F2** ss 62(2), 76(2), 77(5), Sch 4 cl 8(2), Sch 6 cl 14(2) -- every date question -- periods are counted from the
  day after the event (Interpretation Act 1987 s 36(1), not deposited); a period of months ends on the same day of the
  month, or that month's last day where shorter -- the day of the event counts; or a month period from 29 February ends
  on 1 March.
- **F3** the same provisions -- the last day is not moved when it falls on a weekend or public holiday -- it moves to the
  next business day under the Interpretation Act 1987 s 36(2).
- **F4** s 34C(2) "before the expiry of the period" -- `How my court proceedings are taken to have started` -- lodging
  on the last day of the limitation period is before its expiry -- the period expires at the start of its last day.
- **F5** Sch 4 cl 7(b) "an Australian lawyer or other agent" -- `Can I be represented` -- any representative of a party
  to a Retail Leases Act matter, practitioner or not -- "agent" limited to a commercial or leasing agent.
- **F6** s 50(3) "may not make an order dispensing with a hearing unless ..." -- `Must there be a hearing` -- an order
  made without first hearing the parties is an irregularity under s 53(3), which stands unless set aside (s 53(4)) --
  the order is beyond power and void, so a hearing is required.
- **F7** Sch 4 cl 8(1), (2) -- `Can I renew my proceedings` -- renewal under (2) needs the leave in (1) -- (2) stands on
  its own, and any person in whose favour an order was made may renew.
- **F8** ss 71, 72(1), 72(3) "knowing", "without lawful excuse", "without reasonable excuse" -- the penalty questions --
  with the excuse (or without knowledge) the maximum is 0 -- `NOTHING`, leaving the excuse to the court; and a
  designated order is outside s 72(3)'s "any other order" (`NOTHING` for the civil penalty) -- a designated order is
  also an "order" under s 72(3).
- **F9** Sch 4 cl 5(3), (7) -- `Can a court decide my Tribunal issue`, `Can the Tribunal decide an issue already in
  court` -- the tests are read issue by issue, and the Tribunal is taken to be aware of the court proceedings -- (3) reads
  "no issue" over the whole application, so one pending issue lifts the bar for all; or until the Tribunal is aware its
  jurisdiction continues.
- **F10** Sch 6 cl 6(1) with s 50(1)(b) -- `Must there be a hearing` -- in Guardianship proceedings involving a
  substantive function a hearing is required even where a resolution process is used -- the resolution-process
  exception still applies to that step.
- **F11** s 62(2A)(c) "except where a party has argued" -- `Can I ask for reasons` -- any party's argument for special
  circumstances restores the right -- only the requesting party's.
- **F12** s 80(2)(b) "any other kind of decision" -- `Can I appeal to the Appeal Panel` -- costs and consent decisions
  are appealable as of right on a question of law -- costs decisions as ancillary but consent decisions not appealable.
- **F13** Sch 6 cl 14(5) "Subject to any interlocutory order" -- `Does my challenge stop the decision` -- an order
  letting the decision operate ends the automatic stay -- the order can only add conditions to the stay.

## What the Act turns out to say

1. **Almost every time limit a party meets is outside the Act.** s 40 hands the time for applications and appeals to the
   enabling legislation and the procedural rules, s 84(2) the time for most court appeals to the rules of court; only
   s 62(2) (28 days for reasons), Sch 4 cl 8(2) (12 months to renew), Sch 6 cl 14(2) (28 days for Guardianship appeals)
   and ss 76(2), 77(5) are in the Act. s 41 lets the Tribunal extend any time "despite anything to the contrary" in the
   enabling legislation, even after it has expired. Asserted.
2. **s 60 is "subject to enabling legislation and the procedural rules" (s 35).** The no-costs rule and its special
   circumstances exception may be displaced by the NCAT Rules for some classes of claim; whether they are cannot be told
   from the deposited text. The answer here is s 60 with Sch 3 cl 12, 13 only.
3. **A victims support recognition payment review is final in NCAT under this Act.** Sch 3 cl 15(g) removes the internal
   appeal, s 82(1) gives no court appeal from a first-instance decision, and cl 13(c) bars costs either way; the Victims
   Rights and Support Act 2013 ss 49-53 add no appeal. Only judicial review would remain. Asserted (no internal appeal,
   no court appeal, no costs).
4. **The Guardianship Division appeal to the Supreme Court stays the decision automatically** (Sch 6 cl 14(5)); every
   other route says the decision keeps operating unless an order is made (s 43(2), s 83(5), Sch 3 cl 17(3), 18(2), Sch 5
   cl 29(9)). Asserted.
5. **Sch 4 cl 8 does not say whether renewal needs the leave in subclause (1)** (fork F7), and the 12 months run from
   "the end of the period", which the Tribunal sets. Asserted on the anniversary and the day after.
6. **s 50(3) does not say what follows an order made without first hearing the parties.** s 53(3) treats a failure to
   comply with the Act as an irregularity that does not nullify the step unless the Tribunal determines otherwise (fork
   F6). Asserted.
7. **The penalties for contravening orders are split.** A designated order (s 64 non-disclosure orders and some
   Anti-Discrimination Act and Guardianship Act orders) is an offence (50 penalty units or 12 months, 100 penalty units
   for a corporation, 12 months to prosecute); any other order is a civil penalty provision (at most $11,000, or $22,000
   for a corporation, 2 years to bring proceedings), brought only by an authorised official (s 75). s 71 gives no
   separate corporate maximum for false statements. Asserted.
8. **s 34C(2) saves a federal matter from the limitation period** if it was first lodged with the Tribunal before the
   period expired, so a party who started in NCAT does not lose time by going to the District or Local Court. Asserted,
   including lodging on the last day (fork F4).
9. **Sch 4 cl 12(2)(b)** confines a tenant whose termination order has been executed by a warrant of possession to an
   appeal on a question of law: no leave can be given on other grounds. Asserted.
10. **s 62(2) and Sch 6 cl 14(2) word their 28 days differently** ("within 28 days of being given notice"; "within the
    period ending 28 days after"); under the Interpretation Act both end on the 28th day after (fork F2).

## Questions (exported)

`ncat-claims.l4` (35), in the Act's order: `Which kind of jurisdiction is my matter in` (ss 28-31); `Can I take my
matter to a court instead` (s 34B); `How my court proceedings are taken to have started` (s 34C); `Is my application in
time` (ss 40, 41, rule); `Does my challenge stop the decision` (s 43 and the court appeals); `Can I be represented`
(s 45 and the Schedules); `Must there be a hearing` (s 50, Sch 6 cl 6); `Can my application be dismissed` (s 55(1), Sch 4
cl 10); `Can my dismissed proceedings be reinstated` (s 55(2)); `What can be done about a party causing disadvantage`
(Sch 4 cl 10); `Can our settlement be made into orders` (s 59); `Who pays the costs` (s 60, Sch 3 cl 12, 13); `When does
the decision take effect` (s 61); `Can I ask for reasons` (s 62(2), (2A)); `Will I get guardianship reasons without
asking` (Sch 6 cl 11); `The last day to ask for reasons`; `Is my request for reasons in time` (rule); `The last day for
the Tribunal to give me reasons`; `Were my reasons given in time` (rule) (all s 62(2)); `How do I enforce my money
order` (s 78); `The last day to renew`; `Can I renew my proceedings` (rule) (Sch 4 cl 8); `The largest fine for
contravening a designated order`; `The longest imprisonment for contravening a designated order` (s 72(1)); `The
largest civil penalty for contravening an order` (ss 72(3), 77(3)); `The last day for proceedings about a contravention`
(ss 76(2), 77(5)); `Can I appeal to the Appeal Panel` (ss 32, 80 and the Schedules); `Can the Appeal Panel give me leave`
(Sch 4 cl 12(1)); `Can I appeal to a court` (ss 82, 83 and the Schedules); `The last day for my guardianship appeal`
(Sch 6 cl 14(2)); `Is my court appeal in time` (s 84(2), Sch 6 cl 14(2), rule); `Can a court decide my Tribunal issue`
(Sch 4 cl 5(3)-(6)); `Can the Tribunal decide an issue already in court` (Sch 4 cl 5(7), (8)); `The largest fine for a
false statement to the Tribunal` (s 71); `Can I be compelled to give evidence in the restitution review` (Sch 3
cl 13B).

Situations: the Part 3A group arises only where the matter involves federal jurisdiction; the s 55(2) question only once
proceedings are dismissed for non-appearance; the s 62 group once a decision is given; the Part 5 group once an order
is made (s 78, Sch 4 cl 8) or contravened (ss 72, 76, 77); the Part 6 group once there is a decision to appeal; Sch 4
cl 5, 8, 10 and 12(1) only in the Consumer and Commercial Division; Sch 3 cl 13B only for the victim in an offender's
restitution review.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation and
  whether the Act has been amended since 1 July 2024.
- Deposit the Civil and Administrative Tribunal Rules 2014 and Regulation, and replace the time and costs inputs where
  they settle them (finding 2); deposit the Interpretation Act 1987 and settle forks F2 and F3.
- Have a lawyer review the forks, especially F6 (hearings), F7 (renewal) and F9 (courts and the Tribunal).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
