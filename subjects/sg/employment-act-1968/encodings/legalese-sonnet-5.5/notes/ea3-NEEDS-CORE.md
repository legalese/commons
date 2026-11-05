# NEEDS-CORE (ea3)

What ea3 needed from `ea-core.l4` and could not get, and what it did instead, so that the lead can hoist it.

## 1. Two constructors of `Official or body the Act names`

`ea-core.l4:56-71` declares `Official or body the Act names` (from s 3(1), lines 719-722) with the President, the Minister, the Commissioner for Labour, the deputies and assistants, an authorised officer, an inspecting officer, an authorised person, a medical officer, the Comptroller of Income Tax, and the bodies.
Section 124(1)(a) (lines 4929-4934) names two more officials as "relevant authorities": "the Parliamentary Secretary to the Minister" and "the Permanent Secretary to the Ministry of Manpower".
The core has neither (a search of `ea-core.l4` for "Parliamentary" and "Permanent Secretary" finds nothing).

| wanted in `Official or body the Act names` | text | used by |
| --- | --- | --- |
| `Official: the Parliamentary Secretary to the Minister` | s 124(1)(a), line 4929 | `s 124(1)(a) "relevant authority" the person is one` |
| `Official: the Permanent Secretary to the Ministry of Manpower` | s 124(1)(a), lines 4930-4931 | the same |

Done instead (a type of its own, under the ea3 prefix, because a constructor cannot be added to a core type from another module):
`ea3-claims.l4:969-975` declares `s 124(1)(a) Kind of person` with six constructors: the Minister, the Parliamentary Secretary to the Minister, the Permanent Secretary to the Ministry of Manpower, the Commissioner, an inspecting officer, and `s 124(1)(a) some other person`.
If the lead hoists the two constructors, `s 124(1)(a) Kind of person` can be replaced by `Official or body the Act names` and its function re-pointed; no other ea3 rule depends on the type.

## 2. Nothing else

Every other type and constructor ea3 uses is in `ea-core.l4` or `ea-definitions.l4` as shipped:
`Official or body the Act names` (the courts and the Commissioner), `Kind of claimant` (the Second Schedule fee), `Pay for a period` and `Basis of pay`, `Penalty on conviction`, and the definition functions of `ea-definitions.l4` that the Schedules cross-check against.
