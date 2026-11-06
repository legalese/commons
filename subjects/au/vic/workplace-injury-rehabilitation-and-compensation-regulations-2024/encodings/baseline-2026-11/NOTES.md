# Workplace Injury Rehabilitation and Compensation Regulations 2024 (Vic) — baseline encoding

Unofficial. Copyright (c) State of Victoria; Victorian Legislation, published by the Office of the Chief
Parliamentary Counsel with the authority of the Government Printer. Encoded from a plain-text conversion of the
register's Word file; only the authorised version is evidence (Interpretation of Legislation Act 1984 s 64).
Not for public use as advice.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE, no BECAUSE except
`LEST BREACH … BECAUSE`. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No
pipeline, no coverage table, no independent test pass, no human gate. Expected values in the case files are worked
by hand from the text.

The Regulations only fill in numbers and steps that the Workplace Injury Rehabilitation and Compensation Act 2013
leaves to them, so each question is encoded together with the provision of the Act it completes. The Act has no
encoding yet, and the stable `l4` cannot IMPORT across subjects, so the few Act provisions needed (s 3 "full-time
worker", Sch 2 items 2-8, Sch 1 cl 6(3) and 9(5)(c), s 175(4), s 179(5)-(7), s 388) are restated here in the narrow
form the Regulations need. When the Act is encoded, these should be cross-referenced, not copied further.

## Edition

- **Regulations:** S.R. No. 35/2024, Version No. 001, version as at 26 May 2024 (the current version on 2026-11-06),
  deposited at `../../registers/source-bundle/workplace-injury-rehabilitation-and-compensation-regulations-2024.txt`
  from the Word file the owner saved by hand on 2026-11-06 (see `../../SOURCE-LICENSE.md`, "Deposit, 6 November
  2026"; sha256 of the text in the `.meta.json`). No amendments. Sunset 21 May 2034.
- **Act (for the provisions the Regulations complete):** Act No. 67/2013, Version No. 054, incorporating amendments
  as at 2 October 2026, deposited at
  `subjects/au/vic/workplace-injury-rehabilitation-and-compensation-act-2013/registers/source-bundle/`.
- The conversion has not been checked against the authorised PDF (24-35sra001-authorised.pdf), which was not saved.

## Checks

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wirc-regs-dates.l4` | 0 | 0 | 0 | 0 |
| `wirc-regs-seat.l4` | 0 | 0 | 0 | 0 |
| `wirc-regs-seat-employer.l4` | 0 | 0 | 0 | 0 |
| `wirc-regs-seat-cases.l4` | 0 | 0 | 67 | 67 |
| `wirc-regs-seat-employer-cases.l4` | 0 | 0 | 32 | 32 |

`l4 run <file>` on each, read from the diagnostics (l4 exits 0 even when an assertion fails).

## Seats

**First seat: the worker** (`wirc-regs-seat.l4`): the injured worker, including a timber contractor or contractor
deemed to be a worker. Questions: `Am I a full-time worker`; `Which items of Schedule 2 describe me`; `What are my
pre-injury average weekly earnings under item 8`; `How much of my timber contract payment is my remuneration`; `What
percentage of my contract payments is not remuneration`; `How much of my contract payment is my remuneration`; `Must I
prove my identity and incapacity every 3 months`; `What must I do to prove my identity and incapacity`; `By when must I
next prove my identity and incapacity`; `Am I entitled to my weekly payments for this interval while overseas`; `How
must an inquiry into me be conducted`.

**Second seat: the employer** (`wirc-regs-seat-employer.l4`): an employer who pays weekly payments before the
Authority pays it (reg 13), and a self-insurer (regs 14, 15 with s 388). The text puts liabilities on both; a company
is a permitted seat. Questions: `By when must the Authority reimburse me`; `Is the Authority liable to pay me interest
on my weekly payment`; `What is my quarterly self-insurer contribution under regulation 14`; `What is my self-insurer
contribution under regulation 15`; `When is my next self-insurer contribution due`; `Can my contribution be recovered
as a debt`.

The two seats share no names. No mirror cases: no question is asked from both seats.

The 2026-10-18 defaults:

- **The instrument with what sets its numbers.** Followed, the other way round: the Regulations are the numbers; the
  Act provisions they complete are brought in (above). The costs and all-employer remuneration totals in regs 14 and
  15 are the Authority's figures and are inputs.
- **The actors the text names.** The worker, the employer, the self-insurer, the Authority, the medical practitioner,
  the principal, the timber contractor and contractor.
- **Judgments answered conditionally.** The Authority's or self-insurer's satisfaction under s 175(4) is an input.
  Whether the worker is deemed a worker under Sch 1 cl 6 or cl 9 (cl 9(2) turns on an Authority determination) is an
  input.
- **Own definitions worked out, borrowed terms asked.** "Full-time worker" (s 3 with reg 8) and the Schedule 2
  classes are worked out; "industrial award", "ordinary earnings", "relevant remuneration", the s 513(5) costs are
  asked.
- **One case.** One worker and one injury; for Schedule 2, exactly two employers (departure: the Schedule speaks of
  "2 or more"; the internal functions take two employments, so three or more are out of the exported questions).
  For the employer seat, one weekly payment, one contribution.
- **Terms with glosses.** In the `@desc` of each input.
- **Machinery out.** Regs 1-4 (objective, authorising provision, commencement, revocations).

Hours input (departure, fork F5): each job has one hours input, "ordinary hours a week", used both for the class tests
in items 2-6 ("works ... for at least ... hours each week") and for item 8(b) ("ordinary hours"). Overtime that would
lift a worker over 38 hours is not separately asked.

## Scope

**In:** reg 6 (how an inquiry under s 586 must be conducted, as a list); reg 8 with s 3; reg 9 with Sch 2 items 2-8
of the 2013 Act; reg 10 with Sch 1 cl 6(3); reg 11 and Schedule 2 of the Regulations with Sch 1 cl 9(5)(c); reg 12
with s 175(4) (a regulative rule for the 3-monthly proof, evaluated inside the exported question); reg 13 with
s 179(5)-(7); regs 14 and 15 with s 388(1)-(3), (5) (a regulative rule for payment within 14 days).

**Out, and why:**

- Regs 1-4: machinery.
- Reg 5 and Schedule 1 (the search warrant form under s 558): a form for the magistrate and police; the offences it
  warns of are in s 558 of the Act, not the Regulations.
- Reg 7 (what an evidentiary certificate under s 590 may include): addressed to the Authority's proof in proceedings;
  nothing for the worker to decide.
- Reg 9 as it applies to Schedule 1A of the Accident Compensation Act 1985: another Act.
- Reg 12 as it applies to s 97(3) of the Accident Compensation Act 1985: another Act.
- Reg 13 as it applies to s 114D of the Accident Compensation Act 1985: another Act.
- Sch 2 items 2-7 calculations (Division 1 of Part 5): the Regulations do not touch them; only item 8 is computed.
- Whether a person is deemed a worker under Sch 1 cl 6(1)-(2) or 9(1)-(2): Act, asked as a fact.
- The interest amounts under s 179(7) and s 388(5): the rate is not in these Regulations (finding 4).
- s 179(6) (no duty to reimburse an employer who applies more than 3 months after paying): Act; not asked.

## Negatives and "not covered"

Following the corpus convention (ENCODING-GUIDE section 5, rulings of 2026-11-04 and 2026-11-05): `FALSE` or
`JUST FALSE` where the text's own words say no ("means" in s 3; the "if" of s 175(4), s 179(7) and s 388(5)); `NOTHING`
where the provision does not speak (not deemed a worker; s 175(4) or s 179(5) not applying; a contribution date
outside the regulation's own period, where the answer is an amount; a Schedule 2 item other than 8, which this
encoding does not compute; no prescribed percentage). No `NOTHING-kind` tags are carried, so the rulings are cited,
not copied.

## Forks (for the reviewer to overrule)

- **F1** Sch 2 items 2-7 overlap (`the Schedule 2 items for`): all items whose class fits are returned in the
  Schedule's order; item 8 only when none fits. Other reading: one item governs (the most specific, or the first).
- **F2** "to whom no industrial award is applicable" in items 3 and 6 (`no industrial award applies to the worker in`):
  read of the worker, so an award in any of the jobs excludes items 3 and 6. Other reading: of the employment that
  meets the 38 hours. Asserted (case i: item 8 rather than item 3).
- **F3** Reg 12(4) "intervals of 3 months" (`Am I entitled to my weekly payments for this interval while overseas`):
  counted from the last submission, or from the start of overseas payments if there is none; a submission on the day
  3 calendar months later (month-end clamped) is in time. Other reading: a fixed 3-monthly calendar from the first
  proof, regardless of when each proof is given.
- **F4** Reg 14 "Until 31 December 2024": taken as including 31 December 2024, matching reg 15's "On and after 1 January
  2025". Keyed on the date of the determination.
- **F5** One hours input per job (above).
- **F6** Reg 13 "30 days after the day on which the Authority is notified": the day of notification is not counted, so
  notification on 10 March gives 9 April as the last day; reimbursement on that day attracts no interest.

## What the Regulations turn out to say

1. **35 hours for "full-time", 38 hours for Schedule 2.** Reg 8 sets 35 hours a week for a full-time worker where no
   award applies; reg 9 sets 38 hours for Sch 2 items 3, 5, 6 and 8. A worker with two jobs, no award, and 35 to 37
   hours in one of them is a full-time worker of that employer under s 3 but falls outside items 3 and 6, and so into
   item 8, where earnings are averaged per hour and capped at 38 hours. Asserted (reg 8 cases; case c).
2. **The Schedule 2 classes overlap** and the Schedule gives no order between items 2 to 7 (only item 8 is residual).
   Two jobs each at award hours, one of them 38 hours, fit items 2, 4 and 5; item 2 points to the one employer's work
   while items 4 and 5 point to the work with the higher earnings, which can differ. Asserted (case f). Fork F1.
3. **Clause 6(3) and clause 9(5)(c) treat a missing percentage differently.** Where reg 10's circumstances fail, a
   timber contractor's whole payment is remuneration ("less the applicable prescribed percentage (if any)"); where
   reg 11's fail, a contractor's payment is reduced by the part not attributable to labour (cl 9(5)(c)(ii)). Asserted.
4. **Two "prescribed rates" of interest are not in these Regulations.** s 179(7) makes the Authority liable for interest
   "at the prescribed rate" after reg 13's 30 days, and s 388(5) adds interest "at the prescribed rate" to an unpaid
   self-insurer contribution. The 2024 Regulations prescribe the period but no rate. Either the rate is prescribed
   elsewhere or it is missing; the encoding answers only whether interest is payable, not how much.
5. **Regulation 14's D(c) has no period.** D(a) and D(b) are costs "during the preceding quarter"; D(c), "the costs
   incurred by the Authority in meeting any liability incurred under section 403", has none. Regulation 15's matching
   A(c) says "during the preceding financial year", and its A(d) catches earlier years' costs not yet included. Read
   literally, reg 14's D(c) could bring in all s 403 costs in every quarter. Possibly a drafting gap; the encoding takes
   D(c) as a figure the Authority supplies.
6. **The letters swap between regulations 14 and 15.** In reg 14, B is the self-insurer's own remuneration and C the
   total; in reg 15, B is the total and C the self-insurer's own. The inputs are named for what they are, not only by
   letter.
7. **Regulation 15 sets an annual amount; s 388(3) sets four due dates.** Reg 15 has the contribution "determined ... at
   the start of each calendar year, as 25 per cent of" A/B x C. It does not say whether that 25 per cent is what falls
   due on each of the four s 388(3) dates (one quarter of a yearly share) or is the whole year's contribution. The
   encoding gives the determined amount and does not divide it among due dates.
8. **The last row of the Regulations' Schedule 2 holds three contracts** ("plumbers / wall and floor tilers / blind
   fitters | 25% / 25% / 25%"): a merged cell in the Word file. Read as three rows at 25 per cent each; check against
   the authorised PDF.
9. **Regulation 15 A(a)(ii)'s exclusions (A) to (D)** are printed at a shallower indent than (i) to (v) in the
   conversion. Read, as in reg 14, as exclusions from s 513(5)(d) costs only.

## Before relying on it

- Check the conversion against the authorised PDF, especially both Schedule 2 tables and the reg 14 and 15 formulas.
- Encode the 2013 Act (at least Part 5 Division 1, s 153, Sch 1 and Sch 2 in full) and point these questions at it.
- Find the prescribed rates of interest for s 179(7) and s 388(5) (finding 4).
- An independent test pass, and a lawyer's view of forks F1 to F3.
