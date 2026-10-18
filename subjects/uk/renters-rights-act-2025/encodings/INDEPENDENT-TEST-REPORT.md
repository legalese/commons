# Independent test report — Renters' Rights Act 2025 encoding

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any `.l4` module was read. Tests are in `tests-independent.l4`; `rra-tests.l4` was not read.

## Counts

- Scenarios written: 84 (A1–A21, B1–B25, C1–C5, D1–D8, E1–E5, F1–F6, G1–G15).
- Assertions: 80 in `tests-independent.l4`.
- Result (`L4=~/.local/bin/l4 ./check.sh`): **80 satisfied, 0 failed, 0 other errors**. The whole encoding totals 117 satisfied and 0 errors.
- 13 scenarios could not be asserted because the encoding's types have no way to express them (see Remarks 1–5).

## Failures

None. Every value the encoding's interface can express matched the value fixed beforehand, including these edges:

- s 4A(3): 28 days permitted; 29 and 30 days (not monthly) not permitted.
- s 4B(12): a later rent period ending exactly on day 28 (22–28 June; 15–28 June for 14-day periods) is initial rent. A period ending on day 29 or later is not. The first period is always initial.
- Permitted pre-tenancy period: rent due on the day the tenancy is entered into, and on the day before its first day, is permitted. Rent due the day before entry is of no effect. Initial rent due after the tenancy began but before its own period (B12) is of no effect.
- Substitute rent day: the regular rent day where one is given, otherwise the first day of the period. Where the term stands, the day under the terms.
- TFA para 1(1A): rent payable on the day of entry is not prohibited; payable the day before is prohibited; a non-assured tenancy is not caught.
- s 57(2): the window runs from the day after the corresponding date five years earlier, up to and including the new date. Every 29 February case came out as expected: new 29 Feb 2032 gives a window from 1 Mar 2027; new 28 Feb 2033 includes 29 Feb 2028; new 1 Mar 2033 excludes it. A same-day earlier penalty is inside the window. An earlier penalty dated after the new one is outside it. A different subsection, or a withdrawn or quashed notice, gives no additional penalty.

## Remarks (scenarios the interface cannot express; possible gaps)

1. **s 4A(8), monthly with a different first period (A11–A13).** `monthly` has no fields, so there is no way to say "the first period is 31 days". A 31-day first period should stop the periods being "monthly" (4A(8): "not exceeding 30 days"). As encoded, the encoder has to decide that before choosing the constructor. Consider adding a first-period length to `monthly`.
2. **s 4A(4), different rent periods at different times (A17–A18).** `Tenancy terms` holds one `Rent period kind`, so "weekly, then quarterly" cannot be stated or tested. Consider a list of kinds, each of which must be permitted.
3. **s 4A(5), the substitute monthly periods (A19).** The encoding gives no periods beginning with the first day of the tenancy and no rent due on the first day of each period. It only says the periods are not permitted. The brief lists (5) in scope; only the (6) amount is excluded.
4. **s 56(2) and (3) collapsed into booleans.** "Relevant person" (D7) is not an input. "A specific amount" and "states the proposed rent" (D3 vs D2) are merged into one flag, `a specific rent was stated`. "Exceeds the stated rent" (E2–E4) is a single flag, `invited or accepted an offer above the stated rent`, so the encoding never compares an offer with the stated rent. The comparisons the Act makes are therefore inputs, not rules.
5. **s 57(2) takes one earlier penalty (G14).** Several earlier penalties have to be checked one at a time by the caller. The function also does not require that a new penalty under s 57(1) is in fact being imposed (s 57(2)(a)). The caller has to assume it.
6. **s 4B(4), (6)–(7), regular pattern.** Whether the compliant periods have a regular pattern, and which day is the regular rent day, is an input (`regular rent day in this period`, a MAYBE DATE). The encoding does not check that the day given falls inside the period. A regular rent day outside the period is returned as-is.
7. **The top-level goal.** `runs as a periodic tenancy` is just `an assured tenancy`. It does not use the s 4A(1) result, though after s 4A every assured tenancy is periodic, so the value is defensible. The TFA para 1(1A) prohibition is exported but is not part of the top-level position.
8. **No `REFUSE` anywhere.** For a non-assured tenancy, the s 4A and s 4B goals return FALSE. That is defensible, because those sections apply only to assured tenancies. The brief's REFUSE rule does not obviously apply.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md:
- the monthly first period of s 4A(8);
- changing rent periods (s 4A(4));
- the substitute monthly periods (s 4A(5));
- s 56 inputs;
- one earlier penalty at a time;
- the regular rent day as input;
- the top-level periodic field.
