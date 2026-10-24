# Victims of Crime (Financial Assistance) Act 2016 (ACT): baseline encoding for the applicant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. An act before 1 July 2016, and the parts of the Act left out, answer an explicit `not covered` value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`vocfa-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms: the applicant, the assisted person, the commissioner, a primary victim, a related victim, a homicide witness. Computations (who is a victim and of which class, the maximum, each payment, the reductions, the funeral payment, the repayment amount, the deadlines) are functions. Where the text says "must", "may" or "must not", or sets a time, there is a regulative rule (`DEONTIC`): ten in all.
- **`vocfa-seat.l4`**, the applicant's seat. It asks 23 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed to keep. No requirement ledger covers the ACT, so no ledger line is closed.

## Edition

- **Act:** Victims of Crime (Financial Assistance) Act 2016 (A2016-12), Republication No 10 (R10), effective 26 November 2025, last amended by A2025-29, as deposited at `../../registers/source-bundle/A2016-12.txt`.
- **Regulation:** Victims of Crime (Financial Assistance) Regulation 2016 (SL2016-10), Republication No 11 (R11), effective 1 July 2026, last amended by SL2026-8, as deposited at `../../../victims-of-crime-financial-assistance-regulation-2016/registers/source-bundle/SL2016-10.txt`. It holds every dollar figure: reg s 5 (maximum totals), s 6 and table 6 (immediate need), s 7 and table 7 (economic loss), s 8 and table 8 (recognition payments for a primary victim), ss 9 and 10 (class A and B recognition payments), s 11 (funeral) and s 12 (lawyers' costs).
- **Indexation.** Section 25 requires the s 24, s 28, s 29 and s 30 amounts to be amended each year in line with the Canberra CPI, and s 97 the s 96 amounts in line with the WPI. Both are **taken as already reflected in R11**, which SL2026-8 amended for 1 July 2026 (see finding 20). The index figures themselves are not deposited and are not computed.
- Both texts are the register's unauthorised DOCX conversions; the authorised PDFs are named in the meta files.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vocfa-core.l4`, `vocfa-seat.l4` | `vocfa-cases-applicant.l4` | 147 written, 147 satisfied |

In addition, 9 `#TRACE`s carry an `-- expect:` line: four breaches (by the commissioner under s 45 (4), by the assisted person under s 64 and under s 65 with s 67 (3), and by the applicant's lawyer under s 96) and five obligations still pending. Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the Act and the Regulation, with the arithmetic in the comment above the assertion.

## Seat

**The applicant**: a primary victim, a class A, B or C related victim, or a homicide witness; and, for part 4, the person who has paid or must pay the funeral of a primary victim killed by homicide. They ask:

- Am I a primary victim, a class A, B or C related victim, or a homicide witness?
- Which payments can I apply for, and what is the most I can receive in total?
- What can I be paid for an immediate need, for each kind of economic loss, and as a recognition payment for this offence?
- What evidence do I need, and by when must I apply?
- Can I get funeral expenses?
- If I later receive compensation for the same act, what must I tell the commissioner, and might I have to repay?

The commissioner is an official, so has no seat. The commissioner's duties (the s 33 and s 55 notices, the s 45 notice and decision, the s 66 and s 67 notices) appear in the core only as what the applicant is owed, in regulative rules with the commissioner as a party. The s 96 duty is on the applicant's lawyer; it is encoded as what the applicant can be charged (a function and a prohibition), with no seat for the lawyer.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** That is Regulation R11. Followed.
- **The actors the text names:** the applicant, the assisted person, the commissioner, the lawyer. Followed.
- **Judgments left to others are answered conditionally, as inputs:** whether an expense is reasonable (s 26 (2)) and what services are available (s 46 (2)), so every amount is "the most that can be paid"; the s 45 (1) (b) to (e) findings; the contributory-conduct reduction (s 47 (2) (c)); the s 32 (2) extension, answered as "late, but the commissioner may extend if …"; whether the agency is one the commissioner's guidelines list (s 31 (6)); whether appropriate counselling was available under the victims services scheme (table 7 item 1); whether the applicant can afford emergency treatment (table 6 item 4); whether the harm was a "direct result" (s 11).
- **The Act's own definitions are worked out from facts:** act of violence (s 7), injury (s 9), homicide (s 10), primary victim (s 11), the three classes of related victim (ss 13 to 15), homicide witness (s 16), close family member (s 17), family member (s 15 (2)), sexual offence, offence against the person and schedule 1 offence (dictionary), family violence offence (s 9 (2)), special reporting class victim (s 31 (4)), the repayment amount (s 62). **Departures:** "relevant person" and "dependant" are the Act's own dictionary terms, but each is asked as one fact, with the definition in its `@desc`: "relevant person" turns on the Legislation Act's domestic partner, the Family Violence Act's intimate partner and the dictionary's long list of relatives, and "dependant" on economic support. Borrowed terms are asked as facts: domestic partner (Legislation Act s 169), intimate partner (Family Violence Act 2016 s 10), mental illness and mental disorder (Mental Health Act 2015), the age of criminal responsibility (Criminal Code s 25), and whether Crimes Act 1900 s 66 (1) (b) applies.
- **One case:** one application by one person about one act of violence (related acts treated as one under s 44, with the day of the most recent act). A person who is both a primary victim and a related victim of the same act says which their application is about (`my application is about`); s 24 sets the maximum "for an application".
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** pts 6 to 8, and the review procedure of pt 9 beyond its deadlines.

## Scope

**In:**

- pt 2: ss 7, 9, 10, 11, 12 to 15, 16, 17, with schedule 1 (div 1.2.1 items 1 to 7 one by one; div 1.2.2 as one choice) and the dictionary's definitions listed above
- pt 3 div 3.1: ss 18 to 23
- div 3.2: s 24 with reg s 5; s 25 as reflected in R11
- div 3.3: s 26 with reg s 6 and table 6; s 27 with reg s 7 and table 7; ss 28 to 30 with reg ss 8 to 10 and table 8
- div 3.4: s 31 (requirements and evidence, special reporting class), s 32 (time, and the extension as a conditional answer), s 33 (notice)
- div 3.6: s 45 (as findings, with the 14-day reply), s 47 (as amounts)
- pt 4: ss 51 to 55 and s 60, with reg s 11
- pt 5: s 62, s 64 (with the offence), s 65, s 66, s 67
- pt 9: s 92 (2) and schedule 2, for the applicant's deadline to seek reconsideration; s 67 (3) (b) for the ACAT review of a repayment direction
- pt 10: s 96 with reg s 12; s 97 as reflected in R11

**Out, each answering a `not covered` value that a test asserts:**

- recovery from the offender (pt 6)
- the victims financial assistance levy on convicted offenders (pt 7)
- administration, the commissioner's functions, and secrecy (pt 8)
- the review procedure of pt 9 beyond the deadlines, including the ACAT's time limit for reviewing s 44 and s 45 decisions, which is in the ACT Civil and Administrative Tribunal Act 2008 (not deposited)
- applications about criminal injuries before 1 July 2016 (s 98): any act before that day
- the commissioner's guidelines (s 87, not deposited)

**Out, not reached by any question:** division 3.5 (the commissioner's powers to ask for information), ss 34 to 37 and 56 to 59 (withdrawal, amendment, lapse), s 42 (time for deciding), s 44 (related acts: the applicant gives the most recent day), s 46 beyond the amounts, s 48 and s 61 (how payment is made), division 3.7 (variation), s 63 (suspension), s 68 (death before repayment), s 95A (admissibility), ss 99 to 101.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here and not in code.

- **Social Security Act 1991** (`../../../../social-security-act-1991/`, encoded at `encodings/baseline-2026-10/`). The deposited compilation's s 17 (2B) says "A payment under a law of the Commonwealth, a State or a Territory that provides for the payment of compensation for a criminal injury does not constitute compensation for the purposes of this Act", and (2C) defines a criminal injury as "a personal injury suffered, or a disease or condition contracted, as a result of the commission of an offence". So an economic loss payment for lost earnings under this Act should not set off the compensation recovery provisions (pt 3.14) that a workers' compensation or civil damages payment for the same injury would. Whether a payment under this Act counts as income or an asset for the income and assets tests is not settled by that subsection, and is not answered here.
- **Income Tax Assessment Act 1997** (`../../../../income-tax-assessment-act-1997/`, encoded at `encodings/baseline-2026-10/`). Section 118-37 (1) (a) disregards a capital gain or loss from "compensation or damages you receive for … any wrong, injury or illness you or your relative suffers personally". Whether a payment for lost earnings (table 7 item 6) is ordinary income under s 6-5 is a question for that encoding, not this one.
- **The ACT's own other benefits.** A workers' compensation payment (Workers Compensation Act 1951) or a motor accident benefit (Motor Accident Injuries Act 2019) for the same act is an "associated payment" here (dictionary): it reduces the assistance if received first (s 47 (1) (a)) and must be reported, and may have to be repaid, if received afterwards (ss 64 to 67).

## What the Act turns out to say

1. **Amending Bills are pending.** The jurisdiction README records proposed amendments to the Act by the Victims of Crime Legislation Amendment Bill 2026, the Crimes (Coercive Control) Amendment Bill 2026 and the Family, Personal and Sexual Violence Legislation Amendment Bill 2025, and to the Regulation by the first of these. This encoding is of R10 and R11 as deposited. Any of them could change the answers.
2. **The Regulation prescribes no further offence and no aggregate for economic loss.** Section 7 (1) (b) (ii) admits "an offence prescribed by regulation", and s 27 (2) (d) allows a maximum "of all economic loss payments". Regulation R11 prescribes neither. Only the schedule 1 offences make an act of violence, and only the item caps in table 7 and the s 24 maximum limit economic loss: medical expenses of $12,000 are payable in full, and Mia's $49,500 of economic loss is limited only by the $67,959 maximum. Asserted.
3. **Intimate image abuse is a schedule 1 offence but not a "sexual offence".** The dictionary defines a sexual offence as one in schedule 1, div 1.2.1, items 2, 4 or 5; intimate image abuse is item 3. So its victim is not a special reporting class victim on that ground (s 31 (4) (a)). A sense of violation alone is not an injury (s 9 (1) (c)) unless the offender is a relevant person, which makes it a family violence offence (s 9 (2)). And table 8's sexual-offence items do not reach it. Asserted.
4. **A dependent brother or sister of a person killed fits no class of related victim.** Class A needs a close family member or intimate partner (s 13), and a sibling is not a close family member (s 17). Class C needs a family member who is financially independent (s 15 (1) (a)). A dependent sibling who was not the deceased's ward is neither. A grandparent, aunt or cousin fits no class either. Asserted.
5. **A related victim cannot be a homicide witness.** Section 16 excludes "a primary victim, a related victim or a perpetrator". A partner who saw the killing and was traumatised by it applies as a related victim, not for their own shock. Asserted.
6. **The family-violence cap can sit below the related victim's own recognition payment.** Reg s 5 (2) sets $13,590 for any application "only" about a schedule 1 div 1.2.2 offence, whatever the class. A dependent child of a woman killed in an arson by her former partner is a class A related victim, with a recognition payment of $27,183 (reg s 9), but a maximum of $13,590. Asserted.
7. **A death in a division 1.2.2 offence is not a homicide.** Section 10 requires murder, manslaughter or culpable driving causing death. In the arson case there are related victims (ss 13 to 15 need only a death), but no homicide witness (s 16) and no funeral expense payment (s 51 needs "a primary victim who died as a result of homicide"). Asserted.
8. **The $10,000 for immediate needs is per act of violence, not per applicant.** Reg s 6 (4): "The maximum aggregate amount of all immediate need payments that may be made for a single act of violence is $10 000." After $7,000 to one family member, another can get at most $3,000 for the same death. The input asks for payments already made to anyone. Asserted.
9. **A homicide witness's economic loss is narrow.** Table 7 makes items 3 to 8 "not available for a homicide witness" and item 9 "only available for a primary victim". That leaves counselling (if not available under the victims services scheme) and the costs of applying. Table 6 item 4 (emergency medical costs) is not available to them either. Asserted.
10. **Two table conditions are run together in the deposited text.** Table 6 item 4, column 3, reads "only available if applicant does not have financial ability to pay for treatment or service not available for homicide witness"; table 7 item 7 likewise. Each is read as two conditions. Table 7 item 7 counts a parent's or carer's expenses "as part of the maximum amount prescribed for the primary victim under s 5". On a primary victim's application that is what the encoding does. On a related victim's application (a parent of a child who was killed) the encoding counts them within the applicant's own maximum, because the primary victim makes no application. That is a reading.
11. **Only a primary victim can be a special reporting class victim, and not for a recognition payment.** Section 31 (4) speaks of "a primary victim". Under s 31 (2) (d) (ii) the alternative evidence (reports to 2 of the listed bodies, or to a government agency and a practitioner) is open only where "the application does not include a claim for a recognition payment". A 16-year-old abused by her coach can claim economic loss on reports to the Directorate and a counsellor, but needs a police report for a recognition payment. Asserted.
12. **An offender under the age of criminal responsibility: no report needed.** Section 31 (3) excuses only "the requirement under subsection (2) (d) (i)". Because (2) (d) is "(i) … or (ii)", the encoding reads (d) as met without evidence of any report. That is a reading. Asserted.
13. **A child has until three years after turning 18.** Section 32 (1) runs from "the last occurring" of the act and the 18th birthday. READING: "within 3 years of" a day ends on its third anniversary, and 29 February becomes 28 February in a common year. The Legislation Act 2001, which governs periods of time, is not deposited. Asserted.
14. **There is no power to extend the time for a funeral expense payment.** Section 54 says "must be made within 3 years after the day of the death". Part 4 has nothing like s 32 (2), and s 60 (2) applies divisions 3.5 and 3.6 only, not s 32. An application one day late gets nothing. Asserted.
15. **Reductions come off after the maximum.** Section 46 (2) (d) reduces "the amount" decided, and s 24 caps what "may be given". READING: the cap first, then the s 47 reduction. For Mia, $69,373 of claims is capped at $67,959; less $2,500 of insurance, that leaves $65,459, not the $66,873 that reducing first would give. A funeral insurance payment of $3,000 likewise comes off the s 53 amount: $8,000 − $3,000 = $5,000, not the lesser of $8,000 and $11,400 − $3,000. Asserted.
16. **Section 45 (1) (d) disqualifies only a related victim.** A finding that the act was related to a serious crime by the primary victim does not touch the primary victim's own application. READING: through s 60 (2), paras (b), (c) and (e) apply to a funeral application, and (d) does not, since a funeral applicant is not "claiming financial assistance as a related victim". Asserted for the primary victim.
17. **Every later associated payment must be reported, even one for different harm.** An "associated payment" is any amount "paid to the applicant … as a result of an act of violence" (dictionary). Only the s 62 repayment amount is limited to "the same harm or loss". Damages only for pain and suffering must still be reported within 28 days (s 64 (2), an offence under s 64 (3)), yet give a repayment amount of nil. Asserted.
18. **After the ACAT dismisses a review, s 65 does not apply in its terms.** Section 65 (1) (b) (ii) makes the person liable only if they do not "pay the repayment amount or apply for a review" by the repayment date. Section 67 (5) says dismissal "removes the stay of liability". After a dismissal the person did apply, so s 65 is not met in its terms. READING: the stay ends and the person is liable. Asserted.
19. **A refusal under s 45 cannot be reconsidered by the commissioner.** Schedule 2, part 2.1 (internally reviewable) lists ss 32, 46, 47, 50, 63 and 71 (3). The s 44, s 45 and s 67 decisions appear only in part 2.2, so they go straight to the ACAT, whose time limit is in the ACAT Act (not deposited). For s 67 the Act itself sets the time: on or before the repayment date (s 67 (3) (b)). Asserted.
20. **Only some amounts are indexed.** Section 25 indexes the s 24, s 28, s 29 and s 30 amounts. The Regulation's amendment history shows reg ss 5, 8, 9 and 10 amended every year to SL2026-8, and reg s 12 (lawyers' costs, under s 97) too. Tables 6 and 7 have been amended only by SL2016-25, and reg s 11 ($8,000 for a funeral) never. So the immediate need, economic loss and funeral caps have stayed at their 2016 figures while the maximums and recognition payments have risen. The encoding takes R11's figures as they stand.
21. **The Act does not say which year's amounts apply.** The amounts change every 1 July. Section 50 (2), for a variation, refers to "the maximum financial assistance amounts that applied when financial assistance was first given", which suggests the amounts in force when assistance is given, not when the act happened. The cases apply R11's amounts to acts from early 2026, as for a decision made after 1 July 2026. Only R11 is encoded.
22. **Reg s 8 (3) moves one sexual offence down two bands.** Where Crimes Act s 66 (1) (b) applies to a table 8 item 3 offence, it is taken to be item 6: $2,716 instead of $10,873. The Crimes Act is not deposited, so whether s 66 (1) (b) applies is an input. Asserted.
23. **"Family violence offence" in s 9 is wider than division 1.2.2.** Section 9 (2) means any schedule 1 offence against a relevant person, so it includes a div 1.2.1 offence such as intimate image abuse by a former partner. Asserted.

## Before relying on it

- An independent test pass, and a check of every figure against the authorised PDFs of R10 and R11 on the register.
- Confirm the CC BY 4.0 statement in the JACS Copyright Policy in a browser (see `SOURCE-LICENSE.md`).
- Track the three pending Bills (finding 1), and add the 2027-28 Regulation amounts when they are made (from 1 July 2027).
- Deposit, and encode where they bite: the Crimes Act 1900, to check which offences are in part 2 and what s 66 (1) (b) covers; the Legislation Act 2001 (domestic partner, periods of time); the Family Violence Act 2016 (intimate partner); the Criminal Code s 25 (age of criminal responsibility); the Victims of Crime Act 1994 (the commissioner and the victims services scheme); the ACAT Act 2008 (review time limits); and the commissioner's guidelines under s 87 (appropriately qualified non-government agencies).
- Encode the parts left out that touch the applicant: division 3.7 (variation within 7 years), s 63 (suspension), ss 34 to 37 (withdrawal and lapse), s 44 (related acts), and s 68 (no recovery from the estate).
- Settle the readings in findings 10, 12, 13, 15, 16, 18 and 21.
