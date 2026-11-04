# NEEDS-CORE (snap6)

Types and constructors the keel's `snap-core.l4` lacks, which snap6 needed.
A part cannot extend a core type from another module (BRIEF.md), so snap6 used the nearest core constructor or a plain input, and says which.
For each, the lead may hoist the constructor into `Party` at the merge; snap6 does not depend on it, and would change only the party named in the regulative rules.

## `Party` constructors wanted

| constructor wanted | what the text says | where | what snap6 did instead |
| --- | --- | --- | --- |
| the State (as a government, apart from the agency that runs the programs) | "a State", "Each State that has elected", "Any State that establishes", "the State shall" | s 2026(d)(2)(D), (d)(4), (l), (n)(4)(B); s 2031(b)(6), (b)(7), (b)(10), (b)(13), (i); s 2035(e)(2), (e)(3)(A) (fork FR-26-1, FR-31-5, FR-35-1) | rules name `the State agency` |
| the Administrator of the Food and Nutrition Service | "the Administrator" | s 2036a(c)(3)(A)-(B), (c)(9) (fork FR-36a-2) | rules name `the Secretary` |
| the Comptroller General | audits and a report | s 2031(f) | decision functions over facts, not rules |
| the Committee on Agriculture of the House of Representatives, and the Committee on Agriculture, Nutrition, and Forestry of the Senate | the Secretary "shall notify", "shall report to", "shall submit to" them | s 2026(b)(1)(D)(iii), (b)(2)(F), (c), (e), (k)(4)(B), (m)(4), (n)(7); s 2031(f)(2); s 2036a(c)(9) | the Secretary's duty is a rule; that the Committees received the report is a fact input or a date input |
| the Secretary of Health and Human Services | approves the application; is consulted; receives the audit | s 2026(m)(1); s 2031(a)(2), (f)(2) | a `MAYBE BOOLEAN` or `BOOLEAN` input |
| a private nonprofit entity that is a grantee | "eligible private nonprofit entities", a "public food program service provider", "a tribal organization" | s 2034(b)(1), (c) (fork FR-34-1) | `s 2034 kind of entity`, a type of snap6's own, and facts as inputs |
| a local agency, an institution, a facility such as a data consortium, and a contractor | "States, State agencies, local agencies, institutions, facilities such as data consortiums, and contractors" | s 2026(l) | `s 2026 participant`, a type of snap6's own, asked as a choice |

## Types or constructors in snap6's own modules that the lead may hoist

Each begins with its section label, as BRIEF.md requires, so none collides.

- `s 2026 participant` (seven constructors): the parties of s 2026(l).
- `s 2034 kind of entity`: the entities of s 2034(c).
- `s 2031 relationship to the minor child` (seventeen constructors): the relatives of s 2031(j)(3), which s 2012 and s 2014 may also need for "child" and "household".

## `Kind of decision`, `Period of ineligibility`

Nothing needed.
