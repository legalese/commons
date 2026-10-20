# Independent test report: Defence Force Retirement and Death Benefits (Pension Increases) Act 1976

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text only, before any L4 was read. `tests-independent.l4` asserts them against `dfrdb76-rules.l4`.

## Result

`check.sh`: tests-independent.l4 — **32 assertions: 31 satisfied, 1 failed**, no other errors.

## Scenarios asserted (agreeing)

- Part II prescribed percentage: CPI-bound (14%) and AWE-bound (12.34 -> 12.3%) cases; rounding down (4.648 -> 4.6), up (4.662 -> 4.7) and exactly half (4.55 -> 4.6); no increase where either index failed to rise; nil for a child's DFRB pension; s 7 year.
- s 10 month counting: 1 Oct 1971 retirement -> 21/21; 31 Dec 1972 -> 6/21; part-month boundary (14 days of June -> disregarded; 15 days -> counted); s 82ZB pension from 1 Jan 1973 (period counted from the day payable); under one month -> 1; s 82ZB pension payable 16 Jun 1973 -> nil.
- s 11: 6/12, 1/12, nil after 15 June.
- Part III: 17.6%, rounding at 17.64/17.65, no CPI rise, child's additional pension, s 21 scaling (12/12, 6/12, 1/12), nil for a benefit payable after 15 June 1975.

## Disagreement (failing assertion)

**s 10(3) applied to a retirement pension (tests-independent.l4 line 50).** A contributor retired on 20 June 1973 (s 10(1)(a), not a s 82ZB pension), pension payable from 21 June. The module gives nil, because `it came too late` bars every scaled pension that became payable after 15 June. I expect £10 (210 x 1/21): s 10(3) reads "If the pension in accordance with section 82ZB ... became payable after 15 June 1973, the person is not entitled to the increase under section 6" — it is confined to s 82ZB pensions. For a s 10(1)(a) retirement or death case, s 10(2) and (4) apply and the period (21-30 June) is treated as 1 month. Section 11(3) is likewise confined to s 82ZB pensions (s 11 only ever covers them, so no practical difference there). Contrast Part III, where s 21(1)(a) and (b) both expressly exclude a benefit "that became payable after 15 June 1975", so the module's rule is right for Part III. The brief's summary ("A pension that became payable after 15 June before the period ends gets none") appears to have generalised s 10(3) beyond its words. Confidence: medium-high (whether such a pension was "payable immediately before 1 July 1973" for s 6(1) is satisfied on the facts given).

## Coverage gaps and observations

- Whether s 10, s 11 or s 21 applies at all (retirement on/after 1 Oct 1971 or 1 Jul 1974; s 82ZB pension; the s 20(1)(b) widow/child exception; s 10(6) re-entry rule) is left to the caller's `period kind`. A caller who selects a scaled kind for a pre-1 October 1971 retirement gets more than 21/21 of the increase (no cap); asserted only with `not scaled`.
- Similarly the choice between "day after retirement or death" and "day the pension became payable" is the caller's; the Act ties it to the route (s 10(2)/(1)(a) vs (1)(b); s 21(3)/(1)(a) vs (1)(b)).
- s 7's B and D ("highest ... March quarter of any earlier year not earlier than 1972-73") are inputs, so the "highest" selection is untested.
- The s 8 non-contributory portion is an input (out of scope).
- The s 6(1)/7(1) condition "in receipt of a pension immediately before 1 July" is not modelled.

## Change after the pass (encoder)

- The disagreement was accepted: s 10(3)'s 15 June bar now applies only to s 82ZB pensions.
- The gaps are recorded as known limits in NOTES.md.
