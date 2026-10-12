# Bretton Woods Agreements Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `../../registers/source-bundle/BWAA1966.txt`.
The deposit says it "incorporates all amendments up to and including 1 December 2021
and comes into operation on 31 December 2021"; its page footer reads "Informal
Consolidation – version in force from 11/12/2023". The latest amending Act in its
Legislative History is Act 20 of 2023 (Bretton Woods Agreements (Amendment) Act 2023,
commenced 11 December 2023), annotated against ss 5(2), 6A(3A) and 6A(5). Section
numbers follow the body: the arrangement at the top of the deposit is out of step by one.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0160**: tier 3 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The honest
answer is: almost nothing directly. The Act provides for the State's membership of the
International Monetary Fund and the World Bank (IBRD); a person meets it only through
s 12 and through any order under s 11. The Act has 13 sections, so most of it is
encoded: who pays (ss 4 to 10), s 6A, s 7(3), ss 11 and 12, and the terms of admission
in both Schedules. Not encoded: the short title, the s 2 authority to sign, the
definitions, the detail of the MAS's SDR and General Resources Account powers (ss 5, 6),
the Articles of Agreement themselves (not deposited), any order made under s 11 (none
retrieved), and the acceptance windows (First Schedule para 9, Second Schedule para 7),
which ran out in 1966 unless extended.

## What the Act turns out to say

### 1. A grant to the IMF need not be recoverable, but a loan must be

s 6A(4) requires an agreement "to lend or give other financial assistance" to let the
MAS demand early repayment if the Fund arrangement is suspended or ended early. Grants
are named in s 6A(1) but left out of (4). The 2023 amendment added two further
exceptions in (5): a Fund standard form the MAS cannot amend, and an arrangement that
cannot be suspended or ended early. Asserted.

### 2. A Fund office in Singapore escapes every s 6A safeguard except early repayment

s 6A(3A) (2023) disapplies (2) and (3) for an agreement financing a Fund office in
Singapore. So there is no need for a Fund request, another government's participation,
a Gazette statement, or a Parliamentary cap on grants. (3A) does not mention (4). If such
an agreement lends money, the early-repayment term is still required unless (5) applies.
Asserted.

### 3. Grants need Parliament; loans need only the Gazette

Under s 6A(2)(d), grants need a resolution of Parliament fixing their maximum, and
s 6A(3) makes it "not lawful" to exceed it. Loans and other assistance need only a
Minister's Gazette statement of the maximum. The text does not say whether the grant
cap is cumulative. This encoding reads it as a cap on the total under the agreement,
which is an inference. Asserted.

### 4. The World Bank is paid from the Consolidated Fund; the IMF is paid by the MAS

The Bank subscription, increases in it, par-value adjustments, note redemptions and
the interest on any s 9 loan are all "charged on the Consolidated Fund" (ss 7 to 9).
The IMF subscription, its increases, SDR and General Resources Account charges and
s 6A assistance are functions of the MAS (ss 4 to 6A). Notes to the Bank and s 9
loans need the President's concurrence under Article 144(1)(b) of the Constitution.
Notes to the Fund are authorised to the MAS directly (s 4(3)). Asserted.

### 5. A ceiling for the Bank, none for the Fund

s 7(3) caps the Bank subscription at US$40 million, including increases, unless
Parliament resolves otherwise. The Second Schedule subscription is 320 shares at
$100,000, which is $32 million, leaving $8 million of headroom. Those Schedule dollars
are "of the weight and fineness in effect on July 1 1944", while s 7(3) says "US$". The
encoding compares them as one unit, and that is an inference. No ceiling is written for
the Fund: under s 4(2) a quota increase needs only the Minister for Finance's approval.
Asserted.

### 6. Only 10% of the Bank subscription was paid in on joining

Second Schedule para 4: before membership, Singapore paid 2% (gold or US dollars) and 18%
(own currency) of the price of half the shares. That is $320,000 and $2,880,000. The same
portions on the other half were "left uncalled" ($3,200,000). The Schedule does not say
what happens to the remaining 80% of each share. Asserted (the arithmetic).

### 7. Missing the par value deadline counted as withdrawal only once the Fund had extended it

First Schedule para 5 deems Singapore "to have withdrawn from the Fund if agreement on a
par value has not been reached when the extended period expires". It says nothing about
a 60-day period that was never extended. Asserted. (The par value system has since gone.
The 1976 amendments named in s 3 established "a reformed international monetary system",
but their content is not in the deposit.)

### 8. s 12 is the only rule here that reaches a private investor directly

The Bank is "deemed not to be a corporation" under the Companies Act 1967. That Act does
not apply to the Bank or to its issue of "shares, debentures, bonds, notes or other
securities". The section names the Bank only, not the Fund. s 11 lets the President give
the Fund Agreement's rule on "the unenforceability of exchange contracts" the force of
law by order, but the Act itself enacts nothing of it. Asserted.

## What would need doing before this is worth anything

- Any order made under s 11 (immunities, privileges, exchange contracts) should be found
  and read. That is where a person or business would actually meet this Act.
- The Fund and Bank Articles of Agreement, and the current quota and shareholding, were
  not read. The Schedules record the 1966 terms only.
- The cumulative reading of the s 6A(3) grant cap and the unit used in s 7(3) are
  inferences that need checking.
