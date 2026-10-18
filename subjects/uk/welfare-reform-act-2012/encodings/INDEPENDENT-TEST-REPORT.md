# Independent test report: Welfare Reform Act 2012 (ss 3-5, 8; 77-83; 96)

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act
(revised text, 1 July 2026) before any `.l4` module was opened. `wra-tests.l4` was not read.

## Counts

| | |
|---|---|
| Scenarios written (independent-expectations.md) | 71 (U1-U29, P1-P25, C1-C17); a few extra assertions, incl. 9 on the top-level goal |
| Assertions in `tests-independent.l4` | 102 |
| Satisfied | 102 |
| Failed | 0 |
| Non-assertion errors | 0 |

`L4=~/.local/bin/l4 ./check.sh`: all modules 0 errors; TOTAL 139 satisfied, 0 failed
(102 independent + 37 in `wra-tests.l4`). A sanity run on a scratch copy with two
deliberately wrong expectations added confirmed that failures are detected.

## Failures

None. Every value I decided from the Act matches the encoding, including:

- s 4(1)(a) met on the 18th birthday, not the day before; s 4(1)(b) met the day before the
  qualifying age, not on it;
- capital equal to the prescribed limit passes; a penny over fails; an award equal to the
  prescribed minimum passes, a penny under fails; joint claimants fail if either one fails a
  basic condition;
- the s 8 award floors at 0 when deductions equal or exceed the maximum amount;
- every limitation/required-period combination for both PIP components; s 82 gives the enhanced
  daily living rate regardless of findings and drops only the mobility required period
  condition (the limitation and age tests still apply); s 77(4) overrides terminal illness;
- s 83: entitled ON the relevant-age date and not the day after, both where pensionable age is
  above 65 (relevant date = pensionable age) and where it is below 65 (relevant date = 65th
  birthday; entitled in between);
- the four s 96(5A) limits; relevant amount = limit x days / 365 exactly (7, 28, 30, 1, 365 days);
  no reduction exactly at the relevant amount (including a partial-period, non-terminating one).

## Remarks

1. **29 February birthdays (s 4(1)(a)).** Not a failure, because I deliberately asserted only
   the reading-independent case. Probing showed `add years (Date 29 2 2008) 18` = 28 Feb 2026,
   so the encoding treats a leap-day claimant as 18 on 28 February in a non-leap year. The
   common UK reading (Family Law Reform Act 1969 s 9, "the relevant anniversary") is often
   taken to be 1 March. The same helper drives the 65th birthday in s 83. Worth a line in
   NOTES.md, or a `REFUSE` / explicit choice.
2. **s 82(1)(a) and (b) are folded into one boolean** (`terminally ill and claimed on that
   ground`). The "terminally ill but not claimed expressly on that ground" case (P13) can only
   be expressed as FALSE; it cannot be tested as a distinct limb, and the s 82(5) third-party
   claim is invisible. Acceptable as an input simplification, but it is not isomorphic to s 82(1).
3. **The relevant age (s 83(2)) is not exposed as a date**; only `is past the relevant age in`
   (a boolean on the day). Tests went through the component functions instead.
4. **Joint capital and income are single inputs** (`capital`, deductions), so s 5(2) "combined
   capital" and s 8(4)(b) "combined income" rely on the caller summing them. Fine, but the
   field description could say "combined, for joint claimants".
5. **Top-level goal reports a UC award of 0 when not entitled** (`wra-goal.l4`). The Act's s 8
   amount is still computed for s 5(1)(b); reporting 0 is a presentation choice, stated in the
   @export text. An empty claimants list is (rightly) not entitled.
6. s 96(2)'s "reduced by an amount up to or equalling the excess" is encoded as the full
   excess, as the brief directs; the @export says so.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md:
- 29 February birthdays (F8);
- s 82(1)(a)-(b) and (5) as one input;
- the relevant age only as a yes/no;
- joint capital and deductions entered combined;
- an award of 0 where not entitled.
