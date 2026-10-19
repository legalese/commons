# Immigration Act 1959 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the Act is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`; a case the
encoding does not cover returns a value that says so. Checked with the stable
`l4` of VS Code extension 1.6.98. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This encoding replaces the first-pass encoding `naive-2026-10` (190 assertions
over three modules). It keeps that encoding's topics and the hand-checked
values that still hold (day 90 and day 91, the two- and three-check landlord,
the broker and the couple, the wife and the husband, the procedural-only
review), rephrased from the individual's seat, and adds what the deposited
Immigration Regulations now settle.

**Edition:** Immigration Act 1959, 2020 Revised Edition, informal consolidation
in force from 30 September 2026, deposited at
`../../registers/source-bundle/IA1959.txt`; Immigration Regulations (Rg 1),
informal consolidation in force from 1 January 2026, deposited at
`../../registers/source-bundle/IA1959-RG1.txt` (used for reg 6(1), reg 12(1)
to (1B) and Sixth Schedule items 1 and 2).

**Checks:** two case files, 57 assertions satisfied, 0 errors, 0 warnings
(39 in `imm-cases-entry-and-stay.l4`, 18 in `imm-cases-offences.l4`), plus two
`#TRACE`s of the re-entry duty (applying on day 179 is `FULFILLED`; on day 200
it is `BREACHED`). Fixtures are built by a generator script
(`gen_immigration-act-1959_baseline.py`, scratchpad) with expected values
written by hand from the text.

## Seat

**The individual:** the non-citizen who comes to, stays in or is sent away from
Singapore — a visitor, a pass-holder, a permanent resident abroad, a former
citizen — and, in `imm-offences.l4`, the individual who lets a room to,
employs, occupies a site with, marries or applies for such a person.

**Why.** Almost every operative section of the Act is addressed either to the
Controller (who may refuse, cancel, remove) or to the non-citizen (who must
not enter, must not remain). The Controller's powers are encoded as what they
mean for the person: what may be done to me, whether I must be told, whether I
can go to court. The citizen appears only where the Act speaks to the citizen
at the border (s 5, s 7, s 9(2), s 9AA(2)(a), s 32(2)).

**Departure: a second seat for Part 6.** The offences the first-pass encoding
covered (harbouring, employing, marriages of convenience) are committed by a
different individual — a landlord, employer or spouse — whose liability turns
on someone else's status. To keep that coverage, `imm-offences.l4` takes that
individual's seat and says so in its header. The two seats share only the
`Sentence` record.

**The 2026-10-18 defaults:**

- *The Act alone, with the instruments that set its numbers.* Followed. The
  Regulations are deposited, so the 180-day period (reg 6(1)), the visit pass
  rules for prohibited immigrants (reg 12(1) to (1B)) and the permit fees
  (Sixth Schedule items 1 and 2) are brought in. Not brought in: the s 57A(5)
  measures for work places (a Gazette notification, not deposited) and the list
  of compoundable offences under s 59 (not read).
- *The actors the text names.* Followed: the Controller, the Minister, the
  court, the carrier's master. No actor is invented.
- *A judgment handed to someone else, answered conditionally.* Followed: the
  Controller's opinion that I am in a prohibited class (s 8(1)), the
  Controller deeming me undesirable (s 8(3)(d)), the Controller being satisfied
  of a cancellation ground (s 14), the Controller considering reasons against
  the public interest (s 33(6)) are inputs or are carried into the answer
  ("must be cancelled, if the Controller is satisfied of the ground").
- *The Act's own definitions worked out, borrowed terms asked.* Followed for
  "prohibited immigrant" (from the s 8(3) classes), "permanent resident" (the
  holder of an entry permit), "immigration advantage" (s 57C(6)) and the
  harbouring due diligence (s 57(7C), (7D)). **Departure:** "immigration
  offender" (s 57(13)) is the Act's own term but is asked as a fact, because it
  is a fact about another person that the landlord or employer cannot compute
  from their own position. Borrowed and asked: whether I am punishable with
  caning (Criminal Procedure Code 2010 s 325(1)), whether a crossing point is
  authorised (a Gazette declaration), whether a site is a work place.
- *One case is the text's natural unit.* Followed: one person's entry, stay or
  absence; for the offences, one charge.
- *The Act's own terms, each with a plain gloss.* Followed; glosses are in the
  comments beside each type.
- *Operative sections in; machinery out.* Followed: appointments, the
  Minister's directions, regulation-making, officers' powers, carriers'
  passenger information and the cross-border railway Part are out.

## Why this scope

The Act is long (Parts 1 to 6 and Parts 5A and 5B). The individual meets it at
the border, while staying, when status ends, and when removed. Those are
encoded, with the sentences they carry. The carriers' duties (Part 4), the
information-sharing Part 5A, railway pre-clearance (Part 5B), the classes of
pass other than the visit pass, s 6A (children born here who are not
citizens), and the s 57 offences of conveying, obstruction, document misuse and
forgery are left out.

## What the Act turns out to say

1. **HIV still makes a foreigner a prohibited immigrant; the relief is in the
   regulations, discretionary and short.** s 8(3)(ba) is unqualified. Reg
   12(1A) lets the Controller issue a visit pass to that person, called an
   "exempt prohibited immigrant", and reg 12(1B) caps its first validity at
   90 days. Whether reg 12(1A) reaches someone who is also in another class is
   not said; the encoding returns `not covered by this encoding`. Asserted.
2. **Prohibition is inherited.** s 8(3)(n): "the family and dependants of a
   prohibited immigrant" are a prohibited class. Asserted.
3. **Day 91 of an overstay is mandatory prison and caning.** s 15(3): up to 90
   days, a fine up to $4,000 or up to 6 months; from day 91 the person "shall"
   be imprisoned and caned, at least 3 strokes. A person not punishable with
   caning is still imprisoned, with a fine up to $6,000 in lieu. Unlawful entry
   (s 6(3)(a)) carries the same from the first day. Asserted.
4. **A permanent resident abroad has 180 days, and a rejection still ends
   residence.** s 11(1A) with reg 6(1): apply within 180 days of first being
   outside without a valid re-entry permit. Read with s 11(1E) and (1F), the
   last day is the first day plus 179 (inference: the first day counts as day
   1); s 14A(2)(a) cancels the entry permit the next day. Applying early does
   not save a resident whose application is refused (s 14A(1)(c)). Missing the
   deadline is not an offence; its consequence is cancellation. Asserted
   (1 March 2026 gives 27 August and 28 August 2026).
5. **A landlord needs all three checks to escape the negligence charge.** s
   57(7C): any two of the (7D) checks are due diligence against reckless
   harbouring, all three against negligent harbouring, and (7B) lets the
   prosecution fall back to the negligent charge. Asserted.
6. **The broker is guilty where the couple are not, and citizenship is not an
   "immigration advantage".** s 57C(1) needs both knowledge and gratification
   for a party; (2) needs only intention for an arranger. s 57C(6) defines the
   advantage as a visa, pass, permit or re-entry permit for a party or a party's
   child or parent: citizenship is not in the list. Asserted.
7. **Section 12 endorses a wife, not a husband.** Asserted.
8. **Only procedure is reviewable, and no one need be heard.** s 39A excludes
   judicial review, habeas corpus included, except on "compliance with any
   procedural requirement"; s 39B removes the right to be heard. Asserted.
9. **Notice of a cancellation is owed in every case but one.** s 14(5A)
   requires notice of a cancellation under s 14(2), (3), (4) or (5) or a
   declaration, but not of a cancellation under s 14(1) (arriving with a child
   not endorsed on the permit). Asserted.
10. **An overstayer can be removed without being prosecuted, and need not be
    told why.** s 33(1): "whether or not any proceedings are taken"; s 33(6):
    no reason need be assigned where the Controller considers it against the
    public interest; s 35: arrest without warrant and up to 14 days' detention
    pending the decision. Asserted (removal).
11. **A no-boarding directive need not be disclosed, but cannot rest on
    "undesirable" against a pass-holder.** s 9AA(6) and (2)(b). Asserted.
12. **Permanent residence is discretionary for everyone.** s 10(2) "may"; no
    qualifying period and no class of applicant, a citizen's spouse included.
    The fees are $100 to apply and $20 on issue (Sixth Schedule item 1); a
    re-entry permit is $10 for each year or part (item 2). Asserted.
13. **Employing more than five offenders adds caning with no stated minimum.**
    s 57(1A) gives "caning in addition" and names no number of strokes; (1B)
    gives a fine up to $10,000 in lieu. Asserted.
14. **An honest mistake on a form is an offence.** s 57(1)(ka) is strict
    liability (s 57(1AAA)), fine only, up to $4,000; knowing falsity (k) is up
    to $8,000 or 12 months. Asserted.
15. **An entry ban for economic or social reasons spares the resident abroad
    with a re-entry permit; one for security or health does not.** s 9(1A).
    Asserted.

## What would need doing before this is worth anything

- An independent test pass and the human gates.
- The s 57A(5) Gazette measures for work places, and the regulations'
  list of offences compoundable under s 59.
- The other classes of pass (dependant's, student's, special, landing), which
  live in the regulations.
- No case law was searched; sentencing practice on ss 6, 15 and 57 is
  extensive, and the "presumptive minimum" terms (ss 9(5), 36(2), 57(1AA))
  are not explained in the Act.
