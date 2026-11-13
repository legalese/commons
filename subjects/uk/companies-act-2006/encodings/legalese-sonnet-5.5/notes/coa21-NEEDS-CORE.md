# NEEDS-CORE (coa21): types and constructors the core lacks

Part coa21, Companies Act 2006, ss 942 to 993.
Each item names what was wanted, where it was needed, and the own type this part declared instead (every name begins with its section label, so nothing collides at the merge).
The lead may hoist any of them into `coa-core.l4`; if one is hoisted, the own type below can be replaced by the core's.

1. **Party constructors for "a person" and for "the offeror".**
   The core `Party` (`Company`, `Director`, `Member`, `Takeover Panel`, and so on) has no constructor for an arbitrary person required to act by a Panel notice (s 947) or for the person making a takeover offer (ss 981 and 984).
   Own types: `s 947 party` (`s 947 the person required by the notice`), `s 981 party` (`s 981 the offeror`) and `s 984 party` (`s 984 the offeror`), each with its own action type (`s 947 act`, `s 981 act`, `s 984 act`).
   The regulative rule in `coa21-ch2-opting-in.l4` (s 970) uses the core's `Company`, `Takeover Panel` and `Action of a party`.
2. **A "greater of an amount and a level" daily default fine.**
   The core `Fine limit` has `a fine not exceeding the statutory maximum`, `... a level on the standard scale` and `... an amount in pounds`, but no variant for "one-fiftieth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale" (s 980(8)(b)(i) and s 984(7)(b), fork F2).
   Own type: `s 980(8) daily default fine limit` with two constructors (a fraction of the statutory maximum; a fraction of the greater of an amount in pounds and a level), and, because the core `Penalty` types its daily fine as `MAYBE Fine limit`, a record `s 980(8) penalty` with the same fields as `Penalty` and the own limit type for the daily fine.
   The wanted core change: a `Fine limit` constructor `a fine not exceeding the greater of an amount in pounds and a level on the standard scale`, taking a fraction, the pounds and the level.
