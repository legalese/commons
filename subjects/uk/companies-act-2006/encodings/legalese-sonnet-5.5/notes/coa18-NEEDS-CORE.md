# NEEDS-CORE (coa18): what the core lacks, for the lead to hoist

Written 2026-11-12 by part agent coa18.
Status: both entries describe types already declared inside coa18's own modules under the `s 853L` and `s 831(3)` prefixes; nothing in coa18 waits on the core.
How each was checked: `grep -n "Fine limit" coa-core.l4` (lines 200-204) and `grep -n "DECLARE" coa18-part24.l4 coa18-part23-ch1.l4`.

## 1. A fine limit of "the greater of an amount in pounds and a fraction of a level on the standard scale"

- **Where the text needs it:** s 853L(2)(a) and s 853L(6)(a) (lines 11570-11572 and 11576-11577 of `ukpga-2006-46.txt`): "a daily default fine not exceeding the greater of £500 and one-tenth of level 4 on the standard scale".
- **What the core has:** `Fine limit` (`coa-core.l4`:200-204) has four constructors: `a fine without a stated limit`, `a fine not exceeding the statutory maximum`, `a fine not exceeding a level on the standard scale` (level and fraction of the level), `a fine not exceeding an amount in pounds`. None says "the greater of" two amounts, so the pound floor of 500 cannot be written in it.
- **What coa18 declared instead:** `s 853L(2) daily default fine limit` with the constructor `s 853L(2)(a) the greater of an amount in pounds and a fraction of a level on the standard scale` (pounds, level, fraction), and a constructor `s 853L(2)(b) a fraction of a level on the standard scale` for the Scotland and Northern Ireland limb, which the core's `a fine not exceeding a level on the standard scale` could also have carried; and `s 853L(2) penalty`, a copy of the core's `Penalty` whose daily-fine field has that type.
- **What to hoist:** a fifth `Fine limit` constructor, for example `a fine not exceeding the greater of an amount in pounds and a fraction of a level on the standard scale` (pounds, level, fraction of the level).
  Then `s 853L(2) penalty` and `s 853L(2) daily default fine limit` can be deleted from coa18-part24 and the core's `Penalty` used as it is.
- **What the Act does not give:** the number of pounds a level on the standard scale stands for.
  The amount is an input in coa18 (`the pounds that the level on the standard scale named in the limit stands for`, s 853L(2) function `s 853L(2) the daily default fine limit in pounds`).

## 2. One shared type for "Companies Act accounts" and "IAS accounts"

- **Where the text needs it:** ss 831(3), 832, 836, 841 and 844 (lines 11142, 11162, 11241, 11309 and 11357 of `ukpga-2006-46.txt`, found with `grep -n "Companies Act accounts"`) distinguish "Companies Act accounts" from "IAS accounts" (the Act defines both in s 395, which is coa8's range).
- **What coa18 declared:** `s 831(3) kind of relevant accounts` (`coa18-part23-ch1.l4`:22) with the constructors `s 831(3)(a) Companies Act accounts` and `s 831(3)(b) IAS accounts`; ch2 and ch3 import ch1 for it.
- **Why it is listed here:** coa8 (s 395) owns the definitions and may declare its own type for the same distinction; at the merge two parts would then carry two types for one idea.
  The lead may hoist one type into the core and rewrite the two constructors' users in coa18-part23-ch1, ch2 and ch3.
  Nothing breaks if it is not hoisted: the names are prefixed and cannot collide.
