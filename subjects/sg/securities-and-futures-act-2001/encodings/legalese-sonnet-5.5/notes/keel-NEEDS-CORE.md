# NEEDS-CORE (keel, sfa)

## Types or constructors the keel had to put in its own modules because they belong in the core

One, and it is a placement choice, not a gap.

- `Period unit` (`Days`, `Weeks`, `Months`, `Years`) is declared in `sfa-periods.l4`, not in `sfa-core.l4`, and has no provision label (the period functions are `period: ...`).
  A part that counts a period imports `sfa-periods` and gets the type with the functions.
  The lead may hoist it to the core at the merge; nothing in the keel depends on where it lives, provided the modules that use it import whichever module declares it.

The enumerations that `sfa-definitions-persons.l4`, `sfa-definitions-schemes.l4` and `sfa-definitions-markets.l4` declare (the "which meaning of the term" inputs of s 2(1) "customer", "representative", "participant", "responsible person", "voting unit", "user" and "prescribed written law") each carry a provision label and belong with their functions, so they are not core nouns and are not listed as asks.

## Types or constructors the keel expects a part to ask for (not built)

Nothing below has been confirmed by reading the provision: each item comes from a section heading in `inputs/HEADINGS.md` or from a single line cited, and a part that needs one defines it in its own module under its own provision label and records it in its own `NEEDS-CORE.md`.
None is in the core, so none is promised.

- Offer record, for sfac and sfad: the offeror, the issuer, the kind of product (the core has `Kind of product`), the date, whether consideration is given (s 272(1), line 42650: "if no consideration is or will be given for the issue or transfer"), and the number of persons offered to (lines 43345 to 43348: a person is counted "for the purposes of determining whether offers of the securities or securities‑based derivatives contracts are made to no more than the applicable number of persons specified in subsection (1)(a)").
- Profile statement and product highlights sheet records, parallel to the core's `Prospectus` (headings s 240, s 246, s 240AA).
- `Party` constructors for an expert (heading s 249), an issue manager and an underwriter (heading s 249A), a borrowing entity (heading s 268) and a guarantor entity (heading s 269); the core's `A trustee` already covers the trustee of heading s 265A and s 266.
- No ask is foreseen for Parts 7, 8 and 12 (their headings were read, not their provisions): the core's `Party` already has a director, an officer, a chief executive officer, a substantial shareholder, a substantial unitholder and a holder of securities, and the core has `Penalty`.

## Shared input names (not types)

The facts that every part's seat states the same way are fixed in PLAN.md section 7, with their `@desc`; a part that needs another shared fact says so in its own file.
