# Scenario: cradle to grave — Ng Jun Hao (Sim Two, the black sheep)

Simone's younger brother, born 2006, dead at 72 in 2079. His life runs beside hers and off the standard path: a shoplifting charge at fifteen, a vape at sixteen, a late return from leave, the platform years on a power-assisted bicycle, a child born before the wedding, a security job with unpaid overtime, a loan shark at the door, a debt repayment scheme, a separation and a divorce, a flat of his own at thirty-eight, the casino, a fall on a stairwell, retrenchment, a stroke at fifty-six, Silver Support at sixty-five, and an estate small enough for the Public Trustee. Nothing in it is villainous. The law in this life is as often a net as a wall, and the point of the scenario is to show both.

It is the second cradle-to-grave scenario. The first, [`../cradle-to-grave-simone/`](../cradle-to-grave-simone/), is the sunny day; this one touches the rows that life never reaches: the Penal Code and the Youth Court, probation and spent records, the Singapore Armed Forces Act, the Platform Workers Act, the moneylenders, the Debt Repayment Scheme, the Employment Claims Tribunal, maintenance and divorce, the casino exclusion order, work injury twice, retrenchment, Medifund, CareShield Life, and Silver Support said yes. A third character, an overachiever who enters a profession and starts a business, will take the professions, companies, employers and intellectual property, so none of that is here.

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — twenty beats, two a chapter, with ages, as the spine for a second film or the second half of the first.
- [`GAPS.md`](GAPS.md) — what this life needs that the library does not yet hold, and the seams with Simone's scenario.
- [`facts.json`](facts.json) — the cast and 78 dated events, each tagged with its law and status, ages at every event, and the twenty beats flagged.
- [`check-status.py`](check-status.py) — re-derives the status column from the tree.

## Design rules

The same six as Simone's scenario, with two differences.

1. **Real dates, one "now".** The demo's present is 11 October 2026, when Jun Hao is twenty and five months from the end of full-time national service. Everything before is backstory; everything after is live.
2. **Current law, replayed.** No rule-version axis; the 2006 birth is registered under the 2021 Act and the 2021 theft is tried under today's Penal Code.
3. **Statute first, then what the statute leaves out.** The six status words are those of Simone's scenario: `ENC`, `PART`, `NONE`, `REGS`, `ADMIN-POLICY`, `CASE`. Statuses were read from the tree on 11 October 2026 and agree with it; run `check-status.py` before a demo.
4. **No cross-subject import.** `facts.json` is the single input for a build.
5. **Nature permits the unlawful.** This is the scenario where that rule earns its keep. Jun Hao does unlawful things five times, all small, and the law answers each time with a process rather than a wall: composition, probation, a summary trial, a tribunal, a scheme. He is never imprisoned.
6. **Shared cast, shared facts.** His parents, his sister, and their deaths are Simone's facts, unchanged: the father's will to the mother in 2052, the mother's intestacy in 2060. One event here reaches into her life, the family exclusion order she applies for in 2046; her facts file is silent on it, and `GAPS.md` records the seam.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Ng Jun Hao** | 30 Aug 2006, KK Women's and Children's Hospital | the main character | Singapore citizen by birth. Second child. Dies 18 Apr 2079 without a will. |
| Cheryl Tan Li Ying | 11 Mar 2007 | his partner from 2032, wife 2033 to 2041 | childcare assistant |
| Ng Rui En | 22 Jan 2033 | their daughter | born before the marriage; legitimated by it |
| Simone Ng | 14 Mar 2003 | his sister | her own scenario |
| Ng Boon Keng, Teo Siew Lan | 1970, 1972 | their parents | as in Simone's facts |
| a delivery platform operator | — | he rides for it 2027 to 2034 | a platform worker, not an employee |
| Sentinel Guard Services Pte Ltd | — | his employer 2034 to 2055 | a security agency |
| Clean Harbour Services Pte Ltd | — | his employer 2056 to 2063 | a cleaning business under the Progressive Wage Model |

---

## Chapter 0 — Born (2006)

A second child, registered on day fifteen. The Baby Bonus of 2006 paid a second child more than a first, and opened a Child Development Account; the child-support row refuses to state the 2006 rate, which is the encoding working. Insured from birth.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2006-08-30 | birth at KKH | Citizen by birth? | Constitution Art 121 | `ENC` |
| 2006-09-14 | registered and named on day fifteen | By when, and who may? | Registration of Births and Deaths Act 2021 ss 7, 8, 10 | `ENC` (replayed; the 1937 Act applied) |
| 2006-10 | Baby Bonus for a 2006 second child | What did a second child get? | Child Development Co-Savings Act 2001 Part 2; child-support row | `ENC` for the Scheme; `PART`, the row refuses a Cash Gift rate before 2015 by design |
| 2006-08-30 | insured from birth | — | MediShield Life Scheme Act 2015 s 3 | `ENC` |

## Chapter 1 — Primary school and the letter (2013–2018)

Primary 1 in 2013. In Primary 4 he is absent for thirty-one days, and the Ministry writes to his parents, because under the Compulsory Education Act the duty is the child's to attend and the offence is each parent's. Nothing follows but the letter. PSLE in 2018 and a posting to Normal (Technical).

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2013-01-02 | Primary 1 | Is attendance compulsory? | Compulsory Education Act 2000 ss 2, 3 | `ENC` |
| 2016-05-20 | 31 days absent; the Ministry's letter | Whose duty, whose offence, and what happens first? | CEA s 3(2) (each parent commits an offence), s 4 (exemption), s 5 (the Board) | `ENC` |
| 2016-06 | first passport for a school trip | — | Passports Act 2007 s 27 | `ENC` |
| 2018-10 | PSLE; Normal (Technical) | — | MOE posting groups | `ADMIN-POLICY` |

## Chapter 2 — The mall and the Youth Court (2019–2022)

Secondary school in the Normal (Technical) stream. NRIC at fifteen. In November 2021, with two friends, he walks out of a mall shop with a phone case and earbuds worth eighty-nine dollars and is stopped at the door. Theft, and theft in a building used for the custody of property, which is the shop. He is fifteen: a young person, arrested, released to his parents, and brought before the Youth Court, which makes a probation order for twelve months with community service and records no conviction. He finishes it. N-levels in 2022.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2021-08-30 | turns 15: NRIC | — | National Registration Act 1965 s 6 | `ENC` |
| 2021-11-20 | takes $89 of goods from a shop | What offence; does the shop being a building matter? | Penal Code 1871 ss 378-379 (theft), s 380 (theft in a building used for custody of property) | `ENC`, in both Penal Code rows |
| 2021-11-20 | arrested at 15, released to his parents | Arrestable? Which court tries a young person? | Criminal Procedure Code 2010 First Schedule; Children and Young Persons Act 1993 s 2, Part 3 (the Youth Court) | `ENC` for the Schedule; `PART` for the Youth Court, outside the CYPA row's ss 2, 5-8 |
| 2022-02-14 | probation order, 12 months, community service, no conviction recorded | What does probation do to the conviction; what if he breaches? | Probation of Offenders Act 1951 s 5, s 7, s 11 | `ENC` |
| 2022-11 | N-levels | — | — | — |

## Chapter 3 — ITE, a vape, and national service (2023–2027)

ITE from January 2023. He registers for national service at sixteen and a half. In June 2023 he is caught with a vaporiser and pays a composition sum. A Class 2B motorcycle licence at eighteen. He enlists in February 2025, returns from leave two days late that September, is tried summarily and confined to camp for a week. An exit permit for Bangkok in 2026. In November 2026, five years crime-free, the 2021 record becomes spent. He completes full-time service in February 2027; his parents claim the relief.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2023-01 | ITE, Nitec | — | Institute of Technical Education Act 1992 | `NONE` |
| 2023-02-28 | registers for NS at 16½ | Who is subject to the Act? | Enlistment Act 1970 ss 2, 12 | `ENC` |
| 2023-06-02 | a vaporiser; composition $300 | Is possession an offence; may it be compounded? | Tobacco (Control of Advertisements and Sale) and Vaporisers Act 1993 s 16A | `ENC` |
| 2024-08-30 | turns 18; Class 2B licence | — | Road Traffic Act 1961 s 35 and the Driving Licences Rules | `PART` |
| 2025-02-03 | enlists | — | Enlistment Act s 10; Singapore Armed Forces Act 1972 ss 3-4 | `PART`; `ENC` |
| 2025-09-22 | two days late from leave; summary trial; seven days confined | Is late return absence without leave; what may a summary trial award? | SAF Act s 22, Part 4 | `ENC` |
| 2026-05-10 | exit permit, Bangkok | Does a serviceman need a permit to leave? | Enlistment Act ss 32-33 | `ENC` |
| 2026-11-20 | the 2021 record becomes spent | When, and what may he say about it afterwards? | Registration of Criminals Act 1949 ss 7A-7E | `ENC` |
| 2027-02-02 | operationally ready; parents' NSman relief | — | Enlistment Act ss 13-15; Income Tax Act 1947 s 39(2)(n) | `ENC` |

## Chapter 4 — The platform years (2027–2032)

No job waits. He rides for a delivery platform on a power-assisted bicycle for seven years, a platform worker under the 2024 Act, with the operator contributing to his CPF because he was born after 1994. He rides on a footpath once and pays for it. He files a tax return as a self-employed man. In April 2029 a car door opens into him and he breaks a wrist; a platform worker is covered for work injury, and the Act's tables pay for six weeks off and a three per cent permanent incapacity. He answers the census. He does not vote in 2030 and his name comes off the register; he has it put back in 2032. He brings three cartons of cigarettes back from Johor and is stopped. Two credit cards at twenty-four, both at their limits by twenty-five, and then eight thousand dollars from a licensed moneylender at the capped rate.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2027-03-06 | rides for a delivery platform | Is he a platform worker; is the operator one? | Platform Workers Act 2024 ss 3-6, First and Second Schedules | `ENC` |
| 2027-03-31 | first month: the operator's CPF contribution | Must it contribute, at what rate for a rider born after 1994? | Platform Workers Act Part 3; CPF Act 1953 s 7 | `PART` for both: the platform row is scoped to coverage, the CPF row to s 7 |
| 2027-07-14 | PAB on a footpath; composition $300 | Where may a PAB be ridden? | Active Mobility Act 2017 s 16 | `ENC` |
| 2028-04-18 | first tax return as a self-employed rider, $31,000 | Trade income? Medisave for the self-employed? | Income Tax Act s 10(1)(a), s 39; CPF Act self-employed Medisave | `ENC`; `PART` |
| 2029-04-12 | a car door; a fractured wrist; six weeks off | Is a platform worker covered, and what is paid? | Work Injury Compensation Act 2019 ss 7, 14, 16, ss 34A-34P (platform workers), First Schedule; MediShield Life s 3 | `ENC` — the full WICA row carries the platform-worker Part; 3% permanent incapacity from the Table |
| 2030-06-30 | the Census | — | Statistics Act 1973 ss 5-6 | `ENC` |
| 2030-09-12 | does not vote | What happens to a non-voter? | Parliamentary Elections Act 1954 s 43 | `ENC` |
| 2031-01-15 | three cartons from Johor; composition at the checkpoint | The offence; the Green Channel presumption; the allowance | Customs Act 1960 ss 93, 128J, 128L; the Customs (Duties) Order | `ENC`; `REGS` for the allowance (none for cigarettes) |
| 2031-03-02 | a credit card at 24, another in June | Who may be issued one; what income? | Banking Act 1970 s 57; Banking (Credit and Charge Card) Regulations 2013; Credit Bureau Act 2016 ss 4, 6-8 | `ENC`; `REGS`; `ENC` |
| 2032-08-20 | $8,000 from a licensed moneylender | The most a licensee may charge, and what if it charges more? | Moneylenders Act 2008 ss 2-3, 35(3), 36; the Moneylenders Rules | `ENC` for the cap mechanism; `REGS` for 4% a month |
| 2032-10-05 | name restored to the register | — | PEA s 43(8) | `ENC` |

## Chapter 5 — Cheryl, Rui En, and a marriage that came after (2032–2033)

He meets Cheryl Tan in May 2032. Rui En is born in January 2033; her parents are not married. She is a citizen by birth. Cheryl, employed, takes sixteen weeks of maternity leave, which an unmarried mother has had since 2017. Jun Hao, a self-employed father and unmarried, is not eligible for the paternity benefit, and the Child Development Co-Savings Act's Baby Bonus turns on the parents' marriage. They give notice in August and marry at the Registry on 16 September 2033, and the marriage does two things the law lists: it legitimates Rui En, and it brings the Baby Gift, the account and his four weeks of leave within the year. They rent a two-room flat.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2033-01-22 | Rui En born; parents unmarried | Citizen? May the father's particulars be registered? Legitimate? | Constitution Art 121; RBDA 2021 (father's particulars where the parents are not married); Legitimacy Act 1934 s 2 | `ENC`; `PART`; `ENC` |
| 2033-01-22 | Cheryl's maternity leave | Does an unmarried mother get Government-paid leave? | CDCSA s 9 and the 2017 gate; Employment Act s 76 | `ENC` |
| 2033-01-22 | no paternity benefit for an unmarried self-employed father | Eligible? Would marriage within the year change it? | CDCSA ss 12H(4), 12I | `ENC` — and the row's fork F4 is exactly the self-employed father's cohort |
| 2033-02-01 | no Baby Gift yet | Is a child born outside marriage eligible; what if the parents marry? | CDCSA s 3; child-support row, 2033 cohort | `ENC` |
| 2033-08-19 | notice of marriage | How long is it good for? | Women's Charter 1961 ss 14-15 | `ENC` — enlarged for Simone's REQ-0005 |
| 2033-09-16 | married at the Registry; Rui En legitimated | Who may solemnise; what does the marriage do for a child born before it? | Women's Charter ss 9, 11, 22; Legitimacy Act s 3 | `ENC` |
| 2033-10-03 | Baby Gift $10,000, the account, Child Credits; his paternity leave | — | child-support row; CDCSA ss 12H-12I | `ENC` |
| 2033-11-01 | a rented two-room flat at $1,500 | What governs the tenancy; stamp duty on the lease; the owner's consent to let | common law; Stamp Duties Act First Schedule Art 8; HDA 1959 | `CASE`; `ENC` (Art 8 enlarged for REQ-0008); `ENC` |

## Chapter 6 — The security job, the claim, and the debts (2034–2037)

A security officer's licence and a job at Sentinel: $2,600 basic and twelve-hour shifts, which puts him inside Part 4 of the Employment Act, the part Simone never met: hours, rest days, overtime at one and a half. For thirteen months Sentinel pays overtime at the basic rate. He mediates at the Tripartite Alliance and then claims at the Employment Claims Tribunal, and is paid $4,100. In 2036 a friend's debt to an unlicensed lender arrives at his door as paint and glue; the loan is unenforceable, the harassment is an offence with mandatory caning, and the household gets a protection order. By 2037 his own debts are $41,000 and a creditor files for bankruptcy; the Official Assignee, exercising a discretion the Act gives him, finds him suitable for the Debt Repayment Scheme instead. Five years at $690 a month.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2034-02-01 | security officer at Sentinel, posted to the office tower where Lexi Technologies, Haziq's company and Simone's employer, is a tenant | May he work unlicensed; what does Part 4 give a workman on $2,600? | Private Security Industry Act 2007 s 13, ss 16-20; Employment Act ss 35, 36, 38; CPF Act s 7 | `ENC` |
| 2035-03-31 | overtime at the basic rate for 13 months | What is owed; how far back? | Employment Act s 38(4), s 21 | `ENC` — $4,100 |
| 2036-03-10 | mediation, then the Employment Claims Tribunal; order for $4,100 | Must he mediate first; time limits; what may be ordered? | Employment Claims Act 2016 ss 3, 12-16, 21-24 | `ENC` |
| 2036-08-22 | a friend's loan shark: paint and glue on the door | Enforceable? What offence? What protection? | Moneylenders Act ss 19, 47; Protection from Harassment Act 2014 ss 3-4, 12; Vandalism Act 1966 ss 2-3 | `ENC` |
| 2037-02-06 | $41,000 of debt; licensed collectors | Who may collect, and how? | Debt Collection Act 2022 ss 6-7, 17-18, 33-35; Credit Bureau Act ss 11-13 | `ENC` |
| 2037-04-20 | a bankruptcy application; the Debt Repayment Scheme instead | When does the scheme apply; who decides suitability? | Insolvency, Restructuring and Dissolution Act 2018 ss 289-291 | `ENC` — the suitability determination is a discretion written into the Act |
| 2037-06-01 | a five-year plan at $690 a month | — | IRDA s 291 | `ENC` |

## Chapter 7 — Separation, divorce, and a flat of his own (2038–2045)

In June 2038 Cheryl and Rui En, five, move to her mother's. Care and control to Cheryl; maintenance for the child at $600 a month, which he misses three times in the winter and is brought back to court for. Three years apart, and in July 2041 the marriage is dissolved by consent on that ground, the only ground that needs no fault; there are no matrimonial assets to divide. He turns thirty-five that August, which is the age at which HDB lets a single citizen buy, applies for a two-room Flexi flat in 2042, completes the repayment plan the same year, and gets the keys in March 2045. Stamp duty: $1,400.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2038-06-01 | separation | Care and control; maintenance for the child | Guardianship of Infants Act 1934 ss 3, 5; Women's Charter s 69 | `ENC` — $600 a month |
| 2039-01-15 | three missed payments; enforcement | What may the court do about arrears? | Women's Charter s 71; Family Justice Act 2014 s 26(3A) | `PART`; `ENC` |
| 2041-07-10 | divorce by consent, three years apart | Old enough a marriage? The ground? Anything to divide? | Women's Charter s 94, s 95, s 95A(1)(d); Part 10 Chapter 4A; Family Justice Act s 10 | `ENC`; `PART` (division is outside the row; there is nothing to divide); `ENC` |
| 2041-08-30 | turns 35 | May a single citizen buy a new flat? | HDB singles scheme, income ceiling $7,000 | `ADMIN-POLICY` |
| 2042-02-18 | applies for a 2-room Flexi | The Act's property test | HDA s 50(1); the singles grant | `ENC`; `ADMIN-POLICY` |
| 2042-05-31 | the plan completes; discharged | What does the bureau keep, and for how long? | IRDA s 291; Credit Bureau Act (retention) | `ENC`; `PART` |
| 2045-03-20 | keys; stamp duty on $140,000 | How much? | Stamp Duties Act Art 3(a)(iv), (bi); HDA Part 4; CPF Act Part 4A | `ENC` ($1,400; no additional duty); `ENC`; `PART` |

## Chapter 8 — The exclusion order, the stairwell, and the retrenchment (2045–2060)

Singapore Pools on Saturdays, then the casino on paydays, paying the daily entry levy. In May 2046 Simone applies for a family exclusion order against him; the Committee, exercising the discretion the Act gives it, makes the order for a year, and he goes to counselling. A job form in 2047 asks about convictions, and the law says he need not mention a spent one. A speeding composition on the motorcycle. His father dies in 2052 and leaves everything to his mother. In October 2053 he falls on a wet stairwell on patrol: eleven weeks off, and a permanent incapacity the doctor puts at eight per cent, at the edge of a band, so that the lump sum from the Table turns on a clinical judgement. In 2055 Sentinel loses its contract and retrenches him at forty-nine; the Act gives him notice and a retrenchment benefit without saying how much. He becomes a cleaner under the Progressive Wage Model. In 2060 his mother dies intestate and he and Simone take equally; he puts $100,000 of it into his Retirement Account.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2045-09 | Pools, then the casino | Which gambling is lawful; the entry levy | Gambling Control Act 2022 ss 12-13, 20; Casino Control Act 2006 s 116 | `ENC` |
| 2046-05-08 | Simone applies for a family exclusion order | Who may apply, on what grounds, and who decides? | Casino Control Act ss 159-161; s 162 | `PART` for application and grounds; `ENC` for the terms; the Committee's decision is a discretion in the Act |
| 2046-06-20 | order for one year; counselling | — | CCA s 162; NCPG counselling | `ENC`; `ADMIN-POLICY` |
| 2047-03-04 | a job form asks about convictions | Must he disclose a spent record? | Registration of Criminals Act s 7E | `ENC` — no |
| 2049-07-19 | motorcycle, 25 km/h over | — | Road Traffic Act s 63; the demerit points scheme | `PART`; `REGS` |
| 2052-08-19 | his father dies; everything to his mother | Does he take anything? | Wills Act; Probate and Administration Act (succession rows) | `ENC` — no |
| 2053-10-05 | a fall on patrol at 47, in Lexi's building; 8% permanent incapacity, at the edge of a band | The employer's liability; the lump sum; what if the assessment is borderline; is the tenant liable as occupier? | WICA ss 7, 14, 16, First Schedule Tables; WSH Act 2006 ss 11-12 | `ENC` — the sum is arithmetic from the Table, the percentage a clinical judgement; `PART` for ss 11-12 |
| 2055-11-30 | retrenched at 49 | Notice; retrenchment benefit; support | Employment Act ss 10-11, s 45; the Tripartite Advisory; Workfare; SkillsFuture | `ENC` (the Act sets no amount); `ADMIN-POLICY`; `NONE` for the SkillsFuture Act |
| 2056-02-01 | a cleaner under the Progressive Wage Model | The wage floor, and where it is written | Employment Act Part 4; the PWM; Environmental Public Health Act Part 5A | `ENC`; `ADMIN-POLICY`; `PART` |
| 2060-01-27 | his mother dies intestate | Who takes, in what shares? | Intestate Succession Act s 7; PAA | `ENC` — half each |
| 2060-09-15 | $100,000 into his Retirement Account | Relief for a top-up to his own account; is it matched? | Income Tax Act s 39(3A); Matched Retirement Savings Scheme | `ENC`; `ADMIN-POLICY` |

## Chapter 9 — The stroke, Silver Support, and the end (2061–2079)

At fifty-five, with the Basic Retirement Sum met by the top-up, he withdraws what the Act allows. A stroke at fifty-six: MediShield Life, Medisave, and a Medifund application for the rest. A CareShield Life claim in which two activities of daily living are clearly lost and a third sits at the margin, so that the rule is exact and the facts are a clinical judgement; the assessor says yes, and two years later says no. He resigns; ComCare; Rui En, thirty, helps, and the Maintenance of Parents Act waits unused. A lasting power of attorney to her. At sixty-five, CPF LIFE and, unlike his father, Silver Support. An advance medical directive at sixty-eight. A second stroke at seventy-two; his kidneys are donated under the presumption he never objected to; Rui En and Simone register the death. No will, an estate under fifty thousand dollars, and so the Public Trustee rather than a grant; his daughter takes all of it, and his CPF separately as his nominee.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2061-08-30 | turns 55 | With the Basic Retirement Sum met, what comes out? | CPF Act s 15(1)-(6) | `ENC` |
| 2063-03-14 | a stroke at 56; three weeks in hospital | What does MediShield Life pay; Medisave; Medifund for the rest? | MediShield Life Scheme Act ss 3-4; CPF Act s 16; Medical and Elderly Care Endowment Schemes Act 2000 ss 12-17 | `PART` (claim limits are in regulations); `ENC`; `ENC` |
| 2063-04-28 | CareShield Life claim: two activities lost, a third at the margin | What is severe disability, and who says whether he meets it? | CareShield Life and Long-Term Care Act 2019 s 6, First Schedule | `ENC` — three of six activities; the margin is for the assessor |
| 2063-04-30 | resigns; ComCare; Rui En helps | Could he claim maintenance from his daughter? | ComCare; Maintenance of Parents Act 1995 s 3 | `ADMIN-POLICY`; `ENC` (he never applies) |
| 2063-09-10 | lasting power of attorney to Rui En | Capacity? What may she not do? | Mental Capacity Act 2008 ss 3-5, 11-13 | `ENC` |
| 2065-05-01 | reassessed: two activities only; payouts stop | — | CareShield First Schedule | `ENC` |
| 2071-08-30 | turns 65: CPF LIFE; Silver Support | Eligible, unlike his father? | CPF Act Part 3A; Silver Support Scheme Act ss 6-7; the payout amounts | `PART`; `ENC` (yes); `REGS` |
| 2075-04-02 | advance medical directive | — | Advance Medical Directive Act 1996 ss 3-9 | `ENC` |
| 2079-04-18 | dies at 72; kidneys donated | Does the presumption apply at 72; who registers the death? | Human Organ Transplant Act 1987 s 5; RBDA ss 19-23 | `ENC` |
| 2079-05-02 | no will; an estate under $50,000 | Who takes; must there be a grant; the lease refund | ISA s 7; Public Trustee Act 1915 ss 6-8 and the value limit; CPF Act s 25; HDB lease refund; Estate Duty Act s 2A | `ENC`; `ENC` with `REGS` for the limit; `ENC`; `ADMIN-POLICY`; `ENC` |

---

## What the scenario touches

Fifty-seven subjects, against Simone's sixty-eight, with thirty-two in common; the two lives together touch ninety-three. The twenty-five this life reaches that hers never does: Penal Code, Criminal Procedure Code, Children and Young Persons, Probation of Offenders, Registration of Criminals, Family Justice, Tobacco and Vaporisers, Institute of Technical Education, Platform Workers, Active Mobility, Work Injury Compensation (twice), Workplace Safety and Health, Moneylenders, Debt Collection, Insolvency (the Debt Repayment Scheme), Private Security Industry, Employment Claims, Protection from Harassment, Vandalism, Guardianship of Infants, Legitimacy, Gambling Control, Casino Control, Medical and Elderly Care Endowment Schemes, and Maintenance of Parents.

- **ENC, inside a row's scope on at least one question**: 51 subjects, counting the Constitution, the succession subject and the child-support row.
- **PART, a row exists but stops short on at least one question**: Children and Young Persons (the Youth Court), Platform Workers (CPF contributions), CPF (self-employed Medisave, Home Protection, CPF LIFE), Women's Charter (enforcement of maintenance; division of assets), Casino Control (application and grounds for an exclusion order), Registration of Births and Deaths (a father's particulars outside marriage), Road Traffic (licensing, speeding, demerit points), Credit Bureau (retention), MediShield Life (claim limits), Workplace Safety and Health (s 12), Environmental Public Health (cleaning licences), Family Justice (Youth Courts), Enlistment (s 10).
- **NONE**: Institute of Technical Education Act 1992; Skills and Workforce Development Agency Act 2026.

The largest hole in this life is not an Act but a court: the Youth Court's jurisdiction and powers under the Children and Young Persons Act, which the row does not reach, so the one moment that decides whether a fifteen-year-old carries a conviction is adjudicated by a row that only knows what a young person is. [`GAPS.md`](GAPS.md) ranks the rest.

## Sample prompts for the chat demo

1. "I took something from a shop and got stopped. I'm fifteen. What happens now?" — Penal Code s 380; CPC First Schedule; CYPA, where the row stops at the door of the Youth Court.
2. "If I finish probation, do I have a record?" — Probation of Offenders Act s 11; Registration of Criminals Act s 7A.
3. "I came back from leave two days late." — SAF Act s 22.
4. "Does the platform have to pay my CPF?" — Platform Workers Act ss 3-6 for coverage; Part 3 is outside the row, and the assistant says so.
5. "A car door broke my wrist on a delivery. Am I covered?" — WICA ss 34A-34P and the Table.
6. "I didn't vote. Am I in trouble?" — PEA s 43: no, your name is off the register, and here is how to put it back.
7. "The moneylender says 6% a month." — Moneylenders Act s 36: the loan is unenforceable as to the excess.
8. "Rui En was born before we married. Does she get the Baby Gift?" — CDCSA s 3; after the marriage, Legitimacy Act s 3, and yes.
9. "They've been paying my overtime at the basic rate for a year." — Employment Act s 38(4); Employment Claims Act s 3.
10. "Someone glued our lock over a loan that isn't mine." — Moneylenders Act ss 19, 47; POHA s 12.
11. "A creditor wants me bankrupt." — IRDA ss 289-291: the Official Assignee decides whether you go on the Scheme instead, and here is what he must consider.
12. "Cheryl and I have been apart three years." — Women's Charter s 95A(1)(d).
13. "My sister wants me banned from the casino." — Casino Control Act s 162 for what the order can say; the application and grounds are outside the row.
14. "The form asks if I've ever been convicted." — RCA s 7E: a spent record need not be disclosed.
15. "Dad didn't get Silver Support. Will I?" — Silver Support Scheme Act ss 6-7: yes, and the assistant should say which test is different.
