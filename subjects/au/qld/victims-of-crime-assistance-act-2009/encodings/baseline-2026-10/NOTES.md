# Victims of Crime Assistance Act 2009 (Qld): baseline encoding for the applicant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. An act of violence before 2 September 2024 answers `not covered` in every question that applies s 5 or chapter 3, and tests assert it (findings 20, 21).
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`voca-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the applicant", "a primary victim", "the scheme manager", "the government assessor"). Computations (capacities, special assistance and its Schedule 2 age tests, limits, components, reductions, time limits, deferrals, refunds) are functions. Where the text says "must" or sets a deadline there is a regulative rule (`DEONTIC`): eight in the core. A deadline for something the person chooses to do (apply, keep in contact, apply to amend, ask for a review) is a `DO` rule, and missing it is no breach (finding 22).
- **`voca-mai-s37.l4`**, the Motor Accident Insurance Act 1994 s 37(2)-(3) and the s 4 definition of "motor vehicle accident", brought in narrowly because VOCA s 36D turns on them. One regulative rule, the claimant's notice.
- **`voca-dates.l4`**, small date and amount helpers on the stable prelude's date primitives (the `daydate` library is not imported). The date readings are stated at its top.
- **`voca-seat.l4`**, the applicant's seat. It asks 22 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule. Its one test of its own is the coverage gate: the 21 questions that apply s 5 or chapter 3 take the day of the act of violence and answer `not covered` for a day before 2 September 2024 (finding 21). The two rules it once held (special assistance only for a primary victim, and the Schedule 2 age readings) are in the core (finding 25). Inputs with the same meaning carry the same name in every question, so the form can ask them once.

No earlier encoding of this Act existed to keep. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

- **Victims of Crime Assistance Act 2009** (act-2009-035), the version in force from **2 September 2024**, the current version on 20 October 2026, as deposited at `../../registers/source-bundle/act-2009-035.txt` (retrieved 2026-10-20, unofficial HTML conversion).
- **Motor Accident Insurance Act 1994** (act-1994-009), the current in-force version on 22 September 2026, as deposited at `../../../motor-accident-insurance-act-1994/registers/source-bundle/act-1994-009.txt`. Only s 37(2)-(3) and the s 4 definition of "motor vehicle accident" are read. Its licence and attribution are copied in `SOURCE-LICENSE-motor-accident-insurance-act-1994.md` (finding 24).

Every amount and limit is in the Act or Schedule 2. No regulation under the Act is in force (the jurisdiction README, Gaps), so nothing is an input for want of a regulation. The table of costs (s 132), against which expenses are "reasonable", is not deposited: each expense is the applicant's figure, taken as reasonable.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `voca-dates.l4`, `voca-mai-s37.l4`, `voca-core.l4`, `voca-seat.l4` | `voca-cases-applicant.l4` | 211 written, 211 satisfied |

In addition, 8 `#TRACE`s carry an `-- expect:` line. Three end in a breach: the notice of a relevant payment, the reviewer's 42 days, the Nominal Defendant bar. Five end with a rule still open and nothing breached: a late application for victim assistance and one for funeral expense assistance, each left at the permission to ask for more time; a lapsed application, left at the permission to apply again; an amendment application awaiting notice of the decision; a refund still owed. Each was read and matches its expectation. A deliberately wrong assertion was run in the scratchpad to confirm a failure shows as `DiagnosticSeverity_Error`.

`l4 run` on all five files: 0 errors, 0 warnings (2026-10-24, again after the corrections in findings 21 to 25). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion. The long argument lists of the seat questions were laid out by a small formatting script in the session scratchpad. For finding 21, a second script put each case's own day of the act into the existing lines and wrapped their expected values in the new answer types. Neither script holds expected values, and neither is part of the encoding.

## Seat

**The applicant for assistance**: a primary, parent secondary, witness secondary or related victim of an act of violence, or the person applying for funeral expense assistance. They ask:

- "Am I a victim who can get assistance, and in which capacity?"
- "What can I get, and up to how much, including special assistance for my category of act?"
- "By when must I apply?"
- "Will my claim wait while a workers' compensation or motor accident claim runs?"
- "How is my assistance reduced for other payments?"
- "What bars a grant?"
- "Can I get interim help?"
- "How do I ask for a review?"
- "When must I pay money back?"

There is **no second seat**. The scheme manager and the government assessor are officials, and the offender (Part 16) is not the person receiving the benefit. What the officials must do appears only as what the applicant is owed and by when: the deferrals and their limits (ss 36D-36J), the 42-day review (s 124(8)), the notices of decisions on an extension of time (ss 54(3), 58(3)) and on an amendment application (s 105(1)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** None is needed: the amounts are in the Act and Schedule 2. The MAI Act is brought in for s 37 only, because s 36D depends on it.
- **The actors the text names:** the applicant, the victim in each capacity, the scheme manager, the government assessor; in the MAI Act, the claimant.
- **Judgments left to others are answered conditionally, as inputs:** exceptional circumstances (s 28); reasonable excuses (ss 34(4), 36D(3), 81, 82); the scheme manager's extensions (ss 54(2), 58(2), 124(3)) and approvals (s 34(4), s 101(6)); whether expenses must be incurred before the decision (s 98(1)); the contributory conduct reduction (s 85), as a percentage; the part of a relevant payment made for another purpose (s 86(2A)); whether the primary victim's criminal activity was the main reason for the act (s 80); whether a lump sum or a payment was proved to rest on a fraud offence (s 123).
- **The Act's own definitions are worked out from facts:** act of violence and crime (ss 25, 25A), the capacities (s 26), injury and serious injury (s 27, Schedule 2), very serious injury, the categories and category A to C circumstances (Schedule 2), special primary victim (s 81(2)), more serious act of violence, the limits and components (Parts 4-8), the time limits (ss 34, 54, 58, 61, 101, 124) and the s 37(2) period. Borrowed terms are asked as facts: domestic violence (Domestic and Family Violence Protection Act 2012), impaired capacity, guardian and administrator (Guardianship and Administration Act 2000), the Criminal Code offences of Schedule 2 (named by section number only, as the Schedule names them), workers' compensation "finally dealt with" (s 33) and the statutory insurance scheme (MAI s 4).
- **One case:** one applicant, one act of violence (a series of related crimes counts as one, s 25B(5)), in one capacity (s 23).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the scheme manager and assessors (Part 19), guidelines and the table of costs (ss 131-132), information-sharing (ss 133-135), the victim services coordinator (chapter 4), offences other than ss 141A and 141B, and the transitional chapters.

## Scope

**In:**

- s 5 (victim, general meaning); ss 21, 23, 24 (the scheme; one capacity; effect of death)
- ss 25, 25A, 25B (act of violence, crime, series, the series as a fact); s 26 (capacities); s 27 (injury); s 28 (as a fact)
- Part 3, ss 31-34 (workers' compensation: the components left by s 32, and the s 34 conditions and time limit)
- Part 3A, ss 36A-36F (motor accident claims), with MAI s 37(2)-(3) and the s 4 definition
- Part 3B, ss 36G-36J (NIISQ), the NIISQ facts as inputs because the NIISQ Act is not deposited
- Part 4, ss 37-39 (primary victims: up to $120,000 plus up to $500 legal costs; loss of earnings up to $20,000 within 2 years; special assistance)
- Part 5, ss 40-42; Part 6, ss 43-46 (more and less serious acts witnessed); Part 7, ss 47-49; Part 8, s 50 (funeral expense assistance)
- Schedule 2 (special assistance by category A-D, with category A to C circumstances), as a table
- ss 51, 52, 54 (who may apply, the form, the time limit; an extension given is a fact, and asking for one with the notice of the decision is a rule, s 54(2)-(3)); s 55 (in a comment); ss 56-58 (funeral expense applications, with s 58(2)-(3) the same way); ss 59-61 (withdrawal, amendment, lapse)
- ss 78-82 (restrictions), with s 21(2)-(3); s 85 (contributory conduct, as an input percentage); s 86 and the Schedule 3 definition of relevant payment
- ss 89(2), 98(2), 141A, 141B (telling the scheme manager about a relevant payment)
- ss 97-100 (interim assistance); s 101 (applying to amend a grant), with ss 102 and 105(1) for who decides and the notice of the decision; s 106G, s 123, s 126 (refunds); ss 124-125 (review)

**Out:**

- Part 16 (recovery from the offender, who is not the person receiving the benefit)
- Part 12 Division 1 and ss 73-77 (information-gathering powers), ss 62-63, 70 (deciding a series together), ss 83, 84-84C and 87 (other deferrals), ss 88-96 except the s 89(2) condition (submissions, notices, payment), Part 15 Division 2 apart from the s 106G refund, Part 17 apart from s 123
- Part 19 and Part 20 (administration), chapters 2, 4 and 5 apart from ss 141A-141B, and the transitional chapters 6 to 11
- the QCAT Act's time limit for external review (s 125), not deposited

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social Security Act 1991**, `../../../../social-security-act-1991/encodings/baseline-2026-10/`. Section 17(2B), as deposited, says: "A payment under a law of the Commonwealth, a State or a Territory that provides for the payment of compensation for a criminal injury does not constitute compensation for the purposes of this Act." Section 17(2C) defines a criminal injury as "a personal injury suffered, or a disease or condition contracted, as a result of the commission of an offence". So assistance under this Act is not "compensation" for the compensation preclusion and recovery rules of Part 3.14, if it is "compensation for a criminal injury" in the s 17(2B) sense. That holds even for its loss-of-earnings component, which would otherwise meet the s 17(2) test of a payment "in respect of lost earnings". That encoding's finding 9 records the same exclusion. Two cases are not plainly covered:
  - assistance for a domestic violence act of violence that is not an offence (VOCA s 25(2)) is not "the commission of an offence";
  - funeral expense assistance is not for the applicant's own injury.

  For the **income test**, s 8(8) lists no state victims' assistance among the amounts that are not income. Whether a lump sum is an "exempt lump sum" (s 8(11)) depends on a determination by the Secretary, which is not deposited. Only s 8(8)(k), insurance or compensation "by reason of the loss of, or damage to ... personal effects", plainly fits one component, the clothing component (s 39(f)).
- **Income Tax Assessment Act 1997**, `../../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/`. The deposited text does not name victims' assistance. Section 118-37(1)(a)(ii) disregards a capital gain or loss from "compensation or damages you receive for ... any wrong, injury or illness you or your relative suffers personally". Whether the loss-of-earnings component is assessable under s 6-5 (ordinary income) or s 15-30 ("insurance or indemnity for the loss of an amount" that would have been assessable) is not stated. It is a question of characterisation the deposit does not answer.
- **Queensland workers' compensation.** Part 3 of this Act (ss 31-34) turns on facts that the Workers' Compensation and Rehabilitation Act 2003 decides: entitlement to compensation, the s 131 application and its prescribed period, when the total entitlement is decided (s 33), and the lump sum and other compensation paid. That Act is deposited at `../../../workers-compensation-and-rehabilitation-act-2003/`, and its encoding is being written in this workflow at `../../../workers-compensation-and-rehabilitation-act-2003/encodings/baseline-2026-10/`. Here those facts are inputs. A workers' compensation payment is also a "relevant payment" for s 86 (Schedule 3 (b)(iii)).

## What the Act turns out to say

1. **Someone harmed while helping is a "victim" but may get nothing.** Section 5(1)(c) makes a person harmed "as a direct result of intervening to help" a victim. For chapter 3, though, "victim" means a primary, secondary or related victim (Schedule 3, victim (b)), and s 26 has no capacity for an intervener. One is eligible only if the act was committed against them (primary) or they were injured by witnessing it. The same holds for a parent who is harmed but not injured on becoming aware of the act. Asserted.
2. **The Act does not say which capacity a person in two of them gets.** Section 23(2) allows "only 1 of the capacities". It does not say which, and s 60(2) lets the applicant change it. The capacity question returns every capacity open, and the amount question takes the one chosen. Asserted for a son who both witnessed his father's killing and is a related victim.
3. **A workers' compensation lump sum as large as the special assistance leaves none.** Section 32(6) gives the full amount "if the person has not been paid any lump sum" and the difference if the lump sum "is less than" the special assistance. Neither paragraph covers a lump sum equal to it or above it, so nothing is given. Asserted at $9,000 and $12,000 against category B's $9,000.
4. **Section 86(2A) speaks only of expenses.** The relevant-payment reduction does not apply "to the extent ... the purpose for which the relevant payment was or will be made does not include compensating the applicant for expenses in relation to which the applicant is eligible". Loss of earnings, special assistance and distress are not expenses. Read literally, then, a payment made only for lost earnings or for the injury itself escapes the reduction, even against the matching non-expense component. The government assessor decides the purpose, so the encoding asks for the excluded part as an input and does not guess. Not asserted.
5. **The bar for not helping the prosecution is narrower in s 82 than in s 21(3)(b).** Section 21(3)(b) says there is no entitlement if the person "has not given reasonable assistance in the arrest or prosecution". Section 82, the operative restriction, also needs that "the failure has prevented the arrest or prosecution" (s 82(1)(b)). It adds a bar s 21 does not mention: no reasonable help with "the police investigation (if any)", with no prevention test. And s 82(1)(a)(ii) is only for a crime, not for domestic violence that is not an offence. The encoding follows s 82. Asserted.
6. **No time limit is stated for an application made with s 34(4) approval.** Section 34(2), which "applies despite section 54(1)", runs from the day the workers' compensation application is finally dealt with. With s 34(4) approval there is no such application. The encoding applies s 54(1); that is a reading. Asserted.
7. **"Over 60 years" and "under 16 years" are read by the day.** Schedule 2 says "a child under 16 years" and "a person over 60 years". The encoding reads "under 16" as before the 16th birthday, and "over 60" as after the 60th birthday, not on it. So a person assaulted on their 60th birthday gets category D's $3,000, and one assaulted the day after gets category C's $6,000. The text does not settle the birthday itself. Asserted.
8. **Parent secondary victims are outside Part 3.** Section 31 lists "a primary victim, witness secondary victim or related victim". A parent paid workers' compensation (unusual, but possible where the parent was also injured at work) keeps the full s 42 components. Their compensation is still a relevant payment under s 86. Asserted.
9. **The Act gives no order, and no base, for the two reductions.** Sections 85 and 86 both reduce "the amount that would otherwise be payable". The encoding applies s 85 (a percentage) first, then s 86 (an amount), both to the amount after the $120,000 (or other) limit. Applied before the limit, a relevant payment would often cost the applicant nothing. Both are readings. Asserted: $120,500 less $20,000 is $100,500.
10. **Section 21(2)(c) is narrower than s 80(2).** Section 21(2)(c) disentitles "a person claiming assistance for the death of a primary victim" where the primary victim's criminal activity was the main reason for the act and the person was or should have been aware of it. Section 80(2) bars any "person who is not the primary victim", so it also reaches parent and witness secondary victims of an act against a living primary victim. The encoding follows s 80. Asserted for a related victim; the rule reads the same for any victim who is not the primary victim.
11. **A witness to a less serious act gets no legal costs and no exceptional-circumstances components.** Section 44(2) gives legal costs only "In addition to the assistance mentioned in subsection (1)(a)" (a more serious act). Section 46 has only counselling, medical, travel and report expenses. If that witness is paid workers' compensation, s 32(4) leaves only funeral expense assistance. Asserted.
12. **Funeral expense assistance comes off a witness's and a related victim's limit, but not a primary victim's.** Sections 44(1) and 48(1) give their limits "less any funeral expense assistance granted to the victim". Section 38(1) has no such words, and s 23(3)(a) lets a primary victim also be granted funeral expense assistance for an unborn child. Asserted: Liam's limit is $75,000 less $15,000.
13. **Refunds have no time.** Sections 100, 106G, 123 and 126 each say the person "must refund", and the amount "is a debt". No period is set. The regulative rule has no `WITHIN`, so it never breaches by time alone, and a part payment does not discharge it. Asserted by `#TRACE`: still owed 2,000 years on.
14. **"Urgent and immediate" in s 97, "urgent or immediate" in s 98.** Part 14 applies only to "urgent and immediate expenses" (s 97(c)), but s 98(1) grants interim assistance "for urgent or immediate expenses". Since s 98 has no work to do unless s 97 applies, the encoding asks the s 97 question. Not asserted.
15. **An NIISQ deferral holds back only medical expenses.** Section 36J(2) requires the assessor to decide "the application to the extent it relates to assistance mentioned in section 39(a) and (c) to (h)": everything in s 39 except (b), medical expenses. Legal costs under s 38(2) are not named either way. Where a motor accident deferral applies as well, s 36J does not apply (s 36J(1)(c)), and only counselling is decided (s 36F). Asserted.
16. **MAI s 37(3) bars only a claim against the Nominal Defendant.** For an identified vehicle, a late notice of claim is still owed, "and a reasonable excuse for the delay must be given"; s 37(3) never bars it. So VOCA s 36D(3)(a)(i) ("barred under ... section 37(3)") can be met only where the vehicle cannot be identified and 9 months have passed without notice. For an identified vehicle, only (a)(ii) is left: a late notice "tried unsuccessfully". In both, the scheme manager must also accept the excuse. The encoding computes the bar from the MAI dates and asks the rest. Asserted.
17. **The two child time limits end a day apart.** Section 54(1)(c), "within 3 years after ... the day the child turns 18", ends on the 21st birthday (reading the anniversary as the last day). Section 34(2)(b), "before the person turns 21", ends the day before it. Asserted: the 21st birthday in one case, the day before it in the other.
18. **For a series, the Act names no day for the time limit.** Section 54(1)(a) runs from when "the act of violence happens". A series of related crimes "is taken to be a single act of violence" (s 25B(5)), but which crime's day counts is not said. The encoding uses the day the applicant gives and asks for the first crime's day. Schedule 2's age tests apply "when 1 or more of the acts were committed": the core tests under 16 at the first crime and over 60 at the last, which is the same thing, because age only grows. Asserted for the age test.
19. **Some deposited definitions are elided.** Schedule 3 in the deposit shows 14 definitions as "...", among them "assistance limit", "police commissioner", "spent conviction" and "the principles". The MAI Act's s 4 shows "motor vehicle accident claim ..." and "mobile machinery or equipment ...". None is read by this encoding. The deposit should be checked against the authorised PDF.
20. **Acts of violence before 2 September 2024 are not covered.** Section 220(2) (chapter 9) applies chapter 3 "as amended by" the Justice and Other Legislation Amendment Act 2023 "only if the act is committed after the commencement". Chapters 8 and 10 carry further transitional rules (pools of assistance, existing applications). The commencement days are not in the deposit. All of those amending Acts had commenced by 2 September 2024, because the deposited version, in force from that day, contains their transitional chapters. So every question that applies s 5 or chapter 3 answers `not covered` for an earlier act (finding 21). Asserted on both sides of the line.

### Corrections after the independent check (2026-10-24)

An independent verifier raised five points. Each was checked against the deposited text, and all five were real.

21. **Every question that applies s 5 or chapter 3 now takes the day of the act.** Before, only the money and time-limit questions did. The capacity (ss 5, 26), death (s 24), who-may-apply (s 51), form (s 52), withdrawal (ss 59-60), Part 3, 3A and 3B, restriction (ss 78-82), reduction (ss 85-86, 100), interim (ss 97-98), lapse (s 61), relevant-payment (ss 89(2), 98(2), 141A), amendment (s 101), review (s 124) and refund questions answered an earlier act as if the current text applied. Section 220(1) says amended s 5 "applies in relation to a crime only if the crime is committed after the commencement"; s 220(2) says the same of chapter 3 and an act of violence. The deposit does not show the earlier text. Each of those questions now answers `not covered` for an earlier act. This is asserted for each on 1 September 2024, and for two on 2 September 2024. Only the Motor Accident Insurance Act s 37 question takes no such day. The questions that returned a bare yes or no, list or amount now return an answer that can also say `not covered`.
22. **Missing an application deadline is no breach.** The s 54(1), s 58(1) and s 61 rules were `MUST ... LEST BREACH BY the applicant`. Nobody must apply for assistance or keep in contact: "must be made within" sets the time for an application the person chooses to make (s 51(1) and s 56, "may apply"), and s 61(4) makes the application lapse. They are now `DO ... HENCE FULFILLED`, like s 124(2)(a). The LEST is what the Act gives next. For ss 54 and 58, the person may ask the scheme manager to extend the time, and the scheme manager must give notice of the decision (ss 54(2)-(3), 58(2)-(3)). For s 61, the person may make another application (s 61(5)). The three breach traces now end with that permission open. Three new assertions follow a late application, or a lapse, through to FULFILLED. The applicant's real duties stay `MUST`: notice of a relevant payment (s 141A, an offence under s 141B) and the refunds. So does the MAI s 37 rule, because s 37(3) itself speaks of "the obligation to give the notice".
23. **The s 101(3) time limit now has a regulative rule.** It was computed (`the last day to apply to amend the grant (s 101(3))`) but had no `DEONTIC`, although ss 54, 58 and 124(2) had one. The new rule is `DO apply to amend the grant WITHIN` the days to the s 101(3) last day, `LEST FULFILLED`. Its `HENCE` is the duty of whoever decides (the scheme manager, or the assessor it asks under s 102) to give notice of the decision (s 105(1)); no time is set for that notice. Asserted for an adult (6 years, day 2,191: on the day, and the day after) and for a child (before 24, day 3,713). It is also traced while the decision is awaited.
24. **The Motor Accident Insurance Act text has its own attribution.** `voca-mai-s37.l4` quotes MAI s 4 and s 37(2)-(3) word for word from the 22 September 2026 deposit, but the folder attributed only the Victims of Crime Assistance Act deposit. The MAI subject's `SOURCE-LICENSE.md` is now copied as `SOURCE-LICENSE-motor-accident-insurance-act-1994.md`, and `encoding.json` cites both files.
25. **Two rules in the seat are now in the core.** The seat decided that only a primary victim gets special assistance (s 39(h)). It also applied the Schedule 2 age readings to dates: under 16 at the first crime of a series, over 60 at the last (finding 18). Both are now core functions: `the special assistance answer for` a capacity and the facts, and the two age tests over the victim's date of birth and the first and last days. The seat's amount question no longer sets special assistance to 0 for other victims, because the core counts it only for a primary victim (ss 39(h), 32(6)). No expected value changed.

## Before relying on it

- An independent test pass, and a check of the deposit against the authorised PDF (finding 19).
- Deposit the Acts Interpretation Act 1954 (Qld), whose s 38 settles the date readings in `voca-dates.l4` and findings 7 and 17.
- Deposit the commencement days of the 2017 and 2023 amending Acts, and encode chapters 6 and 8 to 10, to cover acts of violence before 2 September 2024 (finding 20).
- Deposit the table of costs (s 132) and the scheme guidelines (s 131), which fix what is "reasonable".
- Deposit the NIISQ Act 2016 and the QCAT Act 2009 (its s 33 time limit for external review), now inputs or left out.
- Link to the Queensland workers' compensation encoding when it is committed: the s 33 "finally dealt with" test and the lump sum figures are its outputs.
- Encode ss 83, 84-84C and 87 (the other deferrals) and the s 88 submission process, which a person whose grant is reduced meets next.
