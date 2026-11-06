# NEEDS-CORE (roc3)

One thing the core lacks, found while encoding lines 1405-2230.

- **`Years` as a `Time unit`.** Order 15, rule 11(11) says the official record of a hearing must be kept for 5 years (`o 15 r 11(11) the time the official record must be kept`).
  The core's `Time unit` has `Days`, `Weeks`, `Months`, `Hours`, `Clear days` and `Working days`, so this row writes the period as 60 months.
  Order 3, rule 3(2) says "month" means a calendar month, so 60 months is 5 calendar years from the same day; a `Years` unit would say so directly and would not depend on that reading.
  The lead may hoist `Years` into `roc-core.l4`; this row would then change one constant and its test.
