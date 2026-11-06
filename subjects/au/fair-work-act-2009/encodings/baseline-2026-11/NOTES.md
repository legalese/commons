# Fair Work Act 2009 — baseline-2026-11: underpayment, sham arrangements, the general protections, unfair dismissal remedies, bullying and sexual harassment

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. Checked with the
stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

**A layer beside `baseline-2026-10` and `naive-2026-10`, not a replacement.** Those encodings cover the NES, who is an
employee, unfair dismissal eligibility (ss 382-389, 394), small claims and the six-year limit (ss 544, 545(5), 548),
records and pay slips. They left out the general protections, sham contracting, civil penalties, and stop bullying and
sexual harassment orders. This encoding adds the provisions a person bringing a claim about pay, dismissal, bullying or
harassment meets there. Neither earlier encoding was changed. The stable `l4` resolves IMPORT only within a folder, so
this encoding cannot call the earlier ones; where a question needs an answer they give (am I protected from unfair
dismissal; is my employer a small business employer), it is asked here as an input.

Five modules. `fwa2-common.l4` holds the day counting and the penalty unit, and is the only one that imports `daydate`.
The four question modules import it:

| Module | Covers |
|---|---|
| `fwa2-pay.l4` | s 62 (maximum weekly hours), s 323 (paid in full, in money, at least monthly; the duty as a regulative rule), ss 324, 326 (deductions), s 325 (being made to spend or pay), ss 327A(7), 546A(2) (the underpayment), s 327A with Sch 1 cl 98 (the wage theft offence and its penalties), s 545A (casual loading set off) |
| `fwa2-protections.l4` | ss 340, 341, 342 items 1-4 with (2)-(4), 351, 352 with reg 3.01, 357, 358, 359, 359B, 359C, 360, 361, 365, 366, 369(1)(c), 370, 372 |
| `fwa2-orders.l4` | ss 390, 391(1)-(4), 392(3)-(6) with reg 3.06; ss 789FC, 789FD, 789FE(1), 789FF; ss 527D, 527E(1)-(2), 527F, 527G, 527J(1)-(2), 527S(1)(e), 527T |
| `fwa2-remedies.l4` | s 539(2) items 1, 2, 10, 11, 11A, 11B, 27A, 27B, 38 with the s 12 "selected civil remedy provision"; s 546(2), (2A), (2AA) (for an individual, a body corporate, and a person involved under s 550 that is either); s 546A(1); ss 557A(1), (2), (5A), 557B(1); s 550; ss 558A, 558B(1)-(3), (7); s 547; s 570 |

Every question is published with `@export` and a description, and every input carries an `@desc` worded from the seat.
Situations a person may not be in (dismissal, bullying, sexual harassment) are marked in the `§` headings.

## Edition

- **The Act:** Fair Work Act 2009, Compilation No. 73, compilation date 7 July 2026 (includes amendments up to Act
  No. 62, 2026; register id C2026C00355), as deposited at `../../registers/source-bundle/C2009A00028.txt`.
- **The Regulations:** Fair Work Regulations 2009 (F2009L02356), Compilation No. 57, compilation date 1 October 2026
  (register id F2026C00996), as deposited at
  `../../../fair-work-regulations-2009/registers/source-bundle/F2009L02356.txt`: reg 3.01 (illness or injury
  prescribed for s 352) and reg 3.06 (leave without pay in the s 392(6) cap). Regs 3.02, 3.03 (fees) read, not encoded.
- **The penalty unit:** Crimes Act 1914 s 4AA (register id C2026C00368), deposited at
  `../../../crimes-act-1914/registers/source-bundle/`, and the Crimes (Amount of a Penalty Unit) Instrument 2026
  (F2026N00424), deposited at `../../../crimes-amount-of-a-penalty-unit-instrument-2026/registers/source-bundle/`:
  $364 from 1 July 2026.
- **Not deposited, so inputs:** modern awards and enterprise agreements (overtime rates, ordinary hours, due days,
  specified payment methods), the high income threshold figure (its indexation is encoded in `baseline-2026-10`), the
  Sex Discrimination Act s 28A meaning of "sexually harass", the WHS Act meaning of "worker", the anti-discrimination
  laws s 351(3) lists, the Acts Interpretation Act 1901 (for counting days).

## Checks

With the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset (7 November 2026):

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `fwa2-pay-cases.l4` | 61 | 61 | 0 | 0 |
| `fwa2-protections-cases.l4` | 55 | 55 | 0 | 0 |
| `fwa2-orders-cases.l4` | 57 | 57 | 0 | 0 |
| `fwa2-remedies-cases.l4` | 47 | 47 | 0 | 0 |
| **Total** | **220** | **220** | 0 | 0 |

`l4 run` on each module (`fwa2-common.l4`, `fwa2-pay.l4`, `fwa2-protections.l4`, `fwa2-orders.l4`,
`fwa2-remedies.l4`) gives no errors or warnings, and a file importing all four question modules together checks clean,
so no name is defined twice. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A negative
control (three expected values altered in a copy of `fwa2-orders-cases.l4`) gave three "assertion failed". Every
expected value was worked by hand from the text, with the edges: exactly 38 hours, the due day and the day after, one
calendar month between pay days, the 21st and 22nd day, the 14th and 15th day after a certificate, 3 months' absence,
the compensation cap a dollar either side, the 24-month anniversary, an individual and a company each involved under
s 550, the underpayment multiple a dollar either side of
the penalty-unit maximum, the penalty unit's indexation day.

## Seat

**The individual bringing or weighing the claim:** the employee who has worked long hours, been underpaid or had
money taken from their pay; the job applicant, employee or contractor something was done to; the dismissed employee;
the worker who is bullied; the person sexually harassed in connection with work. The questions are theirs: "Can I
refuse these hours?", "Was I paid in full by the due day?", "Was that deduction allowed?", "Is it wage theft?", "Was
what they did adverse action, and was it unlawful?", "Was I misled into being a contractor?", "By when must I apply,
and when can I go to court?", "What is the most compensation I can get?", "Have I been bullied at work?", "Is the
business liable for the harasser?", "What is the most penalty the court can order?", "Can I sue the manager, the
franchisor or the parent company too?", "Can I be made to pay costs?"

The provisions speak mostly to the employer ("must not"), to the FWC ("may order", "must start to deal with") or to the
court ("may make", "must not be more than"). Each is encoded as what it means for the claimant. No seat for the
employer, the FWC, the Ombudsman or the court here (`baseline-2026-10` has an employer seat for day one).

Each 2026-10-18 default:

- **The Act alone, with the instruments that set its numbers:** the Regulations (regs 3.01, 3.06) and the penalty unit
  instrument are brought in. Awards and agreements are not deposited, so their rates and dates are inputs.
- **The text's own actors:** the employer, the principal, the person involved, the franchisor, the holding company,
  the FWC, the court.
- **Judgments answered conditionally, as inputs:** whether additional hours are reasonable (s 62(3)); whether a
  requirement or deduction is unreasonable (ss 325, 326); whether the employer proves a reason was not among its
  reasons (s 361), a reasonable belief (s 357(2)) or all reasonable steps (ss 527E(2), 558B(3)); the FWC's findings
  (unfair dismissal, reinstatement inappropriate, bullied, risk of continuing, exceptional circumstances); intention
  for s 327A; good cause against interest; the s 570 findings.
- **The Act's own definitions in L4:** workplace right (s 341), adverse action (s 342 items 1-4), prescribed illness or
  injury (reg 3.01), bullied at work and constitutionally-covered business (s 789FD), serious contravention (s 557A),
  involved in a contravention (s 550), franchisee and responsible franchisor entity (s 558A), selected civil remedy
  provision (s 12), underpayment amount (ss 327A(7), 546A(2)). **Borrowed terms as inputs:** "sexually harass" (Sex
  Discrimination Act s 28A), "worker" (WHS Act), "employee" in its ordinary meaning (s 15AA), constitutional
  corporation, unlawful under an anti-discrimination law.
- **One case:** one employment, one pay period, one dismissal, one application, one contravention.
- **The Act's terms with plain glosses** in the comments and `@desc`s.
- **Operative sections in, machinery out:** application fees, the FWC's procedure, the defence and security
  declarations, ss 727-734 (one claim only).

## In scope and out

In: the provisions in the table above.

Out, and why:

- **The industrial activity protections, coercion, undue influence, misrepresentation of workplace rights (ss 343-350B,
  353-356, 362-364)** and s 342 items 3A, 4A and 5-8 (platform operators, industrial associations, action against an
  employer): the claims in focus are an individual's against an employer or principal; these are for a further layer.
- **Application fees** (ss 367, 373, 395, 527H, 789FC(3)-(4), regs 3.02, 3.03): indexed each year by a CPI formula
  whose index numbers are not deposited.
- **Arbitration outcomes and procedure** (ss 368, 369(2)-(3), 527R, 527S(2)-(3)): how the FWC conducts a conference and
  what it may order once both sides have agreed to arbitration. The orders are open discretions with no test, cap or
  formula for the claimant to meet (s 369(2) lists reinstatement, compensation, lost pay and continuity; s 527S(3)
  compensation, lost pay, any reasonable act, and opinions); the steps that are the claimant's (the certificate, the
  14 and 60 days to agree, the court deadlines) are in.
- **Defence and security** (ss 527J(4), 789FE(2), 527M-527Q, 789FI-789FL): declarations by the Chief of the Defence
  Force and the security agencies, which a claimant cannot know or test; the one rule a defence member meets
  (s 527F(3)) is in, as a fork.
- **ss 527L, 789FH** (actions under work health and safety laws still allowed) and **s 527CA** (State and Territory
  laws run concurrently): they preserve claims under other laws and add no test under this Act.
- **ss 727-734A** (one claim only; the bar on court after agreeing to arbitration): where the question turns on them,
  the answer is `NOTHING`.
- **The other s 539 items:** civil remedy provisions about bargaining, industrial action, right of entry, unions and
  other subjects outside an individual's pay, dismissal, bullying or harassment claim.
- **s 545(1)-(2)** (the Federal Court's and the Federal Circuit and Family Court's orders: injunctions, compensation,
  reinstatement): the court "may make any order the court considers appropriate" once it is satisfied of a
  contravention, with no further test, cap or formula; whether there was a contravention is what the questions here
  answer, and the amount is the court's. s 545(3) (the State courts' power to order unpaid amounts) and the six-year
  limit in s 545(5) are in `baseline-2026-10`.
- **s 548** (small claims, $100,000 with reg 4.01): in `baseline-2026-10`.
- **ss 549, 551-556** (a civil remedy provision is not an offence; civil rules of evidence; civil and criminal
  proceedings and double jeopardy): rules about how the case is run and how it stands against a prosecution, not
  tests the claimant meets.
- **s 558** (regulations for infringement notices) and **s 558C** (a franchisor or holding company's right to recover
  from the employer what it paid): the first is the Ombudsman's tool, the second is between the companies, not the
  claimant's.
- **ss 569, 569A** (Commonwealth and State Ministers may intervene) and **s 571** (no imprisonment for failing to pay
  a penalty): no question for the claimant turns on them.
- **s 388** (the Small Business Fair Dismissal Code): it decides whether a dismissal was unfair (s 385(c)), which
  `baseline-2026-10` asks as an input; the Code is a legislative instrument made by the Minister, not deposited.
  Here the FWC's finding of unfair dismissal is an input, and its `@desc` says it excludes a dismissal consistent with
  the Code.
- **s 391(4)** (what the FWC must take into account in fixing lost pay): "take into account", not "deduct", and no
  cap, so the amount is the FWC's and no figure is computed; s 391(2) and (3) themselves are in.
- **Junior doctors' overtime rates:** in the awards and enterprise agreements (none deposited). The Act gives the s 62
  limit, the s 323 duty to pay overtime in full (note 2), recovery and penalties; the hourly rate is an input.
- **s 327B** (the voluntary small business code): a limit on what the Ombudsman may refer, not on the claimant.

## What the Act turns out to say (findings)

1. **s 392(6)(b) with reg 3.06 may count part pay twice.** The cap adds (a) the remuneration received or entitled to for
   "any period of employment ... during the 26 weeks" and (b) for leave "without pay or without full pay", the
   remuneration the employee "would ordinarily have received during the period of leave". Read literally, part pay
   received during leave without full pay is in (a) and the whole ordinary pay for that leave is added again in (b).
   FORK: this encoding asks for (a) outside the leave periods and (b) as the ordinary pay for the leave, so nothing is
   counted twice; the other reading adds the part pay again. Asserted (30,000 + 5,000 = 35,000).
2. **s 527T(3): a removed party has both periods.** Each of (a) 60 days from the certificate and (b) 14 days from notice
   of removal is "a period specified", so a removed party may file by whichever ends later; (b) only helps where the
   notice comes late. Asserted (8 September; and 30 August where 14 days from notice would end earlier).
3. **s 325(1A)(c) speaks of "the payment" for a requirement to spend.** Subsection (1)(b) is limited "for a payment";
   (1A)(c) has no such limit but still says "the payment is ... for the benefit of the prospective employer". READING:
   (c) applies to a requirement to spend as well, so a job applicant made to spend money that benefits no-one connected
   with the employer has no s 325(1A) claim. Asserted.
4. **When the wage theft offence started is not in the operative text.** Schedule 1 clause 98 applies s 327A(1) to
   conduct after "the commencement of Part 14 of Schedule 1" to the Closing Loopholes Act 2023; the date is only in the
   endnotes' commencement table (items 213-222: 1 January 2025), which does not say which items are Part 14. Asked as a
   fact.
5. **"24 months after" 29 February.** For s 527G the encoding takes the last day as 28 February two years on (daydate's
   `add months` clamps to the month's end). The other reading is 1 March. Asserted (28 February 2026).
6. **The indexed penalty unit and civil penalties.** Crimes Act s 4AA(8) says the indexed amount applies "only ... to
   offences committed on or after the indexation day"; it says nothing of civil penalty provisions. READING: the $364
   applies to a contravention from 1 July 2026 as it does to an offence. Before 1 July 2026 the answer is `NOTHING`: the
   compilation gives $330 as the base but not the day it began. Asserted.
7. **Small business and the penalty multiples.** s 546(2AA) and (2A) turn on whether "the person" was a small business
   employer "when the application for the order is made", not when the contravention happened; an employer that grew
   past 15 employees before the case is filed loses the small business limit. Encoded as the text says.
8. **s 342 item 2 has no dismissal.** A prospective employee cannot be "dismissed"; a withdrawn job offer is "refuses
   to employ". Asserted.
9. **The general protections penalty is not raised for knowing or reckless conduct.** Items 11 and 11A have one tier
   (60 penalty units), unlike items 1, 2 and 10 (600 for a serious contravention). Sham contracting (item 11A) is a
   selected civil remedy provision, so a non-small company faces 1,500 penalty units, five times the general
   protections maximum for the same company. Asserted.
10. **Stop orders cannot award money.** ss 789FF(1) and 527J(1) both say "other than an order requiring payment of a
    pecuniary amount"; compensation for sexual harassment comes only by FWC arbitration (s 527S(3)) or the court.
11. **Who employs a public hospital doctor matters.** s 62 and the rest of these provisions reach national system
    employees (s 13). A doctor employed by a State health body in a State that has not referred its powers may not be
    one; whether the employer is a national system employer is a fact (asked in `baseline-2026-10`).
12. **A company involved in a contravention faces the company maxima.** s 550 makes "a person" involved a contravener,
    and s 546(2)(b) and (2AA) turn only on whether "the person is a body corporate". A labour-hire firm, payroll or
    accounting firm, or parent company knowingly concerned in an award underpayment therefore faces 5 times the
    column 4 maximum, or 25 times for a selected provision when it is not a small business employer when the case is
    filed; only the underpayment multiple in s 546(2A) is barred to it (para (f)). Asserted (15,000 and 3,000 penalty
    units; $5,460,000 where 3 times the underpayment would be $6,000,000).

## Forks (for the human reviewer)

The rulings of 2026-11-04 and 2026-11-05 are in `docs/ENCODING-GUIDE.md` §5. Sites decided case by case:

- s 62(1), `Is my employer breaking the maximum hours rule`: "unless the additional hours are reasonable", met → `JUST
  FALSE`; other reading `NOTHING`. Within the s 62 hours → `NOTHING` (a limit in the prohibition's own words, ruling
  (c)).
- s 62(2), `Can I refuse these additional hours`: "if they are unreasonable", not met → `JUST FALSE`; within the hours
  → `NOTHING`.
- s 370 and s 527T, the court questions: parties agreed to arbitration → `NOTHING` (ss 727, 728, 734A not encoded);
  other reading `JUST FALSE`.
- s 527F(3), `Can I ask for a stop sexual harassment order`: a defence member → `NOTHING` ("except as provided by the
  regulations", none encoded); other reading `JUST FALSE`.
- Boolean questions whose text says "if", "only if", "unless" or "if, and only if" (ss 341, 342, 340, 351, 352, 357-359C,
  390, 789FC, 789FD, 789FF, 527D, 527E, 527J, 550, 558B, 547, 570) answer `FALSE` where the condition fails.

## Before relying on it

- An independent test pass, and a lawyer's look at findings 1, 2, 3 and 6.
- The penalty unit before 1 July 2026 (a deposit of the earlier compilation of Crimes Act s 4AA, or of the 2023
  amending Act's commencement).
- The modern awards that set junior doctors' overtime and the other overtime rates (and the State public sector
  instruments for doctors outside the national system).
- The industrial activity protections and the rest of the s 342 table, for a fuller general protections layer.
- A seat layer for the employer over these modules, with mirror cases.
