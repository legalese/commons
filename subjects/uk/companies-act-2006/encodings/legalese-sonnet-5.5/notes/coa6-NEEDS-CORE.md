# NEEDS-CORE (coa6)

One constructor the core lacks, declared meanwhile under my own prefix.

1. A `Fine limit` constructor for "one-tenth of the greater of £5,000 or level 4 on the standard scale" (s 272(7), second wording of the daily default fine, line 3598 of `ukpga-2006-46.txt`).
   Suggested name: `a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`, with fields `fraction of the greater amount` (a NUMBER, 0.1 here), `amount in pounds` (a NUMBER, 5000 here) and `level` (a NUMBER, 4 here).
   Declared in `coa6-private-and-public.l4` as `s 272(7) a fraction of the greater of an amount in pounds and a level on the standard scale`, a constructor of `s 272(7) daily default fine limit`, and used by the record `s 272(7) penalty` (the core's `Penalty` cannot hold it, because its `daily default fine for continued contravention` is a `MAYBE` of the core's `Fine limit`).
   The keel's own `NEEDS-CORE` note mentions a "greater of £500 and one-tenth of level 4" fine (two uses elsewhere in the Act): a different shape, which the lead may hoist under the same constructor if it is generalised.
   If the constructor is hoisted, `s 272(7) the penalty on a person guilty of an offence under section 272` can return the core's `Penalty` and the `s 272(7)` types can be deleted; the two `s 272(7)` pounds functions would then read the core constructor.

Nothing else is needed: level 5 on the standard scale (`a fine not exceeding a level on the standard scale` 5 1), one-tenth of level 5 (`... 5 0.1`) and "a fine" with no stated limit (`a fine without a stated limit`) are core constructors and are used as they are in `coa6-offence-of-failure-to-notify.l4` (s 279M(3)).
The types and constructors declared in my own modules (`s 273(3) body`, `s 273(2)(c) calling`, `s 279G change in the secretaries`, `s 279G notice given`, `s 279H notice given`, `s 279I notice given`, `s 279J(1) item of the required information about an individual`, `s 279J(3) name`, `s 279K(1) item of the required information about a body corporate or firm`) are specific to Part 12 and need no hoisting.
