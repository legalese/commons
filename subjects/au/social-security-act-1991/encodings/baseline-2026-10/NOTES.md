# Social Security Act 1991 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`, no
`BECAUSE`: where the deposit cannot give an answer, the figure is an input and a
comment says why. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

This encoding replaces the first-pass encoding `naive-2026-10`. It covers
everything the first pass covered and reuses its hand-checked figures where they
still hold: pension age, residence, the age pension and seniors health card
cases, the disability support pension, the jobseeker waiting period, youth
allowance and carer allowance. It adds carer payment for a disabled adult
(ss 197, 198) and the compensation recovery rules of Part 3.14 (ss 17, 1166,
1167, 1169, 1170, 1173). Every question is published with `@export`, and every
parameter carries a `@desc`.

**Edition:** Compilation No. 232, compilation date 1 July 2026, includes
amendments up to Act No. 17, 2025 (register id C2026C00336, in 6 volumes), as
deposited at `../../registers/source-bundle/C2004A04121.txt`. The deposit's
metadata warns that the version in force from 20 September 2026 has no
registered compilation yet, so amendments commencing on or after that date may
be missing. Neither of the two instruments the plan names is deposited:

- the Impairment Tables (Social Security (Tables for the Assessment of
  Work-related Impairment for Disability Support Pension) Determination 2023);
- the Adult Disability Assessment Tool.

So the impairment rating and the ADAT scores are inputs. The indexed rates,
limits and free areas are not in the Act's text either, so they are inputs too.

The formulas the text deposit lost (points 1064-E10, 1064-G4 Table G-2, 1067G-F27,
1067G-F28, ss 17(4), 17(8), 598(2A), 1170(4)) are transcribed by hand on 2026-10-21
in `../../registers/source-bundle/C2004A04121.formulas.md`, from the Word rendering
of the later compilation C2026C00449 (the Register no longer serves C2026C00336 as
its latest); the words around each formula were checked identical to the deposit.

**Checks:** two modules (`ssa-claims.l4`, and `ssa-formulas.l4` added 2026-10-24) and two
case files (`ssa-cases-claims.l4`, 70 assertions, built by the scratchpad generator
`gen_social-security-act-1991_baseline.py`; `ssa-cases-formulas.l4`, 29 assertions, written by
hand). Result: 99 assertions satisfied, 0 errors, 0 warnings in every file, with the stable `l4`
of VS Code extension 1.6.98 (2026-10-24). A deliberately wrong assertion, added to a scratch
copy, was reported as failed.

## Seat

**The claimant**: the pensioner, the jobseeker, the person with a disability,
the student, and the carer. Each asks "Am I qualified, and at what rate will I
be paid?" The Act is written as a set of conditions the Secretary applies.
Each condition is encoded as what it means for the claimant: whether they
qualify, whether the payment is payable, how much, how long they must wait, and
what can stop it.

Decisions are phrased as the claimant asks them:

- **Pension age and residence:** `What is my pension age in months`, `Have I
  reached pension age`, `Do I have 10 years qualifying Australian residence`.
- **Age pension:** `Am I qualified for the age pension`, `What is my assets
  excess`, `What annual rate of age pension do I get`, `Is the age pension
  payable to me`, `What base assets value limit does Table G-1 print for me`.
- **Seniors health card:** `Do I satisfy the seniors health card income test`,
  `Am I qualified for a seniors health card`.
- **Disability support pension:** `Do I have a severe impairment`, `Do I have a
  continuing inability to work`, `Am I qualified for the disability support
  pension`, `Does my disability support pension stay payable`.
- **Jobseeker payment:** `Am I qualified for jobseeker payment`, `How many weeks
  is my liquid assets waiting period`.
- **Youth allowance:** `Am I qualified for youth allowance as a full-time
  student`, `What is my parental income test result`, `What fortnightly youth
  allowance do I get`, `Is youth allowance payable to me`.
- **Carer allowance:** `Is the care receiver my family member`, `Do I satisfy
  the carer allowance income test`, `Am I qualified for carer allowance`.
- **Carer payment:** `Is the care receiver a disabled adult`, `Does the care
  receiver meet the ADAT score for carer payment`, `Am I qualified for carer
  payment`.
- **Compensation recovery:** `Is my payment compensation affected`, `Is what I
  received compensation`, `What is the compensation part of my lump sum`, `How
  many weeks is my lump sum preclusion period`, `Is my payment stopped by my lump
  sum`, `Can my payment be withheld for not pursuing compensation`, `By how much
  is my daily rate reduced for periodic compensation`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers brought in:**
  followed as far as the deposit allows. Neither the Impairment Tables nor the
  ADAT is deposited, so their results are inputs. The indexed figures in force
  (Part 3.16) are inputs as well. The printed Table G-1 figures are encoded only
  as the base figures they are.
- **The actors the text names:** followed. They are the claimant, the
  claimant's partner, parents, care receiver and carer, the Secretary, and the
  compensation payer.
- **A judgment handed to someone else is answered conditionally:** followed.
  The following are inputs, worded "the Secretary is satisfied ...":
  - the Secretary's satisfaction under s 94(2) and s 593(1)(a);
  - the Secretary's approval of a care receiver under s 954(1)(b) and
    s 23(14)(c);
  - the Secretary's opinion of the lost-earnings part of a lump sum
    (s 17(3)(b));
  - a s 1166 requirement.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts:** followed for the following:
  - pension age (s 23(5A)–(5D), as a table);
  - qualifying Australian residence (s 7(5));
  - severe impairment (s 94(3B));
  - continuing inability to work (s 94(2));
  - liquid assets waiting period (ss 14A, 598);
  - family member (s 23(14));
  - disabled adult (s 197(1));
  - compensation, and the compensation part of a lump sum (s 17(2)–(3));
  - compensation affected payment (s 17(1)).

  Departed from where working a definition out would need a Part of its own,
  each asked as a fact instead: "independent" (s 1067A), "Australian resident"
  (s 7), the homeowner definition (s 11), ordinary income and assets (Parts 3.10,
  3.12), deeming, and "constant care", which s 197 does not define.
- **One case is the text's natural unit:** followed. One claim, by one person,
  for one payment, on one day.
- **The Act's own terms, each with a plain gloss:** followed. The comments
  quote the Act's words beside each decision.
- **Operative sections in scope, machinery out:** followed, within a further
  limit set by the size of the Act (see "Why this scope").

## The lives

| Event | Life | What it asks of this Act | Decision asserted |
|---|---|---|---|
| c079 (2037) | Chloe: her father Graham turns 67 | Age pension? Seniors health card? | `Is the age pension payable to me` — no, on assets; `Am I qualified for a seniors health card` — yes |
| c093 (2070) | Chloe turns 67 | Age pension? | `Is the age pension payable to me` — no, on assets; seniors health card — yes |
| d020 (2014) | Daniel, 17, at UWA | Youth allowance and the parental income test | `Am I qualified for youth allowance as a full-time student` — yes; `Is youth allowance payable to me` — no, parental income |
| d083 (2063) | Daniel turns 67 | Age pension? | `Is the age pension payable to me` — no |
| k086 (2055) | Jake, redundant at 49 | What does JobSeeker require? | `Am I qualified for jobseeker payment` — yes, with the mutual obligation; `How many weeks is my liquid assets waiting period` — 13 on $20,000; `Is my payment stopped by my lump sum` — no, for his 2053 impairment lump sum |
| k091 (2063) | Jake's stroke: 20 points | The DSP test | `Am I qualified for the disability support pension` — yes at 20 on one Table, no at 19 |
| k092 (2063) | Ruby, 30, cares for Jake | What does a carer get? | `Am I qualified for carer allowance` — yes; `Am I qualified for carer payment` — yes, on the facts given |
| k093 (2065) | Jake's review | Still qualified? | `Am I qualified for the disability support pension` on a s 63 review — yes |
| k095 (2073) | Jake turns 67 | Which pension? | `Does my disability support pension stay payable` — until the age pension becomes payable; `Is the age pension payable to me` — yes |

**The scenarios give no income or asset figures for any of the lives.** The cases
use invented figures to show the shape of each outcome the scenarios record. They
test the encoding, not the lives.

## Why this scope

The Act runs to six volumes. The baseline keeps to what the claimants in the
three lives meet, and to the conditions, definitions and exceptions needed to
answer them. The rest is left out, including:

- every payment rate and its indexation (ss 1190–1194);
- rent assistance, the supplements and the work bonus;
- deeming, and what counts as income or as an asset (Parts 3.10, 3.12);
- the homeowner definition, disposal of assets, and financial hardship;
- the other jobseeker waiting periods, preclusions and compliance;
- employment pathway plans (Administration Act);
- youth allowance independence and the maintenance income test;
- carer allowance for children and its rate;
- carer payment for children or for an adult and child, its short-term and
  hospital rules, and its own rate and means tests;
- the rest of Part 3.14: ss 1164, 1165, 1171, 1172, 1174–1184K, and the s 17(4)
  repayment adjustment;
- review and appeal, which sit in the Social Security (Administration) Act
  1999, not deposited.

The plan names s 1064 for the rate of age and disability support pensions.
Module A is encoded for the age pension. The DSP rate is not, because none of
Jake's events asks for it.

## What the Act turns out to say

1. **The six formulas the text deposit lost are now in hand, and the three
   inferred shapes were right.** From the sidecar `C2004A04121.formulas.md`:
   - point 1064-E10: the reduction for ordinary income is the ordinary income
     excess × 0.5;
   - Table G-2 column 3: the reduction for assets is assets excess × 19.5 / 250
     a year, the same for every family situation (a member of a couple applies
     both tapers to a 50/50 share, so the first pass's illustrative 25c and 3.9c
     for couples were not the Act's);
   - point 1067G-F28: (the excess / 130) × (the person's maximum payment rate /
     the total of the maximum payment rates of everyone with the parental income
     in common);
   - s 17(8): the income cut-out amount is [2 × (maximum basic rate + pension
     supplement component + energy supplement component) + ordinary free area
     limit] / 52 a week, from four indexed single-person figures (inputs);
   - F27 ((the excess) / 130), s 598(2A) ((liquid assets − maximum reserve) /
     divisor) and s 1170(4) (compensation part / income cut-out amount) are the
     forms the first pass had inferred.

   A single person $1,000 over the assets limit loses $78 a year; illustrative
   components of $23,000, $1,800, $366 and $1,668 give a cut-out amount of $1,000
   a week. Asserted.

2. **The Table G-1 dollar figures are base figures from 2017.** Section
   1192(5C)–(5E) shows that $250,000, $450,000, $187,500 and $287,500 were the
   limits "immediately before" 1 July 2017, indexed since. None is the limit in
   force on any scenario date. Asserted as the printed base figure only.

3. **Graham's refusal and his card come from the same facts.** Step 11 takes
   the lower of the income reduced and assets reduced rates. Section 44(1) says
   an age pension is not payable at a nil rate. The seniors health card
   (s 1061ZG) does not look at assets at all, and requires that the person is
   *not* receiving a social security pension. So a refusal on assets is close to
   a precondition for the card. The card's income test halves a couple's
   adjusted taxable incomes (1071-11). Income "equal to or exceeds" the limit
   fails (Step 5). Asserted.

4. **Pension age is 67 for all four lives, reached on the 67th birthday.** Both
   the men's table (s 23(5A)) and the women's (5D) end at "On or after 1 January
   1957 — 67 years". On the day before his birthday, Jake has not reached it.
   Asserted.

5. **Nothing ends the Disability Support Pension at pension age; Jake has to
   claim.** Section 103(2) makes the DSP not payable once "another social
   security pension ... becomes payable". Note 1 says another payment "will
   generally not become payable to the person until the person claims it". So
   the k095 change is triggered by his claim, not by his birthday. Asserted.

6. **A review is easier than a first claim.** Take an impairment that is not
   severe: 20 points, but not 20 under one Table (s 94(3B)). It needs active
   participation in a program of support (s 94(2)(aa)), except on a s 63
   reassessment of a current recipient (s 94(3A)). Take 10 + 10 points with no
   program of support:
   - on a first claim, the person is **not** qualified;
   - on review, the same person **is** qualified.

   Jake's 20 points "on a borderline table" are taken as all from one Table.
   That is an inference from the scenario's wording. Who rates a borderline case
   is not in this Act. Asserted.

7. **JobSeeker requires the mutual obligation, and unpaid redundancy pay delays
   it.** Section 593(1)(b) requires (1AC): meeting the employment pathway plan
   requirements and being willing to seek and accept paid work. The age band runs
   from 22 to pension age. Section 14A(1)(c) counts amounts "due, and able to be
   paid ... by ... a former employer" as liquid assets. For a single person with
   no children, $20,000 gives the 13-week cap and $8,000 gives 6 weeks. Asserted,
   on the s 598(2A) formula in finding 1.

8. **Carer allowance and carer payment use different ADAT thresholds, and
   Jake's pension helps Ruby.**
   - Carer allowance needs an ADAT score of at least 30 on a professional
     questionnaire score of at least 12 (s 954(1)(c)). Its income test is a flat
     $250,000 on the couple's adjusted taxable incomes **added**, not halved
     (s 957A).
   - Carer payment needs at least 25 on 10 if the carer is the only carer, but
     80 on 32 if not (s 198(2)(a)). Care must be given in the care receiver's
     home (s 198(3)).
   - The care receiver's own income and assets tests (ss 198A, 198D) do not
     apply when the care receiver is on a social security pension (s 198(7)).
     So Jake, on the DSP, does not have to pass them.

   The scenario records only carer allowance. Carer payment's own rate and means
   tests, which bear on Ruby, are not encoded. Asserted.

9. **Compensation recovery reaches the age pension, the DSP, carer payment and
   every social security benefit, but not carer allowance.** Section 17(1)
   lists the compensation affected payments. A lump sum from settling an injury
   claim is counted at 50% (s 17(3)(a)). Any other lump sum counts only for the
   part the Secretary thinks is for lost earnings (s 17(3)(b)). A payment that is
   not "in respect of lost earnings or lost capacity to earn" is not compensation
   at all (s 17(2)). Nor is criminal injuries compensation (s 17(2B)). The
   scenario gives Jake a 2053 workers' compensation lump sum for 14% permanent
   impairment, then JobSeeker in 2055. Whether that lump sum was for lost
   earnings is a fact the scenario does not state. On the assumption that it was
   not, it does not stop his JobSeeker. Asserted on that assumption.

10. **Smaller things worth recording.**
    - Under s 7(5), one period of exactly 10 years qualifies. Several periods
      totalling exactly 10 do not: the aggregate must "exceed" 10 years.
      Asserted.
    - d020 is dated 2014, but this is the 2026 text. The encoding applies 2026
      law to Daniel's 2014 claim.
    - Daniel's sister Sofia, 14, is taken to be an FTB child of their parents
      (an inference). If she is, F31 sends Daniel to the F28 formula, sharing
      the excess in proportion to maximum payment rates (illustrative $450 of
      $700: $469.80 a fortnight). Under Step 13, a nil rate makes youth allowance
      not payable. Asserted on illustrative rates.
    - Under s 543A(2AA), a 16- or 17-year-old in full-time *secondary* study does
      not reach the minimum age unless an exception applies. Daniel, at
      university, does. Asserted.

## Amounts computed from the formulas recovered on 2026-10-24

The sidecar's "Further entries, recovered 2026-10-24" transcribe every other formula image in
the deposited compilation C2026C00336. `ssa-formulas.l4` IMPORTs `ssa-claims.l4` (unchanged) and
computes, from those formulas, figures the claimant was asked to supply or that were out of
scope for want of the formula:

- **Indexation** (ss 1192(2), 1193, 1194): the indexation factor from two CPI index numbers
  (3 places, raised by 0.001 when the 4th place is over 4, never below 1) and the indexed amount
  rounded to the rounding base (half way rounds up). The CPI numbers stay inputs.
- **The pension assets value limits** after a 1 July indexation (s 1191 items 18-20, rounding
  base $250), with the single non-homeowner limit set by **s 1203**: single homeowner + 2 ×
  (partnered non-homeowner − partnered homeowner). On the Table G-1 base figures s 1203 gives
  $450,000, the printed fourth figure, so the table is consistent with the formula. Asserted.
- **Deemed income of a member of a pensioner couple** (s 1077(3), (3A), (3B), (4)): half the
  couple's deemed income, weekly and yearly. The deeming threshold and rates stay inputs
  (ss 1081, 1082).
- **The youth allowance liquid assets test waiting period** (ss 549A(1), (2), 549C): the same
  formula, reserve and divisors as jobseeker payment's s 598, capped at 13 weeks.
- **The F28 total with a relevant sibling** (points 1067G-F31(b), F32, F35): the person's rate
  plus 14/365 of the parent's FTB maximum rate, so the parental income test result is computed
  from the parent's FTB rate instead of a supplied total (Daniel, d020: $468.40 a fortnight on
  illustrative rates).
- **A lump sum after repaid periodic compensation** (s 17(4)): LSP − RPCP, carried through the
  s 17(3) compensation part and the s 1170(4) preclusion period.

No computed value disagrees with an existing assertion of `ssa-cases-claims.l4`.

**Left for later** (formulas now in the sidecar, not yet encoded): the work bonus (s 1073AA);
the rent increased payment rates (ss 1070L-1070R); pension bonus (ss 92V, 93G, 93J); the
student start-up and financial supplement loan formulas (ss 1061ZVEC-1061ZZFD); the income
stream rules (ss 9A-9BA, 1099-1099DAB, 1119-1120AB); the maintenance income free area (point
1067G-GA6); advance payments (ss 1061ED-1061JC); the carer allowance training-day reduction
(s 974(3)); and the other benefit AVL and allowance adjustments (ss 1204-1206B). The rate
calculators' own reductions for youth allowance and jobseeker payment (Module H of point 1067G,
point 1068-G) are in the text, not lost; the sidecar entries there are worked examples, so they
are not taken up here.

## What would need doing before this is worth anything

- ~~Work out the F31(b) sibling rate~~ done 2026-10-24 in `ssa-formulas.l4`; the parent's
  FTB maximum rate (point 1067G-F32) is still an input.
- Supply the indexed rates, limits and free areas for each scenario date, either
  from the Act's indexation machinery or from published figures.
- Encode what counts as income and as an asset (deeming, the principal home,
  superannuation). Until then, "refused on assets" is only a shape.
- Give the lives income and asset figures, so that outcomes can be computed
  rather than illustrated.
- Deposit and encode the Impairment Tables and the ADAT, and the Social Security
  (Administration) Act 1999 for claims, reviews and employment pathway plans.
- Use the 2014 compilation for d020.
- Encode carer payment's own rate and means tests, and the rest of Part 3.14 if
  a life brings in periodic compensation.
