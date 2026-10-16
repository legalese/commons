# Independent expectations: Tax Administration Act 1994 (PAYE reporting, returns, penalties)

Written from BRIEF.md and the source text (TAA as at 4 September 2026; Income Tax Act 2007 s YA 1, s YE 1) **before** opening any `.l4` file. Expected values here are not to be changed after the encoding is opened.

## Calendar used (worked out by hand and checked with a small script)

Non-working days (ITA s YA 1 "working day"): Saturdays, Sundays, and

| Year | Waitangi | Good Fri / Easter Mon | Anzac | Sovereign's bday (1st Mon June) | Matariki | Labour Day (4th Mon Oct) |
|---|---|---|---|---|---|---|
| 2026 | Fri 6 Feb | 3 Apr / 6 Apr | Sat 25 Apr -> Mon 27 Apr | 1 Jun | 10 Jul | 26 Oct |
| 2027 | Sat 6 Feb -> Mon 8 Feb | 26 Mar / 29 Mar | Sun 25 Apr -> Mon 26 Apr | 7 Jun | 25 Jun | 25 Oct |
| 2028 | Sun 6 Feb -> Mon 7 Feb | 14 Apr / 17 Apr | Tue 25 Apr | 5 Jun | (input) | 23 Oct |

plus "a day in the period starting on 25 December in a year and ending on 15 January (both dates inclusive) in the following year".

**Reading of "within N working days after payday"**: the last permitted day is the Nth working day counted from the day after payday (payday itself never counts, whether or not it is a working day).

## Goal 1: working days and employment income information

### Working day (ITA s YA 1)

| id | date | expected working day? | words relied on |
|---|---|---|---|
| WD1 | Fri 6 Feb 2026 | no | "Waitangi Day" |
| WD2 | Mon 8 Feb 2027 | no | "if Waitangi Day ... falls on a Saturday or a Sunday, the following Monday" |
| WD3 | Tue 9 Feb 2027 | yes | — |
| WD4 | Mon 27 Apr 2026 | no | "if ... Anzac Day falls on a Saturday or a Sunday, the following Monday" |
| WD5 | Tue 25 Apr 2028 | no | "Anzac Day" |
| WD6 | Mon 1 Jun 2026 | no | "the Sovereign's birthday" |
| WD7 | Fri 10 Jul 2026 (Matariki given as input) | no | "Matariki Observance Day" |
| WD8 | Mon 26 Oct 2026 | no | "Labour Day" |
| WD9 | Thu 24 Dec 2026 | yes | period starts 25 December |
| WD10 | Fri 25 Dec 2026 | no | "starting on 25 December" |
| WD11 | Fri 15 Jan 2027 | no | "ending on 15 January (both dates inclusive)" |
| WD12 | Mon 18 Jan 2027 | yes | — |
| WD13 | Fri 3 Apr 2026 / Mon 6 Apr 2026 | no / no | "Good Friday, Easter Monday" |
| WD14 | Tue 7 Apr 2026 | yes | — |
| WD15 | Sat 17 Oct 2026 | no | "a Saturday" |

### Employer groups (ss 23D-23H)

Threshold: s 23F(5)(a) "gross amounts of tax payable for the preceding tax year that are below the threshold amount"; s 23F(6) "$50,000". Non-electronic requires s 23F(1)(b) "does not deliver ... electronically" and (c) "is not included in the new group".

| id | inputs | expected group / days | provision |
|---|---|---|---|
| EG1 | existing employer, preceding-year PAYE+ESCT $49,999, paper delivery, no exemption | non-electronic, 10 working days | s 23F(1), (5)(a) "below", (2)(b) "within 10 working days" |
| EG2 | same but $50,000 exactly | online, 2 working days | "below the threshold" — $50,000 is not below; s 23E(1), (2)(b) |
| EG3 | $20,000 but delivers through payroll software | online, 2 working days | s 23F(1)(b); s 23D(2)(b) |
| EG4 | $80,000, s 23G exemption, paper | non-electronic, 10 working days | s 23F(1)(a) "or has an exemption under section 23G" |
| EG5 | $80,000, no exemption, paper | online, 2 working days | s 23E(1) |
| EG6 | new employer (started 1 Aug 2026), paper, payday in new-employer period | new group, 10 working days (if chosen) | s 23H(1), (3)(b) |
| EG7 | new employer delivering electronically | online, 2 working days | s 23H(5) "immediately included in the online group" |
| EG8 | PAYE intermediary | online | s 23D(2)(a) |
| EG9 | new employer started 1 Aug 2026; payday 31 Jan 2027 (paper) | in new-employer period; 10 working days -> Mon 15 Feb 2027 | s 23H(2) "6-month period that starts on the date ... on which the employer starts employing" (period 1 Aug 2026 - 31 Jan 2027 inclusive) |
| EG10 | same employer, accumulated tax $60,000, payday Mon 1 Feb 2027 | outside new-employer period, online, 2 working days -> Wed 3 Feb 2027 | s 23F(7) "following that period, is included in the online group" |

Ambiguity (EG9/EG10): whether a 6-month period starting 1 Aug ends on 31 Jan or 1 Feb; I take 31 Jan (6 calendar months including the start day). Whether a new employer below the threshold after the period is "non-electronic" via s 23F(5)(b) is not tested.

### Due dates for employment income information

| id | group / option | payday | expected last day | note |
|---|---|---|---|---|
| DL1 | online | Wed 14 Oct 2026 | Fri 16 Oct 2026 | s 23E(2)(b) |
| DL2 | online | Thu 15 Oct 2026 | Mon 19 Oct 2026 | weekend |
| DL3 | online | Fri 23 Oct 2026 | Wed 28 Oct 2026 | Labour Day 26 Oct |
| DL4 | online | Tue 22 Dec 2026 | Thu 24 Dec 2026 | — |
| DL5 | online | Wed 23 Dec 2026 | Mon 18 Jan 2027 | 25 Dec-15 Jan |
| DL6 | online | Fri 15 Jan 2027 | Tue 19 Jan 2027 | payday non-working |
| DL7 | online | Thu 25 Mar 2027 | Wed 31 Mar 2027 | Easter 26/29 Mar |
| DL8 | online | Fri 23 Apr 2027 | Wed 28 Apr 2027 | Anzac Mondayised 26 Apr |
| DL9 | online | Fri 24 Apr 2026 | Wed 29 Apr 2026 | Anzac Mondayised 27 Apr |
| DL10 | online, Matariki 10 Jul 2026 given | Thu 9 Jul 2026 | Tue 14 Jul 2026 | Matariki |
| DL11 | online | Fri 29 May 2026 | Wed 3 Jun 2026 | Sovereign's birthday 1 Jun |
| DL12 | online | Fri 5 Feb 2027 | Wed 10 Feb 2027 | Waitangi Mondayised 8 Feb |
| DL13 | online | Thu 5 Feb 2026 | Tue 10 Feb 2026 | Waitangi Fri 6 Feb |
| DL14 | non-electronic | Thu 15 Oct 2026 | Fri 30 Oct 2026 | s 23F(2)(b) |
| DL15 | non-electronic | Wed 9 Dec 2026 | Wed 23 Dec 2026 | — |
| DL16 | non-electronic | Thu 10 Dec 2026 | Thu 24 Dec 2026 | last day before break |
| DL17 | non-electronic | Fri 11 Dec 2026 | Mon 18 Jan 2027 | over break |
| DL18 | non-electronic | Fri 18 Dec 2026 | Mon 25 Jan 2027 | over break |
| DL19 | non-electronic | Mon 15 Mar 2027 | Wed 31 Mar 2027 | Easter |

### Twice-monthly payday option (s 23F(3)(b))

"for an amount paid ... in the period that starts on the 1st day of a month and ends on the 15th day of the month, the 15th of the month; and ... 16th day ... last day of the month, the last day of the month."

| id | payment date | treated payday | expected last day (10 wd) |
|---|---|---|---|
| TM1 | Tue 3 Nov 2026 | Sun 15 Nov 2026 | Fri 27 Nov 2026 |
| TM2 | Sun 15 Nov 2026 | 15 Nov 2026 | Fri 27 Nov 2026 |
| TM3 | Mon 16 Nov 2026 | Mon 30 Nov 2026 | Mon 14 Dec 2026 |
| TM4 | Tue 1 Dec 2026 | Tue 15 Dec 2026 | Wed 20 Jan 2027 |
| TM5 | Sat 20 Feb 2027 | Sun 28 Feb 2027 | Fri 12 Mar 2027 |
| TM6 | Wed 15 Jul 2026 vs Fri 31 Jul 2026 | 15 Jul / 31 Jul | Wed 29 Jul 2026 / Fri 14 Aug 2026 |
| TM7 | Tue 3 Nov 2026, actual-payday option (s 23F(3)(a)) | 3 Nov 2026 | Tue 17 Nov 2026 |

### Ceasing to employ (s 23M)

"within 30 working days after the date on which they stop employing employees"

| id | stop date | expected last day |
|---|---|---|
| CE1 | Fri 13 Nov 2026 | Mon 18 Jan 2027 |
| CE2 | Fri 20 Nov 2026 | Mon 25 Jan 2027 |
| CE3 | Wed 31 Mar 2027 | Thu 13 May 2027 |
| CE4 | Wed 30 Jun 2027 (Matariki 25 Jun 2027 is before; irrelevant) | Wed 11 Aug 2027 |
| CE5 | cessation not intended to be permanent | no s 23M obligation ("intending that the cessation is permanent") |

### Non-notified tax codes (s 24E; ITA sch 2 pt A cl 3 rate 0.45)

Reading: "has not notified their employer of— their name; and their tax file number; and their tax code" means the employee has not notified all three, so missing any one makes the code non-notified (it is the conjunction that must be notified). This is the reading under which (a) does any work for an employee who gives a code but no TFN. Ambiguous; the alternative (only when none of the three is notified) is rejected.

| id | inputs | expected |
|---|---|---|
| NN1 | name, TFN and code all notified; no Commissioner code; not NRSW; not s 24D | not non-notified |
| NN2 | TFN missing, other two given | non-notified |
| NN3 | name missing only | non-notified |
| NN4 | nothing notified; Commissioner provided code (sch 5 pt A cl 3) | not non-notified (s 24E(1)(b)) |
| NN5 | nothing notified; non-resident seasonal worker | not non-notified (s 24E(1)(c)) |
| NN6 | nothing notified; person referred to in s 24D | not non-notified ("other than a person referred to in section 24D") |
| NN7 | nothing notified, none of the exceptions | non-notified |
| NN8 | non-notified; payment $1,000 | tax $450 ("rate of 0.45 for each dollar") |

## Goal 2: returns and the time bar

### Who must file (s 33(1))

| id | inputs | expected |
|---|---|---|
| RF1 | person deriving only exempt income | no return required ("other than a person who derives only exempt income") |
| RF2 | person with some assessable income | must file |

### Due date (s 37(1))

"(a) in the case of any taxpayer with a late balance date, not later than the seventh of the month which is the fourth month after the end of the taxpayer's corresponding income year: (b) in all other cases, not later than 7 July in each year." Late balance date = income year ending 1 April-30 September (ITA s YE 1(7)).

Reading for (b): 7 July following the end of the tax year (31 March). For an early balance date (1 Oct-30 Mar) the corresponding tax year ends on the 31 March following the balance date.

| id | balance date (end of income year) | expected due date |
|---|---|---|
| RD1 | 31 Mar 2027 (standard, 2026-27) | 7 Jul 2027 |
| RD2 | 31 Mar 2028 (standard) | 7 Jul 2028 |
| RD3 | 30 Sep 2027 (late) | 7 Jan 2028 |
| RD4 | 30 Jun 2027 (late) | 7 Oct 2027 |
| RD5 | 30 Apr 2027 (late) | 7 Aug 2027 |
| RD6 | 31 Aug 2027 (late) | 7 Dec 2027 |
| RD7 | 31 Dec 2026 (early) | 7 Jul 2027 |
| RD8 | 31 Oct 2026 (early) | 7 Jul 2027 |
| RD9 | 30 Sep 2026 (late) | 7 Jan 2027 |

### Latest extended date (s 37(5))

(a) 31 March year: not "later than the 31 March that immediately succeeds that 31 March"; (b)(i) date "between 30 September and the next succeeding 31 March": "the 31 March next succeeding the 31 March that immediately succeeds that date"; (b)(ii) date "between 31 March and the next succeeding 1 October": "the 31 March that immediately succeeds that date".

| id | balance date | expected latest extension |
|---|---|---|
| EX1 | 31 Mar 2027 | 31 Mar 2028 |
| EX2 | 31 Dec 2026 | 31 Mar 2028 |
| EX3 | 30 Sep 2026 | 31 Mar 2027 |
| EX4 | 31 Oct 2026 | 31 Mar 2028 |
| EX5 | 30 Jun 2027 | 31 Mar 2028 |
| EX6 | 30 Apr 2027 | 31 Mar 2028 |
| EX7 | 28 Feb 2027 | 31 Mar 2028 |

### Time bar (s 108(1), (2))

"4 years have passed from the end of the tax year in which the taxpayer provides the tax return". Reading: the Commissioner may increase up to and including the 31 March that is 4 years after the end of the tax year in which the return was *provided* (not the year it relates to).

| id | inputs | expected |
|---|---|---|
| TB1 | return provided 15 Jun 2027 | may increase until 31 Mar 2032 |
| TB2 | return provided 31 Mar 2027 | until 31 Mar 2031 |
| TB3 | return provided 1 Apr 2027 | until 31 Mar 2032 |
| TB4 | TB1 asked on 31 Mar 2032 / 1 Apr 2032 | may / may not |
| TB5 | return fraudulent or wilfully misleading | no time limit (s 108(2)(a) "at any time") |
| TB6 | return omits income of a particular nature or source | no time limit (s 108(2)(b)) |
| TB7 | no return provided | s 108(1) does not bar (requires "furnishes an income tax return and an assessment has been made") |

## Goal 3: late filing and late payment penalties

### Late filing penalty (s 139A)

Liability requires both "(a) the taxpayer does not complete and provide on time" and "(b) the Commissioner notifies the taxpayer that the penalty is payable".

| id | inputs | expected |
|---|---|---|
| LF1 | annual return late, notified, net income $99,999 | $50 ("below $100,000") |
| LF2 | net income $100,000 | $250 ("both figures inclusive") |
| LF3 | net income $1,000,000 | $250 |
| LF4 | net income $1,000,001 | $500 ("above $1,000,000") |
| LF5 | net income $0 | $50 |
| LF6 | late, not notified | no penalty ($0) |
| LF7 | filed on time, notified | no penalty |
| LF8 | employment income information late, notified | $250 (s 139A(4)) |
| LF9 | EII, several late filings in one month | at most $250 for the month (s 139A(9)) |
| LF10 | EII first failure after 12 months of on-time delivery | no penalty yet; Commissioner must first give a warning notice (s 139A(6)-(8)) |
| LF11 | annual return, no 30-day prior notice given (individual or public) | penalty may not be imposed (s 139A(5)) |
| LF12 | EII, no 30-day prior notice | (5) does not apply to EII: $250 still |

### Late payment penalty (s 139B)

Readings:
- "4% of the amount of tax to pay" — "tax to pay" includes penalties already imposed (s 139B(6)), so the 4% is on unpaid tax + the 1%.
- Timing: 1% "on the day after the default date"; 4% "at the end of the sixth day after" that day, i.e. at the end of default date + 7. Whether a query "as at" default+7 includes the 4% is ambiguous (added at end of day); I test default+6 (no) and default+8 (yes) only.
- Incremental: "1% of the amount of tax to pay determined on each day that falls 1 month after a day on which a penalty is imposed under this subsection", added "on the day after the last day of successive monthly intervals". I read the monthly chain as starting from the day the initial 1% is imposed (default + 1), so the first incremental is one calendar month after default + 1. (Chaining also off the 4% day would double-count and is rejected.) Ambiguous.
- s 139B(5): non-existent day -> last day of the month.
- No part-payments in these scenarios. Amounts exact (no rounding).

Base: unpaid tax $10,000, default date Wed 20 Jan 2027, liability condition met (e.g. provisional tax, or prior late payment), incremental not excluded.

| id | as at | expected total late payment penalty |
|---|---|---|
| LP1 | 20 Jan 2027 (default date) | $0 |
| LP2 | 21 Jan 2027 | $100 (1%) |
| LP3 | 26 Jan 2027 | $100 |
| LP4 | 28 Jan 2027 | $504 (100 + 4% of 10,100) |
| LP5 | 20 Feb 2027 | $504 |
| LP6 | 21 Feb 2027 | $609.04 (+1% of 10,504) |
| LP7 | 21 Mar 2027 | $715.1304 (+1% of 10,609.04) |
| LP8 | 21 Mar 2027, tax is one of the s 139B(2B) taxes (e.g. income tax 2026-27) | $504 (no incremental) |
| LP9 | default 28 Jan 2027, as at 27 Feb 2027 | $504 |
| LP10 | default 28 Jan 2027, as at 28 Feb 2027 | $609.04 (29 Feb does not exist -> 28 Feb, s 139B(5)) |
| LP11 | good payment history, no s 139B(1)(c) notice, not provisional | no penalty (s 139B(1) not satisfied) |
| LP12 | good history, notice dated 1 Feb 2027 with further date 15 Feb 2027, unpaid on 15 Feb | applies |
| LP13 | good history, notice 1 Feb 2027, further date 15 Mar 2027, paid 28 Feb 2027 | does not apply ("before the date that is the earlier of the further date and ... 1 month after the date of the notice" = 1 Mar) |
| LP14 | as LP13 but paid 1 Mar 2027 | applies (not paid *before* 1 Mar) |
| LP15 | not provisional, Commissioner determines a late payment in prior 2 years | applies (s 139B(1)(b)) |
| LP16 | provisional tax, good history, no notice | applies (s 139B(1)(a)) |

## Goal 4: shortfall penalties

Readings:
- Rates: 141A 20%, 141B 20%, 141C 40%, 141D 100% (20% where s 141D(3A)-type conditions met), 141E 150%.
- s 141FB: a *clean* taxpayer (no disqualifying offence or penalty) has the penalty reduced "to 50%". So "disqualified" below means the 141FB reduction is NOT available.
- Reductions are combined multiplicatively (each applies to the amount left after the others); the Act does not say how 141FB, 141G/141H/141I and 141K combine, and multiplication makes order irrelevant. Where s 141J applies (VD + temporary shortfall), its single reduction (100% or 75%) replaces both the 141G/141H reduction and the 141I reduction.
- s 141JAA cap is applied last, to the amount finally payable ("may not be more than $50,000"), and only for 141A / 141B penalties, not if 141K applies.
- Cap date: later of (a) due date + 3 months and (b) due date + lesser of 1 return period and 6 months. Annual income tax return -> due date + 6 months; monthly return -> + 3 months; two-monthly -> + 3 months; six-monthly -> + 6 months.

Base shortfall $10,000 unless stated.

| id | inputs | expected penalty | provision |
|---|---|---|---|
| SP1 | not reasonable care, disqualified | $2,000 | s 141A(2) "20%" |
| SP2 | not reasonable care, clean | $1,000 | s 141FB(2) "reduced, to 50%" |
| SP3 | UTP, shortfall $10,000 | none ($0) | s 141B(2) "more than both— $50,000" |
| SP4 | UTP, shortfall $60,000, total tax figure $1,000,000, disqualified | $12,000 | s 141B(2), (3) |
| SP5 | as SP4, clean | $6,000 | s 141FB(2) |
| SP6 | UTP, shortfall $50,000, total tax figure $1,000,000 | none | not "more than" $50,000 |
| SP7 | UTP, shortfall $60,000, total tax figure $6,000,000 (1% = $60,000) | none | not more than 1% |
| SP8 | UTP, shortfall $60,000, total tax figure $5,999,900, disqualified | $12,000 | more than both |
| SP9 | gross carelessness, disqualified | $4,000 | s 141C(2) "40%" |
| SP10 | gross carelessness, clean | $2,000 | s 141FB(2) |
| SP11 | abusive, disqualified | $10,000 | s 141D(3) "100%" |
| SP12 | abusive, clean | $5,000 | s 141FB(2) |
| SP13 | abusive, 141EB arrangement, associated shortfalls < $50,000, independent advice, disqualified | $2,000 | s 141D "reduced to 20%" |
| SP14 | evasion, disqualified | $15,000 | s 141E "150%" |
| SP15 | evasion, clean | $7,500 | s 141FB(1) |
| SP16 | RC, disqualified, pre-notification VD | $0 | s 141G(3)(a)(i) "100%" |
| SP17 | UTP (SP4 figures), disqualified, pre-notification VD | $0 | 100% |
| SP18 | GC, disqualified, pre-notification VD | $1,000 | s 141G(3)(a)(ii) "75%" |
| SP19 | evasion, disqualified, pre-notification VD | $3,750 | 75% |
| SP20 | RC, disqualified, post-notification VD | $1,200 | s 141G(3)(b) "40%" |
| SP21 | GC, disqualified, post-notification VD | $2,400 | 40% |
| SP22 | evasion, disqualified, post-notification VD | $9,000 | 40% |
| SP23 | UTP (SP4 figures), disqualified, adequate disclosure | $3,000 | s 141H "75%" |
| SP24 | abusive, disqualified, adequate disclosure | $2,500 | s 141H |
| SP25 | GC, disqualified, adequate disclosure | $4,000 | s 141H only for 141B/141D |
| SP26 | RC, disqualified, whole shortfall temporary | $500 | s 141I(2) "75%" |
| SP27 | GC, disqualified, temporary | $1,000 | s 141I |
| SP28 | RC, disqualified, temporary + pre-notification VD | $0 | s 141J(2)(a) "100%" |
| SP29 | GC, disqualified, temporary + pre-notification VD | $1,000 | s 141J(2)(b) "75%" (not 93.75%) |
| SP30 | RC, disqualified, temporary + post-notification VD | $500 | s 141J(2)(b) 75% (not 40% and 75% stacked = $300) |
| SP31 | evasion, disqualified, temporary + post-notification VD | $3,750 | s 141J(2)(b) |
| SP32 | GC, disqualified, obstruction | $5,000 | s 141K(2) "25%" |
| SP33 | evasion, clean, obstruction | $9,375 | 15,000 x 1.25 x 0.5 (multiplicative reading) |
| SP34 | GC, clean, post-notification VD | $1,200 | 4,000 x 0.5 x 0.6 (multiplicative reading) |
| SP35 | RC, shortfall $500,000, disqualified, no disclosure, Commissioner determines 1 Dec 2027; annual return due 7 Jul 2027 | $50,000 (capped from $100,000) | s 141JAA |
| SP36 | as SP35, Commissioner determines 7 Jan 2028 | $50,000 | due date + 6 months, "no later than" |
| SP37 | as SP35, Commissioner determines 8 Jan 2028 | $100,000 | after cap date |
| SP38 | RC $500,000, disqualified, post-notification VD 1 Dec 2027 | $50,000 (60,000 capped) | s 141JAA "Despite section 141J" |
| SP39 | RC $500,000, disqualified, post-notification VD 8 Jan 2028 | $60,000 | no cap |
| SP40 | RC $500,000, disqualified, obstruction, determined 1 Dec 2027 | $125,000 | s 141JAA(2) "does not apply if section 141K applies" |
| SP41 | GC $500,000, disqualified, determined 1 Dec 2027 | $200,000 | cap only for 141A/141B |
| SP42 | UTP shortfall $300,000, total tax figure $1,000,000, disqualified, determined 1 Dec 2027 (annual return due 7 Jul 2027) | $50,000 (capped from $60,000) | s 141JAA |
| SP43 | RC $500,000, disqualified, monthly return due 20 Feb 2027, determined 20 May 2027 / 21 May 2027 | $50,000 / $100,000 | later of 3 months and 1 period |
| SP44 | RC $500,000, disqualified, two-monthly return due 28 Feb 2027, determined 28 May 2027 / 29 May 2027 | $50,000 / $100,000 | lesser of 2 months and 6 = 2; later of 3 and 2 = 3 months |

### Previous behaviour detail (s 141FB(3)-(4))

| id | inputs | expected | provision |
|---|---|---|---|
| PB1 | current RC income tax penalty; prior RC income tax penalty (not VD-reduced) on a position 3 years earlier | disqualified: $2,000 | 4-year period, "a shortfall penalty of any sort" |
| PB2 | current RC GST penalty; prior RC GST penalty 3 years earlier | not disqualified: $1,000 | 2-year period for GST |
| PB3 | current GC penalty; prior RC penalty (same tax, 1 year earlier) | not disqualified: $2,000 | for GC only evasion/GC/abusive priors count |
| PB4 | current RC penalty; prior penalty reduced for voluntary disclosure | not disqualified: $1,000 | "is not reduced for voluntary disclosure" |
| PB5 | current evasion penalty; prior evasion penalty same tax 10 years earlier (after 26 Mar 2003) | disqualified: $15,000 | s 141FB(3)(b)(i) has no look-back window |
| PB6 | current evasion; prior GC penalty 1 year earlier | not disqualified: $7,500 | only evasion counts under (1) |

### Reasonable care via adviser (s 141A(3))

| id | inputs | expected |
|---|---|---|
| RA1 | relied on adviser, gave adequate info and instructions, no reason to doubt, not employer | took reasonable care: no 141A penalty |
| RA2 | relied on adviser who is the taxpayer's employee | no protection: 141A penalty applies |

## Not expressible / not tested as input-output

- s 23D(3)-(4) (early delivery, Commissioner's approval of other means): discretionary, no computable output.
- s 23G exemption grant and its 6-month expiry after a cancellation notice: Commissioner's judgement; only "has exemption" is an input.
- s 37(3)-(4): whether the Commissioner grants an extension is discretionary; only the s 37(5) ceiling is computable.
- s 139B(3)(b) and (5A)/(5B)-style exceptions for s 157 deductions, and s 139BA financial relief: out of scope of the brief.
- Whether a query on default + 7 includes the 4% (end-of-day timing) — deliberately not asserted.
- Rows above may be marked "not expressible" after the encoding is opened if it has no corresponding input; expected values above are not changed.

## Added after opening the encoding (no expected value above changed)

Marked **not expressible** (the encoding has no input or function for them):

- EG8 (PAYE intermediary: no input on `Employer`).
- CE5 (intention that the cessation be permanent: no input).
- NN8 (0.45 rate: stated in a comment and @export text only; no function computes the tax).
- TB4 (asked on a date: s 108 function returns the last day, not a yes/no; TB1 covers the same edge).
- LF9 ($250 monthly maximum for EII), LF10 (12-month on-time warning, s 139A(6)-(8)), LF11 (30-day prior notice, s 139A(5)): no inputs. LF12 reduces to LF8.
- SP7, SP8 (1% of total tax figure limb of s 141B(2)): no total-tax-figure input.
- PB1-PB6 (s 141FB disqualification details): only a boolean `no disqualifying offence or penalty`.
- RA1, RA2 (s 141A(3) reliance on an adviser): culpability is an input.
- TM7 is tested via a paper employer without the twice-monthly choice.
