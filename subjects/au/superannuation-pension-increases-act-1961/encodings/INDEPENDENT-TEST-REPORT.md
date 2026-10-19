# Independent test report: Superannuation (Pension Increases) Act 1961

Expectations written first in `independent-expectations.md` (from BRIEF.md and the source only), then asserted in `tests-independent.l4` against `spi61-rules.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| spi61-rules.l4 | 0 | 0 | 0 |
| spi61-tests.l4 | 0 | 9 | 0 |
| tests-independent.l4 | 0 | 20 | 0 |

No failures.

## Disagreements with the brief (not code failures)

1. **(c) and (d) are not truncated.** The brief says the deposited text truncates paragraphs (c) and (d) of "the prescribed amount". It does not. Both are complete:
   - (c): the actual unit contribution ÷ (scale units under (a)(i) of "actual unit entitlement" − units determined under s 52(1)(b)).
   - (d): the amount otherwise applicable × (actual annual pension ÷ the s 29 pension he would have had).

   Taking the fraction as an input is a reasonable modelling shortcut, but NOTES/BRIEF should give the real reason: the extra facts are outside the model. Truncation is not the reason.
2. **(d) stacks on (b)/(c).** Under (d) the base is "the amount that would, but for this paragraph, be applicable", which may itself be a (b) or (c) amount. The code always multiplies 32.5 by the fraction. A combined (b)+(d) or (c)+(d) case is right only if the user folds both proportions into the one fraction. This is correct for B13 (a (d) case on an (a) base), but it is not documented.
3. **s 52 applied, no neglect** (B15). Here the person falls under neither (b) nor (c), so (a) applies. The code gets 32.5 when the user selects `the standard case`, but the enum's comment for (b) is the only guide. A user with contribution < entitlement may wrongly pick (b).

## Gaps

- **s 4(4) widow and s 4(2).** The code applies the 1957 reduction from the widow's own record and then takes 5/8 of the net figure. The Act gives the widow "five-eighths of the increase in pension to which her husband would have been entitled under that subsection" (s 4(1)). It is not clear whether the husband's 1957 increase, or a 1957 increase to the widow's own pension, should reduce it, and in what order. I did not assert this combination. A lawyer should settle it.
- **s 4(6) is one boolean.** The child's pension, the s 57 pension (with its State Fund carve-back), and the s 53/s 58 pensions are all left to the user's judgement. The s 57 State Fund exception cannot be tested.
- **s 7(1) is stored, not computed.** The first fortnightly payment date is an input field that no function returns or uses. B14 only checks that the field holds the date.
- **Unit figures are inputs.** The s 13 scale and the notional annual salary are not modelled. The code never checks the min/max rules in "actual unit entitlement" (the greater for contributory pensioners; the lesser of scale units and 4 for non-contributory). Nor does it check that the contribution is ≤ the entitlement.
- **s 4(3), s 4(5), s 5 and s 6 are not modelled**, consistent with the brief's scope.

## Change after the pass (encoder)

- No assertion failed. The brief was corrected: paragraphs (c) and (d) are not truncated in the source; the fraction stays an input, and (d)'s combination with (b) or (c) is now stated.
- The gaps and the widow's order of operations are recorded in NOTES.md.
