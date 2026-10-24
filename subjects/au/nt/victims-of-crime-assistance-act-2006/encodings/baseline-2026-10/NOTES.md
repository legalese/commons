# Victims of Crime Assistance Act 2006 (NT): baseline encoding for the victim, the person who paid for a victim's funeral, and the person on whom the victims levy is imposed

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. An injury item that is not a leaf of Schedule 3, Part 2 answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no human gate. An independent verification on 24 October 2026 found six issues; the fixes are findings 23-26 and the notes on issues 5 and 6 below.
**Not for public use as advice.**

It is written in layers:

- **`voca-schedules.l4`**: the Regulations' tables as data. Schedule 1 (compensable violent acts, all 49 rows that name an offence, with the qualification column, and the two Part 4 rows that refer to other Parts as rules), Schedule 2 (offences that can found a category 1 or 2 psychological or psychiatric disorder) and Schedule 3, Part 2 (every leaf of the compensable injuries table, 142 rows, checked against the deposit by count and by the total of the amounts, with the reg 16(3)(ab) doubling mark), and regs 4, 6, 7, 7A and 14 that read them.
- **`voca-core.l4`**: the seat-neutral core, in the Act's own actors and terms ("a person", "the primary victim", "an eligible victim", "the applicant", "the Territory", "the Director", "the assessor"). Computations are functions: the categories of victim, the exclusions, the heads of financial loss, the standard amounts, loss of earnings, the caps and the sharing of the $40 000 among secondary or family victims, each kind of award with its bars in order, the interim payment, funeral expense assistance, and the s 61 levy. Where the text sets a duty or a deadline with a period, there is a regulative rule (`DEONTIC`): six in all, for ss 29, 45, 46(10) and 47F (payment); ss 47 and 47G (refund); s 46(1) and (4) (an increased award); ss 47C and 47E(1) (funeral expense assistance); ss 47H(2)(b) and 47J (contact details or closure); and s 47K (reopening).
- **`voca-seat.l4`**: the victim's seat, 24 questions.
- **`voca-seat-funeral.l4`**: the seat of the person who paid for a victim's funeral, 8 questions.
- **`voca-seat-levy.l4`**: the seat of the person on whom the s 61 levy is imposed, 3 questions.

Each question has `@export` and a `@desc` on every input, grouped under `§§` headings. The seats build the core's records from plain answers and call the core for every rule: the sums of the heads of loss, the order of the bars, the reg 23 and interim payment conditions and the s 47E bars are core functions (finding 25). Where one answer depends on another question (whether the act is a violent act, its category, whether ss 17-18 exclude me, how much the levy is), the `@desc` names that question.

No earlier encoding of this Act existed. The Northern Territory has no requirement ledger, so no ledger line is closed, and no scenario life covers the Territory, so every case is hypothetical.

## Edition

- **Act:** Victims of Crime Assistance Act 2006 (NT), reprint **REPV014**, as in force at **1 July 2025**, deposited at `../../registers/source-bundle/Victims-of-Crime-Assistance-Act-2006-NT-current-reprint-REPV014.txt`. Its last amending Act is the Domestic and Family Violence and Victims Legislation Amendment Act 2025 (No. 12 of 2025). By the endnotes, that Act amended ss 8, 24 and 61 only; its s 14, which amended s 61 (the levy), commenced on 1 July 2025. A levy imposed before then may have been different.
- **Regulations:** Victims of Crime Assistance Regulations 2007 (NT), reprint **REPV014R1**, as in force at **25 March 2024**, deposited at `subjects/au/nt/victims-of-crime-assistance-regulations-2007/registers/source-bundle/Victims-of-Crime-Assistance-Regulations-2007-NT-current-reprint-REPV014R1.txt`. It includes the Victims of Crime Assistance Amendment Regulations 2023 and the Schedule 1 and 2 substitutions of the Criminal Justice Legislation Amendment (Sexual Offences) Act 2023. The first commit of this encoding also recorded the 24 October 2026 licence ruling in that subject's `SOURCE-LICENSE.md`, because the encoding quotes the Regulations.
- **Transitional:** s 83 and reg 31 apply the 2023 amendments to every application not decided before 2 January 2024. The encoding applies the amended law throughout. An application decided before that date is outside it.

Figures the Act and Regulations fix are constants: $5 000 (s 27(5)), $40 000 and $10 000 (ss 38-40), $7 500 (ss 38(3), 39(3)), $15 000 (s 47D), 28 days (ss 29, 45, 46(10), 47(2)(c), 47F, 47G(2)(c)), 30 days and 6 months (ss 47H, 47K), 2 years (s 47C), 3 years (s 46), 75% (reg 23), 100%, 30% and 15% (reg 18), 200, 150, 50, 1 000 and 40 revenue units (s 61(3), (6)), and the Schedule amounts. Four figures are not in any deposit, so they are **inputs**:

- the Northern Territory average weekly earnings less the notional income tax (reg 23(3));
- the NTCAT Act's time for applying for review;
- the other scheme's entitlement under the Motor Accidents (Compensation) Act 1979 or the Return to Work Act 1986;
- the value of a revenue unit (s 61), which is fixed outside these texts.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `voca-schedules.l4`, `voca-core.l4`, `voca-seat.l4` | `voca-cases-victim.l4` | 221 written, 221 satisfied |
| `voca-schedules.l4`, `voca-core.l4`, `voca-seat-funeral.l4`, `voca-seat.l4` (mirror cases) | `voca-cases-funeral.l4` | 40 written, 40 satisfied |
| `voca-schedules.l4`, `voca-core.l4`, `voca-seat-levy.l4` | `voca-cases-levy.l4` | 25 written, 25 satisfied |

In addition, 9 `#TRACE`s carry an `-- expect:` line. Five are breaches: by the Territory under ss 45, 29 and 47F, and by the person required to refund under ss 47 and 47G. Four are obligations still pending, because the Act sets them no period: the assessor's duty to decide an increased award applied for in time (s 46(4)), the assessor's duty to decide an award application kept open by contact details on day 30 (ss 47H(2)(b), 34(1)), the Director's duty to decide a funeral application made in time (s 47E(1)), and the Director's duty to reopen on a request on the last day (s 47K). Each was read and matches its expectation.

`l4 run` on all nine files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion; the day counts behind the regulative cases were also checked with a calendar outside L4. The funeral case file imports two seats, so it takes about two minutes to run.

## Seats

**1. The victim applying for assistance**: a primary, secondary, family or related victim of a violent act (`voca-seat.l4`). They ask:

- "Is what happened to me a violent act, and is it a compensable one?"
- "What kind of victim am I, and what may I apply for?"
- "Does my motor accident or workers compensation cover it instead?"
- "How much can I get as an interim payment or an award?"
- "What reduces or bars it?"
- "When must I be paid, and when must I repay?"
- "Can I seek review, and what can my lawyer charge?"

**2. The person who paid for a victim's funeral** (`voca-seat-funeral.l4`). The Act makes them "the applicant" (s 4) for funeral expense assistance, and puts a refund on them (s 47G). They ask:

- "Can I apply, and am I in time?"
- "How much can I get?"
- "When must I be paid, and when must I repay?"
- "Can I seek review, and what can my lawyer charge?"

**3. The person on whom the levy is imposed** (`voca-seat-levy.l4`): someone found guilty of an offence in the Territory and not imprisoned for it, someone who pays an infringement notice, or someone against whom an enforcement order is made (s 61(2)). The text puts a liability on them, and every driver who pays a speeding fine meets it, so it is part of the tax-and-benefits sample (finding 26). A company is one of the persons s 61(3)(c) names, and the seat asks whether the person is one. They ask:

- "Must I pay the levy, and how much?"
- "If I pay part of what I owe, how much goes to the levy?"
- "Have I paid enough for the levy not to stand in the way of my immunity from prosecution?"

**The Director and the assessor are officials, so they get no seat.** Their "must not award" (s 43), "must reduce" (s 42), "may reduce" (s 41), "must not approve" (s 47E(2)) and caps are the outcomes of functions that the person reads as "the most I can be awarded" or "no award, because …". The Territory's duty to pay within 28 days, and the Director's and the assessor's duties to decide and to reopen, are parties in the core's regulative rules, so the seats can say what follows and by when, but they have no seat of their own. A court's duty not to reduce a levy (s 61(9)) is part of the levy answer.

The mirror cases in `voca-cases-funeral.l4` ask the shared questions from both the victim's and the funeral seat on the same facts and assert that the answers agree: closure, review of a s 47E or s 47G decision, and legal costs of a Division 5A application. The levy seat shares no question with the other two.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** Followed: the Regulations supply the standard amounts, the categories, the multiple-injury and existing-condition rules, the loss-of-earnings formula and the exceptions to the levy.
- **The actors the text names.** Followed: primary, secondary, family and related victims; the applicant; the individual who incurred the funeral costs; the person required to refund; the person on whom a levy is imposed; the Territory; the Director; the assessor; the offender; NTCAT.
- **Judgments left to others are answered conditionally, as inputs.** Followed. These are:
  - financial hardship;
  - "reasonable" costs and a "reasonable time";
  - the assessor's satisfactions in s 43, s 40(8), s 46(5) and reg 16(1)(b);
  - the s 41 reduction and the reg 19 proportion;
  - "moderately" or "severely disabling and chronic" (reg 15);
  - "more than transient or trifling" (reg 5);
  - the Director's acceptance of a late funeral application (s 47C(2)).
- **The Act's own definitions are worked out from facts.** Followed. These are:
  - violent act and compensable violent act (ss 5, 7(1), reg 4, Schedule 1 row by row);
  - injury (s 6);
  - the four categories of victim (ss 9, 11, 13, 15);
  - what each may apply for, and each one's financial loss (ss 10(5), 12(6), 14(3));
  - factor of aggravation (reg 7), pattern of abuse (reg 6) and domestic violence injuries (reg 5);
  - category 1 and 2 disorders (reg 15);
  - "offence" for the levy (s 61(10)) and "adult" (s 4).

  Borrowed terms are asked as facts: "worker" (Return to Work Act), "domestic relationship" and "domestic violence order" (Domestic and Family Violence Act), "serious harm" and "offensive weapon" (Criminal Code), "indictable offence", "infringement notice" and "enforcement order" (Fines and Penalties (Recovery) Act 2001).
- **One case is one violent act and one person**, or for the levy one offence and one person. The sharing of the $40 000 among secondary or family victims needs the others' assessed totals, which are asked as figures.
- **The Act's own terms**, quoted in the comment above each rule. Quotation is under the licence ruling of 24 October 2026 (see `SOURCE-LICENSE.md`). One gloss comes from outside the deposit: that Part 12 of the Australian Road Rules (reg 26(a)(v)) is the rules on stopping and parking.
- **Machinery out**:
  - the counselling scheme's approvals (s 21) and assessors (s 24);
  - procedure (ss 33-36, 44);
  - the Fund (s 60);
  - guidelines, forms and delegations (ss 65-67);
  - protection and regulations (ss 68-70);
  - application contents (regs 8-12).

## Scope

**In:**

- **Definitions:** ss 4, 5 (violent act), 6 (injury) and 7, with regs 3-7 and 7A.
- **Categories and what each may apply for:** ss 9-16, and s 22 (counselling).
- **Exclusions:** ss 17-18, where a Motor Accidents (Compensation) benefit or Return to Work compensation is paid or payable for the same injury, whether or not a claim was made, with reg 13. The other scheme's entitlement is an input. Counselling stays open.
- **Death:** s 19.
- **Interim payments:** ss 25, 25B, 26, 27(5), 28 and 29. A primary or secondary victim in financial hardship, or a family victim of a homicide in hardship, may apply. There is no time limit, but none after the award is decided (s 26(2A)). The maximum is $5 000 in all (ss 25(3), 27(5)), and at most the financial loss it is for (s 27(2)(a), a reading).
- **Awards:**
  - ss 29A, 31 (no time limit) and 37;
  - the heads of financial loss: ss 10(5), 12(6), 14(3);
  - s 38 (primary victim: $40 000 less interim payments, financial loss capped at $10 000 less interim payments, compensable injuries only if their standard amounts total at least $7 500);
  - s 39 (secondary victims: the shared $40 000, proportional reduction, and the s 39(5)-(7) priority for those who saw the death);
  - s 40 (family victims: the shared $40 000, dependants first, s 40(8)-(9));
  - ss 41, 42 and 43.
- **Standard amounts:**
  - regs 14-16, with Schedule 1 and Schedule 3 as tables;
  - reg 15 with Schedule 2;
  - reg 18 (100%, 30% and 15%, and no more);
  - reg 19 (existing condition);
  - regs 20-22 (aids disregarded, a single remaining body part, burns and scarring, domestic violence injuries);
  - reg 23 (loss of earnings: 75% of the lesser difference, with the NT average weekly earnings as an input).
- **Payment and increase:** ss 45-46, with the s 46(1) application within 3 years as a regulative rule.
- **Refund:** s 47, as a regulative rule on the person required to refund. The notice gives at least 28 days, and the amount is a debt owing to the Territory.
- **Funeral expense assistance:** ss 47A-47G. The application is made within 2 years after the death, though the Director may accept it later; both are in a regulative rule with the Director's duty to decide (s 47E(1)). The amount is the lesser of the reasonable cost net of other payments and $15 000. The s 47G refund is a regulative rule.
- **Closure:** ss 47H-47K, when the applicant cannot be contacted: one rule for the 30 days after the notice (ss 47H(2)(b), 47J), and one for the 6 months after the closure (s 47K).
- **Review:** s 48 and Schedule 1, NTCAT review: who may seek it, and of which decisions. The NTCAT time limit is in the NTCAT Act, which is not deposited, so it is an input.
- **Costs:** s 54, no legal costs beyond reasonable disbursements, and no counsel's fees.
- **The levy:** s 61(2), (3), (6)-(10) and reg 26: who is levied, how many revenue units, the exceptions, the levy paid first out of a part payment, and no immunity from prosecution until the notice's amount and the levy are both paid. The value of a revenue unit is an input.

**Out:**

- **Part 5 (ss 55A-59), recovery from offenders:** debt recovery notices, objections, court recovery and set-off. These are the Territory's rights against an offender, not the victim's, and an offender's seat for them was not asked for.
- s 61(4) and (6)(b) (where the levy amount is recorded), and reg 30 (the Charles Darwin University by-law exception for offences before the 2013 amendment; finding 28).
- s 60 (the Fund), s 62 (civil claims preserved), s 63 (offences), s 64 (inadmissibility).
- s 35(4) and s 36(3): the assessor may refuse an award if the applicant refuses an examination or information without reasonable excuse. This is a discretion, not encoded.
- s 5(6), on acts after an award notice, which are not related to earlier acts. The number of related acts is an input.
- s 55 and regs 24-25: review costs (80% of the Supreme Court scale, and when the Territory pays them).
- regs 8-12, 27-29, 31: application contents, forms, approved examiners, transitional.
- Schedule 3's definitions ("functional impairment", TBSA). These are for the person, or the assessor, choosing the item.

The NT levies no land tax, but nothing in this Act turns on it.

## Read with the other encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Return to Work Act 1986 (NT)**, `../../../return-to-work-act-1986/encodings/baseline-2026-10/` (written in the same workflow, 24 October 2026). Its worker's questions `Am I a worker under the Return to Work Act` and `Is my injury compensable under the Return to Work Act 1986 (NT), and if not, why not` answer whether the injured person is "a worker" and whether they are "entitled to compensation ... for the injury" (s 18(1)(b)): the facts behind this encoding's s 18 inputs. Reg 13 here presumes no entitlement while a Return to Work dispute is in mediation or proceedings. A Return to Work funeral benefit paid for the death is a payment "by an organisation" under s 47D(a) if the insurer pays it. An offence against the Return to Work Act draws no levy (reg 26(a)(i)).
- **Motor Accidents (Compensation) Act 1979 (NT)**, `../../../motor-accidents-compensation-act-1979/encodings/baseline-2026-10/` (same workflow). Its injured person's question `Am I entitled to motor accident benefits` answers whether the injured person "is entitled to a benefit under the Motor Accidents (Compensation) Act 1979 for the injury" (s 17(1)(b)), whether or not they claimed it.
- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`. Its question `Is what I received compensation` (s 17(2), (2A), (2B)) answers no for "criminal injuries compensation". Section 17(2B) says a payment "under a law of ... a Territory that provides for the payment of compensation for a criminal injury does not constitute compensation", so an award or interim payment under this Act does not trigger compensation recovery or a lump sum preclusion period under Part 3.14. Going the other way, a Commonwealth "benefit, compensation, damages or other award" for the same injury or loss reduces an award here (s 42(2)(d)). So do Medicare or private health refunds for medical expenses (regs 9(b), 10(1)(a); s 42(2)(c)). The income tax treatment of an award, and of the levy, is not checked here.
- **Within this Act**, the three seats draw on the same core. A family victim's award (s 40) and funeral expense assistance (s 47D) are separate. Medical expenses "for the primary victim" (s 14(3)(c)) are a family victim's loss; funeral costs are not. The levy funds the Victims Assistance Fund (s 61(1)) from which awards are paid.

## What the Act turns out to say

1. **Two cross-references to s 14(2) mean s 14(3).** Sections 25B and 29A define interim payments and awards as payments for "the victim's financial loss mentioned in section 10(5), 12(6) or 14(2)". Section 14(2) only points to "the financial loss mentioned in subsection (3)(b) to (d)". Section 14(3) itself begins at paragraph (b): there is no (a) in this reprint. The encoding reads the family victim's financial loss as s 14(3)(b)-(d).
2. **Section 40(4) refers to a subsection (3) that does not exist.** It says the assessor must "after awarding any financial assistance under subsection (3), proportionately reduce each amount awarded", but s 40 has subsections (1), (2) and (4)-(9). The encoding applies the proportional reduction to the whole assessed total for the family victims.
3. **An interim payment lowers the caps. It is not deducted from the award.** Sections 38(1)-(2), 39(1)-(2) and 40(1)-(2) take interim payments off the $40 000 and $10 000 maximums. Section 42(2)(a) deducts only "an interim payment to which the applicant was not entitled". So a primary victim with an $8 000 loss and a $5 000 interim payment is awarded $5 000 more, $10 000 in all, on the words. Asserted. Whether the assessor nets the interim payment off the assessed loss is not in the text.
   The order of caps and reductions is not stated either. The encoding caps first (ss 38-40 limit what "may be awarded") and then applies ss 41 and 42, which reduce "an award". With $41 000 assessed, a $2 000 s 41 reduction and $6 000 of damages, that gives $32 000. Reducing first and capping after gives $33 000. Asserted (the $32 000).
4. **The $7 500 threshold can be met by injuries whose award is below it.** Sections 38(3) and 39(3) allow an award for compensable injuries "only if the total of the standard amount for the injury or injuries is at least $7 500". Section 4 defines "standard amount" as the amount prescribed "under section 7(3)", that is the reg 16(3) amount. The encoding therefore adds the prescribed amounts of the injuries that may be awarded: the three most serious (reg 18(3)), less those that reg 21 bars.
   A skull fracture ($5 000) and a deviated septum ($3 000) total $8 000, so the threshold is met, although reg 18 allows only $5 000 + 30% × $3 000 = $5 900. If the threshold were read against the reg 18 total, there would be no award for these injuries at all. Asserted.
5. **A compensable violent act is paid for the act or for the injuries, not both.** Section 10(4)(a) gives the primary victim an award for "(i) the mere commission of the violent act; or (ii) one or more compensable injuries". The award question asks which. A category 1 act is worth $10 000. The injuries can be worth more, so the choice matters. Asserted (both forms).
6. **Schedule 1 rows overlap, and the Regulations do not say which wins.** An aggravated s 208AB offence is in Part 1, which has no qualification, and also in Part 2 ("If a factor of aggravation applies"). The same is true of an attempt at s 208H with aggravation and of old s 188 with a weapon. The encoding takes the highest Part. Asserted.
7. **Attempts sit in a lower category, despite s 5(7).** Section 5(7) says "a person who attempts to commit a criminal act is taken to have committed the criminal act". Regs 4(2) and 7A say that, "despite section 43BJA of the Criminal Code", a Schedule reference to an offence does not include an attempt. The Schedule then lists attempts separately: an attempt at s 208H is category 1 ($10 000) and the completed offence category 2 ($20 000). An attempt at s 186B is category 2, the completed offence category 3. The encoding follows the Schedule. Whether a regulation can narrow s 5(7) for this purpose is not tested. Asserted.
8. **Schedule 2 cites an Act by the wrong year.** Its last heading is "Criminal Code as in force before the commencement of section 10 of the Criminal Code Amendment (Property Offences) Act 2023". The s 196 row and the Regulations' endnotes name the Criminal Code Amendment (Property Offences) Act **2022** (No. 24 of 2022, commenced 30 April 2023). The encoding reads the heading as the 2022 Act, and applies the old s 211(1) row to offences before 30 April 2023.
9. **An unclaimed entitlement shuts the door.** Sections 17(1)(b) and 18(1)(b) exclude the injured person if entitled to a motor accidents benefit or Return to Work compensation "regardless of whether the injured person has made a claim". Reg 13 helps only a worker who did claim, whose employer disputed liability, and whose dispute is in mediation or proceedings and undecided. Once Return to Work compensation has been paid (s 18(1)(a)), the presumption no longer helps. Asserted.
10. **The exclusions reach secondary and family victims in full.** Under ss 17(3) and 18(3), a person who "would ... be a secondary victim or family victim of the violent act against the injured person is not eligible for an interim payment or award in connection with the violent act". So a child who saw a parent deliberately run down gets counselling only, even for the child's own psychological injury, which the parent's motor accidents benefit does not cover. Asserted.
11. **Funeral expense assistance is outside ss 17 and 18.** Those sections speak only of "an interim payment or award". A person who paid for the funeral of someone killed in a motor accident that was an offence, or killed at work, can still apply (s 47B). What a motor accidents or workers compensation insurer paid for the funeral comes off under s 47D(a), as "amounts that are paid by an organisation". Asserted.
12. **The cap on legal costs does not reach interim payment applications.** Section 54 limits a lawyer's recovery to reasonable disbursements, without counsel's fees, only for "an application under Division 3, 5 or 5A": awards, increased awards (s 46) and funeral expense assistance. Division 2, interim payments, is not named. Asserted.
13. **Some decisions cannot be reviewed.** An interim payment decision "is final and is not subject to any review or appeal" (s 28(1)), but a refusal does not stop an award application (s 28(2)). A closure under s 47J is not in Schedule 1; the remedy is a request to reopen within 6 months (s 47K), or a new application. Asserted.
14. **A refund notice must give at least 28 days.** Sections 47(2)(c) and 47G(2)(c) require the notice to state a time "which must be at least 28 days after receipt of the notice". The encoding gives the person the longer of the notice's time and 28 days, so a 14-day notice still leaves 28. That is a reading. Asserted, as a fulfilled refund on day 28 and a breach on day 30.
15. **The $15 000 funeral cap is read as one cap per funeral.** Section 47D sets the maximum "payable in relation to a primary victim's funeral". The encoding shares the $15 000 among everyone paid for the same funeral, and also nets each applicant's own earlier payments (s 47B(4)). If the cap were per applicant, two payers could receive $30 000. Asserted (the $6 000 case).
16. **Doubling a $40 000 item changes nothing.** Reg 16(3)(ab) doubles the named items "that [occur] on each side of the body", and reg 20(2) treats an injury to a sole remaining eye or limb as an injury to both. Loss of both eyes is therefore a standard amount of $80 000, which s 38(1) caps at $40 000. Doubling matters only for items of $20 000 or less. Asserted.
17. **A psychological or psychiatric disorder has a standard amount only after a listed offence.** Item 12 of Schedule 3 is for "category 1" and "category 2" disorders, and reg 15 defines both by the offence: one specified in Schedule 1 or 2. A severely disabling category 2 disorder can also come from domestic violence injuries.
   A current common assault (s 188) is in neither Schedule, so a chronic disorder it causes has no item 12 amount. A moderately disabling disorder from domestic violence injuries without a listed offence has none either. Whether the assessor may treat such a disorder as "similar to" a listed injury (reg 16(1)(b)) is left to the assessor. Asserted.
18. **A late report bars an award even if it came before the decision.** Section 43(b) bars an award if the act "was not reported to a police officer within a reasonable time after its occurrence". Section 43(c) separately bars it if not reported "before the date the assessor decides". Each is excused only if "the assessor is satisfied circumstances prevented the report being made". Asserted.
19. **Reg 23's "average weekly earnings" cannot be worked out from the deposit.** It is the ABS figure for NT full-time adult ordinary time earnings "less a notional deduction for income tax", and the Regulations do not say how to compute the notional deduction. One input carries both. When net earnings during the period exceed the comparison figure, the encoding gives nothing for the week; the Regulations do not say. Asserted.
20. **The periods are counted on readings.** "Within 2 years after the death" (s 47C), "within 3 years after" payment or becoming an adult (s 46(1)) and "within 6 months of the date of the closure" (s 47K) are read as ending on the same calendar day, or on the month's last day where that day does not exist. So a 31 March closure can be reopened until 30 September, and a death on 29 February 2024 gives until 28 February 2026. The 30 days in s 47H run from "the date of the notice", and the closure is read as taking effect on the 30th day (s 47J(2): "On the expiry of the period"). Each regulative rule counts days from its own start to that last day. The Interpretation Act 1978, which may settle these, is not deposited. Asserted.
21. **The duties to decide and to reopen have no period.** Section 47K says the Director "must reopen" a closed application on a timely request, but sets no time; nor do ss 46(4) and 47E(1) for the decisions on an increased award and on funeral expense assistance, nor s 34(1) beyond "as soon as practicable". Those obligations in the regulative rules therefore have no `WITHIN`, and a trace long after the request is still pending. Asserted by `#TRACE`. Not giving contact details, not applying in time, and not asking to reopen are no breach: the consequences are closure or the loss of the right to apply.
22. **The Regulations reprint is older than the Act reprint.** The Regulations reprint is at 25 March 2024; the Act reprint is at 1 July 2025. An amendment to the Regulations after 25 March 2024 (to a standard amount, or to the levy exceptions, say) is not in the deposit. Check the register's history before relying on a figure.
23. **Correction (24 October 2026): the s 47K six months now run from the date of the closure, in a rule of their own.** The first version chained the request to reopen under the `LEST` of the 30-day contact details rule. L4 starts a rule under `LEST` at the first event or `WAITUNTIL` after the deadline, and does not match that event against it. So the 6 months ran from whenever a trace first showed the closure, not from the date of the closure. With the case file's own `WAITUNTIL 31`, a request on 1 October 2026 after a 31 March closure still obliged the Director, one day too many; a request that was the first event after the notice was lost; and after `WAITUNTIL 100` a request in December still obliged the Director. The function behind the seat's closure question was right throughout (1 October was already asserted as too late); the rule was wrong.
   Now ss 47H(2)(b) and 47J are one rule, clocked from the date of the notice: contact details within 30 days keep the application to be decided by the Director or the assessor. Section 47K is another, clocked from the date of the closure and ending on the last day to ask. Asserted: for a 31 March 2026 closure, a request on day 183 (30 September) obliges the Director, one on day 184 (1 October) or day 251 (7 December) does not, and a request that is the first event, on day 70, counts. No rule now chains a second deadline under `LEST`.
24. **Correction (24 October 2026): the two deadlines on the applicant are now regulative rules.** Section 47C(1) ("an application under section 47B must be made within 2 years after the death") and s 46(1) ("may apply ... within 3 years") were dates and yes-or-no answers only, while these notes said every duty with a period had a rule. Both are now rules. Applying in time puts a duty to decide on the Director (s 47E(1)) or the assessor (s 46(4)). Missing the deadline is no breach. After s 47C's 2 years the applicant may still apply, and the Director must still decide, because s 47E(1) speaks of any "application under section 47B" and s 47E(2)(b) bars only approval. After s 46's 3 years there is no right to apply. Asserted, with the day counts worked by hand (an adult paid on 15 March 2026: day 1096; a child paid on 1 February 2026 and born 10 June 2012: day 2686; a death on 10 May 2025: day 730).
25. **Correction (24 October 2026): the seats now call the core for every rule.** The first version did these inside the seats:
    - summed the heads of financial loss (ss 10(5), 12(6), 14(3));
    - checked the reg 23(1) category, the s 14(3)(b) dependency and the s 14(3) death bar;
    - ordered the s 37(1), ss 17-18, s 40(8) and s 43 bars;
    - capped the interim payment at the loss;
    - compared the s 46(1) date;
    - ordered the s 47E(2) bars.

    Those are now core functions (`the s 10(5) financial loss`, `the s 12(6) financial loss`, `the s 14(3) financial loss`, `the award to a primary victim` and its secondary and family counterparts, `the interim payment answer for`, `the reg 23 answer for`, `the application for an increased award is in time`, `the s 47E answer for`, `is a primary victim who died as a direct result of the act`). No answer changed, and every earlier assertion still holds. The choice of what a primary victim's award is for is now worded in the Act's terms (`financial loss only`, `the mere commission of the compensable violent act, with financial loss`, `compensable injuries, with financial loss`), which changes that input's values.
26. **Correction (24 October 2026): the s 61 levy is in.** The first version left the levy out, partly because the value of a revenue unit is not deposited. The brief makes a missing amount an input. The levy is a Territory charge on anyone who pays an infringement notice or is fined in the Territory, so it belongs in the tax-and-benefits sample:
    - 40 revenue units on an infringement notice or an enforcement order (s 61(6));
    - for a person found guilty and not imprisoned (s 61(3)): 200 for an adult on indictment, 150 for an adult otherwise, 50 for a child, and 1 000 for a body corporate.

    It now has its own seat. Asserted, at a hypothetical $1.25 a revenue unit.
27. **The levy on an infringement notice is the same for a child as for an adult.** Section 61(6) sets 40 revenue units for s 61(2)(b) and (c) without the age distinction of s 61(3). Asserted.
28. **Reg 26 skips a paragraph, and an endnote names an instrument the list does not.** Reg 26(a) runs (i) to (vii), then (ix): there is no (viii) in the reprint. Reg 30, which limits the (ix) exception for Charles Darwin University by-laws to later offences and notices, is noted as "ins No. 40, 2013", but the list of legislation names only No. 42, 2013 (commenced 19 December 2013), which amended reg 26. Reg 30 is out of scope; the encoding applies the (ix) exception without it.
29. **Reg 26(b) is read to reach an enforcement order, and reg 26(c) only a finding of guilt.** Reg 26(b) excepts "a person issued a notice under a law ... specified in paragraph (a)", not only one who pays it. So a person against whom an enforcement order is made for an unpaid parking notice pays no levy either. Reg 26(c) excepts "a person found guilty of an offence prosecuted by a local government council", so it is read with s 61(2)(a) only. Where two exceptions apply, the answer names the first. Readings. Asserted.
30. **Part of a payment goes to the levy first.** Section 61(8): money paid by a person levied under s 61(2)(b) "must be initially appropriated towards meeting the person's liability for the levy". Section 61(7): no immunity from prosecution "unless the amount specified in the infringement notice or enforcement order and the levy ... are paid". So a person who pays only the amount on a $300 notice, with a $50 levy, has paid the levy and is $50 short on the notice. Asserted.

## Before relying on it

- An independent test pass. Check every Schedule 1 and Schedule 3 row against the PDF reprint, which is not deposited.
- A current Regulations reprint, if one has been published since 25 March 2024 (finding 22).
- The NTCAT Act's time limit for review, and the Interpretation Act 1978's rules for computing periods (finding 20).
- The ABS NT average weekly earnings figure and the notional tax method for reg 23, or a guideline under s 65 that fixes them (finding 19).
- Deposit the Victims of Crime Assistance guidelines (s 65), if any are published. They may settle the readings in findings 3, 4, 6 and 15.
- For the levy: the value of a revenue unit for each financial year; the Fines and Penalties (Recovery) Act 2001, for "infringement notice", "enforcement order" and the immunity s 61(7) qualifies (finding 29); and a check of the gloss that Part 12 of the Australian Road Rules is the rules on stopping and parking.
- Part 5 (recovery from offenders), if an offender's seat for it is wanted.
- A case run by hand through this encoding and the Return to Work and Motor Accidents (Compensation) encodings together, for one person injured by a crime at work or on the road (the questions to use are named under "Read with the other encodings"; cross-folder IMPORT is not possible).
