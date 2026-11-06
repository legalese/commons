# Motor Accident Insurance Act 1994 (Qld): baseline encoding for the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is the claims machinery of Part 4: who claims and against whom, the notice of accident claim and its time limits, what each side must do and by when once notice is given, the compulsory conference and mandatory final offers, starting proceedings, and the costs and limitation rules that follow.

It is written in layers:

- **`mai-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the claimant", "the insurer", "the Nominal Defendant", "the supervising principal"). Computations are functions; each is preceded by the words of the section it encodes. Where the text sets a deadline there is a regulative rule (`DEONTIC`): nine in all (ss 37, 37A, 37AA, 39, 41(1), 41(5), 45(2)(b), 51C(6), 51D). Starting proceedings within the s 51D 60 days is the claimant's choice and the text says "should", so that rule is a `DO` whose lapse is no breach; only a time limit the court then fixes ends in a breach (the s 51D(5) bar).
- **`mai-dates.l4`**, small date and amount helpers on the stable prelude's date primitives. The `daydate` library is not imported and no `YMD` is defined. The date readings are stated at its top.
- **`mai-seat.l4`**, the claimant's seat: 24 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a claim runs. It builds the core's inputs from plain answers and restates no rule. Inputs with the same meaning carry the same name in every question.
- **`mai-cases-claimant.l4`**, the cases.

No earlier encoding of this Act existed in its own folder. The Victims of Crime Assistance Act 2009 baseline (`subjects/au/qld/victims-of-crime-assistance-act-2009/encodings/baseline-2026-10/voca-mai-s37.l4`) encodes s 37(2)-(3) narrowly for its own s 36D; it is untouched, and nothing is imported from it (IMPORT cannot cross folders). This encoding's s 37 adds s 40 and s 57(3) and answers the same on the facts both cover.
No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Motor Accident Insurance Act 1994** (act-1994-009), the current in-force version on 22 September 2026, as deposited at `../../registers/source-bundle/act-1994-009.txt` (retrieved 2026-09-22, unofficial HTML conversion).

Not deposited, and so asked as facts:

- the **Motor Accident Insurance Regulation 2018**: the information a notice of claim must state, the records it must authorise and the documents that go with it (s 37(1)(a), (b), (e)), and the s 51C(4) costs basis. Whether the notice "was given as required" is the claimant's fact.
- the **lower offer limit, upper offer limit and declared costs limit**, fixed by the Minister under s 100A. The s 55F cases use hypothetical limits.
- the **period of limitation**, set by the Limitation of Actions Act 1974 (usually 3 years; part 3 extensions count, s 57(5)). The cases use a hypothetical 3 years.
- the Transport Operations (Road Use Management) Act 1995 s 93(4) particulars (s 34), and the National Injury Insurance Scheme (Queensland) Act 2016 facts (participant, eligible person, s 44(3)(a) payment).

## Checks

| Module | Run | Result |
|---|---|---|
| `mai-dates.l4` | `l4 run` | 0 errors, 0 warnings |
| `mai-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `mai-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `mai-cases-claimant.l4` | `l4 run` | 0 errors, 0 warnings; **153 assertions written, 153 satisfied** |

In addition, 9 `#TRACE`s carry an `-- expect:` line, one per regulative rule, each ending in the breach expected (the late refund, response, liability notice, additional information form, answer to a request, response to an offer, proceedings started while an offer is open, action started after the court's limit, notice to the Nominal Defendant after 9 months). Each was read and matches.
`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07). Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The claimant**: the person injured in a motor vehicle accident, or a person claiming for them (attorney, guardian or administrator; s 4 examples 1 and 2), or, for a fatal injury, for the dead person's dependants or estate. They ask:

- "Is mine a claim, and whom do I claim against? Whom do I sue?"
- "Must I tell the police? By when must I give notice of my claim? Is it late, or barred?"
- "My law practice gave me no certificate: must it refund my fees?"
- "What must I give the insurer, and by when? What must it tell me, and by when? Is it now taken to accept my notice?"
- "Can I go on if my notice was late or defective?"
- "What must the insurer pay for my treatment before settlement? How does its rehabilitation spending come off my damages?"
- "When can I call the compulsory conference? What must I exchange before it? When must final offers be exchanged?"
- "By when should I start court action? Can I start today? Is my claim barred? Does s 57 save me after the limitation period?"
- "Who gets costs on a small award?"

There is **no second seat** in this baseline. The insurer and the insured person (driver or owner) are parties the text puts duties on, and a seat for either is welcome later as `mai-seat-insurer.l4` or `mai-seat-insured.l4` over the same core. The commission, the Nominal Defendant as a fund, and the court are not seats; the insurer's duties appear only as what the claimant must be given, and by when (ss 39, 41, 42, 47).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** None of them is deposited (the regulation, the s 100A limits), so each is an input, as listed under Edition. A different s 100A figure changes only the s 55F answers.
- **The actors the text names:** the claimant, the insurer, the Nominal Defendant, the self-insurer, the insured person, the supervising principal of a law practice, the commission, the court.
- **Judgments left to others are answered conditionally, as inputs:** whether the insurer is satisfied, waives, or is presumed satisfied; whether a court declares the noncompliance remedied or authorises further proceedings (s 39(5)); a reasonable excuse (ss 37(3), 51D(4)); the further periods agreed or fixed (s 51D(1)(b), (2)(b), (3)); a court-fixed time limit (s 51D(4)(b)); a longer period under s 57(2)(b); dispensing with the conference or the final offers (ss 51A(4)-(5), 51C(11)); contributory negligence as a percentage (ss 42, 51(9A)); expenses "reasonably and appropriately incurred" (s 42), taken at the claimant's figure.
- **The Act's own definitions are worked out from facts:** motor vehicle accident, claim, claimant (s 4); the insurer (ss 31, 33); appropriate notice (s 34(2)); the s 37(2) period and the s 37(3) bar, with s 40; the relevant date (s 51A(3)). Borrowed terms are asked as facts: personal injury, the statutory insurance scheme, CTP insurance in force, self-insurer, the TORUM particulars, the period of limitation, participant in the injury insurance scheme.
- **One case:** one claimant, one claim, one motor vehicle accident.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (below).

## Scope

**In:**

- s 4: claim, claimant, motor vehicle accident
- Part 4 Division 1: s 31(1) (the insurer), s 32 (in effect), s 33(2)-(3) (the Nominal Defendant after insolvency; outside Queensland)
- Division 2: s 34 (police notice)
- Division 2A: s 37AA (refund where no law practice certificate)
- Division 3: s 37(2)-(3) (time for notice, late notice, the Nominal Defendant bar); s 37A(3) (additional information form); s 39(1)(a), (3), (5), (8) (the insurer's response, the presumption, going on despite noncompliance, no waiver of the bar); s 40 (minority and legal incapacity); s 41(1), (3), (5) (the insurer's liability notice; when a defective notice is taken to be received; responding to offers); s 42(1), (3) (payment of private hospital, medical and pharmaceutical expenses)
- Division 4: s 45(2)-(3) (the claimant's 1-month steps); s 47(2) (the insurer's 1-month steps)
- Division 5: s 51(9)-(9A) (rehabilitation costs in damages, with the Act's worked example as a case)
- Division 5A: s 51A(1)-(3) (compulsory conference, the relevant date); s 51B(5) (documents 7 days before); s 51C(1), (6) (mandatory final offers, the 14 days open); s 51D (time for bringing the action, the court-fixed limit and the bar)
- Division 6: s 52(1)-(2) (defendants); s 55F(1)-(3) (costs on small awards); s 57(1)-(3), (5) (limitation altered by notice; notice to the commission in the last 14 days)

**Out, and why:**

- Parts 1-3 and 5-9 except s 4 (the commission, premiums, licensing and supervision of insurers, investigations, offences, transitional provisions): machinery, or duties on insurers and the commission that a claimant never meets.
- s 31(3)-(4) (trailers): a narrower case left for a later pass.
- ss 35-36 (duties of drivers, owners and anyone who receives a claim) and ss 43-44 (the insured person must not admit liability; the insurer acts for them): duties of the insured person, for an insured seat.
- ss 36A-36E, 37AB, 39A, 41A (law practice certificates): duties of the supervising principal; only the claimant's refund (s 37AA) is in.
- s 37(1)(a)-(e) contents of the notice (in the regulation, not deposited) and s 37(4), s 38 (multiple insurers, the claim manager), s 37B (witness information): between insurers.
- s 39(1)(a)(ii)-(v), (1)(b), (2), (4), (6), (7) (the content of the insurer's response; a non-insurer's denial; prejudice; court conditions and costs): left to the insurer and the court; s 39(7)(b) (no interest for a default without reasonable excuse) noted only.
- s 41(2), (4), (6) (estimate, the materials with an offer, admissions not binding), s 42(2), (4)-(5), s 45(1), (7), ss 45A-46B (expert reports and examinations), ss 48-50 (privilege; court enforcement, cited in the rules' breach reasons): procedure the claimant meets without a date or amount to compute.
- s 51(1)-(8), (10) (rehabilitation services and mediation), s 51B(1)-(4), (6)-(12), s 51C(2)-(5), (7)-(11): procedure at and around the conference; s 51C(5) (an insurer that denies liability offers $nil) noted in a `@desc`.
- ss 52(3)-(7), 52A-55 (several insurers, contribution, summary judgment, cross-examination, exemplary damages), s 55F(4)-(7) (costs adjustments left to the court), s 57(4), ss 57A-60 (foreign awards, recourse): for the insurer or the court.
- s 57(1)-(2)'s leave route ("an application for leave to bring a proceeding ... made under division 3"): the deposited Division 3 has no separate leave application other than the court's s 39(5)(c) authorisation, whose interaction with s 57 was left for a later pass.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

Answers say no only where the text does: "means" definitions (s 4 claim and motor vehicle accident: `no`), "if (and only if)" (s 34(2)(b), s 51(9)), "only if" (s 33(3)), "unless" (s 39(5)), "if" conditions (ss 37AA, 51D(5), 57(3)). Where the text "includes" without closing the list (s 4 claim, for someone other than the injured person, a representative, a dependant or the estate), the answer is that the definition does not settle it (`NOTHING` in the core).

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 4, `is a claimant (s 4)`: someone else answers NOTHING; the other reading is no.
2. s 39(5), `the s 39(5) answer`: an "unless" not met answers that the claimant may not proceed; the other reading is that the court may still be asked (s 39(5)(c)), which the answer's wording keeps open.
3. s 51D(4)-(5), `the claim is barred under s 51D(5)`: with no court-fixed limit the answer is no (the text: the expiry "does not prevent the claimant from starting").

## What the Act turns out to say (findings)

1. **Two clocks for one notice.** The s 37(2) period is the earlier of 9 months and 1 month after first consulting a lawyer. A claimant who sees a lawyer a week after the accident has about 5 weeks, not 9 months. Asserted (case 1).
2. **s 40 and the s 37 periods (READING).** s 40(2) says a period "begins when the claimant's minority or legal incapacity ends". The encoding moves the start of every s 37 period that would begin earlier to that day, including the 9 months of the Nominal Defendant bar in s 37(3), and leaves a later start (late symptoms, a lawyer after majority) alone. The other reading keeps the s 37(3) bar running from the accident, since it is a consequence rather than "a period within which the obligation is to be complied with". Asserted (case 3).
3. **Late notice is still owed.** Outside the Nominal Defendant case, s 37(3) sets no end to the continuing obligation; the limitation period and s 39(5) do the work. The s 37 rule waits indefinitely for an identified vehicle. Asserted.
4. **The s 37(3) bar against the presumption of s 39(3).** s 39(8) stops the Nominal Defendant waiving and the court giving leave, but does not mention the s 39(3) presumption. Read with s 37(3) ("the claim ... is barred"), the encoding lets nothing lift the bar. Asserted (case 2).
5. **s 41(3) and a presumed notice (READING).** s 41(3) moves the start of the insurer's 6 months only for a notice "not given as required". A notice the insurer is presumed under s 39(3) to accept is treated as given as required, so the 6 months run from receipt.
6. **s 39's 14 days, the presumption and a late response.** A response on day 15 does not undo the s 39(3) presumption: "does not respond ... within 14 days" is met. Asserted.
7. **s 51(9A) can go below nil.** The set-off of the rehabilitation cost is applied without a floor; with large rehabilitation costs and a large contributory negligence the arithmetic gives a negative "award". The text does not say whether the claimant then owes the difference. Asserted (-4,000).
8. **s 51C(6) (READING).** "Must remain open for 14 days" is read as the 14 days after the day of the exchange; proceedings may start on the 15th day. Asserted.
9. **s 51D(2)(a)(i) differs from s 51A(3)(b).** s 51A(3)(b) takes the later of 6 months after notice and 1 month after the additional information form; s 51D(2)(a)(i) takes, where additional information was asked for, "the date on which the claimant gives the insurer the completed additional information form", with no "later of" and no month. Taken as written: where the form was given early and the conference dispensed with early, the 60 days can run out before 6 months after notice. Possibly a drafting slip. Asserted (8 February 2026).
10. **s 55F where the claimant's offer is at or below the insurer's.** Paragraphs (b) and (c) of s 55F(2) and (3) then overlap. The encoding applies them in their order, so (b) is taken. Asserted.
11. **s 57 helps only a notice given in the last 6 months of the limitation period**, unless the court allows a longer period: proceedings after the period may only be brought within 6 months after the notice. A claimant who gave notice early and waits past the limitation period has no s 57 extension. Asserted.
12. **s 57(3)** lets a notice go to the commission in the last 14 days when the claimant is unsure which insurer; read as the last day and the 13 before it. Asserted at both edges.

## Before relying on it

- Deposit the Motor Accident Insurance Regulation 2018 and the current s 100A limits, and encode the notice contents and the s 51C(4) costs basis.
- Deposit the Limitation of Actions Act 1974 (Qld) and compute the period of limitation instead of asking it.
- Have a lawyer check readings 2, 5, 8, 9 and 11, and the fork lines.
- Add seats for the insurer and the insured person, and the trailer rules of s 31(3)-(4).
- An independent test pass, and the human gates.
