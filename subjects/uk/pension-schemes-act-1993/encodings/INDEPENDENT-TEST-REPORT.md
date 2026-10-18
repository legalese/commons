# Independent test report — PSA 1993 early leavers and cash equivalent transfers

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the Act before any `.l4` file was read; `psa93-tests.l4` was not read. Tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| | |
|---|---|
| assertions | 81 |
| satisfied | 77 |
| failed | 4 |
| non-assertion errors | 0 |

The encoding's own `psa93-tests.l4`: 30 satisfied, 0 failed.

## Failures

### 1. Leaving on the day the member reaches normal pension age (L20), line 116
- **Scenario:** service 1 Jan 2020 – 1 Jan 2025; reaches NPA on 1 Jan 2025.
- **Mine:** no short service benefit. **Encoding:** entitled.
- **Act:** s 71(1) "where a member's pensionable service is terminated **before normal pension age** and— (a) he has at least 2 years' qualifying service ...".
- **View:** a real defect. `is entitled to short service benefit` never tests termination before NPA, although `may elect a cash transfer sum or contribution refund` does (s 101AA(1)(a)). The top-level goal therefore also reports a "latest age short service benefit is payable from" for someone who left at or after NPA.

### 2. Leaving after normal pension age (L22), line 121
- **Scenario:** service 1 Jan 2020 – 2 Jan 2025; reaches NPA on 1 Jan 2025.
- **Mine:** no short service benefit. **Encoding:** entitled.
- **Act / view:** as failure 1, the same missing limb.

### 3. s 99(7) notification, defined benefits, transfer on the corresponding date (T27), line 224
- **Scenario:** guarantee date 15 Jan 2026, applied 1 Mar 2026, carried out 15 Jul 2026.
- **Mine:** must notify the Regulator. **Encoding:** need not notify.
- **Act:** s 99(7) "have not done what is needed ... **within six months of the date** mentioned in paragraph (a) or (b) of subsection (2)"; s 99(2)(a) "within 6 months beginning with the guarantee date".
- **View:** off by one day. The encoding tests `done GREATER THAN add months start 6`, so a transfer on 15 Jul (one day after the s 99(2) last day of 14 Jul, which the encoding's own `the trustees' last day to transfer for` returns) is not reported. s 99(7) is the enforcement of the s 99(2) duty and should share its period: notify when the transfer happens after `the last day of the 6 months beginning with` the date. "within six months of" is less precise than "beginning with", so this is an interpretive point, but the encoding is internally inconsistent: a transfer can be late under s 99(2) yet not reportable under s 99(7).

### 4. s 99(7) notification, money purchase (T29), line 227
- **Scenario:** money purchase, applied 10 Mar 2026, carried out 10 Sep 2026 (s 99(2)(b) last day 9 Sep 2026).
- **Mine:** notify. **Encoding:** no.
- **View:** same off-by-one as failure 3.

## Remarks

1. **Missing "before normal pension age" in s 71(1)** (failures 1–2). Simple fix: add `l's pensionable service ended on LESS THAN l's reaches normal pension age on` to the s 71 rule (it is already in the s 101AA rule).
2. **s 99(7) uses the corresponding date, not the s 99(2) last day** (failures 3–4). Reuse `the last day of the 6 months beginning with`.
3. **s 99(7) is not exported** and has no field in `Leaver position`, although the brief lists "whether they must notify the Regulator" as part of goal 2 and asks for `@export` on each goal.
4. **s 99(3) inputs are thin.** Only the conclusion date is taken; condition (b) ("it appears to the trustees ... the proceedings may lead to ... being forfeited") is folded into the presence of the date, and proceedings that are still running cannot be represented (the deadline is then unknown and should be `REFUSE`d, not computed). My T25 and A6 could not be tested.
5. **s 98(1) with no application** returns "lost" regardless of whether the s 95(1A) period has yet run out; there is no as-at date. Likewise s 99(7) with no `carried out on` returns TRUE (notify) immediately after an application. Both answers are premature until the period ends.
6. **Inputs that can disagree:** `normal pension age, in years` (s 71(3)) and `reaches normal pension age on` (ss 71(1), 95(1A)(b), 101AA) are independent inputs.
7. **Dates I flagged as ambiguous all agreed with the encoding:** 29 February starts (24 months beginning 29 Feb 2020 end 28 Feb 2022), NPA on 29 Feb 2028 (one year before = 28 Feb 2027), the s 99(3) boundary where the 3-month end is the day after the s 99(2) last day (15 Jul 2026), months ending 30 Nov → 28 Feb, and s 99(3) not suspending s 99(7).
8. Everything else passed: the 2-year, 30-day (incl. s 71(11)), personal-pension and three-month routes with earlier counting days; the s 101AB(4) refund cap; the s 71(3) age; the s 95(1A) deadline for flexible and non-flexible benefits; s 98(1) loss; s 99(2) for DB and money purchase; s 99(3) extension; and the top-level goal record.

## Change after the pass (encoder)

- **L20 and L22 fixed.** Short service benefit now requires pensionable service to end before normal pension age.
- **T27 and T29 fixed.** s 99(7) is now read as the six months beginning with the date, matching s 99(2) (F7).
- **The notification is now an export and a field of the top-level goal.** One of the encoder's own assertions (the 15 July case) was updated to the corrected reading, and a 14 July case was added.
- **The other remarks are recorded in NOTES.md:**
  - s 99(3) proceedings still running;
  - no as-at date;
  - normal pension age entered twice.
- None of the independent assertions was changed. `check.sh` shows 112 satisfied, 0 failed, 0 errors.
