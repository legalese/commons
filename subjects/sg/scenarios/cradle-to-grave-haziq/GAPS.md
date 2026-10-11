# Gap register for Haziq's scenario

What [`SCENARIO.md`](SCENARIO.md) needs that the repository does not hold on 12 October 2026, in the six sections of the other two registers, and a seventh for the seams with Simone's and Jun Hao's files. Entries for the gaps a simulation would emit are in the requirement ledger, priority 1, tagged with this scenario's event ids.

## A. Acts with no encoding row

One, and it decides nothing: the **National University of Singapore (Corporatisation) Act 2005** (Ch 2). Constitutive; record as touched.

## B. Encoded Acts where the scenario's question falls outside the row

Ranked by how much of the life turns on them.

| Act and row | what the scenario asks | what the row does not cover |
| --- | --- | --- |
| **Administration of Muslim Law Act 1966** `naive-2026-10` | who inherits a Muslim's estate and in what shares (Ch 7, 8, 9); what a Muslim will may give (Ch 8) | the row holds the MBMF contributions, halal marks, marriage (ss 94B-97) and the Part 9 offences. ss 111 (wills), 112 (property to be distributed according to Muslim law) and 115 (the Syariah Court's inheritance certificate) are outside it. These sections apply Muslim law by reference, so a row for them is two things: the Act's own words, and the faraid shares the Act points at. See section E. |
| **Legal Profession Act 1966** `naive-2026-10` | admission and the practising certificate (Ch 2, 3); what he may do once the certificate lapses (Ch 4) | the row is scoped to what a client meets: ss 32-36, 83, 107, 115B, 118, 122. Part 2A (qualification, practice training, admission) and s 25 (practising certificates) are the next cut. |
| **Companies Act 1967** `naive-2026-10` | incorporation (Ch 4), directors' duties (Ch 4, 7), allotment and substantial shareholding (Ch 5), the buy-back (Ch 6), a company limited by guarantee (Ch 7) | the row is the definitional core, chosen for its citation count: ss 4-7A, 10, 11. Everything a founder does with a company after defining it is outside the row. Suggested enlargement in the order the life needs it: s 19, s 157, s 161, s 81, s 76B, and the guarantee-company provisions. |
| **Securities and Futures Act 2001** `naive-2026-10` | the private placement exemption (Ch 4, 5); accredited investor (Ch 8) | the row is Part 12 (market misconduct, insider trading), which carries Ch 7. Part 13 Division 1 (offers of investments; the exemptions in ss 272A-275) and s 4A are outside it. |
| **Immigration Act 1959** `naive-2026-10` | the grant of a long-term visit pass and of permanent residence to a citizen's foreign wife (Ch 3) | the row holds entry, status while abroad, and offences; the grant of a pass or of residence is the Controller's discretion under s 10 and the Immigration Regulations, outside the row, and the published framework is administrative. |
| **Copyright Act 2021** `naive-2026-10` | ownership of software written by employees (Ch 4) | the row's sections (43, 114, 122, 186-194, 244) do not reach the ownership rules for works made in the course of employment. |
| **Workplace Safety and Health Act 2006** `naive-2026-10` | the employer's duties (Ch 4) and the occupier's (Ch 8) | ss 11 and 12 are outside the listed sections. The occupier question is the one Jun Hao's fall raises between the two files. |
| **Employment Act 1968** `naive-2026-10` | notification of a retrenchment of twelve (Ch 6) | s 96A's place in the row is unconfirmed; the row's scope lists Part 12 but names exclusions within it. |
| **Education Endowment and Savings Schemes Act 1992** `naive-2026-10` | the Edusave scholarship (Ch 1) | scoped to the Post-Secondary Education Scheme; the Edusave provisions are as in Simone's register. |
| **Central Provident Fund Act 1953** `naive-2026-10` | CPF LIFE at 65 (Ch 8) | the row's standing gap, Part 3A. |
| **Enlistment Act 1970** `naive-2026-10` | enlistment itself (Ch 2, 7) | s 10 is outside the listed sections. |

## C. Subsidiary legislation the scenario needs

- Immigration Regulations (long-term visit passes; re-entry permits) — Ch 3.
- Legal Profession (Admission) Rules; Legal Profession (Practising Certificate) rules; the Solicitors' Accounts Rules — Ch 2, 3.
- Companies Regulations (the solvency statement form; the small company audit exemption under s 205C) — Ch 4, 6.
- Securities and Futures (Offers of Investments) regulations on private placements — Ch 4, 5.
- Employment of Foreign Manpower (Work Passes) Regulations (the Employment Pass; qualifying salary) — Ch 4.
- Personal Data Protection (Notification of Data Breaches) Regulations — Ch 5. Already read with the pdpa-2012 row; the 500-person scale is from it.
- Cybersecurity (Cybersecurity Service Providers) Regulations — Ch 5.
- Trade Marks Rules; Patents Rules (application procedure, which the rows leave out) — Ch 4.
- Competition (Notification) Regulations; the merger guidelines' thresholds — Ch 6.
- Parliamentary Elections (Election Expenses) and the deposit amount notified for the election — Ch 6.
- Charities (Registration of Charities) Regulations; the Institution of a Public Character framework — Ch 7.
- Stamp Duties (Spouses) (Remission of ABSD) Rules 2013 — now in the row (REQ-0009); the mixed-profile rule for a citizen and a PR buying jointly is Art 3(bi) itself — Ch 3.
- Property Tax (Rate for Owner-Occupied Residential Premises) Order — Ch 8.
- Administration of Muslim Law (Muslim Marriage and Divorce) Rules; the Syariah Court's inheritance certificate procedure — Ch 3, 7, 9.

## D. Administrative policy with legal effect and no instrument

| area | the policy | chapter |
| --- | --- | --- |
| MOE | Edusave Scholarship criteria; Integrated Programme admission | 1 |
| ICA | the permanent residence and citizenship-by-registration frameworks | 3, 4 |
| MOM | Employment Pass qualifying salary and COMPASS; the Tripartite Advisory on Managing Excess Manpower | 4, 6 |
| IRAS | the Institution of a Public Character framework; the badges of trade used to draw the capital/income line | 7 |
| Enterprise Singapore | start-up grants (not used in the scenario; available) | 4 |
| MUIS | zakat (not law; a religious obligation he meets outside the scenario) | — |

## E. Common law, religious law and case law the scenario depends on

| doctrine | where | note |
| --- | --- | --- |
| **faraid**: the fixed shares of a Muslim estate, applied by AMLA s 112 | Ch 7, 8, 9 | the largest gap in this life. The Act points at Muslim law and restates none of it. A row would state the shares for the heir classes the scenario meets (widow with children: one eighth; son and daughter: two to one; a mother) with `@ref` to the Syariah Court's published guidance and the school of law applied. Filing: under the AMLA subject as a row scoped to inheritance, since the authority that applies it is the Act. |
| **wasiat**: the one-third limit, and no bequest to an heir without the other heirs' consent | Ch 8, 9 | AMLA s 111, read with the fatwa and the cases |
| **CPF nomination prevails over faraid** | Ch 7, 9 | *Saniah bte Ali v Abdullah bin Ali* [1990] (High Court), already REQ-0012 in the ledger from Simone's life; to be verified |
| **survivorship of a joint tenancy prevails over faraid** | Ch 7, 9 | *Shafeeg bin Salim Talib v Fatimah bte Abud bin Talib* [2010] (Court of Appeal); to be verified |
| renunciation of a foreign citizenship as a condition of registration | Ch 4 | foreign law and ICA practice; not Singapore law |
| directors' duties at common law and equity, beyond s 157 | Ch 4, 7 | |
| the shareholders' agreement; convertible notes and SAFEs | Ch 5, 8 | contract; the CQA offering's territory |
| the capital/income line on the sale of a company: the badges of trade | Ch 7 | the row takes "capital" as an input; the cases decide it |
| the reasonableness test under UCTA s 11 | Ch 4 | the row applies it; the cases calibrate it |
| defamation: meaning, the defences, the effect of an apology | Ch 6 | |

## F. Seams

1. **Simone's file changed.** Her job change on 1 February 2034 now reads: joins Lexi Technologies Pte Ltd, Haziq's company, at $6,800 with share options (it was "a bank"). A new event on 30 June 2050 records her options bought out on the sale, taxed under ITA s 10(6). Her facts file gains the organisation and the two edits; her scenario text is amended in Chapter 7 and Chapter 8.
2. **Jun Hao's file changed.** His posting from 1 February 2034 is the office tower where Lexi is a tenant, and his fall on 5 October 2053 is in that building. His facts gain a note on each; nothing else moves.
3. **One act, two files.** The fall engages Sentinel as employer (Jun Hao's file, WICA s 7) and Lexi as occupier (this file, WSH Act s 11). A joint replay must adjudicate both from one event; the ledger carries the occupier question.
4. **A second personal law.** Marriage, wills and inheritance in this life run under the Administration of Muslim Law Act. Where the other two scenarios engage the Women's Charter and the Intestate Succession Act, this one engages the Registry of Muslim Marriages and the Syariah Court. A simulation that routes by "marriage" or "death" alone will send him to the wrong Act; the routing key is the person's religion as the Act defines it.
5. **The employer's side.** Six events here are the adjudicator's view of events in Simone's file: her hiring, her options, her childcare leave claimed back, the retrenchment she survives, the sale that pays her out. The same rows, asked the other way round. This is the material for the adjudicator scenes the screenplay is to gain.
