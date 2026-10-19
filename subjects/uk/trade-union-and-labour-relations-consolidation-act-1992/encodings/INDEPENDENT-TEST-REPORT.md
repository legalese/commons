# Independent test report: TULRCA 1992 (UK)

Expectations were written first, in `independent-expectations.md`, from BRIEF.md and the source text only (ss 146-147, 152-156, 161, 188-192, 195A, 238-239, 292A). The `.l4` modules (not `tulrca-tests.l4`) were then read for names only, and `tests-independent.l4` asserts those expectations unchanged.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 3 | 100 | 3 |
| tulrca-tests.l4 | 0 | 78 | 0 |
| other modules | 0 | 0 | 0 |

The 3 errors are the 3 failed assertions. There are no syntax or type errors.

## Failing assertions

### 1 and 2. A worker who is not an employee, whose engagement is ended (P8)

- **L102** `I am protected under the union provisions` for: reason membership, at an appropriate time, **not an employee**, treatment `dismissal`. **Expected TRUE; the code gives FALSE.**
- **L103** `the last day to complain of the detriment for` the same case (act 1 Jan 2026). **Expected JUST 31 Mar 2026; the code gives NOTHING.**
- **Source:** s 146(5A): "This section does not apply where—(a) the worker is an employee; and (b) the detriment in question amounts to dismissal." Both limbs must be met. A worker who is not an employee and whose contract is ended for union reasons still has s 146 (and so s 147). The code treats `dismissal` as protected only for an employee, and gives a s 147 limit only for `a detriment short of dismissal`.
- **My view:** the Act's reading is right. The code is correct only if users are told to record a non-employee's termination as `a detriment short of dismissal`. Neither the type comments nor the export description say so. Fix: for `dismissal`, protected if the worker is an employee (s 152) **or** is not one (s 146, outside (5A)). Give the s 147 limit whenever s 146 applies, that is for a detriment short of dismissal, or for a dismissal of someone who is not an employee.

### 3. 100 or more across the employer, the duty arising through the establishment route (R8)

- **L211** `the days of consultation needed for` (120 proposed in all, 60 at my establishment, threshold 150). **Expected 45; the code gives 30.**
- **Source:** s 188(1A)(a): "where the employer is proposing to dismiss 100 or more employees as mentioned in subsection (A1), at least 45 days". (A1) says "proposing to dismiss as redundant within a period of 90 days or less— (a) at least the threshold number ..., or (b) 20 or more employees at one establishment".
- **The code's reading (its F4):** count the total only where the threshold route (A1)(a) applies, and otherwise count only the establishment.
- **My view:** "as mentioned in subsection (A1)" picks up the words common to both limbs, "dismiss as redundant within a period of 90 days or less". It does not pick up the one-establishment limit from (b) alone. The employer here is proposing to dismiss 120 as redundant within 90 days, so (1A)(a) applies. The point is open to argument, and the deposited text runs the old and new wording together. But the code's split gives a result that is hard to defend: 120 dismissals get 30 days when the threshold is 150, yet would get 45 days if the threshold were 120. I would record this as a contested reading in NOTES.md and lean towards 45.

## Points where I agree with the code (worth recording)

- **s 292A(3) with long conciliation (C8):** act 1 Mar 2026, Day A 5 Mar, Day B 20 Jun 2026. All 107 days from 6 Mar to 20 Jun are not counted, giving **15 Sep 2026**. The code gives the same. It does not clip the stopped days at the unextended limit, which is one way to read the brief's "so far as they fall within the period".
- **s 239(2)(a) has no s 292A extension (X9).** The deposited text of s 239 applies neither s 292A nor ERA s 207B, and the code (F7) leaves it out. This should be checked against the official text, because the official s 239 may have a subsection (2A) that the harvested text lacks.
- Every month-end and leap-year edge passed (31 Jan, 30 Nov, 29 Nov 2027, 1 Dec, Day B on 31 Jan in a leap and a non-leap year), as did the s 161 EDT + 7 edges, the 20/threshold/100 edges, the 180-day cap and the s 191 exclusions.

## Gaps in the encoding

1. **s 161(6), the "date of dismissal" for the union certificate,** is not modelled. If the contract was ended by notice, it is the day the employer's notice was given. The certificate must state membership on that day (s 161(3)(a)). There is no input for the notice date, and no check of what the certificate says (scenario I15 could not be asserted).
2. **s 195A(3):** the threshold number may not be below 20. The code accepts any threshold, so a threshold of 15 would bring in 15 dismissals. It should `REFUSE`, or treat the input as invalid.
3. **s 189(5)(a):** a complaint "before the date on which the last of the dismissals takes effect" is in time. Only the last day is given, with no "is my complaint in time" check. That makes no practical difference, but S3 is not covered by its own assertion.
4. **s 147(1)(b), 189(5)(c), 192(2)(b), 239(2)(b):** the "not reasonably practicable" extensions are judgements the code does not model. That is acceptable, but the export descriptions do not say the extensions exist.
5. **s 156(2):** for a s 153 dismissal, the contributory-fault reduction applies to the minimum part of the award. This is outside the "before reductions" figure, so it is a scope note, not an error.
6. **s 238(5)(a)** "terminated by notice ... the date on which the employer's notice was given": the input is named `employer's notice given on`, so an employee's own resignation on notice falls to the EDT. That is consistent with the words, but NOTES.md should say so.
7. **s 146(1) applies to "a worker"** and s 152 to "an employee". `Union case` has a single boolean, `an employee`. That is enough, but finding 1 shows how it is combined with `the treatment`.

## Change after the pass (encoder)

- **s 146(5A), a worker who is not an employee (lines 102-103).** Accepted. Such a worker keeps s 146 and the s 147 time limit when the engagement is ended; ss 154 and 161 now apply only to an employee's dismissal. Both assertions pass; one of the encoder's tests that took the old reading was updated, with a comment.
- **s 188(1A)(a), 45 or 30 days (line 211).** Accepted. The 100 is counted across the employer (F4). The assertion passes.
- The gaps listed above are recorded as known limits in NOTES.md.
