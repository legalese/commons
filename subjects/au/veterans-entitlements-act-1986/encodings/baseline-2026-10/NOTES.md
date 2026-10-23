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

Thirteen questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Edition

Compilation No. 199, compilation date 1 July 2026, includes amendments up to Act No. 17, 2025 and Act No. 31, 2026 (register id **C2026C00275**, in 4 volumes), as deposited at `../../registers/source-bundle/C2004A03268.txt` (about 2 MB; this baseline reads Parts I, II, III and IX of it).

No instrument is deposited. Here is what that leaves open:

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

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

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

## What would need doing before this is worth relying on

- **The rates in force** (the s 198 and Part IIIB indexation results), the **Approved Guide** (s 29) and the Commission's **s 37AA determination**, deposited, so that the rate and invalidity questions take fewer inputs. Raised as `REQ-0111`.
- **The Schedule 6 Rate Calculator** for the service pension's rate, in the manner of the Social Security Act 1991 baseline's Pension Rate Calculator A, which it closely parallels. Not raised: it is in this Act and needs only a larger encoding of it.
- **The MRCA** (`REQ-0071`), which now takes every new claim for a disability or war widow's pension.
- **Wider sources.** No DVA policy (CLIK), ruling or case was read. The reading in finding 5 of "within 3 months" at a month end is an interpretive choice.
