# National Injury Insurance Scheme (Queensland) Act 2016: baseline encoding for the injured person

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is what a person seriously injured in a Queensland motor accident meets in the scheme: whether the Act covers the injury, eligibility and buying in, applying and the time the agency has to decide, interim and lifetime participation, getting care paid for, the interplay with a damages claim against the CTP insurer (the preservation notice, the agency's contribution, accepting awarded damages), going overseas, reviews and the medical tribunal, and the person's offences.

It is written in layers:

- **`niis-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the injured person", "the participant", "the agency", "the insurer", "the court", "the medical tribunal", "QCAT"). Each function is preceded by the words of the section it encodes. Where the text sets a deadline there is a regulative rule (`DEONTIC`): eight in all (ss 13(3)-(4), 22(7) with 24, 37(4), 41(1)/(3)-(4), 44(2), 50(1), 53(2), 118(3)). The late preservation notice of s 41(4) is a permission (`MAY`), so missing the 14 days is no breach.
- **`niis-dates.l4`**, small date helpers on the stable prelude's date primitives, including business days. The `daydate` library is not imported and no `YMD` is defined. The date readings are stated at its top.
- **`niis-seat.l4`**, the injured person's seat: 33 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order the scheme is met. It builds the core's inputs from plain answers and restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`niis-cases-injured-person.l4`**, the cases, around one HYPOTHETICAL person (Mia, a passenger with a spinal cord injury from a collision on the Bruce Highway on 14 March 2025).

No earlier encoding of this Act existed. The Motor Accident Insurance Act 1994 baseline (`subjects/au/qld/motor-accident-insurance-act-1994/encodings/baseline-2026-11/`) asks this Act's facts (participant, s 44(3)(a) payment) for its s 42(3); it is untouched, and nothing is imported from it (IMPORT cannot cross folders).
No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**National Injury Insurance Scheme (Queensland) Act 2016** (act-2016-034), the version in force from 1 July 2024 and current on 6 November 2026, as deposited at `../../registers/source-bundle/act-2016-034.txt` (retrieved 2026-11-06, unofficial plain-text conversion of the Queensland Legislation HTML view).

Not deposited, and so asked as facts:

- the **National Injury Insurance Scheme (Queensland) Regulation 2016**: the eligibility criteria for each injury (s 12(1)(b)), the injuries for which a person may buy in and the contribution (s 13), the amounts that cap a payment within Australia (s 37(5)(a)), the waiting period after a s 44(3)(a) payment (s 17(4), at least 5 years by the Act), regulation-made exclusions and registered-provider requirements (s 9(1)(g), (2)(b)), and the vehicles prescribed under s 4(3)(a)(v).
- the day of the insurer's notice under the **Motor Accident Insurance Act 1994** s 39(1) or (2) (s 41(3)(a)); that Act is deposited and encoded in its own folder.
- the end of the **appeal period** for a judgment (s 44(8)(c)), set by the court rules.
- the time to apply to **QCAT** outside s 127(3) (QCAT Act, not deposited).
- the dollar value of a **penalty unit** (Penalties and Sentences Regulation 2015): answers are in penalty units.
- the **public holidays** for business days (s 118), as a list.

## Checks

| Module | Run | Result |
|---|---|---|
| `niis-dates.l4` | `l4 run` | 0 errors, 0 warnings |
| `niis-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `niis-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `niis-cases-injured-person.l4` | `l4 run` | 0 errors, 0 warnings; **186 assertions written, 186 satisfied** |

In addition, 7 `#TRACE`s carry an `-- expect:` line, one per regulative rule that can end in a breach (s 13 contribution, s 22 decision, s 37 payment, s 53 claim notice, s 44 acceptance notice, s 50 absence notice, s 118 documents), each a day late; each was read and ends in the breach expected with the reason written. The s 41 rule is asserted FULFILLED both in time and by the late route.
`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07). Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The injured person**: someone who suffered a serious personal injury in a motor accident in Queensland and applies to the scheme or is a participant in it, or, for them, a parent or guardian (of a child) or another person acting for them (s 11(4), s 18). They ask:

- "Does the Act cover my injury? Am I eligible? If not, can I buy in, and have I paid in time?"
- "By when should I apply? Must the agency take my application? Can I apply now, or can someone apply for me?"
- "By when must the agency decide, and is it taken to have refused?"
- "When does my interim participation end, and do I become a lifetime participant?"
- "Is this care excluded? By when must I ask for an expense to be paid? Must the agency pay, how much and by when? Has my payment request lapsed?"
- "I am claiming damages from the CTP insurer: must I tell the agency? By when must I give my preservation notice? Is the agency still liable to contribute? What happens to awarded damages if I accept them or not?"
- "I am going overseas: must I tell the agency, and can it suspend me?"
- "By when must I seek internal review, a medical tribunal, QCAT? By when must I give the tribunal my documents?"
- "What can I be penalised for, and by when can I be prosecuted?"

There is **no second seat**. The Act puts duties on the agency (an official body) and the insurer only as part of the scheme's administration; the agency and the court are never seats, and their duties appear only as what the person must be given and by when. An insurer seat could be added later as `niis-seat-insurer.l4` over the same core (s 18(2) copy, s 41 notice receipt, s 44(3)(c)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** The regulation is not deposited, so each of its figures is an input (listed under Edition). The s 17(4) waiting period is raised to the Act's floor of 5 years if a smaller figure is given.
- **The actors the text names:** the injured person, the applicant, the participant, the agency, the insurer, the court, the medical tribunal, QCAT.
- **Judgments left to others are answered conditionally, as inputs:** whether the injury meets the eligibility criteria and is likely to continue to (the agency, reviewable by the medical tribunal); whether the agency is satisfied, considers, or agrees (ss 16(3)-(4), 35(4), 41(4), 46, 52(2)); the court's orders (ss 41(4), (7), 43); a reasonable excuse (s 50(1)) is named as a condition in the answer, never decided; the s 52(1)(a) "satisfied the participant has left Australia for more than 3 consecutive months" is worked out from the dates (a fork line).
- **The Act's own definitions are worked out from facts:** serious personal injury, prescribed vehicle, uninsured motor vehicle, excluded treatment, care and support, finalised claim, decision-making period, participation period, approved service, acceptance period. Borrowed terms are asked as facts: road, public place, act of terrorism, mobile machinery, CTP insurance policy in force, self-insurer, contributory negligence.
- **One case:** one injured person, one serious personal injury, one motor accident.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (below).

One departure: the payment-request question (`Must the agency approve my payment request`) asks whether the care is excluded treatment, care and support as a single fact and points the person to the excluded-care question (`Is this care excluded`), which works the s 9 definition out from ten facts. Folding the ten facts into the payment question would make it twice as long; the two can be joined in a later pass.

## Scope

**In:**

- s 4, s 7, schedule 1 serious personal injury: when the Act applies (the four ways, Queensland from 1 July 2016, the uninsured-vehicle and special-vehicle exclusions, terrorism)
- s 9: excluded treatment, care and support, with s 9(2)-(3) (registered providers, the hospital exception)
- s 10: when a claim is finalised (for s 18(1)(a))
- s 12: eligibility, with s 12(2) (damages paid) and (3) (no permanent increase of an earlier disability)
- s 13: buying in, and the 28 days to pay the contribution (s 13(4))
- ss 16-18: the 1-year application period, when an application may not be made (s 17), who may apply (s 18)
- ss 21(2), 22(7)-(8), 24, 29(2), 31(2), 32, 36(2)(a), 37(1), 39, schedule 1 decision-making period: by when the agency must decide, and deemed refusal
- schedule 1 participation period, s 45(3), ss 46-48: the end of interim participation, becoming a lifetime participant
- ss 35-37: the 6 months for a payment request, lapse after an information request (s 36(3)-(4)), when the agency must approve, the cap, and the 28 days to pay
- ss 40-44: the preservation notice and its deadline, when the agency stops being liable to contribute, the acceptance period, and what follows acceptance or rejection
- ss 49-50, 52: notice before leaving Australia, and the power to suspend
- s 53: telling the agency of a claim within 14 days
- ss 105, 106(2)-(3), 107, 109(4), (7), 110(3)-(4), 112(1)-(3), 118(3), (6)-(7), 123, 127: reviews, the medical tribunal, QCAT
- ss 50(1), 53(2), 131(4), 132(1), 133, 134(2): the maximum penalties, the s 133(2) exception, and the time to prosecute

**Out, and why:**

- ss 1-3, 5, 6, 11 (preliminary, interpretation), s 14 (participant kinds: used inside, not asked), s 15 (matters the agency considers): machinery, or the agency's own deliberation.
- ss 19-20 (the contents of an application and notice to the insurer): the approved form and the regulation's information, not deposited.
- ss 25-27 (assessment and support plans), ss 28-31 (service requests, other than the decision deadline), s 34 (funding agreements), s 51 (amending plans for an absence): the agency's discretion, with no date or amount the person can compute beyond what is in.
- s 45(1), (2), (4) (when reviews happen): the agency's.
- chapters 3-5 (the agency, its chief executive, reporting, the fund, the levy, recovery from wrongdoers and interstate insurers, the commission) and chapter 7 (information exchange, other than the s 131(4) penalty): machinery; s 101(3)(a) (no right of recovery against a participant) is noted here only.
- ss 113-117, 119-122, 124-126, 128-129 (referral, the tribunal's constitution and procedure, the right to be heard, finality, the agency's re-review, QCAT procedure): procedure the person meets without a date or amount to compute; s 119 (only the injured person and their representative may be heard) noted.
- ss 135-149 (directions, forms, regulations, transitional provisions): machinery.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

Answers say no only where the text does: a "means" definition (schedule 1 serious personal injury; s 7 prescribed vehicle, read as closed; s 4(4) uninsured motor vehicle), "if" conditions (s 4(1), s 12(1), s 13(1), s 16(2), s 18(1)(a), s 37(2), s 42(1), s 52(1)), flat negatives ("does not apply", s 4(2)-(3); "is not eligible", s 12(2)-(3); "may not be made", s 17), "unless" (s 17(3)), a "stops being liable if" list (s 42(2)), and periods the text fixes (ss 13(4), 16(2), 35(3), 41(3), 44(8), 50(1), 53(2), 107(1), 112(3), 118(3)). Where s 18 lists who may apply without "only", the answer for anyone outside the list is that the Act does not settle it (`NOTHING` in the core).

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 4(2) and (4), `the s 4 answer`: an unidentified vehicle covered by a nominal defendant scheme is not shown to be an "uninsured motor vehicle", so s 4(2) does not exclude an off-road accident with it; the other reading treats it as uninsured. Asserted.
2. s 18(1), `may apply under ss 16 and 18`: a parent of an adult, or another person, not acting for the injured person answers NOTHING; the other reading is no. Asserted.
3. ss 21(2), 29(2), 36(2)(a), 108(2), `the last day of the decision-making period`: an information request made more than 28 days after receipt is read as not an information request, so the period runs from receipt; the other reading is that the 28 days are directory and the late request still restarts the period. Asserted.
4. s 22(8), the same function: an extension of more than 28 days is cut to 28; the other reading is that the notice is ineffective altogether.
5. s 36(3)-(4), `the s 36 answer`: a due day less than 10 days after the request answers that the Act does not say whether the request can lapse; the other readings are that it lapses on the stated day, or on the tenth day. Asserted.
6. s 112(3), `the s 112 answer`: the Act gives no power to extend the 28 days for a referral request (unlike s 107(2) for internal review), so a late request answers no; the other reading is that the agency may still refer it.
7. s 52(1)(a), `the s 52 answer`: "more than 3 consecutive months" is computed from the day of leaving and the last day of the absence so far, and the agency's satisfaction is assumed to follow the dates; the other reading asks the agency's satisfaction as a fact.

## What the Act turns out to say (findings)

1. **s 48(1) points at the wrong section.** It applies "If the agency does not make a decision under section 47 about a review"; the decision is made under s 46, and s 47 is the notice of it. Read as s 46. Possibly a drafting slip.
2. **The age-4 line in the participation period.** Schedule 1 does not say when "a child less than 4 years" is measured; read at acceptance. The two limbs meet almost exactly: a child accepted the day before turning 4 has until the 6th birthday, one accepted on the 4th birthday has 2 years, ending the day before it. Asserted (10 January 2027 and 9 January 2027).
3. **A preservation notice can be late only by agreement.** After the 14 days of s 41(3), s 41(4) needs both the insurer and the agency to agree, and a court order if the claim is in court, and it closes at final judgment or settlement. Asserted.
4. **s 36(3) sets a floor for the due day but no consequence** if the agency states an earlier one (fork line 5). Asserted.
5. **The agency's contribution stops at exactly 50% contributory negligence** ("by 50% or more", s 42(2)(a)); 49% leaves it liable. Asserted at both.
6. **s 44 says nothing about silence.** s 44(3) and (5) deal with a notice that accepts and one that does not; neither says what happens to the awarded treatment, care and support damages if no notice is given within the acceptance period. The s 44 rule breaches with that reason, and the question answers that the Act does not say. Asserted.
7. **s 9(3)'s hospital exception covers only s 9(2)(a).** Care the regulation requires from a registered provider (s 9(2)(b)) is excluded when an unregistered person gives it, even in hospital. Asserted.
8. **An uninsured trailer escapes s 4(2).** "Uninsured motor vehicle" excludes trailers (s 4(4)(c)), so an off-road accident involving an uninsured trailer covered by a nominal defendant scheme is within the Act while the same accident with an uninsured car is not. Asserted.
9. **s 53 has no reasonable-excuse proviso, unlike s 50(1).** Missing the 14 days to tell the agency of a claim is an offence on its face. Asserted.
10. **The decision-making period's extension is for applications only.** s 22(8) lets the agency extend the time for an application by up to 28 days; there is no matching power for service or payment requests (ss 31, 37). Asserted.
11. **s 134(2) read as the later of its two limbs**, with limb (b) capped at 2 years after the offence. The "or" does not say which governs when both are open. Asserted at three points.
12. **"At least 1 month before" a 31st.** Leaving on 31 March 2027, the same day a month earlier does not exist, so the notice is read as due by 28 February 2027 (the last day of the shorter month). The Act does not say how to count back a month; the Acts Interpretation Act 1954 is not deposited. Asserted.

## Before relying on it

- Deposit the National Injury Insurance Scheme (Queensland) Regulation 2016 and encode the eligibility criteria, the buy-in rules and contribution, the payment caps and the s 17(4) period.
- Deposit the Acts Interpretation Act 1954 (Qld) and check the date readings in `niis-dates.l4`, especially business days and "at least ... before".
- Have a lawyer check the fork lines and findings 1, 2, 6 and 11.
- Join the excluded-care facts into the payment-request question.
- Add the support plan and service request machinery (ss 25-31) if the agency's duties to the person there are wanted, and an insurer seat.
- An independent test pass, and the human gates.
