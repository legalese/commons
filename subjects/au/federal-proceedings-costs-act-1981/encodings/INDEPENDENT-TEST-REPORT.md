# Independent test report: Federal Proceedings (Costs) Act 1981 (`fpc-rules.l4`)

## Method

I wrote 24 scenarios to `independent-expectations.md` from BRIEF.md and `../registers/source-bundle/C2004A02401.txt` alone, before opening any L4. I then read `fpc-rules.l4` for names and input shapes only (not `fpc-tests.l4` or NOTES.md) and wrote `tests-independent.l4`, which asserts my expected values.

## Scenarios

Scenarios 1-24 are in `independent-expectations.md`. They cover:
- every forum in the Schedule, with costs below, at and above the cap;
- the s 10 cap exemption (s 18(2)) and the Tribunal cap (s 18(2A));
- a prescribed amount higher and lower than the Schedule (s 18(1));
- every s 14 class and "no route";
- s 15 vacation for ss 7 and 9, and non-vacation for ss 7A and 8;
- s 17 with no notice, with an appeal pending, and with certificates outside s 15 (ss 7A, 10, 10A);
- the s 15(1) party for a s 6 certificate.

The encoding merges ss 6(1) and 6(2) into one route, and ss 10(2) and 10(3) into one.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **37 satisfied, 1 failed**, and no other errors (its single error is the failed assertion). fpc-tests.l4: 17 satisfied, 0 failed.

## Disagreements

### D1: s 15(1) vacation of a s 6 certificate (tests-independent.l4 line 91, scenario 24)

Route s 6 (respondent to a Federal appeal). The other side appealed further and succeeded. I expect the certificate **not vacated**; the encoding says vacated.

s 15(1): "A costs certificate granted under subsection 6(1) or (2) to a respondent to a Federal appeal is vacated if **the respondent to whom the certificate has been granted**: (a) appeals from the judgment in that appeal; and (b) is a successful party in the appeal from that judgment ...".

For a s 6 certificate, the party whose further appeal and success vacates it is the certificate holder, not the other side. Only s 15(2) (s 7) and s 15(3) (s 9) turn on the other party, the respondent. `my certificate is vacated` (fpc-rules.l4 lines 87-90) uses "the other side appealed further and succeeded" for all three routes.

The policy behind the text: a respondent who later wins outright can recover costs in the ordinary way. If the other side appeals and wins against a s 6 holder, nothing in s 15 vacates the certificate.

Confidence: high on the text. The fix needs a separate input for "I appealed further and succeeded" on the s 6 route.

The same misattribution affects s 17 for the s 6 route. Under s 17(2), the respondent "an appeal by whom could result in the vacation of the certificate" is the s 6 holder. The notice under s 17(2)(b)(i) comes from that holder. The encoding instead tests "the other side has appealed or sought leave" (line 129). I did not add a separate failing assertion for this; it follows from D1.

## Coverage gaps and observations

- s 17(1) "unless he or she is satisfied" (the A-G's own satisfaction that the certificate will not be vacated) is not modelled. Only the s 17(2) presumption counts, so the A-G can never pay a s 15 certificate without a notice.
- Routes are not checked against the forum. For example, a s 10A route at the High Court, or s 9 outside the family-law appeals in s 9(1)(a), is not rejected. The s 10(1) list of courts is also not checked. Not tested.
- s 7(2) partial amounts (part of the relevant costs the respondent can't pay) and the "such part as the A-G considers appropriate" in ss 8(3) and 10(4) are folded into "my costs" as an upper bound. That is consistent with "may pay at most".
- When a certificate is vacated the encoding returns 0 as the maximum. That is consistent with s 16(1), but I asserted it only indirectly, through "may pay now".

## Change after the pass (encoder)

- One disagreement is left open: s 15(1) turns on the holder's own further appeal, which the encoding has no separate input for (`tests-independent.l4` line 91 is expected to fail).
- The gaps are recorded as known limits in NOTES.md.
