# Duties Act 2001 (Tas), with the First Home Owner Grant Act 2000 and Regulations 2021: baseline encoding for the buyer

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers `not covered`, naming the gap, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

**The First Home Owner Grant Act 2000 and the First Home Owner Grant Regulations 2021 are encoded here, in this folder, with no encoding in their own folders** (`../../../first-home-owner-grant-act-2000/` and `../../../first-home-owner-grant-regulations-2021/` hold their deposits only). The law ties the three instruments together:

- the duty reliefs borrow the grant Act's "home", "new home" and "owner" (Duties Act s 3 "home" (b), ss 46A, 46J, 57C);
- a grant already paid disqualifies a buyer from the duty reliefs (ss 46C(4)(b), 57E(4)(b));
- the duty exemption covers established homes and the grant covers new homes (FHOG Act s 13(1)(ab) since 1 July 2014), so a buyer's first question is which of the two applies;
- the grant can be applied to the duty (FHOG Act s 19(3));
- both have Help to Buy carve-outs (Duties Act s 32; FHOG Act s 5(2A), Regulations reg 5A).

Keeping them together keeps the Tasmanian tax-and-benefits plan at five encodings.

It is written in two layers:

- **The seat-neutral core**, in the Acts' own actors and terms ("the transferee", "the applicant", "the Commissioner", "an eligible first home buyer", "an eligible pensioner"):
  - `tda-common.l4`: arithmetic, the s 242 month rule, the `not covered` reasons, the parties and acts, and the residence requirement that both Acts state in the same words, as one regulative rule, with the fine for not acting on a failure (ss 46F(6), 57H(6); FHOG Act s 20(4));
  - `fhog-terms.l4`: FHOG Act ss 3-6 (home, new home, established home, relevant interest, owner, spouse, residential property), encoded once and used by both Acts; the Duties Act's own "spouse" (s 3) beside it;
  - `tda-transfer.l4`: Duties Act Chapter 2 (dutiable value, the s 29 scale as a table, s 32, "foreign person" (s 3), the reach of Division 2C, the three reliefs, which of the exemption and the grant a kind of home can open, lodging and paying);
  - `tda-vehicles.l4`: Duties Act Chapter 8 (motor vehicle duty);
  - `fhog-grant.l4`: FHOG Act Part 2 with ss 20 (including what s 20(3A) asks after the interest is given up), 21, 38 and Regulations regs 4, 5, 5A.

  Computations (duty, dutiable value, grant amount) are functions. Where the text says "must", "may" or sets a deadline there is a regulative rule (`DEONTIC`): ten in all (the residence requirement and what follows a failure of it; ss 13-15; the s 57H/46F and s 12/20 forms of the residence requirement; ss 193(1), 196, 196A; FHOG s 14(5); s 19(3); s 20(2), (3A); s 38).
- **`tda-seat.l4`, the buyer's seat.** It asks 29 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a buyer meets them: the duty, new or established, the reliefs, the duty payable, after settlement, the grant, after completion, the vehicle. It builds the core's records from plain answers and restates no rule. The "after settlement" and "after completion" groups arise only when the exemption was given or the grant was paid early, and their headings say so.

## Edition

- **Duties Act 2001** (No. 15 of 2001): consolidation published 2026-10-13, current on the site at 2026-10-20, deposited at `../../registers/source-bundle/act-2001-015.txt` (retrieved 2026-10-19T17:10:28Z).
- **First Home Owner Grant Act 2000** (No. 19 of 2000): consolidation published 2026-10-14, deposited at `../../../first-home-owner-grant-act-2000/registers/source-bundle/act-2000-019.txt`.
- **First Home Owner Grant Regulations 2021** (S.R. 2021, No. 33): consolidation published 2026-06-11, deposited at `../../../first-home-owner-grant-regulations-2021/registers/source-bundle/sr-2021-033.txt`.

Not deposited, and so inputs or text defaults:

- **Extension orders** under ss 46B, 46K, 46T and 57D. The end of each eligible period is a field of `Duty settings` in the core, defaulting to the text: 30 June 2026 (s 57C), 30 June 2024 (s 46A), 30 June 2025 (s 46J), and 30 June 2026 for Division 2C (s 46S), which is not encoded but whose period sets which transfers it can reach (finding 18). The consolidation folds earlier orders into the text (s 46A's history lists S.R. 2019 Nos 2 and 29, S.R. 2020 No 26 and S.R. 2023 No 24; the jurisdiction README notes the 2023 order's clauses are incorporated), so these are the dates in force on 13 October 2026 unless an order was made after that.
- **The Duties Regulations 2021**, which may prescribe the caps in ss 46D(1)(d), 46M(c) and 57F(1)(d). The caps are `Duty settings` fields defaulting to the text's "if no amount is prescribed" figures: $600 000, $600 000 and $750 000.
- **The caps in ss 46D(1)(d) and 46M(c) before 1 January 2022.** Both paragraphs were amended by No. 8 of 2021 (applied 16 March 2021) and No. 8 of 2022 (applied 1 January 2022), and the consolidation shows only the text from 1 January 2022. A transfer before that day whose Division 2A or 2B answer turns on the cap answers `not covered` (finding 17), as a transfer before 21 October 2013 does for s 29.
- **The Taxation Administration Act 1997** (interest, penalty tax, objections): not deposited. The breaches name it and stop there.

The seat uses the deposited text's settings. Under the guide's rule for figures a minister can change, the buyer cannot state an extension order or a prescribed amount, so the seat does not ask. An order or a regulation would change its answers, and the core cases assert both sides.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tda-common.l4`, `fhog-terms.l4`, `tda-transfer.l4` | `tda-cases-transfer.l4` | 128 written, 128 satisfied |
| `tda-common.l4`, `tda-vehicles.l4` | `tda-cases-vehicles.l4` | 50 written, 50 satisfied |
| `tda-common.l4`, `fhog-terms.l4`, `fhog-grant.l4` | `fhog-cases-grant.l4` | 105 written, 105 satisfied |
| all modules, `tda-seat.l4` | `tda-cases-seat.l4` | 93 written, 93 satisfied |

376 assertions in all. In addition, 12 `#TRACE`s carry an `-- expect:` line: six breaches (s 15 late payment, a missed s 57H(6) notice, s 193(1), ss 196/196A by the applicant, ss 195(b)/196/196A by the person acquiring the beneficial ownership after a notice, the FHOG s 20 repayment) and six obligations still pending (the s 57H(6) notice in three situations: never moved in, interest given up, left too late to start again; the Commissioner's s 57I(2) power to reassess once the notice is given; the FHOG s 20 notice and repayment; and the Commissioner's s 38(3) power to impose a penalty). Each was read and matches its expectation.

`l4 run` on all ten files: 0 errors, 0 warnings (2026-10-24, after the corrections below). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A control copy of the transfer cases with one expected value altered ($18 247.50 to $18 247.75) reported the failures, as it should; after the corrections a second control copy with two of the new expected values altered ($6 998.75 to $6 998.50 on 1 January 2022; $18 247.50 to $18 247.75 for the off-the-plan unit outside Division 2C) reported exactly those two failures.

Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion. `tda-cases-seat.l4` takes about two minutes to run.

## Seat

**The buyer:**

- the transferee of a home: a first home buyer, or a pensioner who is downsizing;
- the applicant for the first home owner grant;
- the person who applies to register a motor vehicle, or gives notice of a change of its beneficial ownership, or acquires that ownership and so pays the duty (s 195(b)).

They ask:

- "What transfer duty is payable on this home, transferred on this date?"
- "Is the duty nil under the first home buyer exemption, or halved under the pensioner concession?"
- "Am I entitled to the first home owner grant, and how much is it?"
- "After settlement, what must I do and by when, and what follows if I don't?"
- "What duty is payable to register this vehicle?"

The vehicle rules name their parties as the Act does: for an application, the applicant lodges the s 193(1) statement and pays (s 195(a)); for a notice of a change of beneficial ownership, "the person giving the notice" lodges the statement and "the person acquiring the beneficial ownership" pays (s 195(b)), on the day the notice is lodged (s 196(a)(ii)).

The **Commissioner of State Revenue** is a party to the regulative rules (the power to reassess, s 57I(2); to apply the grant to duty, s 19(3); to impose a penalty, s 38(3)), never a seat. No other party has duties that would earn a second seat: the vendor bears none under these provisions, and Housing Australia and Homes Tasmania appear only as interests left out. So there is one seat, and there are no mirror cases.

**The seat's reach.** The questions take one buyer, or one buyer and one other individual, plus the Commonwealth or Housing Australia under Help to Buy. The buyer asking is the pensioner in the pensioner questions. The core takes any number of transferees and applicants.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The FHOG Act and Regulations are brought in because the Duties Act borrows their terms (above). The Duties Regulations and extension orders are not deposited, so they are settings with text defaults (Edition).
- **The actors the text names.** Followed: the transferee, the applicant, the applicant for registration, the Commissioner.
- **Judgments left to someone else are answered conditionally, as inputs.** Followed. The Commissioner's satisfaction, opinion or approval comes in as a fact the buyer states:
  - intention to meet the residence requirement (ss 46D(1)(c), 46M(b), 57F(1)(c));
  - good reasons (ss 46D(2), 57F(2), 46N(4));
  - age exemptions (ss 46C(2), 57E(2), FHOG s 8(2));
  - longer or lesser periods (s 57H(1)(b), (2); FHOG s 12(1A));
  - joint-transferee exemptions (s 57H(4); FHOG s 12(2));
  - suitability of a building (FHOG s 4(b));
  - the s 5(2) and s 5(4) recognitions;
  - a scheme (s 13(3));
  - allowing an application outside the application period (s 14(6));
  - replacement transactions and extended completion (ss 18D-18M);
  - adequacy of a new vehicle's price (s 198(1A)).

  Each such `@desc` names the Commissioner's part, most with "the Commissioner must also be of that opinion" or "answer no unless told so".
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.** Followed. Worked out:
  - home, new home, established home, relevant interest, owner, spouse (both Acts), residential property;
  - dutiable value (s 18; s 198);
  - eligible first home buyer, eligible pensioner, eligible transaction (all three schemes);
  - passenger vehicle; manufacturer's fleet discount;
  - eligibility criteria 1-5; eligible transaction (s 13); the application period; interested person (s 15).

  Asked as facts:
  - Australian citizen and permanent resident (Commonwealth Acts);
  - significant relationship (Relationships Act 2003);
  - new residential premises (GST Act s 40-75(1)(b));
  - heavy vehicle (Heavy Vehicle National Law);
  - Pensioner Concession Card, Seniors Health Card, special rate pension (Social Security Act 1991, Veterans' Entitlements Act 1986);
  - Help to Buy arrangement (Help to Buy Act 2024);
  - foreign corporation or foreign trustee (s 3 "foreign person" (a), (c); ss 4A-4C not encoded). A foreign natural person, limb (b), is worked out in the core from the citizenship answer (s 3: "a natural person who is not an Australian citizen or a permanent resident"); the seat's buyers are individuals, so the seat passes the corporation-or-trustee fact as a fixed FALSE.
- **One case is the text's natural unit.** Followed: one home transfer, one grant application, one vehicle application.
- **The Act's own terms, each with a plain gloss.** Followed: the comment above each rule quotes the text.
- **Machinery out.** Followed: FHOG Act Parts 3-4 other than ss 20, 21 and 38; objections and appeals; the Taxation Administration Act.
- **The seat restates no rule.** Followed, after the corrections of 24 October 2026: the fines (ss 46F(6), 57H(6); FHOG s 20(4)), the s 20(3A) exemption carve-out, "foreign person" (s 3) and the answer to "which relief can apply" (s 57F(1); FHOG s 13(1)) are all in the core, and the seat only builds records and calls them. Every fixed placeholder the seat passes carries a comment saying the rule does not read it.

**Departures:**

- The seat folds the two limbs of "new home" (b) (substantially renovated; not occupied or sold since) into one answer.
- The seat asks "fixed to the land" and "may lawfully be lived in" (s 4(a)) as one answer.

## Scope

**In:**

- Duties Act 2001:
  - ss 6(1)(a), 9(1)(a), 10, 11, 12; ss 13, 14, 15 (regulative); s 17; ss 18-20; s 29 (table); s 32;
  - Part 5 Division 2A ss 46A-46F, as a dated case (transfers 7 February 2018 to 30 June 2024; 50%; $600 000 from 1 January 2022, the cap before then not deposited), with the s 46F residence requirement;
  - Part 5 Division 2B ss 46J-46O (with s 46P noted; the s 46M(c) cap likewise known only from 1 January 2022);
  - s 3 "foreign natural person" and "foreign person" (to decide whether Part 3A could apply);
  - the reach of Part 5 Division 2C: s 46S (eligible period, a setting), s 46V(2) (eligible dwelling, a fact), s 46W(2)(b), (c), (e);
  - Part 6 Division 2 ss 57C-57I (s 57H regulative; s 57I as the Commissioner's permission and the duty it may reassess);
  - Chapter 8 ss 192, 193(1), 195, 196, 196A, 197, 198 (ss 193(1), 195, 196, 196A regulative, with the notice-giver and the acquirer as parties).
- First Home Owner Grant Act 2000:
  - ss 3-6; s 7; ss 8-12; s 13 (except (6)); s 14(5)-(6); s 15;
  - s 18 with ss 18D-18M as a dated table, and the s 18(2)(b) amounts;
  - s 19(3); s 20 (regulative); s 21(3) (joint applicants are one party, compliance by one is compliance by all); s 38 (regulative).
- First Home Owner Grant Regulations 2021: regs 4, 5, 5A.

**Out (each answers `not covered` where a question can reach it):**

- Part 3A additional duty for foreign purchasers, and s 30J. Reached only where no relief applies (finding 8).
- Division 2C, the pre-completion concession: a transfer it could reach (a strata or conjoined dwelling with no occupancy permit when the agreement was executed, the agreement executed from 1 July 2024 to 30 June 2026 as deposited, the transfer before 30 June 2031) answers `not covered`; any other transfer is answered by the encoded rules (finding 18). s 46X(2)'s bar on the grant is honoured as a fact.
- A Division 2A or 2B transfer before 1 January 2022 that turns on the cap (finding 17): `not covered`.
- Chapter 3 landholders; Part 5 Divisions 1 and 2 (trusts, superannuation); insurance duty (Chapter 7).
- The Part 6 Division 1 exemptions; the s 19(2)-(6) house-and-land improvements rule; ss 21-28 except as glossed.
- Vehicle exemptions and refunds (ss 199-203: `not covered`); dealers' certificates (ss 203A-218).
- Taxation Administration Act 1997 interest and penalties.
- FHOG Act: ss 18A-18C for new homes (1 January 2013 to 31 December 2015: `not covered`; an established-home contract in that window takes $7 000 on the reading in finding 19), s 18 before 1 January 2013 (`not covered`), the ss 18L(5) and 18M(5) top-ups, s 13(6) moveable buildings (`not covered`), ss 16, 17(2), 22, 23 (except as the trigger for s 38), 25-29, Parts 3-4 other than ss 20, 21 and 38.
- Transfers before 21 October 2013 (when the s 29 scale was last amended) and vehicle applications before 1 October 2007: `not covered`.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Social Security Act 1991**, `../../../../social-security-act-1991/encodings/baseline-2026-10/`: the Pensioner Concession Card and the Commonwealth Seniors Health Card (ss 1061ZG, 1071 in that encoding) that open the pensioner duty concession (s 46L(1)(b)(i)-(ii)). Here they are facts.
- **Veterans' Entitlements Act 1986**, `../../../../veterans-entitlements-act-1986/encodings/baseline-2026-10/`: the special rate pension (s 24) that also opens it (s 46L(1)(b)(iii)), and the Pensioner Concession Card issued under that Act ("a relevant Act of the Commonwealth").
- **Help to Buy Act 2024**, `../../../../help-to-buy-act-2024/`: the subject exists, with its text deposited, but is not encoded. "Help to Buy arrangement" (Duties Act s 3, FHOG Act s 3) is its term, and a fact here.
- **Income Tax Assessment Act 1997**, `../../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/`: the grant's income tax treatment. Neither the deposited ITAA 1997 nor its encoding names the first home owner grant, so the encoding answers nothing about it. The usual view, that a grant towards a private home is not ordinary or statutory income, is not encoded anywhere in Commons.

## What the Acts turn out to say

1. **The first home buyer duty exemption has lapsed, as deposited.** The eligible period in s 57C ended on **30 June 2026**, and the consolidation of 13 October 2026 shows no extension order. So a first home buyer whose transfer occurs today pays the full s 29 duty: **$18 247.50** on a $500 000 established home, against nil on 30 June 2026. A s 57D order made but not yet consolidated would change this. Asserted both sides, with a hypothetical extension to 30 June 2027.
2. **Any earlier home ownership bars the duty exemption; the grant is more forgiving.** Section 57E(4)(a) excludes a buyer who, or whose spouse, "has previously been the owner of a home" anywhere in Australia, even an investment property never lived in. The grant's criterion 4 (FHOG s 11) bars only an interest held before 1 July 2000, or a home owned *and lived in* for 6 continuous months. Asserted.
3. **The pensioner concession is closed, through the sale of the former home.** Section 46M sets no period for the purchase. The eligible period (ending **30 June 2025**) bites through ss 46N(1)(a)(ii) and 46O(1)(a)(ii), on the transfer of the *former* home, which must also fall within 6 months before or after the purchase. So a purchase on 1 December 2025 after a sale on 30 June 2025 still qualifies. A purchase after 31 December 2025, and any purchase today, cannot: $16 122.50 rather than $8 061.25 on a $450 000 home. Asserted both sides.
4. **The two first home buyer reliefs overlapped from 18 February to 30 June 2024.** Division 2A ran to 30 June 2024 (50%, $600 000 cap) and Part 6 Division 2 from 18 February 2024 (nil, $750 000 cap). The text does not say which applies, and the encoding takes nil. In the overlap, a buyer whose spouse had an earlier Part 6 Division 2 exemption could still have the Division 2A concession, because s 46C(4) has no bar like s 57E(4)(d). Asserted.
5. **An exempt first home buyer has, by the words, no duty to lodge within 3 months.** Section 14 binds "a transferee who is liable to pay duty", and s 13 "a dutiable transaction that is liable to ad valorem duty"; s 57G makes duty "not chargeable". In practice the exemption is claimed by lodging (the Commissioner must be satisfied, s 57E), and s 243 bars registering an unstamped or unendorsed instrument. Neither is a 3-month duty. The encoding's ss 13-15 rule binds nothing when no duty is payable. Asserted.
6. **Help to Buy (s 32, from 5 June 2026) is read as leaving the Commonwealth's share out entirely.** "No account is to be taken of any interest the Commonwealth or Housing Australia has in the land." The encoding drops Housing Australia from every "each transferee" and "at least one transferee" test and charges the buyer on the whole dutiable value. The words also bear the reading that duty falls only on the buyer's share; that reading is not taken. Asserted (the transferees counted, and the exemption passing with Housing Australia on title).
7. **The grant now reaches only new homes, and has gaps.** Since 1 July 2014 a contract to buy qualifies only for a new home (s 13(1)(ab)); an established home gets the duty exemption instead (while it lasted), never the grant. As deposited:
   - no increased amount covers contracts commencing **1 July 2024 to 30 June 2025** (s 18K ended, s 18L had not begun), so they get **$10 000**;
   - the same holds from **1 July 2027**, after s 18M;
   - contracts from 1 July 2025 get $30 000 (s 18L), and from 1 July 2026 to 30 June 2027 $20 000 (s 18M), if completed within 24 months.

   Asserted.
8. **A foreign co-buyer does not spoil the exemption, and the exemption removes foreign purchaser duty too.** Section 57E(3) lets a temporary-visa partner join a citizen. Section 57G makes duty "not chargeable under this Chapter", and Part 3A is in Chapter 2. For the Part 5 concessions, s 30G(1) switches Part 3A off. So the couple pays nil, Part 3A included. Without a relief, Part 3A applies to the foreign buyer's share (s 30C(3)), and the encoding answers `not covered`. Asserted.
9. **"Spouse" differs between the Acts.** FHOG Act s 6(2) excludes a legal spouse who is living apart with no intention of resuming; Duties Act s 3 has no such rule. So a separated spouse's home ownership bars the duty exemption but not the grant. Asserted.
10. **The residence requirement is a continuous 6 months *commencing* within the 12 months.** A buyer who moves in and leaves early can still meet it by starting a fresh 6 months while the 12 months run. Leaving early is a failure only once the time to begin has passed. Giving up the interest during the stay is a failure at once (s 57H(5), FHOG s 12(3) and s 20(3A)). Asserted. Limit: giving up the interest before moving in is not caught by the trace form; the seat's situation questions answer that case.
11. **Every owner must apply for the grant, and each must qualify.** Section 15 makes every interested person an applicant, and s 7(1)(a) requires each to meet the criteria. So a parent on the title who has owned and lived in a home defeats the grant, whether or not the parent applies. Homes Tasmania and Housing Australia under Help to Buy are excluded (regs 5, 5A). Reg 5A repeats what s 5(2A) already does: a Help to Buy interest is no relevant interest, so Housing Australia is not an owner to begin with. Asserted.
12. **Vehicle duty has a steep band and a fleet-discount trap.**
    - Passenger vehicles between $35 000 and $40 000 pay $11 per $100 at the margin (s 197(2)(b)), moving from 3% to 4% of the whole value: $1 380 at $38 000.
    - The manufacturer's fleet discount rate (s 197(3A), $3.50 per $100) applies "despite subsection (2)". So a new fleet-discounted car below about $37 300 pays *more* than the same car without the discount: $1 050 against $900 at $30 000.

    Asserted.
13. **The $20 fixed duty (s 197(3)) is read as prevailing over the per-$100 rates.** Section 197(3) fixes $20 for a heavy vehicle worth $2 000 or less; s 197(3B) alone would charge $10 at $1 000. Section 197(3) is read as prevailing, and it also lifts a $600 car from $18 to $20; a $601 car pays $21. Asserted.
14. **A grant once paid bars the duty exemption even if it was paid back.** Section 57E(4)(b) asks whether the buyer or spouse "has previously been paid" a grant "under the First Home Owner Grant Act 2000"; FHOG s 10(2) forgives a grant paid back. A grant under another State's law is not named, but the ownership it implies is caught by (4)(a). The seat's `@desc` says so; no separate assertion.
15. **The pensioner concession carries no residence duty after the transfer.** Unlike Division 2A (s 46F) and Part 6 Division 2 (s 57H), Division 2B has no requirement to move in or stay and no duty to notify. Section 46P only lets the Commissioner reassess if the Division's requirements were not met, for example a former home not sold within 6 months after a s 46O purchase. There is therefore no regulative rule for it.
16. **The grant can pay the duty on the new home.** A new home pays the s 29 duty (the exemption is for established homes). At the buyer's request the Commissioner may apply the grant to it (s 19(3)): the $19 097.50 duty on a $520 000 new townhouse is cleared by a $20 000 grant, with $902.50 left over. Asserted.
17. **The Division 2A and 2B caps before 1 January 2022 are not in the deposit.** Sections 46D(1)(d) and 46M(c) carry the history notes "amended by No. 8 of 2021 ... Applied:16 Mar 2021" and "amended by No. 8 of 2022 ... Applied:01 Jan 2022", placed at those paragraphs. The consolidation shows the cap only as it reads from 1 January 2022 ($600 000, or the prescribed amount). The first version of this encoding applied $600 000 back to 7 February 2018 (Division 2A) and 10 February 2018 (Division 2B). That conflicted with its own rule for s 29 before 21 October 2013, s 197 before 1 October 2007 and FHOG s 18 before 1 January 2013. Corrected: a transfer before 1 January 2022 that meets every other requirement of Division 2A or 2B answers `not covered`, and so does its duty. One that fails another requirement answers that failure, because the cap cannot save it. So Alex's $400 000 purchase on 7 February 2018, asserted before as an eligible transaction, is now `not covered`. On 31 December 2021 it is `not covered`; on 1 January 2022 the duty is half of $13 997.50, $6 998.75. A pensioner who sold on 1 September 2021 and bought on 1 November 2021 is `not covered`; with a former home worth less than the new one, the answer is no and $16 122.50. No asserted figure was shown to be wrong. Asserted.
18. **Division 2C reaches only agreements executed in its eligible period.** Section 46W(2) requires "(b) ... an eligible dwelling in respect of which an application for an occupancy permit has not been granted at the time at which the agreement for sale is executed", "(c) the agreement for sale ... is executed during the eligible period" (1 July 2024 to 30 June 2026, s 46S, extendable under s 46T), and "(e) the transfer ... occurs before the fifth anniversary of the end of the eligible period". The first version answered `not covered` for every off-the-plan strata or shared-wall purchase under an agreement from 1 July 2024, with no end date. Corrected: only a transfer that meets (b), (c) and (e) is `not covered`; the agreement date is now asked. An off-the-plan unit under an agreement of 1 August 2026, transferred 1 March 2027, pays the s 29 duty, $18 247.50 on $500 000. Under a hypothetical s 46T extension to 30 June 2027 it is `not covered`. A transfer on 30 June 2031, the fifth anniversary, is outside (e) and pays $18 247.50. Asserted.
19. **ss 18A-18C are read as reaching only new homes (READING).** Sections 18A(2), 18B(2) and 18C(2) say "An eligible transaction satisfies this section if -- (a) the commencement date ... ; and (b) where the eligible transaction is -- (i) ... (iv) [four kinds, each for a new home]". The encoding reads (b) as the list of kinds that can satisfy the section. So a contract for an established home, which could be an eligible transaction only before 1 July 2014 (s 13(1)(a)), satisfies none of them and takes $7 000 (s 18(2)(b)(i)). Item (iv) supports this reading: it adds nothing but completion, which s 7(1)(b)(ii) requires anyway. The words also bear the reading that (b) sets conditions only for the kinds it names. On that reading an established-home contract would meet the section on (a) alone: $15 000 (s 18A), $30 000 (s 18B) or $20 000 (s 18C). That reading is not taken. This was the encoding's reading before, but it was not flagged. It is now marked READING in `fhog-grant.l4`. Asserted ($7 000 on a 1 March 2014 contract for an established home, which would be $30 000 on the other reading).
20. **A notice of a change of beneficial ownership binds two people the Act names apart.** Section 193(1) binds "a person who is required by law to ... give a notice of a change of beneficial ownership" to lodge the statement of dutiable value with it. Section 195(b) makes "the person acquiring the beneficial ownership" liable for the duty, which becomes payable when the notice is lodged (s 196(a)(ii)). The first version bound "the applicant to register the vehicle" to both, even for a notice. Corrected: the rule now takes the dealing and binds the notice-giver to the statement and the acquirer to the payment. Asserted (fulfilled), with a `#TRACE` of the acquirer's breach.

## Corrections of 24 October 2026

An independent verifier raised six issues. Each was checked against the deposited texts:

1. Division 2A and 2B caps applied back to 2018: **fixed** (finding 17).
2. An unflagged reading of FHOG ss 18A-18C: **fixed** by marking it READING and adding finding 19. The reading is kept and the asserted $7 000 stands.
3. The seat restated law: **fixed**.
   - The fines (`the most fine, in penalty units, for not acting after a failure under`, `tda-common.l4`), the s 20(3A) carve-out (`s 20(3A) -- what the applicant must do after ceasing to retain the interest`, `fhog-grant.l4`), "foreign person" (`a transferee is a foreign person (s 3)`, `tda-transfer.l4`) and "which relief can apply" (`which relief the land can open ...`, `tda-transfer.l4`) moved to the core, with core cases.
   - The vacant-land answer no longer says the land "pays duty at the general rate". That was wrong for a foreign buyer, because ss 30A(a)(i) and 30C apply. It now says only that the exemption cannot apply and a building contract can get the grant.
4. Division 2C's reach had no end date: **fixed** (finding 18).
5. The FHOG Act and Regulations' licence terms were missing from the folder: **fixed**. `SOURCE-LICENSE.md` now carries both subjects' SOURCE-LICENSE.md after the Duties Act's, as the Motor Accidents encoding does.
6. Vehicles:
   - The s 193(1)/195 parties for a notice: **fixed** (finding 20).
   - The unexplained placeholders in "Does this interest make me an owner of a home": **fixed**. A comment now says ownership reads only s 4 "home".

## Before relying on it

- Check the Tasmanian Government Gazette and the statutory rules for any extension order under ss 46K, 46T or 57D made after 13 October 2026, and deposit the Duties Regulations 2021 to settle whether amounts are prescribed (findings 1, 3, 18).
- Deposit ss 46D and 46M as they stood before 1 January 2022 (or the amending Acts No. 8 of 2021 and No. 8 of 2022, and any regulations prescribing the caps then), to answer Division 2A and 2B transfers from February 2018 to December 2021 (finding 17).
- Settle the ss 18A-18C reading (finding 19) against the second reading speeches or an SRO ruling, if historical grants matter.
- An independent test pass, and a check of the figures against the State Revenue Office's calculators. None were consulted.
- Encode Part 3A (foreign purchaser duty) and Division 2C (pre-completion concession), which the questions now answer `not covered` (Division 2C only within its reach), and ss 18A-18C for new homes if historical grants matter.
- Deposit and encode the Taxation Administration Act 1997 (interest, penalty tax, objections), to finish the breaches that now stop at "tax default".
- Settle the s 32 reading (finding 6) against the Help to Buy Act 2024 and any SRO ruling, and encode the Help to Buy Act.
- A seat that takes three or more buyers or applicants, if needed (the core already does).
