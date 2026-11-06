# Civil Liability Act 1936 (SA) -- baseline encoding, the claimant

> **Warning.** The texts encoded here are taken from the Open Australian Legal Corpus (South Australian legislation last
> collected on 10 March 2025): the Act as at 22 June 2023 and the Civil Liability Regulations 2013 as at 2 October 2015.
> They are unofficial and may be out of date: later amendments are missing. Check legislation.sa.gov.au before relying
> on anything here.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`cla-core.l4`) holds every rule, with two regulative rules (s 25 and s 70(4), each
a duty to commence within three years after the death) run by `EVALTRACE` inside functions that take only plain facts;
the seat layer (`cla-seat.l4`) restates none of them. Dates and rounding sit in one small module (`cla-dates.l4`, built-in
date functions only). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. Answers are named outcomes
(enumerations) or numbers, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used; where the text says no in its own words
the outcome is a "no: ..." naming the provision, and where it leaves the matter to the general law the outcome says that
the section "does not ...", which follows the 2026-11-04 and 2026-11-05 rulings in substance. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Motor Vehicles Act 1959 baseline
(`subjects/au/sa/motor-vehicles-act-1959/encodings/baseline-2026-11/`) encodes the CTP claim process and points here for
the assessment of damages; the stable `l4` cannot IMPORT across subjects, so the two are not linked in code.

## Edition

- **Act:** Civil Liability Act 1936, corpus document `south_australian_legislation:2023-06-22/1936.2267.un`, deposited at
  `../../registers/source-bundle/civil-liability-act-1936.txt` (sha256 2f71d9df...0a7fb254 as committed).
- **Regulations that set its numbers:** Civil Liability Regulations 2013, corpus document
  `south_australian_legislation:2015-10-02/2013.165.un`, deposited at
  `subjects/au/sa/civil-liability-regulations-2013/registers/source-bundle/civil-liability-regulations-2013.txt` (sha256
  2ff7cb8c...83445a4015 as committed); regs 7 (ISV a whole number), 18 (State average weekly earnings) and 19 ($25 an
  hour, indexed). The deposited Regulations fix no discount rate, so the Act's 5 per cent applies (s 3(1)). A later
  regulation may have changed that, or the ISV rules.
- **Not deposited, so inputs:** the Adelaide CPI figures (s 3(1), s 52(2)(d), (7), reg 19(2)); State average weekly
  earnings (reg 18, an ABS series); the minimum employer superannuation rate (s 56A(7), (9)); the injury scale value or
  scale value itself (assessed by the court under regs 4-17 and Schedule 1).
- **Coverage dates.** Parts 6, 7 and 8: accidents on or after 1 May 2004, when the Law Reform (Ipp Recommendations) Act
  2004 took effect prospectively (Sch 1 cl 1); an earlier accident answers `not covered: an accident before 1 May 2004`,
  asserted. The 2002 and 2003 amounts of s 52(2)(b), (c) are encoded in the core and asserted there. The MVA rules
  (ss 52(3)-(8), 56A, 58(4), 58B, 65(2)) apply to MVA motor accidents on or after 1 July 2013 (Lifetime Support Scheme
  Act 2013, Sch 2 cl 21(2)); an MVA motor accident before then is treated under the general rules, asserted (fork F6).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cla-dates.l4` | 0 | 0 | 0 | 0 |
| `cla-core.l4` | 0 | 0 | 0 | 0 |
| `cla-seat.l4` | 0 | 0 | 0 | 0 |
| `cla-cases.l4` | 0 | 0 | 178 | 178 |

Negative control: with the s 52(3)(c)(ii) $3 000 changed to $3 001 and the s 49 age 16 to 17, the cases failed exactly
3 times, as predicted (ISV 32 and 45; the 16-year-old without a seatbelt); the core was restored and rechecked.

Every expected value was worked by hand from the text, with the edges: the last day of the three years (15 March,
29 February), of the six months (31 August to 29 February), 27, 28 and 29 November 1974, 30 April and 1 May 2004,
30 June and 1 July 2013, 30 June 2014, every band edge of s 52(3)(c), ISV 7/8 and 10/11 and reg 7 rounding (10.4, 10.5),
the half-way $5 in rounding, blood alcohol .079/.08 and .149/.15, age 15 and 16, $1 under and at the prescribed minimum,
the Act's own examples in s 52(2) ($44 850) and s 50(4) ($56 250). The CPI figures in the cases are invented test
figures, not the ABS series.

## Seat

**The claimant (required): the person injured in an accident, or the family member (or personal representative)
claiming for a death** (`cla-seat.l4`, 36 questions). Every question is one that person would ask: "Is the action for
my benefit?", "May I bring it myself?", "By when?", "What solatium can I get?", "Did they have to warn me?", "Is my claim
excluded because I was committing a crime?", "Are my damages reduced because I was drinking / not wearing a seatbelt?",
"How much is left?", "Can I get damages for pain and suffering, and how much?", "for mental harm?", "for my family's
care?", "What is the most for loss of earning capacity?", "Can I sue the good samaritan?", "Does their apology count?".
Provisions addressed to the court are encoded as what they mean for the claimant: a bar, a cap, a reduction, a date.

No seat for the defendant or the insurer here (a defendant seat would be welcome as a second layer), and none for the
court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: Regulations regs 7, 18, 19 brought in; CPI,
  State average weekly earnings and the superannuation rate are inputs (not deposited).
- **The actors the text names.** Followed: injured person, plaintiff, defendant, executor or administrator, parents,
  spouse, domestic partner, good samaritan, person in default, court.
- **Judgments answered conditionally.** Followed: "obvious risk", "inherent risk", "reasonable person would have taken
  steps", "satisfied beyond reasonable doubt", "contributed materially", "exceptional ... harsh and unjust",
  "significantly impaired", "reasonably incurred", "reasonably required", "unreasonably delayed", "good faith and without
  recklessness", s 30(2)'s refusal, and every scale value are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 3 "intoxicated" with s 48(1) (.08 conclusive),
  "prescribed minimum", "prescribed maximum", "prescribed discount rate", "MVA motor accident", the s 3 kinship
  definitions (in the relationship choices), s 51's scope; borrowed: "infant", "indictable offence", "recognised
  psychiatric illness", "seatbelt as required under the Road Traffic Act 1961", Lifetime Support Scheme participation.
- **One case:** one injury (or one death) and one claim.
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** ss 1, 2, 4, 71, 76, 77; transitional provisions used only for coverage dates.

## Scope

**In:** Part 5 (ss 23-30: who benefits, who may sue, one action, three years, expenses, what is not deducted, solatium);
Part 6 Div 3 (ss 36-39) and Div 6 (s 43); Part 7 (ss 44-50, with the s 50 order of reductions); Part 8 (ss 51-58B:
thresholds, the s 52(2) and (3) amounts with indexation, mental harm, first week, the prescribed maximum, the
dependants' cap, the discount rate, interest, management costs, the s 56A threshold, 20% discount and superannuation
caps, gratuitous services with the MVA thresholds and the reg 19 rate, the Lifetime Support Scheme bars, s 58B); Part 9
s 65 (consortium), s 67 (raising a child), s 70 (delay damages, with its three-year limit), s 74 (good samaritans), s 75
(apologies).

**Out, and why:**

- Part 3 (animals), Part 4 (occupiers), Part 6 Divs 1, 2, 4 (standard of care, causation, professionals): they direct
  the court's negligence judgment and give the claimant no threshold, number or date to compute; s 33 (mental harm duty)
  likewise. Encoding them would only restate "if the court finds ...".
- Part 6 Div 5 (s 42, road authorities' immunity for failing to maintain roads): a simple immunity; left for a second
  pass.
- Part 7A and 7B (institutional child abuse liability; setting aside settlements): a separate claims area with its own
  machinery (nominees, associated trusts); to be encoded as its own layer.
- Part 9 Divs 1-4, 7, 9, 10, 11A, 11B, 12A, s 64, s 66: not claim-assessment rules a claimant meets in an injury or death
  claim, or (s 66) a separate head left for a second pass.
- s 76 and Regulations Part 2, Part 4 and Schedule 1 (how the ISV is assessed, medical examinations, the injury table):
  the ISV is taken as an input. Time limits for injury claims generally are in the Limitation of Actions Act 1936, a
  different subject.

## Forks (the text does not say; one reading taken)

- **F1** "within three years after the death", "within six months after the death": the same day of the month that many
  months later, or that month's last day where shorter (29 February 2024 plus 3 years is 28 February 2027). Asserted.
- **F2** "to the nearest multiple of $10": a half-way $5 goes up. Asserted ($67 275 to $67 280; $3 575 to $3 580).
- **F3** s 56A(5): the s 54(2) cap is applied first, then the further 20%. The other reading discounts first.
- **F4** s 58(2) "an amount equivalent to 4 times State average weekly earnings": four times the weekly figure, as a total
  cap; the latest published figure is the input.
- **F5** s 49: one presumption, so one 25% reduction, however many of (a), (b)(i), (b)(ii) apply.
- **F6** an MVA motor accident before 1 July 2013 is assessed under the general rules (Sch 2 cl 21(2)).
- **F7** s 27(1): a family member may sue from the day after the six months end, if none has been commenced.
- **F8** s 28: the maximum is one sum for both parents together (s 28(2) divides "the amount recovered").
- **F9** s 47(5) speaks of "the driver"; the encoding applies the 50% where the person relied on is at the higher level.

## What the Act turns out to say (findings)

1. **s 52(2) Example: the working is missing.** The deposit reads "will, therefore, be $44 850, calculated as follows:"
   and then nothing; the corpus lost the formula (the header says none was missing). $34 500 + 3 x $3 450 = $44 850, so
   the figure is right. Asserted.
2. **ss 28(1), 29(1) leave out 28 November 1974.** The maximum is $1 000 / $1 400 for a death "before" the 1974 Act's
   commencement and $10 000 "after"; a death on the day itself has none. Asserted as a named outcome.
3. **s 52(5)-(6) has no amount.** The court may award damages for an ISV of 10 or less in an exceptional case, but
   s 52(3)(c) states amounts only for 11 and over, and s 52(6) bounds the ISV, not the money. Asserted as a named outcome.
4. **s 52(7) indexes each "(indexed)" amount separately.** Rounding each to $10 gives $13 680 for ISV 20 at a ratio of
   1.138671875, not the $13 660 that indexing the $12 000 total would give. Asserted.
5. **reg 19(2) has no rounding.** Unlike s 52(7), the $25 hourly rate is not rounded to anything: $28.466796875 at the
   test ratio. Asserted.
6. **s 3(1) "prescribed maximum" for 2002.** Part 8 began on 1 December 2002, so the 2002 figures ($2.2 million,
   $2 750, $1 710 a point) serve accidents in December 2002 only.
7. **The Regulations deposit is older than the Act's** (2 October 2015 against 22 June 2023); later regulations may have
   fixed a discount rate or changed the ISV rules.

## Before relying on it

Replace both texts with the register's current versions and recheck every figure; take the CPI and State average weekly
earnings figures from the ABS series; have a lawyer review the forks; add the defendant's seat, s 42, Parts 7A and 7B;
run an independent test pass.
