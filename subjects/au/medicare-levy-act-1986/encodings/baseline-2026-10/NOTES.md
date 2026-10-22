# Medicare Levy Act 1986 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `mla-levy.l4`, holds the rules and the exported questions (each with
`@export` and `@desc`). One case file, `mla-cases-levy.l4`, is built by the
scratchpad generator `gen_medicare-levy-act-1986_baseline.py`. Its expected values
were written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

Medicare Levy Act 1986, Compilation No. 53, compilation date 1 July 2026, includes
amendments up to Act No. 58, 2026 (Register id C2026C00295), as deposited at
`../../registers/source-bundle/C2004A03351.txt`.

**Dated arms (added 21 October 2026).** Two earlier compilations are deposited beside
the current one, retrieved from the Federal Register of Legislation on 21 October 2026:

| File | Compilation | In force | Includes | Figures used for |
|---|---|---|---|---|
| `C2004A03351.2024-03-06.txt` | No. 50, C2024C00076 | 6 March 2024 to 31 December 2024 | Act No. 4, 2024 | 2023-24 |
| `C2004A03351.2025-03-28.txt` | No. 52, C2025C00323 | 28 March 2025 to 30 June 2026 | Act No. 28, 2025 | 2024-25 |
| `C2004A03351.txt` | No. 53, C2026C00295 | from 1 July 2026 | Act No. 58, 2026 | 2025-26 and later |

Which year each set of figures is for is an inference: see finding 1. Compilation
No. 51 (C2025C00013, 1 January to 27 March 2025) carries the same figures as No. 50
and adds s 9A; it is not deposited.

The formulas the text deposit lost (ss 8(2), 8B(2)(b), 8C(3)(b), 8D(4), and the trustee
sections 8E-8G) are transcribed by hand from the Word rendering of the same compilation,
fetched from the Federal Register of Legislation on 2026-10-21, in
`../../registers/source-bundle/C2004A03351.formulas.md`. The encoding uses them.

No instrument sets the Act's numbers. The low-income figures are in its own text
(ss 3, 8 and 8D), and an amending Act changes them each year.

Also used: the Private Health Insurance Act 2007, ss 22-30, 22-35, 22-40, 22-45
and 45-1, as deposited at
`../../../private-health-insurance-act-2007/registers/source-bundle/C2007A00031.txt`.
Section 3A of this Act borrows its income tiers from there, and s 3(5) borrows its
excess limits.

The A New Tax System (Medicare Levy Surcharge—Fringe Benefits) Act 1999 matters
here only for the meaning of "dependant" and "married" in s 3A(3). Those are asked
as facts, so that Act is not encoded.

## Checks

- `mla-cases-levy.l4`: 97 assertions written, 97 satisfied, 0 errors, 0 warnings
  (75 before the dated arms for 2023-24 and 2024-25 were added on 2026-10-21; 68
  before the formulas were recovered the same day).
- `mla-levy.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The taxpayer.** That is the individual on whose taxable income the levy, and any
surcharge, is imposed. The Act addresses no official: every section says what
levy is payable. So every rule is already about the taxpayer, and the questions are
phrased as that person asks them:

- `How much Medicare levy do I pay`
- `Is my income under the threshold`
- `How much levy on my own income`
- `Am I in the family case`
- `What is my family income threshold`
- `By how much is my levy reduced for my family`
- `By how much is my spouse's levy reduced`
- `Must I pay the surcharge`
- `How much surcharge do I pay`
- `Which income tier am I in`
- `Does my policy count as hospital cover`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No
  instrument sets them; the Act's own earlier compilations give the earlier years'
  figures, as dated arms. The surcharge tiers come from the Private Health Insurance
  Act, which s 3A names, and that Act's deposit is used.
- **The actors the text names.** Followed: the person, the spouse, dependants,
  prescribed persons and people entitled to the s 160AAAA rebate. Trustees are left
  out; see "Why this scope".
- **A judgment handed to someone else, answered conditionally.** Nothing in scope
  turns on an official's opinion.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.**
  - Worked out from facts: threshold amount, phase-in limit, family income, family
    income threshold, the s 3(3) married rules, private patient hospital cover
    (s 3(5)), and tier 2 and tier 3 earner (s 3A, through PHI Act s 22-30).
  - Asked as facts: "married" and "spouse" (Part VIIB of the 1936 Act), "dependant"
    (ss 251R, 251V), "prescribed person" (s 251U), "income for surcharge purposes"
    (ITAA 1997), entitlement to the s 160AAAA rebate, the Subdiv 61-A offset and the
    Subdiv 961-A and 961-B notional offsets, and whether family tax benefit was
    payable.
- **One case is the text's natural unit.** Followed: one taxpayer and one year of
  income.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed, with these limits:
  - **The s 8(2) reduction** and **the part-year surcharge formulas** (ss 8B(2)(b),
    8C(3)(b), 8D(4)) are encoded from the sidecar transcription. A part-year surcharge
    is worked out only where no day of the year is a prescribed-person day (the overlap
    of uncovered and prescribed days is not asked) and only one surcharge section
    applies all year; otherwise it is `Not covered by this encoding`.
  - **The PHI Act's indexed tier thresholds** are not deposited, so they are inputs.
    Its s 22-40(4) increase for two or more children, $1,500 x (children - 1), is
    transcribed in the PHI Act's formulas sidecar and worked out in that baseline;
    here the increase is still an input.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| chloe c045, first return, for 2023-24, taxable income $27,500 | `How much Medicare levy do I pay` | **$150**, from Compilation No. 50: $27,500 is $1,500 over the 2023-24 threshold amount of $26,000 and under the $32,500 phase-in limit, so s 7(2) caps the levy at 10% of the excess. Not nil, as the scenario says (finding 12). No surcharge. Under the current figures it would be nil. |
| chloe c048, second return, for 2024-25, taxable income $71,500 | `How much Medicare levy do I pay` | **$1,430**, from Compilation No. 52: above the $34,027 phase-in limit, so the full 2%, matching the scenario's `medicare_levy: 1430`. There is no surcharge: $71,500 is under the singles tier 1 threshold in any year. |

Chloe's hospital cover is not stated in the scenario. The cases assume she has none,
and that her income for surcharge purposes equals her taxable income.

## Why this scope

The seat is the individual taxpayer, and both life events ask only what levy
Chloe pays. The baseline therefore covers what any individual meets:

- the rate;
- the low-income threshold and the shading-in, for ordinary taxpayers and for
  seniors and pensioners;
- the family threshold;
- the surcharge for a person without hospital cover;
- the prescribed-person reduction.

Left out:

- **Trustees** (ss 6(2)-(6), 7(3)-(4), 8E-8G, 10). They are a different seat.
- **s 9A (lump sums in arrears).** It reworks taxable income through 1936 Act
  concepts (s 159ZR). A case with such a lump sum gets
  `Not covered by this encoding`.
- **Machinery:** ss 1, 2, 4, 5 and 11.
- **Rounding.**

This is consistent with the Income Tax Rates Act and ITAA 1997 baselines in this
repository. Both leave the levy to this Act and both use the same taxable incomes
for c045 and c048.

## What the Act turns out to say

1. **The figures carry no year.** Each compilation states each low-income figure
   once. The amendment history shows them amended once a year, each time by an Act
   whose item 14 is an application provision that the compilation does not print:
   - No. 50 (Act No. 4, 2024, in force 6 March 2024): $26,000 / $32,500; seniors
     $41,089 / $51,361; family $43,846 + $4,027, seniors $57,198;
   - No. 52 (Act No. 28, 2025, in force 28 March 2025): $27,222 / $34,027; seniors
     $43,020 / $53,775; family $45,907 + $4,216, seniors $59,886;
   - No. 53 (Act No. 58, 2026, in force 1 July 2026): $28,011 / $35,013; seniors
     $44,268 / $55,335; family $47,238 + $4,338, seniors $61,623.
   The encoding infers, but the deposit does not state, that each set is for the
   year of income in which its Act was made (2023-24, 2024-25, 2025-26) and stands
   for later years until amended. 2022-23 and earlier are `Not in the deposited
   text`. Asserted.
2. **The rate is 2%** (s 6(1)), and it carries no year. Asserted.
3. **Shading-in.** Between the threshold amount and the phase-in limit, the levy
   "shall not exceed 10% of the amount of the excess" (s 7(2)). With the deposited
   figures, 10% of the excess meets 2% at the phase-in limit, to within a few
   cents. Asserted on $31,011 ($300) and $34,011 ($600).
4. **Seniors and pensioners.** For someone entitled to the s 160AAAA rebate, the
   threshold amount is $44,268, the phase-in limit is $55,335 and the family
   threshold is $61,623 (ss 3(1), 8(7)). Asserted.
5. **Single parents.** A single parent's family threshold rises by $4,338 only for a
   child for whom family tax benefit was payable to that parent (s 8(6)). Asserted.
6. **Apportionment between spouses.** Under s 8(3), a married person keeps only the
   share of the s 8(2) reduction that matches their own share of family income.
   Under s 8(4), any part of that share they cannot use reduces their spouse's levy.
   Asserted.
7. **The surcharge's income test and charge use different bases.** The test is on
   income for surcharge purposes, but the charge is a percentage of taxable income:
   1%, 1.25% for a tier 2 earner, 1.5% for a tier 3 earner. Asserted.
8. **A married person with low income of their own pays no surcharge.** Under
   s 8D(3)(c), a married person whose own income for surcharge purposes does not
   exceed $28,011 pays no surcharge, even when the couple's income is over the
   family tier 1 threshold. Asserted.
9. **Hospital cover with a large excess does not count.** A policy whose excess is
   more than $750 a year (one person insured) or $1,500 (any other policy) is not
   private patient hospital cover (s 3(5); PHI Act s 45-1). Asserted.
10. **The tier 1 threshold never falls.** The singles tier 1 threshold was $90,000
    for 2021-22 and 2022-23, and indexation never lowers it (PHI Act ss 22-35,
    22-45(3), (3A)). So an income at or under $90,000 attracts no surcharge in any
    later year. Asserted for c048.
11. **The s 8(2) reduction leaves exactly 10% of the excess.** The formula (recovered
    from the authorised rendering) is 2% of the family income threshold less 0.08 x
    (family income - threshold), and nil once that is negative ("if any"). With the 2%
    levy, a single parent on $50,000 against a $47,238 threshold pays $1,000 - $723.80 =
    $276.20, which is 10% of the $2,762 excess, the same shading-in as s 7(2). The
    reduction runs out when family income passes 1.25 times the threshold. Under s 8(3)
    a married person's share is cut by the spouse's share of family income ($723.80 ->
    $289.52 on $20,000 and $30,000), and s 8(4) passes the unused part to the spouse.
    Asserted.
11a. **The part-year surcharge is the whole-year rate pro rata by days.** ss 8B(2)(b),
    8C(3)(b) and 8D(4) all read (1% of taxable income) x (number of those days / number
    of days in the year), the 1% raised by 0.25 or 0.5 of a point for tier 2 and 3: $200
    for 73 uncovered days on $100,000; $600 for 146 days on $120,000. Asserted.
12. **c045: the scenario's "nil under the threshold" is wrong for 2023-24.** The
    2023-24 threshold amount (Compilation No. 50) is $26,000, not the current
    $28,011. Chloe's $27,500 is $1,500 over it, so s 7(2) gives 10% of $1,500 = $150
    (less than the 2% figure of $550). $27,500 is over the 2024-25 threshold
    ($27,222) as well; it is under only the current $28,011, which the scenario seems
    to have applied. Asserted ($150, and nil under the current figures). Report to the
    scenario's author.
13. **The formulas did not change between 2023-24 and 2025-26.** The equation images
    in the Word downloads of Compilations No. 50 and 52 are byte-identical, and the
    words drawn in them (extracted from the EMF and WMF records) are the s 8(2) and
    part-year surcharge formulas transcribed in `C2004A03351.formulas.md`. The only
    other change across the three texts, apart from the figures, is s 9A, inserted
    from 1 January 2025. Recorded in the `.formulas.md` sidecars of the two dated
    files.

## What would need doing before this is worth anything

- Deposit the amending Acts (No. 4, 2024; No. 28, 2025; No. 58, 2026) and confirm
  from each one's item 14 which year of income its figures apply to; the dated arms
  rest on an inference until then.
- The exported number questions (`Is my income under the threshold`, `How much levy
  on my own income`, `What is my family income threshold`) now take the year, and
  would show the 2023-24 figures for an earlier year; the money answers and
  `What is my threshold amount` / `What is my phase-in limit` say `Not in the
  deposited text` instead. Adding the year changed their inputs (a breaking change
  for any deployment).
- Ask, for a part-year surcharge, the days on which each surcharge section applies
  (married or not, dependants or not, uncovered, not prescribed), so that a year with
  more than one section, or with prescribed days, can be worked out.
- Deposit the indexed PHI Act tier thresholds for each year (they are published,
  not legislated), and work out the s 22-40(4) increase from the number of
  dependent children, as the PHI Act baseline now does.
- Encode s 9A, and the trustee provisions if a trustee seat is wanted.
- An independent test pass and a human gate.
