# Home Affairs Uniformed Services Superannuation Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/HAUSSA2001.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The latest amending Act annotated in the body is Act 35 of 2019; the
Legislative History lists Act 40 of 2018 (in force 30 July 2020) last. SSO marked it
the current version as at 1 October 2026 when it was retrieved. The arrangement of
sections at the top of the deposit is out of step with the body for Part 4; the body's
numbering is followed.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0173** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person it applies to; no scenario has asked a sharper question yet. The
people it applies to are police, civil defence, narcotics, prison and intelligence
officers and their families.

The Act is a framework: the INVEST Plan itself, including its contributions, rates and
retirement ages, is made by regulations (s 3), and none were retrieved. So this row
computes no benefit amount. It takes what the Act itself decides: who is brought into
the Plan (ss 2, 3(1), 4(1)), who may dismiss a member or cut a benefit (s 6), what
creditors may take (s 7), bankruptcy and imprisonment (ss 8, 9), recovery (s 11), the
Board's investment bar and size (ss 15, 19), appeals (s 23) and the Fund's financial year
(s 24(9)). Not encoded: s 4(2)'s guaranteed value for converting officers, s 5, s 10
(death benefits held on trust outside the estate), the Fund's money flows (ss 12-14,
16-18), Board functions and delegation (ss 20-22), audit and actuarial examination
(ss 24(1)-(8), 25) and s 26.

## What the Act turns out to say

### 1. A free pardon restores a stopped pension in full; serving the sentence restores nothing

Under s 9(1) the Minister may stop the pension of anyone sentenced to "any term of
imprisonment", in Singapore or elsewhere. s 9(2) restores it "with retrospective effect"
only on a free pardon. Release after serving the sentence brings no restoration duty; s
9(3) lets the Minister pay the family, or the pensioner after the sentence, at
discretion. A fine alone does not trigger s 9. Asserted.

### 2. Discharge from bankruptcy restores the pension only from the date of discharge

s 8(3) lets the Minister stop a bankrupt pensioner's pension; s 8(5) says that on "a full
and proper discharge" it "must be restored ... with effect from the date of the
discharge". So, unlike a pardon, the stopped months are not repaid. An award officer may
also refuse the award to a member who is an undischarged bankrupt at retirement or
resignation (s 8(2)). Asserted.

### 3. Creditors cannot touch the benefits, except the Government and some maintenance orders

s 7 shields every benefit, Government contribution and interest from assignment,
garnishment and attachment, except for a debt due to the Government, or a court order for
"periodical sums" for the maintenance of "the wife or former wife or minor child (whether
legitimate or not)". Read literally, a husband's maintenance order, an adult child's, and
a lump-sum order are outside the exception. Whether other law reads "wife" more widely
was not checked. Asserted.

### 4. Intelligence officers already serving had no option to convert

s 3(1)(e) brings in intelligence officers appointed after the regulations began. But the
s 4(1) option to leave the Pensions Act scheme for the INVEST Plan is given only to civil
defence, narcotics, police and prison officers. Auxiliary police, Special Constabulary
members and police national servicemen are not "uniformed service officers" at all (s
2). Asserted.

### 5. Who decides depends on rank

For a junior police officer (below inspector), the Commissioner of Police both dismisses
and cuts benefits. For everyone else the Public Service Commission dismisses, but a
Permanent Secretary to the Ministry of Home Affairs cuts benefits (s 6(3), (4)).
Asserted.

### 6. No court appeal from an award, and 12 months to appeal to the Minister

Unless regulations provide otherwise, no award goes to court (s 23(2)). The Minister's
review may increase or decrease the award and is "final and conclusive" (s 23(3)). The
appeal must be brought within 12 months of notification, unless a longer period is
allowed (s 23(4)). Whether month 12 itself counts as in time is an inference. Asserted.

### 7. The Fund may not buy Government paper

s 15(1) lets the Board invest as it thinks fit "but not any stock, bond or security issued
by the Government". Derivatives used for effective portfolio management count as
investments (s 15(4)). The Board has 5 to 15 trustees, each appointed for up to 3 years
(s 19). The Fund's year runs from 1 April to 31 March (s 24(9)). Asserted.

## What would need doing before this is worth anything

- The INVEST Plan regulations, which hold every amount, rate and retirement age, were
  not retrieved. Without them the row cannot say what any officer receives.
- s 4(1)(b) speaks of "every officer" on a contract in the four Services. Whether such an
  officer is on the "permanent establishment", and so a "uniformed service officer", is
  not settled by the text. The row treats them as one category (an inference).
- Article 113 of the Constitution, which qualifies s 6(2), was not read.
- No case law or decisions were searched.
