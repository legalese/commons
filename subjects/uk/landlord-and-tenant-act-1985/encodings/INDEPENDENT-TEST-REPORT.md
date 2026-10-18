# Independent test report: Landlord and Tenant Act 1985

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act (point in time 29 June 2026) before any `.l4` file was read. `lta-tests.l4` was not read. Tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| | |
|---|---|
| Assertions in `tests-independent.l4` | 114 |
| Satisfied | 113 |
| Failed | 1 |
| Non-assertion errors | 0 (the single error diagnostic is the failed assertion) |
| Other modules | 0 errors; `lta-tests.l4` 48 satisfied, 0 failed |

Coverage: s 11 application (27 assertions), s 9A application and first day (21), service charges (26), information about the landlord (25), the top-level goal (10). Some scenarios in the expectations could not be written as tests (see Remarks 2 and 3).

## Failure

### F9: s 9B(6), a fixed term renewed on or after the commencement date (`tests-independent.l4` line 166)

- **Scenario:** a fixed term granted 1 Jan 2018 (before s 9A commenced on 20 Mar 2019) and renewed for a further fixed term on or after that date (`a fixed term renewed on or after 9A commenced` = TRUE, `granted on` = 1 Jan 2018).
- **My value:** s 9A applies (satisfied). The covenant first bites on the renewal date, which is on or after 20 Mar 2019. It cannot be 1 Jan 2018.
- **Encoding's value:** `JUST (Date 1 1 2018)`, the original grant. That is fourteen months before s 9A was in force.
- **The Act:** s 9B(6) "the renewal on or after the commencement date is to be treated as a grant of the lease on or after that date". s 9A(1)(a) "fit for human habitation at the time the lease is granted".
- **My view:** this is a genuine defect. There is no input for the renewal date, and `the first day the fitness covenant bites for` returns `granted on`. A user could work around it by entering the renewal date as `granted on`, but then the input means something different for this one case, and the seven-year test (s 9B(8)) would be measured from the renewal. That is arguably right, but nothing in the type says so. Fix: add a renewal date (MAYBE DATE) and use it as the deemed grant both for the bite date and for the term test. At the least, document that `granted on` holds the renewal date in this case.

## Remarks

1. **s 9A(1)(a) "or, if later, at the beginning of the term" is not modelled.** The encoding says so itself ("The beginning of the term is not an input; the grant is used"). My scenario F3 (granted 1 May 2019, term begins 1 Jun 2019, expected bite 1 Jun 2019) cannot be expressed, so it is not asserted. The brief names "the first day the covenant bites" as a goal, so this gap matters. The same input would also serve s 9B(5), for a periodic tenancy that arises on expiry.
2. **Several date limbs are folded into enum or boolean inputs, so their edges cannot be tested:**
   - the 3 Oct 1980 cut-off and the Crown Estate proviso in s 14(4)-(5) (R30, R31, R33);
   - the pre-24 Oct 1961 counterfactual in s 14(1) (R27);
   - the Localism Act s 166 date for s 13(1A)/(1AA) (R20);
   - "more than seven years", shared ownership and the private registered provider limbs of (1AA) (R22-R24; R24 is an exact seven-year PRP lease, which in my reading falls outside both (1) and (1AA));
   - the s 20(3) "exceed an appropriate amount" test, folded into `qualifying works without consultation`.

   This is acceptable for a draft, but the s 14 and (1AA) date and term rules then sit with the user rather than in the encoding.
3. **s 3(3A) liability is not exposed.** Only the end of the relevant period is computed, so L4/L5 (whether the old landlord is liable for a given breach, including one on the notice day) are untested. The notice-day reading stays an open ambiguity.
4. **s 13(1ZC) and s 13(2)(b).** The encoding excludes a (1ZC) assured tenancy even when a lessor break option makes it "less than seven years" under s 13(2)(b). s 13(2) governs "determining whether a lease is one to which section 11 applies", so (1ZC)(b)(i) "granted for a term of seven years or more" could be read through it. This is an ambiguity, so it is not asserted. Worth a note in NOTES.md.
5. **The s 20 cap is applied per cost item.** s 20(7) limits the tenant's relevant contribution per set of qualifying works. If one set of works is entered as several items, each gets its own cap, and the tenant could be charged above the appropriate amount. The input should be documented as "one item per set of qualifying works".
6. **Date arithmetic checks out at every edge tested:**
   - the seven-year boundary, including a grant on 29 Feb;
   - the s 20B 18-month bar and the s 20B(2) notice window at month ends (31/30/28 Aug, 29 Feb, 1 Mar);
   - the s 1 21-day period across a leap February and a year end;
   - the s 3(1) two-month rule, with the rent day inside, on and after the corresponding date and month-end assignments;
   - the s 22(2) and (4) month ends;
   - the s 9B(4) deferral, including a hypothetical 29 Feb commencement.
7. **Minor.** s 22(4) gives only the latest start, not the end of the two-month facilities period. The brief asks only for the latest start, so this is fine.

## Change after the pass (encoder)

- **Line 166 fixed (s 9B(6)).** For a renewal entered with its original, pre-commencement grant date, the first day the covenant bites is now NOTHING. The renewal date should be entered as the grant (NOTES F5). That case now passes.
- **The other remarks are recorded in NOTES.md:**
  - the term start is not an input (F4);
  - s 13(1ZC) and the lessor's break (F2);
  - the s 20 cap per item (F7);
  - a breach on the day of notice (F9);
  - category inputs.
- None of the independent assertions was changed.
- After the change, `check.sh` shows 7 modules: 162 assertions satisfied, 0 failed, 0 errors.
