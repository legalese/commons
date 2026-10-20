# Independent test report: Crimes (Hostages) Act 1989

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. `tests-independent.l4` asserts them against `ch-rules.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`: tests-independent.l4: **27 satisfied, 1 failed** (the 1 error is the failed assertion; no syntax errors).

## Scenarios covered

s 7 each element missing; s 8(1) act the day before, on, and after the Convention's entry into force; s 8(2) life; s 8(3)(a)(i), (a)(ii), (b)(i)-(iii) and no link; s 9(1)/Art 12; s 9(2) single-State case; s 6(2) (chargeable but not convictable); s 10(1)-(2) with and without consent, and consent with no offence; s 12(1) reappearance day (incl. leap February) and no order.

## Disagreements

**1. An act on the day the Convention entered into force for Australia.** Act on 20 Jun 1990, entry into force 20 Jun 1990. Mine: an offence. Code: not an offence (`the act was on GREATER THAN the Convention entered into force for Australia on`).

Source: s 8(1) "A person who, **at any time after the Convention enters into force for Australia**, commits an act of hostage-taking". A treaty enters into force on a date, conventionally from the beginning of that day, so an act at any time during that day is after it entered into force. The code's strict comparison treats the whole entry-into-force day as before. Confidence: low-medium; the inputs are days, not instants, so the edge is inherently a modelling choice. NOTES.md should state which reading was taken. (Practically moot for Australia, whose entry-into-force day is long past, but the rule is general.)

## Coverage gaps

1. s 9(2)-(3) is a single boolean combining four conditions and the extradition carve-out; the elements (and the extradition exception) are not separately testable.
2. Article 12's own conditions (States Parties bound under the Geneva Conventions to prosecute or hand over) are folded into one boolean.
3. s 8(3) is "Subject to section 9", and the module applies s 9 as an extra bar, which matches. But "chargeable" also requires an offence under s 8(1) — fine.
4. s 10(2) ("may be charged, arrested, remanded without consent") has no separate output; it is implied by `chargeable` being independent of consent.
5. s 12(1) preconditions (offence on an aircraft in flight, objection, court satisfied) are not inputs; the reappearance day is computed from any order date. Acceptable for the seat.
6. s 3 definitions of Australian ship/aircraft and Australia (coastal sea, external Territories) are left to the user's enum choice.

## Change after the pass (encoder)

- The disagreement was accepted: an act on the day the Convention entered into force is covered.
- The gaps are recorded as known limits in NOTES.md.
