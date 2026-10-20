# Electronic Transactions Act 1999 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**This is the Commonwealth Act.** Western Australia has its own Electronic Transactions Act 2011. It is deposited at
`subjects/au/wa/electronic-transactions-act-2011` and is **not encoded here**. Sections 8-15 of this Act work only "for the
purposes of a law of the Commonwealth". A requirement under a WA law, and the WA law of contract, belong to the WA Act.

**Edition:** Compilation No. 4 (register id C2026C00011), compilation date 5 December 2025, which includes amendments up to
Act No. 73, 2025. Deposited at `../../registers/source-bundle/C2004A00553.txt` (retrieved 13 October 2026).
The Electronic Transactions Regulations are **not deposited**. Two things they control are asked as inputs instead: whether
they exempt a law, transaction or matter (s 7A), and whether they require a particular data storage device (s 12(1)(b),
(2)(c), (4)(e)). The encoding cannot say which laws the regulations exempt.

**Checks:** one module (`eta-requirements.l4`, 13 exported questions) and one case file (`eta-cases-requirements.l4`).
39 assertions satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98. One deliberately wrong
expectation was put in a throwaway copy of the case file, and the check caught it (38 of 39).

There was no first-pass encoding of this Act.

## Seat

**The contracting party.** This is the person or business that wants to know whether a click, an email, a scan or an
electronic archive will do in place of paper and ink. In the WA lives that is Daniel, for his company Jarrah. The Act is
written in the third person ("a person is required to give information in writing"), and its conditions are ones that
person can state: how they sent it, whether the recipient agreed, what method identified them. So the exported questions
are the party's: "Can I meet the signature requirement electronically?", "When is my communication received?", "Am I bound
by a communication sent in my name?", "Can I withdraw my input error?".

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The regulations set no number, but they exempt
  laws and may require storage devices. They are not deposited, so both are inputs.
- **The actors the text names.** Followed: the person required to act, the Commonwealth entity, the person "neither a
  Commonwealth entity nor a person acting on behalf of" one, the originator, the addressee, the purported originator, the
  party running an automated message system.
- **A judgment handed to someone else is answered conditionally.** Followed. Three things are asked as facts: whether a
  signing method was "as reliable as appropriate for the purpose" (s 10(1)(b)(i)); whether a State law is "in terms
  substantially the same as" Part 2A (s 15A(2)(b)); and whether a proposal "clearly indicates" an intention to be bound
  (s 15B).
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed. Consent is worked out as "expressly or
  by conduct" (s 5(1)). The recipient's kind is asked as one of two values (Commonwealth entity or anyone else). Proper law,
  visa and citizenship matters are borrowed terms, asked as facts.
- **One case is the text's natural unit.** Followed: one requirement and what I did to meet it; one communication; one
  contract.
- **The Act's own terms, each with a plain gloss.** Followed in comments.
- **Operative sections in scope; machinery out.** Followed. Division 2 of Part 2, ss 14-15 and Part 2A are in.
  Commencement, the object, regulation-making and transitional provisions are out, except s 17(3), which decides whether
  Part 2A reaches a contract.

## The lives

- **Daniel, d045 (10 July 2031, aged 35): "Standard terms for the software: a liability cap, an unfair-terms review,
  electronic acceptance".** The question is "is a click acceptance?", and the scenario cites ss 9-10. The scenario names no
  customer, signing method or governing-law clause, so the encoder supplied them: a customer clicks "I agree" while logged
  in to Jarrah's portal, and the terms are governed by WA law. Decisions asked:
  - `Can I meet the signature requirement electronically`: no Commonwealth law requires Jarrah's customer terms to be
    signed, so the answer is "the Act does not apply". Whether a click forms the contract is the general law of contract.
    Where a Commonwealth law *does* require a signature, the same click meets it: it identifies the customer, shows their
    intention, and is reliable enough (taken as a fact), and Jarrah consented by setting the click up.
  - `Does Part 2A apply to my contract` and `Is the online proposal an offer`: the terms are governed by WA law, and WA has
    its own equivalent of Part 2A (asked as a fact), so Part 2A does not apply (s 15A(2)(b)).
  - Unfair terms and the consumer guarantees are the Competition and Consumer Act 2010's, not this Act's.

## Why this scope

The seat's question has three parts: does an electronic form satisfy a legal formality, when did my message take effect,
and what special rules govern a contract made online. Those are Division 2 of Part 2 (ss 9-12), Division 3 (ss 14-15) and
Part 2A. Places of dispatch and receipt (s 14B) are left out because no life event asks where a message was sent. The
permission limbs (ss 9(2), 11(2)) mirror the requirement limbs word for word, so only the requirement limbs are encoded.

## What the Act turns out to say

1. **The Commonwealth Act does not decide whether a click forms a contract.** ss 9-12 begin "If, under a law of the
   Commonwealth, …". A contract with no Commonwealth formality is outside Division 2 altogether. Asserted.
2. **Part 2A usually gives way to State law.** s 15A(2) applies Part 2A only where the contract's proper law is a State or
   Territory law **and** that State has no law "in terms substantially the same". By its table of contents, WA's 2011 Act
   has provisions on invitations to treat, automated message systems and input errors (encoder's inference). So for a
   WA-governed contract Part 2A is likely to be out. Asserted, on the input.
3. **Signature to a private party needs that party's consent, and consent can be inferred from conduct.** s 10(1)(d) and
   s 5(1). The party that sets up a click-through has consented to it. A typed name sent to someone who never agreed to take
   signatures that way does not meet the requirement. Asserted.
4. **Reliability has a second route.** s 10(1)(b)(ii): a method whose reliability is doubted still works if it is "proven
   in fact" to have identified the signer and shown their intention. Asserted.
5. **To a Commonwealth entity, its IT rules replace consent.** ss 9(1)(b)-(c), 10(1)(c), 11(1)(c)-(d): emailing something
   when the entity requires its own online service fails. Asserted.
6. **Migration and citizenship documents cannot be produced electronically under s 11.** s 11(5), Schedule 1. Asserted.
7. **Retaining an email means keeping its envelope too.** s 12(4)(c): the origin, destination, and sent and received times
   must be kept, not just the text. Asserted.
8. **Receipt at an address the addressee did not designate needs their awareness.** s 14A(1)(b): the later of its
   arriving and the addressee becoming aware of it. At a designated address it is received when it arrives, which is
   presumed to be when it can be retrieved (s 14A(2)). Asserted.
9. **A message that never leaves my system is dispatched only when received.** s 14(1)(b), as with a shared portal.
   Asserted.
10. **Someone who hacks my account does not bind me under s 15(1),** but agency law on actual or apparent authority is
    preserved (s 15(2)). Asserted.
11. **A web shop's "Buy" page is an invitation to treat** unless it "clearly indicates" an intention to be bound (s 15B).
    Asserted.
12. **The input-error right is narrow.** s 15D: it is lost if the system offered a chance to correct, if the error is not
    notified as soon as possible, or if a material benefit has been had. Even when it applies, the right "is not of itself a
    right to rescind" (s 15D(3)). Asserted.
13. **Two drafting remnants.** Schedule 1 cl 3 still refers to "section 13 (which deals with exemptions from Division 2 of
    Part 2)". The endnotes record s 13 as repealed by No. 33, 2011; s 7A now does that work. Schedule 1 cl 2(1)(b) runs from
    (ii) to (iv) after the 2025 amendment. Neither changes an answer.

## What would need doing before this is worth anything

- Deposit the Electronic Transactions Regulations and encode their exemptions, so that "is this law exempt?" stops being an
  input.
- Encode the WA Electronic Transactions Act 2011, the Act that actually governs Jarrah's WA-law contracts. Then decide, with
  a lawyer, whether it is "substantially the same" as Part 2A.
- Encode s 14B (place of dispatch and receipt) and s 15E if a life event turns on where a contract was made.
- Join this to the Competition and Consumer Act 2010 encoding, so that d045 gets one answer covering the click, the cap and
  the guarantees.
- An independent test pass and a human gate, as for any encoding.
