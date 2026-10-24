# Stamp Duty Act 1978 (NT), with the Taxation Administration Act 2007 (NT): baseline encoding

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18 and the brief for the tax-and-benefits encodings of 24 October 2026. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

The encoding has two layers:

- **A seat-neutral core** in the Acts' own actors and terms: the conveyee, the applicant for registration, the transferor, the Commissioner, the Registrar, the decision maker and the person affected by a decision. Where the text says "must" or sets a deadline, the rule is regulative (`DEONTIC`, `PARTY ... MUST ... WITHIN ... LEST`). Computations, such as the duty, a concession amount, penalty tax or interest, are functions.
- **A seat layer** (`sda-seat.l4`) that asks the individual's questions with plain inputs. It builds the core's records and restates no rule.

The Taxation Administration Act 2007 is brought in as a second module (`taa-procedure.l4`) in the same folder. TAA s 5(3) says each taxation law "must be read together with this Act as a single Act", and cross-folder IMPORT does not work. The TAA subject folder holds no encoding of its own; this one encodes the TAA procedure for both duty assessments and first home owner grant decisions.

| File | What it holds |
|---|---|
| `sda-common.l4` | Arithmetic and date helpers, the "not covered" answers, and the parties and acts of every regulative rule (shared by both Acts) |
| `sda-home.l4` | Core: dutiable value, the conveyance scale, who is liable, s 9 lodging and paying, the Part 5 Division 2 concessions with s 88A and s 90B, the grant interactions, the notices of failure to occupy, s 90D, s 91, Schedule 2 items 6(d), 6(e) and 7 |
| `sda-vehicles.l4` | Core: vehicle dutiable value, Schedule 1 cl 5, s 92A, Schedule 2 item 23, ss 57, 59(3), 59A, 61 |
| `taa-procedure.l4` | Core: TAA ss 21(4), 27, 34-36, 39, 41-43, 107-117, 128 |
| `sda-seat.l4` | Seat layer: 39 exported questions, each with `@desc` on every input, under `§` headings |
| `sda-cases-home.l4`, `sda-cases-vehicles.l4`, `taa-cases.l4` | Cases for the three core modules |
| `sda-cases-seat.l4` | Cases for the seat layer, asked with plain answers |

The seat layer and its case file were written by two generator scripts, `gen_seat.py` and `gen_seat_cases.py`, in the session scratchpad (`au-nt-1/`). The scripts only spell out the long argument lists. The expected values were typed into them by hand.

## Edition

- **Stamp Duty Act 1978**: reprint **REPS013**, as in force at **1 July 2025**, deposited at `../../registers/source-bundle/Stamp-Duty-Act-1978-NT-current-reprint-REPS013.txt` (retrieved 2026-10-19).
- **Taxation Administration Act 2007**: reprint **REPT039**, as in force at **1 July 2024**, deposited at `../../../taxation-administration-act-2007/registers/source-bundle/Taxation-Administration-Act-2007-NT-current-reprint-REPT039.txt` (retrieved 2026-10-19). This reprint is more than two years old, so an amendment that commenced after 1 July 2024 is not in it.
- **Dates covered.** The reprint's endnotes record that Schedule 1 was last amended by No. 13, 2017, s 11, which commenced on 1 July 2017. What that amendment changed is not in the deposit. TAA s 26(1) assesses a liability under the law "as in force when the liability arose". So the deposited scale is applied only to conveyances first executed, and certificates issued, **on or after 1 July 2017**. Anything earlier answers `not covered`. The home concessions as they stood before the 2010 amendments (s 102, 4 May 2010) also answer `not covered`.
- **No regulation is deposited.** These figures are therefore treated as follows:
  - the threshold amount uses the Act's own $650,000 (s 88(1));
  - the first home owner discount uses the s 88(1)(b)(ii) fallback, not a prescribed amount;
  - no class is treated as prescribed under Schedule 2 item 23(a)(iii);
  - the TAA market interest rate (s 35(2)) is an input.
  
  A prescribed figure would change the answers.
- **Formula.** The formula in Schedule 1 cl 1(2)(a) lost its superscript in conversion (finding 1). The deposit is not altered.

## Licence

Owner's ruling, 24 Oct 2026 (Michael): the NT terms permit reproduction but are silent on adaptation. As for Canada, the texts may be quoted in L4 encodings in Legalese Commons, keeping the NT attribution and the unofficial-copy notice.

The ruling is recorded in `SOURCE-LICENSE.md` of both `stamp-duty-act-1978` and `taxation-administration-act-2007`, and this folder holds a copy of the former. Every module header carries the unofficial-copy notice and the Northern Territory's ownership of copyright. No Northern Territory arms are used.

## Checks

`l4 run` on every `.l4` in the folder: **0 errors, 0 warnings**, and **274 assertions written, 274 satisfied**.

| Case file | Assertions | `#TRACE`s (each with an `-- expect:` line, read and as expected) |
|---|---|---|
| `sda-cases-home.l4` | 128 | 7: four breaches by the conveyee, three obligations of the Commissioner pending |
| `sda-cases-vehicles.l4` | 33 | 2: breaches by the applicant (s 57) and by the transferor (s 59(3)) |
| `taa-cases.l4` | 48 | 4: decision maker's notice pending, NTCAT application still open, breaches by the taxpayer (s 128 and s 43) |
| `sda-cases-seat.l4` | 65 | none |

The five modules (`sda-common`, `sda-home`, `sda-vehicles`, `taa-procedure`, `sda-seat`) also run clean on their own.

A copy of the seat case file with one expected value altered ($29,700 to $29,705) was run as a control. The runner reported both affected assertions as failed.

Expected values were worked by hand from the deposited texts. The arithmetic of Schedule 1 cl 1(2), cl 5, s 88(1) and TAA ss 27 and 34 was done in an independent calculator, `au-nt-1/calc/hand.py`, written from the statutory words. No value was copied from the encoding's output.

## Seat

**The individual buyer and taxpayer.** That is the conveyee of a home in the Territory, who is liable for the duty under s 50(a), or the applicant registering a motor vehicle, who is liable under s 57(1). As taxpayer, or as applicant for a first home owner grant, this person is also "the person affected" by a decision under TAA Part 11. The questions are the ones that person asks:

- "How much duty is on my home or my car?"
- "Which concession do I get, if any?"
- "Is my purchase exempt?"
- "When must I lodge, pay and notify?"
- "When must I object, and where can I appeal?"
- "What penalty tax applies?"

The core also holds the seller's duty to notify the price of a vehicle within 14 days (s 59(3)). The seat asks it as "I sold my vehicle" and treats it as the same individual's question, not a second seat.

The text puts duties on two other parties: the Commissioner (to reassess, to refund, to decide an objection) and the Registrar. Both are officials, so neither gets a seat. Their duties appear as regulative rules, encoded for what they mean to the buyer.

How each default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The figures are in the Act. The TAA is brought in, as the task requires, because it is the procedure for every duty assessment and grant decision. No regulation is deposited (see Edition).
- **The actors the text names.** Followed.
- **A judgment handed to someone else is answered conditionally.** Followed. Every "the Commissioner is satisfied that ..." in Part 5 is a fact the buyer states, so the answer holds if the Commissioner is so satisfied. This covers the age and occupancy exemptions, special reasons, a qualifying-home declaration (s 90AA(2)), the s 89AAB(11) relationship-breakdown exemption, the penalty tax grounds (TAA s 41) and the extension of time to object (TAA s 111).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: dutiable value (s 4AB), unencumbered share value (s 4AC), the concession amounts and threshold amount (s 88(1)), period for occupancy and prescribed period (s 88(1)), qualifying home and established home (ss 88(1), 90(10), 90AA), the vehicle dutiable value (s 59(1)), electric motor vehicle (s 92A(5), as one fact), relevant decision (TAA s 107).
  - Asked as facts: the First Home Owner Grant Act terms that s 88(1) borrows (Australian citizen, permanent resident, home, relevant interest, residential property, first home owner grant entitlement, owner builder, comprehensive home building contract); new residential premises under the GST Act s 40-75(1)(b); marriage and de facto relationship, orders and binding financial agreements under the Family Law Act 1975; Special Disability Trust (Social Security Act 1991); the veteran's pension rate (Veterans' Entitlements Act 1986 ss 22(4), 24(4)); the NT concession cards (finding 3); building contractor (Building Regulations 1993).
- **One case is the text's natural unit.** Followed: one conveyance (one dutiable instrument), one certificate of registration, one decision.
- **The Act's own terms, each with a plain gloss.** Followed. The comments quote the statutory words.
- **Operative sections in; machinery out.** Followed.

**Departures:**

- **Group facts.** Where a section counts conveyees ("each of the conveyees", "at least one of the conveyees"), the facts are stated for the group in those terms, rather than as a list of conveyees.
- **Readings.** The text leaves some points open; the readings taken are recorded under the findings: s 88A (finding 2), the occupancy of several conveyees (findings 13 and 20), the anniversary in s 91 (finding 19), the order of the s 41(2) exceptions and the 14-day minimum (finding 16), the day count for interest (finding 16), and the grant ending the Territory home owner discount (finding 11).

## Scope

**In.**

*Stamp Duty Act:*

- s 4: conveyee and consideration;
- s 4A(1): unencumbered value, an input;
- s 4AB(1): dutiable value;
- s 4AC: shares in property;
- ss 5, 6 and Schedule 1 cl 1(2) and (3): the conveyance scale, and joint tenants plus $5;
- s 50(a) and s 9(7): who is liable;
- s 9(1), (3), (3A), (5), (6): lodging and paying, as regulative rules;
- Part 5 Division 2:
  - s 88: the amounts, threshold amount, period for occupancy and prescribed period;
  - s 88A: the sunset;
  - ss 89, 89AA, 89AAB, 89AAC, 89A, 90 and 90AA: conditions and windows;
  - ss 90A and 90AB: the grant reassessments, as regulative rules;
  - s 90B: one concession only;
- s 102: the start of the 2010 amendments;
- the notices of failure to occupy (ss 89(3), 89AA(6), 89AAB(7), 89A(3), 90(3), 90D(5)) with the 50 penalty unit fine, and the Commissioner's duty to reassess (ss 89(4), 89AAB(4)(b), 89A(6)-(7), 90(4), 90D(8)), as regulative rules;
- Part 5 Division 2A, ss 90C and 90D: the exemption for a new home bought from a building contractor;
- Part 5 Division 3, s 91: relationship breakdown, with the s 91(3) refund as a regulative rule;
- Schedule 2 items 6(d), 6(e) and 7;
- vehicles:
  - s 57(1) with s 58(1): pay before registration, as a regulative rule;
  - s 59(1), (1A), (2): dutiable value, GST not deducted;
  - s 59(3) and (5): the transferor's 14-day notice, as a regulative rule;
  - s 59A: refund, as a regulative rule;
  - s 61 and s 92A(3): the declaration;
  - Schedule 1 cl 5: $3 per $100 or part;
  - s 92A: the electric vehicle concession;
  - Schedule 2 item 23(a), (b), (e), (j)(i), (j)(v) and (k).

*Taxation Administration Act:*

- s 21(4): the 5-year limit on reassessment, with the Stamp Duty Act provisions that lift it;
- s 27: rounding down to 5 cents;
- ss 34-36: interest, with the market rate an input;
- ss 39, 41-43: penalty tax, with s 43 as a regulative rule;
- ss 107, 109-111, 113-117: objections, review and appeal, for both duty decisions and first home owner grant decisions, as a regulative rule;
- s 128: no suspension of recovery, as a regulative rule.

**Out.**

- Corporate reconstructions, partnerships, landholder duty (Part 3 Division 8A), trusts, declarations of trust and discretionary trusts, options, insurance duty, family farms, managed investment schemes, leases, partitions (cl 1(4)-(10)), statutory vesting.
- The replacement-and-option savings rules of ss 97A, 102(2), 106, 109, 111, 112, 115 and 116.
- Guardians (ss 89(7), 89AA(7) and the like), Housing Act schemes, and the s 89AAB(4)(a) non-disposal reassessment.
- Schedule 2 item 23(c), (d), (f)-(i), (j)(ii)-(iv) and (l), and s 57(2) (hire vehicles).
- TAA Parts 2, 4 (except as named), 6-10, 13 and 14, the MRA royalty branch of Part 11, and NTCAT and Supreme Court procedure.

**The Northern Territory levies no land tax.** Unlike Western Australia's `land-tax-assessment-act-2002`, there is no land tax and no principal place of residence exemption from land tax to encode.

**Rates concessions are not in statute here.** The Rates Act 1971 was not sourced, and council rates and their concessions are council and administrative matters (see the jurisdiction README).

There is no requirement ledger for the Northern Territory and no NT scenario life, so no ledger line is closed and no life event is cited.

## Links to other encodings

Cross-folder IMPORT does not work. These are links in the notes only.

- **First Home Owner Grant Act 2000 (NT):** `../../../first-home-owner-grant-act-2000/encodings/baseline-2026-10/`.
  - Whether a conveyee "has been paid, is entitled to or will become entitled to a first home owner grant" is an input here, and is answered there. It drives ss 89AA(2)(k), 89AAC, 89A(1)(ga), 90(1)(fa), 90A and 90AB.
  - That encoding records that FHOG Act s 51 applies TAA Part 11 to grant decisions. This encoding's `taa-procedure.l4` encodes that path, including the s 115(2) NTCAT-only rule.
- **Social Security Act 1991 (Cth):** `../../../../social-security-act-1991/encodings/baseline-2026-10/`. Special Disability Trust (Schedule 2 item 6(e); also Schedule 1 cl 2(3)).
- **Veterans' Entitlements Act 1986 (Cth):** `../../../../veterans-entitlements-act-1986/encodings/baseline-2026-10/`. Eligibility for a pension at the s 22(4) extreme disablement adjustment rate or the s 24(4) special rate (Schedule 2 item 23(k)).
- **A New Tax System (Goods and Services Tax) Act 1999 (Cth):** `../../../../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/`. New residential premises, s 40-75(1)(b) (s 90AA(1)(b)). GST is included in consideration, unencumbered value and vehicle dutiable value (ss 4(1), 4A(1), 59(1A)).
- **Family Law Act 1975 (Cth):** `../../../../family-law-act-1975/encodings/baseline-2026-10/`. Orders under Parts VIII and VIIIAB, and binding financial agreements under Parts VIIIA and VIIIAB (s 91; s 89AAB(11)).

## What the Act turns out to say

1. **Schedule 1 cl 1(2)(a) reads "0.06571441 x V2", and it means V squared.** The superscript was lost in conversion. At $525,000 (V = 525) the formula gives $25,987.53425625, and 4.95% gives $25,987.50. The two parts of the scale meet within 3.4 cents, which confirms V². Read as V × 2, the formula would give about $7,944 at $525,000. The deposit is not altered. The proper record would be a `.formulas.md` sidecar transcribed from the authorised rendering; that was not made, because no law is fetched in this step. Asserted.
2. **Section 88A closes the whole of Part 5 Division 2 for conveyances first executed after 30 June 2021.** Section 88A says: "Except if otherwise expressly provided, this Division applies to conveyances first executed on or before 30 June 2021."
   - Section 89AAB(1) only says when the Territory home owner discount begins ("on or after 8 February 2019"). It does not expressly provide that the Division applies after 30 June 2021.
   - Sections 88A and 89AAB were inserted by the same Act (No. 22, 2019, ss 9 and 11). Section 88A was then amended by No. 28, 2020, s 8.
   - Section 89A has no date of its own.
   - So the encoding reads s 88A as closing both the Territory home owner discount and the senior, pensioner and carer concession with conveyances first executed on 30 June 2021.
   - The first home owner concession (before 4 December 2012), the first home owner discount (24 May 2016 to 6 May 2019) and the principal place of residence rebate (before 8 February 2019) had already closed by their own words.
   - **For a 2026 purchase, none of these concessions applies.**
   
   The contrary reading, that s 89AAB(1) displaces s 88A, is one constant (`READING: s 89AAB(1) is an express provision displacing s 88A`). Division 2A (s 90D) is not "this Division", so s 88A does not touch it. Asserted, for 30 June and 1 July 2021 and for a 2026 first home buyer.
3. **The concession cards in s 89A are administrative.** Section 89A(12) defines the NT Pensioner and Carer Concession Card only as "a concession card administered for the Northern Territory Pensioner and Carer Concession Scheme by the Territory". The Northern Territory Concession Scheme Card is not defined. Who may hold either card is not in statute, so holding one is an input.
4. **The live relief for a buyer now is the s 90D exemption, and it is broader than the old concessions.** It covers a conveyance first executed from 1 July 2022 to 30 June 2027 for a detached new home bought from a building contractor who bought the lot from its developer and paid duty on it. The whole duty is exempt.
   - There is no value cap and no first-home condition. Any individual buyer qualifies, provided at least one buyer is 18 or older and at least one is a citizen or permanent resident.
   - A repeat buyer at $2,000,000 is exempt, where the duty would otherwise be $99,000.
   - It fails if the builder bought the land from someone other than the developer, or if the contract replaces one signed before 1 July 2022.
   
   Asserted.
5. **The rates above $525,000 apply to the whole dutiable value, so the scale has cliffs.** One dollar over $3,000,000 adds $24,000.0495 of duty. One dollar over $5,000,000 adds $10,000.0575. Asserted.
6. **Duty is rounded down to a multiple of 5 cents (TAA s 27).** $412,345 gives $17,358.4909, which is payable as $17,358.45. Asserted.
7. **The deposited Schedule 1 is applied only from 1 July 2017.** That is the commencement of No. 13, 2017, s 11, the last amendment the endnotes record. The amount of the first home owner concession, which closed in 2012, can therefore never be computed from this deposit, though its conditions can be tested. Asserted.
8. **Section 90B in practice.** On 1 March 2019 a first home buyer of an established home at $400,000 met both the first home owner discount and the Territory home owner discount, and each equalled the whole duty of $16,514.3056. The concessions give the same benefit, so the Commissioner determines which (s 90B(3)(b)), and nothing is payable either way. A senior from interstate at $600,000 in 2020 got the Territory home owner discount ($18,601) rather than the senior concession ($10,000), and paid $11,099. Asserted.
9. **The Territory home owner discount was not limited to first home buyers.** It turned on having had no Territory residential property in the previous 24 months (s 89AAB(2)(d)). Its own definition limits it to a dutiable value not over the $650,000 threshold. At $650,000 the buyer paid $13,574; at $650,001, the full $32,175. Asserted.
10. **Above the threshold, the first home owner discount had no amount from 1 January 2017.** The $10,000 limb for values above $650,000 (s 88(1), definition (c)) ran only to 31 December 2016. A $700,000 established first home in November 2018 paid the full $34,650. Asserted.
11. **The grant and the concessions:**
    - The senior, pensioner and carer concession (s 89A(1)(ga)), the principal place of residence rebate (s 90(1)(fa)) and the first home owner discount (s 89AA(2)(k)) are all closed to a buyer who is paid, or entitled to, a first home owner grant. The first home owner concession (s 89) is not.
    - The Territory home owner discount is denied by s 89AAC for grants on transactions that commenced from 1 January 2015 to 6 May 2019, and reassessed away by s 90AB(2) once a grant is paid. Reading: it is encoded as not surviving the grant.
    - Section 90A(5) lets the s 90A reassessments be made "even if the time limit for reassessment ... has passed". Section 90AB has no such words, so a s 90AB reassessment stays inside the 5-year limit of TAA s 21(4).
    
    Asserted.
12. **Failing to live in the home.** Each concession and the s 90D exemption require written notice to the Commissioner within 30 days after it first becomes apparent that the buyer will not live in the home as required. The maximum penalty is 50 penalty units; the value of a penalty unit is not deposited.
    - With several buyers, ss 89AA, 89AAB and 90D need notice only when all of them fail, and one notice is enough.
    - Section 89A puts the duty on each buyer who fails.
    - The Commissioner must then reassess, even after the 5-year limit, unless there are special reasons (ss 89(4), 89AAB(4)(b), 89A(6), 90(4), 90D(8)).
    - Section 89AA has no such subsection. A first home owner discount can be recovered only by an ordinary reassessment within TAA s 21(4).
    
    Asserted, with traces for notice in time, late notice and the pending reassessment.
13. **Section 90D with several buyers.** Section 90D(3)(c) requires "all conditions in subsection (2)" to be met, which is read as requiring each buyer to live in the home. Yet s 90D(6)(a) requires notice only "if all conveyees fail". The reading follows (3)(c); the Commissioner may vary the requirement for special reasons (s 90D(2)(i)). Not asserted beyond the single-occupancy facts.
14. **An exempt conveyance must still be lodged within 60 days.** Section 9(3)(c) excuses only instruments exempt under Schedule 2 items 9 to 13 and 15. So a s 90D, s 91, item 6 or item 7 conveyance must still be lodged, and duty on a dutiable one is due by the last day for lodgement unless the notice of assessment fixes a later date (s 9(5)). Asserted, including the breach traces.
15. **Challenging a decision:**
    - Object in writing, stating the grounds in full, within 60 days after the notice of the decision (TAA s 110). The decision maker may extend the time on a written application if satisfied there is a reasonable excuse (s 111).
    - A reassessment can be objected to only to the extent it increases the duty (s 109(2)).
    - A late objection obliges the decision maker to nothing (s 113(1)).
    - After a disallowance, apply to NTCAT or appeal to the Supreme Court within 60 days, not both. A first home owner grant decision goes to NTCAT only (s 115(2)).
    - Objecting does not stop recovery (s 128): the duty stays payable by its due day.
    
    Asserted, with traces.
16. **Penalty tax and interest (TAA ss 34-36, 41-43):**
    - Penalty tax is 25% of the default. It is 10% where reasonable care was taken; 75% for intentional disregard or concealment, and 95% for both; and nil where the default was beyond the taxpayer's control and was put right.
    - Reading: the s 41(2) exceptions have no stated order. Nil is taken first, then 75% or 95%, then 10%.
    - The Commissioner may reduce penalty tax by up to 80% for full disclosure before any investigation, or by up to 20% for full cooperation with one. There is no reduction where information was concealed. The Commissioner may also remit penalty tax under s 44, which is not bounded here.
    - Nothing is imposed under $20 (s 42).
    - There are at least 14 days to pay (s 43). Reading: a notice naming fewer than 14 days still leaves 14.
    - Interest is the market rate (an input) plus 8%, worked daily. Reading: the annual rate is divided by 365. Nothing is charged under $20 (s 36). $12,500 unpaid for 73 days at 4.35% + 8% is $308.75.
    
    Asserted.
17. **The s 92A cap of $1,500 never bites.** The first $50,000 of an electric vehicle's dutiable value is exempt, and at $3 per $100 the duty on $50,000 is exactly $1,500. A $60,000 electric car pays $300; a $40,000 one pays nothing. Asserted.
18. **Vehicle exemptions an individual meets:**
    - Registering a car again in your own name, for example on moving to the Territory, is exempt (item 23(a)), unless it seats 12 or more and you never paid duty on it.
    - A trailer or caravan of 4.5 t or less is exempt; at 4.6 t it is not.
    - A veteran eligible at the Veterans' Entitlements Act s 22(4) or s 24(4) rate is exempt for a non-commercial vehicle.
    - The item 23 exemptions need a s 61 declaration; the electric vehicle concession does not (s 92A(3)).
    
    Asserted.
19. **Section 91 (relationship breakdown).** The order or agreement must be made "within 12 months after the date of the conveyance". Reading: an order made on the anniversary counts. A binding financial agreement counts only for a conveyance made after the irretrievable breakdown. Duty paid before the order must be refunded (s 91(3)). Asserted.
20. **Section 89(1)(i), "the conveyee or conveyees will occupy", is read as requiring each conveyee to occupy.** Section 90(8A) had to be added to relax the same words in s 90 from 28 April 2015. The senior concession has its own relaxation in s 89A(11AA), and one senior who moves in is enough. Asserted for s 89A.

## What would need doing before this is worth relying on

- Deposit the later reprints, if any, of both Acts, and the Stamp Duty and Taxation Administration Regulations: the threshold amount, prescribed discount amounts, the item 23(a)(iii) class and the market interest rate. Then replace the inputs and fixed figures with them.
- Deposit or transcribe the authorised rendering of Schedule 1 cl 1(2)(a) as a formulas sidecar (finding 1).
- Deposit the Schedule 1 in force before 1 July 2017 if earlier conveyances are to be answered. Deposit the Penalty Units Act to turn penalty units into dollars.
- Settle the readings in findings 2, 13, 16, 19 and 20 with the owner or Territory Revenue's practice.
- Encode the savings rules for replacement contracts and options (ss 97A, 102(2), 106, 109, 111, 112, 115, 116), guardians and Housing Act schemes, partitions and leases.
- Check against Territory Revenue Office calculators and rulings. None were consulted.
