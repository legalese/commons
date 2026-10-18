# Independent test report: Nationality and Borders Act 2022, Part 2

Expected values were fixed in `independent-expectations.md` (from BRIEF.md and ss 20-22, 26,
30-37) before any `.l4` file was opened. `nba-tests.l4` was not read.

## Counts

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`:

- 94 assertions: 93 satisfied, 1 failed.
- 1 error diagnostic, which is the failed assertion itself. No other errors.
- Encoding's own modules: 0 errors; `nba-tests.l4` 45/45.

Coverage: goal 1 has 31 assertions (commencement edge both sides, every Convention reason,
particular social group with each condition alone, both and neither, stage one, stage two,
severity, all three actors including non-State actors with and without State protection,
protection with each limb alone and both, internal relocation with each limb alone and both).
Goal 2 has 22 (directness three ways, all three s 37(2) situations both ways, cross-situation
facts that should be ignored, s 37(4)). Goal 3 has 28, plus 13 on the top-level goal.
The goal 3 assertions cover lateness on the day before, on, and after the cut-off date,
s 20(4), and twelve s 21(1) end dates. Those include a later and an earlier
appeal-exhaustion date, a 29 February start, a 1 March start running into a leap
February, a year-end start and a month-end start.

## Failure

**L256: s 26(1)(b), evidence not before a deciding authority determining a claim or appeal
(scenario N26).**

- Scenario: evidence notice, evidence provided 20 Mar 2024 after the 15 Mar 2024 date, no
  good reasons, and no claim or appeal being determined. I used
  `a relevant decision is being made = FALSE`, the nearest input the model has.
- My value: minimal-weight principle does **not** apply.
- Encoding: applies (TRUE). `minimal weight applies to the evidence under` checks only
  lateness and good reasons.
- Act: s 26(1) "This section applies where— (a) evidence is provided late ... and (b) the
  evidence falls to be considered by a deciding authority for the purpose of determining—
  (i) the claim, or (ii) where a decision in respect of the claim is the subject of a
  relevant appeal, the appeal."
- My view: a real but minor gap. s 26(1)(b) is a condition of the section, and the encoding
  leaves it out. The model has no s 26(1)(b) input. The only related flag is s 22(3)'s
  "relevant decision", which is wider because it includes reasonable- and conclusive-grounds
  decisions on slavery or trafficking. A dedicated input would be better, or the encoding
  could note that s 26(1)(b) is assumed. As written, the exported result can answer TRUE where
  s 26 is not engaged at all.

## Remarks

1. **s 26(5)(a) is not distinguished (untestable, scenario N25).** For a PRN, s 26 covers
   only evidence in support of the s 120(2)(a)-(c) reasons and grounds statement
   (s 20(3)(a)(i)). It does not cover evidence of relevant status information
   (s 20(3)(a)(ii)), and it does not cover the statement itself as opposed to evidence. The
   encoding treats any late material under a PRN as within s 26. It needs a field for what the
   material was.
2. **s 22(2) and s 20(6) are folded into the same lateness input.** Material given late to a
   tribunal "should have been provided in response to the notice but was not". The encoding
   gives the same answer for both routes, which I consider right in outcome. But nothing records
   which route applies.
3. **The s 21(1) dates are all correct**, including 29 Feb 2024 → 28 Feb 2025, 1 Mar 2023 →
   29 Feb 2024, and a later appeal-exhaustion date that moves the start. A 12-month period
   starting on 29 February 2024 has no corresponding date in 2025. The code then falls back
   to "add months" clamping to 28 Feb 2025 and does not subtract a day. That matches the
   brief.
4. **s 37(1) "directly" when there was no stop** is treated as direct (my reading A1 too).
   The Act only says when a refugee is *not* taken to have come directly. Whether the person
   came directly at all is left to Article 31, and the encoding's `@export` text says so.
5. **s 34 protection**: the encoding treats "not both limbs" as no protection, which matches
   my reading A2. s 31(1)(c) and s 34 use similar facts, but the encoding takes them as separate
   inputs: "State unable or unwilling" and "effective legal system plus access". That means a
   non-State actor case can have inconsistent findings, for example the State is unwilling yet
   operates an effective legal system. A decision-maker would not make findings like these, but
   the model does not stop them.
6. **s 30(5)**: a pre-commencement claim returns its own result rather than "not a refugee",
   which is correct. s 33(5) on sexual orientation and the s 31(3) examples are not modelled.
   Both are illustrative rather than decisive, so this is acceptable.

## Change after the pass (encoder)

- **L256 fixed.** Minimal weight under s 26 now also needs the evidence to fall to be considered in determining the claim or an appeal. The `a relevant decision is being made` input stands for this. That case now passes.
- **The other remarks are recorded in NOTES.md:**
  - under a PRN, s 26(5)(a) covers only evidence for the reasons-and-grounds statement;
  - s 31(1)(c) and s 34 are separate inputs;
  - the tribunal route (ss 20(6), 22(2)) is not recorded.
- None of the independent assertions was changed.
- After the change, `check.sh` shows 7 modules: 139 assertions satisfied, 0 failed, 0 errors.
