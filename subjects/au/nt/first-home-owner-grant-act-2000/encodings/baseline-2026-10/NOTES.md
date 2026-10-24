# First Home Owner Grant Act 2000 (NT): baseline encoding for the first home buyer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit "not covered" value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers, after the pattern of `subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/`:

- **`fhog-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms ("an applicant", "the applicant's spouse or de facto partner", "the Commissioner", "a person on whose application a first home owner grant was paid"). Computations (commencement, completion, the threshold, the amount, the periods and deadlines, interest) are functions. Where the text says "must" or sets a deadline there is a regulative rule (`DEONTIC`): four in all (s 12(1)-(2), s 14(3), s 41(2)-(2A) with a branch for each trigger, s 41(3)(b)-(c) and (6)).
- **`fhog-seat.l4`**, the buyer's seat. It asks 21 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule.
- **`fhog-cases-applicant.l4`**, the case file, built by the scratchpad generator `gen_nt_fhog_cases.py` and edited by hand in the fix pass (see Corrections). The hand-worked expected value and its working are in the comment above each assertion.

No earlier encoding of this Act existed to keep. No requirement ledger covers the Northern Territory, so no ledger line is closed. No scenario life has been written for the NT; the buyers in the cases are the encoder's, hypothetical throughout.

## Edition

- **The Act:** reprint **REPF039**, as in force at **1 July 2026**, deposited at `../../registers/source-bundle/First-Home-Owner-Grant-Act-2000-NT-current-reprint-REPF039.txt` (retrieved 2026-10-19 from legislation.nt.gov.au; text sha256 `e60e1602…`). Its last amendment is the Treasury Legislation Amendment Act 2026 (No. 18 of 2026), in force 1 July 2026, which amended ss 12 and 18. The First Home Owner Grant Amendment Acts 2024 and 2025 (in force 1 October 2024 and 1 October 2025) made the $50,000 new-home amount and the 12-month residence period.
- **The Regulations:** reprint **REPF039R1**, as in force at **1 July 2009**, deposited at `../../../first-home-owner-grant-regulations-2000/registers/source-bundle/First-Home-Owner-Grant-Regulations-2000-NT-current-reprint-REPF039R1.txt` (retrieved 2026-10-19). Regulation 3 (non-conforming interests on farming land or a relative's land) and r 4 (persons who need not join in an application) are encoded. Regulations 5 and 6 are spent (finding 12).
- **The interest rate:** "statutory interest rate, see section 35 of the Taxation Administration Act 2007" (s 3). That Act's reprint is deposited at `../../../taxation-administration-act-2007/`; its s 35 is read for the 8% premium rate. The market interest rate is set by regulation or from RBA figures, neither deposited, so it is an input.

Dates are DATE values, compared by serial day number (the stable `l4` cannot compare two DATEs directly). No `daydate` import is needed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `fhog-core.l4`, `fhog-seat.l4` | `fhog-cases-applicant.l4` | 174 written, 174 satisfied |

Six `#TRACE`s carry an `-- expect:` line: five breaches by the applicant (late repayment, no notice, no payment after the Commissioner's notice, moving out without notifying, never moving in when not paid in anticipation) and one obligation still pending (s 14(3), which has no period). Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24, and again after the fix pass the same day). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. As a control, a copy of the case file with two expected values changed (Mia's grant to $49,999 and the interest to $1,234) was run: the runner reported both as `assertion failed`. In the fix pass, a copy expecting the old answer ("not covered") for the s 13AA(1)(a) building contract was run: the runner reported `assertion failed`. The six traces gave the same output before and after the fix.

Every expected value was written by hand from the text, with the working in the comment above the assertion.

## Seat

**The first home buyer applying for the grant, with their spouse or de facto partner.** They ask: "Am I eligible?", "Is my contract an eligible transaction?", "How much is my grant?", "By when must I apply, and by when must I move in, and for how long?", "When must I repay, and what can I be made to pay?". The spouse or de facto partner is in the seat in two ways: as a joint applicant (whose age, status and residence are asked), and as the person whose past grants and homes count against the applicant whether or not they apply (ss 6, 10, 11, 12A).

The Act puts one duty on the spouse or de facto partner alone (s 14(3), to give the Commissioner further information). That is in the core as a regulative rule with them as a party, but it is too slight to need a seat of its own. No other party has duties under the Act, and the Commissioner gets no seat. Most of Part 2 Divisions 4-5 and s 41 address the Commissioner (authorising payment, paying early, giving notice, imposing the penalty, remitting, the charge). Each is encoded as what it means for the buyer: when the grant is payable, what they must repay and by when, what a notice can require, and whether the home is charged.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The Regulations are deposited and brought in (rr 3, 4). The Act fixes every amount and date itself; the only outside figure is the TAA market interest rate (an input).
- **The actors the text names.** Followed: the applicant, the applicant's spouse or de facto partner, the Commissioner.
- **A judgment handed to someone else is answered conditionally.** Followed. These are inputs, and the answer holds if the Commissioner has so decided:
  - the s 4(b) opinion that a building is suitable as a residence;
  - the s 4A(2) declaration of a new home and the s 13AA(2) declaration of an eligible transaction;
  - the s 5(2)(b), (f) approvals and opinions;
  - the s 6(1) satisfaction that a married couple live apart for good;
  - the age and residence exemptions (ss 8(2), 12(3)(b)) and the longer or shorter residence periods (s 12(3)(a));
  - another commencement date for an owner build (s 13(5)(b)(ii));
  - the s 21(3) satisfaction that a deceased applicant meant to live in the home;
  - remission of penalty and interest (s 41(7)), and an instalment arrangement (s 41(6)).

  Payment before completion (s 17(2), (2A)) cannot be known in advance, so before completion the answer is "not payable until the transaction is completed, unless the Commissioner pays it earlier".
- **The Act's definitions worked out from facts; borrowed terms asked as facts.** Followed. Worked out: home (s 4), new home (s 4A), relevant interest (s 5, regs r 3), spouse (s 6), permanent resident (s 3, from the visa held), commencement date, completion and consideration (s 13(5)-(9)), threshold amount and threshold-relevant transaction (ss 3, 13AA(4)), established home in the urban area (s 18(4)), the application period (s 14(5)), the residence periods (s 12(2)), the required time (s 41(2A)). Asked as facts: Australian citizen, permanent visa and special category visa (Commonwealth Acts); new residential premises under GST Act s 40-75(1)(b); de facto partner (the NT Interpretation Act, not deposited); farming purposes (Stamp Duty Act s 4(1)); whether a past interest was a relevant interest in residential property (ss 10, 11; often under another State's corresponding law).
- **One case is the text's natural unit.** Followed: one transaction (s 7(3): "Only one first home owner grant is payable for the same eligible transaction"), with every applicant on the application.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed (see Scope).

**Departures, for the length of the form:**

- **Relevant interest has its own question.** The transaction and payability questions ask "I am, or on completion will be, an owner of the land" as one yes/no, pointing to that question, rather than repeating its eleven inputs.
- **Each person's history is asked as two choices** ("the first that applies"): one for earlier grants (ss 10(1), (2), 12A) and one for earlier homes (s 11(1), (3)-(5)). A person with more than one past interest picks the one that bars.
- **Applications by the buyer alone or with their spouse or de facto partner.** A third co-applicant (a sibling, parent or friend) answers "not covered: an applicant whose facts are not given".
- **The application period (s 14(5)) is a function, not a regulative rule.** "An application may only be made within a period" is a permission bounded in time, not a duty: not applying is never a breach. The seat gives its end date, and whether a given day is inside it.

## Scope

**In:**

- ss 3 (definitions used, including the threshold amount), 4, 4A, 5 with regs r 3, 6
- s 7 (entitlement)
- ss 8, 9, 10, 11, 12, 12A (the eligibility criteria)
- s 13(1), (2), (5)-(9) (eligible transaction, commencement, completion, consideration, the s 13(7) relocated building)
- s 13AA (the threshold cases), as dated rules: they apply only to transactions that commenced before 1 January 2015
- s 14(3) (as a regulative rule), (5), (6)
- s 15 with regs r 4
- s 17(2), (2A), (3), as conditional answers
- s 18 (the amount, as a dated table, with the s 18(4), (6) urban area)
- s 21 (death of an applicant)
- s 41(1)-(3), (5)-(7), (11), (12) (repayment, as regulative rules for (2) and (3); interest, penalty, charge, instalments, remission, joint and several liability)

**Out:**

- a commencement date before 1 January 2010, answered "not covered" (s 53 keeps the Act as it stood before the Revenue Legislation Amendment Act 2009 for those, and that text is not deposited)
- Part 5 replacement contracts and options (ss 54-56), answered "not covered", unless s 13AA(1)(a) already rules the contract out (finding 22)
- regs rr 5 and 6 (spent, finding 12)
- s 16 (guardians: the person under a disability is "regarded as the applicant", so their own facts are what the questions ask)
- ss 19, 20, 22, 23 (payment method, conditions generally, correcting and notifying decisions), except as the s 41 triggers they create
- administration and delegation (Part 3 Division 1)
- s 41(4), (8)-(10) beyond the offence named in the breach reasons
- s 42 (misleading statements), ss 43A-50
- s 45A (valuation)
- the objection and review path, which is encoded in the Stamp Duty Act encoding (see Links)

## Links

- **Stamp Duty Act 1978 (NT):** `../../../stamp-duty-act-1978/encodings/baseline-2026-10/`, committed on 2026-10-24 by another session. It encodes the duty concessions that turn on this grant:
  - s 89A(1)(ga) (the senior, pensioner and carer concession) and s 90(1)(fa) (the principal place of residence rebate) are denied to a buyer who has been paid, or is or will become entitled to, a first home owner grant;
  - s 89AA(2)(k) (the first home owner discount, for conveyances first executed from 24 May 2016 to before 7 May 2019) is denied to a buyer who is or will become entitled to the grant;
  - s 89AAC (the grant or the Territory home owner discount, not both, for 2015-2019 transactions);
  - s 90A and s 90AB (reassessment of duty when the grant is later paid or not).

  Its fact "a conveyee has been paid, is entitled to or will become entitled to a first home owner grant" is answered by this encoding's `Is the first home owner grant payable to me`. Its s 88(1) borrows this Act's "home", "relevant interest", "residential property", "permanent resident" and "owner builder", which this encoding works out.

  That encoding also has s 90D, the exemption for a new home bought with its land from a building contractor (1 July 2022 to 30 June 2027). Section 90D does not turn on this grant. Its conditions concern the conveyee (an individual, of age, a citizen or permanent resident, with no earlier beneficial interest in the land), the building contractor's land and new home, possession and occupancy (s 90D(2)). It borrows only this Act's "home" and "permanent resident", through s 90C(3) and s 88(1), and defines its own "new home" (s 90C(1)). Nothing in s 90D or in this Act makes the exemption and the grant exclusive.
- **Objecting to a grant decision.** Under Taxation Administration Act 2007 (NT) ss 109-110 a person affected may object in writing within 60 days after notice of the decision. Under s 115(2), for a first home owner grant decision the objector "may only apply to NTCAT", not appeal to the Supreme Court. Under s 116(1) the application to NTCAT is due within 60 days after notice of the objection decision. This is encoded in the Stamp Duty Act encoding (its `taa-cases.l4`) and not repeated here. This Act's s 51 applies TAA Part 11 to grant decisions. The TAA folder was not edited.
- **Commonwealth encodings** (cross-folder IMPORT is not possible, so the links are recorded here):
  - `../../../../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/` encodes GST registration only. Whether a sale is a taxable supply of new residential premises created by substantial renovation (s 40-75(1)(b)) is asked here as a fact; s 4A(1)(b) turns on it.
  - `../../../../migration-act-1958/encodings/baseline-2026-10/` answers "Is my visa a permanent visa (s 30)?", which is this encoding's "the holder of a permanent visa".
  - `../../../../australian-citizenship-act-2007/encodings/baseline-2026-10/` answers whether a person is an Australian citizen.
  - The grant's treatment under the Income Tax Assessment Act 1997 or the Social Security Act 1991 is not addressed: neither deposit mentions the grant, and neither encoding treats it.
- **No land tax.** The Northern Territory levies no land tax. Unlike Western Australia, an NT first home buyer meets only this grant and stamp duty, and there is no principal place of residence exemption to link.

## What the Act turns out to say

1. **$50,000 for a new home from 1 October 2024 to before 1 October 2027, then $10,000.** Section 18(3D)-(3F) sets the amount by commencement date. It is $50,000 for a new home from 1 Oct 2024, and $50,000 for every eligible transaction from 1 Oct 2025 to before 1 Oct 2027. From 1 Oct 2027 it is $10,000. Mia's $520,000 apartment, contracted in March 2026, gets $50,000; a new home contracted on 30 Sep 2027 gets $50,000 and one contracted on 1 Oct 2027 gets $10,000. Asserted.
2. **Since 2015, established homes have qualified for one year only.** A contract to buy any home, new or not, qualified if made before 1 Jan 2015 (s 13(1)(a)(i)). From then to before 1 Oct 2024, and from 1 Oct 2025, only a new home qualifies (s 13(1)(a)(ii), (iv)). In between, from 1 Oct 2024 to before 1 Oct 2025, any home did (s 13(1)(a)(iii)), at $10,000 (s 18(3D)(b)). Tom's established house contracted on 30 Sep 2025 gets $10,000; contracted on 1 Oct 2025 or 30 Sep 2024 it is not an eligible transaction; contracted on 31 Dec 2014 it is. Asserted.
3. **Building contracts and owner builds on site have no new-home test and, since 2015, no price cap.** The new-home tests reach a purchase (s 13(1)(a)) and, from 1 January 2015, a building bought to be moved onto the buyer's land, which s 13(7)(a) treats as an owner build (s 13(1)(c)(ii)(B), finding 18). A comprehensive home building contract (s 13(1)(b)) and an owner build other than under s 13(7) (s 13(1)(c)(ii)(A)) have none. The s 13AA thresholds reach only transactions that commenced before 1 January 2015 (s 13AA(4)). A $450,000 building contract on $900,000 land in 2016 is eligible. The grant is "the lesser of" the consideration actually paid and the amount (s 18(1)): an owner build costing $45,000 gets $45,000, and a $30,000 purchase gets $30,000. Asserted.
4. **Live there 12 months, not 6, for transactions from 1 Oct 2024 to before 1 Oct 2027.** Section 12(2) requires occupation to start within 12 months after completion. It must continue "at least 12 months" for a commencement date in that window, and 6 months otherwise. Josh and Ana's December 2027 contract needs 6 months. Asserted.
5. **Since 28 April 2015, one joint applicant living there is enough.** Section 12(4) exempts an applicant if another applicant complies. Before that date, every applicant had to live there or have the Commissioner's exemption: the same couple contracting in December 2014 fails s 12 unless Ana is exempted. Asserted.
6. **One adult and one citizen or permanent resident are enough for a joint application.** Under s 8(3), a 17-year-old applying with an adult meets the age criterion. Under s 9(2), a temporary visa holder applying with a citizen meets s 9. "Permanent resident" includes a New Zealand citizen on a special category visa (s 3), and, unlike WA's Act, there is no test of an intention to reside. Alone, a 17-year-old needs the Commissioner's exemption (s 8(2)). If both joint applicants are 17, both need it. Asserted.
7. **A spouse's or de facto partner's past counts, even if they do not apply.** Sections 10, 11 and 12A each ask about "the applicant or the applicant's spouse or de facto partner", as at the commencement date (s 6(2)). Priya, buying alone, is barred by her husband's former home. She is not barred if the Commissioner is satisfied they live apart with no intention of resuming (s 6(1)). Section 6(1) speaks only of a marriage, so a de facto partner still counts. Asserted.
8. **"Never owned a home" has three layers.** Any relevant interest in residential property before 1 July 2000 bars (s 11(1)), lived in or not. From 1 July 2000, only property used as the residence of the applicant or partner bars (s 11(3)): an investment unit never lived in does not. A property whose earlier grant was repaid is "taken not to have" been so used (s 11(4)). Asserted.
9. **An earlier grant repaid with penalty and interest no longer bars, except under s 12A.** Section 10(2) excuses a repaid grant. Section 12A bars "despite sections 10(2) and 11(4)" anyone paid a grant on a transaction that turned out to be over the threshold, "even if" it was repaid. Asserted.
10. **The threshold tests add the home's value to the land's.** For a pre-2015 purchase, s 13AA(1)(c) totals "the unencumbered value of the home" and "the unencumbered value ... of the relevant interest in the land on which the home is built". On a purchase of both, that may count the home twice, since the land includes the home; the encoding adds them as the text says. A 2011 purchase at $700,000, with values of $300,000 + $480,000, is over the $750,000 threshold. The threshold is $750,000 before 4 Dec 2012 and $600,000 after (s 3). Asserted.
11. **Read literally, s 41(2A)(c) can end the 30 days before the failure is known.** The 30 days run from "the earlier of" the date by which the person was to have occupied the home and the date the failure became apparent. Mia moves in on time, but realises on 15 Jun 2027 that she must leave before her 12 months are up. The earlier date is the move-in deadline, 20 May 2027, so her 30 days ended on 19 Jun 2027. Had she realised in July, the deadline would already have passed. The encoding applies the text. Asserted.
12. **Regulations rr 5 and 6 are spent, and pre-2010 transactions are outside the encoding.** Regulations 5 and 6 prescribe the 2009 "boost" amounts for ss 13B and 18A of the Act. Those sections were repealed in 2012 (No. 30, 2012, ss 13, 14), and the Regulations reprint, as at 1 July 2009, still carries them. Section 53 keeps the unamended Act for transactions that commenced before 1 January 2010, the commencement of Part 2 Division 3 of the Revenue Legislation Amendment Act 2009 (taken from the endnotes), and that text is not deposited. A November 2009 contract answers "not covered" for eligibility, transaction, amount and payability. Asserted.
13. **Section 56 deems a replacement contract's date for s 13 only.** For a contract that replaces one made before 1 October 2024, "Section 13 ... applies to a replacement contract as if the replacement contract was made on the date" of the original (s 56(3)). Section 18's amount turns on "the commencement date for the transaction", and s 56 does not say whether that date is deemed too. Part 5 is not encoded: such a contract answers "not covered", which is asserted. The question itself is not.
14. **What a default can cost.** Repayment is due within 30 days (s 41(2A)), and failure is a regulatory offence of up to 50 penalty units (s 41(8)). Interest runs from the due date at the statutory interest rate: the market rate plus 8% (TAA s 35). The Commissioner's notice can then require, within 30 days, the amount, the interest and "a penalty equivalent to the amount in default" (s 41(3)(b)), about double the grant. After those 30 days, interest runs on the penalty too (s 41(3)(c)). On $50,000 due 1 Jul 2026 and paid 12 Sep 2026 at a 4.35% market rate, the interest is $1,235. That reading is simple daily interest on a 365-day year: s 41 does not say how interest is worked out, and TAA s 34(3) says "on a daily basis" for tax defaults. The notice can then require $101,235. Asserted.
15. **The debt is a charge on the home, and each joint applicant owes all of it.** Section 41(5) makes the liability "an overriding statutory charge" on the person's interest in the home, and s 41(11) makes joint applicants' liability "joint and several". Asserted.
16. **Leases on Aboriginal land count.** Section 5(2)(h) makes a registered lease or sublease under s 19 or 19A of the Aboriginal Land Rights (Northern Territory) Act 1976 a relevant interest if its term is 15 years or more. A 40-year sublease counts; a 14-year one does not. Asserted.
17. **Building on a relative's land, or on farming land, counts.** Under regs r 3, building on a relative's (non-farming) land, or on farming land, with the owner's permission to occupy the home is a relevant interest. The r 3(3) list of relatives reaches a sibling's spouse but not a cousin. The landowner need not join in the application (r 4(b)). Asserted.
18. **A relocated building must be new.** From 1 January 2015, a building bought to be moved onto the buyer's land (s 13(7)) qualifies only if it is a new home (s 13(1)(c)(ii)(B)). "Place of residence" includes workers accommodation (s 4A(3)), so a former mine-site donga is not new. Asserted.
19. **Section 21(3) covers only an applicant who died before moving in.** It deems the residence requirements met where a deceased applicant "had not ... occupied the home" but intended to. It says nothing of one who died part-way through the continuous period. There the Commissioner's power to approve a shorter period (s 12(3)(a)(ii), which s 30A(2) allows after occupation has ceased) is the only route. Asserted (the third death case).
20. **Two duties have no period.** The further information under s 14(3) and payment under an instalment arrangement (s 41(6)) have no period in the Act, so neither becomes a breach by time alone. The s 14(3) trace is still pending 400 days on (`#TRACE`); the instalment rule is met by a payment on day 100 (`EVALTRACE`).
21. **The stamp duty concessions are closed to grant recipients; the grant is not closed to concession recipients, with one exception.** Stamp Duty Act ss 89A(1)(ga) and 90(1)(fa) deny the senior, pensioner and carer concession and the principal place of residence rebate to anyone paid, or entitled to, the grant. Section 90 is closed anyway to conveyances first executed from 8 February 2019 (s 90(1AA)). In the other direction, only the s 89AA first home owner discount bars the grant, and only while its duty is unpaid (s 10(4), asserted). Since 1 October 2025 an established-home buyer gets no grant, so (ga) no longer stands in their way. Not asserted here: the concessions are encoded in the Stamp Duty Act encoding.
22. **A pre-2000 option rules a contract out whatever Part 5 says.** Section 13AA(1)(a) says a contract made on or after 1 July 2000 "is not an eligible transaction" if the purchaser or vendor had an option granted before that date (for a building contract, if either party had such a right or option), unless the Commissioner declares it eligible (s 13AA(2)). Such a contract is often also a replacement contract under s 56. A contract "made in exercise of" the option is one under s 56(1)(b)-(c). Every building contract caught by s 13AA(1)(a)(ii) is one under s 56(2)(b), which has the same words with "granted before 1 October 2024". The first version asked the Part 5 question first and answered "not covered", so, on the form's own wording, its s 13AA(1)(a) answer could be reached only with contradictory answers. Part 5 cannot make such a contract eligible: s 56(3) deems a date for s 13 only, ss 54-55 change only the threshold tests and the amount, and s 54 applies only to "an eligible transaction". So s 13AA(1)(a) is now answered first, and gives "not an eligible transaction" for an exercised purchase option and for a building contract. The rule was corrected in the fix pass of 24 Oct 2026. With a declaration, the contract goes on to s 13 and to Part 5, which is not covered. A purchaser who held a pre-2000 option but bought under a fresh contract is caught by s 13AA(1)(a) ("had an option") but is not a replacement contract (s 56(1)(b) needs a contract "made in exercise of" the option). Asserted, all three.

## Corrections (fix pass, 24 Oct 2026)

An independent check of this encoding raised five points. Each was checked against the deposited text, and all five were upheld:

1. **The rule:** s 13AA(1)(a) now comes before the Part 5 gate (finding 22). In `fhog-core.l4`, `whether the transaction is an eligible transaction (ss 13, 13AA)` is reordered. The two seat `@desc`s for the pre-2000 option now use the words of s 13AA(1)(a) and say that an exercised option is also a pre-1 October 2024 option. The case that had answered yes to the pre-2000 option and no to the replacement question has been kept, now commented as the case where the option was held but not exercised. Three cases were added: the exercised purchase option, its payability, and the building contract. Assertions: 171 to 174. The answer changes only for a contract caught by s 13AA(1)(a) that is also a replacement contract, from "not covered" to "not an eligible transaction".
2. **Finding 2's heading** said established homes qualified "for one year only". They also qualified for any contract made before 1 January 2015 (s 13(1)(a)(i)). The heading and body now say so. Wording only.
3. **Finding 3** said only a purchase has a new-home test. From 1 January 2015, a s 13(7) building bought to be moved, which s 13(7)(a) treats as an owner build, must also be new (s 13(1)(c)(ii)(B)), as finding 18 and the code already had it. Wording only.
4. **The Stamp Duty Act links** (here and in `encoding.json`) listed s 90D among the concessions that turn on the grant. Its conditions never mention the grant, so it is now listed apart, with the two terms it borrows from this Act. Section 89AA(2)(k), which the Stamp Duty Act encoding also drives from the grant, has been added to the list.
5. **Two case comments** cited the wrong findings: "finding 9" for the literal s 41(2A)(c) reading (finding 11), and "finding 10" for s 21(3) (finding 19).

## Before relying on it

- An independent test pass, and a check against the Territory Revenue Office's published guidance and forms, none of which were consulted.
- Check the register's history for amendments after the 1 July 2026 reprint, and for any amendment of the Regulations after their 1 July 2009 reprint.
- Deposit the Act as it stood before the Revenue Legislation Amendment Act 2009 (or that amending Act), if pre-2010 transactions matter; and encode Part 5 (ss 54-56) for replacement contracts, settling the s 56 and s 18 question (finding 13).
- Deposit the TAA regulations that prescribe the market interest rate, and settle how interest under s 41 is computed (finding 14).
- Link this encoding's `Is the first home owner grant payable to me` to the Stamp Duty Act encoding's grant fact once both are published, and confirm the two agree on a shared case.
- If the form is to serve co-owners beyond a couple, generalise the seat's applicants (the core already takes a list).

## Licence

The text is quoted under the Northern Territory copyright policy of 8 October 1996 and **the owner's ruling of 24 Oct 2026 (Michael)**: the NT terms permit reproduction but are silent on adaptation; as for Canada, the texts may be quoted in L4 encodings in Legalese Commons, keeping the NT attribution and the unofficial-copy notice. The ruling is recorded in `SOURCE-LICENSE.md` here and in both subjects' `SOURCE-LICENSE.md`. Copyright in Northern Territory legislation is owned by the Northern Territory. The quotations come from an unofficial copy, not an official version. The L4 is Apache-2.0.
