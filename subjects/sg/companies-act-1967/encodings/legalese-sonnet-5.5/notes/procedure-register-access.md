## Procedure layer: access to the register of members (Companies Act 1967 s 12(2)(d), s 192(3) and (4), s 196A(1) and (5))

Module `sg-proc-register-access.l4`, tests `sg-proc-register-access-tests.l4`.
It adds a regulative layer over the Boolean encodings in `sgh-registers.l4`, `sgm-part5-div4.l4` and `sgm-part5-div4a.l4`, and edits none of them.
The parties are the corpus's own `Party` (`sg-core.l4`).
The acts are the new enum `register access act`.
Every rule is gated by the existing section function: where the gate does not answer `JUST TRUE`, nothing is owed and the rule is `FULFILLED` at once.

### The seat of each DEONTIC

- `s 12(2)(d) the person may obtain a copy of or an extract from the electronic register of members once the prescribed fee is paid`.
  The person (any `Party`) MAY obtain the copy or extract.
  Gate: `s 12(2)(d) the person may have access to the electronic register of members by obtaining a copy of or an extract from it` (fee paid, the register is the s 196A register, and the s 12(2A) and (2B) exclusions).
- `s 192(3) the person may ask the public company for a copy of the register and the company must send it within the period`.
  The person MAY ask the public company; HENCE the company MUST send the copy WITHIN the period, LEST BREACH BY the company, the BECAUSE naming the s 192(4) offence of the company and of every officer in default.
  Gates: `s 192(3) the person may request a copy of the part of the register` and `s 192(3) the sum required in advance for a page is one the subsection allows`.
  The number of days comes from `s 192(3) the number of days from the receipt of the request to the last day for sending the copy` (new in this module, with four `#ASSERT`s), which calls `s 192(3) the last day for sending the copy`.
- `s 196A(1) the Registrar must keep and maintain an electronic register of members, as a standing duty`.
  The Registrar MUST keep the register, with no time limit.
  Gate: `s 196A(1) the Registrar must keep an electronic register of members of the company`.
- `s 196A(5) the Registrar must update the electronic register of members for a change lodged, as a standing duty`.
  The Registrar MUST update the register, with no time limit.
  Gate: `s 196A(5) the Registrar must update the electronic register of members in accordance with the change`.

### The TIMELINE lines

- s 12(2)(d): unit=calendar day; day 0=the day the person, having paid the prescribed fee, obtains the copy or extract; counting=silent (the text puts no time limit on the person or on the Registrar).
- s 192(3): unit=calendar day; day 0=the day on which the public company receives the request (the day of the person's request is taken to be that day); counting="commencing on the day next after the day on which the request is received by the company", so the 21st day is day 21, and "within such further period as the Registrar considers reasonable in the circumstances" is added to the 21; the number of days is computed from the DATE inputs by `s 192(3) the number of days from the receipt of the request to the last day for sending the copy`.
- s 196A(1): unit=calendar day; day 0=the day the Registrar's duty is asked about (the duty runs "On and after 3 January 2016", which the gate checks); counting=silent (the text states no period within which the register is to be kept).
- s 196A(5): unit=calendar day; day 0=the day the change that is required or authorised to be lodged is lodged with the Registrar; counting=silent (the text states no period within which the Registrar updates the register).

### The forks

- s 192(3): the person's request and the company's receipt of it fall on the same day, which is day 0 (the other reading: the company receives the request on a later day, and the 21 days run from that day).
- s 192(3): "such further period as the Registrar considers reasonable" is days added to the 21 (the other reading: it replaces the 21 days as the whole period).
- s 192(4): the offence is the consequence of the company's breach, written in the BECAUSE of the LEST, because guilt is a status that nobody does; the officers in default are named in the BECAUSE and are no party to the rule (the other reading: each officer in default as a party, with "in default" left as an input).
- s 12(2)(d): the Registrar has no step, because the text gives the person a liberty and names no duty or time for the Registrar (the other reading: the Registrar MUST supply the copy, with no deadline).
- s 196A(1) and (5): a MUST with no deadline carries no LEST and no BREACH, because nothing can be missed (the other reading: a LEST BREACH that can never be reached, as the existing rules for these two subsections have).

### What the text leaves silent

- No time for the person to ask, and none for the Registrar to supply a copy under s 12(2)(d).
- No fee amount: s 12(2) says only "the prescribed fee", so it is an input.
- No time for the Registrar to keep or update the electronic register, and no consequence stated for failing to.
- No step after the s 192(4) offence: the text says "liable on conviction" and names no prosecution, court act or time for one, so none is encoded.
- How the Registrar decides on a further period under s 192(3): the number of further days is an input, not a step.

### Differences from the existing DEONTIC

Compared by reading the existing rules after writing these, not by running them.
There is no existing DEONTIC for s 12(2)(d).

- s 192(3) (`sgm-part5-div4.l4:737`): the existing rule is a single MUST of the company with no gate.
  This module gates the duty on a request the subsection allows, because the text lets a person request a copy "only so far as it relates to names, addresses, number of shares held and amounts paid on shares", on "payment in advance of $1 or such less sum" (src:17248-17254), and the company must send "any copy so requested" (src:17253-17255).
- s 192(3): this module adds the person's request as a first step, a MAY with no limit, because the text begins "Any member or other person may request" (src:17248); the existing rule starts at the company's duty.
- s 192(3): the limit is the same number of days in both, 21 plus the further days, by arithmetic: the last day is the 21st day after receipt (src:17255-17257).
  Here it is computed from a DATE through `s 192(3) the last day for sending the copy`; the existing rule adds the numbers directly.
- s 192(3) and (4): the BECAUSE here names the offence of the company and of every officer in default (src:17261-17265); the existing rule's BECAUSE says only that the copy was not sent in the period.
- s 196A(1) (`sgm-part5-div4a.l4:44`): the existing rule has no gate and a LEST; this module gates it on the company being a private company and the date being on or after 3 January 2016, because the text says "On and after 3 January 2016, the Registrar must, in respect of every private company" (src:17447-17448), and carries no LEST.
  The unstable build warns that the existing rule's LEST can never be reached (`lint/lest-without-deadline`, `sgm-part5-div4a.l4:49`).
- s 196A(5) (`sgm-part5-div4a.l4:249`): the existing rule has no gate and a LEST (warning at `sgm-part5-div4a.l4:254`); this module gates it on a change that is lodged under one of the listed provisions or is required or authorised by another provision to be lodged, because the text says "any change that is required or authorised by any provision of this Act to be lodged with the Registrar" (src:17512-17516).
  Where the gate fails the existing rule's duty stays open, and this one is `FULFILLED`.

### Which binary verified the traces

Both builds were run from inside the encoding folder with `JL4_LIBRARY_PATH` unset.
The unstable build is `l4-unstable-20261125-a50cbd0-darwin-arm64`, and the stable build is the cache entry 112.
All 25 traces matched their `-- EXPECT` on both (`expect_check.py`).
The four `#ASSERT`s are satisfied on both.
Neither file gives an error or a warning on either build; the warnings that appear when the module is run on the unstable build are in the modules it imports (for example `sgh-registers.l4:401` and `sgm-part5-div4a.l4:49`), and are not changed here.
The expected outcomes were written from the text before the first run.
A copy of the module with the limit made one day too long failed three traces, so the traces can fail.

### READS-DIFFERENTLY-ON-MAIN

None by outcome class: every trace gives the same class on the stable build as on the unstable build.
The only difference is in print: a still-open MAY is laid out on one line by the unstable build and on three lines by the stable build.

### What was not encoded

- s 12(2)(a), (b) and (c), and s 12(2AA) to (2D) except as the gate's inputs, because they are outside this unit.
- s 192(1) and (2), the closing of the register and the inspection of it, because they are outside this unit.
- s 196A(2) and (3), what the register contains, and s 196A(4), the company's duty to give the Registrar particulars of a change when it buys its own shares, and s 196A(6), the register as prima facie evidence: no step or clock that the access procedure needs, and the Boolean modules cover them.
- A court step after the s 192(4) offence, because the text states none.
