# NEEDS-CORE (snap5)

What `snap-core.l4` lacks for sections 2025, 2026a and 2028 of the Food and Nutrition Act of 2008, with the name I declared in its place.
Each is declared in my own module under a section-labelled name, so nothing here is needed for my files to run; the lead may hoist them into the core at the merge.

## 1. Places: Puerto Rico and American Samoa

- **Wanted:** two constructors of `Kind of place`: `the Commonwealth of Puerto Rico` and `American Samoa`.
  (Not `Area`: the core's `Area` is the grain of the USDA cost-of-living tables and no table in these sections is for either place.)
- **Why:** section 2028(a)(1): "the term governmental entity means (A) the Commonwealth of Puerto Rico; and (B) American Samoa."
  The core's `Kind of place` has `any other place` only.
- **Declared instead:** `s 2028 place` in `snap5-s2028.l4`, with `s 2028 the Commonwealth of Puerto Rico`, `s 2028 American Samoa` and `s 2028 any other place`.
- **Used by:** `s 2028(a)(1) the place is a governmental entity`; the seat question "Under section 2028(a)(1), is the place where I live one the nutrition assistance block grants go to?".

## 2. Parties

- **Wanted:** constructors of `Party` for the parties these sections put duties on that the core's twelve do not name: `the chief executive officer of a State`, `an administrative law judge`, `the Departmental Appeals Board`, `the Secretary of Health and Human Services`, `the Commonwealth of Puerto Rico`, `American Samoa`.
  (Section 2012(p), line 95, says "Secretary" means the Secretary of Agriculture, so the core's `the Secretary` is not the Secretary of Health and Human Services, who is a different officer in section 2025(k).)
- **Why:** the twelve regulative rules of sections 2025(c)(8), 2025(k)(4) and 2028(b) take a `DEONTIC` actor type, one type per rule, so the actors of one rule cannot be taken from two types.
- **Declared instead:** `s 2025(c)(8) actor`, `s 2025(k) actor` and `s 2028(b) actor` in `snap5-s2025-duties.l4`.
- **Not needed for correctness:** the decision-function twin of each rule takes dates and facts and no actor.

## 3. Nothing else

`Claim` (section 2025(a), the amount of a recovered claim a State may keep) is the only core type my modules import and use, and it fits.
`Individual`, `Household`, `Benefit` and `Kind of decision` were not needed: the three sections concern what a State agency owes the Secretary, what the Secretary owes a State agency, what a Commonwealth must report, and the rules of a few payments, and not a household's allotment (see NOTES.md, "Where PLAN.md and the brief differ").
