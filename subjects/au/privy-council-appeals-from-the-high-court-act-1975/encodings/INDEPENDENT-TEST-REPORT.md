# Independent test report: Privy Council (Appeals from the High Court) Act 1975

Expectations written from BRIEF.md and the source only (`independent-expectations.md`), then encoded in `tests-independent.l4` against `pcah-rules.l4`.

## Counts (`L4=~/.local/bin/l4 ./check.sh`)

| module | errors | satisfied | failed |
|---|---|---|---|
| pcah-rules.l4 | 0 | 0 | 0 |
| pcah-tests.l4 | 0 | 4 | 0 |
| tests-independent.l4 | 0 | 6 | 0 |

No failures. The encoding returns `MAYBE BOOLEAN`: JUST FALSE = barred, JUST TRUE = not barred, NOTHING = this Act does not decide. All four input combinations behave as I expected.

## Disagreements

None in behaviour. Note: the result `JUST TRUE` for the saved case is described in the `@export` text as "may still ask"; the Act only limits, so strictly it means "this Act does not bar it". Wording only.

## Gaps

- The module does not import the 1968 encoding, so "special leave was open under the 1968 Act" is a bare input. Scenario 5 (composition with the 1968 Act) could only be tested by working the 1968 result out by hand, so it adds nothing beyond scenario 1. A composed goal (1968 facts plus the 1975 commencement) would let the two Acts be tested together.
- The source's citation "Privy Council (Limitations of Appeals) Act 1968-1973" (plural) is a drafting slip; the encoding quotes it faithfully and treats it as the 1968 Act. Fine.
- The commencement date of the 1975 Act is fixed by Proclamation and is an input, as the brief says.

## Change after the pass (encoder)

- No disagreements in any answer. The export's wording was changed to say that TRUE means s 3 does not bar asking.
- The gap listed above (the 1968 Act as a bare input) is recorded in NOTES.md.
