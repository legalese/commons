# NOTES: Employment Insurance Regulations, piece er5 (Part IV pilot projects and Part V administrative provisions)

Written by the piece agent `er5` (Sonnet 5.5) on 2026-10-24, for the encoding of the Employment Insurance Act (S.C. 1996, c. 23) and the Employment Insurance Regulations (SOR/96-332) from the plain-text renderings in the lead's inputs.
This piece is lines 1394 to 1708 of `SOR-96-332.txt`: the Regulations' Part IV (Pilot Projects, regs 77 to 77.999) and Part V (Administrative Provisions, regs 78 to 92).

**The text.**
It is the plain-text rendering, made by a converter script, of the Justice Laws consolidation of the Employment Insurance Regulations, SOR/96-332, current to 2026-09-30, last amended 2026-04-01.
It is not the official text and nothing here claims to be verified against the official text; the French version, equally authoritative, is not read, and the converter drops historical notes and footnotes.
Every rule in this piece comes from the Regulations; the Act is named only where a regulation refers to it.
Every `src:N` in the modules is a line of `SOR-96-332.txt`, and `python3 -I srcrefs.py check --refs SOR-96-332.txt er5-*.l4` prints 0 problems (see "What check.sh prints").

**What is in the folder.**
Layer 1, twelve modules that follow the Regulations' own groups, each with a test file: `er5-pilot-claims` (regs 77, 77.1), `er5-pilot-weeks` (77.2, 77.91, 77.92, 77.992, 77.993), `er5-pilot-rate` (77.7, 77.93), `er5-pilot-earnings` (77.8, 77.94, 77.95, 77.97, 77.99), `er5-pilot-elections` (77.96, 77.98, 77.991), `er5-pilot-hours` (77.994), `er5-pilot-24` (77.995 to 77.999), `er5-admin-reconsideration` (78 to 82, 83 to 87), `er5-admin-coverage-decision` (88), `er5-admin-sin` (89), `er5-admin-electronic-systems` (90, 91), `er5-admin-direct-deposit` (92); tests `er5-tests-<same suffix>.l4`.
Layer 2, `er5-seat.l4` (115 questions, grouped under `§§` headings in the text's order) and `er5-cases-seat.l4` (150 cases, at least one for every question).
The keel's `eia-core*.l4` are imported unchanged (`eia-core` only: `YMD`, `Period of days`, `the day ... falls within ...`, `the last day of n days after d`, `weeks as days`, `s 2(1) the Sunday that begins the week containing`); this piece defines no name that the core defines.

**Dates.**
Nothing in lines 1394 to 1708 is the date of enactment or making of the Regulations, or a commencement rule for the Regulations as a whole, so no date of that kind is carried and no rule takes a rule date.
Each pilot project states its own window as dates (benefit period established, week claimed, claim made); those are carried as constants with an `@ref`, and the date of the fact (the benefit period, the week) is an input to every rule.
Three sections refer to "the day on which this section comes into force" or "ceases to have effect" and never state it (reg 77.1, reg 77.994 and reg 77.999): each is a DATE input and is listed under "What the text turns out to say".

## Seat

**The seat** is the one the brief gives: a person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission.
Officials have no seat: the Commission appears only as the party whose duty or power the person is owed or exposed to (the Jural relations table says which).

**Why this seat suits this range.**
Part IV is a run of pilot projects, each of which changes one thing for a claimant who falls inside its window: the maximum weeks, the rate, how much may be earned, how earnings are deducted, how many hours count, the waiting period, the regional rate.
Part V says what a claimant must do or can expect: the content of a request for reconsideration, when benefits are held back while the Commission appeals, when to give a Social Insurance Number, what a claim by telephone or online amounts to, and how direct deposit works.
Both are naturally asked from the claimant ("Am I included in ...?", "By what day must I ...?", "How many weeks can I be paid ...?").

**How it is built.**
Every question has `@export`, and every input has an `@desc` worded as the person would be asked.
The questions call the layer-1 rules and build the periods and the records those rules expect from plain inputs in a `WHERE`; no rule is restated.
A fact that is the Commission's judgment (that good cause is shown, that a form and manner is approved, that it has become aware of a failure, that it has decided to terminate or to waive) is asked as a yes/no fact on the Commission's side.
A figure that another provision gives (a Schedule II.x table, the periods of s 22(2) and s 23(2), the rate of weekly benefits) is asked for as that figure.
A day the text never states (the days regs 77.1, 77.994 and 77.999 come into force or cease to have effect) is asked as a date.
Where the text does not answer, the question returns NOTHING (a `MAYBE`) and a case asserts it: reg 79 ("without delay"), the maximum weeks outside a project, a deadline where no notification was issued.

**The groups** (every `§§` heading says in a comment whether it arises only in a situation the person may not be in, so a form can ask "Has this happened to you?" first): one group per pilot project or pair of projects in the text's order (regs 77, 77.1, 77.2, 77.7 and 77.93, 77.8 and 77.94, 77.91, 77.92, 77.95/77.97/77.99, 77.96/77.98/77.991, 77.992, 77.993, 77.994, 77.996 to 77.999) and then regs 78 and 79, 80 to 82, 88, 89, 90 and 91, 92.
Nearly every pilot project has ended; a question about a spent project answers correctly for the benefit period or the week it governed, and for any other date says that the project does not apply.

**What the seat asks nothing about, and why** (each is still encoded in layer 1 or marked inert in the coverage table):
the purpose clauses (they decide nothing); reg 77(2) "condition of entitlement" (a definition that points at s 49(1) of the Act); the repealed regulations; the headings; reg 77(7) and the cessation days of regs 77.8(4), 77.94(4), 77.95(5), 77.97(5), 77.99(5) (they are inside the questions that use them rather than questions of their own).
The questions are listed one per line in the final report.

**The groups of `er5-seat.l4` and the number of questions in each** (115 in all):

| group | questions |
| --- | --- |
| Reg 77 -- Pilot Project No. 1, periodic claims (ended in 1999) | 7 |
| Reg 77.1 -- Pilot Project No. 5, choosing not to be paid | 5 |
| Reg 77.2 -- Pilot Project No. 6, increased weeks of benefits (ended in 2006) | 2 |
| Regs 77.7 and 77.93 -- Pilot Projects No. 11 and No. 16, a rate based on the 14 highest weeks (ended in 2011 and 2013) | 6 |
| Regs 77.8 and 77.94 -- Pilot Projects No. 12 and No. 17, higher allowable earnings (ended in 2011 and 2012) | 4 |
| Reg 77.91 -- Pilot Project No. 14, extended benefit period and training incentive (ended in 2010) | 6 |
| Reg 77.92 -- Pilot Project No. 15, extended benefits (ended in 2012) | 4 |
| Regs 77.95, 77.97 and 77.99 -- Pilot Projects No. 18, 19 and 20, half of your earnings deducted (2012 to 2018) | 5 |
| Regs 77.96, 77.98 and 77.991 -- electing between the two methods of treating your earnings (2012 to 2018) | 18 |
| Reg 77.992 -- Pilot Project No. 21, increased weeks for seasonal workers (ended in 2021) | 4 |
| Reg 77.993 -- Pilot Project No. 22, additional weeks for seasonal workers (ended in 2024) | 2 |
| Reg 77.994 -- Pilot Project No. 23, additional hours after natural disasters (ended in 2025) | 2 |
| Regs 77.996 to 77.999 -- Pilot Project No. 24, measures for major changes in economic conditions (March 30, 2025 to October 10, 2026) | 10 |
| Regs 78 and 79 -- asking the Commission to reconsider a decision | 4 |
| Regs 80 to 82 -- benefits held back while the Commission appeals | 5 |
| Reg 88 -- benefits held back while a ruling on my insurable hours is pending | 2 |
| Reg 89 -- my Social Insurance Number | 10 |
| Regs 90 and 91 -- giving the Commission information and claiming by telephone or online | 9 |
| Reg 92 -- direct deposit of my benefits | 10 |


## Jural relations

Rights and duties come in pairs; each relation is stated once in layer 1, neutrally, and the table names the pair.
The layer-2 questions take, as plain inputs, the facts about the other party on which the text makes the relation depend (what the Commission has decided, whether it has been informed, whether it appealed, whether it is satisfied of good cause).

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind | the L4 rule |
| --- | --- | --- | --- | --- |
| reg 77(1), 77.1(1), 77.2(1), 77.7(1), 77.8(1), 77.91(1), 77.92(1), 77.93(1), 77.94(1), 77.95(1), 77.96(1), 77.97(1), 77.98(1), 77.99(1), 77.991(1), 77.992(1), 77.993(1), 77.994(1), 77.995 | none | none | a purpose clause: states why a project exists, creates no relation | the `... the purpose of Pilot Project No. N ...` STRING constants |
| reg 77(2) definitions | none | none | definitions | `er5-pilot-claims` `reg 77(2) condition of entitlement to benefits`, `reg 77(2) the period of eligibility ...` |
| reg 77(3) | the claimant (a claim to take part, if eligible) | the Commission (a duty to admit an eligible claimant who signs, read from (4)) | claim / duty | `er5-pilot-claims` `reg 77(3) the claimant is eligible to participate in Pilot Project No. 1` |
| reg 77(4) | the claimant (a power to take part by signing the form) | the Commission (liability to the claimant's participation) | power / liability | `er5-pilot-claims` `reg 77(4) the claimant participates in Pilot Project No. 1` |
| reg 77(4)(b) | the Commission (a claim to be told) | the participant (a duty to notify as soon as possible) | claim / duty | `er5-pilot-claims` `reg 77(4)(b) the claimant must notify the Commission ...` |
| reg 77(5) | the participant (an immunity from the requirement to make periodic claims) | the Commission (a disability to require them) | immunity / disability | `er5-pilot-claims` `reg 77(5) the claimant is deemed to have made a claim for benefits for the week` |
| reg 77(6) | the Commission (a power to end participation) | the participant (a liability to have it ended) | power / liability | `er5-pilot-claims` `reg 77(6) the day as of which the claimant's participation is terminated` |
| reg 77(7) | none | none | a cessation rule: when (3)(a) stops applying | `er5-pilot-claims` `reg 77(7) paragraph 77(3)(a) is in force on the day` |
| reg 77.1(2) | none | none | who is included (status) | `er5-pilot-claims` `reg 77.1(2) the claimant is included in Pilot Project No. 5` |
| reg 77.1(3), (4)(a) | the included claimant (a power to choose not to be paid) | the Commission (a liability to the choice, and to the deeming) | power / liability | `er5-pilot-claims` `reg 77.1(3) the claimant is deemed to have proved ...` |
| reg 77.1(4)(b) | the Commission (a claim to repayment) | the claimant who chose after being paid, uninformed (a duty to repay) | claim / duty | `er5-pilot-claims` `reg 77.1(4)(b) the claimant must repay the benefits paid for the week` |
| reg 77.1(5) | the claimant (a power to rescind, and a claim to be paid) | the Commission (a liability to the rescission, and a duty to pay) | power / liability; claim / duty | `er5-pilot-claims` `reg 77.1(5) the claimant is to be paid the benefits to which they are entitled` |
| reg 77.1(6) | none | none | a counting rule: the weeks to which the project applies | `er5-pilot-claims` `reg 77.1(6) Pilot Project No. 5 applies to the week` |
| reg 77.2(2), 77.7(2), 77.8(2), 77.91(2), (3), 77.92(2), 77.93(2), 77.94(2), 77.95(2), 77.97(2), 77.99(2), 77.992(2), 77.993(2) | none | none | who is included in a project (a status that the rules below attach claims to) | the `... the claimant is included in Pilot Project No. N` rules |
| reg 77.2(3), 77.92(4), 77.992(5) | the included claimant (a claim to the weeks the Schedule table gives) | the Commission (a duty to pay them) | claim / duty | `er5-pilot-weeks` the `... the maximum number of weeks for which benefits may be paid in the benefit period` rules |
| reg 77.91(4), (5) | the included claimant (a claim to the extension and the added weeks) | the Commission (a duty to allow them) | claim / duty | `er5-pilot-weeks` `reg 77.91(4) ...`, `reg 77.91(5) ...` |
| reg 77.91(6) | the included claimant (a claim to the job-search period) | the Commission (a duty to grant it) | claim / duty | `er5-pilot-weeks` `reg 77.91(6) ...` (two rules) |
| reg 77.91(7) | the Commission (a power to end the added weeks when a ground to end the referral exists) | the claimant (a liability to lose them) | power / liability | `er5-pilot-weeks` `reg 77.91(7) the Sunday on which subsection 77.91(5) ceases to apply` |
| reg 77.92(3) | the public, including the claimant (a claim to a published notice) | the Commission (a duty to publish it as soon as possible) | claim / duty | `er5-pilot-weeks` `reg 77.92(3) the Commission must publish a notice in the Canada Gazette and on its website` |
| reg 77.992(3), (4) | none | none | counting rules for criteria (c) and (d) | `er5-pilot-weeks` `reg 77.992(3) ...`, `reg 77.992(4) ...` |
| reg 77.7(3), 77.93(3) | the included claimant (a claim to a rate worked on the 14 highest weeks) | the Commission (a duty to work it so) | claim / duty | `er5-pilot-rate` `reg 77.7(3)(e), (f) and reg 77.93(3)(e), (f) ...`, `... (a), (d) ...`, `... (b), (c) ...` |
| reg 77.7(4), 77.93(4) | the claimant and the employer (a claim to an allocation by pay period, or by evidence) | the Commission (a duty to allocate) | claim / duty | `er5-pilot-rate` `reg 77.7(4)(a) ...`, `reg 77.7(4)(b) ...`, `reg 77.7(4) and reg 77.93(4) ...` |
| reg 77.8(3), 77.94(3) | the included claimant (a privilege to earn up to the amount without deduction) | the Commission (a no-right to deduct below it) | privilege / no-right | `er5-pilot-earnings` `reg 77.8(3) and reg 77.94(3) the maximum allowable earnings`, `reg 77.8(3) the maximum allowable earnings for the week ...` |
| reg 77.8(4), 77.94(4), 77.95(5), 77.97(5), 77.99(5) | none | none | cessation rules: until when each section has effect | `er5-pilot-earnings` `reg 77.8(4) the section has effect for the week` |
| reg 77.95(3), (4), 77.97(3), (4), 77.99(3), (4) | the Commission (a power to deduct 50% up to 90% of the weekly figure and all above it) | the included claimant (a liability to the deduction, and a claim that no more is deducted) | power / liability | `er5-pilot-earnings` `reg 77.95(3), reg 77.97(3) and reg 77.99(3) ...`, `reg 77.95(4), reg 77.97(4) and reg 77.99(4) ...` |
| reg 77.96(2), 77.98(2), 77.991(2) | the claimant (a power to elect the allowable-earnings method) | the Commission (a liability to the election) | power / liability | `er5-pilot-elections` `reg 77.96(2) the claimant may elect`, `reg 77.98(2) the claimant may elect`, `reg 77.991(2) ...` |
| reg 77.96(3), 77.98(5), 77.991(5) | the Commission (a claim to be told by the deadline) | the electing claimant (a duty to inform the Commission by the deadline) | claim / duty | `er5-pilot-elections` `reg 77.96(3) ...`, `reg 77.98(5) ...`, `reg 77.991(5) ...` |
| reg 77.96(4), 77.98(6), 77.991(6) | the claimant (a power to have a late election treated as in time, on good cause) | the Commission (a liability to that, if it is satisfied of good cause) | power / liability | `er5-pilot-elections` `reg 77.96(4), reg 77.98(6) and reg 77.991(6) ...` |
| reg 77.96(5) to (7), 77.98(7), (8) | the Commission (a power to apply the 50% method to the next benefit period of a claimant who did not elect) | the claimant (a liability to it; no power to elect for the next period) | power / liability; disability | `er5-pilot-elections` `reg 77.96(5), (6) and (7) ...`, `reg 77.98(7) and (8) ...` |
| reg 77.96(3) (deemed election), 77.98(3), (4), 77.991(3), (4) | the claimant (a power: an election extends to later portions) | the Commission (a liability to it) | power / liability | `er5-pilot-elections` `reg 77.98(3) ...`, `reg 77.98(4) ...`, `reg 77.991(3) ...`, `reg 77.991(4) ...` |
| reg 77.96(8), 77.98(9), 77.991(7) | the Commission (an immunity from appeal or reconsideration of its decision on an election) | the claimant (a disability to appeal or ask for reconsideration) | immunity / disability | `er5-pilot-elections` `reg 77.96(8)(a) ...`, `reg 77.96(8)(b) ...`, `reg 77.98(9) ...`, `reg 77.991(7) ...` |
| reg 77.994(3), (4) | the referred claimant (a claim to 300 additional hours) | the Commission (a duty to count them) | claim / duty | `er5-pilot-hours` `reg 77.994(3) ...`, `reg 77.994(4) ...`, `reg 77.994(2) to (4) ...` |
| reg 77.994(5) | the claimant (a claim to have the hours count for the listed provisions) | the Commission (a duty to count them) | claim / duty | `er5-pilot-hours` `reg 77.994(5) ...` (two rules) |
| reg 77.996 | the Commission (a power to waive the waiting period) | the claimant (a liability to its being waived or not) | power / liability (a discretion) | `er5-pilot-24` `reg 77.996 the Commission may waive the waiting period`, `reg 77.996 the waiting period is waived` |
| reg 77.997 | the claimant (an immunity from the counting of lay-off or separation earnings) | the Commission (a disability to count them) | immunity / disability | `er5-pilot-24` `reg 77.997 ...` |
| reg 77.998 | the claimant (a claim to the deemed regional rate) | the Commission (a duty to apply it) | claim / duty | `er5-pilot-24` `reg 77.998 the regional rate of unemployment that applies to the claimant` |
| reg 77.999(1) | none | none | a definition: long-tenured worker | `er5-pilot-24` `reg 77.999(1) long-tenured worker` |
| reg 77.999(2) to (4) | the long-tenured claimant (a claim to the 20-week extension and the added weeks) | the Commission (a duty to allow them) | claim / duty | `er5-pilot-24` `reg 77.999(2) ...`, `reg 77.999(3) ...`, `reg 77.999(4)(a) ...`, `reg 77.999(4)(b) ...` |
| reg 77.999(5) | the claimant (an immunity of the added weeks from ending by reason only of ceasing to be long-tenured) | the Commission (a disability to end them for that reason) | immunity / disability | `er5-pilot-24` `reg 77.999(5) the additional weeks are still payable` |
| reg 78(1), (2) | the claimant (a power to have a decision reconsidered, on a request that has the content and is filed as required) | the Commission (a liability to reconsideration, under s 112 of the Act) | power / liability, with its conditions | `er5-admin-reconsideration` `reg 78(1) ...`, `reg 78(2) ...` |
| reg 79 | the person who asked (a claim to a decision without delay) | the Commission (a duty to decide without delay) | claim / duty | `er5-admin-reconsideration` `reg 79 the Commission must render its decision on the request without delay`, `reg 79 the Commission has rendered its decision without delay` |
| reg 80, 81, 82(1), (2) | the Commission (a power to stop benefits being payable by appealing) | the claimant (a liability to have them held back) | power / liability | `er5-admin-reconsideration` `reg 80 ...`, `reg 81 ...`, `reg 82(1) ...`, `reg 82(2) ...`, `reg 82(1) and (2) the claim is caught by the decision` |
| reg 88(1) | the Commission and the Minister (an immunity from payment for hours under ruling until the rulings are final) | the claimant (a disability to be paid before then) | immunity / disability | `er5-admin-coverage-decision` `reg 88(1) ...` (two rules) |
| reg 88(2) | the claimant who qualifies on other hours (an immunity from (1)) | the Commission (a disability to withhold) | immunity / disability | `er5-admin-coverage-decision` `reg 88(2) subsection 88(1) does not apply` |
| reg 89(1), (3), (4), (6) | the Commission, and the employer for (3), (4), (6) (a claim to be told or asked) | the person employed (a duty to apply, or to inform the employer) | claim / duty | `er5-admin-sin` `reg 89(1) ...`, `reg 89(3) and (4) ...`, `reg 89(6) ...` |
| reg 89(2), (5) | the Commission (a claim that the employer ask, and report) | the employer (a duty to ask the employee, and to report when it cannot ascertain the number) | claim / duty | `er5-admin-sin` `reg 89(2) ...`, `reg 89(5) ...` |
| reg 90 | the Commission (a claim to information in a form and manner it approves) | whoever gives it information (a duty to give it so) | claim / duty | `er5-admin-electronic-systems` `reg 90 ...` (two rules) |
| reg 91(1), (2), (3) | the claimant who claims by telephone or electronically (a power: deemed claim, deemed responses, deemed signature, deemed day) | the Commission (a liability to them) | power / liability | `er5-admin-electronic-systems` `reg 91(1) ...`, `reg 91(1)(a) ...`, `reg 91(1)(b) ...`, `reg 91(2) ...`, `reg 91(3) ...` |
| reg 91(4), 92(6) | the Commission (a power: ss 38 and 135 reach a declaration made electronically or about payment) | the declarant (a liability to them) | power / liability (for greater certainty) | `er5-admin-electronic-systems` `reg 91(4) ...`; `er5-admin-direct-deposit` `reg 92(6) ...` |
| reg 91(5), 92(7) | the Commission (a power to refuse a person who knowingly interferes access to the systems) | that person (a liability to be refused) | power / liability | `er5-admin-electronic-systems` `reg 91(5) ...` (two rules); `er5-admin-direct-deposit` `reg 92(7) ...` (two rules) |
| reg 92(1) | none | none | incorporates sections of another instrument | `er5-admin-direct-deposit` `reg 92(1) the sections of the Direct Deposit Regulations that apply ...` |
| reg 92(2) | the claimant (a claim to direct deposit, subject to (7)) | the Commission (a duty to deposit) | claim / duty | `er5-admin-direct-deposit` `reg 92(2) the claimant's benefits are to be deposited directly to their bank account` |
| reg 92(3) | the Commission (a claim that the data be accurate) | the claimant (a duty of accuracy) | claim / duty | `er5-admin-direct-deposit` `reg 92(3) ...` |
| reg 92(4) | the claimant (a presumption of payment in their favour) | the Commission (a burden to bring contrary evidence) | a rule of evidence, not a Hohfeldian relation | `er5-admin-direct-deposit` `reg 92(4) ...` |
| reg 92(5) | the Commission (a claim to be notified) | the claimant who wishes to end the deposit (a duty to notify) | claim / duty | `er5-admin-direct-deposit` `reg 92(5) ...` (two rules) |
| reg 92(8) | the Commission (a power to redirect the deposit when the institution reports a change) | the claimant (a liability to it, unless they advise otherwise) | power / liability | `er5-admin-direct-deposit` `reg 92(8) the Commission may redirect the deposit of benefits` |
| regs 77.3 to 77.6, 77.9, 83 to 87 | none | none | repealed | `er5-pilot-weeks` `regs 77.3 to 77.6 ...`; `er5-pilot-earnings` `reg 77.9 ...`; `er5-admin-reconsideration` `regs 83 to 87 ...` |

## Coverage table

The table is in the text's order, one row per section or per subsection or paragraph that differs in disposition or rule, plus one row per heading.
Counts: 170 rows in all: 111 `encoded`, 27 `fork`, 29 `inert`, 3 `repealed or blank in this text`.
Headings in my ranges: 29 (Part IV; 21 sub-headings of Part IV, one of them the sub-heading "Purpose" and others under reg 77.995 to 77.999; Part V; 6 sub-headings of Part V), each with a row.
Sections in my ranges: 43 (77, 77.1, 77.2, 77.3 to 77.6, 77.7, 77.8, 77.9, 77.91 to 77.99, 77.991 to 77.999, 78 to 92), each with at least one row.
Every `inert` row is a heading, which is a title (the brief's "pure citation or title"): no operative provision of this range is `inert`.
The `fork` rows point at the entry of the fork register that names the reading taken.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Heading "PART IV Pilot Projects" | src:1394 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| Heading "Pilot Project for Exemption from the Requirement to Make Periodic Claims for Benefits for Weeks of Unemployment in the Benefit Period" | src:1396 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77(1) | src:1397 | encoded | `er5-pilot-claims` `reg 77(1) the purpose of Pilot Project No. 1` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. The Commission's duty to establish the project is carried by the string. |
| reg 77(2) "condition of entitlement to benefits" | src:1399 | encoded | `er5-pilot-claims` `reg 77(2) condition of entitlement to benefits` | Defined by pointing at s 49(1) of the Act (piece ei2): the rule takes that as a BOOLEAN input. |
| reg 77(2) "period of eligibility" (a), (b) | src:1400-1404 | fork | `er5-pilot-claims` `reg 77(2) the period of eligibility for the benefits referred to in subparagraph 77(3)(d)(i)`, `... (ii)` | Fork F-reg77a: which of (a)(i) and (a)(ii) goes with which benefit. |
| reg 77(3) | src:1405-1411 | fork | `er5-pilot-claims` `reg 77(3) the claimant is eligible to participate in Pilot Project No. 1` | Paragraph (a) is conditional on reg 77(7); the 'every week' limb (d) is one fact (fork F-reg77d). |
| reg 77(4) | src:1412-1414 | fork | `er5-pilot-claims` `reg 77(4) the claimant has signed the form with the agreements it requires`, `reg 77(4) the claimant participates in Pilot Project No. 1`, `reg 77(4)(b) the claimant must notify the Commission of the condition as soon as possible` | Fork F-reg77c: signing the form is read as what makes a claimant a participant. 'As soon as possible' has no number of days. |
| reg 77(5) | src:1415 | encoded | `er5-pilot-claims` `reg 77(5) the claimant is deemed to have made a claim for benefits for the week` |  |
| reg 77(6) | src:1416 | encoded | `er5-pilot-claims` `reg 77(6) the day as of which the claimant's participation is terminated` | The Commission's choice to terminate is a BOOLEAN input. |
| reg 77(7) | src:1417 | fork | `er5-pilot-claims` `reg 77(7) paragraph 77(3)(a) is in force on the day` | Fork F-reg77b: which day eligibility is tested; ceasing on April 1, 1997 read as the first day the paragraph is out of force. |
| Heading "Pilot Project Extending the Benefit Period of Certain Claimants" | src:1419 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.1(1) | src:1420 | encoded | `er5-pilot-claims` `reg 77.1(1) the purpose of Pilot Project No. 5` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.1(2) | src:1421-1424 | encoded | `er5-pilot-claims` `reg 77.1(2) the claimant is included in Pilot Project No. 5` | The days the section comes into force and ceases to have effect are not stated: inputs. |
| reg 77.1(3) | src:1425 | fork | `er5-pilot-claims` `reg 77.1(3) the claimant is deemed to have proved that they are not entitled to benefits for the week` | Fork F-reg77.1: a choice is read as having no effect once rescinded. Together with (4)(a) and (5). |
| reg 77.1(4)(a) | src:1427 | encoded | `er5-pilot-claims` `reg 77.1(3) ...` (the informed-beforehand input) | (4)(a) is the exception to (3) for a claimant informed before being paid. |
| reg 77.1(4)(b) | src:1428 | fork | `er5-pilot-claims` `reg 77.1(4)(b) the claimant must repay the benefits paid for the week` | Fork F-reg77.1: a rescinded choice carries no repayment. |
| reg 77.1(5) | src:1429 | encoded | `er5-pilot-claims` `reg 77.1(5) the claimant is to be paid the benefits to which they are entitled` |  |
| reg 77.1(6) | src:1430 | encoded | `er5-pilot-claims` `reg 77.1(6) Pilot Project No. 5 applies to the week` | Weeks are read from the Sunday of the week in which the section comes into force and of the week in which it ceases. |
| Heading "Pilot Project Relating to Increased Weeks of Benefits" | src:1432 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.2(1) | src:1433 | encoded | `er5-pilot-weeks` `reg 77.2(1) the purpose of Pilot Project No. 6` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.2(2) | src:1434-1436 | encoded | `er5-pilot-weeks` `reg 77.2(2) the claimant is included in Pilot Project No. 6` | Schedule II.1 (piece er6) is a BOOLEAN input. The period runs June 6, 2004 to June 4, 2006. |
| reg 77.2(3) | src:1437 | encoded | `er5-pilot-weeks` `reg 77.2(3) the maximum number of weeks for which benefits may be paid in the benefit period` | Schedule II.2 (piece er6) is taken as the NUMBER the table gives; NOTHING outside the project. |
| regs 77.3, 77.4, 77.5, 77.6 | src:1438-1441 | repealed or blank in this text | `er5-pilot-weeks` `regs 77.3 to 77.6 are repealed and therefore not encoded` | Each reads only [Repealed, SOR/2011-127, s. 1], [Repealed, SOR/2016-206, s. 7] or [Repealed, SOR/2010-214, s. 1]. |
| Heading "Pilot Project for Calculating Benefit Rate Based On Claimant’s 14 Highest Weeks of Insurable Earnings (2)" | src:1443 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.7(1) | src:1444 | encoded | `er5-pilot-rate` `reg 77.7(1) the purpose of Pilot Project No. 11` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.7(2) | src:1445 | encoded | `er5-pilot-rate` `reg 77.7(2) the claimant is included in Pilot Project No. 11` | Schedule II.8 (piece er6) is a BOOLEAN input. |
| reg 77.7(3)(a), (d) | src:1447, 1450 | encoded | `er5-pilot-rate` `reg 77.7(3)(a), (d) and reg 77.93(3)(a), (d) ...` | One rule for the paragraphs of both regs. |
| reg 77.7(3)(b), (c) | src:1448-1449 | encoded | `er5-pilot-rate` `reg 77.7(3)(b), (c) and reg 77.93(3)(b), (c) the period that the reference to the rate calculation period reads as` |  |
| reg 77.7(3)(e), (f) | src:1451-1454 | fork | `er5-pilot-rate` `reg 77.7(3)(e), (f) and reg 77.93(3)(e), (f) the claimant's weekly insurable earnings` | Fork F-reg77.7e. |
| reg 77.7(4) | src:1455-1457 | fork | `er5-pilot-rate` `reg 77.7(4)(a) ...`, `reg 77.7(4)(b) ...`, `reg 77.7(4) and reg 77.93(4) the insurable earnings allocated to a week with no evidence of its own` | Fork F-reg77.7f: 'proportionately' by days. |
| Heading "Pilot Project Increasing Allowable Earnings from Employment While Claimant is Receiving Benefits (2)" | src:1459 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.8(1) | src:1460 | encoded | `er5-pilot-earnings` `reg 77.8(1) the purpose of Pilot Project No. 12` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.8(2) | src:1461 | encoded | `er5-pilot-earnings` `reg 77.8(2) the claimant is included in Pilot Project No. 12` | Schedule I (piece er6) is a BOOLEAN input. |
| reg 77.8(3) | src:1462-1464 | fork | `er5-pilot-earnings` `reg 77.8(3) and reg 77.94(3) the maximum allowable earnings`, `reg 77.8(3) the maximum allowable earnings for the week under Pilot Project No. 12` | Fork F-reg77.8d: the 40% is not rounded. |
| reg 77.8(4) | src:1465 | fork | `er5-pilot-earnings` `reg 77.8(4) the section has effect for the week`, `reg 77.8(4) the day on which section 77.8 ceases to have effect` | Fork F-reg77.8c: 'ceases to have effect on' a Saturday read as effect through that week. |
| reg 77.9 | src:1466 | repealed or blank in this text | `er5-pilot-earnings` `reg 77.9 is repealed and therefore not encoded` | Reads only [Repealed, SOR/2016-206, s. 8]. |
| Heading "Pilot Project Relating to Extended Employment Insurance and Training Incentive" | src:1468 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.91(1) | src:1469 | encoded | `er5-pilot-weeks` `reg 77.91(1) the purpose of Pilot Project No. 14` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.91(2) | src:1470 | encoded | `er5-pilot-weeks` `reg 77.91(2) the claimant is included in Pilot Project No. 14` |  |
| reg 77.91(3) | src:1471-1478 | encoded | `er5-pilot-weeks` `reg 77.91(3) the claimant meets the criteria of Pilot Project No. 14` | Forks F-reg77.91c and F-reg77.91d. |
| reg 77.91(4) | src:1479 | fork | `er5-pilot-weeks` `reg 77.91(4) the number of weeks by which the benefit period is extended` | Fork F-reg77.91e: the 104 weeks cap the extension. |
| reg 77.91(5) | src:1480-1482 | encoded | `er5-pilot-weeks` `reg 77.91(5) the maximum number of weeks for which benefits may be paid` |  |
| reg 77.91(6) | src:1483 | fork | `er5-pilot-weeks` `reg 77.91(6) the period granted for job-search purposes, in weeks`, `reg 77.91(6) the Sunday on which the period granted for job-search purposes begins` | Fork F-reg77.91f: complete groups of five weeks. |
| reg 77.91(7) | src:1484 | encoded | `er5-pilot-weeks` `reg 77.91(7) the Sunday on which subsection 77.91(5) ceases to apply` |  |
| Heading "Pilot Project Relating to Extended Benefits" | src:1486 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.92(1) | src:1487 | encoded | `er5-pilot-weeks` `reg 77.92(1) the purpose of Pilot Project No. 15` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.92(2) | src:1488-1492 | fork | `er5-pilot-weeks` `reg 77.92(2) the claimant is included in Pilot Project No. 15`, `reg 77.92(2)(b) the last day on which a benefit period can be established under Pilot Project No. 15` | Fork F-reg77.92: the second Saturday after the first day of the 12th period, and (2)(b)(i) not cut off by the date of (ii). Schedule II.6 (piece er6) and the rate test of (2)(b)(i) under reg 17(1) (piece er1) are BOOLEAN inputs. |
| reg 77.92(3) | src:1493 | encoded | `er5-pilot-weeks` `reg 77.92(3) the Commission must publish a notice in the Canada Gazette and on its website` | A duty of the Commission with no number of days ('as soon as possible'); for the person it is the notice of the day their region's benefit periods stop being established. |
| reg 77.92(4) | src:1494 | encoded | `er5-pilot-weeks` `reg 77.92(4) the maximum number of weeks for which benefits may be paid in the benefit period` | Schedule II.7 (piece er6) is taken as the NUMBER the table gives. |
| Heading "Pilot Project for Calculating Benefit Rate Based on Claimant’s 14 Highest Weeks of Insurable Earnings" | src:1496 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.93(1) | src:1497 | encoded | `er5-pilot-rate` `reg 77.93(1) the purpose of Pilot Project No. 16` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.93(2) | src:1498 | encoded | `er5-pilot-rate` `reg 77.93(2) the claimant is included in Pilot Project No. 16` | Schedule II.91 (piece er6) and Part VII.1 of the Act (piece ei5) are BOOLEAN inputs. |
| reg 77.93(3)(a)-(d) | src:1500-1503 | encoded | `er5-pilot-rate` the same rules as reg 77.7(3)(a)-(d) | Cited with reg 77.7(3) in each rule's @ref. |
| reg 77.93(3)(e), (f) | src:1504-1507 | encoded | `er5-pilot-rate` the same rule as reg 77.7(3)(e), (f) |  |
| reg 77.93(4) | src:1508-1510 | encoded | `er5-pilot-rate` the same rules as reg 77.7(4) |  |
| Heading "Pilot Project Increasing Allowable Earnings from Employment While Claimant is Receiving Benefits" | src:1512 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.94(1) | src:1513 | encoded | `er5-pilot-earnings` `reg 77.94(1) the purpose of Pilot Project No. 17` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.94(2) | src:1514 | encoded | `er5-pilot-earnings` `reg 77.94(2) the claimant is included in Pilot Project No. 17` |  |
| reg 77.94(3) | src:1515-1517 | encoded | `er5-pilot-earnings` `reg 77.8(3) and reg 77.94(3) the maximum allowable earnings`, `reg 77.94(3) the maximum allowable earnings for the week under Pilot Project No. 17` |  |
| reg 77.94(4) | src:1518 | encoded | `er5-pilot-earnings` `reg 77.94(4) the day on which section 77.94 ceases to have effect` |  |
| Heading "Pilot Project to Encourage Claimant to Work More While Receiving Benefits" | src:1520 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.95(1) | src:1521 | encoded | `er5-pilot-earnings` `reg 77.95(1) the purpose of Pilot Project No. 18` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.95(2) | src:1522 | encoded | `er5-pilot-earnings` `reg 77.95(2) the claimant is included in Pilot Project No. 18` |  |
| reg 77.95(3) | src:1523-1524 | fork | `er5-pilot-earnings` `reg 77.95(3), reg 77.97(3) and reg 77.99(3) the amount to be deducted under subsection 19(2.1) of the Act as adapted` | The added s 19(2.1) is a computable rule for the pilot claimant, not an amendment of another instrument. Fork F-reg77.95. |
| reg 77.95(4) | src:1525-1526 | encoded | `er5-pilot-earnings` `reg 77.95(4), reg 77.97(4) and reg 77.99(4) the amount to be deducted under subsection 152.18(2.1) of the Act as adapted` | The self-employed person's counterpart. |
| reg 77.95(5) | src:1527 | encoded | `er5-pilot-earnings` `reg 77.95(5) Pilot Project No. 18 governs the deduction for the week` |  |
| reg 77.96(1) | src:1528 | encoded | `er5-pilot-elections` `reg 77.96(1) the purpose of Pilot Project No. 18 beyond its own` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.96(2) | src:1529 | encoded | `er5-pilot-elections` `reg 77.96(2) the claimant may elect`, `reg 77.96(2) the election is irrevocable`, `reg 77.96(2), (5), reg 77.98(2), (7) and reg 77.991(2) the method of treating the earnings of the benefit period` |  |
| reg 77.96(3) | src:1530-1532 | fork | `er5-pilot-elections` `reg 77.96(3) the applicable deadline for informing the Commission of the election` | Fork F-reg77.96a. |
| reg 77.96(4) | src:1533 | encoded | `er5-pilot-elections` `reg 77.96(4), reg 77.98(6) and reg 77.991(6) the election is considered to have been made by the deadline` | Good cause is the Commission's judgment: a BOOLEAN input. |
| reg 77.96(5) | src:1534 | fork | `er5-pilot-elections` `reg 77.96(5), (6) and (7) a failure to elect for an earlier benefit period binds the claimant for the subsequent benefit period` | Fork F-reg77.96b: (5) read as a bar. |
| reg 77.96(6) | src:1535 | encoded | `er5-pilot-elections` the same rule as reg 77.96(5) | The no-earnings exception. |
| reg 77.96(7) | src:1536 | encoded | `er5-pilot-elections` the same rule as reg 77.96(5) | The October 2012 notification exception. |
| reg 77.96(8) | src:1537-1539 | fork | `er5-pilot-elections` `reg 77.96(8)(a) the decision is not subject to appeal under section 114 of the Act`, `reg 77.96(8)(b) the decision is not subject to reconsideration under section 112 of the Act` | Fork F-reg77.96c: 'until March 31, 2013' is inclusive. |
| Heading "Pilot Project to Encourage Claimant to Work More While Receiving Benefits (2)" | src:1541 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.97(1) | src:1542 | encoded | `er5-pilot-earnings` `reg 77.97(1) the purpose of Pilot Project No. 19` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.97(2) | src:1543 | encoded | `er5-pilot-earnings` `reg 77.97(2) the claimant is included in Pilot Project No. 19` |  |
| reg 77.97(3) | src:1544-1545 | encoded | `er5-pilot-earnings` the same rule as reg 77.95(3) |  |
| reg 77.97(4) | src:1546-1547 | encoded | `er5-pilot-earnings` the same rule as reg 77.95(4) |  |
| reg 77.97(5) | src:1548 | encoded | `er5-pilot-earnings` `reg 77.97(5) Pilot Project No. 19 governs the deduction for the week` |  |
| reg 77.98(1) | src:1549 | encoded | `er5-pilot-elections` `reg 77.98(1) the purpose of Pilot Project No. 19 beyond its own` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.98(2) | src:1550-1552 | encoded | `er5-pilot-elections` `reg 77.98(2) the claimant may elect` | The carve-out of (2)(b) is one BOOLEAN fact. |
| reg 77.98(3) | src:1553 | encoded | `er5-pilot-elections` `reg 77.98(3) the election under section 77.96 is deemed to apply to the earnings of the portion of the benefit period within the period` |  |
| reg 77.98(4) | src:1554 | encoded | `er5-pilot-elections` `reg 77.98(4) the election also applies to the earnings of the portion of the benefit period before August 2, 2015` |  |
| reg 77.98(5) | src:1555 | encoded | `er5-pilot-elections` `reg 77.98(5) the last day on which the claimant must inform the Commission of their election` |  |
| reg 77.98(6) | src:1556 | encoded | `er5-pilot-elections` the same rule as reg 77.96(4) |  |
| reg 77.98(7) | src:1557 | encoded | `er5-pilot-elections` `reg 77.98(7) and (8) a failure to elect for an earlier benefit period binds the claimant for the subsequent benefit period` |  |
| reg 77.98(8) | src:1558 | encoded | `er5-pilot-elections` the same rule as reg 77.98(7) | The no-earnings exception. |
| reg 77.98(9) | src:1559 | encoded | `er5-pilot-elections` `reg 77.98(9) the decision is not subject to reconsideration under section 112 of the Act` |  |
| Heading "Pilot Project Relating to Earned Income While Receiving Benefits" | src:1561 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.99(1) | src:1562 | encoded | `er5-pilot-earnings` `reg 77.99(1) the purpose of Pilot Project No. 20` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.99(2) | src:1563 | encoded | `er5-pilot-earnings` `reg 77.99(2) the claimant is included in Pilot Project No. 20` |  |
| reg 77.99(3) | src:1564-1565 | encoded | `er5-pilot-earnings` the same rule as reg 77.95(3) |  |
| reg 77.99(4) | src:1566-1567 | encoded | `er5-pilot-earnings` the same rule as reg 77.95(4) |  |
| reg 77.99(5) | src:1568 | encoded | `er5-pilot-earnings` `reg 77.99(5) Pilot Project No. 20 governs the deduction for the week` |  |
| reg 77.991(1) | src:1569 | encoded | `er5-pilot-elections` `reg 77.991(1) the purpose of Pilot Project No. 20 beyond its own` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.991(2) | src:1570 | fork | `er5-pilot-elections` `reg 77.991(2) the portion of the benefit period to which the claimant may apply an election` | Fork F-reg77.991a: no condition on the claimant, read literally. |
| reg 77.991(3) | src:1571 | encoded | `er5-pilot-elections` `reg 77.991(3) the election under section 77.98 is deemed to apply to the earnings of the portion of the benefit period within the period` |  |
| reg 77.991(4) | src:1572 | encoded | `er5-pilot-elections` `reg 77.991(4) the claimant may make an election under subsection 77.991(2) in respect of the benefit period` |  |
| reg 77.991(5) | src:1573 | encoded | `er5-pilot-elections` `reg 77.991(5) the last day on which the claimant must inform the Commission of their election` |  |
| reg 77.991(6) | src:1574 | encoded | `er5-pilot-elections` the same rule as reg 77.96(4) |  |
| reg 77.991(7) | src:1575 | encoded | `er5-pilot-elections` `reg 77.991(7) the decision is not subject to reconsideration under section 112 of the Act` |  |
| Heading "Pilot Project Relating to Increased Weeks of Benefits for Seasonal Workers" | src:1577 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.992(1) | src:1578 | encoded | `er5-pilot-weeks` `reg 77.992(1) the purpose of Pilot Project No. 21` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.992(2) | src:1579-1583 | encoded | `er5-pilot-weeks` `reg 77.992(2) the claimant is included in Pilot Project No. 21`, `reg 77.992(2)(c) ...`, `reg 77.992(2)(d) ...` | (c) and (d) take the claimant's counts, made with (3) and (4); Schedule II.92 (piece er6) is a BOOLEAN input. |
| reg 77.992(3) | src:1584 | encoded | `er5-pilot-weeks` `reg 77.992(3) the earlier benefit period is considered to have been established within the 260-week period` |  |
| reg 77.992(4) | src:1585-1590 | fork | `er5-pilot-weeks` `reg 77.992(4) the earlier benefit period is considered to have begun around the same time of year` | Paragraphs (a) to (e) are the five calls of one helper; fork F-reg77.992. |
| reg 77.992(5) | src:1591 | encoded | `er5-pilot-weeks` `reg 77.992(5) the maximum number of weeks for which benefits may be paid in the benefit period` | Schedule II.93 (piece er6) is taken as the NUMBER the table gives. |
| Heading "Pilot Project to Provide Additional Weeks of Benefits to Seasonal Workers as a Result of Low Unemployment Rates" | src:1593 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.993(1) | src:1594 | encoded | `er5-pilot-weeks` `reg 77.993(1) the purpose of Pilot Project No. 22` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.993(2) | src:1595 | encoded | `er5-pilot-weeks` `reg 77.993(2) the claimant is included in Pilot Project No. 22` | The conditions of s 12(2.3) (piece ei1) are a BOOLEAN input. |
| reg 77.993(3) | src:1596 | encoded | `er5-pilot-weeks` `reg 77.993(3) the schedule that is read in place of Schedule V in subsection 12(2.3) of the Act` | A reading rule, carried as a STRING. |
| Heading "Pilot Project to Provide Additional Hours of Insurable Employment to Claimants in Areas Affected by Natural Disasters" | src:1598 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.994(1) | src:1599-1601 | encoded | `er5-pilot-hours` `reg 77.994(1)(a) the first purpose of Pilot Project No. 23`, `reg 77.994(1)(b) the second purpose of Pilot Project No. 23` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| reg 77.994(2) | src:1602-1604 | fork | `er5-pilot-hours` `reg 77.994(2) the claimant makes an initial claim under Part I ...`, `reg 77.994(2)(a) ...`, `reg 77.994(2)(b) ...` | Fork F-reg77.994: postal codes compared as the string the text writes. The day on which the section comes into force is not stated: an input. |
| reg 77.994(3) | src:1605 | encoded | `er5-pilot-hours` `reg 77.994(3) the additional hours of insurable employment that the claimant is deemed to have` |  |
| reg 77.994(4) | src:1606-1608 | encoded | `er5-pilot-hours` `reg 77.994(4) the additional hours of insurable employment that the claimant is deemed to have in relation to the claim` |  |
| reg 77.994(5) | src:1609 | encoded | `er5-pilot-hours` `reg 77.994(5) the provisions for which the additional hours count as hours of insurable employment`, `reg 77.994(5) the additional hours are also considered hours of insurable employment for the purposes of the provision` |  |
| Heading "Pilot Project Establishing Measures to Respond to Major Changes in Economic Conditions" | src:1611 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| Heading "Purpose" | src:1613 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.995 | src:1614 | encoded | `er5-pilot-24` `reg 77.995 the purpose of Pilot Project No. 24` | A purpose clause: a named STRING, as phrasebook entry 9.3 writes it; it decides nothing for the person, so the seat asks nothing about it. |
| Heading "Waiting Period" | src:1616 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.996 | src:1617 | encoded | `er5-pilot-24` `reg 77.996 the Commission may waive the waiting period`, `reg 77.996 the waiting period is waived` | The Commission's discretion is kept apart from the fact of its exercise. |
| Heading "Earnings for Benefit Purposes" | src:1619 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.997 | src:1620-1622 | fork | `er5-pilot-24` `reg 77.997 earnings paid by reason of a lay-off or separation do not constitute earnings for the purposes of subsection 35(2)` | Fork F-reg77.997: a week 'falls within' the period when all seven of its days do. Paragraph (b) takes the first week of allocation under reg 36(9) to (11) (piece er3) as an input. |
| Heading "Rate of Unemployment" | src:1624 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.998 | src:1625-1628 | encoded | `er5-pilot-24` `reg 77.998 the regional rate of unemployment that applies to the claimant` | Boundaries 6.1%, 12.1% and 13.1% are tested on both sides. |
| Heading "Benefit Period and Weeks of Regular Benefits" | src:1630 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 77.999(1) | src:1631 | encoded | `er5-pilot-24` `reg 77.999(1) long-tenured worker` | The unassessed-return alternative is the second count input. |
| reg 77.999(2) | src:1632 | encoded | `er5-pilot-24` `reg 77.999(2) the number of weeks by which the benefit period is extended` | The day the section comes into force is not stated: an input. |
| reg 77.999(3) | src:1633-1634 | encoded | `er5-pilot-24` `reg 77.999(3) the length in weeks of the benefit period after its extensions, held to 104 weeks` | NOTHING outside the period: the Act's s 10(14) governs. |
| reg 77.999(4) | src:1635-1637 | encoded | `er5-pilot-24` `reg 77.999(4)(a) ...`, `reg 77.999(4)(b) ...` |  |
| reg 77.999(5) | src:1638 | encoded | `er5-pilot-24` `reg 77.999(5) the additional weeks are still payable` |  |
| Heading "PART V Administrative Provisions" | src:1640 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| Heading "Reconsideration under Section 112 of the Act" | src:1642 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 78(1) | src:1643-1650 | fork | `er5-admin-reconsideration` `reg 78(1) the request for reconsideration is in writing and contains the information required` | Each 'if any' is read for the item it follows (fork F-reg78). |
| reg 78(2) | src:1651 | encoded | `er5-admin-reconsideration` `reg 78(2) the request for reconsideration was filed as the Commission's website provides` | Any one of the four ways. |
| reg 79 | src:1652 | encoded | `er5-admin-reconsideration` `reg 79 the Commission must render its decision on the request without delay`, `reg 79 the Commission has rendered its decision without delay` | 'Without delay' has no measure: the second rule returns NOTHING and a test asserts it. |
| Heading "Suspension of Benefits Pending Appeal" | src:1654 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 80 | src:1655 | fork | `er5-admin-reconsideration` `reg 80 benefits are not payable in accordance with the decision` | 21 days after the decision (fork F-reg80). |
| reg 81 | src:1656 | encoded | `er5-admin-reconsideration` `reg 81 benefits are not payable in respect of the claim` |  |
| reg 82(1) | src:1657-1659 | fork | `er5-admin-reconsideration` `reg 82(1) benefits are not payable on the claim`, with `reg 82(1) and (2) the claim is caught by the decision` | Fork F-reg82: how (a) and (b) combine. |
| reg 82(2) | src:1660 | encoded | `er5-admin-reconsideration` `reg 82(2) benefits are not payable on the claim`, with `reg 82(1) and (2) the claim is caught by the decision` |  |
| regs 83, 84, 85, 86, 87 | src:1661-1665 | repealed or blank in this text | `er5-admin-reconsideration` `regs 83 to 87 are repealed and therefore not encoded` | Each reads only [Repealed, SOR/2013-64, s. 2]. |
| Heading "Payment of Benefits Pending a Coverage Decision" | src:1667 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 88(1) | src:1668-1674 | fork | `er5-admin-coverage-decision` `reg 88(1) no benefits are payable in respect of the hour on the day in question`, `reg 88(1) the later of the day the officer's ruling becomes final and the day the decision at the last stage taken becomes final` | Paragraphs (a) and (b)(i) to (iv) are one rule: the later of the days. Fork F-reg88: 'until' that day is read as payable on it. |
| reg 88(2) | src:1675 | encoded | `er5-admin-coverage-decision` `reg 88(2) subsection 88(1) does not apply` |  |
| Heading "Social Insurance Numbers" | src:1677 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 89(1) | src:1678 | encoded | `er5-admin-sin` `reg 89(1) the person must apply to the Commission to be registered`, `reg 89(1) the last day on which the person must apply to be registered`, `reg 89(1) the person applies to be registered within three days after the day on which the employment begins` |  |
| reg 89(2) | src:1679 | encoded | `er5-admin-sin` `reg 89(2) ...` (three rules) | An employer's duty; for the person it means what the employer must ask of them, and by when. |
| reg 89(3) | src:1680 | encoded | `er5-admin-sin` `reg 89(3) and (4) the last day on which the person must inform the employer of their Social Insurance Number` | Encoded with (4) as one deadline rule. |
| reg 89(4) | src:1681 | encoded | `er5-admin-sin` the same rule as reg 89(3) | 'However': replaces the deadline of (3) for a person employed before being registered. |
| reg 89(5) | src:1682 | encoded | `er5-admin-sin` `reg 89(5) ...` (three rules) | An employer's duty. |
| reg 89(6) | src:1683 | encoded | `er5-admin-sin` `reg 89(6) ...` (three rules) |  |
| Heading "Electronic Systems" | src:1685 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 90 | src:1686 | encoded | `er5-admin-electronic-systems` `reg 90 the information must be provided in a form and manner approved by the Commission`, `reg 90 the information is provided as the Commission requires` | Whether a form and manner is approved is the Commission's judgment: a BOOLEAN input. |
| reg 91(1) | src:1687-1689 | encoded | `er5-admin-electronic-systems` `reg 91(1) the claim is made by telephone or other electronic means with the information section 50 requires`, `reg 91(1)(a) ...`, `reg 91(1)(b) ...` |  |
| reg 91(2) | src:1690-1692 | fork | `er5-admin-electronic-systems` `reg 91(2) the claimant is deemed to have signed the claim` | Fork F-reg91: 'by electronic means' (the mother's maiden name) is read against a claim by telephone. |
| reg 91(3) | src:1693 | encoded | `er5-admin-electronic-systems` `reg 91(3) the day on which the claim is deemed to have been made` | NOTHING for a claim not made by those means. |
| reg 91(4) | src:1694 | encoded | `er5-admin-electronic-systems` `reg 91(4) sections 38 and 135 of the Act apply to the declaration` |  |
| reg 91(5) | src:1695 | encoded | `er5-admin-electronic-systems` `reg 91(5) the act is deemed to be an act or omission specified in subsections 38(1) and 135(1) of the Act`, `reg 91(5) the penalty and the punishment include the right to refuse the person access to the electronic systems` |  |
| Heading "Direct Deposit of Benefits" | src:1697 | inert | - | A heading, which is a title: it carries no text of its own and decides nothing. |
| reg 92(1) | src:1698 | encoded | `er5-admin-direct-deposit` `reg 92(1) the sections of the Direct Deposit Regulations that apply for the purposes of this section` | The Direct Deposit Regulations are not among the inputs: only the section numbers it names are carried. |
| reg 92(2) | src:1699 | encoded | `er5-admin-direct-deposit` `reg 92(2) the claimant's benefits are to be deposited directly to their bank account` |  |
| reg 92(3) | src:1700 | encoded | `er5-admin-direct-deposit` `reg 92(3) the claimant is responsible for the accuracy of the data` |  |
| reg 92(4) | src:1701-1703 | fork | `er5-admin-direct-deposit` `reg 92(4) the documents together constitute evidence of the transfer of funds and the payment of benefits` | Fork F-reg92: NOTHING when there is contrary evidence or a document is missing. |
| reg 92(5) | src:1704 | encoded | `er5-admin-direct-deposit` `reg 92(5) the claimant must notify the Commission`, `reg 92(5) the direct deposit of benefits is terminated` |  |
| reg 92(6) | src:1705 | encoded | `er5-admin-direct-deposit` `reg 92(6) sections 38 and 135 of the Act apply to the declaration` |  |
| reg 92(7) | src:1706 | encoded | `er5-admin-direct-deposit` `reg 92(7) the act is deemed to be an act or omission specified in subsections 38(1) and 135(1) of the Act`, `reg 92(7) the penalty and the punishment include the right to refuse the person access to the electronic systems used for direct deposit` |  |
| reg 92(8) | src:1707 | encoded | `er5-admin-direct-deposit` `reg 92(8) the Commission may redirect the deposit of benefits` |  |


## Fork register

Every entry is assumed, not ruled: a reading chosen so that work could go on, reversible in the one rule named.
The keel's fork F4 (a limit of n days after d ends on d plus n, and that day counts) is used for every day-count in this piece: reg 80 (21 days), reg 77.96, 77.98 and 77.991 (30 days), reg 89 (three and six days), reg 77.91(3)(c) (20 weeks), and reg 77.994.
I looked for ambiguity in every subsection of the range; the entries below are where the text left a real choice, and the last paragraph says where I looked and found none.

| id | provision | readings seen | the reading taken | the text that licenses each |
| --- | --- | --- | --- | --- |
| F-reg77a | reg 77(2) "period of eligibility" (a)(i) and (ii) (src:1400-1403) | R1: (i) is the pregnancy benefits of s 22 and (ii) the benefits of s 23 for a new-born or adopted child, and a claimant of both has both; R2: (i) and (ii) are alternatives for any claimant of the (3)(d)(i) reasons. | R1. The aggregate is carried as the span from the earliest first day to the latest last day of the periods that apply (only where it begins and ends matter to (3)(c)). | R1: the Act's s 22(2) is the pregnancy period and s 23(2) the parental period (Act src:489-519), and (ii) says "unless that waiting period has already been taken into account for the purposes of subparagraph (i)", which only makes sense if both can apply to one claimant. R2: the lead-in of (a) names both reasons together. |
| F-reg77b | reg 77(3)(a) and (7) (src:1406, 1417) | The text does not say on which day eligibility is tested. R1: "ceases to be in force on April 1, 1997" means in force through that day; R2: out of force from that day. | The day tested is an input; R2 (in force on days before April 1, 1997). | The phrase "ceases to be in force on" alone. Contrast F-reg77.8c, where the surrounding dates settle the other reading. |
| F-reg77c | reg 77(4), (5) (src:1412-1415) | R1: the claimant who completes and signs the form participates; R2: the Commission must also accept. | R1. | (4) "who wishes to participate ... shall complete and sign a form"; (5) "a claimant who participates"; nothing speaks of acceptance. |
| F-reg77d | reg 77(3)(d) (src:1409-1411) | R1: every week claimed for the same reason; R2: every week claimed for one or the other reason. | R2: one fact. | "in respect of every week ... (i) ... or (ii)". |
| F-reg77.1 | reg 77.1(2) to (5) (src:1421-1429) | Neither the day the section comes into force nor the day it ceases is stated (inputs). On rescission: R1: a rescinded choice has no effect, so no deeming under (3) and no repayment under (4)(b); R2: the repayment survives. | R1. | (5) "A claimant may rescind a choice made by them under subsection (3). A claimant who rescinds shall be paid benefits to which they are entitled." |
| F-reg77.7e | reg 77.7(3)(e), (f) and 77.93(3)(e), (f) (src:1451-1454, 1504-1507) | Which weeks are "the 14 highest": R1 the weeks ranked with the section 24.1 earnings taken out; R2 ranked with them in and then taken out. With fewer than 14 weeks: R1 sum those and divide by 14; R2 divide by the number of weeks. | R1 on both. | "(i) the insurable earnings from the 14 highest weeks ..., not including any insurable earnings ... under section 24.1" and "(f) ... by 14". |
| F-reg77.7f | reg 77.7(4) and 77.93(4) (src:1455-1457, 1508-1510) | "Proportionately" over the pay period: R1 by days; R2 by weeks. | R1 (equal to R2 for a pay period of whole weeks). | "allocate the amount ... proportionately over the pay period"; a pay period (reg 1(1), piece er1) is not always a number of whole weeks. |
| F-reg77.8c | regs 77.8(4), 77.94(4), 77.95(5), 77.97(5), 77.99(5) (src:1465, 1518, 1527, 1548, 1568) | "Ceases to have effect on D": R1 the section has effect through D; R2 it has none from D. | R1: a week is inside when its last day is on or before D. | Every D (Aug 6, 2011; Aug 4, 2012; Aug 1, 2015; Aug 6, 2016; Aug 11, 2018) is a Saturday, and each (2) window begins on a Sunday and ends on that Saturday (checked with Python's datetime). |
| F-reg77.8d | regs 77.8(3), 77.94(3), 77.95(3), 77.97(3), 77.99(3) (src:1462-1464 and the others) | Whether s 6(2) of the Act (rounding "a percentage or fraction of earnings or benefits" in Part I to the nearest dollar) rounds the 40% and the 50% and 100% parts: R1 yes; R2 no. | R2. A test pins 40% of 188 as 75.2. | s 6(2) speaks of "a reference in this Part"; the Regulations say nothing about rounding. Applying s 6(2) would change a figure by under one dollar. |
| F-reg77.91c | reg 77.91(3)(c) (src:1474) | R1: two alternatives, "within 20 weeks after the beginning of the benefit period" or "before August 23, 2009, if the benefit period began before May 31, 2009"; R2: both required. | R1; the plan counts if it became active on or before the last day. | The word "or" and the "if". |
| F-reg77.91d | reg 77.91(3)(d)(iii) (src:1478) | "One of the 52 weeks following the beginning": R1 the 52 weeks that start with the first day of the benefit period; R2 the 52 weeks after the week in which it begins. | R1. | A benefit period begins on a Sunday, the first day of a week (Act s 10(1)). |
| F-reg77.91e | reg 77.91(4) (src:1479) | "up to a maximum of 104 weeks": R1 caps the extension; R2 caps the benefit period as extended. | R1. | The grammar; the Act's s 10(14) says "must not result in a benefit period of more than 104 weeks" and (4) does not. |
| F-reg77.91f | reg 77.91(6) (src:1483) | "One week of benefits for every five weeks of training completed": R1 complete groups of five; R2 in proportion. | R1. | "for every five weeks". |
| F-reg77.92 | reg 77.92(2)(b) (src:1491-1492) | "The second Saturday after the first day of the 12th period": R1 the first Saturday strictly after that day, plus seven days; R2 the day itself counts if it is a Saturday. And whether (i) is cut off by the date of (ii). | R1; (i) taken literally, not cut off. | "after". |
| F-reg77.95 | regs 77.95(3), 77.97(3), 77.99(3) and (4) (src:1524, 1545, 1565) | "50% of the earnings that are less than or equal to 90% of ..." and "100% of any earnings that are greater than 90% of ...": R1 marginal, 50% on the part up to the threshold and 100% on the part above; R2 a cliff, 50% of all the earnings if they do not pass the threshold and 100% of all if they do. | R1. | The purpose clauses (1): "50% of those earnings, until the earnings exceed 90% of their weekly insurable earnings". |
| F-reg77.96a | reg 77.96(3) (src:1531-1532) | A benefit period with notifications under both (a) (Aug 5, 2012 to Jan 5, 2013) and (b) (after Jan 5, 2013): R1 (b) governs; R2 (a) governs; R3 both apply. They differ only when the last notification is within 30 days of Aug 1, 2015. | R1; "the last notification" moves with the last notice issued. | (b) caps the deadline at the end of the project (Aug 1, 2015), and (a)'s floor of Feb 5, 2013 is always passed when a notice comes after Jan 5, 2013. |
| F-reg77.96b | reg 77.96(5) to (7) (src:1534-1536) | R1: a failure to elect is a bar on electing for the subsequent benefit period; R2: only a default. | R1. | (7) "Despite subsection (5) ... may ... make an election in respect of the subsequent benefit period" restores a right that (5) must otherwise have taken away. |
| F-reg77.96c | reg 77.96(8) (src:1538-1539) | "(a) until March 31, 2013": R1 through that day; R2 before it, leaving March 31 uncovered. | R1. | (b) begins "on or after April 1, 2013", so R1 leaves no gap. |
| F-reg77.991a | reg 77.991(2) (src:1570) | Unlike 77.96(2) and 77.98(2) the text states no condition on the claimant: R1 literally none; R2 the condition of 77.98(2) is implied. | R1. | The words of (2) and (4), which speaks of a claimant "eligible to make an election under section 77.98" only for the earlier benefit periods. |
| F-reg77.992 | reg 77.992(4) (src:1585-1590) | "Begins eight weeks before and ends eight weeks after the week that is N weeks before the first week": R1 from the first day of the eighth week before to the last day of the eighth week after (56 days before the Sunday to 62 days after it); R2 56 days either side of the Sunday. | R1. | Weeks run Sunday to Saturday (Act s 2(1) "week"). |
| F-reg77.994 | reg 77.994(2) (src:1602) | The postal codes T0E 1E0, T0E 0C0 and R0B 1C0: R1 compared as the string the text writes; R2 compared ignoring case and the space. | R1. | The text's own writing. |
| F-reg77.997 | reg 77.997(b) (src:1622) | "The first week of which falls within the period": R1 the whole week; R2 its Sunday. | R1 (the same answer for the dates stated, which run from a Sunday to a Saturday). | "falls within". |
| F-reg78 | reg 78(1)(a)(iii) (src:1647) | "facsimile number and email address, if any": R1 each is required of a person who has it; R2 both only of a person who has both. | R1. | "if any" follows both items. |
| F-reg80 | reg 80 (src:1655) | "Within 21 days after the day on which a decision is given": an appeal on the day of the decision. R1 counts; R2 does not. | R1; an appeal before the decision cannot be an appeal from it. | "within". |
| F-reg82 | reg 82(1) (src:1657-1659) | "Until (a) the final determination of the appeal ...; or (b) the final determination of any application ... for judicial review ..., if the final determination of the appeal declares the provision ... ultra vires": R1 (b) extends the stoppage past (a) only when the Appeal Division's determination declares the provision ultra vires and the Commission has applied for judicial review; R2 the earlier of (a) and (b). | R1. | (b)'s own condition. |
| F-reg88 | reg 88(1) (src:1668-1674) | "Until the later of (a) and (b)": R1 benefits are payable from that day; R2 from the day after. And (b)(i) to (iv) each exist only "where" that step is taken. | R1; the later of every day that applies. | "until the later of (a) and (b)", where each of (b)(i) to (iv) is the day on which a decision "becomes final": the day a decision becomes final is the day from which it can be relied on, as for 'the day on which' in the keel's F4. |
| F-reg91 | reg 91(2)(a) (src:1691) | "If the initial claim is made by electronic means" within "telephone or other electronic means": R1 the maiden name is asked only of an initial claim made by electronic means other than telephone; R2 of every initial claim. | R1. | The contrast drawn between the two means. |
| F-reg92 | reg 92(4) (src:1701-1703) | The two documents "constitute evidence" "in the absence of any evidence to the contrary": R1 the rule answers JUST TRUE with both documents and no contrary evidence and NOTHING otherwise; R2 FALSE when a document is missing. | R1. | The text says what the documents are worth only in that case. |

Where I looked and found no further fork: regs 77.2, 77.92(4), 77.992(2), (3), (5), 77.993, 77.995, 77.996, 77.998, 77.999 (the arithmetic is stated), 79, 81, 89, 90, 91(1), (3) to (5) and 92 (apart from (4)): the text states the figure, the window or the condition; the open points there are the commencement days, listed under "What the text turns out to say" (item 17).


## Cross-references out of my ranges

Each is a plain input named for the fact, with a comment `-- out of range: ...` in the module.
| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| reg 77(2) condition of entitlement | s 49(1) of the Act | ei2 | `the requirement, circumstance or condition is one referred to in subsection 49(1) of the Act` (BOOLEAN) |
| reg 77(2) period of eligibility (a) | s 13, s 22(2) (with any extension) and s 23(2) of the Act | ei1 | three `Period of days` inputs: the waiting period, the s 22(2) period, the s 23(2) period |
| reg 77(2) period of eligibility (b) | s 25(1)(a) of the Act | ei2 | `the period during which the claimant attends a course or program referred to in paragraph 25(1)(a) of the Act` (a `Period of days`) |
| reg 77(3)(b) | s 26(2) of the Act | ei2 | `the claimant makes a claim in respect of which subsection 26(2) of the Act applies` (BOOLEAN) |
| reg 77(3)(d), 77(4)(a), 77(5) | ss 12(3)(a), (b), 19, 22, 23, 25, 49, 50 and s 11 of the Act | ei1, ei2 | BOOLEAN inputs: the weeks claimed for those reasons; `the week is a week of unemployment` |
| reg 77.1(2) | reg 35(2)(f) (an indemnity payment) | er3 | `the claimant receives or is entitled to receive an indemnity payment described in paragraph 35(2)(f) ...` (BOOLEAN) |
| reg 77.1(3) | s 10(10)(d) of the Act | ei1 | none made: the deeming is encoded as the rule's own output |
| reg 77.2(2), 77.7(2), 77.8(2), 77.92(2), 77.93(2), 77.94(2), 77.95(2), 77.97(2), 77.99(2), 77.992(2) | Schedule I and Schedules II.1, II.6, II.8, II.91, II.92 of the Regulations | er6 | a BOOLEAN input per schedule: `... ordinarily resident in a region described in Schedule I that is set out in Schedule II.N` |
| reg 77.2(3), 77.92(4), 77.992(5) | Schedules II.2, II.7 and II.93 (the tables of maximum weeks) | er6 | a NUMBER input per table: the number of weeks the table gives for the rate and the hours |
| reg 77.7(3)(b), (c); reg 77.93(3)(b), (c) | s 14(3) of the Act; reg 24.1 | ei1; er2 | two `Period of days` inputs (the rate calculation period, the qualifying period); a NUMBER (the section 24.1 earnings) |
| reg 77.7(3)(a), (d) | s 14(2), (4), (4.1) of the Act; reg 24.2 | ei1; er2 | none made: the rule states that they do not apply |
| reg 77.8(3), 77.94(3) | s 14 of the Act (the rate of weekly benefits) | ei1 | `the claimant's rate of weekly benefits` (NUMBER) |
| reg 77.95(3), 77.97(3), 77.99(3) | s 14 of the Act; s 19 and s 13 of the Act | ei1 | `the claimant's weekly insurable earnings used to establish their rate of weekly benefits` (NUMBER); `the deduction is for the purpose of section 13 of the Act` (BOOLEAN) |
| reg 77.95(4), 77.97(4), 77.99(4) | s 152.16(1)(a), (b), s 152.18 and s 152.15 of the Act | ei5 | `the sum of the amounts referred to in paragraphs 152.16(1)(a) and (b) of the Act` (NUMBER); `the deduction is for the purpose of section 152.15 of the Act` (BOOLEAN) |
| reg 77.91(3)(d) | s 25(1)(a) of the Act | ei2 | `the claimant is referred ... under paragraph 25(1)(a) of the Act ...` (BOOLEAN) |
| reg 77.91(5) | s 12(1), (2), (3), (6) of the Act | ei1 | `the maximum number of weeks determined by subsection 12(2), (3) or (6) of the Act` (NUMBER); the extra weeks (NUMBER) |
| reg 77.91(7) | s 27(1.1)(b) of the Act | ei2 | `any of the conditions under which the Commission may terminate the claimant's referral ... exists` (BOOLEAN) |
| reg 77.92(2)(b)(i) | reg 17(1) (the regional rate of unemployment) | er1 | `the regional rate of unemployment, as determined in accordance with subsection 17(1), is less than 8.0% for 12 consecutive periods ...` (BOOLEAN) and the first day of the 12th period (DATE) |
| reg 77.93(2) | Part VII.1 of the Act | ei5 | `Part VII.1 of the Act applies in respect of the claimant` (BOOLEAN) |
| reg 77.96, 77.98, 77.991 | ss 112 and 114 of the Act | ei4 | none made: the rules state that the decision is not subject to them |
| reg 77.993(2) | s 12(2.3) of the Act; Schedule II.94 | ei1; er6 | `the claimant meets the conditions set out in subsection 12(2.3) of the Act, read with Schedule II.94 in place of Schedule V` (BOOLEAN) |
| reg 77.994 | s 10(8)(d), s 28(4), s 30(1)(a), s 31(c), s 32(2)(c) of the Act; reg 35(3), 35(7)(e)(ii) | ei1; ei2; er3 | the day a benefit period ended under s 10(8)(d) (MAYBE DATE); the provisions are carried as a list of STRINGs |
| reg 77.997 | reg 35(2), reg 36(9) to (11) | er3 | `the Sunday of the first week to which those earnings would otherwise be allocated` (DATE) |
| reg 77.998 | s 10(1) of the Act; reg 17 | ei1; er1 | `the Sunday on which the later of the weeks referred to in subsection 10(1) of the Act begins` (DATE); `the regional rate ... under section 17` (NUMBER) |
| reg 77.999(2), (3), (4) | ss 9, 10(8)(d), 10(10) to (13.02), 12(2), (2.3), (3), (6), 25 of the Act | ei1; ei2 | a BOOLEAN for s 9; a MAYBE DATE for s 10(8)(d); two NUMBERs (the length with the other extensions; the maximum under s 12(2) or (2.3)) |
| reg 78 | ss 112, 114 of the Act | ei4 | none made: reg 78 states what the request must contain and where it is filed |
| reg 80, 81, 82 | the Department of Employment and Social Development Act, the Federal Courts Act, the Social Security Tribunal's decisions | outside the two texts | BOOLEAN inputs for each step taken (appeal, application, final determination) |
| reg 88 | ss 90(1)(a) to (d) and 103 of the Act; s 28 of the Federal Courts Act | ei3 | BOOLEAN and DATE inputs for each stage taken and the day each decision became final |
| reg 89(1) | s 138 of the Act; s 28.1(2) of the Department of Employment and Social Development Act | ei4; outside the two texts | `the person is required by section 138 of the Act to have a Social Insurance Number` (BOOLEAN) |
| reg 90, 91 | ss 38, 48, 49, 50, 135 and 152.1 of the Act | ei2; ei4; ei5 | `the claimant provides the information required by section 50 of the Act` (BOOLEAN); the rest are stated, not tested |
| reg 92(1) | the Direct Deposit Regulations, ss 2 and 4 to 8 | outside the two texts | none made: the section numbers are carried as a list |

## Needs from the core

Nothing is needed for this piece to run: it imports `eia-core` only and defines no name the core defines.
Four helpers were written locally under specific names; the lead may promote them if another piece needs them.

| local name | module | what it does | why the core might want it |
| --- | --- | --- | --- |
| `er5 reg 77.96 the later of two days` and `er5 reg 77.96 the earlier of two days` | `er5-pilot-elections` | the later and the earlier of two DATEs | "whichever is later / earlier" deadlines recur in the Act (for example the 52-week limits) |
| `er5 reg 77.96 the portion of the benefit period that falls within the period` | `er5-pilot-elections` | the overlap of two `Period of days`, or NOTHING | benefit periods are clipped to windows in several pieces |
| `er5 reg 77.95 the whole week falls within` and `reg 77.8(4) the section has effect for the week` | `er5-pilot-earnings` | a week (by its Sunday) lies wholly inside a period / ends on or before a day | the core has `the day ... falls within ...` but no week-in-a-period test |
| `reg 77.91(6) the Sunday on which the period granted for job-search purposes begins` | `er5-pilot-weeks` | the first Sunday strictly after a day | the keel's `s 2(1) the Sunday that begins the week containing` gives the Sunday on or before a day; "the Sunday after" is the same plus seven days |

## What the text turns out to say

1. Sixteen pilot projects are in this range (Nos. 1, 5, 6, 11, 12, 14 to 24), and every window had closed by the end of the consolidation's currency date except Pilot Project No. 24, which ran to October 10, 2026; all sixteen are therefore spent today, and the brief's `inert` reasons do not include "spent", so all of them are `encoded`. Asserted (each project's window on both sides).
2. Regs 77.998 deems the regional rate to be 7.1% (rate 6.1% or less), the rate plus 1% (more than 6.1% and less than 12.1%) or 13.1% (12.1% or more) only when the rate is below 13.1% and the later week begins from April 6 to October 11, 2025; the three bands join without a gap (6.1% gives 7.1% either way; 12.09% gives 13.09%; 12.1% gives 13.1%), and a rate of exactly 13.1% is outside the section. Asserted.
3. A long-tenured worker (reg 77.999(1)) needs fewer than 36 weeks of regular benefits in 156 weeks and 30% of the maximum premium in 7 of 10 years, counted from the assessed returns; if last year's return is not yet assessed the ten years move back one year. Asserted at 35/36 weeks and at 6/7 years, with the alternative count.
4. The 20-week extension (reg 77.999(2)) is not an extra 20 weeks of benefits by itself: (4) adds 20 weeks to the maximum and reads the 50 weeks of s 12(6) as 70, and (3) holds the whole benefit period to 104 weeks. Asserted.
5. Ceasing to be a long-tenured worker during the benefit period does not end the added weeks (reg 77.999(5)); only some other ground can. Asserted.
6. Reg 77.8(3) and 77.94(3) give $75 below a rate of $188 and 40% of the rate from $188: at $188 exactly that is $75.20, which is more than $75 (the two limbs are not continuous at the boundary), and neither figure is rounded in the Regulations. Asserted.
7. Regs 77.95(3), 77.97(3) and 77.99(3) deduct 50% of earnings up to 90% of the weekly insurable earnings and 100% above it: earnings of 600 against 500 are charged 375, not 300 and not 600. Asserted.
8. Every cessation day of regs 77.8, 77.94, 77.95, 77.97 and 77.99 is a Saturday and every window begins on a Sunday, so a week is either wholly inside a section or wholly outside it. Asserted.
9. Under reg 77.7(3)(f) and 77.93(3)(f) the weekly insurable earnings are the sum of the 14 highest weeks plus the section 24.1 earnings, divided by 14 even when the qualifying period has fewer than 14 weeks. Asserted.
10. The text of reg 77.96(3) has two limbs that can both fit a benefit period with notifications in both periods; they give different deadlines only when the last notification falls within 30 days of August 1, 2015. Asserted (fork F-reg77.96a).
11. Reg 77.96(5) to (7), read with "Despite subsection (5)" in (7), bars a later election after a failure to elect; regs 77.98(7) and (8) have no counterpart of (7); reg 77.991 has no failure rule at all and no condition of earlier earnings on the right to elect (compare 77.96(2) and 77.98(2)). Asserted.
12. Reg 77.91(3)(c) gives a plan an extra deadline of August 23, 2009 only to a benefit period that began before May 31, 2009; for a benefit period that began on May 31, 2009 itself only the 20 weeks (to October 18, 2009) count. Asserted.
13. Reg 77.92(2)(b)(i) ends the window "on the second Saturday after the first day of the 12th period": after a Saturday, the first Saturday is the next one, so the answer is 14 days later, not 7. Asserted.
14. Reg 77.992(4) makes the "same time of year" window 17 weeks wide: from 56 days before to 62 days after the Sunday that begins the week 52, 104, 156, 208 or 260 weeks back. Asserted at both edges of the first window and the last.
15. Reg 77.994(2)(a) and (b) cannot both hold for the same claim (a benefit period that began before the section came into force, against a claim made on or after it); (4)(a) and (b) take the 300 hours away from a claimant who has already had them. Asserted.
16. Reg 77.994(2) names the postal codes T0E 1E0, T0E 0C0 and R0B 1C0 and the text is compared as written. Asserted (a code without its space is not matched).
17. The text never states the day regs 77.1, 77.994 and 77.999 come into force or (77.1) cease to have effect; each is an input. Asserted with invented days.
18. Reg 79 gives the Commission no number of days: "without delay" is not measured, so "has it taken too long?" is not covered. Asserted (NOTHING).
19. Reg 80 counts 21 days from the day a decision is given; a day-21 appeal counts and a day-22 appeal does not. Asserted.
20. Reg 82(1)(a) and (b) read together: the stoppage outlasts the Appeal Division's final determination only if that determination declares the provision ultra vires and the Commission has applied for judicial review. Asserted (fork F-reg82).
21. Reg 88(1) waits for the last of up to five decisions: the officer's ruling and each appeal that was taken; if any one that was taken is not yet final there is no day, and benefits are not payable on any day. Asserted.
22. Reg 89(4) displaces the three days of (3) for a person employed before being registered: the three days run from receiving the number, and no time runs until it is received. Asserted.
23. Reg 89(1) to (6) use "within three days after the day" and "within six days after the day": the day counts (the keel's F4); a leap day is counted in February 2020 (February 27 plus 3 is March 1) and not in 2021 (February 26 plus 3 is March 1). Asserted.
24. Reg 91(2): an initial claim by telephone needs the date of birth; the mother's maiden name is asked only of an initial claim made by electronic means; a weekly claim needs the personal identification number. Asserted.
25. Reg 92(2) is expressly "subject to subsection (7)": a claimant refused access to the direct deposit systems has no direct deposit. Asserted.
26. Reg 92(4) says what two documents are worth only "in the absence of any evidence to the contrary"; it does not say they are the only evidence. Asserted (NOTHING otherwise).
27. Reg 78(1)(d) asks a request to contain "any relevant information that was not previously provided": a person with nothing new to add need add nothing. Asserted.
28. Reg 88 names the "Canada Customs and Revenue Agency"; the name is carried as the text writes it. Not asserted.
29. Regs 77.3 to 77.6, 77.9 and 83 to 87 are repealed and read only "[Repealed, ...]"; each is a labelled stub and the three stubs are tested as strings (or as the inert TRUE of a string chain). Asserted.

## What the stable binary does not accept

Measured in this run with the binary `l4 1.6.98` (sha256 `82ea44ad...263e`), none of it a language claim beyond this build:

- A lone string literal is a STRING, not a BOOLEAN: `#ASSERT \`stub\`` on a stub defined as one string fails with "An ASSERT directive is expected to be of type BOOLEAN but is here of type STRING". A chain of strings joined by `...` is the inert TRUE. The single-string repealed stub (reg 77.9) is therefore asserted `EQUALS` its string.
- The linter warns, at Warning severity (which `check.sh` counts), when `AND` and `OR` sit at the same indentation level inside a parenthesised group spread over several lines. Writing the group on one line, or splitting the operands on separate lines at the group's own indentation, clears it.
- `elem x list` (prelude) is accepted written plain or backticked; both were probed in a one-line file.
- `@export` on a rule with no `GIVEN` is accepted (the questions on reg 77.993(3) and reg 92(1)).
- `YMD` through the keel's shim compares with `AT LEAST`, `AT MOST`, `BELOW` and `ABOVE` without the `__GEQ__` error that the prelude's own `YMD` gives (dialects.md row 53).
- Records and `MAYBE` of a record compare with `EQUALS`; a `DEONTIC` does not, and none is used.
- Not used here: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, a section `GIVEN`, `TYPICALLY`, opaque `DECLARE`, sets, `EVERY`, `RULES EFFECTIVE DATE`, `WAIT UNTIL`, `MUST DO`, an input named in an action (see dialects.md).

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
er5-admin-coverage-decision.l4                 0         0       0        0         0
er5-admin-direct-deposit.l4                    0         0       0        0         0
er5-admin-electronic-systems.l4                0         0       0        0         0
er5-admin-reconsideration.l4                   0         0       0        0         0
er5-admin-sin.l4                               0         0       0        0         0
er5-cases-seat.l4                              0       150       0        0         0
er5-pilot-24.l4                                0         0       0        0         0
er5-pilot-claims.l4                            0         0       0        0         0
er5-pilot-earnings.l4                          0         0       0        0         0
er5-pilot-elections.l4                         0         0       0        0         0
er5-pilot-hours.l4                             0         0       0        0         0
er5-pilot-rate.l4                              0         0       0        0         0
er5-pilot-weeks.l4                             0         0       0        0         0
er5-seat.l4                                    0         0       0        0         0
er5-tests-admin-coverage-decision.l4           0        19       0        0         0
er5-tests-admin-direct-deposit.l4              0        27       0        0         0
er5-tests-admin-electronic-systems.l4          0        29       0        0         0
er5-tests-admin-reconsideration.l4             0        50       0        0         0
er5-tests-admin-sin.l4                         0        36       0        0         0
er5-tests-pilot-24.l4                          0        57       0        0         0
er5-tests-pilot-claims.l4                      0        72       0        0         0
er5-tests-pilot-earnings.l4                    0        79       0        0         0
er5-tests-pilot-elections.l4                   0        77       0        0         0
er5-tests-pilot-hours.l4                       0        42       0        0         0
er5-tests-pilot-rate.l4                        0        32       0        0         0
er5-tests-pilot-weeks.l4                       0       107       0        0         0
TOTAL (30 modules)                             0       777       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/SOR-96-332.txt er5-*.l4` prints:

```
srcrefs check: 384 src: lines, 193 runs, 230 locators, 0 problems
```

The string literals of 30 or more characters in the layer-1 modules were each checked to occur verbatim in `SOR-96-332.txt` (0 problems); the typographic apostrophe of the source is kept in them.
The `l4 check` of every `er5-` file prints no "follows code on its line" or "is at the end of the file" message and no "Unknown annotation" warning.

## Before this is worth relying on

- A person who knows Canadian employment insurance law should read each module against the Regulations, and the forks against the Act. In particular F-reg77.96b (the bar of reg 77.96(5)), F-reg77.95 (the marginal deduction) and F-reg77.8c (the cessation days).
- The three commencement days (regs 77.1, 77.994, 77.999) must come from the published regulations that made those sections; the text here does not carry them.
- The Schedule II tables (II.2, II.7, II.93, II.94), Schedule I and the regions (er6), reg 17's rates (er1), reg 24.1 (er2) and regs 35 and 36 (er3) are inputs here; this piece's answers are only as good as the inputs.
- The Direct Deposit Regulations (reg 92(1)) are not among the inputs; their sections 2 and 4 to 8 are not encoded.
- The Interpretation Act (counting of days, the meaning of "until" and "ceases ... on") is not among the inputs; the keel's F4 and the forks here stand in for it.
- The seat's yes/no inputs about ordinary residence in a region of a Schedule, about a form being approved, and about good cause are the person's and the Commission's judgments, not computations.
- Run only with the stable main build 1.6.98; `check.sh`'s comparison against a second binary was skipped (`L4_TARGET=unstable`, as the brief directs), so there is no second-compiler evidence.
