# Land Tax Act 1936 (SA), with the Taxation Administration Act 1996 (SA): baseline encoding

> **The text is not the official text, and it is out of date.** The Land Tax Act text encoded here is the **Open Australian Legal Corpus text as at 2023-07-01 (scraped 2024-09-13)**, not the official text from legislation.sa.gov.au. The South Australian Current Titles list of 22 September 2026 shows the Act at a version of **4.12.2025**, so the text is out of date. The Taxation Administration Act text is the corpus text as at 2019-10-03 (scraped 2024-09-13), also listed at 4.12.2025. **Every year's land tax thresholds, and any change to the rates after 2023-07-01, must be supplied as inputs.**

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18 and the brief for the Australian tax-and-benefits encodings of 24 October 2026. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act. The Taxation Administration Act subject holds no encoding either.

The encoding has two layers:

- **A seat-neutral core**, in the Acts' own actors and terms: the owner, a natural person, the taxpayer, the objector, the Minister and the Commissioner. Where the text says "must" or sets a deadline, the rule is regulative (`DEONTIC`, `PARTY ... MUST/DO/MAY ... WITHIN ... HENCE ... LEST`). Computations (the exemption, the taxable value, the scale, the waiver amounts, interest and penalty tax) are functions.
- **A seat layer** (`lta-seat.l4`) that asks the owner's questions with plain inputs. It builds the core's records and restates no rule. Its deadline dates are the core's own day counts added to the date the owner gives.

The Taxation Administration Act 1996 is brought in as its own module (`taa-procedure.l4`) in the same folder. The Land Tax Act s 3 says it "should be read together with the Taxation Administration Act 1996", which holds the objection, appeal, interest and penalty tax provisions the Land Tax Act leaves to it. Cross-folder IMPORT does not work.

| File | What it holds |
|---|---|
| `lta-common.l4` | Arithmetic and date helpers, the `not covered` answers, and the parties and acts of every regulative rule (shared by both Acts) |
| `lta-core.l4` | Core: Land Tax Act ss 2, 4, 5 (residential land exemption and neighbours; s 5(7) regulative), 5AA, 5A, 6, 7, 8A, Schedule 1 Part 2, 8B, 9, 14-17, 19 (s 19(1) regulative, and with TAA s 91) |
| `taa-procedure.l4` | Core: TAA ss 25-27, 30-33 (s 33 regulative), 84, 86, 87, 91-95 (Part 10 regulative) |
| `lta-seat.l4` | Seat layer: 43 exported questions, each with `@desc` on every input, under `§` headings |
| `lta-cases-core.l4`, `taa-cases.l4` | Cases for the two core modules |
| `lta-cases-seat.l4` | Cases for the seat layer, asked with plain answers |

Conventions: a financial year is named by the calendar year in which it ends (2025/2026 is 2026); money is in dollars; percentages are numbers out of 100; dates are DATE values.

## Edition

- **Land Tax Act 1936**: the Open Australian Legal Corpus text as at **2023-07-01** (corpus version_id `south_australian_legislation:2023-07-01/1936.2318.un`, scraped 2024-09-13), deposited at `../../registers/source-bundle/land-tax-act-1936.txt`. It is not the official text. The Current Titles list of 22 September 2026 shows a version of **4.12.2025**, so this text is out of date and at least one later version is missing.
- **Taxation Administration Act 1996**: the corpus text as at **2019-10-03** (version_id `south_australian_legislation:2019-10-03/1996.80.un`, scraped 2024-09-13), deposited at `../../../taxation-administration-act-1996/registers/source-bundle/taxation-administration-act-1996.txt`. It is not the official text. It is listed at 4.12.2025, so it too is out of date.
- **Formulas missing.** The deposit lacks 8 formulas (`../../registers/source-bundle/land-tax-act-1936.formulas.md`). Four touch this encoding: the s 8A(2a), (3) and (3b) threshold indexation, and the s 9(8) double-taxation deduction. None was guessed:
  - the thresholds for the year are **inputs** (from the Commissioner's Gazette notice, s 8A(7));
  - the s 9(8) deduction is an **input** (from the owner's assessment notice).
- **Amounts the text states, and used:** 2020/2021 Threshold A $450 000 and Threshold D $1 350 000 (s 8A(2)); Threshold D $1 350 000 for 2021/2022 and $2 000 000 for 2022/2023 (s 8A(3a)). Everything else is supplied.
- **Rates.** Schedule 1 Part 2 clause 2 (2020/2021, 2021/2022) and clause 3 (2022/2023 onward) are in the text. The text is as at 1 July 2023, the day liability for 2023/2024 arose (s 4(2)). So for 2024/2025 and later a change of rates made after that day is an **input**: the clause 3 rates apply unless the owner supplies changed ones.
- **Not deposited:** the Land Tax Regulations 2010 (any further s 5(11) criteria, and the s 5A(1)(c)(v) and (d)(v) criteria, which are asked as a fact); the Gazette notices of thresholds; the TAA market rate (s 26(2)), which is an **input**.
- **Years before 2020/2021** answer `not covered`, because Schedule 1 was inserted from 1 July 2020 (38/2019 s 19) and the earlier scales are not in the deposit.

## Licence

The texts are CC BY 4.0: State of South Australia, through the Open Australian Legal Corpus (Umar Butler / Isaacus, version 7.1.0, CC BY 4.0), taken under the owner's ruling of 2026-10-24. The ruling and terms are in `SOURCE-LICENSE.md` (a copy of the subject's) and in `../../../taxation-administration-act-1996/SOURCE-LICENSE.md`. Every module carries "Based on content from the South Australian Legislation website" with the required attribution.

## Checks

`l4 run` on every `.l4` in the folder: **0 errors, 0 warnings**, and **248 assertions written, 248 satisfied**.

| Case file | Assertions | `#TRACE`s (each with an `-- expect:` line, read and as expected) |
|---|---|---|
| `lta-cases-core.l4` | 135 | 3: breach by the owner (s 5(7), notified on day 22); breach by the taxpayer (s 19(1), only $3 000 of $3 501 paid); breach by the taxpayer (s 19(1) with TAA s 91, objected but did not pay) |
| `taa-cases.l4` | 40 | 3: breach by the taxpayer (s 33, paid on day 31); the objector's appeal still open after a determination; the Minister's notice still pending (20 days left) |
| `lta-cases-seat.l4` | 73 | none |

The four modules (`lta-common`, `taa-procedure`, `lta-core`, `lta-seat`) also run clean on their own.

As a control, a copy of `lta-cases-core.l4` with one expected value altered ($3 501 to $3 502) was run. The runner reported 1 assertion failed and 134 satisfied.

Expected values were worked by hand from the deposited texts. Every threshold in the cases, other than those the Act states, is assumed and labelled so; so is every market rate. No value was copied from the encoding's output.

A trap met on the way: in the stable `l4`, a continuation line that begins `DIVIDED BY 100 TIMES days ...` divides by the whole product. So interest and penalty tax are written with each step bracketed on its own line.

## Seat

**The owner of land: the home owner, and the individual who owns other land.** That is the natural person liable as owner (s 14). The questions are the ones that person asks:

- "Is my home exempt?"
- "What if my home is being built or renovated, or is partly used for business?"
- "I moved house during the year: can the land tax be waived?"
- "How much land tax is payable on my other land this year?"
- "When must I pay?"
- "How do I object, and when can I appeal?"
- "What interest and penalty tax can I be charged?"

The owner is an individual, so "owned by a natural person" (s 5(10)) is fixed as true in the seat layer. The owner who is trustee of a special disability trust (s 5(10)(h), (12a)) is asked about in that capacity.

The text puts duties on the Commissioner (to give the s 5(6) notice, to publish thresholds) and on the Minister (to give notice of the determination of an objection, TAA s 89). Both are officials, so neither gets a seat. Their steps appear as parties in the regulative rules, for what they mean to the owner.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The scale is in the Act. The thresholds are set by Gazette notice and the indexation formulas are missing, so the thresholds are inputs. The TAA is brought in, as the task requires, because the Land Tax Act leaves objections, appeals, interest and penalty tax to it (s 3).
- **The actors the text names.** Followed: the owner, the natural person, the resident (s 5AA), the applicant (s 5A), the purchaser and vendor (s 5A(1)(b)), the taxpayer, the objector, the Minister, the Commissioner and the trustee of a special disability trust.
- **A judgment handed to someone else is answered conditionally.** Followed. These are all facts the owner states, and the answer holds if the official decides that way:
  - every "the Commissioner is satisfied" in s 5(10)(ab), (ac), (ad), (h), (10a) and (12a);
  - the Commissioner's s 5AA(2) satisfaction and s 5AA(3) opinion;
  - the choice of capacity under s 9(2);
  - "unless the Commissioner allows otherwise" in s 5A;
  - the s 30(2) satisfaction and the s 31(2)(c) increase (TAA);
  - the Minister's permission (TAA ss 87, 93(2)).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: owner and its capacities (s 2(1), (1c)); residential land exemption (s 2(1)); prescribed land and prescribed interest (s 5AA); relevant concession (s 5A(2)); retired persons' relocatable home park (s 5(13)); LT (TA)-(TD) (Schedule 1 Part 1); taxable value (s 7); tax default (TAA s 3(1)).
  - Asked as facts: principal place of residence (not defined); site value (Valuation of Land Act 1971); retirement village and residence contract (Retirement Villages Act 1987); special disability trust and principal beneficiary (Social Security Act 1991 and Veterans' Entitlements Act 1986, Cth); deliberate tax default, tax audit, sufficient disclosure and obstructive conduct (TAA).
- **One case is the text's natural unit.** Followed: one piece of land at midnight on 30 June for an exemption; one assessment for the tax (all the land owned alone, or one joint assessment, or one owner's separate assessment); one objection.
- **The Act's own terms, each with a plain gloss.** Followed. The comments quote the statutory words.
- **Operative sections in; machinery out.** Followed.

**Departures and readings:**

- Each piece of land is one case, so a home's exemption and the owner's other land are entered as separate numbers. The seat's all-in-one question takes one home and the total site value of the other land owned alone.
- Where the Act states a threshold, that amount is used, whatever is supplied (finding 6).
- Readings the text leaves open are recorded under the findings:
  - the 50% gap in s 5AA (finding 3);
  - the year asked about counts toward the 2- and 3-year limits (finding 9);
  - the s 5A(3)(b) day count (finding 11);
  - the "negative amount" in s 9(9) (finding 12);
  - "allowed in full" means not dissatisfied (finding 13);
  - the penalty tax adjustments (finding 15);
  - interest on a 365-day year (finding 15);
  - (e) and (f) taken as whole exemptions (finding 16).

## Scope

**In.**

*Land Tax Act 1936:*

- s 2: owner, its capacities (s 2(1c)) and residential land exemption;
- s 4(1)(n), (2), (3): imposition; liability arises at the start of the year, on circumstances at midnight on 30 June before;
- s 5, the residential land exemption and its neighbours:
  - s 5(1), (2): proper grounds plus a grant;
  - s 5(10)(a): a natural person's principal place of residence, whether or not the sole owner;
  - s 5(10)(ab), (ac), (ad): destroyed, rebuilt, renovated or being built, with s 5(10a) (the 12-month occupation condition after completion, and no rent), (10b) (2 years) and (11a) (3 years);
  - s 5(10)(b), (ba), (bb) with the s 5(12) scale: mixed use; for a hotel, motel or serviced apartments, more than 75% of floor area as the residence for the exemption and 25% or more for the partial one;
  - s 5(10)(e): residence contracts in a retirement village;
  - s 5(10)(f): relocatable homes;
  - s 5(10)(h) and (12a): special disability trust land;
  - s 5(10c): waiver or refund for a building year;
  - s 5(4), (6)-(9): notices, penalties; s 5(7) is a regulative rule (notify within 21 days of receipt);
- s 5AA: a minor interest disregarded;
- s 5A: waiver or refund for residential land, its criteria (1), (2), (6a), amounts (3) and time limit (4)(c);
- s 6: minimum tax ($20);
- s 7: taxable value is the site value, a valuation input;
- s 8A(1), (2), (3a), (7), (8): the scale years, the stated thresholds, thresholds otherwise an input, and rounding;
- Schedule 1 Part 1 and Part 2 clauses 2 and 3: the scales, as tables over Thresholds A-D using LT (TB), LT (TC) and LT (TD);
- s 8B: aggregation and apportionment;
- s 9(1), (2), (4), (6), (8), (9): more than one owner (the s 9(8) deduction an input);
- ss 14-17: the person liable, change of ownership, joint and several liability, the burden shared;
- s 19(1): pay within 30 days after service (regulative), also run beside TAA s 91;
- s 19(2), (3): a tax default from wrong or missing information.

*Taxation Administration Act 1996:*

- Part 5: ss 25, 26 (the market rate an input, plus 8%), 27, 30, 31, 32, and s 33 (regulative);
- Part 10: ss 84, 86 (objection within 60 days), 87, 91, 92, 93, 94 (appeal within 60 days, or on 14 days' notice after 90 undetermined days), 95, with Part 10 as a regulative rule.

**Out**, as the task directs:

- trusts (ss 11-13F, Schedule 1 Part 3, the s 13D trustee notices), except the special disability trust;
- related corporations (ss 13G-13J);
- build-to-rent (s 7A);
- strata and community plan assessment (s 10);
- primary production and the other non-residential exemptions (s 4(1) other than (n), and s 5(10)(c), (ca), (cb), (d), (g));
- enforcement (ss 18, 20-24).

Also out:

- the indexation formulas and the s 9(8) formula, which are missing;
- service (s 25) and regulations (s 26);
- the TAA's assessment, refund, collection, record-keeping, investigation and secrecy machinery;
- interest on refunds (TAA ss 90, 99);
- the discretionary remission of interest and penalty tax (TAA ss 29, 34) and rounding down to a dollar (s 102).

## What the Act turns out to say

1. **The text is the Open Australian Legal Corpus text as at 2023-07-01 (scraped 2024-09-13), not the official text, and it is out of date.** The Current Titles list shows a version of 4.12.2025. The Taxation Administration Act text is older still (2019-10-03). So every year's thresholds, and any rate change after 2023-07-01, are inputs, and every answer should be checked against legislation.sa.gov.au.
2. **The Act does not contain the thresholds for any current year.** It states only these:
   - 2020/2021: Threshold A $450 000 and Threshold D $1 350 000 (s 8A(2));
   - Threshold D: $1 350 000 for 2021/2022 and $2 000 000 for 2022/2023 (s 8A(3a)).

   B and C for 2020/2021 are 2010/2011 amounts indexed by the s 8A(2a) formula. A-C for later years are indexed by s 8A(3), and D from 2023/2024 by s 8A(3b). All three formulas are missing from the deposit. The thresholds actually applied are the ones the Commissioner gazettes (s 8A(7)), which are "conclusive in all respects" (s 8A(9)). So a year with no thresholds supplied answers `not covered`. Asserted.
3. **An interest of exactly 50% falls through s 5AA.** It is prescribed land ("not greater than 50%"), but s 5AA(2) reaches only "5% or less" and s 5AA(3) only "exceeds 5% but is less than 50%". So the Commissioner has no power to disregard a resident's half share. Interests of 5% or less are disregarded unless the Commissioner is satisfied otherwise. Interests between 5% and 50% are disregarded only if the Commissioner forms the opinion. Asserted.
4. **A co-owner living elsewhere does not reduce the home exemption.** Section 5(10)(a) exempts the land if it is a natural person owner's principal place of residence "whether or not he or she is the sole owner of the land". The whole land is exempt even when the other owners live elsewhere, subject only to s 5AA. Western Australia's s 21(2) is different: there, owners who do not live in the home must be on the title only as guarantors (`subjects/au/wa/land-tax-assessment-act-2002/encodings/baseline-2026-10/`, finding 6). Asserted.
5. **Business use of the home:**
   - less than 25% of the floor area: wholly exempt (s 5(10)(a));
   - 25% to 75%: partly exempt, with the taxable value reduced by the s 5(12) scale (5-point steps, 75% exactly giving 25%);
   - more than 75%: no exemption.

   A hotel, motel or set of serviced apartments the owner lives in is wholly exempt where more than 75% of the floor area is the residence (s 5(10)(ba)). It is partly exempt where 25% or more is (s 5(10)(bb)), with the accommodation area counted as the business area. Asserted.
6. **The Act's own threshold wins over a supplied one.** For 2022/2023 the encoding uses the Act's $2 000 000 for Threshold D, whatever figure is entered. A Gazette notice that differed would be "conclusive" under s 8A(9). The text does not resolve such a conflict. Asserted.
7. **"$0.50 for every $100 or fractional part of $100" reaches the first dollar over Threshold A.** $1 over A costs $0.50. The $20 minimum (s 6) means nothing is payable up to $3 900 over A (39 parts, $19.50), and $20 from $3 900.01 over (40 parts). Asserted.
8. **The 2020/2021 and 2021/2022 scale differs from the later one in one rate only:** $1.25 against $1.00 per $100 between Thresholds B and C. Asserted.
9. **The 12-month occupation condition applies to building and renovating, not to a destroyed home.** Section 5(10a) names (ac) and (ad) only. It needs at least 12 months' occupation as the principal place of residence after completion, or good reasons, and no rent from anyone else. (ac) and (ad) last at most 2 years unless the Commissioner sees good reasons (s 5(10b)). (ab) lasts at most 3 years, with no exception (s 5(11a)). READING: the year asked about counts toward the limit. Asserted.
10. **A buyer under an unsettled contract is already an owner.** Section 2(1c)(c) makes "a person who has entered into a contract to purchase" a prospective owner, while the seller remains the legal owner. Both are owners at midnight on 30 June. Under s 9(2) the Commissioner may treat the owners in one capacity as the sole owners, so the answer is conditional on that choice. Western Australia turns on possession (s 8(3) there). Asserted.
11. **The s 5A(3)(b) refund of the land tax adjustment** is the lesser of the adjustment paid and the land's own land tax times "the number of days from the date of settlement to the end of that financial year" over 365. READING: the settlement day is not counted, so settlement on 18 April gives 73 days to 30 June. A $1 000 tax then gives $200. Asserted.
12. **A co-owner's separate assessment cannot be finished from the deposit.** The s 9(8) deduction "necessary to avoid double taxation" is a formula that is missing. So the encoding asks for the deduction from the notice, and answers `not covered` without it. It also gives the most the separate assessment can be before the deduction. READING: the "negative amount" in s 9(9) is the owner's tax after the deduction, which becomes nil with no credit. Asserted.
13. **Paying and objecting run side by side:**
    - pay within 30 days after service of the assessment on any one of the taxpayers (s 19(1)), and an objection does not suspend recovery (TAA s 91);
    - object within 60 days of service (TAA s 86), or up to 12 months later with the Minister's permission (s 87);
    - appeal within 60 days after service of the Minister's determination (s 94(1));
    - if the Minister has not determined the objection within 90 days (not counting a s 88 suspension), appeal at any time on 14 days' written notice to the Commissioner (ss 92(b), 94(2));
    - in either case only after paying 50% of the tax, unless the Minister permits otherwise (s 93).

    READING: an objection allowed in full leaves the objector not "dissatisfied" (s 92(a)). Asserted.
14. **Telling the Commissioner:**
    - an error in the factual basis of an exemption notice must be notified within 21 days after receipt (s 5(7); $5 000, expiation $315);
    - a change that ends or reduces an exemption must be notified "forthwith" (s 5(8)). That names no number of days, so it is a yes/no duty, not a deadline;
    - a failure to inform that leads to too little being assessed is a tax default (s 19(2)), with interest from the day the exemption applied (s 19(3)).

    Asserted.
15. **Interest and penalty tax.** Interest is the market rate (an input) plus 8% a year, daily, with nothing payable under $20 (TAA ss 25-27). READING: a 365-day year, and one rate for the whole period.

    Penalty tax is 25% of the unpaid tax, or 75% if the default was deliberate (s 31(1)). It is nil if the Commissioner is satisfied the default was neither deliberate nor careless (s 30(2)). It is cut by 80% for a disclosure before an audit and by 20% for one during an audit. The Commissioner may raise it by 20% for obstruction. Nothing is payable under $20 (s 32). READING: "reduced by 80 per cent" takes 80% of the penalty off, and a reduction and an increase together are multiplied. Asserted.
16. **The retirement village and relocatable home park exemptions run to whoever owns the land** (s 5(10)(e), (f)): the village or park owner. READING: a resident holding only a residence contract or a site licence is not an "owner" under s 2(1), whose paragraph (a) excludes leasehold interests. This owner seat meets (e) and (f) only as an individual who owns such land. The text says "may be exempted" without "wholly"; the land they describe is taken as wholly exempt. Asserted for the exemption grounds only.

## Commonwealth and other links

- **Capital gains tax on the home.** The principal place of residence here is a different question from the main residence exemption from capital gains tax in the Income Tax Assessment Act 1997, Subdivision 118-B. That is encoded at `subjects/au/income-tax-assessment-act-1997/encodings/baseline-2026-10/` (`itaa-cgt.l4`, ss 118-110 and 118-150). The jurisdiction README marks the comparison **unverified (from general knowledge, not from the texts)**. What the two encodings show:
  - land tax tests the residence at midnight on 30 June before each year (s 4(3)) and exempts the land for that year;
  - s 118-110, as that encoding quotes it, asks whether the dwelling was the main residence "throughout your ownership period", for the whole gain;
  - the building rules also differ in length: (ad) here runs 2 years (s 5(10b)), and s 118-150 there up to 4.

  An owner can be exempt from land tax every year and still not qualify for the full capital gains exemption, or the other way round.
- **Special disability trust.** The definitions come from the Social Security Act 1991 (Cth), ss 1209L and 1209M (`subjects/au/social-security-act-1991/`), and from the Veterans' Entitlements Act 1986 (Cth), s 52ZZZW (`subjects/au/veterans-entitlements-act-1986/`). Neither Commonwealth encoding covers the special disability trust yet, so here it is asked as a fact.
- **Aged care.** The approved provider and residential care in s 5(10)(ca), (cb) come from the Aged Care Act 1997 (Cth). Those paragraphs are out of scope.
- **Western Australia.** The model encoding is `subjects/au/wa/land-tax-assessment-act-2002/encodings/baseline-2026-10/`. Findings 4 and 10 compare the two States.
- **South Australian neighbours.** The same home turns up elsewhere in the jurisdiction README's sample, not encoded here:
  - the emergency services levy remission (`../../../emergency-services-funding-remissions-land-regulations-2014/`);
  - the first home owner grant's residence requirement (`../../../first-home-and-housing-construction-grants-act-2000/`);
  - the stamp duty relief on new homes (`../../../stamp-duties-act-1923/`).

Cross-folder IMPORT does not work, so these are links, not code.

## What would need doing before this is worth relying on

- Replace both texts with the current official versions from legislation.sa.gov.au (4.12.2025 or later), and check every finding against them.
- Restore the s 8A(2a), (3), (3b) and s 9(8) formulas from the authorised version into `land-tax-act-1936.formulas.md`. Then compute the thresholds and the deduction instead of asking for them.
- Deposit the Commissioner's Gazette notices of thresholds for 2023/2024 onward, and the Land Tax Regulations 2010, and bring them in.
- Check the readings in findings 3, 9, 11, 12, 13, 15 and 16 against RevenueSA practice or a decision.
- Add the trust provisions (ss 11-13F, Schedule 1 Part 3) and community and strata plan assessment (s 10) if an owner in a scenario meets them.
- Run the Legalese Studio stages this baseline skipped: Resolve, Refine and Test, an independent test pass, and the human gates.
