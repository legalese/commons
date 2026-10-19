# Independent test report: Damage by Aircraft Act 1999 (Cth)

## Method

1. Read BRIEF.md and the source (C2004A00498.txt, including endnote 3) only.
2. Wrote `independent-expectations.md` (33 scenarios) before opening any `.l4` file.
3. Read `dba-types.l4` and `dba-rules.l4` for names only (not `dba-tests.l4`) and wrote `tests-independent.l4`. No expected value was changed to fit the code.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| dba-rules.l4 | 0 | 0 | 0 |
| dba-tests.l4 | 0 | 26 | 0 |
| dba-types.l4 | 0 | 0 | 0 |
| tests-independent.l4 | 0 | 40 | 0 |
| **Total** | 0 | 66 | 0 |

`fails.sh tests-independent.l4` prints nothing. **No failing assertions.**

## Disagreements with the encoding

None found by test. Points where my reading could differ and that the code happens to agree with:

- **s 9(4) with no listed category (scenario 6).** I read s 9(4) as the full reach of the Act, so outside it the Act does not apply (FALSE). The brief's "NOTHING, never FALSE" rule might suggest an unknown here; the encoding returns FALSE / no liability (NOTHING for `who is liable`), which matches my reading.
- **s 11A(3) proportional reduction (scenario 29).** The Act reduces damages "to the extent the court thinks just and equitable having regard to the share"; it does not require a strictly proportional cut. The encoding (its note F2) and I both take damages × (1 − share). This is a reading, not something the Act says.
- **s 10(1A) before 31 March 2013 (scenario 16).** Mental injury alone suffered before commencement: s 10 applies (item 7(3)). Encoding agrees.

## Gaps (things the tests cannot reach because of the types)

1. **s 9(4) is a single boolean** (`an aircraft within s 9(4)`), so the individual paragraphs (a), (b), (c)(i)-(v) (scenarios 7, 8) cannot be tested separately; the user must classify the aircraft themselves.
2. **"More than 14 consecutive days" is a boolean input**, so the boundary (exactly 14 days, scenario 20) cannot be tested: scenario 20 is the same input as 19 and only checks the consequence.
3. **Owner who is also the authoriser.** s 10(2A) says "Subsection (2) does not apply to a person", so a passive owner meeting (2A) who also authorised the use should escape (2)(c) too. The encoding models owner and authoriser as separate liability flags; with a passive leasing owner and an operator lacking >14 days' exclusive use, `the person who authorised the use` comes back TRUE even if that person is the owner. Not testable without a "the owner authorised the use" input. Worth a note in NOTES.md.
4. **s 11A(1) gate.** s 11A applies only if "a defendant proves" my negligence. The encoding has no such input; a share of 0 stands in for "not proved". Harmless numerically, but the answer for a pre-commencement case is NOTHING even when no negligence is alleged.
5. **s 10(1A) "property owned by the person"** and the mental-plus-other-harm case are a single `only mental injury` flag; fine for the brief's inputs.
6. **Share outside 0-100** is clamped by the encoding; the Act says nothing on this. Not tested.
7. **s 6, s 7, s 5** (operator, employees, in flight) are not computed; the user supplies "in flight" via the cause and identifies the operator themselves. Out of reach of tests, consistent with the brief's inputs.

## Change after the pass (encoder)

- No disagreements to resolve.
- The gaps listed above are recorded as known limits in NOTES.md.
