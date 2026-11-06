# National Disability Insurance Scheme Act 2013 (Cth) — compensation: baseline encoding

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE outside `LEST BREACH … BECAUSE`. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is a second encoding beside `../baseline-2026-10/` (access to the scheme), which is untouched.
That one covers becoming and ceasing to be a participant; this one adds the compensation and compensation-recovery provisions (Chapter 5), which it left out.

## Edition

- **The Act:** Compilation No. 26, compilation date 27 August 2026 (includes amendments up to Act No. 66, 2026), register id C2026C00366, deposited at `../../registers/source-bundle/C2013A00020.txt`.
  The deposit's own caveat: a version in force from 19 September 2026 had no registered compilation when the text was retrieved, so amendments commencing on or after 27 August 2026 may be missing.
- **Not deposited:** the NDIS rules. What they prescribe here is an input or out: the further laws whose charges come off the compensation (ss 106(5)(b)(iv), 107(4)(b)(iv), folded into one input with the named Acts), and a review period under s 100(6A) (out: it binds the reviewer, not the person).
- The Health and Other Services (Compensation) Acts 1995 and Part 3.14 of the Social Security Act 1991 are not encoded here: what they take from the compensation is asked as one dollar figure.

## Checks

Three files: `ndis-comp-dates.l4` (the only daydate import), `ndis-compensation.l4` (the questions), `ndis-cases-compensation.l4` (the cases).

- `l4 run ndis-cases-compensation.l4`: 122 assertions written, 122 satisfied, 0 errors, 0 warnings.
- `l4 run ndis-compensation.l4` and `l4 run ndis-comp-dates.l4`: 0 errors, 0 warnings.
- A mutation of three expected values (one amount, two dates) was caught: 108 satisfied, 3 failed. The assertions are live.
- Expected values were worked by hand from the text, with the section in a comment beside each group. Every `NOT` is bracketed. All 23 exported questions carry `@export` and a `@desc` on each input.

## Seat

**The person with disability who has, or may have, a claim for compensation for a personal injury**: a participant, or a prospective participant (one whose access request has been made but not yet decided).
The question is "What does the NDIS Act do to my compensation claim, and what do I owe the Agency out of it?".
Every exported question is that person's:

- "Is this payment compensation?" (s 11)
- "Can the CEO require me to take action to claim compensation?", "By when must I take the required action?", "Have I taken the required action in time?", "What happens to my plan if I do not act?", "Can NDIS amounts be paid for a support during the suspension?", "Can I ask for a variation or reassessment during the suspension?", "Can the CEO claim in my name or take over my claim?" (ss 104, 105, 41(2))
- "How much of the costs does the Agency pay?", "How much of the amount obtained is paid to me?" (ss 105A, 105B)
- "Do I owe the Agency a recoverable amount?", "How much must I repay the Agency?" (ss 106–108, 116)
- "By when must the person I claim against tell the CEO?", "Can the person I claim against pay me now?", "How much can the Agency recover from the person I claim against?", "How much compensation is still owed to me?", "How much do I still owe the Agency?" (ss 109–114)
- "Can I ask for review of this decision?", "By when must I ask for review?" (s 99 items 23–28 and 31–33, s 100(2))
- "By when must the Agency sue me for the debt?", "Can my debt be waived as a small debt?", "How much of my debt must be waived?", "Can my debt be waived in special circumstances?" (ss 183, 193–195)

The CEO's powers, and the duties of the person claimed against and its insurer (ss 109–115), are encoded for what they mean to the person: whether they can be paid, how much reaches them, what they still owe.
No seat for the CEO, the Agency or a court. The person claimed against and its insurer could have a seat layer of their own later (their s 110 and s 114 offences and civil penalties, s 115 liability); none is written here.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed; the NDIS rules are not deposited (see Edition).
- **The actors the text names.** Followed: the participant or prospective participant, the CEO, the Agency, the potential compensation payer or compensation payer, the insurer.
- **A judgement handed to someone else is answered conditionally.** Followed. Inputs: the CEO's opinion that the person is or may be entitled to compensation (s 104(1)(a)); that an agreement giving up the right is void, ineffective or unenforceable (s 104(6)); reasonable prospects of success (s 104(4)); the part the CEO treats as not fixed (s 116); costs unreasonably incurred (s 105A(1)); cost-effectiveness (s 193); special circumstances and waiver over write-off (s 195). The s 104(3) and s 105(5) matters the CEO must weigh are not decided.
- **The Act's own definitions worked out; borrowed terms asked.** Worked out: "compensation" (s 11), "recoverable amount" (ss 106, 107), "reviewable decision" (s 99, for Chapter 5). Asked: "personal injury", "judgement", "consent judgement", "settlement", "scheme of compensation under a Commonwealth, State or Territory law", and the charges under the Health and Other Services (Compensation) Acts and the Social Security Act.
- **One case is the text's natural unit.** Followed: one person, one injury, one compensation claim and its judgement or settlement.
- **The Act's own terms, each with a plain gloss.** Followed, in comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed.

The s 105(1) duty is written as a regulative rule (`the s 105(1) duty`: PARTY the participant or prospective participant MUST take the required action WITHIN the days … LEST BREACH … BECAUSE). The exported question takes plain dates and a yes/no and runs the rule inside with `EVALTRACE`, read with `CONSIDER … WHEN FULFILLED`.

## Rulings on negatives and legal effects (recorded word for word, as the guide requires)

Where the text itself says no in its own words the answer is `JUST FALSE`; elsewhere `NOTHING`. Periods, "where" and scope limits (ruled 2026-11-05): "(a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" ...: outside the scope the answer is `NOTHING`." Questions with no convention are decided site by site, each with a fork line.

### Fork register

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| s 104(6) | `Can the CEO require me to take action to claim compensation` | An agreement giving up the right that the CEO is not satisfied is void: `NOTHING`, but only once the flat bars are passed (reasonable action already taken, s 104(1)(b); prospects not satisfied, s 104(4): `JUST FALSE` whatever the agreement). s 104(6) says when the CEO "may" form the opinion despite the agreement, not that it may not otherwise. | The agreement stops the opinion: `JUST FALSE`. |
| s 104(5) | `By when must I take the required action`, `Have I taken the required action in time` | A notice giving fewer than 28 days: `NOTHING`. The rule binds the CEO and is silent on the person's deadline. | The period is read up to 28 days (as the access encoding read a short s 29A cooling-off period up to 90). |
| s 111(4)(b) | `How much can the Agency recover from the person I claim against` | No judgement or settlement yet, or a contested judgement with no past NDIS support component: `NOTHING`. There is no "recoverable amount in relation to the judgement". | Limb (b) drops out and the sum of the NDIS amounts is the amount. |
| ss 99, 9 | `Can I ask for review of this decision` | The recoverable amount itself is not a reviewable decision: `FALSE` ("reviewable decision has the meaning given by subsections 99(1) and (2)", a closed definition). | — |

## In scope

ss 11 (compensation), 41(1)(b), (2)(a), (c) (the effect of a s 105(2) suspension), 104, 105, 105A(1), 105B, 106, 107, 108, 109 (as what s 110 and s 114 build on), 110 (the deadline only), 111(1)–(4), (6), 112, 113, 114 (whether the person can be paid), 116; s 99 table items 23–28 and 31–33 and s 100(2); ss 183, 193, 194, 195 for the debt that s 108 creates.

## Out of scope, and why

- **s 105A(2)–(5)** (the CEO's conduct of a taken-over claim, the duty to sign documents, the court's direction): procedure between the CEO and the court; the person's duty to sign is plain and has no deadline.
- **The penalties in ss 110 and 114, and s 115** (the payer's and insurer's liability to the Agency): they fall on the person claimed against and its insurer, not on the seat. Only what they mean for the person (when the Agency must be told; whether the person can be paid) is encoded.
- **ss 32K(4), (4A) and 35(4), (5) (rules on taking compensation into account in a plan)**: they only empower the NDIS rules, which are not deposited.
- **s 182 and the rest of Chapter 7, Part 1** (other debts, arrangements, financial institutions, information powers, write-off in s 190, administrative-error waiver in s 192): not compensation debts, or no answer for the person (a write-off "does not prevent" recovery, s 190(5)).
- **s 99 table items 29 and 30** (decisions under s 190 and s 192): those powers are out, as above.
- **s 41(2)(b) and (3)**: whether the Agency funds other supports during a suspension is the CEO's choice; when a support counts as acquired during the suspension is for the NDIS rules (asked as an input). ss 47A and 48 themselves (variation and reassessment) are not encoded; only s 41(2)(c)'s bar on requesting them is.
- **Further review (s 103)** and the s 100(6A) review period.
- Machinery: the Agency, the Board, the rule-making power, commencement.

## What the Act turns out to say

1. **"Compensation" needs a supports element.** A payment counts only if it is "wholly or partly in respect of the cost of supports that may be provided to a participant (whether or not specifically identified as such)" (s 11(1)). A payment for a personal injury that is wholly for something else is not compensation for any purpose of the Act. Asserted.
2. **The notice period has a floor but the Act does not say what follows a short one.** The period "must be a period of at least 28 days after the day on which the notice is given" (s 104(5)), and the CEO may extend it (s 104(5A)). A notice given on 2 November 2026 with 28 days runs to 30 November. Asserted; a 27-day notice answers `NOTHING` (fork).
3. **Statutory schemes and common law claims are treated differently, and s 105(3) is broader than s 105(2).** A participant who fails to act loses the plan (suspended, or not yet in effect) only where the claim is under "a scheme of compensation under a Commonwealth, State or Territory law" (s 105(2)). For a common law claim the plan is untouched but the CEO may sue in the person's name or take over the claim (s 105(4)). For a prospective participant, s 105(3) holds back the plan whatever the kind of claim, and s 105(4) also applies to a common law claim. Asserted.
4. **Drafting slip in s 105(2).** It opens "If a participant does not take the required action" and continues "to enable the participant or prospective participant to claim". The second limb is otiose, because a prospective participant is dealt with by s 105(3). No effect on the answers.
5. **When both s 106(4) and s 106(5) would cap the amount, s 106(2)(b) does not say which.** It refers to "whichever of those subsections is applicable". Each is a ceiling, so the lesser is taken. s 106(4) yields "the lesser of the sum of the past NDIS amounts and the past NDIS support component". When it applies the reduced sum already exceeds the component, so the result is always the component, and the reference to the unreduced past amounts never bites. Asserted (a component of $100,000 against past amounts of $150,000 gives $100,000).
6. **A contested judgement that does not specify a past NDIS support component escapes Part 2.** s 106(1)(c) requires the judgement to specify that component, and s 107 covers only consent judgements and settlements. So a judgement after a contested hearing that is silent on NDIS-type supports creates no recoverable amount. s 111(4)(b) then has nothing to measure (fork). The CEO's s 116 power runs the other way: it treats payments as not fixed. Asserted.
7. **Contributory negligence reduces the repayment proportionately.** The past NDIS amounts are reduced "by the proportion corresponding to the proportion of liability that is apportioned to the participant". A 25% share turns $150,000 into $112,500. Asserted.
8. **Other charges come first.** The recoverable amount cannot exceed the compensation less what the Health and Other Services (Compensation) Acts, Part 3.14 of the Social Security Act and prescribed laws take from it (ss 106(5), 107(4)). If those use the compensation up, the recoverable amount is nil (INFERENCE from "the difference (if any)"). Asserted.
9. **s 183's extensions do not chain.** A part payment, acknowledgement or internal recovery activity extends the time for proceedings only if it happens "within the recovery period". That period is defined once, as the 6 years from the Agency's awareness. A second payment made during an extension, but after that first period, does not extend again on the text. A period "starting on" a day ends the day before its sixth anniversary; a period "after the end of" an activity ends on the anniversary (INFERENCE). The two drafting forms give answers a day apart. Asserted.
10. **Review is three months from receipt of the notice.** The six Chapter 5 decisions in the s 99 table (items 23–28), and refusals to waive the debt under ss 193, 194(3) or (4) and 195 (items 31–33), are reviewable on a request made "within 3 months after receiving the notice" (s 100(2)). A recoverable amount under s 106 or s 107 arises without a decision and is not in the table. A notice received on 30 November 2026 gives until 28 February 2027 (INFERENCE, as in the access encoding). Asserted.
11. **The 28 days before the CEO takes over a claim.** "28 days have passed since the notice was given" (s 105(6)(b)) is read as 28 whole days after the day of the notice. After a warning on 1 March 2027 the CEO may act on 30 March, not on 29 March (INFERENCE). Asserted.
12. **s 105B says "the amount of those damages"** where no damages have been mentioned, only "any amount obtained". It is read as the amount obtained. Where the deductions exceed it, the balance is nil; s 105B does not make the person pay the shortfall (INFERENCE). Asserted.

## What would need doing before this is worth anything

- Deposit the NDIS rules (the prescribed laws in ss 106(5)(b)(iv) and 107(4)(b)(iv), and the compensation rules made under ss 32K and 35) and encode how compensation is taken into account in a plan.
- Encode the Health and Other Services (Compensation) Act 1995 and Part 3.14 of the Social Security Act 1991, so that the "other charges" figure is worked out rather than asked.
- Decide the forks above, and whether s 183's extensions chain.
- Check the version in force from 19 September 2026 once it is registered.
- A seat layer for the person claimed against and its insurer (ss 110, 114, 115).
- An independent test pass and the human gates.
