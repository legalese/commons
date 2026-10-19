# Independent expectations: Defence Forces Retirement Benefits (Pension Increases) Act 1973

Written from BRIEF.md and `../registers/source-bundle/C2004A00007.txt` only, before reading any `.l4` file.

## Working conventions

- CPI rise = ((A − B) ÷ B) × 100; earnings rise = ((C − D) ÷ D) × 100 (the brief's reading of the missing s 4(2) formulas).
- Prescribed percentage (s 4(2)) = lower of 1.4 × CPI rise and earnings rise, then s 4(4) rounding to the nearest tenth, a half-tenth rounding up. Rounding is applied to the prescribed percentage ("If the prescribed percentage ... is or includes a fraction of one-tenth"), i.e. after the lower is chosen. Because rounding is monotone, rounding before or after choosing the lower gives the same answer, so no scenario can tell the two apart.
- s 5(2): increase = prescribed % × 77.5% × annual pension immediately before 1 July 1973.
- s 7(2): where retirement/death is on or after 1 October 1971, increase × (months ÷ 21), months counted from the day after the retirement/death to 30 June 1973, with s 7(5) part-month rounding (a part of half or more of the days of that month counts as a month) and s 7(4) (under a month = one month).
- Month counting: I count whole months from the start day (e.g. 16 Mar 1972 to 15 Jun 1973 is 15 months), the left-over tail lying in June 1973 (30 days). Every s 7 scenario below is chosen so that counting by calendar months instead (part of the first month + whole calendar months) gives the same number.

Unless stated, A = 110, B = 100 (CPI rise 10 %, × 1.4 = 14 %), C = 120, D = 100 (earnings rise 20 %), annual pension £/$1000, retirement 1 January 1970, not a child's pension.

## Scenarios

| # | Facts | Expected | Working | Act's words |
|---|---|---|---|---|
| 1 | Defaults (CPI limb lower) | prescribed % 14; increase 108.5 | 14 % × 77.5 % × 1000 = 108.5; retirement before 1 Oct 1971 so no s 7 | s 4(2)(a) "1.4 times the percentage"; s 5(2) "the prescribed percentage of seventy-seven and one-half per centum" |
| 2 | C = 105, D = 100, pension 2000 (earnings limb lower) | prescribed % 5; increase 77.5 | min(14, 5) = 5; 5 % × 0.775 × 2000 = 77.5 | s 4(2) "whichever is the lower" |
| 3 | A = 105, C = 107 (tie at 7) | prescribed % 7; increase 54.25 | 1.4 × 5 = 7 = 7; 0.07 × 775 = 54.25 | s 4(2) |
| 4 | C = 10464, D = 10000 | prescribed % 4.6; increase 35.65 | earnings rise 4.64; fraction 0.04 of a tenth < 0.05 → dropped; 0.046 × 775 = 35.65 | s 4(4)(a) "less than one-half of one-tenth—that fraction shall be disregarded" |
| 5 | C = 10465, D = 10000 | prescribed % 4.7; increase 36.425 | earnings rise 4.65; fraction exactly half a tenth → treated as a tenth; 0.047 × 775 = 36.425 | s 4(4)(b) "not less than one-half of one-tenth—... treated as one-tenth" |
| 6 | A = 1033, B = 1000 (CPI limb 4.62) | prescribed % 4.6 | 3.3 × 1.4 = 4.62 → 4.6 (earnings 20 higher) | s 4(4)(a) |
| 7 | A = B = 100 | no increase (0) | s 5(1)(a) CPI did not exceed | s 5(1)(a) "exceeds" |
| 8 | C = 100 = D | no increase (0) | s 5(1)(b) not met | s 5(1)(b) "exceeds" |
| 9 | child's pension | no increase (0) | excluded | s 5(1) "(not being a pension payable to or in respect of an eligible child)" |
| 10 | retirement 30 Sept 1971 | 108.5 (no s 7 scaling) | before 1 Oct 1971 | s 7(1)(a) "on or after 1st October, 1971" |
| 11 | retirement 1 Oct 1971 | months 21; increase 108.5 | period 2 Oct 1971–30 Jun 1973: 20 whole months to 1 Jun 1973, then 2–30 Jun = 29 days ≥ 15 → 21 months; 21/21 | s 7(2), 7(5)(b) |
| 12 | retirement 30 June 1972 | months 12; increase 62 | 1 Jul 1972–30 Jun 1973 = 12 months; 108.5 × 12/21 = 62 | s 7(2) "bears to twenty-one" |
| 13 | retirement 15 Mar 1972 | months 16; increase 82.666… (248/3) | 16 Mar 1972–15 Jun 1973 = 15 months; 16–30 Jun = 15 days = half of June's 30 → counts → 16; 108.5 × 16/21 = 248/3 | s 7(5)(b) "not less than one-half" |
| 14 | retirement 16 Mar 1972 | months 15; increase 77.5 | 17 Mar 1972–16 Jun 1973 = 15 months; 17–30 Jun = 14 days < 15 → dropped; 108.5 × 15/21 = 77.5 | s 7(5)(a) "less than one-half ... disregarded" |
| 15 | retirement 30 Sept 1972 (last day a "pension" can arise) | months 9; increase 46.5 | 1 Oct 1972–30 Jun 1973 = 9 months; 108.5 × 9/21 = 46.5 | s 4(1) "pension", s 7(2) |
| 16 | widow; husband retired 1 Jan 1970, died 1 Jan 1973 | 108.5 (no scaling) | s 4(5): widow's pension deemed to be in respect of his retirement, so the retirement date governs | s 4(5) "shall be deemed to be a pension payable in respect of the retirement of the contributor" |
| 17 | widow; husband died in service 30 June 1972 | months 12; increase 62 | death date governs | s 7(1)(a) "retirement or death" |
| 18 | effective date | instalment due 5 July 1973 | | s 12 "the pension pay-day that occurs on 5th July, 1973" |

## Where I read the Act differently from the brief, or the brief is silent

- **s 7(4) under-a-month.** The brief lists "under a month counts as one". But "pension" (s 4(1)) only covers retirement or death on or before 30 September 1972, so the s 7(2) period is always at least 9 months for an s 7(1)(a) pension; s 7(4) can only bite for the out-of-scope s 82ZB limb (s 7(1)(b)). I therefore expect a retirement on, say, 20 June 1973 to yield **no increase at all** (it is not a "pension" under this Act), not a 1/21 share. If the encoding does not model the s 4(1) cut-off, it will give 1/21 of the increase; I record that as a disagreement with the Act rather than with the brief.
- **s 4(5) widow.** The brief lists s 4(5) but does not say what date drives s 7 for a widow whose husband died after retirement; I read s 4(5) as making the retirement date govern (scenario 16).
- **Rounding order.** Immaterial (see conventions).
- **Month counting method.** The Act does not say how to count months; scenarios are chosen to be method-independent.
