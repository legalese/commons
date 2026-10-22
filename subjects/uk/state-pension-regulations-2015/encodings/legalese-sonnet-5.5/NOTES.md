# NOTES: State Pension Regulations 2015 (S.I. 2015/173), encoding `legalese-sonnet-5.5`

Status: DRAFT. Both layers are written and every check below passes, but no domain expert has read this against the text.
Method: a single Sonnet 5.5 agent working alone from `BRIEF.md`.

Source: `../../registers/source-bundle/uksi-2015-173.txt`, a plain-text rendering made by a converter script (ukfetch.py, CLML to text) from the revised text on legislation.gov.uk at the point in time 2026-04-06.
It is not the official text, it is not marked up, and nothing here is "verified against the official text".
The Regulations are read as the text in the file states them.
Amendments after 2026-04-06, and the parent Acts and instruments the text cites, are not among the inputs (see "What is encoded and what is not").

Checked with the stable `l4` 1.6.98 (`stable/extension/bin/darwin-arm64/l4` in the run, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`), `JL4_LIBRARY_PATH` unset.

## Seat

**A person who is, or will become, entitled to the State Pension, asking what these Regulations mean for when and how their State Pension is claimed, paid and affected by their choices.**

Why this seat.
The Regulations are made under the Pensions Act 2014 and speak to the pensioner: whether a day's State Pension is paid at all (prisoners, regs 2 and 3), what a choice to defer or suspend does to the rate (regs 4 to 12A), how an inherited pension is worked out (regs 15 to 20), what living abroad does to an up-rating increase (regs 21 to 23), and which weeks the National Insurance credits in Part 8 add to a person's qualifying years.
Most operative provisions are a right, a choice, a duty or an exposure of that person; the rest are definitions, counting rules and amounts.
The other parties the text names are the Secretary of State, HM Revenue and Customs and the court.
They are officials, so there is no seat for them.
What they must furnish, may decide or may order appears only as what the person is owed or exposed to: the lump sum and pension they must be paid, the information and its deadline, the late choice they may allow, the further time they may allow.
The person's spouse, civil partner, former spouse, carers and partner are not seats either; their facts are inputs to the person's questions ("who makes the request", "how are you related to the child").

Layers.
Layer 1 is the law, stated once and objectively, with the source quoted and cited: `spr-nouns`, `spr-dates`, `spr-part1-general`, `spr-part2-prisoners`, `spr-part3-deferral`, `spr-part4-qualifying-years`, `spr-part5-sharing`, `spr-part6-graduated`, `spr-part7-overseas`, `spr-part8-credits-1`, `-2`, `-3`.
Every module with rules has a `spr-tests-*` file (`spr-nouns` declares types only and has none; `spr-tests-dates` covers `spr-dates`).
Layer 2 is `spr-seat.l4` (84 questions with `@export` and `@desc`, grouped under `§` headings in the text's order) and `spr-cases-seat.l4` (at least one case per question).
The seat imports every layer-1 module and calls their rules; it restates none of them.

What the seat assumes (also at the head of `spr-seat.l4`).

- Every answer assumes the first question, "Do these Regulations apply to me?" (reg 1(3)), is answered yes. The other questions do not re-ask it.
- Pensionable age is fixed by Acts that are not among the inputs, so the date the person reaches it is asked, not worked out.
- A judgment the Regulations leave to the Secretary of State or another official is asked as a fact ("Does the Secretary of State consider it reasonable ...?"), so the answer is conditional on it.
- The person asking is alive: the field reg 6(2)(a) reads, `the person who made the choice has since died`, is fixed to false in the question that calls reg 6(1), not asked.
- A list the rules take is asked one item at a time where one item decides the answer: regs 11 (benefits received on a day), 12A(1) and 23(1) (a single change date), 22(1) (one flag for "any part"), 37(2)(a)(i) (one flag for "each person cared for"). The limits are in "What is encoded and what is not".
- A question that has to be asked only in a situation the person may not be in says so in its heading comment, so a form can ask "Has this happened to you?" first: prison or remand; a late spouse's deferred pension (regs 4 to 6); the person's own deferral (regs 7 to 12A); a death of a spouse or civil partner (regs 15 to 20); living abroad (regs 21 to 23); credits (Part 8); sharing on divorce (Part 5).

## Jural relations

One row per provision that creates a relation, read in Hohfeld's correlatives.
A provision that creates none is listed once as `none`.
"SoS" is the Secretary of State, "HMRC" HM Revenue and Customs.

| Provision | Holder (claim, privilege, power or immunity) | Bearer (duty, no-right, liability or disability) | Relation | L4 rule |
|---|---|---|---|---|
| Reg 1(1) to (5), 1A | none | none | none: title, commencement, scope, definitions, a counting rule, an amount | `regulation 1(2): the commencement date`; `regulation 1(3): these Regulations (except Part 5) apply to the person`; `regulation 1(5): the two people are treated as spouses or civil partners at the time`; `regulation 1A: the full rate of the state pension, in pounds per week` |
| Reg 2(1) to (3) | SoS (privilege: may withhold payment for a day on which the person is a prisoner) | the person (no-right to payment for that day) | privilege / no-right | `regulation 2(2): the person is a prisoner mentioned in regulation 2(2) on the day`; `regulation 2(1): the state pension is not to be paid for the day` |
| Reg 2(4) | none | none | none: says reg 13 has no effect when rights to relevant benefits are determined (fork F7) | `regulation 2(4): regulation 13 has effect when determining rights to relevant benefits for regulation 2` |
| Reg 3 | the person (claim to payment while remanded in custody, unless a described sentence is later imposed) | SoS (duty to pay) | claim / duty | `regulation 3(1): regulation 2(1) does not apply because the person is remanded in custody`; `regulation 3(2): the sentence is a described sentence` |
| Reg 4(1) to (3), reg 5 | the person (power to choose a lump sum or a survivor's pension, within the period and in the manner) | SoS (liability: bound to pay as chosen) | power / liability | `regulation 4: whether the choice is made within the period`; `regulation 5: the choice is made in the manner required` |
| Reg 4(4) | the person (power to make a late choice, if the SoS considers it reasonable and any lump sum paid has been repaid in full in the original currency) | SoS (liability to pay as chosen once the conditions hold); the person carries the duty to repay first | power / liability; duty | `regulation 4(4): a late choice may be made` |
| Reg 4(5) | SoS (privilege: owes no lump sum once a late pension choice is made) | the person (no-right to the lump sum) | privilege / no-right | `regulation 4(5): the amount of the lump sum` |
| Reg 6 | the person (power to alter a choice, within three months of the notification or a longer period the SoS allows) | SoS (liability to pay as altered); the person carries the duty to repay a lump sum in full, in time, in the same currency, before altering to a pension | power / liability; duty | `regulation 6(1): the choice may be altered`; `regulation 6(2)(c): the application is made within the period`; `regulation 6(2)(e): where the alteration is to a state pension, any lump sum has been repaid` |
| Reg 7, reg 8 | the person (power to suspend by notice, and to pick the start date within 28 days) | SoS (liability) | power / liability | `regulation 7: the person has opted to suspend their entitlement`; `regulation 8: the date from which the suspension takes effect` |
| Reg 9 | the person (power to cancel a suspension for up to 12 months back) | SoS (liability) | power / liability | `regulation 9: the suspension can be cancelled for the period` |
| Reg 10, 12, 12A | the person (claim to an increase for the weeks deferred) | SoS (duty to pay the increase under section 17 of the 2014 Act) | claim / duty | `regulation 10: the weekly increase for the weeks counted`; `regulation 12: the number of whole weeks counted`; `regulation 12A(2): the increment for a modification period` |
| Reg 11 | none | none | none: a counting rule for which days count towards the deferral | `regulation 11: the day does not count in determining the number of whole weeks` |
| Reg 13 | the person (the claim to the reduced or the transitional rate under the 2014 Act exists only with the minimum years) | SoS (duty to pay that rate arises only then; no-right below it) | claim / duty, conditional | `regulation 13: whether the person has the minimum number of qualifying years` |
| Reg 14 | none | none | none: gives the Schedule effect | n/a |
| Schedule, inserted reg 6(1), (6) | the person with shareable rights (claim to the information in paragraphs (2) to (6)); their spouse or civil partner (claim to paragraph (6)); the court (power to order it) | SoS (duty to furnish; liability to the order) | claim / duty; power / liability | `inserted regulation 6(1): the information the Secretary of State must furnish` |
| Schedule, inserted reg 6(2) to (5) | the person (claim to the valuation, or the former Category A amount, that the dates select) | SoS (duty) | claim / duty | `inserted regulation 6(2) to (4): the valuation to be given`; `inserted regulation 6(5): the amount of the former Category A entitlement may be given` |
| Schedule, inserted reg 6(7), (8) | the person, their spouse or civil partner, or the court (claim to the information by a deadline) | SoS (duty to furnish within three months, six weeks, a shorter court period or one month) | claim / duty | `inserted regulation 6(7) and (8): the last day by which the Secretary of State must furnish the information` |
| Schedule, inserted reg 7 | the person (claim that the valuation is calculated and verified on the Government Actuary's guidance) | SoS (duty) | claim / duty | `inserted regulation 7: the valuation is calculated and verified in accordance with the Government Actuary's guidance` |
| Reg 15, 16, 17 | the person (claim to a survivor's pension at the inherited rate, and its up-rating) | SoS (duty to pay) | claim / duty | `regulation 15(2): the person is entitled to a state pension under regulation 15`; `regulation 16: which paragraph gives the person an inherited amount`; `regulation 16(4): the inherited amount, in pounds per week`; `regulation 17: the increase in the rate of the state pension under regulation 15` |
| Reg 18 | the person (power to choose a lump sum or a pension; power to make a late choice on the same conditions as reg 4(4); power to alter under reg 6) | SoS (liability to pay as chosen); the person carries the duty to repay first | power / liability; duty | `regulation 18(1) and (8): the person is entitled to a choice under regulation 18`; `regulation 18(4): a late choice may be made`; `regulation 18: what the person is to be paid` |
| Reg 19, 20 | the person (claim to the lump sum, or to the pension at half the deceased's increase, up-rated by order) | SoS (duty to pay) | claim / duty | `regulation 19(1): the lump sum payable`; `regulation 20(1): the person is entitled to a state pension under regulation 20`; `regulation 20(2): the weekly rate of the state pension under regulation 20` |
| Reg 21 | SoS (privilege: need not pay an up-rating increase to an overseas resident once regulations apply reg 21) | the person (no-right to the increase) | privilege / no-right | `regulation 21: whether the person is entitled to the up-rating increase` |
| Reg 22, 23 | the person (claim to an increment, on the rate and amount the paragraphs choose) | SoS (duty) | claim / duty | `regulation 22: the increment for the part`; `regulation 23(5): the increment where regulations 12A and 22 both apply` |
| Reg 24, 25 | none | none | none: interpretation, a limit on Chapter 3, which Chapter applies, a cap on credits and a counting rule | `regulation 24(2): Chapter 3 can credit the day`; `regulation 25(1): the Chapter that makes provision for the week`; `regulation 25(2): the amount the person is credited with`; `regulation 25(3): the tax year in which the week falls` |
| Reg 26, 27, 29, 30, 31, 32 | the person (claim to a credit) | SoS or HMRC (duty to credit) | claim / duty | `regulation 26: the earnings or contributions credited under the 1975 Regulations`; `regulation 27: the Class 3 contribution credited for parents and carers`; `regulation 29(1): the person is also credited for the purposes of Part 1 of the 2014 Act`; `regulation 30: the person is credited with earnings for the week`; `regulation 31: the person is credited with a Class 3 contribution for the week`; `regulation 32(1): the man is credited with earnings for the week` |
| Reg 28, 33, 34, 36, 37 | the person (claim to a credit, on application where the regulation requires one) | SoS or HMRC (duty to credit); the person carries the duty to apply in the required form and in time | claim / duty; duty | `regulation 28(1): the person is credited with a Class 3 contribution for the week`; `regulation 33(1): the person is credited with a Class 3 contribution for the week`; `regulation 34(1): the person is entitled to be credited with a Class 3 contribution for the week`; `regulation 36: the person is credited with a Class 3 contribution for the week`; `regulation 37(1): the person is credited with a Class 3 contribution for the week` |
| Reg 35(1) to (3) | the person (claim to a credit for caring for a child under 12) | SoS (duty to credit) | claim / duty | `regulation 35(1): the person is credited with a Class 3 contribution for the week` |
| Reg 35(4) | the carers (power to elect, with the other carer's agreement); SoS (power to decide in default) | the other carers and the person (liability) | power / liability | `regulation 35(4): which carer is credited` |
| Reg 38 | the person (claim to twelve further weeks of credit) | SoS (duty to credit) | claim / duty | `regulation 38: the day is credited` |
| Reg 39 | the person (claim to the credit if the application arrives in time, or within a further time the SoS or HMRC consider reasonable) | SoS or HMRC (duty to credit); the person carries the duty to apply in time | claim / duty; duty | `regulation 39: the application is received in time` |

The paired questions in the seat, where the text also puts a duty or a liability on the person, are:

- what I must repay before I change my choice (question 12, reg 6(2)(e));
- what a late choice needs, and what it does to the lump sum (questions 7, 8, 40 and 41, regs 4(4), 4(5), 18(4), 18(6));
- what my application must contain (questions 60, 73 and 79, regs 28(5) and (6), 35(5), 37(6));
- whether my application arrives in time (question 84, reg 39);
- what is withheld from me in custody (question 5, regs 2 and 3), and what living overseas takes from an up-rating increase (questions 47 and 48, reg 21);
- what the Secretary of State must furnish about shared pension rights, and by when, which the person is owed (questions 25 to 29, inserted regs 6 and 7).

## What is encoded and what is not

Encoded: every operative provision of Parts 1 to 8, except the condition in reg 15(1) (fork F37), and inserted regulations 6 and 7 of the Schedule (see the coverage table for the one-line disposition of each provision).

Not encoded, and why.

- The Pensions Act 2014 (the text cites sections 2, 3, 4, 7, 8, 9, 12, 14, 17, 18, 19 and 20) and the other Acts and instruments the text cites are not among the inputs. Where a Regulation depends on one, the effect is taken as a stated plain input: the weekly rate of the deceased's graduated retirement benefit (reg 16(5)), the lump sum under the 2005 Regulations (reg 19(1)), the lower earnings limit and the qualifying earnings factor (Part 8), whether a person is an overseas resident (reg 21), whether the Secretary of State has made regulations applying reg 21 to an increase (reg 21(2)), what the 1975 Credits Regulations would have credited (regs 26, 27), and the content of Schedule 1B to the Income Support Regulations (reg 37(2)(b)).
- Pensionable age (Pensions Act 1995) is a date the person states.
- Judgments left to the Secretary of State or HM Revenue and Customs are conditional inputs, never guessed: reasonableness of a late choice (regs 4(4), 18(4)), a longer period (reg 6(2)(c)), a direction to use writing (regs 5, 6, 7), the level of care (reg 37(2)(a)(ii)), further time (reg 39(a)(ii)).
- Reg 2(4) is encoded only as its stated effect: reg 13 has no effect when rights to relevant benefits are determined (fork F7).
- Lists in the seat. Regs 12A(3) and (4) build the modification periods from a list of the dates of non-uprating changes, and reg 22 takes a list of the parts of a deferral. The seat asks about one change date (question 22) and gives the increment for one period, whose weeks and rate the person states (question 23); it has no question that builds the periods from several dates. Question 49 asks one flag for "any part" of the deferral. Regs 11 and 37(2)(a)(i) take lists of benefits: question 19 asks about one benefit received on the day, and questions 76 and 77 ask one flag for "each person I care for" and stand one placeholder benefit in for the list, which assumes there is at least one person cared for.
- No rule of the Regulations is encoded for what happens after an official decides (recovery of an overpayment after a remand, for example; fork F6).

## Coverage table

Dispositions: `encoded`, `inert` (reason given), `repealed or blank in this text`, `not applicable`.
Line numbers are lines of `uksi-2015-173.txt`.

Counts: encoded 45, inert 7, repealed or blank in this text 1, not applicable 0; 53 rows in all.

| Provision | Lines | Heading (as the text gives it) | Disposition | Where / why |
|---|---|---|---|---|
| Preamble | 1-10 | title, enabling powers, SSAC statement, consultation, draft laid | inert | Recites powers and procedure; it creates no relation for the person. |
| Headings of Parts, Chapters and the Schedule | 11, 23, 26, 45, 140, 144, 147, 274, 308-309, 326, 353, 519, 543 | PART 1, 1A, 2, 3, 4, 5, 6, 7, 8; CHAPTER 1, 2, 3; SCHEDULE; PART 3 inserted by the Schedule | inert | Headings carry no rule. |
| Reg 1(1) | 12-13 | Citation | inert | Gives the short title. |
| Reg 1(2) | 14 | Commencement (6th April 2016) | encoded | spr-part1-general: `regulation 1(2): the commencement date` |
| Reg 1(3) | 15 | Who the Regulations do not apply to | encoded | spr-part1-general: `regulation 1(3): these Regulations (except Part 5) apply to the person`, `... Part 5 applies to the person` |
| Reg 1(4), opening words | 16 | Definition of "the 2014 Act" (shown as repealed) | repealed or blank in this text | Marked {repealed: ...} in the rendering. The same definition is given again at line 19, so nothing is lost (finding 13). |
| Reg 1(4), definitions | 17-21 | "the 1965 Act", "the 2014 Act", "deferral period", "graduated retirement benefit" | encoded | spr-part1-general: `regulation 1(4): the benefit is graduated retirement benefit`; "deferral period" is the record DeferralPeriod in spr-nouns. "The 1965 Act" and "the 2014 Act" only name Acts (inert). |
| Reg 1(5) | 22 | Two people treated as not married when either is married to a third person | encoded | spr-part1-general: `regulation 1(5): the two people are treated as spouses or civil partners at the time` |
| Reg 1A | 24-25 | Full rate of state pension | encoded | spr-part1-general: `regulation 1A: the full rate of the state pension, in pounds per week` |
| Reg 2 | 27-37 | Prisoners who are not to be paid state pension | encoded | spr-part2-prisoners: regulation 2(1), 2(2)(a) to (d), 2(3); 2(4) minimally (fork F7) |
| Reg 3 | 38-44 | Paying state pension to persons who are remanded in custody | encoded | spr-part2-prisoners: regulation 3(1), 3(2) |
| Reg 4 | 46-61 | When a choice of lump sum or survivor's pension may be made | encoded | spr-part3-deferral: regulation 4(1) to (5) |
| Reg 5 | 62-69 | How a choice of lump sum or survivor's pension may be made | encoded | spr-part3-deferral: regulation 5, 5(2) and (3) |
| Reg 6 | 70-91 | Changing a choice of lump sum or survivor's pension | encoded | spr-part3-deferral: regulation 6(1), 6(2)(a) to (h), 6(3) |
| Reg 7 | 92-97 | How entitlement to a state pension may be suspended | encoded | spr-part3-deferral: regulation 7, 7(2) and (3) |
| Reg 8 | 98-103 | Date from which a suspension of a state pension begins | encoded | spr-part3-deferral: regulation 8, 8(2) |
| Reg 9 | 104-107 | Cancelling a suspension of a state pension | encoded | spr-part3-deferral: regulation 9, 9(3) |
| Reg 10 | 108-109 | Percentage for the weekly rate of increases resulting from deferral | encoded | spr-part3-deferral: regulation 10 (percentage and weekly increase) |
| Reg 11 | 110-129 | Days which are not included in determining the period of deferral | encoded | spr-part3-deferral: regulation 11, 11(2)(a) to (c) |
| Reg 12 | 130-132 | Part weeks treated as whole weeks | encoded | spr-part3-deferral: regulation 12 |
| Reg 12A | 133-139 | Modification of the amount of an increment for other cases during deferral | encoded | spr-part3-deferral: regulation 12A(1) to (4) |
| Reg 13 | 141-143 | Minimum number of qualifying years | encoded | spr-part4-qualifying-years: regulation 13 |
| Reg 14 | 145-146 | Sharing of state pension scheme rights | inert | Gives the Schedule effect; the rules are in the Schedule. |
| Reg 15 | 148-156 | Survivor's state pension based on inheritance of graduated retirement benefit | encoded | spr-part6-graduated: regulation 15(2), 15(3); (1)'s condition that the dead spouse paid graduated contributions is not tested (fork F37); (4) only points to regulation 17 (inert) |
| Reg 16 | 157-181 | Inherited amount | encoded | spr-part6-graduated: regulation 16(1) to (4), 16(6); 16(5) (how the deceased's rate is determined) is supplied as an input |
| Reg 17 | 182-216 | Up-rating | encoded | spr-part6-graduated: regulation 17 |
| Reg 18 | 217-247 | Choice of lump sum or state pension based on inheritance of deferred graduated retirement benefit | encoded | spr-part6-graduated: regulation 18(1) to (11) |
| Reg 19 | 248-250 | Survivor's lump sum | encoded | spr-part6-graduated: regulation 19(1), 19(2) |
| Reg 20 | 251-273 | Survivor's state pension based on inheritance of deferred graduated retirement benefit | encoded | spr-part6-graduated: regulation 20(1) to (3); (4) and (5) feed the input the rate is built from |
| Reg 21 | 275-295 | Entitlement to state pension for overseas residents | encoded | spr-part7-overseas: regulation 21(1) to (6) |
| Reg 22 | 296-299 | Modification of the amount of an increment for an overseas resident | encoded | spr-part7-overseas: regulation 22 |
| Reg 23 | 300-307 | Where regulations 12A and 22 both apply | encoded | spr-part7-overseas: regulation 23 |
| Reg 24 | 310-319 | Interpretation (Part 8) | encoded | spr-part8-credits-1: regulation 24(2); the definitions in 24(1) name Acts and regulations (inert) |
| Reg 25 | 320-325 | General provisions relating to the crediting of earnings or contributions | encoded | spr-part8-credits-1: regulation 25(1) to (3) |
| Reg 26 | 327-330 | Credits under the 1975 Regulations (Chapter 2) | encoded | spr-part8-credits-1: regulation 26 |
| Reg 27 | 331-334 | Credits for parents and carers | encoded | spr-part8-credits-1: regulation 27 |
| Reg 28 | 335-352 | Credits for spouses and civil partners of members of Her Majesty's forces (Chapter 2) | encoded | spr-part8-credits-1: regulation 28(1) to (6) |
| Reg 29 | 354-365 | Credits under the 1975 Regulations (Chapter 3) | encoded | spr-part8-credits-2: regulation 29 |
| Reg 30 | 366-382 | Credits for persons in receipt of working tax credit | encoded | spr-part8-credits-2: regulation 30(1) to (3); (4) defines "couple" by another Act (inert) |
| Reg 31 | 383-384 | Credits for persons entitled to universal credit | encoded | spr-part8-credits-2: regulation 31 |
| Reg 32 | 385-393 | Credits for persons approaching pensionable age | encoded | spr-part8-credits-2: regulation 32(1) to (4) |
| Reg 33 | 394-411 | Credits for spouses and civil partners of members of Her Majesty's forces (Chapter 3) | encoded | spr-part8-credits-2: regulation 33(3); (1), (2), (4) to (6) are word for word regulation 28's and call its rules |
| Reg 34 | 412-423 | Credits in respect of an award of child benefit | encoded | spr-part8-credits-3: regulation 34(1) to (4) |
| Reg 35 | 424-459 | Credits for persons providing care for a child under the age of 12 | encoded | spr-part8-credits-3: regulation 35(1) to (8) |
| Reg 36 | 460-469 | Credits for being a foster parent | encoded | spr-part8-credits-3: regulation 36(1) to (3) |
| Reg 37 | 470-505 | Credits for persons engaged in caring | encoded | spr-part8-credits-3: regulation 37(1) to (8) |
| Reg 38 | 506-511 | Credits for an additional period in respect of entitlement to carer's allowance or carer support payment | encoded | spr-part8-credits-3: regulation 38(1), (2) |
| Reg 39 | 512-517 | Time limit for making an application under regulation 34(1)(b), 35, 36 or 37 | encoded | spr-part8-credits-3: regulation 39(a), (b) |
| Signature line | 518 | Signed by authority of the Secretary of State | inert | Formality. |
| Schedule, paragraph 1(1) to (10) lead-in | 520-542 | Amendments to the Sharing of State Scheme Rights (Provision of Information and Valuation) (No.2) Regulations 2000 | inert | These sub-paragraphs rename, renumber and re-title another instrument's provisions; they decide nothing for the person. |
| Schedule paragraph 1(10), inserted regulation 6 | 544-566 | Basic information about the sharing of state scheme rights | encoded | spr-part5-sharing: inserted regulation 6(1) to (8) |
| Schedule paragraph 1(10), inserted regulation 7 | 567-568 | Valuation of shareable old or new state scheme rights | encoded | spr-part5-sharing: inserted regulation 7 |
| Schedule paragraph 2 | 569-582 | Amendment of the Pensions on Divorce etc. (Pension Sharing) (Scotland) Regulations 2000 | inert | Amends definitions and the prescribed form in another instrument; it decides nothing for the person. |

## Fork register

Every ambiguity met, the readings seen, the one taken, and the text that licenses it.
The labels F1 to F36 are the ones used in comments in the `.l4` files; F37 is recorded here only.

**F1** (spr-dates: `the last day of a period of days starting with`)

- Readings: "N days starting with D" is (a) D to D+N-1, so D is day 1, or (b) D+1 to D+N.
- Taken: (a): D is day 1, so the last day is D+N-1.
- Text: "28 days starting with the date" (line 102); "six weeks beginning with the date" (line 561). The period starts with the date itself.

**F2** (spr-dates: `the last day of a period of months starting on`)

- Readings: "N months starting on D" ends (a) the day before the corresponding date N months on, or (b) on the corresponding date. Where the target month has no corresponding day, a third question arises.
- Taken: (a); where there is no corresponding date, the last day of the target month.
- Text: "three months starting on the date in that notice" (line 50), "three months beginning with the date" (line 560). A period that starts on D and runs three months ends the day before D three months on.

**F3** (spr-dates; regs 25(3), 28(3), 33(3), 34(3), 39)

- Readings: A "year" in Part 8 is a tax year (reg 24(1)) but the text never says it runs 6 April to 5 April.
- Taken: 6 April to 5 April, named by the calendar year it starts in.
- Text: Regulation 28(3) speaks of "a year beginning on or after 6th April 1975 and ending before 6th April 2016" (line 340) and 33(3) of "6th April 2016" (line 399).

**F4** (spr-dates: `the number of days from`)

- Readings: Days between two dates by calendar or by serial number.
- Taken: Serial-number difference.
- Text: No text; a counting convention.

**F5** (spr-part2-prisoners: regulation 2(2)(c))

- Readings: "on or before the day which the Secretary of State certifies to be the person's release date (if any)": with no certified date, (a) the condition is met or (b) not met.
- Taken: (a): met.
- Text: "(if any)" (line 34) treats the absence of a date as possible; the detention condition would otherwise never be met for a person held without a date.

**F6** (spr-part2-prisoners: regulation 3(1))

- Readings: Whether payments for the remand period are recovered if a described sentence is later imposed.
- Taken: Not encoded: the text says only that reg 2(1) "does not apply unless" such a sentence is later imposed.
- Text: Line 39. The text gives no recovery rule.

**F7** (spr-part2-prisoners: regulation 2(4))

- Readings: "relevant benefits" is not defined here, and the paragraph names "regulation 13 of the State Pension Regulations 2015" inside those Regulations; what replaces reg 13 is not said.
- Taken: Only the stated effect is encoded: reg 13 does not have effect when determining those rights.
- Text: Line 37.

**F8** (spr-part1-general; spr-part6-graduated; seat cases)

- Readings: Regulation 1(3) takes a person who reaches pensionable age before 6 April 2016 outside the Regulations (except Part 5); regs 16(3), 18(1)(d)(ii) and 20(1)(c)(ii) speak of a person over pensionable age when the spouse died.
- Taken: The literal reading: the gate in 1(3) is a separate question, asked first; regs 15 to 20 answer on their own terms.
- Text: Lines 15, 166-168, 224, 257; finding 1.

**F9** (spr-part1-general: regulation 1(5))

- Readings: The paragraph speaks of marriage to a third person; for a civil partner in a civil partnership with a third person it is silent.
- Taken: A civil partnership is taken as it stands.
- Text: Line 22: "two people are to be treated as if they are not married to each other in relation to times when either of them is married to a third person".

**F10** (spr-part1-general: regulation 1A)

- Readings: The full rate has changed over time; the text gives one figure.
- Taken: 241.30 a week, with no date range.
- Text: Line 25, in the 2026-04-06 revised text.

**F11** (spr-part3-deferral: regulations 4(4)(b), 6(2)(e); reg 18(4))

- Readings: Where no lump sum was paid, the repayment limb is (a) met (nothing to repay) or (b) not met.
- Taken: (a).
- Text: "any amount paid ... has been repaid" (lines 58-60, 84-87): no amount, no repayment to prove.

**F12** (spr-part3-deferral: regulation 6(2)(e)(ii))

- Readings: "within the period mentioned in sub-paragraph (c)": (c) has two limbs, three months and a longer period.
- Taken: The later end.
- Text: Lines 78-80 and 86 (regulation 6(2)(c) and (e)(ii)).

**F13** (spr-part3-deferral: regulation 8(2)(b))

- Readings: "not after 28 days starting with the date": the latest day is (a) exercise day + 27 or (b) + 28.
- Taken: (a), by F1.
- Text: Line 102.

**F14** (spr-part3-deferral: regulations 10, 12)

- Readings: Sections 17(3) and (4) of the 2014 Act, which regs 10 to 12 modify, are not among the inputs.
- Taken: Whole weeks = CEILING (days counted / 7); the weekly increase = one-ninth of 1% x weeks x the reference weekly rate.
- Text: Lines 109, 111-132: reg 12 makes a part of a week a whole week.

**F15** (spr-part3-deferral: regulation 12A(3), (4))

- Readings: How the change dates are ordered, and whether the periods include both end days.
- Taken: Dates in date order; the last period ends on the last day of the deferral; periods include both end days.
- Text: Lines 136-139.

**F16** (spr-part3-deferral: regulation 12A(2); spr-part7-overseas: regulation 22)

- Readings: How the whole weeks counted are shared among the modification periods or the parts of a deferral is not said.
- Taken: The weeks for each period or part are an input.
- Text: Lines 135, 297-299.

**F17** (spr-part3-deferral: regulation 4(2), (3))

- Readings: Which notice counts when more than one has been issued, and what its "date" is.
- Taken: The most recent notice issued before the choice; the date printed in it.
- Text: Line 50: "the date in the most recent such notice".

**F18** (spr-part5-sharing: inserted regulation 6(7))

- Readings: (a), (b) and (c) are alternatives; a court's shorter period might also extend time; (c) might apply to any requester.
- Taken: The earliest that applies is the last day; a court period later than three months does not extend time; (c) is for the court's order only.
- Text: Lines 559-566.

**F19** (spr-part6-graduated: regulation 18)

- Readings: A choice not made in the manner reg 5 requires is (a) a choice or (b) no choice.
- Taken: (b): no choice, so the default lump sum follows.
- Text: Line 228 ("the manner set out in regulation 5(2) and (3)"), line 234 ("fails to make a choice within the period").

**F20** (spr-part6-graduated: regulations 16, 18, 20)

- Readings: "under pensionable age" and "over pensionable age" on the day the person reaches it.
- Taken: Strict: on that day the person is neither, and the rules return a not-covered result or false.
- Text: Lines 164, 168, 223-224, 255-257. The text has no "at" or "on reaching".

**F21** (spr-part6-graduated: regulation 17)

- Readings: At R = 0 and S = F, paragraphs (3)-(4) and (8)-(9) both describe the case.
- Taken: The full-rate percentage of paragraph (3)-(4) is taken first.
- Text: Lines 188-192 and 207-212.

**F22** (spr-part6-graduated: regulation 18(1))

- Readings: When the person "becomes entitled to make the choice".
- Taken: The later of the date they reach pensionable age and the date of the death.
- Text: Lines 218-224 and 250 (reg 19(2)).

**F23** (spr-part7-overseas: regulations 21(4), 21(5))

- Readings: "at the time of that increase" and "immediately before the up-rating increase comes into force" might be different moments.
- Taken: The same moment.
- Text: Lines 289 and 292-294.

**F24** (spr-part7-overseas: regulation 23(3), (5))

- Readings: What the "increase or decrease" under 12A is measured against is not said.
- Taken: The difference regulation 12A makes, supplied as a signed input.
- Text: Lines 303-307.

**F25** (spr-part7-overseas: regulation 21(2))

- Readings: Whether regulations have been made applying reg 21 to a given up-rating increase is not in the inputs.
- Taken: A plain input, which gates the whole regulation.
- Text: Lines 277-281.

**F26** (spr-part7-overseas: regulation 21(4)(a))

- Readings: "in respect of the deferral period": an increase that comes into force during it, or one that would have been paid for it.
- Taken: An increase that comes into force during it, both end days included.
- Text: Lines 287-290.

**F27** (spr-part7-overseas: regulation 22)

- Readings: A person who was an overseas resident but in Great Britain or a specified territory during a part is in neither paragraph (2) nor (3).
- Taken: No reference rate for that part.
- Text: Lines 297-299.

**F28** (spr-part8-credits-1: regulation 25(1))

- Readings: Where the line between Chapter 2 and Chapter 3 falls; the 2014 Act definitions are not in the inputs.
- Taken: At the tax year starting 6 April 2016.
- Text: Regs 28(3), 33(3) (lines 340, 399) and 24(2) (line 319).

**F29** (regs 28(4)(b), 30(3)(b), 33(4)(b), 37(8))

- Readings: "a woman ... an election made by her" is two facts or one.
- Taken: One input: the person is a woman with an election in force.
- Text: Lines 348, 381, 407, 505.

**F30** (regs 30(1)(b), 32(4)(a))

- Readings: The rendering carries a literal "..." where words are missing.
- Taken: The words that remain are quoted and encoded as they stand.
- Text: Lines 369, 392.

**F31** (spr-part8-credits-3: regulation 39(b))

- Readings: "after the end of the year in which a week ... falls" for a regulation 35 application: a minimum wait only, or a drafting slip for "before the end of the year following".
- Taken: Read literally: received after the end of that year; no latest date.
- Text: Line 517 against line 515.

**F32** (spr-part8-credits-3: regulation 39(a)(i))

- Readings: "before the end of the year following that in which a week ... falls": receipt on the last day is in or out of time.
- Taken: In time.
- Text: Line 515: the year has not ended until its last day has.

**F33** (spr-part8-credits-3: regulation 38)

- Readings: Length of a "week" and of the 12-week period; which date anchors it.
- Taken: Seven days; 84 days; the date of becoming entitled for "prior to", the last day of the week for "following".
- Text: Lines 507-510.

**F34** (spr-part8-credits-3: regulation 39(a)(ii))

- Readings: "within such further time": a time that replaces or adds to (i).
- Taken: A last day supplied by the person; receipt on or before it is in time; it never shortens (i).
- Text: Line 516.

**F35** (spr-part8-credits-3: regulation 35(4))

- Readings: While no election is agreed and the Secretary of State has not decided, who is credited is not said.
- Taken: A result that says so; nobody is credited yet.
- Text: Lines 436-438.

**F36** (spr-part8-credits-3: regulation 37(5), (8))

- Readings: Whether paragraph (5) binds the (2)(b) route and what (8) does.
- Taken: (5) binds only a credit under (2)(a); the (2)(b) route needs no application; (8) lifts the requirement for a woman with an election in force.
- Text: Lines 496, 505.

**F37** (spr-part6-graduated: regulation 15(1))

- Readings: Paragraph (1) limits the regulation to a person "whose dead spouse or civil partner paid graduated contributions as an insured person"; paragraph (2) lists the conditions without it.
- Taken: Not tested as a separate input. The deceased's weekly rate of graduated retirement benefit (reg 16(5)) is an input, so a spouse who paid none is a rate of 0; the entitlement rule (reg 15(2)) then still answers yes, at a nil weekly rate.
- Text: Lines 149 and 150-155.

## What the text turns out to say

Numbered findings.
Each ends "Asserted." where a case in a test file or `spr-cases-seat.l4` asserts it.

1. A person who reaches pensionable age before 6 April 2016 is outside the Regulations (except Part 5) by reg 1(3), yet reg 16(3) (and 18(1)(d)(ii), 20(1)(c)(ii)) give rights to a person who was over pensionable age when their spouse or civil partner died on or after that day. Someone who reached it on 1 January 2016 and whose spouse (pensionable age 2010) died on 1 June 2016 is inside the words of reg 16(3) and outside the gate. The seat asserts both answers side by side (`spr-cases-seat.l4`, the block headed "Finding 1"). Asserted.
2. Reg 39(b) says an application under reg 35 must be received "after the end of the year in which a week ... falls". As written that is a minimum wait with no latest date, where paragraph (a) gives the other applications a deadline. It may be a slip for "before the end of the year following". The encoding reads it literally (fork F31): received during the year is out of time, the day after the year ends and any later date are in time. Asserted in `spr-tests-part8-credits-3.l4`.
3. A woman with a reduced rate election in force is shut out of the credits in regs 28(4)(b), 30(3)(b) and 33(4)(b), but reg 37(8) lifts the application requirement for her under reg 37 (paragraph (5) opens "Except in a case to which paragraph (8) applies"). The two treatments point opposite ways (forks F29, F36). Asserted in the tests for regs 28, 30 and 37 and in `spr-cases-seat.l4`.
4. The reg 37(2)(b) route (paragraph 4, 5 or 6 of Schedule 1B to the Income Support (General) Regulations 1987) needs neither the hours nor an application: reg 37(5) binds only a credit under paragraph (2)(a). Asserted in `spr-tests-part8-credits-3.l4` and `spr-cases-seat.l4`.
5. Reg 35(4) says what happens when several people can satisfy the care condition (they elect, with agreement, or the Secretary of State decides in default of agreement). It does not say who is credited while neither has happened, so the result says "the Secretary of State has not yet decided which carer is credited" (fork F35). Asserted in `spr-tests-part8-credits-3.l4` and `spr-cases-seat.l4`.
6. Reg 22(2) gives a reference rate for a part of the deferral when the person was an overseas resident outside Great Britain and the specified territories, and reg 22(3) for a part when the person was not an overseas resident. An overseas resident who was in Great Britain or a specified territory for a part is in neither: the rule returns "regulation 22 gives no reference rate for this part" (fork F27). Asserted in `spr-tests-part7.l4`.
7. Reg 17 has gaps. An up-rating order alone gives nothing where the person's rate plus the other pensions is at most the full rate (paragraphs (3) and (4) wait for an increase in the full rate); a full-rate increase alone gives nothing where the other pensions alone reach the full rate (paragraphs (8) and (9) wait for an order); and where the sum is at most the full rate and both events happen, only the full-rate percentage has a paragraph. At a sum exactly equal to the full rate paragraphs (3) and (4) apply, so an order alone gives nothing rather than an increase on an excess of nil. Asserted in `spr-tests-part6.l4` and `spr-cases-seat.l4`.
8. "Under pensionable age" and "over pensionable age" are strict in regs 16, 18 and 20: on the day a person reaches pensionable age they are neither, so a spouse's death on that day gives no inherited amount under reg 16(1) to (3) (fork F20). Asserted in `spr-tests-part6.l4`.
9. Reg 13 sets ten qualifying years for the reduced rate and ten for the transitional rate, and no number for the full rate (the 2014 Act sets that). The rule returns "these Regulations do not set the number of qualifying years for this rate" for the full rate. Asserted in `spr-tests-part4.l4`.
10. Reg 4(3): a choice made before any notice has been issued is in time on or after the later of the day the person claims and the day the spouse or civil partner died, because the period ends on the date of the choice. With a claim on 1 March and a death on 10 February, a choice on 1 March is in time and one on 28 February is outside. Asserted in `spr-tests-part3.l4`.
11. Reg 6(2)(e)(ii) requires the lump sum to be repaid within the period mentioned in paragraph (c), not only the application to be made within it. Repayment completed a day after the period ends fails the condition, and the last day of the period passes it (fork F12). Asserted in `spr-tests-part3.l4`.
12. Reg 21 bites on an up-rating increase only if regulations have been made applying it to that increase (reg 21(2)); those regulations are not among the inputs (fork F25). Without them the rule says that regulation 21 does not apply. Asserted in `spr-tests-part7.l4`.
13. The words that open reg 1(4) are shown as repealed in the 2026-04-06 text (line 16), but the definition of "the 2014 Act" they carried is given again among the definitions at line 19, so no rule turns on the repeal. Not assertable.
14. Reg 35(6)(k) reads "in respect of a son or daughter of a person listed in sub-paragraph (f), that person's spouse ... civil partner ... or partner". If "that person" is the person in (f), (k) repeats (g) to (i); if it is the son or daughter (a cousin), it adds a cousin's spouse or partner. The encoding accepts the paragraph's own words as one of the listed relationships and does not choose. Asserted in `spr-cases-seat.l4`.
15. Regs 28 and 33 are word for word the same except paragraph (3) (diffing lines 336 to 352 against lines 395 to 411 shows one differing line, which is paragraph (3)). Reg 28 covers years from 6 April 1975 to before 6 April 2016, reg 33 years from 6 April 2016. A week is counted in the tax year in which it begins (reg 25(3)): a week starting on 5 April 2016 is in tax year 2015 and a week starting on 6 April 2016 in tax year 2016 (forks F3, F28). Asserted in `spr-tests-part8-credits-1.l4`.
16. Reg 38 does not say what a "week" is or which day anchors the twelve weeks. The encoding takes 84 days, ending the day before the date of becoming entitled, or starting the day after the last day of the week in which entitlement or caring ceases (fork F33). Asserted in `spr-tests-part8-credits-3.l4`.
17. The rendering carries a literal "..." in reg 30(1)(b) ("who would otherwise... be treated as having actually paid") and reg 32(4)(a) ("... would be treated as having actually paid"), where words are missing. The words that remain are encoded as they stand (fork F30). Not assertable.
18. Reg 39(a)(i) "before the end of the year following that in which a week ... falls": an application received on the last day of that year is in time and one received the next day is not (fork F32). Asserted in `spr-tests-part8-credits-3.l4`.
19. Reg 2(2)(c): a person detained in hospital under section 47 of the Mental Health Act 1983 with no certified release date is still a prisoner (fork F5); with a certified date the person is a prisoner on and before it and not after. Asserted in `spr-tests-part2.l4`.
20. Reg 3(1) says reg 2(1) "does not apply" to a person remanded in custody unless a described sentence is later imposed. The text does not say whether payments made during the remand are recovered if one is (fork F6). Not assertable.
21. Reg 1(5) speaks of marriage only: two civil partners, one of whom is married to a third person, are not taken out of their civil partnership (fork F9). Asserted in `spr-tests-part1.l4`.
22. Reg 16(6): the date at which the deceased's graduated retirement benefit rate is determined is the date the person reaches pensionable age for paragraphs (1) and (2), and the date of the death for paragraph (3). Asserted in `spr-tests-part6.l4`.
23. Reg 15(1) limits the regulation to a person "whose dead spouse or civil partner paid graduated contributions as an insured person", and reg 15(2) lists its conditions without that one. The encoding tests only the conditions in (2) (fork F37), so a spouse who paid none (a weekly rate of 0) still gives entitlement under reg 15(2) and a nil rate under reg 15(3), not NOTHING. This is a limit of the encoding, pinned by a seat case so that it is visible. Asserted in `spr-cases-seat.l4`.
24. A choice of a state pension made outside the period, or in a way the Regulations do not accept, and not allowed as a late choice, is no choice: reg 18(5) pays a lump sum under reg 19 (fork F19). Where a late choice of a pension is allowed, the lump sum is reduced to nil (regs 4(5) and 18(6)). Asserted in `spr-tests-part3.l4` and `spr-tests-part6.l4`.

## What the stable binary does not accept

Met while writing, with the workaround used.

- `YMD` is missing from the stable prelude: `spr-dates.l4` defines the shim `YMD y m d MEANS Date d m y`.
- `days between` is not in `daydate` (it is in `actus-daycount`): the rule `the number of days from` ... `to` ... subtracts `DATE_SERIAL`s.
- `length` is not in scope: use `count`.
- A `GIVEN` with two parameters, one of them a list, must put each on its own line; a comma after `LIST OF DATE` is a parse error.
- `EMPTY OF NUMBER` is not valid; use `EMPTY`.
- A multi-line `(Record WITH ...)` as the argument after `THEN fn` is a parse error: bind it in a `WHERE`.
- `JUST 5%` and `6 5%` are type errors: a percent literal given as an argument is parenthesised, `JUST (5%)` and `6 (5%)`.
- `NOT` binds loosely: every `NOT` is parenthesised. `#ASSERT` lines are one line.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used.
- The brief names `references/drafting-patterns.md`, `references/source-patterns/` and `references/dialects.md` of the `writing-l4-rules` skill; the copy in `SKILLS_DIR` has only `builtins.md`, `gotchas.md` and `regulative.md`, so those three were not read.
- Worked: `@export` and `@desc` on a rule that takes no input (the reg 1A question), `MAYBE` and enumerated results from a `DECIDE`, and `%` applied to a plain `NUMBER` input.

## What check.sh prints

`L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, run in this folder; the last column, `written`, is the count of `#ASSERT` lines in the file and must equal satisfied plus failed plus refused.

```
module                                    errors satisfied  failed  refused  expected  written
spr-cases-seat.l4                              0       420       0        0         0      420
spr-dates.l4                                   0         0       0        0         0        0
spr-nouns.l4                                   0         0       0        0         0        0
spr-part1-general.l4                           0         0       0        0         0        0
spr-part2-prisoners.l4                         0         0       0        0         0        0
spr-part3-deferral.l4                          0         0       0        0         0        0
spr-part4-qualifying-years.l4                  0         0       0        0         0        0
spr-part5-sharing.l4                           0         0       0        0         0        0
spr-part6-graduated.l4                         0         0       0        0         0        0
spr-part7-overseas.l4                          0         0       0        0         0        0
spr-part8-credits-1.l4                         0         0       0        0         0        0
spr-part8-credits-2.l4                         0         0       0        0         0        0
spr-part8-credits-3.l4                         0         0       0        0         0        0
spr-seat.l4                                    0         0       0        0         0        0
spr-tests-dates.l4                             0        19       0        0         0       19
spr-tests-part1.l4                             0        16       0        0         0       16
spr-tests-part2.l4                             0        33       0        0         0       33
spr-tests-part3.l4                             0       118       0        0         0      118
spr-tests-part4.l4                             0        11       0        0         0       11
spr-tests-part5.l4                             0        31       0        0         0       31
spr-tests-part6.l4                             0        99       0        0         0       99
spr-tests-part7.l4                             0        37       0        0         0       37
spr-tests-part8-credits-1.l4                   0        54       0        0         0       54
spr-tests-part8-credits-2.l4                   0        56       0        0         0       56
spr-tests-part8-credits-3.l4                   0       156       0        0         0      156
TOTAL (25 modules)                             0      1050       0        0               1050
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <inputs>/uksi-2015-173.txt spr-*.l4` reports 0 problems.
Every `-- src:N` line is a mechanical copy of line N of the source, produced by `srcrefs.py quote`, never typed.

Positive controls (mutation): a copy of the deposit with one line of a layer-1 module changed, the tests rerun, and the run abandoned if the change did not alter the file.
- Eleven single-line changes, one in each of `spr-dates`, Parts 1 to 7 and the three Part 8 modules (the day a month period ends; the commencement date; `AT MOST` to `LESS THAN` in reg 2(2)(c); three months to four in reg 4(2); ten qualifying years to eleven in reg 13(1); 42 days to 43 in inserted reg 6(7); `AT MOST` to `LESS THAN` in reg 17; `AT LEAST` to `GREATER THAN` in reg 21(4); the same in reg 24(2); `GREATER THAN 182` to `AT LEAST 182` in reg 32; 84 to 85 days in reg 38) each failed at least one assertion in that module's own test file.
- Fifteen single-line changes to layer 1 (regs 1(2), 4(2), 6(7) inserted, 8(2), 9(3), 12, 13(1), 17, 21(4), 24(2), 32, 37(2)(a), 38, 39(a), and the month-period helper) each failed at least one assertion in `spr-cases-seat.l4`. The first run of the reg 17 change was NOT caught by the seat; a boundary case (the person's rate plus the other pensions exactly equal to the full rate, with only an order) was added and the change is now caught.
- Five changes to the seat's own wiring each failed between 1 and 15 assertions.

## What would need doing before the encoding is worth relying on

1. A domain expert reads each rule against the official text of S.I. 2015/173 (the file here is a converter rendering; two places, regs 30(1)(b) and 32(4)(a), show a literal "...").
2. Bring in the sections of the Pensions Act 2014 that the text cites (2, 3, 4, 7, 8, 9, 12, 14, 17, 18, 19 and 20), so that the increase, the lump sum and the rates stop being inputs.
3. Add pensionable age from the Acts that fix it, so the person need not state the date.
4. Add the yearly figures: the full rate by date, the lower earnings limit, the qualifying earnings factor, the up-rating orders.
5. Decide the forks that change an answer: F8 and finding 1 (the reg 1(3) gate), F31 (reg 39(b)), F29 and F36 (the reduced rate election), F25 (whether regulations have been made under reg 21(2)), F20 (the day a person reaches pensionable age).
6. Check the one-item list limits in the seat against real cases (several change dates under reg 12A; several parts under reg 22).
7. Re-run the checks against a later revised text; this one is the text at 2026-04-06 only.


## Added after the run: the date as data

`spr-made.l4` was added by the lead after the agent finished, at the maintainer's request that the date of enactment be kept as data for rule-effective-date logic.
It is one definition with a quoted source line and an `@ref`; no rule reads it yet.
