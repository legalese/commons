# Canada Disability Benefit Act and Regulations -- an L4 encoding (legalese-sonnet-5.5)

Status: draft.
No domain expert has read this encoding against the text, and the same agent wrote the rules and the expected values of the tests (there was no independent test author).
The method is a single Sonnet 5.5 agent working alone from `BRIEF.md`.
Written 2026-10-22 against the stable build l4 1.6.98 (dialect `main`), run as `L4_TARGET=unstable ./check.sh`.

## The texts, and which instrument each rule comes from

The two source files are plain-text renderings, made by a converter script from the Justice Laws XML (repository commit `0507465393c224c0491fc8c17c88340217acc656`, "Laws Site Update 2026-10-15", current to 2026-09-30).
They are not the official text, they are not marked up, and nothing in this encoding has been verified against the official text.
Only the English version is deposited; the French version has equal authority and was not read.
Historical notes and the Recent Amendments list are omitted from the renderings; Parts, headings, marginal notes, formulas and the one related provision (SOR/2026-123 s 14) are kept.
The terms the text carries are in `SOURCE-LICENSE.md`.

- `S.C.-2023-c.-17.txt` is the Canada Disability Benefit Act (S.C. 2023, c. 17), last amended 2024-06-22.
  Rules from the Act are in `cdba-act.l4`: ss 4, 5, 6, 7, 8, 9, 10.1 and 14.
- `SOR-2025-35.txt` is the Canada Disability Benefit Regulations (SOR/2025-35), last amended 2026-09-01.
  Every other layer-1 module encodes the Regulations; the figures, dates and conditions the Act leaves to regulations are taken from them.

| file | what it holds | instrument |
|---|---|---|
| `cdba-nouns.l4` | shared records and choices (types only) | both |
| `cdba-calendar.l4` | the `YMD` shim and month helpers | none (stable-binary shim) |
| `cdba-reg-definitions.l4` | s 1: applicant, beneficiary, payment period, release | Regulations |
| `cdba-reg-eligibility.l4` | ss 2, 2.1 (and the related provision SOR/2026-123 s 14); s 3 is inert | Regulations |
| `cdba-reg-application.l4` | ss 4, 5 | Regulations |
| `cdba-reg-amount.l4` | ss 6, 6.1 | Regulations |
| `cdba-reg-payment.l4` | ss 7, 8, 9, 9.1 | Regulations |
| `cdba-reg-suspension.l4` | ss 10, 11 | Regulations |
| `cdba-reg-death.l4` | ss 12 to 16 | Regulations |
| `cdba-reg-reviews.l4` | ss 17 to 19, 31 | Regulations |
| `cdba-reg-appeals.l4` | ss 20 to 29 | Regulations |
| `cdba-reg-compliance.l4` | ss 32, 34 | Regulations |
| `cdba-reg-penalties.l4` | ss 35, 36 | Regulations |
| `cdba-reg-debts.l4` | ss 37 to 40, 42 | Regulations |
| `cdba-act.l4` | Act ss 4 to 9, 10.1, 14 | Act |
| `cdba-tests-*.l4` | hand-written tests of each module above that holds rules (one file per module; `cdba-nouns.l4` holds types only and has none) | |
| `cdba-seat.l4`, `cdba-cases-seat.l4` | layer 2: the seat's questions and their cases | both |

Layer 1 is written from the text alone and takes nobody's point of view; layer 2 imports it and never restates a rule.
Each layer-1 rule carries an `@ref` and the verbatim `-- src:` lines it quotes (`srcrefs.py` checks every quotation and every locator against the text it names).

## Seat

**The seat:** a person with a disability who may apply for the Canada Disability Benefit, asking whether they are eligible, how the benefit is worked out, and what they must do or tell the Minister.

Why: Commons asks of every Act that it be put from the position of the individual to whom the law is applied, because the Legalese website turns such a layer into a question form.
This Act is about one person's entitlement to a monthly payment, so the individual is the person who may apply, and every question is something that person would ask: "Am I eligible ...?", "How much ...?", "Must I ...?", "Can the Minister ... me?".
There is no seat for the Minister, the Tribunal, the Registrar or the Court; what an official must do or may do is asked from the person's side as what they are owed or exposed to (see the Hohfeld pairs below).

How the seat is built:

- Every question has `@export` and `@desc`, takes plain inputs (yes/no, numbers, dates, and the modules' own plain choices), one per fact the person can state, each worded as the person is asked.
  Questions are grouped under `§§` headings in the text's order.
- A question builds the layer-1 records in its `WHERE` from those answers and calls a layer-1 rule.
  Where the rule called does not read a field, the field gets a fixed placeholder, with a comment saying so.
- The Regulations work month by month, so a question about a month takes any day in it ("Which month are you asking about? Give any day in that month").
- Every judgment of the Minister ("if the Minister is satisfied that ...") is a yes/no input worded as that.
- The Consumer Price Index is asked for 2024, 2025 and 2026 (0 means not published yet); a month from July 2028 on needs the 2027 index and comes back as not covered (NOTHING).
  The payment period that began on 1 July 2024 has no indexing factor at all (finding 5) and also comes back as not covered.
- Working income is asked as one total and entered in the first of the six fields of `Working income`; the rule reads only their sum.
- Questions that sum monthly amounts (the first payment, a lump sum on lifting a suspension) take one amount that is used for each month, with a comment; a person whose amount changes across 1 July asks month by month.
- A person with several payments after a certificate asks the s 2.1 question once for each; one qualifying payment is enough.

The questions, with the layer-1 rule each calls (87 questions, 297 cases):


**Act s 4 and Regulations ss 2 to 2.1 - Am I eligible?**

- Am I eligible to receive an allocation for this month (Regs s 2)? -> `the person is eligible to receive an allocation for the month`
- Am I at least 18 and not more than 65 years of age throughout this month (Regs s 2(1)(a))? -> `at least 18 years of age but not more than 65 years of age throughout the month`
- Do I turn 65 years of age in this month (Regs s 2(2))? -> `the person turns 65 years of age in the month`
- Do my residence and status qualify me (Regs s 2(1)(c))? -> `resident in Canada and one of the listed kinds of person`
- Am I free of a qualifying prison sentence this month (Regs s 2(1)(d))? -> `not incarcerated under a qualifying sentence in the month`
- Is this the first month of my imprisonment or the month I am released (Regs s 2(3))? -> `the month is the first month of the incarceration or the month of the release`
- Where do I stand on the condition about my spouse or partner's tax return (Regs s 2(4), 2(5))? -> `where the person stands on the cohabiting spouse or common-law partner condition`
- Is there a circumstance the Regulations name that could lead the Minister to waive the spouse or partner condition (Regs s 2(5))? -> `a circumstance named in subsection 2(5) is present`
- May the Minister waive the spouse or partner condition for me (Regs s 2(5))? -> `the Minister may waive the condition in subsection 2(4)`
- Is my allocation suspended for this month because I asked for a suspension (Regs s 2(6), 11)? -> `payment of the allocation is suspended under section 11 throughout the month`
- Am I owed the supplemental amount (Regs s 2.1)? -> `a supplemental amount is owed for the certificate`
- How much is the supplemental amount (Regs s 6.1)? -> `the supplemental amount`
- How is the supplemental amount paid (Regs s 9.1)? -> `the form in which the supplemental amount is paid`
- Am I eligible for a Canada disability benefit (Act s 4)? -> `the person is eligible for a Canada disability benefit`

**Regulations ss 4, 5 and 7 - Applying, approval, and when the allocation begins**

- On what day is my application treated as made (Regs s 4(2), 4(3))? -> `the day an application is deemed to have been made`
- Do I have to make a new application (Regs s 4(4))? -> `the allocation has ceased and a new application is needed`
- From what day is my application treated as approved (Regs s 5)? -> `the day an application is deemed to have been approved`
- Which is the first month I am entitled to an allocation (Regs s 7)? -> `the first month for which a beneficiary is entitled to an allocation`

**Regulations ss 6 to 9 - How the benefit is worked out and paid**

- Which part of section 6 works out my reduction for income (Regs s 6(1), 6(4.1))? -> `which subsection works out the reduction`
- What is my basic amount for this month, worked out under section 6 (Regs s 6(1))? -> `the basic amount payable for the month`
- What does the section 6 formula give for me this month, before any floor at zero (Regs s 6(1))? -> `the basic amount worked out by the formula for the month`
- Am I entitled to an allocation for this month (Regs s 8(1))? -> `the beneficiary is entitled to an allocation for the month`
- How much allocation is payable to me this month (Regs s 8(1))? -> `the allocation payable for the month`
- Will my allocation be paid as one lump sum for the whole payment period (Regs s 8(2))? -> `the allocation is paid as a lump sum for the payment period`
- How big would my lump sum for the payment period be (Regs s 8(2))? -> `the lump sum for the payment period`
- What will my first payment of the allocation be (Regs s 9)? -> `the first payment of an allocation`

**Regulations ss 10 and 11 - Suspension of payments**

- Can the Minister suspend my payments (Regs s 10(1))? -> `the Minister may suspend payment of the allocation`
- Can the Minister keep my payments suspended (Regs s 10(1))? -> `the Minister may keep payment of the allocation suspended`
- Has the Minister taken too long to review my eligibility (Regs s 10(2))? -> `the Minister has not reviewed the beneficiary's eligibility within a reasonable time`
- Must the Minister resume my payments and pay me what I missed (Regs s 10(3))? -> `the Minister must resume payment and pay a lump sum`
- How much will I be paid when the Minister lifts a suspension (Regs s 10(3))? -> `the lump sum on lifting a suspension`
- On what day would my payments stop if I ask the Minister to suspend them (Regs s 11(1), 11(2))? -> `the day on which payment of the allocation is suspended`
- Is my request to resume payments in time (Regs s 11(3))? -> `a request to resume payment is made in time`
- Has my allocation ended because I did not ask to resume in time (Regs s 11(3))? -> `the allocation is deemed to have ceased and a new application is needed`
- Must the Minister resume my payments when I ask (Regs s 11(4))? -> `the Minister must resume payment of the allocation`
- In which month will my payments resume (Regs s 11(5))? -> `the month in which payment of the allocation resumes`

**Regulations ss 12 to 16 - Death of a beneficiary, and representatives**

- Must I tell the Minister that a beneficiary has died (Regs s 12)? -> `the person must notify the Minister of the beneficiary's death`
- Can the estate or the heirs claim the allocation for the month the beneficiary died (Regs s 13(1))? -> `the estate or succession or the heirs are eligible to receive the allocation payment for the month of death`
- Who is paid an amount owing when a beneficiary dies (Regs s 13(2))? -> `who receives an amount owing on the death of a beneficiary`
- Can the Minister fix a date on which my death is presumed if I have disappeared (Regs s 14(1))? -> `the Minister may determine the date on which the beneficiary's death is presumed to have occurred`
- Will I be paid if the Minister changes the date of a presumed death or finds the beneficiary alive (Regs s 14(2), 14(3))? -> `the Minister must pay any benefit that would have been payable had the first determination not been made`
- May my representative act for me (Regs s 15)? -> `the representative may act on the person's behalf`
- May the Minister pay my benefit to my representative (Regs s 16)? -> `the Minister may direct that the benefit be paid on the beneficiary's behalf to their representative`

**Regulations ss 17 to 19 and 31 - Challenging a decision, and more time**

- Can the Minister change a decision made about me (Regs s 17)? -> `the Minister may amend or rescind the decision`
- Can I ask the Minister to reconsider this decision (Regs s 18(1), 18(2))? -> `the decision is one the person may ask the Minister to reconsider`
- By what day must I ask the Minister to reconsider a decision (Regs s 18(1), 18(2))? -> `the last day of the 180 days to ask the Minister to reconsider`
- Is my request for reconsideration in time (Regs s 18, 19)? -> `the request was made in time`
- Does my request for reconsideration say what the Regulations require (Regs s 18(3))? -> `the request has the contents the Regulations require`
- Must the Minister reconsider my decision and give me written reasons (Regs s 18(4))? -> `the Minister must reconsider the decision and notify the person in writing of the decision and the reasons`
- By what day must I ask the Minister for more time (Regs s 19(1))? -> `the last day to ask the Minister to extend the 180 days`
- Must the Minister allow me more time (Regs s 19(3))? -> `the Minister must allow an extension of time`
- Must the Minister consider my request for more time and tell me the reason (Regs s 19(2), 19(4))? -> `the Minister must consider the request for an extension and notify the person in writing of the decision and the reason`
- Will the Minister put right an administrative error that cost me benefit (Regs s 31)? -> `the Minister must take remedial action to put the person in the position they would be in`

**Act s 10.1 and Regulations ss 20 to 29 - Appeals**

- Does the Act let me appeal this decision (Act s 10.1)? -> `the Act allows an appeal in respect of the decision`
- How can I challenge this decision (Regs s 20)? -> `how the person may challenge the decision`
- Who decides a ground of my appeal that says the Minister got my income wrong (Regs s 21, 29)? -> `who decides the ground of appeal`
- Will the Tribunal now go on to the other grounds of my appeal (Regs s 29)? -> `the Social Security Tribunal must now proceed on the grounds not referred, under its Rules of Procedure`
- Will another person be made a party to my appeal (Regs s 23)? -> `the other person is added as a party to the appeal`
- Where will the hearing of my reference be held (Regs s 24(2))? -> `where the hearing of a reference is held`
- Must the Registrar tell me by registered mail when my hearing is set (Regs s 24(3))? -> `the Registrar must notify the appellant by registered mail of the date, place and time`
- Can the judge make me file written submissions (Regs s 26)? -> `the judge may require written submissions`
- Can I be made to pay costs or fees on a reference to the Tax Court (Regs s 28)? -> `costs may be awarded or fees charged to the appellant on a reference`

**Act ss 5 to 7 and Regulations ss 32 to 34 - Being paid, and what I must give or tell the Minister**

- Must the Minister pay me a Canada disability benefit (Act s 5)? -> `the Minister must pay a Canada disability benefit to the person`
- Must I give the Minister the information they ask for about my application (Act s 6)? -> `the person must provide the Minister with the information`
- Can the Minister collect and use my Social Insurance Number (Act s 7)? -> `the Minister is authorized to collect and use the person's Social Insurance Number`
- Must I give the Minister the information or document in their notice (Regs s 32(2), 32(3))? -> `the person is required to provide the information or document`
- By what day can I apply to a judge to review an authorization served on me (Regs s 32(6))? -> `the last day to apply for a review of the authorization`
- Can the Minister require me to be at a place or available at a time (Regs s 34)? -> `the person is required to be at a suitable place or available at a suitable time`

**Regulations ss 35 and 36 - Penalties and offences**

- Have I committed a violation (Regs s 35(1))? -> `the person commits a violation`
- Can the Minister impose a penalty on me (Regs s 35(2), 35(5), 35(6))? -> `the Minister may impose a penalty`
- Is this a first violation for me (Regs s 35(4))? -> `the violation is deemed to be a first violation`
- How large could my penalty be (Regs s 35(3))? -> `the penalty the Minister may issue`
- Can the Minister cancel a penalty imposed on me (Regs s 35(7))? -> `the Minister may rescind the penalty`
- Am I guilty of an offence (Regs s 36(1))? -> `the person is guilty of an offence punishable on summary conviction`
- Can I still be prosecuted for an act if a penalty was imposed for it (Regs s 36(2))? -> `a proceeding may be commenced under section 36 or the Criminal Code for the act`

**Act s 9 and Regulations ss 37 to 40 - Overpayments, debts and recovery**

- Can my benefit be taken to pay another debt or claim (Act s 9)? -> `how the benefit stands against the claim`
- What do I owe if I was paid more than I was entitled to (Regs s 37(1))? -> `the amount that must be returned`
- From what day is the overpayment a debt I owe (Regs s 37(2))? -> `the day from which the erroneous payment or overpayment is a debt due to His Majesty`
- Can I pay what I owe in instalments (Regs s 37(3))? -> `the debt may be paid in instalments`
- Will I be charged interest on what I owe (Regs s 37(4), 37(5))? -> `interest is payable on the amount owing`
- From what day is a penalty I was given a debt I owe (Regs s 38(1))? -> `the day from which a penalty is a debt due to His Majesty`
- Does interest run on my penalty (Regs s 38(2))? -> `interest accrues on the penalty debt`
- By what day must action be taken to recover money I owe (Regs s 39(1), 39(2))? -> `the last day on which an action to recover money may be taken`
- Does the six-year limit apply to the proceedings against me (Regs s 39(3))? -> `the six-year limitation period applies`
- When may the Minister certify what I owe (Regs s 40(1))? -> `the earliest day on which the unrecovered debt may be certified`
- Can the Minister take money that someone owes me (Regs s 40(6))? -> `the Minister may require the money to be paid to the Receiver General`
- If someone does not pay the Minister as a garnishment notice requires, is the amount a debt (Regs s 40(7))? -> `the unpaid amount is a debt due to His Majesty`

Layer-1 rules the seat does not call directly, and why: Act s 8 (the Minister's agreements with departments and agencies, and publishing them: addressed only to the Minister, so no seat), Act s 14 and Regs s 42 (commencement: nothing the person asks), `the date of death for the purposes of the Act and these Regulations` (s 14: the seat asks whether the Minister may fix a date and whether benefit is paid after a change, not which date applies), and the helpers the questions above reach through the rule they call (the three reductions, the indexing factor, the rounding rule, the two `calendar year ...` rules and the definition of "release" in s 1, the time-limit and protection tests inside the penalty and extension questions).
Provisions the coverage table marks inert (Regs ss 3, 4(1), 22, 24(1), 25, 27, 30, 33, 40(2) to (5)) have no question for the same reason they have no rule.


## Jural relations

One row per provision that creates a relation between two parties, with the party that holds the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, and the L4 rule that carries it.
A provision that creates no such relation (a definition, a counting rule, a purpose clause) appears once, with `none`.
Each relation is stated once in layer 1 under a neutral name and is never restated from the other side.
Hohfeld's correlatives: a claim (right) matches a duty, a privilege matches a no-right, a power matches a liability, an immunity matches a disability.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | relation | L4 rule |
|---|---|---|---|---|
| Act s 4 | the person meeting the criteria | none | a status (eligibility), no counterparty: the claim it leads to is s 5 | `the person is eligible for a Canada disability benefit` (none as a relation) |
| Act s 5 | an eligible person who applies and meets any other condition | the Minister | claim / duty to pay a benefit | `the Minister must pay a Canada disability benefit to the person` |
| Act s 6 | the Minister | an applicant, or the representative of an incapable applicant | claim / duty to give information the Minister requires | `the person must provide the Minister with the information` |
| Act s 7 | the Minister | an applicant | privilege (to collect and use the Social Insurance Number) / no-right | `the Minister is authorized to collect and use the person's Social Insurance Number` |
| Act s 8(1) | the Minister | a federal or provincial department or agency (a province's only with the Governor in Council's approval) | power / liability to be made party to an agreement | `the Minister may enter into an agreement with the party` |
| Act s 8(2) | the public | the Minister | claim / duty to make an agreement public | `the Minister must make the agreement public` |
| Act s 9(a) to (c) | the beneficiary | creditors and every claimant named (bankruptcy law, assignment, charge, attachment, security, retention by deduction or set-off under another Act of Parliament) | immunity / disability | `how the benefit stands against the claim` |
| Act s 9(d) | a claimant under the Family Orders and Agreements Enforcement Assistance Act | the beneficiary | power / liability (the benefit is garnishable moneys) | `how the benefit stands against the claim` |
| Act s 10.1 | the person, or another acting for them | the appeal body the regulations name | power / liability to hear an appeal | `the Act allows an appeal in respect of the decision` |
| Regs s 1 (definitions) | none | none | none: definitions and a counting rule | `the person is an applicant`, `the person is a beneficiary`, `the payment period that includes the day`, `the event is a release` (none) |
| Regs s 2(1) to (4), (6) | none | none | none: the criteria that make a person eligible, a status | `the person is eligible to receive an allocation for the month` (none as a relation) |
| Regs s 2(5) | the Minister | the person with a cohabiting spouse or common-law partner | power / liability (waiver in the person's favour) | `the Minister may waive the condition in subsection 2(4)` |
| Regs s 2.1 | an eligible person with a certificate | the Minister | claim / duty to pay the supplemental amount | `a supplemental amount is owed for the certificate` |
| Regs s 3 | the Minister | none for the person | privilege to learn age and identity from the Commission's information | none (inert) |
| Regs s 4(1) | the Minister | the applicant | claim / duty to apply in the form and manner specified | none (inert: the specification is not in the text) |
| Regs s 4(2), (3), s 5, s 7 | none | none | counting rules for the day an application is made, approved, and the first month | `the day an application is deemed to have been made`, `the day an application is deemed to have been approved`, `the first month for which a beneficiary is entitled to an allocation` (none) |
| Regs s 4(4) | none | the beneficiary | liability to the allocation ceasing, and so a duty to apply again | `the allocation has ceased and a new application is needed` |
| Regs s 6, s 8(1) | the beneficiary | the Minister | claim / duty to pay the monthly allocation | `the allocation payable for the month` |
| Regs s 8(2) | none | none | a rule on the form of payment (a lump sum) | `the allocation is paid as a lump sum for the payment period`, `the lump sum for the payment period` (none) |
| Regs s 9 | the beneficiary | the Minister | claim / duty to pay the first payment as the sum of earlier months | `the first payment of an allocation` |
| Regs s 9.1 | none | none | a rule on the form of payment | `the form in which the supplemental amount is paid` (none) |
| Regs s 10(1) | the Minister | the beneficiary | power / liability to have payment suspended | `the Minister may suspend payment of the allocation`, `the Minister may keep payment of the allocation suspended` |
| Regs s 10(2) | the beneficiary | the Minister | claim / duty to review eligibility within a reasonable time | `the Minister has not reviewed the beneficiary's eligibility within a reasonable time` |
| Regs s 10(3) | the beneficiary | the Minister | claim / duty to resume payment and pay a lump sum | `the Minister must resume payment and pay a lump sum`, `the lump sum on lifting a suspension` |
| Regs s 11(1), (2) | the beneficiary | the Minister | power / liability (a suspension follows the beneficiary's request) | `the day on which payment of the allocation is suspended` |
| Regs s 11(3) | the beneficiary | the Minister | power / liability (a request to resume made in time); and a liability of the beneficiary to the allocation ceasing | `a request to resume payment is made in time`, `the allocation is deemed to have ceased and a new application is needed` |
| Regs s 11(4) | the beneficiary | the Minister | claim / duty to resume payment if satisfied of eligibility | `the Minister must resume payment of the allocation` |
| Regs s 11(5) | none | none | a counting rule (the month payment resumes) | `the month in which payment of the allocation resumes` (none) |
| Regs s 12 | the Minister | the executor, administrator, liquidator or heirs of a deceased beneficiary | claim / duty to notify the death | `the person must notify the Minister of the beneficiary's death` |
| Regs s 13(1), (2) | the estate, succession or heirs (or the Minister's designee if none) | the Minister | claim / duty to pay what is owing on the death | `the estate or succession or the heirs are eligible to receive the allocation payment for the month of death`, `who receives an amount owing on the death of a beneficiary` |
| Regs s 14(1) | the Minister | the beneficiary and the estate | power / liability (a deemed date of death) | `the Minister may determine the date on which the beneficiary's death is presumed to have occurred`, `the date of death for the purposes of the Act and these Regulations` |
| Regs s 14(2), (3) | the beneficiary or estate | the Minister | claim / duty to pay what would have been payable | `the Minister must pay any benefit that would have been payable had the first determination not been made` |
| Regs s 14(4) | the Minister | none | privilege not to be bound by a death certificate | none (inert) |
| Regs s 15 | the representative | those the representative deals with for the person | power / liability | `the representative may act on the person's behalf` |
| Regs s 16 | the Minister | the beneficiary | power / liability to have the benefit paid to a representative | `the Minister may direct that the benefit be paid on the beneficiary's behalf to their representative` |
| Regs s 17 | the Minister | the person the decision is about | power / liability to have a decision amended or rescinded | `the Minister may amend or rescind the decision` |
| Regs s 18(1), (2) | the dissatisfied person | the Minister | power / liability (a request for reconsideration made within 180 days) | `the decision is one the person may ask the Minister to reconsider`, `the request was made in time`, `the request has the contents the Regulations require` |
| Regs s 18(4) | the person who asked | the Minister | claim / duty to reconsider and to give written reasons | `the Minister must reconsider the decision and notify the person in writing of the decision and the reasons` |
| Regs s 19(1), (2) | the person | the Minister | power / liability (a request to extend the 180 days) | `the request for an extension was made in time` |
| Regs s 19(3) | the person | the Minister | claim / duty to allow an extension if satisfied a situation occurred | `the Minister must allow an extension of time` |
| Regs s 19(4) | the person | the Minister | claim / duty to consider the request within a reasonable time and notify | `the Minister must consider the request for an extension and notify the person in writing of the decision and the reason` |
| Regs s 20(1) to (3) | the person | the Social Security Tribunal | power / liability (an appeal from the Minister's reconsideration decisions) | `how the person may challenge the decision` |
| Regs s 21(1), s 29 | the appellant | the Tribunal | claim / duty to refer the income ground to the Court and to proceed on the rest | `who decides the ground of appeal`, `the Social Security Tribunal must now proceed on the grounds not referred, under its Rules of Procedure` |
| Regs s 23(1), (2) | the Minister, and the other person added | the Tribunal, the Registrar | duty to pass on the opinion and to add the person as a party | `the other person is added as a party to the appeal` |
| Regs s 24(2) | the appellant | the Court | immunity / disability (the place of the hearing, unless the appellant consents) | `where the hearing of a reference is held` |
| Regs s 24(3) | the appellant | the Registrar | claim / duty to notify by registered mail | `the Registrar must notify the appellant by registered mail of the date, place and time` |
| Regs s 26 | the appellant | the judge | immunity / disability (written submissions only with consent) | `the judge may require written submissions` |
| Regs s 28 | the appellant | the Court | immunity / disability (no costs, no fees) | `costs may be awarded or fees charged to the appellant on a reference` |
| Regs s 21(2), 22, 23(3), (4), 24(1), 25, 27, 30, 33 | none | none | none: definitions and the Court's and the Registrar's internal steps | none (inert) |
| Regs s 31 | the person denied a benefit by an administrative error | the Minister | claim / duty to take remedial action | `the Minister must take remedial action to put the person in the position they would be in` |
| Regs s 32(1) | the Minister | none for the person | privilege to examine documents | none (inert) |
| Regs s 32(2), (3) | the Minister | an applicant, a beneficiary or their representative; anyone else only if a judge has authorized it | power / liability; immunity of anyone else until the authorization is served | `the person is required to provide the information or document` |
| Regs s 32(6) | the person served with an authorization | the judge | power / liability (a review within 15 days) | `the last day to apply for a review of the authorization` |
| Regs s 34 | the Minister | an applicant, a beneficiary or their representative | power / liability to be required to appear or be available | `the person is required to be at a suitable place or available at a suitable time` |
| Regs s 35(1), (2) | the Minister | the person who commits a violation | power / liability to a penalty | `the person commits a violation`, `the Minister may impose a penalty` |
| Regs s 35(3), (4) | none | none | a rule on the size of the penalty | `the penalty the Minister may issue`, `the violation is deemed to be a first violation` (none) |
| Regs s 35(5), (6) | the person | the Minister | immunity / disability (a mistaken belief, a started prosecution, five years from awareness) | `the person is protected from a penalty by a mistaken belief`, `the time for imposing a penalty has run out` |
| Regs s 35(7) | the Minister | the penalised person | power / liability (a rescission in the person's favour) | `the Minister may rescind the penalty` |
| Regs s 36(1) | the Crown | the person who commits one of the three acts | power / liability to prosecution | `the person is guilty of an offence punishable on summary conviction` |
| Regs s 36(2) | the person | the Crown | immunity / disability (no proceeding once a penalty is imposed) | `a proceeding may be commenced under section 36 or the Criminal Code for the act` |
| Regs s 37(1), (2) | the Crown | the person or agency that received an erroneous payment or overpayment | claim / duty to return it, as a debt | `the amount that must be returned`, `the day from which the erroneous payment or overpayment is a debt due to His Majesty` |
| Regs s 37(3) | the Minister | the debtor | power (to agree to instalments) | `the debt may be paid in instalments` |
| Regs s 37(4), (5), s 38(2) | the debtor | the Crown | immunity / disability (no interest, except after a penalised violation or sentenced offence once no remedy is open) | `interest is payable on the amount owing`, `interest accrues on the penalty debt` |
| Regs s 38(1) | the Crown | the penalised person | claim / duty (the penalty is a debt) | `the day from which a penalty is a debt due to His Majesty` |
| Regs s 39 | the debtor | the Crown | immunity / disability (no action after six years, with suspension) | `the last day on which an action to recover money may be taken`, `the six-year limitation period applies` |
| Regs s 40(1) | the Minister | the debtor | power / liability to a certificate | `the earliest day on which the unrecovered debt may be certified` |
| Regs s 40(2) to (5) | the Crown | the debtor | power / liability (registration and charge) | none (inert) |
| Regs s 40(6), (7) | the Minister | a person indebted to the debtor | power / liability (garnishment); a debt if not paid | `the Minister may require the money to be paid to the Receiver General`, `the unpaid amount is a debt due to His Majesty` |
| Regs s 41, s 42, preamble | none | none | none: an amendment blank in this text, a commencement date, recitals | `the day the Regulations come into force` (none) |
| Act preamble, ss 1, 2, 3, 10, 11, 11.1, 11.2, 12, 13 | none | none | none: purpose, names, funding, rule-making and reporting machinery | none (inert) |
| Act s 14 | none | none | a counting rule for commencement | `the latest day on which the Act could be brought into force`, `the day fixed for commencement is within the time section 14 allows` (none) |


### Pairs in the seat

Where the text gives the person a claim, privilege, power or immunity, the seat question takes as inputs the facts about the other side (what the Minister has done or is satisfied of, whether a notice was served, whether a judge authorized it).
Where the text also puts a duty or a liability on the person there is a paired question, listed in the right-hand column.

| relation | questions where the person holds the claim, privilege, power or immunity (what they are owed, may do or are protected from) | questions where the person bears the duty or liability (what they owe, or what can be done to them) |
|---|---|---|
| payment of a benefit (Act s 5; Regs ss 6 to 9) | Must the Minister pay me a Canada disability benefit?; What is my basic amount for this month?; What will my first payment of the allocation be? | Must I give the Minister the information they ask for about my application?; Must I give the Minister the information or document in their notice?; Can the Minister require me to be at a place or available at a time? |
| suspension (Regs ss 10, 11) | Has the Minister taken too long to review my eligibility?; Must the Minister resume my payments and pay me what I missed?; Must the Minister resume my payments when I ask? | Can the Minister suspend my payments?; Can the Minister keep my payments suspended?; Is my allocation suspended for this month because I asked for a suspension? |
| the person's own power to stop and restart payment (Regs s 11) | On what day would my payments stop if I ask the Minister to suspend them?; Is my request to resume payments in time?; In which month will my payments resume? | Has my allocation ended because I did not ask to resume in time? |
| decisions (Regs ss 17 to 20, 31) | Can I ask the Minister to reconsider this decision?; Must the Minister reconsider my decision and give me written reasons?; Must the Minister allow me more time?; Will the Minister put right an administrative error that cost me benefit?; How can I challenge this decision? | Can the Minister change a decision made about me? |
| death and representatives (Regs ss 12 to 16) | Can the estate or the heirs claim the allocation for the month the beneficiary died?; Who is paid an amount owing when a beneficiary dies?; May my representative act for me?; Will the benefit be paid if the Minister changes the presumed date of death or finds me alive? | Must I tell the Minister that a beneficiary has died?; Can the Minister fix a date on which my death is presumed if I have disappeared?; May the Minister pay my benefit to my representative? |
| penalties and offences (Regs ss 35, 36) | Can the Minister cancel a penalty imposed on me?; Can I still be prosecuted for an act if a penalty was imposed for it?; Is this a first violation for me? | Have I committed a violation?; Can the Minister impose a penalty on me?; How large could my penalty be?; Am I guilty of an offence? |
| debts and recovery (Act s 9; Regs ss 37 to 40) | Can my benefit be taken to pay another debt or claim?; Can I pay what I owe in instalments?; Will I be charged interest on what I owe?; Does interest run on my penalty?; Does the six-year limit apply to the proceedings against me? | What do I owe if I was paid more than I was entitled to?; From what day is the overpayment a debt I owe?; From what day is a penalty I was given a debt I owe?; By what day must action be taken to recover money I owe?; When may the Minister certify what I owe?; Can the Minister take money that someone owes me? |
| appeals (Act s 10.1; Regs ss 21 to 29) | Does the Act let me appeal this decision?; Who decides a ground of my appeal that says the Minister got my income wrong?; Where will the hearing of my reference be held?; Can the judge make me file written submissions?; Can I be made to pay costs or fees on a reference to the Tax Court?; Must the Registrar tell me by registered mail when my hearing is set?; Will the Tribunal now go on to the other grounds of my appeal? | Will another person be made a party to my appeal? |


## What is encoded and what is not

Encoded: every operative provision of the Act that decides something for a person (ss 4 to 9, 10.1, 14) and of the Regulations (ss 1 to 2.1, 4 to 40 apart from the inert subsections listed below, and 42, with the related provision SOR/2026-123 s 14), as rules that answer the question the section asks: who qualifies, for which months, how much, when it starts, when it is suspended, ends or resumes, what must be told or given and by when, what can be reconsidered or appealed and by when, what a penalty or offence is, what must be returned and until when it can be recovered.
Duties are encoded as tests of whether the duty has arisen, and of its amount, never as obligations with a deadline the text does not give.

Not encoded, each with a reason in the coverage table: the preamble and purposes; the definitions that are only names; regulation-making, funding, reporting and review machinery (Act ss 10 to 12); the amendments in Act s 13 and Regs s 41, which the text prints as `[Amendments]` with no wording; the form and manner of an application (Regs s 4(1)), which the Minister specifies outside the text; the Tax Court's and the Registrar's internal procedure (Regs ss 22, 24(1), 25, 27, 30, 33); registration of a certificate in the Federal Court (Regs s 40(2) to (5)).

Borrowed terms, asked as facts and never given a meaning: "cohabiting spouse or common-law partner" and "adjusted income" (Income Tax Act s 122.6), "DTC-eligible individual" (s 146.4(1)), the two limbs of "working income" (s 122.7(1)), "resident in Canada for the purposes of the Income Tax Act", "return of income", the five kinds of person in s 2(1)(c) (Immigration and Refugee Protection Act, Indian Act), "judge", "representative", "incapable of managing their own affairs", and the Consumer Price Index figures.

Not modelled: the day any payment is made (ss 8(2), 9); the length of an extension the Minister allows under s 19(3); a rate of interest; the punishment for an offence; what a "suitable" place or time is (s 34); the conditions a judge may attach (s 32(4)).

## Coverage table

One row per section, subsection or definition.
Counts: 141 rows; encoded 109; inert 30; repealed or blank in this text 2; not applicable 0.

| provision | disposition | where it is encoded, or why not |
|---|---|---|

| Act: Preamble | inert | Eleven recitals (poverty among working-age persons with disabilities, barriers to employment, intersecting statuses, the Accessible Canada Act, the Charter, the Convention on the Rights of Persons with Disabilities, the Poverty Reduction Act, the Sustainable Development Goals, benefits for seniors and families, "Nothing Without Us", the provinces and territories). They state why Parliament acted; they add no condition and decide nothing for a person. |
| Act s 1 (short title) | inert | The Act may be cited as the Canada Disability Benefit Act. A name. |
| Act s 2 "disability" | inert | Same meaning as in s 2 of the Accessible Canada Act (not among the inputs). No operative section of the Act or the Regulations tests whether a person has a disability: the Regulations' criterion is that the person is a DTC-eligible individual (Regs s 2(1)(b)), which is asked as a fact. The word appears only in the purposes, the preamble and the regulation-making powers. |
| Act s 2 "Minister" | inert | The Minister of Employment and Social Development. A name; every rule that mentions the Minister mentions that office and nothing turns on who holds it. |
| Act s 3 (purposes) | inert | The purposes are to reduce poverty and to support the financial security of working-age persons with disabilities. A statement of purpose with no condition and no consequence. |
| Act s 4 (eligibility) | encoded | cdba-act.l4 `the person is eligible for a Canada disability benefit` (the criteria are the Regulations': s 2 for an allocation and s 2.1 for the supplemental amount) |
| Act s 5 (payment of benefit) | encoded | cdba-act.l4 `the Minister must pay a Canada disability benefit to the person` |
| Act s 6 (information) | encoded | cdba-act.l4 `the person must provide the Minister with the information` |
| Act s 7 (Social Insurance Number) | encoded | cdba-act.l4 `the Minister is authorized to collect and use the person's Social Insurance Number` |
| Act s 8(1) (agreements) | encoded | cdba-act.l4 `the Minister may enter into an agreement with the party` |
| Act s 8(2) (publication) | encoded | cdba-act.l4 `the Minister must make the agreement public` |
| Act s 9(a) to (d) (payments cannot be charged) | encoded | cdba-act.l4 `how the benefit stands against the claim` |
| Act s 10 (Consolidated Revenue Fund) | inert | All benefits payable are paid out of the Consolidated Revenue Fund. It names the source of the money and sets no condition on whether, when or how much is paid. |
| Act s 10.1(a) to (c) (appeals) | encoded | cdba-act.l4 `the Act allows an appeal in respect of the decision`; the route the Regulations allow is cdba-reg-appeals.l4 `how the person may challenge the decision` |
| Act s 11(1)(a) to (u) (regulations) | inert | The Governor in Council's power to make regulations on twenty-one subjects. It has been used: it is the authority for the Canada Disability Benefit Regulations, which are encoded. Paragraphs (q) and (r) authorise the offences and penalties that Regs ss 35 and 36 set up. |
| Act s 11(1.1) (amount of benefit) | inert | In making regulations on the amount, the Governor in Council must take five things into consideration (the Official Poverty Line, the cost of living with a disability, the challenge of earning, intersectional needs, human rights obligations). A duty on the rule-maker, now discharged (the Regulations' recitals say so); no person can meet or fail it. |
| Act s 11(1.2) (regulations within 12 months) | inert | The Governor in Council must make the regulations needed to pay a benefit within 12 months of the Act coming into force. A duty on the rule-maker, now discharged by SOR/2025-35; it decides nothing for a person. |
| Act s 11(2) (classes) | inert | Regulations may distinguish among classes of applicants and beneficiaries. The Regulations do so in the reductions for single beneficiaries and those with partners (Regs s 6); the power itself is the rule-maker's. |
| Act s 11.1 (collaboration) | inert | The Minister must give persons with disabilities meaningful and barrier-free opportunities to collaborate in developing the regulations. A duty owed while the Regulations were made, discharged according to the Regulations' recitals; nothing in it turns on a fact about a person applying for the benefit. |
| Act s 11.2(1) to (4) (progress reports) | inert | Within six months and one year after commencement the Minister must table reports in Parliament, which stand referred to a committee and are published on the department's website. Duties to Parliament about the making of the Regulations; an applicant or beneficiary has no claim under them and nothing to do. |
| Act s 12 (parliamentary review) | inert | A committee of the Senate or House of Commons reviews the Act and its administration after the first and third anniversaries of commencement and each fifth anniversary after. A task for Parliament, with no effect on any person's entitlement. |
| Act s 13 (amendment of the Income Tax Act) | repealed or blank in this text | The text shows only "13 [Amendments]": the section is a consequential amendment of the Income Tax Act, and the amending text is not reproduced in the deposited text. |
| Act s 14 (coming into force) | encoded | cdba-act.l4 `the latest day on which the Act could be brought into force`, `the day fixed for commencement is within the time section 14 allows` (the assent date and the order's date are stated inputs: neither is in the text) |
| Regs: preamble (recitals and enabling authority) | inert | Recitals that the Governor in Council considered the elements in s 11(1.1) of the Act and that the Minister provided collaboration opportunities under s 11.1, and the enabling authority (s 11(1) of the Act and s 69 of the Department of Employment and Social Development Act). They explain how the Regulations came to be made and add no condition. |
| Regs s 1 "Act" | inert | A name: the Canada Disability Benefit Act. Nothing is decided by it. |
| Regs s 1 "allocation" | inert | Glossed in cdba-reg-definitions.l4: the part of a benefit that is the monthly payments worked out under s 6. Every rule that mentions an allocation takes it as that; no separate rule is needed to decide it. |
| Regs s 1 "applicant" | encoded | cdba-reg-definitions.l4 `the person is an applicant` |
| Regs s 1 "beneficiary" | encoded | cdba-reg-definitions.l4 `the person is a beneficiary` |
| Regs s 1 "benefit" | inert | A name: a Canada disability benefit payable under the Act. Nothing is decided by it. |
| Regs s 1 "cohabiting spouse or common-law partner" | encoded | Borrowed term (Income Tax Act s 122.6, not among the inputs): asked as a fact in cdba-nouns.l4 (`Person facts for a month`, `Income and household facts`). |
| Regs s 1 "DTC-eligible individual" | encoded | Borrowed term (Income Tax Act s 146.4(1), not among the inputs): asked as a fact in cdba-nouns.l4 `a DTC-eligible individual throughout the month`. |
| Regs s 1 "payment period" | encoded | cdba-reg-definitions.l4 `the payment period that includes the day` |
| Regs s 1 "release" | encoded | cdba-reg-definitions.l4 `the event is a release` |
| Regs s 1 "supplemental amount" | inert | A name pointing at s 6.1; the amount itself is encoded there. |
| Regs s 2(1) lead-in and (a) | encoded | cdba-reg-eligibility.l4 `the month is after May 2025`, `at least 18 years of age but not more than 65 years of age throughout the month` |
| Regs s 2(1)(b) | encoded | cdba-reg-eligibility.l4 `a DTC-eligible individual for the month` (borrowed term, asked as a fact) |
| Regs s 2(1)(c) | encoded | cdba-reg-eligibility.l4 `resident in Canada and one of the listed kinds of person` |
| Regs s 2(1)(d) | encoded | cdba-reg-eligibility.l4 `not incarcerated under a qualifying sentence in the month` |
| Regs s 2(1)(e) | encoded | cdba-reg-eligibility.l4 `a return of income filed for the last taxation year that ended before the payment period` |
| Regs s 2(2) | encoded | cdba-reg-eligibility.l4 `the person turns 65 years of age in the month` |
| Regs s 2(3) | encoded | cdba-reg-eligibility.l4 `the month is the first month of the incarceration or the month of the release` |
| Regs s 2(4) | encoded | cdba-reg-eligibility.l4 `the cohabiting spouse or common-law partner condition is satisfied`, `where the person stands on the cohabiting spouse or common-law partner condition` |
| Regs s 2(5) | encoded | cdba-reg-eligibility.l4 `the Minister may waive the condition in subsection 2(4)` (a conditional input: the Minister is satisfied that), `a circumstance named in subsection 2(5) is present` |
| Regs s 2(6) | encoded | cdba-reg-eligibility.l4 `payment of the allocation is suspended under section 11 throughout the month` (fork F12) |
| Regs s 2.1(1) | encoded | cdba-reg-eligibility.l4 `a supplemental amount is owed for the certificate` |
| Regs s 2.1(2) | encoded | cdba-reg-eligibility.l4 `a supplemental amount is owed for the certificate` (the qualifying test requires entitlement) |
| Regs s 3 | inert | The Minister may determine the age and identity of an applicant from information the Canada Employment Insurance Commission made available under s 28.2(5) of the Department of Employment and Social Development Act. It is a permission to the Minister about how to find out two facts; it adds no condition to eligibility and gives the applicant nothing to do or to be owed. The age is asked as a date of birth in `Person facts for a month` in any case. |
| Regs s 4(1) | inert | An application must be made in the form and manner the Minister specifies. The specification is not in the text, so there is nothing to test: the duty binds every applicant on every application, and no fact the person could state changes it. The seat says what it cannot answer in NOTES.md. |
| Regs s 4(2) | encoded | cdba-reg-application.l4 `the day an application is deemed to have been made` (NOTHING when the Minister has not received it) |
| Regs s 4(3) | encoded | cdba-reg-application.l4 `the day an application is deemed to have been made` (fork F14) |
| Regs s 4(4) | encoded | cdba-reg-application.l4 `the allocation has ceased and a new application is needed` (fork F11) |
| Regs s 5(1) | encoded | cdba-reg-application.l4 `the day an application is deemed to have been approved` (fork F13) |
| Regs s 5(2) | encoded | cdba-reg-application.l4 `the day an application is deemed to have been approved` (24 months back, `add months`) |
| Regs s 6(1) | encoded | cdba-reg-amount.l4 `the basic amount worked out by the formula`, `the basic amount payable` (fork F9), `the basic amount worked out by the formula for the month`, `the basic amount payable for the month` |
| Regs s 6(2) | encoded | cdba-reg-amount.l4 `the reduction based on income when the beneficiary has no cohabiting spouse or common-law partner` |
| Regs s 6(3) | encoded | cdba-reg-amount.l4 `the reduction based on income when the cohabiting spouse or common-law partner is not a beneficiary` |
| Regs s 6(4) | encoded | cdba-reg-amount.l4 `the reduction based on income when the cohabiting spouse or common-law partner is also a beneficiary` |
| Regs s 6(4.1) | encoded | cdba-reg-amount.l4 `which subsection works out the reduction`, `the reduction based on income` |
| Regs s 6(5) | encoded | cdba-reg-amount.l4 `the indexing factor for the payment period` |
| Regs s 6(6) | encoded | cdba-reg-amount.l4 `the indexing factor for the payment period` (the figures are inputs of the kind named in s 6(6); the encoding holds none) |
| Regs s 6(7) | encoded | cdba-reg-amount.l4 `the working income` ("adjusted income" is a borrowed term: Income Tax Act s 122.6, asked as a fact) |
| Regs s 6.1 | encoded | cdba-reg-amount.l4 `the supplemental amount` |
| Regs s 7 | encoded | cdba-reg-payment.l4 `the first month for which a beneficiary is entitled to an allocation` |
| Regs s 8(1) | encoded | cdba-reg-payment.l4 `the beneficiary is entitled to an allocation for the month`, `the allocation payable for the month` |
| Regs s 8(2) | encoded | cdba-reg-payment.l4 `the allocation is paid as a lump sum for the payment period`, `the lump sum for the payment period` (fork F10; the day the lump sum is paid is not modelled) |
| Regs s 9 | encoded | cdba-reg-payment.l4 `the first payment of an allocation` |
| Regs s 9.1 | encoded | cdba-reg-payment.l4 `the form in which the supplemental amount is paid` |
| Regs s 10(1) | encoded | cdba-reg-suspension.l4 `the Minister may suspend payment of the allocation`, `the Minister may keep payment of the allocation suspended` (the Minister reasonable grounds are conditional inputs) |
| Regs s 10(2) | encoded | cdba-reg-suspension.l4 `the Minister has not reviewed the beneficiary's eligibility within a reasonable time` (whether a reasonable time has passed is an input; the text names no consequence) |
| Regs s 10(3) | encoded | cdba-reg-suspension.l4 `the Minister must resume payment and pay a lump sum`, `the lump sum on lifting a suspension` |
| Regs s 11(1) | encoded | cdba-reg-suspension.l4 `the day on which payment of the allocation is suspended` (NOTHING if the request is not in writing) |
| Regs s 11(2) | encoded | cdba-reg-suspension.l4 `the day on which payment of the allocation is suspended` (later of the last day of the processing month and the day indicated; fork F12 for its effect on eligibility) |
| Regs s 11(3) | encoded | cdba-reg-suspension.l4 `a request to resume payment is made in time`, `the allocation is deemed to have ceased and a new application is needed` |
| Regs s 11(4) | encoded | cdba-reg-suspension.l4 `the Minister must resume payment of the allocation` (the Minister is satisfied is a conditional input) |
| Regs s 11(5) | encoded | cdba-reg-suspension.l4 `the month in which payment of the allocation resumes` |
| Regs s 12 | encoded | cdba-reg-death.l4 `the person must notify the Minister of the beneficiary's death` (the text sets no day: "as soon as feasible") |
| Regs s 13(1) | encoded | cdba-reg-death.l4 `the estate or succession or the heirs are eligible to receive the allocation payment for the month of death` |
| Regs s 13(2) | encoded | cdba-reg-death.l4 `who receives an amount owing on the death of a beneficiary` |
| Regs s 14(1) | encoded | cdba-reg-death.l4 `the Minister may determine the date on which the beneficiary's death is presumed to have occurred`, `the date of death for the purposes of the Act and these Regulations` |
| Regs s 14(2) | encoded | cdba-reg-death.l4 `the Minister must pay any benefit that would have been payable had the first determination not been made`, `the date of death for the purposes of the Act and these Regulations` |
| Regs s 14(3) | encoded | cdba-reg-death.l4 `the Minister must pay any benefit that would have been payable had the first determination not been made` |
| Regs s 14(4) | inert | The Minister is not bound by the issuing or revoking of a death certificate by another authority. It is a rule about what evidence the Minister may weigh; it gives the person nothing to do, to be owed, or to be exposed to, and adds no condition to any decision in these modules (the Minister's conclusion in s 14(1) is already a conditional input). |
| Regs s 15 | encoded | cdba-reg-death.l4 `the representative may act on the person's behalf` ("representative" is not defined in the Regulations: asked as a fact) |
| Regs s 16 | encoded | cdba-reg-death.l4 `the Minister may direct that the benefit be paid on the beneficiary's behalf to their representative` |
| Regs s 17 | encoded | cdba-reg-reviews.l4 `the Minister may amend or rescind the decision` |
| Regs s 18(1) | encoded | cdba-reg-reviews.l4 `the decision is one the person may ask the Minister to reconsider`, `the last day of the 180 days to ask the Minister to reconsider`, `the request was made in time` |
| Regs s 18(2) | encoded | cdba-reg-reviews.l4 `the decision is one the person may ask the Minister to reconsider` (penalty decisions), `the request was made in time` |
| Regs s 18(3) | encoded | cdba-reg-reviews.l4 `the request has the contents the Regulations require` |
| Regs s 18(4) | encoded | cdba-reg-reviews.l4 `the Minister must reconsider the decision and notify the person in writing of the decision and the reasons` (the Minister's choice among confirm, amend, rescind and the rest is the Minister's, not modelled) |
| Regs s 19(1) | encoded | cdba-reg-reviews.l4 `the last day to ask the Minister to extend the 180 days`, `the request for an extension was made in time` |
| Regs s 19(2) | encoded | cdba-reg-reviews.l4 `the Minister must consider the request for an extension and notify the person in writing of the decision and the reason` (the Minister's specification of the form and manner is asked as a fact) |
| Regs s 19(3) | encoded | cdba-reg-reviews.l4 `the Minister must allow an extension of time` (the Minister is satisfied is a conditional input; the length of the extension is not stated and is an input to `the request was made in time`) |
| Regs s 19(4) | encoded | cdba-reg-reviews.l4 `the Minister must consider the request for an extension and notify the person in writing of the decision and the reason` |
| Regs s 20(1) | encoded | cdba-reg-appeals.l4 `how the person may challenge the decision` (the body is the Social Security Tribunal) |
| Regs s 20(2) | encoded | cdba-reg-appeals.l4 `how the person may challenge the decision` |
| Regs s 20(3) | encoded | cdba-reg-appeals.l4 `how the person may challenge the decision` |
| Regs s 21(1) | encoded | cdba-reg-appeals.l4 `who decides the ground of appeal` |
| Regs s 21(2) | inert | A definition: "Court" means the Tax Court of Canada, for ss 21 and 23 to 29. It is used as the name in `Body that decides a ground of appeal` and decides nothing. |
| Regs s 22 | inert | A definition: "judge" has the meaning in s 2 of the Tax Court of Canada Act, for ss 23 to 27. A borrowed term with no use in a rule of these modules. |
| Regs s 23(1) to (4) | encoded | cdba-reg-appeals.l4 `the other person is added as a party to the appeal` covers (1) and (2) (the Minister's opinion is a conditional input). (3) and (4) are inert: the Registrar notifies the Chief Justice and others of the receipt of documents, and the Chief Justice appoints a judge; they are the Court's internal steps, which give the appellant nothing to do and no claim. |
| Regs s 24(1) | inert | The Registrar, in consultation with the judge, sets the date, time and place of the hearing. A power of the Court's officer with no condition the appellant can meet; what the appellant is owed by way of notice is s 24(3), and the place is s 24(2). |
| Regs s 24(2) | encoded | cdba-reg-appeals.l4 `where the hearing of a reference is held` |
| Regs s 24(3) | encoded | cdba-reg-appeals.l4 `the Registrar must notify the appellant by registered mail of the date, place and time` (a single condition) |
| Regs s 25(1) and (2) | inert | Proceedings before the Court are informal and summary, and the judge determines the procedure subject to every party's right to be heard. These describe how the Court runs a hearing; they set no condition that decides whether anything is owed to or by the appellant. |
| Regs s 26 | encoded | cdba-reg-appeals.l4 `the judge may require written submissions` (a single condition: the appellant's consent) |
| Regs s 27(1) and (2) | inert | The judge advises the Registrar of the decision, and the Registrar forwards a certified copy to the appellant, the Tribunal, the Minister and any added party. The Court's clerical steps after its decision; they decide nothing for the appellant. |
| Regs s 28 | encoded | cdba-reg-appeals.l4 `costs may be awarded or fees charged to the appellant on a reference` (always false) |
| Regs s 29 | encoded | cdba-reg-appeals.l4 `who decides the ground of appeal`, `the Social Security Tribunal must now proceed on the grounds not referred, under its Rules of Procedure` |
| Regs s 30 | inert | All notices, requests and other documents must be addressed to their recipient at the last known address. It says where a document is sent, not whether a right exists; the times in ss 18 and 19 run from being notified in writing, and what counts as notice is not defined, so there is no condition to encode. |
| Regs s 31 | encoded | cdba-reg-reviews.l4 `the Minister must take remedial action to put the person in the position they would be in` (the Minister is satisfied is a conditional input) |
| Regs s 32(1) | inert | The Minister may examine any document that relates to entitlement or the amount. A power of the Minister over documents with no condition and nothing for the person to do. |
| Regs s 32(2) | encoded | cdba-reg-compliance.l4 `the person is required to provide the information or document` |
| Regs s 32(3) | encoded | cdba-reg-compliance.l4 `the person is required to provide the information or document` (the judge authorization for anyone other than an applicant, a beneficiary or their representative) |
| Regs s 32(4) to (8) | encoded | cdba-reg-compliance.l4 `the last day to apply for a review of the authorization` covers 32(6). (4), (5), (7) and (8) are inert for a person with a disability applying for the benefit: they govern when a judge may authorize the Minister to require documents from someone else, and what a judge does on review; the definition of judge in (8) is used by no rule. |
| Regs s 33 | inert | A certified copy of a document examined or provided is evidence of its nature and content with the same probative force as the original. A rule of evidence in favour of whoever made the copy; it sets no condition on any benefit decision. |
| Regs s 34 | encoded | cdba-reg-compliance.l4 `the person is required to be at a suitable place or available at a suitable time` |
| Regs s 35(1) | encoded | cdba-reg-penalties.l4 `the person commits a violation` |
| Regs s 35(2) | encoded | cdba-reg-penalties.l4 `the Minister may impose a penalty` (the Minister's opinion is a conditional input) |
| Regs s 35(3) | encoded | cdba-reg-penalties.l4 `the penalty the Minister may issue` |
| Regs s 35(4) | encoded | cdba-reg-penalties.l4 `the violation is deemed to be a first violation` (fork F15) |
| Regs s 35(5) | encoded | cdba-reg-penalties.l4 `the person is protected from a penalty by a mistaken belief` |
| Regs s 35(6) | encoded | cdba-reg-penalties.l4 `the time for imposing a penalty has run out` (fork F15) |
| Regs s 35(7) | encoded | cdba-reg-penalties.l4 `the Minister may rescind the penalty` |
| Regs s 36(1) | encoded | cdba-reg-penalties.l4 `the person is guilty of an offence punishable on summary conviction` (the Regulations set no fine and no term of imprisonment) |
| Regs s 36(2) | encoded | cdba-reg-penalties.l4 `a proceeding may be commenced under section 36 or the Criminal Code for the act` |
| Regs s 37(1) | encoded | cdba-reg-debts.l4 `the amount that must be returned` |
| Regs s 37(2) | encoded | cdba-reg-debts.l4 `the day from which the erroneous payment or overpayment is a debt due to His Majesty` |
| Regs s 37(3) | encoded | cdba-reg-debts.l4 `the debt may be paid in instalments` |
| Regs s 37(4) | encoded | cdba-reg-debts.l4 `interest is payable on the amount owing` |
| Regs s 37(5) | encoded | cdba-reg-debts.l4 `interest is payable on the amount owing` |
| Regs s 38(1) | encoded | cdba-reg-debts.l4 `the day from which a penalty is a debt due to His Majesty` |
| Regs s 38(2) | encoded | cdba-reg-debts.l4 `interest accrues on the penalty debt` |
| Regs s 39(1) | encoded | cdba-reg-debts.l4 `the last day on which an action to recover money may be taken` (fork F16) |
| Regs s 39(2) | encoded | cdba-reg-debts.l4 `the last day on which an action to recover money may be taken` (the number of suspended days is an input) |
| Regs s 39(3) | encoded | cdba-reg-debts.l4 `the six-year limitation period applies` |
| Regs s 40(1) | encoded | cdba-reg-debts.l4 `the earliest day on which the unrecovered debt may be certified` |
| Regs s 40(2) to (5) | inert | On production to the Federal Court the certificate is registered and has the force of a judgment; it may be registered in a provincial superior court, its costs are recoverable, and it may be recorded as a charge on property. The legal effect of the Minister's certificate in court and the land registries; no fact the person can state decides it. |
| Regs s 40(6) and (7) | encoded | cdba-reg-debts.l4 `the Minister may require the money to be paid to the Receiver General`, `the unpaid amount is a debt due to His Majesty` |
| Regs s 41 (amendments) | repealed or blank in this text | The text shows only "41 [Amendments]": the section amends the Social Security Tribunal Regulations, 2022, and the amending text is not reproduced here. It also amends a different instrument. |
| Regs s 42 (coming into force) | encoded | cdba-reg-debts.l4 `the day the Regulations come into force` (15 May 2025, a value) |
| Related provision SOR/2026-123 s 14 | encoded | cdba-reg-eligibility.l4 `a supplemental amount is owed for the certificate` (a benefit paid before that section came into force is deemed an allocation; the day it came into force is not in the text, so whether a payment came before it is asked as a fact) |

## Fork register

Every place the text is ambiguous, silent or defers to something not among the inputs; the readings seen, the one taken and the text that licenses it.
Where I looked and found nothing: the lead-in of s 2(1) (cumulative or alternative: settled by "and" and "or" in the text, F3), the order of s 2(2) to (6) (F4), the three-way split in s 6 (settled by the text, tested in all three branches), the "despite" in s 11 against s 4(4) (F11), and the units of every threshold ($, months, days, years; F15, F16).

| # | the question | readings seen | the reading taken, and the text that licenses it |
|---|---|---|---|
| F1 | When in a month is a criterion in Regs s 2(1) tested? s 2(1) says "for any month ... in which they meet the following criteria" and does not say when in the month. | (A) the criterion holds throughout the month; (B) at some time in the month; (C) on the first day; (D) on the last day. | (A). Only (A) leaves both exceptions with work to do. Under (B) or (C) a person who turns 65 during the month is already eligible for it on the first day or on some day, so s 2(2) ("Despite paragraph (1)(a), a person is eligible ... for the month in which they turn 65") would be surplusage; under (C) or (D) a person incarcerated on a middle day is not incarcerated on the first or last day, so s 2(3) would be surplusage for that month. Licensed by s 2(2) and s 2(3), which exist only if (A) is the rule. The fields of `Person facts for a month` hold each fact as it stands throughout the month. |
| F2 | What is "not more than 65 years of age", and when is a birthday attained? | (A) exact elapsed age, so a person is over 65 from the day after the 65th birthday; (B) completed years, so a person is "65 years of age" until the day before the 66th birthday. A person born on 29 February: attains each age on 28 February or on 1 March in a year with no 29 February. | (A), and 28 February: on (B) s 2(2) again has nothing to do (a person would be "65 years of age" for a whole year, not only in the month they turn 65). Calendar-month arithmetic in `add years` clamps 29 February to 28 February; the text does not say. Licensed by s 2(2). |
| F3 | Are the conditions in s 2(1) cumulative or alternative? | cumulative / alternative | Cumulative for (a) to (e): the lead-in says "meet the following criteria" and "and" ends the list at (d); alternative for (c)(i) to (v): "or" ends that list at (iv); the residence condition in (c) is cumulative with one of the five ("are resident in Canada ... and are (i) ... or (v)"). Settled by the words of s 2(1). |
| F4 | What happens when the exceptions overlap with the conditions? | s 2(4) and s 2(6) begin "Despite subsections (1) to (3)"; s 2(2) and s 2(3) begin "Despite paragraph (1)(a)" and "Despite paragraph (1)(d)". | The later "despite" wins: a person in the month they turn 65, or in a month of incarceration or release, is still subject to the spouse condition (s 2(4)) and to a suspension (s 2(6)). Settled by the words. `the person is eligible to receive an allocation for the month` says so. |
| F5 | s 2(3): "the first month in which they are incarcerated": the first ever, or the first month of each term of custody? | per term of custody; first ever | Per term of custody. A person released and later imprisoned again under a new qualifying sentence has a new first month; the text gives no reason to stop the exception after the first spell. `Custody under a sentence` holds one term; one record per term. |
| F6 | Terms the Regulations borrow from Acts that are not among the inputs: "cohabiting spouse or common-law partner" (Income Tax Act s 122.6), "DTC-eligible individual" (s 146.4(1)), "adjusted income" (s 122.6), "working income" paragraphs (a) and (b) (s 122.7(1)), "resident in Canada for the purposes of the Income Tax Act", "return of income", "Canadian citizen", "permanent resident", "temporary resident", "protected person" (Immigration and Refugee Protection Act), "Indian" (Indian Act), "disability" (Accessible Canada Act s 2), "judge" (Tax Court of Canada Act s 2), the Consumer Price Index figures. | invent a meaning / ask as a fact | Asked as facts (or, for figures, inputs); no meaning is written in. Settled by the defaults for Commons. |
| F7 | s 2(4) when the person has no cohabiting spouse or common-law partner: the text says eligibility is "only if their cohabiting spouse or common-law partner has filed a return"; with no partner there is nobody who could have filed. | the condition fails (no partner, no return); the condition has nothing to bite on | The condition has nothing to bite on. s 2(5)(b) and s 6(2) both treat "does not have a cohabiting spouse" as an ordinary case, and a reading under which every single person is ineligible would make s 6(2) (the single beneficiary's reduction) empty. Licensed by s 6(2). The spouse facts are taken as at the last day of the month before (the day s 6(1) uses). |
| F8 | "the last taxation year that ended before the beginning of the payment period" (s 2(1)(e), s 6): which year is that? | the calendar year (an individual's taxation year under the Income Tax Act); the Act is not among the inputs | The calendar year before the one in which the payment period begins: the period beginning on 1 July 2025 has 2024. Stated once in cdba-reg-definitions.l4 `the calendar year taken to be the last taxation year that ended before the payment period that includes the day began`. The Regulations do not say this; it is assumed. |
| F9 | s 6(1): the formula ((2,400 x A) - B) / 12 goes below zero when B passes 2,400 x A, and the text does not say what is payable then. | report the negative amount as the amount payable; nothing is payable | The formula value is reported as it stands (`the basic amount worked out by the formula`) and the amount payable is the greater of it and zero (`the basic amount payable`). A benefit is paid to a person; no provision of the Regulations takes money back from a beneficiary because of income (the only recoveries are s 37 payments not entitled to). Assumed, not stated. |
| F10 | s 8(2): when is "the allocation payable in a month" twenty dollars or less, and how many months are "remaining"? | a payable amount of zero counts as 20 dollars or less (a lump sum of 0); only an amount above zero counts. "Remaining" counts the first payable month or only the months after it. | Only an amount above zero and not above 20 engages s 8(2): if nothing is payable there is no allocation payable and no lump sum. "Months remaining" counts the first payable month and every later month up to June. Both assumed; the text states neither. |
| F11 | s 4(4) says an allocation ceases when a beneficiary "becomes ineligible"; s 2(6) makes a person ineligible in a month in which payment is suspended under s 11; s 11(3) says an allocation is "deemed to have ceased" only if no request to resume is received within 24 months. | s 4(4) applies to a month of ineligibility caused by a suspension; it does not | It does not: the specific rule in s 11 governs a suspension at the beneficiary's own request, so s 4(4)'s cessation is read to leave out a month that is ineligible only because of s 2(6). Otherwise s 11(3) to (5) (resumption without a new application) could never operate. Assumed. |
| F12 | s 2(6): "any month during which payment of the allocation has been suspended under section 11": is a month in which the suspension took effect on some day, but not on the first, such a month? | (A) yes, any day of suspension is enough; (B) only if payment was suspended throughout the month, that is the suspension had taken effect by the first day. | (B). s 11(2)(a) makes the default day of suspension the last day of the month in which the request is processed. That choice does work only if a suspension taking effect on the last day leaves that month payable; under (A) the month the request is processed in would be voided, and the "last day" would be pointless. (B) also matches F1, which reads every other criterion in s 2 as speaking of the whole month. Under (A) the rule would read "took effect on or before the last day of the month" and two test expectations flip. |
| F13 | s 5(1): "the earliest day on which an applicant becomes eligible for a benefit": eligibility is month by month (s 2(1)), so which day? | the first day of the earliest eligible month; some other day in it | The first day of the earliest month for which the applicant met the criteria of section 2 and for which no benefit has been paid. Layer 1 takes the day as an input (`the earliest day on which the applicant becomes eligible for a benefit and for which no benefit has been paid`); the seat builds it from a month. Because s 7 then moves entitlement to the month after the month of approval, the choice of day within the month does not change which month is first. |
| F14 | s 4(3): "within six months before the day on which the applicant turns 18": which days? | the period from the day six months before the birthday to the day before it, both ends included; or one day shorter | Both ends included. `add months` clamps to a month end (a 31 August birthday has 28 or 29 February as its six-months-before day). |
| F15 | How are periods in the text counted: "the 10 years preceding the day on which a violation occurred" (s 35(4)), "five years have passed since the day on which the Minister became aware" (s 35(6)(b)), "within 24 months after the date of suspension" (s 11(3)), "within 180 days after the day on which the person is notified" (s 18), "not later than 185 days after the end of that period" (s 19(1)), "within six months before the day on which the applicant turns 18" (s 4(3)), "the day that is 24 months before the day on which the application is made" (s 5(2)). | (A) the anniversary day is inside the period; (B) the anniversary day is outside it. | (A) for the calendar-unit periods: a penalty imposed exactly ten years before counts; a penalty may still be imposed on the fifth anniversary of the day the Minister became aware and is barred from the day after; a request to resume is in time on the same date two years on. Day counts ("180 days after the day") start with the day after: notified on 1 January 2026, the 180 days end on 30 June 2026. Month and year arithmetic uses `add months` and `add years`, which clamp 29 February to 28 February (checked in cdba-tests-calendar and in each module's tests). The text gives no counting rule; the Interpretation Act is not among the inputs. Assumed, not stated. |
| F16 | s 39(1): "the six-year limitation period ... that begins on the day on which the money becomes due and payable": on which day does it end? | (A) it ends on the day before the sixth anniversary (the beginning day is its first day); (B) it ends on the sixth anniversary. | (A): the period "begins on the day", so that day is counted, and the last day on which an action may be taken is the day before the sixth anniversary (due on 1 January 2026, last day 31 December 2031). A suspension under s 39(2) adds its days. This differs from F15 on purpose: F15 reads "within N after the date" as including the date at the end, while s 39 says on which day the period begins. Assumed, not stated; a due day of 29 February 2028 gives 28 February 2034. |


## What the text turns out to say

Numbered findings; each ends "Asserted." where a case in a test file or in `cdba-cases-seat.l4` asserts it.

1. **The Act fixes no number, date or rate.**
   Act s 4 makes a person eligible if they meet the criteria "set out in the regulations", s 5 says the Minister pays "in accordance with the regulations", and s 11 is the power to make them.
   Every figure comes from the Regulations: $2,400, $23,000, $32,500, $14,000 and $10,000 (indexed by A), the rates 20% and 10%, the supplemental amount $150, the $20 threshold, 24 months, 180 and 185 days, 15% and 50%, six years.
   Each rule in `cdba-act.l4` says so in its comment, and calls the Regulations' rules for the criteria.
   Asserted.

2. **The text shows neither the date of royal assent nor the day the Act came into force.**
   Act s 14 says only that the Act comes into force on a day fixed by order of the Governor in Council, no later than the first anniversary of the day it received royal assent.
   The deposited Act has no date in square brackets under its title and no assent date elsewhere.
   Both days are therefore stated inputs (`the day the Act received royal assent`, `the day fixed by order of the Governor in Council`), and the rule checks the second against the first plus one year (29 February clamps to 28 February).
   The Regulations' own commencement is stated (s 42: 15 May 2025) and is carried as a value.
   Asserted.

3. **The Regulations are in force from 15 May 2025 but no month before June 2025 can be paid.**
   Section 2(1) makes a person eligible "for any month after May 2025", so May 2025 is not an eligible month for anyone, and the first possible month is June 2025.
   Asserted.

4. **The month in which a person first qualifies is never itself paid.**
   Section 5(1) deems an application approved on the earliest day on which the applicant becomes eligible and for which nothing has been paid.
   Eligibility is month by month, so that day is in the earliest eligible month (fork F13).
   Section 7 starts entitlement with "the month following the month in which a beneficiary's application is approved", and s 9 sums from "the month following the month in which their application is approved".
   So a person eligible from June 2025 who applies in September 2025 is entitled from July 2025, and June 2025 is not paid.
   The text may not mean this; it is what the words say.
   Asserted.

5. **There is no indexing factor for the payment period that began on 1 July 2024.**
   Section 6(5) takes CPImax over "any calendar year beginning with 2024 and ending with the last calendar year that ended before the beginning of the payment period"; for the period beginning on 1 July 2024 that range ends in 2023 and is empty.
   June 2025, the first month s 2(1) allows, is in that period.
   The gap never reaches an allocation, because of finding 4: the first month a beneficiary is entitled to is July 2025 at the earliest, in the period that began on 1 July 2025, where CPImax = CPI2024 and A = 1.
   It can reach s 35(3), whose penalty is worked out from the basic amount "during the payment period in which the violation was committed": a violation committed between 15 May and 30 June 2025 has no basis.
   The rule returns NOTHING for such a period and every caller passes it on; the seat asks for the 2024, 2025 and 2026 indices only, so a month from July 2028 on is also not covered.
   Asserted.

6. **The basic amount has no floor at zero.**
   Section 6(1) floors the reduction B at zero (each of ss 6(2) to (4) says "the greater of zero and ...") but not the result ((2,400 x A) - B) / 12.
   For a single beneficiary the result goes below zero once C - D exceeds 35,000 x A (adjusted income less capped working income): with C = 100,000 and no working income the formula gives -1,083.33.
   The text does not say what is payable then (fork F9); `the basic amount payable` is the greater of the formula and zero, and `the basic amount worked out by the formula` shows the formula as it stands.
   Asserted.

7. **A suspension the beneficiary asks for does not void the month in which it takes effect.**
   Section 2(6) makes a person ineligible "for any month during which payment of the allocation has been suspended under section 11", and s 11(2) suspends payment on the later of the last day of the month in which the request is processed and the day the request names.
   On the reading "any day of suspension is enough" the month in which the request is processed would always be lost and s 11(2)(a) would pick a day that does nothing; read as "suspended throughout the month" (fork F12), that month is still paid and the suspension bites from the next one.
   Asserted.

8. **Becoming ineligible only because of a requested suspension does not end the allocation.**
   Section 4(4) says the allocation "ceases as of that month" and a new application is needed when a beneficiary becomes ineligible; s 11(3) to (5) let the beneficiary resume within 24 months without a new application, and s 11(3) says the allocation is deemed to have ceased only after 24 months pass without a request.
   If s 2(6)'s ineligibility triggered s 4(4), s 11(3) to (5) could never operate (fork F11).
   Failing a criterion of s 2 while also suspended does trigger s 4(4).
   Asserted.

9. **A parole that is revoked is not a release.**
   The definition of "release" in s 1 counts release "on parole or statutory release that has not been terminated or revoked", so a person whose parole is revoked has no release, keeps the status of a person in custody, and has no "month of release" under s 2(3).
   One `Custody under a sentence` record holds one release (a later release at the expiry of the sentence needs a new record or answer).
   Asserted.

10. **The spouse or partner condition overrides the exceptions, and a person with no partner is not caught by it.**
    Section 2(4) begins "Despite subsections (1) to (3)", so the person who turns 65 in the month or is released in the month still needs the partner's return.
    The condition says eligibility is "only if their cohabiting spouse or common-law partner has filed", which, taken literally, no single person can meet; s 2(5)(b) and s 6(2) both treat a person with no partner as ordinary, so the condition is read to have nothing to bite on (fork F7).
    The three circumstances in s 2(5) are examples ("including if"), not the only grounds for a waiver, and the waiver is the Minister's judgment ("if the Minister is satisfied"), a conditional input.
    Asserted.

11. **The age edges.**
    A person is 18 for the whole of a month if the 18th birthday falls on or before the first day of it, and not more than 65 throughout it if the 65th birthday falls on or after the last day of it (fork F2).
    Section 2(2) then covers the month in which the 65th birthday falls whatever its day, and the month after is out.
    Asserted.

12. **Within a payment period only the household facts change from month to month.**
    Section 6(1) measures B "on the last day of the month that precedes the applicable month", but C, D, E and F are figures for "the last taxation year that ended before the beginning of the payment period".
    So whether there is a cohabiting spouse or common-law partner, whether they are also a beneficiary and whether the Minister waived s 2(4) are read as at the last day of the month before; the income figures are fixed for the period (fork F8 fixes which year).
    Asserted.

13. **Section 8(2) assumes one basic amount for the rest of the payment period, but s 6(1) can change it monthly.**
    The lump sum is "the basic amount multiplied by the number of months remaining in that period", payable "on the day on which the first payment of an allocation would have been made".
    The text does not say which month's amount is "the basic amount" if household facts change during the period, nor which day that is; the rule takes the caller's one basic amount, counts the first payable month and every later month to June (fork F10), and does not model the day.
    Asserted for the multiplication and the thresholds ($20.00 and $0.01 engage the rule, $20.01 and zero do not).

14. **The first payment can be undefined.**
    Section 9 sums the amounts "for the period beginning with the month following the month in which their application is approved and ending with the month in which the first payment is made".
    A first payment made in the month of approval or before it makes the period empty or backwards, and the text says nothing, so the rule returns NOTHING; so it does for a list of monthly amounts whose length differs from the number of months in the period.
    Asserted.

15. **A request to resume payment is in time up to the same date two years later.**
    Section 11(3) allows a request "within 24 months after the date of suspension"; a suspension on 31 August 2025 gives 31 August 2027, and on 29 February 2028 gives 28 February 2030 (fork F15).
    Asserted.

16. **Only three kinds of decision have a stated route, and the Regulations leave others without one.**
    Section 18 lets a person ask the Minister to reconsider a decision that no benefit be paid, a decision on the amount of a benefit, and a decision to impose a penalty; s 20(2) and (3) let only the Minister's decision on that request (s 18(4)) or on a request for more time (s 19(4)) be appealed to the Social Security Tribunal.
    For any other decision (a suspension under s 10, a refusal to waive s 2(4), a remedial decision under s 31, a requirement under ss 32 or 34) the text states no route; Act s 10.1(a) ("relating to the person's ineligibility") might reach some, but s 18 does not list them.
    The rule returns `the text states no route` for them rather than guess.
    Asserted.

17. **The income ground of an appeal leaves the Tribunal.**
    Under s 21 a ground that the Minister's decision or determination "as to income" was incorrectly made is referred to the Tax Court of Canada, and under s 29 the Tribunal proceeds on the other grounds only on receiving the Court's certified decision.
    A reference is heard where the appellant ordinarily lives unless they consent in writing to another place or to audioconference or videoconference (s 24(2)); written submissions need their consent (s 26); there are no costs or fees (s 28).
    Asserted.

18. **A penalty does not depend on the violator's income.**
    Section 35(3) takes "the basic amount payable ... calculated in accordance with section 6 without any reduction based on income", multiplied by 12: 15% for a first violation and 50% for each later one.
    The basic amount is rounded to the cent by s 6(1) before it is multiplied by 12: indices of 99 and 100 give 202.02, then 2,424.24, then 363.636 for the 15% penalty.
    Asserted.

19. **Time limits on a penalty run from different events.**
    The Minister cannot impose a penalty once a prosecution for the act has been started or five years have passed since the Minister became aware of it (s 35(6)); s 36(2) is the converse, that no proceeding may be commenced under s 36 or the Criminal Code for an act once a penalty for it has been imposed.
    A mistaken belief that a representation was true, or that the applicant was eligible, bars a penalty (s 35(5)).
    The ten-year look-back for "first violation" (s 35(4)) is the ten years ending the day before the violation (fork F15).
    Asserted.

20. **The Regulations create the offences but set no punishment.**
    Section 36(1) says a person is guilty of an offence "punishable on summary conviction" if they do one of three things and sets no fine and no term of imprisonment; the rule answers whether the person is guilty, not what follows.
    Asserted for the yes or no.

21. **Interest is only half-stated.**
    Section 37(4) says no interest is payable on an erroneous payment or overpayment; s 37(5) makes an exception for a payment made because of a penalised violation or a sentenced offence, during any period in which a reconsideration, judicial review or appeal can be made or is pending.
    Read literally, s 37(5) says subsection (4) applies only during those periods, so interest is payable outside them, and no section sets a rate.
    Section 38(2) says only that interest on a penalty debt "does not accrue" during such a period; no section says that it accrues at other times, or at what rate.
    The rules answer yes or no and carry no rate.
    Asserted.

22. **The six-year limit ends the day before the sixth anniversary of the due day, and suspensions add their days.**
    Section 39(1) says the limitation period "begins on the day on which the money becomes due and payable"; a due day of 1 January 2026 gives 31 December 2031 (fork F16), and 30 days of suspension under s 39(2) move that to 30 January 2032.
    Section 39(3) takes the execution, renewal or enforcement of a judgment out of the limit.
    Asserted.

23. **Certification of a debt.**
    Section 40(1) lets the Minister certify "without delay" if the debtor is attempting to avoid payment (the Minister's opinion, a conditional input) and otherwise "30 days after the day on which the default occurred"; "default" is not defined, so the day of default is an input.
    Asserted.

24. **Related provision SOR/2026-123 s 14 widens the supplemental amount.**
    For s 2.1(1), any benefit paid before the day s 14 of SOR/2026-123 comes into force is deemed to be an allocation.
    The deposited Regulations print that provision but not the day it comes into force, so whether a payment was made before that day is a stated input.
    A payment to which the person was not entitled is not considered (s 2.1(2)).
    The supplemental amount is $150 for each certificate, paid as a lump sum (s 6.1, s 9.1); the text does not say when.
    Asserted.

25. **Every place the text hands a judgment to the Minister is a conditional input.**
    These are s 2(5) (waiver, "satisfied"), s 10(1) ("reasonable grounds to believe", "satisfied that they are eligible"), s 10(2) ("reasonable time"), s 11(4) ("satisfied"), s 14(1) to (3), s 19(3) and (4), s 23(1) ("of the opinion"), s 31 ("satisfied"), s 35(2) and (7), s 40(1)(a) and s 40(6) ("knows or suspects").
    None is guessed; each rule says "if the Minister is satisfied ..." as a yes/no input and the seat asks the question in the person's words.
    Asserted.

26. **Death and representatives.**
    Section 12 puts a duty to notify "as soon as feasible" on the executor, administrator, liquidator or heirs, and sets no day; s 13(1) lets the estate or heirs claim the allocation payment for the month of death only if the beneficiary did not receive it; s 13(2) pays an amount owing to the estate or heirs, or to a person or agency the Minister designates if there are no heirs.
    "Representative" is not defined in the Regulations (s 15 and s 16 speak of a person "incapable of managing their own affairs"), so who is a representative is asked as a fact.
    Asserted.


## What the stable binary does not accept

Where the skills describe a construct the stable binary (l4 1.6.98, dialect `main`) rejects, the binary governs.
Each of these was tried on the binary while writing this encoding and is a diagnostic, not a guess:

- `REFUSE` and `#ASSERT REFUSED` are rejected (check error).
  "Not covered" is a constructor or `NOTHING`, and is asserted.
- `TYPICALLY` on a record field is rejected (check error).
- A bodiless `DECLARE Thing` (an opaque type) is a parse error, reported at the token after it.
- A section-level `GIVEN` under a `§` heading is a parse error (`unexpected §` at the next `§§`); every `GIVEN` here belongs to a rule.
- There is no lambda: `\x -> ...` is a lexer error on `\`.
  Helper functions are named in a `WHERE`.
- `YMD` is not in the prelude (check error); `cdba-calendar.l4` defines it once as `YMD y m d MEANS Date d m y`.
- There is no `add days` (the name is not found); days are added with `PLUS` and subtracted with `MINUS`, and `Date MINUS Date` is a number of days.

Behaviours that are not rejections but matter to the dates (checked on the binary, and asserted in `cdba-tests-calendar.l4` and the module tests):

- `Date d m y` is lenient: `Date 31 2 2025` is 3 March 2025.
- `add months` and `add years` clamp to the end of the month: 31 August plus 6 months is 28 February; 29 February 2028 plus 1 year is 28 February 2029.

Other limits met: a name defined in two imported modules cannot be used, so every layer-1 rule name is distinct from the prelude and `daydate` names (for example `the later of`, which `daydate` defines, is `the later day of` here); the test files build their own records because the layer-1 modules export rules, not builders.


## What check.sh prints

Run as `L4=l4 L4_TARGET=unstable ./check.sh` from this folder; `SRC_DIR` defaults to the run's `inputs` folder and must be set to the folder holding the two source texts if the folder is moved.
It prints, per module: errors, warnings, assertions satisfied, failed, refused, expected-failed and written, then the srcrefs line for the Act files and for the Regulations files.
It fails if any module has an error, a warning or a refused assertion, or if the assertions written differ from the assertions reported.
No test is meant to fail: `expected_failed` is empty.
The output of the last run was:

```
check.sh: L4=l4  L4_TARGET=unstable  SRC_DIR=../../registers/source-bundle
module                                    errors  warnings satisfied  failed  refused  expected  written
cdba-act.l4                                    0         0         0       0        0         0        0
cdba-calendar.l4                               0         0         0       0        0         0        0
cdba-cases-seat.l4                             0         0       297       0        0         0      297
cdba-nouns.l4                                  0         0         0       0        0         0        0
cdba-reg-amount.l4                             0         0         0       0        0         0        0
cdba-reg-appeals.l4                            0         0         0       0        0         0        0
cdba-reg-application.l4                        0         0         0       0        0         0        0
cdba-reg-compliance.l4                         0         0         0       0        0         0        0
cdba-reg-death.l4                              0         0         0       0        0         0        0
cdba-reg-debts.l4                              0         0         0       0        0         0        0
cdba-reg-definitions.l4                        0         0         0       0        0         0        0
cdba-reg-eligibility.l4                        0         0         0       0        0         0        0
cdba-reg-payment.l4                            0         0         0       0        0         0        0
cdba-reg-penalties.l4                          0         0         0       0        0         0        0
cdba-reg-reviews.l4                            0         0         0       0        0         0        0
cdba-reg-suspension.l4                         0         0         0       0        0         0        0
cdba-seat.l4                                   0         0         0       0        0         0        0
cdba-tests-act.l4                              0         0        39       0        0         0       39
cdba-tests-calendar.l4                         0         0        20       0        0         0       20
cdba-tests-reg-amount.l4                       0         0        73       0        0         0       73
cdba-tests-reg-appeals.l4                      0         0        21       0        0         0       21
cdba-tests-reg-application.l4                  0         0        24       0        0         0       24
cdba-tests-reg-compliance.l4                   0         0        15       0        0         0       15
cdba-tests-reg-death.l4                        0         0        26       0        0         0       26
cdba-tests-reg-debts.l4                        0         0        32       0        0         0       32
cdba-tests-reg-definitions.l4                  0         0        22       0        0         0       22
cdba-tests-reg-eligibility.l4                  0         0       108       0        0         0      108
cdba-tests-reg-payment.l4                      0         0        35       0        0         0       35
cdba-tests-reg-penalties.l4                    0         0        43       0        0         0       43
cdba-tests-reg-reviews.l4                      0         0        47       0        0         0       47
cdba-tests-reg-suspension.l4                   0         0        38       0        0         0       38
TOTAL (31 modules)                             0         0       840       0        0                840
(a failed assertion is also an error; any other error or warning, any refused assertion, or any written assertion that was not reported, makes the run red)
srcrefs (Act files):         srcrefs check: 26 src: lines, 8 runs, 10 locators, 0 problems
srcrefs (Regulations files): srcrefs check: 207 src: lines, 87 runs, 112 locators, 0 problems
```


## What would need doing before this encoding is worth relying on

1. A domain expert (a lawyer who knows the benefit) must read it against the official English and French texts; every statement here is about the deposited renderings, current to 2026-09-30.
2. The forks that move answers need a ruling, above all F1 (when in the month a criterion is tested), F7 (a person with no partner), F9 (a negative formula), F12 (a suspension that takes effect mid-month), F13 and findings 4 and 5 (the first month is never paid; no index for the period beginning 1 July 2024).
3. The inputs the text does not give must come from somewhere: the date of royal assent and the order bringing the Act into force; the day SOR/2026-123 s 14 comes into force; the published Consumer Price Index figures; the form and manner of an application and of a request for more time.
4. The borrowed terms (cohabiting spouse, DTC-eligible, adjusted income, working income, the five kinds of person) are facts the user states; nothing checks them against the Income Tax Act or the Immigration and Refugee Protection Act.
5. Amendments after 2026-09-30 are not in the text; SOR/2026-123 is only partly deposited (one related provision), so the rest of that instrument is not encoded.
6. Independent tests: the expected values were written by the agent that wrote the rules, from the text and before running; a second reader should re-derive a sample.
7. The seat asks the Consumer Price Index for 2024 to 2026 only; later years need the question widened.

## Where the source does not answer

The date of royal assent and of commencement of the Act; the commencement of SOR/2026-123 s 14; the form and manner of an application (s 4(1)) and of an extension request (s 19(2)); how long a "reasonable time" is (ss 10(2), 18(4), 19(4), 32(2)) and what is "suitable" (s 34); the day of payment of a lump sum (s 8(2)) and of a first payment (s 9) and of the supplemental amount (s 9.1); the rate of interest and whether it accrues outside the periods s 37(5) and s 38(2) name; the fine or imprisonment for an offence (s 36); which month's basic amount is used in s 8(2) when it changes during a period; what an "undue hardship" instalment is (s 37(3)); who is a "representative" (ss 15, 16); what a "default" is (s 40(1)(b)); the route for a decision that is not one of the three kinds in s 18; whether a taxation year is the calendar year (F8).
In each case the rule takes an input or returns an explicit "not covered" value; none is guessed.
