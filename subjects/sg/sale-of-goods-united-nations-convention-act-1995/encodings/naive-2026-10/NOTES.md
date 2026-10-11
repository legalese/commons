# Sale of Goods (United Nations Convention) Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as the finished naive rows show them (the skill itself
was not loadable in this session). No pipeline, no coverage table, no independent
test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SGUNCA1995.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. Its Legislative History lists Act 14 of 1995 (commencement
1 March 1996) and the 1996 and 2013 Revised Editions; no amending Act is annotated.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings. A deliberate
wrong value was caught (52 of 53) before the file was finalised.

## Why this Act, and why scoped

Requirement **REQ-0103**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The Act is five sections. Its substance is the Vienna Convention (CISG) in the
Schedule, 101 articles. This row takes what a Singapore business that imports or
exports goods meets first: whether the Convention governs (s 3, Arts 1 to 6), offer,
revocation and the reply that changes terms (Arts 14, 16, 19), fundamental breach and
the buyer's right to avoid or demand substitutes (Arts 25, 46, 49, 82), notice of
defects (Arts 39, 40, 44), price reduction (Art 50), damages on avoidance (Arts 75 to
77) and impediments (Art 79). Not encoded: interpretation and usages (Arts 7 to 13),
the timing rules for communications (Arts 15, 17, 18, 20 to 24), the seller's and
buyer's detailed duties (Arts 30 to 38, 41 to 43, 53 to 60), the seller's remedies
(Arts 61 to 65), risk (Arts 66 to 70), anticipatory breach and instalments (Arts 71
to 73), interest, effects of avoidance and preservation (Arts 78, 80, 81, 83 to 88),
and Part IV.

## What the Act turns out to say

### 1. Singapore cut the Convention down to sales between two Contracting States

Art 1(1)(b) would apply the Convention whenever conflict rules lead to the law of a
Contracting State. s 3(2) says that sub-paragraph "does not have the force of law in
Singapore", so the Convention applies "only between those parties whose places of
business are in different States when the States are Contracting States". A
Singapore buyer dealing with a seller in a non-Contracting State falls outside it even
where Singapore law governs the contract; the Convention as written would have caught
that sale. s 3(3) lets the Minister delete s 3(2) if the Art 95 reservation is
withdrawn. Asserted (both the Singapore rule and the counterfactual).

### 2. A consumer sale is out only if the seller knew or ought to have known

Art 2(a) excludes goods "bought for personal, family or household use, unless the
seller ... neither knew nor ought to have known" of that use. Personal-use goods
ordered in a way that gave the seller no reason to suspect it (the fixture: a company
letterhead) stay inside the Convention. Auctions, execution sales, securities and
money, ships and aircraft, electricity, goods made from materials the buyer supplies,
and contracts mainly for labour are all out, and the parties may exclude it (Art 6).
The different-States fact counts only if it appears from the contract or dealings
(Art 1(2)). Asserted.

### 3. The two-year limit on notice of defects survives a reasonable excuse

Art 39(2): the buyer loses the right to rely on a lack of conformity unless notice is
given within two years of actual handover, "unless this time-limit is inconsistent
with a contractual period of guarantee". Art 44 lets a buyer with a reasonable excuse
still reduce the price or claim damages "except for loss of profit", but only
"notwithstanding ... paragraph (1) of article 39" -- the reasonable-time rule. It does
not reach the two-year limit. Art 40 does: a seller who knew and did not disclose
cannot rely on Art 39 at all. Treating a guarantee longer than two years as replacing
the limit is an inference. Asserted.

### 4. A reply that changes the price, liability or dispute forum is a counter-offer

Art 19(1) makes a reply with "additions, limitations or other modifications" a
counter-offer. Only terms that "do not materially alter" the offer become part of the
contract, and then only if the offeror does not object without undue delay. Art 19(3)
lists as material, "among other things", price, payment, quality, quantity, delivery,
"extent of one party's liability" and "the settlement of disputes" -- so adding an
arbitration clause or a liability cap to an acceptance makes a counter-offer.
Asserted.

### 5. Avoidance and substitute goods need a fundamental breach and the goods back

The buyer may avoid for a fundamental breach (Art 25: substantial deprivation, unless
neither the party in breach nor a reasonable person would have foreseen it) or, for
non-delivery, after an additional period under Art 47 runs out (Art 49(1)). Once the
goods are delivered he must act within a reasonable time (Art 49(2)). Art 82 bars both
avoidance and substitute goods if he cannot return the goods substantially as
received, unless that is not his doing, came from examination, or the goods were sold
or used in the normal course before the defect was discoverable. Art 83 keeps his
other remedies. Asserted.

### 6. Price reduction is proportional, and damages follow the cover or market price

Art 50 reduces the price "in the same proportion" as the delivered goods' value bears
to conforming goods' value at delivery, paid or not, but not if the seller cured
under Art 37 or 48 or the buyer refused that cure. Art 75 gives the difference to a
replacement purchase or resale, Art 76 the difference to the current price (at taking
over, if the buyer avoided after taking over the goods), both less what the claimant
failed to mitigate (Art 77). Reading "the difference" as recoverable only where it is
a loss is an inference. Art 78 gives interest on sums in arrears but states no rate.
Asserted (except Art 78).

### 7. An impediment excuses damages only, and a subcontractor must be excused too

Art 79(1) requires an impediment beyond the party's control that it could not
reasonably have foreseen, avoided or overcome. If a third person it engaged failed,
both must qualify (Art 79(2)). The exemption lasts only while the impediment exists
and leaves "any right other than to claim damages" intact (Art 79(3), (5)).
Asserted.

## What would need doing before this is worth anything

- Which States are Contracting States, and their Art 92, 95 and 96 declarations,
  are left by s 5 to Gazette notifications. None was retrieved, so "both States are
  Contracting States" is an input.
- Part IV is partly scrambled by page layout in the deposit (the extracted body runs
  Art 92(2) into Art 99(6)); it was read from the raw text only for Arts 95 to 97.
- Time is counted in whole months; "reasonable time" and "fundamental" are inputs.
- No Singapore or foreign CISG case law was searched, and the Art 14 / Art 55 tension
  over open-price contracts is noted but not resolved: Art 14 requires the price to
  be fixed or determinable for an offer, while Art 55 fills a missing price only for a
  contract "validly concluded".
- The seller's remedies, risk, anticipatory breach and preservation of goods are not
  encoded.
