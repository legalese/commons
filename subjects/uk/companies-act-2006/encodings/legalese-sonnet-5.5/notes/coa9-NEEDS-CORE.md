# NEEDS-CORE (coa9)

Types or constructors this part needed and the core (`coa-core.l4`) lacks, for the lead to hoist at the merge.
This part declared its own under its own prefix and uses it; nothing here blocks the part.

## 1. A `Fine limit` constructor for "one-tenth of the greater of an amount in pounds and a level on the standard scale"

- **Wanted:** a constructor of `Fine limit`, for example `a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`, with fields `pounds` (NUMBER), `level` (NUMBER) and `fraction of the greater` (NUMBER).
- **Sections that need it:** s 438(4), second version of the daily default fine: "one-tenth of the greater of £5,000 or level 4 on the standard scale" (line 5851 of `ukpga-2006-46.txt`). The PLAN's section 3 records two uses of a "greater of" fine in the whole Act ("greater of £500 and one-tenth of level 4").
- **What this part did instead:** declared `s 438(4) version of the daily default fine` (two constructors: the first version, one-tenth of level 5, and the second) in `coa9-laying.l4`, and a function `s 438(4) the most the daily default fine may be in pounds on the version`. The `Penalty` returned by `s 438(4) the penalty for an offence under section 438` leaves the daily default fine `NOTHING` because the text carries both versions and does not say which is in force (fork F30).

## 2. Nothing else

The core's `Penalty`, `Fine limit`, `Mode of conviction`, `Period`, `Party` and `Unit of time` were enough for every offence and penalty of the range, and no further type or constructor is wanted.
