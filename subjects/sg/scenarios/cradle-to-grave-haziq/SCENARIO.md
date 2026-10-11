# Scenario: cradle to grave — Muhammad Haziq bin Abdul Rahman (Sim Three, the overachiever)

Born in 1996 to a taxi driver and a clinic assistant in Bedok, seven years before Simone and ten before Jun Hao, and into their lives only in 2034, when Simone joins his company and her brother is the night officer in its building. An officer in national service, a lawyer, a founder, an employer, a candidate, an acquirer, a seller, a philanthropist, a director, an investor. Married under Muslim law to a Malaysian who becomes a citizen; a daughter born in London who is a citizen by descent; an estate divided at the end by faraid, a wasiat and a nomination. He does, by design, what the other two never do, and his life runs on a second body of personal law that the statute book applies by reference.

The third and last cradle-to-grave scenario. Simone's is the sunny day; Jun Hao's is the life off the path; this one is the life that makes the law work for others: the employer's side of the Employment Act and the Child Development Co-Savings Act, the company's side of the Companies Act and the GST Act, the organisation's side of the PDPA, the candidate's side of the Parliamentary Elections Act, the donor's side of the Charities Act, and the Administration of Muslim Law Act from birth to death.

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — twenty beats, two a chapter, with ages.
- [`GAPS.md`](GAPS.md) — what this life needs that the library does not hold, and the seams with the other two scenarios.
- [`facts.json`](facts.json) — the cast and 64 dated events with their law, status, ages and the twenty beats.
- [`check-status.py`](check-status.py) — re-derives the status column from the tree.

## Design rules

The same as the other two scenarios, with these particulars.

1. **One "now".** 12 October 2026: Haziq is thirty, a senior associate and a commissioner for oaths, married two years, his wife's permanent residence granted last month. Everything from 2031 on is live.
2. **Current law, replayed**, as in the other two; and the Administration of Muslim Law Act applies Muslim law by reference, so a status of `CASE` here also covers religious law the Act does not restate.
3. **Six status words**, read from the tree on 12 October 2026 and agreeing with it.
4. **Sunny, in business.** No fraud, no winding up, no disciplinary proceeding, no divorce, no litigation that is not settled. The one dispute is mediated; the one defamation ends in an apology; the retrenchment is lawful and the data breach is reported in time.
5. **Shared cast.** From 2034 he is Simone's employer, and Jun Hao's fall in 2053 happens in his company's building. Those two files have been changed to match, and `GAPS.md` section F records what.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Muhammad Haziq bin Abdul Rahman** | 9 Apr 1996, KKH | the main character | citizen by birth; dies 21 Oct 2078 |
| Nadia binti Yusof | 23 Aug 1997 | his wife from 30 Nov 2024 | Malaysian; LTVP 2024, PR 2026, citizen by registration 2033 |
| Aisyah binte Haziq | 14 Jun 2027, London | their daughter | citizen by descent |
| Imran bin Haziq | 2 Feb 2030, Singapore | their son | citizen by birth |
| Abdul Rahman bin Osman, Rohana binte Ismail | 1968, 1970 | his parents | Bedok 4-room, joint tenants; he dies 2052, she 2069, both intestate |
| Nurul Aini | 1999 | his sister | a nurse; an heir twice |
| Tan & Partners LLC | — | his firm 2021 to 2031 | a law corporation |
| Lexi Technologies Pte Ltd | — | his company 2031 to 2050 | Simone's employer from 2034 |
| an angel; a venture fund; Formly Pte Ltd; a listed buyer | — | investors, a target, an acquirer | |
| Rahman Foundation Ltd | — | his charity from 2051 | company limited by guarantee |

---

## Chapter 0 — Born (1996)

Registered on day nine. The first deduction his father's payslip ever showed for him was not CPF but the Mosque Building and Mendaki Fund, which the Act collects through CPF from Muslim employees unless they opt out.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 1996-04-09 | birth at KKH | Citizen by birth? | Constitution Art 121 | `ENC` |
| 1996-04-18 | registered and named | — | Registration of Births and Deaths Act 2021 ss 7, 8, 10 | `ENC` (replayed) |
| 1996-05 | his father's MBMF deduction | Who contributes, how much, how to opt out? | Administration of Muslim Law Act 1966 ss 78-79, Third Schedule | `ENC` |

## Chapter 1 — School and the scholarship (2003–2014)

Primary 1 in 2003, an Edusave scholarship after the PSLE, an Integrated Programme school, NRIC at fifteen, national service registration at sixteen and a half, A-levels in 2014.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2003-01-02 | Primary 1 | — | Compulsory Education Act 2000 s 3 | `ENC` |
| 2008-11-20 | PSLE; an Edusave scholarship | What is the scholarship, who awards it? | Education Endowment and Savings Schemes Act 1992 ss 7-9; the scholarship criteria | `PART` (the row holds the PSEA provisions); `ADMIN-POLICY` |
| 2011-04-09 | NRIC at 15 | — | National Registration Act 1965 s 6 | `ENC` |
| 2012-10-15 | registers for NS | — | Enlistment Act 1970 ss 2, 12 | `ENC` |
| 2014-11-28 | A-levels | — | — | — |

## Chapter 2 — Officer and law student (2015–2021)

Enlisted in February 2015, commissioned in November, operationally ready in January 2017 and a platoon commander in reserve for the next decade, which makes him a key appointment holder for the relief. NUS Law from 2017, fees partly from his Post-Secondary Education Account. The Bar course in 2021.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2015-02-09 | enlists; Officer Cadet School | What law governs him in uniform? | Singapore Armed Forces Act 1972 ss 3-4, 11; Enlistment Act s 10 | `ENC`; `PART` |
| 2017-01-08 | operationally ready; a reservist officer | His liability; what an employer must do | Enlistment Act ss 13-15, 21-23; National Servicemen (Employment) Act 1970 ss 4-9 | `ENC` |
| 2017-08-07 | NUS Law; PSEA pays part of the fees | May the account pay for a degree, who withdraws? | EESS Act ss 20, 22; NUS (Corporatisation) Act 2005 | `ENC`; `NONE` |
| 2019-09-16 | in-camp training as platoon commander | The key appointment holder's relief | Income Tax Act 1947 s 39(2)(l) | `ENC` |
| 2021-05-30 | LLB; Part B | — | Legal Profession Act 1966 Part 2A | `PART` |

## Chapter 3 — The Bar, a marriage under Muslim law, London (2021–2029)

A training contract, admission in August 2022, a practising certificate every year after. In November 2024 he marries Nadia before a Kadi, her father as wali; she comes on a long-term visit pass and is granted permanent residence in 2026. He is appointed a commissioner for oaths in 2026. A year in London in 2027, where Aisyah is born and registered as a citizen by descent at the High Commission. A condominium in 2028 in both names, where the additional duty follows the PR's profile. A conditional fee agreement in an arbitration in 2029.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2021-07-05 | training contract | — | Legal Profession Act Part 2A; Employment Act Part 2 | `PART`; `ENC` |
| 2022-08-23 | called to the Bar; practising certificate | Who may practise; what may an unauthorised person not do? | LPA ss 32-34; s 25 | `ENC` for ss 32-34; `PART` for s 25 |
| 2024-11-30 | marries Nadia before a Kadi | Who may solemnise; whose consent; a foreign bride? | AMLA ss 94B-97, Fourth Schedule | `ENC` |
| 2024-12-10 | Nadia's LTVP; PR in 2026 | Who decides, and on what? | Immigration Act 1959 (the Controller's discretion); ICA's PR framework | `PART`; `ADMIN-POLICY` |
| 2026-06-01 | commissioner for oaths | Who may administer an oath? | Oaths and Declarations Act 2000 ss 4-6, 8, 11-12 | `ENC` |
| 2027-01-09 | London; Nadia's re-entry permit | What keeps a PR's status abroad? | Immigration Act ss 11, 14A | `ENC` |
| 2027-06-14 | Aisyah born in London | A citizen by descent? By when registered? | Constitution Art 122; Passports Act s 27 | `ENC` |
| 2028-03-15 | a condominium, $1,600,000, citizen and PR | Restricted property? Duty, and whose profile sets it? | Residential Property Act 1976 ss 2-4; Stamp Duties Act Art 3(a)(iv), (bi) | `ENC` — BSD $44,600; ABSD at the PR's 5%, $80,000 |
| 2029-03-04 | a conditional fee in an arbitration | Lawful? Binding arbitration agreement? | LPA ss 107, 115B; Arbitration Act 2001 ss 4, 6, 12-15 | `ENC` |

## Chapter 4 — Founding Lexi (2030–2034)

Imran is born in February 2030; four weeks of paternity leave. Haziq leaves practice in February 2031 and incorporates Lexi Technologies in March, seventy per cent his, ten Nadia's, twenty an angel's for half a million. Three employees in June, and with them every duty an employer carries from day one. Standard terms in July. The LEXI mark, the code and a patent application in September. An Employment Pass for an engineer from Chennai in 2032. GST registration when turnover passes a million in 2033; the start-up exemption in the first corporate return. Nadia becomes a citizen in July 2033. In February 2034 Simone joins at $6,800 with options, and the night officer in the building is her brother; in April the company claims back her childcare leave from the Government.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2030-02-02 | Imran born; Baby Gift; paternity leave | — | Constitution Art 121; child-support row; CDCSA ss 12H-12J | `ENC` |
| 2031-02-28 | leaves practice | Notice; what he may not do once the certificate lapses | Employment Act ss 10-11; LPA s 33 | `ENC` |
| 2031-03-15 | incorporates Lexi | What is a company, a subsidiary, an interest in shares, an auditor? Is a placement to one investor exempt? | Companies Act 1967 ss 4-7, 10; ss 19, 157; ACRA Act 2004; Securities and Futures Act 2001 Part 13 | `ENC` for the definitional core; `PART` for incorporation, directors' duties, filings and the placement exemption |
| 2031-06-01 | first three employees | What does an employer owe from day one? | Employment Act Parts 2-4; CPF Act s 7; SDL Act s 3; WICA s 24; WSH Act s 12; NS (Employment) Act ss 4-9 | `ENC` throughout, except WSH s 12 `PART` |
| 2031-07-10 | standard terms of service | A reasonable liability cap; no third-party rights; a click as a signature | Unfair Contract Terms Act 1977 ss 2-3, 11; Contracts (Rights of Third Parties) Act 2001 ss 2, 3, 7; Electronic Transactions Act 2010 ss 7-8, 11; Misrepresentation Act 1967 ss 2-3 | `ENC` |
| 2031-09-01 | the LEXI mark; the code; a patent application | Duration of a mark; ownership of employees' code; patentability | Trade Marks Act 1998 ss 18, 27; Copyright Act 2021 (works made in employment); Patents Act 1994 ss 13-16 | `ENC`; `PART`; `ENC` |
| 2032-02-01 | an Employment Pass | May a foreigner work without a pass; who applies; what salary? | Employment of Foreign Manpower Act 1990 ss 5, 9-12; the qualifying salary and COMPASS | `ENC`; `ADMIN-POLICY` |
| 2032-06-30 | a business survey | Must a company answer? | Statistics Act 1973 ss 5-6 | `ENC` |
| 2033-01-01 | GST registration at $1,000,000 | When, and from when does it charge? | GST Act 1993 s 8, First Schedule para 1 | `ENC` |
| 2033-07-20 | Nadia a citizen by registration | Who may be registered; what must she give up? | Constitution Arts 123, 126; renunciation of Malaysian citizenship | `ENC`; `CASE` |
| 2033-11-30 | first corporate return | The rate; the start-up exemption | ITA s 43 | `ENC` |
| 2034-02-01 | Simone joins; Jun Hao on the night desk | Options at exercise; the agency's licence | ITA s 10(6); Private Security Industry Act 2007 ss 3, 5-6 | `ENC` |
| 2034-04-14 | Lexi claims Simone's childcare leave from the Government | What may an employer claim back, by when? | CDCSA ss 12C, 12CA | `ENC` |

## Chapter 5 — A round, a breach, a house (2035–2039)

A Series A in 2035: five million for a quarter, and the fund is a substantial shareholder. A customer dispute mediated and recorded as a court order. In April 2036 a breach exposes 1,200 users' email addresses; it is notifiable, and the Commission is told within three days. A licensed penetration tester afterwards. Imran starts school. In 2038 the condominium is sold and a freehold terrace bought in both names, which two citizens may own; no additional duty, because they sold first. A competitor trading as LEXIE receives a letter and rebrands.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2035-09-01 | Series A | An interest in shares; a substantial shareholder; the allotment | Companies Act s 7; ss 81, 161; a shareholders' agreement | `ENC`; `PART`; `CASE` |
| 2035-11-12 | a mediated settlement as a court order | Enforceable as a judgment? | Mediation Act 2017 ss 4, 12 | `ENC` |
| 2036-04-03 | a data breach, 1,200 users | Notifiable? By when? Must users be told? | PDPA Part VIA with the Regulations; ss 13-16, 24-26 | `ENC` (both PDPA rows) |
| 2036-06-20 | a licensed penetration tester | A licensable cybersecurity service? | Cybersecurity Act 2018 s 2, Second Schedule, Part 5 | `ENC` |
| 2037-01-04 | Imran, Primary 1 | — | Compulsory Education Act s 3 | `ENC` |
| 2038-05-20 | the terrace, $4,200,000, both citizens | May they own landed property? Seller's duty after ten years? Buyer's duty? | Residential Property Act s 3; SDA Art 3(a)(iv), (bg), (bi), (bj) | `ENC` — SSD nil, BSD $191,600, ABSD nil |
| 2039-02-11 | LEXIE | Infringement? | Trade Marks Act ss 27-28 | `ENC` |

## Chapter 6 — The candidate and the acquirer (2040–2045)

Nominated in the 2040 general election, deposit paid; a false post about his company during the campaign, corrected and apologised for; forty-one per cent on polling day and the deposit returned. In 2042 Lexi buys back the angel's shares on a directors' solvency statement. In 2043 it acquires Formly, with duty on the share transfer and a merger small enough not to lessen competition. In 2045 twelve staff are retrenched after the acquisition, lawfully, with notice, benefit and notification.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2040-06-23 | nominated; deposit paid | Who may stand; the deposit; forfeiture; expenses | Parliamentary Elections Act 1954 ss 28, 61; Constitution Arts 44-45 | `ENC` |
| 2040-06-30 | a false post; an apology | Defamatory? What does an apology do? | Defamation Act 1957 ss 2-15 | `ENC` |
| 2040-07-04 | 41%; deposit returned | — | PEA s 28 | `ENC` |
| 2042-03-31 | buy-back of the angel's shares | The solvency statement and its offence | Companies Act s 7A; s 76B | `ENC`; `PART` |
| 2043-06-15 | Formly acquired | Duty on shares; a substantial lessening of competition? | SDA Art 3(c); Competition Act 2004 s 54, Fourth Schedule; Companies Act ss 5-6 | `ENC` |
| 2045-10-31 | twelve staff retrenched | What is owed; whom must the employer tell? | Employment Act ss 10-11, 45; s 96A; the Tripartite Advisory | `ENC`; `PART`; `ADMIN-POLICY` |

## Chapter 7 — Exit, foundation, boards (2048–2052)

Imran enlists in 2048. In June 2050 Lexi is sold to a listed buyer for forty million; duty on the transfer, no tax on a capital gain, and Simone's options are bought out and taxed as hers. In 2051 the Rahman Foundation is registered as a charity and receives two million, deductible at two and a half times; he joins a listed board, inside the trading windows. In November 2052 his father dies without a will, and a Muslim estate is divided by faraid: his mother an eighth, himself and his sister two to one, except that the flat passes to his mother by survivorship and the CPF by nomination, both outside the division.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2048-08-10 | Imran enlists | — | Enlistment Act s 10 | `PART` |
| 2050-06-30 | Lexi sold, $40,000,000; options bought out | Duty on the transfer; a capital gain; Simone's options | SDA Art 3(c); ITA s 10(1)(g) and s 10(6) | `ENC` — the capital/income line is a fact the row takes as input |
| 2051-03-01 | the Foundation; $2,000,000 | Must a charity register; the donor's deduction | Charities Act 1994 ss 7, 13; ITA s 37; a company limited by guarantee; IPC status | `ENC`; `ENC`; `PART`; `ADMIN-POLICY` |
| 2051-09-01 | an independent director | What may an insider not do? | Securities and Futures Act Part 12 Divisions 1, 3, 4; Companies Act s 157 | `ENC`; `PART` |
| 2052-11-03 | his father dies intestate | Faraid shares; the flat; the CPF | AMLA ss 112, 115; Muslim law; CPF Act s 25; survivorship and nomination against faraid | `PART`; `CASE`; `ENC`; `CASE` |

## Chapter 8 — Investor, elder (2053–2069)

The night officer's fall in his company's building in 2053 raises the question the two scenarios share: the agency is the employer and liable under the Act; the tenant is an occupier under the safety Act. Angel investments as an accredited investor. The listed board until sixty-two. CPF LIFE at sixty-five and no Silver Support. Property tax on the terrace. A lasting power of attorney and a wasiat of one third to the Foundation at sixty-nine. His mother dies in 2069 and the Bedok flat is divided two to one.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2053-10-05 | Jun Hao's fall in the building | The employer's liability, or the occupier's? | WICA s 7 (Sentinel); WSH Act s 11 (occupier) | `ENC`; `PART` |
| 2056-03-20 | angel investments | Who is an accredited investor? | SFA s 4A; convertible notes | `PART`; `CASE` |
| 2058-04-09 | leaves the board at 62 | — | — | — |
| 2061-04-09 | turns 65 | CPF LIFE; Silver Support? | CPF Act Part 3A; Silver Support Scheme Act ss 6-7 | `PART`; `ENC` (no) |
| 2062-01-15 | property tax on the terrace | The owner-occupier rate on $96,000 | Property Tax Act ss 6, 9; the rate order | `ENC`; `REGS` |
| 2065-04-09 | LPA to Nadia; a wasiat of one third | What may a Muslim will give, to whom? | Mental Capacity Act ss 11-13; AMLA s 111; the one-third rule | `ENC`; `PART`; `CASE` |
| 2069-01-30 | his mother dies | Son and daughter, two to one | AMLA ss 112, 115; faraid | `PART`; `CASE` |

## Chapter 9 — Wasiat, faraid, the end (2070–2078)

An advance medical directive at seventy-eight. The Foundation's trustees succeed him. He dies in October 2078; the Human Organ Transplant Act's presumption applies to a Muslim who did not opt out. The estate goes in order: one third to the Foundation by wasiat, the house to Nadia by survivorship, the CPF to her by nomination, and the residue by faraid: an eighth to the widow, and of the rest two parts to Imran and one to Aisyah. No estate duty.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2074-06-12 | advance medical directive | — | Advance Medical Directive Act 1996 ss 3-9 | `ENC` |
| 2076-05-03 | the Foundation's trustees succeed him | What may a trustee delegate? | Trustees Act 1967 ss 41B, 41N; Charities Act ss 19-20 | `ENC` |
| 2078-10-21 | dies at 82 | Does the presumption apply; who registers? | HOTA s 5; RBDA ss 19-23 | `ENC` |
| 2078-11-15 | the estate | In what order, in what shares? | AMLA ss 111, 112, 115; faraid; CPF Act s 25; survivorship; Estate Duty Act s 2A | `PART`; `CASE`; `ENC`; `CASE`; `ENC` |

---

## What the scenario touches

Fifty-four subjects. Against the other two lives: twenty-four are his alone, among them the Administration of Muslim Law Act, the Legal Profession Act, the Oaths and Declarations Act, the Arbitration and Mediation Acts, the Companies and ACRA Acts, the Securities and Futures Act, the Trade Marks, Copyright and Patents Acts, the Employment of Foreign Manpower Act, the Unfair Contract Terms, Third Parties and Misrepresentation Acts, the Electronic Transactions and Cybersecurity Acts, the Competition Act, the Charities and Trustees Acts, the Defamation Act, the Residential Property Act, and the GST Act on the registrant's side. The three lives together touch a hundred and seventeen subjects.

- **ENC on at least one question**: 50 subjects, counting the Constitution and the child-support row.
- **PART on at least one question**: Legal Profession (admission, the practising certificate), Companies (incorporation, directors' duties, allotment, buy-back, the guarantee company), ACRA (filings), Securities and Futures (placement exemption, accredited investor), Copyright (works made in employment), Immigration (the grant of a pass and of residence), Workplace Safety and Health (ss 11-12), Employment (s 96A), Education Endowment (Edusave), Enlistment (s 10), CPF (CPF LIFE), and the Administration of Muslim Law Act on inheritance (ss 111, 112, 115).
- **NONE**: NUS (Corporatisation) Act 2005.

The largest hole in this life is Muslim law itself. The Act applies it by reference for marriage, which the row carries, and for wills and inheritance, which it does not; the faraid shares that decide two estates in this life are religious law applied by statute, stated in no row and in no instrument. [`GAPS.md`](GAPS.md) sets out how a row for it might be filed.

## Sample prompts for the chat demo

1. "I've just been called. What may I do now that I couldn't yesterday?" — LPA ss 32-34, and the row stops at the practising certificate.
2. "Nadia's father will be the wali. Who else needs to consent?" — AMLA ss 94B-97, Fourth Schedule.
3. "Our daughter was born in London. Is she Singaporean?" — Art 122, and the registration deadline.
4. "We're buying a condo together. Which of us sets the additional duty?" — SDA Art 3(bi): the PR's profile, five per cent of the whole price.
5. "I'm hiring three people on Monday. What do I owe them from day one?" — Employment Act, CPF s 7, the levy, WICA s 24, and the reservist release.
6. "Can I cap our liability at the subscription fee?" — UCTA s 3 and the reasonableness test.
7. "We've crossed a million. When do I start charging GST?" — First Schedule para 1.
8. "Twelve hundred email addresses leaked last night. Do I tell the Commission?" — PDPA Part VIA: yes, within three days.
9. "A competitor is calling itself LEXIE." — Trade Marks Act s 27.
10. "I want to stand in the election. What happens to the deposit if I lose?" — PEA s 28: forfeited below one eighth of the vote.
11. "We're buying Formly. Do we have to tell the competition authority?" — Competition Act s 54.
12. "Is the gain on selling Lexi taxed?" — ITA s 10(1)(g): depends on the capital/income line, which the row takes as a fact.
13. "Dad died without a will. Mum, my sister and I: who gets what?" — AMLA s 112 applies faraid, which no row holds; the assistant quotes the Act and stops.
14. "Can my will leave a third to the Foundation?" — AMLA s 111 and the one-third rule: outside the row.
15. "Does the organ donation presumption apply to Muslims?" — HOTA s 5: yes, since the 2008 amendment, unless he opted out.
