# Notes: the Old Age Security Act, Parts II and III (piece oa2)

Status: the layer-1 modules, their tests, the seat layer and the worked cases are written, and "What check.sh prints" holds the output of the last run of `check.sh` on this folder. PROGRESS.md says what was done and in what order.

**The text.**
`R.S.C.-1985-c.-O-9.txt` is an unofficial plain-text rendering made by a converter script from the Justice Laws XML repository, a consolidation current to 2026-09-30.
It is not the official text, it drops historical notes, footnotes and French items, and nothing here is verified against the official text.
The `-- src:N |` lines in the modules are copied from the rendering by `srcrefs.py quote`, so they show what the rendering says and nothing more.
This piece covers lines 227-822 of the Act file: Part II (Monthly Guaranteed Income Supplement, sections 10 to 18.2) and Part III (Monthly Allowances, sections 19 to 26).
Layer 1 encodes nothing from the Regulations (those are piece oa3's); where the Act leaves a rule or a figure to them it is a plain input named for the fact, and the Cross-references table says which Regulation it comes from. The seat takes one figure from the Regulations (Regulation 26.1(1), for s 18.2(1)), as the Seat section says.

**The files.**
Layer 1 is ten modules, each with a test file: `oa2-indexation` (the shared quarterly index step), `oa2-part2-eligibility` (ss 10, 11), `oa2-part2-amount` (ss 12, 12.1), `oa2-part2-income` (ss 13, 14), `oa2-part2-spouse` (s 15), `oa2-part2-payment` (ss 16 to 18.2), `oa2-part3-spouse-allowance` (ss 19, 20), `oa2-part3-survivor-allowance` (ss 21, 21.1), `oa2-part3-amount` (ss 22, 22.1) and `oa2-part3-payment` (ss 23 to 26).
Layer 2 is `oa2-seat.l4` and `oa2-cases-seat.l4`.
The keel's `oas-core*.l4` files are used as they are.

## Seat

**The seat.**
A person who is 65 or older, or approaching it, asking whether they qualify for the Old Age Security pension's Guaranteed Income Supplement or for an Allowance (the 60-to-64 allowances of Part III), how much they would receive, and what they must do or tell the Minister.
The Commons ruling of 2026-10-18 puts every encoding in the seat of the individual to whom the law is applied, never the Minister or the department; the brief for this piece names this seat.
The seat is two files: `oa2-seat.l4` (60 questions, each with `@export` and `@desc` on every input, grouped under `§` headings in the text's order) and `oa2-cases-seat.l4` (at least one worked case per question, 149 assertions).
The seat calls the rules of the layer-1 modules and restates none of them.
The Minister's side of each relation (has approved, has waived, has deemed, is satisfied) is a plain yes/no input the person can state.

**How the inputs are shaped.**
- Yes/no, numbers, dates and the modules' own lists are the only input types. An optional date is a `MAYBE DATE` and its `@desc` says "leave blank if none".
- The records the modules expect (the facts about a pensioner and a month, the facts about a person who may be paid an allowance, the special qualification facts, a sentence of imprisonment, the figures for an estimate of income) are built inside each question, in its `WHERE`, from the person's answers.
- A record field that the rule called never reads is given a fixed value, and the comment on the question says so (for example `s 11(7)(a)` reads only the month of the application, and `s 21(6)` reads only the month the person became a survivor and the date of birth).
- Fixed value (assumed, not ruled): in the two composite allowance questions the month in which the person dies is left blank, because the person asks about their own entitlement while living.
- Published figures are inputs, copied by the person from the government's tables: the maximum supplement for a quarter, the supplement equivalent, the figure A of section 12.1 and 22.1, the Consumer Price Index figures.
- Prescribed rules that the Act leaves to the Regulations are inputs in layer 1, as the brief's cross-reference rule requires. The seat takes one figure from the Regulations themselves, as the brief's "use the Regulations' figures" asks: for s 18.2(1) it fixes the manner and the time at what Regulation 26.1(1) says (a request to the Minister in writing, no later than six months after the day payment begins; read at src `C.R.C.-c.-1246.txt:283`). The earlier date of s 23(1) is computed by Regulation 12 (piece oa3), which a person cannot be expected to apply, so the question on s 23(1) about an earlier effective date asks for the date as an input (blank if none); at the merge it should call oa3's rule for Regulation 12 instead. The question on s 23(2) needs no such input: the Act itself states the date (the later of a year before the application was received and the 60th birthday).
- Dates the text does not give (the month paragraph 19(6)(e) and subsection 21(7.1) came into force) are inputs.

**Readings the seat takes (see the fork register).**
Maximum and amount of the supplement for every month after December 1997 use s 12(5) (F-12-1); s 18(b) is read as the mirror of (a) (F-18-1); the age 60 to 64 is tested on the last day of the month before the month (F-AGE-1).

**What the seat does not ask.**
Layer 1 encodes every provision of the range (see the coverage table); the seat asks only the questions the person would put.
Provisions with no question of their own are still in layer 1, and the coverage table's "where" column names their rules.
The provisions whose rules are called by no seat question, directly or through another rule, are (computed by following rule calls from the seat to the layer-1 modules, so a provision reached only through a rule the seat calls is not in the list): s 12(1), s 12(5.1), s 12.1(2.1), s 12.1(3), s 12.1(4), s 12.1(5), s 13, s 14(1.01), s 14(1.1), s 14(1.2), s 14(4), s 14(5), s 14(6), s 15(2), s 15(2.1), s 15(2.2), s 15(2.3), s 15(2.4), s 15(3), s 15(3.1), s 15(3.2), s 15(3.3), s 15(4), s 15(4.2), s 15(5), s 15(5.1), s 15(6.1), s 15(7.1), s 15(8), s 18.2(2), s 19(4.01), s 19(4.1), s 19(4.3), s 19(9), s 21(5.1), s 21(5.3), s 21(11), s 21(12), s 21.1(3), s 22(2.1), s 22(4.1), s 22(4.2), s 22(4.3), s 22(4.4), s 22.1(3.1), s 22.1(4), s 22.1(5), s 22.1(6), s 26(1), s 26(2).
The seat gives the person the figures that the Act builds from published data (the maximum supplement, the supplement equivalent, the figure A, the price indexes) as inputs, which is why ss 12(1), 12.1(2.1) to (5), 22(4.1) to (4.4) and 22.1(3.1) to (6) appear in that list.

**The questions.**

1. May I be paid the Guaranteed Income Supplement for this month (ss 10, 11)?
2. In which month is the earliest for which a supplement can be paid to me, if I apply late (s 11(7)(a))?
3. By what day must I file a statement correcting inaccuracies if the Minister tells me my application for the supplement will be waived (s 11(3.3))?
4. Did I decline the waiver in time (s 11(3.4))?
5. By what day may the Minister notify me that I must apply for later months (s 11(5))?
6. What is the maximum monthly supplement for a payment quarter after June 2005 (s 12(2))?
7. How much supplement can I be paid for this month (s 12(5))?
8. What is my monthly base income for the supplement (s 12(6))?
9. How much may be added to my supplement if I have no spouse, or my spouse gets no benefit (s 12.1(1))?
10. How much may be added to my supplement if my spouse also gets a pension (s 12.1(2))?
11. Must I state my income for the base calendar year when I apply (s 14(1))?
12. May I file a statement of estimated income because I stopped work (s 14(2))?
13. What income will be counted if I file a statement of estimated income because I stopped work (s 14(2))?
14. From which month can a supplement calculated on my statement be paid (s 14(7))?
15. Must I say in my application whether I have, or had, a spouse or common-law partner (s 15(1))?
16. Must I tell the Minister without delay that my situation has changed since my last payment period (s 15(1.1))?
17. Must I tell the Minister without delay if I separate, or lose my spouse or partner (s 15(9))?
18. Will my supplement be worked out as though I had, or had no, spouse for a month in which we are separated (s 15(4.1))?
19. Will my supplement be worked out as though I had no partner after my common-law partner dies (s 15(7.2))?
20. Must the Minister consider my application for the supplement without delay (s 16(1))?
21. If I ask, will the Minister tell me in writing how my amount was worked out (s 16(2))?
22. Will the Minister tell me in writing why no supplement may be paid to me (s 16(2))?
23. What is the earliest day on which payment for this month can be made (s 17)?
24. What is the latest day on which payment for this month can be made (s 17)?
25. How much will be deducted from my later payments if my income turns out to have been higher than I showed (s 18(a))?
26. How much will be paid to me if my income turns out to have been lower than I showed (s 18(b))?
27. On what day does my supplement stop if I ask the Minister in writing to stop it (s 18.1)?
28. From which month can my supplement start again after I asked for it to stop (s 18.1)?
29. Can my supplement still be paid for this month although I asked for it to stop (s 18.1)?
30. May I ask for my supplement to be cancelled after payment has started (s 18.2(1))?
31. May I be paid an Allowance for this month as the spouse or common-law partner of a pensioner (s 19)?
32. By what day may the Minister notify me that I must apply for later months of the Allowance (s 19(4.2))?
33. How much Allowance may I be paid for this month as the spouse or common-law partner of a pensioner (ss 19(7), 22(3))?
34. May payment of my Allowance be suspended if I do not comply with the Act (s 20)?
35. May payment of my suspended Allowance be resumed (s 20)?
36. May the Minister work out my Allowance without counting the pensioner's income because we do not live together (s 19(8))?
37. May I be paid an Allowance for this month as a survivor (s 21)?
38. From which month may a survivor's Allowance be paid to me (s 21(6))?
39. By what day may the Minister notify me that I must apply for later months of the survivor's Allowance (s 21(5.2))?
40. How much Allowance may I be paid for this month as a survivor (ss 21(10), 22(4))?
41. Is a survivor's Allowance not payable to me because I have been convicted of killing my spouse or partner (s 21.1(1))?
42. Must I repay an Allowance I received if I am found to have been convicted of killing my spouse or partner (s 21.1(4))?
43. Will the Minister repay what was recovered from me if my conviction is reversed (s 21.1(2))?
44. Will I be paid a supplement under section 22(2) instead of under Part II because my spouse or partner has applied for an Allowance (s 22(2))?
45. Am I treated as having applied for the supplement under Part II when my spouse or partner's Allowance application is approved (s 22(7))?
46. May I be paid the Part II supplement again for a month in which my spouse's or partner's Allowance is suspended or has ended (s 22(5))?
47. How much supplement may I be paid for the month when my spouse or partner is paid an Allowance (s 22(6))?
48. How much may be added to my Allowance as the spouse or common-law partner of a pensioner (s 22.1(2))?
49. How much may be added to my Allowance as a survivor (s 22.1(3))?
50. In which month does payment of my Allowance start (s 23(1))?
51. Can my approval be made effective from an earlier date if it was approved after the month I applied (s 23(1))?
52. How far back may payment of my Allowance start if the Minister waived my application (s 23(1.1))?
53. How far back may my approval be made effective if I applied after turning 60 (s 23(2))?
54. Does my Allowance start in the month I am released from prison (s 23(3))?
55. Must the Minister consider my application for an Allowance without delay (s 24(1))?
56. Will the Minister tell me in writing how the amount of my Allowance was worked out, if I ask (s 24(2))?
57. Will the Minister tell me in writing why no Allowance may be paid to me (s 24(2))?
58. What is the earliest day on which my Allowance for this month can be paid (s 25)?
59. What is the latest day on which my Allowance for this month can be paid (s 25)?
60. May the Minister waive my having to file information again for the Allowance if I already gave it for the supplement (s 26(1.1))?

## Jural relations

Hohfeld's pairs: a claim (right) is matched by a duty, a privilege by a no-right, a power by a liability, an immunity by a disability.
Each relation is stated once, in layer 1, and named neutrally, never once from each side; the seat takes the other party's side as plain inputs.
The Act's "may be paid" is read with s 16(1) and s 24(1), which speak of whether the applicant "is entitled to be paid": the person's claim is conditional on the Minister's approval of payment, and the Minister's duty is to consider the application without delay and decide.
Where a rule below says the person "may" or "must" do something, it is a rule over the facts the section names, answering whether the section lets or requires it.
The Minister, the Crown and the other persons named appear only as the other party of a relation; none has a seat of its own.

| relation | holder (claim, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | section | L4 rule |
| --- | --- | --- | --- | --- |
| The supplement for a month | the pensioner: claim | the Minister: duty to approve and pay | s 11(1), (2) | `s 11(1): a supplement may be paid to the person`; `s 11: a supplement may be paid to the pensioner for the month`; `s 11(2): the requirement for an application is met` |
| Deeming an application made and approved when an allowance ceases at 65 | the Minister: power | the person: liability | s 11(3) | `s 11(3): the Minister may deem an application to have been made and approved`; `s 11(3): the day on which the application is deemed to have been made and approved` |
| Waiving the application at 65 | the Minister: power | the person: liability | s 11(3.1) | `s 11(3.1): the Minister may waive the requirement for an application` |
| Written notice before a waiver | the person: claim | the Minister: duty | s 11(3.2) | `s 11(3.2): the Minister must notify the person in writing and provide the information` |
| Correcting the information | the Minister: claim | the person: duty (by the day before the 65th birthday) | s 11(3.3) | `s 11(3.3): the person has complied with the duty to file a statement correcting inaccuracies`; `s 11(3.3): the last day on which the person may file the statement correcting inaccuracies` |
| Declining the waiver | the person: power | the Minister: liability | s 11(3.4) | `s 11(3.4): the person has declined the waiver in time` |
| Requiring an application after all, with notice | the Minister: power; the person: claim to the notice | the person: liability; the Minister: duty to notify | s 11(3.5) | `s 11(3.5): the Minister may still require the person to make an application`; `s 11(3.5): the Minister must notify the person in writing of the requirement` |
| Waiving the application for later months | the Minister: power | the pensioner: liability | s 11(4) | `s 11(4): the Minister may waive the requirement for an application` |
| Requiring an application for later months, with 15 days' notice | the Minister: power; the pensioner: claim to the notice | the pensioner: liability; the Minister: duty to notify | s 11(5), (6) | `s 11(5): the Minister must notify the pensioner in writing that an application is required`; `s 11(5): the last day on which the Minister may give the notice`; `s 11(6): the Minister must notify the pensioner in writing that an application is required`; `s 11(6): the last day on which the Minister may give the notice` |
| Limits on payment | the Minister: privilege to withhold | the pensioner: no-right | s 11(7) | `s 11(7): a limitation bars payment of a supplement for the month`, `s 11(7)(a): the month is more than eleven months before the month of the application`; `s 11(7)(b): no pension may be paid to the pensioner for the month`; `s 11(7)(c): the pensioner has been outside Canada for six consecutive months before the month`; `s 11(7)(d): the pensioner ceased to reside in Canada six months before the beginning of the month`; `s 11(7)(e): an undertaking by a sponsor is in effect in respect of the pensioner` |
| Lifting the sponsor's-undertaking limit | the pensioner: immunity | the Minister: disability | s 11(8) | `s 11(8): paragraph 11(7)(e) does not apply` |
| Statement of income in the application | the Minister: claim | the applicant: duty | s 14(1), (1.01) | `s 14(1): the person must make a statement of the person's income for the base calendar year in the application`; `s 14(1.01): the Minister may waive the requirement to make a statement of income`; `s 14(1.01): the statement of income is made or is deemed to have been made` |
| Estimating income, requiring a statement | the Minister: power | the applicant: liability | s 14(1.1), (1.2) | `s 14(1.1)(a): the Minister may estimate the applicant's income for the base calendar year`; `s 14(1.1)(b): the Minister may estimate the income of the applicant's spouse or common-law partner for the base calendar year`; `s 14(1.2): the Minister may require the person to make a statement of the person's income for any month in that year` |
| Filing a statement of estimated income | the person: power | the Minister: liability to use it | s 14(2) to (6) | `s 14(2): the person may file a statement of estimated income`; `s 14(3): the person may file a statement of estimated income`; `s 14(4): the person may file a statement of estimated income`; `s 14(5): the person may file a statement of estimated income`; `s 14(6): the person may file a statement of estimated income` |
| The first month a supplement on an estimate is paid | the Minister: privilege to withhold earlier months | the applicant: no-right | s 14(7) | `s 14(7): the first month for which a supplement calculated on the statement may be paid` |
| Stating and telling of a spouse or partner | the Minister: claim | the applicant: duty | s 15(1), (1.1), (4), (9) | `s 15(1): the person must state in the application whether the person has or had a spouse or common-law partner and, if so, who`; `s 15(1.1): the person must notify the Minister without delay of the change`; `s 15(4): the applicant must inform the Minister without delay of the release`; `s 15(9): the applicant must inform the Minister without delay` |
| The spouse's statement of income | the Minister: claim | the spouse or partner: duty | s 15(2), (2.2) | `s 15(2): the application may be considered and dealt with`; `s 15(2.2): the statement is filed or is deemed to have been filed` |
| Waiving the information or the statement | the Minister: power | the applicant, the spouse or partner: liability | s 15(2.1), (2.2) | `s 15(2.1): the Minister may waive the requirement to submit the information described in subsection 15(1)`; `s 15(2.2): the Minister may waive the requirement to file a statement under paragraph 15(2)(a)` |
| Notice to the spouse before a waiver, and the correcting statement | the spouse or partner: claim to the notice; the Minister: claim to the correction | the Minister: duty to notify; the spouse or partner: duty to correct | s 15(2.3), (2.4) | `s 15(2.3): the Minister must notify the spouse or common-law partner in writing and provide the information`; `s 15(2.4): the spouse or common-law partner has complied with the duty to file a statement correcting inaccuracies`; `s 15(2.4): the last day on which the spouse or common-law partner may file the statement correcting inaccuracies` |
| Directing that the application be dealt with as though there were no spouse | the Minister: power | the applicant: liability | s 15(3), (3.2) | `s 15(3)(a): the Minister may direct that the application be dealt with as though the person did not have a spouse or common-law partner`; `s 15(3)(b): the Minister may direct that the application be dealt with as though the person did not have a spouse or common-law partner`; `s 15(3.2): the Minister may direct that the application be dealt with, for the month, as though the applicant did not have a spouse or common-law partner` |
| Considering the application and giving reasons | the applicant: claim | the Minister: duty | s 16(1), (2) | `s 16(1): the Minister must consider without delay whether the applicant is entitled to be paid a supplement`; `s 16(2): the Minister must forthwith notify the applicant in writing of the basis on which the amount was fixed`; `s 16(2): the Minister must forthwith notify the applicant in writing of the decision that no supplement may be paid and the Minister's reasons` |
| Payment in arrears | the pensioner: claim to payment at the end of the month | the Minister: duty | s 17 | `s 17: the end-of-month days on which payment for the month may be made` |
| Deducting an overpayment | the Minister: power | the applicant: liability | s 18(a) | `s 18(a): the amount to be deducted and retained out of subsequent payments of supplement or pension` |
| Paying an underpayment | the applicant: claim | the Minister: duty | s 18(b) | `s 18(b): the amount to be paid to the applicant, read as it is written`; `s 18(b): the amount to be paid to the applicant, read as the mirror of paragraph (a)` |
| Asking that the supplement cease, and applying again | the pensioner: power | the Minister: liability | s 18.1 | `s 18.1: the last day of the month on which the supplement ceases to be payable`; `s 18.1: the first month in which the supplement may resume`; `s 18.1: the supplement is payable for the month in spite of the request` |
| Asking for cancellation of the supplement | the pensioner: power | the Minister: liability | s 18.2 | `s 18.2(1): the pensioner may request cancellation of the supplement`; `s 18.2(2)(a): the application for the supplement is deemed never to have been made`; `s 18.2(2)(b): the supplement is deemed not to have been payable during the period in question` |
| Enhancement for two pensioners who are each other's spouse or common-law partner | the Minister: power to pay the difference | the pensioners: no-right to it | s 12(5.1) | `s 12(5.1): the aggregate paid to the two is less than the aggregate that one would be paid if the other were not a pensioner`; `s 12(5.1): the amount the Minister may pay to the pensioner` |
| The allowance for a month (spouse, common-law partner, former common-law partner) | the person: claim | the Minister: duty to approve and pay | s 19(1), (1.2), (2), (4) (the condition of (1.2) sits inside the rule for 19(1)(a)) | `s 19: an allowance may be paid to the person for the month`; `s 19(1)(a): the spouse meets the separation condition`; `s 19(1)(a.1): the former common-law partner meets the separation condition`; `s 19(1)(b): the person is at least sixty and under sixty-five`; `s 19(1)(c): the person has the required residence in Canada`; `s 19(2): the person's residence in Canada is or was legal`; `s 19(4): the requirement for an application and approval is met for the payment period` |
| Applying individually when the pensioner is incarcerated | the spouse or partner: power | the Minister: liability | s 19(4.01) | `s 19(4.01): the spouse or common-law partner may apply for an allowance individually` |
| Waiving the application, notice, and requiring it after all | the Minister: power; the person: claim to the notice | the person: liability; the Minister: duty to notify | s 19(4.1) to (4.3) | `s 19(4.1): the Minister may waive the requirement for an application`; `s 19(4.2): the Minister must notify the spouse or common-law partner in writing that an application is required`; `s 19(4.3): the Minister must notify the spouse or common-law partner in writing that an application is required` |
| Ceasing, limits and their lifting | the Minister: privilege to withhold; the person: immunity where a limit does not apply | the person: no-right; the Minister: disability | s 19(5), (6), (6.1) to (6.3) | `s 19(5): the allowance is still payable for the month`; `s 19(6): a limitation bars payment of an allowance for the month`; `s 19(6.1): paragraph 19(6)(b) does not apply`; `s 19(6.2): paragraph 19(6)(d) does not apply`; `s 19(6.3): payment resumes in respect of the month of release` |
| Leaving out the pensioner's income | the Minister: power to direct | the spouse or partner: liability | s 19(8), (9) | `s 19(8): the Minister may direct that the monthly joint income be determined without the pensioner's income`; `s 19(9): the direction under subsection 19(8) is in effect for the payment period` |
| Suspension and resumption | the Minister: power to suspend; the beneficiary: claim to resumption | the beneficiary: liability; the Minister: duty to resume | s 20 | `s 20: payment of an allowance may be suspended`; `s 20: payment of the allowance may be resumed` |
| The allowance of a survivor | the survivor: claim | the Minister: duty to approve and pay | s 21(1) to (6) (the exception of (5) sits inside the rule for 21(4)) | `s 21: an allowance may be paid to the survivor for the month`; `s 21(1): the person is a survivor`; `s 21(1)(a): the survivor is at least sixty and under sixty-five`; `s 21(1)(b): the survivor has the required residence in Canada`; `s 21(2): the survivor's residence in Canada is or was legal`; `s 21(4): the requirement for an application and approval is met for the payment period`; `s 21(6): the first month for which an allowance may be paid` |
| Waiving the application, notice, and requiring it after all (survivor) | the Minister: power; the survivor: claim to the notice | the survivor: liability; the Minister: duty to notify | s 21(5.1) to (5.3) | `s 21(5.1): the Minister may waive the requirement for an application`; `s 21(5.2): the Minister must notify the survivor in writing that an application is required`; `s 21(5.3): the Minister must notify the survivor in writing that an application is required` |
| Ceasing and limits (survivor) | the Minister: privilege to withhold; the survivor: immunity where a limit does not apply | the survivor: no-right; the Minister: disability | s 21(7) to (9.2) | `s 21(7): the month is before September 1985`; `s 21(7.1): a limitation for a survivor who was not a widow bars payment for the month`; `s 21(8): the allowance is still payable for the month`; `s 21(9): a limitation bars payment of an allowance for the month`; `s 21(9.1): paragraph 21(9)(c) does not apply`; `s 21(9.2): payment resumes in respect of the month of release` |
| One survivor's eligibility does not depend on another's | the survivor: immunity | the Minister: disability | s 21(12) | `s 21(12): an allowance may be paid to the survivor for the month, whether or not another person is eligible` |
| A conviction for killing the spouse or partner | the Minister: power to treat the allowance as not payable; the Crown: claim to repay | the individual: liability; the person: duty to repay | s 21.1(1), (3), (4) | `s 21.1(1): an allowance under section 21 is not payable to the individual`; `s 21.1(3): the Minister may deem the conviction to be a conviction of first or second degree murder or manslaughter`; `s 21.1(4): the person is deemed not to have been entitled and the amounts are a debt that the Minister must recover` |
| Exemption from the conviction rule (manslaughter, released on probation-order conditions) | the individual: immunity | the Minister: disability | s 21.1(8) | `s 21.1(8): section 21.1 does not apply to the individual` |
| Repayment after the conviction is reversed | the person: claim | the Minister: duty | s 21.1(2) | `s 21.1(2): the individual's entitlement becomes payable as if subsection 21.1(1) had never applied`; `s 21.1(2): the Minister must repay any amount recovered from the person` |
| A pensioner whose spouse is paid an allowance | the pensioner: claim to the supplement of s 22(2), and to the Part II supplement in the cases of (5) and (6) | the Minister: duty | s 22(2), (2.1), (5), (6), (7) | `s 22(2): the amount of the supplement that may be paid, given the formula`; `s 22(2.1): a supplement under subsection 22(2) may not be paid`; `s 22(2): the supplement under this subsection is payable in lieu of the supplement under Part II`; `s 22(5): the pensioner may be paid the amount of supplement provided under Part II for the month`; `s 22(6): the amount of supplement the pensioner may be paid for the month`; `s 22(7): the application is deemed to have been made and approved under Part II` |
| Amounts of the allowances and the added amounts | the person: the content of the claim | the Minister: the content of the duty | s 22(3), (4), 22.1 | `s 22(3): the amount of the allowance that may be paid to the spouse or common-law partner of a pensioner`; `s 22(4): the amount of the allowance that may be paid to a survivor`; `s 22.1: the amount that may be added, given the amount determined by the formula` |
| When payment of the allowance starts | the person: claim | the Minister: duty | s 23(1) to (3) | `s 23(1): the first month for which payment of the allowance commences`; `s 23(1): the earlier date as of which the approval may be effective`; `s 23(1.1): the earliest month in which payment of the allowance may commence`; `s 23(2): the approval may be effective as of the day prescribed`; `s 23(2): the earliest day to which the approval may be made effective`; `s 23(3): payment of the allowance commences in respect of the month of release` |
| Considering the application for an allowance and giving reasons | the applicant: claim | the Minister: duty | s 24(1), (2) | `s 24(1): the Minister must consider without delay whether the applicant is entitled to be paid an allowance`; `s 24(2): the Minister must forthwith notify the applicant in writing of the basis on which the amount was fixed`; `s 24(2): the Minister must forthwith notify the applicant in writing of the decision that no allowance may be paid and the Minister's reasons` |
| Payment of the allowance in arrears | the person: claim to payment at the end of the month | the Minister: duty | s 25 | `s 25: the end-of-month days on which payment of the allowance for the month may be made` |
| Sections 14, 15 and 18 and the Minister's waiver, for an allowance | the Minister: power to waive; the applicant: the claim and duties of those sections | the applicant: liability; the Minister: the duties of those sections | s 26(1), (1.1) | `s 26(1): sections 14, 15 and 18 apply by virtue of section 26(1) in respect of the benefit`; `s 26(1.1): the Minister may waive the requirements of subsections 14(1) and 15(1) and (2) in respect of an application for an allowance` |
| none: definitions, amounts, indexation, counting rules and cross-references | none | none | ss 10, 12 (except 12(5.1)), 12.1, 13 (definitions, amounts, indexation, the income counted before July 1, 1999); s 15(3.1), (3.3), (4.1), (4.2), (5), (5.1), (6.1), (7.1), (7.2), (8) (how a month is treated); s 19(1.1), (1.2) (when partners count as separated), 19(7) (the amount is that of s 22(3)); s 21(10), (11) (the amount is that of s 22(4)); s 22(1), (4.1) to (4.4); s 22.1; s 26(2) | the rules of `oa2-indexation`, `oa2-part2-amount`, `oa2-part2-income` and `oa2-part3-amount`; `s 15: the treatment that the directions and deemings give for the month`; `s 15(3.1): the treatment under a continuing direction`; `s 15(3.3): the treatment under a continuing direction for an incarcerated person's spouse or common-law partner`; `s 15(4.1): the treatment for a separated person`; `s 15(4.2): the treatment after a common-law partner is lost otherwise than by death`; `s 15(5): the treatment under a reviewed direction for a payment period ending before July 1, 1999`; `s 15(5.1): the treatment after the review of a direction`; `s 15(6.1): the treatment after a person begins to have a spouse or common-law partner`; `s 15(7.1): the treatment after a person ceases to have a spouse`; `s 15(7.2): the treatment after a common-law partner dies`; `s 19(1.1): the common-law partners have not become former common-law partners`; `s 19(7): the amount of the allowance`; `s 21(10): the amount of the allowance`; `s 21(11): subsection 21(10) also applies in respect of the month` |

## Coverage table

<!-- COVERAGE BEGIN -->
| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| PART II Monthly Guaranteed Income Supplement | src:227 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| Interpretation (group heading) | src:229 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 10 | src:231-233 | encoded | oa2-part2-eligibility.l4: s 10: the base calendar year; s 10: the current payment period | Payment periods run July 1 to June 30; the base calendar year is the last calendar year ending before the current payment period (the period beginning July 1, 2021 has base year 2020; tested). |
| Supplement Payable (group heading) | src:236 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 11(1) | src:238 | encoded | oa2-part2-eligibility.l4: s 11(1): a supplement may be paid to the person; s 11: a supplement may be paid to the pensioner for the month | A pensioner is a person whose application for the pension has been approved (keel s 2); the pension application itself is Part I, out of range. |
| s 11(2) | src:240 | encoded | oa2-part2-eligibility.l4: s 11(2): the requirement for an application is met; s 11: a supplement may be paid to the pensioner for the month | Needs an application and its approval unless (3) deemed it or (3.1) or (4) waived it. Whether the Minister has approved, waived or deemed is a fact the caller states. |
| s 11(3) | src:242 | encoded | oa2-part2-eligibility.l4: s 11(3): the Minister may deem an application to have been made and approved; s 11(3): the day on which the application is deemed to have been made and app...; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(3.1) | src:244 | encoded | oa2-part2-eligibility.l4: s 11(3.1): the Minister may waive the requirement for an application; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(3.2) | src:246 | encoded | oa2-part2-eligibility.l4: s 11(3.2): the Minister must notify the person in writing and provide the inf...; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(3.3) | src:248 | encoded | oa2-part2-eligibility.l4: s 11(3.3): the last day on which the person may file the statement correcting...; s 11(3.3): the person has complied with the duty to file a statement correcti...; s 11: a supplement may be paid to the pensioner for the month | The last day to file is the day before the 65th birthday. |
| s 11(3.4) | src:250 | encoded | oa2-part2-eligibility.l4: s 11(3.4): the person has declined the waiver in time; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(3.5) | src:252 | encoded | oa2-part2-eligibility.l4: s 11(3.5): the Minister may still require the person to make an application; s 11(3.5): the Minister must notify the person in writing of the requirement; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(4) | src:254 | encoded | oa2-part2-eligibility.l4: s 11(4): the Minister may waive the requirement for an application; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(5) | src:256 | encoded | oa2-part2-eligibility.l4: s 11(5): the Minister must notify the pensioner in writing that an applicatio...; s 11(5): the last day on which the Minister may give the notice; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(6) | src:258 | encoded | oa2-part2-eligibility.l4: s 11(6): the Minister must notify the pensioner in writing that an applicatio...; s 11(6): the last day on which the Minister may give the notice; s 11: a supplement may be paid to the pensioner for the month |  |
| s 11(7) | src:260-265 | fork | oa2-part2-eligibility.l4: s 11(7)(a): the month is more than eleven months before the month of the appl...; s 11(7)(a): the earliest month for which a supplement may be paid; s 11(7)(b): no pension may be paid to the pensioner for the month and 5 more | Five limits. For (7)(c), counting from the month of leaving, the seventh month is the first barred (left January: July is paid, August is not; tested). Fork F-11c: 'Six consecutive months, exclusive of the month in which the pensioner left Canada' is read as: the month of leaving is not counted, so the first barred month is the seventh month after the month of leaving. |
| s 11(8) | src:267-269 | encoded | oa2-part2-eligibility.l4: s 11(8): paragraph 11(7)(e) does not apply; s 11(7): a limitation bars payment of a supplement for the month | The event 'as provided by the regulations' is an input (Regulations s 22.1, piece oa3). |
| Amount of Supplement (group heading) | src:271 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 12(1) | src:273-278 | fork | oa2-part2-amount.l4: s 12(1): the situation of the pensioner for the month; s 12(1): the maximum supplement for the payment quarter commencing on April 1...; s 12(1): the amount of the supplement for a month in the payment quarter comm... | Fork F-12-1: The quarter beginning April 1, 2005 is named by (1); (5) replaces the reduction by its formula for every month after December 1997, so both are encoded and the seat uses the formula of (5). |
| s 12(1.1) | src:280-282 | encoded | oa2-part2-amount.l4: s 12(1.1): the increase for the payment quarter commencing on January 1, 2006; s 12(2): the maximum supplement for a payment quarter commencing after June 3... | A fixed increase for the quarter beginning January 1, 2006. |
| s 12(1.2) | src:284-286 | encoded | oa2-part2-amount.l4: s 12(1.2): the increase for the payment quarter commencing on January 1, 2007; s 12(2): the maximum supplement for a payment quarter commencing after June 3... | A fixed increase for the quarter beginning January 1, 2007. |
| s 12(2) | src:288-292 | fork | oa2-part2-amount.l4: s 12(2): the maximum supplement for a payment quarter commencing after June 3... | Fork F-INDEX-1: The price index series is not in the Act: the indexing is one quarter at a time, with the previous maximum and the two index figures as inputs. |
| s 12(3) | src:294 | fork | oa2-part2-amount.l4: s 12(2): the maximum supplement for a payment quarter commencing after June 3... | Fork F-INDEX-1: The never-less-than floor is part of the quarterly step; see s 12(2). |
| s 12(4) | src:296-298 | fork | oa2-part2-amount.l4: s 12(2): the maximum supplement for a payment quarter commencing after June 3... | Fork F-INDEX-2: A fall in the index suspends adjustment and carries the earlier second index; a later fall while an earlier one is unmatched leaves the earlier in force. |
| s 12(5) | src:300-308 | fork | oa2-part2-amount.l4: s 12(5): the amount determined by the formula; s 12(5): the amount of the supplement that may be paid for the month | Fork F-12-1, F-12-2: Both the April 2005 overlap with (1) and the treatment of a negative result (floored in a wrapper; the raw formula is its own rule). |
| s 12(5.1) | src:310-313 | encoded | oa2-part2-amount.l4: s 12(5.1): the aggregate paid to the two is less than the aggregate that one ...; s 12(5.1): the amount the Minister may pay to the pensioner | Two pensioners who are each other's spouse or common-law partner: when their combined pensions and supplements are less than one of them would be paid alone, the Minister may pay that one the difference; the condition and the amount are two rules. |
| s 12(6) | src:315-326 | encoded | oa2-part2-amount.l4: s 12(6): the situation of the applicant; s 12(6)(a): the monthly base income; s 12(6)(b): the monthly base income and 3 more | Monthly base income by the three situations (a), (b), (c). |
| s 12.1(1) | src:328-335 | fork | oa2-part2-amount.l4: s 12.1: the amount determined for A for the payment quarter beginning on July...; s 12.1(1): the amount determined by the formula for a pensioner referred to i...; s 12.1: the amount that may be added, given the amount determined by the formula | Fork F-12.1-1, F-12.1-2: The rounding is read as applying to the monthly figure; a pensioner whose spouse is paid a benefit is in neither (1) nor (2), and the answer is NOTHING. |
| s 12.1(2) | src:337-344 | fork | oa2-part2-amount.l4: s 12.1: the amount determined for A for the payment quarter beginning on July...; s 12.1(2): the amount determined by the formula for a pensioner referred to i...; s 12.1: the amount that may be added, given the amount determined by the formula | Fork F-12.1-1: The rounding is read as applying to the monthly figure. |
| s 12.1(2.1) | src:346-348 | encoded | oa2-part2-amount.l4: s 12.1(2.1): the increase for the payment quarter beginning on July 1, 2016; s 12.1(3): the amount determined for A for a payment quarter beginning after ... | The $78.92 increase for the quarter beginning July 1, 2016 applies to A in 12.1(1) and in the case set out in paragraph (a) of A in 12.1(2). |
| s 12.1(3) | src:350-353 | fork | oa2-part2-amount.l4: s 12.1(3): the amount determined for A for a payment quarter beginning after ... | Fork F-INDEX-1: One quarter at a time, as for s 12(2). |
| s 12.1(4) | src:355 | encoded | oa2-part2-amount.l4: s 12.1(3): the amount determined for A for a payment quarter beginning after ... | The floor on A, as for s 12(3). |
| s 12.1(5) | src:357-359 | fork | oa2-part2-amount.l4: s 12.1(3): the amount determined for A for a payment quarter beginning after ... | Fork F-INDEX-2: As for s 12(4). |
| Calculation of Income (group heading) | src:361 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 13 | src:363-376 | encoded | oa2-part2-income.l4: s 13(a)(i): the single amount deducted; s 13(a): the deduction from income from office or employment; s 13(b): the deduction from self-employed earnings and 2 more | Applies only to months before July 1, 1999; later months use the keel's definition of income. |
| Statement or Estimate of Income (group heading) | src:378 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 14(1) | src:380 | encoded | oa2-part2-income.l4: s 14(1): the person must make a statement of the person's income for the base...; s 14(1.01): the statement of income is made or is deemed to have been made | The duty is on the person who applies; the Minister's waiver is s 14(1.01). |
| s 14(1.01) | src:382 | encoded | oa2-part2-income.l4: s 14(1.01): the Minister may waive the requirement to make a statement of income; s 14(1.01): the statement of income is made or is deemed to have been made |  |
| s 14(1.1) | src:384-386 | encoded | oa2-part2-income.l4: s 14(1.1)(a): the Minister may estimate the applicant's income for the base c...; s 14(1.1)(b): the Minister may estimate the income of the applicant's spouse ... |  |
| s 14(1.2) | src:388 | encoded | oa2-part2-income.l4: s 14(1.2): the Minister may require the person to make a statement of the per... |  |
| s 14(2) | src:390-393 | encoded | oa2-part2-income.l4: s 14(2)(a): the number of months in the part of the calendar year that is aft...; s 14(2)(a): the pension income divided by the number of months and multiplied...; s 14(2): the payment period immediately after the payment period and 3 more | Estimate of income after ceasing work; the last day to file is the end of the second payment period after the current payment period (tested). |
| s 14(3) | src:395-398 | encoded | oa2-part2-income.l4: s 14(3): the month is the last month of a calendar year that ends in the curr...; s 14(3): the person may file a statement of estimated income; s 14(3): the estimated income |  |
| s 14(4) | src:400-403 | encoded | oa2-part2-income.l4: s 14(4)(a): the number of months in the part of the calendar year that is aft...; s 14(4): the person may file a statement of estimated income; s 14(4): the estimated income |  |
| s 14(5) | src:405-413 | encoded | oa2-part2-income.l4: s 14(5): the last day on which the statement of estimated income may be filed; s 14(5): the circumstance of the person who ceased; s 14(5): the person may file a statement of estimated income and 1 more |  |
| s 14(6) | src:415-423 | encoded | oa2-part2-income.l4: s 14(6): the person may file a statement of estimated income; s 14(6): the estimated income |  |
| s 14(7) | src:425-428 | encoded | oa2-part2-income.l4: s 14(7): the first month for which a supplement calculated on the statement m... | The first month for payment on a statement depends on whether it shows the month of ceasing or the month of the loss. |
| Spouses and Common-law Partners (group heading) | src:430 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 15(1) | src:432 | encoded | oa2-part2-spouse.l4: s 15(1): the person must state in the application whether the person has or h...; s 15(1): the person has or had a spouse or common-law partner at a time in th... | The duty is on the applicant. Section 15 is the one that moves money: each 'as though' circumstance is a rule that answers With, Without or NOTHING. |
| s 15(1.1) | src:434 | encoded | oa2-part2-spouse.l4: s 15(1.1): the person must notify the Minister without delay of the change |  |
| s 15(2) | src:436-439 | fork | oa2-part2-spouse.l4: s 15(2): the application may be considered and dealt with | Fork F-15-2: 'Subject to (3), (4.1) and (4.2)' is read as: where a direction under (3) or (4.1) has been made, or (4.2) applies, the application may be considered without waiting. |
| s 15(2.1) | src:441 | encoded | oa2-part2-spouse.l4: s 15(2.1): the Minister may waive the requirement to submit the information d... |  |
| s 15(2.2) | src:443 | encoded | oa2-part2-spouse.l4: s 15(2.2): the Minister may waive the requirement to file a statement under p...; s 15(2.2): the statement is filed or is deemed to have been filed |  |
| s 15(2.3) | src:445 | encoded | oa2-part2-spouse.l4: s 15(2.3): the Minister must notify the spouse or common-law partner in writi... |  |
| s 15(2.4) | src:447-448 | encoded | oa2-part2-spouse.l4: s 15(2.4): the last day on which the spouse or common-law partner may file th...; s 15(2.4): the spouse or common-law partner has complied with the duty to fil... |  |
| s 15(3) | src:449-451 | encoded | oa2-part2-spouse.l4: s 15(3)(a): the Minister may direct that the application be dealt with as tho...; s 15(3)(b): the Minister may direct that the application be dealt with as tho...; s 15(3.1): the treatment under a continuing direction |  |
| s 15(3.1) | src:453 | encoded | oa2-part2-spouse.l4: s 15(3.1): the treatment under a continuing direction |  |
| s 15(3.2) | src:455 | encoded | oa2-part2-spouse.l4: s 15(3.2): the Minister may direct that the application be dealt with, for th... |  |
| s 15(3.3) | src:457 | encoded | oa2-part2-spouse.l4: s 15(3.3): the treatment under a continuing direction for an incarcerated per... |  |
| s 15(4) | src:459 | encoded | oa2-part2-spouse.l4: s 15(4): the applicant must inform the Minister without delay of the release |  |
| s 15(4.1) | src:461 | encoded | oa2-part2-spouse.l4: s 15(4.1): the treatment for a separated person |  |
| s 15(4.2) | src:463 | encoded | oa2-part2-spouse.l4: s 15(4.2): the treatment after a common-law partner is lost otherwise than by... |  |
| s 15(5) | src:465 | encoded | oa2-part2-spouse.l4: s 15(5): the treatment under a reviewed direction for a payment period ending... |  |
| s 15(5.1) | src:467 | encoded | oa2-part2-spouse.l4: s 15(5.1): the treatment after the review of a direction |  |
| s 15(6) | src:468 | repealed or blank in this text |  | The text shows '[Repealed, 2000, c. 12, s. 194]'. |
| s 15(6.1) | src:470-474 | encoded | oa2-part2-spouse.l4: s 15(6.1): the treatment after a person begins to have a spouse or common-law... |  |
| s 15(7) | src:475 | repealed or blank in this text |  | The text shows '[Repealed, 2000, c. 12, s. 194]'. |
| s 15(7.1) | src:477 | encoded | oa2-part2-spouse.l4: s 15(7.1): the treatment after a person ceases to have a spouse |  |
| s 15(7.2) | src:479 | encoded | oa2-part2-spouse.l4: s 15(7.2): the treatment after a common-law partner dies |  |
| s 15(8) | src:481 | fork | oa2-part2-spouse.l4: s 15: the treatment that the directions and deemings give for the month | Fork F-15-1: The text does not say which prevails when a direction and a deeming give different answers for a month; the combining rule answers NOTHING when none operates or two disagree. |
| s 15(9) | src:483 | encoded | oa2-part2-spouse.l4: s 15(9): the applicant must inform the Minister without delay | The applicant's duty to inform the Minister without delay. |
| Payment of Supplement (group heading) | src:485 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 16(1) | src:487 | encoded | oa2-part2-payment.l4: s 16(1): the Minister must consider without delay whether the applicant is en... | The Minister's duty to consider an application without delay, encoded for what it gives the applicant: a decision. |
| s 16(2) | src:489 | encoded | oa2-part2-payment.l4: s 16(2): the Minister must forthwith notify the applicant in writing of the b...; s 16(2): the Minister must forthwith notify the applicant in writing of the d... | What the applicant is owed: the basis of the amount on request, and the reasons for a refusal. |
| s 17 | src:491 | encoded | oa2-part2-payment.l4: s 17: the end-of-month days on which payment for the month may be made | Payment in arrears at the end of the month; late approval allows the end of the month of approval or the next. |
| Adjustment of Payments (group heading) | src:493 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 18 | src:495-497 | fork | oa2-part2-payment.l4: s 18(a): the amount to be deducted and retained out of subsequent payments of...; s 18(b): the amount to be paid to the applicant, read as it is written; s 18(b): the amount to be paid to the applicant, read as the mirror of paragr... | Fork F-18-1: Paragraph (b) read as written pays nothing; the mirror of (a) is also encoded and the seat uses it. |
| Cessation of Payment (group heading) | src:499 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 18.1 | src:501 | encoded | oa2-part2-payment.l4: s 18.1: the last day of the month on which the supplement ceases to be payable; s 18.1: the first month in which the supplement may resume; s 18.1: the supplement is payable for the month in spite of the request | The date the supplement ceases and the month it may resume are rules; the third rule says whether the month is still payable. |
| Cancellation of Payment (group heading) | src:503 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 18.2(1) | src:505 | encoded | oa2-part2-payment.l4: s 18.2(1): the pensioner may request cancellation of the supplement | The prescribed time (Regulations s 26.1, piece oa3) is an input. |
| s 18.2(2) | src:507-509 | encoded | oa2-part2-payment.l4: s 18.2(2)(a): the application for the supplement is deemed never to have been...; s 18.2(2)(b): the supplement is deemed not to have been payable during the pe... | The effect of a granted cancellation: the application deemed never made; the supplement deemed not payable. |
| PART III Monthly Allowances | src:511 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| Allowance Payable (group heading) | src:513 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 19(1) | src:515-519 | fork | oa2-part3-spouse-allowance.l4: s 19(1)(a): the spouse meets the separation condition; s 19(1)(a.1): the former common-law partner meets the separation condition; s 19(1)(b): the person is at least sixty and under sixty-five and 3 more | Fork F-19-1, F-AGE-1: 'Not more than three months before the month' is read as: the separation commenced on or after the first day of the month three months before; the age 60 to 64 is tested on the last day of the month before the month. |
| s 19(1.1) | src:521 | encoded | oa2-part3-spouse-allowance.l4: s 19(1.1): the common-law partners have become former common-law partners; s 19(1.1): the common-law partners have not become former common-law partners | Common-law partners who separate only because one is incarcerated do not become former common-law partners. |
| s 19(1.2) | src:523 | encoded | oa2-part3-spouse-allowance.l4: s 19(1)(a): the spouse meets the separation condition | A spouse is not considered separated if the sole reason is that the pensioner is incarcerated; the condition is inside the rule for s 19(1)(a). |
| s 19(2) | src:525-527 | encoded | oa2-part3-spouse-allowance.l4: s 19(2): the person's residence in Canada is or was legal |  |
| s 19(3) | src:529 | inert |  | A regulation-making power: the Governor in Council may make regulations on the meaning of legal residence for subsection 19(2). It is machinery, and the Regulations are piece oa3's. Here legal residence enters as the plain facts 'legally resident in Canada' in the s 19 fact record, so nothing is encoded for the power itself. |
| s 19(4) | src:531 | encoded | oa2-part3-spouse-allowance.l4: s 19(4): the requirement for an application and approval is met for the payme... | The in-force text is encoded. The text's AMENDMENTS NOT IN FORCE section (2012, c. 19, s. 459) would replace it; that section is outside lines 227-822 and is not encoded. |
| s 19(4.01) | src:533 | encoded | oa2-part3-spouse-allowance.l4: s 19(4.01): the spouse or common-law partner may apply for an allowance indiv... |  |
| s 19(4.1) | src:535 | encoded | oa2-part3-spouse-allowance.l4: s 19(4.1): the Minister may waive the requirement for an application |  |
| s 19(4.2) | src:537 | encoded | oa2-part3-spouse-allowance.l4: s 19(4.2): the Minister must notify the spouse or common-law partner in writi...; s 19(4.2): the last day on which the Minister may give the notice |  |
| s 19(4.3) | src:539 | encoded | oa2-part3-spouse-allowance.l4: s 19(4.3): the Minister must notify the spouse or common-law partner in writi...; s 19(4.3): the last day on which the Minister may give the notice |  |
| s 19(5) | src:541 | fork | oa2-part3-spouse-allowance.l4: s 19(5): the allowance is still payable for the month | Fork F-19-2: 'No longer meets the conditions' is not a separate month: the per-month evaluation of (1) already gives it. |
| s 19(6) | src:543-551 | fork | oa2-part3-spouse-allowance.l4: s 19(6)(a): the month is more than eleven months before the month of the appl...; s 19(6)(b): no supplement may be paid to the pensioner for the month; s 19(6)(c): the person has been outside Canada for six consecutive months bef... and 5 more | Six limitations; (6)(e) depends on the month it came into force, which the text does not give and which is an input. Fork F-11c: Paragraph (c) is read as s 11(7)(c) is. |
| s 19(6.1) | src:553-555 | encoded | oa2-part3-spouse-allowance.l4: s 19(6.1): paragraph 19(6)(b) does not apply |  |
| s 19(6.2) | src:557-559 | encoded | oa2-part3-spouse-allowance.l4: s 19(6.2): paragraph 19(6)(d) does not apply |  |
| s 19(6.3) | src:561-563 | encoded | oa2-part3-spouse-allowance.l4: s 19(6.3): the month is the month of release; s 19(6.3): payment resumes in respect of the month of release; s 19(6.3): the month of release does not hold back payment |  |
| s 19(7) | src:565 | encoded | oa2-part3-spouse-allowance.l4: s 19(7): the amount of the allowance | The amount is determined by s 22(3). |
| s 19(8) | src:567 | encoded | oa2-part3-spouse-allowance.l4: s 19(8): the Minister may direct that the monthly joint income be determined ... |  |
| s 19(9) | src:569 | encoded | oa2-part3-spouse-allowance.l4: s 19(9): the direction under subsection 19(8) is in effect for the payment pe... |  |
| s 20 | src:571 | encoded | oa2-part3-spouse-allowance.l4: s 20: payment of an allowance may be suspended; s 20: payment of the allowance may be resumed |  |
| s 21(1) | src:573-575 | fork | oa2-part3-survivor-allowance.l4: s 21(1): the person is a survivor; s 21(1)(a): the survivor is at least sixty and under sixty-five; s 21(1)(b): the survivor has the required residence in Canada and 1 more | Fork F-AGE-1: The age 60 to 64 is tested on the last day of the month before the month, from subsections 21(6) and 21(8). |
| s 21(2) | src:577-579 | encoded | oa2-part3-survivor-allowance.l4: s 21(2): the survivor's residence in Canada is or was legal |  |
| s 21(3) | src:581 | inert |  | A regulation-making power: the Governor in Council may make regulations on the meaning of legal residence for subsection 21(2). It is machinery, and the Regulations are piece oa3's. Here legal residence enters as the plain facts 'legally resident in Canada' in the s 21 fact record, so nothing is encoded for the power itself. |
| s 21(4) | src:583 | encoded | oa2-part3-survivor-allowance.l4: s 21(4): the requirement for an application and approval is met for the payme... | The in-force text is encoded. The text's AMENDMENTS NOT IN FORCE section (2012, c. 19, s. 460) would replace it; that section is outside lines 227-822 and is not encoded. |
| s 21(5) | src:585 | encoded | oa2-part3-survivor-allowance.l4: s 21(4): the requirement for an application and approval is met for the payme... |  |
| s 21(5.1) | src:587 | encoded | oa2-part3-survivor-allowance.l4: s 21(5.1): the Minister may waive the requirement for an application |  |
| s 21(5.2) | src:589 | encoded | oa2-part3-survivor-allowance.l4: s 21(5.2): the Minister must notify the survivor in writing that an applicati...; s 21(5.2): the last day on which the Minister may give the notice |  |
| s 21(5.3) | src:591 | encoded | oa2-part3-survivor-allowance.l4: s 21(5.3): the Minister must notify the survivor in writing that an applicati...; s 21(5.3): the last day on which the Minister may give the notice |  |
| s 21(6) | src:593 | encoded | oa2-part3-survivor-allowance.l4: s 21(6): the first month for which an allowance may be paid |  |
| s 21(7) | src:595 | encoded | oa2-part3-survivor-allowance.l4: s 21(7): the month is before September 1985 |  |
| s 21(7.1) | src:597-599 | encoded | oa2-part3-survivor-allowance.l4: s 21(7.1): a limitation for a survivor who was not a widow bars payment for t... | The month in which the subsection came into force is not in the text and is an input. |
| s 21(8) | src:601 | encoded | oa2-part3-survivor-allowance.l4: s 21(8): the allowance is still payable for the month |  |
| s 21(9) | src:603-609 | fork | oa2-part3-survivor-allowance.l4: s 21(9)(a): the month is more than eleven months before the month of the appl...; s 21(9)(b): the survivor has been outside Canada for six consecutive months b...; s 21(9)(c): an undertaking by a sponsor is in effect in respect of the survivor and 3 more | Four limitations; the incarceration limit (d) uses the keel's Sentence of imprisonment. Fork F-11c: Paragraph (b) is read as s 11(7)(c) is. |
| s 21(9.1) | src:611-613 | encoded | oa2-part3-survivor-allowance.l4: s 21(9.1): paragraph 21(9)(c) does not apply |  |
| s 21(9.2) | src:615-617 | encoded | oa2-part3-survivor-allowance.l4: s 21(9.2): the month is the month of release; s 21(9.2): payment resumes in respect of the month of release; s 21(9.2): the month of release does not hold back payment |  |
| s 21(10) | src:619 | encoded | oa2-part3-survivor-allowance.l4: s 21(10): the amount of the allowance | The amount is determined by s 22(4). |
| s 21(11) | src:621 | encoded | oa2-part3-survivor-allowance.l4: s 21(11): subsection 21(10) also applies in respect of the month |  |
| s 21(12) | src:623 | encoded | oa2-part3-survivor-allowance.l4: s 21(12): an allowance may be paid to the survivor for the month, whether or ... | Encoded as a rule that takes the other person's eligibility as an input and gives the same answer as the rule for the survivor alone. |
| s 21.1(1) | src:625 | encoded | oa2-part3-survivor-allowance.l4: s 21.1(1): an allowance under section 21 is not payable to the individual | A conviction of which the Minister is informed and satisfied; a foreign conviction counts only if deemed (3); the exceptions are (2) and (8). |
| s 21.1(2) | src:627 | encoded | oa2-part3-survivor-allowance.l4: s 21.1(2): the individual's entitlement becomes payable as if subsection 21.1...; s 21.1(2): the Minister must repay any amount recovered from the person |  |
| s 21.1(3) | src:629 | encoded | oa2-part3-survivor-allowance.l4: s 21.1(3): the Minister may deem the conviction to be a conviction of first o... |  |
| s 21.1(4) | src:631 | encoded | oa2-part3-survivor-allowance.l4: s 21.1(4): the person is deemed not to have been entitled and the amounts are... |  |
| s 21.1(5) | src:633 | inert |  | A 'for greater certainty' clause that fixes the time of application of section 21.1: it applies to a conviction of which the Minister is informed before, on or after the coming into force. It is commencement machinery. The rule for s 21.1(1) has no date condition on when the Minister was informed, so it already behaves as the clause says. |
| s 21.1(6) | src:635 | inert |  | A definition that sends 'first or second degree murder' to murder within the meaning of section 231 of the Criminal Code. It is a pure citation of another statute's definition: the conviction facts are stated as 'convicted of first or second degree murder or manslaughter', and a court applying the Code decides which offences those are, outside this Act. |
| s 21.1(7) | src:637 | inert |  | A definition that sends 'manslaughter' to manslaughter within the meaning of the Criminal Code. It is a pure citation of another statute's definition, treated as s 21.1(6) is: the conviction facts are stated by the caller and the Code decides what manslaughter is. |
| s 21.1(8) | src:639 | encoded | oa2-part3-survivor-allowance.l4: s 21.1(8): section 21.1 does not apply to the individual |  |
| Amount of Allowance (group heading) | src:641 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 22(1) | src:643-670 | encoded | oa2-part3-amount.l4: s 22(1): the base calendar year; s 22(1): the current payment period; s 22(1): the income for a month before July 1, 1999 and 11 more | Definitions of base calendar year, income, joint income, equivalents and residual incomes; the pension equivalent takes the section 7 amount as an input (piece oa1). |
| s 22(2) | src:672-678 | encoded | oa2-part3-amount.l4: s 22(2): the supplement under this subsection is payable in lieu of the suppl...; s 22(2): the amount determined by the formula; s 22(2): the amount of the supplement that may be paid, given the formula | The supplement payable to a pensioner whose spouse is paid an allowance, in lieu of the Part II supplement. |
| s 22(2.1) | src:680 | encoded | oa2-part3-amount.l4: s 22(2.1): a supplement under subsection 22(2) may not be paid |  |
| s 22(3) | src:682-708 | encoded | oa2-part3-amount.l4: s 22(3)(b): the product against which the monthly joint income is measured; s 22(3)(a): the amount of the allowance; s 22(3)(b): the amount of the allowance and 2 more | (a) and (b) agree at zero income, and (b) and (c) are complementary (tested). |
| s 22(4) | src:710-736 | encoded | oa2-part3-amount.l4: s 22(4)(b): the product against which the monthly income of the survivor is m...; s 22(4)(a): the amount of the allowance; s 22(4)(b): the amount of the allowance and 2 more |  |
| s 22(4.1) | src:738-741 | encoded | oa2-part3-amount.l4: s 22(4.1)(a): the supplement equivalent for the survivor for the payment quar...; s 22(4.1): the increase for the payment quarters commencing on January 1, 200...; s 22(4.2): the supplement equivalent for the survivor for a payment quarter c... |  |
| s 22(4.2) | src:743-746 | encoded | oa2-part3-amount.l4: s 22(4.2): the supplement equivalent for the survivor for a payment quarter c... |  |
| s 22(4.3) | src:748 | encoded | oa2-part3-amount.l4: s 22(4.2): the supplement equivalent for the survivor for a payment quarter c... |  |
| s 22(4.4) | src:750-752 | encoded | oa2-part3-amount.l4: s 22(4.2): the supplement equivalent for the survivor for a payment quarter c... |  |
| s 22(5) | src:754 | encoded | oa2-part3-amount.l4: s 22(5): the pensioner may be paid the amount of supplement provided under Pa... |  |
| s 22(6) | src:756 | encoded | oa2-part3-amount.l4: s 22(6): the amount of supplement the pensioner may be paid for the month |  |
| s 22(7) | src:758 | encoded | oa2-part3-amount.l4: s 22(7): the application is deemed to have been made and approved under Part II |  |
| s 22.1(1) | src:760-765 | encoded | oa2-part3-amount.l4: s 22.1(1): the amount determined for A for the payment quarter; s 22.1(1): the amount determined by the formula for a pensioner referred to i...; s 22.1: the amount that may be added, given the amount determined by the formula |  |
| s 22.1(2) | src:767-772 | encoded | oa2-part3-amount.l4: s 22.1(2): the amount determined for A for the payment quarter; s 22.1(2): the amount determined by the formula for a spouse or common-law pa...; s 22.1: the amount that may be added, given the amount determined by the formula |  |
| s 22.1(3) | src:774-779 | encoded | oa2-part3-amount.l4: s 22.1(3): the amount determined for A for the payment quarter; s 22.1(3): the amount determined by the formula for a survivor referred to in...; s 22.1: the amount that may be added, given the amount determined by the formula |  |
| s 22.1(3.1) | src:781 | encoded | oa2-part3-amount.l4: s 22.1(3.1): the increase on July 1, 2016 for A in subsection 22.1(3) | The $78.92 increase applies to A in 22.1(3) only (the survivor's A). |
| s 22.1(4) | src:783-786 | encoded | oa2-part3-amount.l4: s 22.1(4): the amount determined for A for a payment quarter beginning after ... |  |
| s 22.1(5) | src:788 | encoded | oa2-part3-amount.l4: s 22.1(4): the amount determined for A for a payment quarter beginning after ... |  |
| s 22.1(6) | src:790-792 | encoded | oa2-part3-amount.l4: s 22.1(4): the amount determined for A for a payment quarter beginning after ... |  |
| Commencement of Allowance (group heading) | src:794 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 23(1) | src:796 | encoded | oa2-part3-payment.l4: s 23(1): the first month for which payment of the allowance commences; s 23(1): the earlier date as of which the approval may be effective | The earlier date that may be prescribed by regulation is an input (piece oa3). |
| s 23(1.1) | src:798 | encoded | oa2-part3-payment.l4: s 23(1.1): the earliest month in which payment of the allowance may commence |  |
| s 23(2) | src:800-803 | encoded | oa2-part3-payment.l4: s 23(2): the earliest day to which the approval may be made effective; s 23(2): the approval may be effective as of the day prescribed | The earlier day that may be prescribed is an input (piece oa3). |
| s 23(3) | src:805-807 | encoded | oa2-part3-payment.l4: s 23(3): payment of the allowance commences in respect of the month of release |  |
| Payment of Allowance (group heading) | src:809 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 24(1) | src:811 | encoded | oa2-part3-payment.l4: s 24(1): the Minister must consider without delay whether the applicant is en... |  |
| s 24(2) | src:813 | encoded | oa2-part3-payment.l4: s 24(2): the Minister must forthwith notify the applicant in writing of the b...; s 24(2): the Minister must forthwith notify the applicant in writing of the d... |  |
| s 25 | src:815 | encoded | oa2-part3-payment.l4: s 25: the end-of-month days on which payment of the allowance for the month m... |  |
| Application of Part II (group heading) | src:816 | inert |  | A heading: a title that groups the provisions beneath it and states no rule, so nothing is encoded for it. The provisions under it have their own rows. |
| s 26(1) | src:817 | fork | oa2-part3-payment.l4: s 26(1): sections 14, 15 and 18 apply by virtue of section 26(1) in respect o... | Section 6 is piece oa1's; the rule says that sections 14, 15 and 18 apply to the allowance. Fork F-26-1: 'With such modifications as the circumstances require' states no modifications: the rules of sections 14, 15 and 18 are applied to the allowance by giving them the allowance's facts, and a rule says that they apply. |
| s 26(1.1) | src:819 | encoded | oa2-part3-payment.l4: s 26(1.1): the Minister may waive the requirements of subsections 14(1) and 1... |  |
| s 26(2) | src:821 | encoded | oa2-part3-payment.l4: s 26(2): subsection 11(2) and sections 16 to 18 apply in respect of the suppl... |  |

Counts: 161 rows; 118 encoded, 19 fork, 22 inert, 2 repealed or blank in this text.
<!-- COVERAGE END -->

## Fork register

| id | provision | readings seen | reading taken | the text that licenses it |
| --- | --- | --- | --- | --- |
| F-INDEX-1 | s 12(2), 12.1(3), 22(1) "supplement equivalent", 22(4.2), 22.1(4) | (a) embed the published price-index series and compute every quarter from a base amount; (b) take the previous amount and the two index figures as inputs, one quarter at a time | (b) | The Act defines each amount by "the Consumer Price Index for the first adjustment quarter" and "for the second adjustment quarter", which is published data and is not in the text |
| F-INDEX-2 | s 12(4), 12.1(5), 22.1(6) | when a second fall in the index comes before an earlier one has been made up: (a) the later fall's second index becomes the deemed one; (b) the earlier deemed index stays in force | (b) | Paragraph (b) deems the second adjustment quarter of the quarter of paragraph (a) to be the second one for later quarters until a quarter's first index is higher than it; a quarter in which there is no adjustment does not substitute its own index |
| F-11c | s 11(7)(c), 19(6)(c), 21(9)(b) | "six consecutive months, exclusive of the month in which the pensioner left Canada": (a) the month of leaving is not counted, so the first barred month is the seventh after it; (b) the month of leaving counts as the first of the six; (c) six months counted from the day of leaving | (a): left January, then July is paid and August is barred | The words "exclusive of the month in which the pensioner left Canada" take the month of leaving out of the six, and the limit speaks of a month "throughout which" the person is absent, so whole months are counted |
| F-12-1 | s 12(1), 12(5) | for the quarter beginning April 1, 2005, (1) states a maximum less one dollar for each full two dollars of base income, and (5) says "Despite subsection (2)" the amount for any month after December 1997 is the formula; (a) apply (1) alone; (b) apply (5) alone; (c) encode both | (c): both are rules; the seat uses (5) for every month after December 1997 | (1) names the April 2005 quarter; (5) names "any month after December 1997" and displaces (2), not (1) |
| F-12-2 | s 12(5), 12.1, 22(2), 22(3), 22(4), 22.1 | the formula can come out below zero: (a) a negative supplement; (b) nothing is paid | (b): the raw formula is its own rule and a wrapper takes the greater of it and zero | A supplement "that may be paid" is not a negative sum |
| F-12.1-1 | s 12.1(1), 12.1(2) | the rounding "to the next lower multiple of four dollars" of C: (a) rounds the income in excess of the sum, then divides; (b) rounds the monthly figure that results | (b) | C is defined as "1/12 of the pensioner's income ... in excess of $2,000 rounded ...": the rounding follows the fraction (a test with income 3,000 gives 30, not 29.17) |
| F-12.1-2 | s 12.1(1) | the case C does not name: a pensioner referred to in 12(1)(a) whose spouse or common-law partner may be paid a benefit that is not a pension (an allowance, for example) is neither "a pensioner who has no spouse or common-law partner" (C(a)) nor one whose spouse is a person "to whom no benefit may be paid" (C(b)); (a) treat as C(a); (b) treat as C(b); (c) the text gives no C | (c): the answer is NOTHING, asserted | C has two cases and the Act states no third; 12(1)(b) sends a pensioner whose spouse may be paid a pension to subsection (2), so the gap is the spouse who may be paid an allowance |
| F-15-1 | s 15(3) to (7.2), (8) | when a direction and a deeming give different treatments for a month, or two deemings do: (a) the direction prevails; (b) the later; (c) none is chosen | (c): NOTHING when none operates or two disagree | (8) says the deemings do not limit the power to direct and ranks neither above the other |
| F-15-2 | s 15(2) | "Subject to subsections (3), (4.1) and (4.2)": (a) those subsections lift the waiting rule when they operate; (b) they lift it whether or not they operate | (a): where a direction under (3) or (4.1) has been made, or (4.2) applies, the application may be considered without waiting | The words make (2) subject to those subsections; a subsection that does not operate cannot be a subject-to |
| F-18-1 | s 18(b) | as written: the supplement that would have been paid "if the actual income had been equal to the shown income" is the supplement that was paid, so (b) never pays; (a) the text means the mirror of (a) | both are encoded; the seat uses the mirror | The text of (b) read literally; the mirror is what (b) evidently means |
| F-19-1 | s 19(1)(a), (a.1) | "not more than three months before the month in the payment period": (a) the separation commenced on or after the first day of the month three months before the month; (b) within 90 days; (c) three calendar months counted back from the day | (a) | The text counts in months and the payment is by month |
| F-19-2 | s 19(5) | "no longer meets the conditions set out in subsection (1)" as a separate ground of ceasing: (a) a separate month input; (b) the per-month evaluation of (1) already gives it | (b) | The paragraphs of (1) are read for each month, so a month in which they are no longer met is not paid |
| F-AGE-1 | s 19(1)(b), 21(1)(a) | "has attained sixty years of age but has not attained sixty-five" is not tied to a day: (a) tested on the first day of the month; (b) on the last day of the month before the month; (c) at any time in the month | (b): a month is paid when the person is 60 to 64 on the last day of the month before it | 21(6) starts the allowance in the month after the month in which the person attains 60; 19(5) and 21(8) end it on the expiration of the month in which the person attains 65 |
| F-26-1 | s 26(1) | "with such modifications as the circumstances require" states none: (a) restate sections 14, 15 and 18 for the allowance; (b) apply them with the allowance's facts as inputs and say they apply | (b): a rule says that sections 14, 15 and 18 apply to an allowance | The text states no modification; section 6 is piece oa1's |

## Cross-references out of my ranges

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 11(1) | s 5(1): the pension application is made and approved | oa1 | `the person's application for a pension has been approved` in `s 11: Facts about a pensioner and a month` |
| s 11(7)(b) | the limits on payment of the pension (ss 5 and 9) | oa1 | `no pension may be paid to the pensioner for the month` |
| s 11(8)(b), s 19(6.2)(b), s 21(9.1)(b) | the event "as provided by the regulations" (Regulations section 22.1) | oa3 | `an event as provided by the regulations has occurred` |
| s 12(5), s 12(5.1), s 22(2) | ss 7 and 7.1: the pension amounts before and after the deferral increase | oa1 | the four amount inputs of `s 12(5)`, `s 22(2)` and the record of `s 12(5.1)` |
| s 12(6), s 22(1) | s 7: the full monthly pension | oa1 | `the amount of the full monthly pension calculated without regard to subsection 7(5)`; `the amount of the full monthly pension payable for the month under section 7 ...` |
| ss 12, 12.1, 22, 22.1 | s 2: "special qualifying factor", "specially qualified individual", "income", "pensioner", "survivor" | keel | called by name (`Special qualification facts`, `Income facts`, `the person is a pensioner`, `the person is a survivor`) |
| s 12(2), 12.1(3), 22(4.2), 22.1(4) | Regulation 8: rounding of the product to the cent and of the ratio to three decimals; Regulation 9: the average Consumer Price Index | oa3 | not applied: the amounts are unrounded; the previous amount and the two index figures are inputs |
| s 15(2), (2.2) | s 35: every statement is given in the form the Minister directs | oa1 | `the spouse or common-law partner has filed a statement in prescribed form of the spouse's or common-law partner's income for the base calendar year` (yes/no) |
| s 14(2) to (7) | Regulation 13 (the month in which a person ceases to hold an office, carry on a business or loses pension income) and Regulation 14 (pension income) | oa3 | `the month shown in the statement`; `the pension income received` and `the pension income received by the person in the period the subsection names` |
| s 22 (every allowance amount) | Regulation 6: an allowance of $2 a month or less is paid as $2 | oa3 | none: the amounts of s 22(3) and (4) are given as the Act states them, without the $2 floor (see "Before this is worth relying on") |
| s 15(3.2), 15(4), 19(1.1), 19(1.2), 19(4.01), 22(1), 22(2.1) | s 5(3): the incarcerated person | oa1 | plain inputs ("is an incarcerated person described in subsection 5(3)") |
| s 18(a) | the prescribed manner of deducting | oa3 | none: it changes how, not how much (comment in the module) |
| s 18.2(1), (2) | Regulation 26.1: the manner (in writing to the Minister) and the time (six months after payment begins), and the time for repayment (six months after the request is granted) | oa3 | `the request is made in the prescribed manner`, `the prescribed time after payment of the supplement has commenced` (a `Time limit`), `the amount of any supplement and related allowance is repaid within the prescribed time`; the seat fixes six months and "in writing" from Regulation 26.1(1) |
| s 19(4) | s 30: an application on the pensioner's behalf | oa1 | `an application described in section 30 has been made` |
| s 19(6)(f), s 21(9)(d) | s 5(3): an incarcerated person (the penitentiary and prison conditions) | oa1 (the keel holds the sentence facts) | the keel's `Sentence of imprisonment` record, passed in as a fact |
| s 19(2), s 21(2) | Regulation 22(1), made under ss 19(3) and 21(3): the meaning of legal residence | oa3 | `on the day preceding the day on which the application for an allowance is approved the person is legally resident in Canada` and its three siblings (a yes/no each) |
| s 21.1(4) | s 37: a debt due to the Crown | oa1 | the fact `the person has received an allowance referred to in this section` (comment `out of range: section 37` in the module) |
| s 23(1), s 23(2) | the earlier dates prescribed by regulation | oa3 | `the earlier date prescribed by regulation`, `the earlier day prescribed by regulation` |
| s 26(1) | s 6: the Minister's power to ascertain age | oa1 | none: a rule says that sections 14, 15 and 18 apply |
| s 11(7)(e), s 19(6)(d), s 21(9)(c) | the Immigration and Refugee Protection Act: a sponsor's undertaking | external | the fact "an undertaking by a sponsor is in effect" |
| s 21.1 | the Criminal Code: murder, manslaughter, a probation order | external | the facts about the conviction (7 inputs) |
| s 13, s 14, s 12(6) | the Income Tax Act: income | external | the keel's `Income facts` where income is worked out; elsewhere a number named for the s 2 term |
| s 13 | the home insulation or energy conversion program that is "prescribed": the Old Age Security Regulations do not name it | none | `grants under a prescribed home insulation or energy conversion program of the Government of Canada, included in the income` (a number) |

## Needs from the core

Nothing blocks this piece. Three things the lead may want to settle at the merge:
1. `oa2-indexation` is the quarterly index step ("previous amount times the ratio of the two index figures, never less, with the carry of an unmatched fall"). It names no provision of Part II, so it is a candidate for the shared core if Part I (s 7.1) uses the same step. It is local until then, under the prefix `oa2`.
2. The inputs `the pensioner is an incarcerated person described in subsection 5(3)` (in `oa2-part2-spouse`, `oa2-part3-amount`, `oa2-part3-spouse-allowance`) and `an application described in section 30 has been made` are plain facts here. If piece oa1 defines rules for subsection 5(3) and section 30, those inputs can be replaced by calls to them.
3. The amounts of the pension (before and after the increase of s 7.1, and the monthly pension of s 2.1(2)) enter as plain numbers, and the keel's selector rules are called for "the amount of a full monthly pension" and "the pensioner's monthly pension in subsections 12(5) and 22(2)". A section 7 rule from oa1 would feed them.

## What the text turns out to say

1. The Act gives no figure for the Consumer Price Index and does not round: indexed amounts follow only if the caller supplies the published index figures, and the rounding of the amounts and of the ratio is in Regulations section 8 (piece oa3), which is not applied here. Not asserted: it is a limit of the input.
2. Section 12(5) replaces the reduction of 12(1) ("minus one dollar for each full two dollars of the monthly base income") by its own formula for every month after December 1997, and its words "Despite subsection (2)" do not mention 12(1), so the April 1, 2005 quarter has two formulas in force (F-12-1). Both are encoded and both are tested separately; no assertion compares them, because the text does not say which wins.
3. The increase of July 1, 2016 is $78.92 on A in 12.1(1) and, in 12.1(2), on A in the case of paragraph (a) of A only, the $50 case (12(1)(b)(i)); the $35 case gets none (s 12.1(2.1)). In section 22.1 the Act adds it to A in subsection (3), the survivor's, only: subsections (1) and (2) have no 2016 increase because the Act names none. The absence of an increase in 22.1(1) and (2) is the absence of a rule and cannot be asserted; the other increases are. Asserted.
4. In 22(3) the formulas (a) and (b) agree at no joint income (both give 1000 in the test), and (b) and (c) meet without a jump at the product that divides them: a joint income "equal to" the product is (b) and "more than" it is (c), and the test shows 300 on either side (936 and 937). Asserted.
5. Section 12.1(1) gives C two cases only: no spouse or common-law partner, or a spouse or partner to whom no benefit may be paid. A pensioner of 12(1)(a) whose spouse or partner may be paid a benefit that is not a pension (an allowance, for example) is in neither, and the answer is NOTHING, not zero (F-12.1-2). Asserted.
6. Section 18(b) as written pays nothing, because "the supplement that would have been paid if the actual income had been equal to the shown income" is the supplement that was paid (F-18-1). Asserted.
7. A spouse is never "separated" for 19(1)(a) if the sole reason is that the pensioner is incarcerated (19(1.2)); common-law partners do not become former common-law partners if the sole reason is that either is incarcerated (19(1.1)). The first speaks of the pensioner only, the second of either partner. Asserted.
8. A person born on the first of a month attains 60 on the first of that month and is first paid in the month after (born April 1, 1960: April 2020 is not payable, May 2020 is), and attains 65 on the first of a month and is still paid for that month (April 1, 2025: April is payable, May is not): the words of 19(5) and 21(8) end the allowance "on the expiration of the month in which" the person attains 65, and 21(6) starts it in the month after the month of the 60th birthday (F-AGE-1). Asserted.
9. A survivor's eligibility is not affected by another person's eligibility in respect of the same deceased (21(12)): the rule takes the other person's eligibility as an input and gives the same answer whichever it is. Asserted.
10. Section 11(7)(c) counts "six consecutive months, exclusive of the month in which the pensioner left Canada": a pensioner who left in January 2023 is paid for July 2023 and barred from August 2023 (F-11c). Paragraphs 19(6)(c) and 21(9)(b) say the same of the allowance and are read the same way, with the same boundary (the last day of July is not barred, the first of August is). Asserted.
11. The range contains no commencement date. Paragraph 19(6)(e) and subsection 21(7.1) bar months "before the month in which" they come into force, and the Act does not say when that was: the month is an input in each rule. Paragraphs 11(8)(a), 19(6.2)(a) and 21(9.1)(a) (a person qualified "immediately before the day on which this paragraph comes into force") are facts the person states. Not asserted: there is no date in the text to assert.
12. The Act file ends with AMENDMENTS NOT IN FORCE (from line 1176) that would amend provisions in my range, among them 19(4), 21(4) and 24(1). They belong to piece oa1 and the source marks them not in force: the in-force text is encoded and nothing is merged from them.
13. Subsections 15(6) and 15(7) are repealed in this text ("[Repealed, 2000, c. 12, s. 194]"), and so is the definition of "current fiscal year" in the list of definitions in 22(1) ("[Repealed, 1998, c. 21, s. 116]"); nothing is encoded for them.
14. The text is an unofficial rendering of a consolidation current to 2026-09-30 and nothing here is checked against the official text.

## What the stable binary does not accept

Loud failures (the binary says so; the fix is in the module):
- `DOES NOT EQUAL` is not an operator ("unexpected DOES"): write `NOT (a EQUALS b)`.
- A single-letter name (`A`, `B`, `C`, `D`, the letters the Act uses in its formulas) fails with "unexpected A": the modules name them `partA`, `partB`, `partC`, `partD`.
- An `IF ... ELSE IF ... ELSE` chain on separate lines fails with "incorrect indentation (got 10, should be greater than 10)": write `BRANCH` with one `IF ... THEN ...` line per case and a last `OTHERWISE ...` line (as in `oa2-part2-amount`).
- There is no record update. `value WITH field IS x` fails ("which is not a function"); `Type WITH f IS v ...` builds a record from the type name and needs every field. The tests build their variants from a template with every field listed.
- REFUSE, BECAUSE, section GIVEN, TYPICALLY, sets and ASSUME are not used (not accepted by 1.6.98, per the brief).
- A possessive after a call binds to the call's last argument, not to the call: `` `mk` y's `b` `` reads `` `mk` (y's `b`) ``. When the types do not fit it is a loud type error ("The argument of the projection ... is expected to be of type"); when they do fit it would be silent. Write `` (`mk` y)'s `b` `` or bind the call in a `WHERE`.

Silent failures (the binary runs and gives a different answer):
- **`NOT a OR b` on one line is `NOT (a OR b)`**, and `NOT a AND b` is `NOT (a AND b)`: NOT takes everything to its right on the line. A chain with the operator leading each line (`AND NOT x` on one line, `AND y` on the next) is fine. This went wrong once in `s 21.1(1)` (a foreign conviction was treated as not counting even when the Minister had deemed it) and was caught by an assertion; every other `NOT` in the modules was checked by hand. Parenthesise: `((NOT x) OR y)`.
- A long `AND` chain that contains a `WHERE` or `CONSIDER` makes the type checker very slow (one composite took over a minute); the modules split such chains into small rules. A test file that imports many oa2 modules takes 100 to 190 seconds, and the seat (60 questions over all the modules) about ten minutes to check on a loaded machine (measured at 582 seconds for 59 questions).

## What check.sh prints

Run as `L4=<the stable 1.6.98 binary> L4_TARGET=unstable ./check.sh` in this folder, after the last edit to any module.
It printed this on stdout:

```
module                                    errors satisfied  failed  refused  expected
oa2-cases-seat.l4                              0       149       0        0         0
oa2-indexation.l4                              0         0       0        0         0
oa2-part2-amount.l4                            0         0       0        0         0
oa2-part2-eligibility.l4                       0         0       0        0         0
oa2-part2-income.l4                            0         0       0        0         0
oa2-part2-payment.l4                           0         0       0        0         0
oa2-part2-spouse.l4                            0         0       0        0         0
oa2-part3-amount.l4                            0         0       0        0         0
oa2-part3-payment.l4                           0         0       0        0         0
oa2-part3-spouse-allowance.l4                  0         0       0        0         0
oa2-part3-survivor-allowance.l4                0         0       0        0         0
oa2-seat.l4                                    0         0       0        0         0
oa2-tests-indexation.l4                        0        18       0        0         0
oa2-tests-part2-amount.l4                      0        90       0        0         0
oa2-tests-part2-eligibility.l4                 0        73       0        0         0
oa2-tests-part2-income.l4                      0        88       0        0         0
oa2-tests-part2-payment.l4                     0        48       0        0         0
oa2-tests-part2-spouse.l4                      0       107       0        0         0
oa2-tests-part3-amount.l4                      0       136       0        0         0
oa2-tests-part3-payment.l4                     0        44       0        0         0
oa2-tests-part3-spouse-allowance.l4            0       133       0        0         0
oa2-tests-part3-survivor-allowance.l4          0       135       0        0         0
oas-core-income.l4                             0         0       0        0         0
oas-core-measures.l4                           0         0       0        0         0
oas-core-pension.l4                            0         0       0        0         0
oas-core-periods.l4                            0         0       0        0         0
oas-core-terms.l4                              0         0       0        0         0
oas-core.l4                                    0         0       0        0         0
TOTAL (28 modules)                             0      1021       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

On stderr it printed `check.sh: the target is unstable, so the main check was skipped.`, and its exit status was 0.

The 28 modules are the 10 layer-1 modules, their 10 test files, the seat, the cases file and the keel's six `oas-core*` files.
The 1021 satisfied assertions are 872 in the ten test files and 149 in `oa2-cases-seat.l4`, and each file's satisfied count equals the number of `#ASSERT` lines it carries.
No assertion fails or is refused on purpose, so the `expected_failed` list in `check.sh` stays empty.
The second run the brief asks for, `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/R.S.C.-1985-c.-O-9.txt oa2-*.l4`, printed `srcrefs check: 458 src: lines, 198 runs, 247 locators, 0 problems`; the Regulations' run is vacuous because this piece has no module that quotes the Regulations.

## Before this is worth relying on

- The text must be checked against the official consolidation: the file is an unofficial rendering.
- The Regulations (piece oa3) must supply the prescribed figures and rules: the earlier dates of s 23, the manner and time of s 18.2, the event of 11(8)(b), the rounding of indexed amounts (Regulation 8), and legal residence.
- The published index figures and the published maxima, the supplement equivalents and the figure A must be supplied by whoever uses the seat; the encoding does not carry the price index series (F-INDEX-1).
- Part I (piece oa1) must supply the pension amounts, the incarcerated person of 5(3) and the section 30 application; today they are plain inputs.
- The dates on which 19(6)(e) and 21(7.1) came into force must be supplied; the Act file does not give them.
- Every fork in the register is a reading chosen where the text does not settle; the ones that change an amount (F-12-1, F-12-2, F-12.1-1, F-18-1) deserve a lawyer's eye first.
- Regulation 6 (an allowance of $2 a month or less is paid as $2) is piece oa3's and is not applied: an amount the seat gives for an allowance that is between $0 and $2 is not the amount paid. The seat takes the earlier date of s 23(1) as an input, though Regulation 12 computes it; the merge should connect that question to oa3's rule for Regulation 12.
- The seat treats the Minister's judgments (satisfied, approved, waived) as facts the person states; it does not predict them.
