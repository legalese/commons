# Independent expectations: Removal of Prisoners (Territories) Act 1923

Written from BRIEF.md and the source text only, before reading any `.l4` file.

## Scenarios

| # | Facts | Expected | Act's words |
|---|---|---|---|
| E1 | Person sentenced to imprisonment in a Territory; not within the s 2(1) exclusion | is a prisoner | s 2(1) "Prisoner means any person sentenced to imprisonment in a Territory" |
| E2 | Same, but within the s 2(1) exclusion ("aboriginal native of a Territory") | not a prisoner | s 2(1) "but does not include an aboriginal native of a Territory" |
| E3 | Sentenced to death in a Territory, commuted to a 10-year term | is a prisoner, sentence = the commuted term | s 2(2) "shall be deemed to have been sentenced to imprisonment in the Territory for that term" |
| E4 | Sentenced to imprisonment in a State (not a Territory) | not a prisoner | s 2(1) "in a Territory" |
| E5 | Territory other than NT; Administrator finds no proper prison AND removal expedient for safer custody | Administrator may recommend | s 3(1)(a) |
| E6 | Same, but no proper prison and removal NOT found expedient | may not recommend on (a); no other ground → no | s 3(1)(a) requires both limbs ("by reason of ... no prison ... the removal ... is expedient") |
| E7 | Non-NT Territory; only ground (b) (life endangered / health permanently impaired) | may recommend | s 3(1)(b) |
| E8 | Non-NT Territory; only ground (c) (offence committed partly outside) | may recommend | s 3(1)(c) "wholly or partly beyond the limits" |
| E9 | Non-NT Territory; only ground (d) (class subject to removal under Territory law) | may recommend | s 3(1)(d) |
| E10 | Northern Territory; ground (b) found | may NOT recommend | s 3(1) "a Territory other than the Northern Territory" |
| E11 | Non-NT; no ground found | may not recommend | s 3(1) |
| E12 | Recommendation made, GG orders removal, receiving State concurs, no AG direction | removal may proceed | s 3(2), s 4(1), s 8AA(1) |
| E13 | As E12 but receiving State does not concur | no removal | s 3(2) "with the concurrence of the Government of the State or Territory" |
| E14 | As E12 but Attorney-General has directed in writing the Act not apply | not removed under this Act (Transfer of Prisoners Act 1983 governs) | s 8AA(1) |
| E15 | As E12 but no recommendation | no removal | s 3(2) "Upon the receipt of a recommendation" |
| E16 | As E12 but person is within the s 2(1) exclusion (not a "prisoner") | no removal | s 3 applies to "the prisoner" |
| E17 | Removed prisoner — where may conviction be questioned? | in the Territory of origin, as if not removed | s 5(2) |
| E18 | Removed; discharged at expiry in receiving State; return breaches no condition; not unlawful; applies | entitled to be sent back free of cost | s 8(3)(a)-(d) |
| E19 | As E18 but released on a s 8A licence rather than discharged | entitled | s 8(3)(b) "or ... released ... in pursuance of a licence" |
| E20 | As E19 but return would likely breach a licence condition | not entitled | s 8(3)(c) "would not result, or be likely to result, in a failure ... to comply with a condition" |
| E21 | As E18 but return to the Territory would be unlawful | not entitled | s 8(3)(d) |
| E22 | As E18 but never removed | not entitled | s 8(3)(a) |
| E23 | As E18 but neither discharged nor released (still serving) | not entitled | s 8(3)(b) |
| E24 | As E18 but no application made | not (yet) entitled to be sent | "on making application in such manner and within such time as is prescribed" |
| E25 | Escaped prisoner: 1000-day term, 400 days served before escape, at large 200 days, returned | sentence does NOT run while at large; must still undergo the 600 days left, in addition to any punishment for the escape | s 7A heading "Sentence ceases to run while escaped prisoner at large"; "the punishment that the person would have undergone if the person had not escaped" |
| E26 | Escaped and not yet returned to lawful custody | the s 7A duty is triggered "upon being returned"; no obligation answer until returned | s 7A |

## Where I read the Act differently from, or more precisely than, the brief

- **s 3(1)(a) has two parts.** The brief says "no proper prison and removal is expedient". The Act ties the two together ("by reason of there being no prison ... the removal ... is expedient for his or her safer custody or for the more efficient carriage of his or her sentence into effect"). Lacking a proper prison is not enough by itself (E6).
- **s 8(3) needs an application.** The entitlement is "on making application in such manner and within such time as is prescribed". The brief leaves the application out. I treat it as a condition (E24). An encoding that treats it as a procedural step only would differ.
- **s 7A answers "does my sentence keep running?" with "no".** The heading says the sentence *ceases* to run while the prisoner is at large. The text adds the punishment for the s 7(2) offence on top. Section 7 is not in this compilation, so the s 7(2) offence cannot be checked from the source.
- **s 8AA(1)** stops removal only "pursuant to a warrant under subsection 4(1)". It does not undo a s 3(2) order. Removal *under this Act* fails, but the order may still exist.
- **s 2(3)** (habitual-criminal detention counts as part of the "sentence") is not in the brief's scope. I do not test it.
- **s 2A**: in Territories with no Administrator, a substituted office acts as Administrator. This is out of scope and not tested.
