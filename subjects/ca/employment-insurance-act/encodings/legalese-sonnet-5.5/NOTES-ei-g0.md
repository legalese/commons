# NOTES: Employment Insurance Act and Regulations, the shared core `eia-core`

Written by the keel agent `ei-g0` (Sonnet 5.5) on 2026-10-24 for the thirteen part agents (ei1 to ei7, er1 to er6) that encode the rest of the two texts.
It holds the vocabulary every piece shares, the Act's lines 1 to 132 (the title block and ss 1 to 5), and the facts about the whole text that a piece should not have to rediscover.

**The texts.**
Both are unofficial plain-text conversions made by legalese commons of the Justice Laws Website consolidations; the first lines of each raw file say so.
The Act is `S.C. 1996, c. 23`, current to 2026-09-30, last amended 2026-06-18.
The Regulations are `SOR/96-332`, current to 2026-09-30, last amended 2026-04-01.
Nothing here has been verified against the official text.
The French version is equally authoritative and is not read; historical notes and footnotes are omitted from the conversions.

**Which instrument each rule comes from.**
Every rule, type and quotation in the eight `.l4` files comes from the Act (`src:N` is a line of the Act's raw file).
The Regulations are named in comments only where they decide how the Act reads: regs 2(1) and 3(1) in s 5 (fork F2), regs 2 to 8 as the source of two BOOLEAN inputs of s 5, and reg 25 as the exercise of s 2(5).

**Seat.**
The person who has lost work or cannot work (sickness, pregnancy, caring for a child or a family member), including a self-employed person or a fisher, asking whether they qualify for benefits, how many hours or weeks they need, how much and for how long, and what they must do or tell the Commission.
Officials have no seat: the Commission, the Minister and the Minister of National Revenue appear only as `Party` constructors and as the holders of judgments the text leaves to them.
No seat layer is written here; this folder holds the shared core only.

**Dates.**
No enactment, assent or commencement date appears in lines 1 to 132.
The title block gives only the citation `S.C. 1996, c. 23`.
The coming into force is s 190, which is piece ei6's: s 190(1) (line 3171) says the Act comes into force on June 30, 1996 except as the section otherwise provides, and s 190(2) (line 3173) says s 4, subsection 5(6) and some other provisions come into force on January 1, 1997.
So the keel does nothing about dates: no rule carries a `RULES EFFECTIVE DATE`, and the text is one vintage (current to 2026-09-30), so no rule takes a rule date as input.
A provision limited to a date range takes the date of the fact as an input.

**Files** (all in this folder, flat; `check.sh` runs every `.l4` here).

| file | what it holds |
| --- | --- |
| `eia-core.l4` | shared vocabulary only: the date shim, week and year helpers, `Period of days`, rounding, `Reason for benefits`, `Election of maximum weeks`, `Violation class`, `Party`, `Rate band` |
| `eia-core-interpretation.l4` | s 2: the definitions that can be worked out from facts, and s 2(2); `Part of the Act` |
| `eia-core-maximum-earnings.l4` | s 4: maximum yearly insurable earnings |
| `eia-core-insurable-employment.l4` | s 5: insurable employment |
| `eia-core-tests-core.l4`, `eia-core-tests-interpretation.l4`, `eia-core-tests-maximum-earnings.l4`, `eia-core-tests-insurable-employment.l4` | assertions with hand-written expected values; every figure in the s 4 tests is invented and none is a published figure |
| `NOTES.md`, `PROGRESS.md` | this file; the working log |
| `check.sh`, `srcrefs.py` | supplied tools, unchanged |

## Vocabulary

Every top-level name the keel defines is taken: a piece that declares the same name makes both modules unusable together.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `YMD` | function | `YMD y m d` is the date with that year, month and day; defined as `Date d m y` because the stable binary does not define `YMD` even after `IMPORT daydate` | not from the text; a workaround for the binary (measured with a probe) |
| `s 2(1) the Sunday that begins the week containing` | function DATE to DATE | the Sunday of the week a date falls in | Act s 2(1) "week" (src:50) |
| `s 2(1) the Saturday that ends the week containing` | function DATE to DATE | the Saturday six days after that Sunday | Act s 2(1) "week" (src:50) |
| `s 2(1) the year containing` | function DATE to NUMBER | the calendar year of a date | Act s 2(1) "year" (src:51) |
| `weeks as days` | function NUMBER to NUMBER | n weeks as 7n days, for a time limit written in weeks | Act s 2(1) "week" (src:50) |
| `the last day of n days after d` | function NUMBER and DATE to DATE | d plus n days: a limit of n days after d ends on that date and that date counts | assumed, not ruled: fork F4 |
| `Period of days` | record | `first day of the period` and `last day of the period`, both inclusive; the shape of a qualifying period, a benefit period, a calculation period | convention; no single provision |
| `the day d falls within p` | function DATE and Period of days to BOOLEAN | the date lies in the period, ends included | convention |
| `the number of days in p` | function Period of days to NUMBER | last day minus first day plus one | convention |
| `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` | function NUMBER to NUMBER | nearest dollar, the higher dollar when equidistant: `FLOOR (amount PLUS 0.5)`; pieces ei1 and ei5 call it and cite their own subsection | Act s 6(2) (src:146); s 152.01(5) (src:2142), word for word the same |
| `Reason for benefits` | enum of 7 | the reason a benefit is claimed: a reason other than those in s 12(3) (regular benefits), pregnancy, caring for a new-born or adopted child, a prescribed illness, injury or quarantine, care or support of a family member, of a critically ill child, of a critically ill adult | Act s 12(3)(a)-(f) (src:358-366); s 152.14(1)(a)-(f) (src:2482-2490) |
| `Election of maximum weeks` | enum of 2 | the 35-week maximum or the 61-week maximum, elected for the care of a new-born or adopted child | Act s 12(3)(b), s 23(1.1) (src:511), s 152.05(1.1) (src:2196) |
| `Violation class` | enum of 4 | a minor, a serious, a very serious or a subsequent violation; there is no constructor for a violation for which only a warning was imposed, because s 7.1(5) leaves it out | Act s 7.1(5) (src:203-208) |
| `Party` | enum of 7 | the offices the text puts duties or powers on: the claimant, the insured person, the self-employed person, the employer, the Commission, the Minister (of Employment and Social Development, s 2(1)), the Minister of National Revenue | Act s 2(1) (src:22-42); s 81 (src:1301); s 152.01(1) (src:2122) |
| `Rate band` | enum of 12 | the band of the regional rate of unemployment, in the words of Schedule I; ss 7(2), 7.1(1) and 14(2) use nine bands, whose last, "more than 13%", is bands 9 to 12 here | Act Schedule I (src:3204) |
| `the band of the regional rate of unemployment` | function NUMBER to Rate band | the band a rate falls in; the rate is a fraction (6.5% is 0.065) and a figure on a boundary belongs to the lower band | Act Schedule I (src:3204) |
| `the number of the band` | function Rate band to NUMBER | 1 to 12 in the order of Schedule I, for a table read by column | Act Schedule I (src:3204) |
| `Part of the Act` | enum of 16 (in `eia-core-interpretation`) | Part I, II, III, IV, V, VI, VII, VII.1, VIII, VIII.1, VIII.2, VIII.3, VIII.4, VIII.5, VIII.6, IX | the Part headings, Act (src:133, 1049, 1127, 1294, 1789, 1804, 2054, 2109, 2689, 2711, 2721, 2735, 2763, 2967, 3086, 3096) |
| `Kind of thing the definition of documents lists` | enum of 11 (in `eia-core-interpretation`) | money, securities, books, records, letters, telegrams, vouchers, invoices, accounts, statements, and one for anything not on the list; every constructor begins `s 2(1) documents - ` | Act s 2(1) "documents" (src:26) |
| `Published rate of unemployment` | record (in `eia-core-interpretation`) | `date produced` and `rate produced`: one Statistics Canada release | Act s 2(2) (src:53) |
| `s 2(1) affidavit` | rule BOOLEAN | sworn or affirmed, before a commissioner of oaths or another person authorized to take affidavits | Act s 2(1) (src:18) |
| `s 2(1) benefits` | rule BOOLEAN | unemployment benefits payable under Part I, VII.1 or VIII, keyed on the Part | Act s 2(1) (src:20) |
| `s 2(1) claimant` | rule BOOLEAN | applies or has applied for benefits under the Act | Act s 2(1) (src:22) |
| `s 2(1) common-law partner` | rule BOOLEAN | cohabiting in a conjugal relationship and the first day of cohabitation is at least one year before the day the question is asked (fork F6) | Act s 2(1) (src:24) |
| `s 2(1) confirmed delivery service` | rule BOOLEAN | certified mail, registered mail, or another delivery service that provides proof of delivery | Act s 2(1) (src:25) |
| `s 2(1) documents includes` | rule MAYBE BOOLEAN | JUST TRUE for a listed kind, NOTHING for anything else: the list is open and the Act never says something else is not a document | Act s 2(1) (src:26) |
| `s 2(1) dwelling-house` | rule BOOLEAN | a residence, or a building in the yard connected by a doorway or a covered and enclosed passageway, or a mobile unit being used as a residence | Act s 2(1) (src:27-29) |
| `s 2(1) employer` | rule BOOLEAN | is or has been an employer, or the sponsor or co-ordinator individual of paragraph 5(1)(e) in respect of their own remuneration | Act s 2(1) (src:31) |
| `s 2(1) employment` | rule BOOLEAN | the act of employing or the state of being employed | Act s 2(1) (src:33) |
| `s 2(1) insured person` | rule BOOLEAN | is or has been employed in insurable employment; the caller feeds it the result of `s 5 insurable employment` | Act s 2(1) (src:38) |
| `s 2(1) labour dispute` | rule BOOLEAN | a dispute between employers and employees or between employees and employees, connected with employment, non-employment or the terms or conditions of employment of any persons | Act s 2(1) (src:40) |
| `s 2(1) the Minister for` | rule Part of the Act to Party | the Minister of National Revenue in Parts IV and VII, the Minister of Employment and Social Development everywhere else | Act s 2(1) (src:42); s 81 (src:1301); s 144 (src:2063) |
| `s 2(1) overpayment of benefits` | rule BOOLEAN | an overpayment that is not a benefit repayment as described in Part VII; the positive meaning is Part VI's (ei4) and is an input | Act s 2(1) (src:43) |
| `s 2(1) provincial law` | rule BOOLEAN | provisions of a provincial Act that authorize, or entitle a person to, payment of benefits under a plan established by or under that Act | Act s 2(1) (src:45) |
| `s 2(1) special benefits` | rule Reason for benefits to BOOLEAN | benefits paid for any reason in s 12(3) or s 152.14(1), that is, any reason except the regular one | Act s 2(1) (src:48) |
| `s 2(1) regular benefits` | rule BOOLEAN | payable under Part I or Part VIII, not special benefits and not benefits by virtue of s 24 or s 25 | Act s 2(1) (src:47) |
| `s 2(1) week` | rule Period of days to BOOLEAN | seven consecutive days beginning on a Sunday, or any other prescribed period (an input) | Act s 2(1) (src:50) |
| `s 2(2) the rates produced by` | rule LIST to LIST | the releases produced on or before the day of the final determination | Act s 2(2) (src:53) |
| `s 2(2) the latest day of production among` | rule LIST to NUMBER | the day count of the latest release in a non-empty list | Act s 2(2) (src:53) |
| `s 2(2) the releases produced on the day numbered` | rule LIST and NUMBER to LIST | the releases of one day count | Act s 2(2) (src:53) |
| `s 2(2) the rate in` | rule record to NUMBER | the rate of one release | Act s 2(2) (src:53) |
| `s 2(2) the rate of unemployment most recently produced` | rule LIST and DATE to MAYBE NUMBER | the rate the Commission must use; NOTHING when no release was produced by the day (fork F3) | Act s 2(2) (src:53) |
| `s 4(2)(a) the average of the Average Weekly Earnings for each month of a 12-month period` | rule LIST to MAYBE NUMBER (in `eia-core-maximum-earnings`) | the mean of twelve monthly figures; NOTHING unless exactly twelve are given | Act s 4(2)(a) (src:78); s 4(5) (src:86) |
| `s 4(2)(a) the 12-month period ending on April 30 in the preceding year` | rule NUMBER to Period of days | May 1 two years back to April 30 of the preceding year, for a given year | Act s 4(2)(a) (src:78) |
| `s 4(2)(b) the 12-month period ending 12 months prior to April 30 of that preceding year` | rule NUMBER to Period of days | the 12 months before that | Act s 4(2)(b) (src:80) |
| `s 4(1) base amount of the maximum yearly insurable earnings` | constant NUMBER | 39000 | Act s 4(1) (src:75) |
| `s 4(2) the amount calculated in accordance with subsection (2)` | rule NUMBER and NUMBER to NUMBER | 52 times (A times A/B), A the first average and B the second | Act s 4(2) (src:77-80) |
| `s 4(3) the amount calculated in accordance with subsection (3)` | rule 3 NUMBERs to NUMBER | the earlier year's amount before rounding down times A/B | Act s 4(3) (src:82) |
| `s 4(4) the amount rounded down to the nearest multiple of one hundred dollars` | rule NUMBER to NUMBER | 100 times the floor of amount over 100 | Act s 4(4) (src:84) |
| `s 4(1) the maximum yearly insurable earnings for the year, before rounding down` | rule MAYBE NUMBER and 2 NUMBERs to MAYBE NUMBER | 39000, or the (2) amount once it exceeds 39000, or (3) after an earlier year has exceeded it; NOTHING if an average is not above zero (fork F1) | Act s 4(1) (src:75); s 4(3) (src:82) |
| `s 4(1) the maximum yearly insurable earnings for the year` | rule MAYBE NUMBER and 2 NUMBERs to MAYBE NUMBER | the same, rounded down | Act s 4(1) (src:75) |
| `s 4(3) the amount to carry into the following year` | rule MAYBE NUMBER and 2 NUMBERs to MAYBE NUMBER | what the next year takes as its first input: this year's amount before rounding down once some year has exceeded 39000, else NOTHING | Act s 4(3) (src:82) |
| `s 5(1)(a) employment under a contract of service or apprenticeship` | rule BOOLEAN (in `eia-core-insurable-employment`) | in Canada, by one or more employers, under an express or implied contract of service or apprenticeship | Act s 5(1)(a) (src:91) |
| `s 5(1)(b) employment by Her Majesty in right of Canada` | rule BOOLEAN | paragraph (a) employment by Her Majesty in right of Canada | Act s 5(1)(b) (src:92) |
| `s 5(1)(c) service in the Canadian Forces or in a police force` | rule BOOLEAN | either kind of service | Act s 5(1)(c) (src:93) |
| `s 5(1)(d) employment included by regulations` | rule BOOLEAN | one input: included by regulations under s 5(4) or (5) (regs 2 to 6, piece er1) | Act s 5(1)(d) (src:94) |
| `s 5(1)(e) employment as the sponsor or co-ordinator of an employment support measure` | rule BOOLEAN | in Canada, as sponsor or co-ordinator, the measure not one referred to in paragraph 59(c) or (d) | Act s 5(1)(e) (src:95) |
| `s 5(1) insurable employment, before subsection (2)` | rule 5 BOOLEANs to BOOLEAN | any one of paragraphs (a) to (e) | Act s 5(1) (src:90) |
| `s 5(2)(a) employment of a casual nature other than for the purpose of the employer's trade or business` | rule BOOLEAN | casual, and not for the purpose of the employer's trade or business | Act s 5(2)(a) (src:98) |
| `s 5(2)(b) employment of a person by a corporation they control` | rule BOOLEAN and NUMBER to BOOLEAN | the employer is a corporation and the person controls more than 40% of its voting shares (the portion is a fraction; 40% itself does not exclude; fork F5) | Act s 5(2)(b) (src:99) |
| `s 5(2)(c) employment by Her Majesty in right of a province` | rule BOOLEAN | in Canada, by a province, and not included by regulations under 5(4)(d) (fork F2) | Act s 5(2)(c) (src:100) |
| `s 5(2)(d) employment by a foreign government` | rule BOOLEAN | in Canada, by a foreign government or political subdivision, and not included by regulations under 5(4)(e) (fork F2) | Act s 5(2)(d) (src:101) |
| `s 5(2)(e) employment by an international organization` | rule BOOLEAN | in Canada, by an international organization, and not included by regulations under 5(4)(f) (fork F2) | Act s 5(2)(e) (src:102) |
| `s 5(2)(f) employment under an exchange program` | rule BOOLEAN | in Canada, under an exchange program, not remunerated by an employer resident in Canada | Act s 5(2)(f) (src:103) |
| `s 5(2)(g) employment that constitutes an exchange of work or services` | rule BOOLEAN | one input | Act s 5(2)(g) (src:104) |
| `s 5(2)(h) employment excluded by regulations` | rule BOOLEAN | one input: excluded by regulations under s 5(6) (regs 7 and 8, piece er1) | Act s 5(2)(h) (src:105) |
| `s 5(2)(i) employment if the employer and employee are not dealing with each other at arm's length` | rule 3 BOOLEANs to BOOLEAN | not at arm's length under the Income Tax Act (s 5(3)(a)), unless related and the Minister of National Revenue is satisfied (s 5(3)(b)); both are inputs | Act s 5(2)(i) (src:106); s 5(3) (src:108-110) |
| `s 5(2) insurable employment does not include` | rule 9 BOOLEANs to BOOLEAN | any one of paragraphs (a) to (i) | Act s 5(2) (src:97) |
| `s 5 insurable employment` | rule 2 BOOLEANs to BOOLEAN | within s 5(1) and not within s 5(2) | Act s 5(1), s 5(2) (src:90, 97) |

Not in the table because they are values of the enums: the constructors and record fields, listed under Instructions to the pieces, item 2.

## Naming conventions

1. Rule names: `s N(M) <the Act's own phrase>` for the Act and `reg N(M) <the Regulations' phrase>` for the Regulations, so that no two pieces can define the same name.
2. Inputs: a `GIVEN` parameter named in the Act's own words, in backticks, one parameter per line; a yes/no input is worded as the condition it states (`by Her Majesty in right of Canada`), never `is`/`has` + noun in a field name.
3. Yes/no rules are named as statements of the condition (`s 2(1) common-law partner`); the question the person is asked ("Am I ...?") is worded in the seat layer, not here.
4. Types, constructors and record fields a piece declares begin with the piece id (`ei3 Premium rate`, `er1 Region`), except the keel's own, which have none: this is the keel's rule, not the text's, and it is what keeps two pieces from clashing.
5. Each rule has its own `GIVEN`; the stable binary rejects a `GIVEN` on a section.
6. Money is a NUMBER of Canadian dollars; hours, weeks and days are NUMBERs of that unit; a rate or percentage is a NUMBER fraction written with the postfix `%` (55% is 0.55), and when passed as an argument it is bracketed: `f (6.5%)`, never `f 6.5%`.
7. Dates are built with `YMD y m d` from `eia-core`, never with a little-endian `Date d m y` literal; a week is identified by the DATE of its Sunday.
8. A time limit is a NUMBER of days (a limit in weeks goes through `weeks as days`); "within n days after d" ends on `d PLUS n` and that day counts (fork F4).
9. A fact that lies outside the piece's range is a plain-typed `GIVEN` parameter (NUMBER, BOOLEAN, DATE, or a keel enum), never another piece's record, and the Defined terms table says which type.
10. There is no shared person record: the core would have to guess every piece's facts; each piece takes its section's facts as further `GIVEN` parameters or builds its own record with prefixed names.
11. Where the text does not answer, a rule returns `MAYBE` and `NOTHING` (or a "not covered" constructor) and a test asserts it; `REFUSE` and `#ASSERT REFUSED` do not exist on the stable binary.
12. A judgment the law hands to someone else (the Commission is satisfied, the Minister of National Revenue is satisfied) is a BOOLEAN input named for that satisfaction; the rule answers conditionally and never guesses it.
13. Each module starts `IMPORT prelude`, `IMPORT daydate` and ``IMPORT `eia-core` `` (and any other keel module it uses); a probe showed the `daydate` names arriving through `eia-core`, but prelude names were not tested that way.
14. Tests: one `#ASSERT` per line, expected values written by hand from the text, every assertion satisfied; a test file is named `<module>`'s name with `-tests-` inserted.

## Defined terms

Every term the two texts define, with the line of its definition and the module or piece that carries its meaning.
"By reference: encoded by piece X, section N, taken there as an input" names the piece the brief assigned that section to; none of those pieces had delivered when this file was written, so it is an assignment and not a landed encoding.
Several words are defined more than once with different meanings (employment, claimant, qualifying period, waiting period, disentitled, benefits, Minister, self-employed person, long-tenured worker, plan, provincial benefits, condition of entitlement to benefits, period of eligibility); a piece names its rule by section and says in its own NOTES which definition it used.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| affidavit | Act s 2(1), l.18 | `eia-core-interpretation` `s 2(1) affidavit` |  |
| benefit period | Act s 2(1), l.19 | by reference: encoded by piece ei1, ss 9 and 10, taken there as an input; and by ei5, ss 152.1 and 152.11 | plain input: a `Period of days` |
| benefits | Act s 2(1), l.20 | `eia-core-interpretation` `s 2(1) benefits` | Part VII gives the word its own meaning for that Part (l.2058, ei4). |
| board of referees | Act s 2(1), l.21 | repealed or blank in this text | [Repealed, 2012, c. 19, s. 240]; s 251 (l.3697, ei7) defines the words again for transitional use. |
| claimant | Act s 2(1), l.22 | `eia-core-interpretation` `s 2(1) claimant` | s 153.5(2) (l.2772, ei6) redefines it for Part VIII.4 and Reg 350.1(2) (l.2485, er6) points back at this definition. |
| Commission | Act s 2(1), l.23 | `eia-core` `Party` constructor `the Commission` | an office, not a rule |
| common-law partner | Act s 2(1), l.24 | `eia-core-interpretation` `s 2(1) common-law partner` | fork F6; Reg 34(1) (l.514, er2) takes the Income Tax Act's meaning for that section. |
| confirmed delivery service | Act s 2(1), l.25 | `eia-core-interpretation` `s 2(1) confirmed delivery service` |  |
| documents | Act s 2(1), l.26 | `eia-core-interpretation` `s 2(1) documents includes` | open list: JUST TRUE or NOTHING, never FALSE |
| dwelling-house | Act s 2(1), l.27-29 | `eia-core-interpretation` `s 2(1) dwelling-house` |  |
| employee's premium | Act s 2(1), l.30 | by reference: encoded by piece ei3, s 67, taken there as an input | plain input: a NUMBER of dollars |
| employer | Act s 2(1), l.31 | `eia-core-interpretation` `s 2(1) employer` |  |
| employer's premium | Act s 2(1), l.32 | by reference: encoded by piece ei3, s 68, taken there as an input | plain input: a NUMBER of dollars |
| employment | Act s 2(1), l.33 | `eia-core-interpretation` `s 2(1) employment` | s 29 (l.744, ei2) and Reg 35(1) (l.542, er3) define the word differently for their own sections; name the rule by section. |
| employment benefits | Act s 2(1), l.34 | repealed or blank in this text | [Repealed, 2022, c. 10, s. 387] |
| employment support measure | Act s 2(1), l.35 | by reference: encoded by piece ei2, s 59, taken there as an input | plain input: a BOOLEAN `is an employment support measure` |
| insurable earnings | Act s 2(1), l.36 | by reference: encoded by piece ei3, Part IV, taken there as an input | plain input: a NUMBER of dollars |
| insurable employment | Act s 2(1), l.37 | `eia-core-insurable-employment` `s 5 insurable employment` | by the definition itself it "has the meaning assigned by section 5"; other pieces take a BOOLEAN or call the rule |
| insured person | Act s 2(1), l.38 | `eia-core-interpretation` `s 2(1) insured person` |  |
| interruption of earnings | Act s 2(1), l.39 | by reference: encoded by piece er1, reg 14 (l.210) and reg 14.01 (l.223, the self-employed person), taken there as an input | plain input: a BOOLEAN `an interruption of earnings has occurred` |
| labour dispute | Act s 2(1), l.40 | `eia-core-interpretation` `s 2(1) labour dispute` |  |
| long-tenured worker | Act s 2(1), l.41 | repealed or blank in this text | [Repealed, 2016, c. 7, s. 207]; Regs 77.999(1) (l.1631, er5) and 77.9994(1) (l.2519, er6) define the words anew for those sections. |
| Minister | Act s 2(1), l.42 | `eia-core` `Party` constructors `the Minister`, `the Minister of National Revenue`; `eia-core-interpretation` `s 2(1) the Minister for` | the Minister of National Revenue in Parts IV and VII (s 81 l.1301, s 144 l.2063) |
| overpayment of benefits | Act s 2(1), l.43 | `eia-core-interpretation` `s 2(1) overpayment of benefits` | only the exclusion is s 2(1)'s; the positive meaning is Part VI's (ei4) and is an input |
| prescribed | Act s 2(1), l.44 | nothing to encode | means "prescribed by the regulations"; each piece names the regulation that prescribes the thing it meets, or takes the prescribed thing as an input |
| provincial law | Act s 2(1), l.45 | `eia-core-interpretation` `s 2(1) provincial law` |  |
| rate of unemployment | Act s 2(1), l.46 | by reference: encoded by piece er1, reg 17 and Schedule I (er6), taken there as an input; the keel supplies `eia-core` `Rate band` and `eia-core-interpretation` `s 2(2)` | plain input: a NUMBER, a fraction (6.5% is 0.065) |
| regular benefits | Act s 2(1), l.47 | `eia-core-interpretation` `s 2(1) regular benefits` |  |
| special benefits | Act s 2(1), l.48 | `eia-core-interpretation` `s 2(1) special benefits` |  |
| umpire | Act s 2(1), l.49 | repealed or blank in this text | [Repealed, 2012, c. 19, s. 240]; s 251 (l.3701, ei7) defines the word again for transitional use. |
| week | Act s 2(1), l.50 | `eia-core` `s 2(1) the Sunday that begins the week containing`; `eia-core-interpretation` `s 2(1) week` |  |
| year | Act s 2(1), l.51 | `eia-core` `s 2(1) the year containing` |  |
| disentitled | Act s 6(1), l.138 | by reference: encoded by piece ei1, s 6(1), taken there as an input | a second definition for Part VII.1 is in s 152.01(1), l.2118 (ei5) |
| disqualified | Act s 6(1), l.139 | by reference: encoded by piece ei1, s 6(1), taken there as an input |  |
| initial claim for benefits | Act s 6(1), l.140 | by reference: encoded by piece ei1, s 6(1), taken there as an input | also s 152.01(1) l.2120 (ei5), s 153.5(1)(c) l.2770 and s 153.15 l.2972 (ei6) |
| major attachment claimant | Act s 6(1), l.141 | by reference: encoded by piece ei1, s 6(1), taken there as an input | 600 hours; Schedule II l.3264 (ei6) replaces it for one case |
| minor attachment claimant | Act s 6(1), l.142 | by reference: encoded by piece ei1, s 6(1), taken there as an input | fewer than 600 hours; Schedule II l.3265 (ei6) replaces it for one case |
| qualifying period | Act s 6(1), l.143 | by reference: encoded by piece ei1, s 8, taken there as an input | also s 152.01(1) l.2121 (ei5) and s 153.15 l.2973 (ei6); plain input: a `Period of days` |
| waiting period | Act s 6(1), l.144 | by reference: encoded by piece ei1, s 13, taken there as an input | also s 152.01(1) l.2126 (ei5) and s 153.15 (ei6) |
| a reference to earnings (s 13.1(b)) | Act s 13.1(b), l.406 | by reference: encoded by piece ei1, s 13.1, taken there as an input | a reading rule, not a defined term |
| employment (sections 30 to 33) | Act s 29(a), l.744 | by reference: encoded by piece ei2, s 29, taken there as an input | differs from s 2(1) "employment" |
| loss of employment | Act s 29(b), l.745 | by reference: encoded by piece ei2, s 29, taken there as an input |  |
| voluntarily leaving an employment | Act s 29(b.1), l.746 | by reference: encoded by piece ei2, s 29, taken there as an input |  |
| just cause for voluntarily leaving an employment or taking leave | Act s 29(c), l.750 | by reference: encoded by piece ei2, s 29, taken there as an input | fourteen listed circumstances (l.751-764) |
| insured participant | Act s 58, l.1068 | by reference: encoded by piece ei2, s 58, taken there as an input |  |
| actuary | Act s 65.21, l.1131 | by reference: encoded by piece ei3, s 65.21, taken there as an input |  |
| payment of allowances because of compassionate care, a child's critical illness, an adult's critical illness | Act s 69(6) to (8), l.1218-1222 | by reference: encoded by piece ei3, s 69, taken there as an input | reading rules, not defined terms |
| authorized person (Part IV) | Act s 81, l.1299 | by reference: encoded by piece ei3, s 81, taken there as an input |  |
| judge (Part IV) | Act s 81, l.1300 | by reference: encoded by piece ei3, s 81, taken there as an input |  |
| Minister (Part IV) | Act s 81, l.1301 | `eia-core` `Party` constructor `the Minister of National Revenue` | see Minister above |
| responsible representative | Act s 86(7), l.1393 | by reference: encoded by piece ei3, s 86, taken there as an input |  |
| authorized person (s 126) | Act s 126(22), l.1965 | by reference: encoded by piece ei4, s 126, taken there as an input |  |
| judge (s 126) | Act s 126(22), l.1966 | by reference: encoded by piece ei4, s 126, taken there as an input |  |
| benefit repayment | Act s 144, l.2057 | by reference: encoded by piece ei4, s 144 and s 145, taken there as an input |  |
| benefits (Part VII) | Act s 144, l.2058 | by reference: encoded by piece ei4, s 144, taken there as an input | differs from s 2(1) "benefits" |
| income of a person for a period | Act s 144, l.2059 | by reference: encoded by piece ei4, s 144, taken there as an input | three adjustments to the Income Tax Act income (a) to (c) |
| Minister (Part VII) | Act s 144, l.2063 | `eia-core` `Party` constructor `the Minister of National Revenue` | see Minister above |
| person (Part VII) | Act s 144, l.2064 | by reference: encoded by piece ei4, s 144, taken there as an input | the Income Tax Act's meaning |
| taxation year | Act s 144, l.2065 | by reference: encoded by piece ei4, s 144, taken there as an input | the Income Tax Act's meaning |
| sitting day | Act s 153(9), l.2709 | by reference: encoded by piece ei4, s 153, taken there as an input |  |
| business | Act s 152.01(1), l.2117 | by reference: encoded by piece ei5, s 152.01, taken there as an input |  |
| family member (Act) | Act s 152.01(1), l.2119 | repealed or blank in this text | [Repealed, 2017, c. 20, s. 242]; Reg 1(3) (l.20, er1) defines it |
| self-employed person | Act s 152.01(1), l.2122 | by reference: encoded by piece ei5, s 152.01, taken there as an input | Reg 1(1) l.15 (er1), Reg 30(5) l.485 (er2), Reg 35(1) l.553 (er3) refer to or redefine it; the keel supplies the `Party` constructor `the self-employed person` |
| a reference to earnings (s 152.151(b)) | Act s 152.151(b), l.2524 | by reference: encoded by piece ei5, s 152.151, taken there as an input | a reading rule, not a defined term |
| COVID-19 | Act s 153.5(1)(a), l.2768 | by reference: encoded by piece ei6, s 153.5, taken there as an input |  |
| claimant (Part VIII.4) | Act s 153.5(2), l.2772 | by reference: encoded by piece ei6, s 153.5, taken there as an input | differs from s 2(1) "claimant" |
| "entitled" read as "eligible" | Act s 153.6, l.2800 | by reference: encoded by piece ei6, s 153.6, taken there as an input | a reading rule, not a defined term |
| Census Agglomeration, Census Division, Census Metropolitan Area, Census Subdivision (Schedule VI) | Act Schedule VI s 1, l.3546-3549 | by reference: encoded by piece ei6, Schedule VI, taken there as an input | four terms; the Regulations' Schedule I (l.1762-1765, er6) defines the same four |
| board of referees, Pension Appeals Board, Review Tribunal, Social Security Tribunal, umpire (s 251) | Act s 251, l.3697-3701 | by reference: encoded by piece ei7, s 251, taken there as an input | five terms |
| Regulations (s 292(2)) | Act s 292(2), l.3845 | by reference: encoded by piece ei7, s 292, taken there as an input |  |
| Appeal Division, Board of Appeal, Employment Insurance Section, General Division, Tribunal (s 664) | Act s 664, l.3989-3993 | by reference: encoded by piece ei7, s 664, taken there as an input | five terms |
| Act (Regs) | Regs s 1(1), l.13 | nothing to encode | means the Employment Insurance Act |
| pay period | Regs s 1(1), l.14 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| self-employed person (Regs) | Regs s 1(1), l.15 | by reference: encoded by piece er1, reg 1, taken there as an input | same meaning as Act s 152.01(1), except in regs 30 and 35 |
| international organization | Regs s 1(2), l.16 | by reference: encoded by piece er1, reg 1, taken there as an input | licensed by s 5(7); used by `eia-core-insurable-employment` `s 5(2)(e)`, which takes the fact as a BOOLEAN |
| family member (Regs) | Regs s 1(3), l.20-37 | by reference: encoded by piece er1, reg 1, taken there as an input | seventeen paragraphs (a) to (q) |
| nurse practitioner | Regs s 1(3), l.38 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| guardian | Regs s 1(4), l.39 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| care | Regs s 1(5), l.41 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| support | Regs s 1(5), l.42 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| critically ill child | Regs s 1(6), l.44 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| critically ill adult | Regs s 1(7), l.46 | by reference: encoded by piece er1, reg 1, taken there as an input |  |
| agriculture | Regs s 9(1), l.105 | by reference: encoded by piece er1, reg 9, taken there as an input |  |
| agricultural enterprise | Regs s 9(1), l.119 | by reference: encoded by piece er1, reg 9, taken there as an input |  |
| horticulture | Regs s 9(1), l.120 | by reference: encoded by piece er1, reg 9, taken there as an input |  |
| Gaspesie-Iles-de-la-Madeleine, Lower St. Lawrence and North Shore, Madawaska-Charlotte, Restigouche-Albert | Regs s 17.1(1), l.254-257 | by reference: encoded by piece er1, reg 17.1, taken there as an input | four regions defined by pointing at Schedule I (er6) |
| condition of entitlement to benefits (reg 26.1) | Regs s 26.1(1), l.416 | by reference: encoded by piece er2, reg 26.1, taken there as an input | also reg 77(2) l.1399 (er5) |
| period of eligibility (reg 26.1) | Regs s 26.1(1), l.417 | by reference: encoded by piece er2, reg 26.1, taken there as an input | also reg 77(2) l.1400 (er5) |
| self-employed person (reg 30(5)) | Regs s 30(5), l.485 | by reference: encoded by piece er2, reg 30, taken there as an input |  |
| non-teaching period | Regs s 33(1), l.505 | by reference: encoded by piece er2, reg 33, taken there as an input |  |
| teaching | Regs s 33(1), l.506 | by reference: encoded by piece er2, reg 33, taken there as an input |  |
| cohabitating spouse or common-law partner (reg 34) | Regs s 34(1), l.514 | by reference: encoded by piece er2, reg 34, taken there as an input | the Income Tax Act's meaning |
| employment (reg 35) | Regs s 35(1), l.542 | by reference: encoded by piece er3, reg 35, taken there as an input | differs from Act s 2(1) "employment" |
| income | Regs s 35(1), l.548 | by reference: encoded by piece er3, reg 35, taken there as an input |  |
| pension | Regs s 35(1), l.549 | by reference: encoded by piece er3, reg 35, taken there as an input |  |
| self-employed person (reg 35) | Regs s 35(1), l.553 | by reference: encoded by piece er3, reg 35, taken there as an input | same meaning as reg 30(5) |
| living quarters | Regs s 35(16), l.605 | by reference: encoded by piece er3, reg 35, taken there as an input |  |
| average bank rate, bank rate, debt arising from an act or omission | Regs s 56.1(1), l.967-969 | by reference: encoded by piece er3, reg 56.1, taken there as an input | three terms |
| deduction | Regs s 57(1), l.986 | by reference: encoded by piece er3, reg 57, taken there as an input |  |
| plan (reg 60) | Regs s 60, l.1013 | by reference: encoded by piece er4, reg 60, taken there as an input |  |
| provincial benefits, provincial plan, variable administrative costs | Regs s 76.01, l.1178-1180 | by reference: encoded by piece er4, reg 76.01, taken there as an input | three terms |
| plan established under a provincial law, provincial benefits (reg 76.31) | Regs s 76.31, l.1325-1326 | by reference: encoded by piece er4, reg 76.31, taken there as an input | two terms, close to but not the same as reg 76.01's |
| long-tenured worker (reg 77.999) | Regs s 77.999(1), l.1631 | by reference: encoded by piece er5, reg 77.999, taken there as an input |  |
| long-tenured worker (reg 77.9994) | Regs s 77.9994(1), l.2519 | by reference: encoded by piece er6, reg 77.9994, taken there as an input |  |
| Census Agglomeration, Census Division, Census Metropolitan Area, Census Subdivision (Regs Schedule I) | Regs Schedule I s 1, l.1762-1765 | by reference: encoded by piece er6, Schedule I, taken there as an input | four terms |
| claimant, earnings, former Regulations, new Regulations (reg 350.1) | Regs s 350.1(2), l.2485-2488 | by reference: encoded by piece er6, reg 350.1, taken there as an input | four terms, for a transitional section; "claimant" there has the same meaning as Act s 2(1) |

Counts by kind, over 106 rows: 18 worked out from facts in the keel (a rule in `eia-core-interpretation` or `eia-core-insurable-employment`, or a helper in the core); 4 `Party` constructors; 7 s 2(1) terms whose meaning another piece carries (by reference); 5 repealed or blank; 2 with nothing to encode; 70 definitions that sit in another piece's range.

## Instructions to the pieces

**1. Files and imports.**
The stable `l4` resolves `IMPORT` only inside the importing file's own folder and its libraries, so a piece's folder holds byte-for-byte copies of the keel files it imports; do not edit a copy, report the wanted change to the keel.
Start every module with `IMPORT prelude`, `IMPORT daydate`, ``IMPORT `eia-core` `` and then any of ``IMPORT `eia-core-interpretation` ``, ``IMPORT `eia-core-insurable-employment` ``, ``IMPORT `eia-core-maximum-earnings` ``.
Importing all four keel modules together, and a piece's own record type that uses `Reason for benefits` and `Part of the Act`, ran clean in a throwaway file.

**2. Names that are taken.**
Every rule, constant and type the keel defines is in the Vocabulary table; the constructors and record fields are these.

```
`Period of days`  (record, fields in eia-core.l4)
    `first day of the period`
    `last day of the period`
`Reason for benefits`  (enum, constructors in eia-core.l4)
    `a reason other than those mentioned in subsection 12(3)`
    `pregnancy`
    `caring for a new-born or adopted child`
    `a prescribed illness, injury or quarantine`
    `care or support of a family member`
    `care or support of a critically ill child`
    `care or support of a critically ill adult`
`Election of maximum weeks`  (enum, constructors in eia-core.l4)
    `the 35-week maximum`
    `the 61-week maximum`
`Violation class`  (enum, constructors in eia-core.l4)
    `a minor violation`
    `a serious violation`
    `a very serious violation`
    `a subsequent violation`
`Party`  (enum, constructors in eia-core.l4)
    `the claimant`
    `the insured person`
    `the self-employed person`
    `the employer`
    `the Commission`
    `the Minister`
    `the Minister of National Revenue`
`Rate band`  (enum, constructors in eia-core.l4)
    `6% and under`
    `more than 6% but not more than 7%`
    `more than 7% but not more than 8%`
    `more than 8% but not more than 9%`
    `more than 9% but not more than 10%`
    `more than 10% but not more than 11%`
    `more than 11% but not more than 12%`
    `more than 12% but not more than 13%`
    `more than 13% but not more than 14%`
    `more than 14% but not more than 15%`
    `more than 15% but not more than 16%`
    `more than 16%`
`Part of the Act`  (enum, constructors in eia-core-interpretation.l4)
    `Part I`
    `Part II`
    `Part III`
    `Part IV`
    `Part V`
    `Part VI`
    `Part VII`
    `Part VII.1`
    `Part VIII`
    `Part VIII.1`
    `Part VIII.2`
    `Part VIII.3`
    `Part VIII.4`
    `Part VIII.5`
    `Part VIII.6`
    `Part IX`
`Kind of thing the definition of documents lists`  (enum, constructors in eia-core-interpretation.l4)
    `s 2(1) documents - money`
    `s 2(1) documents - securities`
    `s 2(1) documents - books`
    `s 2(1) documents - records`
    `s 2(1) documents - letters`
    `s 2(1) documents - telegrams`
    `s 2(1) documents - vouchers`
    `s 2(1) documents - invoices`
    `s 2(1) documents - accounts`
    `s 2(1) documents - statements, financial or otherwise`
    `s 2(1) documents - something not on the list`
`Published rate of unemployment`  (record, fields in eia-core-interpretation.l4)
    `date produced`
    `rate produced`
```

A piece's own types, constructors and fields begin with its id (`ei3 ...`, `er2 ...`); its rule names begin `s N` or `reg N`.

**3. Facts from outside your range: take these types.**

| fact | take as | name it | whose it is |
| --- | --- | --- | --- |
| maximum yearly insurable earnings for a year | NUMBER of dollars | `the maximum yearly insurable earnings for the year` | s 4 (keel) gives the formula; the published figure is outside the text, and the pieces that meet it take it as an input: ei1 (ss 14(1.1) and 17), ei3 (ss 82(2) and 95), ei4 (s 145) and ei5 (s 152.17(5), which also reads it "as calculated under section 4") |
| insurable employment, and an insured person | BOOLEAN, or call `s 5 insurable employment` and `s 2(1) insured person` | `is employed in insurable employment` | keel, s 5 |
| a regional rate of unemployment | NUMBER fraction (6.5% is 0.065) | `the regional rate of unemployment` | which region and which rate applies: reg 17 and Schedule I (er1, er6); the band: `the band of the regional rate of unemployment` |
| a benefit period, a qualifying period, a calculation period | `Period of days` (`first day of the period`, `last day of the period`, both inclusive) | `the benefit period`, `the qualifying period` | ei1 ss 8 to 10, ei5 ss 152.08 to 152.11 |
| hours, weeks, days, dollars | NUMBER | the Act's phrase | the piece that meets them |
| which Part a benefit is payable under | `Part of the Act` | `the Part under which the benefits are payable` | keel, `eia-core-interpretation` |
| the reason for the benefit | `Reason for benefits` | `the reason for the benefits` | keel, s 12(3) and s 152.14(1) |
| the election of 35 or 61 weeks | `Election of maximum weeks` | `the election under section 23` | keel; s 23(1.1) is ei1's |
| the class of a violation | `Violation class` | `the class of the violation` | keel, s 7.1(5) |
| a judgment the text leaves to an office | BOOLEAN named for the satisfaction | `the Commission is satisfied that ...` | the piece that meets it |
| a thing that is "prescribed" | the plain type of the thing, or BOOLEAN | the Act's phrase + `prescribed` | the piece that meets it names the regulation |

**4. Rounding and weeks.**
Where s 6(2) or s 152.01(5) says a percentage or fraction of earnings or benefits is rounded to the nearest dollar, call `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` (higher dollar when equidistant) and cite your own subsection; do not restate it.
Identify a week by the DATE of its Sunday and use `s 2(1) the Sunday that begins the week containing` where the text says "the Sunday of the week in which" (ss 10(1) and 152.11).
The nine-band tables (ss 7(2), 7.1(1), 14(2)) read the twelve-band `Rate band` with bands 9 to 12 together as "more than 13%".

**5. Reading rules that bind every piece (ss 2(3) and 2(4) are `inert` here for that reason).**
A document or communication under the Act or the Regulations may be in electronic form (s 2(3)): never add a paper-only condition to a form, record, book, notice, request, demand, decision or other document.
A reference to a claim for benefits includes the questions arising in relation to it, and "action on a claim" includes deciding a question for or against the claimant (s 2(4)): read "claim" and "action on a claim" that widely.
"Prescribed" means prescribed by the Regulations (s 2(1)): name the regulation or take the prescribed thing as an input.

**6. Dates and time.**
The text is one vintage; no keel rule carries a rule date, and neither should a piece unless its own provision names a date range.
Use `YMD`, never a literal `Date`; do not define `YMD` again.
A limit counted in months or years goes through `add months` and `add years` from `daydate`, which clamp to the last day of the month.

**7. Pieces and ranges** (from the brief; lines of the raw files).

| piece | covers |
| --- | --- |
| ei1 | Act 133-669 |
| ei2 | Act 670-1126 |
| ei3 | Act 1127-1803 |
| ei4 | Act 1804-2108 and 2689-2762 |
| ei5 | Act 2109-2688 |
| ei6 | Act 2763-3598 |
| ei7 | Act 3599-4201 |
| er1 | Regs 1-339 |
| er2 | Regs 340-539 |
| er3 | Regs 540-992 |
| er4 | Regs 993-1393 |
| er5 | Regs 1394-1708 |
| er6 | Regs 1709-2536 |

**8. Tripwires measured on the binary** (details under "What the stable binary does not accept").
`f (6.5%)`, not `f 6.5%`; a record type with spaces in its name is backticked before `OF`; `(f x)'s field` does not parse, so read a field in a rule that takes the record; `YMD` only in the core; every rule its own `GIVEN`; `MAYBE` and `NOTHING` for "the text does not say"; one-line `#ASSERT`.

## Coverage table

One row per heading, section, subsection and paragraph of lines 5 to 131 of the Act; lines 1 to 3 are the conversion's own header and lines 4, 8, 10, 14, 60, 72, 87 and 132 are blank.
A `where` that names a piece rather than a module is a by-reference row: the keel encodes nothing for it and gives the input type; the piece was assigned the section and had not delivered when this file was written.
Dispositions: `encoded`, `inert` (with its reason), `repealed or blank in this text`, `fork` (a reading recorded in the Fork register and encoded as shown).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Title block: title, citation, long title | 5-7 | inert | - | The title, the citation `S.C. 1996, c. 23` and the long title name the Act; they create no right, duty or fact, so there is nothing to ask a person or compute. |
| Enacting clause | 9 | inert | - | Records who enacted the Act; no question about benefits turns on it, and the enactment date is not in this text (see Dates above). |
| Heading "Short Title" | 11 | inert | - | A division heading; it carries no text of its own. |
| s 1 Short title | 12-13 | inert | - | Says how the Act may be cited; the encodings cite it by section in `@ref` lines, so no rule can use it. |
| Heading "Interpretation" | 15 | inert | - | A division heading; it carries no text of its own. |
| s 2(1) Definitions, lead-in "In this Act," | 16-17 | encoded | rows below | Makes each definition below apply throughout the Act; the Parts that define a term again for themselves are listed in Defined terms. |
| s 2(1) "affidavit" | 18 | encoded | `eia-core-interpretation` `s 2(1) affidavit` |  |
| s 2(1) "benefit period" | 19 | encoded | piece ei1, ss 9 and 10; piece ei5, ss 152.1 and 152.11 | By reference: the keel encodes nothing for it and gives the input type, a `Period of days`. |
| s 2(1) "benefits" | 20 | encoded | `eia-core-interpretation` `s 2(1) benefits` |  |
| s 2(1) "board of referees" | 21 | repealed or blank in this text | - | [Repealed, 2012, c. 19, s. 240] |
| s 2(1) "claimant" | 22 | encoded | `eia-core-interpretation` `s 2(1) claimant` |  |
| s 2(1) "Commission" | 23 | encoded | `eia-core` `Party` constructor `the Commission` | An office, used as a party in regulative rules. |
| s 2(1) "common-law partner" | 24 | fork | `eia-core-interpretation` `s 2(1) common-law partner` | F6: the year has no date to be counted to; the rule takes the day the question is asked. |
| s 2(1) "confirmed delivery service" | 25 | encoded | `eia-core-interpretation` `s 2(1) confirmed delivery service` |  |
| s 2(1) "documents" | 26 | encoded | `eia-core-interpretation` `s 2(1) documents includes` | An open list: JUST TRUE for a listed kind, NOTHING for anything else. |
| s 2(1) "dwelling-house" | 27-29 | encoded | `eia-core-interpretation` `s 2(1) dwelling-house` | Paragraphs (a) and (b) are the two inclusions. |
| s 2(1) "employee's premium" | 30 | encoded | piece ei3, s 67 | By reference: a NUMBER of dollars input. |
| s 2(1) "employer" | 31 | encoded | `eia-core-interpretation` `s 2(1) employer` |  |
| s 2(1) "employer's premium" | 32 | encoded | piece ei3, s 68 | By reference: a NUMBER of dollars input. |
| s 2(1) "employment" | 33 | encoded | `eia-core-interpretation` `s 2(1) employment` |  |
| s 2(1) "employment benefits" | 34 | repealed or blank in this text | - | [Repealed, 2022, c. 10, s. 387] |
| s 2(1) "employment support measure" | 35 | encoded | piece ei2, s 59 | By reference: a BOOLEAN input. |
| s 2(1) "insurable earnings" | 36 | encoded | piece ei3, Part IV | By reference: a NUMBER of dollars input. |
| s 2(1) "insurable employment" | 37 | encoded | `eia-core-insurable-employment` `s 5 insurable employment` | The definition itself sends the reader to s 5. |
| s 2(1) "insured person" | 38 | encoded | `eia-core-interpretation` `s 2(1) insured person` |  |
| s 2(1) "interruption of earnings" | 39 | encoded | piece er1, regs 14 and 14.01 | By reference: the circumstances are "determined by the regulations"; a BOOLEAN input. |
| s 2(1) "labour dispute" | 40 | encoded | `eia-core-interpretation` `s 2(1) labour dispute` |  |
| s 2(1) "long-tenured worker" | 41 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 207] |
| s 2(1) "Minister" | 42 | encoded | `eia-core` `Party`; `eia-core-interpretation` `s 2(1) the Minister for` | The Minister of National Revenue in Parts IV and VII. |
| s 2(1) "overpayment of benefits" | 43 | encoded | `eia-core-interpretation` `s 2(1) overpayment of benefits` | Only the exclusion belongs here; the positive meaning is piece ei4's (Part VI) and is an input. |
| s 2(1) "prescribed" | 44 | inert | - | It says that "prescribed" means prescribed by the regulations; it adds no condition of its own, so each piece that meets a prescribed thing names the regulation or takes the thing as an input. |
| s 2(1) "provincial law" | 45 | encoded | `eia-core-interpretation` `s 2(1) provincial law` |  |
| s 2(1) "rate of unemployment" | 46 | encoded | piece er1, reg 17; `eia-core-interpretation` `s 2(2)` | By reference: the rate is a NUMBER fraction input; the keel supplies the bands (`eia-core` `Rate band`) and the choice among published rates. |
| s 2(1) "regular benefits" | 47 | encoded | `eia-core-interpretation` `s 2(1) regular benefits` |  |
| s 2(1) "special benefits" | 48 | encoded | `eia-core-interpretation` `s 2(1) special benefits` |  |
| s 2(1) "umpire" | 49 | repealed or blank in this text | - | [Repealed, 2012, c. 19, s. 240] |
| s 2(1) "week" | 50 | encoded | `eia-core` `s 2(1) the Sunday that begins the week containing`; `eia-core-interpretation` `s 2(1) week` | A week is identified by the DATE of its Sunday. |
| s 2(1) "year" | 51 | encoded | `eia-core` `s 2(1) the year containing` |  |
| s 2(2) Rates of unemployment produced by Statistics Canada | 52-53 | fork | `eia-core-interpretation` `s 2(2) the rate of unemployment most recently produced` | F3: a rate produced on the day of the final determination counts. |
| s 2(3) Electronic documents and communication | 54-55 | inert | - | A reading rule: a document or communication may be in electronic form, and a reference to a form, record, notice, request, decision or other document includes an electronic one. It removes a requirement rather than imposing one, so there is no fact the person states and no outcome that differs; a piece must not add a paper-only or in-writing-on-paper condition to anything the text calls a document, and the Instructions say so. |
| s 2(4) References to claims for benefits | 56-57 | inert | - | A reading rule: a reference to a claim for benefits includes questions arising in relation to the claim, and "action on a claim" includes deciding a question for or against the claimant. It widens what other provisions mean and creates no fact; a piece that encodes a decision about a claim reads "claim" this widely, and the Instructions say so. |
| s 2(5) Weeks of benefits paid | 58-59 | inert | - | A power of the Commission, with the approval of the Governor in Council, to make regulations on how many weeks of benefits a claimant was paid, for s 145. Regulation 25 (l.406 of the Regulations, piece er2) exercises it, and that piece carries the rule; the power itself states no fact a person could give. |
| Heading "Report" | 61 | inert | - | A division heading; it carries no text of its own. |
| s 3(1) Commission to assess adjustment | 62-63 | inert | - | A duty on the Commission to monitor and assess how well the benefits and other assistance work, for individuals, communities and the economy; it produces a report about the programme and gives or takes nothing from a person who has lost work. |
| s 3(1)(a) | 64 | inert | - | Part of the same monitoring duty: how employees and employers use the benefits and assistance. |
| s 3(1)(b) | 65 | inert | - | Part of the same monitoring duty: the effect on claimants' obligation to be available for and seek work, and on employers' efforts to keep a stable workforce. The obligation itself is stated in Part I (piece ei1), not here. |
| s 3(2) Report | 66-67 | inert | - | A duty between two offices: the Commission reports to the Minister by March 31 after each year, and at other times on request. A person's entitlement does not turn on whether it does. |
| s 3(3) Tabling in Parliament | 68-69 | inert | - | A duty between the Minister and Parliament (lay each report within 30 days of receiving it, or on the first 30 sitting days if Parliament is not sitting). |
| s 3(4) Referral to committee | 70-71 | inert | - | House of Commons procedure: each report goes to the committee the House designates or establishes. |
| Heading "Maximum Yearly Insurable Earnings" | 73 | inert | - | A division heading; it carries no text of its own. |
| s 4(1) Maximum yearly insurable earnings | 74-75 | fork | `eia-core-maximum-earnings` `s 4(1) the maximum yearly insurable earnings for the year` | F1: no floor after the first exceedance (see s 4(3)). Pieces that use the figure (14(1.1), 17, 82(2), 95, 145, and 152.17(5), which reads it "as calculated under section 4") take it as a NUMBER input. |
| s 4(2) Calculation of amount, lead-in | 76-77 | encoded | `eia-core-maximum-earnings` `s 4(2) the amount calculated in accordance with subsection (2)` | 52 times the product of A and A over B. |
| s 4(2)(a) | 78 | encoded | `eia-core-maximum-earnings` `s 4(2)(a) the average of the Average Weekly Earnings for each month of a 12-month period` | Also the 12-month period itself. |
| s 4(2)(b) | 79-80 | encoded | `eia-core-maximum-earnings` `s 4(2)(b) the 12-month period ending 12 months prior to April 30 of that preceding year` | The ratio of the first average to the second. |
| s 4(3) Subsequent years | 81-82 | fork | `eia-core-maximum-earnings` `s 4(3) the amount calculated in accordance with subsection (3)` | F1: no floor. |
| s 4(4) Rounding down | 83-84 | encoded | `eia-core-maximum-earnings` `s 4(4) the amount rounded down to the nearest multiple of one hundred dollars` |  |
| s 4(5) Average Weekly Earnings | 85-86 | encoded | `eia-core-maximum-earnings` `s 4(2)(a) the average of the Average Weekly Earnings for each month of a 12-month period` | The monthly figures are Statistics Canada's and are inputs. |
| Heading "Insurable Employment" | 88 | inert | - | A division heading; it carries no text of its own. |
| s 5(1) Types of insurable employment, lead-in | 89-90 | encoded | `eia-core-insurable-employment` `s 5(1) insurable employment, before subsection (2)` |  |
| s 5(1)(a) | 91 | encoded | `eia-core-insurable-employment` `s 5(1)(a) employment under a contract of service or apprenticeship` | The "whether" clauses (written or oral, who pays, by time or piece) say what does not matter and have no input. |
| s 5(1)(b) | 92 | encoded | `eia-core-insurable-employment` `s 5(1)(b) employment by Her Majesty in right of Canada` | A subset of paragraph (a), kept because the Act states it. |
| s 5(1)(c) | 93 | encoded | `eia-core-insurable-employment` `s 5(1)(c) service in the Canadian Forces or in a police force` |  |
| s 5(1)(d) | 94 | encoded | `eia-core-insurable-employment` `s 5(1)(d) employment included by regulations` | One BOOLEAN input; regs 2 to 6 (piece er1) decide it. |
| s 5(1)(e) | 95 | encoded | `eia-core-insurable-employment` `s 5(1)(e) employment as the sponsor or co-ordinator of an employment support measure` |  |
| s 5(2) Excluded employment, lead-in | 96-97 | encoded | `eia-core-insurable-employment` `s 5(2) insurable employment does not include` |  |
| s 5(2)(a) | 98 | fork | `eia-core-insurable-employment` `s 5(2)(a) employment of a casual nature other than for the purpose of the employer's trade or business` | F7: "casual nature" is not defined in the Regulations, so it is a BOOLEAN input. |
| s 5(2)(b) | 99 | fork | `eia-core-insurable-employment` `s 5(2)(b) employment of a person by a corporation they control` | F5: whether control through other persons counts is not in the text. |
| s 5(2)(c) | 100 | fork | `eia-core-insurable-employment` `s 5(2)(c) employment by Her Majesty in right of a province` | F2: displaced by regulations under s 5(4)(d). |
| s 5(2)(d) | 101 | fork | `eia-core-insurable-employment` `s 5(2)(d) employment by a foreign government` | F2: displaced by regulations under s 5(4)(e). |
| s 5(2)(e) | 102 | fork | `eia-core-insurable-employment` `s 5(2)(e) employment by an international organization` | F2: displaced by regulations under s 5(4)(f). |
| s 5(2)(f) | 103 | encoded | `eia-core-insurable-employment` `s 5(2)(f) employment under an exchange program` |  |
| s 5(2)(g) | 104 | encoded | `eia-core-insurable-employment` `s 5(2)(g) employment that constitutes an exchange of work or services` |  |
| s 5(2)(h) | 105 | encoded | `eia-core-insurable-employment` `s 5(2)(h) employment excluded by regulations` | One BOOLEAN input; regs 7 and 8 (piece er1) decide it. |
| s 5(2)(i) | 106 | encoded | `eia-core-insurable-employment` `s 5(2)(i) employment if the employer and employee are not dealing with each other at arm's length` | With s 5(3). |
| s 5(3) Arm's length dealing, lead-in | 107-108 | encoded | `eia-core-insurable-employment` `s 5(2)(i) employment if the employer and employee are not dealing with each other at arm's length` | Both limbs are inputs because the Income Tax Act and the Minister of National Revenue decide them. |
| s 5(3)(a) | 109 | encoded | `eia-core-insurable-employment` `s 5(2)(i) employment if the employer and employee are not dealing with each other at arm's length` | The Income Tax Act decides whether persons are not at arm's length; one BOOLEAN input. |
| s 5(3)(b) | 110 | encoded | `eia-core-insurable-employment` `s 5(2)(i) employment if the employer and employee are not dealing with each other at arm's length` | Related persons are deemed to deal at arm's length if the Minister of National Revenue is satisfied of what the paragraph describes; the satisfaction is the Minister's, so it is a BOOLEAN input and never worked out. |
| s 5(4) Regulations to include employment, lead-in | 111-112 | inert | - | A power of the Commission, with the approval of the Governor in Council, to include kinds of employment by regulation; the regulations that use it are regs 2 to 6, which piece er1 encodes, and this module takes their result as the one BOOLEAN of s 5(1)(d). The power states no fact a person could give. |
| s 5(4)(a) | 113 | inert | - | Power to include employment outside Canada that would be insurable if in Canada; regs 4 and 5 look like its exercise (piece er1). |
| s 5(4)(b) | 114 | inert | - | Power to include the whole of an employment shared between insurable and other employment with one employer; not matched to a regulation by the keel. |
| s 5(4)(c) | 115 | inert | - | Power to include employment not under a contract of service but like it; reg 6 looks like its exercise (piece er1). |
| s 5(4)(d) | 116 | inert | - | Power to include employment by a province that waives the exclusion; reg 2(1) exercises it ("except for paragraph 5(2)(c)"), which is the reason for fork F2. |
| s 5(4)(e) | 117 | inert | - | Power to include employment by a foreign government that consents; reg 3(1) exercises it, with (f); fork F2. |
| s 5(4)(f) | 118 | inert | - | Power to include employment by an international organization that consents; reg 3(1) exercises it, with (e); fork F2. |
| s 5(4)(g) | 119 | inert | - | Power to include the tenure of an office as defined in the Canada Pension Plan; reg 6(f) looks like its exercise (piece er1). |
| s 5(5) Regulations to include persons in business | 120-121 | inert | - | A power to include the business activities of a person engaged in a business, with the approval of the Governor in Council and subject to affirmative resolution of Parliament; only the result is an input (s 5(1)(d)). No regulation under it was matched by the keel. |
| s 5(6) Regulations to exclude employment, lead-in | 122-123 | inert | - | A power to exclude kinds of employment by regulation; regs 7 and 8 (piece er1) use it, and this module takes their result as the one BOOLEAN of s 5(2)(h). |
| s 5(6)(a) | 124 | inert | - | Power to exclude employment where another country's laws would cause duplication of contributions or benefits; reg 7(c) and (d) deal with premiums payable under other countries' laws (piece er1). |
| s 5(6)(b) | 125 | inert | - | Power to exclude the whole of a split employment; not matched to a regulation by the keel. |
| s 5(6)(c) | 126 | inert | - | Power to exclude employment like employment that is not insurable; not matched to a regulation by the keel. |
| s 5(6)(d) | 127 | inert | - | Power to exclude a religious-order member who has taken a vow of poverty; reg 7(b) exercises it (piece er1). |
| s 5(6)(e) | 128 | inert | - | Power to exclude employment for no or nominal remuneration; not matched to a regulation by the keel. |
| s 5(6)(f) | 129 | inert | - | Power to exclude employment provided under s 24 or an employment support measure other than one in 59(c) or (d); reg 7(f) looks like its exercise (piece er1). |
| s 5(7) Defining certain expressions | 130-131 | inert | - | A power to define "casual nature", "government" and "international organization" for s 5. Reg 1(2) defines "international organization" (piece er1); nothing in the Regulations defines the other two, which is why s 5(2)(a) is fork F7 and s 5(2)(d) takes its fact as a BOOLEAN. |

Counts: 94 rows over 5 sections (ss 1 to 5): 46 encoded, 35 inert, 9 fork, 4 repealed or blank in this text.

## Fork register

Every entry is assumed, not ruled: the keel chose a reading so that work could go on, and each can be reversed in one place.

| id | provision | what the text leaves open | how it is encoded here | what would settle it |
| --- | --- | --- | --- | --- |
| F1 | s 4(3) (src:82), s 4(1) (src:75) | After a year in which the amount exceeds $39,000, a later year is the earlier year's amount before rounding down times the ratio; the text has no floor, so a later figure can come out below $39,000 (s 4(1) says only "$39,000 until" the first exceedance). | As written: no floor. Test: an earlier 41600 with ratio 0.8 gives 33280, rounded to 33200. NOTHING if either average is not above zero, since the text presupposes positive published earnings. | The published figures, or a ruling; the reading with a permanent floor of $39,000 would change `s 4(1) the maximum yearly insurable earnings for the year, before rounding down` only. |
| F2 | s 5(1) "Subject to subsection (2)" (src:90) with s 5(2)(c)-(e) (src:100-102) and s 5(4)(d)-(f) (src:116-118) | Paragraph (1)(d), employment included by regulations, is itself subject to s 5(2), yet s 5(4)(d) to (f) let regulations include employment by a province, a foreign government or an international organization, which s 5(2)(c), (d) and (e) exclude; regs 2(1) and 3(1) say "would, except for paragraph 5(2)(c) [or (d) and (e)] of the Act, be insurable employment". | Each of (2)(c), (d), (e) takes one more BOOLEAN, "included by regulations made under paragraph 5(4)(d) [(e), (f)]", that switches that exclusion off; the other six exclusions still apply to employment included by regulations. | The text of regs 2 and 3 (piece er1) or a ruling; read alone, s 5(2)(c) to (e) would defeat every regulation made under s 5(4)(d) to (f). |
| F3 | s 2(2) (src:53) | Whether a rate produced on the very day of the Commission's final determination was "most recently produced at the time". | It was: releases produced on or before the day count; the latest wins; NOTHING when there is none. | Statistics Canada's release practice and the Commission's; not in the text. |
| F4 | time limits throughout (the Interpretation Act is not deposited) | Whether the last day of "within n days after d" counts, and how weeks and months are counted. | The limit ends on d plus n and that day counts; weeks are 7 days; months and years go through `add months` and `add years`, which clamp to the last day of the month. | The Interpretation Act, not among the inputs; a piece that meets a limit says which reading it used. |
| F5 | s 5(2)(b) (src:99) | Whether shares controlled through related persons, or indirectly, count toward "controls more than 40% of the voting shares". | One NUMBER input, the portion of the voting shares the person controls, supplied by the caller; strictly more than 40% excludes, 40% does not. | The Income Tax Act or case law on control; outside the texts. |
| F6 | s 2(1) "common-law partner" (src:24) | The year of cohabitation is not tied to a date. | The first day of cohabitation plus one calendar year (`add years`, which clamps 29 February to 28 February) must be on or before the day the question is asked; the piece that uses the term passes the date its provision looks at. | The provision that uses the term, or a ruling. |
| F7 | s 5(2)(a) (src:98) with s 5(7) (src:131) | Section 5(7) lets regulations define "casual nature"; the Regulations text has no occurrence of the phrase. | A BOOLEAN input, `employment of a casual nature`. | A definition added by regulation. |

## What the stable binary does not accept

Binary: `l4 1.6.98 (main, 7689b0d, 2026-10-19)`.

**Measured by this keel** (a probe or a run, each reproduced in this session):

- `YMD` is undefined even after `IMPORT daydate`: "I could not find a definition for the identifier YMD"; the core defines it as `Date d m y`.
- A percent literal as a bare argument: `f 6%` gives "The argument of '%' is expected to be of type NUMBER" (the `%` takes the next token); write `f (6%)`.
- A record type whose name has spaces must be backticked before `OF`; `Period of days OF ...` is a parse error ("unexpected (").
- The possessive after a bracketed application, `(f x)'s field`, is a parse error ("unexpected 's"); read the field in a rule that takes the record.
- A type named `A` (or `B`) does not parse: `A` is a keyword.
- An `IMPORT` of a module that is not in the importing file's folder, the user library path or the binary's libraries fails with "I could not find a module with this name".

**From the skill's `dialects.md`, not re-measured here, and none is used in these files:**

`REFUSE` and `#ASSERT REFUSED`; `BECAUSE` outside `LEST BREACH ... BECAUSE`; a `GIVEN` on a section; `TYPICALLY`; opaque `DECLARE`; sets; the `hierarchy` and `negation-as-failure` imports; the ledger; `EVERY`; `RULES EFFECTIVE DATE` and the temporal built-ins; `@lang`; infix `EXPONENT` with imports; `MUST DO`; the spelling `WAIT UNTIL` (it is `WAITUNTIL`); an input named in an action (use a `PROVIDED` guard).

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core-tests-core.l4                         0        39       0        0         0
eia-core-tests-insurable-employment.l4         0        61       0        0         0
eia-core-tests-interpretation.l4               0        82       0        0         0
eia-core-tests-maximum-earnings.l4             0        36       0        0         0
eia-core.l4                                    0         0       0        0         0
TOTAL (8 modules)                              0       218       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <the Act's raw file> eia-core*.l4` prints:

```
srcrefs check: 113 src: lines, 60 runs, 91 locators, 0 problems
```
