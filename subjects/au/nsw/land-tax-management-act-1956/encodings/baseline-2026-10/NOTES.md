# Land Tax Management Act 1956 (NSW), with the Land Tax Act 1956: baseline encoding for the owner of land

> **Warning.** Both texts encoded here are **taken from the Open Australian Legal Corpus, collected on 10 March 2025. They are not the current official text and may be out of date.** Check legislation.nsw.gov.au before relying on anything here. The thresholds are encoded as the deposited text states them, and **for the 2025 and later land tax years they must be checked against the current register.**

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It contains no REFUSE. Where a case falls outside the encoding, the answer is an explicit `not covered` value, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
There was no pipeline, no coverage table, no independent test pass and no human gate.
**Not for public use as advice.**

The encoding has two layers:

- **`ltma-core.l4`** is the seat-neutral core. It uses the Acts' own actors and terms: the owner, the joint owners (the primary taxpayer), the taxpayer, the members of the family, the foreign person and the Chief Commissioner. Computations are functions: average value, taxable value, the thresholds, the Schedule 13 rate, the s 27 joint and separate assessments, the Schedule 1A exemption, the s 40 discount and the s 5A surcharge. Where the text says "must" or sets a deadline, there is a regulative rule (`DEONTIC`), seven in all:
  - s 12(1A)-(1B), the return;
  - Schedule 1A cl 6(5)-(6) and cl 7(3A)-(4), the revocations;
  - Schedule 1A cl 12(2)-(5), the family election;
  - s 39(1), (3), payment;
  - s 40, the discount;
  - Land Tax Act s 5B(2)-(4), the 200-day residence requirement.
- **`ltma-seat.l4`** is the owner's seat. It asks 22 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule. The five home-exemption questions share the same 22 leading answers, in the same order, so the form can ask them once.

No earlier encoding of either Act existed to keep. NSW has no requirement ledger, so no ledger line is closed.

## Edition

- **Land Tax Management Act 1956 No 26**: NSW Legislation version of 2024-12-02 (`nsw_legislation:2024-12-02/act-1956-026`), as deposited at `../../registers/source-bundle/act-1956-026.txt`.
- **Land Tax Act 1956 No 27**: version of 2024-12-02 (`nsw_legislation:2024-12-02/act-1956-027`), as deposited at `../../../land-tax-act-1956/registers/source-bundle/act-1956-027.txt`. It sets the rates and the surcharge. It is read with the Management Act (its s 1), so it is brought in here rather than encoded on its own.
- Both come from the **Open Australian Legal Corpus**, version 7.1.0, which collected NSW Legislation on 10 March 2025. The owner decided on 2026-10-20 to use this route because legislation.nsw.gov.au returned a bot challenge. **Neither is the current official text, and either may be out of date.**
- **Figures the Acts state**, encoded as stated:
  - the s 62P tax thresholds and s 62S premium rate thresholds, as tables for 2006 (or 2009) to 2023, then $1,075,000 and $6,571,000 for every later year;
  - the Schedule 13 Part 1 scale (nil; $100 plus 1.6%; then 2%);
  - the $100 minimum (s 3AL(5));
  - the surcharge rates (s 5A(2));
  - the day counts: 31 January, 30 days, 6 months, 4 and 6 tax years, 6 years, 182 days, 2 years, 25%, 200 days.
- **Figures the deposit does not supply**, taken as inputs:
  - land values, which come from the Valuer-General's Register (s 9(4));
  - any land value adjustment (s 9AA(2), (6));
  - the Treasurer's discount rate (s 40(2), a Gazette order);
  - the objection period for the family election (Schedule 1A cl 12(3), which refers to the Taxation Administration Act 1996 s 89, not deposited);
  - whether a Gazette order under s 12(1) covers the owner.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ltma-core.l4`, `ltma-seat.l4` | `ltma-cases-owner.l4` | 162 written, 162 satisfied |

Eight `#TRACE`s carry an `-- expect:` line: six breaches (s 12, cl 6(5) twice, cl 7(3A), s 39 and s 5B) and two obligations still pending (cl 12 and s 40). Each was read and matches its expectation.

`l4 run` on all three files gave 0 errors and 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A deliberately wrong assertion was run once as a control, and it was reported as `assertion failed`.

Every expected value was worked by hand from the texts, with the arithmetic in the comment above the assertion. The 1.5% discount rate and the 60-day objection period in the cases are test inputs, not the law.

## Seat

**The individual owner of land in NSW**, including a joint owner and a foreign person liable to surcharge land tax. The owner asks:

- "Do I owe land tax for this year?"
- "Is my home exempt, including while I build, move or am away?"
- "How much do I owe, alone or jointly?"
- "Must I lodge a return or make a family election, and by when?"
- "When must I pay, and do I get the discount?"
- "As a foreign person, what surcharge do I owe, and can I keep my home exemption?"

The death concession (cl 9) is asked by the personal representative or a beneficiary, in the owner's place.

The Chief Commissioner's assessments, satisfactions, extensions and treatments appear only as what they mean for the owner: a condition answered conditionally, or the other party to a regulative rule. There is no second seat. The co-owner's liability for a foreign co-owner's default (s 5A(5)) is out of scope, and no other party bears duties that the encoded provisions state.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** The Land Tax Act is brought in for the rates. The Land Tax Management Regulation 2024 is not deposited, so whatever needs it answers `not covered`. The Treasurer's discount order is an input.
- **The actors the text names**, as listed above.
- **Judgments left to others are answered conditionally, as inputs.** The Chief Commissioner may be satisfied under:
  - cl 2(2)(b), that the land is the owner's principal place of residence;
  - cl 6(4)(a), that works began or significant steps were taken;
  - cl 6(7A), when extending the building period (up to 6 years);
  - cl 9(3), when extending the 2 years after a death;
  - s 5A(4)(d), that the land is partly used for other purposes;
  - s 5B(1)(b), that the owner intends to meet the residence requirement.

  The facts behind the "Chief Commissioner is satisfied" in cl 7(1)-(2) and cl 8(1), (6) are asked as facts.
- **The Acts' own definitions are worked out from facts:**
  - average value and taxable value;
  - residential land, with the excluded residential occupancy and the one business room;
  - lots in the same ownership, asked as one fact for each of cl 13 and cl 14;
  - unoccupied land;
  - the family (cl 12(6)-(9)), glossed in the input description;
  - full time care, glossed;
  - the clause 6, 8 and 9 periods.

  Borrowed terms are asked as facts: "foreign person", "residential land" and "retirement visa holder" (Duties Act 1997 Chapter 2A), "permanent resident" (see finding 10), an approved shared equity scheme (Duties Act s 281), and carer payment (Social Security Act 1991). **One departure:** "special trust" (s 3A) and "non-concessional company" (s 29) are the Act's own terms, but they are asked as facts, because they lead only to answers that are not covered.
- **One case** is one parcel (or one set of lots used as one home) on one taxing date for the exemption questions, and one owner's land on one taxing date for the tax. **Limit:** the seat takes at most one joint holding (land owned with the same co-owners). The core takes a list.
- **The Acts' own terms**, quoted in the comment above each rule.
- **Machinery out:** administration (Part 2), the Hardship Review Board, valuation machinery (Part 7 Division 3), the s 62T review, regulations and savings, and the Taxation Administration Act.

## Scope

**In (Land Tax Management Act 1956):**

- s 7, s 8, s 9(1)-(4), s 9AA(1), (2), (6), (7), (11)
- s 10(1)(r) and Schedule 1A:
  - cl 1 and cl 2 (used and occupied by the owner as principal place of residence and for no other purpose; continuous since 1 July, or the Chief Commissioner satisfied)
  - cl 3 (residential land), cl 4 (one excluded residential occupancy), cl 5 (one business room)
  - cl 6 (unoccupied land being built on: 4 tax years, up to 6 under (7A), the (3)(b) and (4)(a) variant, and the (7) exclusions), with the cl 6(5)-(6) revocation
  - cl 7 (change of residence: a new home bought within 6 months; one taxing date), with the cl 7(3A)-(4) revocation
  - cl 8 (absence: 6 months' prior occupation; 6 years at most; full time care not counted, including cl 8(5)(c) carer payment; the income limits of 6 months or 182 days, or cost recovery; (3A))
  - cl 9 (death of the owner)
  - cl 11 (companies and trustees)
  - cl 12 (one residence per family, with the election as a regulative rule)
  - cl 13 and cl 14 (two or more lots)
  - cl 15 (minimum 25% interest), with Schedule 2 cl 70
- s 12(1A)-(1B) (the return, regulative)
- s 27(2)-(4), with s 33 and s 34 (joint and separate assessments, and the deduction)
- s 39(1), (3) and s 40 (payment and the discount, regulative)
- s 62P and s 62S (the thresholds, as tables)

**In (Land Tax Act 1956):**

- s 3AL(1), (2)(a), (5) and Schedule 13 Part 1
- s 5A(1)-(4): surcharge on residential land owned by a foreign person; the rate by year as a table; no threshold; as if the only land; the proportionate interest
- s 5B(1)-(4): the surcharge home exemption, and the 200-day residence requirement as a regulative rule

**Not covered (an explicit `not covered` answer, asserted):**

- land subject to a special trust (Schedule 13 Part 2)
- land owned with a non-concessional company (Schedule 13 Parts 3 and 4)
- anything that needs the Land Tax Management Regulation 2024: a lessee the regulations make an owner (s 3 "owner" (c)), and the home exemption of a retirement visa holder (s 5BA)
- land tax years before 2009
- residential land partly used for other purposes (s 5A(4)(d), Duties Act s 104ZB)

**Out:**

- s 10 exemptions other than (1)(r)
- s 10AA (primary production)
- ss 9A-9E land value reductions, except as the one adjustment input
- ss 10Q and 10R (low-cost accommodation, retirement villages)
- s 3AL(6)-(9) and s 73 (property tax land, the closed First Home Buyer Choice)
- Land Tax Act ss 5C, 5CA and 5D (developers, build-to-rent, discretionary trusts), s 5A(4)(e)-(f), s 5A(5) (recovery from co-owners and trustees), and s 5BA beyond the not-covered answer
- Schedule 1AA (family unit trusts)
- Schedule 1A cl 8(3) (resuming occupation at the end of 6 years), cl 10, 10A, 10AA and 10B
- deemed owners (ss 20-26, including the purchaser and vendor rule in s 26)
- exempt co-owners within s 27(2) and (5)
- s 12(1C)-(3), ss 14-15
- the Taxation Administration Act 1996 (objections, interest, penalty tax, reassessment periods)

## Links to other encodings

Cross-folder IMPORT does not work, so these links are recorded here only.

- **Social Security Act 1991 (Cth), carer payment.** Schedule 1A cl 8(5)(c) counts as full time care any period in which the owner "resides with another person (a carer) who is eligible for a carer payment under the Social Security Act 1991 of the Commonwealth because the carer provides care to the person". The Act is deposited, and its carer payment questions are encoded at `../../../../social-security-act-1991/encodings/baseline-2026-10/` (for example `Am I qualified for carer payment ...`). Here that eligibility is a fact folded into the days in full time care.
- **Income Tax Assessment Act 1997 (Cth), deduction of land tax on a rental.** That land tax paid on a property let to produce assessable income is deductible (s 8-1) is **unverified** (from general knowledge, not from the texts). See `../../../../income-tax-assessment-act-1997/`.
- **Income Tax Assessment Act 1997 (Cth), Subdivision 118-B (main residence).** This is a similar but different test of the home, encoded in part at `../../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/` (`itaa-cgt-formulas.l4`). That the two tests differ, for example in their absence rules, is **unverified** (from general knowledge, not from the texts), as the jurisdiction README says.
- **Duties Act 1997 (NSW), Chapter 2A and s 281.** Deposited at `../../../duties-act-1997/` but not encoded. It supplies:
  - "foreign person" (s 104J, which adopts the Foreign Acquisitions and Takeovers Act 1975 (Cth), deposited at `../../../../foreign-acquisitions-and-takeovers-act-1975/`);
  - "residential land" and "retirement visa holder" (s 104I);
  - the s 104ZB apportionment factor;
  - approved shared equity schemes.

  Here each of these is a fact or a `not covered` answer.
- **Taxation Administration Act 1996 (NSW).** Not deposited. It sets the objection period (s 89), interest and penalty tax, and the tax default consequences of s 5B(4).

## Findings: what the Acts turn out to say

1. **The thresholds are open-ended in the deposited text.** s 62P(s) gives "$1,075,000" and s 62S(p) "$6,571,000" "for a land tax year after the 2023 land tax year". Schedule 2 cl 69 validates them, and s 62T requires a review by 1 June 2027. They are encoded as stated, so 2025, 2026 and later years use them. They must be checked against the current register. Asserted.
2. **The surcharge rates in Land Tax Act s 5A(2) follow the year of the 31 December ownership date, not the land tax year.**
   - "Commencing with 2024 -- 5%" therefore means the 2025 land tax year onward.
   - The 2023 and 2024 land tax years are taxed at 4%, 2018-2022 at 2%, and 2017 at 0.75%.
   - The task's "5% from the 2024 year" is the ownership year.

   Asserted.
3. **s 5A(4)(h) refers to a repealed Division.** It disapplies "the tax thresholds under Division 4A of Part 7 of the Principal Act", but Division 4A has been repealed (Management Act Schedule 2 cl 68). The thresholds are now in Division 4 (ss 62P, 62S). The stale reference is read for its evident purpose, together with (4)(a) ("as if the residential land were the only land"): surcharge has no threshold. The s 3AL(5) $100 rule applies to land tax "pursuant to this section", so it is not applied to surcharge either. Asserted: on a $900,000 flat, land tax is nil and surcharge is $45,000.
4. **s 3AL(5) never applies to the Schedule 13 Part 1 scale alone.** Any taxable value above the threshold already attracts $100 plus 1.6%. The rule matters only for a joint owner's separate assessment after the s 27(4) deduction, which can leave a small remainder. The Act does not say whether "the total amount of land tax payable ... by any person" is measured before or after the deduction. The encoding reads it as after. Asserted: $45.45 becomes nil.
5. **Read literally, Schedule 1A would defeat its own concessions.** Clause 2(1) and clause 3 require land used "for no other purpose", with no other occupancy and no income. Read that way, they would defeat:
   - cl 8(7), which allows letting while the owner is away;
   - cl 7(2)(c)(ii), which allows the previous owner's tenant;
   - cl 6, which covers unoccupied land;
   - cl 9, which covers a deceased owner.

   The encoding applies the use and income tests of cll 3-5 only to land the owner actually lives in. Under cll 7-9 the land must still be a residential building or a strata lot, and the concession's own use and income conditions apply instead. Clause 6 land is unoccupied by definition. This is an inference. Asserted: Tom's 150 days of letting do not cost the exemption.
6. **cl 8(7)(a) sets two limits.** The right of occupation must "not exceed a continuous period of 6 months, or a total period of 182 days, in the tax year". The encoding reads this as two limits, both of which must be met. A 12-month lease fails, and so do short lets totalling 200 days. Asserted.
7. **Schedule 2 cl 70 ends at the same instant as the 2026 taxing date.** It saves a person "previously entitled" from the cl 15 25% rule, but "ceases to apply at the end of 31 December 2025". That is the same instant as the taxing date for the 2026 land tax year (midnight on 31 December 2025). The encoding applies cl 70 up to the 2025 land tax year only. Whether it reaches 2026 is a question for Revenue NSW. Asserted.
8. **Some answers depend on the Land Tax Management Regulation 2024**, which is in the corpus but not deposited.
   - s 5A(4)(i) lets the regulations modify surcharge. The surcharge amounts here assume no prescribed modification.
   - s 5BA(1) applies s 5B to retirement visa holders "subject to any modifications prescribed by the regulations". Their home exemption answers `not covered`.
   - s 3 "owner" (c) makes a prescribed lessee an owner. That case answers `not covered` too.

   Asserted.
9. **The surcharge home exemption depends on a required return.** s 5B(1)(c) needs a declaration lodged "with a land tax return required to be furnished under section 12". On the words, a foreign owner who is not required to lodge a return (by a s 12(1) Gazette order or a s 12(2) requirement) cannot meet it. It is encoded as a fact the owner states.
10. **"Permanent resident" (s 5B(1)(a)) is defined in neither deposited Act.** Land Tax Act s 2A borrows "foreign person", "residential land" and "retirement visa holder" from Duties Act Chapter 2A, but not this term. The deposited Duties Act's note to s 104J(2) shows how a permanent resident can still be a foreign person: under FATA s 5, a non-citizen is ordinarily resident only after 200 days in Australia in the previous 12 months. It is asked as a fact.
11. **Schedule 1A cl 12(3) and (4) state the election deadline twice:** once by reference to Taxation Administration Act s 89, and once as the end of the period for objecting to the initial assessment. Neither period is in the deposit, so it is an input. Missing it is not a breach, but it brings in cl 12(5) (the highest land value). Traced.
12. **s 39(3) and s 40 use the same 30 days.** A notice cannot require payment earlier than 30 days after service, and paying the whole amount within 30 days (with nothing else owing) earns the discount. A notice that states an earlier due date is read as 30 days. Asserted.
13. **s 27(2) makes joint owners "jointly assessed and liable".** The deposited Management Act does not say that each joint owner can be made to pay the whole; contrast WA Land Tax Assessment Act s 7(4). Recovery is under the Taxation Administration Act 1996, which is not deposited. The encoding reports the joint assessment as an amount the joint owners owe together.
14. **cl 7(2)(b), "within the period of 6 months before the relevant taxing date",** is read as on or after 1 July of the year of the taxing date. Asserted: 1 July is in, 30 June is out.
15. **Schedule 13 states no rounding.** The encoding does not round, so the s 34 apportionment can produce cents.
16. **cl 6(7A) allows an extension "to a period of up to 6 tax years".** An extension stated as longer is read as 6. Asserted.

## Before relying on it

- Replace both texts with the current official text from legislation.nsw.gov.au. Then re-check the thresholds for 2025 and later, the surcharge rate, and every clause quoted.
- Deposit and bring in:
  - the Taxation Administration Act 1996 (objection period, interest, penalty tax, reassessment);
  - the Land Tax Management Regulation 2024;
  - the Treasurer's current s 40 discount order.
- Run an independent test pass, and check the amounts against Revenue NSW's published examples or calculator.
- Encode what is out of scope:
  - deemed owners (ss 20-26);
  - exempt co-owners;
  - more than one joint holding in the seat;
  - Schedule 13 Parts 2-4 and Schedule 1AA;
  - Schedule 1A cl 8(3), 10, 10A, 10AA and 10B;
  - s 5A(5) and s 5BA;
  - the other s 10 exemptions and s 10AA.

## Licence

`SOURCE-LICENSE.md` here is a copy of the Management Act subject's. The Land Tax Act's terms (`../../../land-tax-act-1956/SOURCE-LICENSE.md`) are the same: State of New South Wales, CC BY 4.0, through the Open Australian Legal Corpus 7.1.0 (CC BY 4.0), corpus document `nsw_legislation:2024-12-02/act-1956-027`.

Based on content from the New South Wales Legislation website at 10 March 2025. For the latest information on New South Wales Government legislation please go to https://www.legislation.nsw.gov.au. The L4 is Apache-2.0.
