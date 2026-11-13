# NEEDS-CORE (coa28)

Constructors and types I wanted from `coa-core.l4` and did not find.
Each is declared under my own prefix in `coa28-part44.l4` or `coa28-sch1b.l4` instead, as the brief requires, so nothing here blocks the merge; the lead may hoist them.

## Needed by a rule in layer 1 (declared locally)

- **A `Party` for "the person to whom information is disclosed".**
  Core `Party` has `Member`, `Creditor`, `Registrar`, `Secretary of State`, `Court` and others, but no recipient of information and no public authority.
  `s 1281 241A(5)` (the new s 241A(5) of the Enterprise Act 2002) forbids "the person to whom it is disclosed" to use the information for another purpose, and the discloser in s 241A(1) is "a public authority".
  Wanted constructors: `Public authority` and `Recipient of information`.
  Declared locally as `s 1281 241A(5) party` with the one constructor `s 1281 241A(5) the person to whom the information is disclosed`, in `coa28-part44.l4`.
- **Typed actions.**
  Core has one generic action, `Action of a party` (a performer, a recipient and a `STRING`), and no action types.
  A `MUST` or `SHANT` over a `STRING` cannot be told from any other string, so each regulative rule here declares an action type of its own: `s 1281 241A(5) action` (`coa28-part44.l4`), `sch 1B para 1(6) action` and `sch 1B para 11 action` (`coa28-sch1b.l4`).
  Wanted from the core, if the family wants shared actions: `Has regard to the effect on third parties` (the company, sch 1B para 1(6)), `Withdraws a restrictions notice` (the company, sch 1B para 11), `Uses information for a purpose other than the permitted ones` (the recipient, s 241A(5)).

## Wanted only if a merged jural layer names the parties (not used by layer 1)

The jural relations in `NOTES.md` name parties the core `Party` lacks: each House of Parliament, the Treasury, the holder of a relevant interest (sch 1B), a person aggrieved (sch 1B paras 4, 8), the offeror, the offeree company, the board of the offeree company and the employees' representatives (sch 1C).
Layer 1 does not need them as `Party` constructors, because the rules that use a `Party` are the three above and the other provisions are decision functions.
