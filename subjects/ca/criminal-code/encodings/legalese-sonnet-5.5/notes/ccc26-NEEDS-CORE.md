# NEEDS-CORE.md -- ccc26 (ss 716 to 736, Criminal Code (Canada))

What part ccc26 wanted from the core (`ccc-core.l4`) and did not find.
Each item says what stands in for it in this part, so that the lead can hoist the wanted name and delete the stand-in.
Nothing in this file changes `ccc-core.l4`; this part defined only names that begin with `s <label>`.

## 1. An order on `Length of time`

Wanted: a comparison of two `Length of time` values (at most, less than), with the text's own rule for months and for "less a day".
Why: the text compares a term with a stated length in s 730(1) ("fourteen years"), s 731(1)(b) ("two years"), s 732(1)(a) and (b) ("ninety days or less"), s 732.2(5)(e) ("one year") and s 736(1) ("two years"); each of those functions calls the stand-in below (checked by grep over the layer-1 modules).
The core has `Length of time` (years, months, days, a "less a day" flag) and constants such as `ninety days` and `two years less a day`, but no order.
Stand-in: `s 716 the first period is at most the second period` in `ccc26-interpretation.l4`, answering `MAYBE BOOLEAN`.
A month is put at 28 to 31 days, so the answer is `JUST TRUE` or `JUST FALSE` when every calendar agrees and `NOTHING` when the calendar decides (three months against ninety days: 89 to 92 days).
It is exact when the two months counts are equal or both periods are in days.
If the core takes the comparison, it should keep the three-valued answer: a caller must not read `NOTHING` as no.

## 2. A `Party` for the minister of justice of a territory

Wanted: a constructor of `Party` for "the minister of justice of a territory".
Why: s 732.1(8), (9) and (11) name "the Attorney General of a province or the minister of justice of a territory".
Stand-in: `` `the Attorney General` `` (the core's `Party`, "as s 2 defines it"), used in `s 732.1(11) the Attorney General's duty to cause the samples to be destroyed` in `ccc26-probation.l4`.
The duty of s 732.1(11) also falls on "a person authorized by the Attorney General or minister"; this part does not name that person as a party: the duty is stated for the Attorney General alone.
