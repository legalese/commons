# NEEDS-CORE (coa2)

What this part wanted from the core and did not find.
Nothing was added to or extended from the core: the keel's `coa-core.l4` and `coa-definitions.l4` are untouched.

## 1. A `Fine limit` constructor for "the greater of an amount in pounds and a level on the standard scale"

Wanted by s 63(3) and s 64(6) (lines 701 and 728): "... a daily default fine not exceeding one-tenth of the greater of £5,000 or level 4 on the standard scale."
The core's `Fine limit` (`coa-core.l4`, line 200) has four constructors: `a fine without a stated limit`, `a fine not exceeding the statutory maximum` (fraction), `a fine not exceeding a level on the standard scale` (level, fraction of the level) and `a fine not exceeding an amount in pounds` (pounds).
None can say "the greater of £5,000 or level 4".

Suggested constructor (not declared here, because a name in another module's type cannot be extended):

```
`a fine not exceeding the greater of an amount in pounds and a level on the standard scale` HAS pounds IS A NUMBER, level IS A NUMBER, `fraction of the greater` IS A NUMBER
```

What this part did instead: the daily default fine in `Penalty` is `NOTHING` for s 63(3) and s 64(6) (the text as rendered gives two wordings and does not choose: NOTES.md, fork 1), and each wording is a `NUMBER` function of the levels, under this part's prefix:
`s 63(3) the daily default fine in pounds on the first wording`, `s 63(3) the daily default fine in pounds on the second wording`, `s 64(6) the daily default fine in pounds on the first wording`, `s 64(6) the daily default fine in pounds on the second wording`.
If the core gains the constructor and the lead decides which wording stands, the two functions fold into the `Penalty` value.

## 2. Nothing else

No core type or constructor other than the one above was missing for ss 53 to 111.
(A note for the keel, not a need: pattern variables named `level` or `pounds` clash with the core's `Fine limit` field names, "multiple definitions for the identifier"; this part uses `lvl`, `frac` and `amt`.)
