# Independent test report: United States Naval Communication Station (Civilian Employees) Act 1968

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 20 | 0 |
| usnc-rules.l4 | 0 | 0 | 0 |
| usnc-tests.l4 | 0 | 9 | 0 |

There are **20 independent assertions, all satisfied, with no failures.** No syntax fixes were needed.

## Failures

None. The commencement-day edge I flagged in the expectations (E14, injury on 24 June 1968) passes. The module joins s 6(1) and s 6(2) into a single test, "on or after 29 August 1966". That leaves no gap at commencement.

## Gaps: expectations the module cannot express

| Expectation | Why | Effect |
|---|---|---|
| E2: instrumentality (s 3(2)) | There is no separate field. The caller must fold it into `employed by the US Government at the Station`. | Acceptable. The deeming is not visible in the module. |
| E3 vs E4: which body agreed the terms (Fair Work registered organisation vs WA union) | Both are folded into one boolean, `on terms agreed with an Australian union`. | Acceptable. Note that the Act also covers terms agreed with an "association recognised by" the Fair Work (Registered Organisations) Act, which is not strictly a union. The field name is narrower than the Act. |
| E6: national but not citizen | Citizen and national are folded into one boolean. | This is correct, because s 4(a) excludes either. |
| E8 vs E9: not in connexion with the Station vs not a US Government employer | Both are folded into one boolean. | Acceptable. |
| E13: the dependant claims after death | There is no claimant field. The single answer stands for "he or she or that other person". | The module cannot say *who* may recover. |
| s 6(1) vs s 6(2) | The module does not report which subsection grounds the claim. s 6(2)'s hypothesis (the 1930-1964 version of the CEC Act) has its own input in principle, but the module reuses the s 6(1) inputs. | This matters only if ss 9/10 of the 1964 and 1967 versions differ for a given injury. |
| s 5(1) | `the compensation Act applies to me` is identical to `this Act applies to me`. | This is correct on s 5(1). |

## Disagreements with the brief

None.

## Change after the pass (encoder)

- No disagreements.
- The combined inputs are recorded as known limits in NOTES.md.
