# Independent test report: Weapons of Mass Destruction (Prevention of Proliferation) Act 1995

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. `tests-independent.l4` asserts them against `wmd-rules.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`: tests-independent.l4: **33 satisfied, 1 failed** (the 1 error is the failed assertion; no syntax errors).

## Scenarios covered

ss 9, 10, 11 each dealing; no belief; permit kept / breached; s 12 all-clear; s 6(3) in Australia, Australian abroad, foreigner abroad (for both ss 9-11 and s 14(6)); s 9(2) compliance with a conditional notice; s 14(6) breach of conditions, prohibiting notice with and without knowledge, revoked notice, dealing before the notice, dealing on the last day and the day after; s 14(4) end dates (ordinary, 31 Jan, 29 Feb); s 17(1) goods forfeited, services not; maximum 8 years / 0 when no offence.

## Disagreements

**1. Last day in force of a s 14 notice given on 29 Feb 2024.** Mine: 28 Feb 2025. Code: 27 Feb 2025.

Source: s 14(4) "remains in force for a period of **12 months beginning on the day when the notice is given**". A 12-month period beginning on 29 Feb 2024 runs to the end of the day before the corresponding day in Feb 2025; there is no 29 Feb 2025, so the period ends at the end of February 2025 (the Acts Interpretation Act 1901 s 2G rule for periods of months: where the last month has no corresponding day, the period ends at the end of that month). The code computes `the day before (add months d 12)`; `add months` clamps 29 Feb 2024 + 12 months to 28 Feb 2025 and the day before that is 27 Feb 2025, losing a day. The same off-by-one will hit any notice given on the 29th-31st of a month whose 12-months-later month is shorter (only February in practice: notices given 29 Feb in a leap year). Confidence: medium-high. Practical effect: a person who knowingly deals on 28 Feb 2025 is told no notice binds them when on this reading it still does.

## Coverage gaps

1. The permit is one boolean ("a permit authorises it and I keep its conditions"), so "no permit" and "permit with breached conditions" (both offences under s 9(1)(c)) are indistinguishable inputs.
2. s 14(6) "in contravention of a notice ... in force": the module treats a conditional notice as contravened whenever `I comply with the notice's conditions` is false. Fine; but the notice's scope (particular goods, person or place under s 14(1)-(2)) is assumed to match the dealing.
3. Revocation is a boolean, not a date: a notice revoked after the dealing (so still in force when I dealt) cannot be expressed; setting it TRUE always takes the notice out of force. Untestable; worth an input date.
4. s 14(5) successive notices are out of scope.
5. s 17(1) covers *attempts* to export or supply; attempts are not an input.
6. s 17(1) forfeiture is tied to an offence; a contravention of a s 14 notice without knowledge (no s 14(6) offence) is arguably still "in contravention of this Act" for forfeiture. Low-confidence point, not asserted.
7. s 15(5) (no imprisonment where liability rests only on agent attribution) and the Crimes Act fine notes are out of scope; the maximum is always 8 years.

## Change after the pass (encoder)

- The disagreement was accepted: a notice given on 29 February ends on 28 February.
- The gaps are recorded as known limits in NOTES.md.
