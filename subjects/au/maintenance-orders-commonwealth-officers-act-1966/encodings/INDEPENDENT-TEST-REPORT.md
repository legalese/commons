# Independent test report: Maintenance Orders (Commonwealth Officers) Act 1966

`tests-independent.l4`: **11 assertions, 11 satisfied, 0 failed**, no errors.

## Coverage

All 12 scenarios in `independent-expectations.md` pass:

- s 5 / s 6(1): pay can be attached only where the State or Territory law provides for it.
- s 7(1)(a): orders are complied with by date, whatever order they are listed in (scenario 7).
- s 7(1)(b): each order is paid from what is left after the earlier ones, including a capped order (6), earnings smaller than the first order (8), and three orders (10).
- s 7(3): a varied order is taken to date from when it was first made (9).
- The total paid never exceeds the earnings (12).

## Disagreements

None.

## Gaps (reading or modelling, not failures)

- **s 7(3) is handled by how the input is defined, not by a rule.** The user must supply the date the order first came into force, with the amount as varied. If the user gives the variation's date instead, the module will order the orders wrongly. The field comment says this, but nothing in the rules enforces it.
- **s 6(3) has no input.** "Notwithstanding any law that ... would prevent the attachment" is built into the result: attachable depends only on the State law boolean. So scenario 3 cannot be told apart from scenario 1.
- **"Against the one person" is assumed.** There is no person identifier, so every order in the list is treated as against the same person.
- **Orders made on the same day.** The insertion sort is stable, so ties keep their list order. The Act is silent on ties, and this was not asserted.
- **Out of scope.** s 7(2) (Matrimonial Causes Act Third Schedule priority) and any protected-earnings limits under State law.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
