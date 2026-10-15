# Independent expectations: Holidays Act 2003 (NZ)

Written from the statute (`../registers/source-bundle/act_public_2003_129.txt`, as at 20 December 2023) and `BRIEF.md` only, before any `.l4` module was opened.
Each scenario gives the facts, the answer I expect, and the words of the Act that give it.
Scenario IDs (E-nnn) are cited in `tests-independent.l4`.
Money is in NZD. "Week" means a 5-day Monday-Friday working week unless stated otherwise.

Where the Act is ambiguous I say **AMBIGUOUS**, give my reading, and say why.

Calendar facts I worked out myself (Gregorian computus for Easter; weekday arithmetic):

| Year | Good Friday | Easter Monday | 25 Dec | 26 Dec | 1 Jan | 2 Jan | 6 Feb | 25 Apr | 1st Mon June | 4th Mon Oct |
|---|---|---|---|---|---|---|---|---|---|---|
| 2011 | 22 Apr | 25 Apr | | | | | | Mon (=Easter Mon) | | |
| 2021 | 2 Apr | 5 Apr | Sat | Sun | Fri | Sat | Sat | Sun | 7 Jun | 25 Oct |
| 2022 | 15 Apr | 18 Apr | Sun | Mon | Sat | Sun | Sun | Mon | 6 Jun | 24 Oct |
| 2023 | 7 Apr | 10 Apr | Mon | Tue | Sun | Mon | Mon | Tue | 5 Jun | 23 Oct |
| 2024 | 29 Mar | 1 Apr | Wed | Thu | Mon | Tue | Tue | Thu | 3 Jun | 28 Oct |
| 2025 | 18 Apr | 21 Apr | Thu | Fri | Wed | Thu | Thu | Fri | 2 Jun | 27 Oct |
| 2026 | 3 Apr | 6 Apr | Fri | Sat | Thu | Fri | Fri | Sat | 1 Jun | 26 Oct |
| 2027 | 26 Mar | 29 Mar | Sat | Sun | Fri | Sat | Sat | Sun | 7 Jun | 25 Oct |
| 2028 | 14 Apr | 17 Apr | Mon | Tue | Sat | Sun | Sun | Tue | 5 Jun | 23 Oct |
| 2038 | 23 Apr | 26 Apr | | | | | | Sun (=Easter Sun) | | |

---

## 1. Pay measures (ss 8-11, 14, 10A)

### Ordinary weekly pay, s 8

- **E-001** Base wage $1,000/week; regular commission $200; regular overtime $100; board cash value $50 (agreed, s 10(1)(a)); also received: irregular overtime $300, one-off bonus $500, discretionary payment $100, employer KiwiSaver contribution $30. **OWP = $1,350.** s 8(1)(a) "amount of pay ... for an ordinary working week"; (b)(i)-(iii) include regular commission, regular overtime, board; (c)(i)-(v) exclude irregular productivity/overtime, one-off, discretionary, super contribution.
- **E-002** Same, but the commission is *not* a regular part of pay. **OWP = $1,150** (s 8(1)(c)(i)).
- **E-003** Same as E-001 but no board. **OWP = $1,300.**
- **E-004** s 8(2): OWP cannot be determined under (1). Gross earnings for 4 calendar weeks before end of last pay period = $4,800; payments of the kind in s 8(1)(c)(i)-(iii) in that time = $400. **OWP = (4800 − 400) ÷ 4 = $1,100.** s 8(2), formula (a − b) ÷ c, c "is 4".
- **E-005** s 8(2) with normal pay period longer than 4 weeks (monthly, gross $4,333 for that month, no exclusions). **OWP = 4333 ÷ 4 = $1,083.25.** s 8(2)(a)(ii) "that pay period", but c "is 4". **AMBIGUOUS** in policy (a calendar month is about 4.33 weeks), but the text fixes c at 4; I follow the text.
- **E-006** s 8(2) with no exclusions: gross $4,000 → **$1,000.**
- **E-007** s 8(3): special rate $1,200 in agreement, calculated OWP $1,100 → **$1,200** (rate "equal to, or greater than").
- **E-008** s 8(3): special rate $1,000, calculated $1,100 → special rate ineffective (also s 6(3)); **$1,100.**
- **E-009** s 8(3): special rate equal to calculated ($1,100) → **$1,100.**

### Relevant daily pay, s 9

- **E-010** Would have received $200 wages + $50 overtime + $30 commission (both would have been received that day) + board $10; employer super $15. **RDP = $290.** s 9(1)(a)-(c).
- **E-011** Same but overtime would not have been worked that day → **$240.**
- **E-012** s 9(2): special rate $300 ≥ $290 → **$300**; special rate $250 → **$290.**
- **E-013** s 9(3): for a public holiday, RDP excludes the s 50(1)(a) half-time uplift: day's pay $200 → RDP **$200** (not $300).

### Average daily pay, s 9A

- **E-014** Gross for 52 weeks $52,000; days worked or on paid holiday/leave = 260. **ADP = $200.** s 9A(2), a ÷ b.
- **E-015** $45,000 over 225 days → **$200.**
- **E-016** Employer may use ADP only if RDP not possible/practicable (s 9A(1)(a)) or daily pay varies within the pay period (s 9A(1)(b)). Neither applies → **ADP may not be used.** Either applies → **may**.
- **E-017** Days the employee did not work and was not on paid leave (e.g. unpaid leave) are excluded from b; a part day counts as 1 ("whole or part days"). 200 whole + 10 part days, gross $42,000 → **ADP = $200.**

### Board or lodgings, s 10

- **E-018** Board provided, cash value agreed $60 → included in OWP/RDP (s 10(1)(a)).
- **E-019** Board provided because work requires an overnight stay away from home → **not included** (s 10(2)(a)).
- **E-020** Board provided because of special circumstances → **not included** (s 10(2)(b)).
- **E-021** No agreement on value → Labour Inspector determines (s 10(1)(b)); value is an input.

### Gross earnings, s 14 and s 10A

- **E-022** Over the period: wages $50,000; taxable allowance $2,000; annual and public holiday pay $4,000; commission $3,000; overtime $1,000; board $500; ACC first-week compensation paid by employer $800; travel payments under s 14 of the HCS Settlement Act $700. Also: discretionary bonus $1,000, ACC weekly compensation $2,000, volunteers-leave pay $300, actual-cost reimbursement $400, reasonably assessed reimbursement $200, employer super $1,500, cash-up paid under s 28B $900, HCS s 19 payment $250. **Gross earnings = $62,000.** s 14(a)(i)-(vii), s 14(b)(i)-(iii), s 14(c)(i)-(iv), s 10A.
- **E-023** A non-taxable allowance reimbursing actual costs → excluded (s 14(a)(ii) parenthesis and (c)(i)).

### Average weekly earnings, s 5 and s 16(3)

- **E-024** Gross $52,000 over 12 months → **AWE = $1,000** ("1/52 of an employee's gross earnings").
- **E-025** Agreed-included unpaid leave of exactly 1 week → no reduction; divisor **52**. (s 16(3) only applies to leave "of more than 1 week".)
- **E-026** Agreed-included unpaid leave of 3 weeks → divisor reduced by 2 → **50**; gross $50,000 → AWE **$1,000.**
- **E-027** Agreed-included unpaid leave of 1 week and 1 day → "whole or part weeks greater than 1 week" = 1 part week → divisor **51**. **AMBIGUOUS**: I read "number of whole or part weeks greater than 1 week" as the excess over 1 week rounded *up* to a whole number.
- **E-028** 2.5 weeks unpaid leave agreed included → excess 1.5 weeks → **2** → divisor **50.**

## 2. Annual holidays (ss 16-40)

### Entitlement date, s 16

- **E-030** Start 1 March 2024, no breaks → entitled on **1 March 2025** (12 months completed at end of 28 Feb 2025). On 28 Feb 2025 → **not yet** entitled. s 16(1) "After the end of each completed 12 months".
- **E-031** Second entitlement: **1 March 2026.**
- **E-032** 4 weeks' entitlement (s 16(1) "not less than 4 weeks'").
- **E-033** Unpaid leave for another reason of exactly 7 days (1 week) → counts (s 16(2)(a)(vi) "no more than 1 week") → anniversary still **1 March 2025.**
- **E-034** Unpaid leave for another reason of 8 days, not agreed → does not count (s 16(2)(b)) → anniversary pushed back by **8 days** to **9 March 2025**. **AMBIGUOUS**: the whole 8 days, not only the excess of 1 day, because (b) excludes "any other unpaid leave" and the 1-week allowance in (a)(vi) applies only to leave of "no more than 1 week".
- **E-035** Same 8 days but employer and employee agree it counts → anniversary **1 March 2025**; AWE divisor 51 (s 16(3)).
- **E-036** Unpaid sick leave of 3 weeks → counts (s 16(2)(a)(v)) → **1 March 2025.**
- **E-037** Parental leave of 6 months → counts (s 16(2)(a)(ii)) → **1 March 2025.**
- **E-038** ACC weekly compensation for 2 months → counts ((a)(iv)).
- **E-039** Volunteers leave → counts ((a)(iii)).
- **E-040** Entitlement remains in force until taken or paid out under s 28B (s 16(4)); it does not lapse after 12 months.

### Taking annual holidays, ss 17-20

- **E-041** s 18(1): employer must allow holidays within 12 months after entitlement arose (1 March 2025 → by 1 March 2026).
- **E-042** s 18(2): employee elects 2 weeks continuous → employer must allow. 3 weeks continuous → not required by s 18(2) (only "at least 2 weeks").
- **E-043** s 18(4): employer must not unreasonably withhold consent.
- **E-044** s 19: no agreement reached; notice given 1 December 2025, holidays start 15 December 2025 → 14 days → **valid**. **AMBIGUOUS** whether "14 days' notice" means clear days; I count the difference between the dates (15 − 1 = 14), which is the plain reading.
- **E-045** Notice 1 December, start 14 December → 13 days → **invalid.**
- **E-046** Employer and employee *agreed* on dates → s 19 does not apply; the employer cannot "require" → if they did reach agreement, no requirement power (s 19(1)(a)).
- **E-047** s 20: holidays in advance allowed only by agreement of an "agreed portion".

### Annual holiday pay, s 21

- **E-050** Entitled; takes 2 weeks; OWP $1,000; AWE $1,100 → rate $1,100/week → **$2,200.** s 21(2)(b) "the greater of".
- **E-051** OWP $1,200; AWE $1,100; 2 weeks → **$2,400.**
- **E-052** OWP = AWE = $1,000; 1 week → **$1,000.**
- **E-053** 1 day off (5-day week = 0.2 week), OWP $1,000, AWE $900 → **$200.**

### In advance, s 22

- **E-054** Worked ≥ 12 months but holiday in advance (e.g. between anniversaries with entitlement used): AWE over last 12 months, as s 21. OWP $900, gross $52,000 → AWE $1,000 → 1 week **$1,000.**
- **E-055** Worked < 12 months: 26 weeks exactly, gross $26,000 → AWE = 26000 ÷ 26 = **$1,000**; OWP $950 → 1 week **$1,000.** s 22(2)(b)(ii)(B), s 22(3).
- **E-056** Worked 26 weeks and 2 days, gross $27,000 → divisor 27 (whole or part weeks) → AWE **$1,000**; OWP $900 → **$1,000** per week.
- **E-057** Worked 10 weeks, gross $12,000, OWP $1,000 → AWE $1,200 → **$1,200** per week.

### Termination, ss 23-26, 40(3)

- **E-060** s 23: employment ends after 8 months, gross since start $30,000, nothing paid in advance or under s 28 → **$2,400** (8%).
- **E-061** s 23 with $1,000 paid for holidays in advance → **$1,400.**
- **E-062** s 23 with $500 advance and $300 PAYG under s 28 → **$1,600.**
- **E-063** s 23 deductions exceeding the 8%: advance paid $3,000, 8% = $2,400 → **$0 payable** (the formula gives −$600). **AMBIGUOUS**: the Act says "less any amount"; it does not authorise a negative payment or say the employer may recover the excess. I expect the payable amount to floor at 0; any recovery is outside this Act.
- **E-064** s 23 exactly 12 months? Employee started 1 March 2024 and employment ends on 1 March 2025 (entitlement has arisen) → s 23 does **not** apply; s 24 applies. Employment ends 28 February 2025 → s 23 applies (8%).
- **E-065** s 24: entitled, 2 weeks untaken, OWP at end $1,000, AWE $1,050 → **$2,100.**
- **E-066** s 24: 4 weeks untaken, OWP $1,200, AWE $1,000 → **$4,800.**
- **E-067** s 24: holidays fully taken → s 24 amount **$0** (s 24(1)(c) not met).
- **E-068** s 25: ends 6 months after last entitlement date; gross since then $26,000 → **$2,080.**
- **E-069** s 25 + s 26: same, plus s 24 payout of $2,100 paid in the final pay counts as gross earnings for s 25 → (26,000 + 2,100) × 8% = **$2,248**; total termination holiday pay = 2,100 + 2,248 = **$4,348.**
- **E-070** s 25 less $500 advance → from E-068: **$1,580.**
- **E-071** s 40(3): employment ends Friday 19 December 2025 with 2 weeks (10 working days, Mon-Fri worker) untaken. Notional holidays run Mon 22 Dec onwards; public holidays are not annual holidays (s 40(1)), so the notional period covers 22, 23, 24, 29, 30, 31 Dec, 5, 6, 7, 8 Jan and spans **4 public holidays** (25, 26 Dec, 1, 2 Jan) → employee paid for those 4 days at RDP/ADP.
- **E-072** s 40(3): a public holiday falling in the notional period on a day that would not otherwise be a working day → **not paid** (s 40(3)(a)).

### Timing, s 27

- **E-075** Ordinary case → pay **before** the holiday (s 27(1)).
- **E-076** Agreement to pay in the pay for the period → that pay (s 27(1)(a)).
- **E-077** Employment ended → in the **final pay** (s 27(1)(b), (2)).

### Pay-as-you-go, s 28

- **E-080** Fixed term 6 months (< 12 months), agreed in EA, identifiable, at 8% → **permitted.**
- **E-081** Same at 7.5% → **not permitted** (s 28(1)(d) "not less than 8%").
- **E-082** Same at exactly 8% with a gross of $10,000 → PAYG $800 (minimum).
- **E-083** Fixed term of exactly 12 months, regular hours → **not permitted** (s 28(1)(a)(i) "less than 12 months").
- **E-084** Intermittent/irregular work, agreed, identifiable, 8% → **permitted.**
- **E-085** Not agreed in the EA → **not permitted.**
- **E-086** Not paid as identifiable component → **not permitted.**
- **E-087** s 28(3): fixed term followed by permanent; PAYG received $1,500; 4 weeks' holiday pay otherwise $4,000 → **$2,500.**
- **E-088** s 28(4): PAYG wrongly used for a permanent full-time employee; employment continues 12 months → entitled to annual holidays under s 16 regardless.

### Cash-up, ss 28A-28F

- **E-090** Written request for 1 week, nothing yet paid out this entitlement year → may be agreed; pay = 1 week × max(OWP, AWE). OWP $1,000, AWE $1,100 → **$1,100.**
- **E-091** Already 0.6 week paid out in the year; requests 0.4 → **allowed** (total exactly 1 week).
- **E-092** Already 0.6 week; requests 0.5 → **not allowed** (total 1.1 weeks > "maximum of 1 week").
- **E-093** Oral request → **not a valid request** (s 28A(2)(a) "must be in writing").
- **E-094** Employer has a s 28E policy covering the employee's part of the business → s 28A **does not apply** (s 28E(3)).
- **E-095** Employer may decline without reason (s 28A(4)).
- **E-096** s 28B(2): employer paid out without a request → entitlement **remains** as if no payment.
- **E-097** Cash-up payment is excluded from gross earnings (s 14(c)(iv)).
- **E-098** Payment timing: as soon as practicable after agreement (s 28B(1)(b)).

### Closedowns, ss 29-35

- **E-100** Second closedown within 12 months (no s 30(2) agreement) → **not permitted** under ss 31-35.
- **E-101** s 32(3): notice 8 December, closedown starts 22 December → 14 days → **valid**; notice 9 December → **invalid.**
- **E-102** s 33: entitled employee with 3 weeks' entitlement, closedown 2 weeks → takes 2 weeks as annual holidays, paid under s 21.
- **E-103** s 33(3): entitlement 1 week, closedown 2 weeks → second week only *by agreement* as holidays in advance (s 22); otherwise not required.
- **E-104** s 34: started 1 August 2025, closedown starts 22 December 2025, gross since start $20,000 → **$1,600**; less advance $200 → **$1,400.**
- **E-105** s 35: that employee's 12 months treated as starting **22 December 2025** → next entitlement **22 December 2026** (absent nomination under s 35(2)).
- **E-106** Employee whose first anniversary is the closedown's first day (started 22 Dec 2024, closedown 22 Dec 2025) → entitled "at the commencement" → s 33, not s 34.

### Relationship with other leave, ss 36-40

- **E-110** s 36: sick during annual holidays → may be sick leave **only with employer agreement**.
- **E-111** s 37: bereavement during annual holidays → employer **must** allow bereavement leave.
- **E-112** s 37A: family violence → **must**.
- **E-113** s 38: sick before scheduled holidays → employer **must** allow sick leave (not discretionary, unlike s 36).
- **E-114** s 39: sick leave exhausted → employer **must not require** annual holidays; may agree if employee requests.
- **E-115** s 40(1): public holiday during annual holidays is a public holiday, not an annual holiday day (2 weeks over Christmas does not use the public holidays).

## 3. Public holidays (ss 44-61A)

### Dates, ss 44, 45, 45A (Mon-Fri worker unless stated)

- **E-120** 12 public holidays in s 44(1).
- **E-121** 2026: Good Friday **3 Apr 2026**; Easter Monday **6 Apr 2026**.
- **E-122** 2025: Good Friday **18 Apr**; Easter Monday **21 Apr**.
- **E-123** 2024: Good Friday **29 Mar 2024**; Easter Monday **1 Apr 2024**.
- **E-124** 2027: Good Friday **26 Mar 2027**; Easter Monday **29 Mar 2027**.
- **E-125** Sovereign's birthday 2026: **1 Jun 2026**; 2025: **2 Jun 2025**; 2027: **7 Jun 2027**.
- **E-126** Labour Day 2026: **26 Oct 2026**; 2025: **27 Oct 2025**; 2024: **28 Oct 2024**.
- **E-127** ANZAC Day 2026 is a Saturday; not a working day → **Mon 27 Apr 2026** (s 45A(1)(b)).
- **E-128** ANZAC Day 2026, Saturday is a working day → **Sat 25 Apr 2026** (s 45A(1)(a)).
- **E-129** ANZAC Day 2027 (Sunday), non-working → **Mon 26 Apr 2027**.
- **E-130** Waitangi Day 2027 (Saturday), non-working → **Mon 8 Feb 2027**; 2026 (Friday) → **Fri 6 Feb 2026**.
- **E-131** Christmas 2026 Friday → **25 Dec 2026**. Boxing Day 2026 Saturday, non-working → **Mon 28 Dec 2026** (s 45(1)(b)).
- **E-132** Christmas 2027 (Sat), non-working → **Mon 27 Dec 2027**; Boxing Day 2027 (Sun), non-working → **Tue 28 Dec 2027** (s 45(1)(d)).
- **E-133** Christmas 2022 (Sun), non-working → **Tue 27 Dec 2022**; Boxing Day 2022 (Mon) → **Mon 26 Dec 2022**.
- **E-134** 1 Jan 2023 (Sun), non-working → **Tue 3 Jan 2023**; 2 Jan 2023 (Mon) → **Mon 2 Jan 2023**.
- **E-135** 2 Jan 2027 (Sat), non-working → **Mon 4 Jan 2027**; 1 Jan 2027 (Fri) → **Fri 1 Jan 2027**.
- **E-136** 1 Jan 2028 (Sat) → **Mon 3 Jan 2028**; 2 Jan 2028 (Sun) → **Tue 4 Jan 2028**.
- **E-137** Christmas 2027 Saturday *is* a working day → **Sat 25 Dec 2027**; Boxing Sunday not a working day → **Tue 28 Dec 2027**. The text sends a Sunday holiday to the "following Tuesday" whatever happened to Saturday's. **AMBIGUOUS** in policy (Monday 27 is then free of any holiday), but the text is explicit.
- **E-138** Christmas 2027 Saturday not working; Boxing Sunday working → Christmas **Mon 27 Dec**, Boxing **Sun 26 Dec**.
- **E-139** Weekend worker (works Sat and Sun) → Christmas and Boxing 2027 stay on **25 and 26 Dec**; no Monday/Tuesday holiday (s 45(2): no more than 4).
- **E-140** 2011: Easter Monday and ANZAC Day both 25 Apr → **1 day** (s 44(2)).
- **E-141** 2038: ANZAC Day falls on Easter Sunday (non-working) → moves to Mon 26 Apr 2038, which is Easter Monday → **1 day**. **AMBIGUOUS**: s 44(2) speaks of holidays in "subsection (1)" falling on the same day; s 45A says the holiday "must be treated as falling on" Monday. I read s 44(2) as applying to the treated date ("for the purposes of this subpart"), so 1 day. The alternative (no extra day) gives the same count; an argument that ANZAC moves to Tuesday has no textual basis.
- **E-142** Matariki 2026 (input 10 Jul 2026) is a public holiday; it is not Mondayised (not in s 45 or s 45A).
- **E-143** Waitangi Day on a weekday (Thursday 6 Feb 2025) → that day; no transfer.

### Transfers, ss 44A-44C

- **E-145** s 44B: all criteria met (holiday identified, otherwise working day; target identified, otherwise working day, not a public holiday; purpose not avoidance), agreed in writing → **valid**.
- **E-146** Target day is itself a public holiday → **invalid** (s 44B(2)(b)(iii)).
- **E-147** Target day not otherwise a working day → **invalid**.
- **E-148** Purpose is to avoid ss 50/56 → **invalid** (s 44B(2)(c)).
- **E-149** Agreement not in writing → **invalid**.
- **E-150** Employer s 44C policy covering the business → **no transfer** (s 44C(3)).
- **E-151** s 44A: shift starts one day and ends the next, one is a s 44(1) day, purpose not avoidance, in writing → **valid**; a shift within one day → s 44A **does not apply**.

### Working on a public holiday, ss 47-50, 55

- **E-155** s 47: may require work only if otherwise working day **and** EA requires it.
- **E-156** s 49: does not work, otherwise working day, RDP $200 → **$200**.
- **E-157** s 49: does not work, not otherwise working day → **$0**, no entitlement.
- **E-158** s 50: works 4 hours of an 8-hour day; RDP portion for time worked $120 with no penal rates → **$180** (120 + 60).
- **E-159** s 50: portion of RDP for time worked $200, of which penal rates $80 → (200 − 80) × 1.5 = 180 vs 200 → **$200**.
- **E-160** s 50: portion $240, penal $40 → 200 × 1.5 = 300 vs 240 → **$300**.
- **E-161** s 50(2): an extra payment for a sixth day of work is **not** a penal rate → not deducted.
- **E-162** s 55: paid in the pay for the pay period in which the holiday occurs.

### Alternative holidays, ss 56-61

- **E-165** Works on PH that is an otherwise working day → **alternative holiday** + time and a half.
- **E-166** Works on PH that is *not* otherwise working day → **no alternative holiday**, but time and a half (s 48(1)(b), s 50).
- **E-167** Works only on public holidays → **no alternative holiday** (s 56(4)).
- **E-168** Works 1 hour of the PH → still a whole alternative holiday (s 56(1)(b) "any part", s 57(1)(c)).
- **E-169** s 59(2): on call, otherwise working day, called in → **alternative holiday**.
- **E-170** s 59(3): on call, not called in, restriction means no whole holiday → **alternative holiday**; restriction slight → **none**.
- **E-171** s 59(1)(a): on call on a day that is not otherwise a working day → s 59 does not apply → **none**.
- **E-172** s 60(1): AH pay = RDP or ADP, e.g. **$200**.
- **E-173** s 60(2)(b): AH untaken at termination → paid at RDP for the last day of employment, in the final pay.
- **E-174** s 61: entitlement arose 25 Dec 2024; request on 25 Dec 2025 → **may request** (12 months have passed); on 24 Dec 2025 → **may not**.
- **E-175** s 57(1)(d): AH may not be taken on a public holiday; s 57(1)(b) must be an otherwise working day.
- **E-176** s 57(3): employer fixes the AH date → at least 14 days' notice; 14 days → valid, 13 → invalid.

### s 61A

- **E-178** Rostered to work on a PH, sick and does not work → paid under s 49 (RDP, **not** time and a half), **no** alternative holiday, day is a public holiday (sick leave balance unchanged).

## 4. Sick leave and bereavement leave (ss 63-72)

### Entitlement, s 63

- **E-180** Start 1 March 2025 → entitled on **1 September 2025**; on 31 August 2025 → **not**.
- **E-181** Start 31 August 2025 → 6 months completed → entitled **28 February 2026**? **AMBIGUOUS** for month-end starts. I avoid asserting this.
- **E-182** Next entitlement period: **1 September 2026** (s 63(2)(a)(ii)).
- **E-183** s 63(1)(b): over 6 months, average 10 h/week and ≥ 1 h every week → **entitled**.
- **E-184** Average 9.9 h/week, every week ≥ 1 h → **not entitled**.
- **E-185** Average 12 h/week; one week with 0 h; every month ≥ 40 h → **entitled** (the "or" limb).
- **E-186** Average 12 h/week; one week 0 h; one month 35 h → **not entitled**.
- **E-187** Average exactly 10 h, every month exactly 40 h → **entitled** ("at least", "no less than").

### Sick leave quantity, ss 65-67

- **E-190** **10 days** per 12-month period (s 65(2)).
- **E-191** Carry-over: 10 unused → next period **20**.
- **E-192** 3 unused → **13**.
- **E-193** 0 unused → **10**.
- **E-194** 15 unused (from a 20-day balance less 5) → carry over capped at 10 → **20**.
- **E-195** 20 unused → **20** (cap 20).
- **E-196** 7 unused → **17**.
- **E-197** s 67: unused sick leave at termination → **$0**.

### Proof, s 68

- **E-200** Sick 3 consecutive calendar days (Fri, Sat, Sun; only Fri a working day) → employer **may** require proof (whether or not working days).
- **E-201** Sick 2 consecutive days, employer did not inform early / pay costs → **may not** require.
- **E-202** Sick 2 days, employer informs early and agrees to pay reasonable expenses → **may** require (s 68(1A)).
- **E-203** Sick 1 day, informs early but does not agree to pay → **may not**.
- **E-204** s 72(2): proof required, not produced without reasonable excuse → employer may withhold pay until produced.

### Sick leave pay, s 71

- **E-205** 3 days sick, all working days, RDP $200 → **$600**.
- **E-206** Sick Fri-Mon (4 calendar days), Mon-Fri worker → 2 working days → **$400**, 2 days deducted.
- **E-207** s 71(4): employer tops up first-week/weekly comp for 12 whole days → may deduct **2 days**; 4 days → **0**; 5 days → **1**.

### Bereavement leave, ss 69-70

- **E-210** Death of parent → **3 days**.
- **E-211** Death of spouse/partner, child, sibling, grandparent, grandchild, spouse's parent → **3 days** each.
- **E-212** Death of cousin, employer accepts bereavement → **1 day**; employer does not accept → **0**.
- **E-213** Employee's own miscarriage → **3 days** (s 69(2)(c), s 70(1)(a)).
- **E-214** Partner's still-birth → **3 days** (s 69(2)(d)).
- **E-215** Former partner's miscarriage, would have been biological parent → **3 days**.
- **E-216** Pregnancy ended by abortion services → not a miscarriage → **0** (s 69(4)).
- **E-217** Death of parent and grandparent at same time → **6 days** (s 70(2)).
- **E-218** Two separate bereavements in one entitlement year → 3 + 3 = **6** (no annual cap).
- **E-219** Not yet 6 months employed, no advance agreement → **0**.
- **E-220** Bereavement leave pay: 3 working days at RDP $200 → **$600**.

## 5. Family violence leave (ss 72A-72J)

- **E-230** Affected person, 6 months completed → **10 days** per period.
- **E-231** Start 1 March 2025 → entitled **1 September 2025**; 31 August 2025 → not.
- **E-232** No carry forward: 10 unused → next period **10**.
- **E-233** Violence occurred before employment → **still qualifies** (s 72C(a)).
- **E-234** Child against whom violence inflicted ordinarily resides with employee → **qualifies** (s 72B(b)).
- **E-235** Proof may be required whatever the length (s 72G).
- **E-236** Pay: 2 working days at RDP $200 → **$400**.
- **E-237** s 72I(4): 10 whole days topped up → may deduct **2 days**.
- **E-238** s 72F: not paid out at termination → **$0**.
- **E-239** s 72D(1)(b) hours test as E-183 to E-186.

## 6. Enforcement and records (ss 73-86)

### Penalties, s 75

- **E-250** Individual employer → max **$10,000**; company → **$20,000** per failure.
- **E-251** Person involved (individual) → **$10,000**; body corporate → **$20,000**.
- **E-252** Penalty provisions include: s 16, ss 21-28, s 28A, s 28B, s 40(3), s 46, ss 49-56, s 60, s 61(3), s 63, s 65, ss 69-72, s 72C, ss 72H-72J, s 81, s 82 → **penalty available**.
- **E-253** Not listed: s 18, s 19, s 40(1), s 57, s 66, s 67, s 68, s 72G, s 73 → **no penalty under s 75**. (s 66, carry-over, is notably absent; s 65 is listed.)

### Who may sue, ss 74, 76, 77, 77A

- **E-255** s 74(1): employee, authorised representative, union representative, employer, Labour Inspector may enforce.
- **E-256** s 74(2): enhanced (above-minimum) entitlements → only employee, authorised representative, union representative; **not** Labour Inspector, **not** employer.
- **E-257** s 76(1): penalty against employer → Labour Inspector **yes**, employee **yes**, union representative **no**, authorised representative **no**.
- **E-258** s 76(2): penalty against a person involved → **only** Labour Inspector; employee **no**.
- **E-259** s 77: arrears recovery on behalf of employee → Labour Inspector may.

### Time limits, s 76(5), (5A)

- **E-260** Cause known 1 March 2025 → must commence within 12 months → filed **1 March 2026** in time; **2 March 2026** out of time. **AMBIGUOUS** about the anniversary day itself; I treat "within 12 months after" as inclusive of the anniversary date.
- **E-261** Became known 1 March 2025 but should reasonably have been known 1 January 2025 → time runs from the earlier, **1 January 2025** → deadline 1 January 2026; filing 1 February 2026 out of time.
- **E-262** s 76(5A): court refuses a s 142E order on 10 June 2026 → action must start within 3 months → **10 September 2026** in time; 11 September out.

### s 77A

- **E-265** Unpaid $5,000; employer can pay $2,000 → recoverable from person involved **$3,000**.
- **E-266** Employer can pay all → **$0** from person involved.
- **E-267** Employee recovering → needs prior leave of Authority/court; without leave → **no**. Labour Inspector needs no leave.
- **E-268** Person not "involved" (ERA s 142W) → **no** recovery.

### Records, ss 81-83

- **E-270** Information entered 1 April 2020 → keep until at least **1 April 2026** (s 81(4), "not less than 6 years").
- **E-271** s 82: employee, authorised representative, union representative, Labour Inspector may request access; anyone else **no**.
- **E-272** s 83: if failure to keep record prevented accurate claim → Authority may accept employee's statements.

### s 84, s 85

- **E-275** Interest may be included, capped by ERA Sch 2 cl 11.
- **E-276** Dismissed 1 June 2025, re-employed 1 July 2025 → within 1 month → **continuous**. **AMBIGUOUS** at the exact month; I read "within 1 month after" as inclusive.
- **E-277** Re-employed 2 July 2025 → **not presumed continuous**.
- **E-278** Re-employed within 1 month, but Labour Inspector determines employer acted in good faith and not to evade → presumption **does not apply**; if determination finds only good faith but evasion purpose → presumption **applies**.

### Miscellaneous

- **E-280** s 6(3): agreement giving less than the minimum is of no effect to that extent (e.g. 8 days' sick leave → 10 days).
- **E-281** s 7: Armed Forces → Act does not apply.

---

## Scenarios added after reading the encoding (expected values from the statute, written before running)

- **E-033b** Two separate 5-day spells of other unpaid leave → each is "no more than 1 week" → both count → **1 March 2025**.
- **E-072b** s 40(3), employment ends Fri 18 Dec 2026, 10 working days untaken (Mon-Fri) → notional days 21-24, 29-31 Dec, 5-7 Jan; public holidays 25 Dec, Mon 28 Dec (Boxing Day moved), 1 Jan, Mon 4 Jan (2 Jan moved) → **4**. **AMBIGUOUS**: s 45 moves the days "for the purposes of this subpart" (subpart 3), and s 40 is in subpart 1. Read literally, Boxing Day (Sat) and 2 January (Sat) would not be working days and would not be paid under s 40(3). I prefer the purposive reading (the moved days count), since s 40(1) would otherwise make a Mondayised holiday into an annual-holiday day.
- **E-073** s 40(2)(b): s 40(3) pay is only for an employee who "is entitled to annual holidays". An employee under s 23 (not yet entitled) gets the 8% and nothing for public holidays in a notional holiday. So with 2 such holidays entered, final holiday pay is still **$2,400**.
- **E-016c** Daily pay varies within the pay period and the employer elects ADP ($200) though RDP would be $250 → **$200** (s 9A(1) "may use"; s 49 "relevant daily pay or average daily pay").
- **E-071d** Mon-Wed part-timer ending Fri 19 Dec 2025, 6 working days untaken → no public holiday falls on a Mon-Wed in the notional period → **0**.
- **E-219b** Bereavement leave in advance by agreement (s 63(3)(a)) before 6 months → allowed, 3 days, **$600**.
- **E-281b** s 81 record with every item → complies; without the employee's name → does not.

## Scenarios the encoding could not express (not asserted)

- **E-002/E-003, E-011, E-013, E-021, E-023**: what is "regular", what the employee "would have received", and the s 9(3)/9A(3) exclusion of the s 50 uplift are all inputs already summed. Only the arithmetic can be tested.
- **E-064** (does s 23 or s 24 apply when employment ends on the anniversary): "the employee has become entitled" is an input, not computed from the dates. E-030 covers the date itself.
- **E-140** (2011, Easter Monday = ANZAC Day): the encoding refuses any year before 2022 because Matariki was not then a public holiday. That is defensible, so I did not assert it. The same-day rule is tested for 2038 instead (E-141).
- **E-181** (6 months from a 31 August start): left out as ambiguous.
- **E-184 to E-187** (the s 63(1)(b) / s 72D(1)(b) hours test: average of 10 h/week, 1 h every week **or** 40 h every month): the encoding takes only the date on which the test was first met, so the averages and the "or" limb cannot be tested.
- **E-216** (own pregnancy ended by abortion services, which is not a "miscarriage" under s 69(4)): there is no constructor for it. The `(d) ... for anyone else` constructor is about a different person, not this case.
- **E-218** (two bereavements at different times in one year): each spell is a separate call, so there is nothing to check.
- **s 28(1A)/(2)** (a series of fixed terms beyond 12 months, agreed to stay on pay-as-you-go): not modelled.
- **s 28A cash-up requires an existing entitlement**: `Payout request` has no field for the entitlement held, so a cash-up in the first year (no entitlement yet) would be paid.
- **s 16(3) divisor in a cash-up (s 28B → s 21(2)) and in a closedown under s 33**: both use gross ÷ 52 and ignore agreed unpaid leave. The `Payout request` and `Closedown` records have no absences list, unlike `Annual holiday` and `End of employment`.
- **s 12(4) / s 61A** for a day that is not normally worked but which the employee had agreed to work: AMBIGUOUS, not asserted.
- **E-253 per provision** (ss 18, 19, 57, 66, 68, 72G carry no s 75 penalty): the caller classifies the breach as `another provision`, so the encoding cannot be wrong about it, and s 66 cannot be asked about directly.
- **s 6(3), s 7, s 84**: no computation.
