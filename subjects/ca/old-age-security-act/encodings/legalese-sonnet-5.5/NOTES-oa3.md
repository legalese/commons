# Notes: the Old Age Security Regulations, C.R.C., c. 1246 (piece oa3), encoding legalese-sonnet-5.5

**Status.** Every provision of lines 1-418 of the source (the title block, Part I Applications, Part II Reconsiderations and the Schedule) is encoded, marked repealed, or marked inert with a reason: 11 layer-1 modules (one of them the date helpers), 10 test files with 718 assertions, and a seat layer of 70 questions with 221 cases.
Every module checks and every assertion is satisfied on the stable binary 1.6.98; "What check.sh prints" below is the exact output.
**Unofficial text.** The source is a plain-text reproduction made by legalese commons of the Department of Justice Canada consolidation, current to 2026-09-30, and it says of itself that it "is not an official version".
The encoding follows that reproduction, not the official consolidation.
**Dates are data.** Lines 1-418 contain no date of enactment, making or coming into force; the commencement day of regulation 48 and the date of union of Newfoundland (regulation 2(2)) are inputs, and apart from the dates printed in the Schedule's agreement cells and the years 1969 to 1971 in regulation 21(8), the one calendar date a rule turns on is 7 March 1996 in regulation 22.1(2), carried as a value inside that rule.

## Seat

**The seat is a person who is 65 or older, or approaching it, asking whether they qualify for the Old Age Security pension, the Guaranteed Income Supplement or an Allowance, how much they would receive, and what they must do or tell the Minister.**
There is no seat for the Minister, the Social Security Tribunal, the Tax Court or any other official: what an official must or may do is asked as what is owed to the person or can be done to them.

Why this seat.
The Regulations are the working rules behind the Act: how an application is made and from what day an approval takes effect (regs 3 to 5, 10 to 12), what a payment is rounded to and how it is adjusted (6 to 9), what proof the Minister may ask for (15 to 20, 23), what counts as residence in Canada (21, 22), what a person must tell the Minister and when (25), and what can be done to their payments (24, 26 to 28.1).
A person at or near 65 asking whether they qualify, how much and what to do meets each of these.
Part II (reconsideration, the reference to the Tax Court, interest on a debt) is met only after something has gone wrong, and the seat marks its group as asked only in that situation.

How layer 2 is built.
`oa3-seat.l4` imports the layer-1 modules, takes plain inputs with an `@desc` in the person's words, builds the layer-1 records inside each question, and calls the layer-1 rule; it restates no rule.
`oa3-cases-seat.l4` holds the cases (221 assertions, at least one for each question), written from the words of the Regulations.
Where a layer-1 input is a judgment the text hands to the Minister ("it appears to him", "satisfied", "reasonable grounds"), the person is asked whether the Minister holds that view, as a fact about the other party.
Facts that the Act decides (whether the person is qualified for a pension, the day they became entitled to an allowance) are asked as facts the person can state; the Act's own provisions are encoded by other pieces.
The names of the questions carry the regulation number, so they cannot collide with the questions of the pieces that encode the Act.
Layer 1 and layer 2 repeat nothing: each rule is stated once, in layer 1.

Why duties are rules that answer yes, no or a date, and not DEONTIC contracts.
The Regulations put duties on the person (reg 20(1): give a statement of residence; reg 25: give notices; reg 24(3): an appointee's account) and on officials (regs 24(2), 38 to 47).
They are encoded as BOOLEAN or DATE rules that answer whether the duty has arisen, by what day, or whether it was met.
On the stable binary 1.6.98 an `#ASSERT` over a DEONTIC value fails even when it compares the value with itself (measured with `` `the obligation` EQUALS `the obligation` ``, which printed "assertion failed"), and the counts table of `check.sh` has no column for a `#TRACE` outcome, so a DEONTIC encoding could not be tested to the standard the brief sets.
Where the Regulations say "forthwith" or "immediately" (regs 25(1) to (4)) they give no number: the encoding computes the day the duty arises and takes timeliness as a fact the person states (fork F-25).

Conventions in the inputs.
A fact decided outside lines 1-418 is a plain input, commented `-- out of range: ...` where it is declared (listed under "Cross-references out of my ranges").
In layer 1 the bank rates of the month before the one being priced arrive as a list, so that a month with none gives no average (NOTHING), as the definition requires; the seat asks the person for the average itself and passes it as the one bank rate of that month (a list of one), whose mean is itself.
Regulation 48's rules take one debt record for a debt or for "a portion of the debt"; a debt with a payment schedule is run once for each portion.

The 70 questions, in the order of the Regulations (the group titles are the `§` headings of `oa3-seat.l4`):

**Applying for a benefit** (10)
- Is my application on the form the Minister requires (reg 3(1))?
- Is my application treated as made yet (reg 3(2))?
- Can a responsible person or agency act for me if I cannot (reg 4(1))?
- Can my province's authority apply for my pension for me (reg 4(2))?
- From what day will my pension take effect (reg 5)?
- From what day does my pension take effect if the Minister deems my application made, or waives the need for one (regs 5(3) and 5(4))?
- From what day does my supplement take effect if the Minister waives the need for an application (reg 10.1)?
- Must the Minister approve my application for a supplement (reg 10)?
- Must the Minister approve my application for an allowance (reg 11)?
- From what day will my allowance take effect (reg 12)?

**How my amounts are worked out** (4)
- What allowance will I be paid each month if my entitlement is $2 or less (reg 6)?
- What is my partial monthly pension rounded off to (reg 7)?
- What is my benefit after the quarterly adjustment (reg 8)?
- What Consumer Price Index figure applies to an adjustment quarter (reg 9)?

**Loss of income and pension income** (2)
- In which month is my loss of income treated as occurring (reg 13)?
- How much pension income do I have (reg 14)?

**Social Insurance Number and proof** (15)
- May the Minister give me a Social Insurance Number (reg 15)?
- Which document may the Minister ask me for to show my relationship with my spouse or partner (reg 16(1))?
- May the Minister ask me for the original of my marriage certificate (reg 16(2))?
- May the Minister accept my own declaration about my marriage (reg 16(3))?
- May the Minister use my tax return to decide whether I have a spouse or partner (reg 17)?
- Which year's tax return may the Minister use (reg 17)?
- Can the Minister work out my age and identity from my birth certificate or from the Employment Insurance Commission (reg 18(1))?
- May the Minister ask me for the original of my birth certificate (reg 18(2))?
- May the Minister use other evidence of my age and identity (reg 18(3))?
- May the Minister use Statistics Canada census information about my age (reg 18(4))?
- Are the conditions for a request to Statistics Canada about my age met (reg 18.1)?
- May the Minister accept my age as determined under the Canada Pension Plan (reg 19)?
- Must I give the Minister a statement of my residence and absences (reg 20)?
- Can the Minister require me to give more information or evidence (reg 23(1))?
- May the Minister investigate whether I am eligible to be paid a benefit (reg 23(2))?

**Residence** (5)
- Do I count as residing in Canada, setting aside regs 21(3), 21(5.1) and 21(5.2) which are asked separately (reg 21)?
- Is my time outside Canada counted as residence because I joined a resident who was abroad (reg 21(3))?
- Is my absence abroad with my spouse or dependants counted as time in Canada for an allowance (reg 21(5.1))?
- Does my spouse's or dependant's pensionable employment count as my residence in Canada (reg 21(5.2))?
- Am I legally resident in Canada (reg 22(1))?

**International agreements and sponsors** (3)
- Does the agreement with my country extend spouse treatment to my common-law partner (reg 22.01)?
- Which agreements does the Schedule list for my country (reg 22.01)?
- Does the sponsorship rule apply to my sponsor (reg 22.1)?

**Payments, notices and what I must tell the Minister** (17)
- To whom may the Minister direct my benefit if I cannot manage my own affairs (reg 24(1))?
- Who must give the Minister the notices of regulation 25 if my benefit is paid to someone else to manage (reg 24(4))?
- To whom may a benefit payment be made after I die (reg 24(5))?
- Have I been away from Canada for more than a month (reg 25(1))?
- By what day must I notify the Minister that I have returned to Canada (reg 25(1))?
- Have I given the notices the Regulations require after a long absence (reg 25(1))?
- Must I tell the Minister straight away if my address changes (reg 25(2))?
- Who must tell the Minister straight away if joint applicants for an allowance separate (reg 25(3))?
- Who must tell the Minister straight away if the beneficiary of an allowance dies (reg 25(4))?
- Can the Minister suspend my payments (reg 26(1))?
- For how many days of a suspension will I be paid once payment resumes (reg 26(2))?
- By what day must I ask to cancel my pension or supplement (reg 26.1(1))?
- Is my request to cancel in time (reg 26.1(1))?
- By what day must I repay once my request to cancel is granted (reg 26.1(2) and (3))?
- How much can be deducted from my benefit to recover what I owe (reg 27)?
- May the Minister deduct from my benefit what a province or municipality advanced me (reg 28.1(1))?
- Is the Minister barred from authorizing another such deduction (reg 28.1(2))?

**Reconsideration, appeals and interest** (14)
- Is my request for reconsideration complete (reg 29)?
- May the Minister give me a longer period to ask for reconsideration (reg 29.1)?
- May the Minister take steps to get the information needed to decide on a longer period (reg 29.1(3))?
- Must the Social Security Tribunal tell me that a ground of my appeal has been referred to the Tax Court (reg 38)?
- May the hearing of my reference be held at this place (reg 40(2))?
- Will the Registrar notify me by registered mail of the date, place and time of the hearing (reg 40(3))?
- Will the proceedings before the Court on my reference be informal and summary (reg 41(1))?
- Must the judge hear me before determining the procedure for my hearing (reg 41(2))?
- May the judge require me to file written submissions (reg 42)?
- Will I be sent a certified copy of the Court's decision (reg 44(2))?
- Am I free of costs and fees on a reference to the Tax Court (reg 45)?
- To what address must a notice to me be sent (reg 47)?
- How much interest accrues on my debt in a month (reg 48(4))?
- May the Minister remit the interest I owe (reg 48(7))?

Three groups carry a comment saying they arise only in a situation the person may not be in, so that a form can ask first: loss of income and pension income ("Has your income dropped?"), international agreements and sponsors, and reconsideration, appeals and interest.
No question of its own: regs 2(1), 2(3), 21(8), 22(2), 24(2), 24(3), 38.1, 39, 40(1), 44(1) and 46.
Regs 2(1) and 2(3) define terms; 21(8) and 22(2) name the information prescribed for section 4.1 of the Act, which is out of range; 24(2), 24(3), 38.1, 39, 40(1), 44(1) and 46 bind the Minister, an appointee, the Tribunal, the Registrar or a judge toward one another, and give the person no claim, privilege, power or immunity that the person would state facts to find out.

The Regulations' own figures (the $2 of reg 6, the $50 of reg 28.1(1)(d), the three per cent of reg 48(4), the six months of reg 26.1) are constants in these answers; the amount of a pension itself is the Act's and arrives as an input.

## Jural relations

One row for each provision that creates a relation between two parties; a provision that creates none (a definition, a counting or rounding rule, a rule of when something takes effect) is listed as `none`.
Where the text names no party on one side, the row says "not named in the text" and does not supply one.
A power's correlative is the other party's liability (being subject to the power); a privilege's is the other party's no-right; an immunity's is a disability.
The L4 rule column names rules taken from the coverage mapping, which was checked against the modules.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | relation | L4 rule |
| --- | --- | --- | --- | --- |
| reg 2(1) definitions, 2(2), 2(3) | none | none | none: names and deeming | `reg 2(1): the statute is the Act`, `reg 2(2): the residence or presence in Newfoundland on the day is deemed to be residence or presence in Canada` and 1 more in `oa3-regs-interpretation.l4` |
| reg 3(1) | the Minister (claim to an application on the form, where the Minister requires one) | the applicant (duty) | claim and duty | `reg 3(1): the application has the form the Minister requires` |
| reg 3(2) | none | none | none: says when an application counts as made | `reg 3(2): the application is deemed to have been made` |
| reg 4(1) | a responsible person or agency (power to act for a person the Minister considers unable) | the person acted for (liability) | power and liability | `reg 4(1): a responsible person or agency may make the request, appeal, application, statement or notice on the person's behalf` |
| reg 4(2) | the appropriate provincial authority (power to apply for a pension for a person in receipt of assistance) | the person acted for (liability) | power and liability | `reg 4(2): the appropriate provincial authority may make the application on the person's behalf` |
| reg 5(1) to (4), 10.1 | none | none | none: fix the day on which an approval takes effect; the claim to the benefit is the Act's | `reg 5(1): the approval of the application for a pension is within subsection (1)`, `reg 5(1): the day on which the approval is effective` and 3 more in `oa3-part1-applications.l4` |
| reg 6 | the spouse, common-law partner or survivor (claim to $2 a month) | not named in the text (it is payable "under Part III of the Act") | claim and duty | `reg 6: the allowance is raised to two dollars`, `reg 6: the monthly allowance payable` |
| reg 7, 8, 9 | none | none | none: rounding and averaging | `reg 7: the amount of a partial monthly pension rounded off`, `reg 8(2): the amount of a benefit as adjusted quarterly` and 1 more in `oa3-part1-amounts.l4` |
| reg 10, 11 | the pensioner (reg 10); the spouse, common-law partner or survivor (reg 11) (claim to approval) | the Minister (duty to approve) | claim and duty | `reg 10: the Minister must approve the application for a supplement by the pensioner in accordance with section 11 of the Act`, `reg 11: the Minister must approve the application for an allowance` |
| reg 12 | none | none | none: fixes the day on which an approval takes effect | `reg 12(1): the approval of the application for an allowance is after the last day of the month in which the application was received`, `reg 12(1): the day on which the approval is effective` and 1 more in `oa3-part1-applications.l4` |
| reg 13, 14 | none | none | none: a counting rule and a definition | `reg 13(a)(i): the month in which the person ceases to hold an office or employment`, `reg 13(a)(ii): the month in which the person ceases to carry on a business` and 3 more in `oa3-part1-income.l4` |
| reg 15 | the Minister (power to assign a Social Insurance Number) | the applicant, the beneficiary or their spouse or common-law partner (liability) | power and liability | `reg 15: the Minister may assign or cause to be assigned a Social Insurance Number` |
| reg 16(1) to (3) | the Minister (power to require a document, an original, or to accept a declaration) | the applicant (liability) | power and liability | `reg 16(1): the document of which the Minister may require submission`, `reg 16(2): the Minister may require the original certificate of marriage or, if applicable, a copy of the act of marriage issued by the competent authority` and 1 more in `oa3-part1-evidence.l4` |
| reg 17 | the Minister (privilege to use the person's tax return) | the person whose application was waived (no-right) | privilege and no-right | `reg 17: the Minister may use the person's tax return filed with the Minister of National Revenue`, `reg 17: the most recent calendar year for which the filing due date has passed` |
| reg 18(1) | not named in the text (the applicant is the person determined about) | the Minister (duty to determine age and identity on the stated bases) | duty; the holder of the correlative claim is not named | `reg 18(1): the Minister can determine the applicant's age and identity on the basis of paragraph (a) or (b)` |
| reg 18(2) to (4), 19 | the Minister (power to require an original, to determine on other evidence, to use Statistics Canada information, to accept a determination under the Canada Pension Plan) | the applicant (liability) | power and liability | `reg 18(2): the Minister may require the original birth certificate or, if applicable, a copy of the act of birth issued by the competent authority`, `reg 18(3): the Minister may determine the applicant's age and identity on the basis of any other information or evidence` and 2 more in `oa3-part1-evidence.l4` |
| reg 18.1 | not named in the text | whoever makes the request to Statistics Canada, and whoever receives what it supplies (the conditions of form, signed consent and specific information; confidentiality and limited use) | duty; the holder of the correlative claim is not named | `reg 18.1(a): the request to Statistics Canada meets the conditions`, `reg 18.1(b): the information supplied by Statistics Canada is handled as the condition requires` and 1 more in `oa3-part1-evidence.l4` |
| reg 20(1) | the Minister (claim to a statement of residence) | the person, or someone acting for them (duty) | claim and duty | `reg 20(1): the person or someone acting on the person's behalf must provide a statement giving full particulars of all periods of residence in Canada and of all absences from Canada that are relevant to that eligibility` |
| reg 20(2) | the person (privilege not to give the statement in the circumstances of the Act listed) | the Minister (no-right, unless the Minister requires otherwise under the Act) | privilege and no-right | `reg 20(2): the person is not required to provide a statement under subsection (1)` |
| reg 21, 22(1), 22(2) | none | none | none: definitions of residence, presence and legal residence, and the prescribed information | `reg 21(1)(a): the person resides in Canada`, `reg 21(1)(b): the person is present in Canada` and 2 more in `oa3-part1-residence.l4` |
| reg 22.01 | common-law partners (claim to the treatment afforded to spouses) | not named in the text ("shall be applied in Canada") | claim and duty | `reg 22.01: the agreement with the country is one referred to in the Schedule` |
| reg 22.1 | none | none | none: a list of events and the sponsors it applies to | `reg 22.1(1): Event in relation to a sponsor`, `reg 22.1(1): the events that have occurred in relation to the sponsor` and 1 more in `oa3-part1-agreements.l4` |
| reg 23(1) | the Minister (power to require further information or evidence) | the applicant, the person who applied for them, the beneficiary, or the person who receives payment (liability) | power and liability | `reg 23(1): the Minister may require the person to make available or allow to be made available further information or evidence regarding the eligibility of the applicant or the beneficiary for a benefit` |
| reg 23(2) | the Minister (power to investigate eligibility and capacity) | the person investigated (liability) | power and liability | `reg 23(2): the Minister may at any time make an investigation into the eligibility of a person to receive a benefit` |
| reg 24(1) | the Minister (power to direct a benefit to be paid to another) | the beneficiary (liability) | power and liability | `reg 24(1): the person or agency to whom the Minister may direct the benefit to be paid on behalf of the beneficiary` |
| reg 24(2) | the person or agency appointed (claim to directions) | the Minister (duty to furnish them) | claim and duty | `reg 24(2): the Minister must furnish directions regarding the administration and expenditure of the benefit in the best interests of the beneficiary` |
| reg 24(3) | the Minister (claim to an account) | the person or agency appointed (duty to account) | claim and duty | `reg 24(3): the person or agency has met the duty to account` |
| reg 24(4) | the Minister (claim to the notices of section 25) | the person or agency to whom the benefit is paid (duty to give them) | claim and duty | `reg 24(4): the party who must give the notices required by regulation 25` |
| reg 24(5) | the Minister (power to pay the estate, or a person or agency designated) | the estate (liability) | power and liability | `reg 24(5): the party to whom a benefit payment may be made after the beneficiary's death` |
| reg 25(1), (2) | the Minister (claim to notice of a long absence, of the return, of the address and of a change of it) | the applicant or beneficiary (duty) | claim and duty | `reg 25(1): the applicant or beneficiary has absented himself from Canada for a period in excess of one month`, `reg 25(2): the person must forthwith notify the Minister of a change of the address to which the benefit is to be sent` |
| reg 25(3) | the Minister (claim to notice of the separation) | the beneficiary and the pensioner (duty) | claim and duty | `reg 25(3): the parties who must immediately notify the Minister of the separation` |
| reg 25(4) | the Minister (claim to notice of the death) | the pensioner (duty) | claim and duty | `reg 25(4): the parties who must immediately notify the Minister of the death` |
| reg 26(1) | the Minister (power to suspend where further inquiry is necessary) | the beneficiary (liability to suspension); in the case where the Minister "shall" suspend, the Minister bears a duty and the text names no holder of the claim | power and liability; duty with no named claim-holder | `reg 26(1): Suspension of payment`, `reg 26(1): whether the Minister must or may suspend the payment of the benefit` and 1 more in `oa3-part1-payments.l4` |
| reg 26(2) | the beneficiary (claim to payment for the portion of the suspension during which eligible) | the Minister (duty) | claim and duty | `reg 26(2): the number of days of the period of suspension for which the Minister must pay the benefit` |
| reg 26.1(1) | the person (power to request cancellation, within six months of the first payment) | the Minister (liability to the request) | power and liability | `reg 26.1(1): the prescribed time within which a request for cancellation may be made`, `reg 26.1(1): the last day on which a request for cancellation may be made` and 1 more in `oa3-part1-payments.l4` |
| reg 26.1(2), (3) | the Minister (claim to repayment within six months of the day the request is granted) | not named in the text ("shall be repaid") | claim and duty | `reg 26.1(2): the last day on which the amount of the pension and related supplement or allowance must be repaid`, `reg 26.1(3): the last day on which the amount of the supplement and related allowance must be repaid` |
| reg 27 | the Minister (power to deduct and retain out of a benefit) | the person or their estate or succession (liability) | power and liability | `reg 27: the largest amount that may be deducted and retained out of the benefit` |
| reg 28.1(1) | the Minister (power to make a deduction from a benefit) | the beneficiary (liability) | power and liability | `reg 28.1(1): the Minister may make a deduction from a benefit` |
| reg 28.1(2) | not named in the text | the Minister (duty not to authorize any other deduction and payment) | duty; the holder of the correlative claim is not named | `reg 28.1(2): the Minister is barred from authorizing any other deduction and payment` |
| reg 29 | the Minister (claim to a request in writing, conveyed to the Minister, with the stated particulars) | the person requesting a reconsideration (duty as to form) | claim and duty | `reg 29(a): the request sets out the particulars of the person`, `reg 29(b): the request sets out its grounds and the facts` and 1 more in `oa3-part2-reconsiderations.l4` |
| reg 29.1(1), (2) | the Minister (power to allow a longer period) | the person asking (liability); (2) adds conditions the Minister must be satisfied of | power and liability | `reg 29.1: the Minister may allow a longer period to make the request for reconsideration`, `reg 29.1(2): the request for reconsideration is one that needs the further satisfaction of subsection (2)` |
| reg 29.1(3) | the Minister (power to take steps to obtain information) | the person asking (liability) | power and liability | `reg 29.1(3): the Minister may take any necessary steps to obtain information required to decide whether to allow a longer period` |
| reg 38 | the appellant and the Minister (claim to notice); the Registrar (claim to the documents) | the Social Security Tribunal (duty) | claim and duty | `reg 38(a): the persons the Social Security Tribunal must notify that the appeal on that ground has been referred to the Court`, `reg 38(b): the Social Security Tribunal must transmit to the Registrar of the Court a copy of the documents filed in the appeal that are relevant to the ground of appeal` |
| reg 38.1(1), (2) | not named in the text (the person who may be directly affected is the one it concerns) | the Minister, the Social Security Tribunal and the Registrar (each a duty, in a chain) | duties; the holder of the correlative claim is not named | `reg 38.1(1): the Minister must notify the Social Security Tribunal`, `reg 38.1(2): the Social Security Tribunal must notify the Registrar of the Court` and 1 more in `oa3-part2-reconsiderations.l4` |
| reg 39 | the Chief Judge, the Tribunal, the Minister and any added party (claim to notice); the Court (claim to a judge) | the Registrar (duty to notify); the Chief Judge (duty to appoint a judge) | claim and duty | `reg 39(1): the persons the Registrar of the Court must immediately notify of the receipt of the documents`, `reg 39(2): the Chief Judge of the Court must appoint a judge of the Court to hear the reference` |
| reg 40(1), (3) | the appellant, the Tribunal, the Minister and any added party (claim to notice of the hearing) | the Registrar (duty to fix the hearing and to notify by registered mail) | claim and duty | `reg 40(1): the Registrar of the Court must fix the date, time and place for the hearing of the reference`, `reg 40(3): the persons the Registrar of the Court must notify by registered mail of the date, place and time fixed for the hearing` |
| reg 40(2) | the appellant (claim to a hearing in or nearest the place of ordinary residence; power to consent in writing to another place) | not named in the text ("shall be held") | claim and duty; power | `reg 40(2): the hearing of the reference may be held at that place` |
| reg 41 | the parties or their representatives (claim to be heard); the judge (power to determine the procedure) | the judge (duty to hear them); the parties (liability to the procedure) | claim and duty; power and liability | `reg 41(1): the proceedings must be informal and conducted in a summary manner`, `reg 41(2): the judge must determine the procedure to be followed at the hearing, subject to the right of all parties or their representatives to be heard` |
| reg 42 | the judge (power to require written submissions); the appellant (power to consent, without which the power cannot be used) | the appellant, the Minister and any added party (liability) | power and liability | `reg 42: the persons from whom the judge may require written submissions` |
| reg 44 | the Registrar (claim to be advised); the appellant, the Tribunal, the Minister and any added party (claim to a certified copy) | the judge (duty to advise); the Registrar (duty to forward) | claim and duty | `reg 44(1): the judge must advise the Registrar of the Court of the judge's decision`, `reg 44(2): the persons to whom the Registrar of the Court must forward a certified copy of the decision` |
| reg 45 | the appellant (immunity from costs and fees) | the Court (disability) | immunity and disability | `reg 45: no costs may be awarded and no fees may be charged to the appellant by the Court` |
| reg 46 | not named in the text | the Social Security Tribunal (duty to proceed under its Rules of Procedure) | duty; the holder of the correlative claim is not named | `reg 46: the Social Security Tribunal must proceed in accordance with the Social Security Tribunal Rules of Procedure` |
| reg 47 | the person to whom a notice, request or document is to be sent (claim that it is addressed to the last known address) | whoever sends it (duty) | claim and duty | `reg 47: the address to which the notice, request or other document must be addressed` |
| reg 48(1) | none | none | none: definitions | `reg 48(1): the amount is a debt`, `reg 48(1): the due dates of the debt` |
| reg 48(2) to (4) | Her Majesty (claim to interest from the due date; the heading is "Interest on Amounts Owing to Her Majesty") | the debtor (duty to pay it) | claim and duty | `reg 48(2): interest is payable on the debt`, `reg 48(3): the first day on which interest accrues` and 4 more in `oa3-part2-interest.l4` |
| reg 48(5), (6) | the debtor (privilege: no duty to pay interest for a day on which a proceeding is pending or after the accrual ceases) | Her Majesty (no-right) | privilege and no-right | `reg 48: Facts about the accrual of interest on a debt`, `reg 48: interest accrues on the debt on the day` and 1 more in `oa3-part2-interest.l4` |
| reg 48(7) | the Minister (power to remit the interest, on four conditions) | the debtor (liability: being subject to the remission, which benefits them) | power and liability | `reg 48(7): the Minister may remit the interest payable under this section in whole or in part` |
| Schedule | none | none | none: data, the list of agreements to which reg 22.01 applies | `reg 22.01: the Schedule` |

## Coverage table

The text has 35 headings, and each has a row of its own; the other 141 rows are the title block, regulations, subsections, definitions, the repealed provisions and the Schedule, so there are 176 rows in all.
Counts by disposition: encoded: 129, fork: 28, inert: 3, repealed or blank in this text: 16.
A `fork` row is also encoded; it names its fork-register entry, and the reading taken is the one in the module. The 28 fork rows point to the 26 entries of the register (one entry can cover two rows, and F-5(2)(d) is an entry of its own).
The `inert` rows are the title block, the Short Title heading and regulation 1, which are pure title and citation, and the reason is in each row's note.
The `repealed or blank in this text` rows are those the text itself shows as `[Repealed, ...]`.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| title block (title, citation, long title, enabling authority) | src:5-8 | inert | none | pure title and citation: the name of the Regulations, their citation, their long title and the enabling Act; no rule depends on them |
| "Short Title" (heading) | src:10 | inert | none | a pure citation or title: the heading of regulation 1, which gives the Regulations their short title; it names a section and decides nothing about what any person is owed or must do |
| reg 1 | src:11 | inert | oa3-regs-interpretation.l4 (quoted, no rule) | a pure citation or title: it says only that these Regulations may be cited as the Old Age Security Regulations, which is a name and not a rule; nothing in the Regulations or the Act computes from it, so the text is quoted in the interpretation module and carries no rule |
| "Interpretation" (heading) | src:13 | encoded | oa3-regs-interpretation.l4 | carried as the section heading `Interpretation` of the module |
| reg 2(1), introductory words | src:14 | encoded | oa3-regs-interpretation.l4 | "In these Regulations,": each definition below is its own rule, so the formula needs none |
| reg 2(1) "Act" | src:15 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the statute is the Act` | a name for the thing the Act or the Regulations already name |
| reg 2(1) "appeal" | src:16 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the appeal is an appeal for the purposes of these Regulations` | widens or restates the Act's term |
| reg 2(1) "appellant" | src:17 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the person is an appellant` | widens or restates the Act's term |
| reg 2(1) "applicant" | src:18 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "application form" | src:19 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the form is an application form` | a name for the thing the Act or the Regulations already name |
| reg 2(1) "beneficiary" | src:20 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the person is a beneficiary for the purposes of these Regulations` | widens or restates the Act's term |
| reg 2(1) "Board" | src:21 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "Court" | src:22 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the court is the Court` | a name for the thing the Act or the Regulations already name |
| reg 2(1) "Minister" | src:23 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "reference" | src:24 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the proceeding is a reference` | a name for the thing the Act or the Regulations already name |
| reg 2(1) "Regional Director" | src:25 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "request for reconsideration" | src:26 | encoded | oa3-regs-interpretation.l4: `reg 2(1): the request is a request for reconsideration` | a name for the thing the Act or the Regulations already name |
| reg 2(1) "Review Committee" | src:27 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "Review Tribunal" | src:28 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1) "secretary" | src:29 | repealed or blank in this text | none | the text shows `[Repealed, ...]` |
| reg 2(1.1) | src:30 | repealed or blank in this text | none | the text shows `[Repealed, SOR/2017-225, s. 1]` |
| reg 2(2) | src:31 | fork | oa3-regs-interpretation.l4: `reg 2(2): the residence or presence in Newfoundland on the day is deemed to be residence or presence in Canada` | F-2(2): the date of union is not stated, so it is an input; "prior to" excludes the day itself |
| reg 2(3) | src:32 | fork | oa3-regs-interpretation.l4: `reg 2(3): the individual is a prescribed individual for the purpose of the definition public officer in subsection 33(1) of the Act` | F-2(3): the closing words qualify both kinds of person |
| "PART I Applications" (heading) | src:34 | encoded | every Part I module | carried as the section heading `PART I Applications` in each Part I module |
| "Forms for Applications" (heading) | src:36 | encoded | oa3-part1-applications.l4 | carried as the section heading `Forms for Applications` of the module |
| reg 3(1) | src:37 | encoded | oa3-part1-applications.l4: `reg 3(1): the application has the form the Minister requires` |  |
| reg 3(2) | src:38 | encoded | oa3-part1-applications.l4: `reg 3(2): the application is deemed to have been made` | the Act's deeming (5(2), 11(3)) is an input |
| reg 4(1) | src:39 | encoded | oa3-part1-applications.l4: `reg 4(1): a responsible person or agency may make the request, appeal, application, statement or notice on the person's behalf` | what the Minister considers is an input |
| reg 4(2) | src:40 | encoded | oa3-part1-applications.l4: `reg 4(2): the appropriate provincial authority may make the application on the person's behalf` | only for a pension |
| "Approval of an Application for a Pension" (heading) | src:42 | encoded | oa3-part1-applications.l4 | carried as the section heading `Approval of an Application for a Pension` of the module |
| reg 5(1) | src:43-49 | fork | oa3-part1-applications.l4: `reg 5(1): the approval of the application for a pension is within subsection (1)`, `reg 5(1): the day on which the approval is effective` | F-5(1)(e): no date specified drops that limb |
| reg 5(2) | src:50-54 | fork | oa3-part1-applications.l4: `reg 5(2): the applicant attained the age of 65 years before the day on which the application was received` and the combined `reg 5: the day on which the Minister's approval of the application for a pension is effective` | F-5(2) and F-5(2)(d) |
| reg 5(3) | src:55 | encoded | oa3-part1-applications.l4: `reg 5(3): the day on which the Minister's approval of the deemed application is effective` |  |
| reg 5(4) | src:56 | encoded | oa3-part1-applications.l4: `reg 5(4): the day on which the Minister's approval is effective where the requirement for an application is waived` |  |
| "Payment of an Allowance Under Two Dollars" (heading) | src:58 | encoded | oa3-part1-amounts.l4 | carried as the section heading `Payment of an Allowance Under Two Dollars` of the module |
| reg 6 | src:59 | fork | oa3-part1-amounts.l4: `reg 6: the allowance is raised to two dollars`, `reg 6: the monthly allowance payable` | F-6: a nil entitlement is not raised |
| "Manner of Rounding Off Amount of Partial Monthly Pension" (heading) | src:61 | encoded | oa3-part1-amounts.l4 | carried as the section heading `Manner of Rounding Off Amount of Partial Monthly Pension` of the module |
| reg 7 | src:62-64 | encoded | oa3-part1-amounts.l4: `reg 7: the amount of a partial monthly pension rounded off` | the keel's half-up helper is the dropped-digit rule |
| "Manner of Quarterly Adjustment of Benefit" (heading) | src:66 | encoded | oa3-part1-amounts.l4 | carried as the section heading `Manner of Quarterly Adjustment of Benefit` of the module |
| reg 8(1) | src:67-74 | encoded | oa3-part1-amounts.l4: type `reg 8(1): Provision of the Act under which a benefit is adjusted quarterly` and `reg 8(2): the amount of a benefit as adjusted quarterly` | the five provisions are the five constructors |
| reg 8(2) | src:75-77 | encoded | oa3-part1-amounts.l4: `reg 8(2): the amount of a benefit as adjusted quarterly` | the 7.1(1) increase is read for subsection 7(2) only |
| reg 8(3) | src:78-80 | fork | oa3-part1-amounts.l4: `reg 8(3): the ratio of the Consumer Price Index for the first adjustment quarter to that for the second, expressed as a decimal number` | F-8(3): the digit that decides is the fourth either way; a second index of 0 gives NOTHING |
| "Determination of Average Consumer Price Index for Period of Months" (heading) | src:82 | encoded | oa3-part1-amounts.l4 | carried as the section heading `Determination of Average Consumer Price Index for Period of Months` of the module |
| reg 9(1) | src:83 | encoded | oa3-part1-amounts.l4: `reg 9(1): the average of the Consumer Price Index for Canada for a period of months` | NOTHING for no months |
| reg 9(2) | src:84-86 | fork | oa3-part1-amounts.l4: `reg 9(2): the quotient expressed as a decimal fraction of one digit`, `reg 9: the average of the Consumer Price Index for a period of months as determined under regulation 9` | F-9(2): every quotient is rounded to one decimal |
| "Approval of Application for a Supplement" (heading) | src:88 | encoded | oa3-part1-applications.l4 | carried as the section heading `Approval of Application for a Supplement` of the module |
| reg 10 | src:89 | encoded | oa3-part1-applications.l4: `reg 10: the Minister must approve the application for a supplement by the pensioner in accordance with section 11 of the Act` |  |
| reg 10.1 | src:90 | encoded | oa3-part1-applications.l4: `reg 10.1: the day on which the Minister's approval of the supplement is effective where the requirement for an application is waived` |  |
| "Approval of Application for an Allowance" (heading) | src:92 | encoded | oa3-part1-applications.l4 | carried as the section heading `Approval of Application for an Allowance` of the module |
| reg 11 | src:93 | encoded | oa3-part1-applications.l4: `reg 11: the Minister must approve the application for an allowance` |  |
| reg 12(1) | src:94-96 | encoded | oa3-part1-applications.l4: `reg 12(1): the approval of the application for an allowance is after the last day of the month in which the application was received`, `reg 12(1): the day on which the approval is effective` and the combined `reg 12: the day on which the Minister's approval of the application for an allowance is effective` | (1) is "subject to" (2) and (3) |
| reg 12(2) | src:97-100 | fork | oa3-part1-applications.l4: `reg 12(2): the spouse or common-law partner of a pensioner attained the age of 60 years before the day on which the application was received`, `reg 12(2): the day on which the approval is effective` and the combined `reg 12: the day on which the Minister's approval of the application for an allowance is effective` | F-12: (2) and (3) do not repeat the condition of (1) |
| reg 12(3) | src:101-103 | fork | oa3-part1-applications.l4: `reg 12(3): the survivor became entitled to an allowance under section 21 of the Act before the day on which the application was received`, `reg 12(3): the day on which the approval is effective` and the combined `reg 12: the day on which the Minister's approval of the application for an allowance is effective` | F-12: (2) and (3) do not repeat the condition of (1) |
| "Month in which Loss of Income Occurs" (heading) | src:105 | encoded | oa3-part1-income.l4 | carried as the section heading `Month in which Loss of Income Occurs` of the module |
| reg 13 | src:106-110 | encoded | oa3-part1-income.l4: `reg 13(a)(i): the month in which the person ceases to hold an office or employment`, `reg 13(a)(ii): the month in which the person ceases to carry on a business`, `reg 13(b): the month in which the person suffers a loss of income due to termination or reduction of pension income` | the month is answered as its first day |
| "Definition of Pension Income" (heading) | src:112 | encoded | oa3-part1-income.l4 | carried as the section heading `Definition of Pension Income` of the module |
| reg 14 | src:113-122 | encoded | oa3-part1-income.l4: record `reg 14: Amounts received` and `reg 14: pension income` | (e) and (f) carve something out of their own item: the record keeps the carve-out |
| "Assignment of Social Insurance Numbers to Applicants, Beneficiaries, Spouses or Common-law Partners" (heading) | src:124 | encoded | oa3-part1-evidence.l4 | carried as the section heading `Assignment of Social Insurance Numbers to Applicants, Beneficiaries, Spouses or Common-law Partners` of the module |
| reg 15 | src:125 | encoded | oa3-part1-evidence.l4: `reg 15: the Minister may assign or cause to be assigned a Social Insurance Number` |  |
| "Relationship Evidence" (heading) | src:127 | encoded | oa3-part1-evidence.l4 | carried as the section heading `Relationship Evidence` of the module |
| reg 16(1) | src:128-130 | encoded | oa3-part1-evidence.l4: `reg 16(1): the document of which the Minister may require submission` |  |
| reg 16(2) | src:131 | encoded | oa3-part1-evidence.l4: `reg 16(2): the Minister may require the original certificate of marriage or, if applicable, a copy of the act of marriage issued by the competent authority` |  |
| reg 16(3) | src:132 | encoded | oa3-part1-evidence.l4: `reg 16(3): the Minister may determine the relationship on the basis of a statutory declaration or other evidence of the marriage` |  |
| reg 17 | src:133 | fork | oa3-part1-evidence.l4: `reg 17: the Minister may use the person's tax return filed with the Minister of National Revenue`, `reg 17: the most recent calendar year for which the filing due date has passed` | F-17: the due date is an input; "has passed" excludes the due date itself |
| "Evidence of Age and Identity" (heading) | src:135 | encoded | oa3-part1-evidence.l4 | carried as the section heading `Evidence of Age and Identity` of the module |
| reg 18(1) | src:136-138 | encoded | oa3-part1-evidence.l4: `reg 18(1): the Minister can determine the applicant's age and identity on the basis of paragraph (a) or (b)` | (a) and (b) are not ranked |
| reg 18(2) | src:139 | encoded | oa3-part1-evidence.l4: `reg 18(2): the Minister may require the original birth certificate or, if applicable, a copy of the act of birth issued by the competent authority` |  |
| reg 18(3) | src:140 | encoded | oa3-part1-evidence.l4: `reg 18(3): the Minister may determine the applicant's age and identity on the basis of any other information or evidence` |  |
| reg 18(4) | src:141 | encoded | oa3-part1-evidence.l4: `reg 18(4): the Minister may determine the applicant's age and identity on the basis of information obtained from Statistics Canada` | "if possible" is an input |
| reg 18.1 | src:142-147 | encoded | oa3-part1-evidence.l4: `reg 18.1(a): the request to Statistics Canada meets the conditions`, `reg 18.1(b): the information supplied by Statistics Canada is handled as the condition requires`, `reg 18.1: the conditions for the purposes of section 6 of the Act are met` |  |
| reg 19 | src:148 | encoded | oa3-part1-evidence.l4: `reg 19: the Minister may accept the determination of the applicant's age made under the Canada Pension Plan` |  |
| reg 19.1 | src:149 | repealed or blank in this text | none | the text shows `[Repealed, SOR/96-521, s. 8]` |
| "Residence" (heading) | src:151 | encoded | oa3-part1-evidence.l4 | carried as the section heading `Residence` of the module |
| reg 20(1) | src:152 | encoded | oa3-part1-evidence.l4: `reg 20(1): the person or someone acting on the person's behalf must provide a statement giving full particulars of all periods of residence in Canada and of all absences from Canada that are relevant to that eligibility` | a duty of the person |
| reg 20(2) | src:153 | encoded | oa3-part1-evidence.l4: `reg 20(2): the person is not required to provide a statement under subsection (1)` | the Act's circumstances are one input |
| reg 21(1) | src:154-156 | fork | oa3-part1-residence.l4: `reg 21(1)(a): the person resides in Canada`, `reg 21(1)(b): the person is present in Canada` | the keel's register inputs (`the person resides in Canada`, `the person is present in Canada`) are answered by the composites; F-21: the text does not say which deeming limb wins when they meet |
| reg 21(2) | src:157 | encoded | oa3-part1-residence.l4: `reg 21(2): the person is deemed not to be living in any part of Canada` |  |
| reg 21(2.1) | src:158-165 | encoded | oa3-part1-residence.l4: `reg 21(2.1): the person does not reside in Canada during the period` | the purposes are a record of seven yes/no |
| reg 21(3) | src:166-168 | encoded | oa3-part1-residence.l4: `reg 21(3)(a): the person returns to Canada before or within six months after the return of the other person, or within six months after that person's death`, `reg 21(3): the period outside Canada is considered a period of residence and presence in Canada` |  |
| reg 21(4) | src:169-173 | fork | oa3-part1-residence.l4: `reg 21(4): the interval of absence is deemed not to have interrupted the person's residence or presence in Canada` | F-21(4): "does not exceed one year" is counted to the anniversary day |
| reg 21(5)(a) | src:175-185 | encoded | oa3-part1-residence.l4: `reg 21(5)(a): the absence is in the circumstance of employment out of Canada` | each paragraph is its own rule on its own facts |
| reg 21(5)(b) | src:186-196 | encoded | oa3-part1-residence.l4: `reg 21(5)(b): the absence is in the circumstance of employment or engagement out of Canada` | each paragraph is its own rule on its own facts |
| reg 21(5)(c) | src:197-199 | encoded | oa3-part1-residence.l4: `reg 21(5)(c): the absence is in the circumstance of accompanying a spouse or common-law partner` | each paragraph is its own rule on its own facts |
| reg 21(5)(d) | src:200-202 | encoded | oa3-part1-residence.l4: `reg 21(5)(d): the absence is in the circumstance of awaiting transportation to Canada` | each paragraph is its own rule on its own facts |
| reg 21(5)(e) | src:203-205 | encoded | oa3-part1-residence.l4: `reg 21(5)(e): the absence is in the circumstance of accompanying a spouse awaiting transportation to Canada` | each paragraph is its own rule on its own facts |
| reg 21(5)(f) | src:206-208 | encoded | oa3-part1-residence.l4: `reg 21(5)(f): the absence is in the circumstance of a dependent person accompanying the person on whom they depend` | each paragraph is its own rule on its own facts |
| reg 21(5), introductory words | src:174 | encoded | oa3-part1-residence.l4: `reg 21(5): the absence is one of the absences specified in subsection (5)` |  |
| reg 21(5.1) | src:209 | encoded | oa3-part1-residence.l4: `reg 21(5.1): the absence is not considered to have interrupted the residence or presence in Canada` | for the purposes of an allowance |
| reg 21(5.2) | src:210 | fork | oa3-part1-residence.l4: `reg 21(5.2): the period of pensionable employment is considered a period of residence in Canada` | F-21(5.2): whose residence |
| reg 21(5.3) | src:211 | encoded | oa3-part1-residence.l4: `reg 21(5.3): the person is deemed not to be resident in Canada` |  |
| reg 21(6) | src:212 | encoded | oa3-part1-residence.l4: type `reg 21(6): Relative of a person`, `reg 21(6): the relative is a dependent person for the purposes of paragraph (5)(f)` |  |
| reg 21(7) | src:213-217 | encoded | oa3-part1-residence.l4: `reg 21(7): the relative is a dependant` |  |
| reg 21(8) | src:218-225 | fork | oa3-part1-residence.l4: `reg 21(8)(a): the year counts toward the forty years`, `reg 21(8)(b): the information indicates forty years and returns filed`, `reg 21(8): the prescribed information for subparagraph 3(1)(c)(iii) of the Act has been made available` | F-21(8): the years 1969 to 1971 are excluded from the count of forty returns |
| reg 21(9) | src:226-228 | encoded | oa3-part1-residence.l4: record `reg 21(8): Facts about a calendar year` | the borrowed terms of the Canada and Quebec Pension Plans are asked as facts about each year |
| "Legal Residence" (heading) | src:230 | encoded | oa3-part1-residence.l4 | carried as the section heading `Legal Residence` of the module |
| reg 22(1) | src:231-236 | fork | oa3-part1-residence.l4: `reg 22(1): the person is legally resident in Canada` | F-22(1): the facts are those of the applicable day, taken as inputs |
| reg 22(2) | src:237-241 | encoded | oa3-part1-residence.l4: `reg 22(2): the prescribed information for paragraph 4(1)(a) of the Act has been made available` |  |
| "Application of International Agreements" (heading) | src:243 | encoded | oa3-part1-agreements.l4 | carried as the section heading `Application of International Agreements` of the module |
| reg 22.01 | src:244 | encoded | oa3-part1-agreements.l4: `reg 22.01: the agreement with the country is one referred to in the Schedule` and two siblings |  |
| "Sponsorship Immigrants" (heading) | src:246 | encoded | oa3-part1-agreements.l4 | carried as the section heading `Sponsorship Immigrants` of the module |
| reg 22.1(1) | src:247-251 | fork | oa3-part1-agreements.l4: type `reg 22.1(1): Event in relation to a sponsor`, `reg 22.1(1): the events that have occurred in relation to the sponsor` | F-22.1: a term of imprisonment is a number of months |
| reg 22.1(2) | src:252-254 | fork | oa3-part1-agreements.l4: `reg 22.1(2): subsection (1) applies to the sponsor` | F-22.1: "in effect on or after" is "not ended before" |
| "Further Information and Investigation Before or After the Approval of an Application or Before or After the Requirement of an Application Is Waived" (heading) | src:256 | encoded | oa3-part1-evidence.l4 | carried as the section heading `Further Information and Investigation ...` of the module |
| reg 23(1) | src:257 | encoded | oa3-part1-evidence.l4: `reg 23(1): the Minister may require the person to make available or allow to be made available further information or evidence regarding the eligibility of the applicant or the beneficiary for a benefit` |  |
| reg 23(2) | src:258 | encoded | oa3-part1-evidence.l4: `reg 23(2): the Minister may at any time make an investigation into the eligibility of a person to receive a benefit` | a rule with no input: the text names no condition |
| "Payment to Person other than Beneficiary" (heading) | src:260 | encoded | oa3-part1-payments.l4 | carried as the section heading `Payment to Person other than Beneficiary` of the module |
| reg 24(1) | src:261-263 | encoded | oa3-part1-payments.l4: `reg 24(1): the person or agency to whom the Minister may direct the benefit to be paid on behalf of the beneficiary` | (a) is looked at first, (b) only where (a) fails |
| reg 24(2) | src:264 | encoded | oa3-part1-payments.l4: `reg 24(2): the Minister must furnish directions regarding the administration and expenditure of the benefit in the best interests of the beneficiary` |  |
| reg 24(3) | src:265 | encoded | oa3-part1-payments.l4: `reg 24(3): the person or agency has met the duty to account` |  |
| reg 24(4) | src:266 | encoded | oa3-part1-payments.l4: `reg 24(4): the party who must give the notices required by regulation 25` |  |
| reg 24(5) | src:267-269 | encoded | oa3-part1-payments.l4: `reg 24(5): the party to whom a benefit payment may be made after the beneficiary's death` | NOTHING when neither (a) nor (b) |
| "Notices by or on Behalf of an Applicant or Beneficiary" (heading) | src:271 | encoded | oa3-part1-payments.l4 | carried as the section heading `Notices by or on Behalf of an Applicant or Beneficiary` of the module |
| reg 25(1) | src:272 | fork | oa3-part1-payments.l4: `reg 25(1): the applicant or beneficiary has absented himself from Canada for a period in excess of one month` (four rules) | F-25: "forthwith" is not measured |
| reg 25(2) | src:273 | encoded | oa3-part1-payments.l4: `reg 25(2): the person must forthwith notify the Minister of a change of the address to which the benefit is to be sent` (two rules) |  |
| reg 25(3) | src:274 | encoded | oa3-part1-payments.l4: `reg 25(3): the parties who must immediately notify the Minister of the separation` |  |
| reg 25(4) | src:275 | encoded | oa3-part1-payments.l4: `reg 25(4): the parties who must immediately notify the Minister of the death` |  |
| reg 25(5) | src:276 | repealed or blank in this text | none | the text shows `[Repealed, SOR/81-285, s. 7]` |
| "Suspension of Payments" (heading) | src:278 | encoded | oa3-part1-payments.l4 | carried as the section heading `Suspension of Payments` of the module |
| reg 26(1) | src:279 | encoded | oa3-part1-payments.l4: type `reg 26(1): Suspension of payment`, `reg 26(1): whether the Minister must or may suspend the payment of the benefit`, `reg 26(1): the suspension continues` |  |
| reg 26(2) | src:280 | fork | oa3-part1-payments.l4: `reg 26(2): the number of days of the period of suspension for which the Minister must pay the benefit` | F-26(2): the portion of the period is counted in days, both ends included |
| "Cancellation of Pension or Supplement" (heading) | src:282 | encoded | oa3-part1-payments.l4 | carried as the section heading `Cancellation of Pension or Supplement` of the module |
| reg 26.1(1) | src:283 | encoded | oa3-part1-payments.l4: `reg 26.1(1): the prescribed time within which a request for cancellation may be made` (the keel's register item 11), `reg 26.1(1): the last day on which a request for cancellation may be made`, `reg 26.1(1): the request for cancellation is made in time` | six months, calendar months |
| reg 26.1(2) | src:284 | encoded | oa3-part1-payments.l4: `reg 26.1(2): the last day on which the amount of the pension and related supplement or allowance must be repaid` |  |
| reg 26.1(3) | src:285 | encoded | oa3-part1-payments.l4: `reg 26.1(3): the last day on which the amount of the supplement and related allowance must be repaid` |  |
| "Recovery of Overpayments" (heading) | src:287 | encoded | oa3-part1-payments.l4 | carried as the section heading `Recovery of Overpayments` of the module |
| reg 27 | src:288 | fork | oa3-part1-payments.l4: `reg 27: the largest amount that may be deducted and retained out of the benefit` | F-27: what causes undue hardship is an input |
| reg 28 | src:289 | repealed or blank in this text | none | the text shows `[Repealed, SOR/99-193, s. 2]` |
| "Deductions from Benefits" (heading) | src:291 | encoded | oa3-part1-payments.l4 | carried as the section heading `Deductions from Benefits` of the module |
| reg 28.1(1) | src:292-296 | fork | oa3-part1-payments.l4: `reg 28.1(1): the Minister may make a deduction from a benefit` | F-28.1: the anniversary day is within the year |
| reg 28.1(2) | src:297 | encoded | oa3-part1-payments.l4: `reg 28.1(2): the Minister is barred from authorizing any other deduction and payment` |  |
| reg 28.2 | src:298 | repealed or blank in this text | none | the text shows `[Repealed, SOR/2013-20, s. 7]` |
| reg 28.3 | src:299 | repealed or blank in this text | none | the text shows `[Repealed, SOR/2013-20, s. 7]` |
| reg 28.4 | src:300 | repealed or blank in this text | none | the text shows `[Repealed, SOR/2013-20, s. 7]` |
| "PART II Reconsiderations" (heading) | src:302 | encoded | oa3-part2-reconsiderations.l4, oa3-part2-interest.l4 | carried as the section heading `PART II Reconsiderations` |
| "Request for Reconsideration" (heading) | src:304 | encoded | oa3-part2-reconsiderations.l4 | carried as the section heading `Request for Reconsideration` of the module |
| reg 29 | src:305-307 | encoded | oa3-part2-reconsiderations.l4: `reg 29(a): the request sets out the particulars of the person`, `reg 29(b): the request sets out its grounds and the facts`, `reg 29: the request for a reconsideration under section 27.1 of the Act is made as the Regulations require` |  |
| reg 29.1(1) | src:308 | fork | oa3-part2-reconsiderations.l4: `reg 29.1: the Minister may allow a longer period to make the request for reconsideration` | F-29.1: the 365 days of (2) are days |
| reg 29.1(2) | src:309-311 | fork | oa3-part2-reconsiderations.l4: `reg 29.1(2): the request for reconsideration is one that needs the further satisfaction of subsection (2)` | F-29.1 |
| reg 29.1(3) | src:312 | encoded | oa3-part2-reconsiderations.l4: `reg 29.1(3): the Minister may take any necessary steps to obtain information required to decide whether to allow a longer period` | a rule with no input |
| regs 30 to 37 | src:313 | repealed or blank in this text | none | the text shows `30 to 37 [Repealed, SOR/96-521, s. 18]` |
| "Reference to Tax Court of Canada" (heading) | src:315 | encoded | oa3-part2-reconsiderations.l4 | carried as the section heading `Reference to Tax Court of Canada` of the module |
| reg 38 | src:316-318 | encoded | oa3-part2-reconsiderations.l4: `reg 38(a): the persons the Social Security Tribunal must notify that the appeal on that ground has been referred to the Court`, `reg 38(b): the Social Security Tribunal must transmit to the Registrar of the Court a copy of the documents filed in the appeal that are relevant to the ground of appeal` |  |
| reg 38.1(1) | src:319 | encoded | oa3-part2-reconsiderations.l4: `reg 38.1(1): the Minister must notify the Social Security Tribunal` |  |
| reg 38.1(2) | src:320 | fork | oa3-part2-reconsiderations.l4: `reg 38.1(2): the Social Security Tribunal must notify the Registrar of the Court`, `reg 38.1(2): the Registrar of the Court must add the person as a party to the appeal` | F-38.1(2) |
| reg 39(1) | src:321 | encoded | oa3-part2-reconsiderations.l4: `reg 39(1): the persons the Registrar of the Court must immediately notify of the receipt of the documents` |  |
| reg 39(2) | src:322 | encoded | oa3-part2-reconsiderations.l4: `reg 39(2): the Chief Judge of the Court must appoint a judge of the Court to hear the reference` |  |
| "Date and Place of Reference" (heading) | src:324 | encoded | oa3-part2-reconsiderations.l4 | carried as the section heading `Date and Place of Reference` of the module |
| reg 40(1) | src:325 | encoded | oa3-part2-reconsiderations.l4: `reg 40(1): the Registrar of the Court must fix the date, time and place for the hearing of the reference` |  |
| reg 40(2) | src:326 | encoded | oa3-part2-reconsiderations.l4: `reg 40(2): the hearing of the reference may be held at that place` |  |
| reg 40(3) | src:327 | encoded | oa3-part2-reconsiderations.l4: `reg 40(3): the persons the Registrar of the Court must notify by registered mail of the date, place and time fixed for the hearing` |  |
| "Procedure before Tax Court of Canada" (heading) | src:329 | encoded | oa3-part2-reconsiderations.l4 | carried as the section heading `Procedure before Tax Court of Canada` of the module |
| reg 41(1) | src:330 | encoded | oa3-part2-reconsiderations.l4: `reg 41(1): the proceedings must be informal and conducted in a summary manner` | a standard of conduct: the rule records that it binds proceedings before the Court |
| reg 41(2) | src:331 | encoded | oa3-part2-reconsiderations.l4: `reg 41(2): the judge must determine the procedure to be followed at the hearing, subject to the right of all parties or their representatives to be heard` |  |
| reg 42 | src:332 | encoded | oa3-part2-reconsiderations.l4: `reg 42: the persons from whom the judge may require written submissions` |  |
| "Decision of Tax Court of Canada" (heading) | src:334 | encoded | oa3-part2-reconsiderations.l4 | carried as the section heading `Decision of Tax Court of Canada` of the module |
| reg 43 | src:335 | repealed or blank in this text | none | the text shows `[Repealed, SOR/2000-133, s. 11]` |
| reg 44(1) | src:336 | encoded | oa3-part2-reconsiderations.l4: `reg 44(1): the judge must advise the Registrar of the Court of the judge's decision` |  |
| reg 44(2) | src:337 | encoded | oa3-part2-reconsiderations.l4: `reg 44(2): the persons to whom the Registrar of the Court must forward a certified copy of the decision` |  |
| reg 45 | src:338 | encoded | oa3-part2-reconsiderations.l4: `reg 45: no costs may be awarded and no fees may be charged to the appellant by the Court` |  |
| reg 46 | src:339 | encoded | oa3-part2-reconsiderations.l4: `reg 46: the Social Security Tribunal must proceed in accordance with the Social Security Tribunal Rules of Procedure` |  |
| reg 47 | src:340 | encoded | oa3-part2-reconsiderations.l4: `reg 47: the address to which the notice, request or other document must be addressed` |  |
| "Interest on Amounts Owing to Her Majesty" (heading) | src:342 | encoded | oa3-part2-interest.l4 | carried as the section heading `Interest on Amounts Owing to Her Majesty` of the module |
| reg 48(1), introductory words | src:343 | encoded | oa3-part2-interest.l4 | "The following definitions apply in this section": each definition is its own rule |
| reg 48(1) "average bank rate" | src:344 | encoded | oa3-part2-interest.l4: `reg 48(1): the average bank rate` | NOTHING for a month with no bank rate |
| reg 48(1) "bank rate" | src:345 | encoded | oa3-part2-interest.l4: `reg 48(1): the rate is a bank rate` |  |
| reg 48(1) "debt" | src:346-348 | encoded | oa3-part2-interest.l4: `reg 48(1): the amount is a debt` |  |
| reg 48(1) "demand for payment" | src:349 | encoded | oa3-part2-interest.l4: `reg 48(1): the document is a demand for payment` |  |
| reg 48(1) "due date" | src:350-352 | encoded | oa3-part2-interest.l4: `reg 48(1): the due dates of the debt` | several with a schedule, one 120 days after the demand without |
| reg 48(2) | src:353 | fork | oa3-part2-interest.l4: `reg 48(2): interest is payable on the debt` | F-48(2): the day the section comes into force is an input |
| reg 48(3) | src:354 | fork | oa3-part2-interest.l4: `reg 48(3): the first day on which interest accrues`, `reg 48: interest accrues on the debt on the day` | F-48(3): the due date itself accrues |
| reg 48(4) | src:355 | fork | oa3-part2-interest.l4: `reg 48(4): the rate of interest for the month, in per cent a year`, `reg 48(4): the interest accrued on the debt in the month`, `reg 48(4): the amount of the debt at the end of the month, with the interest of the month compounded` | F-48(4): the daily rate divides by the days of the calendar year; nothing is rounded |
| reg 48(5) | src:356 | encoded | oa3-part2-interest.l4: record `reg 48: Facts about the accrual of interest on a debt` and `reg 48: interest accrues on the debt on the day` | pending periods are Calendar spans |
| reg 48(6) | src:357-366 | fork | oa3-part2-interest.l4: `reg 48(6): the day on which the accrual of interest ceases` | F-48(6): the ceasing day is the last day interest accrues |
| reg 48(7) | src:367-371 | encoded | oa3-part2-interest.l4: `reg 48(7): the Minister may remit the interest payable under this section in whole or in part` |  |
| Schedule (heading and header row) | src:373-374 | encoded | oa3-part1-agreements.l4 | carried as the section heading `SCHEDULE (Section 22.01)`; the header row names the two fields of the record |
| Schedule rows (44 countries) | src:375-418 | encoded | oa3-part1-agreements.l4: `reg 22.01: the Schedule` | 44 rows, generated from the source lines by script |

## Fork register

26 forks.
Each entry gives the readings seen, the reading taken, and the text that licenses it.
Where I looked: every "or" and "and" list, every "within", "before", "after" and "on or after" period, every defined term that names a month or a day, every "forthwith" and "immediately", and every place the text defers to the Act or to something outside the Regulations.

| fork | provision | readings seen | reading taken | what licenses it |
| --- | --- | --- | --- | --- |
| F-2(2) | reg 2(2) | (A) residence and presence on a day strictly before the date of union; (B) the day of union counts | (A) | "prior to the date of union"; the date itself is not stated in the Regulations, so it is an input |
| F-2(3) | reg 2(3) | (A) "on a casual or temporary basis or under a student employment program" qualifies both "employed in" and "whose services are required by"; (B) only the second | (A) | one sentence with one closing phrase after a comma |
| F-5(1)(e) | reg 5(1)(e) | (A) with no date specified in writing, that limb drops out of "the latest of"; (B) the Regulations give no effective day | (A) | (e) "the date specified in writing by the applicant" is listed with (c) and (d) as one of the days the latest of which counts; an applicant need not specify one |
| F-5(2) | reg 5(2) | (A) "an applicant mentioned in subsection (1)" is one for whom both (1)(a) and (1)(b) hold; (B) any applicant for a pension | (A); with (1)(b) failing the Regulations give no day (NOTHING) | (1) names the applicant in (a) and the approval in (b); compare reg 12(2) and (3), written without that reference |
| F-5(2)(d) | reg 5(2)(d) | (d) names "the month immediately before the date specified": (A) the first day of that month; (B) its last day; (C) the same day number in the month before | (A), the earliest day the phrase can mean | the text names a month, not a day; (a) to (c) name days |
| F-6 | reg 6 | (A) an entitlement of nothing is not "an amount that does not exceed $2" for the purpose of paying $2; (B) it is | (A) | "is entitled ... to an allowance in an amount that does not exceed $2": a person entitled to nothing is entitled to no allowance |
| F-8(3) | reg 8(3) | the ratio of two index figures has more than four digits after the point: (A) drop to four digits, then round on the fourth; (B) round on the fourth digit of the exact ratio | (A); the two give the same result, because a half-up decision on the fourth digit depends only on that digit | "a decimal number represented by four digits after the decimal point" does not say what to do with a longer one |
| F-9(2) | reg 9(2) | "where the quotient ... contains a fraction that is less than 1": (A) every quotient is rounded to one decimal place (its fractional part is always less than 1); (B) only a quotient below 1 | (A) | the average index is about 159, so (B) would round nothing and the rule would never apply to an index |
| F-12 | reg 12(1) to (3) | (A) (2) and (3) apply whenever their own condition holds, whenever the Minister approves; (B) they inherit (1)'s condition that the approval comes after the month of receipt | (A); (1) answers only when neither (2) nor (3) applies and the approval is after the month | (1) is "subject to subsections (2) and (3)"; (2) and (3) open with "where" and their own condition |
| F-17 | reg 17 | (A) "the filing due date has passed" is true on the day after the due date; (B) on the due date | (A); the due date of last year's return is an input, because the Regulations do not state it | "for which the filing due date has passed" |
| F-21 | reg 21(1) to (5.3) | the deeming limbs meet: (A) (2), (2.1) and (5.3) override the meaning of (1)(a), while (3), (4), (5.1) and (5.2) add to it; (B) a limb that adds can also override an exclusion | (A) | "notwithstanding subsection (1)" in (2.1); "deemed not to be living" in (2) and "deemed not to be resident" in (5.3); "considered" in (3) and (5.2) and "deemed not to have interrupted" in (4) and (5.1) |
| F-21(4) | reg 21(4)(a) | "of a temporary nature and does not exceed one year": (A) the last day is on or before the day one year after the first; (B) at most 365 days | (A) | "one year" is a calendar year, the keel's `a limit in years` |
| F-21(5.2) | reg 21(5.2) | whose residence the period of pensionable employment is a period of: (A) the person's who is resident in Canada; (B) the spouse's | (A) | "shall ... be considered to be a period of residence in Canada", read with the person "who is resident in Canada" |
| F-21(8) | reg 21(8)(b)(ii) | the returns are for "at least 40 of the years referred to in subparagraph (i), other than for 1969, 1970 and 1971": (A) those three years are left out of the count; (B) they count as satisfied | (A) | the grammar of "other than" |
| F-22(1) | reg 22(1) | (A) the facts are those of the applicable day, taken as inputs; (B) compute "deemed ... pursuant to subsection 21(4) or (5)" from the dates | (A) | the applicable day is named by sections 4(1), 19(2) and 21(2) of the Act, which are out of range |
| F-22.1 | reg 22.1(1)(d), (2) | (d) "more than six months": (A) a number of months, a fraction allowed; (B) days; (2)(a) "in effect on or after March 7, 1996": (A) an undertaking that ended on that day was in effect on it; (B) it must run past it | (A) for both | the text counts in months; "on or after" includes the day |
| F-25 | reg 25(1) to (4) | "forthwith" and "immediately" name no time: (A) compute the day the duty arises and take timeliness as a fact the person states; (B) pick a number of days | (A) | no number appears in the Regulations for either word; "within one month of his return" does carry one and is computed |
| F-26(2) | reg 26(2) | "any portion of the period of suspension during which the beneficiary was eligible": (A) counted in days, both ends of each span included; (B) in payment periods | (A) | "portion of the period" with no unit; the Regulations name no payment period here |
| F-27 | reg 27 | "in any amount that does not cause undue hardship": (A) the largest such amount is a fact stated; (B) a formula | (A) | the Regulations give no test of hardship |
| F-28.1 | reg 28.1(1)(b) | "prior to the expiration of one year after the day on which the consent is signed": (A) the anniversary day is within the year; (B) the record and consent must come before the anniversary day | (A) | a year after a day expires at the end of the anniversary day |
| F-29.1 | reg 29.1(2)(a) | "the 365-day period after the day on which the person is notified": (A) 365 days, so the last day is the notification day plus 365; (B) a year | (A) | the text says 365 days; in a leap year 365 days fall a day short of a year |
| F-38.1(2) | reg 38.1(2) | "On notification, the Social Security Tribunal shall so notify the Registrar of the Court and the Registrar shall add that person": (A) the Registrar's duty follows the Tribunal's notice; (B) it follows the Minister's | (A) | "On notification" follows the Tribunal's own duty to be notified under (1) |
| F-48(2) | reg 48(2) | the day "on which this section comes into force" is not stated | an input | no date in lines 1-418 |
| F-48(3) | reg 48(3) | "begins on the due date": (A) the due date itself accrues; (B) the day after | (A) | "begins on" |
| F-48(4) | reg 48(4) | "calculated daily and compounded monthly": (A) the annual rate over the days of the calendar year (365 or 366); (B) over 365; (C) over 360; the interest of the month is added to the debt at month end; nothing is rounded | (A) | no divisor is named; no rounding is stated |
| F-48(6) | reg 48(6) | "ceases on" a day: (A) that day is the last day interest accrues; (B) no interest on that day; where there is a payment schedule, the debt is run once for each portion, with that portion's due date and last accrual day | (A) | (a) says "the day before the day on which a payment is received", which would leave a day uncovered under (B) |

The forks that move a person's money are F-5(2), F-5(2)(d), F-6, F-12, F-28.1, F-29.1 and F-48(4).

## Cross-references out of my ranges

Every fact decided by a provision outside lines 1-418 is a plain input, commented `-- out of range: ...` where it is declared.
The "piece" column names the piece that holds the provision when it is one of the Act's, per the keel's register; it is not an import (nothing here imports another piece).

| cited | where it appears | taken as | piece |
| --- | --- | --- | --- |
| sections 3 to 5 of the Act (qualification for a pension) | reg 5(1), (2) | inputs: the Minister is satisfied; the day the applicant became qualified | Act |
| sections 5(2), 5(4), 11(3), 11(3.1) of the Act (deemed or waived applications) | regs 3(2), 5(3), 5(4), 10.1, 17 | inputs: that the Act deems or waives | Act |
| sections 5(2), 5(5), 11(3), 11(4), 19(4.1), 21(5), 21(5.1) of the Act | reg 20(2) | input: that the person is in one of those circumstances | Act |
| section 11 of the Act (the supplement) | regs 10, 10.1 | input: the Minister is satisfied the pensioner is eligible | Act |
| sections 19 and 21 of the Act (the allowance) and Part III | regs 6, 11, 12 | inputs: the allowance the person is entitled to; the day they became entitled | Act |
| sections 7(2), 7.1(1), 7.1(2), 12(2), 12.1(3), 22(4.2), 22.1(4) of the Act (the quarterly adjustment) | regs 7, 8 | inputs: the amount and ratio of each; the increase under 7.1(1) | Act |
| the Statistics Act (publication of the Consumer Price Index) | reg 9(1) | inputs: the monthly figures | outside |
| sections 4.1, 3(1)(c)(iii) and 4(1)(a) of the Act | regs 21(8), 22(2) | the prescribed information is a rule here; whether it is required is the Act's | Act |
| sections 4(1), 19(2), 21(2) of the Act (the applicable day for legal residence) | reg 22(1) | inputs: the facts on that day | Act |
| the immigration laws of Canada | reg 22(1)(a), (b)(ii) | inputs: the person was lawfully in Canada | outside |
| sections 9.3 and 18.2 of the Act | reg 26.1 | the keel's register item 11: `reg 26.1(1): the prescribed time within which a request for cancellation may be made` | Act |
| sections 11(8), 19(6.2), 21(9.1) of the Act | reg 22.1 | the events are returned for those sections to take | Act |
| section 40(1) of the Act (agreements) | regs 21(5.1) to (5.3), 22(1), 22.01 | inputs; the Schedule is encoded here | Act |
| sections 27.1, 28(1), 28(2) of the Act; section 55 of the Department of Employment and Social Development Act; the Federal Courts Act | regs 2(1), 29, 29.1, 38, 48(5), 48(6) | inputs: that a request, appeal or review is pending or decided | Act, outside |
| sections 36(2), 37(2), 37(2.02), 37(2.1), 37(4), 44.1 of the Act | regs 27, 28.1, 48 | inputs: the debt, the penalty, the remission | Act |
| section 33(1) of the Act ("public officer") | reg 2(3) | input: the person is employed in or required by a federal institution | Act |
| sections 6 of the Act and 28.2(5) of the Department of Employment and Social Development Act | regs 18(1), 18(4), 18.1 | inputs | Act, outside |
| the Canada Pension Plan; the Quebec Pension Plan | regs 14(e), 19, 21(8), 21(9) | inputs; the borrowed terms are asked as facts about each year | outside |
| the Income Tax Act and the Minister of National Revenue (the filing due date and returns filed) | regs 17, 21(8)(b) | input: the filing due date of last year's return; returns filed | outside |
| the Newfoundland Act (the date of union) | reg 2(2) | input: `the date of union of Newfoundland with Canada` | outside |
| the order or amendment that brought section 48 into force | reg 48(2) | input: `the day on which this section comes into force` | outside |
| the Bankruptcy and Insolvency Act; the Criminal Code | reg 22.1(1)(b), (c) | inputs: the sponsor is convicted or bankrupt | outside |
| the Unemployment Assistance Act; the Canada Assistance Plan | reg 4(2) | input: the person is or has been in receipt of assistance | outside |
| the Tax Court of Canada Act; the Social Security Tribunal Rules of Procedure | regs 2(1), 46 | names only | outside |
| the Department of Human Resources Development Act; the Plant Workers' Adjustment Program, the Fisheries Early Retirement Program, the Northern Cod Adjustment and Recovery Program | reg 14(h), (i) | the record field is an amount received under them | outside |

Names the keel's register fixes, and the oa3 rule that answers each (checked against the modules):

| register input | answered by |
| --- | --- |
| `the Consumer Price Index for the first adjustment quarter that relates to the payment quarter` | `reg 9: the Consumer Price Index for the first adjustment quarter that relates to the payment quarter` |
| `the Consumer Price Index for the second adjustment quarter that relates to the payment quarter` | `reg 9: the Consumer Price Index for the second adjustment quarter that relates to the payment quarter` |
| `the person resides in Canada` | `reg 21: the person resides in Canada for the purposes of the Act and these Regulations` |
| `the person is present in Canada` | `reg 21: the person is present in Canada for the purposes of the Act and these Regulations` |
| `the person is legally resident in Canada` | `reg 22(1): the person is legally resident in Canada` |
| `the prescribed time within which a request for cancellation may be made` | `reg 26.1(1): the prescribed time within which a request for cancellation may be made` |

## Needs from the core

Nothing blocks.
Two small helpers are defined in `oa3-helpers.l4` because the core has none for dates, labelled `oa3:` so that no other piece can clash: `oa3: the later of _ and _` and `oa3: the earlier of _ and _`.
A core rule for the later or earlier of two dates would let the rules of `oa3-part1-applications.l4`, `oa3-part1-payments.l4` and `oa3-part2-interest.l4` that use them drop them.
The core's `Party` has the Minister, the Social Security Tribunal and the Registrar of the Tax Court, but not the appellant, the Chief Judge of the Court, the judge appointed to hear a reference, or a person added as a party, which regs 38 to 47 speak of; as the keel's instruction 12 says, `oa3-part2-reconsiderations.l4` declares its own enumeration, `reg 38: Participant in the appeal or reference`, under its own label.
No module of the keel was edited.

## What the text turns out to say

1. The four rounding rules (regs 7, 8(2), 8(3), 9(2)) all decide on one dropped digit, with 5 or more rounding up; 245.754 rounds to 245.75 and 245.755 to 245.76. Asserted.
2. A nil entitlement is not raised to $2 by reg 6, which speaks of a person "entitled ... to an allowance in an amount that does not exceed $2"; one cent is. Asserted.
3. Reg 5(2)(d) names a month ("the month immediately before the date specified") where (a) to (c) name days; the encoding takes that month's first day. Asserted.
4. A pensioner who turned 65 before applying is paid from the latest of one year before the application, the 65th birthday, the day qualified and the (d) day, so retroactivity is capped at one year (reg 5(2)(a)); an applicant approved in the month the application was received has no effective day under reg 5, and the Regulations give no other. Asserted.
5. Reg 12(2) and (3) give a spouse or survivor retroactivity whenever the approval comes, but (1) applies only when the approval is after the month of receipt; for a person who is not within (2) or (3), approved in the month of receipt, the text gives no day. Asserted (NOTHING).
6. Reg 26.1 says the request is "no later than six months after the day on which payment ... begins"; from a month-end start the six months clamp (31 August 2020 to 28 February 2021). Asserted.
7. "In excess of one month" in reg 25(1) is measured from the day of leaving; from 31 January 2020 the month ends on 29 February, so 29 February is not in excess and 1 March is. Asserted.
8. The "365-day period" of reg 29.1(2)(a) is counted in days: notified on 1 January 2020, the period ends on 31 December 2020 and a request on 1 January 2021 is after it, while for a notice on 1 January 2021 the period ends a year to the day later. Asserted.
9. Reg 24(1)(b) applies "where the Minister is not satisfied that any person or agency is so authorized": a person authorized under (a) always comes before an appointee under (b). Asserted.
10. Reg 48(6)(a) fixes the ceasing day as "the day before the day on which ... a payment ... is received"; read with "ceases on", a payment on 11 January ends accrual after 10 January. Asserted.
11. Reg 48(4) names no divisor; with the days of the calendar year, February 2020 (29 days of a 366-day year) and February 2021 (28 days of 365) accrue at different daily rates. Asserted.
12. Reg 28.1(1)(d) says the amount deducted "exceeds $50": $50 does not, $50.01 does. Asserted.
13. The Schedule's "Agreement" column runs two instruments together without a separator for Australia ("... signed at Canberra on July 4, 1988Protocol amending ..."), Guernsey and Jersey share one agreement text, the Spain row names a Protocol to a Convention, and the United Kingdom row a Memorandum of Understanding; each cell is kept as printed. Asserted for the row count (44) and for the Barbados and New Zealand rows.
14. 16 provisions are shown as repealed in this text: reg 2(1) "applicant", reg 2(1) "Board", reg 2(1) "Minister", reg 2(1) "Regional Director", reg 2(1) "Review Committee", reg 2(1) "Review Tribunal", reg 2(1) "secretary", reg 2(1.1), reg 19.1, reg 25(5), reg 28, reg 28.2, reg 28.3, reg 28.4, regs 30 to 37, reg 43.
15. Reg 17 and reg 21(8)(b)(ii) both use the phrase "the most recent calendar year for which the filing due date has passed", and both depend on a due date that the Regulations do not state.
16. Reg 22.1(2) tests two things on or after 7 March 1996, the undertaking and an event; an undertaking that ended on 7 March 1996 itself is taken to have been in effect that day. Asserted.

## What the stable binary does not accept

All measured on 1.6.98 while writing this encoding; none is a defect of the Regulations.

- **`NOT a AND NOT b` is read as `NOT (a AND NOT b)`.** Measured: `NOT TRUE AND NOT TRUE` evaluates to TRUE. Write `(NOT (a)) AND (NOT (b))`. It was the cause of a defect in the reg 21(8)(b) filter, fixed before this check.
- **`f x's y` is read as `(f x)'s y`.** Write `f (x's y)`. The parse error that follows is reported at the nearest `(` ("unexpected (") and does not name the genitive, so it reads as a layout error; it happened in `oa3-part2-interest.l4`.
- **A continuation line that starts with `(` at the same indent as the line above it begins a new expression.** `append a` on one line and `(append b c)` on the next failed to parse. Write the whole call on one line, or name the pieces in a `WHERE`.
- **A mixfix call inside another call's arguments must be parenthesised.**
- **No `\x -> ...` lambda (a lexer error) and no `length` (not found).** Use `GIVEN y YIELD ...` or a `WHERE` helper, and `count` of a list for its length; `count (filter f list)` counts the matches.
- **An `#ASSERT` over a DEONTIC value fails even against itself**, so duties are BOOLEAN, DATE or list rules; see the Seat section.
- **A `WHERE` helper's body lines must be indented consistently.** A mismatch in the generated seat file was reported as a parse error.

## What check.sh prints

Run as `L4=<the 1.6.98 binary> L4_TARGET=unstable ./check.sh` from this directory, on the tree as delivered; it exited 0.
The 939 satisfied are the 718 assertions of the ten test files and the 221 of the seat cases; the layer-1 modules and the seat carry none.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
oa3-cases-seat.l4                              0       221       0        0         0
oa3-helpers.l4                                 0         0       0        0         0
oa3-part1-agreements.l4                        0         0       0        0         0
oa3-part1-amounts.l4                           0         0       0        0         0
oa3-part1-applications.l4                      0         0       0        0         0
oa3-part1-evidence.l4                          0         0       0        0         0
oa3-part1-income.l4                            0         0       0        0         0
oa3-part1-payments.l4                          0         0       0        0         0
oa3-part1-residence.l4                         0         0       0        0         0
oa3-part2-interest.l4                          0         0       0        0         0
oa3-part2-reconsiderations.l4                  0         0       0        0         0
oa3-regs-interpretation.l4                     0         0       0        0         0
oa3-seat.l4                                    0         0       0        0         0
oa3-tests-agreements.l4                        0        36       0        0         0
oa3-tests-amounts.l4                           0        52       0        0         0
oa3-tests-applications.l4                      0        88       0        0         0
oa3-tests-evidence.l4                          0        66       0        0         0
oa3-tests-income.l4                            0        16       0        0         0
oa3-tests-interest.l4                          0        90       0        0         0
oa3-tests-interpretation.l4                    0        34       0        0         0
oa3-tests-payments.l4                          0        99       0        0         0
oa3-tests-reconsiderations.l4                  0        79       0        0         0
oa3-tests-residence.l4                         0       158       0        0         0
oas-core-income.l4                             0         0       0        0         0
oas-core-measures.l4                           0         0       0        0         0
oas-core-pension.l4                            0         0       0        0         0
oas-core-periods.l4                            0         0       0        0         0
oas-core-terms.l4                              0         0       0        0         0
oas-core.l4                                    0         0       0        0         0
TOTAL (29 modules)                             0       939       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

## Before this is worth relying on

- A lawyer has not read these rules against the official consolidation: the source is an unofficial reproduction, and every `src:` quotation is compared with that reproduction only.
- The Act's own provisions (what makes a person qualified for a pension, entitled to an allowance, resident for ten years, the amounts) belong to the pieces that encode the Act; this piece takes them as inputs, and the seat's questions about "the day you became qualified" and "the day you became entitled" ask the person for a conclusion the Act reaches. A composition with those pieces should compute them from the person's history.
- The 26 forks above are readings; the ones that move a person's money are listed after the register, and they should be ruled by someone with authority over the text.
- Reg 25's "forthwith" and "immediately" are measured by no number; the seat asks whether the person gave notice forthwith, which is itself a judgment.
- The seat is not deployed; its question names, input names and types are a published interface once it is, and changing them is a breaking change.
- Nothing here checks the encoding against a real decision of the Minister; the cases are worked by hand from the words of the Regulations.
