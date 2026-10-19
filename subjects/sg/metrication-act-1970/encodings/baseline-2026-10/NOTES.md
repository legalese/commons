# Metrication Act 1970 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design defaults
ruled on 2026-10-18. No `REFUSE`. No pipeline, no coverage table, no independent test pass,
no human gate. Not for public use as advice.

It replaces the encoding moved to `solutions` (Litigate.4) on 2026-10-19. That encoding's notes
were read for scope and pitfalls; none of its L4 was copied.

**Edition:** 2020 Revised Edition, incorporating all amendments up to and including
1 December 2021, in operation 31 December 2021, as deposited at
`../../registers/source-bundle/MA1970.txt`. The legislative history records one later
instrument, G.N. No. S 22/1989 (a rectification of what is now the Fourth Schedule), already
in the text.

**Checks:** one module (`ma-units.l4`), one case file (`ma-cases-units.l4`), 59 assertions
satisfied, 0 errors, 0 warnings, with the stable `l4` of VS Code extension 1.6.98. Two
deliberately wrong assertions were run separately to confirm that a failure is reported.

## Seat

**A person in Singapore who measures, or is given a measurement, in some unit** — a trader,
a buyer, a party to a document, anyone subject to a written law that states a quantity. The
Act has no applicant, accused or licensee; the person it is applied to is whoever uses a unit
and wants to know whether that use counts. The questions are theirs: `Is my unit a unit of the
International System of Units`, `Does my use of this unit have legal force`, `What is my
measurement in SI units`, `Is the order converting my written law one s 4 allows`, `Can what I
did be challenged only because of the unit I used`.

The 2026-10-18 defaults:

- **The Act alone, with instruments that set its numbers brought in.** Followed. The numbers
  are in the Act's own Schedules. No order under s 4 and no notification under s 6 is deposited,
  so the date of the order relevant to a person's act is an input.
- **The actors the text names.** Followed: the Minister (ss 4, 6) appears only through what an
  order means for the person.
- **A judgment handed to someone else answered conditionally.** Followed: s 4(1)(b)'s
  approximation "as appear to the Minister desirable" is the input `the approximation appears to
  the Minister desirable for convenient terms`.
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.** Followed:
  "International System of Units" (s 2(1)) is computed from the Schedules. Whether the subject or
  context of another written law excludes the Fourth Schedule units, and whether another system of
  units is "lawfully used" (s 7(2)), are readings of other law, asked as facts.
- **One case is the text's natural unit.** Followed: one unit (and, for s 5, one amount in it);
  one act for s 7(1); one order for s 4.
- **The Act's own terms, each with a plain gloss.** Followed: unit names as the Schedules print
  them, the quantity of each recorded as its gloss.
- **Operative sections in; machinery out.** Followed: s 6 (power to vary the Schedules) and s 1
  are out. s 4 is a power, but it decides what can happen to the law a person is subject to, so it
  is in, from that person's side.

## Why this scope

The Act is seven sections and four Schedules, so it is encoded nearly whole: ss 2, 3, 4, 5, 7 and
every Schedule row. Left out: the long title, s 1, s 6. The Act lays no duty on anyone but the
Minister, so there is no regulative rule.

## What the Act turns out to say

1. **The Act confers force on SI and takes it from nothing.** s 3(1) gives the use of SI "legal
   force and validity" on and after 15 February 1971; s 7(2) says nothing in the Act affects any
   other system "lawfully used in Singapore". Nothing in the Act prohibits a non-SI unit. A metre
   used on 14 February 1971 has no force from this Act unless its use was lawful under another
   system. Asserted.
2. **The Fourth Schedule units are SI only by default.** s 2(1)(b) includes hectare, metric tonne,
   litre and Celsius "unless there is something in the subject or context ... inconsistent" or it
   is "otherwise expressly provided"; the First and Second Schedule units carry no such exception.
   A litre can fall outside SI where a metre cannot. Asserted.
3. **s 5 converts only what the Third Schedule lists.** Three imperial units (yard, pound, gallon)
   and four local customary units (tahil, kati, chhun, chhek). A foot, though plainly a "measure of
   extension", gets no conversion from the Act. s 5 is a permission ("may be converted"), not a
   duty. Asserted.
4. **The Third Schedule is not internally consistent for weight.** 16 tahil at 37.799364 g comes to
   604.789824 g; the kati row gives 0.604790 kg. Both rows say "approximately". The relation of 16
   tahil to 1 kati is not in the deposited text; it is the inference that makes the gap visible.
   The two figures are asserted; the relation is not. Length is consistent: 10 chhun = 374.65 mm =
   0.37465 m = 1 chhek, all "exactly". Asserted.
5. **The yard, pound, chhun and chhek are exact; the gallon, tahil and kati are approximate.** The
   gallon is printed twice, as litres and as cubic decimetres; one row carries both. Asserted.
6. **s 7(1) protects only against the units ground alone, and only for acts before the order.** A
   challenge on any other ground is untouched. An act done on the day the order is made is not done
   "before" it. Asserted.
7. **s 7(1) does not say which order.** "Before the making of any order under section 4" could mean
   the first order of any kind or the order touching the law the act was done under. The encoding
   takes the second, with the order's date as an input, and returns `not covered by this encoding:
   no s 4 order date given` where no date is given. A reading, not the text. Asserted.
8. **A conversion order is within s 4 only in the shape s 4 describes.** It must replace a non-metric reference
   with an SI unit that is equivalent or an approximation the Minister finds desirable for
   convenient terms, and it "must be published in the Gazette". What follows for an order outside
   that shape is not in the Act and is not encoded. Asserted.
9. **The deposited text prints the Second and Fourth Schedules out of column.** From volt down, the
   Quantity column drifts one line from the Unit column (farad against "force", ohm against
   "electric capacitance"); the Fourth Schedule prints units and symbols in separate blocks. The
   encoding pairs them in the order printed. That pairing is an inference from the layout; the farad's quantity
   and the ohm's and Celsius's symbols are tested. Asserted.

## What would need doing before this is worth anything

- The column pairing of the Second and Fourth Schedules should be checked against the SSO page
  itself, not the text extraction.
- No order under s 4 or notification under s 6 has been looked for. Any s 6 notification would
  change the Schedules and so this encoding.
- The fork in s 7(1) (which order) needs a human reading, ideally with case law; none was searched.
- Whether a use is "lawfully used" under another system (s 7(2)) and whether another law's context
  excludes the Fourth Schedule are left wholly to the person; nothing here helps them answer.
