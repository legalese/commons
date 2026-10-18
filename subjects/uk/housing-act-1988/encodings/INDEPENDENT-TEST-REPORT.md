# Independent test report: Housing Act 1988 ss 8, 21, 27-28

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any `.l4` file was opened. Tests are in `tests-independent.l4`. Only `ha88-types.l4`, `ha88-possession.l4`, `ha88-damages.l4` and `ha88-goal.l4` were read (for names and record shapes); `ha88-tests.l4` was not read.

## Counts

`L4=~/.local/bin/l4 ./check.sh`, tests-independent.l4: **94 assertions, 92 satisfied, 2 failed, 0 other errors.**

| Area | Assertions | Failed |
|---|---|---|
| A s 8 earliest date (pre-2025) | 24 | 0 |
| B s 8 latest date | 4 | 0 |
| C Ground 7A windows | 20 | 2 |
| D s 21 (England) | 22 | 0 |
| E ss 27-28 | 14 | 0 |
| F top-level goal | 10 | 0 |

## Failures

### 1. L161 — Ground 7A notice served before the conviction (scenario C4)

- Inputs: condition 1/3/5, conviction 10 Mar 2025, notice served 9 Mar 2025.
- My value: FALSE (not served in time). Encoding: TRUE.
- Act, s 8(4D): "the notice must be served on the tenant within (a) the period of 12 months beginning with the day of the conviction". A period *beginning with* 10 Mar 2025 does not contain 9 Mar 2025.
- View: genuine (if narrow) defect. `a Ground 7A notice was served in time under` checks only `served AT MOST <last day>`; it needs `served AT LEAST trigger` too. In practice a notice relying on a conviction that has not yet happened would fail Ground 7A itself, but the s 8(4C) answer the function gives is wrong on its own terms, and the appeal limbs make it reachable: a notice served after the conviction but before an appeal is finally determined is not "within the period beginning with the day on which the appeal is finally determined" under (4D)(b), yet the encoding says TRUE.

### 2. L186 — Ground 7A closure-order notice served before the order (scenario C20)

- Inputs: condition 4, closure order 1 Jun 2025, served 31 May 2025.
- My value: FALSE. Encoding: TRUE.
- Act, s 8(4F)(a): "within the period of 3 months beginning with the day on which the closure order was made".
- View: same defect as failure 1 (no lower bound).

## Remarks

1. **Ground 7A input is split in two.** `grounds` (which drives the earliest date) and `Ground 7A condition` (which drives (4C)-(4F)) are independent fields. A notice whose grounds include Ground 7A but whose condition is NOTHING is reported "served in time" (TRUE) rather than refused or flagged; and a condition can be given without Ground 7A in the grounds. Consider deriving one from the other or refusing on mismatch.
2. **s 8(4) pre-2025 reading.** The merged text of (4) is hard to split. Whichever reading is taken, a notice with Ground 7A gets the (3A) date (always at least the service date), so the encoding's branch order (7A, then 14, then (4A), then (4B)) gives the same results as mine for every combination tested, including 7A+14, 7A+(4A) ground, 14+(4A) ground.
3. **s 28 when the "with right" value exceeds the "without" value.** The encoding floors at 0. The Act says "the difference in value", which could be read as an absolute difference. In practice the vacant-possession value is the higher one, so this is unlikely to matter; not tested, noted only.
4. **s 27(7) reduction** is modelled as an amount deducted ("reduce ... to such amount as it thinks appropriate" is a reduced figure, not a deduction). Equivalent arithmetic; the input's description could say so.
5. **s 27(2) is compressed** into one boolean ("attempted or harassed, and the occupier gave up occupation as a result"), which also absorbs the (2)(b) knowledge requirement. That is why scenarios E10, E11 and E13 (no giving up, no knowledge) can only be tested as that boolean being FALSE. The (8)(b) defence is correctly confined to cases that are "by virtue only of" acts/services (deprivation plus harassment with reasonable grounds stays liable).
6. **Dates.** All month-end and 29 February cases (s 8(3A)(b), (4A)(a), (3)(c); s 21(4B), (4D), (4E); Ground 7A periods) agree with the brief's readings.
7. **Top-level goal** gives NOTHING for the earliest date under the amended version, as required, while still giving the 12-month latest date and the Ground 7A answer for that version. (3)(c) and (4C)-(4F) are the same in both versions, so that looks right.

## Change after the pass (encoder)

- **L161 and L186 fixed.** A Ground 7A notice must now be served on or after the trigger day (NOTES F4). Both now pass.
- **The other remarks are recorded in NOTES.md:**
  - a 7A ground listed without a condition counts as in time;
  - the s 28 difference is floored at 0;
  - s 27(2) is one input.
- None of the independent assertions was changed. `check.sh` shows 129 satisfied, 0 failed, 0 errors.
