# Employment Act 1968 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the employee, with the design
defaults ruled on 2026-10-18. No pipeline, no coverage table, no independent
test pass, no human gate. Not for public use as advice.

**Edition:** 2020 Revised Edition, informal consolidation in force from
5 December 2025, as deposited at `../../registers/source-bundle/EmA1968.txt`;
with the Employment (Retrenchment Reporting) Notification 2019 (S 200/2019),
version in force from 1 November 2021, as deposited at
`../../registers/source-bundle/EmA1968-S200-2019.txt`.

**Checks:** `l4 run ea-cases-employee.l4` with the stable `l4` of VS Code
extension 1.6.98 — 59 assertions written, 59 satisfied, 0 errors, 0 warnings
(19 October 2026). `l4 run ea-employee.l4` is clean too. One `#TRACE` runs the
s 21(1) duty to pay as a regulative rule (FULFILLED).

This baseline replaces the first-pass encoding (`naive-2026-10`, Parts 2 to 12,
334 assertions) and its seat layer (`ea-seat.l4`, 20 questions). Every one of
the seat layer's 20 questions is answered here, re-phrased where the defaults
required it; the first pass's hand-checked values were re-derived against the
text and reused where still right (28 days' notice on a void 1-day term, 5,600
in lieu, the s 13(2) limb (b) case, the s 14(2A) pair, the s 29 ceilings, rest
day pay of 50 / 137.5 / 237.5, annual leave of 7 and 4 days, sick leave of 14
and 24 days, maternity pay of 5,600).

## Seat

**The employee** — one person, in one employment with one employer. The Act is
applied first and last to the employee: it fixes the notice they are owed, when
and how they must be paid and what may be taken from their pay, their rest days
and overtime, their leave, their maternity protection, and when they may be
dismissed or suspended. The employer, the Commissioner and the Minister appear
only as people who must act towards them, so every decision is phrased as the
employee would ask it (`How many days of notice am I owed`, `Was I paid late`,
`Can I claim for wrongful dismissal`, `How much maternity pay must my employer
give me`), with facts the employee could state.

The defaults ruled on 2026-10-18, and where this encoding stands:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed. The Retrenchment Reporting Notification 2019 is deposited and
  brought in. The regulations that would set the prescribed minimum period and
  the key employment terms (s 95A), or substitute the s 29 and s 32 fractions
  and the s 35 salary caps, were not deposited; those numbers are inputs that
  carry the Act's own figures (`the proportions as the Act states them`, `the
  caps as the Act states them`, a `MAYBE` substituted period).
- **The actors the text names.** Followed: employer, employee, workman,
  Commissioner, Minister, President, Comptroller of Income Tax, Tribunal.
- **A judgment handed to someone else answered conditionally.** Followed, which
  departs from the first pass: "reasonable excuse" (s 13(2)), the inquiry's
  finding of misconduct (s 14(1)), the Commissioner's longer suspension period
  (s 14(8)) and permission for a larger deduction (s 29), and "sufficient
  cause" (s 80(3)) are all inputs named `if ...`, never guessed.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed. "Employee" (s 2(1)) and "workman" (s 2(1), with its
  half-the-time proviso) are worked out from facts; the s 10(3) bands are worked
  out from completed weeks and completed years, which the employee states
  (the first pass asked the bands themselves). "Managerial or executive
  position", "contract of service" and s 68(7) of the Income Tax Act are
  borrowed or undefined and asked as facts.
- **One case is the text's natural unit.** Followed: one employment. The
  retrenchment report counts heads across the workforce, which is the
  Notification's own unit, asked as one number.
- **The Act's own terms, each with a plain gloss.** Followed: each § carries a
  gloss in a comment.
- **The operative sections in, the machinery out.** Followed, which departs
  from the first pass: the s 96A administrative penalties and directions
  (ss 126A-126D), secrecy (ss 101-102) and the s 82 offence are out.

## Why this scope

The first pass covered nearly every operative Part. A baseline is held to
25-60 assertions, so this one keeps to what an employee most meets — the seat
layer's 20 questions — and adds a few the text puts beside them: whether the Act
covers me at all (s 2(1)), pay while suspended for an inquiry (s 14(8), (9)),
the employer's deemed breach for late pay (s 13(1)), income tax clearance
(s 24), the s 32 overall cap, the Fourth Schedule's hourly rate, s 76(4) and
s 80(3) on maternity pay, s 88A(8) on untaken leave, and the deadline for the
retrenchment report.

Left out (the first pass encoded some of these; the rest it did not either):
s 9, s 12, ss 16-19, s 20A, ss 25, 28, 30, 31, 33, s 36, the s 38(1) hour
limits and ss 38(5), 38(8), ss 39-41A, s 46, Parts 5-8 (contractors, part-time
employees, domestic workers, children and young persons), s 76(1)(c)(ii),
s 76(3), ss 77-80 except s 80(3), s 82, ss 84-87A (including childcare leave),
s 88 (public holidays), ss 95-96 (records and pay slips), and Parts 13-16.

## What the Act turns out to say

1. **The statutory minimum notice emerges from three provisions read in order.**
   s 10(2) lets the contract govern; s 8 voids a term less favourable than the
   Act "to the extent that it is so less favourable"; with the term void there is
   no provision, and s 10(2) sends the question to s 10(3). So a 1-day term gives a
   ten-year employee 28 days, and is perfectly lawful for a new starter. Asserted.
2. **s 13(2)'s "or" deems a breach even where the excuse is good.** An employee
   absent more than 2 days without leave who had a reasonable excuse but never
   told the employer is deemed to have broken the contract under limb (b). The
   employer's deemed breach (s 13(1)) has one element: late pay. Asserted.
3. **The 6-month qualification for a wrongful-dismissal claim bites only on a
   manager dismissed properly.** Under s 14(2A) a non-manager qualifies from day
   one, and so does a manager sacked without notice or salary in lieu; a manager
   given notice in month 3 does not. The answer is "subject to section 3 of the
   Employment Claims Act 2016", which was not deposited. Asserted.
4. **Suspension pending inquiry costs at most half the salary, and nothing if no
   misconduct is found.** s 14(8)(b) requires at least half; s 14(9) restores the
   withheld half "immediately" if the inquiry discloses no misconduct. The
   one-week limit can be lengthened only by the Commissioner. Asserted.
5. **s 45 only bars; the Act nowhere grants a retrenchment benefit or says how
   much.** The encoding returns `none` under 2 years and `not decided by this
   Act` from 2 years on. Asserted.
6. **The s 29 damages deduction has two ceilings and a procedural gate, and the
   Commissioner can lift only one of them.** It may not exceed the loss, nor
   (without permission) a quarter of a month's wages, nor be made before the
   employee has had a chance to show cause. Asserted.
7. **"Workman" turns on time, not title.** Under the s 2(1) proviso a person
   employed partly as a workman is deemed a workman unless the workman time
   never reached half in any salary period; one who never did is tested against
   the $2,600 cap, not the $4,500 one. Asserted.
8. **Rest day overtime counts "each hour or part thereof".** 1.5 hours over
   normal hours is paid as 2. With no agreed usual hours, normal hours are deemed
   8 (s 37(3A)). Asserted.
9. **Annual leave in a part year is a proportion rounded half up.** Six months
   into the first year gives 3.5, which s 88A(3)(b) makes 4. Reading (inference):
   the proportion is of that year's full entitlement. Asserted.
10. **Maternity pay can be lost or halved for reasons other than service.**
    s 76(4) removes it where the employee already has 2 or more living children
    from more than one previous confinement (subject to a collective agreement,
    award or Gazette notification); s 80(3) halves it if the notices were not
    given without sufficient cause; s 83 forfeits it for working for another
    employer. The benefit period is 8 weeks under every s 76(1) arrangement.
    Asserted.
11. **An incomplete or inaccurate key-terms record is a failure whatever the
    employer knew** (s 95A(5)); day 14 is in time, day 15 is not. Asserted.
12. **The retrenchment report turns on 10 employees and one notice, and runs
    from the day notice is given.** The current Notification has no minimum
    number retrenched and no aggregation period: any notice by an employer with
    10 or more covered employees must be reported "not later than 5 working days
    after" it is given. A notice given on Thursday 4 November 2021 must be
    reported by Thursday 11 November, or a day later if a public holiday falls in
    between (holidays illustrative; not in the deposit). Asserted.

## What would need doing before this is worth anything

- The regulations: the prescribed key employment terms and minimum period
  (s 95A), any substituted fractions and caps, the Fifth Schedule reckoning.
- The Employment Claims Act 2016, s 3, which s 14(2) makes the claim subject to.
- The pre-1 November 2021 text of the Notification, and the s 76(2), (2A)
  rules for confinements before 22 August 2015.
- Childcare leave (s 87A), public holidays (s 88), the s 38(1) limits, and the
  Parts left out above.
- No case law was searched and no human gate has been sought.
