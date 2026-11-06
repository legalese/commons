# Emergency Services Levy Act 2002 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `esl-levy.l4`: the module. It covers the Act's one operative section and the Part 6A rules of the Fire and Emergency Services Act 1998 that the land owner meets: whether the land is leviable, who is liable, how the amount is worked out, the notice, the due date, interest, buying and selling, sale and caveat for unpaid levy, and objections.
- `esl-cases-levy.l4`: the worked cases, built by the scratchpad generator `gen_wa_emergency-services-levy-act-2002_baseline.py`.

Conventions: a levy year is a financial year, named by the calendar year in which it ends (2029/30 is 2030); a day is the number YYYYMMDD.

## The split: what this Act does, and where the levy really lives

The Emergency Services Levy Act 2002 has three sections: short title, commencement, and s 3:

> "The emergency services levy determined under Part 6A of the Fire and Emergency Services Act 1998 is imposed."

That is all it does. It fixes no rate, no amount, no payer, no due date. It exists so that the levy is imposed as a tax by an Act that does nothing else. (Labelled INFERENCE: the reason for the separate Act is not stated in the deposit. The long title says only "An Act to impose the emergency services levy".)

Everything the owner meets is elsewhere:

| What | Where | In this encoding |
|---|---|---|
| The levy imposed | ESL Act s 3 | encoded (`Does the Emergency Services Levy Act itself fix how much levy I pay`: FALSE) |
| Which land, who is liable, how worked out, notice, due date, interest, recovery, sale, objection | Fire and Emergency Services Act 1998 Part 6A (ss 36B–36ZH), with ss 3 and 3A | **brought in**: deposited at `subjects/au/wa/fire-and-emergency-services-act-1998`, which has no encoding of its own |
| The rate in the dollar, the minimum and maximum, for each ESL category and purpose of use, each year | the Minister's Gazette determination under FES Act ss 36G–36I | **inputs**: indexed as `wa/emergency-services-levy-annual-determination`, text not deposited |
| The gross rental value | Valuation of Land Act 1978 (borrowed term) | a fact |
| Pensioner and senior rebates and deferments | Rates and Charges (Rebates and Deferments) Act 1992 | not encoded; asked as a fact where Part 6A defers to it |

So this baseline is, in substance, a baseline of FES Act Part 6A from the owner's seat, filed under the Act that imposes the levy, because that is where the life cites it.

## Edition

- **The Act.** The compilation of the Emergency Services Levy Act 2002 (No. 39 of 2002) deposited at `../../registers/source-bundle/mrdoc_24246.txt` (legislation.wa.gov.au mrdoc 24246, retrieved 2026-09-07). Its compilation table ends with the Fire and Emergency Services Legislation Amendment Act 2012 (No. 22 of 2012), which amended the long title and s 3.
- **Part 6A.** The Fire and Emergency Services Act 1998 (No. 41 of 1998) deposited at `subjects/au/wa/fire-and-emergency-services-act-1998/registers/source-bundle/mrdoc_49451.txt` (mrdoc 49451, retrieved 2026-09-07).
- **Not deposited.** The annual Gazette determination (rates, minimum, maximum, by ESL category area and purpose of use), the regulations that prescribe ESL categories (s 36F(1)) and exemptions (s 36D), and the Gazette interest rates (s 36S(2)). All are inputs or facts. The figures used in the cases (1.2 cents in the dollar, minimum $90, maximum $450, gross rental value $25,000) are **illustrative**, not the real determination.

## Checks

One case file: **39 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run esl-levy.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with two expected values altered (300 to 301, 20290531 to 20290530) was run. The runner reported both failures.

## Seat

**The land owner.** The life asks "What emergency services levy is charged on my home?", and Part 6A makes "the owner of leviable land" the person liable (s 36P(1)).

The Minister determines, the local government assesses and serves, the FES Commissioner recovers, applies for sale and lodges caveats. Those powers appear only as what they mean for the owner: is my land levied, am I liable, how much, how the notice comes, by when, what follows non-payment, and how to object.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed, with the necessary extension. The Act sets nothing; the instrument that does is Part 6A of the FES Act, which is deposited and brought in. The annual determination is not deposited, so its numbers are inputs.
- **The actors the text names.** Followed: the owner, joint owners, the local government, the FES Commissioner, the Minister, the Supreme Court, the State Administrative Tribunal.
- **A judgment handed to someone else is answered conditionally.** Followed. The Minister's determination (including any "other basis" under s 36H(3)), the declaration of ESL category areas, an extension of time to object, and the Supreme Court's order for sale are all inputs or conditions ("an application may be made", not "the land will be sold").
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed. Worked out: leviable land (s 3, ss 36B, 36D, 36E), owner (s 3A(a)(i), (d)), the levy year and its dates. Asked as facts: gross rental value (Valuation of Land Act 1978), whether land is in an ESL category area, whether the regulations exempt it, entitlement to a rebate or deferment under the 1992 Act.
- **One case is the text's natural unit.** Followed: one parcel of land for one levy year.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Left out: local government estimates and accounts (ss 36A, 36U–36Y), records (s 36C), the Minister's method (s 36G(3)–(5)), State land arrangements (ss 36L(1)(a), 36N), ESL agreements (Division 9), and the rest of the FES Act.

**Departures:**

- Dates are YYYYMMDD numbers and years are numbers, so that the tests are simple comparisons.
- Only owners under s 3A(a)(i) (Crown lessees) and (d) (Torrens proprietors, mortgagees in possession) are modelled; Crown land vested in or controlled by a body, the State, deeds-registered land and mining or petroleum holders are not.
- Partial exemption by regulation (s 36D(a)) is not modelled: only whole exemption.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c055** (2029-07-15), handover of the new Byford house: "council rates; the emergency services levy" | `Is my land leviable`, `Am I liable to pay the levy`, `How much levy is charged on my land`, `How will my levy notice come to me`, `Can I be made to pay all of the levy on land I own with others`, `What part of the year's levy is apportioned to me` | Leviable if Byford is in a declared ESL category area (assumed; the category is in the undeposited determination). Chloe and Liam, registered proprietors as joint tenants, are liable, each for the whole. For 2029/30 the levy is the rate in the dollar of the gross rental value in force at 1 July 2029, held between the minimum and maximum: at the illustrative figures, $300. It comes on the Shire's 2029/30 rate notice, payable to the Shire, not earlier than 35 days after issue. For the 2027/28 year in which the land settled (15 May 2028), the levy is apportioned day by day: 46 of 366 days. |

## Why this scope

The scope is what the event asks — who levies what on a new house, and how much — plus what any home owner meets afterwards: the notice and due date, instalments, interest, buying and selling land with levy outstanding, what can be done to land if the levy goes unpaid, and how to object.

Left out, because no owner in the lives meets them: local government finance, ESL agreements, State land, and the fees for emergency services and volunteer firefighter compensation elsewhere in the FES Act.

## What the Act turns out to say

1. **The Act does one thing: it imposes the levy.** s 3 imposes "the emergency services levy determined under Part 6A of the Fire and Emergency Services Act 1998". No rate, payer or date is in it. Asserted.
2. **The life cites sections that do not exist.** Chloe's facts cite the ESL Act "ss 5-7"; the Act has only ss 1–3. The index entry for the annual determination says the levy is imposed by "s 4"; it is s 3. Both citations should be corrected to ESL Act s 3 and FES Act Part 6A.
3. **The levy is on land, not on the house, and on all land in an ESL category area** (s 36B), unless the regulations exempt that kind of land (s 36D). Land outside every declared area pays nothing. Asserted.
4. **A general exemption in another law does not help.** An earlier Act exempting from "any rate, tax or imposition" never frees the owner; a later Act frees the owner only if it "expressly exempts a person from liability to pay the levy" (s 36E). Asserted.
5. **The owner pays, not the tenant, and not a lender out of possession.** s 3A(d): the Torrens proprietor, "except a mortgagee who is not a mortgagee in possession". A tenant of freehold land is not an owner (INFERENCE from the text). Asserted.
6. **Joint owners are each liable for the whole** (s 36P(3)), and a notice served on one is served on all (s 36J(3)). Chloe and Liam, as joint tenants, are each liable for all of it. Asserted.
7. **The amount is a rate in the dollar of the gross rental value at 1 July of the levy year** (s 36H(1)), raised to any minimum and cut to any maximum the Minister determines (s 36I), which apply "despite any other provision of this Part", so even to a levy set on "another basis" under s 36H(3). The rate may differ by ESL category area and by purpose of use (s 36G(4)). Asserted with illustrative figures.
8. **The rates must be gazetted before 31 May for the next levy year**, unless the Minister declares another day (s 36G(1)–(2)). A change in an area's category cannot take effect in the levy year its notice is published (s 36F(3)). Asserted.
9. **The levy arrives with the council rates.** The local government assesses it and serves notice "as part of the rate notice", or separately if no rate notice is given (s 36J(4)); it is paid to whoever served the notice (s 36P(2)). Asserted.
10. **It cannot fall due earlier than 35 days after the notice's issue date** (s 36M(2)), is payable in one payment unless instalments are approved or a payment agreement is made with the council (ss 36Q, 36R(2)), and interest runs from the due date unless the owner is entitled to a rebate or deferment under the 1992 Act or is of a prescribed kind (s 36S). Asserted.
11. **Buying land: the levy follows the land.** It is a charge on the land (s 36O); it can be recovered from "a person who becomes the owner of the land while the levy is unpaid" (s 36Z(1)(b)); between successive owners it is apportioned day by day (s 36T(1)(a)), and an owner must reimburse anyone else who paid it unless they agreed otherwise (s 36T(2)). None of this changes whom the council can pursue (s 36T(3)). Asserted.
12. **Unpaid for 3 years, the land can be sold.** After 3 years unpaid the FES Commissioner may apply to the Supreme Court for sale, after at least 6 months' newspaper notice and notice to the owner if their whereabouts are known (s 36ZC). While any levy is unpaid a caveat can be lodged (s 36ZD). Asserted.
13. **The only objection Part 6A gives is to the purpose of use**, and only where the rate or the minimum or maximum depends on it (s 36ZE(1)). It goes to the Minister in writing within 60 days of service of the notice, extendable by the Minister; then to the State Administrative Tribunal (s 36ZF). The levy remains payable meanwhile; an overpayment is refunded and an underpayment cannot be pursued for 30 days after the adjustment notice (s 36ZH). Objections to the gross rental value itself go under the Valuation of Land Act 1978, not here. Asserted (except the last sentence, which is from s 36ZH(1)(a) and not asserted).

## What would need doing before this is worth anything

- Deposit the annual Gazette determinations (categories, rates, minimum and maximum by purpose of use) and bring in the real figures; the Gazette is outside the WA Legislation site's CC BY licence, so this needs a licensing decision.
- Deposit and encode the FES regulations on ESL categories (s 36F(1)) and exemptions (s 36D), and the Rates and Charges (Rebates and Deferments) Act 1992 for pensioners and seniors.
- Correct the citations in Chloe's facts (ESL Act "ss 5-7") and in the annual-determination index entry ("s 4") to ESL Act s 3 and FES Act Part 6A.
- An independent test pass, a coverage table of Part 6A, and a human gate.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026, after the graffiti encoding's design (Graffiti Vandalism Act 2016, `gva-seat.l4`, its NOTES D2,
D4 and D8). The layer is `esl-qa.l4` (imports `prelude` and `esl-levy`), with its cases in `esl-qa-cases.l4` (imports
`prelude`, `esl-levy` and `esl-qa`). The baseline's files are unchanged: no rule or export of `esl-levy.l4` was touched,
and its 39 cases still pass. The layer calls the baseline's functions and restates none.

**Why.** The site's question form asks only the inputs that can still change an open question. Every exported question
takes `my role` first ("Which of these describes you"); for the role it is not about, it answers `does not arise for
you` without reading any other input. Within a role, a question that arises only in a situation takes that situation's
fact second, and answers `does not arise for you` when it does not hold, again reading nothing else.

**Roles** (`Role`):

- `I own land in Western Australia`: the baseline's seat. "Owner" is the FES Act s 3A owner, so the role takes in a
  mortgagee in possession and a lessee or occupier of Crown land; the baseline's own "Am I an owner" question sorts them.
- `I rent or occupy land that someone else owns`: Part 6A puts no duty on a tenant of freehold land, who is not an
  owner (s 3A(d)), but gives a person who pays levy on land they do not own a right to be paid back by the owner
  (s 36T(2)); and a lessee or occupier of Crown land is an owner (s 3A(a)(i)), liable and open to recovery.

The Minister, the local government and the FES Commissioner are not seats. The buyer of land is not a separate role: the
baseline's owner seat already asks the buyer's questions (apportionment, s 36T(1)(a); recovery from a later owner,
s 36Z(1)(b); the charge on the land, s 36O), and a buyer is an owner once the land is theirs. A mortgagee not in
possession is not a role: the Act gives it nothing to ask beyond "am I an owner", which the owner's question answers.

**Situation inputs.** All are BOOLEAN; FALSE gives `does not arise for you`; each is the second input wherever it is
taken, with the same name, type and `@desc` in every question.

| Name | Role | Questions that take it |
|---|---|---|
| `I own the land with others` | owner | As a co-owner, can I be made to pay all of the levy on our land; Is a levy notice served on my co-owner taken to be served on me |
| `levy on my land has fallen due and is unpaid` | owner; tenant or occupier | Does interest run on the levy I have not paid; Can the unpaid levy on this land be recovered from me; Is the unpaid levy a charge on my land; Can my land be sold for unpaid levy; Can a caveat be lodged against my land for the unpaid levy; (tenant or occupier) Can the levy on the land I rent or occupy be recovered from me |
| `the land changed owners during the levy year` | owner | What part of the year's levy falls to me as a successive owner |
| `I have objected to my levy` | owner | Was my objection in time; May I apply to the State Administrative Tribunal for a review of the objection decision |
| `I have objected to my levy or my valuation` | owner | Must I still pay the levy while my objection is decided; How much is refunded to me when my levy is adjusted down; For how many days after an adjustment notice am I safe from recovery of an underpayment |
| `I have paid levy on land I do not own` | tenant or occupier | Must the owner pay me back the levy I paid |

The Act ties these rules to those facts: s 36P(3) and s 36J(3) to land "owned by 2 or more persons"; ss 36S, 36Z, 36O,
36ZC and 36ZD to levy unpaid after it falls due; s 36T(1)(a) to "successive owners"; ss 36ZE(2)(d), (3) and 36ZF to an
objection to the purpose of use, and s 36ZH to that objection or "an objection to the valuation of the land under the
Valuation of Land Act 1978" (s 36ZH(1)(a)), and to a review by the Tribunal (s 36ZH(2)); s 36T(2) to a part of the levy "paid by a person other than the owner".

**Decisions.**

1. **The situation replaces the baseline input it is.** The two co-owner questions and the caveat question took one
   input, which is now the situation, and the layer passes TRUE for it, so the question settles on the role and the
   situation alone. The baseline's answer for FALSE (no) becomes `does not arise for you`.
2. **Interest takes the unpaid situation.** "Does interest run" took `it is unpaid after its due date` first. That is
   the situation, so the layer passes TRUE for it and asks only the rebate and the prescribed-person inputs.
3. **s 36O, the charge, is in the unpaid situation.** It is fixed (yes) once levy is unpaid, so it reads nothing else.
   Before any levy is unpaid there is nothing for it to charge.
4. **The tenant's questions call the owner's functions.** "Am I liable for the levy on the land I rent or occupy" calls
   the baseline's s 36P(1) function with the interest the answer fixes (Crown lessee or occupier, or tenant of freehold
   land); "Can the levy ... be recovered from me" reads nothing else for a tenant of freehold land; "Must the owner pay
   me back" calls the baseline's s 36T(2) function with its first input TRUE.
5. **Answer types** carry `does not arise for you`: `Yes or no`, `Amount`, `Day answer` (a day written YYYYMMDD, as the
   baseline writes it), `Days answer`, and `Notice answer`, the baseline's three notice routes reworded to the second
   person, through a helper that lists every value with no OTHERWISE.
6. **Names.** Each question's name is a plain first-person question, different from every baseline function's name
   even after the site shortens names to their first 60 characters (letters and digits, the rest as hyphens), so the
   site never runs the baseline's function in the question's place. The first version broke this: "On which day is the
   gross rental value for my levy fixed" and "May I object to the purpose my land is taken to be used for" were the
   baseline's names exactly, and "Can I be made to pay all of the levy on land I own with others, as a co-owner" was
   the baseline's name with a tail past the 60th character; the site ran the baseline's function for the tenant, which
   answered yes or no instead of `does not arise for you`. They are now "Which day fixes the gross rental value for my
   levy", "Can I object to the purpose my land is taken to be used for" and "As a co-owner, can I be made to pay all of
   the levy on our land" (fixed 6 November 2026, after verification).
7. **The days in the levy year are a yes/no** (fixed 6 November 2026). The s 36T(1)(a) question asked the days in the
   levy year as a number, and the baseline divides by it; 0 failed with a division by zero. A levy year is "the
   financial year for which the levy is payable" (FES Act s 3), so it has 365 or 366 days: the layer asks `the levy
   year has 366 days` and passes 366 or 365 to the baseline's function.
8. **The s 36ZH questions take their own objection situation** (fixed 6 November 2026). s 36ZH(1) applies to "an
   objection to the valuation of the land under the Valuation of Land Act 1978" as well as to an objection under the
   Division, and s 36ZH(2) to a review by the Tribunal, so its three questions take `I have objected to my levy or my
   valuation`; the two questions only about the s 36ZE objection keep `I have objected to my levy`.
9. **The tenant's recovery question takes the unpaid-levy situation** (fixed 6 November 2026), as the owner's does:
   s 36Z(1) recovers levy that is payable and unpaid. Its description now says "the land", so it reads for both roles.

**Not covered for the tenant or occupier.** Whether a lease can make the tenant pay the levy (a question of the lease,
not the Act; s 36T(2)'s "agreement ... to the contrary" is asked as a fact); a Crown land occupier's other questions
(the amount, the notice, objection), which are the owner's questions, asked as the owner. The baseline's own gaps
stand.

**Checks.** 32 exported questions: 29 for the owner, 3 for the tenant or occupier. `esl-qa-cases.l4` has 183 assertions,
all satisfied: 32 asking each question for the role it is not about, every other input ASSUMEd; 15 asking each
situation question with FALSE and every later input ASSUMEd; for the owner 64 hand-worked cases, each also asserted
equal to the baseline export's answer on the same facts (64); for the tenant or occupier 8 hand-worked cases. 0 errors
and 0 warnings in all four files (`esl-levy.l4`; `esl-cases-levy.l4`, 39 satisfied; `esl-qa.l4`; `esl-qa-cases.l4`);
`l4 check esl-qa.l4` succeeds. A further script checked that no two exported names, of the layer or the baseline,
shorten to the same first 60 characters. A script listed every `@export` with its inputs and checked `my role` first everywhere,
the six situation inputs identical wherever they occur, each role branch reading its situation first, and no DEONTIC
or EVENT input. Negative control: a case reading an ASSUMEd input fails.
