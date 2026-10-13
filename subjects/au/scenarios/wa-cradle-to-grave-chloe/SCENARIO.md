# Scenario: cradle to grave — Chloe Harding (WA Sim One, the sunny day)

Simone Ng's life, moved to Perth. Born at King Edward Memorial Hospital in March 2003 to a fitter and a school officer in Armadale, she goes to the local public school, UWA on HECS, a graduate program at a logistics company, meets an electrician in a polling-place queue, builds a house in Byford on the first home owner grant, marries in Kings Park, has two children on Paid Parental Leave and Family Tax Benefit, changes jobs to a legal-technology start-up, serves on a jury, registers a dog and a cat, upgrades to a community-titles townhouse, draws her super at sixty-three, is refused the Age Pension at sixty-seven, downsizes to Mandurah, and dies at eighty-five with a will. A sunny day under a different sky: nothing goes wrong, and the law arrives as an answer every time.

The arc is Simone's. What changes is the law, and the change is not only in names. There is no national service and no NRIC; a tax file number at fifteen does the work. Superannuation replaces the Central Provident Fund, and the rate steps from eleven to twelve per cent across her first two years of work. Paid Parental Leave comes from the Commonwealth through the employer as paymaster and has no marriage condition. Family assistance is means-tested and reconciled against the tax return. A will can be made at eighteen. Organ donation is opt-in. There is no additional buyer's duty and no estate duty, but there is a first home owner grant, a dividing fence, a jury summons, and a council that registers her dog.

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — twenty beats, two a chapter, with ages.
- [`GAPS.md`](GAPS.md) — what this life needs from a Commonwealth and Western Australian library that, on the day of writing, holds sources and no encodings.
- [`facts.json`](facts.json) — the cast and 79 dated events with their law and status, ages at every event, the twenty beats flagged.
- [`check-status.py`](check-status.py) — re-derives the status column from the tree. Run it from anywhere; it resolves Commonwealth slugs under `subjects/au/` and state slugs under `subjects/au/wa/`.

## Design rules

The six rules of the Singapore scenarios apply, with three particulars.

1. **One "now".** 13 October 2026: Chloe is twenty-three, two and a half years into her first job, living with Liam at her parents' house and saving for a deposit.
2. **Two legislatures.** Every event names whether the Act is the Commonwealth's or Western Australia's, and a question often engages both: Paid Parental Leave is federal, the birth certificate is state; superannuation is federal, long service leave is state; the first home owner grant is state, the deposit guarantee is a federal scheme. The simulation's routing has to carry the layer.
3. **Statuses are read from the tree on 13 October 2026.** The Commonwealth and WA statute books are deposited in full and encoded nowhere, except where a row lands after this was written. Every `NONE` here is therefore a demand on the library, and `GAPS.md` is the order in which to meet it. `REGS`, `ADMIN-POLICY` and `CASE` mean what they mean in the Singapore scenarios.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Chloe Harding** | 14 Mar 2003, KEMH | the main character | citizen by birth; dies 2 Nov 2088 with a will |
| Liam Nguyen | 22 Jul 1999 | her husband from 18 May 2029 | electrician; a four-year apprenticeship under a training contract |
| Oliver Nguyen | 5 Sep 2030 | their son | |
| Ella Nguyen | 12 Apr 2033 | their daughter | |
| Graham Harding, Sue Harding | 1970, 1972 | her parents | a house in Armadale as joint tenants; he dies 2052 with a will, she 2060 without |
| Jake Harding | 30 Aug 2006 | her brother | his own scenario |
| Ironbark Logistics Pty Ltd | — | her first employer, 2024 to 2034 | a national system employer under the Fair Work Act |
| Jarrah Legal Technologies Pty Ltd | — | her employer from 2034 | Daniel Rossi's company |

---

## Chapter 0 — Born (2003)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2003-03-14 | birth at KEMH | Australian citizen? | Australian Citizenship Act 2007 (Cth) s 12 | `NONE` |
| 2003-04-02 | registered on day nineteen | By when, and who must? | Births, Deaths and Marriages Registration Act 1998 (WA) ss 12-13 (60 days), s 19 | `NONE` |
| 2003-04-02 | Medicare | Is a newborn eligible? | Health Insurance Act 1973 (Cth) s 3, Part II | `NONE` |
| 2003-05 | vaccinations | What does immunisation do to family payments? | A New Tax System (Family Assistance) Act 1999 (Cth) s 6; the National Immunisation Program | `NONE`; `ADMIN-POLICY` |

## Chapter 1 — Primary school (2008–2015)

Kindergarten at four, which is not compulsory; Year 1 in 2010, which is, because she is six and a half by the June before it. A savings account under the deposit guarantee. A first passport for Bali at eight, with both parents' consent, and the passenger card on the way back.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2008-02 | kindergarten | — | School Education Act 1999 (WA) s 6 | `NONE` |
| 2010-02-01 | Year 1 | From which year must she attend? | School Education Act ss 6, 9, 23 | `NONE` |
| 2010-03 | a children's account | Protected? | Banking Act 1959 (Cth) Division 2AA (Financial Claims Scheme) | `NONE` |
| 2011-06 | first passport | Who applies; whose consent? | Australian Passports Act 2005 (Cth) s 11 | `NONE` |
| 2011-06 | home from Bali | The duty-free concession; what to declare | Customs Act 1901 (Cth) ss 68, 234; Biosecurity Act 2015 (Cth) Part 3; the By-laws | `NONE`; `REGS` |
| 2015-05 | NAPLAN; Year 7 to high school | — | Department policy | `ADMIN-POLICY` |

## Chapter 2 — Growing up (2018–2021)

A tax file number and a casual job at fifteen, on junior rates, with no superannuation under thirty hours a week. A learner's permit at sixteen, provisional licence and provisional enrolment at seventeen. The State election falls the day before her eighteenth birthday. At eighteen a list of things switch on, and she registers as an organ donor, which in Australia is a choice and not a presumption.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2018-03-14 | 15: TFN; a casual job | Junior rates? Super? | Taxation Administration Act 1953 (Cth) Part VA; Fair Work Act 2009 (Cth) and the General Retail Industry Award; Superannuation Guarantee (Administration) Act 1992 (Cth) s 28 | `NONE` |
| 2019-03-14 | 16: learner's permit | Age and conditions | Road Traffic (Authorisation to Drive) Act 2008 (WA) s 8; the Regulations | `NONE`; `REGS` |
| 2020-03-14 | 17: provisional licence; provisional enrolment | — | Commonwealth Electoral Act 1918 (Cth) s 100 | `NONE` |
| 2021-03-13 | the State election, a day early | Who may vote? | Electoral Act 1907 (WA) s 17 | `NONE` |
| 2021-03-14 | turns 18 | What switches on? | Age of Majority Act 1972 (WA); Commonwealth Electoral Act ss 93, 245; Marriage Act 1961 (Cth) s 11; Wills Act 1970 (WA) s 7; Liquor Control Act 1988 (WA) s 121; Juries Act 1957 (WA) s 5; Guardianship and Administration Act 1990 (WA) Part 9 | `NONE` |
| 2021-03-20 | organ donor register | Opt-in or presumed? | Human Tissue and Transplant Act 1982 (WA) s 22; the Australian Organ Donor Register | `NONE` |

## Chapter 3 — University (2021–2023)

A Bachelor of Commerce at UWA, fees deferred under HECS-HELP and repaid through the tax system once her income passes the threshold. A first federal election in 2022. An internship that the Fair Work Act does not count as employment if it is a vocational placement.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2021-02 | UWA; HECS-HELP | What is deferred; when repaid? | Higher Education Support Act 2003 (Cth) Parts 3-2, 4-2; University of Western Australia Act 1911 (WA) | `NONE` |
| 2022-05-21 | first federal election | Compulsory? | Commonwealth Electoral Act s 245 | `NONE` |
| 2023-11 | internship | Employee? Super? | Fair Work Act ss 12, 13, 15AA; Superannuation Guarantee (Administration) Act s 12 | `NONE` |
| 2023-12 | graduates | — | — | — |

## Chapter 4 — First job (2024–2026) — the demo's "now"

A graduate program at $70,000. The first payslip shows superannuation at eleven per cent, which becomes eleven and a half that July and twelve the July after, and PAYG withheld with a HECS component once she passes the threshold. Four weeks' annual leave and ten days' personal leave from the National Employment Standards; Western Australia Day from the state's holidays Act. A credit card under responsible lending. The Do Not Call Register. Her first tax return owes nothing; her second starts the HECS repayment. A State election at twenty-two, a federal one where she meets Liam, census night, and insurance inside her super fund.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2024-02-05 | starts at Ironbark | The contract; the minimum standards; probation | Fair Work Act Part 2-2, s 383; Minimum Conditions of Employment Act 1993 (WA) does not apply to a national system employer | `NONE`; probation `CASE` |
| 2024-02-29 | first payslip | How much super; what is withheld? | Superannuation Guarantee (Administration) Act ss 16, 19, 23; Superannuation Industry (Supervision) Act 1993 (Cth) Part 7; Taxation Administration Act Sch 1 Part 2-5; Fair Work Act s 536 | `NONE` — $641.67 at 11% on $5,833 a month |
| 2024-05-06 | three months | Annual leave; personal leave; public holidays | Fair Work Act ss 87, 96, 114-116; Public and Bank Holidays Act 1972 (WA) | `NONE` — 4 weeks; 10 days |
| 2024-06 | credit card; credit report | What must a lender assess; what may a bureau hold? | National Consumer Credit Protection Act 2009 (Cth) Part 3-2 Div 3; Privacy Act 1988 (Cth) Part IIIA | `NONE` |
| 2024-07 | marketing | Can she stop it? | Do Not Call Register Act 2006 (Cth) s 11; Spam Act 2003 (Cth) ss 16, 18; Privacy Act APP 7 | `NONE` |
| 2024-10 | first tax return, 2023-24 | Tax on $27,500? | Income Tax Assessment Act 1997 (Cth) s 4-10, Div 61; Income Tax Rates Act 1986 (Cth) Sch 7; Medicare Levy Act 1986 (Cth) ss 6-7; Higher Education Support Act s 154-10 | `NONE` — nil |
| 2025-03-08 | first State election | — | Electoral Act 1907 (WA) s 156 | `NONE` |
| 2025-05-03 | federal election; Liam in the queue | — | Commonwealth Electoral Act s 245 | `NONE` |
| 2025-10 | second return, 2024-25 | Tax on $71,500; the HECS repayment | ITAA 1997 s 4-10; Rates Act Sch 7; HESA ss 154-1 to 154-20; Medicare Levy Act s 6 | `NONE` — about $12,842 before offsets, levy $1,430, and a compulsory repayment above the threshold |
| 2026-08-10 | census night | Must they answer? | Census and Statistics Act 1905 (Cth) ss 8, 14 | `NONE` |
| 2026-09 | insurance in super | What may a fund offer by default? | SIS Act s 68AAA; Life Insurance Act 1995 (Cth) Part 10; Insurance Contracts Act 1984 (Cth) s 13, Part IV | `NONE` |

## Chapter 5 — A house and a marriage (2027–2029)

They rent in Cannington under the Residential Tenancies Act, the bond with the Bond Administrator. In February 2028 they sign a house-and-land package in Byford: a new home, so the first home owner grant of $10,000; a contract under the threshold, so no transfer duty at the first home owner rate; a five per cent deposit under the Home Guarantee Scheme; the building contract under the home building Act with indemnity insurance. The land settles in May and the mortgage is registered on a Torrens title. A Notice of Intended Marriage a month before the day, a civil celebrant in Kings Park, and a marriage registered with the state. Handover in July 2029 brings council rates, the emergency services levy, water charges, and an exemption from land tax.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2027-09-01 | renting in Cannington, $480 a week | The bond; rent increases; ending | Residential Tenancies Act 1987 (WA) ss 29, 30, 61-64 | `NONE` |
| 2028-02-20 | house-and-land, $620,000 | The grant; the duty; the deposit guarantee; the building contract | First Home Owner Grant Act 2000 (WA) ss 6-13; Duties Act 2008 (WA) first home owner rate; Housing Australia Act 2018 (Cth) and the Home Guarantee Scheme; Home Building Contracts Act 1991 (WA) ss 4-12 | `NONE`; `ADMIN-POLICY` for the scheme — $10,000; duty nil |
| 2028-05-15 | settlement; mortgage | Indefeasibility; the lender's registration | Transfer of Land Act 1893 (WA) ss 68, 105; National Credit Code | `NONE` |
| 2029-04-10 | Notice of Intended Marriage | How long before; how long good for? | Marriage Act 1961 (Cth) ss 39, 42 | `NONE` — one month, eighteen months |
| 2029-05-18 | married in Kings Park | Who may solemnise; who may marry; registration | Marriage Act ss 11, 13, 23B, 45, 50; BDMR Act Part 5 | `NONE` |
| 2029-07-15 | handover | Who levies what? | Local Government Act 1995 (WA) Part 6 Div 6; Emergency Services Levy Act 2002 (WA); Water Services Act 2012 (WA) Part 5; Land Tax Assessment Act 2002 (WA) s 21; Building Act 2011 (WA) s 40 | `NONE` |
| 2029-09-02 | Liam changes employer | What is lost; what is kept? | Long Service Leave Act 1958 (WA) s 8; Fair Work Act ss 117-118 | `NONE` |
| 2030-03 | a spouse super contribution | The offset | ITAA 1997 s 290-230 | `NONE` |

## Chapter 6 — First child (2030–2031)

Antenatal care bulk-billed and the birth in a public hospital. Unpaid parental leave from the employer, up to twelve months with a right to return; twenty-four weeks of Paid Parental Leave from the Commonwealth, paid through the employer, with weeks reserved for each parent and superannuation on it. Oliver is a citizen at birth and registered within sixty days. The Newborn Upfront Payment and Supplement, Family Tax Benefit on the family income test, Medicare enrolment and the immunisation condition. Long day care with the Child Care Subsidy on the activity test. A flexible working request on her return.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2030-01 | antenatal care; the public hospital | What is bulk-billed; what does a public patient pay? | Health Insurance Act Part II; Health Services Act 2016 (WA) Part 4 | `NONE` |
| 2030-08-22 | unpaid leave begins; PPL claimed | How much unpaid leave; how many paid weeks, shared how, paid by whom? | Fair Work Act ss 70-76, 83; Paid Parental Leave Act 2010 (Cth) Part 2-1, Part 3-5 | `NONE` — 12 months; 24 weeks; 4 reserved for each parent |
| 2030-09-05 | Oliver born | Citizen; registration | Australian Citizenship Act s 12; BDMR Act ss 12-13 | `NONE` |
| 2030-09-05 | Liam's reserved weeks | What is reserved; what may be transferred? | PPL Act; Fair Work Act s 72 | `NONE` |
| 2030-10 | Newborn payments; FTB Part A | What does a first child bring, on what test? | Family Assistance Act Part 3, Sch 1, s 58AA; Family Assistance (Administration) Act 1999 (Cth) Part 3 | `NONE` |
| 2030-10 | Medicare; immunisation | — | Health Insurance Act s 3; Family Assistance Act s 6 | `NONE` |
| 2031-02 | long day care; Child Care Subsidy | The percentage; the activity test | Family Assistance Act Part 4A; Child Care Services Act 2007 (WA) and the National Law | `NONE` |
| 2031-03-14 | returns to work; a flexible working request | May she ask; on what grounds may the employer refuse? | Fair Work Act s 65 | `NONE` |
| 2031-06 | Oliver's passport | — | Australian Passports Act s 11 | `NONE` |

## Chapter 7 — The long middle (2032–2039)

A laptop that fails in month three and the consumer guarantees. Ella in 2033. A job change in 2034 to Jarrah at $110,000 with start-up share scheme interests, unused leave paid out and long service leave crystallised at ten years. Hospital cover before the July after her thirty-first birthday, to avoid the Lifetime Health Cover loading. A used car with vehicle licence duty and compulsory third party through the Insurance Commission. Mochi registered with the shire, Biscuit sterilised and microchipped. A jury summons that her employer must honour. Oliver's first day at the local-intake school. Her father's Age Pension claim refused on assets, with a Seniors Health Card instead. A dividing fence.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2032-05 | a laptop fails | The guarantees; who chooses the remedy? | Competition and Consumer Act 2010 (Cth) Sch 2 ss 54, 259; Magistrates Court (Civil Proceedings) Act 2004 (WA) minor cases | `NONE` |
| 2033-04-12 | Ella born | the Chapter 6 cluster again | PPL Act; Family Assistance Act; BDMR Act | `NONE` |
| 2034-02-01 | joins Jarrah, $110,000 and ESS interests | Notice; leave paid out; long service leave; ESS tax | Fair Work Act ss 90, 117; Long Service Leave Act s 8; ITAA 1997 Div 83A | `NONE` |
| 2034-04 | hospital cover before 1 July after 31 | What is the loading, when does it start? | Private Health Insurance Act 2007 (Cth) Div 34; Medicare Levy Surcharge Acts | `NONE` |
| 2034-06 | a used car, $28,000 | Duty; registration; CTP | Duties Act Ch 5; Road Traffic (Vehicles) Act 2012 (WA) Part 2; Motor Vehicle (Third Party Insurance) Act 1943 (WA) ss 3-4; Catastrophic Injuries Act 2016 (WA) | `NONE` — about $770 duty |
| 2035-03 | Mochi the dog | Registration; microchip; the sterilised fee | Dog Act 1976 (WA) ss 15-16, 22; the Regulations and the local law | `NONE`; `REGS` |
| 2036-02 | Biscuit the cat | What must an owner do before six months? | Cat Act 2011 (WA) ss 5-6, 14, 18 | `NONE` |
| 2036-07 | a jury summons | Must she attend; must the employer release and pay her? | Juries Act 1957 (WA) ss 5, 32, 58B-58C; Fair Work Act s 111 | `NONE` |
| 2036-10 | tax return with two children | Family Tax Benefit reconciled | Family Assistance (Administration) Act Parts 3-4 | `NONE` |
| 2037-02 | Oliver, Year 1 | Which school? | School Education Act ss 9, 78 | `NONE` |
| 2037-05-02 | Graham turns 67 | Age Pension? The Seniors Health Card? | Social Security Act 1991 (Cth) ss 43, 1064, 1061ZG | `NONE` — pension no; card yes |
| 2039-08 | a dividing fence | Who pays? | Dividing Fences Act 1961 (WA) ss 7-9 | `NONE` — half each |

## Chapter 8 — Mid-life (2040–2060)

Byford sold with no capital gains tax on the family home; a townhouse in a community titles scheme in Baldivis, with transfer duty at the general rate and no surcharge. Wills, binding super nominations that lapse every three years unless made non-lapsing, enduring powers of attorney. A self-education deduction at forty. Oliver turns eighteen and enrols. Jarrah is sold and her scheme interests pay out. Her father dies at home: the funeral director registers the death, the cremation needs a permit, the will leaves everything to her mother, the house passes by survivorship, the super passes tax-free to a dependant. Her mother dies without a will and the children take equally.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2040-03-20 | Byford sold, $890,000 | Capital gains tax? | ITAA 1997 s 118-110 | `NONE` — nil |
| 2040-04-28 | Baldivis, $1,300,000 | Duty; the community corporation | Duties Act Ch 2 Part 5; Community Titles Act 2018 (WA) Parts 3, 7; Transfer of Land Act s 68 | `NONE` — about $55,185 |
| 2041-02 | wills; super nominations; enduring powers of attorney | Formalities; the lapse; who may be attorney | Wills Act 1970 (WA) ss 8, 13; SIS Act s 59(1A), reg 6.17A; Guardianship and Administration Act Part 9 | `NONE` |
| 2043-03 | a course at 40 | Deductible? | ITAA 1997 s 8-1 | `NONE` |
| 2048-09-05 | Oliver turns 18 | — | Commonwealth Electoral Act s 93 | `NONE` |
| 2050-06-30 | Jarrah sold; her interests bought out | ESS tax; the discount | ITAA 1997 Divs 83A, 115 | `NONE` |
| 2052-08-19 | Graham dies at home | Who registers; the cremation permit; not reportable | BDMR Act Part 6; Cremation Act 1929 (WA) ss 7-8; Coroners Act 1996 (WA) s 17 | `NONE` |
| 2052-08-25 | his will; probate; the house; the super | — | Wills Act ss 8, 13; Administration Act 1903 (WA) s 25, Part IV; Transfer of Land Act s 60; ITAA 1997 Div 302 | `NONE`; no inheritance tax `CASE` |
| 2060-01-27 | Sue dies intestate | Who takes? | Administration Act s 14, s 25 | `NONE` — half each |

## Chapter 9 — Retirement and old age (2063–2088)

Preservation age at sixty and enduring guardians. Retirement at sixty-three with an account-based pension, tax-free from a taxed fund. The Age Pension refused at sixty-seven on assets. Baldivis sold at sixty-seven and a downsizer contribution each into super, a strata apartment in Mandurah. An advance health directive at seventy. Liam dies at eighty-three. A Support at Home package after an aged care assessment. Chloe dies at eighty-five; the will to the children, probate, the super taxed to adult children, the cremation, and no duty of any kind.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2063-03-14 | turns 60 | The condition of release | SIS Regulations Sch 1 | `NONE` |
| 2063-03-14 | enduring guardians | What may a guardian decide? | Guardianship and Administration Act Part 9A | `NONE` |
| 2066-03 | retires at 63 | Is the pension taxed? | ITAA 1997 Div 301; Age Discrimination Act 2004 (Cth) | `NONE` |
| 2070-03-14 | turns 67 | Age Pension? | Social Security Act ss 43, 1064 | `NONE` — no |
| 2070-05 | Baldivis sold; Mandurah; downsizer contributions | The contribution; the duty; the strata company | ITAA 1997 s 292-102; Duties Act; Strata Titles Act 1985 (WA) Part 7 | `NONE` |
| 2073-03 | advance health directive | — | Guardianship and Administration Act Part 9B | `NONE` |
| 2083-02-09 | Liam dies | Registration; will; survivorship; super | BDMR Act Part 6; Wills Act s 8; Administration Act s 25; Transfer of Land Act s 60; ITAA 1997 Div 302 | `NONE` |
| 2085-06 | Support at Home | Who assesses; what is subsidised? | Aged Care Act 2024 (Cth) Chs 2, 4 | `NONE` |
| 2088-11-02 | Chloe dies | Registration; probate; the super to adult children; any duty? | BDMR Act Part 6; Wills Act s 8; Administration Act s 25; ITAA 1997 Div 302; Cremation Act s 7 | `NONE`; no inheritance tax `CASE` |

---

## What the scenario touches

Seventy-two subjects: thirty-four Commonwealth and thirty-eight Western Australian. On 13 October 2026 none has an encoding row. Against Simone's life the shape is the same and the content shifts: twelve of her Singapore Acts have no Western Australian counterpart (national service, the NRIC, CareShield, the executive condominium regime, the additional buyer's duty, Silver Support, the Child Development Account), and twelve things here have no Singapore counterpart (the first home owner grant, the jury summons, the Child Care Subsidy, the Lifetime Health Cover loading, the dividing fence, the downsizer contribution, compulsory enrolment at eighteen, the funeral director's duty to register a death).

The largest early demands on the library, by how often this life asks them: the Fair Work Act (fourteen events), the Income Tax Assessment Act 1997 (eleven), the Family Assistance Act (seven), the Superannuation Guarantee and SIS Acts (eight between them), the Births, Deaths and Marriages Registration Act (seven), the Duties Act (five). [`GAPS.md`](GAPS.md) ranks them.

## Sample prompts for the chat demo

1. "My payslip says super 11%. Is that right, and when does it go up?" — Superannuation Guarantee (Administration) Act s 19, with the 1 July steps.
2. "Do I have to lodge a return for last year?" — ITAA 1997 and the Rates Act: nil tax under the threshold, but a return is still due.
3. "We're building in Byford. Do we get the grant, and is there stamp duty?" — First Home Owner Grant Act; Duties Act first home owner rate.
4. "We lodged the notice with the celebrant on 10 April. How soon can we marry?" — Marriage Act s 42: one month.
5. "How many weeks of Paid Parental Leave, and who pays it?" — PPL Act: 24 weeks, through the employer.
6. "What do we get for the baby?" — Family Assistance Act: Newborn Upfront, Newborn Supplement, FTB on the family income.
7. "I turned 31 in March. Should I get hospital cover?" — Private Health Insurance Act Div 34: before 1 July.
8. "I've been summonsed for jury duty. Can my boss say no?" — Juries Act ss 58B-58C; Fair Work Act s 111.
9. "Do we have to register the dog?" — Dog Act ss 15-16; the shire.
10. "Dad's 67. Does he get the pension?" — Social Security Act ss 43, 1064: assets test.
11. "Dad died at home last night. What do we have to do?" — BDMR Act Part 6: the doctor and the funeral director; the Cremation Act permit.
12. "Mum had no will. Who gets the house?" — Administration Act s 14.
13. "Can I take my super now I'm 60?" — SIS Regulations: a condition of release.
14. "We're selling the townhouse. Can we put the money into super?" — ITAA 1997 s 292-102.
15. "Is there death duty?" — none since 1979; the super to adult children is taxed under Div 302.
