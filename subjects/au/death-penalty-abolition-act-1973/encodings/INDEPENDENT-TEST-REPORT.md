# Independent test report: Death Penalty Abolition Act 1973 (Cth)

Expectations were written in `independent-expectations.md` from BRIEF.md and the source text alone, before any `.l4` file was opened. `tests-independent.l4` asserts them against `dpa-rules.l4`. No expected value was changed to fit the code.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| dpa-rules.l4 | 0 | 0 | 0 |
| dpa-tests.l4 | 0 | 18 | 0 |
| dpa-types.l4 | 0 | 0 | 0 |
| tests-independent.l4 | 2 | 73 | 2 |

The 2 errors are the 2 failed assertions. There are no syntax or type errors.

15 scenarios, 5 assertions each (75 in all): Act applies; death may be imposed; penalty in place of death; offence within s 3(2); and the top-level goal's `death may be imposed` field.

## Failing assertions

- L86 `the penalty in place of death for` `s10` EQUALS NOTHING (State law, provides death, offence after 1973)
- L94 `the penalty in place of death for` `s11` EQUALS NOTHING (same, offence before 1973)

The encoding returns `JUST "not death; the replacement is for the State's law"`.

My reasoning: s 5 applies only to "any law referred to in subsection 3(2)". Under s 3(3) only s 6 reaches the States. For a State offence the Act gives no replacement penalty, and the brief says so too ("the Act ... does not say what penalty replaces it"). The brief's rule is "Where the source does not answer, give NOTHING". The encoding instead returns a value that describes that silence, and it sits in a field named "the penalty in place of death". A consumer could read that as an answer from s 5. The "not death" part repeats s 6, which the `death may be imposed` field already covers. **Disagreement: low severity, but real.** Fix it either by returning NOTHING here, or by renaming the field or the enum so it clearly reports that s 5 does not apply. That choice is for the encoder or a reviewer. Row 12 (State law with no death penalty) passes, because the code returns NOTHING when the law does not provide for death.

## Agreements worth noting

- All three s 3(2) kinds of law, with death provided: imprisonment for life (s 5). Without death provided: NOTHING, not life imprisonment.
- Death may be imposed: JUST FALSE for Commonwealth, Territory, Imperial-within-powers and State law. NOTHING for "some other law". The top-level record agrees.
- The Act applies: TRUE for the four covered kinds, FALSE for other law. FALSE is acceptable here: the question is whether the Act applies, and the Act's own scope (s 3) answers it.

## Gaps

1. **s 4 is not modelled separately.** s 4 ("not liable to the punishment of death") reaches only s 3(2) offences. s 6 ("must not be imposed") also reaches State offences. The encoding merges both into `death may be imposed`, which gives JUST FALSE for States. That is right for the person's question ("can I be sentenced to death?"). But nothing records that s 4's non-liability does not extend to State offences (my Q1 for rows 10-12 = Nothing). I could not test this.
2. **No offence-date input.** s 3(4) makes the date irrelevant, so the encoding leaves it out. My before-1973 and after-1973 rows therefore have identical inputs. Date invariance holds by construction and was not tested as a behaviour.
3. **"Imperial Act outside the Parliament's powers"** has no constructor of its own. It has to be entered as `some other law` (scenario 15). That works, but whether an Imperial Act is within power is left entirely to the user.
4. **s 5's parenthesis** ("a provision that would, but for this Act, have effect by virtue of such a law") has no separate input. It is folded into `the law provides for death`.

## Change after the pass (encoder)

- **Scenarios 10-11 (a State law providing for death).** Accepted. The penalty in place of death is now NOTHING for a State law, since s 5 does not reach it and the Act sets no replacement (F1). One of the encoder's tests that took the old reading was updated, with a comment.
- The gaps listed above are recorded as known limits in NOTES.md.
