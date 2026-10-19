# Independent test report: Removal of Prisoners (Territories) Act 1923

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| rpt-rules.l4 | 0 | 0 | 0 |
| rpt-tests.l4 | 0 | 10 | 0 |
| tests-independent.l4 | 0 | 26 | 0 |

There are **26 independent assertions, all satisfied, with no failures.** No syntax fixes were needed.

## Failures

None. The coverage below is narrower than the expectations, because the module's `Prisoner case` cannot express several of them.

## Gaps: expectations the module cannot express (no assertion written)

| Expectation | Why untestable | Effect |
|---|---|---|
| E2, E16: the s 2(1) exclusion from "prisoner" | `Prisoner case` has no field for it. The only input is `sentenced to imprisonment in a Territory`. | The caller must fold the exclusion into that boolean. The module does not say this. |
| E3: commuted death sentence (s 2(2)) | No field. The caller must feed it as "sentenced to imprisonment". | Acceptable, but undocumented in the input's description. |
| E6: s 3(1)(a) has two limbs (no proper prison *and* removal expedient) | The enum constructor `no proper prison, removal expedient` bundles both limbs. "No proper prison but not expedient" cannot be stated. | The caller has to choose `no ground` for that case. |
| E15: GG orders without a recommendation | Recommendation is derived from the ground, not entered as a fact. "Grounds found, but the Administrator did not recommend" cannot be expressed. | The module treats "may be recommended" as if it were "recommended". `removal is lawful` does not check that a recommendation was actually made. |
| E22: "removed" for s 8(3)(a) | The module uses `removal is lawful` as a stand-in for "has been removed". | A lawful removal order that was never carried out still yields a free-return entitlement. |
| E24: the s 8(3) application | No field. The module grants the entitlement without an application. | This is a difference in reading. The Act says the person is entitled "on making application in such manner and within such time as is prescribed". |
| E25, E26: s 7A | `escape stops the sentence running` is simply a copy of `sentenced to imprisonment in a Territory`. It is TRUE for every prisoner, whether or not they escaped or were returned. Nothing computes the residue still to be served (1000-day term, 400 served gives 600 still to serve) or the extra punishment for the s 7(2) offence. | My boolean assertions pass, but only trivially. The arithmetic and the "upon being returned" trigger are not encoded. |
| s 5(2) | `conviction questioned in the Territory of origin` equals `removal is lawful`. | This is right for removed prisoners. It reads oddly for a prisoner who was never removed, who can of course question the conviction in the Territory anyway. Saying FALSE there is a question of wording, not a legal answer. |

## Disagreements with the brief

None material. The brief's s 8(3) summary leaves out the application requirement, and the module follows the brief there (see E24).

## Change after the pass (encoder)

- No failing assertions.
- The coarse inputs, the s 8(3) application and the s 7A constant are recorded as known limits in NOTES.md.
