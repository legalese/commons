# Independent expectations — TMA 1970 self-assessment encoding

Written from BRIEF.md and the Act text (ukpga-1970-9.txt, point in time 25 June 2026) only, before any `.l4` file was opened.
Tax year Y is written as the calendar year it begins in (2024 = 2024-25). Unless stated, Y = 2024.

## Readings adopted (from the brief)

- R1. s 7(1C)(a) "6 months from the end of the year of assessment" ends 5 October Y+1.
- R2. "the period of 3 months beginning with the date of the notice" ends the day before the corresponding date three months later; if that month has no corresponding date, it ends on the last day of that month.
- R3. s 9ZA(2) "not more than twelve months after the filing date": on or before the corresponding date 12 months later. s 9A(2)(a): the corresponding date 12 months after delivery.
- R4. s 9A(2)(b)-(c) "the quarter day next following the first anniversary": the first quarter day (31 Jan, 30 Apr, 31 Jul, 31 Oct) strictly after the anniversary. An anniversary that is itself a quarter day moves to the next one ("next following").
- R5. s 59B(6): notice date + 30.
- R6. ss 34, 36, 36A: on or before 5 April Y+1+N. Where several apply, the longest governs (s 36(1) is "subject to (1A)"; s 36A(2) is "subject to section 36(1A)"; s 34 is "subject to ... any other provisions ... allowing a longer period").
- R7. s 59A prescribed figures are inputs. I use £1,000 and 20% (the 1996 regulations' figures) in the scenarios; at exactly the prescribed amount/proportion the section applies ("not less than").
- R8. s 9A(6) filing date = "the last day for delivering it in accordance with section 8": so it depends on paper/electronic and on the s 8(1F)/(1G) exceptions. s 9ZA(3) filing date is different: 31 January Y+2 unless the notice was given after 31 October Y+1 (paper/electronic irrelevant).
- R9. s 8(1F)(b) "on or before 31st January" = 31 January Y+2.

## Ambiguities

- A1. Twelve months after 29 February (s 9ZA(2), s 9A(2)(a)): no corresponding date. I read it as 28 February of the next year (the last day of the corresponding month), by analogy with R2. Scenarios C6 and D15 depend on this.
- A2. A first anniversary of 29 February (s 9A(2)(b)): 28 Feb or 1 Mar — both give the same next quarter day (30 April), so D14 is unaffected.
- A3. s 8(1F)(a): a paper return under Exception 1 can end *after* 31 Oct (e.g. notice 15 Aug -> 14 Nov), but with a notice on 31 October the 3-month period ends 30 January, one day earlier than the electronic date. I follow the words.
- A4. s 9A(2)(c) for an amended return: I take the window for the amendment as the (c) date. Where that is later than the (a)/(b) window, the last day for any notice of enquiry is the (c) date.
- A5. s 59B(3)(a) "within six months from the end of the year of assessment": on or before 5 October Y+1 (as R1).
- A6. s 59A(1)(a) "assessed ... in any amount": an assessed amount of 0 means the section does not apply (also (b) fails).
- A7. ss 36/36A: an offshore loss with no carelessness still gets 12 years (s 36A(1)-(2) do not require carelessness). s 36A(7)-(9) exclusions are out of scope.

## A. s 7 — last day to notify chargeability (s 7(1), (1A), (1C)(a))

| # | Inputs | Expected | Words |
|---|---|---|---|
| A1 | Y 2024 | 5 Oct 2025 | "the period of 6 months from the end of the year of assessment" |
| A2 | Y 2023 | 5 Oct 2024 | same |
| A3 | Y 2027 | 5 Oct 2028 | same |

## B. s 8(1D)-(1G) — filing date (Y 2024 unless stated)

| # | Notice date | Return | Expected | Words |
|---|---|---|---|---|
| B1 | 20 Apr 2025 | paper | 31 Oct 2025 | (1D)(a) "on or before 31st October in Year 2" |
| B2 | 20 Apr 2025 | electronic | 31 Jan 2026 | (1D)(b) "on or before 31st January in Year 2" |
| B3 | 31 Jul 2025 | paper | 31 Oct 2025 | (1F) needs notice "after 31st July" — not met |
| B4 | 31 Jul 2025 | electronic | 31 Jan 2026 | same |
| B5 | 1 Aug 2025 | paper | 31 Oct 2025 | (1F)(a) "3 months beginning with the date of the notice" (corresponding date 1 Nov, day before) |
| B6 | 1 Aug 2025 | electronic | 31 Jan 2026 | (1F)(b) |
| B7 | 15 Aug 2025 | paper | 14 Nov 2025 | (1F)(a) |
| B8 | 31 Aug 2025 | paper | 30 Nov 2025 | (1F)(a), R2: no 31 Nov |
| B9 | 30 Sep 2025 | paper | 29 Dec 2025 | (1F)(a) |
| B10 | 31 Oct 2025 | paper | 30 Jan 2026 | (1F) "on or before 31st October"; A3 |
| B11 | 31 Oct 2025 | electronic | 31 Jan 2026 | (1F)(b) |
| B12 | 1 Nov 2025 | paper | 31 Jan 2026 | (1G) "after 31st October ... (whether electronic or not) ... 3 months" |
| B13 | 1 Nov 2025 | electronic | 31 Jan 2026 | (1G) |
| B14 | 15 Nov 2025 | electronic | 14 Feb 2026 | (1G) |
| B15 | 30 Nov 2025 | electronic | 28 Feb 2026 | (1G), R2: no 30 Feb 2026 |
| B16 | 31 Dec 2025 | paper | 30 Mar 2026 | (1G), corresponding date 31 Mar exists |
| B17 | Y 2026, 30 Nov 2027 | electronic | 29 Feb 2028 | (1G), R2, leap year |
| B18 | Y 2026, 29 Nov 2027 | paper | 28 Feb 2028 | (1G), 29 Feb 2028 exists, day before |
| B19 | 10 Jun 2026 | electronic | 9 Sep 2026 | (1G), notice well after Year 2 |

## C. s 9ZA — last day to amend (filing date per s 9ZA(3))

| # | Notice date | Return | Expected | Words |
|---|---|---|---|---|
| C1 | 20 Apr 2025 | electronic | 31 Jan 2027 | (3)(a) "31st January of Year 2"; (2) "not more than twelve months after" |
| C2 | 1 Aug 2025 | paper | 31 Jan 2027 | (3)(a) — paper/Exception 1 irrelevant (R8) |
| C3 | 31 Oct 2025 | electronic | 31 Jan 2027 | (3)(b) needs "after 31st October" |
| C4 | 1 Nov 2025 | electronic | 31 Jan 2027 | (3)(b) filing date 31 Jan 2026 |
| C5 | 15 Nov 2025 | electronic | 14 Feb 2027 | (3)(b) filing date 14 Feb 2026 |
| C6 | Y 2026, 30 Nov 2027 | electronic | 28 Feb 2029 | filing date 29 Feb 2028; A1 |
| C7 | 31 Dec 2025 | paper | 30 Mar 2027 | filing date 30 Mar 2026 |

## D. s 9A(2) — last day for a notice of enquiry

| # | Facts | Expected | Words |
|---|---|---|---|
| D1 | notice 20 Apr 2025, electronic, delivered 15 Jan 2026 | 15 Jan 2027 | (2)(a) "twelve months after the day on which the return was delivered" |
| D2 | same, delivered 31 Jan 2026 (the filing date) | 31 Jan 2027 | (2)(a) "on or before the filing date" |
| D3 | same, delivered 1 Feb 2026 (late) | 30 Apr 2027 | (2)(b) anniversary 1 Feb 2027 |
| D4 | notice 20 Apr 2025, paper, delivered 31 Oct 2025 | 31 Oct 2026 | (2)(a) |
| D5 | notice 20 Apr 2025, paper, delivered 1 Nov 2025 (late) | 31 Jan 2027 | (2)(b) anniversary 1 Nov 2026 |
| D6 | notice 20 Apr 2025, paper, delivered 20 Dec 2025 (late) | 31 Jan 2027 | (2)(b) |
| D7 | notice 20 Apr 2025, electronic, delivered 30 Apr 2026 (late) | 31 Jul 2027 | (2)(b), R4: anniversary 30 Apr 2027 is a quarter day |
| D8 | same, delivered 31 Jul 2026 | 31 Oct 2027 | R4 |
| D9 | same, delivered 31 Oct 2026 | 31 Jan 2028 | R4 |
| D10 | same, delivered 31 Jan 2027 | 30 Apr 2028 | R4 |
| D11 | notice 15 Nov 2025, electronic, delivered 14 Feb 2026 (= filing date) | 14 Feb 2027 | (2)(a), (6) |
| D12 | notice 15 Nov 2025, electronic, delivered 15 Feb 2026 (late) | 30 Apr 2027 | (2)(b) |
| D13 | notice 15 Aug 2025, paper, delivered 14 Nov 2025 (= filing date) | 14 Nov 2026 | (2)(a), (6), s 8(1F)(a) |
| D14 | notice 15 Aug 2025, paper, delivered 15 Nov 2025 (late) | 31 Jan 2027 | (2)(b) |
| D15 | Y 2026, notice 30 Apr 2027, electronic, delivered 29 Feb 2028 (late, filing date 31 Jan 2028) | 30 Apr 2029 | (2)(b); A2 |
| D16 | Y 2022, notice 15 Dec 2023, electronic, delivered 29 Feb 2024 (on time, filing date 14 Mar 2024) | 28 Feb 2025 | (2)(a); A1 |
| D17 | notice 20 Apr 2025, electronic, delivered 15 Jan 2026, amended 10 Mar 2026 | 30 Apr 2027 | (2)(c) anniversary 10 Mar 2027 |
| D18 | same, amended 31 Jan 2027 | 30 Apr 2028 | (2)(c), R4 |
| D19 | same, amended 20 Jan 2026 | 31 Jan 2027 | (2)(c) |
| D20 | notice 20 Apr 2025, paper, delivered 31 Oct 2025, amended 31 Jul 2026 | 31 Oct 2027 | (2)(c), R4 |

## E. s 59A — payments on account (Y 2024, preceding year 2023-24; prescribed £1,000 and 20%)

| # | Assessed (prev yr) | Deducted at source | Expected | Words |
|---|---|---|---|---|
| E1 | 5000 | 1000 | applies; 2000 each; 31 Jan 2025 and 31 Jul 2025 | (1)(a)-(d); (2) "50 per cent. of the relevant amount"; "31st January in that year", "next following 31st July" |
| E2 | 5000 | 4000 | applies (relevant 1000 = amount, 1000/5000 = 20% = proportion); 500 each | (1)(c)-(d) "not less than" |
| E3 | 4999 | 4000 | does not apply (999 < 1000) | (1)(c) |
| E4 | 10000 | 8001 | does not apply (1999/10000 < 20%) | (1)(d) |
| E5 | 10000 | 8000 | applies; 1000 each | (1)(d) at exactly 20% |
| E6 | 3000 | 3000 | does not apply | (1)(b) "exceeds" |
| E7 | 2000 | 3000 | does not apply | (1)(b) |
| E8 | 0 | 0 | does not apply | (1)(a)-(b); A6 |
| E9 | 6001 | 5000 (relevant 1001; 1001/6001 < 20%) | does not apply | (1)(d) |
| E10 | 1001 | 0 | applies; 500.50 each | (2) |
| E11 | Y 2025, 5000 / 1000 | applies; dates 31 Jan 2026, 31 Jul 2026 | (2)(a)-(b) |

## F. s 59B — balancing payment (Y 2024)

| # | Facts | Expected | Words |
|---|---|---|---|
| F1 | SA 10000, POAs 6000, deducted 1000 | 3000 payable | (1) difference |
| F2 | SA 5000, POAs 6000, deducted 0 | -1000 (repayable 1000) | (1) "payable ... or repayable" |
| F3 | SA 5000, POAs 4000, deducted 1000 | 0 | (1) |
| F4 | s 8 notice 20 Apr 2025 (no s 7 notice) | due 31 Jan 2026 | (4) "31st January next following the year of assessment" |
| F5 | s 7 notice 1 Sep 2025, s 8 notice 15 Nov 2025 | due 14 Feb 2026 | (3) "end of the period of three months beginning with the day on which the notice under section 8 ... was given" |
| F6 | s 7 notice 5 Oct 2025, s 8 notice 1 Nov 2025 | due 31 Jan 2026 | (3), A5 |
| F7 | s 7 notice 6 Oct 2025 (late), s 8 notice 15 Nov 2025 | due 31 Jan 2026 | (3)(a) fails -> (4) |
| F8 | s 7 notice 1 Sep 2025, s 8 notice 31 Oct 2025 | due 31 Jan 2026 | (3)(b) "until after the 31st October" fails -> (4) |
| F9 | s 7 notice 1 Sep 2025, s 8 notice 30 Nov 2025 | due 28 Feb 2026 | (3), R2 |
| F10 | s 7 notice 1 Sep 2025, s 8 notice 31 Dec 2025, SA 4000, POA 0, deducted 500 | 3500 due 30 Mar 2026 | (1), (3) |
| F11 | other assessment, notice 1 Mar 2026 | 31 Mar 2026 | (6) |
| F12 | notice 31 Jan 2026 | 2 Mar 2026 | (6) |
| F13 | notice 1 Feb 2028 | 2 Mar 2028 | (6), leap year |
| F14 | notice 15 Dec 2025 | 14 Jan 2026 | (6) |

## G. ss 34, 36, 36A — last day for an assessment

| # | Y / loss | Expected | Words |
|---|---|---|---|
| G1 | 2024, no careless/deliberate/offshore | 5 Apr 2029 | s 34(1) "not more than 4 years after the end of the year" |
| G2 | 2024, careless | 5 Apr 2031 | s 36(1) 6 years |
| G3 | 2024, offshore matter, not careless | 5 Apr 2037 | s 36A(2) 12 years; A7 |
| G4 | 2024, careless + offshore | 5 Apr 2037 | s 36A(2) longer than s 36(1) |
| G5 | 2024, offshore transfer | 5 Apr 2037 | s 36A(1)(b) |
| G6 | 2024, deliberate | 5 Apr 2045 | s 36(1A)(a) 20 years |
| G7 | 2024, deliberate + offshore | 5 Apr 2045 | s 36A(2) "subject to section 36(1A)" |
| G8 | 2024, s 7 failure | 5 Apr 2045 | s 36(1A)(b) |
| G9 | 2024, avoidance scheme disclosure failure | 5 Apr 2045 | s 36(1A)(c) |
| G10 | 2019, careless | 5 Apr 2026 | s 36(1) |
| G11 | 2019, none | 5 Apr 2024 | s 34(1) |

## H. End-to-end through the top-level goal (added when writing the tests; values derived from sections A-G, not from the code)

Y 2024; notice 15 Nov 2025; electronic; delivered 1 Feb 2026; no amendment; previous year 5000 assessed / 1000 deducted (prescribed 1000, 20%); SA 9000, POAs 4000, deducted 1000; s 7 notice given in time; careless loss.
Expected: notify by 5 Oct 2025; file by 14 Feb 2026 (s 8(1G)); amend by 14 Feb 2027; enquiry by 1 Feb 2027 (delivered on time, s 9A(2)(a)); POAs due, 2000 each, 31 Jan 2025 and 31 Jul 2025; balance 4000 due 14 Feb 2026 (s 59B(3)); assessment by 5 Apr 2031.
