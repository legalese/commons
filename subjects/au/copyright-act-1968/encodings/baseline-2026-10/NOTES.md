# Copyright Act 1968 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design
defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent
test pass, no human gate. Not for public use as advice.

**Edition:** Compilation No. 65, compilation date 2 April 2026 ("Includes amendments:
Act No. 29, 2026"; register id C2026C00138), as deposited at
`../../registers/source-bundle/C1968A00063.txt` (retrieved 2026-10-13). No regulations
used: the plan names none. Whether regulations under s 184 extend the Act to a foreign
work is an input.

**Checks:** one module (`ca-ownership.l4`) and one case file (`ca-cases-ownership.l4`),
50 assertions satisfied, 0 errors, 0 warnings, with the stable `l4` of VS Code extension
1.6.98. Expected values were written by hand from the text in the scratchpad generator
`gen_copyright-act-1968_baseline.py`.

## Seat

**The employee-author and the founder**: the person who writes the code, as an employee,
a contractor or a founder-director, and asks "Who owns the code I write at work?". The
life event is a founder's (Daniel's company, Jarrah), and the Act's ownership rule is
about the author, so both sides of the same question are asked from the same rules:
"who owns what I wrote?" and "does my company own what my engineer, and I, wrote?".
Every exported decision is phrased as that person asks it (`Who first owns the copyright
in what I made`, `Would I infringe the copyright`, `Do I have moral rights in it`).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The
  Act sets its own numbers (70 years, 50 years, 1 January 2019); no instrument is needed.
  The s 184 regulations (foreign works) are not deposited, so their effect is an input.
- **The actors the text names.** Followed: author, employer, proprietor of a periodical,
  the person who commissions, assignor and assignee, owner and licensee of a copy, the
  legal personal representative.
- **A judgment handed to someone else is answered conditionally.** Followed: whether it
  was "reasonable in all the circumstances not to identify the author" (s 195AR) is an
  input for the court.
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed:
  "computer program", "literary work", "work", "qualified person", "made public" and the
  s 35 limbs are worked out. "Original", "contract of service" (employee or contractor)
  and "in pursuance of the terms of" the employment come from the general law and are
  asked as facts.
- **One case is the text's natural unit.** Followed: one work, the circumstances of its
  making, and one dealing with it.
- **The Act's own terms, each with a plain gloss.** Followed, in the `@desc` lines.
- **Operative sections in; machinery out.** Followed, and narrowed further (see "Why this
  scope").

## The lives

- **Daniel, d046 (1 September 2031)** — "the code owned by the company". The decisions
  it asks: `Who first owns the copyright in what I made` (the engine written by Jarrah's
  employed engineers is Jarrah's, s 35(6)); `Who owns the copyright now` (Daniel's own code
  as a founder-director without an employment contract stays his until he signs an
  assignment, ss 35(2), 196(3), 197); `What is the last year the copyright lasts` (the
  term runs from the engineer's death, not the company's); `Do I have moral rights in it`
  and `Is my right of attribution infringed` (the engineer keeps moral rights; the
  employment contract's blanket consent protects Jarrah, s 195AWA(4)). Facts the scenario
  does not state are labelled assumptions in the case file: that the engineers are
  employees writing the engine as part of their jobs; that it was written in Perth by
  Australian residents and is unpublished; that Daniel had no employment contract; the
  engineer's year of death (illustrative).

## Why this scope

The Act is very large (over 900,000 characters). The brief asks for the employee-author
and founder's questions: whether software is a literary work, whether copyright
subsists, who owns it (employees, commissioned works, agreements to the contrary), what
only the owner may do, infringement, how long it lasts, assignment in writing, and the
author's moral rights as far as the event needs. Left out: Part IV subject-matter
(sound recordings, films, broadcasts, published editions) except to say it is not a
"work"; fair dealing and the other exceptions (s 47C back-up copies and the rest of
Division 4A, except s 47B(1)-(2)); commercial rental before 1994 (s 31(6), (7));
remedies and offences; Crown copyright (Part VII) and Part X, to which s 35 is subject;
pseudonymous joint works (s 81); performers' moral rights, film moral rights and consent
for films (s 195AW); derogatory treatment beyond the word; attribution for artistic
works (s 194(2)); the Tribunal, collecting societies and statutory licences. Patents and
trade marks, in the same life event, are other Acts.

## What the Act turns out to say

1. **Software is a literary work.** s 10(1): "literary work includes ... (b) a computer
   program or compilation of computer programs", and a "computer program" is "a set of
   statements or instructions to be used directly or indirectly in a computer in order to
   bring about a certain result". Asserted.
2. **Copyright needs no registration, but it needs the code written down and an
   Australian connection.** s 32(1): an unpublished original work whose author was "a
   qualified person" — "an Australian citizen or a person resident in Australia"
   (s 32(4)) — when it was made. A work is made when "first reduced to writing or to some
   other material form" (s 22(1)), which includes invisible storage (s 10(1)). An idea
   never written down, or code copied from elsewhere, gets none. A foreign author's work
   first published abroad depends on regulations under s 184 (not deposited). Asserted.
3. **An employee's code belongs to the employer only if written "in pursuance of the
   terms of" the employment, under a contract of service.** s 35(6). A side project
   outside the employee's duties stays with the employee. Asserted.
4. **Commissioned software stays with the programmer.** The commissioning rule (s 35(5))
   reaches only photographs for a private or domestic purpose, portraits and engravings;
   a contractor paid to write code owns it, absent a written assignment. Asserted.
5. **A founder-director without an employment contract is not an employee for s 35(6).**
   On the text, the founder's own code is his, not the company's, until he assigns it.
   That turns on whether he is under a "contract of service", a general-law question
   asked as a fact (an inference about the founder's position, not stated in the
   scenario). Asserted on the assumption.
6. **An assignment must be in writing and signed by the assignor; future copyright can be
   assigned in advance.** s 196(3): an assignment "does not have effect unless it is in
   writing signed by or on behalf of the assignor". s 197(1): a signed agreement assigning
   "a future copyright" vests it in the assignee when the work comes into existence. An
   assignment can be limited to some acts, places or part of the term (s 196(2)). Asserted.
7. **But the employer's statutory ownership can be displaced "by agreement", and the text
   does not ask for writing.** s 35(3). The contrast with s 196(3) is on the face of the
   text; whether an oral agreement suffices is not tested here. Asserted for an agreement
   that keeps the copyright with the employee; a modification of the rule is not modelled.
8. **The company owns the copyright, but its term runs from the author's death.** s 33(3)
   item 1: "70 years after the calendar year in which the author of the work died"; for
   joint authors, the last to die (s 80). An engineer dying in 2070 gives Jarrah copyright
   to the end of 2140. Until the author dies the end is not fixed (NOTHING). Asserted.
9. **Computer programs are excluded from the posthumous-publication rule.** s 33(2) item 2
   (works made public before 2019 after the author's death) covers "a literary work (other
   than a computer program)": a manuscript published in 2010, 20 years after its author's
   1990 death, lasts to 2080; a program in the same position to 2060. Asserted.
10. **Anonymous works run from making or from first making public.** s 33(3) items 2 and 3:
    an anonymous program made in 2020 and released in 2025 lasts to 2095; one never made
    public is not yet fixed; an anonymous text made in 1960 and never made public lasts to
    2030. Asserted.
11. **Only the owner may reproduce, publish, communicate, adapt, and rent out a program.**
    s 31(1)(a), (d). Renting a machine whose program cannot be copied in ordinary use, or
    where the program is not "the essential object of the rental", is outside the right
    (s 31(3), (5)). Asserted.
12. **The departing employee who copies the code infringes; running a licensed copy does
    not.** s 36(1) (anyone "not being the owner ... and without the licence of the owner");
    s 47B(1), (2) (the automatic copy made in running a copy, except from an infringing
    copy). Asserted.
13. **The employee keeps moral rights in code the employer owns; a company has none.**
    s 190: "Only individuals have moral rights"; s 192(1): they are "in addition to" the
    copyright. They last as long as the copyright (s 195AM(2), (3)) and cannot be assigned
    or left by will (s 195AN(3)); after death the legal personal representative enforces
    them (s 195AN(1)). Asserted.
14. **An employee can give a blanket written consent for all work done in the
    employment.** s 195AWA(4). Anyone else's consent must specify the acts and the works
    (s 195AWA(3)). Duress or a knowingly false statement voids it (s 195AWB). Asserted.
15. **Shipping an employee's code without naming her infringes her right of attribution,**
    unless the employer establishes that it was reasonable not to name her (s 195AR), her
    consent covers it, or it is done outside Australia (s 195AX). Asserted (s 195AR as an
    input).

## What would need doing before this is worth anything

- The general-law questions asked as facts — originality for code, employee or
  contractor, "in pursuance of the terms of" employment, and a founder-director's
  position — need the cases.
- The regulations under s 184 (foreign works) are not deposited; their effect is an input.
- The exceptions (fair dealing, s 47C back-ups, interoperability and security testing in
  Division 4A), remedies and offences are not encoded, so `Would I infringe the copyright`
  can say TRUE where an exception would excuse the act.
- "Until 70 years after the calendar year" is read as to the end of that year; the two
  70-year windows for an unknown author are one input.
- No independent test pass, no coverage table, no human gate.
