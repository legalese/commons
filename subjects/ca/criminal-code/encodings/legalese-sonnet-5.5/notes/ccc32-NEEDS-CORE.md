# NEEDS-CORE.md (ccc32) -- types and constructors the core lacks

Part ccc32 declared these in its own modules, under its own prefix, because `ccc-core.l4` (read-only here) lacks them. The lead may hoist them into the core at the merge; each is a one-line change at the use site.

## Parties (the core's `Party` type)

| wanted constructor | used as | declared instead, in | why a core constructor would be better |
| --- | --- | --- | --- |
| `the Miscarriage of Justice Review Commission` | the party bound by the duties of Part XXI.1 as replaced by 2024, c. 33, s. 3 (ss 696.3(1), 696.4(1) and (5), 696.5(2) and (6), 696.6(1) and (7)) | `ccc32-nif-xxi1.l4`: `s 696.1 (not in force) the Commission` (type `s 696.1 (not in force) party`) | one cast for every regulative rule across parts; the Commission is also the party of ss 696.71 to 696.8 (other parts: ccc24 for the in-force Part XXI.1 held by the Minister) |
| `a medical practitioner or nurse practitioner` | the party bound by 2021, c. 2, s. 4 (medical assistance in dying, request made before royal assent) | `ccc32-related-2.l4`: `2021 c 2 s 4 a medical practitioner or nurse practitioner` (type `2021 c 2 s 4 party`) | the same people are the parties of ss 241.1 to 241.4 (ccc8) |
| `the relevant Attorney General` | the person the Commission must notify, with the applicant (ss 696.4(5), 696.5(2), (6), 696.6(7)) | not declared: the notice duties are encoded with the Commission as the only duty-bearer and the Attorney General named in the action's words | the core has `the Attorney General`; "the relevant Attorney General" is not defined in the text the part holds |
| `the applicant` (for review) | the person the Commission's duties run to | not declared: the applicant is the accused (the seat), named in the action's words | the core has `the accused` and `the offender`; an applicant may be neither (a person found not criminally responsible) |

## Records and enumerations

None needed. `Provision of the Code`, `Province or territory`, `Mode of proceeding`, `Class of offence`, `Punishment`, `Imprisonment`, `Fine`, `Length of time` and the constants `ten years` and `six months` are used as the core gives them (`Length of time` is read for `ten years` in s 264.01(4); `six months` is used only in tests).

## A suggestion, not a need

A second, FUTURE text of a provision (the "AMENDMENTS NOT IN FORCE" band) is carried here by the marker `(not in force)` in each name, because the core has no notion of a provision's version. If the merge wants one answer for "this section as it reads today" and "as it will read", a `Version of a provision` type in the core (in force, not in force with the amending provision named) would let a caller ask for either; this part has not built it.
