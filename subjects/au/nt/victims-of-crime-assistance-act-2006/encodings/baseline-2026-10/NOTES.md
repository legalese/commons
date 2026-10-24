# Victims of Crime Assistance Act 2006 (NT): baseline encoding for the victim and for the person who paid for a victim's funeral

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. An injury item that is not a leaf of Schedule 3, Part 2 answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`voca-schedules.l4`**: the Regulations' tables as data. Schedule 1 (compensable violent acts, all 49 rows that name an offence, with the qualification column, and the two Part 4 rows that refer to other Parts as rules), Schedule 2 (offences that can found a category 1 or 2 psychological or psychiatric disorder) and Schedule 3, Part 2 (every leaf of the compensable injuries table, 142 rows, checked against the deposit by count and by the total of the amounts, with the reg 16(3)(ab) doubling mark), and regs 4, 6, 7, 7A and 14 that read them.
- **`voca-core.l4`**: the seat-neutral core, in the Act's own actors and terms ("a person", "the primary victim", "an eligible victim", "the applicant", "the Territory", "the Director", "the assessor"). Computations are functions: the categories of victim, the exclusions, the standard amounts, loss of earnings, the caps and the sharing of the $40 000 among secondary or family victims, funeral expense assistance. Where the text sets a duty with a period, there is a regulative rule (`DEONTIC`): three in all, covering seven sections.
- **`voca-seat.l4`**: the victim's seat, 24 questions.
- **`voca-seat-funeral.l4`**: the seat of the person who paid for a victim's funeral, 8 questions.

Each question has `@export` and a `@desc` on every input, grouped under `§§` headings. The seats build the core's records from plain answers and restate no rule. Where one answer depends on another question (whether the act is a violent act, its category, whether ss 17-18 exclude me), the `@desc` names that question.

No earlier encoding of this Act existed. The Northern Territory has no requirement ledger, so no ledger line is closed, and no scenario life covers the Territory, so every case is hypothetical.

## Edition

- **Act:** Victims of Crime Assistance Act 2006 (NT), reprint **REPV014**, as in force at **1 July 2025**, deposited at `../../registers/source-bundle/Victims-of-Crime-Assistance-Act-2006-NT-current-reprint-REPV014.txt`. Its last amending Act is the Domestic and Family Violence and Victims Legislation Amendment Act 2025 (No. 12 of 2025). By the endnotes, that Act amended ss 8, 24 and 61 only.
- **Regulations:** Victims of Crime Assistance Regulations 2007 (NT), reprint **REPV014R1**, as in force at **25 March 2024**, deposited at `subjects/au/nt/victims-of-crime-assistance-regulations-2007/registers/source-bundle/Victims-of-Crime-Assistance-Regulations-2007-NT-current-reprint-REPV014R1.txt`. It includes the Victims of Crime Assistance Amendment Regulations 2023 and the Schedule 1 and 2 substitutions of the Criminal Justice Legislation Amendment (Sexual Offences) Act 2023.
- **Transitional:** s 83 and reg 31 apply the 2023 amendments to every application not decided before 2 January 2024. The encoding applies the amended law throughout. An application decided before that date is outside it.

Figures the Act and Regulations fix are constants: $5 000 (s 27(5)), $40 000 and $10 000 (ss 38-40), $7 500 (ss 38(3), 39(3)), $15 000 (s 47D), 28 days (ss 29, 45, 46(10), 47(2)(c), 47F, 47G(2)(c)), 30 days and 6 months (ss 47H, 47K), 2 years (s 47C), 3 years (s 46), 75% (reg 23), 100%, 30% and 15% (reg 18), and the Schedule amounts. Three figures are not in any deposit, so they are **inputs**:

- the Northern Territory average weekly earnings less the notional income tax (reg 23(3));
- the NTCAT Act's time for applying for review;
- the other scheme's entitlement under the Motor Accidents (Compensation) Act 1979 or the Return to Work Act 1986.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `voca-schedules.l4`, `voca-core.l4`, `voca-seat.l4` | `voca-cases-victim.l4` | 209 written, 209 satisfied |
| `voca-schedules.l4`, `voca-core.l4`, `voca-seat-funeral.l4`, `voca-seat.l4` (mirror cases) | `voca-cases-funeral.l4` | 36 written, 36 satisfied |

In addition, 6 `#TRACE`s carry an `-- expect:` line. Five are breaches: by the Territory under ss 45, 29 and 47F, and by the person required to refund under ss 47 and 47G. One is an obligation still pending: the Director's s 47K duty to reopen. Each was read and matches its expectation.

`l4 run` on all six files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion. The funeral case file imports both seats, so it takes about two minutes to run.

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

**The Director and the assessor are officials, so they get no seat.** Their "must not award" (s 43), "must reduce" (s 42), "may reduce" (s 41), "must not approve" (s 47E(2)) and caps are the outcomes of functions that the person reads as "the most I can be awarded" or "no award, because …". The Territory's duty to pay within 28 days and the Director's duty to reopen are parties in the core's regulative rules, so the seats can say by when, but they have no seat of their own.

The mirror cases in `voca-cases-funeral.l4` ask the shared questions from both seats on the same facts and assert that the answers agree: closure, review of a s 47E or s 47G decision, and legal costs of a Division 5A application.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** Followed: the Regulations supply the standard amounts, the categories, the multiple-injury and existing-condition rules and the loss-of-earnings formula.
- **The actors the text names.** Followed: primary, secondary, family and related victims; the applicant; the individual who incurred the funeral costs; the person required to refund; the Territory; the Director; the assessor; the offender; NTCAT.
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
  - what each may apply for;
  - factor of aggravation (reg 7), pattern of abuse (reg 6) and domestic violence injuries (reg 5);
  - category 1 and 2 disorders (reg 15).

  Borrowed terms are asked as facts: "worker" (Return to Work Act), "domestic relationship" and "domestic violence order" (Domestic and Family Violence Act), "serious harm" and "offensive weapon" (Criminal Code), "indictable offence".
- **One case is one violent act and one person.** The sharing of the $40 000 among secondary or family victims needs the others' assessed totals, which are asked as figures.
- **The Act's own terms**, quoted in the comment above each rule. Quotation is under the licence ruling of 24 October 2026 (see `SOURCE-LICENSE.md`).
- **Machinery out**:
  - the counselling scheme's approvals (s 21) and assessors (s 24);
  - procedure (ss 33-36, 44);
  - guidelines, forms and delegations (ss 65-67);
  - protection and regulations (ss 68-70);
  - application contents (regs 8-12).

## Scope

**In:**

- **Definitions:** ss 4, 5 (violent act), 6 (injury) and 7, with regs 3-7 and 7A.
- **Categories and what each may apply for:** ss 9-16, and s 22 (counselling).
- **Exclusions:** ss 17-18, where a Motor Accidents (Compensation) benefit or Return to Work compensation is paid or payable for the same injury, whether or not a claim was made, with reg 13. The other scheme's entitlement is an input. Counselling stays open.
- **Death:** s 19.
- **Interim payments:** ss 25, 25B, 26, 27(5), 28 and 29. A primary or secondary victim in financial hardship, or a family victim of a homicide in hardship, may apply. There is no time limit, but none after the award is decided (s 26(2A)). The maximum is $5 000 in all (ss 25(3), 27(5)).
- **Awards:**
  - ss 29A, 31 (no time limit) and 37;
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
- **Payment and increase:** ss 45-46.
- **Refund:** s 47, as a regulative rule on the person required to refund. The notice gives at least 28 days, and the amount is a debt owing to the Territory.
- **Funeral expense assistance:** ss 47A-47G. The application is made within 2 years after the death, though the Director may accept it later. The amount is the lesser of the reasonable cost net of other payments and $15 000. The s 47G refund is a regulative rule.
- **Closure:** ss 47H-47K, when the applicant cannot be contacted.
- **Review:** s 48 and Schedule 1, NTCAT review: who may seek it, and of which decisions. The NTCAT time limit is in the NTCAT Act, which is not deposited, so it is an input.
- **Costs:** s 54, no legal costs beyond reasonable disbursements, and no counsel's fees.

**Out:**

- **Part 5 (ss 55A-59), recovery from offenders:** debt recovery notices, objections, court recovery and set-off. These are the Territory's rights against an offender, not the victim's, and an offender's seat was not asked for.
- **s 61 and reg 26, the levy:** it falls on offenders and on people who expiate offences, not on the victim. It is set in revenue units whose value is not deposited.
- s 60 (the Fund), s 62 (civil claims preserved), s 63 (offences), s 64 (inadmissibility).
- s 35(4) and s 36(3): the assessor may refuse an award if the applicant refuses an examination or information without reasonable excuse. This is a discretion, not encoded.
- s 5(6), on acts after an award notice, which are not related to earlier acts. The number of related acts is an input.
- s 55 and regs 24-25: review costs (80% of the Supreme Court scale, and when the Territory pays them).
- regs 8-12, 27-31: application contents, forms, approved examiners, transitional.
- Schedule 3's definitions ("functional impairment", TBSA). These are for the person, or the assessor, choosing the item.

The NT levies no land tax, but nothing in this Act turns on it.

## Read with the other encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Return to Work Act 1986 (NT)**, `../../../return-to-work-act-1986/encodings/baseline-2026-10/` (written in the same workflow, 24 October 2026). It answers whether the injured person is "a worker" and whether they are "entitled to compensation ... for the injury" (s 18(1)(b)), the facts behind this encoding's s 18 inputs. Reg 13 here presumes no entitlement while a Return to Work dispute is in mediation or proceedings. A Return to Work funeral benefit paid for the death is a payment "by an organisation" under s 47D(a) if the insurer pays it.
- **Motor Accidents (Compensation) Act 1979 (NT)**, `../../../motor-accidents-compensation-act-1979/encodings/baseline-2026-10/` (same workflow). It answers whether the injured person "is entitled to a benefit under the Motor Accidents (Compensation) Act 1979 for the injury" (s 17(1)(b)), whether or not they claimed it.
- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`. Its question `Is what I received compensation` (s 17(2), (2A), (2B)) answers no for "criminal injuries compensation". Section 17(2B) says a payment "under a law of ... a Territory that provides for the payment of compensation for a criminal injury does not constitute compensation", so an award or interim payment under this Act does not trigger compensation recovery or a lump sum preclusion period under Part 3.14. Going the other way, a Commonwealth "benefit, compensation, damages or other award" for the same injury or loss reduces an award here (s 42(2)(d)). So do Medicare or private health refunds for medical expenses (regs 9(b), 10(1)(a); s 42(2)(c)). The income tax treatment of an award is not checked here.
- **Within this Act**, the victim's seat and the funeral seat draw on the same core. A family victim's award (s 40) and funeral expense assistance (s 47D) are separate. Medical expenses "for the primary victim" (s 14(3)(c)) are a family victim's loss; funeral costs are not.

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
20. **The periods are counted on readings.** "Within 2 years after the death" (s 47C), "within 3 years after" payment or becoming an adult (s 46(1)) and "within 6 months of the date of the closure" (s 47K) are read as ending on the same calendar day, or on the month's last day where that day does not exist. So a 31 March closure can be reopened until 30 September, and a death on 29 February 2024 gives until 28 February 2026. The 30 days in s 47H run from "the date of the notice". The Interpretation Act 1978, which may settle these, is not deposited. Asserted.
21. **The Director's duty to reopen has no period.** Section 47K says the Director "must reopen" a closed application on a timely request, but sets no time. The regulative rule therefore has no `WITHIN`, and a trace 900 days after the request is still pending. Asserted by `#TRACE`. Not responding to a closure notice, or not asking to reopen, is no breach: the consequence is closure.
22. **The Regulations reprint is older than the Act reprint.** The Regulations reprint is at 25 March 2024; the Act reprint is at 1 July 2025. An amendment to the Regulations after 25 March 2024 (to a standard amount, say) is not in the deposit. Check the register's history before relying on a figure.

## Before relying on it

- An independent test pass. Check every Schedule 1 and Schedule 3 row against the PDF reprint, which is not deposited.
- A current Regulations reprint, if one has been published since 25 March 2024 (finding 22).
- The NTCAT Act's time limit for review, and the Interpretation Act 1978's rules for computing periods (finding 20).
- The ABS NT average weekly earnings figure and the notional tax method for reg 23, or a guideline under s 65 that fixes them (finding 19).
- Deposit the Victims of Crime Assistance guidelines (s 65), if any are published. They may settle the readings in findings 3, 4, 6 and 15.
- Part 5 (recovery from offenders) and the s 61 levy, if an offender's seat is wanted. The levy needs the value of a revenue unit, which is set outside these texts, deposited.
- Link to the Return to Work and Motor Accidents (Compensation) encodings once both are in, and check that their entitlement questions answer this encoding's s 17 and s 18 inputs.
