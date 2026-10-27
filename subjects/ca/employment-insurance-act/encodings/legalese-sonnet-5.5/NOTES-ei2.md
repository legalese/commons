# NOTES: Employment Insurance Act, piece ei2 (Act lines 670-1126: Part I second part from s 23.3(6), and Part II)

Written by the piece agent `ei2` (Sonnet 5.5) on 2026-10-24.
Source: the plain-text rendering `S.C.-1996-c.-23.txt` of the Justice Laws consolidation of the Employment Insurance Act, S.C. 1996, c. 23, current to 2026-09-30, last amended 2026-06-18.
The file was made by a converter script; it is not the official text, it is not marked up, and nothing in this folder claims to be verified against the official text.
The French version is equally authoritative and was not read.
`src:N` in a comment or an `@ref` is line N of that file.
The Regulations (`SOR-96-332.txt`, current to 2026-09-30) are not in this piece's range: where the Act leaves a figure or a condition to them, this piece takes it as a plain input and names the regulation and its piece (see "Cross-references out of my ranges").
Every rule in the `ei2-*.l4` files comes from the Act.

**Range.** Lines 670-1126 of the Act: the end of s 23.3 (subsections (6) to (9), the first four rows below, whose section opens at line 646 in piece ei1's range), ss 24 to 55 of Part I (work-sharing, courses, disqualification and disentitlement, penalties, non-assignment and repayment, claim procedure, regulations), and Part II (ss 56 to 65.2, employment support measures and the National Employment Service).

**Target.** The stable binary `l4 1.6.98 (main, 7689b0d, 2026-10-19)`; the dialect written is `main` (see "What the stable binary does not accept").

**Dates.**
My range holds no date of enactment, no assent date and no commencement rule: s 190, the Act's coming-into-force section, is in piece ei6's range (the keel's notes say so too).
So no rule here carries a `RULES EFFECTIVE DATE`, no date is defined with an `@ref`, and the text is one vintage (current to 2026-09-30).
Where a provision is limited by time, the date of the fact is an input.

**Files** (all in this folder, flat).

| file | what it holds |
| --- | --- |
| `eia-core*.l4`, `check.sh`, `srcrefs.py` | the keel's shared core and the supplied tools, unchanged |
| `ei2-nouns.l4` | the three types this piece declares: the kind of employment support measure (s 59), the way weeks are divided (s 23.3(6)), the ground of disqualification (s 27) |
| `ei2-s23-3-division.l4` | s 23.3(6) to (9): dividing the weeks of benefits for a critically ill adult, the 15-week maximum, the limitation, the provincial-law reduction |
| `ei2-work-sharing-and-courses.l4` | ss 24 to 26: work-sharing, courses and programs, benefits are not earnings |
| `ei2-disqualification.l4` | ss 27 to 28: disqualification in general and its duration |
| `ei2-leaving-and-misconduct.l4` | ss 29 to 35: the interpretation for ss 30 to 33, disqualification for misconduct or leaving, disentitlement for suspension, leave and anticipated loss, the union exception |
| `ei2-labour-disputes-and-absence.l4` | ss 36 to 37: labour disputes; prison inmates and persons outside Canada |
| `ei2-penalties.l4` | ss 38 to 41.1: penalties for claimants and for employers, limits, rescission, warnings |
| `ei2-repayment.l4` | ss 42 to 47: non-assignment, liability to repay, the return of benefits by claimants, employers and directors, debts to the Crown |
| `ei2-claim-procedure.l4` | ss 48 to 53: the claim, proof, conditions, information, reconsideration, notice |
| `ei2-hours-methods.l4` | ss 54 and 55: the regulation powers (inert, listed in the coverage table only) and the alternative methods of establishing hours (s 55(2) to (4)) |
| `ei2-employment-support.l4` | Part II, ss 56 to 65.2 |
| `ei2-tests-*.l4` | assertions on layer 1, expected values written by hand from the text |
| `ei2-seat.l4`, `ei2-cases-seat.l4` | layer 2: the seat's questions and worked cases |
| `NOTES.md`, `PROGRESS.md` | this file and the working log |

(The table lists the files as they exist; the ten `ei2-tests-*.l4` files are one per rule module except `ei2-nouns.l4`, which has none.)

## Seat

**The seat** is the one the brief fixes: a person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission.
For this range, which is the middle of Part I and all of Part II, the seat's questions are the ones such a person asks after the benefit period has been set: when they are disqualified or disentitled and for how long, what they may be penalised or made to repay, what they must do and prove to claim, and what the National Employment Service and the employment support measures owe them.
The seat is the individual to whom the law is applied (Commons CLAUDE.md, ruled 2026-10-18); the Commission, the Minister and the courts have no seat, and where a provision is addressed to the Commission the question is what the person is owed or exposed to ("Has the Commission done what it must after receiving my initial claim?", "Can the Commission impose a penalty on me?").

**The layers.**
Layer 1 is the ten `ei2-*.l4` rule modules and `ei2-nouns.l4`, written from the text alone, one module per Part, Chapter or natural group, every rule with an `@ref` and a verbatim quotation; they IMPORT the keel's modules and nothing of another piece.
Layer 2 is `ei2-seat.l4`: 101 `@export` questions, in the text's natural order under `§§` headings, each with `@desc` on every input worded as the person would be asked; and `ei2-cases-seat.l4`: 296 worked assertions, at least one for every question and usually one on each side of each threshold, each date and each figure.
The seat calls the layer-1 rules and the keel's rule `s 2(1) labour dispute`, and restates none of them; layer 1 itself calls the keel's `s 2(1) special benefits` (ss 28(5), 30(4), 34, 36(3)) and `s 2(1) insured person` (s 58); where a rule takes a `Period of days` or a `MAYBE`, the question builds it in the question's own `WHERE` or call from plain inputs.

**Who is not asked.**
The employer's provisions (s 39 penalties on employers, s 46(2) the employer's remittance) and the directors' (s 46.1) are encoded in layer 1 and have no question in this seat, because the person in it is the claimant.
An employer seat (`ei2-seat-employer.l4`) would ask them and mirror the claimant's cases.
Provisions that are only the Commission's own powers with no effect the claimant could ask about (s 61, financial assistance, and ss 62 and 63(1), the agreements; s 59 is asked as "can the Commission establish a measure to help me") get no question; they are still in layer 1.

**How a question that depends on a deeming or "no appeal" rule answers.**
Layer 1 answers a deeming rule (ss 24(3), 25(1), 26, 28(6), 28(7), 35, 36(5), 42(1), 47(1), 49(2), 52(3)(a), 65.2(1)) and a "no appeal" rule (ss 24(2), 25(2), 64) `JUST TRUE` when it applies and `NOTHING` when it does not, never `FALSE`.
The seat asks "Does section N treat me as ...?" and answers `TRUE` for `JUST TRUE` and `FALSE` for `NOTHING`; `FALSE` then means "not by this provision", and the comment at the head of `ei2-seat.l4` says so.

**Judgments.**
What the Commission "considers", "is satisfied of" or "is of the opinion" is asked as a fact about what the Commission has done or found.
"Good cause" (s 27(1)), "no reasonable alternative" (s 29(c)) and "suitable" (ss 27, 29) are asked as the person would answer them, and the decider's answer may differ.

**Figures and inputs the person cannot state.**
The Act's own figures are the modules' constants (7, 12 and 6 weeks; 700 hours; two years; three weeks; 3 and 9 times; $12,000; 36 and 72 months; six years; 15 weeks; 60 months and 3 of 10 years).
Amounts the Act leaves to the Regulations or the Commission (the hours required by section 7 or 7.1, the rate of weekly benefits, the maximum rate, the last day to claim, the benefits that would not have been paid) are asked as facts the person can find out, with the regulation named in the `@desc` where the text of the Regulations says what it is.
A change in any of them by the Commission or the Regulations would change the answers.

**Defaults of Commons CLAUDE.md followed or departed from.**
Followed: the Act alone, with the Regulations brought in only as named inputs; the actors the text names; judgments left to others answered conditionally; the Act's definitions worked out from facts (via the keel); the Act's own terms with a plain gloss; the operative sections in scope.
Departed from: none; the machinery (ss 24(1), 36(2), 54, 55(1), 60(3)) is out as `inert` in the coverage table.

**The one question that answers NOTHING.**
"What is the fewest weeks of disqualification the Act allows for my ground (s 28(1))?" returns a `MAYBE NUMBER`: `JUST 7` for grounds (a) and (b), `NOTHING` for (c), (d) and (1.1), for which s 28(1)(b) states only "not more than 6" and no least number.
Returning 0 would assert that the Act allows a disqualification of no weeks, which it does not say.
The companion question "Does section 28(1) set a least number of weeks of disqualification for my ground?" answers BOOLEAN, so the form can ask it first; the form's handling of a `MAYBE` result was not measured.
The other `THEN 0` arms in the seat are the law's own answer: "how much may the Commission deduct" when the conditions of s 42(3) are not met, and "how much is payable to me" when those of s 52(4) are not met.

## Jural relations

Hohfeld's correlatives: a right (claim) answers a duty; a privilege (liberty) answers a no-right; a power answers a liability; an immunity answers a disability.
Each relation is stated once, in the layer-1 rule named in the last column, and named neutrally there; the table gives both sides.
A disqualification or disentitlement is written as the Commission's privilege not to pay and the claimant's no-right for the weeks it covers.
"The Crown" is Her Majesty, to whom the debts of ss 47 and 65.2 are due; the Receiver General is its receiver.

| section | the party holding the right, privilege, power or immunity | the party bearing the duty, no-right, liability or disability | the L4 rule (module `ei2-...` as named in the coverage table) |
| --- | --- | --- | --- |
| s 23.3(6) | the claimants: a power to divide up to 15 remaining weeks as they agree | the Commission: liable to pay the weeks as divided; if they cannot agree, the prescribed rules (reg 41.6) divide them | `s 23.3(6) the number of remaining weeks that may be divided`, `s 23.3(6) the way the remaining weeks are divided` |
| s 23.3(8) | the Commission: a privilege not to pay compassionate care benefits for the adult during the s 23.3(3) period | the claimant: a no-right to them | `s 23.3(8) benefits under section 23.1 or 152.06 are not payable` |
| s 23.3(9) | the Commission: a power, and a duty ("shall"), to reduce or eliminate the benefits as prescribed | the claimant: liable to the reduction | `s 23.3(9) the benefits payable under section 23.3 are to be reduced or eliminated as prescribed` |
| s 24(2) | the Commission: an immunity from review of its direction on a work-sharing agreement | the claimant and employer: a disability to ask for review under s 112 | `s 24(2) the direction on a work sharing agreement is not subject to review under section 112` |
| s 24(3) | the claimant: a claim to be treated as unemployed and available in a work-sharing week | the Commission: a duty so to treat the claimant | `s 24(3) the claimant is unemployed and capable of and available for work during the week` |
| s 25(1) | the claimant: a claim to be treated as unemployed and available during a referred course, program or activity | the Commission: a duty so to treat the claimant | `s 25(1)(a) ...`, `s 25(1)(b) ...`, `s 25(1) ...` |
| s 25(2) | the Commission: an immunity from review of the referral decision | the claimant: a disability to ask for review under s 112 | `s 25(2) the decision about the referral is not subject to review under section 112` |
| s 26 | the claimant: an immunity from having such benefits counted as earnings (for Part I, Part IV, the Income Tax Act and the Canada Pension Plan) | the Commission and the Minister of National Revenue: a disability to count them | `s 26 the benefits paid are not earnings from employment` |
| s 27(1), (1.1) | the Commission: a privilege not to pay benefits to a disqualified claimant | the claimant: a no-right to benefits | `s 27(1) the claimant is disqualified from receiving benefits under Part I`, `s 27(1.1) ...` |
| s 28(1) | the Commission: a power to determine the weeks of disqualification | the claimant: liable to its determination; immune beyond 12 or 6 weeks and below 7 where the Act sets a least | `s 28(1) ...` |
| s 28(2) to (4) | the Commission: a privilege not to pay for the weeks served or carried forward | the claimant: a no-right for them; an immunity after 700 hours (s 28(4)) | `s 28(2) ...`, `s 28(3) ...`, `s 28(4) ...` |
| s 28(5) | the claimant: a claim to deferral while otherwise entitled to special benefits or s 25 benefits | the Commission: a duty ("shall") to defer | `s 28(5) the serving of the disqualification is deferred` |
| s 28(6), (7) | the Crown: benefits deemed paid for the weeks; the claimant (s 28(7)): a privilege to request a major-attachment benefit period | the claimant: the weeks count as paid; the Commission: a no-right to refuse the request on that ground | `s 28(6) ...`, `s 28(7) ...` |
| s 30(1) | the Commission: a privilege not to pay any benefits after misconduct or leaving without just cause; the claimant: an immunity if (a) the required hours since, or (b) a disentitlement under ss 31 to 33 | the claimant: a no-right; the Commission: a disability in cases (a) and (b) | `s 30(1) the claimant is disqualified from receiving any benefits` |
| s 30(4) | the claimant: a claim to suspension of the disqualification in a week otherwise entitled to special benefits | the Commission: a duty to suspend | `s 30(4) the disqualification is suspended for the week` |
| s 30(5), (6) | the Commission: a privilege not to count the excluded hours | the claimant: a no-right to use them to qualify, or for maximum weeks and rate | `s 30(5) ...`, `s 30(6) ...` |
| s 31, s 32(1), s 33(1) | the Commission: a privilege not to pay while suspended for misconduct, on leave without just cause, or after an anticipated loss | the claimant: a no-right until the event in (a), (b), (c), s 32(2), s 33(2) | `s 31 ...`, `s 32(1) ...`, `s 32(2) ...`, `s 33(1) ...`, `s 33(2) ...` |
| s 34 | the claimant: a claim to benefits in a week otherwise entitled to special benefits | the Commission: a duty to suspend the disentitlement | `s 34 the disentitlement is suspended for the week` |
| s 35 | the claimant: an immunity from ss 30 to 33 where staying would cost union rights | the Commission: a disability to disqualify or disentitle on that ground alone | `s 35 the claimant is not disqualified or disentitled under sections 30 to 33` |
| s 36(1) | the Commission: a privilege not to pay while a work stoppage lasts | the claimant: a no-right until the stoppage ends or regular work elsewhere | `s 36(1) the claimant is not entitled to receive benefits` |
| s 36(3), (4) | the claimant: a claim to suspension (3); an immunity if they prove non-involvement (4) | the Commission: a duty (3); a disability (4) | `s 36(3) ...`, `s 36(4) ...` |
| s 37 | the Commission: a privilege not to pay an inmate or a person outside Canada, except as prescribed | the claimant: a no-right | `s 37 the claimant is not entitled to receive benefits for the period` |
| s 38(1), (2) | the Commission: a power to impose a penalty on a claimant or person acting for them, up to the ceiling | the claimant or that person: a liability; an immunity above the ceiling | `s 38(1) ...`, `s 38(2) ...` |
| s 39(1) to (5) | the Commission: a power to impose a penalty on an employer, a person acting for or pretending to act for one, or an officer, director or agent, up to the ceiling | that person: a liability; an immunity above the ceiling | `s 39(1) ...`, `s 39(3) ...`, `s 39(2) ...`, `s 39(4) ...`, `s 39 the most the Commission may set ...` |
| s 40 | the person: an immunity from a penalty once a prosecution has begun or 36 months have run | the Commission: a disability to impose one | `s 40 a penalty shall not be imposed` |
| s 41 | the Commission: a power to rescind or reduce a penalty | the penalised person: liable to the decision (a favourable one) | `s 41 the Commission may rescind the imposition of the penalty, or reduce it` |
| s 41.1(1), (2) | the Commission: a power to warn instead of penalising, up to 72 months after the act | the person: liable to a warning | `s 41.1(1) ...`, `s 41.1(2) ...` |
| s 42(1) | the claimant: an immunity from any assignment, charge, attachment or security over benefits | every other person: a disability (the transaction is void) | `s 42(1) a transaction appearing to assign ... is void` |
| s 42(2), (3) | the Commission: a power to recover amounts out of benefits (2); to deduct and pay a government (3) | the person: liable; in (3) only if they consented | `s 42(2) ...`, `s 42(3) ...` |
| s 43, s 44 | the Crown: a claim to repayment of overpaid benefits (43); the Commission: a claim to the return of a payment without delay (44) | the claimant (43); the person who received it (44): a duty | `s 43 ...`, `s 44 ...` |
| s 45 | the Receiver General: a claim to the benefits that would not have been paid | the claimant: a duty to pay | `s 45 the amount the claimant shall pay to the Receiver General` |
| s 46(1), (2) | the Receiver General: a claim to the amount deducted (1) or the amount by which the employer's liability was reduced (2) | the employer, trustee or other payer: a duty to ascertain, deduct and remit (1); the employer: a duty to remit (2); the claimant: liable to the deduction | `s 46(1) ...`, `s 46(2) ...` |
| s 46.01 | the claimant and payer: an immunity from s 45 and s 46(1) after 36 months where the Commission thinks costs would equal or exceed the amount | the Crown: a disability | `s 46.01 ...` |
| s 46.1(1) to (4) | the Crown: a claim for the penalty against each director at the time of the act | each director: a duty jointly and severally with the corporation; an immunity unless (2), by due diligence (3), after six years (4) | `s 46.1(1) ...`, `(2) ...`, `(3) ...`, `(4) ...` |
| s 46.1(6), (7) | the director who pays: a claim to the Crown's preference and to an assignment of the certificate (6); to contribution (7) | the Commission: a duty to assign; the other directors: a duty to contribute | `s 46.1(6)(a) ...`, `(6)(b) ...`, `(7) ...` |
| s 47(1) to (4) | the Crown: the amounts are debts and recoverable; a power to deduct out of benefits (2) | the debtor: a duty; liable to the deduction; an immunity after 72 months, tolled during an appeal | `s 47(1) ...`, `s 47(2) ...`, `s 47(3) ...` |
| s 48(1), (2) | the Commission: a privilege not to establish a benefit period until the claim, proof and information are given | the claimant: a duty to claim, prove and supply | `s 48(1) ...`, `s 48(2) ...` |
| s 48(3), s 49(3) | the claimant: a claim to a decision and a notice | the Commission: a duty to decide and notify | `s 48(3) ...`, `s 49(3) ...` |
| s 49(1) | the Commission: a privilege not to pay a week until the claim and proof | the claimant: a duty to claim and prove | `s 49(1) ...` |
| s 49(2) | the claimant: a claim to the benefit of the doubt where the evidence is equally balanced | the Commission: a duty | `s 49(2) the claimant is given the benefit of the doubt on the issue` |
| s 50(1) to (4), (9) | the Commission: a privilege not to pay while a condition is unmet | the claimant: a duty to claim as directed, on the form, in time, and to give a mailing address | `s 50(1) ...` to `s 50(4) ...`, `s 50(9) ...` |
| s 50(5) to (8.1) | the Commission: a power to require information, attendance, registration, proof of efforts, a certificate | the claimant: liable to the requirement; a duty once it is made | `s 50(5) ...` to `s 50(8.1) ...` |
| s 50(10) | the Commission: a power to waive or vary a condition for the claimant's benefit | the claimant: liable (favourably) to the waiver | `s 50(10) ...` |
| s 51 | the claimant and the employer: a claim to an opportunity to give information, and to have it taken into account | the Commission: a duty | `s 51(a) ...`, `s 51(b) ...` |
| s 52(1), (5) | the Commission: a power to reconsider within 36 months, or 72 where a false or misleading statement was made | the claimant: a liability | `s 52(1) and (5) ...` |
| s 52(2), (4) | the claimant: a claim to a calculation and notice (2), and to payment of money they were entitled to (4) | the Commission: a duty | `s 52(2) ...`, `s 52(4) ...` |
| s 52(3) | the Crown: a claim to repayment (a); the debt arises on the day of notice (b) | the claimant: a duty to repay | `s 52(3)(a) ...`, `s 52(3)(b) ...` |
| s 53 | the Commission: a power to notify in the manner it considers adequate | the person: liable to that manner | `s 53 ...` |
| s 55(2) to (4) | the Commission: a power to authorize, alter, rescind an alternative method of counting hours; to agree with employers or employees and rescind | the person: liable to the method; the employer or employee: a power to agree, then liable | `s 55(2) ...`, `s 55(3) ...`, `s 55(4) ...` |
| s 57(1), (2) | the Commission's duty to establish measures by the guidelines and to work in concert and consult; no individual claim is created; (e) is the participant's expected commitment | participants and workers (no enforceable claim stated) | `s 57(1) ...`, `s 57(1)(e) ...`, `s 57(2) ...` |
| s 59, s 61 to 63 | the Commission: a power to establish measures, give financial assistance, make agreements | participants, recipients and the other parties: liable to them | `s 59 ...`, `s 61 ...`, `s 62 ...`, `s 63(1) ...` |
| s 60(1), (2)(a) | workers and employers: a claim to a national employment service that collects and shares employment information | the Commission: a duty | `s 60(1) ...`, `s 60(2)(a) ...` |
| s 60(2)(b) | the worker: a claim not to be discriminated against in a referral; the service: a privilege to give effect to a bona fide occupational requirement or a special programme | the service: a duty; the worker: a no-right in those two cases | `s 60(2)(b) the referral is as the Act requires` |
| s 64 | the Commission: an immunity from review of a decision on a measure (not a s 65.1 decision) | the person: a disability to ask for review under s 112 | `s 64 the decision is not subject to review under section 112` |
| s 65 | the Crown: a claim to repayment of loans, guarantees and amounts paid without entitlement | the person: a duty | `s 65 the amount the person is liable to repay` |
| s 65.1 | the Commission: a power to penalise a person given assistance, up to the assistance; to rescind or reduce | the person: a liability; an immunity after a prosecution has begun or 36 months | `s 65.1(1) ...` to `s 65.1(4) ...` |
| s 65.2 | the Crown: the amounts are debts, recoverable, with a power to deduct out of amounts payable | the person: a duty; liable to the deduction; an immunity after 72 months | `s 65.2(1) ...` to `s 65.2(3) ...` |
| none | - | - | the definitions and counting rules: s 29(a), (b), (b.1), (c); s 30(2), (3), (7); s 23.3(7) (a ceiling stated for greater certainty); s 36(5); s 56; s 58; and the regulation-making powers, inert: s 24(1), s 36(2), s 54, s 55(1), s 60(3) |

## Coverage table

One row per provision of lines 670 to 1126 of the Act: one per section, and one per subsection or paragraph wherever they differ in disposition or in the rule they state.
The marginal notes the converter keeps as separate lines (for example "Presumption", "No appeal") belong to the subsection that follows them and have no row of their own; the division headings ("Work-Sharing", "Courses, Programs and Employment Support Measures", "Disqualification and Disentitlement", "Penalties", "Non-assignment of Benefits and Liability to Return Benefits and Pay Penalties", "Claim Procedure", "Regulations", and the Part II heading) have one row each, marked `inert`.
Dispositions: `encoded` (layer 1, and layer 2 where the person would ask), `inert` (with its reason), `repealed or blank in this text`, `fork` (the reading is in the fork register).
`src:N` is a line of the Act's raw file.
A `where` is a module and the rule(s) that encode the provision; `seat` means the question is in `ei2-seat.l4`.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| s 23.3(6) Division of weeks of benefits | src:670-671 | fork | `ei2-s23-3-division` `s 23.3(6) the number of remaining weeks that may be divided`, `s 23.3(6) the way the remaining weeks are divided` | The tail of a section opened at src:646 (piece ei1). The 15-week ceiling is a figure of the text; the prescribed rules for a failure to agree are reg 41.6 (piece er3), an input. Fork ei2-F1 ("cannot agree"). |
| s 23.3(7) Maximum divisible number of weeks | src:672-673 | encoded | `ei2-s23-3-division` `s 23.3(7) the total number of weeks divided is within the ceiling` | MAYBE BOOLEAN: NOTHING when the subsection does not apply (not a 23.3 claim and a 152.062 claim in respect of the same adult). |
| s 23.3(8) Limitation, compassionate care benefits | src:674-675 | encoded | `ei2-s23-3-division` `s 23.3(8) benefits under section 23.1 or 152.06 are not payable` | The period is that of s 23.3(3) (piece ei1) or s 152.062(3) (piece ei5): an input. |
| s 23.3(9) Limitation, provincial law | src:676-677 | encoded | `ei2-s23-3-division` `s 23.3(9) the benefits payable under section 23.3 are to be reduced or eliminated as prescribed` | The reduction itself is "as prescribed"; no regulation among the inputs prescribes it for s 23.3 (see Cross-references). |
| Heading "Work-Sharing" | src:679 | inert | - | A division heading: it carries no text of its own, and it names the two sections (s 24 only) that follow. |
| s 24(1) Regulations for work-sharing benefits, lead-in | src:680-681 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations for the payment of work-sharing benefits to claimants employed under an approved work-sharing agreement. Regulation-making machinery; regs 42 to 49 (piece er3) are the regulations made under it and carry its content. |
| s 24(1)(a) | src:682 | inert | - | Power to define work-sharing employment for which benefits may be paid (reg 42, piece er3). |
| s 24(1)(b) | src:683 | inert | - | Power to prescribe the maximum number of weeks of work-sharing benefits (regs 42 to 49, piece er3). |
| s 24(1)(c) | src:684 | inert | - | Power to prescribe the method of paying work-sharing benefits. |
| s 24(1)(d) | src:685 | inert | - | Power to prescribe the weekly rate of work-sharing benefits (reg 48, piece er3). |
| s 24(1)(e) | src:686 | inert | - | Power to provide a method of setting the weekly insurable earnings of a claimant in work-sharing employment, for s 14 (reg 48, piece er3). |
| s 24(1)(f) | src:687 | inert | - | Power to prescribe how earnings from the employer or other sources are treated for benefit purposes (reg 47, piece er3). |
| s 24(1)(g) | src:688 | inert | - | Power to extend a qualifying or benefit period by up to the number of weeks of work-sharing employment (reg 45, piece er3). |
| s 24(1)(h) | src:689 | inert | - | Power to defer service of the waiting period until the work-sharing employment has ended (reg 46, piece er3). |
| s 24(1)(i) | src:690 | inert | - | Residual power to provide for other matters necessary to carry out the purposes of s 24. |
| s 24(2) No appeal | src:691-692 | encoded | `ei2-work-sharing-and-courses` `s 24(2) the direction on a work sharing agreement is not subject to review under section 112` | Seat. The review is s 112 (piece ei4). |
| s 24(3) Presumption | src:693-694 | encoded | `ei2-work-sharing-and-courses` `s 24(3) the claimant is unemployed and capable of and available for work during the week` | MAYBE BOOLEAN: a deeming rule; seat. |
| Heading "Courses, Programs and Employment Support Measures" | src:696 | inert | - | A division heading: it carries no text of its own. |
| s 25(1)(a) Status of claimants: a course or program | src:697-699 | encoded | `ei2-work-sharing-and-courses` `s 25(1)(a) attending a referred course or program of instruction or training` | Seat. |
| s 25(1)(b) Status of claimants: another employment activity | src:697, 700-702 | fork | `ei2-work-sharing-and-courses` `s 25(1)(b) participating in a referred employment activity` | Which measures are prescribed is reg 50 (piece er3), an input. Seat. Fork ei2-F15 ("other than" qualifies the measure only). |
| s 25(1) (the lead-in joined to (a) and (b)) | src:698 | encoded | `ei2-work-sharing-and-courses` `s 25(1) the claimant is unemployed and capable of and available for work during the period` | MAYBE BOOLEAN: a deeming rule. |
| s 25(2) No appeal | src:703-704 | encoded | `ei2-work-sharing-and-courses` `s 25(2) the decision about the referral is not subject to review under section 112` | Seat. |
| s 26 Benefits are not earnings | src:705-706 | fork | `ei2-work-sharing-and-courses` `s 26 the benefits paid are not earnings from employment` | MAYBE BOOLEAN; seat. Fork ei2-F15. |
| Heading "Disqualification and Disentitlement" | src:708 | inert | - | A division heading: it carries no text of its own. |
| s 27(1) Disqualification, general: lead-in | src:709-710 | encoded | `ei2-disqualification` `s 27(1) the claimant is disqualified from receiving benefits under Part I` | "Without good cause" is a judgment input. Seat. |
| s 27(1)(a) | src:711 | encoded | `ei2-disqualification` `s 27(1)(a) not applying for or accepting a suitable employment` | "Suitable" is for regulations (s 54(k.1); reg 9.002, piece er1): an input. |
| s 27(1)(b) | src:712 | encoded | `ei2-disqualification` `s 27(1)(b) not taking advantage of an opportunity for suitable employment` | |
| s 27(1)(c) | src:713 | encoded | `ei2-disqualification` `s 27(1)(c) not carrying out a written direction of the Commission` | Reasonableness of the direction is an input. |
| s 27(1)(d) | src:714-716 | encoded | `ei2-disqualification` `s 27(1)(d) not attending an interview directed by the Commission` | (i) and (ii) are alternative purposes. |
| s 27(1.1) Termination of referral | src:717-723 | encoded | `ei2-disqualification` `s 27(1.1)(a) ...`, `s 27(1.1)(b) ...`, `s 27(1.1) the claimant is disqualified from receiving benefits under Part I` | (b)(i)'s "in the opinion of the Commission" is an input. Seat. |
| s 27(2) | src:724 | repealed or blank in this text | - | The text shows `(2) [Repealed, 2016, c. 12, s. 102]`. |
| s 27(3) | src:725 | repealed or blank in this text | - | The text shows `(3) [Repealed, 2012, c. 19, s. 605]`. |
| s 28(1) Duration of disqualification | src:726-729 | encoded | `ei2-disqualification` `s 28(1) the fewest weeks ...`, `s 28(1) the most weeks ...`, `s 28(1) the number of weeks determined is within the limits of the Act` | 7, 12 and 6 are figures of the text; the number the Commission determines is an input. Seat. |
| s 28(2) When disqualification is to be served | src:730-731 | fork | `ei2-disqualification` `s 28(2) the week is served as a week of disqualification` | Fork ei2-F2. |
| s 28(3) Disqualification to be carried forward | src:732-733 | fork | `ei2-disqualification` `s 28(3) a benefit period is established within two years after the event`, `s 28(3) the weeks of disqualification carried forward into the later benefit period` | Fork ei2-F3. Seat. |
| s 28(4) Limitation | src:734-735 | encoded | `ei2-disqualification` `s 28(4) no weeks of disqualification are carried forward` | 700 hours is a figure of the text. |
| s 28(5) Deferral | src:736-737 | encoded | `ei2-disqualification` `s 28(5) the serving of the disqualification is deferred` | |
| s 28(6) Presumption | src:738-739 | encoded | `ei2-disqualification` `s 28(6) benefits are deemed to be paid for the week` | MAYBE BOOLEAN: a deeming rule. |
| s 28(7) Exception | src:740-741 | encoded | `ei2-disqualification` `s 28(7) the deeming of benefits as paid is no bar to the request` | MAYBE BOOLEAN; the request is under s 10(6) (piece ei1). |
| s 29 Interpretation, lead-in "For the purposes of sections 30 to 33," | src:742-743 | encoded | `ei2-leaving-and-misconduct` (it scopes the rules below) | The five definitions below apply to ss 30 to 33 only, and the rules for them are named `s 29(...)`. |
| s 29(a) "employment" | src:744 | encoded | `ei2-leaving-and-misconduct` `s 29(a) the employment is an employment for the purposes of sections 30 to 33` | Differs from s 2(1) "employment" (keel notes). |
| s 29(b) "loss of employment" | src:745 | encoded | `ei2-leaving-and-misconduct` `s 29(b) loss of employment` | Includes suspension; excludes loss on account of union membership or lawful activity. |
| s 29(b.1)(i) to (iii) "voluntarily leaving an employment" | src:746-749 | encoded | `ei2-leaving-and-misconduct` `s 29(b.1) voluntarily leaving an employment`, `s 29(b.1) the day on which a refusal counts as the voluntary leaving` | Three refusals, each with the day the leaving occurs. |
| s 29(c) "just cause", lead-in | src:750 | fork | `ei2-leaving-and-misconduct` `s 29(c) just cause for voluntarily leaving an employment or taking leave exists` | Fork ei2-F4: the test is "no reasonable alternative, having regard to all the circumstances"; seat. |
| s 29(c)(i) to (xiv) the fourteen circumstances | src:751-764 | encoded | `ei2-leaving-and-misconduct` `s 29(c) one of the circumstances listed in the Act is present` | (xiv) is filled by reg 51.1 (piece er3), an input. Seat. |
| s 30(1) Disqualification, misconduct or leaving without just cause | src:765-768 | fork | `ei2-leaving-and-misconduct` `s 30(1) the claimant is disqualified from receiving any benefits` | Seat. Fork ei2-F5 (s 35 overrides the leaving limb). |
| s 30(2) Length of disqualification | src:769-770 | encoded | `ei2-leaving-and-misconduct` `s 30(2) the week is a week of the benefit period following the waiting period` | The benefit and waiting periods are ei1's, inputs. |
| s 30(3) Not retroactive | src:771-772 | encoded | `ei2-leaving-and-misconduct` `s 30(3) the week is not a week before the week in which the event occurs` | |
| s 30(4) Suspension | src:773-774 | encoded | `ei2-leaving-and-misconduct` `s 30(4) the disqualification is suspended for the week`; `s 30(2) to (4) the week is a week of disqualification` | The text says "Despite subsection (6)": finding 3. |
| s 30(5) Restriction on qualifying for benefits | src:775-778 | fork | `ei2-leaving-and-misconduct` `s 30(5) the hours that may be used to qualify under section 7 or 7.1` | Seat. Fork ei2-F14 ("as described in subsection (1)"). |
| s 30(6) Restriction on number of weeks and rate | src:779-780 | encoded | `ei2-leaving-and-misconduct` `s 30(6) the hours that may be used to determine the maximum weeks and the rate of weekly benefits` | Sections 12(2) and 14 are ei1's. |
| s 30(7) Interpretation | src:781-782 | encoded | tested in `ei2-tests-leaving-and-misconduct` | Declaratory ("for greater certainty"): s 30(1) has no input for either fact, so it already says this; recorded as the test it is (phrasebook 10.1). |
| s 31 Disentitlement, suspension for misconduct | src:783-787 | fork | `ei2-leaving-and-misconduct` `s 31 the claimant is not entitled to receive benefits` | The three "until" events are facts about the day in question. Seat. Fork ei2-F13. |
| s 32(1) Disentitlement, leave without just cause | src:788-791 | encoded | `ei2-leaving-and-misconduct` `s 32(1) the claimant who takes leave is disentitled` | Seat. |
| s 32(2) Duration of disentitlement | src:792-796 | fork | `ei2-leaving-and-misconduct` `s 32(2) the disentitlement has ended` | | Fork ei2-F13. |
| s 33(1) Disentitlement, anticipated loss of employment | src:797-800 | fork | `ei2-leaving-and-misconduct` `s 33(1) the claimant is not entitled to receive benefits` | Fork ei2-F6 (three weeks before), ei2-F5. Seat. |
| s 33(2) Duration of disentitlement | src:801-802 | fork | `ei2-leaving-and-misconduct` `s 33(2) the disentitlement is still in force on the day` | Fork ei2-F7. |
| s 34 Suspension of disentitlement | src:803-804 | encoded | `ei2-leaving-and-misconduct` `s 34 the disentitlement is suspended for the week` | |
| s 35 Exception | src:805-808 | fork | `ei2-leaving-and-misconduct` `s 35 the claimant is not disqualified or disentitled under sections 30 to 33` | MAYBE BOOLEAN; fork ei2-F5. Seat. |
| s 36(1) Labour disputes | src:809-812 | fork | `ei2-labour-disputes-and-absence` `s 36(1) the claimant is not entitled to receive benefits` | "Subject to the regulations" (regs 52, 53, piece er3); seat. Fork ei2-F13. |
| s 36(2) Regulations | src:813-814 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations determining the days of disentitlement in a week of a claimant who loses or cannot resume part-time employment because of the stoppage; regulation-making machinery, exercised by reg 52 (piece er3). |
| s 36(3) Suspension of disentitlement | src:815-818 | encoded | `ei2-labour-disputes-and-absence` `s 36(3) the disentitlement is suspended for the period` | |
| s 36(4) Non-application | src:819-820 | encoded | `ei2-labour-disputes-and-absence` `s 36(4) this section does not apply to the claimant`; `s 36 the claimant is disentitled on the day` | Seat. |
| s 36(5) Separate branches of work | src:821-822 | encoded | `ei2-labour-disputes-and-absence` `s 36(5) each department is a separate factory or workshop` | MAYBE BOOLEAN: a deeming rule. |
| s 37 Prison inmates and persons outside Canada | src:823-826 | encoded | `ei2-labour-disputes-and-absence` `s 37 the claimant is not entitled to receive benefits for the period` | "Except as may otherwise be prescribed": regs 54, 55 (piece er3), one BOOLEAN input. Seat. |
| Heading "Penalties" | src:828 | inert | - | A division heading: it carries no text of its own. |
| s 38(1) Penalty for claimants, etc.: lead-in and (a) to (h) | src:829-838 | encoded | `ei2-penalties` `s 38(1) the Commission may impose a penalty on the claimant or a person acting for the claimant` | The Commission's opinion is an input; the eight acts are alternatives. Seat. |
| s 38(2)(a) Maximum penalty: three times the weekly rate | src:839-841 | encoded | `ei2-penalties` `s 38(2)(a) three times the claimant's rate of weekly benefits` | The rate is s 14 (piece ei1), an input. |
| s 38(2)(b) Maximum penalty: paragraph (1)(c) acts | src:842-844 | fork | `ei2-penalties` `s 38(2)(b)(i) ...`, `s 38(2)(b)(ii) ...` | Fork ei2-F8. |
| s 38(2)(c) Maximum penalty: no benefit period | src:845 | fork | `ei2-penalties` `s 38(2)(c) three times the maximum rate of weekly benefits in effect when the act or omission occurred`; all four combined in `s 38(2) the most the Commission may set as the amount of the penalty` | Fork ei2-F8. Seat. |
| s 38(3) Determination under subsection 145(2) | src:846-847 | encoded | `ei2-penalties` `s 38(3) the repaid weeks are deemed to be weeks of regular benefits paid for the purposes of subsection 145(2)` | MAYBE BOOLEAN: a deeming rule; s 145(2) is ei4's. |
| s 39(1) Penalty for employers, etc.: lead-in and (a) to (e) | src:848-854 | encoded | `ei2-penalties` `s 39(1) the Commission may impose a penalty on the employer or a person acting for the employer` | Employer's provision: layer 1 only (no employer seat in this piece). |
| s 39(2) Maximum penalty | src:855-856 | encoded | `ei2-penalties` `s 39(2) nine times the maximum rate of weekly benefits in effect when the penalty is imposed` | |
| s 39(3) Officers, etc., of corporations | src:857-858 | encoded | `ei2-penalties` `s 39(3) the Commission may impose a penalty on an officer, director or agent of the corporation` | |
| s 39(4) Contravention of information requirements | src:859-862 | encoded | `ei2-penalties` `s 39(4) the greater of $12,000 and the penalty imposed under section 38` | $12,000 is a figure of the text. |
| s 39(5) Major contraventions | src:863-864 | fork | `ei2-penalties` `s 39 the most the Commission may set as the amount of the penalty` | Fork ei2-F9; the regulations (s 54(g.1), a maximum of $25,000) are not among the inputs: an amount input. |
| s 40 Limitation on imposition of penalties | src:865-868 | fork | `ei2-penalties` `s 40 a penalty shall not be imposed` | 36 months is a figure of the text; fork ei2-F10. Seat. |
| s 41 Rescission, etc., of penalty | src:869-870 | encoded | `ei2-penalties` `s 41 the Commission may rescind the imposition of the penalty, or reduce it` | The Commission's satisfaction is an input. Seat. |
| s 41.1(1) Warning | src:871-872 | encoded | `ei2-penalties` `s 41.1(1) the Commission may issue a warning instead of setting the amount of a penalty` | Seat. |
| s 41.1(2) Limitation period | src:873-874 | fork | `ei2-penalties` `s 41.1(2) a warning may be issued on the day` | 72 months is a figure of the text; fork ei2-F10. Seat. |
| Heading "Non-assignment of Benefits and Liability to Return Benefits and Pay Penalties" | src:876 | inert | - | A division heading: it carries no text of its own. |
| s 42(1) Benefits not assignable | src:877-878 | encoded | `ei2-repayment` `s 42(1) a transaction appearing to assign, charge, attach, anticipate or give benefits as security is void` | MAYBE BOOLEAN; seat. |
| s 42(2) Exception, recovery of amounts payable | src:879-880 | encoded | `ei2-repayment` `s 42(2) the amount may be recovered out of the benefits payable to the person` | Seat. |
| s 42(3) Exception, payment to other governments | src:881-882 | encoded | `ei2-repayment` `s 42(3) the Commission may deduct from the benefits and pay to the government or authority`, `s 42(3) the amount the Commission may deduct and pay` | "Subject to the regulations": reg 57 (piece er3). Seat. |
| s 43 Liability for overpayments | src:883-886 | encoded | `ei2-repayment` `s 43 the claimant is liable to repay the amount`, `s 43 the amount the claimant is liable to repay` | Seat. |
| s 44 Liability to return overpayment | src:887-888 | encoded | `ei2-repayment` `s 44 the amount the person shall return without delay` | "Without delay" has no number in the text. Seat. |
| s 45 Return of benefits by claimant | src:889-890 | encoded | `ei2-repayment` `s 45 the amount the claimant shall pay to the Receiver General` | The benefits that would not have been paid are an input (regs 35 to 39, piece er3). Seat. |
| s 46(1) Return of benefits by employer or other person | src:891-892 | encoded | `ei2-repayment` `s 46(1) the amount to deduct from the earnings payable to the claimant and remit to the Receiver General` | The payer's duty; its effect on the claimant's earnings is asked in the seat. |
| s 46(2) Return of benefits by employer | src:893-894 | encoded | `ei2-repayment` `s 46(2) the amount the employer shall remit to the Receiver General` | Employer's provision: layer 1 only. |
| s 46.01 Limitation | src:895-896 | fork | `ei2-repayment` `s 46.01 no amount is payable under section 45 or deductible under subsection 46(1)` | The Commission's opinion is an input; 36 months is a figure of the text; fork ei2-F10. Seat. |
| s 46.1(1) Liability of directors to pay penalties | src:897-898 | encoded | `ei2-repayment` `s 46.1(1) the director is jointly and severally liable, together with the corporation, to pay the penalty` | A director's provision: layer 1 only. |
| s 46.1(2) Limitations on liability | src:899-903 | encoded | `ei2-repayment` `s 46.1(2) a condition of the directors' liability is met` | "Unless (a), (b) or (c)": a condition of liability, as the text says. |
| s 46.1(3) Defence of due diligence | src:904-905 | encoded | `ei2-repayment` `s 46.1(3) the director is not liable by reason of due diligence` | The standard is a judgment: a BOOLEAN. |
| s 46.1(4) Limitation period | src:906-907 | fork | `ei2-repayment` `s 46.1(4) the action or proceedings may be commenced` | Six years: a figure of the text; fork ei2-F10. |
| s 46.1(5) Amount recoverable | src:908-909 | encoded | `ei2-repayment` `s 46.1(5) the amount recoverable from a director` | |
| s 46.1(6) Preference | src:910-913 | encoded | `ei2-repayment` `s 46.1(6)(a) ...`, `s 46.1(6)(b) ...` | |
| s 46.1(7) Contribution from other directors | src:914-915 | encoded | `ei2-repayment` `s 46.1(7) the director is entitled to contribution from the other director` | |
| s 47(1) Debts to Crown | src:916-917 | encoded | `ei2-repayment` `s 47(1) the amount is a debt due to Her Majesty` | MAYBE BOOLEAN. Seat. |
| s 47(2) Recovery | src:918-919 | encoded | `ei2-repayment` `s 47(2) the amount of the indebtedness may be deducted and retained out of the benefits` | Seat. |
| s 47(3) Limitation | src:920-921 | fork | `ei2-repayment` `s 47(3) the amount may still be recovered` | 72 months: a figure of the text; fork ei2-F10. Seat. |
| s 47(4) Appeals | src:922-923 | fork | `ei2-repayment` `s 47(3) the amount may still be recovered` | Fork ei2-F11: how the pending days are counted. |
| Heading "Claim Procedure" | src:925 | inert | - | A division heading: it carries no text of its own. |
| s 48(1) Claim required | src:926-927 | fork | `ei2-claim-procedure` `s 48(1) the first condition on which a benefit period may be established is met` | A necessary condition; when a benefit period is established is ss 9 and 10 (piece ei1). Seat. Fork ei2-F16 (necessary, not sufficient). |
| s 48(2) Information required | src:928-929 | fork | `ei2-claim-procedure` `s 48(2) the second condition on which a benefit period may be established is met` | Seat. Fork ei2-F16. |
| s 48(3) Notification | src:930-931 | encoded | `ei2-claim-procedure` `s 48(3) the Commission has done what it must on receiving the initial claim` | What the claimant is owed. Seat. |
| s 49(1) Proof required | src:932-935 | fork | `ei2-claim-procedure` `s 49(1) the person has done what is needed to be entitled to receive benefits for the week` | A necessary condition. Seat. Fork ei2-F16. |
| s 49(2) Benefit of the doubt | src:936-937 | encoded | `ei2-claim-procedure` `s 49(2) the claimant is given the benefit of the doubt on the issue` | MAYBE BOOLEAN; composes with ss 30 to 33 by the caller. Seat. |
| s 49(3) Notification | src:938-939 | encoded | `ei2-claim-procedure` `s 49(3) the Commission has done what it must on receiving the claim for the week` | Seat. |
| s 50(1) Entitlement to benefits | src:940-941 | encoded | `ei2-claim-procedure` `s 50(1) the claimant is not entitled to receive benefits for as long as a condition or requirement is not met` | Seat. |
| s 50(2) How a claim must be made | src:942-943 | encoded | `ei2-claim-procedure` `s 50(2) the claim is made as directed at the proper place` | Seat. |
| s 50(3) Form | src:944-945 | encoded | `ei2-claim-procedure` `s 50(3) the claim is made on the proper form` |  |
| s 50(4) Time | src:946-947 | encoded | `ei2-claim-procedure` `s 50(4) the claim for the week is made within the prescribed time` | The prescribed time is reg 26 (piece er2): the last day is an input. Seat. |
| s 50(5) Additional information | src:948-949 | encoded | `ei2-claim-procedure` `s 50(5) the requirement to provide additional information is met` | A power of the Commission; once exercised, a requirement. Seat. |
| s 50(6) Making claim or providing information in person | src:950-951 | encoded | `ei2-claim-procedure` `s 50(6) the requirement to attend in person is met` | Seat. |
| s 50(7) Registration for employment | src:952-953 | encoded | `ei2-claim-procedure` `s 50(7) the requirement to register for employment is met` | Seat. |
| s 50(8) Proof of efforts to obtain employment | src:954-955 | encoded | `ei2-claim-procedure` `s 50(8) the requirement to prove efforts to obtain employment is met` | The criteria are s 54(k.2) and reg 9.001 (piece er1). Seat. |
| s 50(8.1) Proof, additional certificate | src:956-957 | encoded | `ei2-claim-procedure` `s 50(8.1) the requirement to provide an additional certificate is met` | Seat. |
| s 50(9) Mailing address | src:958-959 | encoded | `ei2-claim-procedure` `s 50(9) the requirement to provide a mailing address is met` | Seat. |
| s 50(10) Waiver or variation of requirements | src:960-961 | encoded | `ei2-claim-procedure` `s 50(10) the Commission may waive or vary a condition or requirement` | The Commission's opinion is an input. Seat. |
| s 51 Information | src:962-965 | encoded | `ei2-claim-procedure` `s 51(a) ...`, `s 51(b) ...` | What the claimant and the employer are owed. Seat. |
| s 52(1) Reconsideration of claim | src:966-967 | fork | `ei2-claim-procedure` `s 52(1) and (5) the Commission may reconsider the claim on the day` | 36 months is a figure of the text; fork ei2-F10. Seat. |
| s 52(2) Decision | src:968-969 | encoded | `ei2-claim-procedure` `s 52(2) the Commission must calculate the amount of the money and notify the claimant of its decision` | Seat. |
| s 52(3) Amount repayable | src:970-973 | encoded | `ei2-claim-procedure` `s 52(3)(a) ...`, `s 52(3)(b) ...` | (b) fixes the day liability arises for s 47(3). Seat. |
| s 52(4) Amount payable | src:974-975 | encoded | `ei2-claim-procedure` `s 52(4) the amount payable to the claimant` | The claimant's claim. Seat. |
| s 52(5) Extended time to reconsider claim | src:976-977 | encoded | `ei2-claim-procedure` `s 52(1) and (5) the Commission may reconsider the claim on the day` | 72 months is a figure of the text; the Commission's opinion is an input. Seat. |
| s 53 Notification | src:978-979 | encoded | `ei2-claim-procedure` `s 53 the person may be notified in that manner` | Seat. |
| Heading "Regulations" | src:981-982 | inert | - | A division heading, repeated as the marginal note of s 54: it carries no text of its own. |
| s 54 Regulations, lead-in | src:983 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations on the matters listed in its paragraphs (a) to (z.4). Regulation-making machinery: the regulations made under it are the Employment Insurance Regulations (SOR/96-332), which pieces er1 to er6 encode, and the rows below say what each paragraph lets be prescribed. |
| s 54(a) | src:984 | inert | - | Power to make regulations on: conditions on which the requirement under Part I or Part VII.1 of serving a waiting period may be waived (reg 39.1, piece er3, is made on that subject). |
| s 54(b) | src:985 | inert | - | Power to make regulations on: what is a working day or working week in any employment or for Part VII.1 (reg 32, piece er2, looks like its exercise). |
| s 54(c) | src:986-989 | inert | - | Power to make regulations on: the conditions and circumstances under which a claimant who is self-employed or in non-insurable employment, or whose pattern of full-time employment differs from the usual, is considered to have worked or not worked a full working week (regs 29 to 31, piece er2, look like its exercise). |
| s 54(c.1) | src:990 | inert | - | Power to make regulations on: how to determine the average number of weeks of regular benefits for paragraph 7.1(6)(b) (reg 13, piece er1, cites that paragraph). |
| s 54(c.2) | src:991 | inert | - | Power to make regulations on: circumstances for the paragraphs of ss 10, 23.1 to 23.3, 152.06 to 152.062 and 152.11 that name them; not matched to a regulation by this piece. |
| s 54(d) | src:992 | inert | - | Power to make regulations on: who are dependent children, the low-income family eligibility criteria and the family supplement amounts, for ss 16 and 152.17 (reg 34, piece er2, deals with the family supplement). |
| s 54(d.1) | src:993 | inert | - | Power to make regulations on: how to determine the period for which benefits were claimed, for ss 19(3) and 152.18(3); not matched to a regulation by this piece. |
| s 54(e) | src:994 | inert | - | Power to make regulations on: the deduction under s 19 of earnings and allowances mentioned in s 19(4); not matched to a regulation by this piece. |
| s 54(f) | src:995 | inert | - | Power to make regulations on: the amount deducted under s 20(2) from weekly benefits where the claimant normally works other than a five-day week; not matched to a regulation by this piece. |
| s 54(f.1) | src:996 | repealed or blank in this text | - | The text shows `(f.1) [Not in force]`: the paragraph is not in force and has no wording in this text. |
| s 54(f.2) | src:997 | repealed or blank in this text | - | The text shows `(f.2) [Repealed, 2017, c. 20, s. 240]`. |
| s 54(f.21) | src:998 | inert | - | Power to make regulations on: what is a medical doctor, a nurse practitioner, a family member, a critically ill child and a critically ill adult, for ss 23.1 to 23.3 and 152.06 to 152.062 (reg 1, piece er1, defines them). |
| s 54(f.3) | src:999 | inert | - | Power to make regulations on: what is care or support, for the same sections (reg 1(5), piece er1). |
| s 54(f.4) | src:1000 | inert | - | Power to make regulations on: classes of medical practitioners and the circumstances in which a certificate may be issued (reg 41.2, piece er3). |
| s 54(f.5) | src:1001 | inert | - | Power to make regulations on: a shorter period for ss 23.1(5) and 152.06(4) and a minimum number of weeks for ss 12(4.3) and 152.14(7); not matched to a regulation by this piece. |
| s 54(f.6) | src:1002 | inert | - | Power to make regulations on: requirements for the paragraphs of ss 23.1(7), 23.2(6), 23.3(5), 152.06(6), 152.061(6) and 152.062(5) that name them; not matched to a regulation by this piece. |
| s 54(f.7) | src:1003 | inert | - | Power to make regulations on: rules for ss 23(4), 23.1(9), 23.2(8), 23.3(6) and their self-employed counterparts: how weeks are divided where claimants cannot agree (reg 41.6, piece er3). |
| s 54(g) | src:1004 | inert | - | Power to make regulations on: the circumstances that constitute the commencement or termination of a stoppage of work, for s 36 (reg 53, piece er3, deals with the termination). |
| s 54(g.1) | src:1005 | inert | - | Power to make regulations on: what is a major contravention for s 39(5), and the amount or maximum amount of its penalty, up to $25,000; the words "major contravention" do not occur in the Regulations file, so the amount for s 39(5) is an input. |
| s 54(h) | src:1006 | inert | - | Power to make regulations on: claims by, and payment of benefits to, any person or agency on behalf of deceased or incapacitated persons or persons with mental disabilities (the Regulations' Part I heading before reg 27, piece er2). |
| s 54(i) | src:1007 | inert | - | Power to make regulations on: additional conditions and terms, and restrictions on amount or period, for persons paid by the piece or otherwise than by time; not matched to a regulation by this piece. |
| s 54(j) | src:1008 | inert | - | Power to make regulations on: prohibiting or restricting benefits for persons in an industry or occupation with an annual period of no work, in the Commission's opinion; not matched to a regulation by this piece. |
| s 54(k) | src:1009 | inert | - | Power to make regulations on: ratifying amounts paid to persons not entitled to them and writing off those amounts, penalties and costs (regs 55.2 and 56, piece er3). |
| s 54(k.1) | src:1010 | inert | - | Power to make regulations on: criteria for what constitutes suitable employment for different categories of claimants (reg 9.002, piece er1). |
| s 54(k.2) | src:1011 | inert | - | Power to make regulations on: criteria for what constitutes reasonable and customary efforts, for s 50(8) (reg 9.001, piece er1). |
| s 54(l) | src:1012 | inert | - | Power to make regulations on: proof of fulfilment of the conditions and of the absence of disqualification, and the attendance of insured persons for that purpose; not matched to a regulation by this piece. |
| s 54(m) | src:1013 | inert | - | Power to make regulations on: the manner in which claims are made and the information to be provided with them; not matched to a regulation by this piece. |
| s 54(n) | src:1014 | inert | - | Power to make regulations on: the procedure for considering and examining claims and questions, and how a question may be raised about the continuation of benefits; not matched to a regulation by this piece. |
| s 54(o) | src:1015 | inert | - | Power to make regulations on: the payment of benefits during the period between an application for determination of a question or claim and its final determination; not matched to a regulation by this piece. |
| s 54(p) | src:1016 | inert | - | Power to make regulations on: the time and manner of paying benefits; not matched to a regulation by this piece. |
| s 54(q) | src:1017 | inert | - | Power to make regulations on: requiring employers to provide information on which entitlement depends, the time and manner of providing it, and its certification; not matched to a regulation by this piece. |
| s 54(r) | src:1018 | inert | - | Power to make regulations on: how to ascertain a claimant's employment history where the employer has not provided a record of employment or cannot; the Regulations' provisions on records of employment (piece er2). |
| s 54(s) | src:1019 | inert | - | Power to make regulations on: defining and determining earnings, their amount and their allocation to weeks (regs 35 to 39, piece er3). |
| s 54(t) | src:1020 | inert | - | Power to make regulations on: criteria for what constitutes a supplemental unemployment benefit plan and the making of those determinations (reg 37, piece er3). |
| s 54(u) | src:1021 | inert | - | Power to make regulations on: the circumstances and time at which an interruption of earnings occurs (regs 14 and 14.01, piece er1). |
| s 54(v) | src:1022 | inert | - | Power to make regulations on: conditions under which benefits may be paid in advance (piece er2, payments in advance). |
| s 54(w) | src:1023 | inert | - | Power to make regulations on: regions for Part I and Part VIII and their boundaries (reg 18 and Schedule I, pieces er1 and er6). |
| s 54(x) | src:1024 | inert | - | Power to make regulations on: the regional rates of unemployment or their averages that apply to a claimant, including an estimate for status Indians on Indian reserves (reg 17, piece er1). |
| s 54(y) | src:1025-1027 | inert | - | Power to make regulations on: the information and evidence a claimant must give to prove inability to work because of illness, injury or quarantine, or pregnancy or the expected date of confinement (reg 40, piece er3). |
| s 54(z) | src:1028-1032 | inert | - | Power to make regulations on: regulations for carrying out s 14: which weeks count as weeks of insurable earnings in a calculation period and what amounts are the insurable earnings, and the allocation of insurable earnings to a calculation period (regs 22 to 24, piece er2). |
| s 54(z.1) | src:1033 | inert | - | Power to make regulations on: allocating hours of insurable employment to a qualifying period (piece er2, allocation of hours and earnings). |
| s 54(z.2) | src:1034-1036 | inert | - | Power to make regulations on: the circumstances in which a claimant who leaves employment in an employer work-force reduction process that preserves co-workers' employment may be paid benefits despite s 30, and what a work-force reduction process is (reg 51, piece er3). |
| s 54(z.3) | src:1037 | inert | - | Power to make regulations on: reducing special benefits when allowances, money or other benefits are payable under a plan other than a provincial plan; not matched to a regulation by this piece. |
| s 54(z.31) | src:1038 | inert | - | Power to make regulations on: eliminating special benefits for a period that is an elimination period under such a plan; not matched to a regulation by this piece. |
| s 54(z.4) | src:1039 | inert | - | Power to make regulations on: prescribing anything that s 2 or Part I says is to be prescribed (every regulation made under Part I answers to it). |
| s 55(1) Hours of insurable employment | src:1040-1041 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations establishing how many hours of insurable employment a person has, including deeming hours for persons not paid by the hour. Regulation-making machinery: regs 9.1 to 11 (piece er1) are made under it. |
| s 55(2) Alternative methods | src:1042-1043 | encoded | `ei2-hours-methods` `s 55(2) the Commission may authorize an alternative method of establishing how many hours of insurable employment a person has` | The Commission's consideration is an input. Seat. |
| s 55(3) Alteration or rescission of authorization | src:1044-1045 | encoded | `ei2-hours-methods` `s 55(3) the Commission may alter the authorized method or rescind the authorization` |  |
| s 55(4) Agreement to provide alternative methods | src:1046-1047 | encoded | `ei2-hours-methods` `s 55(4) the Commission may enter into the agreement`, `s 55(4) the Commission may rescind the agreement` | Seat. |
| Heading "PART II Employment Support Measures and National Employment Service" | src:1049 | inert | - | A Part heading: it carries no text of its own (the keel's `Part of the Act` has the constructor `Part II`). |
| s 56 Purpose | src:1050-1051 | encoded | `ei2-employment-support` `s 56 the purpose of Part II` | A purpose clause: carried as a named STRING that nothing reads, as the phrasebook says (9.3); it is not a reason on the brief's list of inert reasons, so it is not marked inert. |
| s 57(1) Guidelines | src:1052-1063 | encoded | `ei2-employment-support` `s 57(1) the measures are established in accordance with the guidelines`, `s 57(1)(d.1) assistance is available in either official language where there is significant demand`, `s 57(1)(e) the commitment expected of persons receiving assistance is made` | Paragraphs (a) to (f); (d.1) and (e)(iii) bite only on the condition they state. The Commission's side of the guidelines; the participant's side is paragraph (e), asked in the seat. |
| s 57(2) Working in concert and consultations | src:1064-1065 | encoded | `ei2-employment-support` `s 57(2) the Commission has worked in concert and consulted as the Act requires` |  |
| s 57(3) | src:1066 | repealed or blank in this text | - | The text shows `(3) [Repealed, 2022, c. 10, s. 397]`. |
| s 58 Definition of insured participant | src:1067-1070 | fork | `ei2-employment-support` `s 58 the person is an insured participant` | Fork ei2-F12 (reg 76.11, piece er4, adapts the definition). Seat. |
| s 59 Employment support measures | src:1071-1076 | encoded | `ei2-employment-support` `s 59 the Commission may establish the employment support measure`; the four kinds are `ei2-nouns` `ei2 Kind of employment support measure` | The list (a) to (d) is open ("including"), so a fifth constructor stands for any other measure. Seat. |
| s 60(1) National employment service | src:1077-1078 | encoded | `ei2-employment-support` `s 60(1) the Commission has maintained the national employment service as the Act requires` |  |
| s 60(2)(a) Duties of the Commission: information | src:1079-1081 | encoded | `ei2-employment-support` `s 60(2)(a) the Commission has collected and made available the information as the Act requires` |  |
| s 60(2)(b) Duties of the Commission: no discrimination in referral | src:1082-1084 | encoded | `ei2-employment-support` `s 60(2)(b) the referral is as the Act requires` | (i) and (ii) are exceptions to the paragraph. Seat. |
| s 60(3) Regulations | src:1085-1086 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations for the purposes of subsections (1) and (2); regulation-making machinery. Reg 58 and reg 59 (piece er4) are the Regulations' Part II. |
| s 60(4) | src:1087 | repealed or blank in this text | - | The text shows `(4) [Repealed, 2022, c. 10, s. 400]`. |
| s 60(5) | src:1088 | repealed or blank in this text | - | The text shows `(5) [Repealed, 2022, c. 10, s. 400]`. |
| s 61 Financial assistance | src:1089-1090 | encoded | `ei2-employment-support` `s 61 the Commission may provide the financial assistance` |  |
| s 62 Agreements for administering employment support measures | src:1091-1092 | encoded | `ei2-employment-support` `s 62 the Commission may enter into the agreement or arrangement` | An agreement-making power, not one of the three kinds of machinery on the brief's list, so it is encoded. |
| s 63(1) Agreements for paying costs of similar benefits and measures | src:1093-1096 | encoded | `ei2-employment-support` `s 63(1) the Commission may enter into the agreement to pay contributions` | As s 62. |
| s 63(2) | src:1097 | repealed or blank in this text | - | The text shows `(2) [Repealed, 2017, c. 20, s. 308]`. |
| s 63.1 | src:1098 | repealed or blank in this text | - | The text shows `63.1 [Repealed, 2017, c. 20, s. 309]`. |
| s 64 No appeal | src:1099-1100 | encoded | `ei2-employment-support` `s 64 the decision is not subject to review under section 112` | MAYBE BOOLEAN: a decision under s 65.1 is outside the rule. Seat. |
| s 65 Liability for repayments | src:1101-1105 | encoded | `ei2-employment-support` `s 65 the amount the person is liable to repay` | Seat. |
| s 65.1(1) Penalties | src:1106-1111 | encoded | `ei2-employment-support` `s 65.1(1) the Commission may impose a penalty on the person` | The Commission's opinion is an input. Seat. |
| s 65.1(2) Maximum penalty | src:1112-1113 | encoded | `ei2-employment-support` `s 65.1(2) the most the Commission may set as the amount of the penalty` | Seat. |
| s 65.1(3) Limitation on imposition of penalties | src:1114-1117 | fork | `ei2-employment-support` `s 65.1(3) the penalty shall not be imposed` | 36 months: a figure of the text; fork ei2-F10. Seat. |
| s 65.1(4) Rescission, etc., of penalty | src:1118-1119 | encoded | `ei2-employment-support` `s 65.1(4) the Commission may rescind the imposition of the penalty, or reduce it` | Seat. |
| s 65.2(1) Debts due to the Crown | src:1120-1121 | encoded | `ei2-employment-support` `s 65.2(1) the amount is a debt due to Her Majesty` | MAYBE BOOLEAN. Seat. |
| s 65.2(2) Recovery by deduction | src:1122-1123 | encoded | `ei2-employment-support` `s 65.2(2) the indebtedness may be recovered out of the amount payable` | Seat. |
| s 65.2(3) Limitation | src:1124-1125 | encoded | `ei2-employment-support` `s 65.2(3) the amount may still be recovered` | 72 months: a figure of the text; no tolling during an appeal (finding 8). Seat. |

## Fork register

Every entry is assumed, not ruled: the reading is mine, chosen so that work could go on, and each can be reversed in one place (the rule named).
The ids are `ei2-F1` to `ei2-F16` so that they cannot collide with the keel's `F1` to `F7`, whose fork F4 (a limit of n days or months after a day ends on, and counts, the last day) this piece relies on and extends.
"No ambiguities found" would not be believable, so here is where I looked: every "subject to", "despite", "notwithstanding" and "except as" (ss 24(2), 25(2), 28(2), 30(4), 30(7), 35, 36(1), 37, 39(4), 39(5), 41.1(2), 42(1), 52(1)); every list of alternatives or conditions joined by "and", "or" or both (ss 25(1), 27(1), 29(c), 30(1), 38(2), 39(1), 46.1(2), 58); every time limit (28(3), 33(1), 40, 41.1(2), 46.01, 46.1(2), (4), 47(3), 52(1), (5), 58, 65.1(3), 65.2(3)); and every place the text defers to a regulation, a judgment or a provision outside the range.

| id | provision | what the text leaves open | the readings I saw | the reading I took, and the text that licenses it | what would settle it |
| --- | --- | --- | --- | --- | --- |
| ei2-F1 | s 23.3(6) (src:671) | "If they cannot agree": whether it means they have not agreed, or that they are unable to. | (a) not agreed; (b) unable, which would need a finding about the claimants' inability. | (a): the section has two cases, "the manner agreed to by those claimants" and "if they cannot agree", and reg 41.6 (piece er3) uses the same words ("if the claimants cannot agree"). `s 23.3(6) the way the remaining weeks are divided` takes one BOOLEAN, "have agreed". | A ruling, or the Regulations' meaning of "cannot agree". |
| ei2-F2 | s 28(2) with s 28(5) (src:730-731, 736-737) | Whether a week on which serving is deferred counts in the run of weeks "following the waiting period for which benefits would otherwise be payable". | (a) it counts, so the disqualification runs out during weeks of special benefits, which makes the deferral of (5) empty; (b) it does not count. | (b): s 28(5) says the Commission "shall defer the serving"; reading (a) would serve it. `s 28(2) the week is served as a week of disqualification` takes the deferral and counts the place of the week only among weeks not deferred. | The Commission's practice; not in the text. |
| ei2-F3 | s 28(3) (src:732-733) | When a benefit period is "established": on its first day, the day of the claim, or the day the Commission decides. | Those three. | The first day: `s 10(1)` (piece ei1) starts a benefit period on a Sunday, and "within two years after the event" is then a comparison of dates. `s 28(3) a benefit period is established within two years after the event` takes the first day. | Piece ei1's s 10. |
| ei2-F4 | s 29(c) (src:750-764) | Whether the fourteen items are sufficient conditions of just cause or circumstances to be weighed. | (a) each item is enough, so just cause exists if any is present; (b) they are among "all the circumstances" to which regard is had in deciding whether the claimant "had no reasonable alternative". | (b): "just cause ... exists if the claimant had no reasonable alternative to leaving or taking leave, having regard to all the circumstances, including any of the following". `s 29(c) just cause for voluntarily leaving ... exists` takes the judgment; `s 29(c) one of the circumstances listed in the Act is present` is separate, and a TRUE there does not by itself prove just cause (tested). | A ruling or a court's reading. |
| ei2-F5 | s 35 against ss 30 to 33 (src:805-808) | How far "Notwithstanding anything in this Part ... only because the claimant left or refused to accept employment" reaches. | (a) all of ss 30 to 33; (b) only the leaving and refusing limbs; (c) nothing, because no limb of ss 30 to 33 refers to a refusal. | (b): the section protects a claimant who is disqualified or disentitled "only because the claimant left or refused to accept employment". In s 30(1) that is the "voluntarily left ... without just cause" limb, not the misconduct limb; s 33(1) is the same; s 31 is a suspension and s 32 is a period of leave, neither a leaving nor a refusal in those words. `s 30(1)` and `s 33(1)` take a BOOLEAN "section 35 protects the claimant ..." that switches the leaving limb off. | The Act's own history or a ruling. |
| ei2-F6 | s 33(1) (src:797-800) | "within three weeks before": which days are inside. | Three weeks are 21 days; the loss or leaving falls (a) on or after the 21st day before the end day and on or before the end day; (b) on the 21st day before up to the day before the end day. | (a): the keel's F4 (the last day counts), and a leaving on the last day of a term is still before the term's expiry at its end. `s 33(1) the claimant is not entitled to receive benefits`, local helper `the claimant lost or left within three weeks before`. | The Interpretation Act, not deposited. |
| ei2-F7 | s 33(2) (src:801-802) | Whether the disentitlement is in force on the day the term expires or the lay-off day. | In force on that day, or ended the day before. | In force on that day: "lasts until the expiration of the term of employment or the day on which the claimant was to be laid off", and the keel's F4 (the last day counts). `s 33(2) the disentitlement is still in force on the day`. | As ei2-F6. |
| ei2-F8 | s 38(2) (src:839-845) | How the limbs combine: (a), (b) and (c) are joined by "or"; (b)(i) and (ii) by "and". | (1) alternatives: the Commission may use the largest that applies; (2) cumulative caps: the smallest that applies; (3) the sum of (b)(i) and (ii); and within (b), "and" as "both must hold" or as addition. | The largest limb that applies, with (b)(i) and (ii) both binding (the lesser of the two): the "or" before (c) makes (a), (b) and (c) alternatives, and "and" between (i) and (ii) makes both ceilings of (b) apply. With no benefit period only (c) applies, because it says so; (a) and (b) need a benefit period. `s 38(2) the most the Commission may set as the amount of the penalty`; the four ceilings are separate rules. Whatever the reading, no penalty can exceed this figure unless reading (3) is right. | A ruling, or the Commission's guidance. |
| ei2-F9 | s 39(2), (4), (5) (src:855-864) | What happens when (4) and (5) both apply, each "notwithstanding subsection (2)". | The greater, the lesser, (5) always, (4) always. | The greater of the two that apply, as the largest sum the Act allows. `s 39 the most the Commission may set as the amount of the penalty`. The amount for (5) comes from the Regulations under s 54(g.1); the Regulations file has no "major contravention", so it is an input. | The regulations under s 54(g.1). |
| ei2-F10 | ss 40, 41.1(2), 46.01, 46.1(4), 47(3), 52(1) and (5), 58, 65.1(3), 65.2(3) | Whether the day n months after a day is inside or outside a limit, and how "n months have passed since" differs from "within n months after". | For "have passed since" and "more than n months have elapsed": (a) true from the anniversary day; (b) true from the day after it. For "within n months after": through the anniversary day, or up to the day before. | One rule: the n-month anniversary (`add months`, which clamps a short month to its last day) is the last day inside; "n months have passed" and "more than n months have elapsed" are true from the day after it. This is the keel's F4 applied to months, and it makes "have passed" and "within" complementary. | The Interpretation Act, not deposited. |
| ei2-F11 | s 47(3) and (4) (src:920-923) | How a limitation period "does not run" while an appeal or review is pending. | The days pending are left out of the count (the last day moves later by their number); or the whole period restarts. | The days pending within the 72 months extend the last day by their number. `s 47(3) the amount may still be recovered` takes the number of days. s 65.2(3) has no such rule (finding 8). | A ruling. |
| ei2-F12 | s 58 with reg 76.11 (src:1067-1070; Regs line 1227) | Whether the adaptation of the definition by reg 76.11 (piece er4) is part of "insured participant" in s 58. | In or out. | In, as a separate BOOLEAN input: reg 76.11 says "The definition insured participant in section 58 of the Act is adapted to include" a class. `s 58 the person is an insured participant` takes `the person is within the definition as adapted by regulation 76.11`. | Piece er4's reg 76.11, and a lead's merge. |
| ei2-F13 | ss 31, 32(2), 36(1), 48 to 50 | The date at which each "until" and each condition is tested. | A fact as at the day in question; or a date for each event with the day itself in or out. | As at the day in question: each event ("the period of suspension expires", "the work stoppage has ended", "the claimant has resumed") is a BOOLEAN that has or has not happened by that day, so the question of whether the end day counts is the caller's. Only s 33(2) takes dates (ei2-F7). | The Interpretation Act and the Commission's practice. |
| ei2-F14 | s 30(5) (src:775-778) | Whether "an employment as described in subsection (1)" is the loss or leaving that (1) names, or one that is also not saved by (1)(a) or (b). | The first or the second. | The loss or leaving is what is "described"; the "unless" limbs are not part of the description. `s 30(5)` takes the BOOLEAN `the claimant has lost or left an employment as described in subsection 30(1)`; the caller states it. | A ruling. |
| ei2-F15 | ss 25(1)(b)(i) and 26 (src:701, 706) | Whether "other than one referred to in paragraph 59(a) or (c)" (and "59(c) or (d)") qualifies only the employment support measure, or also the measure that is the subject of a section 63 agreement. | Only the measure; or both. | Only the employment support measure: the dash-set phrase follows "employment support measure" and the section 63 measure is joined by "or". `ei2 s 59 there is a measure and it is of neither of the two kinds` is applied to the measure only. | A ruling. |
| ei2-F16 | ss 48(1), 48(2), 49(1) (src:926-929, 932-935) | Whether "No benefit period shall be established unless ..." and "A person is not entitled ... until ..." are sufficient as well as necessary. | Necessary only; or necessary and sufficient. | Necessary only: the sections say when something cannot happen. Whether a benefit period is established, or a week paid, is ss 9, 10 and 18 (piece ei1). The rules say whether the condition is met. | Not in the text. |

**Judgments the Act hands to someone else, taken as BOOLEAN inputs** (not forks, listed so that they are not mistaken for computed answers): good cause (s 27(1)); suitable employment (ss 27, 29); reasonable direction (s 27(1)(c)); the Commission's opinion that completion is unlikely (s 27(1.1)(b)(i)); no reasonable alternative (s 29(c)); misconduct (ss 30, 31, 33); the Commission's opinion that facts establish an act (ss 38(1), 39(1), (3), 65.1(1)); satisfaction as to a material fact (ss 41, 65.1(4)); the Commission's opinion on cost (s 46.01); due diligence (s 46.1(3)); what the Commission considers adequate (s 53), impossible to apply (s 55(2)) or warranting waiver (s 50(10)); and, in Part II, whether a measure is meant to help workers (s 59) and the guidelines (s 57).

## Cross-references out of my ranges

Every one is a plain input with a comment `-- out of range: ...` in the module.
The "piece" is read from the brief's table.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 23.3(6) | s 152.062 (a claim by a self-employed person for the same adult) | ei5 | BOOLEAN `another claimant makes a claim under section 23.3 or 152.062 in respect of the same adult` |
| s 23.3(6) | reg 41.6 (the prescribed rules for dividing weeks) | er3 | none: `ei2 divided in accordance with the prescribed rules` is a value; the rules are not worked out |
| s 23.3(8) | s 23.3(3) (the period); s 152.062(3); ss 23.1 and 152.06 (compassionate care) | ei1; ei5 | `Period of days` `the period referred to in subsection 23.3(3) or 152.062(3) established in respect of the adult`; the keel's `Reason for benefits` constructor `care or support of a family member` |
| s 23.3(9) | the regulations that reduce benefits (none among the inputs prescribes it for s 23.3; regs 76.16 and 76.17 speak of ss 22 and 23 only) | er4 | the rule says only that the reduction or elimination applies; no amount |
| s 24(2), s 25(2), s 64 | s 112 (review of a decision) | ei4 | each rule says the decision is not subject to review under s 112; s 112 is not encoded here |
| s 24(3) | regs 42 to 49 (what work-sharing employment is) | er3 | BOOLEAN `the claimant works in work-sharing employment during the week` |
| s 25(1)(b) | reg 50 (the prescribed measures) | er3 | BOOLEAN `that measure is prescribed` |
| s 27(1)(a), (b), (c) | s 54(k.1) and reg 9.002 (suitable employment) | er1 | the words "suitable employment" are in the names of BOOLEAN inputs |
| s 28(3) | s 10 (benefit period) | ei1 | DATE `the first day of a benefit period subsequently established` |
| s 28(7) | s 10(6) (cancelling a minor attachment benefit period), s 6(1) (minor and major attachment claimant) | ei1 | BOOLEANs `a benefit period was established for the claimant as a minor attachment claimant`, `the request is that it be cancelled under subsection 10(6) ...` |
| s 29(a) | ss 8, 9, 10 (qualifying and benefit period) | ei1 | BOOLEANs `the employment is within the claimant's qualifying period`, `... benefit period` |
| s 29(c)(xiv) | reg 51.1 (other reasonable circumstances) | er3 | BOOLEAN `any other reasonable circumstances that are prescribed` |
| s 30(1), s 31, s 32(2) | ss 7 and 7.1 (hours required to qualify) | ei1 | NUMBER `the number of hours required by section 7 or 7.1 to qualify to receive benefits` |
| s 30(2) | s 10 (benefit period), s 13 (waiting period) | ei1 | `Period of days` `the claimant's benefit period`, `the waiting period` |
| s 30(5), (6) | ss 7, 7.1, 12(2), 14 (hours, maximum weeks, rate) | ei1 | NUMBERs of hours |
| s 36(1) | reg 53 (end of a work stoppage); reg 52 (part-time days); s 2(1) "labour dispute" | er3; keel | BOOLEAN `the work stoppage has ended`; the seat calls the keel's `s 2(1) labour dispute` |
| s 37 | regs 54 and 55 (excepted inmates and absences) | er3 | BOOLEAN `an exception is prescribed that covers the claimant's case` |
| s 38(2) | s 14 (rate of weekly benefits and the maximum rate); s 19(3) (the deduction) | ei1 | NUMBERs `the claimant's rate of weekly benefits`, `the maximum rate of weekly benefits ...`, `the amount of the deduction ...` |
| s 38(3) | s 145(2) (benefit repayment) | ei4 | none: the rule deems weeks paid for that subsection |
| s 39(5) | s 54(g.1) and the regulations on major contraventions (the words do not occur in the Regulations file) | none found | NUMBER `the amount required or authorized by the regulations for the major contravention` |
| s 42(3) | reg 57 (the regulations it is subject to) | er3 | none; the conditions in the text are encoded |
| s 45 | regs 35 to 39 (earnings, and the benefits that would not have been paid) | er3 | NUMBER `the benefits that would not have been paid if the earnings had been paid or payable at the time the benefits were paid` |
| s 46.1(2)(a) | s 126 (certificate of the amount, registered in the Federal Court) | ei4 | BOOLEAN `a certificate ... has been registered in the Federal Court under section 126` |
| s 47(3) | s 52(3)(b) (the day liability arises) | this piece | DATE inputs; the seat composes with `s 52(3)(b) ...` |
| s 50(4) | reg 26 (the prescribed time) | er2 | DATE `the last day on which a claim for that week can be made within the prescribed time` |
| s 50(8) | s 54(k.2) and reg 9.001 (reasonable and customary efforts) | er1 | BOOLEANs of the requirement and the proof |
| s 50(8.1) | ss 23.1(2) and 152.06(1) (the certificate) | ei1; ei5 | BOOLEANs of the requirement |
| s 52(1) | s 111 (reconsideration in general) | ei4 | the rule gives 36 or 72 months; s 111 is not encoded here |
| s 55(2) to (4) | reg 9.1 to 11 (how hours are counted) | er1 | BOOLEAN `the Commission considers that it is not possible to apply the provisions of the regulations` |
| s 58 | s 96(4) (a refund of employee's premiums); Part VIII.4 (the emergency response benefit); reg 76.11 | ei3; ei6; er4 | NUMBER `the number of the last 10 years in which the person paid employee's premiums that did not entitle them to a refund under subsection 96(4)`; MAYBE DATE `the last day on which the person was in receipt of the employment insurance emergency response benefit, if ever`; BOOLEAN for reg 76.11 |
| s 65.1, s 65.2 | none outside the range | - | - |

31 rows.

## Needs from the core

Nothing blocks this piece; each item is a suggestion for the lead to decide after the merge.

1. **The kind of employment support measure** (`ei2 Kind of employment support measure` in `ei2-nouns`, with the helpers `ei2 s 59 the measure is of the kind`, `ei2 s 59 there is a measure and it is of neither of the two kinds` and `ei2 s 59 there is a measure and it is not of the kind` in `ei2-work-sharing-and-courses`).
   Reason: ss 5(1)(e), 25(1), 26 and 27(1.1) all key on "other than one referred to in paragraph 59(a) or (c)" or "59(c) or (d)".
   The keel's `s 5(1)(e)` takes a BOOLEAN for that fact; promoting the type would let the keel and this piece agree on one noun.
2. **A shared reading of a time limit in months** (ei2-F10): "within n months after d" ends on the n-month anniversary (`add months`), and "n months have passed since d" or "more than n months have elapsed" is true from the day after it.
   Nine sections of this piece use it (ss 40, 41.1(2), 46.01, 46.1(4), 47(3), 52(1) and (5), 58, 65.1(3), 65.2(3)), and later pieces will (for example the 36-month and 72-month limits elsewhere).
   A helper beside the keel's `the last day of n days after d` would stop each piece writing `add months` itself.
3. **A shared "tri-state to yes/no" conversion for deeming rules.** This piece's seat has the helper `ei2 seat: a JUST TRUE answer means the provision applies`; other seats that wrap a MAYBE BOOLEAN deeming rule will want the same.

Everything this piece defines carries the prefix `ei2` or begins `s N`, so nothing here collides with another piece's names.
`YMD`, `Period of days`, `Reason for benefits`, `weeks as days`, `s 2(1) the Sunday that begins the week containing`, `the day ... falls within ...`, `s 2(1) special benefits`, `s 2(1) insured person` and `s 2(1) labour dispute` come from the core, unchanged.

## What the text turns out to say

Each finding ends "Asserted." where a case in `ei2-cases-seat.l4` or a test asserts it.

1. **A deeming section does not say the opposite outside its case.** Sections 24(3), 25(1), 26, 28(6), 28(7), 35, 36(5), 42(1), 47(1), 49(2), 52(3)(a) and 65.2(1) say that in a stated case a claimant is treated in a stated way. None says that outside the case the claimant is not; other provisions decide that. The rules answer `JUST TRUE` or `NOTHING` and never `FALSE`. Asserted (every one of those rules has a `NOTHING` test; for example `s 24(3) ... FALSE EQUALS NOTHING`).
2. **Section 64 closes the door and then leaves one door unmarked.** A decision "made in relation to employment support measures" is not reviewable under s 112, "other than a decision under section 65.1". The section does not say a s 65.1 decision is reviewable, only that s 64 does not close it: the answer is `NOTHING`, and s 112 (piece ei4) decides. Asserted (`s 64 ... TRUE TRUE EQUALS NOTHING`; seat Q93).
3. **Section 30(4) opens "Despite subsection (6)", but (6) is about hours.** Subsection (6) says no hours in a lost or left employment may be used for the maximum number of weeks or the rate; subsection (4) is about suspending the disqualification in a week of special benefits. There is nothing in (6) for (4) to override on its face, so the rule encodes (4) on its own words. Not asserted: the point is about the wording.
4. **Section 38(2) has four ceilings and no word saying how they combine.** (a) three times the weekly rate; (b)(i) three times the s 19(3) deduction "and" (ii) three times the benefits that would have been paid; "or" (c) three times the maximum rate if no benefit period was established. See ei2-F8. Asserted (the `s 38(2)` tests and seat Q43 cases, each on figures written down beforehand).
5. **A penalty is barred on the day after the 36th month and a warning on the day after the 72nd.** Section 40(b) says "36 months have passed", s 41.1(2) says a warning "may be issued within 72 months after"; with ei2-F10 they are complementary, and between 36 and 72 months a warning may still be issued although a penalty may not. Asserted (`s 40` and `s 41.1(2)` tests, both ends; seat Q45 and Q48).
6. **The benefit of the doubt in s 49(2) is for ss 30 to 33 only.** It does not reach s 27 (disqualification for not looking for work), s 36 (a labour dispute) or s 37. Asserted (`s 49(2) ... TRUE TRUE`, `FALSE TRUE EQUALS NOTHING`; seat Q64).
7. **Sections 56 and 57 are not machinery.** The brief's list of reasons for `inert` does not include a purpose clause or a guideline, so s 56 is carried as a named STRING nothing reads, and s 57(1) and (2) are encoded as predicates over BOOLEAN facts; (1)(e) is the participant's own side and is asked in the seat. Asserted (`s 57` tests; seat Q86 and Q87).
8. **Section 65.2(3) has no tolling rule.** Section 47(3) and (4) stop the 72-month limit running while an appeal or review is pending; s 65.2(3) has the same 72 months and no such rule. `s 65.2(3) the amount may still be recovered` takes no pending days. Not asserted: the point is an absence.
9. **Section 28(7) is narrow.** It saves only the request, under s 10(6), that a minor attachment benefit period be cancelled and a major attachment one established, and only to enable the claimant to receive special benefits. Asserted (seat Q21).
10. **Section 35 reaches the leaving limbs of ss 30 and 33 and nothing else** (ei2-F5). A claimant dismissed for misconduct whose employment also cost union rights is still disqualified. Asserted (seat Q28 and Q35; `s 30(1)` and `s 33(1)` tests).
11. **Section 30(1)(a) is a count of hours since leaving.** 600 hours since, where 600 are required, saves the claimant; 599 does not. Asserted (`s 30(1)` tests; seat Q28).
12. **Section 33(1) is 21 days.** Lost or left 21 days before the end of a set term, or the end day, is within three weeks; 22 days before is not (ei2-F6). Asserted (`s 33(1)` tests; seat Q35).
13. **Section 36(4) wants three negatives proved.** The claimant must prove they are not participating in, not financing and not directly interested in the dispute; two of three is not enough. Asserted (`s 36(4)` tests; seat Q39).
14. **Section 46.01 needs both conditions.** More than 36 months since the lay-off or separation, and the Commission's opinion that the cost of determining the repayment would equal or exceed it. Asserted (`s 46.01` tests; seat Q57).
15. **Section 39(4)'s ceiling is never below $12,000.** It is the greater of $12,000 and the s 38 penalty and applies "notwithstanding subsection (2)", so even where (2)'s nine times the maximum rate is smaller (here $5,850 on a $650 maximum rate) the ceiling is $12,000. Asserted (`s 39 the most ...` tests).
16. **Section 42(3) needs consent on or before receiving the payment.** Asserted (seat Q51).
17. **The Regulations text has no "major contravention".** Section 39(5) points to regulations under s 54(g.1) (a maximum of $25,000); the words do not occur in the Regulations file, so the amount for a major contravention cannot be computed and is an input. Not asserted: the point is an absence.
18. **Regulation 76.11 adds a class to s 58.** A person with a benefit period under a provincial plan, or who had one end within the previous 60 months, and who would have been entitled to special benefits under s 22 or 23 but for provincial benefits, is an insured participant (ei2-F12). Asserted (`s 58` tests; seat Q88).
19. **Section 52(4) gives the claimant a claim.** If the Commission decides the claimant was qualified and entitled and the money was not paid, the amount calculated is payable to the claimant. Asserted (seat Q82).
20. **Section 47(1) does not list s 44.** The debts due to Her Majesty are the amounts payable under ss 38, 39, 43, 45, 46 or 46.1; the duty to return a payment in s 44 is not in the list (the repayable overpayment is s 43's). Not asserted: the seat takes the list as one BOOLEAN.
21. **Section 40(a) speaks of "the employee, employer or other person".** Section 38 penalises a claimant or a person acting for one, and s 39 an employer; "employee" in s 40(a) can only be the claimant penalised under s 38. `s 40 a penalty shall not be imposed` takes the input as the text words it, `a prosecution for the act or omission has been initiated against the employee, employer or other person`, and the seat asks it of the person penalised. Not asserted: the point is about the wording.

## What the stable binary does not accept

Binary: `l4 1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.

**Rejected, measured in this piece** (each was a file that failed in this session and was rewritten):

- `x NOT EQUALS y` does not parse: `unexpected NOT`. Write `NOT (x EQUALS y)`.
- A type ascription does not parse: `(NOTHING : MAYBE T)` gives `unexpected :`. Write a typed fixture rule: `GIVETH A MAYBE T` over `name MEANS NOTHING`.
- `add months` and `add years` must be backtick names: `` `add months` d n ``. Unquoted, `add` and `months` are two unknown identifiers.

**Accepted, measured in this piece** (listed so that nobody avoids them):

- A string constant at the top level needs no `GIVETH`: `` `s 56 the purpose of Part II` MEANS "..." `` checks (phrasebook 9.3).
- `IF ... THEN ... ELSE` as an argument works when the argument is bracketed, as in the seat's calls.
- `CONSIDER` on a `MAYBE` with `WHEN NOTHING` and `WHEN JUST x`, and `BRANCH IF ... THEN ... OTHERWISE` with a nested `IF` in an arm.
- A `WHERE` with a local mixfix function of two parameters (`s 33(1)`, `s 46.1(2)`, `s 58`).

**By design, not measured here** (from `dialects.md` and the brief): `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used (a case outside an encoding returns `NOTHING` or a constructor); no section `GIVEN` (every rule has its own); no `TYPICALLY`; no set; no `EVERY`; no regulative rule (see below); no `RULES EFFECTIVE DATE`; every `NOT` is bracketed, because `main` reads `NOT a AND b` as `NOT (a AND b)`; every `#ASSERT` is on one line.

**No DEONTIC rule is written.** `check.sh` counts assertions and a `DEONTIC` value cannot be asserted, only traced, so a duty encoded as a `MUST` would be invisible to the gate. Duties are encoded as BOOLEAN decision rules or as the consequence the Act itself states (for example s 50(1) for the conditions of s 50, and "has done what it must" for the Commission's duties).

**Exports.**
101 questions: 100 return BOOLEAN, NUMBER or DATE; one ("the fewest weeks of disqualification the Act allows for my ground") returns a `MAYBE NUMBER`, and the Interact form's treatment of a MAYBE result was not measured (the companion BOOLEAN question tells the form whether the NUMBER exists).
Inputs are BOOLEAN, NUMBER, DATE and enums (the kind of employment support measure, the ground of disqualification, and the keel's `Reason for benefits`).
Two exports were run through `l4 batch` with a JSON row (an enum given as its constructor's name, a date as an ISO 8601 string): both returned `status: success` and the expected result.

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so).
It covers the 12 `ei2-*` nouns, rule and seat modules, the 10 test files, the cases file, and the keel's 4 modules that sit in this folder (the keel's own test files are not in this folder).
The run takes a few minutes: the cases file calls the seat 296 times.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ei2-cases-seat.l4                              0       296       0        0         0
ei2-claim-procedure.l4                         0         0       0        0         0
ei2-disqualification.l4                        0         0       0        0         0
ei2-employment-support.l4                      0         0       0        0         0
ei2-hours-methods.l4                           0         0       0        0         0
ei2-labour-disputes-and-absence.l4             0         0       0        0         0
ei2-leaving-and-misconduct.l4                  0         0       0        0         0
ei2-nouns.l4                                   0         0       0        0         0
ei2-penalties.l4                               0         0       0        0         0
ei2-repayment.l4                               0         0       0        0         0
ei2-s23-3-division.l4                          0         0       0        0         0
ei2-seat.l4                                    0         0       0        0         0
ei2-tests-claim-procedure.l4                   0        86       0        0         0
ei2-tests-disqualification.l4                  0        81       0        0         0
ei2-tests-employment-support.l4                0        85       0        0         0
ei2-tests-hours-methods.l4                     0         9       0        0         0
ei2-tests-labour-disputes-and-absence.l4       0        29       0        0         0
ei2-tests-leaving-and-misconduct.l4            0       103       0        0         0
ei2-tests-penalties.l4                         0        58       0        0         0
ei2-tests-repayment.l4                         0        72       0        0         0
ei2-tests-s23-3-division.l4                    0        23       0        0         0
ei2-tests-work-sharing-and-courses.l4          0        40       0        0         0
ei2-work-sharing-and-courses.l4                0         0       0        0         0
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
TOTAL (27 modules)                             0       882       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <the Act's raw file> ei2-*.l4` prints:

```
srcrefs check: 475 src: lines, 149 runs, 157 locators, 0 problems
```

My own files: 882 assertions satisfied, 0 failed, 0 refused, 0 errors; every test and case file has assertions written equal to assertions satisfied (the counts are in the table: 586 in the ten test files and 296 in the cases file).
No assertion is meant to fail, so `expected_failed` is empty.
`l4 check` on each file prints no `Unknown annotation`, `follows code on its line` or `is at the end of the file` warning.

## Before this is worth relying on

- **A person who knows the law has to read it against the text.** No domain expert has read any of this. The tests were written by the same agent that wrote the rules: the brief gave no independent test author and no subagents. Every expected value was decided from the text before running, and nothing failed, which is also what a misreading shared by rules and tests would look like.
- **The sixteen forks above** should be ruled, especially ei2-F8 and ei2-F9 (the penalty ceilings), ei2-F5 (how far s 35 reaches), ei2-F10 (the day a month limit ends) and ei2-F4 (just cause).
- **The inputs from other pieces and from the Regulations** are not computed here: the hours required by s 7 or 7.1, the rate of weekly benefits, the benefit, qualifying and waiting periods, the last day to claim (reg 26), the prescribed measures (reg 50), the prescribed circumstances (reg 51.1), the work stoppage's end (reg 53), the excepted inmates and absences (regs 54, 55), the benefits that would not have been paid (regs 35 to 39). Once the other pieces land, the seat questions that take them as plain numbers or yes/no could call their rules.
- **The Interpretation Act is not deposited,** so ei2-F10 and the keel's F4 are assumptions about how days and months are counted.
- **The seat has not been tried on the website.** It has 101 questions, some with fifteen inputs; the form's behaviour with them, with enum inputs and with the grouping `§§` headings, was not measured. The employer's and directors' provisions (ss 39, 46(2), 46.1) have no seat; an employer seat `ei2-seat-employer.l4` would ask them.
- **The merge.** The lead should check that no `s N(M) ...` rule here shares a name with another piece's (ours begin with the section number of this range's sections, which the brief assigns to ei2 alone), and that the `ei2-` file names do not collide. The seat's question names (`Can the Commission impose a penalty on me`, `Am I liable to repay an amount paid to me as benefits`, ...) are plain English, so another piece's seat could mint the same one; each seat is its own file, but a deployment of two seats would need distinct names.
- **Nothing was deployed, committed or pushed.**

