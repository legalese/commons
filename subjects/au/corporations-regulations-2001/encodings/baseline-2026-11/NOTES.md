# Corporations Regulations 2001 (Cth) — cooling-off, complaints, compensation and National Guarantee Fund claims: baseline encoding

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except `LEST BREACH … BECAUSE`. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulations. Their seven volumes are almost all machinery addressed to licensees, markets and ASIC; this encoding takes the parts a retail client meets when bringing or answering a claim on insurance, super or an investment: the cooling-off right to return a product and get the money back, the complaints and compensation arrangements a licensee must have, a claim against a licensee's security bond, and a claim on the National Guarantee Fund when a broker becomes insolvent.

The Regulations hang on the Corporations Act 2001 and cannot be read without it. The Act's frame for each group (ss 1019A, 1019B, 912A(1)(g), (2), 912B) is encoded here too, quoted from the Act as deposited at `../../../corporations-act-2001/registers/source-bundle/C2004A00818.txt` (Compilation No. 149, compilation date 19 September 2026, register id C2026C00432; CC BY 4.0, attribution in that subject's `SOURCE-LICENSE.md`). The Act's own encodings (`../../../corporations-act-2001/encodings/`) are untouched; neither covers these sections.

## Edition

- **The Regulations:** Compilation No. 214, compilation date 1 September 2026, includes amendments up to F2026L01038, register id F2026C00854 (seven volumes joined), deposited at `../../registers/source-bundle/F2001B00274.txt`, retrieved 21 October 2026.
- **The Act (frame only):** as above.
- **Not deposited or not used:** the Acts Interpretation Act 1901 as applied by s 5C of the Act (computing periods, a last day on a weekend or holiday); the SIS Regulations (meaning of preserved and restricted non-preserved benefits); the Insurance Contracts Act 1984 (interim contracts, investment-linked products); ASIC's dispute resolution standards (RG 271); the SEGC's determinations and the market operating rules.

## Checks

Three files: `cr-dates.l4` (the only daydate import), `cr-client.l4` (the questions), `cr-cases-client.l4` (the cases).

- `l4 run cr-cases-client.l4`: **134 assertions written, 134 satisfied, 0 errors, 0 warnings**; one `#TRACE` of the nomination rule ends FULFILLED.
- `l4 run cr-client.l4` and `l4 run cr-dates.l4`: 0 errors, 0 warnings.
- A mutation of three expected values (a last day, a repayment, a nomination answer) was caught: 5 assertions failed (the last-day value is shared by three cases).
- Expected values were worked by hand from the text, with the provision beside each group. Every `NOT` is bracketed. All 21 exported questions carry `@export` and a `@desc` on each input.

## Seat

**The retail client**: the person who has acquired, or holds, an insurance, superannuation or investment product, or receives a financial service as a retail client, and wants to return the product or claim for a loss.
The questions are "Can I give it back and get my money, by when, and how much?", "Who must hear my complaint?", "Is there insurance or a bond behind my claim?" and "Can I claim on the National Guarantee Fund, by when, and for how much?".
Almost every provision addresses the issuer, the licensee, ASIC or the SEGC (Securities Exchanges Guarantee Corporation); each is encoded as what the client can expect or must do. No seat for the issuer, licensee, ASIC, the SEGC or a court. The standard employer-sponsor's right to return a super product for its employees (reg 7.9.68) would be a second seat and is not written.

The 2026-10-18 defaults:

- **The instrument alone, plus what sets its numbers or dates.** Followed, with one addition: the Act provisions the Regulations modify are encoded as the frame, since a regulation made "for subsection 1019B(5A)" has no meaning on its own.
- **The actors the text names.** Followed: the client (holder), the responsible person (issuer or seller), the licensee, ASIC, AFCA, a State or Territory Ombudsman, the SEGC, the dealer (broker), the Court.
- **A judgment handed to someone else is answered conditionally.** Followed. Asked as facts: whether costs are "reasonable" and at arm's length (reg 7.9.67(7)); whether PI cover is "adequate" (not decided; reg 7.6.02AAA(1)); whether ASIC "considers" a bond no longer required; whether a claim is "valid"; whether the SEGC or Court "is satisfied" the claimant contributed to the insolvency (reg 7.5.69(b)); whether the SEGC "otherwise determines" on a late claim.
- **The instrument's own definitions worked out; borrowed terms asked.** Worked out: the reg 7.9.64(1)(g) short renewal; "exempt licensee" (reg 7.6.02AAA(3)); "business day" (Act s 9, with holidays as input); the adjustment amount (reg 7.9.67(4)). Asked: "retail client", "risk insurance product" and the other product classes, "preserved benefits", "investment-linked product", "interim contract of insurance", "liquid". **Departure:** "excluded person" (reg 7.5.04) is the Regulations' own definition but runs to some 30 heads of family, trust and company relationships; it is asked as a fact with a gloss.
- **One case is the text's natural unit.** Followed: one product, one return, one complaint, one claim.
- **The text's own terms, each with a plain gloss.** Followed, in comments and `@desc` lines.
- **Operative provisions in; machinery out.** Followed.

**One regulative rule.** reg 7.9.66(4) ("The holder must make the nomination not later than 1 month after notifying") is `the nomination duty` (`PARTY the holder MUST nominate … WITHIN` the days to the same day next month), with `the return of my super` adding the responsible person's duty to "return the money as directed" (reg 7.9.66(7)) under HENCE. The exported question `Has my return of my super taken effect` takes plain dates and runs the duty with EVALTRACE inside; no exported question takes a DEONTIC or EVENT input.

## Rulings on negatives and legal effects (recorded word for word, as the guide requires)

Where the text itself says no in its own words the answer is `JUST FALSE`; elsewhere `NOTHING`.
Periods, "where" and scope limits (ruled 2026-11-05): "(a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" ...: outside the scope the answer is `NOTHING`."
Questions with no convention are decided site by site, each with a fork line below.

### Fork register

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| s 1019A(1)(a); reg 7.9.64(1)(ea), (hb) | `Do I have a cooling-off right for my product` | A CCIV security: `NOTHING`. It is not in the deposited s 1019A(1)(a) list, but the Regulations exclude subclasses of it, implying Chapter 8B brings it in. | `JUST TRUE` (Chapter 8B treats it as a managed investment product), or `JUST FALSE` (not listed). |
| s 1019A(1) | the same | Any other failed condition ("applies if"): `JUST FALSE`. | — |
| s 1019B(3) | `The last day of my cooling-off period` | A period "starting on" a time on day D ends at the end of D + 14 (the starting day is not one of the 14); starting at the end of day D, it runs D + 1 to D + 14. | The starting day counts as day 1, so the last day is D + 13. |
| s 1019B(3) | `Can I still return my product on this day` | Before the period starts (no confirmation received, within five business days of issue) the right "can only be exercised during the period": `JUST FALSE`. | The 14 days are a deadline only, and earlier notice is good. |
| s 1019B(3)(a) | the same | The confirmation day itself is in the period (it starts at that time on that day). | It starts the next day. |
| s 1019B(5)(b) | the same | On the day the rights end, still in (the rights end at some time that day); the day after, out. | Out on that day. |
| reg 7.9.65(1) | the same | Asked as a fact whether the event (the journey) had started when notice was given; on the start day before departure, in. | Day granularity: out on the start day. |
| Acts Interpretation Act s 36(2) | `The last day of my cooling-off period` | Not applied: the answer is the period's own last day, "before any extension". | A last day on a weekend or holiday moves to the next business day. |
| reg 7.9.66(3), (4) | `Has my return of my super taken effect` | A nomination received after the month: `JUST FALSE` (the duty is breached and the right is "taken to have been exercised only on receipt" of a nomination made in time). | A late nomination still takes effect on receipt; (4) is a duty without that consequence. |
| reg 7.9.66 | `Must I nominate a fund to return my super` | Not super or an RSA: `NOTHING`; super without preserved money: `JUST FALSE` ("if"). | — |
| reg 7.9.67 | `The least I can be repaid`, `The most I can be repaid` | "may" reductions are the issuer's choice: the answer is a range, all taken (least) or none (most). | — |
| reg 7.9.67(8) | `The least I can be repaid` | The proportion is taken of the premium for the specific period (the risk insurance part). | The proportion is taken of the whole "amount that would otherwise be repaid", which for a product only partly risk insurance would cut much more. |
| reg 7.9.67 | the same | Never below zero (s 1019B(6): termination "without penalty to the client"). | The text sets no floor. |
| reg 7.9.67(2)(a)(iii) | the same | The price-fall reduction for super is taken as available; "subject to the governing rules" is not asked. | The fund's rules may forbid it. |
| reg 7.9.67(9), 7.9.70(1) | the same | A distribution reduces only the products in reg 7.9.70(1). | Any product's distribution. |
| reg 7.6.02AAA, s 912B(2)(b) | `Must my licensee hold PI insurance to compensate me` | ASIC-approved alternative arrangements: `NOTHING` (the reg's requirement attaches to (2)(a) arrangements). | `JUST FALSE`. |
| reg 7.6.02AA(4)(d) | `May ASIC release the security bond` | A valid claim submitted on or before the day three months after the advertisement blocks release; release is possible only from the next day. | Release possible on that day. |
| reg 7.5.70(2)(b) | `By when must I make my NGF claim` | "within 6 months after" awareness ends on the same day six months on (31 August to 29 February in a leap year). | — |
| reg 7.5.79(1) | `The interest the NGF must pay me` | Simple interest, 365-day year, days counted as the difference of the dates; a determined rate below 5% is replaced by 5% ((2)(b)). The (1)(a), (b) end days (instalments, an insufficient Fund) are not encoded. | Count both end days; 366 in a leap year. |

## In scope

- **Cooling-off (Act Part 7.9 Division 5; Regulations Part 7.9 Division 5):** Act ss 1019A, 1019B; regs 7.9.64 (excluded subclasses), 7.9.64A (notice for risk insurance), 7.9.65 (event insurance; scheme interests together), 7.9.66 (super and RSAs: nominating a fund, eligible rollover fund), 7.9.67 (the amount repaid), 7.9.70 (a distribution is not exercising a right).
- **Complaints and compensation (Act Part 7.6):** Act s 912A(1)(g), (2); reg 7.6.02(5), (6) with Schedule 8AC (as an input); Act s 912B; reg 7.6.02AAA(1), (3); reg 7.6.02AA(4), (5) (claims against a security bond).
- **National Guarantee Fund (Part 7.5 Division 4):** Subdivision 4.9 entitlement, regs 7.5.64(1), 7.5.67, 7.5.68, 7.5.69; reg 7.5.70 (time for claims); reg 7.5.72B(1) (claimant limit); reg 7.5.78 (costs); reg 7.5.79 (interest).

## Out of scope, and why

- **reg 7.9.68** (a standard employer-sponsor returning a super product for its employees): the employer's seat.
- **reg 7.9.14** (return of super or an RSA issued in breach of s 1016E): a second right of return in a different Division; not reached in this pass.
- **reg 7.9.69** (deemed contract terms): no question for the client beyond the right itself.
- **reg 7.6.02(1), (2)** (what ASIC weighs in making IDR standards): addressed to ASIC; the standards themselves (RG 271) are not law here.
- **reg 7.6.02AAA(2), (4), (5)** (ASIC's approvals, bond discharge, 2008 transition) and **reg 7.6.02AA(1)-(3)** (the old Insurance (Agents and Brokers) Act and old Corporations Act PI regime): ASIC machinery and history.
- **Part 7.5 Subdivisions 4.3, 4.7, 4.8 and 4.10 except regs 7.5.78, 7.5.79** (claims for a broker's default on a sale or purchase, unauthorised transfers, cash settlement, the SEGC's power to allow and settle claims, set-off, reductions, arbitration, instalments) and **reg 7.5.72A** and **7.5.72B(3)** (the participant limit, 15% of the Fund's minimum amount, and the pro rata cut): the participant limit needs the Fund's minimum amount, and the other heads are a second pass.
- **Part 7.10B** (compensation scheme of last resort): the deposited regulations deal only with reporting by the CSLR operator; eligibility and the $150,000 cap are in the Act (ss 1063-1069), not here.
- **Part 9.7, reg 9.7.01** (interest on unclaimed money paid back by ASIC): the formula was lost in conversion (only "where:" survives) and there is no `formulas.md` sidecar; a later pass should transcribe it from the authorised rendering.
- **reg 7.1.08AA** and the other claims handling and settling definitions: they decide who needs a licence, not what a claimant may do.
- Everything else in the seven volumes: licensing, markets, disclosure content, takeovers, external administration, fees, transitional provisions.

## What the Regulations turn out to say

1. **No confirmation, no early return.** Act s 1019B(3) gives a right that "can only be exercised during the period of 14 days starting on the earlier of" receipt of confirmation and the end of the fifth business day after issue. Read literally, a client who has not yet received confirmation cannot return the product in the first five business days, and the period then runs to the 14th day after the fifth business day (issued Monday 2 November 2026: 10 to 23 November). Asserted (fork).
2. **A holiday moves the end.** The fifth business day skips public and bank holidays "in the place concerned" (Act s 9), which the text does not tie to the client or the issuer: issued 24 December 2026, the period ends on 19 January 2027 with three holidays and on 14 January without them. Asserted.
3. **Travel insurance ends with the trip.** reg 7.9.65(1): for risk insurance for an event that starts and ends within the 14 days, the right ends at the start of the event (the journey; loading the removal van), even if the 14 days have not run. Asserted.
4. **Only insurance may be cancelled by phone.** Act s 1019B(2) closes the list (writing, electronically, or a way the regulations specify); reg 7.9.64A adds "a way permitted by the responsible person" for risk insurance only. A super fund that takes a phone call does not thereby receive a valid notice. Asserted.
5. **Making a claim ends the right to return.** Act s 1019B(5)(a), and its Note: once the client has used a right under the product (a claim on the policy), the cooling-off right is gone; receiving a distribution does not count (reg 7.9.70(2)). Asserted.
6. **Returning super with preserved money waits on a nomination.** reg 7.9.66(3): the return "is taken to have been exercised only on receipt ... of the nomination", which must come within a month of the notice ((4)), and may come after the 14 days. The text does not say what a late nomination does (fork). Asserted.
7. **The client keeps the upside; the issuer may pass on the downside.** reg 7.9.67(3): a rise in the unit price "is increased"; (2): a fall "may be reduced". Asserted ($10,000 units worth $10,400 on the notice day: at most $10,400; worth $9,500: as little as $9,500 less costs).
8. **RSAs are protected from cost deductions and price adjustments.** reg 7.9.67(7) excludes RSAs from the costs reduction, and (2), (3) do not list them; only unrecoverable tax or duty ((6)) comes off. Asserted.
9. **The proportion rule in reg 7.9.67(8) is open-ended for mixed products.** It reduces "the amount that would otherwise be repaid ... by a proportion equal to the proportion of the period that has passed" where "that part of a financial product that is a risk insurance product" was issued for a period. For super with insurance, read literally, the whole repayment could be cut by that proportion. Read here as a proportion of the insurance premium (fork).
10. **Nothing in reg 7.9.67 stops the reductions exceeding the money paid.** Read with s 1019B(6) ("without penalty to the client") as not below zero (fork). Asserted.
11. **Estate administrators are relieved of the whole complaints system; executors and attorneys only of AFCA.** reg 7.6.02(6) removes s 912A(1)(g) for an administrator of an individual's estate where complaints may be made under a Schedule 8AC law (the State and Territory guardianship laws); reg 7.6.02(5) removes only AFCA membership (s 912A(2)(c)) for a trustee under a will or intestacy, an express trustee of an individual's trust, or an attorney, where a State or Territory Ombudsman takes complaints. An administrator with only an Ombudsman gets neither relief. Asserted.
12. **Schedule 8AC is borrowed.** Its heading prescribes laws "for paragraph 601RAE(4)(b) of the Act—estate administration" and it is applied to reg 7.6.02(6) by cross-reference; it lists guardianship, care and public trustee laws, not probate laws (those are in Schedule 8AD).
13. **Insurers and banks need no PI insurance for client compensation.** reg 7.6.02AAA(3): APRA-regulated general and life insurers and ADIs are exempt licensees, as is a related licensee with an ASIC-approved guarantee; an advice business is not. Asserted.
14. **Three months to claim against a bond.** reg 7.6.02AA(4)(d): ASIC may release a security bond only if "3 months after publication of the advertisement, no valid claim has been submitted". "Valid claim" is not defined. Asserted.
15. **National Guarantee Fund limits.** reg 7.5.72B(1): no more than $1 million to one claimant for one broker and one event, and no more than $250,000 of it for cash held with the broker. Asserted at and just over each limit.
16. **A Form 720 notice can shorten the time to claim.** reg 7.5.70(2): where the SEGC publishes a notice with a closing day (at least three months after publication), that day governs, even if six months from the claimant's awareness would be later; otherwise six months from awareness. A late claim is "barred unless the SEGC otherwise determines". Asserted.
17. **Interest at not less than 5%.** reg 7.5.79: 5% a year, or a higher rate the SEGC determines (not above the Federal Court's rate), from the day the claimant became entitled to claim to payment. Asserted.

## What would need doing before this is worth relying on

- An independent test pass and a coverage table.
- The Acts Interpretation Act 1901 (as applied by s 5C) for a last day falling on a weekend or holiday.
- reg 7.9.14, reg 7.9.68 (the employer's seat), the rest of the NGF claims (Subdivisions 4.3, 4.7, 4.8, 4.10, reg 7.5.72A) and the unclaimed money interest formula (reg 9.7.01, after a `formulas.md` sidecar).
- Case law on when a claimant "becomes aware" of an insolvency, on a "valid claim", and on the meaning of "price" for a product with no unit price; none was searched.
- The Corporations Act's AFCA and CSLR provisions (Part 7.10A, ss 1063-1069) as a further layer.
