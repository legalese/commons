# Stamp Duties Act 1923 (SA), with the First Home and Housing Construction Grants Act 2000: baseline encoding

> **Every text in this encoding is the Open Australian Legal Corpus text, not the official one, and it may be out of date.** South Australia's register (legislation.sa.gov.au) refused this repository's fetcher with a bot challenge, so the texts were taken from the corpus (CC BY 4.0) under the owner's ruling of 2026-10-24. Check legislation.sa.gov.au before relying on any answer.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18 and the brief for the tax-and-benefits encodings of 24 October 2026. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

The encoding has two layers:

- **A seat-neutral core** in the Acts' own actors and terms: the purchasers, the person who executed the instrument, the applicant for the grant, the objector, the Commissioner, the Treasurer and the Minister. Where the text says "must" or sets a deadline, the rule is regulative (`DEONTIC`, `PARTY ... MUST ... WITHIN ... HENCE ... LEST`). Computations are functions: the duty scale, the s 72 surcharge, the grant amount, the vehicle scale, interest and penalty tax.
- **A seat layer** (`sda-seat.l4`) that asks the buyer's questions with plain inputs. It builds the core's records and restates no rule.

Five instruments are brought into one encoding, as the task directs. The Act's s 71DD(12) and (13) adopt the First Home and Housing Construction Grants Act's "relevant interest", "home" and "new home". Section 71DD(3)(b)-(e) repeats the grant's criteria in ss 8A-11, and both Acts carry the same residence requirement of six months beginning within 12 months (s 71DD(4), FHOG s 12). It is the same buyer in the same transaction. The Stamp Duties Regulations 2013 set the concession card class Schedule 2 uses. The Taxation Administration Act 1996 supplies s 71DE's interest and penalty tax and the objection and appeal deadlines. Cross-folder IMPORT does not work, so all modules live in this folder.

| File | What it holds |
|---|---|
| `sda-common.l4` | Arithmetic and date helpers, the "not covered" answers, and the parties and acts of the duty rules |
| `fhog-terms.l4` | FHOG Act ss 3-6 (home, new home, residential property, relevant interest, owner, spouse, domestic partner), shared by the relief and the grant; the parties and acts of the grant rules |
| `taa-procedure.l4` | Core: TAA ss 25-27, 29-34, 82, 86, 87, 89, 92-95 |
| `sda-home.l4` | Core: s 2 (spouse, foreign person), s 20, s 60A, Schedule 2 clause 3(1)(b), s 71CB, s 71DD, s 71DE, s 72 |
| `fhog-grant.l4` | Core: FHOG ss 7-15, 17, 18, 18BB, 18C, 20, 21, 24, 25, 27, 28, 39, 40; Regulations 2015 reg 6 |
| `sda-vehicles.l4` | Core: ss 42A, 42B, Schedule 2 clause 2(1)-(4); Stamp Duties Regulations 2013 reg 14 |
| `sda-seat.l4` | Seat layer: 25 exported questions, each with `@desc` on every input, under `§` headings |
| `sda-cases-home.l4`, `fhog-cases.l4`, `sda-cases-vehicles.l4`, `taa-cases.l4` | Cases for the core modules |
| `sda-cases-seat.l4` | Cases for the seat layer, asked with plain answers |

The seat layer and its case file were written by two generator scripts, `gen_seat.py` and `gen_seat_cases.py`, in the session scratchpad (`au-sa-1/`). The scripts only spell out the long argument lists. The expected values were typed into them by hand.

## Edition

Every text is the Open Australian Legal Corpus text (version 7.1.0), not the official one, and may be out of date:

- **Stamp Duties Act 1923**: as at **2025-02-13** (scraped 2025-03-10), corpus version `south_australian_legislation:2025-02-13/1923.1569.un`, at `../../registers/source-bundle/stamp-duties-act-1923.txt`. The Current Titles list gives no version to compare.
- **First Home and Housing Construction Grants Act 2000**: as at **2025-02-13** (scraped 2025-03-10), `south_australian_legislation:2025-02-13/2000.25.un`, at `../../../first-home-and-housing-construction-grants-act-2000/registers/source-bundle/`. The Current Titles list of 22 September 2026 lists it at **4.12.2025**, so a later version exists and is not reflected here.
- **First Home and Housing Construction Grants Regulations 2015**: as at **2021-03-11** (scraped 2024-09-13), `south_australian_legislation:2021-03-11/2015.61.un`.
- **Stamp Duties Regulations 2013**: as at **2022-09-29** (scraped 2024-09-13), `south_australian_legislation:2022-09-29/2013.209.un`.
- **Taxation Administration Act 1996**: as at **2019-10-03** (scraped 2024-09-13), `south_australian_legislation:2019-10-03/1996.80.un`. The Current Titles list gives version 4.12.2025, so a later version exists.

The duty scale and the grant amounts are encoded as the deposited text states them. Nine formulas are missing from the Stamp Duties Act deposit and four from the FHOG Act deposit (each has a `.formulas.md` sidecar). Where a question needs one, the answer is an explicit `not covered`, and a case asserts it. These are the s 71DD(7) reduction, the s 71DB off-the-plan dutiable value, the s 42BA continuing-owner concession and the FHOG bonus grants.

**Inputs where the deposit is silent:**

- the "relevant day" of each Act (finding 3);
- the market rate for Taxation Administration Act interest (s 26(2)) and for grant instalment interest (reg 6(3));
- the Commissioner's approvals, opinions and determinations, each a fact (see Seat).

## Licence

CC BY 4.0, under the owner's ruling of 2026-10-24 ("On NT, Vic and SA, yes please go ahead"), recorded in each subject's `SOURCE-LICENSE.md`. This folder holds a copy of the Stamp Duties Act's. Attribution: *Based on content from the South Australian Legislation website. Sourced from the South Australian Legislation website at 10 March 2025. For the latest information on South Australian Government legislation, please go to www.legislation.sa.gov.au. State of South Australia, CC BY 4.0. Taken through the Open Australian Legal Corpus (Umar Butler / Isaacus, version 7.1.0, CC BY 4.0).* Every module header repeats it.

## Checks

`l4 run` on every `.l4` in the folder gives **0 errors and 0 warnings**, with **375 assertions written and 375 satisfied**.

| Case file | Assertions | `#TRACE`s (each with an `-- expect:` line, read and as expected) |
|---|---|---|
| `sda-cases-home.l4` | 129 | 4: breaches by the person who executed the instrument (s 20) and by the purchasers (s 71DE); the Commissioner's advice and the purchasers' payment pending; the Commissioner's s 72(5) refund pending |
| `fhog-cases.l4` | 102 | 5: the Commissioner's decision pending; breaches by the applicant (s 20(2), criterion 5, s 39); the Treasurer's decision pending |
| `sda-cases-vehicles.l4` | 48 | none |
| `taa-cases.l4` | 39 | 2: the Minister's determination pending; the appeal still open |
| `sda-cases-seat.l4` | 57 | none |

The seven modules also run clean on their own. A copy of `sda-cases-home.l4` with one expected value altered was run as a control, and the runner reported that assertion as failed.

Expected values were worked by hand from the deposited texts. The arithmetic of the Schedule 2 clause 3(1)(b) and 2(1) scales, s 72(3) and TAA ss 25-27 and 30-32 was also done in an independent calculator, `au-sa-1/hand.py`, written from the statutory words. Dates were counted on a calendar. No value was copied from the encoding's output.

## Seat

**The buyer of a home or a car in South Australia.** This includes the first home buyer who applies for the s 71DD relief and the first home owner grant. The questions are the ones that buyer asks:

- "What duty do I pay on my home?"
- "Does a first home buyer of a new home or of land pay nothing?"
- "What must we do to keep that relief, and what happens if we don't?"
- "Is the grant payable, and how much?"
- "By when do I apply, and when must I repay it?"
- "What is the duty on registering my car?"
- "How do I object or appeal?"

The text puts duties on the Commissioner (to advise, to refund, to decide, to authorise payment), the Treasurer and the Minister (to give notice of a decision on an objection). They are officials, so none gets a seat. Their duties appear in the regulative rules for what they mean to the buyer. The seller has no duty in these provisions beyond executing the transfer, which s 20(4) treats the same way for every party who executed it. So there is no second seat.

How each default was applied:

- **The Act alone, with the instruments that set its numbers.** Departed from, as the task directs: the FHOG Act, both Regulations and the Taxation Administration Act are brought in for the reasons given under Method.
- **The actors the text names.** Followed.
- **A judgment handed to someone else is answered conditionally.** Followed. Each of these is a fact the buyer states, and the answer holds if it is so:
  - the Commissioner's satisfaction or opinion (s 60A(2), s 71CB(3), s 71DD(5), (6), (9), FHOG ss 4(b), 7(1a) through s 18BB, 8A(2), 13(3), 14(6), 20(1));
  - the Commissioner's approval of a shorter residence period or a longer completion period;
  - the Commissioner's determination that land is residential land (s 72(8));
  - the Commissioner's discretion to charge interest and penalty tax (s 71DE(2)(f));
  - the Minister's permission for a late objection or an appeal without payment (TAA ss 87, 93(2)).
- **The Act's definitions worked out; borrowed terms asked as facts.**
  - Worked out: home, new home, residential property, relevant interest, owner, spouse and domestic partner (FHOG ss 3-6), shared residence (s 71CB(1)), foreign person for an individual (s 2(14)(a)(i)), value of the property conveyed (s 60A), value of a motor vehicle (s 42B(1)), eligible transaction and new home transaction (FHOG ss 3, 13).
  - Asked as facts: Australian citizen, permanent visa and special category visa (Commonwealth Acts); new residential premises (GST Act s 40-75(1)(b)); domestic partner under the Family Relationships Act 1975 (SDA s 2); commercial motor vehicle, trailer, heavy vehicle and the s 38 reduced-fee entitlement (Motor Vehicles Act 1959).
  - Departure: the seat asks "has a buyer or partner owned residential property" as one fact rather than working out a relevant interest for each earlier property. The core's `the interest is a relevant interest (s 5)` works it out for one interest and is tested.
- **One case is the text's natural unit.** Followed: one contract or transfer, one grant application (one eligible transaction), one vehicle application, one decision.
- **The Act's own terms, each with a plain gloss.** Followed. The comments quote the statutory words.
- **Operative sections in; machinery out.** Followed.

**Group facts.** Where the text counts purchasers or applicants ("the purchasers", "each of the applicants", "at least 1 of"), the facts are stated for the group in those terms. A separated spouse, who does not count (s 71DD(11), FHOG s 6(2)), is excluded in the wording of each `@desc`.

## Scope

**In.**

*Stamp Duties Act 1923:*

- s 2: spouse, domestic partner (a fact), and foreign person for an individual (s 2(14)(a)(i));
- s 20(1), (2), (4)-(7): pay and stamp within two months of execution, or within two months of a later event, as a regulative rule; the $10,000 offence and its defence;
- s 60A(1), (2): value of the property conveyed;
- Schedule 2 clause 3(1)(b): the general scale, nine bands per $100 or part, as a table;
- s 71CB: a transfer of a shared residence, or of a vehicle's registration, between spouses or domestic partners, current or former;
- s 71DD(1)-(3), (6), (8), (9), (11), (11a), (12), (13): the relief on a new home or vacant land to build on;
- s 71DD(4), (5) with s 71DE: the residence requirement as a regulative rule, and the duty, the s 20(2) deadline, and interest and penalty tax when the relief ends;
- s 72(1)-(5), (8): the 7% foreign ownership surcharge, with its refund as a regulative rule;
- ss 42A, 42B and Schedule 2 clause 2(1)-(4): the registration component as two tables (non-commercial; commercial or trailer) with the $5 minimum; exemptions 4, 6 and 11; the policy of insurance component with exemptions 2, 6 and 8.

*Stamp Duties Regulations 2013:* reg 14 (the State concession card class).

*First Home and Housing Construction Grants Act 2000:*

- ss 3-6: the shared terms;
- s 7: entitlement and the market value cap;
- ss 8, 8A, 9, 10, 11: criteria 1 to 4;
- s 12 with s 20: the residence requirement and payment in anticipation, as a regulative rule (notify and repay within 14 days);
- s 13: eligible transaction, commencement date, completion and consideration;
- s 14(5), (6) with ss 17 and 24: the application period, as a regulative rule;
- s 15: all interested persons join;
- s 18(1), (4a), s 18BB and s 18C: the amount;
- s 21(2)-(4): conditions;
- s 25 with ss 27 and 28: objection within 60 days and review within 60 days, as a regulative rule;
- s 39: repayment and penalty, as a regulative rule;
- s 40: recovery.

*First Home and Housing Construction Grants Regulations 2015:* reg 6 (interest on repayment by instalments).

*Taxation Administration Act 1996:*

- ss 25-27, 29: interest, with the market rate an input;
- ss 30-34: penalty tax;
- ss 82, 86, 87, 89 and ss 92-95: objection and appeal, as a regulative rule, with the s 93 payment condition.

**Out.**

- s 71DB, off-the-plan apartments (its dutiable value formula is missing; `not covered`).
- s 42BA, transfers to or from a continuing owner (its formula is missing; `not covered`).
- s 71DD(7) reductions (formula missing; `not covered`), and s 71DD(9a).
- Landholder duty (Part 4); ss 71C-71CC, 71CBA, 71D-71DC, 71E-71F.
- s 72(6), (7): trusts, and becoming a foreign person later.
- Corporations and trusts as foreign persons.
- The other Schedule 2 clause 2(2) and 2(4) exemptions; Regulations 2013 regs 10A and 10B.
- ss 42C and 42CA (refunds).
- FHOG s 6A (HomeBuilder); ss 12A, 12B and 18B-18BAC (the closed bonus grants, and the construction and seniors grants, whose formulas are missing); s 13A and s 18(2) (special eligible transactions of 2008-2009); ss 13(6), 16, 22 and 23; s 5(4)-(6) and Regulations 2015 regs 4 and 5.
- Grant amounts for commencement dates before 15 October 2012, and for transactions other than new home transactions before 1 July 2014 (`not covered`).
- TAA Parts 3, 4, 6-9 except as named; Supreme Court and SACAT procedure.

There is no South Australian requirement ledger and no South Australian scenario life, so no ledger line is closed and no life event is cited. The jurisdiction README was not edited.

## Links to other encodings

Cross-folder IMPORT does not work. These are links in the notes only.

- **Australian Citizenship Act 2007 (Cth):** `../../../../australian-citizenship-act-2007/encodings/`. "Australian citizen" in SDA s 71DD(13) and s 2(14)(a)(i)(A), and in FHOG ss 3 and 9 (finding 7). An input here.
- **Migration Act 1958 (Cth):** `../../../../migration-act-1958/encodings/`. "Permanent resident" (a permanent visa, s 30; a New Zealand citizen with a special category visa, s 32) in SDA s 71DD(13) and s 2(14), and FHOG ss 3 and 9. An input here.
- **Income Tax Assessment Act 1997 (Cth):** `../../../../income-tax-assessment-act-1997/encodings/`. The income tax treatment of the first home owner grant is **unverified (general knowledge only)**: it is commonly understood not to be assessable income, but no deposited text was checked.
- **A New Tax System (Goods and Services Tax) Act 1999 (Cth):** `../../../../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/`. New residential premises, s 40-75(1)(b) (FHOG s 3, substantially renovated home). An input here.
- **Motor Vehicles Act 1959 (SA):** `../../../motor-vehicles-act-1959/`. The s 38 reduced-fee entitlement (Schedule 2 clause 2(2) exemption 11, clause 2(4) exemption 6), commercial motor vehicle and trailer. Inputs here.
- **Family Relationships Act 1975 (SA):** `../../../family-relationships-act-1975/`. "Domestic partner" in SDA s 2. An input here.
- Model encodings: `../../../../wa/duties-act-2008/encodings/baseline-2026-10/` and `../../../../wa/first-home-owner-grant-act-2000/encodings/baseline-2026-10/`.

## What the Acts turn out to say

1. **A first home buyer of a new home, or of vacant land to build on, pays no duty at any value on a contract made on or after 6 June 2024 (s 71DD(2)(b)).** The $650,000/$700,000 (home) and $400,000/$450,000 (land) thresholds bind only contracts made before then (s 71DD(2)(a), (3)(f)). A $1,000,000 new home in 2026 pays nothing instead of $48,830. A $720,000 new home on 5 June 2024 gets no relief; on 6 June 2024 it pays nothing. Asserted.
2. **The phase-out band before 6 June 2024 cannot be answered from the deposit.** Section 71DD(7)'s two formulas are missing (the formulas sidecar, lines 1233 and 1239). A contract before 6 June 2024 for a new home over $650,000 and under $700,000, or for land over $400,000 and under $450,000, answers `not covered`. Asserted.
3. **"The relevant day" is not in the operative text, and the two Acts define it differently.** Section 71DD(13) of the Stamp Duties Act says "the day on which the Statutes Amendment (Budget Measures) Act 2025 is assented to by the Governor". FHOG s 11(4) says "the day on which section 4 of" that Act "comes into operation". Both are inputs, as the task directs. The deposited legislative histories, which are editorial notes rather than law, record Act No 4 of 2025 as assented on 13.2.2025, with s 11(2), (7) and (8) (SDA) and s 4 (FHOG) commencing that day. The cases use 13 February 2025. The texts are "as at 2025-02-13", the same day. Asserted for 12 and 13 February 2025.
4. **Reading: the relief reaches the foreign ownership surcharge only on a contract before the relevant day.** Section 71DD(11a) withholds relief from the surcharge on contracts "entered into on or after the relevant day". Section 72(4) makes the surcharge "duty payable on the instrument". So, before the relevant day, "no duty will be payable" under s 71DD(2) is read as covering the surcharge too. A foreign co-buyer of half a 2026 new home, whose partner is a citizen, pays $22,400 (7% of $320,000). On a contract of 1 December 2024, nothing. Asserted.
5. **From the relevant day, any earlier relevant interest in residential property bars both the relief and the grant, even if it was never lived in.** Before that day, it bars only if lived in for six continuous months (s 71DD(3)(e)(ii), FHOG s 11(3)(b)). An investment flat never lived in bars a 2026 buyer. On a contract of 1 December 2024 it did not. Asserted.
6. **Reading: "the commencement date of the contract" in s 71DD(3)(e) is not defined in the Stamp Duties Act.** It is read as the date the contract was entered into, the FHOG Act's meaning for a contract (s 13(4)(a)).
7. **The FHOG Act defines "Australian citizen" by the Australian Citizenship Act 1948 (Cth) (s 3).** That Act was repealed and replaced by the Australian Citizenship Act 2007. The Stamp Duties Act cites the 2007 Act (s 71DD(13), s 2(14)). Both are treated as the same fact, citizenship now. The legislative history's note that references "may be obsolete" applies.
8. **The grant has no market value cap for a commencement date on or after 6 June 2024.** Section 7(1a) caps it at $575,000 from 17 September 2010 to 14 June 2023 and at $650,000 from 15 June 2023 to 5 June 2024. After that it applies only an amount "prescribed by regulation", and the deposited Regulations 2015 (as at 2021-03-11) prescribe none. Asserted. A later regulation would change this.
9. **"Spouse" and "domestic partner" are not shared between the Acts.** Section 71DD(12)-(13) adopt only "relevant interest", "home" and "new home". The Stamp Duties Act's own s 2 gives "spouse" (legally married) and "domestic partner" (the Family Relationships Act 1975 meaning). The FHOG Act's s 6 gives "spouse" and "domestic partner" (living together in a close personal relationship, s 3). Both exclude a separated spouse in the same words (s 71DD(11), FHOG s 6(2)). Asserted.
10. **The grant is $15,000, or the consideration if less, and only for a new home transaction (s 18(1)).** For a contract made on or after 1 July 2014 that is not a new home transaction there is no grant (s 18(4a)). For an owner builder or building contract that is not for a new home, s 18(1)(b) gives no amount after 30 June 2014 either. A $9,500 building contract gets $9,500. Earlier commencement dates are `not covered` (the 2012 statutory date and the lost bonus grant formulas). Asserted.
11. **Reading: vehicle exemption 6 ("to the extent that ad valorem stamp duty has already been paid") reduces the registration component by that duty.** The $5 minimum of clause 2(1)(c) is applied first. $300 paid takes a $940 component to $640; $1,000 paid takes it to nil. Asserted.
12. **On vehicles:**
    - Commercial vehicles and trailers have no fourth band: they pay $3 per $100 above $2,000 where other vehicles pay $4 per $100 above $3,000. At $45,000 that is $1,320 against $1,740.
    - A transfer of registration carries no policy of insurance component (s 42B(1d)(b)). A second-hand car at $17,000 pays $620.
    - A Commonwealth pensioner or State concession card with reduced public transport fares frees only the policy component (exemption 8, reg 14).
    - The s 38 reduced-fee entitlement frees both components (exemption 11, policy exemption 6).
    
    Asserted.
13. **Reading: periods of months are calendar months.** None of the Acts says how a period of months is counted, and the Acts Interpretation Act 1915 is not deposited. A period ends on the same day of the month, or on the last day of a shorter month. Two months after 31 December 2025 is 28 February 2026. Asserted.
14. **The residence requirement's deadlines are worded differently.** Section 71DD(4)(a) (new home) says "commences within 12 months of the date on which the conveyance or transfer occurs", read as including the anniversary. Section 71DD(4)(b) (land) says "commences before whichever ... occurs first" of 12 months after a home on the land can first lawfully be lived in and 36 months after the transfer, read as the day before that date. Land transferred on 1 August 2026, with a home usable on 15 March 2028, must be occupied by 14 March 2029. With a home usable on 1 December 2028, by 31 July 2029. FHOG s 12 says "commencing within 12 months after completion". An approved longer completion period (s 71DD(5)(b)) is taken as months from the transfer. Asserted.
15. **Reading: FHOG s 39(2) and (3) are separate powers, each capped at the amount to be repaid.** Where a grant was paid on a false statement and then not repaid, the most is twice the grant: $30,000 on a $15,000 grant. Asserted.
16. **Reading: FHOG s 20(3)(a), "the end of the period allowed for compliance", is the end of a residence period begun on the last day allowed.** With completion on 1 August 2026, that is 1 February 2028. If it becomes apparent on 10 March 2027 that the buyers will not move in, they must notify and repay by 24 March 2027 (s 20(2)). Failing that is an offence with a maximum of $5,000 (s 20(4)), and a penalty up to the grant (s 39(3)). Asserted, with the breach traced.
17. **Reading: interest and penalty tax when the relief is lost.**
    - TAA interest is "calculated on a daily basis" (s 25(1)). It is read as the yearly rate (market rate plus 8%, s 26) divided by 365, at a constant rate.
    - Under s 71DE(2)(f) it runs from the date of the transfer, as if the duty had been unpaid since then.
    - Penalty tax is 25%, or 75% if deliberate (s 31(1)). It is reduced by 80% for disclosure before an audit or by 20% during one, and may be raised by 20% for obstruction (s 31(2)). It is nil where the Commissioner is satisfied it was not deliberate and reasonable care was taken (s 30(2)). Both interest and penalty tax are nil under $20 (ss 27, 32).
    - $29,580 paid 200 days late at a 4.1% market rate gives $1,961.19 interest and $7,395 penalty tax.
    - All of this is at the Commissioner's discretion, and the Commissioner may remit either (ss 29, 34).
    
    Asserted.
18. **The duty when relief is lost is "calculated according to the rates in force as at the date on which the conveyance or transfer occurred" (s 71DE(2)(d)).** The encoding has only the deposited Schedule 2, as at 2025-02-13. A later change to the scale is not here. The duty payable is chargeable "for the purposes of section 20" from the event that ends the relief (s 71DE(2)(e)), so it is due within two months of that event. A home vacated on 15 January 2027 means duty due by 15 March 2027. Asserted, with the breach traced.
19. **Section 20(4) falls on "any person who executed the instrument, or on whose behalf it was executed", the buyer included.** The maximum is $10,000, and the instrument stays valid (s 20(7)). There is a defence for having delivered it to another party in the reasonable expectation that they would stamp it (s 20(6)), which is the usual conveyancing case. Asserted, with the breach traced.
20. **Reading: the s 72(5) refund's "not more than 12 months after the acquisition" includes the anniversary.** No time is set for applying, or for the Commissioner to refund once an application is made. A permanent visa granted 11 or 12 months after acquiring, while still holding the interest, brings a refund; one granted 12 months and a day after does not. Asserted.
21. **To appeal against a duty assessment to the Supreme Court, at least half the duty must first be paid, unless the Minister permits (TAA s 93).** The appeal must be made within 60 days of service of the determination (s 94(1)). Alternatively, if the objection is undetermined after 90 days, an appeal may be made at any time on 14 days' notice to the Commissioner (s 94(2)). Asserted.

## What would need doing before this is worth relying on

- Replace every text with the current official one from legislation.sa.gov.au, including the FHOG Act and Taxation Administration Act versions of 4.12.2025. Restore the s 71DD(7), s 71DB and s 42BA formulas from the authorised rendering, and recheck every figure.
- Settle the "relevant day" of each Act from the official record (finding 3), and confirm the readings in findings 4, 6, 11, 13, 14, 15, 16, 17 and 20 with the owner or RevenueSA practice.
- Deposit the Acts Interpretation Act 1915 (periods of months), and the current market rate notices.
- Encode the out-of-scope parts a buyer can meet: s 71DB, s 42BA, s 72(7), corporations and trusts as foreign persons, and the remaining vehicle exemptions.
- Check against RevenueSA's calculators and guidance; none were consulted.
