# Victims of Crime Assistance Act 1976 (Tas): baseline encoding for the applicant

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit "not covered" value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`vca-core.l4`**: the seat-neutral core, in the Act's own actors and terms ("a person", "a primary victim", "a secondary victim", "a related victim", "the applicant", "the Commissioner"). Awards are "within the discretion of the Commissioner" (s 5(1)), so the amount awarded is always an input. The core decides who may be awarded compensation and as which kind, the heads open to each kind, the exclusions, the prescribed maxima and their indexation, what is paid after the cap and the s 6B deductions, and the time limits. Computations are functions. Where the text sets a duty with a period or a "must not", there is a regulative rule (`DEONTIC`): two in all, covering s 7(1A)-(1D) and (8)-(9) with the limits of ss 5(2), 5(3A), 6 and 6A.
- **`vca-seat.l4`**: the applicant's seat, 11 questions.
- **`vca-cases.l4`** and **`vca-cases-maxima.l4`**: the cases.

Each question has `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order. The seat builds the core's records from plain answers and restates no rule. Where one answer depends on another question (the kind of applicant, the heads claimed, the maximum), the `@desc` names that question.

No earlier encoding of this Act existed. Tasmania has no requirement ledger, so no ledger line is closed, and no scenario life covers Tasmania, so every case is hypothetical.

## Edition

- **Act:** Victims of Crime Assistance Act 1976 (Tas), No. 32 of 1976, consolidated version published **2023-12-08**, current on www.legislation.tas.gov.au at point in time 2026-10-20, deposited at `../../registers/source-bundle/act-1976-032.txt`. Its last amendment applied is the Victims of Crime Assistance Amendment Act 2023 (No. 32 of 2023, 27 November 2023: s 5(10) and s 40B).
- **Regulations:** Victims of Crime Assistance Regulations 2021 (Tas), S.R. 2021, No. 116, consolidated version published **2021-12-14** (in effect from 15 December 2021, reg 2), deposited at `subjects/au/tas/victims-of-crime-assistance-regulations-2021/registers/source-bundle/sr-2021-116.txt`.
- **Law at lodgement:** s 5(9) applies "this Act, as in force at the time the claim was lodged". The provisions in scope have had their present text since 20 April 2023 (No. 2 of 2023 amended s 7(1A) and inserted s 7(1D), (11), (12)), except s 5(10), which s 40B(1) applies to every determination. So the encoding speaks for applications lodged on or after 20 April 2023. "Is my application in time" answers "not covered" for an earlier lodgement; the other questions assume a current one.
- Uncommenced amendments are not in a consolidation, and the site's uncommenced-legislation feed was not checked (README, Currency).

Figures the texts fix are constants: the 2021-22 maxima ($30 000, $50 000, $20 000, $10 000 and the $10 000 funeral maximum, reg 4(2)(a), (3)(a)), 3 years (s 7(1A), (1B), (8)), 18 years (s 7(1B), s 2), 1 November 2015 (s 4(1B), from the history note "Applied:01 Nov 2015") and 15 December 2021 (reg 2). Three things are not in any deposit, so they are **inputs**:

- the Hobart CPI figures (reg 4(1)), as quarterly figures from the March quarter 2020;
- the date the Act commenced (s 1(2), by proclamation), for s 12, asked as "before the Act commenced?";
- the maxima under the regulations in force before 15 December 2021. They are not asked: an answer that needs them says so.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vca-core.l4`, `vca-seat.l4` | `vca-cases.l4` | 93 written, 93 satisfied |
| `vca-core.l4`, `vca-seat.l4` | `vca-cases-maxima.l4` | 53 written, 53 satisfied |

In addition, 6 `#TRACE`s in `vca-cases.l4` carry an `-- expect:` line. All six are breaches:

- by the applicant, lodging a day late, under s 7(1A) and under s 7(1B);
- by the Commissioner, awarding $40 000 over a $33 736.50 maximum (s 6A);
- by the Commissioner, awarding $5 000 where s 6(1)(a) excludes the claim;
- by the Commissioner, not determining within 3 years (s 7(8)), twice: with no determination, and with a determination after the period that an extension would have covered.

Each was read and matches its expectation.

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion. The CPI figures in `vca-cases-maxima.l4` are hypothetical, chosen so that the hand arithmetic is exact. The day counts in the traces are worked in the comments.

## Seat

**The applicant** (`vca-seat.l4`): a primary, secondary or related victim of an offence, or a person who paid, or will pay, a primary victim's funeral expenses (s 4(1A) says "a person", who need not be a victim). They ask:

- "Can I apply, and as which kind of victim?"
- "Which heads of compensation can I claim?"
- "Is my claim excluded, and does it belong to MAIB or workers compensation instead?"
- "Can I be refused because I could sue, and what that I recover must be taken into account?"
- "What is the most I can be awarded for this application?"
- "What would be paid to me on an award?"
- "By when must I apply? Is my application in time? By when is it to be decided?"
- "What must my application contain?"

**The Commissioner is an official, so gets no seat.** The Commissioner's "shall not make an award" (s 5(2), (3A)), "must not be awarded" (s 6), "must not exceed" (s 6A) and "is to be determined within 3 years" (s 7(8)) appear in two ways. The person reads them as the outcome of a function: "wholly excluded because …", or "the most that may be awarded". In the core's regulative rule, the Commissioner is the party, so that a trace shows a late or excessive award as a breach. The Act puts no duty on any other party in the scope (the offender's duties are in s 7A, out of scope), so there is no second seat.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** Followed: reg 4 supplies the maxima and their indexation. Reg 5 (application contents) is also in, as a checklist, because the task asked for it.
- **The actors the text names.** Followed: primary, secondary and related victims, "a person" who incurred funeral expenses, the applicant, the offender and the Commissioner.
- **Judgments left to others are answered conditionally, as inputs.** Followed. These are:
  - the Commissioner's satisfaction on the balance of probabilities (s 5(2));
  - the Commissioner's opinion that the applicant failed to help police (s 5(3A));
  - an adequate civil remedy, and what would likely be recovered (s 5(4));
  - special circumstances for an extension (s 7(1C), (9));
  - whether future services are paid on top of the maximum (s 6A(4));
  - what the Commissioner deducts (s 6B);
  - the amounts assessed under each head, and so what is "actually and reasonably incurred".
- **The Act's own definitions are worked out from facts.** Followed for primary, secondary and related victim, offence, criminal conduct and injury (s 2). Borrowed terms are asked as facts:
  - "violence";
  - the Criminal Code crimes and "excuse or justification at law";
  - "spouse" and "guardian";
  - "personal relationship" (Relationships Act 2003);
  - "motor vehicle" (Vehicle and Traffic Act 1999);
  - what is paid or payable under a "compensation law";
  - what is "claimable" from Medicare or a fund;
  - "child sexual abuse".
- **One case is one applicant, one "particular criminal conduct" (s 6A(2)) and one application.** A person who is two kinds (finding 4) asks the maximum question once for each kind.
- **The Act's own terms**, quoted in the comment above each rule (CC BY 4.0, State of Tasmania; see `SOURCE-LICENSE.md`).
- **Machinery out**: Commissioners (s 2A), s 3, the Fund (s 11), protection (s 40A), regulations (s 41).

## Scope

**In:**

- **Definitions** (s 2): primary, secondary and related victim; offence; criminal conduct; injury, including pregnancy (s 2(2)); dependant (finding 5).
- **Basis of awards** (s 4(1)-(4)): death or injury from an offence, or from an act that would have been one but for the offender's age, insanity or another excuse (s 4(1)(a)), or from assisting a police officer (s 4(1)(b)). Funeral expenses (s 4(1A)-(1B)), for conduct on or after 1 November 2015. The heads open to each kind of victim:
  - expenses;
  - future medical, dental (primary victim only), psychological or counselling services;
  - lost wages, including while caring for the primary victim;
  - pain and suffering;
  - a related victim's financial loss as a dependant of a primary victim who died;
  - the costs of claiming.
- **Conditions** (s 5(2), (3A), (4), (9), (10)):
  - criminal conduct proved on the balance of probabilities;
  - no award to a person who failed to help identify, apprehend or prosecute the offender;
  - an adequate civil remedy may be a ground to refuse, and amounts recovered must be taken into account (reported, not deducted: finding 22);
  - the law at lodgement;
  - the greater of the maxima at lodgement and at determination, with s 40B.
- **Exclusions** (s 6):
  - motor vehicles (the MAIB scheme);
  - exemplary or aggravated damages;
  - property;
  - matters paid or payable under a workers compensation law, head by head;
  - Medicare or health fund expenses.

  Also s 12: no award for conduct before the Act commenced.
- **Caps** (s 6A, reg 4):
  - the class maxima per particular criminal conduct, less what has already been awarded;
  - a higher maximum for a primary victim of a series of offences;
  - the funeral maximum, shared among all claimants;
  - future services, which may be paid above the cap;
  - the 2021-22 figures, indexed each later year by the Hobart CPI, never falling.
- **Deductions** (s 6B): penalties owed to the Crown, the compensation levy, unpaid compensation orders (Sentencing Act 1997 s 68, this Act s 7A). They come off the award and are treated as paid.
- **Deadlines** (s 7(1A)-(1D), (8), (9)):
  - 3 years from the offence;
  - for a victim under 18 at the time, 3 years after turning 18;
  - no limit where child sexual abuse is alleged;
  - extension for special circumstances (an input);
  - determination within 3 years of the application, with its extension.
- **Application contents** (reg 5): the subregulations that apply, as a checklist.

**Out:**

- Part 3 (ss 13-38, restraining, forfeiture and production orders) and the victims fund (s 38). These are the Director of Public Prosecutions' and a judge's powers over an offender's property.
- s 7A, recovery from the offender (provisional orders, objection within 28 days, confirmation as a fine). It is the offender's position, and an offender's seat was not asked for.
- Procedure and publicity: s 7(2)-(7) and (10), s 8 (proceedings in private, and the 5 penalty unit offence of publishing a report).
- s 5(3) (the victim's contributing behaviour: a discretion), s 5(5)-(7) (further applications, interim awards, conditions), s 9 (other remedies and the Treasurer's trust over later damages), s 10 (finality), s 11 (the Fund).
- reg 5(10) (optional evidence) and Schedule 1 (the declaration's wording).

## Read with the other encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Motor Accidents (Liabilities and Compensation) Act 1973 (Tas)**, `../../../motor-accidents-liabilities-and-compensation-act-1973/`, with its Regulations 2020: the MAIB no-fault scheme, to which s 6(1)(a) sends every death or injury "caused by or arising out of the use of a motor vehicle". Whether MAIB then pays is that Act's question; no encoding of it had reached `main` when this was written.
- **Workers Rehabilitation and Compensation Act 1988 (Tas)**, `../../../workers-rehabilitation-and-compensation-act-1988/`, with its Regulations 2021. It is Tasmania's "compensation law" under s 6(2), and it answers which heads are "paid, or ... payable" under it (this encoding's s 6(1)(d) input). The other States', the Territories' and the Commonwealth's employer compensation laws count too. No encoding of it had reached `main` when this was written.
- **Health Insurance Act 1973 (Cth)**, `subjects/au/health-insurance-act-1973/encodings/baseline-2026-10/`. Its question `Is a Medicare benefit payable for my service` (ss 10(1), 17, 19) answers whether an expense is "claimable under Part II" (s 6(1)(e)(i)). The registered health fund half (s 6(1)(e)(ii)) is not encoded anywhere in Commons (finding 25).
- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`. Its question `Is what I received compensation` (s 17(2), (2A), (2B)) answers no when the payment "is criminal injuries compensation". Section 17(2B) says "A payment under a law of the Commonwealth, a State or a Territory that provides for the payment of compensation for a criminal injury does not constitute compensation". (2C) defines a criminal injury as "a personal injury suffered ... as a result of the commission of an offence". This Act is such a law, so **an award under it is not "compensation" for the Social Security Act**: it triggers no compensation recovery and no lump sum preclusion period under Part 3.14, even for the lost wages heads (s 4(2)(c), (3)(d), (4)(d)), which would otherwise fall under s 17(2)(b).
  - (2B) tests the law the payment is made under, not each payment. So the encoding reads it to cover an award to a s 4(1)(b) helper too, although the helper's injury did not result from "the commission of an offence". That is a reading. It is not asserted, since the helper is "not covered" here (finding 1).
  - Going the other way, a workers compensation payment for the same injury is "compensation" under s 17(2)(b) and excludes the matching heads here (s 6(1)(d)).
  - The income tax treatment of an award is not checked.
- **Within this Act**, the funeral maximum (s 6A(1A)-(1B)) is separate from the victim maxima (s 6A(1)), so the same person can hold both (finding 4).

## What the Act turns out to say

1. **A person injured helping police, with no offence against them, has an award but no heads and no maximum.** Section 4(1)(b) allows compensation where a person "suffers injury ... in assisting a police officer in the exercise of the power to arrest a person or to take action to prevent the commission of a crime". Sections 4(2)-(4) list the matters for a primary, secondary or related victim only, and reg 4 prescribes maxima only for them. A "primary victim" is "a person against whom an offence is committed". A helper hurt in a fall, with no offence against them, fits no kind, so the encoding answers "not covered". A helper the arrested person assaults is a primary victim. Asserted (both).
2. **"Primary victim" needs an offence "committed", but s 4(1)(a) also covers acts excused by age or insanity.** Section 4(1)(a) extends awards to an act that "would have constituted an offence" but for the actor's age, insanity or other excuse. The definition of primary victim speaks only of "an offence ... committed". Read literally, the extension would found no award, since ss 4(2)-(4) speak only of the three kinds. The encoding reads the extension into the definition: an assault by a 9-year-old makes the person assaulted a primary victim. Asserted (as a reading: the one input carries both).
3. **The parent of a child victim is a secondary victim, the parent of an adult victim a related victim, with half the maximum.** "Secondary victim" (b) is "a parent, step-parent or guardian of a primary victim who was under 18 years of age at the time of the offence", and needs no injury of the parent's own. "Related victim" (b) is "a parent or step-parent of a primary victim who was over 18 years of age". In 2021-22 terms the first has $20 000, the second $10 000. The encoding reads "over 18" as "not under 18", so a parent of an 18-year-old is a related victim and there is no gap. A guardian of an adult primary victim is neither. Asserted.
4. **One person can be two kinds, and the Act does not say how their maxima combine.** A wife who saw her husband assaulted and was injured is a secondary victim (a) and a related victim (a). Section 6A(1) caps "the total amount ... awarded to a primary victim, a secondary victim or a related victim", without saying whether a person in two classes has one cap or two. The encoding answers each kind separately.
   Funeral expenses are expressly outside s 6A(1) ("not including any amount that may be payable under section 4(1A)"). So a brother of a murder victim who paid for the funeral may have up to the related victim maximum plus the funeral maximum: $11 245.50 + $11 245.50 = $22 491 on the test CPI. Asserted (the kinds and the sum).
5. **The defined term "dependant" is no longer used, and only a related victim has the dependency head.** Section 2 defines "dependant" ("wholly or mainly dependent upon the victim", including "any child of the victim born after his death"). Since s 4 was substituted in 2005, no provision in Part 2 uses it: s 4(4)(f) says "if the related victim was dependent on the primary victim". Whether "wholly or mainly" is read in is open, so dependence is a fact.
   The head belongs to related victims only. A grandchild wholly dependent on a murdered grandparent is not a related victim, so has no claim at all. A child born after the death is still a "child", and so a related victim. Asserted (the grandchild).
6. **Only a primary victim can claim future dental services.** Section 4(2)(b) names "medical, dental, psychological or counselling services"; s 4(3)(c) and (4)(c) omit "dental". Asserted.
7. **The workers compensation exclusion does not reach funeral expenses.** Section 6(1)(d) excludes "any matter referred to in section 4(2), (3) or (4)" paid or payable under a compensation law. Funeral expenses are under s 4(1A). A sister who received a workers compensation funeral benefit is not excluded from a funeral award, though s 5(4) makes the Commissioner take what she received into account. Asserted.
8. **The motor vehicle exclusion is total.** Section 6(1)(a) bars compensation "in respect of a death or injury caused by or arising out of the use of a motor vehicle". The words reach a primary victim deliberately run down, a witness injured by seeing it, and the person who paid for the funeral. Each is pointed to the MAIB scheme; whether it pays is that Act's question. Asserted.
9. **The workers compensation exclusion goes head by head.** Section 6(1)(d) excludes "any matter ... for which compensation has been paid, or is payable". A worker assaulted at work whose lost wages are paid by workers compensation keeps the expenses and pain and suffering heads. "Payable" covers what is payable whether or not it was claimed. Asserted (partial and whole).
10. **Time runs from the offence, not the death, and a funeral claim can be out of time before the death.** Section 7(1A) gives "3 years after the date of the relevant offence" for every application, including one for funeral expenses. A man stabbed on 1 January 2022 who died on 1 June 2025 leaves his funeral payer a period that ended on 1 January 2025, unless the Commissioner extends it (s 7(1C)). Asserted.
11. **The minors' extension turns on the applicant's own age, and a funeral payer who is not a victim never has it.** Section 7(1B) applies "If a primary victim, secondary victim or related victim is less than 18 years old at the time of the relevant offence". So a mother who is a secondary victim of her 14-year-old's assault has 3 years from the offence, though her son has until 3 years after he turns 18. A nephew, who is no kind of victim, has only s 7(1A) for the funeral. Asserted.
12. **No time limit for child sexual abuse, but s 12 still bars conduct before the Act commenced.** Section 7(1D) lifts the limits "in respect of an application ... that involves an allegation of child sexual abuse", and s 7(11)(b) applies this even where the old period had expired. But s 12 says "No award shall be made in respect of criminal conduct occurring before the commencement of this Act". The commencement was fixed by proclamation (s 1(2)), and its date is not in the deposit, so it is asked as a fact. Asserted.
13. **The indexed maxima ratchet.** Reg 4(2)(b) increases each year's maximum "by the percentage change", but (ii) keeps the preceding year's figure if the result would be lower. After a fall, the next rise is applied to the figure held. On the test CPI (average 100, 102, 107.1, 102, 107.1, 109.242 for 2020-2025), the primary victim maximum goes 30 000, 30 600, 32 130, 32 130 (held), 33 736.50, 34 411.23. Following the CPI from the base would give 30 000 × 107.1 / 100 = 32 130 in 2025-26, not 33 736.50. Asserted.
14. **Section 5(10)'s "greater of" in practice means "the maximum at determination".** A determination cannot precede its lodgement, and reg 4 never lets a maximum fall. So the maximum at determination is always at least the one at lodgement, while the 2021 Regulations stand. "The greater of" matters only for an application lodged before 15 December 2021 under the earlier regulations, which are not deposited (the encoding answers "at least" the later figure), or if the Regulations are amended to lower a figure. Section 40B(2) validates earlier determinations that exceeded the lodgement maximum. Asserted.
15. **Reg 4 does not say how to round.** Neither the percentage change nor the indexed maximum is rounded by the text, and reg 4(4) requires the Department to publish the maxima. The encoding does not round, so a published figure may differ by rounding. The test CPI was chosen to need none. Not asserted.
16. **Two separate offenders give two maxima; a series by one gives one larger one.** "Particular criminal conduct" (s 6A(2)) is a single offence, a series by the same offender, or a series by offenders acting in concert. A primary victim of a series has the higher maximum ($50 000 in 2021-22). A person assaulted on two occasions by two unrelated offenders has two particular criminal conducts, each with the single offence maximum. On the test CPI that is $33 736.50 twice, $67 473, against $56 227.50 for a series. Asserted.
17. **The maximum is a total for the conduct, not for the application.** Section 6A(1) caps "the total amount ... awarded ... in respect of any particular criminal conduct". An interim award (s 5(6)) or an earlier award counts against it. A $5 000 interim award leaves $28 736.50 of $33 736.50. Asserted.
18. **Deductions come off the award, after the cap.** Section 6B lets the Commissioner deduct from "an award" a pecuniary penalty owed to the Crown, a compensation levy, or an unpaid compensation order. The encoding caps first and then deducts, never below nothing, and the debt is "treated as paid" or "discharged" to that extent. A $2 000 award against a $3 000 order pays nothing and discharges $2 000 of the order. Asserted.
19. **For a series of offences, the Act does not say which offence's date starts the clock.** Section 7(1A) runs from "the date of the relevant offence". For a series by one offender (s 6A(2)(b)) the first and the last offence give different periods. The encoding takes the date the applicant gives. Not asserted.
20. **The periods are counted on readings.** "Within 3 years after the date of the relevant offence" (s 7(1A)) and "within 3 years of the date of the application" (s 7(8)) are read as ending on the same calendar day 3 years on. "3 years after he or she turns 18" (s 7(1B)) is read as ending on the 21st birthday. Where that day does not exist (29 February), the period ends on 28 February. The Acts Interpretation Act 1931, which may settle these, is not deposited. Asserted.
21. **The duty to decide within 3 years has no stated consequence.** Section 7(8) says an application "is to be determined within 3 years". The encoding's rule shows a late determination as a breach by the Commissioner. The Act gives the applicant no remedy for one, and "A decision of the Commissioner under this Act is final and no appeal lies therefrom" (s 10). Asserted by `#TRACE` only.
22. **"Take into account" is not "deduct".** Section 5(4) says the Commissioner "shall take into account any amount recovered ... by way of damages or compensation" or likely to be recovered. It does not say the amount comes off dollar for dollar, as s 6B says of deductions. The encoding reports the amount and the power to refuse, and leaves the assessed amount (an input) to reflect it. Asserted (the report).
23. **The Act states no place where the offence must occur.** "Offence" is "an offence that involves violence by one person against another", with no territorial words, unlike, for example, the NT Act's "occurs in the Territory". The encoding asks whether there was an offence. Whether it must be a Tasmanian offence is for the Acts Interpretation Act 1931 or the Commissioner. Not asserted.
24. **Applications lodged before 20 April 2023 are under an earlier s 7.** Section 5(9) applies the Act as in force when the claim was lodged. Section 7(1D) (no limit for child sexual abuse) and the amended s 7(1A) date from 20 April 2023, and the earlier text is not deposited. "Is my application in time" answers "not covered" for an earlier lodgement. Asserted.

25. **The health fund exclusion names a registration regime that has been replaced.** Section 6(1)(e)(ii) excludes expenses claimable "from a health benefits organisation registered under the National Health Act 1953 of the Commonwealth". To the encoder's knowledge, outside the deposits, private health insurers have been registered under the Private Health Insurance Act 2007 (Cth) since 2007. Read literally, (ii) may then catch no fund today. Whether a Tasmanian interpretation rule carries the reference over is not checked. The encoding asks whether expenses can be claimed "from your registered private health fund". Not asserted.

## Before relying on it

- An independent test pass against the authorised version on www.legislation.tas.gov.au.
- The Hobart CPI figures from the ABS, and the maxima the Department publishes under reg 4(4). Check the encoding's unrounded figures against the published ones (finding 15).
- The proclaimed commencement date of the Act (s 12), and the Acts Interpretation Act 1931 (Tas) for the counting of periods (finding 20), for "offence" (finding 23) and for "person".
- The Victims of Crime Assistance Regulations in force before 15 December 2021, for applications lodged before then (finding 14), and the earlier text of s 7 for applications lodged before 20 April 2023 (finding 24).
- Any published guidelines of the Commissioners or the Victim Assistance Unit, which may settle the readings in findings 2, 4, 5 and 19.
- Link to the MAIB and Workers Rehabilitation and Compensation encodings once they are on `main`, and check that their answers fit this encoding's s 6(1)(a) and (d) inputs.
- s 7A (recovery from the offender) and Part 3, if an offender's seat is wanted.
