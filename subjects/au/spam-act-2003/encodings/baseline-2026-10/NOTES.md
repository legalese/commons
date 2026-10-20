# Spam Act 2003 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**Edition:** the compilation with register id C2016C00614 (the latest amendment listed in its endnotes is of 11 February
2016), as deposited at `../../registers/source-bundle/C2004A01214.txt` (retrieved 13 October 2026).
The Spam Regulations 2021 are **not deposited**. They can add a commercial purpose (s 6(1)(p)), exclude messages (s 6(7)),
add conditions to sender information and unsubscribe addresses (ss 17(1)(c), 18(1)(g)) and to factual messages (Sch 1
cl 2(1)(c)), designate further messages (Sch 1 cl 5), and say when consent may or may not be inferred (Sch 2 cl 5). The
encoding answers as if they added nothing. The dollar value of a penalty unit (Crimes Act 1914 s 4AA) is not deposited
either, so penalties are given in penalty units.

**Checks:** one module (`sa-messages.l4`, 15 exported questions) and one case file (`sa-cases-messages.l4`). 45 assertions
satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98. One deliberately wrong expectation was
put in a throwaway copy of the case file, and the check caught it (44 of 45).

There was no first-pass encoding of this Act.

## Seat

**The consumer receiving marketing messages.** The Act calls that person the *relevant electronic account-holder* (s 4):
the person responsible for the email, messaging or telephone account a message is sent to. Every rule in Part 2 is addressed
to the sender ("A person must not send, or cause to be sent, …"). But the person the scheme protects, whose consent and
unsubscribe matter (s 16(2), s 18, Sch 2), is the recipient. Chloe's question in the WA lives is "Can she stop them?". So the
exported questions ask what she would ask: "Is this a commercial electronic message?", "Did the sender need my consent?",
"Must it let me unsubscribe?", "Has my unsubscribe taken effect?".

Departure: two questions in § s 25 and Schedule 3 are asked from the **sender's** seat ("What is the most I can be made to
pay?"), because the brief asked for the sender's side as far as Daniel's company might need it. No Daniel event cites this
Act, so those cases are invented.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Regulations set no number this encoding
  needs. They do add conditions, which are left out and said so.
- **The actors the text names.** Followed: the relevant electronic account-holder, the person who authorised the sending,
  government bodies, registered political parties, registered charities, educational institutions, the ACMA, the Federal
  Court.
- **A judgment handed to someone else is answered conditionally.** Followed. Whether "it would be concluded" that a purpose
  of the message is commercial (s 6(1)) is asked as one flag per purpose group. Whether consent "can reasonably be inferred"
  (Sch 2 cl 2(b)) is a flag. The sender's defences of mistake and not knowing of the Australian link (s 16(3), (4)) cannot be
  stated by the consumer, so the s 16 answer is "it breaks s 16(1), unless the sender shows …".
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed for electronic message, commercial
  electronic message, Australian link, designated commercial electronic message, consent and its withdrawal. Borrowed terms
  are facts: standard telephone service, listed carriage service, registered charity, registered political party,
  government body (defined in s 4, but by kind, so asked as the sender's kind).
- **One case is the text's natural unit.** Followed: one message, with what I have said to or done with its sender.
- **The Act's own terms, each with a plain gloss.** Followed in comments.
- **Operative sections in scope; machinery out.** Followed. Part 2 and the Schedules that define its terms are in. ACMA
  powers, injunctions, undertakings and regulation-making are out. The penalty maxima are in only from the sender's seat.

## The lives

- **Chloe, c044 (July 2024, aged 21), "Marketing calls and texts — Can she stop them?"** The scenario cites ss 16 and 18. It
  states no sender, consent or dates, so the encoder supplied them: a retailer's promotional text, a ticked box, a reply of
  STOP on a Monday. Decisions asked:
  - `Is this an electronic message`: her marketing **calls** on an ordinary phone line are not electronic messages (s 5(5)),
    so this Act cannot stop them. The Do Not Call Register Act 2006 is the route for those. Her **texts** are electronic
    messages.
  - `Did the sender need my consent`: without consent, the retailer's text breaks s 16(1). With the ticked box it was allowed
    until her STOP took effect.
  - `Has my unsubscribe taken effect` and `How many calendar days until my unsubscribe takes effect`: a STOP sent on a Monday
    takes effect at the end of Friday, if there is no public holiday.
  - `Does it break the sender-information rule` and `Does it break the unsubscribe rule`: a text that names no sender and
    offers no way to unsubscribe breaks both.

## Why this scope

Chloe's question is answered by four things: whether the message is within the Act (ss 5-7), whether it needed her consent
(s 16, Schs 1-2), whether it had to tell her who sent it and let her unsubscribe (ss 17-18), and when her unsubscribe binds
the sender (Sch 2 cl 6). Those are the whole of Part 2 as it reaches a recipient. The Act gives the recipient no right to sue:
the ACMA brings penalty proceedings (s 26(1)). So the consumer's remedy is a complaint to the ACMA, which is outside the text
encoded. Part 3 (address harvesting) never reaches a recipient as a question they can answer.

## What the Act turns out to say

1. **A marketing voice call on an ordinary phone line is outside the Act.** s 5(5): a message "sent by way of a voice call
   made using a standard telephone service" is not an electronic message. Half of Chloe's problem (the calls) is not this
   Act's. Asserted.
2. **A scam is a commercial electronic message.** s 6(1)(m)-(o) count a purpose of helping someone "by a deception, to
   dishonestly obtain property" or a gain. A parcel-fee scam text is therefore spam under the Act, with an Australian link
   because Chloe reads it in Australia (s 7(c), (d)), wherever it came from. Asserted.
3. **The Australian link is almost always there for an Australian recipient.** s 7(d)(i) is satisfied whenever the
   account-holder "is physically present in Australia when the message is accessed". Only a message read abroad on a foreign
   device, from a foreign sender, escapes. Asserted.
4. **Designated messages are exempt from consent and unsubscribe, but not from sender identification.** Sch 1 cl 1 Notes 1
   and 2. A registered charity selling its own raffle tickets needs neither consent nor an unsubscribe link (cl 3). But if it
   gives no contact details it still breaks s 17. Asserted.
5. **An educational institution's exemption depends on the recipient.** Sch 1 cl 4 applies only if the account-holder, or a
   member or former member of their household, "is, or has been, enrolled". The same course email from a university Chloe
   never attended is ordinary spam. Asserted.
6. **Withdrawal takes 5 business days, counted from the day the STOP is sent.** Sch 2 cl 6(1): "at the end of the period of
   5 business days beginning on" the day an electronic message was sent. Messages sent within that window are still covered
   by the old consent. A STOP sent on Monday binds from Saturday. One sent on Sunday also binds from Saturday, because the
   period starts on Sunday but its first business day is Monday. One sent Tuesday to Friday, or on Saturday, can be relied on
   for 7 calendar days counting the day sent, and binds from the eighth. The weekday table is the encoder's working, not the Act's words, and ignores public holidays.
   Asserted.
7. **Consent cannot be inferred merely from a published address.** Sch 2 cl 4(1). A conspicuously published work address,
   published with agreement and with no "no spam" statement, is deemed consent, but only to messages relevant to the work
   (cl 4(2)). Asserted.
8. **A contract can displace the unsubscribe facility.** s 18(3): s 18(1) "does not apply to the extent (if any) to which it
   is inconsistent with the terms of a contract or other agreement". Nothing equivalent qualifies s 16 or s 17. Asserted.
9. **The penalties are set in penalty units, and doubled for s 16.** s 25: for a body corporate with no prior record, 100
   units per s 16 contravention and 50 for ss 17-18, capped at 2,000 and 1,000 a day. A prior record multiplies each by five.
   An infringement notice (Sch 3 cl 5) is 20 units per s 16 contravention for a company, capped at 1,000 from 50
   contraventions, which is the 50-times rate. Asserted.
10. **The 30-day horizons.** Sender contact details must be "reasonably likely to be valid for at least 30 days" (s 17(1)(d)).
    The unsubscribe address must be able to receive messages "at all times during a period of at least 30 days" (s 18(1)(e)).
    Both are asked as single facts.

## What would need doing before this is worth anything

- Deposit the Spam Regulations 2021 and encode their conditions, exclusions and extra designated messages. The current
  answers assume they add nothing, which is unlikely to be right at the margins.
- Encode public holidays in the business-day count (Sch 2 cl 6(2)), by place.
- Encode s 7(e), s 16(6) and the ancillary contraventions if a sender's seat is ever wanted. Encode Part 3 if a life events
  turns on harvested lists.
- Join this to the Do Not Call Register Act 2006 and to APP 7 of the Privacy Act 1988 so that Chloe's "Can I stop them?"
  gets one answer across calls, texts and post.
- An independent test pass and a human gate, as for any encoding.
