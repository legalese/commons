# NEEDS-CORE: roc7 (Rules of Court 2021, Orders 28 to 33)

One thing the core lacks, found while encoding.

## A years unit in `Time unit`

`roc-core.l4` declares `Time unit` as Days, `Clear days`, `Working days`, Weeks, Months and Hours.
Order 28, rule 15(2)(c) (line 4381 of the text) requires the original paper affidavit to be retained "for a period of 7 years after it is filed".
There is no years constructor, so `roc7-order-28.l4` states the period as 84 months (`o 28 r 15(2)(c) the period of retention in months`).

Wanted: a constructor `Years` in `Time unit`, to be hoisted by the lead; I could not add it from another module.
When it exists, `period length` becomes 7 and `period unit` becomes `Years` in that one constant; nothing else in this row depends on it.
