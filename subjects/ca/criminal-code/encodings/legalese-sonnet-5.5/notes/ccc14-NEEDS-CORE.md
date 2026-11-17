# NEEDS-CORE.md -- ccc14 (Criminal Code, lines 7875-8523: Parts XII, XII.1, XII.2 and XIII)

Written by part agent `ccc14` on 2026-11-16.
Each item is a type, a constructor or a helper this part needed and the core (`ccc-core.l4`) lacks.
This part defined each under its own prefix, so that nothing collides at the merge; the lead may hoist them into the core and then delete the local copy.
Nothing here changes an answer.

## 1. Constructors of `Party` the core lacks

The core's `Party` names the actors of section 2 (offender, victim, peace officer, judge, the Attorney General, the clerk of the court and so on).
Two regulative rules of this part need an actor the core has no constructor for.
Each is a one-constructor type declared in the module that uses it.

| local type | its one constructor | used by | why the core does not have it |
| --- | --- | --- | --- |
| `s 462.42 party` (`ccc14-part122-forfeiture.l4`) | `s 462.42 a person who claims an interest in property that is forfeited to Her Majesty` | `s 462.42(1) the right to apply` (a MAY, WITHIN 30 days of the forfeiture) | "a person who claims an interest in the property" in subsection (1) names a class of claimants, not an office |
| `s 462.48 party` (`ccc14-part122-disclosure.l4`) | `s 462.48 a person to whom information or documents have been disclosed or provided pursuant to subsection (15) or an order made under subsection (3)` | `s 462.48(15) the prohibition on further disclosure` (a SHANT) | "No person to whom information or documents have been disclosed ..." names any recipient, not an office |

If the lead hoists a general constructor (for example `any person`, or `a person who claims an interest in property`), the two local types can go and the two rules can take the core's `Party`.

## 2. An actor the core already has, used for a class

"Every person who executes a warrant" (`s 462.32(4)(b)`, `s 462.321(4)(c)`) is encoded with the core's `a peace officer`, because subsection (1) of each section speaks of "a warrant authorizing a person named in the warrant or a peace officer" to search and seize (ss 462.32(1) and 462.321(1)), so a peace officer is one of the two persons who execute it.
The core has no constructor for "a person named in the warrant"; the rule says what it says about whoever executes, and `a peace officer` stands for them.
If the lead adds such a constructor, those two rules take it.

## 3. Helpers that belong to no provision (hoist candidates)

| name | module | what it does |
| --- | --- | --- |
| `ccc14 both answers hold` | `ccc14-helpers.l4` | strong Kleene AND of two `MAYBE BOOLEAN` answers: a `JUST FALSE` decides it, otherwise a `NOTHING` stays `NOTHING` |
| `ccc14 either answer holds` | `ccc14-helpers.l4` | strong Kleene OR: a `JUST TRUE` decides it, otherwise a `NOTHING` stays `NOTHING` |
| `ccc14 seat includes answer`, `ccc14 seat means answer` | `ccc14-seat.l4` | the seat layer's reading of a yes to an "includes" definition (`JUST TRUE`; a no is `NOTHING`) and of a yes to a "means" definition (`JUST TRUE`; a no is `JUST FALSE`) |
| `ccc14 seat form of the charge`, `ccc14 seat class of the offence`, `ccc14 seat longest term`, `ccc14 seat indictable limb`, `ccc14 seat punishment limbs`, `ccc14 seat the longest term on indictment` | `ccc14-seat.l4` | pure conversions of the seat's plain inputs into the core's `Imprisonment`, `Punishment` and class-of-offence shapes |

## 4. Not a core gap, but the lead will meet it

On the stable builds (1.6.110 and 1.6.109) a `DEONTIC` value cannot be compared in `#ASSERT`, so every regulative rule of this part is run with `#TRACE` and its outcome is written beside the trace; the same duty is also encoded as a decision function that is asserted.
`check.sh` does not see a different `#TRACE` outcome; the traces of this part were compared by hand between the two builds (NOTES.md, "Checks").
