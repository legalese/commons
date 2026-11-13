# NEEDS-CORE (coa22)

Status (2026-11-13): one item. Nothing here has been hoisted into `coa-core.l4`; the part works without it because the type is declared under this part's own prefix.

## 1. A fine of "one-tenth of the greater of a sum and a level on the standard scale"

**What the text needs.** Section 1033(7) (`src:14514`) ends with a daily default fine written "one-tenth of the greater of £5,000 or level 4 on the standard scale", run together on the same line with the earlier wording "one-tenth of level 5 on the standard scale" (finding 1 and fork F14 in `NOTES.md`). The core's `Fine limit` has no constructor for "the greater of a sum and a level on the standard scale", and a constructor of a core type cannot be added from another module.

**What this part declares instead** (`coa22-part31-ch3.l4`, under the section's label):

```
DECLARE `s 1033(7) one-tenth of the greater of a sum and a level on the standard scale` HAS
    `s 1033(7) the sum in pounds` IS A NUMBER
    `s 1033(7) the level on the standard scale` IS A NUMBER
```

used as `` `s 1033(7) the daily default fine on the second wording` `` (the value `... OF 5000, 4`).

**What the lead would hoist.** A constructor of `Fine limit`, for example

```
`a fine not exceeding one-tenth of the greater of a sum in pounds and a level on the standard scale`
    HAS `the sum in pounds` IS A NUMBER, `the level on the standard scale` IS A NUMBER
```

(the fraction one-tenth is part of the name, as in the text; a second constructor would be needed for any other fraction). The pounds a level on the standard scale stands for are not in the Act and stay an input, as for every other `Fine limit`; the function `s 998(4) the amount in pounds of the fine limit` in `coa22-part30.l4` converts the existing constructors to pounds and does not handle this one, which would then need a branch.

**Sections that need it:** s 1033(7) only, in this range. PLAN.md section 3 mentions a "greater of £500 and one-tenth of level 4" fine with 2 uses in the Act and no constructor; that is a differently worded formula, and I have not checked whether it shares a constructor with this one.
