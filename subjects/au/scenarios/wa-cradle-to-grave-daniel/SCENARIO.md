# Scenario: cradle to grave — Daniel Rossi (WA Sim Three, the overachiever)

Haziq's life, moved to Perth. Born in 1996 to a bricklayer from Calabria and a bookkeeper in Spearwood, and into Chloe's and Jake's lives only in 2034, when she joins his company and he guards its tower. A commerce degree and a Juris Doctor on HECS and FEE-HELP, admission by the Supreme Court, a practising certificate under the Uniform Law, an authorised witness, a year in London, a founder, an employer, a candidate who must first renounce the Italian citizenship he was born with, an acquirer under the new mandatory merger regime, a seller with a capital gains discount, a private ancillary fund, a listed board, an angel. Married by a civil celebrant to an Indian national who comes on a partner visa, becomes a permanent resident and then a citizen, and gives up her Indian citizenship because India allows no other way. A daughter born in London who is a citizen by descent. And at the end, an estate that four rules divide: the house by survivorship, the super by nomination, the residue by a will into a testamentary trust, and, when his father dies, a house in Calabria that Italian law divides for the family whatever the Australian will says.

Where Haziq's life ran on a second personal law applied by statute, Daniel's runs on three things Singapore does not have: a federal Constitution that disqualifies a dual citizen from Parliament, a foreign law that reaches into an Australian estate, and a Privacy Act that does not apply to his company until it is big enough.

Companion files:

- [`ABRIDGED.md`](ABRIDGED.md) — twenty beats, two a chapter, with ages.
- [`GAPS.md`](GAPS.md) — the encoding order this life sets, and the seams with Chloe's and Jake's files.
- [`facts.json`](facts.json) — the cast and 63 dated events with their law and status, ages at every event, the twenty beats flagged.
- [`check-status.py`](check-status.py) — re-derives the status column from the tree.

## Design rules

As for Chloe's and Jake's. Two particulars.

1. **One "now".** 13 October 2026: Daniel is thirty, a senior associate, an authorised witness, married two years, his wife's permanent visa three months away.
2. **The adjudicator's side.** Eight events here are the company's and employer's view of events in Chloe's file: her hiring, her share scheme, her parental leave paid through the company, the redundancies she survives, the sale that pays her out. The same Acts, asked the other way round. Jake's fall in 2053 is the occupier's question in this file and the employer's in his.

## The cast

| person | born | role | notes |
| --- | --- | --- | --- |
| **Daniel Rossi** | 9 Apr 1996, KEMH | the main character | Australian by birth, Italian by descent until 2040; dies 21 Oct 2078 with a will |
| Priya Nair | 23 Aug 1997 | his wife from 30 Nov 2024 | Indian; student visa, partner visa 2025, permanent 2027, citizen by conferral 2030 |
| Anjali Rossi | 14 Jun 2027, London | their daughter | citizen by descent |
| Luca Rossi | 2 Feb 2030, Perth | their son | citizen by birth |
| Giuseppe and Maria Rossi | 1968, 1970 | his parents | he owns a house in Reggio Calabria; dies 2052; she dies 2069 |
| Sofia Rossi | 1999 | his sister | a nurse; an heir twice |
| Swan & Partners | — | his firm 2020 to 2031 | |
| Jarrah Legal Technologies Pty Ltd | — | his company 2031 to 2050 | Chloe's employer from 2034 |
| a sophisticated investor; a venture fund; Formly Pty Ltd; an ASX-listed buyer | — | investors, a target, an acquirer | |
| the Rossi Foundation | — | a private ancillary fund from 2051 | |

---

## Chapter 0 — Born (1996)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 1996-04-09 | birth at KEMH | Australian by birth? And Italian? | Australian Citizenship Act 2007 (Cth) s 12; Italian Law 91/1992 (descent) | `NONE`; `CASE` |
| 1996-04-18 | registered; and at the consulate | — | BDMR Act 1998 (WA) ss 12-13 | `NONE` |
| 1996-05 | family payments; Medicare | — | Family Assistance Act 1999 (Cth) Part 3 (replayed); Health Insurance Act 1973 (Cth) s 3 | `NONE` |

## Chapter 1 — School (2003–2013)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2003-02 | Year 1 | — | School Education Act 1999 (WA) s 9 | `NONE` |
| 2008-11 | a Gifted and Talented place | Who decides? | Department selective entry policy | `ADMIN-POLICY` |
| 2012-10 | 16: learner's permit; TFN; a casual job | — | Road Traffic (Authorisation to Drive) Act 2008 (WA) s 8; Taxation Administration Act 1953 (Cth) Part VA | `NONE` |
| 2013-11-28 | ATAR 99.5 | — | — | — |

## Chapter 2 — Commerce, the JD, admission (2014–2019)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2014-02 | Bachelor of Commerce; HECS-HELP; Youth Allowance refused | What is deferred; the parental income test | Higher Education Support Act 2003 (Cth) Part 3-2; Social Security Act 1991 (Cth) Part 2.11 | `NONE` |
| 2014-04-09 | turns 18: enrols; organ donor register; votes | — | Commonwealth Electoral Act 1918 (Cth) ss 93, 101, 245; Human Tissue and Transplant Act 1982 (WA) s 22 | `NONE` |
| 2017-02 | Juris Doctor; FEE-HELP | Is a postgraduate law degree Commonwealth-supported? | HESA Parts 2-2, 3-3; University of Western Australia Act 1911 (WA) | `NONE` |
| 2019-12 | graduates; Practical Legal Training | — | Legal Profession Uniform Law Application Act 2022 (WA): the Uniform Law Part 2.2 and the Admission Rules (replayed; the 2008 Act applied in 2020) | `NONE` |

## Chapter 3 — The Bar, a civil celebrant, London (2020–2029)

Admission by the Supreme Court in August 2020 and a practising certificate every year. A Notice of Intended Marriage, a civil celebrant, and a Hindu ceremony the week after with no legal effect. Priya's partner visa, temporary then permanent, and a resident return visa for the London year. Authorised to witness statutory declarations and affidavits by virtue of his certificate. Anjali born in London and registered as a citizen by descent at Australia House. An apartment in East Perth in both names: a permanent resident is not a foreign person, so no foreign investment approval and no foreign buyer duty, and duty at the general rate. A conditional costs agreement with an uplift, which the Uniform Law allows, in an arbitration, which the state's Act governs.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2020-02 | graduate at Swan & Partners | — | Fair Work Act 2009 (Cth) Part 2-2 | `NONE` |
| 2020-08-24 | admitted; practising certificate | Who may practise; what is unqualified practice? | Uniform Law ss 10, 16-25, 43-49, as applied in WA | `NONE` |
| 2024-10-28 | Notice of Intended Marriage; a civil celebrant; a Hindu ceremony | What makes the marriage valid; does the religious ceremony add anything? | Marriage Act 1961 (Cth) ss 42, 45, 48 | `NONE` — nothing legally |
| 2025-01-10 | Priya's partner visa | On what basis; what bridging visa between? | Migration Act 1958 (Cth) ss 29, 65; the Regulations (subclass 820/801) | `NONE`; `REGS` |
| 2026-06-01 | an authorised witness | Who may witness a statutory declaration? | Oaths, Affidavits and Statutory Declarations Act 2005 (WA) ss 8-9, 12; Statutory Declarations Act 1959 (Cth) s 8 | `NONE` |
| 2027-01-09 | London; a resident return visa | What does a permanent resident need to leave and return? | Migration Act s 29; subclass 155 | `NONE` |
| 2027-06-14 | Anjali born in London | A citizen by descent, by what step? | Australian Citizenship Act s 16; Australian Passports Act 2005 (Cth) s 11 | `NONE` |
| 2028-03-15 | East Perth, $1,600,000, citizen and PR | A foreign person? Foreign buyer duty? Duty at the general rate? | Foreign Acquisitions and Takeovers Act 1975 (Cth) ss 4, 47; Duties Act 2008 (WA) Ch 2 Parts 3B, 5; Strata Titles Act 1985 (WA) Part 7 | `NONE` — about $73,515; no surcharge; no approval |
| 2029-03-04 | a conditional costs agreement; an arbitration | Lawful? What is prohibited? Binding? | Uniform Law ss 181, 183; Commercial Arbitration Act 2012 (WA) ss 7-8 | `NONE` |

## Chapter 4 — Founding Jarrah (2030–2034)

Luca born in Perth. Priya a citizen by conferral in July 2030, after four years' residence, and an OCI card in place of the Indian citizenship she must give up. Daniel leaves practice with a restraint clause the common law will test if it ever has to. Jarrah registered with ASIC in March 2031, seventy per cent his, ten Priya's, twenty a sophisticated investor's under the small-scale exemption; an ABN; a business name; a director identification number. Three employees in June, with superannuation at twelve per cent, workers' compensation insurance, the primary duty of care, no payroll tax under the state threshold, and no Privacy Act under three million of turnover. Standard terms reviewed against the unfair contract terms regime, which now reaches small-business contracts with penalties. The JARRAH mark, the code the company owns by statute, a patent application whose fate the cases decide. A Skills in Demand visa and sponsorship obligations. GST registration at seventy-five thousand and the R&D tax incentive. A base rate entity at twenty-five per cent. Chloe joins in 2034 with start-up scheme interests; Sentinel's night officer is her brother; the company becomes the paymaster of her Paid Parental Leave.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2030-02-02 | Luca born | — | Australian Citizenship Act s 12; PPL Act 2010 (Cth); Family Assistance Act | `NONE` |
| 2030-07-20 | Priya a citizen by conferral | The residence requirement; what she gives up | Australian Citizenship Act ss 21-22, 26; Indian Citizenship Act 1955 s 9 and the OCI scheme | `NONE`; `CASE` |
| 2031-02-28 | leaves practice | Notice; a 12-month restraint | Fair Work Act s 117; restraint of trade | `NONE`; `CASE` |
| 2031-03-15 | Jarrah registered | What registration needs; directors' duties; the small-scale exemption | Corporations Act 2001 (Cth) ss 117, 180-184, 708, 1272C; ASIC Act 2001 (Cth) Part 2; ABN Act 1999 (Cth) s 8; Business Names Registration Act 2011 (Cth) s 18 | `NONE` |
| 2031-06-01 | first three employees | What an employer owes from day one; which laws do not yet reach it | Fair Work Act Parts 2-2, 2-3, s 536; SG (Administration) Act 1992 (Cth) ss 16, 19; Workers' Compensation and Injury Management Act 2023 (WA) Part 8; Work Health and Safety Act 2020 (WA) s 19; Pay-roll Tax Assessment Act 2002 (WA) Part 2; Privacy Act 1988 (Cth) s 6D | `NONE` |
| 2031-07-10 | standard terms | An unfair term? Guarantees excluded? A click a signature? | Competition and Consumer Act 2010 (Cth) Sch 2 Part 2-3, ss 54, 64; Electronic Transactions Act 1999 (Cth) ss 9-10 | `NONE` |
| 2031-09-01 | the mark; the code; the patent | Registration period; who owns employees' code; patentable? | Trade Marks Act 1995 (Cth) ss 72, 120; Copyright Act 1968 (Cth) s 35(6); Patents Act 1990 (Cth) s 18; the cases on computer-implemented inventions | `NONE`; `CASE` |
| 2032-02-01 | a Skills in Demand visa; sponsorship | Work without a visa; the sponsor's obligations; the salary threshold | Migration Act ss 140E-140H, 235; the Regulations | `NONE`; `REGS` |
| 2032-06-30 | a business survey | Must a company answer? | Census and Statistics Act 1905 (Cth) s 14 | `NONE` |
| 2032-10-01 | GST at $75,000; the R&D incentive | When to register; the refundable offset | GST Act 1999 (Cth) ss 23-5, 23-15; ITAA 1997 (Cth) Div 355 | `NONE` |
| 2033-11-30 | first company return | The rate; losses | Income Tax Rates Act 1986 (Cth) s 23; ITAA 1997 Div 36 | `NONE` — 25% |
| 2034-02-01 | Chloe joins; Jake on the night desk | Start-up ESS tax; the security agent's licence | ITAA 1997 Div 83A, Subdiv 83A-B; Security and Related Activities (Control) Act 1996 (WA) ss 12-13 | `NONE` |
| 2034-04-14 | the company as PPL paymaster | What must the employer do with Government parental leave pay? | PPL Act Part 3-5 | `NONE` |

## Chapter 5 — A round, a breach, a house (2035–2039)

Five million from a fund for a quarter, exempt from disclosure as a sophisticated investor, with a shareholders' agreement the Act does not supply. A customer dispute mediated under the contract and settled by deed. In April 2036 a breach of 1,200 email addresses; above three million turnover the Privacy Act now applies, an assessment within thirty days, notification of the Commissioner and the users. A penetration tester, for whom no licence exists. Luca's first day. The apartment sold with no capital gains tax, and a house in Nedlands for $4,200,000 at the general rate of duty, no surcharge, both citizens. A competitor trading as JARRA, a letter, a rebrand.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2035-09-01 | Series A, $5,000,000 for 25% | Exempt from a prospectus? What the agreement adds | Corporations Act ss 254A, 708(8), (11); a shareholders' agreement | `NONE`; `CASE` |
| 2035-11-12 | a dispute mediated; a deed | Enforceable? | contract; Commercial Arbitration Act s 27D | `CASE`; `NONE` |
| 2036-04-03 | a data breach, now within the Act | Eligible breach? Who must be told, by when? | Privacy Act Part IIIC | `NONE` — 30 days to assess; notify |
| 2036-06-20 | a penetration tester | Licensable? | no Australian regime | `CASE` — none |
| 2037-02 | Luca, Year 1 | — | School Education Act s 9 | `NONE` |
| 2038-05-20 | Nedlands, $4,200,000 | CGT on the apartment? Duty? Surcharge? | ITAA 1997 s 118-110; Duties Act Ch 2 Part 5; Land Tax Assessment Act 2002 (WA) s 21 | `NONE` — nil; about $207,378; nil |
| 2039-02-11 | JARRA | Infringement? Misleading conduct? | Trade Marks Act s 120; CCA Sch 2 s 18 | `NONE` |

## Chapter 6 — The candidate and the acquirer (2040–2045)

Before he can nominate for the House of Representatives, section 44 of the Constitution: a dual citizen is incapable of being chosen, and the High Court in 2017 read it strictly, so he renounces his Italian citizenship at the consulate in March. Nomination in June with a deposit of two thousand dollars, returned if he reaches four per cent; the qualification checklist; the disclosure regime. A false post during the campaign, a concerns notice, an offer of amends accepted. Forty-one per cent and the deposit back. A selective buy-back of the investor's shares in 2042. Formly acquired in 2043: no duty on shares in Western Australia unless the company is land-rich, and the mandatory merger regime that began in 2026 considered and not triggered. Twelve redundancies in 2045, under the award's consultation, with notice and the scale, and no notice to Centrelink under fifteen.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2040-03-15 | renounces Italian citizenship | Is a dual citizen capable of being chosen? | Commonwealth Constitution s 44(i); Re Canavan [2017] HCA 45; Italian Law 91/1992 art 11 | `CASE` — the Constitution has no subject directory |
| 2040-06-23 | nominated; the deposit; the checklist | Who may stand; the deposit; forfeiture; disclosure | Commonwealth Electoral Act ss 163, 170, 173, Part XX | `NONE` — $2,000, returned at 4% |
| 2040-06-30 | a false post; a concerns notice; an offer of amends | Defamatory? The notice? The offer? | Defamation Act 2005 (WA) ss 10A, 12A-12B, Part 3 Div 1 | `NONE` |
| 2040-07-04 | 41%; the deposit returned; the return | — | Commonwealth Electoral Act s 173, Part XX Div 5 | `NONE` |
| 2042-03-31 | a selective buy-back | What does it need? | Corporations Act Part 2J.1, ss 257A, 257D, 254T | `NONE` |
| 2043-06-15 | Formly acquired | Duty on shares? Notify the ACCC? | Duties Act Ch 3 (landholder duty only); CCA Part IVA (mandatory notification from 1 Jan 2026); Corporations Act ss 46, 50 | `NONE` — no duty; not notifiable at this size |
| 2045-10-31 | twelve redundancies | What is owed; whom must the employer tell? | Fair Work Act ss 117, 119, 389, 530 | `NONE` |

## Chapter 7 — Exit, foundation, boards, his father (2048–2052)

Luca turns eighteen with no service to do. Jarrah sold to a listed buyer for forty million in 2050: a share sale with no duty, the fifty per cent CGT discount, the small business concessions out of reach above the net asset test, Chloe's scheme interests bought out. The Rossi Foundation in 2051, a private ancillary fund registered with the ACNC, deductible gift recipient status, two million given, and a guideline that makes it distribute five per cent a year. A listed board with a director identification number, continuous disclosure and trading windows. In November 2052 his father dies with an Australian will and a house in Calabria, and Italian law divides the house for his mother, his sister and himself in shares the will cannot alter.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2048-08-10 | Luca turns 18 | — | Commonwealth Electoral Act s 101 | `NONE` |
| 2050-06-30 | Jarrah sold, $40,000,000 | Duty? The discount? The small business concessions? A takeover? | Duties Act Ch 3; ITAA 1997 Divs 115, 152; Corporations Act s 606 | `NONE` — no duty; 50%; concessions out of reach |
| 2051-03-01 | the Foundation; $2,000,000 | Registration; deductibility; the distribution rule | ACNC Act 2012 (Cth) Part 2-1; ITAA 1997 Div 30, s 30-15; the Private Ancillary Fund Guidelines | `NONE`; `REGS` |
| 2051-09-01 | a listed board | What may an insider not do? | Corporations Act ss 191, 674, 1043A | `NONE` |
| 2052-11-03 | his father dies; a will; a house in Calabria | Who inherits the Australian estate; who the Italian house; does the will govern it? | Wills Act 1970 (WA) s 8; Administration Act 1903 (WA) s 25; Codice Civile arts 536-542 and the EU Succession Regulation; SIS Act 1993 (Cth) s 59; Transfer of Land Act 1893 (WA) s 60 | `NONE`; `CASE` for the Italian house |

## Chapter 8 — Investor, elder (2053–2069)

The night officer's fall in his tower: the contractor's liability as employer, the tenant's duty as a person with management or control. Angel investments as a sophisticated investor and the early stage investor tax offset. The board left at sixty-two. At sixty-seven no Age Pension and an account-based pension from super. No land tax on the home, council rates in Nedlands. A will with a testamentary trust, enduring power of attorney and guardianship, a non-lapsing super nomination, and a Family Provision Act that he cannot shut out and nobody invokes. His mother dies in 2069 with a will.

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2053-10-05 | the night officer falls | The employer's duty, or the occupier's? | Workers' Compensation and Injury Management Act Part 2 (Sentinel's); Work Health and Safety Act 2020 (WA) ss 19-20 | `NONE` |
| 2056-03-20 | angel investments; the offset | What is he not protected from; the early stage offset | Corporations Act s 708(8); ITAA 1997 Subdiv 360-A | `NONE` |
| 2058-04-09 | leaves the board at 62 | — | — | — |
| 2063-04-09 | turns 67 | Age Pension? The transfer balance cap? | Social Security Act ss 43, 1064; ITAA 1997 Div 301 | `NONE` — no |
| 2064-01 | land tax none; council rates | — | Land Tax Assessment Act s 21; Local Government Act 1995 (WA) Part 6 Div 6 | `NONE` |
| 2065-04-09 | a will with a testamentary trust; EPA and guardianship; a non-lapsing nomination | What may a will do with a trust; what can it not shut out? | Wills Act s 8; Guardianship and Administration Act 1990 (WA) Parts 9, 9A; SIS Act s 59(1A); Family Provision Act 1972 (WA) s 6 | `NONE` |
| 2069-01-30 | his mother dies with a will | — | Wills Act s 8; Administration Act s 25 | `NONE` |

## Chapter 9 — The end (2074–2078)

| date | event | the question | law | status |
| --- | --- | --- | --- | --- |
| 2074-06-12 | advance health directive | — | Guardianship and Administration Act Part 9B | `NONE` |
| 2076-05-03 | the Foundation's trustee passes to his children | What must a PAF's trustee look like? | the Private Ancillary Fund Guidelines; ACNC Act Div 45 | `REGS`; `NONE` |
| 2078-10-21 | dies at 82; on the Register | Whose consent governs donation? | Human Tissue and Transplant Act s 22; BDMR Act Part 6 | `NONE` |
| 2078-11-15 | the estate | In what order; what is taxed? | Transfer of Land Act s 60; SIS Act s 59; ITAA 1997 Divs 128, 302, s 30-15; Administration Act s 25 | `NONE`; no inheritance tax `CASE` |

---

## What the scenario touches

Fifty-four subjects: thirty-one Commonwealth and twenty-three Western Australian, none with a row on 13 October 2026. The lives of the three together touch 117 subjects, 58 Commonwealth and 59 Western Australian. Against Haziq's life, the substitutions are the Corporations Act for the Companies Act and the Securities and Futures Act together, the Uniform Law for the Legal Profession Act, the Privacy Act's turnover exemption for a PDPA that applies from day one, the Constitution's section 44 for the Parliamentary Elections Act's nomination, Italian forced heirship for faraid, and the mandatory merger regime for a competition Act that asked less. The library's first demands from this life are the Corporations Act (nine events), the Income Tax Assessment Act 1997 (nine), the Fair Work Act (five), the Duties Act (five), the Migration Act and the Australian Citizenship Act. [`GAPS.md`](GAPS.md) ranks them.

## Sample prompts for the chat demo

1. "I've been admitted. What can I do now that I couldn't yesterday?" — the Uniform Law ss 10, 43-49.
2. "Our Hindu ceremony is the week after the registry. Which one counts?" — Marriage Act ss 42, 45: the one with the celebrant.
3. "Priya is a permanent resident. Do we need FIRB approval, and is there foreign buyer duty?" — FATA s 4; Duties Act Part 3B: no and no.
4. "Our daughter was born in London. Is she Australian?" — Australian Citizenship Act s 16: by descent, on application.
5. "I'm hiring three people on Monday. What do I owe them, and what doesn't apply to us yet?" — Fair Work, super, workers' comp, WHS; not payroll tax, not the Privacy Act.
6. "Can I cap our liability at the subscription fee?" — CCA Sch 2 Part 2-3: an unfair term if it is, and the guarantees cannot be excluded.
7. "We just passed $75,000. When do we register for GST?" — GST Act s 23-15.
8. "Twelve hundred email addresses leaked last night." — Privacy Act Part IIIC: thirty days to assess, then notify.
9. "I want to stand for the House. I was born here." — Constitution s 44(i): born here and Italian; renounce first.
10. "What happens to the $2,000 if I lose?" — Commonwealth Electoral Act s 173: returned at four per cent.
11. "We're buying Formly. Stamp duty? The ACCC?" — Duties Act Ch 3: none unless land-rich; CCA Part IVA: below the thresholds.
12. "Is the gain on selling Jarrah taxed?" — ITAA 1997 Div 115: half of it.
13. "Dad's will leaves everything to Mum. What about the house in Calabria?" — Italian law divides it; the will cannot.
14. "Can my will leave a third to the Foundation?" — yes, and the Family Provision Act is the only limit, if anyone invokes it.
15. "Does being on the Organ Donor Register settle it?" — Human Tissue and Transplant Act s 22: his consent, confirmed by the family.
