# NOTES: Employment Insurance Regulations (SOR/96-332), piece er1: title, interpretation and Part I (benefits) first part, lines 1 to 339

Written by the piece agent `er1` (Sonnet 5.5) on 2026-10-24.
All nine layer-1 modules, their tests, the seat layer and its cases are written; PROGRESS.md is the working log.

**The text.**
`../../registers/source-bundle/SOR-96-332.txt` is an unofficial plain-text rendering, made by a converter script (`jl_xml2txt.py`), of the Justice Laws Website consolidation of SOR/96-332 current to 2026-09-30, last amended 2026-04-01.
It is not the official text and nothing here is verified against the official text.
The French version is equally authoritative and is not read; historical notes and footnotes are omitted from the conversion.
`src:N` is line N of that file.
**Which instrument each rule comes from.**
Every rule, type and quotation in the `er1-*.l4` files comes from the Regulations (SOR/96-332).
The Act is named only where a Regulations provision points into it (`section 5`, `7.1(6)(b)`, `152.07(1)(d)(i)` and the like); each such pointer is an input, listed under "Cross-references out of my ranges".
The core `eia-core*.l4` (the keel's) holds the Act's s 2 to s 5, the date shim and the shared enums; this piece imports it and defines none of its names.

## Seat

**The seat.** A person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission.
It is the seat the brief fixes; it follows `COMMONS-CLAUDE.md`: the individual to whom the law is applied, never the Commission, the Minister of National Revenue or a province.
**Why this seat for this range.** The Regulations' first part is the counting machinery under Part I of the Act: which work counts as insurable employment (regs 2 to 9), how many hours it is worth (regs 9.1 to 11), when earnings are interrupted (reg 14), what is deducted from benefits while on a course (reg 16), what job-search and suitable-work tests the claimant must meet (regs 9.001, 9.002), and which regional rate of unemployment fixes the hours and weeks (regs 17 and 17.1). Each of these is something a claimant asks about their own claim.
**What layer 2 is.** `er1-seat.l4` holds 63 exported questions, grouped under `§§` headings in the Regulations' order; every question has `@export` and, on every input, an `@desc` worded as the person would be asked. Each calls layer-1 rules and builds their records from plain inputs; none restates a rule. `er1-cases-seat.l4` has 172 assertions, at least one case for every question and most with a case that goes the other way.
**Seat conventions followed.** (1) A judgment the text hands to someone else is an input worded as that party's act ("the Minister of National Revenue has established ...", "my employer consents in writing"). (2) Where a rule returns `MAYBE`, the question returns it and a `NOTHING` is "this regulation does not fix the answer". (3) A fact that another provision of the Act decides (for instance "would be insurable employment but for paragraph 5(2)(c)") is asked as a yes/no the person can answer from that provision. (4) Provisions that state only an official's duty with no consequence for the person (reg 18(1), the establishment of regions; reg 18(2), the review of boundaries; reg 1(1) "pay period", used by other provisions; reg 1(1) "self-employed person", whose meaning is the Act's s 152.01(1)) are encoded in layer 1 and have no question.
**Where the seat differs from the Guide's defaults.** None known: the Regulations' own definitions are worked out from facts, borrowed terms (the Act's section 152.01(1), the Canada Pension Plan, the Financial Administration Act, the premiums regulations) are asked as facts, one case is one employment or one claim, and machinery is not asked about.
**The questions** (63), by group:
- Regulation 1: family member (1(3)); guardian and ward (1(4)); care and support (1(5)); critically ill child and adult (1(6), (7)); nurse practitioner (1(3)); international organization (1(2)).
- Regulations 2 to 6: provincial government (2); foreign government or international organization (3); ship (4); outside Canada (5); the seven kinds of work of reg 6, one question each.
- Regulations 7 to 9: religious order (7(b)); United States premiums (7(c)); resident of another country (7(d)); rescue operation (7(e)); employment support measure (7(f)); fair or circus (8(1)(a)); election or referendum (8(1)(c)); from when a short job is insurable (8(2), (3), (4)); agriculture, agricultural enterprise, horticulture (9(1)); farm work excluded (9(2)).
- Regulations 9.001 to 9.02: reasonable and customary efforts (9.001); suitable employment (9.002); notice ending a self-employed agreement (9.01); withdrawal (9.02).
- Regulations 9.1 to 11: the hours dispatcher (9.1, 10, 10.2); unpaid earnings (9.2); standby and presence (10.01); paid leave (10.1(1)); lump-sum leave (10.1(2)); paid non-working day (10.1(3)); limited full-time hours (11(1)); standby of Forces or police (11(2)(a)); reserve force (11(2)(b)).
- Regulations 11.1 and 13: the adjusted amount of self-employed earnings (11.1); average number of weeks (13(1), (2)).
- Regulation 14: has an interruption of earnings occurred (all routes); the day, for (2), (5)(a), (5)(b), (7) and 14.01.
- Regulations 14.1 and 16: the end of the period for undeclared earnings (14.1); the deduction on a course (16(1), (2)); the deduction for Part II payments (16(3)).
- Regulations 17 and 17.1: the rate from Statistics Canada's figures (17(1)); which region's rate (17(1.1) to (3)); the special rates for 2000 to 2012 (17.1); the Commission's notice (17.1(18)).

## Jural relations

A relation is stated once, neutrally, as a relation between two parties; the Regulations' counting rules (what counts as insurable employment, how many hours, when earnings are interrupted, which rate applies) create no relation of their own: the relations they feed are the Act's (the claimant's claim to benefits, the employer's duty to pay premiums), outside this range. They are listed once as `none`.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | section | L4 rule |
| --- | --- | --- | --- | --- | --- |
| definitions (family member, guardian, ward, care, support, critically ill child and adult, nurse practitioner, international organization, pay period, self-employed person) | none | none | none | reg 1 | `er1-interpretation` rules |
| province waives the exclusion | the province's government (power, by agreement with the Commission) | the Commission, and the province's employees engaged in such work (liability: their employment becomes insurable) | power / liability | reg 2(1), (2) | `reg 2(1) ...`, `reg 2(2) ...` |
| foreign government or international organization consents | the employing government or organization (power, by written consent) | the Commission, and the employees (liability: the employment becomes insurable) | power / liability | reg 3(1), (2) | `reg 3(1) ...`, `reg 3(2) ...` |
| inclusion of work: ships, outside Canada, the seven kinds | none (a counting rule; the claim to benefits and the duty to pay premiums are the Act's) | none | none | regs 4, 5, 6 | `reg 4 ...`, `reg 5 ...`, `reg 6 ...` |
| exclusion of work | none (a counting rule) | none | none | regs 7, 8(1), 9(2) | `reg 7(b)` to `(f)`, `reg 8(1)(a)`, `(c)`, `reg 9(2) ...` |
| the point from which a short job is insurable | none (a counting rule) | none | none | reg 8(2), (3), (4) | `reg 8(2) ...`, `(3)`, `(4)` |
| definitions of farm work | none | none | none | reg 9(1) | `reg 9(1) agriculture`, `agricultural enterprise`, `horticulture` |
| reasonable and customary efforts | the Commission (claim that the claimant make such efforts, and power to disentitle if not; the duty is the Act's s 50(8)) | the claimant (duty) | claim / duty | reg 9.001 | `reg 9.001 ...` |
| suitable employment | the claimant (privilege to refuse unsuitable work without disqualification; the privilege is the Act's ss 18 and 27) | the Commission (no-right to disqualify for it) | privilege / no-right | reg 9.002 | `reg 9.002(1) suitable employment` |
| notice to end the agreement, and its withdrawal | the Commission (claim to written notice) | the self-employed individual (duty to put the notice, and the withdrawal, in writing) | claim / duty | regs 9.01, 9.02 | `reg 9.01 ...`, `reg 9.02 ...` |
| hours of insurable employment | none (counting rules) | none | none | regs 9.1, 9.2, 10(1), (4), (5), (6), 10.01, 10.1, 10.11, 10.2, 11 | `er1-hours-of-insurable-employment` rules |
| agreement on hours | the employer and the worker or group (power to agree the hours) | the Commission and the Minister of National Revenue (liability: bound by a reasonable agreement) | power / liability | reg 10(2) | `reg 10(2) ...` |
| the Minister's figure of hours | the Minister of National Revenue (power to establish the hours) | the worker and the employer (liability) | power / liability | reg 10(3) | `reg 10(3) ...` |
| adjustment of the self-employed amount; the average number of weeks | none (arithmetic) | none | none | regs 11.1, 13 | `reg 11.1 ...`, `reg 13 ...` |
| interruption of earnings | none (a counting rule; the benefit period it triggers is the Act's) | none | none | regs 14, 14.01 | `reg 14 ...`, `reg 14.01 ...` |
| undeclared earnings: end of the period | none (a counting rule) | none | none | reg 14.1 | `reg 14.1 ...` |
| deduction while on a course; deduction of Part II payments | the Commission (power to deduct) | the claimant (liability: benefits reduced) | power / liability | reg 16(1), (3) | `reg 16(1) ...`, `reg 16(3) ...` |
| the rate of unemployment, the regions | none (counting rules) | none | none | regs 17, 17.1(1) to (17), 18(1) | `er1-rates-of-unemployment` rules |
| notice that the special rates have stopped | the public, and claimants (claim to publication; no right-holder is named in the text) | the Commission (duty to publish in the Canada Gazette and on its website) | claim / duty | reg 17.1(18) | `reg 17.1(18) ...` |
| review of regional boundaries | none identified (the text names no one to whom the duty is owed) | the Commission (duty to review at least every five years) | duty | reg 18(2) | `reg 18(2) ...` |

## Coverage table

Lines 1 to 3 are the converter's own header; blank lines (4, 8, 10, 47, 49, 80 and so on) carry no row.
Dispositions: `encoded`, `inert` (with its reason), `repealed or blank in this text`, `fork` (a reading recorded in the Fork register and encoded as shown; the row names the entry).
`where` names the module (`er1-...`) and the rule; a rule name begins `reg N(M)`.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Converter header | src:1-3 | inert | - | The converter's notice that this is an unofficial reproduction, the source URL and the currency date; it is not part of the Regulations and states no rule. |
| Title block: title, citation, enabling authority | src:5-7 | inert | - | The title `Employment Insurance Regulations`, the citation `SOR/96-332` and the name of the enabling Act; a pure title and citation, with no right, duty or fact. |
| Enacting words | src:9 | inert | - | The Governor in Council, on the Minister's recommendation, approves the Regulations made by the Commission under the listed provisions of the Act; a pure citation of the enabling provisions. It gives no date of making, so this piece carries no making date (see "What the text turns out to say", 1). |
| Heading "Interpretation" | src:11 | inert | - | A division heading; it carries no text of its own. |
| reg 1(1) lead-in | src:12 | encoded | rows below | Makes each definition of reg 1(1) apply in the Regulations; the rules below are named for the definition. |
| reg 1(1) "Act" | src:13 | inert | - | Says only that "Act" means the Employment Insurance Act: a pure citation; every rule here cites the Act by name. |
| reg 1(1) "pay period" | src:14 | encoded | `er1-interpretation` `reg 1(1) pay period` | The period earnings are paid to or enjoyed by an insured person in respect of. |
| reg 1(1) "self-employed person" | src:15 | encoded | `er1-interpretation` `reg 1(1) self-employed person, other than in sections 30 and 35` | The Act's s 152.01(1) meaning (piece ei5) is an input; NOTHING in regs 30 and 35, which define the word for themselves. |
| reg 1(2) "international organization" | src:16-18 | encoded | `er1-interpretation` `reg 1(2) international organization` | Paragraphs (a) and (b) are alternatives; the result is the input `by an international organization` of the core's `s 5(2)(e)` and of reg 3(1). |
| reg 1(3) lead-in | src:19 | encoded | rows below | Makes the two definitions apply in the Regulations and in the listed subsections of the Act. |
| reg 1(3) "family member" (a) to (q) | src:20-37 | encoded | `er1-interpretation` `reg 1(3) family member`, record `er1 Relationship to an individual` | Seventeen independent kinds of relationship, a checkbox record and a disjunction; paragraph (q) is an open standard taken as stated. |
| reg 1(3) "nurse practitioner" | src:38 | encoded | `er1-interpretation` `reg 1(3) nurse practitioner` | All six elements are required. |
| reg 1(4) "guardian" | src:39 | encoded | `er1-interpretation` `reg 1(4) guardian` | "includes" adds four named kinds to the general words. |
| reg 1(4) "ward" | src:39 | encoded | `er1-interpretation` `reg 1(4) ward` | A person for whom a guardian is appointed. |
| reg 1(5) lead-in | src:40 | encoded | rows below | Makes the two definitions apply in the Regulations and in the listed paragraphs of the Act. |
| reg 1(5) "care" | src:41 | encoded | `er1-interpretation` `reg 1(5) care` | Care required because of the state of health, other than care provided by a health care professional. |
| reg 1(5) "support" | src:42 | encoded | `er1-interpretation` `reg 1(5) support` | Psychological or emotional support required because of the state of health; no exception for professionals. |
| reg 1(6) "critically ill child" | src:43-44 | fork | `er1-interpretation` `reg 1(6) critically ill child` | F1: under 18 on the day the period in 23.2(3) or 152.061(3) begins (an input); the age test is shared with reg 1(7); a 29 February birth reaches 18 on 28 February in a year without one. |
| reg 1(7) "critically ill adult" | src:45-46 | fork | `er1-interpretation` `reg 1(7) critically ill adult` | F1: 18 or older on the day the period in 23.3(3) or 152.062(3) begins (an input). |
| Heading "Insurable Employment" | src:48 | inert | - | A division heading; it carries no text of its own. |
| Heading "Employment Included in Insurable Employment" | src:50 | inert | - | A division heading; it carries no text of its own. |
| reg 2(1) | src:51 | fork | `er1-insurable-employment` `reg 2(1) employment in Canada by Her Majesty in right of a province` | F2: one agreement with both undertakings. Province waives the s 5(2)(c) exclusion by agreement with the Commission; feeds the core's `included by regulations made under paragraph 5(4)(d)`. |
| reg 2(2) | src:52 | encoded | `er1-insurable-employment` `reg 2(2) employment by Her Majesty in right of a province, for the purposes of subsection (1)` | "includes only" public-service employees appointed and remunerated under the province's Act, or employees of its agent bodies. |
| reg 3(1) | src:53 | fork | `er1-insurable-employment` `reg 3(1) employment by a foreign government or an international organization` | F3: "may be included ... if ... consents in writing" is read as included on consent. |
| reg 3(2) | src:54 | encoded | `er1-insurable-employment` `reg 3(2) the consent is considered to be a consent referred to in subsection (1)` | An old consent under the Unemployment Insurance Regulations, not revoked. |
| reg 4 (a), (b)(i) to (iii) | src:55-60 | encoded | `er1-insurable-employment` `reg 4 employment on a ship outside Canada` | Canadian ship with an exception, or a foreign ship in one of three cases. |
| reg 5 (a) to (d) | src:61-65 | encoded | `er1-insurable-employment` `reg 5 employment outside Canada` | Four cumulative conditions. |
| reg 6 lead-in | src:66 | encoded | `er1-insurable-employment` `reg 6 employment included` | Any of paragraphs (a) to (g), unless a provision of the Regulations excludes it. |
| reg 6(a) | src:67 | encoded | `er1-insurable-employment` `reg 6(a) employment of a union member by the member's union` | Union business, not picketing. |
| reg 6(b) | src:68 | encoded | `er1-insurable-employment` `reg 6(b) employment of a person as an apprentice or trainee` | |
| reg 6(c) | src:69 | encoded | `er1-insurable-employment` `reg 6(c) employment of a person as a member of the clergy or of a religious order` | |
| reg 6(d) | src:70-72 | encoded | `er1-insurable-employment` `reg 6(d) employment in a barbering or hairdressing establishment` | Not the owner or operator. |
| reg 6(e) | src:73 | encoded | `er1-insurable-employment` `reg 6(e) employment as a driver of a vehicle that carries passengers` | Not owner of more than 50 per cent of the vehicle (50 per cent does not exclude). |
| reg 6(f) (i) to (iv) | src:74-78 | encoded | `er1-insurable-employment` `reg 6(f) employment of a person who holds an office` | Four kinds of office; (iv) only if not already included by (a). |
| reg 6(g) | src:79 | encoded | `er1-insurable-employment` `reg 6(g) employment of a person who is placed by a placement or employment agency` | |
| Regs 2 to 6 together | src:51-79 | encoded | `er1-insurable-employment` `reg 2 to 6 employment included in insurable employment` | The one input of the core's `s 5(1)(d)`; not a provision of its own. |
| Heading "Employment Excluded from Insurable Employment" | src:81 | inert | - | A division heading; it carries no text of its own. |
| reg 7 lead-in | src:82 | encoded | `er1-insurable-employment` `reg 7 employment excluded` | Any of paragraphs (b) to (f). |
| reg 7(a) | src:83 | repealed or blank in this text | `er1-insurable-employment` `reg 7(a) repealed in this text` | `[Repealed, SOR/97-310, s. 1]` |
| reg 7(b) | src:84 | encoded | `er1-insurable-employment` `reg 7(b) employment of a member of a religious order who has taken a vow of poverty` | |
| reg 7(c) | src:85-87 | encoded | `er1-insurable-employment` `reg 7(c) employment in respect of which premiums are payable under the law of the United States` | (i) needs "by reason of the Agreement"; (ii) does not. |
| reg 7(d) | src:88 | encoded | `er1-insurable-employment` `reg 7(d) employment in Canada of a person who resides in another country` | |
| reg 7(e) | src:89 | encoded | `er1-insurable-employment` `reg 7(e) employment for the purpose of a rescue operation` | |
| reg 7(f) | src:90-92 | encoded | `er1-insurable-employment` `reg 7(f) employment under an employment support measure` | |
| reg 8(1) lead-in | src:93 | encoded | rows below | "Subject to subsections (2) to (4)". |
| reg 8(1)(a) | src:94-96 | encoded | `er1-insurable-employment` `reg 8(1)(a) employment in connection with a circus, fair or similar activity` | Fewer than seven days in the year. |
| reg 8(1)(b) | src:97 | repealed or blank in this text | `er1-insurable-employment` `reg 8(1)(b) repealed in this text` | `[Repealed, SOR/98-588, s. 1]` |
| reg 8(1)(c) | src:98-100 | encoded | `er1-insurable-employment` `reg 8(1)(c) employment in connection with a referendum or election` | Fewer than 35 hours in a year after 1998. |
| reg 8(2) | src:101 | encoded | `er1-insurable-employment` `reg 8(2) the point from which the employment is insurable` | An excluded employment that becomes regular is insurable from the day or hour it became regular. |
| reg 8(3) | src:102 | encoded | `er1-insurable-employment` `reg 8(3) the day from which the employments taken together are insurable` | More than six days in the same year. |
| reg 8(4) | src:103 | encoded | `er1-insurable-employment` `reg 8(4) the hour from which the employments taken together are insurable` | More than 34 hours in the same year. |
| Regs 7 to 9 together | src:82-129 | encoded | `er1-insurable-employment` `reg 7 to 9 employment excluded from insurable employment` | The one input of the core's `s 5(2)(h)`; not a provision of its own. |
| reg 9(1) lead-in | src:104 | encoded | rows below | Makes the definitions apply in reg 9. |
| reg 9(1) "agriculture" | src:105-118 | fork | `er1-insurable-employment` `reg 9(1) agriculture`, `reg 9(1) agriculture, listed operations` | F4: the listed operations are agriculture in themselves ("includes"). |
| reg 9(1) "agricultural enterprise" | src:119 | encoded | `er1-insurable-employment` `reg 9(1) agricultural enterprise` | |
| reg 9(1) "horticulture" | src:120-126 | fork | `er1-insurable-employment` `reg 9(1) horticulture` | F5: (a)(i) and (a)(ii) are alternatives. |
| reg 9(2) | src:127-129 | encoded | `er1-insurable-employment` `reg 9(2) employment in agriculture, an agricultural enterprise or horticulture` | Fewer than seven days, or seven or more and no cash pay. |

| Heading "Search for Suitable Employment" | src:131 | inert | - | A division heading; it carries no text of its own. |
| Heading "Reasonable and Customary Efforts" | src:133 | inert | - | A division heading; it carries no text of its own. |
| reg 9.001 lead-in, (a), (b)(i) to (ix), (c) | src:134-146 | fork | `er1-search-for-employment` `reg 9.001(b) the claimant's efforts consist of one or more of the listed kinds of effort`, `reg 9.001 the claimant's efforts to obtain suitable employment are reasonable and customary efforts` | F6: the nine kinds in (b) are read as alternatives (at least one). (a) and (c) are inputs of the whole rule. |
| Heading "Suitable Employment" | src:148 | inert | - | A division heading; it carries no text of its own. |
| reg 9.002(1) lead-in, (a), (b), (c) | src:149-152 | fork | `er1-search-for-employment` `reg 9.002(1) suitable employment` | F10: "not incompatible with ... family obligations or religious beliefs" is read as compatible with both. |
| reg 9.002(1)(d) to (f) | src:153 | repealed or blank in this text | `er1-search-for-employment` `reg 9.002(1)(d) to (f) repealed in this text` | `[Repealed, SOR/2016-162, s. 1]` |
| reg 9.002(2) and (3) | src:154 | repealed or blank in this text | `er1-search-for-employment` `reg 9.002(2) and (3) repealed in this text` | `[Repealed, SOR/2017-27, s. 1]` |
| reg 9.003 | src:155 | repealed or blank in this text | `er1-search-for-employment` `reg 9.003 repealed in this text` | `[Repealed, SOR/2016-162, s. 2]` |
| reg 9.004 | src:156 | repealed or blank in this text | `er1-search-for-employment` `reg 9.004 repealed in this text` | `[Repealed, SOR/2016-162, s. 2]` |
| Heading "Agreement — Self-Employed Person" | src:158 | inert | - | A division heading; it carries no text of its own. |
| Heading "Termination of Agreement — Notice" | src:160 | inert | - | A division heading; it carries no text of its own. |
| reg 9.01 | src:161 | encoded | `er1-self-employed-agreement` `reg 9.01 the notice to terminate the agreement is given in the form the Regulations require` | The individual's notice to the Commission under 152.02(4) of the Act must be in writing. |
| Heading "Withdrawal of Notice" | src:163 | inert | - | A division heading; it carries no text of its own. |
| reg 9.02 | src:164 | encoded | `er1-self-employed-agreement` `reg 9.02 the withdrawal of the notice is given in the form the Regulations require` | The withdrawal under 152.02(6)(b) of the Act must be given to the Commission in writing. |
| Heading "PART I Benefits" | src:166 | inert | - | A Part heading; it carries no text of its own. |
| Heading "Hours of Insurable Employment — Methods of Determination" | src:168 | inert | - | A division heading; it carries no text of its own. |
| reg 9.1 | src:169 | encoded | `er1-hours-of-insurable-employment` `reg 9.1 the hours considered to have been worked by a person paid on an hourly basis` | Hours actually worked and remunerated, fraction counted as a whole hour. |
| reg 9.2 | src:170 | fork | `er1-hours-of-insurable-employment` `reg 9.2 the hours deemed to have been worked where earnings remain unpaid` | F7: "Subject to section 10" is read as: where a section 10 method fixes the hours, NOTHING here. |
| reg 10(1) | src:171 | encoded | `er1-hours-of-insurable-employment` `reg 10(1) the hours deemed to have been worked where the employer provides evidence` | |
| reg 10(2) | src:172 | fork | `er1-hours-of-insurable-employment` `reg 10(2) the hours deemed to have been worked where the parties agree`, `reg 10(2) the employer cannot establish the hours and neither subsection (1) nor section 9.1 applies` | F16: "Except where subsection (1) and section 9.1 apply" is read as except where either applies. The second rule is the shared condition. |
| reg 10(3) | src:173 | encoded | `er1-hours-of-insurable-employment` `reg 10(3) the hours deemed to have been worked as established by the Minister of National Revenue` | The Minister's figure is the Minister's judgment: an input. |
| reg 10(4) | src:174 | fork | `er1-hours-of-insurable-employment` `reg 10(4) the hours deemed to have been worked where the actual hours are not known` | F8: (4) overlaps (2) and (3); read as governing when the hours are "not known or ascertainable". F16: "Except where subsection (1) and section 9.1 apply" as in (2). |
| reg 10(5) | src:175 | fork | `er1-hours-of-insurable-employment` `reg 10(5) the maximum number of hours of insurable employment deemed under subsection (4)` | F9: "seven hours per day" is taken per calendar day of the period of employment. |
| reg 10(6) | src:176 | fork | `er1-hours-of-insurable-employment` `reg 9.1 and reg 10(1) to (6) the hours fixed by the first method that applies` | F8: the order of the answers; reg 10.1 prevails (NOTHING when it fixes the hours). |
| reg 10(7) | src:177 | repealed or blank in this text | `er1-hours-of-insurable-employment` `reg 10(7) repealed in this text` | `[Repealed, SOR/97-31, s. 4]` |
| reg 10.01(1) | src:178 | encoded | `er1-hours-of-insurable-employment` `reg 10.01(1) the hours of availability deemed to be hours of insurable employment` | Paid at a rate equal to or above the working rate. |
| reg 10.01(2) | src:179 | encoded | `er1-hours-of-insurable-employment` `reg 10.01(2) the hours of presence at the premises deemed to be hours of insurable employment`, `reg 10.01 the hours deemed to be hours of insurable employment` | "Despite subsection (1)": (2) is taken first. |
| reg 10.1(1) | src:180 | encoded | `er1-hours-of-insurable-employment` `reg 10.1(1) the hours deemed to have been worked during a period of paid leave` | |
| reg 10.1(2) | src:181-183 | encoded | `er1-hours-of-insurable-employment` `reg 10.1(2) the hours deemed to have been worked during a period of leave paid as a lump sum` | The lesser of (a) and (b). |
| reg 10.1(3) | src:184-186 | encoded | `er1-hours-of-insurable-employment` `reg 10.1(3) the hours deemed to have been worked on a non-working day` | (a) the greater of hours worked and hours normally worked; (b) hours normally worked. |
| reg 10.11 | src:187 | encoded | `er1-hours-of-insurable-employment` `reg 10.11 the amount to be taken into account in determining the hours` | The excluded amounts (subsection 2(3) of the Insurable Earnings and Collection of Premiums Regulations) are an input. |
| reg 10.2 lead-in | src:188 | encoded | rows below | "For the purposes of sections 9.1, 10, 10.01, 10.1 and 22": every rule of the hours module rounds up through (b). |
| reg 10.2(a) | src:189 | encoded | `er1-hours-of-insurable-employment` `reg 10.2(a) the number of hours of insurable employment` | An overtime hour is one hour. |
| reg 10.2(b) | src:190 | encoded | `er1-hours-of-insurable-employment` `reg 10.2(b) hours with a fraction of an hour counted as a whole hour` | CEILING. |
| reg 11(1) | src:191 | encoded | `er1-hours-of-insurable-employment` `reg 11(1) the hours per week deemed to be worked in an occupation with limited full-time hours` | Deems 35 hours a week. |
| reg 11(2) lead-in | src:192 | encoded | rows below | "Subject to section 10": see F7. |
| reg 11(2)(a) | src:193 | fork | `er1-hours-of-insurable-employment` `reg 11(2)(a) the hours per week deemed to be worked by a member of the Canadian Forces or of a police force on standby` | F7. |
| reg 11(2)(b)(i), (ii) and the closing words | src:194-197 | fork | `er1-hours-of-insurable-employment` `reg 11(2)(b) the hours per week deemed to be worked by a member of the reserve force` | F7; a period over 24 hours is not provided for (NOTHING). |
| Heading "Adjustment of Amount of Self-employed Earnings" | src:199 | inert | - | A division heading; it carries no text of its own. |
| reg 11.1(1) | src:200 | fork | `er1-self-employed-earnings` `reg 11.1(1) the adjusted amount for the year`, `reg 11.1(1) the adjusted amount after the years` | F11: each year's adjusted amount is rounded down before the next year's adjustment. The ratio of paragraph 4(2)(b) and the base amount of 152.07(1)(d)(i) are inputs. |
| reg 11.1(2) | src:201 | encoded | `er1-self-employed-earnings` `reg 11.1(2) the ratio after the floor of 1.0` | A ratio below 1.0 that would take the amount below $6,000 counts as 1.0. |
| reg 11.1(3) | src:202 | encoded | `er1-self-employed-earnings` `reg 11.1(3) the adjusted amount rounded down to the nearest dollar` | |
| reg 12 | src:203 | repealed or blank in this text | `er1-self-employed-earnings` `reg 12 repealed in this text` | `[Repealed, SOR/2016-206, s. 1]` |
| Heading "Average Number of Weeks for the Purposes of Paragraphs 7.1(6)(b) and 152.07(3)(b) of the Act" | src:205 | inert | - | A division heading; it carries no text of its own. |
| reg 13(1) | src:206 | encoded | `er1-self-employed-earnings` `reg 13(1) the average number of weeks of regular benefits of a claimant` | (maximum weeks - weeks paid) / 2; NOTHING when more weeks were paid than the maximum. |
| reg 13(2) | src:207 | encoded | `er1-self-employed-earnings` `reg 13(2) the average number of weeks of benefits of a self-employed person` | The same with the maximum in 152.14(1). |
| Heading "Interruption of Earnings" | src:209 | inert | - | A division heading; it carries no text of its own. |
| reg 14(1) | src:210 | encoded | `er1-interruption-of-earnings` `reg 14(1) an interruption of earnings occurs on lay-off or separation` | Seven or more consecutive days with no work and no earnings from the job. No day of occurrence is stated (F12). |
| reg 14(2) | src:211 | encoded | `er1-interruption-of-earnings` `reg 14(2) a reduction in earnings that is more than 40% of the insured person's normal weekly earnings`, `reg 14(2) the day on which an interruption of earnings occurs because of a reduction in earnings`, `reg 14(2) the reason is a circumstance listed in subsection (2)` | More than 40 per cent; occurs at the beginning of the week. |
| reg 14(3) | src:212 | fork | `er1-interruption-of-earnings` `reg 14(3) a period of leave referred to in subsection 11(4) of the Act does not constitute an interruption of earnings` | F12: applied to every route. |
| reg 14(4) | src:213 | fork | `er1-interruption-of-earnings` `reg 14(4) no interruption of earnings occurs during a period greater than a week for which the usual remuneration is payable` | F12: applied to every route. |
| reg 14(5) lead-in | src:214 | encoded | rows below | |
| reg 14(5)(a) | src:215-217 | encoded | `er1-interruption-of-earnings` `reg 14(5)(a) the day on which an interruption of earnings occurs for a real estate salesperson on commission` | |
| reg 14(5)(b) | src:218-220 | fork | `er1-interruption-of-earnings` `reg 14(5)(b) the day on which an interruption of earnings occurs for a person whose earnings are mainly commissions` | F17: "mainly" is a fact the person states; no threshold is encoded. |
| reg 14(6) | src:221 | fork | `er1-interruption-of-earnings` `reg 14(6) a period of leave referred to in subsection 11(3) of the Act does not constitute an interruption of earnings` | F12: applied to every route. |
| reg 14(7) | src:222 | encoded | `er1-interruption-of-earnings` `reg 14(7) the day on which an interruption of earnings occurs when less remunerative work is accepted` | |
| reg 14 together | src:210-222 | fork | `er1-interruption-of-earnings` `reg 14 an interruption of earnings has occurred` | F12. The one BOOLEAN that the core calls `an interruption of earnings has occurred` (s 2(1)). |
| reg 14.01 | src:223 | encoded | `er1-interruption-of-earnings` `reg 14.01 the day on which an interruption of earnings of a self-employed person occurs` | More than 40 per cent of the normal level; the week of the declaration. |
| Heading "Undeclared Earnings Referred to in Subsection 19(3) of the Act" | src:225 | inert | - | A division heading; it carries no text of its own. |
| reg 14.1 | src:226 | encoded | `er1-undeclared-earnings-and-courses` `reg 14.1 the day on which the period ends`, `reg 14.1 August 12, 2001` | A period that began before and was to end on or after August 12, 2001 ends on that day; not spent, it still fixes an end date. |
| reg 15 | src:227 | repealed or blank in this text | `er1-undeclared-earnings-and-courses` `reg 15 repealed in this text` | `[Repealed, SOR/2001-291, s. 2]` |
| Heading "Deductions for Earnings or Allowances While on a Course or Program of Instruction or Training" | src:229 | inert | - | A division heading; it carries no text of its own. |
| reg 16(1) | src:230-232 | encoded | `er1-undeclared-earnings-and-courses` `reg 16(1) the amount deducted from the benefits for a week of unemployment while attending a course or program` | Not for a course the Commission referred the claimant to. |
| reg 16(2) | src:233-235 | encoded | `er1-undeclared-earnings-and-courses` `reg 16(2) the allowances referred to in subsection (1)` | |
| reg 16(3) | src:236-239 | encoded | `er1-undeclared-earnings-and-courses` `reg 16(3) the amount deducted from the benefits for the weeks for which Part II earnings or allowances were paid` | (a), (b) and (c) are cumulative; within each, the alternatives are alternatives. |
| Heading "Rates of Unemployment" | src:241 | inert | - | A division heading; it carries no text of its own. |
| reg 17(1) | src:242-246 | encoded | `er1-rates-of-unemployment` `reg 17(1) the regional rate of unemployment that applies to a claimant, for a region`, `reg 17(1) the average of the seasonally adjusted monthly rates of unemployment for the period` | Sections 2 to 11 of Schedule I: the three-month average; sections 12 to 14: the greater of that and the 12-month average. |
| reg 17(1.1) | src:247-249 | fork | `er1-rates-of-unemployment` `reg 17(1.1) the regional rate of unemployment that applies to a claimant` | F15: (b) omits section 12, so a claimant resident outside Canada has no rate for s 12 from this regulation. |
| reg 17(2) | src:250 | encoded | `er1-rates-of-unemployment` `reg 17(2) and (3) the highest of the regional rates that apply in respect of each of those regions` | |
| reg 17(3) | src:251 | encoded | `er1-rates-of-unemployment` `reg 17(2) and (3) the highest of the regional rates that apply in respect of each of those regions` | The same rule as (2), for the last-employed region. |
| reg 17(4) | src:252 | encoded | `er1-rates-of-unemployment` `reg 17(4) the seasonally adjusted monthly rates are those that incorporate the estimate for status Indians living on Indian reserves` | A condition on the data; the averaging rule returns NOTHING without it. |
| reg 17.1(1) | src:253-257 | encoded | `er1-rates-of-unemployment` `er1 Region named in regulation 17.1`, `reg 17.1(1) the subsection of Schedule I that describes the region` | Four names that point at Schedule I (piece er6). |
| reg 17.1(2) | src:258-262 | fork | `er1-rates-of-unemployment` `reg 17.1(2) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, resident, September 17, 2000 to October 6, 2001. |
| reg 17.1(3) | src:263-267 | fork | `er1-rates-of-unemployment` `reg 17.1(3) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, outside Canada, same period. |
| reg 17.1(4) | src:268-270 | fork | `er1-rates-of-unemployment` `reg 17.1(4) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, resident, October 7, 2001 to October 12, 2002. |
| reg 17.1(5) | src:271-273 | fork | `er1-rates-of-unemployment` `reg 17.1(5) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, outside Canada, same period. |
| reg 17.1(6) | src:274-283 | fork | `er1-rates-of-unemployment` `reg 17.1(6) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, resident, October 13, 2002 to April 7, 2012, three formulas; ends under (16). |
| reg 17.1(7) | src:284-293 | fork | `er1-rates-of-unemployment` `reg 17.1(7) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Madawaska - Charlotte, outside Canada, same periods; ends under (16). |
| reg 17.1(8) | src:294-298 | fork | `er1-rates-of-unemployment` `reg 17.1(8) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, resident, September 17, 2000 to October 6, 2001. |
| reg 17.1(9) | src:299-303 | fork | `er1-rates-of-unemployment` `reg 17.1(9) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, outside Canada, same period. |
| reg 17.1(10) | src:304-306 | fork | `er1-rates-of-unemployment` `reg 17.1(10) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, resident, October 7, 2001 to October 12, 2002. |
| reg 17.1(11) | src:307-309 | fork | `er1-rates-of-unemployment` `reg 17.1(11) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, outside Canada, same period. |
| reg 17.1(12) | src:310-319 | fork | `er1-rates-of-unemployment` `reg 17.1(12) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, resident, October 13, 2002 to April 7, 2012; ends under (17). |
| reg 17.1(13) | src:320-329 | fork | `er1-rates-of-unemployment` `reg 17.1(13) ...` (the wrapper named for the subsection and region) | F13: the date tested is the Sunday of the week referred to in subsection 10(1). Lower St. Lawrence and North Shore, outside Canada, same periods; ends under (17). |
| reg 17.1(14) | src:330 | encoded | `er1-rates-of-unemployment` `reg 17.1(14) the highest of the regional rates for a claimant who resides near the boundaries of more than one region` | |
| reg 17.1(15) | src:331 | encoded | `er1-rates-of-unemployment` `reg 17.1(15) the highest of the regional rates for a claimant last employed near the boundaries of more than one region` | |
| reg 17.1(16) | src:332 | encoded | `er1-rates-of-unemployment` `reg 17.1(16) and (17) the Sunday after the day on which the hours and weeks are exactly the same`, `reg 17.1(16) and (17) the subsection has effect on the day` | Whether the condition has been met depends on the Act's tables (outside the range): an input. |
| reg 17.1(17) | src:333 | encoded | `er1-rates-of-unemployment` `reg 17.1(16) and (17) ...` | The same rule as (16), for subsections (12) and (13). |
| reg 17.1(18) | src:334 | encoded | `er1-rates-of-unemployment` `reg 17.1(18) the Commission has published the notice as required` | The Commission's duty to publish a notice; the cessation in (16) and (17) does not wait for it. |
| reg 17 with reg 17.1 | src:242, 258 | fork | `er1-rates-of-unemployment` `reg 17.1 the first answer that applies`, `reg 17 and reg 17.1 the regional rate of unemployment that applies to the claimant` | F14: where reg 17.1 gives "the applicable regional rate" it prevails over reg 17(1.1) to (3). |
| Heading "Regions" | src:336 | inert | - | A division heading; it carries no text of its own. |
| reg 18(1) | src:337 | encoded | `er1-rates-of-unemployment` `reg 18(1) the region is established for the purposes of Parts I and VIII of the Act` | Schedule I (piece er6) holds the regions. |
| reg 18(2) | src:338 | encoded | `er1-rates-of-unemployment` `reg 18(2) the Commission's review of the boundaries is not overdue` | The Commission's duty to review at least every five years; no consequence for the person is stated. |

The table ends with line 338; line 339 is blank and line 340 begins piece er2.

## Fork register

Every entry is "assumed, not ruled": a reading chosen so that the work could go on, each reversible in one place.

| id | provision | what the text leaves open | readings seen | how it is encoded here | what would settle it |
| --- | --- | --- | --- | --- | --- |
| F1 | reg 1(6), (7) (src:44, 46) | Which day a person born on 29 February reaches 18 in a year without a 29 February. | (1) 28 February (`add years` clamps); (2) 1 March. | (1), through the core's `add years` convention (keel F4/F6). Tested in `er1-tests-interpretation` and marked there as following the reading, not the text. | The Interpretation Act (not among the inputs). |
| F2 | reg 2(1) with the core's s 5(2)(c) (src:51) | Whether the agreement must contain both undertakings (waive the exclusion, insure all its employees) in one agreement. | One agreement with both undertakings; two separate agreements. | One agreement with both undertakings; the inputs are three BOOLEANs (agreement, waiver, insures all). | The agreements themselves. |
| F3 | reg 3(1) (src:53) | "may be included in insurable employment if the employing government or the international organization ... consents in writing": whether consent makes the inclusion automatic or leaves a further discretion. | (1) consent is the only condition, so consent includes; (2) consent is necessary but the Commission may still decline. | (1): the text states no other condition and no decision-maker. | A ruling on how the Commission applies reg 3(1). |
| F4 | reg 9(1) "agriculture" (src:105-118) | "means the operations of farming that are carried out for the benefit of any person who is a farmer and, without limiting the generality of the foregoing, includes ...": whether a listed operation must also be for the benefit of a farmer. | (1) listed operations are agriculture whatever else is true (they are inclusions); (2) every operation, listed or not, must be for a farmer's benefit. | (1): `reg 9(1) agriculture` is the base meaning OR the listed operation with its own conditions. | A ruling. |
| F5 | reg 9(1) "horticulture" (src:121-123) | Paragraph (a) lists two things with "and": (i) vegetables, flowers, shrubs or ornamental grasses, and (ii) their seeds, seedlings, grafts or cuttings. | (1) either is horticulture; (2) a single operation must be both. | (1): the "and" joins two products that each stand alone. | A ruling. |
| F6 | reg 9.001(b) (src:136-145) | The nine kinds of effort are joined by "and" ("... (viii) attending interviews, and (ix) undergoing evaluations of competencies"). | (1) the claimant's efforts must consist of at least one of the nine; (2) of all nine. | (1): the paragraph names kinds of effort, and (2) could not be satisfied by anyone who has not yet been interviewed or assessed. | A ruling or a Commission policy statement. |
| F7 | reg 9.2 (src:170), reg 11(2) (src:192) | "Subject to section 10": which of the two prevails where both could apply, and what "applies" means. | (1) where a section 10 method fixes the hours the section 10 number governs and the subject rule answers nothing; (2) the section 10 number is only a floor. | (1): the rule takes a BOOLEAN `section 10 fixes the person's hours ...` and answers NOTHING when it is TRUE. | A ruling on how the two regulations combine. |
| F8 | reg 10(2), (3) and (4) (src:172-174), reg 10(6) (src:176) | Reg 10(2) and (3) apply where the employer "cannot establish with certainty" the hours; reg 10(4) where they are "not known or ascertainable". Every case of (4) is a case of (2), and (3) always yields a number, so read alone (4) could never apply. | (1) (4) takes precedence where its condition is met, (2) and (3) apply otherwise; (2) and (3) take precedence and (4) is dead text; (3) the parties choose. | (1), so that (4) has a domain. The dispatcher `reg 9.1 and reg 10(1) to (6) ...` orders the answers 9.1, 10(1), 10(4), 10(2), 10(3). Reg 10(6) (all subject to reg 10.1) is the first test: NOTHING when reg 10.1 fixes the hours. | A ruling or the Commission's practice. |
| F9 | reg 10(5) (src:175) | "seven hours per day up to an overall maximum of 35 hours per week": whether a day is each day of the period of employment or only days worked; and what a week is. | (1) every calendar day of the period of employment, weeks being the Act's weeks (Sunday to Saturday); (2) only days actually worked (not known to the employer, which is why reg 10(4) applies). | (1), computed week by week as the sum of min(35, 7 x days of the period in the week). | A ruling. |
| F10 | reg 9.002(1)(b) and (c) (src:151-152) | "not incompatible with the claimant's family obligations or religious beliefs": "not (A or B)" or "(not A) or B". | (1) compatible with both, and likewise for (c); (2) compatible with at least one. | (1): the inputs are the clashes, each negated. | A ruling. |
| F11 | reg 11.1(1) to (3) (src:200-202) | Whether the rounding down of (3) is applied to each year's adjusted amount before the next year's adjustment, or only to the final amount. | (1) each year's amount is rounded down and the next year's ratio applies to the rounded amount; (2) the unrounded amount is carried and only the last is rounded. | (1): "that amount shall be rounded down" refers to the adjusted amount, which the next adjustment "compounds". With 6000 and two years of 1.0123 the readings give 6147 and 6148. | The Commission's published figures, or a ruling. |
| F12 | reg 14(1) to (7) (src:210-222) | (a) On which day an interruption under (1) occurs (the text says "occurs where"). (b) Whether (3), (4) and (6) ("does not constitute", "no interruption ... occurs during that period") limit every route or only (1), which is "Subject to subsections (2) to (7)". | (a) the first day of the seven; the last; the day of the lay-off. (b) every route; only (1). | (a) not decided: reg 14(1) returns only whether an interruption occurs. (b) every route: (3), (4) and (6) are stated generally. | The Act's s 10(1) practice, or a ruling. |
| F13 | reg 17.1(2) to (13) (src:258-329) | Which day is tested against "the period beginning on ... and ending on ...". | (1) the Sunday of the week referred to in subsection 10(1) (the week the benefit period begins); (2) the day of the claim; (3) each week of benefits. | (1): reg 17 itself fixes the statistics by reference to that week. | A ruling. |
| F14 | reg 17(1.1) to (3) (src:247-251) and reg 17.1 (src:258-334) | Whether reg 17.1 displaces reg 17(1.1) to (3) for the claimants it names. | (1) it does ("the applicable regional rate of unemployment is"); (2) the greater of the two applies. | (1). | A ruling. |
| F15 | reg 17(1.1)(b) (src:249) | Paragraph (b) names ss 7, 7.1 and 14 and Part VIII, not s 12, for a claimant resident outside Canada. | (1) the text gives no rate for section 12; (2) an omission to be read as section 12 too. | (1): an explicit NOTHING; a test asserts it. | A ruling or an amendment. |
| F16 | reg 10(2) and (4) (src:172, 174) | "Except where subsection (1) and section 9.1 apply": both together, or either. | (1) either (distributively: except where (1) applies and except where 9.1 applies); (2) only where both apply. | (1): (1) concerns people not paid by the hour and 9.1 people who are, so both can never apply together and reading (2) would make "except" empty. | A ruling. |
| F17 | reg 14(5)(b) (src:218) | "whose earnings from that employment consist mainly of commissions": what "mainly" is (more than half?). | A fact the person states; more than half of the earnings. | A BOOLEAN input; no threshold is encoded. | A ruling. |

## Cross-references out of my ranges

Every row is an input of the rule named (the rule takes the outcome as a plain input named for the fact, with a comment `-- out of range: ...` where the provision is another piece's).
Rows marked "no piece" depend on an instrument that is not among this run's inputs, so no piece encodes it.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| reg 1(1) "self-employed person" | Act s 152.01(1) | ei5 | `the individual is a self-employed person within the meaning of subsection 152.01(1) of the Act` |
| reg 1(5) "care", "support" | Act ss 23.1(2), 152.06(1) (a family member), 23.2 and 23.3 (critically ill child, adult) | ei1, ei5 | `the person needing it is a family member referred to in subsection 23.1(2) or 152.06(1) of the Act, a critically ill child or a critically ill adult` |
| reg 1(6) "critically ill child" | Act ss 23.2(3), 152.061(3) (the day the period begins) | ei1, ei5 | `the day on which the period referred to in subsection 23.2(3) or 152.061(3) of the Act begins` |
| reg 1(7) "critically ill adult" | Act ss 23.3(3), 152.062(3) | ei1, ei5 | `the day on which the period referred to in subsection 23.3(3) or 152.062(3) of the Act begins` |
| reg 2(1) | Act s 5(1), s 5(2)(c) | keel (core) | `the employment would, except for paragraph 5(2)(c) of the Act, be insurable employment` |
| reg 3(1) | Act s 5(1), s 5(2)(d) and (e) | keel (core) | `the employment would, except for paragraphs 5(2)(d) and (e) of the Act, be insurable employment` |
| reg 3(2) | the Unemployment Insurance Regulations as they read immediately before June 30, 1996 | no piece (repealed instrument) | `a consent has been given pursuant to the Unemployment Insurance Regulations, as they read immediately before June 30, 1996` |
| reg 6(f) | Canada Pension Plan s 2(1) "office"; Financial Administration Act Schedules I to V | no piece (statutes not among the inputs) | `the person holds an office, as defined in subsection 2(1) of the Canada Pension Plan`; `the office is in or under a department or other portion of the federal public administration set out in Schedule I, II, III, IV or V to the Financial Administration Act` |
| reg 7(c) | the Agreement between Canada and the United States of March 6 and 12, 1942; the United States Railroad Unemployment Insurance Act | no piece | `by reason of the Agreement between Canada and the United States Respecting Unemployment Insurance, signed on March 6 and 12, 1942`; `premiums are payable under the Railroad Unemployment Insurance Act of the United States` |
| reg 7(f) | Act ss 59(b) and 63 | ei2 | `the employment is under an employment support measure referred to in paragraph 59(b) of the Act`; `the employment is under a measure that is the subject of an agreement under section 63 of the Act` |
| reg 9.001, 9.002 | Act ss 50(8), 18(1)(a), 27(1)(a) to (c) (where the criteria are used) | ei2, ei1 | none: the rules state the criteria and the Act's rules call them |
| reg 9.01, 9.02 | Act s 152.02(4), 152.02(6)(b) | ei5 | `the individual gives the Commission a notice to terminate the agreement`; `the individual gives the Commission a withdrawal of the notice` |
| reg 9.2 | Insurable Earnings and Collection of Premiums Regulations s 2(2) | no piece (instrument not among the inputs) | `the person's earnings or a portion of them for a period of insurable employment remain unpaid for the reasons described in subsection 2(2) of the Insurable Earnings and Collection of Premiums Regulations` |
| reg 10(3) | the Minister of National Revenue's examination | judgment, no piece | `the number of hours in insurable employment established by the Minister of National Revenue` |
| reg 10(4) | the provincial minimum wage on January 1 | no piece (provincial law) | `the minimum wage applicable, on January 1 of the year in which the earnings were payable, in the province where the work was performed` |
| reg 10.11 | Insurable Earnings and Collection of Premiums Regulations s 2(3) | no piece | `the amounts that are excluded from the person's earnings from insurable employment by subsection 2(3) of the Insurable Earnings and Collection of Premiums Regulations` |
| reg 11.1 | Act s 152.07(1)(d)(i) (the amount of self-employed earnings) and s 4(2)(b) (the ratio) | ei5; keel | `the amount of self-employed earnings referred to in subparagraph 152.07(1)(d)(i) of the Act`; `the ratio referred to in paragraph 4(2)(b) of the Act` |
| reg 13(1) | Act ss 7.1(6)(a) and (b), 12(2); Employment Insurance (Fishing) Regulations s 8 | ei1; no piece (Fishing Regulations not among the inputs) | `the maximum number of weeks for which benefits may be paid to the claimant under section 8 of the Employment Insurance (Fishing) Regulations or subsection 12(2) of the Act` |
| reg 13(2) | Act ss 152.07(3), 152.14(1) | ei5 | `the maximum number of weeks for which benefits may be paid to the self-employed person under subsection 152.14(1) of the Act` |
| reg 14(1) | Regulations s 36(13) | er3 | worded into the input: `... other than earnings described in subsection 36(13), are payable or allocated` |
| reg 14(2), 14(5) | Act ss 23(1), 23.1(2) | ei1 | the constructors of `er1 Reason an insured person ceases to work` |
| reg 14(3), 14(6) | Act ss 11(4), 11(3) (the leaves) | ei1 | `the period is a period of leave referred to in subsection 11(4) of the Act`; `... 11(3) ...` |
| reg 14.01 | Act ss 152.05(1), 152.06(1), 152.07(1)(c) | ei5 | `the person is a self-employed person referred to in paragraph 152.07(1)(c) of the Act`; the constructors of `er1 Reason a self-employed person ceases to work` |
| reg 14.1 | Regulations s 15(4) as it read before August 12, 2001 (repealed); Act s 19(3) | no piece (repealed text); ei1 | `earnings that a claimant has failed to declare are being allocated to a period referred to in paragraph 15(4)(a), (b) or (c), as that paragraph read immediately before August 12, 2001` |
| reg 16 | Act s 6(1) (disentitled, disqualified), ss 7 and 7.1, Part VIII (the qualifying conditions), Part II, paras 59(b), s 61 | ei1, ei2, ei4 | `the claimant does not meet the qualifying conditions of section 7 or 7.1 ...`; `the claimant is disentitled within the meaning of subsection 6(1) of the Act`; `... disqualified ...`; `the amounts paid to the claimant using financial assistance provided under section 61 of the Act ...` |
| reg 17(1) | Schedule I of the Regulations (which region a section describes); Statistics Canada's published rates; Act s 10(1) (the week) | er6; no piece (Statistics Canada); ei1 | `the number of the section of Schedule I that describes the region`; the monthly rates; `the Sunday of the week referred to in subsection 10(1) of the Act` |
| reg 17.1(1) | Schedule I subsections 3(1), 3(11), 5(2), 5(3) | er6 | the constructors of `er1 Region named in regulation 17.1` (and the string their rule returns) |
| reg 17.1(16), (17) | Act ss 7, 12 and Schedule I and Schedule II (hours and weeks tables) | ei1, ei2, ei6 | `the first day after March 12, 2011 on which the required number of hours of insurable employment in a claimant's qualifying period and the number of weeks for which benefits are payable are exactly the same` |
| reg 18 | Schedule I; the coming into force of subsection 18(1) (Part VII of the Regulations) | er6 | `the region is described in Schedule I`; `the day of the most recent review of the boundaries, or the day subsection (1) came into force if there has been none` |

Count: 29 rows.

## Needs from the core

1. **The ratio of paragraph 4(2)(b).** The core's `eia-core-maximum-earnings` exposes the averages and the amount of s 4(2) but no rule for the ratio itself (the average for the 12 months ending April 30 of the preceding year over the average for the 12 months before that). Reg 11.1 reads "the ratio referred to in paragraph 4(2)(b) of the Act" for each year from 2012, so this piece takes the ratio as a plain NUMBER input `the ratio referred to in paragraph 4(2)(b) of the Act`. A core rule `s 4(2)(b) the ratio` over two lists of twelve monthly figures would let a seat compute it.
2. **Candidates to promote** (local types that other pieces may also need; the lead decides): `er1 Day and hour` (reg 8(2), (4); the stable binary's datetime library is not used); `er1 Reason an insured person ceases to work` and `er1 Reason a self-employed person ceases to work` (reg 14(2), 14.01; they restate the list that ss 12(3) and 152.14(1) give in `Reason for benefits` with different wording: reg 14(2) says "illness, injury or quarantine", not "prescribed"); `er1 Provision for which the regional rate of unemployment is needed` (regs 17(1.1), 17.1; ss 7, 7.1, 12, 14 and Part VIII); `er1 Region named in regulation 17.1`.
3. **Used from the core** (no change wanted): `YMD`, `s 2(1) the Sunday that begins the week containing`, `Period of days` and `the day ... falls within` (reg 17.1 periods), `the band of the regional rate of unemployment` (a test only), `add years`. The Regulations' outputs feed the core's `s 5(1)(d)`, `s 5(2)(c)`, `(d)`, `(e)` and `(h)` through `reg 2 to 6 employment included in insurable employment`, `reg 2(1) ...`, `reg 3(1) ...` and `reg 7 to 9 employment excluded from insurable employment`; the lead may wire them when the pieces are merged (the core's wording of those inputs is in `KEEL-NOTES.md`).

## What the text turns out to say

1. **No date of making, enactment or commencement is in lines 1 to 339.** The title block (lines 5 to 7) and the enacting words (line 9) carry none; the coming into force is Part VII of the Regulations (piece er6). So this piece carries no commencement date and no rule takes a rule date. The dates that do appear are data inside rules and are not commencement dates: June 30, 1996 (reg 3(2), a version of the old regulations), August 12, 2001 (reg 14.1, carried as `reg 14.1 August 12, 2001` with its source line), and the periods of reg 17.1 (September 17, 2000 to April 7, 2012) and its March 12, 2011.
2. **Regulation 17(1.1)(b) leaves out section 12.** For a claimant ordinarily resident outside Canada the regional rate comes from the region last employed in, for ss 7, 7.1 and 14 and Part VIII, but not for s 12, so these Regulations give such a claimant no regional rate for the length of benefits. The same omission runs through reg 17.1(3), (5), (7), (9), (11) and (13). Asserted.
3. **Exactly 40 per cent is not "more than 40%".** A fall in weekly earnings from 1000 to 600 is not an interruption under reg 14(2), and a self-employed person's cut from 40 hours to 24 is not one under reg 14.01; 599 and 23.9 are. Asserted.
4. **Exactly 50 per cent ownership does not take a driver out of reg 6(e);** 51 per cent does. Asserted.
5. **Regulation 9.001(b) lists nine kinds of effort joined by "and".** Read literally every claimant would need all nine; read as a list of kinds, at least one is needed (fork F6). Asserted.
6. **Regulation 10(4) could never apply if read after reg 10(2) and (3):** (4)'s condition (hours "not known or ascertainable") is a case of (2)'s ("cannot establish with certainty") and (3) always yields a number. Read first, (4) has a domain (fork F8). Asserted.
7. **An overtime hour is one hour** (reg 10.2(a)): ten ordinary hours and four overtime hours are 14 hours, not 16; a fraction of an hour in a total counts as a whole hour (10.2(b)). Asserted.
8. **Regulation 8(1)(c) speaks of "any year after 1998".** For 1998 or an earlier year the paragraph's test cannot be met, so the job is not excluded by it. Asserted.
9. **Regulation 11.1's rounding changes a result by a dollar.** Starting from 6000 with ratios of 1.0123 in two years, rounding each year gives 6147, rounding only at the end 6148 (fork F11). Asserted (6147).
10. **A reserve-force period over 24 hours has no deemed hours** (reg 11(2)(b) covers under 6 and 6 to 24 hours): the encoding answers NOTHING. Asserted.
11. **Regulation 13 does not say what happens when more weeks were paid than the maximum.** The encoding answers NOTHING. Asserted.
12. **A consent under the old Unemployment Insurance Regulations stands only if it has not been revoked** (reg 3(2)). Asserted.
13. **Regulations 17.1(6), (7), (12) and (13) stop on the Sunday after the first day after March 12, 2011 on which the hours and weeks agree,** and on that Sunday itself they no longer apply; a Sunday's "Sunday after" is the next week's. Asserted.
14. **Regulation 14.1 is not spent:** a period of allocation that began before August 12, 2001 and was due to end on or after it still ends on that day. Asserted.
15. **Regulation 10.01(2) has no rate threshold,** unlike (1): a person required to be present at the employer's premises and paid for those hours at any rate is counted, "despite subsection (1)". Asserted.
16. **Regulation 7(c)(i) needs "by reason of the Agreement"; (ii), the Railroad Unemployment Insurance Act, does not.** Asserted.
17. **A person is 18, and no longer "under 18", on their eighteenth birthday** (reg 1(6), (7)): the day before, a critically ill child; the birthday itself, a critically ill adult. Asserted.
18. **Regulation 2(2) requires both "appointed and remunerated"** under the province's public service Act, or employment by its agent. Asserted.
19. **A course the Commission referred the claimant to is outside reg 16(1);** one the claimant chose is inside it. Asserted.
20. **Regulation 4(a)'s exception needs both conditions** (regularly employed in voyages between ports outside Canada, and chartered to a person resident outside Canada); either alone leaves the Canadian ship in. Asserted.
21. **Regulation 17.1(2)(b) averages the neighbouring region's rate with the average of the two rates,** not with itself; (6)(a)(ii) and (12)(a)(ii) likewise nest the (4)(b) or (10)(b) average. Asserted.
22. **Nine rows of the coverage table are repealed:** regs 7(a), 8(1)(b), 9.002(1)(d) to (f), 9.002(2) and (3), 9.003, 9.004, 10(7), 12 and 15. Each is a labelled stub in the module (a STRING constant with an `@ref`) that nothing calls, and a test asserts its text. Asserted.

## What the stable binary does not accept

Binary: `l4 1.6.98 (main, 7689b0d, 2026-10-19)`.

**Measured in this run** (each reproduced):
- `DateTime` and `Time` are not in scope with only `IMPORT prelude` and `IMPORT daydate`: "I could not find a definition for the identifier DateTime". Not used; a day and an hour are a small record (`er1 Day and hour`).
- A percent literal as an argument: `f TRUE 0% FALSE` gives "The argument of '%' is expected to be of type NUMBER"; write `f TRUE (0%) FALSE`. (The keel records the same.)
- `THEN BRANCH` with the arms on the following lines at a smaller column than the word BRANCH: "incorrect indentation (got 9, should be greater than 10)"; put `BRANCH` on its own line and indent the arms further.
- A wrong number of arguments is a type error that names the function and both counts ("expects 24 arguments, but you are applying it to 25"); the only way a long positional call goes wrong is by miscounting, so each group of tests gives the order in a comment.
- Accepted and used: a recursive `DECIDE` (the weekly cap of reg 10(5)); `WHERE` with `MEANS` inside a `DECIDE` and in an `@export`ed question; nested `CONSIDER` inside `WHEN`; `LIST OF NUMBER` and `LIST OF MAYBE NUMBER` parameters; an enum or a `MAYBE` record as a question's result; `count`, `sum`, `maximum`, `null`, `at`, `isJust` from the prelude; a record type with spaces in its name built with `OF` when backticked; `` `Period of days` OF `` in a constant; `add years`.

**From the skill's `dialects.md`, not used in these files:** `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`; a section `GIVEN`; `TYPICALLY`; opaque `DECLARE`; sets; `EVERY`; `RULES EFFECTIVE DATE`; `@lang`; `MUST DO`; `WAIT UNTIL`.

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
er1-cases-seat.l4                              0       172       0        0         0
er1-hours-of-insurable-employment.l4           0         0       0        0         0
er1-insurable-employment.l4                    0         0       0        0         0
er1-interpretation.l4                          0         0       0        0         0
er1-interruption-of-earnings.l4                0         0       0        0         0
er1-rates-of-unemployment.l4                   0         0       0        0         0
er1-search-for-employment.l4                   0         0       0        0         0
er1-seat.l4                                    0         0       0        0         0
er1-self-employed-agreement.l4                 0         0       0        0         0
er1-self-employed-earnings.l4                  0         0       0        0         0
er1-tests-hours-of-insurable-employment.l4       0       104       0        0         0
er1-tests-insurable-employment.l4              0       174       0        0         0
er1-tests-interpretation.l4                    0        71       0        0         0
er1-tests-interruption-of-earnings.l4          0        78       0        0         0
er1-tests-rates-of-unemployment.l4             0       268       0        0         0
er1-tests-search-for-employment.l4             0        26       0        0         0
er1-tests-self-employed-agreement.l4           0         8       0        0         0
er1-tests-self-employed-earnings.l4            0        31       0        0         0
er1-tests-undeclared-earnings-and-courses.l4       0        26       0        0         0
er1-undeclared-earnings-and-courses.l4         0         0       0        0         0
TOTAL (24 modules)                             0       958       0        0
```

The 958 assertions are this piece's: 786 in the nine `er1-tests-*` files and 172 in `er1-cases-seat.l4`. The four `eia-core*.l4` modules are the keel's and carry no assertions here (their tests are not in this folder).
`python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/SOR-96-332.txt er1-*.l4` prints `srcrefs check: 407 src: lines, 152 runs, 198 locators, 0 problems` (the Regulations' file; the test, seat and cases files carry no quotation).
The attach-warning loop (`l4 check` on each file, looking for "is at the end of the file", "follows code on its line", "Unknown annotation") printed nothing.
`l4 run` on each of the 20 `er1-*.l4` files shows 0 `DiagnosticSeverity_Error` and 0 `DiagnosticSeverity_Warning` lines.
No test is expected to fail, so `expected_failed` in `check.sh` is unchanged (empty).

## Before this is worth relying on

1. **A person who knows the law has to read each module against the official text.** The text used is a plain-text conversion, not the official text, and nothing was checked against the official consolidation or the French version.
2. **The seventeen forks (F1 to F17) are readings I took so that work could go on; each is reversible in one place.** The ones most likely to change a person's answer are F6 (the nine kinds of effort), F8 (reg 10(4) before (2) and (3)), F9 (the weekly cap), F11 (rounding each year), F13 (the date tested in reg 17.1) and F15 (no rate for s 12 outside Canada).
3. **No independent test pass was made.** The brief makes this piece's author the only encoder, so the expected values were written by the author, by hand, before each run, and mutation-checked once on the 17.1 formulas (changing 0.85 to 0.80 made 17 assertions fail); an independent reader writing expectations from the text alone is still the best check.
4. **Reg 17.1's special rates apply to claims from 2000 to 2012;** a modern claimant needs only reg 17(1) to (4). The date they are tested against is a reading (F13).
5. **Hours: the Act's hours tests (ss 7 and 7.1, piece ei1) are not here.** The questions give hours of insurable employment; whether they are enough is the Act's. The hours questions do not add hours worked, hours of paid leave and hours of standby together; the text states no such sum.
6. **The premiums regulations, the Fishing Regulations, the Canada Pension Plan and the Financial Administration Act are not among the inputs;** every fact they decide is an input.
7. **Nothing here has been deployed or run through Legalese Studio.** The seat's `@export` descriptions have not been shown to a user.
8. **Wiring to the core:** the lead should wire `reg 2 to 6 employment included in insurable employment`, `reg 2(1)`, `reg 3(1)` and `reg 7 to 9 employment excluded from insurable employment` to the core's `s 5` inputs; this piece does not edit the core.
