# A New Tax System (Goods and Services Tax) Act 1999 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `gst-registration.l4`, holds the rules and the exported questions (each
with `@export` and `@desc`). One case file, `gst-cases-registration.l4`, is built by
the scratchpad generator `gen_a-new-tax-system-goods-and-services-tax-act-1999_baseline.py`.
Its expected values were written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

A New Tax System (Goods and Services Tax) Act 1999, Compilation No. 96, compilation
date 1 January 2026, includes amendments up to Act No. 72, 2025 (Register id
C2026C00081), as deposited at `../../registers/source-bundle/C2004A00446.txt`.

The A New Tax System (Goods and Services Tax) Regulations 2019 set the higher
registration turnover threshold that s 23-15(1)(b) allows ("such higher amount as
the regulations specify"). They are **not deposited**. That amount is therefore an
input. The cases use $75,000, and $150,000 for a non-profit body. Both life
scenarios state $75,000; it was not read from any deposited text. The same goes
for the s 29-80 low-value limit: "$50, or such higher amount as the regulations
specify". It is an input, and the cases use $50.

## Checks

- `gst-cases-registration.l4`: 68 assertions written, 68 satisfied, 0 errors, 0 warnings.
- `gst-registration.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The sole trader or business owner.** The Act puts the duty to register on the
entity that carries on the enterprise. The s 23-5 note says: "It is the entity that
carries on the enterprise that is required to be registered (and not the
enterprise)". For Jake, a sole trader, that entity is Jake himself. For Daniel it is
his company, Jarrah Legal Technologies Pty Ltd, and he asks the questions as its
owner. The questions are phrased as that person asks them:

- `Must I register for GST`
- `Am I required to be registered`
- `Am I carrying on an enterprise`
- `What is my registration turnover threshold`
- `What is my current GST turnover`
- `What is my projected GST turnover`
- `Do I supply taxi travel`
- `By when must I apply to register`
- `Is my supply a taxable supply`
- `How much GST must I pay on my supply`
- `Is my purchase a creditable acquisition`
- `How much input tax credit do I get`
- `Can I claim the credit in this return`
- `By when must I give a tax invoice`
- `What is my net amount`
- `Must I lodge a GST return`
- `By when must I lodge my quarterly return`
- `By when must I lodge my monthly return`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as
  the deposit allows. The GST Regulations 2019 are not deposited, so the amounts
  they specify are inputs.
- **The actors the text names.** Followed: the entity, the recipient of its supplies,
  the supplier of its acquisitions, and the Commissioner.
- **A judgment handed to someone else, answered conditionally.** Followed for
  s 188-10(1)(a): whether "the Commissioner is satisfied that your projected GST
  turnover is below the turnover threshold" is an input.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.**
  - Worked out from facts: enterprise (s 9-20, paragraphs (a) to (c) and the
    (2)(a) to (c) exclusions), current and projected GST turnover, meeting the
    threshold, taxi travel (s 195-1), taxable supply, value, creditable acquisition,
    creditable purpose, and net amount.
  - Asked as facts: "business" in its ordinary sense, "taxi" and "limousine"
    (neither is defined), "non-profit body", how much of a supply is GST-free or
    input taxed, whether a supply is connected with the indirect tax zone, and
    whether the supply made to me is a taxable supply (that depends on the
    seller).
- **One case is the text's natural unit.** Followed: one entity at one time in one
  month, which is the frame s 188-15 and s 188-20 use. One supply, or one
  acquisition, for the supply rules.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. There is one departure, a
  reconstruction rather than an omission. The deposit drops three formulas that are
  set as images: s 9-75(1), s 11-30(3) and s 17-5(1). Each is rebuilt from what
  survives, and each is labelled INFERENCE (see findings 4 to 6).

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| jake k043 (2028-10-20), first tax return as a sole trader, $31,000, riding an e-bike for a food-delivery platform | `Must I register for GST` | `Not required, but I may register`. His GST turnover is $31,000 current and projected, below $75,000. Delivering food is not "taxi travel", so s 144-5 does not reach him. Neither registered nor required, his deliveries are not taxable supplies: no GST, no return, no input tax credit for his e-bike. |
| daniel d049 (2032-10-01), "GST registration when turnover reaches $75,000", for Jarrah | `Must I register for GST`; `By when must I apply to register` | `Required to be registered: my GST turnover meets the threshold`. $75,000 is "at or above" $75,000. Jarrah must apply by 22 October 2032 (s 25-1). It is illustrated after that with an $11,000 sale (GST $1,000), a $3,300 laptop (credit $300), a net amount of $700, and a December-quarter return due 28 February 2033. |

The cases assume three things the scenarios do not state:

- Jake's takings are $31,000 over the 12 months behind him and the same over the 12
  ahead. Nothing in his scenario says he carries passengers.
- Jarrah's current GST turnover reaches exactly $75,000 on 1 October 2032, and its
  projected turnover is $90,000.
- Jarrah was unregistered until then.

## Why this scope

The seat's question is "Must I register for GST?". Both life events turn on
ss 23-5 and 23-15, so the baseline covers:

- the registration test in full: enterprise, the threshold, current and projected
  turnover with their exclusions, the Commissioner's projection, the taxi rule, and
  voluntary registration;
- the 21-day duty to apply;
- what registration then means for the person: which supplies bear GST and how
  much, which purchases give a credit and how much, the net amount, and when
  returns and payments are due.

Left out, as not needed by the seat or the events:

- Chapter 3 beyond a stated fact: which supplies are GST-free or input taxed
  (Divisions 38 and 40) is asked, not worked out.
- Chapter 4's special rules: GST groups, branches, non-residents, the margin scheme,
  second-hand goods, gambling, annual tax periods and instalments.
- Importations, adjustments, cash accounting, and attribution beyond s 29-10(3).
- Date of effect and backdating (s 25-10), and cancellation (Subdivision 25-B).
- Monthly tax periods by election or determination (ss 27-10, 27-15). Whether
  they apply is the person's own knowledge; a separate due-date question covers
  them.
- The machinery.

## What the Act turns out to say

1. **The Act's own threshold is $50,000, not $75,000.** Section 23-15 says "$50,000;
   or such higher amount as the regulations specify" ($100,000 for a non-profit
   body). The $75,000 everyone quotes comes from the regulations, which are not in
   this deposit. Without them, a business on $60,000 is required to register.
   Asserted.
2. **Taxi travel is passengers, by taxi or limousine, for fares.** Section 195-1:
   "travel that involves transporting passengers, by taxi or limousine, for fares".
   Section 144-5 then requires registration "regardless of turnover". Jake carries
   food on an e-bike, so the rule does not reach him. Whether a ride-sourcing car
   counts as a "taxi" is not settled anywhere in the deposited text. The encoding
   asks it as a fact, and the answer turns wholly on that fact. Asserted.
3. **Turnover is tested both backwards and forwards.** The backward test is the 12
   months ending at the end of this month (current turnover). The forward test is
   this month and the next 11 (projected turnover). Either can trigger
   registration, but the backward test fails if the Commissioner is satisfied the
   forward one is below (s 188-10(1)). Input taxed and offshore supplies are left
   out. A capital asset sale, or winding down, is left out of the projection only
   (s 188-25). Asserted.
4. **Value is price x 10/11 (INFERENCE).** The deposit drops the s 9-75(1)
   formula, but the section's example survives: a $22,000 car has a value of
   $20,000 and GST of $2,000. GST is therefore one eleventh of a GST-inclusive
   price. Asserted.
5. **A supply that bears no GST counts at its full price in turnover.** Section
   188-30 takes it at "11/10 of what would be the value of the supply if it were a
   taxable supply", which is 11/10 of 10/11 of the price. So the same $77,000 of
   takings counts as $77,000 for a person not registered, but as $70,000 for a
   registered person who charges GST inside that price. The Act has a circle here:
   a supply is taxable only if the person is "registered, or required to be
   registered" (s 9-5(d)), and that depends on turnover. The encoding breaks the
   circle by treating an unregistered person's supplies as not taxable for the test
   (INFERENCE). Asserted.
6. **The partly creditable formula and the net amount formula are dropped
   (INFERENCE).** Section 11-30(3) defines "full input tax credit", "extent of
   creditable purpose" and "extent of consideration", but its formula is an image.
   It is taken as the product of the three: a $1,100 phone used 60% for the
   business gives $60. Section 17-5's formula is also an image. It is taken as GST
   minus input tax credits, because s 7-5 says they are "set off against each
   other". A negative result is a refund. Asserted.
7. **A company needs no expectation of profit to carry on an enterprise.** The
   s 9-20(2)(c) exclusion, "without a reasonable expectation of profit or gain",
   applies only to individuals and partnerships of individuals. Asserted.
8. **The deadlines.** Apply within 21 days of becoming required (s 25-1). Give a
   tax invoice within 28 days of a request (s 29-70(2)). A quarterly return and
   payment are due on the 28th of the second month after the quarter, except the
   December quarter, which is due 28 February (ss 31-8, 33-3). A monthly return is
   due on the 21st of the next month (s 31-10). All asserted. The s 25-1 duty is
   also written as a regulative rule.
9. **Small purchases need no tax invoice.** Without a tax invoice, a credit waits
   for the first return lodged while holding one (s 29-10(3)). That rule does not
   apply where the value is $50 or less (s 29-80(1)), so a $55 purchase qualifies
   and a $56 one does not. Asserted.

A note on the binary, not the law: a first draft gave a wrong turnover figure, which
was put down to chained MINUS being read right to left. A later check on the stable
`l4` (1.6.98) found chained MINUS left-associative (`10 MINUS 3 MINUS 1` is 6, also
across lines, with function calls and with record fields), so the cause lay elsewhere.
All arithmetic in the module is fully parenthesised for readability.

## What would need doing before this is worth anything

- Deposit the A New Tax System (Goods and Services Tax) Regulations 2019, and read
  the reg 23-15.01 threshold (and the s 29-70 and s 29-80 amounts) from them
  instead of taking them as inputs.
- Recover the three dropped formulas (ss 9-75(1), 11-30(3), 17-5(1)) from an
  edition that carries them, and check the reconstructions.
- Decide whether to encode Divisions 38 and 40, so that "GST-free" and "input
  taxed" are worked out rather than asked.
- Settle the s 9-5(d) / s 188-30 circle against ATO practice or case law, and the
  meaning of "taxi" for ride-sourcing (neither is in the deposit).
- Add s 25-10 (date of effect, the 4-year backdating limit) for a person who
  registers late.
- An independent test pass, and the human gates.
