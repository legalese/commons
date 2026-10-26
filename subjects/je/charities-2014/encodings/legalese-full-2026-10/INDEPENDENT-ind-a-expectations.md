# ind-a expectations: Charities (Jersey) Law 2014, Articles 1 to 12, decided from the Law alone

Written 2026-10-27 by independent test author `ind-a`, BEFORE opening any deposit module, any FRAGMENT-G*.md, domain.l4, PLAN.md, or any phase1 file other than ASSIGN-IND-A.md.
Sources read: BRIEF.md; inputs/charities-jersey-law-2014-2026-10-02.txt (RAW; `src:N` = line N); the PDF text layer (Articles 1 to 12 compared word-by-word after normalising hyphen wraps, endnote markers and page furniture: identical apart from heading case); the endnotes; the amending instruments in inputs/amending/; skills writing-l4-rules/SKILL.md and encoding-a-subject/references/second-pass.md.

Format: one scenario per line. Id = `S<Article>.<paragraph>-NN`. Tags: `AMBIG` (two answers written; goes to the ambiguous file later), `INPUT` (the Law defers to an opinion, a discretion, an Order or Regulations: the expected answer is "an input", and a value supplied by the encoding is a finding), `INERT-EXPECTED` (housekeeping; expected not to be executable), `POWER`/`DUTY`/`PROHIB` (regulative shape expected).

## Conventions (fixed before any scenario uses them)

- C1 Commencement (endnotes src:874-880; R&O.17/2018 Arts 1-2). A provision is in force on day D iff D is on or after its commencement day (the whole commencement day counts). Articles 1 to 7 (Parts 1 to 3): 21 Nov 2014. Articles 8 to 12 (Part 4): 1 May 2018. On a day before commencement the provision gives no answer (not in force), never FALSE-by-default.
- C2 "Minister" (Art. 1, src:26) vintage chain, read from the instruments: R&O.40/2019 Sch 2 para 1(e) substitutes "Minister for External Relations" for "Chief Minister" (made and in force 31 May 2019); R&O.29/2021 Sch 2 para 1(e) substitutes "Minister for External Relations and Financial Services" for "Minister for External Relations" (2 Mar 2021); R&O.28/2023 Sch 2 para 1(4) substitutes "Chief Minister" for "Minister for External Relations and Financial Services" (made 5 Apr 2023, in force 7 days after: 12 Apr 2023); R&O.10/2024 Sch 4 para (1) substitutes "Minister for External Relations" for "Chief Minister" (in force 9.30 a.m. 27 Feb 2024); R&O.102/2026 Art 1 substitutes "Chief Minister" for "Minister for External Relations" (made 25 Sep 2026, in force 7 days after: 2 Oct 2026). Jersey wall-clock in February is GMT = UTC. An instrument "comes into force" at the start of its day unless it names a time. A function of a DATE alone on 27 Feb 2024 cannot decide (REFUSE); a function of an instant answers Chief Minister before 09:30 and MER at or after 09:30.
- C3 Before 31 May 2019 "Minister" = Chief Minister: derived because R&O.40/2019 substitutes FOR the words "Chief Minister" and the Table of Legislation History lists no earlier amendment. The original 2014 text itself is not among the inputs, so a REFUSE for 21 Nov 2014 to 30 May 2019 is also defensible (AMBIG-SRC).
- C4 "Comptroller" (Art. 1, src:12): L.13/2019 Sch 3 para 1 (given effect by L.13/2019 Art at its line 852; whole Law in force 1 Jan 2020 by R&O.136/2019 except Arts 17-19) substitutes "Revenue Administration (Jersey) Law 2019" for "Income Tax (Jersey) Law 1961". So before 1 Jan 2020: meaning given by the Income Tax (Jersey) Law 1961; from 1 Jan 2020: by the Revenue Administration (Jersey) Law 2019.
- C5 Art 2(1)(ba) exists from 16 Oct 2025 (R&O.56/2025: made 9 Oct 2025, in force 7 days after = 16 Oct 2025, endnote agrees). On 15 Oct 2025 the list is (a), (b), (c) to (j).
- C6 Backward window "in the 12 months preceding the application" (Art 11(2)(e)(ii), src:310). My reading P1: the window is the days from the same calendar date 12 months before the application day (inclusive) to the day before the application day (inclusive); the application day itself is excluded. Alternative P2: the window is the 12 months ending with the application day (from the day after the same calendar date 12 months earlier, to the application day inclusive). Month-end: 12 months before 29 Feb is 28 Feb (clip, my reading) or 1 Mar (roll, alternative).
- C7 Forward period "retain for 10 years" (Art 8(6), src:249). START is unstated: my reading R-start-a = from the day the Commissioner receives (or, for notices, serves) each document; alternative R-start-b = from the charity's deregistration (the reading Art 17(1)(a) uses for registered information); R-start-c = from registration. COUNTING: my reading R-count-1 = event day excluded, period ends at the end of the 10th anniversary day, disposal permitted from the day after the anniversary; alternative R-count-2 = event day included, period ends at the end of the day before the anniversary, disposal permitted on the anniversary. Anniversary of 29 Feb in a non-leap year: 28 Feb (clip, mine) or 1 Mar (roll).
- C8 "Most recent year" (Art 8(3)(j), src:234) and the decision period (Art 11(8)(a)(i)) are not defined by the Law: INPUT (Order under Art 13(8) / Art 11(8)).
- C9 Every "in the opinion of", "satisfied", "considers", "substantial", "to a reasonable degree", "unduly restrictive", "reasonably practicable", "reasonable time", "as soon as practicable", "appears to", "analogous" (6(1)(p)) is an INPUT I supply in the scenario.

## Article 1 (interpretation) — src:6-46

- S1-01 Entity entered in the general section today -> "registered charity" TRUE. src:34
- S1-02 Entity entered in the restricted section -> "registered charity" TRUE. src:34
- S1-03 Entity entered only in the historic section (deregistered) -> "registered charity" FALSE. src:34
- S1-04 Entity never entered -> "registered charity" FALSE. src:34
- S1-05 Person registered under the Banking Business (Jersey) Law 1991 -> business is "regulated financial services business" TRUE (limb a). src:36-37
- S1-06 Person holding a permit under the Collective Investment Funds (Jersey) Law 1988 -> TRUE (limb b); holding a certificate under it -> TRUE (limb b). src:38
- S1-07 Person registered under the Financial Services (Jersey) Law 1998 -> TRUE (limb c). src:39
- S1-08 Person authorized by a permit under the Insurance Business (Jersey) Law 1996 -> TRUE (limb d). src:40
- S1-09 Person with none of the four -> FALSE. src:36-40
- S1-10 Company registered under the Companies (Jersey) Law 1991 -> "company" TRUE; an existing company within the meaning of that Law -> TRUE; a company incorporated in England under a UK Act not extended to Jersey -> "company" FALSE. src:11
- S1-11 Foundation incorporated under the Foundations (Jersey) Law 2009 -> "foundation" TRUE; a Liechtenstein foundation -> FALSE. src:19
- S1-12 Whether a trust is one "over which the court has jurisdiction under Article 5 of the Trusts (Jersey) Law 1984" -> INPUT (out-of-scope enactment). src:46
- S1-13 "court" = the Royal Court; "tribunal" = the Charity Tribunal (Art 32); "JFSC" = the Jersey Financial Services Commission. INERT-EXPECTED. src:15,23,45
- S1-14 "publish": whether a manner of publication is likely to bring information to the public's attention is the publisher's opinion -> INPUT. src:30
- S1-15 "Minister" on 2014-11-20 -> no answer (Law not in force). C1
- S1-16 "Minister" on 2014-11-21 -> Chief Minister (AMBIG-SRC: REFUSE also defensible, C3). src:26
- S1-17 "Minister" on 2018-05-01 -> Chief Minister (AMBIG-SRC, C3).
- S1-18 "Minister" on 2019-01-01 (first point-in-time version) -> Chief Minister.
- S1-19 "Minister" on 2019-05-30 -> Chief Minister.
- S1-20 "Minister" on 2019-05-31 -> Minister for External Relations. R&O.40/2019
- S1-21 "Minister" on 2019-12-16 and on 2020-01-01 -> Minister for External Relations.
- S1-22 "Minister" on 2021-03-01 -> Minister for External Relations.
- S1-23 "Minister" on 2021-03-02 -> Minister for External Relations and Financial Services. R&O.29/2021
- S1-24 "Minister" on 2023-04-11 -> Minister for External Relations and Financial Services.
- S1-25 "Minister" on 2023-04-12 -> Chief Minister. R&O.28/2023
- S1-26 "Minister" on 2024-02-26 -> Chief Minister.
- S1-27 "Minister" on 2024-02-27 as a date only -> REFUSE (cannot decide; changes at 09:30). R&O.10/2024
- S1-28 "Minister" at 2024-02-27T09:29 -> Chief Minister; at 2024-02-27T09:30 -> Minister for External Relations; at 2024-02-27T09:31 -> Minister for External Relations.
- S1-29 "Minister" on 2024-02-28 -> Minister for External Relations.
- S1-30 "Minister" on 2025-10-09 and 2025-10-16 -> Minister for External Relations.
- S1-31 "Minister" on 2026-10-01 -> Minister for External Relations.
- S1-32 "Minister" on 2026-10-02 and 2026-10-27 -> Chief Minister. R&O.102/2026
- S1-33 "Comptroller" on 2019-12-31 -> meaning given by the Income Tax (Jersey) Law 1961; on 2020-01-01 -> by the Revenue Administration (Jersey) Law 2019; on 2026-10-27 -> Revenue Administration (Jersey) Law 2019. C4
- S1-34 "Comptroller" on 2014-11-21 -> Income Tax (Jersey) Law 1961 (AMBIG-SRC as C3: derived from the words L.13/2019 replaces).
- S1-35 "donation" and "solicit" -> construed by the Order under Art 9(3)(b) -> INPUT. src:17,44

## Article 2 — src:47-117

### 2(1) entity
- S2.1-01 Trustees (taken together) of a trust the court has jurisdiction over -> entity, sub-paragraph (a). src:49
- S2.1-02 Fidéicommissaires of a court-approved fidéicommis -> entity, (b). src:50
- S2.1-03 On 2025-10-16: body corporate, an NPO under the NPO Law 2008, established under Jersey law, within none of (c) to (h) -> entity, (ba). src:51-54; C5
- S2.1-04 Same body on 2025-10-15 -> NOT an entity (no limb covers it; (j) is foreign only, (i) is unincorporated only). C5
- S2.1-05 Body corporate, established under Jersey law, within none of (c) to (h), but NOT an NPO, on 2026-10-27 -> NOT an entity. src:52
- S2.1-06 NPO body corporate established under Guernsey law, within none of (c) to (h) -> not (ba) (fails (ii)); whether (j) -> INPUT "substantially similar" plus AMBIG-1 (does (j)'s "(a) to (h)" include (ba)). src:53,65
- S2.1-07 NPO body corporate that is a Jersey company -> (f), NOT (ba) (fails (iii)). src:54,61
- S2.1-08 Incorporated 1862 association -> (c). src:55
- S2.1-09 Foundation -> (d). src:56
- S2.1-10 Body corporate established by an enactment / by Act of the States / by Royal Charter in relation to Jersey -> (e) in each case. src:57-60
- S2.1-11 Jersey company -> (f). src:61
- S2.1-12 Body incorporated under (not by) an enactment other than the Companies Law, e.g. a limited liability company under a Jersey LLC Law -> (g). src:62
- S2.1-13 Body incorporated under, not by, a UK Act extended to Jersey -> (h). src:63
- S2.1-14 Unincorporated association of persons, not a partnership, not trustees -> (i). src:64
- S2.1-15 An unincorporated partnership -> NOT (i) -> not an entity (no other limb). src:64
- S2.1-16 English charitable company incorporated under a UK Act not extended to Jersey, substantially similar to a Jersey company (INPUT: similar = yes) -> (j). src:65
- S2.1-17 French unincorporated association -> (i) (limb (i) has no jurisdiction condition), not (j) ((j) refers only to (a) to (h)). src:64-65
- S2.1-18 Jersey company acting as sole trustee of a charitable trust -> falls within BOTH (f) and (a); the register note must say "(f), also within (a)". src:49,61,224
- S2.1-19 A natural person acting alone, not a trustee -> NOT an entity.
- S2.2-01 POWER: the Minister may by Order add sub-paragraphs to 2(1). R&O.56/2025 (made 9 Oct 2025 by the Minister for External Relations, who was "the Minister" that day, C2) -> made by the right office-holder. src:66
- S2.2-02 An Order under 2(2) on 2025-10-09 made by the Chief Minister -> not made by "the Minister" -> not an exercise of 2(2). C2
- S2.2-03 An Order under 2(2) that deletes a sub-paragraph -> outside the power ("add" only). src:66

### 2(3) Jersey entity
- S2.3-01..08 Entity within each of (a), (b), (c), (d), (e), (f), (g), (h) -> Jersey entity TRUE (8 scenarios). src:68
- S2.3-09 Entity within (ba) only -> AMBIG-1: TRUE (my reading: an inserted (ba) lies within the range "(a) to (h)") / FALSE (the range reads only the letters it named in 2014). src:68
- S2.3-10 Entity within (j) only -> FALSE. src:68
- S2.3-11 (i) association, relationship governed by Jersey law, one governor a natural person resident in Jersey -> TRUE. src:69-71
- S2.3-12 (i), Jersey law, no Jersey-resident natural governor, one governor a Jersey company -> TRUE (company is a Jersey entity by 2(3)(a)). src:71
- S2.3-13 (i), Jersey law, only governor is another (i) association that is a Jersey entity only by 2(3)(b) -> FALSE (must be "by virtue of sub-paragraph (a)"). src:71
- S2.3-14 (i), English law governs, governor resident in Jersey -> FALSE. src:70
- S2.3-15 (i), Jersey law, all governors natural persons resident in Guernsey -> FALSE. src:71
- S2.3-16 (i), Jersey law, only governor an English company ((j)) -> FALSE. src:71
- S2.3-17 (i), Jersey law, only governor a (ba) body -> follows AMBIG-1 (TRUE / FALSE).
- S2.3-18 (i), Jersey law, a governor that is the trustees of a Jersey trust ((a)) -> TRUE.

### 2(4) constitution
- S2.4-01 trust -> the terms of the trust. src:73
- S2.4-02 court-approved fidéicommis -> the minute of the contract annexed to the application, other annexed documents, and Art 10 authorisations. src:74
- S2.4-03 incorporated 1862 association -> the Act of the court incorporating it, and the object and rules approved or modified. src:75
- S2.4-04 foundation -> charter and regulations. src:76
- S2.4-05 company -> memorandum and articles of association. src:77
- S2.4-06 (e) body -> the enactment, Act of the States or Royal Charter that established it. src:78
- S2.4-07 (ba), (g), (h), (i), (j) entities -> "any instrument or instruments that establish the entity or give it any powers" (limb g). src:79
- S2.4-08 Jersey company that is sole trustee (dual (a)+(f)) -> AMBIG-3: terms of the trust (limb a, first in order) / memorandum and articles (limb e) / both.

### 2(5) constitutional Law
- S2.5-01 trust -> Trusts (Jersey) Law 1984. src:81
- S2.5-02 court-approved fidéicommis -> Loi of 1862; incorporated 1862 association -> Loi of 1862. src:82
- S2.5-03 foundation -> Foundations (Jersey) Law 2009. src:83
- S2.5-04 company -> Companies (Jersey) Law 1991. src:84
- S2.5-05 body incorporated BY a Law (2(1)(e)(i) where the enactment is a Law) -> that Law. src:85
- S2.5-06 (e)(ii) body established by Act of the States; (e)(iii) by Royal Charter -> no constitutional Law (an Act of the States and a Charter are not a "Law"). Expected NOTHING or REFUSE; a definite Law is a finding. src:85
- S2.5-07 (g) body incorporated UNDER a Jersey LLC Law -> AMBIG-2: no constitutional Law (literal: 2(5)(e) says "by (but not under)") / that LLC Law (purposive: 2(5)(e) was meant to mirror 2(1)(g)). src:62,85
- S2.5-08 (h), (i), (j), (ba) -> no constitutional Law (NOTHING/REFUSE). src:80-85

### 2(6) purpose
- S2.6-01 trust -> limb (a): benefit of beneficiaries or other Art 2(b) Trusts Law purpose specified in the constitution. src:87
- S2.6-02 fidéicommis and 1862 association -> limb (b): the objects created/incorporated for or authorised under Loi Art 10. src:88
- S2.6-03 foundation -> limb (c): objects in charter or regulations. src:89
- S2.6-04 company, (e), (g), (h), (i), (j), (ba) -> limb (d): purposes to which property may lawfully be applied under the constitution, including on winding up. src:90
- S2.6-05 (d): a purpose to which property could be applied only by a court order -> NOT a purpose of the entity. src:90
- S2.6-06 (d): company whose articles distribute surplus to members on winding up -> that distribution is a purpose (non-charitable) -> charity test fails 5(1)(a). src:90,146

### 2(7)-(9) governor
- S2.7-01 trustee of a trust -> governor (a); fidéicommissaire -> governor (a). src:92
- S2.7-02 member of a foundation's council -> governor (b); a foundation's guardian who is not a council member -> NOT a governor under (b). src:93
- S2.7-03 company director -> governor (c); company secretary who is not a director -> NOT; shareholder -> NOT. src:94
- S2.7-04 relevant unincorporated entity: management committee member -> governor (d); ordinary member not on the committee -> NOT. src:95
- S2.7-05 any other case (e.g. a non-model (i) association, an (e)/(g)/(h)/(j)/(ba) body): person who under the constitution has the general control and management of the administration -> governor (e). src:96
- S2.7-06 2(9)(a): employee manager exercising control on behalf of the committee that has it in its own right -> NOT a governor. src:103
- S2.7-07 2(9)(b): person who has general control alone -> governor; as one of five -> governor. src:104
- S2.7-08 Jersey company as sole trustee (dual) -> AMBIG-3: governor is the company (7)(a) / its directors (7)(c).
- S2.8-01 (i) association whose constitution conforms to a model published by the Commissioner for the purpose that provides for a management committee -> relevant unincorporated entity TRUE. src:97-101
- S2.8-02 (i) association, bespoke constitution with a management committee, not conforming to the model -> FALSE (its governors fall under 7(e)). src:99
- S2.8-03 (i) association conforming to a Commissioner model that does NOT provide for a management committee -> FALSE. src:101
- S2.8-04 company using the model -> FALSE (not (i)). src:98
- S2.8-05 model published by a third party, not by the Commissioner -> FALSE. src:100

### 2(10) misconduct
- S2.10-01 (a)(i) registered charity contravenes a provision of this Law (e.g. Art 12(7) unregistered name) -> misconduct. src:106-107
- S2.10-02 (a)(i) governor contravenes an Order made under this Law -> misconduct. src:107
- S2.10-03 (a)(ii) charity contravenes its own constitution -> misconduct; governor contravenes the charity's constitutional Law -> misconduct. src:108
- S2.10-04 (a)(iii) contravention of a required steps notice -> misconduct. src:109
- S2.10-05 (a)(iv) contravention of an order of the court under this Law or under the constitutional Law -> misconduct. src:110
- S2.10-06 (a) negative: a non-governor employee contravenes the constitution -> NOT misconduct under (a). src:106
- S2.10-07 (a) negative: an applicant not yet registered contravenes Art 11 -> NOT (a) misconduct (not a registered charity). src:106
- S2.10-08 (b)(i) any person commits an offence under the constitutional Law of a registered charity, in relation to it -> misconduct. src:111-112
- S2.10-09 (b)(ii) offence under the Financial Services (Jersey) Law 1998 in relation to a registered charity -> misconduct (also Banking, CIF, Insurance, AIF Regs). src:113
- S2.10-10 (b)(iii) offence under the Income Tax Law / GST Law / Taxation (Land Transactions) Law -> misconduct. src:114
- S2.10-11 (b)(iv) money laundering or terrorist financing offence under another enactment -> misconduct. src:115
- S2.10-12 (b)(v) customary-law fraud (dishonesty) -> misconduct. src:116
- S2.10-13 (b)(vi) a UK fraud offence (similar to (v)) -> misconduct. src:117
- S2.10-14 (b) negative: an assault (no dishonesty, none of the listed laws) by a governor in relation to the charity -> NOT misconduct under (b). src:111-117
- S2.10-15 (b) in relation to an excepted foreign charity (Art 22) -> misconduct; in relation to a foreign entity equivalent to a registered charity -> misconduct. src:111
- S2.10-16 (b) in relation to a non-charity, or to a deregistered entity -> NOT misconduct. src:111

## Article 3 — src:120-122
- S3-01 Establishment of a corporation sole; Schedule 1 applies. INERT-EXPECTED. In force 21 Nov 2014 (C1).

## Article 4 — src:123-141
- S4.1-01 The seven general functions (a)-(g) (administer the charity test and operate the register; supervise governors; seek to enforce Part 6; publish guidance; assist AG, court, Bailiff, Comptroller, JFSC; encourage compliance; other conferred functions). INERT-EXPECTED or a list; each is a function. src:124-131
- S4.2-01 POWER: Commissioner does an act calculated to facilitate a function (e.g. contracts an IT supplier for the register) -> permitted. src:132
- S4.2-02 Commissioner acts as governor of a registered charity -> NOT permitted (excluded from 4(2)). src:132
- S4.2-03 Commissioner acts as governor of an unregistered entity with charitable purposes -> NOT permitted. src:132
- S4.2-04 Commissioner does an act not calculated to facilitate / conducive / incidental to any function -> not authorised by 4(2). src:132
- S4.3-01 POWER (a): provide information to the public about registration, model constitutions -> may. src:134
- S4.3-02 POWER (b): advise the Minister on charities and regulation proposals -> may. src:135
- S4.3-03 POWER (c): assist a foreign body equivalent to the Commissioner, AG, court, Comptroller or JFSC -> may. src:136
- S4.3-04 Assisting a foreign body equivalent to the BAILIFF -> NOT within 4(3)(c) (the Bailiff appears in 4(1)(e) but not in 4(3)(c)); whether 4(2) covers it -> INPUT. src:129,136
- S4.4-01 DUTY to "seek to act" in a way that protects trust, encourages giving and participation, is proportionate: qualified by "so far appears to him or her to be reasonably practicable" -> INPUT. src:137-141

## Article 5 — src:144-165
- S5.1-01 Entity all of whose purposes are charitable, which provides public benefit to a reasonable degree (INPUT yes), no 5(2) clause -> meets the charity test. src:145-149
- S5.1-02 One charitable purpose plus a purely ancillary non-charitable purpose (fundraising trading) -> meets. src:148
- S5.1-03 A non-charitable, non-ancillary purpose among others -> fails. src:146
- S5.1-04 Only ancillary purposes, no charitable purpose -> fails (ancillary "to any of its charitable purposes"). src:148
- S5.1-05 Entity with no purposes at all -> AMBIG-5: fails (nothing to give effect to; no public benefit "in giving effect to those purposes") / 5(1)(a) vacuously true. My reading: fails.
- S5.1-06 Registered charity (not an applicant), charitable purposes, intends to but does not yet provide public benefit -> fails 5(1)(b). src:149
- S5.1-07 Applicant, charitable purposes, intends to provide public benefit, none yet -> meets 5(1)(b). src:149
- S5.1-08 Public benefit provided only abroad (Kenya), to a reasonable degree -> meets ("in Jersey or elsewhere"). src:149
- S5.1-09 Public benefit not to a reasonable degree (INPUT no) -> fails. src:149
- S5.1-10 Charitable purposes plus a purpose of advancing a political party presented as ancillary -> fails (6(5)). src:201
- S5.2-01 Constitution expressly permits the Minister for Health, acting as Minister, to direct activities -> fails 5(2)(a). AMBIG-4 ("a Minister" = any Minister; if Art 1 "Minister" = Chief Minister were read in, (a) would not catch the Minister for Health). src:150-151
- S5.2-02 Constitution expressly permits a governor to be a States Assembly member acting in that capacity (ex officio seat) -> fails 5(2)(b). src:152
- S5.2-03 Constitution expressly permits a UK Secretary of State acting as such to control activities -> fails 5(2)(c). src:153
- S5.2-04 Constitution lets any adult be a governor; one governor is a States member serving in a private capacity -> passes 5(2) (no express permission; not "acting in that capacity"). src:150,154
- S5.2-05 Constitution silent; a Minister in fact directs activities -> passes 5(2) (it bites only on express constitutional permission). src:150
- S5.2-06 Entity failing 5(1) and having a 5(2) clause -> fails. src:150
- S5.3-01 5(2) clause, and an Order under 5(3) disapplies 5(2) for this entity -> meets; register must carry the clause text (8(3)(i)). src:155,233
- S5.3-02 Order disapplies 5(2) for a description the entity is not within -> fails. src:155
- S5.4-01 DUTY: Commissioner must publish and maintain charity-test guidance. src:156
- S5.5-01 DUTY: any person determining the charity test must have regard to the guidance; the Commissioner, tribunal, registered charity and governor must have regard when performing other relevant functions. src:157
- S5.6-01 Guidance issued after consulting representatives (i), the Minister (ii) and others (iii), and a report published (b) -> procedure complied. src:158-163
- S5.6-02 Guidance issued without consulting the Minister -> breach of 5(6)(a)(ii). src:161
- S5.6-03 Guidance issued without consulting representatives of charities -> breach of 5(6)(a)(i). src:160
- S5.6-04 Guidance issued without publishing the report -> breach of 5(6)(b). src:163
- S5.6-05 Amending guidance -> the same procedure applies ("issuing or amending"). src:158
- S5.6-06 The Minister to be consulted on 2025-06-01 = Minister for External Relations; on 2026-10-27 = Chief Minister (C2).
- S5.7-01 DUTY: within a reasonable time (INPUT) provide the Minister with the guidance and report; not provided -> breach. src:164
- S5.8-01 DUTY: the Minister must lay them before the States as soon as practicable (INPUT). src:165

## Article 6 — src:166-201
- S6.1-01 food bank for people in poverty -> (a). src:168
- S6.1-02 running a school -> (b). src:169
- S6.1-03 maintaining a place of worship -> (c). src:170
- S6.1-04 hospice -> (d); vaccination campaign (prevention of disease, 6(2)(a)) -> (d). src:171,185
- S6.1-05 lifeboat service -> (e). src:172
- S6.1-06 community development -> (f); urban regeneration (6(2)(b)(i)) -> (f); promoting volunteering, or the efficiency of registered charities (6(2)(b)(ii)) -> (f). src:173,186-188
- S6.1-07 museum (heritage) -> (g); scientific research -> (g). src:174
- S6.1-08 public participation in football -> (h). src:175,189
- S6.1-09 recreation ground open to the public at large, object of improving conditions of life -> (i). src:176,190-192
- S6.1-10 human rights -> (j); conflict resolution -> (j). src:177
- S6.1-11 racial harmony -> (k). src:178
- S6.1-12 equality and diversity -> (l). src:179
- S6.1-13 environmental protection -> (m). src:180
- S6.1-14 relief of elderly people in need by providing a care home (6(2)(e)) -> (n). src:181,193
- S6.1-15 animal shelter -> (o). src:182
- S6.1-16 a purpose said to be analogous to (a)-(o) -> (p) iff the decider so regards it: INPUT. src:183
- S6.2f-01 advancement of a philosophical belief not involving a god (humanism) -> charitable under (p) by deeming, no discretion needed. src:194
- S6.2c-01 public participation in chess / e-sports without physical exertion -> NOT (h) (may be (b) or (p): INPUT). src:189
- S6.2d-01 recreational facility only for fee-paying members of a private club, not disadvantaged -> NOT (i). src:190-192
- S6.2d-02 recreational facility available to all women of the public at large -> (i) (with the object of improving conditions of life). src:192
- S6.2d-03 recreational facility primarily for disabled persons -> (i). src:191
- S6.2d-04 facility open to the public at large but without the object of improving conditions of life -> NOT (i). src:176
- S6.1-17 benefit of the founder's private business -> not a charitable purpose (none of (a)-(o); (p) INPUT no).
- S6.5-01 advancing a political party -> neither charitable nor ancillary. src:201
- S6.5-02 promoting a candidate for election in the UK ("whether in Jersey or elsewhere") -> neither. src:201
- S6.5-03 a purpose within 6(1) on its face (e.g. "education" of voters to support one party) -> 6(5) overrides ("irrespective of whether it would otherwise fall within paragraph (1)"). src:201
- S6.5-04 campaigning on a policy issue, no party or candidate -> 6(5) does not apply (other heads decide; INPUT).
- S6.3-01 POWER: the States, on the recommendation of the Commissioner, by Regulations add a head -> authorised. src:195-196
- S6.3-02 The States add a head WITHOUT the Commissioner's recommendation -> not authorised by 6(3). src:195
- S6.3-03 The Minister (not the States) adds a head by Order -> not authorised by 6(3). src:195
- S6.3-04 Regulations add to 6(2) an explanatory provision for a head added under 6(3)(a) -> authorised; for an original head -> not authorised (6(3)(b) "so added"; 6(4)(a)). src:197,199
- S6.4-01 Regulations restricting 6(1)(b) education -> outside the power. src:199
- S6.4-02 Regulations making advancement of a political party charitable (alters 6(5)) -> outside the power. src:200

## Article 7 — src:202-213
- S7.1-01 7(2)-(3) apply when the Commissioner, the tribunal or the court determines public benefit -> TRUE for each. A governor or a member of the public determining it -> 7(2)-(3) do not apply to them (7(1) lists three deciders). src:203
- S7.2-01 Regard to the private benefit / public disbenefit comparison -> DUTY to have regard; the weighing is INPUT. src:204-208
- S7.2-02 Benefit to a section of the public only -> DUTY to have regard to whether conditions (charges, fees) are unduly restrictive; the answer is INPUT. src:209
- S7.3-01 Charitable purpose (religion) with no evidence of public benefit -> public benefit may NOT be presumed; not established. src:211
- S7.3-02 Entity benefiting only three named grandchildren of the founder -> must NOT be treated as providing public benefit -> fails 5(1)(b). src:212
- S7.3-03 Entity benefiting a single named individual -> must NOT be treated as providing public benefit. src:212
- S7.3-04 Entity benefiting everyone in Jersey with a rare disease (a class, not identified persons) -> 7(3)(b) not triggered; question remains INPUT. src:212
- S7.4-01 DUTY: the Art 5(4) guidance must include guidance on public benefit. src:213

## Article 8 — src:216-253 (in force 1 May 2018)
- S8.1-01 DUTY: Commissioner must establish and maintain a register. src:217
- S8.2-01 The register has exactly three sections: general, restricted, historic. src:218-221
- S8.3-01 Registered Jersey company in the general section, not a trustee, not an organized religious charity, no 5(3) Order, no RSN, never renamed, no 13(9)(c) Order -> required entries: registered name, registration number, (a)(i) "(f), not also (a)", (b) governors' names, (c) principal address, (d) other non-dwelling Jersey premises (if any), (e) registered charitable purposes, (f) registered public benefit statement, (g) date registered, (j) annual return sent / not sent; NOT required: (a)(ii), (h), (i), (k), (l), (m); (n) INPUT. src:222-238
- S8.3a-01 (e) body -> (a)(ii) details of the enactment / Act of the States / Royal Charter required. src:225
- S8.3a-02 (g) body -> (a)(ii) details required; (h) body -> required (UK Act or Order in Council); (j) body -> required (foreign law). src:225
- S8.3a-03 (a), (b), (ba), (c), (d), (f), (i) entities -> (a)(ii) NOT required. src:225
- S8.3a-04 The "also within (a)?" note is required for (f), (g), (h), (i), (j); not for (a), (b), (ba), (c), (d), (e). src:224
- S8.3a-05 Jersey company that is a trustee -> note "(f), also within (a)". src:224
- S8.3d-01 Charity also operates a shop in St Helier -> shop address entered (d); a governor's private dwelling house used for activities -> NOT entered. src:228
- S8.3h-01 Organized religious charity -> note + the provision of the Art 28 Order. src:232
- S8.3i-01 Meets the test by virtue of a 5(3) Order -> text of the constitution provision within 5(2). src:233
- S8.3j-01 Annual return for the most recent year sent -> entry "sent"; not sent -> entry "not sent" (entry required either way). Which year is "most recent" -> INPUT. src:234
- S8.3k-01 RSN served on the charity -> note (or copy) + date served; RSN served on a governor -> note + date; no RSN -> no (k) entry. src:235
- S8.3l-01 Registered name changed from X to Y -> previous name X entered; an alternative name added without change -> no (l) entry. src:236
- S8.3m-01 Order under 13(9)(c) applies -> its details/statement entered; otherwise not. src:237
- S8.3n-01 Other prescribed information -> INPUT (Order). src:238
- S8.4-01 Company -> principal address = registered office (a). src:240
- S8.4-02 Foundation -> its registered office / business address (a). src:240
- S8.4-03 Other entity required by its constitutional Law to have a Jersey registered office -> that address (a); whether so required -> INPUT. src:240
- S8.4-04 Trust (not so required) whose Jersey activities are managed from an office in St Helier -> that office (b). src:241
- S8.4-05 Association whose only premises is a governor's private dwelling house -> (b) excluded -> (c): a governor's Jersey address. src:241-242
- S8.4-06 Association with no Jersey premises, one governor with a Jersey address -> (c) that address. src:242
- S8.4-07 Foreign entity, no Jersey premises, no governor with a Jersey address -> NO principal address in Jersey -> Art 11(4)(d) fails -> must refuse. src:239-242,325
- S8.5-01 General-section charity deregistered -> historic entry: former number; name immediately before deregistration and earlier names; reason summary; registration and deregistration dates; prescribed matters (INPUT). src:243-248
- S8.5-02 Restricted-section charity (restricted throughout) deregistered -> historic entry carries NO name; the rest as S8.5-01. src:245
- S8.5-03 Deregistered for contravening an RSN -> reason summary includes the reason the RSN was served. src:246
- S8.5-04 Charity in the general section 2018-2020 under name X, moved to restricted 2020, deregistered 2023 -> AMBIG-6: no name (8(5)(b) read as "registered in the general section [at deregistration]") / name X entered ("was [ever] registered in the general section"). src:245
- S8.6-01 DUTY: retain for 10 years copies of the constitution and amendments, annual returns, notices served on the charity, prescribed documents. src:249-253
- S8.6-02 Constitution copy received 2020-03-15 -> must still be retained on 2030-03-14 (all readings); disposal permitted from 2030-03-16 (R-start-a, R-count-1) or 2030-03-15 (R-count-2). AMBIG-7 (start and counting). C7
- S8.6-03 Copy received 2020-02-29 -> retained to at least 2030-02-28; end day 2030-02-28 (clip) or 2030-03-01 (roll). AMBIG-7.
- S8.6-04 Correspondence not within (a)-(d) and not prescribed -> no 8(6) duty. src:250-253

## Article 9 — src:254-286 (in force 1 May 2018)
- S9.1-01 Restricted-section charity, public elements: registration number YES; registered name NO. src:256
- S9.1-02 Restricted: 8(3)(a) status YES; (e) purposes YES; (f) PBS YES; (j) annual return YES; (k) RSN YES. src:257
- S9.1-03 Restricted: 8(3)(b) governors NO; (c) principal address NO; (d) premises NO; (g) date of registration NO; (h) ORC NO; (i) 5(3) text NO; (l) previous names NO; (m) 13(9)(c) details NO; (n) NO unless prescribed under 9(1)(d) (INPUT). src:255-259
- S9.1-04 Restricted: the charity's summary of reasons for restricted registration (9(1)(c)) YES; elements prescribed under 9(1)(d) YES. src:258-259
- S9.2-01 Applicant meeting the prescribed funding condition (INPUT) -> may request restricted entry. src:260-261
- S9.2-02 General-section charity meeting another prescribed condition (INPUT) -> may request. src:260,262
- S9.2-03 Applicant meeting no prescribed condition -> may NOT request. src:260-262
- S9.2-04 Charity already in the restricted section -> not a requester under 9(2). src:260
- S9.2-05 Deregistered entity; or an entity neither applying nor registered -> not a requester. src:260
- S9.3-01 The Order must prescribe acceptance/refusal grounds and define soliciting, donation and (absent a prescribed description of persons) the general public; an Order prescribing a description of persons need not define "general public". Content INPUT. src:263-269
- S9.4-01 Request in the published form, evidence satisfying the Commissioner (INPUT), 9(5) statement attached -> 9(4) and 9(5) complied. src:270-279
- S9.4-02 Request not in the published form -> fails 9(4)(a). src:271
- S9.4-03 Evidence not to the Commissioner's satisfaction -> fails 9(4)(b). src:272
- S9.5-01 Applicant's statement "treat as withdrawn" -> valid (a)(i); "treat as an application for the general section" -> valid (a)(ii). src:274-276
- S9.5-02 General-section charity's statement "remain registered" -> valid (b)(i); "treat as applying to be deregistered" -> valid (b)(ii). src:277-279
- S9.5-03 Applicant states "remain so registered" (a (b) option) -> NOT a valid statement for an applicant; general-section charity states "treat as withdrawn" -> NOT valid. src:273-279
- S9.5-04 No statement -> fails 9(5). src:273
- S9.6-01 All of 9(6)(a), (b), (c) satisfied -> the Commissioner MAY enter (AMBIG-8: permissive "must not ... unless" / an implied duty to enter). src:280-283
- S9.6-02 9(6)(a) not satisfied -> must NOT enter. src:281
- S9.6-03 No prescribed condition met -> must NOT enter. src:282
- S9.6-04 A mandatory refusal ground applies -> must NOT enter. src:283
- S9.6-05 A discretionary ground applies and the Commissioner considers the request should be refused -> must NOT enter. src:283
- S9.6-06 A discretionary ground applies but the Commissioner considers it should not be refused -> (c) satisfied -> may enter. src:283
- S9.7-01 Refusal -> DUTY: written notice to the applicant or charity. src:285
- S9.7-02 Refusal + applicant intention "withdrawn" -> MAY treat the application as withdrawn; intention "general" -> MAY proceed with it as a general-section application. src:286
- S9.7-03 Refusal + general-section charity intention "deregister" -> MAY treat as a deregistration application; "remain" -> charity stays in the general section. src:286

## Article 10 — src:287-297 (in force 1 May 2018)
- S10.1-01 DUTY: public parts on a website, free of charge; charging for website inspection -> breach. src:288
- S10.2-01 POWER of the Minister by Order: other manners of access, to the public or specified persons, on a specified charge or a charge determined and published by the Commissioner. src:289-291
- S10.2-02 Commissioner charges for another manner of access with no Order -> not authorised by 10(2). src:289
- S10.3-01 Governor names of a general-section charity -> public. src:293
- S10.3-02 Purposes of a restricted charity -> public; governor names of a restricted charity -> NOT public. src:294
- S10.3-03 Historic section entry -> public. src:295
- S10.4-01 Commissioner considers (INPUT) public access to a refuge charity's principal address would significantly put a person's safety at risk -> MAY designate it non-public; once designated -> NOT public. src:296-297
- S10.4-02 Commissioner considers a risk exists but is not significant -> no 10(5) power. src:296
- S10.4-03 No designation made despite risk -> still public (power, not duty). src:297
- S10.4-04 Historic-section entry of a deregistered entity -> AMBIG-9: no designation power (10(4) says "a particular registered charity") / power applies ("on any section of the register"). src:296

## Article 11 — src:298-352 (in force 1 May 2018)
- S11.1-01 An entity wishing the advantages of registration may apply; a partnership or a natural person (not an entity) cannot apply under 11(1). src:299
- S11.2-01 Application with every item (a)-(f) in the published form -> 11(2) complied. src:300-315
- S11.2-02 Missing copy of constitution (b) / draft purposes (c) / draft PBS (d) -> 11(2) not complied. src:305-307
- S11.2-03 Applicant with no financial accounts states none -> (e)(i) complied ("most recent, if any"). src:309
- S11.2-04 Applicant requesting restricted entry, without the (e)(iv) prescribed financial information -> complied (exempt); applicant NOT requesting restricted entry, without it (where prescribed) -> not complied. src:312
- S11.2-05 (a)(iii) "if applicable": no ORC, no 5(3) Order, no 13(9)(c), nothing prescribed -> nothing needed. src:304
- S11.2-06 Application on 2025-03-15: governor payment on 2024-03-14 -> outside (both readings). C6
- S11.2-07 Application 2025-03-15: payment 2024-03-15 -> INSIDE (P1) / outside (P2). AMBIG-10.
- S11.2-08 Application 2025-03-15: payment 2024-03-16 -> inside (both); payment 2025-03-14 -> inside (both).
- S11.2-09 Application 2025-03-15: payment on 2025-03-15 itself -> OUTSIDE (P1) / inside (P2). AMBIG-10.
- S11.2-10 Application 2025-03-15: payment 2025-03-16 -> outside (both).
- S11.2-11 Application 2024-02-29: payment 2023-02-28 -> inside (P1+clip) / outside (roll to 2023-03-01); payment 2023-03-01 -> inside (both). AMBIG-10.
- S11.2-12 Application 2025-02-28: payment 2024-02-29 -> inside (both).
- S11.3-01 POWER of the States by Regulations: further information and procedure; content INPUT. src:316-318
- S11.4-00 Complies with (2), Regulations and 19(5) (INPUT) and Commissioner satisfied of (a)-(f) -> MUST register. src:319-327
- S11.4-a1 Does not meet the charity test and will not on registration -> MUST refuse (11(5)). src:320,328
- S11.4-a2 Does not meet the test now but will on registration -> (a) satisfied. src:320
- S11.4-b1 Constitution unwritten (oral) -> MUST refuse. src:321
- S11.4-c1 Jersey entity with no substantial Jersey activity -> (c) satisfied. src:323
- S11.4-c2 Not a Jersey entity ((j) English company), carries out an activity in Jersey the Commissioner considers substantial -> (c) satisfied. src:324
- S11.4-c3 Not a Jersey entity, intends to carry out from within Jersey an activity the Commissioner considers substantial -> (c) satisfied. src:324
- S11.4-c4 Not a Jersey entity, no substantial activity -> MUST refuse. src:322-324
- S11.4-d1 No principal address in Jersey (S8.4-07) -> MUST refuse. src:325
- S11.4-e1 Name undesirable under Art 12 -> MUST refuse. src:326
- S11.4-f1 A prescribed mandatory refusal ground applies -> MUST refuse; a prescribed discretionary ground the Commissioner considers should be applied -> MUST refuse; one he considers should not be applied -> (f) satisfied. src:327
- S11.4-p1 19(5) statement missing (or (2), or Regulations, not complied) -> no duty to register; AMBIG-11: must refuse (11(5)) / no decision owed (application incomplete, 19(6)). src:319,328
- S11.5-01 Not satisfied of any one of (a)-(f) -> must refuse; no discretion to register. src:328
- S11.6-01 DUTY: substantiality guidance published and maintained; Art 5(6)-(8) apply to it, so issuing it without consulting the Minister is a breach; the Commissioner must have regard to it; charity, governor, tribunal and court must have regard. src:329-333
- S11.7-01 POWER of the States by Regulations: further must/may refusal grounds, e.g. sole governor not carrying on prescribed RFSB as governor; related governors. Content INPUT. src:334-336
- S11.8-01 POWER of the Minister by Order: decision period and notification (content INPUT). src:337-340
- S11.8-02 Order relieving small applicants from 11(2)(e)(i), after consulting the Commissioner AND a representative body -> valid under 11(8)(b). src:341-343
- S11.8-03 Same Order without consulting the Commissioner -> not valid under 11(8)(b); without a representative body -> not valid. src:341
- S11.8-04 Order relieving from 11(4)(a) (the charity test) -> outside 11(8)(b) (only "any provision of paragraph (2)"). src:341
- S11.9-01 DUTY on registering: certificate with registered name, registration number, date of registration. src:345
- S11.9-02 DUTY on entering a new or alternative name under 12(5): further certificate with that name and the date entered. src:346
- S11.10-01 Applicant required to be NPO-registered but not -> DUTY: provide the additional JFSC information and request NPO registration. src:347-349
- S11.10-02 Applicant already NPO-registered, or not required to be -> no 11(10) duty. src:347
- S11.11-01 Commissioner receives the information and request -> DUTY: pass to the JFSC; JFSC DUTY: treat it as an NPO application. No request received -> no duty. src:350-352

## Article 12 — src:353-370 (in force 1 May 2018)
- S12.1-01 Proposed name identical to a registered charity's name -> undesirable (a). src:355
- S12.1-02 Name too similar in the Commissioner's opinion (INPUT) -> undesirable (a). src:355
- S12.1-03 Name identical to a DEREGISTERED charity's former name, no other ground -> NOT undesirable under (a) (not "any other registered charity"). src:355
- S12.1-04 Misleading as to purpose, activities or identity (INPUT) -> undesirable (b). src:356
- S12.1-05 Implies a connection with a person it is not connected to (INPUT) -> undesirable (c). src:357
- S12.1-06 Offensive (INPUT) -> undesirable (d). src:358
- S12.1-07 None of (a)-(d) -> not undesirable. src:354
- S12.2-01 DUTY on registering: enter the name (registered name), allocate and enter a number (registration number). src:359-361
- S12.3-01 POWER: a registered charity may apply to change its name or add an alternative; an unregistered entity cannot apply under 12(3). src:362
- S12.4-01 Any of (a)-(d) applies to the proposed name -> MUST refuse permission. src:363
- S12.4-02 None applies -> AMBIG-12: MAY grant (discretion) / must grant. src:363-364
- S12.5-01 Permission granted AND the charity notifies the change -> MUST enter the new or alternative name (and 11(9)(b) certificate; 8(3)(l) previous name if changed). src:364
- S12.5-02 Granted but no notification yet -> no duty to enter; notification without permission -> no duty. src:364
- S12.6-01 Charity reports a name matter under 13(6)(b) (INPUT) -> Commissioner MAY require an application to change the name; no such report -> 12(6) not triggered. src:365
- S12.7-01 Charity uses its registered name, or one of its registered names -> permitted. src:367
- S12.7-02 Uses a related name (abbreviation) the Commissioner considers not undesirable in context -> permitted. src:368-370
- S12.7-03 Uses a related name the Commissioner considers undesirable in context -> PROHIBITED (contravention). src:370
- S12.7-04 Uses an unrelated trading name -> PROHIBITED. src:368-369
- S12.7-05 Related name, Commissioner has formed no opinion -> AMBIG-13: permitted (no adverse opinion) / prohibited (an opinion of "not undesirable" is needed). src:370
- S12.7-06 A 12(7) contravention is misconduct (2(10)(a)(i)); 12(7) states no offence or penalty -> no penalty. src:106-107,366

## Commencement of Articles 1 to 12 (endnotes, R&O.17/2018)
- SC-01 Articles 1-7 on 2014-11-20 -> not in force; on 2014-11-21 -> in force. src:876-877
- SC-02 Articles 8-12 on 2014-11-21 -> NOT in force; on 2018-04-30 -> not in force; on 2018-05-01 -> in force. src:878-879
- SC-03 An application under Art 11 made 2018-04-30 -> no right to apply / no duty to register; made 2018-05-01 -> Art 11 applies.
- SC-04 Articles 1-12 on 2026-10-27 -> in force. Article 2(1)(ba) on 2025-10-15 -> absent; 2025-10-16 -> present (C5).

## Ambiguities (two answers written; each is a candidate Interpretation reading)

- AMBIG-1 Does a range "(a) to (h)" written in 2014 (2(3)(a), 2(1)(j)) include the 2025-inserted (ba)? Mine: yes. Discriminator: a (ba) body -> Jersey entity?
- AMBIG-2 2(5)(e) "incorporated by (but not under) any other Law": literal (no constitutional Law for (g) bodies) vs purposive (that Law). Discriminator: an LLC under a Jersey LLC Law. Mine: literal.
- AMBIG-3 An entity in two limbs ((f) company that is trustee, (a)): which limb of 2(4) and 2(7) governs? Discriminator: governor = company or its directors.
- AMBIG-4 5(2)(a) "a Minister": any Minister (mine) vs Art 1 "Minister" (Chief Minister).
- AMBIG-5 5(1) entity with no purposes. Mine: fails.
- AMBIG-6 8(5)(b) "if the entity was registered in the general section" for a charity that moved general -> restricted before deregistration. Mine: section at deregistration (no name).
- AMBIG-7 8(6) start event and counting (C7).
- AMBIG-8 9(6) all satisfied: may (mine) vs must enter.
- AMBIG-9 10(4)-(5) designation over historic-section entries. Mine: literal, no power.
- AMBIG-10 11(2)(e)(ii) window ends (C6). Mine: P1 + clip.
- AMBIG-11 11(4)/(5) when a precondition fails: must refuse vs no decision owed.
- AMBIG-12 12(4) no ground: may (mine) vs must grant.
- AMBIG-13 12(7)(b)(ii) no opinion formed: permitted (mine) vs prohibited.
- AMBIG-SRC "Minister"/"Comptroller" before the first amending instrument (C3): Chief Minister / Income Tax Law (mine) vs REFUSE; 27 Feb 2024 date-only REFUSE.

## Source defects noticed (for report item 6)

- src:111 "in relation a registered charity" (missing "to").
- src:227 "with the meaning of paragraph (4)" (for "within").
- src:261-262 9(2)(a)/(b) say "the applicant meets", though 9(2) also lets a general-section charity request.
- src:300 11(2) "an entity of a description into which that charity falls" and src:310 "applies to the registered charity": the applicant is not yet a charity.
- src:85 vs src:62: 2(5)(e) "by (but not under)" against 2(1)(g) "under, but not by" (AMBIG-2).
- src:129 vs src:136: the Bailiff is in 4(1)(e) but not in 4(3)(c).
- src:296 10(4) "a particular registered charity" vs "any section of the register" including the historic section (AMBIG-9).
- R&O.40/2019 Sch 2 para 1(e) cites "Article 1(1) of the Charities (Jersey) Law 2014"; that Article 1 has no paragraph (1) (R&O.29/2021 and later cite "Article 1").

## Counts (scenario lines per Article, decided before opening the encoding)

Counted by `grep -c '^- S<n>[.-]'` after writing: see the table appended below.

| Article | scenario lines | note |
| --- | --- | --- |
| 1 | 35 | |
| 2 | 84 | |
| 3 | 1 | |
| 4 | 10 | |
| 5 | 28 | |
| 6 | 33 | |
| 7 | 8 | |
| 8 | 31 | |
| 9 | 26 | |
| 10 | 10 | |
| 11 | 38 | |
| 12 | 20 | |
| commencement | 4 | |
| total | 328 | S2.3-01..08 is one line for 8 scenarios; several lines carry two or three cases |

Expectations file closed at 2026-10-26T16:12:13Z (UTC) before any encoding file was opened.
