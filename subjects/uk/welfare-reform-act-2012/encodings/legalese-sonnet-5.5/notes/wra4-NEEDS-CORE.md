# NEEDS-CORE (wra4)

Constructors this part wanted from the core and did not find, for the lead to hoist.
Nothing here blocks anything: each is covered by a small type under the wra4 prefix, so the merge can keep those types or replace them.

## `Authority` (wra-core.l4)

The core type has nine constructors: the Secretary of State, an authorised person, an employment officer, Her Majesty's Revenue and Customs, a local authority, the First-tier Tribunal, the Upper Tribunal, a court, and the Director of Public Prosecutions.
This part names three bodies the text gives a function to that are not among them:

| wanted | where the text names it | what wra4 did instead |
| --- | --- | --- |
| the Department (a Northern Ireland Department: the Department for Communities, the Department of Finance, the Department for the Economy) | s 120 inserting TCA 36A(2)(b)(ii) "the Department (within the meaning of that Act)", that Act being the Social Security Administration (Northern Ireland) Act 1992 (line 2039); s 127(3)(b), (4) and (7) "Northern Ireland Department" | `s 120(2) TCA 36A(2)(b) body` (constructor `... the Department within the meaning of the Social Security Administration (Northern Ireland) Act 1992`) and `s 127(7) department` (three named departments and `some other department`) |
| the Northern Ireland Housing Executive | s 120 inserting TCA 36A(2)(b)(ii) | `s 120(2) TCA 36A(2)(b) body` (constructor `... the Northern Ireland Housing Executive`) |
| the Treasury | s 120 inserting TCA 36A(8) (line 2050) and 36C(9) (line 2121): "The Treasury may by order amend ..."; and the "benefit offence" definitions (lines 2053, 2108): "committed on or after the day specified by order made by the Treasury" | not a constructor: the order-making powers are inert (reason 2) and the one date the Treasury specifies is an input (`the day specified by the Treasury by order`, a `MAYBE DATE`) |

Adding `a Northern Ireland Department`, `the Northern Ireland Housing Executive` and `the Treasury` to `Authority` would let `s 120(2) TCA 36A(2)(b) body` and `s 127(7) department` be dropped in favour of the core type.
A part cannot add a constructor to a core type from its own module, which is why this part declared its own.

## Nothing else

No core type was missing a field.
No constructor meaning "the text says no" or "not covered" was borrowed from the core: each is a constructor or a `NOTHING` under the wra4 prefix.
