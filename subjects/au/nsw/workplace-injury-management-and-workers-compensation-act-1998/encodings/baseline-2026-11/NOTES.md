# Workplace Injury Management and Workers Compensation Act 1998 (NSW) -- baseline encoding, the injured worker

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 1 July 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (s 267 with s 268; s 316)
run by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The Workers Compensation Act 1987 (the entitlements:
weekly payments, medical expenses, lump sums, the s 151H damages threshold) has its own encoding beside this subject
(`subjects/au/nsw/workers-compensation-act-1987/encodings/baseline-2026-10/`); this one covers the claims machinery of the
1998 Act that a claimant meets.

## Edition

- **Act:** Workplace Injury Management and Workers Compensation Act 1998 No 86, corpus document
  `nsw_legislation:2024-07-01/act-1998-086` (in force 1 July 2024), deposited at
  `../../registers/source-bundle/act-1998-086.txt` (sha256 cbe697da...adfb30c8 as committed), taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text.
- **The instrument that sets one of its numbers:** clause 42 of the Workers Compensation Regulation 2016 (the circumstance
  prescribed for s 297(3)(e)), deposited at
  `subjects/au/nsw/workers-compensation-regulation-2016/registers/source-bundle/sl-2016-0559.txt` (sha256
  9c24119b...b92ee2f5), line 561, same corpus and caveat. The stable `l4` cannot IMPORT across subjects, so the clause is
  quoted in `wim-disputes.l4`.
- **Not deposited:** the Workers Compensation Guidelines (reasonable excuses, a provisional medical amount other than
  $5,000) and indexation of the $7,500 cap under Division 6 of Part 3 of the 1987 Act. Each is an input that answers
  `NOTHING`, or a yes/no fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wim-dates.l4` | 0 | 0 | 0 | 0 |
| `wim-claims.l4` | 0 | 0 | 0 | 0 |
| `wim-disputes.l4` | 0 | 0 | 0 | 0 |
| `wim-cases-claims.l4` | 0 | 0 | 125 | 125 |
| `wim-cases-disputes.l4` | 0 | 0 | 99 | 99 |

Every expected value was worked by hand from the text, with the edges: the last day and the day after of every period
(7, 14, 21, 28, 42 days; 1, 2, 3, 6 months; 3 years), month ends (31 August plus 6 months, leap years), the 83/84-day
(12 weeks) and 1-year lines of s 80, the 14/60 days of s 48A, the 70/71 and 84/85 days of s 298, $700 and $701 in the
worker definition, 7 and 8 days of a significant injury, $5,000 and 20% exactly in s 352, and the note's own 30% to 27%
example in s 323.

## Seat

**The injured worker** making a claim under Chapter 7 (a "new claim"), and, for work injury damages, the worker as
claimant against the employer. Every exported question is one the worker would ask ("Am I a worker?", "Does the notice
rule stop me?", "By when must I claim?", "Has the insurer started my payments in time?", "How much notice must I get?",
"May I refer my dispute?", "May I start court proceedings?"). Provisions addressed to the insurer, the employer, the
President, the Commission or a medical assessor are encoded as what they mean for the worker: a date, a stop on payments,
a presumption, an amount. No other seat: the employer's duties here are mostly to the insurer and the Authority, and
officials get none. Dependants claiming on a worker's death are another seat, not written.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulation's clause 42 is brought in;
  the Guidelines are not deposited (inputs). The Act's printed $5,000 and $7,500 are used where nothing else applies;
  a substituted or indexed figure changes the answer (an input says so and the answer is `NOTHING`).
- **The actors the text names.** Followed: worker, employer, insurer, Nominal Insurer, Authority, President, Commission,
  medical assessor, mediator, defendant.
- **Judgments answered conditionally.** Followed: "as soon as possible", "reasonable cause", "not prejudiced", "likely",
  "reasonably practicable", "reasonable efforts", "minimal prospects", "special circumstances", "interests of justice",
  "reasonably necessary" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: worker, injury, significant injury, the required
  period of notice, threshold dispute, the s 323 deduction are worked out; current work capacity, suitable employment and
  work capacity decision (1987 Act terms) and Schedule 1 deemed workers are asked.
- **One case.** One worker, one injury, one claim.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**
- **Definitions** -- s 4(1) worker (exclusions (a)-(d); Schedule 1 asked), injury.
- **Injury management (Chapter 3)** -- s 42 significant injury with s 45(1); s 48, s 48A(1)-(7); s 49.
- **Medical examinations** -- s 119(1)-(4) with s 324(2).
- **Notice and claims (Chapter 7 Part 2)** -- ss 44(1), 254 (with (3), (4)), 256(4); s 261(1), (3)-(6), (9); s 262 (as a
  fact); s 280A, s 280B.
- **Dealing with claims (Part 3)** -- ss 266, 267, 268 (a regulative rule); s 270; ss 274-276; s 279; s 280; ss 281,
  282(2), (3).
- **Stopping or reducing weekly payments** -- ss 80, 84.
- **Disputes (Parts 4, 5)** -- s 287A; ss 288(1), 289, 289A, 289B; s 297(2)-(4) with Regulation cl 42; s 298; s 304;
  s 308(1), (2).
- **Work injury damages (Part 6)** -- ss 313, 314, 315(2), 316 (a regulative rule), 318(1)(c), 318A(1), (2), (4).
- **Medical assessment (Part 7)** -- s 322A, s 323(1), (2), s 327(3), (5), (7), s 330(2), (3).
- **Appeals** -- s 352(3), (3A), (4).

**Out, and why:**
- Chapter 2 (administration, funds, information sharing) and Chapter 10 machinery: machinery.
- Chapter 3: ss 41-43 (programs; the insurer's 3-working-day contact in s 43(4) needs public holidays not deposited),
  s 45(2)-(7), ss 46, 47 (participation duties with no deadline or consequence of their own beyond s 48A and s 297),
  s 50, ss 52-59E (return-to-work programs, schemes, insurer and employer compliance, improvement notices).
- Chapter 4 Part 2 Divisions 1, 4, 5 and most of 6-7 (ss 61-69, 91A-104, 105-130): by ss 60A, 91A, 100A, 111A, 118A they
  apply only to existing claims (before the 2001 and 2002 commencements). s 119 is taken because s 118A does not limit it.
- Chapter 4 Division 2: s 71 (claimant's duty to co-operate; its bar on Commission proceedings would need the date
  proceedings start), ss 72-75; Division 3 ss 76-79, 81-83 (form of notices, the effect of review decisions on the notice
  period), s 85 (offence); Division 8 (touting).
- Chapter 6: ss 230A-249, including s 232 (right to information) and s 233 (no contribution from workers), which are
  plain rights with no test to work out.
- Chapter 7: s 255 (form of notice), s 257, s 258, s 260 (claim form, set by the Guidelines), s 263 (costs), s 264
  (employer forwarding, 7 days: the employer's duty to the insurer), ss 271-273, 277, 278, 283-286 (offences, fees,
  partial acceptance), s 287, s 287B, ss 290-296, 299-303, 304A-307, 309, 310, 311, 312, 317, 318(1)(a), (b), (d), (2),
  (3), 318B-318I, 319-321A, 322, 324(1), (3), (4), 325, 326, 328, 329, 331 (procedure), Part 8 (costs), s 351, s 353,
  Part 10 (Guidelines), Schedules.
- Claims on a worker's death (s 261(2), (7); s 281(6)): another seat.
- The commencement-dependent application provisions (ss 252, 259, 265; existing versus new claims): the encoding assumes
  an injury, claim and notification to which Chapter 7 applies.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** every "within n days after", "n months after", "at least n days after" -- `wim-dates.l4` -- the last day is the
  day plus n days, or the same day number n months later (the month's last day where there is none) -- an inclusive count
  from the event, or the Interpretation Act 1987 (not deposited) read otherwise.
- **F2** s 256(4) -- `Does the notice rule stop me` -- a register entry made as soon as possible answers s 254 whole,
  including "before the worker has voluntarily left" -- the entry answers only the "as soon as possible" limb.
- **F3** s 261(5), (6) -- `Does the time limit stop me` -- the 3 years in (4) and (5) run from the day the injury is
  taken to be received under (6) -- from the day it actually happened.
- **F4** s 274(3), s 276 -- `By when must my weekly payments claim be decided` -- a provisional period ending before the
  21 days does not shorten them -- the period ends with the provisional period.
- **F5** s 4 worker, (d) "except as provided by Schedule 1" -- `Am I a worker` -- where no contract exists, Schedule 1 is
  the only route and answers `NOTHING`; the (a)-(c) exclusions are applied only to a person with a contract -- Schedule 1
  deeming overrides (a)-(c) too.
- **F6** s 282(3) "unless the insurer requested ... within 2 weeks" -- `May the insurer delay for insufficient
  particulars` -- a request in time answers `NOTHING` (whether the particulars are insufficient is not settled) -- `JUST
  TRUE`.
- **F7** s 80(2), (4) "continuous period" -- `the notice required, run from` -- measured from the start of the current run
  of payments to the day the notice is given; 12 weeks is 84 days, 1 year the calendar anniversary -- measured to the day
  payments stop.
- **F8** s 84(3) -- `What can I recover for short notice` -- the weekly difference times the days of the required period
  not given, divided by 7 -- whole weeks only.
- **F9** s 289A(1) -- `May I refer my dispute to the Commission` -- not applied where the only route is the insurer's
  failure to determine (there is then no notice of dispute) -- applied literally, which would bar every such referral
  (finding 2).
- **F10** s 323(2) "(or a part of it)" -- `My impairment after the s 323 deduction` -- the 10% is assumed for the whole
  deduction or not at all -- for the difficult part only.
- **F11** s 314(1)(b) and (2)(a) -- `the s 313 threshold bar holds` -- where 15% is accepted (or certified) and
  ascertainability is disputed, (2) prevails: no threshold dispute -- (1)(b) prevails.
- **F12** s 289B(2) "before the expiry" -- `Will my referral stay the work capacity decision` -- a referral on the day the
  3 months end (the expiry day) is not before it -- it is.
- **F13** s 308(1) "14 days (or such longer period as the President may allow)" -- `Do I lose weekly payments for
  ignoring a recommendation` -- an "allowance" under 14 days is read as 14 -- the President's figure.
- **F14** s 316(1) "respond" -- the s 316 rule and `Can my employer still dispute liability` -- the response (acceptance or
  denial with a defence) is one act; a defence served within 42 days lets the defendant dispute liability -- the defence
  is a separate act from the acceptance or denial.
- **F15** s 119(4) -- `Are my compensation rights suspended for an examination` -- refusing an employer's requirement not
  made in accordance with the Guidelines suspends nothing -- (4) bars the requirement but (3) still suspends.
- **F16** s 267 with s 268 -- the s 267 rule -- where the insurer has a Guidelines excuse, either commencing payments or
  the written notice within 7 days keeps the duty -- with an excuse, only the notice does.
- **F17** s 48A(1) -- `What may the insurer do if I do not try to return to work` -- every s 48A step goes through the
  written notice of (2); compliance by the notice date leaves nothing to do -- (1)(b), (c) may be used without a notice.
- **F18** s 297(3) and (5) -- `Is an interim payment direction presumed warranted` -- "unless it appears" answered `JUST
  FALSE` for the presumption only; (5) keeps a direction possible -- the presumption answer as `NOTHING`.

## What the Act turns out to say

1. **Two definitions of injury.** s 4 of this Act defines a disease injury by employment as "a contributing factor"; the
   1987 Act's s 4 (deposited beside it) requires "the main contributing factor". The 1987 Act is construed as part of this
   Act (s 2A, noted at s 4). `Is it an injury` encodes this Act's words; for entitlement to compensation the 1987 Act's
   narrower definition is the one usually applied. Asserted on this Act's words.
2. **s 289A(1) and failures to determine.** A dispute "cannot be referred ... unless it concerns only matters previously
   notified as disputed". Where the insurer has simply not determined a claim (s 289(1)(b), (2)(b), (3)(c)), nothing has
   been notified as disputed, so read literally s 289A would bar the very referrals s 289 allows. Fork F9 takes the
   working reading.
3. **The s 313 bar lifts on any assessment.** A claimant with a threshold dispute cannot serve a pre-filing statement or
   sue "unless the degree of permanent impairment has been assessed by a medical assessor". Read literally, an assessment
   below 15% lifts the bar; damages are then refused by s 151H of the 1987 Act, not by this Act. `Does the threshold
   dispute stop me` answers no once any assessment is made (asserted), so `May I serve my pre-filing statement` can answer
   yes after an assessment below 15%.
4. **s 297(1A) points at s 298, not s 297.** "Section 298 does not apply to a dispute concerning a decision ... to
   discontinue or reduce weekly payments ... on the basis of a work capacity decision". s 298 only limits the period of a
   direction; the subsection reads as if meant to exclude interim payment directions for such disputes altogether. Not
   encoded; noted.
5. **s 314(1) and (2) can both hold.** An insurer may accept 15% while disputing that impairment is fully ascertainable:
   (1)(b) says there is a dispute, (2)(a) says there is none. Fork F11.
6. **s 80(2) does not say when the 12 weeks are measured.** "has received weekly payments for a continuous period of at
   least 12 weeks" -- at the decision, the notice or the stop. Fork F7.
7. **s 352(3)(b) when nothing was awarded.** "at least 20% of the amount awarded" is met by any amount when the decision
   awarded nothing; only the $5,000 limb then bites. Asserted.
8. **s 44(4)** reads "Subsection (2) do not apply" (a slip for "does"); harmless.
9. **The s 261 time limit runs from awareness for the 3 years too.** s 261(6) applies "for the purposes of this section",
   so it moves the 3 years in (4)(a) and (5) as well as the 6 months. Fork F3; asserted (awareness 1 June 2026).

## Questions (exported)

`wim-claims.l4` (22): `Am I a worker`, `Is it an injury`, `Must the insurer make me an injury management plan`, `Must my
employer give me suitable work`, `Is my suspension date allowed`, `What may the insurer do if I do not try to return to
work`, `Are my compensation rights suspended for an examination`, `Does the notice rule stop me`, `By when must I claim
compensation`, `Does the time limit stop me`, `By when must my provisional weekly payments start`, `Has the insurer
started my payments in time`, `May the insurer stop my provisional payments for missing papers`, `By when must my weekly
payments claim be decided`, `By when must my medical expenses claim be decided`, `How much medical expense can be accepted
provisionally`, `May I claim work injury damages`, `By when must my lump sum or damages claim be decided`, `May the
insurer delay for insufficient particulars`, `How much notice must I get before my payments stop`, `From when may my
payments be stopped`, `What can I recover for short notice`.

`wim-disputes.l4` (23): `May I ask for an internal review`, `By when must I get the review decision`, `May I refer my
dispute to the Commission`, `Will my referral stay the work capacity decision`, `Is an interim payment direction presumed
warranted`, `Is a medical interim payment direction presumed warranted`, `The most a medical interim payment direction can
give`, `Can an interim payment direction cover this period`, `Must I refund interim payments`, `Do I lose weekly payments
for ignoring a recommendation`, `Can my impairment be assessed`, `My impairment after the s 323 deduction`, `May I appeal
the medical assessment`, `By when must I appeal the medical assessment`, `What can I recover for attending a medical
assessment`, `May I appeal the Commission decision`, `Does s 280B stop me recovering damages`, `Does the threshold dispute
stop me`, `May I serve my pre-filing statement`, `By when must the defendant respond`, `From when may I refer to
mediation`, `May I start court proceedings for damages`, `Can my employer still dispute liability`.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Workers Compensation Guidelines (reasonable excuses, claim requirements, provisional amounts) and the
  current indexed figures.
- Have a lawyer review the forks, especially F1 (counting), F9 (s 289A), F11 (s 314) and F14 (the s 316 response).
- Add the dependants' seat (death claims) and the existing-claim provisions if they are needed.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
