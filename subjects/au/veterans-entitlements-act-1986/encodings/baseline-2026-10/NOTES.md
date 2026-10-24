# Veterans' Entitlements Act 1986 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. What the Act leaves to indexation or to the Commission's instruments is an input or a fact.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0070` in `subjects/au/requirements.jsonl` (a scheduled priority-2 entry for the 20 topics: pensions and retirement savings). There was no earlier encoding of this Act to keep. No scenario life raised it. The people in the case file are the encoder's, as is every date:
- Ray, a Vietnam veteran;
- Anne, his wife;
- Kerry, an allied veteran.

**Added 24 October 2026 (REQ-0111, in part):** `vea-guide.l4`, a module beside `vea-veteran.l4` that IMPORTs it, brings in the Approved Guide's Table 23.1 (degree of incapacity from the impairment and lifestyle ratings, with the rounding to five points) and the Repatriation Commission's s 37AA determination (permanent incapacity for work), and asks the disability pension rate and invalidity service pension questions again from them: five more exported questions. The pension rates in force after indexation are still inputs (finding 13). Nothing in `vea-veteran.l4` was changed.

Thirteen questions are exported from `vea-veteran.l4`, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Edition

Compilation No. 199, compilation date 1 July 2026, includes amendments up to Act No. 17, 2025 and Act No. 31, 2026 (register id **C2026C00275**, in 4 volumes), as deposited at `../../registers/source-bundle/C2004A03268.txt` (about 2 MB; this baseline reads Parts I, II, III and IX of it).

`vea-guide.l4` reads the **Guide to the Assessment of Rates of Veterans' Pensions (No. 2) 2016** (F2016L01332, the Approved Guide under s 29, as made; the Register's EPUB rendering, retrieved 23 October 2026), deposited at `../../../guide-to-the-assessment-of-rates-of-veterans-pensions-no-2-2016/registers/source-bundle/F2016L01332.txt` with Table 23.1 transcribed in `F2016L01332.tables.md` (the conversion drops table cells), and the **Veterans' Entitlements (Invalidity Service Pension – Permanent Incapacity for Work) Determination 2023** (F2023L01239, as made), deposited at `../../../veterans-entitlements-invalidity-service-pension-permanent-incapacity-for-work-determination-2023/registers/source-bundle/F2023L01239.txt`.

In `vea-veteran.l4` no instrument is brought in. Here is what that leaves open:

- **The pension rates.** The rates in ss 22(3), 22(4), 23(4), 24(4) and 30(1) are indexed twice a year (s 198, s 59LA and Part IIIB Division 18). The figures the compilation prints are therefore not necessarily those in force: $338.94, $510.40, $619.80, $1,595.66, and the $35 and $25.60 of s 30(1). The rates in force are inputs. The cases use the printed figures as stand-ins.
- **Asked as facts:**
  - the degree of incapacity and the impairment and lifestyle ratings (the Commission's, under the Approved Guide, s 29);
  - permanent incapacity for work (the Commission's s 37AA determination);
  - the MRCA commencement date (the MRCA's);
  - "warlike service" and the Schedule 2 areas.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vea-veteran.l4` | `vea-cases-veteran.l4` | 65 written, 65 satisfied |
| `vea-guide.l4` | `vea-cases-guide.l4` | 25 written, 25 satisfied |
| `vea-formulas.l4` (added 2026-10-24, 4 questions, imports `vea-veteran`) | `vea-cases-formulas.l4` | 21 written, 21 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-23); on all six, 2026-10-24, with the 90 earlier assertions unchanged and still satisfied. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The veteran**, and for ss 13A and 30(1), the veteran's **widow or widower**. The questions are the ones that person asks:

- "Can I still claim under the VEA, or is it the MRCA now?"
- "What is my pension age?"
- "Have I got qualifying service?"
- "Am I eligible for a service pension, and from when?"
- "What rate of disability pension am I on, and how much is it?"
- "Does my wife get a war widow's pension when I die without having to claim?"
- "How long do I have to report a change, or to ask for a review?"

The Repatriation Commission's and the Secretary's decisions are asked as facts.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is deposited (see Edition). The MRCA is named where this Act sends the claimant to it, and not encoded. `REQ-0071` in the same ledger covers the MRCA.
- **The actors the text names:** the veteran, the dependant (widow, widower, child), the Repatriation Commission, the Secretary, the Veterans' Review Board and the ART.
- **Judgments left to others, answered conditionally:**
  - the degree of incapacity (s 21A);
  - the Approved Guide ratings;
  - permanent incapacity for work (s 37AA);
  - "genuinely seeking" work (ss 23(3)(b), 24(2)(b), folded into the loss-of-earnings fact);
  - the Secretary's special-circumstances period (s 54(5A)).
- **The Act's own definitions worked out from facts:** pension age (s 5QA), qualifying service (s 7A(1)(a)), the residence rule (ss 36(2)–(3), 37(3)–(5)), the provisional commencement day (s 36B), and which rate applies (ss 22–24). **Borrowed terms asked as facts:** warlike service, the MRCA commencement date, refugee.
- **One case:** one veteran (or one widow or widower).
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** the Commission, the Board, information, offences, delegation.

## Scope

**In:**
- s 12AA: no new Part II, Part IV or s 111 claims from 1 July 2026.
- s 9A: an injury, disease or death that belongs to the MRCA.
- s 5QA: a veteran's pension age.
- s 7A(1)(a): qualifying service. Paragraphs (b)–(h) are asked as one fact.
- ss 36(1)–(3) and 37(1), (3)–(5): eligibility for the age and invalidity service pensions.
- s 36B(1)–(2): the provisional commencement day.
- ss 22(2)–(4), 23(1)–(4), (3A) and 24(1)–(4), (2A): which rate of disability pension applies, and its amount.
- ss 13A(1), (2) and 30(1): the war widow's or widower's pension.
- s 54(5), (5A): the period to report a change.
- ss 57, 57A, 135(5) and 175(2): review.

**Out:**
- The service pension's *rate*: the Rate Calculator in Schedule 6, with its income and assets tests, and the supplements. This is the largest gap: the encoding answers eligibility for a service pension, not how much it pays.
- The partner service pension (s 38), income support supplement (Part IIIA), veteran payment and pension bonus.
- The special rate's rehabilitation and offsetting rules: ss 23(5)–(6), 24(5)–(6), 25A, 115D.
- Temporary special rate (s 25), s 26 reductions, s 27 specific disability amounts, and compensation offsets (Division 5A).
- The dependant child rate (s 30(2)).
- Parts IV–VIA (the Forces and peacekeepers, treatment, allowances, rehabilitation).
- The Veterans' Review Board's procedure, which now sits in Chapter 8 of the MRCA.
- Information, offences (beyond s 54's penalty, quoted) and machinery.

## What the Act turns out to say

1. **No new disability or war widow's pension claims can be made under this Act from 1 July 2026.** Section 12AA says that "a claim or application may not be made" under Part II (other than Division 2A), Part IV, s 111 (other than bereavement payment) or instruments under ss 105–106 "on or after the date of commencement", and s 5Q defines that as "1 July 2026". Note 1 sends such claims to the MRCA. Part II covers the disability pension and the war widow's and widower's pension. Service pensions (Part III) and income support supplement (Part IIIA) are not listed, so claims for them continue. The ledger entry's question ("Am I eligible for a disability pension") therefore has two answers. For a veteran already on one, this Act still sets the rate. For a new claim from 1 July 2026, it is the MRCA's question. Asserted.
2. **Injury on later service has been the MRCA's for years.** Under s 9A, an injury, disease or death on or after the MRCA commencement date that relates to service on or after that date "is taken not to be war-caused". So long before 2026, the VEA did not cover it. Asserted.
3. **A veteran's pension age is 60.** For a man it is 60 (s 5QA(2)). For a woman born before 1 July 1940 it is 55, rising 6 months for each 18-month birth cohort, to 60 for a woman born on or after 1 January 1954. That is five years below the non-veteran pension age of s 5QB. Asserted (each band edge tested).
4. **Commonwealth and allied veterans need 10 years' residence, which can be shortened.** A veteran who is one only as a Commonwealth or allied veteran or allied mariner needs 10 years' continuous Australian residence (ss 36(2), 37(3)), unless a refugee. The 10 years shrink by the excess of total residence over 10, if the longest period is at least 5 years (ss 36(3), 37(4)). With a longest period of 7 years and 13 in total, the requirement is 7 and is met. With 6 and 13 it is not. With a total of exactly 10 there is no reduction. For the invalidity service pension, the rule does not apply if the incapacity began while resident, was not brought about to get a pension, and is uncompensated (s 37(5)). Asserted.
5. **A defective claim can still fix the start date.** If the first claim was not a proper claim, the pension can run from that first claim if the veteran was eligible then, and lodges a proper claim within 3 months of being told, or at any time if never told (s 36B(2)). The encoding reads "within 3 months after" day N as on or before the same date 3 months later, or the last day of a shorter month: 30 November 2026 gives 28 February 2027. Asserted.
6. **The rate depends on work as well as the percentage.** The special (TPI) rate needs all of these (s 24(1)):
   - at least 70% incapacity;
   - inability, from the war-caused incapacity "of itself alone", to work more than 8 hours a week;
   - loss of earnings caused by it.

   For a claim made at 65 or over, s 24(2A) adds that the last job was after 65, following 10 continuous years of work begun before 65. Blindness in both eyes is enough on its own (s 24(3)). The intermediate rate (s 23) is the same, for someone able to work only part-time (under half of full-time hours, or under 20 hours a week). The extreme disablement adjustment (s 22(4)) needs 100%, age 65 or over, at least 70 impairment points and at least 6 lifestyle points, and no s 23–25 rate. Otherwise the pension is the degree of incapacity as a percentage of the general rate (s 22(2)). Asserted, including that the special rate wins over the EDA for someone qualified for both.
7. **The widow of a veteran on a top rate needs no claim.** If, just before death, the veteran was on the EDA or the intermediate, special or temporary special rate (or certain s 27 rates), the widow's or widower's pension is paid "without the dependant having to make a claim", from the day after the death (s 13A). Since 1 July 2026 no Part II claim can be made, so that automatic route is what is left under this Act. The rate is 1/26 of the annual single service pension MBR, plus two indexed amounts printed as $35 and $25.60 (s 30(1)). Asserted.
8. **Service pension reviews and disability pension reviews follow different routes, both with 3 months.**
   - **Service pension decisions:** the veteran asks the Commission in writing, with grounds, lodged at a Department office in Australia, within 3 months of notice (s 57A), and then may go to the ART (s 175(2)).
   - **Disability pension rate decisions:** the application goes to the Veterans' Review Board under Chapter 8 of the MRCA, within 3 months of service of the decision, "but not otherwise" (s 135(5)).

   Asserted.
9. **A notice to report a change can give 14 days, or up to 28.** A notice under s 54 must give no more than 14 days from the change. In special circumstances the Secretary may direct 15 to 28 days. Failing to comply is a strict liability offence (6 months' imprisonment or 10 penalty units, or both). Asserted (the days).

10. **The degree of incapacity is a table lookup on two ratings.** The Guide rounds the combined impairment rating to the nearest five points and reads Table 23.1 at that row and the lifestyle rating's column (0 to 7). Rows 65 to 90 give 100% at every lifestyle rating; some low-impairment, high-lifestyle cells and the lifestyle-0 cells from 35 up are "N/A", which `vea-guide.l4` answers as no degree. The table has no row above 90: a rounded rating of 95 or 100 answers `not covered` rather than assume 100. The rounded rating is also the one the Guide uses for the extreme disablement adjustment's 70 points. Asserted.
11. **Permanent incapacity for work for the invalidity service pension is mostly automatic.** The 2023 Determination s 7 makes a veteran permanently incapacitated if blind in both eyes, on the special rate, on (or barred only by MRCA ss 204, 415 from) an MRCA Special Rate Disability Pension, or found by the MRCC to meet MRCA s 199(1); otherwise only if an impairment would rate 40 or more under Table 18.1, permanently prevents work over 8 hours a week, and the Commission is satisfied it is permanent. Section 6 carries over those incapacitated under the 2013 Determination. The deposit has lost the label "(a)" of the first limb; the text is otherwise whole. Asserted.
12. **Table 24.1's minimum degrees are not encoded.** For listed disabilities (loss of limbs or eyes, total deafness and others) Chapter 24 sets a minimum degree that overrides a lower Table 23.1 result. `vea-guide.l4` does not apply it; for a veteran with such a disability, the Commission's degree is the input to `vea-veteran.l4`'s question. Not asserted.
13. **The rates in force are still inputs.** The disability pension and war widow's pension rates are substituted on each 20 March and 20 September (s 198(5DA), (5E), (8A), by formulas built on the pension MBR factor of s 59LA and the CPI), but those formulas are lost from the deposited text, and DVA's published rate tables could not be fetched (www.dva.gov.au did not answer the fetcher; treated as a refusal). So no rate in force is computed, and a new ledger entry asks for them. Not asserted (a finding about the sources).

14. **The indexation formulas are now in, from the sidecar (2026-10-24).** Finding 13's lost formulas are transcribed in `../../registers/source-bundle/C2004A03268.formulas.md` (from the authorised Word rendering of the same compilation, each checked against its image): each of the general rate, the three above general rates and the s 30(1)(b) amount becomes "the rate on the day before the adjustment day × Pension MBR factor for the adjustment day", rounded up to the nearest $0.10 (s 198(5DA), (5E), (8A)), and the pension MBR factor is "Current single pension rate MBR amount / Previous single pension rate MBR amount", to 3 places with the 0.001 rule and not below 1 (s 59LA(1), (2A)). `vea-formulas.l4` computes them, and the CPI-indexed s 198(4), (5) relevant rates (including the s 30(1)(c) amount, to the nearest $0.10 with 5 cents up) from the words, and passes the indexed rates to `vea-veteran.l4`'s rate and war widow's questions. Asserted.
15. **The rates in force are still not derived from deposited text alone.** The pension MBR factor rests on the single pension rate MBR amount (s 59A item 1A), which s 59G adjusts from the CPI, the PBLCI and the MTAWE benchmark, none of them deposited; and the rate on the day before the last adjustment day must be known. With those as inputs the rates are computed; REQ-0111 stays open for the figures. Not asserted (a finding about the sources).
16. **A rate not on a 10-cent multiple is rounded up on every adjustment day, even at a factor of 1.** The substitution of s 198(5DA) and (5E) is made "on each adjustment day", and the factor is raised to 1 when the MBR amount falls (s 59LA(2A)(b)); so the compilation's $338.94 becomes $339.00 at the next adjustment day whatever happens to the MBR amount. The printed figures, not being multiples of $0.10, cannot themselves be products of these subsections (they were reset by amending Acts). Read literally. Asserted.
17. **Two different roundings sit side by side in s 198.** The MBR-indexed rates are rounded up to the next $0.10 ((5DA), (5E), (8A)); the CPI-indexed relevant rates, including s 30(1)(c), go to the nearest $0.10 with 5 cents up ((4)(b)). Asserted.
18. **No earlier case supplied a figure that a formula now produces differently.** The earlier rate cases take the printed figures as the rates in force; the new questions take them as the rates on the day before an adjustment day, so the two sets of answers differ by one indexation, as they should. "Worked out to 3 decimal places" is read as cutting off after the third place (an INFERENCE). Not asserted (a note on the cases).

## What would need doing before this is worth relying on

- **The rates in force** (the s 198 and Part IIIB indexation results), so that the rate questions take no rate inputs: the formulas are now encoded (`vea-formulas.l4`); still needed are the single pension rate MBR amounts on each adjustment day (or the CPI, PBLCI and MTAWE figures behind s 59G) and the CPI index numbers, or DVA's published rates (REQ-0111). The **Approved Guide** (Table 23.1) and the **s 37AA determination** are deposited and used since 24 October 2026 (`REQ-0111`); the rest of the Guide (the impairment tables, Table 18.1, Table 24.1) is not encoded.
- **The Schedule 6 Rate Calculator** for the service pension's rate, in the manner of the Social Security Act 1991 baseline's Pension Rate Calculator A, which it closely parallels. Not raised: it is in this Act and needs only a larger encoding of it.
- **The MRCA** (`REQ-0071`), which now takes every new claim for a disability or war widow's pension.
- **Pending claims at 1 July 2026** are now answered by the Consequential and Transitional Provisions Act baseline (`subjects/au/military-rehabilitation-and-compensation-consequential-and-transitional-provisions-act-2004/encodings/baseline-2026-10/`, `REQ-0109`): a VEA claim made before 1 July 2026 of a kind s 12AA closes, and not finally determined by then, continues under this Act, including review (that Act's s 89); a pending prisoner of war claim or Part VII application becomes an MRCA claim (its ss 110, 112). This baseline has no `not covered` answer for pre-2004 conditions, so nothing in its code changes.
- **Wider sources.** No DVA policy (CLIK), ruling or case was read. The reading in finding 5 of "within 3 months" at a month end is an interpretive choice.
