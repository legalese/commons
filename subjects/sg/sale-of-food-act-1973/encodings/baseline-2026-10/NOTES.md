# Sale of Food Act 1973 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the Act is applied, with the design defaults
ruled on 2026-10-18. No pipeline, no coverage table, no independent test pass, no human gate.
No `REFUSE`: where the encoding has no answer, a decision returns `NOTHING` and its comment
says why. Not for public use as advice.

This encoding replaces the one moved to `solutions` (Litigate.4) on 2026-10-19. That
encoding's NOTES.md was read for scope and known pitfalls. Its L4 was not copied.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 1 May 2026
(SSO "Current version as at 01 Oct 2026"), as deposited at
`../../registers/source-bundle/SFA1973.txt`.

**Checks:** one module (`sfa-seller.l4`) and one case file (`sfa-cases-seller.l4`). The case
file is built by the scratchpad generator `gen_sale-of-food-act-1973_baseline.py`, with
expected values written by hand from the text. Result: 59 assertions satisfied, 0 errors,
0 warnings, on the stable `l4` from VS Code extension 1.6.98. The module on its own also runs
with no errors or warnings.

To show the check can fail, a copy was run with one expected value changed (10000 to 9999 in
the second-conviction penalty). It gave 58 satisfied and 1 error.

The stable binary's `daydate` has no `YMD`, so dates in the cases use the little-endian
`Date day month year`.

## Seat

**The food seller: the person who sells or handles food, including one who carries on a food
business.** That covers a hawker, a caterer, a central kitchen, an importer and a wholesaler.

The Act's prohibitions are addressed to "a person" who sells, labels, advertises or carries
on a food business, and its penalties fall on that person. The consumer the Act protects is
not the person it is applied to. The Director-General's powers come in only as what may be
done to the seller and what the seller must be given: a seizure and the notice of it, a
direction and its penalty, a licence penalty, and the appeals against them.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed, but no
  food regulations or orders were deposited. So what they prescribe is asked as a fact:
  - prohibited substances and permitted proportions (ss 12, 13);
  - labelling requirements (s 16);
  - the prescribed standard (s 25(d));
  - the limit for farm or veterinary chemicals (s 2D(2)(b));
  - the licence fee (s 46(8));
  - which offences are compoundable (s 50).

  Two answers come back as `NOTHING` instead: the s 10J appeal period ("a prescribed
  period") and the penalty for an offence created by regulations.
- **The actors the text names.** Followed: the Director-General, authorised officers, the
  Agency, the Minister, the prosecutor, the warrantor, the purchaser, the Magistrate's Court,
  the District Court and the General Division of the High Court.
- **Someone else's judgment answered conditionally.** Followed. Three judgments are inputs:
  "knows or ought reasonably to know", "reasonable excuse" and "insufficient grounds". Whether
  food would be likely to cause harm is also an input. The licence fee is answered "if the
  Director-General charges proportionately".
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.**
  Followed. Worked out: food (s 2A), food business (s 2B), unsafe (s 2C), unsuitable (s 2D),
  sell (s 2E), non-retail food business (s 2F) and adulterated (s 25). Asked as facts:
  - health product, medicinal product, controlled drug and poison (other Acts);
  - the First Schedule purposes of the Environmental Public Health Act 1987;
  - the District Court's jurisdictional limit.
- **One case is the text's natural unit.** Followed: one article, one activity, one sale, one
  warranty, one direction, one offence.
- **The Act's own terms, each with a plain gloss.** Followed, in comments beside each type and
  field.
- **Operative sections in, machinery out.** Followed: s 3 (administration), s 54 to 56
  (exemptions, regulations) and the appointment of officers and analysts are out. **Departure:**
  some operative provisions are also out, to stay within size and because the seller meets
  them least. They are:
  - the inspection and sampling powers themselves (ss 4 to 8);
  - the content of each Part 2A direction (ss 10D to 10H);
  - the infectious-disease and vehicle rules (ss 22, 23);
  - the presumptions in ss 26 to 28;
  - forfeiture and publication of convictions (ss 42, 43);
  - licence grant and security (s 46(1) to (5)).

## Why this scope

The seat decides it. The encoding takes the questions a food seller asks, in the order they
meet them:

1. Is this food (s 2A)?
2. Am I running a food business, and must I be licensed (ss 2B, 2F, 21)?
3. Is what I do "selling" (s 2E)?
4. Is the food unsafe, unsuitable or adulterated (ss 2C, 2D, 25)?
5. Which Part 3 offences does my sale commit (ss 11 to 20, 31)?
6. What defences do I have (ss 16A(6), (7), 32, 33)?
7. What happens if my food is seized or I get a direction (ss 4(2), (4), 10I, 10K)?
8. What can I appeal, and by when (ss 45, 46(14))?
9. What can my licence cost me (s 46(9), (12))?
10. What are my summons dates (ss 30, 34)?
11. What is the most I can be fined, or asked to pay to compound (ss 48, 49, 50)?

The s 10K(1) duty is also written as a regulative rule, `my duty to comply with the
direction`, with the time to comply taken from the direction. It checks, but it is not traced.

## What the Act turns out to say

1. **Unfit food is still food, and an edible wrapper is food too.** s 2A(4) makes a thing food
   "regardless of whether or not it is in a condition fit for human consumption". s 2A(3)(g)
   excludes "any package (except edible packaging)". Medicines, health products, tobacco and
   animal feed are not food. Asserted.

2. **A one-off charity bake sale is a food business; an online marketplace is not.** s 2B(1)
   applies whether the activity is "commercial, charitable or community" and even if it
   happens "on one occasion only". s 2B(2)(a) takes out an intermediary in a non-food
   business, "such as an Internet service provider or an auction site". Asserted.

3. **Only a non-retail food business needs the Director-General's licence under this Act.** A
   hawker stall run wholly for an Environmental Public Health Act First Schedule purpose does
   not need one under s 21. A central kitchen does. Trading without one is an offence under
   s 24(1).

   The "but includes" words in s 2F(1) would, read literally, sweep in every retail business.
   They are read as reaching a business that is partly retail. That is a reading, labelled in
   the module. Asserted.

4. **Giving food away can be selling; donating it to charity is not.** s 2E(1)(l) and (n) make
   free samples to promote a business, and free meals to hospital patients, a sale. s 2E(3)(b)
   says food donated for a charitable purpose is not food given away to advertise. Asserted.

5. **An allergy does not make food unsafe; damaged packaging can make it unsuitable.** Under
   s 2C(2)(d), food is not unsafe merely because it is unhealthy for someone with an allergy.
   Under s 2D(1)(e), food is unsuitable if its packaging is damaged to the extent of affecting
   its use. s 15(3) says unsuitability is an offence "whether the food concerned is safe" or
   not. Asserted.

6. **Selling unsafe food is an offence only if I knew or ought reasonably to have known it was
   unsafe.** s 15 turns on the seller's knowledge, but ss 11 to 14 and 16 to 19 do not.
   Selling adulterated food is not an offence if I "fully" told the buyer at the time (s 11).
   The alcohol limit is "more than 50 parts" per million (s 14), so 50 is lawful and 51 is not.
   Asserted.

7. **A test purchase still counts as prejudice to the buyer.** s 18 requires a sale "to the
   prejudice of the purchaser". s 31 says it is no defence that the purchaser bought for
   analysis "and therefore was not prejudiced". Asserted.

8. **"I did not mean to" is a defence only with proof of all reasonable steps.** s 32. Asserted.

9. **A supplier's written warranty is a defence only with notice within 7 days of the
   summons.** Under s 33(3), the notice goes to the prosecutor, and a like notice by
   registered post to the warrantor. Under s 33(2), a warranty from someone resident outside
   Singapore also needs proof that I checked it and believed it. Read as service day + 7.
   Asserted.

10. **The publisher's defence is never open to the food business itself.** s 16A(7)(c) shuts
    it for "the proprietor of a food business or ... otherwise engaged in the conduct of a food
    business for which the advertisements ... were published". Asserted.

11. **A seizure can be challenged only within 48 hours.** After that the food "becomes the
    property of the Agency" (s 4(2), (3)). The owner is owed immediate written notice only
    when the name and address are known and the address is in Singapore (s 4(4)). Asserted.

12. **Breaching a direction carries a heavier penalty than most of the Act.** The penalty is
    $10,000 or 12 months (s 10K(2)), against the general $5,000 for a first conviction
    (s 49). A reasonable excuse answers it. Removing a posted direction is an offence only
    while the direction is in force (s 10K(3)). Asserted.

13. **The compensation clock runs even if the Agency stays silent.** If the Agency does not
    decide within 28 days it is taken to have refused, and I have 14 days after that to go to
    the District Court (s 10I(4), (5)(b)). Asserted.

14. **Only the general appeal to the Minister stays the decision.** s 45(1) gives 7 days and a
    stay. Licence appeals under s 46(14) have 14 days and no stay is mentioned. The period for
    a Part 2A direction is "prescribed" and not known here. Asserted.

15. **A licence condition breach can cost up to $5,000 without any prosecution.** The
    financial penalty in s 46(12)(d) is open only for breach of a condition or restriction. A
    non-offence failure can lead to suspension or cancellation but no penalty. A short licence
    is charged by the month, part months counting whole (s 46(9)); the fee is asked. Asserted.

16. **The general penalty doubles on a second conviction and adds prison.** s 49: $5,000;
    then $10,000 or 3 months or both. Composition is at most $1,000, for prescribed offences
    only (s 50). s 49 does not say whether the earlier conviction must be for the same offence,
    so that is asked as a fact. Asserted.

## What would need doing before this is worth anything

- The food regulations and orders under ss 2A, 2B, 46 and 56 were not deposited. Without them,
  most Part 3 offences turn on facts the seller cannot state without them.
- s 10L(fa) names the Food Safety and Security Act 2025; the paragraph was inserted with
  effect from 28 November 2025. That Act was not read, and its effect on this one is not known
  here.
- The "clear days" and "within N days" readings (ss 30, 33, 34, 45, 46) and the s 2F "but
  includes" reading are readings; no case law was searched.
- The independent test pass, the coverage table and the human gates were not done.
