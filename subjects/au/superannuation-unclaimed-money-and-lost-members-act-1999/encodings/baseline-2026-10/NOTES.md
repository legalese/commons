# Superannuation (Unclaimed Money and Lost Members) Act 1999 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; two gaps answer `not covered`, and tests assert both.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0072` in `subjects/au/requirements.jsonl` (a scheduled priority-2 entry for the 20 topics: pensions and retirement savings). There was no earlier encoding of this Act to keep. No scenario life raised it, so the people in the case file (Ron, Rita, Mia, Lena) and every date are the encoder's, hypothetical.

Fifteen questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Edition

Compilation No. 42, compilation date 28 September 2022, includes amendments up to Act No. 127, 2021 (register id **C2022C00273**), as deposited at `../../registers/source-bundle/C2004A00518.txt` (retrieved 13 October 2026 as the current compilation).

No instrument is deposited. What the Act leaves to an instrument is handled this way:

- **Unclaimed money days and scheduled statement days** (the Commissioner's legislative instruments under ss 15A and 20B): inputs, as dates.
- **Interest** the Commissioner pays with a refund "worked out in accordance with the regulations": the encoding says whether interest is due, not how much.
- **Things "prescribed"** (visas excluded from s 20AA, the conditions of release in s 20QA(1)(a)(vi), the "prescribed period" in s 24NA(2)(c), the KiwiSaver "matters", a later day under s 20F(1)(c)): asked as facts.
- **Eligibility age:** the Act's own 65 (a man) and 60 (a woman) are used. An age prescribed by the regulations would change the answers (finding 1).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sumlma-member.l4` | `sumlma-cases-member.l4` | 90 written, 90 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The member** of a superannuation fund, approved deposit fund or RSA (s 8 "member"). Where a member has died, the seat is the person entitled to the benefit: a death beneficiary or the legal personal representative. For s 12(2) it is the non-member spouse under a family law payment split.

The questions are the ones that person asks: "Is my super unclaimed or lost?", "Is my old account going to be sent to the ATO?", "When must my fund pay it over?", "Whom will the ATO pay it to — can I have it in cash?", "Is interest paid?", "Will the ATO put it into my active account?", "Can the ATO take an overpayment back?", "Can I object?".

Almost every operative provision is addressed to the superannuation provider or the Commissioner. Those provisions are encoded as what they mean for the member: what my fund must do and by when, whom the Commissioner must pay, and what the Commissioner may recover from me.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is deposited (see Edition).
- **The actors the text names:** the member, the superannuation provider, the Commissioner, the non-member spouse, the death beneficiaries and the legal personal representative.
- **Judgments left to others, answered conditionally:** the Commissioner's satisfaction (s 17(1C)(b) and its counterparts, ss 20H, 24NA); the provider's determination under s 14(b); its "reasonable efforts" and inability to contact (ss 12, 13, 14); its satisfaction under s 24B(2)(c). All are asked as facts.
- **The Act's own definitions worked out from facts:** eligibility age, unclaimed money, inactive low-balance account, lost member account and former temporary resident. **Borrowed terms asked as facts:** "lost member" (from the SIS and RSA Regulations), complying superannuation plan, terminal medical condition, and New Zealand-sourced amount.
- **One case:** one member and one account (or one amount the Commissioner holds).
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** objects, registers, tax file numbers, records, regulations, compensation for acquisition of property.

## Scope

**In:**
- s 10(1), (2): eligibility age.
- s 12(1), (2) and s 13(1), (1A): unclaimed money, and the fund's duty to try to reach me.
- ss 14, 15(1): a member who has died.
- s 20QA(1), (1A): inactive low-balance account.
- s 24B: lost member account.
- s 20AA(1): former temporary resident.
- The days by which my fund must pay the Commissioner: ss 17(1), 20E(2), 20F(1), 20QD(1), 21C(2), 24E(1), and s 22 (a voluntary payment, which has no day).
- Whom the Commissioner must pay: ss 17(1C)–(2AAB), 20QF(1)–(3), 21E(1)–(3), 22B(1)–(3) and 24G(1)–(2A). The death beneficiaries' shares are worked out only where there is one beneficiary.
- Whether interest is due: ss 17(2AB)–(2AE), 20QF(5)–(6), 21E(5)–(6), 22B(5)–(6), 24G(3A)–(3D).
- s 20H(1)–(3): paying a former temporary resident back.
- s 24NA(1)–(2): the transfer to my active account.
- Recovering an overpayment from me: ss 20L, 20QK, 21G, 22E, 24K, and s 24NAA.
- s 20P: objection.

**Out:**
- The statements and their corrections (ss 16, 16A, 20E(1), 20QB, 20QC, 21A, 21B, 22A, 24C, 24D), except their due days.
- The amount formulas: s 17(1A), and the death-beneficiary formulas in ss 17(2AA), 20H(4), 20QF(4), 21E(4), 22B(4) and 24G(3). These are lost in conversion (finding 9); more than one death beneficiary answers `not covered`.
- The amount under s 20F(2)–(4).
- State, Territory and prescribed public sector schemes: ss 18, 18AA, 20JA, 20QG, 20QH, 22D, 24H, 24HA.
- Refunds to providers and repayments by them: ss 18A, 18C, 20K, 20M, 20QJ, 20QL, 21F, 21H, 22C, 22F, 24J, 24L, 24NB.
- s 20J, except as a decision I may object to.
- s 20H(2A)–(2C): interest on payments made before 1 July 2013.
- s 24NA(3) (more than one qualifying fund): `not covered`.
- The offences' penalty amounts (100 penalty units, quoted in comments).
- Parts 1, 5 and 6; ss 19, 20, 20N, 23, 24 and 24M.

The general interest charge and the Taxation Administration Act machinery the notes point to are not encoded.

## What the Act turns out to say

1. **Eligibility age is 65 for a man and 60 for a woman, unless the regulations prescribe another age; a member the fund cannot sex is a man.** Section 10(1) states both ages, with "if another age is prescribed by the regulations, the age so prescribed". The Superannuation (Unclaimed Money and Lost Members) Regulations 1999 are not deposited, so the Act's figures are used. If the regulations prescribe 65 for women, a woman of 60 to 64 gets the wrong answer here. Section 10(2)(a) treats a member of unknown sex as a man. Asserted (s 10 cases, Rita at 61, the 62-year-old of unknown sex). Raised as `REQ-0086`.
2. **Super becomes unclaimed money only when three things are all true, and the fund must try first.** Under s 12(1) the member must have reached eligibility age, nothing may have been received (or accrued, in a defined benefit scheme) for 2 years, and the fund must have been unable to make contact again after reasonable efforts, once 5 years have passed since its last contact. There is no paragraph (b). Once (a) and (c) hold and the 5 years have passed, s 13(1) requires the fund to make reasonable efforts to reach the member (an offence, 100 penalty units). The encoding reads "within the last 2 years" as 24 or more complete months with nothing received, so exactly 24 months qualifies. Asserted.
3. **The Act fixes almost none of the payment days itself.** Unclaimed money, inactive low-balance accounts and lost member accounts are due "at the end of the scheduled statement day for the unclaimed money day". Both days are set by the Commissioner's legislative instrument (s 15A), which is not deposited, so they are inputs. The former temporary resident payment has a rule of its own (s 20F(1)): the next scheduled statement day after the notice, or the following one if the notice came "less than 28 days before". A notice exactly 28 days before therefore falls due on the next day, not the following one. Only the eligible rollover fund days are fixed: 30 June 2021 for an account under $6,000 on 1 June 2021, otherwise 31 January 2022 (s 21C(2)). Both are now past. Asserted, including the statute's own 15 April example.
4. **Getting the money in cash depends on which Part sent it to the ATO.**
   - **Unclaimed money (s 17(2)(d)).** It goes "in any other case — to the person", so a living member who gives no direction is paid directly. A member who directs a fund that is not a complying superannuation plan is also paid directly, because (a) is not met.
   - **Inactive low-balance, ERF, voluntary and lost member amounts (ss 20QF(3), 21E(3), 22B(3), 24G(2A)).** The member is paid directly only if three things hold: no direction was given; the member has reached eligibility age (and the New Zealand age for a New Zealand-sourced amount), or the amount is under $200, or the member has a terminal medical condition; and the member has not died. A failed direction (to a non-complying fund) therefore leaves the member with nothing until a fresh direction is given.
   - **A fund the New Zealand rule forbids** (ss 17(2AAA) and the like). This encoding reads it as not "any other case" under s 17(2)(d): the Commissioner simply cannot pay that fund. This is an interpretive choice, not tested against any ruling.

   Asserted (Ron's and Mia's cases).
5. **The New Zealand test for a transfer to my active account is looser than the one for a direction.** For a direction, ss 17(2AAA), 20H(2AAA), 20QF(2A), 21E(2A), 22B(2A) and 24G(2AA) forbid payment to a fund if it is self managed **or** has not notified that it accepts New Zealand-sourced amounts. For a transfer, s 24NA(2)(f) requires only that the fund "is not self managed superannuation fund" **or** has notified. So an APRA fund that has never notified can receive a New Zealand-sourced amount under s 24NA, but not under a direction. Whether this is deliberate is not known. Asserted.
6. **Interest is due on every refund, but on unclaimed money and lost member money only for payments from 1 July 2013.** Sections 17(2AB) and 24G(3A) apply to payments "on or after 1 July 2013". Sections 20QF(5), 21E(5) and 22B(5) have no date, because those Parts are later. How much interest is the regulations' (the rate may be nil), and nothing here computes it. Asserted (whether due, not how much).
7. **The Act gives an objection only for the former temporary resident Part.** Section 20P lets a person object under Part IVC of the Taxation Administration Act 1953 to a notice or decision under Division 2, 4 or 5 of Part 3A: the s 20C notice, payment or refusal under s 20H, revocation under s 20J, and recovery under s 20L. No provision of this Act gives an objection or review for decisions under Parts 3, 3B, 3C, 3D, 4A or 4B (unclaimed money, inactive low-balance, ERF, voluntary, lost member, and transfers to an active account). Whether some other Act provides one was not checked. Asserted.
8. **An overpayment can be taken back from me only after a notice and 28 days, never above the notice, and never for a transfer to my active account.** The recovery provisions (ss 20L, 20QK, 21G, 22E, 24K) need a written notice naming the amount, at least 28 days to have passed since it was given, and recovery "not more than the amount specified in the notice". Recoveries from all debtors together may not exceed the excess. Under s 24NAA(3) an overpayment into my active account is recoverable only from the superannuation provider. Asserted. 28 days after a notice given on 1 March is 29 March.
9. **The formulas are missing from the deposit.** Wherever the Act says "the following formula:", the converted text has nothing after it. That affects s 17(1A) (the amount a provider pays), and ss 17(2AA), 20H(4), 20QF(4), 21E(4), 22B(4) and 24G(3) (the death beneficiaries' shares). The notes say that "If there is only one death beneficiary, the whole of the amount is payable to that beneficiary", and that is the only share encoded. Asserted (`not covered` for two beneficiaries). A `C2004A00518.formulas.md` sidecar transcribed from the authorised rendering would close it.
10. **A New Zealand citizen is never a former temporary resident.** Section 20AA(1)(c)(ii) excludes Australian and New Zealand citizens. The 6 months run from the later of the visa ceasing and departure. Asserted.
11. **Under s 20H, a direction to a super fund works only for a citizen or permanent resident.** Section 20H(2)(b) needs the Commissioner to be satisfied that the person is an Australian or New Zealand citizen, or holds a permanent (or prescribed) visa. Otherwise payment is to the person under (a), subject to departing Australia superannuation payment withholding (s 20H(6)). That withholding is not encoded. Asserted.

## What would need doing before this is worth relying on

- **The Superannuation (Unclaimed Money and Lost Members) Regulations 1999**, deposited and brought in. They hold the eligibility age (if another is prescribed), the interest rates, prescribed visas, the s 24NA(2)(c) period and the s 24NA(3) allocation, and the KiwiSaver matters. Raised as `REQ-0086`.
- **The Commissioner's s 15A and s 20B instruments** setting the unclaimed money days and scheduled statement days, so that a due day can be computed rather than supplied. Raised as `REQ-0087`.
- **A formulas sidecar** for s 17(1A) and the death-beneficiary formulas (finding 9).
- **The SIS and RSA Regulations' definitions of "lost member"** and the conditions of release prescribed for s 20QA, which are asked as facts here.
- **Wider sources.** No ATO guidance, ruling or case was read. Findings 4 and 5 are readings of the text alone.
