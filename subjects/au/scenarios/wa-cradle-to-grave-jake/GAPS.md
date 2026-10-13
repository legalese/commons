# Gap register for Jake's scenario

As for Chloe's: the Commonwealth and Western Australian statute books are deposited and unencoded on 13 October 2026, so this register is an encoding order, taken from how often and how early an off-the-path life asks each Act. Ledger entries, one `no-row` per Act with a count, are in [`../../requirements.jsonl`](../../requirements.jsonl) (Commonwealth) and [`../../wa/requirements.jsonl`](../../wa/requirements.jsonl) (state).

## A. Acts to encode, in the order this life needs them

| rank | Act | events | what to encode first |
| --- | --- | --- | --- |
| 1 | **Fair Work Act 2009** (Cth) | 9 | s 15AA and Part 3A-2 (employee-like workers; minimum standards orders); Part 2-3 (modern awards: the Security Services Industry and Cleaning Services Awards); ss 45, 117, 119, 389, 544-548 |
| 2 | **Social Security Act 1991** (Cth) | 6 | ss 43, 1064 (Age Pension); s 94 and the Impairment Tables (Disability Support Pension); Part 2.12 (JobSeeker); Part 2.19 (Carer Allowance) |
| 3 | **Young Offenders Act 1994** (WA) with the **Children's Court of Western Australia Act 1988** | 4 | ss 7, 22-30 (cautions, juvenile justice teams, the effect of completion); Children's Court s 19 |
| 4 | **Bankruptcy Act 1966** (Cth) | 4 | Part IX (debt agreements: ss 185C, 185EC, 185H, 185N) |
| 5 | **Child Support (Assessment) Act 1989** and **Child Support (Registration and Collection) Act 1988** (Cth) | 2 | Part 5 of the Assessment Act (the formula, ss 35-55); Parts IV-V of the Collection Act |
| 6 | **National Consumer Credit Protection Act 2009** (Cth) | 4 | s 29 (unlicensed credit); ss 31A-31B (small amount credit contracts); ss 128-133, 133BE (responsible lending) |
| 7 | **Workers' Compensation and Injury Management Act 2023** (WA) | 2 | s 5 (worker); Parts 2-3 (income compensation; permanent impairment); Part 7 (the 15% threshold) |
| 8 | **Family Law Act 1975** (Cth) | 2 | Part VII (parental responsibility; parenting plans s 63C); ss 48, 55A, 79 |
| 9 | **School Education Act 1999** (WA) | 3 | ss 6, 9, 11B, 23, 38-40 |
| 10 | **Residential Tenancies Act 1987** (WA) | 1 | ss 27C, 29, 30, 61-64 |
| 11 | **Security and Related Activities (Control) Act 1996** (WA) | 1 | ss 8, 15-16 |
| 12 | **Casino Control Act 1984** and **Betting Control Act 1954** (WA); **Interactive Gambling Act 2001** (Cth) | 2 | Casino s 25 (exclusion: no family application); Interactive Gambling ss 15, 15AA, Part 7A (BetStop) |
| 13 | **Motor Vehicle (Third Party Insurance) Act 1943** and **Civil Liability Act 2002** (WA) | 1 | s 4; Part 2 |
| 14 | **Restraining Orders Act 1997** and the **Criminal Code** (WA) | 2 | Part 3 (misconduct restraining orders); Code ss 371, 378, 444, 338B |
| 15 | **Spent Convictions Act 1988** (WA) | 2 | s 3, Parts 2-3, and its silence where nothing was recorded |
| 16 | **National Disability Insurance Scheme Act 2013** (Cth) | 1 | ss 21-25 (access) |
| 17 | the rest | 20 | as in Chloe's register, plus: Tobacco and Other Products Control ss 6, 106 and Therapeutic Goods ss 41QD-41QE; Vocational Education and Training Part 7; Fines, Penalties and Infringement Notices Enforcement Part 3; Road Traffic Act s 59 and the Code; ABN Act s 8; GST Act s 23-5; Magistrates Court Act; Competition and Consumer Sch 2 s 50; First Home Owner Grant and the Housing Act; Public Trustee Act s 10; Rates and Charges (Rebates and Deferments) ss 24-25; Work Health and Safety 2020 ss 19-20 |

## B. Subsidiary legislation this life needs

- Road Traffic Code 2000 and the Road Traffic (Vehicles) Regulations 2014: eRideables (footpaths at 10 km/h; roads up to 50 km/h).
- The Security Services Industry Award 2020 and the Cleaning Services Award 2020, with the annual wage review rates.
- Social Security (Tables for the Assessment of Work-related Impairment for Disability Support Pension) Determination 2023.
- Bankruptcy Regulations: the indexed debt agreement thresholds.
- Child Support (Assessment) Regulations and the annual costs-of-children table.
- National Consumer Credit Protection Regulations: the small amount credit contract definitions.
- Customs By-laws: 25 cigarettes.
- Fines enforcement: the modified penalties for traffic offences.

## C. Administrative policy with legal effect

| area | the policy | chapter |
| --- | --- | --- |
| WA Police | when to caution, refer or charge a young person | 2 |
| Keystart; the Housing Authority | low-deposit lending; public housing eligibility | 7 |
| Crown Perth | the self-exclusion program | 8 |
| Services Australia | mutual obligation requirements; the ACCC/ASIC debt collection guideline | 6, 8 |
| Department of Education | attendance panels in practice; TAFE pre-apprenticeship entry | 1, 2 |

## D. Common law and case law

| doctrine | where | note |
| --- | --- | --- |
| employee or contractor: the multifactorial test, now read with s 15AA | Ch 4 | the cases set the line the Act restates |
| no status of illegitimacy | Ch 5 | a negative with no live instrument; the statutes that removed the distinction are historical |
| the welfare of the child in parenting orders | Ch 7 | Part VII names it; the cases apply it |
| damages for personal injury: thresholds and assessment | Ch 4, 8 | Civil Liability Act Part 2 and the cases |
| the clinical judgement behind a statutory percentage: whole-person impairment; impairment points | Ch 8, 9 | not law; the simulation records it as a human input with declared uncertainty |

## E. Seams

1. **With Chloe's file.** The parents' deaths are hers. Her search for an exclusion order is here only.
2. **With Daniel's file.** The 2034 posting and the 2053 fall are in his tower; the fall is the employer's question here and the occupier's there.
3. **Two layers.** Nineteen events engage both legislatures.
4. **Nature mode.** Five unlawful acts, each answered by a process. No replay may block them.
5. **Nothing is encoded.** Every status is `NONE`, `REGS`, `ADMIN-POLICY` or `CASE`; run `check-status.py` before a demo.
