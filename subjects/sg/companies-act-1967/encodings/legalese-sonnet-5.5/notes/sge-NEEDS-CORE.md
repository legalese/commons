# NEEDS-CORE (sge): what the core lacks for Part 10A

One item: a `Party` constructor for a body that is not yet a company.
Rules before registration (s 357(1), s 358(1)) bind a foreign corporate entity: a body corporate incorporated outside Singapore that intends to be registered.
The core's `Party` has `Individual`, `Company`, `Director`, `Officer`, `Secretary`, `Member`, `Creditor`, `Auditor`, `Registrar`, `Minister`, `Court` and `Authority`, and none of them fits a body that becomes a company only on the date of registration (s 361(1)(a)).
`sge-p10a-357-358.l4` therefore declares a small type of its own, `s 357 party`, with one constructor `s 357 the foreign corporate entity` carrying the entity's name, and uses it for the two rules of ss 357(1) and 358(1).
Wanted constructor: `ForeignCorporateEntity HAS `the name of the foreign corporate entity` IS A STRING` (a body corporate incorporated outside Singapore), so that those two rules can use the core's `Party`.
After registration the rules use the core's `Company`, `Registrar`, `Individual` and `Officer` as they are.

Not a missing type but a keel question, recorded in NOTES.md finding 4: the keel's `s 4(1) "private company"` has three limbs (lines 1622 to 1631 of the text) and none for a company registered by transfer, which s 359(3)(c) ("where applicable, a private company") would need; this encoding takes the fact as an input.
