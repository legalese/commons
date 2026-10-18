# Independent test report — Pensions Act 2008 encoding

I fixed the expected values from BRIEF.md and the Act (revised text, point in time 29 June 2026) in `independent-expectations.md` before reading any `.l4` file. After that I read only `pa08-types.l4`, `pa08-status.l4`, `pa08-penalties.l4` and `pa08-goal.l4`, for their names and record shapes. I did not open `pa08-tests.l4`. No expected value was changed after the run.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 2 | 88 | 2 |

- 90 assertions across 75 scenarios: S1-S33, Q1-Q14, C1-C12 and the P scenarios that can be expressed.
- Both errors are the two failed assertions. There are no type, parse or other non-assertion errors.
- The encoding's own modules are unaffected: 40/40 assertions pass in pa08-tests.l4.

## Failures

### F1 — line 146, S29: s 3(3), already an active member of a qualifying scheme

- **Inputs:** worker aged 36, in GB, E = £30,000 for 12 months, `excepted … s 3(3) or (4)` = TRUE, `an active member of a qualifying scheme` = TRUE.
- **My value:** `not within the duties`.
- **Encoding:** `an eligible jobholder excepted by s 3(3) or (4)`.
- **Act:** s 3(3) "Subsection (2) does not apply if the jobholder was an active member of a qualifying scheme on the automatic enrolment date." s 7(1) "This section applies to a jobholder who is not an active member of a qualifying scheme."
- **View:** this is a difference in classification, not an arithmetic error. The brief lists four statuses, and the encoding adds a fifth enum value for "excepted". On the brief's four-way scheme, this worker has no duty and no s 7 right, so the answer should be "none of these". The extra value does carry true information. If it stays, the brief or NOTES should record it as a deliberate fifth status.

### F2 — line 150, S30: s 3(4), ceased membership by their own act and not now a member

- **Inputs:** as F1, but `an active member of a qualifying scheme` = FALSE.
- **My value:** `a jobholder who may opt in`.
- **Encoding:** `an eligible jobholder excepted by s 3(3) or (4)`.
- **Act:** s 3(4) disapplies s 3(2) only. s 7(1) applies to a jobholder "who is not an active member of a qualifying scheme". s 7(2)(a) bars s 7 only "at a time when arrangements are required to be made under section 3". Because of s 3(4), no arrangements are required.
- **View:** this is a substantive finding. Under s 7 this person has a right to opt in, and the encoding's single "excepted" status hides it. The cause is that s 3(3) and s 3(4) are merged into one boolean, although they lead to different s 7 outcomes. I suggest returning `a jobholder who may opt in` whenever the jobholder is excepted but is not an active member of a qualifying scheme. The encoding already has that input, so no new field is needed.

## Scenarios I could not express

- **P12/P13 (s 41(2)(a) is limited to notices within s 41(1)(a)-(c)):** the encoding has no input for the kind of underlying notice. Any pending review bars an escalating notice. That is wrong where the underlying notice is a PA 2004 s 72 or s 72A notice (s 41(1)(d)-(e)). For those, s 41(2)(a) does not apply and only a pending tribunal reference (s 41(2)(b)) bars issue. **This is a gap in the encoding, not covered by a failing test.** One fix is to add an input such as `the underlying notice is under s 35, 36 or 37`. Another is to rename the field so that it already means "a review barring under s 41(2)(a) is pending".
- **P8/P9 (whether a stated payment date is valid) and P20 (whether a start date is valid):** neither is exposed as a predicate. I tested them indirectly. An invalid start date, and a daily rate over £10,000, do not produce days × rate. Both assertions pass, because the encoding returns 0.

## Remarks

1. **Invalid notices return 0.** `the escalating penalty under` gives 0 in each of these cases:
   - a notice may not be issued;
   - the rate exceeds £10,000;
   - the start date is too early.

   These are defects in the notice, not a computed penalty of £0. The brief says to use `REFUSE` where the source does not answer. A MAYBE result, or a separate validity flag, would describe this more honestly than 0, which reads like "nothing owed".
2. **s 20(1)(a) employer contribution > 0.** The encoding agrees with my reading R9, including when QE = 0 (C9 passes). This is an ambiguity in the Act, and it should be noted in NOTES.md.
3. **Everything else matched on the first run:**
   - all the pro-rata edges (annual, monthly, weekly as 12/52 months, six months), including the strict "more than £10,000" and the exact rational upper limits (50270/12 and 50270/52);
   - the age edges at 16, 22, pensionable age and 75;
   - the 28-day payment dates across month ends, year ends and a leap year;
   - the escalating day count, which excludes the compliance day.
4. **The one combined boolean for s 3(3)-(4)** is the root of both failures. Splitting it, or deriving the s 3(3) case from `an active member of a qualifying scheme`, would fix F1 (if the four-way status is kept) and F2.

## Change after the pass (encoder)

- **L146 and L150 fixed.** The separate "excepted" status was removed. A jobholder within s 3(3)-(4) now falls to s 7: an active member of a qualifying scheme is outside the duties, and anyone else may opt in (NOTES F9). Both now pass. The encoder's own test was updated to match.
- **The other remarks are recorded in NOTES.md:**
  - s 41(2)(a) needs the kind of underlying notice;
  - invalid notices give 0;
  - s 20(1)(a) with nil qualifying earnings.
- None of the independent assertions was changed. `check.sh` shows 131 satisfied, 0 failed, 0 errors.
