# Independent test report: Protection of Cultural Objects on Loan Act 2013

Expectations were written to `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`check.sh`: tests-independent.l4: **37 satisfied, 0 failed**, no errors.

## Scenarios

The 23 scenarios cover:
- each s 8(1) condition failing in turn;
- each lender kind, including "another person";
- the 24-month edge, both an ordinary day and 29 February;
- export, tested on the day before and the day after;
- a valid Ministerial declaration, and a purported one inside 24 months;
- a day before import;
- each kind of proceeding;
- each power, for both seizure and forfeiture, including the police-only power that s 11 excepts and s 12 does not;
- the protection end date.

## Disagreements

None.

## Points to note (not failures)

- **Export day and declared day.** The encoding treats the export day and the declared day as the **last protected day** (`AT MOST e`). On the text, the Part ceases *when* the export occurs (s 8(2)(a)(ii)), and *at the time* the declaration works out (s 8(2)(b)). So on the day itself the object is protected for part of the day. My tests avoid the exact day. That simplification is reasonable for a day-granular model, but it should be stated in NOTES.md. Confidence: moderate.
- **Declaration conditions.** A declaration counts only if it is later than the 24-month end. That matches s 8(2)(b)(ii). The requirement that it be made *before* the 24 months end ("before an event described in paragraph (a) occurs") is not an input, so it is not tested.

## Coverage gaps

- The s 9(3) and s 10(2)-(3) exceptions (protected person against protected person; foreign judgment registration) are out of scope, as the brief says.
- The proceeding bar does not distinguish starting proceedings (s 9) from enforcing a judgment (s 10), and there is no input for a judgment already obtained.
- Movement between an external Territory and the mainland (s 8(5)) is not modelled.
- Proceeds of Crime is one option for both seizure and forfeiture. The Act's split by Part (3-5 for seizure; 2-2/2-3 for forfeiture) cannot be tested.
- `Part 2 applies to my object under s 8(1)` ignores the asked day. It is TRUE even before import or after the period ends. The time-sensitive answer is `it is protected on the day asked about`.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
