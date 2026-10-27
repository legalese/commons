# NOTES: piece cp3 of the Canada Pension Plan encoding (Part II: the Part's opening provisions, Division A, and Division B as far as the division of first additional unadjusted pensionable earnings)

STATUS: layer 1 (sections 42 to 55.2(5.1)) and the seat layer are written, and every assertion in the cp3 files was satisfied at the last `check.sh` run recorded under "What check.sh prints".
No lawyer has read this, and no independent test pass (a second agent writing tests from the text without seeing these) has been run: see "Before this is worth relying on".

The source is `R.S.C.-1985-c.-C-8.txt` (the Canada Pension Plan Act, R.S.C. 1985, c. C-8), lines 921-1569, a plain-text rendering made by a converter script from the Justice Laws consolidation.
It is not the official text, and nothing in this folder has been checked against the official text.
Every `src:N` locator in the `.l4` files is a line number of that file.
The range runs from the heading of Part II (line 921) through section 55.2(5.1) (line 1569); subsection 55.2(5.2) onward is piece cp4.

Which instrument each rule comes from: every rule in this folder comes from the Act.
Where the Act leaves a figure or a condition to the Regulations (C.R.C., c. 385; also among the inputs), this piece does not encode the Regulation: the figure or the outcome is a plain input, named for the fact, and the Regulation is named in "Cross-references out of my ranges" (the Regulations' Part V is piece cr2's range).
That follows the brief's rule for any rule outside the range, and it keeps two encodings of one regulation from disagreeing.
If the lead wants the Regulations' formulae inside cp3 instead (regulations 78.3 and 78.4 for the factor of subsection 46(3.1), regulation 75 for the rounding of the Pension Index, regulation 62 for the rounding of the annual adjustment), that is a change to the inputs of `cp3-retirement-pension.l4` and `cp3-part2-interpretation.l4`, and it would duplicate cr2.

Dates are data: this range contains no date of enactment and no commencement rule that fixes a date.
Two provisions speak of "the coming into force of this section" and the text carries no date for it: subsection 44.1(5) (`cp3 When the Minister is informed of a conviction`, three constructors, all of which the subsection covers) and section 55.11 (the day is a stated input of `s 55.11 — section 55.1 applies to the case`).
The dates the text states are written into the rules that compare against them, each under that rule's `@ref`; the ones a whole module shares are defined values of their own: 1 January 1966 (section 49 and subsection 44(2)(b)), 1 January 1978 (sections 49(d), 44(2)(b)(iv) and 55(1)) and 1987 (section 55(1)), 1 January 2019 (subsection 44(1)(d) and section 49.1), 1 January 2024 (section 49.2), 1 January 2025 (section 44.2).
One date appears only inside the name of a yes-or-no input, because the rule tests the fact and not the date: 4 June 1986 in subsections 55.2(2) and (3).

## Seat

The seat is the individual to whom Part II is applied (ruled for Commons on 2026-10-18).
It is a contributor, whether a worker or a self-employed person, who may claim a retirement pension or a post-retirement benefit, or, if disabled, a disability pension or a post-retirement disability benefit; the survivor, the child (dependent child, orphan, disabled contributor's child) and the estate or succession of a deceased contributor; a person whose disability the Minister determines; a former spouse or former common-law partner whose earnings may be divided; and an individual convicted of killing the contributor, to whom sections 44.1 and 44.2 apply.
The questions are phrased as that person would ask them ("Am I entitled to ...?", "What am I liable to repay ...?", "Must I be notified ...?").
The Minister, the court and the department get no seat.

No second seat is written.
Part II puts no duty or liability on an employer or on any other private party, so the further seat layers that Commons allows would have nothing to ask; the employer's duties are in Part I (pieces cp1 and cp2).

How the seat layer is built (`cp3-seat.l4`, with `cp3-cases-seat.l4`):

- Every question has `@export` and, on each input, an inline `@desc`.
- Inputs are plain: yes or no, a number, a date. There are no list inputs. Where a rule takes a list (the years of a record, the twelve Consumer Price Index figures), the question asks for the numbers the person can state: how many years count, how many months, the total, or each of the twelve figures.
- A judgment the Act hands to the Minister ("the Minister is satisfied", "informed and satisfied", "determined in the prescribed manner") is its own input, worded as a fact the person could be told; no answer here decides it.
- A fact about the other party is an input too, paired with its date where the rule needs one (a death, a separation, the day an application was made).
- The seat layer imports the layer-1 modules and calls their rules; it restates none of them. One helper (`cp3 seat — the kind of dependent child I am`) only passes the same facts to the layer-1 rule that classifies a child, so that three questions can share it.
- Paired duty questions (Hohfeld): where the text gives the person a claim, a paired question asks what the other side owes ("Am I to be notified when a division is approved?", "Must I be notified without delay of a division?", "Will my entitlement be reinstated and what was recovered repaid?"); where the text gives the Minister a power, a paired question asks what may be done to the person ("Can the Minister refuse to make or cancel my division ...?", "What am I liable to repay ...?", "Is a survivor's pension not payable to me because of ...?").
- Questions are grouped under `§§` headings in the order of the text. Sections 51 to 52.2 (month-by-month earnings), 50 to 50.2 (sums of monthly lists), the lookback records of sections 51.1, 51.2, 53.3 and 53.4, the months of cohabitation of subsections 55(3) and 55.1(4), the multi-year form of the annual adjustment in subsection 45(2) and the list deductions of subsections 48(2) to (4) have no question: each needs a list or a record that one answer cannot carry. They are encoded and tested in layer 1.

The questions (86), by group:

**Who counts: contributor, disabled, survivor, child (sections 2(1), 42)**

- Am I a contributor under the Canada Pension Plan (s 2(1))?
- Am I considered disabled under the Canada Pension Plan (s 42(2)(a))?
- From what date am I deemed to have become disabled (s 42(2)(b))?
- Am I a child of the contributor under the Canada Pension Plan (s 42(1))?
- Am I a dependent child of the contributor under the Canada Pension Plan (s 42(1))?
- Am I an orphan of the contributor under the Canada Pension Plan (s 42(1))?
- Am I a disabled contributor's child under the Canada Pension Plan (s 42(1))?
- Am I a survivor of the contributor under the Canada Pension Plan (s 42(1))?
- Am I a survivor with dependent children under the Canada Pension Plan (s 42(1))?
- What is my basic number of contributory months (s 42(1))?

**The Pension Index (section 43)**

- What is the Pension Index for a year, from the twelve monthly Consumer Price Index figures (s 43(1))?
- What is the Pension Index for a year, given that it never falls (s 43(2))?

**Whether a benefit is payable to me (section 44)**

- Am I entitled to a retirement pension (s 44(1)(a))?
- Have I made base contributions for the minimum qualifying period for a disability pension (s 44(2)(a))?
- What is my basic exemption for the year I would have been considered disabled, if I applied late (s 44(2.1))?
- Am I deemed to have the minimum qualifying period as a late applicant who was a family allowance recipient (s 44(2.2))?
- Am I entitled to a disability pension (s 44(1)(b))?
- Did the deceased contributor make base contributions for the minimum qualifying period for a death benefit, survivor's pension or orphan's benefit (s 44(3))?
- Is a death benefit payable to the estate or succession of the deceased contributor (s 44(1)(c))?
- Am I entitled to a survivor's pension (s 44(1)(d))?
- Am I entitled to an orphan's benefit (s 44(1)(f))?
- Am I entitled to a disabled contributor's child's benefit (s 44(1)(e))?
- Am I entitled to a post-retirement benefit (s 44(1)(g))?
- Have I made base contributions for the minimum qualifying period for a post-retirement disability benefit (s 44(4))?
- Am I entitled to a post-retirement disability benefit (s 44(1)(h))?

**Conviction for killing the contributor, and survivor's pension after a division (sections 44.1 and 44.2)**

- Is my conviction one that engages section 44.1 (s 44.1)?
- Is a survivor's pension not payable to me because of a conviction for killing the contributor (s 44.1(1)(a))?
- Is a death benefit not payable to me because of a conviction for killing the contributor (s 44.1(1)(b))?
- Is an orphan's benefit not payable to me because of a conviction for killing the contributor (s 44.1(1)(c))?
- Will my entitlement be reinstated and what was recovered repaid (s 44.1(2))?
- What am I liable to repay because of a conviction for killing the contributor (s 44.1(4))?
- Is a survivor's pension not payable to me because of an earlier division of earnings (s 44.2)?

**My retirement pension and its adjustments (sections 45 and 46)**

- What is the basic monthly amount of my retirement pension (s 46(1))?
- What is the first portion of my retirement pension as a former disability pension recipient whose pension a division reduces (s 46(2))?
- What is my retirement pension if it starts after 1986 and before 2011, adjusted for starting early or late (s 46(3))?
- What is my retirement pension if it starts after 2010, adjusted for starting early or late (s 46(3.1))?
- What adjustment factor applies after a division increases my retirement pension (s 46(4))?
- What is my retirement pension when my survivor's pension has been reduced (s 46(5))?
- Over what time interval is the upward adjustment for a division after I reach 65 worked out (s 46(6))?
- What will be paid to me for a month in the following year after the annual adjustment (s 45(2))?

**My average monthly pensionable earnings and my contributory period (sections 47 to 50.2)**

- What are my average monthly pensionable earnings before any deduction (s 48(1))?
- What percentage of my remaining months is deducted when working out my average (s 48(4)(a)(i))?
- What are my first additional monthly pensionable earnings when my first additional contributory period is no longer than 480 months (s 48.1(a))?
- What are my second additional monthly pensionable earnings when my second additional contributory period is no longer than 480 months (s 48.2(a))?
- In which month does my contributory period begin (s 49)?
- In which month does my contributory period end for a retirement pension (s 49)?
- How many months are in my contributory period (s 49)?
- Is a month excluded from my contributory period (s 49(c), (d))?
- In which month does my first additional contributory period begin (s 49.1)?
- In which month does my first additional contributory period end (s 49.1)?
- In which month does my second additional contributory period begin (s 49.2)?
- In which month does my second additional contributory period end (s 49.2)?

**My unadjusted pensionable earnings for a year (sections 53 to 54.2)**

- What are my base unadjusted pensionable earnings for a year (s 53(1))?
- What is my basic exemption in the year my retirement pension becomes payable (s 53(2)(a))?
- What are my maximum pensionable earnings in the year my retirement pension becomes payable (s 53(2)(b))?
- What are my first additional unadjusted pensionable earnings for a year (s 53.1(1))?
- What are my second additional unadjusted pensionable earnings for a year (s 53.2(1))?
- What are my first additional unadjusted pensionable earnings for a year in which an amount is attributed to me as a family allowance recipient (s 53.5)?
- What are my second additional unadjusted pensionable earnings for a year in which an amount is attributed to me as a family allowance recipient (s 53.6)?
- What are my base unadjusted pensionable earnings for a year in which my earnings are divided (s 54)?
- What are my first additional unadjusted pensionable earnings for a year in which my earnings are divided (s 54.1)?
- What are my second additional unadjusted pensionable earnings for a year in which my earnings are divided (s 54.2)?

**Dividing earnings with a former spouse or partner: judgments between 1978 and 1987 (section 55)**

- May I apply for a division of earnings after a divorce or annulment between 1978 and 1987 (s 55(1))?
- Did we cohabit long enough for a division after a divorce or annulment between 1978 and 1987 (s 55(2)(a))?
- On what day is my marriage deemed solemnized, nullified or my divorce deemed made final (s 55(2)(b))?
- Are we deemed to have cohabited during a year (s 55(2)(c))?
- What is attributed to me when the Minister approves a division after a divorce or annulment between 1978 and 1987 (s 55(4))?
- What are my total unadjusted pensionable earnings for a year of division under the Act and a provincial pension plan (s 55(5))?
- Is a division made for a month of our period of cohabitation (s 55(6))?
- From which month will my benefit be paid at the amount recalculated for a division (s 55(7))?
- Am I to be notified when a division is approved (s 55(8))?
- Do I have a right of appeal against a division (s 55(8))?

**Dividing earnings with a former spouse or partner: divorce, separation and the end of a common-law partnership (sections 55.1 to 55.2)**

- Will my earnings be divided on my divorce or the annulment of my marriage (s 55.1(1)(a))?
- Can my earnings be divided on application because my spouse and I live separate and apart (s 55.1(1)(b))?
- Can my earnings be divided on application because my common-law partner and I have separated (s 55.1(1)(c))?
- Are we deemed to have lived separate and apart for a period (s 55.1(2)(a))?
- Is our separation treated as continuing despite an interruption (s 55.1(2)(b))?
- Did we cohabit for a continuous period of at least one year (s 55.1(3))?
- Can the Minister refuse to make or cancel my division because both our benefits would decrease (s 55.1(5))?
- Does a division of my earnings take place under section 55.1 (s 55.1)?
- Does section 55.1 apply to my case (s 55.11)?
- Does the Act say that our agreement or a court order made on or after June 4, 1986 does not bind the Minister in a division (s 55.2(2))?
- Does our agreement that there be no division bind the Minister (s 55.2(3))?
- Must I be notified without delay of a division (s 55.2(4))?
- What base earnings are attributed to me on a division under section 55.1 (s 55.2(5))?
- What first additional earnings are attributed to me on a division under section 55.1 (s 55.2(5.1))?

(86 questions.)

## Jural relations

Each row pairs an advantage with its correlative (Hohfeld).
"Claim / duty": the holder may demand, the other must.
"Power / liability": the holder can change the other's position, and the other is exposed to it.
"Disability / immunity": the holder cannot, and the other is safe from it.
"Privilege / no-claim": the holder is free to, and the other cannot demand otherwise.
Definitions and calculations (sections 42, 43, 45, 46, 47 to 54.2) create no relation of their own: they fix the content of the claims below and are listed `none`.

| provision | holder of the advantage | advantage | other party | correlative | note |
| --- | --- | --- | --- | --- | --- |
| 44(1)(a) | a contributor who has reached 60 | claim to a retirement pension | the Minister | duty to pay it | "shall be paid"; the payment is applied for under Division C (piece cp4) |
| 44(1)(b) | a disabled contributor under 65 to whom no retirement pension is payable | claim to a disability pension | the Minister | duty to pay it | one of three limbs, alternatives (fork F12) |
| 44(1)(c) | the estate or succession of a deceased contributor | claim to a death benefit | the Minister | duty to pay it | the right is the estate's or succession's, not an individual's |
| 44(1)(d) | the survivor of a deceased contributor | claim to a survivor's pension | the Minister | duty to pay it | from 2019 on the minimum qualifying period alone |
| 44(1)(e) | a child of a disabled contributor | claim to a disabled contributor's child's benefit | the Minister | duty to pay it | limbs describe the contributor (fork F16) |
| 44(1)(f) | an orphan of a deceased contributor | claim to an orphan's benefit | the Minister | duty to pay it | |
| 44(1)(g), (h) | a beneficiary of a retirement pension | claim to a post-retirement benefit; if disabled and under 65, to a post-retirement disability benefit | the Minister | duty to pay it | |
| 44.1(1), 44.2 | the Minister | privilege not to pay a survivor's pension, death benefit or orphan's benefit | the individual convicted of killing the contributor; the survivor after a division and no new year-long relationship | no-claim | the Minister's being informed and satisfied is an input |
| 44.1(3) | the Minister | power to deem a conviction outside Canada to be a conviction of murder or manslaughter | the individual convicted outside Canada | liability to the bar of subsection (1) | "may deem" is read as the fact that the Minister has deemed (fork F27) |
| 44.1(2) | the individual whose conviction is reversed, or charges withdrawn, or proceedings stayed | claim to reinstatement and to repayment of what was recovered | the Minister | duty to reinstate and repay | "shall be reinstated" |
| 44.1(4) | Her Majesty | claim to repayment of what was received, including before the conviction, as a debt under section 66 (piece cp5) | the individual | duty to repay; the Minister has the duty to recover ("shall recover") | the individual's side is the liability the seat asks about |
| 45(2) | a beneficiary | claim to the annual adjustment of the benefit | the Minister | duty to adjust | "shall be adjusted annually, in prescribed manner" |
| 55(1) | either former spouse, the estate or succession of either, or a person who may be prescribed | power to apply for a division | the other former spouse and the Minister | liability to a division | 36 months, or any time if both agree in writing |
| 55(2)(a), 55.1(1)(b), (c) | the Minister | power to approve the application | the former spouses or partners | liability to the division | approval is an input, supplied conditionally |
| 55(8), 55.2(4) | each person subject to the division, the applicant | claim to be notified | the Minister | duty to notify, without delay in 55.2(4) | the manner is by regulation 46 (cr2) |
| 55(8) | the dissatisfied applicant or former spouse, or the estate | power to appeal | the Minister | liability to review | the appeal is in a later Division (cp4, cp5) |
| 55.1(1)(a), (b), (c) | the persons whose earnings are divided | (their earnings are divided as a consequence) | the Minister | duty to make the division ("shall take place") | subject to 55.1(3), 55.1(5), 55.2(3) and 55.3 |
| 55.1(5) | the Minister | power to refuse to make or to cancel a division | the persons subject to the division | liability to its not being made or its cancellation | only if benefits are payable to both and both would decrease |
| 55.2(3) | the persons subject to the division | power, by a written agreement, to bind the Minister to make no division | the Minister | disability: the Minister shall not make the division | four conditions, all required |
| 55.2(2) | the Minister | immunity from being bound by an agreement or court order made on or after 4 June 1986 | the persons subject to the division | disability to bind the Minister, except under (3) | |
| 55(9) | the Governor in Council | power to make regulations on applications for a division | everyone subject to Part II | liability to those regulations | left out: machinery (see the coverage table) |

Not a relation: the definitions of sections 42 and 43, the amounts of sections 45 to 54.2, the contributory periods of sections 49 to 50.2, and the deemed contributions of sections 52 to 52.2.

## Coverage table

One row per provision of lines 921-1569: a row per section, and a row per subsection, paragraph or definition wherever they differ in disposition or in the rule they state.
The source lines of a row include its marginal note (a heading line) where it has one; such a heading line is not quoted in a module.
Dispositions: `encoded` (in layer 1, and in layer 2 where a person would ask), `fork` (the text does not settle the reading: the row cites the fork register and the rule encodes the reading taken), `inert` (with its reason), `repealed or blank in this text`.
"Where" names the module `cp3-<name>.l4` and the rules in it; a rule with an `-- out of range:` comment depends on something in "Cross-references out of my ranges".

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Group heading: Part II Pensions and Supplementary Benefits | src:921 | inert | none | a pure title: names Part II (pensions and supplementary benefits); it states no right, duty or condition and carries no figure |
| Group heading: Interpretation | src:923 | inert | none | a pure title (the heading "Interpretation") over section 42; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 42(1) chapeau (marginal note Definitions) | src:924-925 | inert | none | "In this Part," frames the definitions that follow; each definition has its own row below |
| s 42(1) "basic number of contributory months" | src:926 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — the basic number of contributory months` | 120 minus the months excluded by reason of disability; the text sets no floor (finding 1) |
| s 42(1) "child of a contributor" | src:927-930 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — a child of a contributor` | paragraphs (a) and (b) and the closing exclusion; maintaining a child is regulation 65.1 (cr2), an input |
| s 42(1) "decision-making responsibility" | src:931 | encoded | input of `s 42(1) — a child of a contributor` | meaning is that of the Divorce Act, subsection 2(1), which is not among the inputs: it is part of the plain input about parenting time or decision-making responsibility |
| s 42(1) "dependent child of a contributor" | src:932-937 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — the kind of dependent child that a child of a contributor is`, `s 42(1) — a dependent child of a contributor` | paragraphs (a) to (c); ages through section 2(2); school and university as defined by regulation 66 (cr2) are inputs |
| s 42(1) "disabled contributor's child" | src:938 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — a disabled contributor's child` | dependent child of a disabled contributor, without paragraph (c) children |
| s 42(1) "family allowance recipient" | src:939 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — a family allowance recipient` | the Family Allowances Act limb is a plain fact; the "prescribed" limb is regulation 77 (cr2), an input |
| s 42(1) "Maximum Pensionable Earnings Average" | src:940-944 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — the Maximum Pensionable Earnings Average for a year`, `s 42(1) "Maximum Pensionable Earnings Average" — the first day of 1933` | the figures of section 18 (cp1) are supplied per year; NOTHING when a year's figure is missing |
| s 42(1) "Minister" | src:945 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — the Minister of Part II` | the Minister of Employment and Social Development |
| s 42(1) "orphan of a contributor" | src:946 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — an orphan of a contributor` | dependent child of a deceased contributor, without paragraph (c) children |
| s 42(1) "parenting time" | src:947 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — time that is a person's parenting time` | care by a parent, a person standing in a parent's place or one who intends to; physical presence is irrelevant |
| s 42(1) "substantially gainful" | src:948 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — an occupation is substantially gainful` | meaning left to regulations (regulation 68.1, cr2): a plain input |
| s 42(1) "surviving spouse with dependent children" | src:949 | repealed or blank in this text | none | [Repealed, 2000, c. 12, s. 44] |
| s 42(1) "survivor" | src:950-952 | fork | `cp3-part2-interpretation.l4`: `s 42(1) — a survivor of a deceased contributor` | the common-law partner at death; the married person only if there was no common-law partner at death (fork F1) |
| s 42(1) "survivor with dependent children" | src:953 | encoded | `cp3-part2-interpretation.l4`: `s 42(1) — a survivor with dependent children` | survivor who wholly or substantially maintains at least one dependent child |
| s 42(1) "wholly or substantially" | src:954 | encoded | input of `s 42(1) — a survivor with dependent children` | meaning left to regulations (regulation 65, cr2): the input counts the children the survivor maintains in that sense |
| s 42(2)(a) (marginal note When person deemed disabled) | src:955-959 | fork | `cp3-part2-interpretation.l4`: `s 42(2)(a)(i) — a disability is severe`, `s 42(2)(a)(ii) — a disability is prolonged`, `s 42(2)(a) — a person is considered to be disabled` | the determination "in prescribed manner" is a judgment left to the Minister, taken as a conditional input; "only if" is read as the whole test (fork F24) |
| s 42(2)(b) | src:960 | fork | `cp3-part2-interpretation.l4`: `s 42(2)(b) — the time a person is deemed to have become disabled`, `s 42(2)(b) — the time a person is deemed to have ceased to be disabled` | not earlier than fifteen months before the application (fork F2); the limit is on becoming disabled only, not on ceasing (finding 2) |
| Group heading: Pension Index | src:962 | inert | none | a pure title (the heading "Pension Index") over section 43; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 43(1) | src:963-964 | fork | `cp3-part2-interpretation.l4`: `s 43(1) — the Pension Index for a year before the exception` | average of twelve monthly figures; the rounding of regulation 75 (cr2) is not done here (fork F3) |
| s 43(2) | src:965-966 | encoded | `cp3-part2-interpretation.l4`: `s 43(2) — the Pension Index for a year` | never below last year's index |
| s 43(3) | src:967-968 | encoded | `cp3-part2-interpretation.l4`: `s 43(3) — a value of the Pension Index after the Consumer Price Index is rebased` | the same percentage adjustment of every existing value |
| Group heading: DIVISION A Benefits Payable | src:970 | inert | none | a pure title (the heading "DIVISION A Benefits Payable") over sections 44 to 44.2; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 44(1) chapeau (marginal note Benefits payable) | src:971-972 | encoded | `cp3-benefits-payable.l4` (the eight rules below) | "Subject to this Part": the rules decide the conditions of subsection (1) only; the other conditions of Part II (application, payment) are other provisions and other pieces |
| s 44(1)(a) | src:973 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(a) — a retirement pension is payable to a contributor who has reached sixty years of age` | age 60 through section 2(2) |
| s 44(1)(b) chapeau | src:974 | fork | `cp3-benefits-payable.l4`: `s 44(1)(b) — a disability pension is payable to a contributor who is disabled` | under 65, no retirement pension payable, disabled, and one of the three limbs (alternatives: fork F12) |
| s 44(1)(b)(i) | src:975 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(b) — a disability pension is payable to a contributor who is disabled` | the minimum qualifying period is the input fed by `s 44(2)(a)` (cp3-minimum-qualifying-period.l4) |
| s 44(1)(b)(ii) | src:976 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(b) — a disability pension is payable to a contributor who is disabled` | a counterfactual ("would have been payable if an application had been received earlier"), supplied as a fact |
| s 44(1)(b)(iii) | src:977 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(b) — a disability pension is payable to a contributor who is disabled` | a counterfactual about a division under section 55 or 55.1, supplied as a fact |
| s 44(1)(b)(iv) | src:978 | repealed or blank in this text | none | [Repealed, 1997, c. 40, s. 69] |
| s 44(1)(c) | src:979 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(c) — a death benefit is payable to the estate or succession of a deceased contributor` | the right is the estate's or succession's |
| s 44(1)(d)(i) | src:980-986 | fork | `cp3-benefits-payable.l4`: `s 44(1)(d)(i) — a survivor's pension is payable before 2019`, `s 44(1)(d) — a survivor's pension is payable to the survivor of a deceased contributor` | what "before 2019" dates is not said: read as the time the pension would be paid (fork F15) |
| s 44(1)(d)(ii) | src:987 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(d)(ii) — a survivor's pension is payable after 2018` |  |
| s 44(1)(e) | src:988-992 | fork | `cp3-benefits-payable.l4`: `s 44(1)(e) — a disabled contributor's child's benefit is payable to a child of a disabled contributor` | limbs (i) to (iii) read as describing the disabled contributor, not the child (fork F16); limb (iv) is repealed |
| s 44(1)(f) | src:993 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(f) — an orphan's benefit is payable to an orphan of a deceased contributor` |  |
| s 44(1)(g) | src:994 | encoded | `cp3-benefits-payable.l4`: `s 44(1)(g) — a post-retirement benefit is payable to a beneficiary of a retirement pension` |  |
| s 44(1)(h) | src:995-998 | fork | `cp3-benefits-payable.l4`: `s 44(1)(h) — a post-retirement disability benefit is payable to a beneficiary of a retirement pension who is disabled` | "that period ends after 2018" read as the contributory period of subsection (5) (fork F17) |
| s 44(1.1) | src:999 | repealed or blank in this text | none | [Repealed, 2018, c. 12, s. 372] |
| s 44(2)(a) | src:1000-1005 | fork | `cp3-minimum-qualifying-period.l4`: `s 44(2)(a) — base contributions were made for a year on earnings not less than the basic exemption`, `s 44(2)(a)(i) — base contributions on earnings not less than the basic exemption for at least four of the last six calendar years`, `s 44(2)(a)(i) — at least four of the last six calendar years count, by number`, `s 44(2)(a)(i.1) — base contributions on earnings not less than the basic exemption for at least 25 calendar years, three of them in the last six`, `s 44(2)(a)(i.1) — at least 25 calendar years count, three of them among the last six, by number`, `s 44(2)(a)(ii) — base contributions on earnings not less than the basic exemption for each year after the month of cessation of the previous disability benefit`, `s 44(2)(a)(ii) — every calendar year since the previous disability benefit ceased counts, by number`, `s 44(2)(a) — deemed to have made base contributions for not less than the minimum qualifying period, for a disability pension` | limbs (i), (i.1), (ii) are alternatives (fork F12); "each year after the month of cessation" is read as each included year from the year of the cessation month on (fork F13) |
| s 44(2)(b) | src:1006-1011 | encoded | `cp3-minimum-qualifying-period.l4`: `s 44(2)(b) — a month is in the contributory period for the minimum qualifying period of a disability pension`, `s 44(2)(b)(i) — the first day of 1966, the earliest start of the contributory period`, `s 44(2)(b)(iv) — the first day of 1978, December 1977 having passed` | month-by-month test; paragraph (iv) says "less than" the basic exemption, section 49(d) says "equal to or less than" (finding 7) |
| s 44(2.1) | src:1012-1013 | encoded | `cp3-minimum-qualifying-period.l4`: `s 44(2.1) — the basic exemption for the year in which a late applicant would have been considered to have become disabled` |  |
| s 44(2.2) | src:1014-1020 | encoded | `cp3-minimum-qualifying-period.l4`: `s 44(2.2) — a late applicant is deemed to have made base contributions for not less than the minimum qualifying period` | the last condition is a counterfactual about the Act's other conditions, supplied as a fact |
| s 44(3) | src:1021-1024 | fork | `cp3-minimum-qualifying-period.l4`: `s 44(3)(a) — the calendar years in the total, leaving out the years after 65 in which the earnings do not exceed the basic exemption`, `s 44(3)(a) — base contributions were made for at least one third of the years, and for at least three years`, `s 44(3)(b) — base contributions were made for at least ten years`, `s 44(3) — deemed to have made base contributions for not less than the minimum qualifying period, for a death benefit, a survivor's pension and an orphan's benefit` | a year of contributions is one section 52(3)(a) deems (earnings exceed the exemption); reaching 65 is the actual birthday (paragraph 44(3)(a) is excepted from section 2(2)); "one third ... but in no case for less than three years" read as both (fork F14) |
| s 44(4) | src:1025-1029 | fork | `cp3-minimum-qualifying-period.l4`: `s 44(4)(a) — base contributions on earnings not less than the basic exemption for at least four of the last six calendar years`, `s 44(4)(a) — at least four of the last six calendar years count, by number`, `s 44(4)(b) — base contributions on earnings not less than the basic exemption for at least 25 calendar years, three of them in the last six`, `s 44(4)(b) — at least 25 calendar years count, three of them among the last six, by number`, `s 44(4)(c) — base contributions on earnings not less than the basic exemption for each year after the month of cessation of the previous disability pension or post-retirement disability benefit`, `s 44(4)(c) — every calendar year since the previous disability pension or post-retirement disability benefit ceased counts, by number`, `s 44(4) — deemed to have made base contributions for not less than the minimum qualifying period, for a post-retirement disability benefit` | same shapes as subsection (2)(a), limbs alternatives (fork F12); limb (a) has no "fewer than six years" clause and is read the same way |
| s 44(5) | src:1030-1036 | encoded | `cp3-minimum-qualifying-period.l4`: `s 44(5) — a month is in the contributory period for the minimum qualifying period of a post-retirement disability benefit` | no 1966 floor |
| s 44.1(1)(a) | src:1037-1039 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1(1)(a) — a survivor's pension is not payable to an individual convicted of killing the contributor` | the Minister's being informed and satisfied is a conditional input |
| s 44.1(1)(b) | src:1040 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1(1)(b) — a death benefit is not payable to an individual convicted of killing the contributor` |  |
| s 44.1(1)(c) | src:1041-1044 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1(1)(c) — an orphan's benefit is not payable to an individual convicted of killing the contributor` | adds an adult sentence and an age of 18 or more |
| s 44.1(2) | src:1045-1046 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1(2) — the individual's entitlement is reinstated and any amount recovered is repaid` |  |
| s 44.1(3) | src:1047-1048 | fork | `cp3-benefits-not-payable.l4`: `s 44.1 — a conviction that engages this section` (input: the Minister deems the conviction outside Canada) | a power of the Minister ("may deem"), read as the fact that the Minister has deemed (fork F27) |
| s 44.1(4) | src:1049-1050 | fork | `cp3-benefits-not-payable.l4`: `s 44.1(4) — the amount received that is a debt due to Her Majesty` | the debt is under section 66 (piece cp4); for an orphan's benefit the bar of subsection (1)(c) is read as applying (fork F18) |
| s 44.1(5) | src:1051-1052 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1(5) — this section applies to a conviction of which the Minister is informed at a given time` | no date of coming into force is given; the section is read as covering a conviction whatever time the Minister is informed (finding 9) |
| s 44.1(6) | src:1053-1054 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1 — a conviction that engages this section` (input about section 231 of the Criminal Code) | the Criminal Code is not among the inputs |
| s 44.1(7) | src:1055-1056 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1 — a conviction that engages this section` (input about manslaughter) | as (6) |
| s 44.1(8) | src:1057-1058 | encoded | `cp3-benefits-not-payable.l4`: `s 44.1 — a conviction that engages this section` (input about the probation order) |  |
| s 44.2 | src:1059-1060 | encoded | `cp3-benefits-not-payable.l4`: `s 44.2 — a survivor's pension is not payable to an individual after a division of earnings`, `s 44.2 — the first day of 2025, from which a division under paragraph 55.1(1)(b) bars a survivor's pension` | one year of continuous cohabitation counted by the core's calendar (forks F1, F7 of the keel); only a division under paragraph 55.1(1)(b) bars the pension (finding 10) |
| Group heading: DIVISION B Calculation of Benefits | src:1062 | inert | none | a pure title (the heading "DIVISION B Calculation of Benefits") over sections 45 to 55.2; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| Group heading: Basic Amount and Annual Adjustment | src:1064 | inert | none | a pure title (the heading "Basic Amount and Annual Adjustment") over section 45; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 45(1) | src:1065-1066 | encoded | `cp3-retirement-pension.l4`: `s 45(1) — the basic amount of a benefit` | the amount before the annual adjustment |
| s 45(2) | src:1067-1071 | encoded | `cp3-retirement-pension.l4`: `s 45(2) — the amount payable for a month in the following year after the annual adjustment`, `s 45(2) — the amount payable for a month in a later year after the annual adjustments` | "in prescribed manner" is regulation 62 (cr2); the Pension Index of each year is an input |
| Group heading: Retirement Pension | src:1073 | inert | none | a pure title (the heading "Retirement Pension") over sections 46 to 54.2; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 46(1) | src:1074-1078 | encoded | `cp3-retirement-pension.l4`: `s 46(1) — the basic monthly amount of a retirement pension` | 25% + 8.33% + 33.33% |
| s 46(2) | src:1079-1087 | encoded | `cp3-retirement-pension.l4`: `s 46(2) — the portion of a retirement pension under paragraph (1)(a) for a former disability pension recipient whose pension a division reduces` | weighted by months excluded for disability and months of the contributory period |
| s 46(3) | src:1088-1089 | encoded | `cp3-retirement-pension.l4`: `s 46(3) — the basic monthly amount of a retirement pension that becomes payable after 1986 and before 2011, adjusted by the Minister's factor`, `cp3 — the time interval between the commencement of a retirement pension and the month of reaching 65, in months, at most five years` | the Minister's factor is not among the inputs: a plain input; the interval is capped at five years |
| s 46(3.1) | src:1090-1091 | encoded | `cp3-retirement-pension.l4`: `s 46(3.1) — the basic monthly amount of a retirement pension that becomes payable after 2010, adjusted by the factor fixed under subsection (7)` | the factor is that of regulations 78.3 and 78.4 (cr2): a plain input |
| s 46(4) | src:1092-1102 | encoded | `cp3-retirement-pension.l4`: `s 46(4) — the adjustment factor applied after a division increases a retirement pension` | [(F1 x P1) + (F2 x E)] / P2 |
| s 46(5) | src:1103-1107 | fork | `cp3-retirement-pension.l4`: `s 46(5) — the basic monthly amount of a retirement pension when the factor is applied only to the amount left after a survivor's pension reduction` | the part taken off is read as paid at the basic amount (fork F11); an agreement under section 80 (cp5) is an input |
| s 46(6) | src:1108-1109 | encoded | `cp3-retirement-pension.l4`: `s 46(6) — the time interval, in months, on which the upward adjustment factor for an increase due to a division after age 65 is based` |  |
| s 46(7) | src:1110-1111 | inert | none | a power of the Governor in Council to make regulations fixing adjustment factors: regulation-making machinery; the factors it produced (regulations 78.3 and 78.4) are in regulations 78.3 and 78.4 (piece cr2's range) and enter here as the input of subsection (3.1) |
| s 46(8) | src:1112-1113 | inert | none | the conditions on that power (recommendation of the Minister of Finance, consent of two thirds of the included provinces): machinery for making regulations, which decides nothing for a person |
| s 46(9) | src:1114-1115 | inert | none | regulations under subsection (7) may be amended only under subsection 113.1(14): machinery for amending regulations |
| s 47 | src:1116-1117 | encoded | `cp3-average-earnings.l4`: `s 47 — the average monthly pensionable earnings of a contributor whose retirement pension commences before 1976` | total pensionable earnings over the basic number of contributory months; NOTHING when the pension commences in 1976 or later |
| s 48(1) | src:1118-1119 | encoded | `cp3-average-earnings.l4`: `s 48(1) — the average monthly pensionable earnings before the deductions` | the greater of the months of the period and the basic number is the divisor |
| s 48(2) | src:1120-1126 | fork | `cp3-average-earnings.l4`: `s 48(2)(a) — the number of months below which the deduction may not reduce the contributory period`, `s 48(2) — the months of the contributory period that remain after the deduction for child-raising years` | "may be deducted" read as made, lowest months first; "average calculated without regard to (3) and (4)" read as the subsection (1) average over all months (fork F6); "disability benefit" is read as the disability pension and the post-retirement disability benefit (fork F7); months of equal earnings: the earlier month goes first (fork F21) |
| s 48(3) | src:1127-1130 | fork | `cp3-average-earnings.l4`: `s 48(3) — the months of the contributory period that remain after the deduction for months after age 65` | the months deducted from the earnings are the months of least earnings wherever they fall; months of equal earnings: the earlier month goes first (fork F21) |
| s 48(4) | src:1131-1136 | fork | `cp3-average-earnings.l4`: `s 48(4)(a)(i) — the percentage of the months remaining that is deducted`, `s 48(4)(a) — the number of months deducted from the months remaining`, `s 48(4) — the months of the contributory period that remain after the deduction for months over 120` | 15, 16 and 17 per cent by the month the benefit commences; a fraction of a month counts as a month; months of equal earnings: the earlier month goes first (fork F21) |
| s 48(5) | src:1137-1138 | encoded | `cp3-average-earnings.l4`: the last input of `s 48(4)(a) — the number of months deducted from the months remaining` | the percentage already used for another benefit based on the amount is an input |
| s 48.1 | src:1139-1142 | encoded | `cp3-average-earnings.l4`: `s 48.1(a) — the first additional monthly pensionable earnings when the first additional contributory period is not more than 480 months`, `s 48.1(b) — the first additional monthly pensionable earnings when the first additional contributory period exceeds 480 months`, `s 48.1 — the first additional monthly pensionable earnings of a contributor` |  |
| s 48.2 | src:1143-1146 | encoded | `cp3-average-earnings.l4`: `s 48.2(a) — the second additional monthly pensionable earnings when the second additional contributory period is not more than 480 months`, `s 48.2(b) — the second additional monthly pensionable earnings when the second additional contributory period exceeds 480 months`, `s 48.2 — the second additional monthly pensionable earnings of a contributor` |  |
| s 49 chapeau, (a) and (b) | src:1147-1153 | encoded | `cp3-contributory-period.l4`: `s 49 — the first month of the contributory period`, `s 49(a) — the last month of the contributory period, for a benefit other than a disability pension that commences before the end of 1986`, `s 49(b) — the last month of the contributory period, for a benefit other than a disability pension or a post-retirement disability benefit that commences after the end of 1986`, `s 49 — the last month of the contributory period for a benefit` | NOTHING for a disability pension and for a post-retirement disability benefit after 1986: section 49 gives them no end (finding 6) |
| s 49 (c) and (d), the exclusions | src:1154-1156 | encoded | `cp3-contributory-period.l4`: `s 49(c), (d) — a month is excluded from the contributory period`, `s 49 — a month is in the contributory period`, `s 49 — the number of months in the contributory period` | paragraph (d) says "equal to or less than" the basic exemption, where sections 44(2)(b)(iv) and 44(5)(d) say "less than" (finding 7) |
| s 49.1 | src:1157-1161 | encoded | `cp3-contributory-period.l4`: `s 49.1 — the first month of the first additional contributory period`, `s 49.1 — the last month of the first additional contributory period` | no exclusions |
| s 49.2 | src:1162-1166 | encoded | `cp3-contributory-period.l4`: `s 49.2 — the first month of the second additional contributory period`, `s 49.2 — the last month of the second additional contributory period` | no exclusions |
| s 50 | src:1167-1168 | encoded | `cp3-contributory-period.l4`: `s 50 — the total pensionable earnings of a contributor` | the sum of the month-by-month earnings of section 51 |
| s 50.1 | src:1169-1170 | encoded | `cp3-contributory-period.l4`: `s 50.1 — the total first additional pensionable earnings of a contributor` |  |
| s 50.2 | src:1171-1172 | encoded | `cp3-contributory-period.l4`: `s 50.2 — the total second additional pensionable earnings of a contributor` |  |
| s 51(1) the formula A x B and A in cases (a) to (c) | src:1173-1186 | fork | `cp3-pensionable-earnings.l4`: `s 51(1)(a) — the pensionable earnings of a contributor for a month`, `s 51(1)(b) — A, the first additional earnings for a month`, `s 51(1)(b) — the first additional pensionable earnings of a contributor for a month`, `s 51(1)(c) — A, the second additional earnings for a month`, `s 51(1)(c) — the second additional pensionable earnings of a contributor for a month` | A for the base tier is the output of `s 52 — the earnings for which a base contribution is deemed to have been made for a month` (cp3-deemed-contributions.l4), passed as an input; the 60th birthday in B is the actual birthday (fork F23) |
| s 51(1) B in cases (a) and (b) | src:1187-1199 | encoded | `cp3-pensionable-earnings.l4`: `s 51(1) — B, the ratio applied to a month's earnings` | C, D, E, F, G are figures of other sections (the Maximum Pensionable Earnings Average, the Pension Index, the Year's Maximum Pensionable Earnings): plain inputs |
| s 51(1.1) | src:1200-1205 | encoded | `cp3-pensionable-earnings.l4`: `s 51(1.1) — the multiplier of the first additional pensionable earnings of a month in a year` | 0.15, 0.3, 0.5, 0.75 for 2019 to 2022 |
| s 51(2) | src:1206-1211 | encoded | `cp3-pensionable-earnings.l4`: `s 51(2) — the Year's Maximum Pensionable Earnings taken for a year before 1986` | greatest multiple of $100 in 25,800 x A/B; the two Statistics Canada averages are inputs |
| s 51(3) | src:1212-1213 | encoded | `cp3-pensionable-earnings.l4`: `s 51(3) — the words about 1.02 times the preceding year's Pension Index are read into the 1970 Act's calculation` | the 1970 Act is not among the inputs; NOTHING for a year the subsection does not reach (finding 5) |
| s 51.1(1) | src:1214-1254 | fork | `cp3-pensionable-earnings.l4`: `s 51.1(1) — the value determined for each month excluded from the contributory period by reason of disability` (arithmetic in `cp3 — the value determined from a disablement lookback`) | letters A to G are seven year-records; values determined earlier are inputs, not iterated (fork F5) |
| s 51.1(2) | src:1255-1260 | encoded | `cp3-pensionable-earnings.l4`: `s 51.1(2) — the Year's Maximum Pensionable Earnings replaced for the year in which the first additional contributory period begins` | the replacement is also made inside the formula from the record field |
| s 51.2(1) | src:1261-1301 | fork | `cp3-pensionable-earnings.l4`: `s 51.2(1) — the value determined for each month excluded from the contributory period by reason of disability, for the second additional contributory period` | same arithmetic as section 51.1(1); prior values are inputs, not iterated (fork F5) |
| s 51.2(2) | src:1302-1307 | encoded | `cp3-pensionable-earnings.l4`: `s 51.2(2) — the Year's Maximum Pensionable Earnings replaced for the year in which the second additional contributory period begins` |  |
| s 51.3 | src:1308-1309 | encoded | `cp3-pensionable-earnings.l4`: `s 51.3 — the time a contributor is deemed to have become disabled for sections 51.1 and 51.2` | no fifteen-month limit, despite paragraph 42(2)(b) |
| s 52(1) | src:1310-1314 | fork | `cp3-deemed-contributions.l4`: `s 52(1) — a month is one for which the base contribution is deemed to have been made`, `s 52(1) — the months of a year for which the base contribution is deemed to have been made`, `s 52(1) — the earnings for which the base contribution is deemed to have been made for each month of a year`, `s 52 — the earnings for which a base contribution is deemed to have been made for a month` | limbs (a) and (b) and the closing sentence; both paragraphs bearing on one year are cumulative, as they are joined by "and" (fork F4); a month outside the months the section deems gets zero earnings (fork F22) |
| s 52(2) | src:1315-1316 | encoded | `cp3-deemed-contributions.l4`: `s 52(2) — the earnings for which a base contribution is deemed to have been made for a month of a year with no base contribution` | zero, as the text says |
| s 52(3) | src:1317-1320 | encoded | `cp3-deemed-contributions.l4`: `s 52(3)(a) — a base contribution is deemed to have been made for a year`, `s 52(3)(b) — a base contribution is deemed to have been made for earnings for a month` | earnings must exceed the basic exemption; equal is not enough |
| s 52.1(1) | src:1321-1325 | fork | `cp3-deemed-contributions.l4`: `s 52.1(1) — a month is one for which the first additional contribution is deemed to have been made`, `s 52.1(1) — the months of a year for which the first additional contribution is deemed to have been made`, `s 52.1(1) — the earnings for which the first additional contribution is deemed to have been made for each month of a year`, `s 52.1 — the earnings for which a first additional contribution is deemed to have been made for a month` | no disability limbs (they are in sections 51.1 and 51.2); both paragraphs bearing on one year are cumulative (fork F4); a month outside the deemed set gets zero earnings (fork F22) |
| s 52.1(2) | src:1326-1327 | encoded | `cp3-deemed-contributions.l4`: `s 52.1(2) — the earnings for which a first additional contribution is deemed to have been made for a month of a year with no first additional contribution` | zero |
| s 52.1(3) | src:1328-1331 | encoded | `cp3-deemed-contributions.l4`: `s 52.1(3)(a) — a first additional contribution is deemed to have been made for a year`, `s 52.1(3)(b) — a first additional contribution is deemed to have been made for earnings for a month` | the test is against the basic exemption |
| s 52.2(1) | src:1332-1336 | fork | `cp3-deemed-contributions.l4`: `s 52.2(1) — a month is one for which the second additional contribution is deemed to have been made`, `s 52.2(1) — the months of a year for which the second additional contribution is deemed to have been made`, `s 52.2(1) — the earnings for which the second additional contribution is deemed to have been made for each month of a year`, `s 52.2 — the earnings for which a second additional contribution is deemed to have been made for a month` | whether a second additional contribution was made for the year is a plain input (no deeming test in the section: finding 4); both paragraphs bearing on one year are cumulative (fork F4); a month outside the deemed set gets zero earnings (fork F22) |
| s 52.2(2) | src:1337-1338 | encoded | `cp3-deemed-contributions.l4`: `s 52.2(2) — the earnings for which a second additional contribution is deemed to have been made for a month of a year with no second additional contribution` | zero |
| s 52.2(3) | src:1339-1340 | encoded | `cp3-deemed-contributions.l4`: `s 52.2(3) — a second additional contribution is deemed to have been made for earnings for a month` | only the month paragraph; no paragraph (a) (finding 4) |
| s 53(1) | src:1341-1355 | encoded | `cp3-unadjusted-earnings.l4`: `s 53(1) — the base unadjusted pensionable earnings of a contributor for a year` | least of three figures, zero if paragraph (a) does not exceed the basic exemption; section 12, 13, 15 figures and the rates are inputs; "the prescribed manner" is regulation 41(1) (cr2) |
| s 53(2) | src:1356-1359 | encoded | `cp3-unadjusted-earnings.l4`: `s 53(2)(a) — the contributor's basic exemption for the year in which a retirement pension becomes payable`, `s 53(2)(b) — the contributor's maximum pensionable earnings for the year in which a retirement pension becomes payable`, `cp3 — the months of a year before the retirement pension becomes payable that are not excluded` |  |
| s 53.1(1) | src:1360-1374 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.1(1) — the first additional unadjusted pensionable earnings of a contributor for a year` | from 2019 (the section's own words); the rule does not itself refuse a year before 2019 |
| s 53.1(2) | src:1375-1378 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.1(2)(a) — the contributor's basic exemption for the year in which a retirement pension becomes payable, for first additional earnings`, `s 53.1(2)(b) — the contributor's maximum pensionable earnings for the year in which a retirement pension becomes payable, for first additional earnings` | no month is left out for disability |
| s 53.2(1) | src:1379-1390 | fork | `cp3-unadjusted-earnings.l4`: `s 53.2(1) — the second additional unadjusted pensionable earnings of a contributor for a year` | from 2024; "the amount by which ... exceeds" is zero when the earnings do not reach the maximum (fork F8) |
| s 53.2(2) | src:1391-1394 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.2(2)(a) — the contributor's maximum pensionable earnings for the year in which a retirement pension becomes payable, for second additional earnings`, `s 53.2(2)(b) — the contributor's additional maximum pensionable earnings for the year in which a retirement pension becomes payable` |  |
| s 53.3(1) | src:1395-1427 | fork | `cp3-unadjusted-earnings.l4`: `s 53.3(1) — the amount attributed to a family allowance recipient for a year, first additional contributory period, for one child` | letters A to F and M1 to M6 as in the text; F(a) taken as written, though it sets an amount beside ratios (fork F9) |
| s 53.3(2) | src:1428-1429 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.3(2) — the amount attributed to a family allowance recipient for more than one child, first additional contributory period` | the greater of the amounts per child |
| s 53.3(3) | src:1430-1431 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.3(3) — the contributor's basic exemption for the year in which a retirement pension becomes payable, for the attribution` |  |
| s 53.3(4) | src:1432-1433 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.3(4) — the amount attributed for a year in which the first additional contributory period begins or ends` |  |
| s 53.3(5) | src:1434-1439 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.3(5) — the Year's Maximum Pensionable Earnings replaced for the year in which the first additional contributory period begins` | also made inside subsection (1) from the lookback record |
| s 53.4(1) | src:1440-1468 | fork | `cp3-unadjusted-earnings.l4`: `s 53.4(1) — the amount attributed to a family allowance recipient for a year, second additional contributory period, for one child` | no 0.4 filler and no basic exemption test; F(a) as written, an amount among ratios (fork F9) |
| s 53.4(2) | src:1469-1470 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.4(2) — the amount attributed to a family allowance recipient for more than one child, second additional contributory period` |  |
| s 53.4(3) | src:1471-1472 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.4(3) — the amount attributed for a year in which the second additional contributory period begins or ends` |  |
| s 53.4(4) | src:1473-1484 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.4(4)(a) — the Year's Maximum Pensionable Earnings replaced for the year in which the second additional contributory period begins`, `s 53.4(4)(b) — the Year's Additional Maximum Pensionable Earnings replaced for the year in which the second additional contributory period begins` |  |
| s 53.5 | src:1485-1486 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.5 — the first additional unadjusted pensionable earnings of a contributor for a year of attribution` |  |
| s 53.6 | src:1487-1488 | encoded | `cp3-unadjusted-earnings.l4`: `s 53.6 — the second additional unadjusted pensionable earnings of a contributor for a year of attribution` |  |
| s 54 | src:1489-1490 | fork | `cp3-unadjusted-earnings.l4`: `s 54 — the base unadjusted pensionable earnings of a contributor for a year of division` | the adjustment itself is in sections 55(4), (5) and 55.2(5), (5.1) (this piece) and 55.2(6), (6.1) (piece cp4): a division under the Act alone is read as replacing the amount (fork F10) |
| s 54.1 | src:1491-1492 | fork | `cp3-unadjusted-earnings.l4`: `s 54.1 — the first additional unadjusted pensionable earnings of a contributor for a year of division` | as section 54; a division under the Act alone replaces the amount (fork F10) |
| s 54.2 | src:1493-1494 | fork | `cp3-unadjusted-earnings.l4`: `s 54.2 — the second additional unadjusted pensionable earnings of a contributor for a year of division` | as section 54; a division under the Act alone replaces the amount (fork F10) |
| Group heading: Division of Unadjusted Pensionable Earnings for Divorces and Annulments before the Coming into Force of section 55.1 | src:1496 | inert | none | a pure title (the heading "Division of Unadjusted Pensionable Earnings for Divorces and Annulments before the Coming into Force of section 55.1") over section 55; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 55(1) | src:1497-1498 | fork | `cp3-division.l4`: `s 55(1) — an application for a division of the unadjusted pensionable earnings of former spouses may be made`, `s 55(1) — the first day of 1978, the earliest judgment`, `s 55(1) — the first day of 1987, the end of the judgments` | 36 months or, if both agree in writing, at any time; the "subject to" sections (55.2(2) to (4) and 55.3) qualify it; no application before the judgment (fork F25) |
| s 55(2) | src:1499-1503 | fork | `cp3-division.l4`: `s 55(2)(a) — the former spouses cohabited for at least thirty-six consecutive months during the marriage`, `s 55(2)(b) — the day on which the marriage is deemed solemnized or nullified or a divorce is deemed made final`, `s 55(2)(c) — the former spouses are deemed to have cohabited during a year` | paragraphs (b) and (c) are read with actual years in (c) (fork F20); the thirty-six months are months of actual cohabitation, "notwithstanding" paragraphs (b) and (c) (finding 3) |
| s 55(3) | src:1504-1505 | encoded | `cp3-division.l4`: `s 55(3) — the months considered in determining the period for which the earnings are divided` | months of cohabitation "determined in the prescribed manner" (regulation 78, cr2): an input |
| s 55(4) | src:1506-1507 | encoded | `cp3-division.l4`: `s 55(4) — the unadjusted pensionable earnings attributed to each former spouse on a division` | added and divided equally; the earnings attributable to contributions are worked out "as in section 78" (cp5): an input |
| s 55(5) | src:1508-1509 | encoded | `cp3-division.l4`: `s 55(5) — the total unadjusted pensionable earnings of a contributor for a year of division under this Act and a provincial pension plan` |  |
| s 55(6) | src:1510-1515 | encoded | `cp3-division.l4`: `s 55(6) — a division is made for a month of the period of cohabitation` | four bars, paragraphs (a) to (d) |
| s 55(7) | src:1516-1517 | encoded | `cp3-division.l4`: `s 55(7) — the month from which the benefit adjusted for the division is paid` | the month after the application is received |
| s 55(8) | src:1518-1519 | encoded | `cp3-division.l4`: `s 55(8) — the applicant and the former spouse or the former spouse's estate must be notified of the approval`, `s 55(8) — an applicant or a former spouse who is dissatisfied with the division has the right of appeal` | the manner of notice is by regulation (regulation 46, cr2); the appeal is Part II's later Division (cp5) |
| s 55(9) | src:1520-1521 | inert | none | a power of the Governor in Council to make regulations prescribing the time, manner and form of making or withdrawing applications for a division, the procedures for dealing with and approving them, and the information and evidence to be furnished: regulation-making machinery that decides nothing for the person |
| Group heading: Division of Unadjusted Pensionable Earnings | src:1523 | inert | none | a pure title (the heading "Division of Unadjusted Pensionable Earnings") over sections 55.1 to 55.3; it states no right, duty, condition or figure, and the provisions it heads have their own rows |
| s 55.1(1) | src:1524-1532 | fork | `cp3-division.l4`: `s 55.1(1)(a) — a division takes place on a judgment granting a divorce or of nullity of the marriage`, `s 55.1(1)(b) — a division takes place on the approval of an application by spouses living separate and apart`, `s 55.1(1)(c) — a division takes place on the approval of an application by former common-law partners living separate and apart`, `s 55.1 — a division of unadjusted pensionable earnings takes place` | the three-year limit of paragraph (b)(ii) is only for a death (fork F19) |
| s 55.1(2) | src:1533-1538 | encoded | `cp3-division.l4`: `s 55.1(2)(a) — the persons are deemed to have lived separate and apart for a period`, `s 55.1(2)(b) — a period of living separate and apart is not considered to have been interrupted or terminated` | the Minister's being satisfied is a conditional input |
| s 55.1(3) | src:1539-1540 | encoded | `cp3-division.l4`: `s 55.1(3) — the persons subject to a division cohabited for a continuous period of at least one year` | "determined in a manner prescribed by regulation" (regulation 78.1, cr2): an input |
| s 55.1(4) | src:1541-1542 | encoded | `cp3-division.l4`: `s 55.1(4) — the months considered in determining the period for which the earnings are divided` |  |
| s 55.1(5) | src:1543-1546 | encoded | `cp3-division.l4`: `s 55.1(5) — the Minister may refuse to make or may cancel a division` | whether the Minister is "satisfied" is a conditional input; a power of the Minister, which is a liability of the persons |
| s 55.11 | src:1547-1551 | fork | `cp3-division.l4`: `s 55.11 — section 55.1 applies to the case` | the day the section came into force is a stated input; a separation beginning on that day is reached by neither (b) nor (c) (finding 8); "spouse" in the sense before the coming into force is an input (fork F26); the text gives no date for the coming into force (finding 9) |
| s 55.2(1) | src:1552 | repealed or blank in this text | none | [Repealed, 2000, c. 12, s. 48] |
| s 55.2(2) | src:1553-1554 | encoded | `cp3-division.l4`: `s 55.2(2) — an agreement or court order does not bind the Minister in a division` |  |
| s 55.2(3) | src:1555-1563 | encoded | `cp3-division.l4`: `s 55.2(3) — a provision of an agreement is binding on the Minister and the Minister shall not make a division` | paragraphs (a) to (d) cumulative ("and") |
| s 55.2(4) | src:1564-1565 | encoded | `cp3-division.l4`: `s 55.2(4) — each person subject to the division must be notified without delay` | the manner is "prescribed" (regulation 46, cr2) |
| s 55.2(5) | src:1566-1567 | encoded | `cp3-division.l4`: `s 55.2(5) — the base unadjusted pensionable earnings attributed to each person on a division under section 55.1` |  |
| s 55.2(5.1) | src:1568-1569 | encoded | `cp3-division.l4`: `s 55.2(5.1) — the first additional unadjusted pensionable earnings attributed to each person on a division under section 55.1` | subsection (5.2) onward is piece cp4 |

Counts: 150 rows; `encoded` 99, `fork` 33, `inert` 14, `repealed or blank in this text` 4.

## Fork register

Ids F1 to F27 are the ids the coverage table's notes cite.
Each row gives the readings seen, the one taken, and the text that licenses it.
"Where" names the rule (module `cp3-<name>.l4`).
A reading marked "assumed, not ruled" is a design choice of this piece and can be reverted alone.
Where I looked: every provision of the range was read for the date at which a condition is tested, for "and"/"or" between limbs, for overlaps between two rules, and for deferrals to things not among the inputs; the forks below are what that turned up.
Decisions that are not forks (a judgment of the Minister is an input; a counterfactual such as "a disability pension would have been payable if an application had been received earlier" is an input) are in the Seat section and the coverage table.

| id | provision | the readings seen | the reading taken | the text that licenses it | where |
| --- | --- | --- | --- | --- | --- |
| F1 | 42(1) "survivor" (lines 950-952) | (A) the married person and the common-law partner are both survivors; (B) the married person is a survivor only if no one was the common-law partner at the death | B | "(a) if there is no person described in paragraph (b), a person who was married to the contributor at the time of the contributor's death" | part2-interpretation: `s 42(1) — a survivor of a deceased contributor` |
| F2 | 42(2)(b) (line 960) | (A) fifteen months back from the day the application was made; (B) from the month of the application | A, with the core's calendar (a day that does not exist is clamped to the month's last day) | "no case ... earlier than fifteen months before the time of the making of any application" | part2-interpretation: `s 42(2)(b) — the time a person is deemed to have become disabled` |
| F3 | 43(1) (lines 963-964) | (A) the average of the twelve figures unrounded; (B) rounded to one decimal place as regulation 75 says | A: regulation 75 belongs to piece cr2; assumed, not ruled | the Act's own words give no rounding; regulation 75(1) and (2) round to one decimal place | part2-interpretation: `s 43(1) — the Pension Index for a year before the exception` |
| F4 | 52(1) (lines 1311-1314) | when paragraphs (a) and (b) both bear on one year (a year in which a disability pension ceases and a retirement pension becomes payable): (A) a month must satisfy every limb that applies; (B) the later paragraph prevails | A | the paragraphs are joined by "and" ("..., and" at the end of (a)) | deemed-contributions: `s 52(1) — a month is one for which the base contribution is deemed to have been made` (also 52.1(1), 52.2(1)) |
| F5 | 51.1(1) and 51.2(1) (lines 1214-1254, 1261-1301) | (A) "the greater of a ratio and any value already determined for a month of that year" is iterated month by month by the encoding; (B) the earlier values are inputs | B: each year of the lookback carries the values already determined for its months | the formula needs a value determined for each earlier month; the section does not give the order | pensionable-earnings: `s 51.1(1) — the value determined for each month excluded from the contributory period by reason of disability`, `s 51.2(1) — ...` |
| F6 | 48(2) (lines 1120-1126) | "there may be deducted": (A) the deduction is made; (B) it is optional. Which months go when the floor stops the deduction: (A) lowest earnings first; (B) latest first. "the average ... calculated without regard to subsections (3) and (4)": (A) the subsection (1) average over all months before any deduction; (B) the average after the deduction of subsection (2) itself | A, A, A (all assumed, not ruled) | the text names the months deducted ("those months during which he was a family allowance recipient and during which his pensionable earnings were less than his average monthly pensionable earnings") and gives no order when the floor stops the deduction; a deduction of months below the average can only raise the average; reading (B) of the third would make the average depend on itself | average-earnings: `s 48(2) — the months of the contributory period that remain after the deduction for child-raising years` |
| F7 | 48(2)(a)(i), (i.1) (lines 1123-1124) | "a disability benefit in respect of a contributor who is deemed to have become disabled": (A) a disability pension and a post-retirement disability benefit; (B) also a disabled contributor's child's benefit, which is paid in respect of a disabled contributor | A (assumed, not ruled) | "disability benefit" is not defined in section 42(1); subsection 44(1) names the three as "disability pension", "post-retirement disability benefit" and "disabled contributor's child's benefit" | average-earnings: `s 48(2)(a) — the number of months below which the deduction may not reduce the contributory period` |
| F8 | 53.2(1) (lines 1379-1390) | "the amount by which ... exceeds": (A) zero when the earnings do not reach the maximum; (B) not covered | A | the amount is an excess; no excess is zero | unadjusted-earnings: `s 53.2(1) — the second additional unadjusted pensionable earnings of a contributor for a year` |
| F9 | 53.3(1) and 53.4(1), F(a) (lines 1395-1427, 1440-1468) | F is "that amount previously attributed" beside ratios A to E: (A) encoded as written, an amount among ratios; (B) read as a ratio | A | the text lists F(a) among the letters without saying it is a ratio | unadjusted-earnings: `s 53.3(1) — ...`, `s 53.4(1) — ...` |
| F10 | 54 (lines 1489-1494) | (A) a division under the Act alone gives the amount attributed in place of the section 53 amount, and a division under the Act and under a provincial plan gives the aggregate of the two attributed amounts (section 55(5)); (B) the attributed amount is added to the section 53 amount; (C) a division under a provincial plan alone also changes the amount | A; a division under a provincial plan alone does not change the amount under this Act | "is to be adjusted for each year in which there is a division ... under section 55 or 55.1 and under a provincial pension plan"; section 55(5) aggregates the two for benefits under this Act | unadjusted-earnings: `s 54 — the base unadjusted pensionable earnings of a contributor for a year of division` (and 54.1, 54.2) |
| F11 | 46(5) (lines 1103-1107) | the factor "shall be applied ... only to the amount remaining": the part taken off is (A) paid at the basic amount; (B) not paid; (C) not said | A: (basic amount − X) × factor + X, with X the reduction carried by the Pension Index ratio | "any downward adjustment factor ... shall not be applied to the whole" | retirement-pension: `s 46(5) — ...` |
| F12 | 44(1)(b), 44(2)(a), 44(4) | the limbs: (A) alternatives; (B) cumulative | A | the limbs of (1)(b) end "(ii) ..., or (iii)"; of (2)(a) "(i) ... or ... (i.1) ... or (ii)"; of (4) "(b) ...; or (c)" | benefits-payable and minimum-qualifying-period |
| F13 | 44(2)(a)(ii), 44(4)(c) (lines 1005, 1029) | "each year after the month of cessation": (A) each included year from the year of the cessation month on; (B) each year after the cessation month's year | A, assumed, not ruled | the year of the cessation month is partly after the month | minimum-qualifying-period: `s 44(2)(a)(ii) — ...`, `s 44(4)(c) — ...` |
| F14 | 44(3)(a) (line 1023) | "at least one third ... but in no case for less than three years": (A) both a third and three years; (B) a third, or three years | A | "in no case" | minimum-qualifying-period: `s 44(3)(a) — base contributions were made for at least one third of the years, and for at least three years` |
| F15 | 44(1)(d)(i), (ii) (lines 981, 987) | "before 2019" and "after 2018" date what: (A) the time the pension would be paid; (B) the death; (C) the application | A, assumed, not ruled | "a survivor's pension shall be paid (i) before 2019, ..." | benefits-payable: `s 44(1)(d) — a survivor's pension is payable to the survivor of a deceased contributor` |
| F16 | 44(1)(e)(i) to (iii) (lines 989-991) | "each child of a disabled contributor who (i) has made base contributions ..." : (A) the limbs describe the disabled contributor; (B) the child | A: a child does not contribute | the limbs are the contributor's (a "contributor to whom a disability pension would have been payable") | benefits-payable: `s 44(1)(e) — ...` |
| F17 | 44(1)(h)(i) (line 996) | "that period ends after 2018": (A) the contributory period of subsection (5), which ends with the month of deemed disablement; (B) the minimum qualifying period as a span of years | A | subsection (5) defines the contributory period for subsection (4) | benefits-payable: `s 44(1)(h) — ...` |
| F18 | 44.1(4) (lines 1049-1050) | "in respect of whom the Minister is subsequently informed and satisfied that the individual has been convicted": for an orphan's benefit (A) the conditions of (1)(c) (adult sentence, 18 or older) also apply; (B) the conviction alone | A | "a pension or benefit referred to in this section" | benefits-not-payable: `s 44.1(4) — the amount received that is a debt due to Her Majesty` |
| F19 | 55.1(1)(b)(ii) (line 1529) | the three-year limit: (A) only when one spouse has died; (B) always | A | "in the event of the death of one of the spouses ..., the application is made within three years after the death" | division: `s 55.1(1)(b) — ...` |
| F20 | 55(2)(b), (c) (lines 1502-1503) | the years in (c): (A) the actual years of the marriage and of the divorce; (B) the years of the deemed dates of (b) | A | (c) speaks of "the year in which the marriage was solemnized" and "the year of divorce"; (b) deems a date "for the purposes of this section" | division: `s 55(2)(c) — the former spouses are deemed to have cohabited during a year` |
| F21 | 48(2), (3), (4) | months of equal earnings: (A) the earlier month goes first; (B) the later | A | no rule in the text | average-earnings: `cp3 — put a month into a list in order of earnings` |
| F22 | 52(1) to 52.2(1) | a month outside the months the section deems (before the 18th birthday, after the 70th, etc.) in a year of contribution: (A) deemed earnings are zero; (B) not covered | A | subsection (2) of each section gives zero where no contribution was made; none says what a month outside the deemed set has | deemed-contributions: `s 52(1) — the earnings for which the base contribution is deemed to have been made for each month of a year` |
| F23 | 51(1) B(a) (line 1188) | "after the contributor's 60th birthday, a month ... excluded": (A) the actual birthday, a month later than the month containing it; (B) the date section 2(2) deems for reaching 60 | A | the text says "birthday", not "reaches 60" (section 2(2) is about reaching an age) | pensionable-earnings: `s 51(1) — B, the ratio applied to a month's earnings` |
| F24 | 42(2)(a) (lines 957-959) | "only if": (A) the three conditions together are enough; (B) they are necessary and nothing says they suffice | A | the usual way to read a definition built of "only if" conditions that are the whole test | part2-interpretation: `s 42(2)(a) — a person is considered to be disabled` |
| F25 | 55(1) (line 1498) | "within 36 months or, if both former spouses agree in writing, at any time after the date of a judgment": (A) no application before the judgment; (B) any time before as well | A; the 36 months are counted from the judgment day by the core's calendar | "after the date of a judgment" | division: `s 55(1) — an application for a division ... may be made` |
| F26 | 55.11(b) (line 1550) | "spouse" in the sense it had immediately before the coming into force of the section: the repealed definition is not in the text, so (A) an input; (B) the present definition | A | the text points at a definition that is no longer there | division: `s 55.11 — section 55.1 applies to the case` |
| F27 | 44.1(3) (line 1048) | "the Minister may deem that conviction to be a conviction of first or second degree murder or manslaughter": (A) the fact that the Minister has deemed it; (B) the Minister's choice is made for the individual | A: an input, supplied conditionally | the Commons ruling of 2026-10-18 on a judgment handed to someone else | benefits-not-payable: `s 44.1 — a conviction that engages this section` |

Two of the keel's forks are used: F1 of the keel (a date that does not exist is clamped to the last day of the month) and F7 of the keel (a continuous year is complete on the same calendar day a year later), for subsections 42(2)(b), 55(1), 55.1(1)(b), (c) and section 44.2.

## Cross-references out of my ranges

Each row is a dependency on something outside lines 921-1569 of the Act.
The piece is read from the table of pieces and `inputs/SECTION-INDEX.txt`; "other" means another statute that is not among the inputs, and "not deposited" means an instrument the brief does not provide.
Each input is a plain input of the right type, named for the fact, and carries an `-- out of range:` comment in the module.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| 42(1) "child of a contributor" | regulation 65.1 (maintaining the child) | cr2 | a yes-or-no input of `s 42(1) — a child of a contributor` |
| 42(1) "child of a contributor", "parenting time", "decision-making responsibility" | subsection 2(1) of the Divorce Act | other | yes-or-no inputs of `s 42(1) — a child of a contributor` and `s 42(1) — time that is a person's parenting time` |
| 42(1) "dependent child of a contributor" | regulation 66 (attendance at a school or university) | cr2 | two yes-or-no inputs of `s 42(1) — the kind of dependent child that a child of a contributor is` |
| 42(1) "family allowance recipient" | the Family Allowances Act; regulation 77 | other; cr2 | two yes-or-no inputs of `s 42(1) — a family allowance recipient` |
| 42(1) "Maximum Pensionable Earnings Average" | section 18 (the Year's Maximum Pensionable Earnings) | cp1 | the list of `cp3 Maximum pensionable earnings of a year` |
| 42(1) "substantially gainful" | regulation 68.1 | cr2 | a yes-or-no input of `s 42(1) — an occupation is substantially gainful` |
| 42(1) "survivor with dependent children" | regulation 65 (wholly or substantially) | cr2 | a count of the children the survivor maintains |
| 42(2)(a), (b) | the prescribed manner of determining a disability and its date (Part V of the Regulations) | cr2 | the Minister's determination and the time determined, as inputs |
| 43(1) | the Consumer Price Index (Statistics Canada); regulation 75 (rounding to one decimal place) | other; cr2 | the twelve monthly figures as a list; no rounding (fork F3) |
| 44(1)(a) to (h) "shall be paid" | Division C, application for and payment of benefits | cp4 | none: this piece decides entitlement under subsection 44(1) only |
| 44(1)(c); 44.1(1)(b) | section 71 (payment of a death benefit) | cp5 | none: the death benefit is the estate's or succession's under 44(1)(c); 44.1(1)(b) asks of the individual entitled |
| 44(2)(a), (2.2), (4) | subsection 20(2) (the basic exemption "calculated without regard to subsection 20(2)") | cp1 | the basic exemption as a number |
| 44(2.1) | section 20 (the Year's Basic Exemption) | cp1 | the Year's Basic Exemption as a number |
| 44(3), 49(d), 52(3), 53 | sections 19 and 20 (the basic exemption of a person for a year) | cp1 | the basic exemption as a number |
| 44.1(4) | section 66 (a debt due to Her Majesty) | cp4 | none: only the amount is decided |
| 44.1(6), (7), (8) | sections 231 and 731(1)(a) of the Criminal Code | other | yes-or-no inputs of `s 44.1 — a conviction that engages this section` |
| 45(2) | regulation 62 (the "prescribed manner" of the annual adjustment, rounding to the cent) | cr2 | none: the product is not rounded |
| 46(3) | the factor fixed by the Minister on the advice of the Chief Actuary | other | the factor as a number |
| 46(3.1), 46(4), 46(5) | regulations 78.3 and 78.4 (the factor fixed under subsection (7)) | cr2 | the factor as a number |
| 46(5) | subsection 58(2) (reduction of the survivor's pension); section 80 (an agreement that provides otherwise) | cp4; cp5 | two yes-or-no inputs of `s 46(5) — ...` |
| 46(7) to (9) | the Governor in Council's power to fix the factor by regulation; the consent of the provinces | (in my range, inert) | none |
| 48(2) "family allowance recipient" | section 42(1) and regulation 77 | (in my range); cr2 | a yes-or-no field of `cp3 Month of a contributory period` |
| 49(c) | provincial pension plans (a month excluded by reason of disability under such a plan) | other | a yes-or-no input of `s 49(c), (d) — a month is excluded from the contributory period` |
| 51(1) | section 18 (the Year's Maximum Pensionable Earnings); the Pension Index (section 43, in my range) | cp1 | the year's figures as numbers |
| 51(2) | the average weekly wages and salaries of the Industrial Composite in Canada (Statistics Canada) | other | the averages as numbers |
| 51(3) | paragraph 43.1(2)(a) of the Canada Pension Plan, R.S.C. 1970, c. C-5 | not deposited | none: NOTHING for a year not before 1974 (finding 5) |
| 51.1, 51.2 | sections 18 and 18.1 | cp1 | the Year's Maximum and Additional Maximum Pensionable Earnings of each year of the lookback |
| 53(1), 53.1(1), 53.2(1) | sections 8 to 10, 12, 13, 15, 15.1, 15.2, 18, 18.1, 19 and 20 and the contribution rates of section 11.1 | cp1 | the contributory salary and wages, self-employed earnings, contributions, rate, exemption and maxima as numbers |
| 53(1)(b)(ii) | regulation 41 (the salary and wages on which a contribution was made under a provincial pension plan) | cr2 | the provincial amount as a number |
| 53(1), 53.1(1), 53.2(1) | section 10 (an individual who is to contribute on self-employed earnings) | cp1 | a yes-or-no input |
| 53.3, 53.4 | the Family Allowances Act; regulation 77 | other; cr2 | the lookback years and the year the contributor became a family allowance recipient |
| 55(1), 55.1(1) | section 55.3 (to which the provisions are "subject") | cp4 | none |
| 55(3), 55.1(4) | regulations 78 and 78.1(1) (months of cohabitation) | cr2 | the months of cohabitation as a list of months |
| 55(4), 55.2(5), 55.2(5.1) | sections 78 and 78.1 (the earnings for the period of cohabitation attributable to contributions) | cp5 | the earnings as numbers |
| 55(8) | the manner of notice "prescribed by regulation"; the right of appeal "as set out in this Part" (reconsiderations and appeals) | cr2; cp5 | none beyond a yes-or-no for dissatisfaction |
| 55.1(3) | regulation 78.1(2) (a continuous period of at least one year) | cr2 | a yes-or-no input |
| 55.2(4) | regulation 46 (notification) | cr2 | none |
| 55.2(5.2) onward | the division totals and the rest of Division B | cp4 | none: outside my range |
| 55.1(1)(b)(i) "living separate and apart" | subsection 55.1(2) (in my range) | (in my range) | n/a |
| 2(1) and 2(2) definitions used throughout | section 2 | cp-g0 (the core) | none: the core's rules are called (`cpp-core-definitions.l4`, `cpp-core-age.l4`) |

## Needs from the core

Nothing is blocked on the core: every shared term this piece needed is in `cpp-core*.l4`, and the core's rules were called, not restated (section 2(2) through `s 2(2) — the date a person is deemed to reach a specified age`, "contributor", "common-law partner", "Kind of benefit").

Local definitions the lead might promote if another piece defines the same thing under another name (not checked: the pieces cannot see one another):

- `cp3 Life events of a contributor` (date of birth, day died, month the retirement pension becomes payable, month a disability pension ceased, months excluded by reason of disability), in `cp3-nouns.l4`: the record that sections 49 to 53 and 55 all read.
- `cp3 Month of a contributory period`, `cp3 Year in a contributory period`, `cp3 Kind of dependent child`, `cp3 Maximum pensionable earnings of a year`, and the two lookback records, in `cp3-nouns.l4`.
- `cp3 — the later of two dates`, `cp3 — the earlier of two dates` and `cp3 — the number of months from one month to another, both included`, in `cp3-contributory-period.l4`: `max` and `min` on this binary take numbers only (see the stable-binary section), so a date needs its own.

No fixed figure that belongs in the core was found in this range.

## What the text turns out to say

Numbered findings: places where the text says something a reader would not expect, or says nothing.
Each ends "Asserted." where a case in a `cp3-tests-*.l4` file or in `cp3-cases-seat.l4` asserts it.

1. The "basic number of contributory months" of section 42(1) is 120 less the months excluded by reason of disability, and the text sets no floor: 130 excluded months give −10. Asserted (`cp3-tests-interpretation.l4`, `cp3-cases-seat.l4`).
2. The fifteen-month limit of paragraph 42(2)(b) is put on a person's being deemed to have become disabled only; a person is deemed to have ceased to be disabled at the time determined, with no limit. Asserted (`cp3-tests-interpretation.l4`).
3. Paragraph 55(2)(a) opens "notwithstanding paragraphs (b) and (c)": the thirty-six consecutive months must be months of cohabitation, not months made up by the deeming of (b) and (c). Asserted for the threshold (36 suffices, 35 does not; `cp3-tests-division.l4`, `cp3-cases-seat.l4`); that the months are actual months is carried by the name of the input and has no case.
4. Subsection 52.2(3) has only the month paragraph; unlike subsections 52(3) and 52.1(3) it has no paragraph (a) deeming a contribution for a year from earnings above the basic exemption. Whether a second additional contribution was made for a year is therefore a plain input of `s 52.2(1)`. Asserted for the month paragraph (`cp3-tests-deemed-contributions.l4`); the absence of a paragraph (a) is the text's and has no case.
5. Subsection 51(3) reads the 1970 Act's paragraph 43.1(2)(a) without the words "or 1.02 times the Pension Index for the preceding year" for a year before 1974, and says nothing for any other year; the 1970 Act is not among the inputs. The rule answers `JUST FALSE` (the words are not read) for a year before 1974 and `NOTHING` for any other. Asserted (`cp3-tests-pensionable-earnings.l4`).
6. Section 49 gives the contributory period no end for a disability pension, and none for a post-retirement disability benefit that commences after 1986: the rule returns `NOTHING`. Asserted (`cp3-tests-contributory-period.l4`).
7. Paragraph 49(d) excludes a family allowance recipient's month when the year's base unadjusted pensionable earnings are "equal to or less than" the basic exemption; paragraphs 44(2)(b)(iv) and 44(5)(d) exclude it only when they are "less than" it. A month with earnings exactly equal to the exemption is out of the contributory period of section 49 and in those of subsections 44(2)(b) and 44(5). Asserted on both sides (`cp3-tests-contributory-period.l4`, `cp3-tests-minimum-qualifying-period.l4`).
8. Paragraphs 55.11(b) and (c) leave a gap: a separation that begins on the very day section 55.11 came into force is not "before" it (b) and not "after" it (c). Asserted (`cp3-tests-division.l4`, `cp3-cases-seat.l4`; the day is an invented 31 July 2000, since the text gives none).
9. Two sections speak of "the coming into force of this section" (44.1(5), 55.11) and the text file gives no date for either. Subsection 44.1(5) is encoded as true for a conviction of which the Minister is informed before, on or after (all three constructors; asserted in `cp3-tests-benefits-not-payable.l4`); section 55.11 takes the day as a stated input.
10. Section 44.2 bars a survivor's pension only after a division under paragraph 55.1(1)(b) (spouses living apart); a division on a divorce (paragraph (a)) or between former common-law partners (paragraph (c)) does not bar it. Not asserted: the first input of the rule is already "a division under paragraph 55.1(1)(b)".

## What the stable binary does not accept

The binary is the one named in the brief (`l4` 1.6.98).
Each line below was run on it (the probes were short files, now deleted); the messages are copied from what it printed.

- `max` on two DATEs: `There are multiple definitions for the identifier max and I do not have sufficient information to make a choice between them.`, listing `max` for MAYBE OF NUMBER and for NUMBER. `max` and `min` are for numbers; a date needs an `IF` (`cp3 — the later of two dates`).
- `a NOT EQUALS b`: `unexpected NOT`. Write `NOT (a EQUALS b)`.
- `head xs`: `I could not find a definition for the identifier head`. Match the list instead (`WHEN x FOLLOWED BY rest`), as the modules here do.
- A parameter named `A`: `GIVEN A IS A NUMBER` stops with `unexpected A`; `A` is a keyword. Backtick it (`` `A` ``), as the formula letters of sections 51 and 53.3 are; other single capitals (B to R) are accepted.
- `JUST 15%` parses as `(JUST 15)%`: `The argument of '%' is expected to be of type NUMBER`. Write `JUST (15%)`.
- `a DIVIDED BY b` with b zero: `Division by zero in the operation: DIVIDED BY`, an error and not a value. Every division here is guarded and returns `NOTHING`.
- A misspelled field after `'s`: `I could not find a definition for the identifier xz which I have inferred to be of type: FUNCTION FROM Ev TO LIST OF NUMBER`. The message names the missing field, not the record.

Behaviour that is not an error but surprises:

- `NOT a OR b` parses as `NOT (a OR b)`: with a and b both TRUE the assertion `` `p bad` TRUE TRUE `` failed where `(NOT a) OR b` held. Every `NOT` in this piece is parenthesised, as the guide says; the danger is the silent one, because the file compiles.
- `any (GIVEN x YIELD ...) (record's field)` on two lines with the field in parentheses was accepted in a probe here; an earlier mis-parse of a similar layout could not be reproduced, so no limitation is recorded.

Accepted and used: `@export` with an inline `@desc` on each `GIVEN` input; `LIST` literals and `EMPTY`; `CONSIDER ... WHEN NOTHING THEN ... WHEN JUST x THEN ...`; `BRANCH ... OTHERWISE`; `WHERE` after a `CONSIDER`; list patterns `WHEN EMPTY` / `WHEN x FOLLOWED BY rest` with recursion; `foldl`, `sort`, `reverse`, `take`, `drop`, `filter`, `map`, `any`, `all`, `maximum`, `sum`, `count`, `null`, `fromMaybe`, `append`, `FLOOR`, `CEILING`; `YMD` (from the core); comparison of `YMD` values with `AT LEAST` and `LESS THAN`; record field access `r's \`field\``.

## What check.sh prints

The command was `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, run in this folder, and it printed (it exited 0):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
cp3-average-earnings.l4                        0         0       0        0         0
cp3-benefits-not-payable.l4                    0         0       0        0         0
cp3-benefits-payable.l4                        0         0       0        0         0
cp3-cases-seat.l4                              0       244       0        0         0
cp3-contributory-period.l4                     0         0       0        0         0
cp3-deemed-contributions.l4                    0         0       0        0         0
cp3-division.l4                                0         0       0        0         0
cp3-minimum-qualifying-period.l4               0         0       0        0         0
cp3-nouns.l4                                   0         0       0        0         0
cp3-part2-interpretation.l4                    0         0       0        0         0
cp3-pensionable-earnings.l4                    0         0       0        0         0
cp3-retirement-pension.l4                      0         0       0        0         0
cp3-seat.l4                                    0         0       0        0         0
cp3-tests-average-earnings.l4                  0        64       0        0         0
cp3-tests-benefits-not-payable.l4              0        36       0        0         0
cp3-tests-benefits-payable.l4                  0        53       0        0         0
cp3-tests-contributory-period.l4               0        52       0        0         0
cp3-tests-deemed-contributions.l4              0        61       0        0         0
cp3-tests-division.l4                          0       114       0        0         0
cp3-tests-interpretation.l4                    0        89       0        0         0
cp3-tests-minimum-qualifying-period.l4         0        97       0        0         0
cp3-tests-pensionable-earnings.l4              0        55       0        0         0
cp3-tests-retirement-pension.l4                0        46       0        0         0
cp3-tests-unadjusted-earnings.l4               0        69       0        0         0
cp3-unadjusted-earnings.l4                     0         0       0        0         0
cpp-core-age.l4                                0         0       0        0         0
cpp-core-application.l4                        0         0       0        0         0
cpp-core-calendar.l4                           0         0       0        0         0
cpp-core-definitions.l4                        0         0       0        0         0
cpp-core.l4                                    0         0       0        0         0
TOTAL (30 modules)                             0       980       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Read it by column: `errors` counts error diagnostics, `satisfied` the assertions that held, `failed` those that did not, `refused` those that could not be evaluated, and `expected` the failures a module is allowed (none here).
The eleven `cp3-tests-*.l4` files and `cp3-cases-seat.l4` carry the assertions (980 in all: 736 in layer 1's tests and 244 in the seat cases); the other cp3 modules carry none, so their zeros mean they compile and say nothing about their behaviour.
Beyond `check.sh`: `srcrefs check: 805 src: lines, 205 runs, 209 locators, 0 problems`; l4 check on the 13 non-test cp3 modules printed no error and 0 warnings (including the @ref placement warnings "is at the end of the file" and "follows code on its line").
`l4 run` on each of the eleven test files and on `cp3-cases-seat.l4`, counted separately, gave 0 error diagnostics and 0 `DiagnosticSeverity_Warning` lines, and in every file the number of `#ASSERT` lines equals the number satisfied.
No probe file is left in the folder.
After these runs one comment (the seat paragraph of the header) in `cp3-seat.l4` was reworded; `l4 check cp3-seat.l4` was run again and printed `Check succeeded.`, and no rule changed.

## Before this is worth relying on

1. The text is an unofficial converter rendering; nothing here has been compared with the official consolidation, and no lawyer has read the encoding.
2. No independent test pass has been run: every expected value in the `cp3-tests-*.l4` files and in `cp3-cases-seat.l4` is mine, worked by hand from the text before the run. Three expected values were changed during the work, each because I found my own arithmetic or typing wrong and re-derived the value by hand from the text: a test year in section 52.2, the first month of the second additional contributory period (1 January 2024) and a total in section 48(3) (550). No expectation was changed to match the code's output.
3. Twenty-seven forks (F1 to F27) rest on readings of mine. Those that change an answer for a person and are most worth a lawyer's look: F12 to F17 (who is entitled to which benefit), F6 (the average earnings after the child-raising deduction), F10 and F11 (the earnings after a division, and a reduced survivor's pension), F19 (when a spouse's application is out of time), and the forks marked "assumed, not ruled" (F3, F6, F7, F13, F15).
4. Figures that the Regulations set are inputs, not encoded here (the factor of subsection 46(3.1), the rounding of the Pension Index and of the annual adjustment, the cohabitation months of regulations 78 and 78.1, the meaning of "wholly or substantially", "maintaining", school attendance and "substantially gainful"). The seat layer asks for them as numbers or facts. Until piece cr2 is joined to this one, a person's answer is only as good as the figure they supply.
5. Every judgment the Act hands to the Minister (a disability determination, "informed and satisfied", approval of an application, "satisfied that" a separation would have continued) is an input supplied conditionally. The encoding says what follows if the Minister so finds; it does not say whether the Minister will.
6. The 1970 Act is not among the inputs, so subsection 51(3) is answered only for a year before 1974 (finding 5). Section 55.11 and subsection 44.1(5) refer to a coming into force with no date (finding 9).
7. The seat layer has no question for the month-by-month rules (sections 51 to 52.2), the lookback records (51.1, 51.2, 53.3, 53.4), the months of cohabitation (55(3), 55.1(4)), the sums of sections 50 to 50.2 or the list deductions of section 48(2) to (4): a person's answers about their pension rest on totals the person must work out first (their statement of contributions gives some). Those rules are encoded and tested in layer 1 only.
8. Provisions of Division C and later (application for and payment of benefits, the debt of section 66, the division totals of subsection 55.2(5.2) onward) are other pieces'. A survivor's pension that is "payable" under subsection 44(1) here may still not be paid for want of an application.
9. The layer-2 cases are one per question at least, with the facts a real person in the seat would state; a few reuse the figures of layer 1 for the arithmetic. The slowest file (`cp3-cases-seat.l4`) takes several minutes to run on a loaded machine.
