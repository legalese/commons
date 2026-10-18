# Independent test report — Consumer Rights Act 2015 encoding

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act (ss 19, 20, 22, 24, 54-56) before any `.l4` file was opened. `tests-independent.l4` asserts them against `cra-types`, `cra-goods`, `cra-services` and `cra-goal` (`cra-tests.l4` was not read).

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 82 | 0 |
| (whole directory, 6 modules) | 0 | 120 | 0 |

82 assertions over 66 scenarios: s 22(3) (9), s 22(4) (4), s 22(6)-(8) (12), s 19(14)-(15) (14), s 24(5) (5), s 24(8)-(11) (12), ss 20(15)/56(4) (5), services (6 scenarios, 12 assertions), and the top-level goal for one services case and one full goods case (10 assertions).

A deliberately wrong assertion was added to a scratch copy to confirm the harness reports failures (it did); the scratch copy is not in the encoding directory.

## Failures

None. Every expected value agrees with the encoding, including the readings I flagged as uncertain:
- month-end six-month periods (D5, D9, F5): the encoding ends a period whose corresponding date does not exist on the last day of that month (31 Aug 2025 → 28 Feb 2026; 30 Aug 2027 → 29 Feb 2028), and otherwise on the day before the corresponding date. This is my reading too.
- a repair request after the s 22 limit does not revive the right (C8); a request on the last day extends it (C5).
- s 22(7)(a)/(b) "if later" (C4-C6, C11, C12).

## Remarks (not failures; for the author)

1. **Refund of 0 when s 24(5) is not met.** `the refund on final rejection for` returns `0` when none of the s 24(5) situations has arisen. The brief says "never `FALSE` or `0`" where the source does not answer; here the answer is really "no final right to reject, so no refund under s 24", which is better as NOTHING/REFUSE (the top-level goal already uses MAYBE).
2. **Deduction larger than the price.** `price paid MINUS deduction for use claimed` can go negative (price 1000, deduction 1500 after six months → −500). The Act does not answer how big a deduction may be, but a negative refund is plainly wrong; cap at 0 or REFUSE.
3. **s 24(9)** (no deduction for a period when the consumer kept the goods only because the trader failed to collect them) is not modelled; the deduction claimed is taken as given. Worth a note in NOTES.md or an input.
4. **s 20(15) for the short-term right to reject.** The goods refund deadline is produced only when the tier-two remedies are available. A refund after a short-term rejection is also due within 14 days (s 20(7), (15)), but the top-level goal gives no date for it.
5. **`trader agreed to refund on` is a plain DATE** in `Tier two facts` (MAYBE DATE for services). A goods case where the trader has not yet agreed must invent a date.
6. **No sanity checks on dates.** A waiting period with the goods received before the request gives a negative extension; a fault "appearing" before delivery gives FALSE for the presumption rather than a refusal.
7. **s 22(4) input shape.** Taking the perishable limit as a date (`perishes by`) side-steps the Act's silence about when the shorter period starts — a reasonable choice; the encoding applies it only when earlier than the 30-day limit (B4 passes).
8. **Services scope.** Price reduction under s 54(4) and (5) (information terms not about the service; s 52 time of performance), which is available without the repeat-performance gate, is not modelled. Within the brief's scope, but the export description of `a price reduction is available for` could say so.

## Change after the pass (encoder)

- **Remark 2 adopted.** The refund on final rejection is floored at 0 when the deduction claimed exceeds the price.
- **The other remarks are recorded in NOTES.md:**
  - 0 when the tier-two remedies are not available;
  - s 24(9);
  - the refund date after a short-term rejection;
  - the required agreement date;
  - impossible inputs;
  - s 54(4)-(5).
- None of the independent assertions was changed. `check.sh` shows 120 satisfied, 0 failed, 0 errors.
