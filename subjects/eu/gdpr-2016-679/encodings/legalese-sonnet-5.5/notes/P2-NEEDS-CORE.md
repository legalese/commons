# P2-NEEDS-CORE.md -- what P2 needed from `gdpr-core.l4` and what it declared for itself

P2 edited no keel file (`gdpr-core.l4`, `gdpr-core-2.l4`, `gdpr-definitions.l4`, `gdpr-definitions-2.l4`, their tests).
Checked on 2026-11-26 against `grep -n "^DECLARE" P2-art-*.l4 P2-seat-*.l4` and the imports of the P2 modules.

## Taken from the keel, unchanged

- `Role in the Regulation` (the party of every regulative rule: always `controller`) and `Duty outcome` (the answer of every gated duty), both of `gdpr-core.l4`.
- `Kind of person or body` and `Art 4(9) the body is a recipient` (calls from `P2-art-19.l4`), `Art 5(1)(b) purpose of archiving, research or statistics` (a choice in `P2-art-21.l4`).
- Nothing else is imported from `gdpr-definitions-2.l4`; no P1 module is imported (the seams to P1 are plain inputs, PLAN-P2.md section 4.1).

## Declared by P2 itself (each a candidate for the core only if a later part needs the same type)

| type | module | what it is | would a later part need it? |
| --- | --- | --- | --- |
| `Art 12 action` ... `Art 22 action` (11 types, one per module that has a regulative rule; Art 23 has none) | `P2-art-12.l4` ... `P2-art-22.l4` | the one-constructor or few-constructor action of that Article's regulative rules | no: an action type belongs to the rule it names |
| `Art 13(1) item of information`, `Art 13(2) item of further information`, `Art 14(1) item of information`, `Art 14(2) item of information`, `Art 15(1) item of information` | `P2-art-13.l4`, `P2-art-14.l4`, `P2-art-15.l4` | the items the text lists, one constructor each | maybe Art 28 or Art 30 (a record or a contract that must list matters); they would declare their own |
| `Art 23(1) provision whose scope is restricted`, `Art 23(1) objective safeguarded`, `Art 23(2) specific provision` | `P2-art-23.l4` | the lists of Art 23(1) and (2) | Art 6(4) (P1) takes the answer as a BOOLEAN seam, not the type; Art 89 and Art 85 name Article 23's objectives only in prose |
| `P2 subject answer`, `P2 controller answer` | `P2-seat-subject.l4`, `P2-seat-controller.l4` | yes, no, not sure for a MAYBE a combining rule takes (the seat's helper, as in PLAN.md section 6) | no: every part's seat declares its own |

## What P2 would have wanted from the core and did not get

- **The two role facts.**
  Every right of Articles 15 to 22 needs "the person is the data subject" and "the body is the controller" as plain facts.
  P2 declares them as BOOLEAN inputs of each right function (fifteen functions) because calling `Art 4(1)` and `Art 4(7)` of the keel would add nine inputs to each (finding F-1 in `notes/P2-NOTES.md`).
  A core helper that took the keel's own answers (`MAYBE BOOLEAN`) and returned the one fact would let a later part avoid repeating this: proposed, not built, and not needed for P2's tests.
- **A months-between helper.**
  Arts 12(3), 12(4) and 14(3) count a month with `add months` of `daydate` (31 January plus one month is 28 February, a marginal reading listed in NOTES); P2 calls `add months` directly in three places, all in `P2-art-12.l4` (Art 12(3) twice, Art 12(4)).
  A helper in the core that named the counting rule once would make the choice reviewable in one place: proposed, not built.
