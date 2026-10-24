# Duties Act 1997 (NSW): baseline encoding for the buyer

> **Not the current official text.** The text encoded is the Open Australian Legal Corpus copy of the Duties Act 1997 (version of 1 January 2025, collected on 10 March 2025). It may be out of date: check legislation.nsw.gov.au before relying on anything here. Based on content from the New South Wales Legislation website (State of New South Wales, CC BY 4.0), via the Open Australian Legal Corpus (CC BY 4.0); see `SOURCE-LICENSE.md`.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. Where the deposit cannot answer, the answer is an explicit `not covered` value naming the gap, and a test asserts it. Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

It follows the WA Duties Act 2008 baseline (`../../../../wa/duties-act-2008/encodings/baseline-2026-10/`), a home and a vehicle, so that the two states can be compared. It is written in two layers, after the SNAP baseline:

- **`nsw-duties-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the transferee", "the purchaser or transferee", "the applicant", "the applicant for registration"). Computations are functions. Where the text says "must" or sets a deadline there is a regulative rule (`DEONTIC`), five in all: ss 15, 16 and 16A (lodge within 3 months), s 17 (pay within 3 months), s 104W (pay surcharge purchaser duty within 3 months), s 76A(2) (notify and pay within 14 days if the residence requirement is not met) and s 262 (lodge a statement of dutiable value with the application). Dates use only the prelude's built-in DATE functions; daydate is not imported.
- **`nsw-duties-seat.l4`**, the buyer's seat: 20 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule. The same fact has the same input name and wording in every question, so a form can ask it once.

Case files: `nsw-duties-cases-core.l4` (the table, the indexation, the dates, the purchaser tests and the regulative rules) and `nsw-duties-cases-buyer.l4` (the seat's questions; its positional calls are formatted from a table by the scratchpad generator `au-nsw-1/gen_nsw_duties_cases.py`, with every expected value written by hand).

This is the first encoding of this Act; there was none to keep. NSW has no requirement ledger, so no ledger line is closed.

## Edition

- **Statute:** Duties Act 1997 No 123 (act-1997-123), corpus document `nsw_legislation:2025-01-01/act-1997-123` (version date 2025-01-01, scraped 2025-03-10), from the Open Australian Legal Corpus version 7.1.0, deposited at `../../registers/source-bundle/act-1997-123.txt`. Taken from the corpus because legislation.nsw.gov.au answered with a bot challenge. **It is not the current official text and may be out of date.**
- **Brought in:** the First Home Owner Grant and Shared Equity Act 2000 (act-2000-021, corpus version 2023-09-04), at `../../../first-home-owner-grant-and-shared-equity-act-2000/registers/source-bundle/act-2000-021.txt`. It was read only for s 4A ("new home"), which s 74(5) of the Duties Act borrows. Section 74(5) serves only s 74(4), the expired 2020-21 window, which is out of scope, so no code uses it.
- **Not deposited, so inputs:** the Sydney CPI numbers (s 33AB, s 33AC) and the Chief Commissioner's s 33AF notice of each year's adjusted amounts. The s 32 table in the deposit holds the amounts for the year beginning 1 July 2019. For any later year, the seat asks for that year's five threshold amounts and the premium threshold, and works out the base amounts under s 33AD (finding 2). Also not deposited: the Taxation Administration Act 1996 (interest, penalty tax, objections) and the Interpretation Act 1987 (how "within 3 months" is counted).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nsw-duties-core.l4` | `nsw-duties-cases-core.l4` | 114 written, 114 satisfied |
| `nsw-duties-core.l4`, `nsw-duties-seat.l4` | `nsw-duties-cases-buyer.l4` | 160 written, 160 satisfied |

In addition, 9 `#TRACE`s in `nsw-duties-cases-core.l4` carry an `-- expect:` line. Each is a breach (lodged late, lodged without the purchaser's declaration, no written statement, paid late, paid short, surcharge paid late, notice late, relevant duty paid late, statement lodged after the application). Each was read and matches its expectation, with the expected party and reason.

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A copy of `nsw-duties-cases-buyer.l4` with two expected values changed ($29,182 to $29,183) was run as a control: the runner reported 2 assertions failed and 158 satisfied.

Every expected value was worked by hand from the deposited text, with the arithmetic in the comment above the assertion. The later-year amounts used in the cases, **H** = $16,000, $34,000, $91,000, $341,000, $1,138,000 and a premium threshold of $3,414,000, are **hypothetical**. They are what s 33AC gives for A/B = 1.123, and that is asserted. They are not the amounts the Chief Commissioner published for any year, and the CPI numbers in the cases are made up (B = 100).

## Seat

**The buyer:**

- of a home, or of vacant residential land, including a first home buyer, a spouse taking a share of the home, and a foreign person;
- and the applicant to register a motor vehicle.

For land this is the transferee, who pays (s 13; s 104R for surcharge purchaser duty). For the scheme it is "the applicant" (s 76A). For a car it is "the applicant for registration" (s 263).

The Chief Commissioner's powers and judgments appear only as what they mean for the buyer: an approval, an exemption, a longer or shorter residence period, or being "satisfied" of something, each asked as a fact or answered conditionally ("no duty ..., once the Chief Commissioner approves the application"). No seat for the Chief Commissioner. No second seat: the seller has no duty under the provisions in scope.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows. The rates are in the Act, but the thresholds move every year under s 33AC, and the s 33AF notice is not deposited, so a later year's amounts are inputs (finding 2).
- **The actors the text names.** Followed: the transferee, the purchaser or transferee, the applicant, the applicant for registration, and the Chief Commissioner.
- **Judgments left to others, answered conditionally.** Followed:
  - the Chief Commissioner's approval of the application (s 78A(1)) and of a longer or shorter residence period (s 76(1), (2));
  - an exemption from the residence requirement (s 76(2)(b));
  - being satisfied that a spouse is separated (s 71(5)), that land is used for other purposes (s 32B, s 104ZB), or of a relationship breakdown (s 267(6)-(7));
  - a determination under s 73(4) that an under-18 buyer is eligible: the answer says "unless the Chief Commissioner determines otherwise".
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.** Worked out:
  - dutiable value (s 21);
  - residential land, three ways (s 32A(3), s 104A, s 104I; finding 12);
  - first home owner (s 71), with s 71(7);
  - eligibility (ss 73, 73A, 74, 75);
  - the residence requirement (s 76);
  - de facto partner (Dictionary, 2 years);
  - passenger vehicle (s 265(2));
  - the dutiable value of a vehicle (s 266).

  Asked as facts:
  - foreign person (s 104J, the FATA meaning as modified);
  - permanent resident;
  - spouse (s 71(4));
  - Permanent Forces membership and enrolment to vote (s 76(6));
  - the Veterans' Entitlements Act pension rate and MRCA impairment points (s 267(7A), (7AA));
  - GST-free supply under Subdivision 38-P (s 266(2)(a));
  - land used for primary production (s 104I).
- **One case is the text's natural unit.** Followed: one dutiable transaction (one parcel) by the buyer alone or with one other person, or one application to register one vehicle. In the core a purchase holds any number of purchasers; the seat offers you and at most one co-buyer, plus an approved equity partner under an approved shared equity scheme.
- **The Act's own terms, each with a plain gloss.** Followed: the comment above each rule quotes the text.
- **Machinery out.** Followed.

**Departures:** none from the defaults. For the scheme the seat merges two of the Act's facts into one answer: owning residential property, and having been a party to an approved application (s 71(2)(a), and the same for a spouse). Either one disqualifies in the same way.

## Scope

**In:**

- Chapter 2:
  - s 8 (duty is charged on a transfer, or an agreement for transfer, of dutiable property) and s 11(1)(a) (land in NSW);
  - s 12 (liability arises when the instrument is first executed: the seat asks for the day the contract was signed);
  - s 13 (the transferee pays) and s 14 (joint tenants are tenants in common in equal shares);
  - ss 15, 16, 16A (regulative: within 3 months, make a written statement or lodge the instrument, with the purchaser's declaration);
  - s 17 (regulative: pay within 3 months, or a tax default occurs);
  - s 21 (dutiable value);
  - s 32 (the general rate, as the deposited table);
  - s 32A (the premium rate; s 32A(3) residential land from facts);
  - ss 33AB-33AF (s 33AC and s 33AD as functions; the s 33AF amounts as inputs).
- Part 8 Division 1, the First Home Buyers Assistance Scheme:
  - s 70, s 71 (with (4)-(8));
  - s 73, s 73A, s 74(1)-(3), s 75, s 76 (with the s 76(6) ADF exemption);
  - s 76A(2) (regulative) and s 76A(3);
  - s 78A(1);
  - s 78B(1), (2) and (6), only to say when the shared equity concession is in play.
- Part 8 Division 4: ss 104A, 104B and 104C (the s 104C factor is an input).
- Chapter 2A: s 104G, s 104I, s 104J (foreign person, as a fact), s 104K, s 104L, s 104R, s 104U, s 104V, s 104W (regulative), s 104Z, and s 104ZK(2).
- Chapter 9:
  - s 261, s 262 (regulative), ss 263-264, s 265, s 266;
  - s 267(1), (6), (6A), (7), (7A), (7AA), (7B);
  - s 268.
- Schedule 1 cl 147 (the scheme's thresholds from 1 July 2023) and cl 156 (the 9% rate), as date limits.

**Not covered** (an explicit `not covered` answer, asserted):

- the concessional duty formulas in s 78A(2) and (2A), and the shared equity formula in s 78B(3), which the corpus dropped (finding 1);
- s 32B (land used for other purposes) and s 32C (parcels over 2 hectares) above the premium threshold;
- s 104C beyond a supplied apportionment factor;
- s 104ZB (apportionment for surcharge purchaser duty), and s 104ZKA and s 104ZKB (exempt permanent residents and retirement visa holders);
- a general-rate liability before 1 July 2019;
- a scheme agreement before 1 July 2023;
- a surcharge liability before 1 January 2025;
- a later year whose amounts, as given, cannot be s 33AC amounts;
- a building under construction or two or more dwellings under the scheme (finding 13).

**Out:**

- s 78AA (the window from 1 August 2020 to 31 July 2021, expired), s 74(4) and s 74(5);
- Division 1A, the new home grant (historic, s 82);
- s 49A (off-the-plan deferral);
- s 18 (no double duty) and s 18A with First Home Buyer Choice property tax (the scheme is closed);
- s 15(4) (lodging an instrument in place of a statement);
- s 12(4) (electronic registry instruments);
- s 32A(2B) (several items of residential land in one transaction);
- landholder duty (Chapter 4), insurance duty (Chapter 8) and mortgages (Chapter 7);
- the other exemptions and concessions in Parts 6 and 7, and Part 8 Divisions 3 and 5;
- s 267(2)-(5) and (8) (charities, Local Land Services, financiers, ambulances, the Chief Commissioner's equity power), ss 269-270C (stolen vehicles, dealers, modified vehicles for people with disabilities, caravans, heavy trailers) and s 273 (minimum duty, finding 14);
- interest, penalty tax and objections (Taxation Administration Act 1996, not deposited).

**No pensioner or seniors concession.** No pensioner or seniors concession on transfer duty or vehicle duty appears in the deposited Duties Act; the word "pensioner" does not occur in it. None is encoded. The NSW pensioner concession in this sample is the council rates rebate in the Local Government Act 1993.

## The buyer's questions

| The buyer asks | Seat question(s) |
|---|---|
| What duty do I pay on this home or land, and by when? | `What transfer duty do I pay on this home or land`, `What is the dutiable value of my purchase`, `By what day must I lodge and pay the transfer duty`, `What is the adjustable amount for the year` |
| Am I a first home owner, is the purchase eligible, and do I pay no duty? | `Am I a first home owner`, `Is my purchase eligible under the scheme, and do I pay no duty`, `What transfer duty do I pay as a first home buyer` |
| What must I do, and by when, if I do not move in? | `Have I met the residence requirement`, `Must I give notice and pay the relevant duty`, `By what day must I give notice and pay the relevant duty`, `How much relevant duty must I pay` |
| Is a transfer of the home to my spouse duty-free? | `Is the transfer to my spouse exempt`, `What transfer duty is payable on the transfer to my spouse` |
| Do I owe surcharge purchaser duty, and how much? | `Do I owe surcharge purchaser duty, and how much`, `By what day must I pay surcharge purchaser duty` |
| What duty do I pay to register this car, and am I exempt? | `Is my application charged with duty`, `What is the dutiable value of the vehicle`, `Am I exempt from registration duty`, `What duty do I pay to register this vehicle`, `Must I lodge a statement of the dutiable value` |

The situations, marked in the `§§` comments: buying a first home; having been approved in advance and perhaps not meeting the residence requirement; transferring the home to a spouse; a foreign buyer.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **GST Act, Subdivision 38-P** (cars for use by disabled people), cited by s 266(2)(a): `../../../../a-new-tax-system-goods-and-services-tax-act-1999/`. Whether a supply is GST-free under it is asked as a fact. The GST baseline does not encode Subdivision 38-P.
- **Veterans' Entitlements Act 1986, ss 22-24** (the general rate, the extreme disablement adjustment, the intermediate rate, the special rate), cited by s 267(7A): `../../../../veterans-entitlements-act-1986/encodings/baseline-2026-10/`. Which rate a veteran is eligible for is asked as a fact.
- **Military Rehabilitation and Compensation Act 2004** (impairment points, compensation, the special rate disability pension), cited by s 267(7AA): `../../../../military-rehabilitation-and-compensation-act-2004/encodings/baseline-2026-10/`.
- **Foreign Acquisitions and Takeovers Act 1975, "foreign person"**: `../../../../foreign-acquisitions-and-takeovers-act-1975/encodings/baseline-2026-10/`. Section 104J takes the FATA meaning but modifies it (an Australian citizen is taken to be ordinarily resident; a New Zealand citizen on a special category visa is not time-limited). So the NSW surcharge question is a different definition from the one FIRB applies. That the FATA encoding's answer would differ for those two groups is **unverified** (not checked against that encoding).
- **Income Tax Assessment Act 1997, Subdivision 118-B** (main residence exemption) and the cost base: `../../../../income-tax-assessment-act-1997/`. That stamp duty paid on a home forms part of its cost base, and that the main residence exemption asks a question like, but not the same as, the scheme's residence requirement, is **unverified** (from general knowledge, not from the texts).
- **First home owner grant (NSW)**: `../../../first-home-owner-grant-and-shared-equity-act-2000/`. Not yet encoded. The Duties Act's "first home owner" (s 71) is its own definition, not the grant's.

## What the Act turns out to say

1. **The concessional band and the shared equity concession cannot be computed from the deposit.** The corpus dropped the formulas themselves; only their where-clauses survive:
   - **s 78A(2) and (2A).** The text says the duty "is to be calculated in accordance with the following formula—". What follows is not a formula but "where— N ... V ... D ...". So the band from $800,000 to $1,000,000 for a home, and from $350,000 to $450,000 for a vacant block, answers `not covered`.
   - **s 78B(3).** It says "duty is chargeable as follows—", then gives only "D ... R ... E ... C ...". So the shared equity concession answers `not covered`.
   - **s 78AA(3)-(5).** The same loss; the section is out of scope.

   Nothing was filled in from memory. A `formulas.md` sidecar transcribed from an authorised rendering would close the gap. Asserted.
2. **The s 32 table is the 2019-20 table, not the current one.** Section 33AC(1) adjusts every minimum and maximum threshold amount, and the $3,040,000 premium threshold, "for the year commencing on 1 July 2020, and each subsequent year":
   - by the Sydney CPI ratio A/B, to 3 decimal places;
   - rounded to the nearest $1,000;
   - never falling below the year before.

   Section 33AD resets each base amount to "the sum of all fixed rate amounts determined for the preceding threshold ranges", rounded to the dollar with 50 cents rounded down. The deposited base amounts are exactly what s 33AD gives from the deposited thresholds: the sums $1,307.50, $9,112.50 and $41,017.50 round down to $1,307, $9,112 and $41,017. Asserted. Two consequences:
   - the table answers directly only for a liability arising between 1 July 2019 and 30 June 2020;
   - for a later year the seat asks for that year's published amounts, and accepts them only if each is a multiple of $1,000 and not below its 2019-20 amount, which every s 33AC result must be. Asserted.

   The heading of s 32A still says "exceeding $3,000,000", while its text says $3,040,000. The s 32A note's premium base amount of $152,502 is the s 32 duty on $3,040,000. Asserted.
3. **The scale is not quite continuous at $81,000.** Range 3 at its maximum gives $1,307.50, but range 4's base amount is $1,307, because s 33AD(3) rounds 50 cents down. So $81,001 costs $1,310.50, only $3.00 more for the first part of $100 above, not $3.50. The other boundaries meet exactly ($175, $415, $9,112, $41,017). Asserted.
4. **The deposited first home thresholds apply only to agreements from 1 July 2023.** Under Schedule 1 cl 147, the First Home Buyer Legislation Amendment Act 2023 applies to agreements entered into, and transfers that occur, on or after 1 July 2023. The Act as in force before it "continues to apply" to the others. The deposit does not say which provisions that Act changed, so every earlier agreement answers `not covered`, whatever its value. Asserted. As a result, s 70's start date of 1 July 2017 is encoded but never decides a covered case.
5. **The two caps differ in kind:**
   - **eligibility** needs a dutiable value "less than" $1,000,000 for a home, or $450,000 for a vacant block (s 74(3));
   - **nil duty** needs one "not more than" $800,000, or $350,000 (s 78A(1)).

   So an $800,000 home pays nothing, an $800,001 home falls into the missing band, and a $1,000,000 home is not eligible at all. Under the hypothetical amounts H, it pays the full general rate: $39,872. The cap tests the dutiable value, which is the greater of the price and the value (s 21). A home bought for $750,000 but worth $820,000 is in the band. Asserted.
6. **Joint buyers:**
   - **All must be eligible** (s 73A(1)).
   - **The 5% allowance.** Section 71(7) lets buyers who are not first home owners hold up to 5% between them. A parent taking 5% leaves the purchase eligible; at 10% the purchase falls to the shared equity concession (s 78B), which is not covered; at 60% (first home owners under 50%) it is not eligible at all.
   - **Joint tenants.** Section 14 makes joint tenants equal tenants in common, so a joint tenant who has owned a home always holds 50% or more. The purchase can then reach the shared equity concession at best.
   - **Citizenship.** Under s 73(6), a buyer who is neither a citizen nor a permanent resident is excused if a first home owner buying with them is one.

   Asserted.
7. **The 14-day condition runs from a date the Act does not define.** Under s 76A(2), an approval given in advance is conditional. If the residence requirement is not met, the applicant "must within 14 days after the end of the period allowed for compliance" give written notice and pay the relevant duty. The relevant duty is the full duty less any duty paid (s 76A(3)). Failing to is an offence (50 penalty units) and a tax default (s 76A(4), (5)).
   - **The reading.** The Act does not define "the period allowed for compliance". The encoding reads it as the period allowed to move in: 12 months after completion, or the longer period approved. So completion on 15 May 2025 gives a last day of 29 May 2026; with 18 months approved, 29 November 2026.
   - **Where it is doubtful.** For a buyer who moved in and left early, the period could be read otherwise.

   The residence requirement does not apply where, on the day of the contract, one buyer is in the Permanent Forces and each buyer is enrolled to vote in NSW (s 76(6)). Asserted, with traces for late notice and late payment.
8. **The spouse exemption needs all five conditions** in s 104B(1):
   - equal shares, or joint tenants, afterwards;
   - the couple's principal place of residence, or its intended site;
   - land used solely for residential purposes;
   - no other party;
   - for de facto partners, 2 years in the relationship (s 104B(1)(e), and the Dictionary's "de facto partner").

   **The s 104C concession.** Where only the use fails, s 104C reduces "the dutiable value of the land by the residential apportionment factor". The encoding reads that as taking the residential share off, so duty falls on the dutiable value times the non-residential factor: on a $400,000 half share with a factor of 0.2, $1,290. Section 104C(6) applies the general rate only. A $4,000,000 home with a factor of 0.9 pays $183,302 on $3,600,000, without the premium rate. Asserted.
9. **The spouse exemption and the first home scheme do not reach surcharge purchaser duty.** Section 104ZK(2) says the exemptions and concessions in Part 8 "do not ... apply in respect of surcharge purchaser duty". A foreign spouse taking a half share worth $500,000 from a citizen spouse pays no transfer duty (s 104B) but $45,000 surcharge purchaser duty. Asserted.
10. **Surcharge purchaser duty is 9% of the dutiable value, on the foreign share only** (s 104U(1), (2)). Joint tenants hold equal shares (s 104V, s 14), and only foreign transferees are liable (s 104R(2)):
    - a citizen buying with a foreign person owes none;
    - the foreign person's half of a $1,200,000 home bears $54,000.

    **The 9% rate's start date.** Schedule 1 cl 156 applies the 9% rate (as amended by the Revenue Legislation Amendment Act 2024) to transactions after its commencement, a date the deposit does not give. So a liability before 1 January 2025, the deposit's version date, answers `not covered`.

    **Comparison with WA.** The WA rate is 7% (WA baseline finding 8). Asserted.
11. **Vehicle duty is $3 per $100, or $1,350 plus $5 per $100 above $45,000 for a passenger vehicle** (s 265). The two meet at $45,000, so there is no step. Above it a passenger vehicle pays 5% at the margin: a $60,000 car $2,100, a $60,000 motor cycle $1,800. Every "part" of $100 counts: a $45,000.50 car pays $1,355.

    **Comparison with WA.** WA's sliding R% formula reaches 6.5% at $50,000 (WA baseline finding 6). NSW is flat at 3% to $45,000. A $30,000 car pays $900 in NSW and $1,050 in WA. Asserted.
12. **"Residential land" means three different things** in the parts encoded:
    - **s 32A(3)**, the premium rate: one dwelling, and not a "shop and dwelling";
    - **s 104A**, the spouse exemption: includes one dwelling and a shop;
    - **s 104I**, surcharge purchaser duty: "one or more dwellings", but not land used for primary production.

    So a house with a shop escapes the premium rate but can be exempt between spouses. Land with two dwellings bears surcharge purchaser duty but is not residential land for the premium rate. Asserted.
13. **The scheme has two cases and no third.** Sections 74(3) and 78A(1) speak only of property that "has a private dwelling built on it" and "a vacant block of residential land". A house under construction is neither plainly, and land with two or more dwellings falls to the multiple occupancy rules (s 74A, not encoded). Both answer `not covered`. Asserted.
14. **Section 273's $20 minimum is not encoded.** It makes any duty under this Act that would be less than $20 equal to $20, except under Chapters 7 and 8. Two points are unclear:
    - whether it reaches a Chapter 9 application (an application is not plainly "a transaction or an instrument");
    - whether it lifts an exempt nil to $20.

    It would change the answers only for land worth $1,500 or less, and vehicles worth $600 or less.
15. **Deadlines the encoding reads, not states:**
    - **"Within 3 months after the liability arises"** (ss 15, 16, 17, 104W) is taken to end on the same day three months on, or on that month's last day where it is shorter. So 30 November 2025 gives 28 February 2026 (90 days). The Interpretation Act 1987, which settles this, is not deposited.
    - **Vehicle duty has no period to pay.** It "becomes payable when the motor vehicle is registered" (s 264). This Act gives no period, so it is not a regulative rule. The s 262 statement must go "with the application", day 0, on pain of 100 penalty units.

    Asserted.
16. **An amendment the deposit cannot place.** Schedule 1 cl 150 says the "increase in amounts of duty effected by" the Treasury and Revenue Legislation Amendment Act 2023, Schedule 1[1]-[4], does not apply to a transaction before 1 February 2024. The deposit does not say which amounts those are. If any amount encoded here is among them, the answers for transactions before 1 February 2024 would be wrong. Not checked: the amending Act is not deposited.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au, and re-check every figure. In particular, check the s 78A thresholds, the 9% surcharge rate and the vehicle rates, which may have changed since 1 January 2025.
- Transcribe the formulas in s 78A(2) and (2A), s 78AA(3)-(5) and s 78B(3) into `../../registers/source-bundle/act-1997-123.formulas.md` from an authorised rendering. Then encode the concessional band and the shared equity concession (finding 1).
- Deposit the Chief Commissioner's s 33AF notices, or the Sydney CPI series, so that each year's amounts can be a dated table rather than inputs (finding 2).
- Deposit the Taxation Administration Act 1996 (interest, penalty tax, joint liability, objections) and the Interpretation Act 1987 (counting months) (findings 10, 15).
- Encode s 104ZKA and s 104ZKB (exempt permanent residents and retirement visa holders), s 104ZB and s 104C's factor (from the Register of Land Values), ss 32B and 32C, s 74A (multiple occupancy) and s 273.
- Settle the readings in findings 7, 8 and 15 against Revenue NSW rulings or decided cases. None was consulted.
- An independent test pass, and a check against Revenue NSW's calculators.
