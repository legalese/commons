# NEEDS-CORE -- asked by ssc6

One item.

- **`Labour` needs a field for "the labour resulted in the issue of a child, alive or dead".**
  Section 171(1) (src:3352-3353, "confinement") and the sentence of section 153(12) that repeats it distinguish labour "resulting in the issue of a living child" from labour "after 24 weeks of pregnancy resulting in the issue of a child whether alive or dead".
  The core's `Labour` (ssc-core.l4:244-247) has the weeks of pregnancy when labour began, whether labour resulted in the issue of a living child, and the day of the issue, but no field for whether a child was issued alive or dead, so `s 171(1) she is confined` and `s 171(1) the pregnancy terminated otherwise than by confinement` take it as a separate `BOOLEAN` input named `the labour resulted in the issue of a child, alive or dead`.
  The ssc6 modules work without the field; with it the merge lead can drop the extra input.
