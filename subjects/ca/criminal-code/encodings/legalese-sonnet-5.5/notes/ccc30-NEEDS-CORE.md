# NEEDS-CORE.md -- ccc30: what the core lacks, for the lead to hoist at the merge

Written by part agent `ccc30` on 2026-11-13. Nothing below was added to `ccc-core.l4` (it is read-only in this sandbox). Each item is declared in the part's own module under its own prefix and used there.

1. **`Party`: a constructor for the person a demand, order or summons is addressed to.**
   Wanted: `the person to whom a demand, order or summons is addressed` (the Forms print "To (name of person)", "To A.B.", "To (name of financial institution, person or entity)").
   Why the existing constructors do not do: it is not `the accused` (a preservation demand or a production order goes to a third party, and Forms 5.041 and 5.061 go to a person who may have been found not criminally responsible), not `the offender` (same reason), not `a witness`, and not `an organization` (it may be an individual).
   Declared here as `forms 1 to 23 addressee` (one constructor, `forms 1 to 23 the person to whom the demand, order or summons is addressed`) in `ccc30-forms-actors.l4`. Used by the regulative rules of Forms 5.005, 5.0091, 5.041 and 5.061.
2. **`Process document`: members for the documents Forms 5.001 to 5.0091, 5.1 to 5.3, 8, 12 and 15 to 23 prescribe**, if the lead wants `forms 1 to 23 the process document the form prescribes` to answer them rather than `NOTHING`: a preservation demand, a preservation order, a keep-account-open order, a production order, a non-disclosure order, a warrant for committal, a warrant for a witness, a surety declaration, a report to a justice. The register answers `NOTHING` for them today (silent: the core's list has no member), which is the honest answer and is asserted.
