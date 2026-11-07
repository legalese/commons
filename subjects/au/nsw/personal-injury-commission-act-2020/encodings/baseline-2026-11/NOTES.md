# Personal Injury Commission Act 2020 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 27 September 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (a direction to produce
documents or provide information, s 49; the Independent Review Officer's 30 days, Sch 5 cl 8(4)), each run by
`EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The Act sets up the Commission that decides
workers compensation, motor accident and police officer support scheme disputes. Most of it is machinery; the claims
themselves, their thresholds and most of their time limits are in the enabling legislation (the Workers Compensation
Act 1987, the Workplace Injury Management and Workers Compensation Act 1998, the Motor Accident Injuries Act 2017, the
Motor Accidents Compensation Act 1999, the Police Act 1990 Part 9B) and the Commission rules. What a claimant meets in
this Act is encoded: representation, directions and summonses, the conduct and dismissal of proceedings, finality,
reconsideration and corrections, publication, enforcement, the District Court route for federal jurisdiction, the
evidential bars on Commission statements, the Commission officers' protections, and complaints to the Independent Review
Officer.

## Edition

- **Act:** Personal Injury Commission Act 2020 No 18, corpus document `nsw_legislation:2024-09-27/act-2020-018` (in force
  27 September 2024), deposited at `../../registers/source-bundle/act-2020-018.txt` (sha256 9a1e67a4...deee2ea7 as
  committed), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Personal Injury Commission Rules and Regulation, the enabling Acts, the ILARS guidelines, the
  Crimes (Sentencing Procedure) Act 1999 s 17 (the value of a penalty unit), the Interpretation Act 1987 (counting
  periods). What they decide is asked as a fact, or the answer is given in the Act's own unit (penalty units).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pic-dates.l4` | 0 | 0 | 0 | 0 |
| `pic-commission.l4` | 0 | 0 | 0 | 0 |
| `pic-cases.l4` | 0 | 0 | 173 | 173 |

Every expected value was worked by hand from the text, with the edges: compliance with a direction on the last day it
allows, the day after, on the day it was given, and across a year end, with and without reasonable excuse, and while the
time is still running; the Independent Review Officer's 30 days across a short February (31 January to 2 March 2026)
and a year end, a longer period notified on the 30th day and on the 31st, a "longer" period that ends sooner, a report
on the last day and the day after; lodging on the last day of a limitation period and the day after (s 27(2)); each
representative in s 48(8) and one outside it, in each Division; each ground of s 48(4), none, and leave revoked; each
requirement whose breach is an offence, with reasonable excuse, self-incrimination and a non-party summons in the Motor
Accidents Division; each excepted court proceeding in Sch 3 cl 7 and Sch 4 cl 7; each kind of claim in s 25 and Sch 5
cl 1, and one outside.

## Seat

**The claimant**: the injured worker, the person injured in a motor accident, or the police officer under the police
officer support scheme, who is a party to proceedings before the Commission, or complains to the Independent Review
Officer about an insurer. Every exported question is one that person would ask ("Am I entitled to be represented by
this person?", "May the insurer have a lawyer when I have none?", "Did I comply with the direction in time?", "Do I
commit an offence?", "Can what was said at the Commission be used in court?", "Can my proceedings be dismissed?", "Is
the decision final?", "Can the error be corrected?", "Does the certificate operate as a judgment?", "Can the District
Court give me leave?", "Can I complain about my insurer, and by when must it be dealt with?"). The insurer and the
employer meet many of the same rules as parties; a seat for them could be added. Officials (the Commission, the
President, registrars, medical assessors, merit reviewers, mediators, the Independent Review Officer, the District Court)
get no seat: their powers are encoded as what they mean for the claimant.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act's numbers are its own (50 penalty
  units, 30 days). The Commission rules and the regulations, which set the time for applications and appeals (s 45), are
  not deposited.
- **The actors the text names.** Followed: the claimant, the insurer, the parties, the Commission, the President, the
  principal registrar, medical assessors, merit reviewers, mediators, the District Court, the Supreme Court, the
  Independent Review Officer, the Crown.
- **Judgments answered conditionally.** Followed: the Commission's satisfaction (ss 48(2), (4), 52(3), 54), the
  President's (s 57(2)), the District Court's (s 26(3)), reasonable excuse (ss 49, 51, Sch 3 cl 8), good faith (s 64(3)),
  and the Independent Review Officer's view (Sch 5 cl 8(5)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "agent" (s 48(8)), "compensation claim" (s 25),
  "decision-maker" (s 32), "relevant Commission officer" (s 5), "assessment conference" (Sch 4 cl 7(3)), "claimant" and
  "insurer" (Sch 5 cl 1) are worked out; "licensed insurer", "federal jurisdiction" in a case, "jurisdictional error",
  standing under the regulations, and a court's monetary limit are asked.
- **One case.** One claimant's proceedings, or one complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 25 and s 26(1)-(4) (leave for the District Court to decide a compensation matter involving federal
jurisdiction, and what to file); s 27(1), (2) (when the substituted proceedings start; limitation periods); s 31(5)
(proceedings outside the State); ss 32, 38, 40 (assessors, reviewers and mediators competent but not compellable);
s 42(3) (the duty to co-operate, as a comment: no consequence attaches); s 48 (representation, the insurer's lawyer,
interpreters, written submissions); s 49(1), (3), (4) (directions; the regulative rule; the offence; the bar on
admitting what was withheld); s 51(2), (3) (summonses); s 52(3) (no hearing); s 53 (replacing a member); s 54
(dismissal); s 56 (finality; courts; judicial review for jurisdictional error); s 57 (reconsideration; obvious errors
and their examples); s 58(1) (publication); s 59 (recovery as a judgment); s 60 (in a comment); s 64(3), (4) (officers'
protection; the Crown's liability); Sch 3 cll 6, 7, 8 and Sch 3A cll 5, 6 (conciliation first; statements not
admissible in court on a work injury damages claim; evidence on oath; self-incrimination); Sch 4 cl 7 (assessment
conference statements); Sch 5 cll 1, 7(3), 8(1), (2), (4), (5), 9(2) (complaints to the Independent Review Officer,
with the regulative rule; ILARS's purpose).

**Out, and why:**
- ss 1-4, Part 2 (establishment, membership, Divisions, the President, delegations, the Rule Committee and rules,
  registrars), s 24, s 31(1)-(4), (6), Part 4 appointments (ss 33-37, 39), ss 61-63, 65-68, Sch 2 (members' terms), Sch 3
  cll 1-5 and 9, Sch 3A cll 1-4, Sch 4 cll 1-6, Sch 5 Part 2, cll 6, 7(1), (2), (4), (5), 10-14: machinery.
- s 26(5)-(7), s 27(3)-(6), ss 28-30: what the District Court may do in substituted proceedings, and the regulations that
  shape them: the court's powers, not asked by the claimant; the regulations are not deposited.
- ss 41-47: the guiding principle and informal procedure (no fact for the claimant to state changes an answer), s 45
  (applications and appeals in the time and manner the enabling legislation or rules prescribe: not deposited), s 46,
  s 47 (the Authority's right to be heard).
- s 50: the Commission's power to pass documents to another party, a lawyer or a medical practitioner; s 50(3) is a
  lawyer's or medical practitioner's offence, not the claimant's.
- s 52(1), (2), (4), s 55: how proceedings are run and decided; nothing turns on a claimant's facts.
- s 58(2): the summary of agreements registered under the former s 66A of the Workers Compensation Act 1987 (historic).
- s 64(1), (2): the immunity of representatives and witnesses (a lawyer's or witness's own protection; could be added).
- Sch 1: savings and transitional provisions for the change from the Workers Compensation Commission and the motor
  accidents dispute services on the establishment day (1 March 2021); spent for new claims.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 31(5)(b) "with the consent of the parties" -- `Can my proceedings be conducted outside New South Wales` --
  all the parties must consent -- a majority, or the parties other than the one opposing.
- **F2** s 51(2), (3) -- `Do I commit an offence by not complying` -- a summons in the Motor Accidents Division to a
  person who is not a party is not "a summons served ... under this section", so not complying is no offence (`JUST
  FALSE`) -- the summons stands until set aside and the offence is made out.
- **F3** Sch 3 cl 7, Sch 4 cl 7 "not admissible unless the person who made the statement agrees" -- `Can evidence of the
  statement be admitted in court` -- with agreement, or in an excepted proceeding, `NOTHING` (the bar lifts and the
  general law of evidence decides) -- `JUST TRUE`.
- **F4** s 56(2)(b) "not ... liable to be challenged ... by any court" -- `Can a court hear a challenge to the decision`
  -- a court appeal that the enabling legislation gives stands, because Part 5 is subject to the enabling legislation
  (s 41(1)) -- s 56(2)(b) shuts out every court except the Supreme Court on jurisdictional error.
- **F5** s 59(2), (3) -- `Does the certificate operate as a judgment` -- a certificate that does not identify the person
  liable is not "a certificate given under this section" (`JUST FALSE`) -- the defect does not stop it operating.
- **F6** s 27(2) "first lodged ... before the expiry of the period" -- `Does s 27 keep my application in time` -- lodging
  on the last day of the period is before its expiry -- the period expires at the start of its last day.
- **F7** Sch 5 cl 8(1) "about any act or omission ... of an insurer that affects the entitlements, rights or obligations
  of the claimant" -- `Can I complain to the Independent Review Officer` -- a complaint about something that does not
  affect those rights answers `NOTHING` (a grant limited in its own words) -- `JUST FALSE`, since cl 6(a) gives the
  Officer only complaints "under this Schedule".
- **F8** Sch 5 cl 8(4) "within a period of 30 days after the complaint is made" -- `By what day must my complaint be
  dealt with`, `Has my complaint been dealt with in time` -- the day of the complaint is not counted, so the period ends
  30 days later; a notice given after the 30 days does not extend it; a notified period ending sooner is not "longer"
  and is ignored; the Officer "deals with" a complaint by reporting (cl 8(2)) -- the Interpretation Act 1987 (not
  deposited) might count otherwise; a late notice might still bind.
- **F9** s 26(1) "A person with standing" -- `Can the District Court give me leave` -- without standing, `JUST FALSE`
  (the grant names its holder) -- `NOTHING`, standing being for the regulations.
- **F10** s 48(1), (2), (8) -- `Am I entitled to be represented by this person` -- a non-lawyer refused under s 48(2)
  answers `JUST FALSE` in every Division; an agent in the Motor Accidents or Police Officer Support Scheme Division, not
  refused, answers `NOTHING` because "agent" is undefined there -- any person the party appoints is an "agent" there
  (`JUST TRUE`).
- **F11** s 49(1)(a), (b) "at a time ... specified", "within a time specified" -- `Did I comply with the direction in
  time` -- both read as "by the last day the direction allows", that day included -- (a) read as an appointment at one
  time only.
- **F12** s 57(1), s 56(1), Sch 3 cl 6, Sch 3A cl 5 -- `Can the Commission reconsider my matter`, `Is the decision final
  and binding`, `Must the member try to settle my dispute first` -- the Motor Accidents Division, which these provisions
  do not name, answers `NOTHING` -- `JUST FALSE`.

## Rulings recorded

The rulings of 2026-11-04 and 2026-11-05 in `docs/ENCODING-GUIDE.md` section 5 govern every `NOTHING-kind` tag here:
in short, `JUST FALSE` only where the text says no in its own words (a "means" definition; a condition introduced by
"if", "only if", "unless", "provided"; a flat negative; a period the text fixes); `NOTHING` where the text lists without
closing, is silent, points outside the sources, or limits a grant in its own wording and the case falls outside. The
case-by-case sites are the forks above.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 48(1), (6) | the claimant | right to representation and assistance | `Am I entitled to be represented by this person`, `Am I entitled to an interpreter or other assistance` |
| s 48(3) | the insurer | disability: no lawyer against an unrepresented claimant without leave | `May the insurer be represented by a lawyer` |
| s 49(1), (3) | the person directed | duty with a deadline | MUST rule; `Did I comply with the direction in time` |
| s 49(4) | the person who withheld | disability: cannot have the material admitted | `Can I have the document or information admitted` |
| ss 38, 40 | assessors, reviewers, mediators | immunity from compulsion | `Can I compel them to give evidence` |
| s 56(1), (2) | the parties | disability: no appeal or court challenge, save as provided | `Is the decision final and binding`, `Can a court hear a challenge to the decision` |
| s 64(3), (4) | relevant Commission officers; the Crown | immunity; liability | `Can I hold the officer personally liable`, `Does the liability fall on the Crown` |
| Sch 5 cl 8(1) | the claimant | power to complain | `Can I complain to the Independent Review Officer` |
| Sch 5 cl 8(4) | the Independent Review Officer | duty with a deadline | MUST rule; `Has my complaint been dealt with in time` |

## What the Act turns out to say

1. **The Act sets almost none of a claimant's time limits.** s 45 says applications and appeals are made "in the time
   and manner prescribed by enabling legislation or the Commission rules". The only deadline the Act fixes for the
   claimant's benefit is the Independent Review Officer's 30 days (Sch 5 cl 8(4)); a claimant reading this Act alone
   would not learn when to apply or appeal.
2. **Police officers cannot complain to the Independent Review Officer.** Sch 5 cl 1 defines "claimant" as a person with
   a claim under the 1998 Act, the 2017 motor accidents Act or the 1999 motor accidents Act. The police officer support
   scheme was added elsewhere (s 5 "enabling legislation", s 25(c1), Sch 3A) but not here. Whether this is deliberate or
   an omission in the amending Act is not known (the deposited text has no history notes). Asserted (`JUST FALSE`).
3. **"Insurer" for complaints is a licensed insurer only.** Sch 5 cl 1 says "insurer means a licensed insurer under any
   of the enabling legislation", and cl 7(4) names the Nominal Insurer and the Nominal Defendant separately from
   insurers. Whether a complaint lies about the Nominal Insurer (which manages most NSW workers compensation claims), a
   self-insurer or the Nominal Defendant turns on the enabling Acts' meaning of "licensed insurer", which is asked.
4. **"Agent" is defined only for the Workers Compensation Division** (s 48(8)). In the Motor Accidents and Police
   Officer Support Scheme Divisions a party is "entitled to be represented ... by an agent" with no definition. Fork F10.
5. **Finality, reconsideration and conciliation-first cover two Divisions of three.** s 56(1), s 57(1), Sch 3 cl 6 and
   Sch 3A cl 5 reach the Workers Compensation and Police Officer Support Scheme Divisions; motor accidents decisions are
   left to the motor accidents legislation. Fork F12.
6. **s 56(2)(b) has no saving for appeals the enabling legislation gives,** unlike s 56(1) ("Except as otherwise
   provided"). Read with s 41(1), which makes Part 5 subject to enabling legislation. Fork F4.
7. **Withholding a document has a lasting cost.** Under s 49(4) a party who did not, without reasonable excuse, produce a
   document or provide information as directed "cannot ... have the document or information admitted" in proceedings
   before the Commission "or a court": the bar follows the claimant into later court proceedings. Asserted.
8. **A non-party cannot be summonsed in a motor accidents matter** (s 51(2)), so a claimant cannot use a summons to bring
   an independent witness to an assessment conference. Fork F2.
9. **Sch 3 cl 7 sits in the Workers Compensation Division's schedule but speaks of "a statement made in proceedings
   before the Commission"** without naming the Division. The encoding applies it to a statement made in any Commission
   proceedings, when the later court case is on a work injury damages claim.
10. **The Independent Review Officer's 30 days carry no consequence.** Sch 5 cl 8(4) says the Officer "is to deal with"
    the complaint in time, but nothing follows if it does not. The regulative rule's `LEST BREACH` marks the failure;
    what a claimant can then do is not in the Act.

## Questions (exported)

`pic-commission.l4` (33), in the encoding's order: `Can my proceedings be conducted outside New South Wales`
(s 31(5)); `Am I entitled to be represented by this person` (s 48(1), (2), (8)); `May the insurer be represented by a
lawyer` (s 48(1), (3)-(5)); `Am I entitled to an interpreter or other assistance` (s 48(6)); `Must the Commission take
my lawyer's written submission into account` (s 48(7)); `Did I comply with the direction in time` (s 49(1), (3), (4),
with the MUST rule); `Can I have the document or information admitted` (s 49(4)); `Do I commit an offence by not
complying` (ss 49(3), 51(2), (3), Sch 3 cl 8, Sch 3A cl 6); `The most I can be fined in penalty units` (the same);
`Can evidence of the statement be admitted in court` (Sch 3 cl 7, Sch 4 cl 7); `Can I compel them to give evidence`
(ss 38, 40); `Can my matter be decided without a conference or hearing` (s 52(3)); `Can the member hearing my matter be
replaced` (s 53); `Can my proceedings be dismissed` (s 54); `Is the decision final and binding` (s 56(1)); `Can a court
hear a challenge to the decision` (s 56(2), (3)); `Can the Commission reconsider my matter` (s 57(1)); `Can the obvious
error be corrected` (s 57(2)-(5)); `Is this an example of an obvious error` (s 57(6)); `Will details of the decision be
published` (s 58(1)); `Does the certificate operate as a judgment` (s 59); `Can the District Court give me leave`
(ss 25, 26(1)-(3)); `What must I file with my application for leave` (s 26(4)); `On what day are my District Court
proceedings taken to have started` (s 27(1)(a)); `Does s 27 keep my application in time` (s 27(2)); `Must the member try
to settle my dispute first` (Sch 3 cl 6, Sch 3A cl 5); `Can I complain to the Independent Review Officer` (Sch 5 cll 1,
8(1)); `Can the Officer decline my complaint` (Sch 5 cll 7(3), 8(5)); `By what day must my complaint be dealt with`
(Sch 5 cl 8(4)); `Has my complaint been dealt with in time` (Sch 5 cl 8(2), (4), with the MUST rule); `Is my matter
within the purpose of ILARS` (Sch 5 cl 9(2)); `Can I hold the officer personally liable` (s 64(3)); `Does the liability
fall on the Crown` (s 64(4)).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Personal Injury Commission Rules 2021 and Regulation 2020, which set the time and manner of applications
  and appeals (s 45), further dismissal grounds (s 54(c)) and further published decisions (s 58(1)(f)).
- Check the amendment history of Sch 5 cl 1 (finding 2) and the enabling Acts' meaning of "licensed insurer" (finding 3).
- Have a lawyer review the forks, especially F2 (non-party summons), F4 (court appeals) and F10 ("agent").
- Link the encoding to the workers compensation and motor accidents encodings that create the claims.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
