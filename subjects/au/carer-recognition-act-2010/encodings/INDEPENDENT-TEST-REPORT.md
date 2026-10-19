# Independent test report: Carer Recognition Act 2010 (Cth)

Expectations were written in `independent-expectations.md` from BRIEF.md and the source text, before any `.l4` file was opened. The tests are in `tests-independent.l4`.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| carer-rules.l4 | 0 | 0 | 0 |
| carer-tests.l4 | 0 | 20 | 0 |
| carer-types.l4 | 0 | 0 | 0 |
| tests-independent.l4 | 0 | 34 | 0 |
| **TOTAL** | 0 | 54 | 0 |

## Failing assertions

None. All 34 independent assertions pass. They cover s 5(1)(a)-(d), s 5(1) with no qualifying need, s 5(3) (relationship or co-residence without care), s 5(2)(a)-(c), the obligations of each kind of body under ss 7(1), 8(1), 8(2) and 9(a)-(b), and s 10(1)-(2) on the top-level goal.

## Gaps: expectations the encoding cannot express

Each of these is a scenario in `independent-expectations.md` that the model's inputs are too coarse to test. None is a wrong answer. All are places where the encoding takes the answer as an input instead of working it out.

1. **"frail and aged" (scenario 14).** `being frail and aged` is a single enum value. A person who is frail but not aged cannot be entered except as `none of these`, so the user decides the conjunction in s 5(1)(d), not the encoding.
2. **s 4 definitions are inputs, not rules (scenarios 18, 20-23).** `Kind of body` is an enum, so the encoding does not work out:
   - that a "public service care agency" has to be a public service agency (s 4(1));
   - that a subcontractor of the first entity is also an associated provider (s 4(2)(b));
   - that a contract with a State or Territory is excluded, including one made by "another person or body" (s 4(3));
   - that the contract has to be with a *care* agency and *for care supports* (s 4(2)).

   The brief puts these definitions in scope "so far as they decide what an agency must do". As it stands the user has to apply s 4 before entering a body.
3. **s 7(2) is not encoded.** The HR-policy duty ("internal human resources policies ... developed having due regard to the Statement") applies to every public service agency but not to associated providers. The output has no field for it. `the body must make its staff aware of the Statement` covers s 7(1) and s 9(a) only.
4. **s 8(2) timing (scenario 17).** The duty to consult arises only "when developing or evaluating care supports", not when implementing or providing them. The output field is an unqualified boolean. It is correct for the kind of body, but it does not carry this limit.
5. **s 5(2) is per care.** "not a carer in respect of care ... he or she provides" under a contract etc. Each case has a single `the basis`, so a paid worker who also cares unpaid for a relative cannot be represented as a carer in respect of the unpaid care.
6. **s 10(3) is not encoded (scenario 27).** Nothing records that the Act does not require an agency to act inconsistently with another law. It is arguably inert from the carer's seat.
7. **The s 5(3) relationships are not inputs.** The encoding never asks about relationship or co-residence. It relies on the care-given boolean, which is a faithful reading of "merely". The tests could only model s 5(3) as "gives no care" (with any need) and "is a spouse who gives care".

## Disagreements with the brief

These are small, and none changes a tested answer:
- The brief says "frailty and age" where the Act says "frail and aged", which is conjunctive.
- The brief's description of an associated provider leaves out second-tier providers (s 4(2)(b)) and the requirement that the contract be for care supports.

## Change after the pass (encoder)

- No disagreements in any answer.
- The brief's wording was corrected: "frail and aged" (both), and the fuller description of an associated provider.
- The gaps listed above are recorded as known limits in NOTES.md.
