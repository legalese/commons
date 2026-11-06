# NEEDS-CORE (roc6)

Two things the core (`roc-core.l4`) lacks and that Orders 23 to 27 needed.
Neither blocks the encoding: each has a workaround that passes every assertion on 1.6.109 and 1.6.108, so these are requests for the lead to weigh, not defects.
I did not edit the core.

## 1. `Years` in `Time unit`

`Time unit` has `Days`, `Clear days`, `Working days`, `Weeks`, `Months` and `Hours` (`roc-core.l4`, `DECLARE \`Time unit\``).
It has no years.
Order 27 states two periods in years: rule 13 ("a period of 4 years or more") and rule 14(1) ("a period of 6 years and upwards").
These are not periods that run from an event to a deadline (the core `Period` says how long an act may take); they are ages of an account, so a `Period` would be the wrong shape even if `Years` existed.
Workaround, in `roc6-order-27.l4`: a plain NUMBER constant named for the rule (`o 27 r 13 the number of years` is 4, `o 27 r 14(1) the number of years` is 6) and a comparison with a NUMBER of years the asker states.
What would help: a `Years` constructor in `Time unit` only if some part states a period that runs in years from an event; if no part does, nothing is needed.

## 2. A reference to a rule

The core has no type for "Rule 4(2)" or "Rules 1 to 11".
Order 23 rules 12(1), 13(1) and 14(1) say "Rules 1 to 11 (except Rule 7(1) and (2)) apply to committal proceedings before a tribunal"; Order 25 rule 3(3)(b) and (c) say "within the time in Rule 4(2)" and "within the time in Rule 8(4)".
Workaround, in `roc6-order-23.l4`: a rule number and a paragraph number, both NUMBER inputs (`o 23 r 12(1) Rules 1 to 11 apply to committal proceedings before a tribunal` takes `rule` and `paragraph`); in `roc6-order-25.l4`: rule 3(3)(b) and (c) take the last day of the period as a DATE input counted by Order 3, Rule 3, and the name of the function says which rule's time it uses.
This is the same gap as the keel's finding 3 (a table keyed by two strings, `order number` and `rule number`), seen from a second range.
What would help: one record type with an order, a rule and a paragraph, declared once in the core, so that "Rules 1 to 11 except Rule 7(1) and (2)" is a range of those and not a pair of numbers.

## Not a need: officials in regulative rules

Each Order declares its own `o N party` and `o N act` types for the `PARTY ... MUST ... WITHIN` rules (for example `o 27 the Accountant-General`).
The core has `The Registrar` among its decision makers (`Decision maker`) but no type for the Sheriff, the Accountant-General or the Attorney-General as parties to a duty.
This works without the core and collides with nothing, because each name carries its Order's label; it is recorded so that the lead can see that a part which needs the Sheriff declares its own.
