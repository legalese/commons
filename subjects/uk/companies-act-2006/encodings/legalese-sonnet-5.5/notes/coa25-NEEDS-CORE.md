# NEEDS-CORE (coa25)

The core (`coa-core.l4`) was not edited. This part declared the following under its own prefix because the core lacks them; the lead may hoist any of them at the merge (each is used by the sections named).

| what the core lacks | declared here as | sections that need it |
| --- | --- | --- |
| `Party` constructors for the persons a regulative rule names: the valuer; an officer of the company (as the person a valuer questions); a judicial factor; the Charity Commission; the Charity Commission for Northern Ireland; the Regulator of Community Interest Companies; the applicant for approval of a business name; the person issuing out process; the person to whom Chapter 2 of Part 41 applies | `s 1150 party` (the valuer, an officer), `s 1154 party` (judicial factor, the two Commissions, the Regulator), `s 1195 party`, `s 1139 party`, `s 1202 party` | ss 1139(4), 1150(4), 1154, 1155(1), 1195, 1202, 1204 |
| a typed list of "the court" for each part of the United Kingdom (the core has the generic `Court` party only) | `s 1156 court`, `s 1183 court` (two identical lists: s 1156(1) and s 1183 each define "the court", for the Companies Acts and for Part 40) | ss 1156(1), 1183 |
| an instant (a day and an hour of the day) for periods counted in hours | `s 1147 instant` | s 1147 |
| a way to say "the general limit in a magistrates' court" as a period (the Act does not state it) | a plain NUMBER of months, asked as an input; no type | ss 1186(2), 1191(2) |
| a kind of direction to change a company's name (ss 67, 75, 76, 76A, 76B) | `s 1198A direction` | ss 1198A(5), 1198B(7) |

No constructor of a core type was needed beyond these; `Penalty`, `Fine limit`, `Mode of conviction`, `Period`, `Unit of time`, `Form of document` and `Place of registration` were used as the core declares them.
