# What ea2 would like the core (ea-core.l4) to hold

1. **A shared Yes / No / I am not sure type for the seat layer.**
   ea2's seat declares its own, prefixed `ea2 seat: my answer` (with the constructors `ea2 seat: Yes`, `ea2 seat: No`, `ea2 seat: I am not sure`) and the mapping `ea2 seat: what I say, as a fact` to a MAYBE BOOLEAN.
   The merged seat layer imports three parts at once, so each part's copy must be prefixed; a single typed answer and one mapping in the core would remove the three copies and keep the wording of the question the same for the person.
2. **`Penalty on conviction` cannot tell "no imprisonment" from "no maximum stated".**
   The core says `longest imprisonment in months` is a MAYBE NUMBER in which NOTHING means the text states no maximum.
   Section 90(1) states a fine for a first offence and no imprisonment at all; ea2 wrote `JUST 0` for that cell (`s 90(1) the penalty on conviction`, first offence), which reads as "no imprisonment may be imposed" but is a number standing in for a text's silence about imprisonment on a first offence, not a maximum the text states.
   The same cell would read the same for a text that said "imprisonment not exceeding 0 months".
   A third state in the core's type (for example a constructor for "none stated") would separate the three cases: a stated maximum, no maximum stated, and no such penalty.
3. **A pattern for "the public holidays".**
   Layer-1 rules that count days take `the public holidays` as a LIST OF DATE.
   A person cannot state a list, so the seat asks "is the day that would be the last day a public holiday?" and builds a list of at most that one day (assumption A1 in NOTES.md).
   A core type for the public-holiday calendar, with a question the seat can ask once, would make the Interpretation Act's day counts usable without that assumption.
4. **A constructor-level `JUST 0` convention for amounts.**
   Four rules in ea2 answer `JUST 0` where the text says no to an amount, because an amount cannot be FALSE: `s 76(1A) gathered with s 80(3): the amount of the payment`, `s 88A(8) the amount the employer must pay for the paid annual leave not taken`, `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period`, and the first-offence imprisonment cell of `s 90(1) the penalty on conviction`.
   A date, a period and a penalty record have the same gap; ea2 closes it with a yes/no twin for each (NOTES.md, F18).
   The core could hold one named value (for example "no payment") so that the readers of every part see the same marker (NOTES.md, Marginal readings 2 and 3, and F19).
