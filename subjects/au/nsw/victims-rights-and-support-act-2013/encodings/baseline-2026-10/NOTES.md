# Victims Rights and Support Act 2013 (NSW): baseline encoding for the victim applying for support

> **Not the current official text.** The texts encoded are the Open Australian Legal Corpus copies of the Victims Rights and Support Act 2013 and the Victims Rights and Support Regulation 2019, both in their versions of 1 February 2025, collected on 10 March 2025. They may be out of date: check legislation.nsw.gov.au before relying on anything here. Based on content from the New South Wales Legislation website (State of New South Wales, CC BY 4.0), via the Open Australian Legal Corpus (CC BY 4.0); see `SOURCE-LICENSE.md` and `SOURCE-LICENSE-regulation.md`.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. Where the deposit cannot answer, the answer is an explicit `not covered` value naming the gap, and a test asserts it. Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

It is written in two layers, after the SNAP baseline (`subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/`):

- **`vrsa-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the act", "a primary victim", "a secondary victim", "a family victim", "a parent, step-parent or guardian who is caring for a child", "the applicant", "the Commissioner"). The definitions (ss 19-22) are worked out from facts. Computations (financial assistance, funeral expenses, recognition payments, counselling hours and payments, time limits) are functions. Where the text says "must" or sets a period there is a regulative rule (`DEONTIC`), four in all:
  - s 40(1)-(3), (5), (7): the application for financial support or a recognition payment must be duly made in time (no rule has a time limit under s 40(7));
  - s 43(1): the Commissioner must determine a duly made application and give written notice;
  - s 40(6): claims may be made under the application for 5 years, or until the total maximum is given, and no claim after that;
  - s 54(2): the Commissioner must pay a claim.

  Dates use only the prelude's built-in DATE functions; daydate is not imported.
- **`vrsa-seat.l4`**, the victim's seat: 17 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule. The same fact has the same input name and wording in every question, so a form can ask it once.

Case files:

- `vrsa-cases-core.l4` tests the core: dates, the kinds of act, the classes of victim and the exclusions, the support, every amount, the recognition categories and payments, counselling, evidence, time limits and the regulative rules.
- `vrsa-cases-victim.l4` tests the seat's questions on plain answers.

Both are formatted from tables by the scratchpad generators `au-nsw-6/gen_vrsa_cases.py` and `au-nsw-6/gen_vrsa_seat_cases.py`, with every expected value written by hand.

This is the first encoding of this Act; there was none to keep. NSW has no requirement ledger, so no ledger line is closed.

## Edition

- **Act:** Victims Rights and Support Act 2013 No 37 (act-2013-037), corpus document `nsw_legislation:2025-02-01/act-2013-037` (version date 2025-02-01, scraped 2025-03-10), from the Open Australian Legal Corpus version 7.1.0, deposited at `../../registers/source-bundle/act-2013-037.txt`.
- **Regulation:** Victims Rights and Support Regulation 2019 (sl-2019-0398), corpus document `nsw_legislation:2025-02-01/sl-2019-0398` (version date 2025-02-01, scraped 2025-03-10), same corpus, deposited at `../../../victims-rights-and-support-regulation-2019/registers/source-bundle/sl-2019-0398.txt`.
- Both were taken from the corpus because legislation.nsw.gov.au answered with a bot challenge. **They are not the current official text and may be out of date.**
- **The amounts are fixed in the deposited Regulation and are encoded as stated:**
  - cl 5: 22 hours, an initial 2 hours, and $5,500 outside Australia;
  - cl 8: $120, $144 and $256 an hour, with GST capped at 10%;
  - cl 10 to 13: $5,000, $30,000, $20,000, $5,000, $5,000, $1,500 and $9,500;
  - cl 14: $15,000, $7,500, $10,000, $5,000 and $1,500.

  Nothing in them is indexed. A later amendment to the Regulation would change the answers.
- **Not deposited, so inputs or not covered:**
  - the cl 9 rate of actual loss of earnings (finding 9);
  - the approved application form (s 38(2), s 39(1));
  - the Interpretation Act 1987, which governs how the periods in s 40 are counted (finding 16);
  - the Acts whose terms the Act borrows: the Crimes Act 1900, the Modern Slavery Act 2018, the Motor Accidents Compensation Act 1999, the Terrorism (Police Powers) Act 2002 and the Crimes (Administration of Sentences) Act 1999. Their terms are asked as facts.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vrsa-core.l4` | `vrsa-cases-core.l4` | 287 written, 287 satisfied |
| `vrsa-core.l4`, `vrsa-seat.l4` | `vrsa-cases-victim.l4` | 69 written, 69 satisfied |

In addition, 6 `#TRACE`s in `vrsa-cases-core.l4` carry an `-- expect:` line. Each was read, and each matches its expectation with the expected party and reason:

- four breaches by the applicant:
  - an application on day 732 of 731;
  - no application by day 800;
  - a claim after the 5 years;
  - a claim after the total maximum was given;
- two obligations still pending:
  - the Commissioner's s 43 determination;
  - the s 54(2) payment of a claim.

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. As a control, a copy of `vrsa-cases-core.l4` was run with four expected values changed ($18,800 to $18,801, and three category B payments of $10,000 to $9,999). The runner reported 4 assertions failed and 283 satisfied.

Every expected value was worked by hand from the deposited texts, with the reasoning or arithmetic in the comment above the assertion. The amounts claimed in the cases (expenses, weekly rates, fees) are made up. They are not taken from any real claim.

## Seat

**The victim applying for support:** a primary, secondary or family victim, or the parent, step-parent or guardian caring for a child primary victim. Anyone applying on a victim's behalf (s 38(1)(b), (c)) answers for the victim. They ask:

- "Is what happened an act of violence, an act of modern slavery or a road crime?"
- "Am I a primary, secondary or family victim, and am I excluded?"
- "What support am I eligible for, and up to what amounts?"
- "How much can I get for my immediate needs, my economic loss, the funeral, or as a carer?"
- "Which recognition payment category applies, and how much is it?"
- "How much counselling is paid for?"
- "By when must I apply, and how long can I keep claiming?"

The Commissioner's powers and judgments appear only as what they mean for the victim, each asked as a fact or answered conditionally:

- special circumstances for a convicted inmate (s 25(5));
- whether acts are a series of related acts (s 19(4)-(6));
- a counsellor's tier (Reg cl 4);
- costs determined under cl 8(1)(c);
- whether a person is still being established as a victim (cl 5(3)).

Where the amount is the Commissioner's to set, the financial questions give the most that may be paid. Section 44, under which the Commissioner may pay less, is out of scope. The Commissioner's duties under ss 43 and 54(2) are regulative rules in the core, with the Commissioner as a party. There is no seat for the Commissioner or the Tribunal, which are officials, and none for the offender, because Part 5 is out of scope.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed: the Regulation is brought in for its amounts and counselling limits.
- **The actors the text names.** Followed: the person, the primary victim, the parent, step-parent or guardian, the applicant, the Commissioner and the Tribunal.
- **Judgments left to others, answered conditionally.** Followed: the judgments listed above. Answers are worded as "up to", "if the Commissioner considers it appropriate" or "unless the Commissioner is satisfied". The financial questions take the person's class as given and say so in their `@export`, because the eligibility question answers it. This keeps their inputs to the figures of the claim.
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.** Worked out:
  - act of violence (s 19), act of modern slavery (s 19A) and road crime (s 19AB);
  - primary, secondary and family victim, and immediate family (ss 20-22);
  - eligibility and exclusions (ss 23-25);
  - recognition categories (s 35) and their recipients (s 36);
  - dependent family member (s 29(4)).

  Asked as facts: offence, violent conduct, injury, sexual assault, sexual touching, homicide, serious bodily injury, grievous bodily harm, offensive weapon, robbery, modern slavery, motor accident, terrorist act, convicted inmate, de facto partner, domestic violence, child abuse, sexual offence.
- **One case is one act**, with "a series of related acts" counted as a single act (s 19(7), s 19A(6)).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Commissioner's office and functions, the Fund, the Victims Advisory Board and the levies.

## Scope

**In:**

- Part 4, Division 1:
  - s 18 (injury, financial support);
  - s 19: act of violence, its elements as facts, with s 19(3A) and the s 19(8) definition quoted in `@desc`;
  - s 19A: act of modern slavery;
  - s 19AB: road crime;
  - s 20: primary victim, including rescuers;
  - s 21: secondary victim, both the witness and the parent or guardian who later learns of an act against a child;
  - s 22: family victim and immediate family, including a de facto partner after 2 years' cohabitation.
- Division 2:
  - s 23 (eligibility);
  - s 24 (death of the victim);
  - s 25: the exclusions for court compensation; for a motor accident, with the (2A) and (2B) exceptions; for the victim's own offence; for the family of the alleged road-crime offender, with the (3A) exception; and for convicted inmates, with the special-circumstances exception.
- Division 3:
  - ss 26-29A: counselling, immediate needs, economic loss, funeral expenses and recognition payments, with the cross-reductions in ss 26(2) and 27(2);
  - s 30(2): no assistance for loss already paid for;
  - s 30A: each type of support once.
- Division 5: ss 34-36 (categories A-D, the recipients of category A, one payment per series).
- s 53: a recognition payment is suspended pending review by the Tribunal, as a fact.
- Division 6:
  - s 38 (who may apply);
  - s 39 (documentary evidence, with police or agency reports and medical reports as facts);
  - s 40 (time limits, and claims under an application);
  - s 43(1) (determination, as a regulative rule);
  - s 47 (funeral and clean-up expenses of persons other than family victims).
- Division 8: s 54(2) (payment, as a regulative rule).
- Regulation:
  - cl 4: who is a victim for counselling, as the counselling class;
  - cl 5: counselling hours, the initial 2 hours, and the lesser of 22 hours and $5,500 outside Australia;
  - cl 7: ongoing counselling for child sexual or physical abuse;
  - cl 8: counsellor rates, travel, and GST capped at 10%;
  - cl 9: as not covered;
  - cl 10: primary victim;
  - cl 11: parent, step-parent or guardian;
  - cl 12: family victim;
  - cl 13: non-family persons;
  - cl 14: recognition payments.

**Not covered (asserted):**

- the cl 9 rate of actual loss of earnings (finding 9). The economic loss questions take the weekly rate as an input, and cl 10(3)(a) and 11(2)(a) cap the result at $20,000.

**Out:**

- Part 2, the Charter of Victims Rights, which gives no money entitlement;
- Part 3, the Commissioner's functions and the Fund;
- Part 5, restitution orders against offenders. That is the offender's liability, not a benefit, and so there is no offender seat;
- Part 6, court compensation, except as the s 25(1) exclusion;
- ss 41, 41A (withdrawal and lapsing);
- s 42, and s 43(2)-(7) except the determination itself;
- s 44, the Commissioner's reasons for refusing or reducing support, and the postponements in s 44(5)-(7);
- ss 45, 46 and 48: set-off against restitution, to whom a payment is made, and the conditions of approval, including the duties to notify and repay;
- ss 49-53, the review procedure, except s 53 as a fact;
- s 55 (subrogation);
- s 56 (fraud recovery);
- Parts 7-9;
- Regulation cl 6, cl 15 and cl 16.

## Read with

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Commonwealth Social Security Act 1991** (`../../../../social-security-act-1991/`, encodings `baseline-2026-10/` and `naive-2026-10/`). Whether a recognition payment or financial assistance under this Act counts as income or as "compensation" under Part 3.14 for a Centrelink payment is **unverified (from general knowledge, not from the texts)**, as the NSW README says. Checking it means reading the Social Security Act's compensation definitions against this Act.
- **Commonwealth Income Tax Assessment Act 1997** (`../../../../income-tax-assessment-act-1997/`). Whether recognition payments and financial assistance are assessable income is likewise **unverified (from general knowledge, not from the texts)**.
- **Commonwealth A New Tax System (Goods and Services Tax) Act 1999** (`../../../../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/`). Regulation cl 8(5) gives "GST" the meaning it has in that Act. The counselling questions take the GST payable as an input.
- **NSW Workers Compensation Act 1987** (`../../../workers-compensation-act-1987/`, text only, version 2023-10-30). There are three joins:
  - s 30(2) here excludes financial assistance for loss already paid for, workers compensation included. Section 44(5), which is out of scope, postpones a determination until workers compensation entitlements are decided.
  - Regulation cl 5(8) pays for counselling even where the victim is entitled to workers compensation for the same act.
  - Regulation cl 9 borrows the pre-2012 s 37 weekly rate. That version is not deposited: the deposited s 37 is the substituted "second entitlement period" section (finding 9).
- **NSW Motor Accident Injuries Act 2017** (`../../../motor-accident-injuries-act-2017/`, no text). This is where a person excluded by s 25(2) for a motor accident would look. Note that s 25(2) still borrows the Motor Accidents Compensation Act 1999's definition (finding 21).
- **ACT Victims of Crime (Financial Assistance) Act 2016** (`../../../../act/victims-of-crime-financial-assistance-act-2016/encodings/baseline-2026-10/`), the neighbouring scheme encoded the same day, for comparison.

## What the Act turns out to say

1. **Section 19 states no place.** An act of modern slavery must be "committed in New South Wales" (s 19A(1)), and so must a road crime (s 19AB(1)(a)). The deposited s 19 has no such words, so the encoding asks no place for an act of violence, and an assault in Melbourne is an act of violence. Asserted. Whether the Scheme reaches acts outside NSW by some other rule (the Interpretation Act 1987, not deposited) is not answered by the deposited text.
2. **A road crime is not an act of violence, except in the s 25(2A) and (2B) circumstances (s 19(3A)).** So for a death by dangerous driving, the family are family victims of a road crime and get counselling only (s 29A). An injured survivor of the same crash is no victim at all: a primary victim needs an act of violence or an act of modern slavery (s 20). Asserted.
3. **A vehicle death with an identified, living offender who has not been charged is not a road crime.** Section 19AB(1)(b) requires charges, or an offender who has died or cannot be identified. Such a death falls back to being an act of violence that is a motor accident. Section 25(2) then excludes the family, unless someone is charged with murder (s 25(2A)) or it was a terrorist act (s 25(2B)). The family get nothing, not even counselling, until charges are laid. Asserted. The deposited Regulation prescribes no s 19AB(1)(b)(iii) circumstances.
4. **Family victims exist only for acts of violence and road crimes.** Section 22(1) defines a family victim of an act of violence, and (1A) of a road crime. Yet s 36(1)(a) pays category A to family victims where the death was "as a result of an act of violence or act of modern slavery", and s 43(3)(a)(i) speaks of a "family victim of an act of violence or act of modern slavery". The family of a person killed by an act of modern slavery that is not also an act of violence have no s 29 support. Asserted.
5. **The offence exclusion speaks only of an act of violence.** Section 25(3)(a) applies "in relation to an act of violence", and s 25(2) likewise. A victim of an act of modern slavery who was made to commit offences is not excluded, and this holds even where the act is also an act of violence, because the support can rest on the act of modern slavery. Asserted.
6. **The motor-accident exceptions are narrow.** Section 25(2B) (a terrorist act) names only "a primary victim and a family victim", and s 25(2A) (an intentional killing with a murder charge) names only "a family victim". So two people are excluded under s 25(2):
   - a person traumatised by witnessing a vehicle terrorist attack, who is a secondary victim;
   - a person injured by a driver who is charged with the murder of someone else.

   Both asserted.
7. **The caring parent gets no counselling as such.** Section 27 gives a parent, step-parent or guardian caring for a child primary victim only financial assistance for economic loss, up to $30,000 (cl 11(1)). They get counselling only if they are also a secondary victim, for example a parent who learns of the act and is injured by it (s 21(2)). Asserted.
8. **The cross-reductions are not symmetrical, and the Act does not say what is reduced.**
   - Section 26(2) reduces the primary victim's "financial assistance", which includes immediate needs, by everything paid to the carer under s 27.
   - Section 27(2) reduces the carer's assistance by what was paid to the child under s 26(1)(c) only.
   - READING: the amount payable is reduced, not the maximum, and never below nothing. A child paid $15,000 leaves a carer with an $11,300 loss nothing. On the other reading, a shared $30,000 maximum, the carer would get the $11,300.
   - The overlap the reductions guard against is real: cl 10(3)(c) and 11(2)(c) both cover the child's medical and dental expenses, and cl 10(3)(e) and 11(2)(e) the same clothing.

   Asserted.
9. **The weekly rate of actual loss of earnings is not covered.** Regulation cl 9 calculates it "at the rate of weekly payment of compensation payable under section 37 of the Workers Compensation Act 1987 (as in force immediately before its substitution by the Workers Compensation Legislation Amendment Act 2012) and indexed in accordance with law". The deposited 1987 Act is the 2023 version, whose s 37 is the substituted section, and the indexed amounts are not deposited.
   - The cl 9 question answers `not covered`, asserted.
   - The economic loss questions take the weekly rate as an input. Rate times weeks, less what is paid from elsewhere, is capped at $20,000 by cl 10(3)(a) or cl 11(2)(a). Asserted.
10. **The funeral payment is not reduced by s 30(2).** Section 30(2) makes "financial assistance" not payable for loss already paid for. Section 18 lists funeral expenses under s 29(1)(c) as a separate kind of financial support, and s 29(1)(c) calls it "a payment". READING: s 30(2) does not reduce it, though the Commissioner must still have regard to other amounts received (s 44(4), out of scope).
11. **A s 47 reimbursement comes out of the family's funeral and immediate-needs amounts.** Section 47(4)(a) says it "is to be paid from the amount" for which the family victims are eligible, and s 29(1)(b), (c) and (2) deduct it from them.
    - READING: a friend's funeral reimbursement is capped both by cl 13(b) ($9,500) and by what the family victims have left of their $9,500. Where the family have had $6,000, the friend can get $3,500. Asserted.
    - The family victim's own immediate needs and funeral questions deduct any s 47 amount. Asserted.
12. **The recognition categories overlap, and s 36 does not say which one a primary victim gets.**
    - Section 35(3)(a) excludes from category C only a sexual assault "referred to in subsection (2)(b)". A sexual assault with a weapon is therefore category B under (2)(a) and also C.
    - Physical assaults of a child in a series are C under (3)(d) and also D under (4)(d), as an assault not resulting in grievous bodily harm.
    - READING: a primary victim is paid the highest of B, C and D that describes the act; s 26(1)(d) and s 36(2) speak of one payment.

    Asserted.
13. **A person can be both a family victim and an injured primary victim of a homicide.** Take a wife beaten in the attack that killed her husband. Section 36(1)(b)(ii) pays her category A ($7,500), and s 36(1)(e) pays her category D ($1,500) for the assault on her. Section 36(2) limits only a series of related acts against the victim. The encoding gives both. Asserted.
14. **Category A reaches fewer family members than s 22 does, and the Act's two lists differ.**
    - Section 36(1)(a) pays $15,000 (cl 14(a)) to financially dependent family victims and to each "child" under 18.
    - Section 36(1)(b) pays $7,500 (cl 14(b)) to non-dependent parents, step-parents, guardians, spouses and 2-year de facto partners.
    - So the following get nothing, all asserted: a non-dependent adult child, a non-dependent sibling, a non-dependent step-child under 18 ("child", not "step-child", in (a)(ii)), and a de facto partner of under 2 years, even a dependent one (not immediate family, s 22(3)(b)).
    - Section 29(3) makes eligible "each family member who is a parent, step-parent or guardian or a dependent family member", which leaves out the non-dependent spouse that s 36(1)(b)(ii) pays. The encoding follows s 36.
    - Section 29(4)(b) makes a child born after the death a dependent family member, though the child was not immediate family "at the time" of the act (s 22(1)). READING: the child is paid at the s 36(1)(a) amount. Asserted.
15. **Counsellor travel counts only above 2 hours, and then in full.** Regulation cl 8(2) says "Any period of more than 2 hours during which a counsellor travels ... is to be counted". READING: a 3-hour trip adds 3 hours at the scale rate, and a 2-hour trip adds nothing. Asserted.
16. **Section 40 does not say how its periods run.**
    - It does not say which act of a series the 2 years run from. The encoding counts from the date given.
    - The adult limb of s 40(1) speaks only of "the relevant act of violence", while the child limb names acts of modern slavery too. The encoding reads both in.
    - The Interpretation Act 1987, which counts periods, is not deposited. READING: a period "within 2 years after" a day ends on the same day 2 years later, with 29 February becoming 28 February.
    - Where s 40(3) and s 40(1) or (5) both apply, the later day governs.

    Asserted.
17. **Two terms in s 40(5) are undefined.** Section 40(5) uses "domestic violence, child abuse or sexual assault". Section 19(8) defines only the combined phrase "sexual assault and domestic violence", s 34 defines "sexual assault" for Division 5 only, and "child abuse" is not defined at all. The encoding asks one fact.
18. **The s 39(2)(b) evidence does not fit a family victim.** For a recognition payment, s 39(2)(b)(ii) asks for "a medical, dental or counselling report verifying that the applicant or child who is the primary victim concerned has actually been injured". A family victim applying for category A need not be injured (s 22(2)). The encoding applies the section as written and lists the report as missing. Asserted.
19. **Section 40 sets no time limit for counselling, and s 40(7) frees only some claims.** Section 40 applies only to "financial support or a recognition payment", so a request for approved counselling has no time limit. Asserted. Section 40(7) removes the time limit for a child victim of a sexual offence only for:
    - out-of-pocket expenses (cl 10(3)(b));
    - justice-related expenses (cl 10(3)(d));
    - a recognition payment.

    Immediate needs, lost earnings and medical expenses still fall under s 40(1): 2 years after turning 18. Asserted.
20. **The Regulation's counselling exclusion is wider than the Act's exception.** For counselling, Regulation cl 4(d) keeps as a victim the family victim of a motor-accident act that "apparently occurred in the course of the commission of the offence of murder or manslaughter". Section 25(2A) requires an intentional killing and a murder charge. The encoding follows s 25 for eligibility, and the counselling question takes the counselling class as a fact. Not asserted.
21. **Section 25(2) still borrows the Motor Accidents Compensation Act 1999.** The motor accident must be one "within the meaning of the Motor Accidents Compensation Act 1999", while s 44(6A) refers to the Motor Accident Injuries Act 2017. The term is asked as a fact. Not asserted.
22. **Counselling outside Australia has two limits in different units.** Regulation cl 5(5) caps payments at "22 hours or a maximum of $5,500, whichever is the lesser". The encoding takes the dollar limit as the lesser of 22 hours at the counsellor's fee and $5,500, less what has been paid, and gives the hours that buys. At $256 an hour that is $5,500, or 21.48 hours. Asserted. Regulation cl 7 (ongoing counselling for child abuse) overrides it. Asserted.
23. **Out-of-pocket expenses and lost earnings are alternatives.** Regulation cl 10(3)(b) gives "$5,000 for out-of-pocket expenses" only "if the victim cannot demonstrate actual loss of earnings". READING: a victim who shows lost earnings gets nothing for out-of-pocket expenses under (b). Asserted.

## Before relying on it

- **Replace both texts** with the official ones from legislation.nsw.gov.au once it can be fetched, and re-check every amount in cl 5, 8 and 10-14 against the current Regulation.
- **Deposit the pre-2012 Workers Compensation Act 1987 s 37** and the indexed amounts, so that the cl 9 weekly rate can be computed (finding 9).
- **Deposit the Interpretation Act 1987**, which settles the period readings in finding 16 and the territorial question in finding 1.
- **An independent test pass**, in particular of the readings in findings 8, 10-12, 14 and 15.
- **Encode s 44** (reductions for the victim's conduct and for other payments) and **s 48** (the duties to notify and repay), which bear on how much is actually paid.
- **Verify the Commonwealth treatment** of recognition payments and financial assistance under the Social Security Act 1991 and the ITAA 1997. It is unverified here.
