# Motor Accident Insurance Regulation 2018 (Qld): baseline encoding for the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is the provisions a claimant meets: what the notice of claim must contain and what must go with it, settlement, the payment of treatment and rehabilitation expenses, the information the insurer obtains about the claimant, the costs that follow an accepted mandatory final offer, examination allowances, and the gratuitous insurance of motorised mobility devices.

It is written in layers:

- **`mair-core.l4`**, the seat-neutral core, in the regulation's own actors and terms ("the claimant", "the insurer", "the commission", "the court", "the public trustee"). Each function is preceded by the words it encodes. The one deadline in scope, s 22, is a regulative rule (`DEONTIC`): the insurer must give the information within 1 month, or (`ROR`) decide to withhold it on suspicion of fraud and then tell the commission within 1 month after deciding.
- **`mair-dates.l4`**, small date helpers on the stable prelude's date primitives. The `daydate` library is not imported and no `YMD` is defined. The date readings are stated at its top.
- **`mair-seat.l4`**, the claimant's seat: 15 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a claim runs. It builds the core's inputs from plain answers and restates no rule. No question takes a `DEONTIC` or `EVENT` input; the s 22 question builds its trace from dates.
- **`mair-cases-claimant.l4`**, the cases.

The Act has its own baseline (`subjects/au/qld/motor-accident-insurance-act-1994/encodings/baseline-2026-11/`), which asked the regulation's notice contents and the s 51C(4) costs basis as facts because the regulation was not then deposited. It is untouched, and nothing is imported from it (IMPORT cannot cross folders). This encoding supplies what it asked: the notice contents (ss 16-19) and the s 51C(4) basis (s 29).
No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Motor Accident Insurance Regulation 2018** (sl-2018-0113), the version in force from 1 July 2026, current on 6 November 2026, as deposited at `../../registers/source-bundle/sl-2018-0113.txt` (unofficial HTML conversion; not the authorised PDF).

Not deposited, and so asked as facts:

- the **lower offer limit, upper offer limit and declared costs limit**, fixed by the Minister under s 100A of the Act. The s 29 cases use hypothetical limits ($30,000, $50,000, $3,500).
- **item 1 and item 5 costs** under the Uniform Civil Procedure Rules 1999, schedule 2, part 2 (s 29(3)).
- the **District Court witness allowances** (s 30), named but not computed.
- **motorised mobility device** (Transport Operations (Road Use Management) Act 1995, schedule 4), **adult** and **full capacity** (s 20).

Five formula images in the deposited text were not converted (ss 5(6), 8(3), 9(5), 10(8), 12(7)). None is in this encoding's scope.

## Checks

| Module | Run | Result |
|---|---|---|
| `mair-dates.l4` | `l4 run` | 0 errors, 0 warnings |
| `mair-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `mair-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `mair-cases-claimant.l4` | `l4 run` | 0 errors, 0 warnings; **104 assertions written, 104 satisfied** |

In addition, 2 `#TRACE`s carry an `-- expect:` line (the information never given; the commission not told after a decision to withhold). Each ends in the expected breach and was read.
`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07). Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The claimant**: the person injured in a motor vehicle accident who claims under the Motor Accident Insurance Act 1994, a person claiming for them, or, for a death, the dependants. They ask:

- "Is the mobility scooter that hit me insured by the Nominal Defendant?"
- "What must my notice of claim say? What must go with it? Is it in the right form?"
- "Is my old back injury a significant disability I must list?"
- "Does my identity evidence do? Does my photograph count?"
- "Does what my law practice paid for my referral count as consideration?"
- "Must the insurer's offer come with an explanatory statement? Can my claim be settled without approval? May the insurer assume I have full capacity? Can the court protect me?"
- "Will the insurer take my request for expenses?"
- "By when must the insurer give me what it learnt about me, and is it late?"
- "What costs do I get if a mandatory final offer is accepted?"
- "Do I get allowances for attending an examination?"

There is **no second seat**. The registered operator of a vehicle (premium surcharges, class changes, refunds: ss 4-13) is a party the regulation puts duties on, and a seat for them is welcome later as `mair-seat-operator.l4`. The insurer is a party too, but its duties in this regulation are owed to the commission (returns, accounts, the industry deed) apart from ss 20(1) and 22, which appear here as what the claimant must be given. The commission, the court, the public trustee and transport administration are not seats.

The 2026-10-18 defaults:

- **The instrument, with the instruments that set its numbers.** The regulation itself sets most of its numbers ($200, 15 years, 4 weeks, 2 years, 1 year, $175, $150, $400, 1 month). The s 100A limits and the UCPR item costs are inputs.
- **The actors the text names:** the claimant, the insurer, the commission, the court, the public trustee, the Nominal Defendant, a doctor, the law practice.
- **Judgments left to others are answered conditionally, as inputs:** the court's or public trustee's satisfaction and approval (s 20(2)); the court's finding of "another reason" (s 20(4)(b)); whether incapacity "should be apparent to the insurer" (s 20(3)(a)); "reasonable grounds to suspect the claimant of fraud" (s 22(2), taken from what the insurer has told the claimant); "reasonable disbursements" (s 29(1)(e), at the claimant's figure); whether a disability "may be relevant" to the assessment (s 17(3)(a)).
- **The regulation's own definitions are worked out from facts:** significant disability (s 17(3)), identity document, certified copy, recent certified photograph, consideration (s 18(5)), derivative claim (schedule 5, as the claimant's answer). Borrowed terms are asked as facts.
- **One case:** one claimant, one claim, one notice of claim; for s 21 one request; for s 22 one body of information.
- **The regulation's own terms**, quoted in the comment above each rule.
- **Machinery out** (below).

## Scope

**In:**

- s 14 (gratuitous insurance of motorised mobility devices)
- Part 4, the whole Part: s 16 (form of the notice), s 17 (contents; s 17(3) significant disability), s 18 (certificates, identity evidence, s 18(5) definitions), s 19 (records permission, as a contents item), s 20 (offers of settlement, capacity, court protection), s 21(1)-(2) (requests for payment of expenses), s 22 (information the insurer obtains)
- s 29 (costs if a mandatory final offer is accepted: the s 51C(4) basis)
- s 30 (allowances for attending an examination)
- schedule 5: derivative claim, disability, notice of claim, offer of settlement

**Out, and why:**

- Part 1 (title, commencement, definitions): machinery.
- Part 2 and schedule 1 (classification of vehicles), Part 3 Division 1 (ss 5-13: the insurer's premium, additional amounts, levies, surcharges, class changes and refunds) and schedules 2-3: they concern the registered operator and the premium, not a claim; a registered-operator seat could take them later. Four of the five unconverted formulas are here (ss 8(3), 9(5), 10(8), 12(7)); they would need a `sl-2018-0113.formulas.md` sidecar from the authorised PDF first.
- s 15 (interest on amounts owed to transport administration): between insurers and transport administration.
- s 21(3) (a doctor's certificate "if the insurer reasonably requires"): it turns wholly on the insurer's judgment and sets no time; it is mentioned in no question.
- Part 5 (ss 23-26: licence applications, conditions, accounts, returns, and the s 26(6) definitions of disputed notice of claim, compliance date and resolved): duties of licensed insurers to the commission. The s 26(6) definitions describe the Act's s 39 outcomes, which the Act's baseline already encodes.
- s 28 (professional bodies for expert panels), s 31 (who may exchange information), ss 32-33 and schedule 4 (the industry deed: claims management, cost sharing between insurers, referees, late fees), ss 34-35 (expired): machinery, or between insurers, the commission and transport administration.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

Answers say no only where the text does: "means" definitions (s 18(5) identity document, certified copy, recent certified photograph, consideration: no); "if" conditions (s 17(3), s 18(1) and (4), s 20(1), s 20(4), s 29(1)); "unless" (s 20(2), s 20(3)); "must ... be for a total amount of at least $200" (s 21(1)).
Where the text limits a grant to a class and the case falls outside it, the answer is that the provision does not say (`NOTHING` in the core).

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 14, `gratuitously insured by the Nominal Defendant under s 14`: a vehicle that is not a motorised mobility device answers NOTHING; the other reading is no (but other classes may be gratuitously insured under the Act's s 23 itself).
2. s 29, `the s 29 costs entitlement`: an offer not accepted, or outside the band (at or below the lower offer limit, or above the upper), answers NOTHING ("s 29 does not set my costs"); the other reading is no s 29 entitlement ($0).
3. s 20(3), `the insurer may assume full capacity (s 20(3))`: a claimant who is not an adult answers NOTHING; the other reading is no (and s 20(2) then governs in any case).
4. s 21, `the request meets s 21`: expenses other than s 42 and s 51 expenses answer NOTHING; the other reading is that s 21 places no limit on them (yes).
5. s 30, `entitled to witness allowances and expenses (s 30)`: a person not required to attend under Part 5B answers NOTHING.
6. s 22, the regulative rule: a decision to withhold taken after the month has run is not a way out of s 22(1) (the s 22(1) breach stands); the other reading is that s 22(2) excuses at any time. Asserted.

## What the regulation turns out to say (findings)

1. **No medical certificate for a non-fatal derivative claim.** s 18(1)(a) requires the doctor's certificate only "if the claim is not a derivative claim"; s 18(1)(b) requires the death certificate only for a derivative claim "by or for the dependants of a person who died". A derivative claim where nobody died (schedule 5's own example: a spouse's claim for loss of consortium) needs neither, so no medical evidence of the injury goes with that notice. Asserted.
2. **An expired identity document closes both routes in s 18(4).** The s 18(5) definition of identity document has no currency in it. A claimant aged 15 or more whose only identity document has expired "holds an identity document", so s 18(4)(b) (a recent certified photograph, "if the claimant does not hold an identity document") is closed, and cannot give "a certified copy of an identity document ... that is current" under (a). Taken as written; possibly a drafting gap. Asserted.
3. **"Within the last 2 years" and "for at least 1 year" (READING).** s 18(5) gives neither period an anchor. The encoding counts the 2 years back from the day the notice is given (a photograph taken on the same calendar day 2 years earlier counts; one taken after the notice does not) and the 1 year up to the day of the certification. Asserted at both edges and over a leap day.
4. **s 20(2) names "the court or the public trustee".** The encoding reads (a) satisfaction and (b) approval as both needed, from the same body; the inputs do not separate a court that is satisfied from a public trustee that approves.
5. **s 21(2) is narrower than it looks.** It lets a request under $200 through only if the claimant expects no further request and the request is "for the outstanding total of the expenses"; the evidence requirement of s 21(1)(b) still applies. Asserted.
6. **s 22 and when withholding must happen (READING).** s 22(2) ("may withhold") sets no time; the encoding treats it as an alternative to s 22(1) that must be taken within the month (fork line 6). Information "obtain[ed] ... under section 19" is read as information obtained through the claimant's s 19 permission.
7. **s 29(1)(c), a part hour (READING).** "For a period of less than 1 hour, the relevant proportion of the appropriate hourly rate" is read as a part of the first hour at $175 an hour and a part of a later hour at $150 an hour (61 minutes = $177.50). Asserted.
8. **Two caps in s 29.** s 29(1)(d) caps the costs of an application to the court at $400; s 29(2) then caps the total at the declared costs limit. Asserted at both.
9. **The s 29 band.** "More than the lower offer limit but not more than the upper offer limit": an offer equal to the lower limit gets nothing under s 29; one equal to the upper limit does. Asserted.
10. **Duplicate definitions.** "certifying doctor" and "injured person" are defined twice, identically (ss 17(4) and 26(6)). Harmless.
11. **Empty dictionary entries.** Schedule 5 has "direct debit arrangement ..." and "insurance renewal amount ..." with no text in the deposited version; possibly omitted entries or a conversion artefact. Neither is used in scope.

## Before relying on it

- Deposit the current s 100A limits and the Uniform Civil Procedure Rules 1999 schedule 2 items, and compute s 29 from them instead of asking.
- Have a lawyer check readings 3, 4, 6 and 7, findings 1 and 2, and the fork lines.
- Transcribe the five formulas into a `sl-2018-0113.formulas.md` sidecar and add a registered-operator seat for ss 4-13.
- An independent test pass, and the human gates.
