# Employment of Foreign Manpower Act 1990 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the foreign employee, with the design
defaults ruled on 2026-10-18. No pipeline, no coverage table, no independent
test pass, no human gate. Not for public use as advice.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/12/2025"), with amendments to Act 31 of 2023 shown, as deposited at
`../../registers/source-bundle/EFMA1990.txt`; with the Employment of Foreign
Manpower (Work Passes) Regulations 2012 (S 569/2012), informal consolidation in
force from 1 January 2026, as deposited at
`../../registers/source-bundle/EFMA1990-S569-2012.txt` — regs 2(3), 17, 18 and
the Seventh Schedule only.

**Checks:** `l4 run efma-cases-foreign-employee.l4` with the stable `l4` of VS
Code extension 1.6.98 — 60 assertions written, 60 satisfied, 0 errors, 0
warnings (19 October 2026). `l4 run efma-foreign-employee.l4` is clean too. Two
`#TRACE`s run the s 9(1) and s 14(1) duties as regulative rules (both FULFILLED).

This baseline replaces the first-pass encoding (`naive-2026-10`, 118
assertions, written without a seat). It covers every section the first pass
covered (ss 5, 6A, 9, 10, 11, 12, 22A, 22B, 23A, 25, 25A, 25G, 27), turned
round to face the worker, and adds s 2, s 5(2) and (7), s 6, ss 13, 14, 21, 22,
25C(4)(c) and the three regulations. The first pass's hand-checked values were
re-derived against the text and reused where still right (the s 5(6) fines of
5,000 / 30,000 / 60,000 and the one-month minimum, the s 6A repeat maximum of
30,000, the 30% levy-penalty cap giving 300 on 1,000, the s 23A order of 4,500,
composition of 5,000 and 3,000, the 14-day appeal, the s 22B six months and
caning at six convictions).

## Seat

**The foreign employee** — a foreigner who works, or seeks or is offered work,
in Singapore for an employer; for s 10 and s 11, the foreigner who works on his
or her own account. One case is one work pass and one employment.

Most of the Act's duties fall on employers, but the person the Act is applied
to, in the sense the ruling means, is the worker: the Act decides whether he or
she may work at all (ss 5(2), 10, 12), what he or she can be punished with
(ss 5(7), 10(2), 22), whether he or she can be arrested without a warrant
(s 21), what may and may not be taken from his or her pay (ss 22A, 25(6)), and
what happens to the job when the pass goes (s 9). The employer, the occupier,
the Controller and the court appear only as people who act towards the worker,
so every decision is phrased as the worker would ask it (`Is my work pass valid
for this work for this employer`, `Am I breaking section 5(2) by working for
this employer`, `What does the Act say about my employer taking this from me`,
`Can I be arrested without a warrant if suspected of`), from facts the worker
could state. What the person who employs the worker risks is kept, because the
first pass covered it, and asked as the worker would ask it (`What is the most
the person who employed me can be fined`).

The defaults ruled on 2026-10-18, and where this encoding stands:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed, with one small extension. The Work Passes Regulations are deposited;
  regs 17 and 18 and the Seventh Schedule set what s 25(6) lets the employer
  recover from the worker and for how much, so they are brought in. Reg 2(3) is
  brought in too, though it sets no number, because it decides whether a work
  pass is "valid" — the fact on which ss 5(2), 6A and 10 turn (a departure,
  for that reason). The work pass conditions in the First to Sixth Schedules
  are not numbers and are left out. The levy orders under s 11 were not
  deposited: the levy and its late-payment penalty are inputs.
- **The actors the text names.** Followed: the foreign employee, the
  self-employed foreigner, the employer, the occupier and principal contractor,
  the Controller, employment inspectors and police officers, the court, the
  Appeal Board, the Minister.
- **A judgment handed to someone else answered conditionally.** Followed:
  the Controller's approval of other work (s 12(1)(b)), the Controller's
  permission to shift a s 25(6) cost (s 25(6), reg 18) and the Minister's
  Gazette notification (s 2) are inputs named `if ...` or stated as the
  official's act, never guessed. Whether the CPC exempts someone from caning
  (s 22B(3)) is asked as a fact, the CPC not being deposited.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed. "Foreigner", "foreign employee", "self-employed
  foreigner" (s 2) and "valid work pass" (s 12) are worked out from facts.
  "Contract of service", "permanent resident" (Immigration Act) and
  "negligence" are asked as facts.
- **One case is the text's natural unit.** Followed: one work pass and one
  employment.
- **The Act's own terms, each with a plain gloss.** Followed: each § carries a
  gloss in a comment.
- **The operative sections in, the machinery out.** Followed: appointments,
  exemptions, the register, burden of proof, inspection powers, the manner of
  arrest, bodies corporate, abetment, the Appeal Board's constitution, forms,
  regulation-making and transitional provisions are out.

## Why this scope

A baseline is held to 25-60 assertions. This one keeps to what a foreign worker
meets — whether the Act treats me as a foreign employee, whether my pass covers
this job, what I risk by working without one, arrest, the money my employer may
not take, losing the job on revocation, the levy, a lost pass, the Controller's
penalties and my appeal — and keeps the first pass's employer-side tables as
the worker's view of what the employer risks.

Left out: ss 3, 3A, 4, 7 (except as inputs), 8, 9(2), (4), 15-20, 21A-21G, 23,
24, 25(5), 25B, 25D-25F, 25H, 26, 28-30 and the Schedule; from the Regulations
everything but regs 2(3), 17, 18 and the Seventh Schedule's duplicate-pass fees
— in particular the conditions of the Fourth Schedule Parts VI and VII that
bind the worker directly.

## What the Act turns out to say

1. **The worker commits an offence too.** s 5(2): "A foreign employee must not
   be in the employment of an employer without a valid work pass" — up to
   $20,000 or 2 years or both (s 5(7)), longer than the 12 months an employer
   faces on a first conviction under s 5(6)(a). The first pass did not encode
   it. Asserted.
2. **A pass is valid only for one employer and one line of work, and dies
   with the immigration pass.** s 12(1) ties the pass to the employer named in
   it and the occupation specified or applied for, unless the Controller has
   approved other work; reg 2(3) ends it when the immigration pass "expires and
   is not renewed or is cancelled". Asserted.
3. **A lost or damaged pass is the employer's cost unless the worker was
   negligent, and never the third time.** Reg 17 lets the employer recover the
   duplicate fee for a damaged pass ($65.40) and for the first replacement of a
   lost pass ($109) only where the worker's negligence caused it. The $327 fee
   for a second or later lost pass is not listed, so it stays with the employer
   (reading: a duplicate is an "issuance" within s 25(6)(a) — an inference). The
   miscellaneous work pass has no duplicate fee. Asserted.
4. **Placement fees and deposits are crimes; recovering the levy is a
   penalty.** A fee for getting or keeping the job, or a financial guarantee,
   is an offence under s 22A (up to $30,000 or 2 years). The levy, pass fees,
   insurance, medical examinations, required training and repatriation "at any
   time" are the employer's to bear (s 25(6)); taking them from the worker
   draws a financial penalty of up to $20,000 (s 25(4)), not a prosecution.
   Any other unexplained sum is presumed a kickback until the taker proves
   otherwise (s 22A(3)). Asserted.
5. **The s 23A order does not, on its words, go to the worker.** On conviction
   the court must order the taker to pay a sum equal to what was taken, but
   s 23A(3) treats it "as if that sum were a fine"; the text does not say the
   worker receives it. Asserted (the amount); the destination is quoted only.
6. **A literal oddity in s 22A(3).** When the Controller lets an S pass
   holder's employer shift repatriation or training to the worker with the
   worker's written consent (reg 18), the cost is no longer one "the employer
   ... must bear", so s 22A(3)(a) no longer excludes it, and it is not a fee
   "prescribed as recoverable" under s 25(6)(a) either; on the literal words
   recovering it is presumed to be consideration for the employment. That is
   probably not what was meant. Asserted, as the literal reading.
7. **Not every pass offence allows arrest without a warrant.** s 21(1) lists
   s 5(7), s 10(2) and most of s 22, but not s 22(1)(b) (failing to produce the
   pass on demand) or s 22(1)(g) (letting another hold my pass, not handing it
   over, not reporting a loss). An employment inspector may hold an arrested
   person no more than 48 hours, not counting the journey to the Magistrate's
   Court (s 21(4)); a police arrest is left to the CPC, so the encoding returns
   NOTHING. Asserted.
8. **Revocation ends the job within 7 days, and the worker cannot fight it
   through a union.** s 9(1) gives the employer 7 days from notification; s 9(5)
   takes the termination out of union negotiation, industrial action and trade
   disputes. s 9(6) keeps a late termination from making the contract illegal
   (quoted only). Asserted.
9. **The levy is the employer's unless the worker is self-employed, and runs
   until the pass ends formally.** s 11(1) puts it on employers, or on
   self-employed foreigners; s 11(2) keeps it running until the pass expires, is
   suspended or revoked, or is cancelled on application — the worker leaving
   is not on the list. The late-payment penalty is capped at 30% of the levy
   outstanding (s 11(5)). Asserted.
10. **For the employer, a repeat individual must be jailed and a repeat company
    cannot be.** s 5(6)(b): an individual's second conviction carries at least
    one month; any other offender gets $20,000 to $60,000 and no prison.
    Obtaining a pass for a phantom business carries a presumptive minimum of 6
    months (s 22B(1)) and caning at six convictions from more than five charges
    (s 22B(2)). Ignorance of nationality is no defence without checking the
    passport (s 5(5)); a principal contractor has three alternative routes
    (s 6A(3), the "or" read as making them alternatives — an inference).
    Asserted.
11. **Before the Controller the worker stands alone, and has 14 days to
    appeal.** No party may be represented "by an advocate or solicitor or a
    paid agent" (s 25C(4)(c)); an appeal must be lodged within 14 days and holds
    off the determination only if it is against a financial penalty or its
    amount (s 25G). The Controller's penalty for breaching a regulatory
    condition is up to $10,000 (s 25(2)). Asserted.
12. **Composition never costs more than $5,000.** s 27 caps it at the lower of
    half the maximum fine and $5,000; every worker's offence in this encoding's
    table (ss 5(7), 10(2), 22) carries a maximum fine of at least $10,000, so the cap is always
    $5,000 for the worker. Asserted.

## What would need doing before this is worth anything

- The work pass conditions that bind the worker (Fourth Schedule Parts VI and
  VII and their equivalents), which give s 22(1)(a) and s 25(2)(b) their
  content.
- The levy orders under s 11, and any Gazette notifications under s 2 (foreign
  employee classes), s 4 (exemptions) and s 6A(5), (7).
- The Criminal Procedure Code 2010 provisions the Act points to (ss 325, 330,
  319) and the Immigration Act 1959 definition of permanent resident.
- No case law on s 22A(3) or s 22B was searched, and no human gate has been
  sought.
