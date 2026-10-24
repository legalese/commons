# Rates Act 2004 and Land Tax Act 2004 (ACT): baseline encoding for the owner of a residential property

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case the encoding does not reach answers `not covered` with the reason, and a test asserts each reason. The questions themselves return it for commercial, rural or airport land, a proposed unit subdivision, an owner that is a corporation or trustee, a quarter outside 2026-27, and a parcel with no unimproved value given (in the cores, for rates, land tax and the surcharge alike). The catch-all question "Is my other question covered" returns it for the rest: a special disability trust as owner, the Commissioner's decision on a compassionate exemption, the affordable community housing exemption and the valuation, as well as the matters above.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no human gate. One independent check (24 October 2026) raised six issues, all corrected (see Corrections); a full independent test pass is still wanted.
**Not for public use as advice.**

**Land tax is encoded here, in the Rates Act 2004's folder.** Land tax is measured by the Rates Act's average unimproved value: Land Tax Act s 9(4) says "AUV means the average unimproved value of the parcel of land under the Rates Act 2004". The stable `l4` cannot IMPORT across encoding folders, so the two Acts are encoded together, sharing one s 13A. **`subjects/au/act/land-tax-act-2004/` has no encoding folder of its own**; this is its encoding. Encoding both in one place also answers "what do I pay each year on my property" in one set of questions.

The encoding has six files:

- **`rates-shared.l4`**: what both cores use, so neither defines a name the other also defines. It holds the year 2026-27 and its quarters, days and months, the rounding rules (Rates Act s 74, Land Tax Act s 40, DI2026-150 s 4, DI2026-152 s 5) and the marginal tables' arithmetic. It also holds the **Rates Act s 13A average unimproved value**, the monthly interest of Rates Act s 21 and Land Tax Act s 19 (worded alike, read differently: findings 13 and 25), the parties and acts of the regulative rules, the not-covered answers, and the Taxation Administration Act objection (ss 100-102, one regulative rule).
- **`rates-core.l4`**: the seat-neutral core for the Rates Act with DI2026-150 and DI2026-144. It covers rates, levies, payment and instalments, the pensioner rebate and deferral. It has five regulative rules: ss 17-19 payment, s 61 rebate application, s 67 notice of a change, s 46 deferral application, s 55 payment after revocation.
- **`landtax-core.l4`**: the seat-neutral core for the Land Tax Act with DI2026-152. It works out the position for a quarter (payable, put off by s 8A(3), or which exemption), the first taxed quarter after moving out (from that position), the quarter's amount, the foreign ownership surcharge, the 2-year period after a death, and penalty tax under TAA div 5.2 as s 19A applies it. It has three regulative rules: s 14 notice of a change, s 17 payment, s 11D(3) application to extend.
- **`rates-seat.l4`**: the owner's seat. It asks 26 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the cores' records from plain answers and restates no rule. An input with the same name means the same fact in every question.
- **`rates-cases-owner.l4`** and **`landtax-cases-owner.l4`**: the cases.

The rules in the cores use the Acts' own actors and terms ("the owner", "an eligible person", "a pensioner", "a relevant person", "the personal representative", "the commissioner"). Where the texts say "must" or "may", or set a deadline, there is a regulative rule (`DEONTIC`), nine in all. The computations (AUV, rates, levies, rebate, deferral interest, land tax, surcharge, interest, penalty tax) are functions.

No earlier encoding of either Act existed to keep. The ACT has no requirement ledger, so no ledger line is closed. No scenario life raised these provisions; the cases are the encoder's.

## Edition

| Instrument | Register id | Version | Deposited at |
|---|---|---|---|
| Rates Act 2004 | A2004-3 | Republication No 45, effective 26 December 2025 | `../../registers/source-bundle/A2004-3.txt` |
| Taxation Administration (Amounts Payable—Rates) Determination 2026 | DI2026-150 | notified 30 June 2026, commences 1 July 2026 | `../../../taxation-administration-amounts-payable-rates-determination-2026/registers/source-bundle/DI2026-150.txt` |
| Rates (Age 65 or Over—Rates Deferral) Determination 2026 | DI2026-144 | notified 29 June 2026, commences 1 July 2026 | `../../../rates-age-65-or-over-rates-deferral-determination-2026/registers/source-bundle/DI2026-144.txt` |
| Land Tax Act 2004 | A2004-4 | Republication No 34, effective 26 December 2025 | `../../../land-tax-act-2004/registers/source-bundle/A2004-4.txt` |
| Taxation Administration (Amounts Payable—Land Tax) Determination 2026 | DI2026-152 | notified 30 June 2026, commences 1 July 2026 | `../../../taxation-administration-amounts-payable-land-tax-determination-2026/registers/source-bundle/DI2026-152.txt` |
| Taxation Administration Act 1999 | A1999-4 | Republication No 52, effective 26 November 2025 | `../../../taxation-administration-act-1999/registers/source-bundle/A1999-4.txt` |

**Every number comes from the 2026 determinations, not from the Acts.** That covers the fixed charges, the percentage-rate tables (DI2026-150 Tables 1 and 2, DI2026-152 Table 1, encoded as tables), the $750 rebate cap, the $458 emergency services levy, the $70 safer families levy, the $133 PFES rebate, the 75% determined percentage, the 0.75% surcharge and the quarterly apportionment. The determinations commence on 1 July 2026 and revoke earlier ones that are not deposited. Determinations under TAA s 139 are remade each 1 July. So the encoding answers for 1 July 2026 to 30 June 2027 only, and a land tax quarter outside it is `not covered`.

Four figures are not deposited and are inputs:

- the interest rate for overdue rates and land tax (Rates Act s 21, Land Tax Act ss 19 and 19A; a TAA s 139 determination);
- the TAA s 26 market rate component, for deferred rates (s 48(3));
- the Rates Act s 18(3) discount rate (see finding 5);
- the value of a penalty unit (Legislation Act 2001 s 133; the republication notes give $160 for an individual).

The Taxation Administration Act is brought in because both Acts are tax laws under it (Rates Act s 1 note). It supplies the right to object (ss 100-103) and the penalty tax that Land Tax Act s 19A applies (div 5.2). It also supplies the offence of not notifying (s 67(2)) and the interest rules that ss 20, 20A and 21 of the Rates Act and s 19(3) of the Land Tax Act displace (TAA s 25). TAA s 27 (no interest under $20) does not apply to rates or land tax: s 27(2)(b)-(c).

**Attribution.** All six texts: © Australian Capital Territory, from the ACT Legislation Register (https://www.legislation.act.gov.au/), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changed: converted to plain text by Legalese Commons, and quoted in part in the comments of the `.l4` files. Not endorsed by the ACT Government. Unofficial versions; the authorised versions are the PDFs on the register. The terms record for the Rates Act is the copy of `SOURCE-LICENSE.md` beside this file; each other instrument's is in its own subject folder.

## Checks

| Modules | Case file | Assertions |
|---|---|---|
| `rates-shared.l4`, `rates-core.l4`, `landtax-core.l4`, `rates-seat.l4` | `rates-cases-owner.l4` | 116 written, 116 satisfied |
| `rates-shared.l4`, `landtax-core.l4`, `rates-seat.l4` | `landtax-cases-owner.l4` | 100 written, 100 satisfied |

In addition, 7 `#TRACE`s carry an `-- expect:` line. Six are breaches by the owner: not paying by the payment date or the 1st instalment; missing the 2nd instalment; not giving the s 67 notice; not paying the deferred debt the day after revocation; not telling the Commissioner under Land Tax Act s 14; not paying land tax by the payment date. The seventh is an obligation still pending: the Commissioner's duty under s 46(2) to make the deferral determination, for which no period is stated. Each was read and matches its expectation.

`l4 run` on all six files: 0 errors, 0 warnings (2026-10-24, again after the corrections listed below). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the texts, with the arithmetic in the comment above the assertion.

## Seat

**The owner of a residential parcel or unit in the ACT.** That may be an owner-occupier (including a pensioner and an owner aged 65 or over), or an owner who rents a home out, leaves it empty or moves out. They ask:

- "What are my 2026-27 rates and levies on my house or unit?"
- "Am I eligible for the pensioner rebate, how much is it, and what must I report and by when?"
- "Can I defer my rates (as a pensioner, for hardship, or at 65 or over with 75% equity), what interest runs, and when is the debt due?"
- "If I rent out my home or move out, do I pay land tax, from which quarter, and how much each quarter?"
- "What must I tell the Commissioner, by when, and what follows if I do not?"
- "By when can I object?"

The Commissioner's decisions and satisfactions appear as what they mean for the owner. They are inputs: substantial hardship, separation for good, a home unfit to live in or fit again, an extension of the 2-year period after a death, a compassionate exemption, and what the Commissioner is satisfied of for penalty tax. In the cores, the owner, the owner's agent, the personal representative and the commissioner are parties to the regulative rules.

**No second seat.** The texts in scope put duties only on the owner. Land Tax Act s 14 also binds the owner's agent and, after a death, the personal representative, as a "relevant person". They are parties to the s 14 rule, and the personal representative's one question (the s 11D(3) deadline) is in the owner's seat. The Commissioner is an official and gets no seat.

The 2026-10-18 defaults:

- **The Acts, with the instruments that set their numbers.** Those are the three 2026 determinations. The Taxation Administration Act is brought in for objection, interest and penalty tax. Both Acts are encoded together because land tax borrows the Rates Act AUV (see Method).
- **The actors the text names:** the owner, an eligible person, a pensioner, a relevant person, the personal representative, the commissioner.
- **Judgments left to others are answered conditionally:** the deferral answer is "the commissioner must make a deferral determination, on the grounds ...", which binds once the Commissioner is satisfied. The Commissioner's satisfactions are facts, as listed above.
- **The texts' own definitions are worked out from facts:** average unimproved value, AUVRU, base value, rateable days, eligible person, pensioner (pars (a)-(c)), liability for rates, rented, tenancy agreement, foreign individual. Borrowed terms are asked as facts: the Commonwealth pensions and cards, "special rate pensioner", "domestic partner", "principal place of residence", "equity", Australian citizen, permanent visa, "ordinarily resident", unit entitlement. Paragraphs (d)-(g) of "pensioner" and (b)-(c) of "eligible person" are each asked as one fact, as the brief allows.
- **One case:** one parcel (or unit) for one year, and for land tax one parcel for one quarter.
- **The texts' own terms,** quoted in the comment above each rule.
- **Machinery out:** valuation (pt 2), the commissioner's powers of assessment, certificates and statements (ss 76-77, 41-42), fees, regulations, commencement and revocation of instruments.

Departures, recorded here:

- The rebate question works out the owner's liability from the parcel's rates and levy. Its amount is the same whether or not part of the rates is deferred ("rates ... includes any rates deferred", ss 63(6), 64(6)); how it is split against a deferred part (s 65) is a separate question.
- The surcharge question asks only who occupies the parcel; the facts for ss 11B-11I, 13 and 15 are held at "no". It is asked by a foreign individual: for an owner who is not one it answers 0 before anything else, and the unimproved values are not needed.
- The unit questions do not distinguish a units plan registered during 2026-27 (s 29(2)): the unit owner is taken to pay under s 29(4) for the year.

## Scope

**In:**

- **Rates Act 2004:**
  - s 13A; s 14(1)-(3); s 15 (finding 28); s 16; s 17; s 18(1) (finding 5); s 19 (with s 17, one regulative rule); s 20; s 20A(1); s 21; s 29(3)-(5) (a residential unit); s 45; s 74;
  - div 7.2: s 46(1)-(2) and (5) (a regulative rule), s 48, s 49, s 51, s 52(1), s 55(2) (a regulative rule);
  - div 7.3: s 60, s 61 (a regulative rule), s 62, s 63, s 64, s 65, s 67 (a regulative rule), s 69;
  - ss 70-72 (objections);
  - sch 1 ss 1.1(1), 1.3, 2.1, 2.1A, 2.1B, 3.2.
- **DI2026-150:** s 4, s 5(1)(a)(i)-(ii) and (b)(i)-(ii), Tables 1 and 2, s 6, s 7(1)(a), s 9, s 10.
- **DI2026-144:** s 4.
- **Land Tax Act 2004:**
  - ss 7, 8, 8A (with (3) where an owner moves out, finding 26), 9, s 10(1)(a)-(b);
  - ss 11A, 11B, 11C, 11CA, 11D (with (3), a regulative rule), 11G, 11H, 11I;
  - s 13 (the decision as a fact); s 14 (a regulative rule); s 15; s 17 (a regulative rule);
  - s 17A (foreign individual), ss 17D, 17E, 17F;
  - s 18A; ss 19, 19A; s 27(3), (4) and (6); s 38; s 40.
- **DI2026-152:** ss 4, 5, 6 and Table 1, s 7.
- **Taxation Administration Act 1999:** s 26 (the market rate component, an input), s 27(2), div 5.2 (ss 30-35 and table 34, as Land Tax Act s 19A(4) applies it), s 67(2), ss 100-103.

**Out, each answering `not covered`** (asserted in the case files):

- returned by the questions themselves, and by "Is my other question covered":
  - commercial land (DI2026-150 Table 3, the city centre levy, the commercial PFES levy in Table 4)
  - rural land (and its land tax exemption, s 10(1)(d))
  - airport land (pt 5A)
  - div 5.2 proposed unit subdivisions
  - land owned, wholly or partly, by a corporation or trustee (Rates Act s 20A(2), Land Tax Act ss 16 and 27(5))
  - a quarter or year other than 2026-27
- returned by the questions only: a parcel with no unimproved value given (rates, the AUV, land tax, the surcharge)
- returned by "Is my other question covered" only:
  - a special disability trust as owner (Rates Act s 45 par (d) of "eligible person", ss 46(2)(b), 64(5)); its trustee answers "a corporation or trustee" in the other questions
  - the decision on a compassionate exemption (ss 12-13), which the land tax questions take as a fact
  - the affordable community housing exemption (s 13A)
  - the valuation process (pt 2)

**Out, not asked:**

- Rates Act: deferral without application (s 47); amendment of a deferral (s 50); notice and timing of revocation (ss 53-54, 59); instalments after revocation and the s 55(4) balance; s 56 interest after revocation (s 21, encoded, applies); s 58 information; s 66, s 68; exemptions and remissions (ss 41-44); the s 46(6) joint-owner discretion; the rebate for a special disability trust (s 64(5)).
- Land Tax Act: s 10(1)(c), (e)-(k) and s 11 (exemptions for housing bodies, retirement villages, nursing homes, development leases); s 11E-11F decisions (inputs); foreign corporations and trusts (ss 17B-17C); remission (ss 34-37).
- TAA: s 103 permissions, remission of interest and penalty tax, review by the ACAT.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social Security Act 1991** (`../../../../social-security-act-1991/`). A "pensioner" under Rates Act s 45(a) is "a person to, or for whom, a pension, allowance or benefit is being paid under the Social Security Act 1991 (Cwlth) and who has been given a pensioner concession card under that Act". Pars (d) borrow that Act's s 4 "partner". "Special disability trust" is defined by its s 1209L (Rates Act dictionary). Whether a person is paid such a payment and holds the card is that Act's question; here it is an input.
- **Veterans' Entitlements Act 1986** (`../../../../veterans-entitlements-act-1986/`). These are that Act's terms, and inputs here: "service pensioner" (s 45(b)); the card for treatment of all injuries and diseases, the Gold Card (s 45(c)); the partner (s 5E), dependant (s 11) and s 86 cases (pars (e)-(f)); and the special rate pensioner (pt 2, s 24).
- **Military Rehabilitation and Compensation Act 2004** (`../../../../military-rehabilitation-and-compensation-act-2004/`). These are that Act's terms, and inputs here: the card for treatment of all injuries and diseases (s 45(c)); the wholly dependent partner (s 5) and s 284(1) case (par (g)); and the special rate disability pension (ch 4 pt 6, s 199).
- **Income Tax Assessment Act 1997** (`../../../../income-tax-assessment-act-1997/`). For an owner who rents a home out, the rates, levies and land tax on it are outgoings incurred in gaining assessable rental income, deductible under s 8-1 (general deductions), apportioned where only part of the home is rented. For an owner-occupier they are private and not deductible. Not encoded here.

## What the Acts turn out to say

1. **The average unimproved value includes the current year's valuation, though s 13A says "the 5 years immediately before".** Section 13A(1)(g) averages the unimproved value "over the 5 years immediately before the particular year". The s 11(3) example averages, for "the year beginning 1 July 2025", the values "as at 1 January 2021, 1 January 2022 and 1 January 2023 ... 1 January 2024 ... 1 January 2025". By s 10(2) the value as at 1 January 2025 is the value "for the financial year immediately following", that is for 2025-26 itself. The encoding follows the example: for 2026-27, the values as at 1 January 2022 to 2026. Asserted, including the example's $236,000.
2. **"P (or percentage rate)" is an amount, but the Acts multiply by it.** Rates Act s 14(2) and Land Tax Act s 9(3) charge "FC+(AUV×P)". DI2026-150 s 5(1)(b) and DI2026-152 s 6(b) make P "the amount per year listed in column 2", and the column gives "$977.70 plus 0.4545% of the part of the base value that is more than $300 000". Read literally, AUV × P would multiply the AUV by a dollar amount. The encoding reads AUV × P as the column 2 amount for the base value; AUVRUP (= AUVRU × P) likewise.
3. **The tables are continuous.** In DI2026-150 Tables 1 and 2 and DI2026-152 Table 1, each row's base amount equals the row before at its top: for example 0.2842% × $150,000 = $426.30, and $3,155.85 + 0.5071% × $250,000 = $4,423.60. No cliff like the duty tables'. Asserted for every row.
4. **The levies on a unit are read as a fixed charge per unit.** Sch 1 s 1.1(1) imposes the levy "of the fixed charge ... for a parcel", and s 1.3 the safer families levy "for a parcel". Sch 1 s 2.1 applies ss 28-29 "as if a reference to rates included a reference to a levy", and s 28(2)(a) makes "a reference to a parcel ... in relation to the assessment or payment of rates ... a reference to a unit". READING: each residential unit bears the $458 and the $70. Asserted.
5. **No discount rate and no interest rate are determined.** Section 18(1)(a) lets an owner who pays the year in full, with no arrears, pay "the amount of the rates less the discount rate", "determined under the Taxation Administration Act, section 139". DI2026-150 determines none, so none is applied. Section 21's interest rate, which "the Minister may determine", is not in DI2026-150 or any deposited instrument; it is an input.
6. **How s 63 and s 64 meet is read, not stated.** Section 64(1)(b) applies the capped rebate to a grandfathered person (s 63) whose s 63 rebate "is less than or equal to the amount of the rebate cap under this section". READING: that is the full $750, not a joint owner's part, and where both sections apply the person has the greater. A joint tenant with $500 under s 63 last year therefore keeps $500, where s 64 alone would give $375. Asserted. Above $750, s 64 does not apply: $900 last year gives $900. Asserted.
7. **Section 60(2)(b) says two things at once.** Where some joint owners cannot contribute, the liability is what each payer would bear if they "were the sole owners ... as tenants in common in equal shares; and ... the value of their interests ... were increased proportionately". READING: the payers share equally.
8. **The rebate cap does not follow the liability.** Section 60(2) makes a joint owner whose co-owners cannot contribute liable for the whole rates. Section 64(4) still cuts the cap to "the part of the rebate cap" proportional to the owner's interest, with no counterpart of s 60(2). A joint tenant (2 owners) on $1,000 of rates whose co-owner cannot pay has a liability of $1,000 and a formula rebate of $500, but is capped at $375. Asserted.
9. **The safer families levy has no rebate; the emergency services levy has its own.** Sch 1 ss 2.1A and 2.1B apply pt 7 to the levies "other than section 63 ... and section 64". Sch 1 s 3.2 gives a separate PFES rebate, "PFES rebate × (LL)/(levy) × (D)/(days in year)", whose "levy" excludes "the safer families levy". So a pensioner pays the $70 in full and gets $133 off the $458, with no lesser-of test. Encoded; asserted at $133, $72.88 for 200 days, and $66.50 for a joint tenant.
10. **"Equity" is not defined, and DI2026-144 is oddly numbered.** Section 46(2)(f)(ii) turns on "the owner's or owners' equity in the parcel", which neither the Act nor DI2026-144 defines. It is asked as a percentage of the parcel's value. DI2026-144 runs s 1-4 and then "12 Revocation". It revokes "section 6 of Taxation Administration (Amounts Payable—Rates) Determination 2024 (DI2024-172)", not a 2025 instrument, so the 75% may have stood since 2024. Section 46(10) defines an owner's "income" "in the way determined by the Minister"; no such determination is deposited, and income is used only in s 58.
11. **The 65-or-over ground is only for owners who are not pensioners.** Section 46(2)(f), like (c), opens "if the owner, or each owner, is not a pensioner". A pensioner aged 70 with 90% equity defers under (a), not (f). A pensioner and non-pensioner couple have (d) but never (f), even where the partner is 70 with 90% equity. Equity of exactly 75% qualifies ("not less than"). Asserted.
12. **Deferred rates bear the market rate only, by a method not stated.** Section 48(3) charges interest "at the market rate component determined under the Taxation Administration Act, section 26", without TAA s 26(3)'s 8% premium. The method is not stated. READING: simple interest by the day: $2,452.55 at 3.6% for a year is $88.29. Asserted.
13. **Overdue rates may bear compound interest.** Section 21(1)(d) charges each month's interest "on the total amount of overdue rates that are unpaid". The dictionary says "rates includes the total of ... interest payable in relation to the rates", and sch 1 s 2.1(1)(d) applies pt 4 to the levies. READING: earlier months' interest is part of the total, so interest compounds monthly. A month is one twelfth of the yearly rate, and a part month counts as a whole month (s 21(2), the Fred example). $1,000 two months late at 9.6% is $16.06, not $16.00; $458 of levy, $7.36. Asserted. Land Tax Act s 19 is worded alike but reads differently (finding 25).
14. **Land tax falls on a home left empty, not only on one rented out.** Section 9(1) imposes land tax "on each parcel of rateable land that is residential land". Of the exemptions, none covers a home no one lives in, unless it is unfit (s 11I) or in the first quarter after moving out (s 11B). The jurisdiction README describes the tax as one "on a home that is rented out". An empty former home is taxed from the second quarter after the owner leaves. Asserted.
15. **No penalty tax and no $20 floor on an individual's rates.** Rates Act s 20A(1) says TAA div 5.2 "does not apply to unpaid overdue rates", save for a corporation or trust. TAA s 27(2)(b)-(c) disapply the rule that no interest is payable under $20, so $19.62 of interest is payable. Asserted. Land tax differs: s 19A(4) applies TAA div 5.2 where the owner fails to tell the Commissioner under s 14.
16. **The four quarters do not add up to the year.** DI2026-152 s 4 scales each "determined amount" to the quarter, and the instrument's example rounds the FC to "$448.15". READING: the FC and P parts are each scaled and rounded to the cent (s 40(1)), then added. A house with an AUV of $430,000 rented all year pays $1,338.41, $1,338.41, $1,309.31 and $1,323.86: $5,309.99, a cent short of the year's $5,310. Asserted.
17. **A unit's land tax is charged on the whole building's value.** For rates, residential units have their own Table 2. For land tax there is one Table 1, and a unit's base value is the AUVRU of the whole parcel (DI2026-152 s 3), shared by unit entitlement (s 27(6)). A unit with 1% of the entitlement in an $8,000,000 building pays the top marginal rate on the building: $98,700 × 1% + $1,778 = $2,765 a year ($696.93 in October). Asserted.
18. **A foreign owner's home is free of the surcharge, but a home lent rent-free is not.** Section 17E(2)(a) excepts from the surcharge land exempt under s 10, "other than section 10 (1) (a) (vii)", which is s 11H (nil or nominal rent). A foreign owner living in the home pays nothing. One who lets family live there rent-free pays no land tax but pays the 0.75% surcharge ($812.88 in October on an AUV of $430,000). Asserted.
19. **A non-citizen who lives in Australia is not a "foreign individual".** Section 17A defines a foreign individual as one who "is not (a) an Australian citizen; or (b) a permanent resident; or (c) ordinarily resident in Australia". READING: none of the three. A temporary visa holder ordinarily resident in Canberra is not a foreign individual and pays no surcharge. Asserted.
20. **"The 1st quarter after the date" and "rented" in s 11B are read.** The s 11B exemption is "for the 1st quarter after the date the owner stops occupying the parcel". It does not apply "if the parcel of land is rented by a tenant".
    - READING: a quarter beginning on the day itself is not "after" it.
    - READING: "rented" means rented on that quarter's 1st day (s 8(2)).

    Moving out on 1 October 2026 and leaving the home empty, the first taxed quarter begins 1 April 2027. Asserted.
21. **Section 19A has no part-month rule.** Section 19(2) says a part of a month counts as a whole month; s 19A(3), for interest where the owner did not tell the Commissioner, does not. READING: the months are counted as under s 19. Interest runs "from the end of 30 days after the 1st day of the 1st quarter for which the tax is imposed": after 31 October 2026 for the October quarter. Asserted.
22. **Not telling the Commissioner is an offence only through the TAA, and costs ten times the rebate offence.** Land Tax Act s 14 states no penalty. Its note points to TAA s 67(2), "Maximum penalty: 50 penalty units", $8,000 at $160. Rates Act s 67(4)-(5) makes failing to tell the Commissioner of a change after applying for a rebate a strict liability offence of 5 penalty units, $800. Asserted.
23. **A lease back to the seller does not defeat the new-owner exemption.** Section 11C(3)(b) excepts "the seller of the parcel under an agreement with the new owner for a period of not longer than 3 months". A buyer whose seller rents the home back over the 1st day of the next quarter, and who moves in within 3 months, is still exempt for that quarter. Asserted.
24. **Three Rates Act formulas are transcriptions.** The DOCX holds s 15(2), s 15(3) and s 64(3)(b) only as an embedded object or image. The deposited text carries a transcription from the authorised PDF ("rates otherwise payable for year × (rateable days ÷ days in year)"; "(RL ÷ 2) × (D ÷ days in year)"), which the encoding follows. Section 63(5)(b) has the same rebate formula as linear text, so the two agree.
25. **Overdue land tax bears simple interest; an overdue surcharge compounds.** Corrected on 24 October 2026: the first version applied finding 13 to land tax, citing a dictionary entry that does not reach s 19. Section 19(1)(d) charges interest "on the total amount of overdue land tax that is unpaid", in the words of Rates Act s 21. But s 19 is in pt 3, and the dictionary's "land tax" says "(b) for part 3 (Enforcement)—see section 18A". Section 18A says only "land tax includes a foreign ownership surcharge". The inclusion of "interest payable in relation to the land tax" is in par (a), "for this Act generally". READING: in s 19, land tax does not include its own interest, so each month's interest is on the land tax alone. $1,338.41 two months late at 9.6% bears $21.41 of interest, where the same amount of rates bears $21.50. A foreign ownership surcharge is land tax in pt 3. The dictionary, for the whole Act, says it "includes ... interest payable in relation to the foreign ownership surcharge", so its interest compounds: $812.88 two months late bears $13.06. Asserted. The interest question now asks which kind of amount is overdue.
26. **The quarter in which an owner moves out bears no land tax (s 8A(3)).** Corrected on 24 October 2026. Section 8A(3) says: "If an exemption under this part stops applying to a parcel of land, land tax is payable on the 1st day of the quarter after the date the exemption stops applying." When the owner moves out, the s 11A exemption stops on that day. So no land tax is payable for the quarter that contains that day, or begins on it, even if no one lives there on its 1st day. Section 17D(3) says the same of the surcharge. The first version applied this only in "From which quarter do I pay land tax after moving out". "Do I pay land tax for the quarter" taxed the October 2026 quarter of an owner who moved out on 1 October 2026. Both questions now take the answer from one rule in the core. Asserted for a move on 1 October 2026:
    - left empty: October not payable, January exempt under s 11B, April payable;
    - rented from 1 October: October not payable, payable from 1 January.
27. **The 2 years after a death end at the end of the second anniversary.** Corrected on 24 October 2026. Section 11D(2) exempts the parcel "for 2 years after the date of the owner's death", and (3) lets the personal representative apply "before the 2-year period ends". READING: the period runs from the day after the death to the end of the second anniversary. For a death on 15 March 2025 that is 16 March 2025 to 15 March 2027, so an application on 15 March 2027 is in time. The seat used to answer "before 15 March 2027", a day earlier than the core rule, which an application on day 730 fulfils. It now gives the last day, 15 March 2027, taken from the core. On the same reading, a quarter beginning on the anniversary is still within the exemption: after a death on 1 April 2025, the quarter beginning 1 April 2027 is exempt. The first version taxed it. The Legislation Act 2001's rules on periods are not deposited. Asserted.
28. **Rates Act s 15(3) is s 15(2) with a different count of days.** Corrected on 24 October 2026: the first version declared s 15(3) not covered but no question could return that answer. Section 15(3) applies to a parcel "held under a lease from the Commonwealth for only part of the year". The rates are "rates otherwise payable for year × (days lease in force ÷ days in year)", and "days lease in force ... includes any days when an owner continues to occupy the parcel of land after the ending of the lease" (s 15(4)). Sch 1 s 2.1(1)(a) applies s 15 to the levies. The encoding takes one count of days: the rateable days, or, under such a lease, the days the lease is in force. Take a lease that ends on 30 September 2026, with the owner staying on to 8 October: 100 days, and $816.59 in all. Asserted.

## Corrections after the independent check (24 October 2026)

An independent verifier raised six issues. Each was checked against the deposited texts, and all six were real:

1. **Compound interest on land tax** (`rates-shared.l4`). The cited dictionary entry does not reach s 19. Fixed: finding 25.
2. **The surcharge question answered 0 with no unimproved value** (`rates-seat.l4`, `landtax-core.l4`). The core treated a missing AUV as 0. Only the seat's land tax question checked for it. Fixed: the core's land tax and surcharge amounts now check for the AUV and answer `not covered`, and the seat's own check is gone. Asserted for the surcharge. A non-foreign owner still gets 0 (see Departures).
3. **Not-covered answers claimed as asserted that could not be returned** (`encoding.json`, `rates-shared.l4`). Fixed:
    - s 15(3) is now encoded (finding 28), and its unreachable reason is removed;
    - a special disability trust is added to "Is my other question covered";
    - every matter that question names is asserted, including the compassionate decision and s 13A;
    - Method, Scope and `encoding.json` now say which question returns which answer.
4. **The s 11D(3) deadline, one day out from the core** (`rates-seat.l4`). Fixed: finding 27. The seat takes the last day from the core, and the s 11D(3) rule takes the day of the death.
5. **When land tax starts after moving out was encoded twice** (`landtax-core.l4`). Fixed: finding 26. The position applies s 8A(3), and "From which quarter" now asks the position.
6. **Headers and NOTES disagreed on scope; one NOT was unbracketed**:
    - `rates-core.l4` now lists s 55(2) only (s 55(4) stays out, as NOTES says) and s 15 whole;
    - `landtax-core.l4` no longer lists s 10(1)(d), and says that rural land is not covered;
    - the NOT in s 49 is bracketed.

## Before relying on it

- An independent test pass, and a check of every table row against the authorised PDFs of DI2026-150 and DI2026-152.
- Deposit the TAA s 139 determination of the interest rate for Rates Act s 21 and Land Tax Act ss 19 and 19A, and any discount rate under s 18(3), and replace the inputs.
- Confirm the readings in findings 4, 6, 7, 12, 13, 16, 20, 21, 25, 26 and 27 with ACT Revenue practice or a ruling.
- Section 8A(3) is applied where an owner moves out. Its effect where another exemption stops mid-quarter is not: for example s 11I, when the Commissioner becomes satisfied the home is fit again, because that fact carries no date.
- The 2027 determinations when made (from 1 July 2027), and the earlier ones for earlier years.
- Encode the out-of-scope parts a home owner may meet: the s 47 deferral without application; the revocation process (ss 50, 53-54, 55(3)-(4), 56, 58); s 46(6); a units plan registered mid-year (s 29(2)); a special disability trust as owner (ss 46(2)(b), 64(5)); and the Land Tax Act's corporation and trustee rules (ss 16, 27(5)), which a family trust owner would need.
- The JACS copyright policy, which could not be read on 2026-10-20 (see `SOURCE-LICENSE.md`).
