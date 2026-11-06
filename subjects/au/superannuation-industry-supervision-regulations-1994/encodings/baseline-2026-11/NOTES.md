# Superannuation Industry (Supervision) Regulations 1994 (Cth): early release, departing Australia, rollovers and a child's death benefit pension (baseline encoding)

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to, with the design defaults ruled on 2026-10-18.
There is no REFUSE, no `#ASSERT REFUSED` and no BECAUSE other than `LEST BREACH ... BECAUSE`. Checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, coverage table, independent test pass or human gate was used. Not for public use as advice.

This is the first encoding filed under the Regulations' own subject.
The Act's encodings already reach into these Regulations: `../../../superannuation-industry-supervision-act-1993/encodings/baseline-2026-10/` covers preservation age, retirement, permanent incapacity, binding nominations, who may receive a death benefit and Schedule 1 in outline, and `../baseline-2026-11/` there covers insured benefits (regs 4.07C-4.07E), temporary incapacity and item 109.
Both stay as they are. This encoding works out in full what those take as single facts or leave out: severe financial hardship and its amounts, the terminal medical condition certificates, compassionate grounds, small balances, temporary residents and the departing payment, rollover deadlines, and the cashing of a child's death benefit pension.
IMPORT cannot reach across subjects, so `the preservation age of a person born on` is restated here from reg 6.01(2). It agrees with the Act encoding's `What is my preservation age`.

## Edition

- **The Regulations:** Compilation No. 159, compilation date 1 July 2026, register id F2026C00541, deposited at `../../registers/source-bundle/F1996B00580.txt` (retrieved 19 October 2026).
- **Not deposited:** the Migration Act 1958 (what a temporary visa, a permanent visa and Subclasses 405 and 410 are), the Social Security Act 1991 (which payments count as income support), the superannuation data and payment standards under the Act s 34K(3), the Taxation Administration Act 1953 release authorities, and the Acts Interpretation Act 1901 (counting days and months, and business days). Each is taken as a fact or a borrowed reading, as stated below.

## Checks

Three files: `sisr-dates.l4` (date arithmetic using built-ins only, with no daydate import and no `YMD`), `sisr-claimant.l4` (the questions) and `sisr-cases-claimant.l4` (the cases).

- `l4 run sisr-cases-claimant.l4`: 120 assertions written, 120 satisfied, 0 errors, 0 warnings. Two `#TRACE`s: reg 6.20A paid on day 28 ends FULFILLED; reg 6.34A with 5 days allowed and the rollover on day 6 ends in BREACH.
- `l4 run sisr-claimant.l4` and `l4 run sisr-dates.l4`: 0 errors, 0 warnings.
- Mutation check: three expected values were changed (the day of preservation age plus 39 weeks, the item 107 cap, a rollover last day). All three failed, leaving 117 of 120 satisfied.
- Expected values were worked out by hand from the text, with the provision cited beside each group. Every `NOT` is bracketed. All 19 exported questions carry `@export` and a `@desc` on each input.

## Seat

**The claimant: the fund member** who asks for super to be released early or moved. This covers a member in severe financial hardship, a member with a terminal medical condition, a member applying on a compassionate ground, a member with a small balance, a former temporary resident who has left Australia, and a member rolling over to another fund.
The seat also covers **the deceased member's child** who is paid a death benefit pension (reg 6.21(2B)).
Questions are phrased as that person would ask them: "Am I in severe financial hardship ...?", "May my fund pay me this lump sum ...?", "By when must my old fund roll over my super?".
The trustee, the Regulator (the Commissioner of Taxation, for reg 6.19A), APRA and the Immigration Department get no seat. Their satisfactions and determinations are asked as facts.

The 2026-10-18 defaults:

- **The instrument alone, plus what sets its numbers.** Followed. Every number is in the Regulations themselves.
- **The actors the text names.** Followed: the member, the trustee, the Regulator, the Commonwealth agency giving evidence, the mortgagee, the registered medical practitioners, the Immigration Department, and the transferring and receiving funds.
- **Judgments answered conditionally.** Followed. These are asked as facts:
  - the trustee's satisfaction that the member cannot meet "reasonable and immediate family living expenses";
  - the Regulator's satisfaction under reg 6.19A(2), and its determination under (1)(f);
  - the amount the Regulator determined (item 107);
  - the trustee's satisfaction on the Immigration Department's statement (reg 6.20A(3));
  - whether the receiving fund can receive under the standards.
- **Own definitions worked out, borrowed terms asked.** Worked out: "preservation age", "severe financial hardship", "terminal medical condition", the reg 6.21(2C) disability, and the reg 6.01B closed list. Asked: "temporary resident", "permanent resident", "Commonwealth income support payment" (the member says whether the payments are of that kind), "standard employer-sponsor", "lost member", "unfunded public sector superannuation scheme" and "investment choice".
- **One case.** One member, one fund, one application or request.
- **Own terms with plain glosses.** Followed, in comments and `@desc` lines.
- **Machinery out.** Followed (see "Out of scope").

**Regulative rules.** There are two duties with a deadline that the member meets:
- reg 6.20A(4), (5): the fund must pay the departing member within 28 days after the request is lodged;
- reg 6.34A: the fund must roll over within 3 business days, or 30 days.

Each is a `DEONTIC` rule run inside a question by `EVALTRACE` and read with `CONSIDER ... WHEN FULFILLED`. No exported question takes a DEONTIC or an EVENT input.

## Rulings on negatives and legal effects (recorded word for word, as the guide requires)

Where the text itself says no in its own words, the answer is `JUST FALSE` (or plain FALSE for a definition). Elsewhere it is `NOTHING`.

The ruling on periods, "where" and scope limits (2026-11-05), quoted: "(a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" ...: outside the scope the answer is `NOTHING`."

Questions with no convention are decided site by site, each with a line in the fork register below.

### Fork register

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| Sch 1 item 105 | `What is the most my fund may pay me now for severe financial hardship` | "in each 12 month period (beginning on the date of first payment)": each period runs from the payment that began it, so the next payment may be made from the same day 12 months after the latest one. | The periods are fixed years counted from the very first hardship payment ever made. |
| Sch 1 item 105 | `May my fund pay me this lump sum for severe financial hardship` | When the balance is below $1,000, the $1,000 floor falls away and any amount up to the balance may be paid. | The exception means the whole (sub-$1,000) balance must be paid. |
| Sch 1 item 105 | the same | A member who meets both (5)(a) and (5)(b) chooses the ground. The text does not say which applies. | (a)'s cap applies whenever (a) is met. |
| reg 6.01(5A) | `Am I in severe financial hardship on the 26-week ground` | Evidence dated after the application is not "more than 21 days before" it, so it counts. | Evidence must exist when the application is made. |
| reg 6.19A(5), (6) | `Must the Regulator release my super on this compassionate ground` | A mortgagee's statement without the (6) figures is not a statement under (5): `JUST FALSE`. | (6) is a direction about content, and the Regulator may still be satisfied. |
| reg 6.19A(2) | the same | Where the Regulator is not satisfied: `JUST FALSE` (an "if" condition). | `NOTHING`: (2) says "must ... if", not "only if", so a determination is not excluded. |
| reg 6.34A(2) | `By when must my old fund roll over my super` | "Business day" is read as a day that is not a Saturday or Sunday. Public holidays are not skipped because no calendar is deposited. A request on 24 December 2026 is then due on 29 December. | Skip the public holidays of the place: 31 December. |
| reg 6.34A(4) | the same | With an investment choice, the answer is the outer 30 days in (4)(b). The 3 business days after redemption in (4)(a) depend on the trustee's redemption steps, which the member cannot state. | The 3 business days in (2) still apply unless the trustee actually takes the redemption route. |
| reg 6.34A(5), (6) | the same | Consent to an illiquid investment (or notice before 1 July 2008): `NOTHING`, because the regulation sets no last day. | — |
| reg 6.21(2B) | `On what day must my death benefit pension be paid out as a lump sum` | A (2C) disability on the day: `NOTHING` (the "unless" is met and no day is set). | `JUST` no day, read as a permission to continue the pension. |
| dates | `the day of reaching age` | A person born on 29 February reaches an age in a common year on 1 March. | 28 February. |
| reg 6.20A(5) | `By when must my fund pay my departing super` | The 28 days run from the lodging of the request, even if the evidence under (2) or (3) arrives later. | They run from the day (1A)(b) is complied with. |

## In scope

- **Definitions:** reg 6.01(2) "preservation age"; reg 6.01(5), (5A) "severe financial hardship"; reg 6.01A "terminal medical condition"; reg 6.21(2C) disability.
- **Cashing:** reg 6.17(2)(b) (no payment except as permitted); reg 6.18(2) (no more than the accrued preserved benefits); Schedule 1 Part 1 items 102A, 104, 105, 107 and 111 (conditions and cashing restrictions).
- **Compassionate grounds:** reg 6.19A(1)-(6).
- **Temporary residents:** reg 6.01B(1)-(3); regs 6.20A and 6.20B (departing payment); item 103A.
- **Rollovers:** reg 6.33(1), reg 6.34(2) and reg 6.34A(2)-(6) (rollover and transfer deadlines).
- **A child's death benefit pension:** reg 6.21(2B).

## Out of scope, and why

- **Already encoded under the Act**, and not repeated here:
  - retirement (reg 6.01(7)), permanent incapacity (reg 1.03C), binding nominations (reg 6.17A), who may receive a death benefit (reg 6.22), pension or lump sum for dependants (reg 6.21(2A)), and items 101, 103, 106, 108 and 110 (in the Act's `baseline-2026-10`);
  - insured benefits (regs 4.07C-4.07E) and temporary incapacity with item 109 (in the Act's `baseline-2026-11`).
- **reg 6.19B and item 107A** (the COVID-19 release): no application could be made after 31 December 2020. Item 107A appears only in the reg 6.01B list.
- **Approved deposit funds** (Schedule 1 Part 2, regs 6.23-6.27A): a closed class. The items mirror Part 1.
- **The amounts of preserved, restricted non-preserved and unrestricted non-preserved benefits** (regs 6.02-6.16): the balance is asked as one figure. reg 6.20 (unrestricted non-preserved benefits, cashable at any time) is not asked.
- **Release authorities** (items 111A, 111B, 113: Taxation Administration Act 1953 and Income Tax (Transitional Provisions) Act 1997), **unclaimed money** (item 103B, reg 6.20C), **KiwiSaver** (item 113A), **deferred income streams** (item 109A) and **s 62(1)(b)(v) approvals** (item 114): their conditions are set by other instruments. They appear only in the reg 6.01B list.
- **reg 6.20A(5)(a)** (requests lodged by 31 October 2002 had 3 months): historical.
- **Rollover machinery:** the receiving fund's duties (regs 6.33A, 6.34B-6.34D), validation and verification (regs 6.33D, 6.33E), the trustee's information requests and their 5 and 10 business days (reg 6.33C), refusals (reg 6.35) and APRA suspensions (regs 6.36-6.38). These are duties between funds and the regulator. The member meets them only through the start date of the reg 6.34A period, which is asked.
- **Family law payment splits** (reg 6.17(2B), Division 6.7), **forfeiture orders** (reg 6.17(2C)), **portability forms** (Part 6A), and **Parts 1-5 and 7-13** other than the definitions used: not what a claimant meets.

## What the Regulations turn out to say

1. **The hardship evidence has a 21-day shelf life, but only for the 26-week ground.** Reg 6.01(5A): evidence for paragraph (a) "is of no effect if it is dated more than 21 days before the date of the person's application". Evidence of 1 October 2026 supports an application on 22 October, but not on 23 October. Paragraph (b) has no such limit. Asserted.
2. **The preservation-age ground starts 39 weeks after preservation age and is uncapped.** For someone born on 15 August 1966 it starts on 15 May 2027, and it needs 39 weeks of income support in total since preservation age, not 39 weeks in a row. Item 105 sets "Nil" for (b), so the whole preserved balance can be paid. For (a) it is one lump sum of $1,000 to $10,000 in each 12 months. Asserted.
3. **"In each 12 month period (beginning on the date of first payment)" can be read two ways.** One reading has a rolling period that starts again with each payment. The other has fixed years counted from the first payment ever. The two readings give different answers for a member whose payments are more than a year apart (fork). Under the reading taken, a payment of 29 February 2024 lets the next be made from 28 February 2025. Asserted.
4. **A terminal medical condition lasts only as long as the certificates.** Reg 6.01A(c) ends it when a certification period ends, and with two separate certificates it ends when either one does. It exists only once both doctors have certified. A period that ends even one day more than 24 months after the certificate does not qualify at all. Asserted.
5. **Severe financial hardship and the reg 6.19A compassionate grounds are closed to a temporary resident.** Reg 6.01B(3) lists the only conditions such a member can meet. Items 105 and 107 are not on the list, but item 107A (COVID-19) is. A temporary resident who meets item 105 before 1 April 2009 keeps it. Reg 6.19A itself does not mention reg 6.01B, so the Regulator could make a determination that the trustee cannot act on. Asserted for the bar.
6. **The departing payment is a duty with a 28-day clock, but only for a funded scheme.** Reg 6.20A(1A): the benefits "must be cashed" within "28 days after the request is lodged", so a request lodged on 3 November 2026 must be paid by 1 December. An unfunded public sector scheme "may" pay (reg 6.20B), so it is not bound. Below $5,000, copies of the visa evidence and passport are enough. At $5,000 or more, the trustee needs the Immigration Department's statement. Asserted.
7. **A rollover is due within 3 business days of the request, or of the information the fund asked for.** A request received on Thursday 5 November 2026 is due by Tuesday 10 November. The deadline is 30 days if the new fund cannot receive under the standards, or (as an outer limit) if the member made an investment choice. Written consent to an illiquid investment lifts the deadline altogether. The text does not define "business day". Public holidays are not skipped here (fork). Asserted.
8. **The mortgage ground is capped per 12 months.** Item 107(b) limits the release to 3 months' repayments plus 12 months' interest in each 12-month period, below whatever the Regulator determines. The mortgagee's statement must give both figures (reg 6.19A(6)). Asserted.
9. **Medical treatment needs two doctors, one a specialist, and treatment not readily available publicly.** Reg 6.19A(3) says the Regulator "cannot be satisfied" otherwise. Medical transport depends on the treatment being so certified ((4)). Palliative care and the dependant's death, funeral or burial need no certificate. Asserted.
10. **A child's death benefit pension stops at 25 unless the child has a lasting disability.** Reg 6.21(2B) requires a lump sum on the earlier of the pension's end and the 25th birthday. Reg 6.21(2C) lets it continue only where the disability is permanent (or likely to be), reduces capacity for communication, learning or mobility, and needs ongoing support services. All four limbs are needed. Asserted.
11. **Small balances:** under $200 means less than $200, so $200 itself does not qualify. Item 104 counts only a job that ended on or after 1 July 1997. Asserted.

## What would need doing before this is worth relying on

- An independent test pass and a coverage table.
- The Migration Act 1958 and the Social Security Act 1991 definitions (temporary and permanent visas, income support payments), so that the member is not asked to classify them.
- A public holiday calendar for "business day", and the superannuation data and payment standards.
- Case law and Regulator guidance on "reasonable and immediate family living expenses", "required" under reg 6.19A, and the 12-month period in items 105 and 107. None was searched.
