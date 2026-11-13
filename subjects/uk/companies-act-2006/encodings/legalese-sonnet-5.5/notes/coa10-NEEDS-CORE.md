# NEEDS-CORE (coa10)

## Needed: a `Fine limit` constructor for "the greater of an amount in pounds and a level on the standard scale"

Where: s 451(4), the second text printed at line 6128 of `ukpga-2006-46.txt`: "a daily default fine not exceeding one-tenth of the greater of £5,000 or level 4 on the standard scale".
What the core has: `Fine limit` (coa-core.l4, line 200) offers `a fine without a stated limit`, `a fine not exceeding the statutory maximum` (with a fraction), `a fine not exceeding a level on the standard scale` (with a level and a fraction of the level) and `a fine not exceeding an amount in pounds`.
None of them says "the greater of an amount in pounds and a level, times a fraction", and `Penalty` holds its daily default fine as a `Fine limit`, so the core's `Penalty` cannot carry this text.
What coa10 did instead: it declares its own `s 451 daily default fine limit` (two constructors, one per printed text) and `s 451 the penalty in the second text`, so that the first text uses the core's `Penalty` and the second does not.
Constructor wanted, for the lead to hoist (the name is the lead's to choose; the shape is what s 451(4) needs):

```
`a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`
    HAS pounds IS A NUMBER, level IS A NUMBER, `fraction of the greater` IS A NUMBER
```

Once it exists, coa10's `s 451 daily default fine limit` and `s 451 the penalty in the second text` can be deleted and `s 451(4) the penalty in the second text` can return the core's `Penalty`.
One more constructor would have saved this part a small type of its own: the core's `Party` has `Secretary of State` and `Registrar` (coa-core.l4, lines 85-101) but no party for a person authorised by the Secretary of State under s 457, who may be the applicant under s 456(1)(b).
coa10 declares `s 456 party` (`s 456 the applicant`, standing for either applicant, and `s 456 the registrar`) for the one regulative rule that needs it (s 456(7)), so nothing in the core is needed for the part to run.
The constructor wanted is `Person authorised under section 457` in `Party`; the entry is a note for the lead, not a blocker.
