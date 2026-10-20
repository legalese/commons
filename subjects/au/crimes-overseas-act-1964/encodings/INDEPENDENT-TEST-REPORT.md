# Independent test report: Crimes (Overseas) Act 1964

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. `tests-independent.l4` asserts them against `co-rules.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`: tests-independent.l4: **22 satisfied, 4 failed** (the 4 errors are the 4 failed assertions; no syntax errors).

## Scenarios covered

s 3 Australian (both limbs and neither); s 3A(1) diplomatic immunity; s 3A(2) continuing local prosecution, and that it qualifies only (1) not (3); s 3A(3), (4), (5)/(6) routes; category in/out for (4)-(6) and its irrelevance to (1); ground none; s 3A(10)(a) and (b), including overriding (5); s 4(1)(b) no breach; s 4(2) consent / no consent / consent where the Act does not apply; s 4(4) arrest before consent; s 8(6), s 8(8)(a) dates, including a leap-year February crossing.

## Disagreements (all four are the same point)

| Test | Mine | Code |
|---|---|---|
| s 8(6), tender 20 Mar 2025 | 5 Mar 2025 | 6 Mar 2025 |
| s 8(6), tender 10 Mar 2024 | 24 Feb 2024 | 25 Feb 2024 |
| s 8(8)(a), hearing 20 Mar 2025 | 15 Mar 2025 | 16 Mar 2025 |
| s 8(8)(a), hearing 2 Mar 2024 | 26 Feb 2024 | 27 Feb 2024 |

Source: s 8(6) "has, **at least 14 days before** the certificate is sought to be so admitted, been given a copy"; s 8(8)(a) "**at least 4 days notice**". The code subtracts 14 and 4 from the day. My reading: "at least N days" before an event is conventionally N *clear* days (both the day of service and the day of the event excluded; Acts Interpretation Act 1901 s 36(1) excludes the event day, and "at least" is the long-standing marker of clear days in the common-law authorities). On that reading a copy given exactly 14 days before (day T-14) leaves only 13 clear days, so the last day is T-15 (and H-5 for the notice). Confidence: medium. If the encoder deliberately adopted the simple-subtraction reading, NOTES.md should say so and why; as encoded, a defendant served on T-14 is told service was in time when it arguably was not.

## Coverage gaps

1. s 3A(1)(b) distinguishes three immunity sources and s 3A(3)(c) two agreement sources; the module collapses these into one `Ground` value each, which is fine for the outcome but untestable separately.
2. s 3A(5) (declared country) and (6) (declared part) share one value; their separate category conditions cannot be tested.
3. s 3A(7)-(9) (off-duty acts during the relevant period, arrival/departure periods) are not modelled; the user must decide "working under" themselves.
4. s 3A(2) "at a particular time after the act occurs" is a time-varying condition; modelled as a single boolean.
5. The ground is a single enum, so a person qualifying on two routes (e.g. diplomatic immunity lost under s 3A(2) but also working in a declared country) cannot be expressed; the code would answer "does not apply" when s 3A(5) would apply. Untested because inexpressible; worth noting.
6. s 8(8)(b) (court order allowing the call without notice) is out of scope per brief.

## Change after the pass (encoder)

- One disagreement is left open: the tester reads s 8's 14 and 4 days as clear days (`tests-independent.l4` lines 72, 75, 78, 81 are expected to fail).
- The gaps are recorded as known limits in NOTES.md.
