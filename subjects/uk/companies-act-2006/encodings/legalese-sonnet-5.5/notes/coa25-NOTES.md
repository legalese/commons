# NOTES (coa25): Companies Act 2006 (United Kingdom), 2006 c. 46, lines 16190-16445 and 16625-16995 of `ukpga-2006-46.txt`

Written by part agent `coa25` (Sonnet 5.5), 2026-11-13. Part 37 "Companies: supplementary provisions" (ss 1134 to 1157), Part 39 "Companies: minor amendments" (ss 1175 to 1181), Part 40 "Company directors: foreign disqualification etc" (ss 1182 to 1191) and Part 41 "Business names" (ss 1192 to 1208). Status: written and tested on the stable builds `L4_BIN` (1.6.110, main, e51181d) and `L4_MAIN` (1.6.109, main, 4c887e0) with every assertion satisfied on both (numbers under "What `check.sh` printed"); `srcrefs.py check --strict` reports 0 problems for every layer-1 file. Not reviewed by a lawyer. Target: `main` (stable); no unstable syntax is used.

## Source and what "verified" means here

The only source is `ukpga-2006-46.txt`, a plain-text rendering of the Act and its Schedules from legislation.gov.uk (Open Government Licence v3.0) made by a converter script (`inputs/SOURCES.md`); it is **not the official text, and nothing here is "verified against the official text"**. It is the revised text at the version stated as 2026-07-16, which "may carry more than one extent version of a provision, and prospective provisions" (`inputs/SOURCES.md`): section 1139 shows subsections (2) and (3) twice for that reason (finding 1, fork F1). Every `-- src:` line was produced by `srcrefs.py quote` from that file and the gate (`check --strict`) passes. Some words in the rendering look like converter artefacts (for example "Charities Act 2011or section 33" in s 1140(2)(c)(ii) and s 1154(2)(b), with no space, and "...", the omitted words in ss 1190(1) and 1191(1)); the quote lines copy them as they stand. The five rows of dots in s 1136(2), the two in s 1156, and ss 1175 and 1189 are blank in this text and are `repealed or blank` rows.

## Seat

The seat is the one the brief gives: **an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one**, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.) Officials, courts and the registrar are parties the text names (`Party` in the core and the small party types of the modules) and never a seat.

**Each question asks what its function answers, so that `JUST TRUE` reads as "yes" to the question as printed.** Where a function answers whether a prohibition or a duty has been breached (`s 1137(5)(b)`, `s 1194(1)`, `s 1198A(1)`, `s 1198B(1)`), the question asks whether the person is prevented or in breach, not whether they may; a bar's NOTHING and `JUST FALSE` are not a grant, so no question is worded as a permission to be answered by negating the function. A question that asks about a requirement asks whether it has been complied with (`s 1202(1)`, `s 1204(1)`), not whether it exists. This was audited over all 87 questions.

**Assumed, not ruled (Chapter 2 of Part 41, ss 1200 to 1206).** That Chapter applies to an individual or a partnership carrying on business under a business name, not to a company (s 1200(1)). Its questions are asked by the individual or partner who carries on the business (what they must disclose, display and give) and by a customer or supplier who deals with it (what they can require, and the defence of s 1206). Chapter 1 (ss 1192 to 1199A) applies to "any person carrying on business in the United Kingdom": its questions are asked by an individual who carries on business, or by a director of a company that does. This stretch of the seat goes a little beyond "a director, secretary or member", on the brief's words "or who deals with one".

Part 39 (amendments and repeals of other Acts) and the regulation-making powers of Parts 37, 40 and 41 are machinery (inert, reason 2): the seat layer asks nothing about them. Provisions that address only an official are encoded in layer 1 for what they decide (the court's power to relieve under s 1157, the Secretary of State's power to withdraw approval under s 1196, the registrar's notice under s 1154) and in layer 2 only for what they mean to the individual (can the court relieve me; may my approval be withdrawn; who must notify the registrar of my appointment).

## What is encoded and what is not

Encoded, in nine layer-1 modules and one seat layer: every operative provision of the two ranges (sections 1134 to 1157 and 1175 to 1208): the definitions (company records, relevant provisions, service address, company communications provisions, associate, the court, subject to foreign restrictions, disqualification undertaking, associated undertaking, local authority, crime, serious crime, business name, lawful business name, partnership, surname and the others), the duties and their offences and penalties (ss 1135, 1138, 1145, 1153, 1155, 1193, 1194, 1196A, 1197, 1198, 1198A, 1198B, 1203, 1205), the periods (21 days, 14 days, 14 days beginning, twelve months, 48 hours counted over working days only), and the exceptions and savings (ss 1198A(2), 1198B(2), 1199, 1199A). Each rule is a decision function over plain facts, citing its lines with `@ref` and `src:` locators; the duties that name a party are also regulative rules run with `#TRACE`. **Not encoded (inert):** headings, signposts and lead-ins, regulation-making powers and their procedure, amendments and repeals of other Acts and the saving of s 1176(4); each is a row in the coverage table with its reason. Nothing is left `deferred`.

Inputs, not guesses: the pounds a level on the standard scale or the statutory maximum stands for, and "the general limit in a magistrates' court" (ss 1186 and 1191), are asked as numbers and never supplied; the working-day calendar of s 1173(1) is an input (a function in layer 1, a list of dates in the seat); the answers of other parts (s 1121 "officer in default", s 790C, s 1212, s 1162, Schedules 4 and 5, s 2(1)) are `MAYBE BOOLEAN` inputs under the names PLAN.md section 4 gives them.

### Reading a result: FALSE and NOTHING (coa25)

The rule of 2026-10-29 (assumed, not ruled by a lawyer) as it reads in this part. Almost every function answers `MAYBE BOOLEAN`.

- `JUST TRUE`: the text says yes (a definition "means" it; a power or privilege is exercisable on the facts; for a "has complied" function, every requirement that engages is met).
- `JUST FALSE` (a "no"): the text says no in its own words: a "means" or "are to" definition (for example s 1134 "company records" means; s 1200(1) "a person to whom this Chapter applies"); a closed list handed the definition ("The following are the permitted additions", s 1136(2) "The relevant provisions are"); an "if" or "where" that fails (the 2026-11-05 ruling, for example s 1145(1) "Where a member ... has received a document ... otherwise than in hard copy form"); a flat negative ("The company may not make a charge", s 1145(3); "Nothing in this section shall be read as preventing", s 1137(5); "does not apply", s 1138(4)); a period the text fixes in its own words (the 21 days of s 1145(2), the 14 days of s 1155(1)). Each such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- `NOTHING` ("not covered"): the text does not decide the case: it lists without closing the list (s 1140(2), s 1202(1), s 1207), says "includes" (s 1148(1), s 1208), leaves a term undefined or points to a power, regulation or other Act outside the sources (s 1197 regulations, s 1181(4), the Schedules 4 and 5 answers), is silent (the part of the United Kingdom for a summary penalty), or limits a grant or prohibition in its own wording and the case falls outside the limit ("without the approval of the Secretary of State", s 1193(1); "without reasonable excuse", ss 1203(4) and 1205(1); "every officer ... who is in default"; "within the period of 14 days" for a notice not yet due). Each such branch carries `-- NOTHING-kind (<why>)`, <why> being one of silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- **A caller must never turn `NOTHING` into `FALSE`.** In the seat layer `NOTHING` comes back as a null answer; it is never the same as "no".
- **A "has complied" function answers `JUST TRUE` when the requirement does not engage** (nothing is left to fail: fork F5), and `JUST FALSE` only for a requirement that engages and is not met. A separate "the duty applies" function answers `JUST FALSE` where a "where" fails (2026-11-05 ruling (b)).
- **A "who contravenes" offence** answers `JUST FALSE` when there is no contravention (the offence is defined by it: marginal reading (a), fork F17); **"every officer ... who is in default"** answers `NOTHING` for an officer not in default (a named complement: marginal reading (b)).
- `REFUSE` does not exist for this target: "not covered" is `NOTHING` or a constructor, asserted in the tests.

## Coverage (coa25)

Every non-blank line of the two ranges falls in exactly one row (the audit below): **271 rows**: 166 encoded, 11 fork, 7 repealed or blank in this text, 30 inert (reason 1: headings, signposts, lead-ins), 57 inert (reason 2: machinery: regulation-making powers, procedure, amendments and repeals of other Acts, a saving that affects no one now), 0 inert (reason 3). There is no `out-of-scope` row and no `deferred` row. A `fork` row is one whose reading is itself the fork (the two texts of s 1139(2)-(3); the day count of s 1155(1)); other encoded rows that rest on a fork name it in the note.

| provision | text lines | disposition | L4 name(s) | note |
| --- | --- | --- | --- | --- |
| Part 37 heading | 16190 | inert (reason 1: not operative) | - | heading |
| cross-heading "Company records" | 16191 | inert (reason 1: not operative) | - | heading |
| s 1134 "company records", (a)-(b) | 16192-16195 | encoded | `s 1134 the document is a company record` |  |
| s 1135(1)(a)-(b) and proviso: form and arrangement of company records | 16196-16200 | encoded | `s 1135(1) the company may keep its records in this way`; `s 1135 the company has complied with this section` |  |
| s 1135(2) electronic records reproducible in hard copy | 16201 | encoded | `s 1135(2) the requirement of reproduction in hard copy form applies`; `s 1135(2) the company has met the requirement of reproduction in hard copy form`; `s 1135 the company has complied with this section`; `s 1135(2) the company must keep electronic records capable of reproduction in hard copy form` |  |
| s 1135(3) offence | 16202 | encoded | `s 1135(3) an officer of the company commits an offence` |  |
| s 1135(4) penalty | 16203 | encoded | `s 1135(4) the penalty for an offence under s 1135` |  |
| s 1135(5) pre-1979 instruments requiring a hard copy debenture register | 16204 | encoded | `s 1135(5) the instrument's requirement is to be read as requiring hard copy or electronic form` |  |
| s 1136(1) regulations about where certain records are kept | 16205-16206 | inert (reason 2: machinery) | - | regulation-making power |
| s 1136(2) the "relevant provisions": lead-in and s 114 | 16207-16208 | encoded | `s 1136(2) the provision is a relevant provision` |  |
| s 1136(2) two entries shown as dots | 16209-16210 | repealed or blank in this text | - | the text shows two rows of dots |
| s 1136(2) ss 228 and 237 | 16211-16212 | encoded | `s 1136(2) the provision is a relevant provision` |  |
| s 1136(2) one entry shown as dots | 16213 | repealed or blank in this text | - | the text shows a row of dots |
| s 1136(2) ss 358, 702, 720, 743 | 16214-16217 | encoded | `s 1136(2) the provision is a relevant provision` |  |
| s 1136(2) two entries shown as dots | 16218-16219 | repealed or blank in this text | - | the text shows two rows of dots |
| s 1136(2) ss 805, 809, 859Q | 16220-16222 | encoded | `s 1136(2) the provision is a relevant provision` |  |
| s 1136(3) what the regulations may specify | 16223 | inert (reason 2: machinery) | - | regulation-making power |
| s 1136(4) conditions the regulations may impose | 16224 | inert (reason 2: machinery) | - | regulation-making power |
| s 1136(5)(a)-(b) the regulations need not / may specify places | 16225-16227 | inert (reason 2: machinery) | - | regulation-making power |
| s 1136(6) all the records must be kept at the specified place | 16228 | encoded | `s 1136(6) keeping the records available for inspection at the place complies with the requirement` |  |
| s 1136(7) negative resolution procedure | 16229 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1137(1)(a)-(b) regulations about inspection and copies | 16230-16233 | inert (reason 2: machinery) | - | regulation-making power |
| s 1137(2) failure to comply with the regulations treated as refusal | 16234 | encoded | `s 1137(2) the company is treated as having refused or failed` |  |
| s 1137(3)(a)-(b) what the regulations may provide | 16235-16237 | inert (reason 2: machinery) | - | regulation-making power |
| s 1137(4) fees | 16238 | inert (reason 2: machinery) | - | regulation-making power |
| s 1137(5)(a)-(b) a company may give more or charge less | 16239-16241 | encoded | `s 1137(5)(a) the company is prevented from affording more extensive facilities than the regulations require`; `s 1137(5)(b) the company is prevented from charging a lesser fee or none at all` |  |
| s 1137(6) negative resolution procedure | 16242 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1138(1)(a)-(b) precautions against falsification | 16243-16246 | encoded | `s 1138(1) the duty to take precautions applies to the records`; `s 1138 the company has complied with this section`; `s 1138(1) the company must take adequate precautions against falsification` |  |
| s 1138(2) offence | 16247 | encoded | `s 1138(2) an officer of the company commits an offence` |  |
| s 1138(3) penalty | 16248 | encoded | `s 1138(3) the penalty for an offence under s 1138` |  |
| s 1138(4)(a)-(b) records under s 228 and s 237 excepted | 16249-16251 | encoded | `s 1138(4) this section applies to the company record` |  |
| cross-heading "Service addresses" | 16252 | inert (reason 1: not operative) | - | heading |
| s 1139(1) service on a company registered under this Act | 16253-16254 | encoded | `s 1139(1) service of the document on the company is effected` |  |
| s 1139(2)(a)-(b) service on an overseas company, FIRST text | 16255-16257 | fork | `s 1139(2) first text: service of the document on the overseas company is effected` | fork F1 (two versions of s 1139(2)-(3) in the text) |
| s 1139(3) "registered address", FIRST text | 16258 | fork | `s 1139(3) first text: the address is the person's registered address` | fork F1 |
| s 1139(2)(a)-(b) service on an overseas company, SECOND text | 16259-16261 | fork | `s 1139(2) second text: service of the document on the overseas company is effected` | fork F1 |
| s 1139(3)(a)-(b) "registered address", SECOND text | 16262-16264 | fork | `s 1139(3)(a) second text: the address is the registered address of the overseas company`; `s 1139(3)(b) second text: the address is the registered address of a person other than the overseas company` | fork F1 |
| s 1139(4) process on a company registered in Scotland or Northern Ireland carrying on business in England and Wales | 16265 | encoded | `s 1139(4) service of the process on the company is effected` |  |
| s 1139(4) the person issuing out the process must send a copy by post to the registered office | 16266 | encoded | `s 1139(4) the duty to send a copy of the process to the registered office applies`; `s 1139(4) the person issuing out the process has complied with the duty to send a copy`; `s 1139(4) the person issuing out the process must send a copy to the registered office` |  |
| s 1139(5) further provision in the company communications provisions | 16267 | inert (reason 1: not operative) | - | signpost, fork F2 |
| s 1140(1) service on a director, secretary or other person to whom the section applies | 16268-16269 | encoded | `s 1140(1) service of the document on the person is effected` |  |
| s 1140(2)(a)-(c) persons to whom s 1140 applies | 16270-16277 | encoded | `s 1140(2) the section applies to the person` |  |
| s 1140(3) applies whatever the purpose of the document | 16278-16279 | encoded | `s 1140(3) the section applies to the document` |  |
| s 1140(4) "registered address" | 16280 | encoded | `s 1140(4) the address is the person's registered address` |  |
| s 1140(5) a change of address: 14 days | 16281 | encoded | `s 1140(5) the document is validly served at the address previously registered` |  |
| s 1140(6)(a)-(b) when service may not be effected | 16282-16284 | encoded | `s 1140(6) service may be effected by virtue of s 1140 at the address` |  |
| s 1140(7) further provision in the company communications provisions | 16285 | inert (reason 1: not operative) | - | signpost, fork F2 |
| s 1140(8) no effect on permission for service out of the jurisdiction | 16286 | encoded | `s 1140(8) the section affects the requirement of permission for service out of the jurisdiction` |  |
| s 1141(1) "service address" | 16287-16288 | encoded | `s 1141 the address is a service address` |  |
| s 1141(2) regulations specifying conditions | 16289 | inert (reason 2: machinery) | - | regulation-making power |
| s 1141(3) negative resolution procedure | 16290 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1142 an obligation to give an address is to give a service address | 16291-16292 | encoded | `s 1142 the address to be given is a service address` |  |
| cross-heading "Sending or supplying documents or information" | 16293 | inert (reason 1: not operative) | - | heading |
| s 1143(1) the company communications provisions | 16294-16295 | encoded | `s 1143(1) the provision is one of the company communications provisions`; `s 1143(1) the company communications provisions have effect for the purposes of the provision` |  |
| s 1143(2) subject to contrary provision | 16296 | encoded | `s 1143(2) the company communications provisions yield to the other provision` |  |
| s 1143(3) subject to Part 35 for documents sent to the registrar | 16297 | encoded | `s 1143(3) the company communications provisions yield to Part 35` |  |
| s 1143(4) express authority to use a form is not contrary provision | 16298 | encoded | `s 1143(4) the provision is regarded as contrary to the company communications provisions` |  |
| s 1144(1) documents to a company: Schedule 4 | 16299-16300 | encoded | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |  |
| s 1144(2) documents by a company: Schedule 5 | 16301 | encoded | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |  |
| s 1144(3) company to company: Schedule 5 only | 16302 | encoded | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |  |
| s 1145(1) right to a hard copy version | 16303-16304 | encoded | `s 1145(1) the person is entitled to require the company to send a hard copy version`; `s 1145 the company has complied with this section` |  |
| s 1145(2) the company must send it within 21 days | 16305 | encoded | `s 1145(2) the last day for sending the hard copy version`; `s 1145(2) the company sent the hard copy version in time`; `s 1145 the company has complied with this section`; `s 1145(2) the company must send the hard copy version within 21 days` |  |
| s 1145(3) no charge | 16306 | encoded | `s 1145(3) the company may make a charge for providing the hard copy version`; `s 1145 the company has complied with this section` |  |
| s 1145(4) offence | 16307 | encoded | `s 1145(4) the company commits an offence`; `s 1145(4) an officer of the company commits an offence` |  |
| s 1145(5) penalty | 16308 | encoded | `s 1145(5) the penalty for an offence under s 1145` |  |
| s 1146(1) authentication: application | 16309-16310 | encoded | `s 1146(1) the section applies to the authentication of the document or information` |  |
| s 1146(2) hard copy sufficiently authenticated if signed | 16311 | encoded | `s 1146(2) the hard copy document or information is sufficiently authenticated` |  |
| s 1146(3)(a)-(b) electronic form sufficiently authenticated | 16312-16314 | encoded | `s 1146(3) the electronic document or information is sufficiently authenticated` |  |
| s 1146(4) authority to act on behalf of another | 16315 | encoded | `s 1146(4) the section affects the provision of the articles requiring evidence of authority` |  |
| s 1147(1) deemed delivery: application | 16316-16317 | encoded | `s 1147 the day the document is treated as delivered` |  |
| s 1147(2)(a)-(b) by post: 48 hours | 16318-16321 | encoded | `s 1147(2) the instant at which the document or information is deemed received by post` |  |
| s 1147(3)(a)-(b) by electronic means: 48 hours | 16322-16325 | encoded | `s 1147(3) the instant at which the document or information is deemed received by electronic means` |  |
| s 1147(4)(a)-(b) by means of a website | 16326-16328 | encoded | `s 1147(4) the instant at which the document or information is deemed received by means of a website` |  |
| s 1147(5) hours counted only over working days | 16329 | encoded | `s 1147(5) count the hours from the instant over working days only`; `s 1147(5) the instant at which the period of hours ends` |  |
| s 1147(6)(a)-(c) subject to articles, instrument, agreement | 16330-16333 | encoded | `s 1147(6) the deeming rules yield to the contrary provision` |  |
| s 1148(1) "address", "company", "document" | 16334-16338 | encoded | `s 1148(1) the thing is an address`; `s 1148(1) the body is a company`; `s 1148(1) the thing is a document` |  |
| s 1148(2) references to provisions authorising or requiring | 16339 | encoded | `s 1148(2) the reference includes the provision, whatever expression is used` |  |
| s 1148(3) by or to the directors on behalf of the company | 16340 | encoded | `s 1148(3) the reference to sending or supplying by or to a company includes the case` |  |
| cross-heading "Requirements as to independent valuation" | 16341 | inert (reason 1: not operative) | - | heading |
| s 1149 which valuations ss 1150 to 1153 apply to | 16342-16346 | encoded | `s 1149 sections 1150 to 1153 apply to the valuation and report` |  |
| s 1150(1)(a)-(b) the valuer | 16347-16350 | encoded | `s 1150(1) the person may make the valuation and report` |  |
| s 1150(2)(a)-(b)(i)-(ii) another person may value | 16351-16357 | encoded | `s 1150(2) the valuer may arrange for or accept a valuation made by the other person` |  |
| s 1150(3) "officer or employee" does not include an auditor | 16358 | encoded | `s 1150(3) the person counts as an officer or employee for subsection (2)(b)` |  |
| s 1150(4)(a)-(b) the valuer's report where another person values | 16359-16361 | encoded | `s 1150(4) the requirement as to the valuer's report applies`; `s 1150(4) the valuer's report contains what is required`; `s 1150(4) the valuer must state in the report what is required` |  |
| s 1151(1)(a)-(c) the independence requirement | 16362-16373 | encoded | `s 1151(1) the person meets the independence requirement` |  |
| s 1151(2) an auditor is not an officer or employee | 16374 | encoded | `s 1151(2) the person is regarded as an officer or employee of the company for the independence requirement` |  |
| s 1151(3) "associated undertaking" and "associate" | 16375-16379 | encoded | `s 1151(3) the undertaking is an associated undertaking of the company` |  |
| s 1151(4) negative resolution procedure | 16380 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1152(1) this section defines "associate" | 16381-16382 | inert (reason 1: not operative) | - | lead-in, fork F2 |
| s 1152(2)(a)-(c) associate of an individual | 16383-16386 | encoded | `s 1152(2) the other person is an associate of the individual` |  |
| s 1152(3)(a)-(c) associate of a body corporate | 16387-16390 | encoded | `s 1152(3) the other person is an associate of the body corporate` |  |
| s 1152(4)(a)-(c) associate of a partnership that is a legal person | 16391-16394 | encoded | `s 1152(4) the other person is an associate of the partnership that is a legal person` |  |
| s 1152(5) associate of a partnership that is not a legal person | 16395 | encoded | `s 1152(5) the other person is an associate of the partnership that is not a legal person` |  |
| s 1152(6) limited liability partnership: for "director" read "member" | 16396 | encoded | `s 1152(2) the other person is an associate of the individual`; `s 1152(3) the other person is an associate of the body corporate`; `s 1152(4) the other person is an associate of the partnership that is a legal person` | carried by the limited liability partnership constructors of the three functions (fork F13) |
| s 1153(1)(a)-(b) valuer entitled to information and explanation | 16397-16400 | encoded | `s 1153(1) the person is entitled to require the information and explanation from the officers of the company` |  |
| s 1153(2) offence: misleading, false or deceptive statement | 16401 | encoded | `s 1153(2) the person commits an offence` |  |
| s 1153(3)(a)-(b) the statement to which (2) applies | 16402-16404 | encoded | `s 1153(3) the statement is one to which subsection (2) applies` |  |
| s 1153(4)(a)-(b)(i)-(ii) penalty | 16405-16409 | encoded | `s 1153(4) the penalty for an offence under s 1153(2)` |  |
| cross-heading "Notice of appointment of certain officers" | 16410 | inert (reason 1: not operative) | - | heading |
| s 1154(1)(a)-(c) notice of appointment to the registrar | 16411-16415 | encoded | `s 1154(1) notice of the appointment must be given to the registrar` |  |
| s 1154(2)(a)-(c) who gives the notice | 16416-16420 | encoded | `s 1154(2) the person who must give the notice` |  |
| s 1154(3) the notice must specify an address for service | 16421 | encoded | `s 1154(3) the notice meets the requirement as to the address for service` |  |
| s 1154(3) notice of a change in the address for service may be given by the person appointed | 16422 | encoded | `s 1154(3) the person may give the registrar notice of a change in the address for service` |  |
| s 1154(4) notice of termination | 16423-16424 | encoded | `s 1154(4) notice of the termination of the appointment must be given to the registrar` |  |
| s 1155(1) offence: judicial factor fails to give notice within 14 days | 16425-16426 | fork | `s 1155(1) the judicial factor commits an offence`; `s 1155(1) the judicial factor must give the registrar notice within 14 days` | fork F3 (the day of appointment) |
| s 1155(2) penalty | 16427 | encoded | `s 1155(2) the penalty for an offence under s 1155` |  |
| cross-heading "Courts and legal proceedings" | 16428 | inert (reason 1: not operative) | - | heading |
| s 1156(1)(a)-(c) "the court" | 16429-16433 | encoded | `s 1156(1) the courts that are "the court" in the part of the United Kingdom`; `s 1156(1) the tribunal is the court` |  |
| s 1156(2) subject to allocation of jurisdiction | 16434 | encoded | `s 1156(2) the jurisdiction conferred on the court yields to the allocation of jurisdiction` |  |
| s 1156(3) shown as dots | 16435 | repealed or blank in this text | - | the text shows a row of dots |
| s 1156(4) shown as dots | 16436 | repealed or blank in this text | - | the text shows a row of dots |
| s 1157(1) the court's power to relieve | 16437-16441 | fork | `s 1157(1) the court may relieve the defendant from liability` | fork F19 (a power whose "if" gate is unmet) |
| s 1157(2)(a)-(b) application for relief in anticipation | 16442-16444 | encoded | `s 1157(2)(a) the person may apply to the court for relief`; `s 1157(2)(b) the court has the same power to relieve the applicant` |  |
| s 1157(3) judge withdraws the case from the jury | 16445 | fork | `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant` | fork F27 (the "if" limb) |
| Part 39 heading | 16625 | inert (reason 1: not operative) | - | heading |
| s 1175 heading and body shown as dots | 16626-16627 | repealed or blank in this text | - | the text shows a row of dots |
| s 1176(1) s 438 of the 1985 Act ceases to have effect | 16628-16629 | inert (reason 2: machinery) | - | amendment of another Act |
| s 1176(2)(a)-(c) amendments of s 439 of the 1985 Act | 16630-16635 | inert (reason 2: machinery) | - | amendment of another Act |
| s 1176(3) amendment of s 453(1A) of the 1985 Act | 16636 | inert (reason 2: machinery) | - | amendment of another Act |
| s 1176(4) saving for proceedings begun before commencement | 16637 | inert (reason 2: machinery) | - | saving affecting no one now |
| s 1177 repeal of provisions of Part 10 of the 1985 Act | 16638-16643 | inert (reason 2: machinery) | - | repeal of provisions of another Act |
| s 1178 repeal of s 720 of the 1985 Act and Schedule 23 | 16644-16647 | inert (reason 2: machinery) | - | repeal of provisions of another Act |
| s 1179 repeal of s 729 of the 1985 Act | 16648-16649 | inert (reason 2: machinery) | - | repeal of a provision of another Act |
| s 1180 repeal of Part 4 of the Companies Act 1989 | 16650-16651 | inert (reason 2: machinery) | - | repeal of provisions of another Act |
| s 1181(1)(a)-(b) order amending the 1993 and 2002 Acts | 16652-16655 | inert (reason 2: machinery) | - | order-making power and amendment of other Acts |
| s 1181(2) what the references include | 16656 | inert (reason 2: machinery) | - | scope of the order-making power |
| s 1181(3) negative resolution procedure | 16657 | inert (reason 2: machinery) | - | procedure for orders |
| s 1181(4) "RTE companies" and "RTM companies" | 16658-16660 | encoded | `s 1181(4) the company is an RTE company`; `s 1181(4) the company is an RTM company` |  |
| Part 40 heading | 16661 | inert (reason 1: not operative) | - | heading |
| cross-heading "Introductory" | 16662 | inert (reason 1: not operative) | - | heading |
| s 1182(1) this section defines "subject to foreign restrictions" | 16663-16664 | inert (reason 1: not operative) | - | lead-in, fork F2 |
| s 1182(2)(a)-(c)(i)-(ii) subject to foreign restrictions | 16665-16673 | encoded | `s 1182(2) the person is subject to foreign restrictions` |  |
| s 1182(3)(a)-(c) acting in connection with the affairs of a company | 16674-16677 | encoded | `s 1182(3) the activity is acting in connection with the affairs of a company` |  |
| s 1182(4)(a)-(b) "company", "director", "receiver" | 16678-16682 | encoded | `s 1182(4)(a) the body is a company for the purposes of s 1182`; `s 1182(4)(b) the person is a director of the company`; `s 1182(4)(b) the officer is a receiver of the company` |  |
| s 1183 "the court" and "UK company" | 16683-16689 | encoded | `s 1183 the courts that are "the court" in Part 40 for the part of the United Kingdom`; `s 1183 the tribunal is the court`; `s 1183 the company is a UK company` |  |
| cross-heading "Power to disqualify" | 16690 | inert (reason 1: not operative) | - | heading |
| s 1184(1)(a)-(c) regulations disqualifying a person | 16691-16695 | inert (reason 2: machinery) | - | regulation-making power |
| s 1184(2)(a)-(b) automatic or by order of the court | 16696-16698 | inert (reason 2: machinery) | - | regulation-making power |
| s 1184(3) disqualification undertaking | 16699 | encoded | `s 1184(3) the undertaking is a disqualification undertaking` | the definition "disqualification undertaking"; the power itself is machinery |
| s 1184(4)(a)-(b) "person disqualified under this Part", breach | 16700-16704 | encoded | `s 1184(4)(a) the person is a person disqualified under this Part`; `s 1184(4)(b) the act is a breach of a disqualification` |  |
| s 1184(5) applications for permission to act | 16705 | inert (reason 2: machinery) | - | regulation-making power |
| s 1184(6) the regulations must provide for ceasing to be disqualified | 16706 | inert (reason 2: machinery) | - | content required of regulations |
| s 1184(7) affirmative resolution procedure | 16707 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1185(1)(a)-(c) different provision for different cases | 16708-16712 | inert (reason 2: machinery) | - | regulation-making power |
| s 1185(2)(a)-(b) applications to the court | 16713-16715 | inert (reason 2: machinery) | - | regulation-making power |
| s 1185(3)(a)-(d) factors | 16716-16720 | inert (reason 2: machinery) | - | regulation-making power |
| s 1185(4) undertakings given to the Secretary of State | 16721 | inert (reason 2: machinery) | - | regulation-making power |
| s 1185(5)(a)-(b) Secretary of State represented at hearing | 16722-16724 | inert (reason 2: machinery) | - | regulation-making power |
| s 1186(1) regulations may create an offence of breach | 16725-16726 | inert (reason 2: machinery) | - | regulation-making power |
| s 1186(2)(a)-(b)(i)-(ii) the ceiling on penalties | 16727-16731 | encoded | `s 1186(2) the greatest penalty that the regulations may provide` |  |
| s 1186(3) offences before 2 May 2022 | 16732 | encoded | `s 1186(2) the greatest penalty that the regulations may provide` |  |
| cross-heading "Power to make persons liable for company's debts" | 16733 | inert (reason 1: not operative) | - | heading |
| s 1187(1)(a)-(b) regulations making a person personally responsible | 16734-16738 | inert (reason 2: machinery) | - | regulation-making power |
| s 1187(2)(a)-(b) joint and several liability | 16739-16741 | encoded | `s 1187(2) the person is jointly and severally liable with the other` |  |
| s 1187(3) "involved in the management" | 16742 | encoded | `s 1187(3) the person is involved in the management of the company` |  |
| s 1187(4)(a)-(c) different provision for different cases | 16743-16746 | inert (reason 2: machinery) | - | regulation-making power |
| s 1187(5) affirmative resolution procedure | 16747 | inert (reason 2: machinery) | - | procedure for regulations |
| cross-heading "Power to require statements to be sent to the registrar of companies" | 16748 | inert (reason 1: not operative) | - | heading |
| s 1188(1)(a)-(b) regulations requiring a statement | 16749-16753 | inert (reason 2: machinery) | - | regulation-making power |
| s 1188(2)(a)-(b) content of the statement | 16754-16756 | inert (reason 2: machinery) | - | regulation-making power |
| s 1188(3) time for the statement | 16757 | inert (reason 2: machinery) | - | regulation-making power |
| s 1188(4)(a)-(c) different provision for different cases | 16758-16761 | inert (reason 2: machinery) | - | regulation-making power |
| s 1188(5) affirmative resolution procedure | 16762 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1189 heading and body shown as dots | 16763-16764 | repealed or blank in this text | - | the text shows a row of dots |
| s 1190(1) statements treated as records relating to a company | 16765-16766 | inert (reason 2: machinery) | - | regulation-making power |
| s 1190(2)(a)-(b) public inspection and removal | 16767-16769 | inert (reason 2: machinery) | - | regulation-making power |
| s 1190(3) conditions for withholding | 16770 | inert (reason 2: machinery) | - | regulation-making power |
| s 1190(4) s 1081 does not apply | 16771 | inert (reason 2: machinery) | - | regulation-making power |
| s 1190(5) "specified" | 16772 | encoded | `s 1190(5) the matter is specified` |  |
| s 1191(1)(a)-(b) regulations may create offences | 16773-16776 | inert (reason 2: machinery) | - | regulation-making power |
| s 1191(2)(a)-(b)(i)-(ii) the ceiling on penalties | 16777-16781 | encoded | `s 1191(2) the greatest penalty that the regulations may provide` |  |
| s 1191(3) offences before 2 May 2022 | 16782 | encoded | `s 1191(2) the greatest penalty that the regulations may provide` |  |
| Part 41 heading | 16783 | inert (reason 1: not operative) | - | heading |
| Chapter 1 heading | 16784 | inert (reason 1: not operative) | - | heading |
| cross-heading "Introductory" | 16785 | inert (reason 1: not operative) | - | heading |
| s 1192(1) application of Chapter 1 | 16786-16787 | encoded | `s 1192(1) this Chapter applies to the person` |  |
| s 1192(2)(a)-(b) surnames | 16788-16790 | encoded | `s 1192(2) this Chapter prevents the business name` |  |
| s 1192(3)(a)-(c) the permitted additions | 16791-16796 | encoded | `s 1192(3) the addition is a permitted addition` |  |
| cross-heading "Sensitive words or expressions" | 16797 | inert (reason 1: not operative) | - | heading |
| s 1193(1)(a)-(c) name suggesting connection with government or public authority | 16798-16802 | encoded | `s 1193(1) the person contravenes the prohibition on a name suggesting connection with government or a public authority` |  |
| s 1193(2) "local authority", "public authority" | 16803-16808 | encoded | `s 1193(2) the body is a local authority`; `s 1193(2) the person or body is a public authority` |  |
| s 1193(3) affirmative resolution procedure | 16809 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1193(4) offence | 16810 | encoded | `s 1193(4) the person commits an offence` |  |
| s 1193(5) body corporate: officers in default | 16811 | encoded | `s 1193(5) an officer of the body corporate commits an offence` |  |
| s 1193(6) penalty | 16812 | encoded | `s 1193(6) the penalty for an offence under s 1193` |  |
| s 1194(1) other sensitive words or expressions | 16813-16814 | encoded | `s 1194(1) the person contravenes the prohibition on a name including a specified word or expression` |  |
| s 1194(2) approval after being made | 16815 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1194(3) offence | 16816 | encoded | `s 1194(3) the person commits an offence` |  |
| s 1194(4) body corporate: officers in default | 16817 | encoded | `s 1194(4) an officer of the body corporate commits an offence` |  |
| s 1194(5) penalty | 16818 | encoded | `s 1194(5) the penalty for an offence under s 1194` |  |
| s 1195(1)(a)-(b) regulations requiring the applicant to seek a view | 16819-16823 | inert (reason 2: machinery) | - | regulation-making power |
| s 1195(2) the applicant must request the department or body | 16824 | encoded | `s 1195(2) the applicant has complied with the requirement to request the view of the department or body`; `s 1195(2) the applicant must request the view of the department or body and submit a statement` |  |
| s 1195(3) the applicant must submit a statement and the response | 16825 | encoded | `s 1195(3) the applicant has complied with the requirement to submit a statement and a copy of any response`; `s 1195(2) the applicant must request the view of the department or body and submit a statement` |  |
| s 1195(4) the Secretary of State may refuse to consider | 16826 | encoded | `s 1195(4) the Secretary of State may refuse to consider the application for approval` |  |
| s 1195(5) "specified" | 16827 | encoded | `s 1195(5) the matter is specified` |  |
| s 1196(1) approval to which s 1196 applies | 16828-16831 | encoded | `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned` |  |
| s 1196(2) withdrawal of approval | 16832 | fork | `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned` | fork F28 (a power whose "if" gate is unmet) |
| s 1196(3) the notice states the date | 16833 | encoded | `s 1196(3) the notice meets the requirement to state a date`; `s 1196(3) the approval has been withdrawn` |  |
| s 1196A(1)(a)-(b) names suggesting connection with foreign governments | 16834-16837 | encoded | `s 1196A(1) the person contravenes the prohibition on a name suggesting connection with a foreign government or an international organisation` |  |
| s 1196A(2) offence | 16838 | encoded | `s 1196A(2) the person commits an offence` |  |
| s 1196A(3) body corporate: officers in default | 16839 | encoded | `s 1196A(3) an officer of the body corporate commits an offence` |  |
| s 1196A(4) penalty | 16840 | encoded | `s 1196A(4) the penalty for an offence under s 1196A` |  |
| cross-heading "Misleading names" | 16841 | inert (reason 1: not operative) | - | heading |
| s 1197(1)(a)-(b) regulations prohibiting names | 16842-16845 | inert (reason 2: machinery) | - | regulation-making power |
| s 1197(2)(a)-(b) what the regulations may prohibit | 16846-16848 | inert (reason 2: machinery) | - | regulation-making power |
| s 1197(3) "specified" | 16849 | encoded | `s 1197(3) the matter is specified` |  |
| s 1197(4) negative resolution procedure | 16850 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1197(5) offence | 16851 | encoded | `s 1197(5) the person commits an offence` |  |
| s 1197(6) body corporate: officers in default | 16852 | encoded | `s 1197(6) an officer of the body corporate commits an offence` |  |
| s 1197(7) penalty | 16853 | encoded | `s 1197(7) the penalty for an offence under s 1197` |  |
| s 1198(1) misleading indication of activities | 16854-16855 | encoded | `s 1198(1) the person uses a name in contravention of the prohibition on a name giving a misleading indication of activities` |  |
| s 1198(2) offence | 16856 | encoded | `s 1198(2) the person commits an offence` |  |
| s 1198(3) body corporate: officers in default | 16857 | encoded | `s 1198(3) an officer of the body corporate commits an offence` |  |
| s 1198(4) penalty | 16858 | encoded | `s 1198(4) the penalty for an offence under s 1198` |  |
| cross-heading "Restrictions where a company has been required to change a name" | 16859 | inert (reason 1: not operative) | - | heading |
| s 1198A(1) a name that a company has been required to change | 16860-16861 | encoded | `s 1198A(1) the company uses the name in contravention of s 1198A` |  |
| s 1198A(2)(a)-(c) exceptions | 16862-16865 | encoded | `s 1198A(2) subsection (1) prevents the company using the name` |  |
| s 1198A(3)(a)-(b) offence | 16866-16868 | encoded | `s 1198A(3)(a) the company commits an offence`; `s 1198A(3)(b) an officer of the company commits an offence` |  |
| s 1198A(4) penalty | 16869 | encoded | `s 1198A(4) the penalty for an offence under s 1198A` |  |
| s 1198A(5) "company", "relevant direction" | 16870-16872 | encoded | `s 1198A(5) the direction is a relevant direction`; `s 1198A(5) the body is a company for the purposes of s 1198A` |  |
| s 1198B(1) a name that another company has been required to change | 16873-16874 | encoded | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies`; `s 1198B(1) the other company uses the name in contravention of s 1198B` |  |
| s 1198B(2)(a)-(c) exceptions | 16875-16878 | encoded | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies`; `s 1198B(2) subsection (1) prevents the other company using the name` |  |
| s 1198B(3) not necessarily at the same time | 16879 | encoded | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies` |  |
| s 1198B(4)(a)-(b) "relevant relationship" | 16880-16882 | encoded | `s 1198B(4) the person has a relevant relationship with the company` |  |
| s 1198B(5)(a)-(b) offence | 16883-16885 | encoded | `s 1198B(5)(a) the company commits an offence`; `s 1198B(5)(b) an officer of the company commits an offence` |  |
| s 1198B(6) penalty | 16886 | encoded | `s 1198B(6) the penalty for an offence under s 1198B` |  |
| s 1198B(7) "company", "relevant direction" | 16887-16889 | encoded | `s 1198B(7) the direction is a relevant direction`; `s 1198B(7) the body is a company for the purposes of s 1198B` |  |
| cross-heading "Supplementary" | 16890 | inert (reason 1: not operative) | - | heading |
| s 1199(1) the sections s 1199 applies to | 16891-16894 | encoded | `s 1199(1) the saving has effect in relation to the provision` |  |
| s 1199(2)(a)-(b) business carried on before commencement | 16895-16897 | encoded | `s 1199(2) sections 1192 to 1197 do not apply to the business` |  |
| s 1199(3)(a)-(b) business transferred: twelve months | 16898-16901 | encoded | `s 1199(3) sections 1192 to 1197 do not apply to the business carried on under that name on the date` |  |
| s 1199(4)(a)-(b) "lawful business name" | 16902-16904 | encoded | `s 1199(4) the name is a lawful business name` |  |
| s 1199A(1)(a)-(b) notice exempting a person from a prohibition | 16905-16908 | fork | `s 1199A(1) the prohibitions of this Chapter do not apply to the business under the name` | fork F25 (a grant whose gate fails) |
| s 1199A(2)(a)-(b)(i)-(ii) "crime" and "serious" | 16909-16915 | encoded | `s 1199A(2)(a) the conduct is crime`; `s 1199A(2)(b) the crime is serious` |  |
| Chapter 2 heading | 16916 | inert (reason 1: not operative) | - | heading |
| cross-heading "Introductory" | 16917 | inert (reason 1: not operative) | - | heading |
| s 1200(1) application of Chapter 2 | 16918-16920 | encoded | `s 1200(1) the person is a person to whom this Chapter applies` |  |
| s 1200(2)(a)-(b)(i)-(ii) "business name" | 16921-16926 | encoded | `s 1200(2) the name is a business name` |  |
| s 1200(3)(a)-(c) the permitted additions | 16927-16932 | encoded | `s 1200(3) the addition is a permitted addition` |  |
| s 1201(1)(a)-(b) "the information required by this Chapter" | 16933-16937 | encoded | `s 1201(1) the disclosure contains the information required by this Chapter` |  |
| s 1201(2) address in the United Kingdom | 16938 | encoded | `s 1201(2) the address meets the requirement as to place` |  |
| s 1201(3) address where there is no place of business in the United Kingdom | 16939 | encoded | `s 1201(3) the address meets the requirement as to delivery` |  |
| cross-heading "Disclosure requirements" | 16940 | inert (reason 1: not operative) | - | heading |
| s 1202(1)(a)-(d) disclosure on business documents | 16941-16947 | encoded | `s 1202(1) the requirement to state the information applies to the document`; `s 1202(1) the person has complied with the requirement to state the information on the document`; `s 1202(1) the person must state the information on the document` |  |
| s 1202(2) disclosure on request | 16948 | encoded | `s 1202(2) the person has complied with the requirement to give the information on request`; `s 1202(2) the person must give the information to a person who asks` |  |
| s 1202(3) regulations: specified form of notices | 16949 | inert (reason 2: machinery) | - | regulation-making power |
| s 1202(4) negative resolution procedure | 16950 | inert (reason 2: machinery) | - | procedure for regulations |
| s 1203(1) exemption for a partnership of more than 20 persons | 16951-16952 | fork | `s 1203(1) the exemption applies to the document` | fork F26 (an exemption that applies by its own terms) |
| s 1203(2)(a)-(c) the conditions | 16953-16956 | encoded | `s 1203(2) the conditions for the exemption are met` |  |
| s 1203(3) inspection of the list | 16957 | encoded | `s 1203(3) the person may inspect the list` |  |
| s 1203(4) offence | 16958 | encoded | `s 1203(4) the member of the partnership commits an offence` |  |
| s 1203(5) penalty | 16959 | encoded | `s 1203(5) the penalty for an offence under s 1203` |  |
| s 1204(1)(a)-(b) disclosure at business premises | 16960-16964 | fork | `s 1204(1) the requirement to display the notice applies to the premises`; `s 1204(1) the person has complied with the requirement to display the notice`; `s 1204(1) the person must display the notice in the premises` | fork F24 (both limbs of "in any premises" read alike) |
| s 1204(2) regulations: specified form of notices | 16965 | inert (reason 2: machinery) | - | regulation-making power |
| s 1204(3) negative resolution procedure | 16966 | inert (reason 2: machinery) | - | procedure for regulations |
| cross-heading "Consequences of failure to make required disclosure" | 16967 | inert (reason 1: not operative) | - | heading |
| s 1205(1) offence of failure to make required disclosure | 16968-16972 | encoded | `s 1205(1) the person commits an offence` |  |
| s 1205(2) body corporate: officers in default | 16973 | encoded | `s 1205(2) an officer of the body corporate commits an offence` |  |
| s 1205(3) penalty | 16974 | encoded | `s 1205(3) the penalty for an offence under s 1205` |  |
| s 1205(4) the requirements include those of regulations | 16975 | encoded | `s 1205(4) the requirement is a requirement of s 1202 or s 1204` |  |
| s 1206(1) proceedings to which s 1206 applies | 16976-16977 | encoded | `s 1206(1) this section applies to the proceedings` |  |
| s 1206(2)(a)-(b) dismissal unless just and equitable | 16978-16981 | encoded | `s 1206(2) the proceedings shall be dismissed` |  |
| s 1206(3) the requirements include those of regulations | 16982 | encoded | `s 1206(3) the requirement is a requirement of this Chapter` |  |
| s 1206(4) no effect on rights against another person | 16983 | encoded | `s 1206(4) the section affects the right to enforce rights against another person` |  |
| Chapter 3 heading | 16984 | inert (reason 1: not operative) | - | heading |
| s 1207 application of general provisions about offences | 16985-16986 | encoded | `s 1207 the provision applies in relation to the offence` |  |
| s 1208 lead-in "In this Part" | 16987-16988 | inert (reason 1: not operative) | - | lead-in, fork F2 |
| s 1208 "business" | 16989 | encoded | `s 1208 the activity is a business` |  |
| s 1208 "initial" | 16990 | encoded | `s 1208 the abbreviation is an initial` |  |
| s 1208 "partnership" (a)-(b) | 16991-16994 | encoded | `s 1208 the arrangement is a partnership` |  |
| s 1208 "surname" | 16995 | encoded | `s 1208 the surname of the person` |  |

### Audit counts

Text units counted by script over the two ranges (627 lines, 627 non-blank, 10,970 words, the brief's figure): 8 Part and Chapter headings, 18 cross-headings, 62 section headings (ss 1134 to 1157 and 1175 to 1208, with 1196A, 1198A, 1198B and 1199A), 222 subsections, 196 lettered paragraphs, 35 roman paragraphs, 21 quoted defined-term lines, 63 other lines (list items, continuation text, run-in lines) and 2 lines of dots standing alone (ss 1175 and 1189). **Rows in the table: 269 when the skeleton was written (before any L4), 271 at the end**: two merged rows were split (s 1139(4) into the service of process and the copy by post, lines 16265 and 16266; s 1154(3) into the address for service and the notice of a change, lines 16421 and 16422) so that each relation has its own row; no other row was added or removed and no line changed rows; two functions (`s 1198A(5)` and `s 1198B(7)` "company includes an overseas company") were added to existing rows when a re-read found them missing. `work/audit.py` reports "range lines 627, non-blank 627; rows 271; covered 627; missing []; overlapping []; outside []".

## Fork register (coa25)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each. Sites the 2026-11-05 ruling leaves to the encoder carry one line here for the human reviewer to overrule. The rulings of 2026-11-04 and 2026-11-05 are recorded here word for word where this part's `NOTHING-kind` and `FALSE-kind` tags rest on them:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. This part follows option C: each section answers for itself, and the seat layer calls the per-section functions.
- **N2** (does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04.
- **Periods, "where" and scope limits** (2026-11-05): (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z.
- **Delegated definitions, defences and "until" bars** (2026-11-05, approved in the word NOTHINGBURGER): (a) a definition the text itself hands to a list: when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"; (c) "when", "upon" and "whenever" count as "where"; (d) "the property does not pass until X": encode the bar. Typed 2026-11-05T06:04:54.553Z.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings leave open are decided site by site on the text's own words: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line below.

- **F1** (s 1139(2) and (3) (lines 16255-16264); `s 1139(2) first text: ...`, `s 1139(2) second text: ...`, `s 1139(3) first text: ...`, `s 1139(3)(a) second text: ...`, `s 1139(3)(b) second text: ...`): Taken: Both versions are encoded under distinct names; neither overwrites the other; the seat question asks which text to apply ("first text" or "second text"; anything else answers NOTHING). The first text lets service on an overseas company be effected at a resident authorised person's registered address or, if there is no such person (or service fails), at a place of business in the United Kingdom; the second lets it be effected at the company's own registered address (registered under regulations under s 1048A) or at a resident authorised person's registered address. Other reading: One of the two is the text in force and the other is superseded (the text says only that it "may carry more than one extent version", `inputs/SOURCES.md`); a lawyer should say which, and the other pair of functions can then be deleted.
- **F2** (Signposts and lead-ins: s 1139(5), s 1140(7), s 1152(1), s 1182(1), s 1208 "In this Part"): Taken: Inert under reason 1 (not operative): each says only what the section is for or points to another provision (as the keel did, its fork F7). Other reading: Operative scope statements: each would be a function returning `JUST TRUE`.
- **F3** (s 1155(1) "within the period of 14 days after the appointment"; `s 1155(1) the judicial factor commits an offence`): Taken: The period begins on the day after the appointment, so the last day is the day of appointment plus 14: notice on the 14th day after is in time, on the 15th is an offence (tested on 1 June 2026: 15 June in time, 16 June late). "Fails ... within the period": no notice and the 14 days not yet run out answers NOTHING (the failure is not yet made out). Other reading: The day of the appointment counts as day 1, so the last day is the day plus 13.
- **F4** (s 1140(5) "the period of 14 days beginning with the date on which notice of the change is registered"; s 1145(2) "within 21 days of receipt of the request"; s 1199(3) "twelve months beginning with the date of the transfer"): Taken: s 1140(5): the day of registration is day 1, so the last day is that date plus 13 (registered on 10 January: valid on 23 January, not on 24). s 1145(2): the day of receipt is day 0 and the 21st day after it is the last (1 March: 22 March). s 1199(3): see F11. Other reading: s 1140(5): "beginning with" excludes nothing, the other reading counts 14 days after (24 January valid). s 1145(2): the day of receipt is day 1 (21 March the last day).
- **F5** (A bare "must" not done, and "has complied" for a requirement that does not engage: ss 1135(2), 1138(1), 1139(4), 1144, 1150(1) and (4), 1154(3), 1195(2) and (3), 1196(3), 1201(2) and (3), 1202(1) and (2), 1204(1)): Taken: A requirement that engages and is not met answers `JUST FALSE` (a failed duty is a "no"); a requirement that does not engage (the "where" or "if" that would trigger it fails) answers `JUST TRUE` for a "has complied" function, because nothing is left to fail; the matching "the duty applies" function answers `JUST FALSE` under ruling (b). The offence functions read "fails to comply" from the "has complied" answer. Other reading: An unmet bare "must" answers NOTHING (the text does not say what follows); a requirement that does not engage answers NOTHING instead of `JUST TRUE`.
- **F6** ("Unless", "except" and "(other than X)" once met: s 1142 "unless otherwise expressly provided"; s 1156(1) "Except as otherwise provided"; s 1198A(5) and s 1198B(7) "other than a direction under section 76B(1)(b) ..."; s 1206(2) "unless the court ... is satisfied that it is just and equitable"): Taken: s 1142 and s 1156(1): once the exception is met the answer is NOTHING (the other provision decides). s 1198A(5), s 1198B(7): the carved-out direction answers `JUST FALSE` ("means ... other than"). s 1206(2): once the court is satisfied the answer is `JUST FALSE` (not dismissed). Other reading: s 1142 / s 1156(1): `JUST FALSE`. The "other than" carve-out: NOTHING. s 1206(2): NOTHING.
- **F7** (s 1147(2)-(5) hours; `s 1147(5) the instant at which the period of hours ends`, `s 1147(2)`, `(3)`, `(4)`, `s 1147 the day the document is treated as delivered`): Taken: A point in time is a day and an hour of that day (0 to 24); 24:00 is written as 00:00 the next day; hours are counted only on days for which the keel's working-day answer (s 1173(1)) is true, taken as a function-typed input; a search limit of 400 days answers NOTHING if no working day comes. PLAN.md section 4.2 types the answer other parts want as a DATE: `s 1147 the day the document is treated as delivered` is the day of the deemed instant (the text itself gives an instant). Posting on Friday 2 January 2026 at 10:00 reaches Tuesday 6 January 10:00. Other reading: A count of whole days: the Act speaks of hours, so a day count would be wrong for a posting after midnight.
- **F8** (s 1151(1) "only if"; `s 1151(1) the person meets the independence requirement`): Taken: "only if" is read as the complete test: a failed limb answers `JUST FALSE`, and when every limb holds the answer is `JUST TRUE`. The regulations of limb (c) are an input. Other reading: "only if" states necessary conditions: when they hold the text does not say the person meets the requirement (NOTHING).
- **F9** (s 1154(1) and (2); `s 1154(1) notice of the appointment must be given to the registrar`): Taken: Subsection (1) lists three appointments (a judicial factor, an interim manager under s 76 of the Charities Act 2011, a manager under s 47 of the 2004 Act) but (2)(b) and (bb) also name an interim manager under s 33 of the Charities Act (Northern Ireland) 2008 and a receiver or manager under that section: for those the duty of (1) answers NOTHING, and `s 1154(2)` still says who gives the notice (finding 2). Other reading: The duty of (1) covers the Northern Ireland appointments too (an omission in (1)): `JUST TRUE`.
- **F10** (s 1184(3) "(a “disqualification undertaking”)"): Taken: The parenthetical defines the term: an undertaking accepted by the Secretary of State under the regulations, from a person subject to foreign restrictions, not to do anything in breach of a disqualification, is one; any other is not (`JUST FALSE`). Other reading: The sentence is a description of what the regulations may provide, not a definition: NOTHING.
- **F11** (s 1199(3) "twelve months beginning with the date of the transfer"; `s 1199(3) ...`): Taken: The first day is the date of the transfer and the period ends on the day before the same date a year later (transfer 15 March 2026: last day 14 March 2027; transfer 31 January 2026: last day 30 January 2027), computed with the library's `add months`, which clamps a day that does not exist, so a transfer on 29 February is not tested. Other reading: The period ends on the anniversary date.
- **F12** (s 1200(1) second sentence; `s 1200(1) the person is a person to whom this Chapter applies`): Taken: "References in this Chapter to “a person to whom this Chapter applies” are to such an individual or partnership" defines the expression: another kind of person (a company) answers `JUST FALSE`. Other reading: The first sentence is a scope limit with no "only": NOTHING (the 2026-11-05 ruling, (c)).
- **F13** (s 1152(6) "in relation to a limited liability partnership, for “director” read “member”"): Taken: Carried by limited-liability-partnership constructors in the relationship types of s 1152(2), (3) and (4): an LLP of which the person is a member takes the place of a body corporate of which the person is a director. Other reading: A flag on each function.
- **F14** (Lists of scope not closed with "only": s 1140(2), s 1149, s 1154(1) and (2), s 1202(1), s 1207, s 1199(1)): Taken: A case outside the list answers NOTHING (list not closed). Other reading: `JUST FALSE` for any case outside the list.
- **F15** (Closed definitions: s 1136(2) "The relevant provisions are", s 1152 "associate ... means", s 1192(3) and s 1200(3) "The following are the permitted additions", s 1193(2) "local authority means", s 1182(3), s 1201(1), s 1208 "partnership means"): Taken: Definitions by "means", "are" or "are to" are closed (ruling (a) of 2026-11-05): a case outside the list answers `JUST FALSE`. Other reading: NOTHING where the text does not say "only".
- **F16** (Borrowed definitions: s 1181(4) "RTE companies", "RTM companies"; s 1193(2) "a local authority within the meaning of the Local Government Act 1972"): Taken: s 1181(4) is a `MAYBE BOOLEAN` input passed through (`JUST FALSE` is the other Act's no, supplied by the caller). For the Local Government Act 1972 limb the person states which description fits the body (a constructor), not the borrowed meaning. Other reading: Every borrowed term answers NOTHING always.
- **F17** (Offences: "A person who contravenes this section commits an offence" (ss 1193(4), 1194(3), 1196A(2), 1197(5), 1198(2)), "If a company fails to comply ... an offence is committed by every officer ... who is in default" (ss 1135(3), 1138(2), 1145(4)), "Where an offence ... is committed by a body corporate, an offence is also committed by every officer of the body who is in default" (ss 1193(5) ...)): Taken: No contravention (or a company that complied) answers `JUST FALSE` (the offence is defined by the contravention; an "if" or "where" not met); an officer not in default answers NOTHING ("every officer ... who is in default" is a named complement); an officer in default of a failure answers `JUST TRUE`. s 1121 is an input. Other reading: No contravention answers NOTHING ("who" is not "if"); an officer not in default answers `JUST FALSE`.
- **F18** (Permissions limited by their own wording: s 1135(1)(b), s 1139(1), (2), (4), s 1150(2), s 1153(1), s 1154(3), s 1203(3)): Taken: The case outside the limit answers NOTHING (the 2026-11-04 ruling on prohibitions and grants limited by their own wording). Other reading: `JUST FALSE`.
- **F19** (s 1157(1) "If in proceedings for negligence, default, breach of duty or breach of trust ... it appears to the court hearing the case that the officer or person is or may be liable but that he acted honestly and reasonably ..., the court may relieve him"; `s 1157(1) the court may relieve the defendant from liability`): Taken: The judgment the text hands to the court is a plain input. A power whose "if" gate is unmet answers NOTHING (Guide section 5, "In short": a grant limited by its own wording, the case outside the limit): `JUST FALSE` would read as "the court may not". `JUST TRUE` says the power exists, not that it will be exercised. `s 1157(2)(b)` passes the answer through. Other reading: `JUST FALSE` for an unmet "if" (marginal reading (a): the text's own no).
- **F20** (ss 1186(2)-(3) and 1191(2)-(3): the ceilings on the penalties the regulations may provide): Taken: Encoded although the sections are powers: the ceiling is what the text itself fixes; "the general limit in a magistrates' court" is an input; an offence committed before 2 May 2022 is six months in England and Wales (tested on 1 May and 2 May 2022). The powers themselves are inert, reason 2. Other reading: Inert, reason 2, with the ceilings not encoded.
- **F21** (The seat for Chapter 2 of Part 41 (see "Seat")): Taken: An individual or partner who carries on the business, and a customer or supplier who deals with it (assumed, not ruled). Other reading: No seat for Chapter 2, because the Chapter is not addressed to companies.
- **F22** (s 1202(2) "immediately"): Taken: "Immediately" is a plain fact ("was the information given immediately?"); no `WITHIN` is invented. The regulative rules carry no time limit where the text gives none. Other reading: A deadline of zero days.
- **F23** (Seat inputs that answer two limbs: `Under section 1193(1)` and `Under section 1196A(1)`): Taken: One input answers both limbs of s 1199(2) ("carried on ... before" and "continues ... under its lawful business name"), and one input (a written notice) answers the s 1199A(1) conditions on the assumption that a notice is given only when the Secretary of State was satisfied of the national security or serious crime ground (assumed, not ruled). Other reading: Ask the three s 1199A(1) facts separately; the layer-1 function already does.
- **F24** (s 1204(1) "in any premises— (a) where the business is carried on, and (b) to which customers of the business or suppliers of goods or services to the business have access"; `s 1204(1) the requirement to display the notice applies to the premises`): Taken: The function asks the provision's own question (does the requirement apply to these premises?), so a failed condition of either limb answers `JUST FALSE`: ruling (b) of 2026-11-05 for the "where" of limb (a), and limb (b) is read alike because it is a condition of the same "in any premises" clause (the limbs are not split by the word that introduces each, which would give two conditions of one conjunction different answers). The "has complied" function then answers `JUST TRUE` for such premises (nothing is left to fail), and s 1205(1) answers `JUST FALSE` when the other duties are met. Other reading: Limb (b) is a scope limit with no "only" (ruling (c) of 2026-11-05): premises to which no customer or supplier has access answer NOTHING, so "has complied" answers NOTHING and s 1205(1) answers NOTHING (when the other duties are met).
- **F25** (s 1199A(1) "The Secretary of State may, by written notice given to a person, provide that a prohibition ... does not apply ..., if satisfied that to do so is necessary— (a) in the interests of national security, or (b) for the purposes of preventing or detecting serious crime"; `s 1199A(1) the prohibitions of this Chapter do not apply to the business under the name`): Taken: The function states the effect of a power the Secretary of State may exercise, and asks for the notice and for the Secretary of State's own satisfaction. When the notice was not given, or the Secretary of State is satisfied of neither ground, it answers NOTHING: `JUST FALSE` would say that the prohibitions DO apply to the business under the name, which s 1199A(1) never says (it only lifts a prohibition by notice; whether a prohibition applies is decided by the section that imposes it, and by s 1199). The callers (ss 1193(1), 1194(1), 1196A(1), 1197(5), 1198(1), 1198A(1), 1198B(1)) test only for `JUST TRUE`, so they do not depend on which of the two it is. Other reading: `JUST FALSE` for a grant with an unmet "if" (a condition the text introduces with "if" is the text's own no: Guide section 5), the answer given to the unmet "if" of `s 1203(1)` (fork F26).
- **F26** (s 1203(1) "Section 1202(1) ... does not apply in relation to a document issued by a partnership of more than 20 persons if the following conditions are met"; `s 1203(1) the exemption applies to the document`): Taken: The function asks whether the exemption applies, which is the provision's own question, and the exemption works by its own terms with no one's act: conditions unmet answers `JUST FALSE` (an "if" unmet), and the requirement of s 1202(1) stays in force for the document, which s 1202(1) itself says; a partnership of 20 persons or fewer answers NOTHING (a scope limit with no "only", ruling (c) of 2026-11-05). Other reading: NOTHING when the conditions are unmet (an exemption limited by its own wording), as `s 1199A(1)` is answered (fork F25); or `JUST FALSE` for 20 persons or fewer.
- **F27** (s 1157(3) "the judge, after hearing the evidence, may, if he is satisfied that the defendant ... ought ... to be relieved either in whole or in part"; `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant`): Taken: When the judge is not satisfied the answer is NOTHING (a power whose "if" gate is unmet; `JUST FALSE` would read as "the judge may not"). The two "Where" limbs of the same subsection answer differently and are listed in F30. Other reading: `JUST FALSE` for an unmet "if" (marginal reading (a)).
- **F28** (s 1196(2) "If it appears to the Secretary of State that there are overriding considerations of public policy that require such approval to be withdrawn, the approval may be withdrawn by notice in writing"; `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned`): Taken: When it does not appear to the Secretary of State that overriding considerations require the withdrawal the answer is NOTHING (a power whose "if" gate is unmet); an approval other than one given for s 1193 or s 1194 is also NOTHING (limited by its own wording). Other reading: `JUST FALSE` for an unmet "if" (marginal reading (a)).
- **F29** (LISTED, not decided (name-test sweep: "may" with a "provided" gate): `s 1135(1) the company may keep its records in this way`): Taken: Answers `JUST FALSE` when "provided the information in question is adequately recorded for future reference" is not met. ASSUMED, NOT RULED: "provided" goes with the equivalents of "where", "when" and "upon" ("so long as"). Ruling (b) of the Guide's "Periods, where and scope limits" paragraph (and ruling (c) of the 2026-11-05 delegated ruling) says `JUST FALSE`, and the Guide's line on grants points the other way, so this is a question for the maintainer or a lawyer. Other reading: NOTHING (a grant limited by its own wording).
- **F30** (LISTED, not decided (name-test sweep: "may" with a "where" gate): `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant`, the two "Where" limbs): Taken: Answers `JUST FALSE` when "Where a case to which subsection (1) applies is being tried by a judge with a jury" is not met (no jury, or not a case to which subsection (1) applies). ASSUMED, NOT RULED: this is the group of "may" functions whose gate is "where", "when" or "upon"; ruling (b) of the Guide's "Periods, where and scope limits" paragraph says `JUST FALSE`, and the Guide's line on grants points the other way, so this is a question for the maintainer or a lawyer. Other reading: NOTHING (a grant limited by its own wording).
- **F31** (LISTED, not decided (name-test sweep: "may" with a "where" gate): `s 1203(3) the person may inspect the list`): Taken: Answers `JUST FALSE` when "Where a partnership maintains a list of the partners' names for the purposes of this section" is not met; an inspection outside office hours answers NOTHING. ASSUMED, NOT RULED: this is the group of "may" functions whose gate is "where", "when" or "upon"; ruling (b) of the Guide's "Periods, where and scope limits" paragraph says `JUST FALSE`, and the Guide's line on grants points the other way, so this is a question for the maintainer or a lawyer. Other reading: NOTHING for the unmet "Where" as well.
- **F32** (LISTED, not decided (name-test sweep: "entitled"): `s 1145(1) the person is entitled to require the company to send a hard copy version`): Taken: Answers `JUST FALSE` when the member or debenture holder received the document in hard copy ("Where ... has received a document or information from the company otherwise than in hard copy form" is not met), and NOTHING for a person who is neither. An entitlement is a claim, not a power, and the Guide does not settle it. Other reading: NOTHING for the unmet "Where".
- **F33** (LISTED, not decided (name-test sweep: "entitled"): `s 1153(1) the person is entitled to require the information and explanation from the officers of the company`): Taken: Answers NOTHING when the person is not carrying out a valuation or making a report, or the information is not such as the person thinks necessary. An entitlement is a claim, not a power, and the Guide does not settle it. Other reading: `JUST FALSE` for an unmet condition.

### Name-test sweep of 2026-11-12

Nineteen layer-1 functions have a name containing "may", "permitted", "power", "entitled" or "authorised". Each was tested as follows. A function named for a grant or a power that answered `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar, so it answers NOTHING (Guide section 5, "In short"). A gate the text closes itself ("may not", "must", a closed definition), a bar, a duty or the provision's own question keeps `JUST FALSE`. A "may" function whose gate is "where", "when", "upon" or an equivalent, and every "entitled" function, are listed in the fork register above (F29 to F33) and not decided.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 3 | 6 | 3 | 2 |

- **Flipped to NOTHING (3):** `s 1157(1) the court may relieve the defendant from liability` (F19); `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant`, its "if" limb only (F27); `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned` (F28).
- **Kept `JUST FALSE` (6):** `s 1140(6) service may be effected by virtue of s 1140 at the address` (the text says "may not ... if": a bar); `s 1145(3) the company may make a charge for providing the hard copy version` (the text says "may not": a flat bar); `s 1150(1) the person may make the valuation and report` ("must be made by a person who": a requirement, not a grant); `s 1192(3) the addition is a permitted addition` and `s 1200(3) the addition is a permitted addition` ("The following are the permitted additions": a definition, not a grant); `s 1157(2)(b) the court has the same power to relieve the applicant` (no gate of its own: it passes the s 1157(1) answer through).
- **Listed: "may" with where/when/upon (3):** `s 1135(1) the company may keep its records in this way` (F29, "provided"); `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant`, the two "Where" limbs (F30); `s 1203(3) the person may inspect the list` (F31, "Where a partnership maintains a list").
- **Listed: "entitled" (2):** `s 1145(1) the person is entitled to require the company to send a hard copy version` (F32); `s 1153(1) the person is entitled to require the information and explanation from the officers of the company` (F33).
- **Scanned, in none of the four columns:** `s 1150(2)`, `s 1154(3)`, `s 1157(2)(a)` and `s 1195(4)` already answer NOTHING when their gate fails; `s 1186(2)` and `s 1191(2)` return a ceiling on a penalty, not a yes or no.

## Jural relations (coa25)

Hohfeld's correlatives, stated once per provision as a relation between two parties and named neutrally (a right is a claim against a duty; a privilege is a liberty against a no-right; a power is against a liability, that is, being subject to the power; an immunity is against a disability). A provision that creates no relation (a definition, a counting rule, a signpost, a regulation-making power) is listed as `none`. Where the text names only one side, the other is said to be unnamed. The Crown is not named in the text; the offence rows name it as the holder of the claim that the offence be punished, and no seat is ever the Crown.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| Part 37 heading | none | none | (inert) |
| cross-heading "Company records" | none | none | (inert) |
| s 1134 "company records", (a)-(b) | none | none | `s 1134 the document is a company record` |
| s 1135(1)(a)-(b) and proviso: form and arrangement of company records | the company: a PRIVILEGE to keep its records in hard copy or electronic form, arranged as its directors think fit | no one is named (the correlative no-right of anyone who would require otherwise) | `s 1135(1) the company may keep its records in this way`; `s 1135 the company has complied with this section` |
| s 1135(2) electronic records reproducible in hard copy | the text names no holder of the correlative claim | the company: a DUTY | `s 1135(2) the requirement of reproduction in hard copy form applies`; `s 1135(2) the company has met the requirement of reproduction in hard copy form`; `s 1135 the company has complied with this section`; `s 1135(2) the company must keep electronic records capable of reproduction in hard copy form` |
| s 1135(3) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1135(3) an officer of the company commits an offence` |
| s 1135(4) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1135(4) the penalty for an offence under s 1135` |
| s 1135(5) pre-1979 instruments requiring a hard copy debenture register | the company: an IMMUNITY (its pre-1979 instrument is read as allowing electronic form) | no one is named (DISABILITY) | `s 1135(5) the instrument's requirement is to be read as requiring hard copy or electronic form` |
| s 1136(1) regulations about where certain records are kept | none | none | (inert) |
| s 1136(2) the "relevant provisions": lead-in and s 114 | none | none | `s 1136(2) the provision is a relevant provision` |
| s 1136(2) two entries shown as dots | none | none | (repealed or blank) |
| s 1136(2) ss 228 and 237 | none | none | `s 1136(2) the provision is a relevant provision` |
| s 1136(2) one entry shown as dots | none | none | (repealed or blank) |
| s 1136(2) ss 358, 702, 720, 743 | none | none | `s 1136(2) the provision is a relevant provision` |
| s 1136(2) two entries shown as dots | none | none | (repealed or blank) |
| s 1136(2) ss 805, 809, 859Q | none | none | `s 1136(2) the provision is a relevant provision` |
| s 1136(3) what the regulations may specify | none | none | (inert) |
| s 1136(4) conditions the regulations may impose | none | none | (inert) |
| s 1136(5)(a)-(b) the regulations need not / may specify places | none | none | (inert) |
| s 1136(6) all the records must be kept at the specified place | the person entitled to inspection: a CLAIM that all the records be kept at the specified place | the company: a DUTY (a condition of compliance) | `s 1136(6) keeping the records available for inspection at the place complies with the requirement` |
| s 1136(7) negative resolution procedure | none | none | (inert) |
| s 1137(1)(a)-(b) regulations about inspection and copies | none | none | (inert) |
| s 1137(2) failure to comply with the regulations treated as refusal | the person entitled to inspection or copies: a CLAIM | the company: LIABILITY to be treated as having refused or failed | `s 1137(2) the company is treated as having refused or failed` |
| s 1137(3)(a)-(b) what the regulations may provide | none | none | (inert) |
| s 1137(4) fees | none | none | (inert) |
| s 1137(5)(a)-(b) a company may give more or charge less | the company: a PRIVILEGE (to give more, or charge less) | no one is named (no-right) | `s 1137(5)(a) the company is prevented from affording more extensive facilities than the regulations require`; `s 1137(5)(b) the company is prevented from charging a lesser fee or none at all` |
| s 1137(6) negative resolution procedure | none | none | (inert) |
| s 1138(1)(a)-(b) precautions against falsification | the text names no holder of the correlative claim | the company: a DUTY | `s 1138(1) the duty to take precautions applies to the records`; `s 1138 the company has complied with this section`; `s 1138(1) the company must take adequate precautions against falsification` |
| s 1138(2) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1138(2) an officer of the company commits an offence` |
| s 1138(3) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1138(3) the penalty for an offence under s 1138` |
| s 1138(4)(a)-(b) records under s 228 and s 237 excepted | the company: an IMMUNITY from s 1138 for ss 228 and 237 documents | no one is named (DISABILITY) | `s 1138(4) this section applies to the company record` |
| cross-heading "Service addresses" | none | none | (inert) |
| s 1139(1) service on a company registered under this Act | the person serving: a POWER to serve by the stated ways | the company: LIABILITY to be served | `s 1139(1) service of the document on the company is effected` |
| s 1139(2)(a)-(b) service on an overseas company, FIRST text | the person serving: a POWER to serve by the stated ways | the company: LIABILITY to be served | `s 1139(2) first text: service of the document on the overseas company is effected` |
| s 1139(3) "registered address", FIRST text | none | none | `s 1139(3) first text: the address is the person's registered address` |
| s 1139(2)(a)-(b) service on an overseas company, SECOND text | the person serving: a POWER to serve by the stated ways | the company: LIABILITY to be served | `s 1139(2) second text: service of the document on the overseas company is effected` |
| s 1139(3)(a)-(b) "registered address", SECOND text | none | none | `s 1139(3)(a) second text: the address is the registered address of the overseas company`; `s 1139(3)(b) second text: the address is the registered address of a person other than the overseas company` |
| s 1139(4) process on a company registered in Scotland or Northern Ireland carrying on business in England and Wales | the person serving: a POWER to serve by the stated ways | the company: LIABILITY to be served | `s 1139(4) service of the process on the company is effected` |
| s 1139(4) the person issuing out the process must send a copy by post to the registered office | the company: a CLAIM to a copy by post at its registered office | the person issuing out the process: a DUTY | `s 1139(4) the duty to send a copy of the process to the registered office applies`; `s 1139(4) the person issuing out the process has complied with the duty to send a copy`; `s 1139(4) the person issuing out the process must send a copy to the registered office` |
| s 1139(5) further provision in the company communications provisions | none | none | (inert) |
| s 1140(1) service on a director, secretary or other person to whom the section applies | the person serving: a POWER to serve at the registered address (and, for 14 days, the previous one) | the director, secretary or other registered person: LIABILITY to be served | `s 1140(1) service of the document on the person is effected` |
| s 1140(2)(a)-(c) persons to whom s 1140 applies | none | none | `s 1140(2) the section applies to the person` |
| s 1140(3) applies whatever the purpose of the document | none | none | `s 1140(3) the section applies to the document` |
| s 1140(4) "registered address" | none | none | `s 1140(4) the address is the person's registered address` |
| s 1140(5) a change of address: 14 days | the person serving: a POWER to serve at the registered address (and, for 14 days, the previous one) | the director, secretary or other registered person: LIABILITY to be served | `s 1140(5) the document is validly served at the address previously registered` |
| s 1140(6)(a)-(b) when service may not be effected | the director, secretary or other registered person: an IMMUNITY from service at the stated addresses | the person serving: a DISABILITY | `s 1140(6) service may be effected by virtue of s 1140 at the address` |
| s 1140(7) further provision in the company communications provisions | none | none | (inert) |
| s 1140(8) no effect on permission for service out of the jurisdiction | the person who needs permission: no change to the claim | no one is named | `s 1140(8) the section affects the requirement of permission for service out of the jurisdiction` |
| s 1141(1) "service address" | none | none | `s 1141 the address is a service address` |
| s 1141(2) regulations specifying conditions | none | none | (inert) |
| s 1141(3) negative resolution procedure | none | none | (inert) |
| s 1142 an obligation to give an address is to give a service address | none | none | `s 1142 the address to be given is a service address` |
| cross-heading "Sending or supplying documents or information" | none | none | (inert) |
| s 1143(1) the company communications provisions | none | none | `s 1143(1) the provision is one of the company communications provisions`; `s 1143(1) the company communications provisions have effect for the purposes of the provision` |
| s 1143(2) subject to contrary provision | none | none | `s 1143(2) the company communications provisions yield to the other provision` |
| s 1143(3) subject to Part 35 for documents sent to the registrar | none | none | `s 1143(3) the company communications provisions yield to Part 35` |
| s 1143(4) express authority to use a form is not contrary provision | none | none | `s 1143(4) the provision is regarded as contrary to the company communications provisions` |
| s 1144(1) documents to a company: Schedule 4 | the recipient (a company, or the person a company writes to): a CLAIM that the communication follow the Schedule | the sender: a DUTY | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |
| s 1144(2) documents by a company: Schedule 5 | the recipient (a company, or the person a company writes to): a CLAIM that the communication follow the Schedule | the sender: a DUTY | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |
| s 1144(3) company to company: Schedule 5 only | the recipient (a company, or the person a company writes to): a CLAIM that the communication follow the Schedule | the sender: a DUTY | `s 1144 the Schedule that governs the communication`; `s 1144 the document or information has been sent or supplied` |
| s 1145(1) right to a hard copy version | the member or debenture holder: a POWER to require a hard copy | the company: LIABILITY to be so required | `s 1145(1) the person is entitled to require the company to send a hard copy version`; `s 1145 the company has complied with this section` |
| s 1145(2) the company must send it within 21 days | the member or debenture holder: a CLAIM to the hard copy within 21 days | the company: a DUTY | `s 1145(2) the last day for sending the hard copy version`; `s 1145(2) the company sent the hard copy version in time`; `s 1145 the company has complied with this section`; `s 1145(2) the company must send the hard copy version within 21 days` |
| s 1145(3) no charge | the member or debenture holder: an IMMUNITY from any charge | the company: a DISABILITY | `s 1145(3) the company may make a charge for providing the hard copy version`; `s 1145 the company has complied with this section` |
| s 1145(4) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1145(4) the company commits an offence`; `s 1145(4) an officer of the company commits an offence` |
| s 1145(5) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1145(5) the penalty for an offence under s 1145` |
| s 1146(1) authentication: application | none | none | `s 1146(1) the section applies to the authentication of the document or information` |
| s 1146(2) hard copy sufficiently authenticated if signed | the sender to the company: a POWER to authenticate by signature or by the stated means | the company: LIABILITY to treat the document as authenticated | `s 1146(2) the hard copy document or information is sufficiently authenticated` |
| s 1146(3)(a)-(b) electronic form sufficiently authenticated | the sender to the company: a POWER to authenticate by signature or by the stated means | the company: LIABILITY to treat the document as authenticated | `s 1146(3) the electronic document or information is sufficiently authenticated` |
| s 1146(4) authority to act on behalf of another | the company: a PRIVILEGE to require evidence of authority under its articles | the sender on behalf of another: no-right | `s 1146(4) the section affects the provision of the articles requiring evidence of authority` |
| s 1147(1) deemed delivery: application | none | none | `s 1147 the day the document is treated as delivered` |
| s 1147(2)(a)-(b) by post: 48 hours | the company that sends: a POWER to have delivery deemed after 48 hours (or on the website rules) | the intended recipient: LIABILITY to be treated as having received it | `s 1147(2) the instant at which the document or information is deemed received by post` |
| s 1147(3)(a)-(b) by electronic means: 48 hours | the company that sends: a POWER to have delivery deemed after 48 hours (or on the website rules) | the intended recipient: LIABILITY to be treated as having received it | `s 1147(3) the instant at which the document or information is deemed received by electronic means` |
| s 1147(4)(a)-(b) by means of a website | the company that sends: a POWER to have delivery deemed after 48 hours (or on the website rules) | the intended recipient: LIABILITY to be treated as having received it | `s 1147(4) the instant at which the document or information is deemed received by means of a website` |
| s 1147(5) hours counted only over working days | none | none | `s 1147(5) count the hours from the instant over working days only`; `s 1147(5) the instant at which the period of hours ends` |
| s 1147(6)(a)-(c) subject to articles, instrument, agreement | the company, member, debenture holder or other person: a POWER to contract out by articles, instrument or agreement | the other party: LIABILITY | `s 1147(6) the deeming rules yield to the contrary provision` |
| s 1148(1) "address", "company", "document" | none | none | `s 1148(1) the thing is an address`; `s 1148(1) the body is a company`; `s 1148(1) the thing is a document` |
| s 1148(2) references to provisions authorising or requiring | none | none | `s 1148(2) the reference includes the provision, whatever expression is used` |
| s 1148(3) by or to the directors on behalf of the company | none | none | `s 1148(3) the reference to sending or supplying by or to a company includes the case` |
| cross-heading "Requirements as to independent valuation" | none | none | (inert) |
| s 1149 which valuations ss 1150 to 1153 apply to | none | none | `s 1149 sections 1150 to 1153 apply to the valuation and report` |
| s 1150(1)(a)-(b) the valuer | the valuer: a POWER to arrange for or accept another person's valuation, if qualified and independent | no one is named | `s 1150(1) the person may make the valuation and report` |
| s 1150(2)(a)-(b)(i)-(ii) another person may value | the valuer: a POWER to arrange for or accept another person's valuation, if qualified and independent | no one is named | `s 1150(2) the valuer may arrange for or accept a valuation made by the other person` |
| s 1150(3) "officer or employee" does not include an auditor | none | none | `s 1150(3) the person counts as an officer or employee for subsection (2)(b)` |
| s 1150(4)(a)-(b) the valuer's report where another person values | the persons relying on the report (not named): a CLAIM that the report give the stated particulars | the valuer: a DUTY | `s 1150(4) the requirement as to the valuer's report applies`; `s 1150(4) the valuer's report contains what is required`; `s 1150(4) the valuer must state in the report what is required` |
| s 1151(1)(a)-(c) the independence requirement | none | none | `s 1151(1) the person meets the independence requirement` |
| s 1151(2) an auditor is not an officer or employee | none | none | `s 1151(2) the person is regarded as an officer or employee of the company for the independence requirement` |
| s 1151(3) "associated undertaking" and "associate" | none | none | `s 1151(3) the undertaking is an associated undertaking of the company` |
| s 1151(4) negative resolution procedure | none | none | (inert) |
| s 1152(1) this section defines "associate" | none | none | (inert) |
| s 1152(2)(a)-(c) associate of an individual | none | none | `s 1152(2) the other person is an associate of the individual` |
| s 1152(3)(a)-(c) associate of a body corporate | none | none | `s 1152(3) the other person is an associate of the body corporate` |
| s 1152(4)(a)-(c) associate of a partnership that is a legal person | none | none | `s 1152(4) the other person is an associate of the partnership that is a legal person` |
| s 1152(5) associate of a partnership that is not a legal person | none | none | `s 1152(5) the other person is an associate of the partnership that is not a legal person` |
| s 1152(6) limited liability partnership: for "director" read "member" | none | none | `s 1152(2) the other person is an associate of the individual`; `s 1152(3) the other person is an associate of the body corporate`; `s 1152(4) the other person is an associate of the partnership that is a legal person` |
| s 1153(1)(a)-(b) valuer entitled to information and explanation | the valuer: a CLAIM to the information and explanation he thinks necessary | the officers of the company: a DUTY (the correlative of the claim; the text states the claim only) | `s 1153(1) the person is entitled to require the information and explanation from the officers of the company` |
| s 1153(2) offence: misleading, false or deceptive statement | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1153(2) the person commits an offence` |
| s 1153(3)(a)-(b) the statement to which (2) applies | none | none | `s 1153(3) the statement is one to which subsection (2) applies` |
| s 1153(4)(a)-(b)(i)-(ii) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1153(4) the penalty for an offence under s 1153(2)` |
| cross-heading "Notice of appointment of certain officers" | none | none | (inert) |
| s 1154(1)(a)-(c) notice of appointment to the registrar | the registrar: a CLAIM to notice of the appointment and its termination | the person specified in (2) (judicial factor, Charity Commission, Charity Commission for Northern Ireland, Regulator of Community Interest Companies): a DUTY | `s 1154(1) notice of the appointment must be given to the registrar` |
| s 1154(2)(a)-(c) who gives the notice | the registrar: a CLAIM to notice of the appointment and its termination | the person specified in (2) (judicial factor, Charity Commission, Charity Commission for Northern Ireland, Regulator of Community Interest Companies): a DUTY | `s 1154(2) the person who must give the notice` |
| s 1154(3) the notice must specify an address for service | the registrar: a CLAIM that the notice specify an address at which service of documents may be effected on the person appointed | the person specified in (2): a DUTY | `s 1154(3) the notice meets the requirement as to the address for service` |
| s 1154(3) notice of a change in the address for service may be given by the person appointed | the person appointed: a POWER to give notice of a change in the address for service | the registrar: LIABILITY to receive it | `s 1154(3) the person may give the registrar notice of a change in the address for service` |
| s 1154(4) notice of termination | the registrar: a CLAIM to notice of the appointment and its termination | the person specified in (2) (judicial factor, Charity Commission, Charity Commission for Northern Ireland, Regulator of Community Interest Companies): a DUTY | `s 1154(4) notice of the termination of the appointment must be given to the registrar` |
| s 1155(1) offence: judicial factor fails to give notice within 14 days | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1155(1) the judicial factor commits an offence`; `s 1155(1) the judicial factor must give the registrar notice within 14 days` |
| s 1155(2) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1155(2) the penalty for an offence under s 1155` |
| cross-heading "Courts and legal proceedings" | none | none | (inert) |
| s 1156(1)(a)-(c) "the court" | none | none | `s 1156(1) the courts that are "the court" in the part of the United Kingdom`; `s 1156(1) the tribunal is the court` |
| s 1156(2) subject to allocation of jurisdiction | none | none | `s 1156(2) the jurisdiction conferred on the court yields to the allocation of jurisdiction` |
| s 1156(3) shown as dots | none | none | (repealed or blank) |
| s 1156(4) shown as dots | none | none | (repealed or blank) |
| s 1157(1) the court's power to relieve | the officer or auditor sued: a favourable LIABILITY (the court may relieve him) | the court: a POWER to relieve | `s 1157(1) the court may relieve the defendant from liability` |
| s 1157(2)(a)-(b) application for relief in anticipation | the officer or auditor who fears a claim: a POWER to apply for relief | the court: LIABILITY to be applied to, with the same power | `s 1157(2)(a) the person may apply to the court for relief`; `s 1157(2)(b) the court has the same power to relieve the applicant` |
| s 1157(3) judge withdraws the case from the jury | the defendant: a favourable LIABILITY (judgment may be directed for him) | the judge: a POWER to withdraw the case from the jury | `s 1157(3) the judge may withdraw the case from the jury and direct judgment for the defendant` |
| Part 39 heading | none | none | (inert) |
| s 1175 heading and body shown as dots | none | none | (repealed or blank) |
| s 1176(1) s 438 of the 1985 Act ceases to have effect | none | none | (inert) |
| s 1176(2)(a)-(c) amendments of s 439 of the 1985 Act | none | none | (inert) |
| s 1176(3) amendment of s 453(1A) of the 1985 Act | none | none | (inert) |
| s 1176(4) saving for proceedings begun before commencement | none | none | (inert) |
| s 1177 repeal of provisions of Part 10 of the 1985 Act | none | none | (inert) |
| s 1178 repeal of s 720 of the 1985 Act and Schedule 23 | none | none | (inert) |
| s 1179 repeal of s 729 of the 1985 Act | none | none | (inert) |
| s 1180 repeal of Part 4 of the Companies Act 1989 | none | none | (inert) |
| s 1181(1)(a)-(b) order amending the 1993 and 2002 Acts | none | none | (inert) |
| s 1181(2) what the references include | none | none | (inert) |
| s 1181(3) negative resolution procedure | none | none | (inert) |
| s 1181(4) "RTE companies" and "RTM companies" | none | none | `s 1181(4) the company is an RTE company`; `s 1181(4) the company is an RTM company` |
| Part 40 heading | none | none | (inert) |
| cross-heading "Introductory" | none | none | (inert) |
| s 1182(1) this section defines "subject to foreign restrictions" | none | none | (inert) |
| s 1182(2)(a)-(c)(i)-(ii) subject to foreign restrictions | none | none | `s 1182(2) the person is subject to foreign restrictions` |
| s 1182(3)(a)-(c) acting in connection with the affairs of a company | none | none | `s 1182(3) the activity is acting in connection with the affairs of a company` |
| s 1182(4)(a)-(b) "company", "director", "receiver" | none | none | `s 1182(4)(a) the body is a company for the purposes of s 1182`; `s 1182(4)(b) the person is a director of the company`; `s 1182(4)(b) the officer is a receiver of the company` |
| s 1183 "the court" and "UK company" | none | none | `s 1183 the courts that are "the court" in Part 40 for the part of the United Kingdom`; `s 1183 the tribunal is the court`; `s 1183 the company is a UK company` |
| cross-heading "Power to disqualify" | none | none | (inert) |
| s 1184(1)(a)-(c) regulations disqualifying a person | none | none | (inert) |
| s 1184(2)(a)-(b) automatic or by order of the court | none | none | (inert) |
| s 1184(3) disqualification undertaking | none | none | `s 1184(3) the undertaking is a disqualification undertaking` |
| s 1184(4)(a)-(b) "person disqualified under this Part", breach | none | none | `s 1184(4)(a) the person is a person disqualified under this Part`; `s 1184(4)(b) the act is a breach of a disqualification` |
| s 1184(5) applications for permission to act | none | none | (inert) |
| s 1184(6) the regulations must provide for ceasing to be disqualified | none | none | (inert) |
| s 1184(7) affirmative resolution procedure | none | none | (inert) |
| s 1185(1)(a)-(c) different provision for different cases | none | none | (inert) |
| s 1185(2)(a)-(b) applications to the court | none | none | (inert) |
| s 1185(3)(a)-(d) factors | none | none | (inert) |
| s 1185(4) undertakings given to the Secretary of State | none | none | (inert) |
| s 1185(5)(a)-(b) Secretary of State represented at hearing | none | none | (inert) |
| s 1186(1) regulations may create an offence of breach | none | none | (inert) |
| s 1186(2)(a)-(b)(i)-(ii) the ceiling on penalties | none | none | `s 1186(2) the greatest penalty that the regulations may provide` |
| s 1186(3) offences before 2 May 2022 | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1186(2) the greatest penalty that the regulations may provide` |
| cross-heading "Power to make persons liable for company's debts" | none | none | (inert) |
| s 1187(1)(a)-(b) regulations making a person personally responsible | none | none | (inert) |
| s 1187(2)(a)-(b) joint and several liability | the creditors of the company (not named): a CLAIM against the person and the company jointly and severally | the person made personally responsible: a DUTY (joint and several) | `s 1187(2) the person is jointly and severally liable with the other` |
| s 1187(3) "involved in the management" | none | none | `s 1187(3) the person is involved in the management of the company` |
| s 1187(4)(a)-(c) different provision for different cases | none | none | (inert) |
| s 1187(5) affirmative resolution procedure | none | none | (inert) |
| cross-heading "Power to require statements to be sent to the registrar of companies" | none | none | (inert) |
| s 1188(1)(a)-(b) regulations requiring a statement | none | none | (inert) |
| s 1188(2)(a)-(b) content of the statement | none | none | (inert) |
| s 1188(3) time for the statement | none | none | (inert) |
| s 1188(4)(a)-(c) different provision for different cases | none | none | (inert) |
| s 1188(5) affirmative resolution procedure | none | none | (inert) |
| s 1189 heading and body shown as dots | none | none | (repealed or blank) |
| s 1190(1) statements treated as records relating to a company | none | none | (inert) |
| s 1190(2)(a)-(b) public inspection and removal | none | none | (inert) |
| s 1190(3) conditions for withholding | none | none | (inert) |
| s 1190(4) s 1081 does not apply | none | none | (inert) |
| s 1190(5) "specified" | none | none | `s 1190(5) the matter is specified` |
| s 1191(1)(a)-(b) regulations may create offences | none | none | (inert) |
| s 1191(2)(a)-(b)(i)-(ii) the ceiling on penalties | none | none | `s 1191(2) the greatest penalty that the regulations may provide` |
| s 1191(3) offences before 2 May 2022 | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1191(2) the greatest penalty that the regulations may provide` |
| Part 41 heading | none | none | (inert) |
| Chapter 1 heading | none | none | (inert) |
| cross-heading "Introductory" | none | none | (inert) |
| s 1192(1) application of Chapter 1 | none | none | `s 1192(1) this Chapter applies to the person` |
| s 1192(2)(a)-(b) surnames | the individual or partners: a PRIVILEGE to trade under the surname(s) and permitted additions | no one is named (the Chapter does not prevent it) | `s 1192(2) this Chapter prevents the business name` |
| s 1192(3)(a)-(c) the permitted additions | none | none | `s 1192(3) the addition is a permitted addition` |
| cross-heading "Sensitive words or expressions" | none | none | (inert) |
| s 1193(1)(a)-(c) name suggesting connection with government or public authority | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1193(1) the person contravenes the prohibition on a name suggesting connection with government or a public authority` |
| s 1193(2) "local authority", "public authority" | none | none | `s 1193(2) the body is a local authority`; `s 1193(2) the person or body is a public authority` |
| s 1193(3) affirmative resolution procedure | none | none | (inert) |
| s 1193(4) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1193(4) the person commits an offence` |
| s 1193(5) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1193(5) an officer of the body corporate commits an offence` |
| s 1193(6) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1193(6) the penalty for an offence under s 1193` |
| s 1194(1) other sensitive words or expressions | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1194(1) the person contravenes the prohibition on a name including a specified word or expression` |
| s 1194(2) approval after being made | none | none | (inert) |
| s 1194(3) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1194(3) the person commits an offence` |
| s 1194(4) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1194(4) an officer of the body corporate commits an offence` |
| s 1194(5) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1194(5) the penalty for an offence under s 1194` |
| s 1195(1)(a)-(b) regulations requiring the applicant to seek a view | none | none | (inert) |
| s 1195(2) the applicant must request the department or body | the Secretary of State: a CLAIM to the request and the statement | the applicant for approval: a DUTY | `s 1195(2) the applicant has complied with the requirement to request the view of the department or body`; `s 1195(2) the applicant must request the view of the department or body and submit a statement` |
| s 1195(3) the applicant must submit a statement and the response | the Secretary of State: a CLAIM to the request and the statement | the applicant for approval: a DUTY | `s 1195(3) the applicant has complied with the requirement to submit a statement and a copy of any response`; `s 1195(2) the applicant must request the view of the department or body and submit a statement` |
| s 1195(4) the Secretary of State may refuse to consider | the Secretary of State: a POWER to refuse to consider the application | the applicant: LIABILITY | `s 1195(4) the Secretary of State may refuse to consider the application for approval` |
| s 1195(5) "specified" | none | none | `s 1195(5) the matter is specified` |
| s 1196(1) approval to which s 1196 applies | the Secretary of State: a POWER to withdraw approval by notice for overriding public policy | the holder of the approval: LIABILITY | `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned` |
| s 1196(2) withdrawal of approval | the Secretary of State: a POWER to withdraw approval by notice for overriding public policy | the holder of the approval: LIABILITY | `s 1196(2) the approval may be withdrawn by notice in writing given to the person concerned` |
| s 1196(3) the notice states the date | the holder of the approval: a CLAIM to a notice stating the date | the Secretary of State: a DUTY | `s 1196(3) the notice meets the requirement to state a date`; `s 1196(3) the approval has been withdrawn` |
| s 1196A(1)(a)-(b) names suggesting connection with foreign governments | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1196A(1) the person contravenes the prohibition on a name suggesting connection with a foreign government or an international organisation` |
| s 1196A(2) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1196A(2) the person commits an offence` |
| s 1196A(3) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1196A(3) an officer of the body corporate commits an offence` |
| s 1196A(4) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1196A(4) the penalty for an offence under s 1196A` |
| cross-heading "Misleading names" | none | none | (inert) |
| s 1197(1)(a)-(b) regulations prohibiting names | none | none | (inert) |
| s 1197(2)(a)-(b) what the regulations may prohibit | none | none | (inert) |
| s 1197(3) "specified" | none | none | `s 1197(3) the matter is specified` |
| s 1197(4) negative resolution procedure | none | none | (inert) |
| s 1197(5) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1197(5) the person commits an offence` |
| s 1197(6) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1197(6) an officer of the body corporate commits an offence` |
| s 1197(7) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1197(7) the penalty for an offence under s 1197` |
| s 1198(1) misleading indication of activities | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1198(1) the person uses a name in contravention of the prohibition on a name giving a misleading indication of activities` |
| s 1198(2) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1198(2) the person commits an offence` |
| s 1198(3) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1198(3) an officer of the body corporate commits an offence` |
| s 1198(4) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1198(4) the penalty for an offence under s 1198` |
| cross-heading "Restrictions where a company has been required to change a name" | none | none | (inert) |
| s 1198A(1) a name that a company has been required to change | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1198A(1) the company uses the name in contravention of s 1198A` |
| s 1198A(2)(a)-(c) exceptions | the company: a PRIVILEGE (an exception to the prohibition) | no one is named (no-right) | `s 1198A(2) subsection (1) prevents the company using the name` |
| s 1198A(3)(a)-(b) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1198A(3)(a) the company commits an offence`; `s 1198A(3)(b) an officer of the company commits an offence` |
| s 1198A(4) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1198A(4) the penalty for an offence under s 1198A` |
| s 1198A(5) "company", "relevant direction" | none | none | `s 1198A(5) the direction is a relevant direction`; `s 1198A(5) the body is a company for the purposes of s 1198A` |
| s 1198B(1) a name that another company has been required to change | the public and the Secretary of State (not named as holder): a CLAIM that the name not be used | the person or company carrying on business: a DUTY (a prohibition) | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies`; `s 1198B(1) the other company uses the name in contravention of s 1198B` |
| s 1198B(2)(a)-(c) exceptions | the company: a PRIVILEGE (an exception to the prohibition) | no one is named (no-right) | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies`; `s 1198B(2) subsection (1) prevents the other company using the name` |
| s 1198B(3) not necessarily at the same time | none | none | `s 1198B(3) there is a person who has, or has had, a relevant relationship with both companies` |
| s 1198B(4)(a)-(b) "relevant relationship" | none | none | `s 1198B(4) the person has a relevant relationship with the company` |
| s 1198B(5)(a)-(b) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1198B(5)(a) the company commits an offence`; `s 1198B(5)(b) an officer of the company commits an offence` |
| s 1198B(6) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1198B(6) the penalty for an offence under s 1198B` |
| s 1198B(7) "company", "relevant direction" | none | none | `s 1198B(7) the direction is a relevant direction`; `s 1198B(7) the body is a company for the purposes of s 1198B` |
| cross-heading "Supplementary" | none | none | (inert) |
| s 1199(1) the sections s 1199 applies to | none | none | `s 1199(1) the saving has effect in relation to the provision` |
| s 1199(2)(a)-(b) business carried on before commencement | the person carrying on the existing business: an IMMUNITY from ss 1192 to 1197 | no one is named (DISABILITY) | `s 1199(2) sections 1192 to 1197 do not apply to the business` |
| s 1199(3)(a)-(b) business transferred: twelve months | the person carrying on the existing business: an IMMUNITY from ss 1192 to 1197 | no one is named (DISABILITY) | `s 1199(3) sections 1192 to 1197 do not apply to the business carried on under that name on the date` |
| s 1199(4)(a)-(b) "lawful business name" | none | none | `s 1199(4) the name is a lawful business name` |
| s 1199A(1)(a)-(b) notice exempting a person from a prohibition | the Secretary of State: a POWER to lift a prohibition by notice; the person: a favourable LIABILITY | the person named in the notice: an IMMUNITY once it is given | `s 1199A(1) the prohibitions of this Chapter do not apply to the business under the name` |
| s 1199A(2)(a)-(b)(i)-(ii) "crime" and "serious" | none | none | `s 1199A(2)(a) the conduct is crime`; `s 1199A(2)(b) the crime is serious` |
| Chapter 2 heading | none | none | (inert) |
| cross-heading "Introductory" | none | none | (inert) |
| s 1200(1) application of Chapter 2 | none | none | `s 1200(1) the person is a person to whom this Chapter applies` |
| s 1200(2)(a)-(b)(i)-(ii) "business name" | none | none | `s 1200(2) the name is a business name` |
| s 1200(3)(a)-(c) the permitted additions | none | none | `s 1200(3) the addition is a permitted addition` |
| s 1201(1)(a)-(b) "the information required by this Chapter" | none | none | `s 1201(1) the disclosure contains the information required by this Chapter` |
| s 1201(2) address in the United Kingdom | none | none | `s 1201(2) the address meets the requirement as to place` |
| s 1201(3) address where there is no place of business in the United Kingdom | none | none | `s 1201(3) the address meets the requirement as to delivery` |
| cross-heading "Disclosure requirements" | none | none | (inert) |
| s 1202(1)(a)-(d) disclosure on business documents | persons who do business with the individual or partnership (customers, suppliers): a CLAIM to the information | the individual or partnership: a DUTY | `s 1202(1) the requirement to state the information applies to the document`; `s 1202(1) the person has complied with the requirement to state the information on the document`; `s 1202(1) the person must state the information on the document` |
| s 1202(2) disclosure on request | persons who do business with the individual or partnership (customers, suppliers): a CLAIM to the information | the individual or partnership: a DUTY | `s 1202(2) the person has complied with the requirement to give the information on request`; `s 1202(2) the person must give the information to a person who asks` |
| s 1202(3) regulations: specified form of notices | none | none | (inert) |
| s 1202(4) negative resolution procedure | none | none | (inert) |
| s 1203(1) exemption for a partnership of more than 20 persons | the partnership of more than 20 persons: an IMMUNITY from s 1202(1) if the conditions are met | persons dealing with it: a DISABILITY (they cannot insist on names on the document) | `s 1203(1) the exemption applies to the document` |
| s 1203(2)(a)-(c) the conditions | none | none | `s 1203(2) the conditions for the exemption are met` |
| s 1203(3) inspection of the list | any person: a CLAIM to inspect the list during office hours | the partnership: a DUTY | `s 1203(3) the person may inspect the list` |
| s 1203(4) offence | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1203(4) the member of the partnership commits an offence` |
| s 1203(5) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1203(5) the penalty for an offence under s 1203` |
| s 1204(1)(a)-(b) disclosure at business premises | customers and suppliers: a CLAIM to a prominent notice | the individual or partnership: a DUTY | `s 1204(1) the requirement to display the notice applies to the premises`; `s 1204(1) the person has complied with the requirement to display the notice`; `s 1204(1) the person must display the notice in the premises` |
| s 1204(2) regulations: specified form of notices | none | none | (inert) |
| s 1204(3) negative resolution procedure | none | none | (inert) |
| cross-heading "Consequences of failure to make required disclosure" | none | none | (inert) |
| s 1205(1) offence of failure to make required disclosure | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1205(1) the person commits an offence` |
| s 1205(2) body corporate: officers in default | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | every officer of the body corporate who is in default: LIABILITY to conviction and the stated penalty | `s 1205(2) an officer of the body corporate commits an offence` |
| s 1205(3) penalty | the Crown: a POWER to sentence (the text names no court) | the person convicted: LIABILITY to the penalty stated | `s 1205(3) the penalty for an offence under s 1205` |
| s 1205(4) the requirements include those of regulations | none | none | `s 1205(4) the requirement is a requirement of s 1202 or s 1204` |
| s 1206(1) proceedings to which s 1206 applies | none | none | `s 1206(1) this section applies to the proceedings` |
| s 1206(2)(a)-(b) dismissal unless just and equitable | the defendant: a POWER (to have the proceedings dismissed by showing a lost claim or financial loss) | the claimant in breach: LIABILITY to dismissal unless the court finds it just and equitable to continue | `s 1206(2) the proceedings shall be dismissed` |
| s 1206(3) the requirements include those of regulations | none | none | `s 1206(3) the requirement is a requirement of this Chapter` |
| s 1206(4) no effect on rights against another person | any person: an IMMUNITY (rights against another person are unaffected) | no one is named (DISABILITY) | `s 1206(4) the section affects the right to enforce rights against another person` |
| Chapter 3 heading | none | none | (inert) |
| s 1207 application of general provisions about offences | the Crown (the text names no prosecutor or court): a CLAIM that the offence be punished | the person named: LIABILITY to conviction and the stated penalty | `s 1207 the provision applies in relation to the offence` |
| s 1208 lead-in "In this Part" | none | none | (inert) |
| s 1208 "business" | none | none | `s 1208 the activity is a business` |
| s 1208 "initial" | none | none | `s 1208 the abbreviation is an initial` |
| s 1208 "partnership" (a)-(b) | none | none | `s 1208 the arrangement is a partnership` |
| s 1208 "surname" | none | none | `s 1208 the surname of the person` |

## Marginal readings for a lawyer (coa25)

Every branch below rests on one of the two readings the brief marks "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not (the case outside the limit answers NOTHING). The other reading is stated for each.

| functions | branch | rests on | the other reading |
| --- | --- | --- | --- |
| `s 1134`, `s 1136(2)`, `s 1141`, `s 1143(1)`, `s 1151(3)`, `s 1152(2)`-`(5)`, `s 1182(3)`-`(4)`, `s 1183`, `s 1193(2)`, `s 1199(4)`, `s 1199A(2)`, `s 1200(2)`-`(3)`, `s 1201(1)`, `s 1208 "partnership"` | `JUST FALSE` for a case outside a "means" / "are" / "are to" list | (a) and the 2026-11-05 ruling on delegated definitions | NOTHING where the text does not say "only" |
| `s 1137(5)`, `s 1138(4)`, `s 1140(6)`, `s 1140(8)`, `s 1143(4)`, `s 1145(3)`, `s 1146(4)`, `s 1150(3)`, `s 1151(2)`, `s 1192(2)`, `s 1198A(2)`, `s 1198B(2)`, `s 1199(3)`, `s 1206(4)` | `JUST FALSE` for the flat negatives ("may not", "does not apply", "shall not be read as preventing") | (a) and N2 option A | NOTHING: a flat negative reaches only the case it names |
| `s 1145(1)`, `s 1146(2)`-`(3)`, `s 1157(3)` (the "Where" limbs), `s 1182(2)`, `s 1187(3)`, `s 1203(2)`, `s 1206(2)` | `JUST FALSE` when an "if" or "where" of a grant or definition fails | (a) and the 2026-11-05 ruling (b) | NOTHING: "if" does not say "only if" |
| `s 1139(2) first text` | `JUST FALSE` for service at a place of business when the "if" of paragraph (b) is not met (an authorised person exists and accepts service) | (a) | NOTHING |
| `s 1135(3)`, `s 1138(2)`, `s 1145(4)`, `s 1155(1)`, `s 1193(4)`, `s 1194(3)`, `s 1196A(2)`, `s 1197(5)`, `s 1198(2)`, `s 1198A(3)(a)`, `s 1198B(5)(a)`, `s 1205(1)` | `JUST FALSE` for no contravention (the offence is defined by it) | (a): "who contravenes" read like "if" | NOTHING |
| `s 1135(3)`, `s 1138(2)`, `s 1145(4)`, `s 1193(5)`, `s 1194(4)`, `s 1196A(3)`, `s 1197(6)`, `s 1198(3)`, `s 1198A(3)(b)`, `s 1198B(5)(b)`, `s 1205(2)` | NOTHING for an officer not in default | (b): "every officer ... who is in default" is a named complement | `JUST FALSE` |
| `s 1193(1)`, `s 1194(1)` | NOTHING when the Secretary of State has approved the name | (b): "without the approval" | `JUST FALSE` (no contravention) |
| `s 1203(4)`, `s 1205(1)` | NOTHING when the person had a reasonable excuse | (b): "without reasonable excuse" | `JUST FALSE` |
| `s 1139(1)`, `s 1139(2) second text`, `s 1139(4)`, `s 1150(2)`, `s 1153(1)`, `s 1154(3)`, `s 1199(2)`, `s 1203(3)` | NOTHING outside the limit each grant states | (b) | `JUST FALSE` outside the limit |
| `s 1140(2)`, `s 1149`, `s 1154(1)`-`(2)`, `s 1202(1)`, `s 1207`, `s 1199(1)` | NOTHING outside a list not closed with "only" | (b) | `JUST FALSE` |
| `s 1199A(1)` | NOTHING when the notice was not given or the Secretary of State is satisfied of neither ground | (b): a grant whose gate fails (fork F25) | `JUST FALSE` (an unmet "if") |
| `s 1203(1)` | `JUST FALSE` when the conditions of subsection (2) are unmet; NOTHING for a partnership of 20 persons or fewer | (a) for the unmet "if"; (b) with ruling (c) of 2026-11-05 for the threshold (fork F26) | NOTHING when the conditions are unmet |
| `s 1157(1)` | NOTHING when the court is not satisfied of any limb of the "if" | (b): a power limited by its own wording (fork F19) | `JUST FALSE` (a failed "if" as the text's own no) |
| `s 1157(3)` (the "if" limb) | NOTHING when the judge is not satisfied that the defendant ought to be relieved | (b) (fork F27) | `JUST FALSE` |
| `s 1196(2)` | NOTHING when it does not appear to the Secretary of State that overriding considerations of public policy require the withdrawal | (b) (fork F28) | `JUST FALSE` |
| `s 1204(1) the requirement to display the notice applies to the premises` | `JUST FALSE` for premises where the business is not carried on, and for premises to which no customer or supplier has access | (a) with ruling (b) of 2026-11-05, both limbs read alike (fork F24) | Limb (b) answers NOTHING (a scope limit with no "only", ruling (c)), or both limbs NOTHING |
| `s 1151(1)` | `JUST TRUE` when every "only if" limb holds | "only if" read as the complete test (fork F8) | NOTHING |
| `s 1135(1)` | NOTHING when the records are not arranged as the directors think fit | (b): "may be arranged in such manner as the directors ... think fit" | `JUST FALSE` |

## Seams (coa25)

**Brief and PLAN.md differ on one point, and the brief governs.** The brief says layer 1 imports the keel's `coa-core.l4` and `coa-definitions.l4`; PLAN.md section 4.1 says a part never imports `coa-definitions` and takes the keel's answers as inputs named for the section that gives them. This part imports `coa-core` only (the brief does not require the second import) and takes every keel and other-part answer as an input under PLAN.md's name, so that the lead wires them at the merge and no name is defined twice.

Inputs taken (each is one input per seam, declared once in the function that asks):

| input name | type | asked by | the part or keel that answers it |
| --- | --- | --- | --- |
| `s 2(1) the provision is one of the Companies Acts` | MAYBE BOOLEAN | `s 1134` | keel (`coa-definitions.l4`) |
| `s 1121 the officer is in default` | MAYBE BOOLEAN | every offence function against an officer (ss 1135(3), 1138(2), 1145(4), 1193(5), 1194(4), 1196A(3), 1197(6), 1198(3), 1198A(3)(b), 1198B(5)(b), 1205(2)) | coa24 |
| `s 790C the person is a registrable person or a registrable relevant legal entity` | MAYBE BOOLEAN | `s 1140(2)` | coa17 |
| `sch 4 ... in accordance with Schedule 4`, `sch 5 ... in accordance with Schedule 5` | MAYBE BOOLEAN | `s 1144 the document or information has been sent or supplied` | coa29 |
| `s 1173(1) the day is a working day for the company` | FUNCTION FROM DATE TO BOOLEAN | `s 1147(5)`, `s 1147(2)`, `(3)` | keel (the seat builds it from Saturdays, Sundays and a list of dates; a restatement forced by the brief's rule that the seat imports layer 1 only) |
| `s 1173(1) the person is a body corporate or a corporation` | MAYBE BOOLEAN | `s 1148(1) the body is a company` | keel |
| `s 1212 the person is eligible for appointment as a statutory auditor` | MAYBE BOOLEAN | `s 1150(1)` | coa26 |
| `s 1162 the undertaking is a parent undertaking of the company`, `... a subsidiary undertaking of the company`, `... a subsidiary undertaking of a parent undertaking of the company` | BOOLEAN | `s 1151(3)` | keel |
| `s 1199 sections 1192 to 1197 do not apply to the business`, `s 1199A(1) the prohibitions of this Chapter do not apply to the business under the name` | MAYBE BOOLEAN | `s 1193(1)`, `s 1194(1)`, `s 1196A(1)`, `s 1197(5)`, `s 1198(1)`, `s 1198A(1)`, `s 1198B(1)` | this part: `s 1199(2)`, `s 1199(3)`, `s 1199A(1)` (a seam inside the part: wire them in the merged seat) |
| `s 1203(1) the exemption applies to the document` | MAYBE BOOLEAN | `s 1202(1)` | this part: `s 1203(1)` |

**Answers other parts need from this part**, under the names PLAN.md gives them: `s 1141 the address is a service address`, `s 1144 the document or information has been sent or supplied`, `s 1147 the day the document is treated as delivered` (a MAYBE DATE: the day of the deemed instant; see F7), `s 1156(1) the courts that are "the court" in the part of the United Kingdom` (a LIST of the court names; the core `Court` party stays generic), `s 1142 the address to be given is a service address`, `s 1148(1)` (address, company, document), `s 1134` (company records), `s 1146` (authentication). **A seam the plan lacks:** s 1140(2)(aa) needs s 790C (coa17); s 1150(1)(a) needs s 1212 (coa26); s 1151(3) needs s 1162 (the keel); ss 1193 to 1198B need the savings of s 1199 and the notice of s 1199A, which are this part's own. PLAN.md's seam list for coa25 names s 1136: s 702, s 720, s 743, s 805, s 809, s 859Q, s 114, s 228, s 237, s 358: they are section numbers in a list (a plain STRING asked of `s 1136(2)`), not answers another part computes.

## Findings: what the text turns out to say

1. Section 1139 appears with two versions of subsections (2) and (3) in this text (lines 16255-16258 and 16259-16264); both are encoded and asserted. Asserted.
2. Section 1154(1) lists three appointments, but 1154(2)(b) and (bb) also name an interim manager under s 33 of the Charities Act (Northern Ireland) 2008 and a receiver or manager under that section: the duty of (1) does not reach them, so it answers NOTHING for them while (2) still says who gives the notice. Asserted.
3. The two definitions of "relevant direction" differ: s 1198A(5) lists directions under ss 67, 75, 76, 76A and 76B, s 1198B(7) lists ss 67, 75, 76A and 76B (no s 76). A direction under s 76 is relevant for s 1198A and not for s 1198B. Asserted, in both modules and in the seat cases.
4. Section 1199(1) says the saving "has effect in relation to" ss 1192 to 1196 and s 1197: it does not name s 1196A (the foreign-government prohibition), s 1198, s 1198A or s 1198B, so the saving of an existing lawful business name does not reach them on the text. The functions for those prohibitions do not take the s 1199 answer; `s 1199(1)` answers NOTHING for a provision outside its list. Asserted.
5. Section 1203(1) exempts "a partnership of more than 20 persons": a partnership of 20 is outside it (NOTHING), 21 is within. Asserted at both edges.
6. Section 1155(1) "within the period of 14 days after the appointment": notice on the 14th day after is in time and on the 15th is an offence; the day of appointment is not counted (fork F3). Asserted on 15 and 16 June 2026 for an appointment on 1 June, and across a year end.
7. Sections 1186(3) and 1191(3) substitute "six months" for "the general limit in a magistrates' court" for an offence committed before 2 May 2022: an offence on 1 May 2022 has the six-month ceiling and one on 2 May 2022 the general limit. Asserted at both edges.
8. Section 1147(5) counts hours, not days, and ignores "any part of a day that is not a working day": 48 hours from Friday 10:00 end on Tuesday 10:00 (a bank holiday on the Monday moves them to Wednesday). PLAN.md types the seam answer as a DATE; the encoding gives the deemed instant and the day of it (fork F7). Asserted.
9. Section 1205(2) speaks of an offence "committed by a body corporate" although Chapter 2 applies to an individual or a partnership (s 1200(1)): the text does not say how a body corporate comes within Chapter 2 (a partner may be one, s 1200(2)(b)(ii)). Encoded as written. Not asserted beyond the shape of the rule.
10. Section 1193(1)(a) names "Her Majesty's Government, any part of the Scottish administration, the Welsh Assembly Government or Her Majesty's Government in Northern Ireland": the wording of the rendering is encoded as it stands (a constructor); the text does not say whether later renamings are meant. Not asserted.
11. Sections 1175, 1189, 1156(3) and (4) and five entries of s 1136(2) are shown as rows of dots and are `repealed or blank` rows; ss 1190(1) and 1191(1) show an inline "..." where words were omitted: the quote lines copy them as they stand.
12. A silent error of this agent's own was caught by the tests, not by `l4 check`: `NOT a OR b` in `s 1195(3)` read as `NOT (a OR b)` (the brief's trap), a failed assertion at the first run of `coa25-tests-names-ch1.l4`; fixed by bracketing. All the other `NOT`s were then checked by reading each one. A measured confirmation is under "What the stable binary does not accept".
13. Sections 1202(1) and 1203(1) refer to each other ("subject to section 1203", "Section 1202(1) ... does not apply ... if the following conditions are met"): `s 1202(1) the requirement ... applies` takes the s 1203(1) answer as an input and answers `JUST FALSE` when the exemption holds.
14. Section 1206(2) turns on what the defendant "shows" and on what the court is "satisfied" of: both are plain inputs; the court's satisfaction that it is just and equitable lets the proceedings continue (`JUST FALSE` for "must be dismissed"). Asserted.

## What the stable binary does not accept, and what it does (coa25)

Measured on 2026-11-13 with `L4_BIN` (1.6.110) and `L4_MAIN` (1.6.109), identical results on both:

- **A DEONTIC value cannot be compared.** `#ASSERT <rule> EQUALS <rule>` for a regulative rule prints "assertion could not be evaluated: Trying to check equality on types that do not support it". So no regulative rule is asserted: each is run with `#TRACE` (16 traces in the test files, outcomes written beside each and read by eye; they are identical on both builds) and has a decision-function twin that is asserted. `check.sh` counts assertions only, so a trace outcome is not in its numbers.
- **`NOT a OR b` reads as `NOT (a OR b)`**: with `a` and `b` both true, `NOT a OR b` is false and the assertion `... EQUALS TRUE` fails (the brief's trap, measured on both builds). Every `NOT` in the files was bracketed or checked.
- **Accepted, and used:** `MAYBE BOOLEAN`, `MAYBE DATE`, `MAYBE STRING`, `MAYBE Penalty` results; a recursive function with a numeric fuel; a function-typed `GIVEN` in a rule that is not exported; a lambda argument (`GIVEN d YIELD ...`); `LIST OF` an enum type as a result and as an argument; `elem` over a list of enum values; `PROVIDED` in a regulative rule with a `GIVEN` party; `PARTY` given as a `GIVEN`; `§` headings in a module whose names an importer uses; a record built with `WITH` that carries `MAYBE` fields; `Period WITH ... IS (IF ... THEN ... ELSE ...)`; commas, parentheses and the characters `"` and `'` inside backtick names; `@export` over a `DECIDE` that returns a record or a list.
- **A quote line of dots is rejected by `srcrefs.py`** ("quotation has no text"): the quote runs skip the dot lines (gaps inside a locator range are allowed) and the dots rows are `repealed or blank` rows.
- **Not used (the brief forbids them and the two supplied builds accept them anyway):** `REFUSE`, `#ASSERT REFUSED`, `YMD`; the modules use `NOTHING` and `Date day month year` only.

## What `check.sh` printed

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (target `main`: every module is also run with the second stable build and the four counts compared). `expected_failed` is empty: no assertion is meant to fail. The keel's two modules appear because they sit in the same folder (the keel's own tests module is not among the files supplied to this sandbox).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa25-cases-seat.l4                            0       186       0        0         0 |      0       186       0        0  same
coa25-communications.l4                        0         0       0        0         0 |      0         0       0        0  same
coa25-names-ch1.l4                             0         0       0        0         0 |      0         0       0        0  same
coa25-names-ch2.l4                             0         0       0        0         0 |      0         0       0        0  same
coa25-notices-courts.l4                        0         0       0        0         0 |      0         0       0        0  same
coa25-part39.l4                                0         0       0        0         0 |      0         0       0        0  same
coa25-part40.l4                                0         0       0        0         0 |      0         0       0        0  same
coa25-records.l4                               0         0       0        0         0 |      0         0       0        0  same
coa25-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa25-service.l4                               0         0       0        0         0 |      0         0       0        0  same
coa25-tests-communications.l4                  0       114       0        0         0 |      0       114       0        0  same
coa25-tests-names-ch1.l4                       0       244       0        0         0 |      0       244       0        0  same
coa25-tests-names-ch2.l4                       0       127       0        0         0 |      0       127       0        0  same
coa25-tests-notices-courts.l4                  0        62       0        0         0 |      0        62       0        0  same
coa25-tests-part39.l4                          0         6       0        0         0 |      0         6       0        0  same
coa25-tests-part40.l4                          0        63       0        0         0 |      0        63       0        0  same
coa25-tests-records.l4                         0        86       0        0         0 |      0        86       0        0  same
coa25-tests-service.l4                         0        70       0        0         0 |      0        70       0        0  same
coa25-tests-valuation.l4                       0        75       0        0         0 |      0        75       0        0  same
coa25-valuation.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (22 modules)                             0      1033       0        0           |      0      1033       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline numbers this replaced: before any module of this part was written, the folder held the keel's `coa-core.l4` and `coa-definitions.l4` only (0 errors, 0 assertions). `python3 -I srcrefs.py check --strict ukpga-2006-46.txt <each layer-1 file>` reports 0 problems for all nine layer-1 modules (see `PROGRESS.md` for the counts per file); `--refs` reports 0 problems too.

## Open questions for a domain expert

- Which text of s 1139(2) and (3) is in force (fork F1)? The other pair of functions can be deleted.
- Is "A person who contravenes this section commits an offence" (and "If a company fails ... an offence is committed") the definition of the offence, so that no contravention is a plain no (marginal reading (a)), while an officer not in default is "not covered" (marginal reading (b))? The two are asymmetric on purpose (fork F17).
- Do ss 1193(1) and 1194(1) answer NOTHING (not JUST FALSE) where the Secretary of State has approved the name ("without the approval")?
- Does the saving of s 1199 reach ss 1196A, 1198, 1198A and 1198B (finding 4)?
- Is the omission of s 76 from the "relevant direction" of s 1198B(7), and of the Northern Ireland appointments from s 1154(1), intended (findings 2 and 3)?
- Is the seat for Chapter 2 of Part 41 (the individual or partner who carries on the business, and the customer or supplier) the right one (fork F21)?
- Should the "first text" and "second text" seat question for s 1139(2) ask the user, or should the lead choose one at the merge?
- Is it right that a "has complied" function answers `JUST TRUE` where a duty does not engage (fork F5), or should it answer NOTHING?

## Copied modules

None. The layer-1 modules import `coa-core` (the keel's, read-only, unchanged) and no other encoding. `NEEDS-CORE.md` lists the types this part declared under its own prefix that the lead may hoist.
