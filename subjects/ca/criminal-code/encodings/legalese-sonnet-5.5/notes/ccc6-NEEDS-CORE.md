# NEEDS-CORE.md (ccc6)

Constructors that this part wanted in the core and did not find, for the lead to hoist.
Read against `ccc-core.l4` as it stands in this folder on 2026-11-16 (`DECLARE Party`, line 49).

## `Party` (ccc-core.l4, line 49)

The regulative rules of ss 164 to 164.3 (`ccc6-seizure.l4`) name three parties the core's `Party` has no constructor for.
This part declared a type of its own for them, `ss 164 to 164.3 party` (`ccc6-seizure.l4`, line 131), because a constructor cannot be added to a core type from another module.

| constructor wanted in `Party` | where this part uses it | the text |
| --- | --- | --- |
| the custodian of a computer system | `s 164.1(5.1) the custodian's duty to delete the intimate image` (`ccc6-seizure.l4`, lines 349-355), MUST `s 164.1(5.1) delete the material` WITHIN 48 | s 164.1(5.1) (src:3321), s 164.1(1) |
| a person who claims an interest in the thing forfeited | the `s 164.3(1)` rule (PARTY at `ccc6-seizure.l4`, line 529) | s 164.3(1) (src:3347) |
| the applicant for relief from forfeiture | the `s 164.3(3)` rule (PARTY at `ccc6-seizure.l4`, line 564): the applicant "shall cause notice ... to be served on the Attorney General" | s 164.3(3) (src:3351) |

Also named in the text, not used as a party of a rule: the occupier of the premises (s 164(2), "issue a summons to the occupier of the premises", src:3268); the rule's party is the judge, so the occupier is named only in the act's text.

The fourth constructor of `ss 164 to 164.3 party`, `ss 164 to 164.3 the judge`, is not a gap: the core's `a judge` ("a judge of the court that the provision in question names") would serve, and this part kept one type for the four parties of the section.

## Nothing else

No other core type lacked a constructor or a field this part needed: `Punishment`, `Length of time`, `Class of offence`, `Provision of the Code` and `Province or territory` are used in layer 1 as the keel declared them (grep of the `ccc6-*.l4` modules, 2026-11-16).
