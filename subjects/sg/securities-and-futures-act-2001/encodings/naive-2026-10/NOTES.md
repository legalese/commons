# Securities and Futures Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 25 of
2021 shown in force).

**Checks:** two case files, 99 assertions satisfied (52 market conduct + 47 offers and exemptions), 0 errors, 0 warnings.

## Why this Act, and why scoped

**36 of the 527 Singapore Acts** deposited here cite it, the most of any Act not yet
encoded. The deposit is about 1.8 million characters. This row takes Part 12 market
misconduct only: false trading (s 197), false statements (s 199), continuous
disclosure (s 203), insider trading (ss 214-231), and the penalties and civil
liability that follow (ss 204, 221, 232-234). Licensing, prospectuses, collective
investment schemes, takeovers, benchmarks and the Division 5 corporate-liability
provisions are not encoded.

## What the Act turns out to say

### 1. Insiders: a director can be negligent; anyone else must know

s 218 catches a **connected** person (officer, substantial shareholder, adviser) who
"knows or ought reasonably to know" the information is inside information, and
s 218(4) **presumes** that knowledge once possession is proved. s 219 catches
everyone else only if they actually **know**. There is no "ought to know" and no
presumption. A director who should have realised is liable; a dinner guest who
should have realised, but did not, is not. Asserted.

### 2. A negligent false announcement contravenes s 199

s 199(e): "knows or ought reasonably to have known". A careless market announcement
contravenes Part 12 just as a deliberate one does. Asserted.

### 3. Negligent non-disclosure is a contravention but not a crime

s 203(1) forbids failing to disclose "intentionally, recklessly or negligently".
s 203(3) then says it is not an **offence** unless it was intentional or reckless. A
negligent failure is open to a civil penalty and to investor claims, but not to
prosecution. Asserted.

### 4. Investors against an insider share the insider's profit; investors misled by a statement get their loss

s 234(1) gives traders who dealt contemporaneously with an insider a claim only if
the insider made a profit or avoided a loss, and s 234(2) and (6) cap each claim at
the profit, less what other claimants have already been awarded. An insider who made
$10,000 owes $10,000 between all of them, however much they lost.

s 234(1A), added in 2012, makes a person who made a false statement liable "whether
or not" they profited, to anyone who dealt **in reliance** on it. Under (2A)(b) that
claim has no profit cap. A company that made nothing from a misleading announcement
owes every relying investor their whole loss. Asserted.

### 5. Civil penalty and prosecution are alternatives

Under s 232 the civil penalty is up to the greater of 3 times the profit and $2
million, with a floor of $50,000 (individuals) or $100,000 (corporations). Under
ss 204(2) and 221(2), a civil penalty order or agreement bars prosecution. Under
s 233(2), a conviction or an acquittal on the merits bars a civil penalty. Asserted.

### 6. Smaller things worth recording

- **s 197(3):** a wash trade or matched orders raise a rebuttable presumption of a
  false-appearance purpose.
- **s 220:** no need to prove intention to use the inside information.
- **s 228:** knowing only your own plan to deal is not inside information.
- **s 231:** parity defence: the counterparty knew, or ought reasonably to have known.

## What would need doing before this is worth anything

- **No case law was searched.** "Generally available", "material effect" and
  "contemporaneously" are judge-made in practice.
- s 234(5)'s factors for "contemporaneous" are reduced to a flag.
- Division 5 (corporate liability for employees' contraventions) and s 236
  (claims after conviction) are not encoded.

## Source refreshed after encoding (10 Oct 2026)

This row was encoded against the deposit as it stood before the source refresh: the SSO consolidation current at the
earlier retrieval, still in git at commit da331074. The deposit has since been replaced by the consolidation current as at
9 October 2026, whose text differs. **The row has not been re-checked against the refreshed text.** Its assertions do not
read the source, so they still pass; whether the encoded provisions changed is an open question.

## Offers of shares and the prospectus exemptions (added 12 October 2026 for REQ-0285)

Module `sfa-offers-exemptions.l4`, cases `sfa-cases-offers-exemptions.l4` (47 assertions). Encoded against the deposit
as it now stands (consolidation in force from 29/6/2026 to 20/10/2026), body section numbers.

1. **No prospectus is needed for either issue, on the question's facts.** Each issue is to one person within its
   12 months, so s 272B (private placement) applies; and each is for $200,000 or more to an investor taking the shares
   as principal, so s 275(1A) applies too. Both are subject to the same three conditions: no advertisement, no selling
   or promotional expenses beyond professional fees and licensed dealers' commissions, and no registered prospectus
   standing in the way. The question states none of these, so the encoding assumes them absent. The angel's issue four
   years earlier does not count towards the fund issue's 12-month window.
2. **Whether the angel is an accredited investor cannot be answered from the facts given, and it does not matter for
   the prospectus.** s 4A(1)(a)(i) asks about wealth and income: net personal assets over $2 million (the primary
   residence counted net of secured credit and at no more than $1 million, s 4A(1A)), net financial assets over
   $1 million, or income of at least $300,000 in the preceding 12 months. The size of the investment is not a test.
   The case file shows one angel who is and one who is not.
3. **Where the text differs from the ledger's expectation.** The ledger's answer is right in result but not in its
   reasons. (a) s 272B allows offers to **no more than 50** persons in 12 months, not "fewer than 50". (b) The
   ledger's alternative route, "to an accredited investor" (s 275(1)), is not needed: s 275(1A) exempts any offer on
   terms of at least $200,000 a transaction to a principal, whatever the investor's status. (c) The arrangement table
   in the deposit is one line out of step for ss 273-275: in the body s 274 is the institutional-investor exemption
   and s 275 the accredited-investor exemption.
4. **s 272A (small offers) also fits the fund issue, just.** Personal offers raising in total no more than $5 million in
   12 months are exempt; $5,000,000 does not exceed $5 million. But s 272A also needs the written statement and resale
   notification in s 272A(1)(b), which the question does not mention, so the encoding does not rely on it.
5. **If the venture fund is a collective investment scheme, or its manager holds a capital markets services licence,
   it is an institutional investor** (s 4A(1)(c)(xxiv), (xiv)) and s 274 exempts the offer with no conditions at all.
   That is an inference about how venture funds are structured, not a fact in the question.
6. **An offer that fits no exemption is an offence**: s 240(7), fine up to $150,000 or up to 2 years' imprisonment
   or both, plus up to $15,000 a day for a continuing offence after conviction.
7. **What the full answer needs from elsewhere.** The Authority may prescribe amounts in place of the Act's
   $2 million, $1 million, $300,000, $10 million, $5 million and 50 (ss 4A(1)(a), 272A(1)(a)(ii), 272B(2)) and of
   $200,000 by Gazette order (s 275(4)); the "closely related offer" factors (ss 272A(6), 272B(4)); s 4A(2)
   modifications; the Securities and Futures (Classes of Investors) Regulations 2018, which (outside this deposit) are
   understood to govern opting in to accredited-investor status -- the Act itself says nothing of opt-in; and the
   Securities and Futures (Offers of Investments) (Exemption) Regulations, if any apply. None was retrieved. Not
   encoded: s 257 (allotment with a view to resale, which every exemption leaves in force), s 276 (resale of
   securities first acquired under ss 274-275), s 272A(8), s 273, and the Companies Act 1967 rules on private
   companies.
