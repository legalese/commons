# First Home Owner Grant Act 2000 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc` (29 questions).

Files:

- `fhog-grant.l4`: the eligibility criteria, the eligible transaction and the cap, entitlement, the amount, the application window, repayment, the charge, offences, objection and review deadlines, and the Duties Act s 142A test.
- `fhog-cases-grant.l4`: built by the scratchpad generator `gen_wa_first-home-owner-grant-act-2000_baseline.py`.

## Edition

- **The Act.** The compilation of the First Home Owner Grant Act 2000 (No. 16 of 2000) deposited at `../../registers/source-bundle/mrdoc_49121.txt` (legislation.wa.gov.au mrdoc 49121, retrieved 2026-09-07). The deposit gives no compilation number or date. Its compilation table ends with the Help to Buy (Commonwealth Powers) Act 2025 Pt. 4 Div. 2, in operation 19 Dec 2025.
- **The Regulations.** The First Home Owner Grant Regulations 2000, version 03-l0-00, currency from 14 May 2026, deposited at `../../../first-home-owner-grant-regulations-2000/registers/source-bundle/mrdoc_49370.txt` (mrdoc 49370, retrieved 2026-10-20). Two regulations are used:
  - r 6, which sets the cap amount south of the 26th parallel at $800,000 for transactions commencing on or after 7 May 2026;
  - r 8(3), which sets the interest rate under a repayment arrangement at 12.4% a year.
- **Two dates come from the compilation table, not the sections.** Section 19(1) defines "amendment day" and "second amendment day" by reference to amending Acts, and s 14(5A) uses the second. The compilation table gives 25 Sep 2013 for the Revenue Laws Amendment Act 2013 Pt. 4 and 3 Oct 2015 for the Revenue Laws Amendment Act 2015 Pt. 2 Div. 1. Reading s 43 of the 2013 Act as part of its Pt. 4 is an inference.

Dates are entered as YYYYMMDD numbers, as in the WA Duties Act baseline.

## Checks

One case file, **68 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98).

A copy with one expected value altered (the class 8 amount, $15,000 to $14,000) was run as a control. The runner reported the failure.

## Seat

**The first home buyer**: the applicant for a first home owner grant (s 15), who is, or on completion will be, an owner of the home (s 16).

Both life events ask the Act the buyer's question, "Do I qualify for the grant, and how much?" Most of the Act after Part 2 Division 2 addresses the Commissioner of State Revenue: authorising payment (s 18), paying in anticipation (s 21), requiring repayment (s 51), registering a charge (s 55). Each is encoded as what it means for the buyer: what must be paid back, by when, how large a penalty can be, and whether the home can be charged.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The Regulations are deposited and supply the cap (r 6) and the interest rate (r 8(3)). Regulations rr 4, 5 and 7 (prescribed relevant interests and the s 16 exclusions) are folded into facts.
- **The actors the text names.** Followed: the applicant, the applicant's spouse or de facto partner, and the Commissioner.
- **A judgment handed to someone else is answered conditionally.** Followed. Each of these is a fact, and the answer holds if the Commissioner has so decided:
  - the age exemption (s 9A(2));
  - being satisfied of an intention to reside permanently (s 7B(1)(b));
  - the s 11(2)(b) opinion;
  - the residence approvals and exemption (s 13(6A), (6));
  - the s 14(4) declaration;
  - being satisfied that a contract replaced an earlier one (s 19(2C));
  - being satisfied that a married couple live apart for good (s 7(2));
  - the reasonable belief in s 55(2A).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: spouse and de facto partner (ss 3, 7); permanent resident (s 7B); total value (s 14AC); cap amount (s 14AD); eligible transaction (s 14); required residence period and takeup period (s 13).
  - Asked as facts: new, substantially renovated or established home (the last two turn on the GST Act); citizenship and visas (Commonwealth Acts); whether a person held a "relevant interest" in "residential property" (ss 3(2), 6); which side of the 26th parallel the home is on.
- **One case is the text's natural unit.** Followed: one transaction (s 8(3)), with every applicant on the application.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Out: administration, delegation, investigation powers, confidentiality, grant relief declarations and regulation-making.

**Departure.** The special eligible transactions of s 14B (classes 1 to 8) are historical: their windows all closed by 30 June 2017. So the class is a fact, and only its s 19(2) amount is encoded as a table.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c051** (2028-02-20), Byford house-and-land package, $620,000, with Liam | `Is the grant payable to me`, `How much grant will I be paid`, `Am I a concessional first home owner for duty` | Payable, **$10,000**; both are concessional first home owners for duty |
| Jake **k074** (2042-02-18), one-bedroom apartment off the plan, $390,000, alone | `Is my transaction eligible`, `How much is my grant`, `Is the grant payable to me`, `Am I a concessional first home owner for duty` | Eligible, **$10,000**, but **not payable until settlement**; a concessional first home owner for duty |

Facts taken from the lives:

- Chloe is 24 and Liam 28. Chloe was born in Perth.
- Neither has owned a home: they rent in Cannington.
- They live in Byford from handover in July 2029 until it is sold in 2040.
- Jake is 35, born in Perth, and divorced from Tahlia since August 2039. He has only rented.

These are **assumed**, and labelled as such in the generator:

- the package split (land $280,000, building contract $340,000);
- the handover and settlement dates;
- one year of de facto life for Chloe and Liam at February 2028;
- Jake living in the apartment for five years after settlement.

## Why this scope

The scope is what the two events ask, plus what any first home buyer meets on the way:

- the seven eligibility criteria;
- the value cap and how total value is worked out;
- the amount;
- when to apply;
- the residence obligation;
- what happens if the grant has to be paid back.

The Duties Act 2008 s 142A borrows this Act to define a "concessional first home owner". The WA Duties Act baseline (`../../../duties-act-2008/encodings/baseline-2026-10/`) asks that as a fact. This encoding answers it, so the two baselines can be read together.

Left out:

- the s 14B windows;
- movable buildings (s 14AA(3));
- guardians (s 17) and death of an applicant (s 23);
- the objection procedure beyond its deadlines;
- the charge's priority, release and sale;
- Part 6A.

None of these is met by a buyer in the lives.

## What the Act turns out to say

1. **The grant is a flat $10,000 for anything contracted since 3 Oct 2015.** Section 19(2CA) gives "the lesser of ... $10 000" and the consideration, for a new home, a substantially renovated home, a building contract or an owner build alike. The amount does not rise with the price or fall with the region. Both lives get $10,000, as they expect. An owner build costing $8,000 gets $8,000. Asserted.
2. **The cap is $800,000 south of the 26th parallel from 7 May 2026, and $750,000 before.** It is $1,000,000 north of the 26th parallel; no regulation changes that figure. Regulation 6 was made on 13 May 2026 and is in operation from 14 May 2026, but it applies to transactions commencing on or after 7 May 2026. So it reaches back a week. A $760,000 new home contracted on 6 May 2026 is outside the cap; the same home contracted on 7 May is inside. Asserted.
3. **Total value, not price, is tested against the cap.** For a purchase it is the greater of the price and the unencumbered value (s 14AC(1)(a)): a home bought for $790,000 but worth $810,000 is over. For a building contract, the land's value is added to the building price (s 14AC(1)(b), (2)): $500,000 of building on land worth $350,000 is $850,000. Asserted.
4. **Chloe's package is a building contract, and the land counts towards the cap.** On the two-contract reading (land, then a comprehensive home building contract), the transaction is the building contract (s 3, "transaction" (b)). Its total value is $340,000 + $280,000 = $620,000, under the cap. The grant is the lesser of $10,000 and the building price. Read as one contract for a new home, the answer is the same. The split is assumed. The WA Duties Act baseline's figure of $16,356 duty on the one-contract reading is unaffected, because duty falls on the land transfer, not on the grant. On the grant, and on concessional status, the two baselines agree. Asserted.
5. **Jake's grant is not payable until settlement.** Section 8(1)(b)(ii) requires the transaction to "have been completed". An off-the-plan purchase is completed when the purchaser "acquires the relevant interest in land" (s 14AA(2)(a)): in Jake's life, settlement in 2045. He may apply from the day the contract is made, up to 12 months after completion (s 15(5)). The Commissioner may pay early under s 18(2), on condition of repayment if the value turns out over the cap (s 18(3)). Asserted.
6. **Established homes are out, but their buyers keep the duty concession.** Section 14(5A) excludes a contract for an established home made on or after 3 Oct 2015. The Duties Act s 142A(2)(b) still treats a buyer who would otherwise qualify as a concessional first home owner. A 2027 first home buyer of a $450,000 established home gets no grant but is a concessional first home owner for duty. Before the cut-off, s 19(2B)(a) gave $3,000 for an established home, against $10,000 for a new one. Asserted.
7. **"Never owned a home" is narrower than it sounds.** Section 12(3) bars a buyer whose interest was in residential property *and* who lived there, either before 1 July 2004 or for a continuous 6 months since. An investment flat never lived in does not disqualify. Asserted. Any such interest held before 1 July 2000 does disqualify (s 12(1)), lived in or not; that is encoded but not asserted.
8. **A spouse's or de facto partner's past counts against the buyer, but only a partner the Act recognises.** A de facto partner must have lived with the applicant "for at least 2 years" on the commencement date (s 3). A spouse living apart for good is "taken not to be the applicant's spouse" (s 7(2)). A partner of 3 years who owned a home bars the buyer; a partner of 1 year does not. A husband bars her; a husband she has separated from for good does not. For Chloe and Liam it does not matter, since both apply and both are clean. Asserted.
9. **One citizen is enough for a couple.** Under s 10(2), a temporary visa holder buying with Jake meets the criterion. Buying alone, the same person does not. A permanent visa alone is not permanent residence: the buyer must also satisfy the Commissioner of an intention "to reside permanently in Australia" (s 7B(1)(b)). Asserted.
10. **The only age rule is 18, and the Commissioner may waive it.** Section 9A(2) allows an exemption, so a 17-year-old with it qualifies. There is no upper age limit, as Jake's life says. Asserted.
11. **Residence: move in within 12 months of completion, and stay 6 continuous months.** The Commissioner can approve a shorter stay or a longer takeup (s 13(6A)). A co-buyer who never lives there can be exempted only if there are joint applicants and another of them complies (s 13(6)). Asserted. Without that, one non-resident co-buyer sinks the whole application (s 8(1)(a)); this last point is not asserted.
12. **What paying it back costs:**
    - a buyer paid early or in anticipation who learns that the cap or the residence requirement will not be met must, within **30 days**, give written notice and either repay or apply for an arrangement (ss 18(3), 21(2));
    - a repayment required by notice, and any penalty, is due within **28 days** (s 51(4));
    - each penalty is capped at the amount to be repaid (ss 18(6), 21(5a), 51(2), (3));
    - arrangements carry interest at **12.4%** a year (r 8(3));
    - the Commissioner may register a charge over the home (s 55);
    - false information, or breaking a grant condition, carries a fine of up to **$20,000** (ss 47, 22(4)), and a conviction bars any later grant (s 13A).

    Asserted.
13. **Trusts.** A buyer who will hold the home as trustee is ineligible (s 13B(1)). The exception is the part held for the Commonwealth or Housing Australia under a Help to Buy arrangement, added in 2025 (s 13B(2)). Asserted.
14. **The lives cite "ss 6-13" for eligibility.** The criteria are ss 9 to 13B. The new-home and cap rules that both events turn on are ss 14, 14AC and 14AD, with Regulations r 6. Not asserted (a citation note).

## What would need doing before this is worth anything

- Check against Revenue WA's guidance and decisions. None were consulted.
- Settle how a house-and-land package is documented in Chloe's life (one contract or two), and the land and building prices.
- Encode the s 14B class windows if historical claims matter, and movable buildings, guardians and death of an applicant.
- Work out "relevant interest" (s 6) and "residential property" (s 3(2)) from facts rather than asking them, with Regulations rr 4 and 5.
- Add the objection and review procedure (ss 29-32) and the charge's priority and sale (ss 56-59).
- Link the Duties Act baseline's fact "each transferee is a concessional first home owner" to this encoding's `Am I a concessional first home owner for duty`.
