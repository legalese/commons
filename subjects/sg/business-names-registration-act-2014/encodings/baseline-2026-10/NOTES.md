# Business Names Registration Act 2014 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the Act is applied, with the design defaults
ruled on 2026-10-18. No pipeline, no coverage table, no independent test pass, no human gate.
No `REFUSE`: where the encoding has no answer, a decision returns `NOTHING` and its comment
says why. Not for public use as advice.

This encoding replaces the one moved to `solutions` (Litigate.4) on 2026-10-19. That
encoding's NOTES.md was read for scope and known pitfalls. Its L4 was not copied.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 9 June 2025
(SSO "Current version as at 01 Oct 2026"), as deposited at
`../../registers/source-bundle/BNRA2014-2026-10-01.txt`.

**Checks:** one module (`bnra-registration.l4`) and one case file
(`bnra-cases-registration.l4`, built by the scratchpad generator
`gen_business-names-registration-act-2014_baseline.py` with expected values written by hand
from the text). 60 assertions satisfied, 0 errors, 0 warnings, on the stable `l4` from VS Code
extension 1.6.98. To show the check can fail, a copy with one expected value changed
(5000 to 4999) was run: 59 satisfied, 1 error.

## Seat

**The individual who carries on, or proposes to carry on, business in Singapore, as an
individual proprietor (sole proprietor) or as a partner of a firm.** The Act is addressed to
"a person" who carries on business. Most of the people it reaches are sole traders and
partners, and they are the ones who have to answer its questions themselves: must I register,
can I have this name, must I appoint someone, what must I tell the Registrar and by when,
what can I appeal, and what can I be fined. Companies, LLPs, foreign companies and statutory
bodies come in only where they bear on that person, for example as the earlier holder of a
name the person wants.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. No
  regulations under s 43 were deposited. So what they would settle is asked as a fact: who is
  exempted (s 4(1)(p)), which professions lose the s 4(1)(c) exemption (s 4(2)), and whether an
  offence is compoundable (s 37(1)). Fees are not encoded.
- **The actors the text names.** Followed: the Registrar, the Minister, the Minister for
  internal security (by certificate), the CPF Board, the General Division of the High Court and
  the Official Assignee.
- **Someone else's judgment answered conditionally.** Followed. "The Registrar is satisfied",
  "in the Registrar's opinion", "the Minister consents", "the Registrar allows longer in
  special circumstances" and "the court may infer" are all inputs, never guessed.
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.**
  Followed. "Business" (for gain, not an office, employment or occupation), "carrying on
  business in Singapore" (s 2(2)), "full name" (compared with the business name), "resides
  outside Singapore" (s 11(14), for individuals and corporate partners) and the authorised
  representative's qualifications (s 11(2)) are worked out. Borrowed terms are asked: a
  profession under another written law, the First Schedule to the old Business Registration
  Act, a "registered corporate service provider", and an undischarged bankrupt.
- **One case is the text's natural unit.** Followed: one business carried on under one
  business name (s 5(2) requires one registration for each name).
- **The Act's own terms, each with a plain gloss.** Followed, in comments beside each type and
  field.
- **Operative sections in, machinery out.** Followed: s 3 (administration), s 38 (records) and
  s 43 (regulations) are out. **Departure:** the rectification, copies, inspection, information,
  enforcement-order, bodies-corporate, service and transitional provisions (ss 25 to 33, 39,
  40, 42, 45) are also left out, though some are operative. That keeps the encoding within its
  size, and they are the provisions the individual meets least.

## Why this scope

The seat decides it. The encoding takes the questions a sole trader or partner asks, in the
order they meet them. Do I need to register (ss 2, 4, 5)? Who may file (s 6(3))? Will the name
be refused (ss 9, 17)? How long does a reservation last (s 16(4))? Must I appoint an authorised
representative (s 11)? What notices must I lodge, and within how many days (ss 11, 19, 20, 22)?
What can I appeal (ss 8(7), 12(4), 13, 16(5), 17(9))? Can I restore a registration (ss 14(4),
24)? Am I committing an offence, and what is the most it can cost (ss 34 to 37)? Section 2(3)
(when a foreign company is not carrying on business here) and s 4(1)(e) to (o) (bodies and
corporations) are outside the seat.

Two decisions are in the module but not asserted, to keep within the case budget: the s 36
presumption and the days allowed to appoint an authorised representative (s 11(3), (4), (11)).
The s 22(1) duty is also written as a regulative rule, `my duty to give notice that I stopped`.
It checks, but it is not traced.

## What the Act turns out to say

1. **Trading under your own full name, and nothing else, needs no registration.** Under
   s 4(1)(a) a sole proprietor is exempt only if the business name is "only" their full name.
   That means the name on their latest identity card, or on their passport if they are not
   registered under the National Registration Act (s 2(1)). "Tan Ah Kow" is exempt. "Tan Ah Kow
   Trading" must be registered. Under s 4(1)(b), a firm trading under all its partners' full
   names is exempt only if every partner is an individual: one corporate partner removes the
   exemption. Asserted.
2. **An exempt individual may still choose to register.** Under s 4(3), the only people barred
   from choosing are those in s 4(1)(e) to (o), and none of them is an individual trader. A
   person who chooses to register is then bound by the Act while registered (s 4(4), which is
   not encoded). Asserted.
3. **A salary is not a business, and neither is activity not for gain.** "Business" excludes
   "any office, employment or occupation" and needs gain. Having a place of business in
   Singapore makes a person "treated as" carrying on business there (s 2(2)). This encoding
   reads that as a sufficient condition, not the only one, so an online seller with no premises
   can still be carrying on business here. That reading is an inference. Asserted.
4. **The Minister's consent cures a bad name but not a bad business.** Section 17(1) and (2)
   bars apply "except with the Minister's consent". Section 9 applies "Despite any provision in
   this Act or any other written law", so no consent overrides a refusal for unlawful purpose
   or national security. Asserted.
5. **Waiting periods for a name an earlier holder used run from 3 months to 6 years.** The
   periods are one year after a business name is cancelled or ceases, 2 years after a wound-up
   company, and 6 years after a company is struck off (s 17(2)). Under s 17(3), the name of a
   foreign company that ceased business here opens after 3 months, but only at the
   Registrar's choice ("may"). A live registered name is barred with no end date. Asserted.
6. **Some cancellations cannot be appealed.** Appeals to the Minister lie within 30 days
   against a refusal to register or renew (s 8(7)), a cancellation under s 12 (s 12(4), plus any
   further period the Minister allows), a refusal to reserve or extend (s 16(5)), and a
   direction to change name (s 17(9)). No appeal is given in s 14 (failure to renew), s 17(8)
   (not obeying a direction) or s 23 (not carrying on business). There is no appeal at all
   where the refusal or cancellation rests on an internal-security certificate (s 13(2), (3)).
   Asserted.
7. **Living abroad triggers the authorised-representative duty.** An individual resides
   outside Singapore if their residential address is outside it. A corporation does if it was
   incorporated outside it (s 11(14)). A firm needs a representative only if *all* its partners
   reside outside, so one Singapore company partner is enough to avoid it. The representative
   must be at least 18, a natural person, of full capacity and ordinarily resident here
   (s 11(2)). Asserted.
8. **Most notices are due within 14 days, with two exceptions.** No notice is needed for a new
   residential address already reported under s 10 of the National Registration Act (s 19(2)).
   A new business name goes by application under s 18, not by notice (s 20(2)(b)). The s 20(1)
   period can be extended by the Registrar. Asserted.
9. **An expired registration is still a registration.** Under s 14(4) it continues until
   cancelled. Restoration (s 24) is open within 12 months, or longer in special circumstances,
   but only after cancellation under s 12(2), 14 or 23, or cessation under s 22. A
   cancellation under s 12(1) or s 17(8) cannot be restored. The encoding reads "within 12
   months" as fewer than 12 whole months, which is an inference. Asserted.
10. **Trading unregistered can cost $10,000 or 2 years, and composition is capped at $5,000.**
    Under s 35(1), trading unregistered, or under a name other than the registered one, is
    punishable by a fine up to $10,000, up to 2 years, or both. Not notifying that business
    has stopped carries a fine only, up to $5,000 (s 22(3)). Missing a duty about an
    authorised representative carries up to $1,000 (s 11(12)). Composition is the lower of
    half the maximum fine and $5,000 (s 37(1)), and only for offences prescribed as
    compoundable. Asserted.

## What would need doing before this is worth anything

- The regulations under s 43 should be deposited and read. Until then, exemptions,
  professions taken out of s 4(1)(c), and compoundable offences are bare inputs, and no fee is
  known.
- Waiting periods and the restoration window are counted in whole months, not days. The
  anniversary boundary is not modelled.
- The particulars of an application (s 6(1)(b)) and the provisions left out under "Seat" are
  not encoded.
- No case law, ACRA guidance or independent test pass was used, and no Singapore lawyer has
  read the encoding against the text.
