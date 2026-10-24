# Workers Compensation Act 1987 (NSW), with the 1998 Act and the 2016 Regulation: baseline encoding

> **Warning.** All three texts encoded here are taken from the Open Australian Legal Corpus, collected on 10 March 2025.
> **They are not the current official text, and they may be out of date.** Check legislation.nsw.gov.au before relying
> on anything here. Every indexed dollar amount the texts state is older still; see *Figures*.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seats ruled on
2026-10-18 and 2026-10-21, with the recommended design defaults. Nothing was fetched: the encoding uses only what is
deposited. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The shape follows the seat-neutral core and seat layer pattern of
`subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/` and the ACT workers compensation baseline
(`subjects/au/act/workers-compensation-act-1951/encodings/baseline-2026-10/`):

- `nsw-wc-core.l4` is the **seat-neutral core**. It holds the rules in the Acts' own actors and terms ("the worker",
  "the employer", "the insurer", "the dependants", "the worker's legal personal representative"). Computations (the
  weekly payment, pre-injury average weekly earnings, the medical compensation period, lump sums, dates) are functions.
  Duties and deadlines are **12 regulative rules** (`DEONTIC`): 1998 Act s 44(2); s 44 (the worker's notice, then the
  employer's 48 hours); s 261; s 264(1); s 264(2); ss 267-269; s 274; ss 48 and 48A; s 49; 1987 Act s 38(4)(b) (a
  recursive 2-yearly duty); s 38(4)-(5); and Regulation cl 35(3). The acting party is a parameter, so the seats share
  one rule.
- `nsw-wc-seat.l4` is the **worker's seat layer** (25 questions, `@export` and `@desc` on every input). On the worker's
  death the dependants ask the questions in the group "If the worker has died".
- `nsw-wc-seat-insurer.l4` is the **insurer's seat layer** (9 questions), and `nsw-wc-seat-employer.l4` the
  **employer's** (8 questions). They call the same core, so the seats cannot disagree about the law. No two layers
  define the same name.
- Three case files, one per seat: `nsw-wc-cases-worker.l4`, `nsw-wc-cases-insurer.l4`, `nsw-wc-cases-employer.l4`. The
  insurer and employer files hold **mirror cases**: the same facts asked from the worker's seat, with answers that
  agree.

## Edition

| Text | Deposit | Corpus version |
|---|---|---|
| Workers Compensation Act 1987 No 70 | `../../registers/source-bundle/act-1987-070.txt` | `nsw_legislation:2023-10-30/act-1987-070` |
| Workplace Injury Management and Workers Compensation Act 1998 No 86 | `../../../workplace-injury-management-and-workers-compensation-act-1998/registers/source-bundle/act-1998-086.txt` | `nsw_legislation:2024-07-01/act-1998-086` |
| Workers Compensation Regulation 2016 | `../../../workers-compensation-regulation-2016/registers/source-bundle/sl-2016-0559.txt` | `nsw_legislation:2024-07-24/sl-2016-0559` |

All three are from the Open Australian Legal Corpus (version 7.1.0), as at 10 March 2025, by the owner's decision of
2026-10-20 (the official register returned a bot challenge). They are **not the current official text and may be out of
date**: amendments after those version dates, and every indexation order since, are missing. The corpus also dropped
the formulas, keeping only the words around them (see findings 1 and 2). Based on content from the New South Wales
Legislation website; attribution in `SOURCE-LICENSE.md`.

## Checks

Run with the stable `l4` of VS Code extension 1.6.98 (`l4.exe run <file>` from this folder), with `JL4_LIBRARY_PATH`
unset. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. On 2026-10-24:

| File | Errors | Warnings | Assertions written | Assertions satisfied |
|---|---|---|---|---|
| `nsw-wc-core.l4` | 0 | 0 | 0 | 0 |
| `nsw-wc-seat.l4` | 0 | 0 | 0 | 0 |
| `nsw-wc-seat-insurer.l4` | 0 | 0 | 0 | 0 |
| `nsw-wc-seat-employer.l4` | 0 | 0 | 0 | 0 |
| `nsw-wc-cases-worker.l4` | 0 | 0 | 184 | 184 |
| `nsw-wc-cases-insurer.l4` | 0 | 0 | 44 | 44 |
| `nsw-wc-cases-employer.l4` | 0 | 0 | 32 | 32 |

In all, 260 assertions are satisfied. There are also 22 `#TRACE`s with an `-- expect:` line: 16 breaches and 6
obligations or permissions still open. Each was read and was as expected. The stable `l4` cannot assert a breached or
pending trace, so those are traced, not asserted.

Every expected value was worked by hand from the deposited texts, with the arithmetic in a comment above the assertion,
and none was copied from the encoding's output. No scenario life raises these Acts, so every case is HYPOTHETICAL. The
s 66(2A) examples are reproduced on the arithmetic they show (finding 1).

## Seats

1. **The injured worker** (required), and on the worker's death **the dependants** (the lump sum, the weekly payment for
   a dependent child, funeral expenses). Typical questions: "How much is my weekly payment this week, and when does it
   step down or stop?", "Am I entitled after week 130? After 260 weeks? After pension age?", "How long will my medical
   expenses be paid?", "What lump sum is payable for my impairment?", "By what day must I claim, and is my claim in
   time?", "Has the insurer or my employer missed a deadline?", "What can the insurer do after its return to work
   notice?"
2. **The insurer** (a licensed insurer, the Nominal Insurer's agent, or a self-insurer). A private party, not an
   official, with hard deadlines: 7 days from the initial notification to start provisional weekly payments or give
   notice of a reasonable excuse (1998 Act ss 267, 268), 21 days to determine a claim for weekly payments (s 274, an
   offence under s 283), the 14-60 day window of a s 48A notice, the work capacity assessments of 1987 Act s 38(4), and
   the limit on accepting a late claim (s 261(5)). Questions: what must I do, by when, and what follows if I don't.
3. **The employer.** Duties with deadlines and penalties: notify the insurer within 48 hours of becoming aware of a
   workplace injury (s 44(2); Regulation cl 36), forward a claim within 7 days (s 264(1)), give requested information
   within 7 days (s 264(2)), provide suitable work at the worker's request (s 49), keep the notification records 5 years
   and produce them within 7 days of a request (Regulation cl 35(2), (3)).

No seat is given to an official. The judgments of the insurer (work capacity, the s 38 assessments, "satisfied that the
impairment is likely to be more than 20%"), of a medical assessor (the degree of impairment), of the Commission (special
circumstances, reasonable cause) and of the Authority (approval of a late acceptance, the declared indexed amounts) are
asked as facts, and the answers are conditional on them.

### Defaults (2026-10-18)

- **The Act alone, with the instruments that set its numbers or dates.** Followed: the 1998 Act (claims procedure,
  which the 1987 Act is construed with, s 2A) and the 2016 Regulation (the $155 PIAWE minimum, notification) are brought
  in. The SIRA indexation orders are not deposited: their amounts are inputs (see *Figures*).
- **The actors the text names.** Followed: the worker, the employer, the insurer (and self-insurer), the dependants, the
  legal personal representative.
- **A judgment handed to someone else is answered conditionally.** Followed (see *Seats*).
- **The Acts' own definitions worked out; borrowed terms asked.** Worked out: first and second entitlement periods,
  worker with high needs and with highest needs (s 32A), current weekly earnings (Sch 3 cl 8), secondary surgery
  (s 59A(7)), dependent child and student (s 25(5)), the retiring age date arithmetic (s 52). Asked: current work
  capacity and suitable employment (Sch 3 cl 9 and s 32A rest on assessment), the degree of
  permanent impairment (s 65), the age pension age (Social Security Act 1991 (Cth) s 23(5A)-(5D)), and the gross
  earnings and weeks of the relevant earning period (Regulation Part 4 Division 2 adjustments are not worked out).
- **One case is the text's natural unit.** Followed: one worker, one injury; weekly payments asked one week at a time.
- **The Acts' own terms, each with a plain gloss.** Followed; the gloss is in each `@desc`.
- **Operative sections in; machinery out.** Followed (see *Scope*).

**Departures.**
- Regulation Schedule 5 (penalty notice amounts) is outside the Regulation parts the brief named; it is quoted in the
  breach reasons and the "what follows" answers only, because it is what follows a missed deadline.
- 1998 Act s 264(2) (information within 7 days of the insurer's request), s 283 (the offence behind s 274), ss 275-276
  (provisional payments already running extend the s 274 time) and Regulation cl 35(2) (5-year records) were added
  beside the provisions the brief named, as the same duties' other halves.
- **Indexed amounts default to the deposited figure** (brief): each is a `MAYBE NUMBER` input, and leaving it empty
  uses the figure the deposited text states. The worker's seat thus departs from the guide's "use the Act's own
  figures" only in letting a known declared figure in.

## Figures

Every dollar amount of the 1987 Act used here is varied by an order of the State Insurance Regulatory Authority, and
**none of the orders is deposited**. Each is an input, with the deposited figure as the default and the provision named:

| Amount | Deposited figure | Varied under |
|---|---|---|
| Maximum weekly compensation amount (s 34(1)) | $1,838.70 | Division 6 (s 79(a), (a1) base index 240.5; s 80; order under s 82) |
| Earnings for continued payments after week 130 (s 38(3)(b)) | $155 a week | s 82B (order under s 82B(2)) |
| Floor for a worker with highest needs (s 38A(1)) | $788.32 | s 82BA (order under s 82BA(3)) |
| Lump sum death benefit (s 25(1)(a)) | $750,000 | Division 6 (s 79(a)); the amount "in force at the date of death" (s 25(4)) |
| Weekly payment for a dependent child (s 25(1)(b)) | $66.60 | Division 6 (s 79(a)) |
| Permanent impairment, s 66(2)(c)-(h) | $242,010; $309,020; $376,030; $443,030; $510,040; $577,050 | Division 6B (s 82E "variable amount"; order under s 82F(3)) |
| Pre-injury average weekly earnings (Sch 3 cl 2) | the worker's own | s 82A (factor declared under s 82A(4)), one review date at a time |

Not indexed by any deposited text, and used as stated: the PIAWE minimum of $155 (Regulation cl 8AB; s 82B varies "the
amount of $155 specified in sections 38, 40 and 41", not the Regulation's) and the funeral maximum of $15,000 (s 26; not
an adjustable amount under s 79, and the Regulation prescribes no other).

The cases use the deposited figures, which is to say they are worked as if no order had been made since the version
dates. They are HYPOTHETICAL and none of them is a 2026 amount.

## Scope

**In.**
- **1987 Act, weekly payments (Part 3 Division 2):** s 32A (first and second entitlement periods; worker with high needs
  and with highest needs; current work capacity and suitable employment as facts); s 33; s 34(1AA), (1); s 36; s 37;
  s 38(1)-(7); s 38A(1); s 39; s 52; Schedule 3 cl 2(1), (2), (4) with Regulation cl 8AB; Sch 3 cl 8; s 82A as a
  declared factor with s 82C(a).
- **1987 Act, medical:** s 59A (all of it).
- **1987 Act, death:** s 25(1), (2), (4), (5); s 26; s 29(1), (1A), (1B) (who receives the lump sum, not how it is
  apportioned).
- **1987 Act, permanent impairment:** s 66(1), (1A), (2)(c)-(h), (2A), (3); s 66(2)(a)-(b) as **not covered**.
- **1998 Act, duties and deadlines (regulative):** s 44(1), (2), (4); s 48; s 48A; s 49; s 254; s 261; s 264(1), (2),
  (4); ss 266-269; s 274(1)-(4) with ss 275(2), 276(1) and s 283(1).
- **Regulation:** cl 8AB; Part 8 cl 35(1)-(3) and cl 36 (cll 37-38 set no time and are not encoded); Schedule 5 in the
  consequences.

**Not covered** (an explicit value, asserted):
- the s 66(2)(a) and (b) amounts for more than 10% and not more than 50% (finding 1);
- injuries received before 21 October 2019 (Regulation Part 3 and the Schedule 6 transitional provisions), and deaths
  before that date;
- police officers, paramedics, firefighters and coal miners, to whom Schedule 6 does not apply the 2012, 2015 and 2018
  amendments (Pt 19H cll 25-26, Pt 19I cll 14-15, Pt 19L cll 4-5);
- PIAWE details under Regulation Part 4 Division 2 beyond the input of weeks in the relevant earning period, and
  anything resting on the Workers Compensation Guidelines (a reasonable excuse, the approved forms), which are inputs.

The scope gate is applied to the questions that compute an entitlement (weekly payment, medical period, permanent
impairment, death benefits). The definitional questions (high needs, entitlement periods, ss 38, 39, 52) and the 1998 Act
procedure questions are not gated: they answer as the deposited text reads.

**Out.** Work injury damages and common law (1987 Act Part 5; 1998 Act s 262); commutation (Division 9); s 60 medical
rates and approvals beyond the s 59A period; ss 64B-64C return to work assistance; s 40 (occasional variation after
week 130) and s 41 (surgery after week 130); s 53 (residence overseas); s 57 (notifying new employment); disputes,
reviews and the Personal Injury Commission (including s 78 dispute notices and Regulation cll 38-42B); premiums, costs
and insurer licensing; coal miners; injuries before 21 October 2019 under Regulation Part 3; injuries before 2012
(transitional).

## Links (cross-folder IMPORT is not possible)

- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/` (deposited, compilation C2004A04121). The
  s 52 retiring age is the age pension age of s 23(5A)-(5D) (verified in the deposit: 67 for a man born on or after
  1 January 1957, item 5 of the s 23(5A) table; (5B)-(5D) for women). The baseline encoding there
  (`encodings/baseline-2026-10/`) works pension age out; here it is an input date. That NSW weekly payments are
  "compensation" that can reduce or preclude a Centrelink payment under Part 3.14 (Compensation recovery, present in the
  deposit) is **unverified** (not read for this encoding).
- **Income Tax Assessment Act 1997 (Cth)**, `subjects/au/income-tax-assessment-act-1997/`: that weekly payments are
  assessable income is **unverified (from general knowledge, not from the texts)**.
- **Fair Work Act 2009 (Cth)**, `subjects/au/fair-work-act-2009/`: cited by the s 32A definition of "fair work
  instrument" (used by Schedule 3, not by the provisions encoded here).
- **NSW, cross-subject.** `subjects/au/nsw/victims-rights-and-support-regulation-2019/` cl 9 measures a victim's actual
  loss of earnings "at the rate of weekly payment of compensation payable under section 37 of the Workers Compensation
  Act 1987 (as in force immediately before its substitution by the Workers Compensation Legislation Amendment Act
  2012)". That pre-2012 s 37 is not in this deposit, so this encoding cannot supply it.
- **Motor accident weekly benefits** cannot be encoded beside this: `subjects/au/nsw/motor-accident-injuries-act-2017/`
  has no deposited text.

## Readings

- Dates (the Interpretation Act 1987 (NSW) is not deposited): "within N days after" a day ends N days later; "within N
  months after" ends on the same date N months later, or the month's last day; "a period of N years commencing on" a
  day includes it and ends the day before the same date N years later; a first anniversary of 29 February is
  28 February.
- s 52(2)(b): incapacity "more than 12 months after the first occasion" is from the day after the date 12 months on.
- A weekly payment worked out below nil is nil.
- s 66(3): the declared s 66(2) amount is that for the financial year in which the injury was received.
- s 274(3), ss 275-276: the end of a provisional period of w weeks is w weeks after the day it began; it only extends
  the 21 days. On the regulative clock the final determination is due within the weeks accepted, counted from the
  provisional acceptance.
- s 38(4): the last 52 weeks are 364 days; "at least once every 2 years" is 730 days on the rule's clock and the same
  date 2 years later in the date question.
- s 261 on the regulative clock: the late-claim rule starts at the first event after the 6 months, so the trace's
  3-year limit can run a day or so long; the date questions are exact.

## What the Acts turn out to say

1. **The s 66(2)(a) and (b) formulas are not in the deposit.** Paragraphs (a) (more than 10% to 30%) and (b) (more than
   30% to 50%) end "calculated as follows--", and only "where D is the number derived by expressing the degree of
   permanent impairment as D%" survives; the corpus dropped the formula images. The deposited s 66(2A) examples state
   that 12% gives $25,420 and 50% gives $175,000, but two points do not supply a formula, and none was reverse-engineered.
   The encoding answers `not covered` for 11% to 50%, asserted at 11%, 12%, 30% and 50%; the s 66(2A) arithmetic of both
   examples is asserted on their stated amounts ($26,691; $180,833.33).
2. **The indexation formulas are missing too.** s 80(1), s 82A(1), s 82B(1), s 82BA(1) and s 82F(1) each end "as follows"
   or "the formula--" with nothing after; the "where" clauses for A, B and C survive. Every indexed amount is therefore
   an input (the declared figure), never recomputed from index numbers.
3. **Every dollar figure in the deposit is out of date, and no order is deposited.** The 1987 Act text is the version of
   30 October 2023, and the declared amounts change each 1 April, 1 October or 1 July. The s 66(2)(c)-(h) amounts read as
   fixed sums, but s 82E makes each a "variable amount" indexed yearly under s 82F, so they are inputs with the stated
   figure as the default like the rest.
4. **The Division 6 list of adjustable amounts is stale.** s 79 names "the amounts specified in sections 25, 34, 37 and
   40": s 37 now states no dollar amount at all, and the $155 in s 40 is also varied by s 82B, while the same $155 in
   s 38(3)(b) is varied only by s 82B. On its face the s 40 figure has two indexation regimes.
5. **A pending assessment makes a worker one "with highest needs", with no threshold.** Paragraph (b) of both s 32A
   definitions is identical (an assessment "pending" because maximum medical improvement is not reached), so such a
   worker gets the s 38A floor and the s 59A(5) exemption whatever the likely degree. Asserted.
6. **s 38A lifts even a nil payment.** For a worker with highest needs, any amount the Subdivision works out below
   $788.32 "is to be treated as $788.32", including a nil amount where current weekly earnings exceed the share of
   pre-injury earnings the section pays. Asserted (case W8 (n)).
7. **The s 38 application has an earliest day but no latest.** s 38(3)(a) and (3A) require an application "no earlier
   than 52 weeks before the end of the second entitlement period" and say nothing of how late it may be. Asserted (an
   application with 0 weeks left counts).
8. **"Deductible amount" is undefined.** s 38(3)(b) (and ss 40, 41) count "current weekly earnings (or current weekly
   earnings together with a deductible amount)"; no deposited text defines the term.
   It is asked as part of the earnings figure.
9. **s 39 and s 59A draw the 20% line differently.** s 39(2) needs an assessed degree "more than 20%", while s 59A(5)
   exempts a "worker with high needs", which also counts a pending assessment and the insurer's view. A worker can have
   medical expenses without a time limit while weekly payments stop at 260 weeks. Asserted (cases W3, W7, W9).
10. **s 25(2)(b) and s 25(1)(b)(i) can disagree.** Read alone, s 25(2)(b) ends the weekly payment for a child who was a
    student at the worker's death once the child "ceases to be a student", even at 14; s 25(1)(b)(i) gives it to "each
    dependent child ... under the age of 16". The encoding follows (1)(b)(i) for every child under 16.
11. **Two Regulation figures are not indexed by any deposited text:** the cl 8AB PIAWE minimum of $155 (s 82B varies
    only the $155 "specified in sections 38, 40 and 41") and the s 26 funeral maximum of $15,000 (not a s 79 adjustable
    amount; the Regulation prescribes no other). Both are used as stated.
12. **Indexation rounding and the no-reduction rule are only partly encodable.** ss 82D and 82H are permissive (an
    amount "is deemed to have been calculated in accordance with this section if" rounded to $1 or $10), so no rounding
    is applied; s 82C(b) (a later increase counts only beyond an earlier reduction not yet set off) needs the history of
    factors, and only s 82C(a) is applied, one review date at a time.
13. **Two duties set no time at all.** The worker must notify the employer "as soon as possible" (1998 Act s 44(1)), and
    the insurer must give the s 269 notice "as soon as practicable"; the employer's s 49 duty to provide suitable work has
    no time either. These never fall due by time alone. Traced as open obligations.
14. **Only some of the deadlines carry a penalty notice.** Regulation Schedule 5 lists ss 264(1)-(3), 267(5), 268,
    283(1) and cl 36, but not s 49 or cl 35, which can only be prosecuted (50 and 20 penalty units). Asserted.
15. **s 38(5) displaces s 38(4) for a worker with highest needs.** The insurer "must ... ensure" an assessment in the
    last 52 weeks and every 2 years, yet "is not to conduct" one of a worker with highest needs unless it thinks it
    appropriate and the worker asks. The rule makes s 38(4) apply only to other workers. Traced.

## Before relying on it

- Replace the three corpus texts with the current official ones from legislation.nsw.gov.au, and re-check every
  provision against them.
- Deposit the SIRA indexation orders (ss 82, 82A(4), 82B(2), 82BA(3), 82F(3)) for the periods wanted, and the s 66(2)(a)
  and (b) formulas from an authorised rendering as a `act-1987-070.formulas.md` sidecar; then encode the 11-50% bands.
- Deposit the Workers Compensation Guidelines if the reasonable-excuse, claim-form and work capacity questions are to be
  worked out rather than asked.
- Run an independent test pass and the human gates.
