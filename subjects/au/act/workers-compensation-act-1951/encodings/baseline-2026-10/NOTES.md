# Workers Compensation Act 1951 (ACT): baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seats ruled on
2026-10-18 and 2026-10-21, with the recommended design defaults. Nothing was fetched: the encoding uses only what is
deposited. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The shape follows the seat-neutral core and seat layer pattern of `subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/`:

- `wca-core.l4` is the **seat-neutral core**. It holds the Act's rules in the Act's own actors and terms ("the worker",
  "the employer", "the insurer", "the dependants", "the personal representative"). Computations (weekly compensation,
  lump sums, death benefits, indexation, dates) are functions. Duties and deadlines are **9 regulative rules**
  (`DEONTIC`): ss 93(1) and 38(1), s 38(2)-(3), ss 93(2) and 94(3), s 126(1), s 119, s 128, ss 130-132 and 134, s 120,
  and s 121. The party who acts is a parameter of each rule, so the seats share one rule.
- `wca-seat.l4` is the **worker's seat layer**. It asks 18 questions with `@export`, and puts `@desc` on every input. It
  builds the core's records from plain answers and restates no rule.
- `wca-seat-employer.l4` is the **employer's seat layer** (5 questions), and `wca-seat-insurer.l4` the **insurer's**
  (5 questions). They draw on the same core, so the seats cannot disagree about the law. No two layers define the same
  name.
- There are three case files, one per seat: `wca-cases-worker.l4`, `wca-cases-employer.l4` and `wca-cases-insurer.l4`.
  The employer and insurer files hold **mirror cases**: the same facts asked from the worker's seat, with answers that
  agree.

## Edition

- Workers Compensation Act 1951 (A1951-2), **Republication No 88 (R88), effective 26 November 2025**, last amended by
  A2025-30. This was the current version on the ACT Legislation Register on 2026-10-20. It is deposited at
  `../../registers/source-bundle/A1951-2.txt`, converted from the register's DOCX, which the register marks
  "unauthorised"; the authorised text is the PDF.
- The formulas the DOCX held only as images (ch 3 note 1, s 179A(2), s 185(3)(a)) fall outside this encoding's scope.
- **Not deposited:** the Workers Compensation Regulation 2002 (SL2002-20), and any notice of the indexed amounts.

## Checks

Run with the stable `l4` of VS Code extension 1.6.98 (`l4.exe run <file>` from this folder), with `JL4_LIBRARY_PATH`
unset. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. On 2026-10-24:

| File | Errors | Warnings | Assertions written | Assertions satisfied |
|---|---|---|---|---|
| `wca-core.l4` | 0 | 0 | 0 | 0 |
| `wca-seat.l4` | 0 | 0 | 0 | 0 |
| `wca-seat-employer.l4` | 0 | 0 | 0 | 0 |
| `wca-seat-insurer.l4` | 0 | 0 | 0 | 0 |
| `wca-cases-worker.l4` | 0 | 0 | 147 | 147 |
| `wca-cases-employer.l4` | 0 | 0 | 29 | 29 |
| `wca-cases-insurer.l4` | 0 | 0 | 33 | 33 |

In all, 209 assertions are satisfied. There are also 15 `#TRACE`s with an `-- expect:` line: 9 breaches and 6
obligations or permissions still open. Each was read and was as expected. The stable `l4` cannot assert a breached or
pending trace, so those are traced, not asserted.

Every expected value was worked out by hand from the deposited text, with the arithmetic in a comment above the
assertion, and none was copied from the encoding's output. No scenario life raises this Act, so all the cases are
HYPOTHETICAL. The Act's own examples are reproduced: Jim (s 41), Bronwyn and Nicholas (s 42), the s 20 indexing
example, and the s 61 deduction example.

## Seats

1. **The injured worker** (required). This is the private-sector worker the Act compensates. On the worker's death the
   seat passes to **the dependants, or the personal representative** (the section headed "If the worker dies").
   Typical questions: "How much weekly compensation am I paid?", "When does it stop because of my age?", "What lump
   sum do I get, and when can I claim it?", "What do my dependants get if I die?", "By what day must I claim?", "Is my
   claim taken to be accepted?", "How soon after a rejection can my payments stop?"
2. **The employer.** The Act puts real duties on the employer, each with a deadline and a consequence: begin weekly
   payments when the worker gives notice (s 38(1), an offence under s 38(4)); give the insurer an injury notice within
   48 hours (s 93(2)), with the s 95 cost if it is late; confirm an oral notice within 3 days (s 94(3)); and forward
   the claim within 7 days (s 126(1), an offence).
3. **The insurer.** This is the licensed insurer, or the employer as a licensed self-insurer (s 127(1)). It is a
   private party, not an official, and the Act gives it hard deadlines with consequences: 72 hours for the medical
   certificate (s 119), 28 days before acceptance by silence (s 128), 2 or 8 weeks of further payments after a
   rejection (ss 130-131), the Magistrates Court's leave after 1 year (s 132), and liability until it rejects or
   settles (s 134).

No seat is given to an official. The Magistrates Court's and the regulator's judgments appear as facts the person
states: "the Magistrates Court allowed an earlier claim", "the court's order states a day".

### Defaults (2026-10-18)

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows. The
  instruments that set the numbers are not deposited (see *Figures*), so their numbers are inputs.
- **The actors the text names.** Followed: the worker, the employer, the insurer and licensed self-insurer, the
  dependants, the personal representative, the Magistrates Court.
- **A judgment handed to someone else is answered conditionally.** Followed. These are all asked as facts: whether the
  worker is totally or partially incapacitated (ss 6, 7, 35); the assessed loss and its proportion (s 51(2), s 59(3));
  the deductible proportion (s 61); stabilisation under s 121(5); "as soon as practicable" (s 120(1)(a)); and the
  court's leave or order (ss 120A, 121(3), 132).
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed. Worked out: dependant, child and
  full-time student (dictionary), relevant percentage, statutory ceiling, pre-incapacity floor, initial incapacity
  date, cpi indexed and wpi indexed. Asked: pension age (Social Security Act 1991 (Cwlth) s 23), the statutory floor
  (the Fair Work Act 2009 (Cwlth) national minimum wage), AWE, and average pre-incapacity weekly earnings and hours
  (ss 21-26, which leave the method open).
- **One case is the text's natural unit.** Followed: one worker, one injury, one claim. Weekly compensation is asked
  one week at a time.
- **The Act's own terms, each with a plain gloss.** Followed. The gloss is in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see *Scope*).

**Departure.** s 126(1), the employer's duty to forward a claim within 7 days, was not in the task's list. It was
added because it is the employer's other hard deadline in pt 6.1, and the employer's seat would be incomplete without
it.

## Figures

None of the indexed amounts current in October 2026 is deposited, because no Workers Compensation Regulation 2002 and
no indexation notice is deposited. So every question takes these as **inputs**: the indexed single loss amount,
maximum loss amount, death lump sum, weekly payment for a dependent child and funeral maximum; AWE; the statutory
floor (and the pre-incapacity floor); and, for the indexing question, the index numbers.

The Act's base figures **are** encoded: $100 000 (s 49), $150 000 (s 50), $539 002.37, $148.23 and $11 828.87 (s 77).
So are the index arithmetic of s 20 and s 77(7) and the commencement dates the endnotes give: ss 49-50 from 1 July
2002 (A2001-81), and s 77 as amended by A2017-49 from 13 December 2017.

The hand-worked cases use the base figures, which is an index factor of 1, and illustrative floors and AWE. These are
labelled HYPOTHETICAL. None of them is the current figure.

## Scope

**In.**
- **pt 4.1:** s 20; ss 21-26 (as inputs).
- **pt 4.3, weekly compensation:** s 36G; s 37; s 38; ss 39-42 (the 26 weeks, the s 41 floor comparisons, the s 42
  relevant percentages and ceiling); ss 43, 43A, 43B (through the week's facts); ss 44-45; s 83 (as one fact, because
  s 43B counts it).
- **pt 4.4, permanent injuries:** ss 48-51, 53-57, 59 and 61, and all 54 items of Schedule 1.
- **pt 4.6, death:** s 77, with the dictionary's dependant, child and full-time student, and the s 78 payment into
  court.
- **Notice:** s 93; s 94(2)-(3); s 95.
- **ch 6, claims:** s 116(2); s 118(2); s 119; s 120(1)-(2); s 121; s 122; s 126(1); s 127; ss 128-132; s 134(1)-(4).

**Out, each answering `not covered` where a question could reach it.** A claim for an imminently fatal asbestos-related
disease answers `not covered` (asserted); an item outside 1-54 answers `not covered` (asserted).
- Who is a worker (ch 3): a fact.
- The employment connection with the ACT (pt 4.2A).
- Medical and other costs (pt 4.5), beyond the s 130/131 references.
- Hearing loss (ss 63-66); s 58 (bowel); s 62 (further loss); s 68 (death within 3 months).
- Vocational rehabilitation and injury management (ch 5 other than ss 93-95, and ch 7).
- Insurance licensing and the DI fund (ch 8). Terrorism (pt 8.3).
- Common law damages (ch 9).
- Registered agreements (pt 4.7); commutation and settlement (s 137); refunds after an offence (s 135).
- The exceptions in s 82 and s 84, which are facts behind "compensation is payable".
- Comcare, which covers ACT public servants, is Commonwealth law (Safety, Rehabilitation and Compensation Act 1988).

## Commonwealth links

Cross-folder `IMPORT` does not work, so these are links, not code.

- **Social Security Act 1991** (`subjects/au/social-security-act-1991/`; the baseline's `ssa-claims.l4` uses pension
  age). Its s 23(5A)-(5D) pension age is the input that ends weekly compensation under s 39(3) and s 40(4). Its pt 3.14
  (compensation preclusion and recovery) decides how this Act's weekly payments and lump sums reduce or preclude a
  Commonwealth payment.
- **Fair Work Act 2009** (`subjects/au/fair-work-act-2009/`). The national minimum wage set in the annual wage review
  is the statutory floor (s 36G). Its s 130 bars taking or accruing leave while on workers' compensation unless a
  compensation law allows it, and s 46(1) of this Act does allow it.
- **Income Tax Assessment Act 1997** (`subjects/au/income-tax-assessment-act-1997/`). Weekly compensation replaces
  income and is assessable as ordinary income.
- **A New Tax System (Family Assistance) Act 1999** (`subjects/au/a-new-tax-system-family-assistance-act-1999/`).
  Family tax benefit is left out when deciding whether a child was dependent on the worker (s 77(3)).
- **Motor Accident Injuries Act 2019 (ACT)** (`subjects/au/act/motor-accident-injuries-act-2019/`, not yet encoded).
  Its s 98 reduces income replacement benefits for a person receiving workers compensation.

## What the Act turns out to say

1. **s 41(1) says nothing where the earnings equal the floor.** Paragraph (a) needs the earnings to be *less* than the
   pre-incapacity floor, (b) needs them *more* while 65% of them is *less*, and (c) needs 65% of them *more*. So there
   are two gaps. The first is where the earnings equal the floor, which is exactly a worker on the national minimum
   wage. The second is where 65% of the earnings equals the floor. Both are encoded as `not covered`. Asserted.
2. **s 41 compares with one floor and pays another.** The comparisons use the pre-incapacity floor, which is the
   statutory floor immediately before the initial incapacity date. But paragraphs (b) and (c) pay the statutory floor
   at the time of payment. So once the floor rises, a worker under (b) is paid more than they earned before the
   injury: $1,300 against $1,200. s 42 compares with the current floor throughout. Asserted.
3. **s 42(1)(a) and (b) overlap, and "difference" needs a floor.** Whenever (a) applies, (b) does too. The encoding
   takes the paragraphs in order, so (a) wins. In s 39(4)(b) and s 42(1) the "difference" is read as never below nil
   where the worker earns more than the reference amount. Asserted.
4. **A claim on the 8th day loses nothing.** s 38(2) ends payment at the end of 7 days after the injury. But the
   period with no entitlement runs from "the day 8 days after the date of the injury" to "the day before the day the
   worker makes a claim", and for a claim on that 8th day the period is empty. On the other hand, a worker whom the
   injury prevented from claiming, but who then claims more than 7 days after becoming able, loses the whole period
   from day 8, including the days the injury prevented a claim. Asserted.
5. **Schedule 1 has 54 items, not 44.** The task description said 44 items. The deposited Schedule runs from item 1
   (speech) to item 54 (silicosis), and all 54 are encoded. Item 53 (imminently fatal asbestos-related disease) is in
   the table, but the claims path for that disease is out of scope. Asserted (items 9, 11, 12, 14, 33, 41, 46, and 99
   not covered).
6. **s 56 points at items that do not exist.** It treats an only arm, leg, hand or foot as "the loss of both arms,
   legs, hands or feet", but Schedule 1 has no item for both of anything. The encoding reads it as the two items added
   together. For an only arm at or above the elbow that is 80 + 75 = 155%, which s 53 caps at the maximum loss amount
   ($150 000 against 155% of $100 000). Asserted.
7. **s 57 caps itself at the item's figure.** Penis (47%) and one testicle (10%) come to 57%, which is capped at 47%.
   Loss of a sexual organ other than these takes item 41's 47%. Asserted.
8. **The no-negative rule does not reach wpi indexed amounts.** s 20(2)-(4) protect only an amount "to be awe indexed
   or cpi indexed". The death lump sum and the child payment are wpi indexed, a term s 77(7) defines without any
   protection, so read literally they fall with the Wage Price Index. A 2% fall takes the lump sum to $528 222.32.
   Asserted.
9. **s 20 is a ratchet on the highest index.** The effect of s 20(2)-(4) is that a cpi indexed amount is the Act's
   figure times the highest CPI ratio since commencement, and never less than the figure. The Act's own example
   (100, then 120, 108 and 129.60) comes out on this reading. Asserted.
10. **The boundaries of ss 130-132 overlap.** A rejection on the 28th day is both "within 28 days" (s 130: 2 weeks)
    and "28 days or later" (s 131, and s 129(5): 8 weeks). One on the first anniversary is both "not later than 1
    year" (s 131) and "1 year or later" (s 132, which needs leave). The encoding applies the earlier section at each
    boundary; s 128's "at the end of 28 days" supports this at 28. Asserted (day 28 gives 2 weeks; exactly 1 year gives
    8 weeks without leave).
11. **Deciding and rejecting are different days.** s 128 turns on whether the insurer has "decided to reject" by day
    28. But under s 129(2) a rejection takes effect only when the notice is received. So an insurer that decides on
    day 27, with the notice arriving on day 30, avoids acceptance by silence while its rejection counts as one "28
    days or later" (8 weeks). Also, s 128 counts from the day the insurer "receives" the claim, and ss 130-131 from
    the day it "is given" it (s 127(2)). One date stands for both. Asserted.
12. **Acceptance by silence is not final.** After the 28 days the insurer can still reject under s 131 up to 1 year,
    and under s 132 later with leave. What it paid is not recoverable (s 128(2)(b), s 134(2)), except the s 95 amount,
    which is recoverable from the employer (s 134(3)). Asserted.
13. **A flagged certificate moves the claim day.** Under s 119(2), if the insurer flags a deficient certificate
    within 72 hours, the claim "is not considered to have been made" until the certificate complies. If the s 38(2)
    seven days and the s 120 three years read "claim" the same way, they move with it. Asserted for the claim day.
14. **The 48-hour notice has no penalty of its own.** s 93(2) carries no penalty. Its sanction is s 95: the employer
    pays weekly compensation itself, from the date of injury to the notice, without indemnity. By contrast, s 38(4) and
    s 126(1) are strict liability offences (10 and 50 penalty units). Asserted for s 95 and the s 134(3) mirror; the
    breaches are traced.
15. **The worker's notice duty bites through s 120.** s 93(1) ("as soon as possible") sets no day and no sanction, so
    as a regulative rule it never falls due by time alone (traced). Its consequence is in s 120(1)(a): notice as soon
    as practicable, and before the worker voluntarily leaves the job, or the proceeding needs the court (s 120A) or
    s 124. Asserted.
16. **The age limit turns on one question.** s 39(3)(c) and (d), and s 40(4)(b) and (c), give the same result. The
    only line is whether pension age is more than 2 years after the initial incapacity date. If it is, payments stop
    at pension age; if not, 2 years after that date. Read with these choices: the day pension age is reached is
    excluded; the second anniversary is included; and an anniversary of 29 February falls on 28 February. Asserted.
17. **The weekly death payment is for the worker's own children.** It goes to "each dependant who is a child", and
    the dictionary defines "child, of a worker" as the worker's child under 16, or a full-time student aged 16 to 24,
    not in a domestic partnership. So a dependent grandchild shares the lump sum but gets no weekly payment, and the
    payment stops at 16 or 25 (s 77(5)). Asserted.
18. **"When" means the same day.** s 38(1)(a) says payments "must begin when the worker gives notice of the injury",
    and gives no period. It is encoded as the same day. Traced.

## What would need doing before this is worth relying on

- The current indexed amounts, AWE and statutory floor. That means depositing the Workers Compensation Regulation
  2002 and the indexation notices (or the published figures) and replacing the inputs with dated tables.
- The ss 21-26 methods for average pre-incapacity weekly earnings and hours, including overtime, two employers,
  contractors and gradual onset.
- The parts left out: pt 4.5 costs, hearing loss (ss 63-66), s 68, the s 82 and s 84 exceptions, settlements (s 137),
  and the imminently fatal asbestos path (ss 116(2)(a), 121(2)(a), 128A, DI fund).
- The transitional provisions for injuries before 1 July 2017, when A2017-49 introduced the pension-age limits. These
  were not read.
- ACT case law on the s 41 equality gap, the s 56 reading and the boundary days in ss 130-132. None was searched.
- An independent test pass and a human gate.
