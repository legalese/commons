# Independent expectations: CCCFA 2003 (ss 18, 27-29, 39, 40, 45C, 45E-45I, 55-57A, 88-89)

Written from BRIEF.md and the Act's text (as at 1 July 2026) **before** any `.l4` file was opened.
Expected values here are not to be changed after the encoding is opened.

## Calendar used (s 5 "working day")

s 5: a working day is "a day of the week other than a Saturday, a Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, ... Matariki Observance Day, and Labour Day; ... if Waitangi Day or Anzac Day falls on a Saturday or a Sunday, the following Monday; ... a day in the period commencing with 25 December in a year and ending with 2 January in the following year; ... if 1 January falls on a Friday, the following Monday".

Non-working weekdays used:
- 2026: Fri 6 Feb (Waitangi), Fri 3 Apr (Good Friday), Mon 6 Apr (Easter Monday), Mon 27 Apr (Anzac Day 25 Apr is a Saturday), Mon 1 Jun (King's Birthday), Fri 10 Jul (Matariki), Mon 26 Oct (Labour Day), 25 Dec 2026 - 2 Jan 2027.
- 2027: Mon 4 Jan (1 Jan 2027 is a Friday), Mon 8 Feb (Waitangi 6 Feb is a Saturday), Fri 26 Mar / Mon 29 Mar (Easter Sunday 28 Mar), Mon 26 Apr (Anzac on Sunday), Mon 7 Jun, Fri 25 Jun (Matariki), Mon 25 Oct (Labour Day).

Counting convention: "within N working days of [after] the day X" excludes day X and ends at the close of the Nth working day after X (Legislation Act 2019 s 54, item 3 example: "within 10 days of adopting ... adopted on 1 August ... by the close of 11 August"). Months: Legislation Act s 56 ("the period ends immediately before the corresponding day in the ending month or (if there is no such day) at the close of the last day of the ending month").

## Goal 1: Cancellation and disclosure (ss 18, 27, 29)

s 27(1): debtor may cancel "by giving written notice ... within 5 working days of the day that disclosure is made under section 17 (or at any time if that disclosure has not been made) and either, (a) in the case of a contract referred to in subsection (2), paying the cash price ... within 15 working days of the day the notice is given; or (b) in any other case, returning to the creditor any advance and any other property ... within 5 working days of the day that disclosure is made ... (or at any time if that disclosure has not been made)."
Reading: a cancellation is effective only if the notice is in time AND the payment/return is in time. A notice given on the disclosure day itself is in time.

### Notice deadline (5 working days)
| id | disclosure | notice | expected |
|---|---|---|---|
| C01 | Mon 2 Mar 2026 | Mon 9 Mar 2026 | in time (deadline 9 Mar) |
| C02 | Mon 2 Mar 2026 | Tue 10 Mar 2026 | late |
| C03 | Tue 31 Mar 2026 | Thu 9 Apr 2026 | in time (Good Friday, Easter Monday skipped) |
| C04 | Tue 31 Mar 2026 | Fri 10 Apr 2026 | late |
| C05 | Tue 21 Apr 2026 | Wed 29 Apr 2026 | in time (Mon 27 Apr Anzac Mondayised) |
| C06 | Tue 21 Apr 2026 | Thu 30 Apr 2026 | late |
| C07 | Thu 22 Oct 2026 | Fri 30 Oct 2026 | in time (Labour Day 26 Oct) |
| C08 | Thu 22 Oct 2026 | Mon 2 Nov 2026 | late |
| C09 | Mon 6 Jul 2026 | Tue 14 Jul 2026 | in time (Matariki 10 Jul) |
| C10 | Mon 6 Jul 2026 | Wed 15 Jul 2026 | late |
| C11 | Mon 21 Dec 2026 | Wed 6 Jan 2027 | in time (25 Dec-2 Jan and Mon 4 Jan skipped) |
| C12 | Mon 21 Dec 2026 | Thu 7 Jan 2027 | late |
| C13 | Thu 24 Dec 2026 | Mon 11 Jan 2027 | in time |
| C14 | Fri 30 Jan 2026 | Mon 9 Feb 2026 | in time (Waitangi 6 Feb) |
| C15 | Tue 26 May 2026 | Wed 3 Jun 2026 | in time (King's Birthday 1 Jun) |
| C16 | Tue 26 May 2026 | Thu 4 Jun 2026 | late |
| C17 | Wed 3 Feb 2027 | Thu 11 Feb 2027 | in time (Mon 8 Feb Waitangi Mondayised) |
| C18 | Mon 21 Jun 2027 | Tue 29 Jun 2027 | in time (Matariki 25 Jun 2027) |
| C19 | Mon 21 Jun 2027 | Wed 30 Jun 2027 | late |
| C20 | none made | 1 Mar 2027 (a year after contract) | in time ("at any time if that disclosure has not been made") |
| C21 | Mon 2 Mar 2026 | Mon 2 Mar 2026 (same day) | in time |
| C22 | Mon 2 Mar 2026 (deadline function) | - | last day for notice = 9 Mar 2026 |
| C23 | Mon 21 Dec 2026 (deadline function) | - | last day for notice = 6 Jan 2027 |

### s 27(1)(b) - return of advance (any other case)
| id | facts | expected |
|---|---|---|
| C24 | cash loan; disclosure 2 Mar 2026; notice 5 Mar; advance returned 9 Mar | cancellation effective |
| C25 | same, advance returned 10 Mar 2026 | not effective (return late: measured from disclosure, not notice) |
| C26 | cash loan; no disclosure; notice and return 1 Mar 2027 | effective |

### s 27(1)(a) / (2) - payment of cash price within 15 working days of the notice
s 27(2): "(a) a credit sale of goods if the debtor has taken possession of the goods and disclosure of the information referred to in paragraph (s) of Schedule 1 has been made: (b) a credit sale involving a sale of property by auction: (c) a credit sale of property that the debtor wants to keep or of services the debtor wants to obtain: (d) a credit sale of services that have been performed."
| id | facts | expected |
|---|---|---|
| C27 | goods possessed + Sch 1(s) disclosed; disclosure Wed 14 Oct 2026; notice Mon 19 Oct; cash price paid Tue 10 Nov 2026 | effective (19 Oct + 15 WD = 10 Nov, Labour Day skipped) |
| C28 | same, paid Wed 11 Nov 2026 | not effective |
| C29 | auction sale; disclosure Wed 9 Dec 2026; notice Mon 14 Dec 2026; paid Wed 13 Jan 2027 | effective (14 Dec + 15 WD = 13 Jan 2027) |
| C30 | auction sale, same, paid Thu 14 Jan 2027 | not effective |
| C31 | property the debtor wants to keep; disclosure Wed 10 Jun 2026; notice Mon 15 Jun 2026; paid Mon 6 Jul 2026 | effective (15 Jun + 15 WD = 6 Jul) |
| C32 | services performed; disclosure 10 Jun 2026, notice 15 Jun, paid Tue 7 Jul 2026 | not effective |
| C33 | credit sale of goods, possession taken but Sch 1(s) info NOT disclosed: not a s 27(2) contract, so (b) applies; disclosure 2 Mar 2026, notice 5 Mar, goods returned 9 Mar | effective under (b) |
| C34 | as C33 but goods returned 20 Mar 2026 (would be within 15 WD of notice) | not effective (it is (b), 5 WD of disclosure) |
| C35 | 15 WD deadline function: notice 19 Oct 2026 | 10 Nov 2026 |

### s 29 exceptions
s 29(1): "Section 27 does not apply if the credit is provided for a specified period of less than 2 months and no part of the credit is used, with the knowledge of the creditor, to pay amounts owing to the creditor or a related company under another credit contract." (3) "does not apply to a layby sale agreement." (2) "does not entitle a debtor to cancel ... on the ground that disclosure has not been made to a guarantor."
| id | facts | expected |
|---|---|---|
| C36 | specified period 1 month, no refinancing; notice in time | no right to cancel |
| C37 | specified period exactly 2 months (60 days? stated as 2 months) | right applies (not "less than 2 months") |
| C38 | no specified period (open-ended) | right applies |
| C39 | period 1 month, credit used with creditor's knowledge to pay creditor's other contract | right applies |
| C40 | period 1 month, used to pay a related company's contract, with knowledge | right applies |
| C41 | period 1 month, used to pay creditor's contract, creditor did NOT know | no right |
| C42 | layby sale agreement | no right |
| C43 | debtor disclosed to 2 Mar 2026, guarantor not; notice relying on guarantor non-disclosure on 1 Jun 2026 | no right (late; guarantor ground does not give "at any time") |

### s 18(2) continuing disclosure maximum period
"(a) in the case of a revolving credit contract, 45 working days; or (b) in any other case, 6 months."
Ambiguity: how a 45-working-day statement period is counted. Reading taken: the number of working days in the statement period from its opening date to its closing date, both included, must not exceed 45 (s 19(1)(a) treats both opening and closing dates as within "the period covered by the statement"; Legislation Act s 54: a period beginning on a day includes that day).
| id | facts | expected |
|---|---|---|
| D01 | revolving; 1 Jul 2026 - 31 Aug 2026 | within (44 WD or fewer) |
| D02 | revolving; 1 Jul 2026 - Wed 2 Sep 2026 | within (exactly 45 WD inclusive) |
| D03 | revolving; 1 Jul 2026 - Thu 3 Sep 2026 | exceeds (46 WD inclusive) - boundary depends on counting reading |
| D04 | revolving; 1 Jul 2026 - 30 Sep 2026 | exceeds |
| D05 | revolving; 1 Dec 2026 - Thu 11 Feb 2027 | within (45 WD; Christmas period, 4 Jan, 8 Feb skipped) |
| D06 | revolving; 1 Dec 2026 - Fri 12 Feb 2027 | exceeds (46) |
| D07 | non-revolving; 1 Jan 2026 - 30 Jun 2026 | within (6 months) |
| D08 | non-revolving; 1 Jan 2026 - 1 Jul 2026 | exceeds |
| D09 | non-revolving; 31 Aug 2026 - 28 Feb 2027 | within (no 31 Feb: period ends at close of last day of Feb) |
| D10 | non-revolving; 31 Aug 2026 - 1 Mar 2027 | exceeds |
| D11 | non-revolving; 1 Jul 2026 - 30 Sep 2026 (3 months, 66 WD) | within (6 months limb, not 45 WD) |
| D12 | revolving with no credit limit specified, 1 Jul - 31 Aug 2026 | within; still revolving ("whether or not the contract specifies a credit limit") |

## Goal 2: Interest and high-cost credit

### s 39 interest limits
s 5: "daily interest rate means the rate determined by dividing the annual interest rate by 365". s 39(1)(a): "applying the daily interest rate to the unpaid daily balances"; (b) "the sum of each of the amounts determined by applying each daily interest rate to that part of the unpaid daily balances that it applies to". (2): "for a week, a fortnight, a month, a quarter of a year, or a half of a year ... divided by 52 ..., 26 ..., 12 ..., 4 ..., 2 ... to ... the average unpaid daily balances".
| id | facts | expected maximum interest |
|---|---|---|
| I01 | 10% pa; daily balances $3,650 each day for 30 days | $30.00 |
| I02 | 18.25% pa; $2,000 for 10 days | $10.00 |
| I03 | 10% pa; balances 3,650 / 7,300 / 0 on 3 days | $3.00 |
| I04 | two rates: 10% on $3,650 and 20% on $1,825, 1 day | $2.00 |
| I05 | monthly: 12% pa, average unpaid daily balance $1,000 | $10.00 |
| I06 | weekly: 52% pa, average $500 | $5.00 |
| I07 | fortnightly: 26% pa, average $1,000 | $10.00 |
| I08 | quarterly: 8% pa, average $5,000 | $100.00 |
| I09 | half-yearly: 6% pa, average $10,000 | $300.00 |
| I10 | charge of $30.01 against I01 | exceeds the limit; $30.00 does not |

### s 40 default interest
s 40(1) "must not provide that an annual interest rate ... will differ according to whether the debtor has breached the contract." (2) "may provide for a differential rate if the higher rate is imposed only (a) in the event of a default in payment, in respect of the amount of the default, and while the default continues; or (b) ... credit limit ... exceeded and while the credit limit is exceeded." (2A)/(2B): the higher rate may not be imposed on an amount that becomes payable earlier because of default, unless the contract is an on demand facility. (3): on demand facility = "total unpaid balance is repayable at any time on demand by the creditor; and there is no agreement, arrangement, or understanding ... that repayment will only be demanded on the occurrence or non-occurrence of a particular event."
| id | facts | expected |
|---|---|---|
| R01 | higher rate on the $500 in default, only while default continues | permitted |
| R02 | higher rate on the whole $10,000 balance on a $500 default | not permitted |
| R03 | higher rate on the $600 excess over a $5,000 limit (balance $5,600) while exceeded | permitted |
| R04 | higher rate keeps running after default remedied | not permitted |
| R05 | higher rate triggered by a non-payment breach (e.g. failing to insure) | not permitted |
| R06 | default $500; contract accelerates whole $10,000; not on-demand; base for higher rate | $500 (accelerated $9,500 excluded) |
| R07 | same, but on demand facility (repayable on demand, no understanding) | base may be $10,000 (whole called-up amount in default) |
| R08 | repayable on demand but understanding that demand only on a particular event | not on-demand -> base $500 |
| R09 | over-limit base: limit $5,000, balance $5,600, no payment default | $600 |
| R10 | payment default $200 and over-limit excess $300 at same time | base $500 (both limbs) - reading: each limb authorises the rate on its own part |

### s 45C high-cost
"(a) ... annual interest rate of 50% or greater: (b) ... weighted average annual interest rate ... is, or is likely to be, 50% or greater on any day ...: (c) ... the total rate of the interest charges (including default interest charges) that may be applied cumulatively to the same part of an unpaid balance in the event of a default ... is, or is likely to be, a rate of 50% or greater: ... (d) a contract of a class declared by the FMA".
| id | facts | expected |
|---|---|---|
| H01 | annual rate 50% | high-cost |
| H02 | annual rate 49.99%, nothing else | not high-cost |
| H03 | annual rate 30%, weighted average 50% on some day | high-cost |
| H04 | weighted average 49.9% only | not high-cost |
| H05 | Act's example: 40% + 20% default = 60% | high-cost |
| H06 | 40% + 9.99% default = 49.99% | not high-cost |
| H07 | 30% + 20% default = exactly 50% | high-cost |
| H08 | FMA-declared class, 10% | high-cost |
| H09 | annual rate 500% (s 45E example) | high-cost |

### s 45E costs of borrowing cap
"The maximum costs of borrowing ... under a high-cost consumer credit contract and all related consumer credit contracts is an amount equal to the first advance." First advance excludes "credit fees, charges for optional services, and fees or charges passed on by the creditor".
| id | facts | expected |
|---|---|---|
| E01 | first advance $100, costs of borrowing $100 | within cap |
| E02 | first advance $100, costs $101 | exceeds |
| E03 | Act's example: first advance $100, $32 already charged on first contract; remaining cap for refinance | $68 |
| E04 | Act's example: Ms D pays $120 in costs under the new contract | refund/credit $52 (s 48) |
| E05 | advance $500 of which $50 is a credit fee capitalised | first advance $450 -> cap $450 |
| E06 | costs = interest 60 + credit fee 20 + default fee 15 + optional service 5 + passed-on 10 = 110 against advance 100 | exceeds (all five count) |
| E07 | series: first contract advance $200; costs on earlier contracts $150; new contract costs $60 | exceeds (210 > 200) |

### s 45F other creditors (15 days)
"(a) a debtor who has an unpaid balance on any high-cost consumer credit contract under which the creditor is a person other than C; or (b) a person who has had, at any time within the preceding 15 days, an unpaid balance ...". Reading: the preceding 15 days of a contract entered on day Y are Y-15 .. Y-1; a balance outstanding at any time on a day counts for that day.
| id | facts | expected |
|---|---|---|
| F01 | new contract 20 Nov 2026; current balance with other creditor | prohibited |
| F02 | new contract 20 Nov 2026; other creditor's balance last outstanding 5 Nov 2026 | prohibited (5 Nov is within the preceding 15 days) |
| F03 | new contract 20 Nov 2026; balance last outstanding 4 Nov 2026 | permitted |
| F04 | new contract 20 Nov 2026; current balance only with C itself | permitted under 45F |
| F05 | F01 + C made s 9C inquiries AND had reasonable grounds to believe no balance | defence available |
| F06 | F01 + inquiries made but no reasonable grounds | no defence |
| F07 | F01 + reasonable grounds but no compliant inquiries | no defence |
| F08 | other creditor's contract not high-cost | permitted |

### s 45G repeat debtors (90 days)
"... a debtor who has entered into 2 or more high-cost consumer credit contracts at any time within the preceding 90 days." Preceding 90 days of 1 Oct 2026 = 3 Jul .. 30 Sep 2026. Counts contracts with any creditor, including C.
| id | facts | expected |
|---|---|---|
| G01 | new 1 Oct 2026; prior HCCCs 3 Jul 2026 and 1 Sep 2026 | prohibited |
| G02 | new 1 Oct 2026; prior 2 Jul 2026 and 1 Sep 2026 | permitted (only 1 within) |
| G03 | new 1 Oct 2026; one prior 1 Sep 2026 | permitted |
| G04 | new 1 Oct 2026; prior 1 Aug, 1 Sep, 15 Sep (all with C) | prohibited |
| G05 | G01 + inquiries + reasonable grounds | defence |
| G06 | G01 + reasonable grounds only | no defence |

### s 45H rate cap 0.8% a day
| id | facts | expected |
|---|---|---|
| P01 | credit provided $1,000; charge $8.00 in a day | within |
| P02 | $1,000; $8.01 in a day | exceeds |
| P03 | $1,000; $240 over 30 days | within (8/day) |
| P04 | $1,000; $241 over 30 days | exceeds |
| P05 | P02 but excess only because of a part prepayment | no contravention (s 45H(6)) |
| P06 | default fees excluded from "charge": $8 interest + $20 default fee in a day on $1,000 | within |

### s 45I compound interest
| id | facts | expected |
|---|---|---|
| Q01 | high-cost contract provides for compound interest | prohibited |
| Q02 | high-cost, interest on additional credit provided to repay accrued interest | prohibited (compound interest "includes" it) |
| Q03 | high-cost, simple interest | permitted |
| Q04 | not high-cost, compound interest | s 45I does not apply (permitted under 45I) |

## Goal 3: Hardship (ss 55, 57, 57A)

### s 55(3) further applications
"not entitled to make another application ... unless (a) the application is made not less than 4 months after the previous application is made; or (b) ... less than 4 months ..., (i) the creditor agrees to consider the application; or (ii) the reasons ... are materially different".
Ambiguity: the exact boundary of "4 months after". Reading taken (Legislation Act ss 54, 56, example 3): a period of 4 months after 10 Feb starts 11 Feb and ends at the close of 10 June, so the earliest date that is "not less than 4 months after" is 11 June.
| id | facts | expected |
|---|---|---|
| A01 | first application (no previous) | may apply |
| A02 | previous 10 Feb 2026; new 1 Jul 2026 | may apply |
| A03 | previous 10 Feb 2026; new 1 May 2026; no agreement, same reasons | may not apply |
| A04 | A03 + creditor agrees to consider | may apply |
| A05 | A03 + materially different reasons | may apply |
| A06 | previous 10 Feb 2026; new 11 Jun 2026 | may apply |
| A07 | previous 10 Feb 2026; new 9 Jun 2026 | may not apply |
| A08 | previous 10 Feb 2026; new 10 Jun 2026 | may not apply (my reading; boundary ambiguous) |
| A09 | previous 31 Oct 2026; new 1 Mar 2027 | may apply |
| A10 | previous 31 Oct 2026; new 27 Feb 2027 | may not apply |

### s 57 bars
"(a) the debtor is in default ... and ... (i) has been in default for 2 weeks or more after receiving a repossession warning notice ... or a notice under section 119 of the Property Law Act 2007; or (ii) has failed to make 4 or more consecutive periodic payments ...; or (iii) has been in default for 2 months or more; or (b) it was reasonably foreseeable ...". (2) "(1)(a) does not prevent an application being made after the debtor has remedied the default".
| id | facts | expected |
|---|---|---|
| B01 | no default, not foreseeable | not barred |
| B02 | default 14 days after repossession warning notice | barred |
| B03 | default 13 days after repossession warning notice | not barred |
| B04 | default 14 days after s 119 PLA notice | barred |
| B05 | 4 consecutive periodic payments missed | barred |
| B06 | 3 consecutive missed | not barred |
| B07 | in default since 1 Mar 2026, application 1 May 2026 (2 months) | barred |
| B08 | in default since 1 Mar 2026, application 29 Apr 2026 | not barred |
| B09 | B05 but default remedied before application | not barred |
| B10 | cause reasonably foreseeable at contract | barred (remedy irrelevant) |
| B11 | B10 with default remedied | still barred |

### s 57A creditor deadlines
"(a) within 5 working days after receiving the application, acknowledge ...: (b) within 10 working days ..., request any further information ...: (c) within 20 working days ..., decide ...". (2) "if the creditor has requested further information in accordance with subsection (1)(b), the time ... is the later of (a) 10 working days after receiving the further information; and (b) 20 working days after making the request".
| id | facts | expected |
|---|---|---|
| K01 | received Mon 2 Nov 2026 | acknowledge by Mon 9 Nov 2026 |
| K02 | received 2 Nov 2026 | request info by Mon 16 Nov 2026 |
| K03 | received 2 Nov 2026, no request | decide by Mon 30 Nov 2026 |
| K04 | received Tue 1 Dec 2026 | acknowledge by Tue 8 Dec 2026 |
| K05 | received 1 Dec 2026 | request by Tue 15 Dec 2026 |
| K06 | received 1 Dec 2026, no request | decide by Thu 7 Jan 2027 |
| K07 | received Mon 22 Jun 2026; request Fri 3 Jul 2026 (in time: deadline 6 Jul); info Tue 14 Jul 2026 | decide by Mon 3 Aug 2026 (later of 28 Jul and 3 Aug) |
| K08 | as K07, info Fri 31 Jul 2026 | decide by Fri 14 Aug 2026 (later of 14 Aug and 3 Aug) |
| K09 | received 22 Jun 2026, no request | decide by Tue 21 Jul 2026 |
| K10 | received 22 Jun 2026; request made Tue 7 Jul 2026 (after the 10 WD of (1)(b)) | no extension - decide by 21 Jul 2026 (reading: s 57A(2) applies only to a request "in accordance with subsection (1)(b)") |
| K11 | received 22 Jun 2026 | acknowledge by Mon 29 Jun 2026 |

## Goal 4: Statutory damages (ss 88, 89)

Labels (per BRIEF): (1)(a) 9C(3)(a); 9C(4)(a); 9C(5)(a); 45F/45G; s 18; s 24; s 25(1)(a); (1)(d) "any other breach, the lesser of $6,000 or 5% of ...". s 89(3): "If the amount ... under subsection (1)(d) is less than $200, ... rounded up to $200." s 89(2): "Subject to subsection (1)(a) and (b), if a revolving credit contract does not have a credit limit, the amount ... is $6,000." s 89(4): "breached 2 or more provisions ... and the breaches occur at or about the same time, the total ... is equal to the highest".
| id | facts | expected |
|---|---|---|
| S01 | 9C(3)(a) breach; interest+credit fees+default fees payable $1,234 | $1,234 |
| S02 | 9C(3)(a); $150 | $150 (no $200 minimum outside the general limb) |
| S03 | 9C(4)(a); guarantor paid $5,000 | $5,000 |
| S04 | 9C(5)(a); borrower paid $300 under insurance contract | $300 |
| S05 | 45F breach; interest+fees under that contract $450 | $450 |
| S06 | 45G breach; $90 | $90 |
| S07 | s 18 breach; interest+fees during period of breach $210 | $210 |
| S08 | s 18 breach; $50 | $50 |
| S09 | s 24 breach; interest+fees from request to earlier of disclosure / end $75 | $75 |
| S10 | s 25(1)(a); advances under guaranteed contracts $50,000 | $2,500 |
| S11 | s 25(1)(a); $200,000 | $6,000 |
| S12 | other breach (e.g. s 17), non-revolving, advances $10,000 | $500 |
| S13 | other breach, advances $120,000 | $6,000 (exactly 5% = 6,000) |
| S14 | other breach, advances $200,000 | $6,000 |
| S15 | other breach, advances $3,000 (5% = $150) | $200 |
| S16 | other breach, advances $4,000 | $200 |
| S17 | other breach, advances $4,020 | $201 |
| S18 | other breach, revolving, credit limit $10,000 at breach | $500 |
| S19 | other breach, revolving, limit $2,000 | $200 |
| S20 | other breach, revolving, no credit limit | $6,000 |
| S21 | s 18 breach on revolving with no credit limit, $210 | $210 ("Subject to subsection (1)(a) and (b)") |
| S22 | other breach, consumer lease, cash price $20,000 | $1,000 |
| S23 | other breach, buy-back, rateable value $500,000 | $6,000 |
| S24 | other breach (45H), high-cost advances $1,000 | $200 |
| S25 | simultaneous: s 18 ($300) and other breach on $10,000 ($500) | $500 |
| S26 | simultaneous: 9C(3)(a) $1,234 and other breach $200 | $1,234 |
| S27 | same two breaches NOT at about the same time | $800 for S25's pair (each payable separately) - may not be expressible |
| S28 | breach of s 41 (not in s 88(1) list) | no statutory damages - may not be expressible |
| S29 | breach of s 27 / s 57A (not listed) | none - may not be expressible |

Ambiguities noted: s 89(2) for limbs other than (a)/(b) (e.g. s 24 or 45F breach on a revolving contract with no limit): literal text gives $6,000; purposive reading confines (2) to the general limb. Not tested. The s 45F "preceding 15 days" and 45G "preceding 90 days" day-counting and the s 55(3) 4-month boundary are readings stated above. s 45H "calculated in accordance with the regulations": the regulations are not in scope, so the per-day test is a simplification.

Not expressible as input/output (anticipated): whether a notice "shows the intention of the debtor to cancel" (s 28); "reasonably foreseeable" (s 57(1)(b)) and "materially different" (s 55(3)(b)(ii)) are judgements, so only as boolean inputs; the weighted average annual interest rate (regulations).

## Added after opening the encoding: scenarios not expressible (no expected value above was changed)

- R01-R05 (s 40(1)-(2): whether a contract term is permitted): the encoding only computes the base amount on which default interest may run; no function decides whether a term is permitted.
- E05 (first advance excludes credit fees etc.): `first advance` is an input. E04's refund is computed in the test from the encoding's remaining cap.
- F06, F07 (s 45F(2)/45G(2) limbs separately): the defence is one boolean input, so only "defence FALSE" is testable.
- C37-C41 (s 29(1) limbs): collapsed into one input `credit for less than 2 months, not refinancing the creditor`; tested only as that flag TRUE/FALSE. C43 (s 29(2) guarantor ground) is tested only as notice timing.
- Q02 (interest on credit provided to repay accrued interest): collapsed into `provides for compound interest`.
- P05 (s 45H(6) prepayment), P06 (default fees excluded from "charge"): no input; the s 45H function only returns 0.8% x credit x days.
- B04 (s 119 Property Law Act notice): the only input is `days in default after a repossession warning notice`; tested through it.
- S27 (non-simultaneous breaches summed), S28/S29 (breach of an unlisted provision such as s 41, s 27 or s 57A gives no statutory damages): no function or breach kind for these.
