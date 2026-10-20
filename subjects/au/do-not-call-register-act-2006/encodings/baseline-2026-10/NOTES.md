# Do Not Call Register Act 2006 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**Edition:** Compilation No. 16, compilation date 1 September 2021, includes amendments up to Act No. 13, 2021 (register id
C2021C00356), as deposited at `../../registers/source-bundle/C2006A00088.txt` (retrieved 13 October 2026).
These are **not deposited**:

- the Do Not Call Register regulations. They could exclude kinds of call from "telemarketing call" (s 5(7)), add or carve
  out designated calls (Schedule 1 cll 2(c), 3(1)(d), 5), say when consent may or may not be inferred (Schedule 2 cl 5),
  and deem nominees (s 39(4));
- ACMA's s 18 determinations (form of application, removal from the Register);
- the value of a penalty unit (Crimes Act 1914 s 4AA).

Each carve-out the regulations could make is an input flag. Penalties are given in penalty units.

**Checks:** one module (`dnc-consumer.l4`, 12 exported questions), one case file (`dnc-cases-consumer.l4`). 45 assertions
satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98.

There was no earlier first-pass encoding of this Act.

## Seat

**The consumer called by telemarketers**, as the relevant account-holder of the number (or the account-holder's nominee):
Chloe, 21, getting marketing calls and asking whether she can stop them.

The Act's prohibitions fall on callers. Its Register is kept by the ACMA. But both exist for the person whose phone rings,
and the Act gives that person three things: the right to register, the protection of s 11, and the power to consent. Each
exported question is asked as that person would ask it: "Is my number eligible…", "Was this call to my number allowed…",
"What can I do…". The s 25 maximum penalties and the Schedule 3 infringement notice amounts are included as answers to
"what can the caller be made to pay?". That question is the consumer's too.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The regulations and determinations are not
  deposited, so every carve-out they could make is an input. Penalties stay in penalty units.
- **The actors the text names.** Followed: the relevant account-holder, the nominee, the ACMA, government bodies,
  registered charities, registered political parties, members, candidates, educational institutions, the court.
- **A judgment handed to someone else is answered conditionally.** Followed. These are inputs:
  - what "would be concluded" about a call's purpose (s 5(1); Schedule 1 cl 3);
  - whether consent "can reasonably be inferred" (Schedule 2 cl 2(b));
  - whether the caller made out a defence (s 11(3)-(6));
  - whether a court found a contravention and loss (s 30).
- **The Act's own definitions worked out; borrowed terms asked as facts.** Worked out: telemarketing call, designated
  telemarketing call, consent (with the 3-month rule and the published-number rule), relevant account-holder and nominee.
  Asked as facts: "Australian number" (it refers to the Telecommunications Act 1997 numbering plan), "registered charity"
  and "registered political party" (registrations under other Acts), and "emergency service number".
- **One case is the text's natural unit.** Followed: one call to one number.
- **The Act's own terms, each with a plain gloss.** Followed in the comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed. Out: the Register's administration (ss 13, 18), access by
  telemarketers and fees (ss 19-21), the contracted service provider (s 22), formal warnings and ACMA functions (ss 40,
  41), and Schedule 3's procedure. Where a provision addresses only the ACMA or the court (ss 24, 30, 34), the encoding
  answers what it means for the consumer: who may apply, and by when.

## The lives

- **chloe c044** (July 2024, 21): marketing calls and texts. "Can she stop them?"
  - *Is my number eligible for the Register?* Yes: a mobile used for private purposes (s 14(a)).
  - *May I apply?* Yes, as the account-holder (s 15).
  - *How long does registration last?* From entry, indefinitely, unless removed (s 17).
  - *Is it a telemarketing call?* The telco's sales call is. The text message is not, because it is not a voice call:
    texts are the Spam Act 2003.
  - *Does this Act reach the call, so that APP 7 gives way?* For the call, yes. For the text, not because of this Act.
  - *Was the call allowed?* Before she registered, yes. After registration, without her consent and with no exemption,
    it contravened s 11(1).
  - *What can I do?* No application of her own: only the ACMA may seek a penalty or injunction. She may seek compensation
    for loss under s 30 once a court has found the contravention, within 6 years.

  The scenario gives no dates, callers or registration day. Those used here (registered 2 July 2024; a sales call on
  20 August 2024) are the encoder's.

## Why this scope

The plan entry names s 11. The seat's question, "Can I stop the calls?", needs:

- the Register side (ss 14, 15, 17, 39);
- what counts as a telemarketing call (s 5);
- the exemptions (Schedule 1);
- consent (Schedule 2);
- the remedies (ss 24, 30, 34) and what the caller faces (s 25, Schedule 3 cl 4).

Faxes (Part 2A, Schedule 1A) mirror the call rules, but no one in the lives sends or receives a marketing fax, so they are
left out. Section 12 is the caller's duty to put compliance clauses in call-centre contracts and is no question of the
consumer's. Schedule 1 cl 4(2) (an institution calling an employer about an employee's household number) is left out.
The consumer is the account-holder of a private number, so cl 4(1) is the limb that applies.

**Consistency with the Privacy Act baseline.** That encoding asks, as a fact under APP 7.8, whether "the Do Not Call
Register Act or Spam Act applies". `Does this Act reach the call` is that fact for a call: true for a telemarketing call
(s 5). The two encodings then agree on Chloe's c044 call: APP 7 does not reach it, and her protection is s 11. Neither
encoding decides the text message: that belongs to the Spam Act 2003, which has its own baseline (subjects/au/spam-act-2003); the two are listed together in docs/au-baseline-links.md.

## What the Act turns out to say

1. **Registration never lapses on its own.** s 17(1)(b): it "remains in force indefinitely" unless removed under an ACMA
   determination. A removed number may be re-registered (s 17(3)). Asserted (in force 30 years on; out of force from the
   day of removal; back in force on re-registration).
2. **Only private, fax-only, government or emergency numbers qualify.** s 14. A tradesperson's mobile used mainly for the
   business is not eligible. Asserted.
3. **Anyone the account-holder nominates in writing may register, and nobody else.** s 15(a), s 39(1), (2). A flatmate
   never nominated may not. Asserted.
4. **Texts are not covered.** s 5(1) requires "a voice call". A recorded or synthetic voice counts (s 4), but a text
   message does not. Asserted.
5. **Research is not exempt by name; it is simply outside s 5 if nothing is sold or sought.** The Act names no research
   or survey exemption. A call with none of the s 5(1)(e)-(o) purposes is not a telemarketing call. A call that also sells
   or solicits is not saved by being a survey. Whether the regulations exclude some research calls is an input (s 5(7)).
   Asserted for the pure survey call.
6. **Exempt callers are exempt only for their own goods and services.** Schedule 1 cl 2(b): a charity or government body
   is exempt only "if the call relates to goods or services" it supplies. A charity selling another firm's energy plans
   is not exempt. Asserted.
7. **Political callers are exempt only when fund-raising.** Schedule 1 cl 3: the purpose must be "fund-raising for
   electoral purposes" or "for political purposes". A party selling merchandise without fund-raising is not exempt.
   Asserted. (The encoder reads a call with any fund-raising purpose as qualifying: "the purpose, or one of the purposes".)
8. **My school or university may call, but only about what it supplies, and only if I or my household studied there.**
   Schedule 1 cl 4(1). Asserted.
9. **Businesses with an existing relationship are not exempt as such.** The Act has no customer exemption. A relationship
   matters only if consent "can reasonably be inferred" from "the conduct" and "the business and other relationships"
   (Schedule 2 cl 2(b)). That is a judgment, taken as an input. Consent is never inferred from "the mere fact that the
   number has been published" (cl 4). Asserted.
10. **Express consent with no period stated lasts 3 months.** Schedule 2 cl 3. Consent given on 15 May 2024 still holds
    on 14 August and is gone on 15 August (on the encoder's reading of "the period of 3 months beginning on"). Asserted.
11. **The consumer cannot sue.** A civil penalty order (s 24(1)) and an injunction (s 34) are made only "on the
    application of the ACMA". The victim may apply only for compensation (s 30(1)), and only once a court, "in one or more
    proceedings under section 24", has found a contravention. The application must be within 6 years (s 30(4)). The
    court may count the victim's expenses and the effect of "dealing with the calls" (s 30(2)). Complaints to the ACMA
    are made under the Telecommunications Act 1997, not this Act. Asserted.
12. **The caller's defences are real exits.** A number washed against the Register in the 30 days before the call, a
    reasonable mistake of fact, or reasonable precautions and due diligence each take the call out of s 11(1)
    (s 11(3)-(5)). The caller bears an evidential burden (s 11(6)). Asserted (defence as an input).
13. **One call can cost a company 100 penalty units, and an infringement notice 20 a call, capped at 1,000.** s 25(3)-(6):
    the maxima are 100 for a company and 20 for anyone else, or 500 and 100 with a prior record. Schedule 3 cl 4: 20 per
    call to a company up to 49 calls (980), then 1,000 flat at 50 or more. For other callers it is 4 per call, then 200.
    Asserted.

## What would need doing before this is worth anything

- Deposit the Do Not Call Register regulations (excluded calls, regulation-designated calls, inferred-consent rules,
  deemed nominees) and ACMA's s 18 determinations (removal from the Register). Then replace the input flags with the
  rules.
- Deposit the Crimes Act 1914 s 4AA penalty-unit value to give the penalties in dollars.
- Encode the Spam Act 2003 (ss 16, 18). Chloe's texts are there, and the APP 7.8 bridge needs it as much as this Act.
- Encode the Telecommunications Act 1997 complaint route to the ACMA: in practice it is what the consumer does.
- Add marketing faxes (Part 2A, Schedule 1A) and Schedule 1 cl 4(2) if a life needs them.
- Have someone other than the encoder test it, and take it through the human gates.
