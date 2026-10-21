# california/

California (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the California Legislative Information (leginfo.legislature.ca.gov), published by the Office of Legislative Counsel, California Codes; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited then; see the later sections (text deposited 2026-10-20, two encodings 2026-10-24).

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Topics with no legislation here

- **Passenger compensation**: Air passenger rights are federal (DOT rules under 49 U.S.C., with state regulation preempted by the Airline Deregulation Act). California has no passenger-compensation statute comparable to EU261.
- **Customs/duties**: Customs and import duties are exclusively federal (U.S. Const. art. I §§8 and 10; 19 U.S.C.). California has no customs statute.
- **Work permits/immigration**: Immigration and work authorisation are federal (8 U.S.C., INA). California has only peripheral provisions, e.g. Lab. Code §§1019-1019.4 (unfair immigration-related practices) and §§2811-2814 (E-Verify limits). None of these governs permits.

## Priority 3 sample: personal income tax, and social security and benefits (deposited 2026-10-20)

Statute text for California's personal income tax and its main cash benefits was deposited on 2026-10-20 from the **Office of Legislative Counsel's official bulk database export**, with the owner's approval of that route on 20 October 2026.

**Why the bulk route.** leginfo.legislature.ca.gov answered HTTP 403 when this fetcher asked for its robots.txt, so it was not used at all. The bulk host https://downloads.leginfo.legislature.ca.gov/ has no robots.txt (HTTP 404). Its readme (`pubinfo_Readme.pdf`, 2021-05-21) and news file describe the tables but state no terms. The licence rests on Gov. Code 10248.5 (public domain, as recorded from leginfo in the 2026-09-22 index check) and on *Georgia v. Public.Resource.Org* (2020). Verdict: **conditions, met**.

**How it was fetched.** One file was downloaded: `pubinfo_2025.zip`, the 2025-2026 session export and the only file that carries the code tables. It is 1,291,985,079 bytes, sha256 `b0b614a2061dd16d468cddbd4921604365f052a5c21ea18056b2606136e04ec1`, Last-Modified Mon, 19 Oct 2026 04:26:10 GMT.
- The connection broke twice because of a network failure on our side.
- The same file was completed with HTTP Range requests checked against its ETag.
- No 403, 429 or challenge occurred.
- The zip was deleted after extraction.

The files under "Bulk deposit" in each `SOURCE-LICENSE.md` give the details.

**Currency.** The code tables were last updated 2026-10-03 and include 2026 statutes, for example Stats. 2026, Ch. 236 (SB 1435), effective 2026-09-14. That act amended the CalEITC (17052) and the IRC conformity section (17024.5). Where the database holds more than one version of a section (one operative until a date, one from it), every version is kept. Every text is marked as an unofficial version.

| Subject | File | What | Section versions | Characters |
| --- | --- | --- | --- | --- |
| `revenue-and-taxation-code-division-2-part-10-personal-income-tax` (existing) | `ca-rtc-div2-part10-ch1-general-provisions-definitions-2026-10` | Ch. 1: definitions, residence (17014-17016), IRC conformity date (17024.5), "net tax" (17039) | 61 | 73,019 |
| same | `ca-rtc-div2-part10-ch2-imposition-of-tax-rates-credits-2026-10` | Ch. 2: rates (17041), mental health surcharge (17043), CalEITC (17052), Young Child Tax Credit (17052.1), renter's credit (17053.5), exemption credits (17054) and the other credits | 50 | 547,546 |
| same | `ca-rtc-div2-part10-ch3-arts1-3-gross-income-inclusions-exclusions-2026-10` | Ch. 3 arts. 1-3: gross income and AGI by reference to the IRC (17071-17078), items included, items excluded (17081-17158.5) | 112 | 148,882 |
| `unemployment-insurance-code-division-1-part-1-unemployment` (existing) | `ca-uic-div1-part1-ch5-unemployment-compensation-benefits-2026-10` | Ch. 5 whole: eligibility and disqualification, weekly benefit table (1280), duration, claims, overpayments | 115 | 167,334 |
| `welfare-and-institutions-code-division-9-part-3-chapter-2` (existing) | `ca-wic-div9-part3-ch2-arts1-2-5-general-definitions-eligibility-2026-10` | CalWORKs arts. 1-2.5: general, definitions, eligibility | 93 | 136,194 |
| same | `ca-wic-div9-part3-ch2-arts3-2-4-7-welfare-to-work-kinship-2026-10` | arts. 3.2-4.7: welfare-to-work, housing support, Cal-Learn, kinship guardianship | 145 | 342,719 |
| same | `ca-wic-div9-part3-ch2-arts5-6-foster-care-computation-payment-of-aid-2026-10` | arts. 5-6: AFDC-Foster Care; computation and payment of aid, maximum aid payments (11450), income disregards (11451.5) | 133 | 473,853 |
| same | `ca-wic-div9-part3-ch2-arts7-9-7-enforcement-family-violence-evaluation-2026-10` | arts. 7-9.7: enforcement, family violence option, evaluation | 52 | 107,731 |
| `welfare-and-institutions-code-division-9-part-3-chapter-3-state-supplementary-program` (new) | `ca-wic-div9-part3-ch3-arts1-6-state-supplementary-program-2026-10` | SSP arts. 1-6: general, definitions, administration, eligibility, payment of aid (12200 ff.), services | 45 | 46,399 |
| same | `ca-wic-div9-part3-ch3-arts7-8-in-home-supportive-services-relatives-2026-10` | arts. 7-8: In-Home Supportive Services, relatives' responsibility | 91 | 276,200 |

Total: 10 texts, 897 section versions, 2,319,877 characters.

**How the pieces connect.** These connections were read in the deposited text:
- "Internal Revenue Code" in Part 10 means Title 26 as enacted on a specified date for each taxable year (17024.5).
- Adjusted gross income follows IRC § 62 except as otherwise provided (17072). So the federal subject `subjects/us/internal-revenue-code-of-1986` is the starting point, frozen at California's conformity date.
- IRC § 86 (Social Security benefits) does not apply (17087), so Social Security is not taxed by California.
- IRC § 85 (unemployment compensation) does not apply (17083), so UI benefits under UIC ch. 5 are not taxed by California.
- The CalEITC is "an amount determined in accordance with Section 32 of the Internal Revenue Code", as modified and multiplied by an adjustment factor (17052).
- The Young Child Tax Credit is $1,176 times the same adjustment factor (17052.1).
- SSP pays an aged, blind or disabled person an amount which, added to the federal benefit under Part A of Title XVI of the Social Security Act and other income, reaches the state payment standard (12200). That ties it to `subjects/us/social-security-act`.

These links were not read in deposited text and are unverified (general knowledge):
- CalWORKs is California's TANF programme under SSA Title IV-A.
- UI is the federal-state programme under SSA Titles III and IX and FUTA.
- UI benefits are federally taxable under IRC § 85.
- CalFresh/SNAP is federal (`subjects/us/food-and-nutrition-act-of-2008`).

**Gaps.**
- Part 10 chapters 2.1 and 4-14 (AMT, deferred compensation, trusts, partnerships, LLC taxes, nonresidents' gross income, credit for taxes paid, capital gains) are not deposited. Neither is ch. 3 art. 6 (deductions) or art. 9 (nonresidents and part-year residents), which is the next to add for the standard and itemised deductions.
- Withholding (UIC Division 6) is indexed only.
- The California Code of Regulations (Westlaw-hosted, HTTP 403) and CDSS/EDD annual figures (CalWORKs MAP levels set by budget acts, SSP payment levels) were not sourced.
- The CA README line "No statute text has been deposited" above dates from 2026-09-22 and is superseded for these subjects.

## Frontier AI incident reporting (deposited 2026-10-24)

The Transparency in Frontier Artificial Intelligence Act (SB 53, Stats. 2025, ch. 138) was deposited on 2026-10-24 by the same bulk route, reading only the needed members of `pubinfo_2025.zip` (the same export, ETag "4d0220b7-65e29e9d53c80") with HTTP Range requests; leginfo.legislature.ca.gov again answered HTTP 403 (a Cloudflare challenge) and was not used.

| Subject | File | What | Section versions | Characters |
| --- | --- | --- | --- | --- |
| `business-and-professions-code-division-8-chapter-25-1-transparency-in-frontier-ai` (new) | `ca-bpc-div8-ch25-1-tfaia-2026-10` | Bus. & Prof. Code Ch. 25.1 whole (22757.10-22757.16): definitions, frontier AI frameworks and transparency reports, critical safety incident reporting, civil penalty | 7 | 21,821 |
| same | `ca-sb53-stats-2025-ch-138-chaptered` | SB 53 as chaptered, with its uncodified SEC. 1, 5 and 6 | (bill text) | 45,951 |
| same | `ca-time-computation-2026-10` | Code Civ. Proc. §§ 12, 12a; Civ. Code § 10; Gov. Code § 6800 (computing time) | 4 | 2,985 |
| same | `ca-time-computation-holidays-2026-10` | Code Civ. Proc. §§ 12b, 135; Gov. Code § 6700 (the holidays § 12a refers to; deposited, not computed) | 3 | 5,063 |

Encoded as row `solo-2026-10` (critical safety incident reporting, frontier developer's seat; draft).

## Encodings: tax and benefits (2026-10-24)

Two baseline encodings, each from the seat of the individual and checked with the stable `l4` (1.6.98): 0 errors, 0 warnings, every assertion satisfied.

| Encoding | Seat | Questions | Assertions |
|---|---|---|---|
| [`revenue-and-taxation-code-division-2-part-10-personal-income-tax/encodings/baseline-2026-10`](revenue-and-taxation-code-division-2-part-10-personal-income-tax/encodings/baseline-2026-10) | the individual taxpayer (full-year resident) | resident, exemption credits after the phase-out, renter's credit, tax owed for 2025 before the CalEITC and other credits | 30 |
| [`unemployment-insurance-code-division-1-part-1-unemployment/encodings/baseline-2026-10`](unemployment-insurance-code-division-1-part-1-unemployment/encodings/baseline-2026-10) | the unemployed worker | weekly benefit amount, base-period test, maximum award, a week with wages, pension offset, weekly eligibility, disqualification for how the job ended, requalifying | 43 |

**Annual figures deposited.** Most Personal Income Tax Law amounts are recomputed by the Franchise Tax Board each year, so the FTB's 2025 California Tax Rate Schedules and 2025 Form 540 booklet were deposited on 2026-10-24 (public domain under the State's conditions of use) in `revenue-and-taxation-code-division-2-part-10-personal-income-tax/registers/source-bundle/`, and the figures used are recorded in that subject's `registers/annual-figures.json`.

**Not yet encoded:** the CalEITC and Young Child Tax Credit (they turn on a Budget Act adjustment factor and form FTB 3514, not deposited); CalWORKs maximum aid payments and SSP payment standards (recomputed annually, the current figures not deposited). The renter's credit for 2026 onward is $250/$500 only if a Budget Act bill says so, and otherwise stays $60/$120 (Rev. & Tax. Code 17053.5(k)).

## Interpretation provisions

California has no single interpretation act: Gov. Code § 9603 says that the general rules for the construction of statutes are contained in the preliminary provisions of the different codes.
`interpretation-provisions/` is therefore a cluster of sections: Gov. Code §§ 1-26, 6700-6736, 6800-6808 and 9600-9612, Civ. Code §§ 1-23.6, and Code Civ. Proc. §§ 1-34.
Which sections belong in the cluster is an assumption, not a ruling, and the row's `NOTES.md` records it as a fork.
The text was read from the same Legislature bulk export as the sample above, and is public domain under Gov. Code § 10248.5.
The first encoding is `interpretation-provisions/encodings/legalese-sonnet-5.5/`, written by one Sonnet 5.5 agent against the `unstable` compiler.
It encodes the rules for computing time, commencement, the holidays and repeal, and lists each of the 159 sections with a disposition.
No one has read the encoding against the official text.
