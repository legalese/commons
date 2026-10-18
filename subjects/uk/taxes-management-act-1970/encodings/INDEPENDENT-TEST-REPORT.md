# Independent test report — TMA 1970 self-assessment encoding

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act (ukpga-1970-9.txt, point in time 25 June 2026) before any `.l4` file was opened. `tma-tests.l4` was not read. No expected value was changed after reading the code.

## Counts

- Scenarios: 85 in sections A-G (A 3, B 19, C 7, D 20, E 11, F 14, G 11) plus one end-to-end case (H).
- Assertions in `tests-independent.l4`: 100.
- Satisfied: 97. Failed: 3. Other errors: 0.
- `L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 3 errors / 97 satisfied / 3 failed (the 3 errors are the 3 failures); every other module 0 errors (tma-tests.l4 35/35).

## Failures

All three have the same cause: s 9A(2) decides "on or before the filing date" against the **s 9ZA(3)** filing date (31 January Y+2, or 3 months from a notice after 31 October), not the **s 8** date that s 9A(6) points to. The difference shows only for paper returns, because for electronic returns the two dates coincide.

| Line | Scenario | My value | Encoding | 
|---|---|---|---|
| L102 | D5: Y 2024, notice 20 Apr 2025, paper, delivered 1 Nov 2025 | 31 Jan 2027 | 1 Nov 2026 |
| L103 | D6: Y 2024, notice 20 Apr 2025, paper, delivered 20 Dec 2025 | 31 Jan 2027 | 20 Dec 2026 |
| L111 | D14: Y 2024, notice 15 Aug 2025, paper, delivered 15 Nov 2025 | 31 Jan 2027 | 15 Nov 2026 |

The Act says:
- s 9A(6): "In this section 'the filing date' means, in relation to a return, the last day for delivering it in accordance with section 8 or 8A."
- s 8(1D)(a): "in the case of a non-electronic return, on or before 31st October in Year 2"; s 8(1F)(a): "during the period of 3 months beginning with the date of the notice (for a non-electronic return)".
- s 9A(2)(b): "if the return was delivered after the filing date, up to and including the quarter day next following the first anniversary of the day on which the return was delivered".

In D5 the paper filing date is 31 Oct 2025, so delivery on 1 Nov 2025 is late. The anniversary is 1 Nov 2026, and the next quarter day is 31 Jan 2027. The encoding uses 31 Jan 2026 as the filing date, treats the return as on time and gives 1 Nov 2026. D6 and D14 (where the paper Exception 1 date is 14 Nov 2025) work the same way.

**My view:** this is an encoding error. The s 9ZA(3) definition is expressly "In this section". s 9A has its own definition in (6), and it follows s 8, so it depends on paper or electronic and on the Exception 1/2 dates. The fix: in `base d` (tma-returns.l4), compare against the s 8 filing deadline (`the filing deadline for` r), not `the filing date under s 9ZA for` r. When there is no notice there is no s 8 deadline, so that case needs its own handling. The paper/late cases also need a regression test. The tma-returns `@export` text ("twelve months after delivery for a return delivered by the filing date") does not say which filing date it uses.

## Remarks

1. **Loss of tax is a single choice.** `Loss of tax` is one enum, so a careless and offshore loss (G4) or a deliberate and offshore loss (G7) cannot be entered as such. The user has to pick the most serious limb. That gives the right answer here, because the longest period governs: s 36A(2) is "subject to section 36(1A)" and s 36(1) is "subject to subsection (1A)". The `@desc` should say so. Also missing: an offshore loss is not "brought about by the taxpayer", but the first constructor's name (`no loss brought about by the taxpayer`) suggests it covers everything else. The s 36A(7)-(9) exclusions are not modelled and not flagged.
2. **s 59B(3)(a) is a bare boolean.** `notified chargeability in time` is an input, not computed from a s 7 notice date against 5 October Y+1. So the boundary F6/F7 (notice on 5 Oct vs 6 Oct) cannot be tested in the encoding; I could only enter TRUE/FALSE. Someone who never had to notify, because a s 8 notice arrived first, must enter FALSE to get s 59B(4). That is right, but nothing tells the user. s 59B(4ZA)/(4ZB) (s 8B withdrawal) are not modelled.
3. **Month arithmetic is correct**, including all my edge cases: month-end notices (31 Aug -> 30 Nov, 31 Dec -> 30 Mar, 31 Oct -> 30 Jan), February in normal and leap years (30 Nov 2025 -> 28 Feb 2026; 30 Nov 2027 -> 29 Feb 2028; 29 Nov 2027 -> 28 Feb 2028), and twelve months after 29 Feb (-> 28 Feb, my reading A1). The quarter-day rule handles anniversaries that fall on a quarter day (strictly next).
4. s 59A thresholds at exactly the prescribed amount and proportion are inclusive, as "not less than" requires. Zero or negative excess is excluded. A 50% payment of an odd relevant amount gives 500.5 (no rounding; the Act says none).
5. The helper `the last day of the n months beginning with` is defined twice, in tma-returns.l4 and tma-payment.l4. This is harmless, but if one copy changes, the two can drift apart.
6. `the filing deadline for` returns NOTHING when there is no notice to file. That is sensible: s 8 imposes no duty without a notice. s 9ZA, however, falls back to 31 January Y+2 when there is no notice. That case is unreachable in practice, but the two goals treat it differently.
7. I wrote 85 scenarios, above the requested 40-70. The extra ones are boundary cases in B and D.

## Change after the pass (encoder)

- **D5, D6 and D14 fixed.** The enquiry window now judges "on or before the filing date" against s 9A(6)'s filing date: the s 8 deadline, falling back to the s 9ZA date where no notice was given (NOTES F4). All three now pass.
- **The other remarks are recorded in NOTES.md:**
  - the loss of tax as one choice (enter the most serious);
  - s 59B(3)(a) as an input;
  - s 59B(4ZA);
  - the duplicate helper.
- None of the independent assertions was changed. `check.sh` shows 135 satisfied, 0 failed, 0 errors.
