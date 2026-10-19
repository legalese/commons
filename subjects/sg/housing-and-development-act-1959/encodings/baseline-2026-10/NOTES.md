# Housing and Development Act 1959 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`: a case the encoding does
not reach returns `not covered by this encoding` or `NOTHING`, with a comment saying why. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This encoding replaces the one moved to `solutions/Litigate.4/sg/housing-and-development-act-1959/` on 19 October 2026. That
encoding's notes were read for scope and pitfalls; none of its L4 was copied.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 15 July 2026, as deposited at
`../../registers/source-bundle/HDA1959.txt` (retrieved 1 October 2026).

**Checks:** one module (`hda-flats.l4`) and one case file (`hda-cases-flats.l4`): 59 assertions, all satisfied, with 0 errors
and 0 warnings on the stable `l4` of VS Code extension 1.6.98. The case file is built by
`gen_housing-and-development-act-1959_baseline.py` in the session scratchpad. Its expected values were worked out by hand from the text.

## Seat

**The owner of an HDB flat, or a person applying to buy one from the Board.** For s 59 and s 80(2) the seat is the
personal representative, spouse or beneficiary of an owner who has died. Part 4 of the Act is about the person who buys,
lives in, deals with and can lose a Board flat. Almost every provision there is phrased as a power of the Board ("the
Board may re-enter", "may compulsorily acquire"), so each one is turned round to ask what can be done to that person
and by when: `Can the Board re-enter my flat and end my lease`, `What is the last day I can object to the acquisition`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers brought in.** Followed as far as the deposit allows. The rules
  made under s 74 are not deposited. These include the minimum occupation period, the eligibility conditions, the weighting
  of votes and the financial-penalty rules. Where the Act defers to them, the answer is an input, and the encoding says so.
- **The actors the text names.** Followed: the Board, the Minister, the owner, the spouse, the authorised occupier, the
  personal representatives.
- **A judgment handed to someone else, answered conditionally.** Followed. "In the opinion of the Board" (ss 62(1)(e),
  63(1)(a), (i)), the Minister's higher value (s 63(2)), the Minister's exemption (s 63(10)), the Board's exemption
  (s 50(10)) and the Minister's approval of upgrading (s 77) are all inputs.
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.** Partly followed. "Protected property"
  and "approved financial institution" (s 58(12)) are worked out. "Authorised occupier" (s 2) is used in the facts, not
  derived. "Representation", "abatement offence" and "exclusion offence" (offences under the Community Disputes Resolution
  Act 2015), and the "appointed date" are asked as facts. The appointed date is the commencement of a 2024 amending Act and
  is not in the deposit.
- **One case is the text's natural unit.** Followed: one flat, with one application, one sale agreement, one notice and
  one death.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **The operative sections in scope, the machinery out.** Followed: Parts 2, 3, 5 and 6 are left out. Within Part 4 the
  provisions are those the owner most meets; see the next section.

## Why this scope

The Act is large: the Board's machinery, the upgrading Part 4A and the design-build-and-sell Part 4B. The
owner meets it mostly at these points:

- buying (s 50);
- selling and dealing (ss 55, 56);
- borrowing and debt (s 58);
- death (s 59);
- losing the flat (ss 62, 63, with the timetable in ss 63(5), (7), 66, 68 and 69);
- two offences aimed at owners (ss 70, 72);
- the financial penalty in place of losing the flat (s 74(1)(i)-(k));
- upgrading (ss 77, 80, 82).

**Not encoded:**

- ss 49, 51-54, 57, 60, 61 and 71;
- ss 64 and 65 (search and examination);
- s 67 (compensation);
- s 73;
- s 59(4) (rescission);
- the rest of Part 4A;
- Part 4B;
- everything outside Parts 4 and 4A.

## What the Act turns out to say

1. **The bar on buying reaches the whole household and runs on after the application.** Under s 50(1) a person may not buy
   if the person, the spouse or any authorised occupier owns other property. It also applies if any of them sold or
   divested property in the 30 months before applying, or between applying and completion. A sale exactly 30 months before
   is read as inside the window. The Board may exempt (s 50(10)). Asserted.
2. **An application can be cancelled for an innocent misstatement.** Under s 50(12)(a) a material misrepresentation or false
   statement made "whether innocently or otherwise" is enough. Asserted.
3. **A sale agreed inside the minimum occupation period without consent is void, and so is one on the wrong form.**
   Under s 55(3) both are void, but only for agreements made on or after 20 November 1998. The period itself is set by rules
   that are not deposited. Asserted.
4. **The flat cannot be pledged except to the Board, a licensed bank, finance company, direct insurer or merchant bank, or a
   prescribed person.** Any other agreement to use it, or its sale proceeds, as security is void (s 58(1), (4), (12)).
   Asserted.
5. **Bankruptcy and judgment creditors cannot reach the flat, unless no owner is a Singapore citizen.** Under s 58(6) the
   flat does not vest in the Official Assignee. Under s 58(7) it cannot be attached except by a mortgagee whose mortgage had
   the Board's consent, or by a statutory chargee. Both protections fall away when the sole owner, or every owner, is not a
   citizen (s 58(8)). A flat owned only by permanent residents is not protected. Asserted.
6. **No one can claim the flat under a resulting or constructive trust.** An express trust needs the Board's prior written
   approval (s 58(9)-(11)). Asserted.
7. **A late grant of probate does not undo s 59(3)(a).** The limb is "no representation has been taken out ... within 12
   months from the death". Read literally, it stays met when a grant is taken out after the 12 months. This is a reading:
   the Act does not say that a late grant cures it. Asserted.
8. **Owning a small shop does not cost the owner the flat.** Under s 63(2), s 63(1)(b) (acquiring other property) does not
   apply to commercial property bought with the Board's consent and used for business, if its value is not over $250,000
   or a higher value the Minister allows. Asserted.
9. **The acquisition timetable has a gap.** s 66(1)(a) lets the Board lodge the vesting instrument in two cases: 28 days
   after the notice where no objection was made, or after an appeal to the Minister is determined or withdrawn. It says
   nothing about an owner who objected and then did not appeal. The encoding returns `not covered by this encoding` for
   that case. Asserted.
10. **"Until the expiry of N days after service" is counted as service + N + 1.** This applies to ss 50(3A), 59(5A),
    66(1)(a)(i) and 68(1). The appeal and objection deadlines ("within N days after service") are counted as service + N.
    Both are readings about counting; the Act states no rule. Asserted.
11. **A financial penalty instead of losing the flat is capped at $50,000.** This applies only to breaches on or after 20
    July 2015 (s 74(1)(i)-(k)). The rules that actually confer the power are not deposited, so this is the Act's ceiling,
    not an amount. Asserted.
12. **Upgrading goes ahead on 75% of the value in votes, with the Minister's approval** (s 77(4), (9)). An unpaid
    improvement contribution becomes a charge on the flat 3 months after the demand (s 82(1)). A deceased owner's spouse,
    or a beneficiary aged 21 or over, can be made to pay it if the estate is not being administered (s 80(2)). Asserted.
13. **The offences are modest.** Giving the Board false information carries a fine of up to $5,000, up to 6 months'
    imprisonment, or both (s 70). Failing to remove a dangerous article from a window or balcony carries a fine of up to
    $2,000, plus $100 a day while it continues after conviction (s 72), with no imprisonment. Asserted.

## What would need doing before this is worth anything

- **The rules under s 74 are needed.** These cover the minimum occupation period, eligibility, poll weighting and the
  financial-penalty rules. Without them, several answers rest on facts the owner cannot easily state.
- **The month arithmetic does not handle month-ends.** A month is counted by keeping the day of the month, so a day that
  does not exist in the target month (for example, 31 August plus 6 months) rolls into the next month. No case tests it.
- **Some limbs are merged.** s 63(1)(f), (g) and (ga) are one fact, and so is the 3-month count in s 63(1)(k).
- **Some provisions are left out.** s 59(4) rescission, the s 69 disposal of belongings beyond its minimum period, and
  compensation (ss 63(9), 67) are not encoded.
- **No case law was searched,** and no HDB practice was consulted.
- **The readings need review.** The counting readings (finding 10) and the s 59(3)(a) reading (finding 7) should be
  reviewed by someone who knows the Board's practice.
