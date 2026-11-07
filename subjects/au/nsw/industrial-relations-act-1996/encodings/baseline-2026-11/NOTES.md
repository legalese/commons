# Industrial Relations Act 1996 (NSW) -- baseline encoding, the employee bringing a claim

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025
> (corpus document dated 2 March 2025). It is unofficial and may be out of date: amendments after that version are
> missing. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 in substance. A seat-neutral core
(`ira-core.l4`) holds every rule; every time limit is one regulative rule (`PARTY the applicant MUST make the
application WITHIN ... LEST BREACH ... BECAUSE ...`) run by `EVALTRACE` inside a function that takes only plain facts.
The seat layer (`ira-seat.l4`) asks the questions and restates no rule. Dates sit in one small module (`ira-dates.l4`,
built-in date functions only, no daydate, no `YMD`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in
`LEST BREACH`.

Answers are named outcomes (enumerations), amounts or dates, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used.
Where the text says no in its own words ("is not an employee", "does not apply", "only if", "and not otherwise", "cannot
be made", "may only be made if", a "means" definition) the outcome begins "no:"; where the text is silent or uses an
open "includes" it says "this Act does not say"; where a provision's own scope is not met without an "only" (s 210's
list of reasons and its "employee or prospective employee") it says the section "does not reach this". Judgments the Act
leaves to the Commission that decide a test are inputs; judgments on whether a late application is accepted
(s 85(3), s 108B(3), s 213(4)) and on whether pay is "just and equitable" (s 367(2)) are answered conditionally in the
outcome's words. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Industrial Relations Act 1996 No 17, corpus document `nsw_legislation:2025-03-02/act-1996-017`, deposited at
  `../../registers/source-bundle/act-1996-017.txt` (text sha256 5354f837...0397075), from the Open Australian Legal
  Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Regulations:** the Industrial Relations (General) Regulation, which may prescribe the s 83(1)(b) threshold, the
  s 108A remuneration cap and the s 379 small claims maximum, is **not deposited**. The Act's own figures are encoded
  and a figure the person knows of is an input (finding 1).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ira-dates.l4` | 0 | 0 | 0 | 0 |
| `ira-core.l4` | 0 | 0 | 0 | 0 |
| `ira-seat.l4` | 0 | 0 | 0 | 0 |
| `ira-cases.l4` | 0 | 0 | 129 | 129 |

Negative control, in a scratch copy: with the s 85 period lengthened from 21 to 22 days and the s 83(1)(b) figure raised
from $62,200 to $62,201, the cases failed exactly the 7 predicted assertions (the two s 85 last days, the applications
made or considered on the 22nd day in March 2025 and January 2026, and the two $62,201 incomes).

Every expected value was worked by hand from the text, with day counts written beside the cases. Edges: the 21st and
22nd day after a dismissal (and across a year end); the s 85(2) 21 days after a Commonwealth withdrawal, and each of its
four conditions failing; the 28th day after notice in a common and a leap February; 12 months and 12 months plus 3 from
31 August and from 29 February; the sixth anniversary of a 29 February; $62,200, $200,000 and $10,000 exactly and a
dollar over; a package for 6 months taken over 12; a 6- and a 7-month increment deferral; a 5- and a 6-month fixed term;
a 3- and a 4-month probation; the s 105(1)(c) comparison equal and a dollar under.

## Seat

**The employee (or worker) bringing the claim (required)** (`ira-seat.l4`, 16 questions): the dismissed employee, the
public sector employee facing a disciplinary decision, the worker who is party to a contract said to be unfair, the
employee or job applicant who was victimised, and the person owed pay or other money. Questions, grouped under `§§`
headings with the situation in each heading's comment:

- Unfair dismissal (situation: dismissed or threatened): "Can I bring an unfair dismissal claim?", "By when must I
  apply about my dismissal?", "Am I in time to apply about my dismissal?", "What can the Commission order for my
  dismissal?"
- Public sector disciplinary appeals (situation: a decision of a public sector employer): "Can I appeal against my
  employer's decision?", "By when must I lodge my disciplinary appeal?", "Am I in time to lodge my disciplinary appeal?"
- Unfair contracts (situation: working under a contract said to be unfair): "Is my contract an unfair contract?",
  "Can I apply about my unfair contract?", "Am I in time to apply about my unfair contract?"
- Victimisation (situation: the employer or a union acted against you): "Was I victimised?", "By when must I apply
  about victimisation?", "Am I in time to apply about victimisation?"
- Unpaid pay and other money (situation: money owed): "Can I recover the money I am owed?", "By when must I apply to
  recover money?", "How much can a small claims order give me?"

Provisions addressed to the Commission or an industrial court are encoded for what they mean to that person: whether
they may apply, by when, and what may be ordered for them. No seat for the employer (a layer would be welcome: s 89
orders, s 90A, s 210 and the recovery orders bind the employer) and none for the Commission, the Registrar or an
industrial organisation.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, except that the regulation that may prescribe
  three figures is not deposited (finding 1); those figures are inputs, used only as the Act allows (a "greater" amount
  for s 83 and s 108A, "some other amount" for s 379).
- **The actors the text names.** Followed: the employee (applicant), the employer, the public sector employer, an
  industrial organisation, an inspector, the Commission, the industrial court.
- **Judgments answered conditionally.** Followed: whether reinstatement or re-employment is impracticable (s 89), whether
  a longer probation is reasonable (s 98(3)(b)(ii)), whether a contract is unfair, harsh or unconscionable, against the
  public interest or avoids an instrument (s 105(1)(a), (b), (d)), and whether the employer rebutted the s 210(2)
  presumption are inputs; sufficient reason (ss 85(3), 213(4)), exceptional circumstances (s 108B(3)) and "just and
  equitable" (s 367(2)) are answered conditionally in the outcome.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: employee (s 5(1), (4)), dismissal (s 83(5)),
  appealable decision (s 97(1)), unfair contract (s 105(1)), remuneration package over 12 months (s 108A(1)(b)),
  remuneration cap (s 108A(3)). Borrowed and asked: "employed", public sector employee, Federal award, apprentice or
  trainee, industrial instrument, probation, casual "for a short period", detriment.
- **One case:** one dismissal, one decision, one contract, one contravention, one amount owed.
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** Chapter 4 (the Commission), Chapter 5 Parts 2-8 (organisations), Chapter 8 and the Schedules'
  savings and transitional provisions.

## Scope

**In:** s 5 (employee); Chapter 2 Part 6 (unfair dismissals): ss 83, 84, 85, 89, 90 (ss 86-88 are the Commission's
procedure and matters it may consider, met only as the judgments above); Chapter 2 Part 7 (public sector disciplinary
appeals): ss 91, 92, 97(1), 98, 99(2), 100B; Chapter 2 Part 9 Division 2 (unfair contracts): ss 105, 106(1), (2A), 108,
108A, 108B, 109A; Chapter 5 Part 1: ss 210, 213(3), (4); Chapter 7 Part 2 (recovery of remuneration and other amounts):
ss 364-369, 377 (by the absence of any age input), 379(3).

**Out, and why:**

- **Chapter 2 Part 4 (parental leave) and Part 4B (leave for victims of crime), Part 5 (part-time work), Part 10
  (payment of remuneration), Part 11 (outworkers).** Entitlements rather than the claims machinery this baseline serves;
  a second pass on leave entitlements should take Parts 4 and 4B.
- **s 89(1)-(4), (6)-(8) beyond the caps:** continuity, the threat order, mitigation (s 89(6)) and terms are the
  Commission's choices; only the most that may be paid is encoded.
- **s 90A, s 90B** (industrial agents' certificates, how a payment discharges an order): address the representative,
  not the applicant's eligibility.
- **s 97(2)-(7), s 100, ss 100A, 100C-100H** (notice of the decision, carrying it into effect, the Commission's decision
  and orders, conciliation, presentation of cases): procedure and the Commission's choices. s 100D(1) and (3) are left
  for a pass on remedies (finding 6).
- **Part 9 Division 3 (ss 110-116)** (remuneration of building, handbill and door-to-door contractors): only an
  industrial organisation of employees may apply for the s 111 finding.
- **s 107, s 109** (further prohibiting orders; conciliation).
- **ss 210(1) "must not victimise" as a penalty provision, ss 211, 212, 213(1), (2):** the orders s 213(2) lists are
  the Commission's choices.
- **ss 370-376, 378, 379(1), (2), (4)-(8), 380** (making orders, conciliation, interest at the Civil Procedure Act
  s 101 rate, costs, amendment, enforcement, debt recovery in other courts, payment through organisations, small claims
  procedure and representation): the interest rate is in another Act; the rest is procedure.
- **Chapter 3 (industrial disputes), Chapter 6 (public vehicles and carriers, including Part 7 compensation on
  termination of contracts of carriage), Chapter 7 Parts 1 and 3-6 (penalties, Industrial Magistrates, inspectors,
  evidence, prosecutions).** The Chapter 6 Part 7 compensation claim is a claim a carrier meets and would be a good next
  pass.

## Forks (the text does not say; one reading taken)

- **F1** "N days after" a day ends on that day plus N; "12 months after" ends on the same day of the month 12 months on,
  or that month's last day where shorter (31 August 2024 plus 12 months plus 3 months is 30 November 2025; 29 February
  2024 plus 12 months is 28 February 2025).
- **F2** The regulative rule's day 0 is the day the time runs from (the dismissal, the notice, the termination, the
  contravention, the day the money fell due); an application made on the last day is in time.
- **F3** s 369(3) "within the period of 6 years immediately before the application": money that fell due on a day may
  be claimed by an application made on or before the sixth anniversary of that day (the other reading stops a day
  earlier).
- **F4** s 85 for a threat of dismissal: the 21 days run from the threat (the person gives that day as "the day I was
  dismissed").
- **F5** s 108A(1)(b) "would, if ... paid ... for a period of 12 months, have exceeded": the package is scaled pro rata
  by months (package x 12 / months).
- **F6** s 83(1)(b) and s 108A(3): a prescribed amount counts only if greater than the Act's figure ("such greater
  amount", "any greater amount"); s 379(3) "some other amount" counts whether higher or lower.
- **F7** s 83(1)(b)'s income test is applied only to an employee who is not a public sector employee, as para (a)
  covers "any public sector employee" without it.
- **F8** s 98(3)(b): a probation whose length was not fixed in advance is never caught; one fixed at more than 3 months
  is caught only if the Commission finds it reasonable (asked as an input).
- **F9** s 210(2): with no detriment from the employer's or organisation's action, the presumption does not arise and
  the Act does not define "victimise", so the answer is "this Act does not say", not "no".
- **F10** The order of the exclusions in the Part 6 answer: s 5(4), s 5(1), s 83(3), s 83(2), s 83(1A), s 83(1)(b),
  then whether there was a dismissal and a claim; only the first that applies is reported.

## What the Act turns out to say (findings)

1. **Three figures may be replaced by an undeposited regulation.** s 83(1)(b) ($62,200 "or such greater amount as is
   prescribed"), s 108A(3) ($200,000 "or any greater amount prescribed", indexed to the s 83 figure) and s 379(3)
   ($10,000 "or some other amount"). The regulation is not in the deposit, so an answer worked on the Act's figures
   alone may be wrong; the person can give the prescribed figure. Depositing the Industrial Relations (General)
   Regulation would let these be fixed. Asserted (the cases with and without a prescribed figure).
2. **Most private-sector employees in NSW are outside this Act.** s 9B makes the Act subject to the Fair Work Act 2009
   (Cth); for national system employers the Commonwealth Act governs, and Part 6 in practice reaches the NSW public
   sector, local government and the few employers outside the national system. s 83(1A) deals only with employees under
   a Federal award. The encoding does not decide national system coverage; the person answers whether they can go to
   the Fair Work Commission.
3. **No late disciplinary appeal.** s 100B(1) and (3) are repealed, and nothing left in Part 7 lets the Commission accept
   a notice of appeal lodged after 28 days, unlike s 85(3) and s 213(4). Whether the Commission's rules (not deposited)
   allow it is not worked out. Asserted ("out of time ... no power to accept a late one").
4. **s 108B is the only hard bar.** The Commission "does not have jurisdiction to extend" the 12 months, save a further
   3 months on exceptional circumstances; for a contract still running the Act fixes no time at all. Asserted.
5. **The high-income gap.** s 109A(1)(b) shuts Part 9 to an employment contract said to be unfair for a dismissal
   reason even where s 83 excludes the employee from Part 6, and s 108A shuts it to packages over the cap: a high earner
   with no industrial instrument can have neither remedy for the dismissal itself. Asserted (the s 109A and s 108A cases).
6. **s 100D(1)(b) against s 100D(3).** An allowed appeal may bring an order to pay up to the remuneration lost, but
   "nothing in subsection (1) enables ... compensation" where the person is not reinstated or does not continue. Whether
   (1)(b) back pay survives (3) for a person who does not return is not clear; left out.
7. **s 85(2) also covers an application not yet made.** The Commission "is required to accept" an application made
   within 21 days after a timely Commonwealth application is withdrawn or declined; the encoding answers it for an
   application made today as well. Asserted.
8. **"Victimise" is undefined.** s 210(2) supplies a presumption once a detriment is suffered, rebuttable only by the
   employer showing the alleged matter was not "a substantial and operative cause". Asserted.
9. **s 105(1)(c) has no stated comparator.** "less than a person performing the work would receive as an employee
   performing the work": the comparison employee's pay (presumably under the relevant award) is asked as a fact.

## Before relying on it

- Deposit the official current text and the Industrial Relations (General) Regulation; re-check the three figures and
  every section cited.
- An independent test pass and a coverage table; a lawyer's check of forks F3, F4, F7 and F9.
- An employer seat; passes on Chapter 2 Parts 4 and 4B (leave) and Chapter 6 Part 7 (carriers' compensation).
