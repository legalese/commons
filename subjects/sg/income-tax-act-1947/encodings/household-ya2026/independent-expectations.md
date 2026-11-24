# Independent expectations: Singapore household, income tax and employee CPF, YA 2026 (and YA 2027)

Written by the independent test author before any encoding file was opened.
Status: complete and saved before step 2; the checksum and time are in `independent-expectations.frozen.txt` beside this file.
Nothing in this file was changed after the encoding was read; if a number here is later found wrong, the triage in `INDEPENDENT-TEST-REPORT.md` says "my error" and this file stays as it is.

## What I used, and what I did not

Sources read, and nothing else, for what the law says:
- `BRIEF.md` of the encoding (scope and sources only).
- `ITA1947.txt`: s 39 (all of it), s 39A, s 42, s 42A, the Fifth Schedule, the Second Schedule (Table 3), "earned income" in s 2, and s 10B(12) "specified amount" (which s 39(6) uses).
- `CPFA1953.txt`: First Schedule paragraphs 1 (the 2026 table), 2, 4A, 5.
- `scratchpad/sg/cpf2025/FINDINGS.md`: the 2025 employee figures.
  Sanity check against the 2026 text: in every band of both years the factor K of the $500-$750 row is exactly 3 x R, the rate over $750 (2025: 0.6/0.51/0.345/0.225/0.15 against 20/17/11.5/7.5/5%; the 2026 text on disk prints 0.54 = 3 x 18% and 0.375 = 3 x 12.5% for the two bands that changed, and 20%, 7.5%, 5% unchanged).
  The employer totals in FINDINGS (37, 32.5, 23.5, 16.5, 12.5%) also equal the employer's own share plus the employee's share in each band, as the 2026 text does (37, 34, 25, 16.5, 12.5%).
  FINDINGS itself says the pairing for bands (a), (d), (e) was inferred.
  I also read the saved text of the 2025 schedule beside it (`cpf2025/SSO_CPFA1953_FirstSchedule_as-at-2025-01-01.txt`, the encoder's hand copy of the SSO page text): its employee cells give 20%, 17% (0.51), 11.5% (0.345), 7.5% (0.225), 5% (0.15), the same as FINDINGS, and the 2026 text confirms (a), (d), (e) are unchanged.
  The residual risk: that file is the encoder's transcription, not a copy I made, so the 2025 figures are checked for internal consistency (K = 3R, employer plus employee = total) and against the 2026 text, not against the live SSO page.

Not used: IRAS, Lexifina, PolicyEngine, any website, any `.l4` file, `NOTES.md`, tests, cases or `FINDINGS.md` in the encoding folders (I listed the folder's file names, nothing more).
Where my reading differs from what I remember of published practice, the Act's words decide and the case says so.

## Conventions

- Income year 2025 (YA 2026) unless a case says 2026 (YA 2027).
- "OW" ordinary wages for the month, "AW" additional wages, "TW" Total Wages for the month (OW + AW payable that month).
- All adults are citizens or PRs past the second anniversary month, resident, and employed by one employer (the unrelated-employer rules of para 3 are not tested).
- Tax is the sum over the adults of each adult's own tax (Singapore taxes each individual separately); the household's employee CPF is the sum of the adults'.
- **Gross income** for "net income" is wages (OW + AW) + trade income + rent, before tax and CPF. Tax-exempt income is left out of gross income; the one case that has any also prints the net with it counted (the encoding may define gross income either way; I did not find the Act deciding that, because "net income" is the brief's, not the Act's).
- **Net income** = gross income - income tax (after the parenthood rebate) - employee CPF.
- All amounts are exact: the tax is a rational number and is shown as an exact decimal (the Act has no rounding rule for tax; I searched `ITA1947.txt` for "nearest dollar" and "fraction of a dollar" and found none that governs tax).
- Facts the Act leaves to inputs and the cases state: who claims (child relief, working mother's child relief, parenthood rebate, parents), SRS and CPF top-up amounts "within the prescribed limits" (the limits are in rules, not in the Act), the life insurance premium after the 7% limit, the unabsorbed parenthood rebate brought forward from an earlier year.
  Child ages are by birth year (and birth month for adults).
  A child born on 1 January 2009 turns 16 at the very start of 2025 and so is never "below 16" in 2025; the cases give only years, so that edge is not testable here.

## The readings, each with the Act's words

CPF (First Schedule, para 1 table; paras 2, 4A, 5):
- C1. Band by Total Wages for the calendar month: "Exceeding $50 but not exceeding $500": employee NIL; "Exceeding $500 but not exceeding $750": employee pays "K of the difference between the Total Wages and $500"; "Exceeding $750": employee pays "R% of the employee's ordinary wages for the month subject to a maximum of R% of the Ordinary Wage Ceiling; and (b) R% of the Relevant Additional Wages".
  R (2025): 20, 17, 11.5, 7.5, 5%; R (2026): 20, 18, 12.5, 7.5, 5%; K = 3R.
- C2. Ordinary Wage Ceiling per month: $7,400 in 2025, $8,000 in 2026 (para 5(ea)(iii), (iv)).
- C3. Room for additional wages: "no contribution ... on any part of an employee's additional wages ... in excess of the applicable amount less the amount of ordinary wages for the current year" (para 2(1)); applicable amount $102,000 (5(da)); each month's ordinary wages over the ceiling are disregarded (4A(d)); computed "in the order in which the employee's additional wages become payable" (2(5)) and recomputed "at the end of the current year" (2(4)(c)): the whole year's ordinary wages, months after the bonus included, count.
- C4. Age: the rate for "above 55, 60, 65 or 70" is payable "from the first day of the month following the month in which the employee attains that age" (para 5(a)(i)).
- C5. "a fraction of a dollar is to be ignored" in the amount recoverable from the employee (para 5(c)): I floor each month's amount.
  FORK F1 is whether that floor is on each month's total or on its two parts.

Income tax:
- T1. Assessable income = wages + trade + rent (positive amounts only in the cases). Earned income (s 2) = employment + trade; rent is not earned income.
- T2. s 39(1): earned income relief is the lesser of the earned income and $1,000, or $6,000 where the individual "at any time in the year immediately preceding the year of assessment, was above 55 years of age but was not above 60", or $8,000 where "above 60".
  FORK F2 is what "above 55 / above 60" means (beyond the birthday, or completed years above), and a person in both (c) and (d) in one year (I take the larger).
- T3. s 39(2)(a): spouse relief $2,000 where the spouse's "income was not more than ... $8,000" (YA 2025 on).
  FORK F3: whether "income" includes tax-exempt income.
- T4. Child relief: s 39(2)(e) and Fifth Schedule para 1, $4,000: the child unmarried, and below 16 at any time in the year, or in full-time instruction, or incapacitated; para 3 and 3B(b): none for a child who "was engaged in any employment, other than under articles or indentures", or (not incapacitated) whose income "exceeded $8,000"; the proviso: $7,500 for an incapacitated child.
- T5. Working mother's child relief (Fifth Schedule para 5): a married woman, divorcee or widow, a citizen child "as at 31 December": for a child whose date is on or before 31 December 2023, 15%, 20%, 25% of her earned income for the first, second, third-and-later eligible child (5(1A), (1AA)); on or after 1 January 2024, $8,000, $10,000, $12,000 (5(1AB), (1AC)); the total is capped at 100% of her earned income (5(3)) and para 1 plus para 5 for one child at $50,000 (6(2)), para 1 first (6(3)).
  FORK F4: whether a sibling who is not eligible for relief still takes a rank.
  I rank by birth order across both regimes: the Act says "first eligible child", "second eligible child", "third eligible child or a subsequent eligible child" in both (1A) and (1AB), without separating the regimes.
- T6. Parenthood rebate (s 42A): first child $5,000 (born on or after 1 January 2008), second $10,000, third or fourth $20,000, fifth or later $20,000; allowed "for the year of assessment immediately following the year of the birth"; "against the tax payable"; the unabsorbed balance carries to the next year of assessment (42A(3)); where more than one individual is entitled, apportioned as they agree (42A(2C)).
- T7. CPF and life insurance (YA 2026 on is s 39(2)(ga), with (10A)(b)): the total "must not exceed $5,000, except that where the sum of the contributions ... exceeds $5,000, then the deduction allowed ... must be that sum"; a policy's deduction "must not exceed 7% of that capital sum".
  The CPF counted is the employee's CPF, which the First Schedule already limits to the specified amount (s 39(6) refers to the same $102,000 less ordinary wages as para 2(1); I checked s 10B(12)(e), "the difference between $102,000 and the total ordinary wages", with each month over the ceiling disregarded).
- T8. Parents (s 39(2)(i)): $9,000 living with, $5,500 not living with but $2,000 maintained, $14,000 / $10,000 if incapacitated; parent "not less than 55 years of age and whose income was not more than ... $8,000"; "no individual may obtain a deduction ... for more than 2 dependants".
  FORK F5: which two when more than two qualify.
- T9. Sibling $5,500 (j); grandparent caregiver $3,000 (p, with the grandparent's income at most $8,000); NSman (2A)/(2B) $3,000, $5,000, $1,500, $3,500, wife $750 (m); SRS (o) and CPF top-up (3), (3A) as stated amounts.
- T10. s 39A: all deductions under s 39 capped at $80,000.
- T11. Table 3 of the Second Schedule, exactly: nil to 20,000; 2% to 30,000; 3.5% to 40,000; 7% to 80,000; 11.5% to 120,000; 15% to 160,000; 18% to 200,000; 19% to 240,000; 19.5% to 280,000; 20% to 320,000; 22% to 500,000; 23% to 1,000,000; 24% above. Cumulative tax at the edges: 0, 200, 550, 3,350, 7,950, 13,950, 21,150, 28,750, 36,550, 44,550, 84,150, 199,150.
- T12. A child's or dependant's "income" for the $8,000 tests is taxable income (F3 covers the alternative).
- T13. The household can only apply a spouse's or child's reliefs to the adult who claims them; the cases say who claims.

## The forks (the Act is silent or ambiguous; the encoding must choose and say so)

- F1 (case 14): floor of the monthly CPF applies to the sum of the OW part and the AW part (A), or to each (B).
- F2 (cases 15, 21, 22, 23, 65): the meaning of "above 55 / above 60 years of age at any time in the year".
  Under A (age continuous: above N from the day after the Nth birthday) birth year 1970 gets $6,000 for 2025, birth year 1965 gets $8,000.
  Under B (above N means aged N+1 or more) they get $1,000 and $6,000.
  A person who is within both s 39(1)(c) and (d) in the year is given the larger.
  Birth years 1969 and earlier (for "above 55") and 1964 and earlier (for "above 60") are not in dispute in 2025; CPF is not affected by this fork.
- F3 (case 36): "income" in the $8,000 spouse test includes tax-exempt income (B) or not (A); the same question arises for a child and a parent, and cases 39 and 53 avoid it by giving only taxable income.
- F4 (case 47): the working mother's child relief rank counts only children eligible for child relief (A) or all citizen children (B).
- F5 (case 55): which two of three qualifying parents are claimed (A: the largest two, B: the first two listed).

Not forks, though a reader of published practice might think so: a working child (case 40: the Act's para 3 and 3B(b)(ii) deny the relief), and the ranking of the rebate by birth order.

## How the cases are marked

Each case shows the household in plain words, the working with the operative words quoted, and the answer: income tax, employee CPF, net income.
Where a fork matters the numbers for each reading follow, and the test is "either reading".
Cases 66 to 70 are not covered: the encoding must say so (the position must be NOTHING).

## Six cases worked fully by hand

Cases 6, 11, 15, 46 and 56 were worked by hand while planning, before the script existed; case 51 was worked by hand after I redesigned it, with the script's answer unseen.
All six agree with the script (checked afterwards: the tax, CPF and net printed in the answer table are the same digits).

**Case 6: OW $7,400 a month, born June 1990.**
Wages 12 x 7,400 = 88,800.
Employee CPF: TW 7,400 is over $750, so 20% of OW subject to 20% of the $7,400 ceiling: 0.20 x 7,400 = 1,480 a month, a whole number so no fraction to ignore; 12 x 1,480 = 17,760.
Deductions: earned income relief, born 1990 so none of (b)-(d): the lesser of $1,000 and 88,800 = 1,000.
CPF relief: s 39(2)(ga) with (10A)(b): CPF 17,760 exceeds $5,000, so the deduction is that sum, 17,760.
Total 18,760, under $80,000.
Chargeable 88,800 - 18,760 = 70,040.
Table 3: first 20,000 nil; next 10,000 at 2% = 200; next 10,000 at 3.5% = 350; next 40,000 (to 80,000) at 7% on the remaining 30,040 = 2,102.80.
Tax = 200 + 350 + 2,102.80 = 2,652.80.
Net = 88,800 - 2,652.80 - 17,760 = 68,387.20.

**Case 11: OW $3,000, bonuses $40,000 in March and September.**
Room = 102,000 - 12 x 3,000 = 66,000.
March: AW 40,000, all inside the room; room left 26,000.
September: AW 40,000, only 26,000 inside the room.
Monthly CPF on OW: 0.20 x 3,000 = 600; twelve months 7,200.
CPF on AW: 0.20 x 40,000 = 8,000 (March) and 0.20 x 26,000 = 5,200 (September).
Total 7,200 + 8,000 + 5,200 = 20,400.
Wages 36,000 + 80,000 = 116,000.
Deductions: relief 1,000; CPF 20,400 (over $5,000); total 21,400.
Chargeable 94,600.
Tax: 200 + 350 + 2,800 (40,000 at 7%) = 3,350 at 80,000; remaining 14,600 at 11.5% = 1,679; total 5,029.
Net = 116,000 - 5,029 - 20,400 = 90,571.

**Case 15: born June 1970, OW $3,000, bonuses $40,000 (March) and $40,000 (September).**
Para 5(a)(i): attains 55 in June 2025, so the "above 55" rate (2025: 17%) is payable from 1 July 2025.
OW: Jan-Jun 0.20 x 3,000 = 600 each = 3,600; Jul-Dec 0.17 x 3,000 = 510 each = 3,060.
Room 66,000.
March bonus: 0.20 x 40,000 = 8,000 (the March rate is 20%).
September bonus: room left 26,000, rate 17%: 0.17 x 26,000 = 4,420.
CPF = 3,600 + 3,060 + 8,000 + 4,420 = 19,080.
Wages 116,000.
Reading A of "above 55" ($6,000 relief): deductions 6,000 + 19,080 = 25,080; chargeable 90,920; tax 3,350 + (90,920 - 80,000) x 11.5% = 3,350 + 1,255.80 = 4,605.80.
Reading B ($1,000 relief): deductions 20,080; chargeable 95,920; tax 3,350 + 15,920 x 11.5% = 3,350 + 1,830.80 = 5,180.80.
Net (A) = 116,000 - 4,605.80 - 19,080 = 92,314.20; (B) = 116,000 - 5,180.80 - 19,080 = 91,739.20.

**Case 46: a widow, trade profit $400,000, one child born 2018, she claims everything.**
Earned income = trade profit 400,000 (no wages, so no employee CPF in this model).
Relief (a): 1,000.
Child relief: 4,000.
Working mother's relief, first eligible child, born on or before 31 December 2023: 15% x 400,000 = 60,000.
Para 6(2): at most 50,000 for this child over para 1 and para 5 together; para 1 first (6(3)): 50,000 - 4,000 = 46,000.
Para 5(3): 46,000 is under 100% of her earned income.
Total deductions 1,000 + 4,000 + 46,000 = 51,000, under 80,000.
Chargeable 349,000.
Tax: cumulative at 320,000 is 44,550; the next 29,000 at 22% = 6,380; total 50,930.
Net = 400,000 - 50,930 = 349,070.

**Case 51: a couple, husband OW $12,000, wife OW $6,000, children born 2022 and 2025, rebate $10,000 shared 50:50.**
Husband: wages 144,000; CPF 0.20 x 7,400 = 1,480 a month, 17,760; relief 1,000; child relief 2 x 4,000 = 8,000 (claimed by him); CPF 17,760; total 26,760; chargeable 117,240.
Tax: 3,350 at 80,000, then 37,240 x 11.5% = 4,282.60: 7,632.60.
Wife: wages 72,000; CPF 0.20 x 6,000 = 1,200 a month, 14,400; relief 1,000; working mother's relief: 2022 is the first child (15% x 72,000 = 10,800), 2025 the second (dollar regime, $10,000): 20,800; CPF 14,400; total 36,200 (not over 80,000); chargeable 35,800.
Tax: the first 20,000 is nil; the next 10,000 at 2% = 200; 35,800 is under 40,000, so the last 5,800 is at 3.5% = 203; total 403.
Rebate: the second child born 2025, YA 2026, $10,000, apportioned 50:50: 5,000 each.
Husband: 7,632.60 - 5,000 = 2,632.60.
Wife: 403 - 5,000 < 0: payable 0, and 4,597 is unabsorbed and carried forward on her side.
Household tax 2,632.60; CPF 17,760 + 14,400 = 32,160; wages 216,000; net = 216,000 - 2,632.60 - 32,160 = 181,207.40.

**Case 56: wages $2,000 a month, rent $20,000, life insurance premiums $1,000.**
Wages 24,000; assessable 44,000.
CPF 0.20 x 2,000 = 400 a month, 4,800.
CPF and insurance: 4,800 + 1,000 = 5,800 exceeds $5,000 and CPF alone does not exceed $5,000, so the deduction is $5,000 (s 39(10A)(b)).
Earned income relief: earned income is the wages 24,000 (rent excluded): 1,000.
Total 6,000; chargeable 38,000.
Tax: 200 + 8,000 x 3.5% = 280: 480.
Net = 44,000 - 480 - 4,800 = 38,720.

## The 70 cases

### Case 1. OW 500 a month: the nil band

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen, single. Ordinary wages $500 in each of the twelve months, no additional wages, no other income.

**Working** (reading used: the default one unless a fork is shown). First Schedule para 1(a), first row: "Exceeding $50 but not exceeding $500 ... Amount recoverable from the employee: NIL". Total Wages $500 is the top of the nil band. Tax: income 6,000, earned income relief min($1,000, 6,000) = 1,000, chargeable 5,000, below the $20,000 nil band.

- A: wages 6000; assessable income 6000; earned income 6000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; total 1000
  chargeable income 5000; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 0; employee CPF 0; net income 6000.**  (net income = wages + trade + rent 6000, less tax, less CPF)

### Case 2. OW 503 a month: fraction of a dollar ignored in the $500-$750 band

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $503 each month, no other income.

**Working** (reading used: the default one unless a fork is shown). Para 1(a), second row: employee pays "0.6 of the difference between the Total Wages and $500" = 0.6 x 3 = 1.8 a month; para 5(c): "in calculating the amount recoverable by the employer from the employee's wages, a fraction of a dollar is to be ignored" so $1 a month, $12 a year. (A rounding reading would give 2 and 24.)

- A: wages 6036; assessable income 6036; earned income 6036; employee CPF 12 (months: 12 x 1).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 12; total 1012
  chargeable income 5024; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 0; employee CPF 12; net income 6024.**  (net income = wages + trade + rent 6036, less tax, less CPF)

### Case 3. OW 750 a month: top of the $500-$750 band

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $750 each month.

**Working** (reading used: the default one unless a fork is shown). 0.6 x (750 - 500) = 150 a month, 1,800 a year. Both sides of the $750 edge are cases 3 and 4.

- A: wages 9000; assessable income 9000; earned income 9000; employee CPF 1800 (months: 12 x 150).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 1800; total 2800
  chargeable income 6200; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 0; employee CPF 1800; net income 7200.**  (net income = wages + trade + rent 9000, less tax, less CPF)

### Case 4. OW 751 a month: first dollar over $750

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $751 each month.

**Working** (reading used: the default one unless a fork is shown). Over $750 the employee pays "20% of the employee's ordinary wages for the month subject to a maximum of 20% of the Ordinary Wage Ceiling": 0.20 x 751 = 150.2, fraction ignored, $150 a month. No jump at the edge.

- A: wages 9012; assessable income 9012; earned income 9012; employee CPF 1800 (months: 12 x 150).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 1800; total 2800
  chargeable income 6212; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 0; employee CPF 1800; net income 7212.**  (net income = wages + trade + rent 9012, less tax, less CPF)

### Case 5. OW 3,333 a month: a 60-cent fraction every month

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $3,333 each month.

**Working** (reading used: the default one unless a fork is shown). 0.20 x 3,333 = 666.6, fraction ignored (para 5(c)): $666 a month, 7,992 a year (not 7,999.2).

- A: wages 39996; assessable income 39996; earned income 39996; employee CPF 7992 (months: 12 x 666).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 7992; total 8992
  chargeable income 31004; Table 3 tax 235.14  [10000 at 2% = 200; 1004 at 3.5% = 35.14]
  tax payable 235.14

**Answer: income tax 235.14; employee CPF 7992; net income 31768.86.**  (net income = wages + trade + rent 39996, less tax, less CPF)

### Case 6. OW 7,400 a month: the 2025 Ordinary Wage Ceiling

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $7,400 each month in 2025.

**Working** (reading used: the default one unless a fork is shown). Para 5(ea)(iii): the Ordinary Wage Ceiling is "$7,400" for each month in 2025. 20% x 7,400 = 1,480 a month, 17,760 a year. The whole employee CPF exceeds $5,000, so the CPF-and-insurance relief is the CPF itself (s 39(10A)(b): "where the sum of the contributions ... exceeds $5,000, then the deduction allowed ... must be that sum").

- A: wages 88800; assessable income 88800; earned income 88800; employee CPF 17760 (months: 12 x 1480).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 17760; total 18760
  chargeable income 70040; Table 3 tax 2652.8  [10000 at 2% = 200; 10000 at 3.5% = 350; 30040 at 7% = 2102.8]
  tax payable 2652.8

**Answer: income tax 2652.8; employee CPF 17760; net income 68387.2.**  (net income = wages + trade + rent 88800, less tax, less CPF)

### Case 7. OW 7,401 a month: one dollar over the ceiling

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $7,401 each month in 2025.

**Working** (reading used: the default one unless a fork is shown). "subject to a maximum of 20% of the Ordinary Wage Ceiling": CPF stays 1,480 a month, 17,760 a year, while the tax base grows by 12.

- A: wages 88812; assessable income 88812; earned income 88812; employee CPF 17760 (months: 12 x 1480).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 17760; total 18760
  chargeable income 70052; Table 3 tax 2653.64  [10000 at 2% = 200; 10000 at 3.5% = 350; 30052 at 7% = 2103.64]
  tax payable 2653.64

**Answer: income tax 2653.64; employee CPF 17760; net income 68398.36.**  (net income = wages + trade + rent 88812, less tax, less CPF)

### Case 8. OW 7,400 and a December bonus of exactly the room, $13,200

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $7,400 each month; additional wages (a bonus) $13,200 paid in December.

**Working** (reading used: the default one unless a fork is shown). Para 2(1): no contribution on additional wages "in excess of the applicable amount less the amount of ordinary wages for the current year"; applicable amount $102,000 (para 5(da)); ordinary wages 12 x 7,400 = 88,800; room 13,200, all of the bonus. December: Total Wages 20,600 > $750: 20% x 7,400 = 1,480 plus 20% x 13,200 = 2,640 = 4,120. Year: 11 x 1,480 + 4,120 = 20,400.

- A: wages 102000; assessable income 102000; earned income 102000; employee CPF 20400 (months: 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 4120).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 20400; total 21400
  chargeable income 80600; Table 3 tax 3419  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 600 at 11.5% = 69]
  tax payable 3419

**Answer: income tax 3419; employee CPF 20400; net income 78181.**  (net income = wages + trade + rent 102000, less tax, less CPF)

### Case 9. OW 8,000 a month and a $14,000 bonus: months over the ceiling are disregarded in the room

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $8,000 each month in 2025 (the ceiling is $7,400); additional wages $14,000 in December.

**Working** (reading used: the default one unless a fork is shown). Para 4A(d): "for the year 2024 and each subsequent year, the amount of ordinary wages for each month which is in excess of the Ordinary Wage Ceiling is to be disregarded" in computing the room: 102,000 - 12 x 7,400 = 13,200 (a reading that counts the full 96,000 would give 6,000). Contribution: 11 x 1,480 + (1,480 + 20% x 13,200) = 20,400.

- A: wages 110000; assessable income 110000; earned income 110000; employee CPF 20400 (months: 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 1480 + 4120).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 20400; total 21400
  chargeable income 88600; Table 3 tax 4339  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 8600 at 11.5% = 989]
  tax payable 4339

**Answer: income tax 4339; employee CPF 20400; net income 85261.**  (net income = wages + trade + rent 110000, less tax, less CPF)

### Case 10. OW 3,000 and a $70,000 bonus in March: the room is 66,000

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $3,000 each month; one bonus of $70,000 in March.

**Working** (reading used: the default one unless a fork is shown). Room = 102,000 - 36,000 = 66,000 (the whole year's ordinary wages count, including the months after March: para 2(4)(c) recomputes "at the end of the current year"). Employee: 12 x 600 = 7,200 on ordinary wages plus 20% x 66,000 = 13,200 on the bonus = 20,400.

- A: wages 106000; assessable income 106000; earned income 106000; employee CPF 20400 (months: 600 + 600 + 13800 + 600 + 600 + 600 + 600 + 600 + 600 + 600 + 600 + 600).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 20400; total 21400
  chargeable income 84600; Table 3 tax 3879  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 4600 at 11.5% = 529]
  tax payable 3879

**Answer: income tax 3879; employee CPF 20400; net income 81721.**  (net income = wages + trade + rent 106000, less tax, less CPF)

### Case 11. OW 3,000, two bonuses of $40,000 (March and September): the second is cut

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $3,000 each month; bonuses of $40,000 in March and $40,000 in September.

**Working** (reading used: the default one unless a fork is shown). Para 2(5): "in the order in which the employee's additional wages become payable". March: 40,000 in full; September: room left 66,000 - 40,000 = 26,000. Contribution on additional wages 20% x 66,000 = 13,200; total 7,200 + 13,200 = 20,400. Same year total as case 10 but reached by two steps.

- A: wages 116000; assessable income 116000; earned income 116000; employee CPF 20400 (months: 600 + 600 + 8600 + 600 + 600 + 600 + 600 + 600 + 5800 + 600 + 600 + 600).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 20400; total 21400
  chargeable income 94600; Table 3 tax 5029  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 14600 at 11.5% = 1679]
  tax payable 5029

**Answer: income tax 5029; employee CPF 20400; net income 90571.**  (net income = wages + trade + rent 116000, less tax, less CPF)

### Case 12. OW 700 and a $100 bonus in June: Total Wages over $750 changes the formula for that month

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $700 each month; a $100 bonus in June.

**Working** (reading used: the default one unless a fork is shown). Ordinary months: Total Wages 700 is in the $500-$750 band: 0.6 x 200 = 120. June: Total Wages 800 > 750, so "20% of the employee's ordinary wages ... and 20% of the Relevant Additional Wages" = 140 + 20 = 160. Year 11 x 120 + 160 = 1,480 (a reading that bands on ordinary wages alone would give 12 x 120 + 20 = 1,460).

- A: wages 8500; assessable income 8500; earned income 8500; employee CPF 1480 (months: 120 + 120 + 120 + 120 + 120 + 160 + 120 + 120 + 120 + 120 + 120 + 120).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 1480; total 2480
  chargeable income 6020; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 0; employee CPF 1480; net income 7020.**  (net income = wages + trade + rent 8500, less tax, less CPF)

### Case 13. An unpaid month: OW 0 and a $2,000 bonus in August

**Household (income year 2025, YA 2026).** One woman, born June 1990, citizen, single. Ordinary wages $3,000 in every month except August (nothing paid for August); in August she is paid additional wages of $2,000.

**Working** (reading used: the default one unless a fork is shown). August: Total Wages 2,000 > 750: 20% x 0 + 20% x 2,000 = 400. Other months 600. Year 11 x 600 + 400 = 7,000. Room: 102,000 - 33,000 = 69,000, not binding.

- A: wages 35000; assessable income 35000; earned income 35000; employee CPF 7000 (months: 600 + 600 + 600 + 600 + 600 + 600 + 600 + 400 + 600 + 600 + 600 + 600).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 7000; total 8000
  chargeable income 27000; Table 3 tax 140  [7000 at 2% = 140]
  tax payable 140

**Answer: income tax 140; employee CPF 7000; net income 27860.**  (net income = wages + trade + rent 35000, less tax, less CPF)

### Case 14. FORK: a fraction in both parts of one month (OW 3,333, bonus 1,003 in June)

**Household (income year 2025, YA 2026).** One man, born June 1990, citizen. Ordinary wages $3,333 each month; a $1,003 bonus in June.

**Working** (reading used: the default one unless a fork is shown). FORK. Para 5(c) ignores "a fraction of a dollar" in "calculating the amount recoverable ... from the employee's wages" and does not say whether the unit is the month's total (666.6 + 200.6 = 867.2, so 867) or each of the ordinary and additional parts (666 + 200 = 866). Other eleven months: 666 each. A: 11 x 666 + 867 = 8,193; B: 12 x 666 + 200 = 8,192. The Act is silent; both are defensible. The encoding must take one and say so.

- A: wages 40999; assessable income 40999; earned income 40999; employee CPF 8193 (months: 666 + 666 + 666 + 666 + 666 + 867 + 666 + 666 + 666 + 666 + 666 + 666).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 8193; total 9193
  chargeable income 31806; Table 3 tax 263.21  [10000 at 2% = 200; 1806 at 3.5% = 63.21]
  tax payable 263.21

**Answer: income tax 263.21; employee CPF 8193; net income 32542.79.**  (net income = wages + trade + rent 40999, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- floor the sum of the two parts of a month (reading A): tax 263.21; CPF 8193; net 32542.79.
- floor each part separately (reading B): tax 263.245; CPF 8192; net 32543.755.

### Case 15. FORK (earned income relief): turning 55 in June 2025, two bonuses straddling the band change

**Household (income year 2025, YA 2026).** One man, born June 1970 (so 55 in June 2025), citizen. Ordinary wages $3,000 each month; bonuses of $40,000 in March and $40,000 in September.

**Working** (reading used: the default one unless a fork is shown). CPF is not a fork: para 5(a) puts the "above 55" rate from "the first day of the month following the month in which the employee attains that age": January-June 20%, July-December 17% (the 2025 table). Ordinary wages: 6 x 600 + 6 x 510 = 6,660. Bonuses in payment order: March 40,000 at 20% = 8,000; September: room left 66,000 - 40,000 = 26,000 at 17% = 4,420. CPF total 19,080 (a reading that gave the later bonus the earlier rate, or let the room run out in the wrong order, differs). The earned income relief is the fork: s 39(1)(c) "at any time in the year ... above 55 years of age but not ... above 60": A gives $6,000, B gives $1,000.

- A: wages 116000; assessable income 116000; earned income 116000; employee CPF 19080 (months: 600 + 600 + 8600 + 600 + 600 + 600 + 510 + 510 + 4930 + 510 + 510 + 510).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 19080; total 25080
  chargeable income 90920; Table 3 tax 4605.8  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 10920 at 11.5% = 1255.8]
  tax payable 4605.8

**Answer: income tax 4605.8; employee CPF 19080; net income 92314.2.**  (net income = wages + trade + rent 116000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- "above 55" means beyond the 55th birthday (reading A): tax 4605.8; CPF 19080; net 92314.2.
- "above 55" means aged 56 or more (reading B): tax 5180.8; CPF 19080; net 91739.2.

### Case 16. Age band: 57 (born May 1968), OW 4,000

**Household (income year 2025, YA 2026).** One man, born May 1968 (57 in 2025), citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 1(b), "above 55 but not more than 60": employee 17% in 2025 (FINDINGS table): 680 a month, 8,160 a year. Earned income relief s 39(1)(c): $6,000 (above 55 in the whole of 2025, clearly not above 60).

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 8160 (months: 12 x 680).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 8160; total 14160
  chargeable income 33840; Table 3 tax 334.4  [10000 at 2% = 200; 3840 at 3.5% = 134.4]
  tax payable 334.4

**Answer: income tax 334.4; employee CPF 8160; net income 39505.6.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 17. Age band: 62 (born May 1963), OW 4,000

**Household (income year 2025, YA 2026).** One man, born May 1963 (62 in 2025), citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 1(c), "above 60 but not more than 65": employee 11.5% in 2025: 460 a month, 5,520 a year. Earned income relief s 39(1)(d): $8,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 5520 (months: 12 x 460).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 5520; total 13520
  chargeable income 34480; Table 3 tax 356.8  [10000 at 2% = 200; 4480 at 3.5% = 156.8]
  tax payable 356.8

**Answer: income tax 356.8; employee CPF 5520; net income 42123.2.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 18. Age band: 67 (born May 1958), OW 4,000

**Household (income year 2025, YA 2026).** One man, born May 1958 (67 in 2025), citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 1(d), "above 65 but not more than 70": employee 7.5%: 300 a month, 3,600 a year. Relief $8,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 3600 (months: 12 x 300).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 3600; total 11600
  chargeable income 36400; Table 3 tax 424  [10000 at 2% = 200; 6400 at 3.5% = 224]
  tax payable 424

**Answer: income tax 424; employee CPF 3600; net income 43976.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 19. Age band: 72 (born May 1953), OW 4,000

**Household (income year 2025, YA 2026).** One man, born May 1953 (72 in 2025), citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 1(e), "above 70": employee 5%: 200 a month, 2,400 a year. Relief $8,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 2400 (months: 12 x 200).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 2400; total 10400
  chargeable income 37600; Table 3 tax 466  [10000 at 2% = 200; 7600 at 3.5% = 266]
  tax payable 466

**Answer: income tax 466; employee CPF 2400; net income 45134.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 20. Month rule: born December 1969, so "above 55" from January 2025

**Household (income year 2025, YA 2026).** One man, born 15 December 1969, citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 5(a)(i): "from the first day of the month following the month in which the employee attains that age": he attained 55 in December 2024, so the 17% rate applies from 1 January 2025, all twelve months: 680 x 12 = 8,160. Earned income relief $6,000 (56 on 15 December 2025: above 55 on every reading).

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 8160 (months: 12 x 680).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 8160; total 14160
  chargeable income 33840; Table 3 tax 334.4  [10000 at 2% = 200; 3840 at 3.5% = 134.4]
  tax payable 334.4

**Answer: income tax 334.4; employee CPF 8160; net income 39505.6.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 21. FORK (relief only): born 15 December 1970, 55 on 15 December 2025

**Household (income year 2025, YA 2026).** One man, born 15 December 1970, citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). CPF: he attains 55 in December 2025 so the 20% rate applies to every month of 2025 (para 5(a)(i): the new rate starts in January 2026): 800 x 12 = 9,600. Earned income relief: reading A (above 55 means beyond the 55th birthday, so true from 16 December 2025) $6,000; reading B (aged 56 or more) $1,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 9600 (months: 12 x 800).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 9600; total 15600
  chargeable income 32400; Table 3 tax 284  [10000 at 2% = 200; 2400 at 3.5% = 84]
  tax payable 284

**Answer: income tax 284; employee CPF 9600; net income 38116.**  (net income = wages + trade + rent 48000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- A: beyond the 55th birthday: tax 284; CPF 9600; net 38116.
- B: aged 56 or more: tax 459; CPF 9600; net 37941.

### Case 22. FORK (relief only): 55 in May 2025, CPF band changes in June

**Household (income year 2025, YA 2026).** One man, born May 1970, citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). CPF: January-May at 20% (800), June-December at 17% (680): 5 x 800 + 7 x 680 = 8,760. Earned income relief: A $6,000, B $1,000 (see case 15).

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 8760 (months: 800 + 800 + 800 + 800 + 800 + 680 + 680 + 680 + 680 + 680 + 680 + 680).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 8760; total 14760
  chargeable income 33240; Table 3 tax 313.4  [10000 at 2% = 200; 3240 at 3.5% = 113.4]
  tax payable 313.4

**Answer: income tax 313.4; employee CPF 8760; net income 38926.6.**  (net income = wages + trade + rent 48000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- A: beyond the 55th birthday: tax 313.4; CPF 8760; net 38926.6.
- B: aged 56 or more: tax 488.4; CPF 8760; net 38751.6.

### Case 23. FORK (relief only): 60 in May 2025, CPF band changes in June

**Household (income year 2025, YA 2026).** One man, born May 1965, citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). CPF: January-May at 17% (680), June-December at 11.5% (460): 5 x 680 + 7 x 460 = 6,620. Earned income relief: in 2025 he is above 55 but not above 60 until May, and above 60 after (reading A): both s 39(1)(c) and (d) apply at some time in the year; taking the larger, $8,000. Reading B (above 60 means aged 61 or more): only (c), $6,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 6620 (months: 680 + 680 + 680 + 680 + 680 + 460 + 460 + 460 + 460 + 460 + 460 + 460).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 6620; total 14620
  chargeable income 33380; Table 3 tax 318.3  [10000 at 2% = 200; 3380 at 3.5% = 118.3]
  tax payable 318.3

**Answer: income tax 318.3; employee CPF 6620; net income 41061.7.**  (net income = wages + trade + rent 48000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- A: beyond the 60th birthday: tax 318.3; CPF 6620; net 41061.7.
- B: aged 61 or more: tax 388.3; CPF 6620; net 40991.7.

### Case 24. Crossing 65: born June 1960, CPF band changes in July

**Household (income year 2025, YA 2026).** One man, born June 1960, citizen. Ordinary wages $4,000 each month.

**Working** (reading used: the default one unless a fork is shown). Para 5(a)(i): 65 attained in June 2025, so January-June are "above 60 but not more than 65" (11.5%: 460) and July-December "above 65" (7.5%: 300): 6 x 460 + 6 x 300 = 4,560. Relief $8,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 4560 (months: 460 + 460 + 460 + 460 + 460 + 460 + 300 + 300 + 300 + 300 + 300 + 300).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 4560; total 12560
  chargeable income 35440; Table 3 tax 390.4  [10000 at 2% = 200; 5440 at 3.5% = 190.4]
  tax payable 390.4

**Answer: income tax 390.4; employee CPF 4560; net income 43049.6.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 25. Two employees, K factors in the $500-$750 band at 57 and at 67

**Household (income year 2025, YA 2026).** A married couple. The husband, born May 1968 (57), earns $700 a month; the wife, born May 1958 (67), earns $700 a month. Both citizens, no other income.

**Working** (reading used: the default one unless a fork is shown). Total Wages 700 is in the second row. Husband (para 1(b)): the employee pays "0.51 of the difference between the Total Wages and $500" (2025) = 0.51 x 200 = 102. Wife (para 1(d)): 0.225 x 200 = 45. Year: 12 x 147 = 1,764. Each has income of 8,400, which is more than $8,000, so neither gets spouse relief.

- H: wages 8400; assessable income 8400; earned income 8400; employee CPF 1224 (months: 12 x 102).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 1224; total 7224
  chargeable income 1176; Table 3 tax 0  []
  tax payable 0
- W: wages 8400; assessable income 8400; earned income 8400; employee CPF 540 (months: 12 x 45).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 540; total 8540
  chargeable income 0; Table 3 tax 0
  tax payable 0

**Answer: income tax 0; employee CPF 1764; net income 15036.**  (net income = wages + trade + rent 16800, less tax, less CPF)

### Case 26. Table 3 edges: chargeable income 20,000 and 30,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $20,000, the second $30,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Edge 1: the first $20,000 is nil, so 20,000 -> 0; the next $10,000 at 2%: 30,000 -> 200.

- P: wages 0; rent 20000; assessable income 20000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 20000; Table 3 tax 0  []
  tax payable 0
- Q: wages 0; rent 30000; assessable income 30000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 30000; Table 3 tax 200  [10000 at 2% = 200]
  tax payable 200

**Answer: income tax 200; employee CPF 0; net income 49800.**  (net income = wages + trade + rent 50000, less tax, less CPF)

### Case 27. Table 3 edges: chargeable income 40,000 and 80,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $40,000, the second $80,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Next $10,000 at 3.5%: 40,000 -> 550. Next $40,000 at 7%: 80,000 -> 3,350.

- P: wages 0; rent 40000; assessable income 40000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 40000; Table 3 tax 550  [10000 at 2% = 200; 10000 at 3.5% = 350]
  tax payable 550
- Q: wages 0; rent 80000; assessable income 80000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 80000; Table 3 tax 3350  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800]
  tax payable 3350

**Answer: income tax 3900; employee CPF 0; net income 116100.**  (net income = wages + trade + rent 120000, less tax, less CPF)

### Case 28. Table 3 edges: chargeable income 120,000 and 160,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $120,000, the second $160,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Next $40,000 at 11.5%: 120,000 -> 7,950. Next $40,000 at 15%: 160,000 -> 13,950.

- P: wages 0; rent 120000; assessable income 120000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 120000; Table 3 tax 7950  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600]
  tax payable 7950
- Q: wages 0; rent 160000; assessable income 160000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 160000; Table 3 tax 13950  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000]
  tax payable 13950

**Answer: income tax 21900; employee CPF 0; net income 258100.**  (net income = wages + trade + rent 280000, less tax, less CPF)

### Case 29. Table 3 edges: chargeable income 200,000 and 240,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $200,000, the second $240,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Next $40,000 at 18%: 200,000 -> 21,150. Next $40,000 at 19%: 240,000 -> 28,750.

- P: wages 0; rent 200000; assessable income 200000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 200000; Table 3 tax 21150  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200]
  tax payable 21150
- Q: wages 0; rent 240000; assessable income 240000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 240000; Table 3 tax 28750  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600]
  tax payable 28750

**Answer: income tax 49900; employee CPF 0; net income 390100.**  (net income = wages + trade + rent 440000, less tax, less CPF)

### Case 30. Table 3 edges: chargeable income 280,000 and 320,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $280,000, the second $320,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Next $40,000 at 19.5%: 280,000 -> 36,550. Next $40,000 at 20%: 320,000 -> 44,550.

- P: wages 0; rent 280000; assessable income 280000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 280000; Table 3 tax 36550  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800]
  tax payable 36550
- Q: wages 0; rent 320000; assessable income 320000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 320000; Table 3 tax 44550  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800; 40000 at 20% = 8000]
  tax payable 44550

**Answer: income tax 81100; employee CPF 0; net income 518900.**  (net income = wages + trade + rent 600000, less tax, less CPF)

### Case 31. Table 3 edges: chargeable income 500,000 and 1,000,000

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $500,000, the second $1,000,000; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. Next $180,000 at 22%: 500,000 -> 84,150. Next $500,000 at 23%: 1,000,000 -> 199,150.

- P: wages 0; rent 500000; assessable income 500000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 500000; Table 3 tax 84150  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800; 40000 at 20% = 8000; 180000 at 22% = 39600]
  tax payable 84150
- Q: wages 0; rent 1000000; assessable income 1000000; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 1000000; Table 3 tax 199150  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800; 40000 at 20% = 8000; 180000 at 22% = 39600; 500000 at 23% = 115000]
  tax payable 199150

**Answer: income tax 283300; employee CPF 0; net income 1216700.**  (net income = wages + trade + rent 1500000, less tax, less CPF)

### Case 32. Table 3 edges: chargeable income 20,001 and 1,000,001

**Household (income year 2025, YA 2026).** Two adults living together who are not married to each other. The first has rent income of $20,001, the second $1,000,001; neither has other income or any relief.

**Working** (reading used: the default one unless a fork is shown). Rent is not "earned income" (s 2: only employment, trade, profession, vocation and pensions), so s 39(1) gives nothing and chargeable income equals the rent. Tax from Second Schedule Table 3. One dollar into a band: 20,001 -> 0.02 (2% of one dollar); 1,000,001 -> 199,150.24 ("every dollar exceeding $1,000,000" at 24%).

- P: wages 0; rent 20001; assessable income 20001; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 20001; Table 3 tax 0.02  [1 at 2% = 0.02]
  tax payable 0.02
- Q: wages 0; rent 1000001; assessable income 1000001; earned income 0; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 0; total 0
  chargeable income 1000001; Table 3 tax 199150.24  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800; 40000 at 20% = 8000; 180000 at 22% = 39600; 500000 at 23% = 115000; 1 at 24% = 0.24]
  tax payable 199150.24

**Answer: income tax 199150.26; employee CPF 0; net income 820851.74.**  (net income = wages + trade + rent 1020002, less tax, less CPF)

### Case 33. Earned income smaller than $1,000: trade income 800, rent 50,000

**Household (income year 2025, YA 2026).** One man, born 1980, citizen, single. A small trade with profit (after its own deductions) of $800; rent (after its deductions) of $50,000; no wages.

**Working** (reading used: the default one unless a fork is shown). s 39(1)(a): "the sum of $1,000 or the amount of the earned income ... whichever is less": earned income is the trade profit 800 only (rent is not earned income), so the relief is 800, not 1,000. Chargeable 50,800 - 800 = 50,000: tax 200 + 350 + 10,000 x 7% = 1,250 (a relief of 1,000 would give 1,236).

- A: wages 0; trade 800; rent 50000; assessable income 50800; earned income 800; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 800; total 800
  chargeable income 50000; Table 3 tax 1250  [10000 at 2% = 200; 10000 at 3.5% = 350; 10000 at 7% = 700]
  tax payable 1250

**Answer: income tax 1250; employee CPF 0; net income 49550.**  (net income = wages + trade + rent 50800, less tax, less CPF)

### Case 34. Spouse with income exactly $8,000

**Household (income year 2025, YA 2026).** A married couple living together. The husband earns $5,000 a month (born 1985). The wife, born 1985, runs a small trade with profit (after expenses) of exactly $8,000 for the year and has no other income. No children.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(a): a spouse "whose income was not more than ... $8,000 in that year (where the year of assessment is 2025 or any subsequent year of assessment)": 8,000 qualifies, the husband gets $2,000. Wife: earned income 8,000, relief 1,000, chargeable 7,000, no tax. (The wife's income is 8,000 < the husband's, so the husband's income of 60,000 gives her no spouse relief.)

- H: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; spouse s39(2)(a) 2000; CPF+life ins s39(2)(ga),(10A)(b) 12000; total 15000
  chargeable income 45000; Table 3 tax 900  [10000 at 2% = 200; 10000 at 3.5% = 350; 5000 at 7% = 350]
  tax payable 900
- W: wages 0; trade 8000; assessable income 8000; earned income 8000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; total 1000
  chargeable income 7000; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 900; employee CPF 12000; net income 55100.**  (net income = wages + trade + rent 68000, less tax, less CPF)

### Case 35. Spouse with income $8,001

**Household (income year 2025, YA 2026).** The same couple, but the wife's trade profit is $8,001.

**Working** (reading used: the default one unless a fork is shown). 8,001 is "more than $8,000": no spouse relief; the husband's chargeable income is 2,000 higher than in case 34.

- H: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 12000; total 13000
  chargeable income 47000; Table 3 tax 1040  [10000 at 2% = 200; 10000 at 3.5% = 350; 7000 at 7% = 490]
  tax payable 1040
- W: wages 0; trade 8001; assessable income 8001; earned income 8001; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; total 1000
  chargeable income 7001; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 1040; employee CPF 12000; net income 54961.**  (net income = wages + trade + rent 68001, less tax, less CPF)

### Case 36. FORK: the wife has $5,000 of taxable income and $3,001 of tax-exempt income

**Household (income year 2025, YA 2026).** The same couple. The wife has trade profit of $5,000 and receives $3,001 of tax-exempt income (say interest on a bank deposit). No children.

**Working** (reading used: the default one unless a fork is shown). FORK. s 39(2)(a) says "whose income was not more than $8,000" and the Act does not define "income" for this purpose; s 13 exempts the interest from tax but does not say it ceases to be income. Reading A: husband gets 2,000. Reading B: he does not. The brief names this fork. Net income below is shown with the exempt income left out of the household's gross income; the encoding may define gross income differently (see the net_incl_exempt column).

- H: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; spouse s39(2)(a) 2000; CPF+life ins s39(2)(ga),(10A)(b) 12000; total 15000
  chargeable income 45000; Table 3 tax 900  [10000 at 2% = 200; 10000 at 3.5% = 350; 5000 at 7% = 350]
  tax payable 900
- W: wages 0; trade 5000; tax-exempt 3001 (not assessable); assessable income 5000; earned income 5000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; total 1000
  chargeable income 4000; Table 3 tax 0  []
  tax payable 0

**Answer: income tax 900; employee CPF 12000; net income 52100.**  (net income = wages + trade + rent 65000, less tax, less CPF; with the tax-exempt income 3001 counted as income: 55101)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- "income" means taxable income, so 5,000 qualifies (reading A): tax 900; CPF 12000; net 52100; net with the exempt income counted 55101.
- "income" includes tax-exempt income, so 8,001 does not (reading B): tax 1040; CPF 12000; net 51960; net with the exempt income counted 54961.

### Case 37. Children born 2010 and 2009: 15 and 16 in 2025

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Two unmarried citizen children: one born 2010 (15 in 2025) and one born 2009 (16 in 2025), both at school. No other income.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(e)(i): child "below 16 years of age at any time during the year preceding the year of assessment". The child born 2010 is 15 throughout 2025; the child born 2009 turns 16 during 2025 and was below 16 before that. Both qualify: Fifth Schedule para 1, $4,000 each = 8,000. (A child born 1 January 2009 turns 16 at the start of 2025 and would not qualify under (i); the cases give birth years only.) Father: wages 72,000; CPF 1,200 x 12 = 14,400; EIR 1,000.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 8000; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 23400
  chargeable income 48600; Table 3 tax 1152  [10000 at 2% = 200; 10000 at 3.5% = 350; 8600 at 7% = 602]
  tax payable 1152

**Answer: income tax 1152; employee CPF 14400; net income 56448.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 38. Two children born 2008 (17 in 2025): one at university, one not studying

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Two unmarried citizen children, both born 2008 (17 in 2025): one is a full-time university student, the other has left school, is not in work and has no income.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(e): 17 is not "below 16", so only (ii) "receiving full-time instruction at any university, college, school or other educational institution" can qualify: the student gets $4,000, the other child nothing. Total 4,000.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 19400
  chargeable income 52600; Table 3 tax 1432  [10000 at 2% = 200; 10000 at 3.5% = 350; 12600 at 7% = 882]
  tax payable 1432

**Answer: income tax 1432; employee CPF 14400; net income 56168.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 39. Child income exactly $8,000 and $8,001

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Two unmarried citizen children born 2018. One has income of exactly $8,000 for 2025 (rent from a property held for him, no employment); the other $8,001 (same kind of income).

**Working** (reading used: the default one unless a fork is shown). Fifth Schedule para 3B(b)(i): no deduction for a child "(a) who is not incapacitated ... and (b) ... his or her income ... for the year immediately preceding the year of assessment exceeded $8,000". 8,000 does not exceed; 8,001 does. Total 4,000.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 19400
  chargeable income 52600; Table 3 tax 1432  [10000 at 2% = 200; 10000 at 3.5% = 350; 12600 at 7% = 882]
  tax payable 1432

**Answer: income tax 1432; employee CPF 14400; net income 56168.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 40. A child who works (earns $5,000 part-time), age 17 in instruction

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. One unmarried citizen child born 2008 (17), in full-time instruction, who earned $5,000 from part-time employment in 2025.

**Working** (reading used: the default one unless a fork is shown). Fifth Schedule para 3: "No deduction is allowed in respect of any child who was engaged in any employment, other than under articles or indentures ... during the year immediately preceding the year of assessment", repeated in para 3B(b)(ii). The Act's words give nothing although the income is under $8,000. (Published practice, which this file does not use as a source, may allow it; the Act as printed does not.)

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 15400
  chargeable income 56600; Table 3 tax 1712  [10000 at 2% = 200; 10000 at 3.5% = 350; 16600 at 7% = 1162]
  tax payable 1712

**Answer: income tax 1712; employee CPF 14400; net income 55888.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 41. Incapacitated children: aged 10 and an adult aged 30

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Two unmarried citizen children, both incapacitated by physical or mental infirmity: one born 2015, one born 1995 (30 in 2025, no income).

**Working** (reading used: the default one unless a fork is shown). s 39(2)(e)(iv) qualifies an incapacitated child at any age; the proviso (v) raises the Fifth Schedule para 1 deduction to $7,500 "for the year of assessment 2015 or a subsequent year of assessment", and (vi) gives $7,500 where no Fifth Schedule deduction is allowable. 2 x 7,500 = 15,000.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 15000; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 30400
  chargeable income 41600; Table 3 tax 662  [10000 at 2% = 200; 10000 at 3.5% = 350; 1600 at 7% = 112]
  tax payable 662

**Answer: income tax 662; employee CPF 14400; net income 56938.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 42. WMCR, child born 2023 (percentage regime), mother earns 60,000

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen; ordinary wages $5,000 a month. One citizen child born 2023; she maintains the child and claims all child reliefs.

**Working** (reading used: the default one unless a fork is shown). Fifth Schedule para 5(1A) and (1AA): date of birth "on or before 31 December 2023", first eligible child: 15% of her earned income. Earned income = 60,000 (employment; CPF is not deducted): 9,000. Plus para 1: 4,000. EIR 1,000; CPF 12,000.

- A: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; WMCR Fifth Sch para 5 9000; CPF+life ins s39(2)(ga),(10A)(b) 12000; total 26000
  chargeable income 34000; Table 3 tax 340  [10000 at 2% = 200; 4000 at 3.5% = 140]
  tax payable 340

**Answer: income tax 340; employee CPF 12000; net income 47660.**  (net income = wages + trade + rent 60000, less tax, less CPF)

### Case 43. WMCR, child born 2024 (dollar regime)

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen; ordinary wages $5,000 a month. One citizen child born 2024.

**Working** (reading used: the default one unless a fork is shown). Para 5(1AB), (1AC): date "on or after 1 January 2024": "if Y is the eligible child $8,000". Plus 4,000. Compare case 42: the dollar regime gives 8,000 against 9,000.

- A: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; WMCR Fifth Sch para 5 8000; CPF+life ins s39(2)(ga),(10A)(b) 12000; total 25000
  chargeable income 35000; Table 3 tax 375  [10000 at 2% = 200; 5000 at 3.5% = 175]
  tax payable 375

**Answer: income tax 375; employee CPF 12000; net income 47625.**  (net income = wages + trade + rent 60000, less tax, less CPF)

### Case 44. WMCR, three children across both regimes (2018, 2021, 2024), earning 84,000, plus rent

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen; ordinary wages $7,000 a month; rent of $100,000. Three citizen children born 2018, 2021 and 2024; she claims all child reliefs.

**Working** (reading used: the default one unless a fork is shown). Ranks by birth order across both regimes (the Act ranks "first eligible child", "second ... ", "third ... or a subsequent eligible child" without separating the regimes; para 7(b) leaves ranking to the Comptroller). Earned income is the wages, 84,000, and not the rent (s 2 "earned income"). 2018: first, 15% x 84,000 = 12,600. 2021: second, 20% = 16,800. 2024: third, $12,000. Total 41,400, plus child relief 12,000, EIR 1,000, CPF 16,800: 71,200 (under $80,000). Assessable income 184,000.

- A: wages 84000; rent 100000; assessable income 184000; earned income 84000; employee CPF 16800 (months: 12 x 1400).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 12000; WMCR Fifth Sch para 5 41400; CPF+life ins s39(2)(ga),(10A)(b) 16800; total 71200
  chargeable income 112800; Table 3 tax 7122  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 32800 at 11.5% = 3772]
  tax payable 7122

**Answer: income tax 7122; employee CPF 16800; net income 160078.**  (net income = wages + trade + rent 184000, less tax, less CPF)

### Case 45. WMCR capped at 100% of earned income

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen, living on a small trade (profit $15,000 after its own deductions) and rent of $40,000. Three citizen children born 2018, 2020 and 2024; she claims all child reliefs.

**Working** (reading used: the default one unless a fork is shown). Para 5(3): "The total deductions allowable ... under sub-paragraphs (1A) and (1AB) must not exceed 100% of her earned income". Earned income is the trade profit, 15,000 (rent is not earned income). 15% x 15,000 = 2,250; 20% = 3,000; third (dollar regime) 12,000: 17,250, cut to 15,000. QCR 12,000, EIR 1,000: chargeable 55,000 - 28,000 = 27,000; tax 7,000 x 2% = 140.

- A: wages 0; trade 15000; rent 40000; assessable income 55000; earned income 15000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 12000; WMCR Fifth Sch para 5 15000; total 28000
  chargeable income 27000; Table 3 tax 140  [7000 at 2% = 140]
  tax payable 140

**Answer: income tax 140; employee CPF 0; net income 54860.**  (net income = wages + trade + rent 55000, less tax, less CPF)

### Case 46. WMCR capped at $50,000 per child

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen, with trade profit of $400,000. One citizen child born 2018; she claims all child reliefs.

**Working** (reading used: the default one unless a fork is shown). 15% x 400,000 = 60,000, but para 6(2): "The total deductions allowable to all individuals under paragraphs 1 and 5(1A) or (1AB) ... in respect of the same child must not exceed $50,000", and para 6(3) puts para 1 first: 50,000 - 4,000 = 46,000. Total deductions: EIR 1,000 + 4,000 + 46,000 = 51,000; chargeable 349,000.

- A: wages 0; trade 400000; assessable income 400000; earned income 400000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; WMCR Fifth Sch para 5 46000; total 51000
  chargeable income 349000; Table 3 tax 50930  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 40000 at 19% = 7600; 40000 at 19.5% = 7800; 40000 at 20% = 8000; 29000 at 22% = 6380]
  tax payable 50930

**Answer: income tax 50930; employee CPF 0; net income 349070.**  (net income = wages + trade + rent 400000, less tax, less CPF)

### Case 47. FORK: WMCR rank when an older child no longer qualifies for child relief

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen, with trade profit of $100,000. Two citizen children: a son born 2000 (25, working, so not eligible for child relief) and a daughter born 2020; she claims what she can.

**Working** (reading used: the default one unless a fork is shown). FORK. "first eligible child" (para 5(1A)(c)) turns on who is an "eligible child"; para 1 speaks of "eligible children" for the QCR, para 1B counts a stillborn sibling "as if the stillborn child were an eligible child", and para 7(b) leaves ranking to the Comptroller. The Act does not say whether a sibling who no longer qualifies still occupies a rank. A: 15,000; B: 20,000.

- A: wages 0; trade 100000; assessable income 100000; earned income 100000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; WMCR Fifth Sch para 5 15000; total 20000
  chargeable income 80000; Table 3 tax 3350  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800]
  tax payable 3350

**Answer: income tax 3350; employee CPF 0; net income 96650.**  (net income = wages + trade + rent 100000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- rank among children eligible for relief: the daughter is the first eligible child, 15% (reading A): tax 3350; CPF 0; net 96650.
- rank among all citizen children: the daughter is the second, 20% (reading B): tax 3000; CPF 0; net 97000.

### Case 48. The $80,000 cap bites by one dollar

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen, with trade profit of $200,000, SRS contributions of $1,001, two citizen children born 2018 and 2021; she claims all child reliefs.

**Working** (reading used: the default one unless a fork is shown). WMCR: 15% x 200,000 = 30,000 and 20% = 40,000 (each under the per-child 46,000), 70,000 in all. Child relief 8,000, EIR 1,000, SRS 1,001: 80,001. s 39A: "the total amount of all deductions allowable ... under section 39 must not exceed $80,000": 80,000. Chargeable 120,000, tax 7,950 (an uncapped 119,999 would give 7,949.885).

- A: wages 0; trade 200000; assessable income 200000; earned income 200000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 8000; WMCR Fifth Sch para 5 70000; SRS s39(2)(o) 1001; total 80001 -> s 39A cap 80000
  chargeable income 120000; Table 3 tax 7950  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600]
  tax payable 7950

**Answer: income tax 7950; employee CPF 0; net income 192050.**  (net income = wages + trade + rent 200000, less tax, less CPF)

### Case 49. PTR, first child born 2025: absorbed by the tax

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $10,000 a month. His first child, a citizen, was born in 2025. He claims the rebate and the child relief.

**Working** (reading used: the default one unless a fork is shown). s 42A(2A): first child born on or after 1 January 2008: "for the year of assessment immediately following the year of the birth" (YA 2026) "a rebate of $5,000 against the tax payable". Chargeable: 120,000 - 1,000 - 17,760 (CPF, 1,480 a month: ceiling) - 4,000 = 97,240; tax 3,350 + 17,240 x 11.5% = 5,332.6; rebate 5,000 -> tax payable 332.6, nothing carried forward.

- A: wages 120000; assessable income 120000; earned income 120000; employee CPF 17760 (months: 12 x 1480).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; CPF+life ins s39(2)(ga),(10A)(b) 17760; total 22760
  chargeable income 97240; Table 3 tax 5332.6  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 17240 at 11.5% = 1982.6]
  parenthood rebate this year 5000 + brought forward 0: applied 5000, unabsorbed 0 -> tax payable 332.6

**Answer: income tax 332.6; employee CPF 17760; net income 101907.4.**  (net income = wages + trade + rent 120000, less tax, less CPF)

### Case 50. PTR, third child born 2025: $20,000 against a large tax

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen, with a trade profit of $250,000 and no wages. Three citizen children, born 2019, 2022 and 2025; he claims the child relief and the rebate.

**Working** (reading used: the default one unless a fork is shown). s 42A(2)(a): "a third or fourth child of the family born to him or her on or after 1 January 2004 ... a rebate of $20,000 against the tax payable" for YA 2026. EIR 1,000; child relief 3 x 4,000 = 12,000 (a baby of 2025 is "below 16"); chargeable 237,000; tax 21,150 + 37,000 x 19% = 28,180; payable 28,180 - 20,000 = 8,180.

- A: wages 0; trade 250000; assessable income 250000; earned income 250000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 12000; total 13000
  chargeable income 237000; Table 3 tax 28180  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 40000 at 11.5% = 4600; 40000 at 15% = 6000; 40000 at 18% = 7200; 37000 at 19% = 7030]
  parenthood rebate this year 20000 + brought forward 0: applied 20000, unabsorbed 0 -> tax payable 8180

**Answer: income tax 8180; employee CPF 0; net income 241820.**  (net income = wages + trade + rent 250000, less tax, less CPF)

### Case 51. PTR, second child born 2025: $10,000 shared 50:50 by two parents whose taxes differ

**Household (income year 2025, YA 2026).** A married couple, both citizens, both born 1985. The husband earns $12,000 a month; the wife earns $6,000 a month. Two citizen children: born 2022 and 2025. The husband claims the child relief for both children; the wife claims the working mother's relief; the parenthood rebate for the 2025 birth is divided equally between them.

**Working** (reading used: the default one unless a fork is shown). s 42A(1)(a) "a second child ... rebate of $10,000", divided under s 42A(2C) "in such proportion as they may agree" (here 50:50, an input), so 5,000 each. The unabsorbed part of one spouse's share stays with that spouse (s 42A(3): "against the tax payable by the individual"); it does not reduce the other's tax. Wife: earned income 72,000; WMCR 2022 child first 15% = 10,800; 2025 child second, dollar regime $10,000; 20,800; so her tax is small and her share of the rebate is mostly unabsorbed. Husband: 144,000, CPF 17,760 (ceiling), child relief 8,000. Compare an all-to-husband allocation (not this case): husband 0, wife pays her whole tax.

- H: wages 144000; assessable income 144000; earned income 144000; employee CPF 17760 (months: 12 x 1480).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 8000; CPF+life ins s39(2)(ga),(10A)(b) 17760; total 26760
  chargeable income 117240; Table 3 tax 7632.6  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 37240 at 11.5% = 4282.6]
  parenthood rebate this year 5000 + brought forward 0: applied 5000, unabsorbed 0 -> tax payable 2632.6
- W: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; WMCR Fifth Sch para 5 20800; CPF+life ins s39(2)(ga),(10A)(b) 14400; total 36200
  chargeable income 35800; Table 3 tax 403  [10000 at 2% = 200; 5800 at 3.5% = 203]
  parenthood rebate this year 5000 + brought forward 0: applied 403, unabsorbed 4597 -> tax payable 0

**Answer: income tax 2632.6; employee CPF 32160; net income 181207.4.**  (net income = wages + trade + rent 216000, less tax, less CPF)

Unabsorbed parenthood rebate carried forward: 4597.

### Case 52. PTR carry-forward into income year 2026 (YA 2027)

**Household (income year 2026, YA 2027).** A widower, born 1985, citizen; ordinary wages $8,000 a month in 2026. A citizen child was born in 2025; the household brings forward $4,240 of unabsorbed parenthood rebate (an input, for instance what is left of a $5,000 rebate against a tax of $760).

**Working** (reading used: the default one unless a fork is shown). YA 2027: the rebate for the 2025 birth was allowed for YA 2026 (s 42A(1)-(2B)); only the balance carries forward (s 42A(3)). 2026 ceiling $8,000 (para 5(ea)(iv)): CPF 20% x 8,000 = 1,600 a month, 19,200. Wages 96,000. Chargeable 96,000 - 1,000 - 19,200 - 4,000 = 71,800; tax 550 + 31,800 x 7% = 2,776; rebate applied 2,776, tax payable 0, balance carried 4,240 - 2,776 = 1,464.

- A: wages 96000; assessable income 96000; earned income 96000; employee CPF 19200 (months: 12 x 1600).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; CPF+life ins s39(2)(ga),(10A)(b) 19200; total 24200
  chargeable income 71800; Table 3 tax 2776  [10000 at 2% = 200; 10000 at 3.5% = 350; 31800 at 7% = 2226]
  parenthood rebate this year 0 + brought forward 4240: applied 2776, unabsorbed 1464 -> tax payable 0

**Answer: income tax 0; employee CPF 19200; net income 76800.**  (net income = wages + trade + rent 96000, less tax, less CPF)

Unabsorbed parenthood rebate carried forward: 1464.

### Case 53. Parent relief: income $8,000 / $8,001 and the age floor, living with the claimant

**Household (income year 2025, YA 2026).** A widower, born 1995, citizen; ordinary wages $6,000 a month. Three parents live with him in Singapore: his father, born 1955 (70), with income of exactly $8,000; his mother-in-law, born 1955 (70), with income of $8,001; and his stepmother, born 1971 (54), with no income. He claims all that qualify.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(i)(iv)(A): a dependant parent "not less than 55 years of age and whose income was not more than ... $8,000 in that year ... living with him or her in the same household": $9,000. 8,000 qualifies; 8,001 does not; 54 is under 55. Only the first dependant counts: 9,000.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 14400; parents s39(2)(i) 9000; total 24400
  chargeable income 47600; Table 3 tax 1082  [10000 at 2% = 200; 10000 at 3.5% = 350; 7600 at 7% = 532]
  tax payable 1082

**Answer: income tax 1082; employee CPF 14400; net income 56518.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 54. Parent relief: not living with the claimant, maintenance $2,000 / $1,999, and an incapacitated parent

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Three parents/grandparents living in Singapore: one aged 70 with no income living elsewhere, to whom he gave $2,000 in the year; one aged 70 with no income living elsewhere, to whom he gave $1,999; and one incapacitated parent living with him.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(i)(iv)(B): "$5,500, where the dependant was not living with him or her ... a sum of not less than $2,000 ... was incurred"; $1,999 is not enough. (v)(A): incapacitated, living with: $14,000. Proviso (vi): "no individual may obtain a deduction ... for more than 2 dependants": the two deductions are 14,000 and 5,500: 19,500.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 14400; parents s39(2)(i) 19500; total 34900
  chargeable income 37100; Table 3 tax 448.5  [10000 at 2% = 200; 7100 at 3.5% = 248.5]
  tax payable 448.5

**Answer: income tax 448.5; employee CPF 14400; net income 57151.5.**  (net income = wages + trade + rent 72000, less tax, less CPF)

### Case 55. FORK: three qualifying parents, only two can be claimed

**Household (income year 2025, YA 2026).** A widower, born 1985, citizen; ordinary wages $6,000 a month. Three parents, listed in this order: one living elsewhere (maintenance $3,000; $5,500), one aged 70 living with him ($9,000), one incapacitated living with him ($14,000).

**Working** (reading used: the default one unless a fork is shown). FORK. Proviso (vi): "no individual may obtain a deduction under this paragraph for more than 2 dependants". The Act does not say which two. A is the claimant's own choice; B is a mechanical choice. A claimant is entitled to elect, so A is the better reading, but the Act is silent.

- A: wages 72000; assessable income 72000; earned income 72000; employee CPF 14400 (months: 12 x 1200).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 14400; parents s39(2)(i) 23000; total 38400
  chargeable income 33600; Table 3 tax 326  [10000 at 2% = 200; 3600 at 3.5% = 126]
  tax payable 326

**Answer: income tax 326; employee CPF 14400; net income 57274.**  (net income = wages + trade + rent 72000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- the claimant takes the two largest: 14,000 + 9,000 = 23,000 (reading A): tax 326; CPF 14400; net 57274.
- the first two listed: 5,500 + 9,000 = 14,500 (reading B): tax 697; CPF 14400; net 56903.

### Case 56. CPF 4,800 and life insurance premiums 1,000: the $5,000 cap

**Household (income year 2025, YA 2026).** One man, born 1985, citizen; ordinary wages $2,000 a month; rent $20,000. He pays $1,000 of life insurance premiums (allowable amount, on a Singapore insurer), none of it from SRS.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(ga), (10A)(b): "the total deductions allowable under subsection (2)(ga) must not exceed $5,000, except that where the sum of the contributions ... exceeds $5,000, then the deduction allowed ... must be that sum". CPF 400 x 12 = 4,800; 4,800 + 1,000 = 5,800 > 5,000, so 5,000.

- A: wages 24000; rent 20000; assessable income 44000; earned income 24000; employee CPF 4800 (months: 12 x 400).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 5000; total 6000
  chargeable income 38000; Table 3 tax 480  [10000 at 2% = 200; 8000 at 3.5% = 280]
  tax payable 480

**Answer: income tax 480; employee CPF 4800; net income 38720.**  (net income = wages + trade + rent 44000, less tax, less CPF)

### Case 57. CPF 5,280 and premiums 1,000: the CPF alone exceeds $5,000

**Household (income year 2025, YA 2026).** One man, born 1985, citizen; ordinary wages $2,200 a month; rent $20,000; life insurance premiums of $1,000.

**Working** (reading used: the default one unless a fork is shown). CPF 440 x 12 = 5,280 > 5,000: the deduction "must be that sum", 5,280; the premiums add nothing.

- A: wages 26400; rent 20000; assessable income 46400; earned income 26400; employee CPF 5280 (months: 12 x 440).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 5280; total 6280
  chargeable income 40120; Table 3 tax 558.4  [10000 at 2% = 200; 10000 at 3.5% = 350; 120 at 7% = 8.4]
  tax payable 558.4

**Answer: income tax 558.4; employee CPF 5280; net income 40561.6.**  (net income = wages + trade + rent 46400, less tax, less CPF)

### Case 58. Premiums of 6,000 and no CPF: capped at $5,000

**Household (income year 2025, YA 2026).** One man, born 1985, citizen, running a trade with profit of $50,000; no wages; life insurance premiums of $6,000 (allowable amount).

**Working** (reading used: the default one unless a fork is shown). Trade income carries no employee CPF here (the self-employed's CPF is outside the brief). Premiums alone: capped at $5,000 by (10A)(b). EIR 1,000. Chargeable 44,000.

- A: wages 0; trade 50000; assessable income 50000; earned income 50000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 5000; total 6000
  chargeable income 44000; Table 3 tax 830  [10000 at 2% = 200; 10000 at 3.5% = 350; 4000 at 7% = 280]
  tax payable 830

**Answer: income tax 830; employee CPF 0; net income 49170.**  (net income = wages + trade + rent 50000, less tax, less CPF)

### Case 59. Life insurance: the 7% of capital sum limit

**Household (income year 2025, YA 2026).** One man, born 1985, citizen, running a trade with profit of $50,000; he pays life insurance premiums of $6,000 on a policy that secures a capital sum on death of $60,000, with no bonus or other benefit.

**Working** (reading used: the default one unless a fork is shown). s 39(10A)(a)(i): "the amount to be deducted in respect of any policy securing a capital sum on death ... must not exceed 7% of that capital sum": 7% x 60,000 = 4,200, so the premium allowed is 4,200 (modelled with premium input 4,200). If the encoding takes the capital sum and the premium separately, the fact is: premium 6,000, capital sum 60,000, allowed 4,200. EIR 1,000; chargeable 44,800.

- A: wages 0; trade 50000; assessable income 50000; earned income 50000; employee CPF 0 (months: 12 x 0).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 4200; total 5200
  chargeable income 44800; Table 3 tax 886  [10000 at 2% = 200; 10000 at 3.5% = 350; 4800 at 7% = 336]
  tax payable 886

**Answer: income tax 886; employee CPF 0; net income 49114.**  (net income = wages + trade + rent 50000, less tax, less CPF)

### Case 60. NSman (key appointment) and his wife

**Household (income year 2025, YA 2026).** A married couple, both citizens, both born 1990. The husband earns $5,000 a month and is an operationally ready national serviceman who performed operationally ready service in the relevant period and is a key command and staff appointment holder (certified); the wife earns $3,000 a month. No children.

**Working** (reading used: the default one unless a fork is shown). s 39(2A)(d): "a deduction of $5,000 if the individual is a NS key command and staff appointment holder"; s 39(2)(m): wife of an operationally ready NSman who is a citizen: $750 (the husband is entitled under (2A)). Husband CPF 1,000 x 12 = 12,000; wife 600 x 12 = 7,200. Neither has income of 8,000 or less: no spouse relief.

- H: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 12000; NSman s39(2A)/(2B)/(2)(m) 5000; total 18000
  chargeable income 42000; Table 3 tax 690  [10000 at 2% = 200; 10000 at 3.5% = 350; 2000 at 7% = 140]
  tax payable 690
- W: wages 36000; assessable income 36000; earned income 36000; employee CPF 7200 (months: 12 x 600).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 7200; NSman s39(2A)/(2B)/(2)(m) 750; total 8950
  chargeable income 27050; Table 3 tax 141  [7050 at 2% = 141]
  tax payable 141

**Answer: income tax 831; employee CPF 19200; net income 75969.**  (net income = wages + trade + rent 96000, less tax, less CPF)

### Case 61. A widow with an incapacitated brother and her mother as a caregiver grandparent

**Household (income year 2025, YA 2026).** A widow, born 1985, citizen; ordinary wages $5,000 a month. One citizen child born 2020 (5). Her incapacitated brother lives with her. Her mother (born 1955, income $8,000 from a part-time job) lives in Singapore and looks after the child. She claims all she can.

**Working** (reading used: the default one unless a fork is shown). s 39(2)(j): incapacitated sibling living with the individual: $5,500. s 39(2)(p): "a married woman, widow or divorcee whose parent ... was looking after any of her children who is a citizen of Singapore and was 12 years of age and below ... did not derive income that exceeds an aggregate of $8,000": $3,000 "in respect of one such parent or grandparent only". Child relief 4,000, WMCR 15% x 60,000 = 9,000. EIR 1,000; CPF 12,000.

- A: wages 60000; assessable income 60000; earned income 60000; employee CPF 12000 (months: 12 x 1000).
  deductions: EIR s39(1)(a) 1000; QCR s39(2)(e), Fifth Sch para 1 4000; WMCR Fifth Sch para 5 9000; CPF+life ins s39(2)(ga),(10A)(b) 12000; sibling s39(2)(j) 5500; grandparent caregiver s39(2)(p) 3000; total 34500
  chargeable income 25500; Table 3 tax 110  [5500 at 2% = 110]
  tax payable 110

**Answer: income tax 110; employee CPF 12000; net income 47890.**  (net income = wages + trade + rent 60000, less tax, less CPF)

### Case 62. SRS and CPF top-up for the member's own account

**Household (income year 2025, YA 2026).** One man, born 1985, citizen; ordinary wages $9,000 a month. He contributed $15,300 to his SRS account and made a cash top-up of $8,000 to his own CPF Special Account (both within the limits set under the rules).

**Working** (reading used: the default one unless a fork is shown). s 39(2)(o): SRS contributions up to the cap set by regulations (the amount given is the allowed amount, an input). s 39(3A): the lower of the top-up amount subject to the prescribed maximum relief amount and the deduction limit (inputs, not in the Act). CPF 1,480 x 12 = 17,760 (ceiling); EIR 1,000; total deductions 17,760 + 1,000 + 15,300 + 8,000 = 42,060; chargeable 65,940.

- A: wages 108000; assessable income 108000; earned income 108000; employee CPF 17760 (months: 12 x 1480).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 17760; SRS s39(2)(o) 15300; CPF top-up s39(3)/(3A) 8000; total 42060
  chargeable income 65940; Table 3 tax 2365.8  [10000 at 2% = 200; 10000 at 3.5% = 350; 25940 at 7% = 1815.8]
  tax payable 2365.8

**Answer: income tax 2365.8; employee CPF 17760; net income 87874.2.**  (net income = wages + trade + rent 108000, less tax, less CPF)

### Case 63. 2026: OW 8,001, bonus 10,000 in December (ceiling 8,000, room 6,000)

**Household (income year 2026, YA 2027).** One man, born June 1990, citizen. In 2026 his ordinary wages are $8,001 each month and he is paid a $10,000 bonus in December.

**Working** (reading used: the default one unless a fork is shown). Para 5(ea)(iv): ceiling $8,000 from 2026. Room 102,000 - 12 x 8,000 = 6,000: bonus contribution 20% x 6,000 = 1,200; ordinary 1,600 x 12 = 19,200: total 20,400. (Using 2025's ceiling would give 17,760 + room 13,200.)

- A: wages 106012; assessable income 106012; earned income 106012; employee CPF 20400 (months: 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 1600 + 2800).
  deductions: EIR s39(1)(a) 1000; CPF+life ins s39(2)(ga),(10A)(b) 20400; total 21400
  chargeable income 84612; Table 3 tax 3880.38  [10000 at 2% = 200; 10000 at 3.5% = 350; 40000 at 7% = 2800; 4612 at 11.5% = 530.38]
  tax payable 3880.38

**Answer: income tax 3880.38; employee CPF 20400; net income 81731.62.**  (net income = wages + trade + rent 106012, less tax, less CPF)

### Case 64. 2026: born May 1970: 55-60 rate is 18% (2026 table), relief $6,000

**Household (income year 2026, YA 2027).** One man, born May 1970 (56 in 2026), citizen. Ordinary wages $4,000 a month in 2026.

**Working** (reading used: the default one unless a fork is shown). Para 1(b) as in force from 1 January 2026: "above 55 but not more than 60": employee 18% (the 2025 table gave 17%): 720 x 12 = 8,640. Earned income relief $6,000 on every reading (aged 56 in 2026).

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 8640 (months: 12 x 720).
  deductions: EIR s39(1)(c) 6000; CPF+life ins s39(2)(ga),(10A)(b) 8640; total 14640
  chargeable income 33360; Table 3 tax 317.6  [10000 at 2% = 200; 3360 at 3.5% = 117.6]
  tax payable 317.6

**Answer: income tax 317.6; employee CPF 8640; net income 39042.4.**  (net income = wages + trade + rent 48000, less tax, less CPF)

### Case 65. FORK (relief only), 2026: 60 in June 2026, CPF band changes in July

**Household (income year 2026, YA 2027).** One man, born June 1966, citizen. Ordinary wages $4,000 a month in 2026.

**Working** (reading used: the default one unless a fork is shown). CPF 2026 table: January-June 18% (720), July-December "above 60 but not more than 65" 12.5% (500): 6 x 720 + 6 x 500 = 7,320. Relief A $8,000, B $6,000.

- A: wages 48000; assessable income 48000; earned income 48000; employee CPF 7320 (months: 720 + 720 + 720 + 720 + 720 + 720 + 500 + 500 + 500 + 500 + 500 + 500).
  deductions: EIR s39(1)(d) 8000; CPF+life ins s39(2)(ga),(10A)(b) 7320; total 15320
  chargeable income 32680; Table 3 tax 293.8  [10000 at 2% = 200; 2680 at 3.5% = 93.8]
  tax payable 293.8

**Answer: income tax 293.8; employee CPF 7320; net income 40386.2.**  (net income = wages + trade + rent 48000, less tax, less CPF)

**FORK.** The Act does not settle this case; the encoding must take one reading, say which, and the readings give:
- beyond the 60th birthday (A): tax 293.8; CPF 7320; net 40386.2.
- aged 61 or more (B): tax 363.8; CPF 7320; net 40316.2.

### Case 66. Not covered: a non-resident adult

**Household (income year 2025, YA 2026).** A man who was not resident in Singapore in the year of assessment; he is employed in Singapore and earns $5,000 a month.

**Expected answer: NOT COVERED** (the household position must be NOTHING). BRIEF "Not covered: a non-resident adult". s 42(1) excludes "a person not resident in Singapore" from the Part A rates; ss 40A-40C and 43 apply other rates. The position must be NOTHING.

### Case 67. Not covered: a permanent resident in the first two years

**Household (income year 2025, YA 2026).** A permanent resident, who became one 18 months before the end of 2025; ordinary wages $5,000 a month.

**Expected answer: NOT COVERED** (the household position must be NOTHING). BRIEF: "a permanent resident in the first two years". The graduated rates of paras 1A-1H apply until the second anniversary month; the position must be NOTHING.

### Case 68. Not covered: income year 2024

**Household (income year 2025, YA 2026).** A citizen man, born 1990, with ordinary wages $5,000 a month in 2024.

**Expected answer: NOT COVERED** (the household position must be NOTHING). BRIEF: "any income year but 2025 and 2026". NOTHING.

### Case 69. Not covered: income year 2027

**Household (income year 2025, YA 2026).** A citizen man, born 1990, with ordinary wages $5,000 a month in 2027.

**Expected answer: NOT COVERED** (the household position must be NOTHING). BRIEF: "any income year but 2025 and 2026". NOTHING.

### Case 70. Not covered: a taxable pension counted as earned income

**Household (income year 2025, YA 2026).** A citizen woman, born 1960, with a taxable pension of $30,000 in 2025 and no other income.

**Expected answer: NOT COVERED** (the household position must be NOTHING). BRIEF: "taxable pensions in earned income". "earned income" in s 2 includes "any pension on which tax is payable under section 10(1)(e)"; the position must be NOTHING.


## Answer table (output of `python3 -I generate.py`, exact arithmetic with fractions)

The net column leaves tax-exempt income out of gross income (case 36 shows both).

| # | case | tax | CPF | net | fork readings (tax|CPF|net) |
|---|---|---|---|---|---|
| 1 | OW 500 a month: the nil band | 0 | 0 | 6000 |  |
| 2 | OW 503 a month: fraction of a dollar ignored in the $500-$750 band | 0 | 12 | 6024 |  |
| 3 | OW 750 a month: top of the $500-$750 band | 0 | 1800 | 7200 |  |
| 4 | OW 751 a month: first dollar over $750 | 0 | 1800 | 7212 |  |
| 5 | OW 3,333 a month: a 60-cent fraction every month | 235.14 | 7992 | 31768.86 |  |
| 6 | OW 7,400 a month: the 2025 Ordinary Wage Ceiling | 2652.8 | 17760 | 68387.2 |  |
| 7 | OW 7,401 a month: one dollar over the ceiling | 2653.64 | 17760 | 68398.36 |  |
| 8 | OW 7,400 and a December bonus of exactly the room, $13,200 | 3419 | 20400 | 78181 |  |
| 9 | OW 8,000 a month and a $14,000 bonus: months over the ceiling are disregarded in the room | 4339 | 20400 | 85261 |  |
| 10 | OW 3,000 and a $70,000 bonus in March: the room is 66,000 | 3879 | 20400 | 81721 |  |
| 11 | OW 3,000, two bonuses of $40,000 (March and September): the second is cut | 5029 | 20400 | 90571 |  |
| 12 | OW 700 and a $100 bonus in June: Total Wages over $750 changes the formula for that month | 0 | 1480 | 7020 |  |
| 13 | An unpaid month: OW 0 and a $2,000 bonus in August | 140 | 7000 | 27860 |  |
| 14 | FORK: a fraction in both parts of one month (OW 3,333, bonus 1,003 in June) (FORK) | 263.21 | 8193 | 32542.79 | 263.21|8193|32542.79 / 263.245|8192|32543.755 |
| 15 | FORK (earned income relief): turning 55 in June 2025, two bonuses straddling the band change (FORK) | 4605.8 | 19080 | 92314.2 | 4605.8|19080|92314.2 / 5180.8|19080|91739.2 |
| 16 | Age band: 57 (born May 1968), OW 4,000 | 334.4 | 8160 | 39505.6 |  |
| 17 | Age band: 62 (born May 1963), OW 4,000 | 356.8 | 5520 | 42123.2 |  |
| 18 | Age band: 67 (born May 1958), OW 4,000 | 424 | 3600 | 43976 |  |
| 19 | Age band: 72 (born May 1953), OW 4,000 | 466 | 2400 | 45134 |  |
| 20 | Month rule: born December 1969, so "above 55" from January 2025 | 334.4 | 8160 | 39505.6 |  |
| 21 | FORK (relief only): born 15 December 1970, 55 on 15 December 2025 (FORK) | 284 | 9600 | 38116 | 284|9600|38116 / 459|9600|37941 |
| 22 | FORK (relief only): 55 in May 2025, CPF band changes in June (FORK) | 313.4 | 8760 | 38926.6 | 313.4|8760|38926.6 / 488.4|8760|38751.6 |
| 23 | FORK (relief only): 60 in May 2025, CPF band changes in June (FORK) | 318.3 | 6620 | 41061.7 | 318.3|6620|41061.7 / 388.3|6620|40991.7 |
| 24 | Crossing 65: born June 1960, CPF band changes in July | 390.4 | 4560 | 43049.6 |  |
| 25 | Two employees, K factors in the $500-$750 band at 57 and at 67 | 0 | 1764 | 15036 |  |
| 26 | Table 3 edges: chargeable income 20,000 and 30,000 | 200 | 0 | 49800 |  |
| 27 | Table 3 edges: chargeable income 40,000 and 80,000 | 3900 | 0 | 116100 |  |
| 28 | Table 3 edges: chargeable income 120,000 and 160,000 | 21900 | 0 | 258100 |  |
| 29 | Table 3 edges: chargeable income 200,000 and 240,000 | 49900 | 0 | 390100 |  |
| 30 | Table 3 edges: chargeable income 280,000 and 320,000 | 81100 | 0 | 518900 |  |
| 31 | Table 3 edges: chargeable income 500,000 and 1,000,000 | 283300 | 0 | 1216700 |  |
| 32 | Table 3 edges: chargeable income 20,001 and 1,000,001 | 199150.26 | 0 | 820851.74 |  |
| 33 | Earned income smaller than $1,000: trade income 800, rent 50,000 | 1250 | 0 | 49550 |  |
| 34 | Spouse with income exactly $8,000 | 900 | 12000 | 55100 |  |
| 35 | Spouse with income $8,001 | 1040 | 12000 | 54961 |  |
| 36 | FORK: the wife has $5,000 of taxable income and $3,001 of tax-exempt income (FORK) | 900 | 12000 | 52100 | 900|12000|52100 / 1040|12000|51960 |
| 37 | Children born 2010 and 2009: 15 and 16 in 2025 | 1152 | 14400 | 56448 |  |
| 38 | Two children born 2008 (17 in 2025): one at university, one not studying | 1432 | 14400 | 56168 |  |
| 39 | Child income exactly $8,000 and $8,001 | 1432 | 14400 | 56168 |  |
| 40 | A child who works (earns $5,000 part-time), age 17 in instruction | 1712 | 14400 | 55888 |  |
| 41 | Incapacitated children: aged 10 and an adult aged 30 | 662 | 14400 | 56938 |  |
| 42 | WMCR, child born 2023 (percentage regime), mother earns 60,000 | 340 | 12000 | 47660 |  |
| 43 | WMCR, child born 2024 (dollar regime) | 375 | 12000 | 47625 |  |
| 44 | WMCR, three children across both regimes (2018, 2021, 2024), earning 84,000, plus rent | 7122 | 16800 | 160078 |  |
| 45 | WMCR capped at 100% of earned income | 140 | 0 | 54860 |  |
| 46 | WMCR capped at $50,000 per child | 50930 | 0 | 349070 |  |
| 47 | FORK: WMCR rank when an older child no longer qualifies for child relief (FORK) | 3350 | 0 | 96650 | 3350|0|96650 / 3000|0|97000 |
| 48 | The $80,000 cap bites by one dollar | 7950 | 0 | 192050 |  |
| 49 | PTR, first child born 2025: absorbed by the tax | 332.6 | 17760 | 101907.4 |  |
| 50 | PTR, third child born 2025: $20,000 against a large tax | 8180 | 0 | 241820 |  |
| 51 | PTR, second child born 2025: $10,000 shared 50:50 by two parents whose taxes differ | 2632.6 | 32160 | 181207.4 |  |
| 52 | PTR carry-forward into income year 2026 (YA 2027) | 0 | 19200 | 76800 |  |
| 53 | Parent relief: income $8,000 / $8,001 and the age floor, living with the claimant | 1082 | 14400 | 56518 |  |
| 54 | Parent relief: not living with the claimant, maintenance $2,000 / $1,999, and an incapacitated parent | 448.5 | 14400 | 57151.5 |  |
| 55 | FORK: three qualifying parents, only two can be claimed (FORK) | 326 | 14400 | 57274 | 326|14400|57274 / 697|14400|56903 |
| 56 | CPF 4,800 and life insurance premiums 1,000: the $5,000 cap | 480 | 4800 | 38720 |  |
| 57 | CPF 5,280 and premiums 1,000: the CPF alone exceeds $5,000 | 558.4 | 5280 | 40561.6 |  |
| 58 | Premiums of 6,000 and no CPF: capped at $5,000 | 830 | 0 | 49170 |  |
| 59 | Life insurance: the 7% of capital sum limit | 886 | 0 | 49114 |  |
| 60 | NSman (key appointment) and his wife | 831 | 19200 | 75969 |  |
| 61 | A widow with an incapacitated brother and her mother as a caregiver grandparent | 110 | 12000 | 47890 |  |
| 62 | SRS and CPF top-up for the member's own account | 2365.8 | 17760 | 87874.2 |  |
| 63 | 2026: OW 8,001, bonus 10,000 in December (ceiling 8,000, room 6,000) | 3880.38 | 20400 | 81731.62 |  |
| 64 | 2026: born May 1970: 55-60 rate is 18% (2026 table), relief $6,000 | 317.6 | 8640 | 39042.4 |  |
| 65 | FORK (relief only), 2026: 60 in June 2026, CPF band changes in July (FORK) | 293.8 | 7320 | 40386.2 | 293.8|7320|40386.2 / 363.8|7320|40316.2 |
| 66 | Not covered: a non-resident adult | NOT COVERED |  |  |  |
| 67 | Not covered: a permanent resident in the first two years | NOT COVERED |  |  |  |
| 68 | Not covered: income year 2024 | NOT COVERED |  |  |  |
| 69 | Not covered: income year 2027 | NOT COVERED |  |  |  |
| 70 | Not covered: a taxable pension counted as earned income | NOT COVERED |  |  |  |

## The script

The three files are in the same folder as this file: `model.py` (the Act as arithmetic, listed below), `cases.py` (the facts of each case), `generate.py` (runs them, writes this table and `results.json`).
Run with `python3 -I generate.py` from that folder.

```python
#!/usr/bin/env python3
# Independent model of the Singapore household (income tax + employee CPF), worked ONLY from
#   ITA1947.txt (s 39, 39A, 42, 42A, Fifth Schedule, Second Schedule Table 3, s 2 "earned income", s 10B(12))
#   CPFA1953.txt (First Schedule paras 1, 2, 4A, 5) and the 2025 table transcribed in cpf2025/FINDINGS.md.
# Exact arithmetic (fractions); no floating point.
from fractions import Fraction as F
from math import floor

# ---------------------------------------------------------------- Second Schedule, Table 3 (YA 2024 on)
TABLE3 = [(20000, F(0)), (10000, F(2, 100)), (10000, F(35, 1000)), (40000, F(7, 100)),
          (40000, F(115, 1000)), (40000, F(15, 100)), (40000, F(18, 100)), (40000, F(19, 100)),
          (40000, F(195, 1000)), (40000, F(20, 100)), (180000, F(22, 100)), (500000, F(23, 100)),
          (None, F(24, 100))]

def table3(ci):
    rem, tax = F(ci), F(0)
    for width, rate in TABLE3:
        if width is None:
            tax += rem * rate
            break
        take = min(rem, F(width))
        tax += take * rate
        rem -= take
        if rem <= 0:
            break
    return tax

# ---------------------------------------------------------------- CPF First Schedule, employee's share
# para 1 (a)-(e): rate R over $750, K in the $500-$750 band.  2026: text on disk; 2025: FINDINGS.md (K = 3R checked)
CPF = {
    2025: dict(owc=7400, R=[F(20, 100), F(17, 100), F(115, 1000), F(75, 1000), F(5, 100)],
               K=[F(6, 10), F(51, 100), F(345, 1000), F(225, 1000), F(15, 100)]),
    2026: dict(owc=8000, R=[F(20, 100), F(18, 100), F(125, 1000), F(75, 1000), F(5, 100)],
               K=[F(6, 10), F(54, 100), F(375, 1000), F(225, 1000), F(15, 100)]),
}
APPLICABLE = 102000   # para 5(da)

def band_index(year, month, born):
    """para 5(a): the rate for 'above 55/60/65/70' is payable from the first day of the month following
    the month in which the employee attains that age."""
    by, bm = born
    idx = 0
    for t in (55, 60, 65, 70):
        if year * 12 + month > (by + t) * 12 + bm:
            idx += 1
    return idx

def cpf_year(year, born, ow, aw, floor_mode='sum'):
    """returns (total employee CPF, list of monthly amounts)"""
    p = CPF[year]
    owc = p['owc']
    cap = APPLICABLE - sum(min(o, owc) for o in ow)          # para 2(1) with para 4A(d)
    remaining = cap
    months = []
    for m in range(1, 13):
        o, a = ow[m - 1], aw[m - 1]
        tw = o + a
        b = band_index(year, m, born)
        raw = min(a, max(0, remaining)) if a else 0
        remaining -= a
        if tw <= 500:                       # "Exceeding $50 but not exceeding $500": NIL; nothing at or under $50
            amt = 0
        elif tw <= 750:                     # 0.6 (etc.) of the difference between Total Wages and $500
            amt = floor(p['K'][b] * (tw - 500))
        else:
            ow_part = p['R'][b] * min(o, owc)
            aw_part = p['R'][b] * raw
            amt = floor(ow_part + aw_part) if floor_mode == 'sum' else floor(ow_part) + floor(aw_part)
        months.append(amt)
    return sum(months), months

# ---------------------------------------------------------------- earned income relief s 39(1)
def eir_amount(year, born, ei, reading='cont'):
    by = born[0]
    # ages at some time in the year (year immediately preceding the YA = income year)
    if reading == 'cont':       # above N = strictly more than N years, continuous
        above55 = by <= year - 55
        above60 = by <= year - 60
        c = (year - 60 <= by <= year - 55)           # above 55 but not above 60 at some time
    else:                       # 'whole': above N = completed years > N
        above55 = by <= year - 56
        above60 = by <= year - 61
        c = (year - 61 <= by <= year - 56)
    d = above60
    cands = []
    if d:
        cands.append(8000)
    if c:
        cands.append(6000)
    if not cands:
        cands.append(1000)
    return min(max(cands), ei), (8000 if d else 6000 if c else 1000), ('d' if d else 'c' if c else 'a'), (c and d)

# ---------------------------------------------------------------- the household
def adult(name='A', sex='M', born=(1990, 6), ow=0, aw=None, trade=0, rent=0, exempt=0, srs=0, topup=0,
          premium=0, ns=None, married=True, wife_of_ns=False, parents=None, siblings=0, caregiver=0, other=0):
    ow = [ow] * 12 if isinstance(ow, int) else list(ow)
    awl = [0] * 12
    for m, v in (aw or {}).items():
        awl[m - 1] = v
    return dict(name=name, sex=sex, born=born, ow=ow, aw=awl, trade=trade, rent=rent, exempt=exempt, srs=srs,
                topup=topup, premium=premium, ns=ns, married=married, wife_of_ns=wife_of_ns,
                parents=parents or [], siblings=siblings, caregiver=caregiver, other=other)

def child(born, citizen=True, instruction=False, income=0, exempt_income=0, employed=False, incap=False, ordinal=None):
    return dict(born=born, citizen=citizen, instruction=instruction, income=income, exempt_income=exempt_income,
                employed=employed, incap=incap, ordinal=ordinal)

def dep(born, income=0, exempt=0, living=True, maint=0, incap=False, claimant=0):
    return dict(born=born, income=income, exempt=exempt, living=living, maint=maint, incap=incap, claimant=claimant)

DEFAULT_READINGS = dict(eir='cont', cpf_floor='sum', income_test='taxable', wmcr_rank='eligible',
                        dep_pick='best', dep_age='end')

def qcr_for_child(c, year, rd):
    """s 39(2)(e) + Fifth Schedule paras 1, 3, 3B and proviso (v)/(vi)"""
    qual = (c['born'] >= year - 16) or c['instruction'] or c['incap']
    if not qual:
        return 0
    if c['incap']:
        return 7500
    if c['employed']:
        return 0                              # para 3 and para 3B(b)(ii)
    inc = c['income'] + (c['exempt_income'] if rd['income_test'] == 'incl_exempt' else 0)
    if inc > 8000:
        return 0
    return 4000

def run(case, rd_over=None):
    rd = dict(DEFAULT_READINGS)
    rd.update(case.get('readings', {}))
    if rd_over:
        rd.update(rd_over)
    year = case['year']
    A = case['adults']
    kids = case.get('children', [])
    claims = case.get('claims', {})           # qcr: list of adult-share lists per child; wmcr by mother; ptr_share
    res = {'adults': []}
    # first pass: wages, CPF, incomes
    for a in A:
        cpf, months = cpf_year(year, a['born'], a['ow'], a['aw'], rd['cpf_floor'])
        wages = sum(a['ow']) + sum(a['aw'])
        a['_cpf'], a['_months'], a['_wages'] = cpf, months, wages
        a['_assess'] = wages + a['trade'] + a['rent']
        a['_ei'] = wages + a['trade']
        a['_tinc'] = a['_assess']                     # income for the $8,000 tests (taxable)
        a['_tinc_ex'] = a['_assess'] + a['exempt']    # including tax-exempt income
    # children
    qcr_child = [qcr_for_child(c, year, rd) for c in kids]
    # QCR claim shares per child (default: all to adult 0)
    shares = claims.get('qcr', [[1] + [0] * (len(A) - 1)] * len(kids))
    # WMCR rank
    cit = [i for i, c in enumerate(kids) if c['citizen']]
    order = sorted(range(len(kids)), key=lambda i: (kids[i]['born'], i))
    if rd['wmcr_rank'] == 'eligible':
        ranked = [i for i in order if qcr_child[i] > 0 and kids[i]['citizen']]
    else:
        ranked = [i for i in order if kids[i]['citizen']]
    rank_of = {i: r + 1 for r, i in enumerate(ranked)}
    out_adults = []
    total_net_income = F(0)
    household_tax = F(0)
    household_cpf = 0
    carry_total = F(0)
    for ai, a in enumerate(A):
        steps = []
        ded = {}
        # earned income relief
        eir, cap, para, overlap = eir_amount(year, a['born'], a['_ei'], rd['eir'])
        ded['EIR s39(1)(%s)' % para] = eir
        # spouse relief s 39(2)(a)
        if len(A) == 2:
            o = A[1 - ai]
            oinc = o['_tinc_ex'] if rd['income_test'] == 'incl_exempt' else o['_tinc']
            if case.get('spouses', True) and oinc <= 8000:
                ded['spouse s39(2)(a)'] = 2000
        # QCR
        q = F(0)
        for ci, c in enumerate(kids):
            q += qcr_child[ci] * F(shares[ci][ai])
        if q:
            ded['QCR s39(2)(e), Fifth Sch para 1'] = q
        # WMCR (married woman / divorcee / widow only)
        if a['sex'] == 'F' and a['married']:
            w = F(0)
            for ci in ranked:
                if ci not in rank_of or qcr_child[ci] == 0:
                    continue
                r = min(rank_of[ci], 3)
                c = kids[ci]
                if c['born'] <= 2023:
                    amt = F([15, 20, 25][r - 1], 100) * a['_ei']
                else:
                    amt = F([8000, 10000, 12000][r - 1])
                amt = min(amt, F(50000) - qcr_child[ci])      # Fifth Sch para 6(2),(3)
                w += amt
            w = min(w, F(a['_ei']))                          # para 5(3)
            if w:
                ded['WMCR Fifth Sch para 5'] = w
        # life insurance + CPF  s 39(2)(ga), (10A)(b)
        C, P = a['_cpf'], a['premium']
        li = F(C) if C > 5000 else min(F(C + P), F(5000))
        if li:
            ded['CPF+life ins s39(2)(ga),(10A)(b)'] = li
        # parents s 39(2)(i)
        pv = []
        for d in a['parents']:
            dinc = d['income'] + (d['exempt'] if rd['income_test'] == 'incl_exempt' else 0)
            if d['incap']:
                v = 14000 if d['living'] else (10000 if d['maint'] >= 2000 else 0)
            else:
                agecond = (d['born'] <= year - 55) if rd['dep_age'] == 'end' else (d['born'] <= year - 56)
                if agecond and dinc <= 8000:
                    v = 9000 if d['living'] else (5500 if d['maint'] >= 2000 else 0)
                else:
                    v = 0
            pv.append(v)
        if pv:
            if rd['dep_pick'] == 'best':
                pv_used = sorted(pv, reverse=True)[:2]
            else:
                pv_used = [v for v in pv if v > 0][:2]
            if sum(pv_used):
                ded['parents s39(2)(i)'] = sum(pv_used)
        if a['siblings']:
            ded['sibling s39(2)(j)'] = 5500 * a['siblings']
        if a['caregiver']:
            ded['grandparent caregiver s39(2)(p)'] = a['caregiver']
        if a['ns']:
            ded['NSman s39(2A)/(2B)/(2)(m)'] = a['ns']
        if a['srs']:
            ded['SRS s39(2)(o)'] = a['srs']
        if a['topup']:
            ded['CPF top-up s39(3)/(3A)'] = a['topup']
        if a['other']:
            ded['other'] = a['other']
        total = sum(ded.values())
        capped = min(total, F(80000))                         # s 39A
        chargeable = max(F(0), F(a['_assess']) - capped)
        gross_tax = table3(chargeable)
        # PTR s 42A: child born in income year (YA = year + 1), by ordinal
        ptr = F(0)
        for ci, c in enumerate(kids):
            if c['born'] == year and c['citizen']:
                ordl = c['ordinal']
                amt = {1: 5000, 2: 10000}.get(ordl, 20000)
                ptr += amt * F(claims.get('ptr', [1] + [0] * (len(A) - 1))[ai])
        bf = F(claims.get('bf', [0] * len(A))[ai])
        avail = ptr + bf
        applied = min(gross_tax, avail)
        net_tax = gross_tax - applied
        carry = avail - applied
        income_total = a['_wages'] + a['trade'] + a['rent']
        out_adults.append(dict(name=a['name'], wages=a['_wages'], trade=a['trade'], rent=a['rent'], exempt=a['exempt'],
                               assess=a['_assess'], ei=a['_ei'], cpf=a['_cpf'], months=a['_months'], ded=ded,
                               total_ded=total, capped=capped, chargeable=chargeable, gross_tax=gross_tax,
                               ptr=ptr, bf=bf, applied=applied, tax=net_tax, carry=carry, cap_eir=cap, overlap=overlap))
        household_tax += net_tax
        household_cpf += a['_cpf']
        carry_total += carry
        total_net_income += income_total - net_tax - a['_cpf']
    res['adults'] = out_adults
    res['tax'] = household_tax
    res['cpf'] = household_cpf
    res['carry'] = carry_total
    gross = sum(x['wages'] + x['trade'] + x['rent'] for x in out_adults)
    res['gross'] = gross
    res['exempt'] = sum(x['exempt'] for x in out_adults)
    res['net'] = total_net_income
    res['net_incl_exempt'] = total_net_income + res['exempt']
    res['qcr_child'] = qcr_child
    res['rank_of'] = rank_of
    return res

def dec(x):
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    d = x.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    if d != 1:
        return '%d/%d' % (x.numerator, x.denominator)
    ip, rem = divmod(abs(x.numerator), x.denominator)
    fr = ''
    while rem:
        rem *= 10
        dg, rem = divmod(rem, x.denominator)
        fr += str(dg)
    return ('-' if x < 0 else '') + str(ip) + '.' + fr

```
