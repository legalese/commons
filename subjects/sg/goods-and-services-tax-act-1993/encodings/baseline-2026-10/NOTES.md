# Goods and Services Tax Act 1993 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the Act is applied, with the design defaults
ruled on 2026-10-18. No pipeline, no coverage table, no independent test pass, no human gate.
No `REFUSE`. Where the encoding has no answer, a decision returns `NOTHING` and its comment
says why. Not for public use as advice.

This encoding replaces two others:

- the encoding moved to `solutions` (Litigate.4, `legalese-aswathy`) on 2026-10-19. Its
  NOTES.md was read for scope and known pitfalls, but none of its L4 was copied;
- the first-pass encoding `naive-2026-10`. Everything it covered is covered here: s 8, s 16,
  s 17(2), s 40, First Schedule paras 1, 1A and 4, and Fourth Schedule Part 1. Its
  hand-checked values are reused where they are still right ($109 at 9%, $1,070 to $1,080,
  exactly $1 million, 1 March). Two are corrected (findings 3 and 9).

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
11 September 2026 (the last amendment listed is S 590/2026). It is deposited at
`../../registers/source-bundle/GSTA1993.txt`. The first-pass encoding gave its edition as
"amendments to Act 35 of 2022 and S 109/2023". The deposited text also carries S 443/2025
(in force 1 July 2025), which changed the registration date on the forward-looking test.

**Checks:** two modules (`gst-charge.l4`, `gst-obligations.l4`) and two case files
(`gst-cases-charge.l4` with 30 assertions, `gst-cases-obligations.l4` with 29). The case files
are built by the scratchpad generator `gen_goods-and-services-tax-act-1993_baseline.py`, with
expected values written by hand from the text. 59 assertions satisfied, 0 errors, 0 warnings,
on the stable `l4` from VS Code extension 1.6.98. To show the check can fail, a copy with one
expected value changed (1080 to 1079) was run: 29 satisfied, 1 error.

## Seat

**The individual who makes, or proposes to make, supplies of goods or services in the
course of a business in Singapore: a sole proprietor or a partner.** The Act lays the tax on
"the person making the supply" (s 8(3)). It makes that person register (First Schedule),
account for the tax and pay it (s 19), and pay the penalties (Part 9). The customer pays GST
only through the price and has almost no duties under the Act. So the person the Act is
applied to is the trader. That trader asks: is GST charged on what I sell, at what rate, and
how much of my price is tax? What may I charge when the rate changes? Must I register, by
when, and from when am I registered? What do I pay for a period? What does lateness or a
wrong return cost me? Companies come under the same provisions, but they are not the seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The Act
  sets its own rates (s 16), thresholds (First Schedule) and penalty amounts. The regulations
  under s 41, which fix accounting periods and when returns and payments are due, were not
  deposited. So the due date, the months of lateness and the allowable input tax are inputs.
- **The actors the text names.** Followed: the Comptroller, and the court where it convicts.
- **Someone else's judgment answered conditionally.** Followed. These are all inputs, never
  guessed:
  - "the Comptroller is satisfied" (paras 1(3)(b) and 1A(3));
  - "reasonable grounds for believing" (para 1(1)(b));
  - "if the Comptroller thinks fit" (para 5(3) and (4));
  - an agreed earlier date (paras 4(2)(b) and 5(2)(b));
  - an extension of time (s 49(2));
  - which limb of ss 59 and 62 the court found.
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.**
  Followed, with stated exceptions. Worked out from facts:
  - "taxable person" (s 8(2));
  - "taxable supply" (s 8(2A)(a), with s 21(2)(b));
  - "supply" (s 10(2)(a));
  - "exempt supply" (s 22(1) and the Fourth Schedule entries listed);
  - "input tax" with apportionment (s 19(3), (4));
  - the registration value, including capital assets disregarded (para 1C(2)) and values
    before GST (para 16).

  **Departure:** four of the Act's own terms are asked as facts. They are "international
  services" (s 21(3), several pages of descriptions), "belongs in Singapore" (s 15), place of
  supply (s 13) and the Second Schedule's deemed supplies. Each needs an encoding of its own,
  and each is a yes or no the trader can usually answer.
- **One case is the text's natural unit.** Followed, with one unit per question. A supply
  answers the charge questions. A calendar year answers retrospective registration. A day X
  answers the forward test. A prescribed accounting period answers what is paid. One late
  payment, return or wrong return answers the penalty questions.
- **The Act's own terms, each with a plain gloss.** Followed, in comments beside each type
  and field. "Outside the scope of GST" is this encoding's gloss for a supply on which s 8(1)
  charges nothing, and it says so.
- **Operative sections in, machinery out.** Followed. Part 2 (administration), the Board of
  Review (s 50 onward), regulation-making and order-making powers, and the transitional
  provisions are out. **Departure:** many operative provisions are also left out, because
  the Act is very large (sections numbered to 94, and ten Schedules) and the case budget is 25 to 60
  assertions. They are listed under "Why this scope".

## Why this scope

The seat decides it. The encoding takes what a sole trader or partner meets most, in the
order they meet it:

- **The charge.** Is GST charged on what I supply, and is it standard-rated, zero-rated,
  exempt or outside the scope (ss 8, 10, 21, 22, Fourth Schedule)?
- **Timing and rate.** When does my supply take place (s 11(2)), and what is the rate that day
  (s 16)?
- **The price.** How much of my price is GST (s 17(2))? What may I charge when the rate rises
  after I have contracted (s 40)?
- **The period.** How much of the GST I paid counts as input tax (s 19(4))? Do I pay, or get
  money back (s 19(2), (5))?
- **Registration.** Am I liable to be registered (paras 1, 1A, 1C)? By when must I notify, and
  from when am I registered (paras 4, 5)? By when must I report that I have stopped (para 10)?
- **Disputes and penalties.** By when must I object (s 49(2))? What do a late payment, a late
  return, failing to register and an incorrect return cost me (ss 59 to 62)?

Left out, each a candidate for a later encoding:

- Seventh Schedule and marketplace supplies (s 8(1A));
- importation;
- the reverse charge (s 14) and belonging (s 15);
- the exceptions to the time of supply (ss 11(3) to 12A);
- open market value;
- the s 20 attribution rules;
- reliefs (ss 21A to 27A);
- the Part 6 special cases (groups, partnerships, agents, going concerns, vouchers);
- the Part 6A transitional splits when a rate changes (ss 39A to 39F);
- assessment and records (ss 43 to 48);
- the Board of Review and appeals;
- offences other than ss 59 to 62(1);
- recovery;
- voluntary registration, cancellation and exemption from registration (paras 8, 9, 12 to
  15);
- transfers of a going concern (para 6).

The para 4(1A) duty to notify is also written as a regulative rule, `my duty to notify after
a calendar year in which I passed $1 million`. It checks, but it is not traced.

## What the Act turns out to say

1. **No consideration, no supply, unless the Second Schedule says otherwise.** Under
   s 10(2)(a), a "supply" excludes "anything done otherwise than for a consideration", subject
   to the Second Schedule. Free samples are outside the scope. Goods given away that the
   Second Schedule treats as supplied are standard-rated. The moved encoding hit the same
   point (its deemed-supply fix). Asserted.
2. **Zero-rated is not exempt.** Under s 21(2), a zero-rated supply carries "no tax" but "is in
   all other respects treated as a taxable supply". It therefore counts towards registration
   and supports input tax. An exempt supply does neither. An export is a taxable supply; a
   flat let is not. Asserted.
3. **The Act as deposited states no rate before 2003.** Section 16 begins at 4% for 2003,
   and the deposited text gives no earlier rate. The first-pass encoding returned 0% before 2003. That
   asserts a rate the Act does not give, so this encoding returns `NOTHING`. The boundaries
   at 30 June 2007, 31 December 2023 and 1 January 2024 are asserted. Asserted.
4. **The price contains the tax.** Under s 17(2), the value is the amount which, "with the
   addition of the tax chargeable, is equal to the consideration". So $109 at 9% has a value
   of $100, and $1,080 at 8% contains $80 of GST. Asserted.
5. **When the rate rises, the supplier may add the increase. When it falls, the supplier may
   deduct the reduction, and is not told it must.** Both limbs of s 40(1) say "may". A $1,070
   price agreed at 7% may become $1,080 if supplied at 8%. It stays $1,070 if the contract
   expressly excludes the change or the change "has been taken into account". After a fall,
   the most the supplier may charge is still the agreed price. That is this encoding's
   reading of "may deduct"; whether a customer can insist on the deduction is not answered
   by the Act's words. Asserted.
6. **The time of supply is the earlier of invoice and payment.** Under s 11(2), a December 2022
   deposit fixes the time of supply in December 2022 (the 7% period), even if the invoice is
   dated January 2023. Where neither has happened, s 11(2) fixes no time, and the answer is
   `NOTHING`. Asserted.
7. **Input tax is apportioned, and an excess is paid back.** Under s 19(4), only the business
   share of GST on a purchase counts. Under s 19(5), if the credit exceeds the output tax,
   "the amount of the excess must be paid to the taxable person". Asserted.
8. **Registration turns on "exceeded" $1 million, after setting aside capital assets.**
   - Exactly $1 million is not enough (para 1(1)(a)(ii)).
   - Selling the business premises does not count (para 1C(2)): $1.2 million that includes a
     $300,000 premises sale is $900,000 for this test.
   - A trader who belongs in Singapore adds their Seventh Schedule supplies (para 1(1)(a)(ii)(B)).
   - The Comptroller being satisfied that next year will stay under $1 million takes the
     liability away (para 1(3)(b)).

   Asserted.
9. **Registration happens whether or not you notify, and the forward-test date changed on
   1 July 2025.**
   - **Retrospective test.** Notice is due within 30 days of the year end, so 30 January.
     Registration runs from the day after the end of the following month, so 1 March
     (para 4(2)). The first-pass encoding had the same date.
   - **Forward test, day X before 1 July 2025.** Registration runs from "the day immediately
     after the end of the 30 days", so 10 March 2025 gives 10 April 2025.
   - **Forward test, day X on or after 1 July 2025.** Registration runs from the same day two
     months later, or the last day of that month (S 443/2025). So 15 August 2025 gives
     15 October 2025, and 31 December 2025 gives 28 February 2026. The Comptroller "may, if
     the Comptroller thinks fit", register from day X itself.

   The first-pass encoding did not cover the forward-test date. Asserted.
10. **An overseas seller of Seventh Schedule supplies needs both thresholds.** Under para 1A,
    that means worldwide supplies over $1 million **and** Seventh Schedule supplies over
    $100,000. Asserted.
11. **Late payment costs 5%, then 2% a month counted from the due date, capped at 50%.**
    Section 60(1)(b) applies the 2% only if the tax is not paid within 60 days after the 5%
    penalty. But it counts each completed month "commencing from the date on which the tax
    became payable", not from the end of the 60 days. On $10,000 unpaid for 3 completed
    months, the penalty is $500 plus $600. After 30 months, the 2% is capped at $5,000. This
    is the moved encoding's open question F3, read the same way. Asserted.
12. **A late return costs $200 plus $200 a completed month, to $10,000** (s 60(2)). That cap
    is reached after 49 completed months. Asserted.
13. **Failing to register costs 10% of the tax due, plus a fine of up to $10,000 and $50 a
    day after conviction** (s 61). Asserted.
14. **The penalty for a wrong return scales with fault: one times the tax, two times, or three
    times.**
    - Section 59(1) charges one times the tax undercharged, with no fine or imprisonment.
    - Section 59(2) (no reasonable excuse, or negligence) doubles it, with up to $5,000 or
      3 years.
    - Section 62(1) (wilful intent to evade) triples it, with up to $10,000 or 7 years.
    - Under s 62(2), a proved false entry is presumed made with intent to evade "until the
      contrary is proved".

    Asserted (the presumption is a comment, not asserted).
15. **Smaller points worth recording.**
    - Section 49(2) gives 30 days from being notified of a decision to object, and the
      objection must "state precisely the grounds". Asserted.
    - Para 10 gives 30 days to report stopping. Asserted.
    - A life insurance contract is exempt (para 1(l)), but motor insurance is not listed.
      Renting a shop is not exempt; renting a flat is. A coin sold as a collector's item is
      carved out of the currency-exchange exemption. Only the life insurance and the two
      lettings are asserted.
16. **A tension left open.** Section 21(2) zero-rates a supply "whether or not tax would be
    chargeable on the supply apart from this section". But First Schedule para 8(1)(a)(ii)
    still calls financial services that are international services "exempt supplies". This
    encoding lets zero-rating win where a Fourth Schedule supply is also exported or
    international services. That is an inference, and no case asserts it.

## What would need doing before this is worth anything

- **The missing sections.**
  - The s 41 regulations, for accounting periods and due dates, and the s 20 regulations, for
    which input tax is allowable.
  - Section 21(3) (international services), s 13 (place of supply) and s 15 (belonging),
    which are asked here as facts.
  - The Second Schedule, which settles which free transfers are supplies.
  - The Part 6A rules on supplies that span a rate change. Without them, s 16 and s 40
    cannot be applied to a real invoice that straddles 1 January 2023 or 1 January 2024.
- **The registration paths not covered.** Voluntary registration and its 2-year minimum, and
  cancellation.
- **Reading and review.** The Comptroller's e-Tax Guides and decided cases were not
  retrieved. Readings 5 and 16 want a lawyer's view.
- **A coverage table and an independent test pass** before any of this is relied on.
