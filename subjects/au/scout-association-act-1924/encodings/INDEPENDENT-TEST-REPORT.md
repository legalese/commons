# Independent test report: Scout Association Act 1924

Expectations: `independent-expectations.md` (written from BRIEF.md and the source before reading the rules).
Tests: `tests-independent.l4`, run with `L4=~/.local/bin/l4 ./check.sh`.

## Counts

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 19 | 0 |

All 14 scenarios asserted; all agree with the encoding.

## Failures

None.

## Gaps and observations

- **s 4 "the Local Branch for the area in which the use takes place".** The encoding takes one input, "proved authority of the Association or local Branch". Authority from a Branch for a *different* area (scenario 9) and authority claimed but unproven (scenario 10) both have to be entered as FALSE by the user; nothing in the model enforces the area condition. Adequate, but the input's wording ("local Branch") could mislead a user holding another area's authority.
- **s 2 "without authority"** is a single boolean; the Act does not say whose authority, and the burden for s 2 stays with the prosecution (no reversal as in s 4). Not modelled; not testable.
- **"prosecution may be instituted"** is FALSE when no offence is made out, and otherwise equals Minister's consent. That fits s 5 for the seat's question.
- **"maximum penalty units"** is the sum across the two offences (2 when both). I agree this is the per-offence maximum aggregated; the dollar value of a penalty unit (Crimes Act 1914 s 4AA) is out of scope.
- s 3 registration (Minister's approval; the Defence-similarity proviso) is not modelled; whether a uniform is "registered in pursuance of" s 3 is an input.
- s 1A (Criminal Code Ch 2 fault elements) is not modelled.

## Change after the pass (encoder)

- No disagreements.
- The coverage gaps are recorded as known limits in NOTES.md.
