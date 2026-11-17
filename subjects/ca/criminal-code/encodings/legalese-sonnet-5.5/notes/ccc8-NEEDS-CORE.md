# NEEDS-CORE (ccc8)

What this part wanted from `ccc-core.l4` and `ccc-definitions.l4` and did not find, for the lead to hoist at the merge. Nothing here blocks a check: each item has a stand-in under this part's own prefix.

## Party constructors

The core `Party` has no constructor for a practitioner, a pharmacist or an association, so these regulative rules declare local party types under their section label:

- `s 204 party` (ccc8-part7-pari-mutuel.l4): a person or association that uses or operates a pari-mutuel system; an association operating one. Wanted in core `Party`: `a person or association using a pari-mutuel system`, `an association operating a pari-mutuel system`.
- `s 241.2 party` and `s 241.31 party` (ccc8-part8-maid.l4): a medical practitioner or nurse practitioner; a person responsible for preliminary assessments; a pharmacist or pharmacy technician. Wanted in core `Party`: `a medical practitioner or nurse practitioner`, `a pharmacist or pharmacy technician`, `a person responsible for preliminary assessments`.
- The other regulative rules in this part use the core `Party` (`the accused`, `the court`, `a judge`, `a peace officer`) as it is.

## One constructor declared in two enumerations (finding F-4 in NOTES.md)

`ccc-definitions.l4` declares `a person in a capacity that is none of those` in both `s 2 peace officer capacity` and `s 2 public officer capacity`. The stable binary then cannot resolve the bare name ("There are multiple definitions for the identifier"), so nothing outside the keel can pass either constructor. Wanted: rename one, for example `a person in a capacity that is none of those named in the definition of peace officer`.

## Nothing else

No type, constant or constructor of the core was missing for the modules, and no core name was copied: every top-level name of ccc8-* begins with the label of its provision (`s N ...`) or, for the seat, with "Under section N," ("Under sections 197 to 269.1," for the one record type and its helper).
