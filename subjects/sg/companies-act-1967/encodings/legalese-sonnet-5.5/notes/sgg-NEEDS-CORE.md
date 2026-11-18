# NEEDS-CORE (sgg)

What the keel's core (`sg-core.l4`) lacks for Division 2 of Part 11 (foreign companies), and what this part declares in its place.

## The party type has no foreign company and no authorised representative

`Party` in `sg-core.l4` has twelve constructors: `Individual`, `Company`, `Director`, `Officer`, `Secretary`, `Member`, `Creditor`, `Auditor`, `Registrar`, `Minister`, `Court`, `Authority`.
Its own comment on `Company` is "a company incorporated under the Act", which a foreign company is not, and none of the twelve is an authorised representative of a foreign company.
Division 2 has 32 regulative rules, and their bearers are:

- the foreign company, in 25 rules (ss 368(1), 370(1), 370(4), 370(6)(a), 370(7), 372(1), 372(4), 373(6), 373(7), 374, 375(1)(b), 375(1)(c), 375(3), 377(1), 378(5) twice, 379(1)(a), 379(1)(b), 379(2)(a), 379(2)(b), 379(3), 380(2)(a), 380(2)(b), 380(2)(c) and 380(4));
- a director of the foreign company, in 1 rule (s 368A(1));
- an authorised representative of the foreign company, in 4 rules (ss 368A(2), 377(2)(a), 377(2)(b) and 377(2) for the notice of a liquidator's appointment);
- a director or an authorised representative, in 2 rules that take the party as an input (ss 368A(4) and 372(1A)).

This part declares its own types in `sgg-scope.l4`:

- `s 365 party`, four constructors: `s 365 the foreign company`, `s 365 a director of the foreign company`, `s 365 an authorised representative of the foreign company`, `s 365 an officer of the foreign company`, each with a name field.
- `s 365 role`, five constructors, used by the offence functions to say who the person is: `s 365 role: the foreign company`, `s 365 role: a director of the foreign company, or an equivalent person`, `s 365 role: an authorised representative of the foreign company`, `s 365 role: an officer of the foreign company`, `s 365 role: someone else`.
  "Or an equivalent person" is in the constructor because ss 373(18) and (18A) name "every director or equivalent person".

## What would let the part drop its own types

Proposed, not landed: a core `Party` constructor for a foreign company, one for an authorised representative of a foreign company, and a core role type for offence provisions.
With those, `s 365 party` and `s 365 role` would be replaced by the core names, and the regulative rules above would change their party type only; no rule's conditions, which come from the text, would change.

## Why this part did not edit the core

The keel's modules are read-only to a part agent, and the parts are written in separate sandboxes, so a type declared in this part cannot be seen by another part.
A part that needs the same people would have to declare its own, which is the reason to settle the constructors once in the core.
